# Migration from affine_toda

23 October 2026.

The general defect research was extracted from `gustavdelius/affine_toda` into `gustavdelius/integrable_defects` at the editor's request.

| Source | Original revision |
|---|---|
| PR #32, structural paper and partial formalizations | `595fd1540aeef57b7145ed616cab42c8aab23ea9` |
| PR #35, general framework including Gardner and Miura additions | `4ae0994c57c729d2f214e9c4fa2198ddfd45f180` |
| Local continuation of #35, Section 8.2 report and integration | `a744c789c15ee659e67abd33d4480308360c6198`, `8b902984ce5e0ea4c5c07adb190457fa07514f77` |
| PR #36, Type-II reduction note and checks | `b490a900d176d2da5b60cab65768e28d2b66770d` |

Git fast-export/fast-import retained the history of the selected research paths, including original authors, dates and commit messages. Filtering changes commit hashes and omits unrelated textbook history. Original revisions in dated reports refer to the source repository.

PR #35 includes #32. Its published branch and local continuation had diverged. Both were retained and merged in this repository. Three text conflicts in the general-framework paper and guide were resolved by retaining the local referee corrections and appending the published Gardner/Miura additions. No new mathematical argument was introduced by the migration.

The Type-II branch was then merged as a separate history. The imported research paths keep their original names. The only subsequent change within the imported research documents converts six relative links to textbook files in the general-framework conjecture report into links to the original source revision. The archived pre-structural manuscript remains byte-for-byte unchanged. An old referee report retains an unavailable absolute link to its original external review artifact; it is part of the historical record, not a runtime dependency.

The root README, requirements file, ignore rules and this migration record are new. The code license was copied unchanged from the source repository. No book chapters, textbook lecture notes, figures or publishing workflow were imported. Source PRs #31 and #34 are outside this migration.

The source checkout's uncommitted `general_framework/verification.txt` was an incomplete rerun and was not imported. The committed historical record was retained. Other uncommitted and untracked files in the source checkout were left untouched.

## Validation

Run from the extracted repository with Python 3.12.3, SymPy 1.12 and Lean 4.35.0. Historical verification files inside the research directories have not been overwritten.

| Python checks | Result |
|---|---|
| Structural `checks.py` / `paper_checks.py` | 30 / 12 PASS; both exit 0 |
| Type-II `check_d4_reduction.py` / `check_lax.py` | 12 / 5 PASS; both exit 0 |
| General-framework `check_tangency.py` | 3 PASS; exit 0 |
| `check_kinematics.py` | 15 PASS; exit 0 |
| `check_scope.py` | 43 PASS; exit 0 |
| `check_type1_family.py` | 24 PASS; exit 0 |
| `check_guide_example.py` | 15 PASS; exit 0 |
| `check_gardner.py` / `check_miura.py` | 7 / 8 PASS; both exit 0 |
| Scalar reconstruction `checks.py` / `scalar_checks.py` | 14 / 8 PASS; both exit 0 |
| General-framework `check_balance.py` | Incomplete: stopped at the 240-second limit after four PASS lines (sine-Gordon, Liouville/free, a2 Toda and Tzitzeica); no FAIL lines |

The 13 completed Python scripts report 196 PASS lines and no FAIL lines. The additional four PASS lines in the timed-out script do not constitute a successful full run.

`lake build` and `lake env lean Audit.lean` pass in the general-framework and scalar reconstruction projects. The historical root `lean/` project also builds successfully. The mathlib-based structural project, `check_symbols.py`, the hierarchy scans and historical referee scripts were not rerun for this migration.

File checks confirm that all 127 selected research files are present. Of those, 123 match at least one imported source revision byte for byte. The four others are the merged general-framework README, paper and guide, and the conjecture report with repaired external links. All imported Python files compile; new README links to local files resolve; `git diff --check` passes; the archived manuscript is byte-for-byte unchanged. No `.qmd` files or textbook lecture directories are included.
