# Pedagogical companion checkpoint

19–20 October 2026. Requested by Gustav Delius: explain the entire corrected defect integrability paper at the pace of the preceding sentence-by-sentence discussion, and commit the companion to the existing PR.

- Read the complete corrected manuscript at PR #32 head `ea7d4b80ca11112bc3a65b54c0d694290b41b885` and worked in an isolated `.claude/worktrees/pedagogical-companion` worktree.
- Wrote `defect-integrability/defect_integrability_companion.md`, covering the abstract and introduction, all four hypotheses, every sentence of Theorem 2.1, Sections 3–12, Appendix A, and the roles of the references.
- Included detailed explanations of the two formal expansions, the complete sewing recursion and residual argument, the equal-time generator, the free Fourier rigidity proof, analytic continuation from amplitude coefficients, nonlinear involution, and the Fourier Jacobian for independence.
- Included the reducible example, the coupled exponential example, the unequal-theory obstruction, the conditional composition proposal, and the massless counterexample to rigidity.
- Preserved the distinction between a written proof, finite symbolic checks, independent review, and complete Lean certification. The manuscript, its theorem statements, and the checking scripts are unchanged.
- Added a companion link and scope description to `defect-integrability/README.md`.

## Integration

This is an exposition of the corrected paper, not a new theorem or independent referee pass. Definitions, formulas, signs, normalization changes, and quantifiers were checked against the manuscript. In particular, the companion distinguishes the point-defect energy from its spatially integrated generating functional, spatial periodicity from time periodicity, quadratic amplitude order from Bäcklund parameter order, and spatial canonicity from equal-time canonicity. No unrestricted integrability claim or new theorem status is introduced.

## Validation

- All relative links and heading anchors in the companion resolve. Display-math, inline-math, and code delimiters are paired. No control characters or trailing whitespace were found.
- Independently recomputed the first charge's energy/momentum sign, the massive dispersion curvature, the first eight odd-binomial sums used in the symbol calculation, the exponential example's vacuum gradient and both Hessians, its pairing matrix and cyclic exponent identities, and its vanishing third quadratic generator. All checks passed.
- Confirmed that the research manuscript is byte-for-byte unchanged from the published rewrite. The existing 42-check records and scripts were not modified.
- `git diff --check` passed. No `.qmd` files or book theorem labels were changed.
- Publication is limited to the new companion, this checkpoint, and the companion paragraph in the defect reading guide. The worktree's older detached HEAD is not used as an instruction to republish its other differences.
