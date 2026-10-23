# Momentum-Conserving Defects, Kinematic Symmetry and Integrability

*Draft, 20 October 2026.*

**Status.** Sections 2–7 give written proofs, in the formal variational calculus, of general statements about finite-order Lagrangian field theories in $1+1$ dimensions. The main theorem (Theorem 8.1) deduces an infinite hierarchy of independent commuting local charges from momentum conservation at a defect **together with** further hypotheses, each stated explicitly. The unconditional conjecture of Corrigan and Zambon is not proved; Section 10 identifies the missing implication. Section 8.2 derives the family of hypothesis (C) from momentum conservation for relativistic Type-I defects with constant kinetic coupling, given a transparent point; it restates two propositions of the companion manuscript [23] and was added on 23 October 2026, after the independent check. The literature has not been searched systematically for earlier versions of the general statements, so no novelty is claimed for them. Accompanying scripts check identities and hypotheses (Appendix B); they do not replace the proofs. An independent check of the written proofs found statements that were false in the generality claimed, and this version corrects them; the corrections have not yet been checked independently.

## Abstract

A jump defect joins two $(1+1)$-dimensional local Lagrangian field theories at a point. Corrigan, Zambon and collaborators observed in many examples that a defect can conserve a suitably modified momentum only if its sewing conditions form a Bäcklund transformation and the bulk theories are integrable. We prove the first half of this observation in general. For arbitrary finite-order bulk Lagrangians and arbitrary local defect functionals, including auxiliary defect fields and Lagrange multipliers, an off-shell momentum balance implies that the spatial Hamiltonian flows of the two bulk theories are tangent to the sewing correspondence. Under an injectivity condition, which is vacuous without auxiliary fields, every solution of the sewing equations imposed at all points then solves both bulk equations. The proof applies the time-Euler operator to the spatial Hamilton–Jacobi form of the balance. For the second half we isolate a mechanism with three ingredients. First, a conservation law whose current is affine in $(x,t)$ — the Noether current of a Lorentz boost, a Galilean boost, a dilation or a time-linear field shift — turns defect charges into a conserved generating density along the Bäcklund relation. Second, a one-parameter family of momentum-conserving defects with a regular transparent limit turns this density into infinitely many local conservation laws; in the observed cases the family is the orbit of the defect under a kinematic symmetry, or a modulus of the momentum constraint. For relativistic Type-I defects with constant kinetic coupling, momentum conservation itself supplies such a family and its transparent limit, provided the defect potential has a nondegenerate transparent point. Third, for bulk theories with a constant Poisson operator and nonresonant dispersion, such conservation laws are in involution under explicit conditions on their linear and quadratic parts, and an explicit generating quadratic symbol decides their independence. We check the hypotheses case by case on the published defects of the observed cases: sine-Gordon, affine and conformal Toda, Tzitzéica, the nonlinear Schrödinger equation, KdV, mKdV and Boussinesq. The massless theories fail nonresonance and are covered only by the Bäcklund theorem.

---

## 1. Introduction

### 1.1 The observation

Let $\mathcal L_-([\phi])$ on $x<0$ and $\mathcal L_+([\psi])$ on $x>0$ be local Lagrangian densities joined at $x=0$ by a defect action $S_d=\int dt\,\mathcal L_d$. Energy is conserved across any time-independent defect. Momentum is not, because the defect breaks spatial translations. Bowcock, Corrigan and Zambon found that for the sine-Gordon model a local defect contribution can nevertheless restore momentum conservation, and that the resulting sewing conditions are a frozen Bäcklund transformation [1, 2]. Corrigan and Zambon then found the same phenomenon in every model they examined, including models whose bulk potentials were left unspecified in advance [3–8]. They summarised the evidence by saying that "demanding both energy and momentum conservation singles out the integrable models" [6, §6], and stated in several papers that no direct proof was known [5, 6, 8].

The observed cases are the following.

| Setting | References | Bulk input assumed | Bulk theories selected by momentum conservation |
|---|---|---|---|
| one relativistic scalar, Type I | [1, 4] | unspecified potentials | free, Liouville, sine/sinh-Gordon |
| several relativistic scalars, Type I | [2, 4] | exponential potentials | $a_r^{(1)}$ affine Toda, $a_r$ conformal Toda |
| one relativistic scalar, Type II | [5, 6] | unspecified potentials | free, Liouville, sine/sinh-Gordon, Tzitzéica ($a_2^{(2)}$) |
| several relativistic scalars, Type II | [9–11] | affine Toda bulk fixed | compatible defect potentials |
| nonlinear Schrödinger (NLS) | [3, §§2–3] | unspecified self-interaction | cubic NLS |
| KdV and mKdV, potential form | [3, §§7, 9] | unspecified potential | KdV, mKdV |
| Boussinesq, potential form | [8, §3] | unspecified potential | Boussinesq |

Type-I defects involve only the boundary values of the two bulk fields. Type-II defects carry an additional field on the defect [5]. In the KdV and mKdV defects of [3] a term linear in $p_{xx}-q_{xx}$ acts as a Lagrange multiplier.

### 1.2 What a general theorem must supply

A general explanation must supply four logically separate steps:

1. momentum conservation $\Rightarrow$ the sewing conditions, imposed at every $x$, form a Bäcklund relation;
2. a Bäcklund relation $\Rightarrow$ a conserved local *generating density* along it;
3. a one-parameter family of such relations with a regular transparent limit $\Rightarrow$ infinitely many local conservation laws;
4. these conservation laws $\Rightarrow$ independent charges in involution.

### 1.3 Results

* **Theorem 3.3 (Bäcklund theorem).** Step 1 holds for arbitrary admissible bulk Lagrangians and arbitrary local defect functionals, including auxiliary fields and multipliers, under a checkable injectivity condition (I). Condition (I) is vacuous for Type-I defects.
* **Lemma 4.1, Propositions 4.2–4.3, Lemma 5.2 (closure).** Step 2 holds whenever the bulk has a conservation law with current affine in $(x,t)$ whose two constituent laws have defect charges. Boosts, Galilean boosts, dilations and time-linear shifts provide such laws. Every observed bulk theory has one.
* **Lemmas 5.4–5.5, 6.2, 6.6 and Theorem 6.4 (hierarchy).** Step 3 holds for any family with a regular transparent limit. Dilations carry a momentum-conserving defect to a family of such defects when the bulk Lagrangians are strictly homogeneous; Lorentz boosts do the same for Bäcklund relations.
* **Theorems 7.3–7.4 and Proposition 7.5 (involution and independence).** Step 4 holds for bulk theories with a constant Poisson operator and nonresonant dispersion, under conditions on the linear and quadratic parts of the charges. Independence is decided by an explicit generating quadratic symbol, computed in closed form for the observed defects. No Bianchi-permutability assumption is needed.
* **Theorem 8.1** assembles the steps, and **Section 9** checks its hypotheses case by case.
* **Propositions 8.2–8.3 and Theorem 8.4** derive the family and the formal branch of hypothesis (C) from momentum conservation, for relativistic Type-I defects with constant kinetic coupling and a nondegenerate transparent point, following [23].

### 1.4 Relation to earlier work

Caudrelier developed an inverse-scattering approach to defects in integrable field theories, in which a defect acts as a frozen Bäcklund transformation and the modified conserved quantities have a generating function [12]. Caudrelier and Kundu gave a multisymplectic treatment in which spatial and temporal Hamiltonian descriptions coexist [13]. Doikou studied defect dynamics as quasi-Bäcklund transformations [14]. Avan and Doikou [15] and Bristow and Bowcock [10] studied Liouville integrability and momentum conservation for specific classes of defects. These works start from an integrable bulk theory. The present paper starts from momentum conservation and asks which consequences follow without assuming integrability.

---

## 2. The spatial phase space of a bulk theory

### 2.1 Bulk Lagrangians and canonical currents

Let $\phi(x,t)\in\mathbb R^r$; complex fields are treated as pairs $u,\bar u$ of independent components. Write $D_t,D_x$ for total derivatives. A **bulk Lagrangian** is a local density $\mathcal L(\phi_{a,k})$, $\phi_{a,k}=D_t^aD_x^k\phi$, with no explicit $(x,t)$, of spatial order $K\ge1$. It is **admissible** if $\partial_x^K\phi$ enters only through $\phi_{0,K}$ (no mixed top derivatives) and $\det\partial^2\mathcal L/\partial\phi_{0,K}^2\ne0$.

Integrating by parts first in $t$ and then in $x$ gives, for every variation $\eta$,

$$\operatorname{pr}v_\eta\mathcal L=E(\mathcal L)\cdot\eta+D_x\Big(\sum_{m=0}^{K-1}\pi_m\cdot D_x^m\eta\Big)+D_t\,\Xi(\eta), \tag{2.1}$$

with

$$F_k=\sum_{a}(-D_t)^a\frac{\partial\mathcal L}{\partial\phi_{a,k}},\qquad \pi_m=\sum_{j=0}^{K-1-m}(-D_x)^jF_{m+j+1},\qquad E(\mathcal L)=\sum_{k}(-D_x)^kF_k, \tag{2.2}$$

and the explicit temporal boundary term

$$\Xi(\eta)=\sum_{k}\sum_{a\ge1}\sum_{b=0}^{a-1}(-D_t)^b\frac{\partial\mathcal L}{\partial\phi_{a,k}}\cdot D_t^{a-1-b}D_x^k\eta. \tag{2.3}$$

Formula (2.3) is the telescoping identity $P\,D_t^a\zeta=(-D_t)^aP\,\zeta+D_t\sum_{b<a}(-D_t)^bP\,D_t^{a-1-b}\zeta$, applied with $P=\partial\mathcal L/\partial\phi_{a,k}$ and $\zeta=D_x^k\eta$. The $x$-integration uses the same identity in $x$ on $F_kD_x^k\eta$; collecting the coefficient of $D_x^m\eta$ gives $\pi_m$.

**Definition 2.1 (canonical currents).** Put $\Phi_m=D_x^m\phi$ and

$$\mathcal T^0{}_0=\Xi(D_t\phi)-\mathcal L,\quad \mathcal T^1{}_0=\sum_m\pi_m\cdot D_t\Phi_m,\quad \mathcal T^0{}_1=\Xi(D_x\phi),\quad \mathcal T^1{}_1=\mathcal H^{(x)}:=\sum_m\pi_m\cdot D_x\Phi_m-\mathcal L. \tag{2.4}$$

With $\eta_{\mu\nu}=\mathrm{diag}(1,-1)$ write $T^{00}=\mathcal T^0{}_0$, $T^{01}=-\mathcal T^0{}_1$, $T^{10}=\mathcal T^1{}_0$ and $T^{11}=-\mathcal T^1{}_1$.

**Lemma 2.1 (Legendre–Noether identity).** *For every admissible $\mathcal L$, off shell,*

$$D_t\mathcal T^0{}_\nu+D_x\mathcal T^1{}_\nu=-E(\mathcal L)\cdot D_\nu\phi\qquad(\nu=0,1). \tag{2.5}$$

*Thus $(\mathcal T^0{}_\nu,\mathcal T^1{}_\nu)$ are Noether currents of the translations, and the momentum flux is $T^{11}=-\mathcal H^{(x)}$ exactly. Any other pair satisfying (2.5) off shell differs from these, locally, by a trivial current $(D_xC,-D_tC)$ plus a constant. For a first-order Lagrangian they are the usual canonical currents.*

*Proof.* Put $\eta=D_\nu\phi$ in (2.1). Then $\operatorname{pr}v_\eta\mathcal L=D_\nu\mathcal L$, and rearranging gives (2.5). Two such pairs differ by a current conserved off shell. By local exactness of the horizontal variational complex [16, Thm 4.24] such a current is trivial up to a constant. For a first-order Lagrangian, $\Xi(\eta)=\partial\mathcal L/\partial\phi_t\cdot\eta$ and $\pi_0=\partial\mathcal L/\partial\phi_x$. $\square$

### 2.2 Spatial Hamilton equations

The **spatial phase space** at fixed $x$ consists of $t$-histories $z=(\Phi_0,\dots,\Phi_{K-1};\pi_0,\dots,\pi_{K-1})$ [13]. Admissibility lets us solve $\pi_{K-1}=\partial\mathcal L/\partial\phi_{0,K}$ for $\phi_{0,K}=Z(\Phi,\pi_{K-1})$, a local function of the $t$-jets of $\Phi$ and of $\pi_{K-1}$. The spatial Hamiltonian density is

$$\mathcal H(\Phi,\pi)=\sum_{m<K-1}\pi_m\cdot\Phi_{m+1}+\pi_{K-1}\cdot Z-\mathcal L\big|_{\phi_{0,K}=Z}. \tag{2.6}$$

