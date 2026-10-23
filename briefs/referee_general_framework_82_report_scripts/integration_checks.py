"""Integration checks for briefs/referee_general_framework_82_report.md.

Written from the definitions of defect-integrability/general_framework/paper.md;
imports only SymPy (nothing from the referee or from the paper's scripts).
One PASS or FAIL line per check.

Conventions (paper Section 8.2): bulk L = |phi_t|^2/2 - |phi_x|^2/2 - U(phi),
pi = -phi_x, H = -|pi|^2/2 - |phi_t|^2/2 + U.  Defect
L_d = phi.E phi_t/2 + phi.D psi_t + psi.E psi_t/2 - B, sewing equations
phi_x = E phi_t + D psi_t - B_phi, psi_x = D^T phi_t - E psi_t + B_psi.
"""

import itertools
import sympy as sp

ok_all = True


def report(label, ok):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def dot(a, b):
    return (a.T * b)[0]


# ---------------------------------------------------------------- item 1
# Quadratic velocity part of H_- - H_+ for a general constant D, same skew E on both sides.
r = 3
e = sp.symbols("e1:4")
E = sp.Matrix([[0, e[0], e[1]], [-e[0], 0, e[2]], [-e[1], -e[2], 0]])
Dg = sp.Matrix(3, 3, sp.symbols("d1:10"))
a = sp.Matrix(sp.symbols("a1:4"))     # phi_t
b = sp.Matrix(sp.symbols("b1:4"))     # psi_t
I3 = sp.eye(3)


def quad_part(D):
    phx = E * a + D * b                # velocity part of phi_x
    psx = D.T * a - E * b              # velocity part of psi_x
    return sp.expand(-dot(phx, phx) / 2 - dot(a, a) / 2 + dot(psx, psx) / 2 + dot(b, b) / 2)


qp = quad_part(Dg)
formula = sp.expand(dot(a, (Dg * Dg.T + E * E - I3) * a) / 2 + dot(b, (I3 - Dg.T * Dg - E * E) * b) / 2
                    + dot(a, (E * Dg - Dg * E) * b))
report("item 1: velocity-quadratic part = a(DD^T+E^2-I)a/2 + b(I-D^TD-E^2)b/2 + a(ED-DE)b", sp.expand(qp - formula) == 0)
report("item 1: it vanishes for D = I - E", quad_part(I3 - E) == 0)
report("item 1: E = 0, D = 2I has DD^T = D^TD and [E,D] = 0 but leaves velocity terms",
       sp.expand(quad_part(2 * I3).subs({x: 0 for x in e})) != 0)
report("item 1: E = 0, D = -I also cancels (D = I - E is sufficient, not necessary)",
       sp.expand(quad_part(-I3).subs({x: 0 for x in e})) == 0)
# D = (I - E) O with O orthogonal commuting with E: r = 2, E = e J, O a rotation
e0, th = sp.symbols("e0 theta", real=True)
J = sp.Matrix([[0, 1], [-1, 0]])
E2 = e0 * J
O2 = sp.Matrix([[sp.cos(th), -sp.sin(th)], [sp.sin(th), sp.cos(th)]])
D2 = (sp.eye(2) - E2) * O2
cond = sp.simplify(D2 * D2.T - (sp.eye(2) - E2 ** 2)), sp.simplify(D2.T * D2 - (sp.eye(2) - E2 ** 2)), \
    sp.simplify(E2 * D2 - D2 * E2)
report("item 1: D = (I-E)O with O orthogonal, [O,E] = 0 satisfies DD^T = D^TD = I - E^2, [E,D] = 0",
       all(c == sp.zeros(2) for c in cond))

