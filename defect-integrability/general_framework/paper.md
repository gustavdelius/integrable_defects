# Momentum-Conserving Defects, Kinematic Symmetry and Integrability: a General Framework

*Rescued and restructured version of the pre-structural paper* ([history/defect_integrability_paper_pre_structural.md](../history/defect_integrability_paper_pre_structural.md)), 20 October 2026.

**Status.** Sections 2–7 give complete written proofs, in the formal variational calculus, of general statements about arbitrary finite-order Lagrangian field theories in $1+1$ dimensions. The main theorem (Theorem 8.1) deduces an infinite hierarchy of independent commuting local charges from momentum conservation at a defect **together with** three further hypotheses, each stated explicitly: a kinematic symmetry of the bulk, a regular transparent limit of the defect family, and nonresonance of the bulk dispersion relation. The unconditional Corrigan–Zambon conjecture is **not** proved; Section 10 says exactly which implication is missing. The written proofs await independent review. Machine checks cover the algebraic cores of the general lemmas and every observed case of [the conjecture report](conjecture_report.md), Section 1.2 (Appendix B); they do not replace the proofs. The literature has not been searched systematically for earlier versions of Theorems 3.3, 5.2 and 7.3, so no novelty is claimed for them.

## Abstract

A jump defect joins two $(1+1)$-dimensional local Lagrangian field theories at $x=0$. Corrigan and Zambon observed that conservation of momentum across such a defect makes the sewing conditions a Bäcklund transformation and appears to force integrability of the bulk. We prove the first half in general. For arbitrary finite-order bulk Lagrangians and arbitrary local defect functionals, including auxiliary defect fields and Lagrange multipliers, an off-shell momentum balance implies that the spatial Hamiltonian flows of the two bulk theories are tangent to the sewing correspondence. Consequently every solution of the sewing equations imposed at all $x$ solves both bulk equations. The proof applies the time-Euler operator to the spatial Hamilton–Jacobi form of the balance; it needs no Lagrangian, coisotropy or transversality hypothesis. For the second half we isolate a mechanism. A conservation law whose current is affine in $(x,t)$ — the Noether current of a Lorentz boost, a Galilean boost, a dilation or a time-linear field shift — turns the defect charges into a conserved generating density along the Bäcklund relation. A one-parameter family of momentum-conserving defects with a regular transparent limit then yields an infinite sequence of local conservation laws. In the observed cases this family is the orbit of the defect under a kinematic symmetry, or a modulus of the momentum constraint. Finally, for bulk theories with a constant Poisson operator and nonresonant dispersion, any such sequence is in involution, and distinct kinematic weights make it functionally independent. No Bianchi-permutability hypothesis is needed. All observed cases satisfy the hypotheses that apply to them; the massless theories fail nonresonance and are covered only by the Bäcklund theorem.

---

## 1. Introduction

### 1.1 The observation and what a general proof must supply

Let $\mathcal L_-([\phi])$ on $x<0$ and $\mathcal L_+([\psi])$ on $x>0$ be local Lagrangian densities, joined at $x=0$ by a defect action $S_d=\int dt\,\mathcal L_d$. Energy is conserved across any time-independent defect. Momentum is not, because the defect breaks spatial translations. Corrigan, Zambon and collaborators found, model by model, that a local defect contribution can restore momentum conservation only when the sewing conditions form a Bäcklund transformation and the bulk theories are integrable ([conjecture report](conjecture_report.md), Section 1).

A general theorem must supply four logically separate steps:

1. momentum conservation $\Rightarrow$ the sewing conditions, imposed at every $x$, form a Bäcklund relation;
2. a Bäcklund relation $\Rightarrow$ a conserved local *generating density* along it;
3. a one-parameter family of such relations with a regular transparent limit $\Rightarrow$ infinitely many local conservation laws;
4. these conservation laws $\Rightarrow$ independent charges in involution.

The pre-structural paper asserted all four in general. Its referee reports ([first](../referee_report_theorem_D.md), [Lean](../lean_referee/report.md), [second Lean](../lean_referee/report2.md)) showed that step 1 rested on unproved geometric hypotheses, that step 2 was missing outside Lorentz-invariant theories (the proposed KdV route gave only trivial charges), that step 3's family was assumed, and that step 4 assumed Bianchi permutability. This version keeps the original architecture and repairs each step.

### 1.2 Results

* **Theorem 3.3 (Bäcklund theorem).** Step 1 holds for arbitrary finite-order bulk Lagrangians without mixed top derivatives and arbitrary local defect functionals, including auxiliary fields and multipliers, under a checkable injectivity condition (I). Condition (I) is vacuous without auxiliary fields.
* **Lemma 4.1, Propositions 4.2–4.3, Lemma 5.2 (closure).** Step 2 holds whenever the bulk has a conservation law with current affine in $(x,t)$ whose two constituent conservation laws have defect charges. Such laws come from boosts, Galilean boosts, dilations and time-linear shifts. Every observed case has one.
* **Lemmas 5.4–5.5, 6.2, Theorem 6.4.** Step 3 holds for any family with a regular transparent limit. Dilations of the bulk carry a momentum-conserving defect to a family of momentum-conserving defects; Lorentz boosts carry its Bäcklund relation to a family of momentum-conserving relations.
* **Theorems 7.3–7.4.** Step 4 holds for bulk theories with a constant Poisson operator and nonresonant dispersion. Involution follows from a rigidity lemma that generalises the massive-vacuum lemma of the [structural paper](../defect_integrability_paper.md); independence follows from distinct kinematic weights.
* **Theorem 8.1** assembles these steps. **Section 9** checks its hypotheses in each observed case.

### 1.3 Relation to the structural paper

The [structural paper](../defect_integrability_paper.md) proves a complete theorem for normalised constant Type-I defects of multicomponent relativistic scalars near a massive analytic vacuum. There the parameter family and the transparent limit are *derived* from the momentum constraint. That theorem is the relativistic Type-I instance of Theorem 8.1 with hypothesis (C) proved rather than assumed. The present paper trades that depth for breadth: its general statements cover every class of observed defects, at the price of hypothesis (C) in general.

---

## 2. The Ostrogradsky spatial phase space

### 2.1 Bulk Lagrangians and canonical currents

Let $\phi(x,t)\in\mathbb R^r$ (complex fields are treated as pairs $u,\bar u$ of independent components). Write $D_t,D_x$ for total derivatives. A **bulk Lagrangian** is a local density $\mathcal L(\phi_{a,k})$, $\phi_{a,k}=D_t^aD_x^k\phi$, with no explicit $(x,t)$, of spatial order $K\ge1$ and temporal order $A$. We call it **admissible** if $\partial_x^K\phi$ enters only through $\phi_{0,K}$ (no mixed top derivatives) and $\det\partial^2\mathcal L/\partial\phi_{0,K}^2\ne0$.

Integrating by parts first in $t$ and then in $x$ gives, for every variation $\eta$,

$$\operatorname{pr}v_\eta\mathcal L=E(\mathcal L)\cdot\eta+D_x\Big(\sum_{m=0}^{K-1}\pi_m\cdot D_x^m\eta\Big)+D_t\,\Xi(\eta), \tag{2.1}$$

with

$$F_k=\sum_{a}(-D_t)^a\frac{\partial\mathcal L}{\partial\phi_{a,k}},\qquad \pi_m=\sum_{j=0}^{K-1-m}(-D_x)^jF_{m+j+1},\qquad E(\mathcal L)=\sum_{k}(-D_x)^kF_k, \tag{2.2}$$

and the explicit temporal boundary term

$$\Xi(\eta)=\sum_{k}\sum_{a\ge1}\sum_{b=0}^{a-1}(-D_t)^b\frac{\partial\mathcal L}{\partial\phi_{a,k}}\cdot D_t^{a-1-b}D_x^k\eta. \tag{2.3}$$

