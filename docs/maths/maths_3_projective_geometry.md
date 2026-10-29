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

This is called the Grassmann Dimension Formula or Grassmann's Identity. We'll talk about this a little bit more soon.

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

Nete that every finite projective plane of order 2 is a Fano Plane. In other words, the projective plane P has seven points and seven lines, and, with a suitable numbering 1, 2, 3, 4, 5, 6, 7 of the points, the lines of P are the points sets {1, 2, 3}, {1, 4, 5}, {1, 6, 7}, {2, 4, 7}, {2, 5, 6}, {3, 4, 6} and {3, 5, 7}.

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

### Grassman Formula for Intersection of Spaces

As we saw earlier, the Grassmann Dimension Formula or Grassmann's Identity relates the dimensions of two subspaces $U$ and $W$ to the dimensions of their intersection (meet) and their span (join). Because projective dimension is always $1$ less than the underlying vector space dimension (we'll talk about this soon), the formula looks identical in both settings, provided you use the convention that the empty projective subspace $\emptyset$ has projective dimension $-1$.

For any two projective subspaces $U$ and $W$ in a projective space $PG(n, \mathbb{F})$:

$$\dim(U) + \dim(W) = \dim(U \vee W) + \dim(U \cap W)$$

where: $U \vee W$ (Join / Span) is the smallest projective subspace containing both $U$ and $W$. $U \cap W$ (Meet / Intersection) is the largest projective subspace contained in both $U$ and $W$ (with $\dim(\emptyset) = -1$ if $U$ and $W$ are disjoint/skew).

When looking at the dimensions of subspaces, there is a concept called codimension which makes it easy to see how different subspaces interact. If $S \subset H$ and $\dim S = M - c$, then it has codimension $c$ inside $H$. Let $K \subset H$ have dimension $k$. Apply the Grassmann formula to find a minimum dimension of their intersection (where the span of these two subspaces is set to a maximum of M):

$$\dim(S \cap K) \ge (M - c) + k - M = k - c$$

Remember that in projective geometry, the empty set has dimension $\dim(\emptyset) = -1$, while a non-empty intersection (at least a point) requires $\dim(S \cap K) \ge \mathbf{0}$. Therefore, an intersection is guaranteed if and only if:

$$k - c \ge 0 \iff \mathbf{k \ge c} \quad (\text{Dimension} \ge \text{Codimension})$$

Let's look at some examples. A $\text{codim } c = 1$ subspace is forced to intersect a line $K ($\dim k = 1$) because dimension $1$ and codimension $1$ "fill each other out" (their vector space dimensions are $2$ and $m$ inside an $(m+1)$-dimensional vector space, summing to $m + 2 > m + 1$).

But $\text{codim } c = 2$ will not be filled out by $\dim k = 1$ (a line), leaving "wiggle room" for them to miss each other completely (just like two skew lines in $PG(3, F)$, where a line has $\dim 1$ but $\text{codim } 3 - 1 = 2$).
        
Again, $\text{codim } c = 2$ and $\dim k = 3$ will intersect in at least a $1$-dimensional line because $k - c = 3 - 2 = \mathbf{1} \ge 0$.

### A Few Properties of Projective Subspaces

If $\mathbf{P}$ be a projective space and $U$ be a subspace of $\mathbf{P}$, and $p$ be a point of $\mathbf{P}$ outside of $U$. We have:

$$\langle U, p \rangle = \bigcup \{pu \mid u \in U\}$$

In other words, the subspace $\langle U, p \rangle$ consists of the point $p$ and all points $z$ such that the line $pz$ meets the subspace $U$ in a point.

If $B$ is a basis of $U$, then $B \cup p$ is unsurprisingly a basis of $\langle U, p \rangle$. As a side note, if the number of basis elements is $d+1$, the dimension of $U$ is $d$. The dimension of $\langle U, p \rangle = d+1$.

Let $U_1$ and $U_2$ be two nonempty subspaces of a projective space $\mathbf{P}$. Then the subspace $\langle U_1, U_2 \rangle = \langle U_1 \cup U_2 \rangle$ generated by $U_1$ and $U_2$ is given directly by the union of all lines joining a point of $U_1$ to a point of $U_2$:

$$\langle U_1, U_2 \rangle = U_1 \cup U_2 \cup \bigcup \{u_1 u_2 \mid u_1 \in U_1,\, u_2 \in U_2,\, u_1 \neq u_2\}$$

If $U_1$ and $U_2$ are disjoint ($U_1 \cap U_2 = \emptyset$), this simplifies to the exact analogue of the single-point formula $\langle U, p \rangle = \bigcup \{pu \mid u \in U\}$:

$$\langle U_1, U_2 \rangle = \bigcup \{u_1 u_2 \mid u_1 \in U_1,\, u_2 \in U_2\}$$

In other words, a point $z \in \mathbf{P}$ lies in $\langle U_1, U_2 \rangle$ if and only if $z \in U_1 \cup U_2$ or there is a line through $z$ that intersects both $U_1$ and $U_2$.

If $\mathbf{P}$ is a projective space, $U$ a subspace, and $p$ a point not in $U$, then as we saw, $W = \langle U, p\rangle$ is a subspace of $\mathbf{P}$. If we take a point $q \neq p$ in $W$, then $W =  \langle U, p\rangle =  \langle U, q \rangle$. Nothing surprising here since for example, if you took a line and a point not on it, you would generate a plane with them. Take any other point on that plane and regenerate a new plane with the line and that new point. You end up with the same old plane!

Let $\mathbf{P}$ be a projective space, and let $U$ and $W$ be two subspaces of $\mathbf{P}$. $U$ and $W$ are called complementary if $U \cap W = \emptyset$ and $\langle U, W \rangle = \mathbf{P}$. In this case, if $W$ is of finite dimension $r$, $U$ is called a subspace of codimension $r + 1$. For example, a hyperplane has dimension $d-1$, while a point is complementary to it and has dimension $d=0$. We met this term "codimension" just a little while ago.

Let $\mathbf{P}$ be a $d$-dimensional projective space, and let $U$ and $W$ be two subspaces of $\mathbf{P}$ with $U \cap W = \emptyset$. Then, there exists a subspace $W'$ through $W$ such that $U$ and $W'$ are complementary. Note that $W'$ through $W$ implies that $W'$ contains $W$. Once we have that clarity, this proposition is obvious. If $U$ and $W$ are complementary then any $W'$ that $W$ is a subspace of must intersect $U$ by the Grassmann formula and the dimension/codimension analysis we did earlier.

## Vector Spaces and Projective Geometry
Purely axiomatic geometry (also called synthetic geometry) lacks a coordinate system, making it very difficult to compute transformations, intersections, or specific loci. We want to label these abstract points and lines with coordinates so we can calculate with them and get geometrical results by mechanically manipulating numbers. 

Before going further, we must point out that every axiomatic projective space of dimension greater than or equal to 3 can be constructed out of a $(d+1)$-dimensional vector space $V$ over some division ring (which includes skew fields) $K$. Note that a skew field ring is almost the same as a field, except that multiplication must commute in a field, but need not in a division ring. Inverses still commute and are unique. 

If dimension $d = 2$ i.e. if we are looking at projective planes, then we may not be able to find such vector spaces for certain projective planes called non-Desarguesian planes. Essentially, they cannot be embedded inside any 3D projective space. We will not bother about such planes here, but one important plane is the Moufang / Octonion Plane $\mathbb{O}\mathbb{P}^2$, which is built using the 8-dimensional Octonions $\mathbb{O}$, where multiplication is non-associative. Because octonions are not associative, you cannot form a true vector space over them, and $\mathbb{O}\mathbb{P}^2$ cannot exist inside any $\mathbb{O}\mathbb{P}^3$.

To make the geometry of a projective space calculable, we construct a $d$-dimensional projective space out of a standard $(d+1)$-dimensional vector space $V$ over a field $\mathbb{F}$ (such as $\mathbb{F}^3$ for a 2D projective plane). By intentionally defining projective objects as vector subspaces, the geometry inherits the robust machinery of linear algebra.

Think of it this way. Take a 3D vector space. Draw a vector from the origin. This vector will pierce the $z=1$ plane at a point. This point represents a point on the projective plane. Of course, the vector will pierce every plane $z = k \in \mathbf{C}$ except the $z=0$ plane. All these points are considered an equivalence class, which is no different from saying the $1D$ vector is equivalent to the projective point. The points at infinity are formed by the intersection of vectors with the $z=0$ plane at infinity. Thus:

A Projective Point is defined as a 1-dimensional vector subspace (a line extending through the origin in $V$). A Projective Line is defined as a 2-dimensional vector subspace (a plane extending through the origin in $V$). The Projective Plane (dimension $2$) is defined as the entire $3$D vector space $V = \mathbb{F}^3$. The "$-1$ relationship in dimensions continues into higher dimensions. 

This algebraic translation automatically satisfies the abstract axioms. For instance, the axiom stating "any two projective lines must intersect in exactly one projective point" simply becomes the standard linear algebra theorem: "In a 3-dimensional vector space, the intersection of any two distinct 2-dimensional subspaces must be a 1-dimensional subspace."

However, once again, as we saw earlier, we end up rules with qualifications. For example, two lines meet at a point - unless they are parallel. Another example: the intersection of $a_1x + b_1y = c_1$ and $a_2x + b_2y = c_2$ is found by Cramer's rule... unless the determinant is zero. A third example: a conic section can be an ellipse, a parabola, or a hyperbola... depending on how its asymptotes behave.

To avoid these qualifications, we saw how to add points at infinity where parallel lines meet. Similarly, conics stop having three different names: parabolas and hyperbolas are simply ellipses that happen to touch or cross at a point at infinity. 

To label all these points, we use something like the usual coordinate system of $(x, y)$ but add an additional $z$ coordinate such that the coordinates of the points on the line at infinity have $z=0$, while the other points are $z=1$. Of course, this leaves us in a bit of a quandary. What do the points with $z \neq 0, 1$ mean? We need to map these back to the affine plane somehow. The trick that is used is to simply normalize $(x, y, z)$ by $z$, so that $(\rho x, \rho y, \rho z)$ is the same as $(x, y, z)$. The ratio $X/Z$ and $Y/Z$ determines the point of the affine plane, and there is a whole equivalence class of coordinates in the projective plane, which differ only by the scale factor, that map to the same affine and projective plane point. For example, the equivalence class containing $(2, 4, 2)$ can be scaled by $1/2$ to become $(1, 2, 1)$. This class represents the specific finite affine point $(1, 2)$. 

When $z=0$, the $x$ and $y$ values capture the direction vector of a line. Once again, for example because $(4, 8, 0) = 2 \cdot (2, 4, 0)$, both triples belong to the same equivalence class. Geometrically, this makes sense: a direction vector from the origin to $(2, 4)$ points in the exact same direction (a slope of $2$) as a direction vector from the origin to $(4, 8)$. Therefore, they define the exact same point on the line at infinity. Note that these coordinates, called homogenous coordinates are not something new. They are just the coordinate values of each basis vector that is needed to describe a vector of the $d+1$-dimensional vector space. Essentially, if we fix a basis $\{v_0, v_1, \dots, v_d\}$ of $V$. Then we can express any vector as $v = a_0 v_0 + a_1 v_1 + \dots + a_d v_d \in V$ uniquely by its coordinates $(a_0, a_1, \dots, a_d)$ in that basis. Two homogenous coordinates $a$ and $b$ are an equivalence class and therefore the same point (as discussed above) if there is an $\alpha \in F \setminus \{0\}$ such that $(a_0, a_1, \dots, a_d) = \alpha \cdot (b_0, b_1, \dots, b_d)$

The vector space model directly reproduces the axiomatic count $q^2 + q + 1$. The ambient vector space $V = \mathbb{F}_q^3$ has $q^3$ total vectors. Remove the origin $\mathbf{0}$: $q^3 - 1$ non-zero vectors. Every $1$-dimensional vector subspace contains $q - 1$ non-zero scalar multiples of its spanning (unit) vector. The total number of $1$-dimensional subspaces (projective points) is: $\frac{q^3 - 1}{q - 1} = q^2 + q + 1$.

By mapping the projective plane to subspaces of $\mathbb{F}^3$, geometry instantly inherits the computational tools of linear algebra:

Finding the line through two points $\mathbf{p}_1, \mathbf{p}_2$: Take the vector cross product: $\boldsymbol{\ell} = \mathbf{p}_1 \times \mathbf{p}_2$
    
Finding the intersection of two lines $\boldsymbol{\ell}_1, \boldsymbol{\ell}_2$: Take the exact same cross product: $\mathbf{p} = \boldsymbol{\ell}_1 \times \boldsymbol{\ell}_2$
    
Checking if a point $\mathbf{p} = (x, y, z)$ lies on a line $\boldsymbol{\ell} = [a, b, c]$: Take the standard dot product: $\boldsymbol{\ell} \cdot \mathbf{p} = ax + by + cz = 0$
    
Checking collinearity of three points: Compute a single $3 \times 3$ determinant: $\det \begin{pmatrix} x_1 & y_1 & z_1 \\ x_2 & y_2 & z_2 \\ x_3 & y_3 & z_3 \end{pmatrix} = 0$

Geometric problems become straightforward matrix and vector calculations. These rules generalize to higher dimensions $PG(n, \mathbb{F})$ where the 3D cross product is replaced by the exterior wedge product ($\wedge$) and Plücker coordinates, which we won't immediately bother about right now. Similarly, in higher dimensions, we can use the dot product rule to check incidence of a point with a hyperplane. To check incidence between a point and a line or non-hyperplanes, we must take multiple dot products between the point and each additional linear constraint equation.

The vector space representation also includes the principle of duality. For example, because a point is a 1D subspace of $\mathbb{F}^3$ and a line is a 2D subspace of $\mathbb{F}^3$, the incidence condition:

$$ax + by + cz = 0$$

is completely symmetric between the point coordinates $(x, y, z)$ and the line coordinates $[a, b, c]$.

In linear algebra over a 3D vector space, a 2D subspace (a plane through the origin) is uniquely defined by its 1D normal vector (an element of the dual space $V^*$). This means every theorem true for points and lines is automatically true if you swap the words "point" and "line". You prove a theorem once, and you get its dual theorem for free without any additional work.

Note that these relations hold in higher dimensions as well between points and hyperplanes. Also, we have assumed that we are operating with left vector spaces, which is a fancy way of saying that we are using row vectors for the homogenous coordinates of points, and when we want to transform a row vector with a matrix, we do $v.M$ (not $M.v$). With right vector spaces, this flips.

Additionally, the coordinates of a line/hyperplane may be written as $[a, b, c... ]$, but we actually mean a column vector $[a, b, c... ]^T$. Thus, the test for incidence being a dot product makes more sense now. It is simply $(x, y, z...)\cdot[a, b, c... ]^T$.

Thus, a hyperplane is always defined by a linear equation, $x_0 a_0 + \dots + x_d a_d = 0$, which is pretty much what we see with a line on a plane. The homogenous coordinates of any point on this hyperplane satisify this equation. If however, we want to find the unique hyperplane passing through $d$ points, we plug the coordinates of the $d$ points into the hyperplane equation:

$$\begin{aligned} x_0^{(1)} a_0 + x_1^{(1)} a_1 + \dots + x_d^{(1)} a_d &= 0 \\ x_0^{(2)} a_0 + x_1^{(2)} a_1 + \dots + x_d^{(2)} a_d &= 0 \\ &\;\;\vdots \\ x_0^{(d)} a_0 + x_1^{(d)} a_1 + \dots + x_d^{(d)} a_d &= 0 \end{aligned}$$

This is a system of $d$ equations over $d+1$ unknowns (the homogenous coordinates of the hyperplane). A system of $d$ independent homogeneous equations in $d+1$ unknowns has a 1-dimensional space of solutions, which gives the unique homogeneous coordinate vector $[a_0, a_1, \dots, a_d]^T$ (up to a right scalar multiple) of the hyperplane $H$.

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

Note that not every BIBD represents the number of $d$-dimensional subspaces in a $n$-dimensional projective space. The vast majority of BIBDs have parameters $(v, b, r, k, \lambda)$ that do not match any Gaussian binomial coefficients and have no connection to $PG(n, q)$.The relationship is strictly one-way: every system of points and $d$-dimensional subspaces in $PG(n, q)$ forms a $2\text{-}(v, k, \lambda)$ BIBD (whose parameters are given by Gaussian binomials). Almost no general BIBD comes from a projective space $PG(n, q)$.

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

What is the size of the hyperboloid throat? Suppose your top and bottom circular rims at $z = +H$ and $z = -H$ both have radius $R$. Take a single rod connecting angle $\theta = 0$ on the bottom rim to angle $\theta = \phi$ on the top rim. The bottom endpoint ($z = -H$):  $A = (R, \, 0, \, -H)$. The top endpoint ($z = +H$):  $B = (R \cos \phi, \, R \sin \phi, \, +H)$    

Where does this straight rod pass through the central waist plane $z = 0$? Exactly at the midpoint $M = \frac{1}{2}(A + B)$ between the top and bottom endpoints. 

$$M = \left( R \frac{1 + \cos \phi}{2}, \; R \frac{\sin \phi}{2}, \; 0 \right)$$.

Now calculate the distance $r_{\text{throat}}$ of this midpoint $M$ from the central $z$-axis $(0,0,0)$ using the half-angle trig identities ($1 + \cos \phi = 2\cos^2(\phi/2)$ and $\sin \phi = 2\sin(\phi/2)\cos(\phi/2)$):

$$r_{\text{throat}} = \sqrt{x_M^2 + y_M^2} = R \cdot \cos\left(\frac{\phi}{2}\right)$$

So if $\phi = 0^\circ$ (no twist), $\cos(0^\circ) = 1 \implies r_{\text{throat}} = R$. It is an untwisted cylinder; the lines are parallel and meet only at the single point at infinity (creating a degenerate cone/cylinder, not a regulus of skew lines).
    
If $0^\circ \lt \phi \lt 180^\circ$ (any intermediate twist), $0 < r_{\text{throat}} < R$. The lines are mutually skew and carve out an open circular throat of radius $R \cos(\phi/2)$.

At $\phi = 90^\circ$,  $r_{\text{throat}} = R \cos(45^\circ) = \frac{R}{\sqrt{2}} \approx 0.707 R$. At $\phi = 120^\circ$,  $r_{\text{throat}} = R \cos(60^\circ) = 0.5 R$ (the throat is exactly half the width of the top/bottom rims).
        
For $\phi = 180^\circ$ (half-turn twist), $\cos(90^\circ) = 0 \implies r_{\text{throat}} = 0$. Every rod connects $(x, y, -H)$ to $(-x, -y, +H)$, passing straight through the origin $(0,0,0)$. The throat pinches completely shut into a double cone, and the lines are no longer skew.

Also note while the height $H$ of the cylinder doesn't change the throat radius $r_{\text{throat}}$ at $z=0$, changing $H$ changes the slope of the rods—taller $H$ makes a tall, gentle hourglass; shorter $H$ makes a wide, flared hourglass.

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

Now let's look at how many points and lines are there in a regulus. A regulus has as many lines as there are points on a projective line ($\vert{}F\vert{} + 1$ lines). Over $\mathbb{R}$, there are infinitely many lines in $\mathcal{R}$ and infinitely many in $\mathcal{R}'$. Over a finite field $\mathbb{F}_q$, there are $q+1$ lines in $\mathcal{R}$ and $q+1$ lines in $\mathcal{R}'$, forming a $(q+1) \times (q+1)$ grid of $(q+1)^2$ points. 

Let's test a single point $P$ on $g_1$ to see how many transversals can pass through it:

Take the point $P \in g_1$ and span it with the entire second line $g_2$. This creates a single flat 2D plane,  $\Pi = \langle P, g_2 \rangle$.
    
Now look at the third line $g_3$. In 3D projective space, a line ($g_3$) and a plane ($\Pi$) that does not contain it intersect in exactly one point, let's call it $R = \Pi \cap g_3$.
    
Draw the line connecting $P$ and $R$. Because both $P$ and $R$ lie inside the plane $\Pi = \langle P, g_2 \rangle$, the line $PR$ lies completely inside $\Pi$. $g_2$ also lies completely inside this plane. Two lines in the same plane must intersect, so the line $PR$ is forced to intersect $g_2$ at some unique point $Q$.

This is a remarkable geometric constraint:  through every single point $P$ on $g_1$, there is one—and only one—straight line $h_P$ that hits both $g_2$ and $g_3$.

As you slide the point $P$ along $g_1$, this unique transversal line $h_P$ slides along $g_1, g_2,$ and $g_3$ simultaneously. Instead of filling the 3D volume, this 1-parameter family of straight lines [sweeps out a 2-dimensional curved saddle/hourglass surface](https://www.youtube.com/shorts/SoqpsRKFf6k) (in real space, a hyperboloid of one sheet, like a nuclear power plant cooling tower).

What is the significance of the 16-point theorem? In the 16-point theorem, we only talk of 16 points because, we start with three skew lines $g_1, g_2, g_3$ which are fixed as a starting reference frame, and we pick three fixed transversals $h_1, h_2, h_3$ (which automatically gives $3 \times 3 = 9$ intersection points). Now, to prove that every line $g \in \mathcal{R}$ meets every line $h \in \mathcal{R}'$, we pick one arbitrary fourth transversal $g$ of $\{h_1, h_2, h_3\}$ (giving $3$ more intersection points) and one arbitrary fourth transversal $h$ of $\{g_1, g_2, g_3\}$ (giving $3$ more intersection points). We now have $9 + 3 + 3 = 15$ guaranteed intersections in a $4 \times 4$ grid. The theorem asks:  Must $g$ and $h$ intersect at corner 16?

Because $g$ and $h$ were chosen as arbitrary fourth transversals, proving that they must intersect at the 16th point proves that every transversal of $\{h_1, h_2, h_3\}$ intersects every transversal of $\{g_1, g_2, g_3\}$. A regulus exists if and only if that 16th intersection closes up for every choice of $g$ and $h$, which happens if and only if $F$ is commutative i.e. the order of multiplcation of two numbers doesn't matter.

Thus if $g_1, g_2, g_3$ be three skew lines of $\mathbf{P}$, there is exactly one regulus through $g_1, g_2$, and $g_3$ if $F$ is commutative. If $F$ is noncommutative, then there is no regulus in $\mathbf{P}$.

Let's explore how the commutative requirement is forced by the 16-point theorem. Let $\mathbf{P}$ be a $3$-dimensional projective space over the field $F$ which is represented by homogeneous coordinates. Let:

$$\begin{aligned} g_1 &= \langle (1 : 0 : 0 : 0),\, (0 : 1 : 0 : 0) \rangle, \\ g_2 &= \langle (0 : 0 : 1 : 0),\, (0 : 0 : 0 : 1) \rangle, \\ g_3 &= \langle (1 : 0 : 1 : 0),\, (0 : 1 : 0 : 1) \rangle \end{aligned}$$

be three skew lines. Now lets figure out the condition on the set $\mathcal{Q}$ of points on the uniquely determined regulus $\mathcal{R}$ through $g_1, g_2, g_3$. This condition is:

$$\mathcal{Q} = \left\{(a_0 : a_1 : a_2 : a_3) \;\middle\vert{}\; a_0 a_3 = a_1 a_2 \text{ with } a_i \in F,\text{ not all } a_i = 0\right\}$$

Therefore, the coordinates of the points of $\mathcal{Q}$ satisfy the quadratic equation: $x_0 x_3 - x_1 x_2 = 0$. The surface $\mathcal{Q}$ is the hyperbolic quadric in $PG(3, F)$ (also known as the Segre quadric or Klein quadric in miniature). It demonstrates that you can construct and study a curved 2nd-degree algebraic surface ($x_0 x_3 - x_1 x_2 = 0$) using nothing but straight lines and incidence axioms (three skew lines and their transversals).

How does the quadratic condition come about? A line $h$ is a transversal of $\{g_1, g_2, g_3\}$ if it intersects $g_1$ at some point $P_1$,  $g_2$ at some point $P_2$, and $g_3$ at some point $P_3$.

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
    
If $ab \neq ba$ (for example, in the Quaternions $\mathbb{H}$ where $i \cdot j = k$ but $j \cdot i = -k$), the point on $h_b$ is $(1 : j : i : k)$ while the point on $g_a$ is $(1 : j : i : -k)$. Because $k \neq -k$, the two lines pass right by each other in 3D space without touching.

This is pretty much the same as differential geometry, where if you have two vector fields $X$ and $Y$ in 3D space, you can flow along $X$ by distance $a$ and then along $Y$ by distance $b$, or flow along $Y$ by $b$ and then along $X$ by $a$. Do those two paths land on the exact same 4th corner to weave a 2D coordinate grid (a surface)? Only if the Lie bracket vanishes ($[X, Y] = XY - YX = 0$, or $\partial_x \partial_y = \partial_y \partial_x$). If not, the 4th corner fails to close, and the flows twist into 3D volume instead of staying on a 2D surface.
    
Both the projective geometry and the differential geometry observations are two manifestations of the exact same structural principle: integrability (closure of a 2D mesh in a 3D+ space).

In higher dimensions, hyperbolic quadrics (like $x_0 x_5 - x_1 x_4 + x_2 x_3 = 0$ in $PG(5, F)$—the Klein Quadric) are completely ruled not just by straight lines ($1$D subspaces), but by entire flat planes ($2$D subspaces), called generators. Specifically, the Klein quadric in 5D space is woven from two opposite families of flat 2D planes (often called $\alpha$-planes and $\beta$-planes), directly generalizing the two reguli $\mathcal{R}$ and $\mathcal{R}'$ of lines in 3D. The expression $x_0 x_5 - x_1 x_4 + x_2 x_3 = 0$ comes directly from the wedge product (exterior algebra), and the determinant used in the area of a parallelogram or triangle (specifically,  $2 \times 2$ minors and the Laplace cofactor expansion). It is related to the Pfaffian of a $4 \times 4$ skew-symmetric matrix.
    
Also, the mapping $(1 : a) \times (1 : b) \mapsto (1 : b : a : ab)$ is the simplest case of the Segre Embedding $\mathbb{P}^1 \times \mathbb{P}^1 \hookrightarrow \mathbb{P}^3$, which embeds the product of two lines as a curved quadric in 3D space. In general, you can embed $\mathbb{P}^n \times \mathbb{P}^m$ into $\mathbb{P}^{(n+1)(m+1)-1}$ using $x_{ij} = a_i b_j$.

What we showed in this section bridges three seemingly distinct areas of mathematics—pure incidence geometry (skew lines and transversals),  abstract algebra (whether multiplication in the coordinate division ring $F$ is commutative:  $ab = ba$), and algebraic geometry (curved quadratic surfaces, or quadrics).

### What Does A Hyperbolic Quadric Look Like?
What it "looks like" depends on whether you view it in projective space, an affine slice, or over a finite field.

In 3D Projective Space $PG(3, F)$ (over any field), there is no distinction between "finite" points and "points at infinity." The regulus $\mathcal{R}$ and opposite regulus $\mathcal{R}'$ form a completely symmetric, closed grid:  $\mathbb{P}^1(F) \times \mathbb{P}^1(F)$.
    
Over $\mathbb{R}$, a projective line $\mathbb{P}^1(\mathbb{R})$ is a closed circle $S^1$ (a line whose two ends meet at the point at infinity). Thus, in $PG(3, \mathbb{R})$, the surface is topologically a torus ($S^1 \times S^1$).
        
Over a finite field $\mathbb{F}_q$, a projective line $\mathbb{P}^1(\mathbb{F}_q)$ is a discrete set of $q+1$ points. Thus, in $PG(3, q)$, the hyperbolic quadric $Q^+(3, q)$ is literally a finite $(q+1) \times (q+1)$ combinatorial grid of $(q+1)^2$ points, woven from $q+1$ skew lines of $\mathcal{R}$ and $q+1$ skew lines of $\mathcal{R}'$. There is no continuous "curvature" in a finite field, yet every algebraic and incidence property of the hyperboloid (every line of $\mathcal{R}$ meets every line of $\mathcal{R}'$, tangent planes cut out a pair of intersecting lines, etc.) holds identically.
        
In 3D Affine Space (When You Slice Away a Plane at Infinity), depending on which plane you choose as the plane at infinity in $PG(3, \mathbb{R})$, the exact same projective regulus $x_0 x_3 - x_1 x_2 = 0$ appears as two different familiar 3D surfaces:
    
**Hyperboloid of One Sheet ($x^2 + y^2 - z^2 = 1$):** If you choose a plane at infinity that does _not_ contain any lines of the regulus (it cuts the quadric in an ellipse at infinity), the affine remainder is the hourglass hyperboloid of one sheet.
        
**Hyperbolic Paraboloid / Pringles Saddle ($z = xy$):** Look directly at $x_0 x_3 - x_1 x_2 = 0$ and set the affine plane at infinity to be $x_0 = 0$. Normalizing $x_0 = 1$ and writing $(x_1, x_2, x_3) = (x, y, z)$ gives **$z = xy$**! Why does it look like a saddle instead of an hourglass? Because the plane at infinity $x_0 = 0$ is _tangent_ to the quadric and contains two lines of the reguli (pushing the closed waist out to infinity). Projectively, the hourglass ($x^2 + y^2 - z^2 = 1$) and the saddle ($z = xy$) are the exact same geometric object.

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

When $d = 2$ i.e. a plane, skew lines cannot exist ($\dim(g \cap h) = 1 + 1 - 2 = 0$, so any two lines must intersect). In $d = 3$ (3-Space), two lines have codimension $2$ each, so they typically miss each other. A plane ($2$D) and a line ($1$D) always meet at a point ($2 + 1 - 3 = 0$). Therefore, $3$ skew lines uniquely determine a 1-parameter family of transversals (a 2D surface). If $d \ge 4$, for example in 4D space, a plane ($2$D) and a line ($1$D) generally miss each other completely ($2 + 1 - 4 = -1$). If you pick three skew lines in 4D space, there is typically only one single transversal line (or none) in total, rather than a continuous surface of them. Thus, the classical regulus of lines is an intrinsically 3-dimensional phenomenon.

If a regulus of lines only works in 3D, how do we get hyperbolic quadrics in higher dimensions? We noted that in $d = 3$, a line ($\dim = 1$) is guaranteed to intersect a plane ($\dim = 2$) in a point because $1 + 2 - 3 = 0$. In higher odd-dimensional projective spaces $PG(2m-1, F)$, the exact same intersection guarantee holds—not between two lines, but between $(m-1)$-dimensional subspaces.

In $PG(5,F)$ where $d=5$ for example, the equation becomes $x_0 x_5 - x_1 x_4 + x_2 x_3 = 0$. A regulus is woven from two families of flat 2D planes ($\alpha$-planes and $\beta$-planes). 

In general, if $d = 2m - 1$ in $PG(2m-1, F)$, the equation is $\sum_{i=1}^{m} x_{i} y_{i} = 0$. The regulus is woven from two families of $(m-1)$-dimensional flat subspaces. In general, a quadric in $PG(2m-1, F)$ is called hyperbolic (denoted $Q^+(2m-1, F)$) because it is the unique type of non-degenerate quadric that is completely ruled by flat $(m-1)$-dimensional projective subspaces (the maximum possible dimension of a flat subspace that can sit inside a $(2m-2)$-dimensional curved surface).

Note that in higher dimensional spaces, an $m$-regulus in $PG(2m-1, q)$ specifically means a set of $q + 1$  mutually disjoint  $(m-1)$-subspaces such that every line meeting three of them meets all $q + 1$ of them.

## Quadratic Sets

Just as earlier we defined projective spaces purely using points and lines before proving they come from vector spaces, Buekenhout’s synthetic theory of quadrics allows us to define degree-2 curved surfaces (quadrics) purely using point-line incidence rules—without writing a single quadratic equation or taking a single derivative.

A quadric is defined by a homogeneous degree-2 polynomial equation in coordinates. This requires the space to already have coordinates over a commutative field $F$. A Quadratic Set is defined purely by how straight lines intersect the point set $\mathcal{Q}$, with no coordinates, no equations, and no calculus.

Why do this? It allows us to study quadrics in non-Desarguesian planes or over finite fields (including characteristic $2$, where $1+1=0$ breaks standard calculus derivatives) using only clean geometric arguments.

Every algebraic quadric automatically satisfies the two axioms of a quadratic set, which we will define below. And remarkably, the converse is more or less true: in finite projective spaces of dimension $d \ge 3$, almost every quadratic set is an algebraic quadric.

Let $\mathcal{Q}$ be a set of points of the projective space $\mathbf{P}$. We call a line $g$ a tangent of $\mathcal{Q}$ if either $g$ has just one point in common with $\mathcal{Q}$ or each point of $g$ is contained in $\mathcal{Q}$. A line where every point lies in $\mathcal{Q}$, i.e. the entire line is contained in the set, is also called a $\mathcal{Q}$-line. In general, we call a subspace $U$ a $\mathcal{Q}$-subspace if each point of $U$ lies in $\mathcal{Q}$.
    
For each point $P$ of $\mathcal{Q}$, let the set $\mathcal{Q}_P$ consist of the point $P$ and all points $X \neq P$ of $\mathbf{P}$ such that the line $XP$ is a tangent of $\mathcal{Q}$. $\mathcal{Q}_P$ is called the tangent space of $\mathcal{Q}$ at the point $P$.

### Visualizing The Tangent Plane

When you place a tangent plane against a sphere at a point $P$, the entire sphere stays on one side of the plane, so the plane only touches the sphere at that single point $P$.

On a hyperbolic quadric (which is shaped like a saddle or hourglass at every point $P$), the surface curves away from the plane in one direction (up/down along the hourglass) and curves _into_ the plane in the perpendicular direction (around the waist). Because of this saddle shape, the flat tangent plane $\mathcal{Q}_P = \langle g, h \rangle$ cannot stay strictly on the outside of the hourglass—it physically cuts right through the wall of the hourglass, dividing the surface into pieces in front of the plane and behind the plane.

### Axioms of Quadratic Sets
    
We call the set $\mathcal{Q}$ a quadratic set of $\mathbf{P}$ if it satisfies the following conditions:
    
**If-three-then-all axiom:** Any line $g$ that contains at least three points of $\mathcal{Q}$ is totally contained in $\mathcal{Q}$ (which means that each point of $g$ lies in $\mathcal{Q}$). In other words, any line has $0$,  $1$,  $2$, or all points in common with $\mathcal{Q}$. Note that a line that meets $\mathcal{Q}$ in $2$ points is called a secant. If it meets $\mathcal{Q}$ at $0$ points i.e. it does not meet the set at all, it is called a passant. The other two possibilities are tangents.
        
