import GeneralFramework.Basic

/-
  Algebraic cores of the general lemmas of `general_framework/paper.md`.

  Scope.  Each theorem below checks the algebra of one step of a written proof,
  over an arbitrary commutative ring with commuting derivations.  The analytic
  and variational inputs of those proofs (the chain rule for Euler operators,
  Helmholtz self-adjointness, Fourier analysis of local functionals) enter as
  explicitly named hypotheses, stated in the docstrings.  Nothing here is a
  formalisation of the infinite-dimensional theorems themselves.
-/
open Lean.Grind

namespace GeneralFramework

variable {R : Type} [CommRing R]

/-! ## Section 2: spatial Legendre transform and Noether currents -/

/-- **Lemma 2.1, first order.**  For L(u, u_t, u_x) with partial derivatives
Lu, Lt, Lx (chain rules as hypotheses), the canonical currents satisfy the
energy and momentum Noether identities, and the spatial component of the
momentum current is the spatial Hamiltonian density Lx*u_x - L. -/
theorem noether_first_order (S : SpaceTime R) (u L Lu Lt Lx : R)
    (chain_t : S.Dt L = Lu * S.Dt u + Lt * S.Dt (S.Dt u) + Lx * S.Dt (S.Dx u))
    (chain_x : S.Dx L = Lu * S.Dx u + Lt * S.Dx (S.Dt u) + Lx * S.Dx (S.Dx u)) :
    let E := Lu - S.Dt Lt - S.Dx Lx
    let H := Lx * S.Dx u - L
    S.Dt (Lt * S.Dt u - L) + S.Dx (Lx * S.Dt u) = -E * S.Dt u ∧
    S.Dt (Lt * S.Dx u) + S.Dx H = -E * S.Dx u := by
  intro E H
  constructor
  · rw [S.Dt.map_sub, S.Dt.map_mul, S.Dx.map_mul, chain_t, S.comm u]
    grind
  · rw [S.Dt.map_mul, S.Dx.map_sub, S.Dx.map_mul, chain_x, S.comm u]
    grind

/-- Spatial integration by parts for spatial order two (identity (2.6) with K = 2). -/
theorem ostrogradsky_K2 (S : SpaceTime R) (F0 F1 F2 eta : R) :
    F0 * eta + F1 * S.Dx eta + F2 * S.Dx (S.Dx eta) =
      (F0 - S.Dx F1 + S.Dx (S.Dx F2)) * eta +
      S.Dx ((F1 - S.Dx F2) * eta + F2 * S.Dx eta) := by
  rw [S.Dx.map_add, S.Dx.map_mul, S.Dx.map_mul, S.Dx.map_sub]
  grind

/-- **Lemma 2.1, spatial order two (derived, not assumed).**  If the spatial
variation of L along the translation `eta = D_x u` has been integrated by parts
in t, leaving the explicit boundary term `Xi` (hypothesis `chain_x`), then
`(T^0_1, T^1_1) := (Xi, H)` is a momentum Noether current with
`H = pi0 u_x + pi1 u_xx - L` the Ostrogradsky spatial Hamiltonian density. -/
theorem legendre_noether_K2 (S : SpaceTime R) (u L F0 F1 F2 Xi : R)
    (chain_x : S.Dx L = F0 * S.Dx u + F1 * S.Dx (S.Dx u) + F2 * S.Dx (S.Dx (S.Dx u)) + S.Dt Xi) :
    let E := F0 - S.Dx F1 + S.Dx (S.Dx F2)
    let pi0 := F1 - S.Dx F2
    let pi1 := F2
    let H := pi0 * S.Dx u + pi1 * S.Dx (S.Dx u) - L
    S.Dt Xi + S.Dx H = -E * S.Dx u := by
  intro E pi0 pi1 H
  have h := ostrogradsky_K2 S F0 F1 F2 (S.Dx u)
  simp only [H, pi0, pi1, E]
  rw [S.Dx.map_sub, chain_x]
  grind

/-- **Lemma 2.2, spatial order two.**  With b0 = -F0 and b1 = pi0 - F1 the
t-Euler derivatives of the spatial Hamiltonian, the Ostrogradsky momenta of any
field (on or off shell) satisfy D_x pi1 + b1 = 0 and D_x pi0 + b0 = -E. -/
theorem hamilton_slots_K2 (S : SpaceTime R) (F0 F1 F2 : R) :
    let E := F0 - S.Dx F1 + S.Dx (S.Dx F2)
    let pi0 := F1 - S.Dx F2
    let pi1 := F2
    S.Dx pi1 + (pi0 - F1) = 0 ∧ S.Dx pi0 + (-F0) = -E := by
  intro E pi0 pi1
  constructor
  · simp only [pi0, pi1]; grind
  · simp only [pi0, E]; rw [S.Dx.map_sub]; grind