Formula (2.3) is the telescoping identity $P\,D_t^a\zeta=(-D_t)^aP\,\zeta+D_t\sum_{b<a}(-D_t)^bP\,D_t^{a-1-b}\zeta$, applied to $P=\partial\mathcal L/\partial\phi_{a,k}$, $\zeta=D_x^k\eta$. The $x$-integration is the same identity in $x$ applied to $F_kD_x^k\eta$; collecting the coefficient of $D_x^m\eta$ gives $\pi_m$.

**Definition 2.1 (canonical currents).** Put $\Phi_m=D_x^m\phi$ and

$$\mathcal T^0{}_0=\Xi(D_t\phi)-\mathcal L,\quad \mathcal T^1{}_0=\sum_m\pi_m\cdot D_t\Phi_m,\quad \mathcal T^0{}_1=\Xi(D_x\phi),\quad \mathcal T^1{}_1=\mathcal H^{(x)}:=\sum_m\pi_m\cdot D_x\Phi_m-\mathcal L. \tag{2.4}$$

With $\eta_{\mu\nu}=\mathrm{diag}(1,-1)$ write $T^{00}=\mathcal T^0{}_0$, $T^{01}=-\mathcal T^0{}_1$, $T^{10}=\mathcal T^1{}_0$, $T^{11}=-\mathcal T^1{}_1$.

**Lemma 2.1 (Legendre–Noether identity).** *For every admissible $\mathcal L$, off shell,*

$$D_t\mathcal T^0{}_\nu+D_x\mathcal T^1{}_\nu=-E(\mathcal L)\cdot D_\nu\phi\qquad(\nu=0,1). \tag{2.5}$$

*Thus $(\mathcal T^0{}_\nu,\mathcal T^1{}_\nu)$ are Noether currents of the translations, and the spatial momentum flux is $T^{11}=-\mathcal H^{(x)}$ exactly. Any other current with the same characteristic differs from these by a trivial current $(D_xC,-D_tC)$ plus a constant. For $K=A=1$ they are the textbook canonical currents.*

*Proof.* Put $\eta=D_\nu\phi$ in (2.1); then $\operatorname{pr}v_\eta\mathcal L=D_\nu\mathcal L$, and rearranging gives (2.5). Two currents with the same characteristic differ by a current that is conserved off shell; by exactness of the horizontal variational complex on the jet space of $\mathbb R^2$ (Olver, *Applications of Lie Groups to Differential Equations*, Thm 4.24) such a current is $(D_xC,-D_tC)$ plus a constant. For $K=A=1$, $\Xi(\eta)=\partial\mathcal L/\partial\phi_t\cdot\eta$ and $\pi_0=\partial\mathcal L/\partial\phi_x$. $\square$

This replaces the earlier Lemma 2.1, whose identification "$T^{11}=-\mathcal H^{(x)}-\partial_t\Upsilon_1$" was assumed in its Lean version (report 2, item C1). Here the canonical currents are *defined* by the specified integrations by parts, and the identification is a consequence. The Lean theorems `noether_first_order` and `legendre_noether_K2` check the algebra for $K=1$ and $K=2$.

### 2.2 Spatial Hamilton equations

The **spatial phase space** at fixed $x$ consists of $t$-histories $z=(\Phi_0,\dots,\Phi_{K-1};\pi_0,\dots,\pi_{K-1})$. Admissibility lets us solve $\pi_{K-1}=\partial\mathcal L/\partial\phi_{0,K}$ for $\phi_{0,K}=Z(\Phi,\pi_{K-1})$, a local function of the $t$-jets of $\Phi$ and of $\pi_{K-1}$ itself. The spatial Hamiltonian density is

$$\mathcal H(\Phi,\pi)=\sum_{m<K-1}\pi_m\cdot\Phi_{m+1}+\pi_{K-1}\cdot Z-\mathcal L\big|_{\phi_{0,K}=Z}. \tag{2.6}$$

Write $a_m=\partial\mathcal H/\partial\pi_m$ and $b_m=E^{(t)}_{\Phi_m}(\mathcal H)$ (time-Euler derivative). The spatial Hamiltonian vector field is $X=(a,-b)$.

**Lemma 2.2 (Hamilton–Euler–Lagrange identities).** *Let $\phi$ be any field, on or off shell, and let $z=(\Phi_m=D_x^m\phi,\ \pi_m=\pi_m[\phi])$ be its Ostrogradsky lift. Then*

$$D_x\Phi_m=a_m(z)\ \ (\text{all }m),\qquad D_x\pi_m+b_m(z)=0\ \ (m\ge1),\qquad D_x\pi_0+b_0(z)=-E(\mathcal L)[\phi]. \tag{2.7}$$

*In particular $D_xz=X(z)$ if and only if $E(\mathcal L)[\phi]=0$.*

*Proof.* $a_m=\Phi_{m+1}$ for $m<K-1$, and $a_{K-1}=Z+(\pi_{K-1}-\partial\mathcal L/\partial\phi_{0,K})\partial Z/\partial\pi_{K-1}=Z=D_x^K\phi$. In $b_m$ the terms through $Z$ cancel for the same reason; since $Z$ is algebraic in $\pi_{K-1}$ and has no $t$-derivatives of top order, no derivative of $Z$ survives. Hence $b_m=\pi_{m-1}-F_m$ for $m\ge1$ and $b_0=-F_0$. The recursion $\pi_{m-1}=F_m-D_x\pi_m$, which is (2.2), gives the second identity; $E=F_0-D_x\pi_0$ gives the third. $\square$

Lemma 2.2 is checked for $K=2$ by `hamilton_slots_K2`.

---

## 3. Momentum balance and the Bäcklund theorem

### 3.1 Defects

Let $\mathcal L_\pm$ be admissible, of spatial orders $K_\pm$. A **defect functional** is $S_d=\int dt\,\mathcal L_d$, where $\mathcal L_d$ is a local function of the $t$-jets of

$$Y=(\Phi,\Psi,\lambda),\qquad \Phi=(\Phi_m)_{m<K_-}\big|_{x=0^-},\quad \Psi=(\Psi_m)_{m<K_+}\big|_{x=0^+},\quad \lambda\in\mathbb R^p .$$

The auxiliary variables $\lambda$ include dynamical defect fields (Type II) and Lagrange multipliers (constrained defects such as those of KdV and mKdV, Section 9). Varying $S=\int_{x<0}\mathcal L_-+\int_{x>0}\mathcal L_++S_d$ and using (2.1) on each half-line gives the **sewing equations**

$$\pi_{-,m}=\Pi^-_m(Y):=-E^{(t)}_{\Phi_m}\mathcal L_d,\qquad \pi_{+,m}=\Pi^+_m(Y):=E^{(t)}_{\Psi_m}\mathcal L_d,\qquad 0=C(Y):=E^{(t)}_\lambda\mathcal L_d. \tag{3.1}$$

The **sewing correspondence** is $\Gamma_d=\{(\Phi,\Pi^-(Y);\Psi,\Pi^+(Y)):C(Y)=0\}$. A triple of fields $(\phi,\psi,\lambda)$ on a region of $\mathbb R^2$ is a **promoted solution** if (3.1) holds at every $x$, with $\pi_\mp$ the actual Ostrogradsky momenta of $\phi,\psi$.

Let $\mathcal S$ be the Fréchet derivative of the defect Euler–Lagrange expression $E_Y(\mathcal L_d)$, with blocks $S_{AB}$, $A,B\in\{\Phi,\Psi,\lambda\}$. By the Helmholtz conditions (Olver, Thm 5.92) $\mathcal S$ is formally self-adjoint: $S_{AB}^*=S_{BA}$. The linearisation of (3.1) is

