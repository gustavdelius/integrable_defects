# Structural integrability Lean checkpoint

**This is the historical setup checkpoint. Read
[structural_lean_development_checkpoint.md](structural_lean_development_checkpoint.md)
for the current proved results, gaps, verification, and publication state.**

Date: 20 October 2026.

## User request and current phase

The user requested: "Formalize the proof in Lean." This refers to Theorem 2.1 and its supporting proof in the corrected `defect-integrability/defect_integrability_paper.md`, not the older unrestricted theorem or the earlier scalar reconstruction.

The user subsequently suggested compacting context once Lean works, before starting formalization. This checkpoint separates environment setup from the mathematical work. The full formalization remains outstanding. No theorem from the structural paper has yet been claimed as formalized. The only new Lean proofs at this checkpoint are environment checks.

The user previously authorized adding this work to PR #32 and publishing commits. That authorization persists. Do not ask again merely to commit further requested work. Do not merge the PR.

## Repository and isolation

- Repository: `gustavdelius/affine_toda`.
- PR: <https://github.com/gustavdelius/affine_toda/pull/32>.
- Branch: `defect-integrability-conjecture`.
- Last verified remote head: `4ff23cdd6d06aa67a52c9c4e5bef312fd1370ea8`.
- Tree at that head: `ef0e95aa42bc0f3625f9aeb73cbb2c5c13e5b158`.
- Worktree: `.claude/worktrees/lean-structural`, relative to the conversation workspace.
- Lean project: `defect-integrability/structural_type_I/lean` inside that worktree.

The worktree was created from the locally available older commit `38560b8d26211556ce27e7919dca8fdbb052f1ca`. The current paper, companion, reading guide, and structural proof note were copied from the preceding worktree so references resolve. They are already published. **Do not commit or publish all differences from the old local HEAD.** Publish only explicitly selected new Lean files and related status updates, using the current remote tree as the base. Other worktrees contain unrelated/staged material and must remain untouched.

Local `AGENTS.md` requires isolated worktrees and honest status labels. Its earlier Codex-only-referee role is superseded by the user's explicit instruction to take over the proof and formalize it. No book `.qmd` files need editing. Do not spawn subagents: the active developer instruction forbids proactive delegation.

## Toolchain and dependencies

- Lean: `leanprover/lean4:v4.35.0`, already installed at `/home/gustav/.elan/toolchains/leanprover--lean4---v4.35.0`.
- mathlib: release `v4.35.0`, pinned by actual commit `56a005855ea17e0b0958f73ec801ae140b0a1679` in `lakefile.toml`.
- All eight transitive dependency commits are pinned in the generated `lake-manifest.json`. Keep that manifest.
- Dependency sources and compiled artifacts are in the project's ignored `.lake/` directory.
- Download cache: `/tmp/structural-mathlib-cache`; set `MATHLIB_CACHE_DIR` to this path for cache commands so writes stay in an allowed directory.
- mathlib's cache executable was built successfully. The 9,031 cache archives were downloaded successfully from the official cache server, using hashes computed by mathlib's own source hashing code.

Normal commands, run from the Lean project directory:

```sh
lake build
lake env lean Audit.lean
```

If cached artifacts need unpacking again:

```sh
MATHLIB_CACHE_DIR=/tmp/structural-mathlib-cache lake exe cache unpack
```

The aggregate file `Structural.lean` currently imports `Structural.Smoke`. `Structural/Smoke.lean` imports the square-root, ring, and positivity modules and proves a real polynomial identity and positivity of a massive frequency. `Audit.lean` prints their axiom dependencies. These are setup checks only. Use focused mathlib imports: an initial `import Mathlib` build succeeded but took several minutes; focused imports rebuilt the two project modules in about three seconds.

The project uses Lean 4.35's module system. Public theorem signatures need their types available through `public import`, not only a private import. `Structural/Smoke.lean` therefore uses `public import Mathlib.Analysis.SpecialFunctions.Sqrt`; tactic imports can remain private. Keep this distinction when adding modules.

## Network setup lesson

`lake update` initially failed because a Git subprocess could not resolve GitHub. Direct tool commands beginning with the already approved `git fetch` prefix succeeded. Each package was then checked out at the exact upstream revision in its own dependency repository. A later `lake update` succeeded offline and generated the ordinary portable Git manifest. No fake commit metadata or custom mathlib sources were used.

