"""Momentum balance (Definition 3.1 of the general-framework paper) for the observed cases.

For each model this script builds, at the defect, the spatial Ostrogradsky
momenta prescribed by the sewing equations

    pi_{-,m} = - delta S_d / delta Phi_m,    pi_{+,m} = + delta S_d / delta Psi_m,

evaluates the spatial Hamiltonian densities H_-(Phi, pi_-) and H_+(Psi, pi_+)
(the Legendre transform of the bulk Lagrangian in x), reduces modulo the
auxiliary constraint delta S_d / delta lambda = 0 and its time derivatives,
and tests whether H_- - H_+ is a total time derivative of a local function.
That is exactly the hypothesis of Theorem 1.  Defects are transcribed from
the papers cited in each label.  Each check prints one PASS or FAIL line.
"""

import sys
import sympy as sp
from jets import TJets, report

N = 6  # t-jet order


def spatial_hamiltonian(L, K, coords, Z, mom):
    """Legendre transform in x.

    L     : bulk Lagrangian, written with the jet symbols of the Ostrogradsky
            coordinates (coords[m] is the t-jet tuple of Phi_m) and with the
            top spatial derivative d_x^K phi replaced by the symbols Z.
    mom   : list over m of the momentum expressions pi_m (one per component).
    Returns H = sum_{m<K-1} pi_m . Phi_{m+1} + pi_{K-1} . Z - L with Z solved
    from pi_{K-1} = dL/dZ.
    """
    r = len(Z)
    H = 0
    for m in range(K - 1):
        for a in range(r):
            H += mom[m][a] * coords[m + 1][a][0]
    for a in range(r):
        H += mom[K - 1][a] * Z[a]
    H -= L
    eqs = [sp.Eq(mom[K - 1][a], sp.diff(L, Z[a])) for a in range(r)]
    sol = sp.solve(eqs, Z, dict=True)
    assert len(sol) == 1, "Legendre transform not uniquely solvable"
    return sp.expand(H.subs(sol[0]))


def balance(label, J, left, right, aux, L_left, L_right, K, Ld, Zl, Zr,
            constraint_elims=(), simplify_trig=False, explicit_Pd=None):
    """left/right: list over m of list over components of field names."""
    r = len(left[0])
    piL = [[-J.var(Ld, left[m][a]) for a in range(r)] for m in range(K)]
    piR = [[J.var(Ld, right[m][a]) for a in range(r)] for m in range(K)]
    coordsL = [[J[left[m][a]] for a in range(r)] for m in range(K)]
    coordsR = [[J[right[m][a]] for a in range(r)] for m in range(K)]
    HL = spatial_hamiltonian(L_left, K, coordsL, Zl, piL)
    HR = spatial_hamiltonian(L_right, K, coordsR, Zr, piR)
    R = HL - HR
    for (name, k0, expr) in constraint_elims:
        J.eliminate(name, k0, expr, N - 1)
    R = J.reduce(R)
    if simplify_trig:
        R = sp.expand(sp.expand_trig(R))
    if explicit_Pd is not None:
        # The constraint leaves a non-free jet coordinate (Type II), so the
        # Euler-operator test does not apply; compare with the defect momentum.
        res = sp.simplify(sp.expand(J.reduce(R - J.Dt(explicit_Pd))))
        return report(label + " [H_- - H_+ = D_t P~ with the published P~]", res == 0, str(res))
    free = [n for n in J.names if J[n][0] not in J.rules]
    ok, info = J.is_total_derivative(R, free)
    return report(label, ok, str(info))


def sine_gordon_typeI():
    J = TJets(["phi", "psi"], N)
    eps = sp.Symbol("epsilon", positive=True)
    ph, ps = J["phi"], J["psi"]
    Zl, Zr = sp.symbols("Zl Zr")
    U = lambda f: 1 - sp.cos(f)
    Ll = ph[1] ** 2 / 2 - Zl ** 2 / 2 - U(ph[0])
    Lr = ps[1] ** 2 / 2 - Zr ** 2 / 2 - U(ps[0])
    q, w = (ph[0] - ps[0]) / 2, (ph[0] + ps[0]) / 2
    B = 2 * (1 - sp.cos(q)) / eps + 2 * eps * (1 - sp.cos(w))
    Ld = (ph[0] * ps[1] - ps[0] * ph[1]) / 2 - B
    return balance("sine-Gordon, r=1 Type I (BCZ hep-th/0305022)", J, [["phi"]], [["psi"]], [],
                   Ll, Lr, 1, Ld, [Zl], [Zr])


