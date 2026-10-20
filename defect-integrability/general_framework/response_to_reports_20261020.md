# Response to the two reports on the written proofs

- Reports:
  - [referee_report_codex_20261020.txt](referee_report_codex_20261020.txt): Codex (GPT-6), reviewed commit `cd90589`; copied unchanged from `referee_scratch/general_framework_20261020_codex/calculations.txt`. Items are cited as C1–C15.
  - [referee_report.md](referee_report.md): adversarial report, 20 October 2026; the header names neither the model nor the commit, and its line numbers match `cd90589`. Items are cited as G1–G5 (Part I) and G-II.1–G-II.7 (Part II).
- Revised material: [paper.md](paper.md), [conjecture_report.md](conjecture_report.md), [README.md](README.md), [run_checks.sh](run_checks.sh), [checks/check_scope.py](checks/check_scope.py) (new), [lean/README.md](lean/README.md) and one docstring in [lean/GeneralFramework/Framework.lean](lean/GeneralFramework/Framework.lean).
- Date: 20 October 2026; author of the revision: Claude Opus 5.5.

## How the items were verified

No finding was taken over without an independent check. Every counterexample in the two reports was recomputed with a new script written from the paper's definitions, [checks/check_scope.py](checks/check_scope.py), which imports only `jets.py` and the Legendre transform of `check_balance.py`. It prints 41 `PASS` lines (35 after the first round, 5 added after the second and 1 after the third). Its first run had one `FAIL`, a sign slip in my own decomposition of the Remark 3.4.2 balance; the claim itself was right. The proof repairs (Lemma 6.3, the vacuum normalisation in Proposition 4.3, Theorem 7.3, Proposition 7.5, the (NR) argument) were re-derived by hand. Neither referee's scripts were run; Codex states that it wrote none.

## Integration

