# 2. Quantum Physics

## States and Measurement

A state (pure states for the moment) represents the current status of some property of an object, e.g. spin. For mathematical manipulation, states are represented by ket and bra vectors (single-column and single-row matrices over a complex vector space).

To determine what state an object is in (e.g., the value of the spin), you measure an observable. Observables are represented by an operator. If the observable can only take a finite number of possible values (for instance, spin-1/2 is either $+1$ or $-1$), it is represented in this finite-dimensional state space by a square matrix.

The dimensions of the column, row, and square matrices depend on the dimension of that particular state space. For example, a spin-1/2 system is a two-dimensional state space, because the measurement can yield either $+1$ or $-1$ (ignoring the scaling factor of $\hbar/2$). In this case, the state kets and bras are $2 \times 1$ and $1 \times 2$ matrices respectively, while the operators are $2 \times 2$ matrices. 

State spaces can also be infinite-dimensional, such as position, because a particle can occupy an infinite number of possible positions. In continuous bases like position, instead of discrete matrices, we work with wave functions, which are essentially functions of a continuous variable such as position $x$.

A measurement of a state will yield different values (such as the $+1$ and $-1$) with different probabilities. These probabilities vary depending on how a measurement is carried out. For example, measuring spin always results in either a $+1$ or $-1$. But when measured along the $x$-axis, the probabilities of these two measurements may be different from what we would have obtained if we had made the measurement along the $z$-axis.

Additionally, a measurement alters the state of the system. A measurement of spin along the $x$-axis that yields $+1$ will result in the spin state collapsing to align strictly with the positive $x$-axis. This non-unitary evolution (i.e. it is not a result of continuous evolution of the state over time) is known as the collapse of the wave function.

In an ideal situation, the possible measurement values, the probabilities with which those values appear, and the post-measurement states are determined by the operator's eigenvalues, the state's superposition in the operator's eigenbasis, and the corresponding eigenvectors. However, in the real world, we often cannot get perfect accuracy in measurement, or may be faced with a situation where we cannot make a definitive measurement, and so are willing to settle for some weaker definition of measurement. 

For eg. since $+1$ (spin up along z) and $+$ (spin up along x) are not orthonormal, we cannot measure or distinguish between the two. Let us say we were in a situation where are intial state is known to be one of these two. We cannot measure and determine which state it is with 100% confidence. But we may be happy if we could just make out that the state is not $1$ with some high confidence. This is where generalized measurement operations are useful.

### Generalized Measurement Operators

The process of measurement can be mathematically represented via a set of operators acting on an $n$-dimensional Hilbert space. If a measurement has $k$ possible outcomes, we define a set of measurement operators $\{M_m\}$, where $m$ indexes the possible results.

The probability $p(m)$ that the result $m$ occurs is given by the expectation value of the operator $M_m^\dagger M_m$ acting on the initially prepared state $\vert{}\psi\rangle$:

$$p(m) = \langle\psi\vert{}M_m^\dagger M_m\vert{}\psi\rangle$$

If the measurement yields the outcome $m$, the initial state collapses to a new, normalized post-measurement state:

$$\vert{}\psi'\rangle = \frac{M_m\vert{}\psi\rangle}{\sqrt{\langle\psi\vert{}M_m^\dagger M_m\vert{}\psi\rangle}}$$

The denominator is needed to ensure the resulting state vector maintains a unit norm.

Since every measurement must always yield some outcome or the other, the sum of the probabilities of all outcomes must equal $1$:

$$\sum_m \langle\psi\vert{}M_m^\dagger M_m\vert{}\psi\rangle = 1$$

By linearity, we can bring the summation inside the inner product:

$$\langle\psi\vert{}\left(\sum_m M_m^\dagger M_m\right)\vert{}\psi\rangle = 1$$

Since $\vert{}\psi\rangle$ is an arbitrary normalized state vector ($\langle\psi\vert{}\psi\rangle = 1$), this equation holds true if and only if the operators satisfy the completeness relation:

$$\sum_m M_m^\dagger M_m = I$$

Measurements cascade sequentially. If we perform a measurement corresponding to operator $M$ followed immediately by a measurement corresponding to operator $L$, the successive state updates are $L(M\vert{}\psi\rangle)$. The combined, effective measurement operator is therefore $LM$.

### Positive Operator-Valued Measures (POVM)

If we define a new operator $E_m = M_m^\dagger M_m$, then $E_m$ is, by definition, a positive semi-definite Hermitian operator. The set of operators $\{E_m\}$ constitutes a Positive Operator-Valued Measure (POVM).  

The probability of obtaining the measurement outcome $m$ can be written in terms of the POVM element ($E_m$) as:

$$p(m) = \langle\psi\vert{}E_m\vert{}\psi\rangle$$

However, the POVM element $E_m$ alone is insufficient to determine the post-measurement state. The resulting state still strictly depends on the specific measurement operator $M_m$:

$$\vert{}\psi'\rangle = \frac{M_m\vert{}\psi\rangle}{\sqrt{\langle\psi\vert{}E_m\vert{}\psi\rangle}}$$

There is a catch though. If $M_m$ forms a set $E_m$, then $U_m M_m$ can also form the same set $E_m$ for any unitary operator $U_m$. Therefore, given $M_m$ we can determine $E_m$, but given $E_m$, we cannot determine $M_m$ uniquely. Thus, POVM operators are useful primarily to calculate probabilities, and not the states resulting from a measurement operation.

Projection operators bypass this ambiguity because they describe a fundamentally more restrictive physical process: the ideal von Neumann measurement. If we choose projection operators as our POVM elements $E_m$, they are idempotent (provided the vectors forming the projectors are orthonormal), yielding projective (or von Neumann) measurements. 

Because they are projectors, they naturally satisfy orthogonality for distinct outcomes ($E_m E_n = 0$ for $m \neq n$). These are useful for idealized situations where we work directly with the eigenvalues and eigenstates of an observable.

The idempotency condition ($E_m^2 = E_m$) guarantees that we can take the square root of $E_m$ and use it to determine the state after measurement. Idempotency also means that if a projective measurement is made, immediately repeating the exact same measurement will yield the exact same result with a probability of $1$. We cannot guarantee this for a general measurement. 

**Note:** For operators in general (and not just measurement operators), we cannot assume that $AB \psi = BA \psi$, as operators may not commute with each other.

### Eigenvectors & Eigenvalues
Projective Measurements are a special case of Generalized Measurements. 
Consider the measurement of spin along the $z$-axis. To mathematically determine the possible measurement values and their probabilities, the operator matrix for the observable must be defined.

Measurements of physical observables must yield real numbers. Therefore, observables are represented by Hermitian matrices. A Hermitian matrix is equal to its own conjugate transpose ($H = H^\dagger$) and is guaranteed to have purely real eigenvalues.

#### Constructing the Pauli Matrices for Spin-1/2
For a two-dimensional spin-1/2 system, the operator matrix must be $2 \times 2$. A generic $2 \times 2$ Hermitian matrix, where $a, b, c, d$ are real numbers, takes the form:

$$\begin{pmatrix} c & a - ib \\ a + ib & d \end{pmatrix}$$

This matrix can be decomposed as a linear combination of four basis matrices. 

While one could choose a simple canonical basis of 4 matrices such as:

$$\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \dots$$

it is mathematically more convenient to construct a basis composed entirely of Hermitian matrices with specific trace properties -- in the case of spin-1/2, a trace that sums to 0. The reason for this is explained a little later.

One immediate basis candidate is the $2 \times 2$ Identity matrix. Next, looking at the off-diagonal elements $a - ib$ and $a + ib$, we can construct two separate matrices. The first isolates the real part $a$, placing $1$ in the top-right and bottom-left elements. The second isolates the imaginary part $b$, placing $-i$ in the top-right and $i$ in the bottom-left. What remains are the diagonal elements $c$ and $d$. Because the Identity matrix already has $1$ in both diagonal positions, we need an orthogonal matrix to break the symmetry between $c$ and $d$. We define a matrix with $+1$ in the top-left and $-1$ in the bottom-right.

Our generic Hermitian matrix can then be explicitly written as a linear combination of these four basis matrices:

$$\begin{pmatrix} c & a - ib \\ a + ib & d \end{pmatrix} = \left( \frac{c+d}{2} \right) \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + a \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} + b \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} + \left( \frac{c-d}{2} \right) \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$


The three non-identity matrices are the Pauli matrices, representing the $\sigma_x$, $\sigma_y$, and $\sigma_z$ spin operators. While an infinite set of basis matrices exists for the 2x2 Hermitian matrix space, the ones derived here are conventionally chosen because they are mutually orthogonal under the trace inner product and also have a trace of zero. A trace of zero implies that the sum of their eigenvalues (the sum of the possible measurement outcomes) is exactly zero. This suits us when measuring spin-1/2 states, where the possible values are $+1$ and $-1$.

The above matrices are written in the "$z$-basis", i.e., the basis where the spin-up or $+1$ state when measured along the $z$-axis is written as the column vector 

\begin{pmatrix} 1 \\ 0 \end{pmatrix},

while a spin-down or $-1$ state is written as: 

\begin{pmatrix} 0 \\ 1 \end{pmatrix}.

The states along the $x$ and $y$ axes become:

$$\vert{}+x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ 1 \end{pmatrix}, \quad \vert{}-x\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$$


$$\vert{}+y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix}, \quad \vert{}-y\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ -i \end{pmatrix}$$

Each of these kets along $x$, $y$, and $z$ are the eigenvectors of their corresponding Pauli matrices. Each matrix has two eigenvectors and corresponding eigenvalues ($+1$ and $-1$).

Note that we can first choose the basis column vectors (for eg. the $z$-basis) and then arrive at the operator matrices above by experiment. For instance, a prepared state along $z$ would decompose with 50/50 probability to $+1$ and $-1$ when measured along the $x$-axis. We could then construct the possible state kets via the superposition principles given below.

#### Spin Along an Arbitrary Direction
For a spin operator along an arbitrary direction, defined by a unit spatial vector $\hat{n} = (n_x, n_y, n_z)$, we construct the appropriate operator matrix by taking the dot product of the formal vector of Pauli matrices $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ with $\hat{n}$. While $\vec{\sigma}.\hat{n}$ is not a standard vector inner product (since $\vec{\sigma}$ contains matrices), it denotes the linear combination of the Pauli matrices scaled by the spatial components of $\hat{n}$.

$$\sigma_{\hat{n}} = \hat{n} \cdot \vec{\sigma} = n_x \sigma_x + n_y \sigma_y + n_z \sigma_z = \begin{pmatrix} n_z & n_x - in_y \\ n_x + in_y & -n_z \end{pmatrix}$$

We can then calculate the eigenvectors and eigenvalues of this matrix to determine the state kets that result from this measurement. The eigenvalues remain $+1$ and $-1$.

Note that operators are linear, whereas eigenvalues may not be. You cannot simply add up the eigenvalues of the Pauli matrices, scaled by the spatial vector components, and claim that these are the eigenvalues of the spatial spin operator.

The eigenvectors and eigenvalues are intrinsic properties of the operator and do not depend on the initial state of the system. This means the possible values read during a measurement and the states the measurement collapses to depend on the operator alone. However, the probability of collapsing to each eigenvector, as well as the expectation value (the weighted average of the eigenvalues based on measurement probabilities), depend on the initial state.

### Superposition
To compute the probabilities and expectation value, we **decompose the initial state into a superposition of the operator's eigenvectors i.e. the possible final states**. The coefficient for each eigenvector in this linear combination is the probability amplitude. The absolute square of the probability amplitude yields the probability of measuring that specific eigenvalue.

