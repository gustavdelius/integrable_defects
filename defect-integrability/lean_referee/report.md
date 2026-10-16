# Referee report on PR #32: paper vs Lean formalization

- Date: 2026-10-16
- Model: Claude Opus 5.5 (claude-opus-5-5)
- Commit reviewed: `858af50` (head of `refs/pull/32/head`)
- Files: `defect-integrability/defect_integrability_paper.md`, `lean/DefectIntegrability.lean`, `lean/README.md`, `defect-integrability/response_to_referee_theorem_D.md`
- Evidence: `Probe.lean`, `Probe2.lean` and `checks.py` (sympy), in this directory. All probes compile. To rerun them from the repository root:

  ```bash
  cd lean && lake build && lake env lean ../defect-integrability/lean_referee/Probe.lean && lake env lean ../defect-integrability/lean_referee/Probe2.lean; cd ..
  python3 defect-integrability/lean_referee/checks.py
  ```

## Verdict

The Lean file builds (1.6 s, no `sorry`, only the standard axioms `propext`, `Quot.sound`, `Classical.choice`). But it does not formalize the paper's theorems. Almost every declaration either
(a) takes the paper's conclusion, or the key intermediate step, as a hypothesis;
(b) proves a linear-arithmetic rearrangement of hand-typed expressions over `Int`; or
(c) proves an abstract one-line lemma, such as the definition of a Lagrangian subspace or `congrFun`.

The README and the author response say that the Lean "ensure[s] that no sign error, unstated hypothesis, or algebraic gap remains". That is false. The Lean does not cover the steps where the paper's mathematics could fail. I found two sign errors in the revised paper that it did not catch (§D).

## A. Declaration-by-declaration comparison

