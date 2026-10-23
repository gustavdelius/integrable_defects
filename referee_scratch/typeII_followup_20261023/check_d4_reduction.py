"""Independent exact check: candidate is a consistent reduction of D4.

Parent potential: Bristow 1709.03927, (2.4.10)-(2.4.11), f=0.
No existing manuscript/check code imported.
"""
import sympy as S

p=S.symbols('p1:5',real=True); q=S.symbols('q1:5',real=True)
n2,n3=S.symbols('n2 n3',real=True)
sig=S.symbols('sigma',positive=True)
x,y,r,w,ell=S.symbols('x y r w ell',real=True)
mu2,mu3=S.symbols('mu2 mu3',real=True)
passed=0

def simp(v):
    v=S.expand_power_exp(v)
    v=S.powdenest(v,force=True)  # all cosh(real) factors are strictly positive
    return S.factor(S.expand(v.rewrite(S.exp)))

def check(name,v):
    global passed
    vals=list(v) if isinstance(v,(list,tuple,S.MatrixBase)) else [v]
    vals=[simp(z) for z in vals]
    ok=all(z==0 for z in vals)
    print(('PASS' if ok else 'FAIL')+': '+name,flush=True)
    if not ok:
        print(vals,flush=True)
        raise AssertionError(name)
    passed+=1

def U4(v):
    a,b,c,d=v
    return 2*S.cosh(a)*S.exp(-b)+2*S.exp(b-c)+2*S.cosh(d)*S.exp(c)

# First-principles check of the parent momentum identity, to avoid assuming
# the cited formula is correct or using a damaged OCR expression.
D=sig*(2*S.cosh(p[0])*S.exp(-p[1]+mu2)
       +4*S.cosh(q[1])*S.exp(p[1]-p[2]-mu2+mu3)
       +4*S.cosh(q[2])*S.cosh(p[3])*S.exp(p[2]-mu3))
Db=(4*S.cosh(q[0])*S.cosh(q[1])*S.exp(-mu2)
    +2*S.cosh(q[2])*S.exp(mu2-mu3)
    +2*S.cosh(q[3])*S.exp(mu3))/sig
K=(S.diff(D,p[0])*S.diff(Db,q[0])+S.diff(D,p[3])*S.diff(Db,q[3])
   +S.diff(D,q[1])*S.diff(Db,mu2)-S.diff(D,mu2)*S.diff(Db,q[1])
   +S.diff(D,q[2])*S.diff(Db,mu3)-S.diff(D,mu3)*S.diff(Db,q[2]))/2
check('parent D4 momentum identity, recomputed',K-U4([p[i]+q[i] for i in range(4)])+U4([p[i]-q[i] for i in range(4)]))

# An invertible auxiliary change symmetrizes the published potential.
# mu_j=n_j+log(2 cosh(q_j))/2, j=2,3; kinetic change is a total derivative.
c2=2*S.cosh(q[1]); c3=2*S.cosh(q[2])
Ds=sig*(2*S.cosh(p[0])*S.sqrt(c2)*S.exp(-p[1]+n2)
        +2*S.sqrt(c2*c3)*S.exp(p[1]-p[2]-n2+n3)
        +2*S.cosh(p[3])*S.sqrt(c3)*S.exp(p[2]-n3))
Dbs=(2*S.cosh(q[0])*S.sqrt(c2)*S.exp(-n2)
     +S.sqrt(c2*c3)*S.exp(n2-n3)
     +2*S.cosh(q[3])*S.sqrt(c3)*S.exp(n3))/sig
mu_map={mu2:n2+S.log(c2)/2,mu3:n3+S.log(c3)/2}
check('symmetric auxiliary gauge: D',D.subs(mu_map,simultaneous=True)-Ds)
check('symmetric auxiliary gauge: Dbar',Db.subs(mu_map,simultaneous=True)-Dbs)
reflection={p[0]:p[3],p[1]:-p[2],p[2]:-p[1],p[3]:p[0],
            q[0]:q[3],q[1]:-q[2],q[2]:-q[1],q[3]:q[0],n2:-n3,n3:-n2}
check('D4 bulk invariant under the folding involution',U4(p).subs(reflection,simultaneous=True)-U4(p))
check('defect D invariant under the folding involution',Ds.subs(reflection,simultaneous=True)-Ds)
check('defect Dbar invariant under the folding involution',Dbs.subs(reflection,simultaneous=True)-Dbs)

fold={p[0]:x,p[1]:-y,p[2]:y,p[3]:x,
      q[0]:r,q[1]:-w,q[2]:w,q[3]:r,n3:-n2}
# Gradient components normal to the fixed subspace must vanish. Checking
# them rules out an inconsistent substitution that merely matches energies.
for name,V in [('bulk',U4(p)),('defect',Ds+Dbs)]:
    derivatives=[S.diff(V,p[0])-S.diff(V,p[3]),S.diff(V,p[1])+S.diff(V,p[2])]
    if name=='defect':
        derivatives += [S.diff(V,q[0])-S.diff(V,q[3]),S.diff(V,q[1])+S.diff(V,q[2]),S.diff(V,n2)+S.diff(V,n3)]
    check(f'normal gradients vanish: {name}',[v.subs(fold,simultaneous=True) for v in derivatives])

# Direct map in the ORIGINAL published auxiliary variables.
# Parent fields=(u1,-u2,u2,u1), similarly on the right.
# Divide the restricted action by 2 and rescale spacetime by sqrt(2).
mapping={p[0]:x,p[1]:-y,p[2]:y,p[3]:x,
         q[0]:r,q[1]:-w,q[2]:w,q[3]:r,
         mu2:(ell-y)/2+S.Rational(2,3)*S.log(2),
         mu3:(y-ell)/2+S.log(S.cosh(w))+S.log(2)/3,
         sig:sig/2**S.Rational(1,6)}
F=sig*(2*S.cosh(x)*S.exp((y+ell)/2)+S.cosh(w)**2*S.exp(-y-ell))
G=(2*S.cosh(r)*S.cosh(w)*S.exp((y-ell)/2)+S.exp(-y+ell))/sig
check('published D4 D reduces exactly to candidate F',D.subs(mapping,simultaneous=True)/(2*S.sqrt(2))-F)
check('published D4 Dbar reduces exactly to candidate G',Db.subs(mapping,simultaneous=True)/(2*S.sqrt(2))-G)
U=S.exp(y)*S.cosh(x)+S.exp(-2*y)/2-S.Rational(3,2)
check('bulk potential and mass normalization',(U4(p).subs(mapping,simultaneous=True)-6)/4-U)

# Compare kinetic one-forms via exterior derivatives, avoiding arbitrary
# total derivative primitives of log(cosh(w)).
u1,u2,v1,v2,lam=S.symbols('u1 u2 v1 v2 lam',real=True)
coords=(u1,u2,v1,v2,lam)
P=(u2+v2)/2; Q=(u2-v2)/2
M2=(lam-P)/2+S.Rational(2,3)*S.log(2)
M3=(P-lam)/2+S.log(S.cosh(Q))+S.log(2)/3
# Parent restricted kinetic one-form divided by 2:
source=S.Matrix([0,M3-M2,u1,u2-(M3-M2),0])
target=S.Matrix([0,0,u1,0,u2-v2])
diff=source-target
curl=S.Matrix(5,5,lambda i,j:S.diff(diff[j],coords[i])-S.diff(diff[i],coords[j]))
check('kinetic terms agree modulo a total time derivative',curl)
print(f'Completed {passed} exact checks.',flush=True)
