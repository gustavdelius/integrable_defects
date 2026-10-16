**Referee report on Momentum Conserving Defects and the Corrigan–Zambon Conjecture**

Manuscript: [paper_theorem_D.md](/home/gustav/.gemini/antigravity-cli/brain/937c3881-3bf7-46d6-afea-a55c316db1ff/paper_theorem_D.md), version reviewed 16 October 2026. Equation and line references below refer to this version.

**Recommendation: reject in its present form.** The manuscript does not prove the advertised model-independent integrability theorem. Lemma 3.1 is a correct geometric observation, and a suitably restricted, consistently signed version of the spatial Hamilton–Jacobi argument could be useful. However, the passage from that observation to an infinite hierarchy of independent commuting local charges contains several independent gaps. Some displayed identities are demonstrably false even for a standard free massive-scalar defect. Moreover, the permitted class of constrained defects includes symmetry identifications that preserve energy and momentum for nonintegrable bulk theories.

The distinction matters: errors of convention can be repaired without changing the geometric idea, whereas the missing arguments for locality, independence, and involution require substantial new mathematics. The additional hypotheses of Theorem 2 are also not consequences of the hypotheses used to advertise the result.

| Claim | Assessment |
| --- | --- |
| Lemma 2.1 | The momentum-flux identity has the wrong sign under the manuscript's definitions. |
| Lemma 3.1 | Correct with consistent Hamiltonian conventions and a genuinely Lagrangian tangent space. |
| Theorem 1 | A conditional formal result is plausible; the stated equivalences require additional hypotheses and normalization. |
| Proposition 4.1 | Incorrect signs and an unjustified elimination of functions of integration; an allowed auxiliary oscillator gives a counterexample even after sign repair. |
| Theorem 2 | The supplied proof establishes neither the claimed hierarchy nor its independence or involution. |
| Universal integrability conclusion | Unsupported; the allowed constrained-defect class has explicit counterexamples to this breadth of conclusion. |

**1. The unrestricted claim admits symmetry defects for arbitrary interactions**

The abstract, Introduction, and Conclusion claim integrability for arbitrary translation-invariant local bulk theories. Yet §3.1 explicitly permits holonomic sewing constraints implemented with the auxiliary variables, and only assumes that the resulting correspondence is smooth and Lagrangian (lines 120–127).

Consider identical scalar theories

$$
\mathcal L(u)=\tfrac12u_t^2-\tfrac12u_x^2-U(u),\qquad U(-u)=U(u),
$$

with the local defect action

$$
S_d=\int dt\,\lambda(t)(\psi+\phi).
$$

The manuscript's own boundary variation (3.4) gives

$$
\psi=-\phi,\qquad \pi_-=-\lambda,\qquad \pi_+=\lambda.
$$

Since $\pi_-=-\phi_x$ and $\pi_+=-\psi_x$, the sewing is

$$
\psi=-\phi,\qquad \psi_x=-\phi_x.
$$

This is the graph of the symplectic map $(\phi,\pi)\mapsto(-\phi,-\pi)$. Both energy and momentum flux match, and $E_d=P_d=0$ on the constraint. There is a field discontinuity whenever $\phi(0,t)\ne0$. The construction works for **every even potential**. The identity defect follows by replacing $\psi+\phi$ with $\psi-\phi$ and works for every potential, without even the parity restriction.

In particular, take the massive quartic theory

$$
U(u)=\tfrac12m^2u^2+\frac{g}{4!}u^4,\qquad m>0,\quad g>0.
$$

Its failure of the usual massive, local-charge integrability criterion can be seen in tree-level particle production. At the threshold configuration with incoming momenta $(2m,\pm\sqrt3m)$ and four outgoing momenta $(m,0)$, the ten quartic exchange diagrams have propagator denominators $8m^2$ four times and $-4m^2$ six times. Their sum is

