# Defect integrability: current proof and review history

Start with the [Theorem D reconstruction](theorem_D_reconstruction/proof.md) and its [scope and verification guide](theorem_D_reconstruction/README.md).

The reconstruction supplies a complete written formal proof for one relativistic scalar with an analytic Type-I defect, a normalized positive-mass vacuum, and an off-shell local momentum balance. It derives the parameter family, solves both sewing equations, proves Bianchi permutability and equal-time spectrality, and establishes an infinite independent commuting hierarchy. It also gives a corrected KdV Gardner construction and a general spatial Hamilton–Jacobi argument under explicit regularity and geometric assumptions.

**The unrestricted Theorem D remains unproved. The complete scalar theorem is not formalized in Lean.** The replacement Lean project verifies specified differential-ring identities and includes a nonzero derivation model. Its precise limits are documented alongside the proof.

## Verification

Run the reconstruction's checks from the repository root:

```sh
python3 defect-integrability/theorem_D_reconstruction/verify.py
```

The [recorded output](theorem_D_reconstruction/verification.txt) includes exact symbolic checks, the Lean build, and an audit of theorem dependencies. The reconstruction is submitted for independent mathematical review.

## Earlier drafts and reports

These files preserve the development and review history. Claims in them of a universal proof or complete formalization are not established by the reconstruction.

- [Original research paper](defect_integrability_paper.md)
- [Conjecture report](corrigan_zambon_conjecture_report.md)
- [First referee report](referee_report_theorem_D.md) and [author response](response_to_referee_theorem_D.md)
- [Lean referee report](lean_referee/report.md), [author response](lean_referee/response.md), and [second referee report](lean_referee/report2.md)
- [Earlier Lean project](../lean/README.md)

## Integration

The reconstruction replaces the unsupported scalar steps with explicit derivations and independently written exact checks: the full sewing recursion, the equal-time generator, permutability, and functional independence. It replaces the failed KdV density construction and supplies generic-ring Lean lemmas with a consistent nonzero derivation model. It does not accept the earlier unrestricted integrability or complete-formalization claims. The earlier drafts, responses, reports, and Lean project are preserved for comparison; the new project has its own pinned toolchain and verification command.
