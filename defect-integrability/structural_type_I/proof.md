# A structural integrability theorem for massive analytic Type-I defects

**Status: complete written argument under the hypotheses below; not independently refereed or Lean-formalized.**

Date: 2026-10-16. This is a separate continuation of the reconstruction in PR #32. It does not replace the original paper or claim its unrestricted theorem. The potential remains unspecified throughout the proof. No classification of potentials, root system, Lax pair, or assumed Bianchi permutability enters the argument.

## 1. Statement and scope

Let $u(x,t)\in\mathbb R^r$ have Lagrangian and equation

$$
 L=\frac12|u_t|^2-\frac12|u_x|^2-U(u),\qquad
 u_{tt}-u_{xx}+U'(u)=0.                                      \tag{1.1}
$$

Assume the following.

1. **Analytic massive vacuum.** $U$ is real analytic near $0$, with $U(0)=0$, $U'(0)=0$, and $M=U''(0)$ positive definite.
2. **Bulk irreducibility.** There is no nontrivial orthogonal splitting $\mathbb R^r=V_1\oplus V_2$ on which the germ of $U$ is a sum $U_1(u_1)+U_2(u_2)$. This is irreducibility of the bulk potential, not merely of the combined bulk and defect.
3. **Normalized constant Type-I coupling.** The auto-defect joins two copies of (1.1), has no auxiliary fields, and has action density
   $$
   L_d=\frac12u^TEu_t+u^TDv_t+\frac12v^TEv_t-B(u,v),
   \quad E^T=-E,\quad D=I-E.                                \tag{1.2}
   $$
   $B$ is analytic. There is a derivative-free defect momentum $P_d(u,v)$ satisfying the strong momentum identity: after substituting the sewing equations, the identity holds for independent values of $u,v,u_t,v_t$.
4. **Transparent critical point.** In the splitting $B=f(w)+g(q)$ derived below, $g'(0)=0$ and $G=g''(0)$ is invertible. Additive constants in $f,g,P_d$ are immaterial and are normalized as below.

The word “normalized” in hypothesis 3 is substantive: the same right-field coordinates are used for the auto-potential and the transparent diagonal. We do not assert that every possible Type-I defect can be put in this form while preserving both identifications.

**Theorem.** Under hypotheses 1–4, the momentum identity supplies a rescaled family of defects with a unique formal local branch $T_\epsilon=\mathrm{Id}+O(\epsilon)$. Its defect energy has an expansion

$$
 I(\epsilon)=\int B_\epsilon(u,T_\epsilon u)\,dx
            =\sum_{n\geq1}\epsilon^n I_n.                    \tag{1.3}
$$

Each $I_n$ is an analytic finite-jet local conserved functional. All $I_n$ Poisson commute for the canonical equal-time bracket. Infinitely many are functionally independent: for every $N$ there are $N$ members whose differentials are independent at arbitrarily small periodic Cauchy data. The formal maps $T_\epsilon$ commute for different parameters.

The same conclusion holds without hypothesis 2 if one assumes directly that $g''(0)$ is a nonzero scalar matrix. The precise role of irreducibility is to derive this condition.

This is local integrability in the sense of infinitely many independent commuting local charges. The parameter series need not converge. The result gives neither global Bäcklund maps nor a Lax representation, and does not cover Type-II, massless, smooth nonanalytic, or general dispersive theories.

We use local functionals modulo $x$-derivatives, with no explicit $x,t$ dependence. Their densities are analytic in finitely many Cauchy jets $(u,p,u_x,p_x,\ldots)$ near the zero jet, where $p=u_t$. Integrals may be evaluated on small smooth periodic data or rapidly decreasing data. The proof of a local identity can be tested on the line before applying it on a circle. Set

$$
 \Omega=\int\delta u^T\wedge\delta p\,dx,\qquad
 \{F,H\}=\int(F_u^TH_p-F_p^TH_u)\,dx,
 \quad \iota_{X_F}\Omega=dF.                                \tag{1.4}
$$

Subscripts on functionals mean variational derivatives. Constants are fixed by evaluation at the zero field.

## 2. What momentum conservation actually forces

The sewing equations from (1.2) are

$$
 u_x=Eu_t+Dv_t-B_u,\qquad
 v_x=D^Tu_t-Ev_t+B_v.                                      \tag{2.1}
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
 \frac12(|B_u|^2-|B_v|^2)=U(u)-U(v).                        \tag{2.2}
$$

Introduce independent coordinates

