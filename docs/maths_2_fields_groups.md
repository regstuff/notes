# Maths 2 - Sets, Rings, Fields & Groups

## A Bit About Proofs & Logic

The main strategies in proofs are by:

-   Counterexample, where given a general statement $P$, to show that $P$ is true it is necessary to give a general proof; but to show that $P$ is false, we have to give one specific instance in which it fails.
    
-   Contradiction, where to prove that $P$ is true, we assume it is false and then show some contradiction. For e.g. if $n \in \mathbb{N}$, $2n$ must be even. Let's assume $2n$ is odd. Then $2n = 2m + 1$ for some $m \in \mathbb{N}$, which implies $n-m = \frac{1}{2}$, i.e. an integer is a fraction, which is a contradiction!
    
-   Contrapositive. The contrapositive of the statement ‘if $P$, then $Q$’ is the statement ‘if not $Q$, then not $P$’. They are logically equivalent. We can prove this if it is more convenient.
    
-   Induction. Prove a statement $P(n)$ for $n=0$. Then show that if $P(n)$ is assumed true, $P(n+1)$ is true. A variation is the Strong Induction principle where we assume $P(m)$ is true for all $m<n$ and then show that it must hold for $P(n)$ also. For example, you could use this to prove that any natural number greater than 1 has a prime factor.
    

Now for Logical Conditions. We say that $P$ is a sufficient condition for $Q$ if the truth of $P$ implies the truth of $Q$; that is, $P$ implies $Q$, which is the same as "if $P$, then $Q$", or "$Q$ if $P$".

We say that $P$ is a necessary condition for $Q$ if the truth of $P$ is implied by the truth of $Q$, that is, $Q$ implies $P$. (This is the converse of the statement that $P$ implies $Q$.) We also say "$Q$ only if $P$".

We say that $P$ is a necessary and sufficient condition if both the above hold true.

AND ($\land$), OR ($\lor$) and NOT ($\neg$) to combine conditions should be familiar from Boolean operations.

## Sets, Operations & Relations

### Sets

A set is a collection of objects. That definition doesn't help much because what is a collection?! No wonder then that the word "set" has 430 definitions in the Oxford Dictionary, which makes it one of the longest entries. But our definition is something we can more or less grasp, so we won't belabour the point. Let's move on.

Unions, intersections and difference i.e. elements of $A$ not in $B$, correspond to the logical operations OR, AND and NOT. The symmetric difference of two sets is any element that is in only one of $A$ or $B$. This corresponds to XOR. We can write, $A \Delta B = (A \setminus B) \cup (B \setminus A) = (A \cup B) \setminus (A \cap B)$.

The Cartesian Product $A \times B$ is the set of all ordered pairs with first element in $A$ and second element in $B$. You could extend this to a product of $n$ sets as well. The name ‘Cartesian’ commemorates Descartes, who unified algebra and geometry by the insight that the Euclidean plane (a geometric object) is essentially the same as the set $\mathbb{R} \times \mathbb{R} = \mathbb{R}^2$: each point of the plane can be represented by its Cartesian coordinates, which are an ordered pair $(x, y)$ of real numbers.

The number of elements in a set $A$ is called the cardinality of $A$, and written as $\vert{}A\vert{}$. Note that $\vert{}A \cup B\vert{} = \vert{}A\vert{} + \vert{}B\vert{} - \vert{}A \cap B\vert{}$ and $\vert{}A \times B\vert{} = \vert{}A\vert{} \cdot \vert{}B\vert{}$.

The set of all subsets of a set $A$, including $A$ and the empty set, is called the Power Set of $A$.

Surprisingly, you can use logical operations to prove stuff about sets. We already mentioned how unions, intersections etc. are related to logical operations. Now let us say we want to prove: $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$. This will follow if we can show that the two propositions $p \land (q \lor r)$ and $(p \land q) \lor (p \land r)$ are equivalent. We could just write down the truth tables of both the logical expressions and see if they are equivalent.

### Operations & Relations

A binary operation is a mapping from $A \times A$ to $A$ i.e. it takes two elements of set $A$ and outputs one element. Addition and multiplication are examples. You can have n-ary operations.

A binary relation is a mapping from $A \times A$ to an output that is either true or false. Greater than and less than are examples.

An equivalence relation is a binary relation $R$ on $A$ that is reflexive, or $(a,a) \in R$ for all $a \in A$; symmetric i.e. if $(a, b) \in R$ then $(b, a) \in R$; transitive i.e. if $(a, b) \in R$ and $(b, c) \in R$ then $(a, c) \in R$.

The relation mod 4 between two numbers is an equivalence relation.

An equivalence relation results in a partition of the set $A$. A partition is a set of subsets of $A$ where none of them is empty and each element of $A$ lies in only one of these subsets. Thus the equivalence relation between $a$ and $b$ essentially comes down to are we or are we not in the same subset of the partition. The subsets are called equivalence classes.

A non-constant polynomial is called irreducible if it cannot be written as the product of two polynomials of smaller degree. Any linear polynomial is obviously irreducible. Irreducible polynomials play a similar role to prime numbers, with one main difference: any non-constant polynomial can be factorised into irreducible polynomials, but the factors are not unique.

## Rings & Fields

Rings were originally conceptualized to help solve Fermat's Last Theorem, but we don't need to bother about that now. As a starting point, a ring is literally a ring or a circular series of numbers that wraps around after reaching a particular point. You know this for modulo functions already, such as modulo 4 where the remainders are $\{0, 1, 2, 3\}$. Then all the integers wrap around again. So modular arithmetic isn't a separate thing from the integers. A lot of our work with rings is via modular arithmetic, modulo functions, and their algebras. But rings in abstract algebra are not exclusively about modular arithmetic.  

Even the integers $\mathbb{Z}$ are a ring. They don't wrap around, but you could look at it as an infinitely large ring. In fact, modern geometry and algebra view $\mathbb{Z}$ as the "parent ring" from which every other ring inherits its basic characteristics. Every modular ring $\mathbb{Z}/n\mathbb{Z}$ is a slice of the infinite integers. You create them by taking the infinite ring $\mathbb{Z}$ and collapsing it at a certain interval $n$. We can also go the other way around and attempt to construct an "infinitely large ring" using a concept called the inverse limit. We chain together larger and larger modular rings, looking at $\mathbb{Z}/2\mathbb{Z}$, then $\mathbb{Z}/4\mathbb{Z}$, then $\mathbb{Z}/8\mathbb{Z}$, and so on out to infinity. You don't quite get $\mathbb{Z}$, but you get a closely related infinite ring called the $2$-adic integers (a specific instance of the $p$-adic integers, $\mathbb{Z}_p$). In these rings, numbers can be infinitely long, effectively allowing you to work with modular arithmetic at an infinite scale.  

### The Intuitive Picture

Let us build up what goes into a ring step-by-step. Start with the full ring $R = \mathbb{Z}$. Imagine an infinite tape measure marked with ticks at $\dots, -2, -1, 0, 1, 2, \dots$. Addition ($a + b$) is about shifting along the tape. Multiplication ($a \cdot b$) is about scaling the tape. $0$ is the anchor point (origin).

Now we want to build up the rules for mathematics in this ring. For example, how do I add, multiply and whatnot. The rules for addition are pretty straightforward and similar to integers. In terms of the intuitive picture, we'll focus a bit more on other properties, such as multiplication, division and prime numbers, that might trip people up.

Let's say you take a circle that is 4 units in circumference and wrap all your integers around that circle. You keep lapping around again and again. So modular arithmetic is kind of like going in circles, while the integers are like going to infinity. It's very spiritual!

Now when you keep wrapping around the circle, you will see that numbers start to cluster up one above the other. $\{\dots, -8, -4, \mathbf{0}, 4, 8, 12, \dots\}$ would be one stack. Similarly, $\{\dots, -7, -3, \mathbf{1}, 5, 9, \dots\}$ etc. You would get 4 such stacks. Each of these stacks is now called a coset. It is a partition, which is a very literal description: all the integers will be present in exactly one partition. We say they are in an equivalence relation, which is also pretty much what it says. They are equivalent for all practical purposes while working in this ring. This process is technically called gluing i.e. you say this set of points from the integers are all equivalent in this subring. You glued them together into one thing! They are also called equivalence classes and are subsets of the main ring. In fact, they are subrings, but more on this later.

$I = 4\mathbb{Z} = \{\dots, -8, -4, \mathbf{0}, 4, 8, 12, \dots\}$ is a bit special. These are the numbers that stack with $0$. They are equivalent to it. This set (subring actually) of numbers is called an ideal. The most important thing is, if you multiply any integer by any element in this stack, the result is also found in this stack. Nothing surprising here. The stack is all the multiples of 4. $4$ multiplied by an integer will be a multiple of $4$ and so it will be part of the stack.

But conceptually, as far as the ring goes, this entire set, i.e. every number in the ideal, functions in multiplication like a $0$ does among integers. You multiply any number by $0$, you end up with a $0$. This is called the Absorption Property. We have therefore recreated a property of multiplication in the integers in such a way that it will work in a ring.

Now, pick up the entire $I$ and shift it to the right by 1, then 2, then 3.

-   Shift by $0$ (This is called the zero coset / The Ideal itself): $0 + I = \{\dots, -8, -4, \mathbf{0}, 4, 8, \dots\}$
     
-   Shift by $1$ (The coset $1 + I$): $1 + I = \{\dots, -7, -3, \mathbf{1}, 5, 9, \dots\}$
     
-   Shift by $2$ (The coset $2 + I$): $2 + I = \{\dots, -6, -2, \mathbf{2}, 6, 10, \dots\}$

-   Shift by $3$ (The coset $3 + I$): $3 + I = \{\dots, -5, -1, \mathbf{3}, 7, 11, \dots\}$
      
-   Shift by $4$: $4 + I = \{\dots, -4, 0, \mathbf{4}, 8, 12, \dots\} = 0 + I$
    
Shifting by $4$ just lands the grid back on top of itself. So what we have here is the 4 partitions or cosets we talked about earlier. Since we have a $0$ coset, we can also see that the other cosets are essentially just the remainders we get when we divide an integer by the modulus, in this case: $4$. Any integer with the same remainder gets bracketed into the same coset or equivalence class i.e. the $k$-coset consists of all elements $a$ where $a - k$ is in the ideal, which means for any two elements $a$ and $b$ in the same coset, $a - b \in I$.  

The set of 4 cosets (think of them as co-sets) are called a quotient or factor ring $R/I$. Why they are not called the remainder ring is a bit confusing because that is what they are built from, but never mind. 

The set of 4 cosets is a ring in the sense that they satisfy all the rules of addition and multiplication we expect from a ring (we'll talk about that next). The elements of this quotient ring $R/I$ are not individual numbers; they are the 4 distinct stacks of overlapping points (the cosets). 

### The Algebraic Rules

It's good to have the intuitive picture in your head, but the algebraic rules given below make it easy to manipulate and work with rings.

A ring is a set where we define an addition and a multiplication operation. Addition must be closed, commutative and associative. There is a zero and every element in $R$ has an additive inverse. Regarding multiplication, we require closure and the operation should be associative. Multiplication and addition should together follow the Distributive Law. 

Note that the familiar addition and multiplication we already know are just special cases. We could redefine them however we want provided they follow the above rules.

In our definition of a ring, we neither required the multiplicative identity or inverse, or even that multiplication be commutative. Some conventions require a ring to have a multiplicative identity. Rings without an identity are termed rng, without the $i$. If the identity is present, it becomes a ring (with the $i$). We won't bother with that here. Note that any rng can be shown to be a subring (without the identity of course) of a r**i**ng.  

**Examples of Rings:** Natural numbers are not a ring as they do not contain negative integers and so the positive integers have no additive inverse. The integers however form a ring. $n\mathbb{Z}$ for some $n \in \mathbb{N}$ is also a ring, as are the set of all polynomials with coefficients in $R$, for any ring $R$. Note that a set with an upper limit on the degree of polynomials allowed is not a ring as the multiplication operation will result in a polynomial of higher degree, which means we have no closure.

The Cancellation Law holds for rings. If $a + c = b + c$, then $a = b$.

A subring of $R$ is a subset $S \subseteq R$ which itself forms a ring (using the same operations as those in $R$). You need not check all the axioms of a ring to determine if a subset is a ring. A non-empty subset $S$ of a ring $R$ is a subring provided that, for all $a, b \in S$, we have $a - b \in S$ and $ab \in S$.

If you are asked to prove that something is a ring, it is usually much easier to recognise that it is a subset of a structure known to be a ring, and then apply the subring tests.

### Intuition Redux

The set of 4 cosets we talked about earlier is a ring because we used the ideal to partition the ring. Note that you could make cosets using any subring, but the set of cosets becomes a ring only when the subring used in partitioning is an ideal.  

Why do we care so much about the ideal and this absorption property? Because it ensures that multiplication results in the same result irrespective of which integer you use from a coset. So $6 \times 5 = 30 \equiv 2 \pmod{4}$, which is what you get when you do $2 \times 1$ or $10 \times 9$. As mentioned, the ideal includes all the multiples of the number you used while wrapping around ($4$ in our case). That ensures that any two numbers of the type $4 + x$ and $4 + y$, when multiplied, result in $(4 + x)(4 + y) = 16 + 4(x + y) + xy$. Since we then take modulo 4 of this product, we are left with $xy$ always, irrespective of which numbers from an equivalence were multiplied. The mathematics of multiplication is consistent. You can treat all numbers in an equivalence class as the same. So you have ensured one criterion needed to create a ring.  

That's nice but how do we know this wouldn't hold if I used a subring other than an ideal to create my coset partitions? With integers, every subring is an ideal so we can't investigate this property. But let's look at a ring where subrings and ideals are different: the polynomial ring $\mathbb{R}[x]$ or the ring of integers in two variables $\mathbb{Z}[x]$.  

Consider the ring $\mathbb{Z}[x]$ (polynomials with integer coefficients).
  
Let $S$ be the subring of constant polynomials:  

$$S = \mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\} \subset \mathbb{Z}[x]$$

$S$ is a genuine subring because you can add two integers: you get an integer. You can multiply two integers: you get an integer. It has $0$ and $1$.  

Now, when we "glue" this subring $S$ to zero, every integer becomes zero. Now let's multiply some polynomial $x$ by "two zeroes" $0$ and $5$. $0 \cdot x = \mathbf{0}$ and $5 \cdot x = \mathbf{5x}$. Both of these should give the same result up to equivalence class i.e. their difference must be in the glued set $S$. But $5x - 0 = 5x$ which is not an integer and so not in $S$. Multiplication is broken. You can't multiply with certainty.

The failure happened because an element inside our glued set ($5 \in S$), when multiplied by an element outside ($x \in \mathbb{Z}[x]$), escaped outside the glued set ($5x \notin S$). Looking back at our previous example where we multiplied integers using the glued set $4\mathbb{Z}$, we saw that the multiplication results in terms like $16$ and $4(x+y)$, which need to be "cancelled out" so that every product of the equivalence classes results in $xy$. What does cancelling out mean? It means they go to $0$ or that they should fall into the ideal.

### Algebra Redux
So to rigorously define an ideal, an ideal is a subring $S$ of $R$ such that if $s \in S$, then $sr \in S$ and $rs \in S$ for all $r \in R$. This is kind of like a "0" because anything multiplied by 0 is 0.

The set of ideals acts like a black hole. It can pull all elements of $R$ into itself by multiplication. When you quotient out by $I$, every element in $I$ collapses into the additive identity $0$. An ideal allows you to kill information and compress the ring into a smaller quotient ring $R/I$. Ideals are the algebra of $0$ leading to collapsing and singularities.

You needn't write out the entire set of elements in an ideal. Most times, you can just specify the generators like so <g_1, g_2>. Then start adding up linear combinations of the generators to generate your entire set of ideals. 

$$\langle g_1, g_2 \rangle = \{ r_1 g_1 + r_2 g_2 \mid r_1, r_2 \in R \}$$

This will ensure closure when any element of the ideal is multiplied by some element of $R$. 

**Example:** For our previous examples with integers and 4Z, the ideal is simply written as \<4\>, which is equivalent to $\{\dots, -8, -4, \mathbf{0}, 4, 8, \dots\}$.

Now for something more complicated, $\langle 1, x \rangle$ is an ideal of the ring of polynomials, but it is the trivial ideal—the entire polynomial ring itself, because it contains $1$. Any ideal containing the identity $1$ absorbs everything:

$$\forall f(x) \in R[x], \quad f(x) = f(x) \cdot 1 \in \langle 1, x \rangle \implies \langle 1, x \rangle = R[x]$$

Quotienting out by $\langle 1, x \rangle$ sets $1 = 0$, collapsing the entire ring into the zero ring $\{0\}$.

To get a non-trivial factor ring, an ideal cannot contain any non-zero constants (units). In $R = \mathbb{R}[x]$, the ideal generated by the single polynomial $x$:

$$\langle x \rangle = \{ f(x) \cdot x \mid f(x) \in \mathbb{R}[x] \} = \{ a_1 x + a_2 x^2 + \dots + a_n x^n \}$$

This contains every polynomial with no constant term. Multiply any polynomial without a constant term by any arbitrary polynomial, the product has no constant term, so it stays trapped inside $\langle x \rangle$.
    
In the quotient ring $\mathbb{R}[x]/\langle x \rangle$, we declare $x = 0$. Every polynomial $a_0 + a_1 x + a_2 x^2$ collapses down to just its constant term, so $\mathbb{R}[x]/\langle x \rangle \cong \mathbb{R}$.

Another example: $\langle x^2 + 1 \rangle$, the quotient ring of which generates the complex numbers. 

$$\langle x^2 + 1 \rangle = \{ f(x)(x^2 + 1) \mid f(x) \in \mathbb{R}[x] \}$$

This contains every polynomial that has $(x^2 + 1)$ as a factor (i.e., polynomials where $f(i) = 0$ and $f(-i) = 0$). If in $\mathbb{R}[x]/\langle x^2 + 1 \rangle$, we declare $x^2 + 1 = 0 \implies x^2 = -1$, then the quotient ring is essentially the remainders we get when a polynomial is divided by $x^2 + 1$. Such a reminder is utmost of degree 1. 

$$r(x) = ax + b \quad (a, b \in \mathbb{R})$$

Just replace $x$ by $i$ and you are looking at a complex number!

A third example is a multi-generator ideal in two variables: $\langle x, y \rangle$.

In $R = \mathbb{R}[x, y]$:

$$\langle x, y \rangle = \{ p(x,y) \cdot x + q(x,y) \cdot y \mid p, q \in \mathbb{R}[x, y] \}$$

This contains all polynomials whose constant term is $0$. Setting both $x = 0$ and $y = 0$ gives us a quotient ring which is just the constants: $\mathbb{R}[x, y]/\langle x, y \rangle \cong \mathbb{R}$.

### Establishing More Mathematical Properties

So we've figured out how to do consistent multiplication. Now we need to work towards consistency in division. The first step is to eliminate zero divisors, i.e., some non-zero element $k \in R$ such that $k \cdot a = 0$ for some non-zero $a \in R$. Ideally, you don't want multiplication going to $0$ when two non-zero numbers are multiplied. Additionally, it's nice to have commutation in multiplication. If a ring has no zero divisors and is commutative, the ring is called an Integral Domain.

Now, with the integers, every integer has a unique set of prime factors. A ring which has this property (unique up to ordering and multiplication by units) is a Unique Factorization Domain (UFD). From a UFD we move up to a Principal Ideal Domain (PID). A PID is one where every ideal is principal, i.e., it has only one generator. PIDs have some nice properties not found in UFDs. For example, GCDs are linear combinations. In a PID, every non-zero prime ideal is automatically a maximal ideal. This means if you quotient a PID by a prime ideal, you are guaranteed to get a field. PIDs also have some nice properties when it comes to vector spaces.

Upgrading to a field means every non-zero element is invertible. Actually, if a ring has a (multiplicative) identity, and every non-zero element has a (multiplicative) inverse, it is called a Division ring. If a division ring is also commutative, it is a field.

Since every non-zero element of a field has an inverse, say $a^{-1}$, it means multiplying any other element by this inverse gives a valid element of the field. This is the same as saying dividing an element by another non-zero element gives another element of the field. So every non-zero element divides every other element without leaving a remainder. Because of this property, fields allow for the definition of Vector Spaces. You can divide by scalars, talk about exact dimensions, find bases, and solve systems of linear equations without worrying about remainders or fractions.

Note that a field has only two ideals, both trivial:  $\{0\}$ and the entire field. Because every non-zero element has an inverse, any ideal containing a non-zero element will swallow the whole ring. To see why, let's say an ideal has a non-zero element. That element has an inverse in the field. Applying the definition of an ideal, we multiply these two and the product, i.e.,  $1$, must be in the ideal. So $1$ is in the ideal, which means any element of the field multiplied by $1$, i.e., that element itself, must also be in the ideal.

Let's see what it takes to replicate all this mathematics in a ring. But first, in standard school arithmetic, we know that a prime number has only $1$ and itself as factors. They are irreducible into smaller factors. We also know that if a prime $p$ divides a product $ab$, i.e.,  $p \mid ab$, then at least one of $p \mid a$ and $p \mid b$ holds true. These two definitions are collapsed into the same definition.

However, this doesn't always hold in a ring. An element $p$ is irreducible if it cannot be factored into two non-units:  $p = ab \implies a \text{ is a unit or } b \text{ is a unit}$. This is the familiar notion. Wait a minute! What is a unit?

In elementary arithmetic and geometry, the word "unit" is commonly used in two ways:

1.  The unit scale / unit length: The minimal step ($1$) used to measure or generate all other integers via repeated addition ($1 + 1 + 1 = 3$).
    
2.  The multiplicative identity: The number $1$, which leaves other numbers unchanged under multiplication ($x \cdot 1 = x$).
    
When algebraists generalized arithmetic to arbitrary rings, they already had standard terms for those concepts: the additive generator and the multiplicative identity. The word unit was repurposed to mean any element that possesses a multiplicative inverse within the ring:  $u \cdot v = 1$.

In $\mathbb{Z}$, the only numbers with multiplicative inverses happen to be $1$ and $-1$. Because $\pm 1$ also happen to be the numbers that generate the ticks on the tape by addition, everyday intuition conflates the two ideas. In a general ring, however, elements can have multiplicative inverses without having anything to do with a "step size": In $\mathbb{Z}_{12}$, the number $5$ is a unit because $5 \times 5 = 25 \equiv 1 \pmod{12}$. It has an exact inverse ($5^{-1} = 5$), yet it is not a "minimal step size" in the geometric sense.

In modern algebra: the Unity / Identity is the single element $1$. The Unit: any element that can be divided by (has an inverse that lands back in $1$).

In a finite ring, every element is either a unit or a zero divisor. This also means that if you take a unit and multiply it by all the elements in the ring, the set of products will cover all the elements of the ring.

If two elements of a ring $a$ and $b$ are related such that $a = u \cdot b$ where $u$ is a unit (i.e., it has an inverse),  $a$ and $b$ are called associates. This will be important in terms of factorization as we'll see below. Now you see why units are called units. They are similar to $1$ in integers in that if we multiply some element of a ring by a unit, it lands up at some equivalent element called its associate.

Now getting back to primes and irreducibles, an element $p$ is irreducible if it cannot be factored into two non-units: $p = ab \implies a \text{ is a unit or } b \text{ is a unit}$. An element $p$ is prime if: $p \mid ab \implies p \mid a \quad \text{or} \quad p \mid b$. Whenever $p$ divides a product, it must divide at least one of the factors. 

In terms of ideals, this means the principal ideal $\langle p \rangle$ is a prime ideal: $ab \in \langle p \rangle \implies a \in \langle p \rangle \text{ or } b \in \langle p \rangle$.

Now what does unique factorization entail in a ring. A UFD means that every non-zero, non-unit element $x$ can be written as a product of irreducibles, and that factorization is unique up to the order of factors and multiplication by units (basically our equivalence classes or partitions from modulo discussed sometime above). 

Formally, if $x$ is factored into irreducibles in two ways:

$$x = p_1 p_2 \dots p_r = q_1 q_2 \dots q_s$$

then the number of factors is the same: $r = s$. After reordering, each $p_i$ is an associate (is in an equivalence relation) of $q_i$ (meaning $p_i = u_i q_i$ for some unit $u_i$). The "Prime" Property Is what proves this uniqueness.

To prove that the two factorizations are identical:

$$p_1 p_2 \dots p_r = q_1 q_2 \dots q_s$$

You start with the first irreducible building block, $p_1$.

Clearly, $p_1$ divides the left side, so:

$$p_1 \mid (q_1 q_2 \dots q_s)$$

Now you want to cancel $p_1$ with one of the factors on the right.

-   **If $p_1$ is PRIME:**
    
    By definition of prime, $p_1 \mid (AB) \implies p_1 \mid A \text{ or } p_1 \mid B$.
    
    Extending this to $s$ terms, $p_1$ must divide at least one specific $q_j$.
    
    Since $q_j$ is irreducible, its only divisors are units and associates. Therefore, $p_1$ and $q_j$ must be associates:
    
    $$q_j = u \cdot p_1$$
    
    You cancel $p_1$ from both sides, leaving a smaller equation. By induction, every factor matches up.
    
-   **If $p_1$ is ONLY IRREDUCIBLE (Not Prime):**
    
    Knowing that $p_1 \mid (q_1 \cdots q_s)$ does NOT guarantee that $p_1$ divides any individual $q_j$!
    
    It could divide the whole product without dividing any piece.

In short: We factor into irreducibles (unbreakable blocks), but we need those blocks to be prime (divisibility-passing) so that the factorization is guaranteed to be unique.

This is a UFD. We'll skip looking at what it takes to jump to a PID and just look at what is needed to go from PID to a field. To build a field out of a PID, you quotient by a principal ideal $I = \langle p \rangle$.

In any commutative ring: $R/I \text{ is a field} \iff I \text{ is a \textbf{maximal ideal}}$

"Maximal" means there is no other ideal strictly squeezed between $I$ and $R$:

$$I \subseteq J \subseteq R \implies J = I \quad \text{or} \quad J = R$$

Now translate that into the language of a PID, where every ideal is generated by a single element ($I = \langle p \rangle$ and $J = \langle d \rangle$):

$$\langle p \rangle \subseteq \langle d \rangle \iff d \mid p$$
    
Therefore, saying $\langle p \rangle$ is maximal means: If $d$ divides $p$, then either $\langle d \rangle = \langle p \rangle$ ($d$ is an associate of $p$) or $\langle d \rangle = R$ ($d$ is a unit).
    
But that is the definition of an irreducible (or prime) element! In a PID: 

$$\text{Maximal Ideal} \iff \text{Prime Ideal} \iff \text{Generated by an Irreducible Element}$$

This also leads to the condition that a field has only two ideals, both trivial: 0 and the entire field. 

Two rings are isomorphic i.e. essentially the same for the purposes of algebra if we can set up a map between their elements in such a way that addition and multiplication correspond; that is, if $a$ corresponds to $a'$ and $b$ to $b'$, then $a + b$ corresponds to $a' + b'$ and $ab$ to $a'b'$.

A weaker condition is a homomorphism. We define a homomorphism from a ring $R$ to a ring $S$ to be a function or map $\theta : R \to S$ which satisfies $\theta(a + b) = \theta(a) + \theta(b)$ and $\theta(ab) = \theta(a)\theta(b)$ for all $a, b \in R$. Note that the addition and multiplication on the left of these equations are the operations in $R$, while those on the right are the operations in $S$. If a homomorphism is bijective, it becomes an isomorphism. A homomorphism is in some way a preservation of the shape of the ring.

Let $\theta : R \to S$ be a homomorphism of rings. The image of $\theta$ is $\text{Im}(\theta) = \{s \in S : s = \theta(r) \text{ for some } r \in R\}$, and the kernel of $\theta$ is $\ker(\theta) = \{r \in R : \theta(r) = 0\}$.

$\text{Im}(\theta)$ is a subring of $S$. $\ker(\theta)$ is a subring of $R$ which has the additional property that, for any $x \in \ker(\theta)$ and $r \in R$, we have $rx \in \ker(\theta)$ and $xr \in \ker(\theta)$. Two elements of $R$ are mapped to the same element of $S$ under $\theta$ if and only if they lie in the same coset of $\ker(\theta)$.

The kernel of a homomorphism $\theta : R \to S$ is an ideal of $R$. $\text{Im}(\theta)$ is a subring of $S$; $R/\ker(\theta) \cong \text{Im}(\theta)$. This is the first isomorphism theorem.

### Homomorphisms and Isomorphisms

Remember back when we took the modulo 4, i.e., we wrapped the integers around the circle. We ended up with the ideal, i.e., all the numbers stacked over $0$. And we got the quotient ring which consisted of the equivalence classes of the remainders. We can generalize this to a map $\phi$, instead of restricting it to just modulo functions.

Let's first define a ring homomorphism. $\phi: R \to S$ is a structure-preserving map:

$$\phi(a + b) = \phi(a) + \phi(b) \quad \text{and} \quad \phi(ab) = \phi(a)\phi(b)$$

