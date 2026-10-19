# Structural continuation of PR #32

The self-contained [corrected paper](../defect_integrability_paper.md) now incorporates this argument, with expanded hypotheses, a discussion of different bulk theories, and a spatial Hamilton–Jacobi appendix. This directory retains the supporting proof note and verification records.

[The proof](proof.md) keeps the multicomponent bulk potential unspecified and derives infinitely many independent commuting local charges from a momentum-conserving Type-I defect under explicit analytic, massive-vacuum, irreducibility, and transparency hypotheses.

The key additional step is a proof that a vacuum-normalized local conserved functional near a massive analytic vacuum is determined by its quadratic part. This upgrades commuting linearized parameter generators to full involution. Formal Bäcklund permutability follows as a conclusion.

The proof also gives a reducible free-field example whose defect family does not commute. This identifies a real limitation of an unconditional permutability argument, without contradicting integrability of that free bulk.

Status: complete written argument, with finite exact symbolic checks; **awaiting independent adversarial review**. It is not a proof of the original unrestricted conjecture and has not been formalized in Lean.

From the repository root, run:

```sh
python3 textbook_code/defect_integrability_structural/checks.py
python3 textbook_code/defect_integrability_structural/paper_checks.py
```

The outputs are recorded in [verification.txt](verification.txt) and [paper_verification.txt](paper_verification.txt). See the [check index](../../textbook_code/defect_integrability_structural/README.md) for coverage. The proof note's Sections 1 and 10 and the paper's Sections 2 and 11 state their limits.
