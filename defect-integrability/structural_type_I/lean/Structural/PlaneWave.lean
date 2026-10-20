module

public import Structural.LinearRigidity
public import Mathlib.RingTheory.MvPolynomial.EulerIdentity
public import Mathlib.Topology.Algebra.MvPolynomial
import Mathlib.Tactic.Ring

/-!
# Algebraic plane waves and the conservation equation for their symbols

A wave is encoded by its spatial eigenvalue and its vector of field
amplitudes. Substitution gives an actual polynomial in independently labeled
wave amplitudes. Coefficient extraction is the unnormalized polarization.
-/

@[expose] public section
noncomputable section

namespace Structural.Symbol

open MvPolynomial Jet
variable {R α S : Type*} [CommRing R] [Fintype S]

/-- The derivation multiplying the amplitude of wave `s` by `lam s`. -/
def diagonal (lam : S → R) : Derivation R (MvPolynomial S R) (MvPolynomial S R) :=
  ∑ s, (C (lam s) * X s) • pderiv s

@[simp] theorem diagonal_X (lam : S → R) (s : S) :
    diagonal lam (X s) = C (lam s) * X s := by
  classical
  simp [diagonal, Pi.single_apply, smul_eq_mul]

theorem diagonal_monomial (lam : S → R) (d : S →₀ ℕ) (r : R) :
    diagonal lam (monomial d r) = (∑ s, d s • lam s) • monomial d r := by
  classical
  have heval : (diagonal lam) (monomial d r) =
      ∑ s, (C (lam s) * X s) * pderiv s (monomial d r) := by
    simp [diagonal, smul_eq_mul]
  rw [heval, Finset.sum_smul]
  apply Finset.sum_congr rfl
  intro s hs
  rw [mul_assoc, X_mul_pderiv_monomial, ← smul_eq_C_mul, smul_comm, smul_assoc]


/-- Every coefficient is an eigenvector for a diagonal amplitude derivation. -/
theorem coeff_diagonal (lam : S → R) (d : S →₀ ℕ) (P : MvPolynomial S R) :
    (diagonal lam P).coeff d = (∑ s, d s • lam s) * P.coeff d := by
  classical
  induction P using MvPolynomial.induction_on' with
  | monomial e r =>
    rw [diagonal_monomial, coeff_smul]
    by_cases h : e = d
    · subst e; simp [smul_eq_mul]
    · simp [coeff_monomial, h]
  | add P Q hP hQ => simp [hP, hQ, mul_add]

/-- Substitution intertwines two derivations when it does so on generators. -/
theorem aeval_intertwines {β : Type*} (v : α → MvPolynomial β R)
    (D : Derivation R (MvPolynomial α R) (MvPolynomial α R))
    (E : Derivation R (MvPolynomial β R) (MvPolynomial β R))
    (h : ∀ a, aeval v (D (X a)) = E (v a)) (f : MvPolynomial α R) :
    aeval v (D f) = E (aeval v f) := by
  induction f using MvPolynomial.induction_on with
  | C r => simp
  | add f g hf hg => simp only [map_add, hf, hg]
  | mul_X f a hf =>
    simp only [Derivation.leibniz, smul_eq_mul, map_add, map_mul, aeval_X, hf, h]

/-- Substitute a finite sum of spatial eigenmodes for every Cauchy jet. -/
def waves (k : S → R) (v : α → S → R) : Density R α →ₐ[R] MvPolynomial S R :=
  aeval fun j => ∑ s, C (v j.1 s * k s ^ j.2) * X s

@[simp] theorem waves_z (k : S → R) (v : α → S → R) (a : α) (n : ℕ) :
    waves k v (z a n) = ∑ s, C (v a s * k s ^ n) * X s := by
  simp [waves, z]

/-- Total spatial differentiation becomes diagonal differentiation in wave
amplitudes; this holds for every density, without a degree assumption. -/
theorem waves_Dx (k : S → R) (v : α → S → R) (f : Density R α) :
    waves k v (Dx f) = diagonal k (waves k v f) := by
  apply aeval_intertwines
  rintro ⟨a, n⟩
  change waves k v (Dx (z a n)) = _
  simp only [Dx_z, waves_z, map_sum, Derivation.leibniz, MvPolynomial.derivation_C,
    smul_eq_mul, diagonal_X, mul_zero]
  apply Finset.sum_congr rfl
  intro s hs
  simp only [pow_succ, map_mul]
  ring

/-- The symbol component with amplitude multidegree `d`. -/
def component (d : S →₀ ℕ) (k : S → R) (v : α → S → R)
    (f : Density R α) : R := (waves k v f).coeff d

theorem component_Dx (d : S →₀ ℕ) (k : S → R) (v : α → S → R)
    (f : Density R α) :
    component d k v (Dx f) = (∑ s, d s • k s) * component d k v f := by
  exact (congrArg (fun p => p.coeff d) (waves_Dx k v f)).trans (coeff_diagonal k d _)

