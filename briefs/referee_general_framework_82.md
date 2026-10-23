# Brief: referee pass on Section 8.2 of the general-framework defect paper, and on a hypothesis of Proposition 7.5

You are an adversarial mathematical-physics referee. You are working in the repository of a Quarto book on affine Toda field theory, in the main checkout `/home/gustav/Git/affine_toda`, on branch `claude/defect-integrability-rescue`. The material under review is not a book chapter. It is a stand-alone Markdown paper in `defect-integrability/general_framework/`.

**Rules.**
- Other agents may be editing files in this worktree at the same time.
- Do not edit any existing file.
- Do not run git commands that change the index or the working tree (no commit, checkout, stash, reset, rebase or restore).
- Do not run `quarto render`.
- Do not spawn subagents.
- Write scratch scripts only under `referee_scratch/general_framework_82/`.
- Write the report to `briefs/referee_general_framework_82_report.md`.

## Context

The paper is `defect-integrability/general_framework/paper.md`, *Momentum-Conserving Defects, Kinematic Symmetry and Integrability*. Its Theorem 8.1 deduces infinitely many commuting local charges from momentum conservation at a defect together with explicit hypotheses (A)–(E). Hypothesis (C) asks for a nondegenerate one-parameter family of momentum-conserving defects with a formal branch (a regular transparent limit) and linearly independent quadratic symbols. Deriving (C) from momentum conservation is the paper's open problem (§10).

**What is under review.** Commit `09b5ced` (23 October 2026, drafted by Claude Opus 5.5) added Section 8.2, "Hypothesis (C) for relativistic Type-I defects":
- Proposition 8.2 (splitting): for Type-I defects with constant kinetic coupling (8.2) and a derivative-free defect momentum, momentum conservation forces $\mathcal B=f(w)+g(q)$ and the constraint (8.4); with a converse.
- Proposition 8.3 (rescaling family): with a transparent point and an irreducible bulk, $G=g''(0)=\gamma I$, $f=4U/\gamma$, and the family (8.5) $\mathcal B_\epsilon=\epsilon U(w)+\epsilon^{-1}\hat g(q)$ is momentum-conserving.
- Theorem 8.4: the family has a formal branch (via Lemma 6.6), and the listed hypotheses of Theorem 8.1 hold; it states what remains.

Propositions 8.2–8.3 restate Propositions 3.1–3.2 of the companion manuscript [23], `defect-integrability/defect_integrability_paper.md`, in this paper's notation. That manuscript has not been independently reviewed. Do not treat it as established: re-derive what §8.2 takes from it.

The same commit also edited:
- the Status paragraph, the abstract and §1.3;
- the §9 table (rows for sine-Gordon and $a_r^{(1)}$ Toda) and §9 comment 4;
- §10 items 1 and 3;
- Appendix B;
- reference [23].

Comment 4 now claims that the $a_2^{(1)}$ Toda defect of [2] satisfies the hypotheses of [23, Theorem 2.1], so that its charges commute and infinitely many are independent.

**Check script.** `defect-integrability/general_framework/checks/check_type1_family.py` has 15 checks and runs in about 3 s. Run it from its directory. The other scripts in `checks/` are described in Appendix B. `checks/check_balance.py` contains the transcription of the $a_2^{(1)}$ Toda defect of [2] used by the new script.

**Earlier reviews.** Three Codex rounds and one adversarial report on the rest of the paper are in `defect-integrability/general_framework/referee_report*`. Their integration is in `response_to_reports_20261020.md`. `referee_report_codex_20261020.txt` shows the expected depth.

**The drafter's flags for you.**
- The defect of [1] has the form (8.2) only up to a total time derivative. Check that this changes neither the sewing equations nor the defect energy.
- The splitting step needs $\widetilde P$ to exist as a function on a connected, simply connected neighbourhood. The proof does not say so.
- The Toda constraint (8.4) is checked numerically at six rational points to 30 digits, not symbolically.
- The drafter believes, but has not verified, that the hypothesis "$F_2$ is zero or a total $x$-derivative" in Proposition 7.5 is unnecessary whenever the generating density has no linear part at the vacuum. If so, the paper overstates a limitation for Tzitzéica and affine Toda. This is item 6.

