# Response to the second Lean referee report

- Report: [lean_referee/report2.md](../lean_referee/report2.md) (reviewed commit `34ed662`)
- Revised material: this directory ([paper.md](paper.md), [conjecture_report.md](conjecture_report.md), [checks/](checks/), [lean/](lean/))
- Date: 20 October 2026; author of the revision: Claude Opus 5.5

The same model wrote report 2 and this revision. The revision therefore needs an independent referee before any of it is relied on. Item labels below are those of report 2.

## Report 2, Section 1: derivations on `Int` have only the zero model

**Accepted and fixed.** The new Lean project ([lean/](lean/)) works over an arbitrary commutative ring `R` with `Lean.Grind.CommRing`. `Deriv.not_injective_of_nontrivial` records that a derivation is never injective on a nonzero ring, so no theorem assumes global injectivity. Normalisation is a hypothesis about one residual (`potential_from_normalised_residual`). The model `Tri` = ℤ[e₁,e₂]/(e₁², e₁e₂, e₂²) carries two nonzero commuting derivations (`Tri.derivations_nonzero`). In it the normalised kernel property holds (`Tri.normalised_kernel`) while global injectivity fails (`Tri.kernel_nontrivial`). The hypotheses are therefore satisfiable non-trivially. `lake env lean Audit.lean` shows only the standard axioms.

## Report 2, Section 2: the ∂ₓP_d route gives trivial charges

**Accepted and fixed.** The route is removed. Paper, Section 4.3 explains why it fails: the density difference is an exact derivative. Proposition 4.3 replaces it with a closure relation. Lemma 5.2 shows that the closure relation is the x,t-independent part of an affine conservation law. For KdV the generating density is the mass defect charge q − p, which is Gardner's density. For mKdV it is the defect momentum. For Boussinesq it is u − v. [checks/check_hierarchy.py](checks/check_hierarchy.py) verifies that every computed coefficient is a conserved density and records which are nontrivial; for KdV, orders 1, 3 and 5 are nontrivial.

## Report 2, Section 3: earlier items

| Item | Status now |
|---|---|
| D1, D2 (signs) | The paper uses no transcribed sewing relations. Every sewing equation is derived from the published defect Lagrangian in the scripts; the NLS branch check uses all four sewing equations of (2.4). |
| B1 (coisotropy) | No longer needed. Theorem 3.3 proves tangency by applying the t-Euler operator to the balance, using only the chain rule and Helmholtz self-adjointness. Coisotropy is kept only as an interpretation (Appendix A). |
| B2 (decay class) | Proposition 4.2 has two settings: formal branches, where Lemma 6.3 gives constancy of the residual, and actual solutions with a limit at one temporal end. The massless and kink sectors are discussed in Section 9. |
| B3 (involution, maps to generators) | The Bianchi-permutability route is dropped. Theorem 7.3 proves involution from nonresonance (Lemma 7.2, generalising the massive rigidity lemma of the structural paper) and the stated condition (L). |
| B4 (Schur complement) | Replaced by the injectivity conditions (I) of Theorem 3.3 and (T) of Lemma 3.5. Both are derived in the proofs, not postulated; auxiliary fields enter through the multiplier ρ. |
| B5 (off-shell balance) | Definition 3.1 states the balance as membership of an ideal; Lemma 3.2 relates it to conservation of total momentum. |
| B6 (`Int` carrier) | Fixed, as in Section 1 above. |
| C1 (general Lemma 2.1) | The canonical currents are defined by the explicit integrations by parts (2.1)–(2.3), and the identity $T^{11}=-\mathcal H^{(x)}$ is a consequence (Lemma 2.1). In Lean, `legendre_noether_K2` takes only the chain-rule premise; there is no `h_T1_1`. |
| C2 (Hamilton ⇔ Euler–Lagrange) | Lemma 2.2 has a written proof for all $K$; `hamilton_slots_K2` checks its algebra for $K=2$. |
| C3 ((2) ⇒ (1) with λ) | Appendix A gives the converse for Type I; the Type II converse is not claimed. |
| C4 (Theorem 1 chain) | Theorem 3.3(a) proves tangency directly; (b) proves that promoted solutions are bulk solutions. |
| C5 (recursion, symbol, second sewing equation) | Lemma 6.2 (general triangular recursion) and Lemma 3.5 (second sewing equation, with proof). The principal-symbol formula is replaced by the weight argument of Lemma 6.5, which is what independence needs. |
| C6 (nontriviality, "linearly independent") | Theorem 7.4 proves functional independence from linear independence of quadratic symbols, and Lemma 6.5 gives that independence for kinematic families. The overclaim is gone. |
| E (§5.3 flux hypothesis, references, "injective") | Closure is by Lemma 5.2 for every observed bulk theory. References are corrected. "Injective" is replaced by the explicit conditions (I) and (T). |

## Report 2, Section 4: documents out of step

- **Companion report.** [conjecture_report.md](conjecture_report.md) withdraws the claim of a proof "in full generality", restates Conjecture 2, and records per case what is established. The original report is preserved unchanged.
- **PR description and `response_to_referee_theorem_D.md`.** Not edited in this revision; they belong to the PR author. Suggested replacement for the PR description's item: "Theorem D: the Bäcklund half of Conjecture 2 is proved in general (general framework, Theorem 3.3); the integrability half is proved conditionally on a regular transparent family, closure and nonresonance (Theorem 8.1)."

## Report 2, Section 5: misnumbering

This response uses the labels of report 2 throughout.

## What is still open

- Deriving the transparent family from momentum conservation alone (paper, Section 10).
- Formal branches for Type-II defects.
- A direct independence check for Boussinesq, whose family parameter is not kinematic.
- Independent review of every written proof, including Theorems A–C of the report.
