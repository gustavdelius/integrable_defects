module

public import Mathlib.Algebra.MvPolynomial.Funext
public import Mathlib.Algebra.Polynomial.Div
public import Mathlib.Basic.Complex.Basic
import Mathlib.Algebra.CharZero.Infinite

/-!
# Polynomial division on the momentum hyperplane

Write a momentum polynomial as a polynomial in its final momentum `X`,
with coefficients polynomial in all remaining momenta. If it vanishes at
`X = -sum k`, it is divisible by `X + sum k`. The hypothesis is pointwise
vanishing at every real momentum, not a pre-assumed polynomial identity.

This is the division step of Lemma 6.1. Connecting the quotient polynomial
to a symmetrized local density is a separate polarization obligation.
-/

@[expose] public section

noncomputable section

namespace Structural.Momentum

variable {R σ : Type*} [CommRing R] [Fintype σ]

def sumVariables : MvPolynomial σ R := ∑ i, MvPolynomial.X i

def totalMomentum : Polynomial (MvPolynomial σ R) :=
  Polynomial.X + Polynomial.C sumVariables

/-- The polynomial remainder obtained by eliminating the final momentum. -/
def restrict (P : Polynomial (MvPolynomial σ R)) : MvPolynomial σ R :=
  P.eval (-sumVariables)

theorem divisible_iff_restrict_zero (P : Polynomial (MvPolynomial σ R)) :
    totalMomentum ∣ P ↔ restrict P = 0 := by
  have h : totalMomentum (R := R) (σ := σ) = Polynomial.X - Polynomial.C (-sumVariables) := by
    simp [totalMomentum]
  rw [h, Polynomial.dvd_iff_isRoot]
  rfl

/-- Vanishing on the real hyperplane forces a linear total-momentum factor. -/
theorem divisible_of_vanishes [IsDomain R] [Infinite R] (P : Polynomial (MvPolynomial σ R))
    (h : ∀ k : σ → R, MvPolynomial.eval k (restrict P) = 0) :
    totalMomentum ∣ P := by
  apply (divisible_iff_restrict_zero P).2
  apply MvPolynomial.funext
  intro k
  simpa using h k

/-- A quotient polynomial exists, so the division step loses no finite-order
polynomial information. -/
theorem factor_of_vanishes [IsDomain R] [Infinite R] (P : Polynomial (MvPolynomial σ R))
    (h : ∀ k : σ → R, MvPolynomial.eval k (restrict P) = 0) :
    ∃ Q : Polynomial (MvPolynomial σ R), P = totalMomentum * Q :=
  divisible_of_vanishes P h

/-- Fourier symbols may have complex coefficients, while the available
momenta remain real. The real locus already determines the polynomial. -/
theorem complex_divisible_of_real_vanishes (P : Polynomial (MvPolynomial σ ℂ))
    (h : ∀ k : σ → ℝ, MvPolynomial.eval (fun j => (k j : ℂ)) (restrict P) = 0) :
    totalMomentum ∣ P := by
  apply (divisible_iff_restrict_zero P).2
  apply MvPolynomial.funext_set (fun _ : σ => Set.range ((↑) : ℝ → ℂ))
    (fun _ => Set.infinite_range_of_injective Complex.ofReal_injective)
  intro k hk
  have hk' : (fun j => ((k j).re : ℂ)) = k := by
    funext j
    obtain ⟨x, hx⟩ := hk j (Set.mem_univ j)
    rw [← hx]
    rfl
  simpa only [hk', map_zero] using h (fun j => (k j).re)

end Structural.Momentum