def liouville_free_typeI():
    J = TJets(["phi", "psi"], N)
    a = sp.Symbol("a", positive=True)
    ph, ps = J["phi"], J["psi"]
    Zl, Zr = sp.symbols("Zl Zr")
    Ll = ph[1] ** 2 / 2 - Zl ** 2 / 2 - sp.exp(ph[0])
    Lr = ps[1] ** 2 / 2 - Zr ** 2 / 2  # free massless
    q, w = (ph[0] - ps[0]) / 2, (ph[0] + ps[0]) / 2
    B = 2 * a * sp.exp(w) + sp.exp(q) / a
    Ld = (ph[0] * ps[1] - ps[0] * ph[1]) / 2 - B
    return balance("Liouville | free massless, heterogeneous Type I (BCZ hep-th/0305022)", J,
                   [["phi"]], [["psi"]], [], Ll, Lr, 1, Ld, [Zl], [Zr])


def toda_a2_typeI():
    J = TJets(["p1", "p2", "s1", "s2"], N)
    sig = sp.Symbol("sigma", positive=True)
    ph = sp.Matrix([J["p1"][0], J["p2"][0]])
    ps = sp.Matrix([J["s1"][0], J["s2"][0]])
    pht = sp.Matrix([J["p1"][1], J["p2"][1]])
    pst = sp.Matrix([J["s1"][1], J["s2"][1]])
    Zl = sp.symbols("Zl1 Zl2")
    Zr = sp.symbols("Zr1 Zr2")
    # a_2^(1) roots, |alpha|^2 = 2
    a1 = sp.Matrix([sp.sqrt(2), 0])
    a2 = sp.Matrix([-sp.sqrt(2) / 2, sp.sqrt(6) / 2])
    a0 = -a1 - a2
    roots = [a0, a1, a2]
    # Coxeter element: rotation sending alpha_j -> alpha_{j-1}
    c, s = sp.cos(2 * sp.pi / 3), sp.sin(2 * sp.pi / 3)
    pi = sp.Matrix([[c, -s], [s, c]])
    if sp.simplify(pi * a1 - a0) != sp.zeros(2, 1):
        pi = pi.T
    assert sp.simplify(pi * a1 - a0) == sp.zeros(2, 1)
    D = sp.simplify(2 * (sp.eye(2) - pi).inv())
    E = sp.eye(2) - D
    U = lambda f: sum(sp.exp((al.T * f)[0]) for al in roots) - 3
    Ll = (pht.T * pht)[0] / 2 - (Zl[0] ** 2 + Zl[1] ** 2) / 2 - U(ph)
    Lr = (pst.T * pst)[0] / 2 - (Zr[0] ** 2 + Zr[1] ** 2) / 2 - U(ps)
    q = (ph - ps) / 2
    w = (D.T * ph + D * ps) / 2
    f = sum(sp.exp((al.T * w)[0]) for al in roots) - 3
    g = sum(sp.exp((al.T * D * q)[0]) for al in roots) - 3
    # (A.1): 1/2 phi.E phi_t + phi.D psi_t + 1/2 psi.E psi_t - B
    Ld = ((ph.T * E * pht)[0] / 2 + (ph.T * D * pst)[0] + (ps.T * E * pst)[0] / 2
          - (sig * f + g / sig))
    Ld = sp.expand(Ld)
    return balance("a_2^(1) affine Toda, r=2 Type I (BCZ hep-th/0401020)", J,
                   [["p1", "p2"]], [["s1", "s2"]], [], Ll, Lr, 1, Ld, list(Zl), list(Zr))


