# Can a defect join mKdV to KdV through the Miura map?

*Working note, 23 October 2026. Not part of the paper. Section and equation numbers refer to [paper.md](paper.md). Checks: [`checks/check_miura.py`](checks/check_miura.py).*

**Question.** Theorem 3.3 allows a defect between two different theories; Remark 3.4.4 gives a Liouville–free example. The Miura map $u=v^2+v_x$ carries mKdV solutions to KdV solutions. Is there a momentum-conserving defect, Type I or Type II, whose sewing conditions, imposed at every $x$, are the Miura map?

**Answer so far.**
- For Type I: no, for any defect Lagrangian (A2). This is a proof.
- For Type II with one defect field: no, under natural assumptions (A3). This is argued, not proved.
- Momentum conservation alone already says what a Type-II field would have to be (A1).

## Setting

- **mKdV (left, $x<0$).** $\mathcal L_m=\frac12q_xq_t-\frac12q_x^4-\frac12q_{xx}^2$ with $v=q_x$, giving $v_t=6v^2v_x-v_{xxx}$.
- **KdV (right, $x>0$).** $\mathcal L_K=\frac12p_xp_t-p_x^3-\frac12p_{xx}^2$, which is (9.3) of [3], with $u=p_x$, giving $u_t=6uu_x-u_{xxx}$.
- **Miura.** With these signs, $u=v^2+v_x$ maps mKdV solutions to KdV solutions.
- **Ostrogradsky momenta** (§2, $K=2$). For mKdV, $\pi_1=-q_{xx}$ and $\pi_0=\frac12q_t-2q_x^3+q_{xxx}$. For KdV, $\pi_1=-p_{xx}$ and $\pi_0=\frac12p_t-3p_x^2+p_{xxx}$.
- **Momentum densities** (Lemma 2.1). $T^{01}=-\frac12v^2$ for mKdV and $-\frac12u^2$ for KdV.

Boundary data at $x=0$ are $Y=(q,Q_1,p,P_1;\lambda)$, with $Q_1=q_x$ and $P_1=p_x$. The sewing equations (3.1) are $\pi_{-,m}=-E_{\Phi_m}\mathcal L_d$, $\pi_{+,m}=E_{\Psi_m}\mathcal L_d$ and $C=E_\lambda\mathcal L_d=0$.

## A1. Momentum forces a potential for the mKdV energy (argument)

Along promoted solutions, Proposition 4.2 gives $D_x\widetilde P=\frac12v^2-\frac12u^2$. The Miura map turns this into

$$\tfrac12v^2-\tfrac12u^2=D_x\Big(\tfrac12p-\tfrac12q_x-\tfrac13q_x^3\Big)-h,\qquad h=\tfrac12v^4+\tfrac12v_x^2,$$

where $h$ is the mKdV energy density. It is not a total derivative of a local function of $q$, nor of $(q,p)$ treated as potentials. For the latter, expand in powers of the potentials: the top power forces its coefficient to be constant, and the next power then makes $u$ or $v$ trivial.

So $\widetilde P$ needs a defect variable $\lambda$ that, along promoted solutions, is a nonlocal potential of $h$: $D_x\lambda\cong h$. Then $\widetilde P=\frac12p-\frac12Q_1-\frac13Q_1^3-\lambda$. The energy of mKdV is the momentum of KdV, since $\frac12u^2=h+D_x(\frac13v^3)$. So $\lambda$ is also the potential of the KdV momentum density.

If every defect variable is a local function of $(q,p)$ and their jets along promoted solutions, no such $\lambda$ exists. This covers Type I with multipliers that the sewing equations determine algebraically. The rigour gap is the case where $p$ or $\lambda$ is pinned by an implicit relation.

## A2. No Type-I defect has the Miura sewing conditions (proof)

Suppose the sewing outputs satisfy the Miura relations identically in $Y$, with no constraint. The relations are $u=v^2+v_x$ and its $x$-derivatives $u_x=2vv_x+v_{xx}$ and $u_{xx}=2v_x^2+2vv_{xx}+v_{xxx}$. In the last one, $v_{xxx}=-Q_{1,t}+6Q_1^2v_x$ by the left field equation. The time relation for $p$ involves the potential's gauge $p\mapsto p+g(t)$, so it imposes nothing. With $v_x=q_{xx}=E_{Q_1}\mathcal L_d$ and $q_{xxx}=-E_q\mathcal L_d-\frac12q_t+2Q_1^3$, the relations become