## Notation

These are the paper's conventions, not the book's. Most false findings come from convention slips, so check against these first.

- **Bulk.** $\mathcal L=\frac12\lvert\phi_t\rvert^2-\frac12\lvert\phi_x\rvert^2-U(\phi)$. The spatial momentum is $\pi=\partial\mathcal L/\partial\phi_x=-\phi_x$. The spatial Hamiltonian density is $\mathcal H=\pi\phi_x-\mathcal L=-\frac12\lvert\pi\rvert^2-\frac12\lvert\phi_t\rvert^2+U$, and the momentum flux is $T^{11}=-\mathcal H$ (Lemma 2.1).
- **Sewing equations (3.1).** $\pi_-=-E^{(t)}_\Phi\mathcal L_d$, $\pi_+=E^{(t)}_\Psi\mathcal L_d$, and $0=E^{(t)}_\lambda\mathcal L_d$. Here $E^{(t)}$ is the time-Euler operator, and $\Phi=\phi(0^-,t)$, $\Psi=\psi(0^+,t)$ are the boundary values.
- **Momentum balance (Definition 3.1).** $\mathcal H_--\mathcal H_+\in\operatorname{Im}D_t+\langle C\rangle$; for Type I this means $\mathcal H_--\mathcal H_++D_t\widetilde P=0$ for a local $\widetilde P$. It is required off shell, for independent boundary jets.
- **Defect of §8.2.** $\mathcal L_d=\frac12\phi\cdot E\phi_t+\phi\cdot D\psi_t+\frac12\psi\cdot E\psi_t-\mathcal B$ with $E^T=-E$ and $D=I-E$. The coordinates are $q=\frac12(\phi-\psi)$ and $w=\frac12(D^T\phi+D\psi)$, so $\phi=w+Dq$ and $\psi=w-D^Tq$. Gradients of functions are column vectors.
- **Sine-Gordon** has $U=1-\cos\phi$ (mass 1), and the defect of [1] has $\mathcal B=2\sigma(1-\cos w)+2\sigma^{-1}(1-\cos q)$.
- **$a_2^{(1)}$ Toda.** Roots with $\lvert\alpha\rvert^2=2$, $U=\sum_{j=0}^2e^{\alpha_j\cdot\phi}-3$, $D=2(I-\pi)^{-1}$ with $\pi$ the Coxeter rotation, and $\mathcal B=\sigma U(w)+\sigma^{-1}\big(\sum_je^{\alpha_j\cdot Dq}-3\big)$. This is as transcribed in `checks/check_balance.py`. [2] may use a different normalisation of the coupling or of the fields; translate before comparing.
- **Lemma 6.6** concerns families $A_\Phi\cdot\Phi_t+A_\Psi\cdot\Psi_t-\epsilon^{-1}\mathcal B_--\sum_{k\ge0}\epsilon^k\mathcal B_k$ with $\mathcal B_-$ vanishing to second order on $\Psi=\Phi$ and with invertible Hessian $\partial^2\mathcal B_-/\partial\Phi^2$ there.

## Read first