def tzitzeica_typeII():
    J = TJets(["u", "v", "lam"], N)
    sig = sp.Symbol("sigma", positive=True)
    u, v, la = J["u"], J["v"], J["lam"]
    Zl, Zr = sp.symbols("Zl Zr")
    U = lambda f: sp.exp(2 * f) + 2 * sp.exp(-f) - 3
    Ll = u[1] ** 2 / 2 - Zl ** 2 / 2 - U(u[0])
    Lr = v[1] ** 2 / 2 - Zr ** 2 / 2 - U(v[0])
    p, q = (u[0] + v[0]) / 2, (u[0] - v[0]) / 2
    f = (sp.exp(2 * p - 2 * la[0]) + sp.exp(-p + la[0]) * (sp.exp(q) + sp.exp(-q))) / sig
    g = sig / 2 * (8 * sp.exp(-la[0]) + sp.exp(2 * la[0]) * (sp.exp(q) + sp.exp(-q)) ** 2)
    Dd = f + g
    Ld = (u[0] * v[1] - v[0] * u[1]) / 2 + la[0] * (u[1] - v[1]) - la[1] * (u[0] - v[0]) - Dd
    # constraint delta S/delta lambda = 0 is algebraic in (u-v)_t: solve for v_1
    C = J.var(Ld, "lam")
    v1 = sp.solve(sp.Eq(C, 0), v[1])
    assert len(v1) == 1
    return balance("Tzitzeica a_2^(2), r=1 Type II (CZ 0908.3126 eq. 3.7)", J, [["u"]], [["v"]],
                   ["lam"], Ll, Lr, 1, Ld, [Zl], [Zr], constraint_elims=[("v", 1, v1[0])],
                   explicit_Pd=f - g)


def nls():
    J = TJets(["u", "ub", "v", "vb"], N)
    al = sp.Symbol("alpha", positive=True)
    u, ub, v, vb = J["u"], J["ub"], J["v"], J["vb"]
    Zu, Zub, Zv, Zvb = sp.symbols("Zu Zub Zv Zvb")
    I = sp.I
    Ll = I / 2 * (ub[0] * u[1] - ub[1] * u[0]) - Zu * Zub + (u[0] * ub[0]) ** 2
    Lr = I / 2 * (vb[0] * v[1] - vb[1] * v[0]) - Zv * Zvb + (v[0] * vb[0]) ** 2
    d, db = u[0] - v[0], ub[0] - vb[0]
    Om = sp.sqrt(al ** 2 - d * db)
    dlog = (u[1] - v[1]) / d - (ub[1] - vb[1]) / db
    Bcal = (al ** 2 - d * db) / 3 + u[0] * ub[0] + v[0] * vb[0]
    Ld = Om * (I / 2 * dlog + Bcal)
    return balance("NLS (CZ nlin/0512038 eqs. 2.9-2.10)", J, [["u", "ub"]], [["v", "vb"]], [],
                   Ll, Lr, 1, Ld, [Zu, Zub], [Zv, Zvb])


def kdv():
    J = TJets(["p", "P1", "q", "Q1", "mu"], N)
    al = sp.Symbol("alpha")
    p, P1, q, Q1, mu = J["p"], J["P1"], J["q"], J["Q1"], J["mu"]
    Zl, Zr = sp.symbols("Zl Zr")
    Ll = P1[0] * p[1] / 2 - P1[0] ** 3 - Zl ** 2 / 2
    Lr = Q1[0] * q[1] / 2 - Q1[0] ** 3 - Zr ** 2 / 2
    w = p[0] - q[0]
    Ld = ((q[0] * p[1] - p[0] * q[1]) / 4
          + (P1[0] ** 2 + P1[0] * Q1[0] + Q1[0] ** 2) * w
          + mu[0] * (P1[0] + Q1[0] - 2 * al - w ** 2 / 2)
          - 3 * (P1[0] + Q1[0]) * w * (al + w ** 2 / 4)
          + 6 * al ** 2 * w + 2 * al * w ** 3 + sp.Rational(9, 40) * w ** 5)
    Q1sol = 2 * al + w ** 2 / 2 - P1[0]
    return balance("KdV, constrained defect with multiplier (CZ nlin/0512038 eq. 9.16)", J,
                   [["p"], ["P1"]], [["q"], ["Q1"]], ["mu"], Ll, Lr, 2, Ld, [Zl], [Zr],
                   constraint_elims=[("Q1", 0, Q1sol)])


