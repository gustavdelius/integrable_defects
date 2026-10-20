# A guided reading of the defect integrability paper

Companion to [*Momentum-Conserving Type-I Defects and Local Integrability near a Massive Vacuum*](defect_integrability_paper.md), corrected version of 19 October 2026.

This document explains the paper from the beginning, including the proof. It assumes familiarity with differentiation, integration, matrices, and the idea of a differential equation. It explains the field-theoretic and Hamiltonian terminology as it appears. The explanations expand the paper's argument; they are not an independent referee report. The theorem and its analytic lemmas retain the paper's status: a written proof under explicit hypotheses, awaiting independent mathematical review.

The main question is whether the existence of a suitable momentum-conserving defect forces the surrounding field theory to have infinitely many independent commuting conservation laws. The paper gives an answer for a specified class of defects near a massive vacuum. Its hypotheses and its meaning of integrability are part of the answer.

## Reading map

| Companion section | What it explains | Location in the paper |
| --- | --- | --- |
| [1](#1-the-physical-question) | Fields, defects, and the structural question | Abstract and Section 1 |
| [2](#2-the-four-assumptions) | Every hypothesis and the endpoint coordinates | Section 2 |
| [3](#3-theorem-21-sentence-by-sentence) | The theorem, including small periodic Cauchy data | Theorem 2.1 |
| [4](#4-the-calculus-used-in-the-proof) | Local functionals, variations, Poisson brackets, and formal series | Section 2 and throughout |
| [5](#5-how-momentum-conservation-creates-a-parameter) | Splitting, irreducibility, normalization, and the mass matrix | Section 3 |
| [6](#6-solving-the-sewing-equations-order-by-order) | The local Bäcklund branch and its compatibility | Section 4 |
| [7](#7-why-the-coefficients-are-conserved-and-generate-the-transformation) | Continuity equations, canonicity, and the parameter Hamiltonian | Section 5 |
| [8](#8-why-the-quadratic-part-determines-a-conserved-quantity) | The two rigidity lemmas, including the Fourier argument | Section 6 |
| [9](#9-how-quadratic-commutation-becomes-full-commutation) | Linearized generators, nonlinear involution, and permutability | Section 7 |
| [10](#10-why-there-are-infinitely-many-independent-charges) | Polynomial symbols and the Fourier Jacobian | Section 8 |
| [11](#11-what-the-reducible-example-teaches-us) | A momentum-conserving family that fails to commute | Section 9 |
| [12](#12-a-coupled-nonlinear-example) | The two-component exponential example and the checks | Section 10 |
| [13](#13-different-bulk-theories-and-other-limits) | Unequal theories, massless fields, and open extensions | Section 11 |
| [14](#14-the-spatial-hamiltonjacobi-appendix) | Spatial Hamiltonian mechanics and the geometric lemma | Appendix A |
| [15](#15-the-result-and-its-evidence) | The conclusion, verification, and reference guide | Section 12 and references |

## 1. The physical question

### A field is a collection of oscillators coupled through space

The field is a vector

$$
u(x,t)=(u_1(x,t),\ldots,u_r(x,t))\in\mathbb R^r.
$$

There is one spatial coordinate $x$ and one time coordinate $t$. At each position there are $r$ real field components. Subscripts such as $u_t$ and $u_{xx}$ mean derivatives. A prime on $U$ means differentiation with respect to its vector argument: $U'(u)$ is its gradient and $U''(u)$ its Hessian matrix.

The bulk equation is

$$
u_{tt}-u_{xx}+U'(u)=0.
$$

The term $u_{tt}$ describes acceleration. The term $u_{xx}$ couples nearby positions. The potential $U$ supplies the restoring force and nonlinear interactions. The word *bulk* refers to the ordinary field theory away from a defect.

The Lagrangian density is

$$
L=\frac12|u_t|^2-\frac12|u_x|^2-U(u).
$$

Integrating $L$ over space and time gives the action. Requiring its first variation to vanish gives the field equation. The Euclidean norm $|u|^2=u^Tu$ sums the squares of the components; a superscript $T$ denotes matrix transpose.

### What a point defect adds

Imagine cutting the spatial line at $x=0$. Call the field on the left $u$ and the field on the right $v$. A defect adds an action term at the cut, depending on the endpoint fields and their time derivatives. Variation supplies equations relating the two sides at the cut. These are the *sewing equations*.

In this paper there are no additional dynamical variables living at the defect. Its only variables are the endpoint values of $u$ and $v$. This is the relevant meaning of *Type I*. An *auto-defect* joins two copies of the same bulk theory.

A point fixed in space breaks the usual spatial translation symmetry. It is therefore a substantive condition to ask for a local defect contribution $P_d$ that makes

$$
\text{left bulk momentum}+\text{right bulk momentum}+P_d
$$

conserved. The defect can exchange momentum with the fields. The condition is that its exchange exactly balances their momentum flux.

### Why integrability enters

A field theory has infinitely many degrees of freedom. The paper's integrability conclusion supplies infinitely many independent conserved quantities that also Poisson commute. Independence means that the quantities carry different information. Poisson commutation means that the Hamiltonian motions they generate are compatible in a precise sense explained below.

The argument is *structural* because it keeps $U$ unspecified. It derives the hierarchy from properties of the defect instead of first identifying $U$ as a member of a known list of integrable models.

Several steps are needed. The sewing equations must produce a local parameter family. The coefficients of that family must yield conserved quantities. Those quantities must commute and be independent. The paper establishes each of these statements separately.

The resulting hierarchy belongs to the homogeneous bulk equation. A separate problem would be to put a fixed defect back into that equation and give every higher charge a defect correction. The theorem does not solve that separate problem.

## 2. The four assumptions

### Assumption 1: an analytic massive vacuum

The conditions are

$$
U(0)=0,\qquad U'(0)=0,\qquad M=U''(0)>0.
$$

The equation $U'(0)=0$ says that the constant field $u=0$ is an equilibrium, called the *vacuum*. The equation $U(0)=0$ fixes an irrelevant additive energy constant. The notation $M>0$ means that the real symmetric matrix $M$ is positive definite: $a^TMa>0$ for every nonzero real vector $a$.

Near the vacuum,

$$
U(u)=\frac12u^TMu+\text{terms of degree at least three}.
$$

After an orthogonal change of components, the eigenvalues of $M$ are $m_a^2>0$. Linearizing the field equation gives independent Klein–Gordon equations

$$
(u_a)_{tt}-(u_a)_{xx}+m_a^2u_a=0.
$$

These $m_a$ are the masses of the linearized modes. Every mass must be strictly positive. This will matter in the Fourier argument, not just in the interpretation of the vacuum as stable to linear perturbations.

*Real analytic* means that $U$ equals its convergent Taylor series in a neighborhood of zero. Smoothness alone would allow functions whose derivatives of every order vanish at zero while the functions themselves are nonzero nearby. The proof later needs to exclude that possibility. The hypothesis is local in field space and makes no assertion about the potential far from the vacuum.

### Assumption 2: the bulk does not split into independent theories

The paper assumes that no orthogonal change of field components makes

$$
U(u)=U_1(u_1)+U_2(u_2)
$$

on two nonzero mutually orthogonal groups of components near zero. Such a decomposition would also split the kinetic terms, so the bulk would be two independent field theories. *Irreducible* means that this decomposition is impossible.

Orthogonality matters because the kinetic terms use the Euclidean inner product. An arbitrary nonlinear change of fields would usually change those kinetic terms.

The paper refers to the *germ* of $U$: only its values in some neighborhood of zero matter. It also emphasizes bulk irreducibility. A defect could mix two fields whose bulk equations are independent; that mixing would not satisfy this assumption.

There is a precise reason for imposing it. The proof will derive a matrix $G$ and show that it commutes with every Hessian $U''(w)$. Irreducibility then forces $G$ to be a scalar matrix. One can replace this entire assumption by imposing that scalar condition directly.

### Assumption 3: a particular constant Type-I coupling

The defect action density is

$$
L_d=\frac12u^TEu_t+u^TDv_t+\frac12v^TEv_t-B(u,v),
\qquad E^T=-E,\qquad D=I-E.
$$

Here $I$ is the identity matrix. The constant matrix $E$ is skew-symmetric. The first three terms are linear in time derivatives and determine how the endpoint fields are coupled. The analytic function $B$ is the defect energy.

The word *normalized* specifies this actual form of the coupling. The same coordinates must also identify the bulk theories and the diagonal $u=v$. The paper does not assume that every possible Type-I defect admits all these normalizations simultaneously.

The defect momentum $P_d(u,v)$ is *derivative-free*: it depends on endpoint field values but not on their time or spatial derivatives. Its time derivative therefore has the form

$$
\frac{dP_d}{dt}=(P_d)_u^Tu_t+(P_d)_v^Tv_t.
$$

The momentum identity is *strong*. After using the sewing equations to remove $u_x$ and $v_x$, it must hold for independent nearby values of $u,v,u_t,v_t$. It is an identity in these variables, rather than an equality tested only on one special solution. That is what permits the proof to equate coefficients of the endpoint velocities.

### The coordinates used in assumption 4

The proof replaces $(u,v)$ by

$$
q=\frac{u-v}{2},\qquad
w=\frac{D^Tu+Dv}{2}.
$$

The vector $q$ measures the difference between the two fields. The vector $w$ is a modified average. When $E=0$, it is the ordinary average $(u+v)/2$. The inverse transformation is

$$
u=w+Dq,\qquad v=w-D^Tq.
$$

Thus $w$ and $q$ can be varied independently. At $q=0$, both fields equal $w$. These coordinates are useful because momentum balance separates into a condition involving $w$ and a condition involving $q$.

### Assumption 4: a transparent nondegenerate critical manifold

Regard $B$ as a function of $(w,q)$. The conditions are

$$
B_q(w,0)=0\quad\text{for every nearby }w,
\qquad G=B_{qq}(0,0)\text{ invertible}.
$$

The first says that when the fields agree, the derivative of the defect energy in the difference direction is zero. It holds along the whole nearby diagonal. It does not require $B_w(w,0)=0$ for every $w$: this is a critical condition in the $q$ directions.

*Nondegenerate* means that the linear response in those directions can be inverted. The eigenvalues of $G$ must be nonzero; positivity of $G$ is not an initial assumption.

Momentum balance will imply

$$
B(w,q)=f(w)+g(q).
$$

The condition then becomes $g'(0)=0$, $g''(0)=G$ invertible. After rescaling, $g''(0)=4I$. This invertible linear term makes it possible to solve recursively for a branch with $q\to0$ as the parameter tends to zero. That is the transparency used in the proof: the formal transformation tends to $v=u$. The word does not assert that every finite-parameter scattering problem has already been solved.

## 3. Theorem 2.1 sentence by sentence

### The parameter family and its branch

The first sentence says:

> Under hypotheses 1–4, the momentum identity supplies a rescaled family of defects with a unique formal local branch $T_\epsilon=\mathrm{Id}+O(\epsilon)$.

Start with one suitable defect. Momentum conservation forces a split $B=f(w)+g(q)$ whose remaining constraint involves the product of derivatives of $f$ and $g$. Multiplying $f$ by a nonzero parameter and $g$ by its reciprocal preserves the constraint. After a convenient normalization the family is

$$
B_\epsilon=\epsilon U(w)+\epsilon^{-1}g(q).
$$

We now impose the sewing equations throughout space. Given a bulk solution $u$, they define a second formal solution $v=T_\epsilon u$. This is a Bäcklund transformation. On initial data it is a transformation of the pair $(u,p)$, where $p=u_t$; the notation $T_\epsilon u$ suppresses that dependence on the velocity.

The condition $T_\epsilon=\mathrm{Id}+O(\epsilon)$ selects the branch whose constant term is $v=u$. In fact,

$$
v=u+\epsilon(u_x-u_t)+O(\epsilon^2).
$$

*Formal* means that the equations hold coefficient by coefficient in a power series in $\epsilon$. No convergence of the infinite series is claimed. *Local* means that each coefficient uses only finitely many derivatives at the same position. *Unique* means that, once the identity constant term is selected, every coefficient is determined. Other solutions of the full sewing equations are not excluded.

### The defect-energy expansion

The next sentence includes the formula

$$
I(\epsilon)=\int B_\epsilon(u,T_\epsilon u)\,dx
=\sum_{n\geq1}\epsilon^n I_n.
$$

Substitute the transformed field into the defect energy and integrate over space. The resulting expression is a formal generating series for the functionals $I_n$.

There is a useful distinction in the wording. An actual point defect stores energy $B_\epsilon$ at one position. Here the same expression is evaluated on a transformation imposed throughout space and then integrated. Thus $I(\epsilon)$ is a bulk functional built from the defect-energy expression.

Why does no negative or constant power survive? Along the selected branch $q=O(\epsilon)$. Since $g(0)=g'(0)=0$, the term $\epsilon^{-1}g(q)$ is $O(\epsilon)$. The term $\epsilon U(w)$ is also $O(\epsilon)$.

Using $g(q)=2|q|^2+O(|q|^3)$ and $q=\epsilon(p-u_x)/2+O(\epsilon^2)$ gives

$$
I_1=\int\left[\frac12|p-u_x|^2+U(u)\right]dx.
$$

With the paper's physical momentum convention $P_{\rm bulk}=-\int p^Tu_x\,dx$, this is $H+P_{\rm bulk}$. The hierarchy begins with a familiar combination of energy and momentum.

### Analytic finite-jet local conserved functionals

The next sentence describes every coefficient $I_n$ this way. Concretely,

$$
I_n[u,p]=\int\rho_n(u,p,u_x,p_x,\ldots,
\partial_x^{N_n}u,\partial_x^{N_n}p)\,dx.
$$

A *functional* takes field data as input and returns a number. Its density is *local* because the arguments at position $x$ are all evaluated at that same position. A *jet* is a collection of field values and derivatives; *finite-jet* means that only finitely many occur for each $n$. The necessary derivative order may increase with $n$.

*Analytic* refers to the density as a function of these finitely many jet variables near zero. Its Taylor expansion in those variables converges locally. This is a different expansion from the formal parameter series in $\epsilon$.

*Conserved* means $dI_n/dt=0$ on bulk solutions with boundary conditions eliminating flux through the ends. The proof gives a local continuity equation for each density, which can then be integrated.

### Poisson commutation

The next sentence says that all $I_n$ Poisson commute for the canonical equal-time bracket:

$$
\{I_n,I_m\}=0.
$$

At one fixed time, treat $u(x)$ and $p(x)$ as the coordinates on the space of field configurations and velocities. The Poisson bracket measures the change of one functional under the Hamiltonian motion generated by the other. Thus every charge is preserved by the flows generated by all the other charges.

Conservation under the physical Hamiltonian $H$ says $\{I_n,H\}=0$. Mutual commutation requires the additional equalities with every $I_m$. The proof has a separate argument for them.

### Functional independence and small periodic Cauchy data

The next sentence is:

> Infinitely many are functionally independent: for every $N$ there are $N$ members whose differentials are independent at arbitrarily small periodic Cauchy data.

An arbitrary number of conserved expressions need not contain an arbitrary amount of information. The powers $H,H^2,H^3,\ldots$ are conserved, but all their values are determined by $H$. Their differentials are proportional to $dH$.

For selected charges $I_{n_1},\ldots,I_{n_N}$, independence at given data means

$$
\sum_{i=1}^N c_i\,dI_{n_i}=0
\quad\Longrightarrow\quad c_1=\cdots=c_N=0.
$$

Each differential describes the first-order change of a charge under variations of the fields and their velocities. Independence means that suitable variations can change the selected charges independently to first order.

*Cauchy data* are the initial conditions

$$
u(x,t_0)=u_0(x),\qquad u_t(x,t_0)=p_0(x).
$$

Both functions are needed because the equation is second order in time. *Periodic* means periodic in $x$, with some common period $L$. We are placing the bulk field on a spatial circle. The time evolution is not assumed periodic.

*Arbitrarily small* means that the independent differentials can be found as close as desired to the zero initial data. The proof uses a finite Fourier sum

$$
u_0=0,\qquad
p_0(x)=\tau a\sum_{\ell=1}^N\beta_\ell\cos(k_\ell x)
$$

on a circle of length $2\pi$. Here $a$ is a fixed direction in field space, the $k_\ell$ are selected positive integer frequencies, and the $\beta_\ell$ are nonzero real numbers. The parameter $\tau$ scales the amplitudes. For fixed frequencies, taking $\tau\to0$ makes the data and every fixed number of their derivatives tend to zero.

At the exact vacuum the charge differentials vanish, so independence fails there. The theorem supplies data with independence in every neighborhood of the vacuum. The choices of charges, frequencies, and neighborhood can depend on $N$.

Periodicity is convenient for three reasons. Integrated spatial derivatives vanish. Smooth Fourier modes are admissible finite-energy configurations on the circle. Their orthogonality turns independence into an explicit finite matrix calculation. The local conservation laws themselves also apply on the line with suitable decay. The paper's independence argument is carried out on the circle.

### Commuting formal transformations

The last sentence of the main paragraph says

$$
T_\epsilon T_\eta=T_\eta T_\epsilon.
$$

Apply one Bäcklund transformation and then another with a different parameter. The resulting formal field is independent of their order. This is *formal Bianchi permutability*. The paper derives it from the commuting charges. It is an equality of two-parameter formal series and does not assert the existence of globally defined finite-parameter maps.

### The qualification immediately after the theorem

Bulk irreducibility can be replaced by $G=\gamma I$ with $\gamma\ne0$. Irreducibility is used to derive exactly that condition. This gives a version of the theorem covering some reducible potentials as well.

The paper defines *local integrability* by its demonstrated hierarchy and finite-subfamily independence. It does not claim convergence of the Bäcklund series, completeness of action variables, or a general solution formula for every initial condition.

## 4. The calculus used in the proof

### Functionals that differ by a spatial derivative

For periodic data or suitable decay,

$$
\int D_x h\,dx=0.
$$

Consequently two densities differing by a total derivative represent the same functional. This is the meaning of *modulo spatial derivatives*. For instance,

$$
\int u^Tu_{xx}\,dx=-\int|u_x|^2\,dx.
$$

A density can look nonzero and contain high derivatives while its functional is zero. The proof must therefore establish independence of functionals after allowing integration by parts. Counting the highest derivative appearing in a chosen density would not suffice.

### Variational derivatives

For a functional $F$, vary the fields and integrate by parts until no derivative acts on the variations:

$$
\delta F=\int\left(F_u^T\delta u+F_p^T\delta p\right)dx.
$$

The coefficients $F_u,F_p$ are the variational derivatives. They include the integrations by parts. For the bulk energy,

$$
H=\int\left(\frac12|p|^2+\frac12|u_x|^2+U(u)\right)dx,
$$

they are $H_p=p$ and $H_u=-u_{xx}+U'(u)$. More generally the contribution from dependence on $u, u_x, u_{xx},\ldots$ is the alternating sum

$$
F_u=\sum_{j\geq0}(-D_x)^j
\frac{\partial\rho}{\partial(\partial_x^j u)},
$$

with only finitely many terms. These are also called Euler derivatives.

### Hamiltonian vector fields and the equal-time bracket

The canonical symplectic form and Poisson bracket are

$$
\Omega=\int\delta u^T\wedge\delta p\,dx,
\qquad
\{F,G\}=\int(F_u^TG_p-F_p^TG_u)\,dx.
$$

The wedge makes the form antisymmetric in two variations. With the paper's convention, the Hamiltonian vector field generated by $F$ is

$$
X_F=(F_p,-F_u).
$$

For $F=H$, this gives $u_t=p$, $p_t=u_{xx}-U'(u)$, exactly the bulk equation. Along the flow generated by $G$, the change of $F$ is $\{F,G\}$.

A *canonical* transformation preserves $\Omega$, equivalently the canonical bracket. It preserves the Hamiltonian structure of phase space. This property alone does not say that two different canonical transformations commute.

### Total derivatives and two distinct expansions

The symbol $D_x$ differentiates any expression depending on fields and their spatial derivatives, using the chain rule. The symbol $D_t$ does the same along a bulk solution, replacing $u_t$ by $p$ and $p_t$ by $u_{xx}-U'(u)$. Thus

$$
D_tu=p,\qquad D_tp=u_{xx}-U'(u),\qquad D_tD_x=D_xD_t.
$$

The proof uses two different order counts. In the Bäcklund expansion, $\epsilon$ counts the parameter order and the fields are kept nonlinear. In an amplitude expansion, replace every field and every one of its derivatives by $\tau$ times itself. Then $u^2$, $p^2$, and $u_x^2$ all have amplitude degree two. A derivative does not increase amplitude degree.

The notation $F^{(2)}$ means the quadratic amplitude part of a functional. It is not the coefficient $I_2$ of the Bäcklund parameter. Keeping these two expansions separate is essential to Sections 6–8 of the paper.

## 5. How momentum conservation creates a parameter

### From the action to the sewing equations

Varying the bulk actions leaves endpoint terms at the cut. Varying the defect action supplies further endpoint terms. Requiring their sum to vanish for arbitrary variations gives

$$
u_x=Eu_t+Dv_t-B_u,
\qquad
v_x=D^Tu_t-Ev_t+B_v.
$$

These equations tell us how the spatial slopes at the two endpoints depend on the endpoint velocities and the defect potential. They are the starting point of Proposition 3.1.

With physical momentum $-\int p^Tu_x\,dx$, the relevant bulk momentum flux is

$$
T^{11}(u)=\frac12\bigl(|u_t|^2+|u_x|^2\bigr)-U(u).
$$

Conservation of total momentum requires

$$
D_tP_d=T^{11}(u)-T^{11}(v).
$$

The left-hand side is linear in $u_t,v_t$ because $P_d$ contains no derivatives. Substitute the sewing equations into the right-hand side. The terms quadratic in the velocities cancel, using $DD^T=I-E^2$ and $ED=DE$. Equating the remaining velocity coefficients and the velocity-independent term gives

$$
(P_d)_u=EB_u-DB_v,\qquad
(P_d)_v=-D^TB_u-EB_v,
$$

$$
\frac12\left(|B_u|^2-|B_v|^2\right)=U(u)-U(v).
$$

This is where the strong identity assumption is used. The coefficients can be equated because the endpoint velocities are independent variables.

### Why the potential has to split

In the coordinates $(w,q)$, the first two equations simplify to

$$
(P_d)_w=-B_w,\qquad (P_d)_q=B_q.
$$

Differentiate the first equation with respect to $q$, and the second with respect to $w$. Mixed derivatives of $P_d$ agree, whereas the displayed signs are opposite. Hence $B_{wq}=0$.

Vanishing mixed derivatives mean that the dependence on $w$ and $q$ separates locally:

$$
B=f(w)+g(q),\qquad P_d=-f(w)+g(q),
$$

up to constants fixed at the vacuum. The final momentum constraint becomes

$$
U(w+Dq)-U(w-D^Tq)=\frac12f'(w)^Tg'(q).
$$

This equation has a useful interpretation. The difference of the two bulk potentials must factor, in these coordinates, as a pairing of a function of the average variable and a function of the difference variable. That is a strong restriction on the possible $U$ and defect.

The calculation also runs backwards: this splitting and potential identity imply the strong momentum balance. Proposition 3.1 gives an equivalent local formulation of that balance within the specified coupling class.

### Why irreducibility forces one scalar normalization

Differentiate the potential identity with respect to $q$ at $q=0$. The left side gives $2U'(w)$ because $D+D^T=2I$. The right side gives $Gf'(w)/2$, so

$$
Gf'(w)=4U'(w).
$$

Since $G$ is invertible, differentiating with respect to $w$ gives $f''=4G^{-1}U''$. A Hessian is symmetric. Taking the transpose therefore requires $G^{-1}U''=U''G^{-1}$, or

$$
[G,U''(w)]=0.
$$

Here $[A,B]=AB-BA$ denotes a commutator. Choose orthogonal coordinates in which the symmetric matrix $G$ is diagonal, with entries $\gamma_i$. The $(i,j)$ entry of this equation reads

$$
(\gamma_i-\gamma_j)\,U_{ij}(w)=0.
$$

If two eigenvalues differ, all mixed second derivatives of $U$ between their eigenspaces vanish. The potential then splits into a sum over those eigenspaces. Bulk irreducibility excludes such a split. All eigenvalues must consequently agree:

$$
G=\gamma I,\qquad \gamma\ne0.
$$

The earlier gradient identity now integrates to $f=4U/\gamma$, after fixing the constant. This explains exactly what irreducibility contributes. It removes the possibility of different leading defect responses in different field directions.

### Reciprocal rescaling

The product $f'(w)^Tg'(q)$ is unchanged when $f$ is multiplied by $\lambda$ and $g$ by $\lambda^{-1}$. Thus the momentum identity generates a parameter family. Write $\epsilon=4\lambda/\gamma$ and absorb the factor $4/\gamma$ into the definition of $g$. The normalized result is

$$
B_\epsilon=\epsilon U(w)+\epsilon^{-1}g(q),
\qquad P_\epsilon=-\epsilon U(w)+\epsilon^{-1}g(q),
$$

$$
g(0)=0,\qquad g'(0)=0,\qquad g''(0)=4I,
$$

$$
U(w+Dq)-U(w-D^Tq)=\frac12U'(w)^Tg'(q).
$$

The paper reuses the symbol $g$ for this normalized function. This is a change of normalization, not an additional assumption.

### Why the kinetic matrix commutes with the masses

Set $w=0$ in the normalized potential identity and retain terms quadratic in $q$. Since $U'(0)=0$, the right-hand side vanishes. The left side requires

$$
D^TMD=DMD^T.
$$

Substituting $D=I-E$ shows that the difference of these matrices is $2(EM-ME)$. Therefore $[E,M]=0$.

This says that the defect's skew coupling preserves the mass eigenspaces. Later it lets the linearized transformation be written using mutually commuting operators. Proposition 3.2 has thus obtained both the parameter family and an algebraic compatibility with the free bulk evolution.

## 6. Solving the sewing equations order by order

### Two useful derivative combinations

Define

$$
D_+=D_t+D_x,\qquad D_-=D_t-D_x.
$$

Their product is $D_t^2-D_x^2$, the wave operator. In the $(w,q)$ coordinates the sewing equations become

$$
D_+q=-\frac{\epsilon}{2}U'(w),
\qquad
D_-w=\frac{1}{2\epsilon}g'(q).
$$

These are often called chiral combinations because $D_+$ and $D_-$ differentiate along the two characteristic directions of the wave equation. The symbol $D$ without a subscript remains the constant matrix $I-E$; it is not one of these derivatives.

### A differential equation becomes an algebraic recursion

Use $w=u-Dq$ in the second equation:

$$
g'(q)=2\epsilon D_-u-2\epsilon D D_-q.
$$

Seek a series $q=\epsilon q_1+\epsilon^2q_2+\cdots$. Since $g'(q)=4q+O(q^2)$, the coefficient of order $\epsilon$ is

$$
4q_1=2D_-u=2(p-u_x).
$$

At the next order the new unknown appears as $4q_2$. All other terms involve the already known $q_1$. At every later order the same pattern holds: $4q_n$ is determined by earlier coefficients.

The derivative of $q$ on the right is multiplied by $\epsilon$, so at order $n$ it differentiates $q_{n-1}$, not $q_n$. We never need to integrate a differential equation for the new coefficient. We differentiate expressions already obtained and divide by $4$.

This explains existence, uniqueness, and locality simultaneously. Each finite stage uses finitely many differentiations and analytic functions of the fields. The first term gives $v=u-2q=u+\epsilon(u_x-p)+O(\epsilon^2)$.

### Why solving one sewing equation suffices here

There are two sewing equations, so a recursion solving only the second would leave a compatibility problem. The proof addresses it explicitly.

Let

$$
A=D_+q+\frac{\epsilon}{2}U'(w).
$$

This is the error in the first equation. The desired statement is $A=0$.

Differentiate the normalized potential identity with respect to $w$ and $q$, and combine the resulting equations. One obtains

$$
U'(u)=\frac14\left[g''(q)U'(w)+D U''(w)g'(q)\right].
$$

Now differentiate $u=w+Dq$ using the equation already solved. Substitution of the displayed identity gives the exact residual relation

$$
D_+D_-u+U'(u)
=\left(D D_-+\frac{1}{2\epsilon}g''(q)\right)A.
$$

The left side is zero because $u$ solves the bulk equation. The operator on the right begins with $2\epsilon^{-1}I$, because $g''(0)=4I$ and $q=O(\epsilon)$.

Suppose $A$ had a first nonzero coefficient, say $\epsilon^sA_s$. The right side would then have first term $2\epsilon^{s-1}A_s$. Every other contribution has a higher power of $\epsilon$, so nothing could cancel it. This contradicts the vanishing left side. Thus $A$ is zero coefficient by coefficient.

This argument concerns formal series with a lowest power. It uses an invertible leading coefficient. It does not assume that differentiation has no kernel; constant functions, for example, are in the kernel of differentiation.

### Why the transformed field solves the bulk equation

The other combination of derivatives of the potential identity gives

$$
U'(v)=\frac14\left[g''(q)U'(w)-D^TU''(w)g'(q)\right].
$$

Apply $D_+D_-$ to $v=w-D^Tq$ and use both sewing equations. The result is the negative of this expression, so $D_+D_-v+U'(v)=0$.

The transformation therefore takes solutions to formal solutions of the same equation. On Cauchy data it is

$$
T_\epsilon:(u,p)\longmapsto(v,D_tv).
$$

It *intertwines* evolution: evolving the input and then transforming agrees, coefficient by coefficient, with transforming and then evolving the output. It fixes the zero solution. A formal map with identity constant term also has a unique formal inverse, found by recursively cancelling successive powers of $\epsilon$.

## 7. Why the coefficients are conserved and generate the transformation

### A continuity equation from the two sewing equations

Differentiate the defect energy and momentum expressions:

$$
D_tB_\epsilon+D_xP_\epsilon
=\epsilon U'(w)^TD_-w
+\epsilon^{-1}g'(q)^TD_+q.
$$

The second sewing equation makes the first term $U'(w)^Tg'(q)/2$. The first sewing equation makes the second term its negative. They cancel exactly.

After substituting the local branch, expand both densities in $\epsilon$. If their order-$n$ coefficients are $\rho_n$ and $j_n$, the identity reads

$$
D_t\rho_n+D_xj_n=0.
$$

Integrating over a circle or the line with adequate decay proves conservation of $I_n=\int\rho_n\,dx$. This proves conservation at every order, keeping the full nonlinear field dependence in each coefficient.

### A generating functional at fixed time

For independent endpoint fields $u(x),v(x)$ at one time, define

$$
F_\epsilon[u,v]
=\int\left[2q^Tw_x+P_\epsilon(w,q)\right]dx.
$$

The first term is a spatial kinetic term. Up to a total spatial derivative it equals

$$
\frac12u^TEu_x+u^TDv_x+\frac12v^TEv_x.
$$

Replacing a density by an equivalent one modulo a derivative does not change its functional or variational derivatives under the stated boundary conditions. The form $2q^Tw_x$ makes the calculation shorter.

Vary $F_\epsilon$ and integrate the $\delta w_x$ term by parts. This gives

$$
\delta F_\epsilon
=\int\left[
(-2q_x-\epsilon U'(w))^T\delta w
+(2w_x+\epsilon^{-1}g'(q))^T\delta q
\right]dx.
$$

Put $p=u_t$ and $P=v_t$. Here the capital $P$ without a subscript is the right field's canonical momentum; it is different from the defect momentum $P_\epsilon$. The sewing equations identify the two coefficients as $p-P$ and $D^Tp+DP$. Substituting the variations of $u=w+Dq$ and $v=w-D^Tq$ yields

$$
\delta F_\epsilon=\int(p^T\delta u-P^T\delta v)\,dx.
$$

This is the familiar structure of a canonical generating function: differentiating with respect to the old position gives its momentum, and differentiating with respect to the new position gives minus its momentum.

### Why this proves canonicity

Take another exterior derivative. The second derivative of the functional itself is zero, so the old and new symplectic forms agree on the transformation's graph:

$$
T_\epsilon^*\Omega=\Omega.
$$

The star denotes *pullback*: evaluate the output symplectic form on the variations induced by changing the input. This is equal-time canonicity because all the integrals here are over $x$ at one fixed $t$.

The parameter changes the transformation, so it gives another direction of motion in phase space besides physical time evolution. The next step identifies the Hamiltonian generating that parameter motion.

### Differentiate the generating functional with respect to the parameter

Hold $u$ and $v$ fixed while differentiating $F_\epsilon$. Only $P_\epsilon=-\epsilon U+\epsilon^{-1}g$ depends explicitly on $\epsilon$, and therefore

$$
\epsilon\,\partial_\epsilon F_\epsilon
=-\int B_\epsilon\,dx.
$$

It is important that this is a partial derivative at fixed endpoints. If one first substituted $v=T_\epsilon u$ and took a total derivative, extra terms would arise from the variation of $v$.

The source parameter velocity is

$$
W_\epsilon=(DT_\epsilon)^{-1}\partial_\epsilon T_\epsilon.
$$

Here $DT_\epsilon$ means the derivative of the map on phase space; it is not the matrix $D=I-E$. Changing $\epsilon$ at a fixed input produces a vector at the output. Applying the inverse tangent map moves that vector back to the input phase space. That is the meaning of *source* velocity.

The generating-function identity gives

$$
W_\epsilon=X_{K_\epsilon},\qquad
K_\epsilon=-\frac{I(\epsilon)}{\epsilon}
=-\sum_{n\geq1}\epsilon^{n-1}I_n.
$$

Thus the very same conserved quantities obtained from defect energy generate the infinitesimal parameter motion. This connection is what makes their quadratic parts accessible from the linearized transformation.

### The differential-form calculation behind the sign

For readers following every step of Proposition 5.1, put $\theta=\int p^T\delta u\,dx$, so $d\theta=-\Omega$. Let $\widehat F$ denote $F_\epsilon$ evaluated on the transformation's graph. The endpoint variation says

$$
d\widehat F=\theta-T_\epsilon^*\theta.
$$

Write $V=(\partial_\epsilon T)\circ T^{-1}$ for the parameter velocity at the output. The total parameter derivative of $\widehat F$ is its explicit partial derivative minus $T^*(\iota_V\theta)$, because the derivative with respect to the right endpoint in the generating formula is minus its momentum. The symbol $\iota_V$ means inserting the vector $V$ into a differential form.

Differentiate the displayed identity and use Cartan's formula $\mathcal L_V\theta=\iota_Vd\theta+d(\iota_V\theta)$. The terms differentiating $T^*(\iota_V\theta)$ occur on both sides and cancel. What remains is

$$
d\bigl[(\partial_\epsilon F_\epsilon)\circ\operatorname{graph}T\bigr]
=T^*(\iota_V\Omega)=\iota_{W_\epsilon}\Omega.
$$

The last equality uses canonicity. Since the explicit partial derivative evaluated on the graph is $-I(\epsilon)/\epsilon$, this proves the asserted Hamiltonian and its minus sign. The differential-form notation packages the endpoint chain rule and the preservation of the symplectic form.

## 8. Why the quadratic part determines a conserved quantity

### The claim and why it is useful

Section 6 proves the paper's central rigidity statement: a vacuum-normalized analytic local conserved functional is determined by its quadratic amplitude part.

Suppose two such conserved functionals have the same quadratic part. Subtract them. Their difference is conserved and has no constant, linear, or quadratic term. The lemma says that this difference must be zero as a functional.

This is a uniqueness statement. It does not say that every conceivable quadratic expression extends to a nonlinear conserved quantity. Nor does it say that a nonlinear conserved quantity has no higher terms. Those higher terms, when they exist within this class, are fixed by its quadratic part.

The proof proceeds in two stages. First it studies homogeneous polynomial local functionals of the free massive theory. Then it uses the lowest amplitude degree to control the nonlinear analytic theory.

### Free massive fields as Fourier oscillators

After diagonalizing $M$, each Fourier mode of species $a$ has frequency

$$
\omega_a(k)=\sqrt{k^2+m_a^2}.
$$

The label $a$ identifies the field component with mass $m_a$, and $k$ is spatial Fourier momentum. A Fourier transform expresses a field as a superposition of waves $e^{ikx}$. Spatial differentiation becomes multiplication by $ik$.

For a fixed $a,k$, the free equations are a harmonic oscillator. Introduce amplitudes of the two time directions by

$$
\widehat u_a=a_{a,+}+a_{a,-},\qquad
\widehat p_a=i\omega_a(a_{a,+}-a_{a,-}).
$$

Then

$$
\dot a_{a,\sigma}=i\sigma\omega_a(k)a_{a,\sigma},
\qquad \sigma=+1\text{ or }-1.
$$

Thus each amplitude simply picks up a phase $e^{i\sigma\omega_a t}$. The hat denotes the Fourier transform. Complex amplitudes are an algebraic convenience: the original conservation identity is polynomial, so an identity for all real data can be complexified and its components compared independently.

### How a local polynomial looks in Fourier space

Take a homogeneous functional of amplitude degree $n$. Each monomial in its density contains $n$ field or momentum factors, possibly differentiated. It is useful to *polarize* it: replace its repeated input by $n$ independent inputs and keep the symmetric part multilinear in them. For example, a cubic expression can be recovered from the coefficient of $s_1s_2s_3$ after inserting $s_1u^{(1)}+s_2u^{(2)}+s_3u^{(3)}$.

Polarization lets us vary the waves in all $n$ slots independently. Their spatial factors multiply to

$$
e^{ik_1x}\cdots e^{ik_nx}=e^{i(k_1+\cdots+k_n)x}.
$$

Integration over $x$ produces the Fourier constraint

$$
k_1+\cdots+k_n=0.
$$

In the Fourier kernel this is represented by a delta distribution. Apart from that single constraint, the coefficient is a polynomial in the momenta before the change to oscillator amplitudes. The reason is locality and finite differential order: each derivative supplies a factor $ik_j$, and there are only finitely many derivatives.

After changing to $a_{a,\sigma}$, the coefficients may contain the square roots $\omega_a(k)$, but they are real analytic for real $k$ because the masses are positive. Write one such coefficient as $A(k_1,\ldots,k_n)$ for fixed choices of species and signs.

### Conservation becomes a frequency condition

The product of $n$ oscillator amplitudes acquires the time phase

$$
\exp(i\Phi t),\qquad
\Phi=\sum_{j=1}^n\sigma_j\omega_{a_j}(k_j).
$$

For the functional to be conserved for arbitrary wave packets, its coefficient must satisfy

$$
\Phi A=0
\quad\text{on }k_1+\cdots+k_n=0.
$$

This says that a coefficient could contribute only where the signed frequencies cancel. Such momentum configurations are called resonant.

The decisive question is whether that cancellation can persist on an open set of the independent momenta. Eliminate $k_n$ by setting $k_n=-\sum_{j<n}k_j$. When $n\geq3$, at least two independent momenta remain. Differentiate with respect to $k_1$ and $k_2$:

$$
\frac{\partial^2\Phi}{\partial k_1\partial k_2}
=\frac{\sigma_n m_{a_n}^2}
{(k_n^2+m_{a_n}^2)^{3/2}}\ne0.
$$

Every frequency except the last depends on at most one of these variables, so its mixed derivative is zero. The last frequency depends on their sum and has strictly nonzero curvature because $m_{a_n}>0$.

Consequently $\Phi$ cannot vanish on any open set. Wherever $\Phi\ne0$, the equation $\Phi A=0$ forces $A=0$. Those points are dense, and continuity then forces $A=0$ also at the resonant points.

Resonant configurations can exist. The point is that a local density gives an ordinary analytic coefficient, which cannot be nonzero only on a set with empty interior. A distribution concentrated on that set would have a different kind of kernel and would not come from the stipulated finite-derivative local density.

### Why a vanishing kernel means a total spatial derivative

Return from oscillator amplitudes to the original $u,p$ variables. Their polynomial kernels vanish whenever $k_1+\cdots+k_n=0$. A polynomial vanishing on that hyperplane has the factor $k_1+\cdots+k_n$.

One can see this directly by dividing the polynomial by $k_n+\sum_{j<n}k_j$, treating $k_n$ as the division variable. The remainder is independent of $k_n$. Substitution of $k_n=-\sum_{j<n}k_j$ makes the remainder zero, so the division has no remainder.

In Fourier space a total derivative of a product multiplies its kernel by $i(k_1+\cdots+k_n)$. The polynomial factor therefore means that the original density is a total spatial derivative. Symmetrizing the quotient recovers the symmetry used in polarization.

The functional is consequently zero under the boundary conditions used in the paper. This finishes the degree-$n\geq3$ part of Lemma 6.1.

### What happens at degrees one and two

A linear local functional reduces by integration by parts to

$$
F=\int(a^Tu+b^Tp)\,dx
$$

for constant vectors $a,b$. Along the free evolution its derivative is $\int(a^Tp-b^TMu)\,dx$. Independent choices of $u,p$ and invertibility of $M$ force $a=b=0$.

Quadratic conserved functionals do exist, including energy and momentum. At degree two there is only one independent Fourier momentum after imposing $k_1+k_2=0$. For the same species with opposite frequency signs, $\omega_a(k_1)-\omega_a(-k_1)=0$ identically. The mixed-derivative obstruction used above is unavailable. This is precisely where nontrivial local conservation can survive.

The assumptions of no explicit $x$ or $t$ dependence are part of the lemma. Functionals with coordinate-dependent weights are outside its statement.

### From the free theory to the nonlinear theory

Expand a conserved functional and the Hamiltonian by amplitude:

$$
F=F^{(n)}+F^{(n+1)}+\cdots,\qquad
H=H^{(2)}+H^{(3)}+\cdots,
$$

where $n\geq3$ is the first nonzero degree of $F$, if such a degree exists. A variational derivative reduces amplitude degree by one. Thus the bracket of a term of degree $r$ with one of degree $s$ has degree $r+s-2$.

At the lowest degree $n$, conservation $\{F,H\}=0$ therefore gives

$$
\{F^{(n)},H^{(2)}\}=0.
$$

The nonlinear terms of $H$ enter only at higher degree. The leading term of $F$ must consequently be conserved by the free massive theory. Lemma 6.1 says that such a homogeneous term is a total derivative, contradicting its being the first nonzero functional.

Applying this argument successively shows that every amplitude coefficient is zero as a functional. The argument takes place modulo spatial derivatives. A lower-degree density that is a nonzero total derivative contributes no variational derivative and hence no Poisson bracket.

### Where analyticity is needed

Vanishing of all Taylor coefficients by itself is enough for a formal amplitude series. To conclude that an actual analytic local functional vanishes near the vacuum, the proof uses its Euler derivatives.

The density has finitely many jet arguments, so its Euler derivatives are analytic functions of finitely many, possibly more, jet arguments. Every Taylor coefficient of those Euler derivatives vanishes. Analyticity makes the Euler derivatives themselves zero near zero.

Now vary the data along the path $(u,p)\mapsto s(u,p)$, $0\leq s\leq1$. The derivative of the functional along this path is an integral of its Euler derivatives against $u,p$, after integration by parts. It is zero. The functional therefore equals its value at the vacuum, which was normalized to zero.

A conserved analytic local functional also has zero linear part, by the degree-one free argument. This completes the assertion that the quadratic part determines every vacuum-normalized functional in the specified class.

### Why powers of the energy do not contradict the lemma

The expression $H^2$ is conserved and starts at amplitude degree four. But it is a product of integrals:

$$
H^2=\int\!\int h(x)h(y)\,dx\,dy.
$$

It is not a single integral of a density depending only on finitely many fields and derivatives at one point. Its variational derivative contains the global number $H$. The locality assumption excludes it.

This is also why the lemma should not be read as a statement about all conserved observables. It controls the analytic local functionals needed by the paper.

## 9. How quadratic commutation becomes full commutation

### The linearized transformation can be computed exactly

On free Cauchy data $z=(u,p)^T$, the derivative $D_-=D_t-D_x$ is represented by

$$
\mathcal L=
\begin{pmatrix}
-\partial_x&I\\
\partial_x^2-M&-\partial_x
\end{pmatrix}.
$$

Indeed its first component is $p-u_x$, and its second is $u_{xx}-Mu-p_x$. A field-space matrix such as $E$ acts on both the $u$ and $p$ components. Because $[E,M]=0$, it commutes with this operator $\mathcal L$.

At linear order in the fields, $g'(q)=4q$, so the second sewing equation gives $q=(\epsilon/2)D_-w$. Using $u=w+Dq$ and $v=w-D^Tq$ yields

$$
T_\epsilon^{\rm lin}
=\left(I-\frac{\epsilon}{2}D^T\mathcal L\right)
\left(I+\frac{\epsilon}{2}D\mathcal L\right)^{-1}.
$$

The inverse is a formal geometric series. Every coefficient is built out of $E$ and $\mathcal L$, which commute. Thus these linearized maps and their parameter velocities lie in a commutative operator algebra.

### Read off the quadratic Hamiltonian generators

The parameter Hamiltonian was $-I(\epsilon)/\epsilon$. Its linearized vector field is therefore generated by the quadratic parts $I_n^{(2)}$. Logarithmically differentiating the displayed linearized map gives

$$
X_{I_n^{(2)}}=C_n\mathcal L^n,
\qquad
C_n=2^{-n}\left[(I+E)^n-(-1)^n(I-E)^n\right].
$$

For example, $C_1=I$, consistent with $I_1=H+P_{\rm bulk}$: its Hamiltonian vector field at quadratic order is $D_t-D_x$ on free data. The formula retains all powers of the parameter while linearizing only in field amplitude.

All the operators $C_n\mathcal L^n$ commute. Commuting Hamiltonian vector fields have a Poisson bracket with zero Hamiltonian vector field. A quadratic functional with zero variational derivatives is constant, and its value at the zero field is zero. Therefore

$$
\{I_n^{(2)},I_m^{(2)}\}=0.
$$

### Apply rigidity to the full bracket

Define $J_{nm}=\{I_n,I_m\}$. This is again an analytic local functional of finite differential order. The Jacobi identity for Poisson brackets, together with conservation of $I_n$ and $I_m$, implies that $J_{nm}$ is conserved by $H$.

Every $I_n$ starts at quadratic amplitude order: the transformation fixes the vacuum and the defect potentials have no constant or linear terms there. The bracket $J_{nm}$ has no constant or linear part, and its quadratic part is exactly

$$
J_{nm}^{(2)}=\{I_n^{(2)},I_m^{(2)}\}=0.
$$

The rigidity lemma now applies to $J_{nm}$. A conserved analytic local functional with these vanishing low-degree parts must vanish entirely. Hence

$$
\{I_n,I_m\}=0
$$

for the full nonlinear charges.

This is the precise role of the linearized calculation. It is combined with a uniqueness theorem for conserved local functionals. The argument does not merely neglect the nonlinear corrections.

### Why the formal Bäcklund maps commute

The source parameter velocity is a linear combination of the commuting Hamiltonian vector fields:

$$
W_\epsilon=-\sum_{n\geq1}\epsilon^{n-1}X_{I_n}.
$$

For any local expression $f$, the pullback $T_\epsilon^*f$ means evaluate $f$ on the transformed fields. Its parameter derivative is obtained by applying the evolutionary derivative along $W_\epsilon$. Because all those derivatives commute, integrating in $\epsilon$ gives

$$
T_\epsilon^*
=\exp\left(-\sum_{n\geq1}\frac{\epsilon^n}{n}
\mathcal L_{X_{I_n}}\right).
$$

Here $\mathcal L_X$ is a Lie derivative: differentiate an expression along the infinitesimal field variation $X$. It is different notation from the free block operator $\mathcal L$ above. The factors $1/n$ come from integrating $\epsilon^{n-1}$.

The exponents for parameters $\epsilon$ and $\eta$ are sums of commuting operators, so their exponentials commute. This proves formal permutability of the maps. At any specified parameter order only finitely many terms of the exponential contribute, and each uses finitely many derivatives. The construction is therefore meaningful in the local formal setting without a convergence assertion.

## 10. Why there are infinitely many independent charges

### Reduce to a useful slice of initial data

Some coefficients of the hierarchy might be zero, or might depend on others. Section 8 must prove that arbitrarily large independent subfamilies survive.

The real symmetric matrices $-E^2$ and $M$ commute, so they have a common real unit eigenvector $a$. Write

$$
-E^2a=e^2a,\qquad Ma=m^2a,
\qquad e\geq0,\quad m^2>0.
$$

The number $e$ here is a matrix parameter, not the base of the exponential function. The quantity $e^2$ is nonnegative because $E$ is skew-symmetric. This does not require $a$ itself to be an eigenvector of $E$.

For odd $n=2j+1$, the coefficient $C_n$ is a polynomial in $E^2$, so it acts as a scalar in the selected eigenspace. Restrict the quadratic charge to data of the form

$$
u=0,\qquad p=a\varphi(x).
$$

This is a convenient set of initial conditions, not an assumption that the nonlinear evolution stays within this one-component slice.

The $u$ component of a Hamiltonian vector field is the variational derivative with respect to $p$. The formula for $X_{I_n^{(2)}}$ can therefore be integrated on this slice to obtain

$$
I_{2j+1}^{(2)}\big|_{u=0,p=a\varphi}
=\frac12\int\varphi P_j(\partial_x^2)\varphi\,dx,
$$

where $P_j$ is a polynomial with leading term

$$
P_j(z)=c_jz^j+\text{lower powers},
\qquad c_j=\operatorname{Re}(1+ie)^{2j+1}.
$$

The letter $P_j$ in this section denotes a polynomial, not a momentum. It describes how a quadratic charge weights different spatial frequencies. Evaluating a differential operator on Fourier modes in this way is the use of its *symbol*.

### Where the highest power comes from

On the selected mass eigenspace, write the free block operator as

$$
\mathcal L=-\partial_x I+A,
\qquad A^2=(\partial_x^2-m^2)I,
\qquad A_{12}=1.
$$

Expand its odd power using the binomial theorem. Only odd powers of $A$ contribute to the upper-right entry. That entry is a polynomial in $\partial_x^2$ of degree $j$, with leading coefficient $2^{2j}$. One sees this coefficient by keeping the highest derivative from each term: the relevant odd binomial coefficients sum to $2^{2j}$.

The scalar value of $C_{2j+1}$ is $2^{-2j}\operatorname{Re}(1+ie)^{2j+1}$. Multiplication cancels the powers of two and gives the stated $c_j$.

This calculation is performed on the quadratic functional and its variational derivative, so it already respects integration by parts. It avoids inferring independence from an unreduced high-derivative density.

### Why infinitely many leading coefficients survive

Write $1+ie=\sqrt{1+e^2}\,e^{i\theta}$, where $\theta=\arctan e\in[0,\pi/2)$. Then $c_j$ is a positive factor times $\cos((2j+1)\theta)$.

Suppose all sufficiently late $c_j$ vanished. In particular, the cosines at two consecutive late odd multiples would both vanish. Their arguments differ by $2\theta$, so $2\theta$ would be an integer multiple of $\pi$. In the given interval this forces $\theta=0$. But then every cosine is one, a contradiction.

There are therefore infinitely many nonzero $c_j$. Individual ones can still vanish. Select any $N$ indices $j_1<\cdots<j_N$ for which they are nonzero. Their polynomials have distinct degrees and are linearly independent.

### Choose Fourier modes that distinguish those polynomials

On a circle of length $2\pi$,

$$
P_j(\partial_x^2)\cos(kx)=P_j(-k^2)\cos(kx).
$$

The proof chooses distinct positive integers $k_1,\ldots,k_N$ so that

$$
\mathsf A_{i\ell}=P_{j_i}(-k_\ell^2)
$$

is an invertible $N\times N$ matrix. Such integers must exist. Otherwise all the evaluation vectors at positive integers would span a proper subspace of $\mathbb R^N$. A nonzero vector perpendicular to that span would give a nonzero linear combination of the polynomials vanishing at every $-k^2$. A nonzero polynomial cannot have infinitely many distinct roots.

Now take

$$
\varphi(x)=\sum_{\ell=1}^N b_\ell\cos(k_\ell x).
$$

Fourier orthogonality gives

$$
I_{2j_i+1}^{(2)}
=\frac{\pi}{2}\sum_{\ell=1}^N
P_{j_i}(-k_\ell^2)b_\ell^2.
$$

The quadratic charge values are explicit functions of the $N$ amplitudes $b_\ell$.

### Why independence survives nonlinear corrections

Set $b_\ell=\tau\beta_\ell$, with every $\beta_\ell\ne0$. The Jacobian matrix of the selected full charges with respect to the amplitudes has entries

$$
\frac{\partial I_{2j_i+1}}{\partial b_\ell}
=\pi\tau\,P_{j_i}(-k_\ell^2)\beta_\ell+O(\tau^2).
$$

The leading matrix is the invertible evaluation matrix multiplied by a diagonal matrix with nonzero entries and by $\pi\tau$. Its determinant has a nonzero leading term of order $\tau^N$. The higher-amplitude terms cannot cancel that leading term for all sufficiently small nonzero $\tau$. Thus the full Jacobian is invertible there.

Independence on this finite set of variations implies independence in the full phase space: any linear relation between the full charge differentials would remain a relation after restricting to these amplitude variations, contradicting the invertible Jacobian.

The frequencies are fixed after choosing $N$, so shrinking $\tau$ gives arbitrarily small smooth periodic Cauchy data. This establishes the theorem's quantifier for every finite $N$. It does not require one fixed configuration witnessing independence of every member of an infinite list simultaneously.

The proof uses odd-indexed charges to obtain an infinite independent subfamily. Even-indexed charges can also be nontrivial, as the nonlinear example below shows.

## 11. What the reducible example teaches us

Section 9 tests what can go wrong when the scalar condition on $G$ is removed. Take two free fields with

$$
U(u)=\frac12(u_1^2+u_2^2),\qquad
E=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
G=\begin{pmatrix}4&0\\0&8\end{pmatrix}.
$$

The bulk is reducible: it is a sum of two independent massive free theories. Its equal masses allow a defect coupling that mixes the two components. The leading defect Hessian $G$ is invertible but not scalar.

Choose

$$
f(w)=\frac12w_1^2+\frac14w_2^2,
\qquad g(q)=2q_1^2+4q_2^2.
$$

These functions satisfy the split momentum identity exactly. The reciprocal parameter family still exists, as do its transparent local branch and canonical generating construction. Thus those properties by themselves survive this relaxation.

To test commutation, act on one free plane wave. Let $\ell$ be the eigenvalue of $D_-$ on that wave. The transformation is a two-component matrix series

$$
T_\epsilon=I+\epsilon\ell t_1+\epsilon^2\ell^2t_2+\cdots.
$$

The explicit matrices calculated in the paper satisfy

$$
[t_1,t_2]=\frac18\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Consequently

$$
T_\epsilon T_\eta-T_\eta T_\epsilon
=\frac{\epsilon\eta(\eta-\epsilon)\ell^3}{8}
\begin{pmatrix}0&1\\1&0\end{pmatrix}
+O_{\rm total}(4).
$$

The remainder has combined degree at least four in the two parameters. The displayed degree-three term is nonzero. It directly disproves automatic permutability for an arbitrary invertible $G$.

The bulk theory in this example is free and integrable. What fails is commutation of this particular family supplied by the defect. The example establishes the need for a further commutation argument and explains why coupling the fields at the defect is not a substitute for irreducibility of the bulk potential.

If a reducible theory has $G$ scalar, the alternative version of Theorem 2.1 remains available. The example concerns the relaxation to an arbitrary invertible matrix.

## 12. A coupled nonlinear example

### The potential and its vacuum

Section 10 shows that the hypotheses admit a nonlinear interaction between several components. Take three vectors in a two-dimensional field space:

$$
\alpha_1=(\sqrt2,0)^T,\quad
\alpha_2=(-1/\sqrt2,\sqrt6/2)^T,\quad
\alpha_3=(-1/\sqrt2,-\sqrt6/2)^T.
$$

They have equal length and directions separated by $120$ degrees. Define

$$
U(w)=\sum_{i=1}^3\exp(\alpha_i^Tw)-3,
\qquad
E=\frac1{\sqrt3}\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

The subtraction gives $U(0)=0$. Since $\sum_i\alpha_i=0$, the gradient also vanishes there. The Hessian is

$$
M=\sum_i\alpha_i\alpha_i^T=3I,
$$

so both linearized masses are $\sqrt3$. The exponentials contain nonlinear interactions at higher amplitude orders.

Set $D=I-E$, $\beta_i=D^T\alpha_i$, and

$$
g(q)=\sum_{i=1}^3\exp(\beta_i^Tq)-3.
$$

Again its value and first derivative vanish at zero. Since $D^TD=4I/3$, its Hessian is $3D^TD=4I$, the required normalization.

### How the exact defect identity is verified

The relevant pairings are

$$
[\alpha_i^T\beta_j]_{ij}
=\begin{pmatrix}2&0&-2\\-2&2&0\\0&-2&2\end{pmatrix},
\qquad -D\alpha_i=\beta_{i-1},
$$

where the subscripts are cyclic: the predecessor of $1$ is $3$.

Expand the two sides of the potential identity in the independent functions $\exp(\alpha_i^Tw)$. On the left, the coefficient for index $i$ is

$$
\exp(\beta_i^Tq)-\exp(\beta_{i-1}^Tq).
$$

On the right, half the $i$th row of the pairing matrix gives exactly those two exponentials with signs $+$ and $-$. Thus the identity holds for the complete exponentials, with no truncation in field amplitude.

The potential is irreducible. If an orthogonal split existed in two dimensions, every mixed Hessian entry in the splitting coordinates would vanish. Independence of the three exponentials would force each vector $\alpha_i$ to lie along one of the two perpendicular coordinate axes. Three directions separated by $120$ degrees cannot do so.

The paper identifies this as the $A_2^{(1)}$ affine Toda example. Understanding the checks above requires only the displayed vectors and exponentials; Lie-algebra terminology is not needed for the structural proof.

### Why one coefficient vanishes without spoiling the hierarchy

For this $E$, one has $E^2=-I/3$. The formula for the third quadratic generator gives

$$
C_3=\frac{I+3E^2}{4}=0.
$$

Hence $I_3^{(2)}=0$, and the rigidity lemma gives $I_3=0$ as a functional. Its local density is a spatial derivative. This is an example of why the theorem says infinitely many coefficients are independent, rather than declaring every coefficient nonzero.

The checks also show that $I_2$ is nontrivial and verify the bracket of nontrivial charges indexed two and four. The odd-index construction in the general independence proof is a sufficient subfamily, not an exhaustive description of all charges.

### What the computer checks establish

The script `textbook_code/defect_integrability_structural/checks.py` records 30 exact finite checks. They include linearized transformations and generators, a Fourier independence determinant, the reducible counterexample, and nonlinear local currents in the exponential example. In that example the nonlinear computations keep the full field dependence while examining specified parameter orders.

The script `textbook_code/defect_integrability_structural/paper_checks.py` records 12 further exact checks. These include three-component momentum identities, the chiral equations, the endpoint variation, the residual identity used to solve both sewing equations, the spatial signs, and the massless and shifted-vacuum calculations.

These checks help detect sign, factor, and ordering errors in specific identities. Statements about every parameter order and every analytic potential satisfying the hypotheses rely on the written proof, especially the rigidity lemmas. The full theorem is not a Lean-certified result.

## 13. Different bulk theories and other limits

### What happens if the potentials on the two sides differ

Allow a left potential $U_-$ and a right potential $U_+$ while retaining the normalized kinetic coupling. The momentum calculation gives

$$
U_-(w+Dq)-U_+(w-D^Tq)=\frac12f'(w)^Tg'(q).
$$

If the transparent critical point is $q=0$, then $g'(0)=0$. Setting $q=0$ immediately gives $U_-(w)=U_+(w)$ near zero.

One might try a different constant difference $q_*$. If $g'(q_*)=0$, set $z=w+Dq_*$. Since $D+D^T=2I$, the right field equals $z-2q_*$. The same identity becomes

$$
U_-(z)=U_+(z-2q_*).
$$

Thus this change permits potentials related by a constant translation in field space. It does not produce genuinely different local theories. The obstruction follows directly from the momentum identity and the critical-point condition.

The paper points to a Liouville/free-massless defect in its first reference as an example of integrable defects joining genuinely different theories. Such an example does not have the common positive-mass vacuum required here. It lies outside the hypotheses used to construct this particular branch and prove rigidity.

### The proposed composition route

Suppose another construction gave canonical transformations

$$
T_\lambda:\mathcal P_-\longrightarrow\mathcal P_+
$$

between the phase spaces of two different theories, intertwining their time evolutions. Fix a parameter $\lambda_0$ at which the transformation is invertible and compose

$$
S_\lambda=T_{\lambda_0}^{-1}\circ T_\lambda.
$$

This takes the left theory back to itself. It is canonical, it intertwines the left evolution with itself, and $S_{\lambda_0}=\mathrm{Id}$. These facts follow from composing the assumed maps and their inverses.

To adapt the present proof, much more must be established. The expansion near $\lambda_0$ must have local coefficients. Its parameter velocity must have local Hamiltonians with controlled vacuum behavior. The quadratic generators must commute, and their symbols must supply arbitrarily many independent charges.

Local differential equations for a transformation do not automatically give a local solution rule. For example, solving an equation involving a spatial derivative can require a spatial integral and an integration constant. An inverse transformation or its composition can therefore introduce nonlocal dependence. The composition route is a proposal for further work, not a proved extension in this paper.

### Why the massless case needs a different argument

For a free massless scalar, the bulk equations are $u_t=p$ and $p_t=u_{xx}$. Define $r=p+u_x$. Then

$$
D_tr=u_{xx}+p_x=D_xr.
$$

It follows that

$$
D_t(r^n)=D_x(r^n),
\qquad
\frac{d}{dt}\int r^n\,dx=0
$$

under the usual boundary conditions. For $n\geq3$ this is a nonzero local functional with no quadratic part. Its derivative with respect to $p$, for example, is $nr^{n-1}$ and does not vanish identically.

This directly violates the conclusion that would result from removing the positive-mass hypothesis from Lemma 6.1. In the Fourier proof, the corresponding curvature disappears when the mass is zero. The example identifies a failure of the rigidity argument; massless theories can themselves be integrable.

### Why analyticity and the other restrictions remain

A smooth function can have a zero Taylor series at the vacuum without vanishing nearby. The analytic step in Lemma 6.2 excludes this ambiguity. Replacing analyticity by smoothness would require an additional argument. The paper does not claim that every such flat function supplies a conservation law; it identifies what its Taylor-series proof cannot decide.

Auxiliary defect variables, field-dependent kinetic couplings, higher-derivative bulk equations, and nonrelativistic theories can alter the momentum identity, the recursion, and the symplectic structures. They need their own analysis.

The roles of the assumptions can be kept separate:

| Assumption or derived condition | Its role in this proof |
| --- | --- |
| Constant normalized Type-I coupling and strong momentum balance | Give the split potential identity and explicit generating functional |
| Transparent critical point and invertible $G$ | Make the near-identity local recursion possible |
| Bulk irreducibility, or a scalar $G$ imposed directly | Give commuting quadratic parameter generators |
| Positive masses | Exclude higher-degree translation-invariant local conserved functionals of the free theory |
| Analyticity near the vacuum | Turn vanishing Taylor coefficients into a local analytic identity |
| Periodic data in the independence argument | Provide explicit Fourier configurations and an invertible finite Jacobian |

## 14. The spatial Hamilton–Jacobi appendix

### Two Hamiltonian descriptions of the same field equation

The main proof uses ordinary time evolution. A state consists of functions of $x$, the canonical momentum is $p=u_t$, and the Hamiltonian is integrated over $x$.

Appendix A instead treats $x$ as the evolution variable in a Hamiltonian description. At a fixed $x$, a state consists of histories in $t$. The momentum conjugate to $u$ in this description is

$$
\pi=\frac{\partial L}{\partial u_x}=-u_x.
$$

The corresponding Legendre transform is

$$
\mathcal H^{(x)}=\pi^Tu_x-L
=-\frac12|\pi|^2-\frac12|u_t|^2+U(u)
=-T^{11}(u).
$$

The minus signs follow from the minus sign of the spatial kinetic term in $L$. This is the generator for translations in $x$, not the ordinary positive bulk energy for time evolution.

The spatial symplectic form and Hamiltonian are

$$
\Omega^{(x)}=\int\delta u^T\wedge\delta\pi\,dt,
\qquad H^{(x)}=\int\mathcal H^{(x)}\,dt.
$$

Hamilton's equations become

$$
u_x=-\pi,\qquad \pi_x=-u_{tt}-U'(u).
$$

Eliminating $\pi$ recovers $u_{tt}-u_{xx}+U'(u)=0$. Thus the spatial Hamiltonian equations reproduce the same bulk differential equation.

These expressions require histories and boundary conditions for which integration by parts in $t$ has no endpoint term. Periodic histories in $t$ are one possible choice in the appendix. That is a different use of periodicity from the spatially periodic initial data used in the main independence proof. The appendix does not impose time-periodic solutions on that theorem.

### Why minus the defect action is the generating functional

Let $S_d=\int L_d\,dt$. At the cut, varying the left bulk action gives the spatial endpoint term $\pi_-^T\delta u$, and varying the right gives $-\pi_+^T\delta v$. Cancellation with the defect variation requires

$$
d(-S_d)=\int(\pi_-^T\delta u-\pi_+^T\delta v)\,dt.
$$

This is a generating-functional identity, like the equal-time identity for $F_\epsilon$, but now the momenta are $\pi=-u_x$ and the integration variable is $t$. With these conventions the generator is $-S_d$.

The identity describes the sewing conditions as a spatial canonical relation. A relation can allow several outputs for a given input, or fail to admit an output for some inputs. Additional conditions are needed for it to be the graph of an actual map on chosen function spaces.

### What a Lagrangian relation means

Let $\mathcal P_-$ and $\mathcal P_+$ be the phase spaces on the two sides, with symplectic forms $\Omega_-$ and $\Omega_+$. Their product carries the form

$$
\Omega=\Omega_-\oplus(-\Omega_+).
$$

The minus sign compares the old and new symplectic structures. Let $\Gamma$ be the set of pairs related by the sewing conditions. Its tangent space consists of variations of such pairs that preserve the relation to first order.

The relation is *isotropic* if $\Omega$ vanishes on every two tangent variations. It is *Lagrangian* when the tangent space equals its symplectic orthogonal:

$$
T\Gamma=(T\Gamma)^{\perp_\Omega}.
$$

The symplectic orthogonal consists of vectors whose pairing with every tangent vector is zero. In a finite-dimensional symplectic space, a Lagrangian subspace is isotropic of half the total dimension. The term is unrelated to calling $L$ a Lagrangian density: they are two uses of the name in mechanics.

In infinite-dimensional spaces, isotropy alone does not automatically give the needed equality with the symplectic orthogonal. The appendix explicitly assumes that equality, regularity of the relation, and existence of the Hamiltonian vector fields. The formal endpoint variation does not prove all these analytic properties by itself.

### The geometric lemma explained

Write the pair of Hamiltonian evolution vectors as

$$
X=(X_{H_-},X_{H_+}).
$$

For every tangent vector $Y$ to $\Gamma$, Hamilton's defining identity gives

$$
\Omega(X,Y)=d(H_--H_+)(Y).
$$

Suppose the Hamiltonian difference is locally constant when restricted to the relation. Its derivative on every tangent direction is then zero. The displayed equation says that $X$ belongs to the symplectic orthogonal of $T\Gamma$. The Lagrangian property identifies that orthogonal with $T\Gamma$ itself. Thus the pair of evolution vectors is tangent to the relation.

Tangency means that the two Hamiltonian evolutions preserve the sewing relation at the infinitesimal level. Conversely, if $X$ is tangent, isotropy makes its pairing with every tangent $Y$ zero. The Hamiltonian difference is therefore locally constant on the relation. This proves both directions of Lemma A.1.

If the relation is the graph of a map $T$, tangency says

$$
DT\,X_{H_-}=X_{H_+}\circ T.
$$

This is the infinitesimal intertwining condition: the map takes the left evolution into the right evolution. An interpretation in terms of actual flows also requires those flows to exist in the chosen realization.

### How momentum balance supplies the Hamiltonian equality

Since $\mathcal H^{(x)}=-T^{11}$, the defect momentum identity becomes

$$
\mathcal H_-^{(x)}-\mathcal H_+^{(x)}=-D_tP_d.
$$

Integrate over $t$ with vanishing boundary contribution. The spatial Hamiltonians agree on the sewing relation. The geometric lemma then explains why momentum balance leads to spatial intertwining whenever its geometric assumptions hold.

This is the Hamilton–Jacobi viewpoint: the defect action generates a canonical relation compatible with Hamiltonian evolution. The calculation can accommodate different bulk potentials. Its conclusion is spatial compatibility. The equal-time hierarchy requires the additional constructions and proofs in Sections 3–8: the local parameter branch, the temporal generator, commutation, and independence.

## 15. The result and its evidence

### How the complete argument fits together

The paper's conclusion combines the following proved steps under its stated hypotheses:

1. Strong momentum balance forces a split defect potential and a potential identity.
2. Bulk irreducibility forces a scalar leading defect Hessian. Reciprocal rescaling produces the parameter family.
3. The invertible linear term in the difference variable gives a unique local formal branch. The potential identity proves that it satisfies both sewing equations and the bulk equation.
4. A continuity equation supplies conserved coefficients. An equal-time generating functional identifies those same coefficients as parameter Hamiltonians.
5. The free massive Fourier argument and analytic amplitude argument give rigidity of local conserved functionals.
6. The quadratic parameter generators commute. Rigidity applied to their full Poisson brackets gives nonlinear involution and then formal permutability.
7. Infinitely many nonzero polynomial symbols give invertible Fourier Jacobians and functional independence near the vacuum.

The word *structural* refers to obtaining these implications without first classifying $U$ or constructing a Lax representation. A Lax representation is another way of encoding an equation through compatible auxiliary linear equations; this proof does not require one. The existence of a defect satisfying all the hypotheses still imposes substantial constraints on $U$.

The result supplies a bulk hierarchy in the analytic massive Type-I setting. The unrestricted implication from a momentum-conserving defect to integrability of arbitrary adjoining field theories remains open in this work.

### What has been checked

The paper includes [30 structural checks](structural_type_I/verification.txt) and [12 additional derivation checks](structural_type_I/paper_verification.txt). They can be rerun from the repository root:

```sh
python3 textbook_code/defect_integrability_structural/checks.py
python3 textbook_code/defect_integrability_structural/paper_checks.py
```

The exact finite checks support particular calculations and examples. The proof for all orders is written mathematics. Neither the entire theorem nor its analytic variational lemmas has been formalized in Lean. The earlier Lean material concerns other specified algebraic identities and does not certify this theorem. This companion changes none of those status distinctions.

### How the references fit into the story

The [paper's bibliography](defect_integrability_paper.md#references) provides the source details and links. Its references serve different purposes:

| References in the paper | Why they appear |
| --- | --- |
| Bowcock–Corrigan–Zambon, references 1–2 | Earlier classical defect and affine Toda constructions motivating the relation between momentum balance and Bäcklund equations |
| Bristow–Bowcock, reference 3 | Momentum-conserving Type-II defects, a broader setting than the theorem proved here |
| Caudrelier–Kundu, reference 4 | The use of both spatial and temporal Hamiltonian descriptions of defects |
| Kuznetsov–Sklyanin, reference 5 | Generating functions and differentiation with respect to a Bäcklund parameter |
| Gordon and Opanasenko–Popovych, references 6–7 | Earlier work on local conservation laws of the free Klein–Gordon equation |

The paper gives the particular arguments it needs explicitly. Those references provide context and routes into the literature; the companion makes no separate priority claim.

### A notation guide for rereading

| Symbol | Meaning |
| --- | --- |
| $u,v$ | Left and right fields, or the input and transformed bulk solutions |
| $p=u_t$, $P=v_t$ | Equal-time canonical momenta |
| $U$, $M=U''(0)$ | Bulk potential and mass-squared matrix |
| $E$, $D=I-E$ | Constant skew coupling matrix and its associated matrix |
| $q=(u-v)/2$, $w=(D^Tu+Dv)/2$ | Difference and modified average endpoint coordinates |
| $B$, $B_\epsilon$ | Original defect energy and its rescaled family |
| $P_d$, $P_\epsilon$ | Defect momentum and its rescaled family |
| $G$ | Leading Hessian of the original defect energy in the difference directions |
| $g$ | Difference-variable part of the defect potential, normalized to $g''(0)=4I$ after Section 3 |
| $D_t,D_x,D_\pm$ | Total derivatives along bulk solutions and their sum or difference |
| $\epsilon,\eta$ | Formal Bäcklund parameters |
| $\tau$ | An amplitude scaling parameter, independent of $\epsilon$ |
| $T_\epsilon$ | Local formal Bäcklund transformation on Cauchy data |
| $I(\epsilon)$, $I_n$ | Integrated generating series and its conserved coefficients |
| $F_\epsilon$ | Equal-time generating functional with independent endpoint fields |
| $W_\epsilon$, $K_\epsilon$ | Source parameter velocity and its Hamiltonian $-I(\epsilon)/\epsilon$ |
| $F^{(2)}$ | Quadratic field-amplitude part of a functional $F$ |
| $F_u,F_p$ | Variational derivatives, including integration by parts |
| $X_F$ | Hamiltonian vector field $(F_p,-F_u)$ |
| $\mathcal L$ | Block differential operator representing $D_-$ on free Cauchy data |
| $C_n$ | Constant matrix in the quadratic generator $X_{I_n^{(2)}}=C_n\mathcal L^n$ |
| $P_j(z)$ | Polynomial weighting Fourier modes in selected quadratic charges |
| $\pi=-u_x$ | Spatial canonical momentum in Appendix A |
| $\Gamma$ | Spatial sewing relation in the product of the two phase spaces |

The same letter can have several roles when decorated differently. In particular, $P=v_t$, $P_d$, and $P_j$ are different objects. The matrix $D$, the total derivative $D_t$, and the tangent map $DT_\epsilon$ are also different objects. Their definitions determine which is meant in each equation.
