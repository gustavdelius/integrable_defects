"""Formal Bäcklund branches and defect-generated conservation laws.

This checks, model by model, the hypotheses and conclusions of Lemma 4.5
(formal branch), Proposition 4.3 (closure) and Theorem 4.6 of the
general-framework paper:

  1. one promoted sewing equation (or the multiplier constraint) is solved for
     the jump as a formal series in the spectral parameter epsilon, by the
     formal implicit-function iteration of Lemma 4.5;
  2. every other promoted sewing equation, derived here from the published
     defect Lagrangian (not transcribed), is checked on shell order by order:
     this is the formal-branch hypothesis;
  3. the conserved defect density named by the closure relation is expanded,
     and every coefficient Q_n is checked to be a conserved density of the
     bulk equation; triviality (Q_n a total x-derivative) is recorded.

Densities are functions of x-jets of the evolution variables, so conservation
and triviality are decided by x-Euler operators (jets.py).  Orders near the
truncation order are lost when the jump has a 1/epsilon offset; the number of
checked orders is stated in each label.  One PASS or FAIL line per check.
"""

import sys
import sympy as sp
from jets import XJets, report, series_trunc

eps = sp.Symbol("epsilon")


def trunc(expr, N):
    return series_trunc(expr, eps, N)


def coeff(expr, n):
    return sp.expand(expr).coeff(eps, n)


def formal_solve(F, unknowns, N, c0):
    """Solve F = 0 where F = c0 * unknowns + O(eps) (Lemma 4.5)."""
    sol = {x: sp.Integer(0) for x in unknowns}
    c0inv = c0.inv()
    for _ in range(N + 1):
        res = sp.Matrix([trunc(r, N) for r in F(sol)])
        upd = c0inv * res
        sol = {x: trunc(sol[x] - upd[i], N) for i, x in enumerate(unknowns)}
    final = [trunc(r, N) for r in F(sol)]
    assert all(sp.simplify(r) == 0 for r in final), "formal solve did not converge"
    return sol


def euler_t(B, y, tder, sub):
    """t-Euler derivative of the defect density B in the boundary variable y.
    B is affine in the first time derivatives tder[.]; the time derivative is
    taken in boundary variables first, then the branch values `sub` are
    substituted (sub must contain every boundary variable and every tder)."""
    a = sp.diff(B, y)
    b = sp.diff(B, tder[y]) if y in tder else 0
    dtb = sum(sp.diff(b, z) * tder[z] for z in tder) if b != 0 else 0
    return sp.expand((a - dtb).xreplace(sub))


def orders_vanish(resids, lo, hi):
    for r in resids:
        for n in range(lo, hi + 1):
            if sp.simplify(coeff(r, n)) != 0:
                return False
    return True


def check_density(label, X, Q, N):
    ok_all = True
    nontriv = []
    for n in range(1, N + 1):
        Qn = sp.expand(coeff(Q, n))
        ok_all &= report(f"{label}: Q_{n} is a conserved density", X.is_conserved(Qn))
        if not X.is_trivial(Qn):
            nontriv.append(n)
    print(f"INFO: {label}: nontrivial Q_n for n in {nontriv}")
    return ok_all


