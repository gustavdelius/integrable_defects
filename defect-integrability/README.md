# Defect integrability: current proofs and review history

Start with the [structural Type-I proof](structural_type_I/proof.md) and its [verification guide](structural_type_I/README.md). It keeps the multicomponent bulk potential unspecified and supplies a complete written argument for infinitely many independent commuting local charges under explicit hypotheses: an analytic positive-mass vacuum, bulk irreducibility, normalized constant Type-I coupling, a derivative-free strong momentum balance, and a transparent nondegenerate critical point.

The structural argument derives the parameter family, solves both sewing equations formally, and constructs an equal-time generating functional. Its central additional lemma says a local conserved functional near a massive analytic vacuum is determined by its quadratic part. This upgrades commuting quadratic generators to full involution; formal Bäcklund permutability follows. A reducible free-field counterexample shows why an arbitrary momentum-conserving family need not itself commute.

The earlier [Theorem D reconstruction](theorem_D_reconstruction/proof.md), with its [scope guide](theorem_D_reconstruction/README.md), remains available. It supplies a separate scalar proof, an explicit scalar Bianchi formula, a corrected KdV Gardner construction, and a general spatial Hamilton–Jacobi argument under explicit regularity and geometric assumptions.

**The unrestricted Theorem D remains unproved. Neither complete theorem is formalized in Lean. Both new written proofs await independent mathematical review.** The separate Lean project verifies specified differential-ring identities and includes a nonzero derivation model; its precise limits are documented alongside the scalar reconstruction. Parameter series are formal, with no assertion of convergence.

## Verification

From the repository root:

```sh
python3 textbook_code/defect_integrability_structural/checks.py
python3 defect-integrability/theorem_D_reconstruction/verify.py
```

The structural proof's [recorded output](structural_type_I/verification.txt) contains 30 exact finite symbolic checks, including four nonlinear local currents and the Poisson bracket of two nontrivial higher charges in a coupled two-component example. Its massive local-functional lemma and all-orders arguments are written proofs, not machine-certified results.

The scalar reconstruction's [recorded output](theorem_D_reconstruction/verification.txt) includes its symbolic checks, Lean build, and theorem-dependency audit. The structural continuation does not modify that project.

## Earlier drafts and reports

These files preserve the development and review history. Claims in them of a universal proof or complete formalization are not established by either reconstruction.

- [Original research paper](defect_integrability_paper.md)
- [Conjecture report](corrigan_zambon_conjecture_report.md)
- [First referee report](referee_report_theorem_D.md) and [author response](response_to_referee_theorem_D.md)
- [Lean referee report](lean_referee/report.md), [author response](lean_referee/response.md), and [second referee report](lean_referee/report2.md)
- [Earlier Lean project](../lean/README.md)

## Integration

The scalar reconstruction replaces unsupported scalar steps with explicit derivations and independently written exact checks: the full sewing recursion, the equal-time generator, permutability, and functional independence. It replaces the failed KdV density construction and supplies generic-ring Lean lemmas with a consistent nonzero derivation model.

The structural continuation independently rederives the constant Type-I momentum constraints and supplies the missing temporal generator, commutation, and independence arguments under its stated hypotheses. It rejects automatic permutability for an arbitrary invertible leading defect Hessian, with an exact counterexample. Its proof of commutation uses bulk irreducibility to remove that obstruction and uses positive masses and analyticity to justify the upgrade from quadratic to full charges.

Neither reconstruction accepts the earlier unrestricted integrability or complete-formalization claims. The earlier drafts, responses, reports, and Lean project are preserved for comparison. No book theorem labels are changed.
