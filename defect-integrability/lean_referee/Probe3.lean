import DefectIntegrability
open DefectIntegrability

-- 1. Every pair of Leibniz derivations on Int is identically zero.
theorem derivs_vanish (dt dx : Int → Int) (hD : SpaceTimeDerivations dt dx) :
    (∀ a, dt a = 0) ∧ (∀ a, dx a = 0) := by
  have hnat_t : ∀ n : Nat, dt (n : Int) = 0 := by
    intro n; induction n with
    | zero => exact SpaceTimeDerivations.map_zero_t hD
    | succ k ih =>
      have := hD.map_add_t (k : Int) 1
      rw [SpaceTimeDerivations.map_one_t hD, ih] at this
      simpa using this
  have hnat_x : ∀ n : Nat, dx (n : Int) = 0 := by
    intro n; induction n with
    | zero => exact SpaceTimeDerivations.map_zero_x hD
    | succ k ih =>
      have := hD.map_add_x (k : Int) 1
      rw [SpaceTimeDerivations.map_one_x hD, ih] at this
      simpa using this
  constructor
  · intro a; cases a with
    | ofNat n => exact hnat_t n
    | negSucc n =>
      have h := hD.map_neg_t ((n + 1 : Nat) : Int)
      rw [hnat_t] at h
      have e : Int.negSucc n = -((n + 1 : Nat) : Int) := rfl
      rw [e, h]; rfl
  · intro a; cases a with
    | ofNat n => exact hnat_x n
    | negSucc n =>
      have h := hD.map_neg_x ((n + 1 : Nat) : Int)
      rw [hnat_x] at h
      have e : Int.negSucc n = -((n + 1 : Nat) : Int) := rfl
      rw [e, h]; rfl

-- 2. Hence the hypotheses of proposition_4_1_stress_tensor_potentials are contradictory:
--    hD together with h_vac_norm proves False, so the proposition is vacuously true.
theorem prop_4_1_hypotheses_inconsistent (dt dx : Int → Int) (hD : SpaceTimeDerivations dt dx)
    (h_vac_norm : ∀ f : Int, dt f = 0 → f = 0) : False := by
  have := h_vac_norm 1 ((derivs_vanish dt dx hD).1 1)
  omega

-- 3. The only model is dt = dx = 0 (and it is one):
example : SpaceTimeDerivations (fun _ => 0) (fun _ => 0) := by
  constructor <;> intros <;> simp

-- 4. In that model the free-massive-scalar "derivation" forces Ψ1 = 0 and every
--    Leibniz identity in lemma_2_1_first_order, the K=2 identity, the free scalar example and
--    the NLS current reduces to 0 = 0.
example (φ Ψ1 : Int) (h : -(fun _ : Int => (0:Int)) φ = -(fun _ : Int => (0:Int)) φ - Ψ1) :
    Ψ1 = 0 := by simp at h; omega
