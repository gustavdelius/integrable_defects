import Std
import DefectCore
open Lean.Grind
namespace DefectCore

/-- Dual numbers over the integers. The Euler derivation e*d/de is nonzero. -/
structure Dual where
  a : Int
  b : Int
  deriving DecidableEq, Repr

namespace Dual
instance : Add Dual := ⟨fun x y => ⟨x.a+y.a,x.b+y.b⟩⟩
instance : Mul Dual := ⟨fun x y => ⟨x.a*y.a,x.a*y.b+x.b*y.a⟩⟩
instance : Neg Dual := ⟨fun x => ⟨-x.a,-x.b⟩⟩
instance : Sub Dual := ⟨fun x y => ⟨x.a-y.a,x.b-y.b⟩⟩
instance : OfNat Dual n := ⟨⟨n,0⟩⟩
instance : NatCast Dual := ⟨fun n => ⟨n,0⟩⟩
instance : IntCast Dual := ⟨fun n => ⟨n,0⟩⟩
instance : SMul Nat Dual := ⟨fun n x => ⟨n*x.a,n*x.b⟩⟩
instance : SMul Int Dual := ⟨fun n x => ⟨n*x.a,n*x.b⟩⟩
def power (x : Dual) : Nat → Dual
  | 0 => 1
  | n+1 => power x n * x
instance : HPow Dual Nat Dual := ⟨power⟩

@[ext] theorem ext {x y : Dual} (ha : x.a=y.a) (hb : x.b=y.b) : x=y := by
  cases x; cases y; simp_all

instance : CommRing Dual where
  add_zero := by
    intro x
    apply ext
    · change x.a + 0 = x.a; omega
    · change x.b + 0 = x.b; omega
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
  neg_add_cancel := by intro a; apply ext <;> change _ = _ <;> simp only [Neg.neg, HAdd.hAdd, Add.add, OfNat.ofNat] <;> grind
  sub_eq_add_neg := by intro a b; apply ext <;> change _ = _ <;> simp only [HSub.hSub, Sub.sub, Neg.neg, HAdd.hAdd, Add.add] <;> grind
  neg_zsmul := by intro n a; apply ext <;> change _ = _ <;> simp only [HSMul.hSMul, SMul.smul, Neg.neg] <;> grind
  zsmul_natCast_eq_nsmul := by intro n a; rfl
  intCast_ofNat := by intro n; rfl
  intCast_neg := by intro n; apply ext
                    · change (-n : Int) = -n; rfl
                    · change (0 : Int) = -0; omega
  mul_comm := by intro a b; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul] <;> grind

/-- D(a+b e)=b e, where e^2=0. -/
def euler : Deriv Dual where
  apply := fun x => ⟨0,x.b⟩
  map_add := by intro x y; rfl
  map_mul := by intro x y; apply ext <;> change _ = _ <;> simp only [HMul.hMul, Mul.mul, HAdd.hAdd, Add.add] <;> grind

def epsilon : Dual := ⟨0,1⟩
theorem euler_nonzero : euler epsilon = epsilon ∧ epsilon ≠ 0 := by
  constructor
  · rfl
  · intro h
    have := congrArg Dual.b h
    change (1 : Int) = 0 at this
    omega

theorem euler_commutes : ∀ a, euler (euler a) = euler (euler a) := fun _ => rfl

/-- A consistent analogue of normalization: only the zero-constant ideal is normalized. -/
def normalized (x : Dual) : Prop := x.a = 0

theorem normalized_kernel (x : Dual) (hn : normalized x) (hd : euler x = 0) : x = 0 := by
  apply ext
  · exact hn
  · have h := congrArg Dual.b hd
    exact h

theorem one_not_normalized : ¬ normalized (1 : Dual) := by
  intro h
  change (1 : Int) = 0 at h
  omega

/-- A second, commuting derivation, with no injectivity hypothesis. -/
def zeroDeriv : Deriv Dual where
  apply := fun _ => 0
  map_add := by intro x y; rfl
  map_mul := by intro x y; apply ext <;> change _ = _ <;>
    simp only [HMul.hMul, Mul.mul, HAdd.hAdd, Add.add, OfNat.ofNat] <;> grind

theorem euler_zero_commute (x : Dual) : euler (zeroDeriv x) = zeroDeriv (euler x) := rfl

/-- The differentiated density in the free-scalar identity need not vanish.
    With u=1+epsilon, m2=1, dt=euler and dx=zero, its value is 2*epsilon. -/
theorem free_scalar_nonzero_residual :
    let u : Dual := 1 + epsilon
    euler ((zeroDeriv u - euler u) * (zeroDeriv u - euler u) + 1 * (u * u)) +
      zeroDeriv ((zeroDeriv u - euler u) * (zeroDeriv u - euler u) - 1 * (u * u))
      = (2 : Dual) * epsilon := by decide

theorem twice_epsilon_nonzero : (2 : Dual) * epsilon ≠ 0 := by decide

end Dual
end DefectCore
