# Resume the structural integrability Lean formalization

Continue the Lean formalization of Theorem 2.1 in the
[corrected paper](defect-integrability/defect_integrability_paper.md).
The user has authorized implementation of proofs, not merely refereeing.
This explicitly supersedes the repository's earlier referee-only restriction
for this task.

First read these files in order:

1. [Current handoff](structural_lean_handoff.md).
2. [Development checkpoint](briefs/structural_lean_development_checkpoint.md).
3. [Original setup and proof obligations](briefs/structural_lean_checkpoint.md).

Resolve paths relative to this file's directory, at the repository root.
Work in the existing Lean project:

```text
defect-integrability/structural_type_I/lean
```

When resuming in the saved workspace, use its existing checkout under
`.claude/worktrees/lean-structural` and reuse the installed Lean and pinned
mathlib. In a fresh environment, follow the pinned setup only as needed.
The current handoff and
development checkpoint are authoritative about completed work and remaining
obligations; older setup notes may describe historical limitations.

As of 20 October 2026:

- Polynomial free massive rigidity is proved.
- Formal nonlinear amplitude-series rigidity is proved.
- Actual analytic finite-jet functions, convergent polynomial Taylor
  coefficients, and analytic Euler operators are constructed.
- The full analytic rigidity lemma and structural theorem are unfinished.

The next task is to prove that Taylor expansion commutes with actual
partial, spatial, and Euler differentiation. Then construct analytic
evolution and transport analytic conservation into the formal convolution.
Combine this with formal rigidity and Euler exactness, construct the needed
analytic local-functional quotient, and complete the analytic scaling
homotopy. The development checkpoint identifies relevant mathlib APIs.

Do not introduce `sorry`, `admit`, custom axioms, or assumptions that merely
hide a missing proof. Distinguish actual analytic results from formal
series results and from agreement restricted to polynomial functions.
Continue the mathematical work rather than repeating environment setup.

After substantive changes, run from the Lean project directory:

```sh
lake build
lake env lean Audit.lean
```

Update the project README, verification record, development checkpoint,
and root handoff with the exact proved scope and remaining work.

The user has authorized committing and publishing this work to
[PR #32](https://github.com/gustavdelius/affine_toda/pull/32) in
`gustavdelius/affine_toda`, branch `defect-integrability-conjecture`.
Do not merge it. Recheck the remote head before publication. The saved
workspace's worktree has an old detached HEAD: when using that checkout,
publish only explicitly selected files atop the current remote tree, never
its entire diff. Inspect the branch and worktree state in a fresh checkout
before making changes. Do not edit unrelated
worktrees or book files. Do not spawn subagents.

At the last recorded handoff, PR #32 was at commit
`471a0e09af146d8e183322c671cb3c7cce05ba85`, with tree
`80d3206d4870af785b8936800eb8176e8cce7f3b`. The full build and axiom audit
passed for 409 declarations, using only `propext`, `Classical.choice`, and
`Quot.sound`. Treat these as a recorded baseline, not a substitute for
reading the current handoff and checking the live remote state.
