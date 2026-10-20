"""Direct check of Theorem 3.3(a) on Type-II and Type-I examples.

For a defect Lagrangian L_d(Y), Y = (u, v, lambda) with K = 1 relativistic
bulks, this script
  * writes H_- - H_+ - D_t P = rho * C with C = delta S_d / delta lambda
    (polynomial division in the jet variable eliminated by C),
  * forms the spatial Hamiltonian vector fields a = dH/dpi, b = E_Phi(H) at
    pi = Pi^{-+}(Y),
  * applies the Fréchet derivatives S_AB of the defect Euler–Lagrange
    expression E_Y(L_d), and
  * checks the three identities (3.5) modulo the constraint, i.e. that
    (X_-, X_+) is the image of (a_-, a_+, rho) under the linearised sewing map.
It also checks the Type-I case (sine-Gordon), where rho = 0.
One PASS or FAIL line per check.
"""

import sys
import sympy as sp
from jets import TJets, report

N = 6


def frechet(J, expr, direction):
    """D_expr[direction]; direction maps field names to jet expressions."""
    out = 0
    for name, d in direction.items():
        js = J[name]
        coeffs = [sp.diff(expr, js[k]) for k in range(J.order + 1)]
        top = max([k for k, c in enumerate(coeffs) if c != 0], default=-1)
        dk = d
        for k in range(top + 1):
            if coeffs[k] != 0:
                out += coeffs[k] * dk
            if k < top:
                dk = J.Dt(dk)
    return out


def check(label, J, U, V, Ld, P, lam=None, elim=None):
    u, v = J["u"], J["v"]
    Pi_m = -J.var(Ld, "u")
    Pi_p = J.var(Ld, "v")
    # relativistic spatial Hamiltonian H = -pi^2/2 - phi_t^2/2 + U(phi)
    Hm = -Pi_m ** 2 / 2 - u[1] ** 2 / 2 + U(u[0])
    Hp = -Pi_p ** 2 / 2 - v[1] ** 2 / 2 + V(v[0])
    a_m, a_p = -Pi_m, -Pi_p                                  # dH/dpi
    b_m = sp.diff(U(u[0]), u[0]) + u[2]                      # E_Phi(H) = U' + phi_tt
    b_p = sp.diff(V(v[0]), v[0]) + v[2]
    R = sp.expand(Hm - Hp - J.Dt(P))
    names = ["u", "v"] + (["lam"] if lam else [])
    E = {n: J.var(Ld, n) for n in names}
    if lam:
        C = E["lam"]
        sym, sol = elim
        # R vanishes at sym = sol; divide by C, which is linear in sym
        coef = sp.diff(C, sym)
        assert sp.simplify(sp.diff(C, sym, 2)) == 0
        rho = sp.simplify(sp.cancel((R - R.subs(sym, sol)) / (sym - sol)) / coef)
        assert sp.simplify(R.subs(sym, sol)) == 0
    else:
        rho = 0
    direction = {"u": a_m, "v": a_p}
    if lam:
        direction["lam"] = rho
    S = {n: frechet(J, E[n], direction) for n in names}
    # (3.2): delta pi_- = -S_Phi[dY], delta pi_+ = S_Psi[dY], 0 = S_lambda[dY]
    eqs = [(-S["u"]) - (-b_m), S["v"] - (-b_p)]
    if lam:
        eqs.append(S["lam"])
    ok = True
    for e in eqs:
        e = J.reduce(sp.expand(e)) if lam else sp.expand(e)
        ok &= sp.simplify(e) == 0
    return report(label, ok)


def tzitzeica():
    J = TJets(["u", "v", "lam"], N)
    sig = sp.Symbol("sigma", positive=True)
    u, v, la = J["u"], J["v"], J["lam"]
    U = lambda f: sp.exp(2 * f) + 2 * sp.exp(-f) - 3
    p, q = (u[0] + v[0]) / 2, (u[0] - v[0]) / 2
    f = (sp.exp(2 * p - 2 * la[0]) + sp.exp(-p + la[0]) * (sp.exp(q) + sp.exp(-q))) / sig
    g = sig / 2 * (8 * sp.exp(-la[0]) + sp.exp(2 * la[0]) * (sp.exp(q) + sp.exp(-q)) ** 2)
    Ld = (u[0] * v[1] - v[0] * u[1]) / 2 + la[0] * (u[1] - v[1]) - la[1] * (u[0] - v[0]) - (f + g)
    C = J.var(Ld, "lam")
    v1 = sp.solve(sp.Eq(C, 0), v[1])[0]
    J.eliminate("v", 1, v1, N - 1)
    return check("Theorem 3.3(a) on the Tzitzeica Type-II defect: (X_-, X_+) = image of (a_-, a_+, rho)",
                 J, U, U, Ld, f - g, lam=True, elim=(v[1], v1))