$$
 q=\frac{u-v}{2},\quad
 w=\frac{D^Tu+Dv}{2},\qquad
 u=w+Dq,\quad v=w-D^Tq.                                    \tag{2.3}
$$

The first two identities in (2.2) become $(P_d)_w=-B_w$ and $(P_d)_q=B_q$. Equality of mixed derivatives implies $B_{wq}=0$. Consequently, locally,

$$
 B=f(w)+g(q),\qquad P_d=-f(w)+g(q),
$$

and the last identity in (2.2) is exactly

$$
 U(w+Dq)-U(w-D^Tq)=\frac12 f'(w)^Tg'(q).                   \tag{2.4}
$$

These steps derive the split potential; it is not an exponential ansatz. Conversely, (2.4) implies all of (2.2).

Differentiate (2.4) in $q$ at zero. Since $D+D^T=2I$,

$$
 Gf'(w)=4U'(w).                                            \tag{2.5}
$$

Both $G$ and $f''$ are symmetric. Differentiating (2.5) and transposing shows

$$
 [G,U''(w)]=0\quad\hbox{for every }w.                      \tag{2.6}
$$

Diagonalize $G$ orthogonally. Equation (2.6) says every mixed second derivative of $U$ between distinct eigenspaces vanishes. Integrating this statement near zero splits $U$ as a sum of potentials on those eigenspaces; $U'(0)=0$ removes any issue with linear terms. Bulk irreducibility therefore forces $G=\gamma I$, $\gamma\ne0$.

Normalize $f(0)=g(0)=0$. Then $f=4U/\gamma$. Multiplying $f$ by a parameter and $g$ by its inverse preserves (2.4). On rescaling that parameter and replacing $g$ by $4g/\gamma$, the family takes the form

$$
 B_\epsilon=\epsilon U(w)+\epsilon^{-1}g(q),\qquad
 P_\epsilon=-\epsilon U(w)+\epsilon^{-1}g(q),              \tag{2.7}
$$

where, from now on,

$$
 g(0)=0,\quad g'(0)=0,\quad g''(0)=4I,\qquad
 U(w+Dq)-U(w-D^Tq)=\tfrac12 U'(w)^Tg'(q).                 \tag{2.8}
$$

Thus a parameter family is derived within this class. No claim about an arbitrary symmetry producing a spectral family is needed.

There is one further consequence needed later. Put $w=0$ in (2.8) and compare quadratic terms in $q$. This gives

$$
 D^TMD=DMD^T,\qquad [E,M]=0.                              \tag{2.9}
$$

The second equality follows by expanding the first: its difference is $2(EM-ME)$.

## 3. A local formal branch satisfying both sewing equations

Write $D_\pm=D_t\pm D_x$, with $D_t$ acting on Cauchy jets by

$$
 D_tu=p,\qquad D_tp=u_{xx}-U'(u),\qquad [D_t,D_x]=0.
$$

Equations (2.1) become

$$
 D_+q=-\frac\epsilon2U'(w),\qquad
 D_-w=\frac1{2\epsilon}g'(q).                             \tag{3.1}
$$

Since $w=u-Dq$, the second equation is

$$
 g'(q)=2\epsilon D_-u-2\epsilon D D_-q.                   \tag{3.2}
$$

Set $q=\sum_{n\geq1}\epsilon^n q_n$. The linear part of $g'$ is $4q$. At order $n$, the right side uses only $q_1,\ldots,q_{n-1}$, as do the nonlinear terms of $g'(q)$. Division by $4$ determines $q_n$ uniquely. Each coefficient is an analytic function of finitely many Cauchy jets. In particular,

$$
 q_1=\tfrac12(p-u_x),\quad
 v=u-2q=u+\epsilon(u_x-p)+O(\epsilon^2).                  \tag{3.3}
$$

It remains to prove the first equation; solving one equation and declaring the other compatible would be insufficient. Define

$$
 A=D_+q+\tfrac\epsilon2U'(w).
$$

Differentiating (2.8) in $w,q$ and solving the resulting two linear identities for $U'(u)$ gives

$$
 U'(u)=\tfrac14\{g''(q)U'(w)+D U''(w)g'(q)\}.            \tag{3.4}
$$

Use (3.2) to differentiate $u=w+Dq$. Direct substitution yields

$$
 D_+D_-u+U'(u)
   =\left(D D_-+\frac1{2\epsilon}g''(q)\right)A.           \tag{3.5}
$$

