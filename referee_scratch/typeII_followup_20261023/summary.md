# A one-auxiliary Type-II defect from an inverse momentum problem

23 October 2026 · Codex (GPT-6) · Calculation based on repository commit `a744c789c15ee659e67abd33d4480308360c6198`.

An inverse search for momentum-conserving defects, within a restricted exponential ansatz, produced the bulk potential

$$
U(X,Y)=e^Y\cosh X+\tfrac12 e^{-2Y}-\tfrac32.
$$

This is the known $D_3^{(2)}$ affine Toda theory. Further investigation identifies the candidate defect as an exact, consistent reduction of Bristow's $D_4^{(1)}$ defect and supplies a defect Lax representation.

## The defect

Let $u=(u_1,u_2)$ and $v=(v_1,v_2)$ be the left and right fields, with canonical bulk kinetic terms and potential $U$. Define

$$
p=\frac{u_1+v_1}{2},\quad q=\frac{u_1-v_1}{2},\quad
z=\frac{u_2+v_2}{2},\quad w=\frac{u_2-v_2}{2}.
$$

With one auxiliary field $\ell(t)$ and parameter $\sigma>0$, take

$$
L_d=u_1\dot v_1+(u_2-v_2)\dot\ell-F-G,
$$
$$
\begin{aligned}
F&=\sigma\left[2\cosh p\,e^{(z+\ell)/2}+\cosh^2w\,e^{-z-\ell}\right],\\
G&=\sigma^{-1}\left[2\cosh q\cosh w\,e^{(z-\ell)/2}+e^{-z+\ell}\right].
\end{aligned}
$$

This is a mixed Type-I/Type-II defect. With bulk momentum convention $P_{\rm bulk}=-\int\phi_t\cdot\phi_x\,dx$, its momentum contribution is $G-F$.

## Exact reduction of the known defect

Use [Bristow's equations (2.4.4), (2.4.10) and (2.4.11)](https://arxiv.org/pdf/1709.03927), with the arbitrary gauge function set to zero. Write $P_i,Q_i$ for the parent half-sums and half-differences, $\mu_2,\mu_3$ for its auxiliary variables, and $D,\bar D$ for its two potential pieces. The map is

$$
\begin{gathered}
P=(p,-z,z,p),\qquad Q=(q,-w,w,q),\\
\mu_2=\frac{\ell-z}{2}+\frac23\log2,\qquad
\mu_3=\frac{z-\ell}{2}+\log\cosh w+\frac13\log2,\\
\sigma_4=2^{-1/6}\sigma.
\end{gathered}
$$

Divide the restricted action by two and rescale spacetime by $\sqrt2$. Then $D/(2\sqrt2)=F$ and $\bar D/(2\sqrt2)=G$; the kinetic terms agree up to a total derivative.

Consistency follows from a symmetry of the complete parent action. In the auxiliary gauge $n_j=\mu_j-\tfrac12\log(2\cosh Q_j)$, the symmetry acts on each bulk field as $(a,b,c,d)\mapsto(d,-c,-b,a)$ and on the auxiliaries as $(n_2,n_3)\mapsto(-n_3,-n_2)$. The map above lies in its fixed subspace. The discarded equations therefore impose no extra constraints.

## Lax representation and scope

Substitution into Bristow's $8\times8$ defect matrix, equations (3.2.3) and (3.4.17)–(3.4.19), gives a defect Lax representation for this candidate. The parent matrix's complete zero-curvature identity was independently checked, rather than assumed from the publication.

The accompanying [reduction script](check_d4_reduction.py) passes 12 exact checks. The [Lax script](check_lax.py) passes five, including all 128 scalar entries of the zero-curvature identity after separating the two powers of the defect parameter. Run both with Python and SymPy.

The inverse construction thus found a valid defect without prescribing the bulk theory. Its origin in a known defect is now explicit. Whether this particular one-auxiliary reduction has appeared previously remains unresolved; no novelty claim is made. The Lax representation also leaves the Poisson commutativity and functional independence required for full Liouville integrability to be established.
