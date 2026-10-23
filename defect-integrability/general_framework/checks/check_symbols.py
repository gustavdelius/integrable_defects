"""Generating quadratic symbols m(k; epsilon) of the defect hierarchies.

Definition 7.5 (nondegeneracy) and Theorem 7.4 need the quadratic symbols m_n(k)
of the charges Q_n.  Their generating function m(k; epsilon) = sum_n m_n(k) eps^n
is computed here exactly in epsilon, perturbatively in the amplitude eta of a
single Fourier mode E = exp(i(kx - omega t)):

  * the bulk field is eta (a E + conj), D_x = i k E d/dE, D_t = -i omega E d/dE;
  * the branch equation is solved at order eta (first harmonic, exactly in eps)
    and for the zero mode at order eta^2;
  * m is the coefficient of eta^2 |a|^2 in the zero mode of the generating density.

Second harmonics, and the second-order correction of the bulk field, never enter
the zero mode at order eta^2, because D_x and D_t annihilate zero modes and the
linearised branch equation has constant coefficients.

If m is not a polynomial in eps, infinitely many m_n are nonzero (nondegeneracy).
For kinematic families the m_n have distinct weights (Lemma 6.5) and are
therefore linearly independent; for Boussinesq, linear independence of the first
m_n is checked directly.  One PASS or FAIL line per check.
"""

import sys
import sympy as sp
from jets import report

eps, eta, E, k, w, a, ab = sp.symbols("epsilon eta E k omega a abar")
I = sp.I


def Dx(f):
    return sp.expand(I * k * E * sp.diff(f, E))


def Dt(f):
    return sp.expand(-I * w * E * sp.diff(f, E))


def ser2(f):
    return sp.expand(sp.series(f, eta, 0, 3).removeO())


def harm(f, n):
    """Coefficient of E^n in a Laurent polynomial in E with rational coefficients."""
    if f == 0:
        return 0
    num, den = sp.fraction(sp.together(sp.expand(f)))
    pd = sp.Poly(den, E)
    assert len(pd.terms()) == 1, "denominator must be a monomial in E"
    (pdeg,), dcoef = pd.terms()[0]
    pn = sp.Poly(num, E)
    return sp.together(pn.coeff_monomial(E ** (n + pdeg)) / dcoef) if n + pdeg >= 0 else 0


def solve_branch(G, unknowns):
    """unknowns: dict name -> (field form).  G: list of residuals as functions of fields.
    Each unknown D = eta*(A E^{s} + ...) + eta^2*(B0 + second harmonics)."""
    syms = {}
    fields = {}
    for name, harmonics in unknowns.items():
        A = {h: sp.Symbol(f"A_{name}_{h}") for h in harmonics}
        B0 = sp.Symbol(f"B0_{name}")
        C2 = {h: sp.Symbol(f"C2_{name}_{h}") for h in (2, -2)}
        fields[name] = eta * sum(A[h] * E ** h for h in harmonics) + eta ** 2 * (B0 + sum(C2[h] * E ** h for h in C2))
        syms[name] = (A, B0)
    res = [ser2(r) for r in G(fields)]
    eqs1, unk1 = [], []
    for name, (A, B0) in syms.items():
        unk1 += list(A.values())
    for r in res:
        r1 = r.coeff(eta, 1)
        for h in (1, -1):
            c = harm(r1, h)
            if c != 0:
                eqs1.append(c)
    sol1 = sp.solve(eqs1, unk1, dict=True)
    assert len(sol1) == 1, sol1
    sol1 = sol1[0]
    eqs2 = [harm(sp.expand(r.coeff(eta, 2).subs(sol1)), 0) for r in res]
    eqs2 = [e for e in eqs2 if e != 0]
    unk2 = [B0 for (A, B0) in syms.values()]
    sol2 = sp.solve(eqs2, unk2, dict=True)
    assert len(sol2) == 1, sol2
    allsol = dict(sol1)
    allsol.update(sol2[0])
    return {n: f.subs(allsol) for n, f in fields.items()}


def symbol_of(Gdens, fields):
    z = harm(ser2(Gdens(fields)).coeff(eta, 2), 0)
    return sp.simplify(sp.expand(z).coeff(a, 1).coeff(ab, 1))


