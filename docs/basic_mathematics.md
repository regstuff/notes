# 0. Basic Mathematics

## Differential Geometry

### Intuition

Before the mathematical formalism of differential geometry, it helps to understand why differential geometry is needed. For example, if we wanted to setup a coordinate system for the surface of the Earth, you could zoom out into space, create a 3D coordinate system and establish the coordinates in that grid for every point on the Earth's surface. But what if I wanted to do the same thing for the universe as a whole, which is a requirement in General Relativity. There is no place to zoom out to from the universe. We are forced to figure out how to setup a coordinate system, distance measurement tools and a description of the space from within the space itself.

The "low-hanging fruit" method to do that is to describe each point in terms of its immediate neighbours. That should remind you of differentiation, which is more or less what we do, and the reason for the name differential geometry. Essentially, we will be describing every point on the $n$-dimensional surface by the slope or rate of change of the surface along any $n$ linearly independent directions. This way, I don't need any origin defined for my coordinate grid. After all, what is an origin? It is some arbitrary point that we choose and then go ahead and define every point by the "difference" of that point from the origin along various directions. Instead of an origin, in differential geometry I choose to define my "difference" with respect to my neighbouring points. If I know how each point changes with respect to its neighbour, I can iteratively "walk" point by point everywhere on my surface and map out the whole surface.

This is analogous to the situation where you are plonked onto the Earth's surface without any knowledge of what it actually looks like when you zoom out, and are told to create a description and measure various aspects of the Earth's surface. So let's do exactly that.

We start off at some arbitrary point $p$ on the surface (the fact that it is arbitrary will be important later on. Stay tuned). In the Earth's case, this is a 2D surface: at any point you need two independent coordinates to describe any point in the locality. For the universe as a whole it will be a 4D surface. In general, an $n$-dimensional surface is called a manifold.

I have no measurement scale of meters or centimeters etc. I don't know what the rest of the manifold looks like, except that locally around me, it looks flat. In the kind of differential geometry that is relevant for General Relativity, we assume that any manifold, which may be curved and bumpy on the whole, will be flat locally at every point i.e. whatever point you pick, if you zoom in enough, you will find the manifold looks flat in the locality of the point. Mathematically, this local flat space is the tangent space at that point. That makes sense. The tangents are straight lines at every point, so if the manifold is $n$-dimensional, it would have $n$ linearly independent tangents at every point which form the basis of what is called the Tangent Space at every point.

Back to our point $p$, we use these $n$ linearly independent tangent vectors as the basis of our coordinate system. As mentioned, we don't actually have any measurement scale, so we simply say that each of the tangent vectors are unit vectors, and that now gives us some measurement basis.

But I still only have one tick on my scale. I'd like to be able to have as many ticks as I want so that I can measure anything, no matter how big. So I construct what is called a covector basis, which is a tick counter. These are a set of linear counting machines (think of them as contour lines) designed to output the number $1$ when fed my chosen unit tangent vectors. In this local grid, if I feed a vector to the covector machine, it will output the number of ticks for each basis coordinate that the vector covers. I have one tick counter for each basis vector, and so the number of covector bases equals the number of vector bases. These two spaces are called dual spaces. Going back to our contour lines analogy, we measure how many contour lines of some covector basis a vector pierces, and that tells us the length of the vector along that coordinate.

To establish geometry, I define the metric tensor at this point. I do this by claiming my chosen basis vectors are perfectly orthogonal, so they don't mix with each other in this local patch. We have already claimed that our unit vectors at this local patch are one unit long, so we include that in our metric definition. By making this claim, I set the dot products of all the basis vectors such that the metric tensor evaluates to the Minkowski metric, $g_{\mu\nu} = \eta_{\mu\nu}$.

Now that I have a registry of basis dot product values, I can calculate the dot product of any two vectors, which means I can find the lengths of vectors as well as angles between them.

The choice to define the metric tensor this way is not set in stone. Defining it this way means we have chosen a typical Cartesian coordinate system, the flat, orthogonal x,y (and z and whatever else) that we are used to in most graphs. More rigorously, in 4D this is called a Lorentz Coordinate system.

If I suddenly decide to change my coordinate system at this point to something else, like polar coordinates, I would convert my previous unit distance to this new coordinate system with the help of the Jacobian matrix. My covector machines would also change, and so would my metric tensor, absorbing the geometric stretching via the Jacobian. The metric tensor would not look like a Minkowski metric anymore.

In differential geometric terminology, the choice of the flat orthogonal coordinates at some point is called the Riemann Normal Coordinate (RNC) grid at this location. A theorem of differential geometry says that given any smooth manifold, you can pick any point on it and then choose a coordinate system such that the metric will look Minkowski at that point. Note that at every other point as well, the metric will be flat because we said right in the beginning that we work only with manifolds that look locally flat. But the metric components will not look like the Minkowski metric because the coordinate system at every other point would be warped out of shape thanks to the topology of the space or simply because we have chosen some other coordinate system at that point other than the flat orthogonal Lorentz coordinates.

---

**Aside:** A critical mathematical condition that defines RNCs is that the first derivatives of the metric are strictly zero at $p$ ($\partial_\alpha g_{\mu\nu} = 0$). This is the mathematical embodiment of the Equivalence Principle. It guarantees that locally, you feel no gravitational acceleration (Christoffel symbols vanish). Gravity (curvature) only appears in the second derivatives.

---

Let's take a step back and look at what we've managed so far. We've accurately described each point with respect to its neighbours and we now have a mechanism to measure angles and distances in this local neighbourhood. Now all that's left is to iteratively walk all over my surface and apply this mechanism from neighbouring point to neighbouring point.

So let's move a little to an adjacent point $q$ on my manifold. One point to note is that we assume that our surface doesn't pinch or warp in such a way that it is an n-dimensional surface at one point but an m-dimensional one at some other point. We assume that it covers n dimensions everywhere. That of course doesn't mean that it is flat throughout. It is only flat locally. On the whole, as you step from one local patch to another, you might find you have to twist and turn! 

Now I am faced with a choice. Note that in mathematics, the metric tensor is something that is defined globally across the manifold by the mathematician. They would say, the metric is a Minkowski metric everywhere, or it is the Schwarzschild metric because we are near a black hole. The metric is given to us. In physics, gravity decides the metric. Spacetime is a manifold, and the presence of mass and energy dynamically warps that spacetime. This warping is encoded in the metric tensor (or rather, its deviation from a flat metric). So physics hands us the metric. And this is why we have to make a choice now.

Before I move to the new point $q$, I carry a copy of my grid from the previous point, being careful to keep the vectors parallel to themselves. This is called parallel transport. At $q$, let us say I choose to look at my new tangent space and then define a new coordinate system here as well along with all the associated machinery. Then I compare it with my copy of the previous grid. This tells me how the old coordinate grid and the new one are related. So I've established a connection between the two points, which also happens to be the correct technical terminology for this sort of thing: an affine connection. 

I could define a new metric here just like I did at the earlier point, but since I chose to define a completely new coordinate grid, this new metric tensor wouldn't be the same as the older one. So while I can get along just fine in either local patch separately, my measurements of distances and angles change between patches. This is not what we experience in reality. Making a measurement of the mass of an electron gives the same value everywhere and at all times.

The other choice is I set up my new local coordinate grid at $q$ such that when I create my measurement apparatus with the inner products of the new basis vectors, they are compatible with what I had at $p$. This is called choosing a metric-compatible connection, which is what we usually do in general relativity. 

**Note:** Hermann Weyl in 1918 constructed a geometry where the metric was not compatible with the connection, meaning lengths changed as they were transported. He showed that you could calculate this change by integrating a vector field along the path, which he brilliantly identified as the electromagnetic vector potential $A_\mu$. Mathematically, it is a beautiful, fully self-consistent system.The reason we reject this framework in General Relativity is because tit doesn't match with the reality we see that measurements everywhere and always are the same.

---

**Aside:** If you parallel transport a vector around a closed loop and it returns pointing in a different direction, that discrepancy is the definition of the intrinsic curvature of a space (measured by the Riemann curvature tensor). Think of what would happen if you start at the North Pole, walk to the equator along the Prime Meridian, then walk a quarter of the way around the Earth along the equator, and then turn North and head back to the pole again. You would be facing away from the Prime Meridian, which proves that the Earth's surface is not flat. It has soem curvature.

---

Note that my metric tensor itself is unchanged. Only its components at this new point have changed because the coordinate basis vectors have been warped. If I choose a metric compatible connection, tben the components change in sync with the coordinate basis vectors so that all my measurements are compatible with measurements on the rest of the manifold.

Note that at every point on the manifold, the metric is locally a flat metric. This harks back to our point about the Riemann Normal Coordinates, where we said the metric is flat locally at every point, but it might not look that way when we check the components because the coordinate system is warped.

And going back to our initial point $p$, where we said the point is arbitrary, we could just as well have chosen to start our journey at $q$ or anywhere else for that matter and created the RNC at that point, which ties back to the theorem we mentioned earlier that we can establish a RNC at any point by choosing the right coordinate grid there.

And one last point, the fact that the coordinate grids are connected in such a way that our metric tensor is valid at both points means the connection is metric-compatible. The earlier choice we made of a totally new grid at the new point was not metric-compatible. In General Relativity we almost always use a metric-compatible connection, and more specifically a connection known as the Levi-Civita connection which is also torsion-free.

And that's it. Now you have a mechanism to "connect" any two points of the manifold, and once at a point, to use the metric tensor and the locally flat tangent space to get stuff done.

### An Analogy to Introduce Terminology

Imagine the surface of the Earth. This physical surface is the topology we are interested in. To start with, all we can see is a 50,000-ft overview. Are there any "holes" in the mountain, i.e. does it happen to be cracked right down to the base.

Now, pick a specific physical location on Earth, such as the exact summit of Mount Everest. Let's call this physical point $p$. Let's say we are interested in the temperature (coz it gets cold up there!). This is a scalar function that we might be interested in. $f(p)$ is the actual, physical temperature you would feel standing at the summit of Everest (say, $-20^\circ\text{C}$). Notice that the temperature $f$ exists completely independently of any maps, grids, or coordinate systems. The function $f$ maps a physical piece of rock ($p \in M$, where $M$ is the underlying topological space) to a real number ($-20 \in \mathbb{R}$).

To do calculus, like calculating the temperature gradient (how fast it gets colder as you walk north), we cannot plug "pieces of rock" into derivatives. We need numbers. So, we introduce a coordinate system, $\phi_\alpha$. Let's say $\phi_\alpha$ is the standard GPS system (Latitude and Longitude). The function $\phi_\alpha$ maps the physical piece of rock to a pair of numbers in $\mathbb{R}^2$: $\phi_\alpha(p) = (27.98^\circ, 86.92^\circ)$.

The inverse function $\phi_\alpha^{-1}$ does the exact opposite. If you feed $\phi_\alpha^{-1}$ the numbers $(27.98^\circ, 86.92^\circ)$, it outputs the physical location: the summit of Mount Everest.

This grid around the locality of Everest's summit is called a chart. We stitch together charts of all other points on the manifold, such as Everest basecamp, the Mariana Trench etc., to get an atlas. The topological space along with the atlas define a manifold, $M$.

Why must charts be local, and why do we need an atlas? If you try to map the entire surface of the Earth using a single 2D grid like latitude and longitude, the mathematics will inevitably break down in two ways:

**Coordinate Singularities:** What is the longitude at the exact North Pole? It is undefined. All longitude lines converge there. If you try to calculate a vector derivative at the pole using spherical coordinates, the equations will output infinity or divide by zero.

**Discontinuities:** At the International Date Line (or the $180^\circ$ meridian), the longitude suddenly jumps from $+180^\circ$ to $-180^\circ$. The coordinate map is torn; it is not continuous.

These are not physical problems with the Earth. This is purely a mathematical failure of the coordinate chart. Topologically, it is impossible to map the surface of a sphere to a flat sheet of paper ($\mathbb{R}^2$) without tearing it or creating a singularity.

Because no single chart can safely cover the entire manifold, you must use a collection of smaller, local charts: a Cartesian grid for the region around Mount Everest, another might be a polar coordinate grid looking straight down at the North Pole (where the pole is at coordinate $(0,0)$, completely avoiding the spherical coordinate singularity), and a third might cover the Pacific Ocean, smoothly bridging the Date Line. An atlas is simply the complete collection of these local charts that covers the whole manifold, such that the transition maps between charts must be infinitely differentiable (we explain what that means next).

Assume we have two different surveyors mapping the same region of the Earth:

1.  **Surveyor $\alpha$** uses a standard GPS grid: latitude $\theta$ and longitude $\lambda$. Their coordinate chart $\phi_\alpha$ maps a physical piece of rock $p$ to the numbers $(\theta, \lambda)$.
    
2.  **Surveyor $\beta$** uses a flat topographical map grid: Easting $x$ and Northing $y$ (measured in kilometers from a local origin). Their coordinate chart $\phi_\beta$ maps that same physical rock $p$ to the numbers $(x, y)$.
    
Let us say we want to figure out how to go from the GPS grid to the paper map. You start with a pair of numbers from Surveyor $\alpha$'s grid, say $(27.98^\circ, 86.92^\circ)$. You feed these numbers into the inverse map $\phi_\alpha^{-1}$. This takes the numbers and locates the physical piece of rock $p$ on the actual mountain. You immediately feed that physical rock $p$ into $\phi_\beta$. This outputs the coordinates of that rock on Surveyor $\beta$'s grid, say $(596.2, 3094.1)$. Therefore, the combined function $\phi_\beta \circ \phi_\alpha^{-1}$ is the coordinate conversion formula:

$$(x, y) = \phi_\beta(\phi_\alpha^{-1}(\theta, \lambda))$$

Each point on the map would be a one-to-one mapping with some GPS coordinate, and therefore invertible, i.e., we can go from the map to GPS and vice versa without ambiguity. This means the two charts are homeomorphic with each other. We also say this transition map is perfectly smooth (or $C^\infty$) if the equations calculating $x(\theta, \lambda)$ and $y(\theta, \lambda)$ are infinitely differentiable. There are no sharp corners, tears, or sudden jumps in the mathematical conversion between the two grids. If you were to graph the grid lines of $(\theta, \lambda)$ on top of the $(x, y)$ map, the lines would curve gently and continuously. If the smooth criterion is fulfilled, the two atlases are upgraded to being diffeomorphic with each other.

