## Qubits

A qubit (quantum bit) is a two-level quantum system that can exist in a superposition of two orthogonal basis states. These are conventionally defined in the $z$-basis as $\vert{}0\rangle$ (spin-up along the $z$-axis) and $\vert{}1\rangle$ (spin-down along the $z$-axis). One could also choose the $x$-basis, consisting of $\vert{}+\rangle$ (spin-up along $x$) and $\vert{}-\rangle$ (spin-down along $x$), but the $z$-basis (computational basis) is standard. 

Qubits can be physically implemented via various hardware, such as spin-1/2 particles or the horizontal and vertical polarization states of photons. While photons are spin-1 particles, their lack of a longitudinal polarization mode mathematically restricts their physical polarization space to two dimensions, making them isomorphic to a spin-1/2 system for computational purposes. For abstract ket operations, the hardware implementation is ignored.

The primary states encountered are $\vert{}0\rangle$, $\vert{}1\rangle$, $\vert{}+\rangle$, and $\vert{}-\rangle$. These are related by standard superposition principles. Unitary operators manipulate these states, with the Pauli matrices serving as fundamental single-qubit logic gates. 

## Gates

-   **Pauli X (NOT gate):** Flips the computational basis states: $\sigma_x\vert{}0\rangle = \vert{}1\rangle$ and $\sigma_x\vert{}1\rangle = \vert{}0\rangle$.

-   **Pauli Z (Phase gate):** Leaves $\vert{}0\rangle$ unchanged but applies a phase shift of $-1$ to $\vert{}1\rangle$: $\sigma_z\vert{}0\rangle = \vert{}0\rangle$ and $\sigma_z\vert{}1\rangle = -\vert{}1\rangle$.
    
-   **Hadamard (H gate):** Converts $\vert{}0\rangle$ to $\vert{}+\rangle$ and $\vert{}1\rangle$ to $\vert{}-\rangle$ and vice versa. Creates equal superpositions from the basis states. $H\vert{}0\rangle = \frac{1}{\sqrt{2}}(\vert{}0\rangle + \vert{}1\rangle) = \vert{}+\rangle$ and $H\vert{}1\rangle = \frac{1}{\sqrt{2}}(\vert{}0\rangle - \vert{}1\rangle) = \vert{}-\rangle$. This is essential for quantum parallelism and algorithms. It is represented by the matrix:


$$H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

- The general phase gate is defined by the matrix:

$$\begin{bmatrix} 1 & 0 \\ 0 & e^{i\theta} \end{bmatrix}$$


If we set $\theta = \pi$, we get a $-1$ in the bottom right and the phase gate becomes the Pauli $Z$ matrix. If we set $\theta = \pi/2$, we get what is known as the $S$ gate, with an $i$ in the bottom right.

- $HSH$ represents the square root of NOT gate (denoted $\sqrt{X}$), which squares to the Pauli $X$ NOT gate. Any matrix that squares to $X$ must contain complex entries. This is because the determinant of $X$ is $-1$; if a matrix with only real entries squared to $X$, its determinant squared would need to equal $-1$, which is mathematically impossible for real numbers.

- **SWAP gate:** In a two-qubit system, we can define the SWAP gate, which switches the two inputs with each other, i.e., $\vert{}\psi\phi\rangle$ becomes $\vert{}\phi\psi\rangle$. We can construct this gate using outer products (given by the $\vert{}\text{final}\rangle\langle\text{initial}\vert{}$ transition operator) and writing out the transition operators for each computational basis state combination.
$$\text{SWAP} = \vert{}00\rangle\langle00\vert{} + \vert{}10\rangle\langle01\vert{} + \vert{}01\rangle\langle10\vert{} + \vert{}11\rangle\langle11\vert{}$$

We can also construct the matrix for SWAP (and any other permutation operation) by remembering the following rule:

Write out the input basis states in the order of their integer index (decimal equivalent), so $\vert{}00\rangle$ becomes $0$, $\vert{}01\rangle$ becomes $1$, $\vert{}10\rangle$ becomes $2$, and $\vert{}11\rangle$ becomes $3$. Then find the output of each of these as they pass through the gate and write out their corresponding indices. In the case of SWAP, the outputs for inputs $(0, 1, 2, 3)$ become $\vert{}00\rangle \to 0$, $\vert{}10\rangle \to 2$, $\vert{}01\rangle \to 1$, and $\vert{}11\rangle \to 3$. The transformation matrix is constructed by arranging the column vectors of the $4 \times 4$ Identity matrix in this output order. For SWAP, the columns will be the 0th (first column), 2nd (third column), 1st (second column), and 3rd (fourth column) of the Identity. These columns are $4 \times 1$ vectors, reflecting the dimension of the $2 \otimes 2$ tensor product space.

- **Controlled-NOT or CNOT gate:** Takes two qubits as input: a target qubit (let's say $x$) and a control qubit (let's say $y$). It leaves the control qubit $\vert{}y\rangle$ unchanged, but transforms the target qubit $\vert{}x\rangle$ by XORing the two values. Mathematically, it maps the computational basis state $\vert{}x, y\rangle$ to $\vert{}x \oplus y, y\rangle$. Thus, if the control qubit $\vert{}y\rangle$ is in the state $\vert{}1\rangle$, the target qubit $\vert{}x\rangle$ is inverted (a Pauli $X$ operation is applied). Otherwise, if the control is $\vert{}0\rangle$, it is passed through unchanged.

- **The Toffoli Gate (CCNOT):** A three-qubit Controlled-Controlled-NOT gate. It applies a Pauli-X (NOT) operation to the third target qubit if and only if the first two control qubits are both in the $\vert{}1\rangle$ state. This is represented by $\vert{}c_1, c_2, t\rangle \rightarrow \vert{}c_1, c_2, t \oplus (c_1 c_2)\rangle$.
    
 The operator applies the identity matrix $I$ unless the control subspace is $\vert{}11\rangle$, in which case it applies $X$:
    
$$U_{\text{Toffoli}} = (\vert{}00\rangle\langle00\vert{} + \vert{}01\rangle\langle01\vert{} + \vert{}10\rangle\langle10\vert{}) \otimes I + \vert{}11\rangle\langle11\vert{} \otimes X$$
    
It is completely universal for classical reversible computation. Any classical boolean function (including standard AND and NAND gates) can be synthesized using only Toffoli gates.    

- **The Fredkin Gate (CSWAP)** A three-qubit Controlled-SWAP gate. It exchanges the states of the second and third target qubits if and only if the first control qubit is in the $\vert{}1\rangle$ state.
    
    $\vert{}0, x, y\rangle \rightarrow \vert{}0, x, y\rangle$
        
    $\vert{}1, x, y\rangle \rightarrow \vert{}1, y, x\rangle$
        
The operator applies the identity matrix to the targets if the control is $\vert{}0\rangle$, and applies the bipartite SWAP operator if the control is $\vert{}1\rangle$:
    
$$ U_{\text{Fredkin}} = \vert{}0\rangle\langle0\vert{} \otimes I \otimes I + \vert{}1\rangle\langle1\vert{} \otimes \text{SWAP} $$
    
It is also universal for classical reversible computation. Uniquely, the Fredkin gate strictly conserves the total number of $1$s (the Hamming weight) between the input and output states. This property makes it highly valuable for quantum error correction protocols and hardware routing architectures where particle conservation is required.

### Converting Between Standard Product States and Bell States
To convert a regular two-qubit product state like $\vert{}00\rangle$ into a Bell state and back again, apply a Hadamard gate to the first qubit followed by a CNOT gate with the first qubit as the control bit. Start with $\vert{}0\rangle \otimes \vert{}0\rangle$. Applyt H to the first qubit: $(H \otimes I)\vert{}00\rangle = \frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}10\rangle)$.  Apply CNOT with the first qubit as control and the second as target: $\text{CNOT} \left[\frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}10\rangle)\right] = \frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}11\rangle) = \vert{}\Phi^+\rangle$ (the Bell state). 

Similarly, to convert a Bell state into a two-qubit product state, apply the above gates in reverse order. Apply a CNOT with the first qubit as the control qubit, followed by a Hadamard on the second qubit. Start with the Bell state: $\vert{}\Phi^+\rangle = \frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}11\rangle)$. Apply CNOT (since CNOT is its own inverse, $\text{CNOT}^\dagger = \text{CNOT}$): $\text{CNOT} \left[\frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}11\rangle)\right] = \frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}10\rangle)$. Apply Hadamard (H) to the first qubit (since $H^\dagger = H$): $(H \otimes I) \left[\frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}10\rangle)\right] = \vert{}00\rangle$, returning to the original product state. 

$\vert{}00\rangle$ maps to $\frac{1}{\sqrt{2}}(\vert{}00\rangle + \vert{}11\rangle)$ or $\vert{}\Phi^+\rangle$.

$\vert{}01\rangle$ maps to $\frac{1}{\sqrt{2}}(\vert{}01\rangle + \vert{}10\rangle)$ or $\vert{}\Psi^+\rangle$.

$\vert{}10\rangle$ maps to $\frac{1}{\sqrt{2}}(\vert{}00\rangle - \vert{}11\rangle)$ or $\vert{}\Phi^-\rangle$.

$\vert{}11\rangle$ maps to $\frac{1}{\sqrt{2}}(\vert{}01\rangle - \vert{}10\rangle)$ or $\vert{}\Psi^-\rangle$.

---
Note that there is nothing different going in all these gates compared to what has already been seen. The gates, such as the Pauli matrices, simply act on the column vectors as unitary operators and create new column vectors via matrix multiplication. However, care must be taken regarding phase. For example, the $\sigma_x$ gate acts as a NOT gate in the $z$-basis, but in the $x$-basis, it does **not** function as a bit flip on $\vert{}+\rangle$ and $\vert{}-\rangle$. This is because these are its eigenvectors. However, since the eigenvalue of $\vert{}-\rangle$ is $-1$, $\sigma_x$ keeps \vert{}+\rangle$ unchanged but converts $\vert{}-\rangle$ to -$\vert{}-\rangle$.

If $\vert{}-\rangle$ exists in isolation, this minus sign is a global phase and can be mathematically dropped without altering observable physics. However, when it is part of a larger superposition (a relative phase), it governs quantum interference and must be rigorously tracked.  

For example, applying $\sigma_x$ to the superposition $\frac{1}{\sqrt{2}}(\vert{}+\rangle + \vert{}-\rangle)$ (which is $\vert{}0\rangle$) yields:

$$\sigma_x \left[ \frac{1}{\sqrt{2}}(\vert{}+\rangle + \vert{}-\rangle) \right] = \frac{1}{\sqrt{2}}(\vert{}+\rangle - \vert{}-\rangle)$$

This resulting state is exactly $\vert{}1\rangle$, maintaining logical consistency with the standard computational basis definition of a NOT gate.

## Teleportation & Quantum Communication

Many aspects such as quantum communication, quantum cryptography and quantum parallelism depend on entanglement. A two-qubit entangled state is called an e-bit. The idea of teleportation is to transmit a qubit from A to B by utilizing a pre-existing e-bit between the two, and by transmitting two classical bits. This way, we forego the fragile process of physically moving a qubit and instead utilize the more robust classical bit transmission to achieve the same thing.

Here is the classical text-based schematic of the teleportation circuit, designed to mirror the exact operations from your images.

Plaintext


                      Alice's Operations                         Bob's Corrections
                                                               
 α|0⟩+β|1⟩      ────────■───────[ H ]───────[ M ]═════════════════════════════════╗══
                        │                     ║                                   ║
                        │                     ║ (Classical bit 'b')               ║
 ┌─ |Φ⁺⟩_Alice  ────────⊕───────────────────[ M ]══════════╗══════════════════════╬══
 │                                            ║            ║                      ║
(Entangled)                                   ║ (Bit 'a')  ║                      ║
 │                                            ║            V                      V
 └─ |Φ⁺⟩_Bob    ──────────────────────────────╫──────────[ X ]──────────────────[ Z ]────── α|0⟩+β|1⟩



### Legend

-   `───` **Single Line:** A quantum wire carrying a coherent qubit.
    
      
    
-   `═══` **Double Line:** A classical wire carrying deterministic, measured classical bits ($0$ or $1$).
    
      
    
-   `■` / `⊕` **CNOT Gate:** Alice's unknown input acts as the control (`■`), entangling with her half of the Bell pair acting as the target (`⊕`).
    
      
    