For example, if an initial state is spin-up along the $z$-axis ($\vert{}+z\rangle$) and is measured along the $x$-axis, the initial state expressed in the measurement basis is:

 $$\vert{}+z\rangle = \frac{1}{\sqrt{2}}\vert{}+x\rangle + \frac{1}{\sqrt{2}}\vert{}-x\rangle$$

The probability of measuring $+1$ is $\vert{}\frac{1}{\sqrt{2}}\vert{}^2 = 0.5$, and the probability for $-1$ is also $0.5$. The expectation value is $0$. In general, for a spin-1/2 system, if the measurement axis is at an angle $\theta$ relative to the initial spin orientation, the expectation value is $\cos(\theta)$. The probabilities of measuring $+1$ and $-1$ are $\cos^2(\frac{\theta}{2})$ and $\sin^2(\frac{\theta}{2})$, respectively. This expectation value aligns with classical behavior, such as projecting a magnetic dipole moment along a magnetic field axis.

#### Spin-1/2 Measurement Requires 3 Measurements
The spin-1/2 state can be written as a linear combination of two states: up and down. However, the scaling factors are all complex numbers, so there are 4 real scalars. But we have a constraint in terms of requiring the superposition to have unit norm, so we essentially need 3 equations to determine the 3 independent variables. This means we need to carry out 3 measurements on an arbitrarily aligned spin state, for eg. along x, y and z axes. 

Note that we cannot carry out all 3 measurements on a single state as these operators do not commute and are therefore not compatible i.e. making one measurement will collapse the measurement to some value and make the other two measurements pointless. We would have to have multiple copies of the object on which we can carry out several measurments and determine probabilistically what each of the spin components are.

#### Working Directly With Kets
Abstractly, let the initial state be $\vert{}\psi\rangle$ and the observable operator be $A$, with eigenvectors $\vert{}x_+\rangle$ and $\vert{}x_-\rangle$. 

The operation $A\vert{}\psi\rangle$ maps the state to a new, unnormalized vector in the Hilbert space. $A\vert{}\psi\rangle$ has no physical significance. Mathematically speaking, $A$ stretches and skews $\vert{}\psi\rangle$ as a weighted average of the eigenvalues. If we then take the component of this stretched weighted-average along $\vert{}\psi\rangle$, we get the expectation value $\langle\psi\vert{}A\vert{}\psi\rangle$ of a measurement $A$ on an initial state $\vert{}\psi\rangle$.

We define the projection operator for an eigenvector $\vert{}x_i\rangle$ as $\vert{}x_i\rangle\langle x_i\vert{}$. This matrix (an outer product of a column vector and a row vector) acts on a state $\psi$ and projects it onto the subspace defined by $\vert{}x_i\rangle$ i.e. it finds the component of $\psi$ along $\vert{}x_i\rangle$. If the basis happens to correspond to the eigenvectors, $\vert{}x_i\rangle\langle x_i\vert{}$ will have a single $1$ and the rest of the elements set to $0$. The sum of the projection operators for all eigenvectors of an observable is the Identity matrix, $I = \sum_i \vert{}x_i\rangle\langle x_i\vert{}$, known as the completeness relation. 

By inserting the Identity matrix into the expectation value expression $\langle\psi\vert{}A\vert{}\psi\rangle$, we can expand it in terms of the eigenvectors:

$$\langle\psi\vert{}A\vert{}\psi\rangle = \langle\psi\vert{}I \cdot A \cdot I\vert{}\psi\rangle = \sum_i \sum_j \langle\psi\vert{}x_i\rangle\langle x_i\vert{}A\vert{}x_j\rangle\langle x_j\vert{}\psi\rangle$$

Since $\vert{}x_i\rangle$ are eigenvectors of $A$, the term $\langle x_i\vert{}A\vert{}x_j\rangle$ evaluates to the eigenvalue $\lambda_i$ if $i=j$ and $0$ otherwise (because $\langle x_i\vert{}x_j\rangle$ is zero from orthogonality). This collapses the double sum to a single sum:

$$\langle\psi\vert{}A\vert{}\psi\rangle = \sum_i \lambda_i \langle\psi\vert{}x_i\rangle\langle x_i\vert{}\psi\rangle = \sum_i \lambda_i \vert{}\langle x_i\vert{}\psi\rangle\vert{}^2$$

Here, $\lambda_i$ is the measured value and $\vert{}\langle x_i\vert{}\psi\rangle\vert{}^2$ is the probability of that measurement occurring. 

#### Projection Operators of Eigenvectors
If $E_n$ represents the projection operator $\vert{}e_n\rangle\langle e_n\vert{}$, where $\vert{}e_n\rangle$ is an eigenvector of the observable operator $L$ corresponding to the eigenvalue $a_n$, then the probability amplitude of a measurement of $L$ yielding $a_n$ is the projection of the state vector $\vert{}\psi\rangle$ onto the eigenvector $\vert{}e_n\rangle$: $\langle e_n\vert{}\psi\rangle$. 

The probability of obtaining this measurement is the absolute square of the amplitude, $\langle\psi\vert{}e_n\rangle\langle e_n\vert{}\psi\rangle$, which can be rewritten as: $\langle\psi\vert{}E_n\vert{}\psi\rangle$. This demonstrates that the probability of measuring a specific eigenvalue is mathematically identical to the expectation value of its corresponding projection operator $E_n$ for the state $\vert{}\psi\rangle$.

We can also derive the overall expectation value of the observable $L$ for the state $\vert{}\psi\rangle$ from this framework. The expectation value is the sum of all possible eigenvalues weighted by their respective probabilities:

$$\langle L \rangle = \sum_n a_n \langle\psi\vert{}E_n\vert{}\psi\rangle$$

By linearity, we can pull the scalar eigenvalues and the summation inside the inner product:

$$\langle L \rangle = \left\langle\psi\right\vert{} \left(\sum_n a_n E_n\right) \left\vert{}\psi\right\rangle$$

Because the spectral decomposition theorem states that any Hermitian operator can be constructed from its eigenvalues and projection operators ($L = \sum_n a_n E_n$), this simplifies directly to $\langle L \rangle = \langle\psi\vert{}L\vert{}\psi\rangle$

**In short:** 
- Calculate the eigenvalues and eigenkets of the measurement operator. Project the initial state $\psi$ onto each eigenvector via $\langle x_j\vert{}\psi\rangle$. Take the square of the norm to get the probability of the measurement collapsing to that eigenstate. 
OR 
Write the initial ket as a superposition/linear combination of the operator's eigenkets. The components squared are the probabilities. 

- The corresponding eigenvalue of each eigenket will be the measured value if the state collapses to that eigenstate. The eigenvalue is also the expectation value of a measurement along that eigenstate $\langle x_i\vert{}A\vert{}x_i\rangle$ (because it is the only value associated with that component state). 

- To get the expectation value, get the weighted average of eigenvalues. 

**Aside:** $\langle x_i\vert{}A\vert{}x_j\rangle$ is the transfer operator and represents how much of the state $\vert{}x_j\rangle$ maps into the state $\vert{}x_i\rangle$ after the operator $A$ is applied. Note that we can also construct an operator that transforms an initial state $\vert{}\psi\rangle$ into a final state $\vert{}\phi\rangle$, given by $\vert{}\phi\rangle\langle\psi\vert{}$. To see why, simply apply this operator to $\vert{}\psi\rangle$. This yields $\vert{}\phi\rangle\langle\psi\vert{}\psi\rangle$. Assuming $\vert{}\psi\rangle$ is a normalized state, the inner product $\langle\psi\vert{}\psi\rangle$ equals $1$, leaving exactly the state $\vert{}\phi\rangle$.

Also, unambiguously distinguishable states are represented by orthogonal kets.

**Aside 2:** Don't forget to ensure that all probabilities sum to 1. Keep all superpositions normalized. 

### How General POVMs Help

Taking the example from earlier, let us say we are given a state that is either $\vert{}1\rangle$ (spin down along z) or $\vert{}+\rangle$ (spin up along x). These are not orthonormal, so we cannot measure or distinguish between the two with certainty. 

Let us say we used a typical orthonormal projection operator basis for measurement: $\vert{}1\rangle\langle1\vert{}$ and $\vert{}0\rangle\langle0\vert{}$. If our measurement device shows $\vert{}0\rangle$, we can be sure that we started off with $\vert{}+\rangle$, since $\vert{}1\rangle$ is orthogonal to $\vert{}0\rangle$ and so the probability that it will register a measurement of $\vert{}0\rangle$ is $0$. However, if our measurement registered $\vert{}1\rangle$, we cannot say which state we started out with. This is not too bad. At least in some cases, we can say for sure that we are not wrong. Let us say the initial state has a 50/50 probability of being in $\vert{}1\rangle$ or $\vert{}+\rangle$. Our measurement device will register a $\vert{}0\rangle$ only when we start with a $\vert{}+\rangle$, and even then only in half those situations. So we can claim a certain outcome only 25% of the time.

Turns out we can do better by using more general POVM operators. We can construct projective operators $c\vert{}0\rangle\langle0\vert{}$ and $c\vert{}-\rangle\langle-\vert{}$, which are guaranteed to unambiguously identify $\vert{}+\rangle$ and $\vert{}1\rangle$ respectively, because they are formed by vectors that are orthogonal to the opposing states. 

So if the measurement shows up as $\vert{}0\rangle$, we started off with $\vert{}+\rangle$ (since $\vert{}1\rangle$ will never register on the $c\vert{}0\rangle\langle0\vert{}$ measurement operator). Of course, since $\vert{}+\rangle$ is a superposition given by $\frac{1}{\sqrt{2}}(\vert{}0\rangle + \vert{}1\rangle)$, the probability of measuring $\vert{}0\rangle$ is $c/2$. Similarly, if the measurement shows up as $\vert{}-\rangle$, we started off with $\vert{}1\rangle$. Once again, the probability of measurement is $c/2$. There will also be situations where we end up with an indecisive outcome.

The catch is the scalar multiplier $c$ of each operator, and the fact that since these two operators are not orthogonal, we need to define a new catch-all operator $I - c\vert{}0\rangle\langle0\vert{} - c\vert{}-\rangle\langle-\vert{}$ to satisfy the completeness theorem, which accounts for the indecisive outcomes. If we were to calculate the percentage of time with which we can claim an outcome with absolute certainty, it works out to $0.5(c/2 + c/2) = c/2$. 

From the completeness theorem requirement (ensuring the catch-all operator remains positive semi-definite), we can calculate $c$ to be $\frac{\sqrt{2}}{1+\sqrt{2}}$. So the certainty here works out to approximately $0.29$, which is better than the $0.25$ we had earlier. The downside is we cannot determine the post-measurement state when the catch-all indecisive outcome occurs.

## State Change Via Unitary Operators
In general, a superposition of states can be transformed into another superposition by applying a unitary operator $U(t)$. $U(t)$ is unitary means:

$$U^\dagger U = I$$

Unitary operators preserve the length of vectors (explained below), and are thus rotation operations. A unitary operator does not collapse or measure the superposition; it rigidly rotates the entire superposition structure within the Hilbert space. The complex amplitudes of the superposition states remain preserved in relation to the newly rotated basis vectors.

If your initial state is a superposition of basis vectors:

$$\vert{}\psi\rangle=\alpha\vert{}0\rangle+\beta\vert{}1\rangle$$

Applying a unitary operator $U$ yields:

$$U\vert{}\psi\rangle=U(\alpha\vert{}0\rangle+\beta\vert{}1\rangle)$$

$$U\vert{}\psi\rangle=\alpha U\vert{}0\rangle+\beta U\vert{}1\rangle$$

