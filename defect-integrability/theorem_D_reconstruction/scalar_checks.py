#!/usr/bin/env python3
"""Actual on-shell jet derivations and charge checks for beta=1, arbitrary mass squared."""
import sympy as s
u=s.symbols('u0:30')
p=s.symbols('p0:30')
M,e=s.symbols('M e')

def Dx(f):
    f=s.sympify(f)
    assert not ({u[-1],p[-1]} & f.free_symbols), 'Increase the jet buffer'
    return s.expand(sum(s.diff(f,u[j])*u[j+1]+s.diff(f,p[j])*p[j+1]
                        for j in range(len(u)-1) if u[j] in f.free_symbols or p[j] in f.free_symbols))
force=[u[2]-M*s.sinh(u[0])]
def Dt(f):
    f=s.sympify(f)
    terms=[]
    for j in range(len(u)):
        if u[j] in f.free_symbols: terms.append(s.diff(f,u[j])*p[j])
        if p[j] in f.free_symbols:
            while len(force)<=j: force.append(Dx(force[-1]))
            terms.append(s.diff(f,p[j])*force[j])
    return s.expand(sum(terms))
def check(label,f):
    f=s.expand(f)
    if f != 0: f=s.simplify(f)
    if f != 0: raise AssertionError((label,f))
    print('PASS',label,flush=True)
N=5
def mul_trunc(a,b,n):
    out=[0]*(n+1)
    for i in range(min(len(a),n+1)):
        for j in range(min(len(b),n+1-i)): out[i+j]+=a[i]*b[j]
    return [s.expand(x) for x in out]

coeff=[]
for n in range(1,N+1):
    ds=[0]+coeff+[0]*(n-len(coeff))
    powers={0:[1]+[0]*n}
    for j in range(1,6): powers[j]=mul_trunc(powers[j-1],ds,n)
    timepart=u[1]-p[0] if n==1 else -Dt(coeff[n-2])
    masspart=0
    if n>=2:
        masspart=M/2*(sum(s.sinh(u[0])*powers[2*j][n-2]/(2**(2*j)*s.factorial(2*j)) for j in range(3))
                      +sum(s.cosh(u[0])*powers[2*j+1][n-2]/(2**(2*j+1)*s.factorial(2*j+1)) for j in range(3)))
    an=s.expand(timepart+masspart-powers[3][n]/24-powers[5][n]/1920)
    coeff.append(an)
    print('Computed scalar partner coefficient',n,flush=True)

Ds=[0]+coeff
powers={0:[1]+[0]*(N+1)}
for j in range(1,7): powers[j]=mul_trunc(powers[j-1],Ds,N+1)
charges=[]
for n in range(1,N+1):
    g=sum(4*powers[2*j][n+1]/(2**(2*j)*s.factorial(2*j)) for j in range(1,4))
    f=M*(sum(s.cosh(u[0])*powers[2*j][n-1]/(2**(2*j)*s.factorial(2*j)) for j in range(3))
         +sum(s.sinh(u[0])*powers[2*j+1][n-1]/(2**(2*j+1)*s.factorial(2*j+1)) for j in range(3))-(1 if n==1 else 0))
    q=s.expand(g+f); flux=s.expand(g-f)
    charges.append(q)
    check(f'scalar local current coefficient {n}',Dt(q)+Dx(flux))
check('second scalar density is a spatial divergence',charges[1]-Dx((u[1]-p[0])**2/2))

def variational(f,jet):
    out=0
    for j in range(len(jet)):
        if jet[j] not in f.free_symbols: continue
        term=s.diff(f,jet[j])
        for _ in range(j): term=-Dx(term)
        out+=term
    return s.expand(out)
# An integrated bracket vanishes iff its density has both zero Euler derivatives,
# up to a constant. Here every bracket density vanishes at the vacuum.
q3,q5=charges[2],charges[4]
bracket=s.expand(variational(q3,u)*variational(q5,p)-variational(q3,p)*variational(q5,u))
check('Q3 Q5 Poisson bracket: u variational derivative',variational(bracket,u))
check('Q3 Q5 Poisson bracket: p variational derivative',variational(bracket,p))
print('All nonlinear scalar checks passed.',flush=True)
