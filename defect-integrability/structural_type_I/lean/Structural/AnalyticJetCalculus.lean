module

public import Structural.AnalyticTaylor
public import Mathlib.Analysis.Calculus.FDeriv.Analytic
import Mathlib.Analysis.Calculus.FDeriv.Mul

/-!
# Differentiation of actual analytic finite-jet functions

Spatial differentiation increases the allowed jet order by one. The
operator is the actual Fréchet derivative evaluated on the vector of
shifted jets, and preserves analyticity near the vacuum. Partial
differentiation is likewise an actual derivative. Both respect equality
of germs, and both agree with the polynomial operators on evaluated
polynomials. Commutation with Taylor expansion of a general analytic
function is a separate obligation.
-/

@[expose] public section
noncomputable section
namespace Structural.Analytic
open Filter
open scoped Topology

variable {α : Type*} [Fintype α] {N : ℕ}

/-- Drop the highest spatial jet. -/
def lowerJets : JetSpace α (N+1) →L[ℝ] JetSpace α N :=
  ContinuousLinearMap.pi fun j => ContinuousLinearMap.proj (j.1, j.2.castSucc)

/-- The tangent vector used by spatial differentiation: its order `k`
coordinate is the input's order `k+1` coordinate. -/
def shiftedJets : JetSpace α (N+1) →L[ℝ] JetSpace α N :=
  ContinuousLinearMap.pi fun j => ContinuousLinearMap.proj (j.1, j.2.succ)

omit [Fintype α] in
@[simp] theorem lowerJets_apply (x : JetSpace α (N+1)) (j : α × Fin (N+1)) :
    lowerJets x j = x (j.1, j.2.castSucc) := rfl

omit [Fintype α] in
@[simp] theorem shiftedJets_apply (x : JetSpace α (N+1)) (j : α × Fin (N+1)) :
    shiftedJets x j = x (j.1, j.2.succ) := rfl

/-- Actual total spatial differentiation on finite-jet functions. -/
def spatialDerivative (f : JetSpace α N → ℝ) : JetSpace α (N+1) → ℝ :=
  fun x => fderiv ℝ f (lowerJets x) (shiftedJets x)

/-- Actual differentiation in one finite jet coordinate. -/
def jetPartial (j : α × Fin (N+1)) (f : JetSpace α N → ℝ) : JetSpace α N → ℝ := by
  classical
  exact fun x => fderiv ℝ f x (Pi.single j 1)

/-- Spatial differentiation preserves analyticity, with one extra jet order. -/
theorem analyticAt_spatialDerivative {f : JetSpace α N → ℝ}
    (hf : AnalyticAt ℝ f 0) : AnalyticAt ℝ (spatialDerivative f) 0 := by
  have hd : AnalyticAt ℝ (fun x : JetSpace α (N+1) => fderiv ℝ f (lowerJets x)) 0 := by
    have h := (lowerJets (α := α) (N := N)).analyticAt (0 : JetSpace α (N+1))
    have hdf : AnalyticAt ℝ (fderiv ℝ f) (lowerJets (0 : JetSpace α (N+1))) := by
      simpa using hf.fderiv
    exact hdf.comp h
  have hs := (shiftedJets (α := α) (N := N)).analyticAt (0 : JetSpace α (N+1))
  have happ := (ContinuousLinearMap.id ℝ (JetSpace α N →L[ℝ] ℝ)).analyticAt_bilinear
    (fderiv ℝ f (lowerJets (0 : JetSpace α (N+1))), shiftedJets (0 : JetSpace α (N+1)))
  exact happ.comp (f := fun x : JetSpace α (N+1) =>
    (fderiv ℝ f (lowerJets x), shiftedJets x)) (x := 0) (hd.prod hs)

/-- Partial differentiation preserves analyticity in the same finite jet space. -/
theorem analyticAt_jetPartial (j : α × Fin (N+1)) {f : JetSpace α N → ℝ}
    (hf : AnalyticAt ℝ f 0) : AnalyticAt ℝ (jetPartial j f) 0 := by
  classical
  exact ((ContinuousLinearMap.apply ℝ ℝ (Pi.single j (1 : ℝ))).analyticAt
    (fderiv ℝ f 0)).comp hf.fderiv

omit [Fintype α] in
/-- Spatial differentiation depends only on the germ at the zero jet. -/
theorem spatialDerivative_congr {f g : JetSpace α N → ℝ} (h : f =ᶠ[𝓝 0] g) :
    spatialDerivative f =ᶠ[𝓝 0] spatialDerivative g := by
  have hd := h.fderiv (𝕜 := ℝ)
  have hl : Filter.Tendsto (lowerJets (α := α) (N := N)) (𝓝 0) (𝓝 0) := by
    simpa using (lowerJets (α := α) (N := N)).continuous.tendsto (0 : JetSpace α (N+1))
  filter_upwards [hl.eventually hd] with x hx
  exact congrArg (fun L => L (shiftedJets x)) hx

omit [Fintype α] in
/-- The coordinate partial derivative likewise depends only on the germ. -/
theorem jetPartial_congr (j : α × Fin (N+1)) {f g : JetSpace α N → ℝ}
    (h : f =ᶠ[𝓝 0] g) : jetPartial j f =ᶠ[𝓝 0] jetPartial j g := by
  classical
  filter_upwards [h.fderiv (𝕜 := ℝ)] with x hx
  exact congrArg (fun L => L (Pi.single j 1)) hx

