# Adversarial Referee Report on [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md)

**Manuscript:** *Momentum-Conserving Defects, Kinematic Symmetry and Integrability* ([defect-integrability/general_framework/paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md))  
**Date:** 20 October 2026  
**Scope:** Written proofs in Sections 2–8 and Appendix A.

---

## Overall Verdict

The core mechanism of the paper — the Ostrogradsky spatial Hamiltonian identities (Section 2), the variational proof of the Bäcklund theorem via the $t$-Euler operator and Helmholtz self-adjointness (Theorem 3.3 and Lemma 3.5), the closure mechanism from affine conservation laws (Proposition 4.3 and Lemma 5.2), and the nonresonant rigidity argument (Lemma 7.2) — is mathematically sound and impressively clean.

However, a line-by-line adversarial audit of the written proofs turns up **five substantive flaws or gaps** where a statement is false in the generality claimed or a proof step fails as written, along with **seven secondary technical gaps or imprecisions**. Every one of these issues can be repaired cleanly without altering the main conclusions for the observed models.

---

## Part I. Substantive Flaws and Gaps in the Proofs

### 1. Lemma 4.1 and Corollary 5.3: False general claim for $N = D_x\nu$ (and the KdV mass charge)
* **Location:** [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L204-L210) (Lemma 4.1) and [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L272) (Corollary 5.3).
* **The claim:** Lemma 4.1 asserts: *"Moreover, every law with density $N=D_x\nu$ for a local $\nu$ has the defect charge $\nu_+-\nu_-$."* Corollary 5.3 invokes this to deduce a defect charge for the KdV mass law (*"mass, which is topological in the potential variable"*).
* **Why it fails as stated:** By Definition (4.1) ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L192-L195)), a defect charge $Q_d$ for a bulk conservation law $(N, J)$ must satisfy
  $$D_t Q_d \equiv J_-\big|_{x=0} - J_+\big|_{x=0} \pmod{\langle C\rangle} \quad \text{on }\Gamma_d,$$
  i.e., **using only the sewing equations at $x=0$, off the bulk shell**. For $Q_d = \nu_+ - \nu_-$, we have $D_t Q_d = (-D_t\nu_-) - (-D_t\nu_+)$. In the bulk, $D_t(D_x\nu) + D_x J = 0$ on shell only implies $D_x(D_t\nu + J) = 0$ on shell; off shell (and on $\Gamma_d$), $J$ is **not** equal to $-D_t\nu$ unless $(N, J)$ is literally the trivial current $(D_x\nu, -D_t\nu)$.
* **What actually happens in KdV:** For the potential KdV Lagrangian $\mathcal L(p) = \frac{1}{2}p_x p_t - p_x^3 - \frac{1}{2}p_{xx}^2$, the Ostrogradsky momentum is $\pi_0 = \frac{1}{2}p_t - 3p_x^2 + p_{xxx}$. In the KdV row of Lemma 5.2 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L262)), Law 1 is $(N_1, J_1) = (p_x, p_{xxx} - 3p_x^2) = (D_x p, \pi_0 - \frac{1}{2}p_t)$. Notice that $J_1 \ne -p_t$ off shell! Instead, we have the exact off-shell decomposition
  $$(N_1, J_1) = -(N_{\text{shift}}, J_{\text{shift}}) + \frac{1}{2}(D_x p, -D_t p),$$
  where $(N_{\text{shift}}, J_{\text{shift}}) = (-\frac{1}{2}p_x, -\pi_0)$ is the Noether current of the constant field shift $(p, q) \mapsto (p + \epsilon, q + \epsilon)$. On $\Gamma_d$, the trivial current $\frac{1}{2}(D_x p, -D_t p)$ has defect charge $\frac{1}{2}(q - p)$ for *any* defect, whereas $-(N_{\text{shift}}, J_{\text{shift}})$ has defect charge $\frac{1}{2}(q - p)$ **only because** the KdV defect $\mathcal L_d = \frac{1}{4}(qp_t - pq_t) + f(p-q,\dots)$ is shift-invariant up to the gyroscopic total derivative (giving $\pi_{-,0} - \pi_{+,0} = \frac{1}{2}(q_t - p_t)$ by the first part of Lemma 4.1). The two halves sum to $Q^1 = q - p$.
