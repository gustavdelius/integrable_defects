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

17. `JetHomogeneity`: spatial differentiation and linear evolution preserve
    amplitude degree; Euler differentiation lowers it. Homogeneous projection
    commutes with linear evolution and with `Dx`, so actual conservation
    descends to each homogeneous component with an actual projected flux.
18. `EulerSymbol`: the distinguished-slot formula on the momentum hyperplane
    equals the sum of Euler-derivative wave symbols. Selecting one component
    makes every Euler wave symbol vanish with unconstrained remaining momenta.
19. `WaveFaithfulness`: an invertible Vandermonde matrix at integer real
    momenta interpolates every finite jet. Multilinearity and finite support
    turn wave tests into arbitrary polarization tests, which are faithful.
20. `FreeRigidity`: `higher_conserved_is_divergence` combines the preceding
    steps, extension of scalars, and homogeneous homotopy to give an actual
    real polynomial primitive in every homogeneous degree at least three.
    Together with degree one and projection to homogeneous components,
    `polynomial_conserved_quadratic_primitive` shows that every conserved
    vacuum-normalized polynomial differs from its quadratic component by
    an actual spatial derivative. This closes the former reconstruction gap.
21. `FormalRigidity`: formal amplitude series have homogeneous polynomial
    density coefficients of degree `n` and characteristic coefficients of
    degree `k+1`. Evolution is the finite convolution of the actual prolonged
    polynomial derivations. Its grading is proved. Strong induction removes
    all terms except the free linearized term once lower-degree classes are
    zero. `conserved_eq_of_quadratic_eq` proves equality of all coefficient
    classes for two conserved series with equal constant and quadratic
    classes. `conserved_difference_primitives` supplies polynomial spatial
    primitives coefficient by coefficient.

## Current mathematical boundary and next steps

Polynomial free massive rigidity is now proved for finitely many diagonal
positive-mass fields. The reconstruction uses Euler derivatives and
Vandermonde interpolation, rather than reassembling the momentum factors.
No quotient injectivity or vanishing-Euler statement has been assumed.

The amplitude induction of the nonlinear rigidity argument is also proved
in a formal model. Its parameter scales all Cauchy jets; it is not the
Bäcklund parameter. Conservation is defined by a constructed finite
convolution, using the actual polynomial evolutionary derivations. The
formal result does not assert convergence, a uniform spatial-order bound,
or correspondence with Taylor coefficients of analytic finite-jet germs.

Next develop that analytic bridge: define the actual finite-jet analytic
local-density class and spatial/evolutionary operators, identify their
Taylor coefficients with the formal homogeneous model, show Euler
operators annihilate every coefficient divergence, and use analytic
uniqueness followed by the analytic scaling homotopy. Do not infer an
analytic primitive by summing the coefficient primitives without bounds.
A useful small next lemma is independence of the finite Euler cutoff above
the density's spatial order, then vanishing of Euler derivatives for every
zero class without imposing an order bound on the chosen primitive.

The actual canonical Poisson bracket and Jacobi identity are still missing.
All the Bäcklund construction, momentum splitting, normalization, involution,
independence, and permutability also remain to be formalized. The analytic
Lemma 6.2 and full Theorem 2.1 are not claimed as Lean theorems.

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
`ee3456c5998bf523bada54e7e10189ba8011f9b8`, tree
`3287c342de0c9fe88100b830ab3d3f854e6cd219`.
The selected publication adds the five homogeneity, Euler-symbol,
wave-faithfulness, free-rigidity, and formal-rigidity modules; updates the
aggregate imports, audit, README, three earlier status comments,
verification record, and this checkpoint. No manuscript or companion
changes are included. Recheck the live PR head when resuming: this document
cannot contain its own commit SHA. The root `structural_lean_handoff.md`
records the published SHA.
