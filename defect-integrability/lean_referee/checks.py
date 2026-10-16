import sympy as sp
t,x,eps,m=sp.symbols('t x epsilon m')
phi=sp.Function('phi')(t); psi=sp.Function('psi')(t)
# Free massive defect Lagrangian of paper Sec 4.3 example
Ld=sp.Rational(1,2)*(phi*psi.diff(t)-psi*phi.diff(t))-(phi-psi)**2/(2*eps)-eps*m**2/8*(phi+psi)**2
def EL(L,f): return sp.diff(L,f)-sp.diff(sp.diff(L,f.diff(t)),t)
dSdpsi=sp.simplify(EL(Ld,psi))
# A_phi=-psi/2, A_psi=phi/2 ; Omega_{psi phi}=d_psi A_phi - d_phi A_psi = -1
Om_psiphi=-1
gradpsi_B = sp.diff((phi-psi)**2/(2*eps)+eps*m**2/8*(phi+psi)**2, psi)
paper = -Om_psiphi*phi.diff(t) - gradpsi_B         # paper (4.7) line 2 (psi_t term absent: Om_psipsi=0)
correct = +Om_psiphi*phi.diff(t) - gradpsi_B
print("pi_+ = +dS/dpsi =", sp.expand(dSdpsi))
print("(4.7) line 2 as printed matches:", sp.simplify(dSdpsi-paper)==0, "| with +Omega:", sp.simplify(dSdpsi-correct)==0)
# NLS: flux of |u|^2
X,T=sp.symbols('x t',real=True)
u=sp.Function('u')(X,T); ub=sp.Function('ub')(X,T); V=sp.Function('V')
L=sp.I/2*(ub*u.diff(T)-u*ub.diff(T))-u.diff(X)*ub.diff(X)-V(u*ub)
from sympy.calculus.euler import euler_equations
eqs=euler_equations(L,[u,ub],[X,T])
sol=sp.solve([e.lhs for e in eqs],[u.diff(T),ub.diff(T)],dict=True)[0]
dtN=(u*ub).diff(T).subs(sol)
J_paper=sp.I*(ub*u.diff(X)-u*ub.diff(X))
print("dt N + dx J_paper =", sp.simplify(sp.expand(dtN+J_paper.diff(X))))
print("dt N - dx J_paper =", sp.simplify(sp.expand(dtN-J_paper.diff(X))))
T01=-(sp.diff(L,u.diff(T))*u.diff(X)+sp.diff(L,ub.diff(T))*ub.diff(X))
print("J_paper / T01 =", sp.simplify(J_paper/T01))
