# Integrable defects

Research papers, explanatory guides, symbolic calculations and partial Lean formalizations on defects in integrable field theories. The central question is why requiring a defect to conserve momentum so often produces a Bäcklund transformation and selects an integrable bulk theory.

The scope includes relativistic Type-I and Type-II defects, sine-Gordon and Toda theories, nonlinear Schrödinger, KdV, mKdV, Boussinesq and Gardner equations, and defects joining different bulk theories.

**Coordinating editor:** Gustav Delius.

This research grew out of the [affine Toda textbook](https://github.com/gustavdelius/affine_toda). It now lives separately because its questions and methods extend beyond affine Toda theory. The textbook's defects chapters and their lecture notes remain in that repository.

## Start reading

| Material | Where to start |
|---|---|
| General framework: momentum balance, Bäcklund relations, generating densities and conditions for commuting independent charges | [Reader's guide](defect-integrability/general_framework/guide.md), [paper](defect-integrability/general_framework/paper.md), and [scope and review status](defect-integrability/general_framework/README.md) |
| Structural argument for massive analytic relativistic Type-I defects | [Paper](defect-integrability/defect_integrability_paper.md), [pedagogical companion](defect-integrability/defect_integrability_companion.md), and [reading guide](defect-integrability/README.md) |
| Can a defect join mKdV to KdV through the Miura map? | [Working note](defect-integrability/general_framework/miura_defect.md); related Gardner and fused-Miura calculations are in Section 9 of the general-framework paper |
| A one-auxiliary Type-II defect obtained by reduction of Bristow's D4 defect | [Reduction note and Lax checks](referee_scratch/typeII_followup_20261023/summary.md) |
| Earlier scalar reconstruction and spatial Hamilton–Jacobi argument | [Proof and scope](defect-integrability/theorem_D_reconstruction/README.md) |
| Development and review history | [Earlier manuscript](defect-integrability/history/README.md), [general-framework responses](defect-integrability/general_framework/response_to_reports_20261020.md), and [Section 8.2 referee report and integration](briefs/referee_general_framework_82_report.md) |

## Research status

These are working research documents, substantially developed with AI assistance from Claude, Codex and Gemini. Automated reviews and symbolic checks are recorded alongside the work; they do not replace independent mathematical review.

- The unrestricted claim that momentum conservation implies integrability remains open. The general-framework hierarchy theorem has explicit hypotheses, including a suitable family with a regular transparent limit and conditions on the charges and dispersion.
- The structural paper gives a written argument under its massive analytic Type-I hypotheses. Its complete theorem still awaits independent mathematical review and is not fully formalized in Lean. It concerns the bulk hierarchy; it does not establish convergence of the Bäcklund parameter series or a hierarchy of corrected higher charges for a fixed point defect.
- The general-framework paper has undergone several automated referee rounds and corrections. Its directory README identifies the scope of those reviews and the additions still awaiting another check.
- The Type-II note supplies an explicit reduction and a defect Lax representation. Novelty, Poisson commutativity and functional independence remain unresolved there.
- Historical manuscripts and their reports are retained to make the development traceable. Their stronger claims should be read against the current scope statements.

## Run the symbolic checks

Python 3 and SymPy are sufficient for the Python scripts. Existing verification records used Python 3.12 and SymPy 1.12 or 1.14.

```bash
git clone https://github.com/gustavdelius/integrable_defects.git
cd integrable_defects
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt

# Structural Type-I paper: 30 + 12 exact checks
python3 textbook_code/defect_integrability_structural/checks.py
python3 textbook_code/defect_integrability_structural/paper_checks.py

# Type-II reduction and Lax representation: 12 + 5 exact checks
python3 referee_scratch/typeII_followup_20261023/check_d4_reduction.py
python3 referee_scratch/typeII_followup_20261023/check_lax.py
```

For the general framework:

```bash
cd defect-integrability/general_framework/checks
python3 check_balance.py
python3 check_tangency.py
python3 check_kinematics.py
python3 check_scope.py
python3 check_type1_family.py
python3 check_guide_example.py
python3 check_gardner.py
python3 check_miura.py
python3 check_symbols.py
python3 check_hierarchy.py kdv:6 sg:5 nls:3 mkdv:6 bsq:5 tz:3
```

The symbol and hierarchy calculations can take several minutes or longer. The [general-framework guide](defect-integrability/general_framework/README.md) describes their coverage. Its `run_checks.sh` runs the Python suite and Lean checks and **rewrites that directory's `verification.txt`**. Inspect the log for errors and `FAIL` lines; the wrapper's exit status alone is not a success criterion. Committed verification records are dated evidence from earlier runs, not a claim that every check was rerun during the migration.

The scalar reconstruction has two Python check scripts, `checks.py` and `scalar_checks.py`, and a combined Python/Lean verifier, `verify.py`, in [its directory](defect-integrability/theorem_D_reconstruction/).

## Lean projects

Each project has its own `lean-toolchain` and Lake configuration. Install [Lean through elan](https://github.com/leanprover/elan), then run commands from the chosen project directory; the pinned toolchain is Lean 4.35.0. The structural project also pins mathlib and its dependencies, so its first build requires network access and substantially more setup than the core-only projects.

| Project | Scope |
|---|---|
| [Structural Type-I](defect-integrability/structural_type_I/lean/README.md) | Polynomial jet calculus, massive polynomial rigidity, formal amplitude-series rigidity and parts of the analytic finite-jet foundation. The analytic connection and complete structural theorem remain unfinished. |
| [General framework](defect-integrability/general_framework/lean/README.md) | Algebraic steps with substantive variational and analytic inputs supplied as hypotheses. The hierarchy theorem is not formalized. |
| [Scalar reconstruction](defect-integrability/theorem_D_reconstruction/README.md) | Specified differential-ring identities and a nonzero derivation model. |
| [Earlier project](lean/README.md) | Historical algebraic skeleton. Read it with the later referee reports and reconstructions. |

For example, from the repository root:

```bash
cd defect-integrability/general_framework/lean
lake build
lake env lean Audit.lean
```

The structural and scalar projects also provide `Audit.lean`. See the [structural handoff](structural_lean_handoff.md) and [resume brief](structural_lean_resume.md) for the unfinished formalization work. Their saved-workspace paths describe the original development environment.

## Repository layout and provenance

The original relative paths are retained so that the papers, scripts and review records remain connected. In particular, `textbook_code/` now holds only the structural paper's checks, and `referee_scratch/typeII_followup_20261023/` holds the committed Type-II note and scripts.

This repository imports the material from affine_toda PRs [#32](https://github.com/gustavdelius/affine_toda/pull/32), [#35](https://github.com/gustavdelius/affine_toda/pull/35) and [#36](https://github.com/gustavdelius/affine_toda/pull/36), together with the local Section 8.2 referee integration. Relevant Git history and author metadata are preserved, with new commit hashes after filtering out the textbook. See [MIGRATION.md](MIGRATION.md) for source revisions and validation.

PRs [#31](https://github.com/gustavdelius/affine_toda/pull/31) and [#34](https://github.com/gustavdelius/affine_toda/pull/34) belong to the textbook's lecture material and remain there. No Quarto installation or textbook checkout is needed to read these Markdown papers or run their Python checks.

## Feedback and licensing

For a mathematical correction, identify the document, statement and revision, and include a derivation or reproducible calculation where possible. Distinguish a finite symbolic check from an all-orders proof, and a conditional formalization from a proof of its hypotheses.

The imported code retains the [MIT license](LICENSE). Other imported material retains its existing rights and attribution; this migration does not relicense it. The [source project's licensing statement](https://github.com/gustavdelius/affine_toda#license) distinguishes code from book text and figures. Copyright in individual contributions remains with the applicable rights holders.
