# Lean project for structural defect integrability

**Status: polynomial free massive rigidity and formal amplitude-series nonlinear rigidity are proved. The analytic rigidity lemma and Theorem 2.1 are not yet formalized.**

This is a separate project for the corrected structural theorem. It does not import the older integer-based defect development. Its local densities are actual multivariate polynomials in independent Cauchy jets over the reals (with several algebraic results proved over more general coefficient rings). Spatial and evolutionary derivatives are constructed, and local functionals are the vector-space quotient by spatial divergences.

The quotient is not a ring quotient: multiplying two local integrals is not an operation on local densities. Constants have not been discarded. Vacuum normalization remains a separate condition. The derivative and quotient are proved nontrivial.

## What Lean currently proves

| Module | Verified result |
|---|---|
| `JetAlgebra` | Finite spatial order of polynomial densities, total spatial differentiation, prolonged evolutionary derivations, their commutation, quotient local functionals, repeated integration by parts, and evolution on the quotient. |
| `ConstantJet` | Evaluation on constant fields annihilates divergences; the spatial derivative is nonzero, and the classes of one and undifferentiated fields are nonzero. |
| `PeriodicEvaluation` | Smooth fields provide actual jet curves; formal total differentiation evaluates to ordinary differentiation; integrating a divergence gives the endpoint term; matching endpoint jets yields a well-defined integral on the quotient. |
| `LinearRigidity` | The complete degree-one assertion of Lemma 6.1 for diagonal free fields with nonzero squared masses: every conserved homogeneous linear density is a spatial derivative. |
| `Dispersion` | Massive frequency derivatives and positive curvature; the continuous-kernel vanishing argument on the momentum hyperplane for every degree at least three, with arbitrary sign and species choices. The coefficient space can be complex. |
| `MomentumDivisibility` | A polynomial vanishing on the momentum hyperplane is divisible by total momentum. Complex coefficients are allowed while the tested momenta remain real. |
| `Variational` | Actual polynomial Euler derivatives, their commutation identities, the telescoping boundary formula on divergences, and the variational integration-by-parts identity. |
| `PolynomialHomotopy` | Amplitude scaling and Euler's identity in the infinite jet algebra; a positive-degree homogeneous density with vanishing Euler derivatives is a spatial derivative. |
| `FreeChecks` | Exact energy and momentum conservation; nonzero homogeneous conserved chiral powers of every degree for massless fields. This explicitly verifies failure of massive rigidity when the mass condition is dropped. |
| `PlaneWave` | Actual finite plane-wave substitution, spatial and free-time eigenvalue identities, coefficient continuity, and derivation of the phase equation from `Conserved`; extension of scalars preserves conservation. |
| `Polarization` | Exact factorial normalization on the diagonal and injectivity of polarization on homogeneous polynomials in characteristic zero. |
| `PolarizationMultilinear` | A directional-derivative formula for each slot; genuine multilinearity of coefficient polarization and wave symbols. |
| `MassiveSymbol` | Normal modes satisfy the Klein–Gordon equations; the polarized symbol constructed from any conserved density vanishes on the momentum hyperplane in every degree at least three. |
| `NormalModes` | Explicit inverse frequency-mode transformation; vanishing extends to arbitrary Cauchy vectors in every slot, for finitely many species. |
| `PolynomialSymbol` | Actual finite momentum polynomials, their evaluation identities, and divisibility of conserved-density symbols by total momentum. Applies to the original real coefficient model. |
| `JetHomogeneity` | Spatial differentiation preserves amplitude degree; Euler derivatives lower it; linear evolution commutes with homogeneous projection, so each component of a free conserved density is conserved. |
| `EulerSymbol` | On zero total momentum, a distinguished polarization slot gives the Euler derivatives. Conservation forces their wave symbols to vanish with unconstrained remaining momenta. |
| `WaveFaithfulness` | A Vandermonde matrix expresses every finite jet as a sum of real-momentum complex waves. Unconstrained wave tests are therefore faithful on homogeneous densities. |
| `FreeRigidity` | For finitely many diagonal positive-mass fields, every homogeneous conserved density of degree at least three has an actual polynomial spatial primitive. Every vacuum-normalized conserved polynomial functional equals its quadratic component. |
| `FormalRigidity` | Nonlinear evolution is constructed as a finite convolution of homogeneous polynomial coefficients. With positive massive linearization, two conserved formal amplitude series having the same constant and quadratic classes agree modulo spatial derivatives in every degree. |
| `EulerExactness` | The polynomial Euler operator is independent of its cutoff above the density's order. Every zero quotient class has zero Euler derivatives, without any bound on its primitive; this applies to every coefficient supplied by formal rigidity. |
| `AnalyticTaylor` | Actual Fréchet expansions of analytic finite-jet functions give homogeneous polynomials with a uniform spatial-order bound and convergence near the vacuum. The coefficients depend only on the germ, determine it uniquely, and detect the zero germ. |
| `AnalyticJetCalculus` | Actual coordinate partial and total spatial derivatives preserve analyticity and respect equality of germs. They agree with the polynomial jet operators on evaluated polynomials. |
| `AnalyticEuler` | The actual Euler derivative of an analytic density of order `N` is an analytic function of jets through order `2N`. It respects equality of germs and has an actual convergent homogeneous polynomial expansion with that common order bound. |
| `Smoke` | Environment checks only. |