The left side vanishes on the bulk equation. The operator on the right has leading Laurent coefficient $2\epsilon^{-1}I$. If $A$ had a first nonzero coefficient $\epsilon^a A_a$, the lowest term of the right side would be $2\epsilon^{a-1}A_a$, a contradiction. Thus $A=0$ coefficientwise. Using $v=w-D^Tq$ and the other combination of the derivatives of (2.8) now gives $D_+D_-v+U'(v)=0$.

Consequently

$$
 T_\epsilon:(u,p)\longmapsto(v,D_tv)
$$

is a local formal substitution, intertwines the bulk evolution, fixes the zero solution, and has a unique formal inverse. The argument only compares Laurent coefficients bounded below; it does not assert injectivity of $D_t$ on a differential algebra.

## 4. Conserved energy coefficients and equal-time canonicity

The full sewing equations imply the current identity directly:

$$
 D_tB_\epsilon+D_xP_\epsilon
 =\epsilon U'(w)^TD_-w+\epsilon^{-1}g'(q)^TD_+q=0.          \tag{4.1}
$$

On the branch $q=O(\epsilon)$, both densities are $O(\epsilon)$. Therefore (1.3) defines local conserved charges at every order. The first is

$$
 I_1=\int\left\{\tfrac12|p-u_x|^2+U(u)\right\}dx.        \tag{4.2}
$$

Now form a functional on two independent equal-time endpoint fields:

$$
 F_\epsilon[u,v]=\int\{2q^Tw_x+P_\epsilon(w,q)\}\,dx.    \tag{4.3}
$$

The kinetic term is equivalent modulo an $x$-derivative to
$\frac12u^TEu_x+u^TDv_x+\frac12v^TEv_x$.
Its variation in $(w,q)$ is

