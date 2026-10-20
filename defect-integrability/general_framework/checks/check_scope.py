"""Scope of the general statements: the examples that show which hypotheses are
needed, and the small identities that the revised statements rely on.

Each item names the statement of the paper it concerns.  Bulk theories are
first order unless stated, with spatial momentum pi = dL/dw_x.  At the defect,
Pi^- = -E_Phi(L_d), Pi^+ = E_Psi(L_d) and C = E_lambda(L_d), as in (3.1).
One PASS or FAIL line per check.
"""

import sys
import sympy as sp
from jets import TJets, XJets, report, is_zero
from check_balance import spatial_hamiltonian

N = 5
ok = True
m, eps, c, s = sp.symbols("m epsilon c s", positive=True)
x, t = sp.symbols("x t", real=True)


def kg(wt, Z, w, mass=m):
    """Massive Klein-Gordon Lagrangian with w_x replaced by Z."""
    return wt ** 2 / 2 - Z ** 2 / 2 - mass ** 2 * w ** 2 / 2


def h_first_order(J, Ld, Lleft, Lright, left="phi", right="psi"):
    """H_-(Phi, Pi^-) - H_+(Psi, Pi^+) for first-order bulk Lagrangians."""
    Zl, Zr = sp.symbols("Zl Zr")
    PiL = -J.var(Ld, left)
    PiR = J.var(Ld, right)
    HL = spatial_hamiltonian(Lleft(Zl), 1, [[J[left]]], [Zl], [[PiL]])
    HR = spatial_hamiltonian(Lright(Zr), 1, [[J[right]]], [Zr], [[PiR]])
    return sp.expand(HL - HR)


# ------------------------------------------------- Lemma 3.2: the converse needs regularity
J = TJets(["phi", "psi", "lam"], N)
ph, ps, la = J["phi"], J["psi"], J["lam"]
Ld = la[0] * (ps[0] - ph[0]) ** 2
h = h_first_order(J, Ld, lambda Z: kg(ph[1], Z, ph[0]), lambda Z: kg(ps[1], Z, ps[0]))
diag = {ps[k]: ph[k] for k in range(N + 1)}
ok &= report("Lemma 3.2 example L_d = lam (psi-phi)^2: H_- - H_+ vanishes on the prolonged locus C = 0",
             is_zero(h.xreplace(diag)))
Eh = sp.expand(J.var(h, "phi").xreplace(diag))
ok &= report("Lemma 3.2 example: E_phi(H_- - H_+) = phi_tt + m^2 phi on the locus, so the balance "
             "is not in Im D_t + <C>", is_zero(Eh - (ph[2] + m ** 2 * ph[0])))
g = sp.Function("g")(ph[0], ph[1], ps[0], ps[1], la[0], la[1])
C = J.var(Ld, "lam")
ideal_ok = all(is_zero(J.var(e, n).xreplace(diag)) for e in (g * C, g * J.Dt(C)) for n in ("phi", "psi", "lam"))
ok &= report("Lemma 3.2 example: every t-Euler derivative of g C and g D_t C vanishes on the locus "
             "(g a generic function)", ideal_ok)

# ------------------------------------------------- Remark 3.4.2: (I) is needed
phi_, psi_, lam_ = x ** 2, -x ** 2, 2 * x
Ld = la[0] * (ps[0] + ph[0])
PiL = (-J.var(Ld, "phi")).xreplace({la[0]: lam_})
PiR = J.var(Ld, "psi").xreplace({la[0]: lam_})
sewing = [-sp.diff(phi_, x) - PiL, -sp.diff(psi_, x) - PiR, psi_ + phi_]
ok &= report("Remark 3.4.2: (phi, psi, lam) = (x^2, -x^2, 2x) is a promoted solution of L_d = lam (psi+phi)",
             all(is_zero(e) for e in sewing))