-   `[ H ]` **Hadamard Gate:** Rotates the input qubit into the superposition basis before measurement to conceal the quantum amplitudes.
    
      
    
-   `[ M ]` **Measurement:** The physical detectors that collapse the quantum states and output classical bits.
    
      
    
-   `[ X ]` and `[ Z ]` **Conditional Pauli Gates:** Bob's hardware. The classical wires physically route to these gates, triggering them to fire only if the incoming classical bit is a $1$.
 
The circuit involves three qubits. The top wire is Alice's unknown input state. The middle wire is Alice's half of the entangled Bell pair, and the bottom wire is Bob's half.

Alice begins by interacting her unknown qubit with her half of the Bell pair using a CNOT gate, where her unknown state acts as the control. This operation effectively entangles the unknown state into the global system. If her unknown state has a $\vert{}1\rangle$ component, it flips the state of her Bell half, linking the amplitude information ($\alpha, \beta$) to the entangled pair.

Alice then applies a Hadamard gate to her original input qubit. This rotates the qubit into the superposition basis (X-basis). This step is crucial because it ensures that when Alice measures her qubits, she extracts no information about the actual values of $\alpha$ and $\beta$, preserving the quantum information so it can be transferred to Bob rather than destroyed by measurement.

Alice measures both of her qubits in the standard basis, yielding two classical bits (00, 01, 10, or 11). This measurement collapses the global state, instantly isolating Bob's distant qubit into a specific superposition that contains $\alpha$ and $\beta$. She then transmits these two classical bits to Bob via a standard communication channel. Note that the qubit has been destroyed and Alice no longer has it.

Bob receives the classical bits and uses them to apply specific Pauli gates to his qubit. As shown in the table, depending on the classical message, his state is off by a phase (requiring a Z gate), a bit-flip (requiring an X gate), both (ZX), or neither (Identity). Applying the correct sequence perfectly recovers Alice's original state.

To prove how this works, we can also calculate the state vector step-by-step. The global state is written in the order $\vert{}Bob\rangle \otimes \vert{}Alice_{Bell}\rangle \otimes \vert{}Alice_{input}\rangle$. The last digit is the control qubit for the CNOT.

**Step 0: Initial State ($\vert{}\pi_0\rangle$)**
The system begins as the tensor product of Alice's state and the shared Bell state:

$$\vert{}\pi_0\rangle = \vert{}\Phi^+\rangle \otimes (\alpha\vert{}0\rangle + \beta\vert{}1\rangle)$$

Expanding this out yields the four terms shown in the first step:

$$\vert{}\pi_0\rangle = \frac{\alpha\vert{}000\rangle + \alpha\vert{}110\rangle + \beta\vert{}001\rangle + \beta\vert{}111\rangle}{\sqrt{2}}$$

**Step 1: Applying the CNOT ($\vert{}\pi_1\rangle$)**

Alice applies a CNOT controlled by the last qubit (her input) targeting the middle qubit (her Bell half).

-   Terms ending in $0$ are unchanged: $\alpha\vert{}000\rangle$ and $\alpha\vert{}110\rangle$ remain the same.
    
-   Terms ending in $1$ flip the middle bit: $\beta\vert{}001\rangle \rightarrow \beta\vert{}011\rangle$ and $\beta\vert{}111\rangle \rightarrow \beta\vert{}101\rangle$.
    
    $$\vert{}\pi_1\rangle = \frac{\alpha\vert{}000\rangle + \alpha\vert{}110\rangle + \beta\vert{}011\rangle + \beta\vert{}101\rangle}{\sqrt{2}}$$
    

**Step 2: Applying the Hadamard ($\vert{}\pi_2\rangle$)**

Alice applies a Hadamard to the last qubit. This maps $\vert{}0\rangle \rightarrow \vert{}+\rangle$ and $\vert{}1\rangle \rightarrow \vert{}-\rangle$:

$$\vert{}\pi_2\rangle = \frac{\alpha\vert{}00\rangle\vert{}+\rangle + \alpha\vert{}11\rangle\vert{}+\rangle + \beta\vert{}01\rangle\vert{}-\rangle + \beta\vert{}10\rangle\vert{}-\rangle}{\sqrt{2}}$$

**Step 3: Expansion and Regrouping**

To see what happens when Alice measures, we must expand the $\vert{}+\rangle$ and $\vert{}-\rangle$ states and regroup the entire expression based on the states of Alice's two qubits (the last two digits). Following the expansion shown in the detailed calculation:

Substitute $\vert{}+\rangle = \frac{\vert{}0\rangle + \vert{}1\rangle}{\sqrt{2}}$ and $\vert{}-\rangle = \frac{\vert{}0\rangle - \vert{}1\rangle}{\sqrt{2}}$:

$$= \frac{\alpha\vert{}00\rangle(\vert{}0\rangle+\vert{}1\rangle) + \alpha\vert{}11\rangle(\vert{}0\rangle+\vert{}1\rangle) + \beta\vert{}01\rangle(\vert{}0\rangle-\vert{}1\rangle) + \beta\vert{}10\rangle(\vert{}0\rangle-\vert{}1\rangle)}{2}$$

Distribute the terms out fully to get eight basis states:

$$= \frac{\alpha\vert{}000\rangle + \alpha\vert{}001\rangle + \alpha\vert{}110\rangle + \alpha\vert{}111\rangle + \beta\vert{}010\rangle - \beta\vert{}011\rangle + \beta\vert{}100\rangle - \beta\vert{}101\rangle}{2}$$

Now, factor out the four possible measurement outcomes for Alice's qubits (the last two digits: $00$, $01$, $10$, $11$) to isolate Bob's qubit (the first digit):

$$\vert{}\pi_2\rangle = \frac{1}{2}(\alpha\vert{}0\rangle + \beta\vert{}1\rangle)\vert{}00\rangle + \frac{1}{2}(\alpha\vert{}0\rangle - \beta\vert{}1\rangle)\vert{}01\rangle + \frac{1}{2}(\alpha\vert{}1\rangle + \beta\vert{}0\rangle)\vert{}10\rangle + \frac{1}{2}(\alpha\vert{}1\rangle - \beta\vert{}0\rangle)\vert{}11\rangle$$

**Step 4: Measurement Collapse**

Because the global state is now grouped by Alice's possible measurement outcomes, we can clearly read the resulting state of Bob's qubit. When Alice measures, the state collapses into one of the four branches with a probability of $(\frac{1}{2})^2 = \frac{1}{4}$.

As detailed in the final table:

-   If Alice measures $00$, Bob's state is $\alpha\vert{}0\rangle + \beta\vert{}1\rangle$. He does nothing (applies Identity).
    
-   If Alice measures $01$, Bob's state is $\alpha\vert{}0\rangle - \beta\vert{}1\rangle$. He applies a Pauli-Z to fix the phase.
    
-   If Alice measures $10$, Bob's state is $\alpha\vert{}1\rangle + \beta\vert{}0\rangle$. He applies a Pauli-X to flip the bits.
    
-   If Alice measures $11$, Bob's state is $\alpha\vert{}1\rangle - \beta\vert{}0\rangle$. He applies both Z and X (ZX).

## Density Matrices Redux

We can write a qubit state using a density matrix to accommodate both pure states and the mixed states that arise in multi-qubit tensor product spaces (via partial tracing). Any $2 \times 2$ density matrix can be written as a linear combination of the Identity matrix and the Pauli matrices:

$$\rho = \frac{1}{2}(I + \vec{n} \cdot \vec{\sigma})$$

where $\vec{\sigma}$ is the formal vector of Pauli matrices $(\sigma_x, \sigma_y, \sigma_z)$ and $\vec{n} = (n_x, n_y, n_z)$ is a spatial vector of norm utmost $1$, called the Bloch vector.

To see why this is true, a valid density matrix must have a trace of $1$. The Pauli matrices are traceless ($\text{Tr}(\sigma_i) = 0$), and the $2 \times 2$ Identity matrix has a trace of $2$. Therefore, the coefficient $\frac{1}{2}$ on $I$ guarantees that $\text{Tr}(\rho) = 1$, while the traceless Pauli vector accounts for the system's specific quantum state.

Expanding the dot product $\vec{n} \cdot \vec{\sigma}$ into a matrix yields:

$$\rho = \frac{1}{2} \left[ \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} n_z & n_x - in_y \\ n_x + in_y & -n_z \end{pmatrix} \right] = \frac{1}{2} \begin{pmatrix} 1 + n_z & n_x - in_y \\ n_x + in_y & 1 - n_z \end{pmatrix}$$

The determinant of this density matrix is:

$$\det(\rho) = \frac{1}{4} \left[ (1 + n_z)(1 - n_z) - (n_x - in_y)(n_x + in_y) \right]$$

$$\det(\rho) = \frac{1}{4} (1 - n_z^2 - n_x^2 - n_y^2) = \frac{1}{4}(1 - \vert{}\vec{n}\vert{}^2)$$

Because a physical density matrix must be positive semi-definite, its determinant must be greater than or equal to zero ($\det(\rho) \geq 0$). This mathematically constrains the vector $\vec{n}$ to have a norm $\vert{}\vec{n}\vert{} \leq 1$. The set of all valid vectors $\vec{n}$ forms a solid 3D sphere known as the Bloch ball. Pure states ($\vert{}\vec{n}\vert{} = 1$, $\det(\rho) = 0$) live on the surface (the Bloch sphere), while mixed states ($\vert{}\vec{n}\vert{} < 1$) reside in the interior.

The points on the surface are the extreme points or extremums. Any interior point (mixed state) in the Bloch ball can be written as a linear convex combination of two extreme points. What's more, there are infinite such combinations for any such point. To see why, note that any point in the ball can be connected to any point on the sphere's surface via a line. If we extend that line back to meet the surface again (sort of like the antipode but not quite), we have a line between two extremums on which the point lives. There are infinite such lines. Thus, a mixed state density matrix can be decomposed into pure states in an infinite number of ways:

$$\rho = \lambda \rho_1 + (1-\lambda) \rho_2$$

Every mixed state in the Bloch ball (except the maximally mixed state at the exact center) has a unique representation as a convex combination of antipodal points. This is because, for any non-central point, there is exactly one line passing through both that point and the center of the sphere. Therefore, there is only one pair of antipodal points (representing orthonormal states) that can form this combination. Representing a mixed state as a combination of antipodes provides a clear idea of just how mixed it actually is (its purity). A general representation via an arbitrary chord could be misleading because there are infinite chords for which the mixed point is the midpoint. However, a point can only be the midpoint of an _antipodal_ chord (a diameter) if it is exactly at the center, meaning it is the maximally mixed state.

**Aside:** Any pure state on the surface of the Bloch sphere can be parameterized in spherical polar coordinates. If $\theta$ is the polar angle with the $Z$-axis representing the north pole, and $\phi$ is the azimuthal angle from the $X$-axis, then the state is given by the density matrix:

Given a spin state characterized by the Bloch vector $\vec{n}$, the expectation value of an observable measured along an arbitrary spatial unit vector $\hat{p}$ is $\hat{p} \cdot \vec{n}$.

We can prove this in the following way. The observable for spin along $\hat{p}$ is represented by the operator $\hat{p} \cdot \vec{\sigma}$. The expectation value is given by the trace formula:

$$\langle \hat{p} \cdot \vec{\sigma} \rangle = \text{Tr}(\rho (\hat{p} \cdot \vec{\sigma}))$$

Substituting the density matrix definition:

$$\langle \hat{p} \cdot \vec{\sigma} \rangle = \text{Tr} \left( \frac{1}{2}(I + \vec{n} \cdot \vec{\sigma})(\hat{p} \cdot \vec{\sigma}) \right)$$

$$= \frac{1}{2} \text{Tr}(\hat{p} \cdot \vec{\sigma}) + \frac{1}{2} \text{Tr}((\vec{n} \cdot \vec{\sigma})(\hat{p} \cdot \vec{\sigma}))$$

Because the Pauli matrices are traceless, the first term vanishes ($\text{Tr}(\hat{p} \cdot \vec{\sigma}) = 0$). For the second term, we apply the standard Pauli vector identity $(\vec{a} \cdot \vec{\sigma})(\vec{b} \cdot \vec{\sigma}) = (\vec{a} \cdot \vec{b})I + i(\vec{a} \times \vec{b}) \cdot \vec{\sigma}$:

