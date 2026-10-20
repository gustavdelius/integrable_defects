module

public import Structural.ConstantJet
public import Mathlib.RingTheory.MvPolynomial.Homogeneous

/-!
# The degree-one part of free massive rigidity

The Boolean component distinguishes `u` (`false`) from its momentum `p` (`true`).
`massSq a` is the squared mass, and the constructed time evolution is
`u_t = p`, `p_t = u_xx - massSq * u`.

Every homogeneous degree-one polynomial density conserved modulo spatial
derivatives is itself a spatial derivative when each squared mass is nonzero.
This is the full degree-one assertion of Lemma 6.1, in the concrete polynomial
jet model. `FreeRigidity` proves the degree-three-and-higher assertion for
finitely many species with positive squared masses.
-/

@[expose] public section

noncomputable section

namespace Structural.Free

open Jet

variable {R ι : Type*} [Field R]

/-- Free Klein–Gordon characteristic for diagonal squared masses. -/
def characteristic (massSq : ι → R) : (ι × Bool) → Density R (ι × Bool)
  | (a, false) => z (a, true) 0
  | (a, true) => z (a, false) 2 - massSq a • z (a, false) 0

/-- Inverse of the zero-spatial-momentum oscillator matrix.
Its prolonged action inverts free evolution on degree-one local functionals. -/
def inverseCharacteristic (massSq : ι → R) : (ι × Bool) → Density R (ι × Bool)
  | (a, false) => -(massSq a)⁻¹ • z (a, true) 0
  | (a, true) => z (a, false) 0

theorem inverse_evolution_integral_z (massSq : ι → R)
    (hm : ∀ a, massSq a ≠ 0) (a : ι) (b : Bool) (n : ℕ) :
    localEvolution (inverseCharacteristic massSq)
        (localEvolution (characteristic massSq) (integral (z (a, b) n))) =
      integral (z (a, b) n) := by
  cases n with
  | succ n => simp
  | zero =>
    cases b with
    | false =>
      simp [characteristic, inverseCharacteristic]
    | true =>
      simp [characteristic, inverseCharacteristic, map_sub, map_smul,
        dxn_z, smul_smul, hm]

/-- An explicit left inverse on the entire homogeneous degree-one subspace,
proved by the spanning property of the actual jet generators. -/
theorem inverse_evolution_linear (massSq : ι → R) (hm : ∀ a, massSq a ≠ 0)
    (f : Density R (ι × Bool)) (hf : f.IsHomogeneous 1) :
    localEvolution (inverseCharacteristic massSq)
        (localEvolution (characteristic massSq) (integral f)) = integral f := by
  have hmem : f ∈ Submodule.span R (Set.range MvPolynomial.X) := by
    rw [← MvPolynomial.homogeneousSubmodule_one_eq_span_X]
    exact hf
  clear hf
  induction hmem using Submodule.span_induction with
  | mem f h =>
    obtain ⟨⟨⟨a, b⟩, n⟩, rfl⟩ := h
    exact inverse_evolution_integral_z massSq hm a b n
  | zero => simp
  | add f g _ _ hf hg => simp only [map_add, hf, hg]
  | smul c f _ hf => simp only [map_smul, hf]

/-- No nonzero linear local conserved functional exists for nonzero masses. -/
theorem linear_conserved_eq_zero (massSq : ι → R) (hm : ∀ a, massSq a ≠ 0)
    (f : Density R (ι × Bool)) (hf : f.IsHomogeneous 1)
    (hc : Conserved (characteristic massSq) (integral f)) :
    integral f = 0 := by
  rw [← inverse_evolution_linear massSq hm f hf, hc, map_zero]

/-- Equivalently, the conserved density is an actual total spatial derivative. -/
theorem linear_conserved_is_divergence (massSq : ι → R) (hm : ∀ a, massSq a ≠ 0)
    (f : Density R (ι × Bool)) (hf : f.IsHomogeneous 1)
    (hc : Conserved (characteristic massSq) (integral f)) :
    ∃ g, Dx g = f :=
  (integral_eq_zero_iff f).1 (linear_conserved_eq_zero massSq hm f hf hc)

end Structural.Free