| Item | Verdict | How checked | Change |
|---|---|---|---|
| C1 (Lemmas 2.1–2.2) | verified; wording modified | re-derived (2.1)–(2.3) and the cancellation in $a_{K-1}$, $b_m$ | Lemma 2.1: uniqueness is local, and is stated for pairs satisfying (2.5) off shell (also G-II.7) |
| C2 (Theorem 3.3, Lemma 3.5) | verified | re-derived (3.5) and the subtraction in (b) | statement of the multiplier: new (3.3′) obtained by integrating derivatives of $C$ by parts; $E_Y(\rho C)=D_C^*\rho$ on the prolonged locus (also G-II.1) |
| C3 (Lemma 3.2 converse false) | verified | `check_scope.py`: $\mathcal L_d=\lambda(\psi-\phi)^2$; $E_\Phi h=\phi_{tt}+m^2\phi$ on the locus, Euler derivatives of $g\,C$ and $g\,D_tC$ vanish there | Lemma 3.2 restated with the regularity assumption; the example added after it; "precise form" removed here and in the conjecture report |
| C4 (abstract drops (I)) | verified | `check_scope.py`: $(x^2,-x^2,2x)$ is a promoted solution of $\lambda(\psi+\phi)$ with $E_-=2-m^2x^2$ | abstract corrected; Remark 3.4.2 rewritten (the old text called this defect consistent with Theorem 3.3); conjecture report corrected |
| C5 (Noether charges, closure rows) | verified | KdV, mKdV and NLS closure identities re-derived by hand | Lemma 5.2 proof states that the Boussinesq row is checked only by script |
| C6 (Lemma 5.4 up to total derivatives) | verified | `check_scope.py`: bulk $+D_x(w^2/2)$; balance holds at $s=1$, fails at $s=2$; KdV, mKdV, NLS Lagrangians strictly homogeneous | Lemma 5.4 requires strict homogeneity; example and boundary-term remark added. Lemma 5.5: the conclusion is restricted to promoted solutions, and Definition 3.1 for the boosted defect is checked case by case (also G-II.4, G-II.5) |
| C7 (Lemma 6.3 does not cover waves) | verified | the symbol of $(q,p)_t=(p,q_{xx}-V')$ is nilpotent; repair re-derived | Lemma 6.3 replaced by the spatial normal form for every admissible $\mathcal L$, with a proof; the residual normalisation of Theorem 6.4 is now proved (Proposition 4.3, last statement: the vacuum value of $R_2$ vanishes by closure and (4.1)) (also G2, G-II.3) |
| C8 (Lemma 6.2 form; Lemma 6.6 needs momentum conservation) | verified | `check_scope.py`: $-(\phi-\psi)^2/2\epsilon$ is not momentum-conserving and forces $\epsilon\phi_{xx}=0$ | Lemma 6.2 allows $O(\Delta^2)$ at $\epsilon^0$ (also G-II.6); Lemma 6.6 assumes momentum-conserving members; example added |
| C9 (Lemma 6.5 needs $w\ne0$, covariant branch) | verified | eigenvector argument re-derived; the $w=0$ series $\frac{\epsilon}{1-\epsilon}m_*$ | Lemma 6.5 restated (also G3, below); Theorem 8.1(C) now asks for linearly independent symbols, by computation or by Lemma 6.5 |
| C10 ((NR) for all degrees; Lemma 7.2 regularity) | verified | `check_scope.py`: $\partial_1\partial_2\Omega=s_1s_2s_n\omega''(k_n)$ for all signs; $\omega''\not\equiv0$ in every row | §7.1 proves (NR) for all $n\ge3$ (also G-II.2); Lemma 7.2 says it works degree by degree, not for flat smooth densities |
| C11 (Theorem 7.3 intermediate step false) | verified | `check_scope.py`: the canonical example; $\{Q_2,H_2\}+\{Q_1,H_3\}=0$ with $\{Q_2,H_2\}\ne0$; $Q,R$ conserved, commuting, satisfying (L) | **modified**: the extra condition is (L′) $\{Q_{n,1},H_3\}=0$, which is what the degree-2 step uses and is weaker than the suggested $\{Q_{n,1},H\}=0$; analytic/polynomial densities assumed; example added (also G5) |
| C12 (Theorem 7.4 quantifier) | verified | `check_scope.py`: $u=\varepsilon\cos kx$ | statement is now existential; example added |
| C13 (Proposition 7.5) | verified, merged with G4 | re-derived; see G4 | Proposition 7.5 rewritten |
| C14 (sentence after Theorem 8.1) | verified | `check_scope.py`: equal-mass pair, $\{A,H\}=\{B,H\}=0$, $\{A,B\}=2\int(p_1Kq_2-p_2Kq_1)$ | Theorem 8.1 gains hypothesis (E) for the charge conditions; the paragraph after it rewritten |
| C15 (Appendix A constant) | verified | `check_scope.py`: $\mathcal H_--\mathcal H_+=-c$ | converse states the constant and its normalisation (also G-II.7) |
| G1 (Lemma 4.1, $N=D_x\nu$) | verified | `check_scope.py`: KdV mass flux is $\pi_0-\frac12p_t$; $q-p$ is a defect charge for the defect of [3]; adding $\beta p^2$ leaves $2\beta p$ | Lemma 4.1 restricted to trivial laws; KdV mass explained after the lemma and in Corollary 5.3 |
| G2 (Lemma 6.3) | verified | as C7 | as C7 |
| G3 (Lemma 6.5 under boosts) | verified | for a boost $(\mathcal E_d,P_d)$ is a vector (Lemma 5.5), so the density is not an eigenvector; the 1-form $\mathcal G\,dx-\mathcal F\,dt$ is | Lemma 6.5 now states covariance of the closed 1-form and concludes for the integrated charges and an abstract linear action $T_\theta$ on symbols; remark on the $\omega(k)$ factor |
| G4 (Proposition 7.5, $F_2$) | verified | the omitted term is the linear part applied to the quadratic correction of $D_t$; for a total $x$-derivative it averages to zero; `check_scope.py` checks the Boussinesq $F_2$ and the absence of a quadratic term in $\sin\phi$ | **modified**: one hypothesis, "$F_2$ is zero or a total $x$-derivative", replaces G4's two cases; it holds in all five rows of the table; it fails for Tzitzéica and $a_r^{(1)}$, $r\ge2$ (noted in §7.2, §9 comment 4 and §10) |
| G5 (Theorem 7.3) | verified | as C11 | as C11 |
| G-II.1–G-II.7 | verified | as the matching C items | as above; G-II.5's proposed bridge (tangency as an identity on $\Gamma_d$) is not adopted, because it does not supply locality of the boosted potential |

Additional findings of this revision, not in either report:

- **Time-linear shifts (§4.1).** The example claimed that a time-linear shift gives a defect charge whenever the defect depends on the fields only through differences and derivatives. That is false: the shift changes $\Phi_t$, and condition 3 of Lemma 4.1 also needs $(\partial_{D_t\Phi_0}+\partial_{D_t\Psi_0})\mathcal L_d\in\operatorname{Im}D_t$. For the Boussinesq defect this sum contains a nonzero multiple of $U_1+V_1$, so it is not a total derivative (its $t$-Euler derivative in $U_1$ is $\sqrt3\kappa/c$). Nothing depended on the claim: law 2 of the Boussinesq row is the constant-shift law, and Corollary 5.3 now says so.
- **Hypothesis (E) in the observed cases (§9, comment 6).** The paper never checked (L). For sine-Gordon, NLS and mKdV the generating densities start at quadratic order; for KdV the linear parts are Casimirs. For Boussinesq, (L) and (L′) are open (§10).
- **Theorem 8.1(C)** now requires the family to consist of momentum-conserving defects, because Lemma 6.6 and Theorem 6.4 use it.

Not integrated:

- C5 on Boussinesq: no written derivation of the closure row was added; the row is labelled as checked by script only.
- C13 and G4 do not allege that any tabulated symbol is wrong. `check_symbols.py` was not changed. (Superseded by R6 below: Proposition 7.5 is now proved to apply to the first four rows of the symbol table only; the Boussinesq row is evidence.)

## Status

All labels in the paper are unchanged in kind: no statement was upgraded. Several were weakened (Lemmas 3.2, 4.1, 5.4, 5.5, 6.5, Theorem 7.4) or given extra hypotheses (Lemma 6.6, Theorems 7.3 and 8.1). The new proofs (Lemma 6.3, the vacuum normalisation in Proposition 4.3, the all-degree (NR) argument, Proposition 7.5) have had no independent check yet.

## Second round (Codex, 20 October 2026)

- Report: [referee_report_codex_20261020_round2.txt](referee_report_codex_20261020_round2.txt), copied unchanged from `referee_scratch/general_framework_20261020_codex_round2/calculations.txt`. It reviewed the uncommitted revision above (paper SHA-256 `ce15345b…`). Items are cited as R1–R8.
- R1–R4 accept the first-round repairs (C1–C15, Lemma 6.3, the vacuum normalisation, Theorems 7.3 and 7.4) and need no change, except the two remarks below.

| Item | Verdict | How checked | Change |
|---|---|---|---|
| R1, C14 remark | verified | reading of §8 against §9 | §8 now says that §9 verifies (E) for four rows and leaves the others open |
| R2, autonomous charges | verified | the vacuum argument uses $D_tQ^1=0$ at a constant solution, which needs $Q^1$ autonomous | Proposition 4.3, last statement, restricted to autonomous $Q^1,Q^2$ |
| R5 (Lemma 6.5, nonlinear symmetries) | verified | `check_scope.py`: $U=q+r^2$, $V=r$; Hessian determinant $-1$; $U_t=P_r-2rP_q$; the symmetry acts by $q\mapsto aq+(a-a^{-2})r^2$; $\int U_t$ scales by $a$, its quadratic part by $a^{-2}$ | condition 4 added ($Q_{n,1}[B_\theta(v,v)]$ trivial; holds for linear actions and without linear parts); proof uses it; the example added after the lemma |
| R6 (Proposition 7.5, branch solving and potentials) | verified | `check_scope.py`: $\overline{p_t}=6\eta^2\lvert a\rvert^2$ for the KdV potential, and the KdV branch $(2+\epsilon D_x)\Delta=-2\epsilon u+\frac\epsilon2\Delta^2$ re-derived from (9.12) of [3]; (9.4) and (9.12) read on arXiv | Proposition 7.5 now assumes locality in $v,\Delta$ and the Lemma 6.2 branch; the proof says why the inverse preserves $\operatorname{Im}D_x$; the potential example and the KdV and mKdV branch relations added after it; for Boussinesq, Lemma 6.2 is recorded as unchecked |
| R7 (three symbols re-derived) | noted | the report's own derivation; agrees with `check_symbols.py` | none |
| R8 (Boussinesq factors of $c^2$) | verified | $a_0=u/c^2$ gives $\mathcal G=(u-v)/c^2$; in canonical $(u,u_t/c^2)$, $p_t=u_{xx}+\lambda D_x(u_x^2)-\kappa^2u_{xxxx}$ (`check_scope.py`) | table of Lemma 5.2 and §9 comment 5 print $(u-v)/c^2$; §7.2 prints $F_2=(0,\lambda D_x(u_x^2))$; the symbol table has $c=1$ and is unchanged |

## Third round (Codex, 20 October 2026)

- Report: [referee_report_codex_20261020_round3.txt](referee_report_codex_20261020_round3.txt), copied unchanged from `referee_scratch/general_framework_20261020_codex_round3/calculations.txt` (paper SHA-256 `44583e3d…`). It accepts the second-round repairs of Lemma 6.5, Proposition 7.5 and the Boussinesq normalisations, and raises two wording points.

| Item | Verdict | How checked | Change |
|---|---|---|---|
| T1 (boosts are not linear on phase-space data) | verified | at $t=0$ the infinitesimal boost gives $\delta\phi_t=\phi_x+x(\phi_{xx}-U'(\phi))$, quadratic part $-\frac12U'''(0)x\phi^2$ (`check_scope.py`) | Lemma 6.5, condition 4: boosts removed from the linear examples; the quadratic correction and its vanishing for sine-Gordon stated |
| T2 (symbol table attributed to Proposition 7.5) | verified | the Boussinesq row does not satisfy the checked hypotheses of Proposition 7.5 | sentence before the table restricted to the first four rows; the first-round "Not integrated" line marked as superseded |
