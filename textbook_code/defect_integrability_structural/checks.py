#!/usr/bin/env python3
"""Exact finite checks for the structural Type-I proof; not an all-orders proof.

Run from any directory with Python 3 and SymPy. No numerical tolerances are used.
"""

from functools import cache
import sympy as s


def zero(value):
    if isinstance(value, s.MatrixBase):
        return all(s.expand(x) == 0 for x in value)
    return s.expand(value) == 0


def check(name, condition):
    if not condition:
        print(f"FAIL {name}", flush=True)
        raise AssertionError(name)
    print(f"PASS {name}", flush=True)


def matrix_checks():
    e, mu, z, eps = s.symbols("e mu z eps", real=True)
    E = s.Matrix([[0, e], [-e, 0]])
    D = s.eye(2) - E
    lift = lambda A: s.diag(A, A)
    L = s.BlockMatrix([
        [-z * s.eye(2), s.eye(2)],
        [(z**2 - mu) * s.eye(2), -z * s.eye(2)],
    ]).as_explicit()
    P = s.eye(4) + eps * lift(D) * L / 2
    Q = s.eye(4) - eps * lift(D.T) * L / 2
    # Independent check: insert u=P w and v=Q w into the original sewing,
    # using the top/bottom blocks for fields/time derivatives.
    u, p = P[:2, :], P[2:, :]
    v, vp = Q[:2, :], Q[2:, :]
    w = (D.T * u + D * v) / 2
    q = (u - v) / 2
    Bu = eps * D * mu * w / 2 + 2 * q / eps
    Bv = eps * D.T * mu * w / 2 - 2 * q / eps
    check("linear map satisfies both original sewing equations",
          zero(z*u - E*p - D*vp + Bu) and
          zero(z*v - D.T*p + E*vp - Bv))
    J = s.BlockMatrix([[s.zeros(2), s.eye(2)],
                       [-s.eye(2), s.zeros(2)]]).as_explicit()
    adjoint = lambda A: A.subs(z, -z).T
    check("linear canonical identity, with spatial adjoints",
          zero(adjoint(Q)*J*Q - adjoint(P)*J*P))
    check("commuting factors in the linear fractional map", zero(P*Q-Q*P))
    generators = []
    for n in range(1, 8):
        C = ((s.eye(2)+E)**n - (-1)**n*(s.eye(2)-E)**n) / 2**n
        R = lift(C) * L**n
        generators.append(R)
        check(f"quadratic generator n={n} is Hamiltonian",
              zero(adjoint(R)*J + J*R))
    check("quadratic generators n=1..7 commute",
          all(zero(A*B-B*A) for i, A in enumerate(generators)
              for B in generators[i+1:]))
    # Compare the coefficients against the logarithmic derivative directly.
    A, B = lift(D)*L/2, lift(D.T)*L/2
    check("parameter generator coefficients through order six",
          all(zero(generators[n-1] - (B**n - (-A)**n))
              for n in range(1, 8)))
    # A_2 has e^2=1/3. Odd spins 3,9,... disappear; choose 1,5,7.
    degrees = [0, 2, 3]
    polys = []
    scalarL = s.Matrix([[-z, 1], [z*z-3, -z]])
    for j in degrees:
        c = s.expand((1+s.I/s.sqrt(3))**(2*j+1)).as_real_imag()[0]
        poly = s.expand(c * (scalarL**(2*j+1))[0, 1] / 2**(2*j))
        check(f"actual charge principal coefficient j={j}",
              s.expand(poly).coeff(z, 2*j) == c and c != 0)
        polys.append(poly)
    values = s.Matrix([[p.subs(z, s.I*k) for k in [1, 2, 3]] for p in polys])
    check("three actual quadratic charges have independent Fourier Jacobian",
          s.simplify(values.det()) != 0)