$$\text{Tr}((\vec{n} \cdot \vec{\sigma})(\hat{p} \cdot \vec{\sigma})) = \text{Tr}((\vec{n} \cdot \hat{p})I + i(\vec{n} \times \hat{p}) \cdot \vec{\sigma})$$

The trace is a linear operator. The trace of the cross-product term is zero because it is a linear combination of Pauli matrices. The trace of $(\vec{n} \cdot \hat{p})I$ is $2(\vec{n} \cdot \hat{p})$. Therefore:

$$\langle \hat{p} \cdot \vec{\sigma} \rangle = \frac{1}{2} \left[ 2(\vec{n} \cdot \hat{p}) \right] = \vec{n} \cdot \hat{p}$$

This geometric proof implies that to fully determine an unknown $\vec{n}$ (and therefore reconstruct $\rho$), one must perform expectation value measurements along three mutually orthogonal spatial axes (e.g., $x, y, z$). Why do we need three measurements? Because a $2 \times 2$ Hermitian density matrix is characterized by exactly 4 real parameters (two for the diagonal elements, and the real/imaginary parts of the off-diagonal elements). The normalization constraint $\text{Tr}(\rho) = 1$ removes one degree of freedom, leaving exactly 3 independent parameters that must be determined via measurement.

### Purity & Entanglement Are Independent Properties
Purity and entanglement are independent properties. You can have a pure entangled state (the Bell states, for example). You can have pure unentangled states ($\vert{}00\rangle$, for example). You could have a statistical mixture of entangled states ($\frac{1}{2}\vert{}\Phi^+\rangle\langle\Phi^+\vert{} + \frac{1}{2}\vert{}\Phi^-\rangle\langle\Phi^-\vert{}$), a mixture of unentangled states ($\frac{1}{2}\vert{}11\rangle\langle11\vert{} + \frac{1}{2}\vert{}00\rangle\langle00\vert{}$), or a mixture containing both entangled and unentangled states ($\frac{1}{2}\vert{}\Phi^+\rangle\langle\Phi^+\vert{} + \frac{1}{2}\vert{}00\rangle\langle00\vert{}$).

The density matrix of a pure entangled state will be idempotent since it is a pure state (i.e., $\rho^2 = \rho$), which means it can be written as an outer product of a single state vector. If we were to diagonalize this density matrix, it would have a single $1$ on the diagonal, and every other element would be $0$. The reduced density matrices, however, will be mixed states and therefore not idempotent. If we were to diagonalize each of them, there would be multiple non-zero elements on the diagonal. The Schmidt rank will be strictly greater than $1$, and we can write the bipartite state vector as the sum of at least two product states of orthogonal vectors in the respective subspaces.

However, simply because the full density matrix is idempotent does not mean the state is entangled. It only means the state is pure (i.e., it can be written as a single state vector). It may not be entangled at all, for example: $\vert{}00\rangle$. The reduced density matrices here will also be idempotent, representing pure states. The Schmidt decomposition will have a rank of $1$, which means we can factor out a single state vector from each subspace such that the bipartite space is exactly their tensor product.

If we find that the density matrix of the 2-qubit state is not idempotent, it means it is a mixed state. A mixed state represents a classical statistical ensemble. Because it cannot be represented by a single state vector, you cannot perform a Schmidt decomposition on this density matrix. The classical ensemble does not necessarily imply entanglement; it may include entangled states, non-entangled states, or both. 

For a globally mixed state, the reduced density matrices are generally mixed, but they can occasionally be pure (idempotent) if one subsystem is completely uncorrelated and locally pure while the classical uncertainty is entirely confined to the other subsystem. For eg. if we take the pure $\rho_A = \vert{}0\rangle\langle0\vert{}$ and the mixed $\rho_B = \frac{1}{2}\vert{}0\rangle\langle0\vert{} + \frac{1}{2}\vert{}1\rangle\langle1\vert{}$, and create a bipartite state from their tensor product, and then evaluate the combined density matrix to see if it is idempotent:

$$\rho_{AB}^2 = (\rho_A \otimes \rho_B)^2 = \rho_A^2 \otimes \rho_B^2$$

Since $B$ is mixed, this is obviously not equal to $\rho_{AB}$.

An easy way take the reduced density matrix of $A$ in $A \otimes B$ i.e. if we want to trace out $B$, is: $\rho_A = Tr(B) A$ and $\rho_B = Tr(A) B$, i.e. multiply the matrix to retain by the trace of the other matrix. For eg. given 

$$\rho =\left (\frac{1}{2}\vert{}0\rangle\langle0\vert{} \otimes \vert{}0\rangle\langle0\vert{} + \frac{1}{2}\vert{}1\rangle\langle1\vert{} \otimes \vert{}+\rangle\langle+\vert{} \right)$$

To get $\rho_A$, we must trace out $B$, i.e. both $\vert{}0\rangle\langle0\vert$ and $\vert{}+\rangle\langle+\vert$. Taking the trace of an outer product is the same as calculating the inner product, which is $1$ for both of these. Thus, we have:
$$\rho_A = \frac{1}{2}\vert{}0\rangle\langle0\vert{} + \frac{1}{2}\vert{}1\rangle\langle1\vert{}$$

Similarly, 
$$\rho_B = \frac{1}{2}\vert{}0\rangle\langle0\vert{} + \frac{1}{2}\vert{}+\rangle\langle+\vert{}$$

## Closed vs Open Systems

Quantum systems that are closed are ideal situations where there is no interference from external factors. They can be modeled as state vectors, and their evolution can be modeled via unitary operators acting upon them. However, in reality, quantum systems are open to effects from the environment. When we model open systems, we use density matrices, and their evolution is modeled through quantum channels. This modeling rests on the fact that although a quantum system may be open, the quantum system in combination with the environment is considered a closed system.

## Quantum Channels

Quantum channels are linear completely positive trace-preserving (CPTP) maps of a density matrix to a density matrix; i.e., they are more general than just a map of states to states -- they map a system to another system. For example, suppose a qubit that is in a superposition of states passes through a channel. The channel may be noisy, in the sense that it interacts with the environment such that all information about the nature of the superposition and coherence of the qubit is lost. By the time the qubit arrives at the channel output, it will be a completely mixed state—a classical ensemble.

Usually, as in the above case, the output system is the same as the input system. But channels can just as well map an input system to another output system. For example, in the above case, the environment might have entangled one of its qubits with the input qubit. The output system we would then be interested in would be the input qubit combined with the one qubit from the environment.

Inputs and outputs to quantum channels are represented not by state vectors (which are useful only in closed systems), but by density matrices. Moreover, the input system and the environment's initial state are considered to form a product state initially; i.e., they have no correlation and are completely decoupled to start with. 

The channel itself is modeled as a unitary operation on the entire closed system of the system of interest combined with the environment. The environment (or whatever part of the environment we do not care about) is then traced out of the output of this unitary operation, which leaves us with the reduced output system. 

There are three primary mathematical representations that can be used to model this process.

### Stinespring Dilation

This method builds out the channel, its inputs, the environment, and the output almost exactly as just described. If $\rho_s$ is the input density matrix, $\vert{}e_0\rangle$ the initialized state of the environment, $\{\vert{}e_k\rangle\}$ the basis vectors of the environment, and $U$ the unitary operation on the entire closed system, then the initial state of the joint system is given by the tensor product $\rho_s \otimes \vert{}e_0\rangle\langle e_0\vert{}$.

The full output of the unitary operation is given by $U (\rho_s \otimes \vert{}e_0\rangle\langle e_0\vert{}) U^\dagger$.

Now, to trace out the environment, we evaluate the expectation value of the full output with respect to the environment's basis vectors $\{\vert{}e_k\rangle\}$ and sum over them. This partial trace over the environment yields the output density matrix $\rho_o$:

$$\rho_o = \sum_k \langle e_k \vert{} U (\rho_s \otimes \vert{}e_0\rangle\langle e_0\vert{}) U^\dagger \vert{} e_k \rangle$$

Note that writing the bras and kets of the environment directly adjacent to the joint unitary operation is a shorthand. The full mathematical expression using explicit tensor products across the bipartite Hilbert space applies the identity operator $I_s$ to the principal system while projecting the environment:

$$\rho_o = \sum_k (I_s \otimes \langle e_k \vert{}) \left[ U (\rho_s \otimes \vert{}e_0\rangle\langle e_0\vert{}) U^\dagger \right] (I_s \otimes \vert{} e_k \rangle)$$

**Aside:** To see more clearly how the partial trace is being taken, assume that the full output of the unitary operation can be written as a separable term $A_s \otimes B_e$. We can then write the final partial trace step as:

$$\sum_k(I_s \otimes \langle e_k \vert{}) (A \otimes B) (I_s \otimes \vert{} e_k \rangle)$$

$$= \sum_k(I_s A I_s) \cdot (\langle e_k \vert{} B \vert{} e_k \rangle)$$

$$= A \cdot\sum_k \langle e_k \vert{} B \vert{} e_k \rangle$$

The environment component $\sum_k(\langle e_k \vert{} B \vert{} e_k \rangle)$ is the trace of $B$ and evaluates to a simple scalar value, leaving only the operator $A$ acting on the system space. This explicitly defines the partial trace.

### Kraus Operators

From the Stinespring Dilation, if we define the operators $E_k = (I_s \otimes \langle e_k \vert{}) U (I_s \otimes \vert{} e_0 \rangle)$, then their Hermitian adjoints are $E_k^\dagger = (I_s \otimes \langle e_0\vert{}) U^\dagger (I_s \otimes \vert{} e_k \rangle)$. These represent the effective operators acting on the principal system for each measurement outcome $k$ of the environment.

We can therefore write the final reduced system state as:

$$\rho_o = \sum_k E_k \rho_s E_k^\dagger$$

However, we must ensure that $\rho_o$ is a valid density matrix, meaning its trace must equal $1$. Thus, $\text{tr}(\sum_k E_k \rho_s E_k^\dagger) = 1$. By using the linearity of the trace and its cyclic property ($\text{tr}(ABC) = \text{tr}(CAB)$), we can rearrange the terms inside the trace:

$$\sum_k \text{tr}(E_k \rho_s E_k^\dagger) = \sum_k \text{tr}(E_k^\dagger E_k \rho_s) = \text{tr}\left(\left(\sum_k E_k^\dagger E_k\right) \rho_s\right) = 1$$

Because this equation must hold true for _any_ valid input density matrix $\rho_s$, the operator sum multiplying $\rho_s$ must be the identity matrix. This gives us the completeness relation:  

$$\sum_k E_k^\dagger E_k = I$$

The operators $E_k$ are the Kraus operators, and this formulation is the Kraus representation for quantum channels. Note that Kraus operators themselves need not be Hermitian, unitary, or positive-definite.

Moreover, to analyze individual outcomes, we can normalize each term in the summation by dividing it by its trace (which represents the probability of that outcome):

$$\rho_o = \sum_k \text{tr}(E_k \rho_s E_k^\dagger) \cdot \frac{E_k \rho_s E_k^\dagger}{\text{tr}(E_k \rho_s E_k^\dagger)}$$

The fraction $\frac{E_k \rho_s E_k^\dagger}{\text{tr}(E_k \rho_s E_k^\dagger)}$ is a valid, trace-1 density matrix, which we can call $\rho_k$. It represents the post-measurement state of the system if outcome $k$ occurs. If we define the probability of this outcome as $P_k = \text{tr}(E_k \rho_s E_k^\dagger)$, then the overall channel output is clearly a convex sum of these conditional density matrices weighted by their classical probabilities:

$$\rho_o = \sum_k P_k \rho_k$$

### Measurement as an Operator Formalism Example

It is not a coincidence that this maps to the conditions placed on quantum measurements. Measurements can be modeled as quantum channels. Suppose we have a system qubit that we want to measure without completely destroying it. We take an ancillary qubit from the environment, entangle it with the system qubit via a CNOT gate, and then trace out (or measure) the environment qubit.

Entangling the system and environment qubits via a CNOT gate sets the system qubit as the control and the environment qubit as the target. If the environment is initialized in the state $\vert{}0\rangle$, a system qubit in state $\vert{}0\rangle$ leaves the environment unchanged, while a system qubit in state $\vert{}1\rangle$ flips the environment to $\vert{}1\rangle$. The environment qubit thus perfectly correlates with the system qubit in the computational basis, acting as a proxy that we can trace out.