$$\delta\pi_-=-(S_{\Phi\Phi}\delta\Phi+S_{\Phi\Psi}\delta\Psi+S_{\Phi\lambda}\delta\lambda),\quad \delta\pi_+=S_{\Psi\Phi}\delta\Phi+S_{\Psi\Psi}\delta\Psi+S_{\Psi\lambda}\delta\lambda,\quad 0=S_{\lambda\Phi}\delta\Phi+S_{\lambda\Psi}\delta\Psi+S_{\lambda\lambda}\delta\lambda. \tag{3.2}$$

A vector $(\delta z_-,\delta z_+)$ is **tangent** to $\Gamma_d$ if it arises from some $\delta Y$ in this way.

### 3.2 Momentum balance

**Definition 3.1 (momentum balance).** $S_d$ is *momentum-conserving* if

$$\mathcal H_-\big(\Phi,\Pi^-(Y)\big)-\mathcal H_+\big(\Psi,\Pi^+(Y)\big)\ \in\ \operatorname{Im}D_t+\langle C\rangle, \tag{3.3}$$

where $\langle C\rangle$ is the differential ideal generated by the components of $C$. Equivalently there is a local $\widetilde P(Y)$ with $\mathcal H_--\mathcal H_++D_t\widetilde P\in\langle C\rangle$.

**Lemma 3.2.** *Condition (3.3) is the precise form of conservation of $P_-+P_++P_d$, with $P_\pm=\int T^{01}_\pm\,dx$ and $P_d=\widetilde P$, on all solutions of the bulk and sewing equations whose boundary jets at $x=0$ are otherwise unconstrained.*

*Proof.* By (2.5), $D_tT^{01}+D_xT^{11}=0$ on shell, so $\frac{d}{dt}(P_-+P_+)=(-T^{11}_-+T^{11}_+)|_{x=0}=(\mathcal H_--\mathcal H_+)|_{x=0}$ by Lemma 2.1. On solutions of (3.1) the momenta in $\mathcal H_\pm$ are $\Pi^\pm(Y)$. Conservation for all admissible boundary jets is (3.3). $\square$

This is how Corrigan and Zambon impose momentum conservation in each computation: the boundary $t$-jets are treated as independent after the sewing equations are used. Section 9 verifies (3.3) symbolically for every observed case.

### 3.3 The Bäcklund theorem

**Theorem 3.3 (momentum conservation gives a Bäcklund relation).** *Let $S_d$ satisfy Definition 3.1, with $\mathcal H_--\mathcal H_++D_t\widetilde P\equiv\rho\cdot C$ modulo $\operatorname{Im}D_t$ and $C$-derivatives.*

*(a) (Tangency.) At every point of $\Gamma_d$ the pair of spatial Hamiltonian vector fields $(X_-,X_+)$ is tangent to $\Gamma_d$. It is the image of $\delta Y=(a_-,a_+,\rho)$ under (3.2).*

*(b) (Promoted solutions are bulk solutions.) Let $(\phi,\psi,\lambda)$ be a promoted solution and put $\kappa=D_x\lambda-\rho$. Then*

$$S_{\Phi_m\lambda}\kappa=E_-[\phi]\,\delta_{m0},\qquad S_{\Psi_m\lambda}\kappa=-E_+[\psi]\,\delta_{m0},\qquad S_{\lambda\lambda}\kappa=0. \tag{3.4}$$

*If the operator*

$$\text{(I)}\qquad \kappa\longmapsto\big((S_{\Phi_m\lambda}\kappa)_{m\ge1},\ (S_{\Psi_m\lambda}\kappa)_{m\ge1},\ S_{\lambda\lambda}\kappa\big)$$

*is injective, then $E_-[\phi]=0$ and $E_+[\psi]=0$. Without auxiliary variables (Type I, any $K_\pm$) both bulk equations hold with no further condition.*

*Proof.* (a) Apply the $t$-Euler operator $E_Y$ to the balance. It annihilates $\operatorname{Im}D_t$, and on $\{C=0\}$ it sends $\rho\cdot C$ to $D_C^*\rho$. For the left side use the chain rule for Euler operators: if $F$ is local in $z$ and $z=Z[Y]$ is a local map, then $E_Y(F\circ Z)=D_Z^*\,(E_zF\circ Z)$. (Proof: $\delta\!\int F(Z)=\int E_zF\cdot D_Z\delta Y=\int D_Z^*E_zF\cdot\delta Y$ modulo total derivatives.) Here $E_z\mathcal H_\mp=(b_\mp,a_\mp)$, and $D_{\Pi^-}=-(S_{\Phi\Phi},S_{\Phi\Psi},S_{\Phi\lambda})$, $D_{\Pi^+}=(S_{\Psi\Phi},S_{\Psi\Psi},S_{\Psi\lambda})$, $D_C=(S_{\lambda\Phi},S_{\lambda\Psi},S_{\lambda\lambda})$. Self-adjointness gives, on $C=0$,

$$\begin{aligned}
b_--S_{\Phi\Phi}a_--S_{\Phi\Psi}a_+&=S_{\Phi\lambda}\rho,\\
-S_{\Psi\Phi}a_--b_+-S_{\Psi\Psi}a_+&=S_{\Psi\lambda}\rho,\\
-S_{\lambda\Phi}a_--S_{\lambda\Psi}a_+&=S_{\lambda\lambda}\rho .
\end{aligned}\tag{3.5}$$

Insert $\delta Y=(a_-,a_+,\rho)$ into (3.2). The third line of (3.5) is the linearised constraint. The first two give $\delta\pi_-=-b_-$ and $\delta\pi_+=-b_+$, the momentum components of $X_\mp$. The configuration components are $\delta\Phi=a_-$, $\delta\Psi=a_+$.

(b) Differentiating (3.1) in $x$ shows that $D_xz$ is tangent, with $\delta Y=D_xY$. By (a), $X$ is tangent with $\delta Y=(a_-,a_+,\rho)$. By Lemma 2.2, $D_x\Phi=a_-$ and $D_x\Psi=a_+$, because the momenta are the actual ones. The difference of the two tangent vectors therefore has $\delta Y=(0,0,\kappa)$, and (3.2) gives $D_x\pi_-+b_-=-S_{\Phi\lambda}\kappa$, $D_x\pi_++b_+=S_{\Psi\lambda}\kappa$ and $S_{\lambda\lambda}\kappa=0$. By Lemma 2.2 the left sides vanish for $m\ge1$ and equal $-E_-$, respectively $-E_+$, for $m=0$. This is (3.4). Under (I), $\kappa=0$, and (3.4) gives $E_\mp=0$. $\square$

The Lean theorems `tangency_from_euler`, `promoted_implies_bulk` and `promoted_implies_bulk_typeI` check the linear algebra of (a) and (b), with (3.5) and Lemma 2.2 as hypotheses. Independently, `checks/check_tangency.py` computes $\rho$, the vector fields and the Fréchet derivatives for three published defects and confirms the conclusion of (a) exactly: the sine-Gordon Type-I defect ($\rho=0$), the Tzitzéica Type-II defect, and the KdV defect (spatial order 2, Lagrange multiplier).

**Remarks 3.4.**
1. *What is no longer assumed.* The pre-structural Theorem 1 needed $\Gamma_d$ to be a strong Lagrangian submanifold, transverse to the vertical fibres, connected and containing the vacuum. None of these enters Theorem 3.3. The Lagrangian geometry survives as an interpretation (Appendix A).
2. *Constrained defects are allowed.* The referee's counterexample $S_d=\int\lambda(\psi+\phi)\,dt$ conserves momentum for any even potential. Theorem 3.3 is consistent with it: the relation $\psi=-\phi$ is a Bäcklund relation in the trivial sense. Theorem 3.3 is the Bäcklund half of the conjecture only. Integrability needs the nondegenerate family of Section 6, which this defect does not have.
3. *Condition (I) in practice.* It is vacuous for Type I. For the KdV and mKdV multiplier defects $S_{\Phi_1\mu}=\partial C/\partial\Phi_1=1$, so (I) holds. For relativistic Type-II defects it reduces to injectivity of $S_{\lambda\lambda}=-\partial^2\mathcal B/\partial\lambda^2$, a multiplication operator, nonzero for the Tzitzéica defect of Section 9.
4. *Heterogeneous defects.* Theorem 3.3 does not need $\mathcal L_-=\mathcal L_+$. A momentum-conserving defect between Liouville and a free massless field is a Bäcklund relation linearising Liouville (Section 9).

