# Structural Type-I checks

These scripts support the corrected `defect-integrability/defect_integrability_paper.md` and the supporting `defect-integrability/structural_type_I/proof.md`.

| Script | Run | Coverage |
|---|---|---|
| `checks.py` | `python3 textbook_code/defect_integrability_structural/checks.py` | Exact matrix sewing and symplectic identities; seven quadratic Hamiltonian generators; a finite Fourier independence determinant; the anisotropic free counterexample; the massive Fourier phase derivative; an exact nonlinear two-component potential identity, its first four local currents, and the Poisson bracket of its spin-two and spin-four charges, with no amplitude truncation. |
| `paper_checks.py` | `python3 textbook_code/defect_integrability_structural/paper_checks.py` | Twelve exact checks of the corrected paper's derivations and scope: general three-component momentum and chiral identities, temporal endpoint momenta, kinetic gauge term, full-sewing residual, spatial Hamiltonian and generating-functional signs, shifted transparency, and the massless obstruction to quadratic-part rigidity. |

Requires Python 3 and SymPy. Every check prints `PASS` or raises after printing `FAIL`. These are finite symbolic checks, not a formal verification of the theorem.