Because $U$ preserves vector lengths, $U\vert{}0\rangle$ and $U\vert{}1\rangle$ become new, valid, normalized state vectors (let's call them $\vert{}0'\rangle$ and $\vert{}1'\rangle$). The final state is guaranteed to be another valid superposition:

$$\vert{}\psi'\rangle=\alpha\vert{}0'\rangle+\beta\vert{}1'\rangle$$

### Why Unitarity
A unitary operator ensures that the sum of probabilities in the superposition is always equal to $1$. To see how, first note that when a state vector is written as a superposition of the eigenvectors of an operator, the absolute squares of the probability amplitudes or the components, represent the probabilities. The sum of the absolute squares of these components is therefore $1$. But this sum is also the square of the state vector's norm/length (its inner product), which must therefore also be $1$. Since the total probability and thus the norm must remain $1$ throughout time, the operator must be such that it preserves the norm of the vector.

Thus,

$$\langle\psi(t)\vert{}\psi(t)\rangle = \langle\psi(0)\vert{}U^\dagger U\vert{}\psi(0)\rangle = \langle\psi(0)\vert{}I\vert{}\psi(0)\rangle = \langle\psi(0)\vert{}\psi(0)\rangle$$

This holds true only when $U$ is unitary.

Another physical requirement for this operator is perfect reversibility. Time evolution must be deterministic in both directions, meaning given the state at some time $t$, we can calculate the state at some past or future time. While any matrix with a non-zero determinant has an inverse, a unitary matrix guarantees that its inverse ($U^\dagger$) is also a valid physical operator that preserves probability.

Determinism in both directions does not mean we can determine the exact value upon measurement of the state. The measurement will still yield values according to probabilities. Unitarity instead means the probability distribution, the expectation value, and the superposition of states will evolve deterministically with time.

### Measurement vs State Change
In the case of Hermitian operators and observables, we say that multiplying the operator matrix by a state vector does not represent the physical state of the system during or after the measurement. It is just a mathematical operation.

However, in the case of unitary operators and state change, the operator matrix acts as a deterministic transformation. Multiplying the matrix by a state vector i.e. $U\vert{}\psi\rangle$, actively calculates the new, valid physical state of the system.

**Example: Pauli Matrices are Hermitian & Unitary**
Since the Pauli matrices fulfil both conditions, they can serve as mathematical tools for measurement, as well as unitary operators to transform a superposition into something else. 

Multiplying the matrix by a state vector ($\sigma_i\vert{}\psi\rangle$) is used only mathematically to:

-   Calculate expectation probabilities ($\langle\psi\vert{}\sigma_i\vert{}\psi\rangle$).
-   Extract the real eigenvalues (the physical measurement outcomes of $+1$ or $-1$).
-   Define the orthogonal eigenvectors (the localized states the system can collapse into).
    
Physical measurement causes a discontinuous, probabilistic collapse into one of these eigenvectors. This collapse is calculated using projection operators, not by multiplying the state by the observable matrix.

However, in the context of time evolution or quantum logic gates, the Pauli matrix represents a deterministic transformation. $U\vert{}\psi\rangle$ actively calculates the new, valid physical state of the system.

Applying the physical equivalent of the matrix, such as exposing a spin-1/2 particle to a precisely timed external magnetic field or routing a qubit through an X-gate, deterministically rotates the initial state vector into a new superposition while perfectly preserving its total probability.

### Unitary Operators as Time Evolution Operators
Mathematically, any unitary operator can be interpreted as a time evolution operator, i.e. the evolution of a state with time, $\vert{}\psi(t)\rangle$, can be described by the action of operator $U$ on the initial state $\vert{}\psi(0)\rangle$. 

We assume that time evolution is continuous and can thus be broken into an evolution over infinitesimally small discrete steps. 

Since $U$ is a rotation operator, it can be written as $$U=e^{-i\epsilon K}$$ i.e. the complex exponent (which preserves length and only rotates a vector) of some operator $K$. Approximating the complex exponential allows us to write any unitary operator $U$, and of current interest to us: time evolution operators, as a series of small changes from the Identity matrix: $U\approx I-i\epsilon K$, for a state change from time $t$ to time $t+\epsilon$

$K$ must be Hermitian, meaning its eigenvalues are strictly real, which makes it a valid physical observable. To prove this, since $U^\dagger U = I$, we can write:

$$U^\dagger U = \left(I + i\epsilon K^\dagger\right)\left(I - i\epsilon K\right) = I$$

$$I - i\epsilon K + i\epsilon K^\dagger + \epsilon^2K^\dagger K = I$$

Ignoring the second-order $\epsilon^2$ term (as $\epsilon$ is infinitesimally small) and subtracting $I$ from both sides, we get:

$$i\epsilon (K^\dagger - K) = 0$$

Which requires that:

$$K = K^\dagger$$

## Time Dependence
### The Time-dependant Schrodinger Equation
Since any unitary operator can be interpreted as a time evolution operator, we can use an appropriate operator to assess how a state evolves in time. We can utilize the approximate relation $U\approx I-i\epsilon K$, where we use the quantum Hamiltonian $H$ in place of $K$. To ensure the dimensionality of units is maintained from the start (since the exponent or multiplier of a physical time step must be dimensionless), we divide by the reduced Planck constant $\hbar$:

$$U(\epsilon) = I - \frac{i\epsilon}{\hbar}H$$

(The minus sign and the imaginary unit $i$ are conventions that link this equation to classical Hamiltonian mechanics and ensure oscillatory solutions).

Applying this operator to the state at time $t$:

$$\vert{}\psi(t+\epsilon)\rangle = \left(I - \frac{i\epsilon}{\hbar}H\right)\vert{}\psi(t)\rangle = \vert{}\psi(t)\rangle - \frac{i\epsilon}{\hbar}H\vert{}\psi(t)\rangle$$

If we take $\vert{}\psi(t)\rangle$ to the other side and divide by $\epsilon$, we construct the difference quotient for a derivative:

$$\frac{\vert{}\psi(t+\epsilon)\rangle - \vert{}\psi(t)\rangle}{\epsilon} = -\frac{i}{\hbar}H\vert{}\psi(t)\rangle$$

Taking the limit as $\epsilon \to 0$, the left side becomes the time derivative of the state vector. Rearranging the constants yields the time-dependent Schrödinger equation:

$$i\hbar \frac{d}{dt}\vert{}\psi(t)\rangle = H\vert{}\psi(t)\rangle$$

 corresponding to the total energy of the system. $H$ is identified with the Hamiltonian via its analoguous behavior to classical mechanics, where the time derivative of a variable is given by its Poisson Bracket with the Hamiltonian. One can also arrive at this by looking at Noether's theorem for energy conservation. A Unitary operator can be written as the exponential of a Hermitian operator. Taking time derivatives gives a multiplicative factor of the Hermitian operator, which turns out to be $H$.

### The Hamiltonian

Since $H$ is a Hermitian operator, it must have real eigenvalues, which represent the possible energy states. Let us denote these eigenvalues as $E_j$.

Thus, the eigenvalue equation is:

$$H\vert{}E_j\rangle = E_j\vert{}E_j\rangle$$

We can now determine how the probability amplitudes of the energy values of a state evolve over time, by expanding it in the energy eigenbasis. The time-dependent Schrödinger equation is:
 $$i\hbar\frac{d}{dt}\vert{}\psi(t)\rangle = H\vert{}\psi(t)\rangle$$

Write $\vert{}\psi(t)\rangle$ as a linear combination of the eigenstates of $H$, where the probability amplitudes $\alpha_j$ are time-dependent:

$$\vert{}\psi(t)\rangle = \sum_j \alpha_j(t)\vert{}E_j\rangle$$

**Aside:** In the Schrodinger picture, $\alpha_j(t)$ is time dependent while $E_j$ and $H$ are time independent. The Heisenberg picture reverses this.

Substituting the superposition into the Schrödinger equation yields:

$$i\hbar\frac{d}{dt}\left(\sum_j \alpha_j(t)\vert{}E_j\rangle\right) = H\left(\sum_j \alpha_j(t)\vert{}E_j\rangle\right)$$

On the right side, the Hamiltonian acts linearly on the eigenstates, which can be replaced by their corresponding eigenvalues $E_j$:

$$\sum_j \left(i\hbar\frac{d\alpha_j(t)}{dt}\right)\vert{}E_j\rangle = \sum_j \left(E_j\alpha_j(t)\right)\vert{}E_j\rangle$$

Bringing all terms to one side gives:

$$\sum_j \left( i\hbar\frac{d\alpha_j(t)}{dt} - E_j\alpha_j(t) \right) \vert{}E_j\rangle = 0$$
Because the eigenvectors $\vert{}E_j\rangle$ form an orthonormal basis, they are linearly independent. For this sum to equal the zero vector, the coefficient for each $\vert{}E_j\rangle$ must independently be zero. This yields a set of decoupled, first-order differential equations for each amplitude:

$$i\hbar\frac{d\alpha_j(t)}{dt} = E_j\alpha_j(t)$$

Solving this differential equation for $\alpha_j(t)$ gives the complex phase $e^{-iE_jt/\hbar}$ that represents time evolution:

$$\alpha_j(t) = \alpha_j(0)e^{-iE_jt/\hbar}$$

**In short:** To determine how a quantum state evolves over time:
Determine the state ket at the initial time, $\vert{}\psi(0)\rangle$. 

Define the system's Hamiltonian $H$ and determine its energy eigenvalues $E_j$ and eigenstates $\vert{}E_j\rangle$.

Decompose the initial state into the energy eigenbasis by calculating the initial probability amplitude for each component: $\alpha_j(0) = \langle E_j\vert{}\psi(0)\rangle$.

Determine the state $\vert{}\psi(t)\rangle$ at a future time $t$ by multiplying each initial amplitude by its corresponding time-evolution phase factor, $e^{-iE_jt/\hbar}$, and summing the resulting components:
    $$\vert{}\psi(t)\rangle = \sum_j \alpha_j(0)e^{-iE_jt/\hbar}\vert{}E_j\rangle$$
    
**Note:** If we utilize the Schrodinger equation to evaluate time evolution, we are in a sense looking at continuous time evolution over infinitesimal changes in $t$. If we instead directly apply the unitary operator on a state ket, we are in a way looking at time evolution discretely i.e. as a jump from $t_i$ to $t_f$.  

### Time Evolution of Expectation Values

The expectation value $\langle\psi\vert{}L\vert{}\psi\rangle$, denoted as $\langle L \rangle$, can be evaluated dynamically to determine how the center of a measurement's probability distribution evolves over time. In the derivation below, the operator $L$ is assumed to be time-independent, consistent with the Schrödinger picture.

Applying the product rule to the inner product yields:

$$\frac{d}{dt}\langle L \rangle = \frac{d}{dt}\langle\psi(t)\vert{}L\vert{}\psi(t)\rangle = \left(\frac{d}{dt}\langle\psi(t)\vert{}\right)L\vert{}\psi(t)\rangle + \langle\psi(t)\vert{}L\left(\frac{d}{dt}\vert{}\psi(t)\rangle\right)$$

Recall the time-dependent Schrödinger equation and its conjugate transpose (since $H$ is Hermitian, $H^\dagger = H$):

$$\frac{d}{dt}\vert{}\psi(t)\rangle = -\frac{i}{\hbar}H\vert{}\psi(t)\rangle$$

$$\frac{d}{dt}\langle\psi(t)\vert{} = \frac{i}{\hbar}\langle\psi(t)\vert{}H$$

Substituting these relations into the expanded derivative gives:

$$\frac{d}{dt}\langle L \rangle = \left(\frac{i}{\hbar}\langle\psi(t)\vert{}H\right) L \vert{}\psi(t)\rangle + \langle\psi(t)\vert{} L \left(-\frac{i}{\hbar}H\vert{}\psi(t)\rangle\right)$$

Factoring out the constants:

$$\frac{d}{dt}\langle L \rangle = \frac{i}{\hbar}\langle\psi(t)\vert{}(HL - LH)\vert{}\psi(t)\rangle$$

Using standard commutator notation, $[A, B] = AB - BA$, this simplifies to a statement of Ehrenfest's theorem:

$$\frac{d}{dt}\langle L \rangle = \frac{i}{\hbar}\langle\psi(t)\vert{}[H, L]\vert{}\psi(t)\rangle = -\frac{i}{\hbar}\langle\psi(t)\vert{}[L, H]\vert{}\psi(t)\rangle$$

This formulation is structurally analogous to classical mechanics, where the time derivative of a classical dynamical variable relies on its Poisson bracket with the classical Hamiltonian.

Consequently, if an observable operator $L$ does not commute with $H$ (i.e., $[L, H] \neq 0$), its expectation value is not conserved. Conversely, if it does commute with $H$, its expectation value is a constant of the motion. If $L$ commutes with $H$, every function of $L$ is also conserved (e.g., $L^n$). The most trivial candidate for commutation is $H$ itself, which physically implies the conservation of energy. 

### Symmetries in Quantum Mechanics
We can arrive at this commutation relation from another line of reasoning. In general, a symmetry operation is considered a transformation that does not change the physical predictions (the measurable observations) of the system. In quantum mechanics, these observable values are probabilities, which correspond to the absolute square of the transition probability amplitudes between states. Thus, a symmetry operation must leave $\vert{}\langle\psi\vert{}\phi\rangle\vert{}^2$ unchanged for any two states $\vert{}\psi\rangle$ and $\vert{}\phi\rangle$ before and after the transformation.

According to Wigner's theorem, this strict conservation of probability is mathematically possible if and only if the transformation is represented by an operator that is either linear and unitary, where:

$$\langle\psi'\vert{}\phi'\rangle = \langle\psi\vert{}\phi\rangle$$

or antilinear and anti-unitary, where the inner product converts to its complex conjugate:

$$\langle\psi'\vert{}\phi'\rangle = \langle\psi\vert{}\phi\rangle^* = \langle\phi\vert{}\psi\rangle$$

However, for continuous symmetries (such as spatial translations or rotations), the transformation must remain valid even when the applied shift is infinitesimally small. This requires the symmetry operator to continuously tend toward the Identity operator as the transformation parameter approaches zero. Because the Identity operator is strictly linear and unitary, continuous symmetries can only be represented by unitary operators. However, anti-unitary operators become mathematically essential for discrete symmetries that involve sudden flips and cannot be built from infinitesimal steps, most notably time reversal.

We can also impose a dynamical requirement on a continuous symmetry: applying a symmetry transformation to a state followed by time evolution should yield the same physical state as time-evolving the state first and then applying the symmetry. If we denote the unitary symmetry operator as $U_R$ and the time-evolution operator as $U_t$, this requires:

$$U_R U_t\vert{}\psi\rangle = U_t U_R\vert{}\psi\rangle$$

Because this must hold for all states $\vert{}\psi\rangle$, the two operators must commute: $[U_R, U_t] = 0$.

Since the Hamiltonian is the infinitesimal generator of time evolution, and if we define a Hermitian observable $L$ as the infinitesimal generator of the symmetry ($U_R = e^{-i\lambda L/\hbar}$), then both $[L, H] = 0$ and $[U_R, H] = 0$.

## Compatible Observables
### Uncertainty Principle
Given two operators, $A$ and $B$, the generalized uncertainty principle states that the product of the standard deviations (uncertainties) of their measurements, $\sigma_A$ and $\sigma_B$, is strictly bounded by the expectation value of their commutator: $\sigma_A \sigma_B \geq \frac{1}{2} \vert{}\langle[A, B]\rangle\vert{}$ where the uncertainty of a given observable is statistically defined as its standard deviation: $\sigma_A = \sqrt{\langle A^2 \rangle - \langle A \rangle^2}$.

### Mechanics of Commutativity and Simultaneous Observation
If two operators commute, they are compatible, i.e. both observables can be measured simultaneously without any mutual uncertainty in their values.

Two operators commute if and only if they share a simultaneous basis of eigenvectors. Too see why, consider the case when two operators share a simultaneous eigenbasis. This means they can both be diagonalized simultaneously. 

Given the components $x_i$ of a column vector and diagonal components $a_i$ and $b_i$ of $A$ and $B$, both operations $AB$ and $BA$ will result in new vector components $a_ib_ix_i$. Since because $a_ib_i$ = $b_ia_i$. $AB - BA$ is therefore 0. 

However, if they do not commute, then suppose $A$ is diagonalized, $B$ will still have off-diagonal components that will mix the components of $X$. This mixing will differ in magnitude for $AB$ and $BA$, as can be seen below.

**Operation 1: $AB\vert{}\psi\rangle$**

First, $B$ mixes the components of the initial state vector:
 

$$B\vert{}\psi\rangle=\sum_i\left(\sum_j B_{ij}x_j\right)\vert{}i\rangle$$

Next, $A$ scales each newly mixed component by its respective eigenvalue $a_i$:

$$AB\vert{}\psi\rangle=\sum_{i,j} a_i B_{ij} x_j\vert{}i\rangle$$

**Operation 2: $BA\vert{}\psi\rangle$**

First, $A$ scales the original components of the initial state by $a_j$:
  

$$A\vert{}\psi\rangle=\sum_j a_j x_j\vert{}j\rangle$$

Next, $B$ mixes these pre-scaled components:
  
$$BA\vert{}\psi\rangle=\sum_{i,j} B_{ij} a_j x_j\vert{}i\rangle$$

$$(AB-BA)\vert{}\psi\rangle=\sum_{i,j} (a_i B_{ij} x_j - B_{ij} a_j x_j)\vert{}i\rangle$$

$$(AB-BA)\vert{}\psi\rangle=\sum_{i,j} B_{ij}(a_i-a_j)x_j\vert{}i\rangle$$

This equation reveals the fundamental physical reality of the commutator: It is a measure of cross-contamination.

**Note:** The uncertainty principle does not mean that if we make a measurement of an observable, it will somehow disturb the measurement of another observable. This is not a statement of interference or wave function collapse etc. This is a statement of how the standard deviation or uncertainty of an ensemble of measurements will behave. Recall that the standard deviation is define with respect to the expecation values. So the uncertainty principle is really saying that over let's say thousand of measurements, the "spread" in the two measurements has a lower bound. If the observables commute and the lower bound is $0$, it means we can always find some measurement basis that allows us to "deterministically" measure both observables without any variance. For eg., if we prepared a spin-1/2 state along some arbitrary spatial direction $n$, and we wanted to measure the spin and 2 times the spin (just as an example), if we aligned our measurement apparatus along $n$, we would deterministically measure $+1$ and $+2$ every time, and thus have $0$ variance. However, the uncertainty principle only gives a lower bound. If we were to conduct measurements along some other random spatial direction, we _would_ have some variance. 

**Aside:** We see commutativity as a measure of the curvature of the space time, via the Riemann tensor in General Relativity. 
There is also a major, active branch of theoretical physics known as Noncommutative Geometry, where distorted spacetime causes the coordinates themselves to act as non-commuting operators resulting in measurement uncertainty. It enforces a fundamental Spacetime Uncertainty Principle. It dictates that you mathematically cannot measure the x-coordinate and y-coordinate of an event simultaneously with infinite precision

### Complete Set of Compatible Observables
Let us start with an observable $A$. If $A$ has eigenvectors that share the same eigenvalue, the eigenvalue corresponds not to a 1D line, but to a $k$-dimensional geometric subspace. When we make a measurement, we know the value of the measurement, but the state of the system is ambiguous -- it could be any of the corresponding eigenvectors. 

To resolve the ambiguity, we use a compatible observable $B$ to add extra information and reduce the k-dimensional subspace ambiguity. $B$ may be able to split that $k$-dimensional plane into $k$ unique 1D lines. If not, we would like to add other mutually compatible observables until the tuple of eigenvalues for each eigenvector, $x\vert{}a,b,c...\rangle$,  is unique.

The size of the CSCO tells you the independent degrees of freedom in the system. Mathematically, independent degrees of freedom are constructed by taking the tensor product of smaller, fundamental Hilbert spaces.

#### Example: The Hydrogen Atom
Consider the energy states of the Hydrogen atom (ignoring spin).

**Step 1: The Hamiltonian ($H$)**
Measuring just the energy yields the eigenvalue $E_n$. However, there are multiple distinct electron orbitals (like the 2s and 2p orbitals) that possess the exact same energy. The state is degenerate. $H$ alone is not a CSCO.

**Step 2: Adding Total Orbital Angular Momentum ($L^2$)**
$L^2$ commutes with $H$. Measuring it yields the eigenvalue quantum number $l$. Now you have the tuple $(n, l)$. This distinguishes the 2s orbital from the 2p orbital, but the 2p orbital still has three distinct geometric orientations in space ($p_x, p_y, p_z$) that share the exact same $n$ and $l$. The set $\{H, L^2\}$ is still not a CSCO.

**Step 3: Adding the Z-Component of Angular Momentum ($L_z$)**
$L_z$ commutes with both $H$ and $L^2$. Measuring it yields the eigenvalue quantum number $m$. Now you have the tuple $(n, l, m)$.

In the non-relativistic, spinless Hydrogen atom, there is no further degeneracy. Every possible unique spatial orbital corresponds strictly to a unique combination of $(n, l, m)$. Therefore, you know that $\{H, L^2, L_z\}$ is a Complete Set of Commuting Observables.

#### CSCO is Minimal: $p$ and $H$ Example
Note that the CSCO is the *minimal* set of compatible observables needed to acquire the maximum possible information about a system. 

For example, for a free particle, $H$ represents the energy of the particle. Measuring the energy tells you the magnitude of the momentum. However, you still do not know the direction of the momentum, which means you need to measure momentum as well. $H$ and $p$ commute because $H$ is a power of $p$. So are there 2 observables in the CSCO? 

Not really. Consider what would happen if we measured just $p$. It will tell you both the momentum and the energy. This is where the *minimal* requirement of the CSCO comes in. If an operator can be expressed purely as a mathematical function of the other operators in the set, it adds no new physical information and is excluded from the CSCO.

### Measuring Spin Along An Arbitrary Axis
Since $\sigma_x$, $\sigma_y$, and $\sigma_z$ do not commute and are thus incompatible, it means we cannot have simultaneous information about all of them. This means we cannot conclusively determine the spin-1/2 state along some arbitrary spatial direction. To determine an unknown spin direction, you must be provided with an ensemble: a large number of identical particles, all prepared in the exact same unknown state $\vert{}\psi\rangle$, apply measurement along $x$, $y$ and $z$, and determine via the measured expectation value, what $\sigma$ is.

#### The No-Cloning Constraint
It is crucial to understand that you cannot simply take a single unknown particle and copy it to create the required ensemble yourself.

The No-Cloning Theorem strictly forbids the creation of identical copies of an arbitrary, unknown quantum state. If you try to build an ensemble by copying a single particle, the copying mechanism will inherently entangle and corrupt the state. Therefore, the physical direction of a quantum state can only be known if the source that generated it provides you with a statistically significant number of identical iterations.

### Quantum Physics in Projection Operator Formalism
The mathematics of quantum mechanics can also be presented through orthonormal projection operators rather than state vectors. For example, a general density matrix state can be written as a linear combination of orthonormal projection operators:

$$\rho = \sum_i p_i \vert{}i\rangle\langle i\vert{}$$

(For a pure state, this simplifies to $\rho = \vert{}\psi\rangle\langle\psi\vert{}$). Note that the scalar multiplication factors here are the probabilities themselves, and not probability amplitudes as in the case of state vectors.

In terms of matrices, if written in the same orthonormal basis $\{\vert{}i\rangle\}$, each item $\vert{}i\rangle\langle i\vert{}$ in the summation is a matrix with a single $1$ in the $i$-th column and row, and zero everywhere else, multiplied by the scalar $p_i$. If written in some other basis, there will be off-diagonal terms.

The inner product of two density matrices $\rho_1$ and $\rho_2$ is given by $\text{tr}(\rho_1 \rho_2)$. In general, if $\vert{}a\rangle$ and $\vert{}b\rangle$ are two vectors, the trace of their outer product gives the reversed inner product: $\text{tr}(\vert{}a\rangle\langle b\vert{}) = \langle b \vert{} a \rangle$.

The probability of obtaining a specific measurement outcome, represented by the measurement operator $M_m$, is given by $\text{tr}(M_m^\dagger M_m \rho)$. For projective measurements, where the projector is $P_m = \vert{}m\rangle\langle m\vert{}$, and using the cyclic property of the trace ($\text{tr}(ABC) = \text{tr}(CAB)$), this works out to $\text{tr}(\vert{}m\rangle\langle m\vert{} \rho)$.

The post-measurement state is given by:

$$\frac{M_m \rho M_m^\dagger}{\text{tr}(M_m^\dagger M_m \rho)}$$

**Aside:** Note that traces follow the rules of linearity. Also, to understand a trace, see that each element of the matrix can be obtained in the following way: place the $j$-th basis column vector $\vert{}j\rangle$ on the right of the matrix and perform matrix multiplication. This gives us a column vector. Then place the $i$-th basis row vector $\langle i\vert{}$ to the left and perform matrix multiplication. This is just an inner product and gives the $ij$-th element of the matrix. In Dirac notation, this is written as $\langle i \vert{} M \vert{} j \rangle$. Taking the summation of the diagonal elements over all $i$ gives the trace.

## Entanglement
### Density Matrices
Let us evaluate the expectation value of an observable $L$ for a system prepared in a pure state $\vert{}\psi\rangle$. The trace of an operator $L$ is defined as the sum of its diagonal elements in any chosen orthonormal basis $\vert{}i\rangle$:

$$\text{Tr}(L) = \sum_i \langle i\vert{}L\vert{}i\rangle$$

The expectation value $\langle L \rangle$ is the trace of the product of the projection operator $\vert{}\psi\rangle\langle\psi\vert{}$ and the observable $L$. 

To prove this, let us construct the operator $\vert{}\psi\rangle\langle\psi\vert{}L$ and take its trace:

$$\text{Tr}(\vert{}\psi\rangle\langle\psi\vert{}L) = \sum_i \langle i\vert{}\psi\rangle\langle\psi\vert{}L\vert{}i\rangle$$
Because $\langle i\vert{}\psi\rangle$ and $\langle\psi\vert{}L\vert{}i\rangle$ are scalars, they commute and can be rearranged:

$$\text{Tr}(\vert{}\psi\rangle\langle\psi\vert{}L) = \sum_i \langle\psi\vert{}L\vert{}i\rangle\langle i\vert{}\psi\rangle$$
Using the completeness relation $I = \sum_i \vert{}i\rangle\langle i\vert{}$, we can factor out the basis vectors to collapse the sum:

$$\text{Tr}(\vert{}\psi\rangle\langle\psi\vert{}L) = \langle\psi\vert{}L \left( \sum_i \vert{}i\rangle\langle i\vert{} \right) \vert{}\psi\rangle = \langle\psi\vert{}L I \vert{}\psi\rangle = \langle\psi\vert{}L\vert{}\psi\rangle = \langle L \rangle$$

We define the projection operator $\vert{}\psi\rangle\langle\psi\vert{}$  as the density matrix $\rho$, making $\langle L \rangle = \text{Tr}(\rho L)$.

To understand what is happening here, think of what the projection operator of a state vector $\psi$ onto another state $\phi$ represents. It is an extraction of the component vector of $\phi$ along $\psi$. In an analogous fashion, by applying the projection on $L$, we are extracting the specific scalar component of the operator matrix $L$ that acts strictly along the geometric axis defined by the state vector $\vert{}\psi\rangle$.

Density matrices become mathematically necessary when dealing with mixed states. A pure state is a system whose quantum state is known with total certainty, represented by a single state vector $\vert{}\psi\rangle$ (which itself may be a superposition of basis eigenstates). A mixed state is a statistical ensemble where classical uncertainty exists regarding which pure state the system is actually in. If a system has classical probabilities $P_k$ of being in various pure states $\vert{}\psi_k\rangle$, the density matrix generalizes to:

$$\rho = \sum_k P_k \vert{}\psi_k\rangle\langle\psi_k\vert{}$$

where $\sum_k P_k = 1$.

The formula for the expectation value however is still given by: $\langle L \rangle = \text{Tr}(\rho L)$. Density matrices are Hermitian ($\rho = \rho^\dagger$), positive semi-definite, and their trace is exactly $1$ ($\text{Tr}(\rho) = 1$), since the total probability of all states must be $1$. 

For pure states, the density matrix is idempotent ($\rho^2 = \rho$), which implies $\text{Tr}(\rho^2) = 1$. For mixed states, idempotency fails ($\rho^2 \neq \rho$), and $\text{Tr}(\rho^2) < 1$. This provides a concrete mathematical test to determine whether a given state is pure or mixed.

To see why this happens structurally, consider rotating the density matrix into its own eigenbasis. Because $\rho$ is Hermitian, it can always be diagonalized. 

For a pure state $\rho = \vert{}\psi\rangle\langle\psi\vert{}$, the state vector $\vert{}\psi\rangle$ is an eigenvector of $\rho$ with an eigenvalue of $1$ (which represents the probability of $\psi$ in the mixed state). All other orthogonal basis vectors have eigenvalues of $0$. In this basis, $\rho$ is a diagonal matrix with a single $1$ and zeroes elsewhere. Squaring this matrix yields the exact same matrix, so $\rho^2 = \rho$ and $\text{Tr}(\rho^2) = 1$.

For a mixed state, diagonalization yields the classical probabilities on the diagonal. There will be at least two non-zero eigenvalues $p_k$, where $0 < p_k < 1$. The trace is the sum of these eigenvalues, which must be total probability: $\text{Tr}(\rho) = \sum p_k = 1$. However, squaring the matrix squares these eigenvalues. Since each $p_k$ is a positive fraction less than $1$, its square is strictly less than itself ($p_k^2 < p_k$). Therefore, the sum of their squares is strictly less than the sum of the original probabilities:

$$\text{Tr}(\rho^2) = \sum_k p_k^2 < \sum_k p_k = 1$$

Because $\text{Tr}(\rho^2) < 1$, $\rho^2 \neq \rho$, meaning the mixed state density matrix is not idempotent.

### Pure vs. Mixed State Shortcuts
There are several mathematical shortcuts to determine whether a density matrix $\rho$ represents a pure state or a mixed state:
* **Rank Test:** A pure state density matrix has a rank of $1$. This means there is only one linearly independent row or column, which corresponds to the single eigenvector associated with the eigenvalue of $1$ (the state vector $\vert{}\psi\rangle$).
* **Determinant Test ($2 \times 2$ Matrices):** For a $2 \times 2$ density matrix, if $\det(\rho) = 0$, it is a pure state. This is a direct consequence of the rank condition. Because the trace is the sum of the eigenvalues ($\lambda_1 + \lambda_2 = 1$) and the determinant is their product ($\lambda_1 \lambda_2 = 0$), one eigenvalue must be $1$ and the other must be $0$.
This test does not work for $N > 2$ because the determinant = 0 test only tells you that the matrix is not full rank i.e. it is flat in at least one dimension of the Hilbert space. For $N = 2$, this is the same as a rank 1 matrix. As an example, suppose $N = 3$ and we prepare 3 states with probabiltiies $0.5$, $0.5$ and $0$. The determinant is 0, but the state is not pure.
* **Diagonal Element Test:** If a density matrix is completely diagonal, it represents a pure state if and only if exactly one diagonal element is $1$ and all others are $0$.
* **Off-Diagonal Constraint (Coherence):** If the matrix is not diagonal, the magnitudes of the off-diagonal elements (coherences) are strictly constrained by the diagonal elements (populations). For a pure state, the condition $\vert{}\rho_{ij}\vert{}^2 = \rho_{ii}\rho_{jj}$ must hold for any $2 \times 2$ sub-matrix. This is the exact condition required to satisfy $\text{Tr}(\rho^2) = 1$.

### Correlation and Entangled States
Consider a two-particle system. The states of this system can be represented by a tensor product of the individual vector spaces, $U \otimes V$. A composite state vector is represented by $\vert{}a\rangle \otimes \vert{}b\rangle$ (often abbreviated as $\vert{}a, b\rangle$ or $\vert{}ab\rangle$), where $\vert{}a\rangle$ is a state in vector space $U$ and $\vert{}b\rangle$ is a state in vector space $V$.
  
If we have an operator $A$ acting on vector space $U$ and an operator $B$ acting on vector space $V$, then $A$ acts strictly on $\vert{}a\rangle$ and $B$ acts strictly on $\vert{}b\rangle$ as though the other vector space did not exist. Thus:
  
$$(A \otimes B)(\vert{}a\rangle \otimes \vert{}b\rangle) = (A\vert{}a\rangle) \otimes (B\vert{}b\rangle)$$

Additionally, for a sum of non-interacting operators (such as the total Hamiltonian of two non-interacting particles):
  
$$(A \otimes I + I \otimes B)(\vert{}a\rangle \otimes \vert{}b\rangle) = (A\vert{}a\rangle) \otimes \vert{}b\rangle + \vert{}a\rangle \otimes (B\vert{}b\rangle)$$

A tensor product of two 2-dimensional vector spaces yields a 4-dimensional composite vector space. Let us write an arbitrary pure state in the tensor product space of two spin-1/2 particles as a superposition of the basis states:
  
$$\vert{}\psi\rangle = c_1\vert{}uu\rangle + c_2\vert{}ud\rangle + c_3\vert{}du\rangle + c_4\vert{}dd\rangle$$

The constraint on the complex coefficients $c_1, c_2, c_3, c_4$ is that the sum of their absolute squares must equal $1$ due to probability normalization: $\vert{}c_1\vert{}^2 + \vert{}c_2\vert{}^2 + \vert{}c_3\vert{}^2 + \vert{}c_4\vert{}^2 = 1$.
  
However, there is no guarantee that this arbitrary composite state can be factored back into a simple tensor product of two individual particle states, $(a_1\vert{}u\rangle + a_2\vert{}d\rangle) \otimes (b_1\vert{}u\rangle + b_2\vert{}d\rangle)$.
  
If we assume the composite state _can_ be written in this separable form, expanding the product yields:
  
$$(a_1 b_1)\vert{}uu\rangle + (a_1 b_2)\vert{}ud\rangle + (a_2 b_1)\vert{}du\rangle + (a_2 b_2)\vert{}dd\rangle$$

Equating the coefficients to our original arbitrary state requires:
  
$$c_1 = a_1 b_1, \quad c_2 = a_1 b_2, \quad c_3 = a_2 b_1, \quad c_4 = a_2 b_2$$
By multiplying $c_1$ and $c_4$, and $c_2$ and $c_3$, we find that $c_1 c_4 = a_1 b_1 a_2 b_2$ and $c_2 c_3 = a_1 b_2 a_2 b_1$. This enforces the algebraic condition:
  
$$c_1 c_4 - c_2 c_3 = 0$$

This condition is a strict algebraic constraint over and above the normalization constraint, and it is generally not true for an arbitrary set of coefficients. If $c_1 c_4 - c_2 c_3 \neq 0$, the state cannot be factored into independent single-particle pure states. Such a state is defined as an **entangled state**, meaning the properties of the two particles are intrinsically correlated and cannot be described independently.


### Bell States
Some states are obviously correlated. For example, $\frac{1}{\sqrt{2}}(\vert{}uu\rangle + \vert{}dd\rangle)$ implies that measurements of the two particles will always agree (both up or both down). Similarly, $\frac{1}{\sqrt{2}}(\vert{}ud\rangle - \vert{}du\rangle)$ implies they will always disagree.

Because a system of two spin-1/2 particles forms a 4-dimensional Hilbert space, we can construct a complete orthonormal basis of maximally entangled states by defining two additional configurations. These four states are known as the Bell states (or EPR pairs):

$$\vert{}\Phi^\pm\rangle = \frac{1}{\sqrt{2}}(\vert{}uu\rangle \pm \vert{}dd\rangle)$$
$$\vert{}\Psi^\pm\rangle = \frac{1}{\sqrt{2}}(\vert{}ud\rangle \pm \vert{}du\rangle)$$

### Checking for Entanglement (The Reduced Density Matrix)
To mathematically verify if a bipartite (2-particle) pure state is entangled, you must calculate the **reduced density matrix** of one of the individual subsystems (e.g., subsystem A). This is done by taking the "partial trace" over subsystem B, which effectively averages out the degrees of freedom of particle B.

The matrix elements of the reduced density matrix $\rho^A$ are given by:

$$\rho^A_{a,a'} = \sum_b \psi_{a,b} \psi^*_{a',b}$$

This represents the density matrix of a single-particle state, constructed by summing over the basis states of the ignored subsystem B. It is similar to the density matrix of a single particle system, except for the summation over B.

Once $\rho^A$ is constructed, we apply the standard idempotency test ($\text{Tr}((\rho^A)^2) = 1$) to determine if subsystem A is in a pure or mixed state. If the overall composite state is pure, but the reduced density matrix $\rho^A$ describes a mixed state, then the original bipartite state is entangled. 

A mixed state where every eigenvalue of $\rho^A$ is equal (for a qubit, both eigenvalues are $1/2$, making $\rho^A$ proportional to the Identity matrix) indicates a maximally entangled state, meaning all possible measurement outcomes for subsystem A are equally probable.

Note that we cannot determine if a two-particle system is entangled simply by taking local measurements on one of the particles. A local observer measuring particle A cannot mathematically distinguish whether their measurement statistics such as probabilities and expectation values originate from a regular superposition in a pure state or from the classical probabilities of a mixed state.

For example, measuring the spin along the $x$-axis ($\sigma_x$) for a pure state prepared as spin-up along the $z$-axis ($\vert{}+z\rangle$):

$$\vert{}+z\rangle = \frac{1}{\sqrt{2}}(\vert{}+x\rangle + \vert{}-x\rangle)$$

yields an expectation value of $\langle \sigma_x \rangle = 0$.

However, you obtain the exact same expectation value from a statistically mixed state prepared with a $50/50$ classical probability of being strictly spin-up or spin-down. The density matrix for this mixed state is:


$$\rho = \frac{1}{2}(\vert{}u\rangle\langle u\vert{} + \vert{}d\rangle\langle d\vert{}) = \frac{1}{2} \left[ \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \right] = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix}$$


