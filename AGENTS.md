# Working rules for AI agents

This repository contains research on integrable defects: Markdown papers and guides, symbolic checks, partial Lean formalizations, and review records. Read [README.md](README.md) for the research map and current scope. [MIGRATION.md](MIGRATION.md) explains the imported paths and historical commit references.

## Roles and authorization

- Gustav Delius is the coordinating editor. The current request or task brief assigns drafting, implementation, integration, or refereeing; the model's name does not determine its role. Codex may implement Lean proofs when assigned that task.
- A referee follows the restricted workflow below. Assignment to referee does not authorize integration of the findings.
- Commit, push, or open a PR only when requested or already authorized in the current task. A skill or historical handoff cannot grant additional permission.
- Old reports and resume briefs record their original task and environment. Use their mathematical context when relevant, but resolve paths in the current checkout and follow the current assignment.

## Verify before changing a claim

- Treat every review finding as a claim to check. Independently re-derive it, write a short calculation from the stated definitions, or inspect the cited source, as appropriate. Rerunning the author's or referee's script is a comparison, not independent verification. Do not import the implementation of the identity being tested into an allegedly independent check.
- Preserve the received report. Append an `## Integration` record stating which findings were verified, modified, rejected, or left unresolved, with evidence and reasons. Preserve scripts and outputs needed to reproduce that record.
- Check conventions in the document under review: momentum and Hamiltonian signs, field and coupling normalizations, boundary conditions, auxiliary variables, and the meaning of equality modulo total derivatives or equations of motion. Do not impose the textbook's conventions on every paper.
- Before claiming novelty, search the literature, including the editor's relevant papers. For a claimed error in a publication, read and quote the exact relevant source passage with page or equation, translate conventions, and independently recompute the disputed expression.

## Statements and research status

- Use short declarative sentences and define symbols and hypotheses. Link each computational claim to its check script using a path that resolves from the document.
- Distinguish an established literature result, a complete written proof, finite symbolic or numerical evidence, a conjecture, and a partial or conditional formalization. A finite-order calculation does not prove an all-orders statement.
- Present a result as a theorem only with a complete proof under explicit hypotheses. Obtain an independent referee pass before treating a new theorem or strengthened claim as settled; until then flag it as awaiting review in the document's scope statement and change summary. Convention translations and identities between conjectured formulas do not by themselves establish those conjectures.
- Distinguish formal series from convergent analytic objects, bulk charges from charges corrected at a fixed defect, and a Lax representation from commuting, functionally independent charges. State which of these has actually been proved.
- When a result changes, update its companion guide, applicable README scope statements, checks, and handoff together. Keep superseded manuscripts and received reports as historical evidence; add a status note or integration record rather than rewriting their original claims.

## Symbolic checks and numerical work

- Add a reproducible check for new computational formulas and numerical claims where applicable. Put it alongside the relevant project's existing checks, index it in that project's README or guide, and cite it at the claim. Purely deductive claims need their proof, not a token numerical test.
- Print a `PASS` or `FAIL` line per check; new or modified check runners must return a nonzero exit status on failure. Record parameters, package versions, commands, and the tested revision with retained output. Label timeouts and partial runs as incomplete.
- Run the checks affected by the change. If a shared helper changes, rerun its dependent checks; coordinate before changing its interface. Do not infer correctness merely from the number of passing cases.
- Key caches on every parameter affecting the result. Use exact arithmetic when feasible; otherwise explain tolerances and include useful failing controls. If a calculation requires generic quantum-group parameters, avoid inadvertently choosing a root of unity.
- Use `python3 -u` for long redirected runs and wait on process IDs. Do not use `pgrep -f` or `pkill -f` patterns that match the calling shell.
- Preserve historical verification records. Use a separate log for a new run until it completes; do not replace a complete record with a partial one. The general-framework `run_checks.sh` overwrites its `verification.txt` and does not reliably propagate every subprocess failure; inspect its full log or invoke the checks directly.