Let $a_m=\partial\mathcal H/\partial\pi_m$ and $b_m=E^{(t)}_{\Phi_m}(\mathcal H)$, the time-Euler derivative. The spatial Hamiltonian vector field is $X=(a,-b)$.

**Lemma 2.2 (Hamilton–Euler–Lagrange identities).** *Let $\phi$ be any field, on or off shell, and let $z=(\Phi_m=D_x^m\phi,\ \pi_m=\pi_m[\phi])$ be its Ostrogradsky lift. Then*

$$D_x\Phi_m=a_m(z)\ \ (\text{all }m),\qquad D_x\pi_m+b_m(z)=0\ \ (m\ge1),\qquad D_x\pi_0+b_0(z)=-E(\mathcal L)[\phi]. \tag{2.7}$$

*In particular $D_xz=X(z)$ if and only if $E(\mathcal L)[\phi]=0$.*

*Proof.* $a_m=\Phi_{m+1}$ for $m<K-1$, and $a_{K-1}=Z+(\pi_{K-1}-\partial\mathcal L/\partial\phi_{0,K})\partial Z/\partial\pi_{K-1}=Z=D_x^K\phi$. In $b_m$ the terms through $Z$ cancel for the same reason, and no $t$-derivative of $Z$ occurs. Hence $b_m=\pi_{m-1}-F_m$ for $m\ge1$ and $b_0=-F_0$. The recursion $\pi_{m-1}=F_m-D_x\pi_m$, which is (2.2), gives the second identity; $E=F_0-D_x\pi_0$ gives the third. $\square$

---

## 3. Momentum balance and the Bäcklund theorem

### 3.1 Defects

Let $\mathcal L_\pm$ be admissible, of spatial orders $K_\pm$. A **defect functional** is $S_d=\int dt\,\mathcal L_d$, where $\mathcal L_d$ is a local function of the $t$-jets of

$$Y=(\Phi,\Psi,\lambda),\qquad \Phi=(\Phi_m)_{m<K_-}\big|_{x=0^-},\quad \Psi=(\Psi_m)_{m<K_+}\big|_{x=0^+},\quad \lambda\in\mathbb R^p .$$

The auxiliary variables $\lambda$ include dynamical defect fields (Type II) and Lagrange multipliers. Varying $S=\int_{x<0}\mathcal L_-+\int_{x>0}\mathcal L_++S_d$ and using (2.1) on each half-line gives the **sewing equations**

$$\pi_{-,m}=\Pi^-_m(Y):=-E^{(t)}_{\Phi_m}\mathcal L_d,\qquad \pi_{+,m}=\Pi^+_m(Y):=E^{(t)}_{\Psi_m}\mathcal L_d,\qquad 0=C(Y):=E^{(t)}_\lambda\mathcal L_d. \tag{3.1}$$

The **sewing correspondence** is $\Gamma_d=\{(\Phi,\Pi^-(Y);\Psi,\Pi^+(Y)):C(Y)=0\}$. A triple of fields $(\phi,\psi,\lambda)$ on a region of $\mathbb R^2$ is a **promoted solution** if (3.1) holds at every $x$, with $\pi_\mp$ the actual Ostrogradsky momenta of $\phi$ and $\psi$.

Let $\mathcal S$ be the Fréchet derivative of the defect Euler–Lagrange expression $E_Y(\mathcal L_d)$, with blocks $S_{AB}$, $A,B\in\{\Phi,\Psi,\lambda\}$. By the Helmholtz conditions [16, Thm 5.92], $\mathcal S$ is formally self-adjoint: $S_{AB}^*=S_{BA}$. The linearisation of (3.1) is

$$\delta\pi_-=-(S_{\Phi\Phi}\delta\Phi+S_{\Phi\Psi}\delta\Psi+S_{\Phi\lambda}\delta\lambda),\quad \delta\pi_+=S_{\Psi\Phi}\delta\Phi+S_{\Psi\Psi}\delta\Psi+S_{\Psi\lambda}\delta\lambda,\quad 0=S_{\lambda\Phi}\delta\Phi+S_{\lambda\Psi}\delta\Psi+S_{\lambda\lambda}\delta\lambda. \tag{3.2}$$

A vector $(\delta z_-,\delta z_+)$ is **tangent** to $\Gamma_d$ if it arises from some $\delta Y$ in this way.

### 3.2 Momentum balance

**Definition 3.1 (momentum balance).** $S_d$ is *momentum-conserving* if

$$\mathcal H_-\big(\Phi,\Pi^-(Y)\big)-\mathcal H_+\big(\Psi,\Pi^+(Y)\big)\ \in\ \operatorname{Im}D_t+\langle C\rangle, \tag{3.3}$$

