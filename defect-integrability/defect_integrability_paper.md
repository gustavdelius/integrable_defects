# Momentum-Conserving Type-I Defects and Local Integrability near a Massive Vacuum

Corrected version, 19 October 2026. **Status:** complete written argument under the hypotheses of Theorem 2.1, submitted for independent mathematical review. The unrestricted defect-integrability conjecture remains open.

## Abstract

We prove a structural implication from momentum conservation at a Type-I defect to local integrability of a multicomponent relativistic bulk field theory. The bulk potential is real analytic near a positive-mass vacuum and irreducible under orthogonal splitting. The defect has a specified constant first-order kinetic coupling, a derivative-free momentum correction satisfying a strong local balance identity, and a nondegenerate transparent critical manifold. Momentum conservation forces the defect potential to split into two functions and supplies a reciprocal rescaling family. We construct its unique local formal Bäcklund branch, prove equal-time canonicity, and identify the defect-energy coefficients as the Hamiltonians of its parameter velocity. A rigidity lemma shows that a vacuum-normalized analytic local conserved functional near a massive vacuum is determined by its quadratic part. The explicitly commuting quadratic generators therefore yield an infinite hierarchy in involution. A Fourier Jacobian proves functional independence of arbitrarily large finite subfamilies, and formal Bianchi permutability follows. The proof leaves the bulk potential unspecified and uses no classification or Lax representation. We also exhibit a reducible free-field defect family that fails to commute, and explain why the transparent-limit assumptions exclude genuinely different bulk theories on the two sides.

## 1. Introduction