Similarly, `lake exe cache get` could not resolve the cache host from its nested curl subprocess. It produced a very large error stream; do not repeat that approach. Direct tool commands beginning with approved `curl -L` succeeded.

Temporary helpers, if another setup needs the same procedure:

- `/tmp/StructuralCacheManifest.lean` imports `Cache.Hashing`, calls `getHashMemo`, and exports module/hash pairs.
- `/tmp/structural-mathlib-hashes.tsv` contains the 9,031 computed module hashes.
- `/tmp/structural-mathlib-curl.cfg` contains only public official cache URLs and local output paths.
- Direct download command: `curl -L --fail --silent --show-error --parallel --parallel-max 20 --retry 2 --config /tmp/structural-mathlib-curl.cfg`.
- Successful download was followed by `lake exe cache unpack`; cache hashes and decompression use the unmodified upstream tools.

Do not include dependency archives, caches, `.lake`, or temporary transport files in the PR.

## Actual theorem to formalize

For a real multicomponent Klein–Gordon theory, assume an analytic positive-mass vacuum; an orthogonally irreducible bulk potential (or directly a nonzero scalar leading defect Hessian); the specified constant normalized Type-I auto-defect; derivative-free strong momentum balance; and a transparent nondegenerate critical manifold.

The conclusion constructs a unique near-identity local formal Bäcklund branch, analytic finite-jet local conserved coefficients, pairwise canonical equal-time Poisson commutation, arbitrarily large finite independent subfamilies at arbitrarily small periodic Cauchy data, and formal permutability. No convergence or full fixed-defect hierarchy is claimed.

## Proof dependencies and outstanding obligations

Every item below is still pending formalization. Names describe intended mathematical components, not already-proved Lean declarations.

1. **Concrete local-functional framework.** Represent analytic finite-jet densities near the zero jet; total spatial derivative; quotient by spatial divergences and vacuum constants; Euler derivatives; the canonical Poisson bracket; conserved functionals; amplitude Taylor parts. Establish that definitions correspond to actual local field expressions and can be evaluated on small periodic data.
2. **Momentum splitting (paper Proposition 3.1).** Derive multicomponent sewing equations and coefficient identities. Derive `B_wq = 0`, the split `B = f(w) + g(q)`, and the potential identity from strong momentum balance.
3. **Scalar Hessian and normalization (Proposition 3.2).** Derive `G f' = 4 U'`, commutation of `G` with all Hessians, orthogonal splitting when `G` has distinct eigenspaces, scalar `G` from bulk irreducibility, reciprocal rescaling, and `[E,M] = 0`.
4. **Formal branch (Proposition 4.1).** Construct the coefficient recursion in the actual local jet algebra, prove finite differential order and analyticity at each order, then derive the residual identity and use its invertible leading pole to prove the other sewing equation and the transformed bulk equation. A generic recursion lemma is useful but is not this entire result.
5. **Current and equal-time generator (Proposition 5.1).** Prove the local continuity equation, coefficientwise conservation, the variational generating identity, symplectic preservation, and the parameter Hamiltonian `-I(epsilon)/epsilon` with the stated sign.
6. **Free rigidity (Lemma 6.1).** Formalize polarization, finite-jet polynomial Fourier kernels, the momentum hyperplane, oscillator amplitudes, frequency nonresonance on open sets, continuous-kernel vanishing, and polynomial divisibility giving a total derivative. Also handle linear functionals. Proving only the frequency curvature formula is not the lemma.
7. **Analytic rigidity (Lemma 6.2).** Prove the amplitude-degree bracket calculation modulo divergences, induction from the free lemma, analytic Euler-derivative uniqueness, and the scaling homotopy. Do not assume injectivity of the quadratic-part map in a purported formalization of the theorem: deriving it is the central task.
8. **Involution and permutability (Proposition 7.1).** Derive the linearized map and its quadratic generators. Prove their commutation, conservation of the full brackets using Jacobi, apply the proved rigidity result, and integrate the formal parameter velocity to a commuting exponential.
9. **Independence (Proposition 8.1).** Prove the nonvanishing subsequence of odd symbols, distinct-degree polynomial independence, integer evaluation matrix invertibility, Fourier restriction of charges, and persistence of the Jacobian determinant at small nonzero amplitudes. Nontriviality of individual charges is insufficient.
10. **Examples and scope.** Formalize the reducible noncommuting example, the coupled two-component exponential identity, the shifted transparent-point obstruction for different potentials, and the massless counterexample to rigidity.
11. **Appendix A.** Formalize the geometric tangent-space lemma under exactly its stated Lagrangian equality, then connect the spatial Hamiltonian and generating-functional signs to the actual variational setting. This is auxiliary to the main proof.

