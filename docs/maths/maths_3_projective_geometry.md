# Maths 3 - Projective Geometry

Projective geometry is a very significant area since it is effectively how human beings view the world. We see the 3D world as it is projected onto our retinas in 2D. Similarly, computer vision also projects the 3D world onto a 2D computer screen (or whatever else). Projective geometry is also important in physics, for example in the AdS/CFT formalism, where the bulk is projected onto the boundary.

Projective geometry should be quite intuitive on one level because it is essentially what is happening when you shine a torch at something, and a shadow falls on a wall or the floor. What is happening here is that rays of light are grazing the surface of the object i.e. they are tangential to the surface, and then go on to strike the surface serving as the projective wall or plane.

We will do much the same thing in a little while when we take a vector space of $(d+1)$-dimensions, then send out rays/vectors from the origin, and take note of where they intersect a $d$-dimensional subspace that functions as our projective space. This place projective geometry under the umbrella of vector spaces and algebra.

But before that, we look at projective geometry axiomatically, which is called the synthetic approach, so that we understand projective geometry not just in terms of algebra, but also structurally and visually.

In the Euclidean plane that we are familiar with, $\mathbb{R}^2$, we know that any two distinct lines are concurrent (i.e. they meet at a single point), unless they are parallel, and any two distinct points determine a single line. To eliminate the exception of parallelism and make the rule general, we work with the Extended Euclidean Plane (EEP), where we first define a pencil of lines (i.e. given a line, the pencil of lines associated with it are all lines parallel to it). We say that every pencil of lines meets at a distinct point at infinity. Since we require that any two distinct points determine a single line, we then say that all these distinct points at infinity are collinear and lie on the line at infinity called $l_\infty$. If $l$ is a line in the Euclidean plane, we denote $l^*$ as the line in the EEP.

As a matter of notation, we define a triple $(P, L, I)$ to be a set $P$ whose elements are called points, a set $L$ of subsets of $P$ whose elements are called lines (or blocks),and an incidence relation $I$ which describes precisely which points belong to which lines (blocks).

For example, the Euclidean plane is a triple $(P, L, I)$, where $P = \{(x, y) \mid x, y \in \mathbb{R}\}$, $L = \{[a, b, c] \mid a, b, c \in \mathbb{R}, a, b \text{ not both zero}\}$; $I$ : point $(x, y)$ lies on line $[a, b, c]$ if and only if $ax + by + c = 0$.

It is sometimes convenient, particularly when $P$ and $L$ are finite sets, to express $I$ as a subset of $P \times L$. For example, consider the triple $(P, L, I)$ given by: $P = \{1, 2, 3, 4\}$; $L = \{a, b, c, d, e, f\}$; I = \{(1, a),(2, a),(3, b),(4, b),(1, c),(3, c),(2, d),(4, d),(1, e),(4, e),(2, f),(3, f)\}$.

This means that points $1$ and $2$ lie on line $a$, points $3$ and $4$ lie on line $b$, and so on.

In general, in projective geometry, we have The Principle of Duality. If $T$ is a theorem valid in the EEP, and $T'$ is the statement obtained from $T$ by making the following changes: point $\leftrightarrow$ line, collinear $\leftrightarrow$ concurrent, join $\leftrightarrow$ intersection, and whatever grammatical adjustments that are necessary, then $T'$ (called the Dual Theorem) is a valid theorem in the EEP.

## Axioms of Projective Geometry
We can create a set of axioms that define the rules of an r-dimensional projective space. An $r$-dimensional projective space $S_r$, $r \ge 2$, is such that

A1. $S_r$ is a set whose elements are called points.

A2. For every integer $h$, with $-1 \le h \le r$, there are subsets of $S_r$, called subspaces of $S_r$ of dimension $h$. A subspace of $S_r$ of dimension $h$ is usually denoted by $S_h$, and we write $\dim S_h = h$.

A3. There is a unique subspace $S_{-1}$ of $S_r$ called the null subspace. ($S_{-1}$ and $S_r$ are called the non-proper subspaces, and all other subspaces are proper subspaces.)

A4. The points of $S_r$ are the only subspaces of dimension $0$.

A5. There is a unique subspace of dimension $r$, namely $S_r$.

A6. If $S_h$ and $S_k$ are two subspaces of $S_r$, and $S_h \subseteq S_k$, then $h \le k$. Further, $S_h = S_k$ if and only if $h = k$.

A7. Given two subspaces $S_h$ and $S_k$ of $S_r$, then $S_h \cap S_k$ is a subspace $S_i$ of $S_r$.

A8. Given two subspaces $S_h$ and $S_k$ of $S_r$, the span of $S_h$ and $S_k$, denoted by $S_h \oplus S_k$ or by $\langle S_h, S_k \rangle$, is the intersection of all the subspaces of $S_r$ containing both $S_h$ and $S_k$. Let $S_h \cap S_k = S_i$ and $S_h \oplus S_k = S_c$. Then

$$h + k = i + c,$$

that is: $\dim S_h + \dim S_k = \dim (S_h \cap S_k) + \dim (S_h \oplus S_k)$.

A9. (Fano’s Postulate) Every $S_1$ of $S_r$ contains at least three points.

Now for some terminology. In an $r$-dimensional projective space $S_r$ a one-dimensional subspace $S_1$ is called a line. A two-dimensional subspace $S_2$ is called a plane. A three-dimensional subspace $S_3$ is called a solid. An $(r - 1)$-dimensional subspace $S_{r-1}$ is called a hyperplane of the $S_r$. Points which lie on the same line are said to be collinear. Points or lines which lie on the same plane are said to be coplanar. Lines which pass through the same point are said to be concurrent.

We will see that every line in a projective space has the same number of points, say $q+1$. The number $q$ is called the order of the space.

### Projective Plane
A projective plane is a 2D projective space. We can take the axioms of an $r$-dimensional projective space and come up with something specific for a projective plane. The EEP is an example of a projective plane. Later, we will generalize the results for a projective space.

A projective plane $\pi$ is a set $P$ of points and a set $L$ of subsets of $P$, called lines, satisfying the following:

> There exists a unique line joining two distinct points.

> There exists a unique point of intersection of two distinct lines.

> There exist at least three non-collinear points.

> There exist at least three points on each line.

If $\pi$ has a finite number $N_2$ of points. Then:

> Every line of $\pi$ has the same number $N_1 = q + 1$ of points. The order of the plane is $q$.
    
> The number $N_2$ of points in $\pi$ is $q^2 + q + 1 = \frac{q^3 - 1}{q - 1}$.

By the principle of duality in the plane: 

> number of points on a line = number of lines through a point = $q + 1$, 

> number of points in the plane = number of lines in the plane = $q^2 + q + 1$.

### $r$-dimensional Projective Space

More generally, if an $r$-dimensional projective space has a finite number $N_r$ of points, then every line of $S_r$ has the same number $q+1$ of points. The number $q$ is called the order of the space $S_r$. $N_r = q^r + q^{r-1} + \dots + q + 1 = \frac{q^{r+1} - 1}{q - 1}$. Note that the order is always defined based on the number of points on a line (and not a hyperplane or any other subspace), irrespective of the dimension of the projective space.

Duality associates points with hyperplanes, which are $(r-1)$-dimensional projective subspaces of $S_r$. In general, for all $n$, with $0 \le n \le r$, a subspace $S_n$ of dimension $n$ is dual to a subspace $S_{r-n-1}$ of dimension $r - n - 1$.

If $U$ be a $n$-dimensional subspace of $\mathbf{P}$ ($1 \le n \le r$) then $U$ is itself a projective space and the number of points of $U$ is:

$$q^n + q^{n-1} + \dots + q + 1 = \frac{q^{n+1} - 1}{q - 1}$$

The number of lines of $U$ through a fixed point of $U$ equals:

$$q^{n-1} + \dots + q + 1 = \frac{q^n - 1}{q - 1}$$

You can arrive at this by seeing that by duality this is the same number as the number of $(n-2)$-D subspaces contained in an $(n-1)$-subspace of $U$. By duality once again, this is in turn the same as the number of points in a $(n-1)$-subspace. Just for kicks, note that this number can also be arrived at by seeing that every line of $U$ through $P$ contains $P$ plus $q$ other points of $U$, and every point $Q \neq P$ lies on a unique line through $P$. Dividing the remaining points by $q$ points per line gives the number of lines through $P$ (and by duality, the number of $(n-2)$-subspaces in an $(n-1)$-subspace): $\frac{q(q^n - 1)}{q(q - 1)} = \frac{q^n - 1}{q - 1} = q^{n-1} + \dots + q + 1$

Getting back to our original thread, the total number of lines of $U$ equals:

$$\frac{(q^n + q^{n-1} + \dots + q + 1)(q^{n-1} + \dots + q + 1)}{q + 1} = \frac{(q^{n+1} - 1)(q^n - 1)}{(q^2 - 1)(q - 1)}$$

Note that all of these hold for $\mathbf{P}$ also by setting $n = r$.

### 3-dimensional Projective Space $S_3$

In the projective space $S_3$ of dimension $3$,

> a point (of dimension $0$) is dual to a plane (of dimension $2 = 3 - 0 - 1$),
    
> a line (of dimension $1$) is dual to a line (of dimension $1 = 3 - 1 - 1$)

> Number of points = $q^3 + q^2 + q + 1$ = number of planes. 

> Number of planes containing a line $\ell$ = number of points on a line $\ell$ = $q + 1$. 

> Number of lines through a point = number of lines in a plane = $q^2 + q + 1$.

Though we have a formula derived above for this, counting the number of lines in the space in a few different ways helps to give an intuition of the kind of numbers and combinatorics encountered in projective spaces especially over finite fields. 

**Counting the number of lines in $S_3$ - Method I:** Let $N$ be the number of lines in $S_3$. We count the number $M$ of pairs $(\ell, P)$, where $P$ is a point lying on the line $\ell$. On each of the $N$ lines of $S_3$ there are $q + 1$ points. Thus,

$$M = N(q + 1).$$

Further, through each of the $q^3 + q^2 + q + 1$ points of $S_3$, there pass $q^2 + q + 1$ lines. Therefore,

$$M = (q^2 + q + 1)(q^3 + q^2 + q + 1).$$

Hence

$$N = \frac{M}{q + 1} = \frac{(q^2 + q + 1)(q^3 + q^2 + q + 1)}{q + 1}$$

$$= (q^2 + q + 1)(q^2 + 1)$$

$$= q^4 + q^3 + 2q^2 + q + 1.$$

**Counting the number of lines in $S_3$ - Method II:** Each pair of the $q^3 + q^2 + q + 1$ points of $S_3$ gives rise to a line, and any line is specified by a pair of its $q + 1$ points, the number of lines of $S_3$ is

$$N = \frac{\binom{q^3+q^2+q+1}{2}}{\binom{q+1}{2}}$$

$$= \frac{(q^3 + q^2 + q + 1)(q^3 + q^2 + q)}{(q + 1)q}$$

$$= \frac{(q^2 + 1)(q + 1)q(q^2 + q + 1)}{(q + 1)q}$$

$$= (q^2 + 1)(q^2 + q + 1)$$

$$= q^4 + q^3 + 2q^2 + q + 1.$$

## Vector Spaces and Projective Geometry
Purely axiomatic geometry (also called synthetic geometry) lacks a coordinate system, making it very difficult to compute transformations, intersections, or specific loci. We want to label these abstract points and lines with coordinates so we can calculate with them and get geometrical results by mechanically manipulating numbers. 

Before going further, we must point out that every axiomatic projective space of dimension greater than or equal to 3 can be constructed out of a $(d+1)$-dimensional vector space $V$ over some division ring $K$. 

If dimension $d = 2$ i.e. if we are looking at projective planes, then we may not be able to find such vector spaces for certain projective planes called non-Desarguesian planes. Essentially, they cannot be embedded inside any 3D projective space. We will not bother about such planes here, but one important plane is the Moufang / Octonion Plane $\mathbb{O}\mathbb{P}^2$, which is built using the 8-dimensional Octonions $\mathbb{O}$, where multiplication is non-associative. Because octonions are not associative, you cannot form a true vector space over them, and $\mathbb{O}\mathbb{P}^2$ cannot exist inside any $\mathbb{O}\mathbb{P}^3$.

To make the geometry of a projective space calculable, we construct a $d$-dimensional projective space out of a standard $(d+1)$-dimensional vector space $V$ over a field $\mathbb{F}$ (such as $\mathbb{F}^3$ for a 2D projective plane). By intentionally defining projective objects as vector subspaces, the geometry inherits the robust machinery of linear algebra.

Think of it this way. Take a 3D vector space. Draw a vector from the origin. This vector will pierce the $z=1$ plane at a point. This point represents a point on the projective plane. Of course, the vector will pierce every plane $z = k \in \mathbf{C}$ except the $z=0$ plane. All these points are considered an equivalence class, which is no different from saying the $1D$ vector is equivalent to the projective point. The points at infinity are formed by the intersection of vectors with the $z=0$ plane at infinity. Thus:

A Projective Point is defined as a 1-dimensional vector subspace (a line extending through the origin in $V$). A Projective Line is defined as a 2-dimensional vector subspace (a plane extending through the origin in $V$). The Projective Plane (dimension $2$) is defined as the entire $3$D vector space $V = \mathbb{F}^3$. The "$-1$ relationship in dimensions continues into higher dimensions. 

This algebraic translation automatically satisfies the abstract axioms. For instance, the axiom stating "any two projective lines must intersect in exactly one projective point" simply becomes the standard linear algebra theorem: "In a 3-dimensional vector space, the intersection of any two distinct 2-dimensional subspaces must be a 1-dimensional subspace."

However, once again, as we saw earlier, we end up rules with qualifications. For example, two lines meet at a point - unless they are parallel. Another example: the intersection of $a_1x + b_1y = c_1$ and $a_2x + b_2y = c_2$ is found by Cramer's rule... unless the determinant is zero. A third example: a conic section can be an ellipse, a parabola, or a hyperbola... depending on how its asymptotes behave.

To avoid these qualifications, we saw how to add points at infinity where parallel lines meet. Similarly, conics stop having three different names: parabolas and hyperbolas are simply ellipses that happen to touch or cross at a point at infinity. 

To label all these points, we use something like the usual coordinate system of $(x, y)$ but add an additional $z$ coordinate such that the coordinates of the points on the line at infinity have $z=0$, while the other points are $z=1$. Of course, this leaves us in a bit of a quandary. What do the points with $z \neq 0, 1$ mean? We need to map these back to the affine plane somehow. The trick that is used is to simply normalize $(x, y, z)$ by $z$, so that $(\rho x, \rho y, \rho z)$ is the same as $(x, y, z)$. The ratio $X/Z$ and $Y/Z$ determines the point of the affine plane, and there is a whole equivalence class of coordinates in the projective plane, which differ only by the scale factor, that map to the same affine and projective plane point. For example, the equivalence class containing $(2, 4, 2)$ can be scaled by $1/2$ to become $(1, 2, 1)$. This class represents the specific finite affine point $(1, 2)$. 

When $z=0$, the $x$ and $y$ values capture the direction vector of a line. Once again, for example because $(4, 8, 0) = 2 \cdot (2, 4, 0)$, both triples belong to the same equivalence class. Geometrically, this makes sense: a direction vector from the origin to $(2, 4)$ points in the exact same direction (a slope of $2$) as a direction vector from the origin to $(4, 8)$. Therefore, they define the exact same point on the line at infinity. Note that these coordinates, called homogenous coordinates are not something new. They are just the coordinate values of each basis vector that is needed to describe a vector of the $d+1$-dimensional vector space. Essentially, if we fix a basis $\{v_0, v_1, \dots, v_d\}$ of $V$. Then we can express any vector as $v = a_0 v_0 + a_1 v_1 + \dots + a_d v_d \in V$ uniquely by its coordinates $(a_0, a_1, \dots, a_d)$. Two homogenous coordinates $a$ and $b$ are an equivalence class and therefore the same point (as discussed above) if there is an $\alpha \in F \setminus \{0\}$ such that $(a_0, a_1, \dots, a_d) = \alpha \cdot (b_0, b_1, \dots, b_d)$

The vector space model directly reproduces the axiomatic count $q^2 + q + 1$. The ambient vector space $V = \mathbb{F}_q^3$ has $q^3$ total vectors. Remove the origin $\mathbf{0}$: $q^3 - 1$ non-zero vectors. Every $1$-dimensional vector subspace contains $q - 1$ non-zero scalar multiples of its spanning (unit) vector. The total number of $1$-dimensional subspaces (projective points) is: $\frac{q^3 - 1}{q - 1} = q^2 + q + 1$.

By mapping the projective plane to subspaces of $\mathbb{F}^3$, geometry instantly inherits the computational tools of linear algebra:

Finding the line through two points $\mathbf{p}_1, \mathbf{p}_2$: Take the vector cross product: $\boldsymbol{\ell} = \mathbf{p}_1 \times \mathbf{p}_2$
    
Finding the intersection of two lines $\boldsymbol{\ell}_1, \boldsymbol{\ell}_2$: Take the exact same cross product: $\mathbf{p} = \boldsymbol{\ell}_1 \times \boldsymbol{\ell}_2$
    
Checking if a point $\mathbf{p} = (x, y, z)$ lies on a line $\boldsymbol{\ell} = [a, b, c]$: Take the standard dot product: $\boldsymbol{\ell} \cdot \mathbf{p} = ax + by + cz = 0$
    
Checking collinearity of three points: Compute a single $3 \times 3$ determinant: $\det \begin{pmatrix} x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \\ x_3 & y_3 & z_3 \end{pmatrix} = 0$

Geometric problems become straightforward matrix and vector calculations. These rules generalize to higher dimensions $PG(n, \mathbb{F})$ where the 3D cross product is replaced by the exterior wedge product ($\wedge$) and Plücker coordinates, which we won't immediately bother about right now.

The vector space representation also includes the principle of duality. For example, because a point is a 1D subspace of $\mathbb{F}^3$ and a line is a 2D subspace of $\mathbb{F}^3$, the incidence condition:

$$ax + by + cz = 0$$

is completely symmetric between the point coordinates $(x, y, z)$ and the line coordinates $[a, b, c]$.

