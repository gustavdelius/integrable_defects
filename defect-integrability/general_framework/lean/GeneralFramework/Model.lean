import GeneralFramework.Framework

/-
  A nonzero model: R = Z[e1, e2]/(e1^2, e1 e2, e2^2), with D_t = e1 d/de1 and
  D_x = e2 d/de2.  Both derivations are nonzero and commute, so the hypotheses
  of the theorems in `Framework.lean` are not vacuous (contrast report2, §1).
  The residual normalisation used in `potential_from_normalised_residual` is
  satisfiable here: "normalised" means zero constant term.
-/
open Lean.Grind

namespace GeneralFramework

structure Tri where
  a : Int
  b : Int
  c : Int
  deriving DecidableEq, Repr

namespace Tri
instance : Add Tri := ⟨fun x y => ⟨x.a + y.a, x.b + y.b, x.c + y.c⟩⟩
instance : Mul Tri := ⟨fun x y => ⟨x.a * y.a, x.a * y.b + x.b * y.a, x.a * y.c + x.c * y.a⟩⟩
instance : Neg Tri := ⟨fun x => ⟨-x.a, -x.b, -x.c⟩⟩
instance : Sub Tri := ⟨fun x y => ⟨x.a - y.a, x.b - y.b, x.c - y.c⟩⟩
instance : OfNat Tri n := ⟨⟨n, 0, 0⟩⟩
instance : NatCast Tri := ⟨fun n => ⟨n, 0, 0⟩⟩
instance : IntCast Tri := ⟨fun n => ⟨n, 0, 0⟩⟩
instance : SMul Nat Tri := ⟨fun n x => ⟨n * x.a, n * x.b, n * x.c⟩⟩
instance : SMul Int Tri := ⟨fun n x => ⟨n * x.a, n * x.b, n * x.c⟩⟩
def power (x : Tri) : Nat → Tri
  | 0 => 1
  | n + 1 => power x n * x
instance : HPow Tri Nat Tri := ⟨power⟩

@[ext] theorem ext {x y : Tri} (ha : x.a = y.a) (hb : x.b = y.b) (hc : x.c = y.c) : x = y := by
  cases x; cases y; simp_all

instance : CommRing Tri where
  add_zero := by intro x; apply ext <;> change _ = _ <;> simp only [HAdd.hAdd, Add.add, OfNat.ofNat] <;> grind
  add_comm := by intro a b; apply ext <;> change _ = _ <;> simp only [HAdd.hAdd, Add.add] <;> grind
  add_assoc := by intro a b c; apply ext <;> change _ = _ <;> simp only [HAdd.hAdd, Add.add] <;> grind
  mul_assoc := by intro a b c; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul] <;> grind
  mul_one := by intro a; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul, OfNat.ofNat] <;> grind
  one_mul := by intro a; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul, OfNat.ofNat] <;> grind
  left_distrib := by intro a b c; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul, HAdd.hAdd, Add.add] <;> grind
  right_distrib := by intro a b c; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul, HAdd.hAdd, Add.add] <;> grind
  zero_mul := by intro a; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul, OfNat.ofNat] <;> grind
  mul_zero := by intro a; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul, OfNat.ofNat] <;> grind
  pow_zero := by intro a; rfl
  pow_succ := by intro a n; rfl
  ofNat_succ := by intro n; apply ext <;> change _ = _ <;> simp only [OfNat.ofNat, HAdd.hAdd, Add.add] <;> grind
  ofNat_eq_natCast := by intro n; rfl
  nsmul_eq_natCast_mul := by
    intro n x
    apply ext
    · change (n : Int) * x.a = (n : Int) * x.a; rfl
    · change (n : Int) * x.b = (n : Int) * x.b + 0 * x.a; grind
    · change (n : Int) * x.c = (n : Int) * x.c + 0 * x.a; grind
  neg_add_cancel := by intro a; apply ext <;> change _ = _ <;> simp only [Neg.neg, HAdd.hAdd, Add.add, OfNat.ofNat] <;> grind
  sub_eq_add_neg := by intro a b; apply ext <;> change _ = _ <;> simp only [HSub.hSub, Sub.sub, Neg.neg, HAdd.hAdd, Add.add] <;> grind
  neg_zsmul := by intro n a; apply ext <;> change _ = _ <;> simp only [HSMul.hSMul, SMul.smul, Neg.neg] <;> grind
  zsmul_natCast_eq_nsmul := by intro n a; rfl
  intCast_ofNat := by intro n; rfl
  intCast_neg := by
    intro n; apply ext
    · change (-n : Int) = -n; rfl
    · change (0 : Int) = -0; omega
    · change (0 : Int) = -0; omega
  mul_comm := by intro a b; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul] <;> grind

def dt : Deriv Tri where
  apply := fun x => ⟨0, x.b, 0⟩
  map_add := by intro x y; rfl
  map_mul := by
    intro x y; apply ext <;> change _ = _ <;>
      simp only [HMul.hMul, Mul.mul, HAdd.hAdd, Add.add] <;> grind

def dx : Deriv Tri where
  apply := fun x => ⟨0, 0, x.c⟩
  map_add := by intro x y; rfl
  map_mul := by
    intro x y; apply ext <;> change _ = _ <;>
      simp only [HMul.hMul, Mul.mul, HAdd.hAdd, Add.add] <;> grind

def model : SpaceTime Tri where
  Dt := dt
  Dx := dx
  comm := by intro a; rfl

def e1 : Tri := ⟨0, 1, 0⟩
def e2 : Tri := ⟨0, 0, 1⟩

theorem derivations_nonzero : model.Dt e1 = e1 ∧ model.Dx e2 = e2 ∧ e1 ≠ 0 ∧ e2 ≠ 0 := by
  refine ⟨rfl, rfl, ?_, ?_⟩ <;> decide

/-- In the model, D_t r = 0 does not force r = 0 (take r = 1 or r = e2), so
normalisation must be a property of the particular residual, as in the paper.
For residuals with zero constant term and zero e2 part it does give r = 0. -/
def normalised (r : Tri) : Prop := r.a = 0 ∧ r.c = 0

theorem normalised_kernel (r : Tri) (hn : normalised r) (hd : model.Dt r = 0) : r = 0 := by
  apply ext
  · exact hn.1
  · have h := congrArg Tri.b hd
    exact h
  · exact hn.2

theorem kernel_nontrivial : model.Dt 1 = 0 ∧ model.Dt e2 = 0 ∧ (1 : Tri) ≠ 0 := by
  refine ⟨rfl, rfl, ?_⟩; decide

end Tri
end GeneralFramework