E_minus = -sp.diff(phi_, t, 2) + sp.diff(phi_, x, 2) - m ** 2 * phi_
ok &= report("Remark 3.4.2: E_-[phi] = 2 - m^2 x^2 is not zero, so (I) cannot be dropped",
             is_zero(E_minus - (2 - m ** 2 * x ** 2)))
h = h_first_order(J, Ld, lambda Z: kg(ph[1], Z, ph[0]), lambda Z: kg(ps[1], Z, ps[0]))
C = ps[0] + ph[0]
ok &= report("Remark 3.4.2: H_- - H_+ = (psi_t - phi_t) D_tC / 2 + m^2 (phi - psi) C / 2 lies in <C>",
             is_zero(h - ((ps[1] - ph[1]) * J.Dt(C) / 2 + m ** 2 * (ph[0] - ps[0]) * C / 2)))
ok &= report("Remark 3.4.2: S_lambda lambda = 0 and K = 1, so the operator (I) is zero",
             is_zero(sp.diff(Ld, la[0], 2)))

# ------------------------------------------------- Lemma 4.1: N = D_x nu is not enough
# Potential KdV, L = p_x p_t / 2 - p_x^3 - p_xx^2 / 2 (spatial order 2).
pf = sp.Function("p")(x, t)
px, pt, pxx, pxxx = (sp.diff(pf, x), sp.diff(pf, t), sp.diff(pf, x, 2), sp.diff(pf, x, 3))
F1 = pt / 2 - 3 * px ** 2              # dL/dp_x
F2 = -pxx                              # dL/dp_xx
pi0 = F1 - sp.diff(F2, x)
J1 = pxxx - 3 * px ** 2                # mass flux, u = p_x
E_kdv = -sp.diff(px, t) + 6 * px * pxx - sp.diff(pf, x, 4)
ok &= report("Lemma 4.1: the KdV mass law (p_x, p_xxx - 3 p_x^2) satisfies D_tN + D_xJ = -E(L) off shell",
             is_zero(sp.diff(px, t) + sp.diff(J1, x) + E_kdv))
ok &= report("Lemma 4.1: J_1 = pi_0 - p_t/2 = -J_shift + (1/2)(-D_t p), with J_shift = -pi_0",
             is_zero(J1 - (pi0 - pt / 2)))
T = TJets(["p", "P1", "q", "Q1", "mu"], N)
p, P1, q, Q1, mu = T["p"], T["P1"], T["q"], T["Q1"], T["mu"]
al = sp.Symbol("alpha")
w = p[0] - q[0]
Ld_kdv = ((q[0] * p[1] - p[0] * q[1]) / 4 + (P1[0] ** 2 + P1[0] * Q1[0] + Q1[0] ** 2) * w
          + mu[0] * (P1[0] + Q1[0] - 2 * al - w ** 2 / 2) - 3 * (P1[0] + Q1[0]) * w * (al + w ** 2 / 4)
          + 6 * al ** 2 * w + 2 * al * w ** 3 + sp.Rational(9, 40) * w ** 5)


def mass_defect_residual(Ld):
    Pim0, Pip0 = -T.var(Ld, "p"), T.var(Ld, "q")
    Jm, Jp = Pim0 - p[1] / 2, Pip0 - q[1] / 2
    return sp.expand(T.Dt(q[0] - p[0]) - (Jm - Jp))


ok &= report("Corollary 5.3: q - p is a defect charge of the KdV mass law for the defect of [3] (CZ 9.16)",
             is_zero(mass_defect_residual(Ld_kdv)))
beta = sp.Symbol("beta")
res = mass_defect_residual(Ld_kdv + beta * p[0] ** 2)
ok &= report("Lemma 4.1: after adding beta p^2 (shift invariance broken) q - p is no longer a defect charge "
             f"(residual {res})", not is_zero(res) and not res.has(mu[0]))
