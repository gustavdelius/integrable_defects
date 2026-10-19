# Structural Type-I checks

These scripts support `defect-integrability/structural_type_I/proof.md` and do not modify the book.

| Script | Run | Coverage |
|---|---|---|
| `checks.py` | `python3 textbook_code/defect_integrability_structural/checks.py` | Exact matrix sewing and symplectic identities; seven quadratic Hamiltonian generators; a finite Fourier independence determinant; the anisotropic free counterexample; the massive Fourier phase derivative; an exact nonlinear two-component potential identity, its first four local currents, and the Poisson bracket of its spin-two and spin-four charges, with no amplitude truncation. |

Requires Python 3 and SymPy. Every check prints `PASS` or raises after printing `FAIL`. These are finite symbolic checks, not a formal verification of the theorem.
