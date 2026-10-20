module

public import Mathlib.Analysis.SpecialFunctions.Sqrt
import Mathlib.Tactic.Ring
import Mathlib.Tactic.Positivity

/-!
Environment checks only. These statements are not a formalization of any
of the paper's structural integrability claims.
-/

public section

namespace Structural.Smoke

theorem real_ring (x y : ℝ) : (x + y) ^ 2 = x ^ 2 + 2 * x * y + y ^ 2 := by
  ring

theorem massive_frequency_positive (m k : ℝ) (hm : 0 < m) :
    0 < Real.sqrt (k ^ 2 + m ^ 2) := by
  apply Real.sqrt_pos.2
  positivity

end Structural.Smoke
