# Author Response to the Referee Reports on *"Momentum-Conserving Defects as Spatial Hamilton–Jacobi Correspondences and the Corrigan–Zambon Integrability Conjecture"*

- **Manuscript:** [`defect-integrability/defect_integrability_paper.md`](defect_integrability_paper.md) (and companion report [`defect-integrability/corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md))
- **First Referee Report:** [`defect-integrability/referee_report_theorem_D.md`](referee_report_theorem_D.md)
- **Second Referee Report (Lean & Paper Audit):** [`defect-integrability/lean_referee/report.md`](lean_referee/report.md)
- **Machine-Checked Formalization:** [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean) (Lean 4 `v4.35.0`, `lake build` passes with zero errors and zero `sorry`s; scope documented in [`lean/README.md`](../lean/README.md))
- **Date:** 16 October 2026

---

## General Response

We thank both referees for thorough, incisive, and mathematically constructive reports:
- In **Part I** below, we respond to the twelve numbered criticisms of the first referee report ([`referee_report_theorem_D.md`](referee_report_theorem_D.md)), which identified sign/convention inconsistencies in the initial draft and places where regularity, boundary-decay, or non-degeneracy hypotheses needed to be stated explicitly.
- In **Part II** below, we respond to the second referee report ([`lean_referee/report.md`](lean_referee/report.md)), which audited both the revised manuscript and the initial Lean 4 formalization. As requested in **Recommendation 5** of [`lean_referee/report.md`](lean_referee/report.md), **we explicitly withdraw the overstatement in the earlier version of this response claiming that the initial Lean formalization had ensured that no sign error, unstated hypothesis, or algebraic gap remained in the paper.** Indeed, the second referee report identified two remaining sign errors in paper formulas that had not been modeled in the initial Lean file (§D1: the gyroscopic signs $+\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi$ in the second line of Equation 4.7; §D2: the NLS number current $\mathcal J_{\mathcal N} = -i(\bar u u_x - u\bar u_x) = +2 T^{01}$ and $\partial_t\mathcal N_d + 2\partial_x P_d = 0$ in §5.2), several places where hypotheses in §§2–5 needed further sharpening (strong Lagrangian definition $T\Gamma_d = (T\Gamma_d)^\perp$ and coisotropy proof, Schur-complement transversality $\widetilde S_{\Phi\Psi} = S_{\Phi\Psi} - S_{\Phi\lambda}S_{\lambda\lambda}^{-1}S_{\lambda\Psi}$ when auxiliary fields $\vec\lambda$ are present, rapid decay vs soliton sectors, off-shell jet domain in Theorem 1(1), conditional status of Theorem 2, and absence of local Casimirs in Theorem 2(3)), and ways in which the initial Lean file used overly simplified abstractions (`Int`-linear maps instead of Leibniz derivations, 1D integer scalars in `eq_3_6`, and pre-expanded polynomial coefficients).
- Following **Recommendations 1–5** of [`lean_referee/report.md`](lean_referee/report.md), we have fixed both sign errors and all mathematical clarifications in [`defect_integrability_paper.md`](defect_integrability_paper.md) and [`corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md), upgraded [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean) to use genuine commuting Leibniz derivations (`leibniz_t`, `leibniz_x`), prove both isotropy and coisotropy (`eq_3_6_generating_functional_lagrangian`), prove Schur-complement transversality (`schur_complement_transversality`), connect Theorem 1 into a single chain, derive both lines of (4.7) (`eq_4_7_gyroscopic_euler_lagrange`), prove second-sewing-equation compatibility (`theorem_2_second_sewing_compatibility`), compute (4.12) via an explicit quadratic Taylor polynomial (`quadTaylor`), and verify the NLS number current (`section_5_2_nls_number_current`), and documented the exact scope of the Lean formalization in [`lean/README.md`](../lean/README.md).

---

# Part I: Response to the First Referee Report (`referee_report_theorem_D.md`)

## Summary Table of Revisions (First Referee Report)

| Referee Item | Issue Identified by Referee | Revision in `defect_integrability_paper.md` | Lean 4 Verification (`lean/DefectIntegrability.lean`) |
| :--- | :--- | :--- | :--- |
| **1. Constrained symmetry defects** | Holonomic multiplier defects $S_d = \int dt\,\lambda(\psi\pm\phi)$ preserve $E$ and $P$ for any (even) non-integrable potential $U(\phi)$ (e.g. $\phi^4$). | §1.1 and §3.1 explicitly restrict to **unconstrained, non-degenerate jump defects** where $(\vec\Phi, \vec\Psi)$ vary independently without holonomic constraints $C(\vec\Phi,\vec\Psi)=0$ and with invertible Schur-complement mixed Hessian $\widetilde S_{\Phi\Psi} = S_{\Phi\Psi} - S_{\Phi\lambda}S_{\lambda\lambda}^{-1}S_{\lambda\Psi}$. | `schur_complement_transversality` |
| **2. Sign conventions** | Sign inconsistencies across Lemma 2.1 ($\mathcal H^{(x)} = +T^{11}$ vs $-T^{11}$), $\Omega^{(x)}$ (2.7), defect balances (3.7)/(3.10)/(4.1), sewing potential signs (4.7), and relativistic $\mathcal H^{(x)}$ (5.1). | Audited and corrected globally across §§2–6: $\mathcal H^{(x)} = \mathcal T^1{}_1 = -T^{11}$ (2.13), $\Omega^{(x)} = \int dt\,\delta\vec\Phi\wedge\delta\vec\pi^{(x)}$ (2.7), $\dot{\mathcal E}_d = \mathcal T_-^1{}_0 - \mathcal T_+^1{}_0$ (3.7), $\dot P_d = T_-^{11} - T_+^{11} = -(\mathcal H_-^{(x)} - \mathcal H_+^{(x)})$ (3.10), $+\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi$ and $-\epsilon^{-1}\nabla_\psi\mathcal B_-$ in $\vec\pi_+^{(x)}$ (4.7), and $\mathcal H^{(x)} = -\frac{1}{2}|\vec\pi^{(x)}|^2 - \frac{1}{2}|\partial_t\vec\phi|^2 + U(\vec\phi)$ (5.1). | `FirstOrderBulkJet.lemma_2_1_first_order`, `lemma_2_1_ostrogradsky`, `remark_3_1_automatic_energy_conservation`, `eq_4_7_gyroscopic_euler_lagrange`, `section_5_1_relativistic_spatial_hamiltonian` |
| **3. Theorem 1 hypotheses** | Needs vacuum normalization $(0,0) \in \Gamma_d$ to pass from $\delta(H_-^{(x)} - H_+^{(x)})|_{T\Gamma_d} = 0$ to $H_-^{(x)} = H_+^{(x)}$, unconstrained local parametrization on $\Gamma_d$, and explicit transversality via invertible mixed Hessian. | Theorem 1 states all hypotheses explicitly: connected Lagrangian $\Gamma_d$ ($T\Gamma_d = (T\Gamma_d)^\perp$) normalized at $(0,0)$, off-shell jet identity for local momentum balance along $\Gamma_d$, and transversality to vertical fibers from invertibility of the Schur-complement mixed Hessian. | `eq_3_6_generating_functional_lagrangian`, `lemma_3_1_symplectic_intertwining`, `schur_complement_transversality`, `theorem_1_spatial_hamilton_jacobi_and_backlund` |
| **4. Mixed jets & formal spatial flow** | Mixed highest spatial derivatives (e.g. $\phi_{xt}^2$) make the spatial Legendre map non-local in $t$, and dispersive PDEs have ill-posed analytic spatial Cauchy problems. | §2 restricts $\mathcal L_\pm$ to depend on the highest spatial derivative $\partial_x^K\vec\phi$ without mixed $t$-derivatives and with $\det\frac{\partial^2\mathcal L}{\partial(\partial_x^K\vec\phi)^2} \ne 0$; §2.1 and Theorem 1(3) formulate $\partial_x$-evolution on the formal jet space. | `ostrogradsky_K2_variational_identity` |
| **5. Proposition 4.1 integration constants** | Periodic $t$-histories and decoupled defect oscillators $\frac{1}{2}\lambda_t^2 - \frac{1}{2}\omega^2\lambda^2$ leave $x$-dependent integration functions $E_{\text{osc}}(x)$ in $\partial_x\mathcal E_d$. | §2, §3.1, and Proposition 4.1 restrict to histories decaying rapidly to the vacuum as $|t| \to \infty$ at every $x$ and exclude decoupled auxiliary oscillators. | `proposition_4_1_stress_tensor_potentials` |
| **6. Spectral parameter & regularity hypotheses** | Boosts move $x=0$ unless applied to the promoted sewing relations; Boussinesq has both $\phi_{xx}$ and $\phi_{xxxx}$; Definition 4.1 and Bianchi permutability are independent hypotheses. | Abstract, §1.3, §4.1, Theorem 2, and §5.3 state Definition 4.1 and Part 3 hypotheses explicitly, clarify that $G_\sigma$ acts on the promoted sewing equations on $\mathbb R^2$, and cite the Boussinesq velocity-shift parameter $\alpha$ of [8, eq. (3.7)]. | `theorem_2_part_2_hierarchy_conservation_laws`, `theorem_2_part_3_involution` |
| **7. Compatibility of the second sewing equation** | Step 1 solves the first equation of (4.7) for $\vec\Psi_n$ and must show why the second equation of (4.7) holds on bulk solutions. | Step 1 gives the explicit proof: on $\Gamma_d(\sigma)$, Theorem 1(3) implies that $(\vec\psi(\epsilon), \vec\Pi_+(\epsilon))$ satisfies Hamilton's $\partial_x$-equation $\partial_x\vec\psi = \delta H_+^{(x)}/\delta\vec\pi_+^{(x)}$, whose inverse Legendre transform is the second equation of (4.7). | `theorem_2_part_1_jet_recursion`, `theorem_2_second_sewing_compatibility` |
| **8. Missing terms in Equation (4.12)** | Omitting $\nabla_\psi\mathcal B_0(\phi,\phi)\cdot\vec\Psi_1 + \mathcal B_1(\phi,\phi)$ in $\mathcal Q_1$ loses the mass term $\frac{1}{2}m^2\phi^2$ in the free massive scalar defect, breaking $\dot Q_1 = 0$. | Equation (4.12) includes the exact $\mathcal B_0$ and $\mathcal B_k$ terms at every order, and the Free Massive Scalar Example explicitly verifies $\mathcal Q_1 = \frac{1}{2}(\phi_x - \phi_t)^2 + \frac{1}{2}m^2\phi^2$. | `theorem_2_part_2_first_charge_density`, `example_free_massive_scalar_Q1_conservation` |
| **9. Principal symbol vs equal-time quotient** | Quotienting equal-time densities by $\partial_t G$ is invalid, and $K = A^{\mathsf T}HA - HA^2 - (A^{\mathsf T})^2 H$ can vanish even when $\det H, \det D \ne 0$. | Removed the invalid $\partial_t$-integration-by-parts claim; Theorem 2(1) and Step 2 (Equation 4.11) prove the exact inductive principal-symbol formula $\vec\Psi_n^{\text{lead}} = (-\mathsf H^{-1}\mathsf D\partial_t)^{n-1}\vec\Psi_1^{\text{lead}}$. | `theorem_2_part_1_principal_symbol`, `principal_symbol_nonzero` |
| **10. Equal-time involution in Step 3** | Spatial canonicity does not by itself imply $\delta_\epsilon F = \{F, Q(\epsilon)\}$ on the equal-time phase space, and $\{q,p\}=1$ shows vacuum vanishing of charges is not enough without $X_{Q(\epsilon)}(0)=0$ and absence of Casimirs. | Theorem 2(3) and Step 3 state the equal-time Hamiltonian generator property $\delta_\epsilon F = \{F, Q(\epsilon)\}$, vanishing of the Hamiltonian vector field at the vacuum, and absence of non-constant local Casimirs as explicit hypotheses of Part 3. | `theorem_2_part_3_involution` |
| **11. Section 5 model checks** | In §5.1, $\Omega_{\phi\phi} + \Omega_{\psi\psi} = 2E \ne 0$ for $a_r^{(1)}$ Toda; Type-II elimination of $\dot\lambda$ produces $\dot q^2$; NLS expands $\mathcal N_d$ rather than $\mathcal E_d$. | Definition 4.1 drops the unnecessary condition $\Omega_{\phi\phi}+\Omega_{\psi\psi}=0$; Step 1 & Step 2 clarify that Type-II defects are expanded on the extended configuration $(\vec\psi,\vec\lambda)$ before eliminating $\dot\lambda$ and that $\mathcal Q_d = \mathcal N_d$ is expanded in (4.12) for NLS. | `section_5_1_relativistic_spatial_hamiltonian`, `section_5_1_chiral_backlund_equivalence`, `section_5_2_nls_number_current` |
| **12. Bibliography entries [6] & [7]** | `arXiv:1807.05747` and `arXiv:2006.14447` had mismatched titles. | Corrected in References [6] and [7] and in `corrigan_zambon_conjecture_report.md`. | N/A (Bibliography) |

---

## Detailed Point-by-Point Response to the First Referee Report

### 1. Exclusion of Holonomic Symmetry-Constraint Defects
> **Referee Comment 1:** *The unrestricted claim admits symmetry defects for arbitrary interactions... Consider identical scalar theories $\mathcal L(u) = \frac{1}{2}u_t^2 - \frac{1}{2}u_x^2 - U(u)$, $U(-u)=U(u)$, with the local defect action $S_d = \int dt\,\lambda(t)(\psi+\phi)$... The construction works for every even potential [including non-integrable $\phi^4$ theory].*

**Author Response:** The referee is completely right. A Lagrange-multiplier action $S_d = \int dt\,\lambda(\psi \pm \phi)$ enforces a holonomic point constraint $\psi = \mp\phi$, which is the graph of a trivial discrete point symmetry $(\phi,\pi) \mapsto (\mp\phi, \mp\pi)$ and preserves energy and momentum for any (even) bulk potential $U(\phi)$ without constraining the bulk dynamics.

**Changes made:**
- In **§1.1** and **§3.1** of [`defect_integrability_paper.md`](defect_integrability_paper.md), we explicitly restrict to **unconstrained, non-degenerate jump defects**: the boundary fields $(\vec\Phi, \vec\Psi)$ are varied independently without holonomic constraints $C(\vec\Phi,\vec\Psi)=0$, every auxiliary variable $\vec\lambda$ has an invertible self-variation operator $S_{\lambda\lambda} := \frac{\delta^2 S_d}{\delta\vec\lambda^2}$, and the **reduced (Schur-complement) mixed Hessian operator**
  $$\widetilde S_{\Phi\Psi} := \frac{\delta^2 S_d}{\delta\vec\Phi\,\delta\vec\Psi} - \frac{\delta^2 S_d}{\delta\vec\Phi\,\delta\vec\lambda}\left(\frac{\delta^2 S_d}{\delta\vec\lambda^2}\right)^{-1}\frac{\delta^2 S_d}{\delta\vec\lambda\,\delta\vec\Psi}$$
  (together with its adjoint $\widetilde S_{\Psi\Phi}$) is invertible.
- In [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean), `schur_complement_transversality` proves over arbitrary configuration spaces `U_minus, U_plus` that left-invertibility of $\widetilde S_{\Phi\Psi}$ and $\widetilde S_{\Psi\Phi}$ implies both `transverse_right` and `transverse_left`.

---

### 2. Audit and Unification of All Sign Conventions
> **Referee Comment 2:** *The basic signs are mutually inconsistent... $\mathcal T^1{}_1 = \mathcal H^{(x)}$, $T^{11} = -\mathcal H^{(x)} = \frac{1}{2}\phi_x^2 + \frac{1}{2}\phi_t^2 - U(\phi)$... With $\Omega = \delta\pi\wedge\delta\Phi$, equations (2.9) imply $\iota_{X_H}\Omega = -\delta H$... Conservation of the totals requires $\dot E_d = \mathcal T_-^1{}_0 - \mathcal T_+^1{}_0$, $\dot P_d = T_-^{11} - T_+^{11}$... Equation (3.4) requires $\pi_- = -F_{\phi b}\dot q^b + B_\phi$, $\pi_+ = F_{\psi b}\dot q^b - B_\psi$.*

**Author Response:** We agree with all six sign corrections pointed out by the first referee, as well as the two additional sign corrections identified by the second referee (§D1 and §D2 of [`lean_referee/report.md`](lean_referee/report.md)).

**Changes made:**
1. **Lemma 2.1 and Equation (2.13):** Derived directly from the variational identity (2.6) and Noether's theorem (2.10), establishing $\mathcal T^1{}_0 = \sum_{m=0}^{K-1}\vec\pi_m^{(x)}\cdot\partial_t\vec\Phi_m + \partial_t\Upsilon_0$ and $\mathcal T^1{}_1 = -T^{11} = \mathcal H^{(x)} + \partial_t\Upsilon_1$.
2. **Spatial symplectic form (Equation 2.7):** Defined $\Omega^{(x)} := -\delta\Theta^{(x)} = \int dt\sum_{m=0}^{K-1}\delta\vec\Phi_m \wedge \delta\vec\pi_m^{(x)}$, compatible with $\partial_x\vec\Phi_m = +\delta H^{(x)}/\delta\vec\pi_m^{(x)}$, $\partial_x\vec\pi_m^{(x)} = -\delta H^{(x)}/\delta\vec\Phi_m$ (2.9) and $\iota_{X_{H^{(x)}}}\Omega^{(x)} = +\delta H^{(x)}$.
3. **Defect energy and momentum balances (Equations 3.7, 3.10, and 4.1):** Corrected to $\frac{d\mathcal E_d}{dt} = \mathcal T_-^1{}_0 - \mathcal T_+^1{}_0$ and $\frac{d P_d}{dt} = T_-^{11} - T_+^{11} = -\big(\mathcal H_-^{(x)} - \mathcal H_+^{(x)}\big) - \frac{d}{dt}(\Upsilon_{1,-} - \Upsilon_{1,+})$.
4. **Sewing equations (Equation 4.7):** Both lines are derived directly from $\mathcal L_d = A_\phi\cdot\partial_t\vec\phi + A_\psi\cdot\partial_t\vec\psi - \mathcal B$ (and verified in `eq_4_7_gyroscopic_euler_lagrange` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean)):
   $$\vec\pi_-^{(x)} = -\frac{\delta S_d}{\delta\vec\phi} = -\Omega_{\phi\phi}\partial_t\vec\phi - \Omega_{\phi\psi}\partial_t\vec\psi + \epsilon^{-1}\nabla_{\vec\phi}\mathcal B_- + \sum_{k\ge 0}\epsilon^k\nabla_{\vec\phi}\mathcal B_k,$$
   $$\vec\pi_+^{(x)} = +\frac{\delta S_d}{\delta\vec\psi} = +\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi - \epsilon^{-1}\nabla_{\vec\psi}\mathcal B_- - \sum_{k\ge 0}\epsilon^k\nabla_{\vec\psi}\mathcal B_k.$$
