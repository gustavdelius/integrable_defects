# Second referee report on PR #32: response to `lean_referee/report.md`

- Date: 2026-10-16
- Model: Claude Opus 5.5 (claude-opus-5-5)
- Commit reviewed: `34ed662` (head of `defect-integrability-conjecture`)
- Evidence: `Probe3.lean` in this directory; it compiles. To rerun it from the repository root: `cd lean && lake build && lake env lean ../defect-integrability/lean_referee/Probe3.lean`

## Verdict

The response fixes many points. The two sign errors are fixed, the paper's hypotheses are stated much better, coisotropy is proved, Theorem 1 is now one connected chain, and the Q_1 Taylor expansion is now real. It does not fix everything, though. The change to Leibniz derivations introduced a new defect that is worse than the one it replaced. The new §5.3 argument is mathematically wrong. Several earlier points are still open.

## 1. New defect: the derivation axioms have only the zero model

`SpaceTimeDerivations` now requires additivity and the Leibniz rule on `Int`. On `Int` this forces `dt = dx = 0`: `dt 1 = 0`, and additivity then gives `dt n = 0` for every integer (`Probe3.lean`, `derivs_vanish`). So:

- **`proposition_4_1_stress_tensor_potentials` is vacuous.** Its hypotheses `hD` and `h_vac_norm : ∀ f, dt f = 0 → f = 0` together prove `False`, since `dt 1 = 0` would force `1 = 0` (`prop_4_1_hypotheses_inconsistent`). The theorem therefore proves any conclusion whatever.
- **Every other theorem that takes `hD`** holds only for dt = dx = 0. In that model every statement involving dt or dx reduces to `0 = 0` (and the free-scalar example forces Ψ1 = 0). This covers `lemma_2_1_first_order`, `ostrogradsky_K2_variational_identity`, `lemma_2_1_ostrogradsky`, `example_free_massive_scalar_Q1_conservation` and `section_5_2_nls_number_current`. Their Leibniz-rule computations are correct as symbolic manipulation, but the statements say nothing.

The file's comment claims that, "Unlike `Int`-linear maps (which would degenerate…)", a Leibniz derivation does not degenerate. It degenerates further. **Fix:** make the carrier an arbitrary type with ring operations, given as a structure or type-class hypothesis (still possible without Mathlib), or use Mathlib's `Derivation` over a differential ring.

## 2. New mathematical error: the §5.3 and Theorem 2(2) route through ∂ₓP_d gives only trivial conservation laws

The new §5.3 paragraph and the new parenthesis in Theorem 2(2) claim the hierarchy follows "directly from the second row of (4.1)", by expanding T₋^{01}([φ]) − T₊^{01}([ψ(ε)]) = −∂ₓP_d(ε) in ε. That identity says the density difference is an **exact x-derivative**. Every ε^n coefficient of T^{01}([ψ(ε)]) − T^{01}([φ]) is then ∂ₓ of a local function, so the corresponding charge vanishes identically on decaying fields: ∫(T₋^{01} − T₊^{01}) dx = −[P_d] from −∞ to +∞ = 0. The second row of (4.1) only yields the tautology ∂ₜ(∂ₓP_d) − ∂ₓ(∂ₜP_d) = 0.

The Gardner/Miura conserved densities for KdV come from a different density, such as w = φ − ψ, whose t-equation from the Bäcklund transformation is in conservation form. They do not come from T^{01}. So the KdV, mKdV and Boussinesq gap I raised in §E is still open. The new text should be removed or replaced by an argument that names a nontrivial density for each model.

## 3. Status of my earlier points

