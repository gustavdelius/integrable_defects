module

public import Mathlib.Analysis.SpecialFunctions.Sqrt
public import Mathlib.Analysis.Calculus.Deriv.Add
public import Mathlib.Analysis.Calculus.Deriv.Mul
public import Mathlib.Analysis.Calculus.Deriv.Pow
public import Mathlib.Analysis.Calculus.Deriv.Inv
public import Mathlib.Algebra.BigOperators.Fin
public import Mathlib.Data.Fin.Tuple.Basic
import Mathlib.Tactic.FieldSimp
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
# The mixed-curvature step of free massive rigidity

The squared mass is `μ > 0`. We prove the first and second derivatives of
`sqrt(k² + μ)` and the continuous-kernel vanishing argument used in Lemma 6.1.

The kernel argument does not assert absence of resonant momenta. It only
excludes a nonzero continuous kernel supported on their zero set.

The bridge from differential polynomials to these kernels is a separate,
still outstanding part of the free-rigidity proof.
-/

@[expose] public section

noncomputable section
open Filter
open scoped Topology

namespace Structural.Dispersion

def frequency (μ k : ℝ) : ℝ := Real.sqrt (k ^ 2 + μ)
def velocity (μ k : ℝ) : ℝ := k / frequency μ k
def curvature (μ k : ℝ) : ℝ := μ / frequency μ k ^ 3

theorem frequency_pos {μ : ℝ} (hμ : 0 < μ) (k : ℝ) : 0 < frequency μ k := by
  apply Real.sqrt_pos.2
  positivity

theorem frequency_sq {μ : ℝ} (hμ : 0 < μ) (k : ℝ) :
    frequency μ k ^ 2 = k ^ 2 + μ :=
  Real.sq_sqrt (by positivity)

theorem hasDerivAt_frequency {μ : ℝ} (hμ : 0 < μ) (k : ℝ) :
    HasDerivAt (frequency μ) (velocity μ k) k := by
  have hp : k ^ 2 + μ ≠ 0 := ne_of_gt (by positivity)
  convert (((hasDerivAt_id k).pow 2).add_const μ).sqrt hp using 1
  · rfl
  · dsimp [velocity, frequency]
    field_simp

theorem hasDerivAt_velocity {μ : ℝ} (hμ : 0 < μ) (k : ℝ) :
    HasDerivAt (velocity μ) (curvature μ k) k := by
  have hw := ne_of_gt (frequency_pos hμ k)
  convert (hasDerivAt_id k).div (hasDerivAt_frequency hμ k) hw using 1
  · rfl
  · dsimp [velocity, curvature]
    have hs := frequency_sq hμ k
    field_simp
    nlinarith [hs]

theorem curvature_pos {μ : ℝ} (hμ : 0 < μ) (k : ℝ) : 0 < curvature μ k :=
  div_pos hμ (pow_pos (frequency_pos hμ k) 3)

variable {V : Type*} [TopologicalSpace V] [T1Space V]
  [AddCommGroup V] [Module ℝ V] [NoZeroSMulDivisors ℝ V]

/-- A function with an everywhere nonzero mixed derivative cannot support a
nonzero continuous factor whose product with it is identically zero. -/
theorem continuous_kernel_eq_zero
    (φ φx φxy : ℝ → ℝ → ℝ)
    (hx : ∀ x y, HasDerivAt (fun s => φ s y) (φx x y) x)
    (hxy : ∀ x y, HasDerivAt (φx x) (φxy x y) y)
    (hne : ∀ x y, φxy x y ≠ 0)
    (A : ℝ × ℝ → V) (hA : Continuous A)
    (hprod : ∀ x y, φ x y • A (x, y) = 0) :
    ∀ x y, A (x, y) = 0 := by
  intro x y
  by_contra hnonzero
  have hn : ∀ᶠ q in 𝓝 (x, y), A q ≠ 0 :=
    hA.continuousAt.eventually_ne hnonzero
  have hz : ∀ᶠ q in 𝓝 (x, y), φ q.1 q.2 = 0 :=
    hn.mono fun q hq => (smul_eq_zero.mp (hprod q.1 q.2)).resolve_right hq
  rw [nhds_prod_eq] at hz
  obtain ⟨P, hP, Q, hQ, hPQ⟩ := eventually_prod_iff.mp hz
  have hfirst : ∀ᶠ t in 𝓝 y, φx x t = 0 := by
    filter_upwards [hQ] with t ht
    have heq : (fun s => φ s t) =ᶠ[𝓝 x] fun _ => (0 : ℝ) :=
      hP.mono fun s hs => hPQ hs ht
    have hd := heq.deriv_eq
    simpa [(hx x t).deriv] using hd
  have heq : φx x =ᶠ[𝓝 y] fun _ => (0 : ℝ) := hfirst
  have hd := heq.deriv_eq
  have hzero : φxy x y = 0 := by
    simpa [(hxy x y).deriv] using hd
  exact hne x y hzero

