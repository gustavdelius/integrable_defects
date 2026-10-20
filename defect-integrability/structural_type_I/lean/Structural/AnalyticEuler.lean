module

public import Structural.AnalyticJetCalculus
public import Structural.EulerExactness

/-!
# Actual finite-jet analytic Euler derivatives

For a density of spatial order `N`, the Euler expression uses at most order
`2N`. It is built from actual coordinate partial derivatives and iterated
spatial derivatives, and is analytic whenever the density is analytic.
It depends only on the germ at the vacuum and has an actual convergent
homogeneous polynomial expansion.

The remaining bridge must identify this expansion with the polynomial
Euler derivatives of the density's Taylor coefficients; that identification
is not a hypothesis of an asserted analytic rigidity theorem here.
-/

@[expose] public section
noncomputable section
namespace Structural.Analytic
open Filter
open scoped Topology

variable {α : Type*} [Fintype α] {N M : ℕ}

/-- Restrict a larger finite jet vector to a specified lower spatial order. -/
def restrictJets (h : N ≤ M) : JetSpace α M →L[ℝ] JetSpace α N :=
  ContinuousLinearMap.pi fun j =>
    ContinuousLinearMap.proj (j.1, j.2.castLE (Nat.add_le_add_right h 1))

/-- Iterated actual spatial differentiation, retaining the resulting finite
spatial order in the type. -/
def iteratedSpatialDerivative (f : JetSpace α N → ℝ) :
    (k : ℕ) → JetSpace α (N+k) → ℝ
  | 0 => f
  | k+1 => spatialDerivative (iteratedSpatialDerivative f k)

theorem analyticAt_iteratedSpatialDerivative {f : JetSpace α N → ℝ}
    (hf : AnalyticAt ℝ f 0) (k : ℕ) :
    AnalyticAt ℝ (iteratedSpatialDerivative f k) 0 := by
  induction k with
  | zero => exact hf
  | succ k ih => exact analyticAt_spatialDerivative ih

omit [Fintype α] in
theorem iteratedSpatialDerivative_congr {f g : JetSpace α N → ℝ}
    (h : f =ᶠ[𝓝 0] g) (k : ℕ) :
    iteratedSpatialDerivative f k =ᶠ[𝓝 0] iteratedSpatialDerivative g k := by
  induction k with
  | zero => exact h
  | succ k ih => exact spatialDerivative_congr ih

/-- The Euler derivative in component `a`, realized on jets through order `2N`. -/
def eulerFunction (a : α) (f : JetSpace α N → ℝ) : JetSpace α (N+N) → ℝ :=
  fun x => ∑ k : Fin (N+1), (-1 : ℝ)^k.val *
    iteratedSpatialDerivative (jetPartial (a,k) f) k.val
      (restrictJets (by have := k.isLt; omega) x)

/-- Euler derivatives of actual analytic finite-jet densities are analytic. -/
theorem analyticAt_eulerFunction (a : α) {f : JetSpace α N → ℝ}
    (hf : AnalyticAt ℝ f 0) : AnalyticAt ℝ (eulerFunction a f) 0 := by
  unfold eulerFunction
  apply Finset.analyticAt_fun_sum
  intro k _
  apply AnalyticAt.mul analyticAt_const
  have hi := analyticAt_iteratedSpatialDerivative (analyticAt_jetPartial (a,k) hf) k.val
  have hbound : N+k.val ≤ N+N := by have := k.isLt; omega
  have hr := (restrictJets (α := α) hbound).analyticAt (0 : JetSpace α (N+N))
  have hi' : AnalyticAt ℝ (iteratedSpatialDerivative (jetPartial (a,k) f) k.val)
      (restrictJets hbound (0 : JetSpace α (N+N))) := by simpa using hi
  exact hi'.comp hr

omit [Fintype α] in
/-- The finite Euler expression is independent of the chosen representative
of an analytic germ. Analyticity itself is not needed for this congruence. -/
theorem eulerFunction_congr (a : α) {f g : JetSpace α N → ℝ}
    (h : f =ᶠ[𝓝 0] g) : eulerFunction a f =ᶠ[𝓝 0] eulerFunction a g := by
  have he : ∀ k : Fin (N+1), ∀ᶠ x : JetSpace α (N+N) in 𝓝 0,
      iteratedSpatialDerivative (jetPartial (a,k) f) k.val
        (restrictJets (by have := k.isLt; omega) x) =
      iteratedSpatialDerivative (jetPartial (a,k) g) k.val
        (restrictJets (by have := k.isLt; omega) x) := by
    intro k
    have hi := iteratedSpatialDerivative_congr (jetPartial_congr (a,k) h) k.val
    have hbound : N+k.val ≤ N+N := by have := k.isLt; omega
    have hr : Tendsto (restrictJets (α := α) hbound) (𝓝 0) (𝓝 0) := by
      simpa using (restrictJets (α := α) hbound).continuous.tendsto (0 : JetSpace α (N+N))
    exact hr.eventually hi
  filter_upwards [Filter.eventually_all.mpr he] with x hx
  unfold eulerFunction
  apply Finset.sum_congr rfl
  intro k _
  rw [hx k]

/-- The actual analytic Euler function has a convergent polynomial expansion,
with one spatial-order bound `2N` for every coefficient. -/
theorem eulerFunction_has_amplitudeSeries (a : α) {f : JetSpace α N → ℝ}
    (hf : AnalyticAt ℝ f 0) :
    ∃ F : Formal.AmplitudeSeries α, (∀ n, Jet.order (F.coeff n) ≤ N+N) ∧
      ∀ᶠ x in 𝓝 0, HasSum (fun n => MvPolynomial.eval (extendJet x) (F.coeff n))
        (eulerFunction a f x) :=
  analyticAt_has_amplitudeSeries (analyticAt_eulerFunction a hf)

end Structural.Analytic