### 3.4 One-sided construction

**Lemma 3.5 (the second sewing equation follows).** *Let $S_d$ be momentum-conserving and let $\phi$ solve $E_-[\phi]=0$. Suppose $(\Psi,\lambda)$ solve the left sewing equations $\pi_-[\phi]=\Pi^-(Y)$ and $C(Y)=0$ at every $x$. If*

$$\text{(T)}\qquad (\eta,\kappa)\longmapsto\big(S_{\Phi\Psi}\eta+S_{\Phi\lambda}\kappa,\ S_{\lambda\Psi}\eta+S_{\lambda\lambda}\kappa\big)$$

*is injective, then $\Pi^+(Y)$ is the Ostrogradsky momentum of the field $\psi:=\Psi_0$, so the right sewing equations hold, and $E_+[\psi]=0$.*

*Proof.* Put $z_+=(\Psi,\Pi^+(Y))$. As in Theorem 3.3(b), $D_xz$ and $X$ are tangent, and $D_xz_-=X_-$ since $\phi$ is on shell. Their difference has $\delta Y=(0,\eta,\kappa)$ with $\eta=D_x\Psi-a_+(z_+)$, and its $\delta\pi_-$ and constraint components vanish. By (T), $\eta=0$ and $\kappa=0$, so $D_x\Psi=a_+(z_+)$ and $D_x\Pi^++b_+(z_+)=0$. The configuration equations identify $\Psi_m=D_x^m\psi$ and $\Pi^+_{K-1}=\partial\mathcal L_+/\partial\psi_{0,K}$. The momentum equations for $m\ge1$, read downward from $m=K-1$, identify every $\Pi^+_m$ with $\pi_m[\psi]$; the equation for $m=0$ is $E_+[\psi]=0$. $\square$

In the formal setting of Section 6, (T) holds when its leading coefficient in the spectral parameter is an invertible matrix. For gyroscopic Type-I defects with a transparent critical manifold that coefficient is $\epsilon^{-1}\mathsf H$ with $\det\mathsf H\ne0$. This is Definition 4.1 of the pre-structural paper.

---

## 4. Defect charges, potentials and closure

### 4.1 Defect charges

Let $(N,J)$ be a conservation law of each bulk theory: $D_tN_\pm+D_xJ_\pm=0$ on shell. A **defect charge** for it is a local $Q_d(Y)$ with

$$D_tQ_d\equiv J_-\big|_{x=0}-J_+\big|_{x=0}\pmod{\langle C\rangle}\quad\text{on }\Gamma_d. \tag{4.1}$$

Then $\int_{x<0}N_-+\int_{x>0}N_++Q_d$ is conserved.

**Lemma 4.1 (Noether charges at a defect).** *Let $v_Q$ be an evolutionary symmetry of both bulk Lagrangians whose characteristic $Q$ may depend on $t$ but not on $x$. Suppose (i) $\operatorname{pr}v_Q\mathcal L_\pm=D_tA_\pm$ with no $x$-flux, (ii) $D_x^mQ|_{x=0}$ is a local function $Q_{\Phi_m}$ of the boundary data, and likewise on the right, and (iii) for a prescribed action $Q_\lambda$ on $\lambda$, $\operatorname{pr}v_Q\mathcal L_d=D_tA_d$. Then the Noether law $N=A-\Xi(Q)$, $J=-\sum_m\pi_m\cdot D_x^mQ$ has the defect charge $Q_d=A_d-\Xi_d(Q)$, where $\Xi_d$ is the temporal boundary term (2.3) of $\mathcal L_d$. Moreover, every law with density $N=D_x\nu$ for a local $\nu$ has the defect charge $\nu_+-\nu_-$ ("topological" charges).*

*Proof.* (2.1) with $\eta=Q$ gives the current. At $x=0$ the sewing equations give

$$J_--J_+=\sum_m E_{\Phi_m}\mathcal L_d\cdot Q_{\Phi_m}+\sum_m E_{\Psi_m}\mathcal L_d\cdot Q_{\Psi_m},$$

which equals $\operatorname{pr}v_Q\mathcal L_d-E_\lambda\mathcal L_d\cdot Q_\lambda-D_t\Xi_d(Q)$ by the defect analogue of (2.1). On $C=0$ this is $D_t(A_d-\Xi_d(Q))$. For a topological law, $\int_{x<0}D_x\nu_-+\int_{x>0}D_x\nu_+=\nu_-(0)-\nu_+(0)$ plus constants at infinity. $\square$

**Examples.** Time translation ($Q=-D_t\phi$, $A=-\mathcal L$) gives the defect energy $\mathcal E_d$ of every autonomous defect; this is Remark 3.1 of the pre-structural paper. A $U(1)$ phase gives the NLS number defect charge. A constant field shift, or a time-linear shift $\phi\mapsto\phi+\epsilon t$ when $\operatorname{pr}v\mathcal L\in\operatorname{Im}D_t$, gives a charge whenever the defect depends on $\phi,\psi$ only through differences. Spatial translations violate (i), and their defect charge is exactly the hypothesis of Definition 3.1. For momentum, $Q_d=\widetilde P$.

### 4.2 Stress potentials along promoted solutions

**Proposition 4.2 (defect charges are spatial potentials).** *Let $(\phi,\psi,\lambda)$ be a promoted solution satisfying (I), so both bulk equations hold, and let $Q_d$ be a defect charge for $(N,J)$. Put $R:=D_xQ_d+(N_--N_+)$, evaluated along the solution. Then $D_tR=0$. Moreover $R\equiv0$ in either of the following settings:*

*(A) (formal branch) the solution is a formal branch (Definition 6.1), so $R$ is a differential function of $\phi$ alone, and $R$ vanishes at the vacuum;*

*(B) (actual solutions) for each $x$ the solution tends, as $t\to-\infty$, to a constant pair at which $R=0$.*

*Hence $D_tQ_d=J_--J_+$ and $D_xQ_d=-(N_--N_+)$ at every point.*

*Proof.* $D_tR=D_xD_tQ_d+D_t(N_--N_+)=D_x(J_--J_+)+D_t(N_--N_+)=0$, using both bulk laws. In setting (A), $R$ is a differential function of $\phi$ with $D_tR=0$ on solutions of $E_-[\phi]=0$; by Lemma 6.3 it is constant, and the constant is its vacuum value. In setting (B), $R(x,\cdot)$ is constant in $t$ and equals its limit. $\square$

Proposition 4.2 replaces the pre-structural Proposition 4.1. Normalisation is now a property of the single residual $R$, never global injectivity of $D_t$; on any nonzero ring a derivation kills $1$ (`Deriv.not_injective_of_nontrivial`). The closedness step is `potential_residual_closed`; the normalisation step is `potential_from_normalised_residual`, and the nonzero model `Tri` shows its hypothesis is satisfiable. For energy and momentum, Proposition 4.2 gives the four identities (4.1) of the pre-structural paper.

### 4.3 Closure

**Proposition 4.3 (a conserved generating density).** *Let laws 1 and 2 have defect charges $Q^1,Q^2$, and suppose that on each side*

$$N_2+J_1+D_ta_0+D_xb_0=0\quad\text{on shell} \tag{4.2}$$

*for local $a_0,b_0$. Then along every promoted solution in setting (A) or (B)*