/-! ## Section 3: the Bäcklund theorem -/

/-- **Theorem 3.3(a), algebraic core.**  Write S_AB for the blocks of the
Fréchet derivative of the defect Euler–Lagrange expression (self-adjoint by
Helmholtz, which is used in deriving the hypotheses).  Applying the t-Euler
operator to the momentum balance gives, by the chain rule for Euler operators,
the three identities `hPhi`, `hPsi`, `hLam`, where a, b are the configuration
and momentum components of the spatial Hamiltonian vector fields and rho is the
multiplier of the constraint ideal.  Then the variation (a_-, a_+, rho) of the
defect data satisfies the linearised constraint and is mapped by the
linearised sewing maps onto the momentum components (-b_-, -b_+): the pair of
Hamiltonian vector fields is tangent to the sewing correspondence. -/
theorem tangency_from_euler
    (Sff Sfp Sfl Spf Spp Spl Slf Slp Sll : R → R) (am ap bm bp rho : R)
    (hPhi : bm - Sff am - Sfp ap = Sfl rho)
    (hPsi : -Spf am - bp - Spp ap = Spl rho)
    (hLam : -Slf am - Slp ap = Sll rho) :
    Slf am + Slp ap + Sll rho = 0 ∧
    -(Sff am + Sfp ap + Sfl rho) = -bm ∧
    Spf am + Spp ap + Spl rho = -bp := by
  refine ⟨?_, ?_, ?_⟩ <;> grind

/-- **Theorem 3.3(b), algebraic core (two Ostrogradsky slots, auxiliary field).**
For a solution of the sewing system imposed at every x, the x-derivative of the
defect data and the tangent vector of Theorem 3.3(a) agree in their Phi and Psi
components (configuration Hamilton equations hold for actual fields), so the
linearised sewing relations of the two vectors differ only through
kappa = lambda_x - rho.  The Ostrogradsky identities for actual momenta
(`hO*`, Lemma 2.2) then give E_- and E_+ in terms of kappa; under the
injectivity hypothesis (I) both bulk equations hold. -/
theorem promoted_implies_bulk
    (Sf0l Sf1l Sp0l Sp1l Sll : R → R)
    (sub_f1 : ∀ a b, Sf1l (a - b) = Sf1l a - Sf1l b)
    (sub_p1 : ∀ a b, Sp1l (a - b) = Sp1l a - Sp1l b)
    (sub_ll : ∀ a b, Sll (a - b) = Sll a - Sll b)
    (Mm0 Mm1 Mp0 Mp1 MC lamx rho : R)
    (dpm0 dpm1 dpp0 dpp1 bm0 bm1 bp0 bp1 Em Ep : R)
    -- linearised sewing along the x-derivative of the solution:
    (hx_m0 : dpm0 = -(Mm0 + Sf0l lamx)) (hx_m1 : dpm1 = -(Mm1 + Sf1l lamx))
    (hx_p0 : dpp0 = Mp0 + Sp0l lamx) (hx_p1 : dpp1 = Mp1 + Sp1l lamx)
    (hx_C : MC + Sll lamx = 0)
    -- the same relations for the Hamiltonian vector fields (Theorem 3.3(a)):
    (hX_m0 : -bm0 = -(Mm0 + Sf0l rho)) (hX_m1 : -bm1 = -(Mm1 + Sf1l rho))
    (hX_p0 : -bp0 = Mp0 + Sp0l rho) (hX_p1 : -bp1 = Mp1 + Sp1l rho)
    (hX_C : MC + Sll rho = 0)
    -- Ostrogradsky identities for actual momenta (Lemma 2.2):
    (hO_m1 : dpm1 + bm1 = 0) (hO_m0 : dpm0 + bm0 = -Em)
    (hO_p1 : dpp1 + bp1 = 0) (hO_p0 : dpp0 + bp0 = -Ep)
    -- injectivity hypothesis (I):
    (hI : ∀ k, Sf1l k = 0 → Sp1l k = 0 → Sll k = 0 → k = 0) :
    Em = 0 ∧ Ep = 0 := by
  have k1 : Sf1l (lamx - rho) = 0 := by rw [sub_f1]; grind
  have k2 : Sp1l (lamx - rho) = 0 := by rw [sub_p1]; grind
  have k3 : Sll (lamx - rho) = 0 := by rw [sub_ll]; grind
  have hk := hI _ k1 k2 k3
  have hlr : lamx = rho := by grind
  subst hlr
  constructor <;> grind