open MvPolynomial Symbol Jet

/-- Actual polynomial evaluation is differentiable on the finite coordinate space. -/
theorem differentiableAt_eval {J : Type*} [Fintype J] (f : MvPolynomial J ℝ) (x : J → ℝ) :
    DifferentiableAt ℝ (fun y => eval y f) x :=
  (AnalyticOnNhd.eval_mvPolynomial f x (Set.mem_univ x)).differentiableAt

/-- The Fréchet derivative of polynomial evaluation is the constructed
constant-direction polynomial derivation. -/
theorem fderiv_eval {J : Type*} [Fintype J] (f : MvPolynomial J ℝ) (x v : J → ℝ) :
    fderiv ℝ (fun y => eval y f) x v = eval x (direction v f) := by
  induction f using MvPolynomial.induction_on with
  | C r => simp [direction]
  | add f g hf hg =>
    simp only [map_add]
    rw [fderiv_fun_add (differentiableAt_eval f x) (differentiableAt_eval g x)]
    simp [hf, hg]
  | mul_X f j hf =>
    simp only [map_mul, eval_X]
    change fderiv ℝ (fun y => eval y f *
      (ContinuousLinearMap.proj j : (J → ℝ) →L[ℝ] ℝ) y) x v = _
    rw [fderiv_fun_mul (differentiableAt_eval f x)
      (ContinuousLinearMap.proj j : (J → ℝ) →L[ℝ] ℝ).differentiableAt]
    simp [hf, direction, Derivation.leibniz, smul_eq_mul, mul_comm]

/-- The coordinate directional derivation is precisely polynomial partial differentiation. -/
theorem direction_single {J : Type*} [DecidableEq J] (j : J) :
    direction (Pi.single j (1 : ℝ)) = pderiv j := by
  apply MvPolynomial.derivation_ext
  intro k
  simp [direction, Pi.single_apply, apply_ite]

/-- Actual jet partial derivatives agree with polynomial partial derivatives. -/
theorem jetPartial_eval (j : α × Fin (N+1)) (f : MvPolynomial (α × Fin (N+1)) ℝ)
    (x : JetSpace α N) : jetPartial j (fun y => eval y f) x = eval x (pderiv j f) := by
  classical
  unfold jetPartial
  rw [fderiv_eval, direction_single]

omit [Fintype α] in
/-- Evaluation of a finite-jet polynomial ignores the newly added highest jet. -/
theorem eval_jetPolynomial_lower (f : MvPolynomial (α × Fin (N+1)) ℝ)
    (x : JetSpace α (N+1)) :
    eval (extendJet x) (jetPolynomial f) = eval (lowerJets x) f := by
  have hx : extendJet x ∘ (jetIndex (α := α) (N := N)) = lowerJets x := by
    funext j
    simp [extendJet, jetIndex,
      show j.2.val < N+1+1 from by omega]
    rfl
  simp [jetPolynomial, eval_rename, hx]

omit [Fintype α] in
/-- The polynomial total derivative and the actual shifted-jet direction
have the same evaluation. -/
theorem eval_Dx_jetPolynomial (f : MvPolynomial (α × Fin (N+1)) ℝ)
    (x : JetSpace α (N+1)) :
    eval (extendJet x) (Dx (jetPolynomial f)) =
      eval (lowerJets x) (direction (shiftedJets x) f) := by
  induction f using MvPolynomial.induction_on with
  | C r => simp [jetPolynomial]
  | add f g hf hg => simp only [jetPolynomial, map_add] at *; rw [hf, hg]
  | mul_X f j hf =>
    have hDx : Dx (X (jetIndex j) : Density ℝ α) = X (j.1,j.2.val+1) := Dx_z _ _
    have hdir : direction (shiftedJets x) (X j) = C (shiftedJets x j) := by
      simp [direction]
    have hx : eval (extendJet x) (X (jetIndex j)) = lowerJets x j := by
      simp [extendJet, jetIndex, show j.2.val < N+1+1 from by omega]
      rfl
    have hx' : eval (extendJet x) (X (j.1,j.2.val+1)) = shiftedJets x j := by
      simp [extendJet, show j.2.val+1 < N+1+1 from by omega]
      rfl
    have hprod : jetPolynomial (f * X j) = jetPolynomial f * X (jetIndex j) := by
      simp only [jetPolynomial, map_mul, rename_X]
    rw [hprod]
    simp only [Derivation.leibniz, smul_eq_mul, map_add, map_mul, hDx, hdir,
      hx, hx', eval_C, eval_X, hf, eval_jetPolynomial_lower]

/-- On polynomials, the analytic spatial derivative is exactly the already
constructed polynomial total derivative after evaluation on finite jets. -/
theorem spatialDerivative_eval (f : MvPolynomial (α × Fin (N+1)) ℝ)
    (x : JetSpace α (N+1)) :
    spatialDerivative (fun y => eval y f) x = eval (extendJet x) (Dx (jetPolynomial f)) := by
  unfold spatialDerivative
  rw [fderiv_eval, eval_Dx_jetPolynomial]

end Structural.Analytic