theorem waves_dxn (k : S → R) (v : α → S → R) (n : ℕ) (f : Density R α) :
    waves k v (dxn n f) = ((diagonal k).toLinearMap ^ n) (waves k v f) := by
  induction n with
  | zero => rfl
  | succ n ih => rw [dxn_succ, waves_Dx, ih, pow_succ', Module.End.mul_apply]; rfl

/-- Multidegree one in each independently labeled amplitude. -/
def multilinearDegree : S →₀ ℕ := Finsupp.onFinset Finset.univ (fun _ => 1) (by simp)

@[simp] theorem multilinearDegree_apply (s : S) : multilinearDegree s = 1 := rfl

/-- Unnormalized polarization: take the term using every wave exactly once. -/
def polarized (k : S → R) (v : α → S → R) (f : Density R α) : R :=
  component multilinearDegree k v f

theorem polarized_Dx (k : S → R) (v : α → S → R) (f : Density R α) :
    polarized k v (Dx f) = (∑ s, k s) * polarized k v f := by
  simp [polarized, component_Dx]

/-- Coefficients of a polynomial substitution vary continuously if all
coefficients of each substituted generator do. No topology on the infinite
jet algebra or convergence of a Fourier series is required. -/
theorem continuous_coeff_aeval {T β : Type*} [TopologicalSpace T]
    [TopologicalSpace R] [IsTopologicalRing R]
    (v : T → α → MvPolynomial β R)
    (hv : ∀ a d, Continuous fun x => (v x a).coeff d)
    (f : MvPolynomial α R) (d : β →₀ ℕ) :
    Continuous fun x => (aeval (v x) f).coeff d := by
  classical
  induction f using MvPolynomial.induction_on generalizing d with
  | C r => simpa using (continuous_const : Continuous fun _ : T => (C r : MvPolynomial β R).coeff d)
  | add f g hf hg =>
    simp only [map_add, AddMonoidAlgebra.coeff_add, Finsupp.add_apply]
    exact continuous_add.comp ((hf d).prodMk (hg d))
  | mul_X f a hf =>
    simp only [map_mul, aeval_X, coeff_mul]
    exact continuous_finsetSum _ fun e he => (hf e.1).mul (hv a e.2)

theorem continuous_component {T : Type*} [TopologicalSpace T]
    [TopologicalSpace R] [IsTopologicalRing R]
    (k : T → S → R) (v : T → α → S → R)
    (hk : ∀ s, Continuous fun x => k x s)
    (hv : ∀ a s, Continuous fun x => v x a s)
    (f : Density R α) (d : S →₀ ℕ) :
    Continuous fun x => component d (k x) (v x) f := by
  classical
  apply continuous_coeff_aeval
  rintro ⟨a,n⟩ e
  simp only [AddMonoidAlgebra.coeff_sum, Finsupp.finsetSum_apply, coeff_C_mul]
  exact continuous_finsetSum _ fun s hs =>
    ((hv a s).mul ((hk s).pow n)).mul continuous_const

/-- Changing coefficients commutes with spatial differentiation. -/
theorem map_Dx {K : Type*} [CommRing K] (c : R →+* K) (f : Density R α) :
    MvPolynomial.map c (Dx f) = Dx (MvPolynomial.map c f) := by
  induction f using MvPolynomial.induction_on with
  | C r => simp
  | add f g hf hg => simp [hf, hg]
  | mul_X f j hf =>
    change MvPolynomial.map c (Dx (f * z j.1 j.2)) = _
    simp only [Dx_mul, map_add, map_mul, hf, Dx_z]
    simp [Dx, z]

theorem map_dxn {K : Type*} [CommRing K] (c : R →+* K) (n : ℕ) (f : Density R α) :
    MvPolynomial.map c (dxn n f) = dxn n (MvPolynomial.map c f) := by
  induction n with
  | zero => rfl
  | succ n ih => rw [dxn_succ, map_Dx, ih, dxn_succ]

/-- Prolonged evolution is compatible with a change of coefficient ring. -/
theorem map_evolution {K : Type*} [CommRing K] (c : R →+* K)
    (Q : α → Density R α) (f : Density R α) :
    MvPolynomial.map c (evolution Q f) =
      evolution (fun a => MvPolynomial.map c (Q a)) (MvPolynomial.map c f) := by
  induction f using MvPolynomial.induction_on with
  | C r => simp
  | add f g hf hg => simp [hf, hg]
  | mul_X f j hf =>
    simp only [Derivation.leibniz, smul_eq_mul, map_add, map_mul, hf, map_X]
    congr 1
    change _ * MvPolynomial.map c (evolution Q (z j.1 j.2)) = _
    rw [evolution_z, map_dxn]
    simp [evolution]


section Free
variable {ι K : Type*} [Field K]

/-- Algebraic oscillator eigenvectors intertwine the actual free evolution
with time differentiation of the wave amplitudes. -/
theorem waves_free_evolution (massSq : ι → K) (k t : S → K)
    (v : (ι × Bool) → S → K)
    (hu : ∀ a s, v (a, true) s = t s * v (a, false) s)
    (hp : ∀ a s, (k s ^ 2 - massSq a) * v (a, false) s = t s * v (a, true) s)
    (f : Density K (ι × Bool)) :
    waves k v (evolution (Free.characteristic massSq) f) = diagonal t (waves k v f) := by
  apply aeval_intertwines
  rintro ⟨⟨a, b⟩, n⟩
  change waves k v (evolution (Free.characteristic massSq) (z (a,b) n)) = _
  cases b with
  | false =>
    simp only [evolution_z, Free.characteristic, dxn_z, zero_add, waves_z,
      map_sum, Derivation.leibniz, derivation_C, diagonal_X, smul_eq_mul, mul_zero,
      add_zero]
    apply Finset.sum_congr rfl
    intro s hs
    rw [hu a s]
    simp only [map_mul]
    ring
  | true =>
    simp only [evolution_z, Free.characteristic, map_sub, map_smul, dxn_z,
      zero_add, waves_z, map_sum, Derivation.leibniz, derivation_C, diagonal_X,
      smul_eq_mul, mul_zero, add_zero]
    rw [Finset.smul_sum, ← Finset.sum_sub_distrib]
    apply Finset.sum_congr rfl
    intro s hs
    simp only [smul_eq_C_mul, ← mul_assoc, ← sub_mul, ← map_mul, ← map_sub]
    congr 1
    congr 1
    calc
      v (a, false) s * k s ^ (2+n) - massSq a * v (a, false) s * k s ^ n =
          ((k s ^ 2 - massSq a) * v (a, false) s) * k s ^ n := by rw [pow_add]; ring
      _ = (t s * v (a, true) s) * k s ^ n := by rw [hp a s]
      _ = _ := by ring

/-- Conservation of a concrete density gives the spectral equation, with
an actual flux on the right. No Fourier conservation law is assumed. -/
theorem component_conservation (massSq : ι → K) (d : S →₀ ℕ) (k t : S → K)
    (v : (ι × Bool) → S → K)
    (hu : ∀ a s, v (a, true) s = t s * v (a, false) s)
    (hp : ∀ a s, (k s ^ 2 - massSq a) * v (a, false) s = t s * v (a, true) s)
    (f : Density K (ι × Bool))
    (hc : Conserved (Free.characteristic massSq) (integral f)) :
    ∃ flux, (∑ s, d s • t s) * component d k v f =
      (∑ s, d s • k s) * component d k v flux := by
  obtain ⟨flux, hflux⟩ := (conserved_iff _ _).mp hc
  refine ⟨flux, ?_⟩
  rw [← component_Dx, hflux.symm]
  unfold component
  rw [waves_free_evolution massSq k t v hu hp, coeff_diagonal]

/-- On zero total spatial momentum the polarized conservation equation has
zero right-hand side. -/
theorem polarized_conservation (massSq : ι → K) (k t : S → K)
    (v : (ι × Bool) → S → K)
    (hu : ∀ a s, v (a, true) s = t s * v (a, false) s)
    (hp : ∀ a s, (k s ^ 2 - massSq a) * v (a, false) s = t s * v (a, true) s)
    (f : Density K (ι × Bool))
    (hc : Conserved (Free.characteristic massSq) (integral f))
    (hk : ∑ s, k s = 0) :
    (∑ s, t s) * polarized k v f = 0 := by
  obtain ⟨flux, h⟩ := component_conservation massSq multilinearDegree k t v hu hp f hc
  simpa [multilinearDegree_apply, hk, polarized] using h

/-- Conservation survives extension of scalars, in particular from real to
complex coefficients for the normal-mode calculation. -/
theorem map_free_conserved {L : Type*} [Field L] (c : K →+* L)
    (massSq : ι → K) (f : Density K (ι × Bool))
    (hc : Conserved (Free.characteristic massSq) (integral f)) :
    Conserved (Free.characteristic (fun a => c (massSq a))) (integral (MvPolynomial.map c f)) := by
  obtain ⟨flux, hflux⟩ := (conserved_iff _ _).mp hc
  apply (conserved_iff _ _).mpr
  refine ⟨MvPolynomial.map c flux, ?_⟩
  have hchar : (fun a => MvPolynomial.map c (Free.characteristic massSq a)) =
      Free.characteristic (fun a => c (massSq a)) := by
    funext ⟨a,b⟩
    cases b <;> simp [Free.characteristic, z, smul_eq_C_mul]
  rw [← hchar, ← map_evolution, hflux, map_Dx]

end Free

end Structural.Symbol