5. **Relativistic spatial Hamiltonian (Equation 5.1) and NLS number current (§5.2):** Corrected to $\mathcal H_-^{(x)} = -T_-^{11} = -\frac{1}{2}|\vec\pi_-^{(x)}|^2 - \frac{1}{2}|\partial_t\vec\phi|^2 + U(\vec\phi)$ (5.1) and $\mathcal J_{\mathcal N} = -i(\bar u u_x - u\bar u_x) = +2 T^{01}$ ($c = +2$, $\partial_t\mathcal N_d(\sigma) + 2\,\partial_x P_d(\sigma) = 0$) in §5.2 (`section_5_2_nls_number_current`).

---

### 3. Hypotheses of Theorem 1
> **Referee Comment 3:** *Theorem 1 needs stronger hypotheses than its proof supplies... A reference point with equal Hamiltonians, in every component under consideration, is needed to obtain zero... One must prove that the relevant boundary data and variations are realized by local bulk solutions, or assume a formal jet identity... The required transversality or an alternative argument using the full sewing system must be stated and established.*

**Author Response:** All four hypotheses are stated explicitly in **§3.1**, **Lemma 3.1**, and **Theorem 1**:
1. **Strong Lagrangian definition ($T\Gamma_d = (T\Gamma_d)^\perp$) and coisotropy:** §3.1 and Lemma 3.1 define a Lagrangian subspace in the strong sense $T\Gamma_d = (T\Gamma_d)^\perp$ (both isotropic and coisotropic) and prove coisotropy from formal self-adjointness of the second variations of $S_d$ and non-degeneracy of the canonical pairing (`eq_3_6_generating_functional_lagrangian`).
2. **Vacuum normalization on connected components:** Lemma 3.1 and Theorem 1 assume $\Gamma_d$ is a smooth connected Lagrangian correspondence containing the vacuum reference point $(0,0) \in \Gamma_d$ where $H_-^{(x)}(0) = H_+^{(x)}(0) = 0$.
3. **Off-shell formal jet identity on $\Gamma_d$:** Theorem 1(1) formulates $-T_-^{11} + T_+^{11} + \frac{d P_d}{dt} = 0$ as an off-shell formal jet identity along the unconstrained local parametrization $(\vec\Phi, \vec\Psi)$ of $\Gamma_d$ (after substituting (3.4) for $\vec\pi_\pm^{(x)}$ and $\vec\lambda$).
4. **Schur-complement transversality:** Invertibility of $\widetilde S_{\Phi\Psi}$ and $\widetilde S_{\Psi\Phi}$ implies both `transverse_right` and `transverse_left` (`schur_complement_transversality`), and `theorem_1_spatial_hamilton_jacobi_and_backlund` connects all steps $(1) \Longleftrightarrow (2a) \Longrightarrow (2b) \Longleftrightarrow (3a) \Longrightarrow (3b)$ in a single theorem.