$$D_t\big(Q^1+a_{0,-}-a_{0,+}\big)+D_x\big(b_{0,-}-b_{0,+}-Q^2\big)=0. \tag{4.3}$$

*Proof.* $D_tQ^1=J_{1,-}-J_{1,+}=-(N_{2,-}-N_{2,+})-D_t\Delta a_0-D_x\Delta b_0$ by (4.2), and $-(N_{2,-}-N_{2,+})=D_xQ^2$ by Proposition 4.2. $\square$

We call $\mathcal G=Q^1+\Delta a_0$ the **generating density**. This is the step that the pre-structural paper lacked outside Lorentz-invariant theories. Its replacement route for KdV used $T^{01}_--T^{01}_+=-D_xP_d$, an exact derivative, and so gave only trivial charges (report 2, Section 2). Checked by `closure_conserved_density`.

---

## 5. Kinematic symmetry

### 5.1 Affine conservation laws give closure

**Definition 5.1.** An **affine conservation law** is a current $(x a_1+t a_2+a_0,\ x b_1+t b_2+b_0)$, with $a_i,b_i$ local and free of explicit $(x,t)$, that is conserved on shell.

**Lemma 5.2 (closure from kinematic symmetry).** *For an affine conservation law, $(a_1,b_1)$ is a conservation law, $a_2$ is a conserved density, and (4.2) holds with $N_2=a_2$, $J_1=b_1$. The Noether currents of the following symmetries are affine:*

| bulk | symmetry | law 1 | law 2 | $a_0$, $b_0$ | generating density $\mathcal G$ |
|---|---|---|---|---|---|
| relativistic scalars (any potential) | Lorentz boost | energy | $-$momentum | $0,0$ | $\mathcal E_d$ |
| NLS | Galilean boost | number | $-2\,$momentum | $0,0$ | $N_d$ |
| KdV $u_t=6uu_x-u_{xxx}$ | Galilean symmetry | mass | $3u^2$ ($\propto$ momentum) | $0,\ -u_x$ | $q-p$ |
| mKdV $v_t=6v^2v_x+v_{xxx}$ | dilation | $\tfrac12v^2$ (momentum) | $3\times$energy | $0,\ v v_x$ | $P_d$ |
| Boussinesq | $u\mapsto u+\epsilon t$ | trivial | shift law | $u/c^2,\ 0$ | $u-v$ |

*Proof.* In the jet space of the equation, $x$ and $t$ are coordinates independent of the fibre coordinates, and $D_tx=D_xt=0$, $D_xx=D_tt=1$. Expanding the conservation law gives $x(D_ta_1+D_xb_1)+t(D_ta_2+D_xb_2)+(a_2+b_1+D_ta_0+D_xb_0)=0$, and each coefficient vanishes. Each row of the table is checked in `check_kinematics.py`, part A. $\square$

The algebraic expansion is `affine_law_expansion`.

**Corollary 5.3.** *In every row, both constituent laws have defect charges. Energy has one for every autonomous defect (Lemma 4.1). Momentum has one by Definition 3.1. The number has one for $U(1)$-invariant defects. Mass is topological in the potential variable. The Boussinesq shift law has one because the defect depends on $u,v$ through $u-v$, $u_x$, $v_x$, $u_t$, $v_t$. Hence each observed defect has a conserved generating density along its Bäcklund relation.*

The closure relation is a property of the bulk alone. It reflects a kinematic symmetry, not integrability. A non-integrable relativistic theory has the same Lorentz closure. Integrability enters only through the family of Section 6.

### 5.2 Families from kinematic symmetries

**Lemma 5.4 (dilation families).** *Let $\delta_s:(x,t,\phi)\mapsto(sx,s^{\alpha}t,s^{\beta}\phi)$, $\beta$ a vector of weights, satisfy $\mathcal L_\pm\circ\delta_s=s^{w}\mathcal L_\pm$ up to total derivatives. If $S_d$ is momentum-conserving, then so is the pulled-back defect $S_d^{(s)}[Y]:=c(s)\,S_d[\delta_sY]$, for every $s>0$, where $c(s)>0$ is the factor that makes the total action $\int_{x<0}\mathcal L+\int_{x>0}\mathcal L+S_d$ scale homogeneously.*

*Proof.* $\delta_s$ fixes the line $x=0$ and each half-line. It maps the Ostrogradsky data, the momenta and $\mathcal H_\pm$ homogeneously, and maps the sewing equations of $S_d^{(s)}$ to those of $S_d$. Hence it maps identity (3.3) for $S_d$ to a nonzero multiple of identity (3.3) for $S_d^{(s)}$. $\square$

For KdV, mKdV and NLS the published defect functionals are homogeneous under the bulk dilations, with the defect parameter of weight $2$, $1$ and $1$ respectively (`check_kinematics.py`, part B). Their one-parameter families are therefore dilation orbits.

**Lemma 5.5 (Lorentz families).** *Let $\mathcal L_\pm$ be Lorentz-invariant scalar theories, so that $T^{\mu\nu}$ is a symmetric tensor, and let $(\phi,\psi,\lambda)$ range over the promoted solutions of a momentum-conserving defect satisfying (I), with stress potentials $\mathrm{Pot}^0=\mathcal E_d$ and $\mathrm{Pot}^1=P_d$ (Proposition 4.2): $\Delta T^{\mu\nu}=\varepsilon^{\mu\rho}D_\rho\mathrm{Pot}^\nu$. For a boost $\Lambda$, the boosted pairs $(\phi\circ\Lambda^{-1},\psi\circ\Lambda^{-1},\dots)$ again solve both bulk equations, with stress potentials $\Lambda^\nu{}_\beta\,\mathrm{Pot}^\beta\circ\Lambda^{-1}$. In particular momentum is conserved across the line $x=0$ for the boosted relation. When that relation is in sewing form at $x=0$, it is a momentum-conserving defect.*

*Proof.* $T'^{\mu\nu}(x)=\Lambda^\mu{}_\alpha\Lambda^\nu{}_\beta T^{\alpha\beta}(\Lambda^{-1}x)$, and derivatives transform by $\partial'=\Lambda^{-T}\partial$. Since $\det\Lambda=1$, $\Lambda\varepsilon\Lambda^T=\varepsilon$, i.e. $\Lambda\varepsilon=\varepsilon\Lambda^{-T}$, and therefore $\Delta T'^{\mu\nu}=\varepsilon^{\mu\rho}\partial'_\rho(\Lambda^\nu{}_\beta\mathrm{Pot}^\beta\circ\Lambda^{-1})$. $\square$

The two-dimensional identity is `lorentz_curl`. For the Bowcock–Corrigan–Zambon sine-Gordon defect the boosted relation is again in sewing form, with $\sigma\mapsto\sigma e^{\pm\theta}$ (`check_kinematics.py`, part B). This reproduces the spectral parameter of Theorem A of the conjecture report.

---

## 6. The hierarchy from a transparent family

**Definition 6.1 (regular transparent family, formal branch).** Let $\mathcal L_-=\mathcal L_+=\mathcal L$. A family $S_d^{(\epsilon)}$, $\epsilon\in(0,\epsilon_0)$, of momentum-conserving defects (or of promoted relations, Lemma 5.5) has a **formal branch** if there are a local invertible map $g$ that is a symmetry of $\mathcal L$ (the identity, a constant shift, or $\phi\mapsto-\phi$) and formal series

$$\psi=g(\phi)+\sum_{n\ge1}\epsilon^n\Psi_n[\phi],\qquad \lambda=\sum_{n\ge n_0}\epsilon^n\Lambda_n[\phi], \tag{6.1}$$

with local coefficients, such that for every solution of $E[\phi]=0$ every promoted sewing equation holds as a formal series in $\epsilon$. Constant offsets of order $\epsilon^{-1}$ in $\psi-g(\phi)$ are allowed when they solve the vacuum sewing equations; KdV needs one.

