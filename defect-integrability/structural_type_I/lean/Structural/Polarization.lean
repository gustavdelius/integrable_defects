module

public import Structural.PlaneWave
public import Mathlib.Algebra.MvPolynomial.Coeff
import Mathlib.Algebra.CharZero.Infinite

/-!
# Faithfulness and normalization of coefficient polarization

Polarization is defined by actual coefficient extraction after substituting
independent labeled vectors. On a homogeneous polynomial of degree equal to
the number of slots, its diagonal is `n!` times polynomial evaluation.
Consequently this coefficient representation loses no information in
characteristic zero. This is injectivity before taking the quotient by `Dx`;
injectivity modulo divergences is a further obligation.
-/

@[expose] public section
noncomputable section
namespace Structural.Symbol
open MvPolynomial
variable {R α S : Type*} [CommRing R] [Fintype S]

/-- Coefficient polarization of any polynomial on a possibly infinite set
of coordinates. Each polynomial itself uses only finitely many coordinates. -/
def polarization (f : MvPolynomial α R) (v : S → α → R) : R :=
  (aeval (fun a => ∑ s, C (v s a) * X s) f).coeff (multilinearDegree : S →₀ ℕ)

/-- The wave symbol is precisely coefficient polarization on the jets of
the selected plane waves. -/
theorem polarized_eq_polarization (k : S → R) (v : α → S → R) (f : Density R α) :
    polarized k v f = polarization f (fun s j => v j.1 s * k s ^ j.2) := rfl

omit [Fintype S] in
/-- Homogeneous scaling, with a polynomial-valued scale factor. -/
theorem homogeneous_substitution (f : MvPolynomial α R) (n : ℕ)
    (hf : f.IsHomogeneous n) (x : α → R) (P : MvPolynomial S R) :
    aeval (fun a => C (x a) * P) f = C (eval x f) * P ^ n := by
  classical
  rw [← mem_homogeneousSubmodule, homogeneousSubmodule_eq_finsupp_supported,
    AddMonoidAlgebra.supported_eq_span_single] at hf
  induction hf using Submodule.span_induction with
  | mem f h =>
    obtain ⟨d, hd, rfl⟩ := h
    have hd' : d.degree = n := hd
    simp only [single_eq_monomial, aeval_monomial, eval_monomial,
      algebraMap_eq, C_1, one_mul, mul_pow, Finsupp.prod_mul]
    simp only [Finsupp.prod, ← map_pow, ← map_prod, Finset.prod_pow_eq_pow_sum]
    change _ * P ^ d.degree = _
    rw [hd']
  | zero => simp
  | add f g _ _ hf hg => simp only [map_add, hf, hg, add_mul]
  | smul c f _ hf => simp [MvPolynomial.smul_eq_C_mul, hf, mul_assoc]

@[simp] theorem multilinearDegree_sum :
    (multilinearDegree : S →₀ ℕ).sum (fun _ m => m) = Fintype.card S := by
  rw [Finsupp.sum_of_support_subset _ (Finset.subset_univ _) _ (by simp)]
  simp

@[simp] theorem multilinearDegree_multinomial :
    (multilinearDegree : S →₀ ℕ).multinomial = (Fintype.card S).factorial := by
  rw [Finsupp.multinomial_eq_of_support_subset (Finset.subset_univ _)]
  simp [Nat.multinomial]

/-- Exact factorial normalization, including the zero-degree case. -/
theorem polarization_diagonal (f : MvPolynomial α R)
    (hf : f.IsHomogeneous (Fintype.card S)) (x : α → R) :
    polarization f (fun _ : S => x) = ((Fintype.card S).factorial : R) * eval x f := by
  classical
  unfold polarization
  simp only [← Finset.mul_sum]
  rw [homogeneous_substitution f _ hf, coeff_C_mul, coeff_sum_X_pow_of_fintype]
  simp [mul_comm]

section Faithfulness
variable {K : Type*} [Field K] [CharZero K]

/-- Coefficient polarization is faithful on homogeneous polynomials. This
rules out losing density information merely by extracting labeled terms. -/
theorem homogeneous_eq_zero_of_polarization_zero (f : MvPolynomial α K)
    (hf : f.IsHomogeneous (Fintype.card S))
    (h : ∀ v : S → α → K, polarization f v = 0) : f = 0 := by
  apply hf.eq_zero_of_forall_eval_eq_zero
  intro x
  have hx := h (fun _ => x)
  rw [polarization_diagonal f hf x] at hx
  exact (mul_eq_zero.mp hx).resolve_left (Nat.cast_ne_zero.mpr (Nat.factorial_ne_zero _))

/-- Two homogeneous densities with the same coefficient polarization agree
as actual polynomials, before quotienting by total derivatives. -/
theorem homogeneous_eq_of_polarization_eq (f g : MvPolynomial α K)
    (hf : f.IsHomogeneous (Fintype.card S)) (hg : g.IsHomogeneous (Fintype.card S))
    (h : ∀ v : S → α → K, polarization f v = polarization g v) : f = g := by
  apply sub_eq_zero.mp
  apply homogeneous_eq_zero_of_polarization_zero (f-g) (hf.sub hg)
  intro v
  simpa [polarization, h, sub_eq_zero] using sub_eq_zero.mpr (h v)

end Faithfulness

end Structural.Symbol
