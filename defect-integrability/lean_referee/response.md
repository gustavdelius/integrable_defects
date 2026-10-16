# Author Response to the Second Referee Report (`lean_referee/report.md`)

- **Manuscript:** [`defect-integrability/defect_integrability_paper.md`](../defect_integrability_paper.md) (and companion report [`defect-integrability/corrigan_zambon_conjecture_report.md`](../corrigan_zambon_conjecture_report.md))
- **Referee Report:** [`defect-integrability/lean_referee/report.md`](report.md) (with companion probe files [`Probe.lean`](Probe.lean), [`Probe2.lean`](Probe2.lean), and [`checks.py`](checks.py))
- **Upgraded Lean 4 Formalization:** [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean) (documented in [`lean/README.md`](../../lean/README.md); `lake build` compiles with zero errors, zero warnings, and zero `sorry`s)
- **Date:** 16 October 2026

---

## General Response and Withdrawal of Earlier Overclaim (Recommendation 5)

We thank the referee for a thorough, rigorous, and constructive audit of both the revised manuscript [`defect-integrability/defect_integrability_paper.md`](../defect_integrability_paper.md) and the Lean 4 formalization [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean), as well as for providing the executable counterexample probes [`Probe.lean`](Probe.lean), [`Probe2.lean`](Probe2.lean), and [`checks.py`](checks.py).

First, in accordance with **Recommendation 5**, **we explicitly withdraw the overstatement in [`response_to_referee_theorem_D.md`](../response_to_referee_theorem_D.md) claiming that the initial Lean formalization had ensured that no sign error, unstated hypothesis, or algebraic gap remained in the manuscript.** As the referee's report demonstrates:
1. Two genuine sign errors remained in paper formulas that were not modeled in the initial Lean file:
   - **§D1 (Equation 4.7, second line):** Because $\vec\pi_+^{(x)} = +\frac{\delta S_d}{\delta\vec\psi}$ (whereas $\vec\pi_-^{(x)} = -\frac{\delta S_d}{\delta\vec\phi}$), the gyroscopic terms in the second line of (4.7) must carry $+$ signs ($+\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi$), not $-$ signs.
   - **§D2 (Section 5.2, NLS particle-number current):** For $\mathcal L_- = \frac{i}{2}(\bar u u_t - u\bar u_t) - |u_x|^2 - V(|u|^2)$, the continuity equation $\partial_t\mathcal N + \partial_x\mathcal J_{\mathcal N} = 0$ has flux $\mathcal J_{\mathcal N} = -i(\bar u u_x - u\bar u_x) = +2 T^{01}$ ($c = +2$, not $c = -2$), yielding $\partial_t\mathcal N_d(\sigma) + 2\,\partial_x P_d(\sigma) = 0$.
2. Several mathematical definitions and hypotheses in §§2–5 of the paper needed to be stated and proved more sharply:
   - the strong Lagrangian definition $T\Gamma_d = (T\Gamma_d)^\perp$ (both isotropy and coisotropy) and the proof of coisotropy via non-degeneracy of the canonical pairing (§B2),
   - the Schur-complement mixed Hessian $\widetilde S_{\Phi\Psi} = S_{\Phi\Psi} - S_{\Phi\lambda}S_{\lambda\lambda}^{-1}S_{\lambda\Psi}$ (and its adjoint $\widetilde S_{\Psi\Phi}$) when auxiliary fields $\vec\lambda$ are present (§B4),
   - the distinction between the rapid-decay class as $|t| \to \infty$ and topological kink/soliton sectors (§B1),
   - the off-shell jet domain of the local momentum balance in Theorem 1(1) (§B5),
   - the conditional status of Theorem 2 and the absence of non-constant local Casimirs in Theorem 2(3) (§C4 & §E), and
   - how the pKdV/mKdV/Boussinesq conservation laws in §5.3 follow directly from expanding the spatial momentum potential identity $\partial_x P_d(\sigma) = -(T_-^{01} - T_+^{01})$ of Proposition 4.1 (§E).
