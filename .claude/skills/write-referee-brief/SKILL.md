---
name: write-referee-brief
description: Write a self-contained referee brief for an integrable-defects paper, calculation, or Lean formalization when independent mathematical review is requested. Specify a fixed revision, conventions, evidence requirements, and report destination.
---

# Write a referee brief

Read the repository's `AGENTS.md` and the current task. Produce a brief that a referee can use with only this repository and the identified source literature. Writing a brief does not authorize launching a referee or changing the research.

## Establish the target

- Inspect the actual claims, relevant checks, project README, and review history. Identify the files and commit to review; distinguish completed results from the drafter's proposed steps and known gaps.
- Use a fixed committed revision. If relevant work is uncommitted and committing is not authorized, identify the draft and its patch or file hashes explicitly; do not describe it as a reproducible committed state.
- Choose `briefs/referee_<topic>.md`, an exact report destination such as `briefs/referee_<topic>_report.md`, and a fresh scratch tag. Do not overwrite an earlier report. Record files reserved for review in the task checkpoint and tell the editor.
- A useful local model is `briefs/referee_general_framework_82.md`, with its accompanying report. Adapt its mathematical specificity; its old machine paths and textbook instructions are historical.

## Include in the brief

1. **Role and target.** Assign an adversarial mathematical-physics referee. Name the repository, fixed revision, document sections or Lean declarations, and prepared review checkout if one exists. Do not select a model or launch another agent unless requested.
2. **Write restrictions.** State that other agents may be working nearby; the referee must not edit existing research files or run Git commands changing the index, checkout, or refs. Include "Do not spawn subagents." Allow writes only to the named scratch directory and report. Require a scratch copy for checks that write build artifacts or overwrite tracked logs.
3. **Context and conventions.** Explain what changed and the current claim status. Spell out the applicable Lagrangian, momentum/sewing signs, normalizations, boundary conditions, auxiliary fields, and whether identities hold off shell, on solutions, or modulo total derivatives. For formalization, identify the mathematical objects and substantive hypotheses of the declarations under review.
4. **Reading and reproduction.** Give repository-relative paths, statements, exact commands and working directories, known runtimes, and source-paper identifiers with pages or equations. Distinguish existing verification records from new runs. Do not assume local paper downloads or tools exist on the referee's machine.
5. **Evidence rule.** Require an independent derivation or script from the definitions for each mathematical item. Existing scripts are comparison material, not independent evidence. Require inspection of exact source passages for literature claims. Any item without adequate evidence receives **unclear**.
6. **Prioritized questions.** For each item, quote or precisely identify the claim and hypotheses, ask for the calculation or proof audit needed to decide it, and ask whether its status is justified. Prioritize strengthened claims, suspected gaps, publication corrections, and claims still awaiting review. Include prior art and fidelity of citations where relevant.
7. **Report format.** Require date, model, reviewed revision, and scope; then per-item **correct / wrong / unclear**, evidence with reproducible output, and corrections with file and line. End with unverified observations separately. Require disclosure if the reviewer uses the same model as the drafter.

For Lean review, ask the referee to examine definitions, consistency models, all theorem hypotheses, aggregate imports, and transitive axiom dependencies. A successful build without `sorry` does not show that a conditional lemma proves the paper's theorem. Ask explicitly about the distinction between formal and convergent series when it matters.

## Finish

Check that every named file, declaration, and local link exists, commands run from the specified project, and each question can be answered from the supplied context. Do not run the full scientific suite merely to write a brief. State any missing evidence or inaccessible source. Commit or publish only within existing authorization; otherwise leave the brief ready for review. Integrating a later report is a separate task covered by `integrate-referee-report`.
