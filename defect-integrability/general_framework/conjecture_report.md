# The Corrigan–Zambon Defect Integrability Conjecture: Formulations, Results and their Scope

*Rescued revision of [corrigan_zambon_conjecture_report.md](../corrigan_zambon_conjecture_report.md), 20 October 2026. The original file is preserved unchanged.*

**Status of this revision.**
- Section 1 keeps the literature record. Quotes 1 and 4 were checked against the arXiv texts of `0908.3126` and `2306.03772`; quotes 2 and 3 were not re-checked in this revision.
- The inventory table (Section 1.2) now records what is actually established for each case.
- Conjecture 2 and Theorem D (Sections 2.2 and 6) are replaced by the conditional general theorems of the [general-framework paper](paper.md). The earlier claim of a structural proof of Conjecture 2 "in full generality" is withdrawn.
- Theorems A–C (Sections 3–5) are kept verbatim as the classification part of the programme, with a status note. They were **not** re-reviewed in this revision.

## 1. Background and Verbatim Literature Record

### 1.1 Verbatim Statements of the Conjecture

Across a twenty-year programme investigating classical and quantum integrable defects (`hep-th/0305022`, `hep-th/0401020`, `nlin/0512038`, `0902.1307`, `0908.3126`, `1807.05747`, `2006.14447`, `2306.03772`), Edward Corrigan and Cristina Zambon observed that whenever two $(1+1)$-dimensional local field theories are joined across a pointlike discontinuity (jump defect) at $x=0$ without specifying the bulk potentials in advance, requiring total energy and canonical momentum to be conserved across the defect forces the defect conditions to act as a spatial Bäcklund transformation and forces both bulk field theories to be classically integrable.

The four explicit statements of the conjecture in their papers are:

1. **Corrigan & Zambon (2009)**, *A new class of integrable defects*, J. Phys. A: Math. Theor. **42** (2009) 475203 (`arXiv:0908.3126`), Section 1, p. 2:
   > *"On the other hand, previous experience strongly suggests the conditions following from momentum conservation in the presence of a defect are more or less equivalent to the restrictions imposed by integrability: for example, even if the bulk models on either side of the defect are not specified in advance, they will be severely restricted by insisting on momentum conservation once the defect is taken into account."*

2. **Corrigan & Zambon (2018)**, *Type II defects revisited*, JHEP **09** (2018) 019 (`arXiv:1807.05747`), Section 1, p. 2 & Section 6, p. 26:
   > *"Intriguingly, insisting upon sewing conditions that maintain the conservation of energy and momentum seems to be sufficient to guarantee integrability. There is no direct proof of this but there is a body of evidence from many specific cases that indicates it should be the case."*
   > *"Somehow, demanding both energy and momentum conservation singles out the integrable models."*

3. **Corrigan & Zambon (2020)**, *Integrable defects at junctions within a network*, J. Phys. A: Math. Theor. **53** (2020) 484001 (`arXiv:2006.14447`), Section 1, p. 2:
   > *"At least in the relativistic case, presenting the argument the other way round, the presence of defects that preserve a suitably modified energy and momentum seems to require the fields on either side of the defect to be integrable."*

4. **Corrigan & Zambon (2023)**, *Adding integrable defects to the Boussinesq equation*, J. Phys. A: Math. Theor. **56** (2023) 345203 (`arXiv:2306.03772`), Section 1, p. 2:
   > *"In fact, in all situations studied so far, the insistence on a conserved overall momentum including a defect contribution actually requires the fields to either side of a defect to satisfy integrable field equations."*

---

### 1.2 Inventory of observed cases and what is established

The bulk theories in every row are known to be integrable. The question is which general statement derives that from momentum conservation. "Paper" refers to the [general-framework paper](paper.md); "structural" to the [structural paper](../defect_integrability_paper.md); checks are in [checks/](checks/).

| Setting | Reference(s) | Bulk input assumed | Bulk theories selected | Bäcklund property (Paper, Thm 3.3) | Hierarchy (Paper, Thm 8.1) | Classification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| $r=1$ relativistic scalar, Type I | BCZ 2003 (`hep-th/0305022`); CZ 2009 (`0902.1307`) | unspecified $U,V$ | free, Liouville, sine/sinh-Gordon | yes (balance checked for sine-Gordon and Liouville $\vert$ free) | massive: yes (structural, all orders; checks); massless: no, resonant; Bäcklund to a free field instead | Theorem B ($r=1$), not re-reviewed |
| $r\ge1$ relativistic scalars, Type I | BCZ 2004 (`hep-th/0401020`); CZ 2009 | exponential ansatz | $a_r^{(1)}$ affine and $a_r$ conformal Toda | yes (balance checked for $a_2^{(1)}$) | affine Toda: yes (structural); conformal Toda: no, resonant | Theorem B, not re-reviewed |
| $r=1$ relativistic scalar, Type II | CZ 2009 (`0908.3126`); CZ 2018 (`1807.05747`) | unspecified $U,V$ | free, Liouville, sine/sinh-Gordon, Tzitzéica | yes; (I) holds since $\partial_\lambda^2\mathcal D\ne0$ (balance checked for Tzitzéica) | conditional: Type-II formal branch not yet computed | Theorem C, not re-reviewed |
| $r>1$ relativistic scalars, Type II | CZ 2011 (`1012.4186`); Robertson 2014 (`1304.3129`); Bristow–Bowcock 2017 (`1612.03002`) | affine Toda bulk fixed | compatible defect potentials | yes, given the cited momentum conservation and (I) | conditional, as above | — |
| NLS | CZ 2006 (`nlin/0512038` §2) | $V(\vert u\vert^2)$ | cubic NLS | yes (balance checked) | yes: dilation family, Galilean closure, branch and charges checked | CZ's computation; not reproduced |
| KdV, mKdV | CZ 2006 (`nlin/0512038` §§7, 9) | $U(p_x)$ | KdV, mKdV | yes, constrained defects with multiplier; (I) holds (balance checked) | yes: dilation family; Galilean (KdV) or dilation (mKdV) closure; branches and charges checked | CZ's computation; not reproduced |
| Boussinesq | CZ 2023 (`2306.03772` §3) | $U(\phi_x)$ | Boussinesq | yes (balance checked) | family parameter $\sigma_0$ is not kinematic; branch and low-order charges checked; independence to be checked directly | CZ's computation; not reproduced |

## 2. General Formulations of Conjectures 1 and 2

Throughout, we follow the conventions of Part VIII ([38-defect-conditions.qmd](../../part8-defects/38-defect-conditions.qmd) and [part8_defects_conventions.md](../../briefs/part8_defects_conventions.md)): $\vec\phi(x,t) \in \mathbb R^r$ lives on $x<0$, $\vec\psi(x,t) \in \mathbb R^r$ lives on $x>0$, and $\vec\lambda(t) \in \mathbb R^m$ ($m\ge 0$) is a collection of auxiliary fields confined to the defect line $x=0$.

### 2.1 Conjecture 1 (Multi-Component Relativistic Scalar Field Theories)

Consider the total action
$$S[\vec\phi,\vec\psi,\vec\lambda] = \int dt \left\{ \int_{-\infty}^0 dx\,\mathcal L_-(\vec\phi,\partial\vec\phi) + \int_0^\infty dx\,\mathcal L_+(\vec\psi,\partial\vec\psi) + \left.\mathcal L_d(\vec\phi,\vec\psi,\vec\lambda,\dot{\vec\phi},\dot{\vec\psi},\dot{\vec\lambda})\right|_{x=0} \right\},$$
where the bulk Lagrangians are relativistic scalar theories with unspecified smooth potentials $U,V \in C^\infty(\mathbb R^r)$:
$$\mathcal L_- = \frac{1}{2}|\partial_t\vec\phi|^2 - \frac{1}{2}|\partial_x\vec\phi|^2 - U(\vec\phi), \qquad \mathcal L_+ = \frac{1}{2}|\partial_t\vec\psi|^2 - \frac{1}{2}|\partial_x\vec\psi|^2 - V(\vec\psi).$$

**Non-Degeneracy Assumptions on the Sewing Relation:**
1. *(First-order defect dynamics without holonomic constraints)* $\mathcal L_d$ depends at most on the boundary values $(\vec\phi,\vec\psi,\vec\lambda)$ and their first time derivatives $(\dot{\vec\phi},\dot{\vec\psi},\dot{\vec\lambda})$ at $x=0$, without rigid pointwise constraints $C(\vec\phi,\vec\psi)=0$ (such as trivial continuity $\vec\psi = \vec\phi$ or discrete symmetry identifications $\vec\psi = -\vec\phi$) reducing the $2r$ independent boundary values.
2. *(Genuine transmission / non-reflection)* The defect couples every component across $x=0$ without reducing to decoupled half-line boundaries ($\det \mathsf D \ne 0$, where $\mathsf D_{ab} = \frac{\partial^2\mathcal L_d}{\partial\phi_a\partial\dot\psi_b} - \frac{\partial^2\mathcal L_d}{\partial\dot\phi_a\partial\psi_b}$).
3. *(Irreducibility)* The system does not split under an orthogonal transformation of $\mathbb R^r$ into independent subsystems, nor can redundant or decoupled components of $\vec\lambda$ be eliminated algebraically.

