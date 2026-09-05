# 1. Special Relativity and Classical Field Theory
## Special Relativity: Fundamental Postulates and the Lorentz Transformation

Galilean relativity assumes that every observer sees the "same" time; i.e., time is invariant across different inertial reference frames. Special Relativity, however, assumes the speed of light $c$ is invariant in all inertial reference frames. If we look at the equation for velocity $v = \frac{\Delta l}{\Delta t}$, in Galilean relativity, since $\Delta t$ is fixed for everyone, it is $\Delta l$ and $v$ that are correlated. However, in Special Relativity, since the speed of light $c$ is fixed, $\Delta l$ and $\Delta t$ are correlated.

Special Relativity also assumes that spacetime is flat and isotropic, and the laws of physics are identical everywhere, implying no reference frame is absolute or special.

From these postulates, we derive the Lorentz transformation, which defines the coordinate mapping from a rest frame to a moving reference frame. For a frame moving in the $x$-direction with velocity $v$:

$$\begin{bmatrix}ct'\\x'\end{bmatrix}=\begin{bmatrix}\gamma&-\gamma\beta\\-\gamma\beta&\gamma\end{bmatrix}\begin{bmatrix}ct\\x\end{bmatrix}$$

where $\beta=\frac{v}{c}$ and $\gamma=\frac{1}{\sqrt{1-\beta^2}}$

By symmetry, the inverse transformation flips the sign of $\beta$:

$$\begin{bmatrix}ct'\\x'\end{bmatrix}=\begin{bmatrix}\gamma&+\gamma\beta\\+\gamma\beta&\gamma\end{bmatrix}\begin{bmatrix}ct\\x\end{bmatrix}$$

Transformations for basis vectors and components are complementary. Components transform contravariantly, while basis vectors transform covariantly. 

Note that since $c$ is now a constant, we can start talking about time in terms of distance, which is why we introduce $ct$, so that all coordinates are in the dimensions of length.

The above matrix is called the Lorentz boost for one spatial coordinate. The general matrix for all 3 spatial coordinates is a bit more complicated.

The components of this symmetric matrix are:

-   Time-time component: $\Lambda^0_{\phantom{0}0}=\gamma$
    
-   Time-space components: $\Lambda^0_{\phantom{0}i}=\Lambda^i_{\phantom{i}0}=-\gamma\beta_i$
    
-   Space-space components: $\Lambda^i_{\phantom{i}j}=\delta_{ij}+(\gamma-1)\frac{\beta_i\beta_j}{\beta^2}$

$$\Lambda = \begin{bmatrix} \gamma & -\gamma\beta_x & -\gamma\beta_y & -\gamma\beta_z \\ -\gamma\beta_x & 1+(\gamma-1)\frac{\beta_x^2}{\beta^2} & (\gamma-1)\frac{\beta_x\beta_y}{\beta^2} & (\gamma-1)\frac{\beta_x\beta_z}{\beta^2} \\ -\gamma\beta_y & (\gamma-1)\frac{\beta_y\beta_x}{\beta^2} & 1+(\gamma-1)\frac{\beta_y^2}{\beta^2} & (\gamma-1)\frac{\beta_y\beta_z}{\beta^2} \\ -\gamma\beta_z & (\gamma-1)\frac{\beta_z\beta_x}{\beta^2} & (\gamma-1)\frac{\beta_z\beta_y}{\beta^2} & 1+(\gamma-1)\frac{\beta_z^2}{\beta^2} \end{bmatrix}$$

If we set $\beta_y=0$ and $\beta_z=0$, the off-diagonal spatial terms vanish, and the matrix reduces to the standard one-dimensional boost along the x-axis.

### Deriving the Lorentz Transformation (in 1 spatial dimension)
Because the transformation must be linear, the equation relating position $x'$ in $S'$ to coordinates $(x, t)$ in $S$ must take the form:

$$x' = A x + B t$$

Let's look at the origin of frame $S'$. By definition, its coordinate in $S'$ is always $x'=0$. In frame $S$, this origin is moving at velocity $v$, so its position is $x=vt$. Substituting these into the linear equation gives:

$$0 = A(vt) + Bt \implies B = -Av$$

Substituting $B$ back into our linear equation, we get:

$$x' = A(x - vt)$$

By the Principle of Relativity, neither frame is special. From the perspective of $S'$, frame $S$ is moving in the negative $x'$-direction at velocity $-v$. Because space is isotropic, the scaling factor $A$ must be identical for both frames. We will call this constant $\gamma$.

This gives us a symmetric pair of transformation equations:

$$x' = \gamma(x - vt)$$

$$x = \gamma(x' + vt')$$

To find $\gamma$, we invoke the second postulate. Imagine a flash of light is emitted at the exact moment the origins coincide ($t=t'=0$).

Because the speed of light is $c$ in both frames, the position of the light wavefront along the $x$-axis must satisfy:
In frame $S$: 

$$x = ct$$

In frame $S'$: 

$$x' = ct'$$

Substitute these expressions for $x$ and $x'$ into our symmetric transformation equations:

$$ct' = \gamma(ct - vt) = \gamma t(c - v)$$

$$ct = \gamma(ct' + vt') = \gamma t'(c + v)$$

Now, multiply these two equations together:

$$c^2 t t' = \gamma^2 t t' (c - v)(c + v)$$

Divide both sides by $t t'$ (assuming $t>0$) and expand the right side:

$$c^2 = \gamma^2 (c^2 - v^2)$$

Solve for $\gamma^2$:

$$\gamma^2 = \frac{c^2}{c^2 - v^2} = \frac{1}{1 - v^2/c^2}$$

Taking the positive root (since axes are aligned in the same direction), we obtain the Lorentz factor:

$$\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}$$

We have the spatial transformation $x'$ and the factor $\gamma$. We now need to find how time transforms ($t'$). We start with the inverse spatial equation:

$$x = \gamma(x' + vt')$$

Substitute the expression for $x'$ ($x' = \gamma(x - vt)$) into this equation:

