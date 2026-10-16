# Theorem D reconstruction

Start with [proof.md](proof.md). The main result is **Theorem S**: for one relativistic scalar with an analytic Type-I defect, a normalized vacuum with positive mass squared, and an off-shell local momentum balance, the defect produces infinitely many functionally independent local charges in involution.

The proof derives the parameter family, solves both sewing equations formally, proves Bianchi permutability, identifies an equal-time generating functional and its parameter derivative, and proves independence by a Fourier-mode Jacobian. These are conclusions in this scalar class, not assumptions added to its theorem. No convergence of the parameter series is asserted.

**The unrestricted Theorem D remains unproved.** This directory is a replacement proof with explicit scope, not an endorsement of the earlier claims of a universal theorem or complete Lean formalization. The earlier paper, responses, and referee reports have been left intact.

| Result | Written proof | Machine verification |
|---|---|---|
| Scalar Type-I integrability theorem | Sections 2–7, all formal orders | Key exact identities and first five nonlinear current coefficients checked; not fully formalized |
| General spatial Legendre–Noether identity and Hamilton equations | Section 8, under stated local regularity assumptions | First-order and spatial order two identities in Lean, with explicit chain-rule premises |
| General spatial invariance | Section 8, for a strong Lagrangian sewing manifold and an off-shell balance | No new full phase-space formalization |
| KdV Gardner hierarchy, independence and involution | Section 9 | Gardner and Lenard identities checked symbolically |
| Arbitrary Type-II, multicomponent, or higher-derivative defect implies integrability | **Not proved** | **Not formalized** |

## Relation to the second referee report

- **Section 1, derivations and normalization:** the new Lean carrier is an arbitrary commutative ring. A dual-number ring supplies a nonzero derivation; a concrete differentiated scalar density is nonzero. Normalization is imposed only on the specified residuals. A separate theorem shows why global injectivity of a derivation would force a zero ring.
- **Section 2, the erroneous KdV density:** Section 9 uses the actual Gardner density and proves both independence and involution. It does not extract charges from a spatial divergence.
- **C1 and C2:** Section 8 derives the Noether representative by a specified integration by parts and checks the spatial Hamilton–Euler–Lagrange equivalence. Only the indicated lower-order algebra is formalized.
- **C5 and C6:** in the scalar class, Sections 3 and 7 replace assumed symbol recursions by an actual triangular construction, a proof of the second sewing equation, and an independent quadratic calculation. The Fourier-mode determinant proves functional independence, not merely nonvanishing.
- **B3 and the generator gap:** Sections 5 and 6 prove the commuting-map formula, temporal canonicity, the parameter-generator identity, and the passage from commuting maps to commuting Hamiltonian vector fields.

## Reproducing the checks

Requirements: Python 3 with SymPy (tested with Python 3.12.3 and SymPy 1.14.0), and Lean 4.35.0 with Lake. There are no Mathlib or other Lean package dependencies. The toolchain is pinned in `lean/lean-toolchain`.

From this directory, run:

```sh
python3 verify.py
```

The script runs both exact symbolic suites, builds the Lean project, and asks Lean to report the axioms of the checked theorems. It fails if any command fails, any checked source contains a proof placeholder or added axiom declaration, or the printed dependencies contain `sorryAx`. The recorded run is [verification.txt](verification.txt).

The checked Lean statements cover differential-ring algebra. They do not implement a full jet algebra, variational quotient, infinite-dimensional symplectic geometry, or the all-orders proof of Theorem S. The dual-number example demonstrates consistency of the algebraic hypotheses; it does not model the bulk field theory.