We can write this out in the Stinespring representation. Let the initial system state be a superposition $\vert{}\psi\rangle = \alpha\vert{}0\rangle + \beta\vert{}1\rangle$. Its density matrix $\rho_s$ is:

$$\rho_s = \vert{}\alpha\vert{}^2\vert{}0\rangle\langle0\vert{} + \alpha\beta^\*\vert{}0\rangle\langle1\vert{} + \alpha^*\beta\vert{}1\rangle\langle0\vert{} + \vert{}\beta\vert{}^2\vert{}1\rangle\langle1\vert{}$$

The combined initial state of the joint system is $\rho_s \otimes \vert{}0\rangle\langle0\vert{}_e$.

The unitary CNOT operation $U$ cannot be written via its truth table as:

$$U = \vert{}00\rangle\langle00\vert{} + \vert{}01\rangle\langle01\vert{} + \vert{}10\rangle\langle11\vert{} + \vert{}11\rangle\langle10\vert{}$$

Applying the unitary evolution to the joint initial state $U (\rho_s \otimes \vert{}0\rangle\langle0\vert{}_e) U^\dagger$ yields the entangled density matrix:  

$$\rho_{total} = \vert{}\alpha\vert{}^2\vert{}00\rangle\langle00\vert{} + \alpha\beta^\*\vert{}00\rangle\langle11\vert{} + \alpha^\*\beta\vert{}11\rangle\langle00\vert{} + \vert{}\beta\vert{}^2\vert{}11\rangle\langle11\vert{}$$

To find the output state of the system $\rho_o$, we trace out the environment:

$$\rho_o = (I_s \otimes \langle 0 \vert{}) \rho_{total} (I_s \otimes \vert{} 0 \rangle) + (I_s \otimes \langle 1 \vert{}) \rho_{total} (I_s \otimes \vert{} 1 \rangle)$$

Evaluating these partial inner products annihilates the off-diagonal cross-terms, leaving:

$$\rho_o = \vert{}\alpha\vert{}^2\vert{}0\rangle\langle0\vert{}_s + \vert{}\beta\vert{}^2\vert{}1\rangle\langle1\vert{}_s$$

We can arrive at this same result directly using Kraus operators. For $E_0$:

$$E_0 = (I_s \otimes \langle 0 \vert{}_e) U (I_s \otimes \vert{} 0 \rangle_e)$$

Since $U$ applied to $\vert{}0\rangle_e$ yields $\vert{}0\rangle_s\langle0\vert{}_s \otimes \vert{}0\rangle_e + \vert{}1\rangle_s\langle1\vert{}_s \otimes \vert{}1\rangle_e$, applying the bra $\langle 0\vert{}_e$ isolates the $\vert{}0\rangle_s$ component:  

$$E_0 = \vert{}0\rangle\langle0\vert{}_s$$

Similarly for $E_1$:

$$E_1 = (I_s \otimes \langle 1 \vert{}_e) U (I_s \otimes \vert{} 0 \rangle_e) = \vert{}1\rangle\langle1\vert{}_s$$

Applying these Kraus operators to $\rho_s$ yields $\rho_o = E_0\rho_sE_0^\dagger + E_1\rho_sE_1^\dagger$, which evaluates exactly to $\vert{}\alpha\vert{}^2\vert{}0\rangle\langle0\vert{}_s + \vert{}\beta\vert{}^2\vert{}1\rangle\langle1\vert{}_s$.

### Choi Representation

The Choi representation is mathematically isomorphic to the Kraus and Stinespring representations. In essence, it maps a quantum channel to a single bipartite state by passing half of a maximally entangled state through the channel. This serves as a static matrix representation of the channel's action on all possible input states.  

To construct the Choi matrix, we first define an unnormalized, maximally entangled state across two identical $d$-dimensional Hilbert spaces:

$$\vert{}\Phi\rangle = \sum_{i=1}^d \vert{}i\rangle \otimes \vert{}i\rangle$$

We then apply the channel transformation $T$ exclusively to the first subsystem, while applying the identity operation $I$ to the second subsystem.

Because a general quantum channel $T$ might involve noise, decoherence, or measurement, the output is not guaranteed to remain a pure state. It is mathematically evaluated as a density matrix, known as the Choi matrix:  

$$\rho_{\text{Choi}} = (T \otimes I) (\vert{}\Phi\rangle\langle\Phi\vert{})$$

The outer product of the initial state $\vert{}\Phi\rangle$ expands to:

$$\vert{}\Phi\rangle\langle\Phi\vert{} = \sum_{i=1}^d \sum_{j=1}^d (\vert{}i\rangle\langle j\vert{}_A) \otimes (\vert{}i\rangle\langle j\vert{}_B)$$

Applying $T \otimes I$ to this expansion yields the explicit formula for the Choi matrix:

$$\rho_{\text{Choi}} = \sum_{i=1}^d \sum_{j=1}^d T(\vert{}i\rangle\langle j\vert{}_A) \otimes \vert{}i\rangle\langle j\vert{}_B$$

The resulting $\rho_{\text{Choi}}$ is a $d^2 \times d^2$ matrix.  

For the completely dephasing measurement channel discussed previously ($d=2$), the channel acts by annihilating off-diagonal coherence terms. Its action on the standard basis operators is:

-   $T(\vert{}0\rangle\langle0\vert{}) = \vert{}0\rangle\langle0\vert{}$
    
-   $T(\vert{}1\rangle\langle1\vert{}) = \vert{}1\rangle\langle1\vert{}$
    
-   $T(\vert{}0\rangle\langle1\vert{}) = 0$
    
-   $T(\vert{}1\rangle\langle0\vert{}) = 0$
    
Using the unnormalized $2$-qubit state $\vert{}\Phi\rangle = \vert{}00\rangle + \vert{}11\rangle$, the input matrix is:

$$\vert{}\Phi\rangle\langle\Phi\vert{} = \vert{}00\rangle\langle00\vert{} + \vert{}00\rangle\langle11\vert{} + \vert{}11\rangle\langle00\vert{} + \vert{}11\rangle\langle11\vert{}$$

Applying $T \otimes I$ maps each basis term as follows:

-   $T(\vert{}0\rangle\langle0\vert{}) \otimes \vert{}0\rangle\langle0\vert{} = \vert{}00\rangle\langle00\vert{}$
    
-   $T(\vert{}0\rangle\langle1\vert{}) \otimes \vert{}0\rangle\langle1\vert{} = 0$
    
-   $T(\vert{}1\rangle\langle0\vert{}) \otimes \vert{}1\rangle\langle0\vert{} = 0$
    
-   $T(\vert{}1\rangle\langle1\vert{}) \otimes \vert{}1\rangle\langle1\vert{} = \vert{}11\rangle\langle11\vert{}$

Summing the non-zero terms yields the final Choi matrix for the dephasing channel:

$$\rho_{\text{Choi}} = \vert{}00\rangle\langle00\vert{} + \vert{}11\rangle\langle11\vert{}$$

Notice that the initial pure entangled state has been reduced to a separable, classical mixed state.

### What Drives Environmental Interference

Having seen how measurement can be modelled as a quantum channel, we can use this framework to intuitively understand how the environment decoheres a quantum system. Environmental interference occurs when the environment builds a correlation with the principal system's states, effectively becoming entangled with them. 

Let $\{\vert{}e_k\rangle\}$ represent the states in the environment that become entangled with the system's orthonormal basis states. If the environment is to perfectly distinguish the system's orthonormal basis states, then the environment states $\vert{}e_k\rangle$ corresponding to system basis states must themselves be orthogonal. This means the environment has essentially performed a projective measurement on the system. In this limit of maximal entanglement with the environment, the quantum coherence between the system's basis states is completely destroyed. The quantum information leaks into the correlations with the environment, effectively destroying the "integrity" of the channel, and the reduced state of the system becomes a purely classical statistical mixture or ensemble.

Based on this, we can also define the Kraus rank as the minimum number of Kraus operators required in any valid Kraus representation of that channel. A Kraus rank of $1$ indicates that the channel can be described by a single Kraus operator (which must be a unitary matrix to satisfy the completeness relation). Physically, this means the principal system and the environment remain completely separable (unentangled) throughout the interaction. The environment does not acquire any information about the system, representing an ideal closed-system unitary evolution.

If the Kraus rank is equal to the dimension of the principal system $d$, it represents processes like complete dephasing (which requires $d$ operators, such as the orthogonal projectors of the measurement basis). However, this is not the maximum possible decoherence. Maximum decoherence, such as the completely depolarizing channel, which maps any input state to the maximally mixed state $I/d$, requires a Kraus rank of $d^2$. The value $d^2$ is the absolute upper bound on the Kraus rank for any quantum channel acting on a $d$-dimensional Hilbert space.

### Writing out Unitary Operators in Basis Terms
A unitary operation can be described in terms of basis states by writing out the truth table in terms of the sum of $\vert{}finalstate\rangle\langle initialstate\vert$ fir all initial states. For any computational basis state $\vert{}x\rangle$, if a classical truth table dictates that the gate maps $\vert{}x\rangle \to \vert{}f(x)\rangle$, the quantum operator is mathematically constructed as $\sum_x \vert{}f(x)\rangle\langle x\vert{}$.

For eg. the NOT operator can be written as $\vert{}0\rangle\langle1\vert{} + \vert{}1\rangle\langle0\vert{}$, which is just the Pauli X matrix. 

As another eg. the CNOT operator with the first bit as the control can be written as:

$$U_{\text{CNOT}} = \vert{}00\rangle\langle00\vert{} + \vert{}01\rangle\langle01\vert{} + \vert{}11\rangle\langle10\vert{} + \vert{}10\rangle\langle11\vert{}$$

Note that if we know that the target bit is in an initial state of $\vert{}0\rangle$, we _cannot_ simply remove the terms above that are relevant to a target bit of $\vert{}1\rangle$. The unitary operator's matrix representation must remain completely independent of the data being routed through it. To restrict the operation based on known initialization parameters, the input density matrix or state vector is modified, never the channel representation itself.

### Channels & the Bloch Ball
When a density matrix $\rho$ of a single qubit is represented in the Bloch Ball as $1/2(I + \sigma \cdot r)$, the length of the Bloch radial vector for $\rho^2$ is $1/2(1+|r|^2)$. Thus, the length remains $1$ only if it was already $1$ for $\rho$ itself i.e. it was a pure state. For every mixed state, the radius will remain less than 1. 

The Bloch Ball geometry can be helpful in getting an intuitive idea of what happens to a qubit when it passes through a channel. In general, for any channel, if r is the radial vector of channel input and r' is the radial vector of channel output, then the affine transformation $r' = M \cdot r + c$ holds true, where $M = O \cdot S$, with $S$ a symmetric matrix representing a symmetric compression/expansion of the ball, $O$ a rotation of the radial vector, and $c$ a complex constant displacement of the ball's center. 

**Symmetric compression/expansion:** When the center remains fixed ($\vec{c} = 0$) but the sphere contracts asymmetrically, the channel is unital. The environment is not exchanging energy with the system or biasing it toward a specific energetic ground state. If the sphere preserves its full radius strictly along one axis (for example, the $z$-axis) while contracting along the others ($x$ and $y$), it models a process where specific classical information is immune to the noise. States containing superposition (which rely on the $x$ and $y$ axes for relative phase) have their off-diagonal density matrix elements suppressed. The states do not collapse to a specific pure state. Instead, they collapse inward toward the preserved axis. A pure state like $\vert{}+\rangle$ on the $x$-axis will shrink directly toward the origin, eventually becoming the maximally mixed state $I/2$. It loses its quantum coherence (phase) but retains its underlying 50/50 classical probability distribution. This is the behaviour of a dephasing channel (described below).

**Rotation:** Pure decoherence or damping channels typically align with the coordinate axes. However, if the system-environment interaction Hamiltonian contains terms that do not commute with the system's internal Hamiltonian or the noise generator, the channel imparts an effective over-rotation or phase precession.

**Center shift:** The center of the ball does not shift for channels like bit flip or phase flip (described below), which typically represent pure noise. The environment measures or randomizes the system, but it has no directional bias. A shifting center physically represents an asymmetric energy exchange or thermal relaxation between the qubit and its environment, such as in amplitude damping channels. The environment acts as an energetic sink or a thermal bath with a preferred equilibrium state. It actively absorbs energy from (or pumps energy into) the qubit, pulling the state away from the center and toward that environmental equilibrium, regardless of the qubit's initial configuration.