We define $\ker(\phi) = \{k \in R \mid \phi(k) = 0_S\}$ and the image of $\phi$, denoted $\operatorname{im}(\phi)$ (or $\phi(R)$), is the set of all elements in the target ring $S$ that are actually reached by applying $\phi$ to the elements of the source ring $R$:

$$\operatorname{im}(\phi) = \{\phi(r) \mid r \in R\} = \{s \in S \mid \exists r \in R \text{ such that } \phi(r) = s\}$$

Our earlier modulo operation was actually a homomorphism (well, actually a surjective homomorphism, or epimorphism), where $R$ was $\mathbb{Z}$ and $S$ was $\mathbb{Z}_4$.

The kernel should remind you of the ideal. It is the set of all elements that get crushed to zero in $S$.

And when does $\phi$ send two different elements $x, y \in R$ to the exact same value in $S$?

$$\phi(x) = \phi(y) \iff \phi(x) - \phi(y) = 0_S \iff \phi(x - y) = 0_S \iff x - y \in \ker(\phi)$$

The map $\phi$ is literally grouping the elements of $R$ into bundles (cosets) based on $\ker(\phi)$. So the way $\phi(x)$ groups elements should remind you of the quotient ring.

This is the content of the **First Isomorphism Theorem for Rings**, which states:

If $\phi: R \to S$ is a ring homomorphism, then:

$\ker(\phi)$ is an ideal of $R$.

The image $\operatorname{im}(\phi)$ is a subring of $S$.

$R/\ker(\phi) \cong \operatorname{im}(\phi)$.

Now let's look at the **Second Isomorphism Theorem**. Structurally, the theorem is equivalent to what we have in arithmetic. For two integers $a$ and $b$, $a \cdot b = \operatorname{lcm}(a, b) \cdot \gcd(a, b)$. In the isomorphism relation below, the left side's numerator is the $\gcd$ and the right side's denominator is the $\operatorname{lcm}$.

Let $R$ be a ring, $S$ a subring of $R$, and $I$ an ideal of $R$. Then:

1.  The sum $S + I = \{s + i \mid s \in S, i \in I\}$ is a subring of $R$.
    
2.  The intersection $S \cap I$ is an ideal of $S$.
    
3.  $(S + I) / I \cong S / (S \cap I)$    

Let's look at an example. $R = \mathbb{Z}$, with the ideal grid $I = 6\mathbb{Z} = \{\dots, -12, -6, 0, 6, 12, \dots\}$. So $R/I = \mathbb{Z}_6$.

Now introduce a subring $S$. Let $S = 2\mathbb{Z} = \{\dots, -4, -2, 0, 2, 4, 6, \dots\}$ (all even numbers).

The left side of the isomorphism: $(S + I)/I$ involves expanding $S$ by $I$ and then quotienting by $I$. One reason we would want to do this is because some elements of $I$ might not be in $S$, so by adding $I$, we take care of this issue.

What is $S + I$? Add any multiple of $6$ to any even number. Since multiples of $6$ are already even, $S + I$ is just all even numbers: $S + I = 2\mathbb{Z}$.

Modding out by $I = 6\mathbb{Z}$ gives $\{0, 2, 4\}$. So $(S + I)/I$ is the 3-element sub-dial inside the 6-hour clock: **$\{[0], [2], [4]\}$**.

The Right side: $S / (S \cap I)$. Look only at the subring $S = 2\mathbb{Z}$, what part of $I = 6\mathbb{Z}$ lives inside $S$? $6\mathbb{Z}$ itself! So if we quotient by this, what do we get: $0 \pmod 6$, $2 \pmod 6$, and $4 \pmod 6$.

What this means is, the elements of $I$ that don't belong to $S$ contribute nothing to $S$, so modding out by the whole ideal $I$ has the exact same effect as modding out only by the shared overlap $S \cap I$. The only algebraic issue is that you cannot technically form the quotient $S/I$ unless $I$ is entirely contained within $S$ (it must be an ideal of $S$). By adding $I$ to $S$ on the left (creating $S+I$), or taking the intersection on the right ($S \cap I$), we ensure the quotient fractions are perfectly legal.

Now for the **Third Isomorphism Theorem**. Structurally, this is like the fraction rule in elementary arithmetic:

$$\frac{a/c}{b/c} = \frac{a}{b}$$

The theorem states: Let $R$ be a ring, and let $I$ and $J$ be ideals of $R$ with $I \subseteq J \subseteq R$. Then:

1.  $J / I$ is an ideal of the quotient ring $R / I$.
    
2.  $(R / I) \,/\, (J / I) \cong R / J$   

Here's an example. Let the tape be $R = \mathbb{Z}$. Choose $I = 12\mathbb{Z}$. Choose a wider seam that contains $I$: $J = 4\mathbb{Z}$ (every multiple of $12$ is a multiple of $4$, so $12\mathbb{Z} \subseteq 4\mathbb{Z}$).

Now compare the two ways of reducing the tape. The direct fold ($R / J$) gives $\{0, 1, 2, 3\}$.

Now for $(R / I) \,/\, (J / I)$. First, $R/I$ gives $\{0, 1, 2, \dots, 11\}$. And now for $J/I$, which is just $\{[0], [4], [8]\}$. Because $J$ is an ideal in the original ring, this subset of ticks forms a legitimate ideal inside the 12-hour ring.

Now glue the $R / I$, i.e., $\{0, 1, 2, \dots, 11\}$, together along the markers $\{0, 4, 8\}$. $0, 4, 8$ fuse into a single zero point. $1, 5, 9$ fuse together into $[1]$. $2, 6, 10$ fuse together into $[2]$. $3, 7, 11$ fuse together into $[3]$. So both sides of the isomorphism are the same.

Note that when we talk about quotienting and we have glued together a finite number of elements like above, how do we take the remainder; which number do we divide by? The answer is: we don't divide, we shift. Shifting is what taking remainders is. You do not need two separate mental procedures: coset shifting is the geometric definition of remainder arithmetic. In any quotient ring $R/K$, the cosets are generated by taking the base zero-set $K$ and shifting it across the ring: $x + K = \{x + k \mid k \in K\}$

These isomorphism theorems were first published by Emmy Noether. There is no standard agreement on the numbering of the above theorems.


## Groups

In ring theory, we studied systems with two operations (addition and multiplication). A ring models environments where things can be scaled, added, and multiplied, like polynomials or numbers.

Group theory strips away one operation. A group is a set with a single operation (denoted $\circ$). Why do this? Because in the physical world, the most fundamental mathematical object is not a "number," but an action or a transformation. Think of a rotation. You can do one rotation and then another. There isn't any other operation really. You cannot multiply two rotations. So we have just one operation which we call a composition: do one action, then do the next.

To really make this useful, you must be able to reverse actions, you must be able to do nothing, and a composition of operations should result in another recognizable operation. Accordingly, a group is defined as a set of elements with an associated operation, which is closed under that operation, is associative and has an identity. Every element must also have an inverse. Note that the inverse of a composition (usually a composition is also simply called a product) is $(gh)^{-1} = h^{-1}g^{-1}$, i.e., you invert in the reverse order in which you applied the operations. That makes sense. It is very much like the order in which you put on and take off shoes and socks.

Because a group has inverses, it obeys the Cancellation Laws: $gx = gy \implies x = y$.

Groups need not be commutative because actions in space generally depend on the order in which they are performed: rotating a book around the X-axis then the Y-axis yields a different orientation than Y then X. If commutativity holds ($ab = ba$), such groups are called Abelian. It is customary to use $+$ instead of $\circ$ in abelian groups.

**Example:** The set of all integers, with the operation $+$, is a group. In fact, if $R$ is any ring, we get a group with the operation $+$. It is an abelian group which is the same thing as saying it is the additive group of a ring. Conversely, given any abelian group $R$, where the group operation is written as $+$ and the identity as $0$, we obtain a ring (a zero ring) by defining the ring multiplication by the rule $ab = 0$ for all $a, b \in R$.

Similarly, the set of units of a ring with the operation of multiplication is a group. This is called the group of units of the ring $R$.

Similarly, with a field $F$, $F \setminus \{0\}$ is a group, the multiplicative group of $F$, written as $F^*$.

The set of invertible $n \times n$ matrices ($\det(A) \neq 0$) over a field $F$, with the operation of matrix multiplication, is a group, the General Linear group $GL(n, F)$.

A fundamental aspect behind groups is permutation, i.e., taking a set and permuting it or switching some of the elements. Every permutation can be written as a series of swaps between two elements. If there are an even number of these swaps, the parity of the permutation is even. Otherwise, it is odd.

If you take a set and write out all the possible permutations of its elements, these form a group called the symmetric group $S_n$. It has $n!$ elements.

Usually, a permutation is written out in the cycle notation, which tells us which element each element swaps with, until it returns to itself. A permutation may involve multiple cycles working together because it may not be possible for one element to permute into all other elements. If that were possible, we would have a single cycle. For example, $S_3$ consists of the six elements (in cycle notation): $(1)$ (the identity), $(1, 2, 3)$, $(1, 3, 2)$, $(1, 2)$, $(2, 3)$, and $(1, 3)$. A 2-cycle like (2 3) is a transposition.

A Cayley table is like an operation table with the group elements listed on top and to the left, horizontally and vertically. Each slot in the table is filled with the group element produced by the composition of those two elements. This means any row or column will contain only one instance of any element, and every element must be present. This is like Sudoku and is generally called a Latin Square.

Let $R$ be a ring. An automorphism of $R$ is an isomorphism $\theta : R \to R$; in other words, it is a permutation of $R$ which happens also to be a homomorphism satisfying $(x + y)\theta = x\theta + y\theta$ and $(xy)\theta = (x\theta)(y\theta)$. $\operatorname{Aut}(R)$ is the set of all automorphisms of $R$. It is a group: the automorphism group of $R$.

### The Rosetta Stone: Rings vs. Groups

The structural theorems we learned for rings were ported directly into group theory. Here is the exact translation dictionary between the two:

| Concept | Ring Theory (Additive + Multiplicative) | Group Theory (Multiplicative Only) |
| --- | --- | --- |
| **Base Environment** | Ring $R$ | Group $G$ |
| **Neutral Element** | Zero ($0$) | Identity ($1$ or $e$) |
| **Smaller enclosed system** | Subring $S$ | Subgroup $H$ |
| **One-step closure test** | $a - b \in S$ | $ab^{-1} \in H$ |
| **System that permits quotients** | Ideal $I$ (absorbs $r \cdot i$) | Normal Subgroup $N$ (absorbs $g^{-1}ng$) |
| **Equivalence bundles** | Cosets $x + I$ | Left/Right Cosets $gN$ or $Ng$ |
| **Quotient construction** | Factor Ring $R/I$ | Factor Group $G/N$ |
| **Homomorphism property** | $\phi(a+b) = \phi(a)+\phi(b)$ and $\phi(ab) = \phi(a)\phi(b)$ | $\phi(ab) = \phi(a)\phi(b)$ |
| **Homomorphism Kernel** | $\{r \in R \mid \phi(r) = 0\}$ | $\{g \in G \mid \phi(g) = 1\}$ |

### Subgroups & Normal Groups
Given a group, there's a few things we'd like to do. We'd like to see if we can break that group into pieces called subgroups, which would make it easier to understand and analyse its behaviour. The other thing we would like to do is to use that group and combine with other groups to form bigger groups. Let's look at the first item.

A subgroup is a subset of a larger group, with the same operation as the parent, which is also a group. As with rings, the simple condition to test whether a subset is a subgroup is to check inversion (subtraction in rings) and composition (addition in rings) in one shot with $gh^{-1} \in H$ for all $g$ and $h$ in $H$. Unlike rings though, every subgroup will contain the identity. (Well, even in rings, the additive identity is always present).

As with rings, we can partition a group by a subgroup $H$, creating bundles or cosets, which are equivalence classes. However, since commutativity need _not_ hold, we have right and left cosets: $Hg = \{xg \mid x \in H\}$ and $gH = \{gx \mid x \in H\}$, which are: execute any action of $H$, then some element $g$ of $G$; and execute $g$, then any action of $H$.

Because $gh \neq hg$ in general, $gH$ and $Hg$ will usually be completely different sets of actions. Your physical state after $gH$ is not the same as after $Hg$. However, the set of right and left cosets form a bijection with each other.

In a similar way to rings, we can say that $g_1$ and $g_2$ belong to the same coset by checking if the composition of their inverse (subtraction in rings) is in the subgroup, i.e., $g_1 \sim_L g_2$ if and only if $g_1^{-1}g_2 \in H$; and $g_1 \sim_R g_2$ if and only if $g_2g_1^{-1} \in H$.

Now what happens if you composed _every_ element of $G$ with every element of $H$? You would generate a set of all cosets for $H$. However, many different $g$'s will generate the exact same coset.

The order or cardinality of a group $G$, written $\vert{}G\vert{}$, is the number of elements in the group. This may be finite or infinite. Every coset of a subgroup $H$ contains exactly the same number of elements as $H$. Because cosets perfectly partition the group without overlapping, the total size of the group must be a clean multiple of the size of $H$. This is called the index of $H$ (often denoted $[G:H]$):

$$\vert{}G\vert{} = \vert{}H\vert{} \cdot [G:H]$$

This is a rigid quantization rule. A group of 15 elements physically cannot contain a self-contained subsystem of 4 elements.

In rings, we built a quotient ring $R/I$ by partitioning with an ideal. In groups, we build a quotient group $G/N$ by partitioning by a subgroup that is called a Normal Subgroup. We needed an ideal to ensure multiplication of any elements of equivalence classes always produce the same product. Similarly, we want to look at what properties a subgroup must have to allow multiplication of elements of cosets consistently. For example, $(a)(b) = ab$. Now $a$ is an element of the coset $aN$ and $b$ of $bN$, while $ab$ is an element of coset $(ab)N$. We want this relationship of belonging to this same coset $(ab)N$ to hold for the product of any elements of the first two cosets. In other words, we want:

$$(aN)(bN) = abN$$

To make $a \cdot N \cdot b \cdot N$ equal $abN$, you need to be able to swap the $N$ and the $b$ in the middle. You need the set $N$ to commute with the element $b$:

$$Nb = bN$$

So a normal subgroup commutes with every element of $G$. Its right and left cosets are the same. Another way of writing this is $g^{-1}Ng = N$ for every $g \in G$. Or in other words, $g^{-1}xg \in N$ for every $g$ in $G$ and every $x$ in $N$. As an aside, this means the true defining feature of an Abelian group is that every single subgroup inside it is a normal subgroup.

One difference from ideals in rings is that while the ideal has the absorption property, there is nothing like that in the normal subgroup. In a ring, absorption works perfectly because you are absorbing a second operation (multiplication) into a subgroup built on the first operation (addition). $r \cdot 0 = 0$, so multiplying by the additive identity doesn't force $r$ into the ideal. But in a group, you only have one operation. The only subgroup that absorbs the group operation is the entire group itself. However, the normal subgroup does absorb perspective shifts (which we will explain shortly). 

A geometric way of thinking of normal subgroups is through conjugation. Two elements $x$ and $y$ are conjugate if $y = g^{-1}xg$. This is the mathematical formulation of a change of perspective or a change of basis/coordinates. (We will encounter something very similar when we look at Representation Theory and change of basis later.)

Imagine you are standing in a room.

-   Let $x$ be the action: "Step one meter forward."
    
-   Let $g$ be the action: "Rotate your body 90 degrees to the right."

What does $g^{-1}xg$ mean?

1.  **$g^{-1}$:** Rotate 90 degrees to the left (undoing $g$).
    
2.  **$x$:** Step one meter forward.
    
3.  **$g$:** Rotate 90 degrees to the right.
    

If you execute $g^{-1}xg$, the net physical result is that you stepped one meter to the left. The action $x$ (stepping forward) was executed _from a different rotational perspective_.

Conjugate elements are exactly the same physical action, just operating on a different axis or starting state. In the symmetric group $S_n$, two permutations are conjugate if and only if they have the exact same cycle structure (e.g., both are swaps, or both are 3-cycles). They do the same "shape" of shuffling, just to different items.

Saying a subgroup $N$ is normal means that the collection of actions in $N$ is completely blind to orientation. If you take any internal action from $N$ and execute it from a twisted, alien perspective, the resulting physical action might be a different element than the one you started with, but it is guaranteed to still be an action belonging to the set $N$. The internal elements of $N$ might shuffle around under conjugation, but the boundaries of $N$ remain perfectly rigid across all reference frames.

This is very similar to the Lie Bracket in Differential Geometry. The Lie bracket $[X, Y]$ of two vector fields measures the failure of their flows to commute. You flow along $X$, then $Y$, then $-X$, then $-Y$. If the space is flat and the fields are independent, you form a closed loop and return to the origin. If they don't commute, the bracket measures the geometric gap where the loop failed to close.

In discrete group theory, this exact concept is called the Group Commutator, and it is written:

$$[g, h] = g^{-1}h^{-1}gh$$

It is checking whether the inverse of a raw action is cancelled by a conjugated version of the action:

$$[g, h] = g^{-1} \cdot (h^{-1}gh)$$

It takes the inverse of $g$, and multiplies it by $g$ _as viewed from the orientation of $h$_. If changing the orientation to $h$ doesn't alter how $g$ behaves, then $h^{-1}gh = g$, and the commutator collapses: $g^{-1}g = 1$. The loop closes perfectly. THis is the defining feature of the centralizer group (more on that later). 

If instead, in a finite group $G$ with a subgroup $N$, we have: $[G, N] \subseteq N$, then $N$ is a normal subgroup of $G$ i.e. it can absorb the group commutator with any external element

Another way to think of cosets is as macroscopic actions, while individual elements of the coset are microscopic actions. For example, "Drive 50 miles North" vs "drift 1 inch left".

A coset like $aN$ is a "fuzzy" command. It means: Execute the macro-jump $a$, and then suffer some random microscopic error from the set $N$. For the quotient $G/N$ to form a valid, functioning group, you need to be able to string these fuzzy macro-commands together predictably. If you execute $aN$ and then execute $bN$, the final macroscopic destination must be strictly and perfectly $(ab)N$. The random microscopic errors cannot be allowed to derail the macro-trajectory. If normality fails, the quotient group collapses because $(aN)(bN)$ no longer lands neatly inside $(ab)N$.

Let's look at the physical timeline of executing $(aN)$ followed by $(bN)$:

1.  Execute macro-jump $a$.
    
2.  Suffer a random micro-error $n_1$.
    
3.  Execute macro-jump $b$.
    
4.  Suffer a random micro-error $n_2$.    

To guarantee that this sequence is indistinguishable from the clean macroscopic command $(ab)N$, we need to prove that the sequence $[a \to n_1 \to b \to n_2]$ can be perfectly rewritten as $[a \to b \to \text{some final micro-error}]$.

We need the physical state of doing $[n_1 \to b]$ to be identical to doing $[b \to \text{some new error } n_3]$.

Algebraically, this is:

$$n_1 b = b n_3$$

If we multiply both sides by $b^{-1}$, we get:

$$b^{-1} n_1 b = n_3$$

This is the normality condition. We want our final error to fall in the same coset, because then we can somehow figure out how to correct for the error. If it fell into another coset, because we don't know what the error is and whether it even occurred, we wouldn't know whether we need to stay in this same new coset or actually shift back to some other coset.

For any subgroup $H$ of $G$ and any element $g$ of $G$, the conjugate set $g^{-1}hg$ for $h \in H$ is a subgroup of $G$. This means if there is only one subgroup of a certain order, it must be normal.

#### Conditions Implying a Normal Subgroups
Each of the following conditions implies that $H$ is a normal subgroup:

a.) $G$ is abelian;

b.) $H$ is finite and is the only subgroup of $G$ of its order;

c.) $H$ has index 2 in $G$.

We can generalize this. If $G$ is a finite group and $H \le G$ is a subgroup such that $[G : H] = p$, where $p$ is the smallest prime dividing $\vert{}G\vert{}$, then $H \trianglelefteq G$.

When $p = 2$, this reduces directly to the index 2 property: $2$ is the smallest prime dividing any even group order, so index 2 subgroups are always normal.

**Proof:** Let $\Omega$ be the set of left cosets of $H$ in $G$:

$$\Omega = G/H = \{xH \mid x \in G\}$$

Since $[G : H] = p$, the set has size $\vert{}\Omega\vert{} = p$.

Let $G$ act on $\Omega$ by left multiplication:

$$g \cdot (xH) = (gx)H$$

Every group action of $G$ on a set of size $p$ is equivalent to a group homomorphism into the symmetric group on $p$ elements:

$$\phi: G \longrightarrow \text{Sym}(\Omega) \cong S_p$$

The image of $G$ under this map, $\phi(G)$, is a subgroup of $S_p$:

$$\phi(G) \le S_p$$

Let $K = \ker(\phi)$.

By the First Isomorphism Theorem:

$$G/K \cong \phi(G) \le S_p$$

Because $K$ is the kernel of a homomorphism, $K$ is automatically a normal subgroup of $G$ ($K \trianglelefteq G$).

What elements live in $K$?

$$K = \{g \in G \mid g \cdot (xH) = xH \quad \forall x \in G\}$$

Setting $x = 1$ gives:

$$g \cdot (1H) = 1H \implies gH = H \implies g \in H$$

Because every element of $K$ must belong to $H$, we have:

$$K \le H \le G$$

$K$ is a normal subgroup of $G$ contained entirely inside $H$ (in fact, $K$ is the core of $H$, $\text{Core}_G(H) = \bigcap_{g \in G} gHg^{-1}$).

Now determine the index $[G : K]$:

By Lagrange's Theorem:

$$[G : K] = \frac{\vert{}G\vert{}}{\vert{}K\vert{}} \quad \text{divides } \vert{}G\vert{}$$
    
Because $G/K$ is isomorphic to a subgroup of $S_p$, by Lagrange's Theorem:

$$\vert{}G/K\vert{} = [G : K] \quad \text{divides } \vert{}S_p\vert{} = p!$$
    
$$[G : K] = [G : H] \cdot [H : K] = p \cdot [H : K]$$
    
Divide both conditions by $p$:

$[H : K] = \frac{[G : K]}{p}$ must divide $\frac{\vert{}G\vert{}}{p}$.
    
$[H : K]$ must also divide $\frac{p!}{p} = (p - 1)!$.
    
Suppose $[H : K] > 1$.

Then there exists some prime $q$ that divides $[H : K]$:

Because $[H : K]$ divides $(p - 1)!$, all prime factors of $[H : K]$ must be strictly less than $p$:
    
$$q \le p - 1 < p$$
    
But $[H : K]$ also divides $\vert{}G\vert{}$, which means $q$ must divide $\vert{}G\vert{}$.

This forces $q$ to be a prime divisor of $\vert{}G\vert{}$ with:

$$q < p$$

This contradicts the initial condition that $p$ is the smallest prime dividing $\vert{}G\vert{}$.

No such prime $q$ can exist. Therefore:

$$[H : K] = 1 \implies H = K$$

Since $K$ was proven to be normal in $G$ in Step 2:

$$H \trianglelefteq G$$

### Centralizers and the Center

If conjugacy means viewing an action from a different perspective, we can ask: What if changing the perspective doesn't change the action?

$$g^{-1}xg = x \implies xg = gx$$

This is a stronger condition than just being normal. If this equation holds, the action $x$ commutes with the perspective shift $g$. This leads to two critical definitions:

**The Centralizer of an element $x$, denoted $C_G(x)$:** This is the set of all perspective shifts $g$ that leave the action $x$ completely unchanged. It measures how "symmetric" the action $x$ is against the rest of the group. The intersection of the centralizers of all elements in the group is the center of the group $Z(G)$. It contains all elements of $G$ which are unaffected by conjugation with all other elements of $G$. $Z(G) = \{x \in G \mid xg = gx \text{ for all } g \in G\}$. Because $g^{-1}Z(G)g = Z(G)$, the center is always a normal subgroup.

There is a bijection between the conjugacy class of an element $x$ of $G$ and the set of cosets of the centralizer $C_G(x)$ in $G$. Because of this bijection, the size of the conjugacy class of $x$ is exactly equal to the index of its centralizer: $\vert{}Cl(x)\vert{} = [G : C_G(x)] = \frac{\vert{}G\vert{}}{\vert{}C_G(x)\vert{}}$. This is a direct application of the Orbit-Stabilizer Theorem, where the group acts on itself by conjugation.

Since conjugacy classes perfectly partition the group, the sum of the sizes of all distinct conjugacy classes must equal the total size of the group. This is called the class equation. Elements in the center of the group, $Z(G)$, have conjugacy classes of size 1 (they commute with everything, so they only conjugate to themselves). Grouping these together, we get the standard Class Equation:

$$\vert{}G\vert{} = \vert{}Z(G)\vert{} + \sum_{i=1}^k [G : C_G(x_i)]$$

where $x_i$ are representatives of the distinct conjugacy classes that have a size greater than 1 (i.e., elements not in the center).

Dividing this entire equation by the group order $\vert{}G\vert{}$ yields the fractional form you were building towards in your placeholder:

$$1 = \frac{\vert{}Z(G)\vert{}}{\vert{}G\vert{}} + \sum_{i=1}^k \frac{1}{\vert{}C_G(x_i)\vert{}}$$

This leads to the **5/8 Theorem (Probability of Commuting):** The fractional form of the class equation is heavily used in probabilistic group theory. Using this equation, you can prove that if you pick two random elements from a non-abelian group, the probability that they commute can never be higher than $5/8$.

Furthermore, conjugacy classes make finding normal subgroups much easier. Given a subgroup $H$, let's say we want to check if it is a normal subgroup of $G$. Due to the nature of normality, if $H$ contains one element $x$ of a conjugacy class, it must contain the entire conjugacy class. Remember the definition: for $H$ to be normal, $g^{-1}xg$ must be in $H$ for every $g \in G$. But the set of all $g^{-1}xg$ as you vary $g$ is exactly the definition of the conjugacy class of $x$! Therefore, a normal subgroup must be built perfectly out of complete, unbroken conjugacy classes.

Additionally, the identity must be present in $H$ (since the identity is a subgroup, and its conjugacy class has size 1). And by Lagrange's Theorem, the order of $H$ must divide the order of $G$. These add multiple constraints that we can make use of.

For example, the class equation for $A_4$ (the alternating group of degree 4) is:

$$1 + 3 + 4 + 4 = 12$$

The total order of the group is 12. There is only one conjugacy class with a single element, and so that must be the identity.

The possible size of a non-trivial proper normal subgroup is only $1+3 = 4$. Adding any of the other conjugacy classes will mean the order of the proposed subgroup is no longer a divisor of 12. ($1+4 = 5$, $1+4+4 = 9$, $1+3+4 = 8$ — none of these divide 12). So, $A_4$ has exactly one proper non-trivial normal subgroup, and it has order 4.

The same logic is the standard way to prove that $A_5$ (and by extension, the unsolvability of the quintic polynomial) is a Simple Group. The class equation for $A_5$ is $1 + 15 + 20 + 12 + 12 = 60$. If you try to add $1$ to any combination of those numbers, you will never find a sum that perfectly divides $60$. Therefore, $A_5$ has no normal subgroups.

### Homomorphisms and the Isomorphism Theorems

A group homomorphism $\phi: G \to H$ preserves the single group operation:

$$\phi(ab) = \phi(a)\phi(b)$$

Because there is no separate addition and multiplication, the mapping naturally forces the identity to map to the identity ($\phi(1_G) = 1_H$) and inverses to map to inverses ($\phi(a^{-1}) = \phi(a)^{-1}$).

The core theorems map perfectly to their ring counterparts, merely swapping the additive vocabulary for multiplicative vocabulary:

**The Kernel:** In rings, the kernel is what maps to $0$. In groups, the kernel maps to the identity element $1$:

$$\ker(\phi) = \{g \in G \mid \phi(g) = 1_H\}$$

Just as a ring kernel is always an ideal, a group kernel is always a normal subgroup. It absorbs perspective shifts ($g^{-1}kg \in \ker(\phi)$).

**First Isomorphism Theorem:** $G/\ker(\phi) \cong \operatorname{im}(\phi)$.
The bundles (cosets) of the kernel multiply consistently to form a quotient group that is structurally identical to the image in the target group.

**Second Isomorphism Theorem:** $(HN)/N \cong H/(H \cap N)$.
Let $N$ be a normal subgroup (acting like an ideal) and $H$ an ordinary subgroup (acting like a subring). Expanding $H$ by $N$ and modding out by $N$ gives the same geometric structure as restricting $N$ to its overlap with $H$ and modding out $H$ by that overlap.

**Third Isomorphism Theorem:** $(G/N)/(M/N) \cong G/M$.
For normal subgroups $N \subseteq M$, folding the group down in stages (first by $N$, then by $M/N$) is identical to folding the group by $M$ directly.

**Fourth Isomorphism Theorem:** Let $G$ be a group and $N$ a normal subgroup ($N \trianglelefteq G$). Let $\pi: G \to G/N$ be the canonical projection defined by $\pi(g) = gN$.

Consider two collections of subgroups:

The Upper Collection: Subgroups of $G$ that fully contain $N$:

$\mathcal{S}_N(G) = \{H \le G \mid N \subseteq H\}$$
    
The Lower Collection: All subgroups of the quotient group $G/N$:

$$\mathcal{S}(G/N) = \{\overline{H} \le G/N\}$$
    
