"""Checks for the kinematic lemmas of the general-framework paper.

A. Closure relations are Noether identities (Lemma 5.2).  For each bulk theory
   an affine conservation law
       D_t(x a1 + t a2 + a0) + D_x(x b1 + t b2 + b0) = 0
   is exhibited: (a1, b1) is a conservation law, a2 is a conserved density,
   and the x,t-independent part a2 + b1 + D_t a0 + D_x b0 vanishes on shell.

B. Families are kinematic orbits (Lemma 5.4).  The sine-Gordon Type-I sewing
   relations are carried by a Lorentz boost to the same relations with the
   parameter rescaled; the KdV, mKdV and NLS defect functionals are
   homogeneous under the dilations of their bulk theories, with the defect
   parameter carrying a fixed weight.

C. Nonresonance (Definition 6.1).  For the massive Klein-Gordon, NLS, KdV,
   mKdV and Boussinesq dispersion relations, every resonance function of
   degree 3 and 4 is not identically zero on the hyperplane sum k = 0; for the
   massless wave it vanishes on an open set.
One PASS or FAIL line per check.
"""

import itertools
import random
import sys
import sympy as sp
from jets import XJets, TJets, report

ok = True

# ---------------------------------------------------------------- A. closure
def affine_law(label, X, a1, b1, a2, a0, b0):
    global ok
    c1 = sp.simplify(sp.expand(X.Dt(a1) + X.Dx(b1))) == 0
    c2 = X.is_conserved(a2)
    c3 = sp.simplify(sp.expand(a2 + b1 + X.Dt(a0) + X.Dx(b0))) == 0
    ok &= report(f"{label}: affine conservation law (law 1 conserved, a2 conserved, constant term zero)",
                 c1 and c2 and c3, f"{c1} {c2} {c3}")


# relativistic scalar with generic potential: Lorentz boost
X = XJets(["phi", "chi"], 8)
ph, ch = X["phi"], X["chi"]
Uf = sp.Function("U")
X.set_flow("phi", ch[0])
X.set_flow("chi", ph[2] - sp.diff(Uf(ph[0]), ph[0]))
T00 = ch[0] ** 2 / 2 + ph[1] ** 2 / 2 + Uf(ph[0])
T10 = -ph[1] * ch[0]
T01 = -ch[0] * ph[1]
affine_law("relativistic scalar, Lorentz boost (closure T^10 = T^01, density E_d)",
           X, T00, T10, -T01, 0, 0)

# NLS: Galilean boost
X = XJets(["u", "ub"], 8)
u, ub = X["u"], X["ub"]
X.set_flow("u", sp.I * (u[2] + 2 * u[0] ** 2 * ub[0]))
X.set_flow("ub", -sp.I * (ub[2] + 2 * ub[0] ** 2 * u[0]))
N = u[0] * ub[0]
JN = sp.I * (u[0] * ub[1] - ub[0] * u[1])
P = sp.I / 2 * (u[0] * ub[1] - ub[0] * u[1])     # canonical T^01
affine_law("NLS, Galilean boost (closure J_N = 2 T^01, density N_d)", X, N, JN, -2 * P, 0, 0)

# KdV u_t = 6 u u_x - u_xxx: Galilean symmetry
X = XJets(["u"], 8)
u = X["u"]
X.set_flow("u", 6 * u[0] * u[1] - u[3])
affine_law("KdV, Galilean symmetry (closure J_mass = -6 T^01 - D_x u_x, density q - p)",
           X, u[0], -3 * u[0] ** 2 + u[2], 3 * u[0] ** 2, 0, -u[1])

# mKdV v_t = 6 v^2 v_x + v_xxx: dilation
X = XJets(["v"], 8)
v = X["v"]
X.set_flow("v", 6 * v[0] ** 2 * v[1] + v[3])
J1 = -(sp.Rational(3, 2) * v[0] ** 4 + v[0] * v[2] - v[1] ** 2 / 2)
affine_law("mKdV, dilation (closure T^11 = 3 T^00 mod D_x, density P_d)",
           X, v[0] ** 2 / 2, J1, sp.Rational(3, 2) * (v[0] ** 4 - v[1] ** 2), 0, v[0] * v[1])

# Boussinesq: time-linear shift u -> u + e t
c, kap, lam = sp.symbols("c kappa lambda", positive=True)
X = XJets(["u", "chi"], 8)
u, ch = X["u"], X["chi"]
X.set_flow("u", ch[0])
X.set_flow("chi", c ** 2 * (u[2] + 2 * lam * u[1] * u[2] - kap ** 2 * u[4]))
affine_law("Boussinesq, time-linear shift (closure from the shift law, density (u - v)/c^2)",
           X, 0, 0, -ch[0] / c ** 2, u[0] / c ** 2, 0)


# ---------------------------------------------------------------- B. families
def sg_boost():
    """Lorentz covariance of the BCZ sewing relations (Theorem A form)."""
    th, s = sp.symbols("theta sigma", positive=True)
    p, q, pt, px, qt, qx = sp.symbols("phi psi phi_t phi_x psi_t psi_x")
    def B(sig):
        return 2 * sig * (1 - sp.cos((p + q) / 2)) + 2 / sig * (1 - sp.cos((p - q) / 2))
    def rel(sig, pt_, px_, qt_, qx_):
        # phi_x = psi_t - dB/dphi,  psi_x = phi_t + dB/dpsi
        return [px_ - (qt_ - sp.diff(B(sig), p)), qx_ - (pt_ + sp.diff(B(sig), q))]
    # solve the sigma relations for the x-derivatives, then boost
    sol = sp.solve(rel(s, pt, px, qt, qx), [px, qx], dict=True)[0]
    ch_, sh_ = sp.cosh(th), sp.sinh(th)
    tpt, tpx = ch_ * pt + sh_ * sol[px], sh_ * pt + ch_ * sol[px]
    tqt, tqx = ch_ * qt + sh_ * sol[qx], sh_ * qt + ch_ * sol[qx]
    good = []
    for sig2 in [s * sp.exp(th), s * sp.exp(-th)]:
        r = rel(sig2, tpt, tpx, tqt, tqx)
        good.append(all(sp.simplify(sp.expand((x.rewrite(sp.exp)))) == 0 for x in r))
    return any(good)


