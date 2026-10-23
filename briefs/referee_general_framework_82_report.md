# Referee report: general-framework §8.2 and Proposition 7.5

Date: 23 October 2026. Reviewer: Codex, GPT-6.

Reviewed checkout: `b1e97de2cb74b07becdcdc2f584e3248c7324a5c`. The three manuscripts reviewed below are unchanged from the requested commit `09b5ced15840b87e63087eaf1ff58e827ab23921` (`git diff 09b5ced HEAD --` those files is empty). Line numbers refer to this checkout.

Files: `defect-integrability/general_framework/paper.md` (abbreviated **paper**), `defect-integrability/general_framework/guide.md` (**guide**), and `defect-integrability/defect_integrability_paper.md` (**[23]**). No existing file was edited. No agents were spawned, no rendering was performed, and no mutating git command was run.

## Overall assessment and evidence

Propositions 8.2–8.3 and the substantive conclusion of Theorem 8.4 survive this review. The changes needed are principally:

1. Correct the Toda sentence `hat g = g`: with the proposition's notation it is `hat g = sigma g`.
2. Add the short argument establishing analyticity of the split defect potential in Theorem 8.4, or assume it explicitly.
3. Extend Proposition 7.5 to generating densities with zero first variation at the vacuum. The proposed extension is valid. The present claim that the shortcut fails for Toda and Tzitzéica is too restrictive.
4. Credit the general momentum-conservation splitting already present in Bristow–Bowcock [10], and distinguish it from the normalization/transparent-branch results restated from [23].
5. Correct several scope statements in the guide, especially the inclusion of equal-mass several-field theories among cases outside the Type-I result.

There is also a useful strengthening: the exact polarized generating symbols computed below prove independence and involution for the reviewed A2 defect using Section 7, without relying on the unreviewed theorem of [23]. The normalized family and its formal branch extend to every standard real-coupling A_r affine Toda defect, not just A2.

Independent executable evidence:

- `referee_scratch/general_framework_82/independent_checks.py`
- `referee_scratch/general_framework_82/independent_checks_output.txt`

The script imports only SymPy, not manuscript code. It gives **30 PASS, 0 FAIL**, including exact exponential coefficient matching for A2 through A6, the transparent Hessians, the A2 nonlinear branch and energy coefficients through cubic amplitude, both polarized quadratic symbols, and the Tzitzéica auxiliary-field first variation. All-r conclusions below have written proofs; the finite-r checks supplement them.

For comparison only, I ran `python3 check_type1_family.py` from its directory: all 15 checks pass. Those checks are not used as independent evidence. Source comparisons used the local arXiv text/PDF copies in `/home/gustav/referee-copy/papers/`; arXiv records were also checked online. Source quotations below are short exact excerpts; displayed calculations not marked as quotations are my own derivations or translations.

## 1. Proposition 8.2: splitting

**Verdict: correct locally.** The derivative-free restriction is stated at paper line 474 and used explicitly at line 484. The suggested simply-connectedness objection is not a missing substantive hypothesis in this local argument.

Write `a=phi_t`, `b=psi_t`, `A=B_phi`, `C=B_psi`. Varying the kinetic terms, including the time integration by parts, gives

\[
 E^{(t)}_\phi L_d=Ea+Db-A,\qquad
 E^{(t)}_\psi L_d=Eb-D^Ta-C.
\]

Since the spatial momenta are minus the spatial derivatives, (3.1) gives

\[
 \phi_x=Ea+Db-A,\qquad \psi_x=D^Ta-Eb+C.
\]

For a general constant D with the same skew matrix E on both sides, the quadratic velocity part of `H_- - H_+` is

\[
 \tfrac12a^T(DD^T+E^2-I)a
 +\tfrac12b^T(I-D^TD-E^2)b
 +a^T(ED-DE)b.
\]

Thus the necessary and sufficient cancellation conditions are

\[
 DD^T=D^TD=I-E^2,\qquad [E,D]=0.
\]

`D=I-E` is sufficient, not necessary: `E=0`, `D=-I` is an immediate counterexample to necessity. The proposition fixes the normalized choice; its proof does not claim necessity.

Under that choice, direct expansion leaves

\[
 a^T(DC-EA)+b^T(D^TA+EC)
 -\tfrac12 A^TA+\tfrac12 C^TC+U(\phi)-U(\psi).
\]

Matching the independent velocities in the balance with `D_t Ptilde` gives

\[
 \widetilde P_\phi=EA-DC,\qquad
 \widetilde P_\psi=-D^TA-EC,
 \qquad \tfrac12(A^TA-C^TC)=U(\phi)-U(\psi).
\]

The inverse transformation is indeed `phi=w+Dq`, `psi=w-D^Tq`, because `D+D^T=2I`. For column gradients its chain rule is

\[
 \nabla_w=\nabla_\phi+\nabla_\psi,\qquad
 \nabla_q=D^T\nabla_\phi-D\nabla_\psi.
\]

Substitution gives `Ptilde_w=-B_w` and `Ptilde_q=B_q`. Differentiating these identities gives `-B_wq=B_wq`, hence `B_wq=0`. On a sufficiently small product neighbourhood this integrates to `B=f(w)+g(q)`, `Ptilde=g-f+constant`. Finally