Diffeomorphism is important in physics. If the transition map is not smooth, then Surveyor $\beta$ may calculate a temperature gradient that suddenly spikes to infinity or becomes undefined. Surveyor $\beta$ would conclude there is an unphysical "wall of heat" or a physical singularity on the mountain. But Surveyor $\alpha$ does not see this singularity in their grid. This violates general covariance: physical reality (the temperature on the mountain) cannot have a singularity simply because of the way we drew our map grids. By demanding that $\phi_\beta \circ \phi_\alpha^{-1}$ is $C^\infty$, we mathematically guarantee that all transition derivatives are well-behaved.

Note that we may not actually need the transition to be infinitely differentiable. We may only ever go to the second derivatives of the metric (Riemann curvature tensor) or third derivatives (Bianchi identities), but by demanding that the transition maps are $C^\infty$, we guarantee that the coordinate grid is perfectly smooth at all scales. This allows us to differentiate our equations as many times as we want without ever worrying that a mathematical artifact of the coordinate system will cause a calculation to fail.

The new 2D map grid is a new chart for the Everest summit. And combining all our charts of this type, we have a new atlas. However, when two atlases transition between each other smoothly, we kind of tend to clump them together. We say if every chart in Atlas A is smoothly compatible with every chart in Atlas B, they represent the same differentiable structure. Together, all such atlases where you can transition from one to the other smoothly are called the maximal atlas. Note that smooth compatibility only applies to the specific region where the two charts overlap (the intersection $O_\alpha \cap O_\beta$). The charts do not need to cover the same points, and there will naturally be points exclusive to each chart.

As we said earlier, a topological space + an atlas = a manifold. We can now modify that to say a topological space + a maximal atlas = a manifold. For most spaces, there is only one maximal atlas. $\mathbb{R}^4$, however, happens to have infinite maximal atlases. $S^7$ has 28 maximal atlases. These are exotic differentiable structures and are pretty much irrelevant in standard General Relativity.

---

**Aside:** It is important that charts are defined on open sets because standard differential calculus requires the ability to approach a point from any direction. Open sets mathematically guarantee this "wiggle room" around every single point in the chart. Suppose instead that a chart could be a closed set, meaning it includes its boundary edge. You wouldn't be able to approach the points on the boundary from a direction outside the boundary, because all points in that direction are outside the set.

---

### Mathematical Formalities

#### Vectors & Covectors

The coordinate basis of our tangent spaces are quite literally the tangents, or rather the partial derivatives along each coordinate direction. We can therefore define any vector in this space using this basis. 

As we mentioned earlier, the covectors are counting machines. Throw a vector into a covector basis and it tells you how many ticks that vector passes through along that particular coordinate direction, or in other words, along that basis vector. So the components of the vector along each basis can be recovered using the dual covector basis.

Since the covectors are a basis, it means the covector space is a valid vector space, and we can construct arbitrary covectors by taking linear combinations of the basis. Geometrically, a covector is like a contour line; or rather like an infinite family of parallel contour lines: think of all the coordinate lines we would draw perpendicular to the $x$-axis of a graph paper. _All of those lines_, which on the paper may be seperated by a millimeter form a covector basis. The basis covector $dx^\mu$ represents a set of contour lines spaced exactly 1 coordinate unit apart. If you draw the basis tangent vector $\partial_\mu$ (an arrow exactly 1 coordinate unit long), its tip will perfectly pierce exactly one of these contour lines. The machine outputs $1$.

Now let us say we multiply that basis by a component of 5, we get $5 dx^\mu$. This means we now have an infinite family of lines again, but we are cramming 5 lines into the space that formerly seperated two lines. The density of lines has gone up by 5 because to make the machine output a $5$ when fed that same 1-unit vector arrow, the arrow must now pierce 5 contour lines. Because the vector arrow hasn't changed length, the only geometric solution is to more 5 contour lines into the exact same coordinate space. Cramming contour lines closer together means you are traversing values much faster over the same distance. It means a steeper gradient or a faster rate of change. 

**In short:** Vectors scale by length. Change a vector component from $1$ to $5$, the physical arrow stretches to become 5 times longer. Covectors scale by density. Change a covector component from $1$ to $5$, the contour lines get squished together, becoming 5 times denser.

#### Multivariable Chain Rule

We can tie all this together with the chain rule. Depending on how we "factor" it, we generate either the covector (1-form) or the vector (operator). We take a scalar function $f$ evaluated along a parameterized curve $x^\mu(t)$. 

$$\frac{df}{dt} = \frac{dx^\mu}{dt} \frac{\partial f}{\partial x^\mu}$$

The scalar function will lead us to covectors and the curve to vectors. That makes sense. Scalar functions have contours and curves have vectors (their tangents). Let's start with $f$, and let's say we are interested in its rate of change over our manifold. We throw away the $dt$ parameter. We can write this out in terms of the covector basis for that coordinate grid:

$$df = \frac{\partial f}{\partial x^\mu} dx^\mu$$

$dx^\mu$ is the covector basis and $\frac{\partial f}{\partial x^\mu}$ are the covector components. $df$ is called the exterior derivative of the function $f$. By throwing away $dt$, we graduate from a parameterized rate of change (which requires a specific path and speed) to a purely geometric object ($df$) that represents the total possible changes of the function in every direction simultaneously.

However, we can look at this a little differently by focusing on the curve. We factor out the function $f$ from the right side:

$$\frac{d}{dt}(f) = \left( \frac{dx^\mu}{dt} \frac{\partial}{\partial x^\mu} \right) f$$

Now, we recognize that $\frac{dx^\mu}{dt}$ are simply the velocity components of your curve. Let us call them $X^\mu$. We also use the shorthand for the basis operators: $\partial_\mu = \frac{\partial}{\partial x^\mu}$.

$$\frac{d}{dt}(f) = (X^\mu \partial_\mu) f$$

Finally, we "throw away" the scalar function $f$ from both sides to reveal the bare operator:

$$\frac{d}{dt} = X^\mu \partial_\mu$$

Letting $X = \frac{d}{dt}$, we get your exact equation:

$$X = X^\mu \partial_\mu$$

We can merge these two viewpoints now. $df$ is a covector and its geometric purpose is to consume a tangent vector $X$ and output a real number. Similarly, a vector is a linear map or a machine that exists to eat a covector to output a real number, and both of these outputs are the same.  $df(X) = X(f)$.

If we feed this vector $X$ into our $df$ machine, the covector basis $dx^\mu$ mathematically evaluates the vector basis $\frac{\partial}{\partial x^\nu}$. Because they are dual to each other, this outputs the Kronecker delta $\delta^\mu_\nu$, which simply pairs the matching coordinate components. The result is a single scalar number:

$$df(X) = \frac{\partial f}{\partial x^\mu} X^\mu$$

If we feed the scalar function $f$ into our $X$ operator, the vector basis $\partial_\mu$ simply executes its role as a differential operator directly on the function $f$. The result is the same scalar number:

$$X(f) = X^\mu \frac{\partial f}{\partial x^\mu}$$

This operation geometrically represents the vector arrow $X$ piercing through the crammed contour lines of $df$. It is called the directional derivative. It is the the product of two real numbers (or rather the sum of products because the indices are contracted). 
 It tells us how much the function $f$ changes if you move along the specific direction and length defined by the arrow $X$. We have successfully calculated a physical rate of change purely using the duality of vectors and covectors, without ever requiring a metric tensor.

---

**Aside:** Vector and covectors are mathematically on an equal footing. We tend to be more familiar with vectors because we live in a spatial dimension where physical quantities like velocity, force, and momentum are naturally represented as directed arrows (vectors). Covectors (gradients, phase spaces, flux densities) are less visually intuitive, leading introductory physics to treat vectors as primary and covectors as derived tools. But formally, they are identical twins defined entirely by their reciprocal behaviour under coordinate transformations.

In our example above, we said the covector basis first evaluate against the vector basis to get the Kronecker delta, but the vector basis directly applies the differential operation on the function. This seems to be an asymmetry in the significance of the vector and covector. This asymmetry is merely an artifact that falls out of the fact that we constructed our vector space first (from the tangents) and then defined covectors are machines that eat them. We could have done it the other way around to, which is sometimes done in advanced differential geometry. The cotangent space basis $dx^\mu$ is defined as the fundamental geometric object. A vector $X$ is defined formally as an operator on a covector $\omega$: $X(\omega) \in \mathbb{R}$.

---

To concretize this, let's head back to Everest. Say we have a temperature gradient which is 5 degrees per meter, and the component of the wind vector is 10 meters per second along North. Multiplying them gives 50 degrees per second. This means if you were a leaf in the wind, if you were blown north you would experience a temperature change of 50 degrees per second.

We have managed to evaluate this without actually needing to define physical lengths. Though I mentioned meters above just for the sake of concretely defining a velocity and gradient for the convenience of reading, we would get the exact same result even if we had defined everything using feet instead of meters, because the units of length  cancel out. We never need to actually calculate the velocity of the wind in terms of meters per second or the temperature gradient in terms of degrees per meter.

The example with the wind and temperature tells us why we would want to go through this rigmarole of defining vectors and covectors. We can build a massive amount of rigorous mathematics and physics before ever touching a metric. This is called differential topology, where we study intrinsic properties of spaces using only smooth structures, vector fields, and exterior derivatives ($d$).

We can define whether a vector field flows into itself or another vector field using the Lie bracket ($[X, Y]$). We can define whether a differential form is closed ($df = 0$) or exact. We can classify the global topology of the manifold without ever measuring a single distance. The metric tensor is needed when we wish to add geometry to topology. Topology tells you how spaces connect and wrap. Differential geometry (via the metric) tells you how long things are, what angles they intersect at, and what volumes they enclose.
    
By separating the metric-free machinery (like $df(X)$) from the metric-dependent machinery (like lengths and angles), we can isolate physics that requires a gravitational/geometric field from physics that falls only out of smooth manifold structure.

#### Vector Fields & Global Flows

As we mentioned earlier, the metric tensor is what defines measurement and distance and angles in our manifold. And the mathematician or the physics of the situation provide us with it. But what if they don't? Is there any way we can gain knowledge about the situation without resorting to a metric tensor? As we saw above, there is a way. We take a vector and a scalar function and club them together. Earlier, we did that for just one point. But we can do that for every point as well by taking vector fields, which is the collection of vectors at every point of the manifold.  

We can use what is called the flow of the vector field, called the integral curves, to measure how stuff changes as it flows in that field. This is the foundation for one of the most important tools in General Relativity: the Lie Derivative ($\mathcal{L}_X$). The Lie derivative of any tensor simply measures how much that tensor changes when it is "dragged" along the integral curves (the flow $\sigma_t$) of a vector field $X$.

By using the integral curves of $X$, we can measure not just how a scalar field like temperature changes along the flow, but how other vector fields or tensors stretch and twist as they are carried along by the "wind" of $X$, all without ever needing a metric tensor.

Here's an example. When we write the 4-velocity operator $U = U^\mu \partial_\mu$, the hidden parameter is strictly defined as proper time ($\tau$), the actual time ticking on the wristwatch of the observer moving along that path.

If we feed the ambient cosmic microwave background temperature $f$ into an astronaut's 4-velocity operator $U$, the absolute value $U(f)$ tells us exactly how fast the astronaut watches the universe cool down on their own ship's clock.

$$U(f) = \frac{df}{d\tau}$$

We do not need to know the astronaut's global trajectory through the universe to calculate this. We just need their 4-velocity vector at that one specific moment, and the operator $U(f)$ instantly gives us the physical rate of change.

Now for the mathematics. We start by defining a vector field. If you define a specific tangent operator at every point across a region, you have constructed a vector field $X$. These tangent operators have nothing to do with the manifold itself. The vector field is an independent mathematical object. We just describe the vectors of this field at each point using the basis vectors of the tangent space. That is the only link with the manifold itself (apart from the vectors being defined at each point of the manifold, of course). Imagine for example, a weather map showing the wind velocity at every location on Everest. The topography of Everest is different from the flow of the wind itself (though they may influence each other!)

---

**Aside:** Note that you could build a vector field using exactly one of the basis vectors of your coordinate chart; it is called a coordinate vector field (or sometimes a holonomic vector field). This is just one of the infinite vector fields you could have over every point of your manifold. If we take the complete set of $n$ coordinate vector fields together (e.g., both $\partial_x$ and $\partial_y$), we have constructed a coordinate frame field. In General Relativity, when we want to describe the physics experienced by a specific observer moving through spacetime, we attach a specialized frame field to that observer, known as a tetrad (or vierbein).

---

We can find a physical curve $x^\mu(\lambda)$ parameterized by some $\lambda$, by demanding that the curve's tangent perfectly matches the local vector field at every point it passes through:

$$\frac{dx^\mu}{d\lambda} = X^\mu(x(\lambda))$$

This forms a system of ordinary differential equations. By solving these equations, effectively integrating the local slopes from point to point, the global geometry of the curve emerges naturally without ever referencing an arbitrary global origin. This is called a global flow.

Up to now, we used maps (charts) to take a point on the manifold $M$ and assign it coordinates in $\mathbb{R}^n$. Global flows are entirely different. The map $\sigma_t : M \to M$ maps the manifold back onto itself.

It represents an active physical transformation. If you place a particle at point $p$ and let it be carried by the fluid for a time $t$, it will arrive at a new physical point $q$. The map $\sigma_t$ simply formalizes this: $\sigma_t(p) = q$.

The rules governing this map are the basic logic of time evolution:

-   $\sigma_{t=0}$ is the identity map: If zero time passes, the particle stays exactly where it is.
    
-   $\sigma_s \circ \sigma_t = \sigma_{s+t}$: If you flow the particle for time $t$, pause, and then flow it for time $s$, it ends up in the exact same location as if you had flowed it continuously for time $s+t$. It means the flow is steady and has no "memory" of its history.