The theorem states that the following forward map $\Phi$ is a bijection:

$$\Phi: \mathcal{S}_N(G) \longrightarrow \mathcal{S}(G/N)$$

$$\Phi(H) = H/N = \{hN \mid h \in H\}$$

The inverse map $\Phi^{-1}$ pulls subgroups back via the canonical projection $\pi$:

$$\Phi^{-1}(\overline{H}) = \pi^{-1}(\overline{H}) = \{g \in G \mid gN \in \overline{H}\}$$

For any two subgroups $H, K \in \mathcal{S}_N(G)$:

$$H \subseteq K \iff H/N \subseteq K/N$$
    
$$[K : H] = [K/N : H/N]$$
    
$$[G : H] = [(G/N) : (H/N)]$$
    
$$H \trianglelefteq G \iff H/N \trianglelefteq G/N$$

$$(H \cap K)/N = (H/N) \cap (K/N)$$

$$\langle H, K \rangle / N = \langle H/N, K/N \rangle$$

So this is telling us that the normal subgroup is kind of like an inflection point in the group. The topology of the group when you project down with a normal subgroup is the same as when you build out with it.

In modern geometry and algebra, mathematicians describe this property by calling the sequence:

$$1 \longrightarrow N \hookrightarrow G \stackrel{\pi}{\longrightarrow} G/N \longrightarrow 1$$

a fibration or an exact sequence.

Everything strictly inside $N$ represents internal degrees of freedom that get crushed to a single point by the projection map $\pi$. If a subgroup $K$ sits inside $N$ ($K \subset N$), the quotient map cannot resolve it independently—it collapses into the identity pixel.

For the entire universe of subgroups sitting above $N$ ($N \subseteq H \subseteq G$), the projection map preserves the structural arrangement without distortion. The algebraic "topology" of how these larger subgroups nest, intersect, and connect to each other is perfectly copied down into $G/N$.

So in a way N reproduces G itself, minus the details contained within N. The quotient group $G/N$ is $G$ viewed through a low-pass filter. High frequencies (fine details) is everything happening strictly inside $N$. This includes internal shifts, local commutators, and microscopic permutations. Low frequencies (global shape) are the macroscopic routes between different cosets. 

If $N$ were merely a subgroup and not normal, shifting perspective by some macro-jump $g$ would twist the fiber $N$ into a different orientation ($g^{-1}Ng \neq N$). In signal processing terms, that would mean the low-pass filter produces phase distortion.

 Why we call them fibers and fibration? The base space ($G/N$) is the low-resolution map. Every element in $G/N$ is a single "point" on the spine of the map. The point on the spine corresponding to the identity element of $G/N$ has a bristle sticking out of it. That bristle is made of exactly the elements inside the normal subgroup $N$. If you pick any other point on the spine (a macroscopic coordinate like $gN$), the bristle sticking out of it is the coset $gN$.

The word "fibration" implies that this structure is perfectly uniform, smooth, and untangled. If you map a random, unstructured set of data down to a smaller set, the fibers will be chaotic. The fiber over point A might contain 100 elements, the fiber over point B might contain 2 elements, and the fibers might twist unpredictably. Because $N$ is a normal subgroup, the group $G$ forms a perfect, rigid fibration. Every single fiber (coset) has the exact same number of elements. They are all perfect geometric copies of $N$. The cosets strictly partition the group. No two fibers ever cross or share an element. Because $g^{-1}Ng = N$, the fibers don't "shear" when you multiply them. They don't jump ship to another point on the spine.

### Sylow's Theorems and The Anatomy of Prime Blocks

In our quest to break larger groups into simpler constituents, taking some inspiration from the prime factorization of integers is helpful. Prime factors are fundamental and unique components of an integer. In group theory, the $p$-groups play that role where $p$ is a prime number. These groups are highly layered and come with several restrictive properties, such as their order and how they relate to the larger group's order, which helps us put very tight constraints on how a large group can split into smaller one. These tight constraints help us reduce our search space of the smaller constituent groups so we can find them sooner. 

Let's look at their nature for a bit A $p$-group is a group whose entire size is a power of a single prime ($p^a$). Because they are made of a single prime "substance," they possess incredibly rigid, crystalline internal symmetries that mixed-mass groups do not.

We have Cauchy’s Theorem, which says if a prime number $p$ divides the order of a finite group $G$, then $G$ contains an element of order $p$, i.e., it has a cyclic subgroup of order $p$.

The defining feature of any $p$-group is that its center is never trivial ($Z(P) \ne \{1\}$). There is always at least one non-identity action that commutes with absolutely everything else in the group. Because the center is non-empty, you can safely quotient the group by its center, creating a smaller $p$-group, which also has a non-trivial center, and repeat the process. This guarantees that $p$-groups can be thoroughly layered and perfectly dismantled down to the identity.

So, if $G$ is a group of order $p^a m$, where $p$ is a prime not dividing $m$, then for $0 \le i \le a$, $G$ contains a subgroup of order $p^i$. Furthermore, if $i < a$, then any subgroup of order $p^i$ is contained normally in a subgroup of order $p^{i+1}$. This means you can construct a nested sequence of subgroups $P_0 \subset P_1 \subset \dots \subset P_a$ such that $\vert{}P_i\vert{} = p^i$, and each subgroup is a normal subgroup of the next one in the chain ($P_i \triangleleft P_{i+1}$).

Sylow's theorems establish important rules about these $p$-groups. Lagrange’s Theorem is a restrictive law: it tells you that the order of a subgroup must divide the order of the group. If your group has 12 elements, you cannot have a subgroup of size 5. But Lagrange provides no positive guarantees. Just because 6 divides 12 does not mean a subgroup of size 6 actually exists (and in the alternating group $A_4$, it doesn't).

Sylow’s Theorems provide the positive guarantees, but they only work for prime powers. They are the structural beams of group theory.