**Lemma 6.2 (formal implicit function).** *Let $G(\phi,\Delta;\epsilon)=0$ be a system of local equations for $\Delta=\psi-g(\phi)$ (and $\lambda$), formal in $\epsilon$, with $G=M\Delta+O(\epsilon)$ for an invertible constant (or pointwise invertible algebraic) matrix $M$. Suppose that derivatives of $\Delta$ enter only at positive order in $\epsilon$. Then $G=0$ has a unique formal solution $\Delta=\sum_{n\ge1}\epsilon^n\Delta_n$ with local coefficients.*

*Proof.* The coefficient of $\epsilon^n$ in $G$ is $M\Delta_n$ plus a local expression in $\Delta_1,\dots,\Delta_{n-1}$ and their derivatives. Induct on $n$. $\square$

In practice one equation of the sewing system, or the multiplier constraint, has the form of Lemma 6.2. The remaining equations then hold on shell either by Lemma 3.5 or by direct verification. Lemma 6.2 is the triangular recursion (4.10) of the pre-structural paper, now stated for any system with an invertible leading coefficient.

**Lemma 6.3 (top-order lemma).** *Let $v_t=F[v]$ be an evolution system of order $\ge1$ in $x$ whose highest-order symbol is invertible (this includes second-order-in-time wave equations written for $(\phi,\phi_t)$). A differential function $R[v]$ with $D_tR=0$ on shell is constant.*

*Proof.* If $R$ depends on $v_k$ with $k$ maximal, $D_tR$ contains $\partial R/\partial v_k\cdot\partial F/\partial v_m\cdot v_{k+m}$, linear in a jet variable of order $k+m$. No other term contains it. Hence $\partial R/\partial v_k=0$, and induction leaves a constant. $\square$

**Theorem 6.4 (hierarchy).** *Let a family have a formal branch, and let $\mathcal G$ be a generating density (Proposition 4.3), normalised to vanish at the vacuum, with flux $\mathcal F$. Expand*

$$\mathcal G\big(\phi,\psi(\epsilon),\lambda(\epsilon);\epsilon\big)=\sum_{n\ge n_1}\epsilon^nQ_n[\phi],\qquad \mathcal F=\sum_n\epsilon^n\mathcal J_n[\phi].$$

*Then $D_tQ_n+D_x\mathcal J_n=0$ on shell for every $n$, with $Q_n,\mathcal J_n$ local.*

*Proof.* The branch is a promoted solution in setting (A), with residuals that are differential functions of $\phi$. Lemma 6.3 makes them constant, and the vacuum value makes them zero, so Proposition 4.2 applies. Proposition 4.3 gives (4.3) as an identity of formal series; take coefficients. $\square$

**Lemma 6.5 (kinematic weights).** *Suppose a one-parameter group $g_\theta$ of point symmetries of $\mathcal L$ fixes the vacuum, maps the family to itself with $\epsilon\mapsto e^{w\theta}\epsilon$, and transforms $\mathcal G$ with weight $w_0$. Then $g_\theta^*Q_n=e^{(w_0+nw)\theta}Q_n$ modulo trivial densities. If $g_\theta$ acts on the Fourier variable of the linearised theory by $k\mapsto k_\theta$, the quadratic symbol $m_n(k)$ of $Q_n$ satisfies $m_n(k_\theta)=e^{(w_0+nw)\theta}m_n(k)$ (up to the Jacobian weight of the measure). Nonzero symbols with distinct $n$ are therefore linearly independent.*

*Proof.* Uniqueness in Lemma 6.2 makes the branch covariant, and $\mathcal G$ is covariant by assumption; compare coefficients of $\epsilon^n$. Eigenfunctions of a one-parameter group of linear maps with distinct exponents are linearly independent. $\square$

For dilations, $m_n$ is homogeneous in $k$ of degree increasing with $n$. For boosts, $m_n$ is proportional to $e^{(w_0+nw)\vartheta(k)}$ times a $\vartheta$-independent factor, where $\vartheta$ is the rapidity. In both cases distinct orders are independent.

---

## 7. Involution and independence

### 7.1 Setting

Let the bulk equation be Hamiltonian, $v_t=\mathcal J\,\delta H/\delta v$, with a **constant-coefficient** skew-adjoint operator $\mathcal J$ and a vacuum-normalised local $H=H_2+H_{\ge3}$. The linearised system $v_t=\mathcal J\,\delta H_2/\delta v$ has normal modes $a_j(k)$ with real-analytic frequencies $\omega_j(k)$. A monomial $\prod_i a_{j_i}^{(s_i)}(k_i)$, where $s_i=-1$ marks a complex conjugate, has momentum $\sum s_ik_i$ and frequency $\Omega=\sum_is_i\omega_{j_i}(k_i)$.

This setting covers all the massive observed cases:

| bulk | $\mathcal J$ | $\omega(k)$ |
|---|---|---|
| relativistic scalars | canonical $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ on $(\phi,\phi_t)$ | $\pm\sqrt{k^2+m_j^2}$ |
| NLS | $-i$ | $k^2$ |
| KdV, mKdV | $D_x$ | $k^3$ |
| Boussinesq | canonical on $(u,u_t/c^2)$ | $\pm ck\sqrt{1+\kappa^2k^2}$ |

**Definition 7.1 (nonresonance).** (NR) For every $n\ge3$ and every choice of labels and signs, $\Omega$ does not vanish identically on any nonempty open subset of the hyperplane $\sum s_ik_i=0$. (NR2) Every quadratic local functional conserved by the linearised flow is a function of the actions $|a_j(k)|^2$. This holds when distinct normal modes of equal momentum have distinct frequencies on a dense set. It fails for degenerate branches, for example the conjugate particles $a,\bar a$ of $a_r^{(1)}$ Toda with $r\ge2$, whose masses coincide; there one verifies directly that the quadratic parts commute.

Since $\Omega$ is real-analytic, (NR) holds as soon as $\Omega$ is not identically zero. `check_kinematics.py`, part C, confirms this for the table at degrees 3 and 4. It also shows that the massless wave $\omega=|k|$ is resonant on the open set $k_1,k_2>0$. For massive relativistic fields, (NR) at degree 3 is the strict subadditivity of $\sqrt{k^2+m^2}$ that the structural paper uses. For multicomponent theories with different masses, analyticity still gives (NR).

### 7.2 Rigidity

**Lemma 7.2 (rigidity of conserved functionals).** *Assume (NR). Let $F$ be a local functional with polynomial or analytic density, conserved by $H$, whose homogeneous parts of degrees $0,1,2$ vanish. Then $F=0$, i.e. its density is a total $x$-derivative.*

*Proof.* Let $F_d$ be the lowest nonzero part, $d\ge3$. Since $\mathcal J$ is constant, $\{F_a,H_b\}$ has degree $a+b-2$. The degree-$d$ part of $\{F,H\}=0$ is therefore $\{F_d,H_2\}=0$: $F_d$ is conserved by the linearised flow. In normal modes,

$$F_d=\int_{\sum s_ik_i=0}c(k)\prod_ia_{j_i}^{(s_i)}(k_i),$$

with $c$ continuous (polynomial in $k$ times analytic mode vectors). Conservation gives $c\,\Omega=0$ on the hyperplane. By (NR) the zero set of $\Omega$ has empty interior, so $c\equiv0$ and $F_d=0$, a contradiction. A homogeneous polynomial local functional vanishes exactly when its density is a total derivative. $\square$

The inductive structure is `graded_rigidity`.

**Theorem 7.3 (involution).** *Assume (NR), and either (NR2) or that the quadratic parts $Q_{n,2}$ commute pairwise. Let $Q_n$ be vacuum-normalised local functionals conserved by $H$ such that*

$$\text{(L)}\qquad \{Q_{n,1},Q_m\}=0\quad\text{for all }n,m,$$

