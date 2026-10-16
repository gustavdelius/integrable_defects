#!/usr/bin/env python3
"""Independent exact checks for the replacement proof. Not a formalization."""
import sympy as s

def check(name, expression):
    residual = s.factor(s.cancel(s.expand(expression)))
    if residual != 0:
        residual = s.simplify(s.expand_trig(residual))
    if residual != 0:
        raise AssertionError(f'{name}: {residual}')
    print(f'PASS {name}', flush=True)

# Bianchi quadrilateral in exponential coordinates: exp(beta*u/2), etc.
U,V,W,e,f,z=s.symbols('U V W e f z', nonzero=True)
Z=U*(e*V-f*W)/(e*W-f*V)
eta=s.factor(V*s.diff(Z,V)/Z)
shdiff=lambda a,b: (a/b-b/a)/2
shsum=lambda a,b: (a*b-1/(a*b))/2
# Factors C and C2 cancel, so each chiral equation is independently normalized.
bminus=shdiff(U,V)/e-z
cminus=shdiff(U,W)/f-z
dminus=z+eta*(bminus-cminus)
bplus=z+e*shsum(U,V)
cplus=z+f*shsum(U,W)
dplus=z+eta*(bplus-cplus)
check('Bianchi minus edge (v,z)',bminus+dminus-shdiff(V,Z)/f)
check('Bianchi minus edge (w,z)',cminus+dminus-shdiff(W,Z)/e)
check('Bianchi plus edge (v,z)',bplus-dplus+f*shsum(V,Z))
check('Bianchi plus edge (w,z)',cplus-dplus+e*shsum(W,Z))

# The scalar nonlinear defect (beta = 1; analytic beta dependence is in the proof).
u,v,ut,vt,M,eps=s.symbols('u v u_t v_t M eps', nonzero=True)
B=4*(s.cosh((u-v)/2)-1)/eps+eps*M*(s.cosh((u+v)/2)-1)
P=4*(s.cosh((u-v)/2)-1)/eps-eps*M*(s.cosh((u+v)/2)-1)
Bu,Bv=s.diff(B,u),s.diff(B,v)
ux,vx=vt-Bu,ut+Bv
check('defect potential wave equation',s.diff(B,u,2)-s.diff(B,v,2))
check('defect energy current',Bu*ut+Bv*vt+s.diff(P,u)*ux+s.diff(P,v)*vx)
check('spectral derivative eps*dP/deps=-B',eps*s.diff(P,eps)+B)
check('momentum balance',s.diff(P,u)*ut+s.diff(P,v)*vt-(ut**2+ux**2-vt**2-vx**2)/2+M*(s.cosh(u)-s.cosh(v)))

# Differential polynomial algebra for KdV and its Gardner map.
w=s.symbols('w0:10')
D=lambda expr: s.expand(sum(s.diff(expr,w[j])*w[j+1] for j in range(9)))
G=-D(w[2]+3*w[0]**2-2*eps**2*w[0]**3)
miura=w[0]+eps*w[1]-eps**2*w[0]**2
miura_t=G+eps*D(G)-2*eps**2*w[0]*G
check('Gardner intertwines KdV',miura_t+D(D(D(miura)))+6*miura*D(miura))
coeff=[w[0]]
for n in range(1,7):
    coeff.append(s.expand(-D(coeff[n-1])+sum(coeff[i]*coeff[n-2-i] for i in range(n-1))))
print('Gardner coefficients w_0 ... w_4:',coeff[:5],flush=True)
# Third-order squared-eigenfunction identity used for the Lenard pencil.
r,r1,r2,R=s.symbols('r r1 r2 R')
Rx=2*r*R-1/eps
Rxx=2*r1*R+2*r*Rx
Rxxx=2*r2*R+4*r1*Rx+2*r*Rxx
check('Gardner Lenard identity',Rxxx-4*(r1+r*r)*Rx-2*(r2+2*r*r1)*R)

# Quadratic temporal Bäcklund map and its symplecticity.
k=s.symbols('k', real=True)
a=1+eps**2*M/4
b=1-eps**2*M/4
Dsymbol=s.symbols('Dsymbol')
T=s.Matrix([[b,-eps],[eps*(M-Dsymbol**2),b]])/(a-eps*Dsymbol)
J=s.Matrix([[0,1],[-1,0]])
res=s.simplify(T.subs(Dsymbol,-Dsymbol).T*J*T-J)
for i in range(2):
    for j in range(2): check(f'linearized temporal symplecticity {i}{j}',res[i,j])
print('All exact checks passed.',flush=True)
