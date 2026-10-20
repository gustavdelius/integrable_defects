module

public import Structural.NormalModes
public import Structural.JetAlgebra
public import Mathlib.LinearAlgebra.Vandermonde
public import Mathlib.LinearAlgebra.Matrix.NonsingularInverse

/-!
# Faithfulness of real-momentum wave tests on finite jets

A Vandermonde matrix expresses any finite Cauchy jet as a finite sum of
complex plane-wave jets with real integer momenta. Polynomial finite support
and multilinearity then make unrestricted wave tests faithful on each
homogeneous amplitude degree.
-/

@[expose] public section
noncomputable section
namespace Structural.Symbol
open MvPolynomial Jet

/-- Polarization sees only coordinates actually occurring in the polynomial. -/
theorem polarization_congr_vars {R α S : Type*} [CommRing R] [Fintype S]
    (f : MvPolynomial α R) (v w : S → α → R)
    (h : ∀ s a, a ∈ f.vars → v s a = w s a) : polarization f v = polarization f w := by
  unfold polarization
  congr 2
  apply eval₂Hom_congr' rfl _ rfl
  intro a ha _
  apply Finset.sum_congr rfl
  intro s hs
  rw [h s a ha]

/-- Real integer momenta provide distinct complex spatial eigenvalues. -/
theorem integer_wave_nodes_injective (N : ℕ) :
    Function.Injective (fun j : Fin (N+1) => Complex.I * (j.val : ℂ)) := by
  intro i j hij
  apply Fin.ext
  exact_mod_cast (mul_left_cancel₀ Complex.I_ne_zero hij)

/-- Any prescribed finite jet can be interpolated by finitely many waves.
No finiteness assumption on the field-component type is needed. -/
theorem finite_jet_wave_interpolation {α : Type*} (N : ℕ) (x : α × ℕ → ℂ) :
    ∃ v : Fin (N+1) → α → ℂ, ∀ a r, r ≤ N →
      (∑ j : Fin (N+1), v j a * (Complex.I * (j.val : ℂ))^r) = x (a,r) := by
  classical
  let nodes := fun j : Fin (N+1) => Complex.I * (j.val : ℂ)
  have hdet : (Matrix.vandermonde nodes).det ≠ 0 :=
    Matrix.det_vandermonde_ne_zero_iff.mpr (integer_wave_nodes_injective N)
  have hsurj : Function.Surjective (Matrix.vandermonde nodes).vecMul :=
    Matrix.vecMul_surjective_iff_isUnit.mpr
      ((Matrix.isUnit_iff_isUnit_det _).mpr (isUnit_iff_ne_zero.mpr hdet))
  choose c hc using (fun a : α => hsurj (fun r : Fin (N+1) => x (a,r.val)))
  refine ⟨fun j a => c a j, ?_⟩
  intro a r hr
  have h := congrFun (hc a) (⟨r, Nat.lt_succ_of_le hr⟩ : Fin (N+1))
  simpa [Matrix.vecMul, dotProduct, Matrix.vandermonde, nodes] using h

/-- Vanishing on all real-momentum wave jets forces a homogeneous density
to vanish as a polynomial. This statement has no momentum constraint. -/
theorem homogeneous_eq_zero_of_wave_tests {α S : Type*} [Fintype S]
    (f : Density ℂ α) (hf : f.IsHomogeneous (Fintype.card S))
    (h : ∀ (k : S → ℝ) (v : α → S → ℂ), polarized (spatialEigen k) v f = 0) : f = 0 := by
  classical
  apply homogeneous_eq_zero_of_polarization_zero f hf
  intro w
  choose v hv using fun s : S => finite_jet_wave_interpolation (order f) (w s)
  let W : S → (α × ℕ → ℂ) := fun s =>
    ∑ j : Fin (order f + 1), fun a => v s j a.1 * (Complex.I * (j.val : ℂ))^a.2
  have heq : polarization f w = polarization f W := by
    apply polarization_congr_vars
    intro s a ha
    simpa [W] using (hv s a.1 a.2 (le_order_of_mem_vars f a ha)).symm
  rw [heq]
  change (polarizationMap f) (fun s =>
    ∑ j : Fin (order f + 1), fun a => v s j a.1 * (Complex.I * (j.val : ℂ))^a.2) = 0
  rw [MultilinearMap.map_sum]
  apply Finset.sum_eq_zero
  intro j hj
  change polarization f (fun s a => v s (j s) a.1 * (Complex.I * ((j s).val : ℂ))^a.2) = 0
  have ht := h (fun s => ((j s).val : ℝ)) (fun a s => v s (j s) a)
  simpa only [polarized_eq_polarization, spatialEigen, Complex.ofReal_natCast] using ht

end Structural.Symbol