- `paper.md`: §2 (Lemmas 2.1–2.2), §3 (Definition 3.1, Theorem 3.3, Lemma 3.5), §4.1 (Lemma 4.1), §6 (Definition 6.1, Lemmas 6.2, 6.3, 6.6, Theorem 6.4), §7 (Definition 7.1, Theorem 7.3, Proposition 7.5 and the paragraph after it), and all of §8.
- [23] `defect-integrability/defect_integrability_paper.md`: §2 (hypotheses 1–4 and Theorem 2.1), §3 (Propositions 3.1–3.2), §9.
- The guide `defect-integrability/general_framework/guide.md` §11.2 explains §8.2 for readers. Check it only for faithfulness to the paper (item 7).
- Source papers, from arXiv, since no local copies are guaranteed: hep-th/0305022 [1] (Bowcock–Corrigan–Zambon, sine-Gordon), hep-th/0401020 [2] (affine Toda defects), 0902.1307 [4] (Corrigan–Zambon, $a_r$ Toda comments) and 1612.03002 [10] (Bristow–Bowcock). If `~/referee-copy/papers/*.txt` or `papers/` exists, use those texts.

## Evidence rule

For each item, do **one independent computation**: a derivation written out, or a script of your own written from the definitions above. You may run `check_type1_family.py` and the other scripts for comparison, but they are not evidence. A verdict without its own evidence counts as "unclear".

## Items (most important first)

1. **Proposition 8.2 (splitting).**
   - Derive the sewing equations of (8.2) from (3.1) yourself.
   - Verify that the terms of $\mathcal H_--\mathcal H_+$ quadratic in the velocities cancel exactly when $D=I-E$, or state what weaker condition suffices.
   - Derive the gradient conditions on $\widetilde P$ and the identity $\frac12(\lvert\mathcal B_\phi\rvert^2-\lvert\mathcal B_\psi\rvert^2)=U(\phi)-U(\psi)$.
   - Check the change of variables to $(w,q)$, including the transpose conventions in $\partial_q=D^T\partial_\phi-D\partial_\psi$.
   - Check the conclusion $\mathcal B_{wq}=0$, the formula $\widetilde P=g-f$, the constraint (8.4) and the converse.
   - Is the restriction to a derivative-free $\widetilde P$ stated where it is needed? Is the domain assumption (flag 2) needed?
   - Does the remark that the defects of [1] and [2] have the form (8.2) "up to a total time derivative" hold, and does that derivative change neither the sewing equations nor the defect energy?