**Tangent-space axiom:** For any point $P \in \mathcal{Q}$, its tangent space $\mathcal{Q}_P$ is the set of points in a hyperplane or the set of all points of $\mathbf{P}$. Another way to put this is, for any point $P$ of $\mathcal{Q}$, either $\mathcal{Q}_P$ is a hyperplane, which means any line through $P$ in $\mathcal{Q}_P$ is a tangent, and no line through $P$ outside $\mathcal{Q}_P$ is a tangent (each such line contains exactly one further point of $\mathcal{Q}$). Or, $\mathcal{Q}_P$ is equal to $\mathbf{P}$, and so each line through $P$ is a tangent.

### The First Axiom

Let's take a closer look at the first axiom. Look at how the "If-three-then-all" axiom captures "degree 2" without algebra. If you intersect a straight line (parameterized by $t$) with an algebraic surface defined by a degree-2 polynomial $f(t) = a t^2 + b t + c = 0$, how many solutions can a quadratic equation have? $0$ solutions (the line misses the surface—a passant), $1$ solution (a double root $b^2 - 4ac = 0$—the line touches at $1$ point), $2$ solutions (two distinct roots—the line pierces in and pierces out, a secant), or more than $2$ solutions. But, the only way a quadratic polynomial $a t^2 + b t + c = 0$ can have 3 roots is if $a = b = c = 0$, meaning $f(t) = 0$ for all $t$, which means the entire line lies inside the surface since it is parametrized by $t$ i.e. we create the line by varying $t$.

How can an entire tangent line lie in a quadric. In 2D Euclidean geometry, we only study curves like circles ($x^2 + y^2 = 1$), which cannot contain straight lines, so we learn that a tangent line touches at $1$ point. 

Move to 3D Euclidean geometry and look at two surfaces we already know: a Cylinder ($x^2 + y^2 = 1$) or our Hyperboloid of One Sheet ($x^2 + y^2 - z^2 = 1$). Because the hyperbolic quadric in 3D space is a doubly ruled surface, it is made of straight lines, so the idea that a straight line is entirely contained in the surface is not that odd. 

For example, take a point $P$ on the side of a smooth vertical cylinder, and place a flat sheet of metal (the Euclidean tangent plane $\Pi_P$) flush against the cylinder at $P$. Because the cylinder is made of vertical straight lines, that vertical line in the tangent plane rests flush against the cylinder along its entire infinite length. Every point of that vertical line is in $\mathcal{Q}$.

The exact same thing happens on the hyperboloid of one sheet (our regulus $\mathcal{Q}$). At any point $P \in \mathcal{Q}$, the calculus tangent plane $\Pi_P$ contains one line $g \in \mathcal{R}$ and one line $h \in \mathcal{R}'$ passing through $P$. Every other line in $\Pi_P$ through $P$ meets the hyperboloid only at $P$ ($1$ point). The two lines $g$ and $h$ lie inside $\Pi_P$, and they lie completely inside $\mathcal{Q}$ (all points).

In fact, a $\mathcal{Q}$-line is simply the synthetic-geometry name for a ruling (or generator) of a surface: a straight line every single point of which lies inside $\mathcal{Q}$. It is a generator because we can slide the line across one of the skew lines (by changing the point where it intersects with the skew line, so the skew line serves as a guide rail) to generate the entire hyperbolic quadric (in 3D). In higher dimensions, we would not use a $\mathcal{Q}$-line but a maximal flat subspace that lies completely inside $\mathcal{Q}$.

Note that if we did not count $\mathcal{Q}$-lines (lines completely inside $\mathcal{Q}$) as "tangent lines," then the tangent plane $\Pi_P$ to a cylinder would have a missing vertical line ripped out of it, and the tangent plane to a hyperboloid would have two missing lines ($g$ and $h$) ripped out of it. By defining a tangent line as meeting $\mathcal{Q}$ in either $1$ point OR all points, the union of all tangent lines through $P$ forms a complete, unbroken flat hyperplane $\mathcal{Q}_P$.

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

If $P$ is a sharp pinch / singular vertex of $\mathcal{Q}$ then $\mathcal{Q}_P = \mathbf{P}$, the whole space. Imagine a double cone with its sharp tip (vertex) at $V$. Stand at the vertex $V$ and shoot a line in any direction in 3D space. If you shoot along the wall of the cone, the entire line lies in the cone (making it a $\mathcal{Q}$-line and thus a tangent). If you shoot in any other direction through $V$, the line only touches the cone right at the tip $V$ ($1$ point $\implies$ tangent). No line through the vertex $V$ can ever be a 2-point secant. Therefore, every line through the vertex $V$ is a tangent line, which means the tangent space $\mathcal{Q}_V$ is the entire 3D space $\mathbf{P}$.

In fact, this gives a purely geometric definition of a singular point (pinch/vertex): a point $P \in \mathcal{Q}$ is singular if and only if $\mathcal{Q}_P = \mathbf{P}$.

It's pertinent to point out that another condition that implies a point $P$ is singular is that every line connecting $P$ to a point $X \in \mathcal{Q}$ is a $\mathcal{Q}$-line. If every line connecting $P$ to a point of the quadric is entirely contained in the quadric, it means there are no lines through $P$ that are secants of the quadric! Thus, you can take any point in the space and send a line from it to $P$ and you are guaranteed a tangent, meaning $P$ is singular.

### Examples of Quadratic Sets

The empty set, any set consisting of just one point, the set of points on a line, the set of all points of a subspace are all quadratic sets. These quadratic sets $\mathcal{Q}$ have the property that for each point $P \in \mathcal{Q}$ the set $\mathcal{Q}_P$ equals $\mathbf{P}$.

Why is the set of all points of a subspace $U$ a quadratic set? Suppose $\mathcal{Q} = U$ is a flat linear subspace of $\mathbf{P}$ (for example, $\mathcal{Q}$ is a single point, or a single straight line, or a single flat plane in 3D space). 

Let's check the "If-three-then-all" axiom. Suppose a line $g$ contains $3$ points of the subspace $U$. By definition of a linear subspace (which means a linear combination of any two points in the subspace must also be in the subspace), if a line has even $2$ points in $U$, the entire line $g$ lies inside $U$, because a line is essentially parametrized by a variable $\lambda$ and two points - $a + \lambda b$. So a line can only meet a subspace $U$ in $0$ points, $1$ point, or all points, it can never meet a flat subspace in just $2$ points. Thus, the first axiom is trivially satisfied.

This same logic also assures satisfying the Tangent-Space axiom and why $\mathcal{Q}_P = \mathbf{P}$. Pick any point $P \in U$, and take any line $g$ in the entire space $\mathbf{P}$ that passes through $P$. How many points can $g$ share with $U$? Since $P$ is already on both $g$ and $U$, they share at least $1$ point ($P$). If $g$ shares no other points with $U$, then $\vert{}g \cap U\vert{} = 1 \implies g$ is a tangent. If $g$ shares even one more point with $U$, then because $U$ is a linear subspace, all points of $g$ lie in $U \implies g$ is a $\mathcal{Q}$-line $\implies g$ is also a tangent.

Because a line through $P \in U$ can never intersect a flat subspace $U$ in exactly $2$ points, every single line in $\mathbf{P}$ passing through $P$ is a tangent to $U$. Therefore, for every $P \in U$, the tangent space $\mathcal{Q}_P$ is the entire ambient space $\mathbf{P}$, satisfying the second axiom.
    
Another example of a quadratic set is the set of points in the union of two hyperplanes $H_1, H_2$ of $\mathbf{P}$. For each point $P \in H_1 \cap H_2$ we have that $\mathcal{Q}_P$ consists of all points of $\mathbf{P}$, while the points $P \in H_i \setminus (H_1 \cap H_2)$ satisfy $\mathcal{Q}_P = H_i$ ($i = 1, 2$).
    
From elementary geometry we get more examples. Each circle (and each ellipse) in the Euclidean plane is a quadratic set. (Here the tangent spaces are just lines.) Also, the sphere in $3$-dimensional (or $d$-dimensional) real affine space is a quadratic set. In real $3$-dimensional space there exist two other, quite different quadratic sets. These are, first of all, the cones; here, there is a point $V$, the vertex of the cone, such that $\mathcal{Q}_V$ is the whole space. Finally, there is the hyperbolic quadric.

### Properties of Quadratic Sets

The radical $\text{Rad}(\mathcal{Q})$ is the set of all singular points of $\mathcal{Q}$—meaning all points $S \in \mathcal{Q}$ whose tangent space is the entire ambient space ($\mathcal{Q}_S = \mathbf{P}$). 

In geometry, a quadratic set $\mathcal{Q}$ is called nondegenerate if $\text{Rad}(\mathcal{Q}) = \emptyset$ (it has no singular pinch points at all—like a smooth sphere or a hyperbolic quadric). It is degenerate if $\text{Rad}(\mathcal{Q}) \neq \emptyset$ (it has at least one singular point—like a cone or a cylinder).

Now let $\mathcal{Q}$ be a quadratic set of $\mathbf{P}$. 

> Then the radical of $\mathcal{Q}$ is a linear subspace of $\mathbf{P}$.

> Let $U$ be a complement of $\text{Rad}(\mathcal{Q})$ (that is, a subspace $U$ such that $U \cap \text{Rad}(\mathcal{Q}) = \emptyset$ and $\langle U, \text{Rad}(\mathcal{Q}) \rangle = \mathbf{P}$). Then $\mathcal{Q}' := \mathcal{Q} \cap U$ is a nondegenerate quadratic set of $U$.

>$\mathcal{Q}$ can be described as follows: $\mathcal{Q}$ consists of all points that lie on lines that join a point of $\text{Rad}(\mathcal{Q})$ with a point of $\mathcal{Q}' = \mathcal{Q} \cap U$.

These 3 points prove that every degenerate quadratic set is simply a cone (or cylinder) built over a smaller, smooth nondegenerate quadratic set.

Picture a double cone $\mathcal{Q}$ in 3D space with its sharp vertex at the point $V$. What is the radical? What is the only singular point of the cone $\mathcal{Q}$? The vertex $V$. So $\text{Rad}(\mathcal{Q}) = \{V\}$ (a $0$-dimensional subspace).
    
What is the complement $U$ and base $\mathcal{Q}'$? Pick a flat subspace $U$ of maximal dimension that completely misses the vertex $V$. Since $V$ is a point ($0$D) in 3D space, a complement $U$ is any 2D plane that does not pass through $V$ (for instance, a horizontal plane below the vertex). Note that "complement" in projective geometry (and linear algebra) does not mean the set-theoretic difference $\mathbf{P} \setminus \text{Rad}(\mathcal{Q})$. It means a complementary subspace $U$ which alongwith the radical can span the entire projective space. A vertex and a flat plane can do this in the current case. 

Now intersect the cone $\mathcal{Q}$ with that flat plane $U$. What do you get when you slice a cone horizontally with a plane $U$ that misses the vertex?  A smooth circle/ellipse (conic) $\mathcal{Q}'$ inside the plane $U$. Because that circle $\mathcal{Q}'$ has no sharp pinch points,  $\mathcal{Q}'$ is a nondegenerate quadratic set inside the plane $U$.
    
Now how do you rebuild the entire 3D cone $\mathcal{Q}$ starting only from the vertex $\text{Rad}(\mathcal{Q}) = \{V\}$ and the flat circle $\mathcal{Q}'$ down in the plane $U$? You draw a straight line from the vertex $V$ to every point $X$ on the circle $\mathcal{Q}'$! The set of all points on all those connecting lines $VX$ is the entire 3D cone $\mathcal{Q}$.

Now let $\mathcal{Q}$ be a quadratic set of $\mathbf{P}$. If $\mathcal{Q}$ is nondegenerate, then for any two distinct points $P, R \in \mathcal{Q}$ we have $\mathcal{Q}_P \neq \mathcal{Q}_R$. 

In other words, the quadratic set that is induced by $\mathcal{Q}$ in a tangent space $\mathcal{Q}_P$ has a radical that consists of just one point, namely $P$.

First, what does quadratic set induced by $\mathcal{Q}$ in $\mathcal{Q}_P$ mean? $\mathcal{Q}$ is our original 3D quadratic set in the 3D space $\mathbf{P}$. Pick a point $P \in \mathcal{Q}$. Because $\mathcal{Q}$ is nondegenerate, the tangent space $\mathcal{Q}_P$ is a 2D hyperplane (a flat plane). 

Now forget the rest of 3D space and look only inside the 2D flat plane $\mathcal{Q}_P$. Which points of $\mathcal{Q}$ lie inside this 2D plane $\mathcal{Q}_P$? The intersection $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$. 

This intersection is the quadratic set induced by $\mathcal{Q}$ in the tangent space $\mathcal{Q}_P$. Viewed as a set of points inside the 2D plane $\mathcal{Q}_P$, it satisfies the quadratic set axioms inside $\mathcal{Q}_P$. 

Why does this intersection have a radical equal to $\{P\}$? When we intersect the tangent plane $\mathcal{Q}_P$ with a smooth 3D surface $\mathcal{Q}$, let's say a hyperbolic quadric (think of an hourglass) $\mathcal{Q}$ with its tangent plane $\mathcal{Q}_P$ at $P$, what is the 2D cross-section $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$?

It is an X-shaped cross of two intersecting lines $g \cup h$ meeting at $P$. Inside the 2D plane $\mathcal{Q}_P$, an X-shaped pair of intersecting lines $g \cup h$ is a degenerate 1D cone whose vertex is the crossing point $P$. Inside the plane $\mathcal{Q}_P$, every line passing through $P$ is either $g$ (all points in $\overline{\mathcal{Q}}$), $h$ (all points in $\overline{\mathcal{Q}}$), or touches $g \cup h$ only at the crossing point $P$ ($1$ point in $\overline{\mathcal{Q}}$).

Therefore, for the 2D slice $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$ living inside the plane $\mathcal{Q}_P$, the point $P$ is a singular vertex and $\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$.

On a Sphere / Elliptic Quadric $\mathcal{Q}$, when you slice a sphere $\mathcal{Q}$ with its tangent plane $\mathcal{Q}_P$ at $P$, what is the 2D cross-section $\overline{\mathcal{Q}} = \mathcal{Q} \cap \mathcal{Q}_P$? It is just the single point $\{P\}$.

Inside the plane $\mathcal{Q}_P$, every line through $P$ meets $\{P\}$ in $1$ point, so $P$ is a singular point of that cross-section: $\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$

Now why did we say "In Other Words..." in the second paragraph of the theorem, linking $\mathcal{Q}_P \neq \mathcal{Q}_R$ to $\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$?

What does it mean for a point $R \in \mathcal{Q} \cap \mathcal{Q}_P$ to be in the radical of the slice $\mathcal{Q} \cap \mathcal{Q}_P$? It means that every line through $R$ inside the plane $\mathcal{Q}_P$ is tangent to $\mathcal{Q}$. In other words, the plane $\mathcal{Q}_P$ is made entirely of tangent lines to $\mathcal{Q}$ at $R$—which means $\mathcal{Q}_P$ is also the tangent plane to $\mathcal{Q}$ at $R$ ($\mathcal{Q}_R = \mathcal{Q}_P$)!

Now apply the first sentence: The first sentence says that if $\mathcal{Q}$ is nondegenerate, no two distinct points $P \neq R$ can ever share the same tangent plane ($\mathcal{Q}_P \neq \mathcal{Q}_R$). Since no other point $R \neq P$ can have $\mathcal{Q}_P$ as its tangent plane, no other point $R \neq P$ can be in the radical of the slice $\mathcal{Q} \cap \mathcal{Q}_P$. Therefore, $P$ is the only singular point of the tangent-plane cross-section:

$$\mathcal{Q}_P \neq \mathcal{Q}_R \text{ for all } R \neq P \quad \Longleftrightarrow \quad \text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$$

**In Short:** $\text{Rad}(\mathcal{Q}) = \emptyset$: The full 3D surface $\mathcal{Q}$ inside 3D space $\mathbf{P}$ is smooth (nondegenerate).

$\text{Rad}(\mathcal{Q} \cap \mathcal{Q}_P) = \{P\}$: When you slice that smooth 3D surface $\mathcal{Q}$ with its tangent plane $\mathcal{Q}_P$ at $P$, the cross-section $\mathcal{Q} \cap \mathcal{Q}_P$ has a pinch/vertex right at the point of tangency $P$ (an X-cross $g \cup h$ for a hyperboloid, or a single point $\{P\}$ for a sphere).

Now let $\mathcal{Q}$ be a nondegenerate quadratic set of $\mathbf{P}$.

> If $P \in \mathcal{Q}$ and $W$ is a complement of $P$ in $\mathcal{Q}_P$, then $\mathcal{Q}' := \mathcal{Q} \cap W$ is a nondegenerate quadratic set of $W$.
    
> If $H$ is a hyperplane that is not a tangent hyperplane, then $\mathcal{Q}' := \mathcal{Q} \cap H$ is a nondegenerate quadratic set of $H$.

### Index of Quadratic Sets

A quadratic set $\mathcal{Q}$ can be described very well by the dimension of its maximal $\mathcal{Q}$-subspaces (which are flat linear subspaces - a point, a line, a plane etc. that sit completely inside the curved surface $\mathcal{Q}$). The prefix $\mathcal{Q}$ simply means "contained in $\mathcal{Q}$"). This maximum dimension is connected to the index of $\mathcal{Q}$, which turns out to be the crucial parameter to describe $\mathcal{Q}$.

Let $t - 1$ be the maximum dimension of a $\mathcal{Q}$-subspace of a quadratic set $\mathcal{Q}$. Then the integer $t$ is called the index of $\mathcal{Q}$. The $\mathcal{Q}$-subspaces of dimension $t - 1$ are also called maximal $\mathcal{Q}$-subspaces.

In the literature, $\mathcal{Q}$-subspaces are also called generators or totally isotropic / totally singular subspaces of the quadric.

**Examples.** A cone and a hyperboloid in $3$-dimensional real space have index $2$, since they contain lines, but no planes. Any nonempty quadratic set that does not contain a line has index $1$; for instance, a sphere has index $1$.

If $\mathcal{Q}$ is a nondegenerate quadratic set of index $t$ in a $d$-dimensional projective space $\mathbf{P}$, then if $d$ is even, then $t \le \frac{d}{2}$. If $d$ is odd, then $t \le \frac{d + 1}{2}$. The more general formula which includes degenerate spaces is $t \le \frac{d + r + 1}{2}$ where $r$ is the size of the radical.

Why do we care about the index? In linear algebra and differential geometry, this number $t$ is called the Witt Index (or isotropic index) of a quadratic form. The point of the index is classification. Suppose you are in a $d$-dimensional projective space $\mathbf{P}$ over a finite field $\mathbb{F}_q$ (or the real numbers $\mathbb{R}$), and you want a complete list of every possible nondegenerate quadratic set $\mathcal{Q}$ that can exist in $\mathbf{P}$. The index $t$ is the single invariant that tells them apart. 

To see why, look at why $t$ is defined as $(\text{projective dimension}) + 1$. A projective subspace of projective dimension $t - 1$ corresponds to a vector subspace of vector dimension $t$ in the underlying vector space $V = F^{d+1}$. Therefore, the index $t$ counts the maximum number of mutually independent points $\{P_1, \dots, P_t\}$ you can pick inside $\mathcal{Q}$ such that the entire flat subspace they span lies completely inside $\mathcal{Q}$.

Look at how the index $t$ completely classifies all nondegenerate quadrics in $PG(3, q)$ ($d = 3$, where the theorem says $t \le \frac{3+1}{2} = 2$):

| Index $t$ | Max Dimension of a $\mathcal{Q}$-Subspace ($t - 1$) | What the Maximal $\mathcal{Q}$-Subspaces Are | Name of Quadric in $PG(3, q)$ | Canonical Equation |
| --- | --- | --- | --- | --- |
| $t = 1$ | $t - 1 = \mathbf{0}$ | Points (contains no straight lines at all) | Elliptic Quadric $Q^-(3, q)$ (or Ovoid / Sphere) | $x_0^2 + d x_1^2 + x_2 x_3 = 0$ *(where $x_0^2 + dx_1^2$ is irreducible)* |
| $t = 2$ | $t - 1 = \mathbf{1}$ | Lines (contains lines, but no 2D planes) | Hyperbolic Quadric $Q^+(3, q)$ (Regulus / Hourglass) | $x_0 x_3 - x_1 x_2 = 0$ |

And in even dimension $d = 2m$ (e.g., $d = 4$, where $t \le \frac{4}{2} = 2$), there is only one main type of nondegenerate quadric—the Parabolic Quadric $Q(4, q)$ ($x_0^2 + x_1 x_4 - x_2 x_3 = 0$), which has index $t = 2$ (ruled by lines). In fact, over finite fields, we will see that once we are given the dimension of a projective space, we can determine which of the 3 types of non-degenerate quadrics (parabolic, hyperbolic, elliptic) are possible, and which one a specific quadric is, based on its index.

The following lemma shows that the maximal $\mathcal{Q}$-subspaces are 'uniformly distributed'.

Before that, let's understand what uniformly distributed means. Imagine a bizarre surface where one half of the surface was bumpy like a sphere (containing only $0$D points, no lines), and the other half had a flat 2D disc glued onto it, or a single isolated straight line stuck to one side.  The lemma proves that a quadratic set can NEVER look like that. Now for the lemma:

Let $\mathcal{Q}$ be a quadratic set of index $t$ in $\mathbf{P}$.  Then each point of $\mathcal{Q}$ is on a maximal $\mathcal{Q}$-subspace.

More precisely: if $P$ is a point of $\mathcal{Q}$ outside a $(t - 1)$-dimensional $\mathcal{Q}$-subspace $U$, then there is a $(t - 1)$-dimensional $\mathcal{Q}$-subspace $U'$ through $P$ that intersects $U$ in a $(t - 2)$-dimensional subspace.

We formulate the assertion above once more in the case $t = 2$: through each point of $\mathcal{Q}$ outside a $\mathcal{Q}$-line $g$ there is a $\mathcal{Q}$-line that intersects $g$. We have seen this in the regulus.

Now let's relook at what "uniformly distributed" means. It means there are no isolated lower-dimensional patches. If $\mathcal{Q}$ contains even a single  $(t-1)$-dimensional flat subspace $U$ somewhere on it, then every single point $P \in \mathcal{Q}$—no matter where you look on $\mathcal{Q}$—must have at least one $(t-1)$-dimensional flat subspace $U'$ passing right through it. For eg. for a hyperbolic in 3D, this is equivalent to saying, if there is even one $\mathcal{Q}$-line, then every point of the quadric must fall on a $\mathcal{Q}$-line.
    
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

Why must this be true? Let's contrast a cone (degenerate) vs. a hyperboloid (nondegenerate). On a cone, the maximal $\mathcal{Q}$-subspaces are the straight lines ruling the cone.  No two lines on a cone are skew. Every single line passes through the vertex $V$. It is impossible to find a maximal $\mathcal{Q}$-line that is skew to $U$.
    
But in a non-degenerate sphere or hyperboloid, because $\mathcal{Q}$ is nondegenerate, there is no universal vertex $V$ where all maximal $\mathcal{Q}$-subspaces are pinned together. To see why this is so, assume that there is such a vertex $V$. Now let's take some point $X$ in the quadratic set. By the uniform distribution lemma, this point must lie on some maximal subspace $U$. Since $U$ is a flat subspace and it contains both $V$ and $X$, the line $VX$ must lie in $U$ as well, making it a $\mathcal{Q}$-line. Since we chose $X$ arbitrarily, it means the line from $V$ to every point in $\mathcal{Q}$ is a $\mathcal{Q}$-line. Thus $V$ is a singular point and so the radical of the quadratic set is non-empty, which contradicts the fact that it is non-degenerate.

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
We first define a type of object found in 2D projective planes, and a few objects found in 3D projective spaces. Then for 2D and 3D spaces, we list out the possible quadratic sets.

A nonempty set $\mathcal{O}$ of points in a projective plane is called an oval if no three points of $\mathcal{O}$ are collinear and each point of $\mathcal{O}$ is on a unique tangent. Ovals are the only type of nonempty, nondegenerate quadratic sets in a projective plane.

An ovoid is a nonempty set $\mathcal{O}$ of points of a 3D projective space $\mathbf{P}$ where no three points of $\mathcal{O}$ are collinear and for each point $P \in \mathcal{O}$, the tangents through $P$ cover a hyperplane (that is,  $\mathcal{O}_P$ is a hyperplane).

Ovals and ovoids are the same kind of geometric structure, a non-degenerate quadratic set of index $t = 1$, meaning it contains zero lines. Since every point in an oval or an ovoid has a tangent plane that is a hyperplane, this also means that they have no singular points. Later, we will see that in a finite field, ovals and ovoids cannot exist in any projective space of $d \gt 3$.

---

**Aside:** Because no three points of an ovoid are collinear, an ovoid contains no lines at all, meaning its index is $t = 1$. In 3D space, ovoids are the synthetic generalization of spheres/elliptic quadrics. So every sphere and elliptic quadric is an ovoid, but there are ovoids that are not spheres or elliptic quadrics.

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

We can put this in algebraic terms as well. In algebra, a quadric $\mathcal{Q}$ is defined by one single quadratic equation  $f(x_0, x_1, x_2, x_3) = 0$. If that quadratic polynomial factors into two linear pieces:

$$f(x_0, x_1, x_2, x_3) = L_1(x_0, x_1, x_2, x_3) \cdot L_2(x_0, x_1, x_2, x_3) = 0$$

then $L_1(x) = 0$ is a hyperplane  $H_1$, and $L_2(x) = 0$ is a hyperplane  $H_2$, so their union is $H_1 \cup H_2$ (two planes in 3D space). You can never get the union of two 1D lines in 3D space from a single quadratic equation (in algebraic geometry, two skew lines in 3D space require intersecting multiple quadratic surfaces, not just one). The Tangent-Space Axiom is the synthetic rule that detects this.

Note that $L_1, L_2$ can only be hyperplanes. For example, they cannot be a line in 3D space. This comes down to one of the most fundamental rules of linear algebra:  each single linear equation removes only $1$ degree of freedom (reduces the dimension by $1$). If you wanted to arrive at a line, you need two constraint equations, not one.

### Quadratic Sets in Finite Projective Spaces

Compared to the previous section, this section is both a generalization to arbitrary dimension $d$  and a specialization to finite spaces $PG(d, q)$ (where every line has exactly $q + 1$ points).

Switching to finite projective spaces gives us a new tool we didn't have in general (infinite) 2D and 3D spaces: exact counting (pigeonhole and parity arguments). Because the number of points on every line is fixed at $q+1$, we can deduce the exact number of points in any quadratic set $\mathcal{Q}$, tighten the index bound $t$, and completely classify all nondegenerate quadratic sets in any dimension $d$.

Now let $\mathcal{Q}$ be a quadratic set in a $d$-dimensional finite projective space $\mathbf{P} = PG(d, q)$, where every line contains $q + 1$ points.

Pick any non-singular point $P \in \mathcal{Q} \setminus \text{Rad}(\mathcal{Q})$. Because $P$ is not in the radical, its tangent space $\mathcal{Q}_P$ is a hyperplane (dimension $d - 1$). Let $a = a_P$ denote the number of $\mathcal{Q}$-lines (lines completely contained in $\mathcal{Q}$) that pass through $P$.

$\mathcal{Q}_P$ contains $aq + 1$ points of $\mathcal{Q}$. $\vert{}\mathcal{Q}\vert{} = 1 + q^{d-1} + aq$. $a$ is independent of $P$.

The proof reveals some additional, useful numbers. Every line through $P$ that lies outside $\mathcal{Q}_P$ is a 2-point secant line—meaning each such line contains exactly $1$ additional point of $\mathcal{Q}$ besides $P$.

How many lines through $P$ lie outside the hyperplane $\mathcal{Q}_P$? Total lines through $P$ in $PG(d, q)$: $\frac{q^d - 1}{q - 1} = q^{d-1} + q^{d-2} + \dots + q + 1$. Lines through $P$ inside the hyperplane $\mathcal{Q}_P$: $\frac{q^{d-1} - 1}{q - 1} = q^{d-2} + \dots + q + 1$. Subtracting the two gives exactly $q^{d-1}$ secant lines through $P$ outside $\mathcal{Q}_P$.

Each of those $q^{d-1}$ secant lines contributes $1$ point of $\mathcal{Q}$ outside $\mathcal{Q}_P$. Add to this the total number of points in $\mathcal{Q}_P$ i.e. ($1 + aq$), to get the total number of points of the quadratic set. Note that we can be sure that no points of the quadric that are missed by the secants since any two points of a projective space have a line joining them. Thus, since we have accounted for all tangents through $P$ via the tangent plane, every other line connecting $P$ to a point on the quadric is a secant. Also note that as we already saw earlier, any line through $P$ therefore contains either $1$ point of the quadric (P itself), or $q + 1$ points of the quadric (for $\mathcal{Q}$-lines) in both of which cases the line is a tangent, or $2$ points of the quadric for secants.

Why is $a$ independent of $P$? Solving for $a_P$ gives $a_P = \frac{\vert{}\mathcal{Q}\vert{} - 1 - q^{d-1}}{q}$. Because $\vert{}\mathcal{Q}\vert{}$, $d$, and $q$ are global constants of $\mathcal{Q}$, every non-singular point $P \in \mathcal{Q} \setminus \text{Rad}(\mathcal{Q})$ has the same number $a$ of $\mathcal{Q}$-lines passing through it.

Some counts for standard objects:

| Quadratic Set $\mathcal{Q}$ | Ambient Dimension $d$ | Number of $\mathcal{Q}$-Lines Through $P$ ($a$) | Why $a$ Has This Value | Total Points $\vert{}\mathcal{Q}\vert{} = 1 + q^{d-1} + aq$ |
| --- | --- | --- | --- | --- |
| Oval (in a 2D plane) | $d = 2$ | $a = 0$ | No 3 points are collinear, so $\mathcal{Q}$ contains no lines. | $1 + q^{2-1} + 0 = \mathbf{q + 1}$ |
| Ovoid (in 3D space) | $d = 3$ | $a = 0$ | No 3 points are collinear, so $\mathcal{Q}$ contains no lines. | $1 + q^{3-1} + 0 = \mathbf{q^2 + 1}$ |
| Cone (over an oval in 3D) | $d = 3$ | $a = 1$ | Through any non-vertex point $P \neq V$, there is only $1$ line in $\mathcal{Q}$ (the line $PV$ to the vertex). | $1 + q^2 + 1\cdot q = \mathbf{q^2 + q + 1}$ |
| Hyperboloid (Regulus in 3D) | $d = 3$ | $a = 2$ | Doubly ruled: each point $P$ lies on $1$ line $g \in \mathcal{R}$ and $1$ line $h \in \mathcal{R}'$. | $1 + q^2 + 2q = \mathbf{(q + 1)^2}$ |

Now let $\mathcal{Q}$ be a nonempty, nondegenerate quadratic set of a finite projective space $\mathbf{P}$ of dimension $d$. Then there are only three possibilities for the index $t$ of $\mathcal{Q}$. If $d$ is odd, then $t = \frac{d - 1}{2}$ or $t = \frac{d + 1}{2}$. If $d$ is even, $t = \frac{d}{2}$.

This sets an exact value for the index for even dimensions and a very tight bound for odd dimensions. This also means there are no ovoids for $d \geq 4$ because an ovoid has an index of $1$, which is not possible once $d \geq 4$. We mentioned this earlier.

In general, the nomenclature is, if $d$ is even, then the quadratic set is called parabolic. If $d$ is odd, if $t = \frac{d - 1}{2}$, it is called an elliptic, and if $t = \frac{d + 1}{2}$ it is called a hyperbolic.

The parabolic quadratic sets of a projective plane are the ovals. In a 3D projective space, the elliptic quadratic sets are the ovoids and the hyperboloids are the hyperbolic quadratic sets. Additionally, any nonempty non-degenerate quadratic set of a finite projective space is either elliptic, parabolic, or hyperbolic. 

Now let $\mathcal{O}$ be an oval in a finite projective plane of order $q$. As we have seen, $\vert{}\mathcal{O}\vert{} = q + 1$ points. At each of the $q + 1$ points of $\mathcal{O}$, there is a unique tangent line, so there are $q + 1$ tangent lines in total in the plane.

If $q$ is odd, every oval is an algebraic conic ($x_0 x_2 - x_1^2 = 0$), and every external point lies on either $0$ or $2$ tangents. If $q$ is even, all $q + 1$ tangent lines meet at a single common point $N$ called the nucleus or knot of the oval. Adding $N$ to $\mathcal{O}$ gives a set of $q + 2$ points with no $3$ collinear, called a hyperoval.

Now let's look at how we get such tight bounds on the the index of a quadratic set. We will see that this comes about because the number of points in a quadratic set depends on the number of points of a quadratic set of a lower dimension and index. This way, we inductively calculate the number of points on a quadratic set building up from dimensions 2 and 3.  

Now let $\mathcal{Q}$ be a nondegenerate quadratic set of index $t$ in dimension $d$. Pick a point $P \in \mathcal{Q}$ and look at the induced quadratic set $\overline{\mathcal{Q}} = \mathcal{Q}_P \cap \mathcal{Q}$ inside the $(d-1)$-dimensional tangent hyperplane $\mathcal{Q}_P$.

Because $\mathcal{Q}$ is nondegenerate, $\overline{\mathcal{Q}} = \mathcal{Q}_P \cap \mathcal{Q}$ is a degenerate cone with vertex $\text{Rad}(\mathcal{Q}_P \cap \mathcal{Q}) = \{P\}$. Pick a $(d-2)$-dimensional subspace $U \subset \mathcal{Q}_P$ missing $P$. By the Radical/Cone Theorem, the base slice $\mathcal{Q}' := \mathcal{Q} \cap U$ is a nondegenerate quadratic set in dimension $d - 2$ with index $t - 1$ since every $(t-1)$-dimensional maximal $\mathcal{Q}$-subspace through $P$ meets $U$ in dimension $t - 2$. It's point count is $\vert{}\mathcal{Q}'\vert{} = a$ since every $\mathcal{Q}$-line through $P$ pierces $U$ in a unique point of $\mathcal{Q}'$.

---

**Aside:** To make it easy to visualize this whole thing, let us plug the exact numbers for a hyperbolic quadric in a 3D projective space. 

Our starting parameters are $d = 3$ and index: $t = 2$ (because the maximal flat subspaces on $\mathcal{Q}$ are lines, which have projective dimension $t - 1 = 1$). The tangent plane is the 2D tangent plane formed by the two $\mathcal{Q}$-lines touching the saddle surface at $P$.
    
Look at the intersection (also called a slice) $\overline{\mathcal{Q}} = \mathcal{Q}_P \cap \mathcal{Q}$ inside that 2D tangent plane. The tangent plane slices $\mathcal{Q}$ in the two intersecting $\mathcal{Q}$-lines at $P$ — line $g \in \mathcal{R}$ and line $h \in \mathcal{R}'$.
    
