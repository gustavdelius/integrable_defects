"""Small jet-calculus helpers for the general-framework checks.

Two settings are used.

* Boundary jets (``TJets``): functions of t alone, evaluated at the defect.
  A function named ``f`` has jet symbols ``f_0, f_1, ...`` with ``f_k`` the k-th
  time derivative.  ``Dt`` is the total time derivative and ``euler`` the
  t-Euler operator.  An expression R with no explicit t is a total time
  derivative of a local function exactly when every t-Euler derivative of R
  vanishes and R vanishes at the zero jet (Olver, Thm 4.7).

* Space-time jets of an evolution system (``XJets``): densities are functions
  of the x-jets of the dependent variables; ``Dt`` uses the evolution
  equations.  A density Q is conserved exactly when the x-Euler derivatives of
  Dt(Q) vanish.  Q is trivial (a total x-derivative) exactly when its own
  x-Euler derivatives vanish.
"""

import sympy as sp



def is_zero(expr, trials=3):
    """Exact zero test.  expand() decides most cases; a nonzero value at a random
    rational point proves nonzero-ness; simplify() is used only for expressions
    that are numerically zero but not expanded to zero."""
    import random
    e = sp.expand(expr)
    if e == 0:
        return True
    syms = sorted(e.free_symbols, key=str)
    rng = random.Random(12345)
    for _ in range(trials):
        pt = {x: sp.Rational(rng.randint(1, 97), rng.randint(98, 197)) for x in syms}
        try:
            val = complex(sp.N(e.xreplace(pt), 30))
        except (TypeError, ValueError, ZeroDivisionError):
            continue
        if abs(val) > 1e-12:
            return False
    return sp.simplify(e) == 0


class TJets:
    """Jets of boundary functions of t."""

    def __init__(self, names, order):
        self.names = list(names)
        self.order = order
        self.sym = {n: sp.symbols(f"{n}_0:{order + 1}") for n in self.names}
        self.rules = {}  # symbol -> replacement (constraint elimination)

    def __getitem__(self, name):
        return self.sym[name]

    def all_symbols(self):
        return [s for n in self.names for s in self.sym[n]]

    def Dt(self, expr):
        out = 0
        for n in self.names:
            js = self.sym[n]
            for k in range(self.order):
                d = sp.diff(expr, js[k])
                if d != 0:
                    out += d * js[k + 1]
            if sp.diff(expr, js[self.order]) != 0:
                raise ValueError(f"jet buffer too short for {n}")
        return out

    def Dt_n(self, expr, n):
        for _ in range(n):
            expr = self.Dt(expr)
        return expr

    def var(self, expr, name):
        """t-variational derivative of the functional with density expr."""
        js = self.sym[name]
        out = 0
        for k in range(self.order + 1):
            d = sp.diff(expr, js[k])
            if d != 0:
                out += (-1) ** k * self.Dt_n(d, k)
        return out

    def eliminate(self, name, k0, expr0, upto):
        """Impose name_k0 = expr0 together with its time derivatives."""
        js = self.sym[name]
        e = expr0
        for k in range(k0, upto + 1):
            self.rules[js[k]] = e
            e = self.Dt(e)

    def reduce(self, expr, rounds=6):
        for _ in range(rounds):
            new = expr.xreplace(self.rules)
            if new == expr:
                return expr
            expr = new
        return expr

    def is_total_derivative(self, expr, free_names):
        """True when expr (already reduced) is Dt of a local function."""
        expr = sp.expand(expr)
        for n in free_names:
            e = sp.simplify(self.var(expr, n))
            if e != 0:
                return False, (n, e)
        # A total derivative vanishes at every stationary jet (all t-derivatives
        # zero).  Evaluate at a generic stationary jet to exclude a constant.
        primes = [sp.Rational(1, 3), sp.Rational(2, 7), sp.Rational(5, 11), sp.Rational(3, 13),
                  sp.Rational(4, 17), sp.Rational(6, 19), sp.Rational(7, 23), sp.Rational(8, 29)]
        point = {}
        for i, n in enumerate(self.names):
            point[self.sym[n][0]] = primes[i % len(primes)]
            for s in self.sym[n][1:]:
                point[s] = 0
        val = sp.simplify(expr.xreplace(point))
        return val == 0, ("value at a stationary jet", val)