Global curves and local vectors can go back and forth between each other. If you know the macroscopic flow of the fluid (the streamlines), you can deduce the velocity of a particle at any specific point. This generates a vector field $X^\mu(x)$. You get this by taking the time derivative of the streamline precisely as the particle passes through that point.

Conversely, if someone hands you a vector field $X^\mu(x)$ (an array of instantaneous velocity arrows at every point), you can reconstruct the macroscopic streamlines, which is what we talked about just above. You do this by setting up a system of ordinary differential equations (ODEs) as we did above:

$$\frac{dx^\mu}{dt} = X^\mu(x^1, \dots, x^n)$$

By integrating these ODEs starting from an initial position $x^\mu_{\text{initial}}$, you trace out the entire path of the particle i.e. how the coordinates change with time. These reconstructed paths are called integral curves.

Integral curves do not require you to know anything about the metric tensor or connections. You are handed a pre-existing vector field $X$ defined everywhere on the manifold. You just follow the arrows. Because the arrows already exist at every point, you never have to move an arrow yourself. The smooth structure of the manifold is enough to calculate $\frac{dx^\mu}{dt} = X^\mu(x)$.

#### Scalar Fields

A scalar field is a set of scalar values at every point of the manifold. For example, the temperature at every point on Everest. A nice thing to keep in mind about scalar fields is that they have contour lines, which will come in handy soon.

In physics, we are usually interested in how a vector field and a scalar field interact, which is why it is of great interest to take what we know about vector fields above and see how it fits in with scalar fields. Another way of putting this is, we can define a vector field by the rate of change of a scalar field along that vector field, and we can define a scalar field by how many contour lines of the scalar field a vector field pierces. These are essentially the same thing and should remind us of the vector and covector relationships from above, because they are actually the same thing.

Mathematically, we say: $df(X) = X(f)$, where $f$ is the scalar function and $X$ is the vector field. As an example, we can see how this works when we choose the vector $X$ as a coordinate basis vector $\partial_\nu$ and $f = x^\mu$. The equation becomes:

$$dx^\mu(\partial_\nu) = \partial_\nu(x^\mu) = \delta^\mu_\nu$$

This is as expected: $dx^\mu$ is the dual basis one-form to the tangent vector $\partial_\mu$. The $dx$ is no longer a small step along an axis; it is a linear functional that maps vectors to real numbers.

Note that, $df = \frac{\partial f}{\partial x^\mu} dx^\mu$, and so we see that the partial derivatives $\frac{\partial f}{\partial x^\mu}$ are strictly the components of a one-form, not a vector.

In standard engineering physics, the gradient $\nabla f$ is taught as a vector pointing in the direction of steepest ascent. In differential geometry, the gradient of a scalar field is natively a one-form.

Without a metric tensor, there is no concept of "steepest ascent" or "perpendicular to the contour lines" because angles and lengths do not exist. Instead, the gradient $df$ simply is the stack of contour lines of the function $f$. You do not measure steepest ascent. You measure how many contour lines a given vector $X$ pierces by computing $df(X)$. 

Note that the metric tensor maps the one-form back into a vector by raising the index. The classical gradient vector is formally written as $(\nabla f)^\mu = g^{\mu\nu} \partial_\nu f$. This explicitly shows that "steepest ascent" is a metric-dependent geometric construct.

### More Stuff We Don't Need A Metric Tensor For
**The Lie bracket:** $\mathcal{L}_X Y = [X, Y] = XY - YX$

With components: $[X, Y]^\nu = X^\mu \partial_\mu Y^\nu - Y^\mu \partial_\mu X^\nu$

This measures the failure of the two flows to commute. If you flow along $X$ for an infinitesimal distance, then flow along $Y$, and then reverse the sequence (flow along $-X$ then $-Y$), you will not necessarily return to your starting point. The spatial gap between your starting point and ending point is the vector produced by the Lie derivative.

**The Lie Derivative:** Tells you how a tensor changes relative to a dynamic flow of a vector. Whenever you want to know if a physical system, a geometric shape, or a coordinate grid looks exactly the same after you shift it in a certain direction, you calculate the Lie derivative. If the result is zero, you have found a symmetry.

To find out if the vector has its own independent rate of change, meaning it is changing differently than the fluid wants it to, we must take the total observed change and subtract the baseline distortion forced upon it by the fluid.

The Lie derivative of a scalar function $f$ is just the directional derivative $X(f)$. The Lie derivative of a vector field $Y$ along $X$ is given by the Lie bracket $[X, Y]$, whose components are:

$$(\mathcal{L}_X Y)^\mu = X^\nu \partial_\nu Y^\mu - Y^\nu \partial_\nu X^\mu$$

The first term $X^\nu \partial_\nu Y^\mu$ applies the standard directional derivative along $X$ to the scalar components $Y^\mu$. It evaluates how the numerical coordinates of $Y$ change as we take an infinitesimal step along the direction of $X$, scaled by the magnitude of $X$ (because we are not simply interested in the rate of change, but the rate of change "caused" by $X$ or along $X$).

The second term $- Y^\nu \partial_\nu X^\mu$ corrects for the distortions caused to $Y$ by the flow of $X$. When you evaluate the Lie derivative, you are taking the vector $Y$ at point $q$ and letting the fluid flow $X$ carry it backward in time to point $p$. If the fluid flow $X$ is perfectly uniform (all vectors in $X$ are parallel and constant), the vector $Y$ arrives at $p$ exactly as it was. In this case, the Lie derivative is just the naive directional derivative. However, if the fluid $X$ is diverging, converging, or rotating between $p$ and $q$, the act of dragging $Y$ backward through that fluid actively stretches and rotates $Y$. The second term exactly corrects for that geometric distortion.

The Lie derivative of a covector (1-form) $\omega$ is calculated by applying the Leibniz product rule to its components and basis vectors:

$$\mathcal{L}_X \omega = \mathcal{L}_X (\omega_\mu dx^\mu) = (\mathcal{L}_X \omega_\mu) dx^\mu + \omega_\nu \mathcal{L}_X(dx^\nu)$$

Because $\omega_\mu$ is just a scalar component, its Lie derivative is simply $X^\nu \partial_\nu \omega_\mu$. For the basis 1-form $dx^\nu$, the Lie derivative evaluates to $\partial_\mu X^\nu dx^\mu$. Substituting these in gives the final components:

$$\mathcal{L}_X \omega = \left( X^\nu \partial_\nu \omega_\mu + \omega_\nu \partial_\mu X^\nu \right) dx^\mu$$

Notice the sign difference between the vector and covector Lie derivatives. For a vector, the correction term is subtracted. For a covector, the correction term is added. This is a direct mathematical consequence of their dual nature: pushing a vector forward vs. pulling a covector backward.

**Differential Forms:** In this section, we are interested in tensors that are formed from a basis of $p$ covectors, which can be fed $p$ vectors to give a scalar, i.e., $(0,p)$ tensors. First, we generalize our 1-forms to $p$-forms.

A tensor product is a general operation that combines a $(0, p)$ tensor and a $(0, q)$ tensor to create a new $(0, p+q)$ tensor. Completely antisymmetric $(0,p)$ covariant tensors are called **differential forms** (or $p$-forms).

The process of taking the tensor product and extracting the completely antisymmetric portion is represented by the wedge product $\wedge$. For two 1-forms:

$$\omega \wedge \eta = \omega \otimes \eta - \eta \otimes \omega$$

When you evaluate this on two vectors $u$ and $v$, it evaluates to:

$$(\omega \wedge \eta)(u, v) = \omega(u)\eta(v) - \eta(u)\omega(v)$$

A general $p$-form $\Omega$ is expressed in a coordinate basis using Einstein summation convention as:

$$\Omega = \frac{1}{p!} \Omega_{\mu_1 \mu_2 \dots \mu_p} dx^{\mu_1} \wedge dx^{\mu_2} \wedge \dots \wedge dx^{\mu_p}$$

The factor $\frac{1}{p!}$ is required because Einstein summation sums over all possible permutations of the indices independently. Since the wedge product is totally antisymmetric, the same physical basis element appears $p!$ times in the unrestricted sum, so the combinatorial factor prevents overcounting. When written with strictly ordered indices ($\mu_1 < \mu_2 < \dots < \mu_p$), the factorial is omitted:

$$\Omega = \sum_{\mu_1 < \mu_2 < \dots < \mu_p} \Omega_{\mu_1 \mu_2 \dots \mu_p} dx^{\mu_1} \wedge dx^{\mu_2} \wedge \dots \wedge dx^{\mu_p}$$

In unrestricted Einstein summation:

$$\Omega = \frac{1}{2!} \Omega_{\mu\nu} dx^\mu \wedge dx^\nu = \frac{1}{2} \sum_{\mu=1}^3 \sum_{\nu=1}^3 \Omega_{\mu\nu} dx^\mu \wedge dx^\nu$$

Expanding all 9 terms (noting that terms with identical indices vanish since $dx^\mu \wedge dx^\mu = 0$, and using $\Omega_{\nu\mu} = -\Omega_{\mu\nu}$ and $dx^\nu \wedge dx^\mu = -dx^\mu \wedge dx^\nu$):

$$\Omega = \frac{1}{2} \left[ \Omega_{12} dx^1 \wedge dx^2 + \Omega_{21} dx^2 \wedge dx^1 + \Omega_{13} dx^1 \wedge dx^3 + \Omega_{31} dx^3 \wedge dx^1 + \Omega_{23} dx^2 \wedge dx^3 + \Omega_{32} dx^3 \wedge dx^2 \right]$$

$$\Omega = \Omega_{12} dx^1 \wedge dx^2 + \Omega_{13} dx^1 \wedge dx^3 + \Omega_{23} dx^2 \wedge dx^3$$

Swapping the basis 1-forms in a wedge product flips the sign:

$$dx^\mu \wedge dx^\nu = -dx^\nu \wedge dx^\mu$$

Consequently, $dx^\mu \wedge dx^\mu = 0$.

The exterior derivative operator $d$ maps a $p$-form to a $(p+1)$-form. Acting on a $p$-form $\omega$, it is defined as:

$$d\omega = \frac{1}{p!} \left( \partial_\alpha \omega_{\mu_1\dots\mu_p} \right) dx^\alpha \wedge dx^{\mu_1} \wedge \dots \wedge dx^{\mu_p}$$

In component notation, its antisymmetric components are:

$$(d\omega)_{\mu_1\dots\mu_{p+1}} = (p + 1) \partial_{[\mu_1} \omega_{\mu_2\dots\mu_{p+1}]}$$

The anti-symmetrization bracket $[\dots]$ represents the normalized alternating sum over all possible permutations of the enclosed indices:

$$T_{[\mu_1\dots\mu_n]} = \frac{1}{n!} \sum_{\pi} \text{sgn}(\pi) T_{\mu_{\pi(1)}\dots\mu_{\pi(n)}}$$

Here, $\pi$ represents a specific permutation of the indices, and $\text{sgn}(\pi)$ is the signature of that permutation:

-   $+1$ for an even permutation (an even number of index swaps).
    
-   $-1$ for an odd permutation (an odd number of index swaps).
    
For two indices ($n=2$):

$$T_{[\mu\nu]} = \frac{1}{2!} (T_{\mu\nu} - T_{\nu\mu})$$

For three indices ($n=3$):

$$T_{[\mu\nu\rho]} = \frac{1}{3!} (T_{\mu\nu\rho} + T_{\nu\rho\mu} + T_{\rho\mu\nu} - T_{\nu\mu\rho} - T_{\rho\nu\mu} - T_{\mu\rho\nu})$$

An example of the Exterior Derivative in 3D Space is the curl, $d$ acting on a 1-form (producing a 2-form).

Let $A = A_1 dx^1 + A_2 dx^2 + A_3 dx^3$ be a 1-form. Taking the exterior derivative:

$$dA = \partial_\nu A_\mu dx^\nu \wedge dx^\mu$$

Expanding out the non-zero independent wedges:

$$dA = \left(\frac{\partial A_2}{\partial x^1} - \frac{\partial A_1}{\partial x^2}\right) dx^1 \wedge dx^2 + \left(\frac{\partial A_3}{\partial x^1} - \frac{\partial A_1}{\partial x^3}\right) dx^1 \wedge dx^3 + \left(\frac{\partial A_3}{\partial x^2} - \frac{\partial A_2}{\partial x^3}\right) dx^2 \wedge dx^3$$

These component brackets correspond to the standard Cartesian components of $\nabla \times \mathbf{A}$.

Similarly, we get the divergence with $d$ acting on a 2-form (producing a 3-form).

Let $B$ be a 2-form representing flux through coordinate planes:

$$B = B_1 dx^2 \wedge dx^3 + B_2 dx^3 \wedge dx^1 + B_3 dx^1 \wedge dx^2$$

Applying the exterior derivative $d$:

$$dB = \left(\frac{\partial B_1}{\partial x^1}\right) dx^1 \wedge dx^2 \wedge dx^3 + \left(\frac{\partial B_2}{\partial x^2}\right) dx^2 \wedge dx^3 \wedge dx^1 + \left(\frac{\partial B_3}{\partial x^3}\right) dx^3 \wedge dx^1 \wedge dx^2$$

Permuting the differentials to the standard order $dx^1 \wedge dx^2 \wedge dx^3$:

-   $dx^2 \wedge dx^3 \wedge dx^1 = + dx^1 \wedge dx^2 \wedge dx^3$ (even permutation: 2 swaps)
    
-   $dx^3 \wedge dx^1 \wedge dx^2 = + dx^1 \wedge dx^2 \wedge dx^3$ (even permutation: 2 swaps)
    
Factoring gives:

$$dB = \left( \frac{\partial B_1}{\partial x^1} + \frac{\partial B_2}{\partial x^2} + \frac{\partial B_3}{\partial x^3} \right) dx^1 \wedge dx^2 \wedge dx^3 = (\nabla \cdot \mathbf{B}) \, dx^1 \wedge dx^2 \wedge dx^3$$

The coefficient of the resulting top-form is the divergence.