$$\rho \sigma_x = \begin{pmatrix} 0.5 & 0 \\ 0 & 0.5 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 0.5 \\ 0.5 & 0 \end{pmatrix}$$


Thus, the expectation value given by $\text{Tr}(\rho \sigma_x)$ is $0$ in this case as well.

### Schmidt Decomposition

Consider a pure bipartite state $\vert{}\psi\rangle$ in a composite tensor product Hilbert space $\mathcal{H}_A \otimes \mathcal{H}_B$ of dimensions $d_A \times d_B$, where we assume $d_A \leq d_B$.

By applying Singular Value Decomposition (SVD) to the coefficient matrix of the state, it is always possible to find complete orthonormal bases $\vert{}i_A\rangle$ for $\mathcal{H}_A$ and $\vert{}i_B\rangle$ for $\mathcal{H}_B$ such that the state can be written as a single sum of exactly $r$ terms (where $r \leq d_A$):

$$\vert{}\psi\rangle = \sum_{i=1}^r \sqrt{p_i} \vert{}i_A\rangle \otimes \vert{}i_B\rangle$$

Here, $r$ is the Schmidt rank, and the positive real numbers $\sqrt{p_i}$ are the Schmidt coefficients, and $\sum_{i=1}^r p_i = 1$.  

The individual vectors in the summation are perfectly paired in $A$ and $B$. If $i_A$ is paired with $i_B$, it will not appear with any other vector in the summation. Contrast this to a typical situation where we may see terms like $\vert{}10\rangle$ as well as $\vert{}11\rangle$ in a entangled state. Here $\vert{}1\rangle_A$ appears with both $\vert{}0\rangle_B$ and $\vert{}1\rangle_B$.

