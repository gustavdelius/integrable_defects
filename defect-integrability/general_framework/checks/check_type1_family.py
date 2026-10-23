"""Section 8.2: hypothesis (C) for relativistic Type-I defects with constant coupling.

Bulk: L = |phi_t|^2/2 - |phi_x|^2/2 - U(phi), so pi = -phi_x and
H = -|pi|^2/2 - |phi_t|^2/2 + U.  Defect:
    L_d = phi.E phi_t / 2 + phi.D psi_t + psi.E psi_t / 2 - B(phi, psi),  E^T = -E,  D = I - E.
Sewing equations (3.1): pi_- = -E_phi L_d, pi_+ = E_psi L_d.  Coordinates
q = (phi - psi)/2, w = (D^T phi + D psi)/2.  Written from the definitions of paper.md;
imports only SymPy.  One PASS or FAIL line per check.
"""

import random
import sympy as sp

ok = True


def report(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


def vec(name, r):
    return sp.Matrix(sp.symbols(f"{name}1:{r + 1}"))


def dot(a, b):
    return (a.T * b)[0]


# ------------------------------------------------- Proposition 8.2, r = 3, general skew E
r = 3
e1, e2, e3 = sp.symbols("e1 e2 e3")
E = sp.Matrix([[0, e1, e2], [-e1, 0, e3], [-e2, -e3, 0]])
I = sp.eye(r)
D = I - E
report("D D^T = D^T D = I - E^2 and [E, D] = 0",
       sp.expand(D * D.T - (I - E * E)) == sp.zeros(r) and sp.expand(D.T * D - (I - E * E)) == sp.zeros(r)
       and sp.expand(E * D - D * E) == sp.zeros(r))

ph, ps, pht, pst = vec("phi", r), vec("psi", r), vec("phit", r), vec("psit", r)
Bp, Bq = vec("Bphi", r), vec("Bpsi", r)     # gradients of B at the point
Um, Up = sp.symbols("U_phi U_psi")          # U(phi), U(psi)

# E_phi L_d = E phi_t + D psi_t - B_phi,  E_psi L_d = E psi_t - D^T phi_t - B_psi (derived by hand)
phx = E * pht + D * pst - Bp                 # from pi_- = -phi_x = -E_phi L_d
psx = D.T * pht - E * pst + Bq               # from pi_+ = -psi_x = E_psi L_d
H = lambda wx, wt, u: -dot(wx, wx) / 2 - dot(wt, wt) / 2 + u
bal = sp.expand(H(phx, pht, Um) - H(psx, pst, Up))
lin = dot(pht, -E * Bp + D * Bq) + dot(pst, D.T * Bp + E * Bq)
const = -dot(Bp, Bp) / 2 + dot(Bq, Bq) / 2 + Um - Up
report("H_- - H_+ has no terms quadratic in the velocities; it equals "
       "phi_t.(-E B_phi + D B_psi) + psi_t.(D^T B_phi + E B_psi) - |B_phi|^2/2 + |B_psi|^2/2 + U(phi) - U(psi)",
       sp.expand(bal - lin - const) == 0)

# check the two Euler derivatives used above on a concrete quadratic B
Bc = sum(sp.Symbol(f"c{i}{j}") * x * y for i, x in enumerate(list(ph) + list(ps))
         for j, y in enumerate(list(ph) + list(ps)) if i <= j)
Ld = dot(ph, E * pht) / 2 + dot(ph, D * pst) + dot(ps, E * pst) / 2 - Bc
Dt = lambda expr: sum(sp.diff(expr, a) * b for a, b in zip(list(ph) + list(ps), list(pht) + list(pst))) + \
    sum(sp.diff(expr, b) * sp.Symbol("dd_" + str(b)) for b in list(pht) + list(pst))
Ephi = sp.Matrix([sp.diff(Ld, ph[i]) - Dt(sp.diff(Ld, pht[i])) for i in range(r)])
Epsi = sp.Matrix([sp.diff(Ld, ps[i]) - Dt(sp.diff(Ld, pst[i])) for i in range(r)])
gradphi = sp.Matrix([sp.diff(Bc, x) for x in ph])
gradpsi = sp.Matrix([sp.diff(Bc, x) for x in ps])
report("E_phi L_d = E phi_t + D psi_t - B_phi and E_psi L_d = E psi_t - D^T phi_t - B_psi",
       sp.expand(Ephi - (E * pht + D * pst - gradphi)) == sp.zeros(r, 1)
       and sp.expand(Epsi - (E * pst - D.T * pht - gradpsi)) == sp.zeros(r, 1))

# the balance H_- - H_+ + D_t P~ = 0 with P~(phi, psi) gives (8.2); in (w, q): P~_w = -B_w, P~_q = B_q
Pp = E * Bp - D * Bq
Pq = -D.T * Bp - E * Bq
report("(8.2) makes the velocity-linear terms cancel: phi_t.P~_phi + psi_t.P~_psi = -(linear terms)",
       sp.expand(dot(pht, Pp) + dot(pst, Pq) + lin) == 0)
# gradients in (w, q): phi = w + D q, psi = w - D^T q, so d/dw = d/dphi + d/dpsi, d/dq = D^T d/dphi - D d/dpsi
grad_w = lambda gp, gq: gp + gq
grad_q = lambda gp, gq: D.T * gp - D * gq
report("in (w, q): P~_w = -B_w and P~_q = B_q, so B_wq = 0 and B = f(w) + g(q), P~ = g - f",
       sp.expand(grad_w(Pp, Pq) + grad_w(Bp, Bq)) == sp.zeros(r, 1)
       and sp.expand(grad_q(Pp, Pq) - grad_q(Bp, Bq)) == sp.zeros(r, 1))
w_ = (D.T * ph + D * ps) / 2
q_ = (ph - ps) / 2
report("phi = w + D q and psi = w - D^T q", sp.expand(w_ + D * q_ - ph) == sp.zeros(r, 1)
       and sp.expand(w_ - D.T * q_ - ps) == sp.zeros(r, 1))
fp, gp = vec("fp", r), vec("gp", r)          # f'(w), g'(q)
Bphi_split = (D * fp + gp) / 2
Bpsi_split = (D.T * fp - gp) / 2
report("(8.1): for B = f(w) + g(q), (|B_phi|^2 - |B_psi|^2)/2 = f'(w).g'(q)/2",
       sp.expand((dot(Bphi_split, Bphi_split) - dot(Bpsi_split, Bpsi_split)) / 2 - dot(fp, gp) / 2) == 0)

# ------------------------------------------------- Proposition 8.3: the commutator step
G, F2 = sp.Matrix(sp.MatrixSymbol("G", r, r)), sp.Matrix(sp.MatrixSymbol("F", r, r))
report("[G, G F] = G [G, F], so [G, F] = 0 gives [G, U''] = 0 when G f'' = 4 U''",
       sp.expand((G * (G * F2) - (G * F2) * G) - G * (G * F2 - F2 * G)) == sp.zeros(r))

# ------------------------------------------------- the published defects
# sine-Gordon, r = 1, E = 0, D = 1: B = 2 sigma (1 - cos w) + (2/sigma)(1 - cos q)
s, w1, q1, eps = sp.symbols("sigma w q epsilon", positive=True)
fsg, gsg = 2 * s * (1 - sp.cos(w1)), 2 / s * (1 - sp.cos(q1))
Usg = lambda u: 1 - sp.cos(u)
report("sine-Gordon: U(w+q) - U(w-q) = f'(w) g'(q)/2",
       sp.simplify(sp.expand_trig(Usg(w1 + q1) - Usg(w1 - q1) - sp.diff(fsg, w1) * sp.diff(gsg, q1) / 2)) == 0)
gam = sp.diff(gsg, q1, 2).subs(q1, 0)
ghat = sp.simplify(4 * gsg / gam)
report("sine-Gordon: G = 2/sigma, f = 4U/G, g^ = 4(1 - cos q), and the defect is the member eps = 2 sigma",
       sp.simplify(gam - 2 / s) == 0 and sp.simplify(fsg - 4 * Usg(w1) / gam) == 0
       and sp.simplify(ghat - 4 * (1 - sp.cos(q1))) == 0
       and sp.simplify((eps * Usg(w1) + ghat / eps).subs(eps, 2 * s) - (fsg + gsg)) == 0)

# a_2^(1) affine Toda, as transcribed in check_balance.py from BCZ hep-th/0401020
a1 = sp.Matrix([sp.sqrt(2), 0])
a2 = sp.Matrix([-sp.sqrt(2) / 2, sp.sqrt(6) / 2])
roots = [-a1 - a2, a1, a2]
c, sn = sp.cos(2 * sp.pi / 3), sp.sin(2 * sp.pi / 3)
pi = sp.Matrix([[c, -sn], [sn, c]])
if sp.simplify(pi * a1 - roots[0]) != sp.zeros(2, 1):
    pi = pi.T
DT = sp.simplify(2 * (sp.eye(2) - pi).inv())
ET = sp.eye(2) - DT
report("Toda a_2: E = I - D is skew", sp.simplify(ET + ET.T) == sp.zeros(2))
W, Qv = sp.Matrix(sp.symbols("W1 W2")), sp.Matrix(sp.symbols("Q1 Q2"))
UT = lambda u: sum(sp.exp(dot(al, u)) for al in roots) - 3
fT = UT(W)
gT = sum(sp.exp(dot(al, DT * Qv)) for al in roots) - 3
lhs = UT(W + DT * Qv) - UT(W - DT.T * Qv)
rhs = dot(sp.Matrix([sp.diff(fT, x) for x in W]), sp.Matrix([sp.diff(gT, x) for x in Qv])) / 2
random.seed(1)
pts = [{x: sp.Rational(random.randint(-9, 9), 7) for x in list(W) + list(Qv)} for _ in range(6)]
report("Toda a_2: U(w + Dq) - U(w - D^T q) = f'(w).g'(q)/2 at six rational points (30 digits)",
       all(abs(sp.N((lhs - rhs).subs(pt), 30)) < 1e-25 for pt in pts))
gradg0 = sp.Matrix([sp.diff(gT, x) for x in Qv]).subs({x: 0 for x in Qv})
GT = sp.simplify(sp.hessian(gT, list(Qv)).subs({x: 0 for x in Qv}))
report("Toda a_2: transparent point g'(0) = 0, and G = g''(0) = 3 D^T D is a nonzero multiple of I",
       sp.simplify(gradg0) == sp.zeros(2, 1) and sp.simplify(GT - 3 * DT.T * DT) == sp.zeros(2)
       and sp.simplify(GT - GT[0, 0] * sp.eye(2)) == sp.zeros(2) and sp.simplify(GT[0, 0]) != 0)
# the transcribed defect has B = sigma U(w) + g(q)/sigma; its Hessian G = g''(0)/sigma must be 4/sigma
gamma_T = sp.simplify(GT[0, 0] / s)
report("Toda a_2: gamma = 4/sigma, so f = sigma U(w) = 4U/gamma, g^ = 4 (g/sigma)/gamma = g, "
       "and the defect is the member eps = 4/gamma = sigma of (8.3)",
       sp.simplify(gamma_T - 4 / s) == 0 and sp.simplify(s * UT(W) - 4 * UT(W) / gamma_T) == 0
       and sp.simplify(4 * (gT / s) / gamma_T - gT) == 0)
# Lemma 6.6: the stiff spring g^(q), q = (phi - psi)/2, has Hessian g^''(0)/4 in phi on the diagonal
report("Lemma 6.6 for (8.3), Toda a_2: g^''(0) = 4I, so the Hessian of g^((phi - psi)/2) in phi on the diagonal is I",
       sp.simplify(GT - 4 * sp.eye(2)) == sp.zeros(2))

raise SystemExit(0 if ok else 1)
