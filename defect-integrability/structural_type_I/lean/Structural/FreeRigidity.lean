module

public import Structural.EulerSymbol
public import Structural.WaveFaithfulness
public import Structural.PolynomialHomotopy

/-!
# Homogeneous free massive rigidity in the concrete jet quotient

Every conserved homogeneous real density of degree at least three is an
actual total spatial derivative. Every vacuum-normalized conserved polynomial
functional equals its quadratic component. Conservation gives vanishing Euler wave
symbols; finite-jet wave faithfulness gives zero Euler derivatives; the
homogeneous scaling homotopy constructs a primitive. This closes the
reconstruction gap without assuming a symbol-to-density correspondence.

Analytic rigidity and the nonlinear structural theorem remain separate.
-/

@[expose] public section
noncomputable section
namespace Structural.Symbol
open MvPolynomial Jet

/-- The finite Euler operator commutes with extension of the coefficient ring. -/
theorem map_euler {R K α : Type*} [CommRing R] [CommRing K] (c : R →+* K)
    (a : α) (N : ℕ) (f : Density R α) :
    MvPolynomial.map c (euler a N f) = euler a N (MvPolynomial.map c f) := by
  simp [euler, smul_eq_C_mul, map_dxn, pderiv_map]

/-- All Euler derivatives of a homogeneous massive conserved density of
degree at least three vanish, in the complex coefficient model. -/
theorem higher_conserved_euler_eq_zero {ι : Type*} [Fintype ι] (n : ℕ)
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (f : Density ℂ (ι × Bool)) (hf : f.IsHomogeneous (n+3))
    (hc : Conserved (Free.characteristic (fun a => (massSq a : ℂ))) (integral f))
    (N : ℕ) (hN : order f ≤ N) (a : ι × Bool) : euler a N f = 0 := by
  apply homogeneous_eq_zero_of_wave_tests (S := Fin (n+2))
  · simpa using homogeneous_euler f (n+3) N a hf
  · intro k v
    exact massive_euler_symbol_eq_zero massSq hm f hc N hN a k v

end Structural.Symbol

namespace Structural.Free
open MvPolynomial Jet Symbol
variable {ι : Type*} [Fintype ι]

/-- The full degree-three-and-higher homogeneous assertion of the free
massive rigidity lemma, with a primitive in the actual polynomial jet algebra. -/
theorem higher_conserved_is_divergence (n : ℕ) (massSq : ι → ℝ)
    (hm : ∀ a, 0 < massSq a) (f : Density ℝ (ι × Bool))
    (hf : f.IsHomogeneous (n+3)) (hc : Conserved (characteristic massSq) (integral f)) :
    ∃ g, Dx g = f := by
  let fc := MvPolynomial.map Complex.ofRealHom f
  let N := max (order f) (order fc)
  apply homogeneous_is_divergence_of_euler_zero f (n+3) N (by omega) hf (le_max_left _ _)
  intro a
  apply MvPolynomial.map_injective (f := Complex.ofRealHom) Complex.ofReal_injective
  rw [map_zero, map_euler]
  exact higher_conserved_euler_eq_zero n massSq hm fc (hf.map Complex.ofRealHom)
    (map_free_conserved Complex.ofRealHom massSq f hc) N (le_max_right _ _) a

/-- Equivalently, the corresponding local functional is zero in the actual
quotient by spatial divergences. -/
theorem higher_conserved_eq_zero (n : ℕ) (massSq : ι → ℝ)
    (hm : ∀ a, 0 < massSq a) (f : Density ℝ (ι × Bool))
    (hf : f.IsHomogeneous (n+3)) (hc : Conserved (characteristic massSq) (integral f)) :
    integral f = 0 :=
  (integral_eq_zero_iff f).mpr (higher_conserved_is_divergence n massSq hm f hf hc)

/-- In positive amplitude degree, two is the only possible degree of a
nonzero homogeneous massive conserved local functional. -/
theorem homogeneous_conserved_eq_zero (n : ℕ) (hn : n ≠ 0) (hn2 : n ≠ 2)
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a) (f : Density ℝ (ι × Bool))
    (hf : f.IsHomogeneous n) (hc : Conserved (characteristic massSq) (integral f)) :
    integral f = 0 := by
  by_cases hn1 : n = 1
  · subst n
    exact linear_conserved_eq_zero massSq (fun a => ne_of_gt (hm a)) f hf hc
  · have hdeg : n = (n-3)+3 := by omega
    rw [hdeg] at hf
    exact higher_conserved_eq_zero (n-3) massSq hm f hf hc

omit [Fintype ι] in
/-- The constructed Klein–Gordon characteristic has amplitude degree one. -/
theorem characteristic_homogeneous (massSq : ι → ℝ) (a : ι × Bool) :
    (characteristic massSq a).IsHomogeneous 1 := by
  rcases a with ⟨a,b⟩
  cases b with
  | false => exact isHomogeneous_X _ _
  | true =>
    change (z (a,false) 2 - massSq a • z (a,false) 0).IsHomogeneous 1
    rw [smul_eq_C_mul]
    exact (isHomogeneous_X _ _).sub ((isHomogeneous_X _ _).C_mul _)

/-- Polynomial free massive rigidity: every vacuum-normalized conserved
local functional equals its quadratic amplitude component. The equality is
in the concrete quotient by total spatial derivatives. -/
theorem polynomial_conserved_eq_quadratic (massSq : ι → ℝ)
    (hm : ∀ a, 0 < massSq a) (f : Density ℝ (ι × Bool)) (hzero : f.coeff 0 = 0)
    (hc : Conserved (characteristic massSq) (integral f)) :
    integral f = integral (homogeneousComponent 2 f) := by
  classical
  have hsum : (∑ i ∈ Finset.range (f.totalDegree+1), integral (homogeneousComponent i f)) =
      integral (homogeneousComponent 2 f) := by
    apply Finset.sum_eq_single 2
    · intro i hi hne
      by_cases hi0 : i = 0
      · subst i; simp [hzero]
      · exact homogeneous_conserved_eq_zero i hi0 hne massSq hm _
          (homogeneousComponent_isHomogeneous i f)
          (conserved_homogeneousComponent _ (characteristic_homogeneous massSq) i f hc)
    · intro hn
      have hdeg : f.totalDegree < 2 := by
        simp only [Finset.mem_range] at hn
        omega
      rw [homogeneousComponent_eq_zero 2 f hdeg, map_zero]
  rw [← map_sum, sum_homogeneousComponent] at hsum
  exact hsum

/-- An actual finite polynomial primitive removes all nonquadratic terms
from a vacuum-normalized conserved density. -/
theorem polynomial_conserved_quadratic_primitive (massSq : ι → ℝ)
    (hm : ∀ a, 0 < massSq a) (f : Density ℝ (ι × Bool)) (hzero : f.coeff 0 = 0)
    (hc : Conserved (characteristic massSq) (integral f)) :
    ∃ g, Dx g = f - homogeneousComponent 2 f := by
  apply (integral_eq_zero_iff _).mp
  rw [map_sub, polynomial_conserved_eq_quadratic massSq hm f hzero hc, sub_self]

end Structural.Free