$$x = \gamma(\gamma(x - vt) + vt')$$

Expand and isolate the $t'$ term:

$$x = \gamma^2 x - \gamma^2 vt + \gamma v t'$$

$$\gamma v t' = x - \gamma^2 x + \gamma^2 vt$$

$$t' = \gamma t + \frac{x(1 - \gamma^2)}{\gamma v}$$

To simplify the fraction on the right, we express $(1 - \gamma^2)$ in terms of $v$ and $c$:

$$1 - \gamma^2 = 1 - \frac{1}{1 - v^2/c^2} = \frac{1 - v^2/c^2 - 1}{1 - v^2/c^2} = \frac{-v^2/c^2}{1 - v^2/c^2} = -\frac{v^2}{c^2}\gamma^2$$

Substitute this back into our equation for $t'$:

$$t' = \gamma t + \frac{x(-\frac{v^2}{c^2}\gamma^2)}{\gamma v}$$

$$t' = \gamma t - \gamma \frac{vx}{c^2}$$

$$t' = \gamma\left(t - \frac{vx}{c^2}\right)$$

### Boosts & Rotations
The Lorentz boost matrix is only one case of the general Lorentz transformation, which also includes pure spatial rotations. For example, a spatial rotation in the $xy$-plane is represented by the following block-diagonal Lorentz matrix:

$$\Lambda=\begin{bmatrix}1&0&0&0\\0&\cos\theta&-\sin\theta&0\\0&\sin\theta&\cos\theta&0\\0&0&0&1\end{bmatrix}$$

Together, boosts and rotations form the Lorentz group, denoted as $O(1,3)$, defined universally as the set of all linear transformations (represented by $4 \times 4$ matrices $\Lambda$) that leave the Minkowski metric $\eta_{\mu\nu}$ invariant. The defining equation is:

$$\Lambda^\mu_\rho\eta_{\mu\nu}\Lambda^\nu_\sigma=\eta_{\rho\sigma}$$

In matrix notation, this is written as $\Lambda^T\eta\Lambda=\eta$, where $\eta$ is the Minkowski metric (more on this in the next section). Any matrix that satisfies this exact condition is a valid Lorentz transformation. In other words, any transformation that leaves the spacetime interval (more on this in the next section) invariant satisfies it. 

Considering that boosts satisfy this relationship, it is not surprising that spatial rotations also satisfy it. Since the invariant spacetime interval is given by $ds^2=-c^2dt^2+dx^2+dy^2+dz^2$, and a spatial rotation does not touch the time component while leaving the Euclidean distance $dx^2+dy^2+dz^2$ unchanged, the total spacetime interval $ds^2$ is also left unchanged. This is also conceptually as expected, since Special Relativity requires that no inertial reference frame is special, that is to say, the laws of physics should be the same in all inertial reference frames. This means that rotating into another reference frame should not change any of our equations.

Like standard spatial rotations, Lorentz transformations generally do not commute with each other. You cannot multiply the matrices any which way. For example, if you apply the rotation first, you change the orientation of the spatial axes. If you then apply a boost strictly along the $x$-axis, you are boosting along the original $x$-axis, which now corresponds to a different physical direction relative to the rotated particle.

If you apply the boost first, the particle gains velocity along the $x$-axis. If you subsequently apply the rotation, you are rotating the velocity vector itself into a new direction, mixing the boosted $x$-coordinates with the unboosted spatial coordinates. 

However, when the plane of rotation is completely orthogonal to the direction of the boost, they do commute. For example, if you apply a boost along the $x$-axis, the transformation only affects the $t$ and $x$ coordinates. If you apply a spatial rotation in the $yz$-plane, it only affects the $y$ and $z$ coordinates. Because the matrices operate on entirely separate, orthogonal subspaces, their matrix multiplication commutes.

### Lie Algebra of the Lorentz Group
In the Lie algebra of the Lorentz group, The 3 $K_i$ are the generators of boosts and 3 $J_i$ are the generators of rotations. Their commutation relations dictate how the operations interact.

The commutator of two boosts in different directions generates a rotation: $[K_i,K_j]=-i\epsilon_{ijk}J_k$. Thus, if you apply a boost in the $x$-direction followed by a boost in the $y$-direction, the result is not just a single combined boost in the $xy$-plane. It results in a combined boost plus an induced spatial rotation. In physics, this induced relativistic rotation is known as Thomas precession (or Wigner rotation).

A Lorentz transformation matrix may represent a boost, a rotation or both. It can be generated by exponentiating a linear combination of six fundamental generators, written as:

$$\Lambda = \exp\left( \sum_{i=1}^3 \theta^i J_i + \sum_{i=1}^3 \phi^i K_i \right)$$

To take the exponent of a matrix, we evaluate the matrix exponential, which is defined by the infinite Taylor series expansion:

$$\exp(M)=I+M+\frac{1}{2!}M^2+\frac{1}{3!}M^3+\dots=\sum_{n=0}^{\infty}\frac{1}{n!}M^n$$

For pure rotations, the matrix argument is $M=\theta J$. The rotation generators $J$ are anti-Hermitian matrices, which means $J^2=-I$. The Taylor series gives the sequence of matrix powers with alternating signs:

$$\exp(\theta J)=I+\theta J-\frac{1}{2!}\theta^2 I-\frac{1}{3!}\theta^3 J+\frac{1}{4!}\theta^4 I+\dots$$

Seperately grouping terms containing $I$ and $J$:

$$\exp(\theta J)=I\left(1-\frac{1}{2!}\theta^2+\frac{1}{4!}\theta^4-\dots\right)+J\left(\theta-\frac{1}{3!}\theta^3+\dots\right)$$

This reduces to $\exp(\theta J)=I\cos\theta+J\sin\theta$.

For boosts, the boost generators $K$ are Hermitian, so $K^2=I$. The Taylor series can be written as:

$$\exp(\phi K)=I+\phi K+\frac{1}{2!}\phi^2 I+\frac{1}{3!}\phi^3 K+\frac{1}{4!}\phi^4 I+\dots$$

$$=I\left(1+\frac{1}{2!}\phi^2+\frac{1}{4!}\phi^4+\dots\right)+K\left(\phi+\frac{1}{3!}\phi^3+\dots\right)$$

$$\exp(\phi K)=I\cosh\phi+K\sinh\phi$$

If the exponent contains both rotations and boosts simultaneously ($\sum\theta^i J_i+\sum\phi^i K_i$), the expansion becomes significantly more complex.

## The Spacetime Interval
Using the Lorentz transformation, we can see that what is called the spacetime interval squared $ds^2=(c.dt)^2-dx^2$ is the same in all reference frames. Another way of saying that is that it is invariant under coordinate transformation. Each of the coordinates in this equation is actually an infinitesimal difference between two events. This geometry is encoded in the Minkowski metric tensor. Using the $(+, -, -, -)$ signature convention, the diagonal elements are $(1, -1, -1, -1)$, and all off-diagonal elements are 0. $ds$ is also called the line element. This invariance is exactly the same thing as was discussed above in terms of Lorentz invariance.

**Note:** It is only the infinitesimal spacetime interval that is invariant in all reference frames, including non-inertial ones since we can consider any situation as inertial when taking the infinitesimal limit. If we take a macroscopic finite interval ($\Delta s^2$), it will be invariant in all inertial reference frames but not necessarily in non-inertial frames. If the worldline is simply straight, the infinitesimal amounts add up straightforwardly. If however we have situations where the worldline is not simply linear, like in the Twin Paradox where the spaceship turns around, or a spaceship under constant acceleration, we must integrate the infinitesimal amounts over some parameter (usually $\tau$) to arrive at the actual spacetime interval between two events.

### Proper Time & Proper Length
Suppose we were to measure the elapsed time between two events at the same coordinates. Since $s$ is invariant in all reference frames, the measurement of elapsed time will be minimum in the rest frame of the two events because the $x^2$ term is zero for the rest frame and positive for all other moving frames. This minimum time is called the proper time $\tau$. Since it depends only on the spacetime interval and the constant $c$, it is also invariant. It plays an important role in deriving other invariants from the spacetime interval.

Similarly, a measurement of length involves two events separated spatially. In the objects rest frame, since the object is not moving, the length can be measured by noting the coordinates of each end of the object at different points in time. However, in a moving reference frame, we must make the coordinate measurements simultaneously ($t = 0$). 

Since $s$ is invariant and $t^2 = 0$ for all frames other than the rest frame (for which it can be positive) and positive for all other moving frames, the object's rest frame will always measure the maximum spatial length. This is called the proper length $L_0$, which is also invariant under coordinate transformation.

For a moving frame: $\Delta s^2 = c^2\Delta t^2 - \Delta x^2 = 0 - L^2 = -L^2$

For the rest frame: $-L^2 = c^2\Delta t'^2 - L_0^2$ and so $L_0^2 = L^2 + c^2\Delta t'^2$.

Note that this means $\Delta t'$ is non-zero and so the measurement which was simultaneous in a moving frame, will not be simultaneous in the rest frame. This is called the relativity of simultaneity. If we had indeed made the measurement simultaneously in the rest frame, the two events involved are different from the two events we worked with in the moving reference frame. In this case we would get $L^2 = L_0^2 + c^2\Delta t^2$ where $t$ is the time elapsed in the moving frame. However, $L$ in this case is not the length, as it has not been measured simultaneously. It is just the distance between two non-simultaneous events.

### An Illustrative Example
Usually, the Lorentz transformation is derived by giving the example of a light beam shot out in the $y$-direction while the spaceship is moving in the $x$-direction. The distance travelled by the light beam in the spaceship frame is a "vertical" $ct_{\text{sp}}$ while the distance travelled by the light beam in the Earth frame is a "hypotenuse" $ct_{\text{earth}}$. The horizontal component is $vt_{\text{earth}}$. You can then use the Pythagorean theorem to get the relationship between the two times and distances. 

This example works because there is no length contraction in the direction perpendicular to the spaceship's motion. If the example had shot the light beam along the length of the ship instead, we would have to account for the length contraction of the ship as well as the fact that the ship moves forward while the light beam is itself moving towards the front of the ship, as shown below.

Let $S$ be the Earth's frame and $S'$ be the spaceship's rest frame moving at velocity $v = \beta c$ along the $+x$-axis relative to $S$.

In the rest frame of the rocket, the proper length is $L_0$. Light travels from the back to the front at speed $c$: $t_s = \frac{L_0}{c} \implies L_0 = c t_s$

In the Earth frame, the length of the ship is contracted to $L = \frac{L_0}{\gamma}$, where $\gamma = \frac{1}{\sqrt{1 - \beta^2}}$.

During the time $t_e$ it takes for the light to reach the front of the ship, the light travels a total distance $d = c t_e$. Simultaneously, the front of the ship advances by $v t_e$.

Setting the distance traveled by light equal to the contracted length plus the displacement of the front: $c t_e = L + v t_e$

Substitute $L = \frac{L_0}{\gamma} = \frac{c t_s}{\gamma}$: $c t_e = \frac{c t_s}{\gamma} + v t_e$

Divide through by $c$: $t_e (1 - \beta) = \frac{t_s}{\gamma}$

Solving for $t_e$:

$$t_e = \frac{t_s}{\gamma (1 - \beta)} = \frac{t_s \sqrt{1 - \beta^2}}{1 - \beta} = t_s \sqrt{\frac{(1 - \beta)(1 + \beta)}{(1 - \beta)^2}} = t_s \sqrt{\frac{1 + \beta}{1 - \beta}}$$

While this gives the correct result, we can just use the Lorentz transform to quickly arrive at the same answer. However, there is one important connection between this result and the Doppler Effect.

### Connection to the Relativistic Doppler Effect

The same $\sqrt{\frac{1 + \beta}{1 - \beta}}$ factor governs the Relativistic Longitudinal Doppler Shift. If the spaceship emits consecutive light pulses (or wave crests) separated by a proper period $T_0 = t_s$ in its rest frame:

For a receding source, the time interval between received crests on Earth is scaled by: $T_e = T_0 \sqrt{\frac{1 + \beta}{1 - \beta}}$

Since frequency $f = \frac{1}{T}$, the observed frequency $f_e$ is redshifted by $f_e = f_0 \sqrt{\frac{1 - \beta}{1 + \beta}}$

For an approaching Source ($\beta$ becomes $-\beta$): $f_e = f_0 \sqrt{\frac{1 + \beta}{1 - \beta}}$

Note that the factor $\sqrt{\frac{1 + \beta}{1 - \beta}}$ naturally encapsulates both the classical Doppler shift due to changing path length and the kinematic time dilation of the source's internal clock.

## Spacetime Diagrams and Causality

A coordinate frame can be visualized on a Minkowski diagram with $ct$ on the vertical axis and $x$ on the horizontal, forming a square coordinate grid. Transforming to a moving reference frame shifts these axes into a rhombus, bringing the $ct'$ and $x'$ axes closer to the 45° line like a pair of scissors.

Vectors symmetric about this 45° line are Minkowski orthogonal; their slopes relative to the spatial axis are reciprocals. This geometry ensures the spacetime area of the coordinate grid remains constant under transformation, and the 45° line strictly bisects the coordinate axes. This enforces the invariance of the speed of light (1 unit of distance per 1 unit of time).

The 45° line represents the light cone:

* **Timelike Events:** Worldlines falling strictly within the light cone (closer to the $ct$ axis) represent timelike intervals. These events are causally connected. An inertial reference frame exists where the two events occur at the same spatial location.

* **Spacelike Events:** Worldlines falling outside the light cone (closer to the $x$ axis) represent spacelike intervals. An inertial reference frame exists where these events occur simultaneously at different spatial locations.

Because no worldline can cross the light cone (as nothing propagates faster than $c$), a timelike, causal relationship can never become spacelike under any transformation. Cause and effect cannot be reversed. However, for spacelike intervals, changing the reference frame shifts the line of simultaneity. This means two events that are simultaneous in one frame may occur in different chronological orders in other reference frames. This relativity of simultaneity resolves seeming paradoxes, such as Bell’s spaceship paradox.

## 4-Vectors
### 4-Velocity & 4-momentum
Since proper time $\tau$ is an invariant scalar, differentiating the spacetime position 4-vector by $\tau$ yields another invariant. In keeping with the analog in classical mechanics, this is the 4-velocity $U$:

$$U=\frac{d}{d\tau}(ct, x, y, z)= (c\frac{dt}{d\tau},\frac{dx}{dt}\frac{dt}{d\tau}, \frac{dy}{dt}\frac{dt}{d\tau}, \frac{dz}{dt}\frac{dt}{d\tau})  = \gamma(c, u_x, u_y, u_z)$$

Note that  $u_x, u_y, u_z$ is the spatial velocity we are used to from classical mechanics, given by $\frac{dx}{dt}$ etc. 

Also note that $\frac{dt}{d\tau} = \gamma$. To see why, we know that 

$$ds^2 = c^2d\tau^2$$

$$ds^2 = c^2dt^2 - dx^2 - dy^2 - dz^2$$

$$c^2d\tau^2 = c^2dt^2 - (dx^2 + dy^2 + dz^2)$$

$$c^2d\tau^2 = c^2dt^2 \left[1 - \frac{1}{c^2}\left(\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2\right)\right]$$

$$c^2d\tau^2 = c^2dt^2 \left(1 - \frac{v^2}{c^2}\right)$$

$$\left(\frac{dt}{d\tau}\right)^2 = \frac{1}{1 - \frac{v^2}{c^2}}$$

$$\frac{dt}{d\tau} = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} = \gamma$$