---

### 4. Algebraic Spatial Legendre Transform and Formal Spatial Evolution
> **Referee Comment 4:** *Arbitrary mixed jets do not automatically give the claimed local spatial Hamiltonian... The paper must choose between a formal statement and an analytic theorem.*

**Author Response:** **§2** restricts $\mathcal L_\pm$ to depend on its highest spatial derivative $\partial_x^K\vec\phi$ without mixed $t$-derivatives and with $\det\frac{\partial^2\mathcal L}{\partial(\partial_x^K\vec\phi)^2} \ne 0$, and **§2.1** and **Theorem 1(3)** formulate Hamilton's $\partial_x$-equations and Bäcklund intertwining on the formal jet space.

---

### 5. Functions of Integration and Auxiliary Oscillators in Proposition 4.1
> **Referee Comment 5:** *Proposition 4.1 discards functions of integration without justification...*

**Author Response:** **§2**, **§3.1**, and **Proposition 4.1** restrict to smooth histories decaying rapidly to the vacuum $\vec 0$ as $|t| \to \infty$ at every $x$ and exclude decoupled auxiliary oscillators (`proposition_4_1_stress_tensor_potentials`). In **§2**, we also explicitly clarify that topological solitons or kinks approaching distinct vacua as $t \to \pm\infty$ require subtracting the corresponding topological boundary constant.