# ---------------------------------------------------------------- sine-Gordon
def sine_gordon(N=5):
    X = XJets(["phi", "chi"], 2 * N + 8)
    ph, ch = X["phi"], X["chi"]
    X.set_flow("phi", ch[0])
    X.set_flow("chi", ph[2] - sp.sin(ph[0]))
    a, b, at, bt = sp.symbols("a b a_t b_t")   # boundary phi, psi and their t-derivatives
    tder = {a: at, b: bt}
    Bpot = 2 * (1 - sp.cos((a - b) / 2)) / eps + 2 * eps * (1 - sp.cos((a + b) / 2))
    Ld = (a * bt - b * at) / 2 - Bpot          # BCZ defect in the form of Theorem A

    def sub_of(D):
        return {a: ph[0], b: ph[0] + D, at: ch[0], bt: ch[0] + X.Dt(D)}

    # branch from the left sewing equation pi_- = -phi_x = -dS/dphi, scaled by epsilon
    G = lambda s: [sp.expand(eps * (ph[1] - euler_t(Ld, a, tder, sub_of(s["D"]))))]
    D = formal_solve(G, ["D"], N, sp.Matrix([[sp.Rational(1, 2)]]))["D"]
    sub = sub_of(D)
    r = trunc(eps * (-(ph[1] + X.Dx(D)) - euler_t(Ld, b, tder, sub)), N)  # pi_+ = -psi_x = dS/dpsi
    ok = report("sine-Gordon: right sewing equation holds on shell, orders 0..N",
                orders_vanish([r], 0, N))
    Q = trunc(Bpot.xreplace(sub), N)            # E_d of a Lagrangian affine in velocities
    return check_density("sine-Gordon E_d", X, Q, N) and ok


# ------------------------------------------------------------------------ NLS
def nls(N=5):
    X = XJets(["u", "ub"], 2 * N + 8)
    u, ub = X["u"], X["ub"]
    I = sp.I
    X.set_flow("u", I * (u[2] + 2 * u[0] ** 2 * ub[0]))
    X.set_flow("ub", -I * (ub[2] + 2 * ub[0] ** 2 * u[0]))
    U, Ub, V, Vb, Ut, Ubt, Vt, Vbt = sp.symbols("U Ub V Vb U_t Ub_t V_t Vb_t")
    tder = {U: Ut, Ub: Ubt, V: Vt, Vb: Vbt}
    al = 1 / eps
    d, db = U - V, Ub - Vb
    Om = sp.sqrt(al ** 2 - d * db)
    Bd = Om * (I / 2 * ((Ut - Vt) / d - (Ubt - Vbt) / db) + (al ** 2 - d * db) / 3 + U * Ub + V * Vb)

    def sub_of(w, wb):
        return {U: u[0], Ub: ub[0], V: -u[0] + w, Vb: -ub[0] + wb,
                Ut: X.flow["u"], Ubt: X.flow["ub"],
                Vt: -X.flow["u"] + X.Dt(w), Vbt: -X.flow["ub"] + X.Dt(wb)}

    # branch: difference of the two sewing equations, CZ (2.21) second line, scaled
    def F(s):
        w, wb = s["w"], s["wb"]
        dd, ddb = 2 * u[0] - w, 2 * ub[0] - wb
        root = sp.sqrt(1 - eps ** 2 * dd * ddb)
        return [w * root - eps * (2 * u[1] - X.Dx(w)), wb * root - eps * (2 * ub[1] - X.Dx(wb))]

    sol = formal_solve(F, ["w", "wb"], N, sp.eye(2))
    w, wb = sol["w"], sol["wb"]
    sub = sub_of(w, wb)
    # the four sewing equations (2.4): u_x = dB/dub, ub_x = dB/du, v_x = -dB/dvb, vb_x = -dB/dv
    rs = [u[1] - euler_t(Bd, Ub, tder, sub), ub[1] - euler_t(Bd, U, tder, sub),
          (-u[1] + X.Dx(w)) + euler_t(Bd, Vb, tder, sub),
          (-ub[1] + X.Dx(wb)) + euler_t(Bd, V, tder, sub)]
    rs = [trunc(eps * r, N) for r in rs]
    ok = report("NLS: all four sewing equations of CZ (2.9)-(2.10) hold on shell, orders 0..N-1",
                orders_vanish(rs, 0, N - 1))
    Q = trunc(Om.xreplace(sub) - 1 / eps, N)   # defect number, CZ (2.19)-(2.20)
    return check_density("NLS defect number N_d", X, Q, N) and ok


