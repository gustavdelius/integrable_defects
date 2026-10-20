module

public import Structural.FreeRigidity

/-!
# Nonlinear rigidity for formal amplitude series

The parameter here scales all Cauchy jets; it is not the Bäcklund parameter.
The density coefficient of order `n` has amplitude degree `n`. The
characteristic coefficient indexed by `k` has degree `k+1`, so its prolonged
action raises density degree by `k`. The evolution coefficient is the finite
convolution constructed below, using the actual polynomial derivations.

With positive diagonal massive linearization, a conserved formal functional
is determined by its constant and quadratic classes. This is a coefficientwise
statement modulo actual spatial derivatives. It asserts neither convergence
nor a uniform spatial-order bound on coefficients or their primitives.
Analytic finite-jet germs and their Taylor correspondence remain separate.
-/

@[expose] public section
noncomputable section

namespace Structural.Formal
open MvPolynomial Jet

/-- A formal expansion in amplitude, with finite polynomial jet coefficients. -/
structure AmplitudeSeries (α : Type*) where
  coeff : ℕ → Density ℝ α
  homogeneous : ∀ n, (coeff n).IsHomogeneous n

/-- A characteristic vanishing at the vacuum, indexed so that index zero is
its linear part. -/
structure CharacteristicSeries (α : Type*) where
  coeff : ℕ → α → Density ℝ α
  homogeneous : ∀ k a, (coeff k a).IsHomogeneous (k+1)

variable {α : Type*}

/-- The coefficient of the prolonged nonlinear evolution. Only finitely many
pairs of amplitude degrees contribute to each coefficient. -/
def evolutionCoeff (Q : CharacteristicSeries α) (F : AmplitudeSeries α) (n : ℕ) :
    Density ℝ α :=
  ∑ k ∈ Finset.range (n+1), evolution (Q.coeff k) (F.coeff (n-k))

/-- The finite convolution has exactly the claimed amplitude degree. -/
theorem evolutionCoeff_homogeneous (Q : CharacteristicSeries α)
    (F : AmplitudeSeries α) (n : ℕ) : (evolutionCoeff Q F n).IsHomogeneous n := by
  unfold evolutionCoeff
  apply IsHomogeneous.sum
  intro k hk
  have hkn : k ≤ n := by simpa using (Finset.mem_range.mp hk)
  by_cases hzero : n-k = 0
  · have hf := F.homogeneous (n-k)
    rw [hzero, ← totalDegree_zero_iff_isHomogeneous,
      totalDegree_eq_zero_iff_eq_C] at hf
    rw [hzero, hf]
    simp only [MvPolynomial.derivation_C]
    apply isHomogeneous_zero
  · have hdegree : (k+1) + ((n-k)-1) = n := by omega
    simpa only [hdegree] using homogeneous_evolution_weight
      (Q.coeff k) (k+1) (Q.homogeneous k) (F.coeff (n-k)) (n-k) (F.homogeneous (n-k))

/-- Conservation in the formal completion of the concrete local-functional
quotient. Every equation is an equation of actual polynomial classes. -/
def Conserved (Q : CharacteristicSeries α) (F : AmplitudeSeries α) : Prop :=
  ∀ n, integral (evolutionCoeff Q F n) = 0

/-- Once all lower-degree functional classes vanish, the coefficient of
nonlinear conservation reduces to conservation under the linear part. -/
theorem linear_conserved_of_lower_zero (Q : CharacteristicSeries α)
    (F : AmplitudeSeries α) (n : ℕ) (hc : Conserved Q F)
    (hlower : ∀ m, m < n → integral (F.coeff m) = 0) :
    Jet.Conserved (Q.coeff 0) (integral (F.coeff n)) := by
  have h := hc n
  unfold evolutionCoeff at h
  rw [map_sum] at h
  have hsum :
      (∑ k ∈ Finset.range (n+1), integral (evolution (Q.coeff k) (F.coeff (n-k)))) =
        integral (evolution (Q.coeff 0) (F.coeff n)) := by
    apply Finset.sum_eq_single 0
    · intro k hk hk0
      have hk_le : k ≤ n := by simpa using (Finset.mem_range.mp hk)
      rw [← localEvolution_integral, hlower (n-k) (by omega), map_zero]
    · simp
  rw [hsum] at h
  exact h