If the ball is moving upwards, for eg. it starts at the South pole or the excited state $\vert{}1\rangle$ and moves towards the center, it is losing energy to the environment. If the qubit is moving downwards, for eg. from the ground state $\vert{}0\rangle$, it is absorbing energy from the environment. Thus, channels like amplitude damping result in the ball moving towards the North Pole.

**Ball contraction:** If the ball contracts symmetrically, all 3 coordinates axes are decay at the exact same rate towards the origin or the maximally mixed state. This represents total information loss or randomization. 

In quantum statistical mechanics, the thermal equilibrium state of a qubit interacting with a heat bath at temperature $T$ is governed by the Boltzmann distribution. The temperature $T$ dictates the ratio of populations between the ground and excited states. A zero-temperature bath ($T = 0$) absorbs all energy, driving the system to $\vert{}0\rangle$ (a shifted sphere). An infinite-temperature bath ($T \to \infty$) injects massive thermal noise, completely overpowering the energy gap between $\vert{}0\rangle$ and $\vert{}1\rangle$. The populations equalize at 50/50.

A symmetric contraction (called the depolarizing channel) is the exact mathematical model for a qubit submerged in a thermal bath at infinite temperature. The environment is so chaotic that it completely scrambles the qubit's orientation, destroying both its quantum coherence (the $x$ and $y$ axes) and its classical bit value (the $z$ axis) uniformly.

### Types of Channels
**Bit Flip ($\Delta$):** This is represented by the Pauli $X$ or NOT gate:


$$X = \begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$$


It flips $\vert{}0\rangle$ to $\vert{}1\rangle$ and vice versa. It leaves the $\vert{}+\rangle$ state unaffected and changes $\vert{}-\rangle$ to $-\vert{}-\rangle$ because these are the eigenstates of $X$ with eigenvalues $1$ and $-1$ respectively. However, because this $-1$ is a global phase, the density matrix for $\vert{}-\rangle$ remains completely unaffected ($\vert{}-\rangle\langle-\vert{} \to \vert{}-\rangle\langle-\vert{}$). 

Consider a channel where $p$ is the probability of a bit flip occurring. A noisy quantum channel represents a classical statistical mixture of events, not a coherent superposition. Therefore, the channel is modeled using the Kraus operators $K_0 = \sqrt{1-p}I$ and $K_1 = \sqrt{p}X$. Given an input density matrix $\rho$, the output density matrix is:

$$\Delta(\rho) = K_0 \rho K_0^\dagger + K_1 \rho K_1^\dagger$$

$$\Delta(\rho) = (1-p)\rho + p X \rho X$$

To analyze the effect on the Bloch ball, we can express the input density matrix using its Bloch vector $\vec{r} = (r_x, r_y, r_z)$:

$$\rho = \frac{1}{2}(I + r_x X + r_y Y + r_z Z)$$

Applying the bit-flip channel and using the anti-commutation relations of the Pauli matrices ($XYX = -Y$ and $XZX = -Z$, as well as the fact that all Pauli matrices square to Identity), the $X \rho X$ term becomes:

$$X \rho X = \frac{1}{2}(I + r_x X - r_y Y - r_z Z)$$

Substituting this back into the channel equation yields the final output state:

$$\Delta(\rho) = \frac{1}{2} \left[ I + r_x X + (1-2p)r_y Y + (1-2p)r_z Z \right]$$

The Bloch ball contracts towards the $x$-axis. Geometrically, the sphere deforms into a prolate ellipsoid (cigar-shaped) with the $x$-axis remaining as the major axis of length 1. Since the $x$-axis is unaffected, the output will tend to randomize and lose information along the $y$ and $z$ axes, but preserve information perfectly along the $x$-axis.

**Phase Flip ($\Lambda$):** This is represented by the Pauli $Z$ matrix:


$$Z = \begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$$


It changes $\vert{}1\rangle$ to $-\vert{}1\rangle$ and leaves $\vert{}0\rangle$ unchanged, once again because these are the eigenstates of $Z$ with eigenvalues $-1$ and $1$, respectively.

Consider a channel where $p$ is the probability of a phase flip occurring. The channel is modeled using the Kraus operators $K_0 = \sqrt{1-p}I$ and $K_1 = \sqrt{p}Z$. Given an input density matrix $\rho$, the output density matrix is:

$$\Lambda(\rho) = (1-p)\rho + p Z \rho Z$$

To analyze the effect on the Bloch ball, the $Z \rho Z$ term becomes:

$$Z \rho Z = \frac{1}{2}(I - r_x X - r_y Y + r_z Z)$$

Substituting this back into the channel equation yields the final output state:

$$\Lambda(\rho) = \frac{1}{2} \left[ I + (1-2p)r_x X + (1-2p)r_y Y + r_z Z \right]$$

The Bloch ball contracts towards the $z$-axis. This represents a phase-damping or dephasing channel. If $p = 1/2$, the factor $(1-2p)$ becomes $0$. This specific case is the completely dephasing channel, which entirely removes all cross terms in the density matrix, destroying quantum coherence and creating a classical statistical ensemble.

When completely dephased, a superposition $\vert{}\psi\rangle = \alpha\vert{}0\rangle + \beta\vert{}1\rangle$, initially represented by the density matrix:


$$\begin{bmatrix} \vert{}\alpha\vert{}^2 & \alpha\beta^* \\ \alpha^*\beta & \vert{}\beta\vert{}^2 \end{bmatrix}$$


becomes the diagonal matrix:


$$\begin{bmatrix} \vert{}\alpha\vert{}^2 & 0 \\ 0 & \vert{}\beta\vert{}^2 \end{bmatrix}$$


This aligns precisely with what occurs when a projective measurement is made along the $z$-axis; the off-diagonal coherence is lost, and the system collapses into a classical distribution of $\vert{}0\rangle$ and $\vert{}1\rangle$ with probabilities $\vert{}\alpha\vert{}^2$ and $\vert{}\beta\vert{}^2$, respectively.

The Choi representation of this channel is given by:

$$J(\Delta) = \sum_{a,b=0}^{1} \vert{}a\rangle\langle b\vert{} \otimes \Delta(\vert{}a\rangle\langle b\vert{})$$

Because the completely dephasing channel annihilates the off-diagonal coherence terms ($\Delta(\vert{}0\rangle\langle1\vert{}) = 0$ and $\Delta(\vert{}1\rangle\langle0\vert{}) = 0$) while preserving the diagonals, the summation simplifies to:

$$J(\Delta) = \vert{}0\rangle\langle 0\vert{} \otimes \vert{}0\rangle\langle 0\vert{} + \vert{}1\rangle\langle 1\vert{} \otimes \vert{}1\rangle\langle 1\vert{}$$

As a block matrix, the tensor product expansion is written as:


$$J(\Delta) = \begin{pmatrix} \Delta\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} & \Delta\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \\ \Delta\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} & \Delta\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 \end{pmatrix}$$


**Depolarizing Channel:** This channel contracts the input state towards the completely mixed state. Consider a channel where $p$ is the probability of replacing the input state with the maximally mixed state $I/2$. The state of the system after passing through this channel is:

$$\Gamma(\rho) = \frac{p}{2}I + (1-p)\rho$$

Using the operator identity $\rho + X\rho X + Y\rho Y + Z\rho Z = 2I$ and substituting this for $2I$ (meaning $I/2 = \frac{1}{4}(\rho + X\rho X + Y\rho Y + Z\rho Z)$) into the previous equation gives us:

$$\Gamma(\rho) = \left(1-\frac{3p}{4}\right)\rho + \frac{p}{4}(X\rho X + Y\rho Y + Z\rho Z)$$

This means we have the following Kraus operators:

$K_0 = \sqrt{1-\frac{3p}{4}}I, \quad K_1 = \frac{\sqrt{p}}{2}X, \quad K_2 = \frac{\sqrt{p}}{2}Y, \quad K_3 = \frac{\sqrt{p}}{2}Z$

We could have also parameterized the depolarizing channel in terms of discrete Pauli errors:

$$\Gamma(\rho) = (1-p)\rho + \frac{p}{3}(X \rho X + Y\rho Y + Z\rho Z)$$

In this parameterization, the channel applies one of the three Pauli errors symmetrically (each with probability $p/3$). Because the Pauli operations anti-commute, applying them with equal probability isotropically contracts the Bloch vector in all three spatial directions, drawing it directly toward the center point (the maximally mixed state). Note that the probability $p$ here and the probability $p$ in the previous parametrization are not equal; if $p_1$ is the probability of replacement with the mixed state and $p_2$ is the probability of a Pauli error, they are related by $p_1 = \frac{4}{3}p_2$.

The Choi representation of this channel is given by:

$$\begin{aligned} J(\Omega) &= \sum_{a,b=0}^{1} \vert{}a\rangle\langle b\vert{} \otimes \Omega(\vert{}a\rangle\langle b\vert{}) \\ &= \vert{}0\rangle\langle 0\vert{} \otimes \frac{\mathbb{1}}{2} + \vert{}1\rangle\langle 1\vert{} \otimes \frac{\mathbb{1}}{2} \\ &= \frac{1}{2} \mathbb{1} \otimes \mathbb{1} \end{aligned}$$


As a block matrix:

$$J(\Omega) = \begin{pmatrix} \Omega\begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix} & \Omega\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix} \\ \Omega\begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix} & \Omega\begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix} \end{pmatrix} = \begin{pmatrix} \frac{1}{2} & 0 & 0 & 0 \\ 0 & \frac{1}{2} & 0 & 0 \\ 0 & 0 & \frac{1}{2} & 0 \\ 0 & 0 & 0 & \frac{1}{2} \end{pmatrix}$$


**Aside:** You can also write the channel's Bloch ball parametrization in the falling way:

$$\mathcal{E}(\rho) = p\frac{I}{2} + (1-p)\left[\frac{1}{2}(I + \vec{r} \cdot \vec{\sigma})\right]$$$$\mathcal{E}(\rho) = \frac{1}{2}\left(I + (1-p)\vec{r} \cdot \vec{\sigma}\right)$$

## Trace Distance & Fidelity

Having some means to measure how similar two systems are, for example, how close the output of a channel is to the input, is essential in quantum information theory. The main mechanism for this is assessing how well two systems can be distinguished by measurement. In essence, the distance between two systems corresponds to the best possible distinction one could make if given complete freedom to choose any set of measurement operators (POVMs).

For classical probability distributions $P$ and $Q$ over the same index set, distinguishing between them utilizes probabilities $p_i$ and $q_i$. The classical trace distance is given by:

$$D(P, Q)=\frac{1}{2}\sum_i\vert{}p_i-q_i\vert{}$$

The division by two is a sort of normalizing factor that turns $D$ into a metric. For eg. in the worst case distance, for eg. where $p = (1,0)$ and $q=(0,1)$, $D = 1$ thanks to the division by 2. 

The classical fidelity measures similarity rather than distance, given by:

$$F(P, Q)=\sum_i\sqrt{p_i q_i}$$

For quantum pure states $\vert{}\phi\rangle$ and $\vert{}\psi\rangle$, the distance and similarity metrics are evaluated using the trace norm and inner product. Note that  the below definitions are analogous to the above, keeping in mind that the components of the state vectors are the probability amplitudes or the square roots of probabilities $p_i, q_i$:

$$D(\vert{}\phi\rangle, \vert{}\psi\rangle)=  \sqrt{1-\vert{}\langle\phi\vert{}\psi\rangle\vert{}^2}$$

$$F(\vert{}\phi\rangle, \vert{}\psi\rangle)=\vert{}\langle\phi\vert{}\psi\rangle\vert{} = \sum_i\sqrt {p_iq_i}$$

Extending these to quantum mixed states represented by density matrices $\rho$ and $\sigma$, the trace distance and fidelity are formulated as:

$$D(\rho, \sigma)=\frac{1}{2}\text{Tr}\vert{}\rho-\sigma\vert{}$$

$$F(\rho, \sigma)=\text{Tr}\left(\sqrt{\sqrt{\rho}\sigma\sqrt{\rho}}\right)$$

When $[\rho, \sigma] = 0$ i.e. they commute, the two matrices share the exact same eigenbasis and they can be simultaneously diagonalized. Because they commute, $\rho^{1/2}$ and $\sigma$ also commute. We can rearrange the matrix product and the fidelity simplifies to :