3. In the initial Lean file, several definitions were overly simplified (`Int`-linear maps instead of Leibniz derivations, 1D integer scalars in `eq_3_6`, pre-expanded polynomial coefficients in `theorem_2_part_2_first_charge_density`, and unlinked steps in `theorem_1`).

Following **Recommendations 1–5**, we have:
- Fixed both sign errors (§D1 and §D2) and incorporated all mathematical clarifications (§§B, C, E) in [`defect-integrability/defect_integrability_paper.md`](../defect_integrability_paper.md) and [`defect-integrability/corrigan_zambon_conjecture_report.md`](../corrigan_zambon_conjecture_report.md);
- Rebuilt [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean) to implement every structural upgrade in **Recommendation 2** (commuting Leibniz derivations, coisotropy + isotropy over arbitrary configuration spaces, Schur-complement transversality for both `transverse_right` and `transverse_left`, a single connected Theorem 1, derivation of both lines of Equation 4.7, formalization of second-sewing-equation compatibility, inductive derivation of the principal symbol 4.11 from recursion 4.10, explicit quadratic Taylor polynomial `quadTaylor` for 4.12, single-equation chiral Bäcklund compatibility, and the NLS number current with $c = +2$); and
- Updated [`lean/README.md`](../../lean/README.md) (**Recommendation 1**) to state the exact scope of the Lean 4 formalization transparently.

---

## Summary Table of Revisions