**Note:** A tempting logical leap to make is that since $v = \frac{dx}{dt}$, since length contracts in the moving frame and time dilates or speeds up, velocity as seen in a moving frame should reduce by a factor of $\gamma^2$. This is NOT true. The time dilation and length contraction formulas are restricted special cases applicable in different situation i.e. either the clock is at rest or measurement is made simultaneously. They cannot be used together and applied as algebraic identities. For a moving particle, space and time intervals mix together. To find how velocity transforms, you cannot evaluate space and time in isolation; you must apply the full Lorentz transformation to the differential path of the particle.

#### 4-Velocity & Momentum Are Conserved, Not Just Invariant
At this point, we can say that since all 4-vectors are dependant only on some other 4-vector and proper time, which are both invariant, all 4-vectors are invariant under coordinate transformation. All 4-vectors undergo coordinate transformation via the Lorentz boost i.e. the Lorentz transformation matrix given at the very beginning of the notes. Note that when we say invariant, we mean their magnitude is invariant (we can say $V^\mu V_\mu$ is constant). The vectors (and their components) are free to change within this constraint.

However, though 4-position is invariant under coordinate change, it does vary as the world line evolves with proper time. In contrast, the 4-velocity, and therefore the 4-momentum, are conserved, which means they are unchanged for an isolated system not just under coordinate transformations, but also as the world line evolves. This can be easily seen by taking the derivative of spacetime vector with proper time in the rest frame, which just yields $c$. In fact they are even conserved for non-inertial reference frames. 

Thus, the invariant magnitude squared of the 4-velocity is always constant: $U\cdot U=c^2$. This also means, $u_0^2 = 1 + \sum_i u_i^2$ (ignoring the factor $c$ for brevity), which means the time component of velocity is never zero. Thus, no matter what the situation, the worldline of an object will always advance in time, which means time can never stop or reverse.


Multiplying $U$ by mass $m$ (which we assume is invariant) yields the 4-momentum $P$:

$$P=mU=\gamma(mc, mu_x, mu_y, mu_z)=(E/c, p_x, p_y, p_z)$$

where we absorb the $\gamma$ factor into the $E$ and spatial $p$ terms. 

Thus the spatial momentum is actually $\gamma mv$, not $mv$, the classical Newtonian formula. The Newtonian formula is not universally correct. It is fundamentally a low-velocity approximation.

#### Time, Energy, Space & Momentum
Notice that we set the $ct$ coordinate as being related to the energy. Qualitatively, we can say that just as $l = vt$,  $E = vp$ in terms of dimensional analysis. So we are not unjustified in relating the time coordinate of 4-momentum to energy. More rigorously,

$$\gamma = \left(1 - \frac{u^2}{c^2}\right)^{-1/2} \approx 1 + \frac{u^2}{2c^2} + \frac{3u^4}{8c^4} + \dots$$

Substituting this expansion into the time component of 4-momentum gives:

$$P^0 = \gamma mc \approx mc \left(1 + \frac{u^2}{2c^2}\right) = \frac{1}{c} \left(mc^2 + \frac{1}{2}mu^2\right)$$

The second term in the parenthesis, $\frac{1}{2}mu^2$, is the recognizable classical kinetic energy. The first term, $mc^2$, is the constant rest mass energy. Since the entire bracketed expression represents the total energy $E$ of the free particle, we can definitively state:

$$P^0 = \frac{E}{c}$$

From a more advanced theoretical perspective, the grouping of energy and momentum into a single 4-vector is a direct consequence of spacetime symmetries.

Just as the spacetime 4-vector $(ct, x, y, z)$ dictates the geometry of events, Noether's theorem states that symmetries in these continuous coordinates generate conserved quantities:

-   Invariance under spatial translation ($x, y, z$) yields the conservation of 3-momentum ($p_x, p_y, p_z$).
    
-   Invariance under time translation ($t$) yields the conservation of energy ($E$).
    
Because space and time transform into one another under Lorentz transformations, their conjugate conserved quantities (momentum and energy) must also transform into one another as a unified 4-vector $(E/c, p_x, p_y, p_z)$.

#### Conservation of Momentum
From the expression for $P$, as expected from its relationship with $U$, we can see that the dot product $P\cdot P$ is conserved. Expanding this dot product yields:

$$P\cdot P=(E/c)^2-p^2=(mc)^2$$

Rearranging this gives Einstein’s energy-momentum relation:

$$E^2=(mc^2)^2+(pc)^2$$

You can verify that this holds for the components by substituting with $E = \gamma mc^2$ and $p = \gamma mv$ on both sides of the equation. 

When a particle is at rest ($p=0$), the equation reduces to $E=mc^2$. 

**Note 1:** For massless particles traveling at $c$, proper time $\tau$ is undefined and invariant mass $m=0$, and momentum is derived via quantum relations ($p=h/\lambda$) or $E=pc$, and the above formula continues to hold.

**Note 2:** Since total 4-momentum $P$ is conserved in isolated systems and invariant mass $m$ is dictated by the magnitude of the total 4-momentum rather than a simple sum of scalars, the total invariant mass of a system can change during processes such as inelastic collisions, even while $P$ remains rigorously conserved.

**Note 3:** Since 4-momentum is conserved, it means its components are also independently conserved, including the spatial momentum and the time component or relativistic energy. $\sum E_{\text{initial}} = \sum E_{\text{final}}$ and $\sum \mathbf{p}_{\text{initial}} = \sum \mathbf{p}_{\text{final}}$. This last equation would not hold if we used the Newtonian formula for momentum: $p = m \cdot v$


### 4-Acceleration
Differentiating 4-momentum or 4-velocity with respect to $\tau$ yields 4-force and 4-acceleration, respectively. Since the magnitude of 4-velocity cannot change, we can say that 4-acceleration must always be orthogonal to 4-velocity. 

This means that in the objects rest frame, where the only velocity component is the time component, 4-acceleration will have no time component. This is called the proper acceleration on the object i.e. the acceleration measured by the object in its rest frame. This is a non-inertial frame. Note that the magnitude of the 4-acceleration is still invariant under change of coordinates and is equal to the magnitude of the spatial acceleration in the object's rest frame.

Unlike 4-velocity and momentum, the spatial components of 4-acceleration and 4-force are not necessarily parallel to their classical 3-vector counterparts. This is due to the factor of $\gamma$ which is present in the 4-velocity. When we differentiate by proper time $\tau$, since $\gamma$ depends on velocity, it contributes to the derivative in a way that changes the orientation of the components. 

To find $\frac{d\gamma}{dt}$, we apply the chain rule to this correct definition:

$$\frac{d\gamma}{dt}=-\frac{1}{2}\left(1-\frac{u^2}{c^2}\right)^{-3/2}\left(-\frac{2\mathbf{u}\cdot\mathbf{a}}{c^2}\right)$$

Where $\mathbf{a}=\frac{d\mathbf{u}}{dt}$ is the standard 3-acceleration as measured in that reference frame. Recognizing that $(1-u^2/c^2)^{-3/2}=\gamma^3$, this simplifies to:

$$\frac{d\gamma}{dt}=\gamma^3\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}$$

Applying the derivative operator to the time component of 4-velocity $U^0=\gamma c$:

$$A^0=\gamma\frac{d}{dt}(\gamma c)=\gamma c\frac{d\gamma}{dt}$$

Substituting the derivative of $\gamma$ derived above:

$$A^0=\gamma c\left(\gamma^3\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}\right)=\gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c}$$

Applying the derivative operator to the spatial components of 4-velocity $\mathbf{U}=\gamma\mathbf{u}$ requires the product rule. 

$$\mathbf{A}=\gamma\frac{d}{dt}(\gamma\mathbf{u})=\gamma\left(\frac{d\gamma}{dt}\mathbf{u}+\gamma\frac{d\mathbf{u}}{dt}\right)$$

Substituting $\mathbf{a}=\frac{d\mathbf{u}}{dt}$ and our expression for $\frac{d\gamma}{dt}$:

$$\mathbf{A}=\gamma\left(\left(\gamma^3\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}\right)\mathbf{u}+\gamma\mathbf{a}\right)$$

Distributing the outer $\gamma$:

$$\mathbf{A}=\gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}\mathbf{u}+\gamma^2\mathbf{a}$$

Combining the time and spatial components yields the full 4-acceleration vector:

$$A=\left(\gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c}, \gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}\mathbf{u}+\gamma^2\mathbf{a}\right)$$

We can write this out in the $x, y, z$ spatial coordinates as:

$$A_x = \gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}u_x + \gamma^2a_x$$

$$A_y = \gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}u_y + \gamma^2a_y$$

$$A_z = \gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}u_z + \gamma^2a_z$$

The presence of the $\mathbf{u}$ term in the 4-acceleration demonstrates that $\mathbf{A}$ and $\mathbf{a}$ are only parallel in two specific physical cases: if the velocity $\mathbf{u}$ and classical acceleration $\mathbf{a}$ are either parallel or perpendicular to each other (as in centripetal acceleration).

Note that the magnitude of the 4-acceleration in the object's rest frame is given by:

$$A^\mu A_\mu = (A^0)^2 - \vert{}\mathbf{A}\vert{}^2 = 0^2 - \vert{}\boldsymbol{\alpha}\vert{}^2 = -\vert{}\boldsymbol{\alpha}\vert{}^2$$

where $\alpha$ is the proper acceleration. Since the 4-acceleration's magnitude is invariant, it means the magnitude is equal to the above value in any reference frame. 

We can also write the 4-acceleration in terms of the proper acceleration. By first applying a Lorentz boost from the rest frame to an arbitrary frame, we get,