A point defect breaks spatial translation invariance, so a local correction restoring total momentum imposes a substantial constraint. In classical scalar and affine Toda models, this constraint is closely related to Bäcklund sewing equations. The early defect constructions of Bowcock, Corrigan and Zambon demonstrate this relationship in concrete field theories [1](https://arxiv.org/abs/hep-th/0305022), [2](https://arxiv.org/abs/hep-th/0401020). Bristow and Bowcock establish a momentum condition for a class of Type-II defects whose equations extend to Bäcklund transformations [3](https://arxiv.org/abs/1612.03002). These results motivate the broader question: when does the existence of a momentum-conserving defect force integrability of the bulk equation?

A structural answer must establish several logically distinct properties. Compatibility of the sewing equations with bulk evolution does not by itself give a local parameter family. A parameter expansion does not by itself give independent charges. Nor does spatial canonicity establish involution for the equal-time Poisson bracket. The coexistence of spatial and temporal Hamiltonian descriptions is central to the multisymplectic treatment of defects; Caudrelier and Kundu develop it for the nonlinear Schrödinger model [4](https://arxiv.org/abs/1411.0418).

Here these steps are proved for normalized constant Type-I auto-defects near a massive analytic vacuum. The main mechanism is

$$
 \text{momentum identity}
 \ \Longrightarrow\ \text{local canonical parameter family}
 \ \Longrightarrow\ \text{commuting quadratic generators}
 \ \Longrightarrow\ \text{commuting local charges}.
$$

The last implication uses a property of massive local conservation laws. A homogeneous polynomial conserved functional of free massive fields cannot have degree greater than two unless it is a spatial derivative. Expanding a vacuum-normalized analytic nonlinear conserved functional by amplitude then shows that its quadratic part determines it. We apply this statement to Poisson brackets of the defect-generated charges.

The result concerns an infinite commuting hierarchy for the homogeneous **bulk** theory admitting the defect. It does not establish global Bäcklund maps, convergence of their parameter expansion, or a complete Hamiltonian integrability theory for the system with a fixed point defect. The hypotheses are given in Section 2, the proof in Sections 3–8, and examples in Sections 9–10. Section 11 addresses different bulk theories and the remaining restrictions. Appendix A gives the spatial Hamilton–Jacobi interpretation under explicit geometric assumptions.

## 2. Hypotheses and main theorem

Let $u(x,t)\in\mathbb R^r$ have Lagrangian and equation

$$
 L=\frac12|u_t|^2-\frac12|u_x|^2-U(u),\qquad
 u_{tt}-u_{xx}+U'(u)=0.                                      \tag{2.1}
$$

Let $v$ denote the field on the right of the defect, with the same number of components. Write

$$
 q=\frac{u-v}{2},\qquad w=\frac{D^Tu+Dv}{2},\qquad D=I-E,
 \quad E^T=-E.
$$

These are independent coordinates on the endpoint fields; their inverse is given in (3.3). Assume the following.

1. **Analytic massive vacuum.** $U$ is real analytic near $0$, with $U(0)=0$, $U'(0)=0$, and $M=U''(0)$ positive definite.
2. **Bulk irreducibility.** There is no nontrivial orthogonal splitting $\mathbb R^r=V_1\oplus V_2$ on which the germ of $U$ is a sum $U_1(u_1)+U_2(u_2)$. This is irreducibility of the bulk potential, not merely of the combined bulk and defect.
3. **Normalized constant Type-I coupling.** The auto-defect joins two copies of (2.1), has no auxiliary fields, and has action density
   $$
   L_d=\frac12u^TEu_t+u^TDv_t+\frac12v^TEv_t-B(u,v),
   \quad E^T=-E,\quad D=I-E.                                \tag{2.2}
   $$
   $B$ is analytic. There is a derivative-free defect momentum $P_d(u,v)$ satisfying the strong momentum identity: after substituting the sewing equations, the identity holds for independent values of $u,v,u_t,v_t$.
4. **Transparent nondegenerate critical manifold.** Regard $B$ as a function of the independent coordinates $(w,q)$. Assume $B_q(w,0)=0$ for all $w$ near zero and $G=B_{qq}(0,0)$ is invertible. Section 3 derives $B=f(w)+g(q)$ from momentum conservation. Thus this hypothesis is exactly $g'(0)=0$, $g''(0)=G$ in those coordinates. Additive constants are fixed by vacuum normalization.

The word “normalized” in hypothesis 3 is substantive: the same right-field coordinates are used for the auto-potential and the transparent diagonal. We do not assert that every possible Type-I defect can be put in this form while preserving both identifications.

**Theorem 2.1 (structural local integrability).** Under hypotheses 1–4, the momentum identity supplies a rescaled family of defects with a unique formal local branch $T_\epsilon=\mathrm{Id}+O(\epsilon)$. Its defect energy has an expansion

$$
 I(\epsilon)=\int B_\epsilon(u,T_\epsilon u)\,dx
            =\sum_{n\geq1}\epsilon^n I_n.                    \tag{2.3}
$$

Each $I_n$ is an analytic finite-jet local conserved functional. All $I_n$ Poisson commute for the canonical equal-time bracket. Infinitely many are functionally independent: for every $N$ there are $N$ members whose differentials are independent at arbitrarily small periodic Cauchy data. The formal maps $T_\epsilon$ commute for different parameters.

The same conclusion holds without hypothesis 2 if $G$ in hypothesis 4 is assumed to be a nonzero scalar matrix. Bulk irreducibility is used precisely to derive this scalar condition.

The conclusion concerns the homogeneous bulk equation (2.1). It does not assert that every charge admits a local correction at a fixed point defect. Local integrability here means the stated infinite commuting hierarchy and finite-subfamily independence; no completeness of action variables or convergence of the parameter series is claimed.

We use local functionals modulo $x$-derivatives, with no explicit $x,t$ dependence. Their densities are analytic in finitely many Cauchy jets $(u,p,u_x,p_x,\ldots)$ near the zero jet, where $p=u_t$. Integrals may be evaluated on small smooth periodic data or rapidly decreasing data. The proof of a local identity can be tested on the line before applying it on a circle. Set

$$
 \Omega=\int\delta u^T\wedge\delta p\,dx,\qquad
 \{F,H\}=\int(F_u^TH_p-F_p^TH_u)\,dx,
 \quad \iota_{X_F}\Omega=dF.                                \tag{2.4}
$$

Subscripts on functionals mean variational derivatives. Constants are fixed by evaluation at the zero field. The bulk Hamiltonian is

$$
 H=\int\left(\frac12|p|^2+\frac12|u_x|^2+U(u)\right)dx.     \tag{2.5}
$$

All operations with the Bäcklund parameter are coefficientwise. Each coefficient has finite differential order, although that order need not be bounded uniformly over the hierarchy. The proof of Theorem 2.1 occupies Sections 3–8.

## 3. Momentum constraints and the parameter family

**Proposition 3.1 (split momentum identity).** Under hypothesis 3, the sewing equations and momentum balance imply the splitting and potential identity (3.4).

**Proof.** Variation of (2.2) gives the sewing equations

$$
 u_x=Eu_t+Dv_t-B_u,\qquad
 v_x=D^Tu_t-Ev_t+B_v.                                      \tag{3.1}
$$

Choose physical bulk momentum $-\int p^Tu_x\,dx$. Its defect balance requires

$$
 D_tP_d=T^{11}(u)-T^{11}(v),\qquad
 T^{11}(u)=\frac12(|u_t|^2+|u_x|^2)-U(u).
$$

The quadratic velocity terms cancel because $DD^T=I-E^2$ and $ED=DE$. The linear and constant terms give

$$
 (P_d)_u=EB_u-DB_v,\quad
 (P_d)_v=-D^TB_u-EB_v,\quad
 \frac12(|B_u|^2-|B_v|^2)=U(u)-U(v).                        \tag{3.2}
$$

Introduce independent coordinates

$$
 q=\frac{u-v}{2},\quad
 w=\frac{D^Tu+Dv}{2},\qquad
 u=w+Dq,\quad v=w-D^Tq.                                    \tag{3.3}
$$

The first two identities in (3.2) become $(P_d)_w=-B_w$ and $(P_d)_q=B_q$. Equality of mixed derivatives implies $B_{wq}=0$. Consequently, locally,

$$
 B=f(w)+g(q),\qquad P_d=-f(w)+g(q),
$$

and the last identity in (3.2) is exactly

$$
 U(w+Dq)-U(w-D^Tq)=\frac12 f'(w)^Tg'(q).                   \tag{3.4}
$$

Conversely, the splitting and (3.4) imply all of (3.2), so they are sufficient for the strong momentum identity. $\square$

The split potential is therefore a consequence of momentum conservation. Its functional form remains unspecified. The coefficient calculation, including all velocity terms for a general three-component skew matrix, is checked in `textbook_code/defect_integrability_structural/paper_checks.py`.

**Proposition 3.2 (scalar Hessian and rescaling).** Under hypotheses 1–4, the defect admits the normalized family (3.7)–(3.8), and its kinetic matrix commutes with the bulk mass matrix.

**Proof.** Differentiate (3.4) in $q$ at zero. Since $D+D^T=2I$,

$$
 Gf'(w)=4U'(w).                                            \tag{3.5}
$$

Both $G$ and $f''$ are symmetric. Differentiating (3.5) and transposing shows

$$
 [G,U''(w)]=0\quad\hbox{for every }w.                      \tag{3.6}
$$

Diagonalize $G$ orthogonally. Equation (3.6) says every mixed second derivative of $U$ between distinct eigenspaces vanishes. Integrating this statement near zero splits $U$ as a sum of potentials on those eigenspaces; $U'(0)=0$ removes any issue with linear terms. Bulk irreducibility therefore forces $G=\gamma I$, $\gamma\ne0$.

Normalize $f(0)=g(0)=0$. Then $f=4U/\gamma$. Multiplying $f$ by a nonzero parameter $\lambda$ and $g$ by $\lambda^{-1}$ preserves (3.4). Put $\epsilon=4\lambda/\gamma$ and replace $g$ by $4g/\gamma$. The family becomes

$$
 B_\epsilon=\epsilon U(w)+\epsilon^{-1}g(q),\qquad
 P_\epsilon=-\epsilon U(w)+\epsilon^{-1}g(q),              \tag{3.7}
$$

where, from now on,

$$
 g(0)=0,\quad g'(0)=0,\quad g''(0)=4I,\qquad
 U(w+Dq)-U(w-D^Tq)=\tfrac12 U'(w)^Tg'(q).                 \tag{3.8}
$$

Thus a parameter family is derived within this class. No claim about an arbitrary symmetry producing a spectral family is needed.

There is one further consequence needed later. Put $w=0$ in (3.8) and compare quadratic terms in $q$. This gives

$$
 D^TMD=DMD^T,\qquad [E,M]=0.                              \tag{3.9}
$$

The second equality follows by expanding the first: its difference is $2(EM-ME)$. $\square$

## 4. A local formal branch satisfying both sewing equations

**Proposition 4.1 (formal Bäcklund substitution).** The family (3.7) has a unique local formal branch fixing the vacuum and approaching the identity. This branch satisfies both sewing equations and intertwines the bulk evolution.

**Proof.** Write $D_\pm=D_t\pm D_x$, with $D_t$ acting on Cauchy jets by

$$
 D_tu=p,\qquad D_tp=u_{xx}-U'(u),\qquad [D_t,D_x]=0.
$$

Equations (3.1) become

$$
 D_+q=-\frac\epsilon2U'(w),\qquad
 D_-w=\frac1{2\epsilon}g'(q).                             \tag{4.1}
$$

Since $w=u-Dq$, the second equation is

$$
 g'(q)=2\epsilon D_-u-2\epsilon D D_-q.                   \tag{4.2}
$$

Set $q=\sum_{n\geq1}\epsilon^n q_n$. The linear part of $g'$ is $4q$. At order $n$, the right side uses only $q_1,\ldots,q_{n-1}$, as do the nonlinear terms of $g'(q)$. Division by $4$ determines $q_n$ uniquely. Each coefficient is an analytic function of finitely many Cauchy jets. In particular,

$$
 q_1=\tfrac12(p-u_x),\quad
 v=u-2q=u+\epsilon(u_x-p)+O(\epsilon^2).                  \tag{4.3}
$$

To verify the first equation as well, define

$$
 A=D_+q+\tfrac\epsilon2U'(w).
$$

Differentiating (3.8) in $w,q$ and solving the resulting two linear identities for $U'(u)$ gives

$$
 U'(u)=\tfrac14\{g''(q)U'(w)+D U''(w)g'(q)\}.            \tag{4.4}
$$

Use (4.2) to differentiate $u=w+Dq$. Direct substitution yields

$$
 D_+D_-u+U'(u)
   =\left(D D_-+\frac1{2\epsilon}g''(q)\right)A.           \tag{4.5}
$$

The left side vanishes on the bulk equation. The operator on the right has leading Laurent coefficient $2\epsilon^{-1}I$. If $A$ had a first nonzero coefficient $\epsilon^a A_a$, the lowest term of the right side would be $2\epsilon^{a-1}A_a$, a contradiction. Thus $A=0$ coefficientwise. The other combination of the differentiated potential identity is

$$
 U'(v)=\tfrac14\{g''(q)U'(w)-D^TU''(w)g'(q)\}.
$$

Differentiating $v=w-D^Tq$ using (4.1) gives the negative of this expression for $D_+D_-v$. Hence $v$ satisfies the same bulk equation.

Consequently

$$
 T_\epsilon:(u,p)\longmapsto(v,D_tv)
$$

is a local formal substitution, intertwines the bulk evolution, fixes the zero solution, and has a unique formal inverse. The argument only compares Laurent coefficients bounded below. It uses the invertible pole $2\epsilon^{-1}I$, without any assumption that $D_t$ is injective. $\square$

## 5. Conserved energy coefficients and equal-time canonicity

**Proposition 5.1 (current and equal-time generator).** The coefficients in (2.3) are local conserved functionals. The map $T_\epsilon$ is canonical for (2.4), and its source parameter velocity has Hamiltonian $-I(\epsilon)/\epsilon$.

**Proof.** The full sewing equations imply the current identity directly:

$$
 D_tB_\epsilon+D_xP_\epsilon
 =\epsilon U'(w)^TD_-w+\epsilon^{-1}g'(q)^TD_+q=0.          \tag{5.1}
$$

On the branch $q=O(\epsilon)$, both densities are $O(\epsilon)$. Therefore (2.3) defines local conserved charges at every order. The first is

$$
 I_1=\int\left\{\tfrac12|p-u_x|^2+U(u)\right\}dx.        \tag{5.2}
$$

Now form a functional on two independent equal-time endpoint fields:

$$
 F_\epsilon[u,v]=\int\{2q^Tw_x+P_\epsilon(w,q)\}\,dx.    \tag{5.3}
$$

The kinetic term is equivalent modulo an $x$-derivative to
$\frac12u^TEu_x+u^TDv_x+\frac12v^TEv_x$.
Its variation in $(w,q)$ is

$$
 \delta F_\epsilon=\int\left[
 (-2q_x-\epsilon U'(w))^T\delta w
 +(2w_x+\epsilon^{-1}g'(q))^T\delta q\right]dx.            \tag{5.4}
$$

On (4.1), the two coefficients are $p-P$ and $D^Tp+DP$, respectively, where $P=v_t$. By (3.3),

$$
 \delta F_\epsilon=\int(p^T\delta u-P^T\delta v)dx.        \tag{5.5}
$$

Taking an exterior derivative of (5.5) on the graph gives $T_\epsilon^*\Omega=\Omega$. Thus the transformation is canonical for the equal-time form (2.4). Appendix A describes the separate spatial symplectic interpretation.

At fixed endpoints,

$$
 \epsilon\partial_\epsilon F_\epsilon
             =-\int B_\epsilon\,dx.                      \tag{5.6}
$$

The source velocity $W_\epsilon=(DT_\epsilon)^{-1}\partial_\epsilon T_\epsilon$ therefore obeys

$$
 \iota_{W_\epsilon}\Omega=dK_\epsilon,\qquad
 K_\epsilon=-I(\epsilon)/\epsilon.                        \tag{5.7}
$$

To prove the parameter-generator identity with the convention (2.4), put $\theta=\int p^T\delta u\,dx$, so $d\theta=-\Omega$, and let $V=(\partial_\epsilon T)\circ T^{-1}$. Pulling (5.5) to the graph gives $d(F\circ\mathrm{graph}\,T)=\theta-T^*\theta$. Its parameter derivative is

$$
 d\{(\partial_\epsilon F)\circ\mathrm{graph}\,T
       -T^*(\iota_V\theta)\}
 =T^*(\iota_V\Omega)-dT^*(\iota_V\theta).
$$

Cancel the last exact terms and use $T^*\Omega=\Omega$. This proves (5.7). Thus the conserved coefficients are precisely the Hamiltonians of the parameter velocity. $\square$

Generating functions and differentiation in a Bäcklund parameter also feature in the Hamiltonian treatment of Kuznetsov–Sklyanin [5](https://arxiv.org/abs/solv-int/9711010). Here (5.6)–(5.7) are derived directly, without postulating a Lax spectrality relation.

## 6. Rigidity of local conserved functionals near a massive vacuum

The commutation argument rests on a rigidity property of analytic local conserved functionals. The positive masses make the free dispersion relation sufficiently restrictive to exclude a local conserved functional whose first nonzero amplitude degree exceeds two.

**Lemma 6.1 (free massive fields).** For finitely many real free Klein–Gordon fields with positive masses, a translation-invariant homogeneous polynomial local functional of degree $n\geq3$ conserved by the free evolution is zero modulo a spatial derivative. A conserved linear local functional is zero as well.

**Proof.** Diagonalize the positive mass matrix. For a species $a$ and real Fourier momentum $k$, write

$$
 \omega_a(k)=\sqrt{k^2+m_a^2},\qquad
 \widehat u_a=a_{a,+}+a_{a,-},\quad
 \widehat p_a=i\omega_a(a_{a,+}-a_{a,-}).                    \tag{6.1}
$$

Complexification and polarization let the amplitudes be treated independently. They evolve by $\dot a_{a,\sigma}=i\sigma\omega_a a_{a,\sigma}$. Polarize the homogeneous functional into a symmetric multilinear functional of $n$ independent Cauchy data. Translation invariance gives the factor $\delta(k_1+\cdots+k_n)$ in its Fourier kernel. Finite differential order makes each coefficient polynomial in the momenta before (6.1). After that invertible change of amplitudes, each species and sign component has a real-analytic coefficient $A(k_1,\ldots,k_n)$.

Conservation for arbitrary Fourier wave packets implies on the momentum hyperplane

$$
 \Phi A=0,\qquad
 \Phi=\sum_{j=1}^n\sigma_j\omega_{a_j}(k_j),\quad
 k_n=-\sum_{j<n}k_j.                                     \tag{6.2}
$$

For $n\geq3$, two of the independent variables are $k_1,k_2$, and

$$
 \frac{\partial^2\Phi}{\partial k_1\partial k_2}
 =\frac{\sigma_n m_{a_n}^2}
        {(k_n^2+m_{a_n}^2)^{3/2}}\ne0.                    \tag{6.3}
$$

Thus $\Phi$ cannot vanish identically on any open subset. Equation (6.2) forces $A=0$ on the complement of its zero set and hence everywhere by continuity. This does **not** deny the existence of resonant momenta. Locality rules out a kernel supported only on their lower-dimensional set.

Invert (6.1) at each momentum. Each original polynomial kernel vanishes on $\sum k_j=0$, so polynomial division by the monic linear polynomial $k_n+\sum_{j<n}k_j$ has zero remainder. Thus that kernel has this polynomial as a factor. The quotient can be symmetrized over identical arguments without changing the identity. In the polarized differential-polynomial representation, multiplication by $i\sum k_j$ is precisely a total $x$-derivative. This proves that the functional is zero modulo a derivative. At degree one, integration by parts leaves only $\int(a^Tu+b^Tp)dx$; conservation and invertibility of the mass matrix force $a=b=0$. $\square$

**Lemma 6.2 (injectivity of the quadratic part).** Let $H=\int\{\frac12|p|^2+\frac12|u_x|^2+U(u)\}dx$ satisfy hypothesis 1. An analytic finite-jet local conserved functional with zero constant, linear, and quadratic parts as a functional is zero. In particular, two normalized conserved functionals with no linear term and the same quadratic part coincide.

**Proof.** Expand by amplitude degree, assigning degree one to every Cauchy jet. Suppose the first nonzero homogeneous functional has degree $n\geq3$. At that degree, $\{F,H\}=0$ reads $\{F^{(n)},H^{(2)}\}=0$: all nonlinear terms of $H$ contribute at higher degree. Lemma 6.1 makes $F^{(n)}$ a spatial derivative, a contradiction. Equivalently, induction makes every homogeneous functional zero. This induction takes place modulo derivatives, so lower homogeneous densities that are nonzero derivatives cause no extra terms in a Poisson bracket.

For an analytic density involving a fixed finite number of jets, its Euler derivatives are analytic functions of finitely many jets. Their Taylor series vanish by the preceding argument; hence the Euler derivatives vanish near zero. Integrate the first variation along the scaling path $(u,p)\mapsto\lambda(u,p)$, $0\leq\lambda\leq1$. Integration by parts expresses it through those Euler derivatives, so the functional equals its vacuum value, which is zero. The same argument holds purely formally in amplitude. $\square$

Any analytic conserved functional has zero linear part as a functional: its degree-one conservation equation is the free conservation equation treated in Lemma 6.1. Thus the quadratic-part map is injective on vacuum-normalized analytic local conserved functionals. This statement concerns **local** functionals. Products such as $H^2$ are not local integrals. Positivity of the masses and analyticity are used in the two separate steps of the proof.

Local currents of the free Klein–Gordon equation have been studied by Gordon [6](https://doi.org/10.1017/S0305004100058965) and Opanasenko–Popovych [7](https://arxiv.org/abs/1810.12434). Lemma 6.1 gives the multicomponent, translation-invariant statement needed here with a direct proof.

## 7. Commutation to all orders

**Proposition 7.1 (involution and formal permutability).** All the charges $I_n$ Poisson commute, and $T_\epsilon T_\eta=T_\eta T_\epsilon$ as a bivariate formal substitution.

**Proof.** Linearize at zero. On Cauchy columns $z=(u,p)^T$, let

$$
 \mathcal L=
 \begin{pmatrix}-\partial_x I&I\\ \partial_x^2I-M&-\partial_xI\end{pmatrix}.
                                                               \tag{7.1}
$$

This represents $D_-$ on free Cauchy data. A constant field-space matrix acts diagonally on the two Cauchy components; hats for these diagonal lifts will be suppressed. Equation (3.9) ensures that $E,D,D^T$ all commute with $\mathcal L$.

The linearized second equation of (4.1) says $q=(\epsilon/2)D_-w$. Combining it with (3.3) gives the exact formal linearization

$$
 T_\epsilon^{\mathrm{lin}}
 =\left(I-\frac\epsilon2D^T\mathcal L\right)
  \left(I+\frac\epsilon2D\mathcal L\right)^{-1}.            \tag{7.2}
$$

All coefficients belong to the commutative algebra generated by $E,\mathcal L$. Thus its source velocities commute for different parameters. More explicitly, expansion and logarithmic differentiation of (7.2), followed by (5.7), give

$$
 X_{I_n^{(2)}}=C_n\mathcal L^n,\qquad
 C_n=2^{-n}\bigl((I+E)^n-(-1)^n(I-E)^n\bigr).              \tag{7.3}
$$

For any $n,m$, these constant-coefficient linear Hamiltonian vector fields commute. The quadratic functional $\{I_n^{(2)},I_m^{(2)}\}$ has zero Hamiltonian vector field and vanishes at zero, so is zero.

The full bracket $J_{nm}=\{I_n,I_m\}$ is an analytic finite-jet local conserved functional, by the Jacobi identity and $\{I_n,H\}=0$. The substitution fixes zero, and $U$ and $g$ start at quadratic order there. Consequently every $I_n$ has zero constant and linear terms. Therefore $J_{nm}$ has no constant or linear term, and its quadratic part is the bracket just proved zero. Lemma 6.2 implies

$$
 \boxed{\{I_n,I_m\}=0\quad\hbox{for all }n,m.}            \tag{7.4}
$$

Equation (7.4) follows from the computed quadratic generators and Lemma 6.2. Preservation of the bulk Hamiltonian by a canonical family would not alone suffice; Section 9 gives an explicit example.

Permutability follows, in the formal sense appropriate here. Let $A_\epsilon=T_\epsilon^*$ act on local functions. The source-velocity identity is $\partial_\epsilon A_\epsilon=\mathcal L_{W_\epsilon}A_\epsilon$. Equations (5.7) and (7.4), together with $A_0=I$, give

$$
 A_\epsilon=
 \exp\left(-\sum_{n\geq1}\frac{\epsilon^n}{n}
                           \mathcal L_{X_{I_n}}\right).   \tag{7.5}
$$

All coefficients in the exponent commute, so $A_\epsilon A_\eta=A_\eta A_\epsilon$ and consequently $T_\epsilon T_\eta=T_\eta T_\epsilon$. Every coefficient of this exponential involves only finitely many compositions of local evolutionary derivations. It is therefore a well-defined formal substitution. This proves formal Bianchi permutability; a finite algebraic superposition formula is not required. $\square$

## 8. Infinitely many independent charges

**Proposition 8.1 (functional independence).** For every positive integer $N$, some $N$ charges from (2.3) have independent differentials at arbitrarily small periodic Cauchy data.

**Proof.** We compute their quadratic parts as local functionals, modulo integration by parts.

Because $E$ is real skew and commutes with $M$, choose a real unit vector $a$ in a common eigenspace of $-E^2$ and $M$:

$$
 -E^2a=e^2a,\qquad Ma=m^2a,\quad m^2>0,\quad e\geq0.
$$

For odd $n=2j+1$, $C_n$ is a real polynomial in $E^2$, so it acts as a scalar on this subspace. Restrict $I_{2j+1}^{(2)}$ to $u=0$, $p=a\varphi$. The $u$-component of its Hamiltonian vector field is its $p$-gradient. Equation (7.3) therefore gives

$$
 I_{2j+1}^{(2)}\big|_{u=0,p=a\varphi}
       =\frac12\int\varphi P_j(\partial_x^2)\varphi\,dx,
 \qquad
 P_j(z)=c_jz^j+\text{lower powers},\quad
 c_j=\operatorname{Re}(1+ie)^{2j+1}.                       \tag{8.1}
$$

For completeness, write the $2\times2$ restriction of $\mathcal L$ as $-\partial_xI+A$, with $A^2=(\partial_x^2-m^2)I$ and $A_{12}=1$. Its odd power has off-diagonal entry polynomial in $\partial_x^2$ with leading term $2^{2j}\partial_x^{2j}$. Multiplying the scalar $C_{2j+1}=2^{-2j}\operatorname{Re}(1+ie)^{2j+1}$ proves (8.1).

Infinitely many $c_j$ are nonzero. Indeed, set $\theta=\arctan e\in[0,\pi/2)$. If all sufficiently late $c_j$ vanished, two consecutive late odd angles would both have zero cosine. Their difference gives $2\theta\in\pi\mathbb Z$. In the indicated range this forces $\theta=0$, where none of the cosines vanishes, a contradiction. Some individual charges can vanish; no assertion is made that every coefficient is nontrivial.

Choose $N$ indices $j_1<\cdots<j_N$ with $c_{j_i}\ne0$. The polynomials $P_{j_i}$ have distinct degrees and are linearly independent. Hence there are distinct positive integers $k_1,\ldots,k_N$ for which the evaluation matrix $[P_{j_i}(-k_\ell^2)]$ is invertible. Otherwise their evaluation vectors on this infinite set would span a proper subspace, giving a nonzero linear combination vanishing at infinitely many points, impossible for a polynomial.

On the circle of length $2\pi$, restrict further to

$$
 u=0,\qquad p=a\sum_{\ell=1}^N b_\ell\cos(k_\ell x).
$$

The quadratic charges are $(\pi/2)\sum_\ell P_{j_i}(-k_\ell^2)b_\ell^2$. At $b_\ell=\tau\beta_\ell$ with all $\beta_\ell\ne0$, the Jacobian of the full charges is the invertible quadratic Jacobian of order $\tau$, plus $O(\tau^2)$. Its determinant has a nonzero coefficient at order $\tau^N$ and is therefore nonzero for sufficiently small nonzero $\tau$. Their differentials are independent at those data, and by continuity on a neighborhood in a sufficiently regular function space. This proves Proposition 8.1 and completes the proof of Theorem 2.1. $\square$

## 9. A noncommuting family for a reducible bulk theory

Dropping bulk irreducibility while retaining only invertibility of $G$ does not guarantee that the family supplied by one defect commutes. Here is an exact example with two massive free fields:

$$
 U(u)=\tfrac12|u|^2,\quad
 E=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad D=I-E,
 \quad G=\operatorname{diag}(4,8),
$$
$$
 f(w)=\tfrac12w_1^2+\tfrac14w_2^2,\qquad
 g(q)=2q_1^2+4q_2^2.                                     \tag{9.1}
$$

Equation (3.4) holds exactly, since $f''=4G^{-1}$ and $[E,U'']=0$. The family $B_\epsilon=\epsilon f+\epsilon^{-1}g$ has a unique transparent local branch and the same canonical-generating construction.

On a free plane wave, write $\ell$ for the eigenvalue of $D_-$ and set $A=2DG^{-1}$, $B=2D^TG^{-1}$. The amplitude transformation is

$$
 T_\epsilon=(I-\epsilon\ell B)(I+\epsilon\ell A)^{-1}
 =I+\epsilon\ell t_1+\epsilon^2\ell^2t_2+\cdots,
 \quad t_1=-(A+B),\quad t_2=(A+B)A.
$$

Direct matrix multiplication gives

$$
 [t_1,t_2]=\frac18\begin{pmatrix}0&1\\1&0\end{pmatrix},
 \qquad
 T_\epsilon T_\eta-T_\eta T_\epsilon
 =\frac{\epsilon\eta(\eta-\epsilon)\ell^3}{8}
        \begin{pmatrix}0&1\\1&0\end{pmatrix}
   +O_{\mathrm{total}}(4).                               \tag{9.2}
$$

This is an obstruction to automatic commutativity of the defect family, **not** a nonintegrable bulk counterexample: these bulk fields are free and integrable. It also explains why irreducibility of the combined bulk and defect would be the wrong substitute for hypothesis 2.

## 10. A coupled nonlinear example and exact checks

As a check that the assumptions admit a coupled nonlinear example, take

$$
 \alpha_1=(\sqrt2,0)^T,\quad
 \alpha_2=(-1/\sqrt2,\sqrt6/2)^T,\quad
 \alpha_3=(-1/\sqrt2,-\sqrt6/2)^T,
 \quad E=\frac1{\sqrt3}\begin{pmatrix}0&1\\-1&0\end{pmatrix},
$$
$$
 U(w)=\sum_{i=1}^3e^{\alpha_i^Tw}-3,\qquad
 g(q)=\sum_{i=1}^3e^{\beta_i^Tq}-3,\quad \beta_i=D^T\alpha_i.
                                                               \tag{10.1}
$$

Then $M=3I$, $g''(0)=4I$, and

$$
 [\alpha_i^T\beta_j]_{ij}
 =\begin{pmatrix}2&0&-2\\-2&2&0\\0&-2&2\end{pmatrix},
 \qquad -D\alpha_i=\beta_{i-1}
$$

with cyclic indices. Comparing the independent exponentials $e^{\alpha_i^Tw}$ proves (3.8) exactly. The potential is irreducible: an orthogonal splitting in two dimensions would require all mixed Hessian coefficients to vanish; independence of these three exponentials would force every $\alpha_i$ onto one of two perpendicular axes, which their directions exclude. This is the $A_2^{(1)}$ example within the classical Type-I setting of Bowcock–Corrigan–Zambon [2](https://arxiv.org/abs/hep-th/0401020). The example verifies that the hypotheses admit a coupled nonlinear potential; no root data enter the general proof.

The exact symbolic checks are in `textbook_code/defect_integrability_structural/checks.py`. Run them from the repository root with

```sh
python3 textbook_code/defect_integrability_structural/checks.py
```

The [recorded output](structural_type_I/verification.txt) contains 30 passing checks. These cover the original linearized sewing equations, the temporal symplectic identity with spatial adjoints, seven quadratic Hamiltonian generators and their commutators, a finite Fourier independence determinant, the obstruction (9.2), and the mixed derivative (6.3). For (10.1), the script checks the potential identity exactly, the first four nonlinear local currents, and the Poisson bracket of the nontrivial spin-two and spin-four charges. The nonlinear checks do not truncate field amplitude.

The distinction between a sequence of coefficients and a sequence of nontrivial charges is visible in this example. Here $E^2=-I/3$, so $C_3=(I+3E^2)/4=0$. Lemma 6.2 implies $I_3=0$ as a local functional; its density is a spatial derivative. The script checks that fact independently using Euler derivatives, and also verifies that $I_2$ is nontrivial.

Finite calculations verify these identities and examples. The all-orders conclusions use the written proofs, especially Lemmas 6.1–6.2. Neither Theorem 2.1 nor those analytic variational arguments have been formalized in Lean. The separate algebraic Lean lemmas accompanying the earlier scalar reconstruction are not a formal certification of this paper.

The companion script `textbook_code/defect_integrability_structural/paper_checks.py` supplies twelve further exact checks of the derivations and scope examples: the general three-component momentum and chiral identities, the temporal endpoint momenta, the kinetic term modulo a derivative, the full-sewing residual, the spatial Hamiltonian and generating-functional signs, the shifted critical point, and the massless obstruction in Section 11. Its output is in [paper_verification.txt](structural_type_I/paper_verification.txt). Run it with

```sh
python3 textbook_code/defect_integrability_structural/paper_checks.py
```

## 11. Different bulk theories and limits of the result

### 11.1 What transparency forces

Suppose the same normalized constant Type-I coupling instead joins potentials $U_-$ and $U_+$. The calculation of Proposition 3.1 still gives a split defect potential, but (3.4) becomes

$$
 U_-(w+Dq)-U_+(w-D^Tq)=\frac12 f'(w)^Tg'(q).              \tag{11.1}
$$

If $g'(0)=0$, evaluating (11.1) at $q=0$ gives $U_-(w)=U_+(w)$ near zero. More generally, if $g'(q_*)=0$ at any fixed $q_*$, then

$$
 U_-(z)=U_+(z-2q_*),\qquad z=w+Dq_*.                     \tag{11.2}
$$

Thus moving the transparent critical point only permits a constant field shift. In the coordinate normalization used here, genuinely different potentials cannot satisfy the transparent-limit hypothesis. This is an algebraic consequence of momentum conservation, not merely a choice to write the same symbol $U$ on both sides.

Genuinely different bulk theories can nevertheless occur in integrable defect constructions. For example, Section 2 of [1](https://arxiv.org/html/hep-th/0305022) gives a defect joining a Liouville field to a free massless field. Such a pair has no common positive-mass vacuum of the kind required by Theorem 2.1.

### 11.2 A possible composition argument

Suppose a defect between different theories gives equal-time canonical maps $T_\lambda:\mathcal P_-\to\mathcal P_+$ intertwining their evolutions. Wherever $T_{\lambda_0}$ is invertible, the composition

$$
 S_\lambda=T_{\lambda_0}^{-1}\circ T_\lambda:
             \mathcal P_-\longrightarrow\mathcal P_-      \tag{11.3}
$$

is canonical, preserves the left evolution, and equals the identity at $\lambda_0$. These statements follow directly by composing the symplectic and intertwining identities. They do not establish an integrable hierarchy. Solving either Bäcklund transformation may require integration, and the composition may have nonlocal coefficients even though the sewing equations are local.

To use the present mechanism, one would need a local expansion of (11.3) with local Hamiltonian parameter generators, control of its vacuum behavior, commuting quadratic generators, and an unbounded independent sequence of their symbols. Lemma 6.2 would then apply if the remaining analytic massive hypotheses hold. Establishing these additional properties for genuinely different theories is outside Theorem 2.1.

### 11.3 Other restrictions

The assumptions perform different tasks. The constant Type-I coupling gives the split momentum identity and the explicit temporal generating functional. The transparent nondegenerate Hessian makes the local recursion triangular. Bulk irreducibility forces that Hessian to be scalar, which is sufficient for commutation of the quadratic parameter generators. Positive masses exclude higher-degree local free conserved functionals, and analyticity upgrades the amplitude argument to an identity of local analytic functionals.

The mass restriction cannot simply be dropped from the rigidity argument. For a free massless scalar, $r=p+u_x$ satisfies $D_tr=D_xr$, so $\int r^n dx$ is conserved for every positive integer $n$. At $n\geq3$ this is a nonzero local functional with no quadratic part, contradicting the conclusion of Lemma 6.1 if that lemma were stated without its mass hypothesis. Smooth functions flat at the vacuum likewise cannot be excluded by the analytic Taylor-series argument.

Type-II defects with auxiliary variables, field-dependent kinetic couplings, general higher-derivative bulk Lagrangians, and nonrelativistic equations require further work. The spatial geometric statement in Appendix A explains an intertwining mechanism, but does not supply the additional locality, commutation, or independence arguments for these classes.

## 12. Conclusion

Within the hypotheses of Theorem 2.1, momentum conservation produces a reciprocal parameter family whose formal local branch is canonical in equal time. Its defect-energy expansion generates conserved Hamiltonians. The decisive step is the rigidity of massive analytic local conservation laws: the quadratic Hamiltonian generators commute, so their full nonlinear counterparts commute. Actual quadratic charge symbols, rather than unreduced derivative order, prove functional independence of arbitrarily large finite subfamilies. Formal Bianchi permutability is a consequence.

The potential remains unspecified throughout the proof. The resulting theorem is restricted to the analytic massive Type-I setting stated here; the general implication from a momentum-conserving interface to integrability of both adjoining theories remains open.

## Appendix A. The spatial Hamilton–Jacobi interpretation

For the bulk Lagrangian (2.1), the spatial momentum and Hamiltonian density are

$$
 \pi=-u_x,\qquad
 \mathcal H^{(x)}=\pi^Tu_x-L
     =-\frac12|\pi|^2-\frac12|u_t|^2+U(u)=-T^{11}(u).     \tag{A.1}
$$

At fixed $x$, consider histories in $t$, with variations and boundary conditions for which integration by parts has no boundary contribution. Periodic histories are one choice. In the formal variational description,

$$
 \Omega^{(x)}=\int\delta u^T\wedge\delta\pi\,dt,\qquad
 H^{(x)}=\int\mathcal H^{(x)}dt.
$$

Hamilton's equations give $u_x=-\pi$ and $\pi_x=-u_{tt}-U'(u)$, which are equivalent to the bulk equation. If $S_d=\int L_d\,dt$, the boundary variation of the bulk and defect action gives

$$
 d(-S_d)=\int(\pi_-^T\delta u-\pi_+^T\delta v)dt          \tag{A.2}
$$

on the sewing relation. This is the generating-functional identity for a spatial canonical relation. A concrete infinite-dimensional phase-space interpretation additionally requires a regular realization of the relation and the appropriate Lagrangian property; (A.2) alone is not a proof of those analytic hypotheses in every function space.

**Lemma A.1 (symplectic intertwining).** Let $(\mathcal P_\pm,\Omega_\pm)$ be symplectic manifolds on which the Hamiltonian vector fields $X_{H_\pm}$ exist. Let $\Gamma$ be a regular Lagrangian submanifold of $(\mathcal P_-\times\mathcal P_+,\Omega_-\oplus(-\Omega_+))$. In an infinite-dimensional application, assume explicitly the Lagrangian equality $T\Gamma=(T\Gamma)^{\perp_\Omega}$. Then $(X_{H_-},X_{H_+})$ is tangent to $\Gamma$ if and only if $H_--H_+$ is locally constant on $\Gamma$. If the relation is locally a graph, this tangency expresses intertwining of the Hamiltonian evolutions.

**Proof.** For a vector $Y$ tangent to $\Gamma$,

$$
 \Omega\big((X_{H_-},X_{H_+}),Y\big)=d(H_--H_+)(Y).
$$

If the right side vanishes, the Hamiltonian vector belongs to $(T\Gamma)^{\perp_\Omega}=T\Gamma$. Conversely, if it is tangent, the left side vanishes because $\Gamma$ is isotropic, so the restricted differential is zero. The graph assertion follows from the definition of the tangent space of a graph. $\square$

For the momentum balance used in Section 3,

$$
 \mathcal H_-^{(x)}-\mathcal H_+^{(x)}=-D_tP_d.             \tag{A.3}
$$

Integrating over histories with vanishing boundary contribution gives $H_-^{(x)}-H_+^{(x)}=0$ on the relation. Lemma A.1 then explains spatial Bäcklund intertwining whenever its geometric hypotheses hold. The calculation allows distinct bulk potentials. It supplies neither an equal-time canonical map nor an infinite commuting hierarchy on its own. For the class of Theorem 2.1, Sections 4–8 establish those further conclusions directly in the Cauchy-jet algebra.

## References

1. P. Bowcock, E. Corrigan and C. Zambon, [*Classically integrable field theories with defects*](https://arxiv.org/abs/hep-th/0305022), International Journal of Modern Physics A **19S2** (2004), 82–91.
2. P. Bowcock, E. Corrigan and C. Zambon, [*Affine Toda field theories with defects*](https://arxiv.org/abs/hep-th/0401020), Journal of High Energy Physics **01** (2004), 056.
3. R. Bristow and P. Bowcock, [*Momentum conserving defects in affine Toda field theories*](https://arxiv.org/abs/1612.03002), Journal of High Energy Physics **05** (2017), 153.
4. V. Caudrelier and A. Kundu, [*A multisymplectic approach to defects in integrable classical field theory*](https://arxiv.org/abs/1411.0418), Journal of High Energy Physics **02** (2015), 088.
5. V. B. Kuznetsov and E. K. Sklyanin, [*Few remarks on Bäcklund transformations for many-body systems*](https://arxiv.org/abs/solv-int/9711010), Journal of Physics A **31** (1998), 2241–2251.
6. T. J. Gordon, [*Conserved currents of the Klein–Gordon field*](https://doi.org/10.1017/S0305004100058965), Mathematical Proceedings of the Cambridge Philosophical Society **90** (1981), 507–515.
7. S. Opanasenko and R. O. Popovych, [*Generalized symmetries and conservation laws of (1+1)-dimensional Klein–Gordon equation*](https://arxiv.org/abs/1810.12434), Journal of Mathematical Physics **61** (2020), 101515.
