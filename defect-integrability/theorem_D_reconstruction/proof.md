# A reconstruction of Theorem D: a complete scalar result and the remaining general problem

This manuscript replaces the missing arguments by explicit calculations in a substantial, precisely specified case. It proves the implication from a momentum-preserving defect to an infinite independent commuting hierarchy for one relativistic scalar with a normalized Type-I defect and a nondegenerate vacuum. It does **not** prove that implication for arbitrary multicomponent, Type-II, or higher-spatial-derivative theories. In particular, it does not assume Bianchi permutability, a Hamiltonian-generator property, or independence as hypotheses of the scalar theorem: these are proved below.

The scalar potentials and defects obtained here are the familiar free, sine-Gordon, and sinh-Gordon ones. These are classical examples: see Bowcock–Corrigan–Zambon, [*Classically integrable field theories with defects*](https://arxiv.org/abs/hep-th/0305022), Section 2, and [*Affine Toda field theories with defects*](https://arxiv.org/abs/hep-th/0401020), Section 2. The purpose here is a self-contained reconstruction of the implication under discussion, including the bridges missing from the submitted proof, not a novelty claim for the scalar classification.

All parameter expansions below are **formal**. Each coefficient is a finite-order local differential expression; neither convergence of the whole series nor existence of a finite-parameter transformation on a Sobolev space is asserted. Integrals are over a spatial circle, so spatial divergences integrate to zero. The local identities also apply with suitable spatial decay. No decay in time is required for the scalar theorem.

## 1. The theorem actually proved

**Theorem S.** Consider the real scalar Lagrangian

$$
 L(u)=\frac12u_t^2-\frac12u_x^2-U(u),
 \qquad U(0)=U'(0)=0,\qquad U''(0)=M>0,
$$

where $U$ is analytic near the vacuum. Suppose a Type-I defect has Lagrangian

$$
 L_d(u,v)=\frac12(u v_t-v u_t)-B(u,v),
 \qquad B(0,0)=B_u(0,0)=B_v(0,0)=0,
$$

with analytic $B$. Assume its sewing conditions admit the momentum balance

$$
 D_tP_d=T^{11}(u)-T^{11}(v),\qquad
 T^{11}(u)=\frac12(u_t^2+u_x^2)-U(u),                 \tag{1.1}
$$

as an identity for arbitrary boundary histories after imposing the sewing conditions. Here $P_d$ is a local function of finitely many time jets, with no explicit spacetime dependence. This is an off-shell boundary identity, not a statement only on a selected set of bulk solutions. The decomposition $B(u,v)=f(u+v)+g(u-v)$ will be derived below. Its curvature

$$
 h=g''(0)                                          \tag{1.2}
$$

is necessarily nonzero; this is a consequence, not an additional hypothesis. Then the bulk equation $u_{tt}-u_{xx}+U'(u)=0$ has infinitely many local conserved functionals $I_1,I_3,I_5,\ldots$ which are pairwise in involution for

$$
 \{F,G\}=\int\left(\frac{\delta F}{\delta u}\frac{\delta G}{\delta p}
 -\frac{\delta F}{\delta p}\frac{\delta G}{\delta u}\right)dx,
 \qquad p=u_t.                                      \tag{1.3}
$$

For every $N$, the first $N$ of these functionals are functionally independent on an open set arbitrarily close to the vacuum. They are produced by the defect itself through a derived one-parameter family. The family contains the given defect at parameter $\epsilon=1/h$, locally in field space.

The theorem deliberately excludes a vacuum with $M=0$, a different defect one-form, auxiliary defect variables, and several bulk fields. Those cases require additional work; they are not implicit in this statement.

## 2. Momentum conservation determines the potential and the parameter

Variation of the action gives

$$
 u_x=v_t-B_u,\qquad v_x=u_t+B_v.                    \tag{2.1}
$$

First $P_d$ has no genuine dependence on time derivatives. Indeed, if it depended on a time jet of maximal order $r\ge1$, its total time derivative would contain independent jets of order $r+1$, whereas the right side of (1.1), after (2.1), contains only $u,v,u_t,v_t$. Their coefficients force independence of the maximal jets. Descending induction leaves $P_d=P_d(u,v)$. This step uses exactly the off-shell qualification in the theorem.

Substitution of (2.1) into (1.1) gives

$$
 (P_d)_u u_t+(P_d)_v v_t
 =-B_vu_t-B_uv_t+\frac12(B_u^2-B_v^2)-U(u)+U(v).
$$

Independence of $u_t,v_t$, followed by equality of mixed derivatives of $P_d$, gives

$$
 (P_d)_u=-B_v,\quad (P_d)_v=-B_u,\quad
 B_{uu}=B_{vv},\quad
 \frac12(B_u^2-B_v^2)=U(u)-U(v).                     \tag{2.2}
$$

Set $s=u+v, d=u-v$. The equation $B_{uu}=B_{vv}$ in (2.2) gives

$$
 B=f(s)+g(d),\qquad P_d=g(d)-f(s),\qquad
 2f'(s)g'(d)=U((s+d)/2)-U((s-d)/2),                 \tag{2.3}
$$

where irrelevant constants are normalized to zero. The vacuum conditions give $f'(0)=g'(0)=0$. Differentiating (2.3) once in $s$ and once in $d$ at the origin gives $2f''(0)g''(0)=M/2$. Thus $h=g''(0)\ne0$. Differentiation in $d$ at zero now yields

$$
 f'(s)=\frac{U'(s/2)}{2h}.                          \tag{2.4}
