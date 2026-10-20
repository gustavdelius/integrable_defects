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

11. `PlaneWave`: `waves k v` substitutes finite sums of independently labeled
    waves into every jet. The spatial and free-time derivations intertwine
    with diagonal amplitude derivations. Coefficient extraction gives the
    conservation equation from an actual `Conserved` hypothesis, including
    a flux. Coefficients are continuous in continuous wave parameters.
    Changing coefficient rings commutes with `Dx` and prolonged evolution.
12. `Polarization`: general coefficient polarization on any variable type;
    exact diagonal formula `polarization f (constant x) = n! * eval x f`
    for homogeneous degree equal to the number of slots. It is injective on
    that homogeneous subspace over characteristic-zero fields.
13. `PolarizationMultilinear`: `zeroSlot`, directional differentiation, and
    `polarization_slot_formula` prove genuine slot-by-slot multilinearity.
    `polarizationMap` and `wavePolarization` are actual `MultilinearMap`s.
14. `MassiveSymbol`: explicit complex normal-mode vectors, checked oscillator
    equations and continuity; the existing dispersion theorem now proves
    vanishing of the symbols *constructed from conserved densities*.
15. `NormalModes`: explicit inverse `(u ± p/(i ω))/2`, justified by positive
    masses. Multilinearity extends vanishing to arbitrary Cauchy vectors in
    every slot. Finitely many species are used for this expansion.
16. `PolynomialSymbol`: actual finite momentum polynomials constructed by
    running the wave substitution over a polynomial coefficient ring.
    Evaluation returns the earlier wave symbol. The actual symbols of
    conserved densities have a total-momentum polynomial factor in every
    amplitude degree at least three. This is also proved for real densities
    using the proved extension-of-scalars theorem.

## Remaining reconstruction step

The forward chain from arbitrary conserved densities to polynomial momentum
factors is now proved. The complete degree-three-and-higher free-rigidity
lemma is still missing **reconstruction modulo spatial derivatives**.
Unrestricted polarization injectivity alone does not prove this quotient
statement. Do not identify the new divisibility theorem with the full lemma.

Two possible routes remain; neither has been implemented:

1. Reassemble the momentum quotient polynomials as a density primitive, with
   permutation compatibility. A linear reassembly map sends momentum
   monomials to products of spatial jets; multiplication by total momentum
   must map to `Dx`. Summing over field labels should recover `n! * f`.
2. Use Euler derivatives and the existing homogeneous homotopy. Apply
   `polarization_slot_formula` to the distinguished `none` slot on the
   momentum hyperplane. Its factors `(-sum k)^r` should turn into the Euler
   sum for the remaining slots, by the proved `component_Dx` identity.
   This would show that every wave polarization of each Euler derivative
   vanishes, now with *unconstrained* remaining momenta. Finite-order jet
   vectors are spanned by real-momentum plane waves using a Vandermonde
   matrix. Multilinearity and polarization injectivity would then give zero
   Euler derivatives and the existing homotopy would construct the primitive.

The second route may avoid symmetrizing quotient polynomials. Relevant local
mathlib infrastructure: `MvPolynomial.IsHomogeneous.pderiv` in
`RingTheory/MvPolynomial/EulerIdentity.lean`, `Matrix.det_vandermonde_ne_zero_iff`
in `LinearAlgebra/Vandermonde.lean`, and `coeff_rename_mapDomain` for eliminating
an amplitude slot via `rename Option.some`. Homogeneity preservation by `Dx`
and the finite Euler sum still needs to be proved if using this route.

The earlier lack of a ready-made general polynomial-polarization theorem is
no longer a blocker: the new modules prove the required normalization and
multilinearity directly by coefficient extraction and directional derivatives.

After this remain analytic finite-jet germs, the actual Poisson bracket/Jacobi,
Taylor-degree induction, analytic Euler uniqueness, and all the Bäcklund
construction, normalization, involution, independence, and permutability.

## Verification and practical notes

- Consult `verification.txt` for the current full build and axiom audit.
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
- In Lean 4.35, multivariate coefficients use `P.coeff d` (from
  `AddMonoidAlgebra`); the former standalone `MvPolynomial.coeff d P` is gone.
- `Function.update_self` and `Function.update_idem` are the relevant update
  lemmas; `Option.elim` takes the option argument first.
- Put `omit ... in` before a declaration's doc comment.
- Avoid `change polarized _ _ f = 0` under a multilinear-map definition:
  underconstrained higher-order unification can take minutes and exhaust
  heartbeats. Explicitly provide the momenta and the vector function; the
  same proof then checks in seconds.
- For coefficient continuity, `continuous_add.comp (hf.prodMk hg)` avoids
  a problematic elaboration of pointwise `Continuous.add` in this context.
- Do not filter an axiom audit by `ConstantInfo.isTheorem`. Lean 4.35 module
  exports may represent a proved theorem with an axiom-shaped interface.
  `Lean.collectAxioms` correctly uses its recorded proof dependencies. The
  audit therefore checks every declaration in the namespace.
- Do not spawn subagents or merge the PR. Publication to PR #32 is authorized.
  Publish selected files on the current remote tree, never all differences
  against this worktree's older HEAD.

## Publication state

The base rechecked during this continuation was PR #32 head
`336d9d6343b638203b9061aae05f946164861019`, tree
`0b4b59357cbc01e0f09cec58098873ed30f43115`.
The selected publication adds the six symbol/polarization modules and updates
imports, the audit, README, dispersion status comment, verification record,
and this checkpoint. No manuscript or companion changes are included.
Recheck the live PR head when resuming: this document cannot contain its own
commit SHA. The root `structural_lean_handoff.md` records the published SHA.