---

### 6. Status of the Spectral Parameter $\sigma$, Definition 4.1, and Boussinesq
> **Referee Comment 6:** *The parameter family and its regularity are additional assumptions...*

**Author Response:** The **Abstract**, **§1.2**, **§1.3**, **§4.1**, **Theorem 2**, and **§6** explicitly present Theorem 2 as a conditional theorem on one-parameter families $\Gamma_d(\sigma)$ satisfying Definition 4.1, clarify that $G_\sigma$ acts on the promoted sewing equations on $\mathbb R^2$, and explain the Boussinesq parameter $\alpha$ in **§5.3**.

---

### 7. Compatibility of the Second Sewing Equation in Step 1 of Theorem 2
> **Referee Comment 7:** *Lines 243–248 use only the first equation of (4.7). They do not verify the second equation or prove that its residual vanishes for every solution of the left bulk equation.*

**Author Response:** **Step 1 of Theorem 2** proves compatibility of the second equation of (4.7) on solutions of the left bulk equation via Theorem 1(3) and invertibility of the bulk spatial Legendre transform, and this exact argument is formalized as `theorem_2_second_sewing_compatibility` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean).

---

### 8. Exact $O(\epsilon^1)$ Conserved Density Formula (4.12) and Free Massive Scalar Test
> **Referee Comment 8:** *Equation (4.12) omits terms that are necessary even for the first conserved charge...*