def nonpolynomial(m, label, nterms=12):
    s = sp.series(m, eps, 0, nterms + 1).removeO()
    coeffs = [sp.simplify(sp.expand(s).coeff(eps, n)) for n in range(nterms + 1)]
    nz = [n for n, c in enumerate(coeffs) if c != 0]
    denom_has_eps = sp.denom(sp.together(m)).has(eps)
    ok = denom_has_eps and len(nz) >= 4
    report(f"{label}: generating symbol is not a polynomial in epsilon (nonzero orders {nz})", ok)
    return ok, coeffs


ok = True

# sine-Gordon, U = 1 - cos(phi): omega^2 = k^2 + 1
phi = eta * (a * E + ab / E)
F = lambda f: [sp.sin(f["D"] / 2) - eps * (Dx(phi) - Dt(phi) - Dt(f["D"])) - eps ** 2 * sp.sin(phi + f["D"] / 2)]
fl = solve_branch(F, {"D": (1, -1)})
m = symbol_of(lambda f: 2 * (1 - sp.cos(f["D"] / 2)) / eps + 2 * eps * (1 - sp.cos(phi + f["D"] / 2)), fl)
m = sp.simplify(m.subs(w, sp.sqrt(k ** 2 + 1)))
print("INFO: sine-Gordon m(k;eps) =", sp.factor(m))
o, cs = nonpolynomial(m, "sine-Gordon")
ok &= o
# weight check: with k = sinh(theta), omega = cosh(theta) is the measure factor dk = omega dtheta,
# and m_n / omega should be proportional to exp(+-n theta)
th = sp.Symbol("theta", real=True)
weights = []
for n, c in enumerate(cs):
    if c != 0:
        cth = sp.simplify((c / sp.sqrt(k ** 2 + 1)).subs(sp.sqrt(k ** 2 + 1), sp.cosh(th))
                          .subs(k, sp.sinh(th)).rewrite(sp.exp))
        r = sp.simplify(cth / sp.exp(n * th))
        r2 = sp.simplify(cth / sp.exp(-n * th))
        weights.append(r.free_symbols.isdisjoint({th}) or r2.free_symbols.isdisjoint({th}))
ok &= report("sine-Gordon: each m_n has a definite boost weight (Lemma 6.5)", all(weights))

# a_2^(1) Toda, family (8.5) with eps = sigma (Section 8.2): M = 3I, E = nu J with J the rotation
# generator and nu^2 = 1/3, ghat''(0) = 4I, so the generating density E_d = eps U(w) + ghat(q)/eps
# has zero first variation (alternative (i)): only the linear branch enters.  Two components of
# equal mass, so the symbol is a 2x2 Hermitian matrix K: the x-average of the quadratic part of
# E_d on u = A e^{i(kx - omega t)} + cc is A^dagger K A.
nu, kr, wr, er = sp.symbols("nu k_r omega_r epsilon_r", positive=True)
Jm = sp.Matrix([[0, -1], [1, 0]])
Em = nu * Jm
Dm = sp.eye(2) - Em
Av, Qa = sp.Matrix(sp.symbols("A1 A2")), sp.Matrix(sp.symbols("Qa1 Qa2"))
dxs, dts = I * kr, -I * wr
# left sewing equation phi_x = E phi_t + D psi_t - B_phi, psi = u - 2q, w = u - D q,
# B_phi = (D f' + g')/2 with f' = 3 eps w, g' = 4 q/eps (linearised)
sew = dxs * Av - (Em * dts * Av + Dm * dts * (Av - 2 * Qa) - (3 * er * Dm * (Av - Dm * Qa) + 4 * Qa / er) / 2)
solq = sp.solve(list(sew), list(Qa), dict=True)[0]
RQ = sp.Matrix(2, 2, lambda i, j: sp.diff(Qa[i].subs(solq), Av[j]))
RW = sp.eye(2) - Dm * RQ
Kt = 3 * er * RW.H * RW + 4 / er * RQ.H * RQ
onshell = {wr: sp.sqrt(kr ** 2 + 3)}
zpol = {1: sp.Matrix([1, -I]) / sp.sqrt(2), -1: sp.Matrix([1, I]) / sp.sqrt(2)}   # E z_s = i s nu z_s
ok &= report("a_2 Toda: E z_s = i s nu z_s, and K has no cross term between the two polarizations",
             all(sp.simplify(Em * zpol[s_] - I * s_ * nu * zpol[s_]) == sp.zeros(2, 1) for s_ in (1, -1))
             and sp.simplify(((zpol[1].H * Kt * zpol[-1])[0]).subs(onshell)) == 0)
