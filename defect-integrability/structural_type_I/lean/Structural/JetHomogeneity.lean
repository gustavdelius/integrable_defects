module

public import Structural.PolynomialHomotopy

/-! # The amplitude grading of spatial and Euler derivatives -/

@[expose] public section
noncomputable section
namespace Structural.Jet
open MvPolynomial
variable {R α : Type*} [CommRing R]

/-- Spatial differentiation preserves amplitude degree. -/
theorem homogeneous_Dx (f : Density R α) (n : ℕ) (hf : f.IsHomogeneous n) :
    (Dx f).IsHomogeneous n := by
  cases n with
  | zero =>
    rw [← totalDegree_zero_iff_isHomogeneous, totalDegree_eq_zero_iff_eq_C] at hf
    rw [hf, Dx_C]
    apply isHomogeneous_zero
  | succ n =>
    rw [derivation_eq_sum (Dx (R := R) (α := α)) f f.vars (Finset.Subset.refl _)]
    apply IsHomogeneous.sum
    intro j hj
    rw [Dx_z]
    simpa [z, Nat.add_comm] using (isHomogeneous_X R (j.1, j.2+1)).mul hf.pderiv

theorem homogeneous_dxn (f : Density R α) (n r : ℕ) (hf : f.IsHomogeneous n) :
    (dxn r f).IsHomogeneous n := by
  induction r with
  | zero => exact hf
  | succ r ih => rw [dxn_succ]; exact homogeneous_Dx _ n ih

/-- The finite Euler operator lowers amplitude degree by one. -/
theorem homogeneous_euler (f : Density R α) (n N : ℕ) (a : α) (hf : f.IsHomogeneous n) :
    (euler a N f).IsHomogeneous (n-1) := by
  simp only [euler, LinearMap.sum_apply, LinearMap.smul_apply, LinearMap.comp_apply,
    Derivation.coeFn_coe]
  apply IsHomogeneous.sum
  intro r hr
  rw [smul_eq_C_mul]
  exact (homogeneous_dxn _ _ r hf.pderiv).C_mul _

/-- A linear characteristic preserves amplitude degree under prolongation. -/
theorem homogeneous_evolution (Q : α → Density R α)
    (hQ : ∀ a, (Q a).IsHomogeneous 1) (f : Density R α) (n : ℕ) (hf : f.IsHomogeneous n) :
    (evolution Q f).IsHomogeneous n := by
  cases n with
  | zero =>
    rw [← totalDegree_zero_iff_isHomogeneous, totalDegree_eq_zero_iff_eq_C] at hf
    rw [hf]
    simp only [MvPolynomial.derivation_C]
    apply isHomogeneous_zero
  | succ n =>
    rw [derivation_eq_sum (evolution Q) f f.vars (Finset.Subset.refl _)]
    apply IsHomogeneous.sum
    intro j hj
    rw [evolution_z]
    simpa [Nat.add_comm] using (homogeneous_dxn (Q j.1) 1 j.2 (hQ j.1)).mul hf.pderiv

/-- Homogeneous characteristics give the expected amplitude degree after
one derivative with respect to a Cauchy jet. -/
theorem homogeneous_evolution_weight (Q : α → Density R α) (d : ℕ)
    (hQ : ∀ a, (Q a).IsHomogeneous d) (f : Density R α) (n : ℕ) (hf : f.IsHomogeneous n) :
    (evolution Q f).IsHomogeneous (d + (n-1)) := by
  cases n with
  | zero =>
    rw [← totalDegree_zero_iff_isHomogeneous, totalDegree_eq_zero_iff_eq_C] at hf
    rw [hf]
    simp only [MvPolynomial.derivation_C]
    apply isHomogeneous_zero
  | succ n =>
    rw [derivation_eq_sum (evolution Q) f f.vars (Finset.Subset.refl _)]
    apply IsHomogeneous.sum
    intro j hj
    rw [evolution_z]
    exact (homogeneous_dxn (Q j.1) d j.2 (hQ j.1)).mul hf.pderiv

/-- Any linear operator preserving each amplitude degree commutes with
projection to homogeneous components. -/
theorem homogeneousComponent_commutes (D : Density R α →ₗ[R] Density R α)
    (hD : ∀ n f, f.IsHomogeneous n → (D f).IsHomogeneous n)
    (n : ℕ) (f : Density R α) :
    homogeneousComponent n (D f) = D (homogeneousComponent n f) := by
  classical
  induction f using MvPolynomial.induction_on' with
  | monomial d r =>
    have hf : (monomial d r : Density R α).IsHomogeneous d.degree := isHomogeneous_monomial r rfl
    rw [homogeneousComponent_of_mem (hD _ _ hf), homogeneousComponent_of_mem hf]
    split_ifs <;> simp
  | add f g hf hg => simp only [map_add, hf, hg]

theorem homogeneousComponent_Dx (n : ℕ) (f : Density R α) :
    homogeneousComponent n (Dx f) = Dx (homogeneousComponent n f) :=
  homogeneousComponent_commutes Dx.toLinearMap (fun n f => homogeneous_Dx f n) n f

theorem homogeneousComponent_evolution (Q : α → Density R α)
    (hQ : ∀ a, (Q a).IsHomogeneous 1) (n : ℕ) (f : Density R α) :
    homogeneousComponent n (evolution Q f) = evolution Q (homogeneousComponent n f) :=
  homogeneousComponent_commutes (evolution Q).toLinearMap
    (fun n f => homogeneous_evolution Q hQ f n) n f

/-- Under a linear evolution every homogeneous part of a conserved density
is separately conserved, with the corresponding part of its flux. -/
theorem conserved_homogeneousComponent (Q : α → Density R α)
    (hQ : ∀ a, (Q a).IsHomogeneous 1) (n : ℕ) (f : Density R α)
    (hc : Conserved Q (integral f)) : Conserved Q (integral (homogeneousComponent n f)) := by
  obtain ⟨flux, hflux⟩ := (conserved_iff Q f).mp hc
  apply (conserved_iff Q _).mpr
  refine ⟨homogeneousComponent n flux, ?_⟩
  rw [← homogeneousComponent_evolution Q hQ, hflux, homogeneousComponent_Dx]

end Structural.Jet
