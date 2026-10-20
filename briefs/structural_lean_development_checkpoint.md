# Structural integrability: mathematical development checkpoint

Date: 20 October 2026.

The active request remains **"Formalize the proof in Lean"**, most recently
steered by **"continue"**. Setup was followed by context compaction and the
substantive development below. The complete Theorem 2.1 remains outstanding.

Read the [setup checkpoint](structural_lean_checkpoint.md) for the environment,
manuscript, full obligation list, signs, repository history, and authorization.
Its statements that only smoke tests exist are historical.

## Completed mathematical components

The project is `defect-integrability/structural_type_I/lean` in the existing
`.claude/worktrees/lean-structural` worktree. Its README gives a module table,
and `Structural.lean` imports all modules.

1. `JetAlgebra`: actual multivariate polynomials in independent Cauchy jets;
   explicit finite spatial order; constructed `Dx`, iterates `dxn`, prolonged
   `evolution Q`, and proof that evolution commutes with `Dx`. Local functionals
   are the **submodule** quotient by the range of `Dx`; constants are retained.
   Repeated integration by parts and evolution on the quotient are proved.
2. `ConstantJet`: constant-field evaluation descends to the quotient.
   `integral_one_ne_zero`, `integral_z_zero_ne_zero`, and `Dx_ne_zero`
   certify that neither the derivative nor the quotient is vacuous.
3. `PeriodicEvaluation`: actual jet curves, constructed from any smooth field;
   conversely their jets equal iterated derivatives. Evaluation intertwines
   `Dx` with differentiation. The fundamental theorem of calculus gives the
   boundary formula and a periodic integral on the quotient. Only soundness,
   not the converse fundamental lemma, is proved.
4. `LinearRigidity`: the **complete degree-one assertion of Lemma 6.1** in the
   polynomial model, for diagonal nonzero squared masses. Field components
   are `species × Bool` (`false = u`, `true = p`). The inverse oscillator
   characteristic composes with free evolution to the identity on linear
   local functionals, proved on all jet generators and by span induction.
   `linear_conserved_is_divergence` gives an actual primitive.
5. `Dispersion`: massive-frequency derivatives and positive curvature;
   continuous-kernel vanishing from a nonzero mixed derivative, using product
   neighborhoods. `multiPhase_kernel_eq_zero` treats the full momentum
   hyperplane for every `n+3` factors. Kernels may be complex-valued. Resonant
   points are allowed; no absence-of-resonances assumption is made.
6. `MomentumDivisibility`: pointwise vanishing on the momentum hyperplane
   implies divisibility by total momentum.
   `complex_divisible_of_real_vanishes` handles complex coefficients evaluated
   only at **real** momenta by polynomial uniqueness on the real locus.
7. `Variational`: concrete finite Euler operators, commutators with `Dx`, and
   the telescoping formula
   `euler a N (Dx f) = (-1)^N • dxn (N+1) (pderiv (a,N) f)`.
   It vanishes when the primitive lacks that endpoint variable.
8. `PolynomialHomotopy`: finite-support chain rule, amplitude derivation,
   Euler's identity on the infinite jet algebra, and homogeneous homotopy.
   `homogeneous_is_divergence_of_euler_zero` proves that a positive-degree
   homogeneous real density with zero Euler derivatives is a divergence.
   This is a polynomial step, not analytic uniqueness.
9. `FreeChecks`: exact energy and physical-momentum currents; nonzero massless
   homogeneous chiral powers in every degree, in the same concrete model.
10. `Smoke` remains explicitly labeled as environment checks.

## Central missing bridge and next step

The spectral statements **do not yet prove** degree-three-and-higher free
rigidity for arbitrary `Jet.LocalFunctional`. Still needed:

- Polarization into a symmetric multilinear representation.
- Actual finite-order Fourier/symbol kernels for polynomial densities.
- Deriving `phase • kernel = 0` from `Conserved`.
- Inverting the normal-mode change in that representation.
- Reconstructing a symmetric density primitive from the momentum factor,
  or reconstructing through zero Euler derivatives and the proved homotopy.

Do not replace this bridge by an assumption or call the spectral theorem the
complete Lemma 6.1. An algebraic plane-wave substitution is a possible next
route: extract coefficients multilinear in the amplitudes of finite sums of
plane waves, derive the two multipliers, and prove reconstruction. That route
is proposed, not proved. A source search found symmetric-algebra infrastructure
but no ready general polynomial-polarization theorem.

After this remain analytic finite-jet germs, the actual Poisson bracket/Jacobi,
Taylor-degree induction, analytic Euler uniqueness, and all the Bäcklund
construction, normalization, involution, independence, and permutability.

## Verification and practical notes

- `lake build` succeeds on all modules (2,814 build/dependency jobs).
- `Audit.lean` automatically checks every `Structural` declaration and rejects
  all transitive axioms other than `propext`, `Classical.choice`, and
  `Quot.sound`. Consult the project's `verification.txt` for final output.
- No custom axiom, `sorry`, or `admit` is introduced.
- Do not reinstall Lean/mathlib. Keep focused imports.
- Import `Mathlib.Analysis.Calculus.Deriv.Add` explicitly for derivative dot
  methods, which otherwise may resolve to general Fréchet-filter methods.
- `convert` on `HasDerivAt` often gives a function-equality goal (`rfl`) before
  the derivative-value goal.
- Use `Derivation.map_smul`, `MvPolynomial.smul_eq_C_mul`, and
  `Nat.cast_smul_eq_nsmul` explicitly where needed.
- Clear redundant hypotheses before `Submodule.span_induction`.
- Do not filter an axiom audit by `ConstantInfo.isTheorem`. Lean 4.35 module
  exports may represent a proved theorem with an axiom-shaped interface.
  `Lean.collectAxioms` correctly uses its recorded proof dependencies. The
  audit therefore checks every declaration in the namespace.
- Do not spawn subagents or merge the PR. Publication to PR #32 is authorized.
  Publish selected files on the current remote tree, never all differences
  against this worktree's older HEAD.

## Publication state

The base rechecked during this work was PR #32 head
`4ff23cdd6d06aa67a52c9c4e5bef312fd1370ea8`, tree
`ef0e95aa42bc0f3625f9aeb73cbb2c5c13e5b158`.
The selected publication contains the Lean project and its two checkpoint
documents; no manuscript or already-published companion changes.
Recheck the live PR head when resuming: this document cannot contain its own
commit SHA.