| Referee Report Section | Issue Raised in `lean_referee/report.md` | Revision in Paper (`defect_integrability_paper.md`) | Upgrade in Lean (`lean/DefectIntegrability.lean`) |
| :--- | :--- | :--- | :--- |
| **§A1** (`SpaceTimeDerivations` & Lemma 2.1) | `map_mul_c_t` forced `dt` and `dx` to be scalar multiplication by `dt 1`, `dx 1`; `lemma_2_1_first_order` expanded `dt T0_0` by hand; `ostrogradsky_K2_variational_identity` did not apply `dx`. | Lemma 2.1 & Eq. (2.6) unchanged in content. | `SpaceTimeDerivations` now axiomatizes the **Leibniz product rule** `leibniz_t` & `leibniz_x` (deriving `dt 0 = 0`, `dt 1 = 0`, and `map_const_mul_t` as theorems); `lemma_2_1_first_order` and `ostrogradsky_K2_variational_identity` apply `dt` and `dx` via the Leibniz rule. |
| **§A2** (`lemma_2_1_ostrogradsky`) | Assumed `dx H_x = -E_bulk * dx φ - dt Ξ_x` as a hypothesis instead of deriving it from (2.6). | Proof of Lemma 2.1 (lines 98–104). | `lemma_2_1_ostrogradsky` now derives `dx H_x + dt Ξ_x = -E_bulk * dx φ` by specializing `ostrogradsky_K2_variational_identity` to `δφ = dx φ`. |
| **§A3** (Concrete model checks in §4.3 & §5.1) | Free scalar check expanded `dt`/`dx` by hand and assumed `Ψ1 = dx φ - dt φ`; chiral Bäcklund check assumed both first-order equations separately (`Probe.lean`). | §4.3 Example (line 253) and §5.1 (line 270). | `example_free_massive_scalar_Q1_conservation` derives `Ψ1 = dx φ - dt φ` from `-dx φ = -dt φ - Ψ1` and differentiates `Q_1, J_1` via the Leibniz rule; `section_5_1_chiral_backlund_equivalence` uses only the single cross-differentiated compatibility identity `□φ - □ψ = -(U_φ - V_ψ)`. |
| **§B1** (Rapid decay vs periodic/soliton histories) | Rapid decay as $\|t\|\to\infty$ excludes time-periodic and static/kink histories unless boundary constants are adjusted. | §2 (line 56) explicitly notes that topological kinks/solitons approaching distinct vacua as $t\to\pm\infty$ require subtracting the corresponding topological boundary constant. | `proposition_4_1_stress_tensor_potentials` states vacuum-decay injectivity `dt f = 0 → f = 0` explicitly. |
| **§B2** (Isotropy vs Coisotropy in Eq. 3.6 & Lemma 3.1) | `eq_3_6_generating_functional_isotropic` only proved isotropy for 1D `Int` scalars, whereas `lemma_3_1` requires $T\Gamma_d = (T\Gamma_d)^\perp$ (`Probe.lean`). | §3.1 (lines 125–126) and Lemma 3.1 (line 140) define Lagrangian subspaces by $T\Gamma_d = (T\Gamma_d)^\perp$ and prove coisotropy via non-degeneracy of the canonical pairing. | `eq_3_6_generating_functional_lagrangian` proves `IsLagrangianSubspace` (both isotropy and coisotropy) over arbitrary configuration spaces `U_minus, U_plus` with a non-degenerate bilinear pairing. |
| **§B3** (Remark 3.1 Energy Conservation) | `remark_3_1_automatic_energy_conservation` took the time-Legendre identity `dt Ed_0 = -(...)` as an input. | Remark 3.1 (line 130). | Documented in `remark_3_1_automatic_energy_conservation` and `lean/README.md`. |
| **§B4** (Transversality & Auxiliary Fields $\vec\lambda$) | `transverse_of_invertible_mixed_hessian` was 1D, omitted $\vec\lambda$, and only proved `transverse_right`. | §3.1 (line 127) and Theorem 1 (lines 150, 162) introduce the Schur-complement mixed Hessian $\widetilde S_{\Phi\Psi} = S_{\Phi\Psi} - S_{\Phi\lambda}S_{\lambda\lambda}^{-1}S_{\lambda\Psi}$ and its adjoint $\widetilde S_{\Psi\Phi}$. | `schur_complement_transversality` proves **both** `transverse_right` and `transverse_left` over arbitrary configuration spaces `U_minus, U_plus` from left-invertibility of $\widetilde S_{\Phi\Psi}$ and $\widetilde S_{\Psi\Phi}$. |
| **§B5** (Disconnected steps in Theorem 1) | `theorem_1` did not connect the density balance to the integrated differential `dH_minus - dH_plus`, and the domain of (1) needed clarification. | Theorem 1(1) and proof (lines 152, 160–162) clarify the off-shell jet identity on $\Gamma_d$. | `theorem_1_spatial_hamilton_jacobi_and_backlund` connects `(1) ↔ (2a) → (2b) ↔ (3a) → (3b)` in a single theorem using `int_t (dt f) = 0` and `lemma_3_1_symplectic_intertwining`. |
| **§C1** (Compatibility of second sewing equation in Theorem 2) | Lean had no theorem for compatibility of the second equation of (4.7) on bulk solutions. | Step 1 of Theorem 2 (line 240). | Added `theorem_2_second_sewing_compatibility`, proving `Pi_plus_eps = π_plus_ψ_eps` from Theorem 1(3b) and invertibility of the right spatial Legendre transform. |
| **§C2** (Principal symbol 4.11 from recursion 4.10) | `theorem_2_part_1_principal_symbol` assumed `Ψ_lead (k+1) = R (Ψ_lead k)` directly instead of extracting the symbol from the inhomogeneous recursion (4.10). | Step 2 of Theorem 2 (Equation 4.11, lines 243–244). | `theorem_2_part_1_principal_symbol` now takes the inhomogeneous recursion `Ψ (k+1) = H_inv (add_jet (neg_D_dt (Ψ k)) (rem k))` and a symbol map `sym` annihilating `rem k`, proving `sym k (Ψ k) = iterateOp R_sym k (sym 0 (Ψ 0))`. |
| **§C3** (Taylor expansion 4.12) | `theorem_2_part_2_first_charge_density` baked the expanded coefficients into `two_eps_Ed` (`Probe2.lean`). | Step 2 of Theorem 2 (Equation 4.12, lines 247–250). | `theorem_2_part_2_first_charge_density` defines `quadTaylor f0 df d2f δ := 2 * f0 + 2 * df * δ + d2f * (δ * δ)` and evaluates `quadTaylor B_minus_0 dB_minus H (ε * Ψ1 + ε^2 * Ψ2)`, so `H` genuinely comes from `B_-`. |
| **§C4** (Involution & Casimirs in Theorem 2 Part 3) | `h_faithful` assumed absence of non-constant local Casimirs implicitly. | Theorem 2(3) (line 219) and Step 3 (line 257) state the absence of non-constant local Casimirs (`ker X = {0}`) explicitly. | `theorem_2_part_3_involution` names the hypothesis `h_no_casimir` explicitly and derives `vacEval (PB (Q n) (Q m)) = 0` from `evalAtVac (X (Q m)) = zeroVec`. |
| **§C5** (Ostrogradsky $K>1$ in Theorem 2) | Theorem 2 is written in $K=1$ notation while §5.3 has $K=2$. | Step 1 (line 240) and §5.3 (line 283) explain both the Ostrogradsky form and the direct derivation of pKdV/mKdV/Boussinesq conservation laws from $\partial_x P_d = -(T_-^{01} - T_+^{01})$. | Documented in `lean/README.md`. |
| **§D1** (Sign error in second line of Eq. 4.7) | Second line of (4.7) had $-\Omega_{\psi\phi}\partial_t\vec\phi - \Omega_{\psi\psi}\partial_t\vec\psi$ instead of $+\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi$ (`checks.py`). | Fixed in Equation (4.7) (line 229) of `defect_integrability_paper.md` and line 138 of `corrigan_zambon_conjecture_report.md`. | Added `eq_4_7_gyroscopic_euler_lagrange`, deriving both lines of (4.7) from `L_d = A_φ dt φ + A_ψ dt ψ - B`. |
| **§D2** (Sign error in §5.2 NLS number current) | §5.2 had $\mathcal J_{\mathcal N} = +i(\bar u u_x - u\bar u_x) = -2 T^{01}$ ($c=-2$) instead of $-i(\bar u u_x - u\bar u_x) = +2 T^{01}$ ($c=+2$) (`checks.py`). | Fixed in §5.2 (line 276) of `defect_integrability_paper.md` and line 163 of `corrigan_zambon_conjecture_report.md`. | Added `section_5_2_nls_number_current`, proving `dt N + dx J_N = 0` with `J_N = +2 T01` and `dt N_d + 2 dx P_d = 0` from the Leibniz rule. |
| **§E** (Conditional framing of Theorem 2 & §5.3) | §1.2 and §6 should match the conditional framing of Theorem 2 in the Abstract and §1.3; §5.3 should explain how KdV/Boussinesq conservation laws arise. | Updated §1.2 (line 36), §5.3 (line 283), and §6 (line 291) of `defect_integrability_paper.md`. | Documented in `lean/README.md`. |