/-- **Corollary 3.4 (Type I).**  Without auxiliary fields the promoted sewing
system forces both bulk equations, with no injectivity hypothesis. -/
theorem promoted_implies_bulk_typeI
    (Mm0 Mp0 dpm0 dpp0 bm0 bp0 Em Ep : R)
    (hx_m0 : dpm0 = -Mm0) (hx_p0 : dpp0 = Mp0)
    (hX_m0 : -bm0 = -Mm0) (hX_p0 : -bp0 = Mp0)
    (hO_m0 : dpm0 + bm0 = -Em) (hO_p0 : dpp0 + bp0 = -Ep) :
    Em = 0 ∧ Ep = 0 := by
  constructor <;> grind

/-! ## Section 4: defect charges, potentials and closure -/

/-- **Proposition 4.2, closedness step.**  If Q_d is a defect charge for the
conservation law (N, J) (D_t Q_d = J_- - J_+ along the promoted solution) and
both bulk laws hold, the residual R = D_x Q_d + (N_- - N_+) has D_t R = 0.
(The paper then shows R = 0 by normalisation of this particular residual; no
global injectivity of D_t is assumed, cf. `Deriv.not_injective_of_nontrivial`.) -/
theorem potential_residual_closed (S : SpaceTime R) (Q Nm Np Jm Jp : R)
    (hQ : S.Dt Q = Jm - Jp)
    (hm : S.Dt Nm + S.Dx Jm = 0) (hp : S.Dt Np + S.Dx Jp = 0) :
    S.Dt (S.Dx Q + (Nm - Np)) = 0 := by
  rw [S.Dt.map_add, S.comm Q, hQ, S.Dt.map_sub, S.Dx.map_sub]
  grind

/-- Normalisation applied to one residual only: a hypothesis about that residual. -/
theorem potential_from_normalised_residual (S : SpaceTime R) (Q Nm Np Jm Jp : R)
    (normalised : R → Prop)
    (kernel : ∀ r, normalised r → S.Dt r = 0 → r = 0)
    (hn : normalised (S.Dx Q + (Nm - Np)))
    (hQ : S.Dt Q = Jm - Jp)
    (hm : S.Dt Nm + S.Dx Jm = 0) (hp : S.Dt Np + S.Dx Jp = 0) :
    S.Dx Q = -(Nm - Np) := by
  have h := kernel _ hn (potential_residual_closed S Q Nm Np Jm Jp hQ hm hp)
  grind

/-- **Lemma 5.2, algebraic core.**  For coordinates x, t with D_t x = 0,
D_x x = 1, D_t t = 1, D_x t = 0, an affine current splits into its x- and
t-coefficient laws and the x,t-independent closure term. -/
theorem affine_law_expansion (S : SpaceTime R) (x t a1 a2 a0 b1 b2 b0 : R)
    (hxt : S.Dt x = 0) (hxx : S.Dx x = 1) (htt : S.Dt t = 1) (htx : S.Dx t = 0) :
    S.Dt (x * a1 + t * a2 + a0) + S.Dx (x * b1 + t * b2 + b0) =
      x * (S.Dt a1 + S.Dx b1) + t * (S.Dt a2 + S.Dx b2) +
      (a2 + b1 + S.Dt a0 + S.Dx b0) := by
  simp only [S.Dt.map_add, S.Dx.map_add, S.Dt.map_mul, S.Dx.map_mul, hxt, hxx, htt, htx]
  grind

/-- **Proposition 4.3 (closure gives a conserved defect density).**  Let law 1
have defect charge Q1 and law 2 have potential Q2 (D_x Q2 = -(N2_- - N2_+)),
and suppose on each side the closure term of an affine law vanishes:
N2 + J1 + D_t a0 + D_x b0 = 0.  Then G = Q1 + (a0_- - a0_+) is a conserved
density with flux (b0_- - b0_+) - Q2. -/
theorem closure_conserved_density (S : SpaceTime R)
    (Q1 Q2 J1m J1p N2m N2p a0m a0p b0m b0p : R)
    (hQ1 : S.Dt Q1 = J1m - J1p) (hQ2 : S.Dx Q2 = -(N2m - N2p))
    (hcm : N2m + J1m + S.Dt a0m + S.Dx b0m = 0)
    (hcp : N2p + J1p + S.Dt a0p + S.Dx b0p = 0) :
    S.Dt (Q1 + (a0m - a0p)) + S.Dx ((b0m - b0p) - Q2) = 0 := by
  simp only [S.Dt.map_add, S.Dt.map_sub, S.Dx.map_sub, hQ1, hQ2]
  grind