/-- Formal nonlinear rigidity, proved by induction on amplitude degree.
There is no assumption that higher conserved terms already vanish. -/
theorem conserved_eq_zero {ι : Type*} [Fintype ι]
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (Q : CharacteristicSeries (ι × Bool))
    (hlinear : Q.coeff 0 = Free.characteristic massSq)
    (F : AmplitudeSeries (ι × Bool)) (hc : Conserved Q F)
    (hzero : integral (F.coeff 0) = 0) (hquadratic : integral (F.coeff 2) = 0) :
    ∀ n, integral (F.coeff n) = 0 := by
  intro n
  induction n using Nat.strong_induction_on with
  | h n ih =>
    by_cases hn0 : n = 0
    · simpa only [hn0] using hzero
    by_cases hn2 : n = 2
    · simpa only [hn2] using hquadratic
    apply Free.homogeneous_conserved_eq_zero n hn0 hn2 massSq hm _ (F.homogeneous n)
    rw [← hlinear]
    exact linear_conserved_of_lower_zero Q F n hc ih

/-- Subtraction preserves the actual homogeneous density coefficients. -/
def sub (F G : AmplitudeSeries α) : AmplitudeSeries α where
  coeff n := F.coeff n - G.coeff n
  homogeneous n := (F.homogeneous n).sub (G.homogeneous n)

theorem evolutionCoeff_sub (Q : CharacteristicSeries α) (F G : AmplitudeSeries α)
    (n : ℕ) :
    evolutionCoeff Q (sub F G) n = evolutionCoeff Q F n - evolutionCoeff Q G n := by
  simp [evolutionCoeff, sub, map_sub, Finset.sum_sub_distrib]

theorem conserved_sub (Q : CharacteristicSeries α) (F G : AmplitudeSeries α)
    (hF : Conserved Q F) (hG : Conserved Q G) : Conserved Q (sub F G) := by
  intro n
  rw [evolutionCoeff_sub, map_sub, hF n, hG n, sub_self]

/-- Two formal conserved functionals with the same constant and quadratic
classes have identical classes in every amplitude degree. -/
theorem conserved_eq_of_quadratic_eq {ι : Type*} [Fintype ι]
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (Q : CharacteristicSeries (ι × Bool))
    (hlinear : Q.coeff 0 = Free.characteristic massSq)
    (F G : AmplitudeSeries (ι × Bool)) (hF : Conserved Q F) (hG : Conserved Q G)
    (hzero : integral (F.coeff 0) = integral (G.coeff 0))
    (hquadratic : integral (F.coeff 2) = integral (G.coeff 2)) :
    ∀ n, integral (F.coeff n) = integral (G.coeff n) := by
  have h := conserved_eq_zero massSq hm Q hlinear (sub F G) (conserved_sub Q F G hF hG)
    (by change integral (F.coeff 0 - G.coeff 0) = 0; rw [map_sub, hzero, sub_self])
    (by change integral (F.coeff 2 - G.coeff 2) = 0; rw [map_sub, hquadratic, sub_self])
  intro n
  have hn := h n
  change integral (F.coeff n - G.coeff n) = 0 at hn
  rw [map_sub, sub_eq_zero] at hn
  exact hn

/-- Each difference coefficient has a finite polynomial spatial primitive.
No common spatial-order bound on the primitives is asserted. -/
theorem conserved_difference_primitives {ι : Type*} [Fintype ι]
    (massSq : ι → ℝ) (hm : ∀ a, 0 < massSq a)
    (Q : CharacteristicSeries (ι × Bool))
    (hlinear : Q.coeff 0 = Free.characteristic massSq)
    (F G : AmplitudeSeries (ι × Bool)) (hF : Conserved Q F) (hG : Conserved Q G)
    (hzero : integral (F.coeff 0) = integral (G.coeff 0))
    (hquadratic : integral (F.coeff 2) = integral (G.coeff 2)) :
    ∃ g : ℕ → Density ℝ (ι × Bool), ∀ n, Dx (g n) = F.coeff n - G.coeff n := by
  have h := conserved_eq_of_quadratic_eq massSq hm Q hlinear F G hF hG hzero hquadratic
  have hp : ∀ n, ∃ g, Dx g = F.coeff n - G.coeff n := by
    intro n
    apply (integral_eq_zero_iff _).mp
    rw [map_sub, h n, sub_self]
  exact Classical.axiomOfChoice hp

end Structural.Formal
