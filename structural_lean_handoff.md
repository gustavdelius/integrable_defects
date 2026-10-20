# Resume structural integrability formalization

The user's active request remains to formalize the corrected structural proof
in Lean. Theorem 2.1 is not yet completely formalized. Continue mathematical
work; do not repeat the completed Lean installation or hide missing steps as
assumptions.

Read the current [development checkpoint](briefs/structural_lean_development_checkpoint.md)
first, then the [original setup and full proof-obligation checkpoint](briefs/structural_lean_checkpoint.md).
The project is `defect-integrability/structural_type_I/lean`.

The preceding continuation closed the polynomial reconstruction gap. A
distinguished wave slot gives Euler-derivative symbols with unconstrained
remaining momenta; Vandermonde interpolation and faithful polarization
force the Euler derivatives to vanish. The homogeneous homotopy gives an
actual polynomial spatial primitive. Every vacuum-normalized conserved
polynomial functional of finitely many diagonal positive-mass fields equals
its quadratic component modulo `Dx`.

The nonlinear amplitude induction is also proved for formal series.
Conservation uses the constructed finite convolution of actual prolonged
derivations. Two conserved series with equal constant and quadratic classes
have equal classes in every degree, with polynomial primitives for each
coefficient difference. This does not assert convergence or a uniform
spatial-order bound, and the amplitude parameter is not the Bäcklund parameter.

The latest continuation adds four checked modules:

- `EulerExactness`: Euler cutoffs are stable above the density's order.
  A zero polynomial quotient class has zero Euler derivatives, without a
  bound on the chosen primitive. Formal conserved coefficients inherit this.
- `AnalyticTaylor`: actual convergent Fréchet series on fixed finite real
  jet spaces yield homogeneous jet polynomials with a common spatial-order
  bound. Their evaluations converge to the original function. The
  coefficients depend only on the germ and determine it uniquely.
- `AnalyticJetCalculus`: actual coordinate partial and spatial derivatives
  preserve analyticity, respect germ equality, and agree with the polynomial
  operators on evaluated polynomials.
- `AnalyticEuler`: an actual density of order `N` has actual analytic Euler
  functions of order at most `2N`, with convergent polynomial expansions.

All modules are imported by the aggregate and checked by the axiom audit.

**Next:** identify the Taylor coefficients of the actual analytic differential
operators with the corresponding polynomial operators. Agreement on
individual polynomials is proved; commutation with an infinite convergent
expansion is not. Construct actual analytic evolution and transport
conservation into the formal convolution, then use formal rigidity, Euler
exactness, and analytic uniqueness. The analytic local-functional quotient
across different jet orders, analytic scaling homotopy, Poisson/Jacobi, and
the Bäcklund and other structural conclusions remain outstanding. The
development checkpoint names relevant mathlib APIs for the next bridge.

Last proof-bearing publication to PR #32: commit `471a0e09af146d8e183322c671cb3c7cce05ba85`,
tree `80d3206d4870af785b8936800eb8176e8cce7f3b`, parent
`7b57a87a5fe627ac98ef14c01a7a1c5da1d4ba26`. Nine selected files were
published; no manuscript changes. The PR description records the exact
partial scope. The PR remains open and unmerged. All nine published files
were read back and match local bytes.

Full `lake build` passed (2,841 jobs). `lake env lean Audit.lean` passed for all
409 project declarations, with only `propext`, `Classical.choice`, and
`Quot.sound`. There are no live Lean sessions left from this continuation.

The saved workspace's worktree has an old detached HEAD. Do not publish its
complete diff. Inspect the actual branch state when using a fresh checkout.
Check the live remote PR head before publishing only selected new work. Prior
authorization to update PR #32 persists; do not ask again or merge. Do not
spawn subagents.

This file records the proof baseline. Later documentation commits may follow;
check the live PR head rather than treating the recorded proof commit as current.