* **Fix:** In Lemma 4.1, replace *"every law with density $N=D_x\nu$"* by *"every trivial law $(N, J) = (D_x\nu, -D_t\nu)$"*. In Corollary 5.3, note that the KdV mass law is the sum of $\frac{1}{2}(D_x p, -D_t p)$ and the constant-shift Noether current, each contributing $\frac{1}{2}(q - p)$.

---

### 2. Lemma 6.3 (Top-Order Lemma): Statement and proof fail as written for second-order-in-time wave equations
* **Location:** [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L311-L313).
* **The claim:** *"Let $v_t=F[v]$ be an evolution system of order $m\ge1$ in $x$ whose highest-order symbol is invertible; this includes second-order-in-time wave equations written for $(\phi,\phi_t)$. A differential function $R[v]$ with $D_tR=0$ on shell is constant. Proof. If $R$ depends on $v_k$ with $k$ maximal, then $D_tR$ contains $\partial R/\partial v_k\cdot\partial F/\partial v_m\cdot v_{k+m}$, which is linear in a jet variable of order $k+m$ that no other term contains. Hence $\partial R/\partial v_k=0$, and induction leaves a constant."*
* **Why it fails as written:** Write a second-order-in-time wave equation $\phi_{tt} = \phi_{xx} - U'(\phi)$ ($m=2$) or Boussinesq ($m=4$) as a first-order system for $v = (\phi, \chi)^T$:
  $$\begin{pmatrix}\phi \\ \chi\end{pmatrix}_t = F[v] = \begin{pmatrix}\chi \\ G(\phi,\dots,\phi_m)\end{pmatrix}.$$
  1. The highest-order symbol of $F[v]$ at order $m$ is
     $$\frac{\partial F}{\partial v_m} = \begin{pmatrix} 0 & 0 \\ \partial G/\partial\phi_m & 0 \end{pmatrix},$$
     which is **nilpotent (not invertible)**.
  2. If $R[\phi, \chi]$ depends on $\phi_k$ with $k$ maximal, and does not depend on $\chi_k$, then $D_t \phi_k = \chi_k$ has $x$-order $k$, not $k+m$. Thus $D_t R$ contains **no** jet variable of order $k+m$, and $\frac{\partial R}{\partial v_k} \frac{\partial F}{\partial v_m} = \big(\frac{\partial R}{\partial\phi_k}, 0\big)\begin{pmatrix}0&0\\ \partial G/\partial\phi_m&0\end{pmatrix} = (0,0)$ vanishes identically even when $\frac{\partial R}{\partial\phi_k} \ne 0$.
* **Fix:** Treat second-order-in-time systems $\phi_t = \chi$, $\chi_t = G(\phi, \dots, \phi_m)$ (with $\partial G/\partial\phi_m$ invertible, $m \ge 1$) by comparing the maximal $x$-order $k$ of $\phi$ in $R$ and the maximal $x$-order $l$ of $\chi$ in $R$:
  - If $k > l$ (including when $R$ is independent of $\chi$, $l = -\infty$), the unique highest $\chi$-jet in $D_t R$ is $\chi_k$, with coefficient $\partial R/\partial\phi_k = 0$.
  - If $l \ge k$ and $l \ge 0$, the unique highest $\phi$-jet in $D_t R$ is $\phi_{l+m}$, with coefficient $(\partial R/\partial\chi_l)(\partial G/\partial\phi_m) = 0$.

---

