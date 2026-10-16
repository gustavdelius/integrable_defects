# Author Response to the Referee Report on *"Momentum-Conserving Defects as Spatial Hamilton–Jacobi Correspondences and the Corrigan–Zambon Integrability Conjecture"*

- **Manuscript:** [`defect-integrability/defect_integrability_paper.md`](defect_integrability_paper.md) (and companion report [`defect-integrability/corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md))
- **Referee Report:** [`defect-integrability/referee_report_theorem_D.md`](referee_report_theorem_D.md)
- **Machine-Checked Formalization:** [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean) (Lean 4 `v4.35.0`, `lake build` passes with zero errors and zero `sorry`s)
- **Date:** 16 October 2026

---

## General Response

We thank the referee for a thorough, incisive, and mathematically constructive report. Every one of the twelve numbered criticisms identified either a genuine sign/convention inconsistency in the initial draft or a place where an implicit regularity, boundary-decay, or non-degeneracy hypothesis needed to be made explicit to exclude degenerate counterexamples. In particular, the referee's four concrete test cases:
1. the $\mathbb Z_2$ holonomic symmetry-constraint defect $S_d = \int dt\,\lambda(\psi+\phi)$ for non-integrable $\phi^4$ theory (Comment 1),
2. the decoupled defect oscillator $\mathcal L_d = \mathcal L_d^{\text{base}} + \frac{1}{2}\lambda_t^2 - \frac{1}{2}\omega^2\lambda^2$ on periodic histories (Comment 5),
3. the Bowcock–Corrigan–Zambon free massive scalar defect test for the $O(\epsilon^1)$ charge density $\mathcal Q_1$ (Comment 8), and
4. the $2\times 2$ matrix example $H = I_2$, $D = I_2 + \frac{1}{\sqrt 3}\bigl(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\bigr)$ testing $\partial_t$-integration by parts (Comment 9)

were all verified and directly guided the revision of the manuscript.

To ensure that no sign error, unstated hypothesis, or algebraic gap remains after revision, we have also **formalized and machine-checked all main lemmas, propositions, theorems, and model verifications in Lean 4 (`v4.35.0`)** in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean) (indexed in [`lean/README.md`](../lean/README.md)). Below we respond to the referee's summary assessment and to each of the 12 numbered comments in detail, giving the exact equations and lines in the revised manuscript together with the corresponding Lean 4 theorem names.

---

## Summary Table of Revisions

| Referee Item | Issue Identified by Referee | Revision in `defect_integrability_paper.md` | Lean 4 Verification (`lean/DefectIntegrability.lean`) |
| :--- | :--- | :--- | :--- |
| **1. Constrained symmetry defects** | Holonomic multiplier defects $S_d = \int dt\,\lambda(\psi\pm\phi)$ preserve $E$ and $P$ for any (even) non-integrable potential $U(\phi)$ (e.g. $\phi^4$). | §1.1 (line 15) and §3.1 (lines 120–127) explicitly restrict to **unconstrained, non-degenerate jump defects** where $(\vec\Phi, \vec\Psi)$ vary independently without holonomic constraints $C(\vec\Phi,\vec\Psi)=0$ and with invertible mixed Hessian $\frac{\delta^2 S_d}{\delta\vec\Phi\,\delta\vec\Psi}$. | `transverse_of_invertible_mixed_hessian` |
| **2. Sign conventions** | Six sign inconsistencies across Lemma 2.1 ($\mathcal H^{(x)} = +T^{11}$ vs $-T^{11}$), $\Omega^{(x)}$ (2.7), defect balances (3.7)/(3.10)/(4.1), sewing potential signs (4.7), and relativistic $\mathcal H^{(x)}$ (5.1). | Audited and corrected globally across §§2–6: $\mathcal H^{(x)} = \mathcal T^1{}_1 = -T^{11}$ (2.13), $\Omega^{(x)} = \int dt\,\delta\vec\Phi\wedge\delta\vec\pi^{(x)}$ (2.7), $\dot{\mathcal E}_d = \mathcal T_-^1{}_0 - \mathcal T_+^1{}_0$ (3.7), $\dot P_d = T_-^{11} - T_+^{11} = -(\mathcal H_-^{(x)} - \mathcal H_+^{(x)})$ (3.10), $+\epsilon^{-1}\nabla_\phi\mathcal B_-$ in $\vec\pi_-^{(x)}$ and $-\epsilon^{-1}\nabla_\psi\mathcal B_-$ in $\vec\pi_+^{(x)}$ (4.7), and $\mathcal H^{(x)} = -\frac{1}{2}|\vec\pi^{(x)}|^2 - \frac{1}{2}|\partial_t\vec\phi|^2 + U(\vec\phi)$ (5.1). | `FirstOrderBulkJet.lemma_2_1_first_order`, `lemma_2_1_ostrogradsky`, `remark_3_1_automatic_energy_conservation`, `section_5_1_relativistic_spatial_hamiltonian` |
| **3. Theorem 1 hypotheses** | Needs vacuum normalization $(0,0) \in \Gamma_d$ to pass from $\delta(H_-^{(x)} - H_+^{(x)})|_{T\Gamma_d} = 0$ to $H_-^{(x)} = H_+^{(x)}$, unconstrained local parametrization on $\Gamma_d$, and explicit transversality via invertible mixed Hessian. | Theorem 1 (lines 149–162) states all hypotheses explicitly: connected $\Gamma_d$ normalized at $(0,0)$, local momentum balance along $\Gamma_d$, and transversality to vertical fibers from invertibility of $\frac{\delta^2 S_d}{\delta\vec\Phi\,\delta\vec\Psi}$. | `lemma_3_1_symplectic_intertwining`, `transverse_of_invertible_mixed_hessian`, `theorem_1_spatial_hamilton_jacobi_and_backlund` |
| **4. Mixed jets & formal spatial flow** | Mixed highest spatial derivatives (e.g. $\phi_{xt}^2$) make the spatial Legendre map non-local in $t$, and dispersive PDEs have ill-posed analytic spatial Cauchy problems. | §2 (line 56) restricts $\mathcal L_\pm$ to depend on the highest spatial derivative $\partial_x^K\vec\phi$ without mixed $t$-derivatives and with $\det\frac{\partial^2\mathcal L}{\partial(\partial_x^K\vec\phi)^2} \ne 0$; §2.1 (line 79) and Theorem 1(3) formulate $\partial_x$-evolution on the formal jet space. | `ostrogradsky_K2_variational_identity` |
| **5. Proposition 4.1 integration constants** | Periodic $t$-histories and decoupled defect oscillators $\frac{1}{2}\lambda_t^2 - \frac{1}{2}\omega^2\lambda^2$ leave $x$-dependent integration functions $E_{\text{osc}}(x)$ in $\partial_x\mathcal E_d$. | §2 (line 56), §3.1 (line 120), and Proposition 4.1 (lines 183–195) restrict to histories decaying rapidly to the vacuum as $|t| \to \infty$ at every $x$ and exclude decoupled auxiliary oscillators. | `proposition_4_1_stress_tensor_potentials` |
| **6. Spectral parameter & regularity hypotheses** | Boosts move $x=0$ unless applied to the promoted sewing relations; Boussinesq has both $\phi_{xx}$ and $\phi_{xxxx}$; Definition 4.1 and Bianchi permutability are independent hypotheses. | Abstract (line 5), §1.3 (line 50), §4.1 (line 175), Theorem 2 (lines 212–219), and §5.3 (line 279) state Definition 4.1 and Part 3 hypotheses explicitly, clarify that $G_\sigma$ acts on the promoted sewing equations on $\mathbb R^2$, and cite the Boussinesq velocity-shift parameter $\alpha$ of [8, eq. (3.7)]. | `theorem_2_part_2_hierarchy_conservation_laws`, `theorem_2_part_3_involution` |
| **7. Compatibility of the second sewing equation** | Step 1 solves the first equation of (4.7) for $\vec\Psi_n$ and must show why the second equation of (4.7) holds on bulk solutions. | Step 1 (line 240) gives the explicit proof: on $\Gamma_d(\sigma)$, Theorem 1(3) implies that $(\vec\psi(\epsilon), \vec\Pi_+(\epsilon))$ satisfies Hamilton's $\partial_x$-equation $\partial_x\vec\psi = \delta H_+^{(x)}/\delta\vec\pi_+^{(x)}$, whose inverse Legendre transform is the second equation of (4.7). | `theorem_2_part_1_jet_recursion`, `theorem_1_spatial_hamilton_jacobi_and_backlund` |
| **8. Missing terms in Equation (4.12)** | Omitting $\nabla_\psi\mathcal B_0(\phi,\phi)\cdot\vec\Psi_1 + \mathcal B_1(\phi,\phi)$ in $\mathcal Q_1$ loses the mass term $\frac{1}{2}m^2\phi^2$ in the free massive scalar defect, breaking $\dot Q_1 = 0$. | Equation (4.12) (lines 247–250) includes the exact $\mathcal B_0$ and $\mathcal B_k$ terms at every order, and the Free Massive Scalar Example (line 253) explicitly verifies $\mathcal Q_1 = \frac{1}{2}(\phi_x - \phi_t)^2 + \frac{1}{2}m^2\phi^2$. | `theorem_2_part_2_first_charge_density`, `example_free_massive_scalar_Q1_conservation` |
| **9. Principal symbol vs equal-time quotient** | Quotienting equal-time densities by $\partial_t G$ is invalid, and $K = A^{\mathsf T}HA - HA^2 - (A^{\mathsf T})^2 H$ can vanish even when $\det H, \det D \ne 0$. | Removed the invalid $\partial_t$-integration-by-parts claim; Theorem 2(1) and Step 2 (Equation 4.11) prove the exact inductive principal-symbol formula $\vec\Psi_n^{\text{lead}} = (-\mathsf H^{-1}\mathsf D\partial_t)^{n-1}\vec\Psi_1^{\text{lead}}$. | `theorem_2_part_1_principal_symbol`, `principal_symbol_nonzero` |
| **10. Equal-time involution in Step 3** | Spatial canonicity does not by itself imply $\delta_\epsilon F = \{F, Q(\epsilon)\}$ on the equal-time phase space, and $\{q,p\}=1$ shows vacuum vanishing of charges is not enough without $X_{Q(\epsilon)}(0)=0$. | Theorem 2(3) and Step 3 (lines 219, 255–258) state the equal-time Hamiltonian generator property $\delta_\epsilon F = \{F, Q(\epsilon)\}$ and vanishing of the Hamiltonian vector field at the vacuum as explicit hypotheses of Part 3. | `theorem_2_part_3_involution` |
| **11. Section 5 model checks** | In §5.1, $\Omega_{\phi\phi} + \Omega_{\psi\psi} = 2E \ne 0$ for $a_r^{(1)}$ Toda; Type-II elimination of $\dot\lambda$ produces $\dot q^2$; NLS expands $\mathcal N_d$ rather than $\mathcal E_d$. | Definition 4.1 drops the unnecessary condition $\Omega_{\phi\phi}+\Omega_{\psi\psi}=0$ (so $a_r^{(1)}$ Toda with $E\ne 0$ satisfies Definition 4.1 directly); Step 1 & Step 2 clarify that Type-II defects are expanded on the extended configuration $(\vec\psi,\vec\lambda)$ before eliminating $\dot\lambda$ and that $\mathcal Q_d = \mathcal N_d$ is expanded in (4.12) for NLS. | `section_5_1_relativistic_spatial_hamiltonian`, `section_5_1_chiral_backlund_equivalence` |
| **12. Bibliography entries [6] & [7]** | `arXiv:1807.05747` and `arXiv:2006.14447` had mismatched titles. | Corrected in References [6] and [7] (lines 300–301) and in `corrigan_zambon_conjecture_report.md`. | N/A (Bibliography) |

---

## Detailed Point-by-Point Response

### 1. Exclusion of Holonomic Symmetry-Constraint Defects
> **Referee Comment 1:** *The unrestricted claim admits symmetry defects for arbitrary interactions... Consider identical scalar theories $\mathcal L(u) = \frac{1}{2}u_t^2 - \frac{1}{2}u_x^2 - U(u)$, $U(-u)=U(u)$, with the local defect action $S_d = \int dt\,\lambda(t)(\psi+\phi)$... The construction works for every even potential [including non-integrable $\phi^4$ theory].*

**Author Response:** The referee is completely right. A Lagrange-multiplier action $S_d = \int dt\,\lambda(\psi \pm \phi)$ enforces a holonomic point constraint $\psi = \mp\phi$, which is the graph of a trivial discrete point symmetry $(\phi,\pi) \mapsto (\mp\phi, \mp\pi)$ and preserves energy and momentum for any (even) bulk potential $U(\phi)$ without constraining the bulk dynamics. As the referee notes, this is consistent with Lemma 3.1 (a point symmetry is indeed a canonical transformation intertwining $\mathcal L$ with itself), but it is not a genuine jump defect where $\phi(0,t)$ and $\psi(0,t)$ can vary independently across $x=0$.

**Changes made:**
- In **§1.1 (line 15)** and **§3.1 (lines 120–127)** of [`defect_integrability_paper.md`](defect_integrability_paper.md), we have removed the parenthetical permission of holonomic constraints and explicitly restricted to **unconstrained, non-degenerate jump defects**: the boundary fields $(\vec\Phi, \vec\Psi)$ are varied independently without holonomic constraints $C(\vec\Phi,\vec\Psi)=0$ (explicitly citing the identity constraint $\vec\Psi=\vec\Phi$ and parity constraint $\vec\Psi=-\vec\Phi$ via $\lambda(\psi\pm\phi)$ as excluded degenerate cases), every auxiliary variable $\vec\lambda$ couples non-trivially to $(\vec\Phi,\vec\Psi)$, and the mixed Hessian operator $\frac{\delta^2 S_d}{\delta\vec\Phi\,\delta\vec\Psi}$ is invertible.
- In [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean), `transverse_of_invertible_mixed_hessian` proves that invertibility of the mixed Hessian $S_{\Phi\Psi}$ guarantees transversality of $T\Gamma_d$ to the vertical fibers.

---

### 2. Audit and Unification of All Sign Conventions
> **Referee Comment 2:** *The basic signs are mutually inconsistent... $\mathcal T^1{}_1 = \mathcal H^{(x)}$, $T^{11} = -\mathcal H^{(x)} = \frac{1}{2}\phi_x^2 + \frac{1}{2}\phi_t^2 - U(\phi)$... With $\Omega = \delta\pi\wedge\delta\Phi$, equations (2.9) imply $\iota_{X_H}\Omega = -\delta H$... Conservation of the totals requires $\dot E_d = \mathcal T_-^1{}_0 - \mathcal T_+^1{}_0$, $\dot P_d = T_-^{11} - T_+^{11}$... Equation (3.4) requires $\pi_- = -F_{\phi b}\dot q^b + B_\phi$, $\pi_+ = F_{\psi b}\dot q^b - B_\psi$.*

**Author Response:** We agree with all six sign corrections pointed out by the referee.

**Changes made:**
1. **Lemma 2.1 and Equation (2.13) (lines 94–104):** Derived directly from the variational identity (2.6) and Noether's theorem (2.10), establishing
   $$\mathcal T^1{}_0 = \sum_{m=0}^{K-1}\vec\pi_m^{(x)}\cdot\partial_t\vec\Phi_m + \partial_t\Upsilon_0, \qquad \mathcal T^1{}_1 = -T^{11} = \mathcal H^{(x)} + \partial_t\Upsilon_1,$$
   so that the integrated spatial Hamiltonian is $H^{(x)} = \int dt\,\mathcal H^{(x)} = -\int dt\,T^{11}$.
2. **Spatial symplectic form (Equation 2.7, line 76):** Defined $\Omega^{(x)} := -\delta\Theta^{(x)} = \int dt\sum_{m=0}^{K-1}\delta\vec\Phi_m \wedge \delta\vec\pi_m^{(x)}$, which is compatible with Hamilton's equations $\partial_x\vec\Phi_m = +\delta H^{(x)}/\delta\vec\pi_m^{(x)}$, $\partial_x\vec\pi_m^{(x)} = -\delta H^{(x)}/\delta\vec\Phi_m$ (2.9) and $\iota_{X_{H^{(x)}}}\Omega^{(x)} = +\delta H^{(x)}$ (line 81).
3. **Defect energy and momentum balances (Equations 3.7, 3.10, and 4.1, lines 130, 160, 185–186):** Corrected to
   $$\frac{d\mathcal E_d}{dt} = \mathcal T_-^1{}_0 - \mathcal T_+^1{}_0, \qquad \frac{d P_d}{dt} = T_-^{11} - T_+^{11} = -\big(\mathcal H_-^{(x)} - \mathcal H_+^{(x)}\big) - \frac{d}{dt}(\Upsilon_{1,-} - \Upsilon_{1,+}),$$
   so that $\mathcal H_-^{(x)} - \mathcal H_+^{(x)} = -\frac{d\widetilde P_d}{dt}$ with $\widetilde P_d := P_d + \Upsilon_{1,-} - \Upsilon_{1,+}$.
4. **Sewing equations (Equation 4.7, lines 228–229):** Corrected the potential signs to $+\epsilon^{-1}\nabla_{\vec\phi}\mathcal B_- + \sum_{k\ge 0}\epsilon^k\nabla_{\vec\phi}\mathcal B_k$ in $\vec\pi_-^{(x)}$ and $-\epsilon^{-1}\nabla_{\vec\psi}\mathcal B_- - \sum_{k\ge 0}\epsilon^k\nabla_{\vec\psi}\mathcal B_k$ in $\vec\pi_+^{(x)}$, where $\Omega_{AB} := \partial_A A_B - \partial_B A_A$.
5. **Relativistic spatial Hamiltonian (Equation 5.1, line 268):** Corrected to $\mathcal H_-^{(x)} = -T_-^{11} = -\frac{1}{2}|\vec\pi_-^{(x)}|^2 - \frac{1}{2}|\partial_t\vec\phi|^2 + U(\vec\phi)$ (and similarly $-\pi_u^{(x)}\pi_{\bar u}^{(x)}$ in Equation 5.3 for NLS).
6. **Lean 4 verification:** Every one of these identities is machine-checked in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean) (`FirstOrderBulkJet.lemma_2_1_first_order`, `lemma_2_1_ostrogradsky`, `remark_3_1_automatic_energy_conservation`, `theorem_1_spatial_hamilton_jacobi_and_backlund`, `proposition_4_1_stress_tensor_potentials`, and `section_5_1_relativistic_spatial_hamiltonian`).

---

### 3. Hypotheses of Theorem 1
> **Referee Comment 3:** *Theorem 1 needs stronger hypotheses than its proof supplies... A reference point with equal Hamiltonians, in every component under consideration, is needed to obtain zero... One must prove that the relevant boundary data and variations are realized by local bulk solutions, or assume a formal jet identity... The required transversality or an alternative argument using the full sewing system must be stated and established.*

**Author Response:** We agree with all four points and have incorporated each hypothesis explicitly into the statement and proof of **Theorem 1** (lines 149–162):
1. **Vacuum normalization on connected components:** Lemma 3.1 (line 140) and Theorem 1 (line 150) explicitly state that $\Gamma_d$ is a smooth connected Lagrangian correspondence containing the vacuum reference point $(0,0) \in \Gamma_d$ where $H_-^{(x)}(0) = H_+^{(x)}(0) = 0$.
2. **Domain of the momentum balance:** Theorem 1(1) (line 152) formulates the local momentum balance $-T_-^{11} + T_+^{11} + \frac{d P_d}{dt} = 0$ as a formal jet identity along the unconstrained parametrization of $\Gamma_d$ (after substituting the boundary Euler–Lagrange equations (3.4) for $\vec\pi_\pm^{(x)}$).
3. **Converse null-Lagrangian step:** In the proof of $(2) \Longrightarrow (1)$ (line 161), $\iota^*(H_-^{(x)} - H_+^{(x)}) = 0$ is evaluated on the unconstrained parametrization of $\Gamma_d$, where the standard 1D variational lemma implies that $\mathcal H_-^{(x)} - \mathcal H_+^{(x)}\big|_{\Gamma_d}$ is a total time derivative $-\frac{d\widetilde P_d}{dt}$.
4. **Transversality to vertical fibers:** Standing assumption in §3.1 (line 127) and Theorem 1 (lines 150, 162) requires invertibility of the mixed Hessian $\frac{\delta^2 S_d}{\delta\vec\Phi\,\delta\vec\Psi}$, which implies transversality of $T\Gamma_d$ to the vertical fibers $\{0\}\times T\mathcal P_+^{(x)}$ and $T\mathcal P_-^{(x)}\times\{0\}$. Both the abstract equivalence and the mixed-Hessian transversality lemma are machine-checked in Lean 4 (`theorem_1_spatial_hamilton_jacobi_and_backlund` and `transverse_of_invertible_mixed_hessian`).

---

### 4. Algebraic Spatial Legendre Transform and Formal Spatial Evolution
> **Referee Comment 4:** *Arbitrary mixed jets do not automatically give the claimed local spatial Hamiltonian... Even free Schrödinger evolution, treated as an initial-value problem in $x$, has temporal Fourier modes growing as $\exp(c\sqrt{|\omega|}\,x)$... The paper must choose between a formal statement and an analytic theorem.*

**Author Response:** We agree. In all models studied by Corrigan and Zambon (relativistic scalars, NLS, KdV/mKdV, Boussinesq), the highest spatial derivative $\partial_x^K\vec\phi$ appears without mixed $t$-derivatives and with a non-degenerate algebraic Hessian.

**Changes made:**
- **§2 (line 56)** explicitly assumes that $\mathcal L_\pm$ depends on its highest spatial derivative $\partial_x^K\vec\phi$ without mixed $t$-derivatives and with $\det\frac{\partial^2\mathcal L}{\partial(\partial_x^K\vec\phi)^2} \ne 0$, so that the spatial Ostrogradsky Legendre transform is purely local and algebraic.
- **§2.1 (line 79)** and **Theorem 1(3) (line 156)** formulate Hamilton's $\partial_x$-equations and the Bäcklund intertwining equivalence $\vec{\mathcal E}_-([\vec\phi]) = \vec 0 \Longleftrightarrow \vec{\mathcal E}_+([\vec\psi]) = \vec 0$ on the **formal jet space**, avoiding any claim of analytic well-posedness of the spatial Cauchy problem on $C^\infty(\mathbb R_t)$.

---

### 5. Functions of Integration and Auxiliary Oscillators in Proposition 4.1
> **Referee Comment 5:** *Proposition 4.1 discards functions of integration without justification... Add an independent oscillator to a momentum-conserving defect with a zero-field vacuum: $\mathcal L_d = \mathcal L_d^{\text{base}} + \frac{1}{2}\lambda_t^2 - \frac{1}{2}\omega^2\lambda^2$... These histories are periodic in $t$, as expressly allowed... Thus the asserted spatial energy identity is false for the allowed class.*

**Author Response:** The referee's oscillator counterexample $\lambda(x,t) = a(x)\cos(\omega t)$ on periodic $t$-histories is crystal clear and shows both why periodic $t$-histories cannot be used to eliminate the $x$-dependent integration functions in $\partial_t\big(\partial_x\mathcal E_d + \mathcal T_-^0{}_0 - \mathcal T_+^0{}_0\big) = 0$ and why decoupled defect oscillators must be excluded.

**Changes made:**
- **§2 (line 56)** drops periodic $t$-histories and requires smooth fields decaying rapidly to the vacuum $\vec 0$ as $|t| \to \infty$ (and as $|x| \to \infty$).
- **§3.1 (line 120)** excludes decoupled auxiliary oscillators on the defect (requiring every auxiliary field $\vec\lambda$ to couple non-trivially to $(\vec\Phi,\vec\Psi)$ with unique vacuum $\vec\lambda = \vec 0$ when $\vec\Phi = \vec\Psi = \vec 0$).
- **Proposition 4.1 (lines 183–195)** states the rapid-decay hypothesis $Y(x,t;\sigma) \to \vec 0$ as $|t| \to \infty$ at every $x$ explicitly. Because both the defect densities $(\mathcal E_d, P_d)$ and bulk stress-energy components $(\mathcal T_\pm^0{}_0, T_\pm^{01})$ vanish at the vacuum $Y = \vec 0$, any quantity at fixed $x$ satisfying $\partial_t F(x,t) = 0$ and $\lim_{|t|\to\infty} F(x,t) = 0$ vanishes identically (`proposition_4_1_stress_tensor_potentials` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean)).

---

### 6. Status of the Spectral Parameter $\sigma$, Definition 4.1, and Boussinesq
> **Referee Comment 6:** *The parameter family and its regularity are additional assumptions... A nonzero Lorentz boost sends $x=0$ to a moving worldline... The asserted multiplicative scaling for the Boussinesq model in §5.3 also fails for its fixed coefficients.*

**Author Response:** We agree completely.
1. **Explicit status of Definition 4.1 and Bianchi permutability:** The **Abstract (line 5)**, **§1.3 (line 50)**, **Theorem 2 (lines 212–219)**, and **Conclusion (line 289)** now state explicitly that Theorem 1 holds for a single momentum-conserving jump defect, whereas Theorem 2 applies when the promoted Bäcklund correspondence embeds into a one-parameter spectral family $\Gamma_d(\sigma)$ satisfying the high-spectral-parameter regularity conditions of **Definition 4.1** (and, for Part 3, equal-time Hamiltonian generation and Bianchi permutability).
2. **How bulk symmetries generate $\sigma$:** **§4.1 (line 175)** clarifies that the symmetry group $G_\sigma$ acts on the *already-promoted Bäcklund sewing equations on $\mathbb R^2$* (after Theorem 1 unfreezes the correspondence from $x=0$ to all $x$), producing a one-parameter family of spatial correspondences $\Gamma_d(\sigma)$ at fixed $x$.
3. **Boussinesq spectral parameter:** **§5.3 (line 279)** removes the fixed-coefficient scaling claim for Boussinesq and notes that in Boussinesq the Bäcklund parameter enters via the velocity-shift parameter $\alpha$ of Corrigan and Zambon [8, eq. (3.7)].

---

### 7. Compatibility of the Second Sewing Equation in Step 1 of Theorem 2
> **Referee Comment 7:** *Lines 243–248 use only the first equation of (4.7). They do not verify the second equation or prove that its residual vanishes for every solution of the left bulk equation. Such compatibility might be derivable from an appropriately strengthened Hamilton–Jacobi identity, but it must be proved rather than assumed.*

**Author Response:** We have added the explicit proof in **Step 1 of Theorem 2 (line 240)** and **Appendix A.1 of [`corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md)**:
- For identical bulk theories $\mathcal L_+ = \mathcal L_-$ (auto-Bäcklund family $\Gamma_d(\sigma)$), solving the first equation of (4.7) around $\vec\psi = \vec\phi$ by inverting $\mathsf H(\vec\phi)$ defines a unique formal series $\vec\psi(\epsilon) = \vec\phi + \sum_{n=1}^\infty \epsilon^n\vec\Psi_n([\vec\phi])$.
- Define $\vec\Pi_+(\epsilon) := +\frac{\delta S_d^{(\sigma)}}{\delta\vec\psi}\big(\vec\phi, \vec\psi(\epsilon)\big)$ to be the right-hand side of the second equation of (4.7). By construction, the point $\big(\vec\phi, \vec\pi_-^{(x)}([\vec\phi]), \vec\psi(\epsilon), \vec\Pi_+(\epsilon)\big)$ lies on the Lagrangian correspondence $\Gamma_d(\sigma)$ at every $(x,t)$.
- By Theorem 1(3) (the Bäcklund intertwining property, which follows from the spatial Hamilton–Jacobi equation (3.9)), whenever $\vec\phi$ solves the bulk Euler–Lagrange equation $\vec{\mathcal E}([\vec\phi]) = \vec 0$, the right phase-space trajectory $\big(\vec\psi(\epsilon), \vec\Pi_+(\epsilon)\big)$ satisfies Hamilton's $\partial_x$-equations (2.9) for $H_+^{(x)}$.
- In particular, its first Hamilton equation $\partial_x\vec\psi(\epsilon) = \frac{\delta H_+^{(x)}}{\delta\vec\pi_+^{(x)}}\big(\vec\psi(\epsilon), \vec\Pi_+(\epsilon)\big)$—inverted via the bulk spatial Legendre transform—identifies $\vec\Pi_+(\epsilon) = \vec\pi_+^{(x)}([\vec\psi(\epsilon)])$, which is precisely the second equation of (4.7).
- We also note in line 240 how the recursion applies to the Ostrogradsky coordinates $\vec\Phi, \vec\Psi$ when $K > 1$.

---

### 8. Exact $O(\epsilon^1)$ Conserved Density Formula (4.12) and Free Massive Scalar Test
> **Referee Comment 8:** *Equation (4.12) omits terms that are necessary even for the first conserved charge... After substituting $\psi = \phi + \epsilon\Psi_1 + \cdots$, the coefficient of $\epsilon$ is generally $Q_1 = \frac{1}{2}\Psi_1^T H\Psi_1 + (\partial_\psi B_0)_{\text{diag}}\cdot\Psi_1 + B_1(\phi,\phi)$... A direct test uses two free massive scalars... $Q_1 = \frac{1}{2}(\phi_x - \phi_t)^2 + \frac{1}{2}m^2\phi^2$.*

**Author Response:** We are especially grateful to the referee for this catch and for the explicit free massive scalar calculation. Indeed, in the expansion of $\mathcal E_d(\epsilon) = \epsilon^{-1}\mathcal B_-(\vec\phi,\vec\psi) + \mathcal B_0(\vec\phi,\vec\psi) + \epsilon\mathcal B_1(\vec\phi,\vec\psi) + \cdots$, the subleading potentials $\mathcal B_0$ and $\mathcal B_1$ contribute $\nabla_{\vec\psi}\mathcal B_0(\vec\phi,\vec\phi)\cdot\vec\Psi_1 + \mathcal B_1(\vec\phi,\vec\phi)$ at order $\epsilon^1$, and for the Bowcock–Corrigan–Zambon free massive scalar defect $\mathcal B_1(\phi,\psi) = \frac{m^2}{8}(\phi+\psi)^2$ contributes the mass term $\mathcal B_1(\phi,\phi) = \frac{1}{2}m^2\phi^2$ required for conservation of $Q_1 = \int dx\,\mathcal Q_1 = E + P$.

**Changes made:**
- **Theorem 2(2) (line 218)** and **Equation (4.12) (lines 247–250)** now give the exact expansion including $\mathcal B_0(\vec\phi,\vec\phi)$ at $O(\epsilon^0)$ and $\nabla_{\vec\psi}\mathcal B_0(\vec\phi,\vec\phi)\cdot\vec\Psi_n + \mathcal B_n(\vec\phi,\vec\phi)$ at $O(\epsilon^n)$.
- **Step 2 (line 253)** includes the referee's free massive scalar defect example explicitly in the text.
- **Lean 4 verification:** Both the general expansion formula (`theorem_2_part_2_first_charge_density`) and the exact on-shell conservation law for the free massive scalar defect—including the proof that omitting $\mathcal B_1(\phi,\phi) = \frac{1}{2}m^2\phi^2$ leaves the non-zero residual $-m^2\phi(\phi_t - \phi_x)$ (`example_free_massive_scalar_Q1_conservation`)—are machine-checked in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean).