def obstruction_check():
    E = s.Matrix([[0, 1], [-1, 0]])
    D = s.eye(2)-E
    G = s.diag(4, 8)
    w = s.Matrix(s.symbols("w0:2"))
    q = s.Matrix(s.symbols("q0:2"))
    u, v = w+D*q, w-D.T*q
    check("anisotropic free example satisfies the full potential identity",
          zero((u.dot(u)-v.dot(v))/2 - (4*G.inv()*w).dot(G*q)/2))
    A, B = 2*D*G.inv(), 2*D.T*G.inv()
    t1, t2 = -(A+B), (A+B)*A
    expected = s.Matrix([[0, s.Rational(1, 8)], [s.Rational(1, 8), 0]])
    check("first Baecklund commutator is nonzero with the stated coefficient",
          t1*t2-t2*t1 == expected)
    L = s.BlockMatrix([[s.zeros(2), s.eye(2)],
                       [-s.eye(2), s.zeros(2)]]).as_explicit()
    A, B = s.diag(A, A)*L, s.diag(B, B)*L
    W0 = -(A+B)
    W1 = 2*(A+B)*A-W0*W0
    check("the same obstruction occurs on real homogeneous Cauchy data",
          not zero(W0*W1-W1*W0))


def massive_phase_check():
    k1, k2 = s.symbols("k1 k2", real=True)
    m1, m2, m3 = s.symbols("m1 m2 m3", positive=True)
    omega3 = s.sqrt((k1+k2)**2+m3*m3)
    phase = s.sqrt(k1*k1+m1*m1)+s.sqrt(k2*k2+m2*m2)-omega3
    check("mixed derivative in the massive locality lemma",
          s.simplify(s.diff(phase, k1, k2)+m3*m3/omega3**3) == 0)
    resonant = {m1: 1, m2: 1, m3: 2}
    check("a threshold resonance is not an identically resonant phase",
          phase.subs(resonant).subs({k1: 0, k2: 0}) == 0 and
          phase.subs(resonant).subs({k1: 1, k2: -1}) != 0)


def roots_and_potential_check():
    roots = [s.Matrix([s.sqrt(2), 0]),
             s.Matrix([-1/s.sqrt(2), s.sqrt(6)/2]),
             s.Matrix([-1/s.sqrt(2), -s.sqrt(6)/2])]
    E = s.Matrix([[0, 1/s.sqrt(3)], [-1/s.sqrt(3), 0]])
    D = s.eye(2)-E
    beta = [s.simplify(D.T*a) for a in roots]
    check("coupled nonlinear example has M=3I and G=4I",
          zero(sum((a*a.T for a in roots), s.zeros(2))-3*s.eye(2)) and
          zero(sum((b*b.T for b in beta), s.zeros(2))-4*s.eye(2)))
    check("nonlinear potential identity, all independent exponential coefficients",
          all(zero(-D*roots[i]-beta[(i-1) % 3]) and
              all(s.simplify(roots[i].dot(beta[j])/2 -
                            (int(i == j)-int((i-1) % 3 == j))) == 0
                  for j in range(3)) for i in range(3)))
    return roots, D, beta