# chain rule for phi = w + D q, psi = w - D^T q
Dn = I3 - E
F = sp.Function("F")
w_, q_ = sp.Matrix(sp.symbols("w1:4")), sp.Matrix(sp.symbols("q1:4"))
ph_, ps_ = w_ + Dn * q_, w_ - Dn.T * q_
# a generic quadratic-plus-cubic test function of (phi, psi)
cc = sp.symbols("c1:22")
vars6 = list(ph_) + list(ps_)
fun = sum(c * x * y for c, (x, y) in zip(cc, itertools.combinations_with_replacement(vars6, 2)))
P6 = sp.symbols("P1:4 S1:4")
funP = sum(c * x * y for c, (x, y) in zip(cc, itertools.combinations_with_replacement(P6, 2)))
gphi = sp.Matrix([sp.diff(funP, x) for x in P6[:3]]).subs(dict(zip(P6, vars6)))
gpsi = sp.Matrix([sp.diff(funP, x) for x in P6[3:]]).subs(dict(zip(P6, vars6)))
gw = sp.Matrix([sp.diff(fun, x) for x in w_])
gq = sp.Matrix([sp.diff(fun, x) for x in q_])
report("item 1: grad_w = grad_phi + grad_psi and grad_q = D^T grad_phi - D grad_psi",
       sp.expand(gw - gphi - gpsi) == sp.zeros(3, 1) and sp.expand(gq - Dn.T * gphi + Dn * gpsi) == sp.zeros(3, 1))


# ------------------------------------------------------------ helpers for A_r
def helmert(N):
    cols = []
    for k in range(1, N):
        v = [sp.Integer(1)] * k + [sp.Integer(-k)] + [sp.Integer(0)] * (N - k - 1)
        cols.append(sp.Matrix(v) / sp.sqrt(k * (k + 1)))
    return sp.Matrix.hstack(*cols)


def a_r_data(N, orient=1):
    """Roots alpha_i = e_i - e_{i+1} (cyclic) in an orthonormal basis of the sum-zero
    hyperplane; P e_i = e_{i+orient}; D = 2 (I - P)^{-1}."""
    B = helmert(N)
    Pn = sp.zeros(N)
    for i in range(N):
        Pn[(i + orient) % N, i] = 1
    roots = [B.T * (sp.eye(N)[:, i] - sp.eye(N)[:, (i + 1) % N]) for i in range(N)]
    Pr = sp.simplify(B.T * Pn * B)
    Dr = sp.simplify(2 * (sp.eye(N - 1) - Pr).inv())
    return roots, Pr, Dr


def canon(v):
    return tuple(sp.nsimplify(sp.radsimp(sp.simplify(x))) for x in v)


def collect(terms):
    """terms: list of (coefficient, exponent covector).  Group equal covectors exactly."""
    groups = []
    for c, key in terms:
        for g in groups:
            if all(sp.simplify(x - y) == 0 for x, y in zip(g[1], key)):
                g[0] += c
                break
        else:
            groups.append([c, key])
    return groups


# ---------------------------------------------------------------- items 2-4
for N in range(3, 8):
    rr = N - 1
    for orient in (1, -1):
        roots, Pr, Dr = a_r_data(N, orient)
        Ir = sp.eye(rr)
        Er = sp.simplify(Ir - Dr)
        okE = sp.simplify(Er + Er.T) == sp.zeros(rr) and sp.simplify(Dr + Dr.T - 2 * Ir) == sp.zeros(rr)
        # constraint U(w + Dq) - U(w - D^T q) - U'(w).h'(q)/2, with f = sigma U, g = h/sigma
        terms = []
        for al in roots:
            terms.append((1, list(al) + list(Dr.T * al)))          # exp(al.w + al.Dq)
            terms.append((-1, list(al) + list(-Dr * al)))          # exp(al.w - al.D^T q)
        for ai, aj in itertools.product(roots, roots):
            terms.append((-dot(ai, Dr.T * aj) / 2, list(ai) + list(Dr.T * aj)))
        groups = collect(terms)
        okC = all(sp.simplify(g[0]) == 0 for g in groups)
        M = sum((al * al.T for al in roots), sp.zeros(rr))
        h0 = sum((Dr.T * al for al in roots), sp.zeros(rr, 1))
        Hh = sp.simplify(Dr.T * M * Dr)
        okH = sp.simplify(h0) == sp.zeros(rr, 1) and Hh == 4 * Ir
        report(f"item 4: a_{rr}^(1), orientation {orient:+d}: E skew, D + D^T = 2I; constraint (8.4) "
               f"by exact exponent matching; h'(0) = 0, h''(0) = D^T M D = 4I", okE and okC and okH)