# ------------------------------------------------------------------------ KdV
def kdv(N=6):
    X = XJets(["u"], 3 * N + 10)
    u = X["u"]
    X.set_flow("u", 6 * u[0] * u[1] - u[3])
    d = formal_solve(lambda s: [s["d"] - eps / 2 * (2 * u[0] - X.Dx(s["d"]) - s["d"] ** 2 / 2)],
                     ["d"], N, sp.Matrix([[1]]))["d"]
    p, q, P1, Q1, mu, pt, qt, al = sp.symbols("p q P1 Q1 mu p_t q_t alpha")
    P1t, Q1t, mut = sp.symbols("P1_t Q1_t mu_t")
    tder = {p: pt, q: qt, P1: P1t, Q1: Q1t, mu: mut}
    w_ = p - q
    B = ((q * pt - p * qt) / 4 + (P1 ** 2 + P1 * Q1 + Q1 ** 2) * w_
         + mu * (P1 + Q1 - 2 * al - w_ ** 2 / 2) - 3 * (P1 + Q1) * w_ * (al + w_ ** 2 / 4)
         + 6 * al ** 2 * w_ + 2 * al * w_ ** 3 + sp.Rational(9, 40) * w_ ** 5)
    p_t = 3 * u[0] ** 2 - u[2]          # CZ (9.4), decaying sector
    q_x = u[0] - X.Dx(d)
    pv = sp.Symbol("p_value")            # p enters only through derivatives and p - q
    sub = {al: -1 / eps ** 2, p: pv, q: pv - 2 / eps - d, P1: u[0], Q1: q_x,
           pt: p_t, qt: p_t - X.Dt(d)}
    musol = sp.solve(sp.Eq(-u[1], -sp.diff(B, P1).xreplace(sub)), mu)[0]  # pi_{-,1} = -p_xx
    sub.update({mu: musol, P1t: X.Dt(u[0]), Q1t: X.Dt(q_x), mut: X.Dt(musol)})
    # Ostrogradsky momenta of L = p_x p_t/2 - p_x^3 - p_xx^2/2 on the decaying sector:
    rs = [-X.Dx(q_x) - sp.diff(B, Q1).xreplace(sub),            # pi_{+,1} = dS/dQ1
          -p_t / 2 + euler_t(B, p, tder, sub),                   # pi_{-,0} = -dS/dp
          -(p_t - X.Dt(d)) / 2 - euler_t(B, q, tder, sub),       # pi_{+,0} = dS/dq
          (P1 + Q1 - 2 * al - w_ ** 2 / 2).xreplace(sub)]        # dS/dmu = 0
    rs = [trunc(sp.expand(r).subs(pv, 0), N) for r in rs]
    ok = report("KdV: all promoted sewing equations of CZ (9.16) hold on shell, orders -2..N-2",
                orders_vanish(rs, -2, N - 2))
    return check_density("KdV mass defect charge q - p", X, -d, N) and ok