Applying the exterior derivative twice ($d^2 = 0$) always yields exactly zero. This happens because of a fundamental clash of symmetries: via Clairaut's theorem, mixed partial derivatives are symmetric: they are equal regardless of order, whereas the wedge product of the differentials is strictly antisymmetric: swapping them causes a sign change.

Mathematically, let's look at the exterior derivative applied twice to a scalar function $f$ (a 0-form):

First, take the exterior derivative to get a 1-form:

$$df = \partial_\mu f dx^\mu$$

Now, take the exterior derivative again to get a 2-form:

$$d(df) = \partial_\nu (\partial_\mu f) dx^\nu \wedge dx^\mu = \partial_\nu \partial_\mu f dx^\nu \wedge dx^\mu$$

Because we are summing over all possible combinations of $\mu$ and $\nu$, for any distinct pair (say, $\mu=1, \nu=2$), the expansion gives:


$$\partial_2 \partial_1 f dx^2 \wedge dx^1 + \partial_1 \partial_2 f dx^1 \wedge dx^2$$

By Clairaut's theorem, the partial derivatives commute, so $\partial_2 \partial_1 f = \partial_1 \partial_2 f$. However, the wedge product is antisymmetric, meaning $dx^2 \wedge dx^1 = -dx^1 \wedge dx^2$.

Substituting these in:

$$-(\partial_1 \partial_2 f) dx^1 \wedge dx^2 + (\partial_1 \partial_2 f) dx^1 \wedge dx^2 = 0$$

Because the symmetric partial derivatives are contracted against the antisymmetric wedge product, every single term cancels itself out. Therefore, $d^2 = 0$.

**Interior Product:** The interior product, denoted $\iota_X$, is a mathematical operation that "contracts" a vector field with a differential form. You can think of it as permanently occupying one of the input slots of a tensor.

Because a $p$-form is a machine that requires $p$ vectors to output a number, permanently filling one of those slots with a specific vector $X$ leaves $p-1$ empty slots. Therefore, the resulting object is a $(p-1)$-form.

This is written as $\iota_X : \Lambda^p(M) \to \Lambda^{p-1}(M)$ or:

$$\iota_X \omega(Y_1, \dots, Y_{p-1}) = \omega(X, Y_1, \dots, Y_{p-1})$$

You simply take the vector $X$ and plug it into the very first argument of the $p$-form $\omega$. The remaining $Y$ vectors fill the rest of the slots.

In component notation (which often clarifies the math for calculations), this is simply a tensor contraction of the vector $X^\nu$ with the first index of the form $\omega_{\nu\mu_1\dots\mu_{p-1}}$:

$$(\iota_X \omega)_{\mu_1\dots\mu_{p-1}} = X^\nu \omega_{\nu\mu_1\dots\mu_{p-1}}$$

---

**Aside:** The exterior product wedges the gradients of the form's components. You take the partial derivatives of the component functions across all spatial directions ($\partial_\nu \omega_\mu$). Then you wedge the corresponding basis covectors ($dx^\nu$) onto the existing basis to enforce anti-symmetry. The interior product is "unwedging" one of the covectors.

---

The Lie derivative of differential forms can also be calculated via Cartan's Magic Formula using the exterior derivative and the interior product:

$$\mathcal{L}_X \omega = d(\iota_X \omega) + \iota_X(d\omega)$$

### de Rham Cohomology

If the exterior derivative of a form evaluates to zero, $d\omega = 0$, then $\omega$ is called a closed form.

If a $p$-form $\omega$ can be written as the exterior derivative of some lower-degree $(p-1)$-form $\eta$, such that $\omega = d\eta$, then $\omega$ is called an exact form.

These two concepts are intimately linked by the nilpotency property: $d^2 = 0$.

If a form is exact ($\omega = d\eta$), then taking its exterior derivative yields:

$$d\omega = d(d\eta) = 0$$

Therefore, every exact form is automatically a closed form. However, the reverse statement is the central problem of algebraic topology: not every closed form is exact.

Whether a closed form is exact depends on the global topology (the "holes") of the manifold it lives on. If the manifold has a hole in it, you can have a form where $d\omega = 0$ everywhere, yet you cannot mathematically find any $\eta$ to satisfy $\omega = d\eta$. The mathematical field that studies which closed forms fail to be exact is called de Rham cohomology.

### Side Quest in Vector Calculus
The concepts of "closed" and "exact" forms are the rigorous, coordinate-independent generalizations of the exact things you just described from 3D vector calculus.

In standard 3D space ($\mathbb{R}^3$), we map scalar functions to 0-forms and 3-forms, and vector fields to 1-forms and 2-forms. The exterior derivative $d$ automatically becomes the three fundamental derivatives of vector calculus:

-   $d$ on a 0-form is the Gradient ($\nabla f$)
    
-   $d$ on a 1-form is the Curl ($\nabla \times \vec{A}$)
    
-   $d$ on a 2-form is the Divergence ($\nabla \cdot \vec{B}$)
    

Let $\omega$ be a 1-form (representing a vector field).

1.  **Exact:** If $\omega = df$, it means $\omega$ is the exterior derivative of a 0-form. In vector calculus, this means your vector field is a **gradient field** ($\vec{E} = -\nabla \phi$).
    
2.  **Closed:** If $d\omega = 0$, it means the exterior derivative of $\omega$ is zero. In vector calculus, this means your vector field is **curl-free** or irrotational ($\nabla \times \vec{E} = 0$).
    
3.  **Exact $\implies$ Closed:** Because $d(df) = 0$, the curl of a gradient is always zero ($\nabla \times (\nabla \phi) = 0$).
    
Now let $\Omega$ be a 2-form (representing a flux field, like a magnetic field).

1.  **Exact:** If $\Omega = d\eta$, it means $\Omega$ is the exterior derivative of a 1-form. In vector calculus, this means your field is the **curl of a vector potential** ($\vec{B} = \nabla \times \vec{A}$).
    
