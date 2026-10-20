module

public import Structural.JetAlgebra

/-!
# Constant-field evaluation and a nonvacuity check

Evaluation on a spatially constant field annihilates every total derivative.
It therefore descends to local functionals. In particular, the class of an
undifferentiated field, and the class of the constant density one, are nonzero.
-/

@[expose] public section

noncomputable section

namespace Structural.Jet

variable {R α : Type*} [CommRing R]

/-- Evaluate undifferentiated fields at `v` and all positive-order jets at zero. -/
def constantJet (v : α → R) : Density R α →ₐ[R] R :=
  MvPolynomial.aeval fun j => if j.2 = 0 then v j.1 else 0

@[simp] theorem constantJet_z (v : α → R) (a : α) (n : ℕ) :
    constantJet v (z a n) = if n = 0 then v a else 0 := by
  simp [constantJet, z]

/-- A total spatial derivative vanishes on every spatially constant field. -/
@[simp] theorem constantJet_Dx (v : α → R) (f : Density R α) :
    constantJet v (Dx f) = 0 := by
  induction f using MvPolynomial.induction_on with
  | C c => simp
  | add f g hf hg => simp [hf, hg]
  | mul_X f j hf =>
    change constantJet v (Dx (f * z j.1 j.2)) = 0
    simp [hf]

/-- Evaluation of a local-functional class on constant fields, per unit length. -/
def constantEvaluation (v : α → R) : LocalFunctional R α →ₗ[R] R :=
  divergences.liftQ (constantJet v).toLinearMap (by
    rintro f ⟨g, rfl⟩
    exact constantJet_Dx v g)

@[simp] theorem constantEvaluation_integral (v : α → R) (f : Density R α) :
    constantEvaluation v (integral f) = constantJet v f := rfl

theorem integral_one_ne_zero [Nontrivial R] :
    integral (1 : Density R α) ≠ 0 := by
  intro h
  have := congrArg (constantEvaluation (fun _ : α => (0 : R))) h
  simp at this

theorem integral_z_zero_ne_zero [Nontrivial R] (a : α) :
    integral (z a 0 : Density R α) ≠ 0 := by
  intro h
  have := congrArg (constantEvaluation (fun _ : α => (1 : R))) h
  simp at this

theorem Dx_ne_zero [Nontrivial R] (a : α) :
    (Dx : Derivation R (Density R α) (Density R α)) ≠ 0 := by
  intro h
  have hz := congrArg (fun d : Derivation R (Density R α) (Density R α) =>
    MvPolynomial.eval (fun _ => (1 : R)) (d (z a 0))) h
  rw [Dx_z] at hz
  simp [z] at hz

end Structural.Jet