---

## Detailed Point-by-Point Response

### Section A: Differential Algebra and Lemma 2.1

1. **§A1 (`SpaceTimeDerivations` and `lemma_2_1_first_order` / `ostrogradsky_K2_variational_identity`):**
   - *Referee critique:* In the previous version of [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean), `SpaceTimeDerivations` assumed `map_mul_c_t : dt (c * a) = c * dt a` for all `c, a : Int`, which on `Int` forces `dt a = a * dt 1` (a scalar multiplier rather than a derivation), and `lemma_2_1_first_order` expanded `dt T^0_0` manually instead of applying `dt` to `T^0_0`.
   - *Changes made:*
     - [`SpaceTimeDerivations`](../../lean/DefectIntegrability.lean#L85-L132) now axiomatizes additivity, commutativity (`comm : dt (dx a) = dx (dt a)`), and the **Leibniz product rule**:
       ```lean
       leibniz_t : ∀ a b : Int, dt (a * b) = dt a * b + a * dt b
       leibniz_x : ∀ a b : Int, dx (a * b) = dx a * b + a * dx b
       ```
       From these axioms, `map_zero_t` (`dt 0 = 0`), `map_one_t` (`dt 1 = 0`), and `map_const_mul_t` (`dt c = 0 → dt (c * a) = c * dt a`) are proved as theorems.
     - [`FirstOrderBulkJet.lemma_2_1_first_order`](../../lean/DefectIntegrability.lean#L181-L199) defines `T0_0`, `T1_0`, `T01`, `T1_1`, `T11`, and `eulerLagrange` directly in terms of `dt` and `dx` and proves `dt J.T0_0 + dx J.T1_0 = -J.eulerLagrange * dt J.φ` and `dt J.T01 + dx J.T11 = J.eulerLagrange * dx J.φ` using `hD.leibniz_t`, `hD.leibniz_x'`, `J.chain_t`, `J.chain_x`, and `hD.comm J.φ`.
     - [`ostrogradsky_K2_variational_identity`](../../lean/DefectIntegrability.lean#L208-L227) applies the actual derivation `dx` to the boundary term `π0_x * δφ + π1_x * dx δφ` via `hD.leibniz_x'`.

2. **§A2 (`lemma_2_1_ostrogradsky`):**
   - *Referee critique:* Previously `lemma_2_1_ostrogradsky` took `dx H_x = -E_bulk * dx φ - dt Ξ_x` as a hypothesis instead of deriving it from `ostrogradsky_K2_variational_identity`.
   - *Changes made:* [`lemma_2_1_ostrogradsky`](../../lean/DefectIntegrability.lean#L236-L261) now takes the spatial chain-rule expansion `h_dx_L : dx L = F0 * dx φ + F1 * dx (dx φ) + F2 * dx (dx (dx φ)) + dt Ξ_x`, invokes `ostrogradsky_K2_variational_identity dt dx hD F0 F1 F2 (dx φ) Ξ_x`, and proves `dx H_x + dt Ξ_x = -E_bulk * dx φ` as its first conclusion before deducing `T11 = -H_x - dt Υ1`.

3. **§A3 (Concrete model checks in §4.3 and §5.1):**
   - *Referee critique:* `example_free_massive_scalar_Q1_conservation` expanded derivatives manually and took `Ψ1 = dx φ - dt φ` as a `let` definition rather than deriving it from the $O(\epsilon^0)$ sewing equation; `section_5_1_chiral_backlund_equivalence` assumed two separate equations that forced `□φ + U_φ = 0` and `□ψ + V_ψ = 0` individually (`Probe.lean`).
   - *Changes made:*
     - [`example_free_massive_scalar_Q1_conservation`](../../lean/DefectIntegrability.lean#L1002-L1093) now takes the $O(\epsilon^0)$ sewing equation `h_sew0 : -dx φ = -dt φ - Ψ1`, proves `Ψ1 = dx φ - dt φ`, and applies `dt` and `dx` to `two_Q1 = Ψ1 * Ψ1 + m2 * (φ * φ)` and `two_J1 = Ψ1 * Ψ1 - m2 * (φ * φ)` using `hD.leibniz_t`, `hD.leibniz_x'`, and `hD.comm φ`.
     - [`section_5_1_chiral_backlund_equivalence`](../../lean/DefectIntegrability.lean#L1116-L1120) now takes only the single cross-differentiated compatibility identity `h_compat : box_φ - box_ψ = -(U_φ - V_ψ)` (obtained by eliminating the mixed derivative $\partial_t\partial_x\psi$ between the two chiral defect equations), which leaves `box_φ + U_φ` arbitrary off-shell while proving `box_φ + U_φ = 0 ↔ box_ψ + V_ψ = 0`.

---

### Section B: Section 3 and Theorem 1

1. **§B1 (Rapid decay vs periodic/soliton histories):**
   - *Changes made:* In **§2 (line 56)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md), we added an explicit remark clarifying that while the rapid-decay class $\lim_{|t|\to\infty}(\vec\phi,\vec\psi) = (\vec 0,\vec 0)$ is used throughout the general theorems to fix temporal integration constants uniquely, topological kinks or solitons approaching distinct vacua as $t \to \pm\infty$ require subtracting the corresponding topological boundary constant from the integrated spatial Hamiltonian and stress-tensor potentials.

2. **§B2 (Isotropy vs Coisotropy in Equation 3.6 and Lemma 3.1):**
   - *Referee critique:* `eq_3_6_generating_functional_isotropic` only proved isotropy for 1D `Int` scalars, whereas `lemma_3_1_symplectic_intertwining` requires the strong Lagrangian condition $T\Gamma_d = (T\Gamma_d)^\perp$ (both isotropy and coisotropy), as demonstrated in [`Probe.lean`](Probe.lean).
   - *Changes made:*
     - In **§3.1 (lines 125–126)** and **Lemma 3.1 (line 140)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md), we state the strong Lagrangian definition $T\Gamma_d = (T\Gamma_d)^\perp$ explicitly and include the proof of coisotropy: if $w = ((\delta\vec\Phi, \delta\vec\pi_-^{(x)}), (\delta\vec\Psi, \delta\vec\pi_+^{(x)}))$ is $(\Omega_-^{(x)}\ominus\Omega_+^{(x)})$-orthogonal to $T\Gamma_d$, testing against $(\delta\vec\Phi', \vec 0)$ and $(\vec 0, \delta\vec\Psi')$ and using formal self-adjointness of the second variations of $S_d$ together with non-degeneracy of the canonical pairing forces $w \in T\Gamma_d$.
     - In [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean#L292-L386), [`eq_3_6_generating_functional_lagrangian`](../../lean/DefectIntegrability.lean#L292-L386) proves [`IsLagrangianSubspace`](../../lean/DefectIntegrability.lean#L277-L281) (both coisotropy `.mp` and isotropy `.mpr`) over arbitrary configuration spaces `U_minus, U_plus` equipped with non-degenerate bilinear pairings `pair_minus, pair_plus` and formally self-adjoint second-variation operators `S_ΦΦ, S_ΨΨ, S_ΦΨ, S_ΨΦ`.

3. **§B4 (Schur-Complement Transversality with Auxiliary Fields $\vec\lambda$):**
   - *Referee critique:* When auxiliary fields $\vec\lambda$ are present, eliminating $\delta\vec\lambda$ from the linearized Euler–Lagrange equations replaces $S_{\Phi\Psi}$ by the Schur complement $\widetilde S_{\Phi\Psi} = S_{\Phi\Psi} - S_{\Phi\lambda}S_{\lambda\lambda}^{-1}S_{\lambda\Psi}$; furthermore, `transverse_of_invertible_mixed_hessian` was 1D and only proved `transverse_right`.
   - *Changes made:*
     - In **§3.1 (line 127)** and **Theorem 1 (lines 150, 162)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md), we state the non-degeneracy condition explicitly in terms of invertibility of $S_{\lambda\lambda} = \frac{\delta^2 S_d}{\delta\vec\lambda^2}$ and the Schur-complement mixed Hessian $\widetilde S_{\Phi\Psi} = S_{\Phi\Psi} - S_{\Phi\lambda}S_{\lambda\lambda}^{-1}S_{\lambda\Psi}$ (and its adjoint $\widetilde S_{\Psi\Phi}$).
     - In [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean#L486-L540), [`schur_complement_transversality`](../../lean/DefectIntegrability.lean#L486-L540) proves **both** `transverse_right` and `transverse_left` over arbitrary configuration spaces `U_minus, U_plus` from left-invertibility of `S_tilde_ΦΨ` and `S_tilde_ΨΦ`.

4. **§B5 (Connected Theorem 1 and Domain of the Momentum Balance):**
   - *Changes made:*
     - In **Theorem 1(1) and its proof (lines 152, 160–162)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md), we clarify that the local momentum balance $-T_-^{11} + T_+^{11} + \frac{d P_d}{dt} = 0$ is a formal off-shell jet identity along the unconstrained local parametrization $(\vec\Phi, \vec\Psi)$ of $\Gamma_d$.
     - In [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean#L560-L645), [`theorem_1_spatial_hamilton_jacobi_and_backlund`](../../lean/DefectIntegrability.lean#L560-L645) connects all four parts—the local momentum balance `(1)`, the local density Hamilton–Jacobi identity `(2a)`, the integrated differential Hamilton–Jacobi condition `(2b)` (via `int_t (dt f) = 0`), symplectic tangency `(3a)` (via `lemma_3_1_symplectic_intertwining`), and Bäcklund PDE intertwining `(3b)`—into a single connected theorem.

---

### Section C: Section 4 and Theorem 2

1. **§C1 (Compatibility of the Second Sewing Equation of 4.7):**
   - *Changes made:* Added [`theorem_2_second_sewing_compatibility`](../../lean/DefectIntegrability.lean#L760-L790) in [`lean/DefectIntegrability.lean`](../../lean/DefectIntegrability.lean), which formalizes the exact argument of Step 1: given a solution `ψ_eps` of the first sewing equation of (4.7) and defining `Pi_plus_eps := +δS_d/δψ` so that the trajectory lies in `Γ_d`, Theorem 1(3b) implies that on any solution of the left bulk equation `(dx_φ, dx_π_minus_φ) = X_minus`, the right trajectory satisfies `dx_ψ_eps = X_plus_config ψ_eps Pi_plus_eps`; applying the inverse spatial Legendre transform `h_legendre_inv` yields `Pi_plus_eps = π_plus_ψ_eps`.

2. **§C2 (Derivation of Principal Symbol 4.11 from Recursion 4.10):**
   - *Changes made:* [`theorem_2_part_1_principal_symbol`](../../lean/DefectIntegrability.lean#L804-L822) now takes the inhomogeneous recursion `h_rec_4_10 : ∀ k, Ψ (k + 1) = H_inv (add_jet (neg_D_dt (Ψ k)) (rem k))` and a highest-order symbol map `sym : Nat → Jet → Sym` that annihilates the lower-order remainder `rem k`, proving `sym k (Ψ k) = iterateOp R_sym k (sym 0 (Ψ 0))` by induction on `k`.

3. **§C3 (Quadratic Taylor Expansion 4.12 via `quadTaylor`):**
   - *Referee critique:* In the previous Lean file, `two_eps_Ed` was defined as a pre-expanded polynomial in `ε`, as shown in [`Probe2.lean`](Probe2.lean).
   - *Changes made:* [`theorem_2_part_2_first_charge_density`](../../lean/DefectIntegrability.lean#L882-L959) now defines the explicit quadratic Taylor polynomial function
     ```lean
     def quadTaylor (f0 df d2f δ : Int) : Int :=
       2 * f0 + 2 * df * δ + d2f * (δ * δ)
     ```
     and evaluates `quadTaylor B_minus_0 dB_minus H δ + ε * quadTaylor B0_0 dB0 d2B0 (ε * Ψ1) + (ε * ε) * (2 * B1_0)` on `δ = ε * Ψ1 + (ε * ε) * Ψ2` under `B_minus_0 = 0` and `dB_minus = 0`, proving that the $O(\epsilon^2)$ coefficient is `two_Q1 = H * (Ψ1 * Ψ1) + 2 * dB0 * Ψ1 + 2 * B1_0` where `H` genuinely comes from the second derivative slot of `quadTaylor` applied to `B_-`.

4. **§C4 (Involution and Absence of Local Casimirs in Theorem 2 Part 3):**
   - *Changes made:* In **Theorem 2(3) (line 219)** and **Step 3 (line 257)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md), we state explicitly as a hypothesis of Part 3 that the equal-time Poisson structure has no non-constant local Casimir functionals on the vacuum-normalized charge space ($\ker X = \{0\}$). In [`theorem_2_part_3_involution`](../../lean/DefectIntegrability.lean#L970-L990), `vacEval (PB (Q n) (Q m)) = 0` is derived from `h_pb_vac : vacEval (PB F G) = dF_at_vac F (evalAtVac (X G))` and `h_X_vac : evalAtVac (X (Q m)) = zeroVec`, and combined with `h_no_casimir` to conclude `PB (Q n) (Q m) = zeroCharge`.

---

### Section D: Two Concrete Sign Errors in the Paper (§D1 & §D2, Recommendation 3)

1. **§D1 (Equation 4.7, second line):**
   - *Referee finding:* From $\mathcal L_d = A_\phi\cdot\partial_t\vec\phi + A_\psi\cdot\partial_t\vec\psi - \mathcal B$ with $\Omega_{AB} := \partial_A A_B - \partial_B A_A$, $\frac{\delta S_d}{\delta\vec\psi} = +\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi - \nabla_{\vec\psi}\mathcal B$. Because $\vec\pi_+^{(x)} = +\frac{\delta S_d}{\delta\vec\psi}$, the second line of (4.7) has $+\Omega_{\psi\phi}\partial_t\vec\phi + \Omega_{\psi\psi}\partial_t\vec\psi$.
   - *Correction:* Fixed in **Equation (4.7) (line 229)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md) and **line 138** of [`corrigan_zambon_conjecture_report.md`](../corrigan_zambon_conjecture_report.md), and proved from the chain rule in [`eq_4_7_gyroscopic_euler_lagrange`](../../lean/DefectIntegrability.lean#L708-L735).

2. **§D2 (Section 5.2, NLS particle-number current):**
   - *Referee finding:* For $\mathcal L_- = \frac{i}{2}(\bar u u_t - u\bar u_t) - |u_x|^2 - V(|u|^2)$, $i u_t + u_{xx} - V'(|u|^2)u = 0$ gives $\partial_t(|u|^2) = +\partial_x[i(\bar u u_x - u\bar u_x)]$, so $\partial_t\mathcal N + \partial_x\mathcal J_{\mathcal N} = 0$ has $\mathcal J_{\mathcal N} = -i(\bar u u_x - u\bar u_x) = +2 T^{01}$ ($c = +2$) and $\partial_t\mathcal N_d(\sigma) + 2\,\partial_x P_d(\sigma) = 0$.
   - *Correction:* Fixed in **§5.2 (line 276)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md) and **line 163** of [`corrigan_zambon_conjecture_report.md`](../corrigan_zambon_conjecture_report.md), and proved in [`section_5_2_nls_number_current`](../../lean/DefectIntegrability.lean#L1135-L1182).

---

### Section E: Framing of Theorem 2 and Higher-Derivative Dispersive Models (§5.3)

- **Conditional framing of Theorem 2 in §1.2 and §6:** Updated **§1.2 (line 36)** and **§6 (line 291)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md) so that they state explicitly, in complete agreement with the Abstract, §1.3, and Theorem 2, that Theorem 2 is conditional on the promoted Bäcklund correspondence embedding into a one-parameter family $\Gamma_d(\sigma)$ satisfying Definition 4.1 (and, for Part 3, the equal-time Hamiltonian generator, vacuum vector-field, non-Casimir, and Bianchi permutability hypotheses).
- **Conservation laws in §5.3 (pKdV/mKdV and Boussinesq):** Added an explicit paragraph in **§5.3 (line 283)** of [`defect_integrability_paper.md`](../defect_integrability_paper.md) explaining that in higher-$K$ dispersive models where $\partial_t\psi$ is algebraically eliminated from the Bäcklund relation (such as $p_x + q_x = 2\alpha - \frac{1}{2}(p - q)^2$ in pKdV), the tower of local conservation laws arises directly by expanding the spatial momentum potential identity $\partial_x P_d(\sigma) = -(T_-^{01} - T_+^{01})$ of Proposition 4.1 (together with the temporal momentum balance $\partial_t P_d(\sigma) = T_-^{11} - T_+^{11}$) in inverse powers of the spectral parameter $\alpha$.