/-- The phase obtained by freezing all but two independent momenta on the
total-momentum hyperplane. Terms depending only on the second momentum can
be completely arbitrary; only the first term needs a first derivative. -/
theorem massive_phase_kernel_eq_zero
    (μ σ c : ℝ) (hμ : 0 < μ) (hσ : σ ≠ 0)
    (f f' g : ℝ → ℝ) (hf : ∀ x, HasDerivAt f (f' x) x)
    (A : ℝ × ℝ → V) (hA : Continuous A)
    (hprod : ∀ x y, (f x + g y + σ * frequency μ (-x - y + c)) • A (x, y) = 0) :
    ∀ x y, A (x, y) = 0 := by
  apply continuous_kernel_eq_zero
    (fun x y => f x + g y + σ * frequency μ (-x - y + c))
    (fun x y => f' x - σ * velocity μ (-x - y + c))
    (fun x y => σ * curvature μ (-x - y + c)) ?_ ?_ ?_ A hA hprod
  · intro x y
    have hinner : HasDerivAt (fun s : ℝ => -s - y + c) (-1) x := by
      convert (((hasDerivAt_id x).neg).sub_const y).add_const c using 1
      simp
    convert (hf x |>.add_const (g y)).add
      (((hasDerivAt_frequency hμ (-x - y + c)).comp x hinner).const_mul σ) using 1
    · rfl
    · ring
  · intro x y
    have hinner : HasDerivAt (fun t : ℝ => -x - t + c) (-1) y := by
      convert ((hasDerivAt_const y (-x)).sub (hasDerivAt_id y)).add_const c using 1 <;> simp
    convert (hasDerivAt_const y (f' x)).sub
      (((hasDerivAt_velocity hμ (-x - y + c)).comp y hinner).const_mul σ) using 1
    · rfl
    · ring
  · intro x y
    exact mul_ne_zero hσ (ne_of_gt (curvature_pos hμ _))

/-- Phase on the momentum hyperplane for `n + 3` factors: `n + 2` momenta
are independent and the final one is their negative sum. -/
def multiPhase {n : ℕ} (μ σ : Fin (n + 2) → ℝ) (μlast σlast : ℝ)
    (k : Fin (n + 2) → ℝ) : ℝ :=
  (∑ j, σ j * frequency (μ j) (k j)) + σlast * frequency μlast (-(∑ j, k j))

/-- The continuous-kernel conclusion holds for every degree at least three
and every sign/species component, including complex-valued kernels by taking
`V = ℂ`. It uses no claim that the resonant set is empty. -/
theorem multiPhase_kernel_eq_zero {n : ℕ}
    (μ σ : Fin (n + 2) → ℝ) (μlast σlast : ℝ)
    (hμ : ∀ j, 0 < μ j) (hμlast : 0 < μlast) (hσlast : σlast ≠ 0)
    (A : (Fin (n + 2) → ℝ) → V) (hA : Continuous A)
    (hprod : ∀ k, multiPhase μ σ μlast σlast k • A k = 0) :
    ∀ k, A k = 0 := by
  intro k
  let rest := Fin.tail (Fin.tail k)
  let slice (q : ℝ × ℝ) : Fin (n + 2) → ℝ := Fin.cons q.1 (Fin.cons q.2 rest)
  have hslice : Continuous slice := by
    apply continuous_pi
    intro j
    refine Fin.cases ?_ (fun j => ?_) j
    · exact continuous_fst
    · refine Fin.cases ?_ (fun _ => ?_) j
      · exact continuous_snd
      · exact continuous_const
  have hz := massive_phase_kernel_eq_zero μlast σlast (-(∑ j, rest j))
    hμlast hσlast
    (fun x => σ 0 * frequency (μ 0) x)
    (fun x => σ 0 * velocity (μ 0) x)
    (fun y => σ 1 * frequency (μ 1) y +
      ∑ j : Fin n, σ j.succ.succ * frequency (μ j.succ.succ) (rest j))
    (fun x => (hasDerivAt_frequency (hμ 0) x).const_mul (σ 0))
    (fun q => A (slice q)) (hA.comp hslice) (by
      intro x y
      simpa [multiPhase, slice, Fin.sum_univ_succ, sub_eq_add_neg, neg_add_rev,
        add_assoc, add_left_comm, add_comm] using hprod (slice (x, y)))
  have hslice_eq : slice (k 0, k 1) = k := by
    change Fin.cons (k 0) (Fin.cons ((Fin.tail k) 0) (Fin.tail (Fin.tail k))) = k
    rw [Fin.cons_self_tail, Fin.cons_self_tail]
  simpa only [hslice_eq] using hz (k 0) (k 1)

end Structural.Dispersion
