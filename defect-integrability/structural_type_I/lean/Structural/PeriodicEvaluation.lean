module

public import Structural.JetAlgebra
public import Mathlib.Analysis.Calculus.IteratedDeriv.Defs
public import Mathlib.MeasureTheory.Integral.IntervalIntegral.FundThmCalculus
import Mathlib.Analysis.Calculus.Deriv.Mul

/-!
# Evaluation on actual fields

The algebraic total derivative evaluates to the ordinary derivative of the
evaluated density. Consequently its integral vanishes when the jets match at
the endpoints, in particular on smooth periodic Cauchy data.

This proves soundness of quotienting by total derivatives. It does not yet
prove the converse that all densities with zero periodic integral are total
derivatives.
-/

@[expose] public section

noncomputable section
open scoped ContDiff

namespace Structural.Jet

variable {α : Type*}

/-- A field's spatial jets, with their actual differentiability relation. -/
structure JetCurve (α : Type*) where
  val : (α × ℕ) → ℝ → ℝ
  hasDeriv : ∀ a n x, HasDerivAt (val (a, n)) (val (a, n + 1) x) x

namespace JetCurve

/-- Every smooth field supplies a jet curve; this is not an abstract existence
assumption about jet variables. -/
def ofSmooth (u : α → ℝ → ℝ) (hu : ∀ a, ContDiff ℝ ∞ (u a)) : JetCurve α where
  val j := iteratedDeriv j.2 (u j.1)
  hasDeriv a n x := by
    rw [iteratedDeriv_succ]
    exact ((hu a).differentiable_iteratedDeriv n
      (ENat.natCast_lt_of_coe_top_le_withTop le_rfl n) x).hasDerivAt

/-- Conversely, the supplied jets are necessarily the iterated derivatives
of the zeroth field. -/
theorem val_eq_iteratedDeriv (c : JetCurve α) (a : α) (n : ℕ) :
    c.val (a, n) = iteratedDeriv n (c.val (a, 0)) := by
  induction n with
  | zero => simp
  | succ n ih =>
    rw [iteratedDeriv_succ, ← ih]
    funext x
    exact (c.hasDeriv a n x).deriv.symm

/-- Substitute the actual Cauchy jets into a polynomial density. -/
def eval (c : JetCurve α) (f : Density ℝ α) (x : ℝ) : ℝ :=
  MvPolynomial.aeval (fun j => c.val j x) f

@[simp] theorem eval_z (c : JetCurve α) (a : α) (n : ℕ) (x : ℝ) :
    c.eval (z a n) x = c.val (a, n) x := by
  simp [eval, z]

@[simp] theorem eval_add (c : JetCurve α) (f g : Density ℝ α) (x : ℝ) :
    c.eval (f + g) x = c.eval f x + c.eval g x := by simp [eval]

@[simp] theorem eval_mul (c : JetCurve α) (f g : Density ℝ α) (x : ℝ) :
    c.eval (f * g) x = c.eval f x * c.eval g x := by simp [eval]

@[simp] theorem eval_smul (c : JetCurve α) (r : ℝ) (f : Density ℝ α) (x : ℝ) :
    c.eval (r • f) x = r • c.eval f x := by simp [eval]

/-- The formal total derivative is the actual spatial derivative. -/
theorem hasDerivAt_eval (c : JetCurve α) (f : Density ℝ α) (x : ℝ) :
    HasDerivAt (c.eval f) (c.eval (Dx f) x) x := by
  induction f using MvPolynomial.induction_on with
  | C r =>
    have h : c.eval (MvPolynomial.C r) = fun _ => r := by funext y; simp [eval]
    rw [h]
    simpa [eval] using hasDerivAt_const x r
  | add f g hf hg =>
    have h : c.eval (f + g) = c.eval f + c.eval g := by funext y; simp
    rw [h]
    simpa [eval] using hf.add hg
  | mul_X f j hf =>
    change HasDerivAt (c.eval (f * z j.1 j.2)) (c.eval (Dx (f * z j.1 j.2)) x) x
    have h : c.eval (f * z j.1 j.2) = c.eval f * c.val j := by funext y; simp
    rw [h]
    simpa only [Dx_mul, eval_add, eval_mul, Dx_z, eval_z] using
      hf.mul (c.hasDeriv j.1 j.2 x)

theorem continuous_eval (c : JetCurve α) (f : Density ℝ α) : Continuous (c.eval f) :=
  continuous_iff_continuousAt.2 fun x => (c.hasDerivAt_eval f x).continuousAt

/-- Integrating a total derivative gives precisely the endpoint term. -/
theorem integral_Dx_eq_boundary (c : JetCurve α) (f : Density ℝ α) (a b : ℝ) :
    (∫ x in a..b, c.eval (Dx f) x) = c.eval f b - c.eval f a :=
  intervalIntegral.integral_eq_sub_of_hasDerivAt (fun x _ => c.hasDerivAt_eval f x)
    ((c.continuous_eval (Dx f)).intervalIntegrable a b)

/-- Endpoint matching of all field jets eliminates the boundary term. -/
theorem integral_Dx_eq_zero (c : JetCurve α) (f : Density ℝ α) (a b : ℝ)
    (hperiod : ∀ j, c.val j b = c.val j a) :
    (∫ x in a..b, c.eval (Dx f) x) = 0 := by
  rw [c.integral_Dx_eq_boundary]
  have hab : c.eval f b = c.eval f a := by
    simp only [eval, hperiod]
  rw [hab, sub_self]

/-- Ordinary integration of evaluated densities is a linear map. -/
def integrate (c : JetCurve α) (a b : ℝ) : Density ℝ α →ₗ[ℝ] ℝ where
  toFun f := ∫ x in a..b, c.eval f x
  map_add' f g := by
    simp only [eval_add]
    exact intervalIntegral.integral_add
      ((c.continuous_eval f).intervalIntegrable a b)
      ((c.continuous_eval g).intervalIntegrable a b)
  map_smul' r f := by
    simp only [eval_smul, RingHom.id_apply]
    exact intervalIntegral.integral_smul r (c.eval f)

/-- Actual periodic evaluation of a local-functional class. -/
def periodicIntegral (c : JetCurve α) (a b : ℝ)
    (hperiod : ∀ j, c.val j b = c.val j a) : LocalFunctional ℝ α →ₗ[ℝ] ℝ :=
  divergences.liftQ (c.integrate a b) (by
    rintro f ⟨g, rfl⟩
    exact c.integral_Dx_eq_zero g a b hperiod)

@[simp] theorem periodicIntegral_integral (c : JetCurve α) (a b : ℝ)
    (hperiod : ∀ j, c.val j b = c.val j a) (f : Density ℝ α) :
    c.periodicIntegral a b hperiod (integral f) = ∫ x in a..b, c.eval f x := rfl

end JetCurve
end Structural.Jet