$$A = \left( \gamma\frac{\mathbf{u} \cdot \boldsymbol{\alpha}}{c}, \boldsymbol{\alpha} + \frac{\gamma^2}{\gamma + 1}\frac{\mathbf{u} \cdot \boldsymbol{\alpha}}{c^2}\mathbf{u} \right)$$

Equating this to the previous derivation for the 4-acceleration, we get,

$$a_\parallel = \frac{\alpha_\parallel}{\gamma^3}$$

$$a_\perp = \frac{\alpha_\perp}{\gamma^2}$$

where $a_\parallel$ is the acceleration along the direction of movement of the moving frame, and $a_\perp$ is along a direction perpendicular to it. We can immediately see that the acceleration along the direction of movement is suppressed by an extra $\gamma$ factor compared to the perpendicular direction. This is because along the direction of motion of the reference frame, we must account for both time dilation and length contraction, while in the perpendicular direction, time dilation is all that matters.

Another important point about these equations is that when the object is under constant proper acceleration, its rest frame is also constantly accelerating with respect to some arbitrary frame that is moving at constant velocity. Thus, the suppression factor of $\gamma$ grows larger and larger. The acceleration of the object in this constant velocity frame therefore falls drastically. Thus the velocity of the object in this frame increases by smaller and smaller amounts and never crosses $c$, though it approaches $c$. All of this is immaterial when it comes to the rest frame of course, where the object is always at rest. We will see in the next section on the 4-force that the magnitude of the force required to maintain a constant proper acceleration will grow as the object's relative velocity increases. 
 
 ### 4-Force
The 4-force is defined as $K = m A = m\frac{dP}{d\tau}$. Thus the 4-force is also always orthogonal to the 4-velocity, and in the object's rest frame, the time component of the 4-force is 0, making it essentially equal to the spatial force component acting on the object, called the proper force. The invariant length of the 4-force is equal to the length of the proper force, given by $K_\mu K^\mu = -\vert{}\mathbf{F}_{proper}\vert{}^2$.

The proper force represents the physical stress actually experienced by the object. If you attached a mechanical accelerometer (such as a mass on a spring) to the moving block, the reading on that accelerometer would correspond directly to the proper force.

The 4-force can be expressed in terms of the laboratory-frame 3-force $\mathbf{F}$ and velocity $\mathbf{v}$. We can replace the derivative by $\tau$ with $dt$ in the equation for 4-force to get:

$$K^\mu = \gamma \frac{d}{dt} \left( \frac{E}{c}, \mathbf{p} \right) = \left( \frac{\gamma}{c} \frac{dE}{dt}, \gamma \frac{d\mathbf{p}}{dt} \right)$$

The relativistic 3-force $\mathbf{F}$ measured by an observer in the lab frame is the coordinate time derivative of the relativistic 3-momentum $\mathbf{p}$:

$$\mathbf{F} = \frac{d\mathbf{p}}{dt}$$

Substituting this directly into the spatial part of our 4-vector equation gives:

$$\mathbf{K} = \gamma \mathbf{F}$$

For the temporal component, from the work-energy theorem, mechanical power is calculated as the dot product of the applied force and the object's velocity:

$$\frac{dE}{dt} = \mathbf{F} \cdot \mathbf{v}$$

We can formally prove this by taking the time derivative of the invariant mass relation $E^2 - (pc)^2 = (mc^2)^2$. Differentiating yields $2E \frac{dE}{dt} - 2pc^2 \frac{dp}{dt} = 0$. Substituting $E = \gamma mc^2$, $p = \gamma mv$, and $\frac{dp}{dt} = F$ confirms that $\frac{dE}{dt} = F v$ for linear motion, generalizing to $\mathbf{F} \cdot \mathbf{v}$ in 3D. Thus, 

$$K^\mu = \gamma \left( \frac{\mathbf{F} \cdot \mathbf{v}}{c}, \mathbf{F} \right)$$

or

$$K^\mu = \gamma \left( \frac{\mathbf{F} \cdot \mathbf{v}}{c}, F_x, F_y, F_z \right)$$

#### Example of Transforming From The Rest Frame to the Lab Frame

Let the particle's instantaneous rest frame be $S'$. In this frame, the velocity is zero, so the 4-force consists only of the proper force:

$$K'^\mu = (0, F_{proper, x}, F_{proper, y}, F_{proper, z})$$

Let the laboratory frame be $S$, in which the particle is moving with velocity $v$ along the $x$-axis. We transform the 4-force from $S'$ to $S$ using the standard Lorentz boost matrix in the $x$-direction:

$$K^0 = \gamma \left( K'^0 + \frac{v}{c} K'^1 \right) = \gamma \left( 0 + \frac{v}{c} F_{proper, x} \right) = \gamma \frac{v}{c} F_{proper, x}$$

$$K^1 = \gamma \left( K'^1 + \frac{v}{c} K'^0 \right) = \gamma \left( F_{proper, x} + 0 \right) = \gamma F_{proper, x}$$

$$K^2 = K'^2 = F_{proper, y}$$

$$K^3 = K'^3 = F_{proper, z}$$

By equating these Lorentz-transformed components with the spatial components extracted from the 4-Force's relationship with the 3-Force that we derived a little above, we get:

**Longitudinal component (parallel to velocity):** $\gamma F_x = \gamma F_{proper, x} \implies F_x = F_{proper, x}$

**Transverse components (perpendicular to velocity):** $\gamma F_y = F_{proper, y} \implies F_y = \frac{F_{proper, y}}{\gamma}$ and $\gamma F_z = F_{proper, z} \implies F_z = \frac{F_{proper, z}}{\gamma}$

Therefore, a force applied parallel to the direction of motion has the same magnitude in both the lab frame and the rest frame. However, any force applied perpendicular to the direction of motion is measured to be smaller in the lab frame by a factor of $\frac{1}{\gamma}$.

The difference in how the forces transform stems from the fact that both longitudinally and along the transverse, time dilation is present. However, longitudinally or along the direction of movement of the frame, velocity and therefore momentum is also transformed by the factor $\gamma$, which negates the time dilation factor. 

### Relationship Between 4-Force and 4-Acceleration
In terms of 4 vectors, $K = mA$ but in terms of 3-vectors, $\mathbf{F} = m\mathbf{a}$ does not hold in special relativity. It is a Newtonian low velocity approximation. The more fundamental definition of force is $\mathbf{F} = \frac{d\mathbf{p}}{dt}$. In relativity, as we saw, $\mathbf{p} = \gamma m\mathbf{v}$. Since the Lorentz factor $\gamma$ depends on velocity, it is not constant during acceleration. This changes the relationship between force and acceleration from the low velocity approximation.

First, we show that the $K = mA$ relationship holds for 4-vectors, and then derive the relationship that actually holds for 3-vectors.

#### The 4-vector Relationship
We know that $\mathbf{F} = \frac{d\mathbf{p}}{dt} = \frac{d}{dt}(\gamma m\mathbf{v}) = m\left(\frac{d\gamma}{dt}\mathbf{v} + \gamma\frac{d\mathbf{v}}{dt}\right)$

From our 4-acceleration derivation above we have,$\frac{d\mathbf{v}}{dt} = \mathbf{a}$ and $\frac{d\gamma}{dt} = \gamma^3\frac{\mathbf{v}\cdot\mathbf{a}}{c^2}$. Substituting these in yields the explicit kinematic form of the 3-force:

$$\mathbf{F} = m\left(\gamma^3\frac{\mathbf{v}\cdot\mathbf{a}}{c^2}\mathbf{v} + \gamma\mathbf{a}\right)$$

To construct the spatial component of the 4-force, we multiply this 3-force by $\gamma$, as shown previously:

$$\gamma\mathbf{F} = m\left(\gamma^4\frac{\mathbf{v}\cdot\mathbf{a}}{c^2}\mathbf{v} + \gamma^2\mathbf{a}\right)$$

If we distribute the mass $m$, this perfectly matches the spatial component of $mA^\mu$:

$$m\mathbf{A} = m\left(\gamma^4\frac{\mathbf{v}\cdot\mathbf{a}}{c^2}\mathbf{v} + \gamma^2\mathbf{a}\right)$$

For the temporal component, 
$$\mathbf{F} \cdot \mathbf{v} = \left[ m\left(\gamma^3\frac{\mathbf{v}\cdot\mathbf{a}}{c^2}\mathbf{v} + \gamma\mathbf{a}\right) \right] \cdot \mathbf{v}$$

We can factor out the common term $m(\mathbf{v}\cdot\mathbf{a})\gamma$:

$$\mathbf{F} \cdot \mathbf{v} = m(\mathbf{v}\cdot\mathbf{a})\gamma \left(\gamma^2\frac{v^2}{c^2} + 1\right)$$

To simplify the term in the parentheses, recall that $\gamma^2 = \frac{1}{1 - v^2/c^2}$. Rearranging this gives the identity $\gamma^2\frac{v^2}{c^2} + 1 = \gamma^2$. Substituting this identity into our equation collapses the expression:

$$\mathbf{F} \cdot \mathbf{v} = m(\mathbf{v}\cdot\mathbf{a})\gamma(\gamma^2) = m\gamma^3(\mathbf{v}\cdot\mathbf{a})$$

Finally, we construct the temporal component of the 4-force by multiplying this result by $\frac{\gamma}{c}$:

$$\gamma\frac{\mathbf{F} \cdot \mathbf{v}}{c} = \frac{\gamma}{c} \left[ m\gamma^3(\mathbf{v}\cdot\mathbf{a}) \right] = m\gamma^4\frac{\mathbf{v}\cdot\mathbf{a}}{c}$$

This matches the temporal component of $mA^\mu$:

$$mA^0 = m\left(\gamma^4\frac{\mathbf{v}\cdot\mathbf{a}}{c}\right)$$

#### The Relativistic 3-vector Relationship
We apply the product rule to the time derivative of the relativistic momentum:

$$\mathbf{F} = \frac{d}{dt}(\gamma m\mathbf{v}) = m\left( \frac{d\gamma}{dt}\mathbf{v} + \gamma \frac{d\mathbf{v}}{dt} \right)$$

Again, as shown previously, the time derivative of the Lorentz factor is $\dot{\gamma} = \frac{\gamma^3}{c^2}(\mathbf{v} \cdot \mathbf{a})$. Substituting this and $\mathbf{a} = \frac{d\mathbf{v}}{dt}$ into the equation yields the true relativistic equivalent of Newton's Second Law for 3-vectors:

$$\mathbf{F} = \gamma m\mathbf{a} + \frac{\gamma^3 m}{c^2}(\mathbf{v} \cdot \mathbf{a})\mathbf{v}$$