$$
\frac4{8m^2}+\frac6{-4m^2}=-\frac1{m^2}\ne0.
$$

Thus the production amplitude is nonzero, proportional to $g^2/m^2$; continuity gives nonzero production near threshold as well. This is consistent with the established no-production recursion, which requires a nonzero sixth-order interaction when the quartic interaction is nonzero. See Gabai et al., [No Particle Production in Two Dimensions](https://arxiv.org/html/1803.03578), §1.2, equations (8)–(11).

This example does **not** refute Lemma 3.1: a symmetry is indeed a canonical correspondence intertwining the equations. It refutes the inference from the existence of such a correspondence to bulk integrability, in the broad defect class admitted here. It is also not a counterexample to Theorem 2 with all its extra regularity assumptions; those assumptions are precisely additional restrictions absent from the universal claim.

If the intended conjecture excludes constrained identifications, symmetry defects, and transparent spectator sectors, those exclusions must be explicit. The parenthetical permission in line 120 currently goes in the opposite direction. Excluding only the identity defect would not suffice.

**2. The basic signs are mutually inconsistent**

There are several separate issues in §§2–4; they cannot all be repaired by one reinterpretation of notation.

For the scalar Lagrangian above, the definitions (2.5) and (2.8) give

$$
\pi^{(x)}=-\phi_x,\qquad
\mathcal H^{(x)}=\pi^{(x)}\phi_x-\mathcal L
=-\tfrac12\phi_x^2-\tfrac12\phi_t^2+U(\phi).
$$

The canonical tensor compatible with (2.10) is

$$
\mathcal T^\mu{}_{\nu}
=\frac{\partial\mathcal L}{\partial\phi_\mu}\phi_\nu
-\delta^\mu{}_{\nu}\mathcal L.
$$

Consequently

$$
\mathcal T^1{}_1=\mathcal H^{(x)},\qquad
T^{11}=-\mathcal H^{(x)}
=\tfrac12\phi_x^2+\tfrac12\phi_t^2-U(\phi).
$$

Lemma 2.1 and its proof, especially line 104, assert the opposite sign. Equation (5.1) additionally has the wrong sign for the spatial-momentum square: its Legendre transform should contain $-\tfrac12|\pi^{(x)}|^2$, not $+\tfrac12|\pi^{(x)}|^2$. This is an immediate countercheck using the paper's simplest example, without higher-derivative improvements.

The symplectic convention also conflicts with Hamilton's equations. With $\Omega=\delta\pi\wedge\delta\Phi$, equations (2.9) imply

$$
\iota_{X_H}\Omega=-\delta H,
$$

whereas line 81 states $+\delta H$. One can change either the sign of $\Omega$ or the definition of $X_H$. Lemma 3.1 survives a consistent choice.

The flux balances have a further error. Equation (2.12) and conservation of the totals require

$$
\dot E_d=\mathcal T_-^1{}_0-\mathcal T_+^1{}_0,
\qquad
\dot P_d=T_-^{11}-T_+^{11}.
$$

Equations (3.7) and (4.1) assign minus signs to these expressions. For an autonomous first-order defect action, the identity

$$
\frac{dE_d}{dt}
=-\sum_a\frac{\delta S_d}{\delta q^a}\dot q^a
$$

also shows directly that the last equality in (3.7) has the wrong sign. The two expressions for the momentum balance in (3.10) are not algebraically equal under the definitions then in force.

Finally, for $\mathcal L_d=A_a(q)\dot q^a-B(q)$, write $F_{ab}=\partial_aA_b-\partial_bA_a$. Equation (3.4) requires

$$
\pi_-=-F_{\phi b}\dot q^b+B_\phi,
\qquad
\pi_+=F_{\psi b}\dot q^b-B_\psi.
$$

The potential terms in (4.7) have the opposite signs. Changing the definition of the gyroscopic matrices cannot fix the potential signs.

These mistakes do not by themselves destroy the integrated tangency argument: a common sign change in the Hamiltonians leaves the equality of the two Hamiltonians unchanged. They do invalidate the displayed derivations and require a complete convention audit before the stronger results can be assessed.

**3. Theorem 1 needs stronger hypotheses than its proof supplies**

The geometric lemma says

$$
(X_{H_-},X_{H_+})\in T\Gamma
\quad\Longleftrightarrow\quad
d(H_--H_+)|_{T\Gamma}=0.
$$

It gives local constancy, not zero. The use of the lemma in line 162 silently strengthens its conclusion to vanishing. A reference point with equal Hamiltonians, in every component under consideration, is needed to obtain zero. Hamiltonians shifted by different constants illustrate why tangency alone cannot fix this normalization.

More seriously, the proof of $(1)\Rightarrow(2)$ moves from a balance law on actual bulk-plus-defect solutions to a functional identity on the whole correspondence of boundary histories. These are different domains. One must prove that the relevant boundary data and variations are realized by local bulk solutions, or assume a formal jet identity after eliminating the spatial derivatives. No such realization or formal completeness argument is given. Without it, conservation on a restricted set of solutions can impose fewer conditions than constancy on all of $\Gamma_d$.

The converse local-divergence argument in line 161 also needs qualification. The standard one-dimensional null-Lagrangian argument applies locally to unconstrained jet variables. Here variations may be constrained by $\delta S_d/\delta\lambda=0$, and eliminating a dynamical auxiliary field can be nonlocal. Vanishing of an integrated functional on that constrained space does not, without further work, produce a local primitive $P_d$ of the specified kind. The appropriate statement needs a local parametrization or a proof in the constrained variational complex, with boundary and cohomological assumptions specified.

The last part of line 162 introduces invertibility of the mixed Hessian to remove vertical tangent vectors. The preceding standing assumption was only that $\Gamma_d$ is smooth and Lagrangian; line 127 describes nondegeneracy as a sufficient condition for that property, not an assumption on every allowed correspondence. A Lagrangian relation need not be the graph of a local symplectomorphism. For the particular solution-mapping conclusion proved there, the required transversality or an alternative argument using the full sewing system must be stated and established.

Thus the valid geometric lemma should be retained, but the claimed three-way equivalence should be rewritten with explicit hypotheses. Equation (3.6) alone proves isotropy; maximality is a separate assumption already acknowledged in line 127.

**4. Arbitrary mixed jets do not automatically give the claimed local spatial Hamiltonian**

Section 2 allows arbitrary $t$-derivatives of the highest $x$-derivative. Then the spatial Legendre map is generally a differential operator in $t$, rather than an algebraic map. For example,

$$
\mathcal L=\tfrac12\phi_x^2+\tfrac12\phi_{xt}^2
\quad\Longrightarrow\quad
\pi^{(x)}=(1-D_t^2)\phi_x.
$$

The ordinary Hessian with respect to $\phi_x$ is nonzero, but solving for $\phi_x$ uses $(1-D_t^2)^{-1}$, which is nonlocal on periodic or decaying histories. If the parenthetical assumption in line 77 is intended to require a local inverse of the functional Legendre map, this example is excluded and the result no longer covers arbitrary finite-order Lagrangians. If only ordinary regularity is intended, the claimed construction is insufficient.

There is also no general smooth spatial flow on the stated space of smooth histories. Even free Schrödinger evolution, treated as an initial-value problem in $x$, has temporal Fourier modes growing as $\exp(c\sqrt{|\omega|}\,x)$ for one frequency sign. Smooth initial histories alone need not admit such an evolution. A formal jet theorem can avoid an analytic flow claim, but the paper must choose between a formal statement and an analytic theorem with appropriate function spaces and existence assumptions.

**5. Proposition 4.1 discards functions of integration without justification**

Even accepting the displayed signs temporarily, the differentiation in lines 198–200 proves only

$$
D_t(D_xE_d-\Delta\mathcal T^0{}_0)=0,
\qquad
D_t(D_xP_d-\Delta T^{01})=0.
$$

The resulting quantities are functions of $x$, depending on the particular solution. They are not automatically universal numerical constants. Evaluating on the vacuum fixes them on the vacuum solution; it does not fix them on every other solution.

A common vacuum limit as $t\to\pm\infty$, with all relevant jets and normalizations controlled at each $x$, could remove these functions on that restricted class. The alternative of periodic $t$-histories in line 56 does not do so. Another possible repair is a local differential argument showing that the relevant $D_t$-invariants are constants on the full equation manifold. Neither repair appears in the proof.

With the corrected physical balance signs, the corresponding proposed spatial identities would be $D_xE_d=-\Delta\mathcal T^0{}_0$ and $D_xP_d=-\Delta T^{01}$, subject to exactly the same issue. The continuity equation (4.2) can hold in particular models, but it has not been established by the universal argument supplied here.

There is an explicit counterexample to the full proposition within the permitted auxiliary-field class. Add an independent oscillator to a momentum-conserving defect with a zero-field vacuum:

$$
\mathcal L_d=\mathcal L_d^{\rm base}
+\tfrac12\lambda_t^2-\tfrac12\omega^2\lambda^2.
$$

The added oscillator preserves energy conservation, changes no bulk sewing equation or momentum balance, and leaves the projected bulk Lagrangian correspondence unchanged. After promotion to all $x$, take $\phi=\psi=0$ and

$$
\lambda(x,t)=a(x)\cos(\omega t).
$$

Every defect Euler–Lagrange equation holds at every $x$. These histories are periodic in $t$, as expressly allowed; $a(x)$ can be smooth with compact support. But the additional defect energy is

$$
E_{\rm osc}(x)=\tfrac12\omega^2a(x)^2,
\qquad D_xE_{\rm osc}=\omega^2a(x)a'(x),
$$

while the bulk energy-density difference is identically zero. No vacuum normalization removes this state-dependent function of $x$. Thus the asserted spatial energy identity is false for the allowed class, independently of the sign errors. This example does not by itself disprove (4.2), because the added oscillator energy is time independent; it specifically disproves the four-identity proposition used in the argument.

**6. The parameter family and its regularity are additional assumptions**

Translation invariance does not imply a boost or scaling symmetry. Even when such a symmetry exists, its orbit need not supply an essential Bäcklund parameter, a transparent limit, or the asymptotic form (4.3). The paper does not derive Definition 4.1 from energy and momentum conservation. Bianchi permutability is another independent assumption, stated only in part 3 of Theorem 2. The abstract and Conclusion must not present these additional inputs as consequences of the original premises.

There are concrete problems in §4.1. A nonzero Lorentz boost sends $x=0$ to a moving worldline. A Galilean boost does the same. A constant spacetime translation cannot turn a sloping worldline back into $x=0$. One may instead boost already-unfrozen sewing equations and then investigate a new stationary defect action, but that is a different construction and requires proof. It does not follow from invariance of the original stationary boundary problem.

The asserted multiplicative scaling for the Boussinesq model in §5.3 also fails for its fixed coefficients: its linearized equation contains both $\phi_{xx}$ and $\phi_{xxxx}$. Under $(t,x,\phi)\mapsto(\sigma^zt,\sigma x,\sigma^\Delta\phi)$, matching the time derivative to these terms requires both $2z=2$ and $2z=4$. Parameter changes, background shifts, or a different equation could alter this conclusion, but those would have to be specified.

Fusion in Remark 4.1 does not repair these omissions. For a general relation $\Gamma$, $\Gamma^{-1}\circ\Gamma$ need not be the diagonal. Even for invertible local branches, fusion alone establishes neither locality after elimination nor the asymptotic form and nondegeneracy of Definition 4.1.

**7. The recursion solves only part of the asserted problem**

After correcting the signs in (4.7), invertibility of the leading Hessian can indeed support a triangular formal recursion from one set of sewing equations. This is a potentially useful observation. However, lines 243–248 use only the first equation of (4.7). They do not verify the second equation or prove that its residual vanishes for every solution of the left bulk equation. Such compatibility might be derivable from an appropriately strengthened Hamilton–Jacobi identity, but it must be proved rather than assumed.

There is a further issue for different bulk theories. If $\psi=\phi+O(\epsilon)$ solves the right bulk equation for every left solution, the leading term must already satisfy the right equation. This is a substantial compatibility condition on $\mathcal L_-$ and $\mathcal L_+$, absent from Definition 4.1. A rigorously constructed auto-correspondence could address this, subject to the fusion objections above.

The asserted derivative bound is also false at the advertised level of generality. The restriction $K=1$ does not imply $\pi^{(x)}=-\phi_x$, as line 234 assumes; that identity selects a particular kinetic term. For $K>1$, replacing $-\phi_x$ by the Ostrogradsky momentum does not preserve the claim that $\Psi_1$ depends only on first-order jets. The paper's own Boussinesq example has $\pi_0^{(x)}=-\phi_{xxx}-\phi_x-U'(\phi_x)$. Moreover, the components of $\vec\Psi=(\psi,\psi_x,\ldots)$ must satisfy their holonomic relations. Treating their coefficient recursions as independent algebraic substitutions does not verify those relations.

**8. Equation (4.12) omits terms that are necessary even for the first conserved charge**

For the defect Lagrangian (4.3), the first-order gyroscopic terms cancel in the defect energy, giving

$$
E_d=\epsilon^{-1}B_-+B_0+\epsilon B_1+\epsilon^2B_2+\cdots.
$$

After substituting $\psi=\phi+\epsilon\Psi_1+\cdots$, the coefficient of $\epsilon$ is generally

$$
Q_1=\tfrac12\Psi_1^T H\Psi_1
+(\partial_\psi B_0)_{\rm diag}\cdot\Psi_1
+B_1(\phi,\phi).
$$

There can also be a nonzero coefficient $Q_0=B_0(\phi,\phi)$. Equation (4.12) omits all these lower-potential contributions and incorrectly attributes the remainder solely to cubic and higher terms from $B_-$. An $O(\epsilon^0)$ remainder before substitution is not negligible at subsequent positive orders.

A direct test uses two free massive scalars and

$$
\mathcal L_d=\tfrac12(\phi\psi_t-\psi\phi_t)-B,
\qquad
B=\frac{(\phi-\psi)^2}{2\epsilon}
+\frac{\epsilon m^2}{8}(\phi+\psi)^2.
$$

This is a reparametrization of the standard massive free-field defect in Bowcock, Corrigan and Zambon, [Affine Toda field theories with defects](https://arxiv.org/html/hep-th/0401020), §2. Here $H=D=1$, $B_0=0$, and the diagonal self-couplings vanish. Thus the example has the advertised asymptotic regularity.

Using consistent physical signs, its sewing equations and defect momentum are

$$
\phi_x=\psi_t-B_\phi,\qquad
\psi_x=\phi_t+B_\psi,
\qquad
P_d=\frac{(\phi-\psi)^2}{2\epsilon}
-\frac{\epsilon m^2}{8}(\phi+\psi)^2.
$$

Direct substitution verifies the energy and momentum balances and the exact current identity

$$
D_tB+D_xP_d=0.
$$

The leading sewing coefficient is $\Psi_1=\phi_x-\phi_t$. Therefore the actual energy coefficient is

$$
Q_1=\tfrac12(\phi_x-\phi_t)^2+\tfrac12m^2\phi^2.
$$

Its integral is the bulk energy plus the canonical momentum. The expression retained by (4.12) would instead yield

$$
\widehat Q_1=\int dx\,\tfrac12(\phi_x-\phi_t)^2,
\qquad
\frac{d\widehat Q_1}{dt}=-m^2\int dx\,\phi\phi_t,
$$

which is nonzero for generic decaying Cauchy data. For example, choosing $\phi_t=\phi\ne0$ initially makes it strictly negative. The opposite chirality resulting from the manuscript's erroneous sewing signs has the same missing mass term and the same problem.

This is a concrete failure of the claimed coefficient formula and its asserted conservation, after granting the intended sign repairs. The example itself is integrable and its correctly expanded current is conserved; it pinpoints a false step in the proof, rather than denying the existence of the known free-field hierarchy.

**9. The proof of nontriviality and independence uses an invalid quotient and an unproved nondegeneracy assertion**

The charges are integrals over $x$ at fixed $t$. Consequently a density can be changed by $D_xF$ without changing its charge under the stated spatial boundary conditions. It cannot generally be changed by $D_tG$:

$$
\int dx\,D_tG=D_t\int dx\,G
$$

need not vanish. Equation (4.13), which identifies densities modulo $D_t(\cdots)+D_x(\cdots)$, uses the equivalence appropriate to a spacetime integral, not the equivalence needed for the equal-time charges. A trivial conserved current has the improvement form $(D_xF,-D_tF)$, with any on-shell trivial terms accounted for separately. The proposed integration by parts in $t$ does not establish equivalence of the charges.

The alternative instruction to eliminate $\phi_{tt}$ using the equation of motion is not a universal repair. The allowed equations can have arbitrary temporal order or constraints; even in the Klein–Gordon case, the reduction must be carried out in the correct spatial conservation-law class.

Independently, the matrix $K_m$ in (4.13) is never computed. Its nondegeneracy is asserted from invertibility of $H$ and $D$, which is not a valid matrix inference. To test the algebra actually used there, take constant matrices and put $v=\Psi_1$, $A=-H^{-1}D$. The retained quadratic contribution at order $\epsilon^3$ is

$$
v^THA^2v_{tt}+\tfrac12v_t^TA^THAv_t.
$$

Even allowing the paper's integration by parts in $t$, its resulting quadratic matrix is

$$
K=A^THA-HA^2-(A^T)^2H.
$$

Choose

$$
H=I_2,\qquad
D=I_2+\frac1{\sqrt3}
\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$

Then $\det H=1$ and $\det D=4/3$, but $K=0$. This is an algebraic counterexample to the inference from the two invertibility conditions; it is not offered as a construction of a full momentum-conserving defect satisfying every other hypothesis. If momentum conservation imposes additional matrix restrictions that prevent this cancellation, the proof must derive and use them.

Nor does a nonzero expression in unrestricted jets automatically represent a nontrivial conservation law on the bulk equation manifold. The densities must first be reduced to independent Cauchy data, with spatial divergences and terms vanishing on solutions removed. Only then can leading variational derivatives support an independence argument. None of these reductions or the required nonzero symbols has been established.

**10. Step 3 does not prove equal-time involution**

Line 264 begins by assuming the main missing bridge: that the Bäcklund maps are generated by the particular charge series extracted from the defect energy. No previous calculation establishes

$$
\delta_\epsilon F=\{F,Q(\epsilon)\}_{\text{equal time}}.
$$

There are two separate issues. First, the canonical relation constructed in §3 belongs to the spatial phase space of time histories, with symplectic form integrated over $t$. The conclusion concerns the equal-time phase space, with symplectic form integrated over $x$. Canonicity for the former is not canonicity for the latter. A temporal variational or covariant symplectic argument is needed, including the appropriate reduction for theories such as NLS and potential KdV.

Second, even if the maps were canonical on the correct phase space, their formal logarithms or parameter-variation generators need not equal $\sum_n\epsilon^nQ_n$ constructed from $E_d$ or $N_d$. A generating functional for a canonical relation, its parameter derivative, and the Hamiltonian whose flow produces a map are different objects. The required identification, sometimes expressed through a spectrality relation, is not supplied.

Bianchi permutability would imply commutativity of suitable infinitesimal generators once these constructions were justified. It does not identify arbitrary conserved quantities as those generators. In addition, the claim that a constant Poisson bracket vanishes because both charges vanish at the vacuum is insufficient by itself: $q$ and $p$ both vanish at the origin, while $\{q,p\}=1$. Vanishing of the relevant Hamiltonian vector fields at the vacuum, or another normalization argument, would suffice.

The paper must prove temporal canonicity and identify the generators before the Jacobi-identity argument can be used. Assuming Bianchi permutability alone does not fill either gap.

**11. The examples do not verify the hypotheses used in Theorem 2**

Section 5 repeatedly states that the Hamilton–Jacobi equation forces familiar integrable potentials, but supplies neither the required defect ansatz nor the intervening restrictions and solution of the functional equations. The geometric reformulation alone cannot replace those steps. The constrained symmetry defects in comment 1 show why such restrictions matter.

There are also mismatches with Definition 4.1. In §5.1, set $M=0$ and use $D=I-E$, $E^T=-E$. The displayed kinetic term $2q\cdot w_t$, modulo a total derivative, is

$$
\tfrac12\phi^TE\phi_t+\phi^TD\psi_t
+\tfrac12\psi^TE\psi_t.
$$

Its two diagonal gyroscopic blocks have the same sign, so their sum is $2E$, not zero when $E\ne0$. Thus checking positivity of the potential Hessian does not verify the additional diagonal condition in Definition 4.1 for this displayed multicomponent action. This kinetic structure also agrees with the original Toda construction, where $E=F=I-D$; see [Bowcock, Corrigan and Zambon, equation (3.11)](https://arxiv.org/html/hep-th/0401020).

For Type-II defects, eliminating an auxiliary variable need not produce the first-order gyroscopic form (4.3). The cited original paper gives an explicit free-field example with a $q_t^2$ term after elimination, [A new class of integrable defects, equation (3.9)](https://arxiv.org/html/0908.3126). The manuscript provides no argument reducing such examples to its assumed form.

In the NLS application the expanded conserved density is $N_d$, whereas Step 2 analyzes the Hessian of the energy potential $B_-$. A proof that controls the leading terms of $E_d$ does not automatically control $N_d$. Neither this missing analysis nor the higher-spatial-order compatibility discussed in comment 7 is carried out.

**12. References and the required replacement claim**

Two bibliography entries demonstrably pair the wrong titles with their arXiv identifiers. Reference [6], arXiv:1807.05747, is [Type II defects revisited](https://arxiv.org/abs/1807.05747), with DOI corresponding to JHEP 09 (2018) 019. Reference [7], arXiv:2006.14447, is [Integrable Defects at Junctions within a Network](https://arxiv.org/abs/2006.14447). These should be corrected, and the claimed locations and scope of the original conjecture rechecked.

A defensible replacement result would first assume a well-defined spatial Hamiltonian formulation, a smooth Lagrangian correspondence, and a local momentum-balance identity valid on the relevant boundary jet space. Under appropriate temporal boundary conditions, that identity implies constancy of the Hamiltonian difference; Lemma 3.1 then gives tangency. A solution-mapping assertion additionally needs the relevant regularity and existence or formal compatibility conditions. This is a geometric interpretation of momentum conservation, not yet a proof of bulk integrability.

For an integrability theorem, the authors must separately establish an essential parameter family, a compatible local formal solution of the complete sewing system, a correctly expanded conserved current, infinitely many nontrivial independent conservation-law classes, and the equal-time Hamiltonian identification needed for involution. The current manuscript assumes or asserts the decisive parts of this chain. Correcting the signs alone would not change the recommendation.