**Conjecture 1:** *Suppose there exists a smooth defect momentum $P_d(\vec\phi,\vec\psi,\vec\lambda,\dot{\vec\phi},\dot{\vec\psi},\dot{\vec\lambda})\big|_{x=0}$ such that the total canonical momentum*
$$P = -\int_{-\infty}^0 dx\,\partial_t\vec\phi\cdot\partial_x\vec\phi - \int_0^\infty dx\,\partial_t\vec\psi\cdot\partial_x\vec\psi + P_d\big|_{x=0}$$
*obeys $\frac{dP}{dt} = 0$ on all smooth solutions of the bulk-plus-defect Euler–Lagrange equations. Then:*
1. *(Chiral Bäcklund Equivalence — proved in full in **Theorem A** below)* Up to an orthogonal basis change on $\vec\psi$, a gauge addition of a total time derivative to $\mathcal L_d$, and a Darboux coordinate choice on $\vec\lambda$, $\mathcal L_d$ is necessarily linear in time derivatives,
   $$\mathcal L_d = \frac{1}{2}\vec\phi\cdot E\dot{\vec\phi} + \vec\phi\cdot\mathsf D\dot{\vec\psi} + \frac{1}{2}\vec\psi\cdot E\dot{\vec\psi} + 2\vec q\cdot M\dot{\vec\lambda} + \vec\lambda\cdot E_\lambda\dot{\vec\lambda} - \mathcal B_d(\vec\phi,\vec\psi,\vec\lambda),$$
   with $E^{\mathsf T} = -E$, $\mathsf D = \mathsf I - E$, $\vec q = \frac{1}{2}(\vec\phi-\vec\psi)$, and the defect potential and momentum split into chiral halves $\mathcal B_d = \sigma F + \sigma^{-1} G$, $P_d = -(\sigma F - \sigma^{-1} G)$ defining a 1-parameter family of spatial Bäcklund transformations $\mathfrak B_\sigma$ between $\partial_{tt}\vec\phi - \partial_{xx}\vec\phi + \nabla U(\vec\phi) = 0$ and $\partial_{tt}\vec\psi - \partial_{xx}\vec\psi + \nabla V(\vec\psi) = 0$.
2. *(Bulk Integrability — proved for all $r\ge 1, m=0$ in **Theorem B** and for $r=1, m\le 1$ in **Theorem C**)* The potentials $U(\vec\phi)$ and $V(\vec\psi)$ are restricted to the class of classically integrable relativistic scalar field theories (free, Liouville, conformal Toda, or affine Toda field theories associated with a Kac–Moody root system).

---

### 2.2 Conjecture 2 (general local Lagrangian field theories)

Let $\mathcal L_-([\vec\phi])$ on $x<0$ and $\mathcal L_+([\vec\psi])$ on $x>0$ be translation-invariant local Lagrangian densities of finite order, joined at $x=0$ by a local defect functional $S_d=\int dt\,\mathcal L_d$ that may contain auxiliary fields and Lagrange multipliers.

**Conjecture 2.** *If there is a local defect momentum $P_d$ such that $P_-+P_++P_d$ is conserved, then (i) the sewing conditions are a Bäcklund transformation, and (ii) the bulk theories are integrable.*

**What is proved** (see the [general-framework paper](paper.md)):
- **Part (i) holds in general** (Theorem 3.3). Momentum conservation in the precise form of Definition 3.1 implies that the spatial Hamiltonian flows are tangent to the sewing correspondence. Every solution of the sewing equations imposed at all $x$ solves both bulk equations, under the injectivity condition (I). Condition (I) is vacuous without auxiliary fields. No Lagrangian, transversality or connectedness hypothesis is needed.
- **Part (ii) holds conditionally** (Theorem 8.1). The extra hypotheses are: (A) a constant Poisson operator and nonresonant dispersion; (C) a nondegenerate one-parameter family of defects with a regular transparent limit; (D) an affine conservation law whose constituent laws have defect charges. Hypotheses (A) and (D) concern the bulk alone and hold for all massive relativistic theories, integrable or not. Hypothesis (C) is where integrability enters; deriving it from momentum conservation alone is open (Paper, Section 10).
- Momentum conservation does **not** by itself force integrability. Symmetry-identification defects such as $\psi=-\phi$ conserve momentum for any even potential; they are trivial Bäcklund relations with degenerate families.

The earlier formulation of Conjecture 2, with its claim of a structural proof as Theorem D, is in the [original report](../corrigan_zambon_conjecture_report.md).

---

> **Status of Sections 3–5 in this revision.** Theorems A–C are kept verbatim. They were not re-reviewed here; only these consistency checks were made. The Type-I identity (A.14), with $\mathsf D=2(\mathsf I-\pi)^{-1}$ from the Coxeter element as in Step B.3, gives a momentum-conserving $a_2^{(1)}$ Toda defect ([checks/check_balance.py](checks/check_balance.py)). The Type-I momentum constraints agree with those rederived in the [structural paper](../defect_integrability_paper.md), Section 3. The list in Theorem C agrees with CZ `0908.3126`, Section 3, and the Tzitzéica defect of that paper conserves momentum ([checks/check_balance.py](checks/check_balance.py)). Lemma A.1 (constancy of $E_\phi,\mathsf D,E_\psi$), Step B.1 (Levi-Civita separation) and Step C.2 (root ratios) need independent review before they are relied on.

## 3. Complete Proof of Theorem A (Universal Chiral Bäcklund Equivalence for All $r\ge 1, m\ge 0$)

### Theorem A (Universal Chiral Bäcklund Equivalence)
*Let $\mathcal L_-$ and $\mathcal L_+$ be $r$-component relativistic scalar field theories with arbitrary smooth potentials $U,V \in C^\infty(\mathbb R^r)$, joined at $x=0$ by a first-order defect Lagrangian $\mathcal L_d(\vec\phi,\vec\psi,\vec\lambda,\dot{\vec\phi},\dot{\vec\psi},\dot{\vec\lambda})$ with $\vec\lambda \in \mathbb R^m$ ($m\ge 0$) satisfying the non-degeneracy conditions of Section 2.1. Then total canonical momentum $P = P_- + P_+ + P_d$ is conserved on-shell ($\dot P = 0$) if and only if, up to an $O(r)$ basis rotation of $\vec\psi$, addition of a total time derivative to $\mathcal L_d$, and a coordinate transformation on $\vec\lambda$:*

1. *(Gyroscopic structure and Cayley orthogonality)* $\mathcal L_d$ is linear in time derivatives:
   $$\mathcal L_d = \frac{1}{2}\vec\phi\cdot E\dot{\vec\phi} + \vec\phi\cdot\mathsf D\dot{\vec\psi} + \frac{1}{2}\vec\psi\cdot E\dot{\vec\psi} + 2\vec q\cdot M\dot{\vec\lambda} + \vec\lambda\cdot E_\lambda\dot{\vec\lambda} - \mathcal B_d(\vec\phi,\vec\psi,\vec\lambda), \tag{A.1}$$
   where $E^{\mathsf T} = -E$, $\mathsf D = \mathsf I_r - E$ (so $\mathsf D + \mathsf D^{\mathsf T} = 2\mathsf I_r$), $\vec q = \frac{1}{2}(\vec\phi - \vec\psi)$, and $E_\lambda^{\mathsf T} = -E_\lambda$.