2. **Proposition 8.3 (rescaling family).**
   - Check $Gf'=4U'$, the step from $Gf''=4U''$ to $[G,U'']=0$, and the splitting of $U$ over the eigenspaces of $G$ near $0$.
   - Is the irreducibility hypothesis, as stated, exactly what the argument uses?
   - Check $f=4U/\gamma$, the family (8.5) with $\hat g=4g/\gamma$ and $\hat g''(0)=4I$, the defect momentum $\widetilde P_\epsilon$, and that the given defect is the member $\epsilon=4/\gamma$.
   - Check the remark that "$G$ a nonzero multiple of $I$" can replace irreducibility.
   - Are any of the bulk assumptions ($U$ analytic, $U(0)=U'(0)=0$, $M$ positive definite) used here but not stated?
3. **Theorem 8.4.**
   - Check every hypothesis of Lemma 6.6 for (8.5): the form of the kinetic term, with $A_\Phi=-\frac12E\phi$ and $A_\Psi=D^T\phi-\frac12E\psi$; that $\hat g(q)$ vanishes to second order on the diagonal; and that its Hessian in $\phi$ is $\frac14\hat g''(0)=I$.
   - Does Lemma 6.6, as proved in §6, need anything that (8.5) does not supply, such as a condition on $\mathcal B_0$ or on the gyroscopic terms?
   - Check the claims that (A), (B) and (D) of Theorem 8.1 hold, that $\mathcal E_d=\mathcal B_\epsilon$ vanishes to second order at the vacuum, and that (L) and (L′) are therefore vacuous.
   - Check that for one field (NR2) holds, so that only nondegeneracy and independence remain.
   - Is the label (Theorem, with a complete proof in the text) justified? Is anything claimed beyond what the proof gives?
4. **The published defects.**
   - Sine-Gordon: check $\gamma=2/\sigma$, $\hat g=4(1-\cos q)$ and that the defect of [1] is the member $\epsilon=2\sigma$.
   - $a_2^{(1)}$ Toda: compare the defect of [2] directly with (8.2), from the arXiv text and not only from `check_balance.py`, after any change of normalisation. Prove the constraint (8.4) symbolically if you can, rather than at sample points. Check $\gamma=4/\sigma$, $\hat g''(0)=4I$ and that $G$ is a multiple of $I$.
   - Does Theorem 8.4 apply to $a_r^{(1)}$ for every $r$? The paper claims it only for $a_2^{(1)}$; say whether the claim could safely be extended.
5. **§9 comment 4 and [23].** Comment 4 claims that the $a_2^{(1)}$ defect satisfies the hypotheses of [23, Theorem 2.1], with "$G$ a multiple of $I$" in place of irreducibility, so that its charges commute and infinitely many are independent.
   - Check each of [23]'s hypotheses 1–4 for this defect, including the "normalized" condition in its hypothesis 3.
   - Is the claim correctly flagged as resting on an unreviewed manuscript?
   - Do the edited §9 table, §10 items 1 and 3, the Status paragraph, the abstract and §1.3 claim more than §8.2 and [23] give?
6. **Proposition 7.5 without the $F_2$ hypothesis.** Proposition 7.5 computes the generating quadratic symbol from one plane wave and the linearised flow. It assumes that the quadratic part $F_2$ of the evolution is zero or a total $x$-derivative. The paragraph after it says the shortcut fails for Tzitzéica and for $a_r^{(1)}$ Toda with $r\ge2$, because $U'''(0)\ne0$.

   The drafter's conjecture is as follows. Suppose the generating density $\mathcal G(\phi,\Delta)$ has no linear part at the vacuum. Then the quadratic part of each $Q_n$, as a functional of the phase-space data, depends only on the linear part of the branch. That linear part is computed with the linearised flow, so $F_2$ cannot contribute at order $\eta^2$. If so, the hypothesis is needed only when $\mathcal G$ has a linear part, as for KdV ($q-p$) and Boussinesq ($(u-v)/c^2$).
   - Prove or refute this.
   - Test it on a case with $U'''(0)\ne0$: either the $a_2^{(1)}$ Toda family of §8.2, or the Tzitzéica Type-II defect (`checks/check_hierarchy.py` has a `tz` model). Compute $Q_1$ and $Q_2$ to cubic order with the full field equations, and compare their quadratic symbols with the plane-wave prescription.
   - For Type II, does $\mathcal G$ have a linear part in the auxiliary field $\lambda$?
   - If the conjecture holds, give corrected wording for Proposition 7.5, the paragraph after it, §9 comment 4 and §10 item 3, with file and line.
7. **Faithfulness of the guide.** Check that `guide.md` §11.2 and Part 12.4 state §8.2 accurately, with no stronger claims, no wrong normalisations and no misattributions. Check also the remark that the normalised $\epsilon$ is twice the sine-Gordon $\sigma$ used in its Part 5.
8. **Prior art and citations.**
   - §8.2 says that, for one field and for $a_r^{(1)}$ Toda, the splitting and its rescaling were found in [1, 2, 4]. Quote the source lines.
   - Does any of [1, 2, 4, 10], or other literature you find, already derive the splitting and the rescaling family from momentum conservation for general $r$ with constant coupling? If so, quote it, and say how §8.2 and Part 17 of the guide should credit it.
   - The paper claims no novelty for its general statements. Check that §8.2 does not imply novelty.
   - Check that every citation in §8.2 and in the edited §9–10 text says what the source says.

## Report format (`briefs/referee_general_framework_82_report.md`)

A header with the date, your model and the commit reviewed. Then one section per item, with:
- the verdict (correct / wrong / unclear);
- your own computation (the script inline or its path, and its output);
- for errors, replacement text ready to paste, with file and line.

List separately any claim you could not check. End with other observations, labelled as unverified.
