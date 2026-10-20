/-
  Basic differential-ring setting for the general-framework formalisation.

  Derivations act on an arbitrary commutative ring `R` (`Lean.Grind.CommRing`),
  never on `Int` alone: on `Int` every derivation is zero (lean_referee/report2.md, §1).
  No statement in this project assumes that a derivation is globally injective.
-/
open Lean.Grind

namespace GeneralFramework

/-- An additive map satisfying the Leibniz rule. -/
structure Deriv (R : Type) [CommRing R] where
  apply : R → R
  map_add : ∀ a b, apply (a + b) = apply a + apply b
  map_mul : ∀ a b, apply (a * b) = apply a * b + a * apply b

instance {R : Type} [CommRing R] : CoeFun (Deriv R) (fun _ => R → R) := ⟨Deriv.apply⟩

namespace Deriv
variable {R : Type} [CommRing R] (D : Deriv R)

theorem map_zero : D 0 = 0 := by
  have h := D.map_add 0 0
  have hz : (0 : R) + 0 = 0 := by grind
  rw [hz] at h
  grind

theorem map_neg (a : R) : D (-a) = -D a := by
  have h := D.map_add (-a) a
  have hz : -a + a = 0 := by grind
  rw [hz, D.map_zero] at h
  grind

theorem map_sub (a b : R) : D (a - b) = D a - D b := by
  have heq : a - b = a + -b := by grind
  rw [heq, D.map_add, D.map_neg]
  grind

theorem map_one : D 1 = 0 := by
  have h := D.map_mul 1 1
  have ho : (1 : R) * 1 = 1 := by grind
  rw [ho] at h
  grind

/-- A derivation is never injective on a nonzero ring, since it kills 1. -/
theorem not_injective_of_nontrivial (h : ∀ a, D a = 0 → a = 0) : (1 : R) = 0 :=
  h 1 D.map_one

end Deriv

/-- Two commuting derivations, the total derivatives `D_t` and `D_x`. -/
structure SpaceTime (R : Type) [CommRing R] where
  Dt : Deriv R
  Dx : Deriv R
  comm : ∀ a, Dt (Dx a) = Dx (Dt a)

end GeneralFramework