2.  **Closed:** If $d\Omega = 0$, it means the exterior derivative of $\Omega$ is zero. In vector calculus, this means your field is **divergence-free** or solenoidal ($\nabla \cdot \vec{B} = 0$, which is Gauss's Law for Magnetism).
    
3.  **Exact $\implies$ Closed:** Because $d(d\eta) = 0$, the divergence of a curl is always zero ($\nabla \cdot (\nabla \times \vec{A}) = 0$).
    

This also explains why "closed" does not always mean "exact." In vector calculus, we are told that if a vector field has zero curl ($\nabla \times \vec{F} = 0$), you can usually write it as the gradient of a scalar potential ($\vec{F} = \nabla f$).

However, there is a critical caveat: this is only true if the space is simply connected, meaning it has no holes, like the origin being removed, or an infinitely long wire punching through the space. If there is a hole, we can have a field that is completely curl-free everywhere it exists, but it is impossible to define a single, continuous potential function $f$ for it.

This translates identically to forms. If the manifold has no topological holes, Poincaré's Lemma guarantees that every closed form is exact (every curl-free field is a gradient). If the manifold has holes, you can have closed forms that are not exact.

### Side Quest in Thermodynamics
One forms can be used to describe much of thermodynamics. In the 1840s, physicists like James Joule conducted experiments to transition isolated systems from an initial State A to a final State B doing only mechanical work (for example, using a falling weight to turn a paddle wheel inside a sealed tub of water to raise its temperature).

They observed a profound physical fact: to get from State A to State B, the total amount of work required was always the exact same number. It did not matter if they did the work quickly, slowly, or in erratic stages. The work done was entirely independent of the path taken.

In the language of differential geometry, the work 1-form $đW = -p dV$ is generally **inexact**. Its integral over a path $\gamma$ from A to B is path-dependent:

$$W = \int_\gamma đW$$

However, Joule's experiments proved that when the system is isolated ($đQ = 0$), this integral suddenly becomes path-independent. By Stokes' Theorem (and the fundamental theorem of calculus on manifolds), the integral of a 1-form is path-independent if and only if that 1-form is exact, meaning it is the exterior derivative of a 0-form.

Therefore, the physicists concluded that under adiabatic conditions, the work 1-form must be the exact exterior derivative of some previously unknown 0-form (state function). They defined this 0-form as the internal energy, $E$.

$$đW_{\text{adiabatic}} = dE$$

Once it was established that a state function $E$ exists, the First Law of Thermodynamics was formalized for general, non-isolated systems.

If you remove the insulation and allow heat $đQ$ to flow, the total change in the system's state is no longer just $đW$. Because $E$ is a fundamental property of the state (a 0-form), its exterior derivative $dE$ is always an exact 1-form, no matter how the system transitions.

The First Law postulates that while the heat 1-form $đQ$ and the work 1-form $đW$ are individually inexact (path-dependent), their sum is always an exact 1-form:

$$dE = đQ + đW$$

Thus, the quote means that the First Law is not merely an accounting rule for transferring energy; it is the fundamental mathematical postulate that a state function $E$ exists whose exterior derivative perfectly absorbs the path-dependency of heat and work.

### Side Quest into Hamiltonian Mechanics

To transition to Hamiltonian mechanics, we shift our focus from configuration space (described by coordinates and velocities) to phase space (described by coordinates and conjugate momenta).

We can treat the generalized coordinates $q^i$ and their canonical momenta $p_i$ on equal footing by combining them into a single $2n$-dimensional state vector $x^\mu$:

$$x^\mu = (q^i, p_i)$$

Here, $i = 1, \dots, n$, representing the $n$ degrees of freedom of the system, meaning the phase space index $\mu$ runs from $1$ to $2n$. By packaging the coordinates and momenta together into $x^\mu$, we can apply the tools of differential geometry to phase space, treating it as a symplectic manifold.

The time evolution of the system is governed by a Hamiltonian energy function $H$. This function generates a vector field $X_H$ that dictates how the system moves. The strict geometric definition linking the energy to the motion is:

$$\iota_{X_H} \omega = -dH$$

If we want to know if the phase space volume changes as the system evolves over time, we need to take the Lie derivative of the symplectic 2-form $\omega$ along the flow $X_H$. Using Cartan's Magic Formula, the calculation is trivial:

$$\mathcal{L}_{X_H} \omega = d(\iota_{X_H} \omega) + \iota_{X_H}(d\omega)$$

Because the symplectic form is closed, $d\omega = 0$, so the second term vanishes. We then substitute the Hamiltonian definition into the first term:

$$\mathcal{L}_{X_H} \omega = d(-dH) = -d(dH)$$

Because the exterior derivative is nilpotent ($d^2 = 0$), the entire expression collapses:

$$\mathcal{L}_{X_H} \omega = 0$$

In three lines of pure algebra, Cartan's formula mathematically proves Liouville's Theorem: the volume of phase space is strictly conserved as a classical system evolves, regardless of the complexity of the forces involved.

### The Metric Tensor

A metric $g$ is a $(0, 2)$ symmetric tensor field. It can be written as a tensor product of basis 1-forms: $g = g_{\mu\nu}(x) dx^\mu \otimes dx^\nu$, which means it eats two vectors to give a scalar, or one vector to give a covector (this operation is called index lowering: $X_\mu = g_{\mu\nu}X^\nu$). The metric components can be extracted via dot products of the coordinate basis vectors (as we discussed in our intuitive analogy):

$$g_{\mu\nu}(x) = g\left(\frac{\partial}{\partial x^\mu}, \frac{\partial}{\partial x^\nu}\right)$$

We are primarily interested in metrics of pseudo-Riemannian manifolds. For Riemannian manifolds, we are guaranteed that a metric evaluates to a positive number for all non-zero vectors (it is positive-definite). Pseudo-Riemannian manifolds relax this: they only require the metric to be _non-degenerate_. This means that if $g(X, Y) = 0$ for _all_ possible vectors $Y$, then $X$ must be the zero vector. Crucially, a pseudo-Riemannian metric can evaluate to zero or a negative number for a non-zero vector.

The metric components $g_{\mu\nu}$ form a symmetric matrix. As we pointed out about Riemann Normal Coordinates, we can always pick a basis for each tangent space where the metric's matrix is perfectly diagonal. Because the metric is non-degenerate, none of these diagonal elements can be $0$. Furthermore, a theorem called **Sylvester's Law of Inertia** states that no matter what coordinate basis you choose to diagonalize the metric, the _number_ of positive and negative diagonal elements (the metric signature) will always remain strictly the same.

The tensor $g$ can be written as a line element $ds^2$:

$$ds^2 = g_{\mu\nu}(x) dx^\mu dx^\nu$$

For purely spatial (Riemannian) geometry, this allows us to measure the length of a vector $X$ at each point and the angles between vectors:

$$\vert{}X\vert{} = \sqrt{g(X, X)}$$

$$g(X, Y) = \vert{}X\vert{}\vert{}Y\vert{} \cos\theta$$

We can also measure distance along a curve. If $X$ is a vector field tangent to the curve and the coordinates of the curve are given by the functions $x^\mu(t)$, the tangent vector components are $X^\mu = \frac{dx^\mu}{dt}$, and the distance is:

$$\int_a^b dt \sqrt{g_{\mu\nu}(x) \frac{dx^\mu}{dt} \frac{dx^\nu}{dt}}$$

This formula is reparameterization invariant, as we already saw in Special Relativity.

In General Relativity, the manifolds we encounter will have a metric where one of the diagonal entries has a sign opposite to the rest (a signature of either $(-, +, +, +)$ or $(+, -, -, -)$). Such manifolds are called Lorentzian manifolds. They follow hyperbolic geometry. The Minkowski metric is the simplest example of one of these metrics, used for flat spacetime.

If we assume the mostly-plus convention $(-, +, +, +)$, a vector is timelike if $g(X, X) < 0$, null (or lightlike) if $g(X, X) = 0$, and spacelike if $g(X, X) > 0$. For the mostly-minus convention, these signs perfectly flip. The null tangent vectors at any point form a lightcone that seperates events that can be simultaneous from ones that cannot. The direction of lightcones can change at each point of the manifold.

Because a timelike vector yields a negative length squared, our earlier spatial distance formula would return an imaginary number. The physical distance measured along a timelike worldline is therefore the proper time $\tau$. Parameterized by a parameter $t$, it is given by absorbing the negative sign:

$$\tau = \int_a^b dt \sqrt{-g_{\mu\nu} \frac{dx^\mu}{dt} \frac{dx^\nu}{dt}}$$

Since the metric is a tensor product of two covectors, we can also feed it one vector and get a covector. This is an isomorphism, and is called index lowering. The components of the vector $X$  and covector (also called $X$) are related by $X_\mu = g_{\mu\nu}X^\nu$, where the position of the indices tells us that the LHS is the covector component and the RHS is the vector component. You can use the inverse metric to raise the index on a 1-form to get a vector.  $X^\mu = g^{\mu\nu}X_\nu$

### Stuff You Can Do With A Metric

**Volume Form:** The metric tensor $g_{\mu\nu}$ provides a natural, coordinate-independent way to integrate over a manifold $M$ by defining a canonical volume form $v$. For an $n$-dimensional manifold, the volume top-form is:

$$v = \sqrt{\vert{}g\vert{}} dx^1 \wedge \dots \wedge dx^n$$

where $g = \det(g_{\mu\nu})$. The absolute value handles the negative determinants found in Lorentzian (spacetime) manifolds.

The scalar factor $\sqrt{\vert{}g\vert{}}$ perfectly absorbs the Jacobian determinant generated by changing coordinates. This ensures the geometric volume remains invariant regardless of the coordinate grid used.

Associated with the volume form is the totally anti-symmetric Levi-Civita symbol $\epsilon_{\mu_1...\mu_n}$, which is not a true tensor because it transforms with the determinant of the Jacobian matrix (it is a "tensor density of weight +1"). To make it a true tensor, it must be multiplied by $\sqrt{\vert{}g\vert{}}$, yielding the covariant volume components:

$$v_{\mu_1...\mu_n} = \sqrt{\vert{}g\vert{}} \epsilon_{\mu_1...\mu_n}$$

**Hodge Dual:** The metric allows us to map any $p$-form to a complementary $(n-p)$-form via the Hodge dual operator $\star$: $\star : \Lambda^p(M) \to \Lambda^{n-p}(M)$. To execute this mathematically, we must contract the $p$-form with the volume form:

$$(\star\omega)_{\nu_1 \dots \nu_{n-p}} = \frac{1}{p!} \omega^{\mu_1 \dots \mu_p} v_{\mu_1 \dots \mu_p \nu_1 \dots \nu_{n-p}}$$

The Hodge star operator ($\star$) takes a $p$-form and mathematically maps it to its orthogonal complement, the exact $(n-p)$ dimensions of the manifold that are "not in the $p$-form." Applying it twice returns the original form, up to a sign determined by the manifold's dimension, the degree of the form, and the metric signature: $\star (\star \omega) = \pm(-1)^{p(n-p)}\omega$.

**The Inner Product:** The Hodge dual allows the construction of a global, positive-definite (on Riemannian manifolds) inner product for $p$-forms. By wedging a $p$-form $\eta$ with the dual of another $p$-form $\omega$, we create a top-form that can be integrated over the entire manifold:

$$\langle \eta, \omega \rangle = \int_M \eta \wedge \star \omega$$

Note that $\eta \wedge \star \omega$ acts as a volume density. It is a field that varies from coordinate to coordinate. To get a global scalar out of the inner product, we must integrate over the manifold.

This specific integral is incredibly important because it constructs the action of a field. The top-form is the Lagrangian density, and integrating it gives us the action. For example, the entire action for the electromagnetic field in curved spacetime is simply $S = -\frac{1}{2} \int F \wedge \star F$.

**Adjoint Derivative ($d^\dagger$ or $\delta$):** Just as operators in quantum mechanics have adjoints, the exterior derivative $d$ has an adjoint operator $d^\dagger$ (also called the codifferential, often denoted $\delta$).

$$d^\dagger : \Lambda^p(M) \to \Lambda^{p-1}(M)$$

It is constructed by sandwiching $d$ between two Hodge stars:

$$d^\dagger = \pm(-1)^{np+n-1} \star d \star$$

$d^\dagger$ is defined as the formal adjoint of $d$ with respect to the inner product. By applying Stokes' Theorem to a closed manifold, the derivative can be shifted from one form to the other:

$$\langle d\alpha, \omega \rangle = \langle \alpha, d^\dagger\omega \rangle$$

**Laplace-de Rham Operator ($\Delta$):** The exterior derivative $d$ (generalizing gradient/curl) and its adjoint $d^\dagger$ (generalizing divergence) combine to form the Laplacian on manifolds.

$$\Delta = d d^\dagger + d^\dagger d$$

Its action on functions is such that because a scalar function $f$ is a 0-form, $d^\dagger f = 0$ (because $\star$ of a scalar is a top-form and $d$ of a top-form is 0). The geometric Laplacian acting on a function reduces to $- \star d \star d f$. Note that this formulation generates a strictly positive operator, meaning it carries a minus sign relative to the standard curved-space Laplacian ($\nabla^2$) used in physics:

$$\Delta f = - \nabla^2 f = - \frac{1}{\sqrt{\vert{}g\vert{}}} \partial_\nu \left( \sqrt{\vert{}g\vert{}} g^{\mu\nu} \partial_\mu f \right)$$

**Hodge Theory and Topology:** Now we connect local differential equations (the Laplacian) to global topology (cohomology). First, we define what a harmonic form is.

A $p$-form $\gamma$ is called harmonic if it satisfies Laplace's equation: $\Delta\gamma = 0$.

Because the inner product is positive-definite, the equation $\langle \gamma, \Delta \gamma \rangle = 0$ forces the sum of two positive squares to be zero: $\langle d\gamma, d\gamma \rangle + \langle d^\dagger \gamma, d^\dagger \gamma \rangle = 0$ (because $\langle \alpha, d^\dagger \omega \rangle = \langle d\alpha, \omega \rangle$ means $\langle \gamma, d (d^\dagger \gamma) \rangle \implies \langle d^\dagger \gamma, d^\dagger \gamma \rangle$ and $\langle \gamma, d^\dagger (d \gamma) \rangle \implies \langle d\gamma, d \gamma \rangle$).

Therefore, every harmonic form is simultaneously closed: $d\gamma = 0$, and co-closed: $d^\dagger \gamma = 0$.

**The Hodge Decomposition Theorem:** Any arbitrary $p$-form $\omega$ on a compact Riemannian manifold can be uniquely broken into three mutually orthogonal components:

$$\omega = d\alpha + d^\dagger\beta + \gamma$$

Where $d\alpha$ is an exact form, $d^\dagger\beta$ is a co-exact form, and $\gamma$ is a harmonic form.

**Hodge's Theorem:** There is an exact isomorphism between the space of harmonic forms $\text{Harm}^p(M)$ and the de Rham cohomology group $H^p(M)$:

$$\text{Harm}^p(M) \cong H^p(M)$$

The cohomology group $H^p(M)$ groups all closed forms into equivalence classes based on the holes in the manifold. The dimension of this group equals the number of independent holes in that specific dimension and is called the $p$-th Betti number. 

Hodge's Theorem proves that within every infinite equivalence class of closed forms, there is exactly one unique harmonic form ($\Delta \gamma = 0$). Physically, because the Laplacian minimizes energy, this means that for any topological configuration dictated by the shape of the space, a physical field will naturally settle into the single, unique harmonic configuration that represents the minimum energy state for that topology.

#### Hodge Dual's & ELectromagnetism

In classical field theory, the dynamical degrees of freedom are fields, which are objects taking values at each point in the spacetime manifold $M$. The simplest example is a scalar field, which assigns a smooth function across $M$.

The theory of electromagnetism is described by a 1-form field, the vector potential $A$. This field is subject to gauge transformations of the form $A \to A + d\alpha$, where $\alpha$ is an arbitrary scalar function. To extract physical observables that are invariant under this gauge redundancy, we take the exterior derivative to construct the field strength 2-form $F = dA$. Because the exterior derivative is nilpotent ($d^2 = 0$), the field strength is strictly gauge-invariant.

The dynamics of these fields are governed by an action principle, constructed by integrating a top-level form (a 4-form in 4D spacetime) over the manifold $M$. The language of differential geometry severely restricts what actions are mathematically possible to write down.

If the manifold lacks a metric, the only 4-form we can build purely from the field strength is the wedge product of $F$ with itself:

$$S_{top} = -\frac{1}{2} \int_M F \wedge F$$

This is a topological action. In terms of physical electric and magnetic fields, it evaluates to $\int d^4x (\mathbf{E} \cdot \mathbf{B})$. Because we can apply the product rule of exterior derivatives to write $F \wedge F = d(A \wedge F)$, the entire integrand is an exact form (a total derivative). By Stokes' theorem, the integral evaluates purely at the boundary of the manifold. Consequently, it does not contribute to the local classical equations of motion.

To generate non-trivial classical dynamics, the manifold must be equipped with a metric tensor $g_{\mu\nu}$. The metric allows us to define the Hodge star operator $\star$, which maps the 2-form $F$ into its dual 2-form $\star F$. This allows us to construct a dynamically relevant 4-form, giving the Maxwell action in curved spacetime:

$$S_{Maxwell} = -\frac{1}{2} \int_M F \wedge \star F = -\frac{1}{4} \int d^4x \sqrt{-g} \, g^{\mu\nu} g^{\rho\sigma} F_{\mu\rho} F_{\nu\sigma} = -\frac{1}{4} \int d^4x \sqrt{-g} \, F^{\mu\nu} F_{\mu\nu}$$

Breaking down the components of the coordinate representation:

-   $d^4x$: The standard coordinate volume element.
    
-   $\sqrt{-g}$: The square root of the negative determinant of the metric, which acts as the Jacobian correction to ensure the volume element is a true geometric invariant under coordinate transformations.
    
-   $g^{\mu\nu} g^{\rho\sigma} F_{\mu\rho} F_{\nu\sigma}$: The full contraction of the field strength tensor using the inverse metric, yielding the Lorentz-invariant scalar $F^{\mu\nu} F_{\mu\nu}$. In flat Minkowski space, this evaluates to $2(B^2 - E^2)$.
    

Varying this action with respect to the field $A$ yields the source-free Maxwell equations, written elegantly in the language of differential forms as $d \star F = 0$.

To describe physical interactions with matter, we couple the gauge field to an electric current, described geometrically as a 1-form $J$. The interacting action becomes:

$$S = \int_M \left( -\frac{1}{2} F \wedge \star F + A \wedge \star J \right)$$

Fundamental physical consistency requires that this interacting action remains invariant under the gauge transformation $A \to A + d\alpha$. Under this shift, the action transforms by an additional term: $\int d\alpha \wedge \star J$. Integrating this by parts (and assuming the boundary terms vanish at infinity) shifts the exterior derivative from $\alpha$ onto the current dual form. For the action to remain unchanged for any arbitrary scalar $\alpha$, we must enforce:

$$d \star J = 0$$

This is the geometric expression of current conservation (the continuity equation $\nabla_\mu J^\mu = 0$). With the source term included in the action, the variational principle yields the full Maxwell equations of motion: $d \star F = \star J$.

### The Covariant Derivative
A tensor is a physical object that exists on the manifold independently of any coordinate system. The covariant derivative isolates the true, intrinsic rate of change of that tensor relative to the manifold itself. However, when we impose a coordinate grid onto a curved manifold, that grid will inevitably twist, stretch, or shrink from point to point. Because we describe the invariant tensor using the components of this twisting grid, if you only take the naive partial derivative of the tensor components ($\partial_\nu Y^\mu$), you are only measuring how the component's numbers change. As your coordinate grid is curving—like latitude and longitude lines on the Earth, the numerical components $Y^\mu$ of a vector will change from point to point even if the physical vector is pointing rigidly in the exact same direction. The partial derivative is "polluted" by this coordinate illusion. 

This is why the covariant derivative is sensitive to the coordinate grid and how it connects across local patches of the manifold. A connection is a map that helps you go from local patch to local patch in the manifold. It is written in terms of the covariant derivative: $\nabla(X, Y) = \nabla_X Y$, where the object $\nabla_X$ is the covariant derivative. It measures if the field $Y$ is "straight" and constant relative to the intrinsic curvature of the manifold itself.

The covariant derivative satisfies three fundamental properties for all vector fields $X, Y, Z$ and all scalar functions $f, g$:

-   **Additivity:** $\nabla_X(Y + Z) = \nabla_X Y + \nabla_X Z$
    
-   **Linearity in the lower index:** $\nabla_{fX+gY}Z = f\nabla_X Z + g\nabla_Y Z$
    
-   **Leibniz (Product) Rule:** $\nabla_X(fY) = f\nabla_X Y + (\nabla_X f)Y$, where the action on a scalar function is defined as simply taking the directional derivative: $\nabla_X f = X(f)$.
    
The equivalent notations are often used for this: $\nabla_\mu = \nabla_{e_\mu}$. The covariant derivative is:

$$\nabla_X Y = \nabla_X(Y^\mu e_\mu)$$

$$= X(Y^\mu)e_\mu + Y^\mu \nabla_X e_\mu$$

$$= X^\nu e_\nu(Y^\mu)e_\mu + X^\nu Y^\mu \nabla_{e_\nu} e_\mu$$

Swapping the dummy index in the second term so we can factor out $e_\mu$, we write the covariant derivative of the basis vector as a linear combination of the other basis vectors, to get:

$$\nabla_X Y = X^\nu \left[ e_\nu(Y^\mu) + \Gamma^\mu_{\nu\rho} Y^\rho \right] e_\mu$$

Because the operator $\nabla_X$ is linear with respect to $X$ we can cleanly strip off the overall factor of $X^\nu$, and it makes sense to define the components of the covariant derivative  along the basis directions. Assuming a standard coordinate basis where $e_\nu = \partial_\nu$, the components of the covariant derivative $\nabla_\nu Y$ are:

$$(\nabla_\nu Y)^\mu = \partial_\nu Y^\mu + \Gamma^\mu_{\nu\rho} Y^\rho$$

The first term ($\partial_\nu Y^\mu$) is simply the gradient of the components of $Y$. It measures how the raw numerical coordinates of the vector change from point to point.

The second term ($\Gamma^\mu_{\nu\rho} Y^\rho$ is the geometric correction that subtracts how the basis vectors $e_\nu$ themselves are changing, expressed in terms of the other basis vectors. We must include this in our definition of the derivative so that we get an accurate picture of how the vector $Y$ is changing due to its own nature and not because of changes in the coordinate system itself.

For example, let's say the coordinate basis was getting smaller. The first term of the covariant derivative i.e. the components would be positive because the components would appear to get larger. But the second term would be negative because the basis is becoming smaller and these effects owuld cancel each other out to give us the true rate of change of the vector.

It is worth comparing this to the Lie derivative. Both operators coincide when acting on scalar functions: $\nabla_X f = \mathcal{L_X} f = X(f)$, which also matches the partial derivative $\partial_\mu f$.

However, their actions on vector fields are fundamentally different. The Lie derivative $\mathcal{L_X} Y = [X, Y]$ depends on both $X$ and the first derivative of $X$. The covariant derivative depends only on the algebraic value of $X$ at that specific point. This linearity is exactly why we could write $\nabla_X = X^\nu \nabla_\nu$ and think of $\nabla_\mu$ as an independent operator in its own right (there is no equivalent way to write "$\mathcal{L_X} = X^\mu \mathcal{L_\mu}$"). This algebraic independence is why the covariant derivative, not the Lie derivative, is the natural geometric generalization of the partial derivative to curved spacetime.

Notation-wise, $\nabla_\nu Y^\mu$ is the same as $(\nabla_\nu Y)^\mu$, and should not be thought of as the covariant derivative of the $\mu$ component of $Y$. You may also encounter a simple comma used to denote the standard partial derivative. $\partial_\nu Y^\mu$ is written as $Y^\mu_{,\nu}$. A semi-colon denotes the full covariant derivative. $\nabla_\nu Y^\mu$ is written as $Y^\mu_{;\nu}$. The component formula for the covariant derivative of a vector field becomes: $Y^\mu_{;\nu} = Y^\mu_{,\nu} + \Gamma^\mu_{\nu\rho} Y^\rho$

The covariant derivative of a 1-form is $\nabla_\nu \omega_\mu = \partial_\nu \omega_\mu - \Gamma^\rho_{\nu\mu} \omega_\rho$, where the sign in from of the Christoffel symbols has flipped to a minus. 

The covariant derivative is really a relationship between the tensor, the manifold and the connection. You can choose a connection such that it makes the covariant derivative of some random tensor $T$ zero ($\nabla T = 0$), but the rest of the tensors will still experience a non-zero covariant derivative. In general relativity, we tend to choose the Levi-Civita connection which is torsion-free and metric compatible, which means $\nabla_\rho g_{\mu\nu} = 0$ (though other tensors may still have non-zero covariant derivatives). We have picked a connection that perfectly matches how the metric tensor is changing. This means we can make measurements all over the place and be sure that they are compatible with each other because the metric tensor components change in sync with the coordinate system's changes. 

We can see this immediately if we write out the component expansion of $\nabla_\rho g_{\mu\nu} = 0$ and do some basic algebra:

$$\nabla_\rho g_{\mu\nu} = \partial_\rho g_{\mu\nu} - \Gamma^\sigma_{\rho\mu} g_{\sigma\nu} - \Gamma^\sigma_{\rho\nu} g_{\mu\sigma} = 0$$
If you move the connection terms to the other side of the equals sign, you get:

$$\partial_\rho g_{\mu\nu} = \Gamma^\sigma_{\rho\mu} g_{\sigma\nu} + \Gamma^\sigma_{\rho\nu} g_{\mu\sigma}$$

Read this equation purely conceptually: The raw coordinate change of the metric components ($\partial_\rho g_{\mu\nu}$) is perfectly absorbed and matched by the twisting of the connection ($\Gamma$).

The Christoffel symbols of the second kind for the Levi-Civita connection are given by:

$$\Gamma^\lambda_{\mu\nu} = \frac{1}{2} g^{\lambda\rho} (\partial_\mu g_{\nu\rho} + \partial_\nu g_{\mu\rho} - \partial_\rho g_{\mu\nu})$$

Note that for the Minkowski metric, where the metric does not change, these symbols become 0. However, in other coordinates like the polar coordinate system, these symbols can be non-zero even for flat space. To determine if a space is flat, we must check if the Riemann curvature tensor is 0. The Christoffel symbols are not tensors, so they are not reliable indicators. They can change with coordinate systems. The Riemann tensor is a genuine tensor. If it vanishes in one coordinate system then it must vanishes in all of them.

---

**Aside:** The Christoffel symbols are not tensor components. This can be checked by seeing that they do not transform as tensor components. Let us see what the connection looks like when we transition to a different basis. Let us define a new basis $\tilde{e}_\nu$ related to our old basis $e_\mu$ by an invertible transformation matrix $A$:

$$\tilde{e}_\nu = A^\mu_\nu e_\mu$$

If both $e_\mu$ and $\tilde{e}_\nu$ are coordinate bases (which is typically the case in General Relativity), this matrix is simply the Jacobian of the coordinate transformation:

$$A^\mu_\nu = \frac{\partial x^\mu}{\partial \tilde{x}^\nu}$$

To see if the connection coefficients are tensors, we must check if they obey the standard tensor transformation rules. We know that the components of a true $(1, 2)$ tensor, let's call it $T$, transform purely multiplicatively via the matrices:

$$\tilde{T}^\mu_{\nu\rho} = (A^{-1})^\mu_\tau A^\lambda_\nu A^\sigma_\rho T^\tau_{\lambda\sigma}$$

We can now derive the transformation law for the connection components $\Gamma^\mu_{\rho\nu}$ to see if they match this behavior. In our new basis $\tilde{e}_\mu$, the connection is defined as:

$$\nabla_{\tilde{e}_\rho} \tilde{e}_\nu = \tilde{\Gamma}^\mu_{\rho\nu} \tilde{e}_\mu$$

Substituting our transformation matrix into the left side of this equation, we get:

$$\tilde{\Gamma}^\mu_{\rho\nu} \tilde{e}_\mu = \nabla_{(A^\sigma_\rho e_\sigma)} (A^\lambda_\nu e_\lambda)$$

Because the covariant derivative is linear in its lower index, we can immediately pull the scalar $A^\sigma_\rho$ out to the front:

$$\tilde{\Gamma}^\mu_{\rho\nu} \tilde{e}_\mu = A^\sigma_\rho \nabla_{e_\sigma} (A^\lambda_\nu e_\lambda)$$

Now we apply the Leibniz (product) rule to the argument. The covariant derivative will act on the scalar function $A^\lambda_\nu$ (which evaluates to the partial derivative $\partial_\sigma A^\lambda_\nu$) and then act on the basis vector $e_\lambda$ (which evaluates to $\Gamma^\tau_{\sigma\lambda} e_\tau$):

$$\tilde{\Gamma}^\mu_{\rho\nu} \tilde{e}_\mu = A^\sigma_\rho \left[ A^\lambda_\nu \Gamma^\tau_{\sigma\lambda} e_\tau + (\partial_\sigma A^\lambda_\nu) e_\lambda \right]$$

To combine these terms, we can swap the dummy index in the second term from $\lambda$ to $\tau$, allowing us to factor out the basis vector $e_\tau$:

$$\tilde{\Gamma}^\mu_{\rho\nu} \tilde{e}_\mu = \left[ A^\sigma_\rho A^\lambda_\nu \Gamma^\tau_{\sigma\lambda} + A^\sigma_\rho \partial_\sigma A^\tau_\nu \right] e_\tau$$

Finally, we need the left and right sides to use the same basis so we can compare the components directly. We convert $e_\tau$ back into the new basis using the inverse matrix $e_\tau = (A^{-1})^\mu_\tau \tilde{e}_\mu$:

$$\tilde{\Gamma}^\mu_{\rho\nu} \tilde{e}_\mu = \left[ A^\sigma_\rho A^\lambda_\nu \Gamma^\tau_{\sigma\lambda} + A^\sigma_\rho \partial_\sigma A^\tau_\nu \right] (A^{-1})^\mu_\tau \tilde{e}_\mu$$

Stripping off the matching basis vectors $\tilde{e}_\mu$ from both sides, we arrive at the exact transformation law for the components of the connection:

$$\tilde{\Gamma}^\mu_{\rho\nu} = (A^{-1})^\mu_\tau A^\sigma_\rho A^\lambda_\nu \Gamma^\tau_{\sigma\lambda} + (A^{-1})^\mu_\tau A^\sigma_\rho \partial_\sigma A^\tau_\nu$$

This result mathematically proves that connection coefficients (and by extension, the Christoffel symbols) do _not_ transform as tensors.

Looking at the right side of the equation, the first term is exactly the transformation law for a $(1, 2)$ tensor. However, the presence of the second term ruins the tensor nature of the object. This second term contains the derivative of the transformation matrix ($\partial_\sigma A^\tau_\nu$), which in coordinate terms represents the second derivatives of the coordinates ($\frac{\partial^2 x^\tau}{\partial \tilde{x}^\sigma \partial \tilde{x}^\nu}$).

This inhomogeneous second term physically represents the relative acceleration between the two coordinate grids. Because $\Gamma$ is not a tensor, you can always find a specific coordinate transformation (Riemann Normal Coordinates) where the first derivatives of the metric vanish, forcing the connection components to be exactly zero at a specific point. If $\Gamma$ were a true tensor, being zero in one coordinate system would mathematically force it to be zero in all coordinate systems, which would mean curved spacetime could not exist!

---

#### $\partial_x \to \mathcal{L}_X \to \nabla_X$: The Difference

If you want to know how the vector field $Y$ is changing, your first instinct is to just take the standard partial derivative: $X^\mu \partial_\mu Y^\nu$. But this naive partial derivative is contaminated by the twisting of the coordinate grid.

If we are interested in measuring how much $Y$ truly deviates from being straight (parallel) along $X$, we must calculate the Covariant Derivative ($\nabla_X Y$) by correcting for and removing the grid's twisting. The Covariant Derivative doesn't care about how $X$ itself change. $X$ is just a marker of which direction to travel in. We never actually travel all the way along X. It does not matter if the field $X$ is diverging, converging, or swirling wildly an inch away from $p$. Because the covariant derivative is evaluated pointwise, the derivatives of $X$ are mathematically irrelevant. This is why we can ignore the $X$ components and just use the basis vectors as a directional pointer, and then add things up linearly i.e. you multiply by the components of $X$. If $\nabla_X Y = 0$, $Y$ is perfectly straight and is a geodesic. The Christoffel term ($+ \Gamma^\nu_{\mu\rho} X^\mu Y^\rho$) is the correction for the grid's twisting. 

Note that the multiplication by the components of $X$ are necessary. They tell the operator how "fast" you are traversing that path. If $X$ represents a particle's velocity, and the particle passes through point $p$ at twice the speed, it will observe the field $Y$ changing twice as fast with respect to its proper time.

If we are interested in a measurement of how much $Y$ truly deviates from perfectly riding the flow of $X$, we must correct for the dragging effects of $X$. The flow term ($- Y^\nu \partial_\nu X^\mu$) corrects for $X$'s shearing. If $\mathcal{L_X} Y = 0$, the two fields flow together perfectly to form closed coordinate loops, which is why the Lie Derivative of two fields is equal to the commutator. 

### Parallel Transport

Consider a vector field $X$ and one of its integral curves, denoted as $C$. This curve can be parametrized by a scalar variable $\tau$, yielding the coordinate path $x^\mu(\tau)$. By the definition of an integral curve, the vector field evaluated at any point on $C$ is exactly equal to the tangent velocity vector of the curve at that point:

$$X^\mu\vert{}_C = \frac{dx^\mu(\tau)}{d\tau}$$

We define the parallel transport of a general tensor field $T$ along this curve. The tensor $T$ is said to be parallel transported along $C$ if its covariant derivative taken strictly along the direction of $X$ vanishes identically:

$$\nabla_X T = 0$$

This is the "manifold" equivalent of shifting a vector from point to point without changing its orientation. The idea of parallel transport depends on the connection. If the connection changes, the meaning of "parallel" changes because the transport takes place along the connection.

A geodesic is a curve which parallel transports itself. Think of a straight line. If you look at the velocity vector along that line, it never changes direction. At every point on the line, it is parallel to itself at all other points. In other words, a curve whose tangent does not change when it is transported along the curve is a geodesic. This means we must parallel transport the velocity vector along itself.

$$\nabla_X X = 0$$

This leads to the geodesic equation:

$$\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu_{\rho\nu} \frac{dx^\rho}{d\tau} \frac{dx^\nu}{d\tau} = 0 \qquad (3.29)$$

## Tensors You Should Know (& Love!)

### The Torsion Tensor

The Torsion tensor is a rank (1,2) tensor that measures the twisting of the Affine Connection. Evaluated with a one-form $\omega$ and two vector fields $X$ and $Y$, it is written as:

$$T(\omega, X, Y) = \omega(\nabla_X Y - \nabla_Y X - [X, Y])$$

Torsion measures whether the rule for parallel transport (the connection) causes space to twist. To test this, you attempt to build a parallelogram using two vector fields, $X$ and $Y$. You parallel transport $Y$ along $X$ (which is $\nabla_X Y$), and you parallel transport $X$ along $Y$ (which is $\nabla_Y X$).

If you subtract these two terms, you are measuring the gap between where the two paths end. However, this gap could exist simply because the vector fields $X$ and $Y$ do not commute, meaning their flows naturally fail to form a closed loop. The Lie bracket $[X, Y]$ quantifies this. By subtracting $[X, Y]$, you filter out the distortions caused by the vector fields. If the result is not zero, the remaining gap is the Torsion. It means the Affine Connection itself is twisting the vectors as you transport them. (In General Relativity, we enforce a "torsion-free" Levi-Civita connection, forcing this tensor to be exactly zero).

The components of the torsion tensor are:

$$T^\rho_{\mu\nu} = f^\rho(\Gamma^\sigma_{\mu\nu} e_\sigma - \Gamma^\sigma_{\nu\mu} e_\sigma)$$

Applying the dual basis $f^\rho$ to the vector $e_\sigma$ yields the Kronecker delta $\delta^\rho_\sigma$, which simply replaces the index $\sigma$ with $\rho$:

$$T^\rho_{\mu\nu} = \Gamma^\rho_{\mu\nu} - \Gamma^\rho_{\nu\mu}$$

The connection coefficients $\Gamma^\rho_{\mu\nu}$ do not transform as tensors but their anti-symmetric part $\Gamma^\rho_{[\mu\nu]}$ does. Also, the torsion tensor is obviosuly anti-symmetric in its lower two indices, $T^\rho_{\mu\nu} = -T^\rho_{\nu\mu}$. 

If a connection is symmetric in its components, then $\Gamma^\rho_{\mu\nu} = \Gamma^\rho_{\nu\mu}$ and $T^\rho_{\mu\nu} = 0$. Such connections are said to be torsion-free. Geometrically, zero torsion means that if you infinitesimally parallel transport vector $X$ along vector $Y$, and vector $Y$ along vector $X$, the resulting parallelogram perfectly closes.

### The Riemann Curvature Tensor

The Riemann Curvature tensor is a rank (1,3) tensor that measures the intrinsic curvature of the manifold. Evaluated with a one-form $\omega$ and three vector fields $X$, $Y$, and $Z$, it is written as:

$$R(\omega, Z, X, Y) = \omega(\nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X,Y]} Z)$$