def mkdv(variant=1):
    J = TJets(["p", "P1", "q", "Q1", "mu"], N)
    al = sp.Symbol("alpha")
    p, P1, q, Q1, mu = J["p"], J["P1"], J["q"], J["Q1"], J["mu"]
    Zl, Zr = sp.symbols("Zl Zr")
    Ll = P1[0] * p[1] / 2 - P1[0] ** 4 / 2 + Zl ** 2 / 2
    Lr = Q1[0] * q[1] / 2 - Q1[0] ** 4 / 2 + Zr ** 2 / 2
    w = p[0] - q[0]
    if variant == 1:
        rest = al / 6 * sp.cos(w) * (P1[0] ** 2 + Q1[0] ** 2 - 4 * P1[0] * Q1[0]
                                     + al * (P1[0] + Q1[0]) * sp.sin(w) + al ** 2)
    else:
        rest = al / 6 * (sp.cos(w) * (P1[0] ** 2 + Q1[0] ** 2 - 4 * P1[0] * Q1[0])
                         + al * (P1[0] + Q1[0]) * sp.sin(w) + al ** 2)
    Bcal = mu[0] * (P1[0] + Q1[0] - al * sp.sin(w)) + rest
    Ld = (q[0] * p[1] - p[0] * q[1]) / 4 - Bcal
    Q1sol = al * sp.sin(w) - P1[0]
    return balance(f"mKdV, constrained defect, reading {variant} of CZ nlin/0512038 eq. 7.22",
                   J, [["p"], ["P1"]], [["q"], ["Q1"]], ["mu"], Ll, Lr, 2, Ld, [Zl], [Zr],
                   constraint_elims=[("Q1", 0, Q1sol)], simplify_trig=True)


def boussinesq():
    J = TJets(["u", "U1", "v", "V1"], N)
    c, kap, lam, s0, r0 = sp.symbols("c kappa lambda sigma_0 rho_0", positive=True)
    u, U1, v, V1 = J["u"], J["U1"], J["v"], J["V1"]
    Zl, Zr = sp.symbols("Zl Zr")
    L = lambda ut, ux, Z: ut ** 2 / (2 * c ** 2) - ux ** 2 / 2 - lam / 3 * ux ** 3 - kap ** 2 / 2 * Z ** 2
    Ll, Lr = L(u[1], U1[0], Zl), L(v[1], V1[0], Zr)
    a = kap / (sp.sqrt(3) * c)
    b = 2 * a
    mu = 2 * lam / (3 * b)
    wv = sp.Symbol("wv")  # stands for u - v
    sig = s0 + mu * wv
    rho = r0 + sig / (2 * mu) * (1 - sig ** 2 / (3 * c ** 2))
    tau = sp.integrate(-a * sig * rho / kap ** 2, wv)
    fg = -sig ** 2 / (4 * mu * c ** 2)
    sub = {wv: u[0] - v[0]}
    F = a * U1[0] + b * V1[0] + fg.subs(sub)
    G = b * U1[0] + a * V1[0] + fg.subs(sub)
    H = (sig.subs(sub) / 2 * (b * U1[0] ** 2 + 2 * a * U1[0] * V1[0] + b * V1[0] ** 2)
         + rho.subs(sub) * (U1[0] + V1[0]) + tau.subs(sub))
    Ld = sp.expand(u[1] * F + v[1] * G + H)
    return balance("Boussinesq, Type I in Ostrogradsky variables (CZ 2306.03772 eqs. 3.43)", J,
                   [["u"], ["U1"]], [["v"], ["V1"]], [], Ll, Lr, 2, Ld, [Zl], [Zr])


if __name__ == "__main__":
    results = [
        sine_gordon_typeI(),
        liouville_free_typeI(),
        toda_a2_typeI(),
        tzitzeica_typeII(),
        nls(),
        kdv(),
        mkdv(1),
        boussinesq(),
    ]
    sys.exit(0 if all(results) else 1)
