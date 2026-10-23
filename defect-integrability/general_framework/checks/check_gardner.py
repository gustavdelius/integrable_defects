"""A momentum-conserving defect for the Gardner equation (Section 9, comment 7).

Bulk (potential form, w = P_x), on both sides:
    L = (c + P_x) P_t / 2 - (c + P_x)^4 / 2 + 3 c^2 P_x^2 + P_xx^2 / 2,
whose field equation is w_t = 12 c w w_x + 6 w^2 w_x + w_xxx (pure Gardner).  The
representative matters, because total x-derivatives in L change the momentum balance
(Section 5.2).  Defect, with w = p - q at x = 0 and a multiplier mu:
    L_d = (q p_t - p q_t)/4 - Bfrak,
    Bfrak = mu (p_x + q_x + 2c - alpha sin w)
          + alpha/6 cos w [(c+p_x)^2 + (c+q_x)^2 - 4(c+p_x)(c+q_x) + alpha (2c+p_x+q_x) sin w + alpha^2]
          - 3 alpha c^2 cos w - 6 c^3 w.
Without the last two terms this is the mKdV defect of [3] (eq. 7.22) on the constant
background c; that defect conserves momentum only for the bulk with the advection term
-3 c^2 P_x^2 that the Galilean frame change removes.  Uses jets.py and the balance test
of check_balance.py.  One PASS or FAIL line per check.
"""

import io
import contextlib
import sympy as sp
from jets import TJets, report
import check_balance as cb

ok = True
c, al = sp.symbols("c alpha")


def bulk(ux, ut, Z, advection):
    L = (c + ux) * ut / 2 - (c + ux) ** 4 / 2 + Z ** 2 / 2
    return L if advection else L + 3 * c ** 2 * ux ** 2


def bfrak_rest(P1, Q1, w):
    a1, b1 = c + P1, c + Q1
    return al / 6 * sp.cos(w) * (a1 ** 2 + b1 ** 2 - 4 * a1 * b1 + al * (a1 + b1) * sp.sin(w) + al ** 2)


def run(label, advection, k1, k2):
    J = TJets(["p", "P1", "q", "Q1", "mu"], cb.N)
    p, P1, q, Q1, mu = J["p"], J["P1"], J["q"], J["Q1"], J["mu"]
    Zl, Zr = sp.symbols("Zl Zr")
    w = p[0] - q[0]
    B = (mu[0] * (2 * c + P1[0] + Q1[0] - al * sp.sin(w)) + bfrak_rest(P1[0], Q1[0], w)
         + k1 * al * c ** 2 * sp.cos(w) + k2 * c ** 3 * w)
    Ld = (q[0] * p[1] - p[0] * q[1]) / 4 - B
    Q1sol = al * sp.sin(w) - 2 * c - P1[0]
    return cb.balance(label, J, [["p"], ["P1"]], [["q"], ["Q1"]], ["mu"],
                      bulk(P1[0], p[1], Zl, advection), bulk(Q1[0], q[1], Zr, advection), 2, Ld,
                      [Zl], [Zr], constraint_elims=[("Q1", 0, Q1sol)], simplify_trig=True)


# ------------------------------------------------- the bulk equation
x, t = sp.symbols("x t")
P = sp.Function("P")(x, t)
Lsym = bulk(P.diff(x), P.diff(t), P.diff(x, 2), advection=False)
EL = sp.euler_equations(Lsym, [P], [x, t])[0].lhs
wv = P.diff(x)
gardner = -wv.diff(t) + 12 * c * wv * wv.diff(x) + 6 * wv ** 2 * wv.diff(x) + wv.diff(x, 3)
ok &= report("bulk Lagrangian gives the pure Gardner equation w_t = 12c w w_x + 6 w^2 w_x + w_xxx",
             sp.simplify(sp.expand(EL - gardner)) == 0 or sp.simplify(sp.expand(EL + gardner)) == 0)

# ------------------------------------------------- momentum balance
ok &= run("mKdV defect of [3] on the background c, bulk with advection term: momentum-conserving", True, 0, 0)
with contextlib.redirect_stdout(io.StringIO()):
    uncorrected = run("uncorrected", False, 0, 0)
ok &= report("without the two correction terms the defect does not conserve momentum for the pure Gardner bulk",
             not uncorrected)
ok &= run("pure Gardner bulk with Bfrak corrected by -3 alpha c^2 cos w - 6 c^3 w: momentum-conserving",
          False, -3, -6)

# ------------------------------------------------- the sewing relations are a Baecklund relation
# Impose the sewing equations at every x with the vacuum P = 0 on the left; then w = -Q.
Qs, P1s, Q1s, ws, mus = sp.symbols("Q P1 Q1 w mu")
Bf = (mus * (2 * c + P1s + Q1s - al * sp.sin(ws)) + bfrak_rest(P1s, Q1s, ws)
      - 3 * al * c ** 2 * sp.cos(ws) - 6 * c ** 3 * ws)
Qx = (al * sp.sin(ws) - 2 * c - P1s).subs({P1s: 0, ws: -Qs})          # constraint: Q_x(Q)
mu_v = sp.solve(sp.Eq(0, sp.diff(Bf, P1s)), mus)[0]                  # left pi_1: P_xx = 0 = dBfrak/dP1
sub = lambda e: e.subs(mus, mu_v).subs({P1s: 0, Q1s: Qx.subs(Qs, -ws)}).subs(ws, -Qs)
Bp = sub(sp.diff(Bf, ws))                                            # dBfrak/dp at fixed P1, Q1
Qt = sp.simplify(2 * (-2 * c ** 3 - Bp))                             # left pi_0 at P = 0 is -2c^3
Dx = lambda f: sp.diff(f, Qs) * Qx
Qxx, Qxxx = Dx(Qx), Dx(Dx(Qx))
Qxxxx = Dx(Qxxx)
compat = sp.simplify(sp.diff(Qx, Qs) * Qt - Dx(Qt))
right1 = sp.simplify(Qxx + sub(sp.diff(Bf, Q1s)))                    # right pi_1: Q_xx = -dBfrak/dQ1
right0 = sp.simplify(Qt / 2 - 2 * (c + Qx) ** 3 + 6 * c ** 2 * Qx - Qxxx - Bp)   # right pi_0, P_t = 0
elq = sp.simplify(-sp.diff(Qx, Qs) * Qt + 6 * (c + Qx) ** 2 * Qxx - 6 * c ** 2 * Qxx + Qxxxx)
ok &= report("promoted from the vacuum, Q_x = -alpha sin Q - 2c and Q_t are compatible", compat == 0)
ok &= report("promoted from the vacuum, both right sewing equations hold", right1 == 0 and right0 == 0)
ok &= report("promoted from the vacuum, Q solves the pure Gardner equation", elq == 0)

raise SystemExit(0 if ok else 1)