The Riemann Curvature tensor tests if the manifold is curved by taking a vector $Z$ on an infinitesimal round trip. You transport $Z$ along $Y$ and then along $X$ ($\nabla_X \nabla_Y Z$). You compare this to transporting $Z$ along $X$ and then along $Y$ ($\nabla_Y \nabla_X Z$).

If the manifold is flat, the order of operations does not matter, and the vector $Z$ will point in the exact same direction either way. If the final vector points in a different direction than the initial vector after this closed loop, that rotation is purely the result of the manifold's intrinsic curvature.

However, if the vector fields $X$ and $Y$ do not commute, your two paths do not form a closed box; they end at different points. To make a valid comparison, $Z$ must complete a true closed loop. The Lie bracket $[X, Y]$ represents the vector needed to close the gap between the two paths. Therefore, the third term $\nabla_{[X,Y]} Z$ physically transports $Z$ across that final gap. By subtracting this term, you guarantee that $Z$ has returned to its exact starting point. 

The components of this tensor are:

$$R^\sigma_{\rho\mu\nu} = \partial_\mu \Gamma^\sigma_{\nu\rho} - \partial_\nu \Gamma^\sigma_{\mu\rho} + \Gamma^\lambda_{\nu\rho} \Gamma^\sigma_{\mu\lambda} - \Gamma^\lambda_{\mu\rho} \Gamma^\sigma_{\nu\lambda}$$

