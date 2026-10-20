module

public import Structural.PlaneWave
public import Structural.Dispersion
public import Mathlib.Analysis.Complex.Basic
import Mathlib.Tactic.Ring

/-!
# Vanishing of the actual massive polarized symbols

The plane-wave substitution is specialized to the positive and negative
frequency eigenvectors of the free Klein–Gordon system. Conservation of a
polynomial local functional implies vanishing of every polarized normal-mode
component with at least three slots, on the momentum hyperplane.

Reconstruction of a density primitive from these symbols remains separate.
-/

@[expose] public section
noncomputable section
namespace Structural.Symbol

open MvPolynomial Jet Dispersion
variable {ι S : Type*} [Fintype S]

/-- Spatial eigenvalue of a real-momentum plane wave. -/
def spatialEigen (k : S → ℝ) (s : S) : ℂ := Complex.I * (k s : ℂ)

/-- Time eigenvalue for the chosen species and frequency sign. -/
def timeEigen (massSq : ι → ℝ) (species : S → ι) (sign k : S → ℝ) (s : S) : ℂ :=
  Complex.I * (sign s * frequency (massSq (species s)) (k s) : ℝ)

/-- A single normal mode has `u = 1`, `p = i σ ω` in its selected species. -/
def modeVector (massSq : ι → ℝ) (species : S → ι) (sign k : S → ℝ)
    (a : ι × Bool) (s : S) : ℂ := by
  classical
  exact if a.1 = species s then if a.2 then timeEigen massSq species sign k s else 1 else 0

omit [Fintype S] in
theorem modeVector_u (massSq : ι → ℝ) (species : S → ι) (sign k : S → ℝ)
    (a : ι) (s : S) :
    modeVector massSq species sign k (a,true) s =
      timeEigen massSq species sign k s * modeVector massSq species sign k (a,false) s := by
  classical
  by_cases h : a = species s <;> simp [modeVector, h]

omit [Fintype S] in
theorem modeVector_p (massSq : ι → ℝ) (species : S → ι) (sign k : S → ℝ)
    (hm : ∀ a, 0 < massSq a) (hs : ∀ s, sign s ^ 2 = 1) (a : ι) (s : S) :
    (spatialEigen k s ^ 2 - (massSq a : ℂ)) * modeVector massSq species sign k (a,false) s =
      timeEigen massSq species sign k s * modeVector massSq species sign k (a,true) s := by
  classical
  by_cases ha : a = species s
  · subst a
    have hw : (frequency (massSq (species s)) (k s) : ℂ) ^ 2 =
        (k s : ℂ) ^ 2 + (massSq (species s) : ℂ) := by
      exact_mod_cast frequency_sq (hm (species s)) (k s)
    have hsign : (sign s : ℂ) ^ 2 = 1 := by exact_mod_cast hs s
    simp only [modeVector, Bool.false_eq_true, ↓reduceIte, mul_one,
      spatialEigen, timeEigen, Complex.ofReal_mul]
    calc
      (Complex.I * (k s : ℂ)) ^ 2 - (massSq (species s) : ℂ) =
          -(frequency (massSq (species s)) (k s) : ℂ) ^ 2 := by
            rw [mul_pow, Complex.I_sq, hw]; ring
      _ = (Complex.I * ((sign s : ℂ) * (frequency (massSq (species s)) (k s) : ℂ))) ^ 2 := by
        rw [mul_pow, mul_pow, Complex.I_sq, hsign]; ring
      _ = _ := by ring
  · simp [modeVector, ha]

/-- The symbol of a conserved density satisfies the actual massive phase
relation, for arbitrary real momenta with zero sum. -/
theorem massive_phase_relation (massSq : ι → ℝ) (species : S → ι) (sign k : S → ℝ)
    (hm : ∀ a, 0 < massSq a) (hs : ∀ s, sign s ^ 2 = 1)
    (f : Density ℂ (ι × Bool))
    (hc : Conserved (Free.characteristic (fun a => (massSq a : ℂ))) (integral f))
    (hk : ∑ s, k s = 0) :
    (∑ s, sign s * frequency (massSq (species s)) (k s)) •
      polarized (spatialEigen k) (modeVector massSq species sign k) f = 0 := by
  have hk' : ∑ s, spatialEigen k s = 0 := by
    simp [spatialEigen, ← Finset.mul_sum, ← Complex.ofReal_sum, hk]
  have h := polarized_conservation (fun a => (massSq a : ℂ)) (spatialEigen k)
    (timeEigen massSq species sign k) (modeVector massSq species sign k)
    (modeVector_u massSq species sign k) (modeVector_p massSq species sign k hm hs) f hc hk'
  simp only [timeEigen, ← Finset.mul_sum, ← Complex.ofReal_sum, mul_assoc] at h
  have h' := (mul_eq_zero.mp h).resolve_left Complex.I_ne_zero
  simpa only [Complex.real_smul] using h'