where $\langle C\rangle$ is the differential ideal generated by the components of $C$. Equivalently, there is a local $\widetilde P(Y)$ such that $\mathcal H_--\mathcal H_++D_t\widetilde P\in\langle C\rangle$. Integrating by parts in $t$, every element of $\langle C\rangle$ is $\rho\cdot C$ plus an element of $\operatorname{Im}D_t$: a term $f\,D_t^kC$ contributes $(-D_t)^kf$ to the local multiplier $\rho$. So (3.3) holds exactly when
$$\mathcal H_-\big(\Phi,\Pi^-(Y)\big)-\mathcal H_+\big(\Psi,\Pi^+(Y)\big)=\rho\cdot C+D_tB\qquad\text{for local }\rho,\,B. \tag{3.3$'$}$$

**Lemma 3.2.** *Let $P_\pm=\int T^{01}_\pm\,dx$. If (3.3) holds, then $P_-+P_++\widetilde P$ is conserved on all solutions of the bulk and sewing equations. Conversely, suppose that $P_-+P_++P_d$ is conserved on all such solutions for some local $P_d(Y)$, that their boundary jets at $x=0$ fill the prolonged constraint locus $\{D_t^kC=0,\ k\ge0\}$, and that every local function vanishing on that locus lies in $\langle C\rangle$. Then (3.3) holds with $\widetilde P=P_d$.*

*Proof.* By (2.5), $D_tT^{01}+D_xT^{11}=0$ on shell. So $\frac{d}{dt}(P_-+P_+)=(-T^{11}_-+T^{11}_+)|_{x=0}=(\mathcal H_--\mathcal H_+)|_{x=0}$ by Lemma 2.1. On solutions of (3.1) the momenta in $\mathcal H_\pm$ are $\Pi^\pm(Y)$. Conservation is therefore the vanishing of $\mathcal H_--\mathcal H_++D_tP_d$ on the boundary jets of all solutions. Elements of $\langle C\rangle$ vanish there, which gives the first statement. Under the assumptions of the converse, $\mathcal H_--\mathcal H_++D_tP_d$ vanishes on the prolonged constraint locus and so lies in $\langle C\rangle$. $\square$

The regularity assumption in the converse cannot be dropped. Take two copies of the massive Klein–Gordon field, $\mathcal L=\frac12(w_t^2-w_x^2-m^2w^2)$, and $\mathcal L_d=\lambda(\psi-\phi)^2$. Then $C=(\psi-\phi)^2$ and $\Pi^\pm=2\lambda(\psi-\phi)$. Over real fields the constraint locus is $\psi=\phi$, where $\Pi^\pm=0$ and $\mathcal H_-=\mathcal H_+$, so momentum is conserved with $P_d=0$. But $E_\Phi(\mathcal H_--\mathcal H_+)=\phi_{tt}+m^2\phi$ on the locus, while the $t$-Euler derivatives of every element of $\operatorname{Im}D_t+\langle C\rangle$ vanish there, because the linearisation of $C$ vanishes at $\psi=\phi$ (`checks/check_scope.py`). Definition 3.1 is therefore a strong, off-shell form of momentum conservation. It is how momentum conservation is imposed in [1–8]: the boundary $t$-jets are treated as independent once the sewing equations have been used.

### 3.3 The Bäcklund theorem

**Theorem 3.3 (momentum conservation gives a Bäcklund relation).** *Let $S_d$ satisfy Definition 3.1, written in the form (3.3$'$) with multiplier $\rho$.*

*(a) (Tangency.) At every point of $\Gamma_d$, the pair of spatial Hamiltonian vector fields $(X_-,X_+)$ is tangent to $\Gamma_d$. It is the image of $\delta Y=(a_-,a_+,\rho)$ under (3.2).*

*(b) (Promoted solutions are bulk solutions.) Let $(\phi,\psi,\lambda)$ be a promoted solution, and put $\kappa=D_x\lambda-\rho$. Then*

$$S_{\Phi_m\lambda}\kappa=E_-[\phi]\,\delta_{m0},\qquad S_{\Psi_m\lambda}\kappa=-E_+[\psi]\,\delta_{m0},\qquad S_{\lambda\lambda}\kappa=0. \tag{3.4}$$

*If the operator*

$$\text{(I)}\qquad \kappa\longmapsto\big((S_{\Phi_m\lambda}\kappa)_{m\ge1},\ (S_{\Psi_m\lambda}\kappa)_{m\ge1},\ S_{\lambda\lambda}\kappa\big)$$

*is injective, then $E_-[\phi]=0$ and $E_+[\psi]=0$. Without auxiliary variables (Type I, any $K_\pm$), both bulk equations hold with no further condition.*

*Proof.* (a) Apply the $t$-Euler operator $E_Y$ to (3.3$'$). It annihilates $\operatorname{Im}D_t$. It sends $\rho\cdot C$ to $D_C^*\rho+D_\rho^*C$, which equals $D_C^*\rho$ on the prolonged constraint locus $\{D_t^kC=0,\ k\ge0\}$. All identities below hold on that locus. For the left side use the chain rule for Euler operators: if $F$ is local in $z$ and $z=Z[Y]$ is a local map, then $E_Y(F\circ Z)=D_Z^*\,(E_zF\circ Z)$, because $\delta\!\int F(Z)=\int E_zF\cdot D_Z\delta Y=\int D_Z^*E_zF\cdot\delta Y$ modulo total derivatives. Here $E_z\mathcal H_\mp=(b_\mp,a_\mp)$, and $D_{\Pi^-}=-(S_{\Phi\Phi},S_{\Phi\Psi},S_{\Phi\lambda})$, $D_{\Pi^+}=(S_{\Psi\Phi},S_{\Psi\Psi},S_{\Psi\lambda})$, $D_C=(S_{\lambda\Phi},S_{\lambda\Psi},S_{\lambda\lambda})$. Self-adjointness gives, on $C=0$,

$$\begin{aligned}
b_--S_{\Phi\Phi}a_--S_{\Phi\Psi}a_+&=S_{\Phi\lambda}\rho,\\
-S_{\Psi\Phi}a_--b_+-S_{\Psi\Psi}a_+&=S_{\Psi\lambda}\rho,\\
-S_{\lambda\Phi}a_--S_{\lambda\Psi}a_+&=S_{\lambda\lambda}\rho .
\end{aligned}\tag{3.5}$$

Insert $\delta Y=(a_-,a_+,\rho)$ into (3.2). The third line of (3.5) is the linearised constraint. The first two lines give $\delta\pi_-=-b_-$ and $\delta\pi_+=-b_+$, which are the momentum components of $X_\mp$. The configuration components are $\delta\Phi=a_-$ and $\delta\Psi=a_+$.

(b) Differentiating (3.1) in $x$ shows that $D_xz$ is tangent, with $\delta Y=D_xY$. By (a), $X$ is tangent, with $\delta Y=(a_-,a_+,\rho)$. By Lemma 2.2, $D_x\Phi=a_-$ and $D_x\Psi=a_+$, because the momenta are the actual ones. The difference of the two tangent vectors therefore has $\delta Y=(0,0,\kappa)$. Then (3.2) gives $D_x\pi_-+b_-=-S_{\Phi\lambda}\kappa$, $D_x\pi_++b_+=S_{\Psi\lambda}\kappa$ and $S_{\lambda\lambda}\kappa=0$. By Lemma 2.2 the left sides vanish for $m\ge1$, and equal $-E_-$ and $-E_+$ respectively for $m=0$. This is (3.4). Under (I), $\kappa=0$, and (3.4) gives $E_\mp=0$. $\square$

**Remarks 3.4.**
1. *What is not needed.* The proof uses neither a Lagrangian-submanifold property of $\Gamma_d$, nor transversality, nor connectedness. The symplectic interpretation is given in Appendix A.
2. *Condition (I) cannot be dropped.* Between two copies of a relativistic scalar with even potential, the defect $S_d=\int\lambda(\psi+\phi)\,dt$ conserves momentum: $C=\psi+\phi$, and $\mathcal H_--\mathcal H_+\in\langle C\rangle$. Here $K=1$ and $S_{\lambda\lambda}=0$, so the operator (I) is zero, and the conclusion of (b) fails. For the massive Klein–Gordon field, $(\phi,\psi,\lambda)=(x^2,-x^2,2x)$ is a promoted solution, but $E_-[\phi]=2-m^2x^2\ne0$ (`checks/check_scope.py`). The relation $\psi=-\phi$ maps solutions to solutions only because $\phi\mapsto-\phi$ is a symmetry. Theorem 3.3 is only the Bäcklund half of the observation. Integrability needs the nondegenerate families of Section 6, which this defect does not have.
3. *Condition (I) in practice.* It is vacuous for Type I. For the multiplier defects of KdV and mKdV, $S_{\Phi_1\mu}=\partial C/\partial\Phi_1=1$, so (I) holds. For relativistic Type-II defects it reduces to injectivity of the multiplication operator $S_{\lambda\lambda}=-\partial_\lambda^2\mathcal D$.
4. *Heterogeneous defects.* Theorem 3.3 does not need $\mathcal L_-=\mathcal L_+$. For instance, a momentum-conserving defect between Liouville theory and a free massless field is a Bäcklund relation linearising Liouville theory.

### 3.4 The second sewing equation

**Lemma 3.5.** *Let $S_d$ be momentum-conserving, and let $\phi$ solve $E_-[\phi]=0$. Suppose $(\Psi,\lambda)$ solve the left sewing equations $\pi_-[\phi]=\Pi^-(Y)$ and $C(Y)=0$ at every $x$. If*

$$\text{(T)}\qquad (\eta,\kappa)\longmapsto\big(S_{\Phi\Psi}\eta+S_{\Phi\lambda}\kappa,\ S_{\lambda\Psi}\eta+S_{\lambda\lambda}\kappa\big)$$

*is injective, then $\Pi^+(Y)$ is the Ostrogradsky momentum of $\psi:=\Psi_0$. Hence the right sewing equations hold, and $E_+[\psi]=0$.*

*Proof.* Put $z_+=(\Psi,\Pi^+(Y))$. As in Theorem 3.3(b), $D_xz$ and $X$ are tangent, and $D_xz_-=X_-$ because $\phi$ is on shell. Their difference has $\delta Y=(0,\eta,\kappa)$, with $\eta=D_x\Psi-a_+(z_+)$, and its $\delta\pi_-$ and constraint components vanish. By (T), $\eta=0$ and $\kappa=0$. So $D_x\Psi=a_+(z_+)$ and $D_x\Pi^++b_+(z_+)=0$. The configuration equations identify $\Psi_m=D_x^m\psi$ and $\Pi^+_{K-1}=\partial\mathcal L_+/\partial\psi_{0,K}$. The momentum equations, read downward from $m=K-1$, identify every $\Pi^+_m$ with $\pi_m[\psi]$; the equation for $m=0$ is $E_+[\psi]=0$. $\square$

---

## 4. Defect charges, potentials and closure

### 4.1 Defect charges

Let $(N,J)$ be a conservation law of each bulk theory: $D_tN_\pm+D_xJ_\pm=0$ on shell. A **defect charge** for it is a local $Q_d(Y)$ with

$$D_tQ_d\equiv J_-\big|_{x=0}-J_+\big|_{x=0}\pmod{\langle C\rangle}\quad\text{on }\Gamma_d. \tag{4.1}$$

Then $\int_{x<0}N_-+\int_{x>0}N_++Q_d$ is conserved.

**Lemma 4.1 (Noether charges at a defect).** *Let $v_Q$ be an evolutionary symmetry of both bulk Lagrangians, whose characteristic $Q$ may depend on $t$ but not on $x$. Suppose that:*

1. *$\operatorname{pr}v_Q\mathcal L_\pm=D_tA_\pm$, with no $x$-flux;*
2. *$D_x^mQ|_{x=0}$ is a local function $Q_{\Phi_m}$ of the boundary data, and likewise on the right;*
3. *for a prescribed action $Q_\lambda$ on $\lambda$, $\operatorname{pr}v_Q\mathcal L_d=D_tA_d$.*

*Then the Noether law $N=A-\Xi(Q)$, $J=-\sum_m\pi_m\cdot D_x^mQ$ has the defect charge $Q_d=A_d-\Xi_d(Q)$, where $\Xi_d$ is the temporal boundary term (2.3) of $\mathcal L_d$. Moreover, every trivial law $(N,J)=(D_x\nu,-D_t\nu)$, with $\nu$ local, has the defect charge $\nu_+-\nu_-$.*

*Proof.* Equation (2.1) with $\eta=Q$ gives the current. At $x=0$ the sewing equations give

$$J_--J_+=\sum_mE_{\Phi_m}\mathcal L_d\cdot Q_{\Phi_m}+\sum_mE_{\Psi_m}\mathcal L_d\cdot Q_{\Psi_m}=\operatorname{pr}v_Q\mathcal L_d-E_\lambda\mathcal L_d\cdot Q_\lambda-D_t\Xi_d(Q),$$

by the temporal analogue of (2.1) for $\mathcal L_d$. On $C=0$ this is $D_t(A_d-\Xi_d(Q))$. For the trivial law, $D_t(\nu_+-\nu_-)=J_--J_+$ identically. $\square$

A law whose density is a total $x$-derivative need not be trivial off shell, and then need not have the defect charge $\nu_+-\nu_-$. For the potential KdV Lagrangian $\mathcal L=\frac12p_xp_t-p_x^3-\frac12p_{xx}^2$, the mass law $(p_x,\ p_{xxx}-3p_x^2)$ has flux $\pi_0-\frac12p_t$, not $-p_t$. It is the sum of the trivial law $\frac12(D_xp,-D_tp)$ and minus the Noether law $(-\frac12p_x,-\pi_0)$ of the constant shift $p\mapsto p+\epsilon$. Hence it has the defect charge $\frac12(q-p)-(A_d-\Xi_d(1))$ when the defect satisfies conditions 1–3 for the shift, and none of this form in general. For the KdV defect of [3], $A_d-\Xi_d(1)=\frac12(p-q)$ and the charge is $q-p$. Adding $\beta p^2$ to that defect breaks the shift invariance, and $D_t(q-p)-(J_--J_+)=2\beta p$ (`checks/check_scope.py`).

**Examples.**
- *Time translation* ($Q=-D_t\phi$, $A=-\mathcal L$) gives the defect energy $\mathcal E_d$ of every autonomous defect.
- *A $U(1)$ phase* gives the NLS number charge when the defect is phase invariant.
- *A constant field shift* gives a charge whenever the defect depends on $\phi,\psi$ only through differences and derivatives. A time-linear shift $\phi\mapsto\phi+\epsilon t$, when $\operatorname{pr}v\mathcal L\in\operatorname{Im}D_t$, needs in addition that $(\partial_{D_t\Phi_0}+\partial_{D_t\Psi_0})\mathcal L_d\in\operatorname{Im}D_t$.
- *Spatial translations* violate condition 1. Their defect charge, $Q_d=\widetilde P$, is exactly the hypothesis of Definition 3.1.

### 4.2 Stress potentials along promoted solutions

**Proposition 4.2 (defect charges are spatial potentials).** *Let $(\phi,\psi,\lambda)$ be a promoted solution satisfying (I), so that both bulk equations hold, and let $Q_d$ be a defect charge for $(N,J)$. Put $R:=D_xQ_d+(N_--N_+)$ along the solution. Then $D_tR=0$. Moreover $R\equiv0$ in either of the following settings:*

*(A) the solution is a formal branch (Definition 6.1), so that each coefficient of $R$ in $\epsilon$ is a differential function of $\phi$ alone, and $R$ vanishes at the vacuum;*

*(B) for each $x$ the solution tends, as $t\to-\infty$, to a constant pair at which $R=0$.*

*Hence $D_tQ_d=J_--J_+$ and $D_xQ_d=-(N_--N_+)$ at every point.*

*Proof.* $D_tR=D_xD_tQ_d+D_t(N_--N_+)=D_x(J_--J_+)+D_t(N_--N_+)=0$, using both bulk laws. In setting (A), each coefficient of $R$ is a differential function of $\phi$ with $D_tR=0$ on solutions of $E_-[\phi]=0$. By Lemma 6.3 it is constant, and the constant is its vacuum value. In setting (B), $R(x,\cdot)$ is constant in $t$ and equals its limit. $\square$

The normalisation is a property of the single residual $R$, never global injectivity of $D_t$; a derivation annihilates constants. For energy and momentum, Proposition 4.2 gives the four identities

$$D_t\mathcal E_d=T^{10}_--T^{10}_+,\quad D_x\mathcal E_d=-(T^{00}_--T^{00}_+),\quad D_tP_d=T^{11}_--T^{11}_+,\quad D_xP_d=-(T^{01}_--T^{01}_+).$$

### 4.3 Closure

**Proposition 4.3 (a conserved generating density).** *Let laws 1 and 2 have defect charges $Q^1$ and $Q^2$, and suppose that on each side*

$$N_2+J_1+D_ta_0+D_xb_0=0\quad\text{on shell} \tag{4.2}$$

*for local $a_0$ and $b_0$. Then, along every promoted solution in setting (A) or (B),*

$$D_t\big(Q^1+a_{0,-}-a_{0,+}\big)+D_x\big(b_{0,-}-b_{0,+}-Q^2\big)=0. \tag{4.3}$$

*In setting (A) the vacuum condition of Proposition 4.2 holds automatically for law 2, when $Q^1$ and $Q^2$ are autonomous local functions of the boundary jets.*

*Proof.* $D_tQ^1=J_{1,-}-J_{1,+}=-(N_{2,-}-N_{2,+})-D_t\Delta a_0-D_x\Delta b_0$ by (4.2), and $-(N_{2,-}-N_{2,+})=D_xQ^2$ by Proposition 4.2. Only the residual $R_2=D_xQ^2+(N_{2,-}-N_{2,+})$ of law 2 is used. At a constant solution, $D_t$ and $D_x$ of every differential function vanish. There $R_2=N_{2,-}-N_{2,+}$, the closure relation (4.2) gives $N_2=-J_1$ on each side, and (4.1) gives $J_{1,-}-J_{1,+}=D_tQ^1=0$. Hence $R_2$ vanishes at the vacuum. $\square$

We call $\mathcal G=Q^1+\Delta a_0$ the **generating density**. A density difference such as $T^{01}_--T^{01}_+=-D_xP_d$ is an exact derivative. Its expansion therefore yields only trivial charges and cannot replace $\mathcal G$.

---

## 5. Kinematic symmetry

### 5.1 Affine conservation laws give closure

**Definition 5.1.** An **affine conservation law** is a current $(x a_1+t a_2+a_0,\ x b_1+t b_2+b_0)$, with $a_i,b_i$ local and free of explicit $(x,t)$, that is conserved on shell.

**Lemma 5.2 (closure from kinematic symmetry).** *For an affine conservation law, $(a_1,b_1)$ is a conservation law, $a_2$ is a conserved density, and (4.2) holds with $N_2=a_2$ and $J_1=b_1$. The Noether currents of the following symmetries are affine:*

| bulk theory | symmetry | law 1 | law 2 | $a_0$, $b_0$ | generating density $\mathcal G$ |
|---|---|---|---|---|---|
| relativistic scalars, any potential | Lorentz boost | energy | $-$momentum | $0,\ 0$ | defect energy $\mathcal E_d$ |
| NLS $iu_t+u_{xx}+2\vert u\vert^2u=0$ | Galilean boost | number | $-2\times$momentum | $0,\ 0$ | defect number $N_d$ |
| KdV $u_t=6uu_x-u_{xxx}$ | Galilean symmetry | mass | $3u^2$ ($\propto$ momentum) | $0,\ -u_x$ | $q-p$ (potentials) |
| mKdV $v_t=6v^2v_x+v_{xxx}$ | dilation | $\tfrac12v^2$ (momentum) | $3\times$energy | $0,\ v v_x$ | defect momentum $P_d$ |
| Boussinesq (2.1) of [8] | $u\mapsto u+\epsilon t$ | trivial | shift law | $u/c^2,\ 0$ | $(u-v)/c^2$ |

*Proof.* In the jet space of the equation, $x$ and $t$ are coordinates independent of the fibre coordinates, with $D_tx=D_xt=0$ and $D_xx=D_tt=1$. Expanding the conservation law gives $x(D_ta_1+D_xb_1)+t(D_ta_2+D_xb_2)+(a_2+b_1+D_ta_0+D_xb_0)=0$, and each coefficient vanishes. The rows of the table are direct computations, recorded in `checks/check_kinematics.py`; the Boussinesq row is computed only there, from the Lagrangian of [8]. $\square$

**Corollary 5.3.** *In every row both constituent laws have defect charges:*
- *energy, for every autonomous defect (Lemma 4.1);*
- *momentum, by Definition 3.1;*
- *the NLS number, for phase-invariant defects;*
- *the KdV mass, for the defect of [3], with charge $q-p$: the mass law is a trivial law plus a shift Noether law, and that defect is shift invariant up to the total derivative of its gyroscopic term (Section 4.1 and `checks/check_scope.py`);*
- *the Boussinesq law 2, which is the Noether law of the constant shift, because the defect of [8] depends on $u,v$ only through $u-v$ and derivatives.*

*Hence every observed defect has a conserved generating density along its Bäcklund relation.*

The closure relation is a property of the bulk theory alone. It reflects a kinematic symmetry, not integrability; every massive relativistic theory has the Lorentz closure.

### 5.2 Families from kinematic symmetries

**Lemma 5.4 (dilation families).** *Let $\delta_s:(x,t,\phi)\mapsto(sx,s^{\alpha}t,s^{\beta}\phi)$, with $\beta$ a vector of weights, satisfy $\mathcal L_\pm\circ\delta_s=s^{w}\mathcal L_\pm$ exactly, for the chosen representatives $\mathcal L_\pm$. If $S_d$ is momentum-conserving, then so is $S_d^{(s)}[Y]:=c(s)\,S_d[\delta_sY]$ for every $s>0$. Here $c(s)>0$ is the factor that makes the total action scale homogeneously.*

*Proof.* $\delta_s$ fixes the line $x=0$ and each half-line. Because the representatives are homogeneous, it maps the Ostrogradsky data, the momenta and $\mathcal H_\pm$ homogeneously, and maps the sewing equations of $S_d^{(s)}$ to those of $S_d$. Hence it maps identity (3.3) for $S_d$ to a nonzero multiple of identity (3.3) for $S_d^{(s)}$. $\square$

Homogeneity up to a spatial divergence is not enough, because $\pi_m$ and $\mathcal H_\pm$ depend on the representative. If $\mathcal L_\pm\circ\delta_s=s^w(\mathcal L_\pm+D_xB_\pm)$, the half-line integrals produce the boundary term $\int dt\,(B_--B_+)|_{x=0}$, which must be moved into the transformed defect action. For example, take $\mathcal L=\frac12(w_t^2-w_x^2)+D_x(\frac12w^2)$ on both sides and $\mathcal L_d=\phi\psi_t+\frac12(\psi^2-\phi^2)$, which conserves momentum. Under $(x,t,\phi)\mapsto(sx,st,\phi)$ the definition above gives $\mathcal L_d^{(s)}=\phi\psi_t+\frac1{2s}(\psi^2-\phi^2)$, which violates (3.3) for $s\ne1$ (`checks/check_scope.py`). The bulk Lagrangians used here for KdV, mKdV and NLS are strictly homogeneous, and the KdV, mKdV and NLS defects of [3] are homogeneous under the bulk dilations, with the defect parameter of weight $2$, $1$ and $1$ respectively (`checks/check_kinematics.py`). Their parameters are therefore dilation orbits.

**Lemma 5.5 (Lorentz families).** *Let $\mathcal L_\pm$ be Lorentz-invariant scalar theories, so that $T^{\mu\nu}$ is a symmetric tensor. Let $(\phi,\psi,\lambda)$ range over the promoted solutions of a momentum-conserving defect satisfying (I), with stress potentials $\mathrm{Pot}^0=\mathcal E_d$ and $\mathrm{Pot}^1=P_d$:*

$$\Delta T^{\mu\nu}=\varepsilon^{\mu\rho}D_\rho\mathrm{Pot}^\nu .$$

*For a boost $\Lambda$, the boosted pairs again solve both bulk equations, with stress potentials $\Lambda^\nu{}_\beta\,\mathrm{Pot}^\beta\circ\Lambda^{-1}$. In particular, along the boosted solutions, momentum is conserved across the line $x=0$.*

This is an identity along promoted solutions. When the boosted relation is in sewing form at $x=0$, it is a momentum-conserving defect in the sense of Definition 3.1 only if the transported potential is a local function of its boundary data and the balance holds on all its constrained boundary jets; this is checked case by case. For sine-Gordon the boost only changes the defect parameter (below), so it holds.

*Proof.* $T'^{\mu\nu}(x)=\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta T^{\alpha\beta}(\Lambda^{-1}x)$, and derivatives transform by $\partial'=\Lambda^{-T}\partial$. Since $\det\Lambda=1$ we have $\Lambda\varepsilon\Lambda^T=\varepsilon$, that is $\Lambda\varepsilon=\varepsilon\Lambda^{-T}$. Hence $\Delta T'^{\mu\nu}=\varepsilon^{\mu\rho}\partial'_\rho(\Lambda^\nu{}_\beta\mathrm{Pot}^\beta\circ\Lambda^{-1})$. $\square$

For the sine-Gordon defect of [1], with $\mathcal L_d=\tfrac12(\phi\psi_t-\psi\phi_t)-\mathcal B$ and $\mathcal B=2\sigma^{-1}(1-\cos\frac{\phi-\psi}2)+2\sigma(1-\cos\frac{\phi+\psi}2)$, a boost maps the sewing relations with parameter $\sigma$ to those with parameter $\sigma e^{\pm\theta}$. This is the familiar origin of the defect's spectral parameter [1].

---

## 6. The hierarchy from a transparent family

**Definition 6.1 (formal branch).** Let $\mathcal L_-=\mathcal L_+=\mathcal L$. A family $S_d^{(\epsilon)}$, $\epsilon\in(0,\epsilon_0)$, of momentum-conserving defects (or of promoted relations, Lemma 5.5) has a **formal branch** if there are a local invertible symmetry $g$ of $\mathcal L$ (the identity, a constant shift, or $\phi\mapsto-\phi$) and formal series

$$\psi=g(\phi)+\sum_{n\ge1}\epsilon^n\Psi_n[\phi],\qquad \lambda=\sum_{n\ge n_0}\epsilon^n\Lambda_n[\phi], \tag{6.1}$$

with local coefficients, such that for every solution of $E[\phi]=0$ every promoted sewing equation holds, and $E[\psi]=0$, as formal series in $\epsilon$. Under condition (I) the last requirement follows from the others, by Theorem 3.3(b). Constant offsets in $\psi-g(\phi)$ that solve the vacuum sewing equations are allowed, possibly of negative order in $\epsilon$; KdV needs one.

**Lemma 6.2 (formal implicit function).** *Let $G(\phi,\Delta;\epsilon)=0$ be a system of local equations for $\Delta=\psi-g(\phi)$ (and for $\lambda$), formal in $\epsilon$, with $G(\phi,\Delta;0)=M\Delta+O(\Delta^2)$ for an invertible constant (or pointwise invertible algebraic) matrix $M$. Suppose that derivatives of $\Delta$ enter only at positive order in $\epsilon$. Then $G=0$ has a unique formal solution $\Delta=\sum_{n\ge1}\epsilon^n\Delta_n$ with local coefficients.*

*Proof.* Substitute the series. Since $\Delta=O(\epsilon)$, the coefficient of $\epsilon^n$ in $G$ is $M\Delta_n$ plus a local expression in $\Delta_1,\dots,\Delta_{n-1}$ and their derivatives: the terms of order $\Delta^2$ at $\epsilon^0$ involve only lower coefficients, and derivatives of $\Delta$ carry a factor $\epsilon$. Induct on $n$. $\square$

**Lemma 6.3 (no first integrals in $t$).** *Let $\mathcal L$ be admissible, of spatial order $K$.*

*(a) $E(\mathcal L)=(-1)^K\frac{\partial^2\mathcal L}{\partial\phi_{0,K}^2}\,D_x^{2K}\phi+(\text{terms of spatial order at most }2K-1)$. Hence, on the formal solution manifold of $E(\mathcal L)=0$, the jets $D_t^aD_x^j\phi$ with $a\ge0$ and $0\le j\le2K-1$ are free coordinates, every other jet is a local function of them, and $D_t$ maps the coordinate $D_t^aD_x^j\phi$ to $D_t^{a+1}D_x^j\phi$.*

*(b) A differential function $R$, without explicit $(x,t)$ and defined on a connected domain, with $D_tR=0$ on solutions of $E(\mathcal L)=0$ is constant. The same holds coefficientwise for formal series in $\epsilon$.*

*Proof.* (a) In $E=\sum_{k,a}(-D_x)^k(-D_t)^a\,\partial\mathcal L/\partial\phi_{a,k}$, each $\partial\mathcal L/\partial\phi_{a,k}$ has spatial order at most $K$. By admissibility it vanishes for $a\ge1$ unless $k\le K-1$. So every term with $a\ge1$ or $k<K$ has spatial order at most $2K-1$. In $(-D_x)^K\partial\mathcal L/\partial\phi_{0,K}$ the only jet of spatial order $K$ inside the derivative is $\phi_{0,K}$, so the only jet of spatial order $2K$ produced is $\phi_{0,2K}$, with the stated invertible coefficient. Solve $E=0$ for $\phi_{0,2K}$. Its derivatives $D_t^aD_x^bE=0$ have the distinct leading jets $\phi_{a,2K+b}$ and express each of them through jets of lower spatial order. By induction on spatial order every jet with $j\ge2K$ is a local function of the stated coordinates, and these satisfy no relation.

(b) In these coordinates $R$ depends on finitely many of them; let $A$ be the largest $t$-order that occurs. Then $D_tR=\sum_{a\le A}\sum_{j<2K}\partial R/\partial(D_t^aD_x^j\phi)\cdot D_t^{a+1}D_x^j\phi$. The coordinates $D_t^{A+1}D_x^j\phi$ do not occur in $R$ or in its derivatives, and they enter $D_tR$ linearly with coefficients $\partial R/\partial(D_t^AD_x^j\phi)$. These coefficients therefore vanish. Descending induction on $A$ leaves $R$ independent of every coordinate, so $R$ is constant. $\square$

For a relativistic scalar, (a) is the normal form $\phi_{xx}=\phi_{tt}+U'(\phi)$, with free coordinates the $t$-jets of $\phi$ and $\phi_x$. Writing the wave equation as a first-order system in $t$ does not help, because its highest-order symbol is nilpotent.

**Theorem 6.4 (hierarchy).** *Let a family have a formal branch, and let $\mathcal G$ be a generating density (Proposition 4.3) normalised to vanish at the vacuum, with flux $\mathcal F$. Expand*

$$\mathcal G\big(\phi,\psi(\epsilon),\lambda(\epsilon);\epsilon\big)=\sum_{n}\epsilon^nQ_n[\phi],\qquad \mathcal F=\sum_n\epsilon^n\mathcal J_n[\phi].$$

*Then $D_tQ_n+D_x\mathcal J_n=0$ on shell for every $n$, with $Q_n$ and $\mathcal J_n$ local.*

*Proof.* The branch is a promoted solution in setting (A) of Proposition 4.2: both bulk equations hold (Definition 6.1), and the coefficients of the residuals are differential functions of $\phi$. By Lemma 6.3 they are constant. Proposition 4.3 uses only the residual of law 2, whose vacuum value vanishes automatically (Proposition 4.3, last statement). Proposition 4.3 then gives (4.3) as an identity of formal series; take coefficients. $\square$

**Lemma 6.5 (kinematic weights).** *Let $g_\theta$ be a one-parameter group of point symmetries of $\mathcal L$ that fixes the vacuum and acts on solutions. Suppose that:*
1. *$g_\theta$ maps the member with parameter $\epsilon$ to the member with parameter $e^{w\theta}\epsilon$, where $w\ne0$;*
2. *it maps the selected formal branch to the selected branch of the image member (for example, because both are the unique solution of Lemma 6.2);*
3. *on shell it maps the closed 1-form $\mathcal G\,dx-\mathcal F\,dt$ of (4.3) for $\epsilon$ to $e^{w_0\theta}$ times the 1-form for $e^{w\theta}\epsilon$, up to exact forms;*
4. *writing its action on phase-space data as $v\mapsto L_\theta v+B_\theta(v,v)+O(v^3)$, each $Q_{n,1}[B_\theta(v,v)]$ is a trivial functional. This holds when the induced action on phase-space data is linear, as for the dilations of Section 5.2 in the variables used here, or when the $Q_n$ have no linear parts. A Lorentz boost is linear on spacetime fields but not, in general, on phase-space data: at $t=0$ the infinitesimal boost gives $\delta\phi_t=\phi_x+x(\phi_{xx}-U'(\phi))$, whose quadratic part $-\frac12U'''(0)\,x\phi^2$ vanishes only when $U'''(0)=0$, as for sine-Gordon.*

*Then the conserved functionals $\bar Q_n=\int Q_n\,dx$ satisfy $g_\theta^*\bar Q_n=e^{(w_0+nw)\theta}\bar Q_n$. The linearised action $L_\theta$ induces a one-parameter group $T_\theta$ of linear maps of quadratic symbols, and $T_\theta m_n=e^{(w_0+nw)\theta}m_n$. Nonzero symbols with distinct $n$ are therefore linearly independent.*

*Proof.* Compare coefficients of $\epsilon^n$ in condition 3, using condition 2 to identify the coefficients on both sides. Integrate over a Cauchy line; a closed 1-form gives the same integral over $t=0$ and over its image under $g_\theta$, for fields that decay in $x$. The quadratic part of $\bar Q_n\circ g_\theta$ is $Q_{n,2}[L_\theta v]+Q_{n,1}[B_\theta(v,v)]$, and by condition 4 the second term is trivial. Since $g_\theta$ fixes the vacuum, $L_\theta$ maps the linearised theory to itself and acts linearly on its normal modes, and hence on quadratic symbols. Because $w\ne0$, the exponents $w_0+nw$ are distinct, and eigenvectors of a linear map with distinct eigenvalues are linearly independent. $\square$

For a dilation the 1-form transforms by a power of $s$ and $T_\theta$ rescales $k$. For a Lorentz boost, $(\mathcal G,\mathcal F)=(\mathcal E_d,P_d)$ transforms as a vector (Lemma 5.5) and the 1-form is invariant, so $w_0=0$; with $k=m\sinh\vartheta$, $T_\theta$ shifts $\vartheta$ and includes the factor $\omega(k)$ of the measure, so that $m_n/\omega$ are its eigenfunctions. Condition $w\ne0$ is needed: if the parameter does not move, all exponents coincide, and a series such as $\frac{\epsilon}{1-\epsilon}m_*(k)$ has infinitely many nonzero but proportional coefficients. Condition 4 is needed as well. For $\mathcal L=U_tV_t-U_xV_x$ in the variables $q=U-V^2$, $r=V$, whose spatial Hessian has determinant $-1$, the symmetry $(U,V)\mapsto(aU,a^{-1}V)$ acts by $q\mapsto aq+(a-a^{-2})r^2$, $r\mapsto a^{-1}r$. The conserved charge $\int U_t\,dx=\int(P_r-2rP_q)\,dx$ scales by $a$, but its quadratic part $-2\int rP_q\,dx$ scales by $a^{-2}$ under the linearised action (`checks/check_scope.py`).

**Lemma 6.6 (gyroscopic Type-I defects).** *Let $\mathcal L$ be a first-order relativistic theory, and let $\mathcal L_d^{(\epsilon)}$ be a family of momentum-conserving defects of the form*

$$\mathcal L_d^{(\epsilon)}=A_\Phi(\Phi,\Psi)\cdot\Phi_t+A_\Psi(\Phi,\Psi)\cdot\Psi_t-\epsilon^{-1}\mathcal B_-(\Phi,\Psi)-\sum_{k\ge0}\epsilon^k\mathcal B_k(\Phi,\Psi).$$

*Suppose $\mathcal B_-$ vanishes to second order on the diagonal $\Psi=\Phi$, with invertible Hessian $\mathsf H=\partial^2\mathcal B_-/\partial\Phi^2|_{\Psi=\Phi}$. Then the family has a formal branch with $g=\mathrm{id}$.*

*Proof.* Multiply the left sewing equation by $\epsilon$. Its leading term is $\nabla_\Phi\mathcal B_-(\phi,\phi+\Delta)=-\mathsf H\Delta+O(\Delta^2)$, while the gyroscopic terms, which contain the only derivatives of $\Delta$, carry a factor $\epsilon$. Lemma 6.2 gives $\Delta$. In condition (T) of Lemma 3.5, $S_{\Phi\Psi}=\epsilon^{-1}\mathsf H+O(1)$ as a formal series of differential operators. Its leading coefficient is invertible, so (T) holds on formal series. Lemma 3.5, which uses momentum conservation, then gives the right sewing equation. $\square$

Momentum conservation cannot be dropped. Between massive Klein–Gordon fields, $\mathcal L_d=-(\phi-\psi)^2/(2\epsilon)$ has the form above with $\mathsf H=1$ but does not conserve momentum. Its left sewing equation gives $\psi=\phi+\epsilon\phi_x$, and its right one then forces $\epsilon\phi_{xx}=0$ (`checks/check_scope.py`).

For the $a_r^{(1)}$ affine Toda defects of [2], $\mathcal B_-$ is a sum of exponentials of $\tfrac12\alpha_j\cdot\mathsf D(\phi-\psi)$ over the affine roots. Its Hessian on the diagonal is $\tfrac m4\mathsf D^T(\sum_j\alpha_j\alpha_j^T)\mathsf D$, which is positive definite because the roots span $\mathbb R^r$ and $\mathsf D$ is invertible.

---

## 7. Involution and independence

### 7.1 Setting

Let the bulk equation be Hamiltonian, $v_t=\mathcal J\,\delta H/\delta v$, with a **constant-coefficient** skew-adjoint operator $\mathcal J$ and a vacuum-normalised local $H=H_2+H_{\ge3}$. The linearised system $v_t=\mathcal J\,\delta H_2/\delta v$ has normal modes $a_j(k)$ with real-analytic frequencies $\omega_j(k)$. A monomial $\prod_ia_{j_i}^{(s_i)}(k_i)$, where $s_i=-1$ marks a complex conjugate, has momentum $\sum s_ik_i$ and frequency $\Omega=\sum_is_i\omega_{j_i}(k_i)$.

The massive observed cases fit this setting:

| bulk theory | $\mathcal J$ | $\omega(k)$ |
|---|---|---|
| relativistic scalars | canonical on $(\phi,\phi_t)$ | $\pm\sqrt{k^2+m_j^2}$ |
| NLS | $-i$ | $k^2$ |
| KdV, mKdV | $D_x$ | $k^3$ |
| Boussinesq | canonical on $(u,u_t/c^2)$ | $\pm ck\sqrt{1+\kappa^2k^2}$ |

**Definition 7.1 (nonresonance).**
- (NR) For every $n\ge3$ and every choice of labels and signs, $\Omega$ does not vanish identically on any nonempty open subset of the hyperplane $\sum s_ik_i=0$.
- (NR2) Every quadratic local functional conserved by the linearised flow is a function of the actions $|a_j(k)|^2$. This holds when distinct normal modes of equal momentum have distinct frequencies on a dense set.

(NR) holds for every degree $n\ge3$ as soon as no branch $\omega_j$ is affine on an interval. On the hyperplane, eliminate $k_n=-s_n\sum_{i<n}s_ik_i$. For distinct $i,j<n$, which exist since $n\ge3$,
$$\frac{\partial^2\Omega}{\partial k_i\,\partial k_j}=s_is_js_n\,\omega_{j_n}''(k_n).$$
If $\Omega$ vanished on an open subset, $\omega_{j_n}''$ would vanish on an open interval. This is excluded for every row of the table, since $\omega$ is real-analytic and $\omega''\not\equiv0$ for $\sqrt{k^2+m^2}$ with $m>0$, $k^2$, $k^3$ and $k\sqrt{1+\kappa^2k^2}$ (`checks/check_scope.py`; `checks/check_kinematics.py` also samples degrees 3 and 4). The massless wave $\omega=|k|$ violates (NR), since $\omega(k_1)+\omega(k_2)-\omega(k_1+k_2)=0$ for all $k_1,k_2>0$. Condition (NR2) fails for degenerate branches, such as the conjugate particles of $a_r^{(1)}$ Toda for $r\ge2$, whose masses coincide.

### 7.2 Rigidity, involution and independence

**Lemma 7.2 (rigidity).** *Assume (NR). Let $F$ be a local functional with polynomial or analytic density, conserved by $H$, whose homogeneous parts of degrees $0,1,2$ vanish. Then $F=0$, that is, its density is a total $x$-derivative.*

*Proof.* Let $F_d$ be the lowest nonzero part, so $d\ge3$. Since $\mathcal J$ is constant, $\{F_a,H_b\}$ has degree $a+b-2$. The degree-$d$ part of $\{F,H\}=0$ is therefore $\{F_d,H_2\}=0$, so $F_d$ is conserved by the linearised flow. In normal modes

$$F_d=\int_{\sum s_ik_i=0}c(k)\prod_ia_{j_i}^{(s_i)}(k_i)$$

with $c$ continuous. Conservation gives $c\,\Omega=0$ on the hyperplane. By (NR) the zero set of $\Omega$ has empty interior, so $c\equiv0$ and $F_d=0$, a contradiction. A homogeneous polynomial local functional vanishes exactly when its density is a total derivative. For an analytic density the argument applies to each homogeneous part in turn, so $F=0$ as a formal series; nothing is claimed for smooth densities that are flat at the vacuum. $\square$

**Theorem 7.3 (involution).** *Assume (NR). Let $Q_n$ be vacuum-normalised local functionals conserved by $H$, with polynomial or analytic densities, such that*

$$\text{(L)}\qquad \{Q_{n,1},Q_m\}=0\quad\text{for all }n,m,$$

*where $Q_{n,1}$ is the linear part. Assume either that the quadratic parts $Q_{n,2}$ commute pairwise, or (NR2) together with*

$$\text{(L}'\text{)}\qquad \{Q_{n,1},H_3\}=0\quad\text{for all }n.$$

*Both conditions are vacuous without linear parts and hold for Casimirs, such as $\int u$ for $\mathcal J=D_x$; (L$'$) also holds when $H$ has no cubic part. Then $\{Q_n,Q_m\}=0$ for all $n,m$.*

*Proof.* $B=\{Q_n,Q_m\}$ is local, and it is conserved by the Jacobi identity. Since $\mathcal J$ is constant, $\{F_a,G_b\}$ has degree $a+b-2$. By (L) the parts of $B$ of degrees $0$ and $1$ vanish, and its quadratic part is $\{Q_{n,2},Q_{m,2}\}$. In the first alternative this vanishes. In the second, the quadratic part of $\{Q_n,H\}=0$ is $\{Q_{n,2},H_2\}+\{Q_{n,1},H_3\}=0$, so by (L$'$) each $Q_{n,2}$ is conserved by the linearised flow. Under (NR2) it is then a function of the actions, and two such functionals commute. In both cases Lemma 7.2 gives $B=0$. $\square$

Without (L$'$) the quadratic parts need not be conserved by the linearised flow. For canonical fields $(q,p)$, let $f=-p_x^2-2pp_{xx}$, the gradient of $\int pp_x^2$, and let $H=\frac12\int[(q+f)_x^2+p_x^2]\,dx$. This is the free Schrödinger Hamiltonian in the canonical coordinates $(q+f,p)$, so (NR) and (NR2) hold. The charges $Q=\int(q+p_x^2)\,dx$ and $R=\int pq_x\,dx$ are conserved, commute and satisfy (L), but $\{Q_2,H_2\}=-2\int p_{xx}q_{xx}\,dx\ne0$ (`checks/check_scope.py`).

**Theorem 7.4 (independence).** *Suppose the quadratic symbols $m_n(k)$ of $Q_n$, for $n$ in a finite set $S$, are linearly independent functions. Then there is a field $v_0$, supported on finitely many Fourier modes, such that the gradients $\delta Q_n$, $n\in S$, are linearly independent at $\varepsilon v_0$ for every sufficiently small $\varepsilon\ne0$, and hence on a neighbourhood of each such field. In particular the $Q_n$ are functionally independent and nontrivial.*

*Proof.* At $v=\varepsilon v_0$, with $v_0$ supported on modes $k_1,\dots,k_M\ne0$, $M\ge|S|$ and all $\hat v_0(k_l)\ne0$, we have $\delta Q_n(v)=\varepsilon\,m_n(k_l)\hat v_0(k_l)+O(\varepsilon^2)$ on mode $k_l$; a linear part contributes only at $k=0$. Linearly independent functions admit points $k_l$ at which the matrix $(m_n(k_l))$ has full rank. For small $\varepsilon\ne0$ the gradients remain independent. $\square$

The choice of modes matters. The symbols $1$ and $k^2$ of $\frac12\int u^2$ and $\frac12\int u_x^2$ are independent, but at $u=\varepsilon\cos kx$ the gradients satisfy $\delta\frac12\int u_x^2=k^2\,\delta\frac12\int u^2$.

**Proposition 7.5 (generating quadratic symbol).** *Let a family have a formal branch and a generating density $\mathcal G$, with charges $Q_n$ regarded as functionals of the phase-space variables $v$ of Section 7.1, every $t$-derivative being reduced with the full field equations. Put $m(k;\epsilon)=\sum_n\epsilon^nm_n(k)$, where $m_n$ is the quadratic symbol of $Q_n$. Suppose that the quadratic part $F_2$ of the evolution $v_t=F[v]$ is zero or a total $x$-derivative. Suppose also that $\mathcal G$ and the branch equation are local differential functions of $v$ and $\Delta$, and that the branch is the unique solution given by Lemma 6.2. Evaluate $\mathcal G$ at $v=\eta(aE+\bar aE^{-1})$, $E=e^{ikx}$, with no corrections of higher order in $\eta$, letting $D_t$ act by the linearised flow, $D_tE=-i\omega(k)E$. Solve the branch equation for $\Delta$ exactly in $\epsilon$, at order $\eta$ for the first harmonic and at order $\eta^2$ for the zero mode. Then $m(k;\epsilon)$ is the coefficient of $\eta^2|a|^2$ in the $x$-average of $\mathcal G$.*

*Proof.* Expand the phase-space function $\mathcal G$ at $v=\eta v_1$. At order $\eta$ only first harmonics occur, including those from linear parts, and they average to zero. At order $\eta^2$ the $x$-average is the quadratic part evaluated on $v_1$, which is $|a|^2m(k;\epsilon)$; second harmonics average to zero. Reducing $t$-derivatives with the linearised flow instead of the full one changes the order-$\eta^2$ terms only through $F_2$ and its derivatives, $F_2'[v](F_1[v])$ and so on. These enter linearly, through constant-coefficient operators: the linearised flow, the linearisations of $\mathcal G$ and of the branch equation, and, by Lemma 6.2, the inverse of the latter, which is a formal series in $\epsilon$ of constant-coefficient operators. All of these commute with $D_x$. When $F_2$ is a total $x$-derivative, so is every such term, and it averages to zero. $\square$

The prescription holds the phase-space data at $\eta v_1$. Along an actual solution $\eta v_1+\eta^2v_2+\dots$ the linear part contributes $Q_{n,1}[v_2]$ at order $\eta^2$, which must be subtracted. The hypothesis on $F_2$ holds in every row of the table below: $F_2=0$ for sine-Gordon, NLS and mKdV, $F_2=3D_x(u^2)$ for KdV, and $F_2=(0,\lambda D_x(u_x^2))$ for Boussinesq in the canonical variables $(u,u_t/c^2)$ (`checks/check_scope.py`). It fails for Tzitzéica and for $a_r^{(1)}$ Toda with $r\ge2$, whose potentials have $U'''(0)\ne0$. The locality hypothesis matters for potential variables, which are not local functions of $v$. For KdV with $u=p_x$, the potential equation $p_t=3u^2-u_{xx}$ gives $p_t$ the $x$-average $6\eta^2|a|^2$ on $u=\eta(aE+\bar aE^{-1})$, while the linearised flow gives zero. In the KdV and mKdV rows the branch is therefore computed from the spatial Bäcklund relation of [3], which involves only $u=p_x$ and $\Delta=q-p$ and no $t$-derivative. For KdV it reads $(2+\epsilon D_x)\Delta=-2\epsilon u+\frac\epsilon2\Delta^2$ after removing the vacuum offset, and Lemma 6.2 applies with $M=2$. For sine-Gordon (Lemma 6.6), NLS and mKdV the leading matrix is again constant and invertible. For Boussinesq, `checks/check_symbols.py` finds a unique solution order by order, but Lemma 6.2 has not been checked; its row is evidence only.

**Definition 7.6 (nondegenerate family).** A family with a formal branch is *nondegenerate* if infinitely many $m_n$ are nonzero. Trivial families, such as the one in Remark 3.4.2 or $\psi=\phi$, are degenerate.

For the published defects the generating symbols are as follows. The first four rows use Proposition 7.5. The Boussinesq row is computational evidence only, as explained above.

| bulk theory | $m(k;\epsilon)$ | nonzero orders |
|---|---|---|
| sine-Gordon ($k=\sinh\vartheta$, $\omega=\cosh\vartheta$) | $4\epsilon\,\omega\,e^{\vartheta}/(1+\epsilon^2e^{2\vartheta})$ | all odd; $m_{2j+1}=4(-1)^j\omega e^{(2j+1)\vartheta}$ |
| NLS | $-2\epsilon/(1+\epsilon^2k^2)$ | all odd; $m_{2j+1}\propto k^{2j}$ |
| KdV | $2\epsilon^3/(4+\epsilon^2k^2)$ | all odd $\ge3$; $m_{2j+3}\propto k^{2j}$ |
| mKdV | $-4\epsilon/(1+\epsilon^2k^2)$ | all odd; $m_{2j+1}\propto k^{2j}$ |
| Boussinesq ($c=\kappa=1$, $\lambda=3$) | rational in $\epsilon$, $k$ and $\sqrt{1+k^2}$ | every computed order $\ge4$ |

In the first four rows the symbols of distinct orders are, up to a common factor, distinct powers of $e^{\vartheta}$ or of $k$. They are therefore linearly independent, as Lemma 6.5 predicts from their boost or dilation weights. These families are nondegenerate, and Theorem 7.4 gives infinitely many independent charges. For Boussinesq the weight argument is unavailable, because its parameter is not kinematic. The first 18 nonzero symbols span a space of dimension at least 17. This is evidence, not proof, of infinitely many independent charges.

---

## 8. The main theorem

### 8.1 Statement

**Theorem 8.1 (kinematic integrability theorem).** *Let $\mathcal L$ be an admissible bulk Lagrangian, and assume:*

- *(A) (bulk) the equation of $\mathcal L$ is Hamiltonian with a constant Poisson operator and satisfies (NR);*
- *(B) (momentum) $S_d$ is a momentum-conserving defect (Definition 3.1) between $\mathcal L$ and itself, satisfying (I);*
- *(C) (family) $S_d$ embeds in a nondegenerate family of momentum-conserving defects with a formal branch (Definitions 6.1 and 7.6), whose nonzero quadratic symbols are linearly independent, either by direct computation or by Lemma 6.5;*
- *(D) (closure) $\mathcal L$ has an affine conservation law whose constituent laws have defect charges (Lemma 5.2 and Corollary 5.3);*
- *(E) (charges) the resulting $Q_n$ have polynomial or analytic densities and satisfy (L), and either their quadratic parts commute pairwise, or (NR2) and (L$'$) hold.*

*Then the equation of $\mathcal L$ has infinitely many functionally independent local conserved charges in involution. Moreover every solution of the sewing system imposed at all $x$ is a pair of solutions.*

*Proof.* Theorem 3.3 gives the Bäcklund relation. Proposition 4.3 with Lemma 5.2 gives the generating density. Theorem 6.4 gives local conservation laws, Theorem 7.3 with (A) and (E) their involution, and (C) with Theorem 7.4 their independence. $\square$

Hypothesis (B) is the momentum condition of Corrigan and Zambon. Hypothesis (A) and the closure relation in (D) concern the bulk alone: massive relativistic scalar theories satisfy (NR) and have the Lorentz closure, integrable or not. Hypothesis (E) concerns the charges that the defect produces. Its alternative (NR2) is a bulk condition, but it fails for degenerate mass spectra: two free fields of equal mass have conserved quadratic charges $\int(p_1p_2+q_1Kq_2)$ and $\frac12\int(p_1^2+q_1Kq_1-p_2^2-q_2Kq_2)$, with $K=-\partial_x^2+m^2$, whose bracket is not zero (`checks/check_scope.py`). Section 9 verifies hypothesis (E) for sine-Gordon, NLS, KdV and mKdV and leaves it open for the other cases. Hypothesis (C) is where integrability enters, and deriving it from (B) is the open problem of Section 10. Section 8.2 derives the family and its formal branch from (B) for one class of relativistic defects.

### 8.2 Hypothesis (C) for relativistic Type-I defects

For one class of defects, momentum conservation itself supplies the family required by (C), and with it a formal branch. The class consists of Type-I defects between two copies of a relativistic scalar theory with $r$ components,

$$\mathcal L=\tfrac12\lvert\phi_t\rvert^2-\tfrac12\lvert\phi_x\rvert^2-U(\phi),\tag{8.1}$$

whose kinetic coupling is constant:

$$\mathcal L_d=\tfrac12\,\phi\cdot E\phi_t+\phi\cdot D\psi_t+\tfrac12\,\psi\cdot E\psi_t-\mathcal B(\phi,\psi),\qquad E^T=-E,\quad D=I-E.\tag{8.2}$$

Here $\phi$ and $\psi$ denote the boundary values at $x=0$. The potential $U$ is real analytic near $0$, with $U(0)=0$, $U'(0)=0$ and $M=U''(0)$ positive definite. The defects of [1] and [2] have this form, up to a total time derivative in $\mathcal L_d$, which changes neither the sewing equations nor the defect energy. For sine-Gordon $E=0$ and $D=1$. Put

$$q=\tfrac12(\phi-\psi),\qquad w=\tfrac12(D^T\phi+D\psi),\qquad\text{so that}\qquad \phi=w+Dq,\quad \psi=w-D^Tq,\tag{8.3}$$

using $D+D^T=2I$. Propositions 8.2 and 8.3 are Propositions 3.1 and 3.2 of [23], restated in the notation of this paper. For one field and for $a_r^{(1)}$ Toda, the splitting of $\mathcal B$ and its rescaling were found in [1, 2, 4].

**Proposition 8.2 (splitting).** *Let (8.2) be momentum-conserving (Definition 3.1) with a defect momentum $\widetilde P(\phi,\psi)$ that contains no time derivatives. Then, up to additive constants,*

$$\mathcal B=f(w)+g(q),\qquad \widetilde P=g(q)-f(w),\qquad U(w+Dq)-U(w-D^Tq)=\tfrac12\,f'(w)\cdot g'(q).\tag{8.4}$$

*Conversely, (8.4) implies that (8.2) is momentum-conserving with this $\widetilde P$.*

*Proof.* The sewing equations (3.1) are $\phi_x=E\phi_t+D\psi_t-\mathcal B_\phi$ and $\psi_x=D^T\phi_t-E\psi_t+\mathcal B_\psi$, with $\pi_\mp=-\phi_x,-\psi_x$ and $\mathcal H=-\frac12\lvert\pi\rvert^2-\frac12\lvert\phi_t\rvert^2+U$. Insert them into $\mathcal H_--\mathcal H_+$. The terms quadratic in the velocities cancel, because $DD^T=D^TD=I-E^2$ and $ED=DE$. What remains is

$$\mathcal H_--\mathcal H_+=\phi_t\cdot(D\mathcal B_\psi-E\mathcal B_\phi)+\psi_t\cdot(D^T\mathcal B_\phi+E\mathcal B_\psi)-\tfrac12\lvert\mathcal B_\phi\rvert^2+\tfrac12\lvert\mathcal B_\psi\rvert^2+U(\phi)-U(\psi).$$

Definition 3.1 with a derivative-free $\widetilde P$ asks that $\mathcal H_--\mathcal H_++D_t\widetilde P=0$ for independent values of $\phi,\psi,\phi_t,\psi_t$. The terms linear in the velocities give $\widetilde P_\phi=E\mathcal B_\phi-D\mathcal B_\psi$ and $\widetilde P_\psi=-D^T\mathcal B_\phi-E\mathcal B_\psi$; the remaining terms give $\frac12(\lvert\mathcal B_\phi\rvert^2-\lvert\mathcal B_\psi\rvert^2)=U(\phi)-U(\psi)$. In the coordinates (8.3), $\partial_w=\partial_\phi+\partial_\psi$ and $\partial_q=D^T\partial_\phi-D\partial_\psi$, and the first two identities become $\widetilde P_w=-\mathcal B_w$ and $\widetilde P_q=\mathcal B_q$. Equality of the mixed derivatives of $\widetilde P$ gives $\mathcal B_{wq}=0$, hence $\mathcal B=f(w)+g(q)$ and $\widetilde P=g-f$ up to constants. Then $\mathcal B_\phi=\frac12(Df'+g')$ and $\mathcal B_\psi=\frac12(D^Tf'-g')$, so the third identity is the last equation of (8.4). Each step can be reversed. $\square$

**Proposition 8.3 (the rescaling family).** *In the setting of Proposition 8.2, assume in addition:*

1. *(transparent point) $g'(0)=0$, and $G=g''(0)$ is invertible;*
2. *(irreducibility) there is no orthogonal splitting $\mathbb R^r=V_1\oplus V_2$ with $U=U_1+U_2$ near $0$, where $U_i$ depends only on the component in $V_i$.*

*Then $G=\gamma I$ with $\gamma\ne0$, and, normalising $f(0)=g(0)=0$, $f=4U/\gamma$. For every $\epsilon\ne0$ the defect with the kinetic term of (8.2) and*

$$\mathcal B_\epsilon=\epsilon\,U(w)+\epsilon^{-1}\hat g(q),\qquad \hat g=\frac4\gamma\,g,\qquad \hat g(0)=0,\quad\hat g'(0)=0,\quad\hat g''(0)=4I,\tag{8.5}$$

*is momentum-conserving, with $\widetilde P_\epsilon=\epsilon^{-1}\hat g(q)-\epsilon\,U(w)$. The given defect is the member $\epsilon=4/\gamma$.*

*Proof.* Differentiate the last equation of (8.4) in $q$ at $q=0$. Since $D+D^T=2I$, this gives $Gf'(w)=4U'(w)$. Differentiating in $w$ gives $Gf''=4U''$. Both $f''$ and $U''$ are symmetric, so $Gf''=f''G$, and then $[G,U'']=\frac14G[G,f'']=0$ for every $w$. Diagonalise $G$ by an orthogonal matrix. The mixed second derivatives of $U$ between distinct eigenspaces of $G$ vanish, so near $0$ the potential $U$ is a sum of potentials on the eigenspaces. By irreducibility $G$ has a single eigenvalue $\gamma$, and $\gamma\ne0$ because $G$ is invertible. Hence $f'=4U'/\gamma$ and $f=4U/\gamma$. The last equation of (8.4) is bilinear in $(f',g')$, so it also holds for $(\lambda f,\lambda^{-1}g)$ with any $\lambda\ne0$, and the converse in Proposition 8.2 makes each such defect momentum-conserving. Put $\epsilon=4\lambda/\gamma$. $\square$

Without irreducibility the conclusion holds if $G$ is assumed to be a nonzero multiple of $I$. For sine-Gordon, $f=2\sigma(1-\cos w)$ and $g=2\sigma^{-1}(1-\cos q)$, so $\gamma=2/\sigma$, $\hat g=4(1-\cos q)$ and the defect of [1] is the member $\epsilon=2\sigma$. For the $a_2^{(1)}$ Toda defect of [2], $\gamma=4/\sigma$, $\hat g=g$ and the defect is the member $\epsilon=\sigma$ (`checks/check_type1_family.py`).

**Theorem 8.4 (the family and its formal branch).** *Under the assumptions of Propositions 8.2 and 8.3, the family (8.5) is a family of momentum-conserving defects with a formal branch with $g=\mathrm{id}$ (Definition 6.1). Its generating density $\mathcal E_d=\mathcal B_\epsilon$ vanishes to second order at the vacuum. Hypotheses (A), (B) and (D) of Theorem 8.1 hold, and (L) and (L$'$) in (E) are vacuous. What remains of Theorem 8.1 for this class is nondegeneracy and the linear independence of the nonzero symbols in (C), and in (E) that the quadratic parts commute or that (NR2) holds.*

*Proof.* The kinetic term of (8.2) has the form $A_\Phi\cdot\Phi_t+A_\Psi\cdot\Psi_t$ of Lemma 6.6, with $A_\Phi=-\frac12E\phi$ and $A_\Psi=D^T\phi-\frac12E\psi$. In (8.5), $\mathcal B_-=\hat g(q)$ vanishes to second order on the diagonal $q=0$, and its Hessian in $\phi$ there is $\frac14\hat g''(0)=I$. The term $\epsilon\,U(w)$ is the term $\mathcal B_1$. Every member is momentum-conserving by Proposition 8.3. Lemma 6.6 gives the formal branch. The defect energy of (8.2) is $\mathcal B$, because the kinetic term is linear in the velocities. At the vacuum, $\hat g$ and $U$ vanish to second order, so $\mathcal E_d$ does, and the charges $Q_n$ have no linear parts. They are analytic because $U$ and $\hat g$ are. The bulk is canonical, with the frequencies $\sqrt{k^2+m_j^2}$, $m_j^2>0$ the eigenvalues of $M$, so (A) holds by Section 7.1. The defect is Type I, so (I) is vacuous, and (B) holds. The Lorentz closure and the defect charges of energy (Lemma 4.1) and momentum (Definition 3.1) give (D). $\square$

For one field, $E=0$ and irreducibility is automatic. There is a single dispersion branch, so (NR2) holds and only nondegeneracy and independence remain. For sine-Gordon these are given by the generating symbol of Section 7.2. For the class as a whole, [23] proves the remaining conditions, the commutation of the charges and their independence, by a different argument through equal-time canonicity ([23], Theorem 2.1 and Sections 5–8). Theorem 8.4 does not derive the transparent point from momentum conservation. It is an assumption on the defect potential at a single point, $q=0$.

---

## 9. The observed cases

The following table lists, for each observed case, which hypotheses of Theorem 8.1 were verified for the published defects and how. "Checked" means verified by the accompanying exact computation (Appendix B); for a hierarchy, the order of the check is given.

| case | (B) balance | (I) | family | (D) closure | formal branch | (A) | independence |
|---|---|---|---|---|---|---|---|
| sine/sinh-Gordon, Type I [1] | checked | vacuous | boost; Theorem 8.4 | Lorentz | Lemma 6.6 (all orders); checked to order 5 | massive | Prop. 7.5: all odd orders |
| $a_r^{(1)}$ affine Toda, Type I [2] | checked for $a_2^{(1)}$ | vacuous | boost; Theorem 8.4 (checked for $a_2^{(1)}$) | Lorentz | Lemma 6.6 (all orders) | (NR); (NR2) fails for $r\ge2$ | not computed here; [23] for $a_2^{(1)}$ (comment 4) |
| Liouville, conformal Toda, free massless [1, 2, 4] | checked (Liouville and free) | vacuous | — | Lorentz | — | **fails (NR)** | Theorem 3.3 only |
| Tzitzéica $a_2^{(2)}$, Type II [5] | checked, $P_d=f-g$ | $S_{\lambda\lambda}=-\partial_\lambda^2\mathcal D\ne0$ | boost | Lorentz | Lemma 6.2 on the left sewing equation and the constraint (leading matrix $\mathrm{diag}(2,-6)$, $\epsilon=\sigma^{-1}$); right sewing equation checked to order 3 | massive | not computed here |
| several fields, Type II, fixed affine Toda bulk [9–11] | by [9–11] | per defect | boost | Lorentz | not checked | massive | not computed here |
| NLS [3] | checked | vacuous | dilation | Galilean | checked to order 3, all four sewing equations; all orders from the compatibility of Lamb's transformation [20] | yes | Prop. 7.5: all odd orders |
| KdV [3] (multiplier) | checked | $S_{\Phi_1\mu}=1$ | dilation | Galilean | checked to order 6; all orders from the compatibility of the Wahlquist–Estabrook transformation [17] | yes | Prop. 7.5: all odd orders $\ge3$ |
| mKdV [3] (multiplier) | checked | $S_{\Phi_1\mu}=1$ | dilation | dilation | checked to order 6; all orders from the compatibility of Wadati's transformation [18] | yes | Prop. 7.5: all odd orders |
| Boussinesq [8] | checked | vacuous | $\sigma_0$: modulus, not kinematic | time-linear shift | checked to order 5; compare the Bäcklund transformations of [21, 22] | yes | evidence only (Section 7) |
| Gardner (comment 7) | checked | $S_{\Phi_1\mu}=1$ | $\alpha$: not kinematic | not checked | not checked | yes | not computed |

Comments.

1. *Charges found.* The checks find nontrivial charges at orders 1, 3, 5 for sine-Gordon, KdV and mKdV, and at orders 1, 3 for NLS (to order 3). For the Tzitzéica Type-II defect, $Q_1$ is nontrivial while $Q_2$ and $Q_3$ are conserved but trivial; this is consistent with the absence of a spin-3 charge for the Tzitzéica equation [5]. For Boussinesq they find orders 2, 4, 5, skipping order 3. That matches the absence of charges with spin divisible by three in the Boussinesq hierarchy.
2. *Massless theories.* For the free massless field, Liouville and conformal Toda, Theorem 3.3 shows that the momentum-conserving defects are Bäcklund relations to free fields. These theories are integrable in the sense of linearisability, but Theorem 7.3 does not apply, because their dispersion is resonant on an open set.
3. *Heterogeneous defects.* Theorem 3.3 covers defects between different theories. Theorems 6.4–7.4 assume $\mathcal L_-=\mathcal L_+$, because the transparent limit joins a theory to itself.
4. *Affine Toda.* Lemma 6.6 uses momentum conservation, which [2] establishes for every $r$ and the scripts check for $a_2^{(1)}$. For $a_2^{(1)}$, `checks/check_type1_family.py` confirms that the defect of [2] satisfies the hypotheses of Theorem 8.4: it has the form (8.2), its potential splits as in (8.4), and its transparent point has $\hat g''(0)=4I$. So momentum conservation supplies its family. The same checks confirm the hypotheses of [23, Theorem 2.1] for this defect, with $G$ a multiple of $I$ in place of irreducibility. By that theorem its charges commute and infinitely many are independent; this conclusion rests on [23], which has not been reviewed independently. Independence and involution are not established here for $r\ge2$. They would need the generating symbol, for which Proposition 7.5 does not apply as stated because $U'''(0)\ne0$, and either (NR2) or a direct check that the quadratic parts commute.
5. *Boussinesq.* Its dimensional constants $c,\kappa,\lambda$ exclude a dilation. The parameter $\rho_0$ of [8] is an orbit of the time-linear shift, but $\sigma_0$, which controls transparency, is a genuine modulus of the momentum constraint. Its generating density $(u-v)/c^2$ is linear, and conditions (L) and (L$'$) have not been checked.
6. *Hypothesis (E).* For sine-Gordon, NLS and mKdV the generating density starts at quadratic order in the fields and in $\Delta$, which vanishes at the vacuum, so the $Q_n$ have no linear parts and (L), (L$'$) are vacuous. For KdV the linear parts are multiples of $\int u$, a Casimir of $\mathcal J=D_x$. Each of these theories has a single dispersion branch, so (NR2) holds by the criterion of Definition 7.1. The densities are polynomial (NLS, KdV, mKdV) or analytic (sine-Gordon). Hence (E) holds in these four rows.
7. *Gardner.* The pure Gardner equation $w_t=12c\,ww_x+6w^2w_x+w_{xxx}$, with $w=P_x$ and a constant $c\ne0$, is integrable but has neither a dilation nor a Galilean symmetry. It admits a momentum-conserving defect (`checks/check_gardner.py`). Take the bulk representative $\mathcal L=\frac12(c+P_x)P_t-\frac12(c+P_x)^4+3c^2P_x^2+\frac12P_{xx}^2$ on both sides; the representative matters (Section 5.2). With $w=p-q$ at $x=0$ and a multiplier $\mu$, the defect is $\mathcal L_d=\frac14(q\,p_t-p\,q_t)-\mathfrak B$, where
   $$\mathfrak B=\mu\,(p_x+q_x+2c-\alpha\sin w)+\tfrac\alpha6\cos w\,\big[(c+p_x)^2+(c+q_x)^2-4(c+p_x)(c+q_x)+\alpha(2c+p_x+q_x)\sin w+\alpha^2\big]-3\alpha c^2\cos w-6c^3w .$$
   Without its last two terms, $\mathfrak B$ is the mKdV defect (7.22) of [3] on the constant background $c$. That defect conserves momentum only for the bulk with the advection term $-3c^2P_x^2$, which a Galilean change of frame removes. The two corrections are those of a defect moving with speed $6c^2$ relative to the mKdV frame. The term $-3\alpha c^2\cos w$ has the form of the term $-\frac12\beta c'(t)\cos(\tilde q-q)$ of the moving mKdV defects of [24], with $\lvert c'\rvert=6c^2$. So the defect follows from [24] by a constant shift of the background and a Galilean change of frame. We have not found it stated for the Gardner equation. Condition (I) holds, as for mKdV. The sewing conditions, imposed at every $x$ with the vacuum on the left, give a solution of the Gardner equation, as Theorem 3.3 predicts. The parameter $\alpha$ is not the orbit of a kinematic symmetry, since a dilation also changes $c$. So this is a second case, after Boussinesq, whose family must come from a modulus. Its closure law, the defect charges and the formal branch have not been checked.
8. *The KdV defect as two fused Miura maps.* Take mKdV in the form $v_t=6v^2v_x-v_{xxx}$, with Lagrangian $\frac12q_xq_t-\frac12q_x^4-\frac12q_{xx}^2$ and $v=q_x$. The Miura maps $u_\pm=v^2\pm v_x+\alpha$ carry its solutions to solutions of the KdV equation of [3]. Put $v=\frac12(p-q)$. Then $u_+-u_-=p_x-q_x$, and $u_++u_-=2\alpha+\frac12(p-q)^2$ is the spatial Bäcklund relation (9.12) of [3]. So $u_+=p_x$ and $u_-=q_x$, and the KdV defect of [3] composes two Miura maps through an mKdV field of zero width. A single Miura map does not match the momenta. The momentum densities of Lemma 2.1 are $-\frac12v^2$ for mKdV and $-\frac12u^2$ for KdV, and $\frac12u^2=\frac12v^4+\frac12v_x^2+D_x(\frac13v^3)$ is the mKdV energy density up to a total derivative. In the composition the two images differ by a total derivative, $\frac12u_+^2-\frac12u_-^2=D_x\big(\frac23v^3+2\alpha v\big)$. By Proposition 4.2 the defect momentum therefore satisfies $D_x\widetilde P=\frac12p_x^2-\frac12q_x^2$ along promoted solutions. Indeed $\frac23v^3+2\alpha v=\alpha(p-q)+\frac1{12}(p-q)^3$ is the defect momentum (9.13) of [3] (`checks/check_miura.py`). The momentum stored in the KdV defect is exactly what cancels the two Miura mismatches. The composition of two Miura maps into the Wahlquist–Estabrook transformation is classical; we have not found this reading of the defect momentum stated.

---

## 10. What remains open

1. **Hypothesis (C) from momentum conservation alone.** Theorem 3.3 extracts a Bäcklund relation from a single momentum-conserving defect. A local hierarchy needs a one-parameter family with a regular transparent limit. In the observed cases the family arises in one of two ways:
   - as the orbit of a kinematic symmetry that the defect does *not* preserve: boosts for relativistic theories, dilations for NLS, KdV and mKdV;
   - as a modulus of the momentum constraint: the Boussinesq parameter $\sigma_0$, or, for relativistic Type-I defects, the splitting of the defect potential into two functions $F,G$ with $(F,G)\mapsto(\sigma F,\sigma^{-1}G)$ a symmetry of the constraint [1, 4].

   For relativistic Type-I defects with constant kinetic coupling, Theorem 8.4 derives the modulus and the formal branch from momentum conservation, given a nondegenerate transparent point; [23] then proves nondegeneracy, independence and involution for that class. A general theorem would show that the momentum constraint always has such a modulus, or that the orbit of a kinematic symmetry is always nondegenerate with a regular transparent limit. Even in the class of Theorem 8.4 the transparent point is assumed, not derived.
2. **Bulk selection.** For relativistic scalars, momentum conservation restricts the bulk potentials [1, 2, 4–6]. The present framework does not classify potentials. Its integrability conclusion is conditional on (C), not derived from the form of the potential.
3. **Remaining verifications.** Formal branches are still to be checked for the several-field Type-II defects. Independence and involution remain to be checked for affine Toda with $r\ge2$ by the methods of Section 7 (for $a_2^{(1)}$, [23] supplies them; Section 9, comment 4), and the generating symbol for theories with $U'''(0)\ne0$ needs a version of Proposition 7.5 that keeps the quadratic nonlinearity. Conditions (L) and (L$'$) remain to be checked for Boussinesq.
4. **Function spaces.** Everything here is formal or local. Convergence of the parameter series and global Bäcklund maps are not addressed.

---

## Appendix A. The spatial Hamilton–Jacobi interpretation

Equip the product of spatial phase spaces with $\Omega_-^{(x)}\ominus\Omega_+^{(x)}$, where $\Omega^{(x)}=\int dt\,\delta\Phi\wedge\delta\pi$ [13]. Pulling back the Liouville form $\Theta_-^{(x)}-\Theta_+^{(x)}$ to $\Gamma_d$ gives $-\delta S_d$, so $\Gamma_d$ is isotropic.

Without auxiliary fields, $\Gamma_d$ is also coisotropic in the formal cotangent setting. To see this, pair a vector that is symplectically orthogonal to $T\Gamma_d$ against the variations $(\delta\Phi',0)$ and $(0,\delta\Psi')$. Self-adjointness of the second variations of $S_d$ then shows that the vector lies in $T\Gamma_d$. Thus $\Gamma_d$ is a Lagrangian correspondence in the strong sense $T\Gamma_d^\perp=T\Gamma_d$, generated by $S_d$ [19].

The balance (3.3), integrated over $t$, says that $H_-^{(x)}-H_+^{(x)}$ is constant on $\Gamma_d$. This is the spatial Hamilton–Jacobi equation. For a Lagrangian correspondence, $\delta(H_--H_+)$ vanishes on $T\Gamma_d$ if and only if $(X_-,X_+)$ is tangent to $\Gamma_d$. This gives a geometric proof of Theorem 3.3(a) for Type-I defects. The proof in Section 3 is more direct: it needs neither coisotropy nor the integration over $t$, and it handles auxiliary fields through the multiplier $\rho$.

Conversely, if $(X_-,X_+)$ is tangent to an isotropic $\Gamma_d$, then $\delta(H_--H_+)$ vanishes on $T\Gamma_d$. For a Type-I defect, whose boundary data are free, the density $\mathcal H_--\mathcal H_+$ on $\Gamma_d$ then has vanishing $t$-Euler derivative. It is therefore a total $t$-derivative of a local function plus a constant [16, Thm 4.7]. The constant is the value of $\mathcal H_--\mathcal H_+$ at any stationary point of $\Gamma_d$. If it vanishes, for example because $\Gamma_d$ contains a common vacuum at which $\mathcal H_-=\mathcal H_+$, the sewing-form Bäcklund relation of Type I is a momentum-conserving defect. The normalisation is needed: for $\mathcal L_-=\frac12(\phi_t^2-\phi_x^2)$, $\mathcal L_+=\frac12(\psi_t^2-\psi_x^2)-c$ and $\mathcal L_d=\phi\psi_t$, the sewing equations $\phi_x=\psi_t$, $\psi_x=\phi_t$ form a Bäcklund relation, but $\mathcal H_--\mathcal H_+=-c$ (`checks/check_scope.py`).

## Appendix B. Verification

The accompanying scripts (Python 3 with SymPy) check the hypotheses and several conclusions on the published defects. Each prints one `PASS` or `FAIL` line per check.

- `checks/check_balance.py` checks the momentum balance (3.3) for every observed case.
- `checks/check_tangency.py` checks the conclusion of Theorem 3.3(a) exactly for three defects: sine-Gordon (Type I, $\rho=0$), Tzitzéica (Type II) and KdV (spatial order 2, with a multiplier).
- `checks/check_kinematics.py` checks the table of Lemma 5.2, the boost and dilation examples of Section 5.2, and (NR).
- `checks/check_hierarchy.py` computes formal branches. It checks every promoted sewing equation derived from the published defect Lagrangian, and checks conservation and nontriviality of each computed $Q_n$.
- `checks/check_symbols.py` computes the generating symbols of Proposition 7.5.
- `checks/check_type1_family.py` checks the identities in the proofs of Propositions 8.2–8.3 (for a general skew $E$ with three fields), the sine-Gordon normalisation, and the hypotheses of Theorem 8.4 for the $a_2^{(1)}$ Toda defect of [2].
- `checks/check_gardner.py` checks the bulk equation of the Gardner representative, the momentum balance of the Gardner defect of Section 9 (comment 7), the failure of the uncorrected mKdV defect, and that the sewing conditions imposed at every $x$ on the vacuum give a solution of the Gardner equation.
- `checks/check_miura.py` checks the Miura map and the momentum densities of Section 9, comment 8, the identity $\frac12u^2=\frac12v^4+\frac12v_x^2+D_x(\frac13v^3)$, and the fusion identities that give the defect momentum (9.13) of [3].
- `checks/check_scope.py` checks the examples that show which hypotheses are needed (Sections 3–8 and Appendix A), the defect charge of the KdV mass law, the strict homogeneity of the KdV, mKdV and NLS Lagrangians, and the identities behind (NR) for all degrees and behind the hypotheses of Proposition 7.5, including the KdV branch relation from the spatial Bäcklund relation of [3].

A small Lean 4 project (`lean/`) checks the final algebraic step of Lemmas 2.1–2.2 (spatial orders 1 and 2), Theorem 3.3, Propositions 4.2–4.3 and Lemma 5.2, the identity behind Lemma 5.5, and the induction of Lemma 7.2. It works over an arbitrary commutative ring with commuting derivations and includes a model in which both derivations are nonzero. The substantive inputs enter as hypotheses: the Euler-operator chain rule and Helmholtz self-adjointness, which yield (3.5), and the nonresonance step of Lemma 7.2. Theorem 8.1 is not formalised.

---

## References

1. P. Bowcock, E. Corrigan and C. Zambon, *Classically integrable field theories with defects*, Proceedings of the 6th International Workshop on Conformal Field Theory and Integrable Models (Landau Institute, 2002), Int. J. Mod. Phys. A **19** (Supplement) (2004) 82–91, arXiv:hep-th/0305022.
2. P. Bowcock, E. Corrigan and C. Zambon, *Affine Toda field theories with defects*, JHEP **01** (2004) 056, arXiv:hep-th/0401020.
3. E. Corrigan and C. Zambon, *Jump-defects in the nonlinear Schrödinger model and other non-relativistic field theories*, Nonlinearity **19** (2006) 1447–1469, arXiv:nlin/0512038.
4. E. Corrigan and C. Zambon, *Comments on defects in the $a_r$ Toda field theories*, J. Phys. A **42** (2009) 304008, arXiv:0902.1307.
5. E. Corrigan and C. Zambon, *A new class of integrable defects*, J. Phys. A **42** (2009) 475203, arXiv:0908.3126.
6. E. Corrigan and C. Zambon, *Type II defects revisited*, JHEP **09** (2018) 019, arXiv:1807.05747.
7. E. Corrigan and C. Zambon, *Integrable defects at junctions within a network*, J. Phys. A **53** (2020) 484001, arXiv:2006.14447.
8. E. Corrigan and C. Zambon, *Adding integrable defects to the Boussinesq equation*, J. Phys. A **56** (2023) 345203, arXiv:2306.03772.
9. E. Corrigan and C. Zambon, *Integrable defects in affine Toda field theory and infinite dimensional representations of quantum groups*, Nucl. Phys. B (2011), doi:10.1016/j.nuclphysb.2011.03.007, arXiv:1012.4186.
10. R. Bristow and P. Bowcock, *Momentum conserving defects in affine Toda field theories*, JHEP **05** (2017) 153, arXiv:1612.03002.
11. C. Robertson, *Folding defect affine Toda field theories*, J. Phys. A **47** (2014) 185201, arXiv:1304.3129.
12. V. Caudrelier, *On a systematic approach to defects in classical integrable field theories*, Int. J. Geom. Meth. Mod. Phys. **5** (2008) 1085–1108, arXiv:0704.2326.
13. V. Caudrelier and A. Kundu, *A multisymplectic approach to defects in integrable classical field theory*, JHEP **02** (2015) 088, arXiv:1411.0418.
14. A. Doikou, *Classical integrable defects as quasi Bäcklund transformations*, Nucl. Phys. B **911** (2016) 212–230, arXiv:1603.04688.
15. J. Avan and A. Doikou, *Liouville integrable defects: the nonlinear Schrödinger paradigm*, JHEP **01** (2012) 040, arXiv:1110.4728.
16. P. J. Olver, *Applications of Lie Groups to Differential Equations*, 2nd ed., Graduate Texts in Mathematics 107, Springer, New York (1993).
17. H. D. Wahlquist and F. B. Estabrook, *Bäcklund transformations for solutions of the Korteweg–de Vries equation*, Phys. Rev. Lett. **31** (1973) 1386.
18. M. Wadati, *Bäcklund transformation for solutions of the modified Korteweg–de Vries equation*, J. Phys. Soc. Japan **36** (1974) 1498.
19. A. Weinstein, *Symplectic manifolds and their Lagrangian submanifolds*, Adv. Math. **6** (1971) 329–346.
20. G. L. Lamb, *Bäcklund transformation in nonlinear pulse propagation*, Phys. Lett. A **48** (1974) 73.
21. X.-C. Huang, *A two-parameter Bäcklund transformation for the Boussinesq equation*, J. Phys. A **15** (1982) 3367; Corrigendum J. Phys. A **16** (1983) 209.
22. A. G. Rasin and J. Schiff, *Bäcklund transformations for the Boussinesq equation and merging solitons*, J. Phys. A **50** (2017) 325202, arXiv:1701.00243.
23. *Momentum-Conserving Type-I Defects and Local Integrability near a Massive Vacuum*, companion manuscript, corrected version of 19 October 2026, in this repository as `defect-integrability/defect_integrability_paper.md`; not yet independently reviewed.
24. B. Xia and R. Zhou, *Time-dependent defects in integrable soliton equations*, Proc. R. Soc. A (2019), doi:10.1098/rspa.2019.0652, arXiv:1908.05578.