In linear algebra over a 3D vector space, a 2D subspace (a plane through the origin) is uniquely defined by its 1D normal vector (an element of the dual space $V^*$). This means every theorem true for points and lines is automatically true if you swap the words "point" and "line". You prove a theorem once, and you get its dual theorem for free without any additional work.

### Homogenous Polynomials
Since we have homogenous coordinates (the ones with the additional $z=0$ coordinate), we can create homogenous polynomials. A polynomial $F(X_0, X_1, \dots, X_n)$ is homogeneous of degree $d$ if every individual monomial term has the exact same total degree $d$.

Algebraically, scaling all input variables by a non-zero factor $\rho \in \mathbb{F} \setminus \{0\}$ pulls the scalar out cleanly:

$$F(\rho X_0, \rho X_1, \dots, \rho X_n) = \rho^d F(X_0, X_1, \dots, X_n)$$

$F(X, Y, Z) = 2X - 5Y + 3Z$, $F(X, Y, Z) = X^2 + 3XY - Z^2$, $F(X, Y, Z) = Y^2 Z - X^3 + 4XZ^2$ are each homogenous polynomials of degree 1, 2 and 3. A non-homogenous polynomial can be converted into a homogenous polynomial by replacing $x$ and $y$ by $X/Z$ and $Y/Z$ and multiplying by $Z^d$. Essentially we pad each mononomial with $Z$ till all degrees become uniform.

$$y - x^2 = 0 \implies \frac{Y}{Z} - \frac{X^2}{Z^2} = 0 \overset{\times Z^2}{\implies} YZ - X^2 = 0$$

To return to the standard affine plane, set the homogenizing variable $Z = 1$ (or equivalently set $x = X/Z$, $y = Y/Z$):

$$F(X, Y, Z) = Y^2 Z - X^3 - A X Z^2 - B Z^3 \overset{Z = 1}{\implies} y^2 = x^3 + Ax + B$$

Why do we need homogenous polynomials? In projective space, a point is not a single coordinate tuple; it is an equivalence class. If a polynomial is homogeneous of degree $d$, then:

$$F(\rho X_0, \dots, \rho X_n) = \rho^d F(X_0, \dots, X_n)$$

Because $\rho \neq 0$, the condition:

$$F(X_0, \dots, X_n) = 0 \iff F(\rho X_0, \dots, \rho X_n) = 0$$

The zero-locus $F = 0$ is well-defined: whether a point satisfies the equation does not depend on which representative vector of the equivalence class we choose.

### Mapping Projective Subspaces to Blocks
Finite projective geometries over a finite field act as a natural machine for constructing highly symmetric block designs. Note that a $t-(v, k, \lambda)$ design is called a Balanced Incomplete Block Design (BIBD). This is a setup where there are a total of $v$ points. We create "blocks", each with $k$ points (where $k \lt v$, and hence any block is Incomplete), with the constraint that any set of $t$ points must appear together in $\lambda$ blocks (since this property is uniformly applied to all points, the design is balanced). 

When a finite projective space of dimension $n$ over a field of order $q$, denoted as $\text{PG}(n, q)$, is used to build a block design, its geometric components directly map to the elements of a $2\text{-}(v, k, \lambda)$.

Points ($v$) of the block design are the geometric points ($1$-dimensional vector subspaces of $\mathbb{F}_q^{n+1}$) of $\text{PG}(n, q)$.
    
Blocks ($b$), each with $k$ points$ are all $d$-dimensional projective subspaces (subspaces of a fixed projective dimension $1 \le d \le n-1$). For instance, blocks are frequently chosen to be the lines ($d=1$) or hyperplanes ($d=n-1$) of the space. As we have seen, a line contains $q+1=k$ points.
    
Balance ($\lambda$) property of a $2$-BIBD states that any pair of distinct points must appear together in $\lambda$ blocks. In projective geometry, any two distinct points uniquely determine a line, or more broadly, lie together in a constant number of higher-dimensional subspaces.
    
If you choose $d$-dimensional subspaces as blocks in $\text{PG}(n, q)$, the standard design parameters $(v, b, r, k, \lambda)$ are determined using Gaussian binomial coefficients ($q$-analogs):

| Design Parameter | Geometric Meaning | Formula in $\text{PG}(n, q)$ |
| --- | --- | --- |
| **$v$ (Total Points)** | Total number of points in $\text{PG}(n, q)$ | $v = \begin{bmatrix} n+1 \\ 1 \end{bmatrix}_q = \frac{q^{n+1}-1}{q-1}$ |
| **$k$ (Block Size)** | Points contained in a $d$-subspace | $k = \begin{bmatrix} d+1 \\ 1 \end{bmatrix}_q = \frac{q^{d+1}-1}{q-1}$ |
| **$\lambda$ (Pair Replication)** | Subspaces of dim $d$ containing $2$ points | $\lambda = \begin{bmatrix} n-1 \\ d-1 \end{bmatrix}_q = \frac{(q^{n-1}-1)(q^{n-2}-1)\cdots(q^{n-d+1}-1)}{(q^{d-1}-1)(q^{d-2}-1)\cdots(q-1)}$ |
| **$r$ (Point Replication)** | Subspaces of dim $d$ passing through $1$ point | $r = \begin{bmatrix} n \\ d \end{bmatrix}_q$ |
| **$b$ (Total Blocks)** | Total number of $d$-dimensional subspaces | $b = \begin{bmatrix} n+1 \\ d+1 \end{bmatrix}_q$ |

---

**Aside:** $\begin{bmatrix} m \\ k \end{bmatrix}_q$ is the Gaussian binomial coefficient (or $q$-binomial coefficient). It is the $q$-analog of the standard binomial coefficient $\binom{m}{k}$. For integers $m \ge k \ge 0$, the explicit product formula is:

$$\begin{bmatrix} m \\ k \end{bmatrix}_q = \frac{(q^m - 1)(q^{m-1} - 1) \cdots (q^{m-k+1} - 1)}{(q^k - 1)(q^{k-1} - 1) \cdots (q - 1)} = \prod_{i=1}^{k} \frac{q^{m - i + 1} - 1}{q^i - 1}$$

By convention, $\begin{bmatrix} m \\ 0 \end{bmatrix}_q = 1$, and $\begin{bmatrix} m \\ k \end{bmatrix}_q = 0$ if $k < 0$ or $k > m$.

---

As a special case, when you take a $2$-dimensional projective plane $\text{PG}(2, q)$ and let the blocks be the lines, you get a Symmetric BIBD (where $v = b$ and $r = k$) with parameters: $2\text{-}\left(q^2 + q + 1,\; q + 1,\; 1\right)$
    
For the special case of Point-Hyperplane Designs ($d = n-1$), i.e. we move to higher dimensions ($n \ge 3$), and choose the blocks to be hyperplanes (subspaces of codimension $1$), we obtain the family of symmetric designs $\text{PG}_{n-1}(n, q)$:
    
$$v = b = \frac{q^{n+1}-1}{q-1}, \qquad k = r = \frac{q^n-1}{q-1}, \qquad \lambda = \frac{q^{n-1}-1}{q-1}$$

Why do the Gaussian Binomial Coefficient $\begin{bmatrix} m \\ k \end{bmatrix}_q$ count subspaces? A projective space $\text{PG}(n, q)$ is the lattice of vector subspaces of the $(n+1)$-dimensional vector space $V = \mathbb{F}_q^{n+1}$, where a projective subspace of dimension $d$ corresponds to a vector subspace $W \subset V$ of vector dimension $d+1$.

To count the number of $(d+1)$-dimensional vector subspaces in $\mathbb{F}_q^{n+1}$:

Count the number of ordered linearly independent $(d+1)$-tuples of vectors $(w_1, w_2, \dots, w_{d+1})$ in $V$. Starting with the first basis vector $w_1$, it can be any nonzero vector: $q^{n+1} - 1$ choices. $w_2$ can be any vector outside $\text{span}(w_1)$: $q^{n+1} - q$ choices. $w_i$ can be any vector outside $\text{span}(w_1, \dots, w_{i-1})$: $q^{n+1} - q^{i-1}$ choices.

Then divide by the number of ordered bases of a fixed $(d+1)$-dimensional subspace $W$, which by the exact same logic is $(q^{d+1}-1)(q^{d+1}-q)\cdots(q^{d+1}-q^d)$. Canceling common powers of $q$ yields the Gaussian binomial coefficient:

$$b = \begin{bmatrix} n+1 \\ d+1 \end{bmatrix}_q = \frac{(q^{n+1}-1)(q^{n+1}-q)\cdots(q^{n+1}-q^d)}{(q^{d+1}-1)(q^{d+1}-q)\cdots(q^{d+1}-q^d)} = \frac{(q^{n+1}-1)(q^n-1)\cdots(q^{n-d+1}-1)}{(q^{d+1}-1)(q^d-1)\cdots(q-1)}$$

We should also look at the Quotient-Space proof of the $r$ and $\lambda$ formulas. Why does passing through $s$ independent points simply subtract $s$ from both the top and bottom indices of $\begin{bmatrix} n+1 \\ d+1 \end{bmatrix}_q$?

Because in linear algebra, there is a natural bijection between $(d+1)$-dimensional vector subspaces $W \subset V$ containing a fixed $s$-dimensional subspace $U \subset V$ and $(d+1-s)$-dimensional subspaces of the quotient space $V/U \cong \mathbb{F}_q^{n+1-s}$:

Containing $1$ projective point ($s = 1$ vector dimension):

$$r = \begin{bmatrix} (n+1)-1 \\ (d+1)-1 \end{bmatrix}_q = \begin{bmatrix} n \\ d \end{bmatrix}_q$$

Containing $2$ distinct projective points ($s = 2$ vector dimensions, spanning a projective line):

$$\lambda = \begin{bmatrix} (n+1)-2 \\ (d+1)-2 \end{bmatrix}_q = \begin{bmatrix} n-1 \\ d-1 \end{bmatrix}_q$$

Notice that these parameters automatically satisfy the two fundamental necessary conditions of any $2\text{-}(v, k, \lambda)$ block design:

$$bk = vr \qquad \text{and} \qquad \lambda(v - 1) = r(k - 1)$$

### Some Properties of Projective Spaces Embedded in Vector Spaces

If $V'$ is a subspace of the vector space $V$ then $P(V')$ is a subspace of $P(V)$. And if $U$ be a subspace of the projective space $P(V)$, there exists a vector subspace $V'$ of $V$ such that $P(V')=U$.