$$F(\rho, \sigma) = \text{Tr}\left(\sqrt{\rho \sigma}\right)$$

Why is this formula valid only when the two matrices commute? If $\rho$ and $\sigma$ do not commute, their product $\rho \sigma$ is generally not a Hermitian matrix. If a matrix is not Hermitian and positive semi-definite, it does not have a standard principal square root. You cannot mathematically take $\sqrt{\rho \sigma}$ because the resulting eigenvalues could be complex or undefined.

Physically, two quantum states commute if and only if they are classical probability distributions masquerading as density matrices. If they share an eigenbasis, there is no quantum superposition or relative phase difference between them. The trace evaluates strictly to the sum of the square roots of their multiplied probabilities ($F = \sum \sqrt{p_i q_i}$), which is known in classical statistics as the Bhattacharyya coefficient.

Note that the absolute value of an operator $A$ is defined as $\vert{}A\vert{}=\sqrt{A^\dagger A}$, and to find the square root of a matrix, we can find the spectral decomposition of the matrix. The square root of the matrix can be found by taking the square roots of the eigenvalues while retaining the same eigenvectors.

There is a simple formula for the fidelity between a mixed and a pure state. We can write,

$$\sqrt{\sigma}\rho\sqrt{\sigma} = (\vert{}\psi\rangle\langle\psi\vert{}) \rho (\vert{}\psi\rangle\langle\psi\vert{})$$

Pulling the scalar expectation value out and taking the square root, and noting that any projection operator is idempotent i.e. it is its own square, we have,

$$\sqrt{\sqrt{\sigma}\rho\sqrt{\sigma}} = \sqrt{\langle\psi\vert{}\rho\vert{}\psi\rangle} \vert{}\psi\rangle\langle\psi\vert{}$$

$$F(\vert{}\psi\rangle, \rho) = \sqrt{\langle\psi\vert{}\rho\vert{}\psi\rangle} \; \text{Tr}(\vert{}\psi\rangle\langle\psi\vert{})$$

Since $\text{Tr}(\vert{}\psi\rangle\langle\psi\vert{}) = \langle\psi\vert{}\psi\rangle = 1$, we have, 

$$F(\vert{}\psi\rangle, \rho) = \sqrt{\langle\psi\vert{}\rho\vert{}\psi\rangle}$$

For single-qubit states, trace distance can be written in terms of their Bloch vectors $\vec{r}_\rho$ and $\vec{r}_\sigma$ as:

$$D(\rho, \sigma)=\frac{1}{2}\vert{}\vec{r}_\rho-\vec{r}_\sigma\vert{}$$

As two systems tend towards similarity, trace distance decreases while fidelity increases. For pure states, their relationship is exactly $F=\sqrt{1-D^2}$, analogous to $cos \theta = \sqrt{1-sin^2 \theta}$. For general mixed states, this becomes an inequality bound (the Fuchs-van de Graaf inequalities): $1-F\leq D\leq\sqrt{1-F^2}$.

When comparing pure states and mixed states it is possible to make a stronger statement than (9.110) about the relationship between trace distance and fidelity. Prove that

$$1 - F(\vert{}\psi\rangle, \sigma)^2 \leq D(\vert{}\psi\rangle, \sigma).$$

In keeping with the statement above that the distance between two systems corresponds to the best possible distinction one can make between them via POVMs, we can also write

$$D(\rho, \sigma) = \max_{\{E_m\}} D(p_m, q_m)$$
$$F(\rho, \sigma) = \min_{\{E_m\}} F(p_m, q_m),$$

where the maximum and minimum is over all POVMs $\{E_m\}$, and $p_m \equiv \text{tr}(\rho E_m)$, $q_m \equiv \text{tr}(\sigma E_m)$ are the probability distributions for $\rho$ and $\sigma$ corresponding to the POVM $\{E_m\}$. This represents the optimal measurement strategy that provides the best possible statistical distinction between the two quantum states.

Note that given two system, their trace distance cannot increase, and their fidelity cannot decrease after they pass through a system i.e. a channel will always make two systems similar. This is called contractivity of trace distance and monotonicity of fidelity.