A_shift = (p[0] - q[0]) / 4             # pr v L_d = D_t A for p, q -> p + e, q + e
Xi_shift = sp.diff(Ld_kdv, p[1]) + sp.diff(Ld_kdv, q[1])
shift_ok = is_zero(T.Dt(A_shift) - sum(sp.diff(Ld_kdv, z[0]) for z in (p, q)))
ok &= report("Corollary 5.3: the shift charge of the KdV defect is A_d - Xi_d = (p - q)/2",
             shift_ok and is_zero(A_shift - Xi_shift - (p[0] - q[0]) / 2))

# ------------------------------------------------- Lemma 5.4: strict homogeneity is needed
J = TJets(["phi", "psi"], N)
ph, ps = J["phi"], J["psi"]


def lagr_div(wt, Z, w):
    return (wt ** 2 - Z ** 2) / 2 + w * Z    # (w_t^2 - w_x^2)/2 + D_x(w^2/2)


for sval, expect in ((1, True), (2, False)):
    Ld = ph[0] * ps[1] + (ps[0] ** 2 - ph[0] ** 2) / (2 * sval)
    h = h_first_order(J, Ld, lambda Z: lagr_div(ph[1], Z, ph[0]), lambda Z: lagr_div(ps[1], Z, ps[0]))
    tot, _ = J.is_total_derivative(h, ["phi", "psi"])
    ok &= report(f"Lemma 5.4 example with bulk density + D_x(w^2/2), dilated defect at s = {sval}: "
                 f"balance {'holds' if expect else 'fails'}", tot == expect)

# strict homogeneity of the bulk Lagrangians used for KdV, mKdV and NLS
sx, st_ = sp.symbols("s_x s_t", positive=True)
P1s, Pts, Zs, U, Ub, Ut, Ubt, Ux, Ubx = sp.symbols("P1 p_t Z u ub u_t ub_t u_x ub_x")
cases = [
    ("KdV p -> s p(s x, s^3 t)", P1s * Pts / 2 - P1s ** 3 - Zs ** 2 / 2, {P1s: s ** 2, Pts: s ** 4, Zs: s ** 3}),
    ("mKdV p -> p(s x, s^3 t)", P1s * Pts / 2 - P1s ** 4 / 2 + Zs ** 2 / 2, {P1s: s, Pts: s ** 3, Zs: s ** 2}),
    ("NLS u -> s u(s x, s^2 t)", sp.I / 2 * (Ub * Ut - Ubt * U) - Ux * Ubx + (U * Ub) ** 2,
     {U: s, Ub: s, Ut: s ** 3, Ubt: s ** 3, Ux: s ** 2, Ubx: s ** 2}),
]
for label, L, wts in cases:
    ratio = sp.simplify(L.xreplace({z: f * z for z, f in wts.items()}) / L)
    ok &= report(f"Lemma 5.4: the {label} bulk Lagrangian is strictly homogeneous (factor {ratio})",
                 ratio.free_symbols <= {s})

# ------------------------------------------------- Lemma 6.6: momentum conservation is needed
J = TJets(["phi", "psi"], N)
ph, ps = J["phi"], J["psi"]
Ld = -(ph[0] - ps[0]) ** 2 / (2 * eps)
h = h_first_order(J, Ld, lambda Z: kg(ph[1], Z, ph[0]), lambda Z: kg(ps[1], Z, ps[0]))
tot, _ = J.is_total_derivative(h, ["phi", "psi"])
ok &= report("Lemma 6.6 example L_d = -(phi-psi)^2/(2 eps) is not momentum-conserving", not tot)
pf = sp.Function("phi")(x, t)
psi_left = pf + eps * sp.diff(pf, x)                 # from phi_x = (psi - phi)/eps
right = sp.diff(psi_left, x) - (psi_left - pf) / eps  # psi_x - (psi - phi)/eps
ok &= report("Lemma 6.6 example: the two sewing equations force eps phi_xx = 0",
             is_zero(right - eps * sp.diff(pf, x, 2)))