*where $Q_{n,1}$ is the linear part (vacuous when there are no linear parts; satisfied by Casimirs such as $\int u$ for $\mathcal J=D_x$, and by generators of symmetries that leave every $Q_m$ invariant). Then $\{Q_n,Q_m\}=0$ for all $n,m$.*

*Proof.* $B=\{Q_n,Q_m\}$ is local and, by the Jacobi identity, conserved. By (L) its parts of degrees $0$ and $1$ vanish, and its quadratic part is $\{Q_{n,2},Q_{m,2}\}$. Each $Q_{n,2}$ is a quadratic functional conserved by the linearised flow. By (NR2) it is a function of the actions $|a_j(k)|^2$ alone, so two such functionals commute; otherwise their commutation is assumed. Lemma 7.2 gives $B=0$. $\square$

**Theorem 7.4 (independence).** *If the quadratic symbols $m_n(k)$ of $Q_n$, $n\in S$ finite, are linearly independent functions, then the gradients $\delta Q_n$, $n\in S$, are linearly independent at all sufficiently small fields with $|S|$ generic Fourier modes. In particular the $Q_n$ are functionally independent and nontrivial.*

*Proof.* At $v=\varepsilon v_0$ with $v_0$ supported on modes $k_1,\dots,k_M$ ($M\ge|S|$), $\delta Q_n(v)=\varepsilon\,m_n(k_l)\hat v_0(k_l)+O(\varepsilon^2)$ on mode $k_l$; a linear part contributes only at $k=0$. Linearly independent functions admit points $k_l$ at which the matrix $(m_n(k_l))$ has full rank. For small $\varepsilon$ the gradients remain independent. $\square$

With Lemma 6.5, Theorem 7.4 needs only that infinitely many $m_n$ are nonzero.

**Proposition 7.6 (generating quadratic symbol).** *Let a family have a formal branch and a generating density $\mathcal G$, with charges $Q_n$. Put $m(k;\epsilon)=\sum_n\epsilon^nm_n(k)$, where $m_n$ is the quadratic symbol of $Q_n$. Then $m(k;\epsilon)$ is the coefficient of $\eta^2|a|^2$ in the $x$-average of $\mathcal G$, evaluated on $\phi=\eta(aE+\bar a E^{-1})$, $E=e^{i(kx-\omega(k)t)}$, with $\Delta$ solved from the branch equation exactly in $\epsilon$: at order $\eta$ for the first harmonic, and at order $\eta^2$ for the zero mode.*

*Proof.* The $x$-average at order $\eta^2$ receives contributions only from products of two first harmonics and from zero modes of second-order quantities. $D_x$ and $D_t$ annihilate zero modes, and the linearised branch equation has constant coefficients. Hence the second harmonics, and the second-order correction to $\phi$ needed to solve the bulk equation, do not contribute. Linear parts of $Q_n$ contribute nothing to the average. $\square$

Proposition 7.6 turns nondegeneracy into a finite computation, exact in $\epsilon$ (`checks/check_symbols.py`). For the observed cases with their published defects:

| bulk | generating symbol $m(k;\epsilon)$ | nonzero orders |
|---|---|---|
| sine-Gordon ($k=\sinh\vartheta$, $\omega=\cosh\vartheta$) | $4\epsilon\,\omega\,e^{\vartheta}/(1+\epsilon^2e^{2\vartheta})$ | all odd; $m_{2j+1}=4(-1)^j\omega e^{(2j+1)\vartheta}$ |
| NLS | $-2\epsilon/(1+\epsilon^2k^2)$ | all odd; $m_{2j+1}\propto k^{2j}$ |
| KdV | $2\epsilon^3/(4+\epsilon^2k^2)$ | all odd $\ge3$; $m_{2j+3}\propto k^{2j}$ |
| mKdV | $-4\epsilon/(1+\epsilon^2k^2)$ | all odd; $m_{2j+1}\propto k^{2j}$ |
| Boussinesq ($c=\kappa=1$, $\lambda=3$) | rational in $\epsilon$, $k$, $\sqrt{1+k^2}$ | every order $\ge4$ computed |

In the first four rows the symbols of distinct orders have distinct boost or dilation weights, as Lemma 6.5 predicts. These families are therefore nondegenerate, and by Theorem 7.4 they give infinitely many independent charges. For Boussinesq the weight argument is unavailable. The computed symbols are linearly independent up to at most one relation: the span of the first 18 nonzero symbols has dimension at least 17. This is evidence, not a proof, of infinitely many independent charges.

**Definition 7.5 (nondegenerate family).** A family with a formal branch is *nondegenerate* if the quadratic symbols $m_n$ of its generating density are nonzero for infinitely many $n$. Trivial families, such as the symmetry-identification defect of Remark 3.4.2 or $\psi=\phi$, are degenerate.

---

## 8. The main theorem

**Theorem 8.1 (kinematic integrability theorem).** *Let $\mathcal L$ be an admissible bulk Lagrangian. Assume:*

*(A) (bulk) the equation of $\mathcal L$ is Hamiltonian with a constant Poisson operator, and satisfies (NR) and (NR2);*

*(B) (momentum) $S_d$ is a momentum-conserving defect (Definition 3.1) between $\mathcal L$ and itself, satisfying (I);*

*(C) (family) $S_d$ embeds in a nondegenerate family with a formal branch (Definitions 6.1, 7.5) that is covariant under a one-parameter group of point symmetries of $\mathcal L$ (Lemmas 5.4, 5.5, 6.5) — or, without such covariance, whose quadratic symbols are linearly independent;*

*(D) (closure) $\mathcal L$ has an affine conservation law whose constituent laws have defect charges (Lemma 5.2, Corollary 5.3), and the resulting $Q_n$ satisfy (L).*

*Then the equation of $\mathcal L$ has infinitely many functionally independent local conserved charges in involution. Moreover every solution of the sewing system at all $x$ is a pair of solutions (Theorem 3.3).*

*Proof.* Theorem 3.3 and Lemma 3.5 give Bäcklund relations. Proposition 4.3 with Lemma 5.2 gives the generating density. Theorem 6.4 gives the local conservation laws, Theorem 7.3 their involution, and Lemma 6.5 with Theorem 7.4 their independence. $\square$

Hypothesis (B) is the Corrigan–Zambon hypothesis. Hypotheses (A) and (D) concern the bulk theory alone. They hold for whole classes of non-integrable theories, for example all massive relativistic scalars, so they do not smuggle in integrability. The entire gap between momentum conservation and integrability lies in hypothesis (C).

---

## 9. The observed cases

Every case in Section 1.2 of the [conjecture report](conjecture_report.md) is listed below with the hypotheses it satisfies. "Check" refers to `checks/` (Appendix B). Defect functionals are those of the cited papers, transcribed in the scripts; each balance check passing confirms the transcription.

| case | (B) balance (3.3) | (I) | family | closure (D) | formal branch | (A) | charges |
|---|---|---|---|---|---|---|---|
| sine/sinh-Gordon, Type I (BCZ 2003) | check | vacuous | boost, check | Lorentz, check | check (Lemma 3.5) | massive | $Q_1,Q_3,Q_5$ nontrivial, check; all orders: structural paper |
| $a_r^{(1)}$ Toda, Type I (BCZ 2004) | check for $a_2^{(1)}$ | vacuous | boost (Lemma 5.5) | Lorentz | structural paper, Thm 2.1 | massive | structural paper |
| Liouville $\vert$ free, conformal Toda, free massless | check (Liouville $\vert$ free) | vacuous | — | Lorentz | — | **fails (NR)** | Theorem 3.3 only: Bäcklund relation to a free field |
| Tzitzéica $a_2^{(2)}$, Type II (CZ 2009) | check, $P_d=f-g$ | $S_{\lambda\lambda}=-\partial_\lambda^2\mathcal D\ne0$ | boost | Lorentz | **not checked** | massive | open in this paper |
| $r>1$ Type II, fixed affine Toda bulk | by the cited papers | to check per defect | boost | Lorentz | **not checked** | massive | open in this paper |
| NLS (CZ 2006) | check | vacuous | dilation, check | Galilean, check | check, all four sewing equations | yes | check |
| KdV (CZ 2006, multiplier) | check | $S_{\Phi_1\mu}=1$ | dilation, check | Galilean, check | check, all sewing equations | yes | odd orders nontrivial, check; all orders: Gardner, [reconstruction](../theorem_D_reconstruction/proof.md) §9 |
| mKdV (CZ 2006, multiplier) | check | $S_{\Phi_1\mu}=1$ | dilation, check | dilation, check | check | yes | check |
| Boussinesq (CZ 2023) | check | vacuous | $\sigma_0$: modulus of the momentum constraint, not kinematic | time-linear shift, check | check | yes | check of low orders; independence needs Theorem 7.4 directly |

