module

public import Structural.Polarization
public import Mathlib.LinearAlgebra.Multilinear.Basic

/-! # Multilinearity of coefficient polarization -/

@[expose] public section
noncomputable section
namespace Structural.Symbol
open MvPolynomial
variable {R α S : Type*} [CommRing R]

/-- Set one polynomial variable to zero. -/
def zeroSlot (s : S) : MvPolynomial S R →ₐ[R] MvPolynomial S R := by
  classical
  exact aeval fun j => if j = s then 0 else X j

theorem zeroSlot_monomial (s : S) (e : S →₀ ℕ) (r : R) :
    zeroSlot s (monomial e r) = if e s = 0 then monomial e r else 0 := by
  classical
  simp only [zeroSlot, aeval_monomial, algebraMap_eq, Finsupp.prod]
  split_ifs with he
  · rw [monomial_eq, Finsupp.prod]
    congr 1
    apply Finset.prod_congr rfl
    intro j hj
    have hjs : j ≠ s := by intro h; subst j; simp [he] at hj
    simp [hjs]
  · have hs : s ∈ e.support := Finsupp.mem_support_iff.mpr he
    have hz : (∏ j ∈ e.support, (if j = s then (0 : MvPolynomial S R) else X j) ^ e j) = 0 := by
      apply Finset.prod_eq_zero hs
      simp [zero_pow he]
    rw [hz, mul_zero]

/-- Killing a variable preserves every coefficient with exponent zero in it. -/
theorem coeff_zeroSlot (s : S) (d : S →₀ ℕ) (hd : d s = 0) (P : MvPolynomial S R) :
    (zeroSlot s P).coeff d = P.coeff d := by
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial e r =>
    rw [zeroSlot_monomial]
    split_ifs with he
    · rfl
    · have hed : e ≠ d := by intro h; subst e; exact he hd
      simp [coeff_monomial, hed]
  | add P Q hP hQ => simp [hP, hQ]

variable [Fintype S] [DecidableEq S]

/-- The algebra substitution underlying coefficient polarization. -/
def vectorSubstitution (v : S → α → R) : MvPolynomial α R →ₐ[R] MvPolynomial S R :=
  aeval fun a => ∑ s, C (v s a) * X s

omit [DecidableEq S] in
@[simp] theorem vectorSubstitution_X (v : S → α → R) (a : α) :
    vectorSubstitution v (X a) = ∑ s, C (v s a) * X s := by simp [vectorSubstitution]

theorem zeroSlot_substitution (v : S → α → R) (s : S) (f : MvPolynomial α R) :
    zeroSlot s (vectorSubstitution v f) = vectorSubstitution (Function.update v s 0) f := by
  classical
  have h : (zeroSlot s).comp (vectorSubstitution v) =
      vectorSubstitution (Function.update v s 0) := by
    apply MvPolynomial.algHom_ext
    intro a
    simp only [AlgHom.comp_apply, vectorSubstitution_X, map_sum, map_mul, algHom_C]
    apply Finset.sum_congr rfl
    intro j hj
    by_cases hjs : j = s
    · subst j; simp [zeroSlot]
    · simp [zeroSlot, hjs]
  exact congrArg (fun g : MvPolynomial α R →ₐ[R] MvPolynomial S R => g f) h

/-- Differentiate along a fixed vector of polynomial coordinates. -/
def direction (x : α → R) : Derivation R (MvPolynomial α R) (MvPolynomial α R) :=
  mkDerivation R fun a => C (x a)

theorem direction_sum (x : α → R) (f : MvPolynomial α R) :
    direction x f = ∑ a ∈ f.vars, C (x a) * pderiv a f := by
  classical
  let D : Derivation R (MvPolynomial α R) (MvPolynomial α R) :=
    ∑ a ∈ f.vars, (C (x a) : MvPolynomial α R) • pderiv a
  have h : direction x f = D f := by
    apply derivation_eq_of_forall_mem_vars
    intro a ha
    simp [direction, D, Pi.single_apply, ha, smul_eq_mul]
  simpa [D, smul_eq_mul] using h

