import Std

/-
  Checked algebraic components of theorem_D_reconstruction/proof.md.
  This file does NOT claim to formalize infinite-dimensional phase spaces,
  Bianchi permutability, or the complete scalar integrability theorem.
  Derivations act on a generic commutative ring, never on Int alone.
-/
open Lean.Grind
namespace DefectCore

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
end Deriv

/-- A derivation is injective only in a zero ring: never assume global dt injectivity. -/
theorem global_kernel_obstruction {R : Type} [CommRing R] (D : Deriv R)
    (h : ∀ a, D a = 0 → a = 0) : (1 : R) = 0 := h 1 D.map_one

/-- First-order Noether identities, from chain rules and actual derivations. -/
theorem noether_first_order {R : Type} [CommRing R]
    (dt dx : Deriv R) (comm : ∀ a, dt (dx a) = dx (dt a))
    (u L Lu Lt Lx : R)
    (chain_t : dt L = Lu * dt u + Lt * dt (dt u) + Lx * dt (dx u))
    (chain_x : dx L = Lu * dx u + Lt * dx (dt u) + Lx * dx (dx u)) :
    dt (Lt * dt u - L) + dx (Lx * dt u) =
      -(Lu - dt Lt - dx Lx) * dt u ∧
    dt (-(Lt * dx u)) + dx (L - Lx * dx u) =
      (Lu - dt Lt - dx Lx) * dx u := by
  constructor
  · rw [dt.map_sub, dt.map_mul, dx.map_mul, chain_t, comm u]
    grind
  · rw [dt.map_neg, dt.map_mul, dx.map_sub, dx.map_mul, chain_x, comm u]
    grind

/-- Actual second-order spatial integration by parts, with no Noether identity assumed. -/
theorem ostrogradsky_K2 {R : Type} [CommRing R]
    (dx : Deriv R) (F0 F1 F2 eta : R) :
    F0 * eta + F1 * dx eta + F2 * dx (dx eta) =
      (F0 - dx F1 + dx (dx F2)) * eta +
      dx ((F1 - dx F2) * eta + F2 * dx eta) := by
  rw [dx.map_add, dx.map_mul, dx.map_mul, dx.map_sub]
  grind

/-- The x-translation Noether current in the representative obtained by x-last IBP.
    Its spatial component is the Legendre density, derived from the chain rule. -/
theorem noether_spatial_K2 {R : Type} [CommRing R]
    (dt dx : Deriv R) (u L F0 F1 F2 Xi : R)
    (chain_x : dx L = F0 * dx u + F1 * dx (dx u) +
      F2 * dx (dx (dx u)) + dt Xi) :
    dx ((F1 - dx F2) * dx u + F2 * dx (dx u) - L) + dt Xi =
      -(F0 - dx F1 + dx (dx F2)) * dx u := by
  have h := ostrogradsky_K2 dx F0 F1 F2 (dx u)
  rw [dx.map_sub, chain_x]
  grind

/-- Normalization is a property of a residual, not injectivity on the whole ring. -/
theorem stress_potential_from_normalized_residual {R : Type} [CommRing R]
    (dt dx : Deriv R) (comm : ∀ a, dt (dx a) = dx (dt a))
    (E P e p f s : R) (normalized : R → Prop)
    (kernel : ∀ a, normalized a → dt a = 0 → a = 0)
    (normE : normalized (dx E + e)) (normP : normalized (dx P + p))
    (balanceE : dt E = f) (balanceP : dt P = s)
    (bulkE : dt e + dx f = 0) (bulkP : dt p + dx s = 0) :
    dx E = -e ∧ dx P = -p := by
  have hE : dt (dx E + e) = 0 := by
    rw [dt.map_add, comm E, balanceE]
    grind
  have hP : dt (dx P + p) = 0 := by
    rw [dt.map_add, comm P, balanceP]
    grind
  have kE := kernel _ normE hE
  have kP := kernel _ normP hP
  constructor <;> grind

/-- Exact scalar defect-current identity. Bu and Bv are partial derivatives;
    Pu=-Bv and Pv=-Bu follow from the momentum constraint in the written proof. -/
theorem scalar_defect_current {R : Type} [CommRing R]
    (ut vt Bu Bv : R) :
    Bu * ut + Bv * vt + (-Bv) * (vt - Bu) + (-Bu) * (ut + Bv) = 0 := by
  grind

/-- Doubled free-scalar density and flux; their actual derivatives, on any differential ring. -/
theorem free_scalar_current {R : Type} [CommRing R]
    (dt dx : Deriv R) (comm : ∀ a, dt (dx a) = dx (dt a))
    (u m2 : R) (mt : dt m2 = 0) (mx : dx m2 = 0) :
    dt ((dx u - dt u) * (dx u - dt u) + m2 * (u * u)) +
    dx ((dx u - dt u) * (dx u - dt u) - m2 * (u * u)) =
      2 * (dt u - dx u) * (dt (dt u) - dx (dx u) + m2 * u) := by
  simp only [dt.map_add, dt.map_sub, dt.map_mul, dx.map_sub, dx.map_mul, mt, mx,
    comm u]
  grind

/-- Real and imaginary parts of the NLS number current, with arbitrary real
    nonlinear coefficient N. The current has the positive coefficient 2. -/
theorem nls_number_current {R : Type} [CommRing R]
    (dt dx : Deriv R) (a b N : R)
    (eqA : dt a = -(dx (dx b)) - N * b)
    (eqB : dt b = dx (dx a) + N * a) :
    dt (a * a + b * b) + dx (2 * (a * dx b - b * dx a)) = 0 := by
  have h2 : dx (2 : R) = 0 := by
    have he : (2 : R) = 1 + 1 := by grind
    rw [he, dx.map_add, dx.map_one]
    grind
  simp only [dt.map_add, dt.map_mul, dx.map_mul, dx.map_sub, h2, eqA, eqB]
  grind

end DefectCore