/-- Complete the independent real momenta with their negative sum. The
`none` slot is the last factor in the paper's momentum hyperplane. -/
def onHyperplane {n : ℕ} (k : Fin n → ℝ) : Option (Fin n) → ℝ
  | none => -(∑ j, k j)
  | some j => k j

@[simp] theorem sum_onHyperplane {n : ℕ} (k : Fin n → ℝ) :
    ∑ s, onHyperplane k s = 0 := by simp [Fintype.sum_option, onHyperplane]

theorem continuous_onHyperplane {n : ℕ} (s : Option (Fin n)) :
    Continuous fun k : Fin n → ℝ => onHyperplane k s := by
  cases s with
  | none => exact (continuous_finsetSum _ fun j _ => continuous_apply j).neg
  | some j => exact continuous_apply j

omit [Fintype S] in
theorem continuous_modeVector {T : Type*} [TopologicalSpace T]
    (massSq : ι → ℝ) (species : S → ι) (sign : S → ℝ) (k : T → S → ℝ)
    (hk : ∀ s, Continuous fun x => k x s) (a : ι × Bool) (s : S) :
    Continuous fun x => modeVector massSq species sign (k x) a s := by
  classical
  by_cases ha : a.1 = species s
  · cases hb : a.2
    · simp [modeVector, ha, hb]; exact continuous_const
    · simp only [modeVector, ha, hb, ↓reduceIte, timeEigen]
      apply continuous_const.mul
      apply Complex.continuous_ofReal.comp
      exact continuous_const.mul (Real.continuous_sqrt.comp ((hk s).pow 2 |>.add continuous_const))
  · simp [modeVector, ha]; exact continuous_const

/-- Every normal-mode symbol with at least three slots vanishes on the
momentum hyperplane. Here the symbol is *constructed from the conserved
jet polynomial*, not an independently hypothesized kernel. -/
theorem massive_polarized_eq_zero {n : ℕ}
    (massSq : ι → ℝ) (species : Option (Fin (n+2)) → ι)
    (sign : Option (Fin (n+2)) → ℝ)
    (hm : ∀ a, 0 < massSq a) (hs : ∀ s, sign s ^ 2 = 1)
    (f : Density ℂ (ι × Bool))
    (hc : Conserved (Free.characteristic (fun a => (massSq a : ℂ))) (integral f))
    (k : Fin (n+2) → ℝ) :
    polarized (spatialEigen (onHyperplane k))
      (modeVector massSq species sign (onHyperplane k)) f = 0 := by
  let A := fun k : Fin (n+2) → ℝ => polarized (spatialEigen (onHyperplane k))
    (modeVector massSq species sign (onHyperplane k)) f
  have hA : Continuous A := by
    apply continuous_component
    · intro s
      exact continuous_const.mul (Complex.continuous_ofReal.comp (continuous_onHyperplane s))
    · intro a s
      exact continuous_modeVector massSq species sign onHyperplane continuous_onHyperplane a s
  apply multiPhase_kernel_eq_zero
    (fun j => massSq (species (some j))) (fun j => sign (some j))
    (massSq (species none)) (sign none) (fun j => hm _) (hm _)
    (by intro h; simpa [h] using hs none) A hA ?_ k
  intro k
  have h := massive_phase_relation massSq species sign (onHyperplane k) hm hs f hc
    (sum_onHyperplane k)
  simpa [A, multiPhase, Fintype.sum_option, onHyperplane, add_comm] using h

/-- The same vanishing theorem applies to the original real coefficient
jet algebra, by the proved extension-of-scalars compatibility. -/
theorem real_massive_polarized_eq_zero {n : ℕ}
    (massSq : ι → ℝ) (species : Option (Fin (n+2)) → ι)
    (sign : Option (Fin (n+2)) → ℝ)
    (hm : ∀ a, 0 < massSq a) (hs : ∀ s, sign s ^ 2 = 1)
    (f : Density ℝ (ι × Bool))
    (hc : Conserved (Free.characteristic massSq) (integral f)) (k : Fin (n+2) → ℝ) :
    polarized (spatialEigen (onHyperplane k))
      (modeVector massSq species sign (onHyperplane k)) (MvPolynomial.map Complex.ofRealHom f) = 0 := by
  exact massive_polarized_eq_zero massSq species sign hm hs _
    (map_free_conserved Complex.ofRealHom massSq f hc) k

end Structural.Symbol