### 3. Lemma 6.5: Incorrect transformation law under Lorentz boosts and missing $w \ne 0$ hypothesis
* **Location:** [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L323-L325) and [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L390-L398).
* **The claim:** Lemma 6.5 assumes a one-parameter group $g_\theta$ of point symmetries of $\mathcal L$ *"maps the family to itself with $\epsilon\mapsto e^{w\theta}\epsilon$, and transforms $\mathcal G$ with weight $w_0$"*, and concludes *"Then $g_\theta^*Q_n=e^{(w_0+nw)\theta}Q_n$ modulo trivial densities. If $g_\theta$ acts on the Fourier variable of the linearised theory by $k\mapsto k_\theta$, the quadratic symbol $m_n(k)$ of $Q_n$ satisfies $m_n(k_\theta)=e^{(w_0+nw)\theta}m_n(k)$, up to the Jacobian factor of the measure. Nonzero symbols with distinct $n$ are therefore linearly independent."*
* **Why it fails for Lorentz boosts (and when $w = 0$):**
  1. **Vector transformation of $(\mathcal G, \mathcal F)$ under boosts:** While Lemma 6.5 accurately describes *dilations* (which preserve $t = \text{const}$ slices), a Lorentz boost $g_\theta$ mixes $x$ and $t$ and does **not** transform the generating density $\mathcal G = \mathcal E_d = \mathrm{Pot}^0$ with a scalar weight $w_0$. By Lemma 5.5 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L287-L293)), $(\mathcal G, \mathcal F) = (\mathcal E_d, P_d)$ transforms as a Lorentz 2-vector: $\mathcal G$ mixes with the flux $\mathcal F = P_d$.
  2. **1-form pullback and Stokes' theorem:** Consequently, $g_\theta^* Q_n$ is not equal to $e^{(w_0+nw)\theta} Q_n$ modulo $D_x(\dots)$ on a fixed-time slice. Rather, the on-shell closed 1-form $\alpha^{(\epsilon)} = \mathcal G^{(\epsilon)} dx - \mathcal F^{(\epsilon)} dt$ satisfies $g_\theta^* \alpha^{(\epsilon)} = \alpha^{(\epsilon e^{w\theta})}$. By Stokes' theorem on shell, the **integrated conserved functional** $\bar Q_n[\phi] = \int_{t=0} Q_n\,dx$ satisfies $\bar Q_n[g_\theta^* \phi] = e^{nw\theta}\bar Q_n[\phi]$ (with $w_0 = 0$ on the 1-form).
  3. **The $\omega(k)$ factor in the sine-Gordon symbol:** On the linearised mass shell $k = m\sinh\vartheta, \omega(k) = m\cosh\vartheta$, the Lorentz-invariant measure is $d\vartheta = dk/\omega(k)$, so $dk$ has Jacobian $\omega(k_\theta)/\omega(k) = \cosh(\vartheta+\theta)/\cosh\vartheta$. That is why in the sine-Gordon row of Section 7.2 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L392)), $m_{2j+1}(\vartheta) = 4(-1)^j \omega\,e^{(2j+1)\vartheta}$ is **not** itself an eigenfunction of $\vartheta \mapsto \vartheta + \theta$, whereas $m_{2j+1}(\vartheta)/\omega(\vartheta) = 4(-1)^j e^{(2j+1)\vartheta}$ is.
  4. **Missing $w \ne 0$ condition:** Both Lemma 6.5 and Theorem 8.1(C) omit the hypothesis $w \ne 0$ (and that $k \mapsto k_\theta$ has non-trivial orbits). If $w = 0$, the exponents $w_0 + n w$ are identical for all $n$.
  5. **Branch uniqueness:** The proof begins *"Uniqueness in Lemma 6.2 makes the branch covariant"*, but Lemma 6.5 (and Theorem 8.1(C)) only refers to Definition 6.1, which does not include the uniqueness hypothesis of Lemma 6.2.

---