If the order of a group is $p^a \cdot m$ (where $p$ is a prime that doesn't divide $m$), Sylow’s First Theorem guarantees that a subgroup of size $p^a$ must exist. These maximal prime-power blocks are called Sylow $p$-subgroups.

**The Second Theorem (Conjugacy):** All Sylow $p$-subgroups are conjugate. $P_1 = g^{-1}Pg$.

**The Third Sylow Theorem (Counting):** The number of Sylow $p$-subgroups (which are the maximal $p$-subgroups of order $p^a$) is $\equiv 1 \pmod p$. That is, if the order of the parent group is $\vert{}G\vert{} = n = p^a m$ (where $p$ does not divide $m$), then the number of these subgroups, denoted as $n_p$, must leave a remainder of $1$ when divided by $p$ (meaning $n_p = 1 + kp$ for some integer $k$). Additionally, $n_p$ must be a divisor of $m$ (and therefore a divisor of the total group order $n$).

By guaranteeing the existence of these prime-power subgroups, we can disassemble any unknown finite group into its fundamental $p$-group components, study them in isolation, and then figure out how they interlock.

The Third Sylow Theorem is the primary weapon used to prove that a group is _not_ simple. If your constraints ($n_p \equiv 1 \pmod p$ and $n_p \mid m$) leave $1$ as the only mathematically possible value for $n_p$, it means there is exactly _one_ Sylow $p$-subgroup. Because it is unique, it is invariant under conjugation, which guarantees that it is a Normal Subgroup!
    
When you scale up to studying finite simple groups like $PSL(2,7)$ or $G_2(q)$ where $q$ is prime, this theorem dictates the structural "skeleton" of the group. For these groups to remain simple, the Sylow counts ($n_2$, $n_3$, $n_7$) must strictly be greater than 1, forcing multiple conjugate subgroups to perfectly interlock without any of them becoming normal.

### Types of Groups

Understanding the different types of groups gives us more insights into breaking a larger group into smaller pieces and then studying how those smaller pieces behave. 

We already saw the symmetric groups $S_n$, which are the groups of all possible permutations. Let's look at a few more types of groups.

**Cyclic Groups ($C_n$):** A group generated entirely by the powers of a single element $g$. Every subgroup of a cyclic group is also cyclic. A finite group G of order n is cyclic if and only if it contains an element of order $n$. For each divisor $m$ of $n$, there is a unique subgroup of G of order $m$, which is a cyclic group generated by $gn/m$.

This leads us to Cauchy's Theorem. Let $G$ be a finite group, and $p$ a prime number which divides the order of $G$. Then $G$ contains an element of order $p$.

**The Alternating Group ($A_n$) and Parity:** On the symmetric group $S_n$, every complex shuffle can be broken down into a sequence of simple 2-item swaps (transpositions). While there are many ways to build the same shuffle, the parity (whether it takes an even or an odd number of swaps) is an unchangeable physical invariant of that shuffle.

The map sending a permutation to its parity ($+1$ for even, $-1$ for odd) is a homomorphism from $S_n$ to the multiplicative group $\{+1, -1\}$. The kernel of this map is the set of all even permutations. This kernel is a normal subgroup called the Alternating Group ($A_n$). Because the target group has size 2, the kernel splits the original group exactly in half, meaning $\vert{}A_n\vert{} = n! / 2$.

**Symmetry and Dihedral Groups ($D_{2n}$):** These groups represent the rigid physical symmetries of an $n$-sided regular polygon. There are $n$ rotations (forming a cyclic, normal subgroup). There are $n$ reflections (axes of symmetry). Multiplying a rotation by a reflection flips the direction of the rotation ($r \cdot f = f \cdot r^{-1}$). This demonstrates why physical symmetries are strictly non-commutative.

**Simple Groups (The Atoms of Symmetry):** You've studied prime numbers (atoms of integers) and irreducible polynomials (atoms of rings). In groups, the "atoms" are groups that have _no_ normal subgroups whatsoever. These are called Simple Groups. Because they have no normal subgroups, they cannot be quotiented or broken down any further. The Alternating Group $A_n$ (for $n \geq 5$) is simple!

According to Cayley's theorem, every group is in fact a subgroup of a permutation group. The intuition is that any group element $g$ can be viewed as a machine that shuffles the group itself. If you multiply every element in the group by $g$, you simply rearrange the elements. Therefore, $g$ is literally a permutation. There are no abstract groups; there are only permutation groups disguised by abstract notation.

### The Jordan-Hölder Theorem (The Periodic Table of Groups)

If groups are molecules, how do we find their atoms? You take a group $G$ and find a maximal normal subgroup $G_1$ (a seam that allows a clean quotient). You split $G$ into the quotient group $G/G_1$ and the remainder $G_1$. You then take $G_1$ and smash it again along its own maximal normal subgroup $G_2$. You repeat this until you are left with pieces that have no normal subgroups at all.

These unbreakable, indivisible pieces are called Simple Groups. The sequence of smashes is called a Composition Series.

The Jordan-Hölder Theorem is the Fundamental Theorem of Arithmetic for groups. It proves that no matter what normal subgroups you choose to smash along—no matter what path you take to dismantle the group—when you sweep up the simple groups left on the floor at the end, you will always have the exact same list of simple groups.

This theorem broke the study of all finite groups into two distinct massive research programs:

1. **The Classification Problem:** Find and catalogue every single Simple Group in the universe (the periodic table of elements).

2. **The Extension Problem:** Figure out how to chemically bond those simple groups back together.

When we smash groups down to their indivisible "atoms" via the Jordan-Hölder theorem, the non-abelian atoms fall into three buckets:

**The Alternating Groups ($A_n$ for $n \ge 5$):** The group of all even permutations of $n$ items. We can proves $A_5$ is simple because its conjugacy classes (sizes 1, 15, 20, 12, 12) cannot be summed to divide 60. There is no normal subgroup to quotient out.

**Groups of Lie Type (e.g., $PSL(n, q)$):** These are matrix groups over finite fields. If you take all $n \times n$ matrices with determinant 1 over a finite field (the Special Linear group), and quotient out the scalar matrices or the multiples of Identity, (the Center), you get the Projective Special Linear group. Except for two exceptions, these are always simple.

**The 26 Sporadic Groups:** These are the anomalies. They do not fit into any infinite family. They are isolated, highly symmetrical geometric monsters that just happen to exist. The smallest has 7920 elements. The largest, the "Monster Group," has $\sim 10^{54}$ elements and represents the symmetries of a 196,883-dimensional space.

When you run a group through a composition series, the "atoms" you are left with fall into two categories:

1. **Abelian Simple Groups:** These are just the cyclic groups of prime order ($C_2, C_3, C_5$). They are flat, 1-dimensional, commutative gears.

2. **Non-Abelian Simple Groups:** These are massively complex, multi-dimensional, interwoven structures (like the Alternating Group $A_5$ or the Sporadic groups).

If a group shatters entirely into 1D prime cyclic groups ($C_p$), the group is called Soluble (or Solvable). A soluble group can be highly non-commutative overall, but its non-commutativity is superficial. You can measure this using commutators: $[x, y] = x^{-1}y^{-1}xy$. 

If you gather all these errors into a subgroup (the Derived Subgroup), and then measure the errors of the errors, and so on, a Soluble group's errors will eventually vanish to $1$. In contrast, a non-abelian simple group like $A_5$ is purely non-commutative: the errors of $A_5$ are the entirety of $A_5$.

### Group Actions and the Orbit-Stabilizer Theorem

A group can be treated as a closed universe of abstract elements. But historically, groups were invented to do things—to shuffle roots, rotate polyhedra, or permute sets. This is the idea of a Group Action. If $\Omega$ is the set that $G$ acts on, then $\operatorname{deg}(G, \Omega) = \vert{}\Omega\vert{}$ is called the degree of the action.

When you apply a group to a physical object or set of elements, two structural questions immediately arise for any specific point/element of the set $x$:

Where can $x$ travel? Which other elements of the set can $x$ be permuted into under the action of $G$. Or alternatively, which elements of the set look the same from the perspective of the group acting on the set. The set of all possible destinations for $x$ under the group's control is called its Orbit.

The other question is, what part of $G$ leaves $x$ completely alone? The set of all group commands that leave $x$ perfectly stationary is a subgroup called the Stabilizer ($G_x$).

$G_x$ is generally not a normal subgroup of $G$, except when G is regular i.e. sharply 1-transitive and $G_x$ is therefore just the identity element. However, $G_x$ partitions $G$ into a set of cosets $G / G_x = \{ g G_x \mid g \in G \}$, which is isomorphic to the orbit of $x$ under $G$ action. Essentially, the "representative" of each coset can be seen as the point that $x$ shifts to during its orbit traversal. Every element $g$ inside the coset $g G_x$ moves the base point $x$ to the exact same target.

The stabilizers of elements of the set are conjugates $G_\beta = g G_\alpha g^{-1}$ when $g(\alpha) = \beta$ i.e. conjugacy classes of stabilizers are given by the different orbits. If $G$ acts transitively, all stabilizers are conjugates of each other because there is only one orbit.

For transitive actions, since conjugate subgroups are isomorphic, every point stabilizer has the exact same order:

$$\vert{}G_\alpha\vert{} = \vert{}G_\beta\vert{} = \frac{\vert{}G\vert{}}{\vert{}\Omega\vert{}}$$

**Aside:** Note the difference between the stabilizer and the centralizer, which seem to do similar things. The stabilizer is applied when a group $G$ acts on an arbitrary set $\Omega$. The centralizer is applied to elements within the group $G$ itself. The centralizer of an element $a \in G$ is the subgroup of all elements in $G$ that commute with $a$.

---

A more general rule is given in the Orbit-Stabilizer theorem below. 

For transitive actions, the elements of $G$ that fix every point in $\Omega$ (the kernel of the action) is the intersection of all point stabilizers:

$$\ker(\phi) = \bigcap_{\alpha \in \Omega} G_\alpha = \bigcap_{g \in G} g G_\alpha g^{-1} = \text{Core}_G(G_\alpha)$$

This is the largest normal subgroup of $G$ contained inside $G_\alpha$.
    
If the action is faithful (no non-identity element fixes every point), then $\text{Core}_G(G_\alpha) = \{e\}$, meaning the intersection of all these conjugate subgroups collapses to the identity.

#### Orbit-Stabilizer Theorem & Orbit-Counting Lemma
This allows us to state the Orbit-Stabilizer Theorem, a fundamental law of conservation of information. It states that for any point $x$:

$$\vert{}\text{Orbit of } x\vert{} \times \vert{}\text{Stabilizer of } x\vert{} = \vert{}G\vert{}$$

From this we can then write the Orbit-Counting Lemma which is about averaging the symmetries. If a group $G$ acts on a physical object (like the rotations of a cube), how do we count the number of fundamentally distinct configurations (orbits) it can create?

For example, if you paint the faces of a cube with 3 colours, there are $3^6 = 729$ total colourings. But if you can just rotate one colouring to look exactly like another, they belong to the same orbit. How many distinct orbits (unique painted cubes) actually exist?

The Orbit-Counting Lemma (often called Burnside's Lemma) provides a shortcut using fixed points. Instead of trying to track every colouring as it spins through space, you ask each of the 24 rotational actions of the cube: "How many of the 729 colourings do you leave perfectly unchanged (fixed)?"

* The identity action fixes all 729.
* A 90-degree face rotation only fixes colorings where the 4 spinning side-faces are painted the exact same color.

**The Lemma states:** The number of unique orbits is the average number of fixed points across all group actions.

$$\text{Number of Orbits} = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \text{fix}(g)$$

By averaging the fixed points of the 24 cube rotations, the 729 colourings become 57 uniquely painted cubes.

The proof of Burnside's Lemma uses a standard combinatorial trick. When we need to count something that involves two different sets of elements, we create an edge between each of the elements of the two sets that are linked to each other across sets, and then count the number of elements with an incidence in the two sets and get an equality.

Let the two sets be $G$ and $\Omega$. Define an edge between $g \in G$ and $x \in \Omega$ if and only if $g \cdot x = x$. We count the total number of edges $E$ in two ways:

1.  **Summing across $G$:** For each $g \in G$, the number of edges incident to $g$ is the number of points in $\Omega$ fixed by $g$, namely $\vert{}\text{fix}(g)\vert{}$. Summing over all $g$:
    
    $$E = \sum_{g \in G} \vert{}\text{fix}(g)\vert{}$$
    
2.  **Summing across $\Omega$:** For each $x \in \Omega$, the number of edges incident to $x$ is the number of group elements in $G$ that fix $x$, which is the size of its stabilizer $\vert{}G_x\vert{}$. Summing over all $x$:
    
    $$E = \sum_{x \in \Omega} \vert{}G_x\vert{}$$
    

Equating the two counts gives:

$$\sum_{g \in G} \vert{}\text{fix}(g)\vert{} = \sum_{x \in \Omega} \vert{}G_x\vert{}$$

Using the Orbit-Stabilizer Theorem ($\vert{}G_x\vert{} = \frac{\vert{}G\vert{}}{\vert{}\mathcal{O}_x\vert{}}$):

$$\sum_{x \in \Omega} \vert{}G_x\vert{} = \sum_{\text{orbits } \mathcal{O}} \sum_{x \in \mathcal{O}} \frac{\vert{}G\vert{}}{\vert{}\mathcal{O}\vert{}} = \sum_{\text{orbits } \mathcal{O}} \vert{}G\vert{} = \vert{}G\vert{} \cdot (\text{number of orbits})$$

Dividing both sides by $\vert{}G\vert{}$ produces Burnside's Lemma:

$$\text{number of orbits} = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \vert{}\text{fix}(g)\vert{}$$

There is another way to look at this using a permutation representation. The principal character (more commonly called the trivial character, and denoted by $\mathbf{1}$ or $1_G$) is the character corresponding to the 1-dimensional trivial representation of $G$. Specifically, it assigns the value $1$ to every single element of the group:

$$\mathbf{1}(g) = 1 \quad \text{for all } g \in G$$
    
Because $\mathbf{1}(g) = 1$, the inner product of any character $\chi$ with the principal character simplifies directly to the arithmetic average of $\chi$ over the group:
    
$$\langle \chi, \mathbf{1} \rangle = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \chi(g) \overline{\mathbf{1}(g)} = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \chi(g)$$

For the permutation character $\pi$:

$$\langle \pi, \mathbf{1} \rangle = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \pi(g) = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \text{fix}(g)$$

since the diagonal elements of a permutation representation simply record all elements of the set fixed by that group element $g$.

Since the irreducible characters $\text{Irr}(G)$ form an orthonormal basis under this inner product, the multiplicity $m_{\mathbf{1}}$ of the principal character in the decomposition $\pi = \sum_{\chi \in \text{Irr}(G)} m_\chi \chi$ is given by:

$$m_{\mathbf{1}} = \langle \pi, \mathbf{1} \rangle$$

By Burnside's Lemma (Orbit-Counting Lemma), this integer is precisely the number of orbits of $G$ on the set $\Omega$.

#### Jordan's Theorem
A direct consequence of this averaging is Jordan's Theorem. If a group acts transitively i.e. can move any point to any other point of the set, there must exist at least one action in the group that fixes nothing. If there is a transitive action, there is only 1 orbit. Because the identity action fixes everything, it heavily skews the average upward. For the average number of fixed points to drop all the way down to 1, some action needs to fix nothing.

#### Transitive, Regular & $k$-transitive Actions

Now that we have seen transitive action, we can look at free actions. An action of a group $G$ on a set $\Omega$ is free if no non-identity element fixes any point in $\Omega$.

$$\text{Stab}_G(x) = \{e\} \quad \forall x \in \Omega$$

Equivalently:

$$\text{If } x \cdot g = x \text{ for any } x \in \Omega, \quad \text{then } g = e$$

In a free action, group elements move points without "pinning" anything down. There can be multiple separate orbits. But inside every single orbit, the elements of $G$ map points one-to-one without collisions.
    
By the Orbit-Stabilizer Theorem, every orbit $\mathcal{O}_x$ must have an exact size equal to $\vert{}G\vert{}$:

$$\vert{}\mathcal{O}_x\vert{} = \frac{\vert{}G\vert{}}{\vert{}\text{Stab}_G(x)\vert{}} = \frac{\vert{}G\vert{}}{1} = \vert{}G\vert{}$$

Therefore, in any free action, the total size of the set $\vert{}\Omega\vert{}$ must be an exact multiple of the group size: $\vert{}\Omega\vert{} = k \cdot \vert{}G\vert{}$, where $k$ is the number of orbits.
    
An action is regular (also called simply transitive) if it is both transitive and free. There is only one orbit and the stabilizer is trivial. This means that for any pair of points $x, y \in \Omega$, there exists exactly one element $g \in G$ such that: $x \cdot g = y$.

Because it is transitive, $\vert{}\mathcal{O}_x\vert{} = \vert{}\Omega\vert{}$. Because it is free, $\vert{}\mathcal{O}_x\vert{} = \vert{}G\vert{}$. Therefore:

$$\vert{}\Omega\vert{} = \vert{}G\vert{}$$

The canonical example of a regular action is a group acting on itself by left (or right) multiplication: $g \cdot x = gx$. Every group element acts as a unique permutation of the group elements, with no fixed points other than the identity element doing nothing.

A stronger requirement than transitivity, which implies that a group has much more flexibility and symmetry, is $k$-transitivity for some integer $k$, where standard transitivity is the special case with $k=1$. Given any two ordered $k$-tuples of _distinct_ elements $(a_1, \dots, a_k)$ and $(b_1, \dots, b_k)$, there exists some $g \in G$ such that $g \cdot a_i = b_i$ for all $i = 1, \dots, k$. Note that we need the action to respect the order of the tuples. One obvious example of this is the symmetric group $S_n$ of degree $n$, which contains every permutation of $n$ elements and so fulfills the condition of $n$-transitivity.

The action is sharply $k$-transitive if there is exactly one element $g \in G$ that takes the first $k$-tuple to the second $k$-tuple. The pointwise stabilizer of every $k$-tuple from the parent set is the identity subgroup in such cases. A sharply 1-transitive group is a regular group.

The reason $k$-transitivity represents a dramatic leap in internal symmetry is revealed through point stabilizers:

An action of $G$ on $\Omega$ is $k$-transitive if and only if:

$G$ is transitive on $\Omega$, AND

For any point $\alpha_1 \in \Omega$, the point-stabilizer $G_{\alpha_1} = \text{Stab}_G(\alpha_1)$ acts $(k-1)$-transitively on the remaining points $\Omega \setminus \{\alpha_1\}$.

By chaining this downward, a $k$-transitive group satisfies:
 $G$ is transitive on $\vert{}\Omega\vert{} = n$ points.
 
 $G_{\alpha_1}$ is transitive on $n - 1$ points.
 
 $\dots$
 
 $G_{\alpha_1, \dots, \alpha_{k-1}}$ is transitive on $n - (k - 1)$ points.
    
By the Orbit-Stabilizer Theorem applied iteratively down the stabilizer tower:

$$\vert{}G\vert{} = n \cdot \vert{}G_{\alpha_1}\vert{} = n(n - 1) \cdot \vert{}G_{\alpha_1, \alpha_2}\vert{} = \dots = n(n - 1)(n - 2)\cdots(n - k + 1) \cdot \vert{}G_{\alpha_1, \dots, \alpha_k}\vert{}$$

Therefore, for $G$ to be $k$-transitive on $n$ points, the order of $G$ must be a multiple of the falling factorial:

$$\vert{}G\vert{} \quad \text{is divisible by} \quad \frac{n!}{(n - k)!}$$

If $n = 10$ and $G$ is $1$-transitive, $\vert{}G\vert{}$ only needs to be divisible by $10$. If $G$ is $2$-transitive, $\vert{}G\vert{}$ must be divisible by $10 \times 9 = 90$. If $G$ is $3$-transitive, $\vert{}G\vert{}$ must be divisible by $10 \times 9 \times 8 = 720$.

High transitivity is extraordinarily rare. Aside from the full symmetric groups $S_n$ ($n$-transitive) and alternating groups $A_n$ ($(n-2)$-transitive), there are no 6-transitive groups at all. The only non-trivial $4$-transitive and $5$-transitive groups in existence are the sporadic Mathieu groups ($M_{11}, M_{12}, M_{23}, M_{24}$). Any group that is $k$-transitive for $k \ge 2$ is so flexible that it wipes out almost all invariant geometric relations (like lines, distances, or graphs) on the set.

A weaker condition on a $G$-space is $k$-homogeneity, where we don't insist that some $g \in G$ maps any ordered $k$-tuple to another while respecting the order of elements in the tuple. We only require it to map any $k$-element subset to any other $k$-element subset. The order of the mapping is not important, which is why we can downgrade from a tuple to a subset.

Similar to transitivity, we have: if $\Omega$ be a transitive $G$-space and $\alpha \in \Omega$. Then $G$ is $(k + 1)$-homogeneous on $\Omega$ if and only if the stabilizer $G_\alpha$ is $k$-homogeneous on $\Omega \setminus \{\alpha\}$.

#### Orbit Decomposition

Transitive actions are the fundamental building blocks of permutation group theory. If you understand how groups act transitively on individual orbits (which are classified purely as coset spaces $G/\text{Stab}(x)$), you can analyze any arbitrary permutation group by studying its transitive pieces and how they are wired together inside the subdirect product. Towards this, we first look at how a group decomposes into orbits.

Every point $x \in \Omega$ belongs to at least one orbit (since $x \in \mathcal{O}_x$). If two orbits share even a single common point ($z \in \mathcal{O}_x \cap \mathcal{O}_y$), they must be completely identical ($\mathcal{O}_x = \mathcal{O}_y$). So two orbits are either strictly disjoint or equal. Therefore:

$$\Omega = \bigsqcup_{i \in I} \mathcal{O}_{x_i}$$

A $G$-space $\Omega$ breaks down into orbits in exactly one way because being in the same orbit is an equivalence relation.

A point $x$ cannot belong to orbit $A$ and also to a distinct orbit $B$. Every single point in the space is accounted for. Each orbit is a minimal $G$-invariant subset. You cannot slice an orbit into smaller $G$-invariant pieces, nor can you merge two orbits without breaking transitivity.

This theorem helps us further in our foundational "divide and conquer" theorem of permutation groups: any arbitrary permutation group can be decomposed into independent transitive pieces.

$\Omega$ partitions uniquely into disjoint orbits:

$$\Omega = \Delta_1 \sqcup \Delta_2 \sqcup \dots \sqcup \Delta_k$$

For each orbit $\Delta_i$, there is a projection map $\pi_i$ that restricts the action of $g \in G$ to just the points in $\Delta_i$:

$$\pi_i : G \longrightarrow \text{Sym}(\Delta_i), \quad \pi_i(g) = g\vert{}_{\Delta_i}$$

The image of $\pi_i$ is the $i$-th transitive constituent:

$$G^{\Delta_i} = \pi_i(G)$$

$G$ is isomorphic to a subgroup of the direct product of its transitive constituents. 

#### Kernels, Cores & Faithfulness

These three tools serve three fundamental purposes in algebra: detecting hidden normal subgroups, constructing faithful concrete representations (like matrices or permutations) for abstract groups, and detecting simple groups.

First let's explain these terms. Every group action of $G$ on a set $\Omega$ is encoded by a homomorphism:

$$\phi: G \longrightarrow \text{Sym}(\Omega)$$

where each group element $g$ gets mapped to a permutation $\phi(g)$ of the set $\Omega$.

The kernel of this action is the standard kernel of the homomorphism $\phi$:

$$\ker(\phi) = \{g \in G \mid \phi(g) = \text{id}_\Omega\}$$

The kernel consists of all group elements that do absolutely nothing to any point in the set. For an element $g$ to be in $\ker(\phi)$, it must leave every single point $\alpha \in \Omega$ fixed: $g \cdot \alpha = \alpha \quad \forall \alpha \in \Omega$.
    
Since fixing a point $\alpha$ means belonging to its stabilizer $G_\alpha$, an element in the kernel must live inside every single stabilizer simultaneously:

$$\ker(\phi) = \bigcap_{\alpha \in \Omega} G_\alpha$$
    
Because the kernel of any homomorphism is a normal subgroup, $\ker(\phi) \trianglelefteq G$ always.

An action is faithful if the group elements do not pretend to be something they are not—no non-identity element acts as the identity permutation.

$$\text{Faithful} \iff \ker(\phi) = \{e\}$$

Distinct group elements perform distinct permutations. If $g \neq h$, then there is at least one point $\alpha \in \Omega$ where $g \cdot \alpha \neq h \cdot \alpha$. The group $G$ embeds cleanly as a true subgroup of $\text{Sym}(\Omega)$.
    
If the action is unfaithful, there are non-identity elements ($g \neq e$) that leave every single point completely untouched. The action "forgets" or blinds itself to those elements.
    
The core is a concept defined for any arbitrary subgroup $H \le G$. If $H$ is a subgroup of $G$, $H$ might not be normal ($g H g^{-1} \neq H$). The core of $H$ in $G$ is defined as the intersection of all conjugate copies of $H$:

$$\text{Core}_G(H) = \bigcap_{g \in G} g H g^{-1}$$

It is the largest normal subgroup of $G$ that can fit entirely inside $H$. If $H$ is already normal to begin with, then $g H g^{-1} = H$ for all $g$, so $\text{Core}_G(H) = H$. If $H$ contains no non-trivial normal subgroups of $G$, then $\text{Core}_G(H) = \{e\}$ (we say $H$ is core-free).

The bridge connecting these three concepts is the coset action (or any transitive action). Suppose $G$ acts on the set of left cosets $\Omega = G/H$ by left multiplication:

$$g \cdot (xH) = (gx)H$$

What is the stabilizer of the base point? The base point is the coset $1H = H$. An element $g$ fixes this point if $gH = H$, which means $g \in H$. So the stabilizer is: $\text{Stab}_G(1H) = H$.
    
What are the stabilizers of the other points? The coset $xH$ is reached by moving $1H$ by $x$. As established earlier, moving a point conjugates its stabilizer: $\text{Stab}_G(xH) = x H x^{-1}$.
    
What is the kernel of this action? The kernel consists of the elements that fix all cosets in $\Omega$: $\ker(\phi) = \bigcap_{xH \in G/H} \text{Stab}_G(xH) = \bigcap_{x \in G} x H x^{-1}$.

Notice that exact formula: that is the definition of $\text{Core}_G(H)$! Therefore, for any coset action:

$$\ker(\phi) = \text{Core}_G(H)$$

$$\text{The action of } G \text{ on } G/H \text{ is faithful} \iff \ker(\phi) = \{e\} \iff \text{Core}_G(H) = \{e\}$$

Now let's look at why we care about these tools, starting with finding normal subgroups. Subgroups in a group are rarely normal. However, taking the core of _any_ non-normal subgroup automatically creates a normal subgroup:

$$\text{Core}_G(H) = \bigcap_{g \in G} g H g^{-1} \trianglelefteq G$$

Because $\text{Core}_G(H) \le H$, it guarantees the existence of a non-trivial normal subgroup under very light conditions.

**Example (Poincaré’s Theorem):** If $G$ has a subgroup $H$ of finite index $[G : H] = n$, the core $K = \text{Core}_G(H)$ is a normal subgroup of $G$ whose index $[G : K]$ divides $n!$.

This is the exact mechanism behind the theorem you looked at earlier: finding a prime-index subgroup $H$ and showing that $H = \text{Core}_G(H)$, which immediately proves $H$ is normal.

Now let's look at converting abstract groups into concrete permutations or matrices. Abstract groups defined by axioms or generators and relations can be difficult to visualize or compute with. To study them, we map them into concrete geometric groups:

$$\phi: G \longrightarrow \text{Sym}(\Omega) \quad \text{or} \quad \rho: G \longrightarrow \text{GL}(n, \mathbb{C})$$

Calculating the kernel and checking faithfulness tells you whether information is lost in that translation. If the action is faithful ($\ker(\phi) = \{1\}$), by the First Isomorphism Theorem:

$$G / \{1\} \cong G \hookrightarrow \text{Sym}(\Omega)$$

The map is an embedding. You have successfully realized the abstract group $G$ as a concrete group of permutations or invertible matrices. You can now use matrix algorithms or permutation cycle notation to analyze $G$.
    
If the action is unfaithful ($\ker(\phi) \neq \{1\}$), the representation collapses parts of $G$. The image does not represent $G$, but rather the smaller quotient group $G/\ker(\phi)$.

These definitions are also useful for proving that a group is simple. Recall that a group is simple if its only normal subgroups are $\{1\}$ and the group itself. If you are investigating a group $G$ and you construct a non-trivial action on a set $\Omega$:

The kernel $\ker(\phi)$ must be a normal subgroup of $G$. Because $G$ is simple, the only possibilities are: $\ker(\phi) = G \quad \text{or} \quad \ker(\phi) = \{1\}$
    
As long as at least one element of $G$ moves at least one point in $\Omega$, $\ker(\phi) \neq G$. Therefore, $\ker(\phi)$ is forced to be $\{1\}$. Any non-trivial action of a simple group is automatically faithful. This makes it possible to determine the minimum degree $n$ needed to embed a simple group into $S_n$.

These are also useful in diagnosing the "blind spots" of a physical/symmetric system. In physics and coding theory, group actions often represent symmetries applied to a state space:

Elements in the kernel (the core) are global "gauge redundancies" or invisible shifts—operations you apply to the system that leave every measurable state completely unchanged.

If a symmetry action is not faithful, factoring out the kernel ($G/\ker(\phi)$) gives the effective symmetry group that actually impacts the physical degrees of freedom.

**Aside:** The hook arrow symbol $\hookrightarrow$ represents an injective homomorphism (also called an embedding or canonical inclusion). In the expression:

$$G / \{1\} \cong G \hookrightarrow \text{Sym}(\Omega)$$

A standard single arrow $\to$ denotes any arbitrary function or homomorphism.
    
The "hook" tail on $\hookrightarrow$ specifically indicates injectivity (one-to-one).
    
When you write $A \hookrightarrow B$, it asserts two things:

No Information Loss (Trivial Kernel): The map preserves the algebraic structure with zero collapse: $\ker = \{1\}$. Distinct elements in $A$ map to distinct elements in $B$.
    
Subgroup Realization: $A$ is isomorphic to its image inside $B$. $A \cong \text{im}(A) \le B$.

Because the action $\phi: G \to \text{Sym}(\Omega)$ is faithful, its kernel is trivial ($\ker(\phi) = \{1\}$). Therefore, $G$ is not just sending signals into $\text{Sym}(\Omega)$; it is embedded directly inside $\text{Sym}(\Omega)$ as an honest, fully realized subgroup of permutations.

#### Example of Building a Larger Group

Suppose a group $G$ permutes a 10-point set $\Omega = \Omega_1 \sqcup \Omega_2$, where $\vert{}\Omega_1\vert{} = 4$ and $\vert{}\Omega_2\vert{} = 6$.

When you pick any element $g \in G$:

-   $g$ does something to the 4 points in $\Omega_1$. Call that transformation $g_1 \in S_4$.
    
-   Simultaneously, $g$ does something to the 6 points in $\Omega_2$. Call that transformation $g_2 \in D_{12}$.
    

So every element $g \in G$ can be written as an ordered pair:

$$g = (g_1, g_2) \in S_4 \times D_{12}$$

Now the central question is: Are the actions on $\Omega_1$ and $\Omega_2$ completely independent, or are they talking to each other?

If they are completely independent, you can pick any permutation $g_1 \in S_4$ on $\Omega_1$ while keeping $\Omega_2$ frozen ($g_2 = e$). And you can pick _any_ symmetry $g_2 \in D_{12}$ on $\Omega_2$ while keeping $\Omega_1$ frozen. If so, $G$ is the entire direct product $S_4 \times D_{12}$, of size $24 \times 12 = 288$.
    
If the two are somehow coupled, whenever you do something to $\Omega_1$, it forces you to do something compatible on $\Omega_2$. For example: "If I do an odd permutation on the first 4 points, I am strictly forbidden from keeping $\Omega_2$ still. I must perform a reflection on the hexagon." This is the entire motivation: how do we find all possible ways two orbits can be "coupled together"? Goursat's Lemma is the algebraic rule that tells you this.

Before looking at the Lemma, we look at a definition. Let $A$ and $B$ be two groups. A subgroup $G \le A \times B$ is called a subdirect product if:

1.  $G$ has at least one element $(a, b)$ for every $a \in A$ i.e. every element of $A$ appears as the first coordinate of at least one element in $G$ (the projection $\pi_1: G \to A$ is surjective).
    
2.  $G$ has at least one element $(a, b)$ for every $b \in B$ i.e. every element of $B$ appears as the second coordinate of at least one element in $G$ (the projection $\pi_2: G \to B$ is surjective).
    
In our case, the action on $\Omega_1$ is all of $S_4$. The action on $\Omega_2$ is all of $D_{12}$.    

That is literally saying that $G \le S_4 \times D_{12}$ is a subdirect product.

Now for Goursat's Lemma. Look at the elements that fix one orbit entirely:

-   Let $N_1$ be the set of transformations on $\Omega_1$ that can occur while leaving $\Omega_2$ completely unmoved:
    
    $$N_1 = \{ g_1 \in A \mid (g_1, e_B) \in G \}$$
    
-   Let $N_2$ be the set of transformations on $\Omega_2$ that can occur while leaving $\Omega_1$ completely unmoved:
    
    $$N_2 = \{ g_2 \in B \mid (e_A, g_2) \in G \}$$

$N_1$ is a normal subgroup of $A$, and $N_2$ is a normal subgroup of $B$.

Now, what is left over once you ignore the independent movements inside $N_1$ and $N_2$?

-   In $A$, the "coarse" behavior is given by the quotient group $A / N_1$.
    
-   In $B$, the "coarse" behavior is given by the quotient group $B / N_2$.

The reason the quotient group $A / N_1$ is the coupling mechanism is that the second coordinate depends only on which coset of $N_1$ you are in. Suppose $(a, b) \in G$. What happens if you modify $a$ by any internal, independent motion $n_1 \in N_1$?

$$(n_1, e_B) \cdot (a, b) = (n_1 a, b) \in G$$

The first coordinate changed from $a$ to $n_1 a$ (staying inside the same coset $a N_1$). The second coordinate did not change at all. It is still $b$.

Conversely, if $(a, b_1) \in G$ and $(a, b_2) \in G$, then $(a, b_1)^{-1}(a, b_2) = (a^{-1}, b_1^{-1})(a, b_2) = (e_A, b_1^{-1} b_2) \in G$.

This forces $b_1^{-1} b_2 \in N_2$, meaning $b_1$ and $b_2$ belong to the exact same coset $b_1 N_2 = b_2 N_2$.

The individual elements $a \in A$ carry too much fine-grained internal detail ($N_1$). Once you "blur" that fine detail out by quotienting:

$$A \longrightarrow A / N_1$$

each entire coset $a N_1$ determines a unique coarse behavior that matches one-to-one with a coarse behavior $b N_2$ in $B / N_2$. The correspondence between those coarse packages must respect multiplication, which is why it is an isomorphism of quotient groups.

**Goursat's Lemma:** The "locked-together" part of the two groups must be an exact isomorphism between their quotient groups.

$$\theta: A / N_1 \xrightarrow{\sim} B / N_2$$

An element $(g_1, g_2) \in A \times B$ belongs to $G$ if and only if $\theta(g_1 N_1) = g_2 N_2$.

To find all subdirect products of $A$ and $B$, Goursat's Lemma gives a 3-step recipe:

Find normal subgroups $N_1 \trianglelefteq A$ and $N_2 \trianglelefteq B$.

Check if $A/N_1$ and $B/N_2$ are isomorphic ($A/N_1 \cong B/N_2 \cong Q$). If they don't have the same quotient structure, they cannot be coupled this way.

For every isomorphism $\theta: A/N_1 \to B/N_2$, form:

$$G = \{ (g_1, g_2) \in A \times B \mid \theta(g_1 N_1) = g_2 N_2 \}$$

Let us see this machine in action on $S_4 \times D_{12}$:

**Case 1: Quotient $Q = \{1\}$ (Zero coupling)**

-   We choose $N_1 = S_4$ and $N_2 = D_{12}$.
    
-   Quotients: $S_4/S_4 \cong \{1\}$ and $D_{12}/D_{12} \cong \{1\}$.
    
-   Condition: $\theta(g_1 N_1) = g_2 N_2$ is vacuously true for every pair.
    
-   **Result:** No restrictions. $G = S_4 \times D_{12}$. Both orbits move with complete independence.

**Case 2: Quotient $Q = C_2$ (Odd/Even Parity coupling)**

-   In $S_4$, there is only one normal subgroup of index 2: $N_1 = A_4$ (the even permutations). The quotient $S_4 / A_4 \cong \{+1, -1\}$ just records whether a permutation is even or odd.
    
-   In $D_{12}$, is there a normal subgroup of index 2? Yes!
    
    Take $N_2 = \langle r \rangle \cong C_6$ (the 6 rotations of the hexagon).
    
    The quotient $D_{12} / \langle r \rangle \cong \{+1, -1\}$ records whether a symmetry is a pure rotation or includes a reflection.
    
-   Both quotients are $C_2$. They match!
    
-   What is the group $G$?
    
    Goursat says: pair them up via the isomorphism $\theta$:
    
    $$(g_1, g_2) \in G \iff \operatorname{sgn}(g_1) = \begin{cases} +1 & \text{if } g_2 \text{ is a rotation} \\ -1 & \text{if } g_2 \text{ is a reflection} \end{cases}$$
    
**What this means in plain English:** You can shuffle the 4 points however you want, and you can move the hexagon however you want, except: If you do an even shuffle on the 4 points, you are forced to do a rotation on the hexagon. If you do an odd shuffle on the 4 points, you are forced to do a reflection on the hexagon. The two orbits are tied together by a parity "gear."

**Case 3: Quotient $Q = S_3$ (3-fold symmetry coupling)**

Can $S_4$ quotient down to $S_3$? Yes: $S_4 / V_4 \cong S_3$, where $V_4 = \{e, (12)(34), (13)(24), (14)(23)\}$ is the Klein four-group.
    
Can $D_{12}$ quotient down to $S_3$? The center of $D_{12}$ is $Z(D_{12}) = \{e, r^3\}$ (rotation by $180^\circ$).
    
Quotienting out the $180^\circ$ rotation collapses opposite vertices of the hexagon, leaving a triangle! The symmetry group of an equilateral triangle is $D_6 \cong S_3$.
    
So $D_{12} / \langle r^3 \rangle \cong S_3$. Both quotients are $S_3$. They match!
    
**What this means in plain English:** $S_4$ permutes the 3 coordinate axes of the tetrahedron/cube via $S_3$, while $D_{12}$ permutes the 3 main diagonals of the hexagon via $S_3$. The group $G$ locks these two 3-element actions together so that whatever permutation occurs on the 3 axes of $\Omega_1$ must match the permutation on the 3 diagonals of $\Omega_2$.
    
**The Big Picture Takeaway**

Whenever an action has two orbits $\Omega_1$ and $\Omega_2$:

1.  $G$ is always a subgroup of $\operatorname{Sym}(\Omega_1) \times \operatorname{Sym}(\Omega_2)$.
    
2.  The orbits define normal subgroups of "unassisted" internal motions.
    
3.  The cross-talk between the two orbits is governed entirely by a shared quotient group $Q$.
    
4.  Goursat's Lemma is just the classification of all possible gear-locks between two independent mechanisms.

#### Sub-orbits, Orbitals, Blocks & Primitives

When $G$ acts on $\Omega$, we can also consider how $G$ acts on ordered pairs in $\Omega \times \Omega$. Primarily we will be looking at transitive actions here.

$$g \cdot (\alpha, \beta) = (g \cdot \alpha, \; g \cdot \beta)$$

An orbital $\Gamma$ is simply an orbit of this action on pairs:

$$\Gamma = \{ (g \cdot \alpha, g \cdot \beta) \mid g \in G \}$$

The set of pairs with identical elements, $\Delta = \{(\alpha, \alpha) \mid \alpha \in \Omega\}$, is always an orbital. It is the trivial diagonal orbital. Non-diagonal orbitals are the interesting relations between distinct points.
    
An orbital is a $G$-invariant relation. If $(\alpha, \beta)$ is an edge in the orbital, then applying any element of $G$ turns it into another edge in the same orbital.

Now we look at sub-orbits. Fix a point $\alpha \in \Omega$ and look at its point-stabilizer $G_\alpha$.

Even though $G$ moves $\alpha$ everywhere, $G_\alpha$ keeps $\alpha$ pinned down. $G_\alpha$ acts on the rest of the points of $\Omega$. The orbits of $G_\alpha$ on $\Omega$ are called the sub-orbits of $G$.

A sub-orbit requires picking a reference point $\alpha \in \Omega$. By definition, a sub-orbit with respect to $\alpha$ is an orbit of the stabilizer $G_\alpha$ acting on $\Omega$.

If you choose a different point $\beta \neq \alpha$, the stabilizer $G_\beta$ is a conjugate subgroup ($G_\beta = g G_\alpha g^{-1}$ where $g(\alpha) = \beta$). The subsets of $\Omega$ that form the orbits of $G_\beta$ will consist of different elements than the orbits of $G_\alpha$.

A sub-orbit of $G$ with respect to $\alpha \in \Omega$ is an orbit of the point stabilizer $G_\alpha$ acting on $\Omega$. Since $G_\alpha$ fixes $\alpha$, $\{\alpha\}$ is always an orbit of size 1 (the trivial sub-orbit).

An orbital is global (pairs of points). A sub-orbit is local (looking from one fixed base point $\alpha$). 

For every orbital $\Gamma$, the slice:

$$\Gamma(\alpha) = \{\beta \in \Omega \mid (\alpha, \beta) \in \Gamma\}$$

is an orbit of $G_\alpha$ on $\Omega$ (a sub-orbit). That shouldn't be surprising. $\Gamma(\alpha)$ pins $\alpha$ down but moves all other elements, so the $\beta$ portion of the orbital forms the sub-orbit. 

From this, we can see that the number of orbitals of $G$ equals the number of sub-orbits of $G_\alpha$. This number is equal for all points of the set. It is called the rank of the transitive group $G$. But if an action is intransitive and you pick two points from different orbits, the suborbits can have completely different counts, sizes, and group structures.
    
If rank = 2, $G_\alpha$ has only two orbits: $\{\alpha\}$ and $\Omega \setminus \{\alpha\}$. This means $G_\alpha$ acts transitively on all other points, which means $G$ is $2$-transitive.

Looking at it conversely, because $G$ is 2-transitive, for any two distinct points $\beta, \gamma \in \Omega \setminus \{\alpha\}$, there exists $g \in G$ fixing $\alpha$ and sending $\beta \mapsto \gamma$. That means $G_\alpha$ acts transitively on the remaining points $\Omega \setminus \{\alpha\}$. Therefore, $G_\alpha$ partitions $\Omega$ into exactly two orbits: $\{\alpha\}$ and $\Omega \setminus \{\alpha\}$.

Every $2$-transitive action is strictly primitive. The hierarchy of transitivity properties runs strictly in this order:

$$\dots \implies 3\text{-transitive} \implies 2\text{-transitive} \implies \text{Primitive} \implies 1\text{-transitive}$$

We can also say a non-trivial normal subgroup of a primitive permutation group is transitive. And, a transitive group $G$ acting on a set $\Omega$ is primitive if and only if the point stabilizer $G_\alpha$ is a maximal subgroup of $G$.

Why do we care about this? Abstract group theory decomposes groups using normal subgroups:

$$\text{Group} \longrightarrow \text{Composition Factors (Simple Groups)}$$

Permutation group theory uses a geometric and combinatorial hierarchy based on the preservation of structure on $\Omega$:

$$\text{All Actions} \xrightarrow{\text{orbits}} \text{Transitive} \xrightarrow{\text{blocks}} \text{Primitive} \xrightarrow{\text{O'Nan-Scott}} \text{Affine / Almost Simple / Product Action}$$

1.  **Intransitive $\to$ Transitive:** Any permutation action breaks into disjoint transitive components (its orbits).
    
2.  **Transitive $\to$ Primitive:** A transitive group is imprimitive if it preserves a non-trivial partition of $\Omega$ (called a system of blocks, like suits in a deck of cards). If no non-trivial partition is preserved, the group is primitive. Imprimitive groups embed into wreath products $H \wr K$, reducing their study to primitive components.
    
3.  **Primitive $\to$ Almost Simple / Basic Types:** By the O'Nan-Scott Theorem, every finite primitive permutation group belongs to one of five explicit structural classes (e.g., affine type, almost simple, product action, diagonal type).

This yields a completely independent structural ladder where primitive groups play the role of "irreducible" objects. Here, "primitive" refers to prime.

Permutation group theory provides the natural language for symmetry in external mathematical structures:

**Rank and Orbitals $\leftrightarrow$ Graph Theory:** Every orbital $\Delta$ of a transitive group $G$ defines an orbital digraph (directional graph) $\Gamma = (\Omega, \Delta)$. If the orbital is self-paired, $\Gamma$ is an undirected graph. Studying the orbitals of rank 3 permutation groups directly constructs and classifies strongly regular graphs (e.g., the Petersen graph from $S_5$, the Higman-Sims graph).
    
**Point Stabilizers $\leftrightarrow$ Geometries:** Coset spaces $G / G_\alpha$ allow one to reconstruct incidence geometries, projective planes, and block designs purely from subgroup lattice data.
      
#### Equivariant vs Invariant

A couple of definitions before we proceed. An object (a subset, a function, a relation, or a metric) is $G$-invariant if applying any element $g \in G$ leaves it completely unchanged.

For eg. **Invariant subset:** $S \subseteq \Omega$ is $G$-invariant if $g(S) = S$ for all $g \in G$.

**Invariant function:** $f: \Omega \to \mathbb{R}$ is $G$-invariant if $f(g(x)) = f(x)$ for all $g \in G, x \in \Omega$. (The output value does not change when the input is transformed).
        
**Invariant relation ($G$-congruence):** A relation $\sim$ on $\Omega$ is $G$-invariant if $x \sim y \iff g(x) \sim g(y)$ for all $g \in G$.
        
By contrast, a map between two spaces, each equipped with its own $G$-action, is equivariant if applying a group element _before_ the map gives the same result as applying it _after_ the map.    

Let $X$ and $Y$ both be $G$-sets. A map $\phi: X \to Y$ is $G$-equivariant (or a homomorphism of $G$-sets) if: $\phi(g \cdot x) = g \cdot \phi(x) \quad \text{for all } g \in G, x \in X$.
    
**Invariance** is a property of a single static entity or a scalar evaluation (the output space has a trivial action: $g \cdot c = c$, so $\phi(g \cdot x) = \phi(x)$).

**Equivariance** is a dynamic structural property of maps between spaces that transform non-trivially under the group.

**Example 1 of Orbitals**

Consider $G = \langle (1 \; 2 \; 3 \; 4 \; 5) \rangle \cong C_5$ acting on $\Omega = \{1, 2, 3, 4, 5\}$. Let us test the orbit of the pair $(1, 4)$ under $g = (1 \; 2 \; 3 \; 4 \; 5)$. Every transformed pair is an edge in the graph:

1.  $g^0(1, 4) = (1, 4) \implies \text{Edge: } 1 \to 4$
    
2.  $g^1(1, 4) = (2, 5) \implies \text{Edge: } 2 \to 5$
    
3.  $g^2(1, 4) = (3, 1) \implies \text{Edge: } 3 \to 1$
    
4.  $g^3(1, 4) = (4, 2) \implies \text{Edge: } 4 \to 2$
    
5.  $g^4(1, 4) = (5, 3) \implies \text{Edge: } 5 \to 3$

The graph consists of exactly these 5 directed edges:

$$E = \{ (1, 4), \; (2, 5), \; (3, 1), \; (4, 2), \; (5, 3) \}$$

To trace the connected path, match the head of each arrow to the tail of the next:

-   Start at $1$: the edge is $1 \to 4$ (you are now at vertex $4$).
    
-   From $4$: look for the edge starting at $4$, which is $4 \to 2$ (now at vertex $2$).
    
-   From $2$: the edge is $2 \to 5$ (now at vertex $5$).
    
-   From $5$: the edge is $5 \to 3$ (now at vertex $3$).
    
-   From $3$: the edge is $3 \to 1$ (back at vertex $1$).

Chaining them sequentially gives the closed path:

$$1 \longrightarrow 4 \longrightarrow 2 \longrightarrow 5 \longrightarrow 3 \longrightarrow 1$$

Every single vertex $\{1, 2, 3, 4, 5\}$ is visited in a single continuous cycle, so the graph has only $1$ connected component.

Suppose instead we had 6 points and $G = \langle (1 \; 2 \; 3 \; 4 \; 5 \; 6) \rangle \cong C_6$. Applying powers of $g$ to the seed pair $(1, 3)$ generates its orbit:

1.  $g^0(1, 3) = (1, 3) \implies 1 \to 3$
    
2.  $g^1(1, 3) = (2, 4) \implies 2 \to 4$
    
3.  $g^2(1, 3) = (3, 5) \implies 3 \to 5$
    
4.  $g^3(1, 3) = (4, 6) \implies 4 \to 6$
    
5.  $g^4(1, 3) = (5, 1) \implies 5 \to 1$
    
6.  $g^5(1, 3) = (6, 2) \implies 6 \to 2$

The resulting edge set contains 6 directed edges:

$$E = \{ (1, 3), \; (2, 4), \; (3, 5), \; (4, 6), \; (5, 1), \; (6, 2) \}$$

Tracing paths by following the arrows:

$$1 \longrightarrow 3 \longrightarrow 5 \longrightarrow 1$$

Vertex $1$ goes to $3$, $3$ goes to $5$, and $5$ goes back to $1$. This closes a 3-cycle.

$$2 \longrightarrow 4 \longrightarrow 6 \longrightarrow 2$$

Vertex $2$ goes to $4$, $4$ goes to $6$, and $6$ goes back to $2$. This closes a separate 3-cycle.
    

Neither path can reach the other because no edge connects the odd set $\{1, 3, 5\}$ to the even set $\{2, 4, 6\}$.

A single seed pair $(1, 3)$ generated an edge set whose graph naturally splits into two disconnected components (the blocks of imprimitivity $\{1, 3, 5\}$ and $\{2, 4, 6\}$). The orbital graph detects the hidden internal geometry and intermediate subgroups of the action.

**Example 2 of orbitals**

Let $\Omega = \Delta_1 \sqcup \Delta_2$, where:

-   $\Delta_1 = \{1, 2, 3\}$
    
-   $\Delta_2 = \{4, 5, 6\}$

The total product space $\Omega \times \Omega$ contains $6 \times 6 = 36$ ordered pairs. Because an element $g \in G$ cannot map a point from $\Delta_1$ into $\Delta_2$ (or vice-versa), the product space splits into four disjoint, $G$-invariant quadrants:

$$\Omega \times \Omega = (\Delta_1 \times \Delta_1) \;\sqcup\; (\Delta_2 \times \Delta_2) \;\sqcup\; (\Delta_1 \times \Delta_2) \;\sqcup\; (\Delta_2 \times \Delta_1)$$

Every orbital of $G$ on $\Omega$ must live entirely inside one of these four quadrants.

There are two types of orbitals. One is Intra-orbitals (Diagonal Blocks: $\Delta_1 \times \Delta_1$ and $\Delta_2 \times \Delta_2$). These consist of pairs where both points come from the **same** orbit, such as $(1, 2)$ or $(4, 5)$. An orbital inside $\Delta_1 \times \Delta_1$ is identical to an orbital of the transitive constituent $G^{\Delta_1}$ acting on $\Delta_1$. In the orbital graph, these are edges that stay entirely within island $\Delta_1$ or island $\Delta_2$.
        
The other type is Cross-orbitals (Off-Diagonal Blocks: $\Delta_1 \times \Delta_2$ and $\Delta_2 \times \Delta_1$). These consist of mixed pairs, such as $(1, 4)$ or $(2, 6)$, where the starting point is in $\Delta_1$ and the target point is in $\Delta_2$. In the orbital graph, these form a bipartite graph with directed arrows crossing exclusively from the set $\{1, 2, 3\}$ over to $\{4, 5, 6\}$. These cross-orbitals measure how the action on $\Delta_1$ is synchronized with the action on $\Delta_2$.

To see what cross-orbitals reveal, compare two different actions having the exact same orbits $\Delta_1 = \{1, 2, 3\}$ and $\Delta_2 = \{4, 5, 6\}$. In example A,  let $G = \langle (1 \; 2 \; 3)(4 \; 5 \; 6) \rangle \cong C_3$. The order of $G$ is 3. Pick the cross-pair $(1, 4) \in \Delta_1 \times \Delta_2$. Its orbit under $G$ is: $\{(1, 4), \; (2, 5), \; (3, 6)\}$.
    
Because $\vert{}G\vert{} = 3$, this cross-orbital has only 3 pairs. The remaining 6 mixed pairs in $\Delta_1 \times \Delta_2$ split into two other separate cross-orbitals:

Orbit of $(1, 5)$: $\{(1, 5), (2, 6), (3, 4)\}$ and orbit of $(1, 6)$: $\{(1, 6), (2, 4), (3, 5)\}$
        
The cross-orbitals detect the rigid 1-to-1 locking between the two orbits.

As example  B, let's look at a fully independent (Uncoupled) action. Let $G = \langle (1 \; 2 \; 3), \; (4 \; 5 \; 6) \rangle \cong C_3 \times C_3$. The order of $G$ is 9. Pick the cross-pair $(1, 4) \in \Delta_1 \times \Delta_2$. Because you can cycle $\{1, 2, 3\}$ while holding $\{4, 5, 6\}$ stationary (using $(1 \; 2 \; 3)$), and cycle $\{4, 5, 6\}$ independently (using $(4 \; 5 \; 6)$), you can steer $(1, 4)$ to any of the $3 \times 3 = 9$ possible pairs in $\Delta_1 \times \Delta_2$.
    
The entire cross-space $\Delta_1 \times \Delta_2$ forms one single cross-orbital of size 9.
    
How to approach it in practice? If your goal is to analyze blocks of imprimitivity and primitivity: You focus on the transitive constituents first, taking the orbitals of each orbit individually ($\Delta_i \times \Delta_i$), because primitivity is only defined for transitive actions.
    
If your goal is to understand the full group structure of $G$ (as a subdirect product): You take the global orbitals of the whole action on $\Omega \times \Omega$. The cross-orbitals will tell you whether the orbits move independently (direct product) or are constrained together (subdirect product).

The choice between taking the intra-orbitals (orbit-by-orbit analysis) versus the global cross-orbitals corresponds directly to whether you are analyzing the internal structure of an individual code/system or analyzing entanglement, correlations, and cross-talk across multi-component systems.

You care about intra-orbitals ($\Delta_i \times \Delta_i$) and primitivity when analyzing a single space where your group acts transitively. In classical error-correcting codes, the automorphism group of a code, $\text{Aut}(C)$, acts transitively on the coordinate positions $\{1, 2, \dots, n\}$.

If $\text{Aut}(C)$ acts primitively on the bit positions, the code has no non-trivial block structure. It cannot be decomposed into a direct sum or a non-trivial concatenated code over coordinates.

For example, the affine group $\text{AGL}(m, 2)$ acting on Reed-Muller codes $\mathcal{RM}(r, m)$ acts 2-transitively (and hence primitively) on the affine space $\mathbb{F}_2^m$. Its orbital graph is complete, meaning every coordinate is completely symmetric to every other coordinate with no clustered "islands."

If $\text{Aut}(C)$ is imprimitive, the vertices cluster into blocks of imprimitivity. Those blocks pinpoint coordinate sub-blocks—revealing that the code is equivalent to an interleaved code or a generalized concatenated architecture.

In Quantum Information Theory & QEC, consider a stabilizer code $[[n, k, d]]$. The permutation symmetries of the physical qubits correspond to transversal operations that map the code space to itself. In topological codes (like the Toric code or surface codes), stabilizer generators are local. If you analyze the symmetries of the syndrome graph, primitive actions mean there are no invariant sub-lattices. Fixing a base qubit $\alpha$, the sub-orbits of the stabilizer group on the remaining qubits partition the physical qubits into distance shells. The weight distribution of Pauli errors that map into stabilizers is constrained by these sub-orbits.

On the other hand, you care about global cross-orbitals ($\Delta_1 \times \Delta_2$) when your space naturally breaks into multiple distinct sectors or physical subsystems, and you need to measure coupling vs. independence. In classical error correction, suppose you transmit data across two separate parallel channels, $\Delta_1$ and $\Delta_2$. If the symmetry group acts as a full direct product ($G^{\Delta_1} \times G^{\Delta_2}$), there is only one giant cross-orbital. This proves the noise processes or code constraints on channel 1 and channel 2 are completely independent.

If the symmetry group acts as a subdirect product (e.g., $C_3 \le C_3 \times C_3$), the cross-space splits into multiple smaller cross-orbitals. This immediately diagnoses cross-talk, shared parity constraints, or structured joint channel noise.
        
In generalized low-density parity-check (LDPC) codes or turbo codes, parity checks live on bipartite graphs connecting variable nodes ($\Delta_1$) and check nodes ($\Delta_2$). The edges of the Tanner graph are invariant sub-graphs formed by specific cross-orbitals between variable and check sets.
    
In Quantum Information Theory & QEC, in Quantum Entanglement and Bipartite Systems ($\mathcal{H}_A \otimes \mathcal{H}_B$): Let $\Delta_1$ index a basis for system $A$ and $\Delta_2$ index a basis for system $B$. A joint state $\vert{}\psi_{AB}\rangle = \sum_{\alpha, \beta} c_{\alpha, \beta} \vert{}\alpha\rangle \vert{}\beta\rangle$ has a density matrix $\rho_{AB}$ acted on by a symmetry group $G$.
        
If the group action creates multiple, small cross-orbitals, the basis pairs $(\alpha, \beta)$ are locked together in invariant sub-spaces. By Schur’s Lemma, the density matrix $\rho_{AB}$ decomposes into blocks matching these cross-orbitals, proving the existence of entanglement or classical correlations that cannot be disrupted by symmetric local operations.
        
In flag-fault-tolerant architectures, you introduce auxiliary "flag" qubits ($\Delta_2$) to monitor data qubits ($\Delta_1$).

The joint stabilizer-syndrome operations act intransitively: data qubits remain data qubits, and flag qubits remain flag qubits. The cross-orbitals in $\Delta_1 \times \Delta_2$ describe which specific data errors trigger which specific flag measurements. A single cross-orbital connecting a weight-2 data error to a specific flag indicates that the error is uniquely identifiable and will not propagate into an uncorrectable fault.

How do orbitals, subgroups, actions and transitivity fit together? Assume $G$ acts transitively on $\Omega$.
```
Action of G on Ω
       │
       ▼
G acts on pairs (α, β) ∈ Ω × Ω
       │
       ▼
Orbits of pairs = ORBITALS
       │
       ├── Fix α: slice of orbital = SUB-ORBIT (Orbit of G_α on Ω)
       │
       ▼
Draw each orbital as a directed graph = ORBITAL GRAPH
       │
       ├── Graph has disconnected "islands"? ──► IMPRIMITIVE (Blocks exist)
       │
       └── ALL non-trivial graphs are CONNECTED? ──► PRIMITIVE (No blocks)
```
    
### A Little Representation Theory

While Cayley proved every group is a permutation group, permutations are notoriously difficult to do calculus or continuous mathematics on. You cannot easily take the derivative or find the eigenvectors of a permutation.

Mathematicians wanted to port the powerful tools of Linear Algebra (matrices, traces, determinants) into abstract groups. This created Representation Theory.

A group mathematically captures the "symmetries" of a system (like rotations or permutations). When we write a representation, we are drawing matrices that show exactly how those symmetries move vectors around in a space. 

A representation of $G$ over $F$ is a homomorphism $r$ from $G$ to $GL(n, F)$, for some $n$. The degree of $r$ is the integer $n$. Thus if $r$ is a function from $G$ to $GL(n, F)$, then $r$ is a representation if and only if:

$$(gh)r = (gr)(hr) \quad \text{for all } g, h \in G$$

Since a representation is a homomorphism, it follows that for every representation $r: G \to GL(n, F)$, we have:

$$1r = I_n$$

and

$$(g^{-1})r = (gr)^{-1} \quad \text{for all } g \in G$$

Two representations are equivalent (and form an equivalence relation) if: 

Let $\rho: G \to GL(m, F)$ and $\sigma: G \to GL(n, F)$ be representations of $G$ over $F$. We say that $\rho$ is equivalent to $\sigma$ if $n = m$ and there exists an invertible $n \times n$ matrix $T$ such that for all $g \in G$,

$$(g)\sigma = T^{-1}((g)\rho)T$$

To understand why this is so, let $\rho$ map element $g$ to matrix $A_1$ and $h$ to $A_2$, and let $\sigma$ map $g$ to $B_1$ and $h$ to $B_2$. For a representation we must have $\rho$ mapping $gh$ to $A_1A_2$ and $\sigma$ mapping $gh$ to $B_1B_2$.

By the above definition, if we have some matrix $T$ such that $B_1 = T^{-1}A_1T$ and $B_2 = T^{-1}A_2T$, then we can evaluate the product $B_1B_2$:

$$B_1B_2 = (T^{-1}A_1T)(T^{-1}A_2T)$$

The $TT^{-1}$ in the middle cancels out to the identity matrix, leaving $T^{-1}A_1A_2T$. Thus, the equality holds true, preserving the group structure.

Equivalency in representation theory is just linear algebra's "change of basis." The matrix $T$ represents a coordinate transformation. Two equivalent representations are the exact same physical symmetries; you are just writing down the matrices using a different set of coordinate axes.
    
The matrix $T$ is mathematically known as an intertwining operator. It is a linear map between vector spaces that "commutes" with the group action (i.e., $T((g)\sigma) = ((g)\rho)T$). When an intertwining operator is invertible, the representations are equivalent.

A representation is said to be faithful if $\ker(\rho) = \{1\}$; that is, if the identity element of $G$ is the only element $g$ for which $(g)\rho = I_n$. From what we know of kernels and images, it is no surprise that a representation $\rho$ of a finite group $G$ is faithful if and only if $\operatorname{im}(\rho)$ is isomorphic to $G$.

A faithful representation means that no two distinct group elements map to the exact same matrix. The group structure is perfectly preserved without any "crushing" or loss of information. In quantum mechanics, a faithful representation means every distinct physical symmetry operation (like rotating 90 degrees vs. 180 degrees) corresponds to a strictly unique matrix operator acting on your state vectors. If a representation is unfaithful (say, mapping every element to the $1 \times 1$ identity matrix), it means your state space is entirely blind to that specific symmetry.

An abelian group's representations all decompose into 1-dimensional subspaces over $\mathbb{C}$. Conversely, suppose that $G$ is a finite group such that every irreducible $\mathbb{C}G$-module has dimension 1. Then $G$ is abelian.

A representation matrix of any element $g$ is diagonalizable in some basis, but that does not mean the same basis can give us diagonal matrices for all elements of $G$. This will happen only if the group is abelian. This should remind us of commuting observables in quantum mechanics. The theorem proving that an abelian group's representations all decompose into 1-dimensional subspaces over $\mathbb{C}$ is the exact mathematical mechanism that allows a complete set of commuting observables (CSCO) to uniquely identify every pure state in a quantum system.

#### $FG$-modules

A module represents abstract operations of group elements over a vector space. It isn't really different from a representation, which is the same thing but with a concrete choice of basis vectors. Modules are very much like tensors. A tensor $T$ is an intrinsic, geometric multilinear object. When you select a coordinate basis, $T$ reveals itself as a multidimensional array of numbers (components $T^{i}_{\ j}$). If you perform a coordinate transformation, the numbers change according to the transformation rule, but the tensor itself remains unchanged.

Modules are powerful and come with many tools, like character tables, that allow us to determine the many aspects of the interaction between groups, fields and vector spaces without having to resort to matrix manipulations.

Algebraists prefer the module definition because it is coordinate-free (no matrices required), while physicists often prefer the matrix representation for explicit calculations.

An $FG$-module is a vector space $V$ over a field $F$. It needs a few algebraic rules to function consistently. The following conditions should hold for all $u, v \in V$, $\lambda \in F$ and $g, h \in G$:

1.  $vg \in V$
    
2.  $v(gh) = (vg)h$
    
3.  $v1 = v$
    
4.  $(\lambda v)g = \lambda(vg)$,  $\lambda$ is a scalar in $F$.
    
5.  $(u + v)g = ug + vg$

You could actually club conditions 4 and 5 into one single condition representing linearity: $\left( \sum_{i=1}^n \lambda_i v_i \right) g = \sum_{i=1}^n \lambda_i (v_i g)$

A module is faithful if the identity element of $G$ is the only element for which $vg = v$ for all $v \in V$. 

In the conditions above, if you just think of the element $g$ as being a matrix representation of $g$ i.e. $g\rho$ where $\rho$ is a representation, it essentially turns into the conditions for a representation. So, giving a representation $\rho: G \to GL(n, F)$ is equivalent to turning the vector space $F^n$ into an $FG$-module. 

If we have a representation (and its basis vectors) in hand, we don't actually need to test the conditions for a module for each $v$. We can just test that the conditions hold for the basis vectors $v_i$ and extend them linearly to span the whole vector space. 

**Does a finite group only have a finite number of representations?** You can build an infinite number of representations by making bigger and bigger direct sums, or by acting on larger and larger sets. However, a finite group only has a finite number of distinct irreducible representations. (In fact, the number of distinct irreducible representations exactly equals the number of conjugacy classes in the group. We will see this down below). Every other representation in the universe for that group is just built by stacking these few fundamental irreducible blocks together.

#### Permutation Modules & Representations
We define a permutation matrix $P(g)$ of an element $g$. It defines whether $g$ permutes the $i^{th}$ element into the $j{th}$ element of the set. We construct this matrix by placing $1$ in row $i$, column $j$ when $g$ maps the $j$-th element to the $i$-th element, and $)$ everywhere else. 

 $P(g)$ is not a property of just the group element $g$ alone. The matrix $P(g)$ depends on the set $\Omega$ it is acting on. The exact same group $G$ will yield different matrices $P(g)$ if you let it act on a set of 3 points versus a set of 10 points.

A permutation representation specifically comes from the group acting on a finite set $\Omega$ (like permuting the 8 corners of a cube), which we then convert into vector matrices. 

Let a finite group $G$ act on a finite set $\Omega = \{1, 2, \dots, n\}$. To analyze a permutation action with linear algebra, convert the set $\Omega$ into a complex vector space $V = \mathbb{C}^\Omega \cong \mathbb{C}^n$.

Assign a basis vector $e_\alpha$ to each element $\alpha \in \Omega$. Any vector $v \in V$ is a formal linear combination:

$$v = \sum_{\alpha \in \Omega} c_\alpha e_\alpha, \quad c_\alpha \in \mathbb{C}$$
    
Each group element $g \in G$ acts linearly on $V$ by permuting the basis vectors:

$$P(g) e_\alpha = e_{g\alpha}$$
    
In coordinates, $P(g)$ is an $n \times n$ permutation matrix with entries:
    
$$(P(g))_{\alpha \beta} = \begin{cases} 1 & \text{if } g\beta = \alpha \\ 0 & \text{otherwise} \end{cases}$$
    
Because $P(gh) = P(g)P(h)$, the assignment $g \mapsto P(g)$ is a matrix representation of $G$ on $V$.

If we look at this as modules instead of matrices, if $G$ is a subgroup of the symmetry group $S_n$, then this module is called the permutation module and $e_{\alpha} \dots e_{\eta}$ are called the natural basis of the vector space. Since the only element of $G$ which fixes every $v_i$ is the identity, we see that the permutation module is a faithful $FG$-module. And from Cayley's theorem, we know that every $G$ is isomorphic to a subgroup of some symmetry group. Thus, any group has a faithful $FG$-module.

Note that a module can give many representations based on different choices of basis vectors to write our representation matrices in. 

For example, say an $FG$-module defines an abstract linear action of each group element $g \in G$ on the space $V$ via $v \mapsto vg$. Once you choose an ordered basis of vectors $\mathscr{B} = \{v_1, \dots, v_n\}$, each basis vector transforms under $g$ into some new vector $v_i g \in V$. Because $\mathscr{B}$ is a basis, that resulting vector can be written uniquely as a linear combination of the basis vectors: $v_i g = \sum_{j=1}^n a_{ij} v_j$.
    
The coefficients $a_{ij} \in F$ form the entries of the matrix $[g]_{\mathscr{B}}$:

$$[g]_{\mathscr{B}} = \begin{pmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \dots & a_{nn} \end{pmatrix} \in \operatorname{GL}(n, F)$$

The underlying $FG$-module $V$ is a single coordinate-free object. However, there are infinitely many choices of $n$x$n$ vector bases $\mathscr{B}, \mathscr{B}', \dots$ for $V$. From this, we can see that all such representations are equivalent.

These resulting representations are related by a change-of-basis matrix $P$:

$$[g]_{\mathscr{B}'} = P^{-1} [g]_{\mathscr{B}} P \quad \forall g \in G$$

#### Subspaces
    
A subspace $W \subseteq V$ is called $G$-invariant (or a subrepresentation) if applying any permutation keeps vectors inside $W$:
    
$$w \in W \implies P(g)w \in W \quad \text{for all } g \in G$$
    
An invariant subspace $W \subseteq V$ is irreducible (or simple) if $W \neq \{0\}$ and its only $G$-invariant subspaces are $\{0\}$ and $W$ itself. It represents a minimal, indivisible building block of symmetry. 

An (irreducible) invariant subspace of a $FG$-module is also an (irreducible) $FG$-module. 

**Example**

Let $G = C_3 = \langle a \mid a^3 = 1 \rangle$, and let $V$ be the 3-dimensional $FG$-module where $V$ has basis $v_1, v_2, v_3$, and the group elements act on the basis as follows:

$$v_1 1 = v_1, \quad v_2 1 = v_2, \quad v_3 1 = v_3$$

$$v_1 a = v_2, \quad v_2 a = v_3, \quad v_3 a = v_1$$

$$v_1 a^2 = v_3, \quad v_2 a^2 = v_1, \quad v_3 a^2 = v_2$$

Put $w = v_1 + v_2 + v_3$, and let $W = \operatorname{sp}(w)$, the 1-dimensional subspace spanned by $w$. Since

$$w 1 = w a = w a^2 = w,$$

$W$ is an $FG$-submodule of $V$.

However, $\operatorname{sp}(v_1 + v_2)$ is not an $FG$-submodule, since:

$$(v_1 + v_2)a = v_2 + v_3 \notin \operatorname{sp}(v_1 + v_2)$$

**Projections**
Let $V$ be an $FG$-module and let $W$ be an $FG$-submodule of $V$. An $F$-linear map (vector space homomorphism) $\pi: V \to V$ is called a projection from $V$ to $W$ if:

1.  $\operatorname{im}(\pi) = W$
    
2.  $w\pi = w$ for all $w \in W$ (meaning $\pi$ acts as the identity on $W$)
3. Because $w\pi = w$ for any element in the image, applying the map twice yields:

$$v\pi^2 = (v\pi)\pi = v\pi \quad \text{for all } v \in V$$

that is, $\pi^2 = \pi$ (the map is idempotent).

Any idempotent linear operator $\pi$ automatically induces an internal direct sum decomposition of the vector space:

$$V = \operatorname{im}(\pi) \oplus \ker(\pi) = W \oplus \ker(\pi)$$

Every vector splits uniquely as $v = v\pi + (v - v\pi)$, where $v\pi \in W$ and $(v - v\pi) \in \ker(\pi)$.

**IMPORTANT!**
* Not every subspace is an $FG$-module, but a subspace that is $G$-invariant is an $FG$-submodule. A vector subspace $W \subseteq V$ is merely closed under addition and scalar multiplication ($F$). For $W$ to be an $FG$-submodule (and hence an $FG$-module in its own right), it must also be closed under the action of the group $G$.

* An $FG$-module need not necessarily be a subspace of $V$. A good example is one we will show below where the quotient is a module, and therefore is a vector space but not a subspace of $V$ (though it is isomorphic to an actual subspace of $V$).

* For a general $FG$-module like the quotient $V/W$, whether it is isomorphic (as an $FG$-module) to an actual submodule of $V$ depends on whether $V$ is completely reducible. We can figure this out from Maschke's Theorem, which we will see below. 

**Example**

Suppose that $V$ is a reducible $FG$-module, so that there is an $FG$-submodule $W$ with 0 < dim $W$ < dim $V$. Take a basis $B_1$ of $W$ and extend it to a basis $B$ of $V$. Then for all $g \in G$, the matrix $[g]_B$ has the form

$$\begin{pmatrix} X_g & 0 \\ Y_g & Z_g \end{pmatrix} $$

where $X_g$ is $k$x$k$ ($k$ = dim $W$).

$Z_g$ is not just an arbitrary block of numbers; the map $g \mapsto Z_g$ is a genuine representation corresponding to the quotient module $V/W$.

The quotient vector space $V/W$ consists of cosets:

$$V/W = \{v + W \mid v \in V\}$$

Its dimension is $\dim(V/W) = \dim V - \dim W = n - k$.

The Basis of $V/W$: Let the extended basis of $V$ be:

$$\mathscr{B} = \{\underbrace{w_1, \dots, w_k}_{\mathscr{B}_1 \text{ (basis of } W)}, \underbrace{u_{1}, \dots, u_{n-k}}_{\text{complementary vectors}}\}$$

Then the cosets $\overline{\mathscr{B}} = \{u_1 + W, \dots, u_{n-k} + W\}$ form a basis for $V/W$.

$V/W$ is **not** a subspace of $V$. It cannot be a subspace because its elements are not vectors in $V$; they are **entire subsets (cosets)** of $V$.

Moreover a subspace of $V$ must contain the zero vector $0 \in V$. The zero element of the quotient space $V/W$ is the entire subspace $W$ itself: $0_{V/W} = 0 + W = W$.

A common source of confusion is conflating a complementary subspace with the quotient space:

A complementary subspace is a genuine subspace $U \le V$ such that $V = W \oplus U$ as vector spaces. When you choose basis vectors $\{u_1, \dots, u_{n-k}\}$, their span:

$$U = \operatorname{span}_F\{u_1, \dots, u_{n-k}\}$$

is a subspace of $V$.
    
The problem with $U$ is that while $U$ is a vector subspace of $V$, it is not necessarily an $FG$-submodule. Group operations often kick vectors out of $U$: $u_i \in U \quad \not\implies \quad u_i g \in U$
    
Instead, $u_i g$ generally has components along both $W$ and $U$:
    
$$u_i g = \underbrace{w}_{\in W} + \underbrace{u'}_{\in U}$$
    
The matrix block $Y_g$ records that non-zero $w \in W$ portion.
    
Because $U$ fails to be stable under $G$, we mod out by $W$. In the quotient space, the unwanted piece $w \in W$ gets mapped to zero:
    
$$(u_i + W)g = u_i g + W = (w + u') + W = u' + W$$
    
By collapsing $W$ to $0$, the group action becomes well-defined and closed.

**Example in $\mathbb{R}^2**

Consider $V = \mathbb{R}^2$, and let $W$ be the $x$-axis:

$$W = \{(x, 0) \mid x \in \mathbb{R}\}$$

$W$ is a 1-dimensional subspace of $\mathbb{R}^2$. The quotient space $V/W$ is the collection of all horizontal lines:

$$(0, y) + W = \{(x, y) \mid x \in \mathbb{R}\}$$
    
Each horizontal line is a single element of $V/W$.
    
Now consider a shear transformation matrix acting on row vectors:
    
$$g = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$$
    
Choose the complementary subspace $U$ as the $y$-axis, spanned by $u = (0, 1)$. Apply $g$ to $u$:

$$(0, 1) \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix} = (1, 1) = \underbrace{(1, 0)}_{\in W} + \underbrace{(0, 1)}_{\in U}$$
        
Notice that $(1, 1)$ does **not** stay on the $y$-axis ($U$). The transformation introduced a component $(1, 0)$ inside $W$. That component is precisely what produces $Y_g \neq 0$.
        
In the quotient space $V/W$, we project out the $x$-direction:
        
$$(u + W)g = (1, 1) + W = (0, 1) + W = u + W$$
        
The coset moves to itself, giving the representation matrix $Z_g = (1)$ without any spillover.
        
$V/W$ is an abstract vector space isomorphic to $U$, but it lives at a different structural level than a subspace.

**Example with explicit calculation of transformation matrices**

Let $G = C_3 = \langle a \mid a^3 = 1 \rangle$ and let $V$ be the 3-dimensional $FG$-module with basis $\{v_1, v_2, v_3\}$ such that:

$$v_1 a = v_2, \quad v_2 a = v_3, \quad v_3 a = v_1$$

$V$ is a reducible $FG$-module and has an $FG$-submodule $W = \operatorname{sp}(v_1 + v_2 + v_3)$.

Let $\mathcal{B}$ be the new basis $\{b_1, b_2, b_3\}$ of $V$, defined by:

$$b_1 = v_1 + v_2 + v_3$$

$$b_2 = v_1$$

$$b_3 = v_2$$

Notice that from this basis, $v_3$ can be expressed in terms of the basis vectors as:

$$v_3 = b_1 - b_2 - b_3$$

The action of $a$ on the original vectors is:

$$v_1 a = v_2, \quad v_2 a = v_3, \quad v_3 a = v_1$$

Now compute how each basis vector $b_i$ transforms under $a$:

$$b_1 a = (v_1 + v_2 + v_3)a = v_1 a + v_2 a + v_3 a = v_2 + v_3 + v_1 = b_1$$

In coordinates with respect to $\mathscr{B} = \{b_1, b_2, b_3\}$:

$$b_1 a = \mathbf{1}b_1 + \mathbf{0}b_2 + \mathbf{0}b_3 \implies \text{Row 1} = \begin{pmatrix} 1 & 0 & 0 \end{pmatrix}$$
    
Now for the second row:

$$b_2 a = v_1 a = v_2 = b_3$$
    
In coordinates with respect to $\mathscr{B}$:
    
$$b_2 a = \mathbf{0}b_1 + \mathbf{0}b_2 + \mathbf{1}b_3 \implies \text{Row 2} = \begin{pmatrix} 0 & 0 & 1 \end{pmatrix}$$
    
The third row ($b_3 a$):
    
$$b_3 a = v_2 a = v_3 = b_1 - b_2 - b_3$$
    
In coordinates with respect to $\mathscr{B}$:
    
$$b_3 a = \mathbf{1}b_1 - \mathbf{1}b_2 - \mathbf{1}b_3 \implies \text{Row 3} = \begin{pmatrix} 1 & -1 & -1 \end{pmatrix}$$
    
Assembling these rows gives $[a]_{\mathscr{B}}$:

$$[a]_{\mathscr{B}} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & -1 & -1 \end{pmatrix}$$

Similarly for $[a^2]_{\mathscr{B}}$:

Since this is a representation, $[a^2]_{\mathscr{B}} = [a]_{\mathscr{B}}^2$:

$$[a^2]_{\mathscr{B}} = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & -1 & -1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 0 \\ 0 & 0 & 1 \\ 1 & -1 & -1 \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 \\ 1 & -1 & -1 \\ 0 & 1 & 0 \end{pmatrix}$$

The top-left entry across all three matrices is:

$$[1] \mapsto (1), \quad [a] \mapsto (1), \quad [a^2] \mapsto (1)$$

This $1 \times 1$ block corresponds directly to the 1-dimensional subspace spanned by the first basis vector:

$$W = \operatorname{sp}(b_1) = \operatorname{sp}(v_1 + v_2 + v_3)$$

For any vector $w = c b_1 \in W$ and any group element $g \in \{1, a, a^2\}$:

$$w g = (c b_1) g = c (b_1 g) = c b_1 = w$$

Every element of the group acts as the identity transformation (multiplication by $1$) on this subspace. By definition, a representation where $g \mapsto (1)$ for all $g \in G$ is called the trivial representation.
    
Any 1-dimensional module is automatically irreducible because the only vector subspaces of a 1-dimensional space are $\{0\}$ and the space itself—there are simply no non-trivial proper subspaces available.

#### Group Algebras

Abstractly, a vector does not have to be an arrow with spatial coordinates. In abstract algebra,  a vector space is defined entirely by how elements behave under addition and scalar multiplication, not by what the elements "look like." Any set can serve as a basis by declaring its elements to be the basis vectors.

For example, we could use the group elements as basis vectors. Let $G = \{g_1, g_2, \dots, g_n\}$ be a finite group of order $n$. To turn this set into a basis for a vector space $V$:

You treat each symbol $g_i$ as a distinct unit axis, exactly like the standard basis vectors $e_1, e_2, \dots, e_n$ in $\mathbb{R}^n$.
    
A general vector $v \in V$ is a linear combination:
    
$$v = c_1 g_1 + c_2 g_2 + \dots + c_n g_n = \sum_{i=1}^n c_i g_i \quad (c_i \in F)$$
    
We also define vector addition and scalar multiplication:
    
$$\left(\sum_{i=1}^n a_i g_i\right) + \left(\sum_{i=1}^n b_i g_i\right) = \sum_{i=1}^n (a_i + b_i) g_i$$
        
$$\alpha \left(\sum_{i=1}^n c_i g_i\right) = \sum_{i=1}^n (\alpha c_i) g_i$$
        
Because these operations satisfy all standard vector space axioms (associativity, distributivity, existence of zero, etc.), this collection forms a genuine $n$-dimensional vector space over $F$.

The reason for promoting group elements to basis vectors is to define multiplication between vectors, which turns this vector space into the group algebra $FG$ (and the module into something called the regular module):

$$\left(\sum_{g \in G} a_g g\right) \left(\sum_{h \in G} b_h h\right) = \sum_{g, h \in G} (a_g b_h)(gh)$$

The group multiplication rule $g \cdot h = gh$ dictates how basis elements multiply, while vector addition allows you to add and scale them.

If this feels like a ring or a field where we have two operations: addition and multiplication, compared to groups where there is only one operation, you're spot on. That is precisely why the object is named an algebra (specifically, the group algebra $FG$):

$$\text{Group Algebra } FG = \text{Ring} + \text{Vector Space (over a field } F\text{)}$$

Why don't just call it a ring and stop there? Because $FG$ contains two layers of addition and multiplication: Internal ring multiplication: multiplying two group linear combinations via the group's product rule; & external scaling: scaling linear combinations by elements of $F$.

This allows you to deploy tools that only exist in vector spaces—like dimension, kernels, bases, and linear projections—to solve problems about the multiplicative structure of the group.

Now if you take the vector space $V = FG$, built using the group elements as its linearly independent basis, it forms what is called the regular $FG$-module. This module is faithful.

In this module, the group $G$ acts on the space by right multiplication: you take a basis vector $g_i$, multiply it by a group element $g$, and get a new basis vector $g_k = g_i g$.
    
The set $\mathscr{B} = \{g_1, g_2, \dots, g_n\}$ is the natural basis of this vector space. They are the "coordinate axes" of your space, not the representation itself.
    
The representation is the action—specifically, the mapping that assigns an $n \times n$ matrix $[g]_{\mathscr{B}}$ to every group element $g$. Because multiplying by $g$ simply rearranges the group elements (and therefore the basis vectors) without absorbing them or leaving any out, the matrices of the regular representation are purely permutation matrices (matrices with exactly one $1$ in each row and column, and $0$ elsewhere).

If this reminds you of the permutation representation we discussed above, then you're not wrong. The regular representation is not merely close to a permutation representation—it is a permutation representation. Specifically, it is the permutation representation obtained when a group $G$ acts on itself via right multiplication.

Recall that a permutation representation requires two things: a finite set $\Omega$ that the group $G$ acts on by permutations. And a vector space $V$ having $\Omega$ as its basis.    

For the regular representation, the set is the set of group elements themselves. The group action on this set is right multiplication. While any set action can yield a permutation representation, the regular representation is important because it is faithful.

What makes the regular module so vital in representation theory is that it is the "master container." When you decompose the regular module over the complex numbers, it contains every single irreducible representation of the group $G$, with each one appearing exactly as many times as the the irreducible representation's dimension. Looking back the multiplicity formula we gave earlier, for the regular representation we have $m_i = d_i$.

Now there's one more thing you can do. Instead of just allowing a single group element $g$ to act on a vector, you can allow linear combinations of group elements to act on a vector.

Up until now, the rule was strict: you take a vector $v \in V$, and you hit it with a single symmetry $g \in G$ to get a new vector $vg$. But the group algebra $FG$ contains elements like $r = 3g_1 - 2g_2$. 

Now we define how an element like $r$ interacts with $V$ by distributing the action linearly:

$$v(3g_1 - 2g_2) = 3(vg_1) - 2(vg_2)$$

Formally, for any $r = \sum_{g \in G} c_g g \in FG$, the natural extension is:

$$vr = \sum_{g \in G} c_g (vg)$$

Why do we need this? If you only have the group $G$, you can only apply individual symmetries (e.g., "rotate by 90 degrees"). But in representation theory, the most powerful tools are averages and projections. By extending the multiplication to all of $FG$, you upgrade $V$ from being just a "space that gets pushed around by group elements" to a full module over the ring $FG$. This allows you to treat entire sums of symmetries as single, unified operators (like $P$) that act directly on your vectors.

Now we have closure, associativity and distibutivity over multiplication and addition between vectors, group algebra elements and scalars over $F$.

This is where representation theory shifts from being a branch of group theory into a branch of ring theory. Because $V$ satisfies all these axioms, we can stop worrying about individual group matrices and instead use powerful, global ring-theoretic tools (like ideals and ring homomorphisms) to study the symmetries.

#### Maschke’s Theorem

Over $\mathbb{C}$, every representation of a finite group is completely reducible. That is, $V$ decomposes into a direct sum of mutually disjoint irreducible invariant subspaces:

$$V = W_1 \oplus W_2 \oplus \dots \oplus W_k$$

This means every vector $v \in V$ can be written uniquely as $v = w_1 + \dots + w_k$ with $w_i \in W_i$, and the group $G$ never mixes vectors from different subspaces $W_i$. Since $w_i$ is $G$-invariant, it is also a submodule. Note that Maschke's Theorem requires char($F$) to not be a divisor of $|G|$ ($C$ is a field with characteristic $0$.). So Maschke's Theorem is not applicable when we are working with $F(2)$ with the group $G_2(2)$ of order 12096. 

Maschke's Theorem guarantees that if we end up with a representation matrix for $V$ such that 

$$\begin{pmatrix} X_g & 0 \\ Y_g & Z_g \end{pmatrix} $$

then we can find some other basis such that we can transform this representation into

$$\begin{pmatrix} X_g & 0 \\ 0 & Z_g \end{pmatrix} $$

i.e. it become block diagonal. The similarity transformation $T [a]_\mathscr{B} T^{-1}$ cleanly removes $Y_g$.

Maschke's Theorem therefore implies that every $FG$-module can be written as a direct sum of irreducible $FG$-submodules. These submodules are called composition factors. Thus, to understand $FG$-modules, we must understand irreducible $FG$-submodules. When $F=\mathbb{C}$, we can say any irreducible submodule must be isomorphic to one of the irreducible submodules in the direct sum.

What happens when Maschke's Theorem fails? We use Modular Representation Theory. The group algebra $FG$ is not semisimple. Modules can form non-trivial un-splittable chains (extensions) where $Y_g \neq 0$ permanently, leading to non-trivial Jordan block structures.

#### Character Tables, Isomorphism and Grouping into Multiplicities
A representation translates abstract group elements into matrices, turning abstract group multiplication into standard matrix multiplication. However, matrices hold too much data. A $10 \times 10$ matrix has 100 entries. Mathematicians discovered that almost all the vital structural data of the matrix is captured by its trace (the sum of the diagonal elements). This trace is called the Character of the representation.

A Character Table is a grid that records these traces for different representations across the conjugacy classes of the group. It acts as the structural DNA of the group. It compresses complex non-commutative algebraic geometry into a simple spreadsheet of numbers, allowing mathematicians to identify normal subgroups, centers, and factoring properties just by looking at the rows and columns.

The character of the representation is the function $\chi: G \to \mathbb{C}$ tracking the traces of the matrices:

$$\chi(g) = \operatorname{Tr}(\rho g)$$

**Do many representations have the same character?** No! This is one of the most powerful theorems in the subject: Two representations have the exact same character if and only if they are identical (isomorphic). The character is a perfect mathematical fingerprint. If the characters match, the representations are built out of the exact same irreducible blocks in the exact same quantities.   

If $x$ and $y$ are conjugate elements of the group $G$, then they have the same character in all representations of $G$. 

In a permutation representation, because a permutation matrix has a $1$ on the diagonal if and only if $g\alpha = \alpha$, the character simply counts fixed points:

$$\chi(g) = \big\vert{}\{\alpha \in \Omega : g\alpha = \alpha\}\big\vert{}$$



Two irreducible subspaces $W_a$ and $W_b$ are isomorphic as representations if there is an invertible linear map between them that commutes with every $P(g)$.

Let $V_1, V_2, \dots, V_s$ denote the distinct, non-isomorphic types of irreducible representations that appear in $V$. We group isomorphic copies together:

$$V \cong \underbrace{(V_1 \oplus \dots \oplus V_1)}_{m_1 \text{ copies}} \oplus \underbrace{(V_2 \oplus \dots \oplus V_2)}_{m_2 \text{ copies}} \oplus \dots \oplus \underbrace{(V_s \oplus \dots \oplus V_s)}_{m_s \text{ copies}} = \bigoplus_{k=1}^s V_k^{\oplus m_k}$$

Note that this is not different from what we saw just a little earlier. 

$$V = W_1 \oplus W_2 \oplus W_3 \oplus W_4 \oplus W_5$

Where $W_1$ and $W_2$ are both Type $V_1$, $W_3$ is Type $V_2$, and $W_4$ and $W_5$ are both Type $V_3$.

We then "group" the identical copies together:

$$V = (\text{Type} V_1 \oplus \text{Type} V_1) \oplus (\text{Type} V_2) \oplus (\text{Type} V_3 \oplus \text{Type} V_3)$$

Each $V_k$ is called an irreducible constituent of the permutation representation.
    
The integer $m_k \ge 1$ is the multiplicity of the constituent $V_k$. Note that $dim(V) = \sum_{i=1}^k m_i d_i$ where the dimension of each $V_i$ is $d_i$. 
    
The character decomposes into a sum of irreducible characters $\chi_k = \operatorname{Tr}\vert{}_{V_k}$: $\chi = \sum_{k=1}^s m_k \chi_k$
    
The representation is called multiplicity-free if every $m_k = 1$.

**Example**

if $G = D_6$ (the dihedral group of order $6$, symmetries of an equilateral triangle), then the complex group algebra decomposes as:

$$\mathbb{C}G = U_1 \oplus U_2 \oplus U_3 \oplus U_4$$

where $U_1, U_2$ are non-isomorphic $1$-dimensional $\mathbb{C}G$-modules, and $U_3, U_4$ are isomorphic irreducible $2$-dimensional $\mathbb{C}G$-modules ($U_3 \cong U_4$).

This illustrates the general decomposition theorem (Theorem 11.9) for the regular representation:

$$\mathbb{C}G \cong \bigoplus_{i=1}^k d_i V_i$$

where each distinct irreducible module $V_i$ appears with multiplicity equal to its dimension $d_i = \dim V_i$:

-   $U_1$ occurs once, with $\dim U_1 = 1$;
    
-   $U_2$ occurs once, with $\dim U_2 = 1$;
    
-   The $2$-dimensional irreducible module type of $U_3$ occurs twice ($U_3 \oplus U_4$), with $\dim U_3 = 2$.
    
Summing the dimensions confirms the total dimension of the regular module:

$$\dim(\mathbb{C}G) = \vert{}G\vert{} = 1^2 + 1^2 + 2^2 = 1 + 1 + 4 = 6$$

### Schur’s Lemma

Let $U$ and $W$ be two irreducible representations of $G$. Loosely, Schur's Lemma says that $U$ and $W$ are either isomorphic or the homomorphism is the zero-map i.e. the kernel is the whole of $U$ . If they are isomorphic, then the map between the two is a scalar multiple of identity 

More formally, let $T: U \to W$ be a linear map satisfying $T P(g) = P(g) T$ for all $g \in G$:

1.  If $U \not\cong W$, then $T = 0$ (no non-zero commuting maps exist between distinct irreps).
    
2.  If $U = W$, then $T = \lambda I$ for some scalar $\lambda \in \mathbb{C}$ (the only commuting maps from an irrep to itself are scalar multiplications).

In terms of the intertwining operator, the lemma is stating that if two representations are  irreducible, any intertwining operator $T$ between them is either the zero matrix or an invertible matrix (making them equivalent). Furthermore, an intertwining operator from an irreducible representation to itself must be a scalar multiple of the identity matrix.

You can also give Schur's Lemma as: 

For any field $F$: If $V, W$ are irreducible, then $\operatorname{Hom}_{FG}(V, W) = \{0\}$ if $V \not\cong W$, and if $V \cong W$, every non-zero map is an isomorphism ($\operatorname{End}_{FG}(V)$ is a division algebra).
    
Over an algebraically closed field (e.g., $\mathbb{C}$): $\operatorname{End}_{\mathbb{C}G}(V) \cong \mathbb{C}$, meaning every endomorphism is uniquely of the form $\lambda I$.

There is also another way to look at Schur's Lemma. Suppose $\rho$ is an irreducible representation of $G$ into $\operatorname{GL}(n, \mathbb{C})$ acting on an $n$-dimensional complex vector space $V$. The set of all $n \times n$ matrices that commute with the representation matrix of every group element is called the Centralizer Algebra ("centralizer" because the centralizer of a group element is the set of all elements that leave the element fixed under conjugation, which is the same thing as commuting with it). Any $n \times n$ matrix $A$ that belongs to the Centralizer Algebra must be a scalar multiple of the identity matrix.

To see why, a matrix commuting with the group representation means:

$$A(g\rho) = (g\rho)A \quad \text{for all } g \in G$$

where $g$ is an abstract group element, $\rho$ is the representation map, and therefore $g\rho$ denotes the actual representation matrix. For brevity, let us denote the operator $(g\rho)$ simply by $g$.

Because the field $\mathbb{C}$ is algebraically closed, the linear transformation $A$ has at least one eigenvalue $\lambda \in \mathbb{C}$. Let $V_\lambda$ denote the eigenspace corresponding to $\lambda$:

$$V_\lambda = \{v \in V \mid Av = \lambda v\}$$

Since $\lambda$ is an eigenvalue, $V_\lambda \neq \{0\}$. Now let $v \in V_\lambda$ and $g \in G$. Because $A$ commutes with $g$:

$$A(gv) = (Ag)v = (gA)v = g(Av) = g(\lambda v) = \lambda(gv)$$

Thus, the vector $gv$ is also an eigenvector of $A$ with the same eigenvalue $\lambda$, which means $gv \in V_\lambda$. Because this holds for all $g \in G$ and all $v \in V_\lambda$, the eigenspace $V_\lambda$ is a non-zero $G$-invariant subspace of $V$ (an $FG$-submodule).

However, the representation $\rho$ is given to be irreducible, which implies the only non-zero $G$-invariant subspace of $V$ is $V$ itself. Therefore:

$$V_\lambda = V$$

Since every vector in $V$ is an eigenvector of $A$ with eigenvalue $\lambda$, the operator acts as a uniform scaling across the entire space. **Hence, $A = \lambda I_n$. All commuting matrices must be of this form.**

**Aside:** In quantum mechanics, Schur's Lemma is the mathematical core behind superselection rules and the evaluation of central charges/Casimir operators. If a Hamiltonian $\hat{H}$ commutes with every generator of a symmetry group $G$ acting irreducibly on a multiplet space, $\hat{H}$ must act as a pure scalar energy eigenvalue $E \cdot \hat{I}$ on that entire multiplet (explaining energy degeneracy in spherical/rotational symmetry).

---

The above result is used as a test to see if a representation is irreducible, though it is a highly inefficient method. In practice, one easy way it to check if the representation is 1-dimensional, which is trivially irreducible. Other than that, the standard way is to check the inner product of a character with itself and sum those over all elements of the group.

The character inner product is a mathematical operation that measures how much two representations "overlap" or share structural components. It functions as a geometric dot product for the space of group characters.

$$\langle \chi, \psi \rangle = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \chi(g) \overline{\psi(g)}$$

$\vert{}G\vert{}$ is the total number of elements in the group, and $\overline{\psi(g)}$ is the complex conjugate of the character value.

Because characters evaluate to the same trace for any elements within the same conjugacy class, this formula is the same as:

$$\langle \chi, \psi \rangle = \frac{1}{\vert{}G\vert{}} \sum_{i=1}^k \vert{}C_i\vert{} \chi(g_i) \overline{\psi(g_i)}$$

$\vert{}C_i\vert{}$ is the number of elements in that class, and $g_i$ is a representative element chosen from it.

This operation is the primary computational engine of character theory due to three rigid rules:

Irreducible characters are perfectly orthogonal to one another. If $\chi_i$ and $\chi_j$ are distinct irreducible characters, they have zero overlap: $\langle \chi_i, \chi_j \rangle = 0$.

If you have a large, reducible module $V$ with character $\chi_V$, you can determine exactly how many times an irreducible module $W_i$ (with character $\chi_i$) appears inside it by calculating their inner product: $m_i = \langle \chi_V, \chi_i \rangle$.

A representation is strictly irreducible if and only if its character's inner product with itself is unity: $\langle \chi, \chi \rangle = 1$. If it is greater than 1, which means it is composed of multiple irreducible characters, it is reducible.


### The Centralizer Algebra
#### The Centre of the Group Algebra: $Z(\mathbb{C}G)$

The centre is defined abstractly as the set of elements $z$ inside the group algebra $\mathbb{C}G$ that commute with every element $r$ in $\mathbb{C}G$: $zr = rz$.

-   It is a subspace of the group algebra itself.
    
-   It exists entirely independently of any specific matrix representation. It is an intrinsic property of the group $G$.
    
-   For abelian groups, because everything commutes, the centre is the entire group algebra.
    
-   The dimension of this subspace exactly equals the number of irreducible representations of $G$. We will show why, shortly.

#### The Centralizer Algebra of a Representation: $\operatorname{End}_{\mathbb{C}G}(V)$

This is what we were discussing with Schur's Lemma above. This is the set of all $n \times n$ matrices $A$ that commute with the representation matrices $g\rho$.This algebra lives inside the space of physical transformations (matrices acting on a specific vector space $V$). It depends entirely on which representation $\rho$ you are looking at.

Because elements $z \in Z(\mathbb{C}G)$ commute with every group element $g$ in the abstract algebra, when you plug $z$ into any representation $\rho$, the resulting matrix $\rho(z)$ will commute with every representation matrix $\rho(g)$. This means the representation maps the Centre directly into the Centralizer Algebra.

If the representation is irreducible, Schur's Lemma kicks in immediately. Because $\rho(z)$ commutes with everything, Schur's Lemma forces $\rho(z)$ to be a scalar multiple of the identity:

$$\rho(z) = \lambda_z I_n$$

If there is a faithful irreducible $\mathbb{C}G$-module, the center of the group $G$, $Z(G)$ is cyclic. 
 
#### The Orbitals Span $\mathcal{A}$

Now let's see how things work out with the centralizer algebra and Schur's Lemma if we use a permutation representation.  

We first look at how orbitals can be represented via matrices, called Adjacency Matrices. $A_1, \dots, A_r$ are the $0$-$1$ adjacency matrices of orbitals $R_1, \dots, R_r$ , defined as:

$$(A_i)_{\alpha \beta} = \begin{cases} 1 & \text{if } (\alpha, \beta) \in R_i \\ 0 & \text{otherwise} \end{cases}$$

The centralizer algebra (or commutant) $\operatorname{End}_G(V)$ is the set of all $n \times n$ complex matrices $M$ that commute with the group action:

$$\mathcal{A} = \{M \in M_n(\mathbb{C}) : M P(g) = P(g) M \text{ for all } g \in G\}$$


Let $M \in M_n(\mathbb{C})$. The commutation condition $M P(g) = P(g) M$ can be evaluated entry-by-entry:

$$(P(g^{-1}) M P(g))_{\alpha \beta} = M_{g\alpha, g\beta}$$

So $M$ commutes with all $P(g)$ if and only if:

$$M_{\alpha, \beta} = M_{g\alpha, g\beta} \quad \text{for all } g \in G \text{ and all } \alpha, \beta \in \Omega$$

This condition forces the entries of $M$ to be constant along each orbit of $G$ on $\Omega \times \Omega$ (the orbitals $R_1, \dots, R_r$).

Then any matrix $M \in \mathcal{A}$ and is uniquely expressed as:

$$M = \sum_{i=1}^r c_i A_i, \quad c_i \in \mathbb{C}$$

Thus, $\{A_1, \dots, A_r\}$ forms a vector space basis for $\mathcal{A}$.

$\text{End}_G(V)$ is just the formal, mathematical name for the centralizer algebra. $\text{End}$ stands for Endomorphisms (linear maps from a vector space $V$ back to itself). The subscript $G$ means we only want the endomorphisms that commute with the group $G$ (i.e., $T P(g) = P(g) T$).

To determine what the commuting centralizer algebra matrices look like, we examine how a commuting map acts on the decomposed space $V = \bigoplus_{k=1}^s V_k^{\oplus m_k}$.

**Example**

Suppose an irreducible block $V_k$ is a $2$-dimensional space (a $2 \times 2$ block of symmetry).

Suppose this block appears with multiplicity $m_k = 3$ (there are 3 identical copies of it).

The total subspace holding these copies is $2 \times 3 = 6$-dimensional.

Therefore, the commuting matrix $M^{(k)}$ acting on this whole subspace is a $6 \times 6$ matrix.

But because of Schur's lemma, this $6 \times 6$ matrix is locked into a rigid grid where every $2 \times 2$ block is just a multiple of the identity matrix:

$$M^{(k)} = \begin{pmatrix} c_{11}I_2 & c_{12}I_2 & c_{13}I_2 \\ c_{21}I_2 & c_{22}I_2 & c_{23}I_2 \\ c_{31}I_2 & c_{32}I_2 & c_{33}I_2 \end{pmatrix}$$

Notice that this entire $6 \times 6$ matrix $M^{(k)}$ is completely controlled by just a $3 \times 3$ grid of regular complex numbers. That grid of regular numbers:

$$C = \begin{pmatrix} c_{11} & c_{12} & c_{13} \\ c_{21} & c_{22} & c_{23} \\ c_{31} & c_{32} & c_{33} \end{pmatrix}$$

is the matrix of scalars $(c_{ab})$.

So, the freedom you have to build the $6 \times 6$ matrix $M^{(k)}$ is exactly equivalent to freely choosing a $3 \times 3$ matrix of numbers. Therefore, the algebra of these commuting matrices is isomorphic to a "complete matrix algebra" of size $m_k \times m_k$.    

#### Dimension Formula for the Rank

$\mathcal{A}$ is isomorphic to the direct sum of complete matrix algebras: $\bigoplus_{k=1}^s M_{m_k}(\mathbb{C})$. Every matrix of $M_{m_k}(\mathbb{C})$ can be written as a linear combination of the basis of $r$ adjacency matrices. 

To show this, apply Schur’s Lemma to $V = \bigoplus_{k=1}^s V_k^{\oplus m_k}$:

-   Between two different constituents $V_j$ and $V_k$ ($j \neq k$), any commuting matrix acts as the zero block.
    
-   Within the block $V_k^{\oplus m_k} = \underbrace{V_k \oplus \dots \oplus V_k}_{m_k \text{ copies}}$, a linear map can mix the copies. If we write a map on this subspace as an $m_k \times m_k$ block matrix of operators:
    
    $$M^{(k)} = \begin{pmatrix} T_{11} & \dots & T_{1 m_k} \\ \vdots & \ddots & \vdots \\ T_{m_k 1} & \dots & T_{m_k m_k} \end{pmatrix}$$
    
    each sub-block $T_{ab}: V_k \to V_k$ must commute with $G$. By Schur's Lemma, each $T_{ab} = c_{ab} I_{d_k}$ for some complex number $c_{ab}$.
    
Therefore, the matrix of scalars $(c_{ab})$ can be any arbitrary $m_k \times m_k$ matrix with complex entries. The commuting operations on that sector form the full matrix algebra $M_{m_k}(\mathbb{C})$.

Summing across all irreducible constituents gives:

$$\mathcal{A} \cong \bigoplus_{k=1}^s M_{m_k}(\mathbb{C})$$

Now what is the dimension of a complete $m_k \times m_k$ matrix algebra? It has $m_k$ rows and $m_k$ columns, so it has exactly $m_k^2$ independent entries. If an irrep is $5$-dimensional, but it appears $3$ times in the decomposition ($m_k = 3$), the commuting matrix algebra for that block is $3 \times 3$, not $5 \times 5$.
    
The dimension of a direct sum is just the sum of the dimensions of its pieces. Thus, the dimension of the right side is $\sum_{k=1}^s m_k^2$.
    
But $\mathcal{A}$ has $r$ basis matrices and so is $r$-dimensional. Equating the dimensions of both sides gives: $r = \sum_{k=1}^s m_k^2$.

The rank $r$ (the number of orbitals) equals the sum of the squares of the multiplicities of the irreducible constituents.

A corollary of the isomorphism theorem is that the algebra is commutative if and only if the permutation character is multiplicity-free. Matrix multiplication in a complete matrix algebra $M_m(\mathbb{C})$ is commutative if and only if $m = 1$ ($1 \times 1$ matrices are ordinary numbers $\mathbb{C}$, whereas $m \times m$ matrices do not commute when $m \ge 2$). Hence:

$$\bigoplus_{k=1}^s M_{m_k}(\mathbb{C}) \text{ is commutative} \iff m_k = 1 \text{ for every } k$$

**Can we determine the number of irreps via the Class Equation?**

Yes! This is one of the most beautiful dualities in finite group theory. The Class Equation partitions the sheer number of elements in the group $\vert{}G\vert{}$ into the sizes of its conjugacy classes:

$$\vert{}G\vert{} = 1 + \vert{}C_2\vert{} + \vert{}C_3\vert{} + \dots + \vert{}C_k\vert{}$$

If you count the number of "buckets" (terms) in this equation, you get the integer $k$. That $k$ is the number of conjugacy classes, which mathematically guarantees there are exactly $k$ distinct irreducible representations.

Furthermore, this gives birth to a famous "dual" equation. While the class equation partitions $\vert{}G\vert{}$ using conjugacy class sizes, the representation theory partitions $\vert{}G\vert{}$ using the dimensions ($d_i$) of those $k$ irreducible representations:

$$\vert{}G\vert{} = d_1^2 + d_2^2 + d_3^2 + \dots + d_k^2$$

This equation follows from the $r = \sum_{k=1}^s m_k^2$ formula above if we choose the regular representation. Then $r = |G|$ and $m_k = d_k$.

**The Duality:**

-   You have exactly $k$ conjugacy classes (grouping the _group elements_).
    
-   You have exactly $k$ irreducible representations (grouping the _matrix actions_).
    
-   The sum of the sizes of the classes equals $\vert{}G\vert{}$.
    
-   The sum of the squares of the irrep dimensions equals $\vert{}G\vert{}$.
    
This is why, if you know the class equation of a group, you instantly know exactly how many irreducible representations exist before you even write down a single matrix.

Another aspect of the Centralizer Algebra is that closure under multiplication shows that, if $\mathcal{O}_1, \dots, \mathcal{O}_r$ are the orbitals of $G$ on $\Omega$, then we have:

$$A(\mathcal{O}_i) A(\mathcal{O}_j) = \sum_{k=1}^r p_{ij}^k A(\mathcal{O}_k)$$

for some constants $p_{ij}^k$, where $A$ is the Adjacency Matrix.

This formula also has a combinatorial proof which gives an explicit interpretation to these numbers: $p_{ij}^k$ is the number of points $\gamma \in \Omega$ such that $(\alpha, \gamma) \in \mathcal{O}_i$ and $(\gamma, \beta) \in \mathcal{O}_j$, where $(\alpha, \beta)$ is any fixed pair chosen from the orbital $\mathcal{O}_k$. Essentially, $p_{ij}^k$ is the number of points on orbital $k$ which is also on orbitals $i$ and $j$.

(This follows directly from the definition of matrix multiplication for zero-one adjacency matrices: the $(\alpha, \beta)$ entry of the product matrix $A(\mathcal{O}_i)A(\mathcal{O}_j)$ is given by $\sum_{\gamma \in \Omega} A(\mathcal{O}_i)_{\alpha \gamma} A(\mathcal{O}_j)_{\gamma \beta}$, which simply counts the number of intermediate vertices $\gamma$ where both the $(\alpha, \gamma)$ entry of the first factor and the $(\gamma, \beta)$ entry of the second factor are equal to $1$.)

Fix any ordered pair $(\alpha, \beta) \in \mathcal{O}_k$. The parameter $p_{ij}^k$ is the number of points $\gamma \in \Omega$ such that:

$$(\alpha, \gamma) \in \mathcal{O}_i \quad \text{and} \quad (\gamma, \beta) \in \mathcal{O}_j$$

This proves that the intersection numbers $p_{ij}^k$ are non-negative integers that depend solely on the chosen orbitals $i, j, k$, independent of the specific representative pair $(\alpha, \beta) \in \mathcal{O}_k$.

### Coherent Configurations

As we just discussed, the group symmetry of a permutation group forces the intermediate count $p_{ij}^k$ to be identical for every edge in that orbital. But we based it on the group structure, its action on the set, the orbitals etc. 

A coherent configuration is the purely combinatorial generalization of permutation groups: it keeps the regular numerical structure of group orbitals, even if no underlying group actually exists to produce it.

Formally, let the permutation group $G$ have $m$ orbits on $\Omega$, and have rank $r$ (the number of orbits on $\Omega^2 = \Omega \times \Omega$). An orbital is an orbit of $G$ on $\Omega^2$, that is, a set of ordered pairs invariant under the componentwise action of $G$. It is customary to regard such a set of pairs as a binary relation on $\Omega$. Accordingly, we denote the orbitals by $R_1, \dots, R_r$, and regard them as relations on $\Omega$.

If $\Omega_1, \dots, \Omega_m$ are the orbits of $G$ on $\Omega$, we choose the indexing convention so that, for $1 \le i \le m$,

$$R_i = \{(\alpha, \alpha) \mid \alpha \in \Omega_i\}$$

is the diagonal relation on the orbit $\Omega_i$. Let $\mathcal{R} = \{R_1, \dots, R_r\}$.

The relations $R_i \in \mathcal{R}$ satisfy the following fundamental properties:

1.  **Partition of $\Omega^2$:** The orbitals form a partition of the Cartesian product $\Omega \times \Omega$:
    
    $$\bigcup_{k=1}^r R_k = \Omega \times \Omega \quad \text{and} \quad R_j \cap R_k = \emptyset \quad \text{for } j \neq k$$
    
2.  **Diagonal Subsets:** The diagonal $\Delta = \{(\alpha, \alpha) \mid \alpha \in \Omega\}$ decomposes as the disjoint union of the first $m$ relations:
    
    $$\Delta = \bigcup_{i=1}^m R_i$$
    
    The number of diagonal orbitals is equal to $m$, the number of orbits of $G$ on $\Omega$. This provides an immediate structural check: $r \ge m$. In particular, if $G$ is transitive ($m = 1$), there is exactly one diagonal orbital $R_1 = \{(\alpha, \alpha) \mid \alpha \in \Omega\}$. 
    
3.  **Paired Relations (Converse Orbitals):** For each orbital $R_k \in \mathcal{R}$, the converse relation
    
    $$R_k^* = \{(\beta, \alpha) \mid (\alpha, \beta) \in R_k\}$$
    
    is also an orbital in $\mathcal{R}$ (often denoted $R_{k^*}$). If $R_k = R_k^*$, the orbital is called self-paired (or symmetric), corresponding to an undirected orbital graph.

4. **Intersection Numbers:** The number of intermediate points $\gamma \in \Omega$ with $(\alpha, \gamma) \in R_i$ and $(\gamma, \beta) \in R_j$ depends only on the orbital $R_k$ containing $(\alpha, \beta)$, because $G$ acts transitively on each orbital $R_k$.

In algebraic combinatorics, the partition $\Omega \times \Omega = \bigcup_{k=1}^r R_k$ together with the intersection numbers $p_{ij}^k$ forms a coherent configuration $(\Omega, \mathcal{R})$. If $G$ is the permutation group of $\Omega$ and $\mathcal{R}$ the associated set of orbitals of $G$, then this is called the coherent configuration of $G$.

When $G$ is transitive ($m = 1$), this coherent configuration is called homogeneous, which means the diagonal is a single orbital.

If we have commutativity:

$$p_{ij}^k = p_{ji}^k \quad \text{for all } i, j, k$$

This means: for a fixed pair $(\alpha, \beta) \in R_k$, the number of two-step paths that take an $i$-step followed by a $j$-step is exactly equal to the number of two-step paths that take a $j$-step followed by an $i$-step. This configuration is called an Association Scheme. 

If every relation is self-paired, $(\alpha, \beta) \in R_i \iff (\beta, \alpha) \in R_i$, this is a symmetric association scheme. If there is a directed edge $\alpha \to \beta$ in a relation, the reverse directed edge $\beta \to \alpha$ is also in the same relation. Thus, every relation graph becomes an undirected graph. Symmetry implies commutativity but not the other way around.

The definition of a coherent configuration can be phrased in the language of matrices. Given a binary relation $R$ on $\Omega$, we define its basis matrix $B(R)$ to be the matrix with rows and columns indexed by $\Omega$, with $(\alpha, \beta)$ entry $1$ if $(\alpha, \beta) \in R$, and $0$ otherwise. This is pretty much the adjacency matrix of an orbital of a permutation group, but in the spirit of generalization of coherent configurations, we call this the characteristic function of the relation $R$.

If $I$ denotes the identity matrix, and $J$ denotes the all-ones matrix of appropriate size ($\vert{}\Omega\vert{} \times \vert{}\Omega\vert{}$). The following translates the four axioms we gave above of a coherent configuration directly into matrix algebra:

Let $\mathcal{A} = \{A_1, \dots, A_r\}$ be a set of non-zero $0\text{--}1$ matrices with rows and columns indexed by $\Omega$. Then $\mathcal{A}$ is the set of basis matrices of a coherent configuration on $\Omega$ if and only if the following conditions are satisfied:

1.  Partition of the Complete Graph: $\sum_{i=1}^r A_i = J$
        
2.  Partition of the diagonal: There exists a subset $\mathcal{A}_0 \subseteq \mathcal{A}$ whose sum is the identity matrix: $\sum_{A_i \in \mathcal{A}_0} A_i = I$
    
    (If the configuration is homogeneous / the group action is transitive, $\vert{}\mathcal{A}_0\vert{} = 1$ and $A_1 = I$).
    
3.  Transposition Invariance: The set $\mathcal{A}$ is closed under transposition. That is, for every $A_i \in \mathcal{A}$, there exists $i^* \in \{1, \dots, r\}$ such that: $A_i^T = A_{i^*}$
    
4.  Intersection Numbers (Closure under Multiplication): For all $i, j \in \{1, \dots, r\}$, the matrix product is a linear combination of the basis matrices:
    
    $$A_i A_j = \sum_{k=1}^r p_{ij}^k A_k$$
    
    for non-negative integers $p_{ij}^k$

Let $V(\mathcal{A}) = \operatorname{span}_{\mathbb{C}}(\mathcal{A})$ be the complex linear span of $\mathcal{A}$. Condition 4 asserts that $V(\mathcal{A})$ is closed under matrix multiplication, making it a finite-dimensional associative $\mathbb{C}$-algebra. We call $V(\mathcal{A})$ the basis algebra (or coherent algebra) of the configuration. Condition 2 guarantees that this algebra contains the multiplicative identity $I$, and condition 3 ensures it is a $*$-algebra closed under Hermitian adjoints (transposition and complex conjugation). A matrix algebra closed in this way is called semisimple (it has no non-zero nilpotent ideals).

If the coherent configuration is associated with a group, then this basis algebra is just the centraliser algebra we already encountered.

Unlike the centralizer algebra which commutes with every permutation group matrix, a general coherent algebra need not be commutative. However, they become commutative if $p_{ij}^k = p_{ji}^k$ for all $i, j, k$.

Let's look a little deeper at this basis algebra. We can apply something analogous to Schur's Lemma. The basis algebra $\mathcal{A}$ of a coherent configuration decomposes as a direct sum of complete matrix algebras over $\mathbb{C}$.:

$$\mathcal{A} \cong M_{e_1}(\mathbb{C}) \oplus M_{e_2}(\mathbb{C}) \oplus \dots \oplus M_{e_s}(\mathbb{C})$$

This is an instance of the Artin–Wedderburn Theorem for semisimple finite-dimensional algebras (which we showed holds true for this algebra due to the equality between a matrix and the complex conjugate transpose).
    
When the coherent configuration comes from a permutation group $G$ acting on $\Omega$ with permutation character $\pi$, the permutation representation decomposes into its distinct irreducible representations $\rho_i$ with multiplicities $m_i$:
    
$$\mathbb{C}^\Omega \cong \bigoplus_{i=1}^s m_i V_i$$
    
So the character is $\pi = \sum_{i=1}^s m_i \chi_i$.
    
By Schur's Lemma, the algebra of all endomorphisms that commute with $G$ (the centralizer algebra $\mathcal{A} = \text{End}_G(\mathbb{C}^\Omega)$) decomposes as:
    
$$\text{End}_G(\mathbb{C}^\Omega) \cong \bigoplus_{i=1}^s \text{End}_G(m_i V_i) \cong \bigoplus_{i=1}^s M_{m_i}(\mathbb{C})$$
    
Comparing with the coherent configuration case, each block is the complete matrix algebra $M_{m_i}(\mathbb{C})$. Thus, the degrees are the multiplicities of the irreducible constituents: $e_i = m_i$. As we already saw in the case of a group, the total dimension of the basis algebra is the rank $r$ of the configuration:

$$r = \dim \mathcal{A} = \sum_{i=1}^s e_i^2 = \sum_{i=1}^s m_i^2$$

(which is the character norm $\langle \pi, \pi \rangle$).

The algebra is commutative ($A_i A_j = A_j A_i$) if and only if every matrix block has size $e_i = 1$. If associated with a group, then this happens if and only if the permutation representation is multiplicity-free ($m_i = 1$ for all $i$).

Now let's apply the stronger condition of a symmetry. In such a case the coherent. Under symmetry $A_i^T = A_i$ for all $i$. This allows us to place further constraints on the intersection numbers. 

Let $v_k = p_{k k^*}^0$ be the valency (degree) of the relation $R_k$. For $p_{ij}^m$, if $m = 0$ that corresponds to the diagonal. Because $m = 0$, the starting and ending vertices must satisfy $(\alpha, \beta) \in R_0$. Since $R_0$ is the diagonal, $\alpha$ and $\beta$ must be the exact same vertex: $\alpha = \beta$. So $p_{k k^*}^0$ is the number of vertices $\gamma \in \Omega$ such that:

$$(\alpha, \gamma) \in R_k \quad \text{and} \quad (\gamma, \alpha) \in R_{k^*}$$

Then we have what is called the full triangle symmetry:

$$v_k p_{ij}^k = v_i p_{jk}^i = v_j p_{ki}^j$$

Shifting the roles of the three vertices of the triangle $(\alpha, \beta, \gamma)$ cyclicly or by reflections leaves the weighted count of triangles invariant.

**Aside:** Regarding the permutation character, by definition, the inner product of any two characters is:

$$\langle \pi, \pi \rangle = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \pi(g) \overline{\pi(g)} = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \vert{}\pi(g)\vert{}^2$$

Let $\chi_1, \dots, \chi_s$ be the irreducible characters, which are orthonormal under this inner product:

$$\langle \chi_i, \chi_j \rangle = \frac{1}{\vert{}G\vert{}} \sum_{g \in G} \chi_i(g) \overline{\chi_j(g)} = \delta_{ij} = \begin{cases} 1 & \text{if } i = j \\ 0 & \text{if } i \neq j \end{cases}$$

Now, write the decomposition of the permutation character into irreducible constituents:

$$\pi = \sum_{i=1}^s m_i \chi_i$$

Taking the inner product of $\pi$ with itself:

$$\langle \pi, \pi \rangle = \left\langle \sum_{i=1}^s m_i \chi_i, \, \sum_{j=1}^s m_j \chi_j \right\rangle = \sum_{i=1}^s \sum_{j=1}^s m_i m_j \langle \chi_i, \chi_j \rangle$$

$$\langle \pi, \pi \rangle = \sum_{i=1}^s m_i^2 \langle \chi_i, \chi_i \rangle = \sum_{i=1}^s m_i^2 (1) = \sum_{i=1}^s m_i^2$$

$$\frac{1}{\vert{}G\vert{}} \sum_{g \in G} \pi(g)^2 = \langle \pi, \pi \rangle = \sum_{i=1}^s m_i^2$$

---

#### The Intersection Algebra

There's a bit of a problem though. Groups often act on huge sets. But the centralizer algebra $\mathcal{A}$ is spanned by exactly $r$ linearly independent basis matrices: $\{A_1, A_2, \dots, A_r\}$. $r$ is generally a fairly manageable number. Can we switch our algebra from $n \times n$ matrices to $r \times r$ matrices?

Yes! Because these $r$ matrices form a basis, any matrix $M$ inside $\mathcal{A}$ can be uniquely written as a linear combination:

$$M = c_1 A_1 + c_2 A_2 + \dots + c_r A_r$$

Instead of writing out $M$ as a massive $n \times n$ grid of numbers, we can completely identify $M$ by extracting its $r$ coefficients in this linera combination and writing them as a simple $r$-dimensional column vector:

$$\vec{c} = \begin{pmatrix} c_1 \\ c_2 \\ \vdots \\ c_r \end{pmatrix}$$

To see how multiplication works in this compressed format, recall that the basis $\{A_1, \dots, A_r\}$ closes under matrix multiplication:

$$A_i A_j = \sum_{k=1}^r p_{ij}^k A_k$$

Now consider what happens when we take a specific basis matrix, say $A_i$, and left-multiply $M$ by it. Every finite-dimensional algebra acts on itself by left multiplication. Because $\mathcal{A}$ is closed under multiplication, the product $A_i M$ is guaranteed to still be inside $\mathcal{A}$. Therefore, the new product matrix must have its own unique set of $r$ coefficients:

$$A_i M = d_1 A_1 + d_2 A_2 + \dots + d_r A_r$$

This gives us a new $r$-dimensional coordinate vector:

$$\vec{d} = \begin{pmatrix} d_1 \\ d_2 \\ \vdots \\ d_r \end{pmatrix}$$

The operation of left-multiplying by $A_i$ maps the old coordinate vector $\vec{c}$ to the new coordinate vector $\vec{d}$. We can define this linear operator as $L_{A_i}: \mathcal{A} \to \mathcal{A}$, where $L_{A_i}(X) = A_i X$. Because matrix multiplication is distributive and associative, this mapping is a linear transformation from $\mathbb{C}^r$ to $\mathbb{C}^r$, which means it can be written as an $r \times r$ matrix.

Let's call the matrix that performs this exact coordinate transformation $P_i$. We can find its entries by looking at how $A_i$ acts on the basis vectors. Multiplying $A_i$ by the $j$-th basis vector $A_j$ gives the $j$-th column of $P_i$. Looking at our multiplication rule above, the coefficient for the $k$-th row is $p_{ij}^k$. Therefore, the entries of $P_i$ are explicitly:

$$(P_i)_{kj} = p_{ij}^k$$

_(Note: The indices are $k,j$, not $j,k$, because the sum over $k$ represents the rows of the $j$-th column)._

The linear span of $\{P_1, \dots, P_r\}$ forms an algebra of $r \times r$ matrices, called the intersection algebra $\hat{\mathcal{A}}$.

Because matrix multiplication is associative, the assignment $A_i \mapsto P_i$ strictly preserves the multiplication table:

$$P_i P_j = \sum_{k=1}^r p_{ij}^k P_k$$

This makes the map $A_i \mapsto P_i$ an algebra isomorphism. By extracting the $r$ basis coefficients, we compress the act of matrix multiplication into the $r \times r$ intersection matrices $P_i$. It transfers all eigenvalue equations and algebraic identities from the large $n \times n$ matrices down to the explicit $r \times r$ matrices, allowing us to solve the system without ever computing anything of size $n$.

For an association scheme on $n$ vertices, the algebra formed by the association matrices is called the Bose-Mesner Algebra, which is isomorphic to the intersection algebra. For an association scheme, since it is commutative, the basis matrices in both algebras form a commuting family of normal (in the symmetric case, real symmetric) matrices. They are therefore simultaneous diagonalizable via an orthonormal basis of common eigenvectors. In this common eigenbasis, every matrix in the algebra decomposes into a diagonal matrix (a direct sum of $1 \times 1$ blocks). 

The Bose-Mesner algebra has two distinguished dual bases:

1.  The geometric basis: $\{A_0, A_1, \dots, A_d\}$ under ordinary and Schur-Hadamard multiplication:
    
$$A_i A_j = \sum_{k=0}^d p_{ij}^k A_k, \qquad A_i \circ A_j = \delta_{ij} A_i$$
    
2.  The spectral basis of primitive idempotents: $\{E_0, E_1, \dots, E_d\}$:
    
$$E_i E_j = \delta_{ij} E_i, \qquad E_i \circ E_j = \frac{1}{n} \sum_{k=0}^d q_{ij}^k E_k$$
    
where $E_0 = \frac{1}{n} J$.
    
The transition matrices between these two dual bases define the first eigenmatrix $P$ and the second eigenmatrix $Q$:

$$A_j = \sum_{i=0}^d P_{ij} E_i \quad \Longleftrightarrow \quad E_j = \frac{1}{n} \sum_{i=0}^d Q_{ij} A_i$$

Here, $P_{ij}$ represents the $i$-th eigenvalue of the adjacency matrix $A_j$. Writing this linear change of basis in matrix form yields the orthogonality relation:

The relationship between the first and second eigenmatrices $P$ and $Q$ is $P Q = Q P = n I_{r}$, and $r = d+1$ where $d$ is the diameter of the graph.

#### A Little Graph Theory

First, some definitions. In an undirected graph, every edge can be traversed in both directions. "Connected" means that for every pair of vertices $u, v$, there exists a path from $u$ to $v$. Because edges are bidirectional, you can automatically retrace your steps backwards from $v$ to $u$.
    
In a directed graph (digraph), edges have arrows ($u \to v$). It is strongly connected if for every ordered pair of vertices $(u, v)$, there is a directed path from $u$ to $v$ and a directed path from $v$ to $u$.

In a general coherent configuration (or a non-symmetric association scheme), the forward edge and reverse edge do not have to belong to the same orbital. But they will belong to the same orbital in a symmetric association scheme.

The diameter of a connected graph is the maximum shortest-path distance between any two vertices in the graph.

A complete graph ($K_n$, $n \ge 2$) is one where every vertex is directly connected to every other vertex by an edge, so $d(u, v) = 1$ for all $u \neq v$. The diameter is $1$.

A cycle graph ($C_n$) is one where to reach the farthest vertex along the ring, you traverse at most half the perimeter. For even $n$: diameter is $n / 2$. For odd $n$: diameter is $(n - 1) / 2$.
        
A $d$-Dimensional hypercube ($Q_d$) is one where the two antipodal corners differ in all $d$ coordinates, requiring $d$ bit flips. The diameter is $d$.

There is a particularly important class of symmetric association schemes derived from graphs. Let $\Gamma$ be a connected graph on the vertex set $\Omega$, having diameter $d$. Let $d(x, y)$ be the shortest-path distance between the vertices $x$ and $y$ of $\Gamma$. We let $\Gamma_i(x)$ denote the set of all vertices whose distance from the vertex $x$ is $i$, for $0 \le i \le d$ (so that $\Gamma_0(x) = \{x\}$ and $\Gamma_1(x)$ is the set of neighbours of $x$).

We say that $\Gamma$ is distance-transitive if, for $0 \le i \le d$, the automorphism group $G = \operatorname{Aut}(\Gamma)$ acts transitively on the set of ordered pairs of vertices at distance $i$: $\{(x, y) \in \Omega \times \Omega \mid d(x, y) = i\}$
    
We say that $\Gamma$ is distance-regular if there exist parameters $c_i, a_i, b_i$ for $0 \le i \le d$ such that, whenever $d(x, y) = i$, the number of neighbours of $y$ that lie at distance $i - 1$, $i$, and $i + 1$ from $x$ are $c_i$, $a_i$, and $b_i$ respectively:

$$c_i = \vert{}\Gamma_1(y) \cap \Gamma_{i-1}(x)\vert{}$$
    
$$a_i = \vert{}\Gamma_1(y) \cap \Gamma_i(x)\vert{}$$
    
$$b_i = \vert{}\Gamma_1(y) \cap \Gamma_{i+1}(x)\vert{}$$
 
Note that, for a distance-regular graph, the parameters $c_0$ and $b_d$ are undefined, or set to $0$ by convention, since there are no vertices at distances $-1$ or $d + 1$.

The intersection parameters of a distance-regular graph satisfy:

1.  $1 = c_1 \le c_2 \le \dots \le c_d$
    
2.  $k = b_0 \ge b_1 \ge \dots \ge b_{d-1} \ge 1$
    

Furthermore, the intersection numbers satisfy $c_i \le b_{d-i}$ for all $i$ such that $i \le d - i$.

Every distance-transitive graph is distance-regular. If $\Gamma$ is distance-regular with diameter $d$, then the distance relations:
    
$$R_i = \{(x, y) \in \Omega \times \Omega \mid d(x, y) = i\} \quad \text{for } 0 \le i \le d$$
    
form a symmetric association scheme on the vertex set $\Omega$.

The relationship between distance-transitive and distance-regular graphs mirrors that between transitive permutation groups and coherent configurations:
    
$$\text{Distance-Transitive (Algebraic / Group-Theoretic)} \implies \text{Distance-Regular (Combinatorial)}$$
    
Distance-transitivity demands a large automorphism group $G \le \operatorname{Sym}(\Omega)$ to actively map any distance-$i$ pair to another. Distance-regularity relaxes this: the graph only needs its local triangle/path counts ($c_i, a_i, b_i$) to remain constant everywhere, even if the graph has a trivial automorphism group $\operatorname{Aut}(\Gamma) = \{1\}$.
    
Also, since every neighbour of $y$ must lie at distance $i-1$, $i$, or $i+1$ from $x$ in a metric graph, the local parameters must sum to the graph valency $k = b_0$:
    
$$c_i + a_i + b_i = k \quad \text{for all } 1 \le i \le d-1$$
    
with $c_1 = 1$ and $a_0 = 0$. In terms of the intersection numbers $p_{1j}^k$ from your earlier notes, the adjacency matrix of $\Gamma$ acts tridiagonally on the scheme basis:
    
$$A_1 A_i = b_{i-1} A_{i-1} + a_i A_i + c_{i+1} A_{i+1}$$
    
This makes the Bose-Mesner algebra of a distance-regular graph a polynomial algebra generated by the single adjacency matrix $A_1$:
    
$$A_i = v_i(A_1)$$
    
for orthogonal polynomials $v_i(x)$ of degree $i$.
    
These are also connected to Strongly Regular Graphs. A strongly regular graph can also be seen as a graph $\Gamma$ on the vertex set $\Omega$ having the property that $(\Omega, \{R_0, R_1, R_2\})$ is an association scheme, where $R_0, R_1, R_2$ are the relations of equality, adjacency, and non-adjacency respectively.

A disconnected strongly regular graph is a disjoint union of complete graphs of the same size, and conversely.

A connected strongly regular graph is a distance-regular graph of diameter $2$, and conversely:
    
$b_0 = k, \quad c_1 = 1, \quad a_1 = \lambda, \quad b_1 = k - 1 - \lambda$
        
$c_2 = \mu, \quad a_2 = k - \mu, \quad b_2 = 0$
        
The distance relations $R_0 = I$, $R_1 = A$ (adjacent), and $R_2 = J - I - A$ (non-adjacent) form the classic 2-class association scheme. More generally, a distance regular graph of diameter $d$ defines an association scheme with $d$ classes. 

### Extensions

First let's define Direct & Semi-Direct Products. For $G$ to be the internal direct product $G \cong A \times B$, three conditions must hold:

$A \trianglelefteq G$ and $B \trianglelefteq G$.
    
$A \cap B = \{1\}$
    
$AB = G$. _(Every element $g \in G$ can be written as $g = ab$ with $a \in A, b \in B$)._
    
When conditions 1 and 2 hold, elements of $A$ and elements of $B$ automatically commute with each other:

$$a b a^{-1} b^{-1} = \underbrace{(a b a^{-1})}_{\in B} b^{-1} \in B \quad \text{and} \quad a b a^{-1} b^{-1} = a \underbrace{(b a^{-1} b^{-1})}_{\in A} \in A$$

Since the commutator belongs to $A \cap B = \{1\}$, we get $aba^{-1}b^{-1} = 1 \implies ab = ba$.

For $G$ to be an internal semidirect product $G = A \rtimes B$:

$A$ must be **normal** in $G$ ($A \trianglelefteq G$).
    
$B$ is a **subgroup** of $G$ ($B \le G$), but $B$ does **not** have to be normal in $G$.
    
$A \cap B = \{1\}$ (trivial intersection).
    
$AB = G$ (full span).

Why does having $A \cap B = \{1\}$ with $A \trianglelefteq G$ allow $B$ to act on $A$? Because $A$ is normal in $G$, conjugating any element $a \in A$ by _any_ element of the entire group maps it back into $A$. Since $B$ lives inside $G$, every element $b \in B$ can act on $A$ by conjugation:

$$\phi_b(a) = b a b^{-1} \in A$$

Conjugation by $b$ is an invertible automorphism of $A$. Combining two operations respects group structure:

$$\phi_{b_1 b_2}(a) = (b_1 b_2) a (b_1 b_2)^{-1} = b_1 (b_2 a b_2^{-1}) b_1^{-1} = \phi_{b_1}(\phi_{b_2}(a))$$
    
This defines an action homomorphism: $\phi: B \longrightarrow \text{Aut}(A)$.    

The trivial intersection $A \cap B = \{1\}$ ensures this action is clean: no non-identity element in $B$ can be confused with an element in $A$. It guarantees that every element $g \in G$ factors uniquely as:

$$g = a \cdot b \quad (a \in A, \, b \in B)$$

When you multiply two factored elements $(a_1 b_1)(a_2 b_2)$, you slide $b_1$ past $a_2$ by letting $b_1$ act on $a_2$:

$$(a_1 b_1)(a_2 b_2) = a_1 (b_1 a_2 b_1^{-1}) b_1 b_2 = a_1 \phi_{b_1}(a_2) \cdot (b_1 b_2)$$

If the action $\phi$ is trivial ($\phi_b(a) = a$ for all $b$, meaning $b$ does not twist $a$), then $b$ commutes with $a$, $B$ becomes normal, and the semidirect product collapses into an ordinary direct product.

If the action $\phi$ is non-trivial (like reflections flipping rotations in $D_4$), $B$ twists $A$.

For both direct and semi-direct products, the order of $G$ is the product of the orders of $A$ and $B$.

### Extensions - 2
Now back to extensions. Sylow's Theorems tell us how to break a group apart to study it easily. But is there a way to take two groups and use them to build a larger group. If Jordan-Hölder gives us the bricks (Simple Groups), how do we build a house? Suppose you know a group $G$ has a normal subgroup $A$, and the quotient $G/A$ is $B$. The group $G$ is an Extension of $A$ by $B$. But simply knowing the bricks ($A$ and $B$) does not uniquely determine $G$.

For example, if $A = C_2$ and $B = C_2$, the resulting group $G$ could be the cyclic group $C_4$ or the Klein four-group $V_4$. To precisely rebuild $G$, you need two pieces of mortar:

1. **The Action:** How does the top layer $B$ physically twist or permute the bottom layer $A$ when you move through the group? (Represented as a homomorphism into the automorphisms of $A$).

2. **The Factor Set:** When you multiply two elements in the top layer $B$, they might not land exactly on the expected element in $B$; they might "slip" by a specific element of $A$. This slipping is tracked by a function $f(b_1, b_2)$ called a factor set.

If the factor set is trivial (zero slippage), the group is a clean Semidirect Product (like stacking blocks perfectly on top of each other). If the factor set is complex, the layers weave together tightly. 

In group theory, tracking these structural slippages between abstract layers gave birth to Homological Algebra and Cohomology groups, a way to use topology and algebraic grids to map exactly how mathematical structures twist into one another. We take the group $G$ and embed it into a ring, creating the **Group Ring** $\mathbb{Z}G$.

* You are now allowed to formally add group elements with integer coefficients, like $3g_1 - 2g_5$.
* Multiplication in this ring is called **convolution**, where you multiply out the terms using the group's internal multiplication table and gather the resulting coefficients.

By turning the group into a ring module, you can run algebraic topology on it. In topology, **Cohomology Groups** ($H^0, H^1, H^2 \dots$) measure the number of "holes" or "twists" in a multi-dimensional shape. In algebra, they measure the twists in the group extensions:

* **The Second Cohomology Group ($H^2(\mathbb{Z}B, A)$):** This is exactly the **Extension Group** $E(B, A)$ we built earlier. It is the mathematical space of all valid factor sets minus the trivial inner factor sets. If $H^2 = 0$, there are no topological "twists" possible, and every extension perfectly splits into a clean semidirect product.
* **The First Cohomology Group ($H^1(\mathbb{Z}G, A)$):** If the extension *does* split cleanly, there might be multiple different geometric ways to slice the complement group out of the whole. $H^1$ exactly counts the number of conjugate classes of these complements.

Homological algebra allows mathematicians to measure the "glue" holding groups together using the exact same machinery used to count multi-dimensional holes in a donut.

## Some Theorems of Abstract Algebra
There are the main theorems from PJ Cameron's [Introduction to Algebra](https://webspace.maths.qmul.ac.uk/p.j.cameron/algebra/)

### Chapter 1: Introduction

Theorem 1.1: There are inﬁnitely many prime numbers.

Theorem 1.2: $\sqrt{2}$ is irrational; that is, there is no number $x = p/q$ (where $p$ and $q$ are whole numbers) such that $x^2 = 2$.

Theorem 1.3: Two lines parallel to the same line are parallel to one another.

Theorem 1.5: Let $S$ be any set of natural numbers. Suppose that (a) 0 belongs to $S$; (b) for any natural number $n$, if $n$ belongs to $S$, then $n + 1$ belongs to $S$. Then $S = \mathbb{N}$, that is, $S$ is the set of all natural numbers.

Theorem 1.6 (Division algorithm for natural numbers): Let $m$ and $n$ be any natural numbers with $n > 0$. Then there exist natural numbers $q$ and $r$ such that (a) $m = nq + r$; (b) $r < n$. Moreover, $q$ and $r$ are unique; that is, if also $m = nq' + r'$, where $r' < n$, then $q = q'$ and $r = r'$.

Theorem 1.7: For any natural number $n$, we have $(\cos\theta + i\sin\theta)^n = \cos n\theta + i\sin n\theta$.

Theorem 1.8 (Principle of Induction): Let $P(n)$ be a statement about the natural number $n$. Suppose that (a) $P(0)$ is true; (b) For any natural number $n$, if $P(n)$ is true, then $P(n + 1)$ is true. Then $P(n)$ is true for every natural number $n$.

Theorem 1.9 (Principle of Strong Induction): Let $P(n)$ be a statement about the natural number $n$. Suppose that, for any natural number $n$, if $P(m)$ is true for all $m < n$, then $P(n)$ is true. Then $P(n)$ is true for every natural number $n$.

Theorem 1.11: Let $T$ be any non-empty subset of the natural numbers. Then $T$ has a smallest element.

Theorem 1.13 (Remainder Theorem): If $f(x)$ is divided by $x - c$, the remainder is $f(c)$.

Theorem 1.14 (Factor Theorem): Let $f(x)$ be a polynomial and $c$ a number. Then $x - c$ divides $f(x)$ if and only if $f(c) = 0$.

Theorem 1.19 (Equivalence Relation Theorem): (a) Let $R$ be an equivalence relation on a set $A$. Then the set of equivalence classes is a partition of $A$. (b) Conversely, let $\{A_1,A_2,\dots\}$ be a partition of $A$. Then there is an equivalence relation on $A$ whose equivalence classes are $A_1,A_2,\dots$.

Theorem 1.20 (Binomial Theorem): For any natural number $n$, $(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$.

Theorem 1.21: Let $m$ and $n$ be natural numbers. Then $\gcd(m,n) = m$ if $n = 0$, $\gcd(n,r)$ if $m = nq + r$ with $0 \le r < n$.

Theorem 1.22: For any two natural numbers $m$ and $n$, there exist integers $x$ and $y$ such that $\gcd(m,n) = xm + yn$.

Theorem 1.24: In $\mathbb{Z}_m$, the element $[x]_m$ has an inverse if and only if $\gcd(x,m) = 1$.

Theorem 1.25: Suppose that the system of equations for $i$ from $1...n$ is:

$$a_{i1}x_1 + a_{i2}x_2 + \dots + a_{in}x_n = b_i$$

Let $A$ be the matrix of coefficients, and let $b$ be the $n \times 1$ matrix (the column vector) with entries $b_1, b_2, \dots, b_n$. Let $B_i$ be the matrix obtained from $A$ by replacing the $i$-th column by the column vector $b$.

Then, provided that $\det(A) \neq 0$, the system has a unique solution given by Cramer's Rule:

$$x_i = \frac{\det(B_i)}{\det(A)}$$

for $i = 1, 2, \dots, n$.

If $\det(A) = 0$, then either the equations have no solution, or they have more than one solution.

### Chapter 2: Rings

Theorem 2.2 (First Subring Test): A non-empty subset $S$ of a ring $R$ is a subring provided that, for all $a,b \in S$, we have $a + b,ab,-a \in S$.

Theorem 2.3 (Second Subring Test): A non-empty subset $S$ of a ring $R$ is a subring provided that, for all $a,b \in S$, we have $a - b,ab \in S$.

Theorem 2.5 (Ideal Test): A non-empty subset $S$ of a ring $R$ is an ideal of $R$ if and only if (a) for all $s_1,s_2 \in S$, we have $s_1 - s_2 \in S$; (b) for all $s \in S$ and $r \in R$, we have $rs,sr \in S$.

Theorem 2.8: The factor ring is indeed a ring. Let $I$ be an ideal in the ring $R$. The factor ring or quotient ring $R/I$ is the set of cosets of $I$ in $R$, with operations of addition and multiplication defined by: $(I + x)+(I + y) = I + (x + y)$, $(I + x)(I + y) = I + xy$.

Theorem 2.9: The canonical homomorphism $\theta : R \to R/I$ deﬁned by $x\theta = I + x$ for $x \in R$ is indeed a homomorphism; its image is $R/I$ and its kernel is $I$.

Theorem 2.10 (First Isomorphism Theorem): Let $\theta : R \to S$ be a ring homomorphism. Then (a) $\text{Im}(\theta)$ is a subring of $S$; (b) $\text{Ker}(\theta)$ is an ideal of $R$; (c) $R/\text{Ker}(\theta) \cong \text{Im}(\theta)$.

Theorem 2.11 (Second Isomorphism Theorem): Let $I$ be an ideal of $R$. There is a one-to-one correspondence between the set of subrings of $R$ which contain $I$ and the set of subrings of $R/I$. Under this correspondence, ideals of $R$ containing $I$ correspond to ideals of $R/I$.

Theorem 2.12 (Third Isomorphism Theorem): Let $I$ be an ideal of $R$ and $S$ a subring of $R$. Then (a) $I + S = \{a + s : a \in I,s \in S\}$ is a subring of $R$ containing $I$; (b) $I \cap S$ is an ideal of $S$; (c) $S/(I \cap S) \cong (I + S)/I$.

Theorem 2.13: For any ring $R$, $R[x]$ is a ring. It is commutative if and only if $R$ is commutative; it has an identity if and only if $R$ has an identity; but it is never a division ring.

Theorem 2.16 (Gauss’ Lemma): If $R$ is a UFD, then $R[x]$ is a UFD.

Theorem 2.17: (a) In an integral domain, if $a$ divides $b$ and $b$ divides $a$, then $a$ and $b$ are associates. (b) In an integral domain, if $a$ and $b$ have a greatest common divisor, then any two g.c.ds are associates. (c) In a unique factorisation domain, every two elements have a greatest common divisor.

Theorem 2.21: Every principal ideal domain is a unique factorisation domain.

Theorem 2.24: (a) A Euclidean domain is a principal ideal domain. (b) A Euclidean domain is a unique factorisation domain.

Theorem 2.25: Any integral domain has a ﬁeld of fractions.

Theorem 2.27: Let $R$ be a commutative ring with identity, and $I$ an ideal of $R$. Then $R/I$ is a ﬁeld if and only if $I$ is a maximal ideal of $R$.

Theorem 2.29: Let $F$ be a ﬁeld, and $f$ a polynomial which is irreducible in $F[x]$. Then there is a ﬁeld $K$ containing $F$ and an element $\alpha$ satisfying $f(\alpha) = 0$.

Theorem 2.30: For any prime number $p$ and any positive integer $n$, there is an irreducible polynomial of degree $n$ over $\mathbb{Z}_p$, and hence a ﬁnite ﬁeld of order $p^n$.

Theorem 2.31: Let $R$ be a commutative ring with identity, and $n$ a positive integer. (a) If $S$ is an ideal of $R$, then $M_n(S)$ is an ideal of $M_n(R)$. (b) Every ideal of $M_n(R)$ is of this form.

### Chapter 3: Groups

Theorem 3.1 (First Subgroup Test): Let $H$ be a non-empty subset of the group $G$. Then $H$ is a subgroup of $G$ if and only if (a) for all $h_1,h_2 \in H$, we have $h_1h_2 \in H$; (b) for all $h \in H$ we have $h^{-1} \in H$.

Theorem 3.2 (Second Subgroup Test): Let $H$ be a non-empty subset of a group $G$. Then $H$ is a subgroup if and only if, for all $h_1,h_2 \in H$, we have $h_1h_2^{-1} \in H$.

Theorem 3.4: Let $H$ be a subgroup of the group $G$. Then there is a bijection between the left cosets and the right cosets of $H$ in $G$; so there are equally many of each.

Theorem 3.5 (Lagrange’s Theorem): Let $H$ be a subgroup of the ﬁnite group $G$. Then $\vert{}G\vert{} = \vert{}H\vert{} \cdot \vert{}G : H\vert{}$. In particular, the order of $H$ divides that of $G$.

Theorem 3.6: (a) Let $g$ be an element of the group $G$. Then the set $\{g^m : m \in \mathbb{Z}\}$ is a subgroup of $G$; its order is equal to the order of $g$. (b) The order of any element of a ﬁnite group $G$ divides the order of $G$. (c) If $g$ has ﬁnite order $n$, then $g^m = 1$ if and only if $n$ divides $m$.

Theorem 3.8: Let $G = \langle g \rangle$ be a cyclic group of order $n$. Then, for each divisor $m$ of $n$, there is a unique subgroup of $G$ of order $m$, which is a cyclic group generated by $g^{n/m}$; and these are all the subgroups of $G$.

Theorem 3.9 (Cauchy’s Theorem): Let $G$ be a ﬁnite group, and $p$ a prime number which divides the order of $G$. Then $G$ contains an element of order $p$.

Theorem 3.10: Two cyclic groups of the same order are isomorphic.

Theorem 3.12: Let $H$ be a subgroup of a group $G$. Then the following are equivalent: (a) for all $g \in G, x \in H$, we have $g^{-1}xg \in H$; (b) for all $g \in G$, we have $g^{-1}Hg = H$; (c) for all $g \in G$, we have $Hg = gH$.

Theorem 3.14: The factor group, as deﬁned above, is indeed a group.

Theorem 3.15: The canonical homomorphism $\theta : G \to G/N$ deﬁned by $g\theta = Ng$ for $g \in G$ is indeed a homomorphism; its image is $G/N$ and its kernel is $N$.

Theorem 3.16 (First Isomorphism Theorem): Let $\theta : G \to H$ be a group homomorphism. Then: (a) $\text{Im}(\theta)$ is a subgroup of $H$; (b) $\text{Ker}(\theta)$ is a normal subgroup of $G$; (c) $G/\text{Ker}(\theta) \cong \text{Im}(\theta)$.

Theorem 3.17 (Second Isomorphism Theorem): Let $N$ be a normal subgroup of $G$. There is a one-to-one correspondence between the set of subgroups of $G$ which contain $N$ and the set of subgroups of $G/N$. Under this correspondence, normal subgroups of $G$ containing $N$ correspond to normal subgroups of $G/N$.

Theorem 3.18 (Third Isomorphism Theorem): Let $N$ be a normal subgroup of $G$ and $H$ a subgroup of $G$. Then: (a) $NH = \{nh : n \in N,h \in H\}$ is a subgroup of $G$ containing $N$; (b) $N \cap H$ is a normal subgroup of $H$; (c) $H/(N \cap H) \cong (NH)/N$.

Theorem 3.21: (a) For any element $x \in G$, $C_G(x)$ is a subgroup of $G$. (b) There is a bijection between the conjugacy class of an element $x$ of $G$ and the set of cosets of $C_G(x)$ in $G$. (c) (the class equation) $\vert{}G\vert{} = \sum \vert{}G : C_G(x_i)\vert{}$, where the elements $x_i$ are representatives of the conjugacy classes.

Theorem 3.23: Let $G$ have order $p^n$, where $p$ is prime and $n > 0$. Then $Z(G) \ne \{1\}$.

Theorem 3.24 (Cayley’s Theorem): Every group is isomorphic to a permutation group (a subgroup of the symmetric group).

Theorem 3.28: Two elements of $S_n$ are conjugate if and only if they have the same cycle structure.

Theorem 3.29: The map $\theta$ that takes a permutation $\pi$ to its parity is a homomorphism from $S_n$ to the group $\mathbb{Z}_2$ of integers mod 2. Its kernel, the set of all permutations of even parity, is a normal subgroup of $S_n$ having index 2.

Theorem 3.31: The symmetry group of a regular $n$-gon is the dihedral group of order $2n$. It has a cyclic normal subgroup of order $n$ consisting of rotations; every element outside this subgroup has order 2.

Theorem 3.32: The properties of the ﬁve Platonic polyhedra are given in the following table:

Theorem 3.33: The number of non-isomorphic groups of order $n$ does not exceed $n^{n \log_2 n}$.

### Chapter 4: Vector spaces

Theorem 4.1 (First subspace test): A non-empty subset $W$ of a vector space $V$ is a subspace of $V$ if and only if it is closed under addition and scalar multiplication; that is, $w_1,w_2 \in W$ implies $w_1 + w_2 \in W$, and $c \in F, w \in W$ implies $cw \in W$.

Theorem 4.2 (Second subspace test): The non-empty subset $W$ of the vector space $V$ over $F$ is a subspace if and only if, for any $c_1,c_2 \in F$ and $w_1,w_2 \in W$, we have $c_1w_1 + c_2w_2 \in W$.

Theorem 4.5: The following conditions for a ﬁnite subset $X$ of a vector space are equivalent: (a) $X$ is a maximal linearly independent set; (b) $X$ is a minimal spanning set; (c) $X$ is a linearly independent spanning set.

Theorem 4.6: (a) If $X$ is a basis for $V$, then every element of $V$ has a unique expression as a linear combination of $X$. (b) If $V$ has a basis containing $n$ elements, then $V$ is isomorphic to $F^n$.

Theorem 4.8 (Properties of linear independence): (a) If $X \in I$ and $Y \subset X$, then $Y \in I$. (b) (Steinitz exchange axiom) Suppose that $X,Y \in I$ with $\vert{}Y\vert{} > \vert{}X\vert{}$. Then there exists $y \in Y \setminus X$ such that $X \cup \{y\} \in I$.

Theorem 4.9: If $V$ has a basis, then any two bases have the same number of elements.

Theorem 4.10: Two ﬁnite-dimensional vector spaces over the same ﬁeld $F$ are isomorphic if and only if they have the same dimension.

Theorem 4.11: If $U$ and $W$ are subspaces of $V$, then $\dim(U \cap W) + \dim(U + W) = \dim(U) + \dim(W)$.

Theorem 4.12: (a) $\text{Im}(\theta)$ is a subspace of $W$; (b) $\text{Ker}(\theta)$ is a subspace of $V$; (c) Two vectors $v_1,v_2 \in V$ satisfy $v_1\theta = v_2\theta$ if and only if they lie in the same coset of $\text{Ker}(\theta)$.

Theorem 4.14 (First Isomorphism Theorem): Let $\theta : V \to W$ be a linear transformation. Then (a) $\text{Im}(\theta)$ is a subspace of $W$; (b) $\text{Ker}(\theta)$ is a subspace of $V$; (c) $V/\text{Ker}(\theta) \cong \text{Im}(\theta)$.

Theorem 4.18: Let $S : U \to V$ be a linear transformation. Choose two bases for $U$ and $V$; let the transition matrix between the ﬁrst and second bases in $U$ be $P$, and the transition matrix between the ﬁrst and second bases in $V$ be $Q$. Suppose that the matrix representing $S$ relative to the ﬁrst bases in $U$ and $V$ is $A$, and the matrix representing $S$ relative to the second bases is $A'$. Then $A' = PAQ^{-1}$.

Theorem 4.19: Let $S : U \to V$ be a linear transformation. Then there is a natural number $r$ and a choice of bases in $U$ and $V$ such that the matrix of $S$ relative to these bases is...

Theorem 4.20: Any matrix can be transformed into reduced echelon form by a sequence of elementary row operations.

Theorem 4.22: (a) Any invertible matrix is a product of elementary matrices. (b) For any matrix $A$, there is an invertible matrix $P$ such that $PA$ is in reduced echelon form.

Theorem 4.23: There is a unique determinant on $M_n(F)$, for any positive integer $n$ and ﬁeld $F$.

Theorem 4.25: (a) For any $A,B \in M_n(F)$, we have $\det(AB) = \det(A) \det(B)$. (b) $\det(A) \ne 0$ if and only if $A$ is invertible.

Theorem 4.26: $\det(A) = \det(A^T)$, where $A^T$ is the transpose of the matrix $A$.

Theorem 4.29: Let $A$ be an $m \times n$ matrix over a Euclidean domain $R$. Then $A$ can be transformed, by means of elementary row and column operations, to a matrix of the form...

### Chapter 5: Modules

Theorem 5.1 (Submodule Test): The non-empty subset $N$ of $M$ is a submodule if and only if it is closed under subtraction and scalar multiplication.

Theorem 5.2: Let $\theta : M \to N$ be an $R$-module homomorphism. Then the image and kernel of $\theta$ are submodules of $N$ and $M$ respectively; and $M/\text{Ker}(\theta) \cong \text{Im}(\theta)$ (as $R$-modules).

Theorem 5.3: Let $M$ be a unital module over a commutative ring $R$ with identity.

Theorem 5.4: Let $M$ be a $R$-module, where $R$ is a commutative ring with identity.

Theorem 5.6: Let $M$ be an $R$-module, where $R$ is a commutative ring with identity. Suppose that $M$ contains submodules $M_1,M_2,\dots,M_n$ such that any element of $M$ can be uniquely written as $m_1 +m_2 +\dots +m_n$, with $m_i \in M_i$ for $i = 1,\dots,n$. Then $M$ is isomorphic to the direct sum of $M_1,\dots,M_n$.

Theorem 5.7: A ﬁnitely generated module over a Euclidean domain is isomorphic to a direct sum of cyclic modules.

Theorem 5.8: Let $R$ be a Euclidean domain, $M$ a free module of rank $n$, and $N$ a submodule of $M$. Then there exist elements $m_1,\dots,m_n \in M$, a natural number $r \le n$, and elements $d_1,\dots,d_r \in R$ such that ...

Theorem 5.9: Let $M$ be a ﬁnitely generated module over a Euclidean domain. Then there exist elements $d_1,\dots,d_n \in R$ such that ...

Theorem 5.11 (Primary decomposition): Let $M$ be a module over a principal ideal domain $R$. Let $\text{Ann}(M) = \langle r \rangle$, and suppose that $r = p_1^{n_1} p_2^{n_2} \cdots p_k^{n_k}$, ...

Theorem 5.13: Suppose that $M$ is expressed in two diﬀerent ways as a direct sum of cyclic submodules whose annihilators are powers of irreducibles. Then the annihilators are the same, up to associates.

Theorem 5.14: Let $A$ be a ﬁnitely generated abelian group. Then ...

Theorem 5.15: Suppose that ...

Theorem 5.18 (Normal forms of matrices): Let $\theta : V \to V$ be a linear transformation, and regard $V$ as an $F[x]$-module in the usual way.

Theorem 5.19: Let $A$ be a $n \times n$ matrix over $F$.

Theorem 5.20 (Jordan form): Let $A$ be a $n \times n$ matrix over an algebraically closed ﬁeld $F$. Then there is an invertible $n \times n$ matrix $Q$ over $F$ such that $QAQ^{-1}$ is a block diagonal matrix with Jordan blocks on the diagonal and zeros elsewhere.

Theorem 5.21 (The Cayley–Hamilton Theorem): Let $c(x)$ and $m(x)$ be the characteristic and minimal polynomials of the matrix $A$. Then: ...

Theorem 5.23: Let $A \in M_n(F)$. The following conditions for the scalar $\lambda$ are equivalent: ...

Theorem 5.24 (Perron–Frobenius Theorem): Let $A$ be a $n \times n$ real matrix with all its entries non-negative, and suppose that $A$ is indecomposable. Then, up to scalar multiplication, there is a unique eigenvector $v$ for $A$ with the property that $x_i > 0$ for all $i$. The corresponding eigenvalue is the largest eigenvalue of $A$.

### Chapter 6: The number systems

Theorem 6.1: Let $P(n)$ be a proposition about the natural number $n$. Suppose that ...

Theorem 6.2: Let $P(m,n)$ be a proposition about pairs of natural numbers. Assume that: ...

Theorem 6.4: The set $\mathbb{Z}$, with the above-deﬁned operations, is a commutative ring with identity, and is an integral domain.

Theorem 6.5: $\mathbb{Q}$, with the above operations, is a ﬁeld.

Theorem 6.6: $\mathcal{C}$ is a commutative ring with identity, and $\mathcal{N}$ is a maximal ideal in $\mathcal{C}$.

Theorem 6.7: $\mathbb{R}$ is a ﬁeld.

Theorem 6.8 (Fundamental Theorem of Algebra): Any non-constant polynomial in $\mathbb{C}[x]$ has a root in $\mathbb{C}$.

Theorem 6.10: Suppose that $E,F,G$ are ﬁelds with $E \subseteq F \subseteq G$. Then $[G : E]$ is ﬁnite if and only if both $[G : F]$ and $[F : E]$ are ﬁnite. If this holds, then $[G : E] = [G : F] \cdot [F : E]$.

Theorem 6.11: Let $E$ and $F$ be ﬁelds with $E \subseteq F$. Then the set of all elements of $F$ which are algebraic over $E$ is a ﬁeld containing $E$.

Theorem 6.12: $A$ is an algebraically closed ﬁeld.

Theorem 6.15: Let $\alpha$ be an algebraic number whose minimal polynomial has degree $n$. Then there is a constant $c > 0$ such that there are only ﬁnitely many rational numbers $p/q$ satisfying $\vert{}\alpha - p/q\vert{} < 1/cq^n$.

Theorem 6.16: (a) The set $A$ is countable. (b) The sets $\mathbb{R}$ and $\mathbb{C}$ are not countable.

Theorem 6.17: If $T$ is constructible from $S$, then the coordinates of the points in $T$ lie in a ﬁeld $F$ containing $\mathbb{Q}(S)$ such that $[F : \mathbb{Q}(S)]$ is a power of 2.

Theorem 6.18 (Schr¨oder–Bernstein Theorem): If there are injective maps from $A$ to $B$ and from $B$ to $A$, then there is a bijection between $A$ and $B$.

Theorem 6.19: $\vert{}A\vert{} < \vert{}P(A)\vert{}$.

Theorem 6.20: (a) The union and Cartesian product of countable sets are countable.

Theorem 6.21: The following statements are equivalent: ...

Theorem 6.22 (Krull’s Theorem): Assume AC. Then every ring with identity has a maximal ideal.

### Chapter 7: Further topics

Theorem 7.2 (Orbit–Stabiliser Theorem): Given an action of $G$ on $\Omega$, and $x \in \Omega$: ...

Theorem 7.3 (Orbit–Counting Lemma): The number of orbits of $G$ on $\Omega$ is given by the formula ...

Theorem 7.5 (Sylow’s Theorem): Let $G$ be a group of order $n = p^a m$, where $p$ is prime and $p$ does not divide $m$.

Theorem 7.6 (Cauchy’s Theorem): If a prime number $p$ divides the order of a group $G$, then $G$ contains an element of order $p$.

Theorem 7.7: Let $G$ be a group of order $p^a m$, where $p$ is a prime not dividing $m$. Then, for $0 \le i \le a$, ...

Theorem 7.9: (a) The centre of a non-trivial $p$-group is non-trivial.

Theorem 7.10 (Jordan–H¨older Theorem): Let ...

Theorem 7.12: The following conditions for the ﬁnite group $G$ are equivalent: ...

Theorem 7.14: The alternating group $A_n$ is simple for all $n \ge 5$.

Theorem 7.16: The function $f : B \times B \to A$ is a factor set if and only if it satisﬁes ...

Theorem 7.17 (Schur’s Theorem): Suppose that the abelian group $A$ and the group $B$ have coprime orders. Then any extension of $A$ by $B$ splits.

Theorem 7.19: The following conditions on a ring $R$ are equivalent: ...

Theorem 7.21 (Hilbert Basis Theorem): Let $R$ be a commutative Noetherian ring with identity. Then $R[x]$ is Noetherian.

Theorem 7.22 (Hopkins’ Theorem): If a commutative ring with identity is Artinian, then it is Noetherian, and has the property that there is a ﬁnite upper bound on the length of any chain of ideals.

Theorem 7.25: $\sqrt{2}$ is irrational.

Theorem 7.27 (Eisenstein’s criterion): Let $R$ be a principal ideal domain, and $p$ an irreducible in $R$.

Theorem 7.28 (Nullstellensatz): Let $F$ be an algebraically closed ﬁeld.

Theorem 7.30 (Bezout’s Theorem): Let $A(f)$ and $A(g)$ be plane curves over a ﬁeld $F$ such that $A(f)$ is irreducible and not contained in $A(g)$. Then $A(f)$ and $A(g)$ intersect in only ﬁnitely many points.

Theorem 7.34: For any ﬁeld $F$, there is a unique $F$-linear map $D : F[x] \to F[x]$ satisfying the following two conditions: ...

Theorem 7.35: A polynomial $f(x) \in F[x]$ has repeated roots (possibly in an extension ﬁeld of $F$) if and only if the greatest common divisor of $f$ and $Df$ is not 1.

Theorem 7.37: Let $f$ be an irreducible polynomial over the ﬁeld $F$, and suppose that $f$ has repeated roots in an extension of $F$. Then $F$ has non-zero characteristic $p$ (a prime), and there is a polynomial $g \in F[x]$ such that $f(x) = g(x^p)$.

Theorem 7.39: Let $F$ be a perfect ﬁeld. Then an irreducible polynomial over $F$ has no repeated roots in any extension ﬁeld of $F$.

Theorem 7.41: Let $f$ be a non-constant polynomial over $F$. Then $f$ has a splitting ﬁeld over $F$; and any two such splitting ﬁelds are $F$-isomorphic.

Theorem 7.43 (Galois’ Theorem on ﬁnite ﬁelds): The order of a ﬁnite ﬁeld is a prime power. Conversely, there is a unique ﬁnite ﬁeld of any given prime power order (up to isomorphism).

Theorem 7.44: Let $p$ and $q$ be primes, $m$ and $n$ positive integers.

Theorem 7.47 (Wedderburn’s Theorem): A ﬁnite division ring is a ﬁeld (that is, it is commutative).

Theorem 7.49 (First Isomorphism Theorem): Let $\theta : A \to B$ be a homomorphism. Then: ...

Theorem 7.50: A class of algebras (with a ﬁxed set of operators) is a variety if and only if it is closed under isomorphism and under taking subalgebras, factor algebras, and Cartesian products.

Theorem 7.51: Let $(X,\le)$ be a partially ordered set. Suppose that ...

Theorem 7.52: Any ﬁnite distributive lattice is isomorphic to a sublattice of the subset lattice of a ﬁnite set.

Theorem 7.54: A ﬁnite Boolean lattice is isomorphic to the lattice of subsets of a set.

Theorem 7.55: (a) For any ring $R$, the submodule lattice of an $R$-module is modular. (b) The congruence lattice of a group is modular.

Theorem 7.56: Let $L$ be an atomic modular lattice. Then $L$ is isomorphic to the direct product of a ﬁnite number of lattices of the following form: ...

### Chapter 8: Applications

Theorem 8.2: The code $C$ is $e$-error-correcting if and only if its minimum distance is $2e + 1$ or greater.

Theorem 8.3: Let $C$ be a code of length $n$ over an alphabet of $q$ symbols, having minimum distance $d$.

Theorem 8.8: (a) Let $G$ and $H$ be matrices of size $k \times n$ and $(n - k) \times n$ respectively over a ﬁnite ﬁeld $F$, both having linearly independent rows. Then $G$ and $H$ are the generator and check matrices for the same code if and only if $GH^T = 0$.

Theorem 8.12: Suppose that $g(x)$ is the generator polynomial of the cyclic code $C$.

Theorem 8.14: The BCH code of length $n$ and designed distance $\delta$ over $\text{GF}(q)$ has minimum distance at least $\delta$, and has dimension at least $n - e(\delta - 1)$.

Theorem 8.18: Let $K$ be a ﬁnite extension of $F$. Then $K/F$ is a normal extension if and only if $K$ is the splitting ﬁeld of a polynomial in $F[x]$.

Theorem 8.19: A ﬁnite normal extension $K/F$ is separable if and only if $K$ is the splitting ﬁeld of a separable polynomial over $K$.

Theorem 8.22: Let $K$ be an extension of $F$. Then the set of elements of $K$ which are separable over $F$ is a subﬁeld of $K$ containing $F$.

Theorem 8.23: Let $K/F$ be a Galois extension with Galois group $G$. Then $\vert{}G\vert{} = [K : F]$.

Theorem 8.24 (Fundamental Theorem of Galois Theory): Let $K/F$ be a Galois extension with Galois group $G$. Then the maps ...

Theorem 8.26: Let $f$ be a polynomial over a ﬁeld $F$ of characteristic zero, with Galois group $G$. Suppose that $F$ contains a primitive $\vert{}G\vert{}$-th root of unity. Then $f$ is soluble by radicals over $F$ if and only if $G$ is a soluble group.

Theorem 8.30 (Newton’s Theorem): Let $f$ be a polynomial of degree $n$. Then any symmetric function of the roots of $f$ can be expressed as a polynomial in the coeﬃcients of $f$.

Theorem 8.31: Let $S$ be a set of points in the Euclidean plane, containing $(0,0)$ and $(1,0)$. A point $p$ can be constructed from $S$ with ruler and compass if and only if its coordinates lie in a normal extension of $\mathbb{Q}(S)$ with degree a power of 2.

Theorem 8.33: Let $S$ be a set of points in the Euclidean plane, containing $(0,0)$ and $(1,0)$. A point $p$ can be constructed from $S$ with ruler and compass if and only if $c(p)$ lies in a normal extension of $\mathbb{Q}(c(S))$ with degree a power of 2.

Theorem 8.34: A regular $n$-gon is constructible with ruler and compass if and only if $n$ is the product of a power of 2 and a number of distinct Fermat primes.

Theorem 8.35 (The Theorem of the Primitive Element): Let $K/F$ be a ﬁnite extension. Then the following are equivalent: (a) $K = F(a)$ for some $a \in K$; (b) there are only ﬁnitely many ﬁelds $L$ intermediate between $F$ and $K$ (that is, satisfying $F \subseteq L \subseteq K$).