lr = wr + kr
mts = {s_: sp.simplify((zpol[s_].H * Kt * zpol[s_])[0]) for s_ in (1, -1)}
ok &= report("a_2 Toda: m_s = 4 eps (3 + l^2)/(4 - 4 s nu eps l + eps^2 l^2 (1 + nu^2)), l = omega + k, for every nu",
             all(sp.simplify((mts[s_] - 4 * er * (3 + lr ** 2)
                              / (4 - 4 * s_ * nu * er * lr + er ** 2 * lr ** 2 * (1 + nu ** 2))).subs(onshell)) == 0
                 for s_ in (1, -1)))
th = sp.Symbol("theta", real=True)
rap = {kr: sp.sqrt(3) * sp.sinh(th), wr: sp.sqrt(3) * sp.cosh(th), nu: 1 / sp.sqrt(3)}
mrap = {s_: 2 * sp.sqrt(3) * er * sp.sqrt(3) * sp.cosh(th) * sp.exp(th)
        / (1 - s_ * er * sp.exp(th) + er ** 2 * sp.exp(2 * th)) for s_ in (1, -1)}
ok &= report("a_2 Toda: at nu^2 = 1/3, with k = sqrt3 sinh(theta), m_s = 2 sqrt3 eps omega e^theta/"
             "(1 - s eps e^theta + eps^2 e^(2 theta)), the table entry",
             all(sp.simplify((mts[s_].subs(rap) - mrap[s_]).rewrite(sp.exp)) == 0 for s_ in (1, -1)))
X_ = sp.Symbol("X")
okc = True
for s_ in (1, -1):
    ser = sp.series(X_ / (1 - s_ * X_ + X_ ** 2), X_, 0, 13).removeO()
    for n in range(1, 13):
        cn = ser.coeff(X_, n)
        okc &= sp.simplify(cn - s_ ** (n - 1) * sp.sin(n * sp.pi / 3) / sp.sin(sp.pi / 3)) == 0
        okc &= (cn == 0) == (n % 3 == 0)
ok &= report("a_2 Toda: m_(n,s) = 2 sqrt3 s^(n-1) omega e^(n theta) sin(n pi/3)/sin(pi/3) for n <= 12; "
             "zero exactly when 3 | n, so the nonzero m_(n,+) are distinct powers of e^theta", okc)


