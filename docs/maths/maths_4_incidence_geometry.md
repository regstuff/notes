# Maths 4 - Incidence Geometry

A convention used here: Vector spaces are right vector spaces, with scalars written on the right and coordinates as column vectors, whereas the earlier projective geometry notes used left vector spaces. The prologue explains why this changes nothing over a field ([right vector spaces](#linear-algebra-over-finite-fields)).


## Prologue: The Linear Algebra We Need

Incidence geometry is concerned with point-line geometries, which is a fancy way of saying "how points connect to each other with lines." One important aspect is to figure out what sort of point-line geometries (or connections between points via lines) are allowed and not allowed over various fields and within various constraints. Surprisingly, some pretty simple matrics which contain just $1$s and $0$s can tell us a lot when we apply the tools of linear algebra on them.

Most of what follows is core linear algebra, with a few items a physics degree may have skipped. Each topic gets a small example and a line saying where it is used. One example runs throughout:

$$A = \begin{pmatrix} 0 & 1 & 1 \\ 1 & 0 & 1 \\ 1 & 1 & 0 \end{pmatrix}.$$

Label the corners of a triangle $1, 2, 3$, and put a $1$ in row $x$, column $y$ when corners $x$ and $y$ are joined by an edge, and $0$ otherwise. The result is $A$, which the next chapter calls [the adjacency matrix](#the-adjacency-matrix-and-its-eigenvalues) of the triangle.

### Eigenvalues and eigenspaces

A number $\theta$ is an eigenvalue of a square matrix $A$ when $Av = \theta v$ for some nonzero vector $v$. The eigenvectors for $\theta$, together with $0$, form the eigenspace $V_\theta = \ker(A - \theta I)$. Two numbers measure how much of $\theta$ there is. The *algebraic multiplicity* is its multiplicity as a root of the characteristic polynomial $\det(XI - A)$. The *geometric multiplicity* is $\dim V_\theta$. The second is never larger than the first, and $A$ is diagonalizable exactly when the two agree for every eigenvalue.

For the running example, $\det(XI - A) = (X-2)(X+1)^2$. The eigenvalue $2$ has the eigenvector $j = (1,1,1)^T$, because every row of $A$ sums to $2$. For $\theta = -1$, note that $(Ax)_i = (x_1 + x_2 + x_3) - x_i$. Since $Av = \theta v$, we have $(x_1 + x_2 + x_3) - x_i = -1\cdot x_i$ and cancelling the $x_i$ on both side, we see every vector in the plane $x_1 + x_2 + x_3 = 0$ is an eigenvector. That plane has dimension $2$, equal to the algebraic multiplicity. Compare

$$N = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix},$$

whose characteristic polynomial is $(X-1)^2$ but whose only eigenvectors are the multiples of $(1,0)^T$. Its two multiplicities are $2$ and $1$, and it cannot be diagonalized.

Similar matrices $P^{-1}AP$ (where $P$ represents a change of basis and is invertible) have the same characteristic polynomial, so they have the same eigenvalues with the same multiplicities.

**Where it is used.** The next chapter shows that the eigenvalues of a graph do not depend on how its vertices are labelled ([the adjacency matrix and its eigenvalues](#the-adjacency-matrix-and-its-eigenvalues)). In the chapter on [strongly regular graphs](#the-adjacency-matrix-of-a-strongly-regular-graph), the decisive test is that a multiplicity, being the dimension of an eigenspace, must be a whole number.

### Real symmetric matrices and the spectral theorem

Almost every matrix in the graph chapters is real and symmetric, and such matrices are as well behaved as matrices get. Their eigenvalues are real. Eigenvectors for different eigenvalues are orthogonal: if $Au = \theta u$ and $Av = \tau v$, then

$$\theta \langle u, v\rangle = \langle Au, v\rangle = \langle u, Av\rangle = \tau \langle u, v\rangle,$$

so $\langle u, v\rangle = 0$ when $\theta \neq \tau$. And there is an orthonormal basis of eigenvectors, so the two multiplicities always agree and we can simply say "multiplicity".

The spectral theorem packages all this. Let $E_\theta$ be the [orthogonal projector](#projectors-trace-and-positive-semidefinite-matrices) onto $V_\theta$. Then

$$A = \sum_\theta \theta E_\theta, \qquad \sum_\theta E_\theta = I, \qquad E_\theta E_\tau = 0 \ \text{ for } \theta \neq \tau.$$

This is the decomposition of an observable in quantum mechanics, with $E_\theta = \sum |v\rangle\langle v|$ over an orthonormal basis of $V_\theta$.

In the running example, the projector onto the line through $j$ is $E_2 = jj^T/3$, with every entry $1/3$, and the projector onto the plane is $E_{-1} = I - E_2$, with diagonal entries $2/3$ and off-diagonal entries $-1/3$. Then $2E_2 - E_{-1}$ has diagonal entries $0$ and off-diagonal entries $2/3 + 1/3 = 1$: it is $A$.

**Where it is used.** Adjacency matrices are real and symmetric, which is why a graph's eigenvalues are real ([the adjacency matrix and its eigenvalues](#the-adjacency-matrix-and-its-eigenvalues)). The decomposition $A = \sum_\theta \theta E_\theta$ is the backbone of [distance-regular graphs](#distance-regular-graphs), where $E_\theta$ is also called a minimal idempotent.

### Projectors, trace and positive semidefinite matrices

An **orthogonal projector** of a subspace $U$ is a matrix $E$ which takes a vector and returns the portion of the vector inside the subspace. Here's how it works. Every subspace $U \subseteq \mathbb{R}^n$ splits the entire space into two mutually perpendicular pieces: the target subspace $U$ (the image of $E$) and its orthogonal complement $U^\perp$ (the kernel of $E$), so that $\mathbb{R}^n = U \oplus U^\perp$. Every vector $v \in \mathbb{R}^n$ can be uniquely written as the sum of two perpendicular vectors: $v = v_\parallel + v_\perp$, where $v_\parallel \in U$ lies completely inside the subspace, and $v_\perp \in U^\perp$ is perpendicular to every vector in $U$.

When you multiply $v$ by the matrix $E$, it acts as a linear filter on those two components:

$$Ev = E(v_\parallel + v_\perp) = Ev_\parallel + Ev_\perp = 1\cdot v_\parallel + 0\cdot v_\perp = v_\parallel$$

It leaves the in-plane part $v_\parallel$ untouched (eigenvalue $1$). It annihilates the perpendicular part $v_\perp$ (eigenvalue $0$).

It's properties are $E^2 = E$ (doing it twice is the same as doing it once) and $E^T = E$ (it projects at right angles). Its eigenvalues are $0$ and $1$ as we saw: vectors in its image are fixed, and vectors orthogonal to the image are sent to $0$.

The trace, the sum of the diagonal entries, equals the sum of the eigenvalues counted with multiplicity, and $\operatorname{tr}(BC) = \operatorname{tr}(CB)$. For a projector the trace counts the eigenvalues equal to $1$, so $\operatorname{tr} E = \operatorname{rank} E$, the dimension of the image. In the running example $\operatorname{tr} E_2 = 3 \cdot \tfrac13 = 1$ and $\operatorname{tr} E_{-1} = 3 \cdot \tfrac23 = 2$, the dimensions of the two eigenspaces.

Trace equations pin down multiplicities. In the running example $\operatorname{tr} A = 0 = 2 + 2\cdot(-1)$, and $\operatorname{tr} A^2 = \sum_{i,l} A_{il}^2$, which for a symmetric matrix of zeros and ones counts its ones, is $6 = 2^2 + 2\cdot(-1)^2$. Knowing only the eigenvalues $2$ and $-1$ and that their multiplicities add up to $3$, either equation tells us how often each occurs.

A symmetric matrix $M$ is **positive semidefinite** when $x^T M x \geq 0$ for every vector $x$; equivalently, all its eigenvalues are $\geq 0$. Density matrices are the familiar case. Projectors are positive semidefinite, since $x^T E x = x^T E^T E x = |Ex|^2$.

**Where it is used.** In the chapter on [strongly regular graphs](#the-adjacency-matrix-of-a-strongly-regular-graph), the equation $\operatorname{tr} A = 0$ turns the eigenvalues into multiplicities. Positive semidefiniteness drives two inequalities proved there and in [distance-regular graphs](#distance-regular-graphs), the absolute bound and the Krein conditions.

### Polynomials in a matrix and the minimal polynomial

A polynomial $p(X) = c_0 + c_1 X + \dots + c_m X^m$ can be evaluated at a square matrix: $p(A) = c_0 I + c_1 A + \dots + c_m A^m$. Polynomials in the same matrix commute, and if $Av = \theta v$ then $p(A)v = p(\theta)v$: $p(A)$ has the eigenvalues $p(\theta)$ on the same eigenvectors.

The **minimal polynomial** of $A$ is the monic polynomial $m_A$ (leading coefficient $1$) of least degree with $m_A(A) = 0$; any nonzero scalar multiple of it is also called a minimal polynomial. It divides every polynomial that sends $A$ to $0$, including the characteristic polynomial (Cayley–Hamilton). Its roots are exactly the eigenvalues: if $Av = \theta v$ then $0 = m_A(A)v = m_A(\theta)v$, so $m_A(\theta) = 0$.

In the running example, $A^2$ has diagonal entries $2$ and off-diagonal entries $1$, so $A^2 = A + 2I$. Since $A$ is not a multiple of $I$, no polynomial of degree $1$ works, and

$$m_A(X) = X^2 - X - 2 = (X-2)(X+1).$$

It has degree $2$, although $A$ is $3 \times 3$ and its characteristic polynomial $(X-2)(X+1)^2$ has degree $3$.

You know minimal polynomials from field theory, where the minimal polynomial of an element $\alpha$ over a field $K$ is always irreducible. Here $m_A$ factors, and the difference is zero divisors. In a field, $g(\alpha)h(\alpha) = 0$ forces $g(\alpha) = 0$ or $h(\alpha) = 0$, so a factorization would produce a smaller polynomial. Matrices can multiply to zero without either being zero: $(A - 2I)(A + I) = 0$ here. For a matrix, "minimal" means least degree and nothing more.

The factorization carries information: a real matrix is diagonalizable over $\mathbb{R}$ exactly when its minimal polynomial has distinct real roots $\theta_1, \dots, \theta_s$. The reason is a set of projectors built from $A$:

$$E_i = \prod_{l \neq i} \frac{A - \theta_l I}{\theta_i - \theta_l},$$

the Lagrange polynomial that is $1$ at $\theta_i$ and $0$ at the other roots, evaluated at $A$. These add up to $I$, as the polynomials add up to $1$, and $(A - \theta_i I)E_i$ is a multiple of $m_A(A) = 0$, so each $E_i$ maps into the eigenspace of $\theta_i$; the eigenspaces fill the space. A repeated root signals failure ($N$ above has $m_N = (X-1)^2$, since $(N - I)^2 = 0 \neq N - I$), and so does a missing real root (a rotation by $90^\circ$ has $X^2 + 1$). For a real symmetric matrix, $m_A = \prod (X - \theta)$ over its distinct eigenvalues, so the degree of $m_A$ is the number of distinct eigenvalues, and the $E_i$ are exactly the orthogonal projectors onto the eigenspaces. In the example, $E_2 = (A + I)/3$ and $E_{-1} = (2I - A)/3$.

**Where it is used.** For [strongly regular graphs](#the-adjacency-matrix-of-a-strongly-regular-graph), a quadratic equation holds for the adjacency matrix on the vectors orthogonal to the all-ones vector, giving two eigenvalues there and, with one more on the all-ones vector, three in all. For [distance-regular graphs](#distance-regular-graphs), the degree of the minimal polynomial counts the eigenvalues. Projectors written as polynomials in $A$ appear in both.

### The all-ones matrix and commuting matrices

Write $j$ for the column vector with every entry $1$, and $J = jj^T$ for the square matrix with every entry $1$. The earlier projective geometry notes used $J$ for the matrix of a symplectic form; in these notes $J$ is always the all-ones matrix. For any $x$, $Jx = (x_1 + \dots + x_n)\,j$. So the $n \times n$ matrix $J$ has eigenvalue $n$ on $j$, and eigenvalue $0$ on the $(n-1)$-dimensional space $j^\perp$ of vectors whose entries sum to zero. Also $J^2 = nJ$.

Matrices of the form $aI + bJ$ come up constantly, and their eigenvalues can be read off: $a + nb$ once, on $j$, and $a$ with multiplicity $n - 1$, on $j^\perp$. Hence

$$\det(aI + bJ) = (a + nb)\,a^{n-1}.$$

The running example $A = J - I$ has eigenvalues $2$ once and $-1$ twice, as found above. In the next chapter the $7 \times 7$ matrix $2I + J$ appears; its eigenvalues are $9$ once and $2$ six times, and its determinant is $9 \cdot 2^6 = 576$, which is not zero.

Commuting symmetric matrices can be diagonalized together: if $AB = BA$ and $Av = \theta v$, then $A(Bv) = \theta\, Bv$, so $B$ maps each eigenspace of $A$ into itself and can be diagonalized inside it. The typical case: if every row and column of $A$ sums to $k$, then $AJ = JA = kJ$, so we may take $j$ as one eigenvector and all the others in $j^\perp$, where $J$ acts as $0$. On $j^\perp$, any equation in $A$, $I$ and $J$ loses its $J$ terms.

**Permutation matrices.** A permutation matrix $P$ has exactly one $1$ in each row and each column, and $0$ elsewhere. It is orthogonal, $P^T = P^{-1}$, and $PJ = JP = J$. Renumbering the rows and columns of $A$ by the same permutation replaces $A$ by the similar matrix $P^TAP$, with the same eigenvalues. And $P$ commutes with $A$ exactly when $P^TAP = A$, as every permutation of three indices does for the running example.

**Where it is used.** Relabelling a graph is conjugation by a permutation matrix ([the adjacency matrix and its eigenvalues](#the-adjacency-matrix-and-its-eigenvalues)). The matrix $2I + J$ counts incidences in the Fano plane ([point-line geometries](#point-line-geometries)), and a relative of it gives Fisher's inequality<!-- relink once Fisher's inequality is in these notes -->. Dropping $J$ on $j^\perp$ is the first step for [strongly regular graphs](#the-adjacency-matrix-of-a-strongly-regular-graph). The permutation matrices commuting with $A$ are the symmetries of a graph, and the matrices commuting with all of them form the commutant you know from group theory, which returns in [distance-regular graphs](#distance-regular-graphs).

### Rank, determinants and Gram matrices

The rank of a matrix is the dimension of its column space; for a symmetric matrix it is the number of nonzero eigenvalues, counted with multiplicity. The determinant is the product of the eigenvalues, so a square matrix is invertible exactly when its determinant is nonzero.

One rank fact does real work later. For a real matrix $M$,

$$\operatorname{rank}(MM^T) = \operatorname{rank} M.$$

The reason: if $MM^Tx = 0$, then $0 = x^TMM^Tx = |M^Tx|^2$, so $M^Tx = 0$; thus $MM^T$ and $M^T$ have the same kernel, hence the same rank. So if $M$ has $n$ rows and $MM^T$ is invertible, $M$ has at least $n$ columns. The step $|M^Tx|^2 = 0 \Rightarrow M^Tx = 0$ fails over $\mathbb{F}_2$: for $M = (1 \;\; 1)$, $MM^T = (2) = (0)$ although $M$ has rank $1$. This is one reason why the zero-one matrices of a geometry are taken over $\mathbb{R}$.

The **Gram matrix** of vectors $v_1, \dots, v_m$ in $\mathbb{R}^n$ is the $m \times m$ matrix $G$ with $G_{il} = \langle v_i, v_l \rangle$. If the $v_i$ are the columns of a matrix $V$, then $G = V^TV$. So $G$ is symmetric, positive semidefinite ($x^TGx = |Vx|^2$), and of rank equal to the dimension of the span of the $v_i$. It records the vectors up to rotation: their lengths and angles, nothing else.

Conversely, every positive semidefinite matrix $M$ of rank $r$ is a Gram matrix of vectors in $\mathbb{R}^r$. Write $M = \sum \theta\, uu^T$ over an orthonormal basis of eigenvectors $u$, with exactly $r$ of the $\theta$ positive. Stack the $r$ rows $\sqrt{\theta}\, u^T$ into a matrix $B$; then $M = B^TB$, the Gram matrix of the columns of $B$.

For example, three unit vectors in the plane at $120^\circ$ to each other have inner products $1$ and $\cos 120^\circ = -\tfrac12$, so their Gram matrix is

$$\begin{pmatrix} 1 & -\tfrac12 & -\tfrac12 \\ -\tfrac12 & 1 & -\tfrac12 \\ -\tfrac12 & -\tfrac12 & 1 \end{pmatrix} = \tfrac32\, E_{-1},$$

of rank $2$, as it must be for vectors in a plane. Read backwards, the projector $E_{-1}$ of the running example *is* a configuration of three vectors at $120^\circ$. Project the three standard basis vectors $e_i$ onto the plane $x_1 + x_2 + x_3 = 0$: the Gram matrix of the projections is $E_{-1}$ itself, because $\langle Ee_i, Ee_l\rangle = (E^TE)_{il} = E_{il}$. This is the idea behind the absolute bound for strongly regular graphs. A small eigenspace must hold one vector per vertex with only a few different angles between them, and there is a limit: $\mathbb{R}^m$ holds at most $m(m+3)/2$ unit vectors with only two different angles between them.

The **entrywise product** of two matrices of the same shape multiplies them entry by entry: $(B \circ C)_{il} = B_{il} C_{il}$. It is also called the Hadamard or Schur product. The **Schur product theorem** says that the entrywise product of two positive semidefinite matrices is positive semidefinite. With Gram matrices the proof is one line. Write $B$ as the Gram matrix of vectors $u_i$ and $C$ as the Gram matrix of vectors $w_i$; then $B \circ C$ is the Gram matrix of the tensor products $u_i \otimes w_i$, because

$$\langle u \otimes w,\, u' \otimes w' \rangle = \langle u, u' \rangle \langle w, w' \rangle,$$

the rule for the inner product of two product states of a pair of qubits. For instance, $E_{-1} \circ E_{-1}$ has diagonal entries $4/9$ and off-diagonal entries $1/9$, so it equals $\tfrac13 I + \tfrac19 J$, with eigenvalues $\tfrac13 + \tfrac39 = \tfrac23$ once and $\tfrac13$ twice: positive, as promised.

One more identity is needed only for the Krein conditions in [distance-regular graphs](#distance-regular-graphs): for symmetric $B$ and $C$, the sum of all the entries of $B \circ C$ is $\operatorname{tr}(BC)$. For $E_{-1} \circ E_{-1}$ both sides equal $2$.

**Where it is used.** The rank argument is Fisher's inequality<!-- relink once Fisher's inequality is in these notes -->. Gram matrices give the absolute bound for [strongly regular graphs](#the-adjacency-matrix-of-a-strongly-regular-graph), and the Schur product theorem gives the Krein conditions for [distance-regular graphs](#distance-regular-graphs).

### Linear algebra over finite fields

This section is used only from the chapter on hyperplanes and projective embeddings<!-- relink to the ch4 section once it is merged --> onwards and can be skipped until then. It sharpens two tools from the earlier notes' construction of $PG(n, q)$ from $\mathbb{F}_q^{n+1}$, hyperplanes as kernels and quotient spaces, after a convention.

**Right vector spaces.** In these notes, scalars multiply vectors on the right, $v\lambda$, and coordinates are column vectors, so a matrix acts by $v \mapsto Mv$. The earlier projective geometry notes used left vector spaces and row vectors. Over a field the two conventions describe the same objects, and every finite skew field is a field (Wedderburn's theorem). The choice matters only over a genuine skew field such as the quaternions, in [polar spaces from sesquilinear forms](maths_3_projective_geometry.md#polar-spaces-polarity).

**Linear functionals and hyperplanes.** A linear functional is a linear map $\varphi: V \to \mathbb{F}_q$. In coordinates, $\varphi(x) = a^Tx = a_0x_0 + \dots + a_nx_n$ for a coefficient vector $a$: the earlier notes wrote $a$ as the column of hyperplane coordinates $[a_0, \dots, a_n]$, and as a functional it acts as the row $a^T$. A nonzero $\varphi$ has a hyperplane as its kernel, every hyperplane arises this way, and two nonzero functionals have the same kernel exactly when one is a scalar multiple of the other. So the hyperplanes of $PG(n, q)$ correspond to the nonzero functionals up to scalars, and there are as many hyperplanes as points, $(q^{n+1} - 1)/(q - 1)$. Over $\mathbb{F}_2$ the only nonzero scalar is $1$, so hyperplanes and nonzero functionals match one to one: $PG(3, 2)$ has $2^4 - 1 = 15$ planes, and $PG(4, 2)$ has $2^5 - 1 = 31$ hyperplanes.

**Quotient spaces.** For a subspace $U$ of $V$, the quotient $V/U$ has the cosets $v + U$ as its elements, and $\dim(V/U) = \dim V - \dim U$. Its subspaces correspond to the subspaces of $V$ that contain $U$, the bijection the earlier notes used to count subspaces through a fixed one. In particular, a projective point of $V/U$ is a subspace of $V$ one dimension larger than $U$ and containing it.

For example, take $V = \mathbb{F}_2^4$ and $U = \langle c \rangle$ with $c = (1,0,0,1)^T$; any nonzero $c$ would do, and this one returns in what projection loses<!-- relink to the ch4 section once it is merged -->. Then $V/U \cong \mathbb{F}_2^3$. A point of the quotient is a line of $PG(3, 2)$ through the point $\langle c \rangle$. Each such line holds two points $p$ and $p + c$ besides $c$, so the $14$ other points fall into $7$ pairs, the $7$ points of a Fano plane. This is projection from $c$: each pair looks like one point when seen from $c$.

**Where it is used.** A hyperplane of $PG(n, q)$, the kernel of a single functional, cuts out a hyperplane of any geometry sitting inside $PG(n, q)$, and projection from a point is a quotient (giving a geometry coordinates<!-- relink to the ch4 section once it is merged --> and what projection loses<!-- relink to the ch4 section once it is merged -->). Quotients also build quotient polar spaces<!-- relink to the ch7 section once it is merged -->.

### Bilinear and sesquilinear forms in coordinates

This section is used only from the chapter on [polar spaces](#polar-spaces) onwards, apart from one example in what projection loses<!-- relink to the ch4 section once it is merged -->, and can be skipped until then. It handles the forms behind the earlier notes' polar spaces through their matrices.

Fix a basis $e_0, \dots, e_n$ of $V$. A bilinear form $f$ is determined by its Gram matrix $G$, with $G_{il} = f(e_i, e_l)$: the same idea as before, all pairings of the basis vectors. For coordinate vectors $x$ and $y$,

$$f(x, y) = x^T G y.$$

The form is symmetric when $G^T = G$, and alternating when $G^T = -G$ with zero diagonal.

Changing the basis changes $G$ by congruence. If the new basis vectors are the columns of an invertible $P$, so that $x = Px'$, the new Gram matrix is $G' = P^TGP$. This is not similarity: the eigenvalues of $G$ mean nothing for a form, but its rank does not change.

The radical of $f$, met in the earlier notes, is the set of vectors orthogonal to everything:

$$\operatorname{rad} f = \{ v : f(v, w) = 0 \text{ for all } w \}.$$

For a symmetric or alternating form it is the null space of $G$, and $f$ is nondegenerate (radical $0$) exactly when $\det G \neq 0$.

Two examples over $\mathbb{F}_2$:

- The form $f(x, y) = x_0y_1 + x_1y_0 + x_2y_3 + x_3y_2$ on $\mathbb{F}_2^4$ has the Gram matrix with $G_{01} = G_{10} = G_{23} = G_{32} = 1$ and all other entries $0$. Its determinant is $1$, so $f$ is nondegenerate. It is alternating, since $f(x, x) = 2x_0x_1 + 2x_2x_3 = 0$ over $\mathbb{F}_2$. Its totally isotropic lines give the $15$-point geometry of [generalized quadrangles](#generalized-quadrangles).
- The quadratic form $\Phi(x) = x_0^2 + x_1x_2 + x_3x_4$ on $\mathbb{F}_2^5$ has the polar form $f(x, y) = \Phi(x + y) - \Phi(x) - \Phi(y) = 2x_0y_0 + x_1y_2 + x_2y_1 + x_3y_4 + x_4y_3$. Over $\mathbb{F}_2$ the term $2x_0y_0$ vanishes, so the first row and column of $G$ are zero and $\operatorname{rad} f = \langle e_0 \rangle$. The quadric $\Phi = 0$ itself, with its $15$ points, is still the nondegenerate parabolic quadric $Q(4, 2)$ of the earlier notes, and $\langle e_0 \rangle$ is its nucleus.

**Sesquilinear forms.** A sesquilinear form twists one slot by a field automorphism $\sigma$, such as complex conjugation, or $a \mapsto a^q$ on $\mathbb{F}_{q^2}$. In these notes $\sigma$ acts on the first slot,

$$f(v\lambda, w\mu) = \lambda^\sigma f(v, w)\, \mu,$$

just as Dirac's $\langle v | w \rangle$ is antilinear in the bra. The earlier projective geometry notes put $\sigma$ on the second slot. The two conventions are mirror images: $f(v, w)$ in one is $f(w, v)$ in the other.

In coordinates, $f(x, y) = (x^\sigma)^T G y$, where $x^\sigma$ applies $\sigma$ to each entry, and a change of basis gives $G' = (P^\sigma)^T G P$. The form is Hermitian when $f(w, v) = f(v, w)^\sigma$ for all $v, w$. For example, let $\mathbb{F}_4 = \{0, 1, \omega, \omega^2\}$ with $\omega^2 = \omega + 1$, and let $\sigma(a) = a^2$, which swaps $\omega$ and $\omega^2$ and fixes $0$ and $1$. The form $f(x, y) = x_0^2 y_0 + x_1^2 y_1$ on $\mathbb{F}_4^2$ has $G = I$ and is Hermitian. A vector is isotropic when $f(x, x) = x_0^3 + x_1^3 = 0$. Every nonzero element of $\mathbb{F}_4$ has cube $1$ (the multiplicative group has order $3$), so $x_0^3 + x_1^3$ is $1 + 1 = 0$ when both coordinates are nonzero and $1$ otherwise. Of the $5$ points of $PG(1, 4)$, the $3$ points $\langle (1, a)^T \rangle$ with $a \neq 0$ are isotropic.

**Where it is used.** Forms in coordinates are the language of [polar spaces from sesquilinear forms](maths_3_projective_geometry.md#polar-spaces-polarity) and [the classical polar spaces](maths_3_projective_geometry.md#polar-spaces-polarity), and the radical of a polar form is the nucleus used in what projection loses<!-- relink to the ch4 section once it is merged -->.

<!-- terms checked: positive semidefinite; minimal polynomial; entrywise product -->

## Graphs and Point-Line Geometries

<!-- terms checked: degree; automorphism; geometry; points; subspace; hyperplane -->

How can linear algebra prove that a finite geometry does not exist? The bridge goes through graphs. Every [point-line geometry](#point-line-geometries) gives rise to two natural graphs (one recording which points share a line, the other recording which points lie on which lines). Once we encode a graph in a real symmetric $0/1$ matrix, those local counts turn into polynomial equations for its [eigenvalues](#eigenvalues-and-eigenspaces), whose multiplicities are the dimensions of the corresponding eigenspaces and whose non-vanishing counts give the matrix rank. Because a vector space cannot have a fractional dimension, any hypothetical geometry whose counts force a non-integer eigenspace dimension cannot exist: that single integrality test will rule out impossible quadrangles in [Strongly Regular and Distance-Regular Graphs](#strongly-regular-and-distance-regular-graphs) and restrict finite [generalized polygons](#generalized-polygons) (with at least three points per line and three lines per point) to $3$-, $4$-, $6$- and $8$-gons in [The Feit–Higman theorem](#the-feithigman-theorem-and-order-bounds), while a two-line rank check on [the incidence matrix](#collinearity-graphs-incidence-graphs) will bound block counts in [Designs](#combinatorial-designs). First we build the graph language, then the geometry language that feeds into it.

### Graphs

#### Neighbours, valency and why local counts miss global shape

Let's begin by defining a simple undirected graph $\Gamma = (V, E)$, where $V$ is a set of vertices and $E$ is a set of 2-element subsets of $V$ called edges. Because edges are 2-element subsets rather than ordered pairs or multisets, loops (edges from a vertex to itself) and multiple edges between the same two vertices are automatically excluded.

* Empty and Complete graphs: An empty graph has no edges ($E = \emptyset$), whereas a complete graph $K_n$ has every possible edge between its $n$ vertices.

* Isomorphism and Automorphism: Two graphs are isomorphic if we can relabel the vertices of one to get the exact edge structure of the other. An automorphism is a symmetry of a single graph: a permutation of its vertices that preserves adjacency and non-adjacency.

* Complement: The complement of $\Gamma$ keeps the same vertices $V$ but flips all connections: edges become non-edges ($x \not\sim y$) and non-edges become edges ($x \sim y$).

* Valency (or degree) and Regularity: The valency of a vertex is the number of neighbors it has. If every vertex has the same number of neighbors $k$, the graph is regular of valency $k$.

![Three regular graphs of valency 2: a triangle, a hexagon, and two disjoint triangles](figures/maths4_graphs_regular2.png)

*Figure 1. Three graphs that are all regular of valency $2$: (a) the triangle $C_3 = K_3$, (b) the hexagon $C_6$ with alternating blue and orange vertices and top and bottom corners $x, y$, and (c) two disjoint triangles $2 K_3$. Looking one step out from any vertex, all three look identical.*

Every vertex in Figure 1 has valency $2$. Even total counts fail to separate $C_6$ from $2 K_3$: both have $6$ vertices and $6$ edges, yet one is a single ring and the other falls into two pieces. Valency is purely local; to tell graphs apart, we have to walk further than one step.

* Cliques: A clique is a subset of vertices where every vertex is connected to every other vertex in the subset. It is therefore a complete graph sitting inside a larger graph. A maximal clique is one that does not lie within a larger clique i.e. adding any other vertex from the graph cannot enlarge it.

#### Paths, geodesics and distance
A path is a walk along edges without repeating vertices. The distance $d(x, y)$ is the length of a shortest path (called a geodesic) between $x$ and $y$. The distance between a set of points or lines and a point or set of points or lines is the shortest distance between two points, one take from each of the two sets.

The diameter $\operatorname{diam}(\Gamma)$ is the largest distance between any pair of vertices in the graph (or $\infty$ if $\Gamma$ is disconnected), while the girth $g = \operatorname{girth}(\Gamma)$ is the length of a shortest closed cycle (or $\infty$ if $\Gamma$ has no cycles). In any graph with a cycle, two opposite vertices $x, y$ on a shortest cycle $C$ of length $g$ lie at distance $d(x, y) = \lfloor g / 2 \rfloor$ in $\Gamma$ (any shorter path between them would combine with half of $C$ to create a cycle shorter than $g$). Because $d(x, y) \le \operatorname{diam}(\Gamma)$, girth and diameter always satisfy

$$\operatorname{girth}(\Gamma) \le 2 \operatorname{diam}(\Gamma) + 1$$

(sharpening to $\operatorname{girth}(\Gamma) \le 2 \operatorname{diam}(\Gamma)$ when $g$ is even), and any two vertices at distance $d(u, v) < g / 2$ have a *unique* geodesic between them (two distinct paths of length $i$ would close a cycle of length $\le 2i < g$).

Two points at the maximum possible distance (the diameter $d$) are called **opposite**.

Check Figure 1:

- $C_3$ has diameter $1$ and girth $3 = 2(1) + 1$.
- In $C_6$, the girth is $6 = 2(3)$ and the top and bottom corners $x$ and $y$ in Figure 1(b) satisfy $d(x, y) = 3$ (the diameter), joined by *two* distinct geodesics of length $3$ (left or right around the ring), whereas closer pairs ($d < 6 / 2 = 3$) have a unique geodesic.
- $2 K_3$ is disconnected, with $2$ components, girth $3$, and diameter $\infty$.

Valency only tells you what happens in the locality of a vertex. Distance captures global information. Keep that uniqueness switch in $C_6$ in mind: in [Basic properties of generalized polygons](#generalized-polygons), geodesics will stay *unique* at every distance below the maximum distance, then close from several directions at once.

* Subgraph vs. Induced Subgraph: A general subgraph takes a subset of vertices $V'$ and some chosen subset of edges between them. An induced subgraph on $V'$ takes the subset of vertices $V'$ and is forced to keep every edge from the original graph whose endpoints both lie in $V'$.

Induced subgraphs vs. cliques in collinearity graphs: Later, when we pass from a graph to a point-line geometry, a line is always a clique in the collinearity graph, but not every maximal clique is a line. Also, the distinction between a general subgraph and an induced subgraph mirrors the later distinction between a general subgeometry and a subspace.

#### Bipartite graphs

A graph $\Gamma = (V, E)$ is **bipartite** if $V$ splits into two disjoint subsets $X_1, X_2$ (possibly empty) so every edge has one endpoint in $X_1$ and one in $X_2$. A graph is bipartite if and only if every cycle has even length. To see this, consider the hexagon in Figure 1(b). Colour each vertex alternately with two colours, blue and orange. Each edge then passes between the two disjoint sets (one blue and the other orange) of coloured vertices. Check how alternating blue and orange around $C_6$ in Figure 1(b) works cleanly, whereas two-colouring $C_3$ fails on the third corner. This is because in odd cycles, we will invariably end up with two vertices of the same colour adjacent to each other.

[Every geometry's incidence graph](#point-line-geometries) is bipartite by construction, and distance-parity will [recover a polygon from its double](#generalized-polygons).

A **multipartite** (or **$k$-partite**) graph partitions the vertex set $V$ into $k$ disjoint sets $X_1, \dots, X_k$ so that every edge crosses between two different sets. It is a **complete $k$-partite graph**, written $K_{n_1, n_2, \dots, n_k}$ when the parts have sizes $|X_i| = n_i$ (and $K_{n_1, n_2}$ for a **complete bipartite graph** when $k = 2$), if every vertex in each $X_i$ is joined by an edge to every vertex in every other $X_j$ ($i \neq j$).

#### The Petersen graph as a packing puzzle

Before bringing in matrices, watch how small diameter plus large girth locks a graph's size and local structure completely.

**Puzzle:** If every vertex of $\Gamma$ has valency $3$ and any two vertices lie at distance at most $2$, how many vertices can $\Gamma$ have?

Count outwards from any base vertex $x$: there is $1$ vertex at distance $0$ ($x$), $3$ neighbours at distance $1$, and at most $2$ further edges leaving each neighbour, giving at most $3 \times 2 = 6$ vertices at distance $2$. Since diameter $\le 2$, there is nothing further out:

$$|V| \le 1 + 3 + 6 = 10.$$

What if $\Gamma$ actually hits $10$ vertices? Then none of the $6$ outgoing edges from distance $1$ can be wasted:

1. No edge can join two neighbours of $x$ (that would stay inside layer $1$ and form a triangle). Since $x$ was arbitrary, $\Gamma$ has no $3$-cycles, and *adjacent vertices share $0$ common neighbours*.
2. No two outgoing edges can meet at the same distance-$2$ vertex (that would merge two of the $6$ slots and form a $4$-cycle). Since $x$ was arbitrary, $\Gamma$ has no $4$-cycles, and *non-adjacent vertices share a unique common neighbour*.

Reaching $10$ vertices forces girth $\ge 5$! We can build this graph in one stroke: take the $\binom{5}{2} = 10$ two-element subsets of $\{1, 2, 3, 4, 5\}$ as vertices, and join two $2$-subsets whenever they are disjoint. This is the **Petersen graph** (Figure 2).

![The Petersen graph with vertices labelled as 2-subsets of {1,2,3,4,5}, joined when disjoint](figures/maths4_graphs_petersen.png)

*Figure 2. The Petersen graph: vertices are the $10$ two-element subsets of $\{1, 2, 3, 4, 5\}$, joined when disjoint. From $\{1, 2\}$ (orange), the $3$ blue neighbours are pairs from $\{3, 4, 5\}$, and the $6$ green vertices at distance $2$ overlap $\{1, 2\}$ in one symbol. Unmarked crossings of inner star edges are not vertices.*

Check all four properties directly from $\{1, 2, 3, 4, 5\}$:

- **Valency $3$:** $\{1, 2\}$ leaves $\{3, 4, 5\}$, forming $\binom{3}{2} = 3$ disjoint pairs $\{3, 4\}, \{3, 5\}, \{4, 5\}$.
- **Adjacent pairs share $0$ neighbours:** $\{1, 2\}$ and $\{3, 4\}$ use four symbols, leaving only $\{5\}$, too small to form a pair.
- **Non-adjacent pairs share $1$ neighbour:** $\{1, 2\}$ and $\{1, 3\}$ use $\{1, 2, 3\}$, leaving uniquely $\{4, 5\}$ disjoint from both (diameter $2$, no $4$-cycles).
- **Girth $5$:** the outer pentagon $\{1, 2\} \sim \{3, 4\} \sim \{5, 1\} \sim \{2, 3\} \sim \{4, 5\} \sim \{1, 2\}$ closes a $5$-cycle.

This is the fundamental of what we will call [Generalized Polygons](#generalized-polygons) later: forbidding short cycles while keeping everything close forces an exact vertex count and uniform neighbour counts. Graphs on $v$ vertices of valency $k$ whose adjacent and non-adjacent pairs have constant common-neighbour counts $\lambda$ and $\mu$ are called [strongly regular](#the-adjacency-matrix-and-its-eigenvalues) (here $(v, k, \lambda, \mu) = (10, 3, 0, 1)$), studied in [Strongly Regular and Distance-Regular Graphs](#strongly-regular-and-distance-regular-graphs).

#### The adjacency matrix and its eigenvalues

Order the $v$ vertices of a finite graph $\Gamma$ as $(p_1, \dots, p_v)$ and form its $v \times v$ **adjacency matrix** $A$ over $\mathbb{R}$ (never over $\mathbb{F}_2$, since we want real path counts without mod-$2$ cancellation), setting $A_{ij} = 1$ if $p_i \sim p_j$ and $0$ otherwise. Because $A$ is real symmetric with zero diagonal, [the spectral theorem](#real-symmetric-matrices-and-the-spectral-theorem) guarantees real eigenvalues and diagonalizability.

Writing $A$ down needs an order for the vertices. But let's say you changed the order. You can do this by using $P^TAP$ as the adjacency matrix, where $P$ is a permutation matrix on the vertices. The new madjacency matrix will still have the same eigenvalues and multiplicities ([permutation matrices](#the-all-ones-matrix-and-commuting-matrices)). These eigenvalues are therefore the eigenvalues of $\Gamma$ itself. The list of eigenvalues is sometimes called the spectrum of $\Gamma$. In eigenvalue lists, exponents mark multiplicity: $1^2$ means eigenvalue $1$ twice.

Compare our two $6$-vertex valency-$2$ graphs from Figure 1:

- **Two triangles $2 K_3$:** The $2K_3$ adjacency matrix contains two triangle matrices arranged along the diagonal with zeroes everywhere else. Since $A_{K_3} = J_3 - I_3$ had eigenvalues $2, (-1)^2$ in [the prologue](#real-symmetric-matrices-and-the-spectral-theorem). Doubling the block gives $2^2, (-1)^4$.
- **Hexagon $C_6$:** Around the $6$-cycle, $(A w)_i = w_{i-1} + w_{i+1}$. Constant $(1, 1, 1, 1, 1, 1)^T$ gives $\theta = 2$; alternating $(1, -1, 1, -1, 1, -1)^T$ gives $\theta = -2$; $(1, 1, 0, -1, -1, 0)^T$ and its shift $(0, 1, 1, 0, -1, -1)^T$ give $\theta = 1$ twice; and $(1, -1, 0, 1, -1, 0)^T$ and $(0, 1, -1, 0, 1, -1)^T$ give $\theta = -1$ twice. Thus $C_6$ has eigenvalues $2, 1^2, (-1)^2, -2$.

Where do these eigenvalues come from without guessing the vectors?

1. **Standing waves around the cycle (roots of unity):** Because shifting one step around the $6$-cycle is rotation by $\alpha = \frac{2\pi r}{6}$ ($r = 0, 1, 2, 3, 4, 5$), testing $w_m = e^{i m \alpha}$ gives $(Aw)_m = e^{i(m-1)\alpha} + e^{i(m+1)\alpha} = (e^{-i\alpha} + e^{i\alpha})e^{im\alpha} = 2\cos(\alpha)\, w_m$. Plugging in $\alpha = r \cdot 60^\circ$ immediately yields $\theta_r = 2\cos(r \cdot 60^\circ) = 2,\, 1,\, -1,\, -2,\, -1,\, 1$ (and the real eigenvectors above are integer-scaled combinations of $\cos(m \cdot 60^\circ)$ and $\sin(m \cdot 60^\circ)$).

2. **Polynomial shortcut ($A^3 - 3A = 2P$):** Taking $3$ steps on $C_6$ from vertex $i$ either reaches the opposite corner ($2$ ways: clockwise or counterclockwise) or steps back and forth to an immediate neighbour ($3$ ways each). Thus $A^3 = 3A + 2P$, where $P$ swaps opposite corners of the hexagon. Since $P^2 = I$ has eigenvalues $\pm 1$, every eigenvalue $\theta$ of $A$ satisfies $\theta^3 - 3\theta = \pm 2$, which factors into $(\theta - 2)(\theta + 1)^2 = 0$ and $(\theta + 2)(\theta - 1)^2 = 0$, giving $\theta = 2, (-1)^2$ and $\theta = -2, 1^2$.

Two differences jump out between $2^2, (-1)^4$ and $2, 1^2, (-1)^2, -2$: the multiplicity of $2$, and the appearance of $-2$ because the hexagon is bipartite.

We can put a few conditions on the eiegenvalues. The valency $k$ is always an eigenvalue of the graph because every row has $k$ ones, so the all-ones vector $j$ satisfies $Aj = kj$.

No eigenvalue $\theta$ can ever exceed $k$ in absolute value ($\vert{}\theta\vert{} \le k$). To see why, assume that the eigenvector $w$ has a maximum component $w_i$. The $i^{th}$ component of $Aw = \theta w$ will be a maximum of $kw_i$. But this should equal $\theta w_i$, which means $\theta w_i \le kw_i$ which gives us the limit.

The multiplicity of the eigenvalue $k$ counts the exact number of connected components of the graph. In particular, a $k$-regular graph is connected if and only if the eigenvalue $k$ has multiplicity 1.

A connected finite $k$-regular graph ($k \ge 1$) has $-k$ as an eigenvalue if and only if it is bipartite. 

A few more definitions of types of graphs. 

Strongly Regular Graphs (SRGs): A graph with $v$ vertices (neither empty nor complete) is strongly regular with parameters $(v, k, \lambda, \mu)$ if it is $k$-regular i.e. every vertex has a valency of $k$, every pair of adjacent vertices shares $\lambda$ common neighbors, and every pair of distinct non-adjacent vertices shares $\mu$ common neighbors. Note that when we say non-adjacent, we mean any distance larger than 1, but when $\mu > 0$ the fact that they share common neighbours means that the distance is always 2 (this holds for every primitive, that is nondegenerate, strongly regular graph; when $\mu = 0$ the graph is a disjoint union of complete graphs).

Distance-Regular Graphs (DRGs): This generalizes strong regularity to arbitrary diameter $d$, with parameters $(a_i, b_i, c_i)$ for each distance $i \in \{0, \dots, d\}$. Instead of only looking at distance 1 (adjacent) and distance 2 (non-adjacent), we require that for any two vertices $x$ and $y$ at distance $i$ from each other, the number of neighbors of $y$ that are one step closer to $x$ (at distance $i-1$) is a constant $c_i$, the number of neighbors of $y$ at the same distance $i$ from $x$ is a constant $a_i$, and the number of neighbors of $y$ one step further away from $x$ (at distance $i+1$) is a constant $b_i$.

We have the property $a_i + b_i + c_i = k$ for every $i$ because any neighbor of $y$ can only be at distance $i-1$, $i$, or $i+1$ from $x$. Since $y$ has $k$ neighbors in total, those three counts must add up to $k$. At the boundaries, several values are fixed automatically: $c_0 = 0$ and $a_0 = 0$ (no vertices at distance $-1$ and no self-loops), $b_0 = k$ (all $k$ neighbors of $x$ are at distance $1$), $c_1 = 1$ (for $y \sim x$, $x$ itself is the only neighbor of $y$ at distance $0$), and $b_d = 0$ (no vertices exist beyond the diameter $d$).

SRGs are DRGs of diameter 2. In a connected graph of diameter 2, the only possible distances between distinct vertices are $i = 1$ (adjacent) and $i = 2$ (non-adjacent). For $i = 1$, $a_1$ is the number of common neighbors of two adjacent vertices ($\lambda$). For $i = 2$, $c_2$ is the number of common neighbors of two non-adjacent vertices ($\mu$).

### Point-line geometries

#### Points, lines, duals and doubles

A point-line geometry is a triple $S = (\mathcal{P}, \mathcal{L}, I)$ of points $\mathcal{P}$, lines $\mathcal{L}$ (kept formally disjoint from $\mathcal{P}$), and an incidence relation $I \subseteq \mathcal{P} \times \mathcal{L}$ telling us which points lie on which lines, with the single basic requirement that every line contains at least two points.

From any geometry $S$, we have three derived geometries:

**The Point-Line Dual $S^D$**: Swap the roles of points and lines ($\mathcal{P}^D = \mathcal{L}$ and $\mathcal{L}^D = \mathcal{P}$) and keep incidence the same. Notice the condition: every point of $S$ must lie on at least two lines. Why? Because our definition of a geometry requires every line to have at least two points; when points of $S$ become lines of $S^D$, each old point needs at least two old lines on it so that the new lines in $S^D$ have at least two new points.

**The Double $S'$**: Put points and lines of $S$ together as the points of $S'$, and use the flags $\{x, L\}$ ($x$ is a point) of $S$ as the lines of $S'$ (so every line in $S'$ is thin, having size 2).

**The Internal Structure $S_x$ at a point $x$**: Assuming every line through $x$ has at least 3 points, take all neighbors of $x$ ($x^\perp \setminus \{x\}$, where $x^\perp$ is the set of points collinear with $x$ as well as $x$ itself) as the points, and the lines of $S$ passing through $x$ as the lines.

Notice carefully that in $S_x = (x^\perp \setminus \{x\}, \mathcal{L}_x, I_x)$, the lines are only the lines through $x$. If $S$ is a partial linear space, two lines through $x$ cannot meet anywhere else, so in $S_x$ the lines $\mathcal{L}_x$ simply partition $x^\perp \setminus \{x\}$ into disjoint sets of points. Later, when studying polar spaces or near polygons, we enrich this local view by either looking at how lines not through $x$ cut across $\mathcal{L}_x$ (turning the lines through $x$ into points and planes through $x$ into lines, which gives the residue at $x$), or looking at the induced subgeometry on $x^\perp \setminus \{x\}$.

On the $3 \times 3$ grid in figure 5, $\mathcal{S}_x$ is $4$ points on two disjoint $2$-point lines. **Do not confuse $\mathcal{S}_x$ with the residue at $x$** from the earlier projective geometry notes (and Quotient polar spaces<!-- relink to the ch7 section once it is merged -->), where lines through $x$ become *points* and planes through $x$ become *lines*; $\mathcal{S}_x$ keeps neighbouring points as points, which is how we will build [derived designs](#unitals-inversive-planes-and-witt-mathieu-designs) in [Designs: a first look](#combinatorial-designs) and [New designs from old](#unitals-inversive-planes-and-witt-mathieu-designs).

Here are a few examples:

**The Fano plane $\mathrm{PG}(2, 2)$** (Figure 4(a)): $7$ points and $7$ lines of $3$ points each, $3$ lines per point. Swapping vectors and functionals on $\mathbb{F}_2^3$ shows $\mathrm{PG}(2, 2)$ is self-dual; its double has $14$ points and $21$ two-point lines.

**The $3 \times 3$ grid $Q^+(3, 2)$** ($x_0 x_3 + x_1 x_2 = 0$ in $\mathrm{PG}(3, 2)$, where $+$ and $-$ agree over $\mathbb{F}_2$): $9$ points on $3$ rows $R_1, R_2, R_3$ and $3$ columns $C_1, C_2, C_3$ ($2$ lines per point). Its dual $\mathcal{S}^D$ has $6$ points $\{R_1, R_2, R_3, C_1, C_2, C_3\}$ and $9$ two-point lines $\{R_i, C_j\}$ joining every row-point to every column-point (a **dual grid**), visibly non-isomorphic to the $9$-point grid yet sharing the same $15$-point, $18$-line double. Both return in [Basic properties of generalized polygons](#generalized-polygons) and [Which polygons exist](#the-feithigman-theorem-and-order-bounds).

#### Partial Linear Spaces

In a projective plane, we say any two lines are incident at exactly one point and any two points are connected by exactly one line. This is a linear space. But recall that our hyperbolic quadric in 3D did not satisfy this rule. Any two points had either 0 or 1 line connecting them.

So a more general rule is a geometry where any two distinct points lie on at most one common line (equivalently, any two distinct lines intersect in at most one point). This is a partial linear space. Here, no two distinct lines have the exact same set of incident points.

The partial linear space has order $(s, t)$ if every line has $s + 1$ points, and every point lies on $t + 1$ lines. Why $s + 1$ and $t + 1$ instead of $s$ and $t$? This comes from projective geometry over a finite field $\mathbb{F}_q$, where a projective line $PG(1, q)$ has $q + 1$ points (one point at infinity plus $q$ affine points). So for classical geometries over $\mathbb{F}_q$, $s = q$. Also, when you fix a point $x$ on a line, there are exactly $s$ other points on that line, so in a partial linear space of order $(s, t)$, the collinearity graph is regular with valency $k = s(t + 1)$.

A subgeometry picks a subset of points $\mathcal{P}'$ and a subset of lines $\mathcal{L}'$. In a general subgeometry, a line $L \in \mathcal{L}'$ might lose some of its original points if those points were not included in $\mathcal{P}'$ (so the line gets "chopped" or shortened). A subgeometry is called full if every line $L \in \mathcal{L}'$ keeps 100% of the points it had in the ambient geometry $S$. For example, in $PG(2, q) \subset PG(3, q)$, every line in the plane retains all $q + 1$ of its points from the ambient 3-space, making it a full subgeometry.

In a partial linear space $S = (\mathcal{P}, \mathcal{L}, I)$:

* Subspace: A subset of points $X \subseteq \mathcal{P}$ with the "two-point closure rule": whenever a line of $S$ has at least two of its points inside $X$, the entire line (all of its points) must lie inside $X$. Every nonempty subspace $X$ naturally forms a full subgeometry $\tilde{X}$ using the lines contained in $X$.

* Singular Subspace: A subspace where every pair of points is collinear. (Because $X$ is also a subspace, for any two points in a singular subspace, the unique line joining them exists in $S$ and lies completely inside $X$. Thus, singular subspaces look like projective spaces: points, lines, planes, etc., where all points are mutually collinear.)

  In $\mathrm{PG}(n, q)$, if a subset $X$ obeys the two-point line rule ("whenever $x, y \in X$, the line $xy$ is in $X$"), then every pair $x, y \in X$ has a line in $X$, because every pair had a line in $\mathrm{PG}(n, q)$ to begin with.

* Generated Subspace $\langle X \rangle$: Given any starting set of points $X$, there is a unique smallest subspace containing $X$, equal to the intersection of all subspaces containing $X$. How to build this subspace step by step from the bottom up:

Start with $X_0 = X$. To get $X_1$, draw every line that passes through at least two points of $X_0$, and throw all the points on those lines into $X_1$. Repeat: to get $X_i$, take every line passing through at least two points of $X_{i-1}$ together and add all points on those lines. The union $\bigcup_{i \in \mathbb{N}} X_i$ of all these steps is the exact subspace generated by $X$.

Adding all lines through pairs of points in $X_0$ creates new points in $X_1$. A line passing through two of those newly added points in $X_1$ might not have contained two points of $X_0$, so you have to run the line-completion step again for $X_2$, $X_3$, and so on. 

The generating index is the minimum number of points needed to generate the whole geometry $\mathcal{P}$. For an $n$-dimensional projective space $PG(n, q)$, the generating index is $n + 1$ (a basis of $n + 1$ points in general position generates the entire space in $n$ steps), whereas for polar spaces and generalized quadrangles, computing the generating index tells us the minimum dimension of the ambient vector space into which the geometry can be projectively embedded.

* Hyperplane: A proper subspace ($X \neq \mathcal{P}$) that intersects every single line of the geometry in at least one point. (Because $X$ is a subspace, any line of $S$ either meets the hyperplane $X$ in a single point, or is completely contained inside $X$.)

Unlike projective hyperplanes, a hyperplane of $\mathcal{S}$ need not look flat and may contain *no lines at all*! Let us find every hyperplane $H$ of the $3 \times 3$ grid (Figure 5):

- **If $H$ contains a line**, say row $R_i$, then $R_i$ alone misses the other two rows, so $H$ needs points in both. Picking points in two different columns would give two columns $2$ points each in $H$, swallowing both columns and then all $9$ points ($H = \mathcal{P}$, not proper). So the extra points must lie in one column $C_k$, giving **$9$ hyperplanes** $x^\perp = R_i \cup C_k$ of $5$ points each (Figure 5(a)).
- **If $H$ contains no line**, it meets every row and every column in *precisely $1$ point*: a permutation pattern! There are $3! = 6$ such $3$-point **transversals** (Figure 5(b)), which are subspaces vacuously because no line hits them twice.

There are thus 15 hyperplanes in total.

![Two hyperplanes of the 3x3 grid: a 5-point cross containing two lines, and a 3-point transversal (ovoid) containing no lines](figures/maths4_graphs_grid_hyperplanes.png)

*Figure 5. The $15$ hyperplanes of the $3 \times 3$ grid fall into two shapes: (a) $9$ crosses $x^\perp$ ($5$ orange points, two full lines), and (b) $6$ transversals ($3$ blue points, no lines at all, meeting all six lines once).*

A set of points meeting *every line of $\mathcal{S}$ in precisely one point* is an **ovoid** of $\mathcal{S}$ (so every ovoid of a thick-lined partial linear space is a line-free hyperplane, like the $6$ transversals). **Watch the context shift:** in the earlier projective geometry notes, an ovoid of $\mathrm{PG}(3, q)$ was a $(q^2 + 1)$-point cap like $Q^-(3, q)$ missing many ambient lines, whereas an ovoid *of $\mathcal{S}$* meets every line *of $\mathcal{S}$* once. Notice that the $3 \times 3$ grid $Q^+(3, 2) \subset \mathrm{PG}(3, 2)$ has $9 + 6 = 15$ hyperplanes, matching the $15$ planes of $\mathrm{PG}(3, 2)$ ($9$ tangent planes cutting crosses, $6$ non-tangent planes cutting ovoids), a match explained in What projection loses<!-- relink to the ch4 section once it is merged -->.

#### Collinearity Graphs & Incidence Graphs

Every point-line geometry $S$ has two natural graphs attached to it:

The Collinearity Graph $\Gamma$: Vertices are the points $\mathcal{P}$, and two points are connected by an edge if they share a line.

For straightforward geometries where any line has only two points, this graph is the actual figure of the geometry that we would have learnt in high school. For example, the collinearity graph of a triangle is a triangle.

But notice what this graph cannot distinguish: one $3$-point line also has a collinearity graph that is a triangle $K_3$. This is why we need the Incidence Graph. 

The Incidence Graph: Vertices are both points and lines ($\mathcal{P} \cup \mathcal{L}$), and edges connect a point $p$ to a line $L$ whenever $(p, L)$ is a flag.

If every line of the geometry has only $2$ points (for example, in a thin geometry or when taking the double $\mathcal{S}'$), the incidence graph is literally obtained from the collinearity graph by inserting one line node in the middle of every edge.

When a line has $3$ or more points (say $L = \{p_1, p_2, p_3\}$), instead of putting $3$ separate line nodes on the $3$ edges of that triangle, all $3$ points connect to one single shared line node $L$ (forming a $3$-spoke star with hub $L$):

$$p_1 - L - p_2 \quad\text{and}\quad p_3 - L.$$

(Putting a separate node on each of the $3$ edges would instead describe three separate $2$-point lines $\{p_1, p_2\}, \{p_2, p_3\}, \{p_1, p_3\}$.)

![Comparison of a collinearity path and the corresponding alternating point-line path in the incidence graph](figures/maths4_graphs_alternating.png)

*Figure 3. Collinearity distance $d$ versus incidence distance $\delta$: (a) a two-step collinearity path $x_0 \sim x_1 \sim x_2$ reaching the nearest point $x_2$ of $L$, giving $d(x_0, x_2) = d(x_0, L) = 2$; (b) the matching alternating incidence path $x_0 - L_{01} - x_1 - L_{12} - x_2 - L$, giving $\delta(x_0, x_2) = 4$ and $\delta(x_0, L) = 5$.*

There is a relationship that translates distances $d(\cdot, \cdot)$ measured in the collinearity graph into distances $\delta(\cdot, \cdot)$ measured in the bipartite incidence graph:

- Between two points $x$ and $y$: $\delta(x, y) = 2 \cdot d(x, y)$.
- Between a point $x$ and a line $L$: $\delta(x, L) = 2 \cdot d(x, L) + 1$.
- Between two distinct lines $L_1$ and $L_2$: $\delta(L_1, L_2) = 2 \cdot d(L_1, L_2) + 2$.

Why are there $+0$, $+1$, and $+2$ in the three formulas?

In the incidence graph, every single step alternates between a point and a line: $\text{point} \to \text{line} \to \text{point}$. So one collinearity step between two points always takes 2 steps in the incidence graph, giving $2 \cdot d(x, y)$.

For a point $x$ and a line $L$, $d(x, L)$ measures the collinearity distance from $x$ to the closest point $y$ on $L$. In the incidence graph, getting from $x$ to $y$ takes $2 \cdot d(x, L)$ steps, and then stepping from the point $y$ onto the line vertex $L$ itself takes 1 final step, giving $2 \cdot d(x, L) + 1$. (Notice that if $x$ lies on $L$, $d(x, L) = 0$ and $\delta(x, L) = 1$, which is a single flag edge.)

Similarly, for two distinct lines $L_1$ and $L_2$, we add another $1$ for the second line as well. 

Notice also that parity in the incidence graph is completely locked: point-to-point and line-to-line distances are always even, while point-to-line distances are always odd.

For a finite geometry $\mathcal{S}$, the two graphs give two real matrices: an adjacency matrix $A$ of $\Gamma$ (a **collinearity matrix**, whose eigenvalues are the eigenvalues of $\mathcal{S}$). 

But the full adjacency matrix of the bipartite incidence graph listing all points $\mathcal{P}$ first and all lines $\mathcal{L}$ second, splits into four blocks:

$$\widetilde{A} = \begin{pmatrix} 0 & M \\ M^T & 0 \end{pmatrix} \begin{matrix} \leftarrow \text{points } \mathcal{P} \\ \leftarrow \text{lines } \mathcal{L} \end{matrix}$$

- **Top-left ($0$):** no point-to-point edges in the incidence graph.
- **Bottom-right ($0$):** no line-to-line edges in the incidence graph.
- **Top-right ($M$):** point-to-line edges ($M_{p, L} = 1$ if $p \,\mathrm{I}\, L$).
- **Bottom-left ($M^T$):** line-to-point edges (just the transpose of $M$).

Because the two diagonal blocks are always $0$ and the bottom-left is just $M^T$, all the information in the incidence graph's adjacency matrix lives in that **top-right $|\mathcal{P}| \times |\mathcal{L}|$ block $M$**, which is what we call the **incidence matrix**. 

![The Fano plane PG(2,2) beside its bipartite 14-vertex incidence graph, the Heawood graph](figures/maths4_graphs_fano_heawood.png)

*Figure 4. (a) The Fano plane $\mathrm{PG}(2, 2)$ of order $(2, 2)$ ($7$ points, $7$ lines; $L_1$ and $L_4$ meet at $p_1$). (b) Its bipartite incidence graph, the $14$-vertex Heawood graph, drawn as a $14$-cycle alternating blue points and green lines with step-$5$ chords; orange edges mark the flags $(p_1, L_1)$ and $(p_1, L_4)$.*

Check both on $\mathrm{PG}(2, 2)$ in Figure 4. Its collinearity graph is $K_7$, forgetting which triples are lines; its incidence graph, the **Heawood graph** (also called simply the incidence graph of $\mathrm{PG}(2, 2)$), keeps everything, with $14$ vertices, valency $3$, girth $6$, and diameter $3$ (every two distinct points share a line and every two distinct lines share a point, giving $\delta = 2$, while anti-flags have $d(x, L) = 1$ and $\delta(x, L) = 3$). And multiplying its $7 \times 7$ incidence matrix $M$ by $M^T$ counts lines through both $x$ and $y$ via $(M M^T)_{xy} = \sum_L M_{x, L} M_{y, L}$: $3$ on the diagonal, $1$ off the diagonal (because each point has 3 lines incident on it and any pair of points share one line), giving

$$M M^T = 3 I_7 + (J_7 - I_7) = 2 I_7 + J_7$$

without writing down a single entry of $M$. Products like $M M^T$ and $A^2$ turn incidence counts into eigenvalue equations ([The adjacency matrix of a strongly regular graph](#the-adjacency-matrix-of-a-strongly-regular-graph) and Fisher's inequality<!-- relink once Fisher's inequality is in these notes -->).

This will give us two algebraic weapons that prove theorems and rule out impossible geometries without ever having to draw or search for them. We will look at this in a little while. 

<!-- terms checked: subspace; hyperplane -->

## Classes of Point-Line Geometries

Before investigating individual geometries in depth, it helps to build a working catalogue of the main families of point-line geometries.

Before meeting spaces built from algebra or field theory, it is useful to name eight elementary point-line geometries. They appear constantly as extreme cases, degenerate cases, or building blocks inside larger theorems.

**A point:** A point-line geometry with a single point ($|\mathcal{P}| = 1$), no lines ($\mathcal{L} = \emptyset$), and empty incidence ($\mathrm{I} = \emptyset$).

**A line:** A linear space with exactly one line ($|\mathcal{L}| = 1$) and at least two points, all of which lie on that unique line.

**Graphs and circular spaces:** Any simple graph $\Gamma = (V, E)$ (where $V \neq \emptyset$ is the vertex set and $E$ is a set of $2$-element subsets of $V$) can be viewed directly as a partial linear space whose points are the vertices $V$ and whose lines are the edges $E$, all of which are **thin** ($2$ points per line). When $\Gamma = K_n$ is the complete graph on $n \ge 3$ vertices (every pair of vertices joined by a $2$-point edge), this partial linear space is called a **circular space**. It is called circular because no $3$ points on a circle are collinear, making all lines thin, just like the complete graph. Furthermore, in a complete graph, every line has exactly 2 points, just like the secant of a circle.

**Generalized $2$-gons (generalized digons):** A point-line geometry $(\mathcal{P}, \mathcal{L}, \mathrm{I})$ with $|\mathcal{P}| \ge 2$, $|\mathcal{L}| \ge 2$, and $\mathrm{I} = \mathcal{P} \times \mathcal{L}$, meaning **every point is incident with every line**.

A generalized digon is the classic example of a geometry that is **not** a partial linear space and where lines **cannot** be treated as subsets of points. Every line $L \in \mathcal{L}$ has the exact same set of incident points, namely all of $\mathcal{P}$. Keeping $\mathcal{P}$ and $\mathcal{L}$ as abstract disjoint sets linked by $\mathrm{I}$ in the definition of a point-line geometry is what allows generalized digons to exist cleanly.

**Ordinary $n$-gons ($n \ge 3$):** A partial linear space isomorphic to the $n$ vertices $\mathcal{P} = \{1, 2, \dots, n\}$ and $n$ thin edges $\mathcal{L} = \{\{1, 2\}, \{2, 3\}, \dots, \{n - 1, n\}, \{n, 1\}\}$ of an ordinary polygon, with containment as incidence. When $n = 3$, an ordinary $3$-gon (triangle) is the same thing as a circular space on $3$ vertices. Every ordinary $n$-gon is self-dual: swapping vertices and edges of an $n$-sided polygon yields another $n$-sided polygon.

**Near-pencils:** A **near-pencil** is a linear space in which one line contains *every point except one*.

Suppose a near-pencil has $n$ points in total ($n \ge 3$). Then $n - 1$ of the points, say $x_1, x_2, \dots, x_{n-1}$, all sit on one long line $L_0$, while a single outsider point $p$ sits off $L_0$ (panel (a) of Figure 7 shows $n = 5$). Because a near-pencil is a linear space, $p$ must be joined to each $x_i$ by a unique line, and none of these connecting lines can hit a second point $x_j$ on $L_0$ (otherwise it would share two points with $L_0$). That forces the remaining lines to be the $n - 1$ thin lines $\{p, x_1\}, \{p, x_2\}, \dots, \{p, x_{n-1}\}$.

So a near-pencil on $n$ points always has $n$ lines as well: one line of size $n - 1$ and $n - 1$ lines of size $2$. When $n = 3$, the "long" line also has size $2$, so a near-pencil on $3$ points is an ordinary $3$-gon. Also, the point-line dual of any near-pencil is again a near-pencil: the $n - 1$ thin lines through $p$ become $n - 1$ dual points all sitting on the dual line $p$, while $L_0$ becomes the lone outsider point. Here, we have every line meeting at a point, except for $L_0$.

**$(k_1, k_2, \dots, k_s)$-stars and $(k_1, k_2)$-crosses:** Let $s \ge 2$ and let $k_1, k_2, \dots, k_s \ge 2$ be integers. A **$(k_1, k_2, \dots, k_s)$-star** is a linear space having a distinguished hub point $p$ through which pass $s$ lines $L_1, \dots, L_s$ of respective sizes $|L_i| = k_i$, while **every line not passing through $p$ is thin** (size $2$). Because it is a linear space, every point on $L_i \setminus \{p\}$ is joined to every point on $L_j \setminus \{p\}$ ($i \neq j$) by a thin $2$-point line, and there are no other points in the geometry. When $s = 2$, a $(k_1, k_2)$-star is called a **$(k_1, k_2)$-cross**.

Note that a near-pencil on $n$ points is just the special case of a $(k_1, 2)$-cross where $k_1 = n - 1$, and the crossing point is one of the points on $L_0$, or equivalently a $(2, 2, \dots, 2)$-star with $n - 1$ rays of size $2$ where one of the outer points is viewed as the hub.

For example, consider a $(3, 3, 4)$-star (here $s = 3$). There are 3 lines through the hub $p$, containing 3, 3, and 4 points respectively (so 2, 2, and 3 points outside $p$, giving $1 + 2 + 2 + 3 = 8$ points in total). Every other line connects one point from one ray to one point on another ray, and has size 2. There are $(2 \times 2) + (2 \times 3) + (2 \times 3) = 16$ such thin lines. Total lines in the space: $3 + 16 = 19$ lines (three of sizes 3, 3, 4, and sixteen of size 2). There is no single line uniting the 3 rays outside $p$.

A circular space is also a special case. Remember that a circular space is a linear space on $n \ge 3$ points in which every line is thin (contains exactly 2 points). Because every pair of distinct points must lie on a unique 2-point line, a circular space on $n$ points is simply the complete graph $K_n$.

A $(2, 2, \dots, 2)$-star with $n - 1$ rays of size $2$ connects every pair of outer points by its own separate two-point line rather than putting them on one long line, so a $(2, 2, \dots, 2)$-star is a circular space $K_n$ (matching a near-pencil only when $n = 3$).

**$(n_1 \times n_2)$-grids and dual grids:** Given sets $X_1, X_2$ of sizes $n_1 \ge 2$ and $n_2 \ge 2$, an **$(n_1 \times n_2)$-grid** is a partial linear space isomorphic to the Cartesian product point set $X_1 \times X_2$, whose lines are the $n_1$ "rows" $\{i\} \times X_2$ ($i \in X_1$, each of size $n_2$) and the $n_2$ "columns" $X_1 \times \{j\}$ ($j \in X_2$, each of size $n_1$). Through every point $(i, j)$ pass exactly $2$ lines (its row and its column), so every $(n_1 \times n_2)$-grid has $t = 1$ (where every point is incident with $t+1$ lines). The grid is called **symmetrical** if $n_1 = n_2$ (in which case it has order $(n_1 - 1, 1)$) and **nonsymmetrical** if $n_1 \neq n_2$ (in which case lines have two different sizes, so it has no single parameter $s$ which would say every line has $s+1$ points).

Its point-line dual is called a **(symmetrical or nonsymmetrical) dual grid**. What does a dual grid look like? First, note that two row-lines never intersect, and two column-lines never intersect, while every row-line meets every column-line in a unique grid point $(i, j)$. This unique point becomes a thin $2$-point line in the dual. The $n_1$ row-lines and $n_2$ column-lines become two disjoint sets of points of sizes $n_1$ and $n_2$. Therefore, **dual grids are precisely the complete bipartite graphs $K_{n_1, n_2}$ with $n_1, n_2 \ge 2$**, viewed as partial linear spaces with thin lines.

The hyperbolic quadric $Q^+(3,q)$ in $\text{PG}(3,q)$ is a symmetrical $(q+1) \times (q+1)$ grid of order $(s, t) = (q, 1)$. Its lines split into two families of $q+1$ mutually skew lines (the regulus and the opposite regulus), where every line of the first regulus intersects every line of the second regulus in a unique point.

![Four basic point-line geometries: near-pencil, (3,4)-cross, (2x3)-grid with its dual K_{2,3}, and generalized digon](figures/maths4_classes_basic_geometries.png)

*Figure 7. Four elementary geometries. (a) A near-pencil on $5$ points: one line of size $4$, and four thin lines joining the outside point $p$ to it. (b) A $(3, 4)$-cross: two lines of $3$ and $4$ points through the hub $p$, and the six thin lines joining their other points. (c) A nonsymmetrical $2 \times 3$ grid ($6$ points, $5$ lines) and its dual grid $K_{2,3}$ ($5$ points, $6$ thin lines). (d) A generalized digon with $3$ points and $3$ lines, drawn as its incidence graph: every point lies on every line.*

| Elementary Geometry | Point Count $\lvert\mathcal{P}\rvert$ | Line Count $\lvert\mathcal{L}\rvert$ | Line Sizes | Linear Space? | Self-Dual? |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Point | $1$ | $0$ | none | vacuously yes | dual undefined |
| Line (size $k \ge 2$) | $k$ | $1$ | $k$ | yes | dual undefined |
| Circular space ($K_n, n \ge 3$) | $n$ | $\binom{n}{2}$ | all $2$ (thin) | yes | only for $n = 3$ |
| Generalized digon | $m \ge 2$ | $n \ge 2$ | all $m$ | no (not even partial linear) | iff $m = n$ |
| Ordinary $n$-gon ($n \ge 3$) | $n$ | $n$ | all $2$ (thin) | only for $n = 3$ | yes |
| Near-pencil ($n \ge 3$) | $n$ | $n$ | one of $n-1$, and $n-1$ of $2$ | yes | yes |
| $(k_1, \dots, k_s)$-star | $1 + \sum_{i=1}^s (k_i - 1)$ | $s + \sum_{i < j}(k_i - 1)(k_j - 1)$ | $k_1, \dots, k_s$, rest $2$ | yes | iff near-pencil |
| $(n_1 \times n_2)$-grid ($n_i \ge 2$) | $n_1 n_2$ | $n_1 + n_2$ | $n_1$ of size $n_2$; $n_2$ of size $n_1$ | no | yes if $n_1 = n_2 = 2$; no otherwise (dual is $K_{n_1, n_2}$) |

Why is the star self-dual only when it is a near-pencil? A star is a linear space, meaning if it is self-dual, the dual has to be a linear space too. If a star is not a near-pencil, it always contains two disjoint lines (one of the rays $L_i$ and a thin line connecting two other rays), so its dual has pairs of points with no line between them and fails to be a linear space. Conversely, every near-pencil on $n$ points has $n$ points, $n$ lines, and every pair of lines meets in a unique point, making it self-dual.

### Projective planes: degenerate vs. nondegenerate

A **projective plane** is a linear space $\mathcal{S}$ satisfying two axioms:

1. Any two distinct lines of $\mathcal{S}$ meet in a unique point.
2. There exist three noncollinear points.

Because three noncollinear points $x_1, x_2, x_3$ determine three lines $x_1 x_2, x_2 x_3, x_3 x_1$ that do not all pass through a common point (three nonconcurrent lines), swapping points and lines preserves every axiom: **the point-line dual of any projective plane is again a projective plane**.

Pause and ask: is requiring *three* noncollinear points enough to give a rich plane like the Fano plane? Look back at panel (a) of Figure 7: in a **near-pencil** on $n \ge 3$ points, every two points determine a unique line, *every two lines intersect in a unique point* (two thin lines meet at $p$, and each thin line $\{p, x_i\}$ meets the long line at $x_i$), and $p, x_1, x_2$ are three noncollinear points. So near-pencils satisfy the two axioms above, even though almost all their points are collapsed onto a single line.

To separate genuine planes from near-pencils, we strengthen "three noncollinear points" to four:

- A projective plane is **irreducible** (or **nondegenerate**) if it contains **four points, no three of which are collinear** (a quadrangle).
- Otherwise, it is **reducible** (or **degenerate**). The degenerate projective planes are **precisely the near-pencils**.

We now show why in any nondegenerate projective plane $\mathcal{S}$, every line has the same number of points, which also equals the number of lines in the plane.

Take any two lines $L_1$ and $L_2$. Because the plane is nondegenerate, there is an external point $p$ lying on neither line. Draw the lines through $p$. In a projective plane, every point $x$ on $L_1$ connects to $p$ by a unique line $px$. That line $px$ must intersect $L_2$ in a unique point $x'$ (since any two lines in a projective plane intersect). Thus, the rays through $p$ pair up every point $x \in L_1$ with a unique point $x' \in L_2$, and simultaneously pair every point on $L_1$ with a unique line through $p$:

$$\text{Points on } L_1 \longleftrightarrow \text{Lines through } p \longleftrightarrow \text{Points on } L_2$$

Because all three sets are in one-to-one correspondence, $\vert{}L_1\vert{} = \vert{}L_2\vert{} = \text{deg}(p)$. Since $L_1, L_2$ are arbitrary, every line has the same number of points $s + 1$, and every point has the same number of lines $s + 1$ passing through it.

$s$ (possibly infinite) and $\ge 2$ is called the **order** of the projective plane. When $s$ is finite, double counting flags starting from one point $p$ (each of the $s + 1$ lines through $p$ holds $s$ additional points, covering all of $\mathcal{P}$) gives:

$$|\mathcal{P}| = |\mathcal{L}| = 1 + (s + 1)s = s^2 + s + 1.$$

### Projective spaces of arbitrary dimension and the Veblen–Young axiom

In dimension $3$ or higher, we cannot require every two lines to intersect, because skew lines exist in $3$-space. How do we express "no parallel lines exist inside any plane" purely in terms of points and lines, without mentioning planes first? That is the job of the **Veblen–Young axiom**:

A **projective space** is a linear space $\mathcal{S}$ satisfying the **Veblen–Young axiom** $(\star)$:

> $(\star)$ Whenever $L_1$ and $L_2$ are two distinct lines meeting at a point $z$, and we pick two distinct points $x_1, y_1 \in L_1 \setminus \{z\}$ and two distinct points $x_2, y_2 \in L_2 \setminus \{z\}$, the lines $x_1 x_2$ and $y_1 y_2$ must intersect in a point.

![Veblen-Young crossbar axiom and the 7-point Fano plane PG(2,2)](figures/maths4_classes_veblen_young_fano.png)

*Figure 8. (a) The Veblen–Young axiom: the lines $L_1$ and $L_2$ meet at $z$, and for points $x_1, y_1$ on $L_1$ and $x_2, y_2$ on $L_2$ the lines $x_1 x_2$ and $y_1 y_2$ must meet, here at $w$. (b) The Fano plane $\mathrm{PG}(2, 2) = S(2, 3, 7)$, each point labelled by its coordinates; the circle is the seventh line.*

Look at panel (a) of Figure 8 to see why $(\star)$ works. The lines $L_1$ and $L_2$ meet at $z$, so they lie in a common $2$-dimensional flat sheet. In an affine (Euclidean) plane, you could pick $x_1 x_2$ parallel to $y_1 y_2$, and those two crossbar lines would never meet. Forcing $x_1 x_2$ and $y_1 y_2$ to meet kills off parallel lines inside every $2$-dimensional sheet while still allowing skew lines elsewhere in $3$-space. In fact, the Veblen–Young axiom $(\star)$ is completely equivalent to:

> $(\star')$ Whenever $x_1, x_2, x_3$ are three noncollinear points of $\mathcal{S}$, the subspace $X = \langle x_1, x_2, x_3 \rangle$ they generate carries the induced geometry of a (possibly degenerate) **projective plane**.

Just as with planes, we distinguish thick projective spaces from glued-together pieces:

- A projective space is **irreducible** if **every line is thick** (incident with at least $3$ points). If at least one line is thin (incident with only $2$ points), the projective space is **reducible**. For a projective space of dimension at least $2$, irreducibility is equivalent to requiring every generated plane $\langle x_1, x_2, x_3 \rangle$ of three noncollinear points to be an *irreducible* projective plane.
- The **dimension** of a projective space $\mathcal{S}$ is defined via its generating index $N_{\mathcal{S}}$ (the minimum number of points needed to generate $\mathcal{S}$):

$$\dim(\mathcal{S}) = N_{\mathcal{S}} - 1.$$

Why subtract $1$? Because a single point requires $N_{\mathcal{S}} = 1$ generator and has dimension $0$; a line is generated by $N_{\mathcal{S}} = 2$ distinct points and has dimension $1$; and a projective plane is generated by $N_{\mathcal{S}} = 3$ noncollinear points $x_1, x_2, x_3$ and has dimension $2$ (any point $y \neq x_1$ lies on the line $x_1 y$, which intersects $x_2 x_3$ at some point $w$, so $y$ lies on $x_1 w$ and is generated by $\{x_1, x_2, x_3\}$). By convention, if $\Sigma$ denotes the collection of all subspaces of $\mathcal{S}$, we often refer to the pair $(\mathcal{P}, \Sigma)$ itself as a projective space, and we declare the empty structure $(\emptyset, \{\emptyset\})$ to be a projective space of **dimension $-1$** ($N = 0$ generators).

### Combinatorial designs

Projective and affine planes have the striking uniformity that *every* pair of distinct points lies on $1$ line, and *every* line has the exact same size $k$. Combinatorial design theory generalizes this symmetry in two directions: instead of demanding balance for pairs ($t = 2$) of points, we can demand balance for arbitrary $t$-tuples of points; and instead of requiring $1$ line per $t$-tuple, we can require any constant number $\lambda$ of lines.

#### Definition and notations: $t$-designs and Steiner systems

We will be covering this in detail later, so we will not bother about it here.

#### Unitals, inversive planes, and Witt (Mathieu) designs

Beyond projective and affine spaces, three celebrated geometric and group-theoretic families of Steiner systems appear throughout finite geometry:

**Unitals $S(2, n + 1, n^3 + 1)$ and Hermitian curves.** A Steiner system of type $S(2, n + 1, n^3 + 1)$ is called a **unital**. To see where $n^3 + 1$ points and $(n + 1)$-point lines come from naturally, work inside the projective plane $\mathrm{PG}(2, q^2)$ over a square-order finite field $\mathbb{F}_{q^2}$. After a suitable choice of projective coordinates, a **Hermitian curve** $\mathcal{H}$ in $\mathrm{PG}(2, q^2)$ has equation

$$X_0^{q+1} + X_1^{q+1} + X_2^{q+1} = 0.$$

We can verify that this is Hermitian with the Frobenius automorphism $\bar{x} = x^q$ by applying $f(X, X) = \sigma(f(X, X))$. There are two ways to check this. The first way is with the underlying two-variable sesquilinear form:

$$f(X, Y) = X_0 Y_0^q + X_1 Y_1^q + X_2 Y_2^q$$

It is linear in $X$ and $\sigma$-semilinear in $Y$, and it satisfies the Hermitian symmetry condition $f(Y, X) = \sigma(f(X, Y))$ because:

$$\sigma(f(X, Y)) = (X_0 Y_0^q + X_1 Y_1^q + X_2 Y_2^q)^q = X_0^q (Y_0^q)^q + X_1^q (Y_1^q)^q + X_2^q (Y_2^q)^q = Y_0 X_0^q + Y_1 X_1^q + Y_2 X_2^q = f(Y, X)$$

Here we used two properties of $\mathbb{F}_{q^2}$:

In characteristic $p$ (where $q$ is a power of $p$), raising a sum to the power $q$ distributes across addition: $(a + b)^q = a^q + b^q$.

For any element $y \in \mathbb{F}_{q^2}$, $y^{q^2} = y$.

Set $Y = X$ to get the diagonal evaluation: $f(X, X) = X_0^{q+1} + X_1^{q+1} + X_2^{q+1}$

The second way is to apply $\sigma$ to $f(X, X)$, we get:

$$\sigma(f(X, X)) = (X_0^{q+1} + X_1^{q+1} + X_2^{q+1})^q = (X_0^{q+1})^q + (X_1^{q+1})^q + (X_2^{q+1})^q$$

Look at the exponent on each term: $(X_i^{q+1})^q = X_i^{q^2 + q} = X_i^{q^2} \cdot X_i^q$. Since $X_i \in \mathbb{F}_{q^2}$, we have $X_i^{q^2} = X_i$, so:

$$X_i^{q^2} \cdot X_i^q = X_i \cdot X_i^q = X_i^{q+1}$$

Therefore, $\sigma(f(X, X)) = f(X, X)$.
The curve $\mathcal{H}$ contains $q^3 + 1$ points, and every line of $\mathrm{PG}(2, q^2)$ meets $\mathcal{H}$ in either $1$ point (a tangent) or $q + 1$ points (a secant). Taking $\mathcal{H}$ as the point set and keeping only the lines of $\mathrm{PG}(2, q^2)$ that meet $\mathcal{H}$ in $q + 1$ points produces a linear space $\mathcal{U}_{\mathcal{H}}$: any two points of $\mathcal{H}$ determine a unique line of $\mathrm{PG}(2, q^2)$, which already hits $\mathcal{H}$ twice and must therefore be a $(q + 1)$-point secant. So $\mathcal{U}_{\mathcal{H}}$ is a Steiner system $S(2, q + 1, q^3 + 1)$, and hence a unital.

Since $\sigma(f(X, X)) = f(X, X)$, $f(X, X)$ always takes values in the fixed subfield $\mathbb{F}_q$ (just as $H(x, x)$ over $\mathbb{C}$ always takes values in the real subfield $\mathbb{R}$). The Hermitian curve is the locus of points where this $\mathbb{F}_q$-valued norm equals $0$.

**Worked example ($q = 2$ in $\mathrm{PG}(2, 4)$).** Let us carry this out by hand for $q = 2$. Write $\mathbb{F}_4 = \{0, 1, \alpha, \alpha + 1\}$ (remember $\alpha$ is kind of like $i$ and the "alpha" field elements can be read as $1 \cdot \alpha + 0$ and $1\cdot \alpha + 1$). Coefficients are added modulo $2$: $1 + 1 = 0$ and $\alpha + \alpha = 0$, and $\alpha^2 + \alpha + 1 = 0$ (because it is the only quadratic polynomial over $\mathbb{F}_2$ that has no roots in $\mathbb{F}_2$). The only such polynomial is $x^2 + x + 1$. Raising elements of $\mathbb{F}_4$ to the power $q + 1 = 3$ sends $0^3 = 0$, while $1^3 = 1$, $\alpha^3 = \alpha(\alpha + 1) = \alpha^2 + \alpha = 1$, and $(\alpha + 1)^3 = 1$. Every nonzero element of $\mathbb{F}_4$ cubes to $1$.

So in $\mathrm{PG}(2, 4)$, the equation $X_0^3 + X_1^3 + X_2^3 = 0$ just adds $1$ once for each nonzero coordinate of $(X_0 : X_1 : X_2)$. In characteristic $2$, a sum of $1$'s vanishes only when an even number of terms are nonzero. Since $(0 : 0 : 0)$ is excluded, a point of $\mathrm{PG}(2, 4)$ lies on $\mathcal{H}$ if and only if two of its coordinates are nonzero and one coordinate is $0$. There are $3$ choices for which coordinate is $0$; scaling the first nonzero coordinate to $1$ leaves $3$ choices $\{1, \alpha, \alpha + 1\}$ for the remaining slot, giving $3 \times 3 = 9 = 2^3 + 1$ points on $\mathcal{H}$:

$$(0 : 1 : 1),\; (0 : 1 : \alpha),\; (0 : 1 : \alpha + 1),$$

$$(1 : 0 : 1),\; (1 : 0 : \alpha),\; (1 : 0 : \alpha + 1),$$

$$(1 : 1 : 0),\; (1 : \alpha : 0),\; (1 : \alpha + 1 : 0).$$

Test two lines of $\mathrm{PG}(2, 4)$ against $\mathcal{H}$. The line $X_0 = 0$ has $5$ points in $\mathrm{PG}(2, 4)$: $(0 : 1 : 0)$, $(0 : 0 : 1)$, $(0 : 1 : 1)$, $(0 : 1 : \alpha)$, and $(0 : 1 : \alpha + 1)$. The last three lie on $\mathcal{H}$, so $X_0 = 0$ is one of the $12$ secant blocks of $\mathcal{U}_{\mathcal{H}}$. Meanwhile, the line $X_1 + X_2 = 0$ contains $(1 : 0 : 0)$, $(0 : 1 : 1)$, $(1 : 1 : 1)$, $(\alpha : 1 : 1)$, and $(\alpha + 1 : 1 : 1)$. Only $(0 : 1 : 1)$ has two nonzero coordinates, so this line touches $\mathcal{H}$ at a single point and is one of the $9$ tangents. Thus $\mathcal{U}_{\mathcal{H}}$ is an $S(2, 3, 9)$, which by our $S(2, n, n^2)$ rule is an affine plane of order $3$, necessarily isomorphic to $\mathrm{AG}(2, 3)$.

**Finite inversive planes $S(3, q + 1, q^2 + 1)$.** A Steiner system of type $S(3, q + 1, q^2 + 1)$ is called a **finite inversive plane**. Think of a sphere in ordinary $3$-space: any $3$ distinct points on a sphere determine a unique plane slice, which cuts the sphere in a circle.

In $\mathrm{PG}(3, q)$, the finite-field counterpart of a sphere is an **elliptic quadric** $Q^-(3, q)$, meaning a nonsingular quadric of $\mathrm{PG}(3, q)$ that contains points ($q^2 + 1$ of them) *but contains no lines*. Because $Q^-(3, q)$ contains no straight lines, no three points of $Q^-(3, q)$ are ever collinear in $\mathrm{PG}(3, q)$. So any $3$ distinct points of $Q^-(3, q)$ span a unique plane $\alpha$ of $\mathrm{PG}(3, q)$, and $\alpha$ slices $Q^-(3, q)$ in a nonsingular conic (a finite "circle") of $q + 1$ points. Taking the points of $Q^-(3, q)$ as points and these conic plane-sections as blocks yields a finite inversive plane $S(3, q + 1, q^2 + 1)$, called **classical** (or **Miquelian**).

For $q = 3$, this produces an $S(3, 4, 10)$, which is an example of a Steiner quadruple system; up to isomorphism, there is only one inversive plane of type $S(3, 4, 10)$, namely this classical one. What does this mean?

For a given parameter set $S(3, k, v)$, there can often be multiple non-isomorphic Steiner systems that have the exact same parameters $(3, k, v)$, meaning they have the same number of points and block sizes, but their blocks are wired together in fundamentally different ways. For example, for $q = 8$, there are two non-isomorphic inversive planes of type $S(3, 9, 65)$: the classical one built from the elliptic quadric $Q^-(3, 8)$ and a second non-classical one built from a Suzuki-Tits ovoid.

Saying that the classical inversive plane is the only one of type $S(3, 4, 10)$ up to isomorphism means that if we take any set of $10$ points and arrange $4$-element subsets (blocks) so that every $3$ points lie in a unique block, the resulting incidence structure is guaranteed to be isomorphic to the plane sections of $Q^-(3, 3)$. There is only one structural way to wire an $S(3, 4, 10)$ together.

By "wired differently" we mean if we label all the points from $1$ to $n$, the connection pattern is so different that no possible renaming of the points can make the two structures match.

Why are these Steiner systems referred to as inversive planes? In classical Euclidean geometry, the inversive plane (or Möbius plane) is constructed by taking the ordinary affine plane $\mathbb{R}^2$ and adding a single point at infinity, $\infty$. In this extended plane, a straight line together with $\infty$ is treated as a circle of infinite radius passing through $\infty$. Under this unification, every pair of circles intersects in at most two points, any three distinct points determine a unique circle, and the geometry is preserved by geometric inversion across any circle (which can swap straight lines and ordinary circles) and by fractional linear (Möbius) transformations $z \mapsto \frac{az+b}{cz+d}$. Through stereographic projection from the north pole $\infty$, this extended plane $\mathbb{R}^2 \cup \{\infty\}$ maps directly onto the unit sphere $S^2$ in $\mathbb{R}^3$, where both ordinary circles and lines-plus-$\infty$ correspond to planar cross-sections of the sphere.

Over a finite field $\mathbb{F}_q$, an $S(3, q+1, q^2+1)$ does the exact same thing: if we pick any point $\infty$ of the $q^2+1$ points and remove it, the remaining $q^2$ points and the blocks that passed through $\infty$ (now of size $q$) form an affine plane of order $q$, while the elliptic quadric $Q^-(3, q)$ acts as the finite sphere under stereographic projection. Because it is the direct finite analogue of the classical geometry of circles and geometric inversion, it is called an inversive plane.

**The five Mathieu (Witt) designs, derived designs, and extensions.** Outside infinite families, Carmichael and Witt proved that for each of the five parameter triples

$$(t, k, v) \in \{(4, 5, 11),\; (5, 6, 12),\; (3, 6, 22),\; (4, 7, 23),\; (5, 8, 24)\},$$

there is a unique Steiner system $S(t, k, v)$ up to isomorphism. These five Steiner systems are called the **Mathieu** or **Witt designs**. The systems $S(4, 5, 11)$ and $S(5, 6, 12)$ are called the **small Mathieu** (or **small Witt**) designs, while $S(3, 6, 22)$, $S(4, 7, 23)$, and $S(5, 8, 24)$ are called the **large Mathieu** (or **large Witt**) designs.

Notice how the three numbers in each group shift by $1$ together. That comes from zooming in on a single point of a geometry. In any point-line geometry $\mathcal{S}$ where every line through a chosen point $x$ has size at least $3$, the **internal structure** $\mathcal{S}_x$ at $x$ takes $x^\perp \setminus \{x\}$ (all points collinear with $x$, other than $x$ itself) as its points, and takes all lines of $\mathcal{S}$ through $x$ (each with $x$ removed) as its lines.

Suppose $\mathcal{D}$ is a $t$-$(v, k, \lambda)$-design with $t \ge 2$ and $k \ge 3$, and pick any point $x$ of $\mathcal{D}$. Because $t \ge 2$, $\mathcal{D}$ is at least a $2$-design, so $x$ shares blocks with *every* other point of $\mathcal{D}$; removing $x$ leaves all $v - 1$ remaining points. Keeping only blocks that contained $x$, and deleting $x$ from each of them, trims every kept block from size $k$ down to size $k - 1 \ge 2$. And if you pick any $t - 1$ distinct points among the remaining $v - 1$ points, putting $x$ back beside them gives $t$ distinct points of $\mathcal{D}$, which lie together in $\lambda$ blocks of $\mathcal{D}$ (all containing $x$, so all surviving in $\mathcal{D}_x$).

Therefore $\mathcal{D}_x$ is a $(t - 1)$-$(v - 1, k - 1, \lambda)$-design, called the **derived design of $\mathcal{D}$ with respect to $x$**. In the reverse direction, $\mathcal{D}$ is called an **extension** of $\mathcal{D}_x$, and a design is called **extendable** if it has at least one extension.

When $\mathcal{D}$ is a Steiner system $S(t, k, v)$ ($t \ge 2, k \ge 3$), any derived design $\mathcal{D}_x$ is a Steiner system $S(t - 1, k - 1, v - 1)$. In particular, the derived design of any Steiner quadruple system $S(3, 4, v)$ is a Steiner triple system $S(2, 3, v - 1)$, and every inversive plane $S(3, q + 1, q^2 + 1)$ is an extension of an affine plane $S(2, q, q^2)$ of order $q$ (deleting one point $x$ from the sphere $Q^-(3, q)$ and keeping only circles through $x$ turns those circles into the lines of an affine plane, just like stereographic projection).

Panel (b) of Figure 9 shows how the Witt designs stack into two extension towers. On the right, $S(5, 8, 24)$ extends $S(4, 7, 23)$, which extends $S(3, 6, 22)$, which extends $S(2, 5, 21)$, the projective plane of order $4$. On the left, $S(5, 6, 12)$ extends $S(4, 5, 11)$, which extends the inversive plane $S(3, 4, 10)$, which extends $S(2, 3, 9) \cong \mathrm{AG}(2, 3)$, the affine plane of order $3$.

![AG(2,3) parallel classes and the two Witt design extension towers](figures/maths4_classes_design_extensions.png)

*Figure 9. (a) The $12$ blocks of $\mathrm{AG}(2, 3) = S(2, 3, 9)$ on a $3 \times 3$ array of points, in four parallel classes of three disjoint lines (slopes $0$, $\infty$, $1$ and $2$ mod $3$); colours tell apart the lines within a class. (b) The two towers of Witt designs: a downward arrow takes a derived design, from $(t, k, v)$ to $(t - 1, k - 1, v - 1)$, and an upward arrow is a one-point extension.*

---

### Generalized quadrangles

In a projective plane, every point $x$ outside a line $L$ is collinear with **all** points of $L$, so triangles are everywhere. What happens if we forbid triangles completely by swinging to the opposite extreme: every point $x$ outside a line $L$ is collinear with **precisely one** point of $L$?

#### Definition and why both axioms matter

A partial linear space $\mathcal{S} = (\mathcal{P}, \mathcal{L}, \mathrm{I})$ is called a **generalized quadrangle** (abbreviated **GQ**) if:

1. There exist two lines that have no points in common (disjoint lines exist).
2. For every anti-flag $(x, L)$ (a point $x$ not on a line $L$), there exists a **unique** point $y$ on $L$ collinear with $x$.

![Generalized quadrangle W(3,2) ("the doily") showing unique projection from an anti-flag and an ordinary 4-gon subgeometry](figures/maths4_classes_gq_doily.png)

*Figure 10. The generalized quadrangle $W(3, 2)$, the doily: $15$ points and $15$ lines of $3$ points (five sides, five lines through the centre and five arcs; the centre is not a point). (a) For the anti-flag $(x, L)$, $y$ is the unique point of $L$ collinear with $x$. (b) Two noncollinear points $A_1, A_2$ and two of their common neighbours $q_1, q_2$ form an ordinary $4$-gon; the hollow rings mark the third point on each of its four lines.*

Look closely at what these two axioms accomplish together:

- **No triangles can exist.** Suppose $x, y_1, y_2$ formed three mutually noncollinear-line vertices of a triangle (with $x$ off the line $L = y_1 y_2$, joined by distinct lines $x y_1$ and $x y_2$ to two points of $L$). That would give *two* points on $L$ collinear with $x$, violating Axiom 2. Instead, the smallest closed circuits of lines are $4$-sided quadrangles (as in panel (b) of Figure 10), which is why Tits named these geometries *generalized quadrangles*.
- **Why do we need Axiom 1 (two disjoint lines exist)?** Suppose $\mathcal{S}$ consisted of a single line $L$ (no anti-flags at all, so Axiom 2 holds vacuously), or suppose $\mathcal{S}$ were a tree-like star of lines all meeting at one central hub point $p$ with no thin cross-lines (for any $x \neq p$ and any line $L \not\ni x$, $p \in L$ is the unique point on $L$ collinear with $x$, and $p$ lies on *every* line so $(p, L)$ is never an anti-flag). Axiom 1 rules out these degenerate "pencil" configurations cleanly.
- **Automatic self-duality of the class:** Let us check why **the point-line dual $\mathcal{S}^D$ of any GQ $\mathcal{S}$ is again a GQ**. First, does every point $x$ of $\mathcal{S}$ lie on at least two lines (so $\mathcal{S}^D$ is well-defined)? By Axiom 1, there exist two disjoint lines $L_1$ and $L_2$; since $L_1 \cap L_2 = \emptyset$, $x$ misses at least one of them, so Axiom 2 gives at least one line through $x$. Suppose for contradiction that $x$ lay on only one line $M$. Because $M$ must intersect any line missing $x$ (by Axiom 2), if $x \in L_1$ then $L_1 = M$, which would intersect $L_2$, impossible. Thus $x$ lies on neither $L_1$ nor $L_2$, and $M$ intersects $L_1$ at a unique point $y$ and $L_2$ at a unique point $z$ ($y \neq z$ since $L_1 \cap L_2 = \emptyset$). Because $L_1$ has at least two points, pick $y' \in L_1 \setminus \{y\}$. By Axiom 2 applied to $(y', L_2)$, some line $N$ connects $y'$ to a point $w \in L_2$. Then $(x, N)$ is an anti-flag (as $y' \notin M$), so $M$ must intersect $N$ at some point collinear with $y'$, which can only be $y$ (by Axiom 2 on $(y', M)$). That forces $y, y' \in L_1 \cap N$ with $y \neq y'$, so $N = L_1$, contradicting $w \in N \cap L_2$ with $L_1 \cap L_2 = \emptyset$. Hence **every point of a GQ lies on at least two lines**. Swapping points and lines turns two noncollinear points (any $p \in L_1$ has a noncollinear point on $L_2$) into two disjoint lines and preserves Axiom 2 on every anti-flag $(L, x)$, so $\mathcal{S}^D$ is always a GQ.

#### Orders and parameter restrictions for generalized quadrangles

Does every generalized quadrangle have a uniform order $(s, t)$ i.e. do every point and every line follow the same counts? Almost. Here is how the whole family of generalized quadrangles breaks down:

**Thick generalized quadrangles ($s \ge 2$ and $t \ge 2$):** In these geometries, every line has at least 3 points, and every point has at least 3 lines passing through it. A standard theorem of incidence geometry proves that in any thick generalized quadrangle, every line is forced to have the exact same number of points $s + 1$, and every point is forced to lie on the exact same number of lines $t + 1$. Thus, every thick generalized quadrangle has a uniform order $(s, t)$ with $s, t \ge 2$. (For example, the symplectic space $W(3, q)$ has order $(q, q)$, and the elliptic quadric $Q^-(5, q)$ has order $(q, q^2)$.)

**Thin generalized quadrangles (where $t = 1$ or $s = 1$):** One can prove that any generalized quadrangle with $t = 1$ (i.e. it has 2 lines through every point) must be an $(n_1 \times n_2)$-grid (where the points are where rows and columns meet and so have only 2 lines through them), and any generalized quadrangle with $s = 1$ (i.e. any line has 2 points) must be a dual grid $K_{n_1, n_2}$ (i.e. a bipartite graph).

Within these grids and dual grids, there are two subcases. If $n_1 = n_2$ (symmetrical), then all lines have the same size AND all points lie on the same number of lines. So symmetrical grids have a valid order $(s, 1)$ (where $s = n_1 - 1$), and symmetrical dual grids have a valid order $(1, t)$ (where $t = n_1 - 1$).

But if $n_1 \neq n_2$ (nonsymmetrical), then in a nonsymmetrical grid, rows have size $n_2$ and columns have size $n_1$, so there is no single number $s$ for all lines (even though $t = 1$). Dually, in a nonsymmetrical dual grid, points have either $n_1$ or $n_2$ lines through them, so there is no single number $t$ for all points (even though $s = 1$).

When $\mathcal{S}$ is a **finite** generalized quadrangle of order $(s, t)$, two powerful arithmetic restrictions govern $(s, t)$:

**Divisibility condition:** $(s + t)$ must divide $st(s + 1)(t + 1)$.

**Higman's inequalities:** If $s \ge 2$ and $t \ge 2$ (both points and lines are thick), then neither parameter can exceed the square of the other:

$$s \le t^2 \qquad \text{and} \qquad t \le s^2.$$

**Worked test on concrete parameters:**

Take $s = 2, t = 2$ (the "doily" $W(3, 2)$ drawn in Figure 10, with $15$ points and $15$ lines of $3$ points each): $s + t = 4$, and $st(s+1)(t+1) = 4 \cdot 3 \cdot 3 = 36$, which is divisible by $4$ ($36 / 4 = 9$); and $2 \le 2^2 = 4$ satisfies Higman's bound.

What if someone asks whether a thick GQ of order $(s, t) = (2, 5)$ can exist? $s + t = 7$ fails to divide $10 \cdot 3 \cdot 6 = 180$, but a quicker way is Higman's inequality which kills it at a glance: $t = 5 > 2^2 = s^2$, impossible. What about $(s, t) = (2, 3)$? It satisfies Higman's inequality ($3 \le 4$), *but* $s + t = 5$ does not divide $st(s+1)(t+1) = 6 \cdot 3 \cdot 4 = 72$. Thus **no generalized quadrangle of order $(2, 3)$ can exist**, jumping straight from $(2, 2)$ to $(2, 4)$ (where $2 + 4 = 6$ divides $8 \cdot 3 \cdot 5 = 120$, and indeed a classical GQ $Q^-(5, 2)$ of order $(2, 4)$ exists).

---

### Polar spaces
We will not speak about these as they are covered in the projective geometry notes.

### Generalized polygons

Look back at two geometries we have already met. In a **projective plane**, there are no $2$-gons (any two points determine *at most* one line), ordinary $3$-gons (triangles) exist, and *any two elements* (two points, two lines, or a point and a line) can be placed inside an ordinary $3$-gon subgeometry.

In a **generalized quadrangle**, there are no $2$-gons and no $3$-gons, ordinary $4$-gons exist, and *any two elements* can be placed inside an ordinary $4$-gon subgeometry (as we saw in panel (b) of Figure 10).

In 1959, Jacques Tits noticed that this pattern defines an infinite hierarchy of rank-$2$ building blocks for simple groups, one for each polygon number $n \ge 2$.

#### Definition via ordinary $n$-gon subgeometries

For any integer $n \ge 3$, a **generalized $n$-gon** is a partial linear space $\mathcal{S} = (\mathcal{P}, \mathcal{L}, \mathrm{I})$ satisfying three axioms:

**No smaller polygons:** $\mathcal{S}$ contains **no** subgeometries that are ordinary $m$-gons for any $m \in \{3, 4, \dots, n - 1\}$.

**Existence of $n$-gons:** $\mathcal{S}$ contains subgeometries that are ordinary $n$-gons.

**Every pair lies in an $n$-gon ("apartment" property):** For *any* two elements $\{A_1, A_2\} \subseteq \mathcal{P} \cup \mathcal{L}$ (two points, two lines, or one point and one line), there exists a subgeometry $\mathcal{S}' = (\mathcal{P}', \mathcal{L}', \mathrm{I}')$ of $\mathcal{S}$ isomorphic to an ordinary $n$-gon that contains both $A_1$ and $A_2$ ($\{A_1, A_2\} \subseteq \mathcal{P}' \cup \mathcal{L}'$).

Combining this with **generalized $2$-gons** (generalized digons, where $|\mathcal{P}|, |\mathcal{L}| \ge 2$ and $\mathrm{I} = \mathcal{P} \times \mathcal{L}$), a point-line geometry is called a **generalized polygon** if it is a generalized $n$-gon for some $n \ge 2$.

Several immediate consequences and structural connections follow right from the axioms:

**Self-duality of the class:** Because ordinary $m$-gons are self-dual and $\{A_1, A_2\} \subseteq \mathcal{P} \cup \mathcal{L}$ treats points and lines completely symmetrically, **the point-line dual of any generalized $n$-gon is again a generalized $n$-gon**.

**Thin examples for every $n \ge 3$:** Every ordinary $n$-gon ($n \ge 3$) is trivially a generalized $n$-gon of order $(s, t) = (1, 1)$.

**Small values of $n$:**
The **generalized $3$-gons** are precisely the **possibly degenerate projective planes** (both nondegenerate projective planes and near-pencils). Why is a near-pencil on $4$ points a generalized $3$-gon? It contains no $m$-gons for $m < 3$ (it is a partial linear space), it contains ordinary triangles ($p$, $x_1$, $x_2$), and any two elements (say two points $x_1, x_2$ on the long line, plus the apex $p$) sit inside a triangle $\{p, x_1, x_2\}$. Notice, however, that a near-pencil on $\ge 4$ points does *not* have a uniform order $(s, t)$ because its lines have mixed sizes $n - 1$ and $2$.

The **generalized $4$-gons** are precisely the **generalized quadrangles**.

**Diameter, near $n$-gons, and doubles:** Every generalized $n$-gon ($n \ge 2$) has diameter $\lfloor n / 2 \rfloor$ (just like walking halfway around an ordinary $n$-gon from one vertex to an opposite vertex).

A connected partial linear space of diameter $d$ is called a **near $2d$-gon** if for every point $p$ and every line $L$, there is a *unique* point on $L$ nearest to $p$. It is called a **near $(2d + 1)$-gon** ($d \ge 1$) if for every $(p, L)$ at distance $d(p, L) \le d - 1$ there is a unique point on $L$ nearest to $p$, while at least one pair $(p', L')$ achieves $d(p', L') = d$ (all points on $L'$ tied at maximal distance $d$ from $p'$, like a vertex opposite the base of a triangle or pentagon). Every generalized $n$-gon ($n \ge 3$) is a near $n$-gon.

Doubling an ordinary $n$-gon subdivides each of its $n$ edges into two, turning it into an ordinary $2n$-gon, and in general, the double of any generalized $n$-gon ($n \ge 2$) is a generalized $2n$-gon (whose lines are all thin, $s = 1$).

#### The Feit–Higman theorem and order bounds

If ordinary thin $n$-gons ($s = t = 1$) exist for *every* $n \ge 3$, you might naturally expect thick finite generalized $n$-gons ($s, t \ge 2$), say thick generalized pentagons ($n = 5$) or heptagons ($n = 7$), to exist as well. One of the biggest shocks in twentieth-century combinatorics, proved by Walter Feit and Graham Higman in 1964 using matrix eigenvalues of the incidence graph, is that almost all values of $n$ are completely forbidden.

> **Feit–Higman Theorem.** Let $\mathcal{S}$ be a **finite** generalized $n$-gon ($n \ge 3$) of order $(s, t)$. Then at least one of the following six cases holds:
>
> 1. $\mathcal{S}$ is an **ordinary $n$-gon**, with $s = t = 1$ (any $n \ge 3$).
> 2. $\mathcal{S}$ is a **nondegenerate projective plane** ($n = 3$), with $s = t \ge 2$.
> 3. $\mathcal{S}$ is a **generalized quadrangle** ($n = 4$).
> 4. $\mathcal{S}$ is a **generalized hexagon** ($n = 6$); moreover, if $s \neq 1$ and $t \neq 1$, then $st$ must be a perfect square.
> 5. $\mathcal{S}$ is a **generalized octagon** ($n = 8$); moreover, if $s \neq 1$ and $t \neq 1$, then $2st$ must be a perfect square.
> 6. $\mathcal{S}$ is a **generalized dodecagon** ($n = 12$), in which case **either $s = 1$ or $t = 1$** (it is thin).

**Unpacking the implications.** For $n \ge 3$, thick finite generalized $n$-gons ($s \ge 2$ and $t \ge 2$) can ONLY exist for $n \in \{3, 4, 6, 8\}$. Not a single finite thick generalized pentagon ($5$), heptagon ($7$), nonagon ($9$), decagon ($10$), or even dodecagon ($12$) can ever exist.

Where do the "semithin" generalized dodecagons ($n = 12$ with $s = 1$ or $t = 1$) come from? Remember the double of a point-line geometry. Take any thick finite generalized hexagon ($n = 6$) of order $(q, q)$ (such as the split Cayley hexagon of order $(2, 2)$). Its double is a generalized $2 \times 6 = 12$-gon. In that double, every line is a flag $\{x, L\}$ of size $2$ (so $s + 1 = 2 \implies s = 1$), while every point (coming from an original point or line of the hexagon, each incident with $q + 1$ flags) lies on $t + 1 = q + 1$ lines (so $t = q \ge 2$). Taking its point-line dual swaps $(1, q)$ to $(q, 1)$.

Similarly, doubling a projective plane of order $q$ ($n = 3$) produces a generalized $6$-gon of order $(1, q)$, and doubling a GQ of order $(q, q)$ ($n = 4$) produces a generalized $8$-gon of order $(1, q)$, which explains why the arithmetic conditions "$st$ is a square" ($n = 6$) and "$2st$ is a square" ($n = 8$) explicitly include the hypothesis $s \neq 1 \neq t$. For example, projective planes exist for prime powers, and since $s=1$ for the hexagon we get from doubling it, $q$ must be square but that's impossible for a prime number.

There is a parity constraint on $n = 8$. Because $2st$ must be a perfect square in any thick finite generalized octagon ($s, t \ge 2$), $st$ cannot be odd (twice an odd number is never a square), nor can $s = t$. Unlike projective planes, quadrangles, and hexagons, which all admit thick examples with $s = t = q$, **no finite thick generalized octagon can ever have $s = t$** (for example, the classical Ree–Tits octagons have order $(q, q^2)$ with $q = 2^{2e+1}$ an odd power of $2$, making $2st = 2 q^3 = (2^{3e+2})^2$ a perfect square).

Finally, for every thick finite generalized $2n$-gon (so $s \ge 2, t \ge 2$, and by Feit–Higman $2n \in \{4, 6, 8\}$, meaning $n \in \{2, 3, 4\}$), the parameters $s$ and $t$ cannot be too lopsided:

| Thick Finite Generalized $2n$-Gon ($s, t \ge 2$) | Polygon Type | Arithmetic Square Rule | Mutual Bounds Between $s$ and $t$ | Attribution |
| :--- | :--- | :--- | :--- | :--- |
| $n = 2$ ($2n = 4$) | Generalized quadrangle | none (instead $(s+t) \mid st(s+1)(t+1)$) | $s \le t^2$ and $t \le s^2$ | Higman's bounds |
| $n = 3$ ($2n = 6$) | Generalized hexagon | $st$ is a square | $s \le t^3$ and $t \le s^3$ | Haemers–Roos inequalities |
| $n = 4$ ($2n = 8$) | Generalized octagon | $2st$ is a square | $s \le t^2$ and $t \le s^2$ | Higman's bounds |

## Strongly Regular and Distance-Regular Graphs

Whenever a finite point-line geometry has uniform incidence rules, such as a generalized quadrangle of order $(s, t)$ or a partial geometry, its collinearity graph inherits strict local symmetry. Once we record that graph in its symmetric adjacency matrix $A$, linear algebra gives us three strict feasibility tests that any real geometry must pass.

First, eigenvalue multiplicities count the dimensions of real eigenspaces, so those formulas must work out to nonnegative integers. Second, projecting the vertices onto a unit sphere inside one of those eigenspaces puts a ceiling, called the absolute bound, on how many vertices can fit when only two pairwise angles are allowed. Third, the Krein parameters, which track what happens when we multiply two eigenspace projection matrices entry by entry, can never be negative.

### Basic properties and examples of strongly regular graphs

Regularity says every single vertex sees the same number of neighbours $k$. R. C. Bose strengthened this one step further by asking every *pair* of vertices to see a predictable number of common neighbours, depending only on whether the pair is joined by an edge or not. Then we get Strongly Regular Graphs.

#### Definition, parameters, and the double-counting equation

Recall from [the adjacency matrix and its eigenvalues](#the-adjacency-matrix-and-its-eigenvalues) that a finite graph $\Gamma = (V, E)$, neither empty nor complete, is strongly regular with parameters $(v, k, \lambda, \mu)$, written $\mathrm{SRG}(v, k, \lambda, \mu)$, when it has $v$ vertices, every vertex has $k$ neighbours (the valency), any two adjacent vertices have $\lambda$ common neighbours, and any two distinct nonadjacent vertices have $\mu$ common neighbours.

Note that when $\mu > 0$, any two distinct nonadjacent vertices have a common neighbour, so the diameter is $2$. This holds for every primitive (nondegenerate) strongly regular graph, defined below. It fails only when $\mu = 0$, where, as we will see next, the graph falls apart into disjoint complete graphs.
<!-- terms checked: primitive; Krein parameters; orbitals -->

Why do we exclude empty graphs and complete graphs from the definition? In an empty graph there are no edges, so there are no adjacent pairs of vertices to test, and any number $\lambda$ at all would satisfy the third rule by default. In a complete graph $K_v$ every pair of distinct vertices is adjacent, leaving no nonadjacent pairs to pin down $\mu$. Requiring $\Gamma$ to be neither empty nor complete guarantees $k > 0$ (each vertex has at least one neighbour) and $v > k + 1$ (each vertex $x$ has at least one non-neighbour $z \neq x$).

![Distance partition of an SRG around x, and the pentagon C5](figures/maths4_srg_partition_pentagon.png)

*Figure 11. (a) The distance partition of an $\mathrm{SRG}(v, k, \lambda, \mu)$ around a vertex $x$: each neighbour $y$ sends $k - \lambda - 1$ edges to the non-neighbours, and each non-neighbour $z$ receives $\mu$ edges from the neighbours, so $k(k - \lambda - 1) = (v - k - 1)\mu$. (b) The pentagon $C_5 = \mathrm{SRG}(5, 2, 0, 1)$, a conference graph with eigenvalues $(-1 \pm \sqrt{5})/2$: the orange vertex is joined by the orange edges to its two neighbours (blue), and the two grey vertices are its non-neighbours.*

The four numbers $(v, k, \lambda, \mu)$ cannot be chosen freely. They are tied together by a basic double count around a single vertex.

**Parameter relation for strongly regular graphs.** If $\Gamma$ is an $\mathrm{SRG}(v, k, \lambda, \mu)$, then $k - \lambda - 1 \ge 0$, $v - k - 1 \ge 0$, and

$$k(k - \lambda - 1) = (v - k - 1)\mu.$$

Look at Figure 11(a) to read this equation straight off the diagram. Fix one base vertex $x \in V$ and split the vertex set into three boxes: $\{x\}$ itself ($1$ vertex), the neighbour box $\Gamma_1(x)$ ($k$ vertices), and the non-neighbour box $V \setminus (\{x\} \cup \Gamma_1(x))$ ($v - k - 1 \ge 0$ vertices; when $\mu > 0$, so that $\Gamma$ is connected, this third box is the distance-$2$ sphere $\Gamma_2(x)$). Now count the number $N$ of edges crossing between the neighbour box and the non-neighbour box, meaning pairs $(y, z)$ with $y \in \Gamma_1(x)$, $z \notin \{x\} \cup \Gamma_1(x)$, and $y \sim z$.

Counting from the neighbour box outward, there are $k$ choices for $y \in \Gamma_1(x)$. Since $y$ has valency $k$, it sends $k$ edges out in total: $1$ edge goes back to $x$, and $\lambda$ edges stay inside $\Gamma_1(x)$ because $x$ and $y$ are adjacent and share $\lambda$ common neighbours. The remaining $k - \lambda - 1$ edges from $y$ must cross into the non-neighbour box (which also shows $k - \lambda - 1 \ge 0$), giving $N = k(k - \lambda - 1)$.

Counting from the non-neighbour box inward, there are $v - k - 1$ choices for a vertex $z$ not adjacent to $x$. Because $z$ and $x$ are distinct and nonadjacent, they share $\mu$ common neighbours, which are precisely the $\mu$ vertices $y \in \Gamma_1(x)$ joined to $z$. That gives $N = (v - k - 1)\mu$, and equating the two counts proves $k(k - \lambda - 1) = (v - k - 1)\mu$.

#### Disconnected graphs, complements, and primitive versus imprimitive graphs

Two boundary families (which happen to be complements of each other) show what happens when $\mu$ hits the bottom or top of its possible range, $0 \le \mu \le k$.

First, take $r \ge 2$ separate complete graphs $K_m$ on $m \ge 2$ vertices, with no edges between different copies. This disconnected graph is strongly regular with parameters $(v, k, \lambda, \mu) = (rm, m - 1, m - 2, 0)$: each vertex is joined to the other $m - 1$ vertices in its own clique, two vertices in the same clique share the remaining $m - 2$ vertices of that clique, and two vertices in different cliques share $\mu = 0$ common neighbours. In fact, these are the *only* disconnected strongly regular graphs.

**Characterization of disconnected strongly regular graphs.** For any $\mathrm{SRG}(v, k, \lambda, \mu)$, we have $k \ge \lambda + 1$, and four statements are equivalent: $\Gamma$ is the disjoint union of $r$ complete graphs on $m$ vertices for some $r, m \ge 2$; $k = \lambda + 1$; $\mu = 0$; and $\Gamma$ is not connected.

The first two are equivalent because each component is complete, so it has a valency that is one greater than the number of mutual neighbours that it shares with each neighbour. Note that completeness means there are no non-adjacent vertices. Strictly speaking, the definition of a strongly regular graph $\mathrm{SRG}(v, k, \lambda, \mu)$ excludes complete graphs. A disjoint union of complete graphs, however, does have nonadjacent vertices, with no mutual neighbours between them, which allows us to set $\mu = 0$.

Let us verify that the four conditions are equivalent, using the algebraic conditions as well. Disjoint copies of $K_m$ are clearly disconnected, and in any disconnected SRG, picking two vertices from different components forces $\mu = 0$. Since $k > 0$ and $v - k - 1 > 0$ in $k(k - \lambda - 1) = (v - k - 1)\mu$, having $\mu = 0$ on the right is equivalent to having $k = \lambda + 1$ on the left. Finally, suppose $k = \lambda + 1$. Whenever $x$ and $y$ are adjacent, one of $x$'s $k$ neighbours is $y$, and all $k - 1 = \lambda$ remaining neighbours of $x$ must also be neighbours of $y$. That makes the relation "$x = y$ or $x \sim y$" transitive, so it is an equivalence relation on $V$. Each equivalence class is a complete graph of size $m = k + 1 \ge 2$ with no edges to any other class, partitioning $\Gamma$ into $r = \frac{v}{k + 1} \ge 2$ disjoint complete graphs.

**Complement of a strongly regular graph.** What happens when we pass from $\Gamma$ to its complement $\overline{\Gamma}$? Because $\Gamma$ is neither empty nor complete, $\overline{\Gamma}$ is neither complete nor empty, and flipping edges and non-edges preserves strong regularity. If $\Gamma$ is an $\mathrm{SRG}(v, k, \lambda, \mu)$, then its complement $\overline{\Gamma}$ is an $\mathrm{SRG}(\bar{v}, \bar{k}, \bar{\lambda}, \bar{\mu})$ with

$$\bar{v} = v, \quad \bar{k} = v - k - 1,$$

$$\bar{\lambda} = v - 2k + \mu - 2, \quad \bar{\mu} = v - 2k + \lambda.$$

Each of these four formulas comes from counting in $\Gamma$. The vertex count stays $\bar{v} = v$, and each vertex $x$ is nonadjacent in $\Gamma$ to $\bar{k} = v - k - 1$ other vertices. To find $\bar{\lambda}$, pick two vertices $x$ and $y$ that are adjacent in $\overline{\Gamma}$, meaning $x \nsim y$ in $\Gamma$. Their common neighbours in $\overline{\Gamma}$ are the vertices distinct from $x$ and $y$ that are adjacent to *neither* $x$ nor $y$ in $\Gamma$. In $\Gamma$, $\mu$ vertices are adjacent to both $x$ and $y$, leaving $k - \mu$ adjacent only to $x$ and $k - \mu$ adjacent only to $y$; subtracting $(2k - 2\mu) + \mu = 2k - \mu$ from the $v - 2$ vertices other than $x$ and $y$ gives $\bar{\lambda} = v - 2k + \mu - 2$. To find $\bar{\mu}$, pick $x$ and $y$ that are nonadjacent in $\overline{\Gamma}$, meaning $x \sim y$ in $\Gamma$. Now $\lambda$ vertices are adjacent to both in $\Gamma$, while $2k - 2\lambda$ vertices (a count that already includes $x$ and $y$ themselves, since each is adjacent to the other) are adjacent to just one of $x, y$. Subtracting $(2k - 2\lambda) + \lambda = 2k - \lambda$ from all $v$ vertices leaves $\bar{\mu} = v - 2k + \lambda$ vertices nonadjacent to both in $\Gamma$.

Applying this complement formula to $r \ge 2$ disjoint copies of $K_m$ ($m \ge 2$, parameters $(rm, m - 1, m - 2, 0)$) produces the complete $r$-partite graph with $r$ parts of size $m$, which is an SRG with parameters

$$(\bar{v}, \bar{k}, \bar{\lambda}, \bar{\mu}) = \bigl(rm,\; (r - 1)m,\; (r - 2)m,\; (r - 1)m\bigr).$$

Notice that here $\bar{\mu} = \bar{k} = (r - 1)m$. That characterizes complete multipartite SRGs in general.

**Characterization of complete multipartite strongly regular graphs.** Every $\mathrm{SRG}(v, k, \lambda, \mu)$ satisfies $\mu \le k$, with equality $\mu = k$ if and only if $\Gamma$ is a complete multipartite graph.

Why? If $x$ and $y$ are distinct nonadjacent vertices, their common neighbours $\Gamma_1(x) \cap \Gamma_1(y)$ form a subset of $\Gamma_1(x)$, so $\mu \le k$. In a complete multipartite graph with $r$ parts of size $m$, two nonadjacent vertices sit in the same part and are both joined to all $(r - 1)m$ vertices outside their part, giving $\mu = k = (r - 1)m$. Conversely, suppose $\mu = k$ (since $k > 0$, we have $\mu > 0$, so $\Gamma$ is connected). Whenever two distinct vertices $x$ and $y$ are nonadjacent, they lie at distance $2$ and share all $k$ of each other's neighbours ($\Gamma_1(x) = \Gamma_1(y)$). Having the exact same neighbour set makes "equal or nonadjacent" an equivalence relation on $V$, whose equivalence classes are independent parts with every cross-pair joined by an edge, so $\Gamma$ is complete multipartite.

In both of these boundary families, either $\Gamma$ itself ($\mu = 0$) or its complement $\overline{\Gamma}$ ($\mu = k$, which gives $\bar{\mu} = 0$) falls apart into disconnected complete graphs. To separate genuine strongly regular graphs from those two families, we call a strongly regular graph $\Gamma$ **primitive** (or **nontrivial**) if neither $\Gamma$ nor $\overline{\Gamma}$ is a disjoint union of complete graphs, and **imprimitive** (or **trivial**) otherwise. In parameter terms, $\Gamma$ is primitive precisely when $0 < \mu < k$, in which case both $\Gamma$ and $\overline{\Gamma}$ are connected graphs of diameter $2$.

#### Four classic families of strongly regular graphs

**The pentagon $C_5$.** Shown in Figure 11(b), an ordinary $5$-cycle is an $\mathrm{SRG}(5, 2, 0, 1)$. Each of its $5$ vertices has $k = 2$ neighbours, adjacent vertices share $\lambda = 0$ common neighbours because a $5$-cycle contains no triangles, and any two nonadjacent vertices sit $2$ steps apart along the cycle and share $\mu = 1$ common neighbour. You can check $k(k - \lambda - 1) = 2(1) = 2 = (5 - 2 - 1)(1)$. Plugging $(5, 2, 0, 1)$ into the complement formula returns $(5, 2, 0, 1)$: the non-edges of a pentagon form the inner $5$-pointed star (a pentagram), which is another $5$-cycle, so $C_5$ is self-complementary and primitive.

Note that the pentagon $C_5$ and its complement (the inner $5$-pointed star) are isomorphic, which is the exact definition of a graph being self-complementary.

To see the isomorphism explicitly, label the vertices around the outer pentagon in order as $0, 1, 2, 3, 4 \pmod 5$: $0 \sim 1 \sim 2 \sim 3 \sim 4 \sim 0$.

In the complement $\overline{C_5}$ (the $5$-pointed star), the edges connect vertices that were not connected in the pentagon, namely vertices at step $2$: $0 \sim 2 \sim 4 \sim 1 \sim 3 \sim 0$.

Both graphs are single closed loops of $5$ vertices. If we apply the permutation $x \mapsto 2x \pmod 5$ to the vertex labels (sending $0 \mapsto 0$, $1 \mapsto 2$, $2 \mapsto 4$, $3 \mapsto 1$, $4 \mapsto 3$), the outer cycle $0 \sim 1 \sim 2 \sim 3 \sim 4 \sim 0$ maps directly onto the star cycle $0 \sim 2 \sim 4 \sim 1 \sim 3 \sim 0$.

**Triangular graphs $T(m)$ ($m \ge 4$).** Fix an $m$-element set $\{1, 2, \dots, m\}$. The **triangular graph** $T(m)$ takes all $\binom{m}{2} = \frac{m(m - 1)}{2}$ two-element subsets of $\{1, \dots, m\}$ as its vertices, with an edge joining two distinct $2$-subsets whenever they intersect (share $1$ element). For every $m \ge 4$, $T(m)$ is strongly regular with parameters

$$(v, k, \lambda, \mu) = \left(\frac{m(m - 1)}{2},\; 2(m - 2),\; m - 2,\; 4\right).$$

We can verify each count on concrete subsets. Fix $\{1, 2\}$: a $2$-subset overlapping $\{1, 2\}$ in one element chooses either $1$ or $2$ ($2$ choices) and pairs it with one of the remaining $m - 2$ elements $\{3, \dots, m\}$, giving $k = 2(m - 2)$. For two adjacent vertices like $\{1, 2\}$ and $\{1, 3\}$, a common neighbour either contains $1$ ($\{1, j\}$ for any of the $m - 3$ elements $j \in \{4, \dots, m\}$) or avoids $1$ while meeting both ($\{2, 3\}$ alone), giving $\lambda = (m - 3) + 1 = m - 2$. For two nonadjacent (disjoint) vertices like $\{1, 2\}$ and $\{3, 4\}$, a common neighbour must pick one element from $\{1, 2\}$ and one from $\{3, 4\}$, giving $\mu = 2 \times 2 = 4$ for every $m \ge 4$.

Notice what happens at $m = 4$: $T(4)$ has parameters $(6, 4, 2, 4)$ with $\mu = k = 4$. Among $2$-subsets of $\{1, 2, 3, 4\}$, each pair has only one disjoint partner ($\{1, 2\}$ opposite $\{3, 4\}$, $\{1, 3\}$ opposite $\{2, 4\}$, and $\{1, 4\}$ opposite $\{2, 3\}$). They do not share an edge, whereas each item of a pair shares an edge with every other item in each pair. So $T(4)$ is the imprimitive complete $3$-partite graph with $r = 3$ parts of size $2$ (the octahedron graph: its $6$ vertices and $12$ edges are the vertices and edges of the octahedron, the solid with $8$ triangular faces). For all $m \ge 5$, $k = 2(m - 2) > 4 = \mu$, so $T(m)$ is primitive.

**The Petersen graph $\overline{T(5)}$.** At $m = 5$, $T(5)$ has parameters $(10, 6, 3, 4)$. Its complement $\overline{T(5)}$ is the [Petersen graph](#the-petersen-graph-as-a-packing-puzzle) of Figure 2: its $10$ vertices are the $2$-subsets of $\{1, 2, 3, 4, 5\}$, joined by an edge whenever two $2$-subsets are *disjoint*. Feeding $(10, 6, 3, 4)$ into the complement formula gives $\bar{v} = 10$, $\bar{k} = 10 - 6 - 1 = 3$, $\bar{\lambda} = 10 - 12 + 4 - 2 = 0$, and $\bar{\mu} = 10 - 12 + 3 = 1$, so the Petersen graph is an $\mathrm{SRG}(10, 3, 0, 1)$.

Both $\bar{\lambda} = 0$ and $\bar{\mu} = 1$ are immediate on subsets of $\{1, 2, 3, 4, 5\}$: if two pairs like $\{1, 2\}$ and $\{3, 4\}$ are disjoint (adjacent in Petersen), only element $5$ remains outside them, so no $2$-subset can be disjoint from both ($\bar{\lambda} = 0$); if two pairs like $\{1, 2\}$ and $\{1, 3\}$ overlap (nonadjacent in Petersen), $\{4, 5\}$ is the unique $2$-subset disjoint from both ($\bar{\mu} = 1$).

**Square lattice graphs $L_2(n)$ ($n \ge 2$).** The collinearity graph of a symmetrical $(n \times n)$-grid is called a **square lattice graph** and denoted by **$L_2(n)$**. Its $v = n^2$ vertices are the grid points $(i, j)$ in an $n \times n$ array, joined when they share a row or a column. Each point shares its row with $n - 1$ other points and its column with $n - 1$ other points, giving $k = 2n - 2$. Two points in the same row share only the remaining $\lambda = n - 2$ points of that row. Two points $(i_1, j_1)$ and $(i_2, j_2)$ in different rows and different columns share $\mu = 2$ common neighbours, namely the other two corners $(i_1, j_2)$ and $(i_2, j_1)$ of the rectangle they determine. Thus $L_2(n)$ is an $\mathrm{SRG}(n^2, 2n - 2, n - 2, 2)$ (imprimitive $C_4 \cong K_{2, 2}$ when $n = 2$, and primitive for all $n \ge 3$).

### The adjacency matrix of a strongly regular graph

The adjacency matrix $A$ is our main item of interest. When $\Gamma$ is regular with valency $k$, every row of $A$ contains $k$ ones and $v - k$ zeros, so every row adds up to $k$. As we saw in [the adjacency matrix and its eigenvalues](#the-adjacency-matrix-and-its-eigenvalues), $k$ is an eigenvalue, and its multiplicity is the number of connected components; in particular, when $\Gamma$ is connected, $k$ has multiplicity $1$. Every eigenvalue $\theta$ satisfies $|\theta| \leq k$. If $\Gamma$ is bipartite, its eigenvalues come in pairs $\theta, -\theta$, so $-k$ is an eigenvalue too.

Now let $\Gamma = (V, E)$ be an $\mathrm{SRG}(v, k, \lambda, \mu)$, fix an ordering $(p_1, \dots, p_v)$ of its vertices with adjacency matrix $A$, and write $I$ for the $v \times v$ identity matrix and $J$ for the $v \times v$ all-ones matrix.

#### Eigenvalues of J and the quadratic equation for A

If a graph is connected, regular, and has 3 distinct eigenvalues, it is guaranteed to be an SRG; we prove this converse [below](#the-three-eigenvalue-converse-and-the-bose-mesner-algebra), once the eigenvalues of an SRG are in hand.

If we forget the regular condition however, a non-regular graph can have 3 distinct eigenvalues without being an SRG. For example, the complete bipartite graph $K_{1, 3}$ (a star with 1 hub and 3 leaves) has the three eigenvalues $\sqrt{3}, 0, -\sqrt{3}$, yet it is not an SRG because it is not regular: the hub has degree $3$ and the leaves have degree $1$, so $\mathbf{j}$ is not even an eigenvector.

First recall the eigenvalues of the all-ones matrix $J$ from [the all-ones matrix and commuting matrices](#the-all-ones-matrix-and-commuting-matrices): the $v \times v$ matrix $J$ has eigenvalue $v$ with multiplicity $1$, on $\mathbf{j}$, and eigenvalue $0$ with multiplicity $v - 1$, on the vectors whose coordinates add up to $0$.

Next, look at what happens when we square the adjacency matrix $A$. For any $i, j \in \{1, \dots, v\}$, the $(i, j)$-entry of $A^2$ is $(A^2)_{ij} = \sum_{l=1}^v A_{il} A_{lj}$. A product $A_{il} A_{lj}$ equals $1$ when $p_l$ is adjacent to both $p_i$ and $p_j$, and $0$ otherwise, so $(A^2)_{ij}$ simply counts the vertices adjacent to both $p_i$ and $p_j$. It is the number of 2-step walks between any two vertices.

Every pair of indices $(i, j)$ falls into one of three disjoint cases. On the main diagonal ($i = j$, marked by $I$), $(A^2)_{ii}$ counts all neighbours of $p_i$, which is $k$. Off the diagonal when $p_i$ and $p_j$ are adjacent ($d(p_i, p_j) = 1$, marked by $A$), $(A^2)_{ij}$ counts their common neighbours, which is $\lambda$. Off the diagonal when $p_i$ and $p_j$ are nonadjacent ($d(p_i, p_j) > 1$, marked by $J - I - A$, the adjacency matrix of $\overline{\Gamma}$, which we get by starting from all pairs ($J$), then taking off each vertex paired with itself ($I$) and all adjacent pairs ($A$)), $(A^2)_{ij}$ counts their common neighbours, which is $\mu$. Putting all three cases together gives one quadratic matrix equation for $A$:

$$A^2 = k I + \lambda A + \mu(J - I - A),$$

which rearranges to

$$A^2 + (\mu - \lambda)A + (\mu - k)I = \mu J.$$

**Getting the eigenvalue spectrum.** That quadratic equation determines the full eigenvalue spectrum of every strongly regular graph, splitting into the disconnected case ($\mu = 0$) and the connected case ($\mu \neq 0$).

**Disconnected case ($\mu = 0$).** When $\mu = 0$, $\Gamma$ is the disjoint union of $r = \frac{v}{k + 1} \ge 2$ complete graphs $K_m$ of size $m = k + 1 \ge 2$. Ordering the vertices one complete graph at a time makes $A$ block-diagonal with $r$ blocks equal to $J_m - I_m$. Since $J_m$ has eigenvalues $m$ (multiplicity $1$) and $0$ (multiplicity $m - 1$), subtracting $I_m$ shifts them to $m - 1 = k$ (multiplicity $1$) and $-1$ (multiplicity $m - 1$). Across all $r$ blocks, $\Gamma$ has two distinct eigenvalues: $k$ with multiplicity $r$, and $-1$ with multiplicity $r(m - 1) = v - r$.

**Connected case ($\mu \neq 0$).** When $\mu \neq 0$, $\Gamma$ has one eigenvalue $k$ that we already know of, whose eigenvector is the all-ones column $\mathbf{j}$. Since the adjacency matrix is symmetric, all eigenvectors will be orthogonal, so the remaining eigenvectors must be orthogonal to $\mathbf{j}$.

For any eigenvector $x$ orthogonal to $\mathbf{j}$, since $\mathbf{j}^T x = 0$, it implies $Jx = 0$. When we apply the SRG matrix equation $A^2 + (\mu - \lambda)A + (\mu - k)I = \mu J$ to the eigenvector $x$, the right-hand side vanishes and the eigenvalue $\theta$ must satisfy the quadratic equation:

$$\theta^2 + (\mu - \lambda)\theta + (\mu - k) = 0$$

We will see that there are two distinct eigenvalues $R_1$ and $R_2$ satisfying this equation.

$$R_1 = \frac{1}{2}\left(\lambda - \mu + \sqrt{(\lambda - \mu)^2 + 4(k - \mu)}\right),$$

$$R_2 = \frac{1}{2}\left(\lambda - \mu - \sqrt{(\lambda - \mu)^2 + 4(k - \mu)}\right).$$

The following relations hold:

$$k > R_1 \ge 0 \quad \text{and} \quad R_2 < -1,$$

with $R_1 = 0$ if and only if $\Gamma$ is a complete multipartite graph ($\mu = k$).

Sum of roots: $R_1 + R_2 = \lambda - \mu$

Product of roots: $R_1 R_2 = \mu - k \implies \mu = k + R_1 R_2$ and $\lambda = k + R_1 + R_2 + R_1 R_2$

The eigenvalue $k$ has multiplicity $1$, while $R_1$ and $R_2$ have positive integer multiplicities

$$M_1 = \frac{(R_2 + 1)k(k - R_2)}{\mu(R_2 - R_1)} > 0,$$

$$M_2 = \frac{(R_1 + 1)k(k - R_1)}{\mu(R_1 - R_2)} > 0.$$

Let us walk through how this connected spectrum comes out of $A^2 + (\mu - \lambda)A + (\mu - k)I = \mu J$. Divide by $\mu$ to write $J = \frac{1}{\mu}\bigl(A^2 + (\mu - \lambda)A + (\mu - k)I\bigr)$. If $\theta_1, \theta_2, \dots, \theta_v$ are the $v$ eigenvalues of $A$ (listed with multiplicity), then applying the polynomial on the right sends each $\theta_i$ to an eigenvalue $\frac{1}{\mu}\bigl(\theta_i^2 + (\mu - \lambda)\theta_i + (\mu - k)\bigr)$ of $J$. We already know the $v$ eigenvalues of $J$: $v$ appears once, and $0$ appears $v - 1$ times. Test the valency $\theta = k$: using $(v - k - 1)\mu = k(k - \lambda - 1)$, we get

$$\begin{aligned}
\frac{1}{\mu}\bigl(k^2 + (\mu - \lambda)k + \mu - k\bigr) &= \frac{k(k - \lambda - 1) + \mu(k + 1)}{\mu} \\
&= (v - k - 1) + k + 1 = v.
\end{aligned}$$

That uses up the single copy of $v$ among the eigenvalues of $J$, so $k$ has multiplicity $1$ as an eigenvalue of $A$. Every other eigenvalue of $A$ must therefore map to the eigenvalue $0$ of $J$, so it has to satisfy $X^2 + (\mu - \lambda)X + (\mu - k) = 0$.

Check the discriminant $D = (\lambda - \mu)^2 + 4(k - \mu)$ of this quadratic. Because $k \ge \mu$, we have $D \ge 0$, and $D$ cannot be $0$ because $D = 0$ would require $\lambda = \mu = k$, contradicting $k \ge \lambda + 1$. So the quadratic has two distinct real roots $R_1 > R_2$ given by the square-root formulas above. Since $R_1 R_2 = \mu - k \le 0$, we have $R_1 \ge 0$, with $R_1 = 0$ precisely when $\lambda \le \mu = k$ (which holds if and only if $\Gamma$ is complete multipartite). Also $R_1 < k$ (either because $\Gamma$ is connected and $k$-regular, or directly because $k > \lambda$ and $\mu > 0$ imply $k - \mu < k(k - \lambda) + k\mu$, which is equivalent to $\sqrt{D} < 2k - \lambda + \mu$). And because $\mu \neq 0$ forces $k > \lambda + 1$, we have $(\lambda - \mu)^2 + 4(k - \mu) > (\lambda - \mu + 2)^2$, which means $\lambda - \mu + 2 - \sqrt{D} < 0$, or $R_2 < -1$.

Finally, to find the multiplicities $M_1$ of $R_1$ and $M_2$ of $R_2$ without computing determinants, count the total number of eigenvalues and take the trace of $A$:

$$1 + M_1 + M_2 = v, \quad k \cdot 1 + M_1 R_1 + M_2 R_2 = \operatorname{Tr}(A) = 0.$$

Solving those two linear equations for $M_1$ and $M_2$ gives $M_1 = \frac{R_2(v - 1) + k}{R_2 - R_1}$ and $M_2 = \frac{R_1(v - 1) + k}{R_1 - R_2}$. Using $R_i^2 + (\mu - \lambda)R_i + (\mu - k) = 0$ together with $k(k - \lambda - 1) = (v - k - 1)\mu$ turns those fractions into the factored formulas $M_1 = \frac{(R_2 + 1)k(k - R_2)}{\mu(R_2 - R_1)}$ and $M_2 = \frac{(R_1 + 1)k(k - R_1)}{\mu(R_1 - R_2)}$. Checking signs with $k > R_1 \ge 0$ and $R_2 < -1$ shows that $M_1 > 0$ (both $R_2 + 1$ and $R_2 - R_1$ are negative, while $k, k - R_2, \mu$ are positive) and $M_2 > 0$ (all factors positive), so both $R_1$ and $R_2$ genuinely appear as eigenvalues of $A$.

Substituting the square-root expressions for $R_1$ and $R_2$ into $M_i = \frac{R_{3-i}(v - 1) + k}{R_{3-i} - R_i}$ also writes $M_1$ and $M_2$ directly in terms of $(v, k, \lambda, \mu)$:

$$M_1 = \frac{1}{2}\left(v - 1 + \frac{(v - 1)(\mu - \lambda) - 2k}{\sqrt{(\lambda - \mu)^2 + 4(k - \mu)}}\right),$$

$$M_2 = \frac{1}{2}\left(v - 1 - \frac{(v - 1)(\mu - \lambda) - 2k}{\sqrt{(\lambda - \mu)^2 + 4(k - \mu)}}\right).$$

#### Conference graphs and when eigenvalues are integers

Look at the fraction $\frac{(v - 1)(\mu - \lambda) - 2k}{\sqrt{(\lambda - \mu)^2 + 4(k - \mu)}}$ sitting inside $M_1$ and $M_2$. Because $M_1$ and $M_2$ count eigenspace dimensions, they have to be positive integers. If the discriminant $D = (\lambda - \mu)^2 + 4(k - \mu)$ is not a perfect square, $\sqrt{D}$ is irrational, and the only way $M_1$ and $M_2$ can still be integers is if the numerator $(v - 1)(\mu - \lambda) - 2k$ vanishes completely. When the numerator vanishes, it singles out one special family of graphs.

A strongly regular graph $\Gamma$ with parameters $(v, k, \lambda, \mu)$ is called a **conference graph** if there is an integer $\mu \ge 1$ such that

$$v = 4\mu + 1, \quad k = 2\mu, \quad \lambda = \mu - 1.$$

These are the only parameters that send the numerator to $0$.

In any conference graph, $v = 4\mu + 1$ is odd, the discriminant simplifies to $D = (-1)^2 + 4\mu = 4\mu + 1 = v$, the eigenvalues are $R_1 = \frac{-1 + \sqrt{v}}{2}$ and $R_2 = \frac{-1 - \sqrt{v}}{2}$, and the two multiplicities are equal: $M_1 = M_2 = \frac{1}{2}(v - 1) = 2\mu$. (Plugging $(4\mu + 1, 2\mu, \mu - 1, \mu)$ into our complement formula also returns $(4\mu + 1, 2\mu, \mu - 1, \mu)$, so the complement of a conference graph always has the exact same parameters.)

**Characterization of conference graphs.** For any connected $\mathrm{SRG}(v, k, \lambda, \mu)$ ($\mu > 0$), three conditions are equivalent: $\Gamma$ is a conference graph; $M_1 = M_2$ (because the numerator multiplying $\frac{1}{\sqrt{D}}$ is $0$); and $(v - 1)(\mu - \lambda) = 2k$.

The multiplicity formulas make $M_1 = M_2$ equivalent to $(v - 1)(\mu - \lambda) = 2k$ at a glance, and every conference graph satisfies $M_1 = M_2 = \frac{1}{2}(v - 1)$ (from the multiplicities of the eigenvalues). To go from $(v - 1)(\mu - \lambda) = 2k$ back to conference-graph parameters, recall that $\Gamma$ is not complete, so $v > k + 1$, or $v - 1 > k > 0$. Dividing $2k$ by $v - 1$ traps the integer $\mu - \lambda = \frac{2k}{v - 1}$ strictly between $0$ and $2$. The only integer strictly between $0$ and $2$ is $1$, so $\mu - \lambda = 1$ ($\lambda = \mu - 1$) and $v - 1 = 2k$ ($v = 2k + 1$). Substituting $\lambda = \mu - 1$ and $v = 2k + 1$ into $k(k - \lambda - 1) = (v - k - 1)\mu$ gives $k(k - \mu) = k\mu$, which forces $k = 2\mu$ and $v = 4\mu + 1$.

**Integrality of eigenvalues.** Every eigenvalue of an $\mathrm{SRG}(v, k, \lambda, \mu)$ is an integer, except when $\Gamma$ is a conference graph and $v$ is not a perfect square. Both conditions must hold.

Why? If $\mu = 0$, the eigenvalues are the integers $k$ and $-1$. Suppose $\mu \neq 0$ and not all eigenvalues of $\Gamma$ are integers. Look at $R_{1, 2} = \frac{1}{2}\bigl(\lambda - \mu \pm \sqrt{D}\bigr)$ where $D = (\lambda - \mu)^2 + 4(k - \mu)$. If $D = s^2$ were a perfect square, then $s^2$ and $\lambda - \mu$ would have the same even/odd parity (since $4(k - \mu)$ is even), making $\lambda - \mu \pm s$ even integers and $R_1, R_2$ integers. So $D$ must be a nonsquare. Since $M_1$ and $M_2$ are integers, having $\sqrt{D}$ irrational forces $(v - 1)(\mu - \lambda) = 2k$, which means $\Gamma$ is a conference graph. Then $R_{1, 2} = \frac{-1 \pm \sqrt{v}}{2}$, which fail to be integers precisely when the odd number $v$ is not a square.

Compare two small conference graphs to see both cases happen. At $\mu = 1$, the pentagon $C_5 = \mathrm{SRG}(5, 2, 0, 1)$ is a conference graph whose vertex count $v = 5$ is not a square, so its eigenvalues $2$ and $\frac{-1 \pm \sqrt{5}}{2}$ are irrational. At $\mu = 2$, the $3 \times 3$ square lattice graph $L_2(3) = \mathrm{SRG}(9, 4, 1, 2)$ is also a conference graph, and here $v = 9 = 3^2$ *is* a square, so its eigenvalues $4$, $\frac{-1 + 3}{2} = 1$ (multiplicity $4$), and $\frac{-1 - 3}{2} = -2$ (multiplicity $4$) are all integers.

#### Gram matrices and the absolute bounds

Even when $R_1$ and $R_2$ are integers and $M_1$ and $M_2$ are positive integers, a proposed set of SRG parameters can still fail geometrically if $v$ vertices are too many to fit into an $M_i$-dimensional eigenspace.

The tool that turns an eigenspace into Euclidean geometry is the Gram matrix from [rank, determinants and Gram matrices](#rank-determinants-and-gram-matrices). For vectors $\bar{v}_1, \dots, \bar{v}_m$ in $\mathbb{R}^n$ with the standard dot product $(\bar{x}, \bar{y})$, we write $\operatorname{Gr}(\bar{v}_1, \dots, \bar{v}_m)$ for their Gram matrix, the $m \times m$ matrix whose $(i, j)$-entry is $(\bar{v}_i, \bar{v}_j)$. It is symmetric and positive semidefinite, with rank equal to the dimension of the span $\langle \bar{v}_1, \dots, \bar{v}_m \rangle$, and conversely every symmetric positive semidefinite matrix of rank at most $n$ is the Gram matrix of some vectors in $\mathbb{R}^n$.

**Absolute bounds for primitive strongly regular graphs.** If $\Gamma$ is a primitive strongly regular graph with parameters $(v, k, \lambda, \mu)$ and eigenvalue multiplicities $M_1$ and $M_2$, then

$$v \le \frac{1}{2} M_1(M_1 + 3) \quad \text{and} \quad v \le \frac{1}{2} M_2(M_2 + 3).$$

Let us follow the spherical two-distance argument behind these **absolute bounds**. Pick $\{i, i'\} = \{1, 2\}$, so we isolate the eigenspace of $R_i$ (dimension $M_i$) by killing off the other two eigenvalues $k$ and $R_{i'}$. Form the $v \times v$ symmetric matrix

$$F = \frac{1}{(R_{i'} + 1)k}(A - R_{i'} I)(A - k I).$$

(Because $\Gamma$ is primitive, $R_1 > 0$ and $R_2 < -1$, so $R_{i'} + 1 \neq 0$.) Check the eigenvalues of $F$: both $R_{i'}$ and $k$ map to $0$ (total multiplicity $M_{i'} + 1$), while $R_i$ maps to $\frac{(R_i - R_{i'})(R_i - k)}{(R_{i'} + 1)k} > 0$ with multiplicity $M_i$ (for $i = 1, i' = 2$, $(R_1 - R_2)(R_1 - k) < 0$ and $(R_2 + 1)k < 0$; for $i = 2, i' = 1$, both numerator and denominator are positive). Thus $F$ is symmetric, positive semidefinite, and has rank $M_i > 0$.

Now expand $(A - R_{i'} I)(A - k I) = A^2 - (R_{i'} + k)A + R_{i'} k I$ inside $F$ and substitute $A^2 = k I + \lambda A + \mu(J - I - A)$. Collecting terms expresses $F$ as

$$F = I + \alpha A + \beta(J - I - A),$$

where $\alpha = \frac{\lambda - R_{i'} - k}{(R_{i'} + 1)k}$ and $\beta = \frac{\mu}{(R_{i'} + 1)k}$. Because $F$ is symmetric, positive semidefinite, and of rank $M_i$, we can realize $F = \operatorname{Gr}(\bar{w}_1, \bar{w}_2, \dots, \bar{w}_v)$ for $v$ vectors in $\mathbb{R}^v$ that span an $M_i$-dimensional subspace $W \subseteq \mathbb{R}^v$.

Read what $F = I + \alpha A + \beta(J - I - A)$ tells us about those $v$ vectors $\bar{w}_1, \dots, \bar{w}_v$. Every diagonal entry of $F$ is $1$, so $(\bar{w}_j, \bar{w}_j) = 1$: all $v$ vectors have norm $1$ and lie on the unit sphere $\Omega$ of $W$. Whenever $d(p_{j_1}, p_{j_2}) = 1$, their dot product (the cosine of the angle between them) is $(\bar{w}_{j_1}, \bar{w}_{j_2}) = \alpha$; whenever $d(p_{j_1}, p_{j_2}) = 2$, their dot product is $(\bar{w}_{j_1}, \bar{w}_{j_2}) = \beta$.

Are all $v$ unit vectors $\bar{w}_1, \dots, \bar{w}_v$ distinct? Two unit vectors are equal if and only if their dot product is $1$. First, if $\beta$ were $1$, solving $\frac{\mu}{(R_{i'} + 1)k} = 1$ would give $R_{i'} = \frac{\mu}{k} - 1 \in [-1, 0]$, impossible because $\Gamma$ is primitive ($R_1 > 0$ and $R_2 < -1$). Second, if $\alpha$ were $1$, then every pair of adjacent vertices would have $\bar{w}_{j_1} = \bar{w}_{j_2}$; because $\Gamma$ is connected, walking along paths would force all $v$ vectors $\bar{w}_j$ to be equal, which would make $(\bar{w}_{j_1}, \bar{w}_{j_2}) = 1$ at distance $2$ as well, contradicting $\beta \neq 1$. So $\alpha \neq 1$ and $\beta \neq 1$, and all $v$ vectors $\bar{w}_1, \dots, \bar{w}_v$ on $\Omega$ are mutually distinct.

To bound $v$, work in the real vector space $V_{\Omega}$ of all functions from $\Omega$ to $\mathbb{R}$. Fix an orthonormal basis of the $M_i$-dimensional space $W$, so each $\bar{x} \in W$ has coordinates $(X_1, \dots, X_{M_i})$, with $X_1^2 + \dots + X_{M_i}^2 = 1$ on $\Omega$. Inside $V_{\Omega}$, take the $M_i$ degree-$1$ coordinate functions $f_j(\bar{x}) = X_j$ ($1 \le j \le M_i$) together with the $\frac{M_i(M_i + 1)}{2}$ degree-$2$ functions $f_{j_1, j_2}(\bar{x}) = X_{j_1} X_{j_2}$ ($1 \le j_1 \le j_2 \le M_i$). Those $M_i + \frac{M_i(M_i + 1)}{2} = \frac{M_i(M_i + 3)}{2}$ functions on $\Omega$ are linearly independent: if a linear combination $\sum \lambda_j f_j + \sum \lambda_{j_1, j_2} f_{j_1, j_2}$ vanishes identically on $\Omega$, evaluating at the two unit vectors with $\pm 1$ in coordinate $j$ and $0$ elsewhere gives $\lambda_j + \lambda_{j, j} = -\lambda_j + \lambda_{j, j} = 0$ (so $\lambda_j = \lambda_{j, j} = 0$), and evaluating at the unit vector with $\frac{\sqrt{2}}{2}$ in coordinates $j_1, j_2$ and $0$ elsewhere then gives $\lambda_{j_1, j_2} = 0$ for all $j_1 < j_2$. Thus they span a subspace $V'$ of $V_{\Omega}$ of dimension $\frac{1}{2}M_i(M_i + 3)$.

Now attach to each of our $v$ unit vectors $\bar{w}_j$ ($1 \le j \le v$) the function $f_{\bar{w}_j} : \Omega \to \mathbb{R}$ defined by

$$f_{\bar{w}_j}(\bar{x}) = \frac{\bigl[(\bar{w}_j, \bar{x}) - \alpha\bigr]\bigl[(\bar{w}_j, \bar{x}) - \beta\bigr]}{(1 - \alpha)(1 - \beta)}.$$

Notice that $f_{\bar{w}_j}(\bar{w}_j) = 1$, while for every $j' \neq j$ the dot product $(\bar{w}_j, \bar{w}_{j'})$ is either $\alpha$ or $\beta$, giving $f_{\bar{w}_j}(\bar{w}_{j'}) = 0$. That makes the $v$ functions $f_{\bar{w}_1}, \dots, f_{\bar{w}_v}$ linearly independent: if $\sum_{j=1}^v \lambda_j f_{\bar{w}_j} = 0$ on $\Omega$, plugging in $\bar{x} = \bar{w}_{j'}$ leaves $0 = \lambda_{j'}$ for each $j' \in \{1, \dots, v\}$. Meanwhile, expanding the numerator of $f_{\bar{w}_j}(\bar{x})$ in $(X_1, \dots, X_{M_i})$ produces degree-$2$ terms, degree-$1$ terms, and a constant term $\frac{\alpha\beta}{(1 - \alpha)(1 - \beta)}$, which on $\Omega$ can be rewritten as $\frac{\alpha\beta}{(1 - \alpha)(1 - \beta)}(X_1^2 + \dots + X_{M_i}^2)$ without needing a separate constant function. Hence all $v$ linearly independent functions $f_{\bar{w}_1}, \dots, f_{\bar{w}_v}$ belong to the $\frac{1}{2}M_i(M_i + 3)$-dimensional space $V'$, forcing $v \le \frac{1}{2}M_i(M_i + 3)$.

(To see why primitivity was required in the theorem, check the imprimitive octahedron graph $T(4) \cong K_{2, 2, 2} = \mathrm{SRG}(6, 4, 2, 4)$: here $R_1 = 0$ has $M_1 = 3$ and $R_2 = -2$ has $M_2 = 2$, where $\frac{1}{2}M_2(M_2 + 3) = 5 < 6 = v$. The proof breaks down at $i = 2, i' = 1$ because $\beta = \frac{4}{(0 + 1)4} = 1$, collapsing each opposite nonadjacent pair onto the same unit vector.)

**Worked example: ruling out fake SRG parameters.** Test two plausible parameter quadruples $(v, k, \lambda, \mu)$ against our eigenvalue tests.

First try $(17, 4, 0, 1)$. Double counting passes: $k(k - \lambda - 1) = 4(3) = 12$ matches $(v - k - 1)\mu = 12(1) = 12$. Is it a conference graph? No, $4\mu + 1 = 5 \neq 17$, so any such graph would need integer eigenvalues. Yet the discriminant is $D = (0 - 1)^2 + 4(4 - 1) = 13$, which is not a square ($M_1 = \frac{1}{2}(16 + \frac{8}{\sqrt{13}}) \notin \mathbb{N}$), ruling out $\mathrm{SRG}(17, 4, 0, 1)$ right away.

Second try $(28, 9, 0, 4)$. Double counting passes: $9(8) = 72 = 18(4)$. The discriminant is $D = (0 - 4)^2 + 4(9 - 4) = 36 = 6^2$, giving integer eigenvalues $R_1 = \frac{-4 + 6}{2} = 1$ and $R_2 = \frac{-4 - 6}{2} = -5$. Their multiplicities are

$$M_{1, 2} = \frac{1}{2}\left(27 \pm \frac{27(4 - 0) - 18}{6}\right) = \frac{27 \pm 15}{2},$$

so $M_1 = 21$ and $M_2 = 6$, both clean positive integers. Every basic integrality check passes. Now test the absolute bound: since $0 < 4 < 9$, any $\mathrm{SRG}(28, 9, 0, 4)$ would be primitive, yet at $M_2 = 6$ we get $\frac{1}{2}M_2(M_2 + 3) = \frac{1}{2}(6)(9) = 27 < 28 = v$. Twenty-eight distinct two-angle unit vectors cannot fit on the unit sphere in $\mathbb{R}^6$, so no $\mathrm{SRG}(28, 9, 0, 4)$ exists.

#### The three-eigenvalue converse and the Bose-Mesner algebra

Why does having only two other distinct eigenvalues aside from the valency force an SRG? Because $\Gamma$ is connected, the eigenvalue $k$ has multiplicity $1$ and its eigenspace is spanned by $\mathbf{j}$. So every vector in $\mathbb{R}^v$ can be written as a sum of a component along $\mathbf{j}$ and eigenvectors from the $R_1$ and $R_2$ eigenspaces.

Look at the matrix operator $(A - R_1 I)(A - R_2 I)$. If we apply it to any eigenvector in the $R_1$-eigenspace or $R_2$-eigenspace, it kills that vector (sends it to $0$). But so does the matrix $J$, because $\mathbf{j}^T x = 0$ for every eigenvector $x$ of $R_1$ or $R_2$, so every row of $J$ dotted with $x$ is $0$, so $Jx = 0$.

Now apply $(A - R_1 I)(A - R_2 I)$ to $\mathbf{j}$: since $A\mathbf{j} = k\mathbf{j}$, we get $(k - R_1)(k - R_2)\mathbf{j}$. Similarly, $J\mathbf{j} = v\mathbf{j}$.

Because the matrix $(A - R_1 I)(A - R_2 I)$ and the matrix $\frac{(k - R_1)(k - R_2)}{v} J$ have the exact same action on $\mathbf{j}$ and the exact same action ($0$) on all eigenvectors orthogonal to $\mathbf{j}$, they must be the exact same matrix:

$$(A - R_1 I)(A - R_2 I) = \frac{(k - R_1)(k - R_2)}{v} J$$

Expanding the left-hand side gives:

$$A^2 - (R_1 + R_2)A + R_1 R_2 I = \mu J$$

where $\mu = \frac{(k - R_1)(k - R_2)}{v}$. Reading this matrix equation entry by entry is the definition of an SRG: for every adjacent pair ($A_{ij} = 1$, $I_{ij} = 0$, $J_{ij} = 1$), $(A^2)_{ij}$ must equal the constant $\lambda = \mu + R_1 + R_2$, and for every nonadjacent pair ($A_{ij} = 0$, $I_{ij} = 0$, $J_{ij} = 1$), $(A^2)_{ij}$ must equal the constant $\mu$. That is why a connected regular graph is an SRG if and only if it has 3 distinct eigenvalues.

Moreover, if there were more than two non-valency eigenvalues, we would have applied $(A - R_1 I)(A - R_2 I) \cdots (A - R_n I)$ to $\mathbf{j}$ and ended up with a polynomial of degree $n$ in $A$, whose entries count walks of length up to $n$ between vertices. In algebraic graph theory, this polynomial is called the Hoffman polynomial of the graph. In an SRG, $n = 2$.

Thus, having three distinct eigenvalues is not only a consequence of being a connected strongly regular graph; among connected regular graphs, it characterizes strong regularity completely.

The quadratic relation on $A$ also builds a compact matrix algebra attached to any connected $\mathrm{SRG}(v, k, \lambda, \mu)$. Inside the $v^2$-dimensional real vector space $\mathcal{M}$ of all $v \times v$ real matrices, the identity $A^2 = k I + \lambda A + \mu(J - I - A)$ with $\mu \neq 0$ (and the fact that $I$, $A$, and $J - I - A$ have $1$'s in disjoint positions) implies that $I, A, A^2$ are linearly independent and span a $3$-dimensional subspace $\mathcal{A} = \langle I, A, A^2 \rangle$ containing $J$. Multiplying by $A$ again gives $A^3 = k A + \lambda A^2 + \mu(J A - A - A^2) = k A + \lambda A^2 + \mu(k J - A - A^2) \in \langle I, A, A^2 \rangle$, and by induction $A^i \in \langle I, A, A^2 \rangle$ for every $i \in \mathbb{N}$. So the product $B_1 B_2$ of any two matrices in $\langle I, A, A^2 \rangle$ stays inside $\langle I, A, A^2 \rangle$. Equipped with ordinary matrix multiplication, this $3$-dimensional vector space $\mathcal{A} = \langle I, A, A^2 \rangle$ is called the **Bose-Mesner algebra** of the strongly regular graph $\Gamma$.

#### What can the eigenvalues tell us?

First let's look at what the eigenvector represents. Suppose we have a graph with $v$ vertices. In algebra, how do we represent a subset of vertices $S$ (like a line, a cluster, or a half of the graph)? We represent it by its indicator vector (or characteristic vector) $x \in \mathbb{R}^v$: we put a $1$ at index $i$ if vertex $i$ is in our subset $S$, and a $0$ if it is not.

Now, what happens when we multiply the adjacency matrix $A$ by that indicator vector $x$? Because $A_{ij} = 1$ only when $j$ is a neighbor of $i$, and $x_j = 1$ only when $j$ is in the subset $S$, the number $(Ax)_i$ literally counts how many neighbors vertex $i$ has inside the subset $S$.

So to start with, if we use $\mathbf{j}$, it means our subset is every vertex. The valency $k$ is the number of neighbours in the entire set of vertices.

If we pick a subset of vertices $S$ and create its indicator vector $u$ (putting $1$ for vertices in $S$, and $0$ for vertices outside $S$), for $u$ to be an eigenvector ($Au = \theta u$), two things would have to happen. For every vertex $i$ inside $S$ (where $u_i = 1$), $(Au)_i$ must equal $\theta \cdot 1 = \theta$. That means every vertex in $S$ has $\theta$ neighbors in $S$.

For every vertex $i$ outside $S$ (where $u_i = 0$), $(Au)_i$ must equal $\theta \cdot 0 = 0$. That means every vertex outside $S$ has $0$ neighbors in $S$.

If vertices outside $S$ have $0$ neighbors inside $S$, then $S$ is completely disconnected from the rest of the graph. In a connected graph, no proper subset $S$ has $0$ connections to the outside. Therefore, in a connected graph, a $0$-$1$ indicator vector $u$ of a smaller subset can never be an eigenvector on its own, because vertices outside $S$ still have some positive number of neighbors inside $S$ (so $(Au)_i$ is not $0$ outside $S$).

How do we fix that non-zero spillover outside $S$ so that we get a valid eigenvector? We subtract a fraction of the all-ones vector $\mathbf{j}$. Watch how this works step by step on a concrete geometric object inside an SRG:

Suppose $S$ is a special substructure in our graph (say, a line, a clique, or an independent set) where every vertex inside $S$ has $a$ neighbors inside $S$. Every vertex outside $S$ has $b$ neighbors inside $S$ (with $b > 0$ since the graph is connected).

Write down what $Au$ gives for the $0$-$1$ indicator vector $u$ of $S$. If vertex $i$ is in $S$ ($u_i = 1$): $(Au)_i = a$. If vertex $i$ is outside $S$ ($u_i = 0$): $(Au)_i = b$.

Notice that across the whole graph, the output $(Au)_i$ only takes two values: $a$ (when $u_i = 1$) and $b$ (when $u_i = 0$). We can write that as a single linear equation valid for every vertex $i$:

$$(Au)_i = (a - b)u_i + b$$

Or in vector form, since $\mathbf{j}$ has $1$ at every vertex:

$$Au = (a - b)u + b\mathbf{j}$$

Look at that equation: $u$ fails to be an eigenvector only because of the extra constant term $+ b\mathbf{j}$ (the $b$ neighbors that outside vertices have in $S$).

Because we already know $A\mathbf{j} = k\mathbf{j}$, we can cancel out that extra $+b\mathbf{j}$ term by shifting $u$ by a constant multiple of $\mathbf{j}$. Specifically, set:

$$x = u - c\mathbf{j}$$

where $c = \frac{b}{k - (a - b)}$ is just a constant number. Now multiply $x$ by $A$:

$$Ax = Au - c A\mathbf{j} = (a - b)u + b\mathbf{j} - ck\mathbf{j} = (a - b)\left(u - c\mathbf{j}\right) = (a - b)x$$

Look at what we just found. The shifted indicator vector $x = u - c\mathbf{j}$ is a genuine eigenvector of $A$. Its eigenvalue is $\theta = a - b$: the number of neighbors a vertex in $S$ has inside $S$, minus the number of neighbors a vertex outside $S$ has inside $S$.

And why does the eigenvector $x = u - c\mathbf{j}$ have negative numbers in it? Because we started with the $0$-$1$ indicator vector $u$ (which has $1$ on $S$ and $0$ outside $S$) and subtracted the constant $c$ from every vertex (giving $1 - c$ on $S$ and $-c$ outside $S$) so that the vector is orthogonal to $\mathbf{j}$ and the outside spillover cancels out.

So whenever a subset $S$ has these two constant counts $a$ and $b$, its indicator vector $u$, shifted by the constant $-c\mathbf{j}$ so that its entries sum to zero, is an eigenvector orthogonal to $\mathbf{j}$, and its eigenvalue $\theta = a - b$ is the internal neighbor count $a$ minus the external neighbor count $b$. The converse fails: most eigenvectors do not come from a subset at all. In the pentagon $C_5$, for instance, $a - b$ is always an integer while $R_1$ and $R_2$ are irrational, so no subset of $C_5$ gives an eigenvector orthogonal to $\mathbf{j}$.

Using this exact formula for the eigenvalue $\theta = a - b$ (internal neighbours $a$ minus external neighbours $b$), we can see directly what the two non-valency eigenvalues $R_1 > 0$ and $R_2 < 0$ of an $\mathrm{SRG}(v, k, \lambda, \mu)$ tell us about the subsets inside the graph.

What the positive eigenvalue $R_1 > 0$ tells us ($a > b$): Since $\theta = a - b = R_1 > 0$, we have $a > b$. That means a vertex inside $S$ has more neighbours inside $S$ than a vertex outside $S$ has inside $S$. In other words, $R_1$ governs tightly connected, self-contained clusters (such as cliques or geometric lines).

For example, suppose $S$ is a clique (a line of the geometry, where every pair of points in $S$ is connected) of size $\vert{}S\vert{} = s + 1$, and suppose every point outside the line is connected to $b = 1$ point on the line (just like in a generalized quadrangle).

Every vertex in $S$ is connected to all other $s$ vertices in $S$, so $a = s$. Every vertex outside $S$ is connected to $b = 1$ vertex in $S$. Then $\theta = a - b = s - 1 > 0$, which must equal the positive eigenvalue $R_1$. Thus, $R_1 = s - 1$, telling us the exact size of the lines ($s + 1 = R_1 + 2$) inside the geometry.

What the negative eigenvalue $R_2 < 0$ tells us ($a < b$): Since $\theta = a - b = R_2 < 0$, we have $a < b$. That means a vertex inside $S$ has fewer neighbours inside $S$ than a vertex outside $S$ has. The extreme case of this is when $S$ is an independent set (an ovoid or coclique: a set of vertices with zero edges between them). Because no two vertices in $S$ are connected, every vertex in $S$ has $a = 0$ neighbours inside $S$. Every vertex outside $S$ has $b$ neighbours inside $S$. Plugging $a = 0$ into our eigenvalue rule $\theta = a - b$ immediately forces:

$$R_2 = 0 - b = -b \implies b = -R_2$$

Look at how concrete that is: if an SRG contains a regular independent set $S$, the negative eigenvalue $R_2$ (with its minus sign dropped) literally counts how many neighbours every outside vertex has inside $S$ ($b = -R_2$).

Furthermore, we can use $b = -R_2$ to count the exact number of vertices in $S$ (which is Hoffman's bound):

Each of the $\vert{}S\vert{}$ vertices inside $S$ has degree $k$, and since $a = 0$, all $k$ of its edges go out to the $v - \vert{}S\vert{}$ vertices outside $S$. That gives $\vert{}S\vert{} \cdot k$ edges between $S$ and the outside.

Meanwhile, each of the $v - \vert{}S\vert{}$ vertices outside $S$ sends $b = -R_2$ edges into $S$. That gives $(v - \vert{}S\vert{})(-R_2)$ edges between $S$ and the outside. Equating the two counts of edges between $S$ and the outside gives:

$$\vert{}S\vert{} \cdot k = (v - \vert{}S\vert{})(-R_2) \implies \vert{}S\vert{} = \frac{v(-R_2)}{k - R_2}$$

**Concrete check on the $3 \times 3$ grid $L_2(3)$**

Take the $3 \times 3$ square lattice graph $L_2(3)$, which is an $\mathrm{SRG}(9, 4, 1, 2)$. Using our quadratic formula, its non-valency eigenvalues are $R_1 = 1$ and $R_2 = -2$. What do $R_1 = 1$ and $R_2 = -2$ tell us about subsets $S$ of the $3 \times 3$ grid?

Reading $R_1 = 1$: Let $S$ be a single row of $3$ points. Inside that row, every point is connected to the other $a = 2$ points of the row. Outside that row, every point shares a column with $b = 1$ point of that row. So $\theta = a - b = 2 - 1 = 1 = R_1$. The positive eigenvalue $R_1 = 1$ detects the rows and columns of the grid.

Reading $R_2 = -2$: Let $S$ be $3$ points with no two in the same row or column (like the $3$ points along the main diagonal of the $3 \times 3$ grid, or the transversal in Figure 5(b)). No two points in $S$ share a row or column, so $a = 0$. Every point outside $S$ shares its row with $1$ point of $S$ and its column with $1$ point of $S$, so it has $b = 2$ neighbours in $S$. Thus $\theta = a - b = 0 - 2 = -2 = R_2$, and the size of $S$ is $\frac{9(2)}{4 - (-2)} = 3$. The negative eigenvalue $R_2 = -2$ detects the independent transversal sets of the grid, and $-R_2 = 2$ counts how many diagonal points each off-diagonal point sees.

**An intuitive picture of SRGs.** The two imprimitive extremes of SRGs (which we looked at in the beginning of the SRG section) embody pure $R_1$ behavior and pure $R_2$ behavior and are a good way to think about the spectrum of an SRG.

The disjoint union of cliques $mK_c$ are pure "connected within" sets of points. $\mu = 0$, $R_1 = k = c - 1$, and $R_2 = -1$. Each clique is completely sealed off ($a = k, b = 0$).

The other extreme is the complete multipartite graph $K_{c, c, \dots, c}$. It is a pure "connected outside" set. $\mu = k$, $R_1 = 0$, and $R_2 = -c$. Each independent group has zero internal edges ($a = 0$) and sends all its edges outside ($b = c = -R_2$).

Every primitive SRG lives in the tension between those two extremes: its $R_1$-eigenspace pulls subsets toward acting like the cliques of $mK_c$ (tight sets, lines, subgeometries), while its $R_2$-eigenspace pulls subsets toward acting like the independent parts of $K_{c, \dots, c}$ (ovoids, cocliques, bipartite-like splits).

The $R_1$-subsets and $R_2$-subsets (like ovoids/cocliques, where $a < b$) sit transversely (orthogonally) across each other like warp and weft threads on a loom. For example, take a subset of vertices $S$, but switch from the graph $\Gamma$ to its complement graph $\overline{\Gamma}$ (replacing $A$ with $\overline{A} = J - I - A$), then an eigenvector $x$ of $A$ with eigenvalue $\theta$ satisfies:

$$\overline{A}x = (J - I - A)x = 0 - x - \theta x = (-1 - \theta)x$$

Since $R_1 > 0$ and $R_2 < 0$, this formula swaps the two eigenspaces directly:

$$\overline{R_1} = -1 - R_2, \qquad \overline{R_2} = -1 - R_1$$

A clique/line in $\Gamma$ (which lives in the $R_1 > 0$ eigenspace of $\Gamma$) literally becomes an independent set/coclique in $\overline{\Gamma}$ (which lives in the $\overline{R_2} < 0$ eigenspace of $\overline{\Gamma}$).

Look at our $3 \times 3$ grid $L_2(3)$ in the example. An $R_1$-subset ($a - b = 1 > 0$) is a horizontal row of $3$ points (all connected to each other: $a = 2, b = 1$).

An $R_2$-subset ($a - b = -2 < 0$) is a diagonal transversal of $3$ points (none connected to each other: $a = 0, b = 2$). Because the row eigenvector lies in the $R_1$-eigenspace and the diagonal eigenvector lies in the $R_2$-eigenspace, their shifted indicator vectors are strictly orthogonal ($x_{\text{row}}^T x_{\text{diag}} = 0$).

Unpacking that dot product $x_1^T x_2 = 0$ reveals a remarkable geometric fact: any $R_1$-subset $S_1$ and any $R_2$-subset $S_2$ in an SRG must intersect in the exact average number of vertices $\frac{\vert{}S_1\vert{}\cdot \vert{}S_2\vert{}}{v}$. In $L_2(3)$, every row of $3$ points and every diagonal transversal of $3$ points must intersect in $\frac{3 \times 3}{9} = 1$ point.

Note that a subset and its complement do not lie in different $R$-subsets because they both share the same eigenvalue. Let $S$ be a subset and its outside/complement be $S' = V \setminus S$. Suppose every vertex $x \in S$ has $a$ neighbours inside $S$ (and therefore $k - a$ neighbours outside in $S'$), and every vertex $y \in S'$ has $b$ neighbours inside $S$ (and therefore $k - b$ neighbours inside its own set $S'$).

Now compute the "internal minus external" value $a' - b'$ from the perspective of $y \in S'$. How many neighbours does $y \in S'$ have inside its own set $S'$? Since $y$ has $k$ neighbours in total and $b$ of them go into $S$, it has $a' = k - b$ neighbours inside $S'$. How many neighbours does a vertex $x \notin S'$ (meaning $x \in S$) have inside $S'$? Since $x$ has $k$ neighbours in total and $a$ of them stay inside $S$, it sends $b' = k - a$ edges into $S'$.

Subtract them to find the eigenvalue $\theta'$ of the outside set $S'$:

$$\theta' = a' - b' = (k - b) - (k - a) = a - b = \theta$$

They are identical. We can also see this immediately from the shifted indicator vectors: the indicator vector of $S'$ is $\mathbf{j} - u$, so shifting it orthogonal to $\mathbf{j}$ just gives $-x = -(u - c\mathbf{j})$, which is the exact same eigenvector (just flipped in sign) with the exact same eigenvalue $\theta = a - b$.

Why doesn't the sign of $a - b$ flip when going over to the complement? Because "inward-looking" compares two vertices, not two sets. $S$ is inward-looking when a vertex inside $S$ sees more of $S$ than a vertex outside does, $a > b$. For $S'$ the same comparison reads: a vertex $y \in S'$ sees $k - b$ points of $S'$, while a vertex $x \in S$ sees $k - a$ points of $S'$. Since every vertex has $k$ neighbours in all, $k - b > k - a$ says exactly the same as $a > b$, so when $S$ is "inward-looking", its complement $S'$ is too. (Counting the edges between $S$ and $S'$ gives $\vert{}S\vert{}(k - a) = \vert{}S'\vert{}\, b$, which ties the two counts together but does not by itself make $b$ small: that also depends on how big $S$ and $S'$ are.)

**And what about multiplicity?** The multiplicity of an eigenvalue is the dimension of its eigenspace, so it is an upper bound on the number of linearly independent shifted indicator vectors $x = u - c\mathbf{j}$ that can exist for those structures (and not the raw total count of the structures). The bound need not be reached: in $C_5$ both multiplicities are $2$, yet no subset gives an eigenvector at all.

Because the multiplicity $M_1$ (or $M_2$) is the dimension of the eigenspace, and every shifted indicator vector $x = u - c\mathbf{j}$ of a valid structure lives inside that eigenspace, the structures themselves are often linearly dependent on one another.

Look at our $3 \times 3$ grid $L_2(3)$ where $v = 9$, $k = 4$, $R_1 = 1$, and $R_2 = -2$. Since $M_1 + M_2 = v - 1 = 8$ and $4 + 1 M_1 + (-2) M_2 = 0$, the multiplicities are $M_1 = 4$ and $M_2 = 4$.

Compare the multiplicity $M_1 = 4$ with the actual number of lines (rows and columns) in the $3 \times 3$ grid. There are $3$ horizontal rows and $3$ vertical columns, giving $6$ lines in total, even though $M_1 = 4$. Why is $M_1 = 4$ instead of $6$? Let $u_{r_1}, u_{r_2}, u_{r_3}$ be the $0$-$1$ indicator vectors of the $3$ rows, and $u_{c_1}, u_{c_2}, u_{c_3}$ be the indicator vectors of the $3$ columns. Since the $3$ rows partition the entire $3 \times 3$ grid, adding their indicator vectors gives the all-ones vector:

$$u_{r_1} + u_{r_2} + u_{r_3} = \mathbf{j}$$

When we shift them by $-\frac{1}{3}\mathbf{j}$ to get their eigenvectors $x_{r_1}, x_{r_2}, x_{r_3}$ in the $R_1$-eigenspace, those three eigenvectors add up to the zero vector:

$$x_{r_1} + x_{r_2} + x_{r_3} = 0 \implies x_{r_3} = -x_{r_1} - x_{r_2}$$

So the $3$ row eigenvectors only span a $2$-dimensional subspace (once you know Row $1$ and Row $2$, Row $3$ is forced).

By the exact same logic, the $3$ columns partition the grid ($u_{c_1} + u_{c_2} + u_{c_3} = \mathbf{j}$), so the $3$ column eigenvectors $x_{c_1}, x_{c_2}, x_{c_3}$ also sum to $0$ and span a $2$-dimensional subspace.

Together, the $2$ independent row directions plus the $2$ independent column directions span the entire $2 + 2 = 4$-dimensional eigenspace ($M_1 = 4$).

Now look at the other eigenspace on $L_2(3)$, where $R_2 = -2$ and $M_2 = 4$. The independent sets of size $3$ (picking $3$ points with no two in the same row or column) correspond to the $3! = 6$ permutation matrices of size $3 \times 3$. There are $6$ such independent sets in the grid, yet their shifted indicator vectors all live inside the $4$-dimensional $R_2$-eigenspace ($M_2 = 4$) because of linear dependencies among the $6$ permutations.

In general, the multiplicity $M_i$ acts as a hard algebraic ceiling (a rank bound) on the geometry: the shifted indicator vectors of the structures of one type span a subspace of the eigenspace, so at most $M_i$ of them are linearly independent, although their span can be smaller than the whole eigenspace. If you have a collection of $m$ structures whose shifted indicator vectors are mutually orthogonal (or linearly independent), then $m$ can never exceed the multiplicity: $m \le M_i$. For instance, if $m$ cliques partition the vertex set and each of them is a regular set with eigenvalue $R_1$ (every outside vertex has the same number of neighbours in it, as for the lines of a spread in a generalized quadrangle), their shifted indicator vectors span an $(m - 1)$-dimensional subspace of the $R_1$-eigenspace, forcing $m - 1 \le M_1$.

Everything we derived about the shifted indicator vector $x = u - c\mathbf{j}$, the eigenvalue $\theta = a - b$, and the dimension bound from the multiplicity holds for any $k$-regular graph and not just an SRG.

So in any $k$-regular graph:

If you find a regular subset $S$ where every vertex inside $S$ has $a$ neighbours in $S$ and every vertex outside $S$ has $b$ neighbours in $S$ (what Delsarte called a **completely regular code** of covering radius $1$, or an **intriguing set** / $2$-cell equitable partition), then $x = u - c\mathbf{j}$ is guaranteed to be an eigenvector of $A$ with eigenvalue $\theta = a - b$.

For an independent set ($a = 0$) where every outside vertex has $b$ neighbours in $S$, $\theta = -b$ must be one of the negative eigenvalues of the graph, and Hoffman's bound $\vert{}S\vert{} \le \frac{v(-\theta_{\min})}{k - \theta_{\min}}$ holds for every $k$-regular graph (where $\theta_{\min}$ is the smallest eigenvalue of $A$), with equality if and only if every vertex outside $S$ has exactly $b = -\theta_{\min}$ neighbours in $S$.

The multiplicity of the eigenvalue $\theta = a - b$ is still an upper bound on the number of linearly independent shifted indicator vectors of such subsets.

What makes Strongly Regular Graphs (and more generally, distance-regular graphs) special compared to an arbitrary regular graph is the *concentration of the spectrum*:

A generic $k$-regular graph on $v$ vertices might have $v$ different eigenvalues, each with multiplicity $1$. Because the eigenspaces are tiny ($1$-dimensional) and the eigenvalues are usually messy irrational roots of a degree-$v$ polynomial, the graph rarely admits clean integer solutions to $\theta = a - b$, and even if one exists, a $1$-dimensional eigenspace can only hold a single subset $S$ and its complement.

An SRG forces all $v - 1$ non-valency dimensions to collapse into just two huge eigenspaces ($M_1$ and $M_2$) with clean algebraic eigenvalues $R_1$ and $R_2$. That collapse gives the eigenspaces massive dimension (room to pack whole families of lines, grids, ovoids, and spreads) and restricts $\theta = a - b$ to just two possible target values, $R_1$ or $R_2$.

### Distance-regular graphs

A connected strongly regular graph has diameter $2$, and standing at any vertex $x$ splits the graph into $\{x\}$, $\Gamma_1(x)$, and $\Gamma_2(x)$ with uniform edge counts between layers. Norman Biggs extended this layer-by-layer symmetry to graphs of any diameter $d \ge 2$.

#### Distance layers, intersection numbers, and sphere sizes

Pick any base vertex $x$ in a connected finite graph $\Gamma$ of diameter $d \ge 2$, and arrange the vertices of $\Gamma$ into the distance layers $\Gamma_0(x), \Gamma_1(x), \dots, \Gamma_d(x)$ radiating out from $x$. Now stand at some vertex $y$ in layer $i$ (so $d(x, y) = i$). Every edge leaving $y$ must either step one layer closer to $x$ (into $\Gamma_{i-1}(x)$), stay inside the same layer $\Gamma_i(x)$, or step one layer further away from $x$ (into $\Gamma_{i+1}(x)$).

Recall from [the adjacency matrix and its eigenvalues](#the-adjacency-matrix-and-its-eigenvalues) that $\Gamma$ is distance-regular when these three neighbour counts depend only on the distance $i$, and not on which pair of vertices $x$ and $y$ at distance $i$ we chose. The constant counts $a_i, b_i, c_i$ ($i \in \{0, 1, \dots, d\}$) are called the **intersection numbers** of $\Gamma$: $y$ has $c_i$ neighbours at distance $i - 1$ from $x$, $a_i$ at distance $i$ and $b_i$ at distance $i + 1$. Every vertex has valency $k = a_i + b_i + c_i$ for every $i$, with $c_0 = a_0 = 0$, $b_0 = k$, $c_1 = 1$ and $b_d = 0$, and we put $a_j = b_j = c_j = 0$ for every integer $j \notin \{0, 1, \dots, d\}$.

At diameter $d = 2$, the distance-regular graphs are precisely the connected strongly regular graphs, with $(c_0, a_0, b_0) = (0, 0, k)$, $(c_1, a_1, b_1) = (1, \lambda, k - \lambda - 1)$, and $(c_2, a_2, b_2) = (\mu, k - \mu, 0)$.

The intersection numbers also fix the size of every distance sphere $\Gamma_i(x)$. Define $k_0 = 1$ and $k_{i+1} = \frac{k_i b_i}{c_{i+1}}$ for $i \in \{0, 1, \dots, d - 1\}$. Counting the edges between $\Gamma_i(x)$ and $\Gamma_{i+1}(x)$ from both sides gives $\lvert \Gamma_i(x) \rvert b_i = \lvert \Gamma_{i+1}(x) \rvert c_{i+1}$; starting from $\lvert \Gamma_0(x) \rvert = 1 = k_0$, induction gives $\lvert \Gamma_i(x) \rvert = k_i$ for every vertex $x$ and every $i \in \{0, 1, \dots, d\}$ (and $v = k_0 + k_1 + \dots + k_d$).

![The 3-cube Q3 in distance layers, and the two bases of its Bose-Mesner algebra](figures/maths4_drg_cube_bose_mesner.png)

*Figure 12. (a) The $3$-cube $Q_3$ drawn in the distance layers $\Gamma_0, \Gamma_1, \Gamma_2, \Gamma_3$ of the vertex $000$, with sphere sizes $k_i = 1, 3, 3, 1$ and intersection numbers $(b_0, b_1, b_2) = (3, 2, 1)$, $(c_1, c_2, c_3) = (1, 2, 3)$, $a_i = 0$. (b) The two bases of its Bose-Mesner algebra: each cell of the left grid names the distance matrix $A_i$ that has a $1$ there, and the right grid is the idempotent $8E_1$ for $\theta_1 = 1$, with entries $3, 1, -1, -3$ at distances $0, 1, 2, 3$.*

#### Distance matrices, distance polynomials, and the Bose-Mesner algebra

Let $\Gamma$ be a distance-regular graph of diameter $d \ge 2$ on $v$ vertices ordered as $(p_1, \dots, p_v)$, with adjacency matrix $A$. For every integer $i \in \mathbb{Z}$, define the $v \times v$ **distance-$i$ matrix** $A_i$ (for $j, k \in \{1, \dots, v\}$) by setting $(A_i)_{jk} = 1$ if $d(p_j, p_k) = i$ and $(A_i)_{jk} = 0$ otherwise. Then $A_0 = I$, $A_1 = A$, $A_i = 0$ for $i \notin \{0, 1, \dots, d\}$, and $A_0 + A_1 + \dots + A_d = J$ because every pair of vertices sits at one unique distance between $0$ and $d$.

**Three-term recurrence for distance matrices.** In a distance-regular graph we can multiply two distance matrices and expand the product as a linear combination of the others:

$$A_i A_j = \sum_{k=0}^d p_{ij}^k A_k$$

Here the coefficient $p_{ij}^k$ is the number of vertices $z$ at distance $i$ from $x$ and distance $j$ from $y$ when $d(x, y) = k$. Distance-regularity is what makes this number depend only on $i$, $j$ and $k$ and not on the pair $x, y$; in a general graph it depends on the pair, and $A_i A_j$ need not be a combination of distance matrices at all. These $p_{ij}^k$ are also called intersection numbers. Because $p_{ij}^k$ counts vertices, it is a nonnegative integer.

When one factor is $A = A_1$, the relation becomes the three-term recurrence, for every $i \in \{0, 1, \dots, d\}$,

$$A A_i = b_{i-1} A_{i-1} + a_i A_i + c_{i+1} A_{i+1}.$$

To see why, compute the $(j, k)$-entry $(A A_i)_{jk} = \sum_{l=1}^v A_{jl} (A_i)_{lk}$, which counts how many neighbours of $p_j$ lie at distance $i$ from $p_k$ (the neighbours are given by $p_l$). Stand at $p_k$ as the base vertex: by the triangle inequality, $p_j$ has $0$ such neighbours unless $d(p_j, p_k) \in \{i - 1, i, i + 1\}$. When $d(p_j, p_k) = i - 1$ (marked by $A_{i-1}$), $p_j$ has $b_{i-1}$ neighbours one step further out at distance $i$ from $p_k$. When $d(p_j, p_k) = i$ (marked by $A_i$), $p_j$ has $a_i$ neighbours at distance $i$ from $p_k$. And when $d(p_j, p_k) = i + 1$ (marked by $A_{i+1}$), $p_j$ has $c_{i+1}$ neighbours one step closer at distance $i$ from $p_k$.

Because $c_{i+1} \ge 1$ for $0 \le i \le d - 1$, we can divide the recurrence by $c_{i+1}$ and solve for $A_{i+1}$ one step at a time as a polynomial in $A$.

We do this inductively step-by-step, with $A_{-1}$ as the zero matrix $0$ (along with $b_{-1} = 0$), $A_{d+1} = 0$ and $c_{d+1} = 0$, $A_0 = I$ (the vertices are their own 0 neighbours) and $A_1 = A$.

Rearrange the three-term recurrence to isolate $A_{i+1}$ on the left-hand side:

$$A_{i+1} = \frac{1}{c_{i+1}} \bigl( A A_i - a_i A_i - b_{i-1} A_{i-1} \bigr)$$

Unrolling this one step at a time shows how each distance matrix $A_m$ becomes a degree-$m$ polynomial $p_m(A)$ in $A$:

**Base case ($i = 0$):** Since $A_{-1} = 0$, $b_{-1} = 0$, $a_0 = 0$, and $c_1 = 1$, the formula at $i = 0$ simply gives:

$$A_1 = \frac{1}{1}(A I - 0 - 0) = A$$

$A_0 = I$ is a polynomial of degree $0$ in $A$, and $A_1 = A$ is a polynomial of degree $1$ in $A$.

**First inductive step ($i = 1 \implies$ solving for $A_2$):** Plug $i = 1$ into the rearranged recurrence (using $A_0 = I$, $A_1 = A$, and $b_0 = k$):

$$A_2 = \frac{1}{c_2} \bigl( A(A) - a_1 A - b_0 I \bigr) = \frac{1}{c_2} \bigl( A^2 - a_1 A - k I \bigr)$$

In an SRG, $a_1 = \lambda$, $c_2 = \mu$, and $A_2 = J - I - A$ marks the vertices at distance $2$. Plugging those in gives $J - I - A = \frac{1}{\mu}(A^2 - \lambda A - kI)$, which is our exact SRG quadratic equation.

Continuing this induction, we will see that we multiply each previous $A_i$ by $A$ up to $i = d - 1$, and so every distance matrix $A_m$ is a polynomial $p_m(A)$ of exact degree $m$ in $A$. These polynomials $p_0, p_1, \dots, p_d$ are called the **distance polynomials** of the distance-regular graph.

**Distance polynomials, minimal polynomial, and eigenvalue count.** Let $\Gamma$ be a distance-regular graph of diameter $d \ge 2$. For each $i \in \{0, 1, \dots, d\}$, there is a unique polynomial $p_i(X) \in \mathbb{R}[X]$ of degree $i$ satisfying $A_i = p_i(A)$, given by $p_0(X) = 1$, $p_1(X) = X$, and for $1 \le i \le d - 1$,

$$p_{i+1}(X) = \frac{1}{c_{i+1}}\Bigl((X - a_i)p_i(X) - b_{i-1} p_{i-1}(X)\Bigr).$$

Summing $J = A_0 + \dots + A_d$ gives a unique degree-$d$ polynomial $p^*(X) = p_0(X) + p_1(X) + \dots + p_d(X)$ with $J = p^*(A)$. Moreover, the [minimal polynomial](#polynomials-in-a-matrix-and-the-minimal-polynomial) of $A$ has degree $d + 1$ and is proportional to both $(X - b_0)p^*(X)$ and $(X - a_d)p_d(X) - b_{d-1} p_{d-1}(X)$. Consequently, $\Gamma$ has precisely $d + 1$ distinct eigenvalues, the largest of which is $b_0$ with multiplicity $1$.

Let us check the degree and uniqueness step in that theorem. The $d + 1$ matrices $A_0, A_1, \dots, A_d$ have $1$'s in nonempty, mutually disjoint positions, so they are linearly independent in the space of all $v \times v$ real matrices. Since each $A_i$ is a degree-$i$ polynomial in $A$, the powers $A^0, A^1, \dots, A^d$ must also be linearly independent, meaning no nonzero polynomial of degree $d$ or less can annihilate $A$. That forces the minimal polynomial of $A$ to have degree at least $d + 1$ (and makes each $p_i(X)$ and $p^*(X)$ unique).

On the other hand, since $\Gamma$ is $b_0$-regular, $AJ = b_0J \implies (A - b_0 I)J = 0$, so $m(X) = (X - b_0)p^*(X)$ has degree $d + 1$ and satisfies $m(A) = 0$; likewise, setting $i = d$ in $A A_i = b_{i-1} A_{i-1} + a_i A_i + c_{i+1} A_{i+1}$ (where $A_{d+1} = 0$) gives $(A - a_d I)A_d - b_{d-1} A_{d-1} = 0$ at degree $d + 1$. Thus the minimal polynomial of $A$ has degree $d + 1$ and is proportional to both expressions. Because $A$ is real and symmetric, the number of distinct eigenvalues of $A$ equals the degree $d + 1$ of its minimal polynomial, and connectedness gives $b_0$ multiplicity $1$.

The $(d + 1)$-dimensional real vector space

$$\mathcal{A} = \langle I, A, A^2, \dots, A^d \rangle = \langle A_0, A_1, \dots, A_d \rangle,$$

together with standard matrix multiplication, is closed under multiplication (and commutative, since every element is a polynomial in $A$). It is called the **Bose-Mesner algebra** of the distance-regular graph $\Gamma$, and both $\{I, A, \dots, A^d\}$ and $\{A_0, A_1, \dots, A_d\}$ are bases of $\mathcal{A}$.

Just as important, $\mathcal{A}$ carries a second multiplication, the [entrywise (Hadamard or Schur) product](#rank-determinants-and-gram-matrices) $(M \circ N)_{jk} = M_{jk} N_{jk}$ of two $v \times v$ matrices $M$ and $N$. Because $A_0, A_1, \dots, A_d$ are $0$-$1$ matrices with disjoint supports, multiplying them entrywise gives

$$A_i \circ A_j = \delta_{ij} A_i$$

for all $i, j \in \{0, 1, \dots, d\}$, where $\delta_{ij}$ is the Kronecker symbol ($1$ if $i = j$ and $0$ if $i \neq j$). Extending by linearity shows that the Bose-Mesner algebra $\mathcal{A}$ is closed under Hadamard multiplication.

#### Normalized polynomials, standard sequences, and Biggs' multiplicity formula

Recall that $k_i = \lvert \Gamma_i(x) \rvert$ satisfies $k_0 = 1$ and $k_{i+1} c_{i+1} = k_i b_i$. For each $i \in \{0, 1, \dots, d\}$, divide $p_i(X)$ by $k_i$ to define the normalized degree-$i$ polynomial

$$u_i(X) = \frac{p_i(X)}{k_i} \in \mathbb{R}[X]$$

(putting $u_i(X) = 0$ for $i \notin \{0, 1, \dots, d\}$). Then $u_0(X) = 1$ and $u_1(X) = \frac{X}{k}$ where $k = b_0$. Substituting $p_i(X) = k_i u_i(X)$ into $c_{i+1} p_{i+1}(X) + (a_i - X)p_i(X) + b_{i-1} p_{i-1}(X) = 0$ and using $k_{i+1} c_{i+1} = k_i b_i$ cancels $k_i$ across all three terms, giving the symmetric recurrence

$$b_i u_{i+1}(X) + (a_i - X)u_i(X) + c_i u_{i-1}(X) = 0$$

for every $i \in \{0, 1, \dots, d - 1\}$ (valid at $i = 0$ as well), while $k_{d-1} b_{d-1} = k_d c_d$ makes the minimal polynomial of $A$ proportional to $(X - a_d)u_d(X) - c_d u_{d-1}(X)$.

Let $\Theta$ be the set of all $d + 1$ distinct eigenvalues of $\Gamma$. For any $\theta \in \Theta$, the $(d + 1)$-tuple $\bigl(u_0(\theta), u_1(\theta), \dots, u_d(\theta)\bigr)$ is called the **standard sequence or cosine sequence** corresponding to $\theta$. Write $f(\theta)$ for the multiplicity of $\theta$ as an eigenvalue of $A$, and build the matrix

$$E(\theta) = \sum_{i=0}^d u_i(\theta) A_i,$$

$E(\theta)$ can never be the zero matrix because $u_0(\theta) = 1$ and $u_0(\theta)A_0 = I$. Since every $A_i$ with $i \neq 0$ has only $0$ along its diagonal, the diagonal from $A_0$ is unaffected by whatever polynomials we build with $A_i$.

Now multiply the equation by $A$. The LHS becomes $AE(\theta)$. On the right, substitute $A A_i = b_{i-1} A_{i-1} + a_i A_i + c_{i+1} A_{i+1}$.

$$A E(\theta) = \sum_{j=0}^d u_j(\theta) b_{j-1} A_{j-1} + \sum_{j=0}^d u_j(\theta) a_j A_j + \sum_{j=0}^d u_j(\theta) c_{j+1} A_{j+1}$$

What is the total coefficient sitting in front of a specific matrix $A_i$? From the first sum $\sum u_j(\theta) b_{j-1} A_{j-1}$, we get an $A_i$ term when $j - 1 = i$ (meaning $j = i + 1$). That contributes $b_i u_{i+1}(\theta) A_i$. From the second sum $\sum u_j(\theta) a_j A_j$, we get an $A_i$ term when $j = i$. That contributes $a_i u_i(\theta) A_i$. From the third sum $\sum u_j(\theta) c_{j+1} A_{j+1}$, we get an $A_i$ term when $j + 1 = i$ (meaning $j = i - 1$). That contributes $c_i u_{i-1}(\theta) A_i$.

Adding those three contributions together, the total coefficient of $A_i$ inside $A E(\theta)$ is: $c_i u_{i-1}(\theta) + a_i u_i(\theta) + b_i u_{i+1}(\theta)$.

Rearranging the recurrence of the polynomials $u_i(x)$ and plugging in $x = \theta$, we have $c_i u_{i-1}(\theta) + a_i u_i(\theta) + b_i u_{i+1}(\theta) = \theta u_i(\theta)$ for $0 \le i \le d - 1$ and so $\theta u_i(\theta)$ becomes the coefficient of $A_i$. For $i = d$ the coefficient of $A_d$ is just $c_d u_{d-1}(\theta) + a_d u_d(\theta)$.

Does $c_d u_{d-1}(\theta) + a_d u_d(\theta) =\theta u_d(\theta)$ as well? Moving everything to one side is equivalent to: $(\theta - a_d) u_d(\theta) - c_d u_{d-1}(\theta) = 0$.

The degree-$(d+1)$ polynomial $P(X) = (X - a_d)u_d(X) - c_d u_{d-1}(X)$ is a constant multiple of the minimal polynomial of $A$ (it is not monic), and its roots are precisely the $d + 1$ eigenvalues of $A$. So yes, the condition holds for the boundary as well.

So we have:

$$A \cdot E(\theta) = \theta \cdot E(\theta)$$

for every $\theta \in \Theta$. And notice what this says geometrically: every column of the matrix $E(\theta)$ is an eigenvector of $A$ with eigenvalue $\theta$. Take any vector $v$, multiply it by $E(\theta)$ to get $w = E(\theta)v$, and then multiply by $A$:

$$Aw = A E(\theta)v = \theta E(\theta)v = \theta w$$

Every vector that comes out of $E(\theta)$ is automatically an eigenvector of $A$ with eigenvalue $\theta$. In fact, $\frac{f(\theta)}{v} E(\theta)$ is the orthogonal projection matrix onto the $\theta$-eigenspace.

Now because $\mathcal{A}$ is commutative, $A$ can slide between any two factors $E(\theta_1)$ and $E(\theta_2)$: whenever $\theta_1 \neq \theta_2$, we get $\theta_1 E(\theta_1) E(\theta_2) = A E(\theta_1) E(\theta_2) = E(\theta_1) A E(\theta_2) = \theta_2 E(\theta_1) E(\theta_2)$, so $E(\theta_1) \cdot E(\theta_2) = 0$.

Taking the trace of $E(\theta)$ in two ways now gives a formula for the multiplicity $f(\theta)$ of each eigenvalue $\theta \in \Theta$ called **Biggs' multiplicity formula**:

$$f(\theta) = \frac{v}{\sum_{i=0}^d k_i u_i(\theta)^2}.$$

As we check below, $E(\theta)$ completely kills (sends to $0$) every other eigenspace $\theta' \neq \theta$, while scaling every vector inside the $\theta$-eigenspace by a single constant number $\phi(\theta)$. So $E(\theta)$ is a constant multiple of the projection matrix onto the $\theta$-eigenspace, not the projection itself (a projection scales by $1$); the next section shows that the constant is $v / f(\theta)$.

Now let's look at how to compute the trace of $E(\theta)$ in two standard ways from linear algebra. First, sum the diagonal entries. Every diagonal entry of $E(\theta)$ is $1$ (since $A_0$ is the only summand of it with diagonal entries), and there are $v$ rows, so the trace is $v$.

The other way to get the trace is to look at the $\theta$-eigenspace (which has dimension $f(\theta)$). Set $\phi(X) = \sum_{i=0}^d u_i(\theta) p_i(X)$, so $\phi(A) = E(\theta) \neq 0$ (because each distance matrix $A_i$ is generated by the distance polynomial $p_i$ evaluated at the adjacency matrix $A$: $A_i = p_i(A)$) and $\deg(\phi) \le d$.

In linear algebra, if a vector $x$ is an eigenvector of a matrix $A$ with eigenvalue $\lambda$ ($Ax = \lambda x$), then for any polynomial $\phi(X)$, that same vector $x$ is an eigenvector of the matrix $\phi(A)$ with eigenvalue $\phi(\lambda)$.

Take an eigenvector $x$ of $A$ belonging to the eigenvalue $\theta$ ($Ax = \theta x$), then multiplying it by $E(\theta) = \phi(A)$ gives: $E(\theta)x = \phi(A)x = \phi(\theta)x$

So $E(\theta)$ has eigenvalue $\phi(\theta)$ on the $\theta$-eigenspace. On every other eigenspace it is $0$: if $Ax = \theta' x$ with $\theta' \neq \theta$, then $E(\theta)x = \phi(\theta')x$ is a multiple of $x$, so it lies in the $\theta'$-eigenspace, and it is also a $\theta$-eigenvector, because every vector that comes out of $E(\theta)$ is one. Only the zero vector lies in both, so $E(\theta)x = 0$. So the sum of the eigenvalues of $E(\theta)$ is $f(\theta) \cdot \phi(\theta)$.

Setting the two equal gives $v = f(\theta)\phi(\theta)$. Since $p_i(\theta) = k_i u_i(\theta)$, we have $\phi(\theta) = \sum_{i=0}^d u_i(\theta) p_i(\theta) = \sum_{i=0}^d k_i u_i(\theta)^2$, so

$$f(\theta) = \frac{v}{\phi(\theta)} = \frac{v}{\sum_{i=0}^d k_i u_i(\theta)^2}$$

#### Minimal idempotents of the Bose-Mesner algebra

Recall that a matrix $E$ is called **idempotent** if $E^2 = E$. Because $A$ is real and symmetric, we can choose an invertible real $v \times v$ matrix $U$ such that $A' = U^{-1} A U$ is diagonal. The diagonal matrix $A'$ generates a $(d + 1)$-dimensional real algebra $\mathcal{A}'$ consisting entirely of diagonal matrices, and the conjugation map $M \mapsto U^{-1} M U$ is an isomorphism between the algebras $\mathcal{A}$ and $\mathcal{A}'$.

Suppose for concreteness that $v = 4$, and $A$ has $d + 1 = 3$ distinct eigenvalues: $\theta_0 = 2$ (multiplicity $1$), $\theta_1 = 0$ (multiplicity $2$), and $\theta_2 = -2$ (multiplicity $1$). Then:

$$A' = \begin{pmatrix} 2 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -2 \end{pmatrix}$$

Now, what is the algebra $\mathcal{A}'$ generated by $A'$? It is the set of all polynomials in $A'$. Because $A'$ is diagonal with equal entries in rows $2$ and $3$, any polynomial $p(A')$ will also be diagonal and will always have the exact same number in rows $2$ and $3$:

$$p(A') = \begin{pmatrix} p(2) & 0 & 0 & 0 \\ 0 & p(0) & 0 & 0 \\ 0 & 0 & p(0) & 0 \\ 0 & 0 & 0 & p(-2) \end{pmatrix}$$

Look at the three "building block" diagonal matrices $E'_{\theta}$ that put $1$'s in the slots belonging to a single eigenvalue $\theta$ and $0$'s everywhere else:

$$E'_2 = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad E'_0 = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 \end{pmatrix}, \quad E'_{-2} = \begin{pmatrix} 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$

We can see that $A' = \sum_{\theta \in \Theta} \theta E'_\theta$. Note that $E'_\theta$ is idempotent of rank $f(\theta)$. Clearly $\{E'_\theta \mid \theta \in \Theta\}$ is a basis of $\mathcal{A}'$. $\operatorname{Tr}(E'_\theta) = f(\theta)$, and $E'_{\theta_1} E'_{\theta_2} = 0$ for $\theta_1 \neq \theta_2$.

Moreover, any matrix $M'$ in the diagonal algebra $\mathcal{A}'$ is a linear combination of these $d+1$ building blocks: $M' = \sum_{\theta \in \Theta} \lambda_\theta E'_\theta$.

What happens when we square $M'$? All cross-terms $E'_{\theta_1} E'_{\theta_2}$ vanish and $(E'_\theta)^2 = E'_\theta$, squaring a linear combination just squares the coefficients.

$$(M')^2 = \left(\sum_{\theta \in \Theta} \lambda_\theta E'_\theta\right)^2 = \sum_{\theta \in \Theta} \lambda_\theta^2 (E'_\theta)^2 = \sum_{\theta \in \Theta} \lambda_\theta^2 E'_\theta$$

For $M'$ to be idempotent ($(M')^2 = M'$), the coefficients of each basis matrix $E'_\theta$ must match: $\lambda_\theta^2 = \lambda_\theta \quad \text{for every } \theta \in \Theta$. So $\lambda = 0,1$.

Therefore, any idempotent matrix in $\mathcal{A}'$ is made of the building blocks $E'_\theta$. Furthermore, a single building block $E'_\theta$ cannot be split into smaller non-zero idempotents inside $\mathcal{A}'$. So the matrices $E'_\theta$ are called the **minimal (or primitive) idempotents**.

Why go through all this? Because the map $M \mapsto U^{-1} M U$ is an **algebra isomorphism**: it preserves addition, matrix multiplication, ranks, traces, and equations like $E^2 = E$.

Pulling each $E'_\theta$ back into $\mathcal{A}$ by defining $E_\theta = U E'_\theta U^{-1}$ (the projection matrix onto the $\theta$-eigenspace of $A$) carries every one of those properties back to $\mathcal{A}$:

- the matrices $E_\theta$ ($\theta \in \Theta$) form a basis of $\mathcal{A}$, and each $E_\theta$ is an idempotent matrix of $\mathcal{A}$ (and symmetric, since every matrix in $\mathcal{A}$ is a polynomial in the symmetric matrix $A$);
- $\operatorname{rank}(E_\theta) = \operatorname{Tr}(E_\theta) = f(\theta)$;
- $A E_\theta = \theta E_\theta$ and $A = \sum_{\theta \in \Theta} \theta E_\theta$;
- $E_{\theta_1} E_{\theta_2} = 0$ whenever $\theta_1 \neq \theta_2$;
- every idempotent of $\mathcal{A}$ is the sum of a subset of $\{E_\theta \mid \theta \in \Theta\}$.

$E_\theta$ are the minimal idempotents of the Bose-Mesner algebra $\mathcal{A}$, with $E_\theta$ the minimal idempotent corresponding to $\theta$.

How does $E_\theta$ relate to the matrix $E(\theta) = \sum_{i=0}^d u_i(\theta) A_i$? We showed that $E(\theta)$ satisfies $A E(\theta) = \theta E(\theta)$ and has trace $v$, whereas the true minimal idempotent $E_\theta$ satisfies $A E_\theta = \theta E_\theta$ and has trace $f(\theta)$. Because the subspace of matrices in $\mathcal{A}$ satisfying $A M = \theta M$ is $1$-dimensional (spanned by $E_\theta$), $E(\theta)$ is simply $E_\theta$ scaled by $\frac{v}{f(\theta)}$:

$$E_\theta = \frac{f(\theta)}{v} E(\theta) = \frac{f(\theta)}{v} \sum_{i=0}^d u_i(\theta) A_i$$

So the Bose-Mesner algebra $\mathcal{A}$ has two natural bases:

**The Combinatorial Basis $\{A_0, A_1, \dots, A_d\}$:** $0$-$1$ matrices that are idempotent under _entrywise_ (Hadamard) multiplication ($A_i \circ A_i = A_i$ and $A_i \circ A_j = 0$).

**The Spectral Basis $\{E_\theta \mid \theta \in \Theta\}$:** Projection matrices that are idempotent under _standard matrix_ multiplication ($E_\theta^2 = E_\theta$ and $E_{\theta_1} E_{\theta_2} = 0$).

And the standard sequence values $u_i(\theta)$ are literally the change-of-basis coefficients that translate between the distance matrices $A_i$ and the eigenspace projections $E_\theta$.

At the largest eigenvalue $\theta_0 = k = b_0$, we have $k = a_i + b_i + c_i$ for every $i$, so the constant tuple $(1, 1, \dots, 1)$ satisfies the recurrence $k u_i = b_i u_{i+1} + a_i u_i + c_i u_{i-1}$ along with $u_0(k) = 1$ and $u_1(k) = \frac{k}{k} = 1$. Thus the standard sequence for $k = b_0$ is $(1, 1, \dots, 1)$, giving $E(k) = \sum_{i=0}^d A_i = J$, and since $f(k) = 1$, the minimal idempotent corresponding to $k = b_0$ is $\frac{1}{v} J$.

Figure 12(b) illustrates the symmetry between these two bases of $\mathcal{A}$ (writing $\Theta = \{\theta_0, \dots, \theta_d\}$, $E_j = E_{\theta_j}$, $f_j = f(\theta_j)$, and $Q_{ij} = f_j u_i(\theta_j)$):

| Basis of $\mathcal{A}$ | Orthogonal under | Change of basis |
| :--- | :--- | :--- |
| Distance $A_0, \dots, A_d$ | $A_i \circ A_j = \delta_{ij} A_i$ | $E_j = \frac{1}{v}\sum_{i=0}^d Q_{ij} A_i$ |
| Idempotents $E_0, \dots, E_d$ | $E_i E_j = \delta_{ij} E_i$ | $A_i = \sum_{j=0}^d p_i(\theta_j) E_j$ |

---

**Aside:** The Bose-Mesner algebra $\mathcal{A}$ is the exact combinatorial generalization of a commutative **centralizer algebra** (for a transitive action with point stabilizer $H$, also known as the **Hecke algebra** of the pair $(G, H)$) from group representation theory.

When a graph comes from a group action (specifically, when a group $G$ acts transitively on the $v$ vertices such that the orbitals, the orbits of $G$ on pairs of vertices $V \times V$, correspond to the distance relations), the Bose-Mesner algebra $\mathcal{A}$ is literally the centralizer algebra of the permutation representation of $G$.

Here is how the dictionary between the two worlds lines up entry by entry:

Suppose a finite group $G$ acts transitively on a set of vertices $V$ (with $\vert{}V\vert{} = v$). Let $\rho: G \to \operatorname{GL}(\mathbb{R}^v)$ be the permutation representation, where each group element $g \in G$ is represented by a $v \times v$ permutation matrix $P_g$.

The **centralizer algebra** (or commutant) of this action is the algebra of all $v \times v$ matrices $M$ that commute with every permutation matrix $P_g$:

$$\mathcal{C}(G) = \{ M \in \operatorname{Mat}_{v \times v}(\mathbb{R}) \mid M P_g = P_g M \text{ for all } g \in G \}$$

What does the condition $M P_g = P_g M$ actually mean for the entries $M_{xy}$ of the matrix $M$? Unpacking $P_g^{-1} M P_g = M$ at entry $(x, y)$ says:

$$M_{g(x), g(y)} = M_{x, y} \quad \text{for all } g \in G$$

In other words, a matrix $M$ commutes with the group action if and only if $M_{xy}$ is constant on every orbit of $G$ acting on pairs of vertices $V \times V$ (the **orbitals** $O_0, O_1, \dots, O_d$).

If we put $1$ on the $i$-th orbital $O_i$ and $0$ everywhere else, we get the $0$-$1$ basis matrices $A_0, A_1, \dots, A_d$ of the centralizer algebra.

When $G$ acts **distance-transitively** on a graph $\Gamma$ (meaning $G$ can map any pair of vertices at distance $i$ to any other pair at distance $i$), the orbitals $O_i$ are precisely the distance-$i$ relations, and the centralizer algebra $\mathcal{C}(G)$ is literally the Bose-Mesner algebra $\mathcal{A}$.

In representation theory, if we decompose the permutation module $\mathbb{R}^v$ into irreducible representations of $G$:

$$\mathbb{R}^v = V_0 \oplus V_1 \oplus \dots \oplus V_d$$

**Schur's Lemma** tells us what the centralizer algebra $\mathcal{C}(G) = \operatorname{End}_G(\mathbb{R}^v)$ looks like when this decomposition is multiplicity-free (meaning each irreducible $V_\theta$ appears only once, which is equivalent to the centralizer algebra being commutative):

Any matrix $M$ that commutes with $G$ cannot mix different irreducible subspaces $V_{\theta_1}$ and $V_{\theta_2}$, and on each irreducible subspace $V_\theta$, $M$ must act as a scalar multiple $\lambda_\theta I_{V_\theta}$.

Therefore, in a basis adapted to the irreducible subspaces $V_\theta$, every matrix in the centralizer algebra becomes block-diagonal, acting as a single scalar on each block $V_\theta$, which is exactly the diagonal algebra $\mathcal{A}'$ from [minimal idempotents of the Bose-Mesner algebra](#minimal-idempotents-of-the-bose-mesner-algebra).

The minimal idempotents $E_\theta$ of the Bose-Mesner algebra are the **isotypic projection operators** from representation theory that project $\mathbb{R}^v$ orthogonally onto each irreducible representation $V_\theta$, and the eigenvalue multiplicity $f(\theta) = \operatorname{Tr}(E_\theta) = \dim(V_\theta)$ is the degree (dimension) of that irreducible representation.

Even the standard sequence $u_i(\theta)$ has a representation-theoretic name: when $G$ acts distance-transitively with point stabilizer $H = G_x$, $(G, H)$ is a **Gelfand pair**, and the values $u_i(\theta)$ are the **zonal spherical functions** on the double cosets $H \backslash G / H$, while Biggs' multiplicity formula is the **orthogonality relation for spherical characters**.

What Delsarte, Bose, and Mesner realized is that you don't actually need the group $G$ to exist for all of this machinery to work:

Every distance-transitive group action gives a distance-regular graph whose centralizer algebra is a Bose-Mesner algebra. However, many strongly regular graphs and distance-regular graphs have trivial or tiny automorphism groups. For example, there are exactly 32,548 non-isomorphic $\mathrm{SRG}(36, 15, 6, 6)$ graphs (McKay and Spence completed the search, so this is the full count and not just the ones known so far). And of the $15$ conference graphs $\mathrm{SRG}(25, 12, 5, 6)$, known as the Paulus graphs, only the Paley graph $P(25)$ has a group acting transitively on its vertices; the other $14$ have none.

Even when there is no group $G$ for the matrices to commute with, the purely combinatorial regularity condition $A A_i = b_{i-1} A_{i-1} + a_i A_i + c_{i+1} A_{i+1}$ forces the span of $\{A_0, A_1, \dots, A_d\}$ to close under matrix multiplication into a commutative semisimple algebra $\mathcal{A}$ that behaves _as if_ it were the centralizer algebra of a multiplicity-free group action, complete with minimal idempotents $E_\theta$, character tables (the eigenmatrices $P$ and $Q$), and character orthogonality relations.

---

#### Krein parameters and the Krein inequalities

Keep the numbering $\Theta = \{\theta_0, \theta_1, \dots, \theta_d\}$ with $\theta_0 = k = b_0$, $E_i = E_{\theta_i}$, $f_i = f(\theta_i)$, and $Q_{ij} = f_j u_i(\theta_j)$. Under ordinary matrix multiplication, $E_i E_j = \delta_{ij} E_i$. What happens when we take the *Hadamard* (entrywise) product $E_i \circ E_j$ instead? Because $\mathcal{A}$ is closed under Hadamard multiplication and $\{E_0, E_1, \dots, E_d\}$ is a basis of $\mathcal{A}$, there exist unique real numbers $q_{ij}^k \in \mathbb{R}$ ($i, j, k \in \{0, 1, \dots, d\}$) such that

$$E_i \circ E_j = \frac{1}{v} \sum_{k=0}^d q_{ij}^k E_k.$$

The numbers $q_{ij}^k$ are called the **Krein parameters** of the distance-regular graph $\Gamma$. Every single one of them is nonnegative. The $\frac{1}{v}$ is just a standard normalization factor.

These are the exact dual of the intersection numbers $p_{ij}^k$ in the Bose-Mesner algebra. While intersection numbers govern what happens when you multiply the combinatorial basis $A_i$ under standard matrix multiplication, the Krein parameters $q_{ij}^k$ govern what happens when you multiply the spectral basis $E_i$ under entrywise (Hadamard) multiplication.

For the combinatorial numbers $p_{ij}^k$, nonnegativity ($p_{ij}^k \ge 0$) is trivial because you can't have a negative number of vertices. Why must $q_{ij}^k$ also be nonnegative? Because from a matrix viewpoint, $E_i$ and $E_j$ are positive semidefinite projection matrices, so the [Schur product theorem](#rank-determinants-and-gram-matrices) says their Hadamard product $E_i \circ E_j$ is also positive semidefinite, which forces all of its eigenvalues $\frac{1}{v} q_{ij}^k$ to be $\ge 0$.

So if even one $q_{ij}^k$ comes out negative, no such graph can exist. Next, we will look at how to calculate the Krein parameters.

---

**Aside:** In our earlier centralizer algebra analogy, $E_i$ and $E_j$ project onto irreducible representations $V_i$ and $V_j$. Entrywise multiplication corresponds to the pointwise product of functions on $V$, $(f \cdot g)(x) = f(x)g(x)$. This is not the tensor product $f \otimes g$, which is a function on pairs $(x, y)$, but its restriction to the diagonal pairs $(x, x)$. When you multiply an eigenvector from $V_i$ entry-by-entry with an eigenvector from $V_j$, which eigenspaces $V_k$ does the resulting vector land in? The Krein parameter $q_{ij}^k$ measures the overlap of the pointwise product $V_i \circ V_j$ with the eigenspace $V_k$. If $q_{ij}^k = 0$, the pointwise product of an eigenvector in $V_i$ and an eigenvector in $V_j$ is strictly orthogonal to $V_k$.

---

**Krein conditions.** For all $i, j, k \in \{0, 1, \dots, d\}$,

$$\begin{aligned}
v f_k q_{ij}^k &= \sum_{l=0}^d k_l Q_{li} Q_{lj} Q_{lk} \\
&= f_i f_j f_k \sum_{l=0}^d k_l u_l(\theta_i) u_l(\theta_j) u_l(\theta_k) \ge 0.
\end{aligned}$$

Let us trace why $v f_k q_{ij}^k$ equals that sum and why it can never be negative. Write $M(x, y)$ for the $(x, y)$-entry of any matrix $M \in \mathcal{A}$ ($x, y \in V$), and let $S = \sum_{x, y \in V} E_i(x, y) E_j(x, y) E_k(x, y)$ be the sum of all entries of $E_i \circ E_j \circ E_k$.

On the idempotent side, for any two symmetric $v \times v$ matrices $L_1$ and $L_2$, summing all entries of $L_1 \circ L_2$ gives $\sum_{x, y} L_1(x, y) L_2(y, x) = \operatorname{Tr}(L_1 L_2)$. Taking $L_1 = E_i \circ E_j = \frac{1}{v}\sum_{l=0}^d q_{ij}^l E_l$ and $L_2 = E_k$ (using $E_l E_k = \delta_{lk} E_k$ and $\operatorname{Tr}(E_k) = f_k$) gives

$$v^2 S = v^2 \operatorname{Tr}\bigl((E_i \circ E_j) E_k\bigr) = v f_k q_{ij}^k.$$

On the distance-matrix side, expand $E_i$, $E_j$, and $E_k$ via $E_r = \frac{1}{v}\sum_{l=0}^d Q_{lr} A_l$. Because $A_l \circ A_m \circ A_n = 0$ unless $l = m = n$ (where $A_l \circ A_l \circ A_l = A_l$, and the sum of all entries of $A_l$ is $v k_l$), the triple sum collapses to a single sum over $l$:

$$v^2 S = \frac{1}{v} \sum_{l=0}^d Q_{li} Q_{lj} Q_{lk} (v k_l) = \sum_{l=0}^d k_l Q_{li} Q_{lj} Q_{lk}.$$

To see why $S \ge 0$, use the fact that $E_i$, $E_j$, and $E_k$ are symmetric and idempotent ($E_r = E_r^2$), so $E_r(x, y) = \sum_{u \in V} E_r(u, x) E_r(u, y)$. Substituting those three sums into $S = \sum_{x, y \in V} E_i(x, y) E_j(x, y) E_k(x, y)$ separates the $x$-sum from the $y$-sum: setting $q(u, v, w) = \sum_{x \in V} E_i(u, x) E_j(v, x) E_k(w, x)$ for each triple $u, v, w \in V$, we obtain a sum of real squares,

$$S = \sum_{u, v, w \in V} q(u, v, w)^2 \ge 0.$$

**Worked example: the $3$-cube $Q_3$.** Let us run the full distance-regular machinery by hand on the $3$-dimensional cube $Q_3$ from Figure 12(a) ($v = 8$ binary triples $\{0, 1\}^3$, joined when differing in one bit, so diameter $d = 3$).

Standing at `000`, a vertex at distance $i$ has $i$ ones and $3 - i$ zeros: flipping one of the $i$ ones steps closer ($c_i = i$), flipping one of the $3 - i$ zeros steps further ($b_i = 3 - i$), and no single bit-flip preserves weight ($a_i = 0$). That gives sphere sizes $k_0 = 1$, $k_1 = \frac{1 \cdot 3}{1} = 3$, $k_2 = \frac{3 \cdot 2}{2} = 3$, and $k_3 = \frac{3 \cdot 1}{3} = 1$ ($1 + 3 + 3 + 1 = 8$).

Now build the normalized polynomials $u_i(X)$: $u_0(X) = 1$ and $u_1(X) = \frac{X}{3}$. At $i = 1$, $2 u_2(X) - \frac{X^2}{3} + 1 = 0$ gives $u_2(X) = \frac{X^2 - 3}{6}$. At $i = 2$, $u_3(X) - \frac{X(X^2 - 3)}{6} + \frac{2X}{3} = 0$ gives $u_3(X) = \frac{X^3 - 7X}{6}$. Then $(X - a_3)u_3(X) - c_3 u_2(X) = \frac{X^4 - 10X^2 + 9}{6} = \frac{(X^2 - 9)(X^2 - 1)}{6}$, giving the $d + 1 = 4$ eigenvalues $\Theta = \{3, 1, -1, -3\}$.

Test $\theta_1 = 1$: its standard sequence is $(1, \frac{1}{3}, -\frac{1}{3}, -1)$, Biggs' formula gives $f(1) = \frac{8}{1(1) + 3(1/9) + 3(1/9) + 1(1)} = \frac{8}{8/3} = 3$, and $8 E_1 = 3(A_0 + \frac{1}{3}A_1 - \frac{1}{3}A_2 - A_3) = 3 A_0 + A_1 - A_2 - 3 A_3$, matching every $+3, +1, -1, -3$ entry in Figure 12(b). Finally, check a Krein parameter such as $q_{11}^2$ for $\theta_1 = 1$ and $\theta_2 = -1$ (where $\theta_2 = -1$ has standard sequence $(1, -\frac{1}{3}, -\frac{1}{3}, 1)$ and multiplicity $f_2 = 3$):

$$\begin{aligned}
\sum_{l=0}^3 k_l u_l(1)^2 u_l(-1) &= 1 + 3\left(\frac{1}{9}\right)\left(-\frac{1}{3}\right) + 3\left(\frac{1}{9}\right)\left(-\frac{1}{3}\right) + 1 \\
&= 2 - \frac{2}{9} = \frac{16}{9},
\end{aligned}$$

so $8 \cdot 3 \cdot q_{11}^2 = 27 \cdot \frac{16}{9} = 48$, which gives $q_{11}^2 = 2 \ge 0$.

#### Specializing the Krein conditions to connected strongly regular graphs

Now specialize back to diameter $d = 2$, where $\Gamma$ is a connected $\mathrm{SRG}(v, k, \lambda, \mu)$ with eigenvalues $k, R_1, R_2$, sphere sizes $k_0 = 1$, $k_1 = k$, $k_2 = v - k - 1$, and $(c_1, a_1, b_1) = (1, \lambda, k - \lambda - 1)$. Pick either $R \in \{R_1, R_2\}$ and compute its standard sequence $(u_0, u_1, u_2)$: we have $u_0 = 1$, $u_1 = \frac{R}{k}$, and from $b_1 u_2 + (a_1 - R)u_1 + c_1 u_0 = 0$,

$$u_2 = \frac{1}{k - \lambda - 1}\left((R - \lambda)\frac{R}{k} - 1\right) = \frac{R^2 - \lambda R - k}{k(k - \lambda - 1)}.$$

Using $R^2 + (\mu - \lambda)R + (\mu - k) = 0$ rewrites the numerator $R^2 - \lambda R - k$ as $-\mu(R + 1)$, while $k(k - \lambda - 1) = \mu(v - k - 1)$ rewrites the denominator, canceling $\mu > 0$ to leave $u_2 = -\frac{R + 1}{v - k - 1}$. Feeding $(u_0, u_1, u_2)$ into the diagonal Krein condition $\sum_{i=0}^2 k_i u_i^3 \ge 0$ (corresponding to $q_{11}^1 \ge 0$ and $q_{22}^2 \ge 0$) produces the **Krein inequalities for connected strongly regular graphs**:

$$1 + \frac{R_1^3}{k^2} - \frac{(R_1 + 1)^3}{(v - k - 1)^2} \ge 0,$$

$$1 + \frac{R_2^3}{k^2} - \frac{(R_2 + 1)^3}{(v - k - 1)^2} \ge 0.$$

(If you test our earlier fake candidate $\mathrm{SRG}(28, 9, 0, 4)$ here, where $k = 9$, $v - k - 1 = 18$, and $R_2 = -5$, the second inequality gives $1 - \frac{125}{81} + \frac{64}{324} = -\frac{28}{81} < 0$, so $q_{22}^2 \ge 0$ independently rules out $(28, 9, 0, 4)$ as well.)

In any primitive $\mathrm{SRG}(v, k, \lambda, \mu)$ with eigenvalues $\theta_0 = k$, $\theta_1 = R_1 > 0$, and $\theta_2 = R_2 < 0$, almost all the Krein parameters $q_{ij}^k$ are automatically nonnegative (several of them are $0$). The only two that can actually go negative and restrict the parameters are the "self-triple" products $q_{11}^1 \ge 0$ and $q_{22}^2 \ge 0$.

---

**Aside:** If the Krein parameters and generalized intersection numbers remind you of the Christoffel symbols from General Relativity and differential geometry, you're not off the mark. The structural analogy to Christoffel symbols $\Gamma_{ij}^k$ goes beyond the index placement: the two kinds of numbers play closely parallel algebraic roles.

In differential geometry or Lie theory, if you have a basis of vector fields or tangent vectors $\{e_0, e_1, \dots, e_d\}$, a connection (or product) tells you how combining two basis directions $e_i$ and $e_j$ decomposes back into the basis $\{e_k\}$:

$$\nabla_{e_i} e_j = \sum_{k=0}^d \Gamma_{ij}^k e_k$$

In a Bose-Mesner algebra $\mathcal{A}$, you have a single $(d+1)$-dimensional space equipped with two dual products and two natural bases. The intersection numbers $p_{ij}^k$ and Krein parameters $q_{ij}^k$ are the **structure constants** (the "connection coefficients") of those two products.

**Combinatorial connection ($p_{ij}^k$).** It measures how two distance spheres $A_i$ and $A_j$ compose under _path concatenation_ (matrix multiplication) and project onto the distance sphere $A_k$:

$$A_i A_j = \sum_{k=0}^d p_{ij}^k A_k$$

**Spectral connection ($q_{ij}^k$).** It measures how two eigenspace projectors $E_i$ and $E_j$ compose under _pointwise interference_ (Hadamard multiplication) and project onto the eigenspace $E_k$:

$$E_i \circ E_j = \frac{1}{v} \sum_{k=0}^d q_{ij}^k E_k$$

Because both products are commutative ($A_i A_j = A_j A_i$ and $E_i \circ E_j = E_j \circ E_i$), both sets of structure constants are **torsion-free** (symmetric in their lower indices):

$$p_{ij}^k = p_{ji}^k \quad \text{and} \quad q_{ij}^k = q_{ji}^k$$

In Riemannian geometry, you lower an upper index on $\Gamma_{ij}^k$ by contracting with the metric tensor $g_{km}$:

$$\Gamma_{ijk} = \sum_m g_{km} \Gamma_{ij}^m$$

In the Bose-Mesner algebra, each basis has its own natural diagonal **metric tensor** (inner product) defined by the trace or entrywise sum.

On the distance basis $\{A_k\}$, the inner product is $\langle A_k, A_m \rangle = \frac{1}{v}\operatorname{Tr}(A_k A_m) = \delta_{km} k_k$, so the diagonal metric tensor has entries $k_k$ (the valencies of the spheres). Lowering the upper index $k$ on $p_{ij}^k$ by multiplying by $k_k$ gives the fully symmetric 3-index tensor

$$p_{ijk} = k_k p_{ij}^k = \frac{1}{v}\operatorname{Tr}(A_i A_j A_k),$$

which is symmetric under _any_ permutation of $(i, j, k)$ (since it counts triangles of vertices with side lengths $i, j, k$).

On the spectral basis $\{E_k\}$, the inner product is $\langle E_k, E_m \rangle = \operatorname{Tr}(E_k E_m) = \delta_{km} f_k$, so the diagonal metric tensor has entries $f_k$ (the multiplicities of the eigenspaces). Lowering the upper index $k$ on $q_{ij}^k$ by multiplying by $f_k$ gives

$$q_{ijk} = f_k q_{ij}^k = v \sum_{x, y \in V} E_i(x, y) E_j(x, y) E_k(x, y),$$

which is the quantity $v f_k q_{ij}^k$ of the [Krein conditions](#krein-parameters-and-the-krein-inequalities) divided by $v$. Look back at those conditions:

$$v f_k q_{ij}^k = \sum_{l=0}^d k_l Q_{li} Q_{lj} Q_{lk}$$

The right-hand side is completely symmetric in $i, j, k$, whereas $q_{ij}^k$ by itself is not symmetric in $k$. Multiplying $q_{ij}^k$ by the metric component $f_k$ lowers the index $k$ to produce the fully symmetric tensor $q_{ijk} = f_k q_{ij}^k$.

There is even a direct geometric reason why the three-term recurrence behaves like parallel transport:

- In general, $p_{ij}^k$ has three independent indices (and in a graph that is not distance-regular these counts are not even constants, because they depend on the pair of vertices).
- In a distance-regular graph, stepping one unit along an edge ($i = 1$) reduces the connection coefficients $p_{1j}^k$ to a *tridiagonal* connection: from a vertex on sphere $j$, a single step can only take you back to sphere $j - 1$ ($c_j$ ways), keep you on sphere $j$ ($a_j$ ways) or take you out to sphere $j + 1$ ($b_j$ ways), so $p_{1j}^k = 0$ unless $k \in \{j - 1, j, j + 1\}$. In the recurrence $A A_j = b_{j-1} A_{j-1} + a_j A_j + c_{j+1} A_{j+1}$ the same counts appear indexed by the sphere a step starts from: $b_{j-1}$ counts the steps out of sphere $j - 1$ into sphere $j$, and $c_{j+1}$ the steps in from sphere $j + 1$.
- In fact, discrete notions of Ricci curvature (following Ollivier, Lin–Lu–Yau and Bakry–Émery) have been studied on distance-regular graphs, where the curvature of an edge depends on local intersection numbers such as $a_1$, $b_1$ and $c_2$.

---

### Applications to partial geometries and generalized quadrangles

In 1963, R. C. Bose introduced **partial geometries** to study generalized quadrangles, linear spaces, and nets under one common framework whose collinearity graphs are strongly regular.

#### Partial geometries and their collinearity graphs

Recall how a finite [generalized quadrangle](#generalized-quadrangles) of order $(s, t)$ behaves: every line has $s + 1$ points, every point lies on $t + 1$ lines. Moreover, from any point $x$ outside a line $L$, you can reach *just $1$* point of $L$ along a line of the geometry. More simply, any point is either incident with a line or is connected to that line by exactly one other line.

A **partial geometry with parameters $(s, t, \alpha)$** (often written $\mathrm{pg}(s, t, \alpha)$, with integers $s \ge 1$, $t \ge 1$, and $\alpha \ge 1$) relaxes that "just $1$" rule to a fixed constant $\alpha$: it is a finite [partial linear space](#partial-linear-spaces) $\mathcal{S} = (\mathcal{P}, \mathcal{L}, \mathrm{I})$ of order $(s, t)$ (every line has $s + 1$ points and every point lies on $t + 1$ lines) in which, for every point $x$ and every line $L$ not passing through $x$ (every anti-flag $(x, L)$), $x$ is collinear with $\alpha$ points of $L$.

Swapping points and lines turns a partial geometry with parameters $(s, t, \alpha)$ into its [point-line dual](#points-lines-duals-and-doubles) $\mathcal{S}^D$, which is a partial geometry with parameters $(t, s, \alpha)$ (each of the $\alpha$ lines joining an external point $x$ to a point of $L$ in $\mathcal{S}$ becomes one of the $\alpha$ dual points on the dual line $x$ collinear with the dual point $L$).

Check the two extreme values of $\alpha$ ($1 \le \alpha \le \min(s + 1, t + 1)$). When $\alpha = 1$, every point outside a line $L$ is collinear with a *unique* point of $L$, so a partial geometry with parameters $(s, t, 1)$ is a finite generalized quadrangle of order $(s, t)$ (having $s, t \ge 1$ guarantees two disjoint lines automatically: take a line $L$, pick a second line $M$ through some point $y \in L$, pick $x \in M \setminus \{y\}$, and take a second line $N \neq M$ through $x$; since $\alpha = 1$, $y$ is already the lone point of $L$ collinear with $x$, so $N$ misses $L$). At the other extreme, when $\alpha = s + 1$, every external point $x$ is collinear with all $s + 1$ points of $L$, so $\mathcal{S}$ is a linear space ($2$-$(v, s + 1, 1)$ Steiner system) whose collinearity graph is complete.

![Counting lambda and mu in the collinearity graph of a partial geometry pg(s,t,alpha)](figures/maths4_pg_collinearity_counts.png)

*Figure 13. Counting common neighbours in the collinearity graph of a partial geometry $\mathrm{pg}(s, t, \alpha)$, drawn with $t = 2$ and $\alpha = 2$. (a) For collinear points $x \sim y$: the $s - 1$ other points of the line $xy$, plus $\alpha - 1$ points on each of the $t$ other lines through $x$, give $\lambda = s - 1 + t(\alpha - 1)$. (b) For noncollinear points $x$ and $z$: $\alpha$ points on each of the $t + 1$ lines through $x$ give $\mu = \alpha(t + 1)$.*

Now suppose $\alpha \le s$, so $\mathcal{S}$ is not a linear space and noncollinear pairs of points exist. We can read the parameters $\lambda$ and $\mu$ of the collinearity graph $\Gamma$ of $\mathcal{S}$ straight off the two panels of Figure 13, and $k$ and $v$ follow from short counts.

Start with the valency $k$. Through any point $x$ pass $t + 1$ lines, each containing $s$ points other than $x$, and in a partial linear space no two lines through $x$ share a second point. So $\Gamma$ is regular with valency $k = s(t + 1)$.

For two noncollinear points $x$ and $z$, look at Figure 13(b). None of the $t + 1$ lines through $x$ passes through $z$, so $z$ forms an anti-flag with each of those $t + 1$ lines. On each line through $x$, $z$ is collinear with $\alpha$ points (none equal to $x$, since $z \nsim x$), giving $\mu = \alpha(t + 1) > 0$ common neighbours (which also shows $\Gamma$ is connected).

For two collinear points $x \sim y$, look at Figure 13(a), where $L = xy$ is the unique line joining them. Any point collinear with both $x$ and $y$ sits on one of the $t + 1$ lines through $x$. On $L$ itself, all $s - 1$ remaining points besides $x$ and $y$ are collinear with both. On each of the remaining $t$ lines $M \neq L$ through $x$, $(y, M)$ is an anti-flag, so $y$ is collinear with $\alpha$ points of $M$; one of those $\alpha$ points is $x$ itself, leaving $\alpha - 1$ common neighbours on each of those $t$ lines. Adding the two counts gives $\lambda = s - 1 + t(\alpha - 1)$.

To get the total point count $v$, we double-count collinear connections from a fixed line $L$. The line $L$ contains $s + 1$ points, so there are $v - (s + 1)$ points outside $L$. Now count the number of pairs $(x, y)$ where $x \notin L$ is a point outside $L$, $y \in L$ is a point on $L$, and $x$ is collinear with $y$ ($x \sim y$).

Count from the outside points $x \notin L$: Every point $x \notin L$ is collinear with $\alpha$ points on $L$. Since there are $v - (s + 1)$ points outside $L$, the total number of such pairs $(x, y)$ is: $\bigl(v - (s + 1)\bigr)\alpha$.

Count from the line points $y \in L$: Pick any of the $s + 1$ points $y \in L$. There are $t + 1$ lines passing through $y$ in total. One of those lines is $L$ itself; the remaining $t$ lines through $y$ step outside $L$ (and cannot meet $L$ again because two lines intersect in at most one point). Each of those $t$ lines contains $s$ points outside $L$. Thus, each $y \in L$ is collinear with $st$ points outside $L$. Across all $s + 1$ points $y \in L$, the total number of pairs $(x, y)$ is: $(s + 1)st$. Equate the two counts and solve for $v$:

$$\bigl(v - (s + 1)\bigr)\alpha = (s + 1)st,$$

$$v = (s + 1) + \frac{(s + 1)st}{\alpha} = \frac{(s + 1)(st + \alpha)}{\alpha}.$$

Now let's check if this is an SRG by ascertaining if the relationship between the parameters is satisfied. Plug $k, \lambda, \mu$ into $k(k - \lambda - 1) = (v - k - 1)\mu$. Since $k - \lambda - 1 = s(t + 1) - (s - 1 + t\alpha - t) - 1 = t(s + 1 - \alpha)$, canceling $t + 1$ gives $st(s + 1 - \alpha) = (v - s(t + 1) - 1)\alpha$, and solving for $v$ gives

$$v = 1 + s(t + 1) + \frac{st(s + 1 - \alpha)}{\alpha} = \frac{(s + 1)(st + \alpha)}{\alpha}.$$

In summary, whenever $\alpha \le s$, the collinearity graph $\Gamma$ of a $\mathrm{pg}(s, t, \alpha)$ is a connected $\mathrm{SRG}(v, k, \lambda, \mu)$ with $v = \frac{(s + 1)(st + \alpha)}{\alpha}$, $k = s(t + 1)$, $\lambda = s - 1 + t(\alpha - 1)$, and $\mu = \alpha(t + 1)$.

#### Divisibility conditions

**Divisibility theorem for partial geometries and generalized quadrangles.** If $\mathcal{S}$ is a partial geometry with parameters $(s, t, \alpha)$, then $\alpha(s + t + 1 - \alpha)$ is a divisor of $st(s + 1)(t + 1)$. In particular, if $\mathcal{S}$ is a finite generalized quadrangle of order $(s, t)$ ($\alpha = 1$), then $s + t$ is a divisor of $st(s + 1)(t + 1)$. This is the divisibility condition stated in [orders and parameter restrictions for generalized quadrangles](#orders-and-parameter-restrictions-for-generalized-quadrangles); here is where it comes from.

Let's see how this happens. Still assuming $\alpha \le s$, compute the three eigenvalues $k, R_1, R_2$ of $\Gamma$. Here $\mu - \lambda = \alpha(t + 1) - (s - 1 + t\alpha - t) = \alpha + t - s + 1$ and $\mu - k = (\alpha - s)(t + 1)$, so the quadratic $X^2 + (\mu - \lambda)X + (\mu - k)$ factors cleanly without square roots:

$$X^2 + (\alpha + t - s + 1)X + (\alpha - s)(t + 1) = (X + \alpha - s)(X + t + 1).$$

Therefore the three distinct eigenvalues of $\Gamma$ are $k = s(t + 1)$, $R_1 = s - \alpha \ge 0$, and $R_2 = -t - 1 < -1$. Substituting these into our factored multiplicity formula $M_1 = \frac{(R_2 + 1)k(k - R_2)}{\mu(R_2 - R_1)}$ gives

$$\begin{aligned}
M_1 &= \frac{(-t)s(t + 1)\bigl(s(t + 1) + t + 1\bigr)}{\alpha(t + 1)(-t - 1 - s + \alpha)} \\
&= \frac{st(s + 1)(t + 1)}{\alpha(s + t + 1 - \alpha)}.
\end{aligned}$$

Because $M_1$ must be an integer (and when $\alpha = s + 1$, $\alpha(s + t + 1 - \alpha) = (s + 1)t$ trivially divides $st(s + 1)(t + 1)$), we obtain the divisibility test for partial geometries and its $\alpha = 1$ specialization to generalized quadrangles.

The Divisibility Theorem for partial geometries (and generalized quadrangles) is not new information independent of the SRG: it is the exact algebraic translation of the integrality of the eigenvalue multiplicities ($M_1, M_2 \in \mathbb{Z}$) of the collinearity graph.

Do we get any new parameter restrictions from the geometry that the SRG alone cannot see? No, it is $100\%$ identical to the SRG multiplicity condition $M_1 \in \mathbb{Z}$.

The Divisibility Theorem is useful because, without it, testing whether a candidate triple like $\mathrm{pg}(4, 5, 2)$ can exist requires four separate translation steps. Compute the four SRG parameters, then set up the quadratic equation $\theta^2 + (\mu - \lambda)\theta + (\mu - k) = 0$ and solve for the roots $R_1$ and $R_2$. Then set up the linear system $1 + M_1 + M_2 = v$ and $k + M_1 R_1 + M_2 R_2 = 0$. Then solve for $M_1$ and check if the resulting fraction is an integer. The Divisibility Theorem pre-computes that entire pipeline once and for all in terms of $(s, t, \alpha)$. For $\mathrm{pg}(4, 5, 2)$ it takes one line: $\alpha(s + t + 1 - \alpha) = 2 \cdot 8 = 16$ would have to divide $st(s + 1)(t + 1) = 20 \cdot 5 \cdot 6 = 600$, but $600 / 16 = 37.5$. So $M_1$ would not be an integer, and no $\mathrm{pg}(4, 5, 2)$ exists, even though its point count $v = \frac{5 \cdot 22}{2} = 55$ and line count $b = \frac{55 \cdot 6}{5} = 66$ are whole numbers.

It also helps us see some hidden symmetry. Writing the multiplicity condition explicitly as $\alpha(s + t + 1 - \alpha) \mid st(s + 1)(t + 1)$ reveals a structural symmetry that is completely hidden inside the SRG formula for $M_1$: the expression is visibly symmetric in $s$ and $t$.

In the SRG world, the point graph $\Gamma$ has parameters $(v, k, \lambda, \mu)$, while the line graph (the collinearity graph of the dual geometry $\mathrm{pg}(t, s, \alpha)$) has $b = \frac{v(t + 1)}{s + 1}$ vertices, valency $t(s + 1)$ and its own $\lambda', \mu'$; these differ from the point graph's unless $s = t$. Yet the Divisibility Theorem shows that the geometry and its dual share the exact same arithmetic bottleneck. If $N$ is the $v \times b$ point-line [incidence matrix](#collinearity-graphs-incidence-graphs), then $N N^T = A + (t + 1)I$ and $N^T N$ have the same nonzero eigenvalues with the same multiplicities: $(s + 1)(t + 1)$ once, and $s + t + 1 - \alpha$ with multiplicity $M_1$.

#### Krein bounds and Higman's inequalities

Applying our SRG Krein inequality to the negative eigenvalue $R_2 = -(t + 1)$ bounds $s$ and $t$ directly in terms of each other.

**Krein bounds for partial geometries.** If $\mathcal{S}$ is a partial geometry with parameters $(s, t, \alpha)$, then

$$(s + 1 - 2\alpha)t \le (s - 1)(s + 1 - \alpha)^2,$$

$$(t + 1 - 2\alpha)s \le (t - 1)(t + 1 - \alpha)^2.$$

Because the point-line dual of a $\mathrm{pg}(s, t, \alpha)$ is a $\mathrm{pg}(t, s, \alpha)$, proving the first inequality gives the second automatically. If $\alpha = s + 1$, the first inequality says $-(s + 1)t \le 0$, which holds trivially. So assume $\alpha \le s$, making $\Gamma$ a connected SRG with $k = s(t + 1)$, $v - k - 1 = \frac{st(s + 1 - \alpha)}{\alpha}$, and $R_2 = -(t + 1)$. Plugging $R_2 = -(t + 1)$ into $1 + \frac{R_2^3}{k^2} - \frac{(R_2 + 1)^3}{(v - k - 1)^2} \ge 0$ and canceling $(t + 1)^2$ and $t^2$ gives

$$1 - \frac{t + 1}{s^2} + \frac{t \alpha^2}{(s + 1 - \alpha)^2 s^2} \ge 0.$$

Multiply through by $s^2(s + 1 - \alpha)^2 > 0$:

$$s^2(s + 1 - \alpha)^2 - (t + 1)(s + 1 - \alpha)^2 + \alpha^2 t \ge 0.$$

Now factor $(s + 1)$ out of the left-hand side:

$$(s + 1)\Bigl[(s - 1)(s + 1 - \alpha)^2 - (s + 1 - 2\alpha)t\Bigr] \ge 0.$$

(You can check that factorization directly: $(s + 1)(s - 1)(s + 1 - \alpha)^2 = (s^2 - 1)(s + 1 - \alpha)^2$, while $-t(s + 1)(s + 1 - 2\alpha) = -t(s + 1 - \alpha)^2 + \alpha^2 t$, and adding the two gives $(s^2 - t - 1)(s + 1 - \alpha)^2 + \alpha^2 t$, which is the left-hand side of the previous inequality.) Dividing by $s + 1 > 0$ proves $(s + 1 - 2\alpha)t \le (s - 1)(s + 1 - \alpha)^2$.

Now set $\alpha = 1$ for a finite generalized quadrangle of order $(s, t)$. The two partial-geometry inequalities reduce to

$$(s - 1)t \le (s - 1)s^2 \quad \text{and} \quad (t - 1)s \le (t - 1)t^2.$$

Dividing by $s - 1 > 0$ when $s \neq 1$, and by $t - 1 > 0$ when $t \neq 1$, gives Higman's inequalities, which were stated in [orders and parameter restrictions for generalized quadrangles](#orders-and-parameter-restrictions-for-generalized-quadrangles):

**Higman's inequalities for generalized quadrangles.** Let $\mathcal{S}$ be a finite generalized quadrangle of order $(s, t)$. If $s \neq 1$, then $t \le s^2$. If $t \neq 1$, then $s \le t^2$.

Look at why the hypothesis $s \neq 1$ is genuinely needed in Higman's inequality. In $(s - 1)t \le (s - 1)s^2$, setting $s = 1$ collapses both sides to $0 \le 0$ for every $t$. Geometrically, $s = 1$ means every line has only $2$ points, and the complete bipartite graph $K_{t+1, t+1}$ (a symmetrical dual grid) is a valid generalized quadrangle of order $(1, t)$ for arbitrarily large $t$, such as $t = 100$ even though $s^2 = 1$. Having $(s - 1)$ appear as an explicit factor shows why thin lines ($s = 1$) escape the $t \le s^2$ ceiling, while every thick line size ($s \ge 2$) locks $t$ below $s^2$.

Note that a generalized $n$-gon with $n \ge 5$ is never a partial geometry, and for $n \ge 6$ its collinearity graph has diameter at least $3$, so it is not a strongly regular graph. (For $n = 5$ the only finite examples with an order are the ordinary pentagons, and their collinearity graph $C_5$ is strongly regular.) Instead, the collinearity graph of a generalized $n$-gon of order $(s, t)$ is a distance-regular graph of diameter $d = \lfloor n/2 \rfloor$, which means you apply the exact same Krein parameter machinery ($q_{ij}^k \ge 0$) inside the larger $(d + 1)$-dimensional Bose-Mesner algebra to get the generalized polygon bounds. We will look at this later.