# ------------------------------------------------- Theorem 7.3: linear parts and H_3
X = XJets(["q", "p"], 16)
q, p = X["q"], X["p"]


def bracket(F, G):
    return sp.expand(X.euler(F, "q") * X.euler(G, "p") - X.euler(F, "p") * X.euler(G, "q"))


f = -p[1] ** 2 - 2 * p[0] * p[2]                      # delta/delta p of int p p_x^2
ok &= report("Theorem 7.3 example: f = -p_x^2 - 2 p p_xx is the gradient of int p p_x^2",
             is_zero(f - X.euler(p[0] * p[1] ** 2, "p")))
Uq = q[0] + f
Hd = (X.Dx(Uq) ** 2 + p[1] ** 2) / 2
H2, H3 = (q[1] ** 2 + p[1] ** 2) / 2, q[1] * X.Dx(f)
Qd, Q1d, Q2d = q[0] + p[1] ** 2, q[0], p[1] ** 2
Rd = p[0] * q[1]
ok &= report("Theorem 7.3 example: H = H_2 + H_3 + H_4 with the stated H_2 and H_3",
             X.is_trivial(sp.expand(Hd - H2 - H3 - X.Dx(f) ** 2 / 2)))
ok &= report("Theorem 7.3 example: Q = int (q + p_x^2) and R = int p q_x are conserved",
             X.is_trivial(bracket(Qd, Hd)) and X.is_trivial(bracket(Rd, Hd)))
ok &= report("Theorem 7.3 example: (L) holds, {Q_1, Q} = {Q_1, R} = 0, and {Q, R} = 0",
             X.is_trivial(bracket(Q1d, Qd)) and X.is_trivial(bracket(Q1d, Rd)) and X.is_trivial(bracket(Qd, Rd)))
ok &= report("Theorem 7.3 example: {Q_2, H_2} + {Q_1, H_3} = 0 while {Q_2, H_2} = -2 int p_xx q_xx != 0",
             X.is_trivial(bracket(Q2d, H2) + bracket(Q1d, H3))
             and X.is_trivial(bracket(Q2d, H2) + 2 * p[2] * q[2]) and not X.is_trivial(bracket(Q2d, H2)))
ok &= report("Theorem 7.3 example: the extra condition {Q_1, H} = 0 fails here",
             not X.is_trivial(bracket(Q1d, Hd)))

# ------------------------------------------------- Theorem 7.4: existence, not every seed
k = sp.Symbol("k", positive=True)
u = eps * sp.cos(k * x)
ok &= report("Theorem 7.4: at u = eps cos(kx), delta(int u_x^2/2) = k^2 delta(int u^2/2)",
             is_zero(-sp.diff(u, x, 2) - k ** 2 * u))

# ------------------------------------------------- Section 8: equal masses violate (NR2)
X = XJets(["q1", "p1", "q2", "p2"], 8)
q1, p1, q2, p2 = X["q1"], X["p1"], X["q2"], X["p2"]


def br2(F, G):
    return sp.expand(sum(X.euler(F, f"q{i}") * X.euler(G, f"p{i}") - X.euler(F, f"p{i}") * X.euler(G, f"q{i}")
                         for i in (1, 2)))


def Kop(z):
    return -z[2] + m ** 2 * z[0]


Hd = (p1[0] ** 2 + p2[0] ** 2 + q1[0] * Kop(q1) + q2[0] * Kop(q2)) / 2
Ad = p1[0] * p2[0] + q1[0] * Kop(q2)
Bd = (p1[0] ** 2 + q1[0] * Kop(q1) - p2[0] ** 2 - q2[0] * Kop(q2)) / 2
ok &= report("Section 8: two free fields of equal mass have conserved quadratic A, B with {A, B} != 0",
             X.is_trivial(br2(Ad, Hd)) and X.is_trivial(br2(Bd, Hd)) and not X.is_trivial(br2(Ad, Bd))
             and X.is_trivial(br2(Ad, Bd) - 2 * (p1[0] * Kop(q2) - p2[0] * Kop(q1))))