def toda_a2_jets(N=5):
    """Cross-check of Proposition 7.5 (i): the quadratic parts of the actual charges Q_n of (8.5),
    from the formal branch of the left sewing equation in jet space.  Only the linear branch can
    reach the quadratic part, since E_d has zero first variation; t-derivatives are reduced by the
    linearised flow u_t = p, p_t = u_xx - 3u.  nu is kept symbolic."""
    NJ = 2 * N + 4
    uj = [[sp.Symbol(f"u{i}_{j}") for j in range(NJ)] for i in range(2)]
    pj = [[sp.Symbol(f"p{i}_{j}") for j in range(NJ)] for i in range(2)]

    def Dtj(expr):
        out = 0
        for i in range(2):
            for j in range(NJ - 2):
                out += sp.diff(expr, uj[i][j]) * pj[i][j] + sp.diff(expr, pj[i][j]) * (uj[i][j + 2] - 3 * uj[i][j])
        return sp.expand(out)

    def tr(expr):
        e_ = sp.expand(expr)
        return sp.expand(sum(e_.coeff(er, n_) * er ** n_ for n_ in range(N + 1)))

    uv = sp.Matrix([uj[0][0], uj[1][0]])
    pv = sp.Matrix([pj[0][0], pj[1][0]])
    ux = sp.Matrix([uj[0][1], uj[1][1]])
    q = sp.zeros(2, 1)
    # eps times the linearised left sewing equation: 4q = 2 eps (p - u_x) - 4 eps D D_t q - 3 eps^2 D (u - Dq)
    for _ in range(N + 1):
        q = ((2 * er * (pv - ux) - 4 * er * Dm * q.applyfunc(Dtj) - 3 * er ** 2 * Dm * (uv - Dm * q)) / 4).applyfunc(tr)
    res = 4 * q - 2 * er * (pv - ux) + 4 * er * Dm * q.applyfunc(Dtj) + 3 * er ** 2 * Dm * (uv - Dm * q)
    good = all(tr(r_) == 0 for r_ in res)
    wv = uv - Dm * q
    Ed = sp.expand(3 * er * (wv.T * wv)[0] / 2 + 2 * (q.T * q)[0] / er)
    av, bv = sp.Matrix(sp.symbols("a1 a2")), sp.Matrix(sp.symbols("b1 b2"))   # b stands for conj(a)
    hat, hatc = {}, {}
    for i in range(2):
        for j in range(NJ):
            hat[uj[i][j]], hatc[uj[i][j]] = (I * kr) ** j * av[i], (-I * kr) ** j * bv[i]
            hat[pj[i][j]], hatc[pj[i][j]] = (I * kr) ** j * (-I * wr) * av[i], (-I * kr) ** j * (I * wr) * bv[i]
    for n_ in range(1, N + 1):
        avg = 0
        for term in sp.Add.make_args(sp.expand(Ed.coeff(er, n_))):
            cf, facs = term.as_coeff_mul()
            js = []
            for f_ in facs:
                if f_.is_Pow and f_.base in hat:
                    js += [f_.base] * int(f_.exp)
                elif f_ in hat:
                    js.append(f_)
                else:
                    cf *= f_
            good &= len(js) == 2
            avg += cf * (hat[js[0]] * hatc[js[1]] + hatc[js[0]] * hat[js[1]])
        avg = sp.expand(avg)
        Kn = sp.Matrix(2, 2, lambda i, j: avg.coeff(bv[i]).coeff(av[j]))
        good &= sp.simplify(((zpol[1].H * Kn * zpol[-1])[0]).subs(onshell)) == 0
        for s_ in (1, -1):
            pred = sp.series(mts[s_], er, 0, n_ + 1).removeO().coeff(er, n_)
            good &= sp.simplify(((zpol[s_].H * Kn * zpol[s_])[0] - pred).subs(onshell)) == 0
    return report(f"a_2 Toda, Proposition 7.5 (i): the quadratic parts of Q_1..Q_{N}, from the formal branch in "
                  "jet space, have no cross term and the symbols m_(n,s) above, for every nu", good)


ok &= toda_a2_jets()

# NLS: u = eta a E, ub = eta abar / E, omega = k^2
u, ub = eta * a * E, eta * ab / E
def Fn(f):
    W, Wb = f["W"], f["Wb"]
    root = sp.sqrt(1 - eps ** 2 * (2 * u - W) * (2 * ub - Wb))
    return [W * root - eps * (2 * Dx(u) - Dx(W)), Wb * root - eps * (2 * Dx(ub) - Dx(Wb))]
fl = solve_branch(Fn, {"W": (1,), "Wb": (-1,)})
m = symbol_of(lambda f: (sp.sqrt(1 - eps ** 2 * (2 * u - f["W"]) * (2 * ub - f["Wb"])) - 1) / eps, fl)
print("INFO: NLS m(k;eps) =", sp.factor(m))
o, cs = nonpolynomial(m, "NLS")
ok &= o
degs = [sp.Poly(c, k).degree() if c != 0 else None for c in cs]
nz = [d for d in degs if d is not None]
ok &= report(f"NLS: m_n homogeneous in k of degree n-1 (dilation weight, Lemma 6.5): {degs}",
             all(sp.Poly(c, k).is_monomial for c in cs if c != 0) and len(set(nz)) == len(nz))

