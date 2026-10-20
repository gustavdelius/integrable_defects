module

public import Structural.FormalRigidity
public import Mathlib.Analysis.Analytic.Basic
public import Mathlib.Analysis.Analytic.Uniqueness
public import Mathlib.Analysis.Analytic.Polynomial

/-!
# Actual analytic expansions as homogeneous jet polynomials

For a function of a fixed finite collection of real jets, its genuine
Fréchet power series gives homogeneous polynomials in the existing jet
algebra. We construct those polynomials, prove their common spatial-order
bound, and prove that their evaluations sum to the original function near
the vacuum. Thus zero polynomial coefficients imply a zero analytic germ.

This file does not yet prove that total differentiation, evolution, or
Euler differentiation commute with this Taylor construction.
-/

@[expose] public section
noncomputable section
namespace Structural.Analytic
open MvPolynomial Jet Filter
open scoped Topology

/-- The polynomial on the diagonal of a multilinear form, constructed by
expanding every vector in the coordinate basis. No symmetry is required. -/
def diagonalPolynomial {J : Type*} [Fintype J] {n : ℕ}
    (L : MultilinearMap ℝ (fun _ : Fin n => J → ℝ) ℝ) : MvPolynomial J ℝ := by
  classical
  exact ∑ b : Fin n → J, C (L (fun i => Pi.single (b i) 1)) * ∏ i, X (b i)

theorem diagonalPolynomial_homogeneous {J : Type*} [Fintype J] {n : ℕ}
    (L : MultilinearMap ℝ (fun _ : Fin n => J → ℝ) ℝ) :
    (diagonalPolynomial L).IsHomogeneous n := by
  classical
  unfold diagonalPolynomial
  apply IsHomogeneous.sum
  intro b _
  apply IsHomogeneous.C_mul
  simpa using IsHomogeneous.prod Finset.univ (fun i : Fin n => (X (b i) : MvPolynomial J ℝ))
    (fun _ => 1) (fun i _ => isHomogeneous_X ℝ (b i))

/-- Evaluation of the constructed polynomial is the original diagonal form. -/
theorem eval_diagonalPolynomial {J : Type*} [Fintype J] {n : ℕ}
    (L : MultilinearMap ℝ (fun _ : Fin n => J → ℝ) ℝ) (x : J → ℝ) :
    eval x (diagonalPolynomial L) = L (fun _ => x) := by
  classical
  have hx : (∑ j : J, x j • Pi.single j (1 : ℝ)) = x := by
    ext j
    simp [Pi.single_apply]
  have h := L.map_sum (fun _ : Fin n => fun j : J => x j • Pi.single j (1 : ℝ))
  rw [hx] at h
  simpa [diagonalPolynomial, MultilinearMap.map_smul_univ, smul_eq_mul, mul_comm] using h.symm

/-- The finite jet coordinates through spatial order `N`. -/
abbrev JetSpace (α : Type*) (N : ℕ) := (α × Fin (N+1)) → ℝ

/-- Embed finite jet labels into the independent infinite jet-label type. -/
def jetIndex {α : Type*} {N : ℕ} (j : α × Fin (N+1)) : α × ℕ := (j.1, j.2.val)

theorem jetIndex_injective {α : Type*} {N : ℕ} :
    Function.Injective (jetIndex (α := α) (N := N)) := by
  rintro ⟨a,i⟩ ⟨b,j⟩ h
  simp only [jetIndex, Prod.mk.injEq] at h
  exact Prod.ext h.1 (Fin.ext h.2)

/-- Extend a finite jet vector by zero; only its first `N+1` coordinates
will be used in the polynomials constructed here. -/
def extendJet {α : Type*} {N : ℕ} (x : JetSpace α N) (j : α × ℕ) : ℝ :=
  if h : j.2 < N+1 then x (j.1, ⟨j.2,h⟩) else 0

@[simp] theorem extendJet_jetIndex {α : Type*} {N : ℕ} (x : JetSpace α N)
    (j : α × Fin (N+1)) : extendJet x (jetIndex j) = x j := by
  simp [extendJet, jetIndex, j.2.isLt]

/-- Rename a finite-coordinate polynomial as a density in the existing jet algebra. -/
def jetPolynomial {α : Type*} {N : ℕ} (f : MvPolynomial (α × Fin (N+1)) ℝ) :
    Density ℝ α := rename jetIndex f

theorem jetPolynomial_order_le {α : Type*} {N : ℕ}
    (f : MvPolynomial (α × Fin (N+1)) ℝ) : order (jetPolynomial f) ≤ N := by
  classical
  apply Finset.sup_le
  intro j hj
  obtain ⟨k, _, hk⟩ := mem_vars_rename jetIndex f hj
  subst j
  exact Nat.le_of_lt_succ k.2.isLt

@[simp] theorem eval_jetPolynomial {α : Type*} {N : ℕ}
    (f : MvPolynomial (α × Fin (N+1)) ℝ) (x : JetSpace α N) :
    eval (extendJet x) (jetPolynomial f) = eval x f := by
  simp [jetPolynomial, eval_rename, Function.comp_def]

/-- Homogeneous jet coefficients constructed from an actual Fréchet power series. -/
def amplitudeSeries {α : Type*} [Fintype α] {N : ℕ}
    (p : FormalMultilinearSeries ℝ (JetSpace α N) ℝ) : Formal.AmplitudeSeries α where
  coeff n := jetPolynomial (diagonalPolynomial (p n).toMultilinearMap)
  homogeneous n := (diagonalPolynomial_homogeneous (p n).toMultilinearMap).rename_isHomogeneous