$$\overline{\mathcal{Q}} = \mathcal{Q}_P \cap \mathcal{Q} = g \cup h$$
    
Why did we call this "X" of two lines a degenerate cone with vertex $\text{Rad}(\overline{\mathcal{Q}}) = \{P\}$? Because inside a 2D plane, as we saw, the union of two hyperplanes (i.e. lines) is a quadratic set. Further, a line from every point in the 2D plane to $P$, besides $g$ and $h$, touches this quadratic set at just one point, $P$ itself. If it touched either $g$ or $h$ at a second point, it would have to overlap with $g$ and $h$ itself because there can only be one line connecting two points on a projective plane. Thus  $P$ is singular. $\overline{\mathcal{Q}}$ is therefore referred to as a cone with $P$ as the apex/vertex where both lines are pinned together ($\text{Rad}(\overline{\mathcal{Q}}) = \{P\}$).

Next, our text says: Pick a $(d-2)$-dimensional subspace $U \subset \mathcal{Q}_P$ missing $P$.

Since $d = 3$, we have $d - 2 = 3 - 2 = \mathbf{1}$. So $U$ is simply a straight 1D line drawn inside the 2D tangent plane $\mathcal{Q}_P$ such that $U$ does not pass through the crossing point $P$ ($P \notin U$).

Now read the final sentences: "By the Radical/Cone Theorem, the base slice $\mathcal{Q}' := \mathcal{Q} \cap U$ is a nondegenerate quadratic set in dimension $d-2$ with index $t-1$... Its point count is $\vert{}\mathcal{Q}'\vert{} = a$ since every $\mathcal{Q}$-line through $P$ pierces $U$ in a unique point of $\mathcal{Q}'$."

What happens on our 2D $\mathcal{Q}_P$ when the line $U$ cuts across the two lines $g$ and $h$ of the "X"? The base slice $\mathcal{Q}' = \mathcal{Q} \cap U$ is literally just two points $\{A, B\}$ sitting on the 1D line $U$, where it intersects $g$ and $h$.

$$\mathcal{Q}' = \mathcal{Q} \cap U = \{A, B\} \quad \implies \quad \vert{}\mathcal{Q}'\vert{} = a = 2$$

---

This whole process of stripping away hyperbolic coordinates step by step is called a Witt decomposition. Each time we perform this tangent-slice reduction to algebraically peel off one hyperbolic coordinate pair $x_i y_i$, the ambient dimension drops by $2$ and the index drops by $1$. Repeat this reduction $t - 1$ times until we strip away all the straight lines and reach a nondegenerate quadratic set of index $t_{\text{stop}} = 1$ (a line-free ovoid/oval). 

Because no line-free quadratic set ($t_{\text{stop}} = 1$) can exist in dimension $d_{\text{stop}} \ge 4$, the stopping dimension $d_{\text{stop}} = d - 2(t - 1)$ must be $1$, $2$, or $3$:

$$1 \le d - 2(t - 1) \le 3 \quad \Longleftrightarrow \quad \frac{d - 1}{2} \le t \le \frac{d + 1}{2}$$

This single inequality locks $t$ into only three possibilities across all dimensions $d$. In fact, we can make the bound tighter, at least for even dimensions.

In even dimension $d = 2m$, we have parabolic quadrics $\mathcal{Q}(2m, q)$), and reducing $d = 2m$ by $2$ (and $t$ by 1) repeatedly $m - 1$ times lands in $d_0 = 2$ (the projective plane $\text{PG}(2, q)$). Since every nonempty nondegenerate quadratic set in $\text{PG}(2, q)$ is an oval of index $t_0 = 1$, we can now inductively build back to our original $d$-dimensional space, which will add $m - 1$ to the index: $t = 1 + (m - 1) = m = \frac{d}{2}$. You can also arrive at this quite easily by checking $d_{\text{stop}}$ from above. Starting from an even dimension, we will naturally end up at $d_{\text{stop}} = 2$. From $d - 2(t - 1) = 2$, we get $t = \frac{d}{2}$.
            
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

Note that we already encountered the conics referred to here when slicing with a tangent hyperplane. What's new here is slicing with a non-tangent hyperplane $H^*$, which drops you by $1$ dimension (just like the slice by the tangent plane) but yields a nondegenerate quadratic set (unlike the tangent plane slice). Because $d$ and $d - 1$ have opposite parities, a non-tangent slice forces the quadric to switch between the even-dimensional family (parabolic) and the odd-dimensional families (hyperbolic / elliptic).

Now let $\mathcal{Q}$ be a hyperbolic quadratic set in $\mathbf{P} = \text{PG}(5, q)$. Then $a = (q + 1)^2$ and $\vert{}\mathcal{Q}\vert{} = q^4 + q^3 + 2q^2 + q + 1 = (q^2 + q + 1)(q^2 + 1)$. Note that as we saw previously while inductively building the point count formula, $a$ is equal to the number of points of a quadratic set of $d-2$ dimensions and index $t-1$. When $d=3$, $a$ becomes the number of points on a regulus in a 3D projective space, which we already know is $(q+1)^2$.

A hyperbolic quadratic set has an extremely remarkable property: one can divide its maximal $\mathcal{Q}$-subspaces into two equivalence classes. The equivalence relation is given by the property that the corresponding subspaces intersect in a subspace of a certain parity. In fact, if $\mathcal{Q}$ has index $t$ with $d = 2t - 1$ and maximal subspace of dimension $t-1$, any two maximal $\mathcal{Q}$-subspaces $U_1, U_2$ are equivalent if and only if $(t-1) - \dim(U_1 \cap U_2)$ is even. 

If $d \ge 5$, all the maximal $\mathcal{Q}$-subspaces are partitioned into two equivalence classes by this parity formula.

In a $3$-dimensional projective space, we already know that the maximal $\mathcal{Q}$-subspaces of a hyperboloid are the lines of a regulus and its opposite regulus. If we define that two $\mathcal{Q}$-lines are equivalent if they are equal or skew, we get two classes of $\mathcal{Q}$-lines. There are two equivalence classes since $(t-1) = 1$ and $\dim(U_1 \cap U_2) = -1$, so $(t-1) - \dim(U_1 \cap U_2) = 2$, which is even.

Similarly, let $\mathcal{Q}$ be a hyperbolic quadratic set of a $5$-dimensional projective space $\mathbf{P}$. We say that two $\mathcal{Q}$-planes $\pi_1$ and $\pi_2$ are equivalent ($\pi_1 \sim \pi_2$) if $\pi_1$ and $\pi_2$ are equal or intersect each other in a single point.

The relation $\sim$ is reflexive and symmetric. Surprisingly, it is also transitive, making it an equivalence relation. 

## Quadrics Redux

Let's get back to quadrics. What we'll be doing here parallels what we did earlier with projective geometry in general. We first gave the synthetic axioms of a projective space and then introduced vector spaces and proved that any $\mathbf{P}(V)$ satisfies those axioms, and also looked at the converse, which is that almost every synthetic projective space is actually a $\mathbf{P}(V)$ (holds for all $d > 2$ but not for non-Desarguesian planes).
    
We'll do something similar here. We already looked at quadratic sets and their synthetic axioms: "If-three-then-all" and "Tangent-space" axioms. Now, we look at an algebraic model, or quadrics, inside $\mathbf{P}(V)$ defined by a polynomial equation $q(v) = 0$, and prove that every algebraic quadric satisfies the two axioms of a quadratic set, and that the converse is almost true with specific exceptions (like Tits ovoids or hyperovals in even characteristic).

First we define a quadratic form, which is essentially a homogenous polynomial of degree 2. Note that this implies that $q(\alpha \cdot v) = \alpha^2 \cdot q(v)$ for all $v \in V$ and all $\alpha \in F$. Note that we cannot use an inhomogenous polynomial because then once again, as earlier, the solution to the polynomial will not be independent of the scaling factor which treats points along a ray but in different $z$ (or whatever) planes as an equivalence class in projective spaces.

The quadric $\mathcal{Q}$ in $\mathbf{P}(V)$ is simply the set of all projective points $\langle v \rangle$ where that polynomial equals zero:  $q(v) = 0$. So you can simply write out a quadratic form and find its zeroes to arrive at all the points of a quadric.

Examples include the polynomial $x_0^2 - x_1^2 - x_2^2$ which yields a quadric in the plane; $x_0^2 - x_1^2 - x_2^2 - x_3^2$ and $x_0^2 + x_1^2 - x_2^2 - x_3^2$ provide quadrics in $3$-dimensional space.

We also define the polar form of $q$ as the map $B : V \times V \to F$ defined by $B(v, w) := q(v + w) - q(v) - q(w)$. It is a symmetric bilinear form. 

Note that $q(v)$ only takes one vector as input, which tells us whether a single point $\langle v \rangle$ lies on the quadric ($q(v) = 0$). To study how a straight line connecting two points $\langle v \rangle$ and $\langle w \rangle$ intersects the quadric, we have to evaluate $q$ on a linear combination $v + \lambda w$. This is where $B(v,w)$ comes into play. Think of $B(x, v) = 0$ as the algebraic version of the dot product, which defines the tangent hyperplane at $v$ without needing limits or derivatives. Similarly, $B$ will also be useful in our algebraic definition of tangents.

The above relation of $B$ also has a parallel with the dot product. If we define the quadratic form $q(v)$ as the squared norm of a vector:

$$q(v) = \Vert{}v\Vert{}^2 = v \cdot v$$

Expand $q(v + w) = \Vert{}v + w\Vert{}^2$ using the standard dot product:

$$\Vert{}v + w\Vert{}^2 = (v + w) \cdot (v + w) = v \cdot v + 2(v \cdot w) + w \cdot w = \Vert{}v\Vert{}^2 + 2(v \cdot w) + \Vert{}w\Vert{}^2$$

Subtracting $\Vert{}v\Vert{}^2$ and $\Vert{}w\Vert{}^2$ from both sides gives the same formula as above:

$$\underbrace{\Vert{}v + w\Vert{}^2}_{q(v+w)} - \underbrace{\Vert{}v\Vert{}^2}_{q(v)} - \underbrace{\Vert{}w\Vert{}^2}_{q(w)} = \underbrace{2(v \cdot w)}_{B(v, w)}$$

We can write a quadratic form via matrices once we define a vector space basis, $B(v, w) = v^T M w$. $M$ is a symmetric matrix. Note that there can be various $M$ that give the same quadratic form, since the coefficients of the cross terms $b_ib_j$ in the quadratic form will depend on the sum of entries in $M$ that correspond to the terms $b_ib_j$ and $b_jb_i$. In order to be able to define this uniquely, we can use an upper triangular matrix. This is also useful in characteristic 2 fields, because you cannot divide an odd coefficient by $2$ to split $b_1 b_2$ symmetrically into $\frac{1}{2} b_1 b_2 + \frac{1}{2} b_2 b_1$. Using an upper-triangular sum $\sum_{i \le j} c_{ij} b_i b_j$ works in every field.

As an example, suppose we have the quadratic polynomial:

$$q(b_1, b_2, b_3) = 2b_1^2 + \mathbf{6b_1 b_2} - 4b_1 b_3 + 5b_2^2 + 3b_3^2$$

Both

$$A_{\text{sym}} = \begin{pmatrix} 2 & \mathbf{3} & -2 \\ \mathbf{3} & 5 & 0 \\ -2 & 0 & 3 \end{pmatrix}, \qquad A_{\text{other}} = \begin{pmatrix} 2 & \mathbf{5} & -4 \\ \mathbf{1} & 5 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

will give us the polynomial. However, there is a unique upper triangular matrix that does the job.

$$C_{\text{upper}} = \begin{pmatrix} 2 & \mathbf{6} & -4 \\ 0 & 5 & 0 \\ 0 & 0 & 3 \end{pmatrix}$$

The polar form is key to understanding how a quadric satisfies both axioms of a quadratic set. Understanding this fact will also give us insight into why the polar form is defined the way it is, so let's take the two axioms and see what is needed from a quadratic form to satisfy the two axioms.

Any point on the line $vw$ is given by $v + \lambda w$. Let's check if it lies on the quadric. By the definition of the bilinear form:

$$q(v + \lambda w) = q(v) + q(\lambda w) + B(v, \lambda w)$$

Since $q(\lambda w) = \lambda^2 q(w)$ and $B$ is bilinear (linear in each slot, $B(v, \lambda w) = \lambda B(v, w)$), we get the fundamental Line-Quadric Intersection Formula:

$$q(v + \lambda w) = q(v) + \lambda B(v, w) + \lambda^2 q(w)$$

The RHS is an ordinary quadratic equation $A \lambda^2 + C \lambda + D = 0$ in the scalar parameter $\lambda$, and $B(v, w)$ is the cross-term (the coefficient of $\lambda^1$) that controls how $\langle v \rangle$ and $\langle w \rangle$ interact.

This formula $q(v + \lambda w) = q(v) + \lambda B(v, w) + \lambda^2 q(w)$ proves both axioms of a quadratic set for any quadric.

Let's look at the "If-Three-Then-All" axiom. Let $g$ be the line through $\langle v \rangle$ and $\langle w \rangle$. Every point on $g$ (aside from $\langle w \rangle$) has the form $\langle v + \lambda w \rangle$. Suppose $g$ contains three distinct points of the quadric $\mathcal{Q}$. Without loss of generality, let two of those points on $\mathcal{Q}$ be the base points $\langle v \rangle$ and $\langle w \rangle$ themselves, so $q(v) = 0$ and $q(w) = 0$. Plugging $q(v) = 0$ and $q(w) = 0$ into our intersection formula leaves:

$$q(v + \lambda w) = \lambda B(v, w)$$

Now use the third point of $\mathcal{Q}$ on the line $g$, which corresponds to some non-zero scalar $\lambda_0 \neq 0$ with $q(v + \lambda_0 w) = 0$: 

$$\lambda_0 B(v, w) = 0 \quad \stackrel{\lambda_0 \neq 0}{\Longrightarrow} \quad B(v, w) = 0$$

Since $q(v) = 0$, $q(w) = 0$, and $B(v, w) = 0$, our formula gives $q(v + \lambda w) = 0$ for all $\lambda \in F$. Every point of the line $g$ lies in $\mathcal{Q}$.

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
    
But when $\text{char}(F) = 2$ (like $\mathbb{F}_2, \mathbb{F}_4, \mathbb{F}_8, \dots$, where $2 = 1 + 1 = 0$), we cannot recover $q(v)$ from $B(v, v)$ by dividing by $2$, because $2 = 0$. 

In fact, in char $=2, B(x, x) = 0$ for every point in the projective space, not just the points on the quadric. Why? Because it is a symmetric bilinear form, which means $B(x, y) = B(y, x)$. This implies that every cross term such as $x_1y_2$ or $x_1y_1$ has a corresponding term with the $x$ and $y$ flipped i.e. $y_1x_2$ and $y_1x_1$. Note that $x_1, x_2...$ and $y_1, y_2...$ are the homogenous coordinates of the points $x$ and $y$. 

When we look at $B(x, x)$, this means that crossterms across coordinates such as $x_1y_2$ will become $x_1x_2$ and will appear twice. A multiplication by $2$ in char $=2$ is $0$. What about the non-crossterms? They end up as squares. In a finite field of characteristic 2, every element has a unique square root, and the map $x \mapsto x^2$ is an additive homomorphism ($(a+b)^2 = a^2+b^2$ because $2ab=0$). This means we can rewrite the surviving squares as a single perfect square. $B(x, x) = 0$ therefore implies that the square root (which has coordinate degrees of $1$) is also zero, which represent a linear equation, not a quadric. 

Let's look at this for a general symmetric bilinear form: 

$$B(\mathbf{x},\mathbf{y})=c_{11}x_{1}y_{1}+c_{12}x_{1}y_{2}+c_{21}x_{2}y_{1}+c_{22}x_{2}y_{2}$$

For $B$ to be symmetric, we must have $c_{12} = c_{21}$. Let's call this coefficient $d$. So our form is:

$$B(\mathbf{x},\mathbf{y})=c_{11}x_{1}y_{1}+d(x_{1}y_{2}+x_{2}y_{1})+c_{22}x_{2}y_{2}$$

Note that there are no squares such as $x_1^2$ here because then the form wouldn't be linear under scalar transformation. 

Now, plug a vector into itself ($\mathbf{y} = \mathbf{x}$) :

$$B(\mathbf{x},\mathbf{x})=c_{11}x_{1}^{2}+d(x_{1}x_{2}+x_{2}x_{1})+c_{22}x_{2}^{2}$$

In characteristic 2, the crossterms vanish. We have just the square terms: $c_{11}x_1^2 + c_{22}x_2^2$.

But in characteristic 2, every element has a unique square root, and the map $x \mapsto x^2$ is an additive homomorphism ($(a+b)^2 = a^2+b^2$). This means we can rewrite the surviving squares as a single perfect square:    
    
$$B(\mathbf{x},\mathbf{x})=(\sqrt{c_{11}}x_{1}+\sqrt{c_{22}}x_{2})^{2}$$
    
If $B(\mathbf{x}, \mathbf{x}) = 0$, then its square root $\sqrt{c_{11}}x_{1}+\sqrt{c_{22}}x_{2}=0$ must also be zero. This is the equation of a flat linear hyperplane. 

So in $\text{char} \neq 2$, evaluating $B(\mathbf{x}, \mathbf{x}) = 0$ gives you a beautiful curved cone or circle. But in $\text{char} = 2$, evaluating $B(\mathbf{x}, \mathbf{x}) = 0$ either collapses into a flat linear subspace (if $c_{11}$ or $c_{22}$ is non-zero) or becomes identically $0$ everywhere (if $c_{11}=c_{22}=0$, making the form alternating). 

This is why we define the quadratic form seperately to actually pinpoint the points of the quadric, so the diagonal squared terms $c_i b_i^2$ are retained, and also why nondegeneracy requires checking both  $B(x, v) = 0$ for all $x$  and  $q(v) = 0$.

**An example of a cone and finding its radical**

Take the 3D cone in $PG(3, \mathbb{R})$ with coordinates $v = (x_0, x_1, x_2, x_3)$ and quadratic form:

$$q(v) = x_0^2 + x_1^2 - x_2^2 = 0 \quad (\text{notice } x_3 \text{ is missing!})$$

Its bilinear form is $B(x, v) = 2x_0 v_0 + 2x_1 v_1 - 2x_2 v_2$.
    
Now test the vertex point $V_{\text{tip}} = \langle (0, 0, 0, 1) \rangle$, where $v = (0, 0, 0, 1) \neq 0$:
    
Does $q(v) = 0$? Yes:  $0^2 + 0^2 - 0^2 = 0$. So $V_{\text{tip}} \in \mathcal{Q}$.
        
Does $B(x, v) = 0$ for all $x = (x_0, x_1, x_2, x_3)$? Yes:  $2x_0(0) + 2x_1(0) - 2x_2(0) = 0$ for every  $x \in \mathbb{R}^4$!
        
Because $v = (0, 0, 0, 1) \neq 0$ satisfies both $q(v) = 0$ and $B(x, v) = 0$ for all $x$, this quadratic form is degenerate, and $\langle (0, 0, 0, 1) \rangle$ is the singular vertex of the cone ($\text{Rad}(\mathcal{Q}) = \{\langle (0,0,0,1) \rangle\}$).

## Flags, Residues & Amalgamations
We'll take a brief detour that is not especially relevant right now, but could hold significance for the general mathematical and physics work we do. We'll first look at the process involved in this, and then look at the motivation.

A point, a line, a plane etc. are each elements of a different geometric type. We can even have blocks (in BIBDs) as a geometric type. Note that no two elements of the same geometric type can be incident with each other. A flag is an iterative sequence of elements of different geometric type, which are each incident on each other. Thus a point on a line on a plane is a flag (of rank 3). A point on a line is a flag (of rank 2). The rank is given by the number of elements of the flag. Since two distinct elements of the same type can never be incident with each other and every element in a flag must be incident with every other element in that flag, a flag can contain at most one element of each type. Therefore, the number of elements in the flag is always equal to the number of types in the flag.

A chamber is a maximal flag of a geometry, a flag whose type set equals the entire type set $I$ of the geometry ($\text{type}(F) = I$). Because a flag can contain at most one element of each type, a chamber contains exactly one element of every available type in $I$, all mutually incident with one another. Consequently, its corank is $0$ (there are no missing types left to add).

Note that a flag does not need to include elements that are of successive dimensions i.e. a point on a line or a line on a plane. A point on a plane or a point on a hyperplane are also valid flags. Only a chamber (a maximal flag of type $I$) is required to contain every type without skipping any.

A flag can be extended to a chamber by iteratively finding higher-dimensional elements containing lower-dimensional ones all the way to the maximal dimension, and also filling in any missing lower-dimensional elements and intermediate-dimensional elements. Because a starting flag $F$ can contain any subset of types in $I$, extending $F$ to a chamber means finding one element for every missing type in $I \setminus \text{type}(F)$ so that the entire collection is mutually incident.

#### Principle of Double Counting

We will also state a theorem here which can be shown easily using flags, but has far-reaching consequences in incidence geometry. This is the Principle of Double Counting. 

Consider a rank 2 pregeometry such as points and lines or points and blocks in a BIBD. Let $A$ be the set of points (type $0$) and $B$ be the set of lines or blocks (type $1$). For a single point $a \in A$, the number $[a]$ is the number of lines passing through $a$. For a single line $b \in B$, the number $[b]$ is the number of points lying on $b$. Then:

$$\sum_{a \in A} [a] = \sum_{b \in B} [b]$$

When we sum $[a]$ over every point $a \in A$, versus summing $[b]$ over every line $b \in B$, the LHS, $\sum_{a \in A} [a]$, goes point by point and counts how many incident point-line flags contain each point. Summing over all points counts the total number of incident point-line flags in the entire geometry. Similarly, the RHS goes line by line, and counts how many incident point-line flags contain each line. Summing over all lines counts the same total number of incident point-line flags in the entire geometry.

For a BIBD, this equation becomes the well-known BIBD identity $vr = bk$. However, let us look at when a BIBD gives us $r=k$ i.e. the number of blocks through a point ($r = [a]$) equals the number of points on a block ($k = [b]$). This happens if and only if the total number of points equals the total number of blocks i.e. $v = b$. This is known as a symmetric BIBD, and includes projective planes where $v = b = q^2 + q + 1$ and $r = k = q + 1$.

### Residues
A residue means fixing a chosen object (or flag of objects) and looking only at the local incidence structure of the remaining types that touch it. It is given by a two-step process:

- Remove the entire type (or types) belonging to the chosen element $x$ (or flag $F$). This is actually a redundant step. As we pointed above, no two distinct elements of the same type can ever be incident with each other. So if we just ask "which elements $y \neq x$ are incident with $x$?", every other element of the same type as $x$ is automatically filtered out anyway.
    
- From the remaining types, keep only the elements that were incident with $x$ in the original geometry, along with the original incidence relations among them. We can form a new incidence geometry based on the remaining types and how they are incident on each other.

Here's an example. Consider the 3D cube as a rank 3 incidence geometry $\Gamma$ with type set:

$$I = \{\text{vertices (0)}, \text{edges (1)}, \text{faces (2)}\}$$

The top face is formed by vertices numbered $1234$ and the bottom face directly underneath it is $8765$ (with $1$ above $8$,  $2$ above $7$,  $3$ above $6$, and $4$ above $5$, or more specifically from the edges given:  $1$ is connected to $2$,  $4$, and $5$, so $5$ is directly below $1$).

Now let us find the residue $\Gamma_1$ of the single-element flag $F = \{\text{vertex } 1\}$:

- Remove the type of the fixed element: Since vertex $1$ has type $0$ (vertices), we discard all vertices from our type set. The remaining types in the residue $\Gamma_1$ are:
    
    $$I_1 = I \setminus \{0\} = \{\text{edges (1)}, \text{faces (2)}\}$$
    
    Thus,  $\Gamma_1$ is a rank 2 geometry (it has only two types of objects, which we can think of as "new points" and "new lines").
    
- Collect all elements incident with vertex $1$. Which edges of the cube touch vertex $1$? Exactly the 3 edges $12$,  $14$, and $15$. Which faces of the cube touch vertex $1$? Exactly the 3 faces $1234$,  $1458$, and $1256$. (All other vertices, edges, and faces of the cube that do not touch vertex $1$ are ignored.)
        
- Check the incidence inside $\Gamma_1$ (Why it forms a triangle): Inside this rank 2 geometry $\Gamma_1$, let the 3 edges $\{12, 14, 15\}$ act as the "points" of the triangle, and let the 3 faces $\{1234, 1458, 1256\}$ act as the "lines" (sides) of the triangle:
    
    -   The face $1234$ contains the two edges $12$ and $14$.
        
    -   The face $1458$ contains the two edges $14$ and $15$.
        
    -   The face $1256$ contains the two edges $12$ and $15$.
   
   Geometrically, if we take a flat plane and slice off the corner of the 3D cube right near vertex $1$ (a vertex figure), the cross-section is a triangle: the 3 edges radiating from vertex $1$ pierce our slicing plane at 3 points (the corners of the triangle), and the 3 faces meeting at vertex $1$ slice our plane in 3 line segments connecting those 3 points.

### Amalgamations
Now we go the other way, and we'll do it with an example with the Fano plane. Briefly, take a Fano plane. Take all points and edges and create an incidence structure with them to get a 21-point structure called the Haewood graph. That structure can again be furthered built into a 63-point structure which is the split Cayley Hexagon.

In more detail, start with the Fano plane $\Gamma = PG(2, 2)$, which is a rank 2 geometry with:

* $7$ points (type $0$)
* $7$ lines (type $1$), each containing $3$ points
* $7 \times 3 = 21$ chambers (incident point-line flags $\{P, \ell\}$ where $P \in \ell$)
* $7 \times 4 = 28$ anti-flags (non-incident point-line pairs $\{P, \ell\}$ where $P \notin \ell$)

If we turn all $7$ points and $7$ lines into vertices of a bipartite graph ($7 + 7 = 14$ vertices total, and $7$ on each side), and connect a vertex that was a point $P$ to a vertex that was a line $\ell$ whenever $P \in \ell$ in the Fano plane, we get the Levi graph (or incidence graph) of the Fano plane. That graph is also called the Heawood graph:

* Its $14$ vertices are the $7$ points + $7$ lines of the Fano plane.
* Its $21$ edges are the $21$ incident flags $\{P, \ell\}$ of the Fano plane.

We can build this on to get larger graphs such as the Ljubljana graph. Alternatively, we can make a different amalagamation of the Fano plane to get another kind of geometry.

Consider the numbers we listed from the Fano plane:

$$7 \text{ (points)} + 7 \text{ (lines)} + 21 \text{ (flags)} + 28 \text{ (anti-flags)} = 63 \text{ elements}$$

Notice that $63 = 2^6 - 1$ is the exact number of points in the 5-dimensional projective space $PG(5, 2)$, and it is also the exact number of points (and lines) of the smallest Split Cayley Generalized Hexagon $H(2)$ (which lives inside $PG(5, 2)$ on the parabolic quadric $Q(6, 2)$ or symplectic space $W(5, 2)$).

This is Tits' famous combinatorial construction of the Split Cayley Hexagon $H(2)$ (associated with the exceptional group $G_2(2)$) directly from the Fano plane $PG(2, 2)$:

| Component from the Fano Plane $PG(2, 2)$ | Count | Role in the Split Cayley Hexagon $H(2)$ |
| --- | --- | --- |
| Points $P$ of $PG(2, 2)$ | $7$ | $7$ points of $H(2)$ |
| Lines $\ell$ of $PG(2, 2)$ | $7$ | $7$ points of $H(2)$ |
| Incident Flags $\{P, \ell\}$ ($P \in \ell$) | $21$ | $21$ points of $H(2)$ |
| Anti-Flags $\{P, \ell\}$ ($P \notin \ell$) | $28$ | $28$ points of $H(2)$ |
| Total Points of $H(2)$ | $63$ | All $63$ points of $H(2)$ |

In the Split Cayley Hexagon $H(2)$, every line contains $q + 1 = 3$ points, and there are $63$ lines in total, which also split into matching families of sizes $21$, $7$, $7$, and $28$:

- $21$ lines of type $[P, \ell, \{P, \ell\}]$: For each of the $21$ flags $\{P, \ell\}$ of the Fano plane (where $P \in \ell$), the 3 hexagon points $P$, $\ell$, and $\{P, \ell\}$ form a line of $H(2)$.

- $7$ lines from each Fano line $\ell = \{P_1, P_2, P_3\}$: For each of the $7$ lines $\ell$ of the Fano plane, the 3 flags $\{P_1, \ell\}, \{P_2, \ell\}, \{P_3, \ell\}$ form a line of $H(2)$.

- $7$ lines from each Fano point $P$ on $\ell_1, \ell_2, \ell_3$: Dually, for each of the $7$ points $P$ of the Fano plane, the 3 flags $\{P, \ell_1\}, \{P, \ell_2\}, \{P, \ell_3\}$ form a line of $H(2)$.

- $28$ lines mixing flags and anti-flags: The remaining $28$ lines of $H(2)$ each consist of 1 flag and 2 anti-flags (or triples tied to a triangle/anti-flag configuration in the Fano plane).

### Motivation

The motivation behind flags, residues, and amalgamation comes down to a single overarching goal instituted by Jacques Tits and Francis Buekenhout: turning abstract group theory (specifically the classification of finite simple groups and Lie groups) into concrete, visual geometry, and breaking high-dimensional geometries down into simple 2-dimensional building blocks.

Here is what each of these three tools does for us and what it points toward.

#### Flags and Chambers Connect Geometry to Group Theory

Why package a nested chain of subspaces $P \in \ell \subset \Pi$ into a single object called a flag or chamber? Because flags translate symmetry groups directly into geometry.

**Chambers as a Coordinate Frame (Regular Group Action):** In $PG(2, q)$, there are many automorphisms (collineations) that fix a single point $P$, and still many that fix both a point $P$ and a line $\ell$ through $P$. However, if we fix a chamber (a maximal flag) along with a standard frame of reference, we pin down the group elements completely. The automorphism group $G$ of a classic geometry acts transitively on the set of all chambers.
    
**Dictionary Between Subgroups and Flags (Parabolic Subgroups):** In group theory, it is often difficult to understand the internal subgroup structure of a large matrix group or simple group $G$. Once $G$ acts on a geometry $\Gamma$:
    
- The stabilizer in $G$ of a single element $x$ (a flag of rank $1$) is a maximal parabolic subgroup $P_x \subset G$.
        
- The stabilizer in $G$ of a chamber $C$ (a maximal flag of type $I$) is the Borel subgroup $B \subset G$ (for example, the group of upper-triangular matrices in $PGL(n+1, q)$).
        
- The residue $\Gamma_x$ of the element $x$ is the exact geometry on which the quotient of the parabolic subgroup $P_x$ acts. Thus, taking a flag $F$ and looking at its residue $\Gamma_F$ is the geometric equivalent of taking a subgroup $P_F \subset G$ and factoring out its unipotent radical to get a smaller Levi subgroup.
        
**Walking Between Chambers (Galleries and Coxeter Groups):** Two chambers are called $i$-adjacent if they differ only in their element of type $i$ (for example, two flags $\{P_1, \ell, \Pi\}$ and $\{P_2, \ell, \Pi\}$ sharing the same line and plane, but with different points). Moving step-by-step from one chamber to an adjacent chamber is governed by reflection groups (Weyl groups / Coxeter groups), turning pathfinding in geometry into word problems in algebra.

#### Residues Give Local-to-Global Classification and Induction

A high-dimensional geometry (say, rank $5$ or rank $8$) is too large to visualize all at once. Taking residues acts like a microscope or a Taylor series expansion in calculus: it lets us study a complex global space by looking at its small, local neighborhoods.

**Reduction to Rank 2 (Buekenhout-Tits Diagrams):** If we have a geometry of rank $n$, and we take the residue of a flag of rank $n - 2$ (corank $2$), we are left with a rank $2$ geometry (just "points" and "lines"). Rank $2$ geometries are easy to classify: they are usually projective planes, generalized quadrangles, generalized hexagons, or generalized digons.
    
**Fingerprinting the Whole Space from Local Pieces:** A foundational theorem by Tits proves that for a broad class of geometries (called buildings), if we know all the rank $2$ residues, the entire global geometry is uniquely determined (up to coverings). For example, consider a rank $3$ geometry over $I = \{0, 1, 2\}$ (points, lines, planes):
    
- Fix a plane (type $2$): its residue of points and lines is a projective plane.

- Fix a point (type $0$): its residue of lines and planes is also a projective plane.
        
- Fix a line (type $1$): its residue of points on the line and planes through the line is a generalized digon (every point on the line lies in every plane through the line). Any simply connected rank $3$ geometry whose local rank $2$ residues obey those three rules is forced to be the 3D projective space $PG(3, \mathbb{F})$.
        
**Inductive Counting and Proofs:** Just as we saw with the Witt decomposition on a quadric, taking the residue of a point on a polar space reduces its rank by $1$. This lets us prove theorems and count points or generators by induction on the rank.
    
#### Amalgamation Constructions Help Build Exotic Geometries and Exceptional Groups

**Constructing Exceptional Objects That Have No Simple Matrix Equation:** Classical geometries ($A_n, B_n, C_n, D_n$) come easily from standard vector spaces and quadratic or symplectic forms. However, nature also contains exceptional Lie groups ($G_2, F_4, E_6, E_7, E_8$) and sporadic simple groups (like the Mathieu groups or the Monster group). You cannot just write down a simple $3 \times 3$ quadratic equation to get an $E_8$ geometry or a sporadic geometry. Instead, we construct them from the bottom up by gluing together (amalgamating) smaller pieces—combining points, lines, flags, and anti-flags of simpler spaces like the Fano plane or quadrics.
    
**Revealing Hidden Symmetries (Triality and Automorphism Lifts):** In the Fano plane $PG(2, 2)$, points and lines are separate types ($7$ points and $7$ lines), and the automorphism group $PSL(3, 2)$ has order $168$ (or $336$ if we include point-line duality). When we bundle the $7$ points,  $7$ lines,  $21$ flags, and $28$ anti-flags together into the $63$ points of the Split Cayley Hexagon $H(2)$, something remarkable happens: in $H(2)$, all $63$ points look completely identical. An element that used to be a "flag" $\{P, \ell\}$ and an element that used to be a "point" $P$ or an "anti-flag" can now be mapped to one another by symmetries of the hexagon. By amalgamating these different pieces into one unified point set, the symmetry group jumps from order $336$ all the way up to the exceptional group $G_2(2)$ of order $12,096$.
    
**Shadow Spaces (Turning Flags into Points):** Similarly, if we take the lines of $PG(3, q)$ (which are rank $1$ flags of type $\{1\}$) and promote them to be the "points" of a new space, they form the Klein quadric $Q^+(5, q)$ in $PG(5, q)$. Doing this allows us to study complicated families of lines or flags in a low-dimensional space as ordinary points on a smooth quadric in a higher-dimensional space.

