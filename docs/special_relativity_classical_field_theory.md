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

## The Spacetime Interval
Using the Lorentz transformation, we can see that what is called the spacetime interval squared $ds^2=(c.dt)^2-dx^2$ is the same in all reference frames. Another way of saying that is that it is invariant under coordinate transformation. Each of the coordinates in this equation is actually an infinitesimal difference between two events. This geometry is encoded in the Minkowski metric tensor. Using the $(+, -, -, -)$ signature convention, the diagonal elements are $(1, -1, -1, -1)$, and all off-diagonal elements are 0.

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

Thus, the invariant magnitude squared of the 4-velocity is always constant: $U\cdot U=c^2$.

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

Consider a scenario where two reference frames begin accelerating at the same time and with the same proper acceleration from the perspective of an inertial frame (Bell's Spaceship Paradox). In the inertial frame, the coordinate distance between them remains a constant $L$ throughout their worldlines. However, from the perspective of the rear non-inertial frame's MCIF, the proper distance between them continually grows. Because the rear frame's line of simultaneity (aligned with its $\vec{e}_x$ axis) tilts forward into the future as it accelerates, it intersects the forward frame's worldline at a progressively later proper time. Consequently, in the rear frame's instantaneous rest frame, the forward frame always appears to have accelerated for a longer duration, reaching a higher velocity and thus stretching the distance between them.

### Rindler Coordinates
These hyperbolic trajectories form the basis of the Rindler coordinate system $(T, X)$, which maps spacetime for uniformly accelerating observers. For a family of hyperbolas intersecting the inertial axis at distances $D, 2D, 3D$, the associated proper accelerations are $c^2/D, c^2/2D, c^2/3D$.

The relationship transforming the Rindler coordinates $(T, X)$ (where the reference observer with acceleration $a$ is at $X=0$) to the global inertial coordinates $(t, x)$ is given by:

$$ct=\left(X+\frac{c^2}{a}\right)\sinh\left(\frac{aT}{c}\right)$$

$$x=\left(X+\frac{c^2}{a}\right)\cosh\left(\frac{aT}{c}\right)$$

In this non-inertial coordinate system, governed by the Rindler metric, inertial worldlines (straight lines in Minkowski space) map to curved trajectories, and light worldlines asymptotically approach the Rindler horizon at $X=-c^2/a$ as coordinate time $T \to \infty$. This demonstrates geometrically how the light cone boundary acts as an absolute horizon for the accelerating observer.

In the global inertial (Minkowski) frame, the accelerating object's spatial coordinate $x$ changes continuously with time $t$ as it traces its hyperbolic worldline. It is in constant motion, and its coordinate velocity $dx/dt$ asymptotically approaches $c$.

When we switch to the Rindler coordinate system $(T, X)$, we are mathematically forcing the coordinate grid to accelerate alongside the object. Depending on how you define the origin of the Rindler chart, the accelerating object is assigned a permanently fixed spatial coordinate:

* **Shifted Origin:** The object is defined to sit exactly at $X=0$.
* **Horizon Origin:** The object is defined to sit exactly at $X=c^2/a$.

In either convention, the spatial coordinate $X$ of the accelerating object is a constant constant scalar.

Note that since the time basis in the Rindler coordinates is the tangent of the hyperbloic curve, which also matches the velocity vector, it means the spatial velocity of the object is 0 in that coordinate system, and therefore at rest:

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

## References
- [Eigenchris Relativity Playlist](https://www.youtube.com/playlist?list=PLJHszsWbB6hqlw73QjgZcFh4DrkQLSCQa)
- Ch 01 of Classical Field Theory by Joel Franklin
- [Lecture 01](https://davidtong.org/pdfs/teaching/general-relativity/gr1.pdf) of David Tong's General Relativity Notes
- Special Relativity and Classical Field Theory - The Theoretical Minimum by Leonard Susskind