$$\text{(S1) } E_{Q_1}\mathcal L=P_1-Q_1^2,\qquad \text{(S2) } E_{P_1}\mathcal L-E_q\mathcal L=-2Q_1P_1+\tfrac12q_t,$$
$$\text{(S3) } E_p\mathcal L+2Q_1E_q\mathcal L=\tfrac12p_t-P_1^2+2Q_1^2P_1-Q_1q_t-Q_{1,t}.$$

Let $S_{AB}$ be the Fréchet derivative of $E_A\mathcal L$ with respect to $B$. By the Helmholtz conditions (§3.1) it is self-adjoint, $S_{AB}^*=S_{BA}$.
- (S1) gives $S_{Q_1P_1}=1$ and $S_{Q_1q}=0$.
- Hence $S_{qQ_1}=S_{Q_1q}^*=0$.
- (S2) then gives $S_{P_1Q_1}=S_{qQ_1}-2P_1=-2P_1$.
- Self-adjointness requires $S_{P_1Q_1}=S_{Q_1P_1}^*=1$, a contradiction.

No Type-I defect Lagrangian of any order has these sewing conditions, whether or not it conserves momentum. The same argument works for $u=v^2-v_x$, for a constant shift $u=v^2\pm v_x+\alpha$, and for any constant rescaling of either Lagrangian.

In the language of Appendix A: the Miura map does not intertwine the spatial symplectic structures of $\mathcal L_m$ and $\mathcal L_K$.

`check_miura.py` confirms this independently. A general ansatz of 110 monomials gives 168 linear equations, and they have no solution.

## A3. Type II with one defect field (argued, not proved)

Give the fields their scaling weights: $v$ weight 1, $u$ weight 2, $\partial_t$ weight 3, $q$ weight 0, $p$ weight 1. By A1, $\lambda$ has weight 3.
- The left sewing equations need $\mathcal L_d$ of weight 3, because $\pi_{-,1}$ has weight 2.
- The right sewing equations need weight 5, because $\pi_{+,0}$ has weight 4.
- The bulk Lagrangians themselves have different weights, 4 and 6.

So $\mathcal L_d$ must combine a weight-3 and a weight-5 part. The sewing relations (S1)–(S3) and the momentum balance then split by weight, provided the constraint $C$ is homogeneous. A homogeneous constraint is natural, because the Miura map has no parameter.

Now list the ways $\lambda$ can enter.
- **Through $\lambda_t$ only** (shift-invariant, so that $\lambda$ stays nonlocal). Then $C=-D_tn(Y)$, so $n(Y)$ is constant on the defect. Weight counting gives $n$ weight 0, 1 or 2. For weight 0 the constraint freezes $q_t$. For weight 1 or 2 the constraint either freezes left Cauchy data ($Q_1$, or $q_{xx}$ through (S1)), or makes $p$ a local function of the boundary data. The last is impossible, because $p_x=u$ and $v^2$ is not a total derivative.
- **Algebraically** (as a multiplier, or with a potential in $\lambda$). Then the sewing equations determine $\lambda$ as a local function of the boundary data. By A1 it cannot then be a potential of $h$.
- **As a free multiplier.** Its terms must drop out of (S1)–(S3), and the problem reduces to A2 restricted to $C=0$. A homogeneous constraint of weight 2 is $aP_1+bQ_1^2+(\text{terms with }p)=0$. It again freezes $q_{xx}$ at the defect or pins $p$.

None of these leaves an admissible structure. The argument assumes:
- a polynomial $\mathcal L_d$;
- one defect field;
- a constraint homogeneous in the weights;
- no dimensionful defect parameter that drops out of the Miura relations.

It is not a proof.

## What remains open, and what came out of it

- **Open.** Two or more defect fields; non-polynomial dependence; an inhomogeneous constraint with a parameter that drops out of the promoted relations. A heterogeneous defect in which the KdV side uses a different, nonlocal Lagrangian would sidestep A1, because the KdV momentum depends on the Lagrangian chosen.
- **Spin-off 1.** The Wahlquist–Estabrook defect of [3] is two Miura maps fused through an mKdV field of zero width. The two momentum mismatches of A1 then cancel, and what remains is exactly the defect momentum (9.13) of [3] (paper, §9 comment 8).
- **Spin-off 2.** Fusing in the other order, mKdV | KdV | mKdV through $v^2+v_x=w^2-w_x$, makes the momentum mismatch local: $\frac12v^2-\frac12w^2=-\frac12D_x(v+w)$. That relation might give a parameter-free Type-I mKdV defect, which would be degenerate in the sense of Definition 7.6. Not checked.
- **Spin-off 3.** The Gardner defect (paper, §9 comment 7).
