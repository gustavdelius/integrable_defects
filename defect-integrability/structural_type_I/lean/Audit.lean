module

import Structural
import Lean.Util.CollectAxioms

/-!
Audit *every* declaration in the project's namespace, including dependencies.
Fail rather than merely printing a warning if any theorem uses `sorryAx` or
an additional mathematical axiom. These are Lean's standard classical
foundations, not integrability assumptions.
-/

open Lean in
run_cmd do
  let allowed : Array Name := #[``propext, ``Classical.choice, ``Quot.sound]
  let env ← getEnv
  let mut count : Nat := 0
  -- Imported module theorems can be represented by axiom-shaped interface
  -- entries. Do not filter with `isTheorem`: `collectAxioms` consults the
  -- module's recorded proof dependencies.
  for (name, _) in env.constants.toList do
    if (privateToUserName name).toString.startsWith "Structural." then
      let axioms ← collectAxioms name
      for ax in axioms do
        unless allowed.contains ax do
          throwError "{name} depends on unapproved axiom {ax}"
      count := count + 1
  if count == 0 then
    throwError "No Structural declarations were found; the audit checked nothing."
  logInfo m!"PASS: audited {count} Structural declarations; only propext, Classical.choice, Quot.sound."

#print axioms Structural.Jet.evolution_commutes_Dx
#print axioms Structural.Jet.integral_z_zero_ne_zero
#print axioms Structural.Jet.JetCurve.periodicIntegral_integral
#print axioms Structural.Free.linear_conserved_is_divergence
#print axioms Structural.Dispersion.multiPhase_kernel_eq_zero
#print axioms Structural.Momentum.complex_divisible_of_real_vanishes
#print axioms Structural.Jet.homogeneous_is_divergence_of_euler_zero
#print axioms Structural.Free.massless_chiral_power_conserved
#print axioms Structural.Free.chiral_power_ne_zero

#print axioms Structural.Symbol.polarized_conservation
#print axioms Structural.Symbol.homogeneous_eq_zero_of_polarization_zero
#print axioms Structural.Symbol.polarizationMap
#print axioms Structural.Symbol.real_massive_arbitrary_vectors_eq_zero
#print axioms Structural.Symbol.real_conserved_fourierPolynomial_divisible
#print axioms Structural.Symbol.homogeneous_eq_zero_of_wave_tests
#print axioms Structural.Free.higher_conserved_is_divergence
#print axioms Structural.Free.polynomial_conserved_quadratic_primitive
#print axioms Structural.Formal.conserved_eq_of_quadratic_eq
#print axioms Structural.Formal.conserved_difference_primitives