What is a shadow space? A shadow space is not an amalgamation of different objects like the Fano-to-hexagon construction. Instead, we stay inside the exact same geometry, pick one specific type of element (like lines) to act as our new "points", and define our new "lines" using the incident flags of the original geometry.

Why is it called a shadow? Imagine shining a flashlight from an element $x$ onto the set of all original points (type 0). The set of all points incident with $x$ is called the $0$-shadow of $x$. More generally, if we pick any fixed type $j \in I$, the $j$-shadow of a flag $F$ is the set of all elements of type $j$ that are incident with $F$.

To build the $j$-shadow space of a geometry $\Gamma$:

- New Points: We declare all elements of type $j$ in $\Gamma$ to be the new points of our shadow space.

- New Lines: We take flags of the remaining types $I \setminus \{j\}$ (specifically, chambers of the reduced type set $I \setminus \{j\}$) and look at their $j$-shadows. Each such shadow is a collection of elements of type $j$, which becomes a single new line in our shadow space.

Let us trace how this works when we start with ordinary 3D projective space $\Gamma = PG(3, q)$, where the types are points (0), lines (1), and planes (2):

- Choose type $1$ (the lines of $PG(3, q)$) to be our new points:
Every line $\ell$ in 3D space is now treated as a single 0-dimensional point in a new space. (In $PG(3, q)$, there are $(q^2+1)(q^2+q+1)$ lines in total.)

- What becomes a new line in this shadow space?
Remove type $1$ from the type set $I = \{0, 1, 2\}$. The remaining types are $\{0, 2\}$, which corresponds to an incident point-plane flag $\{P, \Pi\}$ in $PG(3, q)$ where the point $P$ lies on the plane $\Pi$.

Now ask: what is the $1$-shadow of the flag $\{P, \Pi\}$? It is the set of all lines $\ell$ in $PG(3, q)$ that are incident with both $P$ and $\Pi$—that is, the flat pencil of $q + 1$ lines that pass through the point $P$ and lie flat inside the plane $\Pi$.

Why does this land in a higher-dimensional space ($PG(5, q)$)? In $PG(3, q)$, a point has 4 homogeneous coordinates $(x_0, x_1, x_2, x_3)$. To specify a line $\ell$ joining two points $x$ and $y$, we take the $2 \times 2$ determinants $p_{ij} = x_i y_j - x_j y_i$ for $0 \le i < j \le 3$ (called Plücker coordinates).

Because there are $\binom{4}{2} = 6$ ways to choose pairs $(i, j)$ from 4 coordinates, every line in $PG(3, q)$ gets 6 homogeneous coordinates $(p_{01}, p_{02}, p_{03}, p_{12}, p_{13}, p_{23})$, which defines a point in 5D projective space $PG(5, q)$.
Furthermore, those 6 determinants always satisfy the single quadratic equation:

$$p_{01}p_{23} - p_{02}p_{13} + p_{03}p_{12} = 0$$

That equation is a non-degenerate hyperbolic quadric $Q^+(5, q)$ in $PG(5, q)$ (the Klein quadric), and every pencil of lines $\{P, \Pi\}$ from $PG(3, q)$ maps to a straight $\mathcal{Q}$-line on $Q^+(5, q)$.

Here's a summary of the difference between amalgamations vs. shadow spaces

| Feature | Amalgamation (e.g., Fano Plane to Hexagon $H(2)$) | Shadow Space / Grassmannian (e.g., Lines of $PG(3, q)$ to Klein Quadric) |
| --- | --- | --- |
| What becomes a new point? | A mixture of different objects glued together (7 points + 7 lines + 21 flags + 28 anti-flags = 63 points). | Only one single type of element from the original geometry (e.g., only the lines of $PG(3, q)$). |
| What becomes a new line? | Combinatorial triples linking flags, points, lines, and anti-flags across orbits. | The shadow of a flag of the remaining types (e.g., the pencil of lines incident with a point-plane flag $\{P, \Pi\}$). |
| Why do we do it? | To construct a brand-new geometry with a larger symmetry group out of smaller pieces. | To turn a rank $n$ incidence geometry into a concrete point-line linear space (rank 2) that can often be embedded as an algebraic variety in a higher projective space. |

### Diagrams

A Buekenhout-Tits diagram is a visual blueprint of a geometry. Instead of trying to draw all the points, lines, and planes at once, the diagram summarizes how any two types of objects interact locally when we freeze all the other types. 

A diagram is a graph where each node (circle) represents one type in the type set $I$. If a geometry has rank $3$ over $I = \{0, 1, 2\}$ (such as points, lines, and planes), its diagram has $3$ nodes. Each edge connecting two nodes $i$ and $j$ tells us how elements of type $i$ and elements of type $j$ interact with each other as a rank 2 point-line geometry. To achieve this, we find the residue of a flag containing every type except $i$ and $j$. Since taking the residue of $F$ erases all the types inside $F$, we are left with the types that are not in $F$ i.e. $i, j$. 

This helps us decompose complex geometries into rank 2 point-line geometries and understand how they fit together to form the more complex geometry. 

One natural question arises: if there are many different flags $F$ of type $I \setminus \{i, j\}$ in our geometry, what if one flag gives a projective plane on $\{i, j\}$ while another flag of the exact same type gives a square?

In the definition of a Buekenhout-Tits diagram, the label on the edge between node $i$ and node $j$ represents the class of rank $2$ geometries (such as the class of all projective planes, or all generalized quadrangles) to which the residue $\Gamma_F$ belongs for every flag $F$ of cotype $\{i, j\}$. In highly symmetric geometries (like buildings, polar spaces, projective spaces, and regular polytopes), the automorphism group acts transitively on chambers, which guarantees that any two flags of the exact same type have isomorphic residues.

As an aside, we will also define an incidence graph. Let $\Gamma$ be a geometry of rank $d$. The incidence graph  $I(\Gamma)$ of $\Gamma$ is defined as follows: The vertices of $I(\Gamma)$ are the elements of $\Gamma$. Two distinct vertices $x$ and $y$ of $I(\Gamma)$ are joined by an edge if and only if $x$ and $y$ are incident.

A geometry $\Gamma$ is called connected if the incidence graph $I(\Gamma)$ of $\Gamma$ is connected, i.e., for any two vertices $x$ and $y$, there exists a path from $x$ to $y$.

$\Gamma$ is called residually connected if all rank-$m$ residues ($2 \le m \le d$) of $\Gamma$ are connected. Noth affine and projective spaces are residually connected.

#### The Digon

Next, we'll define something called a digon. A generalized digon is a rank $2$ geometry over two types (say, type $0$ "points" and type $1$ "lines") in which every element of type $0$ is incident with every element of type $1$.

Think of the sequence of ordinary polygons as thin rank $2$ geometries: a 4-gon (square) has $4$ vertices and $4$ edges. A 3-gon (triangle) has $3$ vertices and $3$ edges. A 2-gon (digon) has $2$ vertices (say,  $A$ and $B$) and $2$ edges (say,  $e_1$ and $e_2$) that both connect $A$ to $B$.

When we generalize this to allow more than $2$ elements of each type (say,  $m$ elements of type $0$ and $n$ elements of type $1$, where every element of type $0$ is still incident with every element of type $1$), we call it a generalized digon.

#### Notation
To save clutter, diagrams use a shorthand for the edges between two nodes $i$ and $j$:

No Edge at all (Blank Space) = Generalized Digon: Every element of type $i$ is incident with every element of type $j$. Because this is a trivial complete bipartite relation where everything touches everything, we draw no line at all between node $i$ and node $j$.

A Single Unlabeled Stroke ( `o-----o` ) = Projective Plane (or Generalized Triangle): The residue on types $i$ and $j$ is a projective plane (like the Fano plane, or a triangle in thin geometries). Because projective planes are the most common building blocks, a single line without a label always means a projective plane.

A Double Stroke ( `o=====o` ) or an Edge Labeled $4$ = Generalized Quadrangle: The residue on types $i$ and $j$ is a generalized quadrangle (such as a square, or the points and lines on a 3D hyperboloid or 4D quadric).

 An Edge with a Label ($L$, $c$, $6$, etc.): If the rank $2$ residue is something else, we write a label directly over the edge—for instance, $L$ for a general linear space, $A$ for an affine plane, $c$ for a circle geometry (blocks of size $2$, like the edges and vertices of a polygon), or $6$ for a generalized hexagon.

Sometimes numbers are also written underneath the nodes. Usually, the type name $0, 1, 2$ is written above the node, and $s_i$—meaning each panel of cotype $i$ is contained in $s_i + 1$ chambers—is written below the node.

---

**Aside:** Why does a generalized diagon get no stroke? Whenever a rank $2$ residue is a generalized digon, the two types $i$ and $j$ do not place any restriction on each other at all—picking an element of type $i$ in that residue gives zero information about which element of type $j$ can be paired with it, because every choice works.

This happens any time we fix an intermediate dimension in a nested chain. If we fix an edge in a polyhedron, every vertex on that edge automatically lies in every face containing that edge. Or if we fix a line $\ell$ in $PG(3, q)$, every point $P \in \ell$ automatically lies in every plane $\Pi \supset \ell$ (giving a generalized digon with $q+1$ points and $q+1$ planes, where all $(q+1) \times (q+1)$ pairs are incident).
    
Because the incidence between the two remaining types is automatic and universal (a cartesian product of choices), Buekenhout-Tits diagrams leave the space between those two nodes blank.

---

#### How to Build a Diagram: The 3D Cube

Let us build the diagram for our 3D cube geometry over $I = \{0 \text{ (vertices)}, 1 \text{ (edges)}, 2 \text{ (faces)}\}$.

Draw 3 nodes for the 3 types: Node $0$ (vertices), Node $1$ (edges), and Node $2$ (faces).

Find the connection between Node $0$ (vertices) and Node $1$ (edges): Fix the remaining type: pick a single Face (type $2$). Inside that fixed square face, what geometry do its $4$ vertices (type $0$) and $4$ edges (type $1$) form? They form a square (a $4$-gon / generalized quadrangle). So between Node $0$ and Node $1$, we draw a double stroke (or an edge labeled $4$).

Find the connection between Node $1$ (edges) and Node $2$ (faces): Fix the remaining type: pick a single Vertex (type $0$). As we saw earlier when we took the residue $\Gamma_1$ of vertex $1$, the $3$ edges and $3$ faces meeting at a vertex form a triangle (a thin projective plane). So between Node $1$ and Node $2$, we draw a single unlabeled stroke.

Find the connection between Node $0$ (vertices) and Node $2$ (faces): Fix the remaining type: pick a single Edge (type $1$). What are the vertices on that edge, and what are the faces through that edge? There are $2$ vertices at the ends of the edge and $2$ faces meeting along that edge. Every vertex on that edge automatically lies in every face containing that edge. That is a generalized digon. So between Node $0$ and Node $2$, we draw no edge at all.

Putting these together gives the diagram of the cube (called the $B_3$ / $C_3$ diagram):

```
   0 (Vertices)          1 (Edges)          2 (Faces)
       o =================== o ----------------- o
          (Square / 4-gon)      (Triangle / PP)

```

Notice why Node $0$ and Node $2$ are placed on opposite ends with Node $1$ in the middle: because Node $0$ and Node $2$ have no edge between them, placing Node $1$ in the middle makes the diagram a clean straight line.

#### How to Build a Diagram: 3D Projective Space $PG(3, q)$

Now let us do the exact same 4 steps for $PG(3, q)$, where $I = \{0 \text{ (points)}, 1 \text{ (lines)}, 2 \text{ (planes)}\}$:

- Between $0$ (points) and $1$ (lines) — Fix a Plane (type $2$): The points and lines lying inside a fixed plane form a projective plane $PG(2, q)$. So we draw a single stroke between $0$ and $1$.

- Between $1$ (lines) and $2$ (planes) — Fix a Point (type $0$): The lines and planes passing through a fixed point in 3D space also form a projective plane $PG(2, q)$. So we draw a single stroke between $1$ and $2$.

- Between $0$ (points) and $2$ (planes) — Fix a Line (type $1$): Every point on the fixed line automatically lies inside every plane passing through that line. That is a generalized digon, so we draw no edge between $0$ and $2$.

This gives the $A_3$ diagram for $PG(3, q)$:

```
   0 (Points)            1 (Lines)          2 (Planes)
       o ----------------- o ----------------- o
         (Projective Plane)  (Projective Plane)

```

---

#### Reading Diagrams by Deleting Nodes

Once we have a diagram for a high-rank geometry, we can read off the diagram of any residue immediately without doing any new geometric work. To find the diagram of the residue of a flag $F$, simply erase the nodes in $\text{type}(F)$ and all edges attached to those erased nodes.

Let us test this on the cube diagram `o === o --- o` (Nodes $0, 1, 2$):

- Residue of a Vertex (erase Node $0$): We are left with `o --- o` on Nodes $1$ and $2$ (a triangle / projective plane).

- Residue of a Face (erase Node $2$): We are left with `o === o` on Nodes $0$ and $1$ (a square / quadrangle).

- Residue of an Edge (erase Node $1$ in the middle): We are left with `o     o` on Nodes $0$ and $2$ with no edge between them (a generalized digon).

Let's do another example, the 4-dimensional projective space $PG(4, q)$, which has rank $4$ over the type set: $I = \{0 \text{ (points)}, 1 \text{ (lines)}, 2 \text{ (planes)}, 3 \text{ (3-spaces / solids)}\}$

Its diagram is a 4-node chain ($A_4$):

```
   0 (Points)       1 (Lines)       2 (Planes)       3 (Solids)
       o -------------- o -------------- o -------------- o

```

Let us see how we read the different parts of this 4-node diagram by deleting nodes.

Deleting 1 Node (Fixing a Flag of Rank 1 -> Leaves a Rank 3 Sub-Diagram): Suppose we fix just one single element, say a Solid $S$ (type $3$). Erasing node $3$ leaves the 3-node sub-diagram on $\{0, 1, 2\}$:
    
    ```
    0 (Points)       1 (Lines)       2 (Planes)
        o -------------- o -------------- o
    
    ```
    
This tells us that all the points, lines, and planes inside a single solid $S$ form a 3D projective space $PG(3, q)$.
    
Deleting 2 Nodes (Fixing a Flag of Rank 2 -> Leaves a Single Rank 2 Edge): Now suppose we want to read the single edge between $0$ (points) and $1$ (lines). To isolate nodes $0$ and $1$, we must erase both node $2$ (planes) and node $3$ (solids). 

Geometrically, that means we fix a rank $2$ flag $F = \{\Pi, S\}$ consisting of a plane $\Pi$ lying inside a solid $S$ ($\Pi \subset S$). The residue of $F = \{\Pi, S\}$ consists of all points $P$ and lines $\ell$ that are incident with both $\Pi$ and $S$. Since $\Pi$ is already inside $S$, any point or line inside $\Pi$ is automatically inside $S$. Thus, the points and lines inside $\Pi$ form the projective plane $PG(2, q)$, which gives the single stroke `o --- o` between node $0$ and node $1$.
    
What if we delete the middle two nodes ($1$ and $2$)? Fix a flag $F = \{\ell, \Pi\}$ consisting of a line $\ell$ inside a plane $\Pi$. Erasing nodes $1$ and $2$ leaves nodes $0$ (points) and $3$ (solids) with no edge between them. Why is it a generalized digon? Because the remaining elements are the points $P$ on the line $\ell$ and the solids $S$ containing the plane $\Pi$. Since $P \in \ell \subset \Pi \subset S$, every point on $\ell$ is automatically incident with every solid containing $\Pi$.

#### Common Diagrams at a Glance

| Geometry | Type Set $I$ | Diagram | Why It Looks Like That |
| --- | --- | --- | --- |
| Projective Plane $PG(2, q)$ | $0$ (pts), $1$ (lines) | `o ----- o` | Only 2 types; they form a projective plane. |
| 3D Projective Space $PG(3, q)$ | $0$ (pts), $1$ (lines), $2$ (planes) | `o --- o --- o` | Fixing a plane gives a projective plane; fixing a point gives a projective plane; fixing a line gives a digon. |
| $d$-Dim Projective Space $PG(d, q)$ | $0, 1, \dots, d-1$ | `o --- o --- ... --- o` | A chain of $d$ nodes connected by single strokes ($A_d$ diagram). |
| 3D Cube (or Polar Space of Rank 3) | $0, 1, 2$ | `o --- o === o` | Fixing type $2$ gives a projective plane; fixing type $0$ gives a generalized quadrangle ($B_3 / C_3$ diagram). |
| Affine Space $AG(3, q)$ | $0$ (pts), $1$ (lines), $2$ (planes) | `o --L-- o ----- o` | Fixing a plane gives an affine plane (which is a linear space $L$, not a projective plane); fixing a point gives a projective plane of lines and planes through that point. |


#### How Do Diagrams Help?

For a single 3D cube, we obviously do not need a diagram to know what a cube looks like. The power of the diagram appears when we go in the opposite direction: when we do not know what the global space looks like, or when we are working in dimensions or finite fields where we cannot visualize the object at all. Here are the four concrete things a diagram does for us.

**The Rigidity Theorem: Local Rules Force the Global Space**: Suppose we do not know what our global geometry $\Gamma$ is, or how many elements it has. All we know is its local diagram:

* Around every vertex, edges and faces meet like a triangle (`---`).
* Inside every face, vertices and edges form a square (`===`).
* Along every edge, vertices and faces form a digon (blank).

Can we glue squares and triangles together in some weird, arbitrary way to get thousands of different irregular polyhedra that all obey this local rule? No. Tits proved that if the geometry is simply connected (doesn't wrap around on itself like a quotient), there is one and only one thin geometry in the universe with the diagram `o === o --- o`: the 3D cube (and its dual, the octahedron, obtained by reading the diagram backwards).

More importantly, what if we thicken the diagram over a finite field $\mathbb{F}_q$ (so each triangle becomes a thick projective plane $PG(2, q)$ with $q+1$ points per line, and each square becomes a thick generalized quadrangle with $q+1$ points per line)?
With zero coordinate equations, the diagram `o === o --- o` immediately tells us that the global space is a Polar Space of rank $3$ (such as a non-degenerate quadric of Witt index $t = 3$, where the 3 types are points, lines, and planes lying entirely on the quadric).

**Instant Dualities and Hidden Isomorphisms (Reading the Diagram)**

Because the diagram encodes the entire axiom system visually, any symmetry of the diagram immediately gives us a geometric theorem:

* Dualities (Flipping the Diagram Left-to-Right): Look at the cube diagram `o === o --- o`. If we reverse the order of the types (read it from right to left, swapping vertices $0$ and faces $2$), the diagram becomes `o --- o === o`. Geometrically, swapping vertices and faces turns the cube into the regular octahedron (where faces are triangles and $4$ faces meet at every vertex). Because it is the exact same diagram just read right-to-left, the cube and the octahedron are isomorphic as incidence geometries and have the exact same symmetry group. The cube and the octahedron are dual polyhedra, as the cube's 8 vertices and 6 faces perfectly mirror the octahedron's 6 vertices and 8 faces.

* Triality (Three-Way Symmetry in $D_4$): When we look at the hyperbolic quadric $Q^+(7, q)$ in 7D projective space (Witt index $t = 4$), its diagram is not a straight line—it is a 4-node Y-shaped star ($D_4$):

```
                    o  (Type 2: + Solids)
                   /
   0 (Points)     1 (Lines)
       o -------- o
                   \
                    o  (Type 3: - Solids)

```

Just by looking at this Y-shaped diagram, we can see that the three outer branches (Points of dimension $0$, and the two families of $3$-dimensional solids on the quadric) are completely symmetric around the central node (Lines).

Without doing a single matrix calculation, the diagram reveals Cartan's Triality: in $Q^+(7, q)$, 0-dimensional points behave identically to 3-dimensional solids, and there is an outer automorphism of the orthogonal group $P\Omega^+(8, q)$ of order $3$ that cycles points and 3-solids into one another.

** Automatic Structural Theorems from Blank Spaces (Disconnected Nodes)**

Whenever a diagram has no edge between two nodes (a generalized digon), we get a massive computational shortcut. For example, in any diagram that is a straight line (like the cube `0 === 1 --- 2` or projective space `0 --- 1 --- 2`), node $0$ and node $2$ have no edge between them, and node $1$ sits between them. 

In Buekenhout-Tits theory, the Separation Theorem states that whenever node $1$ separates node $0$ from node $2$ in the diagram: * A point $P$ (type $0$) and a plane/face $\Pi$ (type $2$) are incident in the global space if and only if they share a common line/edge $\ell$ (type $1$) between them. Furthermore, the entire geometry is completely determined by just the elements of type $0$ (points) and their shadows on the other nodes.

**Counting Elements and Group Orders Mechanically**

The diagram also gives us a recipe to calculate the exact number of elements and the exact size of the symmetry group just by multiplying local numbers.

Take the cube diagram `0 === 1 --- 2`:

* In a square (`0 === 1`), each edge has $2$ vertices, and each vertex of that square meets $2$ edges.
* In a triangle (`1 --- 2`), each vertex has $3$ faces/edges, and each face/edge at that vertex meets $2$ others.
* From those tiny numbers ($2$ and $3$) on the 2-node pieces of the diagram, Coxeter/Tits theory immediately computes the total number of chambers of the cube:

$$\vert{}\text{Chambers}\vert{} = 2^3 \times 3! = 8 \times 6 = 48$$

And from $48$ chambers:
* Since each vertex residue (triangle `1 --- 2`) has $3 \times 2 = 6$ chambers, the cube must have $48 / 6 = 8$ vertices.
* Since each face residue (square `0 === 1`) has $4 \times 2 = 8$ chambers, the cube must have $48 / 8 = 6$ faces.
* Since each edge residue (digon `0   2`) has $2 \times 2 = 4$ chambers, the cube must have $48 / 4 = 12$ edges.



Notice what just happened: we never drew a 3D cube. We only knew that one rank-2 piece was a triangle ($6$ chambers) and the other rank-2 piece was a square ($8$ chambers), and the diagram forced the global object to have $8$ vertices, $12$ edges, $6$ faces, and a symmetry group of order $48$.

| Without the Diagram | With the Diagram |
| --- | --- |
| We have to visualize a high-dimensional space or solve systems of quadratic equations over $\mathbb{F}_q$. | We only look at a tiny graph of 2-node building blocks (triangles, squares, projective planes, quadrangles). |
| Proving two geometries or groups are isomorphic requires explicit coordinate transformations. | If their diagrams match (up to flipping or rotating the graph), the geometries and their groups match automatically. |
| Counting subspaces of dimension $k$ requires new combinatorial arguments each time. | Deleting node $k$ from the diagram tells us the exact size of the stabilizer subgroup, letting us divide total chambers by residue chambers. |

## Autocorrelations, Automorphisms & Collineations

### Autocorrelations

An autocorrelation $\alpha$ is a bijection $\alpha: X \to X$ that preserves incidence ($x * y \iff \alpha(x) * \alpha(y)$) and maps elements of the same type to elements of the same type:

$$\text{type}(x) = \text{type}(y) \iff \text{type}(\alpha(x)) = \text{type}(\alpha(y))$$

Notice that this definition does not require $\alpha(x)$ to have the exact same type as $x$—it only requires that if $x$ and $y$ share a type (say, both are points), then $\alpha(x)$ and $\alpha(y)$ must also share a type (say, both become planes).

Because $\alpha$ sends all elements of a given type $i \in I$ into a single target type $j \in I$,  $\alpha$ gives us a well-defined permutation $\alpha_I: I \to I$ on the set of types itself, defined by: $\alpha_I(\text{type}(x)) = \text{type}(\alpha(x))$

Visually,  $\alpha_I$ is the action of $\alpha$ on the nodes of the Buekenhout-Tits diagram:

-   In $PG(3, q)$ with $I = \{0 \text{ (points)}, 1 \text{ (lines)}, 2 \text{ (planes)}\}$, a duality sends all points ($0$) to planes ($2$), all lines ($1$) to lines ($1$), and all planes ($2$) to points ($0$).
    
-   Here, the induced permutation $\alpha_I$ on the type set $I = \{0, 1, 2\}$ is the swap $\alpha_I = (0 \,\, 2)(1)$, which flips the diagram `0 --- 1 --- 2` left-to-right.

The autocorrelation $\alpha$ is an automorphism of $\Gamma$ if $\alpha$ induces the identity on $I$ i.e. it is type preserving. It maps points to points, lines to lines, and planes to planes, or $\alpha_I(i) = i$ for all $i \in I$.

So autocorrelation ($\text{Cor}(\Gamma)$) is the overarching term for any incidence-preserving symmetry of $\Gamma$, whether it scrambles the types in $I$ or keeps them fixed. Automorphism ($\text{Aut}(\Gamma)$) is reserved strictly for an autocorrelation where the induced permutation $\alpha_I$ on the types is the identity permutation ($\alpha_I(i) = i$ for all $i \in I$).

Different textbooks use the word "automorphism" in one of two ways—some authors define $\text{Aut}(\Gamma)$ to mean only the type-preserving automorphisms (which are the collineations), while calling the larger group that includes dualities as the correlation group or extended automorphism group $\text{Cor}(\Gamma)$. In rank $2$, i.e., a projective plane $PG(2, q)$, hyperplanes are lines, so a duality literally swaps points and lines.
    
#### Order of an Autocorrelation

Because an autocorrelation $\alpha$ lives in two worlds at once—it permutes the actual geometric elements in $X$, and it induces a permutation $\alpha_I$ on the type set $I$—there are two closely related "orders" to keep track of:

**The Group-Theoretic Order $\vert{}\alpha\vert{}$ (Action on $X$)**

As a bijection $\alpha: X \to X$, the order of $\alpha$ is the smallest positive integer $m$ such that applying $\alpha$  $m$ times sends every element $x \in X$ back to itself:

$$\alpha^m = \text{id}_X \quad (\text{i.e., } \alpha^m(x) = x \text{ for all } x \in X)$$

**The Induced Type-Order $\vert{}\alpha_I\vert{}$ (Action on the the Buekenhout-Tits Diagram)**

The order of the induced permutation $\alpha_I \in \text{Sym}(I)$ is the smallest positive integer $k$ such that applying $\alpha$  $k$ times brings every type back to its original type:

$$(\alpha_I)^k = \text{id}_I \iff \alpha^k \text{ is an automorphism of } \Gamma$$

Because $\alpha \mapsto \alpha_I$ is a group homomorphism from $\text{Cor}(\Gamma)$ to $\text{Sym}(I)$ whose kernel is $\text{Aut}(\Gamma)$, the induced type-order $k = \vert{}\alpha_I\vert{}$ always divides the full order $m = \vert{}\alpha\vert{}$.

But why do we care about $\alpha_I$? Because if the order of $\alpha_I$ is $1$, then $\alpha$ is an automorphism. Similarly if the order of $\alpha_I$ is $2$, this is called a duality of $PG(d, q)$ where $\alpha_I$ swaps $0 \leftrightarrow d-1$. Then $\alpha^2$ is guaranteed to be an automorphism, even if $\alpha^2$ still permutes the individual points among themselves. If both $\alpha$ and $\alpha_I$ are of order 2, this is called a polarity. We will see shortly, with an example of the Fano Plane, that $\alpha$ could be quite different from $2$ even if $\alpha_I = 2$.

Note that if a textbook simply asks for "the order of an autocorrelation $\alpha$" without specifying $\alpha_I$, it always means the first order—the number of steps $m$ needed for $\alpha^m$ to fix every individual element in $X$.

Let's compare $\alpha$ vs. $\alpha_I$ with the example of the Fano Plane $PG(2, 2)$, which has $7$ points $\{P_1, \dots, P_7\}$ and $7$ lines $\{\ell_1, \dots, \ell_7\}$ ($14$ elements in total). It's diagram contains only two nodes.     

Suppose we pick an autocorrelation $\alpha$ that swaps points and lines in such a way that applying $\alpha$ once ($1$ step) sends every point to a line, and every line to a point. However, when we apply $\alpha$ twice ($\alpha^2$), point $P_1$ does not land back on $P_1$; instead,  $P_1$ lands on a different point $P_2$, and it takes $14$ steps ($\alpha^{14}$) for every individual point $P_i$ and line $\ell_i$ to return to its exact starting spot. Thus, order of $\alpha = 14$ but order of $\alpha_I=2$.

Let's look at some more examples. 

**In Projective Space $PG(d, q)$ (Diagram $A_d$:  `0 --- 1 --- ... --- d-1`):** The diagram is a straight line, so its only non-trivial diagram symmetry $\alpha_I$ is flipping the line left-to-right ($i \mapsto d - 1 - i$), which has type-order $k = 2$.
    
Therefore, for any correlation $\alpha$ that swaps points and hyperplanes, its square $\alpha^2$ is guaranteed to be a type-preserving automorphism (collineation).
        
What is the full order $m = \vert{}\alpha\vert{}$ on $X$? It can be any even number $2r$. In the special case where $m = 2$ (meaning $\alpha^2 = \text{id}_X$, so if point $P$ goes to hyperplane $\Pi$, then hyperplane $\Pi$ goes back to the exact same point $P$), the correlation of order $2$, as we saw, is called a polarity (which defines polar spaces: quadrics, symplectic spaces, and Hermitian varieties). 
        
**In the Hyperbolic Quadric $Q^+(7, q)$ (Diagram $D_4$: Y-shaped with 3 outer nodes):** Because the $D_4$ diagram has 3 identical outer branches (points,  $+$-solids, and $-$-solids), an autocorrelation $\alpha$ can induce a 3-cycle $\alpha_I$ on those 3 types (a triality).
    
Here, the induced type-order on the diagram is $k = 3$ (or $k = 2$ if it swaps two branches, up to $\text{Sym}(3)$ of order $6$).
        
When $\alpha^3 = \text{id}_X$, the autocorrelation has full order $3$ and is called a triality of order $3$.
        
**In the 3D Cube (Diagram $B_3$:  `0 === 1 --- 2`):** Look at the two ends of the cube's diagram: node $0$ has a double stroke `===` attached to it, while node $2$ has a single stroke `---` attached to it. Because a square (`===`) is not isomorphic to a triangle (`---`), you cannot flip the cube's diagram left-to-right without changing the geometry.
    
Thus, for the cube, the only possible permutation $\alpha_I$ is the identity ($k = 1$). Every autocorrelation of the cube is already a type-preserving automorphism.

### Collineations
A collineation is a bijection on the points that sends full lines to full lines (and higher subspaces to higher subspaces) while maintaining incidence relations. Note that we cannot send a line to any other arbitrary line because a collineation must preserve incidence (intersections). Suppose two lines $\ell_1$ and $\ell_2$ intersect at a point $P$. Any valid collineation $\phi$ must send $\ell_1$ and $\ell_2$ to two lines $\phi(\ell_1)$ and $\phi(\ell_2)$ that also intersect at the point $\phi(P)$. For example, you cannot map two intersecting lines to two skew lines.

This means given any two lines $\ell_1$ and $\ell_2$, there exists a collineation that sends $\ell_1$ to $\ell_2$. But not every bijective mapping of the set of lines is a valid collineation.
    
More specifically, a collineation $\phi$ of a projective space is defined as a bijection on the set of points $\mathcal{P} \to \mathcal{P}$ and a bijection on the set of lines $\mathcal{L} \to \mathcal{L}$ (and all higher subspaces), such that for every point $P$ and every line $\ell$: $P \in \ell \iff \phi(P) \in \phi(\ell)$.

Once a bijection on points maps every collinear triple of points to a collinear triple of points, its action on all lines, planes, and higher subspaces is completely locked in.

From what we have already seen above, we can now see that collineations are automorphisms as they preserve type. Automorphism ($\text{Aut}(\Gamma)$) is the general Buekenhout-Tits term that applies to any incidence geometry $\Gamma$ over any type set $I$ (even geometries that do not have "points" and "lines," such as a graph or a abstract polytope). It simply means an incidence-preserving bijection of $X$ that fixes every type in $I$ ($\alpha_I = \text{id}_I$). Collineation is the classical projective geometry term for that exact same map when the types in $I$ are points, lines, planes, and higher subspaces.

#### What Do Collineations Look Like?
For any projective space $PG(d, q)$ of dimension $d \ge 2$ over a finite field $\mathbb{F}_q$ (where $q = p^h$ for a prime $p$), the Fundamental Theorem of Projective Geometry tells us exactly what the collineation group $P\Gamma L(d+1, q)$ is made of. 

Every collineation is a combination of two operations on the homogeneous coordinate vectors $\mathbf{x} = (x_0, x_1, \dots, x_d)$:

Projective Linear Transformations ($PGL(d+1, q)$): Multiplying the coordinate vector by any invertible $(d+1) \times (d+1)$ matrix $A$ over $\mathbb{F}_q$: $\mathbf{x} \mapsto A\mathbf{x}$
    
Field Automorphisms ($\text{Aut}(\mathbb{F}_q)$): Applying a Frobenius field automorphism $\sigma(x) = x^{p^k}$ to every coordinate of the vector: $(x_0, x_1, \dots, x_d) \mapsto (x_0^\sigma, x_1^\sigma, \dots, x_d^\sigma)$
    
Together, all invertible matrices combined with all field automorphisms (modulo scalar multiples $cI$) give the exact group of all collineations $P\Gamma L(d+1, q)$ of $PG(d, q)$.

#### Collineations & Automorphisms
First, a few definitions. A linear map (also called a linear transformation or linear operator) is a map between two vector spaces that preserves the operations of vector addition and scalar multiplication. So we have $A(a_1u + a_2v) = a_1A(u) + a_2A(v)$. Note that this means $A(cu) = cA(u)$.

A field isomorphism or skew-field isomorphism $\sigma: K \to K'$ (where $K, K'$ are two fields or division rings (skew fields)) is a mapping of scalars in $K$ to $K'$. It is a bijection so every scalar in $K'$ comes from a unique scalar in $K$. It also preserves addition and multiplication for all scalars: $\sigma(a + b) = \sigma(a) + \sigma(b) \quad \text{and} \quad \sigma(a \cdot b) = \sigma(a) \cdot \sigma(b)$.
    
This automatically forces $\sigma(0) = 0$ and $\sigma(1) = 1$. However, other scalars could get scrambled. 

Note that a field isomorphism becomes an automorphism if it maps a field into itself. 

A semilinear transformation is what you get if you take a linear transformation and replace the scalar multiplication with a field isomorphism. So a semilinear transformation is specified by the pair $(A, \sigma)$, where $A: V \to V'$ is the map on vectors and $\sigma: K \to K'$ is the accompanying field isomorphism.

**Additivity:** $A(\mathbf{x} + \mathbf{y}) = A(\mathbf{x}) + A(\mathbf{y})$
    
