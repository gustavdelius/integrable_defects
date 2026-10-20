module

public import Structural.PolarizationMultilinear
public import Structural.JetHomogeneity
public import Structural.NormalModes

/-!
# Euler derivatives from the distinguished wave slot

Removing the last amplitude variable turns coefficient polarization into a
sum of directional derivatives. On zero total momentum, its spatial powers
become the alternating total derivatives in the Euler operator.
-/

@[expose] public section
noncomputable section
namespace Structural.Symbol
open MvPolynomial Jet
variable {R α S : Type*} [CommRing R] [Fintype S]

/-- After setting the distinguished amplitude to zero, the remaining
substitution is just a renaming of the other amplitude variables. -/
theorem substitution_without_none [DecidableEq S] (v : Option S → α → R) (f : MvPolynomial α R) :
    vectorSubstitution (Function.update v none 0) f =
      rename Option.some (vectorSubstitution (fun s => v (some s)) f) := by
  classical
  have h : vectorSubstitution (Function.update v none 0) =
      (rename Option.some).comp (vectorSubstitution (fun s => v (some s))) := by
    apply MvPolynomial.algHom_ext
    intro a
    simp [vectorSubstitution, Fintype.sum_option]
  exact congrArg (fun g : MvPolynomial α R →ₐ[R] MvPolynomial (Option S) R => g f) h

theorem multilinearDegree_erase_none :
    (multilinearDegree : Option S →₀ ℕ).erase none =
      (multilinearDegree : S →₀ ℕ).mapDomain Option.some := by
  classical
  ext s
  cases s with
  | none => simp [Finsupp.mapDomain_of_notMem_range]
  | some s => simp [Finsupp.mapDomain_apply_of_injective (Option.some_injective S)]

/-- Recursive coefficient polarization, with no normalization factors. -/
theorem polarization_option_formula (f : MvPolynomial α R) (v : Option S → α → R) :
    polarization f v = ∑ a ∈ f.vars, v none a *
      polarization (pderiv a f) (fun s => v (some s)) := by
  classical
  rw [polarization_slot_formula f v none]
  apply Finset.sum_congr rfl
  intro a ha
  rw [substitution_without_none, multilinearDegree_erase_none,
    coeff_rename_mapDomain _ (Option.some_injective S)]
  rfl

/-- Applied to wave jets, the distinguished slot contributes its field
amplitude times its spatial eigenvalue to the corresponding power. -/
theorem polarized_option_formula (f : Density R α)
    (k : Option S → R) (v : α → Option S → R) :
    polarized k v f = ∑ j ∈ f.vars, (v j.1 none * k none ^ j.2) *
      polarized (fun s => k (some s)) (fun a s => v a (some s)) (pderiv j f) := by
  simp only [polarized_eq_polarization]
  exact polarization_option_formula f (fun s j => v j.1 s * k s ^ j.2)

/-- The symbol depends linearly on the density. -/
def polarizedLinear (k : S → R) (v : α → S → R) : Density R α →ₗ[R] R where
  toFun := polarized k v
  map_add' f g := by simp [polarized, component]
  map_smul' c f := by simp [polarized, component]

@[simp] theorem polarizedLinear_apply (k : S → R) (v : α → S → R) (f : Density R α) :
    polarizedLinear k v f = polarized k v f := rfl

theorem polarized_dxn (k : S → R) (v : α → S → R) (r : ℕ) (f : Density R α) :
    polarized k v (dxn r f) = (∑ s, k s)^r * polarized k v f := by
  induction r with
  | zero => simp
  | succ r ih => rw [dxn_succ, polarized_Dx, ih, pow_succ', mul_assoc]

/-- The Euler operator becomes a finite sum of powers of negative total
momentum multiplying the partial-derivative symbols. -/
theorem polarized_euler (k : S → R) (v : α → S → R) (a : α) (N : ℕ) (f : Density R α) :
    polarized k v (euler a N f) = ∑ r ∈ Finset.range (N+1),
      (-(∑ s, k s))^r * polarized k v (pderiv (a,r) f) := by
  change polarizedLinear k v (euler a N f) = _
  simp only [euler, LinearMap.sum_apply, LinearMap.smul_apply, LinearMap.comp_apply,
    map_sum, map_smul, polarizedLinear_apply, Derivation.coeFn_coe, polarized_dxn, smul_eq_mul]
  apply Finset.sum_congr rfl
  intro r hr
  rw [← mul_assoc, ← mul_pow, neg_one_mul]

/-- On zero total momentum, the distinguished slot evaluates precisely the
Euler derivatives of the density. The finite order bound is explicit. -/
theorem polarized_none_euler [Fintype α] (f : Density R α) (N : ℕ)
    (hN : order f ≤ N) (k : S → R) (v : α → S → R) (w : α → R) :
    polarized (fun s : Option S => s.elim (-(∑ j, k j)) k)
      (fun a s => s.elim (w a) (v a)) f =
      ∑ a, w a * polarized k v (euler a N f) := by
  classical
  rw [polarized_option_formula]
  simp only [Option.elim_none, Option.elim_some]
  have hsub : f.vars ⊆ Finset.univ.product (Finset.range (N+1)) := by
    intro j hj
    exact Finset.mem_product.mpr ⟨Finset.mem_univ _, Finset.mem_range.mpr
      (Nat.lt_succ_of_le ((le_order_of_mem_vars f j hj).trans hN))⟩
  calc
    _ = ∑ j ∈ Finset.univ.product (Finset.range (N+1)),
        (w j.1 * (-(∑ s, k s))^j.2) * polarized k v (pderiv j f) := by
      apply Finset.sum_subset hsub
      intro j hj hnot
      rw [pderiv_eq_zero_of_notMem_vars hnot]
      simp [polarized, component]
    _ = _ := by
      simp [Finset.sum_product, polarized_euler, Finset.mul_sum, mul_assoc]

/-- The last Fourier eigenvalue is the negative sum of the others. -/
theorem spatialEigen_onHyperplane {n : ℕ} (k : Fin n → ℝ) :
    spatialEigen (onHyperplane k) =
      (fun s : Option (Fin n) => s.elim (-(∑ j, spatialEigen k j)) (spatialEigen k)) := by
  funext s
  cases s <;> simp [spatialEigen, onHyperplane, ← Finset.mul_sum, ← Complex.ofReal_sum]

/-- Conservation forces every wave polarization of an Euler derivative to
vanish. The remaining wave momenta are completely unconstrained. -/
theorem massive_euler_symbol_eq_zero {ι : Type*} [Fintype ι] {n : ℕ}
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (f : Density ℂ (ι × Bool))
    (hc : Conserved (Free.characteristic (fun a => (massSq a : ℂ))) (integral f))
    (N : ℕ) (hN : order f ≤ N) (a : ι × Bool)
    (k : Fin (n+2) → ℝ) (v : (ι × Bool) → Fin (n+2) → ℂ) :
    polarized (spatialEigen k) v (euler a N f) = 0 := by
  classical
  let w : (ι × Bool) → ℂ := Pi.single a 1
  have h := massive_arbitrary_vectors_eq_zero massSq hm f hc k
    (fun s c => s.elim (w c) (v c))
  rw [spatialEigen_onHyperplane, polarized_none_euler f N hN] at h
  simpa [w, Pi.single_apply] using h

end Structural.Symbol
