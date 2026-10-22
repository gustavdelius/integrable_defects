"""The examples of guide.md: the classical-mechanics toy of Part 3, and the
sine-Gordon example, checked from the definitions of paper.md.

Toy: a jump with action S(q, Q, lam) has jump rule p = -S_q, P = S_Q, 0 = S_lam,
the finite-dimensional form of the sewing equations (3.1).

Bulk: L = (phi_t^2 - phi_x^2)/2 - U(phi), U = 1 - cos(phi), so pi = -phi_x and
H = -pi^2/2 - phi_t^2/2 + U.  Defect of [1]: L_d = (phi psi_t - psi phi_t)/2 - B,
B = f + g, f = 2 sigma (1 - cos((phi+psi)/2)), g = (2/sigma)(1 - cos((phi-psi)/2)).
Self-contained: imports only SymPy.  One PASS or FAIL line per check.
"""

import sympy as sp

ok = True


def report(name, cond):
    global ok
    ok = ok and bool(cond)
    print(("PASS " if cond else "FAIL ") + name)


s = sp.symbols("sigma", positive=True)
P, Ps, Pt, Pst = sp.symbols("phi psi phi_t psi_t")
U = lambda u: 1 - sp.cos(u)
f = 2 * s * (1 - sp.cos((P + Ps) / 2))
g = 2 / s * (1 - sp.cos((P - Ps) / 2))
B = f + g

# Sewing equations (3.1): pi_- = -E_Phi L_d, pi_+ = E_Psi L_d.
phix = Pst - sp.diff(B, P)
psix = Pt + sp.diff(B, Ps)
H = lambda wx, wt, w: -wx ** 2 / 2 - wt ** 2 / 2 + U(w)
bal = H(phix, Pt, P) - H(psix, Pst, Ps)
Ptil = g - f
DtPtil = sp.diff(Ptil, P) * Pt + sp.diff(Ptil, Ps) * Pst
report("momentum balance (3.3) with P~ = g - f", sp.simplify(sp.expand_trig(bal + DtPtil)) == 0)

# Defect energy T^00_d = Xi_d(D_t Y) - L_d equals B.
Ld = (P * Pst - Ps * Pt) / 2 - B
Ed = sp.diff(Ld, Pt) * Pt + sp.diff(Ld, Pst) * Pst - Ld
report("defect energy equals B", sp.simplify(Ed - B) == 0)

# First order of the formal branch, epsilon = sigma.
x, t, e = sp.symbols("x t epsilon")
ph = sp.Function("phi")(x, t)
D1 = sp.Function("D1")(x, t)
psi = ph + e * D1
eq = sp.diff(ph, x) - (sp.diff(psi, t) - sp.diff(B, P).subs({P: ph, Ps: psi, s: e}))
D1sol = sp.solve(sp.series(eq, e, 0, 1).removeO(), D1)[0]
report("Delta_1 = 2(phi_x - phi_t)", sp.simplify(D1sol - 2 * (sp.diff(ph, x) - sp.diff(ph, t))) == 0)

G = B.subs({P: ph, Ps: ph + e * D1sol, s: e})
Q1 = sp.series(G, e, 0, 2).removeO().coeff(e, 1)
T00 = (sp.diff(ph, t) ** 2 + sp.diff(ph, x) ** 2) / 2 + U(ph)
T01 = -sp.diff(ph, t) * sp.diff(ph, x)
report("Q_1 = 2(T^00 + T^01)", sp.simplify(Q1 - 2 * (T00 + T01)) == 0)

# Generating symbol (Proposition 7.5): phi = aE, Delta = dE, E = exp(i(kx - wt)).
th = sp.symbols("theta", real=True)
a, d = sp.symbols("a d")
k, w = sp.sinh(th), sp.cosh(th)
lin = sp.I * k * a - (-sp.I * w * (a + d) - (-d / (2 * s) + s * (2 * a + d) / 2))
r = sp.simplify(sp.solve(lin, d)[0] / a)
report("Delta/phi = 2 i sigma e^theta / (1 - i sigma e^theta)",
       sp.simplify((r - 2 * sp.I * s * sp.exp(th) / (1 - sp.I * s * sp.exp(th))).rewrite(sp.exp)) == 0)
# B = sigma^{-1} Delta^2/4 + sigma (2 phi + Delta)^2/4 + O(3); x-average of a real
# plane wave squared is 2|amplitude|^2.
avg = (sp.Abs(r) ** 2 / s + s * sp.Abs(2 + r) ** 2) / 2
target = 4 * s * w * sp.exp(th) / (1 + s ** 2 * sp.exp(2 * th))
vals = [(avg - target).subs({th: v1, s: v2}).evalf(30) for v1, v2 in [(sp.Rational(37, 100), sp.Rational(21, 100)),
                                                                      (sp.Rational(-13, 10), sp.Rational(17, 10)),
                                                                      (sp.Rational(21, 10), sp.Rational(1, 20))]]