# ----------------------------------------------------------------------- mKdV
def mkdv(N=6):
    X = XJets(["v"], 3 * N + 10)
    v = X["v"]
    X.set_flow("v", 6 * v[0] ** 2 * v[1] + v[3])
    w = formal_solve(lambda s: [sp.sin(s["w"]) - eps * (2 * v[0] - X.Dx(s["w"]))],
                     ["w"], N, sp.Matrix([[1]]))["w"]
    p, q, P1, Q1, mu, pt, qt, al = sp.symbols("p q P1 Q1 mu p_t q_t alpha")
    P1t, Q1t, mut = sp.symbols("P1_t Q1_t mu_t")
    tder = {p: pt, q: qt, P1: P1t, Q1: Q1t, mu: mut}
    w_ = p - q
    Bcal = (mu * (P1 + Q1 - al * sp.sin(w_))
            + al / 6 * sp.cos(w_) * (P1 ** 2 + Q1 ** 2 - 4 * P1 * Q1
                                     + al * (P1 + Q1) * sp.sin(w_) + al ** 2))
    B = (q * pt - p * qt) / 4 - Bcal     # CZ (7.20), (7.22)
    p_t = 2 * v[0] ** 3 + v[2]           # CZ (7.4)
    q_x = v[0] - X.Dx(w)
    pv = sp.Symbol("p_value")
    sub = {al: 1 / eps, p: pv, q: pv - w, P1: v[0], Q1: q_x, pt: p_t, qt: p_t - X.Dt(w)}
    musol = sp.solve(sp.Eq(v[1], -sp.diff(B, P1).xreplace(sub)), mu)[0]   # pi_{-,1} = p_xx
    sub.update({mu: musol, P1t: X.Dt(v[0]), Q1t: X.Dt(q_x), mut: X.Dt(musol)})
    rs = [X.Dx(q_x) - sp.diff(B, Q1).xreplace(sub),             # pi_{+,1} = q_xx = dS/dQ1
          -p_t / 2 + euler_t(B, p, tder, sub),
          -(p_t - X.Dt(w)) / 2 - euler_t(B, q, tder, sub),
          (P1 + Q1 - al * sp.sin(w_)).xreplace(sub)]
    rs = [trunc(sp.expand(eps * r).subs(pv, 0), N) for r in rs]
    ok = report("mKdV: all promoted sewing equations of CZ (7.22) hold on shell, orders 0..N-2",
                orders_vanish(rs, 0, N - 2))
    Q = trunc((sp.cos(w) - 1) / eps, N)  # defect momentum, CZ (7.19)
    return check_density("mKdV defect momentum", X, Q, N) and ok


# ----------------------------------------------------------------- Boussinesq
def boussinesq(N=4):
    c, kap, lam = sp.Integer(1), sp.Integer(1), sp.Integer(3)   # generic nonzero constants
    X = XJets(["u", "chi"], 3 * N + 12)
    u, ch = X["u"], X["chi"]
    X.set_flow("u", ch[0])
    X.set_flow("chi", c ** 2 * (u[2] + 2 * lam * u[1] * u[2] - kap ** 2 * u[4]))
    a_ = kap / (sp.sqrt(3) * c)
    b_ = 2 * a_
    mu = 2 * lam / (3 * b_)
    s0 = 1 / eps
    Uv, Vv, U1, V1, Ut, Vt = sp.symbols("U V U1 V1 U_t V_t")
    U1t, V1t = sp.symbols("U1_t V1_t")
    tder = {Uv: Ut, Vv: Vt, U1: U1t, V1: V1t}
    wv = Uv - Vv
    sig = s0 + mu * wv
    rho = sp.expand((sig * (1 - sig ** 2 / (3 * c ** 2)) - s0 * (1 - s0 ** 2 / (3 * c ** 2))) / (2 * mu))
    ws = sp.Symbol("ws")
    tau = sp.integrate((-a_ * sig * rho / kap ** 2).subs(wv, ws), (ws, 0, wv))
    fg = -sig ** 2 / (4 * mu * c ** 2)
    Dd = (Ut * (a_ * U1 + b_ * V1 + fg) + Vt * (b_ * U1 + a_ * V1 + fg)
          + sig / 2 * (b_ * U1 ** 2 + 2 * a_ * U1 * V1 + b_ * V1 ** 2) + rho * (U1 + V1) + tau)
    uv = sp.Symbol("u_value")

    def sub_of(w):
        return {Uv: uv, Vv: uv - w, U1: u[1], V1: u[1] - X.Dx(w),
                Ut: ch[0], Vt: ch[0] - X.Dt(w), U1t: X.Dx(ch[0]), V1t: X.Dx(ch[0] - X.Dt(w))}

    # pi_{-,1} = -kappa^2 u_xx = -dD/dU1 gives the branch
    F = lambda s: [sp.expand(2 * c ** 2 * eps ** 2 * (kap ** 2 * u[2] - sp.diff(Dd, U1).xreplace(sub_of(s["w"]))))]
    w = formal_solve(F, ["w"], N, sp.Matrix([[1]]))["w"]
    sub = sub_of(w)
    vx = u[1] - X.Dx(w)
    vxx, vxxx = X.Dx(vx), X.Dx(X.Dx(vx))
    pi0 = lambda ux, uxxx: -ux - lam * ux ** 2 + kap ** 2 * uxxx
    rs = [-kap ** 2 * vxx - sp.diff(Dd, V1).xreplace(sub),             # pi_{+,1} = dD/dV1
          pi0(u[1], u[3]) + euler_t(Dd, Uv, tder, sub),                 # pi_{-,0} = -dD/du
          pi0(vx, vxxx) - euler_t(Dd, Vv, tder, sub)]                   # pi_{+,0} = dD/dv
    rs = [trunc(sp.expand(eps ** 2 * r).subs(uv, 0), N + 1) for r in rs]
    ok = report("Boussinesq: all promoted sewing equations of CZ (3.43) hold on shell, orders 0..N",
                orders_vanish(rs, 0, N))
    return check_density("Boussinesq mass defect charge v - u", X, -w, N) and ok