| Paper | Lean | What is actually proved | Gap |
|---|---|---|---|
| Lemma 2.1, general K, A | `lemma_2_1_ostrogradsky` | Hypothesis `h_T1_1 : T1_1 = H_x + dΥ1_dt` *is* (2.13). The conclusion rearranges it. | The lemma is assumed, not proved. Nothing about (2.4), (2.6), Ostrogradsky momenta or Noether's identity enters. |
| Lemma 2.1, K=A=1 | `FirstOrderBulkJet.lemma_2_1_first_order` | Items 1–3 hold by `rfl`, because `T1_0`, `T1_1`, `H_x` are *defined* by the formulas to be proved. Items 4–5 are polynomial identities whose "∂_t T^0_0" was expanded by hand with the chain rule. | Scalar case only (r = 1). There is no derivation structure, so the chain-rule expansion is not checked. |
| (2.6) for K=2 | `ostrogradsky_K2_variational_identity` | `F1·δφ_x = (π0 + dF2_x)·δφ_x` with `π0 := F1 − dF2_x`. True for arbitrary integers. | Nothing ties `d_boundary_dx` to a total x-derivative. No t-derivatives (A > 0, Ξ) appear. |
| (3.6) isotropy | `eq_3_6_generating_functional_isotropic` | 1-dimensional, `Int` scalars, and S_ΨΦ = S_ΦΨ built in. | The paper needs formal self-adjointness of t-differential operators and handles λ; neither is modelled. Only **isotropy** is shown (see B1). |
| Remark 3.1 | `remark_3_1_automatic_energy_conservation` | Hypotheses are (2.12) and (3.7); the conclusion is their sum. | The content of (3.7), including the autonomous identity and Υ_0, is assumed. |
| Lemma 3.1 | `lemma_3_1_symplectic_intertwining` | Correct and faithful *pointwise linear-algebra* version. | It needs `IsLagrangianSubspace` in the strong form Γ^⊥ = Γ (B1). The parenthetical "locally constant / vanishes on components" in the paper's statement (1) is not formalized. |
| Transversality | `transverse_of_invertible_mixed_hessian` | Proves only `transverse_right`, in one dimension. Over `Int`, `S_inv * S = 1` forces S = ±1 (`Probe2.lean`). | `transverse_left` is not derived. λ is absent, so the Type-II criterion is wrong (B4). |
| Theorem 1 | `theorem_1_spatial_hamilton_jacobi_and_backlund` | Three **disconnected** conjuncts over unrelated variables. (1)↔(2) is `omega` on eight free integers (`Probe.lean` §4). (2)↔(3a) restates Lemma 3.1. (3b) uses only transversality and subtraction closure, not `hLag` (`Probe.lean` §5). | Scalar `H_x_minus` (density) and functional `dH_minus` (differential) are never linked. So the chain "momentum balance ⇒ ι*(H₋−H₊)=0 ⇒ δ(H₋−H₊)\|TΓ=0 ⇒ tangency" is **not** formalized. Also missing: the ∃P_d quantifier, the converse "vanishing integral ⇒ total t-derivative", the substitution of (3.4), connectedness and vacuum normalization, and the Hamilton ⇔ Euler–Lagrange step (2.9). The README's "(1)⇔(2)" and "(2)⇔(3a)" use two different statements called (2). |
| Prop. 4.1 | `proposition_4_1_stress_tensor_potentials` | Valid abstract argument. Over `Int`, though, every `SpaceTimeDerivations` is multiplication by a constant (`Probe.lean` §1). | `h_vac_norm : ∀ f, dt f = 0 → f = 0` is global injectivity of ∂_t (B2). The temporal balances at every x are hypotheses. No σ appears. |
| Thm 2(1) recursion | `theorem_2_part_1_jet_recursion` | `H v = r ↔ v = H⁻¹ r`. | Triangularity (R̃_n depends only on lower orders), existence, (4.9) and compatibility of the second equation are not formalized. |
| Thm 2(1) symbol | `theorem_2_part_1_principal_symbol` | Hypothesis `Ψ_lead (k+1) = R (Ψ_lead k)` *is* the claim. The proof is a trivial induction. | The fact that the leading part obeys that recursion is the content, and it is assumed. |
| — | `principal_symbol_nonzero` | Iterates of an injective map on a nonzero vector are nonzero. | **Not a statement of the paper.** The response uses it as a reply to referee item 9, but nonzero Ψ_n says nothing about Q_n being nontrivial or independent. |
| Thm 2(2) hierarchy | `theorem_2_part_2_hierarchy_conservation_laws` | `congrFun`: equal series have equal coefficients. | The series starts at n = 0 (no ε⁻¹ pole in J; P_d's pole is never discussed). Locality of the coefficients and the substitution of ψ(ε) are not formalized. |
| (4.12) Q_1 | `theorem_2_part_2_first_charge_density` | After `rw`, every conjunct is `x + 0 = x`. The docstring lists `∂²_ψB₋(φ,φ) = H` as a hypothesis, but **no such hypothesis exists**. H is a free variable, and the theorem stays true with H := 12345 (`Probe.lean` §3). | The Taylor expansion (4.8)/(4.12) is not formalized at all. |
| Thm 2(3) | `theorem_2_part_3_involution` | Correct, given its hypotheses. | Its hypotheses differ from the paper's (B3). |
| §4.3 example | `example_free_massive_scalar_Q1_conservation` | Correct identity for the hand-supplied Q_1, J_1. I re-derived Ψ_1 = φ_x − φ_t and Q_1 independently. | J_1 is not derived from P_d. |
| (5.1) | `section_5_1_relativistic_spatial_hamiltonian` | Correct, scalar. | — |
| §5.1 / Thm A | `section_5_1_chiral_backlund_equivalence` | The two hypotheses already imply **both** bulk equations (`Probe.lean` §6), so the "iff" is between two true statements. | Refers to the companion report's Theorem A, not to a statement in the paper. |

## B. Assumptions in the Lean that the paper does not state (or states differently)

1. **Lagrangian means Γ^⊥ = Γ.** `IsLagrangianSubspace` requires coisotropy as well as isotropy. The paper proves only isotropy (3.6) and then says "Since Γ is Lagrangian, (TΓ)^⊥ = TΓ". The space of t-histories with Ω = ∫dt δΦ∧δπ is only weakly symplectic, so "Lagrangian" is ambiguous there. The coisotropy half is exactly what the direction *momentum conservation ⇒ tangency* needs. Isotropy alone does not suffice (`Probe.lean` §7: Γ = {0} is isotropic but not Lagrangian).
   - Without λ, I checked by hand that the graph generated by S_d is coisotropic, provided the second variations are formally self-adjoint and the test-function class is closed under the operators. The paper should state the strong definition and prove it.
   - With λ, coisotropy needs δλ to be solvable from S_λΦδΦ + S_λΨδΨ + S_λλδλ = 0. S_λλ may be a t-differential operator, so this can be nonlocal or obstructed. This is unproved.
2. **Vacuum normalization.** `h_vac_norm` says ∂_t is injective on the whole algebra. The paper says only that specific combinations decay as |t| → ∞. The abstraction is acceptable only if the carrier is read as "local densities evaluated on t-decaying histories", and that should be said. The paper should also note that the decay class excludes kinks: a sine-Gordon kink tends to 2π/β, not 0, as t → +∞ at fixed x. It also excludes breathers, and Bäcklund partners ψ that add a soliton to a decaying φ. Prop. 4.1 is therefore unavailable in the soliton sectors that motivate the conjecture. This does not affect the formal series in Theorem 2.
3. **Involution (Thm 2(3)).**
   - `h_faithful` (X_H = 0 ∧ H(vac) = 0 ⇒ H = 0) means no non-constant Casimirs. The paper never states this nondegeneracy. It fails for the KdV-type Poisson structure ∂_x, whose Casimir is ∫u.
   - `h_vac_pb` (every bracket vanishes at the vacuum) is a *global* hypothesis on all charges. The paper derives it only for Q(ε) from X_{Q(ε)}(vac) = 0.
   - `h_bianchi` assumes [X_{Q_n}, X_{Q_m}] = 0 coefficientwise. The paper assumes commuting *finite* maps A_ε, and it never specifies how A_ε is "generated" by Q(ε) (time-1 flow? δ_εF = {F,Q(ε)}?). The passage from commuting maps to commuting generators is missing in both.
4. **Transversality criterion.** Both texts use invertibility of δ²S_d/δΦδΨ. For Type-II defects with λ, the relevant operator is the Schur complement S_ΦΨ − S_Φλ S_λλ⁻¹ S_λΨ (when S_λλ is invertible). The paper's criterion is therefore incomplete for the cases it claims to cover (§5.1, Type II). The Lean never models λ.
5. **"Identically along Γ_d".** The Lean treats the momentum balance as holding at every point of Γ_d. The paper's Theorem 1(1) says the same. That is stronger than requiring conservation on boundary data of actual bulk solutions. For massive fields, evanescent modes (|ω| < m) make the admissible data a proper subset. This is consistent with how Corrigan and Zambon compute (treating jets as independent), but it should be stated.
6. **`Int` as carrier.** Pure polynomial identities transfer to ℝ, so this is harmless for items such as (5.1). For "invertible operator" and "derivation" it is not: S⁻¹S = 1 forces S = ±1, and every derivation is a scalar. The README calls these formalizations of operator statements; they are not.

## C. Paper steps with no formal counterpart

1. Lemma 2.1 for general K and A: the identification "up to ∂_tΥ" from two divergence identities, which needs exactness of the 2-D variational complex.
2. (2.9): Ostrogradsky x-Hamilton equations ⇔ E = 0.
3. Theorem 1 (2)⇒(1): "vanishing functional ⇒ total t-derivative of a *local* P̃_d". This fails as stated when λ is constrained by δS_d/δλ = 0 rather than free.
4. The bridge from a vanishing function on a connected Γ_d to a vanishing differential on TΓ_d.
5. The Taylor expansions (4.8)–(4.12), triangularity, and compatibility of the second sewing equation.
6. Any statement that the Q_n are nontrivial or independent. Without this, Theorem 2 does not give integrability. So neither the paper nor the Lean proves the second half of the Corrigan–Zambon conjecture, contrary to the PR description ("proving Conjecture 2 in full generality"). The paper's own Theorem 2 is conditional on an assumed spectral family, Definition 4.1 and Bianchi permutability. The abstract and PR description should say that integrability is *conditional* on these.

## D. Errors in the revised paper that the Lean did not catch

1. **(4.7), second line: sign of the gyroscopic terms.** From L_d = A_Φ·Φ_t + A_Ψ·Ψ_t − …, one gets δS_d/δΨ = +Ω_ΨΦ Φ_t + Ω_ΨΨ Ψ_t − ε⁻¹∇_ΨB₋ − …. So π₊ = +δS_d/δΨ has **+Ω_ψφ φ_t + Ω_ψψ ψ_t**; the paper prints −. Check on the paper's own free example (`checks.py`): π₊ = −φ_t + …, and Ω_ψφ = −1. The first line of (4.7) is correct. The error does not propagate into (4.10), which uses only the first line, but the response says the (4.7) signs were audited.
2. **§5.2 NLS number current.** For the paper's L₋, ∂_t|u|² = **+**∂_x[i(ū u_x − u ū_x)]. The flux is therefore J_N = −i(ū u_x − u ū_x) = **+2T^{01}**, not −2T^{01}. Equation (4.2) then gives ∂_tN_d **+** 2∂_xP_d = 0. The paper's J_N has the wrong sign, and so has its continuity equation (`checks.py`: J_paper/T01 = −2, and ∂_tN − ∂_xJ_paper = 0).

## E. Other points

- Theorem 2 requires (4.2), a bulk conservation law whose flux is c·T^{01}. §5.3 (KdV, mKdV, Boussinesq) never identifies such a law. For pKdV, T^{01} = −½p_x², while the mass flux contains p_xxx, so it is not obviously of this form. The applicability of Theorem 2 claimed in §5.3 and the Conclusion is unverified.
- §4.3 example cites [2] (affine Toda) for the free massive defect. That defect appears in [1].
- Line 243 calls R = −H⁻¹D∂_t "invertible". ∂_t is injective on decaying histories but not surjective onto local functions.

## Recommendations

1. Rename the Lean results honestly: "algebraic consistency checks", not "formalization of Theorems 1–2". Alternatively, formalize the bridge in C4 and the expansions in C5 over a genuine differential ring (e.g. Mathlib `Derivation`, `PowerSeries`).
2. Delete or fix `theorem_2_part_2_first_charge_density`. As written it is `x + 0 = x`, and its docstring names a hypothesis that does not exist.
3. In the paper, state explicitly:
   - the strong Lagrangian (coisotropy) hypothesis, with a proof for generating functionals;
   - the Schur-complement transversality condition when λ is present;
   - no Casimirs (for Part 3);
   - the decay class and its exclusion of kink sectors;
   - that Theorem 1(1) is an off-shell identity on Γ_d.
4. Fix the sign errors D1 and D2.
5. Withdraw from `response_to_referee_theorem_D.md` the statement that the Lean rules out sign errors and unstated hypotheses.