theorem amplitudeSeries_order_le {α : Type*} [Fintype α] {N : ℕ}
    (p : FormalMultilinearSeries ℝ (JetSpace α N) ℝ) (n : ℕ) :
    order ((amplitudeSeries p).coeff n) ≤ N :=
  jetPolynomial_order_le _

@[simp] theorem eval_amplitudeSeries {α : Type*} [Fintype α] {N : ℕ}
    (p : FormalMultilinearSeries ℝ (JetSpace α N) ℝ) (n : ℕ) (x : JetSpace α N) :
    eval (extendJet x) ((amplitudeSeries p).coeff n) = p n (fun _ => x) := by
  exact (eval_jetPolynomial _ x).trans (eval_diagonalPolynomial _ x)

/-- The polynomial coefficients really sum to the original analytic function
on a neighborhood of the vacuum. This is convergence inherited from its
given Fréchet expansion, not a convergence claim about arbitrary formal series. -/
theorem eventually_hasSum_amplitudeSeries {α : Type*} [Fintype α] {N : ℕ}
    {f : JetSpace α N → ℝ} {p : FormalMultilinearSeries ℝ (JetSpace α N) ℝ}
    (hf : HasFPowerSeriesAt f p 0) :
    ∀ᶠ x in 𝓝 0, HasSum (fun n => eval (extendJet x) ((amplitudeSeries p).coeff n)) (f x) := by
  simpa using hf.eventually_hasSum

/-- Actual polynomial Taylor coefficients detect the zero analytic germ.
Vanishing as a polynomial is stronger than vanishing modulo divergences;
the latter must first be passed through the Euler operator. -/
theorem eventually_eq_zero_of_amplitudeSeries_eq_zero {α : Type*} [Fintype α] {N : ℕ}
    {f : JetSpace α N → ℝ} {p : FormalMultilinearSeries ℝ (JetSpace α N) ℝ}
    (hf : HasFPowerSeriesAt f p 0) (hp : ∀ n, (amplitudeSeries p).coeff n = 0) :
    ∀ᶠ x in 𝓝 0, f x = 0 := by
  filter_upwards [eventually_hasSum_amplitudeSeries hf] with x hx
  simp only [hp, map_zero] at hx
  exact hx.unique hasSum_zero

/-- Every analytic finite-jet function has a homogeneous polynomial expansion
with one spatial-order bound and actual convergence near the vacuum. -/
theorem analyticAt_has_amplitudeSeries {α : Type*} [Fintype α] {N : ℕ}
    {f : JetSpace α N → ℝ} (hf : AnalyticAt ℝ f 0) :
    ∃ F : Formal.AmplitudeSeries α, (∀ n, order (F.coeff n) ≤ N) ∧
      ∀ᶠ x in 𝓝 0, HasSum (fun n => eval (extendJet x) (F.coeff n)) (f x) := by
  obtain ⟨p,hp⟩ := hf
  exact ⟨amplitudeSeries p, amplitudeSeries_order_le p, eventually_hasSum_amplitudeSeries hp⟩

/-- The polynomial coefficients depend only on the analytic germ, even
though nonsymmetric multilinear power-series representatives need not be unique. -/
theorem amplitudeSeries_eq_of_eventuallyEq {α : Type*} [Fintype α] {N : ℕ}
    {f g : JetSpace α N → ℝ} {p q : FormalMultilinearSeries ℝ (JetSpace α N) ℝ}
    (hf : HasFPowerSeriesAt f p 0) (hg : HasFPowerSeriesAt g q 0)
    (heq : f =ᶠ[𝓝 0] g) (n : ℕ) :
    (amplitudeSeries p).coeff n = (amplitudeSeries q).coeff n := by
  have hzero : HasFPowerSeriesAt (0 : JetSpace α N → ℝ) (p-q) 0 :=
    (hf.sub hg).congr (by filter_upwards [heq] with x hx; simp [hx])
  apply congrArg jetPolynomial
  apply (diagonalPolynomial_homogeneous (p n).toMultilinearMap).funext
    (diagonalPolynomial_homogeneous (q n).toMultilinearMap)
  intro x
  rw [eval_diagonalPolynomial, eval_diagonalPolynomial]
  exact sub_eq_zero.mp (hzero.apply_eq_zero n x)

/-- Conversely, equality of the polynomial coefficients implies equality
of the actual analytic germs. -/
theorem eventuallyEq_of_amplitudeSeries_eq {α : Type*} [Fintype α] {N : ℕ}
    {f g : JetSpace α N → ℝ} {p q : FormalMultilinearSeries ℝ (JetSpace α N) ℝ}
    (hf : HasFPowerSeriesAt f p 0) (hg : HasFPowerSeriesAt g q 0)
    (heq : ∀ n, (amplitudeSeries p).coeff n = (amplitudeSeries q).coeff n) :
    f =ᶠ[𝓝 0] g := by
  filter_upwards [eventually_hasSum_amplitudeSeries hf, eventually_hasSum_amplitudeSeries hg]
    with x hx hy
  simp only [heq] at hx
  exact hx.unique hy

end Structural.Analytic