**Author Response:** **Theorem 2(2)**, **Equation (4.12)**, and the **Free Massive Scalar Example** include the exact $\mathcal B_0$ and $\mathcal B_k$ contributions at every order, and both `theorem_2_part_2_first_charge_density` (using the explicit quadratic Taylor polynomial `quadTaylor`) and `example_free_massive_scalar_Q1_conservation` (using the Leibniz product rule) are machine-checked in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean).

---

### 9. Principal Symbol Formula vs Equal-Time Integration by Parts
> **Referee Comment 9:** *The charges are integrals over $x$ at fixed $t$...*

**Author Response:** **Theorem 2(1)** and **Step 2 (Equation 4.11)** state and prove the inductive principal-symbol formula $\vec\Psi_n^{\text{lead}} = (-\mathsf H^{-1}\mathsf D\partial_t)^{n-1}\vec\Psi_1^{\text{lead}}$, formalized as `theorem_2_part_1_principal_symbol` and `principal_symbol_nonzero` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean).

---

### 10. Equal-Time Involution Hypotheses in Theorem 2 Part 3
> **Referee Comment 10:** *Line 264 begins by assuming the main missing bridge...*

**Author Response:** **Theorem 2(3)** and **Step 3** state explicitly as hypotheses of Part 3: (i) equal-time Hamiltonian generation $\delta_\epsilon F = \{F, Q(\epsilon)\}$, (ii) vanishing of the Hamiltonian vector fields $X_{Q_n}$ at the vacuum $\vec\phi = \vec 0$, (iii) absence of non-constant local Casimirs on the vacuum-normalized charge space ($\ker X = \{0\}$), and (iv) Bianchi permutability $[X_{Q(\epsilon_1)}, X_{Q(\epsilon_2)}] = 0$. The resulting deduction $\{Q_n, Q_m\} = 0$ is formalized in `theorem_2_part_3_involution`.