Note that the indices $\mu$ and $\nu$ that are associated with the covariant derivatives are placed at the very end. 

Physically, the first two terms ($\partial \Gamma$) represent the raw, first-order changes in the connection from point to point, measuring how the coordinate grid's stretching accelerates. The last two terms ($\Gamma \Gamma$) are non-linear correction factors. They account for the fact that as you parallel transport a vector around a closed loop to measure curvature, the coordinate basis vectors themselves are constantly twisting along the journey.

#### The Riemann Tensor Components

A bunch of Riemann components are $0$ from mathematical symmetries, especially in a Levi-Civita connection.

If we lower an index on the Riemann tensor, and write $R_{\sigma\rho\mu\nu} = g_{\sigma\lambda} R^\lambda_{\phantom{\lambda}\rho\mu\nu}$, then the resulting object also obeys the following identities:

-   $R_{\sigma\rho\mu\nu} = -R_{\sigma\rho\nu\mu}$ (for all connections)
    
-   $R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\mu\nu}$ (for metric compatible connections)
    
-   $R_{\sigma\rho\mu\nu} = R_{\mu\nu\sigma\rho}$ (The first Bianchi Identity: for torsion free connections)
    
-   $R_{\sigma[\rho\mu\nu]} = 0$ (for metric-compatible, torsion free connections)

-   Second Bianchi identity: $\nabla_{[\lambda} R_{\sigma\rho]\mu\nu} = 0$. Alternatively, we can anti-symmetrize on the final three indices: $R^\sigma_{\phantom{\sigma}\rho[\mu\nu;\lambda]} = 0$

* $R^0_{101}$ represents an analysis of a beam of particles with a bulk velocity strictly along the $x$-axis (the 2nd and 4th indices are both $1$). We take a separation vector between a reference particle and a second particle infinitesimally close to it in the same frame, separated only by a time delay $X^0$ (the 3rd index). This component dictates how that time delay accelerates in the time direction $A^0$ (the 1st index). Physically, this represents the longitudinal stretching of the time interval (time dilation) between particles seperated by time but at the same spatial location such as between pulses in a beam.
* $R^0_{102}$ evaluates how the time interval between two consecutive particles stretches or shrinks when the entire beam possesses a simultaneous velocity in both the $x$ and $y$ directions (y comes from the 4th index being 2).
* $R^1_{010}$ evaluates the change in acceleration along the $x$-axis of a spatial separation between particles along the $x$-axis, when the particles have a velocity strictly in time (they are stationary relative to the source).
* $R^\rho_{0\nu 0}$ represents the standard Newtonian tidal forces on a stationary swarm of objects, such as a cluster of particles dropped from rest above the Earth. Such tidal forces are the gravitational equivalent of the electric field $\vec{E}$, causing straightforward stretching and squeezing.
* $R^\rho_{0\nu i}$ represents the tidal forces on an object possessing spatial velocity. These cross-terms manifest as relativistic effects like gravitomagnetism or frame-dragging.

#### What's That 1-form $\omega$ for?
Why do we need the 1-form in these two tensors? Because we'd like to get a nice scalar at the end of the operations. If we look at the operations inside the brackets, they output a vector $V$ representing the gap. $\omega$ is the set of contour lines we use to measure how "long" that gap is in a specific coordinate direction.

### Curvature, the Riemann Tensor and Geodesic Deviation
To evaluate curvature, a single geodesic is insufficient because the Equivalence Principle guarantees we can always find a local frame where a single geodesic looks like a straight line in flat space.

Instead, we must analyze a congruence (a continuous family) of geodesics. Imagine two freely falling observers dropping side-by-side. We parameterize this system with two variables:

-   $\tau$: The proper time (affine parameter) along any specific geodesic.
    
-   $s$: A continuous label that identifies _which_ geodesic you are on.
    
From these parameters, we define two fundamental vector fields:

-   **The Tangent Vector ($U^\mu$):** The four-velocity of the freely falling observer, defined as $U^\mu = \frac{\partial x^\mu}{\partial \tau}$. Because it follows a geodesic, we know $\nabla_U U^\mu = 0$.
    
-   **The Deviation Vector ($S^\mu$):** A spatial vector pointing exactly from one geodesic to its infinitesimally close neighbor, defined as $S^\mu = \frac{\partial x^\mu}{\partial s}$.
- 
Because partial derivatives commute ($\frac{\partial^2 x}{\partial \tau \partial s} = \frac{\partial^2 x}{\partial s \partial \tau}$), the Lie bracket of these two vector fields is zero ($[U, S] = 0$). In a torsion-free geometry like General Relativity:

$$T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$, where $[X, Y]$ and $T(X, Y)$$

$$\implies \nabla_U S^\mu = \nabla_S U^\mu$$

Physically, this means the rate at which the separation vector changes over time is equal to the rate at which the velocity field changes across space.

In flat Euclidean or Minkowski space, initially parallel straight lines remain parallel forever. The deviation vector $S^\mu$ might have a constant velocity, but its acceleration is strictly zero.

On a curved manifold, this is no longer true. Think of how longitudes behave for example. They accelerate towards each other as we go from equator to pole. We define Geodesic Acceleration ($A^\mu$) as the second covariant derivative of the deviation vector along the tangent path:

$$A^\mu = \nabla_U (\nabla_U S^\mu)$$

If $A^\mu \neq 0$, the neighboring freely falling observers are accelerating toward or away from each other, despite both traveling in perfectly "straight" lines.

By the earlier symmetry, we have: 

$$A^\mu = \nabla_U (\nabla_S U^\mu)$$

By definition, the Riemann Curvature Tensor $R^\mu_{\nu\rho\sigma}$ measures the failure of covariant derivatives to commute. Applying its formal definition to the vector $U^\mu$, we get:  

$$\nabla_U \nabla_S U^\mu - \nabla_S \nabla_U U^\mu = R^\mu_{\nu\rho\sigma} U^\nu U^\rho S^\sigma$$

Because $U^\mu$ is a geodesic, its own covariant acceleration is zero ($\nabla_U U^\mu = 0$). Therefore, the second term vanishes completely, leaving us with the Equation of Geodesic Deviation:

$$\nabla_U \nabla_U S^\mu = R^\mu_{\nu\rho\sigma} U^\nu U^\rho S^\sigma$$

Relative acceleration of geodesics is therefore another measure of the curvature of the manifold.
  
In the context of General Relativity, the Equation of Geodesic Deviation is the geometric definition of tidal forces. If you drop a cloud of dust particles into a black hole, every individual particle believes it is in a local inertial frame experiencing zero gravity ($\nabla_U U^\mu = 0$). However, because the Riemann tensor $R^\mu_{\nu\rho\sigma}$ is non-zero, the Equation of Geodesic Deviation dictates that the dust particles will accelerate relative to one another.  

The dust cloud will stretch along the axis of the fall (spaghettification) and compress along the perpendicular axes. Gravity, as a force, does not exist in this framework; what we perceive as gravity is simply the Riemann tensor driving geodesic deviation across a finite volume.

### Ricci Tensor
Given the $(1, 3)$ RIemann tensor, we get the $(0, 2)$ Ricci tensor by contraction:

$$R_{\mu\nu} = R^\rho_{\phantom{\rho}\mu\rho\nu}$$

The symmetries of the Riemann tensor ensure we have symmetries in the Ricci tensor. $R_{\mu\nu} = g^{\sigma\rho} R_{\sigma\mu\rho\nu} = g^{\rho\sigma} R_{\rho\nu\sigma\mu}$, and so:

$$R_{\mu\nu} = R_{\nu\mu}$$

Contracting the Ricci tensor gives us a scalar function called the Ricci scalar:

$$R = g^{\mu\nu} R_{\mu\nu}$$

In fact, from the Bianchi Identity, 

$$\nabla_\lambda R_{\sigma\rho\mu\nu} + \nabla_\sigma R_{\rho\lambda\mu\nu} + \nabla_\rho R_{\lambda\sigma\mu\nu} = 0$$

Multiplying by the inverse metric tensors $g^{\mu\lambda} g^{\rho\nu}$ contracts the indices, yielding:

$$\nabla_\mu R^\mu_{\phantom{\mu}\sigma} - \nabla_\sigma R + \nabla_\nu R^\nu_{\phantom{\nu}\sigma} = 0$$

Combining the identical first and third terms and rearranging gives:

$$\nabla_\mu R^\mu_{\phantom{\mu}\nu} = \frac{1}{2} \nabla_\nu R$$

This motivates us to introduce the Einstein tensor, defined as:

$$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu}$$

which has the property that it is covariantly constant (divergence-free), meaning:

$$\nabla^\mu G_{\mu\nu} = 0$$

Let us look at what the Riemann and Ricci tensors actually mean from the perspective of curvature. Take the Riemann tensor component $R^\rho_{\mu\nu\sigma}$. If you look at this equation in terms of the relative acceleration of the separation vector between geodesics, you get:

$$A^\rho = -R^\rho_{\mu\nu\sigma} V^\mu X^\nu V^\sigma$$

* $A^\rho$ is the acceleration of the separation vector along the $\rho$ direction.
* $V^\mu$ and $V^\sigma$ are the components of the 4-velocity of the reference frame in the $\mu$ and $\sigma$ directions.
* $X^\nu$ is the separation vector between two adjacent geodesics in the $\nu$ direction.

