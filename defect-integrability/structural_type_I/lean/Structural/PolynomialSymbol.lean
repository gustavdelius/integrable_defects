module

public import Structural.NormalModes
public import Structural.MomentumDivisibility
public import Mathlib.Algebra.MvPolynomial.Equiv

/-!
# Polynomial Fourier symbols and their momentum factors

The wave construction over a polynomial coefficient ring gives actual finite
momentum polynomials. For every conserved massive density, their restrictions
to the momentum hyperplane vanish and hence they have a total-momentum factor.
Reassembling these factors as a density primitive is not proved here.
-/

@[expose] public section
noncomputable section
namespace Structural.Symbol
open MvPolynomial Jet
variable {R K α S : Type*} [CommRing R] [CommRing K] [Fintype S]

/-- Plane-wave substitution commutes with changing its coefficient ring. -/
theorem map_waves (c : R →+* K) (k : S → R) (v : α → S → R) (f : Density R α) :
    MvPolynomial.map c (waves k v f) =
      waves (fun s => c (k s)) (fun a s => c (v a s)) (MvPolynomial.map c f) := by
  induction f using MvPolynomial.induction_on with
  | C r => simp [waves]
  | add f g hf hg => simp only [map_add, hf, hg]
  | mul_X f j hf =>
    simp only [map_mul, hf, map_X]
    congr 1
    change MvPolynomial.map c (waves k v (z j.1 j.2)) = _
    simp [waves, z]

theorem map_polarized (c : R →+* K) (k : S → R) (v : α → S → R) (f : Density R α) :
    c (polarized k v f) =
      polarized (fun s => c (k s)) (fun a s => c (v a s)) (MvPolynomial.map c f) := by
  unfold polarized component
  rw [← coeff_map, map_waves]

/-- The Fourier symbol with constant Cauchy vectors and indeterminate
momenta. It is a polynomial, not merely a continuous kernel. -/
def fourierPolynomial (v : α → S → ℂ) (f : Density ℂ α) : MvPolynomial S ℂ :=
  polarized (fun s => C Complex.I * X s) (fun a s => C (v a s)) (MvPolynomial.map C f)

/-- Evaluation of the polynomial symbol is the previously constructed
plane-wave symbol, with no approximation or infinite Fourier sum. -/
theorem eval_fourierPolynomial (v : α → S → ℂ) (f : Density ℂ α) (k : S → ℂ) :
    eval k (fourierPolynomial v f) =
      polarized (fun s => Complex.I * k s) v f := by
  rw [fourierPolynomial, map_polarized]
  simp only [map_mul, eval_C, eval_X, map_map]
  have hc : (eval k).comp (C : ℂ →+* MvPolynomial S ℂ) = RingHom.id ℂ := by ext r; simp
  rw [hc, map_id]

section Division
variable {ι : Type*} [Fintype ι]

/-- Actual momentum-polynomial vanishing, now for arbitrary constant
Cauchy vectors; the square-root mode factors have been removed. -/
theorem conserved_fourierPolynomial_vanishes {n : ℕ}
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (f : Density ℂ (ι × Bool))
    (hc : Conserved (Free.characteristic (fun a => (massSq a : ℂ))) (integral f))
    (v : (ι × Bool) → Option (Fin (n+2)) → ℂ) (k : Fin (n+2) → ℝ) :
    eval (fun s => (onHyperplane k s : ℂ)) (fourierPolynomial v f) = 0 := by
  rw [eval_fourierPolynomial]
  exact massive_arbitrary_vectors_eq_zero massSq hm f hc k (fun s c => v c s)

/-- Restriction of a multivariate polynomial expressed with a distinguished
last momentum agrees with evaluation on the momentum hyperplane. -/
theorem eval_restrict_option (P : MvPolynomial (Option S) ℂ) (k : S → ℂ) :
    eval k (Momentum.restrict (optionEquivLeft ℂ S P)) =
      eval (fun s => s.elim (-(∑ s, k s)) k) P := by
  rw [optionEquivLeft_elim_eval]
  unfold Momentum.restrict
  rw [← Polynomial.eval_map_apply]
  simp [Momentum.sumVariables]

/-- The actual symbol of a conserved massive density has a total-momentum
factor in every amplitude degree at least three. The factor is polynomial,
so this step preserves finite differential order. -/
theorem conserved_fourierPolynomial_divisible {n : ℕ}
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (f : Density ℂ (ι × Bool))
    (hc : Conserved (Free.characteristic (fun a => (massSq a : ℂ))) (integral f))
    (v : (ι × Bool) → Option (Fin (n+2)) → ℂ) :
    Momentum.totalMomentum ∣ optionEquivLeft ℂ (Fin (n+2)) (fourierPolynomial v f) := by
  apply Momentum.complex_divisible_of_real_vanishes
  intro k
  rw [eval_restrict_option]
  have heq : (fun s => s.elim (-(∑ j, (k j : ℂ))) (fun j => (k j : ℂ))) =
      (fun s => (onHyperplane k s : ℂ)) := by
    funext s
    cases s <;> simp [onHyperplane]
  rw [heq]
  exact conserved_fourierPolynomial_vanishes massSq hm f hc v k

/-- The same polynomial factor conclusion holds for real conserved densities. -/
theorem real_conserved_fourierPolynomial_divisible {n : ℕ}
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (f : Density ℝ (ι × Bool)) (hc : Conserved (Free.characteristic massSq) (integral f))
    (v : (ι × Bool) → Option (Fin (n+2)) → ℂ) :
    Momentum.totalMomentum ∣ optionEquivLeft ℂ (Fin (n+2))
      (fourierPolynomial v (MvPolynomial.map Complex.ofRealHom f)) := by
  exact conserved_fourierPolynomial_divisible massSq hm _
    (map_free_conserved Complex.ofRealHom massSq f hc) v

end Division
end Structural.Symbol