**Twisted Homogeneity:**  $A(k\mathbf{x}) = \sigma(k)A(\mathbf{x})$

Thus if we "remove" $\sigma$—meaning we set $\sigma$ to be the trivial identity map $\sigma(k) = k$—then the rule $A(k\mathbf{x}) = \sigma(k)A(\mathbf{x})$ becomes $A(k\mathbf{x}) = kA(\mathbf{x})$, which is an ordinary linear map. Thus, every linear transformation is a special case of a semilinear transformation where $\sigma = \text{id}_K$.

Let's look at two familiar examples of a semilinear map:

**Complex Conjugation over $\mathbb{C}$:** Let $V = \mathbb{C}^3$ over the complex numbers $K = \mathbb{C}$, and let $\sigma(z) = \bar{z}$ (complex conjugation), which is an automorphism of the field $\mathbb{C}$ since $\overline{z_1 + z_2} = \bar{z}_1 + \bar{z}_2$ and $\overline{z_1 z_2} = \bar{z}_1 \bar{z}_2$. Now define $A(x_0, x_1, x_2) = (\bar{x}_0, \bar{x}_1, \bar{x}_2)$. What happens when we scale a vector $\mathbf{x}$ by $k = i$ before applying $A$?
    
$$A(i\mathbf{x}) = \overline{(i\mathbf{x})} = -i\bar{\mathbf{x}} = \sigma(i)A(\mathbf{x})$$
    
Because $i$ came out as $-i = \sigma(i)$ instead of $+i$,  $A$ is not linear over $\mathbb{C}$—it is semilinear with accompanying automorphism $\sigma(z) = \bar{z}$.

**Frobenius Automorphisms over Finite Fields $\mathbb{F}_q$:** In a finite field $\mathbb{F}_q$ where $q = p^h$ (for instance,  $\mathbb{F}_4$ or $\mathbb{F}_8$ or $\mathbb{F}_9$), the map $\sigma(k) = k^p$ is a non-trivial field automorphism ($\sigma(a+b) = (a+b)^p = a^p + b^p$ and $\sigma(ab) = a^p b^p$). Raising every coordinate of a vector $\mathbf{x} = (x_0, \dots, x_d)$ to the $p$-th power, combined with multiplying by an invertible matrix $M$, gives a semilinear map:
    
$$A(\mathbf{x}) = \mathbf{x}^\sigma M$$

So why do we care about semilinear maps? Because they represent collineations. You might expect collineations to be represented by just linear maps. Linear maps do represent some but not all collineations. Why? Because a projective point is not defined as a single vector $\mathbf{x}$; it is an entire equivalence class and 1-dimensional subspace $\langle \mathbf{x} \rangle = \{k\mathbf{x} \mid k \in K\}$.

If we want a map $A: V \to V$ to send a projective point $\langle \mathbf{x} \rangle$ to a well-defined projective point $\langle A(\mathbf{x}) \rangle$, we need all scalar multiples $k\mathbf{x}$ of $\mathbf{x}$ to land inside the same 1-dimensional subspace spanned by $A(\mathbf{x})$.

Look at what a semilinear map does to the set of scalar multiples $\{k\mathbf{x} \mid k \in K\}$:

$$A(\langle \mathbf{x} \rangle) = \{A(k\mathbf{x}) \mid k \in K\} = \{\sigma(k)A(\mathbf{x}) \mid k \in K\} = \langle A(\mathbf{x}) \rangle$$

Because $\sigma: K \to K$ is a bijection on the scalars, as $k$ sweeps over all of $K$, $\sigma(k)$ also sweeps over all of $K$. And what about a projective line joining $\langle \mathbf{x} \rangle$ and $\langle \mathbf{y} \rangle$ (the 2D subspace $\{k_1\mathbf{x} + k_2\mathbf{y} \mid k_1, k_2 \in K\}$)?

$$A(k_1\mathbf{x} + k_2\mathbf{y}) = \sigma(k_1)A(\mathbf{x}) + \sigma(k_2)A(\mathbf{y})$$

It maps the entire line through $\langle \mathbf{x} \rangle$ and $\langle \mathbf{y} \rangle$ directly onto the line through $\langle A(\mathbf{x}) \rangle$ and $\langle A(\mathbf{y}) \rangle$. 

In short: Once again, linear maps are NOT the only maps on $V$ that preserve projective lines. Semilinear maps preserve projective points, lines, planes, and incidence just as well as linear maps do, because geometry only cares about whether two vectors lie in the same 1D span, i.e. are they a scaled version of each other, and not which specific scalar $k$ vs. $\sigma(k)$ labeled them.

Furthermore, the Fundamental Theorem of Projective Geometry proves the converse: in dimension $d \ge 2$, every collineation (automorphism) of $\mathbf{P}(V)$ comes from a semilinear transformation of $V$. If we left out semilinear transformations and only used linear ones, we would miss part of the collineation group whenever $K$ has non-trivial field automorphisms. We'll look at this a little more in a bit.

Let's look at something called an inner automorphism. An inner automorphism is a symmetry (automorphism) of a group or a skew field that is created entirely from the inside of the algebraic structure, simply by picking one fixed invertible element $c$ and sandwiching every element $x$ between $c$ and $c^{-1}$ or conjugating by $c$.

Let $K$ be a skew field (division ring), and pick any fixed non-zero element $c \in K^\times$. The map $\sigma_c: K \to K$ defined for all $x \in K$ by $\sigma_c(x) = c x c^{-1}$ is called the inner automorphism of $K$ induced by $c$. 

Let us check that is obeys the rules of a semilinear map: it must be a bijection that preserves both addition and multiplication. Just from the distributive and associative laws of $K$, we can see that it preserves addition:
    
$$\sigma_c(x + y) = c(x + y)c^{-1} = cxc^{-1} + cyc^{-1} = \sigma_c(x) + \sigma_c(y)$$
    
Preserves Multiplication (Notice how $c^{-1}$ and $c$ cancel in the middle):
    
$$\sigma_c(x \cdot y) = c(xy)c^{-1} = cx(c^{-1}c)yc^{-1} = (cxc^{-1})(cyc^{-1}) = \sigma_c(x) \cdot \sigma_c(y)$$
    
Bijection (Reversible): To undo the sandwiching by $c$, we simply sandwich by $c^{-1}$, since $c^{-1}(cxc^{-1})c = x$.

What is the difference between inner and outer automorphisms? In any algebraic system, inner automorphisms are automorphisms of the form $\sigma_c(x) = cxc^{-1}$ that can be written using the multiplication of an element $c$ that already lives inside $K$. Outer automorphisms are ones that cannot be written as $cxc^{-1}$ for any $c \in K^\times$. For example, complex conjugation $\sigma(a + bi) = a - bi$ in $\mathbb{C}$ or the Frobenius map $\sigma(x) = x^p$ in $\mathbb{F}_q$ cannot be achieved by multiplying by a number and its inverse—they are genuine external symmetries of the field.

Inner automorphisms are found only in skew fields. In a commutative field, it reduces to the identity and so we end up with a linear map. because if $K$ is an ordinary commutative field (like $\mathbb{R}$,  $\mathbb{C}$, or $\mathbb{F}_q$), then for any non-zero constant $c \in K^\times$:

$$c k c^{-1} = c c^{-1} k = 1 \cdot k = k$$

So in a commutative field,  $\sigma(k) = ckc^{-1}$ is just the identity $\sigma(k) = k$.

In a skew field $K$, where multiplication is not commutative ($ck \neq kc$), suppose we take an ordinary linear map $L: V \to V$ (which has $\sigma = \text{id}_K$, so $L(k\mathbf{x}) = kL(\mathbf{x})$), and we scale the entire map $L$ on the left by a fixed non-zero scalar $c \in K^\times$ to define a new map $A(\mathbf{x}) = cL(\mathbf{x})$.

Notice that on projective space $\mathbf{P}(V)$,  $A(\mathbf{x}) = cL(\mathbf{x})$ and $L(\mathbf{x})$ define the same projective point, because $\langle cL(\mathbf{x}) \rangle = \langle L(\mathbf{x}) \rangle$. Yet look at what happens when we plug $k\mathbf{x}$ into $A(\mathbf{x}) = cL(\mathbf{x})$:

$$A(k\mathbf{x}) = c L(k\mathbf{x}) = c \big(k L(\mathbf{x})\big) = (ck) L(\mathbf{x})$$

We want to rewrite $L(\mathbf{x})$ in terms of $A(\mathbf{x}) = cL(\mathbf{x})$, so we insert $c^{-1}c = 1$:

$$A(k\mathbf{x}) = (ckc^{-1}) \big(c L(\mathbf{x})\big) = (ckc^{-1}) A(\mathbf{x})$$

Look at the scalar factor in front of $A(\mathbf{x})$: because $c$ and $k$ do not commute, scaling a purely linear map $L$ by $c$ turned its scalar rule into $\sigma(k) = ckc^{-1}$.

What this calculation shows is that any semilinear map $A$ whose $\sigma$ is an inner automorphism $\sigma(k) = ckc^{-1}$ is just $c$ times a purely linear map $L(\mathbf{x}) = c^{-1}A(\mathbf{x})$, and both $A$ and $L$ induce the exact same collineation on $\mathbf{P}(V)$.

**Motivation Behind Inner Automorphisms**

Let us look at why we need inner automorphisms before looking at an example. The entire reason we have to talk about inner automorphisms is to solve an embarrassing algebraic glitch that happens when we try to do Nothing (the identity map) in projective space over a non-commutative skew field.

Let us look at what goes wrong when we try to scale a vector by a constant $c$, and how inner automorphisms fix it.

In projective space $\mathbf{P}(V)$, any vector $\mathbf{x}$ and its scalar multiple $c\mathbf{x}$ (for a fixed non-zero constant $c \in K^\times$) represent the exact same projective point:

$$\langle c\mathbf{x} \rangle = \langle \mathbf{x} \rangle$$

So suppose we define a map $S_c: V \to V$ on our left vector space $V$ that simply multiplies every vector on the left by a fixed constant $c \in K^\times$:

$$S_c(\mathbf{x}) = c\mathbf{x}$$

Geometrically, what does $S_c$ do to the points of projective space $\mathbf{P}(V)$? Nothing at all! It sends every projective point $\langle \mathbf{x} \rangle$ to $\langle c\mathbf{x} \rangle = \langle \mathbf{x} \rangle$. It induces the identity collineation on $\mathbf{P}(V)$.

Now ask the algebra question: Is this trivial scaling map $S_c(\mathbf{x}) = c\mathbf{x}$ a linear transformation of $V$? Let us test the linear transformation rule $S_c(k\mathbf{x}) = k S_c(\mathbf{x})$:

-   Left side:  $S_c(k\mathbf{x}) = c(k\mathbf{x}) = (ck)\mathbf{x}$.
    
-   Right side:  $k S_c(\mathbf{x}) = k(c\mathbf{x}) = (kc)\mathbf{x}$.
 
If $K$ is non-commutative ($ck \neq kc$), the left side does NOT equal the right side! That means in a left vector space over the quaternions $\mathbb{H}$, multiplying every vector by $c = i$ is NOT a linear map.

Instead, look at what $S_c$ actually obeys:

$$S_c(k\mathbf{x}) = (ck)\mathbf{x} = (ckc^{-1})(c\mathbf{x}) = \sigma_c(k) S_c(\mathbf{x})$$

Because $ck = (ckc^{-1})c$, the trivial scaling map $S_c(\mathbf{x}) = c\mathbf{x}$ is actually a semilinear map whose accompanying automorphism is the inner automorphism $\sigma_c(k) = ckc^{-1}$.

In projective geometry, we want to build a dictionary between:

-   Geometry: Collineations of $\mathbf{P}(V)$ (which live in $P\Gamma L(V)$ and $PGL(V)$), and

-   Algebra: Transformations of the vector space $V$ (which live in $\Gamma L(V)$ and $GL(V)$).

To pass from the vector space $V$ to the projective space $\mathbf{P}(V)$, we have to quotient out (divide out) all the scaling maps $S_c(\mathbf{x}) = c\mathbf{x}$ that do nothing to projective points. Look at what happens in that quotient if we did not know about inner automorphisms:

1.  Over a commutative field $\mathbb{F}$, all scaling maps $S_c(\mathbf{x}) = c\mathbf{x}$ are linear ($\sigma = \text{id}$), so they sit inside $GL(V)$, and we simply write: $PGL(V) = GL(V) / \{S_c\}$
    
2.  Over a non-commutative skew field $K$, the scaling maps $S_c(\mathbf{x}) = c\mathbf{x}$ are NOT inside $GL(V)$ (unless $c$ is in the center $Z(K)$ of the skew field, meaning $c$ commutes with everything). Most scaling maps $S_c$ actually sit out in the semilinear group $\Gamma L(V)$ with inner automorphisms $\sigma_c(k) = ckc^{-1}$.

Therefore, when we ask: "Which semilinear maps $(A, \sigma)$ in $\Gamma L(V)$ represent a pure matrix collineation in $PGL(V)$ (like a central collineation)?"

-   We cannot simply say "the ones with $\sigma = \text{id}$," because if someone takes a linear map $L$ (with $\sigma = \text{id}$) and multiplies it by a harmless scalar $c$ to get $A(\mathbf{x}) = cL(\mathbf{x})$ (which is the exact same collineation on $\mathbf{P}(V)$!), its $\sigma$ suddenly changes from $\text{id}$ to the inner automorphism $\sigma_c(k) = ckc^{-1}$.

-   Conversely, if a semilinear map $(A, \sigma)$ happens to have an inner automorphism $\sigma(k) = ckc^{-1}$, we can multiply $A$ by $c^{-1}$ to get $L(\mathbf{x}) = c^{-1}A(\mathbf{x})$, which kills off the $\sigma_c$ and turns the map back into an ordinary linear matrix $L$ with $\sigma = \text{id}$.
  
In short, inner automorphisms are not a new geometric transformation we are trying to construct—they are simply the "gauge freedom" (coordinate redundancy) created by scaling vectors by a non-commuting constant $c$:


| Level | What Plays the Role of "Trivial Scaling" (Doing Nothing Geometrically) | What Plays the Role of "Pure Projective Linear Transformations" $PGL(V)$ |
| --- | --- | --- |
| On Vectors $V$ | Multiplying a vector by $c \in K^\times$: $\mathbf{x} \mapsto c\mathbf{x}$ | Linear maps $L \in GL(V)$, or scalar multiples $cL$ |
| On Scalars $K$ | Inner automorphisms $\sigma_c(k) = ckc^{-1} \in \text{Inn}(K)$ | Semilinear maps $(A, \sigma)$ where $\sigma \in \text{Inn}(K)$ (because dividing $A$ by $c$ makes $\sigma = \text{id}$) |
| On Projective Space $\mathbf{P}(V)$ | The identity map $\langle c\mathbf{x} \rangle = \langle \mathbf{x} \rangle$ | The group $PGL(V)$, which contains all central collineations |

So the only reason the textbook mentions inner automorphisms is bookkeeping:

Scaling a vector by $c$ does nothing in projective space.

In a non-commutative skew field, scaling by $c$ twists scalars by the inner automorphism $ckc^{-1}$.

Therefore, any inner automorphism $ckc^{-1}$ can be canceled out just by rescaling our map by $c^{-1}$, reducing the semilinear map to a pure linear matrix.
    
Once we know that, whenever we see "$\sigma$ is an inner automorphism" in a theorem, we can immediately translate it in our heads as: "After rescaling by a constant $c^{-1}$, we can set $\sigma = \text{id}$ and treat the map as an ordinary linear matrix."

Now let's work on an example. Let us compare what $\sigma_c(x) = cxc^{-1}$ does in an ordinary commutative field versus a non-commutative skew field like the quaternions $\mathbb{H}$:

-   Case A: In any commutative field (like $\mathbb{R}$,  $\mathbb{C}$, or $\mathbb{F}_q$): Because multiplication is commutative ($cx = xc$), the $c$ and $c^{-1}$ immediately cancel out for every $x$:
    
    $$\sigma_c(x) = cxc^{-1} = cc^{-1}x = 1 \cdot x = x$$
    
    Therefore, in a commutative field, every inner automorphism is just the trivial identity map $\sigma(x) = x$.
    
-   Case B: In the non-commutative skew field of Quaternions $\mathbb{H}$: Recall that in $\mathbb{H}$, the basis elements $i, j, k$ satisfy $i^2 = j^2 = k^2 = -1$ (so $i^{-1} = -i$), and $ij = k = -ji$,  $ik = -j = -ki$. Now pick the fixed non-zero quaternion $c = i$, and form the inner automorphism $\sigma_i(x) = i x i^{-1} = -ixi$:
    
    -   On $x = 1$:  $\sigma_i(1) = i(1)i^{-1} = 1$
        
    -   On $x = i$:  $\sigma_i(i) = i(i)i^{-1} = i$
        
    -   On $x = j$:  $\sigma_i(j) = i(j)(-i) = k(-i) = -j$
        
    -   On $x = k$:  $\sigma_i(k) = i(k)(-i) = (-j)(-i) = -k$

    Look at what happened: for a general quaternion $x = a + bi + cj + dk$, the inner automorphism $\sigma_i$ sends:
    
    $$\sigma_i(a + bi + cj + dk) = a + bi - cj - dk$$
    
    Even though we only multiplied by $i$ on the left and $i^{-1}$ on the right, the non-commutativity of $\mathbb{H}$ flipped the signs of the $j$ and $k$ components, creating a genuine, non-trivial automorphism of $\mathbb{H}$ (geometrically, a 180-degree rotation around the $i$-axis in 3D space).

This matters for projective space $\mathbf{P}(V)$, where a projective point is the 1D subspace $\langle \mathbf{v} \rangle = \{k\mathbf{v} \mid k \in K\}$. If we take a purely linear map $L: V \to V$ (which obeys $L(k\mathbf{v}) = kL(\mathbf{v})$) and multiply its output on the left by a fixed non-zero scalar $c \in K^\times$ to define $A(\mathbf{v}) = cL(\mathbf{v})$:

Geometrically on $\mathbf{P}(V)$,  $A$ and $L$ do the exact same thing to every projective point, because scaling a vector by $c$ does not change which 1D line through the origin it spans:  $\langle cL(\mathbf{v}) \rangle = \langle L(\mathbf{v}) \rangle$.
    
Algebraically on $V$, however, when a scalar $k$ passes through $A(\mathbf{v}) = cL(\mathbf{v})$, it gets conjugated by $c$:
    
$$A(k\mathbf{v}) = cL(k\mathbf{v}) = ckL(\mathbf{v}) = (ckc^{-1})\big(cL(\mathbf{v})\big) = \sigma_c(k)A(\mathbf{v})$$

So in projective geometry over a skew field $K$, saying "a semilinear map $A$ has an inner automorphism $\sigma_c(k) = ckc^{-1}$" is simply the algebraic way of saying "$A$ is just a scalar multiple $cL$ of an ordinary linear map $L$."

Now for a few properties of semilinear maps. 

| Goal | Mathematical Statement | What It Means Conceptually |
| --- | --- | --- |
| Semilinear $\implies$ Collineation | Any bijective semilinear map $A: V \to V$ induces a collineation (automorphism) $\alpha$ of $\mathbf{P}(V)$ via $\alpha(\langle \mathbf{x} \rangle) = \langle A(\mathbf{x}) \rangle$. | Both matrices ($PGL$) and field automorphisms ($\sigma$) produce valid geometric symmetries of $\mathbf{P}(V)$, giving the group $P\Gamma L(V)$. |
| When Two Maps Give the Same Collineation | Two semilinear maps $A_1, A_2$ induce the exact same collineation on $\mathbf{P}(V)$ if and only if $A_2(\mathbf{x}) = c A_1(\mathbf{x})$ for a fixed scalar $c \in K^\times$. | Scaling every vector by a global constant $c$ doesn't move any 1D subspace $\langle \mathbf{x} \rangle$, so we quotient out scalar transformations $Z(GL(V))$. |
| Central Collineations Are strictly Linear | If a semilinear map $A$ induces a central collineation (fixes a hyperplane $H$ pointwise, with $\dim H \ge 1$), then its accompanying automorphism $\sigma$ is forced to be an inner automorphism ($\sigma(k) = c k c^{-1}$), meaning the central collineation can actually be represented by a purely linear map ($\sigma = \text{id}$). | Why? Because fixing all the points on a line inside the axis $H$ freezes all the scalar cross-ratios on that line, which forces $\sigma$ to act trivially on the coordinates. |

That third point is the punchline of the section: while a general collineation of $\mathbf{P}(V)$ requires a semilinear map ($P\Gamma L$), a central collineation (elation or homology) is so constrained by its pointwise-fixed axis $H$ that it can always be written as a pure linear transformation ($PGL$).

Why do we care that central collineations come from linear maps (and not semilinear maps)?

**It Separates Pure Geometry (Matrices) from Field Arithmetic (Galois Theory)**

The full collineation group $P\Gamma L(d+1, K)$ is a mixture of two completely different worlds:

* Matrix transformations ($PGL(d+1, K)$): Coming from linear maps ($\sigma = \text{id}$).
* Field automorphisms ($\text{Aut}(K)$): Coming from Galois theory (like $\sigma(z) = \bar{z}$ or $\sigma(k) = k^p$).

How can you tell, purely from looking at how a collineation moves points and lines in space, whether it came from a pure matrix ($PGL$) or has a field automorphism $\sigma$ mixed in?

Central collineations give us the answer. Because every central collineation is induced by a linear map, the subgroup generated by all central collineations (elations and homologies) consists purely of matrices—it never has any field automorphism twist $\sigma$ in it.

**You Cannot Fix a Line Pointwise If $\sigma \neq \text{id}$**

Why can't a genuinely semilinear map ($\sigma \neq \text{id}$) be a central collineation?

Suppose $\alpha$ is a central collineation with axis $H$. Inside the hyperplane $H$, pick a line $\ell$ spanned by two basis points $P_1 = \langle \mathbf{e}_1 \rangle$ and $P_2 = \langle \mathbf{e}_2 \rangle$, and also containing the unit point $U = \langle \mathbf{e}_1 + \mathbf{e}_2 \rangle$.

Because $\ell$ lies inside the axis $H$, every single point on $\ell$ must stay fixed under $\alpha$:

* Fixing $P_1, P_2,$ and $U$ forces $A(\mathbf{e}_1) = \mathbf{e}_1$ and $A(\mathbf{e}_2) = \mathbf{e}_2$ (up to a common scalar).
* Now look at any other point $P_k = \langle \mathbf{e}_1 + k\mathbf{e}_2 \rangle$ on the line $\ell$ (for any scalar $k \in K$).
* Apply our semilinear map $A$ to $P_k$:

$$A(\mathbf{e}_1 + k\mathbf{e}_2) = A(\mathbf{e}_1) + \sigma(k)A(\mathbf{e}_2) = \mathbf{e}_1 + \sigma(k)\mathbf{e}_2$$

* For the point $P_k = \langle \mathbf{e}_1 + k\mathbf{e}_2 \rangle$ to stay fixed on the axis $H$ for every $k \in K$, we must have:

$$\mathbf{e}_1 + \sigma(k)\mathbf{e}_2 = \mathbf{e}_1 + k\mathbf{e}_2 \implies \sigma(k) = k \quad \text{for all } k \in K$$

In other words, if $\sigma(k) \neq k$, then $\alpha$ will move the point $\langle \mathbf{e}_1 + k\mathbf{e}_2 \rangle$ to the different point $\langle \mathbf{e}_1 + \sigma(k)\mathbf{e}_2 \rangle$, making it impossible to freeze an entire line pointwise!

**It Lets Us Write Every Central Collineation as a Simple Matrix**

Because central collineations are guaranteed to be induced by linear maps, we never have to worry about $\sigma$ when computing with elations and homologies. Every central collineation of $\mathbf{P}(V)$ can be written directly as a linear transformation of the form:

$$A(\mathbf{x}) = \mathbf{x} + \varphi(\mathbf{x})\mathbf{c}$$

where $\mathbf{c}$ is a vector spanning the centre $C = \langle \mathbf{c} \rangle$, and $\varphi: V \to K$ is a linear functional whose kernel $\ker(\varphi) = \{ \mathbf{x} \in V \mid \varphi(\mathbf{x}) = 0 \}$ is the hyperplane axis $H$.

In summary:

| Concept | Algebraic Meaning | Geometric Meaning in $\mathbf{P}(V)$ |
| --- | --- | --- |
| Semilinear Map $(A, \sigma)$ | $A(\mathbf{x}+\mathbf{y}) = A(\mathbf{x})+A(\mathbf{y})$ and $A(k\mathbf{x}) = \sigma(k)A(\mathbf{x})$ | Generates the entire collineation group $P\Gamma L(V)$ (matrices + field automorphisms). |
| Linear Map ($A$ with $\sigma = \text{id}$) | $A(k\mathbf{x}) = kA(\mathbf{x})$ (pure matrix multiplication) | Generates the projective linear group $PGL(V)$ (collineations that preserve cross-ratios). |
| Central Collineations (Elations & Homologies) | Always linear: $A(\mathbf{x}) = \mathbf{x} + \varphi(\mathbf{x})\mathbf{c}$ ($\sigma$ is forced to be trivial because the axis $H$ is fixed pointwise). | Elementary projections with a centre $C$ and pointwise-fixed axis $H$; they generate $PSL(V)$ and $PGL(V)$ inside $P\Gamma L(V)$. |

How do we actually compute with semilinear maps if they are not matrices? Even though a semilinear transformation $A: V \to V$ is not a pure matrix, it is almost as easy to compute with. Once we choose a basis $\{\mathbf{e}_0, \mathbf{e}_1, \dots, \mathbf{e}_d\}$ for $V$, every semilinear transformation splits into a two-step assembly line:

1. Apply the field automorphism $\sigma$ to every coordinate of the vector $\mathbf{x}$.
2. Multiply the resulting vector by an ordinary invertible matrix $M$.

Let us derive why this works directly from the definition $A(k\mathbf{x}) = \sigma(k)A(\mathbf{x})$.

Suppose a vector $\mathbf{x} \in V$ has coordinates $(x_0, x_1, \dots, x_d)$ relative to the basis $\{\mathbf{e}_0, \dots, \mathbf{e}_d\}$:

$$\mathbf{x} = x_0 \mathbf{e}_0 + x_1 \mathbf{e}_1 + \dots + x_d \mathbf{e}_d$$

Now apply the semilinear transformation $A$ to $\mathbf{x}$ using additivity and the $\sigma$-rule:

$$\begin{aligned} A(\mathbf{x}) &= A(x_0 \mathbf{e}_0 + x_1 \mathbf{e}_1 + \dots + x_d \mathbf{e}_d) \\ &= A(x_0 \mathbf{e}_0) + A(x_1 \mathbf{e}_1) + \dots + A(x_d \mathbf{e}_d) \\ &= \sigma(x_0) A(\mathbf{e}_0) + \sigma(x_1) A(\mathbf{e}_1) + \dots + \sigma(x_d) A(\mathbf{e}_d) \end{aligned}$$

Just as in standard linear algebra, each basis image $A(\mathbf{e}_i)$ is some vector in $V$, which can be written as a row of an invertible $(d+1) \times (d+1)$ matrix $M = (m_{ij})$.

If we write $\mathbf{x}^\sigma$ for the coordinate vector where $\sigma$ has been applied to each entry:

$$\mathbf{x}^\sigma = \big(\sigma(x_0), \, \sigma(x_1), \, \dots, \, \sigma(x_d)\big)$$

then the action of the semilinear transformation $A$ on the coordinate row vector $\mathbf{x}$ is simply:

$$A(\mathbf{x}) = \mathbf{x}^\sigma M$$

Or if we write coordinates as column vectors with matrices on the left over a commutative field, $A(\mathbf{x}) = M \mathbf{x}^\sigma$.

---

Let us do a concrete calculation in the projective plane $PG(2, 4)$ over the finite field $\mathbb{F}_4 = \{0, 1, \omega, \omega^2\}$, where $\omega^2 = \omega + 1$ and $\omega^3 = 1$.

In $\mathbb{F}_4$, the Frobenius field automorphism is squaring: $\sigma(k) = k^2$. It swaps $\omega \leftrightarrow \omega^2$ and leaves $0$ and $1$ fixed.

Suppose our semilinear transformation $A$ has the accompanying automorphism $\sigma(k) = k^2$ and the matrix:

$$M = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \omega & 0 \\ 1 & 0 & 1 \end{pmatrix}$$

How do we find the image of the point $\mathbf{x} = (1, \omega, \omega^2)$ under $A$?

1. Step 1 (Apply $\sigma$ entry-by-entry to the coordinate vector $\mathbf{x}$):

$$\mathbf{x}^\sigma = \big(\sigma(1), \, \sigma(\omega), \, \sigma(\omega^2)\big) = (1^2, \, \omega^2, \, \omega^4) = (1, \, \omega^2, \, \omega)$$


2. Step 2 (Multiply $\mathbf{x}^\sigma$ by the matrix $M$):

$$\mathbf{x}' = \mathbf{x}^\sigma M = (1, \, \omega^2, \, \omega) \begin{pmatrix} 1 & 0 & 0 \\ 0 & \omega & 0 \\ 1 & 0 & 1 \end{pmatrix} = (1 + \omega, \, \omega^3, \, \omega) = (\omega^2, \, 1, \, \omega)$$

What happens if we compose two different semilinear transformations $A_1 = (M_1, \sigma_1)$ and $A_2 = (M_2, \sigma_2)$?

Let us apply $A_1$ first, and then apply $A_2$ to the result:

1. Applying $A_1$ to $\mathbf{x}$ gives: $\mathbf{y} = \mathbf{x}^{\sigma_1} M_1$.
2. Applying $A_2$ to $\mathbf{y}$ means we must first apply $\sigma_2$ to every entry of $\mathbf{y}$, and then multiply by $M_2$:

$$A_2(A_1(\mathbf{x})) = \big(\mathbf{x}^{\sigma_1} M_1\big)^{\sigma_2} M_2$$


3. Since $\sigma_2$ is a field automorphism, it distributes across all the additions and multiplications inside $\mathbf{x}^{\sigma_1} M_1$, meaning it hits both $\mathbf{x}^{\sigma_1}$ and every entry of the matrix $M_1$:

$$A_2(A_1(\mathbf{x})) = \mathbf{x}^{\sigma_2 \circ \sigma_1} \big(M_1^{\sigma_2} M_2\big)$$

This gives us the multiplication rule for pairs $(M, \sigma)$ in the semilinear group $\Gamma L(d+1, K)$:

$$(M_1, \sigma_1) \cdot (M_2, \sigma_2) = \big(M_1^{\sigma_2} M_2, \,\, \sigma_2 \circ \sigma_1\big)$$

In group theory, this twisted multiplication rule is called a semidirect product:

$$\Gamma L(d+1, K) = GL(d+1, K) \rtimes \text{Aut}(K)$$

And when we pass to projective space by factoring out scalar matrices, we get the full collineation group:

$$P\Gamma L(d+1, K) = PGL(d+1, K) \rtimes \text{Aut}(K)$$

So in practice, working with a semilinear transformation just means carrying around an ordinary matrix $M$ alongside a field automorphism $\sigma$, applying $\sigma$ to the coordinates, and twisting matrix entries by $\sigma$ whenever a field automorphism jumps across a matrix.

As an aside, note that $PGL(d+1, K)$ operates transitively on the chambers of $P$. Additionally, we define a frame of $P$ as an ordered set of $d+2$ points such that any $d+1$ of them form a basis of $P$. $PGL(d+1, K)$ operates transitively on the frames of $P$. If K is commutative, it operates sharply transitively. In this case, every projective collineation of P is uniquely determined by its definition on a frame.

We should also point out briefly that there are fields called rigid fields. As we saw, the field $\mathbb{C}$ has non-trivial (i.e. other than the identity or mapping a scalar to the same scalar making it a linear map) outer automorphisms (such as the complex conjugation we just saw, as well as uncountably many wild, non-continuous automorphisms). A field $K$ whose only field automorphism is the identity map is called a rigid field. Every semilinear map over a rigid field reduces to an ordinary linear map. The field of real numbers $\mathbb{R}$ has this property. A few other rigid fields include:

**The Rational Numbers ($\mathbb{Q}$):** Any field automorphism must fix $0$ and $1$. Since every rational number is built from $1$ via addition, subtraction, and division, every automorphism of $\mathbb{Q}$ must fix every element ($\sigma(q) = q$).
    
**Prime Finite Fields ($\mathbb{F}_p$ or $\mathbb{Z}/p\mathbb{Z}$):** Like $\mathbb{Q}$, these fields are generated entirely by the element $1$, so no non-trivial automorphism can exist.
    
**Real Closed Fields:** Any algebraic extension of $\mathbb{Q}$ or field equipped with an ordering where positive elements are squares (like $\mathbb{R}$) forces any automorphism to preserve order ($x > 0 \implies x = y^2 \implies \sigma(x) = \sigma(y)^2 > 0$), making non-trivial automorphisms impossible.

This distinction has a major impact on collineations. Over rigid fields, the semilinear group collapses into the projective linear group: $P\Gamma L(n+1, \mathbb{R}) = PGL(n+1, \mathbb{R})$. Every collineation is induced strictly by a matrix (a projective linear transformation). You cannot construct "exotic" collineations using field twists, unlike on $\mathbb{CP}^n$ where complex conjugation $\sigma(z) = \bar{z}$ yields non-linear collineations.

## Polar Spaces & Polarity
We looked at quadratic forms and quadrics. There were in fact special cases of polar spaces. Recall that quadratic sets with their two axioms of three-or-all and tangent space provide a synthetic geometry handle, while quadrics provide an algebraic handle when quadratic sets are embedded in projective spaces. We find a similar distinction here, but we will flip the order of study. 

We will first look at polar spaces and their analysis when they are embedded in projective spaces. This will allow us to apply algebraic tools on them. We will then look at the single axiom which ensures a set of lines and points form a polar space. This is called the One-or-All axiom. This gives us the synthetic geometry analogue to polar spaces in projective spaces. A famous theorem by Jacques Tits assures us that every abstract (synthetic) non-degenerate polar space of rank $\ge 3$ is isomorphic to a classical polar space embedded in a projective space, thus tying these two aspects together.

---

**Aside:** Tits discovered that in rank $3$, there is an exceptional polar space that does not come from a form on a vector space: the polar space of the 27-dimensional exceptional Jordan algebra (the Albert algebra) over the octonions $\mathbb{O}$, whose automorphism group is a form of the exceptional Lie group $E_7$. In rank $\ge 4$, however, the projective planes inside the polar space are forced to be Desarguesian by ambient 3-space intersections, locking you strictly into vector spaces over division rings.

---