As noted however, the 4-force $K^\mu$, the invariant rest mass $m$, and the 4-acceleration $A^\mu$, are still related by Newton's Law. The complexity of the 3-vector equation is merely an artifact of projecting the simple 4-dimensional reality down into separate 3-dimensional space and 1-dimensional coordinate time.

The most significant physical consequence of this equation is that force and acceleration are generally no longer parallel.

Because of the second term containing the dot product $(\mathbf{v} \cdot \mathbf{a})\mathbf{v}$, the force vector $\mathbf{F}$ possesses a component pointing in the direction of the velocity vector $\mathbf{v}$. An applied force will only produce an acceleration in the exact same direction if the force is applied strictly parallel or strictly perpendicular to the particle's current velocity.

Because $\mathbf{F}$ and $\mathbf{a}$ do not scale by a single scalar constant, a particle's resistance to acceleration (its inertia) depends entirely on the angle between the applied force and the particle's velocity.

**Transverse Acceleration (Force perpendicular to velocity):** If the force is applied at a right angle to the motion, $\mathbf{v} \cdot \mathbf{a} = 0$. The second term vanishes, yielding: $\mathbf{F} = \gamma m\mathbf{a}$. The particle's effective inertia is $\gamma m$.

**Longitudinal Acceleration (Force parallel to velocity):** If the force is applied in the exact direction of motion, $\mathbf{v}$ and $\mathbf{a}$ are parallel, so $\mathbf{v} \cdot \mathbf{a} = va$. The equation simplifies (using $\gamma^2 = 1/(1 - v^2/c^2)$) to: $\mathbf{F} = \gamma^3 m\mathbf{a}$.

The particle's effective inertia is $\gamma^3 m$. It is significantly harder to accelerate a relativistic particle along its path of motion than it is to deflect it laterally.

#### 4-force is not a gradient like the 3-force
In classical mechanics, a conservative force is simply the negative gradient of a scalar potential: $F^\alpha=-m\partial^\alpha\Phi$, where $\alpha \in \{1,2,3\}$ represents the spatial dimensions. What prevents us from just upgrading this to a 4-vector equation by letting the index cover time as well: $ma^i=-\partial^i\Phi$.

Since velocity and acceleration are always orthogonal, $a^i u_i=0$. If we substitiute this into our hypothetical equation: $m(a^i u_i)=-(\partial^i\Phi)u_i$, and so $0=-u^i\partial_i\Phi$. From the chain rule, we get that $u^i\partial_i\Phi=\frac{dx^i}{d\tau}\frac{\partial\Phi}{\partial x^i} =\frac{d\Phi}{d\tau}$. This is a pretty boring and useless potential field. As the particle travels along its worldline (advancing its proper time $\tau$), the potential field $\Phi$ it experiences cannot change. The particle will never convert potential into kinetic energy.

What other options do we have to construct a 4-force such that $F^i u_i=0$ without forcing the particle to stay at a constant potential? By constructing the force using an antisymmetric tensor multiplied by the 4-velocity. The canonical example is the electromagnetic Lorentz force. Because you are contracting an antisymmetric tensor ($F^{ik}$) with a symmetric product of vectors ($u_k u_i$), the sum automatically evaluates to exactly zero.

## Hyperbolic Formulation

The Lorentz transformation naturally maps to hyperbolic geometry, satisfying the constant hyperbolic curve $(ct)^2-x^2=\text{constant}$:

$$\begin{bmatrix}ct'\\x'\end{bmatrix}=\begin{bmatrix}\cosh\phi&-\sinh\phi\\-\sinh\phi&\cosh\phi\end{bmatrix}\begin{bmatrix}ct\\x\end{bmatrix}$$

Here, $\phi$ is the rapidity, defined by the relation $\tanh\phi=v/c=\beta$. Note that $\gamma=\cosh\phi$ and $\gamma\frac{v}{c}=\sinh\phi$. This hyperbolic formulation allows relative velocities to be calculated via the simple addition of rapidities: $\phi_{AC}=\phi_{AB}+\phi_{BC}$

To see why this is so, just multiply the two Lorentz boost matrices, one for each rapidity that we want to add up. We end up with terms that can be replaced by hyperbolic identities $\cosh(\phi_1-\phi_2)=\cosh\phi_1\cosh\phi_2-\sinh\phi_1\sinh\phi_2$ and $\sinh(\phi_1-\phi_2)=\sinh\phi_1\cosh\phi_2-\cosh\phi_1\sinh\phi_2$:

$$\Lambda(\phi_1)\Lambda(\phi_2)=\begin{bmatrix}\cosh\phi_1&\sinh\phi_1\\\sinh\phi_1&\cosh\phi_1\end{bmatrix}\begin{bmatrix}\cosh\phi_2&\sinh\phi_2\\\sinh\phi_2&\cosh\phi_2\end{bmatrix}$$

$$\Lambda(\phi_1)\Lambda(\phi_2)=\begin{bmatrix}\cosh\phi_1\cosh\phi_2+\sinh\phi_1\sinh\phi_2&\cosh\phi_1\sinh\phi_2+\sinh\phi_1\cosh\phi_2\\\sinh\phi_1\cosh\phi_2+\cosh\phi_1\sinh\phi_2&\sinh\phi_1\sinh\phi_2+\cosh\phi_1\cosh\phi_2\end{bmatrix}$$

$$\Lambda(\phi_1)\Lambda(\phi_2)=\begin{bmatrix}\cosh(\phi_1+\phi_2)&\sinh(\phi_1+\phi_2)\\\sinh(\phi_1+\phi_2)&\cosh(\phi_1+\phi_2)\end{bmatrix}=\Lambda(\phi_1+\phi_2)$$

If we do not use the hyperbolic formulation, we must resort to the non-linear velocity addition formula given by:

$$v=\frac{v_1+v_2}{1+\frac{v_1v_2}{c^2}}$$

This formulation also means that under constant proper acceleration $a$, the rapidity $\phi$ changes linearly with respect to proper time $\tau$ according to $d\phi/d\tau=a/c$. To derive this, note that

$$U^\mu=\left(c\cosh\phi,c\sinh\phi,0,0\right)$$

$$A^\mu=\frac{dU^\mu}{d\tau}=\left(c\sinh\phi\frac{d\phi}{d\tau},c\cosh\phi\frac{d\phi}{d\tau},0,0\right)$$

Since the scalar magnitude of acceleration in invariant: $a^2=\eta_{\mu\nu}A^\mu A^\nu=-(A^0)^2+(A^1)^2$, and:

$$a^2=-\left(c\sinh\phi\frac{d\phi}{d\tau}\right)^2+\left(c\cosh\phi\frac{d\phi}{d\tau}\right)^2$$

$$a^2=c^2\left(\frac{d\phi}{d\tau}\right)^2(\cosh^2\phi-\sinh^2\phi) = c^2\left(\frac{d\phi}{d\tau}\right)^2(1)$$

$$\frac{d\phi}{d\tau}=\frac{a}{c}$$