/-! ## Section 5: transport of potentials by a Lorentz boost -/

/-- **Lemma 5.3, two-dimensional Lorentz core.**  With Lambda = [[c,s],[s,c]],
c^2 - s^2 = 1, epsilon = [[0,1],[-1,0]] and the chain rule d' = Lambda^{-T} d
for derivatives, Lambda epsilon d = epsilon d' componentwise.  Hence if the
current differences are epsilon-curls of potentials P^nu, the boosted currents
are epsilon-curls of the boosted potentials Lambda P. -/
theorem lorentz_curl (c s d0 d1 : R) (h : c * c - s * s = 1) :
    let d0' := c * d0 - s * d1      -- (Lambda^{-T} d)_0
    let d1' := -s * d0 + c * d1     -- (Lambda^{-T} d)_1
    -- d' really is Lambda^{-T} d:  Lambda^T d' = d  (this uses c^2 - s^2 = 1)
    (c * d0' + s * d1' = d0 ∧ s * d0' + c * d1' = d1) ∧
    -- (Lambda eps d)_mu  =  (eps d')_mu,  with (eps d)_0 = d1, (eps d)_1 = -d0
    (c * d1 + s * (-d0) = d1' ∧ s * d1 + c * (-d0) = -d0') := by
  intro d0' d1'
  refine ⟨⟨?_, ?_⟩, ?_, ?_⟩
  · have e : c * (c * d0 - s * d1) + s * (-s * d0 + c * d1) = (c * c - s * s) * d0 := by grind
    simp only [d0', d1']; rw [e, h]; grind
  · have e : s * (c * d0 - s * d1) + c * (-s * d0 + c * d1) = (c * c - s * s) * d1 := by grind
    simp only [d0', d1']; rw [e, h]; grind
  · grind
  · grind

/-! ## Section 7: rigidity and involution -/

/-- **Lemma 7.2, inductive structure.**  Let G d be the degree-d homogeneous part
of a vacuum-normalised conserved local functional.  If (i) the lowest nonzero
part is conserved by the linearised flow, and (ii) under nonresonance a
linearly conserved homogeneous functional of degree >= 3 vanishes, then every
part vanishes once the parts of degree 0, 1, 2 do. -/
theorem graded_rigidity {M : Type} [Zero M] (G : Nat → M) (LinCons : Nat → M → Prop)
    (h_low : ∀ d, (∀ e, e < d → G e = 0) → LinCons d (G d))
    (h_rig : ∀ d, 3 ≤ d → ∀ g, LinCons d g → g = 0)
    (h0 : G 0 = 0) (h1 : G 1 = 0) (h2 : G 2 = 0) : ∀ d, G d = 0 := by
  intro d
  refine Nat.strongRecOn d ?_
  intro n ih
  match n, ih with
  | 0, _ => exact h0
  | 1, _ => exact h1
  | 2, _ => exact h2
  | k + 3, ih => exact h_rig (k + 3) (by omega) _ (h_low (k + 3) ih)

/-- **Theorem 7.3, structure.**  The bracket of two conserved charges is a
conserved local functional (Jacobi identity); its parts of degree 0 and 1
vanish when the linear parts of the charges leave the charges invariant
(hypothesis (L)); its quadratic part is the bracket of quadratic parts, which
vanishes when they commute, or under (NR2) together with (L').  That vanishing
enters as the hypothesis `hNR2`.  Rigidity then gives involution. -/
theorem involution {M : Type} [Zero M] (B : Nat → M) (LinCons : Nat → M → Prop)
    (h_low : ∀ d, (∀ e, e < d → B e = 0) → LinCons d (B d))
    (h_rig : ∀ d, 3 ≤ d → ∀ g, LinCons d g → g = 0)
    (hL0 : B 0 = 0) (hL1 : B 1 = 0) (hNR2 : B 2 = 0) :
    ∀ d, B d = 0 :=
  graded_rigidity B LinCons h_low h_rig hL0 hL1 hNR2

end GeneralFramework