### Quadrics Re-redux!
Let's rejig our exploration of quadrics a bit. We defined a quadric as all points where a quadratic form $Q(x) = 0$. We then defined the bilinear form $B(x, y) := q(x + y) - q(x) - q(y)$. Note that by this definition, we end up with a symmetric bilinear form, which means $B(x, y) = B(y, x)$. Remember that we said we really didn't need the quadratic form. We could just as well have defined a bilinear form and then defined the quadric with it because $Q(x) = \frac{1}{2}B(x,x)$... except in char $=2$. It is only because of char $=2$ that we introduced a quadratic form. Additionally, in this situation, the bilinear form is $0$ for all points in the projective space. We need the quadratic form to actually filter the points on the quadric.

The point (sorry!) of all this is that the bilinear form is the key, but in specific cases (quadrics in char $=2$), we need to define a quadratic form to handle weird situations. In every other situation, we needn't even bother defining the quadratic form and in fact we won't for any polar form other than a quadric. Now let's look at two different types of bilinear forms and the closely related sesquilinear form, which will help us define polar spaces. 

### A Few Definitions & An Intuitive Picture
#### Forms & Orthogonality
**Sesquilinear Form $f(x, y)$:** ("Sesqui" is Latin for "one and a half.") It is a generalization of a bilinear form where the first slot is linear, and the second slot is semilinear (twisted by a field automorphism $\sigma$):

$$f(ax, y) = a f(x, y) \quad \text{and} \quad f(x, by) = f(x, y)\sigma(b)$$

Why do we need this? Think of the standard inner product in a complex vector space $\mathbb{C}^n$: if we defined the dot product of $z = (i, 0)$ with itself without complex conjugation, we would get $i^2 = -1$ instead of $+1$ as the length. To fix that, the complex inner product conjugates the second vector: $f(x, y) = x_0 \bar{y}_0 + x_1 \bar{y}_1$. That makes it linear in $x$ and semilinear in $y$ (with $\sigma(z) = \bar{z}$). Over a finite field $\mathbb{F}_{q^2}$, the exact same role is played by $\sigma(b) = b^q$.

**Orthogonality:** Once we have a form $B(x, y)$, setting $B(x, y) = 0$ implies $x$ and $y$ are orthogonal. Think of a dot product. This is very similar. 

**Reflexive Form:** A bilinear or sesquilinear form $f(x, y)$ where "orthogonality is a two-way street": $f(x, y) = 0 \iff f(y, x) = 0$.

**Isotropic Points:** Our polar spaces are going to be point sets where a point is orthogonal to itself as defined by a reflexive form. These are called isotropic points. This idea doesn't make much sense when we use the regular dot product formula of length (and for that matter, what is the length of a point anyway?). But we are not really thinking of length here. We are defining a form and using that to define orthogonality, which might arise due to, for example, minus signs in the form ($x_1y_1 - x_2y_2$) or due to the field being finite, in which case, as we saw in $\text{char} = 2$, a scalar multiple turns out to be $0$ modulo the characteristic. We'll come back to what isotropic points can tell us about a projective space in a bit.

Now let's build a mental model of polar spaces. We have as a background, a vector space or its projective space. We then filter points using a reflexive form that identifies which points are isotropic and which pairs of points are orthogonal i.e. a point $x$ can only "see" (be collinear with) a subset of other points $y$ that satisfy $B(x, y)=0$. 

Note that if a pair of isotropic points is orthogonal, then all pairs of points on the line formed by those points will also be orthogonal because the form $B$ is bilinear (or sesquilinear); it is linear (or semilinear) in its arguments.

If we have two isotropic points $\mathbf{x}$ and $\mathbf{y}$ such that they are orthogonal ($B(\mathbf{x}, \mathbf{y}) = 0$), any other point $\mathbf{p}$ on the projective line connecting them can be written as a linear combination $\mathbf{p} = \mathbf{x} + \alpha \mathbf{y}$ (ignoring the scaling factor on $\mathbf{x}$). Let's check if the whole line is orthogonal to $\mathbf{x}$:

$$B(\mathbf{x},\mathbf{p})=B(\mathbf{x},\mathbf{x}+\alpha \mathbf{y})=B(\mathbf{x},\mathbf{x})+\alpha B(\mathbf{x},\mathbf{y})$$

Since $\mathbf{x}$ is isotropic,  $B(\mathbf{x}, \mathbf{x}) = 0$. Since we chose $\mathbf{y}$ to be orthogonal to $\mathbf{x}$,  $B(\mathbf{x}, \mathbf{y}) = 0$. Therefore:

$$B(\mathbf{x},\mathbf{p})=0+\alpha(0)=0$$

By extension, if you pick any two points $\mathbf{p}_1 = \mathbf{x} + \alpha_1 \mathbf{y}$ and $\mathbf{p}_2 = \mathbf{x} + \alpha_2 \mathbf{y}$ on this line,  $B(\mathbf{p}_1, \mathbf{p}_2) = 0$ (requiring $\mathbf{y}$ to also be isotropic so that $B(\mathbf{y}, \mathbf{y}) = 0$). Thus, every single pair of points on that line is mutually orthogonal. 

We can then extend this to higher-dimensional subspaces as well. Such subspaces where all points are isotropic and all pairs of points are orthogonal are called totally isotropic subspaces. We then include all totally isotropic subspaces in our polar space and study how they are incident with each other. This is the whole game in polar spaces and their geometry.

Why do we care about isotropic points? In projective space $\text{PG}(n, \mathbb{F})$, a point is an equivalence class, a 1D subspace $\langle \mathbf{x} \rangle$, meaning $\mathbf{x}$ and $\lambda \mathbf{x}$ ($\lambda \neq 0$) represent the same projective point. If you try to evaluate the "length squared" $B(\mathbf{x}, \mathbf{x})$ of a projective point, scaling by $\lambda$ changes the value to $B(\lambda \mathbf{x}, \lambda \mathbf{x}) = \lambda^2 B(\mathbf{x}, \mathbf{x})$ (or $\lambda \overline{\lambda} B(\mathbf{x}, \mathbf{x})$). Thus, a non-zero value of $B(\mathbf{x}, \mathbf{x})$ is not well-defined on projective points.

Note that the condition $Q(x) = 0$ is completely independent of the choice of coordinate basis. Let $\mathcal{B} = (e_1, \dots, e_n)$ be a basis of $V$, giving coordinate vectors $[x]_{\mathcal{B}}$. In this basis, the quadratic form is represented by a symmetric (or upper-triangular) matrix $A$: $Q(x) = [x]_{\mathcal{B}}^T A [x]_{\mathcal{B}}$

If you choose another basis $\mathcal{B}'$, related by an invertible change-of-basis matrix $M \in \text{GL}(V)$ such that $[x]_{\mathcal{B}} = M [x]_{\mathcal{B}'}$, the Gram matrix transforms by congruence: $A' = M^T A M$

Evaluating the condition in the new basis yields:

$$[x]_{\mathcal{B}'}^T A' [x]_{\mathcal{B}'} = [x]_{\mathcal{B}'}^T (M^T A M) [x]_{\mathcal{B}'} = (M [x]_{\mathcal{B}'})^T A (M [x]_{\mathcal{B}'}) = [x]_{\mathcal{B}}^T A [x]_{\mathcal{B}} = Q(x)$$

The evaluated scalar is identically equal before and after the coordinate transformation. If it evaluated to zero in one basis, it evaluates to zero in every other basis.

---

**Aside:** When moving to characteristic 2, we also speak of  singular and totally singular forms. Given a quadratic form, a point $\langle \mathbf{x} \rangle$ is singular if $Q(\mathbf{x}) = 0$, and a subspace $U$ is totally singular if $Q(U) = 0$. (In $\text{char} = 2$, taking two singular points $\mathbf{x}, \mathbf{y}$ with $Q(\mathbf{x}) = Q(\mathbf{y}) = 0$ that are orthogonal under the polar form $B(\mathbf{x}, \mathbf{y}) = 0$ gives $Q(\mathbf{x} + \alpha \mathbf{y}) = Q(\mathbf{x}) + \alpha^2 Q(\mathbf{y}) + \alpha B(\mathbf{x}, \mathbf{y}) = 0$, making the whole line totally singular.) In standard algebra and incidence geometry (across all characteristics, not just characteristic 2), a singular point is one where the quadratic form equates to 0. Since the bilinear form is 0 for all points in char $=2$, we use the quadratic form and so the points are called singular, not isotropic. However, this is just a naming convention. The singular points are what would have been called isotropic points if the whole char $=2$ weirdness didn't exist. Note that these singular points are totally different from the radical of a quadric, which is also sometimes called a singular point (but of a quadric, not a quadratic set).

---

#### Polarity
**Polarity:** A global map defined on all points in $PG(d, K)$. Every point $P$ gets mapped to a hyperplane $P^\pi$ which contains all points orthogonal to $P$ (as defined by the polar form). Thus $P^\pi = \{ \langle y \rangle \in PG(d, K) \mid f(x, y) = 0 \}$. $P^\pi$ is called the polar hyperplane of $P$. It is a full hyperplane of the ambient projective space $PG(d, K)$.

Applying a polarity on a point will always give a hyperplane because $f(x, y) = 0$ is a linear equation in terms of $y$ i.e. when $x$ is fixed. As long as $x \neq 0$ and $f$ is non-degenerate, this linear equation always has a $(d)$-dimensional vector space of solution vectors $y$. In $PG(d, K)$, those solutions form a $(d-1)$-dimensional hyperplane.

If $P$ is not isotropic (which will see is only possible in orthogonal and unitary polar spaces and not in symplectic spaces), the hyperplane will not contain $P$, and will slice through the polar space. $P^\pi \cap \mathcal{Q}$ is given by the set of points $T \in \mathcal{Q}$ where lines from $P$ are tangent to $\mathcal{Q}$, forming a nondegenerate smaller polar space (of the same type as the original) inside $P^\pi$. We saw this in the quadrics section where we ended up with ellipses when we sliced a cone. 

If $P$ is isotropic, then $P$ lies directly on $P^\pi$, which means the hyperplane is tangent to the polar space at $P$. $P^\pi$ typically consists of a mix of isotropic and non-isotropic points. The plane will slice the polar space such that we have a radical at $P$. We end up with a degenerate polar space of the same time. We saw this too with the hyperboloid, where the point $P$ became a singular point because the two lines of the two regulus families meet there.

 Note that the synthetic geometry equivalent of the isotropic point is the absolute point i.e. a point $P$ such that $P \in P^\pi$. They are one and the same. Similarly a hyperplane $H$ is absolute if and only if $H^\pi \in H$ i.e. its assigned pole (the pointa polarity maps the hyperplane to) lies inside $H$.

To build a totally isotropic subspace, typically you start with an isotropic point $P$. To extend $P$ to a 1-dimensional totally isotropic subspace/line you pick another point $Q = \langle y \rangle \in P^\pi$ that is itself isotropic. As we saw, the line $\langle P, Q \rangle$ will be contained in $P^\pi$ and by the same logic of a line being a linear subspace, will be totally isotropic. Continue this process inside $P^\pi$ to build higher-dimensional totally isotropic subspaces.

Here's a concrete example: a sphere in $PG(3, \mathbb{R})$. Consider the quadratic form $f(x, y) = x_0 y_0 + x_1 y_1 + x_2 y_2 - x_3 y_3 = 0$ in $PG(3, \mathbb{R})$. The isotropic points form a sphere/cone: $x_0^2 + x_1^2 + x_2^2 - x_3^3 = 0$.

Let $P = \langle (0, 0, 1, 1) \rangle$. Check isotropy:  $0^2 + 0^2 + 1^2 - 1^2 = 0 \implies P$ is isotropic.
    
The polar hyperplane $P^\pi$ is given by $f((0,0,1,1), y) = 0 \implies y_2 - y_3 = 0$.
    
Now test points in $P^\pi$:

- $Q_1 = \langle (1, 0, 0, 0) \rangle$: Fits $y_2 - y_3 = 0$. But $f(Q_1, Q_1) = 1 \neq 0 \implies$ Non-isotropic point inside $P^\pi$.
        
- $Q_2 = \langle (1, 0, 1, 1) \rangle$: Fits $y_2 - y_3 = 0$, and $f(Q_2, Q_2) = 1^2 + 0^2 + 1^2 - 1^2 = 1 \neq 0 \implies$ Non-isotropic.
        
- $P = \langle (0, 0, 1, 1) \rangle$: Isotropic point inside $P^\pi$.

In this example,  $P^\pi$ is a 2D plane tangent to the sphere at $P$. The only isotropic point on that tangent plane is $P$ itself. All other points on the plane lie strictly outside the sphere and are non-isotropic. This is what you would expect from a sphere.

Note that a point lies on $\frac{q^d - 1}{q - 1}$ hyperplanes of the projective space. But the polarity will map the point to only one hyperplane i.e. the hyperplane tangent to the polar space at point $P$ (if $P$ is isotropic).

Also note that a general map between points and hyperplanes that reverses inclusion ($\langle x \rangle \subseteq \langle y \rangle \implies \langle y \rangle^\pi \subseteq \langle x \rangle^\pi$) is called a correlation (or duality). To be a polarity, a correlation must be an involution ($\pi^2 = \text{id}$). Without requiring $\pi^2 = \text{id}$, you would just have an arbitrary correlation, where taking the polar hyperplane of $P$, and then taking the pole of that hyperplane, might land you on a completely different point $Q \neq P$. We saw this happen with the Fano plane example for collineations some time ago.

The involutory property $(P^\pi)^\pi = P$ holds if and only if $f$ is reflexive: $f(x, y) = 0 \iff f(y, x) = 0$. Because $f$ is reflexive, if $Y \in P^\pi$ (meaning $f(x, y) = 0$), then $f(y, x) = 0$, which means $X \in Y^\pi$. This mutual orthogonality is what guarantees: $(P^\pi)^\pi = P$.

---

**Aside:** The polar hyperplanes of isotropic points are their tangent hyperplanes. What do the polar hyperplanes of non-isotropic points look like? There are two direct geometric ways to visualize this. Imagine the polar space $\mathcal{Q}$ is a solid sphere or planet floating in 3D space $PG(3, \mathbb{R})$, and $P$ is a point outside the sphere (say, the sun or a flashlight at $P$). If you shine light rays (straight lines) in all directions from $P$ toward the sphere $\mathcal{Q}$:
-   Some rays miss the sphere completely (passants).
-   Some rays pierce right through the sphere at two points (secants).
-   A glowing ring of boundary rays just graze the edge of the sphere at a single point (tangents)—this ring of grazing points is the horizon of the sphere as seen from the satellite $P$.

Now ask: Where do all those grazing points $T_1, T_2, T_3, \dots$ lie? Every single point $T$ where a ray from $P$ is tangent to $\mathcal{Q}$ lies on one flat hyperplane—and that flat hyperplane slicing through the sphere along the horizon ring is $P^\pi$.
  
```
                         . T_1 (Tangent touchpoint: P lies in T_1^pi, so T_1 lies in P^pi)
                      . ' |
                   . '    |
                . '     ( | )
       P *----.'-------(  |  )-------> Secant line (hits Q at A and B)
                ' .     ( | )
                   ' .    |   Quadric / Polar Space Q
                      ' . |
                         ' T_2 (Tangent touchpoint)
                          |
                        P^pi (The Polar Hyperplane of P: the flat plane
                              passing through all tangent touchpoints T_i)
```
Why does this happen mathematically? Remember the symmetry rule of a polarity ($\pi^2 = \text{id}$): $T \in P^\pi \iff P \in T^\pi$.

Look at what the right-hand side ($P \in T^\pi$) says when $T$ is an isotropic point on the quadric $\mathcal{Q}$. Since $T$ is on the quadric,  $T^\pi$ is the tangent hyperplane to the quadric at $T$. Saying $P \in T^\pi$ means the tangent hyperplane at $T$ passes through $P$—which means the line $P \vee T$ is tangent to the quadric at $T$. By $T \in P^\pi \iff P \in T^\pi$, the polar hyperplane $P^\pi$ cuts the quadric $\mathcal{Q}$ in the exact locus of points $T \in \mathcal{Q}$ whose tangent lines pass through $P$.

Since we spoke of the sun/planet analogy, the polar hyperplane is kind of like the day-night terminator on Earth. Think of the Sun as a point source of light. Now look at the day-night terminator, which is the slice of the polar hyperplane on the sphere (Earth). Since the sun is far off, the terminator covers nearly half the sphere, but if it was much closer (and still a point source), the terminator would be closer to the side of the Earth that is towards the Sun.

What if we push the point $P$ inside the Earth? You can no longer shine tangent lines from $P$ to the surface, yet the polar plane $P^\pi$ still exists—it now sits completely outside the Earth! Why? By the reciprocity rule ($Q \in P^\pi \iff P \in Q^\pi$), if $P$ is inside the Earth at distance $d < R$ from the center, its polar plane $P^\pi$ lies outside the Earth at distance $R^2 / d > R$. Every point $Q$ lying on that external plane $P^\pi$ is a satellite position whose day-night terminator plane $Q^\pi$ slices through the Earth right through our interior point $P$.

The other way to visualize this is a mirror reflection. What if we look at a secant line through $P$ that pierces the quadric at two points $A$ and $B$ (or what if $P$ is inside the sphere so there are no real tangent lines from $P$)? How does $P^\pi$ distinguish itself then?
  
Draw any secant line $\ell$ through $P$ that hits the quadric $\mathcal{Q}$ at two points $A$ and $B$, and passes through the hyperplane $P^\pi$ at a point $M = \ell \cap P^\pi$:
  
```
                        | P^pi (Polar Hyperplane)
                        |
      P *-------A-------M-------B------->  Secant line through P
                        |
```
Where on the segment $AB$ does the hyperplane $P^\pi$ cross the line?
  
-   If $P$ were infinitely far away,  $M$ would be the exact midpoint between $A$ and $B$.
-   In projective geometry, when $P$ is at a finite distance,  $M$ is the projective harmonic conjugate of $P$ with respect to the two quadric points $A$ and $B$ (meaning the cross-ratio $(P, M; A, B) = -1$).

In fact, this gives the cleanest geometric visualization of all: Every non-isotropic point $P$ defines a unique reflection collineation $\rho_P$ of the entire projective space that swaps the two intersection points $A \leftrightarrow B$ on every secant line through $P$ (leaving the quadric $\mathcal{Q}$ unchanged). As a central collineation of $PG(d, K)$:
  
-   The point $P$ is the Centre of the reflection $\rho_P$ (all points move along rays through $P$).
-   The polar hyperplane $P^\pi$ is the Axis of the reflection $\rho_P$ (the mirror wall that stays completely frozen pointwise while $A$ and $B$ swap across it).

Essentially, if you reflect the polar space $\mathcal{Q}$ across the hyperplane $P^\pi$ along rays radiating from $P$, the polar space $\mathcal{Q}$ maps onto itself ($A \leftrightarrow B$ on every ray through $P$). $P^\pi$ is the unique mirror hyperplane for which $P$ is the centre of reflection preserving $\mathcal{Q}$.

Using directed segments, the distances of these points becomes:
    
$$\frac{\overline{MA}\cdot \overline{PB}}{\overline{MB}\cdot \overline{PA}}=-1\implies \frac{\overline{MA}}{\overline{MB}}=-\frac{\overline{PA}}{\overline{PB}}$$
    
The negative sign here simply means that one of the points ($P$ or $M$) lies inside the segment $AB$, while the other lies outside it.
    
If we drop the signs and look strictly at the physical lengths (distances) of the segments, the negative sign disappears:
    
$$\frac{\vert{}MA\vert{}}{\vert{}MB\vert{}}=\frac{\vert{}PA\vert{}}{\vert{}PB\vert{}}$$
    
This tells us that $P$ and $M$ divide the segment $AB$ in the exact same ratio, one internally and one externally.

This cross-ratio $(A, B; M, P) = -1$ defines a harmonic quadruple (where $M$ and $P$ are harmonic conjugates with respect to $A$ and $B$). If you choose projective coordinates on the line $\text{PG}(1, \mathbb{F})$ so that $A = [1:0]$,  $B = [0:1]$, and $P = \mathbf{a} + \lambda \mathbf{b}$, then its harmonic conjugate is always the negative linear combination: $M = \mathbf{a} - \lambda \mathbf{b}$.

In a field of characteristic 2, something interesting happens. Algebraically, the cross-ratio condition $(A, B; M, P) = -1$ becomes $(A, B; M, P) = 1$, which simplifies to $M = P$. In terms of linear combinations,  $P = \mathbf{a} + \lambda \mathbf{b}$ and $M = \mathbf{a} - \lambda \mathbf{b}$ become the same projective point because $+\lambda = -\lambda$.

Geometrically, harmonic conjugacy degenerates: the two fixed points collapse into a single center (giving an elation instead of a homology), which is the 1D projective manifestation of the exact same characteristic-2 collapse you noted for symmetric bilinear forms.

--

**Generator (Maximal Totally Singular Subspace):** A totally singular subspace of the largest possible dimension inside a polar space. The number of nodes in the polar space diagram—its rank $n$, also called the Witt index $t$—is the vector space dimension of a generator, which has projective dimension $n - 1$. Note that in a $d$-dimensional projective space, the maximal isotropic subspace need NOT be of dimension $d-1$.

All maximal totally isotropic subspaces of a given non-degenerate polar form have the exact same dimension $r$. You can start with any totally isotropic subspace $W_k$ of dimension $k < r$ and extend it step-by-step until it reaches dimension $r$.

The union of all such maximal totally isotropic subspaces across the projective space will sweep out ("generate") the set of all isotropic points. The polar space is therefore the set of all these points along with every smaller isotropic subspace contained within them. This is why we refer to these maximal subspaces as generators. A good example to remember is the hyperboloid in 3D, which is generated by the straight lines that rule its surface.

A totally isotropic subspace $W$ is maximal if and only if:

$$W^\perp \cap \mathcal{Q} = W$$

In terms of incidence,  $W$ is maximal if no point outside $W$ is collinear to all of $W$.

To understand why this holds, first note that $W \subseteq W_\perp$ always, since $W$ consists of points that are orthogonal to each other. Thus, each point is orthogonal to all points of $W$. $W_\perp$  also consists of points orthogonal to all points of $W$, but it consists of *all* points that fulfill this criterion, which means it contains $W$.. Now let's look at the condition above. Let's say there is some point of the polar space that belongs to $W^\perp$ but not to $W$. Since this point belongs to $W^\perp$, it must be orthogonal to every point in $W$. Since it is a point of the polar space, it must be isotropic. Thus the new subspace of $W$ and this point is a totally isotropic subspace and since it has a point not in $W$ but includes all points in $W$, it must be of higher dimension than $W$, which contradicts $W$ being a maximal subspace. The statement of no point outside $W$ being collinear to all of $W$ is the same thing, since collinearity is just orthogonality algebraically.

$W^\perp$ is the intersection of the polar hyperplanes of all points in $W$, which means every point in $W^\perp$ is orthogonal to every point in $W$. See the aside below.

---

**Aside 1:** A polarity can also swap higher dimensional subspaces and not just points with their complements. If $U \subseteq PG(d, K)$ is a projective subspace of dimension $t$ (corresponding to a vector subspace $W \subseteq V$ of dimension $t + 1$), its polar image under $\pi$ is defined as the joint orthogonal complement of all points in $U$, or the intersection of the polar hyperplanes of all points $\in U$:

$$U^\pi = \bigcap_{P \in U} P^\pi = \{\langle y \rangle \in PG(d, K) \mid f(x, y) = 0 \text{ for all } \langle x \rangle \in U\}$$

Algebraically, $U^\pi$ corresponds to $W^\perp \subseteq V$. Since $f$ is non-degenerate:

$\dim(W^\perp) = (d + 1) - \dim(W) = (d + 1) - (t + 1) = d - t$ and translating back to projective dimensions: $\dim(U^\pi) = \dim(W^\perp) - 1 = d - 1 - t$. So a $t$-dimensional subspace is mapped to a subspace of codimension $t$.

**Aside 2:** Every point in $W^\perp$ is orthogonal to every point in $W$. This should remind you of error correction codes where codewords and parity checks are orthogonal. When applied to Reed-Muller codes and finite geometries, the polar space structure and incidence geometry emerge in several concrete ways:

**Codewords vs. Dual Code ($C$ vs. $C^\perp$)**

In a linear block code $C \subseteq \mathbb{F}_2^n$ every codeword $c \in C$ is orthogonal to every vector in the dual code $H \in C^\perp$ under the standard dot product: $c \cdot h = 0 \quad \text{for all } h \in C^\perp$.
    
For Reed-Muller codes $\mathrm{RM}(r, m)$ of length $n = 2^m$, the dual code is another Reed-Muller code: $\mathrm{RM}(r, m)^\perp = \mathrm{RM}(m - r - 1, m)$.
    
When $r = \frac{m - 1}{2}$ (for odd $m$), the code is self-dual ($C = C^\perp$), meaning every codeword is orthogonal to every other codeword—making $C$ a maximal totally isotropic subspace (a Lagrangian subspace) of $\mathbb{F}_2^n$ under the standard bilinear form.

**Incidence Geometry of First-Order Codes $\mathrm{RM}(1, m)$**

The connection to projective and affine polar spaces becomes direct when viewing codewords as geometric incidence vectors. In $\mathrm{RM}(1, m)$, the codewords correspond to affine functions over $\mathbb{F}_2^m$, which are characteristic vectors of affine hyperplanes and their complements. 

The minimum weight codewords correspond to affine hyperplanes.

In projective terms, extended Reed-Muller codes and projective Reed-Muller codes embed directly into $\mathrm{PG}(m, 2)$. The syndrome equations used in majority-logic decoding are intersections of secant lines and hyperplanes, mimicking how points outside a polar space are tested against polar hyperplanes to locate errors.

**Quadratic Forms and the Kerdock / Preparata Codes**

The exact quadratic/polar machinery ($Q(x)$, symplectic forms, and isotropic subspaces) appears directly when analyzing second-order Reed-Muller codes $\mathrm{RM}(2, m)$. Any codeword in $\mathrm{RM}(2, m)$ can be viewed as a Boolean quadratic function $q(x_1, \dots, x_m)$. Associated with $q(x)$ is a symplectic bilinear form (polar form):

$$B_q(x, y) = q(x + y) + q(x) + q(y) + q(0)$$
    
The radical of this alternating form,  $\mathrm{rad}(B_q) = \{ x \mid B_q(x, y) = 0 \text{ for all } y \}$, defines the invariant subspace where the quadratic function degenerates.

The weight (number of ones) of the codeword corresponds to whether the quadric $q(x) = 0$ is hyperbolic, elliptic, or parabolic, giving Dickson's invariant classification of codewords via Witt index.

Non-linear codes with optimal error-correcting properties (like the Kerdock code) are formed by partitioning the set of all symplectic forms on $\mathbb{F}_2^m$ into maximal isotropic sets (spreads and packings of polar spaces).

---

The polar form and the polarity are two sides of the same coin (the algebraic vs synthetic coin). Solving $f(x,x) = 0$ is the algebraic approach, while building via generators/polar planes is the incidence-geometric (synthetic) approach.

In the algebraic approach, you set up the quadratic/Hermitian equation $f(x, x) = 0$ in coordinates: $\sum_{i,j} a_{ij} x_i x_j = 0$. You get the set of point coordinates that satisfy the equation (the quadric / locus of absolute points). But this has a limitation. Knowing the algebraic locus of points alone doesn't immediately reveal the internal geometric structure—such as what flat linear subspaces (lines, planes, etc.) lie entirely inside the surface, or how those subspaces intersect one another.

In the synthetic or incidence approach of generators and polarities, we use the polarity map $P \mapsto P^\pi$ to systematically identify which subspaces are orthogonal to themselves ($W \subseteq W^\perp$). This gives us the full lattice of linear subspaces contained in the polar space, classified by their dimensions and intersection properties.
    
This matters because in axiomatic and finite geometry, polar spaces are often defined without coordinates at all (e.g., via the Buekenhout-Shult axioms). In that framework, there is no algebra or coordinate system to "solve"—the polar space is defined purely synthetically as a set of points and family of generator subspaces satisfying geometric incidence rules.

So very roughly speaking, a polar form is a fancy way of writing out the equation of some degree 2 curved surface (or hypersurface) inside a vector or projective space. If the dimension of the projective space is $d \ge 3$, this curved surface can be studied purely by geometric axioms as well.

_**Generalized Quadrangle (`o === o`):** A rank 2 point-line geometry that has no triangles, and satisfies the "One-or-All" axiom: given any line $\ell$ and any point $P \notin \ell$, there is at most $1$ point on $\ell$ collinear with $P$ (in fact, for a generalized quadrangle, there is always a unique point $Q \in \ell$ and a unique line $P \vee Q$ connecting $P$ to $\ell$). A simple square is a thin generalized quadrangle ($2$ points per line, $2$ lines per point). A hyperbolic quadric $Q^+(3, q)$ in $PG(3, q)$ (two reguli of $q+1$ lines each) is a grid generalized quadrangle ($q+1$ points per line, $2$ lines per point)._

### One-or-All Axiom

We showed why if two isotropic points are orthogonal, all pairs of points on the line formed by them will also be orthogonal. This sets up the stage for the famous One-or-All axiom (called the Buekenhout-Shult axiom) of abstract polar spaces.

Note that this axiom is from the stable of synthetic geometry. It is formulated purely as an incidence structure $(\mathcal{P}, \mathcal{L})$ without referencing coordinates, matrices, or forms. We do not have a concept of orthogonality yet because that requires the definition of a form algebraically. Thus, two points $p, q \in \mathcal{P}$ are defined to be collinear (often written $p \sim q$ or $p \perp q$) if there exists a line $m \in \mathcal{L}$ (the line set) of the polar space containing both $p$ and $q$. By convention, every point is also considered collinear to itself. Also, a line belongs to the line set of the polar space only if every point of the line lies in the polar space. When we look at this through an algebraic lens, since a line is totally isotropic, any pair of points on the line are orthogonal. Thus two points being collinear is the same as them being orthogonal. 

Now for the axiom: Given a point $p$ and a line $L$ of the polar space (meaning $p$ is isotropic and $L$ is a totally isotropic line), either $p$ is collinear (we could also say orthogonal) to every point on $L$ (so $p$ and $L$ span a totally isotropic plane) or $p$ is collinear with exactly one point on $L$ (i.e. $L$ intersects the tangent hyperplane at a single point, which itself lies on the polar space).

This single rule—the "One-or-All Axiom"—is the defining incidence axiom of a Polar Space.

#### Example: Hyperboloid in 3D Space
The ambient space $PG(3, K)$ has lots of points, lines, and planes. Now [restrict your attention](https://www.researchgate.net/profile/Ricardo-Uribe-Vargas/publication/341213554/figure/fig2/AS:888541198438401@1588856138343/A-one-sheet-hyperboloid.png) ONLY to the points $P$ that lie on the surface $Q$, and the straight lines $\ell$ that lie completely flat inside the surface $Q$. Notice what happens to the projective geometry axioms when we restrict to points and lines inside $Q$:

* In all of $PG(3, K)$, any two points have a line joining them.
* Inside $Q$, two points on the surface might NOT have a line of $Q$ joining them (because the line through them in $PG(3, K)$ pokes outside the surface).
* Instead, if you pick any line $\ell$ lying on the surface $Q$ and any point $P$ on $Q$ (not on $\ell$), how many lines of $Q$ pass through $P$ and intersect $\ell$? Exactly one, a line of the opposite regulus.

```
         P  (Point on the polar space, outside line L)
        /|\
       / | \
      /  |  \   <-- Out of all points on line L, either:
     /   |   \      (1) P is joined by a line of the polar space
    /    |    \         to AT MOST ONE point Q on L, OR
   *-----Q-----*    (2) P is joined to EVERY point on L.
  Line L (lying inside the polar space)

```

#### Example: Klein Quadric $\mathcal{Q}^+(5, K)$ in $\mathrm{PG}(5, K)$
When can $P$ be collinear with all of $\ell$? This happens only in polar spaces of rank $\ge 3$, which require ambient projective space of dimension at least 4 or 5. For example, on the Klein quadric $\mathcal{Q}^+(5, K)$ in $\mathrm{PG}(5, K)$, maximal generators are projective planes. Entire planes are embedded in the quadric. Pick a line $\ell$ and a point $P \notin \ell$ that both lie inside the same totally isotropic plane. Then $P$ is collinear to every point on $\ell$.

Note that when the set of isotropic points contains no lines—such as an elliptic quadric (a sphere or ellipsoid) $\mathcal{Q}^-(3, \mathbb{F})$ or an abstract ovoid $\mathcal{O}$ in $\mathrm{PG}(3, \mathbb{F})$—the Buekenhout-Shult axiom holds vacuously.

#### Generating The Whole Polar Space
How do we build up from this axiom about points and lines to get an entire polar space? Because we can build successively higher subspaces. In a polar space, we define a "subspace" $U$ to be any set of points such that whenever two points $X, Y$ are in $U$, they are joined by a line $X \vee Y$ of the polar space and that entire line lies inside $U$. 

Suppose we take a line $\ell$ and a point $P \notin \ell$. Assume that the "All" case holds (every line joining $P$ to a point of $\ell$ is in the polar space). Then the union of all those lines joining $P$ to $\ell$ forms a 2D plane $\Pi = P \vee \ell$ inside the polar space. Since $P$ and $\ell$ (and therefore the intersection of the line joining $P$ to $\ell$) lie in the plane, once again, every point on every one of these connecting lines is pairwise orthogonal and isotropic. Since the plane is spanned by these lines, every point on the line is isotropic and pairwise orthogonal. So we have a totally isotropic plane. 

We can also show this synthetically via the Veblen–Young theorem. In short, if you take any two lines $\ell_1, \ell_2$ inside $\Pi$ and pick a point $X \in \ell_1$, the Buekenhout-Shult axiom says $X$ must be joined to at least one point of $\ell_2$, which forces $\ell_1$ and $\ell_2$ to intersect inside $\Pi$. Since the Veblen–Young theorem holds for this plane, every plane inside a polar space is an ordinary Projective Plane $PG(2, K)$.

Note that we made an assumption that $P$ is collinear with all points of $\ell$. It is possible that that assumption does not hold and the specific subspace spanned by $p$ and $\ell$ is not isotropic. But the line $\ell$ itself may still be capable of growing into a larger totally isotropic subspace by choosing a different point.

### The Rank of a Polar Space
In Tits' classification, the rank of a polar space is the projective dimension of its maximal totally isotropic subspaces plus 1, which is the vector dimension of a maximal totally isotropic subspace. 

A hyperbolic quadric $\mathcal{Q}^+(3, \mathbb{F})$ contains lines (1-dimensional projective subspaces or vector dimension 2). This is a polar space of rank 2 (a generalized quadrangle).

Similarly, the Klein quadric has entire planes embedded in it, and the polar space rank is 3.
    
An elliptic quadric $\mathcal{Q}^-(3, \mathbb{F})$ (sphere / ovoid) contains points (0-dimensional projective subspaces) but no lines. The underlying anisotropic or defect form allows maximal totally isotropic subspaces of vector dimension only 1. Therefore, a sphere or ovoid is a degenerate/trivial polar space of rank 1.

Because rank 1 structures are just sets of points with an empty line set, the main theorems of polar space theory explicitly add non-triviality conditions to rule them out.

The rank is the geometric generalization of the algebraic Witt index to the language of incidence geometry and buildings. The Witt index is the algebraic invariant measured in the vector space, while the rank is the geometric and combinatorial invariant measured in the projective lattice and the building.

### 3 Types of Polar Spaces
    
A theorem by Birkhoff and von Neumann proves that there are only three ways a form $f(x, y)$ can satisfy $f(x, y) = 0 \iff f(y, x) = 0$ i.e. there are only three types of reflexive forms:
    
**Symmetric / Orthogonal (field automorphism $\sigma = \text{id}$, making this a bilinear form):** $f(x, y) = f(y, x)$. (Example: $x_0 y_0 + x_1 y_1 - x_2 y_2$). The matrices preserving this form make up the Orthogonal Group (which includes both rotations and reflections). These form our nondegenerate quadrics.

You will see $\mathcal{Q}^+(2n-1, q)$,  $\mathcal{Q}(2n, q)$, and $\mathcal{Q}^-(2n-1, q)$ representing their geometric shapes: hyperbolic, parabolic, and elliptic.
        
**Alternating / Symplectic ($\sigma = \text{id}$):** $f(x, y) = -f(y, x)$ and so $f(x, x) = 0$ for every vector $x$. Because $f(x, x) = 0$ always, every single vector in the vector space (and therefore point in the projective space) is orthogonal to itself. In two variables, it is the 2D determinant (signed area): $f(x, y) = x_0 y_1 - x_1 y_0$. In physics (Hamiltonian mechanics and optics), this measures phase-space area (position $\times$ momentum). The matrices preserving a symplectic form make up the Symplectic Group.
        
**Hermitian / Unitary ($\sigma \neq \text{id}$ with $\sigma^2 = \text{id}$):** $f(y, x) = \sigma(f(x, y))$. An example is conjugation over $\mathbb{C}$: $x_0 \bar{y}_0 + x_1 \bar{y}_1$; or over $\mathbb{F}_{q^2}$: $x_0 y_0^q + x_1 y_1^q$. The matrices preserving a Hermitian form make up the Unitary Group.

Since we already looked at quadrics, let's look at the other two.

### Symplectic Spaces & Antisymmetric Bilinear Forms
#### Difference From a Quadric
Since $B(x, x) = 0$ for all points, every point in the entire projective space is isotropic. This is a key difference from quadrics where most points in the projective space are not in the polar space/quadric. In a symplectic space, the point set is the entire projective space.

#### Notation
Such spaces are denoted by $\mathcal{W}_{2n-1}(q)$ where:

-   $2n-1$: The dimension of the projective space $\text{PG}(2n-1, q)$ it lives in. Non-degenerate alternating forms can only exist in even-dimensional vector spaces, which correspond to odd-dimensional projective spaces.
    
-   $q$: The polar space is defined over the finite field $\mathbb{F}_{q}$.

#### Other Properties
Field Constraint: None! A symplectic space can be constructed over ANY commutative field $K$ (finite or infinite, characteristic $2$ or $\neq 2$). However, it cannot exist over a strictly non-commutative skew field, because alternating forms $f(x, x) = 0$ force the underlying ring to be commutative in order for $f$ to be reflexive. Commutativity is implied by the alternating form because:

Pull out $\alpha$ first:

$$B(\alpha \mathbf{x}, \beta \mathbf{y}) = -B(\beta \mathbf{y}, \alpha \mathbf{x}) = -\beta B(\mathbf{y}, \alpha \mathbf{x}) = -\beta \big(\alpha B(\mathbf{y}, \mathbf{x})\big) = -\beta \alpha \big(-B(\mathbf{x}, \mathbf{y})\big) = (\beta \alpha) B(\mathbf{x}, \mathbf{y})$$

Pull out $\beta$ first (or use the alternating property $B(\mathbf{u}, \mathbf{v}) = -B(\mathbf{v}, \mathbf{u})$):

$$B(\alpha \mathbf{x}, \beta \mathbf{y}) = -B(\beta \mathbf{y}, \alpha \mathbf{x}) = -\beta B(\mathbf{y}, \alpha \mathbf{x}) = -\beta \big(\alpha B(\mathbf{y}, \mathbf{x})\big) = -\beta \alpha \big(-B(\mathbf{x}, \mathbf{y})\big) = (\beta \alpha) B(\mathbf{x}, \mathbf{y})$$

Set the two equal to see that commutativity is forced.

Dimension Constraint: The vector space dimension $d+1$ MUST be even ($d+1 = 2n$), which means the ambient projective dimension $d = 2n - 1$ MUST be odd ($PG(1, K), PG(3, K), PG(5, K), \dots$).

Why? Because a skew-symmetric matrix $M^T = -M$ of odd size $(2n+1) \times (2n+1)$ always has determinant $0$, so it is always degenerate (there is at least one point orthogonal to the entire space).

Witt Index & Uniqueness: Up to a change of basis, there is only one non-degenerate symplectic form in dimension $2n$, with canonical equation:

$$(x_0 y_1 - x_1 y_0) + (x_2 y_3 - x_3 y_2) + \dots + (x_{2n-2} y_{2n-1} - x_{2n-1} y_{2n-2}) = 0$$

Therefore, its Witt index is always the maximum possible value: $r = n = \frac{d+1}{2}$ regardless of what field $K$ you use (even over $\mathbb{R}$, where $x^2 + y^2 = 0$ has no solutions, $x_0 y_1 - x_1 y_0 = 0$ still has Witt index $n$).

Special Geometric Property (All Points Are Absolute): Because $f(x, x) = 0$ for every vector $x \in V$, EVERY point of the ambient projective space $PG(2n-1, K)$ is a point of the symplectic polar space $W(2n-1, K)$.

Geometrically, every point $P$ lies inside its own polar hyperplane ($P \in P^\pi$). What makes $W(2n-1, K)$ a non-trivial polar space is that NOT every line of $PG(2n-1, K)$ is a line of $W(2n-1, K)$: through any point $P$, only the lines lying inside the hyperplane $P^\pi$ belong to the polar space.

### Unitary (Hermitian) Spaces $\mathcal{H}(n, q^2)$
#### The Field Automorphism
A Hermitian sesquilinear form satisfies:

$$B(\mathbf{x},\mathbf{y})=\sigma(B(\mathbf{y},\mathbf{x}))$$

$$B(\alpha \mathbf{x},\beta \mathbf{y})=\alpha \sigma(\beta)B(\mathbf{x},\mathbf{y})$$

The specific constraint on $\sigma$:  $\sigma$ must be a field automorphism, and specifically one of order 2 (meaning $\sigma(\sigma(k)) = k$, with $\sigma \neq \text{id}$). Think of $\sigma$ exactly like complex conjugation ($z \mapsto \bar{z}$). 

In finite fields, a field $\mathbb{F}_{q^{2}}$ has a natural, unique automorphism of order 2 given by:

$$\sigma(k)=k^{q}$$

$\sigma(k) = k^q$ is a power of the Frobenius automorphism. To be precise, the fundamental Frobenius map is $x \mapsto x^p$ (where $p$ is the prime characteristic of the field). When working in the field $\mathbb{F}_{q^{2}}$ (where $q = p^m$), applying that base map $m$ times gives $\sigma(k) = k^q$, which acts as the unique generator of the Galois group $\text{Gal}(\mathbb{F}_{q^2} / \mathbb{F}_q)$.

Are there other order-2 field automorphisms? In the world of finite fields, the answer is a strict no. Galois theory dictates that the Galois group of any finite field extension is cyclic. For a finite field $\mathbb{F}_{Q}$ to possess an order-2 automorphism, its absolute Galois group $\text{Gal}(\mathbb{F}_Q / \mathbb{F}_p)$ must have an element of order 2. Since $\text{Gal}(\mathbb{F}_{p^d} / \mathbb{F}_p) \cong \mathbb{Z}_d$, this is only mathematically possible if the extension degree $d$ is even ($d = 2m$), which means the field's size is a perfect square ($Q = p^{2m} = q^2$). In that specific case,  $\sigma(k) = k^q$ is the one and only automorphism of order 2.
    
If we step outside finite fields into infinite fields, we can have order-2 automorphisms without being restricted to a square field size. The classic order-2 automorphism is complex conjugation ($z \mapsto \bar{z}$). Here, the fixed subfield is the Real numbers ($\mathbb{R}$), and the characteristic is $0$. Over the rational numbers, the map $a + b\sqrt{2} \mapsto a - b\sqrt{2}$ is an order-2 automorphism. It referred to as adjoining the square root ($\mathbb{Q}(\sqrt{2})$).

If classical polar spaces were only defined over finite fields, we would always be stuck with $\mathbb{F}_{q^{2}}$ for Unitary spaces. But because they are defined over arbitrary fields, a Unitary (Hermitian) polar space can be constructed over any field that possesses an order-2 automorphism (making it a quadratic Galois extension of its fixed subfield), using its corresponding involution map.

#### Difference From a Quadric

For a quadric, a line meets it in $0, 1, 2$, or all points. For a Hermitian variety over $\mathbb{F}_{q^{2}}$, a line meets the variety in $1$,  $q + 1$, or all ($q^2 + 1$) points ( specifically, a secant line meets the variety in $q+1$ points, a tangent line meets it in $1$ point, and a totally isotropic line lies entirely inside it). It creates a highly rigid, beautiful combinatorial structure. Note that this means a non-degenerate Hermitian variety $H(d, q^2)$ has no passant (exterior) lines at all.
    
#### Notation
These spaces are denoted by $\mathcal{H}(n, q^2)$ where:

-   $\mathcal{H}$: Stands for Hermitian.
    
-   $n$: The dimension of the projective space $\text{PG}(n, q^2)$ it lives in. Unlike symplectic spaces, non-degenerate Hermitian spaces can exist in both even and odd projective dimensions.
    
-   $q^{2}$: The underlying finite field must be a quadratic extension (its size must be a perfect square, like $\mathbb{F}_4, \mathbb{F}_9, \mathbb{F}_{25}$) because you absolutely need that order-2 field automorphism $\sigma(k) = k^q$ to define the Hermitian property.

#### Other Properties

Field Constraint (Requires a Field Involution $\sigma$ of Order 2): Unlike symplectic spaces or quadrics, you CANNOT build a unitary polar space over just any field! The field $K$ must possess an automorphism $\sigma \neq \text{id}$ of order $2$ ($\sigma(\sigma(k)) = k$).

Over finite fields: $K$ must be a field of square order $\mathbb{F}_{q^2}$ (like $\mathbb{F}_4, \mathbb{F}_9, \mathbb{F}_{16}, \mathbb{F}_{25}$), where the unique involution is $\sigma(k) = k^q$. You cannot build a unitary space over $\mathbb{F}_2, \mathbb{F}_3, \mathbb{F}_5, \mathbb{F}_7,$ or $\mathbb{F}_8$!

Over infinite fields: Examples include $\mathbb{C}$ (with $\sigma(z) = \bar{z}$, fixing $\mathbb{R}$) or the quaternions $\mathbb{H}$ (with quaternion conjugation).

Dimension Constraint: None. Both even and odd vector space dimensions $d+1$ are completely valid ($PG(2, q^2), PG(3, q^2), PG(4, q^2), \dots$ all work).

Witt Index (Depends on the Field $K$): Over a finite field $K = \mathbb{F}_{q^2}$: Just like in the symplectic case, there is ONLY ONE non-degenerate Hermitian form in each dimension up to change of basis! In diagonal form it is:

$$x_0^{q+1} + x_1^{q+1} + \dots + x_d^{q+1} = 0$$

and in hyperbolic form it always splits completely, giving the maximum possible Witt index:

$$r = \left\lfloor \frac{d+1}{2} \right\rfloor$$

So for $d+1 = 2n$, $r = n$; for $d+1 = 2n+1$, $r = n$.

Over $\mathbb{C}$ (with $\sigma(z) = \bar{z}$): By Sylvester's Law of Inertia, the form has $p$ plus signs and $m$ minus signs ($z_0 \bar{z}_0 + \dots - z_d \bar{z}_d = 0$), and the Witt index can be any integer $r = \min(p, m)$ from $0$ up to $\lfloor (d+1)/2 \rfloor$.

Special Geometric Property (Line Secants Have $q+1$ Points): In $PG(d, q^2)$, every line of the ambient space has $q^2 + 1$ points. If a line of $PG(d, q^2)$ does not lie completely inside the Hermitian variety $H(d, q^2)$ and is not tangent ($1$ point), it intersects $H(d, q^2)$ in a subline $PG(1, q)$ of exactly $q + 1$ points (called a Baer subline).

### Orthogonal Polar Spaces / Non-Degenerate Quadrics $\mathcal{Q}$

We'll only look at the other properties here because everything else has been covered elsewhere. 

#### Other Properties

Field Constraint: None! Quadrics exist over any commutative field $K$. (However, as we saw earlier, characteristic $2$ behaves slightly differently from characteristic $\neq 2$ because the associated bilinear form $f(x, y) = Q(x+y) - Q(x) - Q(y)$ is alternating in characteristic $2$.)

Dimension & Witt Index Constraints: Unlike symplectic and finite unitary spaces (where each dimension has only one space), the Witt index $r$ of a quadric depends heavily on both the parity of $d+1$ and the arithmetic of the field $K$.

Over a Finite Field $\mathbb{F}_q$ (Chevalley-Warning Theorem), any quadratic form in $3$ or more variables over $\mathbb{F}_q$ ALWAYS has a non-zero zero ($Q(x) = 0$). This forces the anisotropic core $V_{\text{aniso}}$ to have dimension at most $2$, which leaves exactly 3 possibilities depending on whether $d+1$ is even or odd:

1. Hyperbolic Quadric $Q^+(2n-1, q)$ in odd projective dimension $d = 2n-1$ (even vector dimension $2n$):
Canonical equation: $x_0 x_1 + x_2 x_3 + \dots + x_{2n-2} x_{2n-1} = 0$.
Anisotropic core has dimension $0$. Witt index is $r = n$.
2. Parabolic Quadric $Q(2n, q)$ in even projective dimension $d = 2n$ (odd vector dimension $2n+1$):
Canonical equation: $x_0 x_1 + \dots + x_{2n-2} x_{2n-1} + x_{2n}^2 = 0$.
Anisotropic core has dimension $1$ ($x_{2n}^2$). Witt index is $r = n$.
*(Note in characteristic $2$: When $q = 2^h$, the polar bilinear form $f(x, y)$ of $Q(2n, q)$ has a 1-dimensional radical $N = \langle (0, \dots, 0, 1) \rangle$ called the nucleus of the quadric, where all tangent hyperplanes intersect. Quotienting out the nucleus gives an isomorphism between the polar space $Q(2n, 2^h)$ and the symplectic space $W(2n-1, 2^h)$)*
3. Elliptic Quadric $Q^-(2n+1, q)$ in odd projective dimension $d = 2n+1$ (even vector dimension $2n+2$):
Canonical equation: $x_0 x_1 + \dots + x_{2n-2} x_{2n-1} + (x_{2n}^2 + a x_{2n} x_{2n+1} + b x_{2n+1}^2) = 0$ (where $t^2 + at + b$ is irreducible over $\mathbb{F}_q$).
Anisotropic core has dimension $2$. Witt index is $r = n$.

Over General Infinite Fields (like $\mathbb{R}$ or $\mathbb{Q}$): The Witt index $r$ can be ANY integer from $0$ up to $\lfloor (d+1)/2 \rfloor$ (for instance, the sphere $x_0^2 + x_1^2 + x_2^2 - x_3^2 = 0$ over $\mathbb{R}$ has Witt index $r = 1$, whereas $x_0^2 + x_1^2 + x_2^2 + x_3^2 = 0$ has Witt index $r = 0$).

### Comparison: Finite Classical Polar Spaces (Over $\mathbb{F}_q$ or $\mathbb{F}_{q^2}$)

In finite geometry, a finite polar space of rank $r$ (Witt index $r$) has two numerical parameters $(s, t_{\text{line}})$ that control all counting formulas:

* Every line has $s + 1$ points (where $s$ is the size of the field: $q$ or $q^2$).
* Every sub-generator of projective dimension $r - 2$ is contained in $q^e + 1$ maximal generators of projective dimension $r - 1$. That exponent $e$ (which sits on the last node of the $C_r$ diagram) is the single number that distinguishes all 5 finite classical polar spaces of the same rank $r$:

| Polar Space Family | Ambient Space | Vector Dim $d+1$ | Field Needed | Witt Index (Rank $r$) | Parameter $e$ (Generators per $(r-2)$-subspace: $q^e + 1$) |
| --- | --- | --- | --- | --- | --- |
| Hyperbolic Quadric $Q^+(2n-1, q)$ | $PG(2n-1, q)$ | $2n$ (Even) | Any $\mathbb{F}_q$ | $r = n$ | $e = 0$ ($q^0 + 1 = 2$ generators; gives thin $D_n$ branching!) |
| Symplectic Space $W(2n-1, q)$ | $PG(2n-1, q)$ | $2n$ (Even) | Any $\mathbb{F}_q$ | $r = n$ | $e = 1$ ($q + 1$ generators) |
| Parabolic Quadric $Q(2n, q)$ | $PG(2n, q)$ | $2n+1$ (Odd) | Any $\mathbb{F}_q$ | $r = n$ | $e = 1$ ($q + 1$ generators) |
| Elliptic Quadric $Q^-(2n+1, q)$ | $PG(2n+1, q)$ | $2n+2$ (Even) | Any $\mathbb{F}_q$ | $r = n$ | $e = 2$ ($q^2 + 1$ generators) |
| Hermitian Space $H(2n-1, q^2)$ | $PG(2n-1, q^2)$ | $2n$ (Even) | Square $\mathbb{F}_{q^2}$ | $r = n$ | $e = 1/2$ in base $q^2$, so $(q^2)^{1/2} + 1 = q + 1$ generators |
| Hermitian Space $H(2n, q^2)$ | $PG(2n, q^2)$ | $2n+1$ (Odd) | Square $\mathbb{F}_{q^2}$ | $r = n$ | $e = 3/2$ in base $q^2$, so $(q^2)^{3/2} + 1 = q^3 + 1$ generators |

Look at that last column: for a fixed rank $r = n$, all six classical polar spaces share the exact same diagram $C_n$ (`o --- o --- ... --- o === o`), and the only difference between them is how thick the Generalized Quadrangle `o === o` is at the right-hand end of the diagram ($2, q+1, q^2+1,$ or $q^3+1$ generators meeting at each $(n-2)$-subspace).

Now let's look at the formulas for some counts in these polar spaces. 

#### Index or Rank
Let $d$ be the projective dimension of the ambient space $\text{PG}(d, \mathbb{F})$, so the underlying vector space $V$ has vector dimension $N = d + 1$. Let $r$ denote the Witt index (polar rank), which is the vector dimension of a maximal totally isotropic (or totally singular) subspace $U$ (so its projective dimension inside $\text{PG}(d, \mathbb{F})$ is $r - 1$).

As we saw, always, for any non-degenerate reflexive form on a vector space of dimension $N$, a totally isotropic subspace $U$ satisfies $U \subseteq U^\perp$, and by non-degeneracy $\dim(U) + \dim(U^\perp) = N$. Therefore the Witt index $r$ in terms of the projective dimension $d$ and vector space dimension $N = d + 1$ is given by:

$$2r \le N = d + 1 \implies r \le \left\lfloor \frac{d+1}{2} \right\rfloor$$
    
For quadrics in finite fields, we saw $r = \frac{d}{2}$ for even $d$, and $r = \frac{d+1}{2}$ or $\frac{d-1}{2}$ for odd $d$. What happens in the other two finite field polar spaces (Symplectic and Unitary)? Over arbitrary fields (like $\mathbb{R}$ or $\mathbb{Q}$), we can give away the answer right now. These formulas break down completely for all polar spaces, so we won't spend any time on these fields. 

First, recall that by Witt's Decomposition Theorem, any vector space $V$ with a non-degenerate reflexive form can be decomposed into an orthogonal direct sum of $r$ hyperbolic planes  $\mathbb{H}$ (each of vector dimension $2$, given by $x_1 y_2 + x_2 y_1$, which contributes $1$ to the Witt index $r$) plus an anisotropic kernel  $V_0$ (a subspace containing zero isotropic vectors).

$$V = \underbrace{\mathbb{H} \perp \mathbb{H} \perp \dots \perp \mathbb{H}}_{r \text{ copies}} \perp V_0$$

Therefore, the vector dimension $N = d+1$ is always:
  
$$d + 1 = 2r + \dim(V_0) \implies r = \frac{d + 1 - \dim(V_0)}{2}$$

Over a finite field $\mathbb{F}_q$ (or $\mathbb{F}_{q^2}$ for Unitary), the Chevalley–Warning Theorem guarantees that any anisotropic part of the space (what is left over after we strip away all nondegenerate components via Witt decomposition) has vector dimension at most $2$ (for orthogonal) or $1$ (for unitary). 

In Symplectic ($\mathcal{W}$) space, every vector satisfies $B(\mathbf{x}, \mathbf{x}) = 0$, so an anisotropic subspace cannot exist ($\dim(V_0) = 0$ always). Thus $d+1 = 2r \implies r = \frac{d+1}{2}$ (and $d$ must be odd).

For Unitary ($\mathcal{H}$ over $\mathbb{F}_{q^2}$) spaces, take two variables in $V_0$:  $x_1^{q+1} + x_2^{q+1} = 0 \implies (x_1/x_2)^{q+1} = -1$. Because the norm map $z \mapsto z^{q+1}$ from $\mathbb{F}_{q^2}^\times \to \mathbb{F}_q^\times$ is surjective, there is always a non-zero solution in 2 variables. Thus, a 2D unitary space over $\mathbb{F}_{q^2}$ is never anisotropic ($\dim(V_0)$ can only be $0$ for odd $d$, or $1$ for even $d$). That gives $r = \frac{d+1}{2}$ (odd $d$) and $r = \frac{d}{2}$ (even $d$).

In Orthogonal ($\mathcal{Q}$ over $\mathbb{F}_q$) space, over 2 variables, a quadratic form $x_1^2 + a x_1 x_2 + b x_2^2 = 0$ can be an irreducible quadratic polynomial over $\mathbb{F}_q$ (with no roots in $\mathbb{F}_q$). That gives a 2-dimensional anisotropic kernel ($\dim(V_0) = 2$). By Chevalley–Warning, a quadratic form in $3$ variables ($x_1^2 + x_2^2 + x_3^2 = 0$) always has a non-trivial root over $\mathbb{F}_q$, so $\dim(V_0)$ can never be $3$ or higher.

For even $d$ ($N$ odd):  $\dim(V_0)$ must be odd, so $\dim(V_0) = 1 \implies r = \frac{d}{2}$. For odd $d$ ($N$ even):  $\dim(V_0)$ must be even, so either $\dim(V_0) = 0 \implies r = \frac{d+1}{2}$ (Hyperbolic $\mathcal{Q}^+$) or $\dim(V_0) = 2 \implies r = \frac{d-1}{2}$ (Elliptic $\mathcal{Q}^-$).

Thus,  Symplectic and Unitary spaces do not have the plus/minus split in odd projective dimension. Instead, they always hit the theoretical maximum $r = \lfloor \frac{d+1}{2} \rfloor$.
  
So for even projective dimension, Orthogonal $\mathcal{Q}(d, q)$ and Unitary $\mathcal{H}(d, q^2)$ obey the exact same rule:  $r = \frac{d}{2}$. Symplectic $\mathcal{W}(d, q)$ cannot exist as a non-degenerate polar space when $d$ is even, because an alternating matrix of odd vector size $N = d+1$ always has determinant $0$.

In odd projective dimension, we know that orthogonal splits into two types: Hyperbolic ($r = \frac{d+1}{2}$) and Elliptic ($r = \frac{d-1}{2}$). Symplectic and Unitary do not split. They only take the upper value $r = \frac{d+1}{2}$.      

Note that over an infinite field like $\mathbb{R}$, the Chevalley–Warning theorem no longer holds, and the anisotropic kernel $V_0$ can be arbitrarily large. However Symplectic spaces retain $r = \frac{d+1}{2}$ over every field $\mathbb{F}$, because $B(\mathbf{x}, \mathbf{x}) = 0$ is built into the definition of an alternating form regardless of the field.

#### Number of Points
The exact same inductive machinery gives a formula for the number of points on a polar space. We got a taste of this with quadrics. For all polar spaces, we have a single unified master formula controlled by the Witt index $r$ and a single parameter $e$ tied to the anisotropic kernel $V_0$.

Let's go through the decomposition again. Let $\mathcal{P}_d$ be a non-degenerate polar space in $\text{PG}(d, \mathbb{F}_Q)$ (where the field size is $Q = q$ for Orthogonal/Symplectic, and $Q = q^2$ for Unitary).

Pick any isotropic point $P \in \mathcal{P}_d$. Its tangent hyperplane $P^\perp$ is a projective $(d-1)$-space $\text{PG}(d-1, \mathbb{F}_Q)$. How does $P^\perp$ intersect the polar space $\mathcal{P}_d$?

Because $P$ is isotropic ($P \in P^\perp$), the restriction of the form to $P^\perp$ is degenerate with a 1-dimensional radical: $\text{Rad}(P^\perp) = P$. Quotienting out $P$ (which geometrically means projecting from the vertex $P$ onto a complementary hyperplane $H \cong \text{PG}(d-2, \mathbb{F}_Q)$ not containing $P$) removes the entire hyperbolic plane $\mathbb{H} = \langle P, R \rangle$ from the Witt decomposition:

$$V = \mathbb{H} \perp V' \implies \dim(V') = \dim(V) - 2$$

Note that $R$ is a second isotropic point chosen outside the tangent hyperplane $P^\perp$ ($R \notin P^\perp$) so that the projective line joining $P$ and $R$ forms a hyperbolic plane $\mathbb{H} = \langle P, R \rangle$.

The intersection $P^\perp \cap \mathcal{P}_d$ is a cone with vertex $P$ over a non-degenerate polar space $\mathcal{P}_{d-2}$ of the exact same type in $\text{PG}(d-2, \mathbb{F}_Q)$, with Witt index $r - 1$.

In terms of the "quotient / star" geometry at $P$: the isotropic lines of $\mathcal{P}_d$ passing through $P$ correspond bijectively to the points of $\mathcal{P}_{d-2}$, and the $k$-dimensional flats of $\mathcal{P}_d$ passing through $P$ correspond bijectively to the $(k-1)$-dimensional flats of $\mathcal{P}_{d-2}$. We saw how the $\mathcal{Q}$-lines through a point in a one-sheeted hyperboloid in 3D correspond to the 2 only points of the lower-dimensional ($d-2 = 1$) quadric. These two points and the point $P$ form two lines intersecting at $P$, which are the lines of the two reguli.

---

**Aside:** This exact correspondence is why the quotient geometry at $P$ is also called the residue of $P$ in the language of Tits buildings: taking the residue of a point in a polar space of rank $r$ yields a polar space of rank $r - 1$, shifting the projective dimension of every incident flat down by 1.

---

We can count the total number of points $\vert{}\mathcal{P}_d\vert{}$ directly from this $d \to d-2$ cone structure by partitioning all points $X \in \mathcal{P}_d$ into two disjoint sets relative to $P^\perp$:

Points inside the tangent hyperplane ($X \in P^\perp \cap \mathcal{P}_d$). This is the cone $P \mathcal{P}_{d-2}$. It consists of:
- The vertex $P$ itself: $1$ point.
- For each of the $\vert{}\mathcal{P}_{d-2}\vert{}$ points $Y \in \mathcal{P}_{d-2}$, the projective line $\langle P, Y \rangle$ contains $Q + 1$ points total, which gives $Q$ points other than $P$: $Q \cdot \vert{}\mathcal{P}_{d-2}\vert{}$ points.

$$\text{Total inside } P^\perp = 1 + Q\vert{}\mathcal{P}_{d-2}\vert{}$$

Points outside the tangent hyperplane ($X \in \mathcal{P}_d \setminus P^\perp$). For any point $X \notin P^\perp$, the line $L = \langle P, X \rangle$ is a secant line to $\mathcal{P}_d$ (since it is not contained in $P^\perp$, it is not tangent and not totally isotropic).

There are $Q^{d} + Q^{d-1} + \dots + 1$ lines through $P$ in $\text{PG}(d, \mathbb{F}_Q)$, of which $Q^{d-1} + Q^{d-2} + \dots + 1$ lie inside the hyperplane $P^\perp$. Thus, there are exactly $Q^{d-1}$ secant lines through $P$ pointing outside $P^\perp$. How many isotropic points (other than $P$) lie on each secant line through $P$?

* Orthogonal ($\mathcal{Q}$, $Q = q$): Every secant line meets a quadric in $2$ points ($P$ and $1$ other point). So each of the $q^{d-1}$ lines contributes $1$ point $\implies q^{d-1}$ points.
* Symplectic ($\mathcal{W}$, $Q = q$): Every point is isotropic, so each of the $q^{d-1}$ lines contributes $q$ points $\implies q \cdot q^{d-1} = q^d$ points.
* Unitary ($\mathcal{H}$, $Q = q^2$): As we proved earlier, every secant line meets $\mathcal{H}(d, q^2)$ in $q + 1$ points ($P$ and $q$ other points). So each of the $(q^2)^{d-1}$ lines contributes $q$ points $\implies q \cdot q^{2d-2} = q^{2d-1}$ points.

Putting the inside and outside counts together gives the exact $d \to d-2$ inductive recurrence for all three families:

Orthogonal $\mathcal{Q}(d, q)$:

$$\vert{}\mathcal{Q}_d\vert{} = 1 + q\vert{}\mathcal{Q}_{d-2}\vert{} + q^{d-1}$$


Symplectic $\mathcal{W}(d, q)$:

$$\vert{}\mathcal{W}_d\vert{} = 1 + q\vert{}\mathcal{W}_{d-2}\vert{} + q^d$$


Unitary $\mathcal{H}(d, q^2)$:

$$\vert{}\mathcal{H}_d\vert{} = 1 + q^2\vert{}\mathcal{H}_{d-2}\vert{} + q^{2d-1}$$


Unrolling those $d \to d-2$ recurrences down to the base case (the anisotropic kernel $V_0$, where $r = 0$ and there are $0$ isotropic points) gives the explicit point counts for all five classical finite polar spaces:

| Polar Space | Projective Dim $d$ | Witt Index $r$ | Parameter $e$ | Total Number of Isotropic Points $\vert{}\mathcal{P}_d\vert{}$ |
| --- | --- | --- | --- | --- |
| Symplectic $\mathcal{W}(2n-1, q)$ | $2n-1$ | $n$ | $1$ | $\frac{q^{2n}-1}{q-1} = \frac{(q^n - 1)(q^n + 1)}{q - 1}$ |
| Hyperbolic Quadric $\mathcal{Q}^+(2n-1, q)$ | $2n-1$ | $n$ | $0$ | $\frac{(q^n - 1)(q^{n-1} + 1)}{q - 1} = \frac{q^{2n-1}-1}{q-1} + q^{n-1}$ |
| Parabolic Quadric $\mathcal{Q}(2n, q)$ | $2n$ | $n$ | $1$ | $\frac{q^{2n}-1}{q-1} = \frac{(q^n - 1)(q^n + 1)}{q - 1}$ |
| Elliptic Quadric $\mathcal{Q}^-(2n-1, q)$ | $2n-1$ | $n-1$ | $2$ | $\frac{(q^{n-1} - 1)(q^{n+1} + 1)}{q - 1} = \frac{q^{2n-1}-1}{q-1} - q^{n-1}$ |
| Unitary (Odd Dim) $\mathcal{H}(2n-1, q^2)$ | $2n-1$ | $n$ | $1/2$ | $\frac{(q^{2n} - 1)(q^{2n-1} + 1)}{q^2 - 1}$ |
| Unitary (Even Dim) $\mathcal{H}(2n, q^2)$ | $2n$ | $n$ | $3/2$ | $\frac{(q^{2n} - 1)(q^{2n+1} + 1)}{q^2 - 1}$ |

Let's put all this into a master formula. Let $Q$ be the ambient field size ($Q = q$ for Orthogonal/Symplectic, $Q = q^2$ for Unitary) and $r$ be the Witt index. Then every single row in the table above is given by one universal expression:

$$\vert{}\mathcal{P}\vert{} = \frac{(Q^r - 1)(Q^{r + e - 1} + 1)}{Q - 1}$$

And the inductive step from rank $r$ down to rank $r-1$ (peeling off one hyperbolic plane $\mathbb{H}$) is universally:

$$\vert{}\mathcal{P}(r)\vert{} = 1 + Q\vert{}\mathcal{P}(r-1)\vert{} + Q^{2r + e - 2}$$

Look at the magic of the parameter $e$. Notice that $\mathcal{W}(2n-1, q)$ and $\mathcal{Q}(2n, q)$ have the exact same $r = n$ and $e = 1$, which means they have the exact same number of points ($\frac{q^{2n}-1}{q-1}$)—and in fact, in characteristic 2, $\mathcal{Q}(2n, q)$ and $\mathcal{W}(2n-1, q)$ are isomorphic as polar spaces by projecting from the nucleus (knot).

Notice how the three quadrics sit around the baseline $\frac{q^d - 1}{q - 1}$ (the size of a hyperplane $\text{PG}(d-1, q)$):

* Parabolic $\mathcal{Q}(2n, q)$ has exactly $\frac{q^{2n}-1}{q-1}$ points (same size as a hyperplane $\text{PG}(2n-1, q)$).
* Hyperbolic $\mathcal{Q}^+(2n-1, q)$ has  an extra $+q^{n-1}$ points above a hyperplane: $\frac{q^{2n-1}-1}{q-1} + q^{n-1}$.
* Elliptic $\mathcal{Q}^-(2n-1, q)$ has a deficit of $-q^{n-1}$ points below a hyperplane: $\frac{q^{2n-1}-1}{q-1} - q^{n-1}$.

#### Number of Maximal Isotropic Subspaces

To count the maximal totally isotropic subspaces or generators, we once again use the same inductive Witt decomposition ($r \to r-1$) and double-counting. Note that the number of points is not equal to the number of maximal isotropic subspaces. Self-duality is a special property of projective spaces $PG(d, K)$. In a general polar space, the number of points is not equal to the number of generators. There are some famous exceptions which will see later. Also note that the diagram of a polar space is not symmetric (it has a generalized quadrangle at one end), unlike a projective space.

Let $g(r)$ denote the total number of generators in our polar space $\mathcal{P}(r)$ of rank $r$. Each generator is a projective flat of projective dimension $r - 1$, meaning it is isomorphic to $\text{PG}(r-1, \mathbb{F}_Q)$.

Let us count the number of incident pairs $(P, M)$ where $P$ is an isotropic point of $\mathcal{P}(r)$ and $M$ is a generator containing $P$:

Counting by choosing the point $P$ first. There are $\vert{}\mathcal{P}(r)\vert{}$ choices for the isotropic point $P$. Once $P$ is fixed, every generator $M$ containing $P$ lies entirely inside the tangent hyperplane $P^\perp$. As we established in the Witt decomposition step, quotienting out $P$ projects $P^\perp \cap \mathcal{P}(r)$ onto a non-degenerate polar space $\mathcal{P}(r-1)$ of the same type and parameter $e$, but with rank $r - 1$.

This projection gives a bijection between the generators of $\mathcal{P}(r)$ passing through $P$ and all generators of $\mathcal{P}(r-1)$. Thus, there are $g(r-1)$ generators passing through $P$. 

Total number of pairs: $\vert{}\mathcal{P}(r)\vert{} \cdot g(r-1)$

Now we count by choosing the generator $M$ first. There are $g(r)$ choices for the generator $M$. Because $M \cong \text{PG}(r-1, \mathbb{F}_Q)$ is a projective space of dimension $r - 1$ over $\mathbb{F}_Q$, the number of points inside $M$ is $\frac{Q^r - 1}{Q - 1}$.

Total number of pairs: $g(r) \cdot \frac{Q^r - 1}{Q - 1}$

Now apply the inductive step. Equating our two counts of the incident pairs $(P, M)$ gives:

$$g(r) \cdot \frac{Q^r - 1}{Q - 1} = \vert{}\mathcal{P}(r)\vert{} \cdot g(r-1)$$

Now we substitute our master formula for the number of points $\vert{}\mathcal{P}(r)\vert{}$:

$$\vert{}\mathcal{P}(r)\vert{} = \frac{(Q^r - 1)(Q^{r + e - 1} + 1)}{Q - 1}$$

Plugging this into the double-counting equation yields:

$$g(r) \cdot \frac{Q^r - 1}{Q - 1} = \frac{(Q^r - 1)(Q^{r + e - 1} + 1)}{Q - 1} \cdot g(r-1)$$

Since $r \ge 1$, the factor $\frac{Q^r - 1}{Q - 1}$ is non-zero and cancels cleanly from both sides, leaving the recurrence relation:

$$g(r) = (Q^{r + e - 1} + 1) \cdot g(r-1)$$

When we unroll this recurrence down to the base case $r = 0$ (where the polar space is reduced to the anisotropic kernel $V_0$, so the unique maximal totally isotropic subspace is the trivial zero vector subspace $\{0\}$, giving $g(0) = 1$), each step $k$ from $1$ to $r$ multiplies the count by $(Q^{k + e - 1} + 1)$:

$$g(r) = \prod_{k=1}^{r} (Q^{k + e - 1} + 1) = (Q^e + 1)(Q^{e+1} + 1)(Q^{e+2} + 1) \cdots (Q^{r + e - 1} + 1)$$

Substituting the specific values of $Q$ and $e$ for each classical polar space gives the complete table of generator counts:

| Polar Space | Field Size $Q$ | Witt Index $r$ | Parameter $e$ | Number of Generators $g(r)$ |
| --- | --- | --- | --- | --- |
| Hyperbolic Quadric $\mathcal{Q}^+(2n-1, q)$ | $q$ | $n$ | $0$ | $2(q + 1)(q^2 + 1) \cdots (q^{n-1} + 1)$ |
| Symplectic $\mathcal{W}(2n-1, q)$ | $q$ | $n$ | $1$ | $(q + 1)(q^2 + 1) \cdots (q^n + 1)$ |
| Parabolic Quadric $\mathcal{Q}(2n, q)$ | $q$ | $n$ | $1$ | $(q + 1)(q^2 + 1) \cdots (q^n + 1)$ |
| Elliptic Quadric $\mathcal{Q}^-(2n-1, q)$ | $q$ | $n-1$ | $2$ | $(q^2 + 1)(q^3 + 1) \cdots (q^n + 1)$ |
| Unitary (Odd Dim) $\mathcal{H}(2n-1, q^2)$ | $q^2$ | $n$ | $1/2$ | $(q + 1)(q^3 + 1)(q^5 + 1) \cdots (q^{2n-1} + 1)$ |
| Unitary (Even Dim) $\mathcal{H}(2n, q^2)$ | $q^2$ | $n$ | $3/2$ | $(q^3 + 1)(q^5 + 1)(q^7 + 1) \cdots (q^{2n+1} + 1)$ |

Notice two structural features in this table:

For the hyperbolic quadric $\mathcal{Q}^+(2n-1, q)$ where $e = 0$, the first factor ($k = 1$) is $q^0 + 1 = 2$. This factor of $2$ reflects the bipartite splitting of the generators of $\mathcal{Q}^+(2n-1, q)$ into two families (where two generators meet in a subspace of even codimension if and only if they belong to the same family). For $n = 2$ ($\mathcal{Q}^+(3, q)$ in $\text{PG}(3, q)$), this gives $2(q + 1)$ lines, which are the two reguli of $q+1$ lines on a hyperbolic quadric surface.

In the two Unitary cases, because $Q = q^2$ and $e$ is a half-integer ($1/2$ or $3/2$), the term $Q^{k + e - 1} = (q^2)^{k + e - 1} = q^{2k + 2e - 2}$ produces purely odd powers of $q$.

Now let's look at the exceptions where the number of isotropic points equal the number of maximal isotropic subspaces. Look closely at the two formulas above and ask: When can the exponent $2n + e - 2$ equal $\frac{1}{2}n(n-1) + ne$?

 Rank $n = 2$ with $e = 1$ (Generalized Quadrangles $W(3, q)$ and $Q(4, q)$): When $n = 2$, the $C_2$ diagram only has two nodes (`o === o`, points and lines). Flipping the diagram `o === o` still gives `o === o`! Plug $n = 2$ and $e = 1$ into the formulas above:
    
- Points of $W(3, q)$ or $Q(4, q)$:  $(q^2 + 1)(q + 1)$.
- Generators (lines) of $W(3, q)$ or $Q(4, q)$:  $(q + 1)(q^2 + 1)$. 

They match! In fact, the parabolic quadric $Q(4, q)$ and the symplectic space $W(3, q)$ are exact point-line duals of each other (when you swap points and lines of $Q(4, q)$, you get $W(3, q)$, and when $q = 2^h$ is even, both are self-dual).
        
Rank $n = 4$ with $e = 0$ (Study's Triality on $Q^+(7, q)$ / Diagram $D_4$): Plug $n = 4$ and $e = 0$ (the hyperbolic quadric $Q^+(7, q)$ in $PG(7, q)$) into the formulas:
    
- Points:  $\frac{(q^4 - 1)(q^3 + 1)}{q - 1} = (q + 1)(q^2 + 1)(q^3 + 1)$.
- Generators:  $(q^0 + 1)(q^1 + 1)(q^2 + 1)(q^3 + 1) = 2(q + 1)(q^2 + 1)(q^3 + 1)$. 

Why is there a factor of $2$ on the generators? Because just like the two reguli on $Q^+(3, q)$, the generators (3-spaces) on $Q^+(7, q)$ split into two families of equal size, and each family has $(q + 1)(q^2 + 1)(q^3 + 1)$ generators—the exact same number as the points! This happens because for $Q^+(7, q)$, the double bond at the end of the $C_4$ diagram splits into two single branches, giving the symmetric three-pronged $D_4$ diagram:
        
```
                      o  (Generator Family 1)
                     /
   0 (Points) o --- o (Lines)
                     \
                      o  (Generator Family 2)

```

Because the three outer prongs of $D_4$ (Points, Generator Family 1, Generator Family 2) are completely symmetric around the central node (Lines),  $Q^+(7, q)$ possesses a 3-way symmetry called Triality that swaps points with either family of generators.

Outside of those special low-rank coincidences ($n = 2$ with $e = 1$, and $n = 3, 4$ with $e = 0$ splitting the generators into two families), a polar space does not have equal numbers of points and generators; flipping a polar space diagram backwards creates a distinct geometry known as a Dual Polar Space.

### Polar Spaces Have the Same Diagram ($C_n$) as a Cube

Let us trace how the diagram of a polar space of rank $3$ (types $0 = \text{points}$, $1 = \text{lines}$, $2 = \text{planes lying inside the polar space}$) is built by taking residues, and compare it directly to the 3D cube:

```
   0 (Points)          1 (Lines)          2 (Planes)
       o ----------------- o ================= o
          (Proj. Plane)      (Gen. Quadrangle)

```

Fix a plane $\Pi$ of the polar space (delete node $2$, leaving nodes $0$ and $1$). What do all the points (type $0$) and lines (type $1$) lying inside a single plane $\Pi$ of the polar space look like? As we saw, every plane inside a polar space satisfies the Veblen-Young axiom and so is an ordinary Projective Plane $PG(2, K)$. So the edge between node $0$ and node $1$ is a single stroke `o --- o` (Projective Plane).
    
Fix a Point $P$ of the polar space (delete node $0$, leaving nodes $1$ and $2$). Look at all the lines (type $1$) and planes (type $2$) of the polar space that pass through the fixed point $P$. If you pick a plane $\Pi$ through $P$ and a line $\ell$ through $P$ ($\ell \not\subset \Pi$), the Buekenhout-Shult "One-or-All" axiom guarantees that inside that residue, there is a unique plane through $\ell$ meeting $\Pi$ in a line through $P$—meaning the lines and planes through $P$ form a Generalized Quadrangle. In Buekenhout-Tits notation, any generalized quadrangle (the thick version of a square / 4-gon) is drawn with a double stroke `o === o`.
    
Fix a Line $\ell$ of the polar space (delete node $1$, leaving nodes $0$ and $2$). Every point $P$ on the line $\ell$ automatically lies in every plane $\Pi$ containing the line $\ell$. So nodes $0$ and $2$ form a generalized digon (blank space).    

Now compare this to the 3D cube. A thin projective plane (`o --- o`) is a triangle ($q = 1$), and a thin generalized quadrangle (`o === o`) is a square ($q = 1$). In fact, if you take a 3D octahedron (the dual of the cube, with $6$ vertices, $12$ edges, and $8$ triangular faces), notice how its vertices and edges behave: the $6$ vertices come in $3$ opposite pairs $\{N, S\}, \{E, W\}, \{F, B\}$ (just like $3$ hyperbolic pairs $x_0 x_1 + x_2 x_3 + x_4 x_5 = 0$), and every vertex is joined by an edge to all vertices EXCEPT its opposite partner.
    
The octahedron / cube is literally the "thin" ($q = 1$) polar space of rank $3$, and a polar space over $\mathbb{F}_q$ is the "thick" ($q > 1$) version where every vertex-pair gets thickened into $(q+1)$ points and every triangle gets thickened into $PG(2, q)$.

More generally, for a polar space of rank $n$, if we fix a generator (node), all the points, lines, and planes inside it form an ordinary projective space , which has the linear diagram: `o --- o --- ... --- o`.

If we fix a flag of low-dimensional subspaces and look at the last two nodes, they form a rank $2$ polar space, which is a Generalized Quadrangle (a thick square `o === o`, because the "1-or-all" axiom forbids triangles).

### The Classical Tits-Veldkamp Definition of Polar Spaces
This definition is superseded by the One-or-All axiom but it tells us quite a bit about the properties of polar spaces. So let's go through it here. Additionally, it ties back to the diagram in its first point about projective spaces. 

A polar space of rank $n \ge 1$ is a pair $(\mathcal{P}, \Sigma)$, where $\mathcal{P}$ is a non-empty set whose elements are called points, and $\Sigma$ is a collection of non-empty subsets of $\mathcal{P}$ called singular subspaces (or simply subspaces), satisfying the following axioms:

1.  **Subspaces are Projective Spaces:** Every element $S \in \Sigma$, considered as an incidence structure with the induced subsets belonging to $\Sigma$, is a projective space of dimension at most $n - 1$.
    
2.  **Intersection Closed:** The intersection of any two elements of $\Sigma$ is either empty or belongs to $\Sigma$.
    
3.  **Subspace Completeness:** If $S \in \Sigma$ and $S'$ is a projective subspace of $S$, then $S' \in \Sigma$.
    
4.  **The Projective Bundle (Cone) Axiom:** If $S \in \Sigma$ has dimension $n - 1$ (a maximal singular subspace, or generator) and $p \in \mathcal{P} \setminus S$ is a point not in $S$, then:
    
    -   There exists a unique singular subspace $S' \in \Sigma$ containing $p$ such that $S \cap S'$ has dimension $n - 2$.
        
    -   The union of all lines joining $p$ to points in $S \cap S'$ is contained in $S'$.

     In modern terms: the set of points of $S$ collinear to $p$ forms a projective hyperplane of $S$.
    
5.  **Non-Degeneracy (Existence of Disjoint Generators):** There exist two maximal singular subspaces in $\Sigma$ of dimension $n - 1$ that are completely disjoint ($S_1 \cap S_2 = \emptyset$).
    

#### Unpacking the Axioms

**Axiom 1 & 3 (Internal Projective Geometry):** This formalizes the phrase "behaving like projective spaces internally". Every flat on the polar space—whether it is an isotropic line, plane, or higher-dimensional flat—satisfies Desargues' and Veblen-Young axioms natively. The intrinsic geometry inside any individual subspace $S \in \Sigma$ has no "curvature" or missing points; it is identical to a standard projective space $\mathrm{PG}(d, \mathbb{F})$.
    
**Axiom 4 (The Polar Connection):** This is the higher-dimensional ancestor of the Buekenhout-Shult point-line axiom. Instead of testing a point against a line, it tests a point $p$ against a maximal subspace $S \cong \mathrm{PG}(n - 1, \mathbb{F})$. It dictates that the locus of points in $S$ that can "see" $p$ along polar lines does not form a messy curved slice: it cuts $S$ along a genuine, flat projective hyperplane $S \cap S' \cong \mathrm{PG}(n - 2, \mathbb{F})$.
    
**Axiom 5 (Global Non-Degeneracy):** If all maximal subspaces shared a common intersection $R$, the geometry would simply be a cone over a smaller polar space with vertex $R$. Demanding disjoint maximal subspaces forces the radical of the geometry to be empty, ensuring the space is non-degenerate.


### What Do Isotropic Points Tell You About A Projective Space

A projective space $\mathrm{PG}(V)$ by itself is completely uniform. The group $\mathrm{PGL}(V)$ acts transitively on points, on lines, and on frames. Every point looks like every other point, and every hyperplane looks like every other hyperplane.

Introducing a non-degenerate form $f$ (or quadratic form $Q$) breaks this global homogeneity and equips the projective space with geometric measurement, duality, and coordinate fibrations.

The set of isotropic points $\mathcal{Q} = \{ \langle x \rangle \mid Q(x) = 0 \}$ acts as the absolute variety (or the "horizon" / "gauge") of the projective space. Without isotropic points, a projective space lacks the internal boundary needed to distinguish different types of incidence, define metrics, or construct geometric dualities.

Here is what isotropic points reveal about the host projective space $\mathrm{PG}(V)$ that cannot be seen otherwise.

**Classification of Lines and Invariant Intersections**

In an unadorned projective space $\mathrm{PG}(n, \mathbb{F})$, all lines are projective copies of $\mathrm{PG}(1, \mathbb{F})$. They have no intrinsic distinction.

The existence of isotropic points immediately stratifies every projective line $\ell$ in $\mathrm{PG}(V)$ into three geometrically distinct types, based solely on how $\ell$ meets the isotropic locus $\mathcal{Q}$: secants, tangents and passants. 

This gives $\mathrm{PG}(V)$ an incidence calculus: you can classify arbitrary linear subspaces by their signature relative to the isotropic locus.

Note that a locus is not a single point. It is a set of all points that satisfy a specified condition, property, or equation. The set of isotropic points is the locus here.

**Concrete Projective Duality Without Coordinates**

Projective geometry has a fundamental duality principle: any theorem about points and hyperplanes remains true if you swap "point" and "hyperplane".

Abstractly, duality maps $\mathrm{PG}(V)$ to the dual projective space $\mathrm{PG}(V^*)$. This map is an external isomorphism: $V^*$ is not $V$. To identify a point with a hyperplane inside the same space, you need a correlation or polarity: $P \mapsto P^\perp$

Isotropic points are precisely the fixed elements of this polarity: $P \in P^\perp \iff Q(P) = 0$.

They mark where a point and its dual hyperplane collide. Non-isotropic points never meet their duals. In synthetic and classical geometry, knowing the locus where $P$ lies on its own dual hyperplane is the only way to anchor the polarity geometrically inside $\mathrm{PG}(V)$.

**Recovering Affine and Non-Euclidean Metrics (Cayley-Klein Geometries)**

Projective space has no notion of distance, angle, or perpendicularity. Cayley and Klein showed that all classical metrics (Euclidean, hyperbolic, elliptic, affine) arise purely inside projective space by designating an absolute quadric of isotropic points $\mathcal{Q}$.

For any two non-isotropic points $A, B \in \mathrm{PG}(V)$, the line $AB$ intersects the isotropic locus $\mathcal{Q}$ at two points, say $X$ and $Y$. The projective cross-ratio:

$$(A, B; X, Y) = \frac{(x_A - x_X)(x_B - x_Y)}{(x_B - x_X)(x_A - x_Y)}$$

is a projective invariant. The metric distance between $A$ and $B$ is then defined purely projectively by $d(A, B) = k \ln (A, B; X, Y)$.

* If $X$ and $Y$ are real points: this is the Beltrami-Klein model of Hyperbolic Geometry.
* If $X$ and $Y$ are complex conjugate points: this produces Elliptic Geometry.
* If the quadric degenerates to a hyperplane: you recover standard Affine / Euclidean Geometry.

Without isotropic points, cross-ratios require choosing four arbitrary points. The isotropic locus provides the two universal reference points on every line to define projective distance and orthogonality.

#### Doesn't This Feel Artificial?
Defining a polar form and then saying we can classify lines based on whether they are tangent, passant or secant to this polar form seems a bit artificial. It seems to depend on the polar form and could change with it. But that's not true. 

Over a finite field $\mathbb{F}_q$ (or $\mathbb{C}$ or $\mathbb{R}$), if you and I write down two completely different-looking non-degenerate symplectic forms, or two different-looking Hermitian forms, or two hyperbolic quadrics in $PG(d, q)$, they are projectively identical. There exists a change of basis in $PGL(d+1, q)$ that turns your equation into my equation.

That means the geometry of the isotropic points and the partition of lines into tangents, secants, and passants is an intrinsic property of the dimension $d$ and the field $K$ itself (with at most 1, 2, or 3 canonical flavors in a given dimension). Choosing a specific polarity is just like choosing a specific basis in a vector space: the coordinates depend on your choice, but the structural invariants you uncover do not.

In general, when applying polar spaces to solve problems, we don't invent a form to classify lines for its own sake. We start with a problem in geometry, coding theory, quantum physics, or group theory where a quadratic or sesquilinear form is naturally baked in.

It is the projective analogue of equipping a bare differentiable manifold with a Riemannian or Lorentzian metric $g_{\mu\nu}$ in general relativity. Before you add the metric, every direction in the tangent space looks the same. Once the physics or geometry problem hands you a metric (or polarity), directions split into light-like (isotropic/tangent), space-like (secant), and time-like (passant), and the polarity gives you a canonical way to map vectors to covectors (points to hyperplanes) without needing to pick coordinates.

Let's look at a few applications of polar spaces and projective geometry.

**Line Geometry in 3D Space (The Klein Correspondence):** Suppose you are studying purely projective 3D space $PG(3, K)$—no metrics, no forms, just points, lines, and planes. You want to understand how lines in 3D space intersect one another. In the 19th century, Felix Klein discovered that the set of all lines in $PG(3, K)$ can be mapped bijectively onto the points of a hyperbolic quadric $Q^+(5, K)$ inside 5-dimensional projective space $PG(5, K)$ (via Plücker coordinates $x_0 x_1 + x_2 x_3 + x_4 x_5 = 0$):

-   A line in $PG(3, K)$ is an isotropic point on $Q^+(5, K)$ in $PG(5, K)$.
    
-   Two lines in $PG(3, K)$ intersect if and only if their corresponding points in $PG(5, K)$ are orthogonal ($f(x, y) = 0$), meaning the line joining them in $PG(5, K)$ lies completely inside the quadric.
    
-   Two lines in $PG(3, K)$ are skew (do not intersect) if and only if the line joining their points in $PG(5, K)$ is a secant line to $Q^+(5, K)$.
    

Here, nobody artificially added a quadratic form to $PG(3, K)$. Simply asking "When do two lines in 3D projective space intersect?" automatically generates the Klein quadric $Q^+(5, K)$ in $PG(5, K)$, and classifying lines in $PG(5, K)$ as tangent/isotropic versus secant literally classifies pairs of 3D lines as intersecting versus skew.

**Quantum Information Theory (Pauli Stabilizer Codes and Qubits):** If you have $n$ qubits in quantum computing, the basic error operators acting on them are products of the $2 \times 2$ Pauli matrices $I, X, Y, Z$. Two Pauli operators either commute ($AB = BA$) or anti-commute ($AB = -BA$). When you quotient out overall phase factors ($\pm 1, \pm i$), every $n$-qubit Pauli operator corresponds to a vector in the $2n$-dimensional vector space $\mathbb{F}_2^{2n}$ (or projective point in $PG(2n-1, 2)$), and the physical question "Do these two quantum observables commute?" translates into a symplectic bilinear form over $\mathbb{F}_2$:

$$f(x, y) = \sum_{i=1}^n (x_i y_{n+i} + x_{n+i} y_i) = 0$$

-   A totally isotropic subspace of this symplectic polar space $W(2n-1, 2)$ is a set of mutually commuting quantum observables—which is the exact definition of a quantum stabilizer code used in quantum error correction.
    
-   If you include the $\pm 1$ signs on the Pauli operators, you get a quadratic form $Q(x)$ over $\mathbb{F}_2$ whose singular/non-singular points and tangent/secant lines classify the eigenvalues and entanglement geometries of multi-qubit systems.

**Error-Correcting Codes and Cryptography (Maximum Distance Separable Codes & Arcs):** Suppose you want to transmit data across a noisy channel using symbols from $\mathbb{F}_q$. A linear error-correcting code is specified by a generator matrix whose columns can be viewed as a set of points in $PG(d, q)$. To prevent errors, you want no $d+1$ points of your set to lie on a common hyperplane (in $PG(2, q)$, no 3 points collinear—called an arc). How do you construct the largest possible set of points in $PG(2, q)$ where no 3 points are collinear? You take a non-degenerate conic (quadric $Q(x) = 0$) in $PG(2, q)$! Because a degree-2 curve can be intersected by any line in at most 2 points (secants hit 2 points, tangents hit 1 point, passants hit 0 points), the $q+1$ isotropic points of the quadric automatically guarantee that no 3 points are ever collinear. Even better, in characteristic $2$ ($q = 2^h$), all $q+1$ tangent lines to the conic concur at a single point called the nucleus $N$; adding $N$ to the $q+1$ isotropic points gives a hyperoval of $q+2$ points with no 3 collinear, yielding optimal error-correcting codes.

**Extremal Combinatorics and Network Design (Ramsey Theory & Moore Graphs):** In computer science and combinatorics, you often want to build dense communication networks (graphs) that have no triangles ($K_3$), or where every pair of nodes is connected by a path of length at most 2 with minimal redundancy (Strongly Regular Graphs and Generalized Quadrangles). Trying to build these graphs by hand or random search fails rapidly as the number of vertices grows. Instead, taking the isotropic points of a polar space in $PG(d, q)$ as vertices, and connecting two vertices by an edge when the line joining them is totally isotropic (lies inside the polar space), produces the most symmetric triangle-free and strongly regular graphs known in mathematics. The line classification (isotropic lines = edges, secant lines = non-adjacent pairs) is what guarantees the exact combinatorial degree and intersection numbers of the network.

**Symmetry Braking and Subgroups of $PGL(d+1, K)$:** In physics and algebra, we often study symmetry breaking: starting with the full group of all projective transformations $PGL(d+1, K)$, how do we isolate smaller simple groups like $PSp(2n, q)$,  $PSU(n, q)$, or $P\Omega(n, q)$? As we saw earlier, if you try to define those groups by writing down all matrix entries that satisfy $M^T J M = J$, you get a complicated system of coupled quadratic equations in the matrix entries. Instead, locking down a polarity $\pi$ breaks the homogeneity of $PG(d, K)$ into orbits (isotropic vs. non-isotropic points; totally isotropic, tangent, secant, and passant lines). That partition allows us to count the exact size of the classical simple groups (by counting how many flags of isotropic points and lines exist) and prove they are simple using Tits buildings.

### Is a Polar Space Always a Homogeneous Polynomial of Degree 2?

Yes, when defined analytically using coordinates, classical polar spaces are always defined by homogeneous polynomials of degree 2 (quadratic forms) or their close algebraic relatives (degree-2-like bilinear/sesquilinear forms). Here is exactly how the math aligns:

-   Orthogonal Spaces (Quadrics): These are exactly the vanishing sets of a homogeneous polynomial of degree 2, meaning $Q(x_1, x_2, \dots, x_n) = 0$. Every term is explicitly of degree 2 (e.g.,  $x_{1}^{2}$ or $x_{1}x_{2}$).
    
-   Symplectic Spaces: An alternating bilinear form $B(\mathbf{x}, \mathbf{y}) = 0$ is a bi-homogeneous polynomial of degree $(1,1)$, i.e., total degree 2 in the coordinates of $\mathbf{x}$ and $\mathbf{y}$). Since $B(\mathbf{x}, \mathbf{x}) = 0$ for all points, the point set is the entire projective space, and the "degree 2" aspect comes from checking the orthogonality relationship between pairs of points.
    
-   Unitary Spaces: A sesquilinear form in finite fields $\mathbb{F}_{q^{2}}$ expands to terms like $x_{i}x_{j}^{q}$, making it a homogeneous polynomial of degree $q+1$. While not strictly a polynomial of degree 2 in the classical sense due to the field automorphism exponent ($q$), it behaves structurally like a degree-2 quadratic form (it is sometimes called a "$q$-quadratic" or Hermitian form) because it pairs two vector inputs together.
    
Ultimately, the geometry of a classical polar space is fundamentally the geometry of degree-2 (two-input) algebraic structures.

Why can't we build a polar space out of a homogeneous polynomial of degree $3$ (a cubic hypersurface $\mathcal{C}$ in $\text{PG}(n, \mathbb{F})$)? 

Test the One-or-All Axiom on a degree-$d$ hypersurface $F(\mathbf{x}) = 0$: suppose $L = \langle \mathbf{x}, \mathbf{y} \rangle$ is a line lying entirely inside the hypersurface, and $p = \langle \mathbf{z} \rangle$ is an external point on the hypersurface ($F(\mathbf{z}) = 0$). For a point $\mathbf{w} = \mathbf{x} + t\mathbf{y} \in L$, we want the line joining $\mathbf{z}$ and $\mathbf{w}$ to lie entirely inside the hypersurface:

$$F(\mathbf{z} + s\mathbf{w}) = 0 \quad \text{for all } s \in \mathbb{F}$$

By Taylor / homogeneous expansion in $s$:

$$F(\mathbf{z} + s\mathbf{w}) = F(\mathbf{z}) + s D_{\mathbf{w}}F(\mathbf{z}) + s^2 D_{\mathbf{w}}^2 F(\mathbf{z}) + \dots + s^d F(\mathbf{w})$$

Since $\mathbf{z}$ and $\mathbf{w}$ are on the hypersurface,  $F(\mathbf{z}) = 0$ and $F(\mathbf{w}) = 0$.

**When $d = 2$ (Quadric):** There is only one intermediate cross-term $s B(\mathbf{z}, \mathbf{w})$, which is linear in $\mathbf{w} = \mathbf{x} + t\mathbf{y}$. Setting $B(\mathbf{z}, \mathbf{x}) + t B(\mathbf{z}, \mathbf{y}) = 0$ gives a single linear equation in $t$, which always has either 1 solution or all $t$ as solutions (the One-or-All Axiom!).
    
**When $d = 3$ (Cubic):** Expanding $F(\mathbf{z} + s\mathbf{w}) = 0$ for all $s$ requires two simultaneous conditions to vanish: the term linear in $s$ ($D_{\mathbf{w}}F(\mathbf{z}) = 0$, which is linear in $t$) and the term quadratic in $s$ ($D_{\mathbf{z}}F(\mathbf{w}) = 0$, which is quadratic in $t$). A random point $\mathbf{z}$ on the cubic will fail to satisfy both equations simultaneously for _any_  $t \in L$, meaning $\mathbf{z}$ is collinear with zero points of $L$! Thus, the One-or-All Axiom fails for $d \ge 3$ unless the cross-terms collapse into a single condition—which happens over finite fields only when $F$ is a Frobenius twist $x_i x_j^q$ (a Hermitian form of degree $q+1$, where $(a+b)^q = a^q + b^q$ eliminates all intermediate binomial terms).

### The Picture From Group Theory

When initially studying projective spaces, we built a connection between: 

- Synthetic Incidence Geometry: Abstract points, lines, and planes obeying the Veblen-Young axioms.
- Buekenhout-Tits Diagram Geometry: The linear diagram $A_n$ (`o --- o --- ... --- o`).
- Algebra & Group Theory: Vector spaces $V$ over a skew field $K$, giving $PG(d, K)$ and the full projective linear/semilinear groups $PGL(V)$ and $P\Gamma L(V)$.

In group theory, $PGL(V)$ is only the first family of classical simple groups. What about the other three great families of classical groups—the Orthogonal groups, the Symplectic groups, and the Unitary groups?

In linear algebra, those three families of groups are obtained by taking a vector space $V$ and equipping it with an inner product (a bilinear, sesquilinear, or quadratic form—like a dot product or Lorentz metric) and looking at the matrices that preserve the vectors of length zero ($x^2 + y^2 - z^2 = 0$).

What do those zero-length points, lines, and planes inside $PG(d, K)$ look like as an incidence geometry in their own right, and can we characterize them purely by a simple point-line axiom without mentioning coordinates or equations? That geometry is a Polar Space, and its Buekenhout-Tits diagram is $C_n$ (a cube diagram `o === o --- o --- ... --- o` thickened up).

A few words on group notation and what $GL$ vs. $PGL$ vs. $SL$ vs. $PSL$, and What $P\Omega$, $PSp$, $PSU$ mean.

In algebra and group theory, all classical matrix groups go through a standard 3-step ladder of prefixes/letters:

- Start with the full matrix group on the vector space $V$: $GL$ (General Linear), $O$ (Orthogonal), $Sp$ (Symplectic), $U$ (Unitary).
- Put an "S" in front ("Special" = determinant $1$): $SL$, $SO$, $SU$.
- Put a "P" in front ("Projective" = quotient out scalar matrices $cI$ so it acts faithfully on projective space $PG(V)$): $PGL$, $PSL$, $PO$, $PSO$, $PSp$, $PU$, $PSU$.

Here is the exact ladder:

| Step in the Ladder | Linear Maps (All Invertible Matrices) | Symplectic Form $f(x, y) = -f(y, x)$ | Hermitian / Unitary Form $f(y, x) = \sigma(f(x, y))$ | Quadratic / Orthogonal Form $Q(x)$ |
| --- | --- | --- | --- | --- |
| 1. Full Matrix Group on $V$ | $GL(n, q)$ (General Linear: all invertible $n \times n$ matrices) | $Sp(n, q)$ (Symplectic matrices preserving $f$) | $U(n, q^2)$ or $GU(n, q)$ (Unitary matrices preserving $f$) | $O(n, q)$ or $GO(n, q)$ (Orthogonal matrices preserving $Q$) |
| 2. "Special" Subgroup ($\det = 1$) | $SL(n, q)$ (Special Linear: $\det(M) = 1$) | $Sp(n, q)$ (Every symplectic matrix already has $\det = 1$!) | $SU(n, q^2)$ (Special Unitary: $\det(M) = 1$) | $SO(n, q)$ (Special Orthogonal: $\det(M) = 1$) |
| 3. Commutator / Simple Core (Only needed for Orthogonal!) | $SL(n, q)$ | $Sp(n, q)$ | $SU(n, q^2)$ | $\Omega(n, q)$ (The commutator subgroup of $SO(n, q)$ of index $2$, where spinor norm $= 1$) |
| 4. "Projective" Quotient (Divide out scalar matrices $cI$) | $PGL(n, q)$ and $PSL(n, q)$ | $PSp(n, q) = Sp(n, q) / \{\pm I\}$ | $PGU(n, q)$ and $PSU(n, q)$ | $PO(n, q)$, $PSO(n, q)$, and $P\Omega(n, q)$ |

Why did we write $P\Omega$ instead of $PSO$ in the bottom-right corner? For $SL$, $Sp$, and $SU$, once you take $\det = 1$ and divide out scalar matrices $cI$ (putting "P" in front), the resulting groups $PSL(n, q)$, $PSp(n, q)$, and $PSU(n, q)$ are already Simple Groups (the atomic building blocks of finite group theory, like prime numbers).

For the Orthogonal group $SO(n, q)$, however, even after taking $\det = 1$ and dividing out $\pm I$ to get $PSO(n, q)$, the group is STILL not quite simple—it has one last subgroup of index $2$ inside it (consisting of products of an even number of reflections with trivial "spinor norm"), denoted by the Greek letter $\Omega(n, q)$.

When we quotient $\Omega(n, q)$ by scalar matrices $\pm I$ to act on projective space, we get $P\Omega(n, q)$ (often written $P\Omega^+(2m, q)$, $P\Omega^-(2m, q)$, or $P\Omega(2m+1, q)$ corresponding to hyperbolic, elliptic, and parabolic quadrics), which is the actual simple orthogonal group.

## Polygons

We refer to a configuration as an $n$-angle in the EEP, if it is a set of n points, no three collinear. The lines of this configuration are formed by connecting every possible pair of these initial points. Because no three points are collinear, any single line in this configuration contains $2$ of the generating points. Furthermore, from any single point, lines must be drawn to connect to all the remaining points in the set, meaning each point lies on exactly $n-1$ lines. 

Similarly, an $n$-lateral is a set of n lines, no three concurrent. The points of this configuration are formed by the intersections of every possible pair of these lines. Because no three lines are concurrent, any single intersection point in this configuration is formed by and lies on $2$ lines. Furthermore, any single line must intersect all the other lines in the set, meaning each line contains exactly $n-1$ intersection points.

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