\[
 B_\phi=\tfrac12(Df'+g'),\qquad
 B_\psi=\tfrac12(D^Tf'-g'),
 \quad \tfrac12(|B_\phi|^2-|B_\psi|^2)=\tfrac12f'^Tg'.
\]

This proves the printed identity and its converse, including all signs.

**Domain.** The momentum function is assumed to exist; no closed one-form is being integrated to establish its existence. Equality of its mixed derivatives is local and does not require simple connectedness. Local splitting follows on a product neighbourhood. A global splitting on an arbitrary domain with disconnected coordinate fibres is a different assertion; neither connectedness nor an unqualified appeal to simple connectedness substitutes for specifying the domain. The intended germ near the vacuum is sufficient.

Optional precision at **paper line 474**: replace “Then, up to additive constants,” by:

> Then, locally on a product neighbourhood in the coordinates `(w,q)` and up to additive constants,

**Published kinetic terms.** In [1], eq. (1.2), the scalar kinetic term is `(phi psi_t-psi phi_t)/2`. Its difference from `phi psi_t` is `-D_t(phi psi/2)`. For an autonomous endpoint function K, `E^{(t)}(D_tK)=0` and

\[
 \sum y_t\frac{\partial D_tK}{\partial y_t}-D_tK=0.
\]

Therefore the sewing equations and energy are unchanged. In [2], eq. (3.1) already has the printed kinetic representative, and eq. (3.11) sets `F=E=I-D`; no additional total derivative is needed. The paper's statement is correct for these representatives. It should not be generalized to arbitrary explicitly time-dependent boundary terms without qualification.

## 2. Proposition 8.3: scalar Hessian and rescaling

**Verdict: correct proposition; wrong normalization shorthand in the following Toda example.**

Differentiating the constraint in q at zero gives

\[
 (D^T+D)U'(w)=\tfrac12Gf'(w),\qquad Gf'=4U'.
\]

Thus `G f''=4 U''`. Transposition, using symmetry of all Hessians, gives `G f''=f'' G`, and multiplication gives `[G,U'']=0`. In an orthogonal eigenbasis of G, every mixed Hessian block of U between distinct eigenspaces vanishes. On a product neighbourhood, integrating these zero mixed derivatives expresses U as a sum of functions on the eigenspaces. Any possible affine terms are themselves sums on the eigenspaces; `U'(0)=0` fixes the vacuum normalization. Irreducibility then forces one eigenvalue, `G=gamma I`, and invertibility forces `gamma != 0`.

The irreducibility needed here is exactly local orthogonal indecomposability of the **bulk potential**, not of the bulk-defect pair. In line 489, “nontrivial orthogonal splitting” would avoid the literal zero-dimensional-summand ambiguity; this is plainly the intended meaning and is explicit in [23].

With the constants removed, `f=4U/gamma`. The rescaling is algebraically

\[
 \lambda f+\lambda^{-1}g
 =\epsilon U+\epsilon^{-1}\frac4\gamma g,
 \qquad \epsilon=4\lambda/\gamma.
\]

It preserves `f'^Tg'`, so the momentum is the rescaled `g-f`; `hat g''=4I`; and setting `lambda=1` gives the original member `epsilon=4/gamma`. Assuming `G=gamma I` directly does replace irreducibility. No positivity of gamma is needed for this algebra. If a family parameter is required to be positive as in Definition 6.1, a negative original gamma is accommodated by reversing the parameter on the negative component; this is a parameter convention, not an obstruction to a formal branch.

All the listed bulk assumptions are stated in the paragraph at paper line 468. Positivity of M is not needed for the scalar-Hessian argument, but is used subsequently for (NR) and for the analytic argument in item 3. `U(0)=0` fixes the constant in `f=4U/gamma`. No hidden bulk assumption is needed.

**Actual typo.** In the proposition, g includes the coefficient `sigma^{-1}`. For Toda put

\[
 h(q)=\sum_j e^{\alpha_j^TDq}-(r+1),\qquad
 f=\sigma U,\quad g=\sigma^{-1}h.
\]

Then `gamma=4/sigma` and `hat g=(4/gamma)g=sigma g=h`, not `g`. The check script silently uses `gT` for h and correctly checks `(4/gamma)(gT/sigma)=gT`; that does not justify using the same g for both functions in the prose.

Replace the Toda sentence at **paper line 499** by:

> For the $a_2^{(1)}$ Toda defect of [2], write $h(q)=\sum_j e^{\alpha_j\cdot Dq}-3$, so that $f=\sigma U$ and $g=\sigma^{-1}h$. Then $\gamma=4/\sigma$, $\hat g=h=\sigma g$, and the given defect is the member $\epsilon=\sigma$.

## 3. Theorem 8.4 and Lemma 6.6

**Verdict: correct conclusion and formal-branch proof. Add a short analytic justification to make the written proof self-contained.**

The coefficient one-forms are

\[
 A_\Phi=-\tfrac12E\phi,\qquad
 A_\Psi=D^T\phi-\tfrac12E\psi.
\]

They have no parameter singularity. For `B_-=hat g((phi-psi)/2)`, its value and gradient vanish at every point of the diagonal and its phi Hessian is `hat g''(0)/4=I`. The remaining potential is `epsilon U(w)`, so `B_0=0` and `B_1=U(w)`.

