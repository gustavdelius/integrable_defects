module

public import Structural.JetAlgebra
public import Mathlib.Algebra.MvPolynomial.PDeriv
import Mathlib.Tactic.Abel

/-!
# Polynomial Euler derivatives

The Euler operator is constructed from actual partial derivatives of the jet
polynomial. We prove its commutation rules with `Dx` and the telescoping
identity which makes Euler derivatives annihilate spatial divergences.

`euler a N` uses spatial orders `0,...,N`. The explicit endpoint remainder
records exactly the order condition needed to use this finite sum.
-/

@[expose] public section

noncomputable section

namespace Structural.Jet

open MvPolynomial
variable {R α : Type*} [CommRing R]

theorem pderiv_zero_Dx (a : α) (f : Density R α) :
    pderiv (a, 0) (Dx f) = Dx (pderiv (a, 0) f) := by
  classical
  have h : ⁅pderiv (R := R) (a, 0), Dx⁆ =
      (0 : Derivation R (Density R α) (Density R α)) := by
    apply MvPolynomial.derivation_ext
    rintro ⟨b, k⟩
    change pderiv (a, 0) (Dx (z b k)) - Dx (pderiv (a, 0) (z b k)) = 0
    rw [Dx_z]
    simp [z, Pi.single_apply, apply_ite]
  exact sub_eq_zero.mp (congrArg (fun d : Derivation R (Density R α) (Density R α) => d f) h)

theorem pderiv_succ_Dx (a : α) (n : ℕ) (f : Density R α) :
    pderiv (a, n + 1) (Dx f) =
      Dx (pderiv (a, n + 1) f) + pderiv (a, n) f := by
  classical
  have h : ⁅pderiv (R := R) (a, n + 1), Dx⁆ =
      (pderiv (a, n) : Derivation R (Density R α) (Density R α)) := by
    apply MvPolynomial.derivation_ext
    rintro ⟨b, k⟩
    change pderiv (a, n + 1) (Dx (z b k)) - Dx (pderiv (a, n + 1) (z b k)) =
      pderiv (a, n) (z b k)
    rw [Dx_z]
    simp [z, Pi.single_apply, Prod.mk.injEq, apply_ite]
    split_ifs <;> simp_all
  exact sub_eq_iff_eq_add.mp
    (congrArg (fun d : Derivation R (Density R α) (Density R α) => d f) h) |>.trans
      (add_comm _ _)

/-- The finite Euler sum as a linear operator on densities. -/
def euler (a : α) (N : ℕ) : Density R α →ₗ[R] Density R α :=
  ∑ k ∈ Finset.range (N + 1), (-1 : R) ^ k •
    (dxn k).comp (pderiv (a, k)).toLinearMap

@[simp] theorem euler_zero (a : α) (f : Density R α) :
    euler a 0 f = pderiv (a, 0) f := by
  simp [euler]

theorem euler_succ (a : α) (N : ℕ) (f : Density R α) :
    euler a (N + 1) f =
      euler a N f + (-1 : R) ^ (N + 1) • dxn (N + 1) (pderiv (a, N + 1) f) := by
  simp [euler, Finset.sum_range_succ]

/-- The Euler sum of a total derivative telescopes to a single endpoint term. -/
theorem euler_Dx_boundary (a : α) (N : ℕ) (f : Density R α) :
    euler a N (Dx f) = (-1 : R) ^ N • dxn (N + 1) (pderiv (a, N) f) := by
  induction N with
  | zero => simp [pderiv_zero_Dx, dxn_succ]
  | succ N ih =>
    rw [euler_succ, ih, pderiv_succ_Dx, map_add, smul_add,
      ← dxn_succ_right]
    simp only [pow_succ, mul_neg_one, neg_smul]
    abel

/-- If the primitive has no jet of order `N` in component `a`, its total
derivative has zero Euler sum through order `N`. -/
theorem euler_Dx_eq_zero (a : α) (N : ℕ) (f : Density R α)
    (hf : (a, N) ∉ f.vars) : euler a N (Dx f) = 0 := by
  rw [euler_Dx_boundary, pderiv_eq_zero_of_notMem_vars hf, map_zero, smul_zero]

/-- The integration-by-parts step in the scaling homotopy, for any finite
collection of jets. The zeroth field now multiplies the alternating Euler
terms. -/
theorem variational_integration_by_parts (s : Finset (α × ℕ)) (f : Density R α) :
    integral (∑ j ∈ s, z j.1 j.2 * pderiv j f) =
      integral (∑ j ∈ s, z j.1 0 * ((-1 : R) ^ j.2 • dxn j.2 (pderiv j f))) := by
  classical
  simp only [map_sum]
  apply Finset.sum_congr rfl
  intro j _
  have h := integration_by_parts_iterated j.2 (pderiv j f) (z j.1 0 : Density R α)
  simpa [dxn_z, mul_comm, mul_smul_comm, map_smul] using h

end Structural.Jet