# negative control: the same matching with the factor 1/2 of (8.4) replaced by 1/4 must fail
roots, Pr, Dr = a_r_data(3, 1)
terms = []
for al in roots:
    terms += [(1, list(al) + list(Dr.T * al)), (-1, list(al) + list(-Dr * al))]
for ai, aj in itertools.product(roots, roots):
    terms.append((-dot(ai, Dr.T * aj) / 4, list(ai) + list(Dr.T * aj)))
report("item 4: control: with 1/4 in place of 1/2 the exponent matching fails",
       not all(sp.simplify(g[0]) == 0 for g in collect(terms)))

# A_2 specifics: M = 3I, gamma = 4/sigma, ghat = h = sigma g; analyticity formula of item 3
sig = sp.Symbol("sigma", positive=True)
roots, Pr, Dr = a_r_data(3, 1)
M = sum((al * al.T for al in roots), sp.zeros(2))
report("item 4: a_2: M = 3I, E^2 = -I/3, D^T D = 4I/3",
       M == 3 * sp.eye(2) and sp.simplify((sp.eye(2) - Dr) ** 2 + sp.eye(2) / 3) == sp.zeros(2)
       and sp.simplify(Dr.T * Dr - 4 * sp.eye(2) / 3) == sp.zeros(2))
Q = sp.Matrix(sp.symbols("Q1 Q2"))
h = sum(sp.exp(dot(al, Dr * Q)) for al in roots) - 3
g = h / sig
G = sp.simplify(sp.hessian(g, list(Q)).subs({x: 0 for x in Q}))
gam = G[0, 0]
report("item 2: a_2: G = g''(0) = (4/sigma) I, so gamma = 4/sigma and ghat = (4/gamma) g = sigma g = h, not g",
       G == 4 / sig * sp.eye(2) and sp.simplify(4 * g / gam - h) == 0 and sp.simplify(4 * g / gam - g) != 0)
# item 3: g'(q) = 2 f''(0)^{-1} [U'(Dq) - U'(-D^T q)], f = sigma U, f''(0) = sigma M
Minv = 2 * (sig * M).inv()
okA = True
for i in range(2):
    terms = [(-(Dr.T * al)[i] / sig, list(Dr.T * al)) for al in roots]          # -g'(q)
    terms += [((Minv * al)[i], list(Dr.T * al)) for al in roots]                 # U'(Dq)
    terms += [(-(Minv * al)[i], list(-Dr * al)) for al in roots]                 # -U'(-D^T q)
    okA &= all(sp.simplify(gr[0]) == 0 for gr in collect(terms))
report("item 3: a_2: g'(q) = 2 f''(0)^{-1}[U'(Dq) - U'(-D^T q)] with f''(0) = sigma M (exact exponent matching)", okA)

# ---------------------------------------------------------------- item 6: Tzitzeica energy
P, q, lam, ep = sp.symbols("P q lambda epsilon")
f_tz = ep * (sp.exp(2 * P - 2 * lam) + sp.exp(-P + lam) * (sp.exp(q) + sp.exp(-q)))
g_tz = (8 * sp.exp(-lam) + sp.exp(2 * lam) * (sp.exp(q) + sp.exp(-q)) ** 2) / (2 * ep)
Etz = f_tz + g_tz
at0 = {P: 0, q: 0, lam: 0}
report("item 6: Tzitzeica Type-II energy (check_hierarchy.py model): value 3 eps + 6/eps and zero first "
       "variation in P, q and lambda at the vacuum",
       sp.simplify(Etz.subs(at0) - 3 * ep - 6 / ep) == 0
       and all(sp.simplify(sp.diff(Etz, x).subs(at0)) == 0 for x in (P, q, lam)))

print("All integration checks passed." if ok_all else "SOME CHECKS FAILED")
raise SystemExit(0 if ok_all else 1)
