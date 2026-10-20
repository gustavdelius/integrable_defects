# General framework: momentum conservation, kinematic symmetry and integrability

This directory rescues the general results of the [pre-structural paper](../history/defect_integrability_paper_pre_structural.md) and of the [conjecture report](../corrigan_zambon_conjecture_report.md). The aim is general theorems that cover every observed case in Section 1.2 of that report. It complements, and does not replace, the [structural paper](../defect_integrability_paper.md). That paper proves a deeper theorem for one class: massive relativistic Type-I defects.

## Contents

- [paper.md](paper.md) — the rescued paper. Start here.
- [conjecture_report.md](conjecture_report.md) — the rescued report: literature record, case inventory with what is established, Conjecture 2 restated, Theorems A–C kept with a status note.
- [response_to_report2.md](response_to_report2.md) — how each point of the [second Lean referee report](../lean_referee/report2.md) is addressed.
- [checks/](checks/) — exact symbolic checks (Python 3, SymPy). One `PASS` or `FAIL` line per check.
- [lean/](lean/) — Lean 4 (v4.35.0, core only) formalisation of the algebraic cores of the general lemmas, over an arbitrary commutative ring.
- [verification.txt](verification.txt) — recorded output of all checks and the Lean audit.

## What is proved, and what is assumed

| Step | Statement | Status |
|---|---|---|
| Momentum conservation ⇒ Bäcklund relation | Theorem 3.3: any finite-order bulk, any local defect functional (auxiliary fields and multipliers allowed), under the injectivity condition (I) | written proof; algebraic core in Lean |
| Bäcklund relation ⇒ conserved generating density | Lemma 4.1, Propositions 4.2–4.3, Lemma 5.2: needs an affine conservation law of the bulk (boost, Galilean boost, dilation, time-linear shift) | written proof; Lean core; every observed bulk checked |
| Family ⇒ local conservation laws | Lemma 6.2, Theorem 6.4: needs a family with a regular transparent limit (formal branch) | written proof; branches checked for sine-Gordon, NLS, KdV, mKdV, Boussinesq |
| Conservation laws ⇒ commuting independent charges | Theorems 7.3–7.4: needs a constant Poisson operator and nonresonant dispersion; no Bianchi permutability | written proof; inductive structure in Lean; nonresonance checked |
| Momentum conservation ⇒ the family | — | **open** in general (paper, Section 10); proved for massive relativistic Type I in the structural paper |

## Reproducing

```sh
cd defect-integrability/general_framework/checks
python3 check_balance.py
python3 check_tangency.py
python3 check_kinematics.py
python3 check_hierarchy.py          # or a subset: sg nls kdv mkdv bsq
cd ../lean
lake build
lake env lean Audit.lean
```

Tested with Python 3.12.3, SymPy 1.14.0 and Lean 4.35.0. `check_hierarchy.py` takes several minutes per model.

## Scope of the machine checks

The scripts check identities and hypotheses on the defect functionals published by Corrigan, Zambon and collaborators, transcribed in the scripts. A balance check passing also confirms the transcription. The hierarchy checks verify conservation of each computed $Q_n$ to the stated finite order; they do not prove all orders. The Lean files check the algebra of each general lemma with the variational and analytic inputs as named hypotheses; they do not formalise the variational calculus or the Fourier analysis. All written proofs await independent review.
