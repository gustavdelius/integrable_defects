module

public import Structural.Variational
public import Structural.FormalRigidity

/-!
# Euler derivatives of zero local-functional classes

The Euler cutoff can be any bound on the density's own spatial order.
No bound on an unknown spatial primitive is needed: increase the cutoff
temporarily, use the telescoping identity, then lower it again.
This is the polynomial input to analytic Euler uniqueness.
-/

@[expose] public section
noncomputable section
namespace Structural.Jet
open MvPolynomial
variable {R α : Type*} [CommRing R]

/-- Above the density's spatial order every jet partial derivative is zero. -/
theorem pderiv_eq_zero_of_order_lt (f : Density R α) (a : α) (k : ℕ)
    (hk : order f < k) : pderiv (a,k) f = 0 := by
  apply pderiv_eq_zero_of_notMem_vars
  intro h
  exact (not_le_of_gt hk) (le_order_of_mem_vars f (a,k) h)

/-- Increasing the Euler cutoff past the density's order changes nothing. -/
theorem euler_stable (f : Density R α) (a : α) (N M : ℕ)
    (hN : order f ≤ N) (hNM : N ≤ M) : euler a M f = euler a N f := by
  classical
  simp only [euler, LinearMap.sum_apply, LinearMap.smul_apply, LinearMap.comp_apply,
    Derivation.coeFn_coe]
  symm
  apply Finset.sum_subset (Finset.range_mono (Nat.add_le_add_right hNM 1))
  intro k _ hk
  have hNk : N < k := by
    simp only [Finset.mem_range] at hk
    omega
  rw [pderiv_eq_zero_of_order_lt f a k (lt_of_le_of_lt hN hNk), map_zero, smul_zero]

/-- Any two cutoffs bounding the density's order give the same Euler derivative. -/
theorem euler_cutoff_eq (f : Density R α) (a : α) (N M : ℕ)
    (hN : order f ≤ N) (hM : order f ≤ M) : euler a N f = euler a M f := by
  exact (euler_stable f a N (max N M) hN (le_max_left _ _)).symm.trans
    (euler_stable f a M (max N M) hM (le_max_right _ _))

/-- Euler differentiation annihilates every zero quotient class. Only the
density's order is bounded; its spatial primitive may have any finite order. -/
theorem euler_eq_zero_of_integral_eq_zero (f : Density R α) (a : α) (N : ℕ)
    (hN : order f ≤ N) (hf : integral f = 0) : euler a N f = 0 := by
  obtain ⟨g, hg⟩ := (integral_eq_zero_iff f).mp hf
  let M := max N (order g + 1)
  rw [← euler_stable f a N M hN (le_max_left _ _), ← hg]
  apply euler_Dx_eq_zero
  intro h
  have hm := le_order_of_mem_vars g (a,M) h
  have hM : order g + 1 ≤ M := le_max_right _ _
  omega

end Structural.Jet

namespace Structural.Formal
open Jet

/-- Formal nonlinear rigidity kills the Euler derivative of each coefficient,
at any cutoff bounding that coefficient's density order. -/
theorem conserved_euler_eq_zero {ι : Type*} [Fintype ι]
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (Q : CharacteristicSeries (ι × Bool))
    (hlinear : Q.coeff 0 = Free.characteristic massSq)
    (F : AmplitudeSeries (ι × Bool)) (hc : Conserved Q F)
    (hzero : integral (F.coeff 0) = 0) (hquadratic : integral (F.coeff 2) = 0)
    (n N : ℕ) (hN : order (F.coeff n) ≤ N) (a : ι × Bool) :
    euler a N (F.coeff n) = 0 :=
  euler_eq_zero_of_integral_eq_zero _ a N hN
    (conserved_eq_zero massSq hm Q hlinear F hc hzero hquadratic n)

end Structural.Formal