* $R_{11}$ is the trace (contraction) of the Riemann components with the same first and third index. It evaluates the spatial and temporal divergence when the particle swarm has strict $x$-velocity i.e. acceleration along the direction of the spatial seperation, when the particle has x velocity. So for eg. R^2_121 would be the y acceleration along the y direction. So R_11 becomes the contraction in the transverse plane (yz-plane or fixed x) and the longitudinal time dilation, as the particles travel along the x-axis. (Remember that R^1_111 is 0 so we don't take it into account in the summation)
* $R_{12}$ represents the shear-stress equivalent of curvature. It dictates how motion along the $x$-axis and $y$-axis couple together to shear the transverse cross-section of the particle beam.
* $R_{00}$ evaluates the pure 3D volume convergence or divergence of a stationary swarm of test particles dropped from rest. This is equivalent to the Energy density.
Yes, several specific names from continuum mechanics and the gravito-electromagnetic analogy map directly to these tensor components. By categorizing them with these formal names, you directly connect the abstract geometry to the physical properties of the matter sourcing the gravitational field.
* $R_{01}, R_{02}, R_{03}$ represent Momentum Density / Energy Flux. This specific Ricci component dictates the rotation of the local inertial frame, which is the direct source of **Frame-Dragging** (the Lense-Thirring effect).
* $R_{11}, R_{22}, R_{33}$ represent Normal Stress / Principal Pressure.
* $R_{12}, R_{13}, R_{23}$ represent shear stress and evaluate how motion along one spatial axis couples with momentum in another. They map identically to the mechanical shear stress within the matter field (e.g., viscous fluid layers sliding past one another).

#### The Ricci Scalar

The Ricci scalar $R$ is the complete trace of the Ricci tensor across all time and spatial dimensions. It represents an invariant measure of the total scalar volume deviation of a 4D hyper-volume compared to flat Euclidean space.

### Tetrad Formalism
As we've seen, the coordinate system twists and turns along the manifold, leadings to some messy calculations if we want to make measurements and calculate the Riemann tensor to assess the curvature of the manifold. But going back to the RNC, we know that it is possible to pick a coordinate system at any point such that the metric there becomes Minkowski. The only issue is, every other point on the manifold becomes a mess. 

What if we could have the best of both worlds? Rather than change the coordinate system at any point, we will leave the coordinate system as it is i.e. twisting and turning with the metric, but instead choose our basis vectors at any point such that we have a flat metric there _when calculated with this new basis._ Note that every point will have a different basis. These do not replace the coordinate basis that we can evaluate at every point. They are separate from them and are called non-coordinate basis. They are explicitly chosen so that we can calculate a new metric out of them, which will be Minkowski, and we can then use a local Jacobian matrix to map between these non-coordinate basis and the actual "global" coordinate basis that we've always had.

This way, I can conduct experiments and measurements using the flat local metric, and use the local mapping at that point to translate these results into the global metric and coordinate system. This is called the tetrad formalism or vielbiens. It makes the calculation of the Riemman curvature tensor much more algebraic and straightforward. The downside is we have to keep track of our translator Jacobian matrix that must be recalculated at every point.

The vielbein $e^a_\mu$ is the transformation matrix that translates vectors between the curved coordinate grid and the flat local frame. The inner product of the vielbein basis vectors yields the flat Minkowski metric:

$$g = g_{\mu\nu} dx^\mu \otimes dx^\nu = \eta_{ab} \hat{\theta}^a \otimes \hat{\theta}^b$$

$$g(\hat{e}_a, \hat{e}_b) = \eta_{ab}$$

If you want to know what the curved spacetime metric $g_{\mu\nu}$ looks like in your coordinates, you take the flat metric $\eta_{ab}$ and push it through the translator matrices:

$$g_{\mu\nu} = e^a_\mu e^b_\nu \eta_{ab}$$

If you are floating in your perfectly flat free-falling laboratory, you can arbitrarily rotate your setup or boost your velocity (a Lorentz transformation, $\Lambda^a_b$), and the physics inside the lab doesn't change. Therefore, you can rotate the vielbeins at any point without changing the underlying metric $g_{\mu\nu}$. Gravity has now been recast as a gauge theory, similar to electromagnetism, where the gauge group is local Lorentz transformations.

In the coordinate approach, when you move from point A to point B, the grid distorts, and the Christoffel symbols ($\Gamma^\lambda_{\mu\nu}$) tell you how to correct for that distortion.

In the vielbein approach, our local laboratory frame ($\hat{e}_a$) is always rigidly flat ($\eta_{ab}$). It never distorts. But as you carry it from point A to point B over a curved manifold, the whole laboratory frame rotates relative to the background coordinates. The spin connection one-form, $\omega^a_b$, tracks exactly how this happens. Its components are given by:

$$\omega^a_b = \Gamma^a_{cb} \hat{\theta}^c$$

Note that $\hat{\theta}^c$ are the basis 1-forms dual to the vielbein vectors and not polar coordinates. Because the local frame only undergoes Lorentz rotations, and Lorentz transformations are generated by antisymmetric matrices, the spin connection for the Levi-Civita connection is perfectly antisymmetric: $\omega_{ab} = -\omega_{ba}$

If someone hands you a metric, calculating the Christoffel symbols is a nightmare of partial derivatives. The vielbein formalism offers a massive computational shortcut devised by Élie Cartan.

Cartan's First Structure Equation states that for a torsion-free connection:

$$d\hat{\theta}^a + \omega^a_b \wedge \hat{\theta}^b = 0$$

Instead of evaluating derivatives of the metric, you do this:

1.  Read the vielbein 1-forms ($\hat{\theta}^a$) directly off the metric line element.
    
2.  Take their exterior derivatives ($d\hat{\theta}^a$).
    
3.  Algebraically solve the wedge product equation above to find the unknown $\omega^a_b$ terms, utilizing the antisymmetry ($\omega_{ab} = -\omega_{ba}$) to eliminate variables.
Once you have the spin connection, you need to find the curvature. The Riemann tensor $R^\sigma_{\rho\mu\nu}$ has four indices. Cartan simplifies this by compressing the two coordinate indices ($\mu, \nu$) into a differential 2-form, leaving only the two flat-frame indices ($a, b$).

This yields the **Curvature Two-Form**:

$$R^a_b = \frac{1}{2} R^a_{bcd} \hat{\theta}^c \wedge \hat{\theta}^d$$

Cartan's Second Structure Equation tells you exactly how to compute this curvature directly from the spin connection:

$$R^a_b = d\omega^a_b + \omega^a_c \wedge \omega^c_b$$

If you look closely at this equation, it is mathematically identical to the field strength tensor of a Yang-Mills gauge field ($F = dA + A \wedge A$). By switching to vielbeins, you have mathematically formatted General Relativity to look exactly like the quantum gauge theories of the Strong and Electroweak forces.

Besides utility in general relativity, the vielbein is required to put quantum mechanics into curved spacetime. Fermions (like electrons) are described by spinors. Spinors transform under the rules of flat-space Lorentz rotations. A spinor does not know what a curved coordinate grid ($g_{\mu\nu}$) is; it literally cannot be mathematically defined on a general curved manifold. To describe an electron in a gravitational field, you _must_ establish a flat local vielbein frame ($\hat{e}_a$), define the spinor inside that flat frame, and use the spin connection ($\omega^a_b$) to track how the electron's spin rotates as it falls through curved space.

#### Example with the Schwarzschild Metric

The global Schwarzschild metric in coordinates $(t, r, \theta, \phi)$ is given by the line element:

$$ds^2 = -\left(1 - \frac{2M}{r}\right)dt^2 + \left(1 - \frac{2M}{r}\right)^{-1}dr^2 + r^2 d\theta^2 + r^2 \sin^2\theta d\phi^2$$

The goal is to force this equation to look exactly like the flat space Minkowski line element inside the physicist's laboratory:

$$ds^2 = -(\hat{\theta}^0)^2 + (\hat{\theta}^1)^2 + (\hat{\theta}^2)^2 + (\hat{\theta}^3)^2$$

Because the Schwarzschild metric is completely diagonal (there are no mixed terms like $dt dr$), we can simply take the square root of each term to find our basis 1-forms $\hat{\theta}^a$.

By defining $\hat{\theta}^a = e^a_\mu dx^\mu$, we can literally read the vielbein matrix components $e^a_\mu$ right off the page:

-   $\hat{\theta}^0 = \sqrt{1 - \frac{2M}{r}} dt \implies e^0_t = \sqrt{1 - \frac{2M}{r}}$
    
-   $\hat{\theta}^1 = \frac{1}{\sqrt{1 - \frac{2M}{r}}} dr \implies e^1_r = \frac{1}{\sqrt{1 - \frac{2M}{r}}}$
    
-   $\hat{\theta}^2 = r d\theta \implies e^2_\theta = r$
    
-   $\hat{\theta}^3 = r \sin\theta d\phi \implies e^3_\phi = r \sin\theta$

$e^\mu_a$ translates local flat measurements ($a$) back into global coordinate steps ($\mu$). 

-   $e^t_0 = \frac{1}{\sqrt{1 - \frac{2M}{r}}}$
    
-   $e^r_1 = \sqrt{1 - \frac{2M}{r}}$
    
-   $e^\theta_2 = \frac{1}{r}$
    
-   $e^\phi_3 = \frac{1}{r \sin\theta}$
    
Suppose the physicist in the free-falling lab holds up their physical steel ruler, pointing it radially toward the black hole. They measure an object to be exactly 1 meter long. In their local flat coordinates, the length vector is $X^1 = 1$. They want to know: How much Schwarzschild coordinate distance ($r$) does this object span? They use the inverse vielbein:

$$X^r = e^r_1 X^1 = \left( \sqrt{1 - \frac{2M}{r}} \right) (1)$$

The physicist instantly sees that $X^r < 1$. The physical 1-meter ruler spans less than 1 unit of the Schwarzschild $r$-coordinate. Similarly, if they wait for exactly 1 second on their physical laboratory wristwatch ($X^0 = 1$), they calculate the elapsed Schwarzschild coordinate time $t$:

$$X^t = e^t_0 X^0 = \frac{1}{\sqrt{1 - \frac{2M}{r}}} (1)$$

Because the denominator is less than 1, $X^t > 1$. The physicist realizes that 1 second of their actual physical life corresponds to _more_ than 1 unit of coordinate time passing for a distant observer.

The vielbein matrices are simply the mathematical scaling factors (gravitational time dilation and length contraction) neatly organized into a translation dictionary between the abstract grid and the physical laboratory.

Now let's calculate the Riemann tensor for this metric as well. We first take the exterior derivative. If we set:

$$f(r) = \sqrt{1 - \frac{2GM}{r}}$$

The basis of non-coordinate one-forms then can be written as:

$$\hat{\theta}^0 = f dt, \qquad \hat{\theta}^1 = f^{-1} dr, \qquad \hat{\theta}^2 = r d\theta, \qquad \hat{\theta}^3 = r \sin\theta d\phi \qquad (3.53)$$

The metric takes the simple form:

$$ds^2 = \eta_{ab} \hat{\theta}^a \otimes \hat{\theta}^b$$

We now compute $d\hat{\theta}^a$:

$d\hat{\theta}^0 = f' dr \wedge dt$ (since f is  a function of r and nothing else)

$$d\hat{\theta}^1 = 0$$

$$d\hat{\theta}^2 = dr \wedge d\theta$$

$$d\hat{\theta}^3 = \sin\theta dr \wedge d\phi + r \cos\theta d\theta \wedge d\phi$$

The first Cartan structure relation, $d\hat{\theta}^a = -\omega^a_{\phantom{a}b} \wedge \hat{\theta}^b$ gives $\omega^0_{\phantom{0}1} = f' f dt = f' \hat{\theta}^0$. Anti-symmetry and raising and lowering by the Minkowski metric to get $\omega^1_{\phantom{1}0} = \omega_{10} = -\omega_{01} = \omega^0_{\phantom{0}1}$. The Cartan structure equation then gives $d\hat{\theta}^1 = -\omega^1_{\phantom{1}0} \wedge \hat{\theta}^0 + \dots$ and the $\omega^1_{\phantom{1}0} \wedge \hat{\theta}^0$ contribution happily vanishes because it is proportional to $\hat{\theta}^0 \wedge \hat{\theta}^0 = 0$.

$\omega^2_{\phantom{2}1} = f d\theta = (f/r) \hat{\theta}^2$ to solve the $d\hat{\theta}^2$ structure equation. Anti-symmetry gives $\omega^1_{\phantom{1}2} = -\omega^2_{\phantom{2}1} = -(f/r) \hat{\theta}^2$ and this again gives a vanishing contribution to the $d\hat{\theta}^1$ structure equation.

Finally, the $d\hat{\theta}^3$ equation suggests that we take $\omega^3_{\phantom{3}1} = f \sin\theta d\phi = (f/r) \hat{\theta}^3$ and $\omega^3_{\phantom{3}2} = \cos\theta d\phi = (1/r) \cot\theta \hat{\theta}^3$. These anti-symmetric partners $\omega^1_{\phantom{1}3} = -\omega^3_{\phantom{3}1}$ and $\omega^2_{\phantom{2}3} = -\omega^3_{\phantom{3}2}$ do not contribute to $d\hat{\theta}^1$. We have:

$$\omega^0_{\phantom{0}1} = \omega^1_{\phantom{1}0} = f' \hat{\theta}^0, \qquad \omega^2_{\phantom{2}1} = -\omega^1_{\phantom{1}2} = \frac{f}{r} \hat{\theta}^2$$

$$\omega^3_{\phantom{3}1} = -\omega^1_{\phantom{1}3} = \frac{f}{r} \hat{\theta}^3, \qquad \omega^3_{\phantom{3}2} = -\omega^2_{\phantom{2}3} = \frac{\cot\theta}{r} \hat{\theta}^3$$

Now for the curvature two-form, let's start with:

$$R^0_{\phantom{0}1} = d\omega^0_{\phantom{0}1} + \omega^0_{\phantom{0}c} \wedge \omega^c_{\phantom{c}1}$$

We have:

$$d\omega^0_{\phantom{0}1} = f' d\hat{\theta}^0 + f'' dr \wedge \hat{\theta}^0 = \left( (f')^2 + f'' f \right) dr \wedge dt$$

The second term in the curvature 2-form is $\omega^0_{\phantom{0}c} \wedge \omega^c_{\phantom{c}1} = \omega^0_{\phantom{0}1} \wedge \omega^1_{\phantom{1}1} = 0$. So we are left with:

$$R^0_{\phantom{0}1} = \left( (f')^2 + f'' f \right) dr \wedge dt = \left( (f')^2 + f'' f \right) \hat{\theta}^1 \wedge \hat{\theta}^0$$

The other curvature 2-forms, or at leats the non-zero ones after lowering an index, are:

$$R_{0101} = f f'' + (f')^2$$

$$R_{0202} = \frac{f f'}{r}$$

$$R_{0303} = \frac{f f'}{r}$$

$$R_{1212} = -\frac{f f'}{r}$$

$$R_{1313} = -\frac{f f'}{r}$$

$$R_{2323} = \frac{1 - f^2}{r^2}$$

In the coordinates $x^\mu = (t, r, \theta, \phi)$, we can get the same by:

$$R_{\mu\nu\rho\sigma} = e^a_\mu e^b_\nu e^c_\rho e^d_\sigma R_{abcd}$$

$$R_{trtr} = f f'' + (f')^2$$

$$R_{t\theta t\theta} = r f^3 f'$$

$$R_{t\phi t\phi} = r f^3 f' \sin^2\theta$$

$$R_{r\theta r\theta} = -r \frac{f'}{f}$$

$$R_{r\phi r\phi} = -r \frac{f'}{f} \sin^2\theta$$

$$R_{\theta\phi\theta\phi} = (1 - f^2) r^2 \sin^2\theta$$

## References
- [University of Toronto Cheat Sheet](https://xueqilin.me/engsci-2t4/apm426/apm426.pdf)