2. *(Chiral d'Alembert splitting)* Introducing the twisted sum coordinate $\vec w := \frac{1}{2}(\mathsf D^{\mathsf T}\vec\phi + \mathsf D\vec\psi) = \vec u + E\vec q$ (where $\vec u = \frac{1}{2}(\vec\phi + \vec\psi)$, so $\vec\phi = \vec w + \mathsf D\vec q$ and $\vec\psi = \vec w - \mathsf D^{\mathsf T}\vec q$) and when $E_\lambda = 0$ the characteristic coordinates $\vec w_\pm := \vec w \pm M\vec\lambda$, the defect potential $\mathcal B_d$ and defect momentum $P_d$ split into chiral halves:
   $$\mathcal B_d = F(\vec w_+, \vec q) + G(\vec w_-, \vec q), \qquad P_d = -F(\vec w_+, \vec q) + G(\vec w_-, \vec q), \tag{A.2}$$
   where for Type I ($m=0$, $M=0$), $F = f(\vec w)$ is independent of $\vec q$ and $G = g(\vec q)$ is independent of $\vec w$.

3. *(Generalized Poisson-bracket potential identity and Bäcklund system)* The functions $(U,V,F,G)$ obey the exact zero-velocity identity
   $$U(\vec w + \mathsf D\vec q) - V(\vec w - \mathsf D^{\mathsf T}\vec q) = \nabla_{\vec w_+}F(\vec w_+, \vec q)\cdot\nabla_{\vec q}G(\vec w_-, \vec q) + \nabla_{\vec q}F(\vec w_+, \vec q)\cdot\nabla_{\vec w_-}G(\vec w_-, \vec q) \tag{A.3}$$
   (which for Type I reduces to $U(\vec w + \mathsf D\vec q) - V(\vec w - \mathsf D^{\mathsf T}\vec q) = \frac{1}{2}\nabla_{\vec w}f(\vec w)\cdot\nabla_{\vec q}g(\vec q)$ with $F = \frac{1}{\sqrt 2}f, G = \frac{1}{\sqrt 2}g$), and under Lorentz boosts $(x^+, x^-) \mapsto (\sigma x^+, \sigma^{-1}x^-)$ the defect equations form a 1-parameter family of spatial Bäcklund transformations $(F,G) \mapsto (\sigma F, \sigma^{-1}G)$ between $\square\vec\phi + \nabla U(\vec\phi) = 0$ and $\square\vec\psi + \nabla V(\vec\psi) = 0$.

---

### Proof of Theorem A

#### Step A.1: Linearity of $\mathcal L_d$ in the Velocities
Let $Y = (\vec\phi, \vec\psi, \vec\lambda) \in \mathbb R^{2r+m}$ denote the boundary variables at $x=0$. The boundary Euler–Lagrange equations obtained from $\delta S = 0$ at $x=0$ are
$$\partial_x\vec\phi = \frac{\partial\mathcal L_d}{\partial\vec\phi} - \frac{d}{dt}\left(\frac{\partial\mathcal L_d}{\partial\dot{\vec\phi}}\right), \qquad \partial_x\vec\psi = -\frac{\partial\mathcal L_d}{\partial\vec\psi} + \frac{d}{dt}\left(\frac{\partial\mathcal L_d}{\partial\dot{\vec\psi}}\right), \qquad 0 = \frac{\partial\mathcal L_d}{\partial\vec\lambda} - \frac{d}{dt}\left(\frac{\partial\mathcal L_d}{\partial\dot{\vec\lambda}}\right). \tag{A.4}$$
For the sewing relation at $x=0$ to be a first-order transmission condition (free of second-order time derivatives $\ddot Y$), the Hessian $\frac{\partial^2\mathcal L_d}{\partial\dot Y_A\partial\dot Y_B}$ must vanish identically. (Indeed, if $\partial_x\vec\phi$ or $\partial_x\vec\psi$ depended linearly on $\ddot Y$, then $\dot P_- + \dot P_+ = \big[-\frac{1}{2}|\dot{\vec\phi}|^2 - \frac{1}{2}|\partial_x\vec\phi|^2 + U(\vec\phi) + \frac{1}{2}|\dot{\vec\psi}|^2 + \frac{1}{2}|\partial_x\vec\psi|^2 - V(\vec\psi)\big]_{x=0}$ would be quadratic in $\ddot Y$, whereas $\dot P_d$ for any first-order $P_d(Y,\dot Y)$ is at most linear in $\ddot Y$.) Thus $\mathcal L_d$ is affine in $\dot Y$:
$$\mathcal L_d = A_\phi(Y)\cdot\dot{\vec\phi} + A_\psi(Y)\cdot\dot{\vec\psi} + A_\lambda(Y)\cdot\dot{\vec\lambda} - \mathcal B_d(Y), \tag{A.5}$$
and $P_d = P_d(\vec\phi,\vec\psi,\vec\lambda)$ is a function of $Y$ alone.

#### Step A.2: Presymplectic 2-Form and Cayley Solution of Quadratic Velocity Cancellation
Let $\Theta = A_\phi\cdot d\vec\phi + A_\psi\cdot d\vec\psi + A_\lambda\cdot d\vec\lambda$ be the velocity 1-form on $\mathbb R^{2r+m}$, and let $\omega = d\Theta$ be its exterior derivative, with antisymmetric block components $\Omega_{AB} = \frac{\partial A_B}{\partial Y_A} - \frac{\partial A_A}{\partial Y_B}$. Setting $E_\phi := \Omega_{\phi\phi}$ ($E_\phi^{\mathsf T} = -E_\phi$), $\mathsf D := \Omega_{\phi\psi}$, and $E_\psi := \Omega_{\psi\psi}$ ($E_\psi^{\mathsf T} = -E_\psi$), the boundary equations (A.4) read
$$\begin{aligned}
\partial_x\vec\phi &= E_\phi\dot{\vec\phi} + \mathsf D\dot{\vec\psi} + M_\phi\dot{\vec\lambda} - \nabla_\phi\mathcal B_d, \\
\partial_x\vec\psi &= \mathsf D^{\mathsf T}\dot{\vec\phi} - E_\psi\dot{\vec\psi} - M_\psi\dot{\vec\lambda} + \nabla_\psi\mathcal B_d, \\
0 &= -M_\phi^{\mathsf T}\dot{\vec\phi} - M_\psi^{\mathsf T}\dot{\vec\psi} + 2E_\lambda\dot{\vec\lambda} - \nabla_\lambda\mathcal B_d.
\end{aligned} \tag{A.6}$$
In the bulk momentum balance $\dot P_- + \dot P_+ + \dot P_d = 0$, the terms quadratic in $(\dot{\vec\phi},\dot{\vec\psi})$ when $\dot{\vec\lambda}=0$ form the quadratic form
$$Q(\dot{\vec\phi},\dot{\vec\psi}) = |\dot{\vec\phi}|^2 + |E_\phi\dot{\vec\phi} + \mathsf D\dot{\vec\psi}|^2 - |\dot{\vec\psi}|^2 - |\mathsf D^{\mathsf T}\dot{\vec\phi} - E_\psi\dot{\vec\psi}|^2.$$
Writing $\mathcal M := \begin{pmatrix} E_\phi & \mathsf D \\ \mathsf D^{\mathsf T} & -E_\psi \end{pmatrix}$ and $J := \begin{pmatrix} \mathsf I_r & 0 \\ 0 & -\mathsf I_r \end{pmatrix}$, the antisymmetry $E_\phi^{\mathsf T} = -E_\phi$ and $E_\psi^{\mathsf T} = -E_\psi$ gives $\mathcal M^{\mathsf T} J = -J\mathcal M$. Hence vanishing of the quadratic form $Q(\dot{\vec\phi},\dot{\vec\psi}) = 0$ is equivalent to
$$J + \mathcal M^{\mathsf T}J\mathcal M = 0 \iff J(\mathsf I_{2r} - \mathcal M^2) = 0 \iff \mathcal M^2 = \begin{pmatrix} E_\phi^2 + \mathsf D\mathsf D^{\mathsf T} & E_\phi\mathsf D - \mathsf D E_\psi \\ \mathsf D^{\mathsf T}E_\phi - E_\psi\mathsf D^{\mathsf T} & \mathsf D^{\mathsf T}\mathsf D + E_\psi^2 \end{pmatrix} = \mathsf I_{2r}. \tag{A.7}$$
Since $E_\phi$ is real skew-symmetric, $\mathsf I_r \pm E_\phi$ is invertible, and $\mathsf D\mathsf D^{\mathsf T} = \mathsf I_r - E_\phi^2 = (\mathsf I_r + E_\phi)(\mathsf I_r - E_\phi)$. Define the Cayley matrix
$$\mathsf O := (\mathsf I_r + E_\phi)^{-1}\mathsf D.$$
Then:
$$\mathsf O\mathsf O^{\mathsf T} = (\mathsf I_r + E_\phi)^{-1}\mathsf D\mathsf D^{\mathsf T}(\mathsf I_r - E_\phi)^{-1} = \mathsf I_r \implies \mathsf O \in O(r),$$
and the off-diagonal block $E_\phi\mathsf D = \mathsf D E_\psi$ yields
$$E_\psi = \mathsf D^{-1}E_\phi\mathsf D = \mathsf O^{\mathsf T}(\mathsf I_r + E_\phi)^{-1}E_\phi(\mathsf I_r + E_\phi)\mathsf O = \mathsf O^{\mathsf T}E_\phi\mathsf O.$$
Performing the orthogonal field redefinition $\vec\psi \mapsto \mathsf O^{\mathsf T}\vec\psi$ (which preserves the bulk kinetic term $\frac{1}{2}|\partial_t\vec\psi|^2 - \frac{1}{2}|\partial_x\vec\psi|^2$) sets $\mathsf O = \mathsf I_r$, giving
$$E_\psi = E_\phi =: E \quad (E^{\mathsf T} = -E), \qquad \mathsf D = \mathsf I_r - E, \qquad \mathsf D + \mathsf D^{\mathsf T} = 2\mathsf I_r. \tag{A.8}$$

**Lemma A.1 (Euclidean Isometry Rigidity — Why $E_\phi, \mathsf D, E_\psi$ Must Be Constant):** *Without assuming in advance that $E_\phi(\vec\phi,\vec\psi), \mathsf D(\vec\phi,\vec\psi), E_\psi(\vec\phi,\vec\psi)$ are constant matrices, closure $d\omega = 0$ combined with $\mathcal M(\vec\phi,\vec\psi)^2 = \mathsf I_{2r}$ forces $E_\phi, \mathsf D, E_\psi$ to be constant on $\mathbb R^{2r}$.*

*Proof of Lemma A.1:* From the linear velocity terms in $\dot P_- + \dot P_+ + \dot P_d = 0$, the differentials of $F = \frac{1}{2}(\mathcal B_d - P_d)$ and $G = \frac{1}{2}(\mathcal B_d + P_d)$ annihilate the $+1$ and $-1$ eigenbundles $T_\pm := \ker(\mathcal M \mp \mathsf I_{2r})$ of $\mathcal M(\vec\phi,\vec\psi)$. On $T_-$, the tangent distribution is defined by $\delta\vec\psi = -\mathsf O^{\mathsf T}(\vec\phi,\vec\psi)\,\delta\vec\phi$, where $\mathsf O(\vec\phi,\vec\psi) = (\mathsf I_r + E_\phi)^{-1}\mathsf D \in O(r)$ is orthogonal at every point $(\vec\phi,\vec\psi)$, and on $T_+$, $\delta\vec\psi = R_+(\vec\phi,\vec\psi)\,\delta\vec\phi$, where $R_+ := \mathsf O^{\mathsf T}(\mathsf I_r + E_\phi)^{-1}(\mathsf I_r - E_\phi) \in O(r)$ is also orthogonal at every point. By $d\omega = 0$ and the non-degeneracy of the chiral coordinates $(\vec w, \vec q)$ parametrizing the leaves of $T_+$ and $T_-$, both $r$-dimensional distributions $T_+$ and $T_-$ are Frobenius integrable. Along any integral leaf $\vec\psi = \vec h(\vec\phi)$ of $T_-$ (or $T_+$), the Jacobian matrix $D\vec h(\vec\phi)$ lies in $O(r)$ everywhere on $\mathbb R^r$:
$$\partial_a\vec h\cdot\partial_b\vec h = \delta_{ab} \implies \partial_c\partial_a\vec h\cdot\partial_b\vec h + \partial_a\vec h\cdot\partial_c\partial_b\vec h = 0.$$
Permuting $(a,b,c)$ cyclicly and subtracting gives $\partial_c\partial_a\vec h\cdot\partial_b\vec h = 0$ for all $a,b,c$, and since $\{\partial_b\vec h\}_{b=1}^r$ is an orthonormal basis of $\mathbb R^r$, $\partial_c\partial_a\vec h = \vec 0$ identically. Thus $\mathsf O$ and $R_+$—and hence $E_\phi = (\mathsf I_r - \mathsf O R_+)(\mathsf I_r + \mathsf O R_+)^{-1}$ and $\mathsf D = (\mathsf I_r + E_\phi)\mathsf O$—are necessarily constant matrices. Furthermore, for the quadratic $\dot{\vec\lambda}$ terms $|M_\phi\dot{\vec\lambda}|^2 - |M_\psi\dot{\vec\lambda}|^2$ to cancel and for the $\dot{\vec\lambda}$ cross-terms to factor through the third defect equation of (A.6), $M_\psi = -M_\phi =: -M$ so that $\vec\lambda$ couples to the jump $\vec q = \frac{1}{2}(\vec\phi - \vec\psi)$, and by closure $d\omega = 0$ (Darboux's theorem) the matrices $M, E_\lambda$ are likewise constant up to a coordinate transformation on $\vec\lambda$ and addition of an exact 1-form $d\chi$ to $\Theta$. This establishes (A.1). $\square$

#### Step A.3: Exact Cancellation of Velocity Terms and Chiral d'Alembert Splitting
Pass to the sum and difference coordinates $\vec u = \frac{1}{2}(\vec\phi + \vec\psi)$ and $\vec q = \frac{1}{2}(\vec\phi - \vec\psi)$, and then to the twisted sum coordinate
$$\vec w := \frac{1}{2}(\mathsf D^{\mathsf T}\vec\phi + \mathsf D\vec\psi) = \vec u + E\vec q \implies \begin{cases} \vec\phi = \vec u + \vec q = \vec w + \mathsf D\vec q, \\ \vec\psi = \vec u - \vec q = \vec w - \mathsf D^{\mathsf T}\vec q. \end{cases} \tag{A.9}$$
Up to the total time derivative $\frac{d}{dt}\big(\frac{1}{2}|\vec u|^2 - \frac{1}{2}|\vec q|^2 - \vec u\cdot\vec q + \vec u\cdot E\vec q\big)$, the defect Lagrangian (A.1) in $(\vec w, \vec q, \vec\lambda)$ coordinates is simply
$$\mathcal L_d = 2\vec q\cdot\dot{\vec w} + 2\vec q\cdot M\dot{\vec\lambda} + \vec\lambda\cdot E_\lambda\dot{\vec\lambda} - \mathcal B_d(\vec w, \vec q, \vec\lambda). \tag{A.10}$$
Notice that in the coordinates $(\vec w, \vec q, \vec\lambda)$, the $2\vec q\cdot E\dot{\vec q}$ term has been completely absorbed into $2\vec q\cdot\dot{\vec w} = 2\vec q\cdot(\dot{\vec u} + E\dot{\vec q})$.
Since $\partial_x\vec\phi = \partial_x\vec u + \partial_x\vec q$ and $\partial_x\vec\psi = \partial_x\vec u - \partial_x\vec q$, the boundary variation of the bulk action is $-\int dt\,(\delta\vec\phi\cdot\partial_x\vec\phi - \delta\vec\psi\cdot\partial_x\vec\psi) = -\int dt\,(2\delta\vec u\cdot\partial_x\vec q + 2\delta\vec q\cdot\partial_x\vec u) = -\int dt\,\big[2\delta\vec w\cdot\partial_x\vec q + 2\delta\vec q\cdot(\partial_x\vec u + E\partial_x\vec q)\big]$.
Varying $S$ with respect to $\vec w, \vec q, \vec\lambda$ gives at $x=0$:
$$\begin{aligned}
\text{(i)}\quad \partial_x\vec q &= -\dot{\vec q} - \frac{1}{2}\nabla_{\vec w}\mathcal B_d, \\
\text{(ii)}\quad \partial_x\vec u + E\partial_x\vec q &= \dot{\vec w} + M\dot{\vec\lambda} - \frac{1}{2}\nabla_{\vec q}\mathcal B_d \iff \partial_x\vec u = \dot{\vec u} + 2E\dot{\vec q} + M\dot{\vec\lambda} + \frac{1}{2}E\nabla_{\vec w}\mathcal B_d - \frac{1}{2}\nabla_{\vec q}\mathcal B_d, \\
\text{(iii)}\quad 0 &= -M^{\mathsf T}\dot{\vec q} + E_\lambda\dot{\vec\lambda} - \frac{1}{2}\nabla_{\vec\lambda}\mathcal B_d.
\end{aligned} \tag{A.11}$$
Now substitute (i), (ii), (iii) into the bulk momentum rate of change $\dot P_- + \dot P_+ = -2\dot{\vec u}\cdot\dot{\vec q} - 2\partial_x\vec u\cdot\partial_x\vec q + U(\vec\phi) - V(\vec\psi)$:
Using $\dot{\vec u} = \dot{\vec w} - E\dot{\vec q}$ and $\partial_x\vec u = \dot{\vec w} + E\dot{\vec q} + M\dot{\vec\lambda} + \frac{1}{2}E\nabla_{\vec w}\mathcal B_d - \frac{1}{2}\nabla_{\vec q}\mathcal B_d$:
$$\begin{aligned}
-2\dot{\vec u}\cdot\dot{\vec q} - 2\partial_x\vec u\cdot\partial_x\vec q &= -2(\dot{\vec w} - E\dot{\vec q})\cdot\dot{\vec q} + 2\left(\dot{\vec w} + E\dot{\vec q} + M\dot{\vec\lambda} + \frac{1}{2}E\nabla_{\vec w}\mathcal B_d - \frac{1}{2}\nabla_{\vec q}\mathcal B_d\right)\cdot\left(\dot{\vec q} + \frac{1}{2}\nabla_{\vec w}\mathcal B_d\right) \\
&= 2\dot{\vec\lambda}\cdot M^{\mathsf T}\dot{\vec q} + \dot{\vec w}\cdot\nabla_{\vec w}\mathcal B_d - \dot{\vec q}\cdot\nabla_{\vec q}\mathcal B_d + M\dot{\vec\lambda}\cdot\nabla_{\vec w}\mathcal B_d - \frac{1}{2}\nabla_{\vec q}\mathcal B_d\cdot\nabla_{\vec w}\mathcal B_d,
\end{aligned}$$
where we used $(E\dot{\vec q})\cdot\dot{\vec q} = 0$, $(E\nabla_{\vec w}\mathcal B_d)\cdot\nabla_{\vec w}\mathcal B_d = 0$, and $(E\dot{\vec q})\cdot\nabla_{\vec w}\mathcal B_d + (E\nabla_{\vec w}\mathcal B_d)\cdot\dot{\vec q} = 0$ by the skew-symmetry $E^{\mathsf T} = -E$!
Substituting $M^{\mathsf T}\dot{\vec q} = E_\lambda\dot{\vec\lambda} - \frac{1}{2}\nabla_{\vec\lambda}\mathcal B_d$ from (iii) and using $\dot{\vec\lambda}\cdot E_\lambda\dot{\vec\lambda} = 0$ gives the **exact identity**
$$\dot P_- + \dot P_+ = \dot{\vec w}\cdot\nabla_{\vec w}\mathcal B_d - \dot{\vec q}\cdot\nabla_{\vec q}\mathcal B_d + \dot{\vec\lambda}\cdot\big(M^{\mathsf T}\nabla_{\vec w}\mathcal B_d - \nabla_{\vec\lambda}\mathcal B_d\big) - \frac{1}{2}\nabla_{\vec w}\mathcal B_d\cdot\nabla_{\vec q}\mathcal B_d + U(\vec w + \mathsf D\vec q) - V(\vec w - \mathsf D^{\mathsf T}\vec q). \tag{A.12}$$
Adding $\dot P_d = \dot{\vec w}\cdot\nabla_{\vec w}P_d + \dot{\vec q}\cdot\nabla_{\vec q}P_d + \dot{\vec\lambda}\cdot\nabla_{\vec\lambda}P_d$ and writing
$$\mathcal B_d = F + G, \qquad P_d = -F + G,$$
equation (A.12) becomes
$$\dot P_- + \dot P_+ + \dot P_d = 2\dot{\vec w}\cdot\nabla_{\vec w}G - 2\dot{\vec q}\cdot\nabla_{\vec q}F + \dot{\vec\lambda}\cdot\big[M^{\mathsf T}\nabla_{\vec w}(F+G) - 2\nabla_{\vec\lambda}F\big] - \frac{1}{2}\nabla_{\vec w}\mathcal B_d\cdot\nabla_{\vec q}\mathcal B_d + U - V = 0, \tag{A.13}$$
which must hold for all velocities satisfying the constraint (iii) $M^{\mathsf T}\dot{\vec q} - E_\lambda\dot{\vec\lambda} = -\frac{1}{2}\nabla_{\vec\lambda}(F+G)$:
- **For Type I ($m=0$, no $\vec\lambda$):** $\dot{\vec w}$ and $\dot{\vec q}$ are completely unconstrained, so their coefficients in (A.13) must vanish identically:
  $$\nabla_{\vec w}G = 0 \implies G = g(\vec q), \qquad \nabla_{\vec q}F = 0 \implies F = f(\vec w),$$
  and the zero-velocity part of (A.13) gives
  $$U(\vec w + \mathsf D\vec q) - V(\vec w - \mathsf D^{\mathsf T}\vec q) = \frac{1}{2}\nabla_{\vec w}f(\vec w)\cdot\nabla_{\vec q}g(\vec q). \tag{A.14}$$
- **For Type II ($m\ge 1$, with $E_\lambda = 0$):** Absorbing $\vec w$ into $\vec{\hat\lambda} = \vec w + M\vec\lambda$ along the range of $M$ (so that $\dot q$ is fixed along $\operatorname{im} M$ by $M^{\mathsf T}\dot{\vec q} = -\frac{1}{2}\nabla_{\vec\lambda}\mathcal B_d$) and defining the characteristic coordinates $\vec w_\pm = \vec w \pm M\vec\lambda$, the vanishing of the coefficients of the independent velocities $\dot{\vec w}$ and $\dot{\vec\lambda}$ gives the 1D wave equations $\nabla_{\vec w}P_d = -\nabla_{M\vec\lambda}\mathcal B_d$ and $\nabla_{M\vec\lambda}P_d = -\nabla_{\vec w}\mathcal B_d$, whose general solution is d'Alembert's formula (A.2):
  $$\mathcal B_d = F(\vec w_+, \vec q) + G(\vec w_-, \vec q), \qquad P_d = -F(\vec w_+, \vec q) + G(\vec w_-, \vec q),$$
  and substituting $M^{\mathsf T}\dot{\vec q} = -\frac{1}{2}\nabla_{\vec\lambda}\mathcal B_d$ into the $-2\dot{\vec q}\cdot\nabla_{\vec q}F$ term of (A.13) yields the exact bilinear identity (A.3).

#### Step A.4: Spatial Bäcklund Property and Spectral Parameter $\sigma$
In light-cone coordinates $x^\pm = \frac{1}{2}(t \pm x)$ ($\partial_\pm = \partial_t \pm \partial_x$, $\square = \partial_+\partial_- = \partial_{tt} - \partial_{xx}$), equations (i) and (ii) of (A.11) read:
$$\partial_+\vec q = -\frac{1}{2}\nabla_{\vec w}\mathcal B_d, \qquad \partial_-\vec w + M\dot{\vec\lambda} = \frac{1}{2}\nabla_{\vec q}\mathcal B_d. \tag{A.15}$$
Applying $\partial_-$ to the first equation and $\partial_+$ to the second (with $\dot{\vec\lambda}$ eliminated via (iii)) and using the potential identity (A.3) gives at $x=0$:
$$\begin{aligned}
\frac{1}{2}(\square\vec\phi - \square\vec\psi) = \partial_-\partial_+\vec q &= -\frac{1}{2}(\nabla_{\vec\phi}U - \nabla_{\vec\psi}V), \\
\frac{1}{2}(\mathsf D^{\mathsf T}\square\vec\phi + \mathsf D\square\vec\psi) = \partial_+\partial_-\vec w &= -\frac{1}{2}(\mathsf D^{\mathsf T}\nabla_{\vec\phi}U + \mathsf D\nabla_{\vec\psi}V).
\end{aligned}$$
Since $\begin{pmatrix} \mathsf I & -\mathsf I \\ \mathsf D^{\mathsf T} & \mathsf D \end{pmatrix}$ has determinant $\det(\mathsf D + \mathsf D^{\mathsf T}) = 2^r \ne 0$, this linear system is invertible, proving that $\square\vec\phi + \nabla_{\vec\phi}U(\vec\phi) = 0 \Longleftrightarrow \square\vec\psi + \nabla_{\vec\psi}V(\vec\psi) = 0$. Finally, a Lorentz boost $\partial_\pm \mapsto \sigma^{\pm 1}\partial_\pm$ leaves the bulk wave equations invariant while rescaling $(F,G) \mapsto (\sigma F, \sigma^{-1}G)$, generating a 1-parameter family of spatial Bäcklund transformations $\mathfrak B_\sigma$. $\blacksquare$

---

## 4. Complete Proof of Theorem B (Classification of All $r$-Component Type-I Defects via Levi-Civita Separation)

### Theorem B (Multi-Component Type-I Integrability Theorem)
*Let $\mathcal L_-$ and $\mathcal L_+$ be $r$-component relativistic scalar field theories ($r\ge 1$) with smooth bulk potentials $U,V \in C^\infty(\mathbb R^r)$ joined at $x=0$ by an irreducible, non-degenerate Type-I defect ($m=0$). If total canonical momentum is conserved on-shell, then (without assuming any exponential ansatz on $U,V,f,g$ in advance):*
1. *(Exponential-polynomial structure)* $U(\vec\phi), V(\vec\psi), f(\vec w), g(\vec q)$ are necessarily finite linear combinations of exponential (or quadratic free-field) modes.
2. *(Root-system classification)* Every irreducible nonlinear component of $U(\vec\phi)$ and $V(\vec\psi)$ is either:
   - for $r=1$: the **sine-Gordon / sinh-Gordon** ($a_1^{(1)}$) potential or the **Liouville** potential;
   - for $r\ge 2$: the **$a_r^{(1)}$ untwisted affine Toda** potential or the **$a_r$ conformal Toda** potential, with defect matrix $\mathsf D = 2(\mathsf I - \pi)^{-1}$ generated by the Coxeter cyclic permutation $\pi$ of the simple roots.
   In all cases, both bulk field theories $\mathcal L_-$ and $\mathcal L_+$ are classically integrable.

---

### Proof of Theorem B

By Theorem A, momentum conservation for a Type-I defect ($m=0$) is equivalent to the functional-differential equation (A.14):
$$U(\vec w + \mathsf D\vec q) - V(\vec w - \mathsf D^{\mathsf T}\vec q) = \sum_{a=1}^r \Phi_a(\vec w)\,\Psi_a(\vec q) \qquad \forall\,\vec w,\vec q \in \mathbb R^r, \tag{B.1}$$
where $\Phi_a(\vec w) := \frac{1}{2}\frac{\partial f}{\partial w_a}(\vec w)$, $\Psi_a(\vec q) := \frac{\partial g}{\partial q_a}(\vec q)$, and $\mathsf D = \mathsf I_r - E$ with $E^{\mathsf T} = -E$.

#### Step B.1: Eliminating the Exponential Ansatz via the Multi-Variable Levi-Civita Theorem
For any vector $\vec\xi \in \mathbb R^r$, define the first-order directional derivative operator in $(\vec w, \vec q)$-space along the fibers $\vec\psi = \vec w - \mathsf D^{\mathsf T}\vec q = \text{const}$:
$$\mathcal D_{\vec\xi}^- := (\mathsf D^{\mathsf T}\vec\xi)\cdot\nabla_{\vec w} + \vec\xi\cdot\nabla_{\vec q}.$$
Since $\mathsf D + \mathsf D^{\mathsf T} = 2\mathsf I_r$, we have
$$\mathcal D_{\vec\xi}^-(\vec w - \mathsf D^{\mathsf T}\vec q) = \mathsf D^{\mathsf T}\vec\xi - \mathsf D^{\mathsf T}\vec\xi = \vec 0, \qquad \mathcal D_{\vec\xi}^-(\vec w + \mathsf D\vec q) = (\mathsf D^{\mathsf T} + \mathsf D)\vec\xi = 2\vec\xi.$$
Applying $\mathcal D_{\vec\xi}^-$ to (B.1) annihilates $V(\vec w - \mathsf D^{\mathsf T}\vec q)$ identically and yields, for each component $c \in \{1,\dots,r\}$ (choosing $\vec\xi = \vec e_c$):
$$2\frac{\partial U}{\partial\phi_c}(\vec w + \mathsf D\vec q) = \sum_{a=1}^r \Big[ (\mathsf D^{\mathsf T}\vec e_c\cdot\nabla_{\vec w}\Phi_a(\vec w))\,\Psi_a(\vec q) + \Phi_a(\vec w)\,\frac{\partial\Psi_a}{\partial q_c}(\vec q) \Big]. \tag{B.2}$$
Since $\mathsf D = \mathsf I_r - E$ is invertible on $\mathbb R^r$, we may set $\vec z := \mathsf D\vec q \in \mathbb R^r$. Equation (B.2) then takes the form of a **finite-rank translation equation** on $\mathbb R^r$:
$$U_c(\vec w + \vec z) := \frac{\partial U}{\partial\phi_c}(\vec w + \vec z) = \sum_{I=1}^{2r} A_{c,I}(\vec w)\,B_{c,I}(\vec z) \qquad \forall\,\vec w,\vec z \in \mathbb R^r. \tag{B.3}$$

**Lemma B.1 (Multi-Variable Levi-Civita Theorem):** *Any smooth function $U_c \in C^\infty(\mathbb R^r)$ satisfying (B.3) is an exponential polynomial $U_c(\vec\phi) = \sum_{j=1}^N P_{c,j}(\vec\phi)\,e^{\vec\alpha_j\cdot\vec\phi}$.*

*Proof of Lemma B.1:* By (B.3), the translation space $\mathcal V_c := \operatorname{span}_{\mathbb C}\{\vec w \mapsto U_c(\vec w + \vec z) : \vec z \in \mathbb R^r\} \subset C^\infty(\mathbb R^r, \mathbb C)$ is contained in $\operatorname{span}_{\mathbb C}\{A_{c,1},\dots,A_{c,2r}\}$ and is therefore finite-dimensional, with $\dim_{\mathbb C}\mathcal V_c = d_c \le 2r$. Since $\mathcal V_c$ is translation-invariant, it is invariant under the commuting partial derivative operators $L_a := \frac{\partial}{\partial w_a}\big|_{\mathcal V_c} \in \operatorname{End}(\mathcal V_c)$ ($a=1,\dots,r$). Choosing a basis $\vec\Upsilon(\vec w) = (\Upsilon_1(\vec w),\dots,\Upsilon_{d_c}(\vec w))^{\mathsf T}$ of $\mathcal V_c$, the commuting linear system $\frac{\partial\vec\Upsilon}{\partial w_a} = L_a\vec\Upsilon$ integrates uniquely to
$$\vec\Upsilon(\vec w) = \exp\!\left(\sum_{a=1}^r w_a L_a\right)\vec\Upsilon(\vec 0).$$
By the simultaneous Jordan–Chevalley decomposition of the commuting matrices $\{L_1,\dots,L_r\}$, the matrix entries of $\exp(\sum_a w_a L_a)$—and hence $U_c(\vec\phi)$ and its integral $U(\vec\phi)$—are exponential polynomials $\sum_j P_j(\vec\phi) e^{\vec\alpha_j\cdot\vec\phi}$. The symmetric operator $\mathcal D_{\vec\eta}^+ := (\mathsf D\vec\eta)\cdot\nabla_{\vec w} - \vec\eta\cdot\nabla_{\vec q}$ proves the identical result for $V(\vec\psi)$, $f(\vec w)$, and $g(\vec q)$. $\square$

#### Step B.2: Exclusion of Non-Constant Polynomial Prefactors for Non-Zero Roots
In $(\vec w, \vec z)$ coordinates with $\vec z = \mathsf D\vec q$, we have $\vec\phi = \vec w + \vec z$ and $\vec\psi = \vec w - \mathsf D^{\mathsf T}\mathsf D^{-1}\vec z = \vec w + \pi\vec z$, where $\pi := -(\mathsf D^{\mathsf T})^{-1}\mathsf D = -(\mathsf I_r + E)^{-1}(\mathsf I_r - E) \in O(r)$. Notice that $\pi$ has **no eigenvalue $+1$** ($\pi\vec\alpha = \vec\alpha \iff -(\mathsf I_r - E)\vec\alpha = (\mathsf I_r + E)\vec\alpha \iff \vec\alpha = \vec 0$).
1. Consequently, for any non-zero root $\vec\alpha \ne \vec 0$ appearing in $U(\vec\phi) = \sum_j P_j(\vec\phi)e^{\vec\alpha_j\cdot\vec\phi}$, the exponential $e^{\vec\alpha\cdot(\vec w + \vec z)} = e^{\vec\alpha\cdot\vec w + \vec\alpha\cdot\vec z}$ is **strictly distinct** from every exponential $e^{\vec\gamma\cdot(\vec w + \pi\vec z)} = e^{\vec\gamma\cdot\vec w + (\pi^{\mathsf T}\vec\gamma)\cdot\vec z}$ appearing in $V(\vec w + \pi\vec z)$ (since equality would require $\vec\gamma = \vec\alpha$ and $\pi^{\mathsf T}\vec\gamma = \vec\alpha$, contradicting $1 \notin \operatorname{spec}(\pi)$).
2. Matching the polynomial prefactor of $e^{\vec\alpha\cdot\vec w + \vec\alpha\cdot\vec z}$ on both sides of (B.1) therefore gives
   $$P_{\vec\alpha}(\vec w + \vec z) = \frac{1}{2}\big(\vec\alpha f_{\vec\alpha}(\vec w) + \nabla_{\vec w}f_{\vec\alpha}(\vec w)\big)\cdot\mathsf D^{\mathsf T}\big(\vec\alpha g_{\vec\alpha}(\vec z) + \nabla_{\vec z}g_{\vec\alpha}(\vec z)\big),$$
   where $f_{\vec\alpha}(\vec w)e^{\vec\alpha\cdot\vec w}$ and $g_{\vec\alpha}(\vec z)e^{\vec\alpha\cdot\vec z}$ are the $\vec\alpha$-modes of $f(\vec w)$ and $\hat g(\vec z) = g(\mathsf D^{-1}\vec z)$.
3. Let $d_1 = \deg f_{\vec\alpha}$ and $d_2 = \deg g_{\vec\alpha}$. Because $\vec\alpha\cdot\mathsf D^{\mathsf T}\vec\alpha = \frac{1}{2}\vec\alpha\cdot(\mathsf D + \mathsf D^{\mathsf T})\vec\alpha = |\vec\alpha|^2 > 0$, the term of highest total degree $d = d_1 + d_2$ on the right-hand side is $\frac{1}{2}|\vec\alpha|^2 f_{\vec\alpha}^{(d_1)}(\vec w)\,g_{\vec\alpha}^{(d_2)}(\vec z)$, which is homogeneous of **pure bi-degree $(d_1, d_2)$** in $(\vec w, \vec z)$. On the left-hand side, the highest-degree homogeneous part $P_{\vec\alpha}^{(d)}(\vec w + \vec z)$ of a non-zero polynomial in $\vec w + \vec z$ contains non-zero terms of bi-degree $(d,0)$ (at $\vec z = \vec 0$) and $(0,d)$ (at $\vec w = \vec 0$). This is impossible unless $d = d_1 = d_2 = 0$. Thus for all $\vec\alpha_j \ne \vec 0$, $P_j, f_{\vec\alpha_j}, g_{\vec\alpha_j}$ are constants:
$$f(\vec w) = \sum_{j=1}^N A_j\,e^{\vec\alpha_j\cdot\vec w}, \qquad g(\vec q) = \hat g(\mathsf D\vec q) = \sum_{k=1}^M B_k\,e^{\vec\beta_k\cdot\mathsf D\vec q}. \tag{B.4}$$

#### Step B.3: Mode Orthogonality and the $a_r^{(1)}$ / $a_r$ Root-System Classification
Substituting (B.4) into (B.1) gives
$$U(\vec w + \mathsf D\vec q) - V(\vec w - \mathsf D^{\mathsf T}\vec q) = \frac{1}{2}\sum_{j=1}^N\sum_{k=1}^M A_j B_k (\vec\alpha_j\cdot\mathsf D^{\mathsf T}\vec\beta_k)\,e^{\vec\alpha_j\cdot\vec w + \vec\beta_k\cdot\mathsf D\vec q}. \tag{B.5}$$
By linear independence of distinct exponentials on $\mathbb R^{2r}$, every pair $(j,k)$ with $\vec\alpha_j\cdot\mathsf D^{\mathsf T}\vec\beta_k \ne 0$ must have an exponent $\vec\alpha_j\cdot\vec w + \vec\beta_k\cdot\mathsf D\vec q$ that is a linear function of **either** $\vec\phi = \vec w + \mathsf D\vec q$ alone **or** $\vec\psi = \vec w - \mathsf D^{\mathsf T}\vec q$ alone:
1. It is a function of $\vec\phi = \vec w + \mathsf D\vec q$ alone if and only if $\vec\beta_k = \vec\alpha_j$.
2. It is a function of $\vec\psi = \vec w - \mathsf D^{\mathsf T}\vec q$ alone if and only if $\mathsf D^{\mathsf T}\vec\beta_k = -\mathsf D\vec\alpha_j$, i.e.
   $$\vec\beta_k = \pi\vec\alpha_j, \qquad \text{where } \pi := -(\mathsf D^{\mathsf T})^{-1}\mathsf D = -(\mathsf I_r + E)^{-1}(\mathsf I_r - E) \in O(r). \tag{B.6}$$
3. For all other pairs $(j,k)$, the coefficient must vanish:
   $$\vec\alpha_j\cdot\mathsf D^{\mathsf T}\vec\beta_k = 0 \qquad \forall\,\vec\beta_k \notin \{\vec\alpha_j, \pi\vec\alpha_j\}. \tag{B.7}$$

Inverting (B.6) gives $\mathsf D = 2(\mathsf I_r - \pi)^{-1}$.
- Because $\pi \in O(r)$ preserves Euclidean lengths ($|\pi\vec\alpha_j| = |\vec\alpha_j|$) and maps each root $\vec\alpha_j$ present in both $U$ and $V$ to another root $\vec\alpha_{\pi(j)} = \pi\vec\alpha_j$ in the finite set $\{\vec\alpha_1,\dots,\vec\alpha_N\}$, $\pi$ decomposes $\{\vec\alpha_j\}$ into disjoint orbits.
- By irreducibility, a single orbit spans $\mathbb R^r$. Since $\pi$ has no fixed vector on $\mathbb R^r$, a closed orbit of $\pi$ spanning $\mathbb R^r$ has length $h = r+1$ with $\sum_{j=0}^r \vec\alpha_j = \vec 0$ and $\pi\vec\alpha_j = \vec\alpha_{j-1 \pmod h}$.
- Using $\mathsf D^{\mathsf T}\vec\alpha_j = -\mathsf D\vec\alpha_{j+1}$ and $\vec\alpha_j\cdot\mathsf D^{\mathsf T}\vec\alpha_j = \frac{1}{2}\vec\alpha_j\cdot(\mathsf D + \mathsf D^{\mathsf T})\vec\alpha_j = |\vec\alpha_j|^2$ (normalized to $|\vec\alpha_j|^2 = 2$), condition (B.7) gives
  $$\vec\alpha_j\cdot\mathsf D\vec\alpha_k = 2\delta_{jk} - 2\delta_{j,k+1 \pmod h},$$
  and therefore the Euclidean inner products of the roots are
  $$\vec\alpha_j\cdot\vec\alpha_k = \frac{1}{2}\vec\alpha_j\cdot(\mathsf D + \mathsf D^{\mathsf T})\vec\alpha_k = \begin{cases} 2\delta_{jk} - 2\delta_{j,k+1} & (h=2,\ r=1:\ a_1^{(1)}\text{ sine/sinh-Gordon}), \\ 2\delta_{jk} - \delta_{j,k+1} - \delta_{j,k-1} & (h=r+1\ge 3:\ a_r^{(1)}\text{ affine Toda}). \end{cases} \tag{B.8}$$
- If the orbit is an open chain $\vec\alpha_1, \dots, \vec\alpha_r$ (where the last mode $\vec\beta_{r+1} = \pi\vec\alpha_r$ appears in $g$ without a companion in $f$), the same inner-product formula gives the simple roots of **$a_r$ conformal Toda** (or **Liouville** for $r=1$). $\blacksquare$

---

## 5. Complete Proof of Theorem C (Classification of Single-Scalar Type-II Defects via Rank-2 Levi-Civita Separation)

### Theorem C (Single-Scalar Type-II Integrability Theorem)
*Let $\mathcal L_-$ and $\mathcal L_+$ be single-scalar ($r=1$) relativistic field theories with smooth potentials $U(\phi), V(\psi)$ joined at $x=0$ by a Type-II defect ($m=1$ auxiliary field $\Lambda(t)$). If total canonical momentum is conserved on-shell, then $U(\phi)$ and $V(\psi)$ must belong to the following exhaustive list of classically integrable potentials (up to affine field shifts and overall scale):*
1. **Free massive or massless scalar:** $U(\phi) = \frac{1}{2}m^2\phi^2$;
2. **Liouville:** $U(\phi) = A e^{\beta\phi}$ (with Liouville or free massless on the other side);
3. **Sine-Gordon / sinh-Gordon ($a_1^{(1)}$):** $U(\phi) = A e^{\beta\phi} + B e^{-\beta\phi}$;
4. **Tzitzéica / Bullough–Dodd ($a_2^{(2)}$):** $U(\phi) = A e^{\beta\phi} + B e^{-\frac{1}{2}\beta\phi}$.

---

### Proof of Theorem C

By Theorem A with $r=1, m=1$ (in the variables $p = \frac{1}{2}(\phi+\psi)$, $q = \frac{1}{2}(\phi-\psi)$, $w_+ = p - \Lambda$, $w_- = \Lambda$ of [38-defect-conditions.qmd](../../part8-defects/38-defect-conditions.qmd#L236-L248), so $w_+ + w_- = p$), momentum conservation is equivalent to the Poisson-bracket functional equation:
$$U(w_+ + w_- + q) - V(w_+ + w_- - q) = F_{w_+}(w_+, q)\,G_q(w_-, q) + F_q(w_+, q)\,G_{w_-}(w_-, q) \qquad \forall\,w_+, w_-, q \in \mathbb R. \tag{C.1}$$

#### Step C.1: Rank-2 Levi-Civita Separation in $(w_+, w_-)$
Fix $q \in \mathbb R$ and define $H_q(w_+ + w_-) := U(w_+ + w_- + q) - V(w_+ + w_- - q)$. As a function of the two independent variables $(w_+, w_-) \in \mathbb R^2$, $H_q(w_+ + w_-)$ is a sum of **at most two products** of a function of $w_+$ and a function of $w_-$:
$$H_q(w_+ + w_-) = \Phi_1(w_+, q)\Psi_1(w_-, q) + \Phi_2(w_+, q)\Psi_2(w_-, q). \tag{C.2}$$
By Lemma B.1 (applied in dimension $1$ to $w_+, w_-$ with separation rank $\le 2$), for every fixed $q$ the space of translates $\{w_+ \mapsto H_q(w_+ + w_-) : w_- \in \mathbb R\}$ has dimension **at most $2$**. Consequently, $H_q(p) = U(p+q) - V(p-q)$ satisfies a second-order constant-coefficient linear ODE in $p$:
$$\left(\frac{\partial}{\partial p} - \alpha\right)\!\left(\frac{\partial}{\partial p} - \beta\right)\big[U(p+q) - V(p-q)\big] = 0, \tag{C.3}$$
where the characteristic roots $\alpha, \beta \in \mathbb C$ are independent of $q$ (since applying $\partial_p - \partial_q$ annihilates $U(p+q)$ and applying $\partial_p + \partial_q$ annihilates $V(p-q)$).
Therefore, **without needing the 15-page Taylor-series determinant expansion of `1807.05747`**, the rank-2 Levi-Civita property of (C.1) immediately forces $U(\phi)$ and $V(\psi)$ to have at most two exponential modes:
- **Degenerate double root $\alpha = \beta = 0$:** $U(\phi) = \frac{1}{2}m^2\phi^2 + c_1\phi + c_0$ (**free massive or massless scalar**).
- **Single non-zero exponential ($\beta = 0$ or one amplitude zero):** $U(\phi) = A e^{\alpha\phi}$, $V(\psi) = B e^{\alpha\psi}$ (**Liouville**, or Liouville coupled to a free massless field when $B=0$).
- **Two distinct non-zero exponentials ($\alpha \ne \beta$, $\alpha,\beta \ne 0$):**
  $$U(\phi) = A_1 e^{\alpha\phi} + A_2 e^{\beta\phi}, \qquad V(\psi) = B_1 e^{\alpha\psi} + B_2 e^{\beta\psi}, \tag{C.4}$$
  and similarly $F(w_+, q)$ and $G(w_-, q)$ have modes $e^{\alpha w_\pm}$ and $e^{\beta w_\pm}$:
  $$F(w_+, q) = \frac{1}{\alpha}f_1(q)\,e^{\alpha w_+} + \frac{1}{\beta}f_2(q)\,e^{\beta w_+}, \qquad G(w_-, q) = \frac{1}{\alpha}g_1(q)\,e^{\alpha w_-} + \frac{1}{\beta}g_2(q)\,e^{\beta w_-}. \tag{C.5}$$

#### Step C.2: Closed-Form First Integrals and Root Ratio $\alpha/\beta \in \{-1, -2, -1/2\}$
Substituting (C.4) and (C.5) into (C.1) expands the right-hand side into exactly four exponential terms in $(w_+, w_-)$:
$$\begin{aligned}
\big(A_1 e^{\alpha q} - B_1 e^{-\alpha q}\big)e^{\alpha p} + \big(A_2 e^{\beta q} - B_2 e^{-\beta q}\big)e^{\beta p} &= \frac{1}{\alpha}(f_1 g_1)'(q)\,e^{\alpha p} + \frac{1}{\beta}(f_2 g_2)'(q)\,e^{\beta p} \\
&\quad + \left(\frac{1}{\beta}f_1 g_2' + \frac{1}{\alpha}f_1' g_2\right) e^{\alpha w_+ + \beta w_-} + \left(\frac{1}{\alpha}f_2 g_1' + \frac{1}{\beta}f_2' g_1\right) e^{\beta w_+ + \alpha w_-}.
\end{aligned} \tag{C.6}$$
Since $\alpha \ne \beta$, the four exponentials $e^{\alpha(w_+ + w_-)}$, $e^{\beta(w_+ + w_-)}$, $e^{\alpha w_+ + \beta w_-}$, and $e^{\beta w_+ + \alpha w_-}$ are linearly independent on $\mathbb R^2$. Equating their coefficients in (C.6) gives four first-order ODEs that **integrate immediately in closed form**:
1. Vanishing of the two mixed exponentials $e^{\alpha w_+ + \beta w_-}$ and $e^{\beta w_+ + \alpha w_-}$ gives
   $$\frac{1}{\beta}f_1 g_2' + \frac{1}{\alpha}f_1' g_2 = 0, \qquad \frac{1}{\alpha}f_2 g_1' + \frac{1}{\beta}f_2' g_1 = 0 \implies \boxed{f_1(q)^\beta\, g_2(q)^\alpha = c_1, \qquad f_2(q)^\alpha\, g_1(q)^\beta = c_2,} \tag{C.7}$$
   where $c_1, c_2$ are constants.
2. Matching the coefficients of $e^{\alpha p}$ and $e^{\beta p}$ integrates to
   $$\boxed{f_1(q)\,g_1(q) = A_1 e^{\alpha q} + B_1 e^{-\alpha q} + D_1, \qquad f_2(q)\,g_2(q) = A_2 e^{\beta q} + B_2 e^{-\beta q} + D_2,} \tag{C.8}$$
   where $D_1, D_2$ are constants of integration.

Comparing (C.7) and (C.8) (for instance when $f_1, g_2$ are non-zero constants as in [38-defect-conditions.qmd](../../part8-defects/38-defect-conditions.qmd#L261-L279), or by taking the ratio $(f_1 g_1)^\beta / (f_2 g_2)^\alpha = (c_1/c_2)(g_1/g_2)^{\alpha+\beta}$) imposes the algebraic identity
$$\big(A_1 e^{\alpha q} + B_1 e^{-\alpha q} + D_1\big)^{-\beta} \propto \big(A_2 e^{\beta q} + B_2 e^{-\beta q} + D_2\big)^{\alpha} \tag{C.9}$$
on the Laurent polynomials in $e^q$. Two non-constant Laurent polynomials $A_1 e^{\alpha q} + B_1 e^{-\alpha q} + D_1$ and $A_2 e^{\beta q} + B_2 e^{-\beta q} + D_2$ with $\alpha \ne \beta$ can have proportional powers for all $q \in \mathbb R$ **if and only if they share the exact same zeros in $q$**, which occurs in only three cases:
- **$\alpha = -\beta$** (with $A_1 = B_2, B_1 = A_2, D_1 = D_2 = 2\cosh 2\tau$): **sine-Gordon / sinh-Gordon ($a_1^{(1)}$)** ([38-defect-conditions.qmd](../../part8-defects/38-defect-conditions.qmd#L261-L264));
- **$\alpha = -2\beta$** (with $D_2 = 0$ and $A_1 e^{-2\beta q} + B_1 e^{2\beta q} + D_1 = (a e^{\beta q} + b e^{-\beta q})^2$, the square of $f_2(q) \propto a e^{\beta q} + b e^{-\beta q}$): **Tzitzéica / Bullough–Dodd ($a_2^{(2)}$)** ([38-defect-conditions.qmd](../../part8-defects/38-defect-conditions.qmd#L276-L279));
- **$\beta = -2\alpha$** (the same as $\alpha = -2\beta$ with $\alpha \leftrightarrow \beta$): **Tzitzéica / Bullough–Dodd ($a_2^{(2)}$)**. $\blacksquare$

> [!TIP]
> **Corollary C.1 (Universal Exponential-Potential Theorem for All Multi-Component Type-II Defects, $r\ge 1, m\ge 1$):**
> For *any* number of scalar components $r \ge 1$ and *any* number of auxiliary defect fields $m \ge 1$, the general Type-II momentum-conservation identity (A.3),
> $$U\!\left(\frac{\vec w_+ + \vec w_-}{2} + \mathsf D\vec q\right) - V\!\left(\frac{\vec w_+ + \vec w_-}{2} - \mathsf D^{\mathsf T}\vec q\right) = \nabla_{\vec w_+}F(\vec w_+, \vec q)\cdot\nabla_{\vec q}G(\vec w_-, \vec q) + \nabla_{\vec q}F(\vec w_+, \vec q)\cdot\nabla_{\vec w_-}G(\vec w_-, \vec q),$$
> has separation rank at most $2r$ between $\vec w_+$ and $\vec w_-$ for every fixed $\vec q \in \mathbb R^r$. By Lemma B.1, **every smooth bulk potential $U(\vec\phi), V(\vec\psi)$ admitting a momentum-conserving Type-I or Type-II defect for any $(r,m)$ is necessarily a finite sum of exponentials $\sum_j A_j e^{\vec\alpha_j\cdot\vec\phi}$ (or a free quadratic potential).**

---

## 6. Theorem D, rescued: what the general framework proves

The earlier Theorem D (Propositions D.1 and D.2, preserved in the [original report](../corrigan_zambon_conjecture_report.md)) claimed a structural proof of Conjecture 2. Its Proposition D.1 is replaced by **Theorem 3.3** of the [general-framework paper](paper.md), which proves the Bäcklund property with weaker hypotheses than D.1 stated. Its Proposition D.2 is replaced by **Theorem 8.1** there, which makes explicit the hypotheses D.2 used tacitly:
- a regular transparent family;
- a closure relation (D.2 had only the Lorentz and NLS cases, and its KdV route gave trivial charges);
- nonresonance for involution, which replaces the unstated Bianchi-permutability input.

The explicit verifications of Section 6.3 of the earlier report are replaced by the case table of Paper, Section 9, and by the checks in [checks/](checks/). That table derives no bulk potential; the selection of $V\propto|u|^4$, $U\propto u^3,u^4$ and the Boussinesq cubic remains Corrigan and Zambon's computation.