def sine_gordon():
    J = TJets(["u", "v"], N)
    eps = sp.Symbol("epsilon", positive=True)
    u, v = J["u"], J["v"]
    U = lambda f: 1 - sp.cos(f)
    q, w = (u[0] - v[0]) / 2, (u[0] + v[0]) / 2
    B = 2 * (1 - sp.cos(q)) / eps + 2 * eps * (1 - sp.cos(w))
    Ld = (u[0] * v[1] - v[0] * u[1]) / 2 - B
    P = -2 * (1 - sp.cos(q)) / eps + 2 * eps * (1 - sp.cos(w))   # defect momentum -F + G
    Pm = [P, -P]
    # find the sign of P for which the balance holds, then check tangency
    Pi_m = -J.var(Ld, "u")
    Pi_p = J.var(Ld, "v")
    R = lambda PP: sp.simplify(sp.expand(-Pi_m ** 2 / 2 - u[1] ** 2 / 2 + U(u[0])
                                         + Pi_p ** 2 / 2 + v[1] ** 2 / 2 - U(v[0]) - J.Dt(PP)))
    PP = next(PP for PP in Pm if R(PP) == 0)
    return check("Theorem 3.3(a) on the sine-Gordon Type-I defect (rho = 0)", J, U, U, Ld, PP)


def kdv():
    """Spatial order 2 with a Lagrange multiplier mu (CZ nlin/0512038, eq. 9.16)."""
    J = TJets(["p", "P1", "q", "Q1", "mu"], N)
    al = sp.Symbol("alpha")
    p, P1, q, Q1, mu = J["p"], J["P1"], J["q"], J["Q1"], J["mu"]
    w = p[0] - q[0]
    Ld = ((q[0] * p[1] - p[0] * q[1]) / 4 + (P1[0] ** 2 + P1[0] * Q1[0] + Q1[0] ** 2) * w
          + mu[0] * (P1[0] + Q1[0] - 2 * al - w ** 2 / 2) - 3 * (P1[0] + Q1[0]) * w * (al + w ** 2 / 4)
          + 6 * al ** 2 * w + 2 * al * w ** 3 + sp.Rational(9, 40) * w ** 5)
    E = {n: J.var(Ld, n) for n in ["p", "P1", "q", "Q1", "mu"]}
    Pm = [-E["p"], -E["P1"]]          # Pi^-_0, Pi^-_1
    Pp = [E["q"], E["Q1"]]            # Pi^+_0, Pi^+_1
    # L = p_x p_t/2 - p_x^3 - p_xx^2/2:  pi_1 = -p_xx, so Z = -pi_1 and
    # H(Phi0, Phi1; pi0, pi1) = pi0 Phi1 - pi1^2/2 - Phi1 Phi0_t/2 + Phi1^3
    def H(Ph0, Ph1, pi0, pi1):
        return pi0 * Ph1[0] - pi1 ** 2 / 2 - Ph1[0] * Ph0[1] / 2 + Ph1[0] ** 3
    # a_m = dH/dpi_m, b_m = E_{Phi_m}(H) (t-Euler derivative)
    def ab(Ph0n, Ph1n, pi0, pi1):
        a0 = J[Ph1n][0]
        a1 = -pi1
        b0 = J.Dt(J[Ph1n][0]) / 2                      # E_{Phi0}(-Phi1 Phi0_t/2)
        b1 = pi0 - J[Ph0n][1] / 2 + 3 * J[Ph1n][0] ** 2
        return a0, a1, b0, b1
    am0, am1, bm0, bm1 = ab("p", "P1", *Pm)
    ap0, ap1, bp0, bp1 = ab("q", "Q1", *Pp)
    R = sp.expand(H(p, P1, *Pm) - H(q, Q1, *Pp))
    C = E["mu"]
    sol = sp.solve(sp.Eq(C, 0), Q1[0])[0]
    ok_any = False
    for sgn in (1, -1):
        Pt = sgn * (al * w + w ** 3 / 12)              # CZ (9.21), sign to be found
        RR = sp.expand(R - J.Dt(Pt))
        if sp.simplify(RR.subs(Q1[0], sol)) != 0:
            continue
        coef = sp.diff(C, Q1[0])
        rho = sp.simplify(sp.cancel((RR - RR.subs(Q1[0], sol)) / (Q1[0] - sol)) / coef)
        direction = {"p": am0, "P1": am1, "q": ap0, "Q1": ap1, "mu": rho}
        S = {n: frechet(J, E[n], direction) for n in E}
        J.eliminate("Q1", 0, sol, N - 1)
        eqs = [-S["p"] + bm0, -S["P1"] + bm1, S["q"] + bp0, S["Q1"] + bp1, S["mu"]]
        ok_any = all(sp.simplify(J.reduce(sp.expand(e))) == 0 for e in eqs)
        break
    return report("Theorem 3.3(a) on the KdV constrained defect (K = 2, multiplier mu)", ok_any)


if __name__ == "__main__":
    ok = sine_gordon() & tzitzeica() & kdv()
    sys.exit(0 if ok else 1)