The degree-one result holds for arbitrarily many components because each polynomial uses only finitely many. The homogeneous Euler homotopy uses finitely many field components, as in the paper.

## How reconstruction and formal rigidity are proved

Conservation of an actual jet density implies a phase equation, hence vanishing of its normal-mode symbols and vanishing for arbitrary Cauchy vectors. The **reconstruction gap is now closed**: a distinguished slot on the momentum hyperplane gives wave symbols of the Euler derivatives with unconstrained remaining momenta. Vandermonde interpolation and faithful polarization force these Euler derivatives to vanish. The homogeneous scaling homotopy then produces a spatial primitive in the original real polynomial jet algebra. No symbol-to-density correspondence is assumed.

In `FormalRigidity`, the parameter scales all Cauchy jets; it is not the Bäcklund parameter. Density coefficient `n` is homogeneous of degree `n`, and characteristic coefficient `k` is homogeneous of degree `k+1`. The actual prolonged evolution gives a finite convolution in each degree. Strong induction shows that a conserved series whose constant and quadratic classes vanish has every coefficient class zero: evolution of lower-degree divergences is again a divergence, leaving a free conserved term to which polynomial rigidity applies.

The formal theorem also supplies a polynomial primitive for each coefficient difference. It does **not** assert convergence or a common spatial-order bound for the coefficients or their primitives. It concerns formal sequences of homogeneous polynomials, with conservation defined by the constructed convolution, rather than Taylor expansions of an already defined analytic local functional.

## The analytic connection so far

`AnalyticTaylor` starts from an actual real function of the jets through a fixed order `N` and a genuine convergent Fréchet power series at zero. Expanding each multilinear coefficient in the coordinate basis constructs a homogeneous polynomial in the existing jet algebra. All coefficients have spatial order at most `N`, their evaluations sum to the function near zero, and equality of these polynomials is equivalent to equality of the analytic germs. No symmetry of the multilinear representative is assumed.

Actual spatial differentiation is `Df(lower jets)[shifted jets]`. Actual coordinate partial differentiation and the finite Euler expression are also constructed. Their analyticity and invariance under changes of germ representative are proved. On polynomials, partial and spatial differentiation agree with the original polynomial operators. An Euler expression uses jets through at most order `2N` and therefore also has an actual convergent polynomial expansion.

On the polynomial side, zero local-functional classes have zero Euler derivatives at any cutoff bounding the density's order. This needs no order or convergence estimate on the arbitrary primitives obtained from formal rigidity.

## What is still missing

The key remaining identification is that **Taylor expansion commutes with the differential operators on general analytic functions**. In particular, the coefficients of the actual analytic Euler expression must be identified with the polynomial Euler derivatives of the original coefficients. Agreement on individual polynomial functions does not establish this for an infinite convergent expansion. Analytic evolution and transport of conservation into the formal convolution also remain to be proved. Thus the available analytic uniqueness theorem cannot yet be applied to conclude analytic rigidity.

The analytic local-functional quotient across different finite jet orders and the analytic scaling homotopy remain outstanding. Germ equality is currently handled by equality on a neighborhood in each fixed finite jet space. The canonical Poisson bracket and its Jacobi identity also remain to be constructed. The sound periodic-evaluation map is proved for polynomial densities; its converse is not.

The momentum-splitting and normalization arguments, the actual formal Bäcklund branch, generating-functional identities, quadratic generators, nonlinear involution, functional independence, and formal permutability also remain to be formalized. No theorem in this project packages these missing results as assumptions and then claims Theorem 2.1.

## Reproducing the checks

The project pins Lean 4.35.0 and mathlib commit `56a005855ea17e0b0958f73ec801ae140b0a1679` (release v4.35.0). The dependency manifest pins the transitive dependencies.

From this directory:

```sh
lake build
lake env lean Audit.lean
```

`Audit.lean` inspects every declaration in the `Structural` namespace and fails if any transitive dependency is an axiom other than Lean's standard `propext`, `Classical.choice`, or `Quot.sound`. In particular, `sorryAx` fails the audit. It also prints the dependencies of the principal results. It uses Lean's recorded module dependencies, since imported theorem interfaces need not have the internal `isTheorem` flag. See [verification.txt](verification.txt) for the recorded build and audit.

See the [formalization checkpoint](../../../briefs/structural_lean_checkpoint.md) for the exact proof obligations, conventions, environment setup, and continuation instructions. In particular, assuming rigidity or independence in a conditional theorem would not formalize their proofs.
