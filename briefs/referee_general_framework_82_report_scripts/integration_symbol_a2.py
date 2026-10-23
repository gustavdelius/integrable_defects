"""Item 6 of briefs/referee_general_framework_82_report.md: the generating symbol of the
a_2^(1) Toda family (8.5), where U'''(0) != 0.

Plane waves, written from paper.md (Sections 7-8) with SymPy only: the linearised left
sewing equation is solved exactly in epsilon for a plane wave of arbitrary complex
polarization; the x-average of the quadratic part of E_d = eps U(w) + ghat(q)/eps gives a
2x2 Hermitian symbol K(k; eps).  The jet-space cross-check is integration_symbol_jets.py.

Coordinates: orthonormal basis of the sum-zero plane of R^3; roots e_i - e_{i+1}.
"""

import sympy as sp

ok_all = True


def report(label, ok):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def dot(a, b):
    return (a.T * b)[0]


B = sp.Matrix([[1 / sp.sqrt(2), 1 / sp.sqrt(6)], [-1 / sp.sqrt(2), 1 / sp.sqrt(6)], [0, -2 / sp.sqrt(6)]])
e3 = sp.eye(3)
roots = [B.T * (e3[:, i] - e3[:, (i + 1) % 3]) for i in range(3)]
P3 = sp.zeros(3)
for i in range(3):
    P3[(i + 1) % 3, i] = 1
Pr = sp.simplify(B.T * P3 * B)
D = sp.simplify(2 * (sp.eye(2) - Pr).inv())
E = sp.simplify(sp.eye(2) - D)
M = sp.simplify(sum((al * al.T for al in roots), sp.zeros(2)))
beta = [sp.simplify(D.T * al) for al in roots]
assert M == 3 * sp.eye(2)
nu = sp.simplify(E[1, 0])          # E = nu * [[0, -1], [1, 0]]
assert sp.simplify(E - nu * sp.Matrix([[0, -1], [1, 0]])) == sp.zeros(2)
print("INFO: E =", E.tolist(), " nu =", nu)

eps, k = sp.symbols("epsilon k", positive=True)
om = sp.sqrt(k ** 2 + 3)
ell = om + k
I = sp.I

# polarization vectors: E z_s = i e_s z_s
zs = {}
for s in (1, -1):
    z = sp.Matrix([1, -s * I]) / sp.sqrt(2)
    lamv = sp.simplify((E * z)[0] / z[0])
    assert sp.simplify(E * z - lamv * z) == sp.zeros(2, 1)
    zs[s] = (z, sp.simplify(lamv / I))
print("INFO: polarizations e_s =", {s: zs[s][1] for s in zs})

# ------------------------------------------------------------------ (a) plane waves
# u = phi = A e^{i(kx - wt)} + cc, q = Qv e^{...} + cc; psi = u - 2q; w = u - D q.
# left sewing: u_x = E u_t + D psi_t - B_phi, B_phi = (D f' + g')/2, f' = eps M w, g' = 4 q/eps
A = sp.Matrix(sp.symbols("A1 A2"))
Qv = sp.Matrix(sp.symbols("Qv1 Qv2"))
dx, dt = I * k, -I * om
W = A - D * Qv
Psi = A - 2 * Qv
lhs = dx * A - (E * dt * A + D * dt * Psi - (D * eps * M * W + 4 * Qv / eps) / 2)
sol = sp.solve(list(lhs), list(Qv), dict=True)[0]
RQ = sp.Matrix(2, 2, lambda i, j: sp.diff(Qv[i].subs(sol), A[j]))
RW = sp.simplify(sp.eye(2) - D * RQ)
RQ = sp.simplify(RQ)
# x-average of eps (3/2)|w|^2 + (2/eps)|q|^2 on a real plane wave = a^dagger K a
K = sp.simplify(3 * eps * RW.H * RW + 4 / eps * RQ.H * RQ)
Kc = sp.simplify(K.subs(k, sp.Symbol("kk", real=True)).subs(sp.Symbol("kk", real=True), k))
cross = sp.simplify((zs[1][0].H * K * zs[-1][0])[0])
report("(a) the Hermitian symbol K(k; eps) has no cross term between the two polarizations", cross == 0)
m_closed = {s: 4 * eps * (3 + ell ** 2) / (4 - 4 * zs[s][1] * eps * ell + sp.Rational(4, 3) * eps ** 2 * ell ** 2)
            for s in (1, -1)}
for s in (1, -1):
    ms = sp.simplify((zs[s][0].H * K * zs[s][0])[0])
    report(f"(a) polarization e_s = {zs[s][1]}: m_s = 4 eps (3 + l^2)/(4 - 4 e_s eps l + 4 eps^2 l^2/3), l = omega + k",
           sp.simplify(ms - m_closed[s]) == 0)

# coefficients: m_{n,s} = (3 + l^2) l^(n-1) 3^{-(n-1)/2} (sign s)^(n-1) sin(n pi/3)/sin(pi/3)
L = sp.Symbol("L", positive=True)
NMAX = 12
okc = True
for s in (1, -1):
    mL = m_closed[s].subs(ell, L)
    ser = sp.series(mL, eps, 0, NMAX + 1).removeO()
    for n in range(1, NMAX + 1):
        c = sp.simplify(ser.coeff(eps, n))
        pred = (3 + L ** 2) * L ** (n - 1) * sp.sqrt(3) ** (-(n - 1)) * (s * sp.sign(zs[s][1])) ** 0 \
            * (sp.sign(zs[s][1])) ** (n - 1) * sp.sin(n * sp.pi / 3) / sp.sin(sp.pi / 3)
        okc &= sp.simplify(c - pred) == 0
        okc &= (c == 0) == (n % 3 == 0)
report(f"(a) m_(n,s) = (3+l^2) l^(n-1) 3^(-(n-1)/2) (sgn e_s)^(n-1) sin(n pi/3)/sin(pi/3), n <= {NMAX}; "
       "zero exactly when 3 | n", okc)

print("All symbol checks passed." if ok_all else "SOME CHECKS FAILED")
raise SystemExit(0 if ok_all else 1)