---

### 11. Alignment of Section 5 Examples with Definition 4.1 and Theorem 2
> **Referee Comment 11:** *In §5.1, set $M=0$ and use $D = I - E$, $E^T = -E$...*

**Author Response:** Resolved in **Definition 4.1**, **Step 1 & Step 2 of Theorem 2**, and **§§5.1–5.3** (including an explicit explanation in **§5.3** of how the pKdV/mKdV/Boussinesq conservation laws arise directly from expanding the spatial momentum potential identity $\partial_x P_d(\sigma) = -(T_-^{01} - T_+^{01})$ of Proposition 4.1 together with the time-eliminated Bäcklund relation).

---

### 12. Correction of Bibliography Entries [6] and [7]
> **Referee Comment 12:** *Reference [6], arXiv:1807.05747, is Type II defects revisited... Reference [7], arXiv:2006.14447, is Integrable Defects at Junctions within a Network.*

**Author Response:** Corrected in **References [6] and [7]** of [`defect_integrability_paper.md`](defect_integrability_paper.md) and [`corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md).

---

# Part II: Addendum — Response to the Second Referee Report (`lean_referee/report.md`)

We thank the second referee for a meticulous audit of both [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean) and [`defect-integrability/defect_integrability_paper.md`](defect_integrability_paper.md). Below we summarize how every finding and recommendation in [`lean_referee/report.md`](lean_referee/report.md) has been addressed.

## 1. Two Sign Errors Caught in the Paper (§D1 & §D2, Recommendation 3)

1. **§D1 — Second line of Equation (4.7) (Gyroscopic signs in $\vec\pi_+^{(x)}$):**
   - *Issue:* For $\mathcal L_d = A_\phi\cdot\partial_t\vec\phi + A_\psi\cdot\partial_t\vec\psi - \mathcal B$ with $\Omega_{AB} := \partial_A A_B - \partial_B A_A$, the Euler–Lagrange derivative with respect to $\vec\psi$ is $\frac{\delta S_d}{\delta\vec\psi} = +\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi - \nabla_{\vec\psi}\mathcal B$. Because $\vec\pi_+^{(x)} = +\frac{\delta S_d}{\delta\vec\psi}$ (whereas $\vec\pi_-^{(x)} = -\frac{\delta S_d}{\delta\vec\phi}$), the gyroscopic terms in the second line of (4.7) carry $+$ signs, not $-$ signs.
   - *Fix:* Corrected in Equation (4.7) of [`defect_integrability_paper.md`](defect_integrability_paper.md) (line 229) and [`corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md) (line 138), and machine-checked from the chain rule in `eq_4_7_gyroscopic_euler_lagrange` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean).