Comments.

1. *Massless theories.* For the free massless field, Liouville and conformal Toda, Theorem 3.3 shows that the momentum-conserving defects are Bäcklund relations to free fields. These theories are integrable in the sense of linearisability. Theorem 7.3 does not apply, because the massless dispersion is resonant on an open set. This matches the massless obstruction of the structural paper.
2. *Heterogeneous defects.* Theorem 3.3 covers defects between different theories. Theorems 6.4–7.4 assume $\mathcal L_-=\mathcal L_+$, because the transparent limit joins a theory to itself. Section 11 of the structural paper explains why transparency forces equal potentials up to a field shift.
3. *Type II.* Theorem 3.3 and the closure lemma cover Type-II defects. The formal branch for Type II (the analogue of Lemma 3.5 with $\lambda$) has not been computed here. It is the main open verification among the observed cases.
4. *Boussinesq.* Its spectral parameter is not produced by a kinematic symmetry: the dimensional constants $c,\kappa,\lambda$ exclude a dilation. The parameter $\rho_0$ is a time-linear-shift orbit, but $\sigma_0$ is a genuine modulus of the momentum constraint. Lemma 6.5 is unavailable, and independence must be checked through Theorem 7.4 directly.

---

## 10. What remains open

1. **Hypothesis (C) from momentum conservation alone.** Theorem 3.3 extracts a Bäcklund relation from a single momentum-conserving defect. A local hierarchy needs a one-parameter family with a regular transparent limit. In the observed cases the family arises in two ways: as the orbit of a kinematic symmetry *not* preserved by the defect (boosts for relativistic theories; dilations for NLS, KdV and mKdV), or as a modulus of the momentum constraint (Boussinesq $\sigma_0$; the potential splitting $\mathcal B_d=F+G$ that makes $(F,G)\mapsto(\sigma F,\sigma^{-1}G)$ a symmetry of the constraint in Theorem A). A general theorem would show that the momentum constraint always has such a modulus, or that a kinematic orbit is always nondegenerate with a regular transparent limit. For massive relativistic Type-I defects the structural paper proves this. In general it is open.
2. **Bulk selection.** Theorems A–C of the conjecture report show, for relativistic scalars, that momentum conservation restricts the bulk potentials. The general framework does not classify. Its integrability conclusion is conditional on (C), not derived from the shape of the potential.
3. **Type-II formal branches** (Section 9, comment 3), and the Boussinesq independence check.
4. **Function spaces.** Everything here is formal or local. Convergence of the parameter series and global Bäcklund maps are not addressed.

---

## Appendix A. The spatial Hamilton–Jacobi interpretation

The pre-structural paper phrased Theorem 3.3 geometrically, and that reading remains correct under its stated hypotheses. Equip the product of spatial phase spaces with $\Omega_-^{(x)}\ominus\Omega_+^{(x)}$, $\Omega^{(x)}=\int dt\,\delta\Phi\wedge\delta\pi$. Pulling back the Liouville form $\Theta_-^{(x)}-\Theta_+^{(x)}$ to $\Gamma_d$ gives $-\delta S_d$, so $\Gamma_d$ is isotropic. Without auxiliary fields it is also coisotropic in the formal cotangent setting. Pairing a vector symplectically orthogonal to $T\Gamma_d$ against the variations $(\delta\Phi',0)$ and $(0,\delta\Psi')$, and using self-adjointness of the second variations, shows that it lies in $T\Gamma_d$. Thus $\Gamma_d$ is Lagrangian in the strong sense $T\Gamma_d^\perp=T\Gamma_d$ (Lean: `eq_3_6_generating_functional_lagrangian` in the [earlier project](../../lean/DefectIntegrability.lean)). The balance (3.3) integrated over $t$ says that $H_-^{(x)}-H_+^{(x)}$ is constant on $\Gamma_d$: this is the spatial Hamilton–Jacobi equation. Lemma 3.1 of the pre-structural paper then gives tangency. Theorem 3.3 reaches the same conclusion more directly. It needs neither coisotropy nor the integration over $t$, and it handles auxiliary fields through the multiplier $\rho$.

Conversely, if $(X_-,X_+)$ is tangent to an isotropic $\Gamma_d$, then $\delta(H_--H_+)$ vanishes on $T\Gamma_d$, so $H_--H_+$ is constant on each connected component. For Type-I defects, whose boundary data are free, the density $\mathcal H_--\mathcal H_+$ on $\Gamma_d$ then has vanishing $t$-Euler derivative and is a total derivative: momentum is conserved. A sewing-form Bäcklund relation of Type I is therefore a momentum-conserving defect.

## Appendix B. Verification

From the repository root:

```sh
cd defect-integrability/general_framework/checks
python3 check_balance.py      # Definition 3.1 for all observed cases
python3 check_tangency.py     # Theorem 3.3(a) directly: Type I, Type II, multiplier
python3 check_kinematics.py   # Lemma 5.2 table, Lemmas 5.4-5.5 examples, (NR)
python3 check_hierarchy.py    # formal branches and conserved Q_n (sg, nls, kdv, mkdv, bsq)
cd ../lean && lake build && lake env lean Audit.lean
```

The recorded output is [verification.txt](verification.txt). The Lean project checks the algebraic core of each general lemma over an arbitrary commutative ring with commuting derivations. It uses no `sorry` and no added axioms, and it includes a nonzero model (`Tri`) with two nonzero commuting derivations. It does not formalise the variational calculus, the Fourier analysis of Section 7, or the infinite-dimensional geometry. Those are written proofs.

## References

1. P. Bowcock, E. Corrigan, C. Zambon, *Classically integrable field theories with defects*, Int. J. Mod. Phys. A **19S2** (2004) 82 (`hep-th/0305022`).
2. P. Bowcock, E. Corrigan, C. Zambon, *Affine Toda field theories with defects*, JHEP **0401** (2004) 056 (`hep-th/0401020`).
3. E. Corrigan, C. Zambon, *Jump-defects in the nonlinear Schrödinger model and other non-relativistic field theories*, Nonlinearity **19** (2006) 1447 (`nlin/0512038`).
4. E. Corrigan, C. Zambon, *A new class of integrable defects*, J. Phys. A **42** (2009) 475203 (`0908.3126`).
5. E. Corrigan, C. Zambon, *Adding integrable defects to the Boussinesq equation*, J. Phys. A **56** (2023) 345203 (`2306.03772`).
6. R. Bristow, P. Bowcock, *Momentum conserving defects in affine Toda field theories*, JHEP **05** (2017) 153 (`1612.03002`).
7. V. Caudrelier, A. Kundu, *A multisymplectic approach to defects in integrable classical field theory*, JHEP **02** (2015) 088 (`1411.0418`).
8. P. J. Olver, *Applications of Lie Groups to Differential Equations*, 2nd ed., Springer (1993).
9. A. Weinstein, *Symplectic manifolds and their Lagrangian submanifolds*, Adv. Math. **6** (1971) 329.
