module

public import Mathlib.Algebra.MvPolynomial.Derivation
public import Mathlib.LinearAlgebra.Quotient.Basic
public import Mathlib.RingTheory.Derivation.Lie

/-!
# Polynomial Cauchy jets and local functionals

`Density R α` is the polynomial algebra on the independent variables `z[a,n]`,
where `a` labels a field and `n` its number of spatial derivatives. Every
polynomial has finite support, even though there are infinitely many jets.

The spatial derivative is a *constructed* nontrivial derivation. Local
functionals form a vector-space quotient by its image, not a ring quotient:
products of integrated local densities are not local densities.

This is the polynomial core. Analytic germs and evaluation on periodic fields
are separate obligations.
-/

@[expose] public section

noncomputable section

namespace Structural

abbrev Density (R α : Type*) [CommRing R] := MvPolynomial (α × ℕ) R

namespace Jet

variable {R α : Type*} [CommRing R]

/-- The independent jet variable with component `a` and spatial order `n`. -/
def z (a : α) (n : ℕ) : Density R α := MvPolynomial.X (a, n)

/-- A finite bound on the spatial orders appearing in a density. -/
def order (f : Density R α) : ℕ := f.vars.sup Prod.snd

theorem le_order_of_mem_vars (f : Density R α) (j : α × ℕ) (hj : j ∈ f.vars) :
    j.2 ≤ order f :=
  Finset.le_sup (f := Prod.snd) hj

/-- Total spatial differentiation, `Dx z[a,n] = z[a,n+1]`. -/
def Dx : Derivation R (Density R α) (Density R α) :=
  MvPolynomial.mkDerivation R fun j => z j.1 (j.2 + 1)

@[simp] theorem Dx_z (a : α) (n : ℕ) :
    Dx (z a n : Density R α) = z a (n + 1) := by
  simp [Dx, z]

@[simp] theorem Dx_C (c : R) : Dx (MvPolynomial.C c : Density R α) = 0 := by
  simp

theorem Dx_mul (f g : Density R α) :
    Dx (f * g) = Dx f * g + f * Dx g := by
  simp [Derivation.leibniz, smul_eq_mul, add_comm, mul_comm]

/-- Iterated total spatial derivative, retained as a linear map. -/
def dxn (n : ℕ) : Density R α →ₗ[R] Density R α := Dx.toLinearMap ^ n

@[simp] theorem dxn_zero (f : Density R α) : dxn 0 f = f := rfl

theorem dxn_succ (n : ℕ) (f : Density R α) :
    dxn (n + 1) f = Dx (dxn n f) := by
  simp [dxn, pow_succ', Module.End.mul_apply]

theorem dxn_succ_right (n : ℕ) (f : Density R α) :
    dxn (n + 1) f = dxn n (Dx f) := by
  simp [dxn, pow_succ, Module.End.mul_apply]

@[simp] theorem dxn_z (n : ℕ) (a : α) (k : ℕ) :
    dxn n (z a k : Density R α) = z a (k + n) := by
  induction n with
  | zero => simp
  | succ n ih => rw [dxn_succ, ih, Dx_z, Nat.add_assoc]

/-- Prolong a local characteristic `Q[a]` to all its spatial derivatives. -/
def evolution (Q : α → Density R α) :
    Derivation R (Density R α) (Density R α) :=
  MvPolynomial.mkDerivation R fun j => dxn j.2 (Q j.1)

@[simp] theorem evolution_z (Q : α → Density R α) (a : α) (n : ℕ) :
    evolution Q (z a n) = dxn n (Q a) := by
  simp [evolution, z]

/-- Evolution and spatial differentiation commute on every polynomial density. -/
theorem evolution_commutes_Dx (Q : α → Density R α) (f : Density R α) :
    evolution Q (Dx f) = Dx (evolution Q f) := by
  have h : ⁅evolution Q, Dx⁆ = (0 : Derivation R (Density R α) (Density R α)) := by
    apply MvPolynomial.derivation_ext
    rintro ⟨a, n⟩
    change evolution Q (Dx (z a n)) - Dx (evolution Q (z a n)) = 0
    simp [dxn_succ]
  have hf := congrArg (fun d : Derivation R (Density R α) (Density R α) => d f) h
  exact sub_eq_zero.mp hf

/-- Densities which are total spatial derivatives. This is a submodule, not an ideal. -/
def divergences : Submodule R (Density R α) := LinearMap.range Dx.toLinearMap

abbrev LocalFunctional (R α : Type*) [CommRing R] :=
  Density R α ⧸ (divergences : Submodule R (Density R α))

/-- Formal integration of a local density, modulo a total spatial derivative. -/
def integral : Density R α →ₗ[R] LocalFunctional R α := divergences.mkQ

theorem integral_eq_zero_iff (f : Density R α) :
    integral f = 0 ↔ ∃ g, Dx g = f := by
  change Submodule.Quotient.mk f = (0 : LocalFunctional R α) ↔ _
  rw [Submodule.Quotient.mk_eq_zero]
  rfl

@[simp] theorem integral_Dx (f : Density R α) : integral (Dx f) = 0 :=
  (integral_eq_zero_iff _).2 ⟨f, rfl⟩

@[simp] theorem integral_z_succ (a : α) (n : ℕ) :
    integral (z a (n + 1) : Density R α) = 0 := by
  rw [← Dx_z, integral_Dx]

theorem integration_by_parts (f g : Density R α) :
    integral (f * Dx g) = -integral (Dx f * g) := by
  have h := integral_Dx (f * g)
  rw [Dx_mul, map_add] at h
  exact eq_neg_of_add_eq_zero_right h

/-- Repeated integration by parts; no boundary conditions are hidden in this
algebraic assertion. The periodic interpretation is established separately. -/
theorem integration_by_parts_iterated (n : ℕ) (f g : Density R α) :
    integral (f * dxn n g) = (-1 : R) ^ n • integral (dxn n f * g) := by
  induction n generalizing f with
  | zero => simp
  | succ n ih =>
    rw [dxn_succ, integration_by_parts, ih, ← dxn_succ_right]
    simp [pow_succ]

/-- Evolution descends to the quotient because it preserves total derivatives. -/
def localEvolution (Q : α → Density R α) :
    LocalFunctional R α →ₗ[R] LocalFunctional R α :=
  divergences.mapQ divergences (evolution Q).toLinearMap (by
    rintro f ⟨g, rfl⟩
    exact ⟨evolution Q g, (evolution_commutes_Dx Q g).symm⟩)

@[simp] theorem localEvolution_integral (Q : α → Density R α) (f : Density R α) :
    localEvolution Q (integral f) = integral (evolution Q f) := rfl

/-- Conservation means the actual prolonged evolution is a spatial divergence. -/
def Conserved (Q : α → Density R α) (F : LocalFunctional R α) : Prop :=
  localEvolution Q F = 0

theorem conserved_iff (Q : α → Density R α) (f : Density R α) :
    Conserved Q (integral f) ↔ ∃ flux, evolution Q f = Dx flux := by
  simp only [Conserved, localEvolution_integral, integral_eq_zero_iff]
  exact exists_congr fun _ => eq_comm

end Jet
end Structural
