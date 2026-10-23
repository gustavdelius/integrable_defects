# Task template: integrate a referee report

Use this template only when the editor has authorized an integration worker. Fill in the bracketed fields and remove inapplicable instructions before handing it over. Do not select a model or spawn another agent merely because this template exists.

---

You are integrating a referee report on research in `integrable_defects`. Read `AGENTS.md` in the assigned checkout and `.claude/skills/integrate-referee-report/SKILL.md` first. The current assignment authorizes integration of the listed findings, not unrelated research.

Do not spawn subagents.

## Workspace and scope

- Worktree and branch: [prepared checkout and branch]. Run commands there; do not edit another checkout.
- Report: [repository-relative report path], reviewed revision [commit]. Its received contents are preserved at [revision or hash].
- Research under review: [paper sections, script paths, Lean declarations].
- Editable files: [explicit list, including companion guides and scope statements that need consistency changes].
- Files reserved for another reviewer: [list, or none]. Record needed changes there as pending.
- Scratch directory: `referee_scratch/[unique-tag]/`.
- Persistent evidence: `briefs/[report-name]_scripts/`, using `integration_` prefixes for your scripts and output.
- Checkpoint: `briefs/[task]_checkpoint.md`.
- Git authorization: [whether named-file commits are authorized]. Do not push or open a PR unless separately included in the assignment.

Stage only named files. Do not use bare `git stash`, `git add .`, or `git add -A`. Preserve unrelated changes.

## Read first

1. [Project README and current scope statement].
2. [Relevant definitions, conventions, and complete target argument].
3. The report, its scripts, and [identified source papers with pages/equations].
4. [Current task handoff or checkpoint, if applicable].

Old line numbers refer to the reviewed revision. Match by content and check whether later work already resolves a finding.

## Findings to assess

[List report items, their priorities, and the editor's scope constraints. Do not preassign verdicts.]

For each finding, independently derive the result or write a calculation from the definitions before changing the claim. Do not import the disputed implementation from the author or referee. For literature findings, inspect the exact source passage and translate conventions. A script rerun establishes reproducibility only.

Classify each item as verified, modified, rejected, or unresolved, with evidence. For Lean, inspect theorem hypotheses and transitive dependencies; a build does not prove assumptions. Do not replace an unproved step with an axiom, placeholder, or equivalent assumption and then call it complete.

After each item, update the checkpoint with the verdict, evidence, files changed, unfinished work, and next step. Preserve the received report and append an `## Integration` record. Keep archived drafts unchanged.

## Validation and handoff

- Run [affected check commands, with working directories and expected runtime]. Record command output and exit status; report timeouts and omitted checks explicitly.
- If Lean code changes, build the applicable pinned project and run its audit where present; inspect the output for unapproved dependencies and incomplete coverage.
- Update affected guides, scope statements, script indexes, and handoffs within the editable-file list. Flag anything requiring an out-of-scope edit.
- Check changed links and run `git diff --check`.
- In the final report, list dispositions, changed claims and assumptions, validation results and limits, and any theorem upgrades still awaiting independent review. Include paths to the integration record, persistent evidence, and checkpoint.