$$
 \delta F_\epsilon=\int\left[
 (-2q_x-\epsilon U'(w))^T\delta w
 +(2w_x+\epsilon^{-1}g'(q))^T\delta q\right]dx.            \tag{4.4}
$$

On (3.1), the two coefficients are $p-P$ and $D^Tp+DP$, respectively, where $P=v_t$. By (2.3),

$$
 \delta F_\epsilon=\int(p^T\delta u-P^T\delta v)dx.        \tag{4.5}
$$

Hence the already constructed transformation is canonical for the **equal-time** form (1.4). This is an explicit additional calculation, not an identification of spatial and temporal symplectic structures.

At fixed endpoints,

$$
 \epsilon\partial_\epsilon F_\epsilon
             =-\int B_\epsilon\,dx.                      \tag{4.6}
$$

The source velocity $W_\epsilon=(DT_\epsilon)^{-1}\partial_\epsilon T_\epsilon$ therefore obeys

$$
 \iota_{W_\epsilon}\Omega=dK_\epsilon,\qquad
 K_\epsilon=-I(\epsilon)/\epsilon.                        \tag{4.7}
$$

Here is a sign check of this generating-function fact. Put $\theta=\int p^T\delta u\,dx$, so $d\theta=-\Omega$, and let $V=(\partial_\epsilon T)\circ T^{-1}$. Pulling (4.5) to the graph gives $d(F\circ\mathrm{graph}\,T)=\theta-T^*\theta$. Its parameter derivative is

$$
 d\{(\partial_\epsilon F)\circ\mathrm{graph}\,T
       -T^*(\iota_V\theta)\}
 =T^*(\iota_V\Omega)-dT^*(\iota_V\theta).
$$

Cancel the last exact terms and use $T^*\Omega=\Omega$. This proves (4.7). Thus the conserved coefficients are precisely the Hamiltonians of the parameter velocity.

## 5. A rigidity lemma for massive local conservation laws

The following argument is the main replacement for an assumed Bianchi identity.

**Lemma 5.1 (free massive fields).** For finitely many real free Klein–Gordon fields with positive masses, a translation-invariant homogeneous polynomial local functional of degree $n\geq3$ conserved by the free evolution is zero modulo a spatial derivative. A conserved linear local functional is zero as well.

**Proof.** Diagonalize the positive mass matrix. For a species $a$ and real Fourier momentum $k$, write

$$
 \omega_a(k)=\sqrt{k^2+m_a^2},\qquad
 \widehat u_a=a_{a,+}+a_{a,-},\quad
 \widehat p_a=i\omega_a(a_{a,+}-a_{a,-}).                    \tag{5.1}
$$

Complexification and polarization let the amplitudes be treated independently. They evolve by $\dot a_{a,\sigma}=i\sigma\omega_a a_{a,\sigma}$. A finite-jet homogeneous local functional has, in each polarized component, a Fourier kernel supported only by the overall factor $\delta(k_1+\cdots+k_n)$. Its coefficient $A(k_1,\ldots,k_n)$ is a real-analytic function of the real momenta after (5.1); before this invertible change of amplitudes it is polynomial in them.

Conservation for arbitrary Fourier wave packets implies on the momentum hyperplane

$$
 \Phi A=0,\qquad
 \Phi=\sum_{j=1}^n\sigma_j\omega_{a_j}(k_j),\quad
 k_n=-\sum_{j<n}k_j.                                     \tag{5.2}
$$

For $n\geq3$, two of the independent variables are $k_1,k_2$, and

$$
 \frac{\partial^2\Phi}{\partial k_1\partial k_2}
 =\frac{\sigma_n m_{a_n}^2}
        {(k_n^2+m_{a_n}^2)^{3/2}}\ne0.                    \tag{5.3}
$$

Thus $\Phi$ cannot vanish identically on any open subset. Equation (5.2) forces $A=0$ on the complement of its zero set and hence everywhere by continuity. This does **not** deny the existence of resonant momenta. Locality rules out a kernel supported only on their lower-dimensional set.

Invert (5.1). Each original polynomial kernel vanishes on $\sum k_j=0$, so is divisible by $\sum k_j$. In the polarized differential-polynomial representation this factor is precisely a total $x$-derivative (up to the harmless Fourier factor $i$). This proves the functional is zero. At degree one, integration by parts leaves only $\int(a^Tu+b^Tp)dx$; conservation and invertibility of the mass matrix force $a=b=0$. $\square$

**Lemma 5.2 (injectivity of the quadratic part).** Let $H=\int\{\frac12|p|^2+\frac12|u_x|^2+U(u)\}dx$ satisfy hypothesis 1. An analytic finite-jet local conserved functional with zero constant, linear, and quadratic parts as a functional is zero. In particular, two normalized conserved functionals with no linear term and the same quadratic part coincide.

**Proof.** Expand by amplitude degree, assigning degree one to every Cauchy jet. Suppose the first nonzero homogeneous functional has degree $n\geq3$. At that degree, $\{F,H\}=0$ reads $\{F^{(n)},H^{(2)}\}=0$: all nonlinear terms of $H$ contribute at higher degree. Lemma 5.1 makes $F^{(n)}$ a spatial derivative, a contradiction. Equivalently, induction makes every homogeneous functional zero. This induction takes place modulo derivatives, so lower homogeneous densities that are nonzero derivatives cause no extra terms in a Poisson bracket.

For an analytic density involving a fixed finite number of jets, its Euler derivatives are analytic functions of finitely many jets. Their Taylor series vanish by the preceding argument; hence the Euler derivatives vanish near zero. Integrate the first variation along the scaling path $(u,p)\mapsto\lambda(u,p)$, $0\leq\lambda\leq1$. Integration by parts expresses it through those Euler derivatives, so the functional equals its vacuum value, which is zero. The same argument holds purely formally in amplitude. $\square$

This is a lemma about **local** functionals. Products such as $H^2$ are not local integrals and are not counterexamples. Positivity of the masses and analyticity have been stated where used, not hidden in an appeal to a general injectivity assertion.

For context, the classification of local currents of the free Klein–Gordon equation is an established subject: see [Gordon (1981)](https://doi.org/10.1017/S0305004100058965) and [Opanasenko–Popovych](https://arxiv.org/abs/1810.12434). The multicomponent translation-invariant statement needed here has the self-contained proof above; no classification theorem from those sources is being assumed.

## 6. Commutation to all orders

Linearize at zero. On Cauchy columns $z=(u,p)^T$, let

$$
 \mathcal L=
 \begin{pmatrix}-\partial_x I&I\\ \partial_x^2I-M&-\partial_xI\end{pmatrix}.
                                                               \tag{6.1}
$$

This represents $D_-$ on free Cauchy data. A constant field-space matrix acts diagonally on the two Cauchy components; hats for these diagonal lifts will be suppressed. Equation (2.9) ensures that $E,D,D^T$ all commute with $\mathcal L$.

The linearized second equation of (3.1) says $q=(\epsilon/2)D_-w$. Combining it with (2.3) gives the exact formal linearization

$$
 T_\epsilon^{\mathrm{lin}}
 =\left(I-\frac\epsilon2D^T\mathcal L\right)
  \left(I+\frac\epsilon2D\mathcal L\right)^{-1}.            \tag{6.2}
$$

All coefficients belong to the commutative algebra generated by $E,\mathcal L$. Thus its source velocities commute for different parameters. More explicitly, expansion and logarithmic differentiation of (6.2), followed by (4.7), give

$$
 X_{I_n^{(2)}}=C_n\mathcal L^n,\qquad
 C_n=2^{-n}\bigl((I+E)^n-(-1)^n(I-E)^n\bigr).              \tag{6.3}
$$

For any $n,m$, these constant-coefficient linear Hamiltonian vector fields commute. The quadratic functional $\{I_n^{(2)},I_m^{(2)}\}$ has zero Hamiltonian vector field and vanishes at zero, so is zero.

The full bracket $J_{nm}=\{I_n,I_m\}$ is an analytic finite-jet local conserved functional, by the Jacobi identity and $\{I_n,H\}=0$. Both charges begin quadratically. Therefore $J_{nm}$ has no constant or linear term, and its quadratic part is the bracket just proved zero. Lemma 5.2 implies

$$
 \boxed{\{I_n,I_m\}=0\quad\hbox{for all }n,m.}            \tag{6.4}
$$

There is no assumption that a general Hamiltonian-preserving canonical family commutes. The calculation of its quadratic generators and the massive locality lemma supply the missing argument for this family.

Permutability follows, in the formal sense appropriate here. Let $A_\epsilon=T_\epsilon^*$ act on local functions. The source-velocity identity is $\partial_\epsilon A_\epsilon=\mathcal L_{W_\epsilon}A_\epsilon$. Equations (4.7) and (6.4), together with $A_0=I$, give

$$
 A_\epsilon=
 \exp\left(-\sum_{n\geq1}\frac{\epsilon^n}{n}
                           \mathcal L_{X_{I_n}}\right).   \tag{6.5}
$$

All coefficients in the exponent commute, so $A_\epsilon A_\eta=A_\eta A_\epsilon$ and consequently $T_\epsilon T_\eta=T_\eta T_\epsilon$. This proves formal Bianchi permutability without supplying a finite algebraic superposition formula.

## 7. Infinitely many independent charges

Increasing jet order alone is not the argument. We examine the actual quadratic charges, modulo integration by parts.

Because $E$ is real skew and commutes with $M$, choose a real unit vector $a$ in a common eigenspace of $-E^2$ and $M$:

$$
 -E^2a=e^2a,\qquad Ma=m^2a,\quad m^2>0,\quad e\geq0.
$$

For odd $n=2j+1$, $C_n$ is a real polynomial in $E^2$, so it acts as a scalar on this subspace. Restrict $I_{2j+1}^{(2)}$ to $u=0$, $p=a\varphi$. The $u$-component of its Hamiltonian vector field is its $p$-gradient. Equation (6.3) therefore gives

$$
 I_{2j+1}^{(2)}\big|_{u=0,p=a\varphi}
       =\frac12\int\varphi P_j(\partial_x^2)\varphi\,dx,
 \qquad
 P_j(z)=c_jz^j+\text{lower powers},\quad
 c_j=\operatorname{Re}(1+ie)^{2j+1}.                       \tag{7.1}
$$

For completeness, write the $2\times2$ restriction of $\mathcal L$ as $-\partial_xI+A$, with $A^2=(\partial_x^2-m^2)I$ and $A_{12}=1$. Its odd power has off-diagonal entry polynomial in $\partial_x^2$ with leading term $2^{2j}\partial_x^{2j}$. Multiplying the scalar $C_{2j+1}=2^{-2j}\operatorname{Re}(1+ie)^{2j+1}$ proves (7.1).

Infinitely many $c_j$ are nonzero. Indeed, set $\theta=\arctan e\in[0,\pi/2)$. If all sufficiently late $c_j$ vanished, two consecutive late odd angles would both have zero cosine. Their difference gives $2\theta\in\pi\mathbb Z$. In the indicated range this forces $\theta=0$, where none of the cosines vanishes, a contradiction. Some individual charges can vanish; no assertion is made that every coefficient is nontrivial.

Choose $N$ indices $j_1<\cdots<j_N$ with $c_{j_i}\ne0$. The polynomials $P_{j_i}$ have distinct degrees and are linearly independent. Hence there are distinct positive integers $k_1,\ldots,k_N$ for which the evaluation matrix $[P_{j_i}(-k_\ell^2)]$ is invertible. Otherwise their evaluation vectors on this infinite set would span a proper subspace, giving a nonzero linear combination vanishing at infinitely many points, impossible for a polynomial.

On the circle of length $2\pi$, restrict further to

$$
 u=0,\qquad p=a\sum_{\ell=1}^N b_\ell\cos(k_\ell x).
$$

The quadratic charges are $(\pi/2)\sum_\ell P_{j_i}(-k_\ell^2)b_\ell^2$. At $b_\ell=\tau\beta_\ell$ with all $\beta_\ell\ne0$, the Jacobian of the full charges is the invertible quadratic Jacobian of order $\tau$, plus $O(\tau^2)$. Its determinant has a nonzero coefficient at order $\tau^N$ and is therefore nonzero for sufficiently small nonzero $\tau$. Their differentials are independent at those data, and by continuity on a neighborhood in a sufficiently regular function space. This proves the independence assertion of the theorem.

## 8. Why a hypothesis controlling the leading Hessian matters

Dropping bulk irreducibility while retaining only invertibility of $G$ does not guarantee that the family supplied by one defect commutes. Here is an exact example with two massive free fields:

$$
 U(u)=\tfrac12|u|^2,\quad
 E=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad D=I-E,
 \quad G=\operatorname{diag}(4,8),
$$
$$
 f(w)=\tfrac12w_1^2+\tfrac14w_2^2,\qquad
 g(q)=2q_1^2+4q_2^2.                                     \tag{8.1}
$$

Equation (2.4) holds exactly, since $f''=4G^{-1}$ and $[E,U'']=0$. The family $B_\epsilon=\epsilon f+\epsilon^{-1}g$ has a unique transparent local branch and the same canonical-generating construction.

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
   +O_{\mathrm{total}}(4).                               \tag{8.2}
$$

This is an obstruction to automatic commutativity of the defect family, **not** a nonintegrable bulk counterexample: these bulk fields are free and integrable. It also explains why irreducibility of the combined bulk and defect would be the wrong substitute for hypothesis 2.

## 9. Nonempty nonlinear example and verification

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
                                                               \tag{9.1}
$$

Then $M=3I$, $g''(0)=4I$, and

$$
 [\alpha_i^T\beta_j]_{ij}
 =\begin{pmatrix}2&0&-2\\-2&2&0\\0&-2&2\end{pmatrix},
 \qquad -D\alpha_i=\beta_{i-1}
$$

with cyclic indices. Comparing the independent exponentials $e^{\alpha_i^Tw}$ proves (2.8) exactly. The potential is irreducible: an orthogonal splitting in two dimensions would require all mixed Hessian coefficients to vanish; independence of these three exponentials would force every $\alpha_i$ onto one of two perpendicular axes, which their directions exclude. This familiar $A_2^{(1)}$ example is only a consistency check, not an ingredient of the proof. For the classical Type-I context see [Bowcock–Corrigan–Zambon](https://arxiv.org/abs/hep-th/0401020).

The script `textbook_code/defect_integrability_structural/checks.py` independently checks the matrix and exponential identities, the actual quadratic charge symbols and a finite independence determinant, the first nonzero commutator in (8.2), and finite nonlinear jet coefficients for (9.1). Its output is recorded beside this proof. These finite calculations supplement the written all-orders arguments; they do not formalize or independently referee them.

## 10. What has and has not been closed

For hypotheses 1–4, every link is supplied: momentum conservation gives the split identity and rescaling family; the leading Hessian and irreducibility give its scalar normalization; the singular recursion gives a local branch satisfying the full sewing system; the defect current gives local charges; the equal-time generating functional identifies their Hamiltonian vector fields; massive locality upgrades commuting quadratic parts to exact involution; a Fourier Jacobian proves independence. Formal permutability is a conclusion.

The largest departures from the original unrestricted conjecture are the analytic massive vacuum, constant normalized Type-I kinetic coupling, absence of defect auxiliaries, derivative-free momentum correction, strong momentum identity, and transparent nondegenerate critical point. Removing these restrictions is further work. In particular, the proof of Lemma 5.1 fails for massless dispersion, and Lemma 5.2 does not exclude smooth functions flat at the vacuum.

No novelty or priority claim is made. The new material should receive an independent adversarial referee pass, especially Lemmas 5.1–5.2 and the passage from them to (6.4), before its status is promoted in the book.
