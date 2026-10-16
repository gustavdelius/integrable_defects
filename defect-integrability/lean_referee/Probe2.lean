import DefectIntegrability
example (S Sinv : Int) (h : Sinv * S = 1) : S = 1 ∨ S = -1 := by
  have h1 : S ∣ 1 := ⟨Sinv, by rw [Int.mul_comm]; exact h.symm⟩
  have h2 := Int.natAbs_dvd_natAbs.mpr h1
  simp at h2
  omega
