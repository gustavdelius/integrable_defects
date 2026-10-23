"""Check Bristow's parent defect matrix and hence the consistent reduction.

Transcribes 1709.03927 (3.4.19), f=0, independently of book code.
Checks the complete gauge-transformed zero-curvature identity (3.2.5)
as a Laurent polynomial in independent exponentials and spectral parameter.
"""
import sympy as S

N=8
def unit(i,j):
    M=S.zeros(N); M[i-1,j-1]=1
    return M
H=[unit(2*i+1,2*i+1)-unit(2*i+2,2*i+2) for i in range(4)]
E=[unit(2,3)+unit(4,1),unit(1,3)+unit(4,2),
   unit(3,5)+unit(6,4),unit(5,7)+unit(8,6),unit(5,8)+unit(7,6)]
e=[M.T for M in E]
a,b,c,d,f=e
rt=S.sqrt(2)
P=S.symbols('P1:5',nonzero=True); Q=S.symbols('Q1:5',nonzero=True)
M2,M3,rho=S.symbols('M2 M3 rho',nonzero=True)
z,w=Q[1:3]; cz=z+1/z; cw=w+1/w
k=[S.eye(N)]
k.append(-a-b-rt*cz*c-cw*(d+f))
k.append(a*b+rt*(z*a*c+c*a/z)+rt*(z*b*c+c*b/z)
         +rt*cz*(w*c*d+d*c/w)+rt*cz*(w*c*f+f*c/w)+cw**2*d*f)
k.append(-rt*(z*a*b*c+c*a*b/z)
         -rt*(z*w*a*c*d+d*c*a/(z*w))
         -rt*(z*w*a*c*f+f*c*a/(z*w))
         -rt*(z*w*b*c*d+d*c*b/(z*w))
         -rt*(z*w*b*c*f+f*c*b/(z*w))
         -rt*cz*cw*(w*c*d*f+d*f*c/w))
k.append(2*c*a*b*c+2*cz**2*c*d*f*c
         +rt*(z*w*a*b*c*d+d*c*a*b/(z*w))
         +rt*(z*w*a*b*c*f+f*c*a*b/(z*w))
         +rt*cw*(z*w*a*c*d*f+d*f*c*a/(z*w))
         +rt*cw*(z*w*b*c*d*f+d*f*c*b/(z*w)))
k.append(-rt*cw*(z*w*a*b*c*d*f+d*f*c*a*b/(z*w))
         -2*(w*c*a*b*c*d+d*c*a*b*c/w)
         -2*(w*c*a*b*c*f+f*c*a*b*c/w)
         -2*cz*(z*a*c*d*f*c+c*d*f*c*a/z)
         -2*cz*(z*b*c*d*f*c+c*d*f*c*b/z))
k.append(2*z**2*a*b*c*d*f*c+2/z**2*c*d*f*c*a*b
         +2*w**2*c*a*b*c*d*f+2/w**2*d*f*c*a*b*c
         +2*a*c*d*f*c*a+2*b*c*d*f*c*b
         +2*d*c*a*b*c*d+2*f*c*a*b*c*f)
Kh=sum((ki/rho**i for i,ki in enumerate(k)),S.zeros(N))
Kh=Kh.applyfunc(S.expand)

def derivative(expr,var):
    return var*S.diff(expr,var)
def com(A,B): return A*B-B*A
def anti(A,B): return A*B+B*A
def check(name,mat):
    entries=[S.expand(v) for v in mat]
    bad=[(i,v) for i,v in enumerate(entries) if v!=0]
    print(('FAIL' if bad else 'PASS')+': '+name,flush=True)
    if bad:
        print(bad[:2],flush=True)
        raise AssertionError(name)

roots=[(-1,-1,0,0),(1,-1,0,0),(0,1,-1,0),(0,0,1,-1),(0,0,1,1)]
marks=[1,1,2,1,1]
def monomial(variables,root):
    return S.prod(v**r for v,r in zip(variables,root))
check('Cartan/root conventions',S.Matrix.vstack(*[com(H[j],E[i])-roots[i][j]*E[i] for i in range(5) for j in range(4)]))
check('root/transposed-root conventions',S.Matrix.vstack(*[com(E[i],e[i])-sum((roots[i][j]*H[j] for j in range(4)),S.zeros(N)) for i in range(5)]))

D=(P[0]+1/P[0])*M2/P[1]+2*cz*P[1]*M3/(P[2]*M2)+cw*(P[3]+1/P[3])*P[2]/M3
Db=(Q[0]+1/Q[0])*cz/M2+cw*M2/M3+(Q[3]+1/Q[3])*M3
mu=(1,M2,M3,1)
for name,V,is_plus in [('sigma part',D,True),('inverse sigma part',Db,False)]:
    lhs=derivative(Kh,z)*derivative(V,M2)+derivative(Kh,w)*derivative(V,M3)
    for j in range(4):
        lhs+=derivative(V,Q[j])*com(Kh,H[j])
        if is_plus:
            lhs+=derivative(V,P[j])*anti(Kh,H[j])
    rhs=S.zeros(N)
    for i,root in enumerate(roots):
        if is_plus:
            rhs+=2*rho*S.sqrt(marks[i])*monomial(P,root)/monomial(mu,root)*com(Kh,E[i])
        else:
            rhs-=2/rho*S.sqrt(marks[i])*monomial(mu,root)*(monomial(Q,root)*Kh*e[i]-e[i]*Kh/monomial(Q,root))
    check('all 64 zero-curvature entries, '+name,lhs-rhs)

# Leading term is invertible for every finite real field, so the restricted
# K is a genuine defect transport matrix for generic spectral parameter.
check('generic invertibility: leading coefficient is identity',k[0]-S.eye(N))
print('Completed 5 exact matrix checks (128 zero-curvature entries).',flush=True)