The line of $P(V)$ through the points $v, w$ consists of the point $w$ and the points $v + aw, (a \in \mathbf{F})$. In particular we have: if $\mathbf{F}$ is a finite field with $q$ elements, then any line of $P(V)$ has exactly $q+1$ points. In this case $P(V)$ has order $q$. This implies that for any prime power $q$ ($q = p^a$ where p is prime), and any positive integer $d>2$ there is a projective space of order $q$ and dimension $d$. (Since any prime power $q$ implies there is a finite field $\mathbf{F}$ with $q$ elements.

Let $H$ be a hyperplane of $\mathbf{P}(V)$. Then the homogeneous coordinates of the points of $H$ are the solutions of a homogeneous linear equation ($c_0 x_0 + c_1 x_1 + \dots + c_r x_r = 0$) with coefficients in $F$. Conversely, any homogeneous linear equation that is different from the ‘zero equation’ (where all coefficients are $0$) describes a hyperplane of $\mathbf{P}(V)$. We already saw this with a line in a projective plane.

A projective subspace (like a line, plane, or hyperplane) is strictly flat geometry. It is built entirely out of linear equations. Instead of a linear equation, if we use a homogeneous polynomial of degree $d = 2$, such as:

$$X^2 + Y^2 - Z^2 = 0$$

because the variables are squared, the geometry curves. It ceases to be a subspace and becomes an algebraic variety, specifically, a hypersurface of order 2, which is called a quadric (or a conic in 2D). Similarly, a polynomial of degree 3 (e.g.,  $X^3 + Y^2 Z - X Z^2 = 0$), gives a cubic hypersurface, and so on.

Note that the dimension of the resulting surface is determined by the ambient space and the number of equations, not the degree of the equation. If we are working in an $r$-dimensional projective space, applying one homogeneous equation (whether it is degree 1, degree 2, or degree 100) always reduces the dimension by exactly one.

One equation of degree 1 defines a hyperplane of dimension $r - 1$. One equation of degree 2 defines a quadric hypersurface of dimension $r - 1$. One equation of degree $n$ defines a hypersurface of order $n$ of dimension $r - 1$.

To reduce the dimension further (for example, to get a 1D curve in 3D space), we do not increase the degree of the polynomial but intersect multiple surfaces by applying multiple equations simultaneously.

Algebraically, we can write all this as any $t$-dimensional subspace $U$ of a projective space of dimension $d$ given by homogeneous coordinates can be described by a homogeneous system of $d - t$ linear equations. More precisely: there exists a $(d - t) \times (d + 1)$ matrix $H$ (of rank $d - t$) such that a point $P = (a_0 : a_1 : \dots : a_d)$ is a point of $U$ if and only if $(a_0, a_1, \dots, a_d)H^T = 0$.

Let $\mathbf{P}(V)$ be a projective space whose points are given by homogeneous coordinates $(a_0 : a_1 : \dots : a_d)$ with $a_i \in F$,  $(a_0, a_1, \dots, a_d) \neq (0, 0, \dots, 0)$. This notation is not different from the $(x, y, z)$ notation we introduced for the projective plane. Here $a_0$ plays the role of $z$ in the corresponding $d-$dimensional projective space.

Any hyperplane of $\mathbf{P}(V)$ can be represented by $[b_0 : b_1 : \dots : b_d]$ with $b_i \in F$,  $[b_0, b_1, \dots, b_d] \neq [0, 0, \dots, 0]$. Conversely, to any such $(d + 1)$-tuple $[b_0 : b_1 : \dots : b_d]$ there belongs a hyperplane. Moreover, we have:

$$(a_0 : a_1 : \dots : a_d) \;\mathbf{I}\; [b_0 : b_1 : \dots : b_d] \iff a_0 b_0 + a_1 b_1 + \dots + a_d b_d = 0$$

We already saw that this holds for a line and a point incidence relation in a projective plane. 

### Projective & Affine Spaces

Projective spaces are just affine spaces with a hyperplane added at infinity. Let $H_0$ be the hyperplane of $\mathbf{P}(V)$ with equation $x_0 = 0$. Then the affine space $\mathbf{A} = \mathbf{P} \setminus H_0$ can be described as follows:

The points of $\mathbf{A}$ are the vectors $(a_1, \dots, a_d)$ of the $d$-dimensional vector space $F^d$.
    
The lines of $\mathbf{A}$ are the cosets of the $1$-dimensional subspaces of $F^d$; that is, the sets $u + \langle v \rangle$, where $u, v \in F^d$,  $v \neq 0$.
    
Incidence is set-theoretical containment.

Notice that using cosets for lines is unique to affine geometry. We never saw cosets in projective geometry because projective subspaces correspond strictly to vector subspaces (which must all pass through the origin $\mathbf{0}$), whereas affine lines can be shifted anywhere in space without passing through the origin.
  
A line in the affine space is a set of the form:
  
$$u + \langle v \rangle = \{ u + t v \mid t \in \mathbb{F} \}$$
where $u, v \in \mathbb{F}^d$ and $v \neq \mathbf{0}$.
  
In linear algebra and group theory $\langle v \rangle = \{ t v \mid t \in \mathbb{F} \}$ is a 1-dimensional vector subspace. Geometrically, it is a straight line passing directly through the origin $\mathbf{0}$ in the direction of vector $v$.

$u + \langle v \rangle$ is a translated line or a coset. Adding a fixed starting vector $u$ to every vector in the subspace $\langle v \rangle$ shifts the entire line away from the origin so that it passes through the point $u$ instead.

In group theory, shifting a subgroup $W$ by a fixed element $u$ is called a coset ($u + W$). In analytical geometry, we already know this expression as the parametric vector equation of a line: a starting position $u$ plus a scalar multiple $t$ of a direction vector $v$.
  
Compare this to projective space. In the $(d+1)$-dimensional vector space $\mathbb{F}^{d+1}$, every projective object is a true vector subspace passing through the origin $(0, 0, \dots, 0)$. There is no need for cosets because nothing is ever shifted off the origin of $\mathbb{F}^{d+1}$.

However, when restricting our view to the affine slice/hyperplane $x_0 = 1$ (which is a copy of $\mathbb{F}^d$), its "origin" is the single point $[1 : 0 : \dots : 0]$. Most 2D planes through $(0,0,\dots,0)$ in $\mathbb{F}^{d+1}$ do not pass through $[1 : 0 : \dots : 0]$—they slice the $x_0 = 1$ flat space along offset lines that miss $[1 : 0 : \dots : 0]$. Inside $\mathbb{F}^d$, an offset line that misses the origin is no longer a vector subspace; it is a coset  $u + \langle v \rangle$.

## Hyperbolic Quadrics

Let $\mathbf{P}$ be a projective space. We call a set $\mathcal{S}$ of subspaces of $\mathbf{P}$ skew if no two distinct subspaces of $\mathcal{S}$ have a point in common. We also refer to these as skew subspaces.

Let $\mathcal{S}$ be a set of skew subspaces. A line is called a transversal of $\mathcal{S}$ if it intersects each subspace of $\mathcal{S}$ in a single point.

Let's test a single point $P$ on $g_1$ to see how many transversals can pass through it:

Take the point $P \in g_1$ and span it with the entire second line $g_2$. This creates a single flat 2D plane,  $\Pi = \langle P, g_2 \rangle$.
    
Now look at the third line $g_3$. In 3D projective space, a line ($g_3$) and a plane ($\Pi$) that does not contain it intersect in exactly one point, let's call it $R = \Pi \cap g_3$.
    
Draw the line connecting $P$ and $R$. Because both $P$ and $R$ lie inside the plane $\Pi = \langle P, g_2 \rangle$, the line $PR$ lies completely inside $\Pi$. And because two lines in the same plane must intersect, the line $PR$ is forced to intersect $g_2$ at some unique point $Q$.

This is a remarkable geometric constraint:  through every single point $P$ on $g_1$, there is one—and only one—straight line $h_P$ that hits both $g_2$ and $g_3$.

As you slide the point $P$ along $g_1$, this unique transversal line $h_P$ slides along $g_1, g_2,$ and $g_3$ simultaneously. Instead of filling the 3D volume, this 1-parameter family of straight lines [sweeps out a 2-dimensional curved saddle/hourglass surface](https://www.youtube.com/shorts/SoqpsRKFf6k) (in real space, a hyperboloid of one sheet, like a nuclear power plant cooling tower).

Now let $\mathbf{P}$ be a $3$-dimensional projective space over the division ring $F$. Let $\{g_1, g_2, g_3\}$ and $\{h_1, h_2, h_3\}$ be sets of skew lines with the property that each line $g_i$ meets each line $h_j$ i.e. $g_i$ is a transversal of $\{h\}$ and $h_i$ is a transversal of $\{g\}$. Then the following is true:

$F$ is commutative (hence a field) if and only if each transversal $g \notin \{g_1, g_2, g_3\}$ of $\{h_1, h_2, h_3\}$ intersects each transversal $h \notin \{h_1, h_2, h_3\}$ of $\{g_1, g_2, g_3\}$. (To picture this, think of a grid of $16$ points formed by $4$ horizontal lines $g_1, g_2, g_3$, and $g$, and $4$ vertical lines $h_1, h_2, h_3$, and $h$, where $g$ is a transversal of $h_1, h_2$, and $h_3$, and $h$ is a transversal of $g_1, g_2$, and $g_3$.) Essentially, what we are saying is that every transversal of $g$ will intersect every transversal of $h$ and form a "coordinate grid." This is called the 16-point theorem.

Now let $\mathbf{P}$ be a $3$-dimensional projective space. A nonempty set $\mathcal{R}$ of skew lines of $\mathbf{P}$ is called a regulus if the following are true:

Through each point of each line of $\mathcal{R}$ there is a transversal of $\mathcal{R}$.

Through each point of a transversal of $\mathcal{R}$ there is a line of $\mathcal{R}$.

It is clear that the set $\mathcal{R}'$ of all transversals of a regulus $\mathcal{R}$ again forms a regulus; we call it the opposite regulus of $\mathcal{R}$.

Notice that no two $h$-lines i.e. lines of the opposite regulus, ever touch each other (if they did, their plane would contain points of $g_1, g_2, g_3$, violating skewness). So $\mathcal{R}'$ is a family of mutually skew lines covering the surface.

Imagine taking a cylinder made of vertical straight rods arranged in a circle (none of the rods touch each other).
    
Now grab the top ring and twist it by $90^\circ$ clockwise while holding the bottom ring fixed to form a ruled surface that is essentially a "discretized" hyperboloid of one sheet.
    
Every rod remains completely straight, and because they all twist in the same direction around the outside of the central hole,  none of the rods ever collide. They pass each other at a distance around the open waist. That collection of twisted, non-touching rods is the regulus $\mathcal{R}$ (the "left-tilted" lines).
    
Now imagine you had twisted the top ring $90^\circ$  counter-clockwise instead. Those straight rods sweep out the exact same hourglass surface, also without ever touching one another. That second collection is the opposite regulus $\mathcal{R}'$ (the "right-tilted" lines).

The twist by angle $90^\circ$ is only an example. You can twist the top ring by any angle $\phi$ between $0^\circ$ and $180^\circ$ and the straight rods will always sweep out a valid hyperboloid of one sheet (a regulus).

What is the size of the hyperboloid throat. Suppose your top and bottom circular rims at $z = +H$ and $z = -H$ both have radius $R$. Take a single rod connecting angle $\theta = 0$ on the bottom rim to angle $\theta = \phi$ on the top rim. The bottom endpoint ($z = -H$):  $A = (R, \, 0, \, -H)$. The top endpoint ($z = +H$):  $B = (R \cos \phi, \, R \sin \phi, \, +H)$    

Where does this straight rod pass through the central waist plane $z = 0$? Exactly at the midpoint $M = \frac{1}{2}(A + B)$ between the top and bottom endpoints. 

$$M = \left( R \frac{1 + \cos \phi}{2}, \; R \frac{\sin \phi}{2}, \; 0 \right)$$.

Now calculate the distance $r_{\text{throat}}$ of this midpoint $M$ from the central $z$-axis $(0,0,0)$ using the half-angle trig identities ($1 + \cos \phi = 2\cos^2(\phi/2)$ and $\sin \phi = 2\sin(\phi/2)\cos(\phi/2)$):

$$r_{\text{throat}} = \sqrt{x_M^2 + y_M^2} = R \cdot \cos\left(\frac{\phi}{2}\right)$$

So if $\phi = 0^\circ$ (no twist), $\cos(0^\circ) = 1 \implies r_{\text{throat}} = R$. It is an untwisted cylinder; the lines are parallel and meet only at the single point at infinity (creating a degenerate cone/cylinder, not a regulus of skew lines).
    
If $0^\circ \text{ less than } \phi \text{ less than } 180^\circ$ (any intermediate twist), $0 < r_{\text{throat}} < R$. The lines are mutually skew and carve out an open circular throat of radius $R \cos(\phi/2)$.

At $\phi = 90^\circ$,  $r_{\text{throat}} = R \cos(45^\circ) = \frac{R}{\sqrt{2}} \approx 0.707 R$. At $\phi = 120^\circ$,  $r_{\text{throat}} = R \cos(60^\circ) = 0.5 R$ (the throat is exactly half the width of the top/bottom rims).
        
For $\phi = 180^\circ$ (half-turn twist), $\cos(90^\circ) = 0 \implies r_{\text{throat}} = 0$. Every rod connects $(x, y, -H)$ to $(-x, -y, +H)$, passing straight through the origin $(0,0,0)$. The throat pinches completely shut into a double cone, and the lines are no longer skew.

Also note while the height $H$ of the cylinder doesn't change the throat radius $r_{\text{throat}}$ at $z=0$, changing $H$ changes the slope of the rods—taller $H$ makes a tall, gentle hourglass; shorter $H$ makes a wide, flared hourglass.

A regulus has as many lines as there are points on a projective line ($\vert{}F\vert{} + 1$ lines). Over $\mathbb{R}$, there are infinitely many lines in $\mathcal{R}$ and infinitely many in $\mathcal{R}'$. Over a finite field $\mathbb{F}_q$, there are $q+1$ lines in $\mathcal{R}$ and $q+1$ lines in $\mathcal{R}'$, forming a $(q+1) \times (q+1)$ grid of $(q+1)^2$ points. 

In the 16-point theorem, we only talk of 16 points because, we start with three skew lines $g_1, g_2, g_3$ are fixed as your starting reference frame, and you pick three fixed transversals $h_1, h_2, h_3$ (which automatically gives $3 \times 3 = 9$ intersection points). Now, to prove that every line $g \in \mathcal{R}$ meets every line $h \in \mathcal{R}'$, you pick one arbitrary 4th transversal $g$ of $\{h_1, h_2, h_3\}$ (giving $3$ more intersection points) and one arbitrary 4th transversal $h$ of $\{g_1, g_2, g_3\}$ (giving $3$ more intersection points). You now have $9 + 3 + 3 = 15$ guaranteed intersections in a $4 \times 4$ grid. The theorem asks:  Must $g$ and $h$ intersect at that 16th corner?

Because $g$ and $h$ were chosen as arbitrary fourth transversals, proving that they must intersect at the 16th point proves that every transversal of $\{h_1, h_2, h_3\}$ intersects every transversal of $\{g_1, g_2, g_3\}$. A regulus exists if and only if that 16th intersection closes up for every choice of $g$ and $h$, which happens if and only if $F$ is commutative i.e. the order of multiplcation of two numbers doesn't matter.

Thus if $g_1, g_2, g_3$ be three skew lines of $\mathbf{P}$, there is exactly one regulus through $g_1, g_2$, and $g_3$ if $F$ is commutative. If $F$ is noncommutative, then there is no regulus in $\mathbf{P}$.

Now let $\mathbf{P}$ be a $3$-dimensional projective space over the field $F$ which is represented by homogeneous coordinates. Let:

$$\begin{aligned} g_1 &= \langle (1 : 0 : 0 : 0),\, (0 : 1 : 0 : 0) \rangle, \\ g_2 &= \langle (0 : 0 : 1 : 0),\, (0 : 0 : 0 : 1) \rangle, \\ g_3 &= \langle (1 : 0 : 1 : 0),\, (0 : 1 : 0 : 1) \rangle \end{aligned}$$

be three skew lines. Now lets figure out the condition on the set $\mathcal{Q}$ of points on the uniquely determined regulus $\mathcal{R}$ through $g_1, g_2, g_3$. This condition is:

$$\mathcal{Q} = \left\{(a_0 : a_1 : a_2 : a_3) \;\middle\vert{}\; a_0 a_3 = a_1 a_2 \text{ with } a_i \in F,\text{ not all } a_i = 0\right\}$$

Therefore, the coordinates of the points of $\mathcal{Q}$ satisfy the quadratic equation: $x_0 x_3 - x_1 x_2 = 0$. The surface $\mathcal{Q}$ is the hyperbolic quadric in $PG(3, F)$ (also known as the Segre quadric or Klein quadric in miniature). It demonstrates that you can construct and study a curved 2nd-degree algebraic surface ($x_0 x_3 - x_1 x_2 = 0$) using nothing but straight lines and incidence axioms (three skew lines and their transversals).

How does this condition come about? A line $h$ is a transversal of $\{g_1, g_2, g_3\}$ if it intersects $g_1$ at some point $P_1$,  $g_2$ at some point $P_2$, and $g_3$ at some point $P_3$.

Let's pick a scalar $b \in F$ to locate a point on $g_1$:

Take $(1, 0, 0, 0) + b(0, 1, 0, 0) = (1, b, 0, 0) \in g_1$.
    
Take the corresponding point on $g_2$:  $(0, 0, 1, 0) + b(0, 0, 0, 1) = (0, 0, 1, b) \in g_2$.
    
If you add those two vectors together, you get $(1, b, 1, b) = (1, 0, 1, 0) + b(0, 1, 0, 1)$, which lies directly on $g_3$!

Because $(1, b, 0, 0) \in g_1$,  $(0, 0, 1, b) \in g_2$, and their sum $(1, b, 1, b) \in g_3$, the line connecting them hits all three lines $g_1, g_2, g_3$. Thus, for every scalar $b \in F$, we get a transversal line $h_b$:

$$h_b = \langle (1 : b : 0 : 0),\, (0 : 0 : 1 : b) \rangle$$

To set up our $3 \times 3$ starting grid, we pick the three simplest values for $b$ (namely $b = 0$,  $b = 1$, and $b = \infty$, which corresponds to just taking the second basis vector):

$$\begin{aligned} h_1 \;(b=0) &= \langle (1 : 0 : 0 : 0),\, (0 : 0 : 1 : 0) \rangle \\ h_2 \;(b=\infty) &= \langle (0 : 1 : 0 : 0),\, (0 : 0 : 0 : 1) \rangle \\ h_3 \;(b=1) &= \langle (1 : 1 : 0 : 0),\, (0 : 0 : 1 : 1) \rangle \end{aligned}$$

Now leave $h_b$ (for an arbitrary scalar $b \in F$) as our 4th vertical line $h$:

$$h = h_b = \langle (1 : b : 0 : 0),\, (0 : 0 : 1 : b) \rangle$$

Now do the exact same thing in the opposite direction: find a 4th line $g_a$ (for an arbitrary scalar $a \in F$) that intersects $h_1, h_2,$ and $h_3$:

1.  Take $(1, 0, 0, 0) + a(0, 0, 1, 0) = (1, 0, a, 0) \in h_1$.
    
2.  Take $(0, 1, 0, 0) + a(0, 0, 0, 1) = (0, 1, 0, a) \in h_2$.
    
3.  Adding those two vectors gives $(1, 1, a, a) = (1, 1, 0, 0) + a(0, 0, 1, 1)$, which lies directly on $h_3$!
   
Thus, for any scalar $a \in F$, our fourth horizontal line $g$ (a transversal of $\{h_1, h_2, h_3\}$) is:

$$g = g_a = \langle (1 : 0 : a : 0),\, (0 : 1 : 0 : a) \rangle$$

Now we have our two 4th lines in 3D space:

Line $h_b$ spanned by $U_1 = (1, b, 0, 0)$ and $U_2 = (0, 0, 1, b)$.
    
Line $g_a$ spanned by $V_1 = (1, 0, a, 0)$ and $V_2 = (0, 1, 0, a)$.
    
Let's look at the coordinates of any point on $h_b$ versus any point on $g_a$ (normalized so the first coordinate is $1$):

Every point on $h_b$ with first coordinate $1$ is formed by taking $U_1$ and adding a left-scalar multiple $\lambda$ of $U_2$:

$$P_{h}(\lambda) = (1, b, 0, 0) + \lambda (0, 0, 1, b) = (1,\, b,\, \lambda,\, \lambda b)$$

Every point on $g_a$ with first coordinate $1$ is formed by taking $V_1$ and adding a left-scalar multiple $\mu$ of $V_2$:

$$P_{g}(\mu) = (1, 0, a, 0) + \mu (0, 1, 0, a) = (1,\, \mu,\, a,\, \mu a)$$

For the line $h_b$ and the line $g_a$ to intersect in 3D space, there must exist scalars $\lambda, \mu \in F$ such that the point $P_h(\lambda)$ on $h_b$ is the exact same point as $P_g(\mu)$ on $g_a$:

$$(1,\, b,\, \lambda,\, \lambda b) = (1,\, \mu,\, a,\, \mu a)$$

Compare the four coordinates slot by slot:

1st coordinate:  $1 = 1$ (matches).
    
2nd coordinate:  $b = \mu \implies \mu$  must equal $b$.
    
3rd coordinate:  $\lambda = a \implies \lambda$  must equal $a$.
    
4th coordinate: Substitute $\lambda = a$ into $\lambda b$, and substitute $\mu = b$ into $\mu a$:
    
$\text{Point on } h_b \text{ has 4th coordinate: } \lambda b = ab$
    
$\text{Point on } g_a \text{ has 4th coordinate: } \mu a = ba$
    
Look at what happened. To reach the intersection point along line $h_b$, you started with a vector containing $b$ and multiplied it on the left by $\lambda = a$, giving $(1 : b : a : \mathbf{ab})$. To reach the intersection point along line $g_a$, you started with a vector containing $a$ and multiplied it on the left by $\mu = b$, giving $(1 : b : a : \mathbf{ba})$.
    
Therefore if $ab = ba$ (the division ring $F$ is a commutative field), the two points $(1 : b : a : ab)$ and $(1 : b : a : ba)$ are identical, so the lines $h_b$ and $g_a$ intersect at that point.
    
If $ab \neq ba$ (for example, in the Quaternions $\mathbb{H}$ where $i \cdot j = k$ but $j \cdot i = -k$), the point on $h_b$ is $(1 : j : i : k)$ while the point on $g_a$ is $(1 : j : i : -k)$. Because $k \neq -k$, the two lines pass right by each other in 3D space without touching!

This is pretty much the same as differential geometry, where if you have two vector fields $X$ and $Y$ in 3D space, you can flow along $X$ by distance $a$ and then along $Y$ by distance $b$, or flow along $Y$ by $b$ and then along $X$ by $a$. Do those two paths land on the exact same 4th corner to weave a 2D coordinate grid (a surface)? Only if the Lie bracket vanishes ($[X, Y] = XY - YX = 0$, or $\partial_x \partial_y = \partial_y \partial_x$). If not, the 4th corner fails to close, and the flows twist into 3D volume instead of staying on a 2D surface.
    
Both the projective geometry and the differential geometry observations are two manifestations of the exact same structural principle: integrability (closure of a 2D mesh in a 3D+ space).

In higher dimensions, hyperbolic quadrics (like $x_0 x_5 - x_1 x_4 + x_2 x_3 = 0$ in $PG(5, F)$—the Klein Quadric) are completely ruled not just by straight lines ($1$D subspaces), but by entire flat planes ($2$D subspaces), called generators. Specifically, the Klein quadric in 5D space is woven from two opposite families of flat 2D planes (often called $\alpha$-planes and $\beta$-planes), directly generalizing the two reguli $\mathcal{R}$ and $\mathcal{R}'$ of lines in 3D. The expression $x_0 x_5 - x_1 x_4 + x_2 x_3 = 0$ comes directly from the wedge product (exterior algebra), and the determinant used in the area of a parallelogram or traingle (specifically,  $2 \times 2$ minors and the Laplace cofactor expansion). It is related to the Pfaffian of a $4 \times 4$ skew-symmetric matrix.
    
Also, the mapping $(1 : a) \times (1 : b) \mapsto (1 : b : a : ab)$ is the simplest case of the Segre Embedding $\mathbb{P}^1 \times \mathbb{P}^1 \hookrightarrow \mathbb{P}^3$, which embeds the product of two lines as a curved quadric in 3D space. In general, you can embed $\mathbb{P}^n \times \mathbb{P}^m$ into $\mathbb{P}^{(n+1)(m+1)-1}$ using $x_{ij} = a_i b_j$.

What we showed in this section bridges three seemingly distinct areas of mathematics—pure incidence geometry (skew lines and transversals),  abstract algebra (whether multiplication in the coordinate division ring $F$ is commutative:  $ab = ba$), and algebraic geometry (curved quadratic surfaces, or quadrics).

### What Does A Hyperbolic Quadric Look Like?
What it "looks like" depends on whether you view it in projective space, an affine slice, or over a finite field.

In 3D Projective Space $PG(3, F)$ (over any field), there is no distinction between "finite" points and "points at infinity." The regulus $\mathcal{R}$ and opposite regulus $\mathcal{R}'$ form a completely symmetric, closed grid:  $\mathbb{P}^1(F) \times \mathbb{P}^1(F)$.
    
Over $\mathbb{R}$, a projective line $\mathbb{P}^1(\mathbb{R})$ is a closed circle $S^1$ (a line whose two ends meet at the point at infinity). Thus, in $PG(3, \mathbb{R})$, the surface is topologically a torus ($S^1 \times S^1$).
        
Over a finite field $\mathbb{F}_q$, a projective line $\mathbb{P}^1(\mathbb{F}_q)$ is a discrete set of $q+1$ points. Thus, in $PG(3, q)$, the hyperbolic quadric $Q^+(3, q)$ is literally a finite $(q+1) \times (q+1)$ combinatorial grid of $(q+1)^2$ points, woven from $q+1$ skew lines of $\mathcal{R}$ and $q+1$ skew lines of $\mathcal{R}'$. There is no continuous "curvature" in a finite field, yet every algebraic and incidence property of the hyperboloid (every line of $\mathcal{R}$ meets every line of $\mathcal{R}'$, tangent planes cut out a pair of intersecting lines, etc.) holds identically!
        
In 3D Affine Space (When You Slice Away a Plane at Infinity), depending on which plane you choose as the plane at infinity in $PG(3, \mathbb{R})$, the exact same projective regulus $x_0 x_3 - x_1 x_2 = 0$ appears as two different familiar 3D surfaces:
    
**Hyperboloid of One Sheet ($x^2 + y^2 - z^2 = 1$):** If you choose a plane at infinity that does _not_ contain any lines of the regulus (it cuts the quadric in an ellipse at infinity), the affine remainder is the hourglass hyperboloid of one sheet.
        
**Hyperbolic Paraboloid / Pringles Saddle ($z = xy$):** Look directly at $x_0 x_3 - x_1 x_2 = 0$ and set the affine plane at infinity to be $x_0 = 0$. Normalizing $x_0 = 1$ and writing $(x_1, x_2, x_3) = (x, y, z)$ gives **$z = xy$**! Why does it look like a saddle instead of an hourglass? Because the plane at infinity $x_0 = 0$ is _tangent_ to the quadric and contains two lines of the reguli (pushing the closed waist out to infinity). Projectively, the hourglass ($x^2 + y^2 - z^2 = 1$) and the saddle ($z = xy$) are the exact same geometric object.

Note that in a finite field $\mathbb{F}_q$, the continuous trigonometric formulas ($\cos \phi$, $\sin \phi$, Euclidean distance $\sqrt{x^2+y^2}$) do not hold because finite fields have no concept of angles, ordering ("less than" or "greater than"), or real-valued square-root lengths.

However, the algebraic counterparts of the cylinder, the twist, the throat, and the pinching into a cone all hold with 100% precision in $\mathbb{F}_q$. Instead of a smooth, curved hourglass, a finite field generates a discrete $(q+1) \times (q+1)$ combinatorial incidence grid that obeys the exact same intersection laws as the real hyperboloid.

For example, in the real 3D model, we used $\cos \phi$ and $\sin \phi$ to create the twist because we wanted the top and bottom cross-sections to be Euclidean circles ($x^2 + y^2 = R^2$).

In projective geometry over any field $F$ (including $\mathbb{F}_q$), we don't need trigonometry to twist a line. We can write the family of lines using a purely algebraic "twist parameter" $k \in F$.

For each parameter $t \in F$ (which selects which rod you are looking at around the rim), connect a point on the bottom plane to a "twisted" point on the top plane:
* Regulus $\mathcal{R}_k$ (twisted by $+k$): Connect $(1 : t : 0 : 0)$ to $(0 : 0 : 1 : k t)$.
* Opposite Regulus $\mathcal{R}'_k$ (twisted by $-k$): Connect $(1 : s : 0 : 0)$ to $(0 : 0 : k s : 1)$.

Every point on the $t$-th line of $\mathcal{R}_k$ is a linear combination $(1 : t : \lambda : \lambda k t)$. Notice that its coordinates $(x_0 : x_1 : x_2 : x_3)$ satisfy the quadratic equation:

$$x_3 x_0 - k x_1 x_2 = 0 \quad \Longleftrightarrow \quad \det \begin{pmatrix} x_0 & x_1 \\ k x_2 & x_3 \end{pmatrix} = 0$$

Look at what the scalar $k \in \mathbb{F}_q$ does—it acts just like the twist angle $\phi$, without a single trig function:

| Real Twisted Cylinder ($\phi$) | Finite Field Algebraic Twist ($k \in \mathbb{F}_q$) | Geometric Result in $PG(3, q)$ |
| --- | --- | --- |
| $0^\circ \text{ less than } \phi \text{ less than } 180^\circ$ (Open throat: $r_{\text{throat}} \neq 0$) | $k \neq 0$ (Non-zero determinant) | Non-degenerate Hyperbolic Quadric $Q^+(3, q)$: The $q+1$ lines are mutually skew. None of them touch each other, and there is no "pinch point." |
| $\phi = 180^\circ$ (Pinched throat: $r_{\text{throat}} = 0$) | $k = 0$ (Zero determinant: $x_0 x_3 = 0$) | Degenerate Pinch: Every line $(1 : t : \lambda : 0)$ passes through the exact same pinch point $P = (0 : 0 : 1 : 0)$! Skewness collapses completely, just like at $\phi = 180^\circ$. |
---

What replaces the "throat" and "curvature" in a Finite Field? In $\mathbb{F}_q$, you cannot measure the "narrowest waist radius" in millimeters because there is no Euclidean metric. Yet the geometric signature of curvature—how flat planes slice the surface—is identical in $\mathbb{R}$ and $\mathbb{F}_q$.

If you take the finite point-set $\mathcal{Q} = \{ (x_0 : x_1 : x_2 : x_3) \in PG(3, q) \mid x_0 x_3 - x_1 x_2 = 0 \}$, it consists of exactly $(q+1)^2$ points. Why do mathematicians still call this discrete cloud of $(q+1)^2$ points a "curved quadric surface"? Because of what happens when you slice it with any 2D plane $\Pi$ in $PG(3, q)$:

1. No 3 Collinear Points Outside the Rulings: If you pick a line in $PG(3, q)$ that is *not* one of the $2(q+1)$ lines of $\mathcal{R} \cup \mathcal{R}'$, that line can hit $\mathcal{Q}$ in at most $2$ points (because a degree-2 equation $x_0 x_3 - x_1 x_2 = 0$ has at most $2$ roots!). That is the finite-geometry definition of "curved": a line that isn't part of the ruling pierces in and pierces out in at most $2$ points.
2. Horizontal Slices ("The Throat and Rims"): If you slice $\mathcal{Q}$ with a plane $\Pi$ that is not tangent to $\mathcal{Q}$, the intersection $\Pi \cap \mathcal{Q}$ is a non-degenerate conic (an oval of $q+1$ points in the plane $\Pi$ where no three points are collinear).
   * In $\mathbb{R}$, slicing the hyperboloid horizontally gives a circle/ellipse (the circular throat and rims).
   * In $\mathbb{F}_q$, slicing $\mathcal{Q}$ with a non-tangent plane gives a finite conic (an oval of $q+1$ points), and every single one of the $q+1$ lines in $\mathcal{R}$ pierces that oval in exactly $1$ point!

3. Tangent Plane Slices: If you pick any point $P \in \mathcal{Q}$ and take the tangent plane $\Pi_P$ at $P$, the plane slices $\mathcal{Q}$ in exacty two intersecting lines: the unique line $g \in \mathcal{R}$ through $P$ and the unique line $h \in \mathcal{R}'$ through $P$ (which contains $2q+1$ points).

As an example, let's look at a regulus in the smallest field $PG(3, 2)$, $\mathbb{F}_2 = \{0, 1\}$ ($q = 2$).

The entire 3D projective space $PG(3, 2)$ has $2^3 + 2^2 + 2 + 1 = 15$ points and $35$ lines. Each line has $q + 1 = 3$ points. A regulus $\mathcal{R}$ consists of $q + 1 = 3$ skew lines: $\{g_1, g_2, g_3\}$. The opposite regulus $\mathcal{R}'$ consists of $q + 1 = 3$ skew transversals: $\{h_1, h_2, h_3\}$. Together, they form a $3 \times 3$ grid of $(2+1)^2 = 9$ points satisfying $x_0 x_3 - x_1 x_2 = 0 \pmod 2$:

|  | $h_1 \in \mathcal{R}'$ | $h_2 \in \mathcal{R}'$ | $h_3 \in \mathcal{R}'$ |
| --- | --- | --- | --- |
| $g_1 \in \mathcal{R}$ | $(1:0:0:0)$ | $(0:1:0:0)$ | $(1:1:0:0)$ |
| $g_2 \in \mathcal{R}$ | $(0:0:1:0)$ | $(0:0:0:1)$ | $(0:0:1:1)$ |
| $g_3 \in \mathcal{R}$ | $(1:0:1:0)$ | $(0:1:0:1)$ | $(1:1:1:1)$ |

Look at that $3 \times 3$ table of $9$ points inside the 15-point space $PG(3, 2)$:

* Rows are $g_1, g_2, g_3 \in \mathcal{R}$: Each row is a valid 3-point projective line in $PG(3, 2)$ (the 3rd point is the binary sum of the first two!). None of the rows share a point (they are skew).

* Columns are $h_1, h_2, h_3 \in \mathcal{R}'$: Each column is also a valid 3-point projective line in $PG(3, 2)$ (the 3rd point is the binary sum of the top two!).

* Every row meets every column in 1 point: That is the entire doubly ruled "hyperboloid" $Q^+(3, 2)$.

* Where are the "circular rims/throat" in this $3 \times 3$ grid? Pick $3$ points from the table with no two in the same row or column—for example, the diagonal $\{(1:0:0:0),\, (0:0:0:1),\, (1:1:1:1)\}$, plus $(0:1:1:0)$ outside the quadric. A plane cutting across the three lines $g_1, g_2, g_3$ without containing any of them hits one point in each row, forming a 3-point finite conic ("circle") that the three skew lines pass through.

### Hyperbolic Quadrics & 3D Projective Spaces
In projective geometry, $d = 3$ is the "Goldilocks dimension" where lines can be skew and where three skew lines uniquely lock transversals into a 2D surface.

When$d = 2$, a plane, skew lines cannot exist ($\dim(g \cap h) = 1 + 1 - 2 = 0$, so any two lines must intersect). In $d = 3$ (3-Space), two lines have codimension $2$ each, so they typically miss each other. A plane ($2$D) and a line ($1$D) always meet at a point ($2 + 1 - 3 = 0$). Therefore, $3$ skew lines uniquely determine a 1-parameter family of transversals (a 2D surface). If $d \ge 4$, for example in 4D space, a plane ($2$D) and a line ($1$D) generally miss each other completely ($2 + 1 - 4 = -1$). If you pick three skew lines in 4D space, there is typically only one single transversal line (or none) in total, rather than a continuous surface of them. Thus, the classical regulus of lines is an intrinsically 3-dimensional phenomenon.

If a regulus of lines only works in 3D, how do we get hyperbolic quadrics in higher dimensions? We noted that in $d = 3$, a line ($\dim = 1$) is guaranteed to intersect a plane ($\dim = 2$) in a point because $1 + 2 - 3 = 0$. In higher odd-dimensional projective spaces $PG(2m-1, F)$, the exact same intersection guarantee holds—not between two lines, but between $(m-1)$-dimensional subspaces.

In $PG(5,F)$ where $d=5$ for example, the equation becomes $x_0 x_5 - x_1 x_4 + x_2 x_3 = 0$. A regulus is woven from two families of flat 2D planes ($\alpha$-planes and $\beta$-planes). 

In general, if $d = 2m - 1$ in $PG(2m-1, F)$, the equation is $\sum_{i=1}^{m} x_{i} y_{i} = 0$. The regulus is woven from two families of $(m-1)$-dimensional flat subspaces. In general, a quadric in $PG(2m-1, F)$ is called hyperbolic (denoted $Q^+(2m-1, F)$) because it is the unique type of non-degenerate quadric that is completely ruled by flat $(m-1)$-dimensional projective subspaces (the maximum possible dimension of a flat subspace that can sit inside a $(2m-2)$-dimensional curved surface).

## Quadratic Sets

Just as earlier we defined projective spaces purely using points and lines before proving they come from vector spaces, Buekenhout’s synthetic theory of quadrics allows us to define degree-2 curved surfaces (quadrics) purely using point-line incidence rules—without writing a single quadratic equation or taking a single derivative.

A quadric is defined by a homogeneous degree-2 polynomial equation in coordinates. This requires the space to already have coordinates over a commutative field $F$. A Quadratic Set is defined purely by how straight lines intersect the point set $\mathcal{Q}$, with no coordinates, no equations, and no calculus.

Why do this? It allows us to study quadrics in non-Desarguesian planes or over finite fields (including characteristic $2$, where $1+1=0$ breaks standard calculus derivatives) using only clean geometric arguments.

Every algebraic quadric automatically satisfies the two axioms of a quadratic set, which we will define below. And remarkably, the converse is more or less true: in finite projective spaces of dimension $d \ge 3$, almost every quadratic set is an algebraic quadric.

Let $\mathcal{Q}$ be a set of points of the projective space $\mathbf{P}$. We call a line $g$ a tangent of $\mathcal{Q}$ if either $g$ has just one point in common with $\mathcal{Q}$ or each point of $g$ is contained in $\mathcal{Q}$. If a tangent $g$ has just one point $P$ in common with $\mathcal{Q}$, then one calls $g$ a tangent of $\mathcal{Q}$ at the point $P$. A line $g$ with the property that each point of $g$ lies in $\mathcal{Q}$ is also called a $\mathcal{Q}$-line. In general, we call a subspace $U$ a $\mathcal{Q}$-subspace if each point of $U$ lies in $\mathcal{Q}$.
    
For each point $P$ of $\mathcal{Q}$, let the set $\mathcal{Q}_P$ consist of the point $P$ and all points $X \neq P$ of $\mathbf{P}$ such that the line $XP$ is a tangent of $\mathcal{Q}$. One calls $\mathcal{Q}_P$ the tangent space of $\mathcal{Q}$ at the point $P$.

### Visualizing The Tangent Plane

When you place a tangent plane against a sphere at a point $P$, the entire sphere stays on one side of the plane, so the plane only touches the sphere at that single point $P$.

On a hyperbolic quadric (which is shaped like a saddle or hourglass at every point $P$), the surface curves away from the plane in one direction (up/down along the hourglass) and curves _into_ the plane in the perpendicular direction (around the waist). Because of this saddle shape, the flat tangent plane $\mathcal{Q}_P = \langle g, h \rangle$ cannot stay strictly on the outside of the hourglass—it physically cuts right through the wall of the hourglass, dividing the surface into pieces in front of the plane and behind the plane.

### Axioms of Quadratic Sets
    
We call the set $\mathcal{Q}$ a quadratic set of $\mathbf{P}$ if it satisfies the following conditions:
    
If-three-then-all axiom: Any line $g$ that contains at least three points of $\mathcal{Q}$ is totally contained in $\mathcal{Q}$ (which means that each point of $g$ lies in $\mathcal{Q}$). In other words, any line has $0$,  $1$,  $2$, or all points in common with $\mathcal{Q}$. Note that a line that meets $\mathcal{Q}$ in $2$ points is called a secant.
        
Tangent-space axiom: For any point $P \in \mathcal{Q}$, its tangent space $\mathcal{Q}_P$ is the set of points in a hyperplane or the set of all points of $\mathbf{P}$. One can also express the important tangent-space axiom as follows. For any point $P$ of $\mathcal{Q}$, either $\mathcal{Q}_P$ is a hyperplane, which means any line through $P$ in $\mathcal{Q}_P$ is a tangent, and no line through $P$ outside $\mathcal{Q}_P$ is a tangent (each such line contains exactly one further point of $\mathcal{Q}$). Or, $\mathcal{Q}_P$ is equal to $\mathbf{P}$, and so each line through $P$ is a tangent.

### The First Axiom

Let's take a closer look at the first axiom. Look at how the "If-three-then-all" axiom captures "degree 2" without algebra. If you intersect a straight line (parameterized by $t$) with an algebraic surface defined by a degree-2 polynomial $f(t) = a t^2 + b t + c = 0$, how many solutions can a quadratic equation have? $0$ solutions (the line misses the surface—a passant), $1$ solution (a double root $b^2 - 4ac = 0$—the line touches at $1$ point), $2$ solutions (two distinct roots—the line pierces in and pierces out, a secant), or more than $2$ solutions. But, the only way a quadratic polynomial $a t^2 + b t + c = 0$ can have 3 roots is if $a = b = c = 0$, meaning $f(t) = 0$ for all $t$, which means the entire line lies inside the surface since it is parametrized by $t$ i.e. we create the line by varying $t$.

How can an entire tangent line lie in a quadric. In 2D Euclidean geometry, we only study curves like circles ($x^2 + y^2 = 1$), which cannot contain straight lines, so we learn that a tangent line touches at $1$ point. Move to 3D Euclidean geometry and look at two surfaces we already know: a Cylinder ($x^2 + y^2 = 1$) or our Hyperboloid of One Sheet ($x^2 + y^2 - z^2 = 1$).

Because the hyperbolic quadric in 3D space is a doubly ruled surface, it is made of straight lines, so the idea that a straight line is entirely contained in the surface is not that odd. 

For example, take a point $P$ on the side of a smooth vertical cylinder, and place a flat sheet of metal (the Euclidean tangent plane $\Pi_P$) flush against the cylinder at $P$. Because the cylinder is made of vertical straight lines, that vertical line in the tangent plane rests flush against the cylinder along its entire infinite length. Every point of that vertical line is in $\mathcal{Q}$.

The exact same thing happens on the hyperboloid of one sheet (our regulus $\mathcal{Q}$). At any point $P \in \mathcal{Q}$, the calculus tangent plane $\Pi_P$ contains one line $g \in \mathcal{R}$ and one line $h \in \mathcal{R}'$ passing through $P$. Every other line in $\Pi_P$ through $P$ meets the hyperboloid only at $P$ ($1$ point). The two lines $g$ and $h$ lie inside $\Pi_P$, and they lie completely inside $\mathcal{Q}$ (all points).

 In fact, a $\mathcal{Q}$-line is simply the synthetic-geometry name for a ruling (or generator) of a surface: a straight line every single point of which lies inside $\mathcal{Q}$.

If we did not count $\mathcal{Q}$-lines (lines completely inside $\mathcal{Q}$) as "tangent lines," then the tangent plane $\Pi_P$ to a cylinder would have a missing vertical line ripped out of it, and the tangent plane to a hyperboloid would have two missing lines ($g$ and $h$) ripped out of it. By defining a tangent line as meeting $\mathcal{Q}$ in either $1$ point OR all points, the union of all tangent lines through $P$ forms a complete, unbroken flat hyperplane $\mathcal{Q}_P$.

### How $\mathcal{Q}$-Lines Classify All 3D Quadratic Sets

Counting how many $\mathcal{Q}$-lines pass through a point $P \in \mathcal{Q}$ (and how they sit inside the tangent plane $\mathcal{Q}_P$) is how projective geometry classifies all non-empty quadratic sets in 3D space:

| 3D Quadratic Set $\mathcal{Q}$ | Ruled Surface? | Number of $\mathcal{Q}$-Lines Through a Point $P \in \mathcal{Q}$ | How the Tangent Space $\mathcal{Q}_P$ Intersects $\mathcal{Q}$ |
| --- | --- | --- | --- |
| Elliptic Quadric (e.g., Sphere / Ellipsoid) | No (contains no straight lines) | $0$ $\mathcal{Q}$-lines | $\mathcal{Q}_P \cap \mathcal{Q} = \{P\}$ (the tangent plane touches $\mathcal{Q}$ only at the single point $P$; every line in $\mathcal{Q}_P$ through $P$ is a 1-point tangent). |
| Cone / Cylinder (Degenerate / Parabolic) | Singly Ruled | $1$ $\mathcal{Q}$-line (for smooth points $P \neq V$) | $\mathcal{Q}_P \cap \mathcal{Q} = g$ (the tangent plane touches $\mathcal{Q}$ along a single ruling line $g$ connecting $P$ to the vertex $V$). |
| Hyperbolic Quadric (Regulus / Hyperboloid of 1 sheet) | Doubly Ruled | $2$ $\mathcal{Q}$-lines ($g \in \mathcal{R}$ and $h \in \mathcal{R}'$) | $\mathcal{Q}_P \cap \mathcal{Q} = g \cup h$ (the tangent plane slices $\mathcal{Q}$ right along the two intersecting straight rulings $g$ and $h$ through $P$; every other line in $\mathcal{Q}_P$ through $P$ touches $\mathcal{Q}$ only at $P$). |
| Union of Two Planes ($H_1 \cup H_2$) | Completely Flat Pieces | A full pencil of $\mathcal{Q}$-lines | For $P \in H_1 \setminus H_2$, $\mathcal{Q}_P = H_1$, and *every* line through $P$ inside $H_1$ is a $\mathcal{Q}$-line. |

Notice the third row: for a hyperbolic quadric, if you take any point $P \in \mathcal{Q}$, its two rulings $g \in \mathcal{R}$ and $h \in \mathcal{R}'$ intersect at $P$, which means they span a 2D plane $\langle g, h \rangle$. Because both $g$ and $h$ are $\mathcal{Q}$-lines, they are both tangents at $P$, so the plane $\langle g, h \rangle$ they span is the tangent plane $\mathcal{Q}_P$ at $P$.

### The Second Axiom

Now let's look at the second axiom. In 3D Euclidean geometry, imagine standing at the North Pole $P$ of a hollow glass sphere $\mathcal{Q}$, if you shoot a line straight horizontally in any compass direction at the North Pole, the laser skims the top of the glass sphere at only $1$ point ($P$). Those horizontal rays are all tangents. And what do all horizontal rays through the North Pole sweep out? A single flat 2D plane—the tangent hyperplane $\mathcal{Q}_P$.

What if we shoot a line anywhere outside that horizontal plane (tilted downward into the sphere, or tilted upward, which extends backward into the sphere)? The line goes into the interior of the glass sphere and must exit through the glass wall at one second point $Q \neq P$. That makes it a 2-point secant line, so it is not in $\mathcal{Q}_P$.

That is the entire physical meaning of the Tangent-Space Axiom. If $P$ is a smooth (called non-singular) point of $\mathcal{Q}$ (like any point on a sphere or hyperboloid), the tangent lines through $P$ sweep out a flat hyperplane $\mathcal{Q}_P$ (the classical tangent plane). Every line through $P$ that is not in that tangent plane pierces the surface and hits $\mathcal{Q}$ at one additional point.

If $P$ is a sharp pinch / singular vertex of $\mathcal{Q}$ then $\mathcal{Q}_P = \mathbf{P}$, the whole space. Imagine a double cone with its sharp tip (vertex) at $V$. Stand at the vertex $V$ and shoot a line in any direction in 3D space. If you shoot along the wall of the cone, the entire line lies in the cone ($\mathcal{Q}$-line $\implies$ tangent). If you shoot in any other direction through $V$, the line only touches the cone right at the tip $V$ ($1$ point $\implies$ tangent). No line through the vertex $V$ can ever be a 2-point secant. Therefore, every line through the vertex $V$ is a tangent line, which means the tangent space $\mathcal{Q}_V$ is the entire 3D space $\mathbf{P}$.

In fact, this gives a purely geometric definition of a singular point (pinch/vertex): a point $P \in \mathcal{Q}$ is singular if and only if $\mathcal{Q}_P = \mathbf{P}$.

### Examples of Quadratic Sets

The empty set, any set consisting of just one point, the set of points on a line,  $\dots$, in short: the set of all points of a subspace is a quadratic set. These quadratic sets $\mathcal{Q}$ have the property that for each point $P \in \mathcal{Q}$ the set $\mathcal{Q}_P$ equals $\mathbf{P}$.

Why is the set of all points of a subspace $U$ a quadratic set? Suppose $\mathcal{Q} = U$ is a flat linear subspace of $\mathbf{P}$ (for example, $\mathcal{Q}$ is a single point, or a single straight line, or a single flat plane in 3D space). 

Let's check the "If-three-then-all" axiom. Suppose a line $g$ contains $3$ points of the subspace $U$. By definition of a linear subspace, if a line has even $2$ points in $U$, the entire line $g$ lies inside $U$, because a line is essentially parametrized by a variable $\lambda$ and two points - $a + \lambda b$. So a line can only meet a subspace $U$ in $0$ points, $1$ point, or all points, it can never meet a flat subspace in just $2$ points. Thus, the first axiom is trivially satisfied.

This same logic also assures satisfying the Tangent-Space axiom and why $\mathcal{Q}_P = \mathbf{P}$. Pick any point $P \in U$, and take any line $g$ in the entire space $\mathbf{P}$ that passes through $P$. How many points can $g$ share with $U$? Since $P$ is already on both $g$ and $U$, they share at least $1$ point ($P$). If $g$ shares no other points with $U$, then $\vert{}g \cap U\vert{} = 1 \implies g$ is a tangent. If $g$ shares even one more point with $U$, then because $U$ is a subspace, all points of $g$ lie in $U \implies g$ is a $\mathcal{Q}$-line $\implies g$ is also a tangent.

Because a line through $P \in U$ can never intersect a flat subspace $U$ in exactly $2$ points, every single line in $\mathbf{P}$ passing through $P$ is a tangent to $U$. Therefore, for every $P \in U$, the tangent space $\mathcal{Q}_P$ is the entire ambient space $\mathbf{P}$, satisfying the second axiom.
    
Other examples of quadratic sets include $\mathcal{Q}$, which consists of the points in the union of two hyperplanes $H_1, H_2$ of $\mathbf{P}$. For each point $P \in H_1 \cap H_2$ we have that $\mathcal{Q}_P$ consists of all points of $\mathbf{P}$, while the points $P \in H_i \setminus (H_1 \cap H_2)$ satisfy $\mathcal{Q}_P = H_i$ ($i = 1, 2$).
    
From elementary geometry we immediately get examples. Each circle (and each ellipse) in the Euclidean plane is a quadratic set. (Here the tangent spaces are just lines.) Also, the sphere in $3$-dimensional (or $d$-dimensional) real affine space is a quadratic set. In real $3$-dimensional space there exist two other, quite different quadratic sets. These are, first of all, the cones; here, there is a point $V$, the vertex of the cone, such that $\mathcal{Q}_V$ is the whole space. Finally, there is the hyperbolic quadric.

### Properties of Quadratic Sets

The radical $\text{Rad}(\mathcal{Q})$ is the set of all singular points of $\mathcal{Q}$—meaning all points $S \in \mathcal{Q}$ whose tangent space is the entire ambient space ($\mathcal{Q}_S = \mathbf{P}$). 

In geometry, a quadratic set $\mathcal{Q}$ is called nondegenerate if $\text{Rad}(\mathcal{Q}) = \emptyset$ (it has no singular pinch points at all—like a smooth sphere or a hyperbolic quadric). It is degenerate if $\text{Rad}(\mathcal{Q}) \neq \emptyset$ (it has at least one singular point—like a cone or a cylinder).

Now let $\mathcal{Q}$ be a quadratic set of $\mathbf{P}$. 

> Then the radical of $\mathcal{Q}$ is a linear subspace of $\mathbf{P}$.

> Let $U$ be a complement of $\text{Rad}(\mathcal{Q})$ (that is, a subspace $U$ such that $U \cap \text{Rad}(\mathcal{Q}) = \emptyset$ and $\langle U, \text{Rad}(\mathcal{Q}) \rangle = \mathbf{P}$). Then $\mathcal{Q}' := \mathcal{Q} \cap U$ is a nondegenerate quadratic set of $U$.

>$\mathcal{Q}$ can be described as follows: $\mathcal{Q}$ consists of all points that lie on lines that join a point of $\text{Rad}(\mathcal{Q})$ with a point of $\mathcal{Q}' = \mathcal{Q} \cap U$.

These 3 points prove that every degenerate quadratic set is simply a cone (or cylinder) built over a smaller, smooth nondegenerate quadratic set.

Picture a double cone $\mathcal{Q}$ in 3D space with its sharp vertex at the point $V$. What is the radical? What is the only singular point of the cone $\mathcal{Q}$? The vertex $V$. So $\text{Rad}(\mathcal{Q}) = \{V\}$ (a $0$-dimensional subspace).
    
What is the complement $U$ and base $\mathcal{Q}'$? Pick a flat subspace $U$ of maximal dimension that completely misses the vertex $V$. Since $V$ is a point ($0$D) in 3D space, a complement $U$ is any 2D plane that does not pass through $V$ (for instance, a horizontal plane below the vertex). Now intersect the cone $\mathcal{Q}$ with that flat plane $U$. What do you get when you slice a cone horizontally with a plane $U$ that misses the vertex?  A smooth circle/ellipse (conic) $\mathcal{Q}'$ inside the plane $U$. Because that circle $\mathcal{Q}'$ has no sharp pinch points,  $\mathcal{Q}'$ is a nondegenerate quadratic set inside the plane $U$.
    
Now how do you rebuild the entire 3D cone $\mathcal{Q}$ starting only from the vertex $\text{Rad}(\mathcal{Q}) = \{V\}$ and the flat circle $\mathcal{Q}'$ down in the plane $U$? You draw a straight line from the vertex $V$ to every point $X$ on the circle $\mathcal{Q}'$! The set of all points on all those connecting lines $VX$ is the entire 3D cone $\mathcal{Q}$.

Now let $\mathcal{Q}$ be a quadratic set of $\mathbf{P}$. If $\mathcal{Q}$ is nondegenerate, then for any two distinct points $P, R \in \mathcal{Q}$ we have $\mathcal{Q}_P \neq \mathcal{Q}_R$. 

In other words, the quadratic set that is induced by $\mathcal{Q}$ in a tangent space $\mathcal{Q}_P$ has a radical that consists of just one point, namely $P$.

First, what does quadratic set induced by $\mathcal{Q}$ in $\mathcal{Q}_P$ mean? $\mathcal{Q}$ is our original 3D quadratic set in the 3D space $\mathbf{P}$. Pick a point $P \in \mathcal{Q}$. Because $\mathcal{Q}$ is nondegenerate, the tangent space $\mathcal{Q}_P$ is a 2D hyperplane (a flat plane). 

Now forget the rest of 3D space and look only inside the 2D flat plane $\mathcal{Q}_P$. Which points of $\mathcal{Q}$ lie inside this 2D plane $\mathcal{Q}_P$? The intersection $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$. 

This intersection is the quadratic set induced by $\mathcal{Q}$ in the tangent space $\mathcal{Q}_P$. Viewed as a set of points inside the 2D plane $\mathcal{Q}_P$, it satisfies the quadratic set axioms inside $\mathcal{Q}_P$. 

Why does this intersection have a radical equal to $\{P\}$? When we intersect the tangent plane $\mathcal{Q}_P$ with a smooth 3D surface $\mathcal{Q}$, let's say a hyperbolic quadric (think of an hourglass) $\mathcal{Q}$ with its tangent plane $\mathcal{Q}_P$ at $P$, what is the 2D cross-section $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$?

It is an X-shaped cross of two intersecting lines $g \cup h$ meeting at $P$. Inside the 2D plane $\mathcal{Q}_P$, is an X-shaped pair of intersecting lines $g \cup h$ a smooth conic, or is it a degenerate 1D cone whose vertex is the crossing point $P$? It is degenerate, with vertex $P$. Inside the plane $\mathcal{Q}_P$, every line passing through $P$ is either $g$ (all points in $\overline{\mathcal{Q}}$), $h$ (all points in $\overline{\mathcal{Q}}$), or touches $g \cup h$ only at the crossing point $P$ ($1$ point in $\overline{\mathcal{Q}}$)!

Therefore, for the 2D slice $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$ living inside the plane $\mathcal{Q}_P$, the point $P$ is a singular vertex and $\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$.

On a Sphere / Elliptic Quadric $\mathcal{Q}$, when you slice a sphere $\mathcal{Q}$ with its tangent plane $\mathcal{Q}_P$ at $P$, what is the 2D cross-section $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$? It is just the single point $\{P\}$.

Inside the plane $\mathcal{Q}_P$, every line through $P$ meets $\{P\}$ in $1$ point, so $P$ is a singular point of that cross-section: $\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$

Now why did we say "In Other Words..." in the second paragraph of the theorem and linking $\mathcal{Q}_P \neq \mathcal{Q}_R$ to $\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$?

What does it mean for a point $R \in \mathcal{Q} \cap \mathcal{Q}_P$ to be in the radical of the slice $\mathcal{Q} \cap \mathcal{Q}_P$? It means that every line through $R$ inside the plane $\mathcal{Q}_P$ is tangent to $\mathcal{Q}$. In other words, the plane $\mathcal{Q}_P$ is made entirely of tangent lines to $\mathcal{Q}$ at $R$—which means $\mathcal{Q}_P$ is also the tangent plane to $\mathcal{Q}$ at $R$ ($\mathcal{Q}_R = \mathcal{Q}_P$)!

Now apply the first sentence: The first sentence says that if $\mathcal{Q}$ is nondegenerate, no two distinct points $P \neq R$ can ever share the same tangent plane ($\mathcal{Q}_P \neq \mathcal{Q}_R$). Since no other point $R \neq P$ can have $\mathcal{Q}_P$ as its tangent plane, no other point $R \neq P$ can be in the radical of the slice $\mathcal{Q} \cap \mathcal{Q}_P$. Therefore, $P$ is the only singular point of the tangent-plane cross-section:

$$\mathcal{Q}_P \neq \mathcal{Q}_R \text{ for all } R \neq P \quad \Longleftrightarrow \quad \text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$$

**In Short:** $\text{Rad}(\mathcal{Q}) = \emptyset$: The full 3D surface $\mathcal{Q}$ inside 3D space $\mathbf{P}$ is smooth (nondegenerate).

$\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$: When you slice that smooth 3D surface $\mathcal{Q}$ with its tangent plane $\mathcal{Q}_P$ at $P$, the cross-section $\mathcal{Q} \cap \mathcal{Q}_P$ has a pinch/vertex right at the point of tangency $P$ (an X-cross $g \cup h$ for a hyperboloid, or a single point $\{P\}$ for a sphere).

Now let $\mathcal{Q}$ be a nondegenerate quadratic set of $\mathbf{P}$.

> If $P \in \mathcal{Q}$ and $W$ is a complement of $P$ in $\mathcal{Q}_P$, then $\mathcal{Q}' := \mathcal{Q} \cap W$ is a nondegenerate quadratic set of $W$.
    
> If $H$ is a hyperplane that is not a tangent hyperplane, then $\mathcal{Q}' := \mathcal{Q} \cap H$ is a nondegenerate quadratic set of $H$.

### Index of Quadratic Sets

A quadratic set $\mathcal{Q}$ can be described very well by the dimension of its maximal $\mathcal{Q}$-subspaces (which are flat linear subspaces - a point, a line, a plane etc. that sits completely inside the curved surface $\mathcal{Q}$. The prefix $\mathcal{Q}$ simply means "contained in $\mathcal{Q}$"). This maximum dimension is connected to the ‘index’ of $\mathcal{Q}$, which turns out to be the crucial parameter to describe $\mathcal{Q}$.

Let $t - 1$ be the maximum dimension of a $\mathcal{Q}$-subspace of a quadratic set $\mathcal{Q}$. Then the integer $t$ is called the index of $\mathcal{Q}$. The $\mathcal{Q}$-subspaces of dimension $t - 1$ are also called maximal $\mathcal{Q}$-subspaces.

In the literature, $\mathcal{Q}$-subspaces are also called generators or totally isotropic / totally singular subspaces of the quadric.

**Examples.** A cone and a hyperboloid in $3$-dimensional real space have index $2$, since they contain lines, but no planes. Any nonempty quadratic set that does not contain a line has index $1$; for instance, a sphere has index $1$.

If $\mathcal{Q}$ is a nondegenerate quadratic set of index $t$ in a $d$-dimensional projective space $\mathbf{P}$, then if $d$ is even, then $t \le \frac{d}{2}$. If $d$ is odd, then $t \le \frac{d + 1}{2}$. The more general formula which includes degenerate spaces if $t \le \frac{d + r + 1}{2}$ where $r$ is the size of the radical.

Why do we care about the index? In linear algebra and differential geometry, this number $t$ is called the Witt Index (or isotropic index) of a quadratic form. The point of the index is classification. Suppose you are in a $d$-dimensional projective space $\mathbf{P}$ over a finite field $\mathbb{F}_q$ (or the real numbers $\mathbb{R}$), and you want a complete list of every possible nondegenerate quadratic set $\mathcal{Q}$ that can exist in $\mathbf{P}$. The index $t$ is the single invariant that tells them apart. 

To see why, look at why $t$ is defined as $(\text{projective dimension}) + 1$. A projective subspace of projective dimension $t - 1$ corresponds to a vector subspace of vector dimension $t$ in the underlying vector space $V = F^{d+1}$. Therefore, the index $t$ counts the maximum number of mutually independent points $\{P_1, \dots, P_t\}$ you can pick inside $\mathcal{Q}$ such that the entire flat subspace they span lies completely inside $\mathcal{Q}$.

Look at how the index $t$ completely classifies all nondegenerate quadrics in $PG(3, q)$ ($d = 3$, where the theorem says $t \le \frac{3+1}{2} = 2$):

| Index $t$ | Max Dimension of a $\mathcal{Q}$-Subspace ($t - 1$) | What the Maximal $\mathcal{Q}$-Subspaces Are | Name of Quadric in $PG(3, q)$ | Canonical Equation |
| --- | --- | --- | --- | --- |
| $t = 1$ | $t - 1 = \mathbf{0}$ | Points (contains no straight lines at all) | Elliptic Quadric $Q^-(3, q)$ (or Ovoid / Sphere) | $x_0^2 + d x_1^2 + x_2 x_3 = 0$ *(where $x_0^2 + dx_1^2$ is irreducible)* |
| $t = 2$ | $t - 1 = \mathbf{1}$ | Lines (contains lines, but no 2D planes) | Hyperbolic Quadric $Q^+(3, q)$ (Regulus / Hourglass) | $x_0 x_3 - x_1 x_2 = 0$ |

And in even dimension $d = 2m$ (e.g., $d = 4$, where $t \le \frac{4}{2} = 2$), there is only one main type of nondegenerate quadric—the Parabolic Quadric $Q(4, q)$ ($x_0^2 + x_1 x_4 - x_2 x_3 = 0$), which has index $t = 2$ (ruled by lines).

The following lemma shows that the maximal $\mathcal{Q}$-subspaces are ‘uniformly distributed’.

Before that, let's understand what uniformly distributed means. Imagine a bizarre surface where one half of the surface was bumpy like a sphere (containing only $0$D points, no lines), and the other half had a flat 2D disc glued onto it, or a single isolated straight line stuck to one side.  The lemma proves that a quadratic set can NEVER look like that. Now for the lemma:

Let $\mathcal{Q}$ be a quadratic set of index $t$ in $\mathbf{P}$.  Then each point of $\mathcal{Q}$ is on a maximal $\mathcal{Q}$-subspace.

More precisely: if $P$ is a point of $\mathcal{Q}$ outside a $(t - 1)$-dimensional $\mathcal{Q}$-subspace $U$, then there is a $(t - 1)$-dimensional $\mathcal{Q}$-subspace $U'$ through $P$ that intersects $U$ in a $(t - 2)$-dimensional subspace.

We formulate the assertion above once more in the case $t = 2$: through each point of $\mathcal{Q}$ outside a $\mathcal{Q}$-line $g$ there is a $\mathcal{Q}$-line that intersects $g$. We have seen this in the regulus.

So let's relook at what "uniformly distributed" means. It means there are no isolated lower-dimensional patches. If $\mathcal{Q}$ contains even a single  $(t-1)$-dimensional flat subspace $U$ somewhere on it, then every single point $P \in \mathcal{Q}$—no matter where you look on $\mathcal{Q}$—must have at least one $(t-1)$-dimensional flat subspace $U'$ passing right through it.
    
Furthermore, every maximal subspace has the same dimension ($t-1$). And in a finite space $PG(d, q)$, every $(t-1)$-dimensional projective subspace has the exact same number of points ($q^{t-1} + \dots + q + 1$), and by symmetry, every non-singular point $P \in \mathcal{Q}$ lies on the exact same number of maximal $\mathcal{Q}$-subspaces.

So,  for a sphere / ovoid ($t = 1$): Every point is on $1$ maximal subspace (itself).

For a 3D cone ($t = 2$): Every smooth point is on $1$ maximal subspace (the single line connecting it to the vertex).

For a 3D hyperbolic quadric ($t = 2$): Every point is on $2$ maximal subspaces (one line $g \in \mathcal{R}$ and one line $h \in \mathcal{R}'$).
        
For a 4D parabolic quadric $Q(4, q)$ ($t = 2$): Every point is on $q + 1$ maximal subspaces (lines).

The idea of uniformly distributed is very closely associated with what a spread is. In finite geometry, a spread of a quadric $\mathcal{Q}$ (sometimes called an ovoidal fibration or partition) is a subset of maximal $\mathcal{Q}$-subspaces that are mutually disjoint (skew) and partition every point of $\mathcal{Q}$ (so every point of $\mathcal{Q}$ lies in exactly one subspace of the spread).

On a 3D hyperbolic quadric $Q^+(3, q)$, each point lies on $2$ maximal $\mathcal{Q}$-lines ($g \in \mathcal{R}$ and $h \in \mathcal{R}'$). So the set of all $2(q+1)$ lines on $Q^+(3, q)$ is not a spread (because they cross each other in a grid). 

However, a single regulus $\mathcal{R}$ (just the $q+1$ left-tilted lines) IS a spread of the quadric $Q^+(3, q)$ (and is a partial spread of the ambient 3D space $PG(3, q)$), because those $q+1$ lines are mutually skew and cover every single one of the $(q+1)^2$ points of $\mathcal{Q}$ exactly once.

Now let $\mathcal{Q}$ be a quadratic set in $\mathbf{P}$. Let $\mathcal{S}$ be a subset of $\mathcal{Q}$ with the property that the line through any two points of $\mathcal{S}$ is a $\mathcal{Q}$-line. Then $\langle \mathcal{S} \rangle$ is a $\mathcal{Q}$-subspace.

You can visualize this in the following way: Suppose $\mathcal{S} = \{A, B, C\}$ is a triangle of 3 non-collinear points on $\mathcal{Q}$, and suppose the 3 sides of the triangle ($AB, BC, CA$) are all $\mathcal{Q}$-lines (completely contained in $\mathcal{Q}$).
    
Take any point $X$ inside the flat 2D plane $\langle A, B, C \rangle$, and draw a line through $X$ that cuts across the triangle. That line hits side $AB$ at one point of $\mathcal{Q}$ and side $BC$ at a second point of $\mathcal{Q}$. If it hits $CA$ at a third point of $\mathcal{Q}$, then by the If-three-then-all axiom, the entire line through $X$ (including $X$ itself!) must lie in $\mathcal{Q}$!
    
Thus, the entire 2D flat interior of the triangle $\langle A, B, C \rangle$ gets filled in and becomes a flat 2D $\mathcal{Q}$-plane.

Now let $\mathcal{Q}$ be a quadratic set in a $d$-dimensional projective space $\mathbf{P}$, and let $U$ be a maximal $\mathcal{Q}$-subspace. If $\mathcal{Q}$ is nondegenerate, then there is a maximal $\mathcal{Q}$-subspace that is skew (disjoint, which means their intersection is empty) to $U$.

Why must this be true? Let's contrast a cone (degenerate) vs. a hyperboloid (nondegenerate). On a cone, the maximal $\mathcal{Q}$-subspaces are the straight lines ruling the cone.  No two lines on a cone skew. Every single line passes through the vertex $V$. It is impossible to find a maximal $\mathcal{Q}$-line that is skew to $U$.
    
But in a non-degenerate sphere or hyperboloid, because $\mathcal{Q}$ is nondegenerate, there is no universal vertex $V$ where all maximal $\mathcal{Q}$-subspaces are pinned together. To see why this is so, assume that there is such a vertex $V$. Now let's take some point $X$ in the quadratic set. By the uniform distribution lemma, this point must lie on some maximal subspace $U$. Since $U$ is a flat subspace and it contains both $V$ and $X$, the line $VX$ must lie in $U$ as well, making it a $\mathcal{Q}$-line. Since we chose $X$ arbitrarily, it means the line from $V$ to every point in $\mathcal{Q}$. Thus $V$ is a singular point and so the radical of the quadratic set is non-empty, which contradicts the fact that it is non-degenerate.

Now back to visualizing our two skew maximal subspaces, for $t = 1$ (sphere / ovoid), a maximal $\mathcal{Q}$-subspace $U$ is just a single point $P$ ($\dim = 0$). Saying there is a maximal $\mathcal{Q}$-subspace $U'$ skew to $U$ just means there is a second point $P' \in \mathcal{Q}$ disjoint from $P$ ($P \neq P'$).
        
For $t = 2$ (3D Hyperboloid / Regulus), a maximal $\mathcal{Q}$-subspace $U$ is a line $g_1 \in \mathcal{R}$. Because $\mathcal{Q}$ is nondegenerate,  $g_1$ is not pinned to a cone vertex—there are $q$ other lines $g_2, g_3, \dots \in \mathcal{R}$ in the regulus that are completely skew to $g_1$.
        
How do we construct the skew subspace $U'$ in general? If $U = \langle P_1, \dots, P_t \rangle$ is a maximal $\mathcal{Q}$-subspace, nondegeneracy guarantees that for each vertex $P_i$, you can find a point $Q_i \in \mathcal{Q}$ that lies outside the tangent hyperplane $\mathcal{Q}_{P_i}$ (so the line $P_i Q_i$ is a 2-point secant, not a $\mathcal{Q}$-line). Doing this carefully for the basis of $U$ builds a complementary maximal $\mathcal{Q}$-subspace $U' = \langle Q_1, \dots, Q_t \rangle$ that cannot share any point with $U$ ($U \cap U' = \emptyset$).

This also proves our earlier result relating the dimension of the space to the maximum limit of the index of the quadratic set.  Since there is a maximal $\mathcal{Q}$-subspace $U'$ skew to $U$, it means $U$ has dimension $t - 1$ and $U'$ also has dimension $t - 1$. But they are skew, so  $\dim(\langle U, U' \rangle) = \dim(U) + \dim(U') - \dim(U \cap U') = (t - 1) + (t - 1) - (-1) = 2t - 1$.
    
Since their span $\langle U, U' \rangle$ must fit inside the ambient $d$-dimensional projective space $\mathbf{P}$, we must have $2t - 1 \le d \quad \Longleftrightarrow \quad t \le \frac{d + 1}{2}$. The formula follows from this.

How does this formula change for degenerate subspaces. $t$ gets larger because every maximal $\mathcal{Q}$-subspace $U$ of a degenerate quadratic set must contain the radical $\text{Rad}(\mathcal{Q})$.

Instead of being completely skew ($U \cap U' = \emptyset$), two "as-disjoint-as-possible" maximal $\mathcal{Q}$-subspaces $U$ and $U'$ in a degenerate quadratic set are pinned together along $\text{Rad}(\mathcal{Q})$: $U \cap U' = \text{Rad}(\mathcal{Q})$.

If $r = \dim(\text{Rad}(\mathcal{Q})) + 1$ is the number of independent points in the radical, and if we plug $\dim(U \cap U') = r - 1$ into the Grassmann formula, look at what you get:

$$\dim(\langle U, U' \rangle) = (t - 1) + (t - 1) - (r - 1) = 2t - r - 1 \le d$$

Rearranging that gives the universal bound that works for both degenerate and nondegenerate quadratic sets:

$$d \ge 2t - r - 1 \quad \Longleftrightarrow \quad t \le \frac{d + r + 1}{2}$$

When $\mathcal{Q}$ is nondegenerate,  $\text{Rad}(\mathcal{Q}) = \emptyset$, so $r = 0$, and we recover $d \ge 2t - 1$ ($t \le \frac{d+1}{2}$).
    
When $\mathcal{Q} = H_1 \cup H_2$ is two planes in $d = 3$,  $\text{Rad}(\mathcal{Q})$ is a line ($r = 2$), and the formula gives $t \le \frac{3 + 2 + 1}{2} = 3$, which matches $t = 3$.

### Quadratic Sets in 2D and 3D Projective Spaces
We first define a type of objects found in 2D projective planes, and a few objects found in 3D projective spaces. Then for 2D and 3D spaces, we list out the possible quadratic sets.

A nonempty set $\mathcal{O}$ of points in a projective plane is called an oval if no three points of $\mathcal{O}$ are collinear and each point of $\mathcal{O}$ is on a unique tangent. Ovals are the only type of nonempty, nondegenerate quadratic sets in a projective plane.

An ovoid is a nonempty set $\mathcal{O}$ of points of $\mathbf{P}$ where no three points of $\mathcal{O}$ are collinear and for each point $P \in \mathcal{O}$, the tangents through $P$ cover a hyperplane (that is,  $\mathcal{O}_P$ is a hyperplane).

---

**Aside:** Because no three points of an ovoid are collinear, an ovoid contains no lines at all, meaning its index is $t = 1$. In 3D space, ovoids are the exact synthetic generalization of spheres/elliptic quadrics. So every sphere and elliptic quadric is automatically an ovoid, but there are ovoids that are not spheres or elliptic quadrics.

---

Now suppose $d = 3$. A set $\mathcal{K}$ of points of $\mathbf{P}$ is called a cone if there exist a plane $\pi$, an oval $\mathcal{O}$ in $\pi$, and a point $V \notin \pi$ such that $\mathcal{K}$ consists of the points on the lines $VX$ with $X \in \mathcal{O}$. We call $V$ the vertex of the cone $\mathcal{K}$.

The nonempty, nondegenerate quadratic sets in a $3$-dimensional projective space are ovoids and hyperboloids (hyperbolic quadrics). The nonempty degenerate quadratic sets are either a subspace, a cone, or the union of two planes (hyperplanes).

As an interesting aside, let's see why the union of two lines is not a quadratic set in 3D space. This is a great test of the Tangent-Space Axiom. 

Suppose in a 3-dimensional projective space  $\mathbf{P}$ ($d = 3$), we have $\mathcal{Q} = g_1 \cup g_2$, the union of two distinct lines $g_1$ and $g_2$.

What is the tangent space $\mathcal{Q}_P$ look like at a point $P \in g_1$ (with $P \notin g_2$). To find $\mathcal{Q}_P$, we stand at $P$, shoot lines in all 3D directions, and keep the lines that meet $\mathcal{Q}$ in $1$ point or all points. Equivalently, we throw away all the 2-point secant lines.

Which lines through $P$ are 2-point secant lines? Lines connecting $P$ to some point $X \in g_2$. So what does the tangent space at $P$ become? The 2D flat plane $\Pi = \langle P, g_2 \rangle$ spanned by $P$ and $g_2$.

Now which lines through $P$ are NOT secants and are therefore tangents in $\mathcal{Q}_P$? Every line in 3D space passing through $P$ that does not lie in the plane $\Pi$.

The resulting tangent space $\mathcal{Q}_P$ is $\mathcal{Q}_P = \left( \mathbf{P} \setminus \langle P, g_2 \rangle \right) \cup g_1$. The Tangent-Space Axiom says this should be either a hyperplane or the entire space. Neither of these descriptions fit this tangent space. Thus, these two lines do not form a quadratic set.

Of course, in a 2D projective plane, there is no 3D space through which tangent lines can travel, so the tangent space ends up being the entire plane, and so the two lines are quadratic sets.

In algebra, a quadric $\mathcal{Q}$ is defined by one single quadratic equation  $f(x_0, x_1, x_2, x_3) = 0$. If that quadratic polynomial factors into two linear pieces:

$$f(x_0, x_1, x_2, x_3) = L_1(x_0, x_1, x_2, x_3) \cdot L_2(x_0, x_1, x_2, x_3) = 0$$

then $L_1(x) = 0$ is a hyperplane  $H_1$, and $L_2(x) = 0$ is a hyperplane  $H_2$, so their union is $H_1 \cup H_2$ (two planes in 3D space). You can never get the union of two 1D lines in 3D space from a single quadratic equation (in algebraic geometry, two skew lines in 3D space require intersecting multiple quadratic surfaces, not just one). The Tangent-Space Axiom is the synthetic rule that detects this.

Note that $L_1, L_2$ can only be hyperplanes. For example, they cannot be a line in 3D space. This comes down to one of the most fundamental rules of linear algebra:  each single linear equation removes only $1$ degree of freedom (reduces the dimension by $1$).

### Quadratic Sets in Finite Projective Spaces

Compared to the previous section, this section is both a generalization to arbitrary dimension $d$  and a specialization to finite spaces $PG(d, q)$ (where every line has exactly $q + 1$ points).

Switching to finite projective spaces gives us a new tool we didn't have in general (infinite) 2D and 3D spaces: exact counting (pigeonhole and parity arguments). Because the number of points on every line is fixed at $q+1$, we can deduce the exact number of points in any quadratic set $\mathcal{Q}$, tighten the index bound $t$, and completely classify all nondegenerate quadratic sets in any dimension $d$.

Now let $\mathcal{Q}$ be a quadratic set in a $d$-dimensional finite projective space $\mathbf{P} = PG(d, q)$, where every line contains $q + 1$ points.

Pick any non-singular point $P \in \mathcal{Q} \setminus \text{Rad}(\mathcal{Q})$. Because $P$ is not in the radical, its tangent space $\mathcal{Q}_P$ is a hyperplane (dimension $d - 1$). Let $a = a_P$ denote the number of $\mathcal{Q}$-lines (lines completely contained in $\mathcal{Q}$) that pass through $P$.

$\mathcal{Q}_P$ contains $aq + 1$ points of $\mathcal{Q}$. $\vert{}\mathcal{Q}\vert{} = 1 + q^{d-1} + aq$. $a$ is independent of $P$.

The proof reveals some additional, useful numbers. Every line through $P$ that lies outside $\mathcal{Q}_P$ is a 2-point secant line—meaning each such line contains exactly $1$ additional point of $\mathcal{Q}$ besides $P$.

How many lines through $P$ lie outside the hyperplane $\mathcal{Q}_P$? Total lines through $P$ in $PG(d, q)$: $\frac{q^d - 1}{q - 1} = q^{d-1} + q^{d-2} + \dots + q + 1$. Lines through $P$ inside the hyperplane $\mathcal{Q}_P$: $\frac{q^{d-1} - 1}{q - 1} = q^{d-2} + \dots + q + 1$. Subtracting the two gives exactly $q^{d-1}$ secant lines through $P$ outside $\mathcal{Q}_P$.

Each of those $q^{d-1}$ secant lines contributes $1$ point of $\mathcal{Q}$ outside $\mathcal{Q}_P$. Add to this the total number of points in $\mathcal{Q}_P$ ($1 + aq$) to get the total number of points of the quadratic set.

Why $a$ is independent of $P$: Solving for $a_P$ gives $a_P = \frac{\vert{}\mathcal{Q}\vert{} - 1 - q^{d-1}}{q}$. Because $\vert{}\mathcal{Q}\vert{}$, $d$, and $q$ are global constants of $\mathcal{Q}$, every non-singular point $P \in \mathcal{Q} \setminus \text{Rad}(\mathcal{Q})$ has the same number $a$ of $\mathcal{Q}$-lines passing through it.

Some counts for standard objects:

| Quadratic Set $\mathcal{Q}$ | Ambient Dimension $d$ | Number of $\mathcal{Q}$-Lines Through $P$ ($a$) | Why $a$ Has This Value | Total Points $\vert{}\mathcal{Q}\vert{} = 1 + q^{d-1} + aq$ |
| --- | --- | --- | --- | --- |
| Oval (in a 2D plane) | $d = 2$ | $a = 0$ | No 3 points are collinear, so $\mathcal{Q}$ contains no lines. | $1 + q^{2-1} + 0 = \mathbf{q + 1}$ |
| Ovoid (in 3D space) | $d = 3$ | $a = 0$ | No 3 points are collinear, so $\mathcal{Q}$ contains no lines. | $1 + q^{3-1} + 0 = \mathbf{q^2 + 1}$ |
| Cone (over an oval in 3D) | $d = 3$ | $a = 1$ | Through any non-vertex point $P \neq V$, there is only $1$ line in $\mathcal{Q}$ (the line $PV$ to the vertex). | $1 + q^2 + 1\cdot q = \mathbf{q^2 + q + 1}$ |
| Hyperboloid (Regulus in 3D) | $d = 3$ | $a = 2$ | Doubly ruled: each point $P$ lies on $1$ line $g \in \mathcal{R}$ and $1$ line $h \in \mathcal{R}'$. | $1 + q^2 + 2q = \mathbf{(q + 1)^2}$ |

Now let $\mathcal{Q}$ be a nonempty, nondegenerate quadratic set of a finite projective space $\mathbf{P}$ of dimension $d$. Then there are only three possibilities for the index $t$ of $\mathcal{Q}$. If $d$ is odd, then $t = \frac{d - 1}{2}$ or $t = \frac{d + 1}{2}$.

This sets an exact value for the index for even dimensions and a very tight bound for odd dimensions. This also means there are no ovoids for $d \geq 4$ because an ovoid has an index of $1$, which is not possible once $d \geq 4$.

In general, the nomenclature is, if $d$ is even, then the quadratic set is called parabolic. If $d$ is odd, if $t = \frac{d - 1}{2}$, it is called an elliptic, and if $t = \frac{d + 1}{2}$ it is called a hyperbolic.

The parabolic quadratic sets of a projective plane are the ovals. In a 3D projective space, the elliptic quadratic sets are the ovoids and the hyperboloids are the hyperbolic quadratic sets. And any nonempty non-degenerate quadratic set of a finite projective space is elliptic, parabolic, or hyperbolic. 

Now let $\mathcal{O}$ be an oval in a finite projective plane of order $q$. As we have seen, $\vert{}\mathcal{O}\vert{} = q + 1$ points. At each of the $q + 1$ points of $\mathcal{O}$, there is a unique tangent line, so there are $q + 1$ tangent lines in total in the plane.

If $q$ is odd, every oval is an algebraic conic ($x_0 x_2 - x_1^2 = 0$), and every external point lies on either $0$ or $2$ tangents. If $q$ is even, all $q + 1$ tangent lines meet at a single common point $N$ called the nucleus or knot of the oval. Adding $N$ to $\mathcal{O}$ gives a set of $q + 2$ points with no $3$ collinear, called a hyperoval.

Now let's look at how we get such tight bounds on the the Witt index. We will see that this comes about because the number of points in a quadratic set depends on the number of points of a quadratic set of a lower dimension and index. This way, we inductively calculate the number of points on a quadratic set building up from dimension 2 and 3.  

Now let $\mathcal{Q}$ be a nondegenerate quadratic set of index $t$ in dimension $d$. Pick a point $P \in \mathcal{Q}$ and look at the induced quadratic set $\overline{\mathcal{Q}} = \mathcal{Q}_P \cap \mathcal{Q}$ inside the $(d-1)$-dimensional tangent hyperplane $\mathcal{Q}_P$.

Because $\mathcal{Q}$ is nondegenerate, $\overline{\mathcal{Q}} = \mathcal{Q}_P \cap \mathcal{Q}$ is a degenerate cone with vertex $\text{Rad}(\mathcal{Q}_P \cap \mathcal{Q}) = \{P\}$. Pick a $(d-2)$-dimensional subspace $U \subset \mathcal{Q}_P$ missing $P$. By the Radical/Cone Theorem, the base slice $\mathcal{Q}' := \mathcal{Q} \cap U$ is a nondegenerate quadratic set in dimension $d - 2$ with index $t - 1$ since every $(t-1)$-dimensional maximal $\mathcal{Q}$-subspace through $P$ meets $U$ in dimension $t - 2$. It's point count is $\vert{}\mathcal{Q}'\vert{} = a$ since every $\mathcal{Q}$-line through $P$ pierces $U$ in a unique point of $\mathcal{Q}'$.

Each time we perform this tangent-slice reduction to algebraically peel off one hyperbolic coordinate pair $x_i y_i$, the ambient dimension drops by $2$ and the index drops by $1$. Repeat this reduction $t - 1$ times until we strip away all the straight lines and reach a nondegenerate quadratic set of index $t_{\text{stop}} = 1$ (a line-free ovoid/oval).

Because no line-free quadratic set ($t_{\text{stop}} = 1$) can exist in dimension $d_{\text{stop}} \ge 4$, the stopping dimension $d_{\text{stop}} = d - 2(t - 1)$ must be $1$, $2$, or $3$:

$$1 \le d - 2(t - 1) \le 3 \quad \Longleftrightarrow \quad \frac{d - 1}{2} \le t \le \frac{d + 1}{2}$$

This single inequality locks $t$ into only three possibilities across all dimensions $d$. In fact, we can make the bound tighter, at least for even dimensions.

In even dimension $d = 2m$ parabolic quadrics $\mathcal{Q}(2m, q)$), reducing $d = 2m$ by $2$ (and $t$ by 1) repeatedly $m - 1$ times lands in $d_0 = 2$ (the projective plane $\text{PG}(2, q)$). Since every nonempty nondegenerate quadratic set in $\text{PG}(2, q)$ is an oval of index $t_0 = 1$, we can now inductively build back to our original $d$-dimensional space, which will add $m - 1$ to the index: $t = 1 + (m - 1) = m = \frac{d}{2}$.
            
For odd dimensions $d = 2m + 1$ (elliptic $\mathcal{Q}^-(2m+1, q)$ and hyperbolic $\mathcal{Q}^+(2m+1, q)$ quadrics), reducing $d = 2m + 1$ by $2$ repeatedly $m - 1$ times lands in $d_0 = 3$ ($\text{PG}(3, q)$), where the only nondegenerate quadratic sets are ovoids ($t_0 = 1$) and hyperboloids ($t_0 = 2$). Adding back $m - 1$ to the index leaves only two possibilities: $t = 1 + (m - 1) = m = \frac{d - 1}{2}$for elliptic, $t = 2 + (m - 1) = m + 1 = \frac{d + 1}{2}$ for hyperbolic.

Thus, finite fields restrict nondegenerate quadrics to only three families: parabolic, elliptic and hyperbolic. The bounds also mean that in a finite projective space of dimension $d \ge 4$, since $t \geq 2$, the maximal subspace will have a dimension of at least 2, and will therefore contain lines, which means every non-empty quadratic set is ruled by straight lines, and in higher dimensions, by planes, 3-spaces, etc.).

Of course, in real space $PG(d, \mathbb{R})$ you can still have line-free spheres $x_1^2 + \dots + x_d^2 = x_0^2$ in any dimension $d$. Also, in dimension $d \ge 4$, $\mathcal{Q}$ has dimension $d - 1 \ge 3$, so geometers call it a ruled hypersurface or ruled variety rather than a 2D "surface."

| Stopping Dimension $d_{\text{stop}} = d - 2(t-1)$ | What the Line-Free Set of Index $1$ Is at $d_{\text{stop}}$ | Parity of Original Dimension $d$ | Resulting Formula for Index $t$ | Type of Full $d$-Dimensional Quadric & Canonical Equation |
| --- | --- | --- | --- | --- |
| $d_{\text{stop}} = 1$ (Line $PG(1, q)$) | $2$ points on a line ($x_1 y_1 = 0$) | $d = 2m - 1$ is ODD ($d = 2t - 1$) | $t = \frac{d + 1}{2} = m$ | Hyperbolic Quadric $Q^+(2m-1, q)$: $x_1 y_1 + \dots + x_m y_m = 0$ |
| $d_{\text{stop}} = 2$ (Plane $PG(2, q)$) | A $2$D Oval of $q+1$ points ($x_1 y_1 + z_1^2 = 0$) | $d = 2m$ is EVEN ($d = 2t$) | $t = \frac{d}{2} = m$ | Parabolic Quadric $Q(2m, q)$: $x_1 y_1 + \dots + x_m y_m + z_1^2 = 0$ |
| $d_{\text{stop}} = 3$ ($3$D Space $PG(3, q)$) | A $3$D Ovoid of $q^2+1$ points ($x_1 y_1 + z_1^2 + \alpha z_1 z_2 + \beta z_2^2 = 0$) | $d = 2m - 1$ is ODD ($d = 2t + 1$) | $t = \frac{d - 1}{2} = m - 1$ | Elliptic Quadric $Q^-(2m-1, q)$: $x_1 y_1 + \dots + x_{m-1} y_{m-1} + f_{\text{irred}}(z_1, z_2) = 0$ |

**Concrete $6$D Example: Tracing a $6$D Parabolic Quadric ($d = 6, \, m = 3$)**

Consider a Parabolic Quadric $\mathcal{Q}$ in $6$-dimensional projective space $PG(6, q)$ ($d = 2m = 6$) with $7$ homogeneous coordinates $(x_1 : y_1 : x_2 : y_2 : x_3 : y_3 : z_1)$:


$$\underbrace{x_1 y_1}_{\text{Pair 1}} + \underbrace{x_2 y_2}_{\text{Pair 2}} + \underbrace{x_3 y_3 + z_1^2}_{\text{2D Oval}} = 0$$

* Start at $d = 6$ (Index $t = 3$): $\mathcal{Q}$ is a $6$D parabolic quadric ruled by $2$D planes ($t - 1 = 2$).
* Peel off Pair 1 ($x_1 = y_1 = 0$) $\implies$ Drop to $d = 4$ (Index $t = 2$): You get $x_2 y_2 + x_3 y_3 + z_1^2 = 0$ in $PG(4, q)$, a $4$D parabolic quadric ruled by $1$D lines ($t - 1 = 1$).
* Peel off Pair 2 ($x_2 = y_2 = 0$) $\implies$ Drop to $d_{\text{stop}} = 2$ (Index $t_{\text{stop}} = 1$): You get $x_3 y_3 + z_1^2 = 0$ in $PG(2, q)$, which is a $2$D oval (conic) of index $1$ (no lines) in dimension $d_{\text{stop}} = 2 \le 3$.
* Why $t = 2$ is impossible in $d = 6$: If a nondegenerate quadric in $d = 6$ had index $t = 2$, peeling off $t - 1 = 1$ pair would leave a line-free set ($t_{\text{stop}} = 1$) in dimension $d_{\text{stop}} = 6 - 2(1) = \mathbf{4}$—a $4$D ovoid in $PG(4, q)$, which cannot exist.

Now we can come up with an exact point counting formula for quadratic sets in finite fields. Because $\vert{}\mathcal{Q}'\vert{} = a$, our point-counting formula $\vert{}\mathcal{Q}\vert{} = 1 + q^{d-1} + aq$ becomes a recursion across dimensions:

$$\vert{}\mathcal{Q}_{d, t}\vert{} = 1 + q^{d-1} + q \cdot \vert{}\mathcal{Q}_{d-2, t-1}\vert{}$$

Solving this recursion from the three stopping base cases ($d_{\text{stop}} = 1, 2, 3$) yields the universal closed-form formula for any nondegenerate quadratic set of index $t$ in $PG(d, q)$:
            
$$\vert{}\mathcal{Q}\vert{} = \frac{q^d - 1}{q - 1} + \varepsilon q^{\frac{d-1}{2}} \qquad \text{where } \varepsilon = \begin{cases} 0 & \text{if } d \text{ is even } (t = d/2) \\ -1 & \text{if } d \text{ is odd, elliptic } (t = (d-1)/2) \\ +1 & \text{if } d \text{ is odd, hyperbolic } (t = (d+1)/2) \end{cases}$$

Written out explicitly for the three nondegenerate families in $PG(d, q)$:

**1. Parabolic Type ($d = 2m$ even, $t = m$):**

$$\vert{}\mathcal{Q}(2m, q)\vert{} = \frac{q^{2m} - 1}{q - 1} = q^{2m-1} + q^{2m-2} + \dots + q + 1$$

It has the same number of points as a hyperplane $PG(2m-1, q)$. 

- For $d=2, m=1$ [Oval]: $q + 1$. 
- For $d=4, m=2$: $q^3 + q^2 + q + 1$.

**2. Hyperbolic Type ($d = 2m - 1$ odd, $t = m = \frac{d+1}{2}$):**

$$\vert{}\mathcal{Q}^+(2m - 1, q)\vert{} = \frac{(q^m - 1)(q^{m-1} + 1)}{q - 1} = \frac{q^{2m-1} - 1}{q - 1} + q^{m-1}$$

- For $d=3, m=2$ [3D Regulus]: $(q+1)^2 = q^2 + 2q + 1$. 
- For $d=5, m=3$ [Klein Quadric]: $(q^2+1)(q^2+q+1) = q^4 + q^3 + 2q^2 + q + 1$.

**3. Elliptic Type ($d = 2m - 1$ odd, $t = m - 1 = \frac{d-1}{2}$):**

$$\vert{}\mathcal{Q}^-(2m - 1, q)\vert{} = \frac{(q^m + 1)(q^{m-1} - 1)}{q - 1} = \frac{q^{2m-1} - 1}{q - 1} - q^{m-1}$$

- For $d=3, m=2$ [3D Ovoid]: $q^2 + 1$. 
- For $d=5, m=3$: $(q^3 + 1)(q + 1) = q^4 + q^3 + q + 1$.

### Some Properties of Parabolic, Elliptic & Hyperbolic Quadratic Sets

Let $\mathcal{Q}$ be a parabolic quadratic set in a $2t$-dimensional projective space $\mathbf{P}$ with $t \ge 2$. Let $H = \mathcal{Q}_P$ be a tangent hyperplane. Then $\mathcal{Q}' := \mathcal{Q} \cap H$ is a cone over a parabolic quadratic set. Let $H^*$ be a hyperplane that is not a tangent hyperplane. Then $\mathcal{Q}^* := \mathcal{Q} \cap H^*$ is an elliptic or a hyperbolic quadratic set.

Now let $\mathcal{Q}$ be a hyperbolic quadratic set of a $(2t - 1)$-dimensional projective space $\mathbf{P}$ with $t \ge 2$. If $H = \mathcal{Q}_P$ is a tangent hyperplane, then $\mathcal{Q}' := \mathcal{Q} \cap H$ is a cone over a hyperbolic quadratic set. Let $H^*$ be a hyperplane that is not a tangent hyperplane. Then $\mathcal{Q}^* := \mathcal{Q} \cap H^*$ is a parabolic quadratic set.

Note that we already encountered the conics referred to here when slicing with a tangent hyperplane. What's new here is slicing with a non-tangent hyperplane $H^*$, which drops you by only $1$ dimension and yields a nondegenerate quadratic set. Because $d$ and $d - 1$ have opposite parities, a non-tangent slice forces the quadric to switch between the even-dimensional family (parabolic) and the odd-dimensional families (hyperbolic / elliptic).

Now let $\mathcal{Q}$ be a hyperbolic quadratic set in $\mathbf{P} = \text{PG}(5, q)$. Then $a = (q + 1)^2$ and $\vert{}\mathcal{Q}\vert{} = q^4 + q^3 + 2q^2 + q + 1 = (q^2 + q + 1)(q^2 + 1)$. Note that as we saw previously while inductively building the point count formula, $a$ is equal to the number of points of a quadratic set of $d-2$ dimensions and index $t-1$. When $d=3$, $a$ becomes the number of points on a regulus in a 3D projective space, which we already know is $(q+1)^2$.

A hyperbolic quadratic set has an extremely remarkable property: one can divide its maximal $\mathcal{Q}$-subspaces into two equivalence classes. The equivalence relation is given by the property that the corresponding subspaces intersect in a subspace of a certain parity. In fact, if $\mathcal{Q}$ has index $t$ with $d = 2t - 1$ and maximal subspace of dimension $t-1$, any two maximal $\mathcal{Q}$-subspaces $U_1, U_2$ are equivalent if and only if $(t-1) - \dim(U_1 \cap U_2)$ is even. 

If $d \ge 5$, all the maximal $\mathcal{Q}$-subspaces are partitioned into two equivalence classes by this parity formula.

In a $3$-dimensional projective space, we already know that the maximal $\mathcal{Q}$-subspaces of a hyperboloid are the lines of a regulus and its opposite regulus. If we define that two $\mathcal{Q}$-lines are equivalent if they are equal or skew, we get two classes of $\mathcal{Q}$-lines. There are two equivalence classes.

Similarly, let $\mathcal{Q}$ be a hyperbolic quadratic set of a $5$-dimensional projective space $\mathbf{P}$. We say that two $\mathcal{Q}$-planes $\pi_1$ and $\pi_2$ are equivalent ($\pi_1 \sim \pi_2$) if $\pi_1$ and $\pi_2$ are equal or intersect each other in a single point.

The relation $\sim$ is reflexive and symmetric. Surprisingly, it is also transitive, making it an equivalence relation. 

## Quadrics Redux

Let's get back to quadrics. What we'll be doing here parallels what we did earlier with projective geometry in general. We first gave the synthetic axioms of a projective space and then introduced vector spaces and proved that any $\mathbf{P}(V)$ satisfies those axioms, and also looked at the converse, which is that almost every synthetic projective space is actually a $\mathbf{P}(V)$ (holds for all $d > 2$ but not for non-Desarguesian planes).
    
We'll do something similar here. We already talked of quadratic sets and their synthetic axioms: "If-three-then-all" and "Tangent-space" axioms. Now, we look at an algebraic model, or quadrics, inside $\mathbf{P}(V)$ defined by a polynomial equation $q(v) = 0$, and prove that every algebraic quadric satisfies the two axioms of a quadratic set, and that the converse is almost true with specific exceptions (like Tits ovoids or hyperovals in even characteristic).

First we define a quadratic form, which is essentially a homogenous polynomial of degree 2. Note that this implies that $q(\alpha \cdot v) = \alpha^2 \cdot q(v)$ for all $v \in V$ and all $\alpha \in F$. Note that we cannot use an inhomogenous polynomial because then once again, as earlier, the solution to the polynomial will not be independent of the scaling factor which treats multiple points as an equivalence class in projective spaces.

The quadric $\mathcal{Q}$ in $\mathbf{P}(V)$ is simply the set of all projective points $\langle v \rangle$ where that polynomial equals zero:  $q(v) = 0$. So you can simply write out a quadratic form and find its zeroes to arrive at all the points of a quadric.

Examples include the polynomial $x_0^2 - x_1^2 - x_2^2$ which yields a quadric in the plane; $x_0^2 - x_1^2 - x_2^2 - x_3^2$ and $x_0^2 + x_1^2 - x_2^2 - x_3^2$ provide quadrics in $3$-dimensional space.

We also define the polar form of $q$ as the map $B : V \times V \to F$ defined by $B(v, w) := q(v + w) - q(v) - q(w)$. It is a symmetric bilinear form. 

We can write a quadratic form via matrices once we define a vector space basis, $B(v, w) = v^T M w$. $M$ is a symmetric matrix. Note that there can be various $M$ that give the same quadratic form, since the coefficients of the cross terms $b_ib_j$ in the quadratic form will depend on the sum of entries in $M$ that correspond to the terms $b_ib_j$ and $b_jb_i$. In order to be able to define this uniquely, we can use an upper triangular matrix. This is also useful in characteristic 2 fields, because you cannot divide an odd coefficient by $2$ to split $b_1 b_2$ symmetrically into $\frac{1}{2} b_1 b_2 + \frac{1}{2} b_2 b_1$! Using an upper-triangular sum $\sum_{i \le j} c_{ij} b_i b_j$ works in every field.

As an example, suppose we have the quadratic polynomial:

$$q(b_1, b_2, b_3) = 2b_1^2 + \mathbf{6b_1 b_2} - 4b_1 b_3 + 5b_2^2 + 3b_3^2$$

Both

$$A_{\text{sym}} = \begin{pmatrix} 2 & \mathbf{3} & -2 \\ \mathbf{3} & 5 & 0 \\ -2 & 0 & 3 \end{pmatrix}, \qquad A_{\text{other}} = \begin{pmatrix} 2 & \mathbf{5} & -4 \\ \mathbf{1} & 5 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

will give us the polynomial. However, there is a unique upper triangular matrix that does the job.

$$C_{\text{upper}} = \begin{pmatrix} 2 & \mathbf{6} & -4 \\ 0 & 5 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

The polar form is key to understanding how a quadric satisfies both axioms of a quadratic set. Understanding this fact will also give us insight into why the polar form is defined the way it is, so let's take the two axioms are see what is needed from a quadratic form to satisfy the two axioms.

Note that $q(v)$ only takes one vector as input, which tells us whether a single point $\langle v \rangle$ lies on the quadric ($q(v) = 0$). To study how a straight line connecting two points $\langle v \rangle$ and $\langle w \rangle$ intersects the quadric, we have to evaluate $q$ on a linear combination $v + \lambda w$. This is where $B(v,w)$ comes into play. Think of $B(x, v) = 0$ as the algebraic version of the calculus gradient dot product $\nabla q(v) \cdot x = 0$, which defines the tangent hyperplane at $v$ without needing limits or derivatives.

Any point on the line $vw$ is given by $v + \lambda w$. Let's check if it lies on the quadric. By the definition of the bilinear form:

$$q(v + \lambda w) = q(v) + q(\lambda w) + B(v, \lambda w)$$

Since $q(\lambda w) = \lambda^2 q(w)$ and $B$ is bilinear or linear in each slot ($B(v, \lambda w) = \lambda B(v, w)$), we get the fundamental Line-Quadric Intersection Formula:

$$q(v + \lambda w) = q(v) + \lambda B(v, w) + \lambda^2 q(w)$$

The RHS is an ordinary quadratic equation $A \lambda^2 + C \lambda + D = 0$ in the scalar parameter $\lambda$, and $B(v, w)$ is the cross-term (the coefficient of $\lambda^1$) that controls how $\langle v \rangle$ and $\langle w \rangle$ interact.

This formula $q(v + \lambda w) = q(v) + \lambda B(v, w) + \lambda^2 q(w)$ proves both axioms of a quadratic set for any quadric.

Let's look at the "If-Three-Then-All" axiom. Let $g$ be the line through $\langle v \rangle$ and $\langle w \rangle$. Every point on $g$ (aside from $\langle w \rangle$) has the form $\langle v + \lambda w \rangle$. Suppose $g$ contains three distinct points of the quadric $\mathcal{Q}$. Without loss of generality, let two of those points on $\mathcal{Q}$ be the base points $\langle v \rangle$ and $\langle w \rangle$ themselves, so $q(v) = 0$ and $q(w) = 0$. Plugging $q(v) = 0$ and $q(w) = 0$ into our intersection formula leaves:

$$q(v + \lambda w) = \lambda B(v, w)$$

Now use the third point of $\mathcal{Q}$ on the line $g$, which corresponds to some non-zero scalar $\lambda_0 \neq 0$ with $q(v + \lambda_0 w) = 0$:$$\lambda_0 B(v, w) = 0 \quad \stackrel{\lambda_0 \neq 0}{\Longrightarrow} \quad B(v, w) = 0$$Since $q(v) = 0$, $q(w) = 0$, and $B(v, w) = 0$, our formula gives $q(v + \lambda w) = 0$ for all $\lambda \in F$. Every point of the line $g$ lies in $\mathcal{Q}$.

Now let's look at how the tangent space axiom behaves. First let's define something that will become our tangent space. 

Let $q$ be a quadratic form of the vector space $V$. For a vector $v \in V \setminus \{0\}$ (which is a point in projective space) we define $\langle v \rangle^\perp := \{x \in V \mid B(x, v) = 0\}$. Note that we already gave an analogy relating $B$ to the dot product, and the dot product of a line with a tangent or perpendicular line is $0$.

If $q$ be a quadratic form of the vector space $V$, and $\mathcal{Q}$ be the corresponding quadric of $\mathbf{P}(V)$, then for each vector $v \in V \setminus \{0\}$ we have:

> $\langle v \rangle^\perp$ is a subspace of $V$, hence also a subspace of $\mathbf{P}(V)$.
    
> Either $\langle v \rangle^\perp$ is a hyperplane, or we have $\langle v \rangle^\perp = V$. (should remind you of tangent planes being hyperplanes or the whole space)
    
> Suppose that $\langle v \rangle \in \mathcal{Q}$. Then each line in $\langle v \rangle^\perp$ through $\langle v \rangle$ that contains another point $\langle w \rangle \in \mathcal{Q} \setminus \{\langle v \rangle\}$ contains only points of $\mathcal{Q}$. (should remind you of $\mathcal{Q}$-lines. This means that each line in $\langle v \rangle^\perp$ through $\langle v \rangle$ is a tangent of $\mathcal{Q}$.
    
> Suppose that $\langle v \rangle \in \mathcal{Q}$. Then each line through $\langle v \rangle$ that is not contained in $\langle v \rangle^\perp$ intersects $\mathcal{Q}$ in a single further point (any line touching the quadric that is not a tangent is a secant).

The intersection formula $q(v + \lambda x) = q(v) + \lambda B(x, v) + \lambda^2 q(x)$ can help prove all these. Suppose $\langle v \rangle \in \mathcal{Q}$, so **$q(v) = 0$**. Then for any other point $\langle x \rangle$ in space, the points on the line joining $\langle v \rangle$ and $\langle x \rangle$ satisfy:

$$q(v + \lambda x) = \lambda \big( B(x, v) + \lambda q(x) \big)$$

We already have the root $\lambda = 0$ (which is the point $\langle v \rangle$ itself). When is there a second root $\lambda \neq 0$ on the line? If $\langle x \rangle \in \langle v \rangle^\perp$, meaning $B(x, v) = 0$, then the equation becomes $q(v + \lambda x) = \lambda^2 q(x) = 0$.

If $q(x) \neq 0$ ($\langle x \rangle \notin \mathcal{Q}$), the only root is $\lambda = 0$ (making it a double root). So the line meets $\mathcal{Q}$  only at the single point $\langle v \rangle$ ($1$-point tangent). If $q(x) = 0$ ($\langle x \rangle \in \mathcal{Q}$), then $q(v + \lambda x) = 0$ for all  $\lambda$. So the entire line is a $\mathcal{Q}$-line (also a tangent).
        
So a line through $\langle v \rangle$ is a tangent to $\mathcal{Q}$ if and only if it lies inside $\langle v \rangle^\perp$.

Let's see what happens when $\langle x \rangle \notin \langle v \rangle^\perp$, meaning $B(x, v) \neq 0$. Then $B(x, v) + \lambda q(x) = 0$ has one unique non-zero solution $\lambda = -\frac{B(x, v)}{q(x)}$ (or if $q(x)=0$, the second root is the point $\langle x \rangle$ itself). Thus, every line through $\langle v \rangle$ outside $\langle v \rangle^\perp$ is a 2-point secant intersecting $\mathcal{Q}$ in a single further point.
    
Why is $\langle v \rangle^\perp$ a hyperplane or all of $V$? Because $B(x, v)$ is linear in $x$, the condition $B(x, v) = 0$ is one single linear equation on $V$ for a fixed point $v$. As we saw earlier, a single linear equation either has all zeros as coefficients (giving the whole space $V$, which means $\langle v \rangle \in \text{Rad}(\mathcal{Q})$) or has at least one non-zero coefficient, which reduces the dimension by $1$ and defines a hyperplane.

Thus, since a quadric automatically satisfies both axioms of a quadratic set, we can say each quadric is a quadratic set.

Note that we call the quadratic form $q$ of $V$ nondegenerate if the following is true: if $q(v) = 0$ and $B(x, v) = 0$ for all $x \in V$, then $v = 0$. To see why this condition holds, lets assume there is some $v \neq 0$ for which these conditions hold. Then the point in the projective space corresponding to $v$ is on the quadric (since $q(v)=0$) and is also in the tangent space (since $B(x, v) = 0$). Since this holds for all $x \in V$, the tangent space is the entire projective space, and so the point is singular and the form is degenerate.

The definition of a quadratic form is so complicated only because one wants to include the case of characteristic $2$. If the characteristic of $F$ is different from $2$, then one can reconstruct the quadratic form directly from the bilinear form via $q(v) = \frac{1}{2}B(v, v)$.

Let's explore this a bit. Plug $w = v$ into the definition of $B(v, w)$:

$$B(v, v) = q(v + v) - q(v) - q(v) = q(2v) - 2q(v)$$

Since $q(2v) = 2^2 q(v) = 4q(v)$, this simplifies in every field $F$ to:

$$B(v, v) = 4q(v) - 2q(v) = \mathbf{2q(v)}$$

Now look at the difference between characteristic $\neq 2$ and characteristic $2$. When $\text{char}(F) \neq 2$ (like $\mathbb{R}$, $\mathbb{C}$, or $\mathbb{F}_p$ for odd primes $p = 3, 5, 7, \dots$), since $2 \neq 0$, you can divide both sides of $B(v, v) = 2q(v)$ by $2$: $q(v) = \frac{1}{2} B(v, v)$.
    
This means $q(v)$ and $B(v, w)$ contain the same information. You don't need a separate definition of a quadratic form—you can just start with any symmetric bilinear form $B(v, w) = v^T M w$ (where $M$ is a symmetric matrix), define $q(v) = \frac{1}{2} B(v, v) = \frac{1}{2} v^T M v$, set it equal to $0$, and the non-zero solutions $\langle v \rangle$ are the points of the quadric $\mathcal{Q}$.
    
But when $\text{char}(F) = 2$ (like $\mathbb{F}_2, \mathbb{F}_4, \mathbb{F}_8, \dots$, where $2 = 1 + 1 = 0$), multiplying by $2$ gives zero.

$$B(v, v) = 2q(v) = \mathbf{0} \quad \text{for all } v \in V\text{.}$$
    
We cannot recover $q(v)$ from $B(v, v)$ by dividing by $2$, because $2 = 0$. Look at a concrete example in $\mathbb{F}_2$: suppose $q(x_1, x_2) = c_1 x_1^2 + x_1 x_2 + c_2 x_2^2$. When we compute $B(v, w) = q(v + w) - q(v) - q(w)$ in characteristic $2$, the squared terms cancel out completely because $(v_1 + w_1)^2 - v_1^2 - w_1^2 = 2 v_1 w_1 = 0$. Only the cross-term $x_1 x_2$ survives in $B(v, w)$, while the diagonal squared terms $c_1 x_1^2 + c_2 x_2^2$ vanish from $B(v, w)$.
    
That is why we must define the quadratic form $q(v)$ first (to keep the diagonal squared terms $c_i b_i^2$), and why nondegeneracy requires checking both  $B(x, v) = 0$ for all $x$  and  $q(v) = 0$.

**An example of a cone and finding its radical**

Take the 3D cone in $PG(3, \mathbb{R})$ with coordinates $v = (x_0, x_1, x_2, x_3)$ and quadratic form:

$$q(v) = x_0^2 + x_1^2 - x_2^2 = 0 \quad (\text{notice } x_3 \text{ is missing!})$$

Its bilinear form is $B(x, v) = 2x_0 v_0 + 2x_1 v_1 - 2x_2 v_2$.
    
Now test the vertex point $V_{\text{tip}} = \langle (0, 0, 0, 1) \rangle$, where $v = (0, 0, 0, 1) \neq 0$:
    
Does $q(v) = 0$? Yes:  $0^2 + 0^2 - 0^2 = 0$. So $V_{\text{tip}} \in \mathcal{Q}$.
        
Does $B(x, v) = 0$ for all $x = (x_0, x_1, x_2, x_3)$? Yes:  $2x_0(0) + 2x_1(0) - 2x_2(0) = 0$ for every  $x \in \mathbb{R}^4$!
        
Because $v = (0, 0, 0, 1) \neq 0$ satisfies both $q(v) = 0$ and $B(x, v) = 0$ for all $x$, this quadratic form is degenerate, and $\langle (0, 0, 0, 1) \rangle$ is the singular vertex of the cone ($\text{Rad}(\mathcal{Q}) = \{\langle (0,0,0,1) \rangle\}$).

## Polygons

We refer to a configuration as a n-angle in the EEP, if it is a set of n points, no three collinear. The lines of this configuration are formed by connecting every possible pair of these initial points. Because no three points are collinear, any single line in this configuration contains $2$ of the generating points. Furthermore, from any single point, lines must be drawn to connect to all the remaining points in the set, meaning each point lies on exactly $n-1$ lines. 

Similarly, an n-lateral is a set of n lines, no three concurrent. The points of this configuration are formed by the intersections of every possible pair of these lines. Because no three lines are concurrent, any single intersection point in this configuration is formed by and lies on $2$ lines. Furthermore, any single line must intersect all the other lines in the set, meaning each line contains exactly $n-1$ intersection points.

The dual of a configuration can be obtained by replacing point ←→ line, collinear ←→ concurrent, join ←→ intersection.

These are obviously quite different from the regular squares or pentagons we encounter in high school. These configurations are used in projective geometry, whereas the ordinary polygons we study are in Euclidean geometry. These are called complete $n$-angles. By contrast, a square or a rectangle is a simple $n$-angle.

Here is how they differ. In the simple $n$-angle, you select $n$ points and connect them with exactly $n$ lines to form a closed loop or boundary. There are no lines connecting opposite corners (the diagonals). By contrast, in the complete $n$-angle, you select $n$ points and draw every possible line between them. For $4$ points, this means drawing $\binom{4}{2} = 6$ lines. A complete quadrangle includes the $4$ "outer" edges plus the $2$ "inner" diagonals as equal structural elements, completely ignoring the concept of an "inside" or "outside" boundary.

Now let's look at a few examples.

---

**Triangle:** Points ($v$): $3$ non-collinear vertices.

Lines ($b$): $\binom{3}{2} = 3$ joining lines.

Incidences: Each point lies on $2$ lines, and each line contains $2$ points.

In configuration notation, this is represented as the symmetric configuration $(3_2, 3_2)$ (or simply $(3_2)$). Interchanging points and lines yields $3$ lines and $3$ intersection points with the exact same incidence relations. Because it is isomorphic to its dual, the complete triangle is self-dual.

---

**Quadrangle:** Points ($v$): $4$ points, no three collinear.

Lines ($b$): The lines connecting pairs of points, giving $\binom{4}{2} = 6$ lines.

Incidences: Each of the $4$ points lies on $3$ lines, and each of the $6$ lines contains $2$ points.

The configuration symbol is: $(4_3, 6_2)$

---

**Quadrilateral:** Applying projective duality to the quadrangle (replacing points with lines and lines with points):

Lines ($b$): $4$ lines, no three concurrent.

Points ($v$): The intersection points of pairs of lines, giving $\binom{4}{2} = 6$ points.

Incidences: Each of the $6$ points lies on $2$ lines, and each of the $4$ lines contains $3$ points.

The dual configuration symbol is:

$$(6_2, 4_3)$$

These two are clearly not self-dual.

---

## References
- Projective Geometry: An Introduction by Rey Casse
- Projective Geometry: From Foundations to Applications by Albrecht Beutelspacher, Ute Rosenbaum
- Foundations of Incidence Geometry: Projective and Polar Spaces by Johannes Ueberberg
- An Introduction to Incidence Geometry by Bart De Bruyn
- The Geometry of the Classical Groups by DE Taylor