report("m(k; sigma) = 4 sigma w e^theta / (1 + sigma^2 e^{2 theta})", all(abs(z) < 1e-25 for z in vals))

ser = sp.series(target, s, 0, 6).removeO()
report("m_1 = 4 w e^theta, m_3 = -4 w e^{3 theta}, m_5 = 4 w e^{5 theta}, even orders 0",
       all(sp.simplify(ser.coeff(s, n) - c) == 0 for n, c in
           [(1, 4 * w * sp.exp(th)), (2, 0), (3, -4 * w * sp.exp(3 * th)), (4, 0), (5, 4 * w * sp.exp(5 * th))]))

# ------------------------------------------------- Part 3: the mechanics toy
q, Q, lam, al, sv = sp.symbols("q Q lambda alpha s")
V = sp.Function("V")
# derivatives of h = H_-(q, -S_q) - H_+(Q, S_Q) for generic H_-, H_+, S: the left sides of (3.5)
Sg = sp.Function("S")(q, Q, lam)
pq, pp = sp.symbols("pq pp")
Hm, Hp = sp.Function("Hm"), sp.Function("Hp")
zm, zp = (q, -sp.diff(Sg, q)), (Q, sp.diff(Sg, Q))
h = Hm(*zm) - Hp(*zp)
am = sp.diff(Hm(pq, pp), pp).subs({pq: zm[0], pp: zm[1]}); bm = sp.diff(Hm(pq, pp), pq).subs({pq: zm[0], pp: zm[1]})
ap = sp.diff(Hp(pq, pp), pp).subs({pq: zp[0], pp: zp[1]}); bp = sp.diff(Hp(pq, pp), pq).subs({pq: zp[0], pp: zp[1]})
d = lambda a, b: sp.diff(Sg, a, b)
eqs = [sp.diff(h, q) - (bm - d(q, q) * am - d(q, Q) * ap),
       sp.diff(h, Q) - (-d(Q, q) * am - bp - d(Q, Q) * ap),
       sp.diff(h, lam) - (-d(lam, q) * am - d(lam, Q) * ap)]
report("toy: dh/dq, dh/dQ, dh/dlam have the form of the left sides of (3.5)", all(sp.simplify(e) == 0 for e in eqs))

S1 = -(q - Q) ** 2 / (2 * e)
p1, P1 = -sp.diff(S1, q), sp.diff(S1, Q)
report("toy: the spring S = -(q-Q)^2/(2 eps) gives P = p, Q = q - eps p",
       sp.simplify(p1 - P1) == 0 and sp.simplify(Q - (q - e * p1)) == 0)
report("toy: the spring preserves p^2/2 but not p^2/2 + V(q)",
       sp.simplify(p1 ** 2 / 2 - P1 ** 2 / 2) == 0 and sp.simplify(V(q) - V(Q)) != 0)
S2 = ((q ** 2 + Q ** 2) * sp.cos(al) - 2 * q * Q) / (2 * sp.sin(al))
p2, P2 = -sp.diff(S2, q), sp.diff(S2, Q)
report("toy: S = ((q^2+Q^2) cos a - 2qQ)/(2 sin a) is the oscillator flow for time a and preserves H",
       sp.simplify(Q - (q * sp.cos(al) + p2 * sp.sin(al))) == 0
       and sp.simplify(P2 - (-q * sp.sin(al) + p2 * sp.cos(al))) == 0
       and sp.simplify(p2 ** 2 + q ** 2 - P2 ** 2 - Q ** 2) == 0)
S3 = lam * (q + Q)
p3, P3, C3 = -sp.diff(S3, q), sp.diff(S3, Q), sp.diff(S3, lam)
report("toy: S = lam (q+Q), H = (p^2+q^2)/2: h = rho C with rho = (q-Q)/2",
       sp.simplify(p3 ** 2 / 2 + q ** 2 / 2 - P3 ** 2 / 2 - Q ** 2 / 2 - (q - Q) / 2 * C3) == 0)
qs, Qs, ls = sv ** 2, -sv ** 2, -2 * sv
report("toy: (q, Q, lam) = (s^2, -s^2, -2s) obeys the jump rule and both velocity equations, "
       "but qdot-dot + q = s^2 + 2 != 0",
       sp.diff(qs, sv) == -ls and sp.diff(Qs, sv) == ls and qs + Qs == 0
       and sp.simplify(sp.diff(qs, sv, 2) + qs - (sv ** 2 + 2)) == 0)

raise SystemExit(0 if ok else 1)