$$

Applying $\partial_u\partial_v=\partial_s^2-\partial_d^2$ to (2.3) gives

$$
 f'''(s)g'(d)-f'(s)g'''(d)=0.                       \tag{2.5}
$$

Both $f'$ and $g'$ are nonzero analytic functions: $f''(0)=M/(4h)\ne0$ and $g''(0)=h\ne0$. Fixing a point where each is nonzero in turn shows that there is a real constant $a$ with $f'''=af'$ and $g'''=ag'$. The identities extend across their zeros by analyticity. Equation (2.4) implies

$$
 U'''=\kappa U',\qquad \kappa=4a.                  \tag{2.6}
$$

Define the entire functions

$$
 C_\kappa(z)=\sum_{n\ge1}\frac{\kappa^{n-1}z^{2n}}{(2n)!},
 \qquad S_\kappa(z)=C_\kappa'(z).
$$

Thus $C_0(z)=z^2/2$; for $\kappa=\beta^2\ne0$,

$$
 C_\kappa(z)=\frac{\cosh(\beta z)-1}{\beta^2},
 \qquad S_\kappa(z)=\frac{\sinh(\beta z)}{\beta}.
$$

Negative $\kappa$ gives the real trigonometric functions through the same series. Solving (2.6) with the vacuum data, and then solving for $f,g$, gives

$$
 U(u)=M C_\kappa(u),\quad
 f(s)=\frac{M}{h}C_\kappa(s/2),\quad
 g(d)=4h C_\kappa(d/2).                             \tag{2.7}
$$

In particular, the product constraint in (2.3) is invariant under inverse rescalings of $f$ and $g$. It supplies the family

$$
 \boxed{B_\epsilon(u,v)=\frac4\epsilon C_\kappa((u-v)/2)
                  +\epsilon M C_\kappa((u+v)/2)},
$$

$$
 \boxed{P_\epsilon(u,v)=\frac4\epsilon C_\kappa((u-v)/2)
                  -\epsilon M C_\kappa((u+v)/2)}.   \tag{2.8}
$$

Every member obeys (2.2). This derives the parameter from momentum conservation in the stated class; no presumed spectral parameter or boost orbit is needed.

## 3. A local formal transformation satisfying both sewing equations

Work in the algebra of finite-order local functions of the Cauchy jets $u_j=D_x^ju, p_j=D_x^jp$. On this algebra set

$$
 D_xu_j=u_{j+1},\quad D_xp_j=p_{j+1},\quad
 D_tu_j=p_j,\quad D_tp_j=D_x^j(u_2-U'(u)).           \tag{3.1}
$$

These are actual derivations and commute. Equation (3.1) is the bulk equation and all its differential consequences, not a derivation acting on integers.

Write $v=u+\Delta$, where $\Delta=\sum_{n\ge1}\epsilon^na_n$. The first sewing equation is equivalent to

$$
 2S_\kappa(\Delta/2)
 =\epsilon(u_x-p-D_t\Delta)
   +\frac{\epsilon^2M}{2}S_\kappa(u+\Delta/2).       \tag{3.2}
$$

The left side is $\Delta+O(\Delta^3)$. At order $\epsilon^n$, its only occurrence of $a_n$ is $a_n$ itself. Every other term uses earlier coefficients: $D_t\Delta$ carries an extra $\epsilon$, the last term carries $\epsilon^2$, and the nonlinear terms on the left have degree at least three in $\Delta$. Consequently (3.2) determines a unique local coefficient $a_n$ by algebraic recursion. No inversion of a differential operator is involved. For example,

$$
 a_1=u_x-p,\qquad
 a_2=u_{xx}-p_x-\frac12U'(u).                      \tag{3.3}
$$

The second sewing equation must still be proved. Define its residual

$$
 R=v_x-u_t-(B_\epsilon)_v.
$$

Differentiating the first sewing equation, substituting this definition, and using (2.2), gives the exact identity

$$
 u_{xx}-u_{tt}=U'(u)+(D_t-(B_\epsilon)_{uv})R.       \tag{3.4}
$$

On the left bulk equation, $(D_t-(B_\epsilon)_{uv})R=0$. On the formal diagonal branch,

$$
 (B_\epsilon)_{uv}=-\epsilon^{-1}+O(\epsilon).
$$

If a nonzero Laurent series $R$ bounded below began with $\epsilon^rR_r$, the lowest term of $(D_t-(B_\epsilon)_{uv})R$ would be $\epsilon^{r-1}R_r$. There is no other term of that order. Hence $R=0$. This proves the second sewing equation coefficient by coefficient. Differentiating the two sewing equations then gives

$$
 v_{xx}-v_{tt}=U'(v).
$$

The substitution $T_\epsilon:(u,p)\mapsto(v,D_tv)$ therefore commutes with the bulk evolution and is $\mathrm{Id}+O(\epsilon)$. Its formal inverse exists recursively as a substitution. Its coefficients have finite differential order at every order in $\epsilon$.

## 4. Conserved densities, with the regular terms included

The following identity uses only the full sewing equations and the two first-derivative identities in (2.2):

$$
\begin{aligned}
 D_tB_\epsilon+D_xP_\epsilon
 &=B_u u_t+B_vv_t-B_vu_x-B_uv_x\\
 &=0.                                               \tag{4.1}
\end{aligned}
$$

On the diagonal branch the apparent pole in (2.8) disappears, since $C_\kappa(\Delta/2)=O(\epsilon^2)$. Define

$$
 B_\epsilon(u,T_\epsilon u)=\sum_{n\ge1}\epsilon^n\rho_n,
 \qquad
 P_\epsilon(u,T_\epsilon u)=\sum_{n\ge1}\epsilon^nj_n.
$$

Then $D_t\rho_n+D_xj_n=0$ and $I_n=\int\rho_n\,dx$ is conserved. In particular,

$$
 \rho_1=\frac12(u_x-p)^2+U(u),\qquad
 j_1=\frac12(u_x-p)^2-U(u).                          \tag{4.2}
$$

The $\epsilon M C_\kappa((u+v)/2)$ term in $B_\epsilon$ contributes all of $U(u)$. Discarding this regular term would give an incorrect first charge. Also,

$$
 \rho_2=D_x\bigl((u_x-p)^2/2\bigr),                \tag{4.3}
$$

so not every coefficient supplies a nonzero charge. Section 7 proves independence of the odd-indexed subsequence.

## 5. Bianchi permutability is an explicit identity

For $\kappa=\beta^2\ne0$, set $D_\pm=D_t\pm D_x$. The sewing equations become

$$
 D_+(u-v)=-\frac{\epsilon M}{\beta}
              \sinh\!\left(\frac{\beta(u+v)}2\right),\qquad
 D_-(u+v)=\frac4{\beta\epsilon}
              \sinh\!\left(\frac{\beta(u-v)}2\right).             \tag{5.1}
$$

Let $v=T_eu, w=T_fu$. Define a fourth field $z$ by

$$
 \tanh\!\left(\frac{\beta(z-u)}4\right)
   =\frac{e+f}{e-f}\tanh\!\left(\frac{\beta(v-w)}4\right).     \tag{5.2}
$$

Here is a direct algebraic verification, including the choice of formal branch. Put

$$
 U=e^{\beta u/2},\quad V=e^{\beta v/2},\quad W=e^{\beta w/2},
 \quad Z=U\frac{eV-fW}{eW-fV},
 \quad H=\frac{(e^2-f^2)VW}{(eV-fW)(eW-fV)}.         \tag{5.3}
$$

The logarithmic derivatives of $Z$ with respect to $U,V,W$ are $1,H,-H$; therefore $D_\pm z=D_\pm u+H(D_\pm v-D_\pm w)$. Write

$$
 A(X,Y)=\tfrac12(X/Y-Y/X),\qquad
 C(X,Y)=\tfrac12(XY-(XY)^{-1}).
$$

Substitution of (5.3), followed by multiplication by its denominators, proves the four rational identities

$$
\begin{aligned}
 A(U,V)/e+H\{A(U,V)/e-A(U,W)/f\}&=A(V,Z)/f,\\
 A(U,W)/f+H\{A(U,V)/e-A(U,W)/f\}&=A(W,Z)/e,\\
 eC(U,V)-H\{eC(U,V)-fC(U,W)\}&=-fC(V,Z),\\
 fC(U,W)-H\{eC(U,V)-fC(U,W)\}&=-eC(W,Z).
\end{aligned}                                                     \tag{5.4}
$$

Together with (5.1), these give exactly the sewing equations on the edges $(v,z;f)$ and $(w,z;e)$. These are polynomial identities after clearing denominators; `checks.py` independently verifies all four.

There is no division by a nonunit $e-f$ in the resulting formal transformation. Since $v,w$ arise from the **same** formal map, write

$$
 V=U+eA_0(e),\qquad W=U+fA_0(f).
$$

The common series $A_0$ has coefficients in the local jet algebra extended by $U$. Then

$$
 eW-fV=(e-f)\left[U-ef\frac{A_0(e)-A_0(f)}{e-f}\right].       \tag{5.5}
$$

The divided difference in brackets is a genuine bivariate power series, and the bracket has invertible constant term $U$. The numerator $eV-fW$ is divisible by $e-f$ for the same reason. Cancel these factors and take the formal logarithm of $Z/U$. This defines $z\in\mathcal A[[e,f]]$ with $z|_{f=0}=v$ and $z|_{e=0}=w$.

By the uniqueness established in (3.2), the two new edges identify this $z$ with both $T_fT_eu$ and $T_eT_fu$; their time derivatives agree as well. Thus

$$
 T_fT_e=T_eT_f.                                      \tag{5.6}
$$

For $\kappa<0$ the calculation may be made with complex $\beta$; all final field identities are real because their power-series coefficients depend on $\beta^2$. At $\kappa=0$, (5.2) has the limit $z-u=(e+f)(v-w)/(e-f)$; the same divisibility and uniqueness argument applies. Alternatively every coefficient identity above extends to $\kappa=0$ by its analytic dependence on $\kappa$.

## 6. The charges are the actual Hamiltonian generators

Spatial canonicity alone would be insufficient. All identities of variational forms in this section are understood coefficientwise in the formal parameters. On the **equal-time** Cauchy phase space, take

$$
 F_\epsilon[u,v]=\int\bigl(u v_x+P_\epsilon(u,v)\bigr)dx.
$$

Its variational derivatives, using (2.2), are

$$
 \frac{\delta F_\epsilon}{\delta u}=v_x-B_v=p,
 \qquad
 \frac{\delta F_\epsilon}{\delta v}=-u_x-B_u=-P,
 \qquad P=v_t.                                      \tag{6.1}
$$

Thus the already constructed $T_\epsilon$ is a canonical transformation for $\Omega=\int\delta u\wedge\delta p\,dx$. Equation (6.1) is obtained from the sewing equations themselves, rather than imposed as an extra assumption.

There is also the explicit fixed-endpoint identity

$$
 \epsilon\,\partial_\epsilon F_\epsilon[u,v]
       =-\int B_\epsilon(u,v)\,dx.                  \tag{6.2}
$$

For completeness, the parameter-generator relation needs a small differential-geometric argument. Set

$$
 W_\epsilon=(DT_\epsilon)^{-1}\partial_\epsilon T_\epsilon,
 \quad g_\epsilon=(\partial_\epsilon F_\epsilon)(u,T_\epsilon u),
 \quad \theta=\int p\,\delta u\,dx,
 \quad d\theta=-\Omega.
$$

At fixed parameter, (6.1) gives $d(F_\epsilon\circ\mathrm{graph}\,T_\epsilon)=\theta-T_\epsilon^*\theta$. Write $V_\epsilon=(\partial_\epsilon T_\epsilon)\circ T_\epsilon^{-1}$ for the velocity at the target. Differentiating this identity in $\epsilon$ and using Cartan's formula gives

$$
 d\left(g_\epsilon-T_\epsilon^*(\iota_{V_\epsilon}\theta)\right)
 =T_\epsilon^*(\iota_{V_\epsilon}\Omega)
       -d\left(T_\epsilon^*(\iota_{V_\epsilon}\theta)\right).
$$

The last terms cancel, so $\iota_{W_\epsilon}\Omega=dg_\epsilon$. Equations (6.2) and (4.1) identify the generator exactly:

$$
 W_\epsilon=X_{K_\epsilon},\qquad
 K_\epsilon=-\frac{I(\epsilon)}\epsilon,
 \qquad I(\epsilon)=\int B_\epsilon(u,T_\epsilon u)\,dx.
                                                               \tag{6.3}
$$

This is the spectrality calculation needed here. The broader generating-function viewpoint is discussed in [Kuznetsov–Sklyanin, *Few remarks on Bäcklund transformations for many-body systems*](https://arxiv.org/abs/solv-int/9711010); the particular identity (6.2) is verified directly above.

It remains to pass from commuting finite maps to commuting generators; this is not automatic without the parameter derivative in (6.3). Let $A_\epsilon=T_\epsilon^*$ act on local functions. The source velocity satisfies

$$
 \mathcal L_{W_\epsilon}=(\partial_\epsilon A_\epsilon)A_\epsilon^{-1}.
$$

Equation (5.6) implies $A_eA_f=A_fA_e$. Differentiating once in either parameter and once in both gives commutation of $A_e,A_f,\partial_eA_e,\partial_fA_f$ across the two parameters. Their inverses commute too. Consequently

$$
 [\mathcal L_{W_e},\mathcal L_{W_f}]=0,
 \quad [X_{K_e},X_{K_f}]=0,
 \quad X_{\{K_e,K_f\}}=0.                           \tag{6.4}
$$

For the canonical bracket (1.3), the last equality says both variational derivatives of the bracket vanish. Hence it is a constant functional on the connected neighbourhood under consideration. Each $K_\epsilon$ has zero first variation at the vacuum: $T_\epsilon$ preserves zero, and $B_\epsilon$ starts quadratically. The bracket evaluated there is zero. Therefore $\{K_e,K_f\}=0$, and coefficient extraction in (6.3) proves

$$
 \{I_n,I_m\}=0\quad\text{for all }m,n\ge1.          \tag{6.5}
$$

This proof uses the explicitly nondegenerate canonical bracket of this scalar theory. It makes no assertion that all brackets for other field theories lack Casimirs.

## 7. Nontriviality and functional independence

Neither a recursion nor increasing formal jet order alone proves this part. We compute the quadratic terms and exhibit a nonzero Jacobian.

At the vacuum, put $D=D_x$, $a=1+\epsilon^2M/4$, and $b=1-\epsilon^2M/4$. Linearizing the two sewing equations and eliminating $P$ gives

$$
 \binom{v}{P}
 =\frac1{a-\epsilon D}
   \begin{pmatrix}b&-\epsilon\\ \epsilon(M-D^2)&b\end{pmatrix}
   \binom{u}{p}.                                     \tag{7.1}
$$

Here the inverse is the well-defined formal inverse of $1+O(\epsilon)$. Restrict the quadratic charge to the subspace $u=0$. Then $v=-\epsilon(a-\epsilon D)^{-1}p$, so

$$
 I(\epsilon)^{(2)}\big|_{u=0}
 =\frac{\epsilon a}{2}\int
       p\,(a^2-\epsilon^2D^2)^{-1}p\,dx.            \tag{7.2}
$$

Consequently, for every $j\ge0$,

$$
 I_{2j+1}^{(2)}\big|_{u=0}=\frac12\int p\,P_j(D^2)p\,dx,
 \qquad P_j(z)=z^j+\text{terms of lower degree}.     \tag{7.3}
$$

To see the leading coefficient, expand the right side of (7.2) as

$$
 \frac\epsilon2\sum_{k\ge0}\epsilon^{2k}a^{-2k-1}
            \int pD^{2k}p\,dx.
$$

At order $\epsilon^{2j+1}$, only $k=j$ contributes degree $j$ in $D^2$, and its coefficient is one. In particular the highest term in (7.3) is $(-1)^j\int(D^jp)^2dx/2$, not a spatial divergence.

Choose $N$ distinct positive integer wavenumbers $k_1,\ldots,k_N$ on a $2\pi$-periodic circle and restrict further to

$$
 u=0,\qquad p=\sum_{\ell=1}^N c_\ell\cos(k_\ell x).
$$

The quadratic parts of $I_{2j+1}$, $j=0,\ldots,N-1$, are

$$
 \frac\pi2\sum_{\ell=1}^N c_\ell^2P_j(-k_\ell^2).
$$

The matrix $(P_j(-k_\ell^2))$ is invertible: changing from the monic degree-$j$ polynomials $P_j$ to monomials is triangular with unit diagonal, and the monomial evaluation matrix is Vandermonde at distinct points. The formal substitution is odd under $(u,p)\mapsto(-u,-p)$, by uniqueness of (3.2); hence the charges are even. Their restricted Jacobian at $c_\ell=\delta\ne0$ has determinant

$$
 (\pi\delta)^N\det(P_j(-k_\ell^2))+O(\delta^{N+2}),
$$

which is nonzero for sufficiently small nonzero $\delta$. A restriction with independent differentials implies independence on the full phase space. Continuity gives an open set of independence around these points. This proves every finite-subfamily assertion in Theorem S and completes its proof.

## 8. What survives in the general spatial Hamilton–Jacobi argument

The following establishes a useful general result, but it does not by itself establish an integrable hierarchy.

For a finite-order local Lagrangian, write $u_{a,k}=D_t^aD_x^ku$ and suppose the maximal spatial order is $K$. To keep the Legendre inversion local, suppose the Lagrangian contains no $u_{a,K}$ with $a>0$, and that its Hessian in $u_{0,K}$ is invertible. All formulas below also apply componentwise to several fields. Define

$$
 F_k=\sum_a(-D_t)^a\frac{\partial L}{\partial u_{a,k}},
 \quad E(L)=\sum_{k=0}^K(-D_x)^kF_k,
 \quad
 \pi_m=\sum_{j=0}^{K-1-m}(-D_x)^jF_{m+j+1}.        \tag{8.1}
$$

An explicit integration by parts first in $t$, then in $x$, gives for any variation $\eta$

$$
 \delta_\eta L
 =E(L)\eta+D_x\left(\sum_{m=0}^{K-1}\pi_mD_x^m\eta\right)
    +D_t\Xi_\eta.                                  \tag{8.2}
$$

For example, the time integration of a term $A D_t^aD_x^k\eta$ has boundary term

$$
 \sum_{b=0}^{a-1}(-D_t)^bA\;D_t^{a-1-b}D_x^k\eta,
$$

which specifies $\Xi_\eta$ without appealing to an unspecified improved current. Set $q_m=D_x^mu$. In (8.2), put $\eta=D_xu$, so $\delta_\eta L=D_xL$. It follows that

$$
 D_x\mathcal H^{(x)}+D_t\Xi_{D_xu}=-E(L)D_xu,
 \qquad
 \mathcal H^{(x)}=\sum_{m=0}^{K-1}\pi_mq_{m+1}-L.  \tag{8.3}
$$

Thus the Noether representative actually produced by this specified integration by parts has momentum flux $T^{11}=-\mathcal H^{(x)}$ and density $T^{01}=-\Xi_{D_xu}$. This **derives** the Legendre–Noether identification in that representative. It does not assume it as `h_T1_1`, nor infer an improvement merely because two currents happen to be conserved on shell.

The spatial Hamilton equations can also be checked directly. Eliminate $v=q_K$ using $\pi_{K-1}=F_K=\partial L/\partial v$, and let

$$
 H=\int\left(\sum_{m=0}^{K-2}\pi_mq_{m+1}+\pi_{K-1}v-L\right)dt.
$$

Its functional derivatives give $D_xq_m=q_{m+1}$ for $m<K-1$, $D_xq_{K-1}=v$, and

$$
 D_x\pi_0=F_0,\qquad D_x\pi_m=F_m-\pi_{m-1}\quad(1\le m<K). \tag{8.4}
$$

Derivatives of the eliminated $v$ cancel because $\pi_{K-1}=\partial L/\partial v$. Equations (8.4) reproduce the recursion in (8.1); its remaining equation is precisely $E(L)=0$. Conversely (8.1) and $E(L)=0$ give (8.4). This is the Hamilton–Euler–Lagrange equivalence under the stated regularity assumptions.

Now suppose a defect functional $S_d[q,Q]$, with no unresolved auxiliary variables, generates a **strong Lagrangian** sewing submanifold

$$
 \pi=-\delta_qS_d,\qquad\Pi=\delta_QS_d
$$

in the product of the two spatial phase spaces. In a formal cotangent setting its tangent vectors have the form $(a,-S_{qq}a-S_{qQ}b;b,S_{Qq}a+S_{QQ}b)$. Self-adjointness of the variational Hessian shows both isotropy and, by pairing against arbitrary $a,b$, equality of the symplectic orthogonal with this tangent space. In a topological function space the same conclusion needs the corresponding duality and closed-range conditions; it must not be inferred just by finite-dimensional counting.

The off-shell momentum balance in the representative (8.3) gives

$$
 \mathcal H_-^{(x)}-\mathcal H_+^{(x)}=-D_tP_d,
$$

so the difference of spatial Hamiltonian functionals is constant on the sewing manifold, with temporal boundary conditions that discard this boundary term, or in the formal quotient by $D_t$. Its differential vanishes on the tangent space. Since

$$
 \iota_{(X_{H_-},X_{H_+})}(\Omega_- -\Omega_+)=d(H_- -H_+),
$$

the Hamiltonian pair lies in the symplectic orthogonal, hence in the tangent space. This proves spatial invariance. If the correspondence projects invertibly to either side, it intertwines the spatial evolutions.

Auxiliary variables can enter this argument only after an actual reduction: a local solution of $\delta_\lambda S_d=0$, or an appropriate constrained symplectic treatment. An invertible differential operator in the auxiliary Hessian need not have a **local** inverse. The above argument does not settle arbitrary Type-II reduction.

Finally, the step $D_tR=0\Rightarrow R=0$ is valid for an actual residual $R(t,x)$ whose limit at one temporal end is zero. It is false on the whole differential algebra, since $D_t1=0$. A correct normalization hypothesis applies to the particular residuals $R=D_xE_d+\Delta T^{00}$ and $R=D_xP_d+\Delta T^{01}$. The scalar proof avoided this issue altogether by deriving (4.1) directly.

## 9. A correct Gardner argument for KdV

This section repairs a specific failed example in the response. It is an independent derivation for KdV, not a proof that an arbitrary defect must produce the Gardner map.

For $u_t+u_{xxx}+6uu_x=0$, take

$$
 u=w+\epsilon w_x-\epsilon^2w^2.                    \tag{9.1}
$$

The exact differential identity is

$$
 u_t+u_{xxx}+6uu_x
 =(1+\epsilon D_x-2\epsilon^2w)
   \left[w_t+D_x(w_{xx}+3w^2-2\epsilon^2w^3)\right]. \tag{9.2}
$$

The formal inverse $w=\sum_{n\ge0}\epsilon^nw_n$ exists with

$$
 w_0=u,\qquad
 w_n=-D_xw_{n-1}+\sum_{i+j=n-2}w_iw_j.              \tag{9.3}
$$

Since $1+\epsilon D_x-2\epsilon^2w=1+O(\epsilon)$ has a formal inverse, (9.2) proves that $w$ itself is a generating **density**. The first coefficients are

$$
\begin{aligned}
 w_1&=-u_x,\\
 w_2&=u_{xx}+u^2,\\
 w_3&=-u_{xxx}-4uu_x,\\
 w_4&=u_{xxxx}+6uu_{xx}+5u_x^2+2u^3
       \equiv -u_x^2+2u^3\pmod{D_x\mathcal A}.
\end{aligned}
$$

The even coefficients yield independent charges. Indeed, integrating (9.1) gives $\int w=\int u+\epsilon^2\int w^2$. The linear part of $w$ is $(1+\epsilon D_x)^{-1}u$, so the quadratic part of $\int w$ is

$$
 \epsilon^2\int u(1-\epsilon^2D_x^2)^{-1}u\,dx.
$$

Thus $\int w_{2n}$ has quadratic part $(-1)^{n-1}\int(D_x^{n-1}u)^2dx$, for $n\ge1$. The same finite Fourier-mode Vandermonde argument as in Section 7 proves functional independence; possible cubic and higher terms do not change its leading Jacobian.

Involution can be proved without an assumption excluding Casimirs. Let

$$
 R_\epsilon=\frac{\delta\int w\,dx}{\delta u},\qquad
 (1-\epsilon D_x-2\epsilon^2w)R_\epsilon=1.          \tag{9.4}
$$

The second identity follows by taking the adjoint of the linearization of (9.1). Put $r=1/(2\epsilon)-\epsilon w$. Then

$$
 (R_\epsilon)_x=2rR_\epsilon-1/\epsilon,\qquad
 r_x+r^2=1/(4\epsilon^2)-u.
$$

Differentiating the first identity twice more gives

$$
 (D_x^3+4uD_x+2u_x)R_\epsilon=\epsilon^{-2}D_xR_\epsilon. \tag{9.5}
$$

Both $J_0=D_x$ and $J_1=D_x^3+4uD_x+2u_x$ are skew-adjoint. Therefore, for the first KdV bracket,

$$
 B(e,f):=\int R_eJ_0R_f\,dx
 =f^2\int R_eJ_1R_f\,dx
 =\frac{f^2}{e^2}\int R_eJ_0R_f\,dx.
$$

Multiplying by $e^2$ gives $(e^2-f^2)B(e,f)=0$. Multiplication by this nonzero scalar polynomial is injective on bivariate formal series with coefficients in the real vector space of local functionals, hence $B=0$. Every coefficient charge is in involution. This derivation uses the actual density $w$. Expanding a density difference already known to equal $D_xP_d$ would instead give zero charges and cannot replace it.

## 10. Verification scope and the unresolved part of Theorem D

The mathematical proof of Theorem S is Sections 2–7, not a finite symbolic experiment. The accompanying checks test identities and signs which are useful sources of mistakes:

- `checks.py`: all four Bianchi edge identities, the defect momentum/current identities, the fixed-endpoint parameter derivative, the Gardner differential identity, the Lenard identity, and linearized equal-time symplecticity.
- `scalar_checks.py`: construction of the first five nonlinear scalar coefficients in the actual on-shell jet algebra, their conservation laws, the triviality of the second density, and vanishing Euler derivatives of the $\{I_3,I_5\}$ bracket density. Jet buffers are guarded against silent truncation.
- `lean/DefectCore.lean`: generic differential-ring identities for first-order Noether currents, $K=2$ spatial integration by parts and the Legendre–Noether identity, correctly restricted normalization, scalar current identities, and the NLS number current.
- `lean/DualModel.lean`: an explicit nonzero commutative ring with a nonzero derivation and a satisfiable restricted normalization condition. This is a consistency witness, not a model of the full PDE jet algebra.

The Lean files do **not** formalize the all-orders scalar theorem, its variational phase spaces, or Bianchi permutability. They contain no claim of a complete formalization. In particular, the general Hamilton–Euler–Lagrange equivalence in Section 8 is a written proof, not a Lean theorem in these files.

What remains open in the proposed general theorem is the implication from a general momentum-preserving defect to the additional structures used explicitly here: an appropriate parameter family, local solvability of the full sewing equations after auxiliary reduction, a genuine density, equal-time canonicity and spectrality, permutability, and independent charge symbols. The scalar proof derives those structures using the special constraint (2.3); the general spatial Hamilton–Jacobi argument does not derive them. No conclusion for arbitrary Type-II systems, NLS defects, mKdV defects, Boussinesq defects, or general multicomponent potentials follows from this manuscript alone.

Accordingly, the unconditional, fully general version of Theorem D is still **not established**. The result established here is a complete formal local integrability theorem in the scalar Type-I class, together with a precise general spatial statement and a corrected KdV construction.