# ------------------------------------------------------------ Tzitzeica, Type II
def tzitzeica(N=5):
    """Type-II defect of CZ 0908.3126, eq. (3.7); transparent limit sigma = 1/epsilon -> infinity."""
    X = XJets(["u", "chi"], 2 * N + 10)
    u, ch = X["u"], X["chi"]
    X.set_flow("u", ch[0])
    X.set_flow("chi", u[2] - 2 * sp.exp(2 * u[0]) + 2 * sp.exp(-u[0]))
    P, Qv, L = sp.symbols("P Q Lam")
    sig = 1 / eps
    f = (sp.exp(2 * P - 2 * L) + sp.exp(-P + L) * (sp.exp(Qv) + sp.exp(-Qv))) / sig
    g = sig / 2 * (8 * sp.exp(-L) + sp.exp(2 * L) * (sp.exp(Qv) + sp.exp(-Qv)) ** 2)
    Dd = f + g
    D_u = (sp.diff(Dd, P) + sp.diff(Dd, Qv)) / 2      # u = P + Q, v = P - Q
    D_v = (sp.diff(Dd, P) - sp.diff(Dd, Qv)) / 2
    D_l = sp.diff(Dd, L)

    def at(expr, q, lam):
        return expr.subs({P: u[0] - q, Qv: q, L: lam})

    def F(s):
        q, lam = s["q"], s["lam"]
        v_t = ch[0] - 2 * X.Dt(q)
        # CZ (2.2)-(2.4): u_x = v_t - 2 lam_t - D_u ;  (u - v)_t = D_lambda / 2
        return [sp.expand(eps * (u[1] - v_t + 2 * X.Dt(lam) + at(D_u, q, lam))),
                sp.expand(eps * (2 * X.Dt(q) - at(D_l, q, lam) / 2))]

    sol = formal_solve(F, ["q", "lam"], N, sp.Matrix([[2, 0], [0, -6]]))
    q, lam = sol["q"], sol["lam"]
    v_x = u[1] - 2 * X.Dx(q)
    resid = trunc(eps * (v_x - (ch[0] - 2 * X.Dt(lam) + at(D_v, q, lam))), N)  # CZ (2.3)
    ok = report("Tzitzeica Type II: right sewing equation holds on shell, orders 0..N",
                orders_vanish([resid], 0, N))
    Q = trunc(at(Dd, q, lam) - (3 * eps + 6 / eps), N)   # defect energy, vacuum-normalised
    return check_density("Tzitzeica Type-II E_d", X, Q, N) and ok


if __name__ == "__main__":
    which = sys.argv[1:] or ["sg", "nls", "kdv", "mkdv", "bsq", "tz"]
    fns = {"sg": sine_gordon, "nls": nls, "kdv": kdv, "mkdv": mkdv, "bsq": boussinesq,
           "tz": tzitzeica}
    results = [fns[k]() for k in which]
    sys.exit(0 if all(results) else 1)
