import DefectIntegrability
open DefectIntegrability

-- 0. Axioms used by each main declaration
#print axioms theorem_1_spatial_hamilton_jacobi_and_backlund
#print axioms proposition_4_1_stress_tensor_potentials
#print axioms theorem_2_part_3_involution
#print axioms lemma_2_1_ostrogradsky

-- 1. On Int, every `SpaceTimeDerivations` is multiplication by a constant.
theorem derivs_are_scalars (dt dx : Int → Int) (hD : SpaceTimeDerivations dt dx) :
    (∀ a, dt a = a * dt 1) ∧ (∀ a, dx a = a * dx 1) := by
  constructor
  · intro a; have := hD.map_mul_c_t a 1; simpa using this
  · intro a; have := hD.map_mul_c_x a 1; simpa using this

-- ... and the identity map satisfies all hypotheses including `h_vac_norm`.
example : SpaceTimeDerivations id id :=
  ⟨rfl, rfl, fun _ _ => rfl, fun _ _ => rfl, fun _ _ => rfl, fun _ _ => rfl,
   fun _ => rfl, fun _ => rfl, fun _ _ => rfl, fun _ _ => rfl, fun _ => rfl⟩

-- 2. `lemma_2_1_ostrogradsky` takes Lemma 2.1 itself (T^1_1 = H^(x) + ∂_tΥ_1) as a hypothesis.
--    Its first conclusion is a rearrangement of the two hypotheses.

-- 3. `theorem_2_part_2_first_charge_density`: H, Ψ1, B0, B1 are free variables and the
--    O(ε) "coefficient" is typed by hand; the statement is x + 0 = x.  Replace H by 12345:
example (Ψ1 Ψ2 dB0 B1 : Int) :
    2 * (0:Int) * Ψ2 + 12345 * (Ψ1 * Ψ1) + 2 * dB0 * Ψ1 + 2 * B1 =
      12345 * (Ψ1 * Ψ1) + 2 * dB0 * Ψ1 + 2 * B1 := by omega

-- 4. Theorem 1, conjunct (1)<->(2) holds for arbitrary integers, unrelated to Γ_d, dH, X:
example (Hm Hp Tm Tp dP dUm dUp dPt : Int)
    (h1 : Tm = -Hm - dUm) (h2 : Tp = -Hp - dUp) (h3 : dPt = dP + dUm - dUp) :
    (-Tm + Tp + dP = 0) ↔ (Hm - Hp = -dPt) := by omega

-- 5. Theorem 1, conjunct (3b) does not use the Lagrangian hypothesis at all:
--    it holds for ANY subtraction-closed transverse relation.
example {Vm Vp : Type} (zm : Vm) (zp : Vp) (sm : Vm → Vm → Vm) (sp : Vp → Vp → Vp)
    (Γ : Vm × Vp → Prop) (hT : TransverseLinearCorrespondence zm zp sm sp Γ)
    (Xm dzm : Vm) (Xp dzp : Vp) (htraj : Γ (dzm, dzp)) (htan : Γ (Xm, Xp)) :
    dzm = Xm ↔ dzp = Xp := by
  have hD := hT.sub_mem (dzm, dzp) (Xm, Xp) htraj htan
  constructor
  · intro h; subst h; rw [hT.sub_self_minus] at hD
    exact hT.eq_of_sub_eq_zero_plus _ _ (hT.transverse_right _ hD)
  · intro h; subst h; rw [hT.sub_self_plus] at hD
    exact hT.eq_of_sub_eq_zero_minus _ _ (hT.transverse_left _ hD)

-- 6. `section_5_1_chiral_backlund_equivalence`: the hypotheses already imply BOTH bulk equations.
example (bφ bψ Uφ Vψ : Int) (h_diff : bφ - bψ = -(Uφ - Vψ)) (h_sum : bφ + bψ = -(Uφ + Vψ)) :
    bφ + Uφ = 0 ∧ bψ + Vψ = 0 := by omega

-- 7. eq_3_6 proves only isotropy, in one scalar dimension; the Lagrangian property
--    Γ^⊥ = Γ used by Lemma 3.1 / Theorem 1 is a separate hypothesis that nothing derives.
--    Isotropy alone does not give the HJ ⇒ tangency direction: take Γ = {0} (isotropic,
--    not Lagrangian) in V × V with Ω = 0... (zero form): every w is ⊥ to Γ.
example : ¬ IsLagrangianSubspace (V_minus := Int) (V_plus := Int)
    (fun _ _ => 0) (fun _ _ => 0) (fun v => v = (0, 0)) := by
  intro h
  have := (h (1, 0)).mp (fun v _ => by simp [omegaDiff])
  simp at this