The worldline of an object under constant proper acceleration (the acceleration measured by an accelerometer in the object's rest frame) can be evaluated by integrating the 4-velocity vector. This integration yields a worldline where the Lorentz transformation is applicable at every individual point to map to a Momentarily Comoving Inertial Frame (MCIF), but the global worldline traces a hyperbola.

We can use this relationship and the equations between $\gamma, \beta, v$ and $\tau$ to find the time, velocity and position of the accelerating body as seen from some inertial frame.

$$v(\tau)=c\beta=c\tanh\left(\frac{a\tau}{c}\right)$$

$$\frac{dt}{d\tau}=\gamma(\tau)=\cosh\left(\frac{a\tau}{c}\right)$$

Integrating this yields the coordinate time equation:

$$t=\frac{c}{a}\sinh\left(\frac{a\tau}{c}\right)$$

To find the position, use the chain rule:

$$v(\tau)=\frac{dx}{dt}=\frac{\frac{dx}{d\tau}}{\frac{dt}{d\tau}}\implies\frac{dx}{d\tau}=c\sinh\left(\frac{a\tau}{c}\right)$$

Integrating with respect to proper time yields the position equation (assuming the particle starts at $x=0$ when $t=0$ and $\tau=0$):

$$x=\frac{c^2}{a}\cosh\left(\frac{a\tau}{c}\right)-\frac{c^2}{a}$$

By combining the position and time equations and utilizing the hyperbolic identity $\cosh^2\theta-\sinh^2\theta=1$, we recover the invariant trajectory equation, proving that the worldline of constant proper acceleration is a hyperbola in Minkowski spacetime:

$$\left(x+\frac{c^2}{a}\right)^2-c^2t^2=\frac{c^4}{a^2}$$

### Bell's Paradox

Let us define the hyperbola of a worldline under constant proper acceleration $a$ such that it intersects the $ct=0$ axis of an inertial frame at the spatial coordinate $x=c^2/a$ (let us define this constant distance as $D$). This worldline will asymptotically approach, but never cross, the light cone emanating from the origin. Thus, the frame's coordinate velocity approaches $c$ but never reaches it. At the same time, any light worldline originating from the origin $(0,0)$ after a certain coordinate time will never intersect the object's worldline. From the perspective of the accelerating frame, light from these regions is infinitely redshifted because the coordinate speed of light drops to zero at the horizon (where the metric component $g_{00}$ becomes zero). This is analogous to what happens at the event horizon of a black hole, where an object falling toward the black hole appears to freeze at the horizon for a distant inertial observer.

The non-inertial frame's local basis vectors are $\vec{e}_t$, which is the tangent to the hyperbola at a given event (parallel to the 4-velocity), and the Minkowski orthogonal spatial vector $\vec{e}_x$. Because the global Minkowski 4-position vector $\vec{S}$ (originating from the focal center of the hyperbola) is orthogonal to the hyperbola's tangent, it is entirely parallel to the local spatial basis vector $\vec{e}_x$. Furthermore, because the 4-velocity has a strictly constant invariant magnitude, its derivative (the 4-acceleration) must be Minkowski orthogonal to it. Therefore, while the 4-velocity is aligned with $\vec{e}_t$, the 4-acceleration is entirely aligned with $\vec{e}_x$.

The non-inertial frame's local basis vectors are $\vec{e}_t$, which is the tangent to the hyperbola at a given event (parallel to the 4-velocity), and the Minkowski orthogonal spatial vector $\vec{e}_x$. Because the global Minkowski 4-position vector $\vec{S}$ (originating from the focal center of the hyperbola) is orthogonal to the hyperbola's tangent, its projection onto the local time axis is exactly zero. Consequently, from the point of view of the non-inertial frame's instantaneous basis, the position vector from the origin is given entirely by its spatial component: $\vec{S}=\tilde{x}\vec{e}_x$, where $\tilde{x}$ is the invariant coordinate distance along the instantaneous $\vec{e}_x$ direction (specifically, $\tilde{x}=c^2/a$). Furthermore, because the 4-velocity has a strictly constant invariant magnitude, its derivative (the 4-acceleration) must be Minkowski orthogonal to it. Therefore, while the 4-velocity is aligned with $\vec{e}_t$, the 4-acceleration is entirely aligned with $\vec{e}_x$.

Consider a scenario where two reference frames begin accelerating at the same time and with the same proper acceleration from the perspective of an inertial frame (Bell's Spaceship Paradox). In the inertial frame, [the coordinate distance between them remains a constant](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOmiyAA4o1VxyzzGKzVb6ZqBtYLHOCYsoXv6ADu33c7w&s=100) $L$ throughout their worldlines. However, from the perspective of the rear non-inertial frame's MCIF, the proper distance between them continually grows. Because the rear frame's line of simultaneity (aligned with its $\vec{e}_x$ axis) tilts forward into the future as it accelerates, it intersects the forward frame's worldline at a progressively later proper time. Consequently, in the rear frame's instantaneous rest frame, the forward frame always appears to have accelerated for a longer duration, reaching a higher velocity and thus stretching the distance between them.

### Rindler Coordinates
These hyperbolic trajectories form the basis of the [Rindler coordinate system](https://thumb.wikimedia.org/wikipedia/commons/thumb/5/56/Rindler_chart.svg/1280px-Rindler_chart.svg.png) $(T, X)$, which maps spacetime for uniformly accelerating observers. For a family of hyperbolas intersecting the inertial axis at distances $D, 2D, 3D$, the associated proper accelerations are $c^2/D, c^2/2D, c^2/3D$.

The relationship transforming the Rindler coordinates $(T, X)$ (where the reference observer with acceleration $a$ is at $X=0$) to the global inertial coordinates $(t, x)$ is given by:

$$ct=\left(X+\frac{c^2}{a}\right)\sinh\left(\frac{aT}{c}\right)$$

$$x=\left(X+\frac{c^2}{a}\right)\cosh\left(\frac{aT}{c}\right)$$

In this non-inertial coordinate system, governed by the Rindler metric, inertial worldlines (straight lines in Minkowski space) map to curved trajectories, and light worldlines asymptotically approach the Rindler horizon at $X=-c^2/a$ as coordinate time $T \to \infty$. This demonstrates geometrically how the light cone boundary acts as an absolute horizon for the accelerating observer.

In the global inertial (Minkowski) frame, the accelerating object's spatial coordinate $x$ changes continuously with time $t$ as it traces its hyperbolic worldline. It is in constant motion, and its coordinate velocity $dx/dt$ asymptotically approaches $c$.

When we switch to the Rindler coordinate system $(T, X)$, we are mathematically forcing the coordinate grid to accelerate alongside the object. Depending on how you define the origin of the Rindler chart, the accelerating object is assigned a permanently fixed spatial coordinate:

* **Shifted Origin:** The object is defined to sit exactly at $X=0$.
* **Horizon Origin:** The object is defined to sit exactly at $X=c^2/a$.

In either convention, the spatial coordinate $X$ of the accelerating object is a constant constant scalar.

Note that since the time basis in the Rindler coordinates is the tangent of the hyperbolic curve, which also matches the velocity vector, it means the spatial velocity of the object is 0 in that coordinate system, and therefore at rest:

$$\frac{dX}{dT}=0$$

While the object is kinematically at rest ($dX/dT=0$), the system remains a non-inertial frame. The physical reality of the acceleration is transferred from the object's motion into the geometry of the spacetime metric itself.

In the Rindler frame, an onboard accelerometer still measures a proper acceleration $a$. However, because the object is at rest in these coordinates, this measurement is not interpreted as kinematic acceleration, but rather as the object resisting a fictitious gravitational field. The spatial dependence of the Rindler metric time component, $g_{00}=(1+aX/c^2)^2$, acts mathematically identical to a uniform gravitational potential pulling everything toward the Rindler horizon. The object remains at rest at $X=0$ because it is "supported" against this fictitious field, much like a book resting stationary on a table in Earth's gravity.

### Tying Hyperbolic Motion Back to Force & Acceleration
Consider a situation where we are applying a constant force F and we would like to make note of how momentum changes. As $\mathbf{F} = \frac{d\mathbf{p}}{dt}$, for a constant force applied in one dimension over a coordinate time $t$, the integral is:

$$\int_{0}^{t} F \, dt = \int_{p_0}^{p(t)} dp$$

$$F t = p(t) - p_0$$

If the object is already moving at velocity $v_0$ at $t = 0$, the initial momentum is $p_0 = \gamma_0 m v_0$. The equation becomes:

$$\frac{m v}{\sqrt{1 - (v/c)^2}} - \frac{m v_0}{\sqrt{1 - (v_0/c)^2}} = F t$$

If the block starts from rest ($v_0 = 0$), then $\frac{m v}{\sqrt{1 - (v/c)^2}} = F t$ and rearranging this to solve for $v(t)$ yields the standard equation for relativistic hyperbolic motion.

Using $dx = v(t)dt$ and integrating from $x(0)=0$:

$$x(t) = \int_{0}^{t} \frac{\alpha \tau}{\sqrt{1 + \left(\frac{\alpha \tau}{c}\right)^2}} d\tau$$

Evaluating this integral yields the position function:

$$x(t) = \frac{c^2}{\alpha} \left( \sqrt{1 + \left(\frac{\alpha t}{c}\right)^2} - 1 \right)$$

By algebraically rearranging this trajectory and squaring it, we can group the space and time variables:

$$\left(x(t) + \frac{c^2}{\alpha}\right)^2 - (ct)^2 = \left(\frac{c^2}{\alpha}\right)^2$$

This is the standard geometric equation for a hyperbola ($X^2 - Y^2 = R^2$) in the Minkowski spacetime diagram. While a classical particle under constant force traces a parabola ($x = \frac{1}{2}at^2$), a relativistic particle under constant force traces a hyperbola, forever approaching the light cone $x = ct$ as an asymptote but never crossing it.

## Useful Formulas
$$\begin{bmatrix}ct'\\x'\end{bmatrix}=\begin{bmatrix}\gamma&-\gamma\beta\\-\gamma\beta&\gamma\end{bmatrix}\begin{bmatrix}ct\\x\end{bmatrix}$$

where $\beta=\frac{v}{c}$ and $\gamma=\frac{1}{\sqrt{1-\beta^2}}$

---

The full Lorentz Boost is given by,

$$\Lambda = \begin{bmatrix} \gamma & -\gamma\beta_x & -\gamma\beta_y & -\gamma\beta_z \\ -\gamma\beta_x & 1+(\gamma-1)\frac{\beta_x^2}{\beta^2} & (\gamma-1)\frac{\beta_x\beta_y}{\beta^2} & (\gamma-1)\frac{\beta_x\beta_z}{\beta^2} \\ -\gamma\beta_y & (\gamma-1)\frac{\beta_y\beta_x}{\beta^2} & 1+(\gamma-1)\frac{\beta_y^2}{\beta^2} & (\gamma-1)\frac{\beta_y\beta_z}{\beta^2} \\ -\gamma\beta_z & (\gamma-1)\frac{\beta_z\beta_x}{\beta^2} & (\gamma-1)\frac{\beta_z\beta_y}{\beta^2} & 1+(\gamma-1)\frac{\beta_z^2}{\beta^2} \end{bmatrix}$$

---

$ds^2=(cdt)^2-\sum_i dx_ix^i$ is the invariant spacetime interval in the Minkowski metric.

---

Doppler effect on a receding source, the observed frequency $f_e$ is redshifted by $f_e = f_0 \sqrt{\frac{1 - \beta}{1 + \beta}}$. For an approaching Source ($\beta$ becomes $-\beta$): $f_e = f_0 \sqrt{\frac{1 + \beta}{1 - \beta}}$

---

$$\frac{dt}{d\tau} = \frac{1}{\sqrt{1 - \frac{v^2}{c^2}}} = \gamma$$

---

$$U=\frac{d}{d\tau}(ct, x, y, z)= (c\frac{dt}{d\tau},\frac{dx}{dt}\frac{dt}{d\tau}, \frac{dy}{dt}\frac{dt}{d\tau}, \frac{dz}{dt}\frac{dt}{d\tau})  = \gamma(c, u_x, u_y, u_z)$$

$u_x, u_y, u_z$ is the spatial velocity we are used to from classical mechanics, given by $\frac{dx}{dt}$ etc. 

---

$P=mU=\gamma(mc, mu_x, mu_y, mu_z)=(E/c, p_x, p_y, p_z)$, where we absorb the $\gamma$ factor into the $E$ and spatial $p$ terms. Thus the spatial momentum is actually $\gamma mv$, not $mv$, and  $\frac{E}{c} = P^0 = \gamma mc$

Thus, $p$ is not the usual Newtonian $mv$. That is a low velocity approximation.

---

$P\cdot P$ is conserved and $P\cdot P=(E/c)^2-p^2=(mc)^2$. Rearranging this gives Einstein’s energy-momentum relation: $E^2=(mc^2)^2+(pc)^2$


When a particle is at rest ($p=0$), the equation reduces to $E=mc^2$. For massless particles use $p=h/\lambda$) or $E=pc$.

---


$$\frac{d\gamma}{dt}=\gamma^3\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}$$

---

$$A=\left(\gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c}, \gamma^4\frac{\mathbf{u}\cdot\mathbf{a}}{c^2}\mathbf{u}+\gamma^2\mathbf{a}\right)$$

---

The magnitude of the 4-acceleration in the object's rest frame is given by:

$$A^\mu A_\mu = (A^0)^2 - \vert{}\mathbf{A}\vert{}^2 = 0^2 - \vert{}\boldsymbol{\alpha}\vert{}^2 = -\vert{}\boldsymbol{\alpha}\vert{}^2$$

where $\alpha$ is the proper acceleration. Since the 4-acceleration's magnitude is invariant, it means the magnitude is equal to the above value in any reference frame. 

