# General framework: momentum conservation, kinematic symmetry and integrability

This directory rescues the general results of the [pre-structural paper](../history/defect_integrability_paper_pre_structural.md) and of the [conjecture report](../corrigan_zambon_conjecture_report.md). The aim is general theorems that cover every observed case in Section 1.2 of that report. It complements, and does not replace, the [structural paper](../defect_integrability_paper.md). That paper proves a deeper theorem for one class: massive relativistic Type-I defects.

## Contents

- [paper.md](paper.md) — the rescued paper, self-contained, with a complete bibliography. Start here.
- [guide.md](guide.md) — a reader's guide to the paper: the strategy; the central argument first in classical mechanics; a toolkit of the variational calculus it uses; the proofs move by move with sine-Gordon as a running example; and a catalogue of the counterexamples.
- [conjecture_report.md](conjecture_report.md) — the rescued report: literature record, case inventory with what is established, Conjecture 2 restated, Theorems A–C kept with a status note.
- [response_to_report2.md](response_to_report2.md) — how each point of the [second Lean referee report](../lean_referee/report2.md) is addressed.
- [response_to_reports_20261020.md](response_to_reports_20261020.md) — verification and integration of the reports on the written proofs: [referee_report.md](referee_report.md), [referee_report_codex_20261020.txt](referee_report_codex_20261020.txt) and its second and third rounds, [referee_report_codex_20261020_round2.txt](referee_report_codex_20261020_round2.txt) and [referee_report_codex_20261020_round3.txt](referee_report_codex_20261020_round3.txt).
- [checks/](checks/) — exact symbolic checks (Python 3, SymPy). One `PASS` or `FAIL` line per check.
- [lean/](lean/) — Lean 4 (v4.35.0, core only) checks of the final algebraic step of several lemmas, over an arbitrary commutative ring. The substantive inputs (Euler-operator chain rule, Helmholtz self-adjointness, the nonresonance step of the rigidity lemma) enter as hypotheses. **Theorem 8.1 is not formalised**; see [lean/README.md](lean/README.md) for the exact scope.
- [verification.txt](verification.txt) — recorded output of all checks and the Lean audit.

## What is proved, and what is assumed

| Step | Statement | Status |
|---|---|---|
| Momentum conservation ⇒ Bäcklund relation | Theorem 3.3: any finite-order bulk, any local defect functional (auxiliary fields and multipliers allowed), under the injectivity condition (I) | written proof; final linear-algebra step in Lean, with identities (3.5) as hypotheses; direct exact check on three defects |
| Bäcklund relation ⇒ conserved generating density | Lemma 4.1, Propositions 4.2–4.3, Lemma 5.2: needs an affine conservation law of the bulk (boost, Galilean boost, dilation, time-linear shift) | written proof; closure identity in Lean; every observed bulk checked |
| Family ⇒ local conservation laws | Lemma 6.2, Theorem 6.4: needs a family with a regular transparent limit (formal branch) | written proof; branches checked for sine-Gordon, NLS, KdV, mKdV, Boussinesq |
| Conservation laws ⇒ commuting independent charges | Theorems 7.3–7.4: needs a constant Poisson operator, nonresonant dispersion, and conditions (L), (L′) on the linear parts of the charges; no Bianchi permutability | written proof; induction over degrees in Lean, with the nonresonance step as a hypothesis; nonresonance checked |
| Momentum conservation ⇒ the family | Propositions 8.2–8.3, Theorem 8.4: relativistic Type I with constant kinetic coupling, given a nondegenerate transparent point; the family and its formal branch follow | written proof (restating the structural paper); identities checked for a general skew coupling with three fields; hypotheses checked for sine-Gordon and $a_2^{(1)}$ Toda. **Open** in general (paper, Section 10) |

## Reproducing

```sh
cd defect-integrability/general_framework/checks
python3 check_balance.py
python3 check_tangency.py
python3 check_kinematics.py
python3 check_scope.py
python3 check_type1_family.py
python3 check_guide_example.py     # the examples of guide.md
python3 check_hierarchy.py          # or a subset, e.g. kdv:6 sg:5 nls:3 mkdv:6 bsq:5 tz:3
cd ../lean
lake build
lake env lean Audit.lean
```

Or run everything and rewrite `verification.txt` with `./run_checks.sh` (about half an hour). Tested with Python 3.12.3, SymPy 1.14.0 and Lean 4.35.0. `check_hierarchy.py` takes several minutes per model.

## Scope of the machine checks

The scripts check identities and hypotheses on the defect functionals published by Corrigan, Zambon and collaborators, transcribed in the scripts. A balance check passing also confirms the transcription. The hierarchy checks verify conservation of each computed $Q_n$ to the stated finite order; they do not prove all orders. The Lean files check the algebra of each general lemma with the variational and analytic inputs as named hypotheses; they do not formalise the variational calculus or the Fourier analysis. An independent check of the written proofs on 20 October 2026 found several statements that were false in the generality claimed; the corrections, and the examples that show which hypotheses are needed (`checks/check_scope.py`), are recorded in [response_to_reports_20261020.md](response_to_reports_20261020.md). The corrected statements await a second independent check.