ok &= report("sine-Gordon Type I: a Lorentz boost maps the sewing relations with parameter sigma "
             "to those with parameter sigma e^{+-theta}", sg_boost())


def homogeneous(label, B, weights, param, pw):
    s = sp.Symbol("s", positive=True)
    scaled = B.xreplace({z: s ** w * z for z, w in weights.items()} | {param: s ** pw * param})
    ratio = sp.simplify(sp.expand(scaled) / sp.expand(B))
    good = ratio.free_symbols <= {s}
    return report(label + f" (B scales by {ratio})", good)


p, q, P1, Q1, mu, pt, qt, al = sp.symbols("p q P1 Q1 mu p_t q_t alpha")
w_ = p - q
Bkdv = ((q * pt - p * qt) / 4 + (P1 ** 2 + P1 * Q1 + Q1 ** 2) * w_
        + mu * (P1 + Q1 - 2 * al - w_ ** 2 / 2) - 3 * (P1 + Q1) * w_ * (al + w_ ** 2 / 4)
        + 6 * al ** 2 * w_ + 2 * al * w_ ** 3 + sp.Rational(9, 40) * w_ ** 5)
# KdV dilation p(x,t) -> s p(s x, s^3 t): p ~ s, p_x ~ s^2, p_xx ~ s^3, p_t ~ s^4 ; alpha ~ s^2
ok &= homogeneous("KdV defect (CZ 9.16) is dilation homogeneous with alpha of weight 2",
                  Bkdv, {p: 1, q: 1, P1: 2, Q1: 2, mu: 3, pt: 4, qt: 4}, al, 2)
Bm = (q * pt - p * qt) / 4 - (mu * (P1 + Q1 - al * sp.sin(w_))
                              + al / 6 * sp.cos(w_) * (P1 ** 2 + Q1 ** 2 - 4 * P1 * Q1
                                                      + al * (P1 + Q1) * sp.sin(w_) + al ** 2))
# mKdV dilation p(x,t) -> p(s x, s^3 t): p ~ 1, p_x ~ s, p_xx ~ s^2, p_t ~ s^3 ; alpha ~ s
ok &= homogeneous("mKdV defect (CZ 7.22) is dilation homogeneous with alpha of weight 1",
                  Bm, {p: 0, q: 0, P1: 1, Q1: 1, mu: 2, pt: 3, qt: 3}, al, 1)
U, Ub, V, Vb, Ut, Ubt, Vt, Vbt, a_ = sp.symbols("U Ub V Vb U_t Ub_t V_t Vb_t alpha", positive=True)
d, db = U - V, Ub - Vb
Bn = sp.sqrt(a_ ** 2 - d * db) * (sp.I / 2 * ((Ut - Vt) / d - (Ubt - Vbt) / db)
                                  + (a_ ** 2 - d * db) / 3 + U * Ub + V * Vb)
# NLS dilation u(x,t) -> s u(s x, s^2 t): u ~ s, u_t ~ s^3 ; alpha ~ s
ok &= homogeneous("NLS defect (CZ 2.9-2.10) is dilation homogeneous with alpha of weight 1",
                  Bn, {U: 1, Ub: 1, V: 1, Vb: 1, Ut: 3, Ubt: 3, Vt: 3, Vbt: 3}, a_, 1)


# ---------------------------------------------------------------- C. nonresonance
def omega_fns():
    m, c, kap = 1.0, 1.0, 1.0
    return {
        "massive Klein-Gordon": lambda k: (k * k + m * m) ** 0.5,
        "NLS": lambda k: k * k,
        "KdV": lambda k: k ** 3,
        "mKdV": lambda k: k ** 3,
        "Boussinesq": lambda k: c * k * (1 + kap ** 2 * k ** 2) ** 0.5,
    }


random.seed(1)
for name, om in omega_fns().items():
    good = True
    for n in (3, 4):
        # a monomial in modes a(k_i) (s_i = +1) and conjugate modes (s_i = -1) has momentum
        # sum s_i k_i and frequency sum s_i omega(k_i)
        for sgn in itertools.product([1, -1], repeat=n):
            # random points on sum s_i k_i = 0; a nonzero value shows that the real-analytic
            # resonance function is not identically zero, so its zero set has empty interior
            vals = []
            for _ in range(5):
                ks = [random.uniform(-2, 2) for _ in range(n - 1)]
                ks.append(-sgn[-1] * sum(si * ki for si, ki in zip(sgn, ks)))
                vals.append(abs(sum(si * om(ki) for si, ki in zip(sgn, ks))))
            if max(vals) < 1e-9:
                good = False
    ok &= report(f"nonresonance of degree 3 and 4 for {name}", good)

# massless wave: omega(k)+omega(l)-omega(k+l) = 0 for all k, l > 0 (an open set)
k, l = sp.symbols("k l", positive=True)
ok &= report("massless wave is resonant on an open set (omega(k)+omega(l)-omega(k+l)=0, k,l>0)",
             sp.simplify(sp.Abs(k) + sp.Abs(l) - sp.Abs(k + l)) == 0)

sys.exit(0 if ok else 1)