Tracing out either subsystem yields the reduced density matrices:

$$\rho_A = \sum_{i=1}^r p_i \vert{}i_A\rangle\langle i_A\vert{}, \quad \rho_B = \sum_{i=1}^r p_i \vert{}i_B\rangle\langle i_B\vert{}$$

The two subsystems share the exact same non-zero eigenvalues $p_i$, meaning their probability distributions match perfectly. We have mathematically decomposed the pure entangled state into a set of perfectly correlated mixed states in the local subsystems.

The probability distribution $p_i$ is called the **entanglement spectrum**. The Schmidt rank $r$ defines the entanglement class:
-   **$r = 1$:** Product state (completely separable, unentangled).
-   **$r > 1$:** Entangled state.
-   **$r = d_A$ and $p_i = 1/d_A$ for all $i$:** Maximally entangled state.
    
Note that the orthonormal bases $\vert{}i_A\rangle$ and $\vert{}i_B\rangle$ are specific to that particular entangled state $\vert{}\psi\rangle$ and do not constitute universal basis for decomposition of all states in the product space.

Schmidt decomposition allows us to build a direct correlation map between the subsystems. If an observer measures subsystem $A$ in the Schmidt basis $\vert{}i_A\rangle$ and obtains a specific eigenstate $\vert{}i_A\rangle$, the state of subsystem $B$ instantaneously collapses into the strictly correlated basis state $\vert{}i_B\rangle$. The probability of measuring $\vert{}i_A\rangle$ is exactly $p_i$. In this specific measurement basis, the outcomes act like a classical statistical ensemble in the sense, you will have perfectly correlated output readouts. A $+1$ measurement readout in $A$ means a $+1$ readout in $B$. Note that we could still have some probability of $+1$ and $-1$. We cannot say that we will always get $+1$, but we do know that the readouts will be synchronized in both subspaces.

