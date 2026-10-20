# Defect integrability: current proofs and review history

Start with the corrected [research paper](defect_integrability_paper.md), *Momentum-Conserving Type-I Defects and Local Integrability near a Massive Vacuum*. It is self-contained and uses the multicomponent structural proof. Theorem 2.1 gives infinitely many independent commuting local charges under explicit hypotheses: an analytic positive-mass vacuum, bulk irreducibility, normalized constant Type-I coupling, a derivative-free strong momentum balance, and a transparent nondegenerate critical manifold.

For a slower explanation, read the [pedagogical companion](defect_integrability_companion.md). It explains every assumption and each sentence of Theorem 2.1, including small periodic Cauchy data, then follows every proof section, both examples, the limits on different bulk theories, and the spatial Hamilton–Jacobi appendix. It includes a reading map and notation guide. The companion explains the existing argument and retains its review status; it is not an independent referee report.

The structural argument derives the parameter family, solves both sewing equations formally, and constructs an equal-time generating functional. Its central additional lemma says a vacuum-normalized local conserved functional near a massive analytic vacuum is determined by its quadratic part. This upgrades commuting quadratic generators to full involution; formal Bäcklund permutability follows. A reducible free-field counterexample shows why an arbitrary momentum-conserving family need not itself commute.

The paper states the normalization and locality assumptions explicitly. Section 11 explains why the transparent critical manifold requires the same bulk potential up to a field shift, and what remains to be established for genuinely different theories. Appendix A retains the spatial Hamilton–Jacobi interpretation under its geometric assumptions. The theorem concerns the bulk hierarchy, without asserting a corrected higher-charge hierarchy for a fixed point defect.

The earlier [structural proof note](structural_type_I/proof.md) and its [verification guide](structural_type_I/README.md) remain as supporting material. The replaced manuscript is preserved verbatim in [history](history/README.md), so the original referee reports can still be read against their target.

The earlier [Theorem D reconstruction](theorem_D_reconstruction/proof.md), with its [scope guide](theorem_D_reconstruction/README.md), remains available. It supplies a separate scalar proof, an explicit scalar Bianchi formula, a corrected KdV Gardner construction, and a general spatial Hamilton–Jacobi argument under explicit regularity and geometric assumptions.

**The unrestricted Theorem D remains unproved. Neither complete theorem is formalized in Lean. Both new written proofs await independent mathematical review.** The separate Lean project verifies specified differential-ring identities and includes a nonzero derivation model; its precise limits are documented alongside the scalar reconstruction. Parameter series are formal, with no assertion of convergence.

## Verification

From the repository root:

```sh
python3 textbook_code/defect_integrability_structural/checks.py
python3 textbook_code/defect_integrability_structural/paper_checks.py
python3 defect-integrability/theorem_D_reconstruction/verify.py
```

The structural proof's [recorded output](structural_type_I/verification.txt) contains 30 exact finite symbolic checks, including four nonlinear local currents and the Poisson bracket of two nontrivial higher charges in a coupled two-component example. Its massive local-functional lemma and all-orders arguments are written proofs, not machine-certified results.

Twelve further [paper checks](structural_type_I/paper_verification.txt) cover the three-component derivations, the spatial Hamiltonian and defect-generating signs, shifted transparency, and the massless obstruction to rigidity.

The scalar reconstruction's [recorded output](theorem_D_reconstruction/verification.txt) includes its symbolic checks, Lean build, and theorem-dependency audit. The structural continuation does not modify that project.

## Earlier drafts and reports

These files preserve the development and review history. Claims in them of a universal proof or complete formalization are not established by either reconstruction.

- [Superseded research paper](history/defect_integrability_paper_pre_structural.md)
- [Conjecture report](corrigan_zambon_conjecture_report.md)
- [First referee report](referee_report_theorem_D.md) and [author response](response_to_referee_theorem_D.md)
- [Lean referee report](lean_referee/report.md), [author response](lean_referee/response.md), and [second referee report](lean_referee/report2.md)
- [Earlier Lean project](../lean/README.md)

## Integration

The scalar reconstruction replaces unsupported scalar steps with explicit derivations and independently written exact checks: the full sewing recursion, the equal-time generator, permutability, and functional independence. It replaces the failed KdV density construction and supplies generic-ring Lean lemmas with a consistent nonzero derivation model.

The structural continuation independently rederives the constant Type-I momentum constraints and supplies the missing temporal generator, commutation, and independence arguments under its stated hypotheses. It rejects automatic permutability for an arbitrary invertible leading defect Hessian, with an exact counterexample. Its proof of commutation uses bulk irreducibility to remove that obstruction and uses positive masses and analyticity to justify the upgrade from quadratic to full charges.

Neither reconstruction accepts the earlier unrestricted integrability or complete-formalization claims. The earlier drafts, responses, reports, and Lean project are preserved for comparison. No book theorem labels are changed.

The corrected paper incorporates the structural proof in place of the earlier universal claims. It retains the spatial symplectic argument as a conditional geometric lemma, supplies the full proof of both sewing equations and the quadratic-part rigidity lemmas, and separates the demonstrated bulk theorem from the open heterogeneous and Type-II extensions. Its theorem statements still await independent mathematical review.
