"""The Miura map and momentum: why no defect without defect fields joins mKdV to KdV
by the Miura map, and how the Wahlquist-Estabrook defect of [3] fuses two Miura maps.

Bulk Lagrangians (potential form): mKdV L_m = q_x q_t/2 - q_x^4/2 - q_xx^2/2 with v = q_x,
KdV L_K = p_x p_t/2 - p_x^3 - p_xx^2/2 with u = p_x (the KdV Lagrangian of [3], eq. 9.3).
Self-contained: imports only SymPy.  One PASS or FAIL line per check.
"""

import sympy as sp

ok = True


def report(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


x, t, kap, lam, w = sp.symbols("x t kappa lambda w")
v = sp.Function("v")(x, t)
q = sp.Function("q")(x, t)
p = sp.Function("p")(x, t)

Lm = q.diff(x) * q.diff(t) / 2 - q.diff(x) ** 4 / 2 - q.diff(x, 2) ** 2 / 2
Lk = p.diff(x) * p.diff(t) / 2 - p.diff(x) ** 3 - p.diff(x, 2) ** 2 / 2
vq, up = q.diff(x), p.diff(x)
ELm = sp.euler_equations(Lm, [q], [x, t])[0].lhs
ELk = sp.euler_equations(Lk, [p], [x, t])[0].lhs
report("L_m gives v_t = 6 v^2 v_x - v_xxx and L_K gives u_t = 6 u u_x - u_xxx",
       sp.simplify(ELm - (-vq.diff(t) + 6 * vq ** 2 * vq.diff(x) - vq.diff(x, 3))) == 0
       and sp.simplify(ELk - (-up.diff(t) + 6 * up * up.diff(x) - up.diff(x, 3))) == 0)

vt = 6 * v ** 2 * v.diff(x) - v.diff(x, 3)
u = v ** 2 + v.diff(x)
ut = sp.diff(u, t).subs(sp.Derivative(v, t), vt).doit()
report("Miura: if v solves mKdV then u = v^2 + v_x solves KdV",
       sp.simplify(sp.expand(ut - (6 * u * u.diff(x) - u.diff(x, 3)))) == 0)

T01m = -sp.diff(Lm, q.diff(t)) * q.diff(x)
T01k = -sp.diff(Lk, p.diff(t)) * p.diff(x)
report("momentum densities (Lemma 2.1): T^01 = -v^2/2 for mKdV and -u^2/2 for KdV",
       sp.simplify(T01m + vq ** 2 / 2) == 0 and sp.simplify(T01k + up ** 2 / 2) == 0)

report("u^2/2 = v^4/2 + v_x^2/2 + D_x(v^3/3): Miura carries the KdV momentum density to the mKdV energy density",
       sp.expand(u ** 2 / 2 - (v ** 4 / 2 + v.diff(x) ** 2 / 2) - sp.diff(v ** 3 / 3, x)) == 0)

dens = (kap - sp.Rational(1, 2)) * vq ** 2 + vq ** 4 / 2 + vq.diff(x) ** 2 / 2
E = sp.expand(sp.euler_equations(dens, [q], [x, t])[0].lhs)
report("(kappa - 1/2) v^2 + v^4/2 + v_x^2/2 is a total x-derivative for no kappa (its Euler derivative "
       "contains q_xxxx)", E.coeff(q.diff(x, 4)) != 0)

up_, um_ = v ** 2 + v.diff(x) + lam, v ** 2 - v.diff(x) + lam
report("fusion: for u_pm = v^2 pm v_x + lambda, u_+^2/2 - u_-^2/2 = D_x(2 v^3/3 + 2 lambda v)",
       sp.expand(up_ ** 2 / 2 - um_ ** 2 / 2 - sp.diff(2 * v ** 3 / 3 + 2 * lam * v, x)) == 0)
report("with v = (p-q)/2: 2v^3/3 + 2 lambda v = lambda (p-q) + (p-q)^3/12, the defect momentum (9.13) of [3], "
       "and u_+ + u_- = 2 lambda + (p-q)^2/2 is (9.12)",
       sp.expand((2 * v ** 3 / 3 + 2 * lam * v).subs(v, w / 2) - (lam * w + w ** 3 / 12)) == 0
       and sp.expand((up_ + um_).subs(v, w / 2).doit() - (2 * lam + w ** 2 / 2)) == 0)

raise SystemExit(0 if ok else 1)