/-- The amplitude derivative is the constant directional derivative in the
input polynomial. This is a proved chain rule, including repeated jets. -/
theorem substitution_direction (v : S → α → R) (s : S) (f : MvPolynomial α R) :
    vectorSubstitution v (direction (v s) f) = pderiv s (vectorSubstitution v f) := by
  classical
  apply aeval_intertwines
  intro a
  simp [direction, pderiv_X, Pi.single_apply]

omit [DecidableEq S] in
/-- Extracting the square-free coefficient can be done by differentiating
in any slot and then extracting a coefficient independent of that slot. -/
theorem coeff_multilinear_derivative (s : S) (P : MvPolynomial S R) :
    (pderiv s P).coeff ((multilinearDegree : S →₀ ℕ).erase s) =
      P.coeff (multilinearDegree : S →₀ ℕ) := by
  classical
  rw [coeff_pderiv]
  simp only [Finsupp.erase_same, Nat.cast_zero, zero_add, mul_one]
  change P.coeff (Finsupp.erase s multilinearDegree +
    Finsupp.single s (multilinearDegree s)) = _
  rw [Finsupp.erase_add_single]

/-- Slot formula: all dependence on the selected vector is in the displayed
linear factor. The remaining coefficient sets that slot to zero. -/
theorem polarization_slot_formula (f : MvPolynomial α R) (v : S → α → R) (s : S) :
    polarization f v = ∑ a ∈ f.vars, v s a *
      (vectorSubstitution (Function.update v s 0) (pderiv a f)).coeff
        ((multilinearDegree : S →₀ ℕ).erase s) := by
  classical
  change (vectorSubstitution v f).coeff multilinearDegree = _
  rw [← coeff_multilinear_derivative s, ← substitution_direction, direction_sum]
  simp only [map_sum, map_mul, algHom_C, AddMonoidAlgebra.coeff_sum,
    Finsupp.finsetSum_apply, algebraMap_eq, coeff_C_mul]
  apply Finset.sum_congr rfl
  intro a ha
  rw [← coeff_zeroSlot s _ Finsupp.erase_same _, zeroSlot_substitution]

/-- Coefficient polarization is genuinely multilinear, in every degree and
without a homogeneity hypothesis on the input polynomial. -/
def polarizationMap (f : MvPolynomial α R) : MultilinearMap R (fun _ : S => α → R) R where
  toFun := polarization f
  map_update_add' v s x y := by
    classical
    simp only [polarization_slot_formula f _ s, Function.update_self,
      Function.update_idem, Pi.add_apply, add_mul, Finset.sum_add_distrib]
  map_update_smul' v s c x := by
    classical
    simp only [polarization_slot_formula f _ s, Function.update_self,
      Function.update_idem, Pi.smul_apply, smul_eq_mul, mul_assoc, Finset.mul_sum]

/-- Taking spatial jets of a wave is linear in its field amplitudes. -/
def waveJet (k : S → R) (s : S) : (α → R) →ₗ[R] (α × ℕ → R) where
  toFun v j := v j.1 * k s ^ j.2
  map_add' v w := by ext j; simp [add_mul]
  map_smul' c v := by ext j; simp [smul_eq_mul, mul_assoc]

/-- Polarized wave symbols form a multilinear map of their Cauchy vectors. -/
def wavePolarization (f : Density R α) (k : S → R) :
    MultilinearMap R (fun _ : S => α → R) R :=
  (polarizationMap f).compLinearMap (waveJet k)

omit [DecidableEq S] in
@[simp] theorem wavePolarization_apply (f : Density R α) (k : S → R) (v : S → α → R) :
    wavePolarization f k v = polarized k (fun a s => v s a) f := rfl

end Structural.Symbol