However, this deterministic correlation is only guaranteed if the measurements are conducted within the specific Schmidt bases. If measurements are made in a different, rotated basis, it introduces standard quantum superposition and probability cross-terms. The subsystems remain entangled, meaning their expectation values and joint probability distributions over multiple measurements will still reflect quantum correlation, but individual paired readouts will generally no longer be $1:1$ identical (unless the specific entangled state possesses a continuous spatial symmetry, such as the spin-singlet state).

### Purification
Conversely to the Schmidt Decomposition, we have the concept of purification, which states that given a density matrix $\rho$ acting on a Hilbert space $\mathcal{H}_Q$, we can always find a pure state $\vert{}\psi\rangle$ in an enlarged Hilbert space $\mathcal{H}_Q \otimes \mathcal{H}_R$ such that the partial trace over the reference system $R$ yields the original state: $\text{Tr}_R(\vert{}\psi\rangle\langle\psi\vert{}) = \rho$. The dimension of the reference space $R$ must be greater than or equal to the rank of $\rho$. Essentially, any mixed state on a given system can be viewed as the reduced state of a pure, entangled state in a larger composite system.

A purification is never unique. If $\vert{}\phi_1\rangle$ is a valid purification of $\sigma$, you can generate an infinite number of alternative purifications by applying any unitary operator $U$ strictly to the ancillary system.

$$\vert{}\phi_2\rangle = (I_S \otimes U_A) \vert{}\phi_1\rangle$$

Because $U_A$ only rotates the unobservable environment, tracing it out yields the exact same principal state $\sigma$.

## Entanglement Examples
### Bell Inequalities & EPR Paradox

Einstein, Podolsky, and Rosen (EPR) formulated a thought experiment challenging the probabilistic nature of Quantum Physics. They claimed that quantum states do not represent inherent probability, but rather classical statistical ensembles. They argued that any complete physical theory must satisfy a condition known as Local Realism, which says physical properties exist independent of measurement (realism). If you measure a particle as having spin-up, it possessed a definite spin-up property prior to the measurement; we merely lacked the complete information (hidden variables) to predict it. A measurement performed in one location cannot instantaneously affect a simultaneous measurement performed elsewhere (no faster-than-light influence or non-localism).   

For example, EPR claimed that when we conduct a measurement on a Bell State and observe a $50\%$ chance of two spin-ups and a $50\%$ chance of two spin-downs, this actually indicates that there are particle pairs of two pre-existing types: half initialized as up-up and half as down-down. They argued we are dealing with a classical statistical mixture, represented by the density matrix $\rho = \frac{1}{2}\vert{}00\rangle\langle00\vert{} + \frac{1}{2}\vert{}11\rangle\langle11\vert{}$ or alternately as the probability vector $\frac{1}{2}\vert{}00\rangle + \frac{1}{2}\vert{}11\rangle$ , rather than a true quantum superposition. Similarly, if we make measurements along both the $Z$ and $X$ axes and see corresponding $25\%$ distributions, they would argue we simply have equal numbers of pairs belonging to four predetermined sets of two-qubit states.

However, Bell proved that this classical hidden-variable assumption leads to a strict mathematical limit that Quantum Mechanics violates. To see this, we measure the entangled system along 3 distinct axes.

Under local realism, each particle leaves the source with a predetermined spin (+ or -) for all three axes. This creates $2^3 = 8$ possible hidden-variable populations for the particles: $(+++), (++-), (+-+), (+--), (-++), (-+-), (--+),$ and $(---)$. Because the Bell state dictates that the two particles must always have the same spins when measured along the same axis, a particle 1 of type $(++-)$ strictly implies a particle 2 of type $(+--)$.

If we randomly choose to measure particle 1 along axis $A$ and particle 2 along axis $B$, Bell's logic dictates that the number of pairs where both yield spin-up, denoted $N(A+, B+)$, must satisfy classical set theory based on those 8 types. Because $N(A+, B+) = N(A+, B+, C+) + N(A+, B+, C-)$, we can derive the inequality:

$$N(A+, B+) + N(B+, C+) \geq N(A+, C+)$$

Dividing by the total number of pairs yields Bell's Inequality for probabilities:

$$P(A+, B+) + P(B+, C+) \geq P(A+, C+)$$