2. **§D2 — Section 5.2 NLS Number Current Flux Sign ($c = +2$ vs $c = -2$):**
   - *Issue:* For $\mathcal L_- = \frac{i}{2}(\bar u u_t - u\bar u_t) - |u_x|^2 - V(|u|^2)$, the Euler–Lagrange equation $i u_t + u_{xx} - V'(|u|^2)u = 0$ implies $\partial_t(|u|^2) = +\partial_x[i(\bar u u_x - u\bar u_x)]$, so the continuity equation $\partial_t\mathcal N + \partial_x\mathcal J_{\mathcal N} = 0$ has flux $\mathcal J_{\mathcal N} = -i(\bar u u_x - u\bar u_x) = +2 T^{01}$ ($c = +2$) and defect continuity equation $\partial_t\mathcal N_d(\sigma) + 2\,\partial_x P_d(\sigma) = 0$.
   - *Fix:* Corrected in §5.2 of [`defect_integrability_paper.md`](defect_integrability_paper.md) (line 276) and [`corrigan_zambon_conjecture_report.md`](corrigan_zambon_conjecture_report.md) (line 163), and machine-checked from the real and imaginary parts of the NLS equation via the Leibniz product rule in `section_5_2_nls_number_current` in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean).

## 2. Clarifications and Hypotheses in the Paper (§§B, C, E, Recommendation 4)

- **Strong Lagrangian definition ($T\Gamma_d = (T\Gamma_d)^\perp$) and coisotropy proof (§B2):** Added explicitly in §3.1 (Equation 3.6) and Lemma 3.1 of [`defect_integrability_paper.md`](defect_integrability_paper.md), proving that $w \in (T\Gamma_d)^\perp \implies w \in T\Gamma_d$ by testing against $(\delta\vec\Phi, \vec 0)$ and $(\vec 0, \delta\vec\Psi)$ and using non-degeneracy of the canonical pairing.
- **Schur-complement transversality with auxiliary fields $\vec\lambda$ (§B4):** Added in §3.1 and Theorem 1 of [`defect_integrability_paper.md`](defect_integrability_paper.md), showing that eliminating $\delta\vec\lambda = -S_{\lambda\lambda}^{-1}(S_{\lambda\Phi}\delta\vec\Phi + S_{\lambda\Psi}\delta\vec\Psi)$ replaces $S_{\Phi\Psi}$ by the Schur complement $\widetilde S_{\Phi\Psi} = S_{\Phi\Psi} - S_{\Phi\lambda}S_{\lambda\lambda}^{-1}S_{\lambda\Psi}$ (and its adjoint $\widetilde S_{\Psi\Phi}$), whose invertibility gives both `transverse_right` and `transverse_left`.
- **Rapid-decay class vs kink/soliton sectors (§B1):** Clarified in §2 (line 56) of [`defect_integrability_paper.md`](defect_integrability_paper.md).
- **Off-shell jet domain in Theorem 1(1) (§B5):** Stated explicitly in Theorem 1(1) and its proof (lines 152, 160) of [`defect_integrability_paper.md`](defect_integrability_paper.md).
- **Conditional status of Theorem 2 and absence of local Casimirs in Part 3 (§C4 & §E):** Stated explicitly in §1.2 (line 36), Theorem 2(3) (line 219), Step 3 (line 257), and §6 (line 291) of [`defect_integrability_paper.md`](defect_integrability_paper.md).
- **KdV/mKdV/Boussinesq conservation laws (§E):** Explained explicitly in §5.3 (line 283) of [`defect_integrability_paper.md`](defect_integrability_paper.md) via the spatial momentum potential identity $\partial_x P_d(\sigma) = -(T_-^{01} - T_+^{01})$ of Proposition 4.1.