---

We can also write the 4-acceleration in terms of the proper acceleration by applying a Lorentz boost from the rest frame to an arbitrary frame.

$$A = \left( \gamma\frac{\mathbf{u} \cdot \boldsymbol{\alpha}}{c}, \boldsymbol{\alpha} + \frac{\gamma^2}{\gamma + 1}\frac{\mathbf{u} \cdot \boldsymbol{\alpha}}{c^2}\mathbf{u} \right)$$

Equating this to the previous derivation for the 4-acceleration, we get,

$$a_\parallel = \frac{\alpha_\parallel}{\gamma^3}$$

$$a_\perp = \frac{\alpha_\perp}{\gamma^2}$$

where $a_\parallel$ is the acceleration along the direction of movement of the moving frame, and $a_\perp$ is along a direction perpendicular to it. 

---
 The 4-force is defined as $K = m A = m\frac{dP}{d\tau}$. The invariant length of the 4-force is equal to the length of the proper force, given by $K_\mu K^\mu = -\vert{}\mathbf{F}_{proper}\vert{}^2$.

---

The 4-force can be expressed in terms of the laboratory-frame 3-force $\mathbf{F}$ and velocity $\mathbf{v}$. 

$$K^\mu = \gamma \left( \frac{\mathbf{F} \cdot \mathbf{v}}{c}, F_x, F_y, F_z \right)$$

**Longitudinal component (parallel to velocity):** $\gamma F_x = \gamma F_{proper, x} \implies F_x = F_{proper, x}$

**Transverse components (perpendicular to velocity):** $\gamma F_y = F_{proper, y} \implies F_y = \frac{F_{proper, y}}{\gamma}$ and $\gamma F_z = F_{proper, z} \implies F_z = \frac{F_{proper, z}}{\gamma}$

---

The relationship between the 3-force and 3-acceleration, the relativistic equivalent of Newton's Second Law $F = ma$ (which is a low velocity approximation):

$$\mathbf{F} = \gamma m\mathbf{a} + \frac{\gamma^3 m}{c^2}(\mathbf{v} \cdot \mathbf{a})\mathbf{v}$$

**Transverse Acceleration (Force perpendicular to velocity):** If the force is applied at a right angle to the motion, $\mathbf{v} \cdot \mathbf{a} = 0$. The second term vanishes, yielding: $\mathbf{F} = \gamma m\mathbf{a}$. The particle's effective inertia is $\gamma m$.

**Longitudinal Acceleration (Force parallel to velocity):** If the force is applied in the exact direction of motion, $\mathbf{v}$ and $\mathbf{a}$ are parallel, so $\mathbf{v} \cdot \mathbf{a} = va$. The equation simplifies (using $\gamma^2 = 1/(1 - v^2/c^2)$) to: $\mathbf{F} = \gamma^3 m\mathbf{a}$. The particle's effective inertia is $\gamma^3 m$.

---
The Lorentz transformation naturally mapped to hyperbolic geometry:

$$\begin{bmatrix}ct'\\x'\end{bmatrix}=\begin{bmatrix}\cosh\phi&-\sinh\phi\\-\sinh\phi&\cosh\phi\end{bmatrix}\begin{bmatrix}ct\\x\end{bmatrix}$$

Here, $\phi$ is the rapidity, defined by the relation $\tanh\phi=v/c=\beta$. 

---
Hyperbolic formulation allows relative velocities to be calculated via the simple addition of rapidities: $\phi_{AC}=\phi_{AB}+\phi_{BC}$, bypassing the non-linear velocity addition formula $v=\frac{v_1+v_2}{1+\frac{v_1v_2}{c^2}}$

---

The relationship transforming the Rindler coordinates $(T, X)$ (where the reference observer with acceleration $a$ is at $X=0$) to the global inertial coordinates $(t, x)$ is given by:

$$ct=\left(X+\frac{c^2}{a}\right)\sinh\left(\frac{aT}{c}\right)$$

$$x=\left(X+\frac{c^2}{a}\right)\cosh\left(\frac{aT}{c}\right)$$

Depending on how you define the origin of the Rindler chart, the accelerating object is assigned a permanently fixed spatial coordinate:

* **Shifted Origin:** The object is defined to sit exactly at $X=0$.
* **Horizon Origin:** The object is defined to sit exactly at $X=c^2/a$.

## Classical Field Theory

## Principle of Least Action in Special Relativity

Let us start by applying the principle to a free particle (i.e. it has no forces acting on it) in non-relativistic physics. Since $L = T - V$ and $V$ can be ignored as there is no force and therefore no gradient in the potential, we can set $L = T$, which is just the kinetic energy. $L = \frac{1}{2}mv^2$, or written in component notation, $L = \frac{1}{2}m\dot{x}_i\dot{x}^i$.

Applying the Euler-Lagrange equations gives us the equations of motion using $t$ as the parameter:

$$\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{x}^i}\right) - \frac{\partial L}{\partial x^i} = 0$$

Since $\frac{\partial L}{\partial x^i} = 0$ (there is no coordinate dependence) and $\frac{\partial L}{\partial \dot{x}^i} = m\dot{x}_i$, the equation of motion reduces to $m\ddot{x}_i = 0$.

When we move to relativistic particles, we start with the spacetime interval $ds^2$. The Action is proportional to the proper time along the worldline, $S \propto \int ds$. Using a generic parameter $\sigma$ to parameterize the path, and adopting the Minkowski metric $\eta_{\mu\nu}$, we can write the Lagrangian as:

$$L = -mc\sqrt{-\eta_{\mu\nu}\dot{x}^\mu\dot{x}^\nu}$$

where $\dot{x}^\mu = \frac{dx^\mu}{d\sigma}$.

The Action then becomes:

$$S = \int_{\sigma_1}^{\sigma_2} L d\sigma = -mc \int_{\sigma_1}^{\sigma_2} \sqrt{-\eta_{\mu\nu}\frac{dx^\mu}{d\sigma}\frac{dx^\nu}{d\sigma}} d\sigma$$

### Properties of a "Successful" Action
A few things to note about the Action:

The $mc$ term is needed to ensure the Action has dimensions of energy $\times$ time.
    
The Action is Lorentz invariant since all the dummy indices are contracted, which means all the terms are scalars, which are naturally Lorentz invariant.    

We have used $\sigma$ as the parameter of the functionals. In the non-relativistic case, we used time $t$, however with Special Relativity, coordinate time depends on the reference frame, so which $t$ should we use? One obvious choice is the proper time $\tau$ which is invariant. But it turns out that in this Action, we can choose any parameter and get away with it. The only constraint is the mathematical one that it monotonically increases along a worldline, because that is literally the job of the parameter.
    
This is because the two $d\sigma$ terms in the denominator in the square root cancel out the one on the outside. So if we chose a new parameter $\lambda$, we can rewrite all the derivatives in terms of $\lambda$, and they would cancel out the $\frac{d\lambda}{d\sigma}$ term on the outside.

$$\tilde{S} = -mc \int_{\tilde{\sigma}_1}^{\tilde{\sigma}_2} d\tilde{\sigma} \sqrt{-\eta_{\mu\nu} \frac{dx^\mu}{d\tilde{\sigma}} \frac{dx^\nu}{d\tilde{\sigma}}} = -mc \int_{\sigma_1}^{\sigma_2} d\sigma \frac{d\tilde{\sigma}}{d\sigma} \sqrt{-\eta_{\mu\nu} \frac{dx^\mu}{d\sigma} \frac{dx^\nu}{d\sigma} \left( \frac{d\sigma}{d\tilde{\sigma}} \right)^2} = S$$

Why does this matter? The Action must be reparameterization invariant because when a mathematical quantity is parameter-independent, it means the final numerical value you calculate does not depend on how you choose to label or parametrize the path. The value is not an artifact of the choice of coordinate system. It must be a direct property of the geometric curve itself. It describes a real physical reality (like the actual aging of a particle or the true spacetime distance between events) rather than a mathematical illusion created by a lucky coordinate choice.

Additionally, because the parameter $\sigma$ is physically meaningless, it acts as a "gauge" degree of freedom. This grants us the mathematical liberty to choose whatever parameter makes solving our differential equations the easiest for a given problem.

The Action must be Lorentz invariant because the equations of Special Relativity must hold i.e. when we transform the coordinates of an inertial observer, the physics looks exactly the same, and the metric doesn't morph into a complicated, position-dependent tensor. 

To see the difference between what Lorentz invariance adds to the table that reparameterization invariance doesn't, imagine we created a completely geometric, reparameterization-independent action, but deliberately broke Lorentz invariance by using a Euclidean metric $\delta_{\mu\nu} = \text{diag}(1, 1, 1, 1)$ instead of the Minkowski metric:

$$S_{\text{wrong}}=\int \sqrt{\delta_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda}} d\lambda$$

This action is perfectly geometric and independent of our mathematical choices of path labeling ($\lambda$). However, it describes a universe where space and time are treated exactly the same, meaning the speed of light is not constant, there is no cosmic speed limit, and moving observers would see the laws of physics change. In a Euclidean metric, the distance between any two distinct points is strictly positive, meaning there are no null paths ($ds^2=0$) and therefore no absolute structure separating past, future, and elsewhere.

**Aside:** While we have $4$ spacetime coordinates and therefore can derive $4$ equations of motion, we actually only have $3$ physical degrees of freedom. All $4$ coordinates are not dynamically independent of each other. There is redundancy among them. This comes from the constraint of the constant magnitude of the 4-velocity which satisfies the constraint: $\eta_{\mu\nu}u^\mu u^\nu = -c^2$. This binds the temporal and spatial velocities together, reducing the system by one degree of freedom. The reduction of a degree of freedom is the direct consequence of the "gauge" degree of freedom.

---

One more requirement we must meet when choosing a Lagrangian or action is that it reduces to Newton's equations of motion under the low-velocity approximation. This can be seen to be true when we parameterize the action by proper time $\tau$, and can be written as:

$$S = -mc \int \sqrt{ c^2 \left(\frac{dt}{d\tau}\right)^2 - \sum_i \left(\frac{dx^i}{dt}\frac{dt}{d\tau}\right)^2 } d\tau$$

By factoring out the $\left(\frac{dt}{d\tau}\right)^2$ to cancel with the $d\tau$ integration measure, and pulling $c^2$ out of the square root, we get:

$$S = -mc^2 \int \sqrt{1 - \frac{\dot{x}^2}{c^2}} dt$$

