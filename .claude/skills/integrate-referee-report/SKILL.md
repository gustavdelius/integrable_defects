---
name: integrate-referee-report
description: Independently verify and integrate a referee report on integrable-defects papers, symbolic checks, or Lean formalizations. Use when the editor asks to act on review findings; preserve the report and record the disposition and evidence for each item.
---

# Integrate a referee report

A report is a set of claims to check, not an edit list. Follow `AGENTS.md` and the current assignment. Integration must be assigned explicitly; being the referee or receiving a report does not itself authorize editing the research.

## Preserve and locate the evidence

- Confirm that the report is finished. Identify the reviewed revision and match passages by content rather than assuming old line numbers still apply.
- Preserve the received report unchanged, apart from a later appended integration record. If committing is authorized, a separate "report as received" commit makes that distinction clear. Otherwise retain the received file and record its revision or hash before editing.
- Preserve useful referee scripts and outputs under `briefs/<report-name>_scripts/`, excluding tool caches and unrelated downloads. Rerun from a scratch copy if they write relative outputs. A rerun checks reproducibility; it is not independent verification.
- Identify files another referee is reviewing and leave them unchanged. Record any necessary changes to those files as pending.

## Verify before editing

For each substantive finding, re-derive the result, write a short independent calculation from the definitions, or inspect the exact literature passage as appropriate. Do not reuse the author's or referee's implementation of the disputed step as your own evidence. Translate signs and normalizations explicitly.

Check whether a claimed omission is already addressed elsewhere, whether the finding applies to the current revision, and whether its proposed correction follows from its own evidence. Recompute claimed publication errors from the source definitions. Independently assess every proposed theorem upgrade; finite checks and identities between conjectured expressions do not close proof gaps.

For Lean findings, examine the actual definitions and theorem hypotheses, not just the build result. Keep the distinction between an axiom-free conditional lemma and a proof of the substantive hypothesis it assumes. Do not resolve an incomplete proof by introducing `sorry`, an axiom, or an assumption equivalent to the desired conclusion.

Classify each finding as **verified**, **modified**, **rejected**, or **unresolved**, and give the reason. An unresolved finding must not be silently treated as correct.

## Integrate supported corrections

- Edit only within the assignment. Keep notation and prose consistent with the affected paper. Check other current documents that repeat the corrected claim, including the guide, applicable README scope statements, and formalization handoff.
- Add or revise the checks that substantiate a computational correction and update their index. Preserve historical manuscripts and received reports; describe their supersession rather than retroactively rewriting them.
- For a new or strengthened theorem, require a complete written proof and flag any part still awaiting an independent referee pass. Report assumptions introduced, conclusions weakened, and novelty claims withdrawn.
- For a large task, keep `briefs/<task>_checkpoint.md` current after each item. If delegation is expressly authorized, adapt [agent-prompt.md](agent-prompt.md); otherwise work in the current session. The template is not permission to spawn an agent.

## Record and validate

Append `## Integration` to the report, with the date and reviewed/current revisions. Use a table of finding, disposition, independent evidence and output, files changed, and remaining work. Preserve integration scripts with an `integration_` prefix in the report's scripts directory. A local example is `briefs/referee_general_framework_82_report.md` and its scripts directory.

Run affected symbolic checks and dependent checks if shared helpers changed. For changed Lean code, build the relevant pinned project and run its audit where present; inspect printed dependencies as well as the exit status. Distinguish passes from timeouts, partial runs, and checks not run. Check links and `git diff --check` for documentation changes. No textbook renderer or chapter-reference checker is needed.

Update the relevant scope statement and checkpoint, then commit or publish only within the current authorization. The final summary identifies corrections, rejected or unresolved findings, validation limits, and any strengthened claims still awaiting review.