Next, let's figure out the probability of making a measurement of spin up on both systems when one measurement is along z and the other at an angle $\theta$ to z. Now, a spin measurement at an angle $\theta$ in the x-z plane corresponds to the operator $\cos\theta \, \sigma_z + \sin\theta \, \sigma_x$, which gives the expected matrix: 


$$\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}$$

To find the possible states post-measurement, we find the eigenvectors. The $\vert 1 \rangle$ part drops out because a 0 measurement on $A$ collapses the shared state strictly to $\vert 00\rangle$.

To find the eigenvector with eigenvalue $\lambda = +1$, we solve the characteristic matrix equation:

$$(M - \lambda I)v = 0$$

Where $M$ is the rotated Pauli matrix, $I$ is the identity matrix, and $v$ is the eigenvector $\begin{pmatrix} x \\ y \end{pmatrix}$.

Set up the matrix equation:  
 
 $$\begin{pmatrix} \cos\theta - 1 & \sin\theta \\ \sin\theta & -\cos\theta - 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$$
 
 
Solving the first row we get:
$$\sin\left(\frac{\theta}{2}\right)x = \cos\left(\frac{\theta}{2}\right)y$$

The simplest solution that balances this equation is setting $x = \cos(\frac{\theta}{2})$ and $y = \sin(\frac{\theta}{2})$.

Because $\cos^2(\frac{\theta}{2}) + \sin^2(\frac{\theta}{2}) = 1$, this vector is already perfectly normalized. Written in Dirac bra-ket notation, it yields the eigenvector:

$$\vert{}+\rangle_\theta = \cos\left(\frac{\theta}{2}\right)\vert{}0\rangle + \sin\left(\frac{\theta}{2}\right)\vert{}1\rangle$$

The probability of making a measurement of spin up is therefore $\cos^2\left(\frac{\theta}{2}\right)$.

Now back to the Bell inequalities, if we arrange axes $A$, $B$, and $C$ in a single plane separated by $60^\circ$ each (so the angle between $A$ and $C$ is $120^\circ$), quantum mechanics predicts:

$$P(A+, B+) = \sin^2(30^\circ) = 0.25$$

$$P(B+, C+) = \sin^2(30^\circ) = 0.25$$

$$P(A+, C+) = \sin^2(60^\circ) = 0.75$$

Substituting these quantum predictions into Bell's classical inequality yields:

$$0.25 + 0.25 \geq 0.75 \implies 0.5 \geq 0.75$$

This is a mathematical impossibility. Therefore, the Local Realism framework proposed by EPR (the 8 types of predetermined particles) cannot describe reality, as it physically contradicts the predictions of quantum mechanics.

## Continuous Wavefunctions
Unlike spin-1/2, which is defined in a 2-dimensional space, observables such as position have a continuous spectrum and can take an infinite number of values. Instead of using discrete eigenstates, eigenvalues, and summations, continuous observables are represented by continuous functions with a continuum of eigenstates and eigenvalues, and using integrals in place of summations in formulas. Probabilities are also replaced by probability densities.

For example, consider an arbitrary state vector $\vert{}\Psi\rangle$. If the observable is position $x$, the eigenbasis consists of the position kets $\vert{}x\rangle$, and the possible eigenvalues are infinite and span all real numbers. 

The wavefunction $\psi(x)$ represents the state $\vert{}\Psi\rangle$ in the position eigenbasis, representing the complex probability amplitude of measuring the particle at position $x$. Conceptually, $\psi(x)$ is analogous to the component of a state vector along a discrete eigenvector (like in spin), but instead of $N$ components as in the discrete situation, it has infinite components, and is therefore represented not by a column vector (which would have to be infinitely long) but as a "wave"-function of $x$. The complex probability amplitude, which in the discrete situation was given by the $c_1$, $c_2$... components of the state vector, is instead given by the wavefunction:

$$\psi(x) = \langle x\vert{}\Psi\rangle$$

This is the projection of the state vector $\vert{}\Psi\rangle$ onto the position eigenbasis $\vert{}x\rangle$. Because the eigenbasis is continuous, projecting the state vector yields a continuum of probability amplitudes as a function of $x$.

The probability density of a particle being found at position $x$ is given by the absolute square of the wavefunction: $\psi^*(x)\psi(x) = \vert{}\psi(x)\vert{}^2$. Because the total probability of finding the particle somewhere in space must be exactly $1$, the probability density function, when integrated from $-\infty$ to $+\infty$, must equal $1$:

$$\int_{-\infty}^{\infty} \vert{}\psi(x)\vert{}^2 dx = 1$$

This ensures the wavefunction is appropriately normalized.

The expectation value of position, $\langle x \rangle$, is the continuous analogue of the discrete weighted average:

$$\langle x \rangle = \int_{-\infty}^{\infty} x \vert{}\psi(x)\vert{}^2 dx = \int_{-\infty}^{\infty} \psi^*(x) x \psi(x) dx$$

In writing the expectation value, we have assumed that $x$ (and $p$ below) is an operator. This will be detailed in the next section.

Similarly, we can define a momentum wavefunction $\phi(p)$ that represents the state $\vert{}\Psi\rangle$ in the momentum eigenbasis $\vert{}p\rangle$. Here, $\phi(p) = \langle p\vert{}\Psi\rangle$ is the complex probability amplitude density of measuring the momentum value $p$.

The expectation value of momentum, $\langle p \rangle$, is:
$$\langle p \rangle = \int_{-\infty}^{\infty} \phi^*(p) p \phi(p) dp$$

The position wavefunction $\psi(x)$ and the momentum wavefunction $\phi(p)$ are related by the Fourier and inverse Fourier transforms. This relationship stems from the inner product between the position and momentum eigenstates (which will be proved in the next section on operators):

$$\langle x\vert{}p\rangle = \frac{1}{\sqrt{2\pi\hbar}} e^{ipx/\hbar}$$
$$\langle p\vert{}x\rangle = \frac{1}{\sqrt{2\pi\hbar}} e^{-ipx/\hbar}$$

We can derive $\phi(p)$ by inserting the completeness relation for position, $I = \int_{-\infty}^{\infty} \vert{}x\rangle\langle x\vert{} dx$, into the inner product:

$$\phi(p) = \langle p\vert{}\Psi\rangle = \int_{-\infty}^{\infty} \langle p\vert{}x\rangle\langle x\vert{}\Psi\rangle dx$$

Substituting $\langle p\vert{}x\rangle$ and $\psi(x) = \langle x\vert{}\Psi\rangle$ yields the formal Fourier transform:

$$\phi(p) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} e^{-ipx/\hbar} \psi(x) dx$$

Similarly, $\psi(x)$ can be recovered from $\phi(p)$ via the inverse Fourier transform by inserting the completeness relation for momentum and switching the sign of the complex exponent:

$$\psi(x) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} e^{ipx/\hbar} \phi(p) dp$$


### Position and Momentum Operators
Though position and momentum are continuous observables, they are represented by operators, denoted as $\hat{X}$ and $\hat{P}$. Just as operators in the discrete regime act on state vectors (whose components represent complex probability amplitudes), in the continuous regime, operators act directly on the wavefunction.

In their respective eigenbases, these operators act via simple scalar multiplication, because every $x$ is a eigenvalue of $\Psi$ with eigenvector (or rather eigenfunction) $\psi(x)$ and every $p$ is an eigenvalue with eigenfunction $\phi(p)$:

$\hat{X}\psi(x) = x\psi(x)$ and  $\hat{P}\phi(p) = p\phi(p)$

We can also represent the momentum operator $\hat{P}$ in the position basis $x$. To do this, we recognize that momentum is the physical quantity that generates linear movement. Therefore, momentum is the generator of spatial translation.

In quantum mechanics, symmetries and transformations are governed by Stone's Theorem. This theorem dictates that any continuous, unitary transformation $T(\epsilon)$ parameterized by a continuous real spatial variable $\epsilon$ is constructed by placing a Hermitian operator (the generator $\hat{P}$) into a complex exponential. To ensure dimensional consistency, we divide by $\hbar$:

$$T(\epsilon) = \exp\left(-\frac{i\epsilon}{\hbar}\hat{P}\right)$$

When we apply an active spatial translation by a distance $\epsilon$ to a state, the new wavefunction evaluated at position $x$ is equivalent to the old wavefunction evaluated at $x - \epsilon$. Thus:

$$T(\epsilon)\psi(x) = \psi(x - \epsilon)$$

Applying Taylor's theorem to expand the right side for an infinitesimally small $\epsilon$, and ignoring terms beyond the first order, we get:

$$\psi(x - \epsilon) = \psi(x) - \epsilon\frac{d}{dx}\psi(x)$$

Now, we expand the unitary operator $T(\epsilon)$ on the left side to first order:

$$T(\epsilon)\psi(x) = \left(I - \frac{i\epsilon}{\hbar}\hat{P}\right)\psi(x) = \psi(x) - \frac{i\epsilon}{\hbar}\hat{P}\psi(x)$$

Equating the two expansions gives:

$$\psi(x) - \epsilon\frac{d}{dx}\psi(x) = \psi(x) - \frac{i\epsilon}{\hbar}\hat{P}\psi(x)$$

Subtracting $\psi(x)$ from both sides and dividing by $-\epsilon$ leaves:

$$\frac{d}{dx}\psi(x) = \frac{i}{\hbar}\hat{P}\psi(x)$$

Solving for the operator $\hat{P}$ by multiplying both sides by $\frac{\hbar}{i}$ (which is equivalent to multiplying by $-i\hbar$) yields the momentum operator in the position basis:

$$\hat{P}\psi(x) = -i\hbar\frac{d}{dx}\psi(x)$$

$$\hat{P} = -i\hbar\frac{d}{dx}$$

Note that the derivative operator $\frac{d}{dx}$ by itself is anti-Hermitian. By multiplying it by the imaginary constant $-i$ (along with the real scalar $\hbar$), we ensure that $\hat{P}$ is strictly Hermitian, which is a mandatory requirement for any physical observable.

**Aside:** The momentum operator is a differential operator over $x$, which reflects its relation to symmetry via spatial translation. Similarly, the Hamiltonian is a differential operator over $t$, which reflects its relation to symmetry via time invariance.

We can use the momentum operator $\hat{P}$ to find the momentum eigenfunctions in the position basis, i.e., the wavefunctions of position $x$ that correspond to a state of definite momentum $p$. All we need to do is apply the $\hat{P}$ operator to a wavefunction for some specific $p$, and then integrate over the variable $x$, to get a wavefunction of $x$ for that specific $p$.

The eigenvalue equation for the momentum operator is:

$$\hat{P}\psi_p(x) = p\psi_p(x)$$

Substituting the position-basis representation of $\hat{P}$:

$$-i\hbar\frac{d}{dx}\psi_p(x) = p\psi_p(x)$$

Rearranging to solve the differential equation:

$$\frac{d}{dx}\psi_p(x) = \frac{ip}{\hbar}\psi_p(x)$$

The solution to this first-order differential equation is:

$$\psi_p(x) = A e^{ipx/\hbar}$$

Because this is a continuous plane wave extending over all space, the constant $A$ cannot be determined by standard probability normalization ($\int \vert{}\psi_p(x)\vert{}^2 dx = 1$), as the integral of a constant over the entire real line diverges to infinity. Instead, continuous eigenstates are normalized using the Dirac delta function, $\int \psi_p^*(x)\psi_{p'}(x) dx = \delta(p-p')$, which yields the normalization constant $A = \frac{1}{\sqrt{2\pi\hbar}}$.