def nonlinear_jet_checks(roots, D, beta):
    # The exponential variables X_i represent exp(alpha_i.u). Their exact
    # chain rules avoid any truncation in field amplitude or nonlinearity.
    X = s.symbols("X0:3")
    size = 12
    uj = [[s.Symbol(f"u{a}_{j}") for j in range(size)] for a in range(2)]
    pj = [[s.Symbol(f"p{a}_{j}") for j in range(size)] for a in range(2)]
    p0 = s.Matrix([p[0] for p in pj])
    u1 = s.Matrix([u[1] for u in uj])
    force = sum((a*x for a, x in zip(roots, X)), s.zeros(2, 1))
    dx_rules = {uj[a][j]: uj[a][j+1] for a in range(2) for j in range(size-1)}
    dx_rules.update({pj[a][j]: pj[a][j+1] for a in range(2) for j in range(size-1)})
    dx_rules.update({x: a.dot(u1)*x for a, x in zip(roots, X)})
    top = {uj[a][-1] for a in range(2)} | {pj[a][-1] for a in range(2)}

    @cache
    def dx(expr):
        assert not expr.free_symbols & top, "jet allocation too small"
        return s.expand(sum(s.diff(expr, z)*dx_rules[z]
                            for z in expr.free_symbols if z in dx_rules))

    def dxn(expr, n):
        for _ in range(n):
            expr = dx(expr)
        return expr

    dt_rules = {uj[a][j]: pj[a][j] for a in range(2) for j in range(size-2)}
    dt_rules.update({pj[a][j]: uj[a][j+2]-dxn(force[a], j)
                     for a in range(2) for j in range(6)})
    dt_rules.update({x: a.dot(p0)*x for a, x in zip(roots, X)})

    @cache
    def dt(expr):
        assert all(z in dt_rules for z in expr.free_symbols), "missing time rule"
        return s.expand(sum(s.diff(expr, z)*dt_rules[z] for z in expr.free_symbols))

    def expseries(c, order):
        out = [s.S.One]
        for n in range(1, order+1):
            out.append(s.expand(sum(k*c[k]*out[n-k]
                                     for k in range(1, n+1))/n))
        return out

    order = 4
    q = [s.zeros(2, 1) for _ in range(order+2)]
    for n in range(1, order+1):
        nonlinear = s.zeros(2, 1)
        for b in beta:
            ex = expseries([s.expand(b.dot(q[k])) for k in range(n+1)], n)
            nonlinear += b*ex[n]
        # q[n] is still zero: only lower coefficients enter 'nonlinear'.
        rhs = (p0-u1)/2 if n == 1 else -D*q[n-1].applyfunc(lambda a: dt(a)-dx(a))/2
        q[n] = (rhs-nonlinear/4).applyfunc(s.expand)
    un = [s.S.Zero]*(order+1)
    for a, x in zip(roots, X):
        ex = expseries([s.expand(-a.dot(D*q[k])) for k in range(order+1)], order)
        for n in range(order+1):
            un[n] += x*ex[n]
    un[0] -= 3
    gn = [s.S.Zero]*(order+2)
    for b in beta:
        ex = expseries([s.expand(b.dot(q[k])) for k in range(order+2)], order+1)
        for n in range(order+2):
            gn[n] += ex[n]
    gn[0] -= 3
    rho, flux = {}, {}
    for n in range(1, order+1):
        rho[n] = s.expand(un[n-1]+gn[n+1])
        flux[n] = s.expand(-un[n-1]+gn[n+1])
        check(f"exact nonlinear local current at parameter order {n}",
              zero(dt(rho[n])+dx(flux[n])))

    def euler(expr, a, momentum=False):
        jets = pj[a] if momentum else uj[a]
        out = s.S.Zero
        if not momentum:
            out += sum(roots[i][a]*X[i]*s.diff(expr, X[i]) for i in range(3))
        for j, v in enumerate(jets):
            term = s.diff(expr, v)
            if term != 0:
                out += (-1)**j*dxn(term, j)
        return s.expand(out)

    check("nonlinear spin-three coefficient is a spatial derivative in A2",
          all(euler(rho[3], a, p) == 0 for a in range(2) for p in [False, True]))
    check("nonlinear spin-two charge is not a spatial derivative",
          any(euler(rho[2], a, p) != 0 for a in range(2) for p in [False, True]))
    bracket = s.expand(sum(euler(rho[2], a)*euler(rho[4], a, True) -
                           euler(rho[2], a, True)*euler(rho[4], a)
                           for a in range(2)))
    check("exact nonlinear Poisson bracket of spin-two and spin-four charges",
          all(euler(bracket, a, p) == 0 for a in range(2) for p in [False, True]))


if __name__ == "__main__":
    matrix_checks()
    obstruction_check()
    massive_phase_check()
    nonlinear_jet_checks(*roots_and_potential_check())