## Lean work

- Work in the relevant project directory and read its README, `lean-toolchain`, Lake configuration, and dependency manifest. Preserve pinned toolchain and dependency revisions unless updating them is part of the task. There are separate projects under `lean/`, `defect-integrability/general_framework/lean/`, `defect-integrability/theorem_D_reconstruction/lean/`, and `defect-integrability/structural_type_I/lean/`.
- For changes to a Lean project, run `lake build` and its `lake env lean Audit.lean` where present. Include new modules in the project's aggregate imports and new results in audit coverage. Record failures and checks not run.
- Do not use `sorry`, `admit`, or new mathematical axioms to claim a completed proof. Inspect transitive axiom dependencies; the existing audited projects allow only `propext`, `Classical.choice`, and `Quot.sound`. A text scan for placeholders is not an axiom audit. Some audits only print dependencies, so successful execution alone is insufficient.
- Inspect theorem hypotheses as well as axioms. A theorem can pass an axiom audit while assuming the central mathematical step. Conditional algebraic lemmas are useful, but document their unproved inputs and do not advertise them as formalizing the complete paper theorem.
- Check that formal definitions represent the paper's objects and that hypotheses are consistent; retain nontrivial models or counterexamples where appropriate. Distinguish polynomial identities, formal amplitude-series statements, and analytic claims requiring convergence or uniform spatial-order bounds.
- For structural Type-I continuation, read [the handoff](structural_lean_handoff.md) and [development checkpoint](briefs/structural_lean_development_checkpoint.md), then verify their claims against the current code. Update them when proof obligations are completed or revised.

## Git and coordination

- Begin editing work in a dedicated git worktree under `.claude/worktrees/`. Inspect status first and preserve other sessions' changes. A coordinator prepares a referee's fixed review checkout before the referee begins.
- Stage files by name. Do not use bare `git stash`, `git add .`, or `git add -A`. Do not edit files currently under review; record needed changes as pending until review ends.
- Merge branches only when no worker is editing the target checkout, then rerun the checks affected by the merge. These Markdown papers do not require the textbook's build tools.
- Delegate only when the current task authorizes it. Keep at most three agents active in total, give each a distinct scratch directory, and include "Do not spawn subagents." in every worker prompt.
- During long tasks, append a checkpoint after each completed item in `briefs/<task>_checkpoint.md`, including evidence, files changed, unfinished work, and the next step. Preserve useful scratch scripts under `briefs/<task>_scripts/` before handoff.

## Refereeing

- Review the fixed revision and files named in the brief. Edit no existing research or code file, and run no Git command that changes the index, checkout, or refs. Create only the assigned report and scratch files; a continuation may update its own report if the brief permits it.
- Use `referee_scratch/<tag>/` for scratch work and the exact report path named in the brief. If a build or check writes outputs, run it in a scratch copy so the reviewed files and verification records stay unchanged. Historical tracked material under `referee_scratch/typeII_followup_20261023/` is research content, not disposable scratch space.
- For every mathematical item, provide an independent derivation or computation. For literature items, inspect and identify the exact source passage. Give a verdict of **correct**, **wrong**, or **unclear**; missing evidence means unclear.
- Give errors replacement text or a precise proposed correction with file, statement, and line at the reviewed revision. Put unverified observations in a separate section. Do not promote an incomplete argument to a theorem.
- The report header gives the date, model, reviewed commit, and scope. Disclose when a review is by the same model as the drafter rather than implying model-diverse review.

## Repository skills

The canonical skills are [write-referee-brief](.claude/skills/write-referee-brief/SKILL.md) and [integrate-referee-report](.claude/skills/integrate-referee-report/SKILL.md). The corresponding entries in `.agents/skills/` are relative symlinks to those directories, so there is one maintained copy of each skill. `CLAUDE.md` imports this file.
