"""Item 6 of briefs/referee_general_framework_82_report.md, second route: the quadratic
parts of the actual charges Q_n of the a_2^(1) Toda family (8.5), computed in jet space.

When the generating density E_d = eps U(w) + ghat(q)/eps has zero first variation at the
vacuum, the quadratic part of each Q_n is E_d's quadratic part evaluated on the LINEAR
part of the branch (composition of power series).  Terms of degree >= 2 in the branch and
in the flow (U'''(0) != 0) can only reach degree >= 3 of Q_n, so only the linear branch is
computed here, by the formal implicit-function iteration of Lemma 6.2 on jets, with
t-derivatives reduced by the linearised flow u_t = p, p_t = u_xx - M u.

The coupling of a_2^(1) is E = nu J with J the rotation generator, M = 3I and
ghat''(0) = 4I (nu^2 = 1/3 for Toda).  nu is kept symbolic: the closed form
m_s = 4 eps (3 + l^2) / (4 - 4 e_s eps l + eps^2 l^2 (1 + e_s^2)), e_s = s nu, l = omega + k,
should hold for every nu.  The Hermitian symbol of a quadratic jet polynomial is read off
on u = a e^{ikx} + cc, p = -i omega a e^{ikx} + cc.  SymPy only.
"""

import sympy as sp

ok_all = True


def report(label, ok):
    global ok_all
    ok_all &= bool(ok)
    print(("PASS " if ok else "FAIL ") + label, flush=True)


def dot(a, b):
    return (a.T * b)[0]


nu, eps, k = sp.symbols("nu epsilon k", positive=True)
I = sp.I
J = sp.Matrix([[0, -1], [1, 0]])
E = nu * J
D = sp.eye(2) - E
mu = 3                                     # M = mu I
N = 6                                      # orders in epsilon
NJ = 2 * N + 4

u = [[sp.Symbol(f"u{i}_{j}") for j in range(NJ)] for i in range(2)]
p = [[sp.Symbol(f"p{i}_{j}") for j in range(NJ)] for i in range(2)]


def Dt(expr):
    out = 0
    for i in range(2):
        for j in range(NJ - 2):
            out += sp.diff(expr, u[i][j]) * p[i][j] + sp.diff(expr, p[i][j]) * (u[i][j + 2] - mu * u[i][j])
    return sp.expand(out)


def Dx(expr):
    out = 0
    for i in range(2):
        for j in range(NJ - 1):
            out += sp.diff(expr, u[i][j]) * u[i][j + 1] + sp.diff(expr, p[i][j]) * p[i][j + 1]
    return sp.expand(out)


def trunc(expr, n):
    e = sp.expand(expr)
    return sp.expand(sum(e.coeff(eps, m) * eps ** m for m in range(0, n + 1)))


uv = sp.Matrix([u[0][0], u[1][0]])
pv = sp.Matrix([p[0][0], p[1][0]])
ux = sp.Matrix([u[0][1], u[1][1]])
# left sewing equation (8.2) with B = eps U(w) + ghat(q)/eps, w = u - D q, psi = u - 2q, multiplied by eps
# and linearised:  4 q = 2 eps (p - u_x) - 4 eps D D_t q - eps^2 mu D (u - D q)
q = sp.zeros(2, 1)
for it in range(N + 1):
    rhs = 2 * eps * (pv - ux) - 4 * eps * D * q.applyfunc(Dt) - eps ** 2 * mu * D * (uv - D * q)
    q = (rhs / 4).applyfunc(lambda x: trunc(x, N))
res = 4 * q - 2 * eps * (pv - ux) + 4 * eps * D * q.applyfunc(Dt) + eps ** 2 * mu * D * (uv - D * q)
report(f"jets: the linearised left sewing equation is solved through eps^{N}",
       all(trunc(x, N) == 0 for x in res))
report("jets: q_1 = (p - u_x)/2", sp.expand(q.applyfunc(lambda x: x.coeff(eps, 1)) - (pv - ux) / 2) == sp.zeros(2, 1))
wv = uv - D * q
Ed = sp.expand(eps * mu * dot(wv, wv) / 2 + 2 * dot(q, q) / eps)

om = sp.sqrt(k ** 2 + mu)
ell = om + k
av = sp.Matrix(sp.symbols("a1 a2"))
ab = sp.Matrix(sp.symbols("b1 b2"))       # stands for conj(a)
hat, hatc = {}, {}
for i in range(2):
    for j in range(NJ):
        hat[u[i][j]] = (I * k) ** j * av[i]
        hatc[u[i][j]] = (-I * k) ** j * ab[i]
        hat[p[i][j]] = (I * k) ** j * (-I * om) * av[i]
        hatc[p[i][j]] = (-I * k) ** j * (I * om) * ab[i]


def herm(Q2):
    """x-average of a quadratic jet polynomial on u = a E + cc, as a Hermitian matrix in a."""
    out = 0
    for term in sp.Add.make_args(sp.expand(Q2)):
        c, facs = term.as_coeff_mul()
        js = []
        for f in facs:
            if f.is_Pow and f.base in hat:
                js += [f.base] * int(f.exp)
            elif f in hat:
                js.append(f)
            else:
                c *= f
        assert len(js) == 2, term
        x, y = js
        out += c * (hat[x] * hatc[y] + hatc[x] * hat[y])
    out = sp.expand(out)
    return sp.Matrix(2, 2, lambda i, j: out.coeff(ab[i]).coeff(av[j]))


# polarizations: J z = i z for z = (1, -i)/sqrt2, so E z_s = i (s nu) z_s
zs = {1: sp.Matrix([1, -I]) / sp.sqrt(2), -1: sp.Matrix([1, I]) / sp.sqrt(2)}
m_closed = {s: 4 * eps * (mu + ell ** 2) / (4 - 4 * s * nu * eps * ell + eps ** 2 * ell ** 2 * (1 + nu ** 2))
            for s in (1, -1)}
okq = True
for n in range(1, N + 1):
    Qn = sp.expand(Ed.coeff(eps, n))
    Kn = herm(Qn)
    okq &= sp.simplify((zs[1].H * Kn * zs[-1])[0]) == 0
    for s in (1, -1):
        mjet = sp.simplify((zs[s].H * Kn * zs[s])[0])
        mpw = sp.series(m_closed[s], eps, 0, n + 1).removeO().coeff(eps, n)
        okq &= sp.simplify(mjet - mpw) == 0
    print(f"INFO: n = {n}: m_(n,+) at nu^2 = 1/3:",
          sp.factor(sp.simplify((zs[1].H * Kn * zs[1])[0]).subs(nu, 1 / sp.sqrt(3))), flush=True)
report(f"jets: for every nu, the Hermitian symbols of Q_1..Q_{N} have no cross term between the "
       "polarizations and equal the eps^n coefficients of the plane-wave m_s", okq)
# Toda value nu = 1/sqrt(3): m_(3,s) = 0 = m_(6,s)
Q3 = herm(sp.expand(Ed.coeff(eps, 3))).subs(nu, 1 / sp.sqrt(3))
Q6 = herm(sp.expand(Ed.coeff(eps, 6))).subs(nu, 1 / sp.sqrt(3))
report("jets: at nu^2 = 1/3 the quadratic parts of Q_3 and Q_6 vanish (Q_3, Q_6 have no quadratic part)",
       sp.simplify(Q3) == sp.zeros(2) and sp.simplify(Q6) == sp.zeros(2))

print("All jet checks passed." if ok_all else "SOME CHECKS FAILED")
raise SystemExit(0 if ok_all else 1)