Here is an independent check of the formal argument. Put `psi=phi+Delta` and multiply the left sewing equation by epsilon. Its algebraic leading part is `-Delta+O(Delta^2)`; all derivatives of Delta have positive epsilon order. The coefficient of `epsilon^n` determines `Delta_n` from lower coefficients. The cross Euler linearization has leading term `epsilon^{-1}I`. Acting on a nonzero Laurent series bounded below, this term cannot be cancelled by its order-zero differential part. Thus the formal kernel required to vanish in Lemma 3.5 is zero, and the right sewing equation follows on every bulk solution. This proves both sewing equations, not only the left one. Neither an additional condition on `B_0` nor a nondegeneracy condition on the gyroscopic coefficients is needed. For this family the vacuum solution is exactly `Delta=0`; uniqueness makes every coefficient vanish there.

The energy is B because the kinetic terms are homogeneous of degree one in the velocities. Since U and `hat g` start quadratically and the branch fixes the vacuum, every charge has zero linear part. Consequently (L) and (L') hold. The canonical equal-time Poisson operator is constant. Every mass is positive, and for `omega_j=sqrt(k^2+m_j^2)` one has `omega_j''=m_j^2/(k^2+m_j^2)^(3/2)>0`. The mixed-derivative test on each n-wave momentum hyperplane proves (NR) for all `n>=3`, even with repeated masses. Type I makes (I) vacuous. Autonomy supplies the defect energy, the assumed balance supplies the defect momentum, and Lorentz symmetry supplies closure. These prove (A), (B), (D).

For one real field, the only positive-frequency species has nonconstant massive dispersion. Its translation-invariant conserved quadratic functionals are diagonal in the oscillator actions; thus (NR2) holds. For several species the equal-mass obstruction is real, and Theorem 8.4 correctly retains the alternative of checking the actual quadratic charges.

**Analyticity.** Section 8.2 explicitly assumes U analytic but does not explicitly assume B or g analytic. The sentence “They are analytic because U and hat g are” therefore skips a step. It is repairable from the existing assumptions, not a counterexample. Differentiating (8.4) in w at zero gives

\[
 g'(q)=2 f''(0)^{-1}\bigl(U'(Dq)-U'(-D^Tq)\bigr),
 \qquad f''(0)=4M/\gamma.
\]

This is analytic since M is invertible. Integrating along straight lines from zero shows that g is analytic; the formal recursion then gives analytic finite-jet coefficients.

At **paper line 503**, replace the analytic sentence by:

> Analyticity of $g$ follows by differentiating (8.4) in $w$ at $w=0$: $g'(q)=2f''(0)^{-1}[U'(Dq)-U'(-D^Tq)]$, where $f''(0)=4M/\gamma$ is invertible. The formal recursion therefore gives analytic densities.

The theorem is a proved conditional formal-existence statement, not a mere convention identity. Its label is justified after making this short implication explicit. It does not prove the existence of the transparent critical point, convergence, or the remaining independence/involution conditions for the general class.

## 4. Published defects and the all-r extension

**Verdict: correct, subject to the notation repair in item 2. Theorem 8.4 can safely be applied to every standard real-coupling A_r defect, using the scalar-G alternative.**

**Sine-Gordon.** Direct differentiation gives `G=2/sigma`, `hat g=4(1-cos q)`, and `epsilon=2sigma`. The constraint reduces to

\[
 (1-\cos(w+q))-(1-\cos(w-q))=2\sin w\sin q
 =\tfrac12(2\sigma\sin w)(2\sigma^{-1}\sin q).
\]

For the source comparison, [1], eq. (2.13), gives the exponential sinh-Gordon potential and its reciprocal parameter coefficients. Continuing the coupling to imaginary values, rescaling the field so that the cosine argument is phi, and measuring length in units of the physical inverse mass gives `U=1-cos phi` and `B=-2sigma cos w-2sigma^{-1}cos q`. Adding the vacuum constant gives the paper's formula. Equivalently, in [1]'s conventions set the continued real cosine coupling b by `phi=sqrt(2)b phi_source` and use physical bulk mass `2m`; the common action factor is removed and the resulting coefficients are precisely 2. The kinetic total derivative was checked in item 1. [1] states: “There is a single free parameter σ in the defect condition”. [Source: §2, eq. (2.13)](https://arxiv.org/abs/hep-th/0305022).

**Toda transcription.** [2], eqs. (3.1), (3.11), (3.21), (4.3) and the coefficient condition following (4.4) give the same kinetic matrix and exponential arguments as the manuscript. Set the suppressed bulk mass and coupling to one and the simply-laced root lengths to 2. Its coefficients then obey `d_j s_j=1`, with the cyclic condition making them constant: take `d_j=sigma`, `s_j=sigma^{-1}`. Subtracting the vacuum constants gives exactly `sigma U(w)+sigma^{-1}h(q)`. Both bulk potentials use the same root coordinates: no right-only rotation is required. [Source](https://arxiv.org/abs/hep-th/0401020).

**Independent symbolic proof for all ranks.** Let `N=r+1`, work in the sum-zero hyperplane of `R^N`, let `P e_i=e_{i+1}` cyclically, and take

\[
 \alpha_i=e_i-e_{i+1},\quad D=2(I-P)^{-1},\quad
 M=\sum_i\alpha_i\alpha_i^T=(I-P)(I-P^T).
\]

All inverses in this paragraph are restricted to the sum-zero hyperplane. If H is its orthogonal projector, then

\[
 D\alpha_i=2He_i,\quad D^T\alpha_i=-2He_{i+1},\quad
 -D\alpha_i=D^T\alpha_{i-1},\quad
 \alpha_i^TD^T\alpha_j=2\delta_{ij}-2\delta_{i,j+1}.
\]

It follows, by matching the coefficient of each exponential `exp(alpha_i.w)`, that

\[
 \tfrac12U'(w)^Th'(q)
 =\sum_i e^{\alpha_i^Tw}
 \left(e^{\alpha_i^TDq}-e^{-\alpha_i^TD^Tq}\right)
 =U(w+Dq)-U(w-D^Tq).
\]

This is an identity, not a sample-point test. Moreover

\[
 h'(0)=D^T\sum_i\alpha_i=0,\qquad
 h''(0)=D^TMD=4I.
\]

M is positive definite on this hyperplane and all potentials are analytic. Thus `G=4I/sigma`, `hat g=h` and `epsilon=sigma` for every rank, including the A1 sinh-Gordon normalization. The script matches the exponent covectors exactly for ranks 2 through 6 and checks the Hessians; all 15 of these checks pass. For A2, in orthonormal coordinates, `M=3I`, `E^2=-I/3`, `D^TD=4I/3` and hence `G=3D^TD/sigma=4I/sigma`.

The all-r extension needs the scalar-G alternative explicitly stated after Proposition 8.3, rather than an unproved appeal to irreducibility. It establishes the family and branch, not by itself the entirety of Theorem 8.1. Item 6 supplies the remaining Section 7 calculation for A2.

## 5. Section 9 comment 4, [23], and the overview claims

**Verdict: correct as a conditional application of [23]; it is not an independent verification of [23]'s general theorem. Some overview language should state the scope more precisely.**

Each hypothesis of [23, Theorem 2.1] holds for the reviewed A2 defect:

1. The exponential potential has `U(0)=U'(0)=0`, `M=3I`, and is real analytic.
2. The allowed scalar-G alternative holds by item 4. In fact the bulk is also irreducible: if it split in orthogonal one-dimensional subspaces, its mixed Hessian would vanish for every u. Independence of the three functions `exp(alpha_i.u)` would force every root to lie on one of two perpendicular lines. The three A2 root directions do not. This independently verifies the stronger hypothesis as well.
3. The source action already has `D=I-E` in the same endpoint coordinates in which the two potentials agree. Thus the **normalized** condition is satisfied, not inferred from an arbitrary rotation of the right field. B and `Ptilde=g-f` are analytic and derivative-free, and the exact coefficient identity in item 4 proves the strong balance for independent boundary velocities.
4. `B_q(w,0)=sigma^{-1}h'(0)=0` for every w, and `B_qq(0,0)=4I/sigma` is invertible. This checks the critical manifold, not merely an isolated zero at `w=0`.

Accordingly the conclusion of [23] applies **if its theorem is accepted**. The caveat that [23] has not been independently reviewed is present in comment 4, the guide's A2 paragraph and reference [23]; it is adequate. This report checks the hypotheses and rederives the two imported propositions. It does not certify the entire general equal-time canonicity proof in [23]. For A2, the conclusion also follows independently from item 6 below.

The edited table accurately separates Theorem 8.4 from the independence result. The Status paragraph and abstract do not claim an unconditional proof of the Corrigan–Zambon conjecture. Their shorter descriptions of “constant coupling” should nevertheless be read as the normalized class (8.2), not every constant Type-I coupling. A family and branch can be obtained even without scalar G by reciprocal rescaling of f and g and Lemma 6.6 with its invertible, possibly nonscalar Hessian; the scalar-G/irreducibility condition is needed for the particular normalized conclusion and the invocation of [23]. Thus omitting this distinction is risky when discussing the **remaining** claims of [23].

Suggested replacement for the new bullet at **paper line 50**:

> **Propositions 8.2–8.3 and Theorem 8.4** derive a momentum-conserving family and its formal branch for the normalized Type-I coupling (8.2), assuming a derivative-free defect momentum and a nondegenerate transparent critical point. The normalization (8.5) uses bulk irreducibility, or the alternative that $G$ is a nonzero scalar matrix. These statements supply the family and branch portions of (C), following [23].

At **paper line 543**, use:

> For the normalized Type-I class of Section 8.2, momentum conservation forces the splitting and reciprocal rescaling. A nondegenerate transparent critical point supplies the formal branch. With the additional irreducibility or scalar-$G$ condition of Proposition 8.3, [23] asserts nondegeneracy, independence and involution for this class. Its general theorem has not yet been independently reviewed. The transparent point is assumed, not derived.

The pre-existing sentence at **paper line 47**, “computed in closed form for the observed defects”, overstates the coverage: no Tzitzéica symbol is given there and the Boussinesq claim is evidence only. Replace its last two sentences by:

> Independence is decided by quadratic symbols, whose generating functions are computed for the cases specified in Section 7. No Bianchi-permutability assumption is needed.

Replacement text for comment 4 and §10 item 3 is supplied in item 6, because the new quadratic-symbol result changes what remains open.

## 6. Proposition 7.5 without the F2 condition

**Verdict: the proposed extension is correct when “no linear part” means zero first variation of the generating density in all its independent field/branch jets at the chosen vacuum. The present exclusion of Toda and Tzitzéica is unnecessarily strong.**

### Independent general proof

Work coefficientwise in epsilon, allowing a finite Laurent pole, and expand in a separate amplitude eta about a branch vacuum. Let the independent arguments of the density be collectively Z: bulk jets, difference-field jets, and any auxiliary-field jets after subtracting their vacuum values. Assume `G(0)=0`, `dG(0)=0`, and that the branch fixes this vacuum. Write

\[
 \Delta[\eta v]=\eta L[v]+\eta^2B[v,v]+O(\eta^3),\qquad
 \mathcal G(Z)=\mathcal G_2(Z)+\mathcal G_3(Z)+\cdots.
\]

Then

\[
 [\eta^2]\mathcal G\bigl(\eta v,\Delta[\eta v]\bigr)
 =\mathcal G_2(v,L[v]).
\]

Terms involving B would need a linear term of G to contribute at degree two. In a factor already of degree one, replacing a time derivative by its full evolution instead of the linear evolution changes that factor only at degree two, hence changes a quadratic density first at degree three. The linear branch L itself is computed entirely with the linearized bulk flow. Therefore F2 cannot affect the quadratic symbol. The proof holds with auxiliary fields too, provided their variations are included in `dG(0)=0`.

This sufficient condition concerns the generating density **before nonlinear branch substitution**, modulo a consistently chosen trivial density if desired. Mere cancellation of a linear term after substitution is not the condition proved here. Potential-variable locality and the selected formal-branch hypotheses still matter. In degenerate multiplets one must evaluate all polarizations (and polarize cross terms), not just a single arbitrarily chosen real field direction.

### Full nonlinear A2 computation through cubic order

Use the orthonormal roots and E of [23, §10], which agree with the reviewed defect, and define

\[
 p=u_t,\quad h=p-u_x,\quad \partial_-=D_t-D_x,\quad
 C(a,b)=\sum_i\alpha_i(\alpha_i^Ta)(\alpha_i^Tb),
\]
\[
 T(a,b)=\sum_i\beta_i(\beta_i^Ta)(\beta_i^Tb),\qquad
 \beta_i=D^T\alpha_i,\qquad T_3(a)=a^TT(a,a).
\]

Here `C=U'''(0)` and `T=hat g'''(0)` as symmetric tensors; neither vanishes. In particular

\[
 U(u)=\tfrac32|u|^2+\frac{\sqrt2}{4}(u_1^3-3u_1u_2^2)+O(|u|^4),
\]
\[
 \tfrac16T_3(h)=\frac{2\sqrt6}{9}(h_2^3-3h_1^2h_2).
\]

Combining the two sewing equations gives

\[
 (D_t+D_x)q=-\tfrac\epsilon2U'(w),\qquad
 \hat g'(q)=2\epsilon\partial_-u-2\epsilon D\partial_-q,
 \qquad w=u-Dq.
\]

Using the **full** field equation `p_t=u_xx-U'(u)`, solve `q=epsilon q_1+epsilon^2 q_2+...`:

\[
 q_1=\tfrac12h,\qquad
 q_2=-\tfrac14D\partial_-h-\tfrac1{32}T(h,h)+O(\text{amplitude}^3),
\]
\[
 \partial_-h=2u_{xx}-2p_x-U'(u),\qquad
 U'(u)=3u+\tfrac12C(u,u)+O(|u|^3).
\]

The nonlinear `C(u,u)` term is retained in q2. Expanding the energy density `epsilon U(u-Dq)+epsilon^{-1}hat g(q)` gives its first two coefficients, through cubic amplitude:

\[
 Q_1=\tfrac12|h|^2+\tfrac32|u|^2+\tfrac16u^TC(u,u)+O(\text{amplitude}^4),
\]
\[
 Q_2=h^TDh_x-h^TE\left(3u+\tfrac12C(u,u)\right)
       -\tfrac1{24}T_3(h)+O(\text{amplitude}^4).
\]

Before eliminating time derivatives the second formula is

\[
 Q_2=-\tfrac12U'(u)^TDh-\tfrac12h^TD\partial_-h-\tfrac1{24}T_3(h).
\]

These two representatives agree by the full field equation; `h^Th_x` is a total spatial derivative. The script verifies the branch recursion, directly composes the Taylor expansions to extract Q1 and Q2, and checks the displayed simplification. Thus this computation has not discarded F2 in advance. Its contribution first appears in the cubic term `-h^TEC(u,u)/2`.

### Polarized generating symbols and the remaining A2 conditions

Let `omega=sqrt(k^2+3)`, `ell=omega+k`, and take normalized eigenvectors `z_s=(1,s i)^T/sqrt(2)` of E, with

\[
 Ez_s=i e_s z_s,\qquad e_s=s/\sqrt3,\qquad s=\pm1.
\]

For the real field `u=eta(a z_s exp(ikx-i omega t)+conjugate)`, use `|a|^2` as the amplitude normalization. The linear branch and weighted average amplitudes are

\[
 q/u=\frac{-i\epsilon\ell}{2-i\epsilon\ell(1-i e_s)},\qquad
 w/u=\frac{2}{2-i\epsilon\ell(1-i e_s)}.
\]

The averaged quadratic generating density is therefore

\[
 m_s(k;\epsilon)=
 \frac{4\epsilon(3+\ell^2)}{4-4e_s\epsilon\ell+\tfrac43\epsilon^2\ell^2}.
\]

The independent full-nonlinear Q1 and Q2 above give

\[
 m_{1,s}=3+\ell^2=2\omega\ell,\qquad
 m_{2,s}=e_s\ell(3+\ell^2)=2e_s\omega\ell^2,
\]

exactly the first two coefficients of this rational function. Both polarizations pass the symbolic comparison in the script, reducing only by `omega^2-k^2=3`.

This calculation also deals with the equal-mass issue. The quadratic bulk and defect Hessians are scalar, and the branch is a rational function of E. Consequently the generating quadratic forms are diagonal in the **same** fixed polarization basis for every epsilon. Cross-polarization entries vanish, so all quadratic charge functionals commute. This checks the actual charges; it does not falsely assert (NR2) for all conserved quadratic functionals of the two-field free theory.

For `s=+1`, the coefficient at order n is explicitly

\[
 m_{n,+}(k)=(3+\ell^2)\ell^{n-1}
 3^{-(n-1)/2}\frac{\sin(n\pi/3)}{\sin(\pi/3)}.
\]

It is nonzero exactly when `3` does not divide n. Infinitely many coefficients are nonzero, and any finite selection of these functions is independent: after dividing by the common positive factor, they are distinct powers of ell on an interval. The other polarization changes their signs by `(-1)^(n-1)`. Theorems 7.3–7.4, the already proved branch, analyticity, and the absence of linear parts now establish commutation and finite-subfamily independence for the full A2 charges. This is an independent proof for this example; it does not verify [23] for arbitrary potentials.

### Type-II auxiliary field

For the Tzitzéica model actually used by `check_hierarchy.py`, write its average endpoint field as P, its difference as q, its auxiliary field as lambda, and `epsilon=sigma^{-1}`. The energy is

\[
 \epsilon\left(e^{2P-2\lambda}+2e^{-P+\lambda}\cosh q\right)
 +\epsilon^{-1}\left(4e^{-\lambda}+2e^{2\lambda}\cosh^2q\right).
\]

At `P=q=lambda=0` its value is `3epsilon+6/epsilon`; after subtracting that constant all three first derivatives vanish. In the lambda direction the cancellations are `epsilon(-2+2)` and `epsilon^{-1}(-4+4)`. Thus **there is no linear auxiliary-field term in this Tzitzéica energy**. The script checks all three derivatives. This is not a universal assertion about arbitrary Type-II defect energies. Establishing the complete Tzitzéica hierarchy still requires its branch and symbol calculations; the density criterion alone does not supply them.

### Paste-ready revisions

At **paper line 418**, replace the F2 sentence by:

> Assume either that the first variation of $\mathcal G$ vanishes at the chosen vacuum with respect to all independent bulk, branch and auxiliary-field jets, and the branch fixes that vacuum, or that the quadratic part $F_2$ of the phase-space evolution is zero or a total $x$-derivative.

Replace the instruction about solving the branch at two amplitude orders by:

> When the first variation vanishes, only the linear branch is needed. Otherwise also compute the quadratic zero mode. For a degenerate normal-mode multiplet, apply the prescription to arbitrary polarizations and recover the full Hermitian quadratic symbol by polarization.

At **paper line 420**, before the existing F2 argument insert:

> In the zero-first-variation case, write $\Delta=\eta L[v]+O(\eta^2)$ and $\mathcal G=\mathcal G_2+O(\eta^3)$. Then the quadratic coefficient is $\mathcal G_2(v,L[v])$. The nonlinear part of the evolution and the quadratic part of the branch can first contribute at cubic order. Thus the linearized flow suffices in this case. In the other case the following total-derivative argument applies.

At **paper line 422**, replace the sentence beginning “It fails for Tzitzéica” by:

> Although the $F_2$ condition fails for Tzitzéica and for $a_r^{(1)}$ Toda with $r\ge2$, their vacuum-normalized defect energies have zero first variation, including in the Tzitzéica auxiliary field. The new alternative therefore removes this obstruction; the formal-branch and locality hypotheses must still be checked.

Replace **paper line 532, comment 4**, after incorporating the displayed A2 symbol calculation above into Section 7, by:

> *Affine Toda.* The published normalized Type-I defects satisfy the split momentum identity and have $G=4I/\sigma$; the cyclic-root calculation proves this for every $r$. Hence Theorem 8.4 gives their families and formal branches using the scalar-$G$ alternative. For $a_2^{(1)}$, the two polarized generating symbols computed in Section 7 are diagonal in a common basis. Their nonzero coefficients, at orders not divisible by three, are linearly independent. Theorems 7.3–7.4 therefore prove involution and independence for this example despite the failure of (NR2). The quadratic nonlinearity of the bulk equation is no obstruction because the generating density has zero first variation. The hypotheses of [23, Theorem 2.1] also hold for this defect, but its general theorem has not yet been independently reviewed. The corresponding quadratic-symbol verification for higher rank is not supplied here.

If the editor does not add the A2 symbol calculation, retain the conditional reliance on [23] and replace only the last two sentences by:

> By the methods of Section 7, independence and involution still require a generating-symbol calculation and a check that the quadratic parts commute. The nonzero cubic bulk potential is not an obstruction to the extended Proposition 7.5, since the defect energy has zero first variation. Equal masses require checking the actual quadratic charges in place of (NR2).

Replace **paper line 545, §10 item 3**, when adding the A2 calculation, by:

> **Remaining verifications.** Formal branches are still to be checked for the several-field Type-II defects. The corresponding matrix-symbol calculation for higher-rank affine Toda remains to be supplied by the methods of Section 7; the $a_2^{(1)}$ calculation above establishes its independence and involution. Nonzero $U'''(0)$ does not obstruct Proposition 7.5 when the generating density has zero first variation. Conditions (L) and (L') remain to be checked for Boussinesq.

## 7. Faithfulness of the guide

**Verdict: mostly faithful, but several scope sentences are wrong or need the corrections now established above.**

The nine-step argument in §11.2 reproduces the equations correctly. Its sine-Gordon identity and `epsilon=2sigma` agree with the direct computation in item 4 and Part 5's `2sigma U(w)+2sigma^{-1}U(q)`. The guide does not reproduce the `hat g=g` typo. The A2 paragraph accurately reports the current paper and flags [23] as unreviewed, but its assertion that `U'''(0)!=0` blocks Link 4 should change with item 6.

Independent checks on the guide's scope are the following:

- Velocity cancellation needs `DD^T=D^TD=I-E^2`, not merely `DD^T=D^TD` and commutation. For example `E=0`, `D=2I` has both properties listed in the guide but leaves quadratic velocity terms. The stated `D=I-E` is sufficient, so this is a missing equality in the explanation, not a counterexample to the theorem.
- Equal masses do not put a theory outside the normalized Type-I class: the computed A2 example has `M=3I` and satisfies the theorem. Thus line 981 contradicts its own preceding example.
- A heterogeneous pair does not satisfy Theorem 8.1(B), which explicitly requires the same bulk on both sides. Such a defect can satisfy Definition 3.1; this is a different assertion. Line 980 currently confuses them.
- A transparent point requires **both** `g'(0)=0` and invertible `g''(0)`. Invertibility alone does not place the critical point at the prescribed diagonal. The last sentence of line 972 should not reduce the remaining hypothesis to nondegeneracy alone.

Paste-ready corrections:

**Guide line 848, step 2:**

> The velocity-quadratic terms cancel because $D=I-E$ gives $DD^T=D^TD=I-E^2$ and $ED=DE$.

**Guide line 865:** use the revised A2 conclusions from item 6. If the new symbol calculation is not incorporated, replace the sentence beginning “The general paper's own Link 4” by:

> The paper has not yet carried out the generating-symbol and quadratic-commutation calculation for this example. Equal masses invalidate (NR2), but the nonzero cubic bulk potential does not obstruct the extended Proposition 7.5 because the defect energy has zero first variation.

**Guide line 972, final sentence:**

> Within the normalized class, and subject to the irreducibility or scalar-$G$ condition and the theorem of the still-unreviewed structural paper, the additional assumption is a transparent critical point: $g'(0)=0$ and $g''(0)$ invertible.

**Guide line 980:**

> *Heterogeneous defects need a different question.* A defect between Liouville theory and a free massless field can satisfy Definition 3.1 but is outside Theorem 8.1(B), which joins a theory to itself. Such examples show why a transparent auto-family cannot be inferred from momentum conservation for arbitrary pairs of bulks.

**Guide line 981:**

> *Outside the normalized Type-I class, no general mechanism is proved here.* Examples include Type-II defects and nonrelativistic theories without a dilation, such as Boussinesq. Equal masses alone do not place a theory outside the class: they require a direct check of quadratic commutation instead of (NR2).

Update guide lines **993 and 1003** consistently with the selected version of the revised paper's comment 4 and §10 item 3. Do not continue to list `U'''(0)!=0` as the reason the shortcut fails. Line 983 should also qualify the assertion about (C3), (C4) as depending on the general theorem of the unreviewed companion manuscript, unless that theorem receives a separate review.

## 8. Prior art and citations

**Verdict: the model-specific citations are substantially correct, but attribution of the general splitting is incomplete and the description of [10] is misleading. No novelty is explicitly claimed; nevertheless the credit should be repaired.**

**[1].** The single-field momentum conditions are at eqs. (2.15)–(2.16), and the reciprocal parameter occurs in (2.13). The exact short source quotation and normalization comparison are in item 4. Starting with its scalar momentum identity, the change `w=(phi+psi)/2`, `q=(phi-psi)/2` turns equality of pure second derivatives into `B_wq=0`; the potential constraint is bilinear. This independently identifies the splitting/rescaling content being cited. The source discusses sinh-Gordon explicitly; sine-Gordon follows by the continuation described above. [Source](https://arxiv.org/abs/hep-th/0305022).

**[2].** Section 5, eqs. (5.29)–(5.32), contains a general constant-coupling splitting, not merely a list of Toda examples. Its exact source line is:

> which is solved if Bµν = 0, with solution B = B1 (µ)+B2 (ν).

This is at local text line 1036, following eq. (5.31). Its coordinates are `mu=2w`, `nu=-2Dq`. To translate independently, define `f(w)=B1(2w)`, `g(q)=B2(-2Dq)`. Then `f'=2 B1_mu`, `g'=-2D^T B2_nu`; its bilinear equation becomes precisely (8.4). Reciprocal rescaling is immediate. The distinction in provenance is that this subsection obtains the conditions by demanding decoupled Lorentz-invariant bulk equations from a Bäcklund system. Section 4 separately establishes momentum conservation. It should not be described as a new general splitting invented in [23]. [Source](https://arxiv.org/abs/hep-th/0401020).

**[4].** Section 2 derives the normalized constant matrices and the defect-momentum gradient conditions directly from energy and momentum, eqs. (2.7)–(2.16). The text then says:

> Since u, v are Toda-like fields, solutions for the defect potential D should have the form

It next uses an exponential ansatz, and the reciprocal parameter appears explicitly in (2.41). Thus [4] supports the Toda specialization and its momentum-based derivation. Its use of the exponential ansatz should be distinguished from an ansatz-free proof for arbitrary potentials. The independent reduction of its gradient conditions to `P_w=-B_w`, `P_q=B_q` is item 1, after translating its A and B matrices to E and D. [Source](https://arxiv.org/abs/0902.1307).

**[10], decisive general prior art.** Section 2 does not assume an affine Toda bulk potential. It treats general vector-field potentials; the Toda specialization begins in §4. Around eqs. (2.46)–(2.47), local text line 729, it says:

> The first four of these equations are satisfied if we require the dependencies of D and D̄ to be

Its Type-I specialization has only the `(1)` fields. Write their endpoint average as p and difference as q. Independently translating its equations gives `D=f(p+Aq)` and `Dbar=g(q)`. With `A=E`, the first argument is exactly

\[
 p+Eq=\tfrac12[(I+E)\phi+(I-E)\psi]=w.
\]

Its momentum condition (2.48) consequently becomes `2(U-V)=f_w^T g_q`, precisely (8.4). Rescaling the two functions reciprocally preserves this equation, with no Toda assumption. The paper also explicitly uses reciprocal sigma factors in its Toda ansatz, eqs. (4.2)–(4.3). Therefore the **general constant-coupling momentum-conservation splitting and its elementary rescaling consequence** are already contained in [10]. The scalar-Hessian normalization and the formal branch are separate steps; I do not attribute them to [10]. [Source](https://arxiv.org/abs/1612.03002).

This also corrects the framing at paper §1.4 and guide Part 17: [10] studies momentum conservation and Bäcklund relations in its general section. It does not establish general Liouville integrability by a Lax/r-matrix argument. The all-purpose statement that all these works start from an integrable bulk is inaccurate for that section of [10].

Replace the final two sentences of **paper line 472** by:

> Propositions 8.2 and 8.3 restate Propositions 3.1 and 3.2 of [23] in the present notation. The single-field and affine Toda splittings and reciprocal defect parameters occur in [1,2,4]. A general constant-coupling splitting is also given in [2, §5], and the Type-I specialization of the momentum-conservation conditions in [10, §2, eqs. (2.46)–(2.48)] gives (8.4) without an affine Toda assumption. Reciprocal rescaling follows from that bilinear condition. We include the derivation to fix the conventions and to connect it to the scalar-Hessian normalization and formal-branch criterion.

At **guide line 1084**, replace the claim assigning the general derivation only to [23] by:

> The general constant-coupling splitting is present in [2, §5] and follows directly from the Type-I specialization of Bristow–Bowcock's general momentum-conservation conditions [10, §2]. Reciprocal rescaling preserves their bilinear constraint. Section 8.2 restates the derivation through [23] and adds the normalization and transparent-branch argument used here.

At **paper line 54**, replace its last two sentences by:

> The inverse-scattering and Liouville-integrability constructions cited above use integrable bulk structures. Bristow and Bowcock [10, §2] also derive general momentum-conservation conditions and a Bäcklund construction before specializing to affine Toda potentials. The present paper asks how far momentum conservation yields a local commuting hierarchy under explicit additional hypotheses.

At **guide lines 1092–1093**, replace the blanket attribution by:

> Avan–Doikou [15] study Liouville integrability using integrable bulk structures. Bristow–Bowcock [10] derive general momentum-conservation and Bäcklund conditions, then specialize to affine Toda; this is also prior art for the splitting in Link 3. The general local commuting-hierarchy conclusion requires additional arguments.

There is no explicit novelty claim in §8.2; the Status disclaimer is clear. The problem is incomplete attribution and an inaccurate contrast with [10], not an explicit assertion of priority. References [1], [2], [4] support the models and rescaling statements after the translations above. Reference [23] is accurately identified as an unreviewed companion manuscript.

## Claims not independently checked

- The complete proof of [23, Theorem 2.1] for arbitrary analytic potentials, including its general canonical-generator and formal-map-commutation arguments. Its hypotheses for A2 and its imported Propositions 3.1–3.2 were checked here. A2 charge involution and independence were also proved independently above.
- An all-orders Tzitzéica generating symbol and a complete renewed proof of its Type-II branch. The check here establishes that its energy has zero first variation, including the auxiliary direction. A2 was the full nonlinear cubic test requested as the alternative in item 6.
- Exhaustive priority beyond the cited papers. The explicit general precedent in [10] already settles the attribution issue raised by this brief; no claim of exhaustive literature coverage is made.
- Other models' pre-existing table entries and the Lean project. Only the requested new check script was run for comparison; the independent script and written derivations supply this report's evidence.

## Other observations (unverified)

No additional unverified mathematical findings are proposed. The all-r quadratic-symbol calculation is a natural next check, since the cyclic construction simultaneously diagonalizes the bulk Hessian and E, but this report's explicit all-orders involution/independence proof is restricted to A2. No claim about convergence of the epsilon series or global defect dynamics is made.