# KdV: u = eta (a E + abar/E), branch d = (eps/2)(2u - d_x - d^2/2), density -d
uu = eta * (a * E + ab / E)
fl = solve_branch(lambda f: [f["d"] - eps / 2 * (2 * uu - Dx(f["d"]) - f["d"] ** 2 / 2)], {"d": (1, -1)})
m = symbol_of(lambda f: -f["d"], fl)
print("INFO: KdV m(k;eps) =", sp.factor(m))
o, cs = nonpolynomial(m, "KdV")
ok &= o
degs = [sp.Poly(c, k).degree() if c != 0 else None for c in cs]
nz = [d for d in degs if d is not None]
ok &= report(f"KdV: nonzero m_n are monomials in k of distinct degrees: {degs}",
             all(sp.Poly(c, k).is_monomial for c in cs if c != 0) and len(set(nz)) == len(nz))

# mKdV: v = eta (a E + abar/E), branch sin w = eps (2 v - w_x), density (cos w - 1)/eps
vv = eta * (a * E + ab / E)
fl = solve_branch(lambda f: [sp.sin(f["w"]) - eps * (2 * vv - Dx(f["w"]))], {"w": (1, -1)})
m = symbol_of(lambda f: (sp.cos(f["w"]) - 1) / eps, fl)
print("INFO: mKdV m(k;eps) =", sp.factor(m))
o, cs = nonpolynomial(m, "mKdV")
ok &= o
degs = [sp.Poly(c, k).degree() if c != 0 else None for c in cs]
nz = [d for d in degs if d is not None]
ok &= report(f"mKdV: nonzero m_n are monomials in k of distinct degrees: {degs}",
             all(sp.Poly(c, k).is_monomial for c in cs if c != 0) and len(set(nz)) == len(nz))

# Boussinesq (c = kappa = 1, lambda = 3): branch from pi_{-,1}; density -w (i.e. u - v ~ w)
c_, kap, lam = 1, 1, 3
al_ = kap / (sp.sqrt(3) * c_)
be_ = 2 * al_
mu = sp.Rational(2) * lam / (3 * be_)
ub_ = eta * (a * E + ab / E)
def Fb(f):
    W = f["w"]
    s0 = 1 / eps
    sig = s0 + mu * W
    rho = sp.expand((sig * (1 - sig ** 2 / (3 * c_ ** 2)) - s0 * (1 - s0 ** 2 / (3 * c_ ** 2))) / (2 * mu))
    ux, ut = Dx(ub_), Dt(ub_)
    vx, vt = ux - Dx(W), ut - Dt(W)
    fg = -sig ** 2 / (4 * mu * c_ ** 2)
    # dD/dU1 = alpha u_t + beta v_t + sigma (beta u_x + alpha v_x) + rho
    r = kap ** 2 * Dx(ux) - (al_ * ut + be_ * vt + sig * (be_ * ux + al_ * vx) + rho)
    return [sp.expand(2 * c_ ** 2 * eps ** 2 * r)]
fl = solve_branch(Fb, {"w": (1, -1)})
m = symbol_of(lambda f: f["w"], fl)
m = sp.simplify(m.subs(w, c_ * k * sp.sqrt(1 + kap ** 2 * k ** 2)))
print("INFO: Boussinesq m(k;eps) =", sp.factor(m))
o, cs = nonpolynomial(m, "Boussinesq")
ok &= o
# linear independence of the first nonzero m_n as functions of k (rank at sample points)
# The family parameter sigma_0 is not kinematic, so Lemma 6.5 does not apply.  Estimate the
# rank of the span of the computed symbols from many generic sample points (a lower bound).
nzc = [c for c in cs if c != 0]
pts = [sp.Rational(2 * j + 1, 7) for j in range(2 * len(nzc))]
M = sp.Matrix([[sp.N(c.subs(k, p), 50) for p in pts] for c in nzc])
rk = M.rank(iszerofunc=lambda x: abs(x) < 1e-35)
ok &= report(f"Boussinesq: the {len(nzc)} computed nonzero m_n span a space of dimension {rk} "
             f"(at most one linear relation)", rk >= len(nzc) - 1)

sys.exit(0 if ok else 1)
