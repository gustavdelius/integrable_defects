#!/usr/bin/env python3
"""Exact checks of derivations and scope examples in the corrected paper.

These supplement checks.py; they do not certify the analytic rigidity lemma.
"""

import sympy as s


def check(name, value):
    values = list(value) if isinstance(value, s.MatrixBase) else [value]
    ok = all(s.expand(v) == 0 for v in values)
    print(f"{'PASS' if ok else 'FAIL'} {name}", flush=True)
    if not ok:
        raise AssertionError(name)


def vector(name):
    return s.Matrix(s.symbols(f"{name}0:3"))


def main():
    a, b, c = s.symbols("a b c")
    E = s.Matrix([[0, a, b], [-a, 0, c], [-b, -c, 0]])
    D = s.eye(3)-E
    p, P, bw, bq = map(vector, ["p", "P", "bw", "bq"])
    bu, bv = (D*bw+bq)/2, (D.T*bw-bq)/2
    ux, vx = E*p+D*P-bu, D.T*p-E*P+bv
    pdu, pdv = E*bu-D*bv, -D.T*bu-E*bv
    flux_without_potential = (p.dot(p)+ux.dot(ux)-P.dot(P)-vx.dot(vx))/2
    check("three-component momentum flux, all velocity terms",
          flux_without_potential-pdu.dot(p)-pdv.dot(P)-bw.dot(bq)/2)
    check("momentum gradients become minus B_w and plus B_q",
          (pdu+pdv+bw).col_join(D.T*pdu-D*pdv-bq))
    check("potential constraint reduces to one gradient product",
          bu.dot(bu)-bv.dot(bv)-bw.dot(bq))
    qx, wx = (ux-vx)/2, (D.T*ux+D*vx)/2
    qt, wt = (p-P)/2, (D.T*p+D*P)/2
    check("both chiral sewing equations in three components",
          (qt+qx+bw/2).col_join(wt-wx-bq/2))
    check("temporal generating functional has the stated endpoint momenta",
          (-2*qx-bw-(p-P)).col_join(2*wx+bq-(D.T*p+D*P)))

    w, q, dw, dq = map(vector, ["w", "q", "dw", "dq"])
    u, v, du, dv = w+D*q, w-D.T*q, dw+D*dq, dw-D.T*dq
    kinetic = u.dot(E*du)/2+u.dot(D*dv)+v.dot(E*dv)/2
    remainder = s.expand(kinetic-2*q.dot(dw))
    y, dy = list(w)+list(q), list(dw)+list(dq)
    primitive = s.expand(sum(s.diff(remainder, dyj)*yj for yj, dyj in zip(y, dy))/2)
    check("spatial kinetic term differs from 2q.w_x by an exact derivative",
          remainder-sum(s.diff(primitive, yj)*dyj for yj, dyj in zip(y, dy)))

    h = s.Matrix(3, 3, s.symbols("h0:9"))
    g = s.Matrix(3, 3, s.symbols("g0:9"))
    eps = s.symbols("eps", nonzero=True)
    fprime, gprime, residual, residual_minus = map(vector, ["fp", "gp", "A", "Am"])
    qplus = residual-eps*fprime/2
    wminus = gprime/(2*eps)
    qpm = residual_minus-eps*h*wminus/2
    wpm = g*qplus/(2*eps)
    Uprime = (g*fprime+D*h*gprime)/4
    check("full-sewing residual identity preserves matrix order",
          wpm+D*qpm+Uprime-D*residual_minus-g*residual/(2*eps))

    pi, time_derivative, space_derivative = map(vector, ["pi", "ut", "ux"])
    potential = s.symbols("U")
    lagrangian = (time_derivative.dot(time_derivative)-space_derivative.dot(space_derivative))/2-potential
    hx = pi.dot(space_derivative)-lagrangian
    hx = hx.subs(dict(zip(space_derivative, -pi)))
    t11 = (time_derivative.dot(time_derivative)+pi.dot(pi))/2-potential
    check("spatial Legendre transform equals minus momentum flux", hx+t11)
    # Boundary variation is pi_- du - pi_+ dv + dS_d = 0.
    # Insert the original sewing, pi_-=-u_x and pi_+=-v_x.
    action_u, action_v = E*p+D*P-bu, -D.T*p+E*P-bv
    check("spatial defect generating functional has the required minus sign",
          (-action_u+ux).col_join(-action_v-vx))

    z, qstar = vector("z"), vector("qs")
    check("a shifted transparent critical point only shifts the bulk field",
          z-D*qstar-D.T*qstar-(z-2*qstar))

    mom, first, second, mom_x = s.symbols("mom first second mom_x")
    n = s.symbols("n", integer=True, positive=True)
    rho = (mom+first)**n
    # Free massless evolution: p_t=u_xx, (u_x)_t=p_x.
    dt_rho = s.diff(rho, mom)*second+s.diff(rho, first)*mom_x
    dx_rho = s.diff(rho, mom)*mom_x+s.diff(rho, first)*second
    check("massless higher-degree local conservation laws", dt_rho-dx_rho)
    # There are no derivatives of p in rho; its p-Euler derivative is 3(p+u_x)^2.
    # Its nonzero value at p=1,u_x=0 proves the cubic functional is nontrivial.
    check("massless cubic charge has nonzero p-Euler derivative",
          s.diff(rho.subs(n, 3), mom).subs({mom: 1, first: 0})-3)


if __name__ == "__main__":
    main()