### 4. Proposition 7.5: Omission of quadratic bulk time-evolution terms $F_2[v]$ in the generating symbol proof
* **Location:** [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L382-L384).
* **The claim:** Proposition 7.5 computes the generating quadratic symbol $m(k; \epsilon) = \sum_n \epsilon^n m_n(k)$ by evaluating $\mathcal G$ on the linearised plane wave $\phi = \eta(a E + \bar a E^{-1})$, $E = e^{i(kx - \omega(k)t)}$, using the linearised operators $D_x = ik E\partial_E$ and $D_t = -i\omega(k)E\partial_E$, and solving the branch equation for the first harmonic at $O(\eta)$ and the zero mode at $O(\eta^2)$. The proof argues: *"$D_x$ and $D_t$ annihilate zero modes, and the linearised branch equation has constant coefficients. Hence neither the second harmonics nor the second-order correction to $\phi$ contribute."*
* **Why the proof has a gap in general:** In Theorem 6.4, the charges $Q_n[v]$ are functionals of the spatial phase-space state $v$ at fixed $t$, defined by using the **full nonlinear bulk equation** $v_t = F_1[v] + F_2[v] + F_{\ge 3}[v]$ whenever $D_t$ acts on the formal branch $\Delta[v; \epsilon] = \Delta^{(1)}[v; \epsilon] + \Delta^{(2)}[v; \epsilon] + \dots$. By the chain rule, the homogeneous quadratic part of $D_t \Delta[v; \epsilon]$ is
  $$\big(D_t \Delta\big)^{(2)}[v] = D_{\Delta^{(2)}}[F_1[v]] + D_{\Delta^{(1)}}[F_2[v]].$$
  When evaluated on a first harmonic $v_1 = a E + \bar a E^{-1}$, the first term $D_{\Delta^{(2)}}[F_1[v_1]]$ has zero spatial average, **but the second term $D_{\Delta^{(1)}}[F_2[v_1]]$ has spatial average**
  $$\frac{\partial \Delta^{(1)}}{\partial v}\Big|_{k=0} \cdot \big(\text{zero mode of } F_2[v_1]\big).$$
  This term is completely absent when $D_t$ is replaced by the linearised operator $-i\omega(k)E\partial_E$.
  - Whenever $F_2[v]$ is not a total $x$-derivative (for instance, in any relativistic scalar theory with $U'''(0) \ne 0$, such as Tzitzéica or $a_r^{(1)}$ affine Toda for $r \ge 2$), the zero mode of $F_2[v_1]$ is nonzero and shifts the $O(\eta^2)$ zero mode of $\Delta$.
  - Moreover, if one instead tried to include a second-order correction $\eta^2 \phi_2$ so that $\phi = \eta\phi_1 + \eta^2\phi_2$ solves the nonlinear bulk equation to $O(\eta^2)$, then (a) $\phi_2$ has a nonzero zero mode $B_0 = -(U'''(0)/m^2)|a|^2$ whenever $U'''(0) \ne 0$ (which is *not* annihilated by algebraic terms in the branch equation), and (b) substituting $\eta\phi_1 + \eta^2\phi_2$ into $Q_n = Q_{n,1} + Q_{n,2} + \dots$ contaminates $Q_{n,2}[\phi_1]$ with $Q_{n,1}[\phi_2] = Q_{n,1}[B_0] \ne 0$ whenever $Q_{n,1}$ is a non-trivial linear part.
* **Why the table in Section 7.2 is still right, and how to fix Proposition 7.5:**
  - If $\frac{\partial\mathcal G}{\partial\Delta}\big|_{v=\Delta=0} = 0$ (which holds in sine-Gordon, affine Toda, Tzitzéica, NLS, and mKdV, where $\mathcal G$ starts at quadratic order), the $O(\eta^2)$ zero mode of $\Delta$ **does not enter $\mathcal G$ at order $\eta^2$ at all** — only the $O(\eta)$ first harmonic $\Delta^{(1)}$ enters!
  - If $\frac{\partial\mathcal G}{\partial\Delta}\big|_{v=\Delta=0} \ne 0$ (which holds in KdV and Boussinesq, where $\mathcal G = \pm\Delta$), Proposition 7.5 requires that the quadratic bulk nonlinearity $F_2[v]$ have vanishing zero mode on first harmonics (which holds in KdV and Boussinesq because $F_2 = 3D_x(u^2)$ and $F_2 = (0, c^2\lambda D_x(u_x^2))$ are total $x$-derivatives). State this explicitly in Proposition 7.5.

---

### 5. Theorem 7.3 (Involution): Missing hypothesis $\{Q_{n,1}, H\} = 0$ when linear parts are present
* **Location:** [paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L370-L376).
* **The claim:** Theorem 7.3 assumes $\{Q_n, H\} = 0$ and condition $\text{(L)}\ \{Q_{n,1}, Q_m\} = 0$ for all $n, m$, and states in the proof: *"Each $Q_{n,2}$ is conserved by the linearised flow, so under (NR2) it is a function of the actions"*.
* **Why there is a gap:** Expanding $0 = \{Q_n, H\} = \{Q_{n,1} + Q_{n,2} + \dots,\, H_2 + H_3 + \dots\}$ at homogeneous degree $2$ gives
  $$\{Q_{n,2}, H_2\} + \{Q_{n,1}, H_3\} = 0.$$
  Condition (L) as written only assumes $\{Q_{n,1}, Q_m\} = 0$ for the hierarchy charges $Q_m$, not $\{Q_{n,1}, H\} = 0$ (nor that $H$ belongs to the span of $\{Q_m\}$). Without $\{Q_{n,1}, H_3\} = 0$, $Q_{n,2}$ need not be conserved by $H_2$.
* **Fix:** Include $\{Q_{n,1}, H\} = 0$ in condition (L) (or require that $Q_{n,1}$ be a Casimir of $\mathcal J$ or generate a symmetry of $H$ as well as of $Q_m$).

---

## Part II. Secondary Technical Issues and Clarifications

1. **Theorem 3.3 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L144-L166)): Wording of *"modulo $\operatorname{Im} D_t$ and $t$-derivatives of $C$"* and $\{C = 0\}$.**
   - In line 144, Theorem 3.3 writes $\mathcal H_- - \mathcal H_+ + D_t\widetilde P \equiv \rho\cdot C$ *"modulo $\operatorname{Im} D_t$ and $t$-derivatives of $C$"*. By the telescoping identity (integration by parts in $t$), any element $\sum_{k\ge 0} f_k(Y) D_t^k C(Y) \in \langle C\rangle$ can be written as $\rho(Y)\cdot C(Y) + D_t B(Y)$ with $\rho(Y) = \sum_{k\ge 0} (-D_t)^k f_k(Y)$. However, if a term $f_k(Y) D_t^k C(Y)$ ($k \ge 1$) were simply discarded as a "$t$-derivative of $C$" without integrating it by parts into $\rho\cdot C$, its $t$-Euler derivative on the constraint locus would be $D_C^*((-D_t)^k f_k) \ne 0$, giving the wrong multiplier $\rho$.
   - Fix: State that by integrating by parts in $t$, any element of $\operatorname{Im}D_t + \langle C\rangle$ takes the form $\rho\cdot C \pmod{\operatorname{Im}D_t + \langle C\rangle^2}$, and note in line 158 that $E_Y(\rho\cdot C) = D_C^*\rho$ holds on the prolonged constraint locus $\{D_t^k C = 0\ \forall k \ge 0\}$.

2. **Definition 7.1(NR) ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L354-L358)): Analytic proof for all $n \ge 3$ instead of numerical checks at $n = 3, 4$.**
   - Definition 7.1(NR) requires $\Omega = \sum_{i=1}^n s_i\omega_{j_i}(k_i)$ not to vanish on any open subset of $\sum_{i=1}^n s_i k_i = 0$ **for every $n \ge 3$**, whereas line 358 only cites a check at degrees $n = 3$ and $n = 4$.
   - In fact, (NR) holds for **all $n \ge 3$ at once** by a two-line derivative test whenever no branch $\omega_j(k)$ is affine on an open interval ($\omega''_j(k) \not\equiv 0$ on open intervals): on the hyperplane $k_n = -s_n \sum_{i=1}^{n-1} s_i k_i$ with $n - 1 \ge 2$, differentiating with respect to $k_1$ and $k_2$ gives
     $$\frac{\partial^2 \Omega}{\partial k_1 \partial k_2} = s_1 s_2 s_n\,\omega''_{j_n}(k_n).$$
     If $\Omega$ vanished on a nonempty open subset of the hyperplane, $\omega''_{j_n}$ would vanish on a nonempty open interval, which fails for every massive dispersion relation in the table ($\pm\sqrt{k^2+m^2}$, $k^2$, $k^3$, $\pm ck\sqrt{1+\kappa^2 k^2}$). Including this two-line proof establishes (NR) for all $n \ge 3$ rigorously.

3. **Theorem 6.4 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L315-L321)): Implicit hypotheses from Proposition 4.2.**
   - The proof of Theorem 6.4 applies Proposition 4.2(A) and Proposition 4.3 to a formal branch (Definition 6.1). Proposition 4.2 requires condition (I) (so that $E_+[\psi(\epsilon)] = 0$ follows from $E_-[\phi] = 0$ via Theorem 3.3(b)), the top-order property of Lemma 6.3 for the bulk equation, and that the residual $R = D_x Q^2 + (N_{2,-} - N_{2,+})$ vanishes at the vacuum (i.e. $N_2(\phi_{\text{vac}}) = N_2(\psi_{\text{vac}})$, which is distinct from $\mathcal G|_{\text{vac}} = 0$). These should be stated in Theorem 6.4 or built into Definition 6.1.

4. **Lemma 5.4 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L281-L283)): Strict scaling vs *"up to total derivatives"*.**
   - If $\mathcal L_\pm \circ \delta_s = s^w \mathcal L_\pm$ held only up to total derivatives, the total-derivative terms would alter the Ostrogradsky momenta $\pi_m$ and $\mathcal H_\pm$. The proof uses strict homogeneity $\mathcal L_\pm \circ \delta_s = s^w \mathcal L_\pm$, which holds in all the paper's examples.

5. **Lemma 5.5 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L287-L293)): Promoted solutions vs off-shell momentum balance at $x = 0$.**
   - Lemma 5.5 boosts the stress-potential equations $\Delta T^{\mu\nu} = \varepsilon^{\mu\rho} D_\rho \mathrm{Pot}^\nu$ along *promoted solutions* (which satisfy the bulk equations) and concludes in the final sentence: *"When that relation is in sewing form at $x=0$, it is a momentum-conserving defect."* Definition 3.1 requires the momentum balance to hold off shell for arbitrary boundary $t$-jets at $x=0$. To bridge this without assuming jet-density of global solutions at $x=0$, note that on $\Gamma_d$ the spatial derivative $D_x$ along the tangent vector $\delta Y = (a_-, a_+, \rho)$ of Theorem 3.3(a) satisfies $D_x z_\mp = X_\mp(z_\mp)$ (and hence $E_\mp = 0$ by Lemma 2.2) purely as an identity on the $t$-jet space of $\Gamma_d$.

6. **Lemma 6.2 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L307-L309)): Algebraic nonlinearities in $\Delta$ at order $\epsilon^0$.**
   - Lemma 6.2 writes $G = M\Delta + O(\epsilon)$, whereas in Lemma 6.6 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L333)) it is applied to $\nabla_\Phi \mathcal B_-(\phi, \phi+\Delta) + O(\epsilon) = -\mathsf H \Delta + O(\Delta^2) + O(\epsilon)$, which contains $O(\Delta^2)$ terms at order $\epsilon^0$. Writing $G = M\Delta + O(\Delta^2, \epsilon)$ (with derivatives of $\Delta$ entering only in the $O(\Delta^2, \epsilon)$ part at positive total order) makes Lemma 6.2 match its application in Lemma 6.6.

7. **Lemma 2.1 ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L86-L88)) and Appendix A ([paper.md](file:///home/gustav/Git/affine_toda/defect-integrability/general_framework/paper.md#L466)): Minor variational-complex precision.**
   - In Lemma 2.1, two currents with the same characteristic $Q$ in Olver's sense ($D_t N + D_x J = Q\cdot E(\mathcal L) + \operatorname{Div} R$ with $R = 0$ on shell) differ by $(D_x C, -D_t C) + \text{const}$ **plus a trivial current of the first kind** $R$ (vanishing on shell), unless "with the same characteristic" is restricted to currents satisfying the exact off-shell identity (2.5).
   - In Appendix A line 466, vanishing of $E^{(t)}_Y(\mathcal H_- - \mathcal H_+)$ implies $\mathcal H_- - \mathcal H_+ \in \operatorname{Im} D_t + \mathbb R$; the additive constant vanishes when $\Gamma_d$ contains a shared vacuum where $\mathcal H_- = \mathcal H_+$.