| Item in `report.md` | Status |
|---|---|
| D1 sign of (4.7), line 2 | **Fixed** in the paper. `eq_4_7_gyroscopic_euler_lagrange` checks it, but only for a single field (r = 1), where Ω_φφ = Ω_ψψ = 0 by definition. |
| D2 NLS current, c = +2 | **Fixed** in the paper. The Lean check sits in the zero-derivation model (§1). |
| B1 strong Lagrangian / coisotropy | **Fixed.** `eq_3_6_generating_functional_lagrangian` is a genuine proof over abstract spaces. With λ, the paper relies on S_λλ being invertible and self-adjoint; the Lean has no λ. |
| B2 decay class | **Fixed in the paper** (kinks, breathers and soliton-adding partners are now excluded explicitly). **Made worse in the Lean** (§1). |
| B3 involution hypotheses | **Mostly fixed.** "No Casimirs" is now explicit in the paper and in the Lean. The step from commuting finite maps A_ε to [X_{Q_n}, X_{Q_m}] = 0 is still asserted in a parenthesis ("so …"), not proved. |
| B4 Schur-complement transversality | **Fixed in the paper.** The Lean proves transversality from given S̃ operators but does not derive S̃ from λ elimination. Its conclusion is not plugged into Theorem 1, which still takes `TransverseLinearCorrespondence` and `IsLagrangianSubspace` as hypotheses; the coisotropy theorem is not plugged in either. |
| B5 off-shell balance | **Fixed** in the paper. |
| B6 `Int` carrier | **Worse** (§1). |
| C1 general Lemma 2.1 | **Open.** `lemma_2_1_ostrogradsky` still takes `h_T1_1 : T1_1 = H_x + dt Υ1`, which is (2.13) itself. The new first conclusion concerns H_x only, not the Noether tensor. (The response describes this item as a different hypothesis, which I never raised.) |
| C2 (2.9) Hamilton ⇔ Euler–Lagrange | **Open.** Not formalized. |
| C3 (2)⇒(1) with λ | **Addressed** by stating an assumption in the paper. The Lean no longer contains any (2)⇒(1) direction. |
| C4 Theorem 1 chain | **Fixed** at the linearized level. |
| C5 Taylor expansion and recursion | Q_1: **fixed** (`quadTaylor`). Principal symbol: **open**. The induction step is now the hypothesis `h_sym_step`, quantified over all u, which is again the claim to be proved. Second sewing equation: **formalized as a corollary** of an assumed Theorem 1(3b). Triangularity: open. |
| C6 nontriviality / integrability | **Partly.** The paper now says "Conditional". But the new parenthesis in Theorem 2(2) ("non-trivial, linearly independent … whenever … non-vanishing") overclaims: nonvanishing modulo divergences gives nontriviality of each charge, not linear independence. |
| E §5.3 flux hypothesis | **Not fixed.** The new text is wrong (§2). |
| E reference [1] and "injective" | **Fixed.** |
| Rec. 1 README scope | **Fixed** in tone. But the README still describes the derivation axioms as a faithful model (§1). |
| Rec. 2 `first_charge_density` | **Fixed.** |
| Rec. 5 withdraw overclaim | **Partly.** The withdrawal is in `lean_referee/response.md`. But `response_to_referee_theorem_D.md` line 20 still says the Lean ensures "no sign error, unstated hypothesis, or algebraic gap remains". |

## 4. Out-of-step documents

- **PR description.** It still says "complete … formalization" and "Theorem D (proving Conjecture 2 in full generality)".
- **Companion report** (`corrigan_zambon_conjecture_report.md`, Conjecture 2 / Theorem D).
  - Part I claims the Bäcklund conclusion "for **any** local Lagrangian field theories", without the Lagrangian, transversality and connectedness hypotheses.
  - Part II claims an infinite hierarchy "in involution" "of increasing derivative order" under assumptions 1–3. Those assumptions omit the critical-manifold condition (4.4), Bianchi permutability, the Hamiltonian-generator property and the no-Casimir condition, and nontriviality is not proved.
  - The response says the companion report was brought in line; only one line changed.

## 5. The response misnumbers this report

The response cites sections "§A1–A3", "§B3", "§C1–C5" and "Recommendation 2" for criticisms that differ from what `report.md` says. It also attributes to `Probe2.lean` a finding about `two_eps_Ed`; `Probe2.lean` showed that S⁻¹S = 1 forces S = ±1 over `Int`. Future responses should quote the report's own item labels.

## Requested changes

1. Replace the `Int` carrier of `SpaceTimeDerivations` with a generic differential ring. Then re-prove Prop 4.1, Lemma 2.1, the free-scalar example and the NLS current, and check that their hypotheses are satisfiable in a nontrivial model.
2. Delete the "directly from the second row of (4.1)" route in Theorem 2(2) and §5.3. State instead that the hierarchy for KdV, mKdV and Boussinesq is not covered by Theorem 2, or give the correct density.
3. Either prove the (2.13) identification and `h_sym_step`, or relabel those Lean theorems as consequences of stated assumptions.
4. Bring the companion report's Theorem D and the PR description into line with the conditional paper.
5. Add a pointer in `response_to_referee_theorem_D.md` to the withdrawal.