# ------------------------------------------------- Section 7.1: (NR) for all degrees
om = sp.Function("omega")
k1, k2, s1, s2, s3 = sp.symbols("k1 k2 s1 s2 s3")
k3 = -s3 * (s1 * k1 + s2 * k2)
Om = s1 * om(k1) + s2 * om(k2) + s3 * om(k3)
mixed = sp.diff(Om, k1, k2).subs({s1 ** 2: 1, s2 ** 2: 1, s3 ** 2: 1})
target = s1 * s2 * s3 * sp.diff(om(x), x, 2).subs(x, k3)
signs_ok = all(is_zero((mixed - target).subs({s1: a, s2: b, s3: cc}).doit())
               for a in (1, -1) for b in (1, -1) for cc in (1, -1))
ok &= report("Section 7.1: on the momentum hyperplane, d^2 Omega/dk_1 dk_2 = s_1 s_2 s_n omega''(k_n)", signs_ok)
kk = sp.Symbol("k", real=True)
for name, wk in [("massive relativistic", sp.sqrt(kk ** 2 + m ** 2)), ("NLS", kk ** 2), ("KdV, mKdV", kk ** 3),
                 ("Boussinesq", c * kk * sp.sqrt(1 + kk ** 2))]:
    ok &= report(f"Section 7.1: omega'' is not identically zero for {name}",
                 not is_zero(sp.diff(wk, kk, 2).subs(kk, sp.Rational(1, 3))))

# ------------------------------------------------- Proposition 7.5: quadratic nonlinearities
ph0 = sp.Symbol("phi")
ok &= report("Proposition 7.5: sin(phi) has no quadratic Taylor term (sine-Gordon)",
             sp.series(sp.sin(ph0), ph0, 0, 3).removeO().coeff(ph0, 2) == 0)
lam_b, kap = sp.symbols("lambda kappa", positive=True)
X = XJets(["u"], 8)
uu = X["u"]
# canonical variables (u, p = u_t/c^2): p_t = u_xx + 2 lambda u_x u_xx - kappa^2 u_xxxx
quad = 2 * lam_b * uu[1] * uu[2]
ok &= report("Proposition 7.5: the quadratic term of the Boussinesq p_t, p = u_t/c^2, is lambda D_x(u_x^2)",
             X.is_trivial(quad) and is_zero(quad - lam_b * X.Dx(uu[1] ** 2)))
# potential variables are not local in v: KdV p_t = 3u^2 - u_xx (CZ nlin/0512038 eq. 9.4)
aa, ab, kq = sp.symbols("a abar k", positive=True)
eta_ = sp.Symbol("eta", positive=True)
uw = eta_ * (aa * sp.exp(sp.I * kq * x) + ab * sp.exp(-sp.I * kq * x))
pt_full = sp.expand(3 * uw ** 2 - sp.diff(uw, x, 2))
avg = sp.simplify(sp.integrate(sp.expand(pt_full.rewrite(sp.cos)), (x, 0, 2 * sp.pi / kq)) * kq / (2 * sp.pi))
ok &= report("Proposition 7.5: on a first harmonic in u, the KdV potential p_t has x-average 6 eta^2 |a|^2",
             is_zero(avg - 6 * eta_ ** 2 * aa * ab))
# KdV branch from the spatial Baecklund relation p_x + q_x = 2 alpha + (p - q)^2/2 (CZ eq. 9.12)
Pf = sp.Function("p")(x)
Dl = sp.Function("Delta")(x)
qf = Pf - 2 / eps + Dl
rel = sp.diff(Pf, x) + sp.diff(qf, x) - (-2 / eps ** 2 + (Pf - qf) ** 2 / 2)
target = (2 * Dl + eps * sp.diff(Dl, x)) + 2 * eps * sp.diff(Pf, x) - eps / 2 * Dl ** 2
ok &= report("Proposition 7.5: with alpha = -1/eps^2, q = p - 2/eps + Delta, (9.12) is "
             "(2 + eps D_x) Delta = -2 eps u + (eps/2) Delta^2", is_zero(sp.expand(eps * rel - target)))

