module

public import Structural.MassiveSymbol
public import Structural.PolarizationMultilinear
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Ring

/-!
# Returning from frequency modes to arbitrary Cauchy vectors

The normal-mode transformation is explicitly inverted. Multilinearity then
extends massive-symbol vanishing from all sign/species choices to arbitrary
field/momentum vectors in every wave slot.
-/

@[expose] public section
noncomputable section
namespace Structural.Symbol
open MvPolynomial Jet Dispersion
variable {ι : Type*}

/-- The two frequency signs, indexed by a Boolean. -/
def modeSign (b : Bool) : ℝ := if b then -1 else 1

@[simp] theorem modeSign_sq (b : Bool) : modeSign b ^ 2 = 1 := by cases b <;> norm_num [modeSign]

/-- A normal mode at one fixed spatial momentum. -/
def normalVector (massSq : ι → ℝ) (k : ℝ) (m : ι × Bool) : (ι × Bool) → ℂ := by
  classical
  exact fun c => if c.1 = m.1 then
    if c.2 then Complex.I * (modeSign m.2 * frequency (massSq m.1) k : ℝ) else 1 else 0

/-- Explicit inverse coefficients `(u ± p/(i ω))/2`. -/
def normalAmplitude (massSq : ι → ℝ) (k : ℝ) (v : (ι × Bool) → ℂ) (m : ι × Bool) : ℂ :=
  (v (m.1,false) + (modeSign m.2 : ℂ) * v (m.1,true) /
    (Complex.I * (frequency (massSq m.1) k : ℂ))) / 2

/-- The two massive frequency modes span the Cauchy coordinates for each
species. All divisions are justified by strictly positive masses. -/
theorem normal_expansion [Fintype ι] (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (k : ℝ) (v : (ι × Bool) → ℂ) :
    (∑ m : ι × Bool, normalAmplitude massSq k v m • normalVector massSq k m) = v := by
  classical
  funext ⟨a,b⟩
  have hw : (frequency (massSq a) k : ℂ) ≠ 0 := by
    exact_mod_cast ne_of_gt (frequency_pos (hm a) k)
  have hiw : Complex.I * (frequency (massSq a) k : ℂ) ≠ 0 :=
    mul_ne_zero Complex.I_ne_zero hw
  simp only [Finset.sum_apply, Pi.smul_apply, smul_eq_mul, Fintype.sum_prod_type]
  rw [Finset.sum_eq_single a]
  · cases b <;> simp [normalAmplitude, normalVector, modeSign] <;>
      field_simp <;> ring
  · intro a' ha' hne
    simp [normalVector, Ne.symm hne]
  · simp

/-- The per-slot vectors agree with the normal modes used in the spectral
proof; only their argument order differs. -/
theorem normalVector_eq_modeVector {S : Type*} (massSq : ι → ℝ)
    (k : S → ℝ) (m : S → ι × Bool) (s : S) (c : ι × Bool) :
    normalVector massSq (k s) (m s) c =
      modeVector massSq (fun s => (m s).1) (fun s => modeSign (m s).2) k c s := by
  simp only [normalVector, modeVector, timeEigen]

/-- Massive conservation kills every polarized Cauchy-vector symbol on the
momentum hyperplane, not only the normal-mode components. -/
theorem massive_arbitrary_vectors_eq_zero [Fintype ι] {n : ℕ}
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (f : Density ℂ (ι × Bool))
    (hc : Conserved (Free.characteristic (fun a => (massSq a : ℂ))) (integral f))
    (k : Fin (n+2) → ℝ) (v : Option (Fin (n+2)) → (ι × Bool) → ℂ) :
    polarized (spatialEigen (onHyperplane k)) (fun c s => v s c) f = 0 := by
  classical
  let M := wavePolarization f (spatialEigen (onHyperplane k))
  change M v = 0
  have hv : v = fun s => ∑ m : ι × Bool,
      normalAmplitude massSq (onHyperplane k s) (v s) m •
        normalVector massSq (onHyperplane k s) m := by
    funext s
    exact (normal_expansion massSq hm _ _).symm
  rw [hv, M.map_sum]
  apply Finset.sum_eq_zero
  intro m hm'
  rw [M.map_smul_univ]
  suffices hz : M (fun s => normalVector massSq (onHyperplane k s) (m s)) = 0 by
    rw [hz, smul_zero]
  change polarized (spatialEigen (onHyperplane k))
    (fun c s => normalVector massSq (onHyperplane k s) (m s) c) f = 0
  simp only [normalVector_eq_modeVector]
  exact massive_polarized_eq_zero massSq (fun s => (m s).1) (fun s => modeSign (m s).2)
    hm (fun s => modeSign_sq _) f hc k

/-- The original real jet model inherits arbitrary-vector symbol vanishing. -/
theorem real_massive_arbitrary_vectors_eq_zero [Fintype ι] {n : ℕ}
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (f : Density ℝ (ι × Bool)) (hc : Conserved (Free.characteristic massSq) (integral f))
    (k : Fin (n+2) → ℝ) (v : Option (Fin (n+2)) → (ι × Bool) → ℂ) :
    polarized (spatialEigen (onHyperplane k)) (fun c s => v s c)
      (MvPolynomial.map Complex.ofRealHom f) = 0 := by
  exact massive_arbitrary_vectors_eq_zero massSq hm _
    (map_free_conserved Complex.ofRealHom massSq f hc) k v

end Structural.Symbol