Taking the low-velocity approximation and applying the binomial Taylor series expansion ($\sqrt{1 - \epsilon} \approx 1 - \frac{\epsilon}{2}$), the Action becomes:

$$S \approx \int \left( -mc^2 + \frac{1}{2}m\dot{x}^2 \right) dt$$

Because the Euler-Lagrange equations operate via derivatives, adding or subtracting a constant to the Lagrangian does not change the resulting equations of motion. We can then ignore the constant rest mass energy term ($-mc^2$), and the action reduces to the non-relativistic action we saw earlier: $S_{\text{NR}} = \int \frac{1}{2}m\dot{x}^2 dt$

### Parameterization with Proper Time
Since $ds^2=-c^2d\tau^2$, if we parameterize the Action with $\tau$ the Action can be written as $S=-mc^2\int d\tau$. This makes sense since Action is after all energy $\times$ time. The natural choice for energy of a free particle is its rest mass energy, while the natural choice for a free particle is to measure time in its rest frame, which is proper time. 

Extremizing this action means the particle will follow the path through spacetime that maximizes the proper time i.e. time in its rest frame. Note that this is _not_ the same as saying the clock in a rest frame measures the least time, which is a statement about how the world line changes due to coordinate change. In contrast, extremizing the action is about an equation of motion. What path does the free particle follow in spacetime, or alternatively what is the shape/geometry of the particle's worldline when it is simply floating in space. 

The action principle is in fact saying that a free particle travels in a straight line in spacetime. This is a geodesic. Any curve or deviation (acceleration) decreases the elapsed proper time. This is the Twin Paradox. Imagine two twins starting at Event A and meeting again at Event B. Twin 1 floats freely through space without firing any thrusters. This is an inertial, straight-line path in spacetime. Twin 2 fires thrusters, accelerating near the speed of light, turning around, and returning to meet Twin 1 at Event B. Because Twin 2 accelerated, they underwent severe time dilation relative to the inertial frame. When they meet at Event B, Twin 2's wristwatch will have ticked significantly less than Twin 1's wristwatch.

### Canonical Momentum is 4-Momentum
The invariant spacetime interval $ds^2$ is related to proper time $\tau$ by $ds^2=-c^2d\tau^2$. We can also write $ds^2$ in terms of the metric:

$$-c^2d\tau^2=\eta_{\mu\nu}dx^\mu dx^\nu$$

$$cd\tau=\sqrt{-\eta_{\mu\nu}dx^\mu dx^\nu}$$

Now, divide both sides by the arbitrary parameter differential $d\sigma$:

$$c\frac{d\tau}{d\sigma}=\sqrt{-\eta_{\mu\nu}\frac{dx^\mu}{d\sigma}\frac{dx^\nu}{d\sigma}}$$

Notice that the right side of this equation is the square root term from the Lagrangian. Therefore, we can substitute this into the Lagrangian:

$$L=-mc\left(c\frac{d\tau}{d\sigma}\right)=-mc^2\frac{d\tau}{d\sigma}$$

$$\frac{d\tau}{d\sigma}=-\frac{L}{mc^2}$$

The canonical momentum conjugate is $p_\mu=\frac{\partial L}{\partial\dot{x}^\mu}$

Using the Lagrangian $L=-mc(-\eta_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta)^{1/2}$:

$$p_\mu=-mc\left[\frac{1}{2}(-\eta_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta)^{-1/2}\right]\frac{\partial}{\partial\dot{x}^\mu}(-\eta_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta)$$

Using the chain rule, the derivative of the term inside the parenthesis is $-2\eta_{\mu\nu}\dot{x}^\nu$. Substituting this back in:

$$p_\mu=-mc\left[\frac{1}{2\sqrt{-\eta_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta}}\right](-2\eta_{\mu\nu}\dot{x}^\nu)$$

$$p_\mu=\frac{mc\eta_{\mu\nu}\dot{x}^\nu}{\sqrt{-\eta_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta}}$$

The denominator is equal to $c\frac{d\tau}{d\sigma}$. We substitute this into our momentum equation:

$$p_\mu=\frac{mc\eta_{\mu\nu}\frac{dx^\nu}{d\sigma}}{c\frac{d\tau}{d\sigma}}$$

The $c$ terms cancel, and the $d\sigma$ terms in the differentials cancel out via the chain rule ($\frac{dx^\nu}{d\sigma} \frac{d\sigma}{d\tau} = \frac{dx^\nu}{d\tau}$):

$$p_\mu=m\eta_{\mu\nu}\frac{dx^\nu}{d\tau}$$

This is the covariant canonical momentum (index down). To compare it to the contravariant 4-momentum $P^\mu$ (index up), we raise the index using the inverse metric tensor $\eta^{\rho\mu}$:

$$p^\rho=\eta^{\rho\mu}p_\mu=m\eta^{\rho\mu}\eta_{\mu\nu}\frac{dx^\nu}{d\tau}$$

Since $\eta^{\rho\mu}\eta_{\mu\nu}$ is the Kronecker delta $\delta^\rho_\nu$ (the identity matrix), it simply swaps the index from $\nu$ to $\rho$:

$$p^\rho=m\frac{dx^\rho}{d\tau}$$

Relabeling the dummy index $\rho$ back to $\mu$ yields:

$$p^\mu=m\frac{dx^\mu}{d\tau}$$

This is just the definition of 4-momentum. So, the canonical momentum derived from the action principle is physically identical to the kinematic 4-momentum: $P^\mu \equiv p^\mu$

### Action with Potentials in Electromagnetism

If we have to add a potential in order to account for forces operating on the particle (i.e., it is no longer a free particle), we need to add a $V(x)$ term to the Lagrangian. How do we do this while ensuring it is reparameterization and Lorentz invariant?

For the first requirement, using a term that depends on $\dot{x}$ will do the job, as the $d\sigma$ in the denominator cancels out the $d\sigma$ integration parameter (just like we saw in the free particle case). For Lorentz invariance, we need to contract the indices. Together, we can propose an action:

$$S_1 = \int_{\sigma_1}^{\sigma_2} \left[ -mc \sqrt{-\eta_{\mu\nu} \frac{dx^\mu}{d\sigma} \frac{dx^\nu}{d\sigma}} + qA_\mu(x) \dot{x}^\mu \right] d\sigma$$

Here $q$ is added as a coupling factor between $A$ and $\dot{x}$ and, as can be seen below, will turn out to be the charge in the electromagnetic equations.

If we pick the worldline parameter to coincide with the time of some inertial observer, $\sigma = t$, so that $dx^0/d\sigma = c$. If we write the contravariant 4-potential as $A^\mu(x) = (\phi(x)/c, \mathbf{A}(x))$, lowering the index gives $A_\mu(x) = (-\phi(x)/c, \mathbf{A}(x))$. Contracting this with $\dot{x}^\mu = (c, \dot{\mathbf{x}})$ and substituting it into the integral, we find:

$$S_1 = \int_{t_1}^{t_2} \left[ -mc^2 \sqrt{1 - \frac{\dot{\mathbf{x}}^2}{c^2}} - q\phi(x) + q\mathbf{A}(x) \cdot \dot{\mathbf{x}} \right] dt$$

This is essentially the electromagnetic Action, from which the Lorentz force law can be derived.

### Action with Potentials in Gravity

For gravity, we do something a little different. We write the action as:

$$S_2 = \int_{t_1}^{t_2} \left[ -mc^2 \sqrt{1 + \frac{2\Phi(x)}{c^2} - \frac{\dot{\mathbf{x}}^2}{c^2}} \right] dt$$

If we Taylor expand the square root, assuming that $\vert{}\dot{\mathbf{x}}\vert{} \ll c$ and that $2\Phi(x) \ll c^2$, then the leading terms give:

$$S_2 \approx \int_{t_1}^{t_2} \left[ -mc^2 + \frac{1}{2}m\dot{\mathbf{x}}^2 - m\Phi(x) \right] dt$$

Why did we choose this action? One motivation is that the low-velocity approximation gives us a potential energy term that is proportional to $m$ ($V = m\Phi$), which is exactly the definition of Newtonian gravitational potential energy.

How do we ensure this action is reparameterization invariant and preserves spacetime symmetries? The $1$ in the Taylor approximation actually originates from the time component of the flat Minkowski metric, $-\eta_{00}$. To incorporate gravity, we promote this constant to a coordinate-dependent metric component, $-g_{00}(x) = 1 + \frac{2\Phi(x)}{c^2}$.

Of course, once we've done this to the time component, we are no longer in Minkowski spacetime. We use a general metric tensor $g_{\mu\nu}$. Because $g_{00}$ is dependent on the coordinates, it means that to maintain **general covariance** (invariance under arbitrary coordinate transformations, which replaces global Lorentz invariance in General Relativity), we need to ensure the spatial and off-diagonal components of the metric can also dynamically respond to spacetime curvature.

Just as in the previous two situations, the fully contracted spacetime velocity terms are parameter invariant. This indicates that we can write a generalized covariant line element and place it directly inside our Lagrangian:

$$S_2 = -mc \int_{\sigma_1}^{\sigma_2} \sqrt{-g_{\mu\nu}(x) \frac{dx^\mu}{d\sigma} \frac{dx^\nu}{d\sigma}} d\sigma$$

This describes a particle moving in curved spacetime. The components of the metric $g_{\mu\nu}$ are deduced from the Einstein Field Equations, but even without them, we can see that modifying the $g_{00}$ term correctly reduces to Newtonian motion in the low-velocity, weak-field approximation as seen above.

Applying the Euler-Lagrange equations, we see that just as the free-particle non-relativistic action yields $m\ddot{x}_i = 0$, the curved spacetime action yields free-fall along geodesics. yields the geodesic equation: 

$$\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0$$

where the Christoffel symbols are given by

$$\Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\rho} \left( \partial_\mu g_{\nu\rho} + \partial_\nu g_{\rho\mu} - \partial_\rho g_{\mu\nu} \right)$$

## References
- [Eigenchris Relativity Playlist](https://www.youtube.com/playlist?list=PLJHszsWbB6hqlw73QjgZcFh4DrkQLSCQa)
- Ch 01 of Classical Field Theory by Joel Franklin
- [Lecture 01](https://davidtong.org/pdfs/teaching/general-relativity/gr1.pdf) of David Tong's General Relativity Notes
- Special Relativity and Classical Field Theory - The Theoretical Minimum by Leonard Susskind