The main mathematical design task after setup is item 1 and the concrete bridge for items 6–7. It is legitimate to prove reusable abstract lemmas, but their hypotheses must not conceal these missing analytic results. Consider separately a formal differential-polynomial core and a concrete analytic-germ realization, and explicitly prove the connection before claiming the original analytic theorem.

## Conventions and errors to avoid

- Work over real vector spaces / suitable differential algebras, not only derivations on integers. The older integer-based model had only zero derivations.
- Never assume a total time derivative is injective on the full algebra: its kernel includes constants.
- `q=(u-v)/2`, `w=(D^T u + D v)/2`, `D=I-E`, `E^T=-E`.
- After normalization: `B_epsilon=epsilon U(w)+epsilon^-1 g(q)`, `P_epsilon=-epsilon U(w)+epsilon^-1 g(q)`, `g''(0)=4I`.
- `D_+ q = -epsilon U'(w)/2`, `D_- w = g'(q)/(2epsilon)`.
- `q_1=(p-u_x)/2`; `v=u+epsilon(u_x-p)+...`.
- Bulk physical momentum is `-integral p·u_x`; first charge is energy plus that momentum.
- Equal-time form: `Omega = integral delta u wedge delta p`; `X_F=(F_p,-F_u)`.
- Spatial momentum is `pi=-u_x`; spatial Hamiltonian density is `-T11`; spatial generating functional is **minus** the defect action.
- Parameter order and amplitude degree are distinct gradings.
- The theorem concerns bulk charges, not a corrected hierarchy at a fixed defect.
- Final theorem dependencies must be audited. No `sorry`, `sorryAx`, custom unproved axioms, or inconsistent hypotheses may be presented as a completed formalization. Standard Lean foundations (`propext`, `Quot.sound`, `Classical.choice`) must be distinguished from extra mathematical assumptions.
- A conditional theorem assuming rigidity, formal locality, or functional independence does not fulfill the request to formalize their proofs. Record it honestly as a reusable partial result, and continue toward the concrete statements.

## Status before context compaction

**Setup is verified and ready for context compaction.**

- `lake exe cache unpack`: succeeded, 9,030 files decompressed and one already decompressed.
- Final `lake build`: succeeded, 2,087 dependency/build jobs; `Structural.Smoke` built in 2.1 seconds and `Structural` in 1.0 second after narrowing the imports.
- `lake env lean Audit.lean`: succeeded. Both smoke theorems depend only on `[propext, Classical.choice, Quot.sound]`. There is no `sorryAx` or custom mathematical axiom in those proofs.
- The broader `import Mathlib` setup was also tested successfully before narrowing imports. The full mathlib cache is available for future work.
- No background builds or downloads remain running.
- No structural proof development has begun, and no changes from this setup have yet been published. The formalization request remains active for the next context.

After compaction, read this checkpoint and the paper, inspect the actual mathlib APIs, then start the concrete local jet/functionals framework and the free-rigidity bridge. Do not redo the dependency setup. Useful existing sources include `Mathlib/Algebra/MvPolynomial/Derivation.lean`, `Mathlib/Algebra/MvPolynomial/PDeriv.lean`, `Mathlib/RingTheory/PowerSeries/Basic.lean`, `Mathlib/Analysis/Analytic/Basic.lean`, `Mathlib/Analysis/Analytic/Within.lean`, `Mathlib/Analysis/Fourier/FourierTransform.lean`, `Mathlib/Analysis/Fourier/FourierTransformDeriv.lean`, and `Mathlib/Topology/Germ.lean`. These are starting points, not evidence that the local-functional or Poisson framework already exists.