# ------------------------------------------------- Lemma 6.5: a nonlinear symmetry
qf2, rf2 = sp.Function("q")(x, t), sp.Function("r")(x, t)
# boosts are not linear on phase-space data: delta phi = x phi_t + t phi_x at t = 0,
# with phi_tt = phi_xx - U'(phi) and U'(phi) = m^2 phi + U3 phi^2 / 2 + O(phi^3)
U3, Q0, Q1x, Q2x, P0, Ptt = sp.symbols("U3 q q_x q_xx p p_tt")
phb = sp.Function("phi")(x, t)
dphit = sp.diff(x * sp.diff(phb, t) + t * sp.diff(phb, x), t).subs(t, 0)
dphit = dphit.subs({sp.Derivative(phb, (t, 2)).subs(t, 0): Ptt}).subs(
    {sp.Derivative(phb, x).subs(t, 0): Q1x, sp.Derivative(phb, t).subs(t, 0): P0})
dphit = dphit.subs(Ptt, Q2x - (m ** 2 * Q0 + U3 * Q0 ** 2 / 2))
ok &= report("Lemma 6.5: the infinitesimal boost gives delta phi_t a quadratic part -U3 x phi^2 / 2",
             is_zero(sp.expand(dphit).coeff(Q0, 2) + U3 * x / 2))
Ufun, Vfun = qf2 + rf2 ** 2, rf2
L_UV = sp.diff(Ufun, t) * sp.diff(Vfun, t) - sp.diff(Ufun, x) * sp.diff(Vfun, x)
Pq = sp.diff(L_UV, sp.diff(qf2, t))
Pr = sp.diff(L_UV, sp.diff(rf2, t))
qx_, rx_, r_ = sp.symbols("q_x r_x r")
Lx = -(qx_ + 2 * r_ * rx_) * rx_
hess = sp.Matrix([[sp.diff(Lx, u_, v_) for v_ in (qx_, rx_)] for u_ in (qx_, rx_)])
ok &= report("Lemma 6.5 example: L = U_t V_t - U_x V_x with U = q + r^2, V = r has spatial Hessian of "
             "determinant -1, and U_t = P_r - 2 r P_q", hess.det() == -1
             and is_zero(sp.diff(Ufun, t) - (Pr - 2 * rf2 * Pq)))
av = sp.Symbol("a", positive=True)
qn, rn = av * qf2 + (av - av ** -2) * rf2 ** 2, rf2 / av
ok &= report("Lemma 6.5 example: (U, V) -> (a U, V/a) acts by q -> a q + (a - a^-2) r^2, r -> r/a",
             is_zero(qn + rn ** 2 - av * Ufun) and is_zero(rn - Vfun / av))
Rs, PQs = sp.symbols("R P_q")
Q2 = -2 * Rs * PQs
ok &= report("Lemma 6.5 example: the charge int U_t scales by a, its quadratic part -2 int r P_q by a^-2",
             is_zero(Q2.subs({Rs: Rs / av, PQs: PQs / av}, simultaneous=True) - av ** -2 * Q2))

# ------------------------------------------------- Appendix A: the converse loses a constant
J = TJets(["phi", "psi"], N)
ph, ps = J["phi"], J["psi"]
Ld = ph[0] * ps[1]
h = h_first_order(J, Ld, lambda Z: (ph[1] ** 2 - Z ** 2) / 2, lambda Z: (ps[1] ** 2 - Z ** 2) / 2 - c)
ok &= report("Appendix A: with L_+ shifted by -c, H_- - H_+ = -c on the sewing correspondence of phi psi_t",
             is_zero(h + c))

sys.exit(0 if ok else 1)
