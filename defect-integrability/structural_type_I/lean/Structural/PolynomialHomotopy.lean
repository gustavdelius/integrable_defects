module

public import Structural.Variational
public import Mathlib.RingTheory.MvPolynomial.EulerIdentity
public import Mathlib.Basic.Real.Basic
import Mathlib.Algebra.CharZero.Infinite
import Mathlib.Algebra.BigOperators.Group.Finset.Sigma
import Mathlib.Algebra.Module.NatInt

/-!
# The homogeneous polynomial scaling homotopy

This file extends the finite-variable Euler identity to the infinite jet
algebra, where each individual polynomial still has finite support. Combining
it with integration by parts gives the homogeneous scaling homotopy.
-/

@[expose] public section

noncomputable section

namespace Structural.Jet

open MvPolynomial
variable {R α : Type*} [CommRing R]

/-- Chain rule on a finite collection containing every variable of `f`. -/
theorem derivation_eq_sum (d : Derivation R (Density R α) (Density R α))
    (f : Density R α) (s : Finset (α × ℕ)) (hs : f.vars ⊆ s) :
    d f = ∑ j ∈ s, d (z j.1 j.2) * pderiv j f := by
  classical
  let e : Derivation R (Density R α) (Density R α) :=
    ∑ j ∈ s, d (z j.1 j.2) • pderiv j
  have h : d f = e f := by
    apply MvPolynomial.derivation_eq_of_forall_mem_vars
    intro j hj
    simp [e, Pi.single_apply, hs hj, z, smul_eq_mul]
  simpa [e, smul_eq_mul] using h

/-- Amplitude scaling gives weight one to every jet, irrespective of its
spatial order. This grading differs from differential order. -/
def amplitude : Derivation R (Density R α) (Density R α) :=
  MvPolynomial.mkDerivation R MvPolynomial.X

@[simp] theorem amplitude_z (a : α) (n : ℕ) :
    amplitude (z a n : Density R α) = z a n := by simp [amplitude, z]

theorem amplitude_monomial (d : (α × ℕ) →₀ ℕ) (r : R) :
    amplitude (monomial d r) = d.degree • monomial d r := by
  classical
  by_cases hr : r = 0
  · simp [hr]
  rw [derivation_eq_sum amplitude (monomial d r) d.support (by
    rw [vars_monomial hr])]
  simp only [z, amplitude, mkDerivation_X, Prod.mk.eta,
    X_mul_pderiv_monomial, ← Finset.sum_smul]
  rfl

theorem amplitude_homogeneous (f : Density R α) (n : ℕ) (hf : f.IsHomogeneous n) :
    amplitude f = n • f := by
  rw [← mem_homogeneousSubmodule, homogeneousSubmodule_eq_finsupp_supported,
    AddMonoidAlgebra.supported_eq_span_single] at hf
  induction hf using Submodule.span_induction with
  | mem f h =>
    obtain ⟨d, hd, rfl⟩ := h
    have hd' : d.degree = n := hd
    simpa [single_eq_monomial, hd'] using (amplitude_monomial (R := R) d 1)
  | zero => simp
  | add f g _ _ hf hg => simp [hf, hg, smul_add]
  | smul r f _ hf => simp [Derivation.map_smul, hf, smul_comm]

/-- Euler's amplitude identity for a density with an arbitrary finite jet
support; the global jet-variable type need not be finite. -/
theorem sum_jets_pderiv (f : Density R α) (n : ℕ) (hf : f.IsHomogeneous n)
    (s : Finset (α × ℕ)) (hs : f.vars ⊆ s) :
    (∑ j ∈ s, z j.1 j.2 * pderiv j f) = n • f := by
  rw [← amplitude_homogeneous f n hf, derivation_eq_sum amplitude f s hs]
  simp

/-- Homogeneous scaling followed by integration by parts. -/
theorem homogeneous_scaling_homotopy (f : Density R α) (n : ℕ)
    (hf : f.IsHomogeneous n) (s : Finset (α × ℕ)) (hs : f.vars ⊆ s) :
    n • integral f =
      integral (∑ j ∈ s, z j.1 0 * ((-1 : R) ^ j.2 • dxn j.2 (pderiv j f))) := by
  rw [← map_nsmul, ← sum_jets_pderiv f n hf s hs]
  exact variational_integration_by_parts s f

theorem homogeneous_euler_homotopy [Fintype α] (f : Density R α) (n N : ℕ)
    (hf : f.IsHomogeneous n) (hN : order f ≤ N) :
    n • integral f = integral (∑ a, z a 0 * euler a N f) := by
  classical
  have hs : f.vars ⊆ Finset.univ.product (Finset.range (N + 1)) := by
    intro j hj
    exact Finset.mem_product.mpr ⟨Finset.mem_univ _, Finset.mem_range.mpr
      (Nat.lt_succ_of_le ((le_order_of_mem_vars f j hj).trans hN))⟩
  rw [homogeneous_scaling_homotopy f n hf _ hs]
  congr 1
  simp [euler, Finset.sum_product, Finset.mul_sum]

/-- The polynomial version of the scaling argument used at the end of Lemma
6.2: a positive-degree homogeneous density with zero Euler derivatives is
an actual total spatial derivative. -/
theorem homogeneous_is_divergence_of_euler_zero [Fintype α]
    (f : Density ℝ α) (n N : ℕ) (hn : n ≠ 0) (hf : f.IsHomogeneous n)
    (hN : order f ≤ N) (he : ∀ a, euler a N f = 0) :
    ∃ g, Dx g = f := by
  apply (integral_eq_zero_iff f).1
  have h := homogeneous_euler_homotopy f n N hf hN
  simp only [he, mul_zero, Finset.sum_const_zero, map_zero] at h
  have hreal : (n : ℝ) • integral f = 0 := by
    rw [Nat.cast_smul_eq_nsmul]
    exact h
  exact (smul_eq_zero.mp hreal).resolve_left (Nat.cast_ne_zero.mpr hn)

end Structural.Jet
