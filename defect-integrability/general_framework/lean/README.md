# Lean checks for the general framework

Lean 4 v4.35.0, core library only. Build with `lake build`; list axioms with `lake env lean Audit.lean`. No `sorry`, no added axioms.

**Scope.** These files check the final algebraic step of several lemmas of [../paper.md](../paper.md), over an arbitrary commutative ring with commuting derivations (`GeneralFramework.SpaceTime`). Fields, variations and operators are single ring elements and arbitrary maps of the ring. Jet spaces, Euler operators, adjoints and formal power series are not represented. **The main Theorem 8.1 is not formalised, and neither are the substantive steps of its proof.**

| Declaration | Paper step | Checked | Assumed (hypotheses) |
|---|---|---|---|
| `noether_first_order` | Lemma 2.1, spatial order 1 | Noether identities, $T^1{}_1=\mathcal H^{(x)}$ | chain rule for L |
| `ostrogradsky_K2`, `legendre_noether_K2` | (2.1), Lemma 2.1, spatial order 2 | integration by parts; Legendre–Noether identity | chain rule with the temporal boundary term Ξ |
| `hamilton_slots_K2` | Lemma 2.2, spatial order 2 | Ostrogradsky identities | — |
| `tangency_from_euler` | Theorem 3.3(a) | identities (3.5) imply tangency | (3.5) itself: its derivation (Euler-operator chain rule, Helmholtz) is the core of the proof |
| `promoted_implies_bulk`, `promoted_implies_bulk_typeI` | Theorem 3.3(b) | subtraction and injectivity argument | tangency relations, Lemma 2.2 facts, condition (I) |
| `potential_residual_closed`, `potential_from_normalised_residual` | Proposition 4.2 | D_t R = 0; normalisation of that residual | the normalisation hypothesis on R |
| `affine_law_expansion` | Lemma 5.2 | expansion of an affine current | — |
| `closure_conserved_density` | Proposition 4.3 | closure identity | defect charge and potential identities |
| `lorentz_curl` | Lemma 5.5 | 2×2 identity behind ΛεΛᵀ = ε | transformation law of the currents |
| `graded_rigidity`, `involution` | Lemma 7.2, Theorem 7.3 | induction over degrees | the nonresonance step (`h_rig`), (L), and the vanishing of the quadratic part (commuting quadratic parts, or (NR2) with (L′)) |
| `Tri.*` | consistency | nonzero commuting derivations; restricted normalisation satisfiable | — |

Not formalised: Lemmas 3.2, 3.5, 4.1, 5.4, 6.2, 6.3, 6.5; Lemma 6.6; Theorems 6.4, 7.4, 8.1; Proposition 7.5. A real formalisation would need jet bundles, the variational bicomplex, Euler operators and the Helmholtz conditions, none of which are in Mathlib.