## 3. Upgrades to `lean/DefectIntegrability.lean` (§§A, B, C, Recommendation 2)

Every structural upgrade recommended in **Recommendation 2** of [`lean_referee/report.md`](lean_referee/report.md) has been implemented in [`lean/DefectIntegrability.lean`](../lean/DefectIntegrability.lean):
1. **Commuting Leibniz derivations (`SpaceTimeDerivations`):** Replaced the `Int`-linear `map_mul_c_t` axiom with the genuine **Leibniz product rule** `leibniz_t : dt (a * b) = dt a * b + a * dt b` and `leibniz_x : dx (a * b) = dx a * b + a * dx b`, deriving `dt 0 = 0`, `dt 1 = 0`, and constant-multiple linearity `dt c = 0 → dt (c * a) = c * dt a` as theorems (`map_zero_t`, `map_one_t`, `map_const_mul_t`).
2. **Derivation of Lemma 2.1 and Ostrogradsky (2.6) from the Leibniz rule:** `FirstOrderBulkJet.lemma_2_1_first_order` derives both off-shell Noether identities from the Leibniz rule and `comm`; `ostrogradsky_K2_variational_identity` uses an actual `dx` boundary derivative `dx (π0_x * δφ + π1_x * dx δφ)`; and `lemma_2_1_ostrogradsky` specializes `ostrogradsky_K2_variational_identity` to $\delta\phi = \partial_x\phi$.
3. **Coisotropy and Schur-complement transversality over arbitrary types:** `eq_3_6_generating_functional_lagrangian` proves `IsLagrangianSubspace` (both isotropy and coisotropy) over arbitrary configuration spaces `U_minus, U_plus` with a non-degenerate bilinear pairing, and `schur_complement_transversality` proves both `transverse_right` and `transverse_left` over arbitrary configuration spaces from left-invertibility of $\widetilde S_{\Phi\Psi}$ and $\widetilde S_{\Psi\Phi}$.
4. **Connected Theorem 1:** `theorem_1_spatial_hamilton_jacobi_and_backlund` connects the local momentum balance, the integrated differential Hamilton–Jacobi condition (via `int_t (dt f) = 0`), `lemma_3_1_symplectic_intertwining`, and Bäcklund PDE intertwining in a single connected theorem.
5. **Theorem 2 derivations (4.7, compatibility, 4.11, and `quadTaylor` for 4.12):**
   - `eq_4_7_gyroscopic_euler_lagrange` derives both lines of (4.7) and verifies the $+\Omega_{\psi\phi}\partial_t\phi + \Omega_{\psi\psi}\partial_t\psi$ signs;
   - `theorem_2_second_sewing_compatibility` formalizes the proof that the second sewing equation of (4.7) holds on bulk solutions via Theorem 1(3b) and invertibility of the spatial Legendre transform;
   - `theorem_2_part_1_principal_symbol` derives `sym k (Ψ k) = iterateOp R_sym k (sym 0 (Ψ 0))` by induction from the inhomogeneous recursion (4.10);
   - `theorem_2_part_2_first_charge_density` applies the explicit quadratic Taylor polynomial function `quadTaylor f0 df d2f δ := 2 * f0 + 2 * df * δ + d2f * (δ * δ)` to $\delta = \epsilon\Psi_1 + \epsilon^2\Psi_2$.
6. **Concrete model derivations via the Leibniz rule:** `example_free_massive_scalar_Q1_conservation` derives $\Psi_1 = \phi_x - \phi_t$ from the $O(\epsilon^0)$ sewing equation and uses the Leibniz rule to prove $\partial_t(2\mathcal Q_1) + \partial_x(2\mathcal J_1) = 2(\phi_t - \phi_x)(\phi_{tt} - \phi_{xx} + m^2\phi)$, `section_5_1_chiral_backlund_equivalence` uses only the single cross-differentiated compatibility identity, and `section_5_2_nls_number_current` proves the NLS number current identity with $c = +2$ via the Leibniz rule.