Note that $\psi_p(x)$ is the same as $\langle x\vert{}p\rangle$. If you were to prepare an electron such that you know its momentum is exactly $p$, the quantum state of that electron is $\vert{}p\rangle$, if you then ask the question, "What is the probability amplitude of the detector triggering at coordinate $x$?", you project the state onto the position basis by evaluating $\langle x\vert{}p\rangle$.

The exact mathematical symmetric counterpart exists. It is the inner product $\langle p\vert{}x\rangle$ and therefore the complex conjugate of the above function.If you prepare a particle in a state of perfectly definite, exact position $x$ (the state $\vert{}x\rangle$), the wave function that describes its momentum distribution is:
$$\phi_x(p) = \langle p\vert{}x\rangle = \frac{1}{\sqrt{2\pi\hbar}}e^{\frac{-ipx}{\hbar}}$$

### The Uncertainty Principle
To evaluate the compatibility of position and momentum, we calculate the action of their commutator $[\hat{X}, \hat{P}]$ on an arbitrary test wavefunction $\psi(x)$:

$$[\hat{X}, \hat{P}]\psi(x) = (\hat{X}\hat{P} - \hat{P}\hat{X})\psi(x)$$
$$= x\left(-i\hbar\frac{d}{dx}\psi(x)\right) - \left(-i\hbar\frac{d}{dx}(x\psi(x))\right)$$

Applying the product rule to the second term:

$$= -i\hbar x \frac{d\psi(x)}{dx} + i\hbar \left(\psi(x) + x\frac{d\psi(x)}{dx}\right)$$
$$= -i\hbar x \frac{d\psi(x)}{dx} + i\hbar\psi(x) + i\hbar x\frac{d\psi(x)}{dx} = i\hbar\psi(x)$$

Because this holds for any $\psi(x)$, the operators satisfy the fundamental commutation relation:

$$[\hat{X}, \hat{P}] = i\hbar I$$

Therefore, $\hat{X}$ and $\hat{P}$ do not commute. Applying the generalized uncertainty principle relation, $\sigma_x \sigma_p \geq \frac{1}{2}\vert{}\langle[\hat{X}, \hat{P}]\rangle\vert{}$:

$$\Delta x \Delta p \geq \frac{1}{2} \vert{}\langle i\hbar \rangle\vert{} = \frac{\hbar}{2}$$

We can observe the physical consequence of this uncertainty principle by examining a state of exact, definite momentum $p$ in the position basis:

$$\psi_p(x) = \frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}$$

The probability density of finding the particle at any position $x$ is given by the absolute square of the wavefunction:

$$\vert{}\psi_p(x)\vert{}^2 = \psi_p^*(x)\psi_p(x) = \left(\frac{1}{\sqrt{2\pi\hbar}}e^{-ipx/\hbar}\right)\left(\frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}\right) = \frac{1}{2\pi\hbar}$$

This probability density is a constant, completely independent of $x$. This implies that if a particle has an exact momentum ($\Delta p = 0$), its position wavefunction is smeared uniformly across the entire real line, meaning its position is completely uncertain ($\Delta x = \infty$). It also means that the probability, which is an integral of the probability density over the entire real line, will be infinite, which is absurd. Such a state cannot physically exist in reality. It is strictly a mathematical idealization used as a building block.

**In short:** $\psi(x)$ and $\phi(p)$ are representations of the exact same quantum state $\vert{}\Psi\rangle$, just expressed in the position $x$ and momentum $p$ bases, respectively.
  
-   For any arbitrary state, you can convert between these two representations using the Fourier and inverse Fourier transform relations, which is nothing more than a change of coordinate basis.  

-   The time evolution of a state, as well as the system's energy eigenstates, depend entirely on the Hamiltonian. Given an initial state, the system's dynamics are found by solving the time-dependent Schrödinger equation using that specific Hamiltonian. Note that, for the initial state, you can mathematically prepare a particle in almost any initial shape you choose, provided it is square-integrable (so that it normalizes to exactly $1$) and satisfies the physical boundary conditions of the system.

You can write and work with the Hamiltonian operator in either the $x$ or $p$ representation. The equation $\hat{H}\psi(x) = E\psi(x)$ and the equation $\hat{H}\phi(p) = E\phi(p)$ are not two different physical laws. They are the exact same abstract, basis-independent physical law:
  
$$\hat{H}\vert{}\Psi\rangle = E\vert{}\Psi\rangle$$
The only difference is the mathematical machinery you use to solve them:
  
-   **In position space ($x$):** Because $\hat{P} = -i\hbar\frac{d}{dx}$, the Hamiltonian usually contains spatial derivatives. $\hat{H}\psi(x) = E\psi(x)$ becomes a differential equation.

-   **In momentum space ($p$):** Because $\hat{P} = p$, kinetic energy is just an algebraic multiplier, but the position operator $\hat{X} = i\hbar\frac{d}{dp}$ means any spatial potential $V(x)$ turns into a derivative or convolution. $\hat{H}\phi(p) = E\phi(p)$ becomes either an integral equation or a different differential equation.    
    
Both equations will yield the exact same physical energy eigenvalues $E$. If you solve for $\psi_E(x)$ and take its Fourier transform, you will get exactly $\phi_E(p)$. The physics is identical; only the coordinate axis has changed.


### Example: Solving the Hamiltonian for a Free Particle

For a free particle, the potential energy is zero, so the Hamiltonian consists strictly of kinetic energy:

$$\hat{H} = \frac{\hat{P}^2}{2m}$$

The time-dependent Schrödinger equation is:  

$$\hat{H}\Psi(x,t) = i\hbar\frac{\partial\Psi(x,t)}{\partial t}$$

Substituting the momentum operator in the position basis, $\hat{P} = -i\hbar\frac{\partial}{\partial x}$, we square it to find $\hat{P}^2 = -\hbar^2\frac{\partial^2}{\partial x^2}$. The equation becomes:
  
$$-\frac{\hbar^2}{2m}\frac{\partial^2\Psi(x,t)}{\partial x^2} = i\hbar\frac{\partial\Psi(x,t)}{\partial t}$$

A valid solution to this partial differential equation for a specific, definite momentum $p$ is a plane wave:
  
$$\Psi_p(x,t) = A e^{\frac{i}{\hbar}\left(px - \frac{p^2}{2m}t\right)}$$

where we replaced the energy eigenvalue $E$ with the classical relation $\frac{p^2}{2m}$.
  
Another way of solving this is to use the time-independent Schrödinger equation to find the spatial energy eigenstates first:
  
$$\hat{H}\psi(x) = E\psi(x)$$

$$-\frac{\hbar^2}{2m}\frac{d^2\psi(x)}{dx^2} = E\psi(x)$$

The solution to this ordinary differential equation for a definite momentum $p$ is:
  
$$\psi_p(x) = A e^{\frac{i}{\hbar}px}$$

where $E = \frac{p^2}{2m}$.
  
This is the probability amplitude density over $x$ for a particular $p$. Note that this represents a snapshot in time ($t=0$) and has no time dependence. To get the time-dependent equation, we multiply this spatial eigenstate by the standard time-evolution phase factor $e^{-iEt/\hbar}$:
  
$$\Psi_p(x,t) = \psi_p(x) e^{-i\frac{E}{\hbar}t} = A e^{\frac{i}{\hbar}\left(px - \frac{p^2}{2m}t\right)}$$

This is exactly the same as what we derived by solving for $t$ and $x$ simultaneously above.
  
This is the wavefunction over $x$ and $t$ for one particular exact momentum $p$. To get the general wavefunction (a physical wave packet), we integrate these eigenstates over all possible momentum eigenvalues $p$, weighted by the momentum-space probability amplitude $\phi(p)$:
  
$$\Psi(x,t) = \frac{1}{\sqrt{2\pi\hbar}} \int_{-\infty}^{\infty} \phi(p) e^{\frac{i}{\hbar}\left(px - \frac{p^2}{2m}t\right)} dp$$

The term $\frac{1}{\sqrt{2\pi\hbar}}$ is exactly the constant $A$ from the individual momentum eigenstate.

## Useful Formulas
From R Shankar's Book, Ch 01)

* **Inner Product Symmetry:** $\langle V \vert{} W \rangle = \langle W \vert{} V \rangle^*$
* **Linearity (Ket):** $\langle V \vert{} aW_1 + bW_2 \rangle = a\langle V \vert{} W_1 \rangle + b\langle V \vert{} W_2 \rangle$
* **Anti-linearity (Bra):** $\langle aV_1 + bV_2 \vert{} W \rangle = a^\*\langle V_1 \vert{} W \rangle + b^\*\langle V_2 \vert{} W \rangle$
* **Gram-Schmidt Orthogonalization:** Converts linearly independent vectors $\vert{}v_i\rangle$ into an orthonormal basis $\vert{}i\rangle$.
 $\vert{}1\rangle = \frac{\vert{}v_1\rangle}{\vert{}v_1\vert{}}$
 $\vert{}2'\rangle = \vert{}v_2\rangle - \vert{}1\rangle\langle 1 \vert{} v_2 \rangle$, then normalize: $\vert{}2\rangle = \frac{\vert{}2'\rangle}{\vert{}2'\vert{}}$
* **Matrix Elements:** $\Omega_{ij} = \langle i \vert{} \Omega \vert{} j \rangle$
* **Adjoint of a Product:** $(\Omega \Lambda)^\dagger = \Lambda^\dagger \Omega^\dagger$
* **Cyclic Property of Trace:** $\text{Tr}(\Omega\Lambda) = \text{Tr}(\Lambda\Omega)$
* **Basis Independence:** Both $\text{Tr}(\Omega)$ and $\det(\Omega)$ are invariant under a change of basis.
* **Anti-Hermitian Operator:** $\Omega^\dagger = -\Omega$
* **Unitary Operator ($U^\dagger U = U U^\dagger = I$):** Represents physical transformations.
Preserves the inner product (norm): $\langle U V \vert{} U W \rangle = \langle V \vert{} W \rangle$.
Eigenvalues are unimodular phase factors ($u_i = e^{i\theta}$).
Eigenvectors corresponding to distinct eigenvalues are orthogonal.
* **Commutator:** $[\Omega, \Lambda] = \Omega\Lambda - \Lambda\Omega$
* **Anti-commutator:** $\{\Omega, \Lambda\} = \Omega\Lambda + \Lambda\Omega$
* **Commutator Identities:**
* $[\Omega, \Lambda\Theta] = \Lambda[\Omega, \Theta] + [\Omega, \Lambda]\Theta$
* $[\Lambda\Omega, \Theta] = \Lambda[\Omega, \Theta] + [\Lambda, \Theta]\Omega$
* **Dirac Delta Function (Orthonormality):** $\langle x \vert{} x' \rangle = \delta(x-x')$
* **Completeness Relation (Continuous):** $\int \vert{}x\rangle\langle x\vert{} dx = I$
* **Inner Product of Functions:** $\langle f \vert{} g \rangle = \int f^*(x)g(x) dx$
* **Expansion of a Ket:** $\vert{}f\rangle = \int f(x)\vert{}x\rangle dx$, where $f(x) = \langle x \vert{} f \rangle$
* **Continuous Matrix Elements:** $\langle x \vert{} \Omega \vert{} x' \rangle = \Omega(x, x')$
* **Derivative of Delta Function:** $\int f(x)\delta'(x-a) dx = -f'(a)$ (Integrating by parts shifts the derivative to the function $f(x)$).

## References
- Quantum Mechanics: The Theoretical Minimum by Leonard Susskind
- [Quantum Physics 2, MIT 8.05 PLaylist](https://www.youtube.com/playlist?list=PLUl4u3cNGP60QlYNsy52fctVBOlk-4lYx)
- Mastering Quantum Mechanics by Barton Zwiebach