class XJets:
    """x-jets of an evolution system u_t = F[u]."""

    def __init__(self, names, order):
        self.names = list(names)
        self.order = order
        self.sym = {n: sp.symbols(f"{n}x0:{order + 1}") for n in self.names}
        self.flow = {}

    def __getitem__(self, name):
        return self.sym[name]

    def Dx(self, expr):
        out = 0
        for n in self.names:
            js = self.sym[n]
            for k in range(self.order):
                d = sp.diff(expr, js[k])
                if d != 0:
                    out += d * js[k + 1]
            if sp.diff(expr, js[self.order]) != 0:
                raise ValueError(f"x-jet buffer too short for {n}")
        return out

    def Dx_n(self, expr, n):
        for _ in range(n):
            expr = self.Dx(expr)
        return expr

    def set_flow(self, name, rhs):
        self.flow[name] = rhs

    def _flow_x(self, name, k):
        key = (name, k)
        if not hasattr(self, "_cache"):
            self._cache = {}
        if key not in self._cache:
            self._cache[key] = self.flow[name] if k == 0 else sp.expand(self.Dx(self._flow_x(name, k - 1)))
        return self._cache[key]

    def Dt(self, expr):
        out = 0
        for n in self.names:
            for k, s in enumerate(self.sym[n]):
                d = sp.diff(expr, s)
                if d != 0:
                    out += d * self._flow_x(n, k)
        return out

    def euler(self, expr, name):
        js = self.sym[name]
        out = 0
        for k in range(self.order + 1):
            d = sp.diff(expr, js[k])
            if d != 0:
                out += (-1) ** k * self.Dx_n(d, k)
        return out

    def is_trivial(self, expr):
        return all(is_zero(self.euler(expr, n)) for n in self.names)

    def is_conserved(self, expr):
        dt = sp.expand(self.Dt(expr))
        return all(is_zero(self.euler(dt, n)) for n in self.names)


def report(label, ok, detail=""):
    print(("PASS" if ok else "FAIL") + f": {label}" + (f" -- {detail}" if detail and not ok else ""))
    return ok


# ---------------------------------------------------------------------------
# Truncated Laurent series in a parameter, for formal-branch computations.
# A series is a dict {power: coefficient}; powers above N are dropped.

def _ser(expr, e, N):
    if not expr.has(e):
        return {0: expr}
    if expr == e:
        return {1: sp.Integer(1)}
    if expr.is_Add:
        out = {}
        for a in expr.args:
            for k, v in _ser(a, e, N).items():
                out[k] = out.get(k, 0) + v
        return out
    if expr.is_Mul:
        out = {0: sp.Integer(1)}
        for a in expr.args:
            out = _mul(out, _ser(a, e, N), N)
        return out
    if expr.is_Pow:
        base, ex = expr.args
        if ex.has(e):
            raise NotImplementedError(expr)
        s = _ser(base, e, N)
        if ex.is_Integer and ex >= 0:
            out = {0: sp.Integer(1)}
            for _ in range(int(ex)):
                out = _mul(out, s, N)
            return out
        return _power(s, ex, N)
    if isinstance(expr, (sp.sin, sp.cos, sp.exp, sp.log, sp.sinh, sp.cosh)):
        s = _ser(expr.args[0], e, N)
        if any(k < 0 for k, v in s.items() if v != 0):
            raise ValueError("function of a series with a pole")
        c0 = s.get(0, 0)
        d = {k: v for k, v in s.items() if k > 0}
        f = expr.func
        x = sp.Symbol("_x")
        out = {}
        term = {0: sp.Integer(1)}
        for j in range(N + 1):
            if j > 0:
                term = _mul(term, d, N)
                if not term:
                    break
            cj = sp.diff(f(x), x, j).subs(x, c0) / sp.factorial(j)
            for k, v in term.items():
                out[k] = out.get(k, 0) + cj * v
        return out
    raise NotImplementedError(type(expr))


def _mul(a, b, N):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            if i + j <= N:
                out[i + j] = out.get(i + j, 0) + x * y
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def _power(s, ex, N):
    s = {k: sp.expand(v) for k, v in s.items() if sp.expand(v) != 0}
    m = min(s)
    lead = s[m]
    shift = m * ex
    if not sp.Integer(shift) == shift or not sp.sympify(shift).is_Integer:
        raise ValueError("non-integer leading power")
    rest = {k - m: sp.expand(v / lead) for k, v in s.items() if k != m}
    # (lead e^m)^ex (1 + rest)^ex, binomial series
    depth = N - int(shift)
    out = {}
    term = {0: sp.Integer(1)}
    j = 0
    while True:
        cj = sp.binomial(ex, j)
        for k, v in term.items():
            if k <= depth:
                out[k] = out.get(k, 0) + cj * v
        j += 1
        if j > depth + 1:
            break
        term = _mul(term, rest, depth)
        if not term:
            break
    lp = lead ** ex
    return {k + int(shift): sp.expand(lp * v) for k, v in out.items() if k + int(shift) <= N}


def series_trunc(expr, e, N, guard=6):
    """Truncated expansion to order N.  Intermediate products are kept to order
    N + guard, which must bound the total pole order of the factors involved."""
    s = _ser(sp.sympify(expr), e, N + guard)
    return sp.expand(sum(v * e ** k for k, v in s.items() if k <= N))