$$D(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \le D(\rho, \sigma)$$

$$F(\mathcal{E}(\rho), \mathcal{E}(\sigma)) \ge F(\rho, \sigma)$$

### Uhlmann's Theorem
Uhlmann's theorem states that for any two density matrices $\rho$ and $\sigma$ acting on a system Hilbert space $\mathcal{H}_S$, the fidelity between them is equal to the maximum overlap (inner product) between their purifications in an extended composite Hilbert space $\mathcal{H}_S \otimes \mathcal{H}_R$.

$$F(\rho, \sigma) = \max_{\vert{}\phi\rangle, \vert{}\psi\rangle} \vert{}\langle\psi\vert{}\phi\rangle\vert{}$$

However, since purifications of a state are not unique and are related by unitary transformations, the process of iterating over say, all psi, involves applying unitary transformations to it, which could just as well be absorbed into the process of iterating over phi. Instead, we can fix an arbitrary purification $\vert{}\psi\rangle$ for $\rho$. The theorem is then stated as a maximization over all possible purifications $\vert{}\phi\rangle$ of $\sigma$:

$$F(\rho, \sigma) = \max_{\vert{}\phi\rangle} \vert{}\langle\psi\vert{}\phi\rangle\vert{}$$

Equivalently, if we start with fixed arbitrary purifications $\vert{}\psi\rangle$ of $\rho$ and $\vert{}\phi\rangle$ of $\sigma$, the maximization is over all unitary operators $U$ acting only on the reference space $R$:

$$F(\rho, \sigma) = \max_{U} \vert{}\langle\psi\vert{} (I \otimes U) \vert{}\phi\rangle\vert{}$$

### Convexity of Trace Distance
Trace distance is a convex function. Mathematically, for any classical probability distribution $p_i$ and sets of density matrices $\rho_i$ and $\sigma_i$, the trace distance satisfies the following inequality:

$$D\left(\sum_i p_i \rho_i, \sum_i p_i \sigma_i\right) \le \sum_i p_i D(\rho_i, \sigma_i)$$

The left side evaluates the distinguishability of two statistical mixtures. The right side evaluates the weighted average of their individual distinguishabilities.

The inequality proves that mixing states always shrinks the maximum distinguishability. If a system is subject to classical noise or random variations (meaning you do not know the exact index $i$), the resulting mixed states are forced closer together. Ignorance acts as a blur, making it physically harder to tell the two ensembles apart than if you knew exactly which state $i$ was prepared.

Similarly for fidelity, it is concave, and we have,

$$F\left(\sum_i p_i \rho_i, \sum_i p_i \sigma_i\right) \ge \sum_i p_i F(\rho_i, \sigma_i)$$

### Examples

A phase-flip (dephasing) channel that applies a $Z$ gate with probability $p$ alters a Bloch vector $(r_x, r_y, r_z)$ to $((1-2p)r_x, (1-2p)r_y, r_z)$. The trace distance between input and output is $p\sqrt{r_x^2+r_y^2}$. Similarly, a bit-flip channel applying an $X$ gate with probability $p$ results in a trace distance between input and output of $p\sqrt{r_y^2+r_z^2}$.

This relates to the notion of fixed points—states in the Bloch ball where the channel's input and output are identical. Different channels possess different fixed points. For example, the dephasing channel's fixed points are any states on the $z$-axis, represented by the Bloch vector set $\{(0, 0, r_z)\}$. The bit-flip channel's fixed points are any states on the $x$-axis, given by $\{(r_x, 0, 0)\}$.

## Quantum Error Correction
### Discretization of Quantum Errors

Classical bits are discrete; a bit is either 0 or 1. Qubits, however, can exist in a superposition of states. Geometrically, on the Bloch sphere, a qubit can lie at any point on the surface, not just the North and South poles.

For example, utilizing the polar angle $\theta$ and azimuthal angle $\phi$, a generic single-qubit pure state is written as the superposition:

$$\vert{}\psi\rangle = \cos(\theta/2)\vert{}0\rangle + e^{i\phi}\sin(\theta/2)\vert{}1\rangle$$

An error on a qubit can conceptually involve a continuum of deviations in $\theta$ and $\phi$. However, because quantum mechanics is linear, any error operation (whether a unitary evolution or a general completely positive trace-preserving map) acting on a single qubit can be expanded in the basis of the $2 \times 2$ Pauli matrices: $I$, $X$, $Y$, and $Z$. Since $Y = iXZ$ (ignoring global phase factors), an error $E$ is often expressed in terms of the operators $I$, $X$, $Z$, and their product $XZ$:

$$E = \alpha_I I + \alpha_X X + \alpha_Z Z + \alpha_{XZ} XZ$$

If the error operation is unitary ($E^\dagger E = I$), the complex coefficients satisfy $\sum \vert{}\alpha_i\vert{}^2 = 1$. When this error operation acts on a state $\vert{}\psi\rangle$, the output is a superposition of the discrete Pauli errors acting on the state:

$$E\vert{}\psi\rangle = \alpha_I\vert{}\psi\rangle + \alpha_X X\vert{}\psi\rangle + \alpha_Z Z\vert{}\psi\rangle + \alpha_{XZ} XZ\vert{}\psi\rangle$$

This mathematical structure means that discretizing quantum errors is possible. If we perform an appropriate measurement, the superposition collapses into exactly one of these four branches. We then only need to correct for one of a finite set of discrete errors (an $X$ error, a $Z$ error, or both, i.e., $XZ$). The challenge is that measuring the data qubit directly collapses its quantum state, destroying the encoded computational information.

To resolve this, we do not measure the data directly. Instead, we encode the information of a single abstract "logical qubit" into a highly entangled state of multiple "physical qubits" (e.g., using a repetition code or Shor code). We then entangle these physical data qubits with additional auxiliary qubits, known as "ancilla qubits." By measuring only the ancilla qubits, we can extract the error syndrome, information about which error occurred, without disturbing the superposition of the logical qubit.

For instance, a quantum repetition code relies on parity checks that function similarly to a majority vote. A 3-qubit repetition code can detect and correct an error on a single physical qubit. An 11-qubit repetition code can correct errors on up to 5 qubits.

Measurements of the ancilla qubits yield a syndrome that indicates whether an $X$, $Z$, or $XZ$ error occurred and on which physical qubit. Once the specific error is identified, we apply a recovery operation. Because Pauli operators are Hermitian and unitary, they are their own inverses ($P^2 = I$). If the syndrome indicates an $X$ error occurred on a specific physical qubit, applying the $X$ operator to that same qubit reverses the error: $XX\vert{}\psi\rangle = \vert{}\psi\rangle$.

### Correcting for a Bit Flip in a 3-bit code
Note that qubits can undergo discrete errors, primarily represented by the Pauli matrices: bit flips ($X$), phase flips ($Z$), and combinations of the two ($Y = iXZ$). Let us say we want to detect and correct a bit-flip error ($Z$) using a 3-qubit repetition code.

Mathematically, the encoding for a bit-flip code is achieved by first encoding the state into a standard bit-flip code, and then rotating the basis using Hadamard gates. We take an initial data qubit state $\vert{}\psi\rangle = \alpha\vert{}0\rangle + \beta\vert{}1\rangle$ and two ancillary qubits initialized to $\vert{}0\rangle$.

We use the data qubit as the control for two CNOT gates targeting the ancillary qubits. This generates an entangled GHZ-like state in the computational basis:

$$\alpha\vert{}000\rangle + \beta\vert{}111\rangle$$

When this repetition code is passed through an error-prone channel which introduces, for example, a bit flip on the first qubit, we get an output from the channel of:

$$\alpha\vert{}100\rangle + \beta\vert{}011\rangle$$

If we now just take a majority vote, we can determine the error and fix it. Note that we do not actually need to measure the individual values of the qubits, which would collapse the superposition. We assume that only one qubit has flipped. Therefore, we only need to determine which of the qubits disagrees with the other two and flip it back.

To do this, we measure the parity observables $Z_1 \otimes Z_2$ and $Z_2 \otimes Z_3$. The $Z$ operator leaves the state $\vert{}0\rangle$ unchanged (eigenvalue $+1$) but applies a phase of $-1$ to the state $\vert{}1\rangle$. If two qubits are in the same computational state ($\vert{}00\rangle$ or $\vert{}11\rangle$), the joint observable $Z \otimes Z$ yields an eigenvalue of $+1$. If they are different ($\vert{}01\rangle$ or $\vert{}10\rangle$), it yields $-1$.

Measuring $Z_1 \otimes Z_2$ and $Z_2 \otimes Z_3$ gives us a unique error syndrome indicating which qubit differs from the rest:

-   If $Z_1 \otimes Z_2$ returns $-1$ and $Z_2 \otimes Z_3$ returns $+1$, then qubit 1 is different (flipped).
    
-   If $Z_2 \otimes Z_3$ returns $-1$ and $Z_1 \otimes Z_2$ returns $+1$, then qubit 3 is different (flipped).
    
-   If both return $-1$, then qubit 2 is different (flipped).

To perform let us say the $Z_1 \otimes Z_2$ measurement without collapsing the data qubits, we initialize an ancilla qubit in the state $\vert{}0\rangle_A$, pass it through a Hadamard gate to create the superposition $\frac{1}{\sqrt{2}}(\vert{}0\rangle_A + \vert{}1\rangle_A)$ or $\vert{}+\rangle_A$, and use it as the control for a controlled-$(Z_1 \otimes Z_2)$ operation targeting the data qubits. Due to phase kickback, the eigenvalue of the target state is kicked back to the relative phase of the control qubit.

For the error state where the first qubit has flipped ($\alpha\vert{}100\rangle + \beta\vert{}011\rangle$), the controlled operation yields:

$$C-(Z_1 \otimes Z_2) \left[ \frac{1}{\sqrt{2}}(\vert{}0\rangle_A + \vert{}1\rangle_A) \otimes (\alpha\vert{}100\rangle + \beta\vert{}011\rangle) \right]$$

$$= \frac{1}{\sqrt{2}} \left[ \vert{}0\rangle_A \otimes (\alpha\vert{}100\rangle + \beta\vert{}011\rangle) + \vert{}1\rangle_A \otimes (Z_1 \otimes Z_2)(\alpha\vert{}100\rangle + \beta\vert{}011\rangle) \right]$$

Since both $\vert{}100\rangle$ and $\vert{}011\rangle$ are eigenstates of $Z_1 \otimes Z_2$ with eigenvalue $-1$, this becomes:

$$= \frac{1}{\sqrt{2}} \left[ \vert{}0\rangle_A \otimes (\alpha\vert{}100\rangle + \beta\vert{}011\rangle) - \vert{}1\rangle_A \otimes (\alpha\vert{}100\rangle + \beta\vert{}011\rangle) \right]$$

$$= \frac{1}{\sqrt{2}}(\vert{}0\rangle_A - \vert{}1\rangle_A) \otimes (\alpha\vert{}100\rangle + \beta\vert{}011\rangle)$$

$$= \vert{}-\rangle_A \otimes (\alpha\vert{}100\rangle + \beta\vert{}011\rangle)$$

Applying a final Hadamard gate to the ancilla transforms $\vert{}-\rangle_A$ to $\vert{}1\rangle_A$. Measuring the ancilla as $1$ indicates the $-1$ eigenvalue, successfully extracting the syndrome without destroying the superposition of the data qubits.

This setup works because to detect a bit flip, we depend on the $Z$ gate, which differentiates between $\vert{}0\rangle$ and $\vert{}1\rangle$. A bit flip is essentially a transition between $\vert{}0\rangle$ and $\vert{}1\rangle$. Both of these are eigenstates of $Z$ with different eigenvalues ($+1$ and $-1$, respectively). The fact that they are eigenstates of $Z$ is what allows phase kickback to function without entangling the data with the ancilla. The fact that they have different eigenvalues allows us to receive distinct measurement readouts for the two states.

### Correcting for a Phase Flip in a 3-bit code
Similarly, to detect a relative phase flip—for example, an error that changes $\frac{1}{\sqrt{2}}(\vert{}0\rangle + \vert{}1\rangle)$ to $\frac{1}{\sqrt{2}}(\vert{}0\rangle - \vert{}1\rangle)$, or $\vert{}+\rangle$ to $\vert{}-\rangle$—we need an operator that differentiates between $\vert{}+\rangle$ and $\vert{}-\rangle$. We need an operator where these two are eigenstates with different eigenvalues. That operator is the $X$ gate.

To correct phase flips, we therefore encode our logical qubit into a phase-flip repetition code. We first create repetition qubits (e.g., $\alpha\vert{}000\rangle + \beta\vert{}111\rangle$) and then convert the physical data qubits via Hadamard gates into the $X$ basis, yielding $\alpha\vert{}+++\rangle + \beta\vert{}---\rangle$. When passing these through a noisy channel, a phase flip ($Z$ error) acts on these states exactly like a bit flip ($X$ error) acts on the computational basis.

To detect this, we measure the parity observables $X_1 \otimes X_2$ and $X_2 \otimes X_3$. This is done using two ancilla qubits initialized to $\vert{}0\rangle_A$, passed through Hadamard gates to create $\vert{}+\rangle_A$, and used as control qubits for controlled-$(X_1 \otimes X_2)$ and controlled-$(X_2 \otimes X_3)$ operations on the data qubits. Once again, phase kickback transfers the relative phase difference into the ancilla superposition. Passing the ancillae through final Hadamard gates converts the relative phase into a definitive $0$ or $1$ measurement, yielding the error syndrome.

### Correcting for a Bit & Phase Flip in a 9-bit Shor Code

The catch is that if we want to detect both bit and phase flips, we cannot rely solely on the 3-qubit repetition code. Measuring the syndrome for one type of error collapses the superposition required to correct the other, and the code lacks the degrees of freedom to protect against both simultaneously. To accommodate both, we create a 9-qubit concatenated code known as the Shor code.

The Shor code encodes a single logical qubit, $\vert{}0\rangle_L$, into three blocks of the phase-flip protection state $\vert{}+\rangle_{3b}$, where $\vert{}+\rangle_{3b} = \frac{1}{\sqrt{2}}(\vert{}000\rangle + \vert{}111\rangle)$. The full logical $\vert{}0\rangle_L$ state is therefore:

$$\vert{}0\rangle_L = \left[ \frac{1}{\sqrt{2}}(\vert{}000\rangle + \vert{}111\rangle) \right]^{\otimes 3}$$

Similarly, the logical qubit $\vert{}1\rangle_L$ is encoded using $\vert{}-\rangle_{3b}$ blocks:

$$\vert{}1\rangle_L = \left[ \frac{1}{\sqrt{2}}(\vert{}000\rangle - \vert{}111\rangle) \right]^{\otimes 3}$$

Bit flips can be detected by $Z_1Z_2$ and $Z_2Z_3$, along with their equivalents in the other blocks: $Z_4Z_5$, $Z_5Z_6$, $Z_7Z_8$, and $Z_8Z_9$. Phase flips must be detected across the $\vert{} \pm \rangle_{3b}$ blocks because an error in phase (and therefore a difference in relative phase) can only be detected by comparing the superpositions across these blocks. Therefore, phase flips are detected by the joint operators $X_1X_2X_3X_4X_5X_6$ and $X_4X_5X_6X_7X_8X_9$. This yields 8 syndrome generators. Since there are 9 physical qubits in the code, we are left with $9 - 8 = 1$ encoded data qubit.

To convert $\vert{}0\rangle_L$ into $\vert{}1\rangle_L$ (i.e., to perform a logical $\bar{X}$ operation), we apply a $Z$ gate to one qubit in each of the three blocks, such as $Z_1Z_4Z_7$. This flips the sign on the $\vert{}111\rangle$ terms in every $\vert{} \pm \rangle_{3b}$ block, converting between the two logical states. 

We could also use $Z_1Z_2Z_3Z_4Z_5Z_6Z_7Z_8Z_9$, but we are particularly interested in the minimum weight operator i.e. the string with the smallest number of non-identity Pauli elements capable of this transformation. This weight defines the distance $d$ of the code, which is the minimum number of local physical errors needed to map one valid logical codeword to another. A codeword is a valid string of logical qubits.

The distance for the Shor code is $3$. The number of errors $t$ that can be reliably detected and corrected is given by $d \ge 2t + 1$; hence, $t = 1$. If the number of errors exceeds $t$ but is strictly less than $d$, the errors can be detected but not reliably corrected, as the corrupted state may be closer to a different (but still valid) logical codeword.

### Stabilizer Formalism

The mechanics of the Shor code can be generalized into the Stabilizer Formalism, which describes a broad class of quantum error correction codes. Several classical linear error correcting codes can also be written in the stabilizer formalism, but we will focus on quantum error correction here.

Looking at the Shor code, we have 9 total qubits, with 8 syndromes and 1 data bit, and a distance of 3. A stabilizer code encoding $k$ logical qubits in $n$ physical qubits with distance $d$ is denoted as an $[[n, k, d]]$ code. The Shor code is a $[[9, 1, 3]]$ code.

Looking at each of the syndrome detection strings, note that they only trigger a syndrome, i.e. an eigenvalue of $-1$ for errors. For all valid codewords, they must trigger an eigenvalue of $+1$. In the stabilizer formalism, the syndrome strings are called the stabilizers because they stabilize or do not disturb valid codewords.

This tells us that we should construct our stabilizers such that each of them catches one particular error. Or, we can work the other way around and given a group of stabilizers, figure out what errors they can detect.

All generators of the stabilizer group must commute with each other ($[g_i, g_j] = 0$) to ensure they can be measured simultaneously without disturbing the system, as per the requirement of commutativity for compatible observables. The set of all unique products of these $n-k$ generators forms the stabilizer group $\mathcal{S}$. For $n-k$ independent generators, the group contains $2^{n-k}$ elements.

Notice that each stabilizer can have an eigenvalue of either +1 or -1. Because each independent stabilizer generator restricts the valid codeword space to its $+1$ eigenspace (effectively halving the dimension of the allowed Hilbert space), an $n$-qubit system constrained by $n-k$ generators leaves a $2^k$-dimensional code space. This code space accommodates $k$ logical qubits.

Operations within this $2^k$-dimensional space are executed by logical operators ($\bar{X}$, $\bar{Y}$, $\bar{Z}$), which are strings formed by applying one of the 4 Pauli operators on each qubit. By definition, logical operators must commute globally with all elements of the stabilizer group (they reside in the normalizer, $N(\mathcal{S})$) so that applying them does not move the state out of the valid code space.

To see why, note that $L C_1 = C_2$ where $C_1$ and $C_2$ are valid codewords. If $g$ is a stabilizer then multiplying with $g$ on both sides, we get $gL C_1 = gC_2 = C_2$ (because all codewords are eigenstates with eigenvalue 1 for any $g$). Similarly, we can write $gC_1 = C_1$. Multiplying on both sides with $L$ we get $LgC_1 = LC_1 = C_2$. Since these results are valid for all $C_1$, $Lg = gL$.

While they commute with the stabilizers, logical operators corresponding to the same logical qubit must anticommute with each other to to preserve the anticommutativity of operators for a single physical qubit. The logical operators represent the equivalents of the single qubit $Z$ and $X$ operators, but applied on the logical qubits and depicted by $\bar Z$ and $\bar X$. Thus for a 2-logical qubit system, we would have the equivalents for each logical qubit, which would be $\bar Z_1$, $\bar X_1$ and $\bar Z_2$ and $\bar X_2$ 

Note that when we say commute and anticommute, we are referring to these operations on a per qubit basis, and when determining commutativity between multi-qubit Pauli strings, sign changes accumulate per qubit. Operators that anticommute on an even number of individual physical qubits will commute globally. For instance, $Z_1Z_2$ commutes with $Z_2Z_3$ because $Z_2^2$ is the identity. But it does not commute with $X_2X_3$ because $Z_2$ and $X_2$ do not commute. However it will commute with $X_1X_2$ since the two minus signs cancel out.

The $n-k$ stabilizer generators combined with the $k$ logical $\bar{Z}$ operators form a maximally commuting set of $n$ observables, which completely defines a unique computational basis state for the full Hilbert space. Generally, the X logical operators are also included in the list as a complete description of the error correction code.

An error correction code will flag any error that anticommutes with at least one element of the stabilizer group. Errors that are elements of the stabilizer group $\mathcal{S}$ are degenerate; they act as the identity operation on the code space and do not corrupt the logical state. However, the code will fail to detect errors that commute with all stabilizers but are not in the stabilizer group (errors in the Normalizer of $S$, $N(\mathcal{S}) \setminus \mathcal{S}$), as these execute undetected logical operations.

We can calculate the logical qubits by applying the below projector to any unconstrained reference state such as $\vert{}+++\rangle$.

$$\prod_i\frac{I+P_i}{2}$$

where $P_i$ is a Pauli stabilizer generator.

Note that if the reference state is perfectly orthogonal to the target logical state (meaning they have zero mathematical overlap), the projector will completely annihilate it, returning a scalar zero ($0$) instead of a state vector. When you are writing classical software to simulate these projections and you receive a $0$ output, the algorithmic response is trivial: you simply discard the result, load a different unentangled basis state (such as $\vert{}000\rangle$ or $\vert{}+++\rangle$), and run the projection matrix again until a non-zero vector survives.

Here is an example of the mechanical derivation for the 3-bit bit-flip repetition code, which encodes $k=1$ logical qubit into $n=3$ physical qubits.

To uniquely define the state, we need exactly $n=3$ commuting constraint equations.

-   $g_1=Z_1Z_2$
    
-   $g_2=Z_2Z_3$
    
-   $\bar{Z}=Z_1Z_2Z_3$
    

We construct the global projector $\Pi$ by multiplying the filters for all three constraints. To construct $\vert{}0\rangle_L$, we enforce the $+\bar{Z}$ condition:

$$\Pi=\left(\frac{I+Z_1Z_2}{2}\right)\left(\frac{I+Z_2Z_3}{2}\right)\left(\frac{I+Z_1Z_2Z_3}{2}\right)$$

If we apply this to the physical vacuum state $\vert{}000\rangle$, the math is trivial because $\vert{}000\rangle$ is already a $+1$ eigenstate of all three operators. The projector simply outputs $\vert{}000\rangle$.

To see the filtering mechanics in action, we apply $\Pi$ to an unconstrained reference state, such as the uniform superposition:

$$\vert{}\psi_{\text{raw}}\rangle=\Pi\vert{}+++\rangle$$

$$\vert{}+++\rangle=\frac{1}{2\sqrt{2}}(\vert{}000\rangle+\vert{}001\rangle+\vert{}010\rangle+\vert{}011\rangle+\vert{}100\rangle+\vert{}101\rangle+\vert{}110\rangle+\vert{}111\rangle)$$

We pass the superposition through each matrix factor sequentially.

_Step A: Apply the $g_1$ filter_

The operator $\frac{I+Z_1Z_2}{2}$ annihilates any term where the first and second qubits differ in parity.

$$\vert{}\psi_A\rangle=\frac{1}{2\sqrt{2}}(\vert{}000\rangle+\vert{}001\rangle+\vert{}110\rangle+\vert{}111\rangle)$$

_Step B: Apply the $g_2$ filter_

The operator $\frac{I+Z_2Z_3}{2}$ annihilates any term where the second and third qubits differ. This isolates the error-correcting subspace.

$$\vert{}\psi_B\rangle=\frac{1}{2\sqrt{2}}(\vert{}000\rangle+\vert{}111\rangle)$$

_Step C: Apply the $\bar{Z}$ filter_

The operator $\frac{I+Z_1Z_2Z_3}{2}$ evaluates the total $Z$-parity. The term $\vert{}000\rangle$ yields an eigenvalue of $+1$, while $\vert{}111\rangle$ yields an eigenvalue of $-1$ and is annihilated.

$$\vert{}\psi_{\text{raw}}\rangle=\frac{1}{2\sqrt{2}}\vert{}000\rangle$$

Normalizing the surviving vector gives the final logical state:

$$\vert{}0\rangle_L=\vert{}000\rangle$$

Applying the transversal logical bit-flip $\bar{X}=X_1X_2X_3$ to this result will flip all three bits, generating $\vert{}1\rangle_L=\vert{}111\rangle$.

### Unitary Operations via Stabilizer Formalism

In the Schrodinger picture of Quantum Physics, time evolution and unitary operations are described via the differential equations involved. To simulate these on classical computers involves massive computation. For eg. a $2^n$-dimensional Hilbert space involves solving and tracking $2^n$ differential equations. In the Heisenberg picture, upon which the stabilizer formalism is based, we utilize the stabilizers to create simple lookup tables that depict how different operations affect a state.

Given a unitary operation $U$ and a state $\vert{}\psi\rangle$ with a set of stabilizer generators $\{g\}$, the state $\vert{}\phi\rangle$ after the operation acts on $\vert{}\psi\rangle$ will be stabilized by the generators $\{UgU^\dagger\}$. For eg. let us say we apply a Hadamard gate to a single qubit. Note that $HXH^\dagger=Z$; $HYH^\dagger=-Y$; $HZH^\dagger=X$. As a consequence we can deduce that after a Hadamard gate is applied to the quantum state stabilized by $Z$ ($\vert{}0\rangle$), the resulting state will be stabilized by $X$ ($\vert{}+\rangle$).

As another example, consider the CNOT gate. We can see that the $X_1$ operation on $\vert{}\psi\rangle$, where the first bit is the control bit, becomes an $X_1X_2$.

$$(X\otimes I)C=(X\otimes I)(\vert{}0\rangle\langle0\vert{}\otimes I+\vert{}1\rangle\langle1\vert{}\otimes X)$$

We distribute the terms. Because $X\vert{}0\rangle=\vert{}1\rangle$ and $X\vert{}1\rangle=\vert{}0\rangle$, the basis vectors on the control qubit flip:

$$=X\vert{}0\rangle\langle0\vert{}\otimes II+X\vert{}1\rangle\langle1\vert{}\otimes IX$$

$$=\vert{}1\rangle\langle0\vert{}\otimes I+\vert{}0\rangle\langle1\vert{}\otimes X$$

Now, we complete the conjugation by multiplying the CNOT operator on the left side of our previous result:

$$C(X\otimes I)C=(\vert{}0\rangle\langle0\vert{}\otimes I+\vert{}1\rangle\langle1\vert{}\otimes X)(\vert{}1\rangle\langle0\vert{}\otimes I+\vert{}0\rangle\langle1\vert{}\otimes X)$$

We expand this multiplication using the standard FOIL method. When we multiply the outer products, any terms containing orthogonal vectors (where $\langle0\vert{}1\rangle$ or $\langle1\vert{}0\rangle$ appear in the middle) mathematically evaluate to $0$.

-   **First term:** $(\vert{}0\rangle\langle0\vert{}\otimes I)(\vert{}1\rangle\langle0\vert{}\otimes I)=0$
    
-   **Outside term:** $(\vert{}0\rangle\langle0\vert{}\otimes I)(\vert{}0\rangle\langle1\vert{}\otimes X)=\vert{}0\rangle\langle1\vert{}\otimes X$
    
-   **Inside term:** $(\vert{}1\rangle\langle1\vert{}\otimes X)(\vert{}1\rangle\langle0\vert{}\otimes I)=\vert{}1\rangle\langle0\vert{}\otimes X$
    
-   **Last term:** $(\vert{}1\rangle\langle1\vert{}\otimes X)(\vert{}0\rangle\langle1\vert{}\otimes X)=0$
    

Only the outside and inside terms survive the multiplication. We factor out the tensor product:

$$C(X\otimes I)C=\vert{}0\rangle\langle1\vert{}\otimes X+\vert{}1\rangle\langle0\vert{}\otimes X$$

$$=(\vert{}0\rangle\langle1\vert{}+\vert{}1\rangle\langle0\vert{})\otimes X$$

The resulting term inside the parentheses is the exact geometric definition of the Pauli $X$ matrix:

$$=X\otimes X$$

Thus, a state stabilized by $X_1$ ($\vert{}+\rangle$) becomes a state stabilized by $X_1X_2$ ($\vert{}++\rangle$ or $\vert{}--\rangle$ or $\frac{1}{\sqrt{2}}(\vert{}00\rangle+\vert{}11\rangle)$).

Now consider an analysis of the SWAP gate, which can be described by a CNOT gate with control qubit 1, followed by a CNOT gate with control qubit 2 and another CNOT with control 1. The operator $Z_1$ transforms through the sequence $Z_1\to Z_1\to Z_1Z_2\to Z_2$ and the operator $Z_2$ transforms through the sequence $Z_2\to Z_1Z_2\to Z_1\to Z_1$. Similarly, $X_1\to X_2$ and $X_2\to X_1$ under the circuit. Thus we see the stabilizers swap across qubits 1 and 2. We had no need to perform any matrix multiplication to determine this.

### CSS Codes

CSS codes are stabilizer codes formed by $2$ linear classical codes $C_1$ and $C_2$ such that $C_1^\perp$ is a subset of $C_2$. Note that this also means that $C_2^\perp$ is a subset or equal to $C_1$. If the codes are $[n, k_1, d_1]$ and $[n, k_2, d_2]$ type, then we can form a quantum error correction code $[[n, k_1+k_2-n, d]]$ where $d$ is greater than or equal to the min of $d_1$ and $d_2$.

To form the CSS code, we take the parity matrices of the classical codes, $H_1$ and $H_2$. They will be $(n-k_1)\times n$ and $(n-k_2)\times n$ matrices. For one matrix, say $H_1$, replace every $1$ in a row of $H_1$ by a $Z$ for that qubit and a $0$ by identity. Similarly, for $H_2$, replace every $1$ by an $X$ and a $0$ by identity. The combined set of stabilizer generators form a CSS code. The logical operators for this code are given by the equivalence classes of codewords that commute with the stabilizers but are not stabilizers themselves. Specifically, the logical $X$ operators are formed by the classical codewords in $C_1 \setminus C_2^\perp$, and the logical $Z$ operators are formed by the classical codewords in $C_2 \setminus C_1^\perp$.

For surface codes it is beneficial to adopt a [pictorial representation](https://arxiv.org/html/1907.11157) where the basic unit is a four-cycle. Code qubits and ancilla qubits alternate in a lattice with edges connecting them. The red edges represent controlled-X gates, each controlled on an ancilla qubit $A$ and acting on a data qubit $D$. Likewise, the blue edges represent controlled-Z operations, each controlled by an ancilla qubit and acting on a data qubit. These controlled operations are the gates with which the stabilizers of the four-cycle are measured. Ancilla qubit $A_1$ connects to data qubits $D_1$ and $D_2$ via red edges, and therefore measures the stabilizer $X_{D1}X_{D2}$. Likewise, ancilla qubit $A_2$ measures the stabilizer $Z_{D1}Z_{D2}$.

In a surface code, stabilizers are local checks. Geometrically, they are closed loops or localized clusters (the crosses and plaquettes). If you multiply adjacent stabilizers together, they merge into larger closed loops. Therefore, any operator inside the stabilizer group $\mathcal{S}$ always forms a boundary-less geometric shape on the lattice.

To find a logical operator, an operator in $N(\mathcal{S}) \setminus \mathcal{S}$, you must draw a string of Pauli operators that satisfies two rules:

1.  **Commutation:** It must cross every stabilizer on an even number of qubits ($0$ or $2$) so that it commutes.
    
2.  **Independence:** It cannot be a closed loop, because all closed loops can be generated by multiplying stabilizers.
    

The only geometric object that satisfies both rules is an open string that stretches continuously from one boundary of the lattice to the opposite boundary. Because it stretches across the entire lattice, it cannot be formed by local closed loops (it is not in $\mathcal{S}$). Because it passes cleanly through the internal lattice structure, it enters and exits every local stabilizer it touches, guaranteeing it overlaps on exactly $2$ qubits (it is in $N(\mathcal{S})$).

Note that a string that forms a closed loop, either in the bulk or by traveling exclusively along boundaries of its own colour, belongs to the stabilizer group and evaluates to $+1$. It cannot be a logical operator.

To be a valid logical operator, the string must satisfy one strict geometric condition: it must start on one boundary and terminate on the opposite, disconnected boundary of its own colour. The path traversed to go from one boundary to the other should however be of the same colour, that is red for the $X$ operator and blue for the $Z$ logical operator.

So for the $[[13, 1, 3]]$ code in the paper, $X_{11}X_9X_{10}X_8X_3$ is a valid operator as is $X_{11}X_6X_4X_5X_3$ and $X_{13}X_8X_5X_2$. They can be continuously deformed into one another by multiplying them by the code's local $X$ stabilizers, they represent mathematically equivalent forms of the exact same logical $\bar{X}$ operator.
