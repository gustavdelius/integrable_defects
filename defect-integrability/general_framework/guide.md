# A reader's guide to *Momentum-Conserving Defects, Kinematic Symmetry and Integrability*

*Companion to [paper.md](paper.md) (draft of 20 October 2026). Written 22 October 2026.*

This guide explains why the paper is organised as it is and what each step of its proof does. It adds no results. References such as §3.3, (3.5) or Theorem 6.4 are to the paper. The examples in this guide that are not in the paper (the mechanical toy model of [Part 3](#part-3-the-guiding-picture-a-jump-in-classical-mechanics), the sine-Gordon formulas of [Part 5](#part-5-the-running-example-sine-gordon) and the examples of [Part 12](#part-12-a-closer-look-at-hypothesis-c)) are checked by [`checks/check_guide_example.py`](checks/check_guide_example.py).

The paper's own status note applies here too. The Corrigan–Zambon conjecture is not proved. The general statements were corrected after an independent check on 20 October 2026, and the corrected versions await a second check ([response_to_reports_20261020.md](response_to_reports_20261020.md)).

## How to read this guide

The guide assumes classical mechanics (Hamilton's equations), basic Lagrangian field theory and Fourier analysis. Everything else is explained when it is first needed.

- **Parts 1–2** state the question and the strategy, in words.
- **Part 3** explains the central idea in classical mechanics with finitely many degrees of freedom, where every step is an ordinary partial derivative. The whole of the paper's first main theorem is already visible there.
- **Part 4** is a toolkit: the notation and standard facts of the calculus of local expressions that the paper uses, each with a small example. Skip it and come back when a later part points to an item such as [T3](#t3-the-euler-operator).
- **Part 5** is the running example, sine-Gordon, used throughout.
- **Parts 6–10** follow the paper's Sections 2–7. Each is written in up to three layers:
  - **Idea.** What the step achieves and why the chain needs it.
  - **How the proof goes.** The argument, move by move, in the paper's notation.
  - **Fine print.** Why each hypothesis is there, with the paper's counterexample.
- **Part 11** assembles the main theorem, and **Part 12** looks closely at hypothesis (C), where integrability enters: how strong it is, how to check it, and whether it could follow from momentum conservation.
- **Parts 13–16** read the table of cases, list what is open, collect the counterexamples and say where each statement is checked.
- **Part 17** says, link by link, which ideas the paper takes from the literature and which tools it brings in.

For a short overview, read Parts 1–3 and the **Idea** paragraphs of Parts 6–10.

## Contents

1. [The question](#part-1-the-question)
2. [The strategy: four links](#part-2-the-strategy-four-links)
3. [The guiding picture: a jump in classical mechanics](#part-3-the-guiding-picture-a-jump-in-classical-mechanics)
4. [A toolkit for local field theory](#part-4-a-toolkit-for-local-field-theory)
5. [The running example: sine-Gordon](#part-5-the-running-example-sine-gordon)
6. [The spatial phase space (§2)](#part-6-the-spatial-phase-space-2)
7. [Link 1: momentum conservation gives a Bäcklund relation (§3)](#part-7-link-1-momentum-conservation-gives-a-bäcklund-relation-3)
8. [Link 2: one conserved density along the relation (§4, §5.1)](#part-8-link-2-one-conserved-density-along-the-relation-4-51)
9. [Link 3: a family and its transparent limit (§5.2, §6)](#part-9-link-3-a-family-and-its-transparent-limit-52-6)
10. [Link 4: involution and independence (§7)](#part-10-link-4-involution-and-independence-7)
11. [The main theorem, hypothesis by hypothesis (§8)](#part-11-the-main-theorem-hypothesis-by-hypothesis-8)
12. [A closer look at hypothesis (C)](#part-12-a-closer-look-at-hypothesis-c)
13. [Reading the table of cases (§9)](#part-13-reading-the-table-of-cases-9)
14. [What is open (§10)](#part-14-what-is-open-10)
15. [Catalogue of counterexamples](#part-15-catalogue-of-counterexamples)
16. [Where each statement is checked](#part-16-where-each-statement-is-checked)
17. [What comes from the literature, and what the paper brings in](#part-17-what-comes-from-the-literature-and-what-the-paper-brings-in)

---

## Part 1. The question

A **jump defect** joins two field theories in one space and one time dimension at the point $x=0$. The field is called $\phi(x,t)$ on the left, $x<0$, and $\psi(x,t)$ on the right, $x>0$. The total action is

$$S=\int dt\int_{-\infty}^0dx\,\mathcal L_-(\phi)+\int dt\int_0^\infty dx\,\mathcal L_+(\psi)+\int dt\,\mathcal L_d .$$

The **defect Lagrangian** $\mathcal L_d$ depends on the values of $\phi$ and $\psi$ at $x=0$ and on their time derivatives there. It may also depend on extra fields that live only on the defect. Varying the action gives the bulk field equations on each side and, at $x=0$, **sewing conditions** that say how $\phi$ and $\psi$ are joined.

A defect that does not depend on time conserves energy automatically. It breaks translations in $x$, so momentum is in general not conserved: a wave hitting the defect can push it. One can ask for a corrected momentum $P_-+P_++P_d$ to be conserved, where $P_-$ and $P_+$ are the field momenta on the two sides and $P_d$ is a local expression in the fields at the defect. This is a strong condition on $\mathcal L_d$, and it even restricts which bulk theories can be used.

Bowcock, Corrigan and Zambon found that for the sine-Gordon equation the condition can be met. The resulting sewing conditions turned out to be a **Bäcklund transformation**, a classical device of integrable systems (see [T9](#t9-bäcklund-transformations)), imposed only at one point. Corrigan and Zambon then found the same in every model they examined: sine-Gordon, Liouville, affine and conformal Toda, Tzitzéica, the nonlinear Schrödinger equation (NLS), KdV, mKdV and Boussinesq (the table in §1.1). In each case momentum conservation was possible only if

1. the sewing conditions were a Bäcklund transformation, and
2. the bulk theory was integrable.

They said no direct proof was known. This is the **Corrigan–Zambon observation**.

Half of it is unsurprising. Integrable theories have Bäcklund transformations, and Bäcklund transformations are known to generate conservation laws. What needs explaining is the direction of the implication. A single conservation law, momentum, seems to force infinitely many.

The paper proves as much of this as it can in general, and isolates the one step it cannot prove.

---

## Part 2. The strategy: four links

The paper breaks the implication into four links (§1.2):

```
  momentum-conserving defect S_d
          │
          │  Link 1  (§3, Theorem 3.3)        needs: injectivity condition (I)
          ▼
  the sewing relation, imposed at every x, is a Bäcklund relation
          │
          │  Link 2  (§4, §5.1)               needs: an affine conservation law
          ▼                                           (Lorentz boost, Galilean boost, dilation, …)
  one conserved "generating density" G along the relation
          │
          │  Link 3  (§5.2, §6)               needs: a one-parameter family of defects
          ▼                                           with a regular transparent limit
  infinitely many local conservation laws Q_n          ◄── integrability enters here
          │
          │  Link 4  (§7)                     needs: constant Poisson operator,
          ▼                                           nonresonant dispersion, conditions (L)
  infinitely many independent charges in involution    (Theorem 8.1)
```

In words:

1. **Link 1.** If momentum is conserved, the sewing conditions can be imposed at *every* point $x$, not just at the defect. Imposed everywhere, they turn solutions of one theory into solutions of the other. That is what a Bäcklund relation is.
2. **Link 2.** Along such a relation, one particular expression built from the defect, such as the energy stored in the defect, becomes a conserved density.
3. **Link 3.** If the defect comes in a one-parameter family that becomes invisible ("transparent") as the parameter goes to zero, then expanding that one density in powers of the parameter gives infinitely many conserved densities.
4. **Link 4.** Under conditions on the dispersion relation of the bulk theory, these conserved quantities Poisson-commute and are independent. That is integrability in the sense of Liouville.

**Why four links and not one.** Each link uses a different kind of mathematics. Link 1 is Hamiltonian mechanics with $x$ playing the role of time. Link 2 is Noether's theorem. Link 3 is perturbation theory in a small parameter. Link 4 is Fourier analysis of the dispersion relation. Each link can also fail on its own; [Part 15](#part-15-catalogue-of-counterexamples) gives an example for each. [Part 17](#part-17-what-comes-from-the-literature-and-what-the-paper-brings-in) says which ideas in each link come from the literature and which tools the paper brings in.

**The main message.** Links 1, 2 and 4 hold for theories that are not integrable. Every massive relativistic scalar theory satisfies the bulk hypotheses of Links 2 and 4, whatever its potential. Only Link 3, hypothesis (C) of Theorem 8.1, carries integrability. The paper therefore reduces the conjecture to one statement: *momentum conservation implies hypothesis (C)*. That statement is open in general (§10). §8.2 proves it in part for one class of relativistic defects ([§11.2](#112-hypothesis-c-for-relativistic-type-i-defects-82)); [Part 12](#part-12-a-closer-look-at-hypothesis-c) discusses how strong (C) is and how it might follow.

**A dictionary.** The paper's main objects, and what they mean. Each is explained properly later.

| paper | meaning |
|---|---|
| spatial phase space, $z=(\Phi,\pi)$ (§2.2) | the data needed to evolve the field in the $x$ direction: the field and its "momentum" as functions of $t$ at a fixed $x$ |
| spatial Hamiltonian $\mathcal H^{(x)}$ (2.6) | the generator of evolution in $x$; it equals minus the momentum flux (Lemma 2.1) |
| sewing correspondence $\Gamma_d$ (§3.1) | the set of left and right data that the defect allows to sit next to each other |
| momentum balance (3.3) | "momentum flowing in equals momentum flowing out, up to what is stored in the defect", as an identity |
| promoted solution (§3.1) | fields satisfying the sewing conditions at every $x$, not only at $x=0$ |
| defect charge $Q_d$ (4.1) | the defect's contribution that makes a bulk charge conserved |
| affine conservation law (Def. 5.1) | a conserved current that contains $x$ and $t$ explicitly, such as that of a Lorentz boost |
| generating density $\mathcal G$ (§4.3) | a defect charge that is itself a conserved density along promoted solutions |
| formal branch (Def. 6.1) | $\psi$ written as a power series in the family parameter $\epsilon$, with coefficients that are local expressions in $\phi$ |
| quadratic symbol $m_n(k)$ (§7) | the quadratic part of the charge $Q_n$, as a function of wavenumber $k$ |
| nonresonance (NR) (Def. 7.1) | no continuous family of resonant wave interactions |

---

## Part 3. The guiding picture: a jump in classical mechanics

**The idea in one paragraph.** The defect sits at a point in $x$. So it is natural to think of $x$ as "time" and to describe the field as evolving in the $x$ direction. In that description, the defect is an instantaneous event at "time" $x=0$, at which the state of the field jumps from the left values to the right values. Momentum is the conserved quantity of translations in $x$. When $x$ plays the role of time, momentum therefore plays the role of *energy*. Momentum conservation at the defect becomes the statement that the jump conserves energy. This part explains, in ordinary classical mechanics, why a jump that conserves energy is special.

In this part only, the time variable of the mechanical system is called $s$, to keep it apart from the field theory's $t$. The translation back to field theory is in [§3.5](#35-back-to-field-theory).

### 3.1 Hamilton's equations

A mechanical system has coordinates $q=(q_1,\dots,q_n)$ and momenta $p=(p_1,\dots,p_n)$. A Hamiltonian $H(q,p)$ determines the motion through Hamilton's equations,

$$\dot q=\frac{\partial H}{\partial p},\qquad \dot p=-\frac{\partial H}{\partial q},$$

where a dot is $d/ds$. It helps to give the two right-hand sides names, as the paper does. Write

$$a=\frac{\partial H}{\partial p}\quad\text{(the velocity)},\qquad b=\frac{\partial H}{\partial q}\quad\text{(minus the force)}.$$

Then Hamilton's equations say: in a short time $ds$ the state moves by $(\delta q,\delta p)=(a,-b)\,ds$. The pair $(a,-b)$ is called the **Hamiltonian vector field** $X$. It is the velocity of the state in phase space.

The first equation, $\dot q=a$, is usually not new information. If $H$ came from a Lagrangian by the Legendre transform, then $\dot q=\partial H/\partial p$ just inverts the definition $p=\partial L/\partial\dot q$. Only the second equation, $\dot p=-b$, is the actual equation of motion. Keep this in mind; it is the content of the paper's Lemma 2.2.

### 3.2 A jump described by an action

Now let the system evolve with a Hamiltonian $H_-$ for $s<0$. At $s=0$ the state jumps from $(q,p)$ to a new state $(Q,P)$, and for $s>0$ it evolves with a Hamiltonian $H_+$. The two Hamiltonians may differ. Describe the jump by adding a function $S(q,Q)$ of the old and new coordinates to the action:

$$\int_{-\infty}^0\big(p\,\dot q-H_-\big)\,ds+\int_0^\infty\big(P\,\dot Q-H_+\big)\,ds+S\big(q(0),Q(0)\big).$$

Vary $q(0)$ and $Q(0)$. The first integral contributes the boundary term $p\cdot\delta q(0)$, the second contributes $-P\cdot\delta Q(0)$, and $S$ contributes $\partial S/\partial q\cdot\delta q+\partial S/\partial Q\cdot\delta Q$. Setting the total to zero gives the **jump rule**

$$p=-\frac{\partial S}{\partial q}(q,Q),\qquad P=\frac{\partial S}{\partial Q}(q,Q).$$

This is the finite-dimensional version of the paper's sewing equations (3.1), with $S$ in the role of the defect action $S_d$.

The jump rule is easiest to think of as a *relation*: for each choice of the coordinates $q$ and $Q$, it tells you which momenta $p$ and $P$ go with them. Call the set of all allowed pairs of states $\big((q,p),(Q,P)\big)$ the **jump relation** $\Gamma$. It is parametrised by $(q,Q)$. If the matrix $\partial^2S/\partial q\,\partial Q$ is invertible, one can also solve the jump rule for $(Q,P)$ in terms of $(q,p)$. Then the jump is a map from old states to new states. Maps produced this way are the **canonical transformations** of classical mechanics, and $S$ is (up to sign) their **generating function of type 1**. The paper never needs to solve for the map, so it works with the relation.

Two examples will be useful.

- *A stiff spring.* $S=-(q-Q)^2/(2\epsilon)$. The jump rule gives $p=P=(q-Q)/\epsilon$, so $P=p$ and $Q=q-\epsilon p$. The jump keeps the momentum and shifts the position backwards by $\epsilon p$.
- *An oscillator flow.* For $H=\frac12(p^2+q^2)$ and a fixed angle $\alpha$, take $S=\big((q^2+Q^2)\cos\alpha-2qQ\big)/(2\sin\alpha)$. The jump rule gives $Q=q\cos\alpha+p\sin\alpha$ and $P=-q\sin\alpha+p\cos\alpha$. The jump is the oscillator's own motion for a time $\alpha$.

### 3.3 Energy-conserving jumps are symmetries

Say that the jump **conserves energy** if $H_-(q,p)=H_+(Q,P)$ for every allowed pair. Because the allowed pairs are parametrised by $(q,Q)$, this says that the function

$$h(q,Q)=H_-\big(q,\,-\partial_qS\big)-H_+\big(Q,\,\partial_QS\big)$$

vanishes identically in $q$ and $Q$. (The paper's version, (3.3), allows the difference to be a total time derivative; [§3.5](#35-back-to-field-theory) explains why.)

In the first example, with $H_-=H_+=p^2/2$ (a free particle), energy is conserved because $P=p$. With a potential, $H=p^2/2+V(q)$, it is not, because $V(q)\ne V(q-\epsilon p)$ in general. In the second example energy is conserved because the oscillator's motion conserves energy.

> **Fact.** If a jump conserves energy, then it is a symmetry: if $(q,p)$ and $(Q,P)$ are allowed partners at one moment, and each is evolved with its own Hamiltonian, they remain allowed partners at all later moments. Equivalently, jumping and then evolving gives the same result as evolving and then jumping.

In the free-particle example the Fact says: shifting a free trajectory back by $\epsilon p$ gives another free trajectory, which is clearly true. In the oscillator example it says that waiting for a time $\alpha$ commutes with the motion.

*Proof, by differentiating $h$.* Since $h\equiv0$, its partial derivatives vanish. Write $a_\mp,b_\mp$ for the velocity and minus-force of each side, evaluated at the allowed pair, and write $S_{qQ}$ for $\partial^2S/\partial q\,\partial Q$ and so on. The chain rule gives

$$\frac{\partial h}{\partial q}=b_--S_{qq}\,a_--S_{Qq}\,a_+=0,\qquad \frac{\partial h}{\partial Q}=-S_{qQ}\,a_--b_+-S_{QQ}\,a_+=0 .$$

Now move both states by their Hamiltonian velocities: $\delta q=a_-$ and $\delta Q=a_+$. By how much must the momenta change for the pair to stay allowed? Differentiate the jump rule:

$$\delta p=-S_{qq}\,\delta q-S_{qQ}\,\delta Q,\qquad \delta P=S_{Qq}\,\delta q+S_{QQ}\,\delta Q .$$

Insert $\delta q=a_-$, $\delta Q=a_+$, and use the two equations above together with $S_{qQ}=S_{Qq}$ (mixed partial derivatives commute). The result is

$$\delta p=-b_-,\qquad \delta P=-b_+ .$$

These are exactly the momentum changes that Hamilton's equations prescribe. So the displacement $(a_-,-b_-;\,a_+,-b_+)$, which is how the two states actually move in a short time, keeps the pair allowed. In geometric language: the pair of Hamiltonian vector fields is **tangent** to $\Gamma$. A curve whose velocity is always tangent to $\Gamma$ stays in $\Gamma$, which proves the Fact. $\square$

There are three ingredients: differentiate the energy identity; use the symmetry of the second derivatives of $S$; read the result as "the Hamiltonian motion keeps the pair allowed". The paper's proof of Theorem 3.3(a) has exactly these three moves ([§7.3](#73-the-bäcklund-theorem-33)).

### 3.4 The converse half, and what can go wrong

The Fact has a second half, which becomes Theorem 3.3(b). Suppose now that the jump rule is imposed at *every* moment $s$, not only at $s=0$. That is, we have curves $q(s)$ and $Q(s)$, we define $p(s)$ and $P(s)$ from them by the jump rule at each $s$, and we know only the velocity equations $\dot q=a_-$ and $\dot Q=a_+$. Do both curves solve Hamilton's equations?

Yes. Differentiate the jump rule along the curve:

$$\dot p=-S_{qq}\,\dot q-S_{qQ}\,\dot Q=-S_{qq}\,a_--S_{qQ}\,a_+=-b_- ,$$

by the first equation for $\partial h/\partial q$. In the same way $\dot P=-b_+$. Both force equations follow. In field theory the velocity equations hold automatically ([§3.1](#31-hamiltons-equations)), so the sewing relation imposed at every point produces two genuine solutions.

**Auxiliary variables.** Some defects contain extra variables that live only on the defect: extra fields (Type II defects) or Lagrange multipliers. In the toy model, let $S=S(q,Q,\lambda)$ depend on an extra variable $\lambda$ with no momentum of its own. The jump rule gains a constraint $C:=\partial S/\partial\lambda=0$. The energy condition now only needs to hold where the constraint holds, so it reads $h=\rho\,C$ for some function $\rho(q,Q,\lambda)$. Differentiating, and using $C=0$, gives three equations instead of two:

$$\begin{aligned}
b_--S_{qq}a_--S_{qQ}a_+&=S_{q\lambda}\,\rho,\\
-S_{Qq}a_--b_+-S_{QQ}a_+&=S_{Q\lambda}\,\rho,\\
-S_{\lambda q}a_--S_{\lambda Q}a_+&=S_{\lambda\lambda}\,\rho .
\end{aligned}$$

These are the paper's equations (3.5), letter for letter. The forward argument works as before if one also moves $\lambda$ by $\delta\lambda=\rho$: the extra variable must change at the rate $\rho$ for the pair to stay allowed.

The converse half can now fail. Along a curve on which the jump rule holds at every $s$, differentiating gives

$$\dot p=-b_--S_{q\lambda}\,\kappa,\qquad \dot P=-b_++S_{Q\lambda}\,\kappa,\qquad 0=S_{\lambda\lambda}\,\kappa,\qquad \kappa:=\dot\lambda-\rho .$$

Nothing forces $\lambda$ to change at the right rate. The mismatch $\kappa$ spoils the force equations unless the last equation forces $\kappa=0$. This is the origin of the paper's injectivity condition (I). In the toy model, (I) says that $S_{\lambda\lambda}$ is invertible. In field theory there are further equations that can detect $\kappa$ (§3.3).

*An example of the failure.* Take $H_\pm=\frac12(p^2+q^2)$ and $S=\lambda(q+Q)$. The jump rule gives $p=-\lambda$, $P=\lambda$ and the constraint $Q=-q$, so the jump is the reflection $(q,p)\mapsto(-q,-p)$, and $h=\frac12(q-Q)\,C$: energy is conserved. Here $S_{\lambda\lambda}=0$, so (I) fails. Indeed $q=s^2$, $Q=-s^2$, $\lambda=-2s$ satisfies the jump rule at every $s$ and both velocity equations, but $\ddot q+q=s^2+2\ne0$: it is not a solution. This is the toy version of the paper's Remark 3.4.2.

### 3.5 Back to field theory

Here is the translation. The paper sets it up in §2 and uses it in §3.

| toy model | field theory with $x$ as "time" |
|---|---|
| time $s$ | position $x$ |
| coordinates $q_1,\dots,q_n$ | the field at fixed $x$ as a function of $t$: one coordinate $\phi(t)$ for each instant $t$ (and $\phi_x(t),\dots$ for higher-derivative theories) |
| momenta $p$ | the "spatial momenta" $\pi(t)$, for example $\pi=\partial\mathcal L/\partial\phi_x$ |
| Hamiltonian $H(q,p)$ | $H^{(x)}=\int dt\,\mathcal H^{(x)}$, an integral over $t$ of a density built from $\phi$, its $t$-derivatives and $\pi$ |
| a sum over $i$ | an integral over $t$ |
| partial derivative $\partial H/\partial q_i$ | functional derivative $\delta H^{(x)}/\delta\phi(t)$, computed by the Euler operator ([T3](#t3-the-euler-operator)) |
| energy $H$ | momentum (more precisely, minus the momentum flux, Lemma 2.1) |
| jump action $S(q,Q,\lambda)$ | defect action $S_d=\int dt\,\mathcal L_d$ |
| matrix of second derivatives $S_{qQ}$ | linearisation of the sewing equations, a differential operator in $t$ ([T4](#t4-linearisation-and-adjoints)) |
| $S_{qQ}=S_{Qq}$ | the second variation of $S_d$ is self-adjoint ([T5](#t5-symmetry-of-second-variations-helmholtz)) |
| $h\equiv0$ | $\mathcal H_--\mathcal H_+=D_t(\dots)$, a total time derivative (Definition 3.1) |
| jump rule at every $s$ | sewing conditions at every $x$: a promoted solution, that is, a Bäcklund relation |

Three points need comment.

1. **Why "up to a total time derivative".** In field theory the Hamiltonians are integrals over $t$. The integral of a total derivative $D_tB$ vanishes for histories that settle down as $t\to\pm\infty$. So equality of the integrals only requires the densities to agree up to such a term. The Euler operator, which replaces the partial derivative, annihilates total derivatives ([T3](#t3-the-euler-operator)), so the proof does not see them.
2. **Why "off shell".** In the toy model, $h$ must vanish for *all* $q$ and $Q$, not only along actual motions. In field theory, the data for evolution in $x$ at the point $x=0$ are arbitrary histories in $t$. So the momentum balance must hold for all boundary histories allowed by the defect, not only for those of solutions. This is how Corrigan and Zambon impose it, and it is Definition 3.1.
3. **What is not needed.** The toy proof used only the symmetry of second derivatives. It did not need the jump to be invertible, nor any further geometry. The same is true of the paper's proof. In geometric language, the jump relation of a generating function is a *Lagrangian submanifold* (a canonical relation); the paper's Appendix A gives the geometric proof for readers who know that language, but the main text does not need it.

---

## Part 4. A toolkit for local field theory

This part collects the notation and standard facts that the paper uses without comment. Each item has an example. Olver's *Applications of Lie Groups to Differential Equations* (the paper's reference [16]) is the standard source.

### T1. Fields, derivatives and local functions

A field $\phi(x,t)$ may have several components; complex fields such as the NLS field $u$ are treated as two independent fields $u$ and $\bar u$. Derivatives are written $\phi_x,\ \phi_{tt},\dots$, or in general $\phi_{a,k}=\partial_t^a\partial_x^k\phi$.

A **local function** (Olver: *differential function*) is a function of finitely many of these derivatives, such as $\frac12\phi_t^2-\frac12\phi_x^2-U(\phi)$ or $\phi\,\phi_{xxx}$. A **local functional** is the integral of a local function, such as $\int\phi_x^2\,dx$.

The key convention of the "formal variational calculus" is to treat $\phi,\phi_x,\phi_t,\phi_{xx},\dots$ as *independent variables*. An identity between local functions that holds for all values of these variables holds for every field. Such an identity is said to hold **off shell**. An identity that holds only when the field equations are used holds **on shell**.

### T2. Total derivatives

The **total derivative** $D_x$ of a local function is its $x$-derivative when a field is substituted, computed by the chain rule:

$$D_xf=\frac{\partial f}{\partial x}\Big|_{\text{explicit}}+\sum_{a,k}\frac{\partial f}{\partial\phi_{a,k}}\,\phi_{a,k+1}.$$

For example, $D_t\big(\tfrac12\phi_t^2\big)=\phi_t\phi_{tt}$ and $D_x U(\phi)=U'(\phi)\phi_x$. The paper's Lagrangians have no explicit $x$ or $t$, so the first term is absent except in §5.

$\operatorname{Im}D_t$ (the "image of $D_t$") is the set of all local functions of the form $D_tB$ with $B$ local. Writing $f\in\operatorname{Im}D_t$ means: $f$ is a total time derivative. Its integral over $t$ is then a boundary term.

### T3. The Euler operator

For a local function $f$, the **Euler operator** (or variational derivative) is

$$E(f)=\sum_{a,k}(-D_t)^a(-D_x)^k\,\frac{\partial f}{\partial\phi_{a,k}} .$$

It is the functional derivative: $\delta\int f=\int E(f)\cdot\delta\phi$ up to boundary terms. The field equation of a Lagrangian $\mathcal L$ is $E(\mathcal L)=0$. The paper also uses the **time-Euler operator** $E^{(t)}$, written $E_Y$ when it acts on the variables $Y$. It involves only $t$-derivatives and acts on functions of $t$-histories at a fixed $x$. For example

$$E^{(t)}_\phi\Big(-\tfrac12\phi_t^2+U(\phi)\Big)=U'(\phi)+\phi_{tt}.$$

Two facts make the Euler operator the right tool:

1. It annihilates total derivatives: $E(D_tB)=0$ for every local $B$.
2. Conversely, a local function whose Euler derivative is zero is a total derivative plus a constant (locally; Olver, Thm 4.7).

So "$f$ is a total derivative" can be tested by computing $E(f)$. In the toy model of Part 3 the analogue is: a function is constant if and only if its gradient vanishes.

### T4. Linearisation and adjoints

The **linearisation** (Fréchet derivative) of a local function $F$ is the operator $D_F$ that gives its first-order change:

$$D_F[\eta]=\frac{d}{d\varepsilon}F[\phi+\varepsilon\eta]\Big|_{\varepsilon=0}=\sum_{a,k}\frac{\partial F}{\partial\phi_{a,k}}\,D_t^aD_x^k\eta .$$

It is a differential operator acting on $\eta$. For example, the linearisation of $\phi_{tt}+U'(\phi)$ is $\eta\mapsto\eta_{tt}+U''(\phi)\eta$.

The **adjoint** $D^*$ of a differential operator $D$ is defined by integration by parts: $\int g\cdot(D\eta)=\int(D^*g)\cdot\eta$ up to boundary terms. So $(D_t)^*=-D_t$, $(D_t^2)^*=D_t^2$, and multiplication by a function is its own adjoint. The adjoint is the infinite-dimensional analogue of the transpose of a matrix.

The **chain rule for Euler operators** is the analogue of the rule $\nabla_y f(z(y))=(\partial z/\partial y)^{T}\,\nabla_zf$ for gradients. If $z=Z[Y]$ is a local change of variables, then

$$E_Y(F\circ Z)=D_Z^*\big(E_zF\circ Z\big).$$

The paper uses it in Move 1 of Theorem 3.3 ([§7.3](#73-the-bäcklund-theorem-33)).

### T5. Symmetry of second variations (Helmholtz)

In finite dimensions the matrix of second derivatives of a function is symmetric. The infinite-dimensional statement is: *the linearisation of an Euler–Lagrange expression is self-adjoint.* For example, $E(\frac12\phi_t^2-U)=-\phi_{tt}-U'(\phi)$ has linearisation $\eta\mapsto-\eta_{tt}-U''(\phi)\eta$, which equals its own adjoint. These are the **Helmholtz conditions** (Olver, Thm 5.92). In the paper, $\mathcal S$ is the linearisation of the defect's Euler–Lagrange expression, with blocks $S_{AB}$ for $A,B\in\{\Phi,\Psi,\lambda\}$, and self-adjointness reads $S_{AB}^*=S_{BA}$. It plays the role of $S_{qQ}=S_{Qq}$ in Part 3.

### T6. Conservation laws, charges and Noether's theorem

A **conservation law** is a pair of local functions, a density $N$ and a flux $J$, with

$$D_tN+D_xJ=0\quad\text{on shell}.$$

If the fields decay at infinity, the **charge** $\int N\,dx$ is then constant in time. Near a defect at $x=0$, the charge on the left half-line changes by the flux through the defect: $\frac d{dt}\int_{-\infty}^0N\,dx=-J|_{x=0^-}$.

A **trivial** conservation law has $N=D_x\nu$ and $J=-D_t\nu$ for a local $\nu$. It holds for every field, on shell or not, and its charge is a boundary term. It carries no information.

It is often useful to package a conservation law as the 1-form $N\,dx-J\,dt$ in the $(x,t)$ plane. The law says exactly that this 1-form is closed: $d(N\,dx-J\,dt)=(D_tN+D_xJ)\,dt\wedge dx=0$. A closed 1-form is locally the differential of a function $Q$: $N=D_xQ$ and $J=-D_tQ$. Defect charges will turn out to be such potentials ([§8.2](#82-defect-charges-as-potentials-42)).

**Noether's theorem** gives a conservation law for each continuous symmetry of the Lagrangian: time translation gives energy, space translation gives momentum, a phase rotation gives particle number.

### T7. Energy, momentum and the stress tensor

The densities and fluxes of energy and momentum form the **stress tensor** $T^{\mu\nu}$. The second index says which quantity, the first says density or flux:

| | density | flux |
|---|---|---|
| energy | $T^{00}$ | $T^{10}$ |
| momentum | $T^{01}$ | $T^{11}$ |

Conservation reads $D_tT^{0\nu}+D_xT^{1\nu}=0$ for $\nu=0,1$. For a scalar field with $\mathcal L=\frac12(\phi_t^2-\phi_x^2)-U(\phi)$, in the paper's conventions,

$$T^{00}=\tfrac12(\phi_t^2+\phi_x^2)+U,\qquad T^{01}=T^{10}=-\phi_t\phi_x,\qquad T^{11}=\tfrac12(\phi_t^2+\phi_x^2)-U .$$

The momentum flux $T^{11}$ is the pressure. The equality $T^{10}=T^{01}$, energy flux equals momentum density, is a consequence of Lorentz invariance. The Noether current of a Lorentz boost has density $xT^{00}-tT^{01}$ and flux $xT^{10}-tT^{11}$, and its conservation is equivalent to $T^{10}=T^{01}$. Link 2 is built on this fact.

In Lorentz-invariant theories it is convenient to parametrise the energy and momentum of a particle of mass $m$ by the **rapidity** $\vartheta$: $k=m\sinh\vartheta$, $\omega=m\cosh\vartheta$. A Lorentz boost shifts every rapidity by the same amount.

### T8. Defects

A defect Lagrangian $\mathcal L_d$ depends on the boundary values $\Phi=\phi(0^-,t)$ and $\Psi=\psi(0^+,t)$ and their $t$-derivatives. For higher-derivative bulk theories it also depends on the boundary values of $\phi_x,\psi_x,\dots$. Corrigan and Zambon distinguish

- **Type I** defects, which involve only the boundary values of the two bulk fields;
- **Type II** defects, which carry an additional field $\lambda(t)$ living on the defect.

Some defects also contain **Lagrange multipliers**: auxiliary variables that appear linearly and enforce a constraint. The paper collects all such extra variables into $\lambda$. Varying $\lambda$ gives the constraint $C=E^{(t)}_\lambda\mathcal L_d=0$.

"Modulo the constraint" is written $\pmod{\langle C\rangle}$. Here $\langle C\rangle$ is the **differential ideal** generated by $C$: all expressions $\sum_kf_k\,D_t^kC$ with local coefficients $f_k$. If $C=0$ at every time, then all its time derivatives vanish too, so every element of $\langle C\rangle$ vanishes. The **prolonged constraint locus** is the set where $C$ and all its time derivatives vanish.

### T9. Bäcklund transformations

A **Bäcklund transformation** is a pair of relations between two fields $\phi$ and $\psi$, involving only low-order derivatives, with this property: if the relations hold at every point, then $\phi$ and $\psi$ both solve their field equations. Given a solution $\phi$, solving the relations for $\psi$ gives a new solution. For sine-Gordon, the classical example is

$$\phi_x=\psi_t-\partial_\phi\mathcal B,\qquad \psi_x=\phi_t+\partial_\psi\mathcal B,$$

with the function $\mathcal B$ of [Part 5](#part-5-the-running-example-sine-gordon). The usual proof cross-differentiates the two relations. The relations also contain a free parameter, $\sigma$ here, often called the **spectral parameter**. Expanding a Bäcklund transformation in its spectral parameter is a classical way of producing infinitely many conservation laws.

The paper uses **Bäcklund relation** for the sewing conditions imposed at every $x$, and **promoted solution** for fields that satisfy them everywhere.

### T10. Hamiltonian field equations and Poisson brackets

Many field equations have the form

$$v_t=\mathcal J\,\frac{\delta H}{\delta v},$$

with a Hamiltonian functional $H$ and a skew-adjoint operator $\mathcal J$, the **Poisson operator**. Two examples:

- *KdV.* $v=u$, $\mathcal J=D_x$ and $H=\int(u^3+\frac12u_x^2)\,dx$. Then $\delta H/\delta u=3u^2-u_{xx}$ and $u_t=6uu_x-u_{xxx}$.
- *Relativistic scalar.* $v=(\phi,p)$ with $p=\phi_t$, $\mathcal J=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and $H=\int\big(\frac12p^2+\frac12\phi_x^2+U(\phi)\big)\,dx$. Then $\phi_t=p$ and $p_t=\phi_{xx}-U'(\phi)$.

The **Poisson bracket** of two local functionals is

$$\{F,G\}=\int\frac{\delta F}{\delta v}\cdot\mathcal J\,\frac{\delta G}{\delta v}\,dx .$$

A functional $F$ is conserved exactly when $\{F,H\}=0$. Two conserved functionals are **in involution** when their bracket vanishes. The bracket of two conserved functionals is again conserved, by the Jacobi identity: $\{\{F,G\},H\}=\{F,\{G,H\}\}-\{G,\{F,H\}\}=0$. A **Casimir** is a functional whose bracket with everything vanishes. For $\mathcal J=D_x$, $\int u\,dx$ is a Casimir, because $\delta\int u/\delta u=1$ and $D_x1=0$.

Functionals are **functionally independent** if their gradients $\delta F/\delta v$ are linearly independent at generic points, as for functions on $\mathbb R^n$. A field theory with infinitely many independent local conserved charges in involution is **integrable** in the sense used by the paper.

**Degrees.** Expand a functional in powers of the fields around the vacuum $v=0$: $F=F_0+F_1+F_2+\dots$, where $F_n$ is homogeneous of degree $n$. If $\mathcal J$ has constant coefficients, then $\delta F_a/\delta v$ has degree $a-1$, and $\{F_a,G_b\}$ has degree exactly $a+b-2$. Link 4 runs on this degree counting.

### T11. Plane waves, dispersion and quadratic symbols

Linearise the field equation around the vacuum. For $\phi_{tt}-\phi_{xx}+m^2\phi=0$, the plane wave $e^{i(kx-\omega t)}$ is a solution exactly when $\omega^2=k^2+m^2$. The function $\omega(k)$ is the **dispersion relation**; for several fields there are several branches $\omega_j(k)$. The Fourier amplitudes that evolve simply, $a_j(k,t)=a_j(k)\,e^{-i\omega_j(k)t}$, are the **normal modes**.

A product of $n$ normal modes, some of them complex-conjugated, oscillates in time like $e^{-i\Omega t}$, where $\Omega$ is the sum of the frequencies with signs: $+\omega$ for each $a$ and $-\omega$ for each $\bar a$. Its total momentum is the corresponding signed sum of the wavenumbers. A local functional of degree $n$ only contains products whose total momentum is zero, because it is an integral over $x$.

The **quadratic symbol** $m(k)$ of a functional is its quadratic part written in Fourier space, roughly $F_2=\int m(k)\,\lvert a(k)\rvert^2\,dk$. It can be found from one plane wave. Insert $\phi=\eta\,(aE+\bar a\bar E)$, with $E=e^{ikx}$, into the density and average over $x$. Terms containing $E^2$ or $\bar E^2$ average to zero. What remains at order $\eta^2$ is $\eta^2\lvert a\rvert^2m(k)$. For example, $\frac12\int\phi^2$ has symbol $1$, and $\frac12\int\phi_x^2$ has symbol $k^2$. A total $x$-derivative averages to zero, so a density with nonzero symbol is never trivial.

### T12. Formal power series

A **formal** power series $\sum_n\epsilon^nc_n$ is handled coefficient by coefficient, without asking whether it converges. The paper's series have coefficients that are local functions of a field. Such series can often be found by solving order by order. For example, the equation $\Delta=\epsilon\,(u+\Delta_x)$ for an unknown $\Delta$ has the solution $\Delta=\epsilon u+\epsilon^2u_x+\epsilon^3u_{xx}+\dots$. Each coefficient is local, because at each order the unknown appears without derivatives and the derivatives act only on lower coefficients. By contrast, $\Delta_x=u$ has the solution $\Delta=\int^xu$, which is not local. Lemma 6.2 is the general form of this observation.

---

## Part 5. The running example: sine-Gordon

This example runs through every link. All formulas are checked in [`checks/check_guide_example.py`](checks/check_guide_example.py).

**Bulk.** $\mathcal L=\tfrac12(\phi_t^2-\phi_x^2)-U(\phi)$ with $U=1-\cos\phi$, so the mass is $1$. The field equation is $\phi_{tt}-\phi_{xx}+\sin\phi=0$.

For evolution in $x$, the "velocity" is $\phi_x$. Its conjugate momentum is $\pi=\partial\mathcal L/\partial\phi_x=-\phi_x$. The spatial Hamiltonian density is the Legendre transform with respect to $\phi_x$,

$$\mathcal H^{(x)}=\pi\,\phi_x-\mathcal L=-\tfrac12\pi^2-\tfrac12\phi_t^2+U(\phi).$$

Hamilton's equations in $x$ are, in the language of Part 3:

- the velocity equation $D_x\phi=\partial\mathcal H/\partial\pi=-\pi$, which only restates the definition of $\pi$;
- the force equation $D_x\pi=-E^{(t)}_\phi\mathcal H=-(\phi_{tt}+U'(\phi))$, which is the field equation $\phi_{xx}=\phi_{tt}+U'(\phi)$.

The Euler derivative appears because $\mathcal H$ contains $\phi_t$ ([T3](#t3-the-euler-operator)).

**Defect** of Bowcock, Corrigan and Zambon [1]:

$$\mathcal L_d=\tfrac12(\phi\psi_t-\psi\phi_t)-\mathcal B(\phi,\psi),\qquad \mathcal B=f+g,\quad f=2\sigma\big(1-\cos\tfrac{\phi+\psi}2\big),\quad g=\tfrac2\sigma\big(1-\cos\tfrac{\phi-\psi}2\big).$$

Here $\phi$ and $\psi$ stand for the boundary values at $x=0$. The term $\frac12(\phi\psi_t-\psi\phi_t)$ is first order in time derivatives; such terms are called **gyroscopic**. The sewing equations (3.1), $\pi_-=-E^{(t)}_\phi\mathcal L_d$ and $\pi_+=E^{(t)}_\psi\mathcal L_d$, read

$$\phi_x=\psi_t-\partial_\phi\mathcal B,\qquad \psi_x=\phi_t+\partial_\psi\mathcal B\qquad\text{at }x=0 .$$

These are the Bäcklund relations of [T9](#t9-bäcklund-transformations), imposed at one point.

**Momentum balance.** Insert the sewing equations into $\mathcal H_--\mathcal H_+$. After expanding the squares,

$$\mathcal H_--\mathcal H_+=\big(\psi_t\,\partial_\phi\mathcal B+\phi_t\,\partial_\psi\mathcal B\big)+\tfrac12\big((\partial_\psi\mathcal B)^2-(\partial_\phi\mathcal B)^2\big)+U(\phi)-U(\psi).$$

Because $f$ depends only on $\phi+\psi$ and $g$ only on $\phi-\psi$, the first bracket is $D_t(f-g)$. The second bracket is $-2f'g'$, and $2f'g'=\cos\psi-\cos\phi=U(\phi)-U(\psi)$. Hence

$$\mathcal H_--\mathcal H_++D_t(g-f)=0 .$$

The defect is momentum-conserving, with $\widetilde P=g-f$ stored in the defect. The relation $2f'g'=U(\phi)-U(\psi)$ is the constraint that momentum conservation places on the bulk potential; for sine-Gordon it can be met.

**Where it goes next.**

- *Link 1.* The defect is Type I, so Theorem 3.3 says: if the sewing equations hold at every $x$, then $\phi$ and $\psi$ both solve sine-Gordon. This is the classical Bäcklund statement, obtained here without cross-differentiating.
- *Link 2.* The gyroscopic term carries no energy, so the defect energy is $\mathcal E_d=\mathcal B$. Lorentz invariance ($T^{10}=T^{01}$) gives $D_t\mathcal B+D_xP_d=0$ along the Bäcklund relation: $\mathcal B$ is a conserved density.
- *Link 3.* The family parameter is $\epsilon=\sigma$. As $\sigma\to0$ the term $g$ becomes a very stiff spring forcing $\psi\to\phi$: the defect becomes transparent. Write $\Delta=\psi-\phi=\sigma\Delta_1+O(\sigma^2)$. The left sewing equation at lowest order gives $\Delta_1=2(\phi_x-\phi_t)$. Expanding $\mathcal B$ gives
  $$Q_1=(\phi_x-\phi_t)^2+2(1-\cos\phi)=2(T^{00}+T^{01}),$$
  a combination of energy and momentum. The higher odd orders give the spin-3, spin-5, … charges of sine-Gordon.
- *Where the family comes from.* In the coordinates $w=\frac12(\phi+\psi)$ and $q=\frac12(\phi-\psi)$, $\mathcal B=f(w)+g(q)$ with $f\propto\sigma$ and $g\propto\sigma^{-1}$. §8.2 shows that momentum conservation forces this splitting, and that rescaling $f$ up and $g$ down preserves momentum conservation ([§11.2](#112-hypothesis-c-for-relativistic-type-i-defects-82)).
- *Kinematics.* A boost of rapidity $\theta$ maps $\sigma\to\sigma e^{\pm\theta}$ (§5.2). So the spectral parameter of the Bäcklund transformation is a rapidity, and $Q_n$ has Lorentz spin $n$.
- *Link 4.* The generating quadratic symbol is $m(k;\sigma)=4\sigma\,\omega\,e^{\vartheta}/(1+\sigma^2e^{2\vartheta})$, with $k=\sinh\vartheta$ and $\omega=\cosh\vartheta$. Its coefficients $m_{2j+1}=4(-1)^j\omega e^{(2j+1)\vartheta}$ are distinct powers of $e^\vartheta$, so the charges are independent. [§10.5](#105-the-generating-symbol-proposition-75) derives this formula.

---

## Part 6. The spatial phase space (§2)

**Idea.** Set up the Hamiltonian description of evolution in $x$ for a Lagrangian of any finite order, as in the sine-Gordon example. Two facts proved here carry the rest of the paper:

- the momentum flux *is* minus the spatial Hamiltonian, as an identity off shell (Lemma 2.1);
- of Hamilton's equations in $x$, all but one hold identically, and the remaining one is the field equation (Lemma 2.2). This is the field version of "the velocity equation is automatic" in [§3.1](#31-hamiltons-equations).

### How it goes

**First-order Lagrangians.** Start with $\mathcal L(\phi,\phi_t,\phi_x)$. Vary $\phi$ by $\eta$ and integrate by parts:

$$\delta\mathcal L=\Big(\frac{\partial\mathcal L}{\partial\phi}-D_x\frac{\partial\mathcal L}{\partial\phi_x}-D_t\frac{\partial\mathcal L}{\partial\phi_t}\Big)\eta+D_x\Big(\frac{\partial\mathcal L}{\partial\phi_x}\eta\Big)+D_t\Big(\frac{\partial\mathcal L}{\partial\phi_t}\eta\Big).$$

The first term is the Euler–Lagrange expression $E(\mathcal L)\,\eta$. The second is a spatial boundary term; its coefficient $\pi=\partial\mathcal L/\partial\phi_x$ is the momentum for evolution in $x$. The third is a temporal boundary term, $D_t\,\Xi(\eta)$ with $\Xi(\eta)=\frac{\partial\mathcal L}{\partial\phi_t}\eta$. This is (2.1) for spatial order $K=1$.

**Higher order (Ostrogradsky).** If $\mathcal L$ contains $\phi_{xx}$, as for KdV in potential form, then evolution in $x$ needs both $\phi$ and $\phi_x$ as coordinates, each with its own momentum. In general, for a Lagrangian containing $x$-derivatives up to order $K$, the coordinates are $\Phi_m=D_x^m\phi$ for $m<K$, and the integration by parts in (2.1) produces one momentum $\pi_m$ for each. Formula (2.2) is the general bookkeeping, due to Ostrogradsky. The $F_k$ there are the coefficients of $D_x^k\eta$ after the $t$-derivatives have been moved off $\eta$. For potential KdV, $\mathcal L=\frac12p_xp_t-p_x^3-\frac12p_{xx}^2$ with $K=2$, one finds $\pi_1=-p_{xx}$ and $\pi_0=\frac12p_t-3p_x^2+p_{xxx}$. That is why the KdV defect has two pairs of sewing equations.

**Admissibility.** The Legendre transform must exist: one must be able to solve $\pi_{K-1}=\partial\mathcal L/\partial\phi_{0,K}$ for the highest $x$-derivative. The paper therefore asks that the highest $x$-derivative enter without mixed $t$-derivatives and with a nonzero second derivative $\partial^2\mathcal L/\partial\phi_{0,K}^2$. For a relativistic scalar this second derivative is $-1$.

**Lemma 2.1 (Legendre–Noether).** Choose $\eta=D_x\phi$ in (2.1), the variation produced by a translation in $x$. Then $\delta\mathcal L=D_x\mathcal L$, and rearranging (2.1) gives, for $K=1$,

$$D_t\,\Xi(\phi_x)+D_x\big(\pi\phi_x-\mathcal L\big)=-E(\mathcal L)\,\phi_x .$$

On shell the right side vanishes, so this is the momentum conservation law ([T6](#t6-conservation-laws-charges-and-noethers-theorem)). Its flux is $\pi\phi_x-\mathcal L=\mathcal H^{(x)}$, the Legendre transform with respect to the $x$-velocity. With the paper's signs, the momentum flux is $T^{11}=-\mathcal H^{(x)}$ exactly. The same computation works for any $K$, and with $\eta=D_t\phi$ it gives the energy law. For sine-Gordon, $T^{11}=\frac12(\phi_t^2+\phi_x^2)-U$ and $-\mathcal H^{(x)}=\frac12(\pi^2+\phi_t^2)-U$ agree because $\pi=-\phi_x$.

The uniqueness clause of Lemma 2.1 says the momentum flux is unambiguous. Any other pair satisfying (2.5) off shell differs only by a trivial current and a constant.

**Lemma 2.2 (Hamilton–Euler–Lagrange).** Take any field $\phi$, solution or not, and form its **Ostrogradsky lift**: the coordinates $D_x^m\phi$ together with the momenta $\pi_m$ computed from $\phi$. Then:

- every velocity equation $D_x\Phi_m=\partial\mathcal H/\partial\pi_m$ holds, because the Legendre transform inverts the definition of the momenta;
- every force equation $D_x\pi_m+b_m=0$ with $m\ge1$ holds, because the momenta were defined by the recursion $\pi_{m-1}=F_m-D_x\pi_m$;
- the last force equation reads $D_x\pi_0+b_0=-E(\mathcal L)[\phi]$.

Only the last equation carries information. The lift is a solution of Hamilton's equations in $x$ exactly when $\phi$ solves its field equation. Theorem 3.3(b) uses this: a mismatch between two tangent vectors can only show up in the $m=0$ force component.

### Fine print

- The Lagrangian has no explicit $x$ or $t$. Explicit coordinates appear only in the affine currents of §5.
- The canonical currents (2.4) are what one gets from $\eta=D_t\phi$ and $\eta=D_x\phi$ in (2.1). For a first-order Lagrangian they are the familiar ones.

---

## Part 7. Link 1: momentum conservation gives a Bäcklund relation (§3)

### 7.1 Defects and the sewing correspondence (§3.1)

**Idea.** Vary the total action of [Part 1](#part-1-the-question). By (2.1), each half-line leaves a boundary term at $x=0$: $+\pi_-\cdot\delta\Phi$ from the left and $-\pi_+\cdot\delta\Psi$ from the right, exactly as in [§3.2](#32-a-jump-described-by-an-action). Adding the variation of $S_d$ and requiring the total to vanish gives the sewing equations (3.1):

$$\pi_-=\Pi^-(Y):=-E^{(t)}_\Phi\mathcal L_d,\qquad \pi_+=\Pi^+(Y):=E^{(t)}_\Psi\mathcal L_d,\qquad 0=C(Y):=E^{(t)}_\lambda\mathcal L_d .$$

Here $Y=(\Phi,\Psi,\lambda)$ collects the boundary data and the auxiliary variables. The defect prescribes the spatial momenta on both sides as functions of $Y$, like the jump rule of the toy model. The **sewing correspondence** $\Gamma_d$ is the set of all left and right data obtained in this way, as $Y$ runs over all histories that satisfy the constraint. It is the field version of the jump relation $\Gamma$.

A **promoted solution** imposes (3.1) at every $x$, with $\pi_\mp$ the actual Ostrogradsky momenta of $\phi$ and $\psi$. A Bäcklund relation is a relation that can be promoted in this way.

**The linearisation (3.2).** Let $\mathcal S$ be the linearisation of the defect's Euler–Lagrange expression $E_Y(\mathcal L_d)$ ([T4](#t4-linearisation-and-adjoints)). Its blocks $S_{AB}$ are differential operators in $t$, the analogues of the second derivatives $S_{qQ}$ of the toy model. Equation (3.2) says how the momenta and the constraint change when $Y$ changes by $\delta Y$; it is the analogue of differentiating the jump rule. A change of the data is **tangent** to $\Gamma_d$ if it arises from some $\delta Y$ in this way: it keeps the data allowed, to first order. By the Helmholtz conditions ([T5](#t5-symmetry-of-second-variations-helmholtz)), $S_{AB}^*=S_{BA}$.

### 7.2 What "momentum-conserving" means (§3.2)

**Idea.** Definition 3.1 asks that

$$\mathcal H_-\big(\Phi,\Pi^-(Y)\big)-\mathcal H_+\big(\Psi,\Pi^+(Y)\big)\in\operatorname{Im}D_t+\langle C\rangle ,$$

as an identity in the $t$-derivatives of $Y$. In words: insert the sewing equations into the difference of the momentum fluxes. After using the constraint, the result must be the time derivative of a local function of the boundary data, the defect momentum. This must hold for *arbitrary* boundary histories, not only those of bulk solutions. That is the field version of "$h\equiv0$" ([§3.5](#35-back-to-field-theory)).

Any multiple of the constraint or of its time derivatives can be integrated by parts into the form $\rho\cdot C$ plus a total derivative. So Definition 3.1 is equivalent to

$$\mathcal H_--\mathcal H_+=\rho\cdot C+D_tB\qquad(3.3')$$

for local $\rho$ and $B$. This is the field version of $h=\rho\,C$ in [§3.4](#34-the-converse-half-and-what-can-go-wrong). The multiplier $\rho$ will be the rate at which the Hamiltonian flow moves $\lambda$.

**Lemma 3.2** connects this with the physical statement that $P_-+P_++\widetilde P$ is conserved. By [T6](#t6-conservation-laws-charges-and-noethers-theorem), $\frac d{dt}(P_-+P_+)=(-T^{11}_-+T^{11}_+)|_{x=0}=(\mathcal H_--\mathcal H_+)|_{x=0}$, and the balance makes this $-D_t\widetilde P$.

**Fine print.** The converse of Lemma 3.2, "conserved momentum implies the off-shell balance", needs two regularity assumptions. The boundary data of solutions must fill out the constraint locus, and $\langle C\rangle$ must contain every function that vanishes on that locus. The paper's example is two Klein–Gordon fields with $\mathcal L_d=\lambda(\psi-\phi)^2$. The constraint is $(\psi-\phi)^2=0$, which forces $\psi=\phi$: the defect is invisible, and momentum is conserved with $P_d=0$. But $C=(\psi-\phi)^2$ vanishes to second order, so the multiples of $C$ are too few to absorb $\mathcal H_--\mathcal H_+$, and the off-shell balance fails. Definition 3.1 is therefore strictly stronger than conservation on solutions. It is the form Corrigan and Zambon use.

### 7.3 The Bäcklund theorem (§3.3)

**Idea.** Run the toy argument of [§3.3](#33-energy-conserving-jumps-are-symmetries) and [§3.4](#34-the-converse-half-and-what-can-go-wrong) with the dictionary of [§3.5](#35-back-to-field-theory).

- Part (a) is the Fact: the pair of spatial Hamiltonian vector fields $(X_-,X_+)$ is tangent to $\Gamma_d$. Evolving both sides in $x$ keeps them allowed partners.
- Part (b) is the converse half: a promoted solution solves both bulk equations, provided condition (I) rules out a mismatch $\kappa$ in the auxiliary variables.

**How part (a) goes: three moves.** Each move has the same job as in the toy model.

*Move 1: differentiate the balance.* In the toy model we took partial derivatives of $h$. Here we apply the time-Euler operator $E_Y$ to (3.3′) ([T3](#t3-the-euler-operator)).
- $E_Y$ annihilates $D_tB$. This is why the balance need only hold up to a total time derivative.
- Where the constraint and its time derivatives vanish, $E_Y(\rho\cdot C)=D_C^*\rho$; the other term, $D_\rho^*C$, contains $C$ and vanishes. This is the field version of differentiating $\rho\,C$ and setting $C=0$.
- On the left, the chain rule for Euler operators ([T4](#t4-linearisation-and-adjoints)) gives $D_{\Pi^\mp}^*$ applied to the velocity $a_\mp=\partial\mathcal H_\mp/\partial\pi$, plus the force $b_\mp=E^{(t)}_\Phi\mathcal H_\mp$. This is the field version of the chain rule in $\partial h/\partial q$.

*Move 2: use the symmetry of the second variation.* In the toy model we used $S_{qQ}=S_{Qq}$. Here the operators $D_{\Pi^\pm}$ and $D_C$ are blocks of $\mathcal S$, and self-adjointness $S_{AB}^*=S_{BA}$ turns their adjoints into the blocks of (3.2). The result is (3.5), the same three equations as in [§3.4](#34-the-converse-half-and-what-can-go-wrong), with the $S$'s now differential operators in $t$.

*Move 3: read (3.5) as tangency.* Put $\delta Y=(a_-,a_+,\rho)$ into (3.2). The third line of (3.5) says the constraint stays satisfied. The first two lines say $\delta\pi_\mp=-b_\mp$, and the configuration changes are $\delta\Phi=a_-$, $\delta\Psi=a_+$. The resulting change of the data is $(a_-,-b_-;\,a_+,-b_+)=(X_-,X_+)$: the Hamiltonian motion in $x$ keeps the data allowed, with the auxiliary variables moving at the rate $\rho$.

**How part (b) goes.** Let $(\phi,\psi,\lambda)$ be a promoted solution. At each point there are two tangent vectors to $\Gamma_d$:

- the actual $x$-derivative of the data, which comes from $\delta Y=D_xY$ (differentiate the sewing equations in $x$);
- $(X_-,X_+)$, which comes from $\delta Y=(a_-,a_+,\rho)$ by part (a).

By Lemma 2.2 the velocity equations $D_x\Phi=a_-$ and $D_x\Psi=a_+$ hold automatically. So the two vectors differ only through $\delta Y=(0,0,\kappa)$, with $\kappa=D_x\lambda-\rho$: the mismatch between how fast $\lambda$ actually changes and how fast the Hamiltonian flow says it should. The momentum components of the difference are $D_x\pi_\mp+b_\mp$. By Lemma 2.2 they vanish for $m\ge1$ and equal $-E_-$ and $-E_+$ for $m=0$. Reading these through (3.2) gives (3.4): the two field equations are images of $\kappa$. The remaining rows of (3.4) form the operator (I). If (I) is injective, that is, if it sends only $\kappa=0$ to zero, then $\kappa=0$ and both field equations hold.

A Type-I defect has no auxiliary variables, so there is no $\kappa$, and the bulk equations follow with no condition.

**Sine-Gordon.** Type I. Theorem 3.3 says the Bäcklund relation of [Part 5](#part-5-the-running-example-sine-gordon) maps solutions to solutions, and that imposing it everywhere implies both field equations.

**Fine print (Remarks 3.4).**

- *Condition (I) cannot be dropped.* Take two scalars with an even potential and $S_d=\int\lambda(\psi+\phi)\,dt$. This is the field version of the toy example in [§3.4](#34-the-converse-half-and-what-can-go-wrong). The constraint is $\psi=-\phi$, momentum balances, and the operator (I) is zero. For Klein–Gordon, $(\phi,\psi,\lambda)=(x^2,-x^2,2x)$ is a promoted solution but $E_-[\phi]=2-m^2x^2\ne0$. The relation $\psi=-\phi$ maps solutions to solutions only because $\phi\mapsto-\phi$ is a symmetry. It has no nondegenerate family, so Link 3 fails for it too.
- *Condition (I) in practice.* It is vacuous for Type I. For the KdV and mKdV defects with a multiplier $\mu$, the $m=1$ row gives $S_{\Phi_1\mu}=\partial C/\partial\Phi_1=1$, which is injective. For relativistic Type II, $K=1$, so only the $\lambda\lambda$ row remains, and (I) says that multiplication by $S_{\lambda\lambda}=-\partial_\lambda^2\mathcal D$ is injective, as in the toy model.
- *Different bulk theories.* Nothing requires $\mathcal L_-=\mathcal L_+$. A momentum-conserving defect between Liouville theory and a free massless field is a Bäcklund relation that linearises Liouville theory.
- *What is not used.* Neither the invertibility of the jump, nor the full Lagrangian property of $\Gamma_d$, nor any connectedness.

### 7.4 Half the sewing equations imply the other half (Lemma 3.5)

**Idea.** Let $\phi$ solve its field equation. Choose $(\Psi,\lambda)$ so that the left sewing equations and the constraint hold at every $x$. Then, under condition (T), the right sewing equations hold automatically, and $\psi=\Psi_0$ solves its field equation. Momentum conservation supplies the missing half.

**How it goes.** It is the subtraction of part (b) again. Now the unknown difference of the two tangent vectors comes from $\delta Y=(0,\eta,\kappa)$, where $\eta$ is the mismatch in the right configuration. Its left-momentum component and its constraint component vanish. Condition (T) says this forces $\eta=\kappa=0$. Reading the right force equations downward from $m=K-1$ then identifies $\Pi^+$ with the actual momenta of $\psi$.

**Why it is needed.** Link 3 constructs $\psi$ by solving only the *left* sewing equation in a power series (Lemma 6.6). Lemma 3.5 then gives the right one.

---

## Part 8. Link 2: one conserved density along the relation (§4, §5.1)

**Idea.** A Bäcklund relation maps solutions to solutions. We want something different: conserved densities of a single theory. The bridge is the *defect charge*.

1. A defect charge is what the defect contributes to make a bulk charge conserved. The defect energy is one.
2. When the relation is imposed at every $x$, a defect charge becomes a field on the whole plane. It is a potential for the *difference* of the two bulk currents (Proposition 4.2). On its own this gives nothing new: a difference of known conserved densities is known.
3. But a kinematic symmetry, such as a Lorentz boost, can relate the flux of one conservation law to the density of another. This **closure** relation turns the defect charge of the first law into a conserved density in its own right (Proposition 4.3). That density is the **generating density** $\mathcal G$.

For relativistic theories the generating density is the defect energy. The relation used is "energy flux equals momentum density" ([T7](#t7-energy-momentum-and-the-stress-tensor)).

### 8.1 Defect charges (§4.1)

Take a conservation law $(N,J)$ that holds on both sides. A **defect charge** for it is a local $Q_d(Y)$ with (4.1):

$$D_tQ_d\equiv J_-\big|_{x=0}-J_+\big|_{x=0}\pmod{\langle C\rangle}.$$

The flux into the defect from the left minus the flux out to the right is stored in the defect. Then $\int_{x<0}N_-+\int_{x>0}N_++Q_d$ is conserved ([T6](#t6-conservation-laws-charges-and-noethers-theorem)).

**Lemma 4.1** produces defect charges from symmetries. The symmetry must act within each time slice: it must not involve $x$-derivatives in a way that produces an $x$-flux (condition 1). It must act on the boundary data (condition 2), and it must be a symmetry of $\mathcal L_d$ (condition 3). The proof applies the first-variation formula at $x=0$ and uses the sewing equations. Examples:

- *Time translation* gives the defect energy $\mathcal E_d$, for every defect that does not depend explicitly on time.
- *A phase rotation* gives the NLS particle number, for defects that are phase-invariant.
- *Field shifts* $\phi\mapsto\phi+\text{const}$ give charges when the defect depends on the fields only through differences.
- *Spatial translation* violates condition 1. Its defect charge, $\widetilde P$, is exactly what Definition 3.1 assumes. Momentum is the one charge the defect has to work for.

**Sine-Gordon.** The defect energy is $\mathcal E_d=\Xi_d(D_tY)-\mathcal L_d$, the Legendre transform of $\mathcal L_d$ with respect to the time derivatives. For a gyroscopic term $A(\phi,\psi)\cdot\phi_t$ the Legendre transform gives $A\cdot\phi_t-A\cdot\phi_t=0$, so $\mathcal E_d=\mathcal B$.

**Fine print.** A conservation law whose density is an $x$-derivative is not always trivial off shell. The KdV mass law $(p_x,\,p_{xxx}-3p_x^2)$, in the potential variable $p$ with $u=p_x$, is a trivial law plus the Noether law of the shift $p\mapsto p+\text{const}$. So it has a defect charge only when the defect is shift-invariant. The KdV defect of [3] is, with charge $q-p$. Adding $\beta p^2$ to it destroys the charge.

### 8.2 Defect charges as potentials (§4.2)

**Idea.** Along a promoted solution, $Q_d$ becomes a function on the whole plane, and (4.1) holds at every $x$: $D_tQ_d=\Delta J$, where $\Delta$ means "left minus right". We want also $D_xQ_d=-\Delta N$. Then $Q_d$ is a potential for the closed 1-form $\Delta N\,dx-\Delta J\,dt$ ([T6](#t6-conservation-laws-charges-and-noethers-theorem)).

**How it goes.** Put $R=D_xQ_d+\Delta N$, the amount by which the second equation fails. Using both bulk laws, $D_tR=D_x\Delta J+D_t\Delta N=0$. So $R$ does not depend on $t$. It remains to show $R=0$.

**Why this last step is subtle.** $D_tR=0$ does not imply $R=0$. A derivative kills constants, and along one particular solution $R$ could be any function of $x$. The paper uses two settings.

- **(A) Formal branch.** This is the setting of Link 3. Each coefficient of $R$ in the power series is a local function of $\phi$ alone. Lemma 6.3 says that such a function, if $D_t$ annihilates it on every solution, is a constant. The constant is its value at the vacuum, which can be computed.
- **(B) Asymptotics.** For each $x$ the solution tends to a constant pair as $t\to-\infty$, and $R$ is zero there.

**Lemma 6.3, in one picture.** Can a local function $f(\phi,\phi_x,\phi_t,\dots)$ have zero time derivative on every solution of, say, the sine-Gordon equation, without being constant? No, and the proof is easiest with $x$ as the evolution direction. Using the field equation to eliminate $\phi_{xx}$ and its derivatives, every derivative of $\phi$ can be written in terms of the $t$-derivatives of $\phi$ and $\phi_x$ alone. These are free: any values can occur (they are Cauchy data for evolution in $x$). In these coordinates $D_t$ acts as a pure shift: it sends $\partial_t^a\phi$ to $\partial_t^{a+1}\phi$ and $\partial_t^a\phi_x$ to $\partial_t^{a+1}\phi_x$. Suppose $f$ depends on $t$-derivatives up to order $A$. Then $D_tf$ contains the order-$A+1$ derivatives, multiplied by $\partial f/\partial(\partial_t^A\phi)$ and $\partial f/\partial(\partial_t^A\phi_x)$, and nothing else can cancel them. So these partial derivatives vanish, $f$ does not depend on order $A$, and by induction $f$ is constant. Part (a) of Lemma 6.3 does the elimination for any admissible Lagrangian; for spatial order $K$ the free coordinates are the $t$-derivatives of $\phi,\phi_x,\dots,D_x^{2K-1}\phi$.

**Outcome.** For energy and momentum this gives four identities,

$$D_t\mathcal E_d=\Delta T^{10},\quad D_x\mathcal E_d=-\Delta T^{00},\quad D_tP_d=\Delta T^{11},\quad D_xP_d=-\Delta T^{01}.$$

The defect energy and defect momentum are potentials for the differences of the stress tensors on the two sides.

### 8.3 Closure (§4.3, §5.1)

**Proposition 4.3.** Suppose laws 1 and 2 have defect charges $Q^1$ and $Q^2$, and on each side

$$N_2+J_1+D_ta_0+D_xb_0=0\quad\text{on shell}\qquad(4.2)$$

for some local $a_0$ and $b_0$: the density of law 2 plus the flux of law 1 is a divergence. Then

$$D_tQ^1=\Delta J_1=-\Delta N_2-D_t\Delta a_0-D_x\Delta b_0=D_xQ^2-D_t\Delta a_0-D_x\Delta b_0 .$$

The first equality is (4.1), the second is (4.2), the third is Proposition 4.2 applied to law 2. Rearranged, $\mathcal G=Q^1+\Delta a_0$ is a conserved density with flux $\Delta b_0-Q^2$. Only law 2 needs the normalisation $R=0$ of §8.2, and its vacuum value vanishes automatically.

**Where closure comes from (Lemma 5.2).** An **affine conservation law** has a current that depends on $x$ and $t$ explicitly, but only linearly:

$$\big(x\,a_1+t\,a_2+a_0,\ \ x\,b_1+t\,b_2+b_0\big),$$

with $a_i,b_i$ free of explicit coordinates. Noether currents of symmetries that move points of spacetime have this form. Expand its conservation law, using $D_xx=D_tt=1$ and $D_tx=D_xt=0$:

$$x\,(D_ta_1+D_xb_1)+t\,(D_ta_2+D_xb_2)+\big(a_2+b_1+D_ta_0+D_xb_0\big)=0 .$$

The coefficients of $x$, of $t$ and the remainder must vanish separately. The first two say that $(a_1,b_1)$ and $(a_2,b_2)$ are conservation laws. The third is closure (4.2), with $N_2=a_2$ and $J_1=b_1$. The observed bulk theories all have one:

| bulk | symmetry | closure: density of law 2 $+$ flux of law 1 | $\mathcal G$ |
|---|---|---|---|
| relativistic scalars | Lorentz boost | $-$momentum density $+$ energy flux $=0$, i.e. $T^{10}=T^{01}$ | defect energy $\mathcal E_d$, with flux $P_d$ |
| NLS | Galilean boost | $-2\times$momentum density $+$ number flux $=0$ | defect number |
| KdV | Galilean symmetry | $3u^2$ ($\propto$ momentum density) $+$ mass flux $=u_{xx}$ | $q-p$ (potentials) |
| mKdV | dilation | $3\times$energy density $+$ flux of $\tfrac12v^2$ (momentum) $=-D_x(vv_x)$ | defect momentum $P_d$ |
| Boussinesq | time-linear shift $u\mapsto u+\epsilon t$ | shift-law density $+$ trivial flux $=-D_t(u/c^2)$ | $(u-v)/c^2$ |

For the relativistic row, the boost current is $(xT^{00}-tT^{01},\ xT^{10}-tT^{11})$ ([T7](#t7-energy-momentum-and-the-stress-tensor)). Law 1 is energy, law 2 is minus momentum, and closure is $T^{10}=T^{01}$. Proposition 4.3 gives

$$D_t\mathcal E_d+D_xP_d=0\quad\text{along every promoted solution}.$$

This is the heart of Link 2 in the relativistic case. The defect energy measures how much energy the defect stores. Once the sewing relation holds at every $x$, the defect energy becomes a conserved density of the pair of theories, and its flux is the defect momentum.

**Fine print.**

- *Closure is kinematic.* It is a property of the bulk alone and comes from a symmetry, not from integrability. Every massive relativistic theory has the Lorentz closure. Link 2 therefore does not distinguish integrable theories from others.
- *Why not use a density difference.* The difference $T^{01}_--T^{01}_+=-D_xP_d$ is an exact $x$-derivative. Expanding it in a parameter gives only trivial charges.
- *Corollary 5.3* checks that both constituent laws have defect charges in every observed case.

---

## Part 9. Link 3: a family and its transparent limit (§5.2, §6)

**Idea.** The generating density $\mathcal G(\phi,\psi,\lambda)$ is conserved, but it depends on both fields. To get conserved densities of $\phi$ alone we must express $\psi$ through $\phi$. The Bäcklund relation does determine $\psi$ from $\phi$, but only by integrating a differential equation in $x$, which gives nonlocal expressions.

The way out is perturbation theory around a defect that does nothing. Call a defect **transparent** if it forces $\psi=g(\phi)$, where $g$ is a symmetry such as the identity. Take a one-parameter family of defects $S_d^{(\epsilon)}$ that becomes infinitely stiff as $\epsilon\to0$, forcing $\psi\to g(\phi)$. Then $\psi$ can be written as a power series in $\epsilon$ whose coefficients are local expressions in $\phi$ ([T12](#t12-formal-power-series)). Substituting into $\mathcal G$ and expanding, each coefficient of $\epsilon^n$ is a local conserved density $Q_n[\phi]$. The same mechanism underlies the Gardner $\epsilon$-expansion for KdV and the expansion of a Bäcklund transformation in its spectral parameter.

A single defect gives a Bäcklund relation (Link 1) and one conserved density (Link 2). Infinitely many local charges need the family. This is where integrability enters.

### 9.1 Where families come from (§5.2)

1. **Dilation orbits (Lemma 5.4).** Suppose the bulk Lagrangian is unchanged, up to an overall factor, by a rescaling $(x,t,\phi)\mapsto(sx,s^\alpha t,s^\beta\phi)$, but the defect is not. Then the rescaled defects form a one-parameter family, and each member is again momentum-conserving. This is how the parameters of the NLS, KdV and mKdV defects arise, with weights 1, 2 and 1.
2. **Lorentz orbits (Lemma 5.5).** A boost maps solutions of the bulk to solutions, and maps a promoted solution to a promoted solution of the boosted relation. The defect energy and momentum transform as the two components of a vector. For sine-Gordon the boosted relation is the same defect with $\sigma\to\sigma e^{\pm\theta}$.
3. **Free parameters of the momentum constraint.** The Boussinesq parameter $\sigma_0$ is not produced by any symmetry. It is simply a free parameter in the general solution of the momentum constraint (a *modulus*). Similarly, the relativistic Type-I potential splits as $\mathcal B=F+G$, and the constraint is unchanged by $(F,G)\mapsto(\sigma F,\sigma^{-1}G)$.

**Fine print.**

- *Strict homogeneity.* Lemma 5.4 needs the chosen Lagrangians to rescale exactly, not up to an $x$-derivative. The spatial momenta and $\mathcal H$ change if a total $x$-derivative is added to $\mathcal L$. The paper's example adds $D_x(\frac12w^2)$ to a free Lagrangian; the rescaled defects are then not momentum-conserving for $s\ne1$.
- *Boosted defects.* For Lemma 5.5 the boosted relation is, in general, only known to hold along promoted solutions. Whether it is again a defect of the form (3.1), with a local defect momentum, is checked case by case. For sine-Gordon it is.

### 9.2 Formal branches and the formal implicit function theorem (Definition 6.1, Lemma 6.2)

A **formal branch** is a pair of series

$$\psi=g(\phi)+\sum_{n\ge1}\epsilon^n\Psi_n[\phi],\qquad\lambda=\sum_{n\ge n_0}\epsilon^n\Lambda_n[\phi],$$

whose coefficients $\Psi_n,\Lambda_n$ are local functions of $\phi$. Every promoted sewing equation must hold order by order in $\epsilon$ whenever $\phi$ solves its field equation. The symmetry $g$ is the identity, a constant shift, or $\phi\mapsto-\phi$. Constant offsets in the vacuum are allowed; KdV needs one.

**Lemma 6.2** says when a branch can be found by algebra alone, as in the example of [T12](#t12-formal-power-series). Two conditions are needed for the unknown $\Delta=\psi-g(\phi)$:

1. at $\epsilon=0$ the sewing equation has the form $M\Delta+O(\Delta^2)=0$ with an invertible matrix $M$, so that it forces $\Delta=0$;
2. derivatives of $\Delta$ appear only with a positive power of $\epsilon$.

Then the coefficient of $\epsilon^n$ reads $M\Delta_n=$ (a local expression in $\Delta_1,\dots,\Delta_{n-1}$ and their derivatives), and each $\Delta_n$ follows by matrix inversion. If derivatives of $\Delta$ appeared at order $\epsilon^0$, each step would require solving a differential equation, and the coefficients would be nonlocal. A "regular transparent limit" means exactly that this does not happen.

### 9.3 Gyroscopic Type-I defects (Lemma 6.6)

**Idea.** A wide class of relativistic Type-I families has a formal branch. The class is

$$\mathcal L_d^{(\epsilon)}=A_\Phi\cdot\Phi_t+A_\Psi\cdot\Psi_t-\epsilon^{-1}\mathcal B_-(\Phi,\Psi)-\sum_{k\ge0}\epsilon^k\mathcal B_k(\Phi,\Psi),$$

where $\mathcal B_-$ vanishes to second order on the diagonal $\Psi=\Phi$ and its matrix of second derivatives $\mathsf H$ there is invertible. The term $\epsilon^{-1}\mathcal B_-$ is a stiff spring holding $\Psi$ close to $\Phi$. The terms $A\cdot\Phi_t$ are gyroscopic.

**How it goes.** Multiply the left sewing equation by $\epsilon$. Its leading term comes from the spring, $-\mathsf H\Delta+O(\Delta^2)$. The gyroscopic terms contain the only derivatives of $\Delta$, and they carry a factor $\epsilon$. So Lemma 6.2 gives $\Delta$. For the right sewing equation use Lemma 3.5, which needs momentum conservation. Its condition (T) holds because $S_{\Phi\Psi}=\epsilon^{-1}\mathsf H+O(1)$ is invertible as a power series.

For sine-Gordon, $\mathcal B_-=2(1-\cos\frac{\phi-\psi}2)$ with $\mathsf H=\frac12$, and $\mathcal B_1=2(1-\cos\frac{\phi+\psi}2)$. For $a_r^{(1)}$ affine Toda, $\mathsf H$ is positive definite because the roots span $\mathbb R^r$.

**Fine print.** Momentum conservation is essential here. The stiff spring $-(\phi-\psi)^2/(2\epsilon)$ between Klein–Gordon fields has the right form but does not conserve momentum; it is the field version of the spring in [§3.2](#32-a-jump-described-by-an-action) with a potential added. Its left sewing equation gives $\psi=\phi+\epsilon\phi_x$, and its right one then forces $\epsilon\phi_{xx}=0$.

### 9.4 The hierarchy (Theorem 6.4)

**How it goes.** A formal branch is a promoted solution in setting (A) of §8.2. By Lemma 6.3 the residuals $R$ are constants, and Proposition 4.3 shows that the one it needs vanishes. So the conservation law $D_t\mathcal G+D_x\mathcal F=0$ holds as an identity between power series in $\epsilon$. Each coefficient of $\epsilon^n$ is then a separate local conservation law, $D_tQ_n+D_x\mathcal J_n=0$.

**Sine-Gordon.** At order $\sigma^0$ the left sewing equation gives $\Delta_1=2(\phi_x-\phi_t)$. At order $\sigma$ the expansion of $\mathcal G=\mathcal B$ gives

$$Q_1=\tfrac14\Delta_1^2+2(1-\cos\phi)=(\phi_x-\phi_t)^2+2(1-\cos\phi)=2(T^{00}+T^{01}).$$

The paper's checks find nontrivial charges at orders 1, 3 and 5 (§9, comment 1).

### 9.5 Kinematic weights (Lemma 6.5)

**Idea.** Theorem 6.4 produces charges $Q_n$ but does not say whether they differ from one another. Symmetry can decide this. Suppose a symmetry $g_\theta$ of the bulk moves the parameter, $\epsilon\mapsto e^{w\theta}\epsilon$ with $w\ne0$, and maps the branch to the branch. Comparing powers of $\epsilon$ shows that the charge $\bar Q_n=\int Q_n\,dx$ is an eigenvector of $g_\theta$ with eigenvalue $e^{(w_0+nw)\theta}$. Eigenvectors with distinct eigenvalues are linearly independent. Physically, the charges carry distinct spins, or distinct scaling dimensions.

For sine-Gordon, $w=\pm1$ and $w_0=0$, so $Q_n$ has spin $n$. In terms of symbols ([T11](#t11-plane-waves-dispersion-and-quadratic-symbols)), $m_n/\omega\propto e^{n\vartheta}$, and a boost shifts $\vartheta$.

**Fine print.**

- *$w\ne0$ is needed.* If the parameter does not move, all eigenvalues coincide. A family such as $\frac{\epsilon}{1-\epsilon}m_*(k)$ has infinitely many nonzero but proportional coefficients.
- *Condition 4 is needed.* The argument compares quadratic parts, so the symmetry must not mix a quadratic piece into the linear parts of the charges. A Lorentz boost is linear on fields in spacetime, but its action on Cauchy data at $t=0$ uses the field equation and can be nonlinear. Its quadratic part is $-\frac12U'''(0)\,x\phi^2$. This vanishes for sine-Gordon but not for Tzitzéica or $a_r^{(1)}$ Toda with $r\ge2$. The paper gives an explicit counterexample with a nonlinear change of variables.

---

## Part 10. Link 4: involution and independence (§7)

**Idea.** Conserved is not the same as commuting. The usual proofs that conserved charges Poisson-commute use a Lax pair, an $r$-matrix, or the commutativity of Bäcklund transformations ("Bianchi permutability"). None is available here. The paper uses a perturbative rigidity argument instead.

- In a theory whose waves do not resonate, a conserved local functional is completely determined by its parts of degree 0, 1 and 2 in the fields (Lemma 7.2).
- The Poisson bracket of two conserved charges is again conserved (Jacobi identity, [T10](#t10-hamiltonian-field-equations-and-poisson-brackets)). If its parts of degree at most 2 vanish, it vanishes.
- Independence can also be read off from the quadratic parts, and those can be computed in closed form from the generating density (Proposition 7.5).

### 10.1 Setting and nonresonance (§7.1)

The bulk is Hamiltonian, $v_t=\mathcal J\,\delta H/\delta v$, with a **constant** operator $\mathcal J$ and $H=H_2+H_3+\dots$. Because $\mathcal J$ is constant, brackets lower the degree by exactly 2 ([T10](#t10-hamiltonian-field-equations-and-poisson-brackets)). All the degree counting below rests on this.

**Why resonances matter.** Let $F_d$ be a homogeneous functional of degree $d$, written in normal modes as a sum (an integral) of products of $d$ modes with coefficients $c(k)$ ([T11](#t11-plane-waves-dispersion-and-quadratic-symbols)). Under the linearised flow, each product oscillates like $e^{-i\Omega t}$. So $F_d$ is conserved by the linearised flow only if $c(k)=0$ wherever $\Omega(k)\ne0$. If $\Omega$ is nonzero almost everywhere on the set of allowed momenta, then $c$ vanishes almost everywhere, and, being continuous, everywhere.

**(NR)** asks exactly this: for every degree $n\ge3$, $\Omega$ does not vanish on any open piece of the momentum hyperplane $\sum s_ik_i=0$. In physical terms, there is no continuous family of resonant $n$-wave interactions.

**Why (NR) holds for massive theories.** Use the momentum constraint to eliminate $k_n$. For two other wavenumbers $k_i$ and $k_j$,

$$\frac{\partial^2\Omega}{\partial k_i\,\partial k_j}=s_is_js_n\,\omega''(k_n).$$

If $\Omega$ vanished on an open set, so would this second derivative, so $\omega''$ would vanish on an interval. That is impossible for a dispersion relation that is real-analytic and not a straight line: $\sqrt{k^2+m^2}$ with $m>0$, $k^2$, $k^3$ and $k\sqrt{1+\kappa^2k^2}$.

For massless waves, $\omega=\lvert k\rvert$ is a straight line for $k>0$, and $\omega(k_1)+\omega(k_2)=\omega(k_1+k_2)$ for all positive $k_1,k_2$: two right-moving massless waves can always merge into one. This is why massless theories are excluded from Link 4.

Isolated resonances do no harm. In one space dimension, an elastic collision of two particles of equal mass can only exchange their momenta. This set of resonances has no interior, so (NR) still holds for products of four modes.

**(NR2)** asks that every quadratic functional conserved by the linearised flow be built from the mode intensities $\lvert a_j(k)\rvert^2$. Such functionals commute with one another. (NR2) holds when distinct modes with the same momentum have distinct frequencies. It fails for degenerate spectra, such as the pairs of particles of equal mass in $a_r^{(1)}$ Toda with $r\ge2$.

### 10.2 Rigidity (Lemma 7.2)

**Statement.** Under (NR), a conserved local functional whose parts of degree 0, 1 and 2 vanish is zero: its density is a total $x$-derivative.

**How it goes.** Let $F_d$ be its lowest nonzero part, so $d\ge3$. Collect the terms of degree $d$ in $\{F,H\}=0$. Since brackets lower degree by 2, the only such term is $\{F_d,H_2\}$, so $\{F_d,H_2\}=0$: $F_d$ is conserved by the linearised flow. By the resonance argument of §10.1, its coefficients vanish, so $F_d=0$, contradicting the choice of $d$.

**Why locality matters.** The square $H_2^2$ of the free Hamiltonian is a quartic functional conserved by the linear flow, so the lemma would be false without locality. But $H_2^2$ is a product of two integrals, not a single integral of a local density. In normal modes its coefficients are concentrated on the set where the four momenta cancel in pairs, which has no interior. The coefficients of a local functional are continuous functions and cannot be concentrated in that way.

The argument works degree by degree. It therefore covers densities that are polynomials or convergent power series in the fields. Nothing is claimed for smooth densities whose Taylor series at the vacuum vanishes.

### 10.3 Involution (Theorem 7.3)

**How it goes.** Let $B=\{Q_n,Q_m\}$. It is a local functional, and it is conserved by the Jacobi identity. Count degrees, using "degree $a$ bracket degree $b$ gives degree $a+b-2$":

- every term of degree 0 or 1 in $B$ involves a linear part $Q_{n,1}$ or $Q_{m,1}$. Condition (L), $\{Q_{n,1},Q_m\}=0$, removes them all;
- the remaining degree-2 part is $\{Q_{n,2},Q_{m,2}\}$.

There are two ways to make the degree-2 part vanish. Either assume directly that the quadratic parts commute. Or use the degree-2 part of $\{Q_n,H\}=0$, which is $\{Q_{n,2},H_2\}+\{Q_{n,1},H_3\}=0$. Under (L′), $\{Q_{n,1},H_3\}=0$, so $Q_{n,2}$ is conserved by the linearised flow. Under (NR2) it is then built from mode intensities, and such functionals commute. Either way, Lemma 7.2 now gives $B=0$.

Both (L) and (L′) are automatic when the charges have no linear parts. They also hold when the linear parts are Casimirs, such as $\int u\,dx$ for $\mathcal J=D_x$.

**Fine print.**

- *(L′) is needed.* The paper gives a canonical pair $(q,p)$ with a Hamiltonian that is free in disguised coordinates. Two conserved charges commute and satisfy (L), but the quadratic part of one of them is not conserved by the linearised flow.
- *(NR2) is needed.* Two free fields of equal mass have two conserved quadratic charges whose bracket is not zero. They generate rotations between the two fields.

### 10.4 Independence (Theorem 7.4)

**How it goes.** Evaluate the gradients $\delta Q_n/\delta v$ at a small field $\varepsilon v_0$ made of finitely many Fourier modes $k_l\ne0$. To lowest order in $\varepsilon$, the gradient of $Q_n$ on the mode $k_l$ is $\varepsilon\,m_n(k_l)\,\hat v_0(k_l)$, where $m_n$ is the quadratic symbol. Linear parts contribute only at $k=0$. If the functions $m_n$, $n\in S$, are linearly independent, one can choose $\lvert S\rvert$ wavenumbers $k_l$ at which the matrix $(m_n(k_l))$ has full rank. The gradients are then linearly independent at $\varepsilon v_0$, and nearby. So the charges are functionally independent and nontrivial.

**Fine print.** One mode is not enough. At $u=\varepsilon\cos kx$ the gradients of $\frac12\int u^2$ and $\frac12\int u_x^2$ are proportional, although their symbols $1$ and $k^2$ are independent.

### 10.5 The generating symbol (Proposition 7.5)

**Idea.** Computing each $Q_n$ and then its symbol is laborious. All the symbols can be found at once. A quadratic functional is determined by its values on plane waves ([T11](#t11-plane-waves-dispersion-and-quadratic-symbols)), and at quadratic order only the *linearised* branch matters. The linearised sewing equation can be solved exactly in $\epsilon$, because for a plane wave every derivative becomes multiplication by $ik$ or $-i\omega$. So: insert one plane wave into $\mathcal G$, solve the linearised sewing equation exactly, and average over $x$. The result is $m(k;\epsilon)=\sum_n\epsilon^nm_n(k)$ in closed form. A nonzero $m_n$ also shows that $Q_n$ is nontrivial.

**Sine-Gordon, worked out.** Linearise the left sewing equation $\phi_x=\psi_t-\partial_\phi\mathcal B$ in $\phi$ and $\Delta=\psi-\phi$, with $\epsilon=\sigma$. To linear order $\partial_\phi\mathcal B=-\Delta/(2\sigma)+\sigma(2\phi+\Delta)/2$, and multiplying by $2\sigma$,

$$(1-\sigma^2)\Delta+2\sigma\Delta_t=2\sigma(\phi_x-\phi_t)+2\sigma^2\phi .$$

Insert $\phi=a\,E$ and $\Delta=d\,E$, with $E=e^{i(kx-\omega t)}$, $k=\sinh\vartheta$, $\omega=\cosh\vartheta$. Then $D_x\to ik$ and $D_t\to-i\omega$. The coefficient of $\Delta$ factorises, $1-\sigma^2-2i\sigma\omega=(1-i\sigma e^{\vartheta})(1-i\sigma e^{-\vartheta})$, and $k+\omega=e^\vartheta$. Solving,

$$\frac da=\frac{2i\sigma e^{\vartheta}}{1-i\sigma e^{\vartheta}},\qquad 2+\frac da=\frac2{1-i\sigma e^{\vartheta}} .$$

To quadratic order, $\mathcal B=\frac1{4\sigma}\Delta^2+\frac\sigma4(2\phi+\Delta)^2$. A real plane wave $\eta(aE+\bar a\bar E)$ squared has $x$-average $2\eta^2\lvert a\rvert^2$. So the $x$-average of $\mathcal B$ is $\eta^2\lvert a\rvert^2m$ with

$$m(k;\sigma)=\frac12\Big(\frac{\lvert d/a\rvert^2}\sigma+\sigma\lvert2+d/a\rvert^2\Big)=\frac{4\sigma\,\omega\,e^{\vartheta}}{1+\sigma^2e^{2\vartheta}}=4\omega e^{\vartheta}\sum_{j\ge0}(-1)^j\sigma^{2j+1}e^{2j\vartheta}.$$

This is the first row of the table after Definition 7.6. Its order-$\sigma$ term $4\omega e^\vartheta$ is the symbol of $Q_1$ above. The coefficients are distinct powers of $e^\vartheta$, so they are linearly independent, and Theorem 7.4 applies.

**Fine print.** Two hypotheses keep the shortcut honest.

- *The quadratic part $F_2$ of the evolution is zero or a total $x$-derivative.* The shortcut replaces $t$-derivatives using the linearised equation. The error comes from the quadratic terms $F_2$ of the full equation $v_t=F[v]$. It enters through constant-coefficient operators, which commute with $D_x$. If $F_2$ is a total $x$-derivative, so is the error, and it averages to zero. This holds for sine-Gordon, NLS, mKdV, KdV and Boussinesq. It fails for Tzitzéica and for $a_r^{(1)}$ Toda with $r\ge2$, where $U'''(0)\ne0$.
- *Locality in the phase-space variables.* The potential $p$ with $u=p_x$ is not a local function of $u$. On a plane wave in $u$, the potential equation $p_t=3u^2-u_{xx}$ gives $p_t$ the average $6\eta^2\lvert a\rvert^2$, which the linearised flow misses. For KdV and mKdV the branch is therefore computed from the spatial Bäcklund relation, which involves only $u$ and $\Delta=q-p$. For KdV it is $(2+\epsilon D_x)\Delta=-2\epsilon u+\frac\epsilon2\Delta^2$, and Lemma 6.2 applies with $M=2$.

**The symbols of the published defects** (table after Definition 7.6). For sine-Gordon, NLS, KdV and mKdV, the symbols of different orders are distinct powers of $e^\vartheta$ or of $k$, up to a common factor. They are therefore independent, as Lemma 6.5 predicts from the boost or dilation weights. For Boussinesq the parameter is not produced by a symmetry, and the paper has only computational evidence: 18 nonzero symbols spanning a space of dimension at least 17.

A family is **nondegenerate** (Definition 7.6) if infinitely many $m_n$ are nonzero. The trivial relations $\psi=\pm\phi$ are degenerate.

---

## Part 11. The main theorem, hypothesis by hypothesis (§8)

### 11.1 The theorem (§8.1)

Theorem 8.1 composes the four links. Its proof is five lines long. What matters is what each hypothesis is about.

| hyp. | content | concerns | integrable theories only? |
|---|---|---|---|
| (A) | constant Poisson operator and (NR) | bulk dispersion | no: every massive theory in the table |
| (B) | momentum-conserving defect satisfying (I) | the defect | this is the Corrigan–Zambon condition |
| (C) | a nondegenerate family with a formal branch and independent symbols | the family of defects | **yes: integrability enters here** |
| (D) | an affine conservation law whose parts have defect charges | bulk kinematics and the defect | no: every relativistic theory has the Lorentz closure |
| (E) | (L), and commuting quadratic parts or (NR2) with (L′) | the charges produced | partly; automatic without linear parts |

The proof chain is: Theorem 3.3 (Link 1); Proposition 4.3 with Lemma 5.2 (Link 2); Theorem 6.4 (Link 3); Theorem 7.3 with (A) and (E), and Theorem 7.4 with (C) (Link 4).

**A thought experiment.** Take a massive relativistic scalar theory that is not integrable, and suppose it had a momentum-conserving Type-I defect. Then (A), (B), (D) and (I) hold automatically. Theorem 3.3 gives a Bäcklund relation, and Proposition 4.3 gives the conserved density $\mathcal E_d$ along it. Theorem 8.1 then says the defect cannot lie in a nondegenerate family with a regular transparent limit satisfying (E). Proving the Corrigan–Zambon conjecture along these lines therefore means proving that (B) forces (C).

The theorem's second conclusion, that every solution of the sewing system imposed at all $x$ is a pair of solutions, is Theorem 3.3(b).

### 11.2 Hypothesis (C) for relativistic Type-I defects (§8.2)

**Idea.** For one class of defects, the paper derives the first two requirements of (C) from momentum conservation: the family and its transparent limit (see [§12.1](#121-what-c-asks-for) for the four requirements). The class consists of Type-I defects between two copies of a relativistic scalar theory with $r$ fields, whose kinetic coupling is constant:

$$\mathcal L_d=\tfrac12\,\phi\cdot E\phi_t+\phi\cdot D\psi_t+\tfrac12\,\psi\cdot E\psi_t-\mathcal B(\phi,\psi),\qquad E^T=-E,\quad D=I-E .$$

The mechanism is the one already visible for sine-Gordon in [Part 5](#part-5-the-running-example-sine-gordon). Momentum conservation forces the defect potential $\mathcal B$ to split into one part that depends on a weighted average of the two fields and another that depends on their difference. The two parts are linked by a constraint that is bilinear in them. Scaling one part up and the other down by the same factor preserves the constraint, and that rescaling is the family. Propositions 8.2 and 8.3 restate Propositions 3.1 and 3.2 of the companion [structural paper](../defect_integrability_paper.md).

**How the proof goes.**

1. *Sewing equations.* They are $\phi_x=E\phi_t+D\psi_t-\mathcal B_\phi$ and $\psi_x=D^T\phi_t-E\psi_t+\mathcal B_\psi$, the several-field version of [Part 5](#part-5-the-running-example-sine-gordon).
2. *Insert them into the momentum balance.* The terms quadratic in the velocities cancel, because $D=I-E$ gives $DD^T=D^TD$ and $ED=DE$. The constant coupling is chosen so that this happens.
3. *Separate the balance by powers of the velocities.* The defect momentum $\widetilde P(\phi,\psi)$ is assumed to contain no time derivatives. The balance must hold for independent values of $\phi,\psi,\phi_t,\psi_t$ (off shell, [T1](#t1-fields-derivatives-and-local-functions)). The terms linear in the velocities fix the gradient of $\widetilde P$ as a linear combination of the gradients of $\mathcal B$. The velocity-free terms give the identity $\frac12(\lvert\mathcal B_\phi\rvert^2-\lvert\mathcal B_\psi\rvert^2)=U(\phi)-U(\psi)$.
4. *Change coordinates.* Use $q=\frac12(\phi-\psi)$, which measures how far $\psi$ is from $\phi$, and $w=\frac12(D^T\phi+D\psi)$, a weighted average. In these coordinates the gradient conditions read $\widetilde P_w=-\mathcal B_w$ and $\widetilde P_q=\mathcal B_q$.
5. *Use that $\widetilde P$ exists.* Its mixed second derivatives agree, so $\mathcal B_{wq}=0$, that is, $\mathcal B=f(w)+g(q)$. This is where momentum conservation does real work: it rules out any coupling between $w$ and $q$ in the defect potential.
6. *The constraint.* The velocity-free identity becomes
   $$U(w+Dq)-U(w-D^Tq)=\tfrac12\,f'(w)\cdot g'(q),$$
   which is bilinear in $(f',g')$. So $(f,g)\mapsto(\lambda f,\lambda^{-1}g)$ preserves it. By the converse in Proposition 8.2, every rescaled defect again conserves momentum. This is the family, requirement (C1).
7. *The transparent point.* Assume $g'(0)=0$ with $G=g''(0)$ invertible. Differentiating the constraint at $q=0$ gives $Gf'=4U'$. It follows that $G$ commutes with $U''$ everywhere. If the bulk potential cannot be split into independent pieces (irreducibility), then $G=\gamma I$ and $f=4U/\gamma$. The family then takes the normal form
   $$\mathcal B_\epsilon=\epsilon\,U(w)+\epsilon^{-1}\hat g(q),\qquad\hat g''(0)=4I .$$
8. *The formal branch.* As $\epsilon\to0$, the term $\epsilon^{-1}\hat g(q)$ is a stiff spring holding $q=0$, that is $\psi=\phi$. This is exactly the form of Lemma 6.6 ([§9.3](#93-gyroscopic-type-i-defects-lemma-66)), which gives the formal branch, requirement (C2). This is Theorem 8.4.
9. *What is left.* Nondegeneracy and independence, (C3) and (C4), and in (E) commuting quadratic parts or (NR2). The generating density is the defect energy $\mathcal B_\epsilon$. It is quadratic at the vacuum, so the charges have no linear parts, and (L) and (L′) are automatic. For one field there is a single dispersion branch, so (NR2) holds as well. The structural paper proves the remaining conditions for the whole class by a different route, equal-time canonicity.

**Sine-Gordon.** Here $E=0$ and $D=1$, so $w=\frac12(\phi+\psi)$ and $q=\frac12(\phi-\psi)$.
- The defect of [Part 5](#part-5-the-running-example-sine-gordon) has $f=2\sigma(1-\cos w)$ and $g=\frac2\sigma(1-\cos q)$.
- The constraint reads $U(w+q)-U(w-q)=\frac12f'g'=2\sin w\sin q$, which is the identity $\cos(w-q)-\cos(w+q)=2\sin w\sin q$.
- The transparent point has $\gamma=2/\sigma$, so $\hat g=4(1-\cos q)$, and the published defect is the member $\epsilon=2\sigma$ of the normal form. This normalised $\epsilon$ is twice the $\sigma$ used in [Part 5](#part-5-the-running-example-sine-gordon); both are parameters of the same family.

**Affine Toda $a_2^{(1)}$.** The defect of Bowcock, Corrigan and Zambon has exactly this form. Its coupling is $D=2(I-\pi)^{-1}$, with $\pi$ the Coxeter rotation of the root system, and its potential is $\sigma f(w)+\sigma^{-1}g(q)$. The checks confirm the splitting, the constraint and the transparent point $\hat g''(0)=4I$, so Theorem 8.4 applies. The same checks confirm the hypotheses of the structural paper's theorem. That theorem then gives involution and independence. The general paper's own Link 4 could not provide these, because $U'''(0)\ne0$ and (NR2) fails for Toda. This conclusion rests on the structural paper, which has not been reviewed independently.

**Fine print.**
- *Derivative-free defect momentum.* Definition 3.1 allows $\widetilde P$ to contain time derivatives; Proposition 8.2 assumes that it does not.
- *Constant coupling.* The theorem says nothing about defects whose kinetic term depends on the fields, nor about Type-II defects.
- *The transparent point is assumed, not derived.* It is a condition on the defect potential at the single point $q=0$. Without it, the rescaling family still exists, but nothing makes $\epsilon^{-1}\hat g(q)$ a stiff spring around $\psi=\phi$.
- *Irreducibility.* If the bulk potential splits into decoupled pieces, $G$ can have several eigenvalues and the pieces can be rescaled independently. The structural paper shows (its §9) that the resulting family need not commute. Assuming that $G$ is a multiple of $I$ can replace irreducibility.
- The identities of the proofs, for a general skew $E$ with three fields, and the sine-Gordon and Toda statements are checked in [`checks/check_type1_family.py`](checks/check_type1_family.py).

[Part 12](#part-12-a-closer-look-at-hypothesis-c) looks at hypothesis (C) more closely.

---

## Part 12. A closer look at hypothesis (C)

Hypothesis (C) is where the integrability of the bulk enters Theorem 8.1. This part covers four questions:
- what (C) asks for;
- how strong it is;
- how one checks it for a given defect;
- what is known about deriving it from momentum conservation.

The paper derives it for one class, assuming a transparent point (§8.2, explained in [§11.2](#112-hypothesis-c-for-relativistic-type-i-defects-82)), and states that it is open in general (§10). The assessments in [§12.4](#124-could-c-follow-from-momentum-conservation-alone) are the guide's reading of the evidence.

### 12.1 What (C) asks for

Hypothesis (C) bundles four requirements on the defect $S_d$.

| | requirement | in the paper | sine-Gordon |
|---|---|---|---|
| (C1) | **A family.** $S_d$ is one member of a one-parameter family $S_d^{(\epsilon)}$ of momentum-conserving defects, or of promoted relations (Lemma 5.5). | Def. 6.1 | the parameter $\sigma$ |
| (C2) | **A regular transparent limit.** As $\epsilon\to0$ the family forces $\psi\to g(\phi)$. The fields $\psi$ and $\lambda$ then have power series in $\epsilon$, with local coefficients, that solve every sewing equation: a formal branch. | Def. 6.1, Lemmas 6.2 and 6.6 | $\sigma\to0$ forces $\psi\to\phi$ |
| (C3) | **Nondegeneracy.** Infinitely many of the quadratic symbols $m_n$ of the resulting charges are nonzero. | Def. 7.6 | every odd $n$ |
| (C4) | **Independence.** The nonzero symbols are linearly independent functions of $k$. | Thm 8.1(C), Lemma 6.5 | distinct powers of $e^\vartheta$ |

(C1) and (C2) are what Theorem 6.4 needs to produce local conservation laws at all. (C3) and (C4) make sure that infinitely many of them are different.

### 12.2 How strong is it?

**Strong enough to carry integrability.** Take a massive relativistic scalar theory. Then (A) holds whatever the potential. Energy always has a defect charge, momentum has one by (B), and the Lorentz closure holds, so (D) is automatic too. (E) holds whenever the generating density has no linear part, as for sine-Gordon. For such theories Theorem 8.1 reads: a momentum-conserving defect satisfying (I) and (C) forces infinitely many independent commuting charges. So in a massive theory that is not integrable, (C) must fail for every momentum-conserving defect. (C) is not a mild technical condition. In this setting it is at least as strong as integrability itself.

**But it is a finite statement.** Integrability asks for infinitely many charges. (C) asks for one family of defects and one generating function. The economy is the same as that of a Lax pair, or of a Bäcklund transformation with a free parameter: one object encodes a whole hierarchy. In soliton theory, a Bäcklund transformation with a free parameter that reduces to the identity at some value is a familiar sign of integrability. (C) is the defect version of that sign.

**Which parts carry the weight.** On their own, (C1) and (C2) are cheap. Every theory has a family with a regular transparent limit, if one allows relations that are not defects. Take the translations $\psi(x,t)=\phi(x+\alpha,t)$.
- As a formal series, $\psi=\phi+\alpha\phi_x+\frac12\alpha^2\phi_{xx}+\dots$. The coefficients are local, and $\psi=\phi$ at $\alpha=0$.
- Along this family, the natural conserved density is the energy between $x$ and $x+\alpha$, $\int_x^{x+\alpha}T^{00}(x',t)\,dx'$, with flux $\int_x^{x+\alpha}T^{10}(x',t)\,dx'$.
- Its expansion in $\alpha$ gives the energy density at first order, and total $x$-derivatives of it at every higher order.
- Its quadratic symbol is $\alpha$ times the symbol of the energy density: a polynomial in $\alpha$ with a single nonzero coefficient.

The family is degenerate. It produces only the Noether charge of the symmetry that generates it. (This is a thought experiment of the guide, not an example from the paper. The translation family is not a family of defects in the sense of Definition 3.1, because at finite $\alpha$ the relation between $\psi(0,t)$ and the data of $\phi$ at $x=0$ is not a local sewing equation.)

Relations built from internal symmetries behave in the same way; Remark 3.4.2's $\psi=-\phi$ is an example. So (C3) is the heart of (C): the family must not be the orbit of a bulk symmetry in disguise. The families of the observed cases pass this test. Each is either the orbit of a kinematic symmetry acting on a defect that is *not* invariant under it, or a modulus of the momentum constraint, and in neither case is the defect relation induced by a symmetry of the bulk Lagrangian. Once (C3) holds, (C4) is usually easy to check ([§12.3](#123-how-to-check-c-for-a-given-defect), step 3).

### 12.3 How to check (C) for a given defect

The steps below follow the order in which the paper treats the observed cases in §9.

**Step 1: find a family.** There are two sources.

- *Kinematic orbits.* Apply a symmetry of the bulk that the defect does not share.
  - For a dilation, Lemma 5.4 says the rescaled defects are automatically momentum-conserving when the bulk Lagrangians are strictly homogeneous.
  - For a Lorentz boost, check that the boosted relation is again of sewing form, with a local defect momentum, by rerunning the momentum-balance check.

  For sine-Gordon the boost works because of the light-cone structure of the sewing relations:
  $$(\partial_x-\partial_t)(\phi+\psi)=-\tfrac2\sigma\sin\tfrac{\phi-\psi}2,\qquad(\partial_x+\partial_t)(\phi-\psi)=-2\sigma\sin\tfrac{\phi+\psi}2 .$$
  A boost multiplies the two light-cone derivatives $\partial_x\pm\partial_t$ by reciprocal factors $e^{\pm\theta}$. Since $\sigma^{-1}$ and $\sigma$ sit on opposite light-cone derivatives, both relations keep their form, with $\sigma$ replaced by $\sigma e^{-\theta}$. A relation without this structure would in general acquire new terms under a boost.
- *Moduli.* Solve the momentum constraint and look for free parameters in its solutions. A constraint of product form has one automatically. For sine-Gordon the constraint is $2f'g'=U(\phi)-U(\psi)$ ([Part 5](#part-5-the-running-example-sine-gordon)). It is unchanged by $(f,g)\mapsto(\sigma f,\sigma^{-1}g)$, and this rescaling is the parameter $\sigma$.

  Proposition 8.2 of the paper proves that the same happens for every relativistic Type-I defect with several fields and a constant gyroscopic coupling ([§11.2](#112-hypothesis-c-for-relativistic-type-i-defects-82)). Momentum conservation forces the defect potential to split as $\mathcal B=f(w)+g(q)$, in coordinates $q=\frac12(\phi-\psi)$ and $w=\frac12(D^T\phi+D\psi)$ adapted to the coupling matrix $D$. The constraint becomes $U(w+Dq)-U(w-D^Tq)=\frac12f'(w)\cdot g'(q)$, which has the same rescaling.

**Step 2: find the transparent limit.** Look for an end of the parameter range at which the defect forces $\psi=g(\phi)$.

- Write the left sewing equation as $G(\phi,\Delta;\epsilon)=0$ for $\Delta=\psi-g(\phi)$. Check the two conditions of Lemma 6.2: at $\epsilon=0$ the equation is algebraic in $\Delta$ with invertible linear part, and derivatives of $\Delta$ come only with positive powers of $\epsilon$.
- For gyroscopic Type-I defects this is the stiff-spring condition of Lemma 6.6. The part of the defect potential that blows up as $\epsilon\to0$ must vanish to second order on the diagonal $\psi=\phi$, with an invertible Hessian there.
- For a rescaling modulus, $\sigma^{-1}g$ is the stiff spring, so the condition is $g'(0)=0$ with $g''(0)$ invertible.
- For a boost orbit, the transparent limit $\sigma e^{-\theta}\to0$ is the limit of infinite rapidity.

Then check the remaining sewing equations. This can be done either order by order, as `check_hierarchy.py` does to finite order, or for all orders at once by Lemma 3.5.

**Step 3: compute the generating symbol.** When Proposition 7.5 applies, $m(k;\epsilon)$ comes out in closed form.

- (C3) holds exactly when $m(k;\epsilon)$ is not a polynomial in $\epsilon$. A power series with only finitely many nonzero coefficients is a polynomial. The translation family fails here: its symbol is $\alpha$ times a fixed function.
- Suppose $m$ has the geometric form $m=A(k)\,\epsilon^a/\big(1-\epsilon^bB(k)\big)$, with $A$ not identically zero and $A$ and $B$ analytic. Then its coefficients are $A\,B^j$, and they are linearly independent exactly when $B$ is not constant. A linear relation $\sum_jc_j\,A\,B^j=0$ says that a polynomial vanishes on all values taken by $B$ where $A\ne0$, and there are infinitely many such values when $B$ is not constant. All four closed forms in the paper have this geometric form:

  | bulk | $m(k;\epsilon)$ | $A$ | $a$ | $B$ |
  |---|---|---|---|---|
  | sine-Gordon | $4\epsilon\,\omega e^{\vartheta}/(1+\epsilon^2e^{2\vartheta})$ | $4\omega e^{\vartheta}$ | 1 | $-e^{2\vartheta}$ |
  | NLS | $-2\epsilon/(1+\epsilon^2k^2)$ | $-2$ | 1 | $-k^2$ |
  | KdV | $2\epsilon^3/(4+\epsilon^2k^2)$ | $\frac12$ | 3 | $-\frac14k^2$ |
  | mKdV | $-4\epsilon/(1+\epsilon^2k^2)$ | $-4$ | 1 | $-k^2$ |

  In each case $b=2$. The counterexample $\frac{\epsilon}{1-\epsilon}m_*(k)$ of Lemma 6.5 is the case of constant $B=1$.
- Otherwise, compute finitely many $m_n$ and their rank. This gives evidence, not proof; for Boussinesq, 18 nonzero symbols span a space of dimension at least 17. When the family is a kinematic orbit, the weight argument of Lemma 6.5 can replace the computation.
- When Proposition 7.5 does not apply, as for Tzitzéica and $a_r^{(1)}$ Toda with $r\ge2$ where $U'''(0)\ne0$, the symbols must be computed from the charges themselves, order by order.

**Step 4: know what a finite computation establishes.**
- (C1) can be checked exactly.
- (C2) can be checked exactly when Lemma 6.2 or 6.6 applies, and otherwise only to the order computed.
- (C3) and (C4) can be checked exactly when the generating symbol is known in closed form or when Lemma 6.5 applies, and otherwise only as evidence.

### 12.4 Could (C) follow from momentum conservation alone?

The paper leaves this open (§10). What follows summarises the evidence; it is not a result.

**Evidence for.**

- *The observed cases.* In every observed case the published defect lies in a one-parameter family with a transparent limit (§9). In the four cases where the generating symbol is known in closed form, (C3) and (C4) hold.
- *The families were never postulated.* They came either from kinematic symmetries that the defect breaks or from moduli of the momentum constraint.
- *One class is proved.* Section 8.2 of the paper ([§11.2](#112-hypothesis-c-for-relativistic-type-i-defects-82)), restating the structural paper, treats massive relativistic Type-I defects with several fields, a constant gyroscopic coupling and a defect momentum without derivatives. For these, momentum conservation itself forces the splitting $\mathcal B=f(w)+g(q)$ and the rescaling family, (C1) (Propositions 8.2 and 8.3). With a transparent point, $g'(0)=0$ with $g''(0)$ invertible, and an irreducible bulk potential, the family has a formal branch, (C2) (Theorem 8.4). The structural paper then proves (C3), (C4) and involution for the same class (its Theorem 2.1). The published sine-Gordon and $a_2^{(1)}$ Toda defects satisfy these hypotheses. Within the class, what remains of (C) after momentum conservation is a nondegeneracy condition at a single point of the defect potential.
- *A simple mechanism.* In the relativistic Type-I class there is a simple reason for the moduli. The momentum constraint pairs the two halves $f$ and $g$ of the defect potential bilinearly, and a bilinear equation is unchanged when one factor is rescaled and the other inversely rescaled.

**Reasons for caution.**

- *One condition against infinitely many.* Momentum conservation is a single condition, while (C) yields infinitely many charges. A proof must use the rigidity of the momentum constraint as a functional equation, not merely the existence of a solution.
- *A different route may be needed.* Corrigan and Zambon found that momentum conservation severely restricts the bulk, and that in every class they analysed only integrable bulks admit such defects. If that bulk selection holds in general, then (B) ⇒ (C) may be true for a classification reason: (B) has solutions only for integrable bulks. A proof might then have to go through bulk selection rather than through a direct construction of the family.
- *Degenerate families exist.* The translation family above and the symmetry relations of Remark 3.4.2 show that families with transparent limits can be degenerate. Any derivation of (C) must show that the family supplied by momentum conservation is not a symmetry orbit in disguise.
- *Not every momentum-conserving defect can become transparent.* A defect between two different theories, such as Liouville and a free massless field, satisfies (B) but has no transparent limit. So (B) ⇒ (C) can only be expected for defects that join a theory to itself. A realistic target is the form proved in §8.2 and the structural paper: momentum conservation plus a transparent point implies (C).
- *Outside the relativistic Type-I class, no general mechanism is known.* This covers Type-II defects, several fields with equal masses, and non-relativistic theories without a dilation, such as Boussinesq. There, (C) has only been checked case by case.

**Summary.** For defects that join a massive relativistic theory to itself, (B) ⇒ (C) is proved in one natural class, with the transparent point assumed: (C1) and (C2) in §8.2 of the paper, (C3) and (C4) in the structural paper. In general the implication is supported by every known example, but no mechanism is known that would prove it. It may also turn out to hold only because momentum conservation already selects integrable bulks.

---

## Part 13. Reading the table of cases (§9)

The table in §9 records, for each observed case, how each hypothesis of Theorem 8.1 was established for the published defect. "Checked" means verified by exact computation, to the stated order where a series is involved. "Lemma 6.6 (all orders)" and "all orders from the compatibility of …" are proofs. Points to notice:

- **Fully covered.** Sine-Gordon, NLS, KdV and mKdV satisfy every hypothesis (comment 6). For these four, Theorem 8.1 is a theorem about the published defects.
- **Massless theories.** For Liouville, conformal Toda and the free massless field, (NR) fails. Only Link 1 applies: the momentum-conserving defects are Bäcklund relations to free fields. These theories are integrable in the sense of being linearisable, which is a different mechanism.
- **Affine Toda, $r\ge2$.** Links 1–3 hold, and for $a_2^{(1)}$ Theorem 8.4 derives the family from momentum conservation. The paper's own Link 4 is open on two counts: Proposition 7.5 does not apply because $U'''(0)\ne0$, and (NR2) fails because of the pairs of particles of equal mass. For $a_2^{(1)}$ the structural paper's theorem supplies involution and independence instead (§9, comment 4).
- **Tzitzéica.** $Q_1$ is nontrivial, and $Q_2$ and $Q_3$ are conserved but trivial. This matches the absence of a spin-3 charge in the Tzitzéica hierarchy.
- **Boussinesq.** Charges appear at orders 2, 4 and 5 but not 3, matching the absence of charges with spin divisible by three. Its parameter is a modulus, not produced by a symmetry, so the weight argument of Lemma 6.5 is unavailable and independence is evidence only.

---

## Part 14. What is open (§10)

1. **Hypothesis (C) from momentum conservation alone.** This is the real gap. In the observed cases the family arises either as the orbit of a symmetry that the defect does not share (boosts, dilations), or as a free parameter of the momentum constraint (the Boussinesq $\sigma_0$; the splitting $\mathcal B=F+G$ with $(F,G)\mapsto(\sigma F,\sigma^{-1}G)$). A general theorem would show that one of these always happens, with a regular transparent limit and nondegeneracy. [Part 12](#part-12-a-closer-look-at-hypothesis-c) discusses the evidence. Section 8.2 proves a statement of this kind for one class, relativistic Type-I defects with constant kinetic coupling: there momentum conservation forces the splitting and supplies the rescaling family and its formal branch, given a transparent point ([§11.2](#112-hypothesis-c-for-relativistic-type-i-defects-82)). The transparent point itself is not derived.
2. **Bulk selection.** Corrigan and Zambon found that momentum conservation restricts the bulk potential. The framework does not classify potentials. Its conclusion is conditional on (C).
3. **Remaining verifications.** Formal branches for several-field Type-II defects; involution and independence for affine Toda with $r\ge2$, which needs a version of Proposition 7.5 that keeps the quadratic nonlinearity; (L) and (L′) for Boussinesq.
4. **Analysis.** Everything is formal or local. Convergence of the series in $\epsilon$ and global Bäcklund maps are not addressed.

---

## Part 15. Catalogue of counterexamples

Each example shows that a hypothesis cannot be dropped. All are computed in [`checks/check_scope.py`](checks/check_scope.py) except the $w\ne0$ and massless examples, which are immediate. The toy version of the (I) example is in [`checks/check_guide_example.py`](checks/check_guide_example.py).

| hypothesis | example | what goes wrong | paper |
|---|---|---|---|
| regularity in the converse of Lemma 3.2 | Klein–Gordon, $\mathcal L_d=\lambda(\psi-\phi)^2$ | momentum conserved on solutions, but the off-shell balance fails: the multiples of $C$ are too few | §3.2 |
| (I) in Theorem 3.3(b) | $\mathcal L_d=\lambda(\psi+\phi)$, even potential | the promoted solution $(x^2,-x^2,2x)$ is not a bulk solution | Remark 3.4.2 |
| off-shell triviality in Lemma 4.1 | KdV mass law; defect plus $\beta p^2$ | a density that is an $x$-derivative need not have a defect charge | §4.1 |
| strict homogeneity in Lemma 5.4 | free bulk plus $D_x(\frac12w^2)$ | the rescaled defect violates the balance for $s\ne1$ | §5.2 |
| $w\ne0$ in Lemma 6.5 | $\frac\epsilon{1-\epsilon}m_*(k)$ | infinitely many proportional symbols | §6 |
| condition 4 in Lemma 6.5 | $U_tV_t-U_xV_x$ in variables $q=U-V^2$, $r=V$ | the charge scales by $a$, its quadratic part by $a^{-2}$ | §6 |
| momentum conservation in Lemma 6.6 | stiff spring $-(\phi-\psi)^2/(2\epsilon)$ | the right sewing equation forces $\epsilon\phi_{xx}=0$ | §6 |
| (NR) | massless $\omega=\lvert k\rvert$ | waves resonate on an open set | §7.1 |
| (L′) in Theorem 7.3 | free Hamiltonian in coordinates $(q+f,p)$ | the quadratic part of a charge is not conserved by the linearised flow | §7.2 |
| several modes in Theorem 7.4 | $u=\varepsilon\cos kx$ | gradients proportional although the symbols are independent | §7.2 |
| locality in Proposition 7.5 | KdV potential $p$ | $p_t$ has a nonzero average that the linearised flow misses | §7.2 |
| (NR2) in Theorem 8.1 (E) | two free fields of equal mass | two conserved quadratic charges that do not commute | §8 |
| normalisation in Appendix A | $\mathcal L_+$ with an added constant $-c$ | a Bäcklund relation with $\mathcal H_--\mathcal H_+=-c$ | App. A |

---

## Part 16. Where each statement is checked

The scripts are in [`checks/`](checks/). Each prints one `PASS` or `FAIL` line per check. They check identities and hypotheses on the published defects; they do not replace the written proofs.

| script | checks |
|---|---|
| `check_balance.py` | the momentum balance (3.3) for every observed defect |
| `check_tangency.py` | Theorem 3.3(a) exactly for sine-Gordon, Tzitzéica (Type II) and KdV (order 2, multiplier) |
| `check_kinematics.py` | the closure table of Lemma 5.2, the boost and dilation families, (NR) at degrees 3 and 4 |
| `check_hierarchy.py` | formal branches, every promoted sewing equation, conservation and nontriviality of each $Q_n$ to finite order |
| `check_symbols.py` | the generating symbols of Proposition 7.5 |
| `check_scope.py` | the counterexamples of [Part 15](#part-15-catalogue-of-counterexamples), and the identities behind (NR) and Proposition 7.5 |
| `check_type1_family.py` | the identities in the proofs of Propositions 8.2–8.3 for a general skew coupling with three fields, the sine-Gordon normalisation, and the hypotheses of Theorem 8.4 for the $a_2^{(1)}$ Toda defect |
| `check_guide_example.py` | the examples of this guide: the mechanical toy of Part 3 (the derivatives of $h$, the spring, the oscillator, the auxiliary-variable failure), the sine-Gordon formulas (balance, $\mathcal E_d=\mathcal B$, $\Delta_1$, $Q_1$, the closed form of $m(k;\sigma)$ and its first coefficients), and the two examples of Part 12 (the light-cone form of the sine-Gordon relations, the symbol of the translation family) |

The Lean project in [`lean/`](lean/) checks the final algebraic step of several lemmas, with the variational and analytic inputs as named hypotheses. Theorem 8.1 is not formalised. [verification.txt](verification.txt) records the output of a full run; it does not yet include `check_guide_example.py`.

---

## Part 17. What comes from the literature, and what the paper brings in

The following says, for each link, which ideas the paper takes from earlier work and which tools it brings in. Numbers in brackets are the paper's references. "Brought in" means *not used in the defect papers the paper cites*. It does not mean "new". The paper states that it has not searched the literature systematically for earlier versions of its general statements, and it claims no novelty for them.

**Link 1: momentum conservation gives a Bäcklund relation.**

- *From the literature.*
  - The observation itself: sewing conditions that conserve momentum turn out to be Bäcklund transformations frozen at $x=0$. Bowcock, Corrigan and Zambon, and then Corrigan and Zambon, found this model by model, by direct computation [1–8].
  - The view of a defect as a frozen Bäcklund transformation, in Caudrelier's inverse-scattering approach [12]. That approach starts from an integrable bulk.
  - The description with $x$ as the evolution direction: the spatial phase space of $t$-histories. It is taken from the multisymplectic treatment of Caudrelier and Kundu [13], in which spatial and temporal Hamiltonian descriptions coexist.
  - The geometric fact that a generating function defines a Lagrangian correspondence (Weinstein [19]). The paper uses it only in Appendix A.
  - The mechanical fact of [Part 3](#part-3-the-guiding-picture-a-jump-in-classical-mechanics), that a canonical transformation preserving the Hamiltonian maps trajectories to trajectories, is textbook classical mechanics.
- *Brought in.*
  - A general proof (Theorem 3.3) for any finite-order bulk Lagrangian and any local defect functional. It works in the formal variational calculus of Olver [16]. It applies the time-Euler operator to the momentum balance written as an off-shell identity, then uses the chain rule for Euler operators and the Helmholtz self-adjointness of the second variation. Ostrogradsky momenta handle higher-order bulks such as KdV in potential form.
  - The treatment of auxiliary defect fields and Lagrange multipliers. It uses a multiplier $\rho$ and isolates the injectivity condition (I).
  - Counterexamples showing that (I) and the off-shell form of the balance are needed.

**Link 2: one conserved density along the relation.**

- *From the literature.*
  - Defect contributions to energy and momentum, which Bowcock, Corrigan and Zambon, and Corrigan and Zambon, construct for each model [1–8].
  - The observation that a Lorentz boost changes the sine-Gordon defect parameter by $\sigma\to\sigma e^{\pm\theta}$, which is the origin of the spectral parameter [1].
  - Caudrelier's generating function for the modified conserved quantities [12]. It is obtained by inverse scattering in an integrable bulk.
  - Noether's theorem, and the symmetry of the stress tensor in Lorentz-invariant theories, which are standard.
- *Brought in.*
  - Defect charges recast as spatial potentials for the difference of the bulk currents along promoted solutions (Proposition 4.2). Their normalisation is proved from a spatial normal form of the field equations (Lemma 6.3).
  - The closure relation, read off from any conservation law whose current is affine in $(x,t)$ (Lemma 5.2). It turns a defect charge into a conserved generating density without assuming integrability.
  - One table covering the Lorentz boost, Galilean boosts, dilations and a time-linear shift.

**Link 3: a family and its transparent limit.**

- *From the literature.*
  - Expanding a Bäcklund transformation in its parameter to generate conservation laws. This is a classical technique of soliton theory; the best-known instance is the expansion of Miura, Gardner and Kruskal (1968) for KdV.
  - For the specific models, the paper's all-orders statements rest on the compatibility of the classical Bäcklund transformations of Wahlquist and Estabrook (KdV) [17], Wadati (mKdV) [18] and Lamb (NLS) [20].
  - The defect parameters themselves, and the splitting $(F,G)\mapsto(\sigma F,\sigma^{-1}G)$ of the relativistic Type-I defect potential, found for one field and for affine Toda [1, 2, 4].
  - The derivation of that splitting and rescaling from momentum conservation for every relativistic Type-I defect with constant coupling (§8.2). It restates Propositions 3.1 and 3.2 of the companion structural paper [23], which belongs to the same project and has not been reviewed independently.
- *Brought in.*
  - Two general sources of one-parameter families: dilation orbits of momentum-conserving defects (Lemma 5.4) and Lorentz orbits of Bäcklund relations (Lemma 5.5).
  - A formal implicit-function lemma that says when a transparent limit gives series with local coefficients (Lemma 6.2). The argument is standard, and the paper applies it to sewing equations. Lemma 6.6 combines it with Lemma 3.5 for the gyroscopic Type-I defects.
  - The weight argument (Lemma 6.5): charges are eigenvectors of a kinematic symmetry with distinct eigenvalues, so they are independent.

**Link 4: involution and independence.**

- *From the literature.*
  - Liouville integrability in the presence of defects, studied for specific classes by Avan and Doikou [15] and by Bristow and Bowcock [10].
  - These works, and Caudrelier's [12, 13], start from an integrable bulk with its Lax pair or $r$-matrix. The traditional route to commuting charges from Bäcklund transformations is Bianchi permutability.
- *Brought in.*
  - A perturbative rigidity argument based on nonresonance of the bulk dispersion relation (Lemma 7.2, Theorem 7.3). It is familiar from the perturbation theory of Hamiltonian partial differential equations, but it is not used in the cited defect papers. It needs no Lax pair and no Bianchi permutability.
  - An independence criterion through quadratic symbols (Theorem 7.4).
  - A closed-form generating symbol computed from a single plane wave (Proposition 7.5).
  - The companion [structural paper](../defect_integrability_paper.md) uses the same rigidity idea for massive relativistic Type-I defects.
