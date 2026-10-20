module

public import Structural.LinearRigidity
public import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Ring
import Mathlib.Tactic.NormNum

/-!
# Nontrivial checks of the free-field model

These are kernel-checked identities in the same jet quotient used for
rigidity. Energy and momentum are conserved. In the massless case, every
power of a chiral field is a nonzero conserved local functional. Thus removing
the mass hypothesis really does invalidate higher-degree rigidity in this
model.
-/

@[expose] public section

noncomputable section

namespace Structural.Free

open Jet
variable {ι : Type*}

def energyDensity (massSq : ι → ℝ) (a : ι) : Density ℝ (ι × Bool) :=
  (1 / 2 : ℝ) • (z (a, true) 0 ^ 2 + z (a, false) 1 ^ 2 +
    massSq a • z (a, false) 0 ^ 2)

theorem energy_current (massSq : ι → ℝ) (a : ι) :
    evolution (characteristic massSq) (energyDensity massSq a) =
      Dx (z (a, true) 0 * z (a, false) 1) := by
  rw [energyDensity, Derivation.map_smul]
  calc
    _ = (1 / 2 : ℝ) • ((2 : ℝ) • Dx (z (a, true) 0 * z (a, false) 1)) := by
      congr 1
      simp [Derivation.leibniz_pow, characteristic, dxn_succ,
        Derivation.leibniz, smul_eq_mul, MvPolynomial.smul_eq_C_mul,
        show (MvPolynomial.C (2 : ℝ) : Density ℝ (ι × Bool)) = 2 from
          MvPolynomial.C_eq_coe_nat 2]
      ring
    _ = _ := by rw [smul_smul]; norm_num

theorem energy_conserved (massSq : ι → ℝ) (a : ι) :
    Conserved (characteristic massSq) (integral (energyDensity massSq a)) :=
  (conserved_iff _ _).2 ⟨z (a, true) 0 * z (a, false) 1, energy_current massSq a⟩

/-- The sign agrees with the physical bulk momentum convention of the paper. -/
def momentumDensity (a : ι) : Density ℝ (ι × Bool) :=
  -(z (a, true) 0 * z (a, false) 1)

theorem momentum_current (massSq : ι → ℝ) (a : ι) :
    evolution (characteristic massSq) (momentumDensity a) =
      Dx (-(1 / 2 : ℝ) • (z (a, true) 0 ^ 2 + z (a, false) 1 ^ 2 -
        massSq a • z (a, false) 0 ^ 2)) := by
  have h : Dx (z (a, true) 0 ^ 2 + z (a, false) 1 ^ 2 -
      massSq a • z (a, false) 0 ^ 2) =
      (-2 : ℝ) • evolution (characteristic massSq) (momentumDensity a) := by
    simp [momentumDensity, Derivation.leibniz_pow, characteristic, dxn_succ,
      Derivation.leibniz, smul_eq_mul, MvPolynomial.smul_eq_C_mul,
      show (MvPolynomial.C (2 : ℝ) : Density ℝ (ι × Bool)) = 2 from
        MvPolynomial.C_eq_coe_nat 2]
    ring
  rw [Derivation.map_smul, h, smul_smul]
  norm_num

theorem momentum_conserved (massSq : ι → ℝ) (a : ι) :
    Conserved (characteristic massSq) (integral (momentumDensity a)) :=
  (conserved_iff _ _).2 ⟨_, momentum_current massSq a⟩

def chiral (a : ι) : Density ℝ (ι × Bool) := z (a, true) 0 + z (a, false) 1

theorem massless_chiral_transport (a : ι) :
    evolution (characteristic (fun _ : ι => (0 : ℝ))) (chiral a) = Dx (chiral a) := by
  simp [chiral, characteristic, dxn_succ, add_comm]

theorem massless_chiral_power_conserved (a : ι) (n : ℕ) :
    Conserved (characteristic (fun _ : ι => (0 : ℝ))) (integral (chiral a ^ n)) := by
  apply (conserved_iff _ _).2
  refine ⟨chiral a ^ n, ?_⟩
  simp only [Derivation.leibniz_pow, massless_chiral_transport]

theorem chiral_power_homogeneous (a : ι) (n : ℕ) :
    (chiral a ^ n).IsHomogeneous n := by
  simpa [chiral, z] using ((MvPolynomial.isHomogeneous_X (R := ℝ) ((a, true), 0)).add
    (MvPolynomial.isHomogeneous_X (R := ℝ) ((a, false), 1))).pow n

theorem chiral_power_ne_zero (a : ι) (n : ℕ) :
    integral (chiral a ^ n) ≠ 0 := by
  intro h
  have hval := congrArg (constantEvaluation (fun _ : ι × Bool => (1 : ℝ))) h
  simp [chiral] at hval

end Structural.Free