---

### 9. Principal Symbol Formula vs Equal-Time Integration by Parts
> **Referee Comment 9:** *The charges are integrals over $x$ at fixed $t$. Consequently a density can be changed by $D_x F$ without changing its charge... It cannot generally be changed by $D_t G$... Independently, the matrix $K_m$ in (4.13) is never computed. Its nondegeneracy is asserted from invertibility of $H$ and $D$, which is not a valid matrix inference [counterexample: $H=I_2$, $D = I_2 + \frac{1}{\sqrt 3}J \implies K=0$].*

**Author Response:** The referee's $2\times 2$ counterexample $H = I_2$, $D = I_2 + \frac{1}{\sqrt 3}\bigl(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\bigr)$ (where $\det H = 1$, $\det D = 4/3$, and $A = -D$ satisfies $A^{\mathsf T}A - A^2 - (A^{\mathsf T})^2 = 0$) and the observation that $\int dx\,\partial_t G = \frac{d}{dt}\int dx\,G \ne 0$ for equal-time charges are both completely correct.

**Changes made:**
- In **Theorem 2(1) (line 215)** and **Step 2 (Equation 4.11, lines 243–244)** of [`defect_integrability_paper.md`](defect_integrability_paper.md), we have removed the invalid $\partial_t$-integration-by-parts claim and stated what the recursion (4.10) genuinely proves at the universal level: for every $n \ge 1$, the principal time-derivative symbol of $\vec\Psi_n([\vec\phi])$ is given inductively by
  $$\vec\Psi_n([\vec\phi]) = \big(-\mathsf H(\vec\phi)^{-1}\mathsf D(\vec\phi)\partial_t\big)^{n-1}\vec\Psi_1([\vec\phi]) + \text{(terms of lower }\partial_t\text{-order)},$$
  which is non-vanishing at every order $n$ because $\det\mathsf H \ne 0$ and $\det\mathsf D \ne 0$ (`theorem_2_part_1_principal_symbol` and `principal_symbol_nonzero` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean)), and produces the local conservation laws $\partial_t\mathcal Q_n + \partial_x\mathcal J_n = 0$ via (4.12) (`theorem_2_part_2_hierarchy_conservation_laws`).
