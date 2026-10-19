# Structural continuation of PR #32

[The proof](proof.md) keeps the multicomponent bulk potential unspecified and derives infinitely many independent commuting local charges from a momentum-conserving Type-I defect under explicit analytic, massive-vacuum, irreducibility, and transparency hypotheses.

The key additional step is a proof that a local conserved functional near a massive analytic vacuum is determined by its quadratic part. This upgrades commuting linearized parameter generators to full involution. Formal Bäcklund permutability follows as a conclusion.

The proof also gives a reducible free-field example whose defect family does not commute. This identifies a real limitation of an unconditional permutability argument, without contradicting integrability of that free bulk.

Status: complete written argument, with finite exact symbolic checks; **awaiting independent adversarial review**. It is not a proof of the original unrestricted conjecture and has not been formalized in Lean.

From the repository root, run:

```sh
python3 textbook_code/defect_integrability_structural/checks.py
```

The output is recorded in [verification.txt](verification.txt). See the [check index](../../textbook_code/defect_integrability_structural/README.md) for coverage. The proof's Sections 1 and 10 state its limits.
