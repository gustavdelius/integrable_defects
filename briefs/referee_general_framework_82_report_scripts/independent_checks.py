"""Independent exact checks; imports no manuscript code. Run from repository root."""
import sympy as s

def check(label, expr):
    if isinstance(expr, s.MatrixBase):
        ok = all(s.simplify(v) == 0 for v in expr)
    else:
        ok = s.simplify(expr) == 0
    print(('PASS ' if ok else 'FAIL ') + label, flush=True)
    assert ok

# Cyclic realization of A_(n-1), on the sum-zero hyperplane of R^n.
# Inverting I-P only on that hyperplane avoids arbitrary root coordinates.
for n in range(3, 8):
    P = s.zeros(n)
    for i in range(n):
        P[(i+1) % n, i] = 1
    J = s.ones(n)/n
    H = s.eye(n)-J
    D = 2*((s.eye(n)-P+J).inv()-J)
    roots = [s.eye(n)[:, i]-s.eye(n)[:, (i+1) % n] for i in range(n)]
    M = sum((a*a.T for a in roots), s.zeros(n))
    check(f'A{n-1}: normalized coupling on sum-zero space', D+D.T-2*H)
    check(f'A{n-1}: transparent Hessian exactly 4I on sum-zero space', D.T*M*D-4*H)
    # Exponentials are represented by their exact exponent covectors (w,q).
    # Thus this is coefficient matching, not numerical sampling.
    terms = {}
    def term(a,b,c):
        key = tuple(a)+tuple(b)
        terms[key] = terms.get(key, 0)+c
    for a in roots:
        term(a,D.T*a,1)
        term(a,-D*a,-1)
        for b in roots:
            term(a,D.T*b,-(a.T*D.T*b)[0]/2)
    check(f'A{n-1}: exact exponential momentum constraint', sum(v*v for v in terms.values()))

# Two orthonormal field coordinates, choosing a clockwise Coxeter rotation.
rt=s.sqrt
E=s.Matrix([[0,1/rt(3)],[-1/rt(3),0]])
D=s.eye(2)-E
roots=[s.Matrix([rt(2),0]),s.Matrix([-1/rt(2),rt(6)/2]),s.Matrix([-1/rt(2),-rt(6)/2])]
u=s.Matrix(s.symbols('u0:2'))
p=s.Matrix(s.symbols('p0:2'))
ux=s.Matrix(s.symbols('ux0:2'))
px=s.Matrix(s.symbols('px0:2'))
uxx=s.Matrix(s.symbols('uxx0:2'))
h=p-ux
dot=lambda a,b:(a.T*b)[0]
U3=sum(dot(a,u)**3 for a in roots)/6
U=3*dot(u,u)/2+U3
Up=s.Matrix([s.diff(U,v) for v in u])
C=lambda a,b:sum((r*dot(r,a)*dot(r,b) for r in roots),s.zeros(2,1))
T=lambda a,b:sum((D.T*r*dot(r,D*a)*dot(r,D*b) for r in roots),s.zeros(2,1))
T3=lambda a:dot(a,T(a,a))
q1=h/2
# Full nonlinear field equations, through amplitude degree two.
dmh=2*uxx-2*px-Up
q2=-D*dmh/4-T(h,h)/32
check('A2: epsilon^2 branch recursion with full nonlinear flow',4*q2+T(q1,q1)/2+D*dmh)
Q1=U+2*dot(q1,q1)
Q2=-dot(Up,D*q1)+4*dot(q1,q2)+T3(q1)/6
Q2compact=dot(h,D*(px-uxx))-dot(h,E*Up)-T3(h)/24
check('A2: Q2 exact through cubic amplitude',Q2-Q2compact)
print('U_cubic =',s.expand(U3))
print('g_cubic(h) =',s.simplify(T3(h)/6))

# Independently extract the epsilon coefficients by Taylor composition.
ep=s.Symbol('epsilon')
q=ep*q1+ep**2*q2
w=u-D*q
Uofw=3*dot(w,w)/2+sum(dot(a,w)**3 for a in roots)/6
B=ep*Uofw+(2*dot(q,q)+T3(q)/6)/ep
check('A2: energy coefficient Q1 by direct composition',s.expand(B).coeff(ep,1)-Q1)
check('A2: energy coefficient Q2 by direct composition',s.expand(B).coeff(ep,2)-Q2)

# Polarized normal modes resolve the two equal-mass species. Positive frequency
# is omega=sqrt(k^2+3); E z=i e z and z^dagger z=1.
k,om,ell=s.symbols('k omega ell', real=True)
a,ab,Z=s.symbols('a abar Z')
for sign in [1,-1]:
    e=sign/rt(3)
    z=s.Matrix([1,sign*s.I])/rt(2)
    check(f'A2: polarization {sign}',E*z-s.I*e*z)
    uv=a*z*Z+ab*s.conjugate(z)/Z
    pv=-s.I*om*a*z*Z+s.I*om*ab*s.conjugate(z)/Z
    uxv=s.I*k*a*z*Z-s.I*k*ab*s.conjugate(z)/Z
    pxv=k*om*uv
    uxxv=-k*k*uv
    sub=dict(zip(list(u)+list(p)+list(ux)+list(px)+list(uxx),list(uv)+list(pv)+list(uxv)+list(pxv)+list(uxxv)))
    def avg2(expr):
        return s.expand(expr.subs(sub, simultaneous=True)).coeff(Z,0).coeff(a,1).coeff(ab,1)
    m1=avg2(Q1)
    m2=avg2(Q2compact)
    reduce=lambda x:s.rem(s.together(x).as_numer_denom()[0],om**2-k**2-3,om)
    check(f'A2: full nonlinear Q1 symbol polarization {sign}',reduce(m1-(3+(om+k)**2)))
    check(f'A2: full nonlinear Q2 symbol polarization {sign}',reduce(m2-e*(om+k)*(3+(om+k)**2)))
    symbol=4*ep*(3+ell**2)/(4-4*e*ep*ell+(1+e*e)*ep**2*ell**2)
    check(f'A2: plane-wave Q1 agrees polarization {sign}',s.diff(symbol,ep).subs(ep,0)-(3+ell**2))
    check(f'A2: plane-wave Q2 agrees polarization {sign}',s.diff(symbol,ep,2).subs(ep,0)/2-e*ell*(3+ell**2))

# Tzitzeica: all first derivatives vanish, including the auxiliary direction.
P,Q,L,eps=s.symbols('P Q L eps',nonzero=True)
f=eps*(s.exp(2*P-2*L)+2*s.exp(-P+L)*s.cosh(Q))
g=(8*s.exp(-L)+4*s.exp(2*L)*s.cosh(Q)**2)/(2*eps)
check('Tzitzeica: no linear part in P,q,lambda',s.Matrix([s.diff(f+g,v).subs({P:0,Q:0,L:0}) for v in [P,Q,L]]))
print('All independent exact checks passed.',flush=True)