- In **Appendix A.2 of [`corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md)**, we also explain how for symmetric/diagonalizable $\mathsf A = -\mathsf H^{-1}\mathsf D$ and on-shell elimination of $\partial_t^2\vec\phi = \partial_x^2\vec\phi + \cdots$ modulo spatial divergences $\partial_x F$, the even orders $Q_{2m+1}$ yield independent equal-time charges of spin $2m+1$.

---

### 10. Equal-Time Involution Hypotheses in Theorem 2 Part 3
> **Referee Comment 10:** *Line 264 begins by assuming the main missing bridge: that the Bäcklund maps are generated by the particular charge series extracted from the defect energy... In addition, the claim that a constant Poisson bracket vanishes because both charges vanish at the vacuum is insufficient by itself: $q$ and $p$ both vanish at the origin, while $\{q,p\}=1$. Vanishing of the relevant Hamiltonian vector fields at the vacuum, or another normalization argument, would suffice.*

**Author Response:** We agree with both points.
- **Theorem 2(3) (line 219)** and **Step 3 (lines 255–258)** now state explicitly as hypotheses of Part 3 that:
  1. the formal auto-Bäcklund transformations $\mathcal A_\epsilon$ are generated on the equal-time phase space by $Q(\epsilon) = \sum_{n=1}^\infty \epsilon^n Q_n$ ($\delta_\epsilon F = \{F, Q(\epsilon)\}$),
  2. the Hamiltonian vector fields $X_{Q_n}$ (and hence the Poisson brackets $\{Q_n, Q_m\}$ of translation-invariant local charges) vanish at the vacuum $\vec\phi = \vec 0$, and
  3. the family satisfies Bianchi permutability $\mathcal A_{\epsilon_1} \circ \mathcal A_{\epsilon_2} = \mathcal A_{\epsilon_2} \circ \mathcal A_{\epsilon_1}$ (so $[X_{Q(\epsilon_1)}, X_{Q(\epsilon_2)}] = 0$).
- Under these explicit hypotheses, the Lie–Poisson homomorphism $X_{\{F,G\}} = [X_F, X_G]$ and faithfulness on vacuum-normalized charges with vanishing vacuum Hamiltonian vector field immediately give $\{Q_n, Q_m\} = 0$ for all $n, m \ge 1$. This deduction is machine-checked in `theorem_2_part_3_involution` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean).

---

### 11. Alignment of Section 5 Examples with Definition 4.1 and Theorem 2
> **Referee Comment 11:** *In §5.1, set $M=0$ and use $D = I - E$, $E^T = -E$. The displayed kinetic term $2q\cdot w_t$, modulo a total derivative, is $\frac{1}{2}\phi^T E\phi_t + \phi^T D\psi_t + \frac{1}{2}\psi^T E\psi_t$. Its two diagonal gyroscopic blocks have the same sign, so their sum is $2E$, not zero when $E\ne 0$... For Type-II defects, eliminating an auxiliary variable need not produce the first-order gyroscopic form (4.3)... In the NLS application the expanded conserved density is $N_d$, whereas Step 2 analyzes the Hessian of the energy potential $B_-$.*

**Author Response:** All three points are well taken and have been resolved in the revised text:
1. **$a_r^{(1)}$ affine Toda and $\Omega_{\phi\phi} = \Omega_{\psi\psi} = E$:** In **Definition 4.1 (lines 203–210)**, we dropped the unnecessary condition $\Omega_{\phi\phi} + \Omega_{\psi\psi} = 0$. In the recursion (4.10) (line 237), a non-zero $\Omega_{\phi\phi} = E$ simply shifts the coefficient of $\partial_t\vec\phi$ in $\vec\Psi_1$ to $-(\Omega_{\phi\phi} + \mathsf D)\partial_t\vec\phi$ without affecting the invertibility of $\mathsf H$ or $\mathsf D$ in the higher-order recursion (4.10)–(4.11). Thus the $a_r^{(1)}$ affine Toda defect with $E^{\mathsf T} = -E \ne 0$ satisfies Definition 4.1 as stated (noted explicitly in **§5.1, line 271**).
2. **Type-II defects:** In **Step 1 (line 240)**, we clarify that for Type-II defects with auxiliary defect fields $\vec\lambda$, Definition 4.1 and the recursion (4.10) apply on the extended defect configuration $(\vec\psi, \vec\lambda)$ where the action is first-order gyroscopic in $(\partial_t\vec\phi, \partial_t\vec\psi, \partial_t\vec\lambda)$, rather than after eliminating $\partial_t\vec\lambda$.
3. **Expansion of $\mathcal N_d(\sigma)$ in NLS:** In **Step 2 (line 245)** and **§5.2 (line 276)**, we explicitly note that when Proposition 4.1 is applied with $\mathcal Q_d(\sigma) = \mathcal N_d(\sigma)$ ($c = -2$ for NLS), one expands $\mathcal N_d\big(\vec\phi, \vec\phi + \vec\Delta; \epsilon\big)$ in powers of $\epsilon$ in (4.12) to obtain the conserved densities $\mathcal Q_n$.

---

### 12. Correction of Bibliography Entries [6] and [7]
> **Referee Comment 12:** *Reference [6], arXiv:1807.05747, is Type II defects revisited, with DOI corresponding to JHEP 09 (2018) 019. Reference [7], arXiv:2006.14447, is Integrable Defects at Junctions within a Network.*

**Author Response:** Corrected in **References [6] and [7] (lines 300–301)** of [`defect_integrability_paper.md`](defect_integrability_paper.md) and throughout [`corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md):
- [6] E. Corrigan and C. Zambon, *Type II defects revisited*, JHEP **09** (2018) 019 (`arXiv:1807.05747`).
- [7] E. Corrigan and C. Zambon, *Integrable defects at junctions within a network*, J. Phys. A: Math. Theor. **53** (2020) 484001 (`arXiv:2006.14447`).
