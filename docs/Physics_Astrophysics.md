# Physics 5 - Astrophysics

## Basics of Stellar Astrophysics

### Blackbody Radiation

While studying stars, it is convenient as a first approximation to model them as blackbodies. Accordingly, the formula for the energy density per frequency interval of a blackbody is given by Planck's Law:

$$u_\nu=\frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_B T}-1}$$

In order to convert this formula into wavelength terms, we cannot simply replace $\nu$ with $c/\lambda$, as that would simply give us the energy density per frequency interval, but written in terms of $\lambda$. Instead, we note that the actual energy density must be equal for both differential intervals, which means:

$$u_\nu d\nu = u_\lambda d\lambda$$

Further, $\nu = c/\lambda$, which means the magnitude of the differential is $d\nu = \frac{c}{\lambda^2} d\lambda$.

Therefore:

$$u_\lambda = u_\nu\frac{c}{\lambda^2} = \frac{8\pi hc}{\lambda^5}\frac{1}{e^{hc/\lambda k_B T}-1}$$

Note that we can get the bolometric energy density (i.e., the energy density over all frequencies or wavelengths) by integrating over frequency or wavelength, which gives:

$$u = \int_0^\infty u_\nu d\nu = \int_0^\infty u_\lambda d\lambda = aT^4$$

_(where $a = \frac{8\pi^5 k_B^4}{15c^3 h^3}$ is the radiation constant)._

We can also take the energy density per frequency as well as the bolometric energy density and derive a few more analogous quantities from these. For example, the intensity at a given frequency is the flux per solid angle, which becomes:

$$I_\nu = \frac{c}{4\pi}u_\nu \quad \text{(power per unit area per unit solid angle per frequency)}$$

Since this is a blackbody approximation, we must note that this intensity at an infinitesimally small surface (which we consider to be flat) represents blackbody emission, which means photons will be emitted isotropically in all directions from this flat surface, including inwards into the star. To find the actual emergent photon flux from a star, we therefore first find the flux from this infinitesimally small, flat surface, by taking the dot product of the intensity in the outward direction with the normal vector at the flat surface, and integrating over the entire outward hemisphere. This is given by:

$$f_\nu = \int_{\text{hemisphere}} I_\nu \cos\theta \, d\Omega = \pi I_\nu$$

_(where $d\Omega = \sin\theta \, d\theta \, d\phi$ is the solid angle element)._

We then multiply this flux by the entire spherical surface area of the star (i.e., $4\pi R^2$) to get the luminosity at that frequency:

$$L_\nu = 4\pi R^2 f_\nu = 4\pi^2 R^2 I_\nu$$

To get the luminosity (or more accurately, the observed flux) seen by an observer at distance $d$, we just adjust the area over which photons have been dissipated:

$$f_{\nu,\text{obs}} = f_\nu \frac{R^2}{d^2}$$

Integrating all of these formulas over the entire frequency range gives the equivalent bolometric formulas, which are:

$$I = \int_0^\infty I_\nu d\nu = \frac{c}{4\pi}u = \frac{ac}{4\pi}T^4 = \frac{\sigma}{\pi}T^4$$

$$f = \int_0^\infty f_\nu d\nu = \pi I = \sigma T^4$$

$$L = \int_0^\infty L_\nu d\nu = 4\pi R^2 f = 4\pi R^2 \sigma T^4$$

We can, of course, do something analogous for the equations written per wavelength to get analogous formulas:

$$I_\lambda = \frac{c}{4\pi}u_\lambda = \frac{2hc^2}{\lambda^5}\frac{1}{e^{hc/\lambda k_B T}-1}$$

$$f_\lambda = \pi I_\lambda$$

$$L_\lambda = 4\pi R^2 f_\lambda$$

An important equation here is the Stefan-Boltzmann Law, which gives the total flux of a blackbody in terms of temperature:

$$f = \sigma T^4$$

Since we are considering the star to be a blackbody, we can utilize these formulas to find an effective temperature of the star if we consider it an approximate blackbody. We say the Sun has an effective temperature of $T \approx 5800\text{ K}$, which means that a blackbody would have to be at 5800 K to radiate the same total power (across all wavelengths) as given by the Stefan-Boltzmann Law. How do we get the total power emitted by the star? By calculating the flux received from the star at Earth, then calculating the distance to the star, and using these two pieces of information to calculate the total luminosity of the star itself. (The distance could be calculated, for example, by parallax measurements).

We can find certain other "effective" temperatures of the star by considering the frequency and wavelength at which the star's "blackbody" spectrum peaks. This leads to two forms, called Wien's Displacement Law:

$$\lambda_{\text{max}}T = 0.2898\text{ cm}\cdot\text{K}$$

$$h\nu_{\text{max}} = 2.82 k_B T$$

In a similar manner, we can also determine so-called color temperatures by comparing, for instance, the U-B (Ultraviolet & Blue band spectrum) or B-V (blue and visual band specturm) colors of a star with that of a black body. 

The Sun—which radiates approximately like a blackbody at $T = 5800\text{ K}$—has a peak in $B_\lambda$ at 5000 $ \mathring{A} $, which is the wavelength of green light, in the middle of the visual regime. In fact, the eyesight of most animals on Earth apparently evolved to have the most sensitivity in the wavelength range within which the Sun emits the most energy. (No less important, this wavelength range also coincides with the transmission range of water vapor in the atmosphere.) Note that the fact that different temperatures mean different peak emission frequencies implies that stars at different effective temperatures will appear to be of different colours to us. Thus, in general, as stars get hotter, they progress from red to yellow to white to blue. Wolf-Rayet stars, which are massive, aging stars that have blown off their outer hydrogen layers emit mainly in UV, as do young white dwarves. Neutron stars may emit mainly at x-ray frequencies.

For the Sun, the temperature calculated via Wien's displacement law is also approximately 5800 K, which matches the Sun's effective temperature. The fact that these two temperatures agree is a bit of a coincidence that comes down to the Sun's chemistry, which we will explain shortly. However, for many stars, these two temperatures may not coincide.

For a true blackbody, the effective temperature and the temperature given by Wien's Displacement Law would coincide by definition. A blackbody has a surface flux spectrum given at every wavelength by a single thermodynamic temperature $T$:

$$f_\lambda(T)=\pi B_\lambda(T)=\frac{2\pi hc^2}{\lambda^5}\frac{1}{e^{hc/\lambda k_B T}-1}$$

From this single function $f_\lambda(T)$, you can extract the parameter $T$ in two ways:

By integrating the total area under the curve (Stefan-Boltzmann Law):

$$F_{\text{bol}}=\int_0^\infty f_\lambda(T)\,d\lambda=\frac{2\pi^5 k_B^4}{15c^2 h^3}T^4=\sigma T^4\implies T_{\text{eff}}\equiv\left(\frac{F_{\text{bol}}}{\sigma}\right)^{1/4}=T$$

Or by setting the derivative to zero to find the peak wavelength (Wien’s Law):

$$\frac{df_\lambda(T)}{d\lambda}=0\implies\lambda_{\text{max}}=\frac{hc}{4.9651\,k_B T}\implies T_W\equiv\frac{2.898\times 10^7 \mathring{A} \cdot\text{K}}{\lambda_{\text{max}}}=T$$

Therefore, whenever an object's spectrum closely follows a Planck blackbody curve near its peak, $T_{\text{eff}}$ and $T_W$ will automatically coincide.

However, stars are not perfect blackbodies. For example, Alpha Lyrae (the star Vega) has an effective temperature that is calculated to be around 9500 K, whereas the temperature we get from its measured peak emission wavelength (via Wien's displacement law) is 7600 K. Why does this happen? If Vega were a true 9500 K blackbody, its peak wavelength $\lambda_{\text{max}}$ according to Wien's law would be at:

$$\lambda_{\text{max, expected}} = \frac{2.898 \times 10^7 \mathring{A} \cdot\text{K}}{9500\text{ K}} \approx 3050 \mathring{A} \quad(305\text{ nm, in the Near-UV})$$

If we trace Vega’s spectrum from red (7000 $ \mathring{A} $) toward the ultraviolet (3000 $ \mathring{A} $), from 7000 $ \mathring{A} $ down to 3800 $ \mathring{A} $, Vega's spectrum rises steeply toward the ultraviolet, following the exact slope of a 9500 K blackbody curve heading toward a peak at 3050 $ \mathring{A} $. However, just as the curve is climbing past 3800 $ \mathring{A} $ on its way to 3050 $ \mathring{A} $, over 50% of the star's light suddenly vanishes! The highest surviving point left standing on the graph is the edge right before the cliff—at $\lambda = 3800 \mathring{A} $! When we blindly plug that "chopped-off shoulder" at 3800 $\mathring{A}$ into Wien's law, we get an artificially low temperature of 7600 K instead of 9500 K.

Why does something in Vega's atmosphere suddenly absorb over half the photons with wavelengths shorter than $\approx 3700 \mathring{A} $? We will examine this after looking a bit more at spectra and absorption in the next section.

---

**Aside:** Note that the frequency $\nu_{\text{max}}$ where $B_\nu$ peaks is not the same as the frequency $\nu = c/\lambda_{\text{max}}$ at which $B_\lambda$ peaks. The two spectral distributions are different, because a constant frequency interval $d\nu$ corresponds to a changing wavelength interval $\vert{}d\lambda\vert{} = \frac{c}{\nu^2} d\nu$ that grows with wavelength (and falls with frequency).

To avoid this shifting peak paradox (where for example $B_\nu$ peaks in the near-infrared at $\approx 8800 \mathring{A} $ for the Sun while $B_\lambda$ peaks at $\approx 5000 \mathring{A} $), observational astrophysicists often plot the spectral energy distribution (SED) per unit _logarithmic_ frequency or wavelength interval:

$$\nu B_\nu = \lambda B_\lambda$$

Because $d(\ln \nu) = \frac{d\nu}{\nu} = -\frac{d\lambda}{\lambda} = -d(\ln \lambda)$, the distribution $\nu B_\nu(T) = \lambda B_\lambda(T)$ peaks at the exact same physical photon energy regardless of whether you work in frequency or wavelength ($h\nu_{\text{max}} = \frac{hc}{\lambda_{\text{max}}} \approx 3.92\,k_B T$, which for the Sun gives $\lambda \approx 6350 \mathring{A} $).

**Physical intuition of percentage change:** $\frac{d\lambda}{\lambda}$ is the fractional (or percentage) bandwidth. Suppose you are looking at light around $\lambda = 500\text{ nm}$ through a filter of width $\Delta\lambda = 5\text{ nm}$. The fractional width is $\frac{\Delta\lambda}{\lambda} = \frac{5}{500} = 0.01$ (a $1\%$ change in wavelength). Because $\nu = c/\lambda$, increasing $\lambda$ by $1\%$ decreases $\nu$ by $1\%$. Therefore, the corresponding frequency interval $\Delta\nu$ around $\nu = 6\times 10^{14}\text{ Hz}$ must also be a $1\%$ change in frequency: $\frac{\vert{}\Delta\nu\vert{}}{\nu} = 0.01$.
    
So while the absolute widths $\vert{}d\nu\vert{}$ and $\vert{}d\lambda\vert{}$ have completely different units and behaviors, the fractional bandwidth $\frac{\vert{}d\nu\vert{}}{\nu} = \frac{\vert{}d\lambda\vert{}}{\lambda}$ is dimensionless and identical at every point in the spectrum.

Note that the different formulas for the energy density (i.e., per frequency and per wavelength) are used in different situations.

You would use per wavelength representations $B_\lambda$ in Optical/UV grating spectroscopy. When a diffraction grating disperses light linearly in wavelength ($\Delta\lambda = \text{const}$ per pixel).

$B_\nu$ (per unit $d\nu$) is useful in radio astronomy & radiative transfer theory, when receivers have fixed $\Delta\nu$ bandwidths, or when integrating over frequency against atomic cross-sections $\sigma(\nu)$.

You would use $\nu B_\nu = \lambda B_\lambda$ (per $\ln\nu$ or $\ln\lambda$) in multi-wavelength astrophysics (SEDs), when plotting spectra across broad ranges or identifying where a source actually emits most of its bolometric power.

---

#### Rayleigh Jeans & Wien's Approximations of Blackbody Spectra

In astronomical data analysis and theoretical modeling, the full Planck function is mathematically awkward because the temperature $T$ and frequency $\nu$ are trapped inside a non-linear denominator ($e^{h\nu/k_B T} - 1$). You cannot easily invert it, integrate it over a passband, or propagate it through the differential equation of radiative transfer.

We can however utilize two approximations: the Rayleigh-Jeans ($h\nu \ll k_B T$) and Wien ($h\nu \gg k_B T$) approximations to untangle $e^{h\nu/k_B T} - 1$ into a pure linear law at low frequencies and a pure exponential law at high frequencies. 

Here is how each directly simplifies real astronomical analysis.

**1. The Rayleigh-Jeans Limit ($h\nu \ll k_B T$): Why Radio Astronomy Exists as It Does**

When photon energies are much smaller than the thermal kinetic energy ($x = \frac{h\nu}{k_B T} \ll 1$), we Taylor-expand the exponential in the denominator to first order:

$$e^{h\nu/k_B T} - 1 \approx \left(1 + \frac{h\nu}{k_B T} + \dots\right) - 1 = \frac{h\nu}{k_B T}$$

Substituting this back into the Planck function causes Planck's constant $h$ to cancel out completely:

$$B_\nu^{\text{RJ}}(T) = \frac{2h\nu^3}{c^2}\left(\frac{k_B T}{h\nu}\right) = \frac{2\nu^2 k_B T}{c^2} = \frac{2k_B T}{\lambda^2}$$

_(In wavelength space, $B_\lambda^{\text{RJ}}(T) = B_\nu^{\text{RJ}}\frac{c}{\lambda^2} = \frac{2ck_B T}{\lambda^4}$.)_

This single formula creates three massive simplifications across radio, microwave, and infrared astronomy:

_A. Intensity Becomes Strictly Linear in Temperature ($I_\nu \propto T$)_

In the general Planck curve, intensity is a complicated nonlinear function of $T$. In the Rayleigh-Jeans regime, intensity is directly proportional to temperature. Because of this, radio astronomers almost never report specific intensity $I_\nu$ in units of $\text{W}\cdot\text{m}^{-2}\cdot\text{Hz}^{-1}\cdot\text{sr}^{-1}$. Instead, they define the Brightness Temperature ($T_b$) of any observed source by inverting the Rayleigh-Jeans law:

$$T_b \equiv \frac{c^2}{2\nu^2 k_B}I_\nu = \frac{\lambda^2}{2k_B}I_\nu$$

Even if a source is not a blackbody, quoting its intensity in Kelvins ($T_b$) immediately tells you what temperature an equivalent blackbody would need to produce that radio signal.

_B. The Radiative Transfer Equation Linearizes into Temperatures_

Recall the differential equation of radiative transfer for a ray passing through an absorbing/emitting gas cloud of uniform temperature $T_{\text{gas}}$ and optical depth $\tau_\nu$:

$$I_\nu(\tau_\nu) = I_\nu(0)e^{-\tau_\nu} + B_\nu(T_{\text{gas}})\left(1 - e^{-\tau_\nu}\right)$$

At optical or X-ray wavelengths, $I_\nu$ and $B_\nu(T)$ are messy exponentials. In the Rayleigh-Jeans radio regime (such as the famous $21\text{-cm}$ ($\nu = 1420\text{ MHz}$) hyperfine line of neutral hydrogen, where $h\nu/k_B \approx 0.068\text{ K} \ll T_{\text{gas}}$), we just multiply the entire equation by $\frac{\lambda^2}{2k_B}$, and every intensity turns directly into a temperature:

$$T_b(\tau_\nu) = T_{\text{bg}}e^{-\tau_\nu} + T_{\text{gas}}\left(1 - e^{-\tau_\nu}\right)$$

If the gas cloud is optically thin ($\tau_\nu \ll 1$, so $1 - e^{-\tau_\nu} \approx \tau_\nu$) with no background source ($T_{\text{bg}} \approx 0$), the observed brightness temperature is simply:

$$T_b \approx \tau_\nu T_{\text{gas}}$$

This allows radio astronomers to map the column density and temperature of hydrogen gas across the Milky Way using basic linear algebra rather than nonlinear transcendental fits.

_C. Instant Identification of Thermal vs. Non-Thermal Sources (Spectral Index)_

When astronomers discover a new radio source, how do they know if it is a hot thermal cloud (blackbody/bremsstrahlung) or a supermassive black hole jet (synchrotron radiation)? They plot $\log I_\nu$ vs. $\log\nu$ and measure the slope (called the spectral index $\alpha$, where $I_\nu \propto \nu^\alpha$):

-   A thermal blackbody in the Rayleigh-Jeans tail must have $I_\nu \propto \nu^{+2}$ (slope $\alpha = +2$, rising with frequency).
    
-   Synchrotron radiation from relativistic electrons spiralling in magnetic fields falls with frequency as $I_\nu \propto \nu^{-0.7}$ (slope $\alpha \approx -0.7$).
    
-   Furthermore, if a radio receiver measures a brightness temperature $T_b \sim 10^{12}\text{ K}$ from a quasar core, you immediately know the emission cannot be thermal blackbody radiation (since gas at $10^{12}\text{ K}$ would instantly cool via inverse-Compton catastrophe)—it must be coherent or relativistic beaming.
    

**2. The Wien Limit ($h\nu \gg k_B T$): Exponential Sensitivity & High-Energy Cutoffs**

At the opposite extreme—high frequencies and short wavelengths (UV, X-ray, and gamma-ray astronomy, where $x = \frac{h\nu}{k_B T} \gg 1$)—the exponential term dominates the denominator ($e^{h\nu/k_B T} \gg 1$), so we drop the $-1$:

$$B_\nu^{\text{Wien}}(T) \approx \frac{2h\nu^3}{c^2}\exp\left(-\frac{h\nu}{k_B T}\right)$$

_(Or in wavelength space, $B_\lambda^{\text{Wien}}(T) \approx \frac{2hc^2}{\lambda^5}\exp\left(-\frac{hc}{\lambda k_B T}\right)$.)_

Dropping that single "$-1$" simplifies high-energy and stellar astrophysics in three major ways:

_A. Linearizing X-Ray Spectra to Measure Accretion Disk & Neutron Star Temperatures_

Suppose an X-ray telescope (like Chandra or XMM-Newton) observes the thermal glow of a neutron star surface or the inner edge of a black hole accretion disk ($k_B T \sim 1\text{ keV}$, observed at photon energies $E = h\nu \sim 3\text{–}10\text{ keV}$).

In the Wien regime, divide the observed intensity $I_\nu$ by $\nu^3$ and take the natural logarithm:

$$\ln\left(\frac{I_\nu}{\nu^3}\right) = \text{const} - \left(\frac{h}{k_B T}\right)\nu$$

On a semi-log plot of $\ln(I_\nu / \nu^3)$ versus photon energy $E = h\nu$, the spectrum becomes a straight line whose slope is simply $-\frac{1}{k_B T}$. You can read the temperature of a neutron star or X-ray cluster gas directly off the slope of the high-energy exponential tail.

_B. Analytic Integrals for Ionizing Photons (H II Regions & Recombination)_

In both nebular astrophysics (H II regions around massive O-stars) and early-universe cosmology (hydrogen recombination at $T_{\text{rec}} \approx 3000\text{ K}$), we need to calculate the total number of photons capable of ionizing hydrogen ($h\nu \ge \chi_{\text{ion}} = 13.6\text{ eV}$):

$$n_\gamma(\ge \chi_{\text{ion}}) = \int_{\nu_{\text{ion}}}^\infty \frac{u_\nu}{h\nu}\,d\nu \propto \int_{\nu_{\text{ion}}}^\infty \frac{\nu^2\,d\nu}{e^{h\nu/k_B T} - 1}$$

With the $-1$ in the denominator, this integral has no closed-form elementary solution.

However, for both a hot star ($T \approx 30,000\text{ K} \implies k_B T \approx 2.6\text{ eV}$) and the early universe at recombination ($T \approx 3000\text{ K} \implies k_B T \approx 0.26\text{ eV}$), the $13.6\text{ eV}$ ionization threshold sits deep in the Wien tail ($\frac{\chi_{\text{ion}}}{k_B T} \gg 1$). Dropping the $-1$ turns the integrand into $\nu^2 e^{-h\nu/k_B T}$, which you can integrate by parts in two lines to get:

$$n_\gamma(\ge \chi_{\text{ion}}) \propto \left(\frac{\chi_{\text{ion}}}{k_B T}\right)^2 \exp\left(-\frac{\chi_{\text{ion}}}{k_B T}\right)$$

This exact Wien-tail integral is why hydrogen recombination in the early universe happened at $k_B T \approx 0.3\text{ eV}$ ($3000\text{ K}$) instead of $13.6\text{ eV}$ ($158,000\text{ K}$): only the tiny $\exp(-13.6\text{ eV}/k_B T)$ fraction of CMB photons in the far Wien tail had enough energy to keep hydrogen ionized!

_C. Extreme Temperature Sensitivity of UV/Blue Stellar Colors_

Compare how sensitive a star's flux is to a small change in temperature $\frac{dT}{T}$ in the two regimes by taking the logarithmic derivative $\frac{d\ln B_\nu}{d\ln T}$:

-   In the Rayleigh-Jeans tail ($h\nu \ll k_B T$):
    
    $$B_\nu \propto T^1 \implies \frac{d\ln B_\nu}{d\ln T} = 1$$
    
    A $10\%$ increase in stellar temperature produces only a $10\%$ increase in infrared/radio flux. Moreover, the color ratio between two infrared bands ($\frac{B_{\nu_1}}{B_{\nu_2}} = \left(\frac{\nu_1}{\nu_2}\right)^2$) is completely independent of $T$—you cannot measure a hot star's temperature from infrared colors alone!
    
-   In the Wien tail ($h\nu \gg k_B T$):
    
    $$\ln B_\nu = \text{const} - \frac{h\nu}{k_B T} \implies \frac{d\ln B_\nu}{d\ln T} = \frac{h\nu}{k_B T} \gg 1$$
    
    At $h\nu / k_B T = 10$ (in the UV), a $10\%$ change in temperature produces a $100\%$ ($\sim e^1$) change in flux! That is why optical/UV astronomers always use short-wavelength filters ($U - B$ or $B - V$ color indices) as ultra-sensitive thermometers for stars.

### Spectra & Absorption Lines


The light from stars can be observed to have certain characteristics which help us identify the nature of the star. Specifically, the light from stars will be such that the intensity dips at specific wavelengths. These are called absorption lines. We will focus on Hydrogen absorption lines for now.

As we saw, a star emits photons whose energy follows a distribution (i.e., the number of photons at a given energy will be very different from the number of photons at say twice that energy). The number density of photons per unit energy interval emitted by a blackbody at a particular energy $E$ is given by:

$$n_E = \frac{8\pi E^2}{(hc)^3}\frac{1}{e^{E/k_B T}-1}$$

Now, photons do not escape a star from its entire bulk. A photon emitted somewhere in the star's interior is generally scattered and does not escape the star's surface directly. The depth of the star from which a photon stops being scattered and can actually escape the star is called the surface of last scattering. The various layers of the star around and above this point through which the photon travels before escaping is called the photosphere.

When a photon is emitted from the surface of last scattering and travels through the photosphere, it can encounter various atoms (primarily of Hydrogen, but other elements such as Helium and Carbon as well). Now Hydrogen atoms hold an electron which could be in various energy states. The energy of the electron in the $n$-th energy state is given by $-\frac{13.6}{n^2}\text{ eV}$.

Thus, a photon with an energy of say $\frac{13.6}{n_1^2} - \frac{13.6}{n_2^2}\text{ eV}$ can be absorbed by the Hydrogen atom, whose electron would then move from the $n_1$ state to the $n_2$ state. If the hydrogen atoms are in the ground state ($n_1=1$), then any absorption lines are said to be Lyman lines. Lines corresponding to an electron shifting from the ground state to $n=2$ are called Lyman-alpha ($\text{Ly}\alpha$), to $n=3$ are Lyman-beta ($\text{Ly}\beta$), and so forth. Similarly, if the electron was already sitting in the $n=2$ state, and transitions to $n=3, 4,$ etc., we get the Balmer series or Balmer-alpha ($\text{H}\alpha$), beta ($\text{H}\beta$), etc. Starting from $n=3, 4,$ and $5$, we get the Paschen, Brackett, and Pfund series.

Note that the Lyman series are generally at wavelengths in the UV range, while everything above the Balmer series is at wavelengths in the infrared, which means they are largely blocked by the Earth's atmosphere. Early astronomers observing stellar spectra were therefore only able to observe the Balmer series. Based on this, and the presence of absorption lines of other elements such as Calcium (for the Sun), astronomers created a classification system for stars: $\text{O, B, A, F, G, K, M}$ (and $\text{L}$ & $\text{T}$ for brown dwarfs). Each of these classifications has a finer continuum going from $0$ to $9$, with $0$ being hotter and $9$ being cooler. Thus, the Sun is a $\text{G2}$ star.

Note that these classifications are not so much about the chemical composition of the star's atmosphere, but about the temperature of the star (and thus its color). This is because temperature induces an exponential change in the number of photons emitted at a particular energy level, or in the number of hydrogen (or other element) atoms in a particular excitation or ionization state (for e.g., $n=1, 2,$ etc.). A simple change in composition is mostly only linear and is overpowered by the exponential dependence on temperature.

Thus, for a particular absorption line to be present in a star's spectrum, the star must be hot (or cool) enough to emit enough continuum photons at that energy, and must also be at a high (or low) enough temperature to maintain a sufficient population of atoms in those specific excitation and ionization states. Therefore, stellar spectral classes reflect temperature, not abundance variations. This is governed by two competing statistical mechanics equations:

The Boltzmann Equation (Excitation): Gives the ratio of neutral hydrogen atoms in the $n=2$ (Balmer-absorbing) state relative to the $n=1$ ground state:
    
$$\frac{N_2}{N_1} = \frac{g_2}{g_1} e^{-(E_2 - E_1)/k_B T} = 4 e^{-10.2\text{ eV}/k_B T}$$
    
As $T$ rises, the fraction of hydrogen in the $n=2$ state grows exponentially. Here, $g_1$ and $g_2$ are the statistical weights (or degeneracies) of the ground state ($n=1$) and the first excited state ($n=2$) of the Hydrogen atom. $g_n = 2n^2$.
    
The Saha Equation (Ionization): Gives the ratio of ionized hydrogen ($\text{H II}$, naked protons with no electron to absorb anything) to neutral hydrogen ($\text{H I}$):
    
$$\frac{N_{\text{II}}}{N_{\text{I}}} = \frac{2 k_B T}{P_e} \left(\frac{2\pi m_e k_B T}{h^2}\right)^{3/2} e^{-13.6\text{ eV}/k_B T}$$
    
Above $T \approx 10,000\text{ K}$, almost all hydrogen becomes ionized ($N_{\text{II}}/N_{\text{I}} \gg 1$). Note that here, $N_{\text{I}} = N_1 + N_2 + N_3 + \dots$ i.e. the subscript in Roman numerals represents all neutral states, whereas the Arabic numeral subscripts represent the neutral states at various energy levels. 
    
Combining both equations gives the fraction of total hydrogen capable of producing Balmer lines:
    
$$\frac{N_2}{N_{\text{total}}} = \left(\frac{N_2}{N_{\text{I}}}\right) \left(\frac{N_{\text{I}}}{N_{\text{I}} + N_{\text{II}}}\right)$$
    
This product peaks sharply at $T \approx 9500\text{ K}$ (spectral type $\text{A0}$, like Vega), which is why $\text{A}$ stars have the strongest hydrogen lines even though $\text{O}$, $\text{B}$, $\text{A}$, and $\text{G}$ stars are all $\sim 75\%$ hydrogen by mass.

For example, the Sun is too cold to have hydrogen Balmer lines. Because $T \lesssim 6000\text{ K}$, for the Sun or red stars, by the Boltzmann distribution, the ratio of neutral hydrogen atoms in the $n=2$ state ($E_2 = -3.4\text{ eV}$) to the ground state $n=1$ ($E_1 = -13.6\text{ eV}$, so $\Delta E_{12} = 10.2\text{ eV}$) is:

$$\frac{N_{n=2}}{N_{n=1}} = \frac{g_2}{g_1}\exp\left(-\frac{\Delta E_{12}}{k_B T}\right) = 4\exp\left(-\frac{10.2\text{ eV}}{k_B T}\right)$$

For the Sun ($T \approx 5800\text{ K} \implies k_B T \approx 0.5\text{ eV}$):

$$\frac{N_{n=2}}{N_{n=1}} = 4\exp\left(-\frac{10.2}{0.5}\right) = 4 e^{-20.4} \approx 5.6 \times 10^{-9}$$

Even though $74\%$ of the Sun's photosphere is hydrogen, only 1 out of every 200 million hydrogen atoms is in the $n=2$ state! The other $99.9999995\%$ are sitting in the ground state ($n=1$), which can only absorb ultraviolet Lyman photons ($10.2\text{ eV}$), not visible Balmer photons. Thus, the Sun has relatively modest visible hydrogen lines despite being made almost entirely of hydrogen.

At the other extreme, when $T \gtrsim 15,000\text{ K}$, like O and B stars, as you raise the temperature $T$, the Boltzmann factor $e^{-10.2\text{ eV}/k_B T}$ climbs rapidly, putting more atoms into $n=2$. However, hydrogen's total ionization energy from the ground state is $\chi = 13.6\text{ eV}$ (and from $n=2$, it takes only $3.4\text{ eV}$ to strip the electron completely!).

According to the Saha Ionization Equation, the ratio of ionized hydrogen ($N_{\text{II}}$) to neutral hydrogen ($N_{\text{I}}$) given electron number density $n_e$ is:

$$\frac{N_{\text{II}}}{N_{\text{I}}} = \frac{1}{n_e}\left(\frac{2\pi m_e k_B T}{h^2}\right)^{3/2}\exp\left(-\frac{13.6\text{ eV}}{k_B T}\right)$$

Because electron density in a stellar photosphere is very low ($n_e \sim 10^{14}\text{ cm}^{-3}$), the huge phase-space volume factor $\frac{1}{n_e}\left(\frac{2\pi m_e k_B T}{h^2}\right)^{3/2} \sim 10^{15}$ wins as soon as $T$ reaches $\sim 10,000\text{ K}$. Above $12,000\text{ K}$, almost every hydrogen atom is stripped into a bare proton! And a bare proton has no electron left to jump between levels, so it produces zero absorption lines.

So every element has a narrow "Goldilocks temperature window" where its excitation is high enough to populate the lower level of the transition, but its ionization isn't yet high enough to destroy that ion:

| Spectral Type | Photosphere Temperature $T$ | Dominant Absorption Lines Seen | Physical Reason (Same Composition!) |
| --- | --- | --- | --- |
| **O Stars** | $30,000\text{–}50,000\text{ K}$ | Ionized Helium ($\text{He II}$), multiply ionized $\text{C, N, O}$ | Hydrogen and neutral Helium are completely ionized; only tightly bound $\text{He}^+$ ($54.4\text{ eV}$ to ionize) retains an electron. |
| **B Stars** | $11,000\text{–}30,000\text{ K}$ | Neutral Helium ($\text{He I}$, $\Delta E \approx 20\text{ eV}$) | Hot enough to excite $\text{He I}$, not quite hot enough to strip it. |
| **A Stars** | $7,500\text{–}10,000\text{ K}$ | Maximum Hydrogen Balmer Lines ($\text{H I}$) | Exact peak of the Saha $\times$ Boltzmann curve ($\sim 9,500\text{ K}$). |
| **F & G Stars (Sun)** | $5,200\text{–}7,500\text{ K}$ | Singly ionized Calcium ($\text{Ca II}$ H & K lines) & Iron ($\text{Fe II}$) | Hydrogen is locked in the $n=1$ ground state; easily ionized metals ($\text{Ca}^+, \text{Fe}^+$) have low-lying $2\text{–}3\text{ eV}$ levels that absorb visible light. |
| **K & M Stars** | $2,500\text{–}5,200\text{ K}$ | Neutral metals ($\text{Fe I, Na I}$) & Molecules ($\text{TiO}$) | Cool enough that fragile molecules like titanium oxide ($\text{TiO}$) can survive without dissociating. |


Look at the row for the Sun (G-type star): the two darkest, most dramatic absorption lines in the entire solar spectrum are the $\text{Ca II}$ (ionized calcium) H and K lines at $393\text{ nm}$ and $397\text{ nm}$—even though Calcium makes up less than $0.0002\%$ of the atoms in the Sun, compared to $92\%$ for Hydrogen! Why? Because at $5800\text{ K}$, almost $100\%$ of Calcium is in the $\text{Ca}^+$ ground state ready to absorb $393\text{ nm}$ photons, whereas only $5\times 10^{-9}$ of Hydrogen is in the $n=2$ state needed to absorb Balmer photons.

We can now once again look at the discrepenacy in the effective temperature and Wien displacement temperature of Vega, and why this happens to be absent in the Sun. Vega ($\alpha$ Lyrae) is an A0 star with $T_{\text{eff}} = 9500\text{ K}$ — the exact peak of the Payne curve (which is the product we showed above of Boltzmann Excitation multiplied by Saha Ionization, which tells us how the fraction of total hydrogen capable of producing Balmer lines) where Hydrogen has the maximum possible population in the $n=2$ first excited state!

How much energy does it take to completely photoionize a hydrogen atom whose electron is sitting in the $n=2$ state (known as the Balmer continuum or Balmer limit, $n=2 \to \infty$)?

$$E_{\text{ion}}(n=2) = \frac{13.6\text{ eV}}{2^2} = 3.40\text{ eV}$$

What wavelength $\lambda_{\text{limit}}$ corresponds to a photon energy of $3.40\text{ eV}$?

$$\lambda_{\text{limit}} = \frac{hc}{3.40\text{ eV}} = \frac{12,398 \mathring{A} \cdot\text{eV}}{3.40\text{ eV}} = 3646 \mathring{A} \quad(\approx 365\text{ nm})$$

And because discrete Balmer lines $n=2 \to 10, 11, 12\dots$ crowd together and blend just below the ionization limit, the drop visibly starts around $3700 \mathring{A} $!

#### Why Are Absorption Lines Dark?

A common misconception is that absorption lines are completely devoid of light. They only appear "dark" in contrast to the brighter continuum beside them. The fundamental mechanism comes down to how far into the star you can see. If the photons at some frequency are barely scattered, then we can see photons at this frequency emitted by the deeper layers of a star. If a photon is at a frequency where it will tend to be scattered, then the opacity of the star's gas with respect to this photon increases, and so we only see photons from the upper layers of the star. Generally, the upper layers are cooler and the deeper layers are hotter, and since the intensity of the photon emission rises as temperature rises, we see more brightness when a photon emerges from deeper portions of a star.

Of course, there is a bit of a catch here. One catch is that upper layers of stars such as the Sun are actually hotter. The outer chromosphere and corona are extremely hot compared to almost all the rest of the Sun. However, the density here is extremely low, which means very few photons are emitted at these layers. An additional point here is that the temperature is so high that any photons emitted are usually in the UV or x-ray frequencies and not in the visible range. Thus, we actually see bright emission lines at these frequencies from the Sun, mostly from these two very hot outer layers.

The other catch is that even if photons are scattered by atoms or ions in the stellar atmosphere, if these atoms or ions re-emit a photon of the same energy, wouldn't that lead to a recovery of the lost photon's energy? The thing to keep in mind here is that, let's say an atom scatters a photon and picks up that photon's energy. Even if it immediately re-emits a photon at the same energy, this photon has a 50% chance of being re-emitted into the star's interior. This is one reason why the opacity for photons of these frequencies is high. Thus, we have a 50% loss of photons. But suppose the atom does not immediately re-emit the photon. It is possible that some free electron might scatter off the atom and gain the energy of that photon. But then the electron distributes that energy via thermal scattering across the entire blackbody frequency spectrum. Thus, the energy is emitted, but it is spread out over a large frequency spread and not at the original photon's frequency. In fact, we do see a general increase in radiative transfer across the entire frequency spectrum in stellar radiation.

### Hertzsprung-Russell Diagram

A crucial step toward understanding stellar physics was taken in 1911 independently by two astronomers, Hertzsprung and Russell, who placed measurements of stars on a logarithmic plot with axes of luminosity and effective surface temperature.

Almost all known stars are concentrated in several well-defined loci on [such a diagram](https://cdn.britannica.com/17/143617-050-DA3F8537/diagram-Hertzsprung-Russell-Annie-Jump-Cannon-type-order.jpg). About $80\text{–}90\%$ of all stars (depending on what stellar environment one looks at) lie in a narrow diagonal strip called the main sequence, which corresponds very roughly to a relation $L \sim T_E^8$.

Since the luminosity of a spherical blackbody radiator is

$$L = 4\pi r_*^2 \sigma T_E^4$$

this immediately implies that hotter stars are bigger, with $r_* \sim T_E^2$.

The Sun is a main sequence star. Since the coolest stars have about half the surface temperature of the Sun and the hottest stars have about $5$ times the Solar temperature, the radii of main-sequence stars are in the range of about $1/4$ to $25$ times the Solar radius.

Two other stellar loci are apparent on the H-R diagram. There is a concentration of points corresponding to stars that are cool (i.e., red) yet with luminosities orders of magnitude higher than those of main sequence stars. Clearly, these must be objects with large surface areas, with radii of order $100$ times the Solar radius, i.e., $\sim 10^8\text{ km}$, or about $1\text{ AU}$. Accordingly, such stars are named red giants. In the lower left part of the diagram there is another sequence of points, corresponding to stars that are quite hot (i.e., white to blue), yet with luminosities that are orders of magnitude smaller than those of main sequence stars with such temperatures. These must be stars with much smaller radii, of order $10^4\text{ km}$ (i.e., of the order of the Earth’s radius, $6400\text{ km}$), and they are therefore labeled white dwarfs.

The main sequence is a mass sequence, with high-mass stars at high luminosities and high effective temperatures, and low-mass stars at low luminosities and low effective temperatures. The range of masses on the main sequence is between $\sim 0.1$ and $\sim 100\,M_\odot$. The luminosity as a function of mass goes as $L \sim M^\alpha$, with $\alpha \approx 3$ for stars more massive than the Sun and $\alpha \approx 5$ for the less massive stars. Red giants, despite their large luminosities, turn out to have masses usually in the range $1\text{–}2\,M_\odot$. White dwarfs generally have masses similar to that of the Sun, or lower, and are never more massive than $1.4\,M_\odot$.

The strict upper bound of $1.4\,M_\odot$ on white dwarf masses is the Chandrasekhar limit. Unlike main-sequence stars (where thermal gas pressure $P = nk_B T$ increases when the core contracts and heats up), white dwarfs have exhausted their nuclear fuel and are supported entirely by quantum mechanical electron degeneracy pressure ($P_e \propto \rho^{5/3}$ in the non-relativistic regime). As a white dwarf gains mass, its radius actually _shrinks_ ($R_{\text{WD}} \propto M^{-1/3}$), driving the electrons to relativistic speeds where the equation of state softens to $P_e \propto \rho^{4/3}$. At $M_{\text{Ch}} \approx 1.44\,M_\odot$, gravity scales identically with radius as relativistic degeneracy pressure, triggering runaway collapse.

#### Stellar Size & Lifetimes

The scaling $L \sim M^\alpha$ comes directly from hydrostatic equilibrium and radiative diffusion, which dictate how efficiently photons escape the stellar interior based on the dominant opacity ($\kappa$) and pressure ($P$):

-   Low-to-Intermediate Mass Stars ($M \lesssim 0.5\text{–}2\,M_\odot$): Opacity is dominated by Kramers' bound-free and free-free opacity ($\kappa \propto \rho T^{-3.5}$), which yields a steep dependence $L \propto M^{5}\text{–}M^{5.5}$.
    
-   High-Mass Stars ($M \gtrsim 2\text{–}20\,M_\odot$): The interior is hot enough to completely ionize heavy elements, so opacity becomes dominated by constant Thomson electron scattering ($\kappa_{\text{es}} = \text{const}$). With constant opacity and ideal gas pressure, radiative diffusion gives precisely $L \propto M^3$.
    
-   Very Massive Stars ($M \gtrsim 50\,M_\odot$): Radiation pressure ($P_{\text{rad}} = \frac{1}{3}aT^4$) overtakes ideal gas pressure in supporting the star against gravity (approaching the Eddington limit), flattening the relation to $L \propto M^1$.

Because a star's available nuclear fuel is proportional to its mass ($E_{\text{fuel}} \propto M c^2$) while its fuel consumption rate is its luminosity ($L \propto M^\alpha$), the main-sequence lifetime scales as:

$$\tau_{\text{MS}} \propto \frac{M}{L} \propto M^{1-\alpha}$$

For $\alpha \approx 3.5$, $\tau_{\text{MS}} \approx 10^{10}\text{ yr} \left(\frac{M}{M_\odot}\right)^{-2.5}$. This explains why most field red giants we observe today have masses of only $1\text{–}2\,M_\odot$: higher-mass stars exhaust their core hydrogen in just a few million years and quickly die, whereas sub-solar stars ($M \lesssim 0.8\,M_\odot$) have lifetimes longer than the current age of the universe ($13.8\text{ Gyr}$) and have not yet evolved off the main sequence.

#### More Classifications
A final note on nomenclature: apart from their spectral types ($\text{B0}$, $\text{A5}$, $\text{G2}$, etc.), stars are divided into luminosity classes, which are labeled by Roman numerals going from $\text{I}$ to $\text{V}$, with decreasing luminosity. Classes $\text{I}$ to $\text{IV}$ are giants, and $\text{V}$ designates main sequence stars. Thus, the Sun is a $\text{G2V}$ star.

In full Morgan-Keenan (MK) classification, the Roman numerals break down into:

-   $\text{I}$ ($\text{Ia}, \text{Ib}$): Supergiants
    
-   $\text{II}$: Bright giants
    
-   $\text{III}$: Normal giants
    
-   $\text{IV}$: Subgiants
    
-   $\text{V}$: Main-sequence stars (dwarfs)
    
(Often supplemented by $\text{VI}$ or $\text{sd}$ for subdwarfs, and $\text{VII}$ or $\text{D}$ for white dwarfs).
    
Spectroscopically, you can distinguish a $\text{G2I}$ supergiant from a $\text{G2V}$ main-sequence star without knowing its distance by measuring the width of its spectral absorption lines. Because a giant has a huge radius ($R \sim 100\,R_\odot$) for a similar mass, its surface gravity $g = GM/R^2$ and photospheric density are orders of magnitude lower. Fewer particle collisions mean much less collisional (Stark) pressure broadening, giving giants razor-sharp, narrow absorption lines compared to the broad wings seen in dense main-sequence atmospheres.

## Equations of Stellar Equilibrium

In order to calculate the steady-state pressure, luminosity, mass, etc. of a star, we must first understand how a star stays in equilibrium. One aspect is gravity. The mass of the star and the corresponding gravitational attraction will tend to cause contraction of the star. This contraction must be resisted by the outward pressure of the material that makes up the star. In regular stars, this pressure could be from thermal energy due to kinetic motion of particles. In larger, brighter stars, the pressure from the photons radiating outward might be the main contributor. In white dwarfs or neutron stars, the pressure could be degeneracy pressure from the Fermi sea of electrons or neutrons.

Another aspect is the temperature of the star and its relationship to luminosity. Since we approximate stars to blackbodies, the luminosity or radiative power of photons is related to temperature via the Stefan-Boltzmann Law, and of course the opacity of the star's material to photons of various frequencies. Opacity is fundamentally related to scattering and absorption of photons through various processes. The relation is basically that radiative energy flux $F_{\text{rad}} = \frac{L(r)}{4\pi r^2}$ is driven by the gradient of the radiation energy density ($u_{\text{rad}} = a T^4$) divided by the photon mean-free-path opacity ($\kappa \rho$).

A third aspect is energy conservation. The fundamental source of energy in a star is nuclear reactions of various kinds, and what nuclear reactions are present depend on the chemical composition of the star. However, for protostars where nuclear reactions haven't been triggered, the source of energy might be gravitational collapse. Either way, conservation of energy dictates that the rate at which a star loses total energy to space is its luminosity.

These three aspects of equilibrium correspond directly to the three fundamental timescales of stellar astrophysics. Gravity vs pressure determines the time it would take a star to collapse if pressure support suddenly vanished ($t_{\text{dyn}} \sim \frac{1}{\sqrt{G\bar{\rho}}} \sim \sqrt{\frac{R^3}{GM}}$). For the Sun, $t_{\text{dyn}} \approx 30\text{ minutes}$.
    
Radiative transport & gravitational contraction decides the time it takes a star (or contracting protostar) to radiate away its entire reservoir of thermal/gravitational potential energy at its current luminosity ($t_{\text{KH}} \sim \frac{\vert{}E_{\text{gr}}\vert{}}{L} \sim \frac{GM^2}{RL}$). For the Sun, $t_{\text{KH}} \approx 3 \times 10^7\text{ years}$.
    
Nuclear energy generation decides the time it takes the star to exhaust its available core nuclear fuel ($t_{\text{nuc}} \sim \frac{\epsilon_{\text{frac}} M c^2}{L}$, where $\epsilon_{\text{frac}} \approx 0.007$ for hydrogen fusion). For the Sun, $t_{\text{nuc}} \approx 10^{10}\text{ years}$.
    
Because $t_{\text{dyn}} \ll t_{\text{KH}} \ll t_{\text{nuc}}$ by many orders of magnitude, a main-sequence star can maintain instantaneous mechanical (hydrostatic) and thermal equilibrium while its chemical composition evolves very slowly over billions of years.

Both the Kelvin-Helmholtz (thermal) timescale ($t_{\text{KH}}$) and the dynamical (free-fall) timescale ($t_{\text{dyn}}$) are not merely theoretical constructs—they are the actual physical clocks that govern a star's birth, its transitions between fusion stages, its pulsations, and its death.

A star only runs on the slow nuclear clock ($t_{\text{nuc}}$) when a stable nuclear fuel source is actively burning in its core. The moment that fuel runs out—or before it ever ignites—the star immediately switches to the Kelvin-Helmholtz clock ($t_{\text{KH}}$). And if hydrostatic pressure support ever fails, the star switches to the dynamical clock ($t_{\text{dyn}}$).

Whenever a star (or its core) lacks nuclear fusion to balance the energy radiating away from its surface, gravity takes over as the power source. By the Virial Theorem ($2K + U = 0$), as a star contracts under gravity, half of the released gravitational potential energy goes into radiating light ($L$), and the other half goes into heating up the internal gas ($K$).

This gravitational contraction happens strictly on the Kelvin-Helmholtz timescale ($t_{\text{KH}} \sim \frac{GM^2}{RL}$). It dictates three major observational realities.

**Star Birth: The Pre-Main-Sequence Phase (T Tauri & Herbig Ae/Be Stars):** Before a newborn protostar gets hot enough in its core ($T_c \approx 10^7\text{ K}$) to ignite Hydrogen fusion, how does it shine? Entirely by Kelvin-Helmholtz gravitational contraction.

A $1\,M_\odot$ protostar (like the young Sun) spends roughly $30\text{ million years}$ ($t_{\text{KH}}$) slowly shrinking and heating its core along the Hayashi and Henyey tracks on the H-R diagram until its core hits $10\text{ million K}$ and ignites the Main Sequence.
    
Why Brown Dwarfs exist: If a protostar has a mass below $0.07\,M_\odot$, quantum electron degeneracy pressure halts its Kelvin-Helmholtz contraction before the core can reach $10^7\text{ K}$. It never enters the nuclear timescale—it simply cools and fades on its thermal timescale forever.
    
**The "Hertzsprung Gap". Crossing from Main Sequence to Red Giant:** When a star exhausts Hydrogen in its core at the end of the Main Sequence, the core stops producing nuclear energy. Immediately, the star switches from $t_{\text{nuc}}$ to $t_{\text{KH}}$. The inert Helium core contracts on the Kelvin-Helmholtz timescale, releasing gravitational energy that heats a thin Hydrogen shell around it and causes the outer envelope to balloon into a Red Giant (while the core heats up from $1.5 \times 10^7\text{ K}$ to $10^8\text{ K}$ to ignite Helium fusion).
    
Because $t_{\text{KH}}$ is roughly 1,000 times shorter than $t_{\text{nuc}}$, stars race across the middle of the H-R diagram (the Subgiant branch) in just a few million years.
    
When you plot a star cluster's H-R diagram, there is an almost completely empty void between the Main Sequence and the Red Giant Branch—called the Hertzsprung Gap. We rarely catch massive or intermediate-mass stars in this region because they cross it at the speed of $t_{\text{KH}}$ rather than $t_{\text{nuc}}$.

**The Self-Regulating "Thermostat" of Fusion:** Even during the Main Sequence, $t_{\text{KH}}$ is the damping timescale of the star's nuclear thermostat. If the Sun's core fusion rate accidentally spiked by $10\%$ today, the extra heat would expand and cool the core, and that thermal perturbation would relax back to equilibrium on the Kelvin-Helmholtz timescale. Furthermore, because $t_{\text{KH}} \approx 30\text{ million years}$, the thermal energy generated in the Sun's core today takes millions of years of radiative diffusion and thermal relaxation to alter the surface luminosity.

The dynamical timescale ($t_{\text{dyn}}$) rules a star's life in certain situations. Because $t_{\text{dyn}} \sim \frac{1}{\sqrt{G\bar{\rho}}}$ measures how fast pressure waves (sound waves) cross the star to restore hydrostatic equilibrium ($t_{\text{dyn}} \approx \frac{R}{c_s}$, the sound-crossing time), it governs rapid physical motion, oscillations, and catastrophic collapse.

**Variable Stars & Cepheid Pulsations (Cosmic Distance Ladder):** Cepheid variables and RR Lyrae stars pulsate with a strictly regular period $P$ (ranging from hours to weeks) that depends directly on their luminosity. A pulsating star is literally ringing like a giant acoustic bell in its fundamental radial mode. The period of pulsation $P$ is set directly by the dynamical timescale:
    
$$P \propto t_{\text{dyn}} \propto \frac{1}{\sqrt{G\bar{\rho}}}$$
    
Because larger, more luminous supergiants have a much lower average density $\bar{\rho}$, their dynamical timescale $t_{\text{dyn}}$ is longer (days to weeks instead of minutes). Henrietta Swan Leavitt's Period-Luminosity Relation—which Edwin Hubble used to discover the expansion of the universe—is a direct observational manifestation of $t_{\text{dyn}}$.

**Core-Collapse Supernovae ($t_{\text{dyn}} \approx 0.1\text{ to }1\text{ second}$):** At the end of a massive star's life ($M > 8\,M_\odot$), its core is a dense ball of Iron ($\bar{\rho} \approx 10^9\text{ g/cm}^3$) supported by electron degeneracy pressure. Once the Iron core exceeds the Chandrasekhar limit ($\approx 1.4\,M_\odot$), two things happen simultaneously: high-energy photons shatter Iron nuclei (photodisintegration), and protons capture electrons ($p + e^- \to n + \nu_e$).

Pressure support vanishes instantaneously. The core switches to the dynamical free-fall timescale:
    
$$t_{\text{dyn}} \sim \frac{1}{\sqrt{G \rho_{\text{core}}}} \approx \frac{1}{\sqrt{(6.67\times 10^{-8})(10^9)}} \approx 0.1\text{ seconds}$$
    
An Earth-sized Iron core collapses to a $20\text{ km}$ neutron star at $\approx 25\%$ the speed of light in less than a quarter of a second, triggering a Type II Supernova.
    
**Helioseismology and Asteroseismology:** Our Sun has a dynamical timescale of $t_{\text{dyn}} \approx 30\text{ minutes}$. Because acoustic waves ($p$-modes) bounce through the Sun on fractions of this timescale, the entire surface of the Sun rises and falls every 5 minutes ("solar 5-minute oscillations"). By measuring these exact dynamical frequencies via Doppler shifts, astronomers map the internal sound speed, rotation rate, and depth of the convection zone inside the Sun and distant stars.

### Hydrostatic Equilibrium

A star is a sphere of particles acting on each other via gravity. However, the gravitational attraction does not cause all the particles to collapse to the center because of the pressure build-up in the star's layers. If we look at a small mass element of the star, and equate the gravitational force on it towards the center to the difference in pressure in the radially outward direction, we get:

$$-\frac{GM(r)dm}{r^2} = AdP$$

Since $dm = \rho(r)Adr$, we get:

$$\frac{dP(r)}{dr} = -\frac{GM(r)\rho(r)}{r^2}$$

which is the equation of hydrostatic equilibrium. We can multiply both sides by $4\pi r^3 dr$ and integrate, which converts the RHS into the gravitational potential energy needed to assemble the entire star shell by shell, bringing it from infinity to a radius of $r$ going from $0$ to the final $r_*$ radius of the star. This is the gravitational potential self-energy of the star, $E_{\text{gr}}$:

$$-\int_0^{r_*} \frac{GM(r)\rho(r)4\pi r^2 dr}{r}$$

The LHS can be integrated by parts to get:

$$\left[P(r)4\pi r^3\right]_0^{r_*} - 3\int_0^{r_*} P(r)4\pi r^2 dr$$

We assume that at the surface of the star, the pressure is zero, and so the first term goes to $0$. The second term is just $3$ multiplied by the volume-averaged pressure multiplied by volume. Thus,

$$\bar{P} = -\frac{1}{3}\frac{E_{\text{gr}}}{V}$$

This is one form of the virial theorem. To understand where the $1/3$ factor comes from, imagine taking the entire star of radius $R$ and volume $V$ and expanding every radial coordinate uniformly by a tiny fraction $\epsilon = \frac{dR}{R}$ (so every shell moves outward from $r \to r(1+\epsilon)$). Because gravity is held in check by hydrostatic pressure, the mechanical work $\delta W$ done by the internal pressure pushing outward must balance the increase in gravitational potential energy $\delta E_{\text{gr}}$:

$$\delta W = \delta E_{\text{gr}}$$

Gravitational potential energy between every pair of mass elements scales inversely with distance to the first power ($E_{\text{gr}} \propto R^{-1}$), whereas if we look at work done, pressure works against 3D volume $dV$. Volume scales as length cubed ($V \propto R^3$) in 3-dimensional space; stretching every linear dimension by $\frac{dR}{R}$ increases the total volume by thrice that fraction. Thus we have:

$$3\bar{P}V\left(\frac{dR}{R}\right) = -E_{\text{gr}}\left(\frac{dR}{R}\right)$$

$$\bar{P} = -\frac{1}{3}\frac{E_{\text{gr}}}{V}$$

When the star expands by $1\%$ in radius, its gravitational energy changes by $1\%$, but its volume changes by $3\%$. Because the volume expands by $3\%$ for every $1\%$ change in radius, the pressure $\bar{P}$ pushing on that volume only needs to be $\frac{1}{3}$ as strong as the gravitational energy density $\frac{\vert E_{\text{gr}}\vert}{V}$ to do the same $1\%$ of work. By the same logic, in the formula $\bar{P} = -\frac{1}{3}\frac{E_{\text{gr}}}{V}$, the numerator has $E_{\text{gr}} \propto R^{-1}$ (drops by $1\%$); the denominator has $V \propto R^3$ (increases by $3\%$); combining the numerator and denominator gives $\bar{P} \propto \frac{R^{-1}}{R^3} = R^{-4}$.

So if a star expands in radius by $1\%$, its mean equilibrium pressure actually drops by $4\%$ ($1\%$ because gravity got weaker, plus $3\%$ because the same energy is spread over a larger volume).

We can also relate the gravitational potential energy to the thermal energy of the star. If we assume the star is made up of an ideal monoatomic gas (which would be a fair assumption since stars are mostly ionized hydrogen), we can write for every point of the star:

$$PV = Nk_B T$$

where $N$ is the number of individual particles, which includes ionized nuclei and free electrons. For a monoatomic gas, we know that the equipartition of energy with $3$ degrees of translational freedom gives:

$$E_{\text{th}} = \frac{3}{2} Nk_B T$$

Therefore, $PV = \frac{2}{3} E_{\text{th}}$.

Integrating and averaging this over the entire star gives us the relationship between average pressure, volume, and the star's total thermal energy:

$$\bar{P}V = \frac{2}{3}E_{\text{th}}^{\text{tot}}$$

Thus, we get the second form of the virial theorem:

$$E_{\text{th}}^{\text{tot}} = -\frac{1}{2}E_{\text{gr}}$$

This is also written as $2 E_{\text{th}} + E_{\text{gr}} = 0$ and sometimes as $2K + U = 0$.

The total energy of a star ($E_{\text{tot}} = E_{\text{th}}^{\text{tot}} + E_{\text{gr}}$) is therefore:

$$E_{\text{tot}} = \frac{1}{2}E_{\text{gr}} = -E_{\text{th}}^{\text{tot}}$$

Due to the minus sign relating the thermal and gravitational energy, if the star contracts, the radius decreases and therefore the magnitude of $E_{\text{gr}}$ will increase (i.e., it becomes more negative). The total thermal energy therefore becomes more positive, which means the star heats up as it collapses. This also means that a star heats up as it loses energy, which means it has a negative heat capacity. This isn't all that surprising since when a star collapses, its particles will gain kinetic energy, which translates to more thermal energy and heat.

The negativegravothermal heat capacity is the reason stars do not blow themselves up like hydrogen bombs. In a terrestrial fusion reactor (or a degenerate white dwarf where $P$ does not depend on $T$), if a fluctuation slightly increases the nuclear reaction rate, the temperature rises, which exponentially increases the fusion rate further, causing a runaway thermonuclear explosion. In a main-sequence star governed by the virial theorem, if the core generates excess nuclear energy ($dE_{\text{tot}} > 0$), the core expands ($r$ increases, $E_{\text{gr}}$ becomes less negative) and cools down ($dE_{\text{th}} = -dE_{\text{tot}} < 0$), automatically throttling the fusion rate back down to equilibrium. Let's put some concrete example numbers to this.

Suppose our star starts in equilibrium state 1, where the virial theorem holds: $E_{\text{gr},1}$ is $-200\text{ J}$, $E_{\text{th},1}$ is $+100\text{ J}$ and $E_{\text{tot},1} = E_{\text{th},1} + E_{\text{gr},1}$ is $-100\text{ J}$
    
Now, suppose a fluctuation in the core causes nuclear fusion to suddenly dump $\Delta E = +10\text{ J}$ of extra heat into the star. At the exact microsecond the $+10\text{ J}$ of nuclear energy is released, the star’s radius $R$ has not had time to change yet.

Because $R$ hasn't changed yet, $E_{\text{gr}}$ is still $-200\text{ J}$. The $+10\text{ J}$ goes temporarily into thermal energy ($E_{\text{th}}$ jumps to $+110\text{ J}$), and therefore the total energy of the star increases by $+10\text{ J}$.
    
Its thermal energy ($+110\text{ J}$) is now too high compared to half its gravitational energy ($\frac{1}{2}\vert{}E_{\text{gr}}\vert{} = 100\text{ J}$). Physically, its outward gas pressure is now stronger than the inward pull of gravity. The star expands ($R$ increases). As the star expands to a larger radius $R_2 > R_1$, it has to lift its own mass outward against gravity. By conservation of energy, as it settles into its new virial equilibrium (state 2), its new total energy is fixed at $E_{\text{tot},2} = -90\text{ J}$. The new gravitational energy $E_{\text{gr},2}$ is $\mathbf{-180\text{ J}}$. It got smaller because the radius $R$ expanded. The new thermal energy $E_{\text{th},2}$ is $\mathbf{+90\text{ J}}$.

So far, we assumed that the star is made of an ideal monoatomic gas, which has an adiabatic index $\gamma = 5/3$ (where pressure and internal energy density $u_{\text{th}}$ are related by $P = (\gamma - 1)u_{\text{th}}$). We can generalize this to a gas with arbitrary adiabatic index $\gamma$.

First, see that:

$$C_v = \frac{dU}{dT} = \frac{f}{2}R$$

$$C_p = C_v + R = \frac{f}{2}R + R = \left(\frac{f}{2} + 1\right)R$$

$$\gamma = \frac{C_p}{C_v} = \frac{\left(\frac{f}{2} + 1\right)R}{\frac{f}{2}R} = \frac{\frac{f}{2} + 1}{\frac{f}{2}} = 1 + \frac{2}{f}$$

Then we can write $E_{\text{th}} = \frac{f}{2} Nk_B T = \frac{1}{\gamma - 1}Nk_B T$.

$$\bar{P}V = (\gamma - 1)E_{\text{th}}^{\text{tot}}$$

Substituting this into the virial equation $\bar{P}V = -\frac{1}{3}E_{\text{gr}}$ gives:

$$E_{\text{th}}^{\text{tot}} = -\frac{1}{3(\gamma - 1)}E_{\text{gr}}$$

and the total energy of the star becomes:

$$E_{\text{tot}} = E_{\text{th}}^{\text{tot}} + E_{\text{gr}} = \frac{3\gamma - 4}{3(\gamma - 1)}E_{\text{gr}}$$

Notice what happens as $\gamma \to 4/3$ (which occurs in very massive stars dominated by radiation pressure, or in relativistic white dwarfs approaching the Chandrasekhar limit): $3\gamma - 4 \to 0$, so the total binding energy $E_{\text{tot}} \to 0$! A star with $\gamma = 4/3$ is on the razor's edge of dynamical instability—any slight perturbation can cause it to either explode or collapse completely without an energy barrier.

We can also combine the generalized thermal energy $E_{\text{th}}^{\text{tot}} = \frac{1}{\gamma - 1}Nk_B \bar{T}$ with the generalized total energy $E_{\text{tot}} = -(3\gamma - 4)E_{\text{th}}^{\text{tot}}$ to write the gravothermal heat capacity $C_* = \frac{dE_{\text{tot}}}{d\bar{T}}$ directly in terms of $\gamma$:

$$C_* = -\frac{3\gamma - 4}{\gamma - 1} N k_B$$

For a monoatomic ideal gas ($\gamma = 5/3$), $C_* = -\frac{3}{2}Nk_B < 0$ (negative heat capacity). As $\gamma \to 4/3$, $C_* \to 0$, meaning the star can change its temperature and radius enormously with almost zero change in total energy.

Additionally, in the formula $\gamma = 1 + \frac{2}{f}$, notice what happens when a gas begins to dissociate (like $\text{H}_2 \to 2\text{H}$ in a collapsing molecular cloud) or ionize (like $\text{H I} \to \text{H II}$ or $\text{He II} \to \text{He III}$ in a stellar envelope). During ionization, any compression energy added to the gas goes into stripping electrons rather than increasing the translational kinetic energy (temperature) of the particles. This acts like a massive sink of internal degrees of freedom ($f_{\text{eff}} \gg 6$), driving the effective adiabatic index below $4/3$ (often down to $\gamma \approx 1.1\text{–}1.2$). By the total energy formula $E_{\text{tot}} = \frac{3\gamma - 4}{3(\gamma - 1)}E_{\text{gr}}$, when $\gamma < 4/3$, $E_{\text{tot}}$ becomes positive, triggering dynamical collapse (in protostars) or driving mechanical pulsations (the $\kappa$-$\gamma$ mechanism in Cepheid and RR Lyrae variable stars).

In physics, we define the gravitational potential energy of particles infinitely far apart ($R = \infty$) with zero kinetic energy as $E_{\text{tot}} = 0$. When $E_{\text{tot}} < 0$ we have a bound, stable star. The star is trapped at the bottom of an energy well. To disperse the star to infinity, you would have to inject a huge amount of positive energy from the outside.

When $E_{\text{tot}} = 0$, the radius $R$ has completely disappeared from the total energy. Because every possible radius $R$ has the exact same total energy ($E_{\text{tot}} = 0$), it costs zero energy to change the star's size. The star can collapse to a point or expand to infinity adiabatically (instantly, on the free-fall dynamical timescale $t_{\text{dyn}}$) without violating conservation of energy.
    
When $E_{\text{tot}} > 0$ (Unbound, $\gamma < 4/3$), the star has more internal thermal energy than gravity can hold onto—or, if compressed, releases more gravitational energy than its internal pressure can absorb, triggering runaway collapse.

---

**Aside:** The derivation $\gamma = 1 + \frac{2}{f}$ provides an intuitive way to see why relativistic gases (including photon gases / radiation pressure and ultra-relativistic degenerate electrons in massive white dwarfs) have $\gamma = 4/3$. For a non-relativistic particle with $f = 3$ translational degrees of freedom, the kinetic energy is quadratic in momentum ($\epsilon = \frac{p^2}{2m}$), and the equipartition theorem gives $\frac{1}{2}k_B T$ per quadratic degree of freedom, yielding $E_{\text{th}} = \frac{3}{2}Nk_B T$ and $\gamma = 1 + \frac{2}{3} = \frac{5}{3}$. However, for an ultra-relativistic particle, energy is linear in momentum ($\epsilon = pc$). Integrating over the Maxwell-Boltzmann (or Fermi-Dirac/Bose-Einstein) phase space with a linear dispersion relation yields twice the thermal energy per translational direction ($1\,k_B T$ per spatial dimension instead of $\frac{1}{2}k_B T$), so $E_{\text{th}} = 3Nk_B T$ and $P = \frac{1}{3}u_{\text{th}}$. Effectively, $f_{\text{eff}} = 6$, which gives:

$$\gamma = 1 + \frac{2}{6} = \frac{4}{3}$$

---

Now, going back to our integration to calculate $E_{\text{gr}}$:

$$E_{\text{gr}} = -\int_0^{r_*} \frac{GM(r)\rho(r)4\pi r^2 dr}{r}$$

The actual value of $E_{\text{gr}}$ depends on how the density varies with radius. If we assume constant density, we get:

$$E_{\text{gr}} = -\frac{3}{5}\frac{GM_*^2}{r_*}$$

However, in a real star, unsurprisingly, the weight of the overlying layers compresses the core, so density increases inward as radius decreases. This means more mass is closer together, which means the magnitude of $E_{\text{gr}}$ increases. Usually, we assume $E_{\text{gr}}$ is of the order of $-\frac{GM_*^2}{r_*}$. We can therefore get a Virial temperature from:

$$\frac{3}{2}Nk_B T_{\text{vir}} \sim \frac{1}{2}\frac{GM_*^2}{r_*} = \frac{1}{2}\frac{GM_* N\bar{m}}{r_*}$$

Assuming mostly ionized hydrogen, we get $\bar{m} \approx m_H / 2$.

$$T_{\text{vir}} \sim 4 \times 10^6\text{ K}$$

This is the characteristic average temperature of the Sun needed to maintain hydrostatic balance given the mass and gravitational potential of the Sun.

More generally, in stellar structure, stars are modeled as polytropes of index $n$ (where $P \propto \rho^{1 + 1/n}$, and larger $n$ means higher central concentration $\rho_c / \bar{\rho}$). A classic theorem (the Betti-Ritter theorem) gives the exact prefactor $\alpha$ for any polytrope of index $n$:

$$\alpha = \frac{3}{5 - n}$$

Here's how $\alpha$ behaves as central density increases:

| Polytropic Index ($n$) | Physical System | Central-to-Mean Density Ratio ($\rho_c / \bar{\rho}$) | Prefactor $\alpha$ in $E_{\text{gr}} = -\alpha\frac{GM^2}{R}$ |
| --- | --- | --- | --- |
| *(Hollow Shell)* | Mass at outer boundary $r=R$ | $0$ | $\alpha = \frac{1}{2} = \mathbf{0.50}$ |
| **$n = 0$** | Uniform-density sphere ($\rho = \text{const}$) | $1$ | $\alpha = \frac{3}{5} = \mathbf{0.60}$ |
| **$n = 1.5$** | Fully convective star / Low-mass white dwarf | $6.0$ | $\alpha = \frac{3}{3.5} = \frac{6}{7} \approx \mathbf{0.86}$ |
| **$n = 2$** | Centrally condensed sphere | $11.4$ | $\alpha = \frac{3}{3} = \mathbf{1.00}$ |
| **$n = 3$** | Standard Solar Model (Eddington Model) / Relativistic white dwarf | $54.2$ | $\alpha = \frac{3}{2} = \mathbf{1.50}$ |

---

#### Jeans Mass & Radius

The relationship between gravitational potential energy and thermal pressure gives us the mechanism through which large gaseous molecular clouds in the interstellar medium collapse to become stars.

Consider a large diffuse molecular cloud. If it contracts slightly (due to some perturbation or shock wave), the magnitude of its gravitational potential energy increases. Its thermal energy increases as well because the volume has contracted and work has been done on the gas.

$$\vert{}E_{\text{gr}}\vert{} \approx \frac{GM^2}{r}$$

If the cloud undergoes a radial compression $dr$, the gravitational energy will change (become more negative) by:

$$\vert{}dE_{\text{gr}}\vert{} = \frac{GM^2}{r^2}dr$$

The volume will decrease by:

$$dV = 4\pi r^2 dr$$

and the thermal energy will therefore grow by the work done ($P\,dV$):

$$dE_{\text{th}} = P\,dV = nk_B T 4\pi r^2 dr = \frac{\frac{M}{\bar{m}}}{\frac{4}{3}\pi r^3}k_B T 4\pi r^2 dr = 3\frac{M}{\bar{m}}k_B T\frac{dr}{r}$$

The cloud will be unstable to gravitational collapse if the magnitude of the change in gravitational energy is greater than the rise in thermal energy (and the pressure support it provides):

$$\vert{}dE_{\text{gr}}\vert{} > dE_{\text{th}}$$

Substituting from our expressions for $\vert{}dE_{\text{gr}}\vert{}$ and $dE_{\text{th}}$, we see that for a cloud of given radius $r$ and temperature $T$, collapse will occur if the mass is greater than the Jeans mass:

$$M_J = \frac{3k_B T}{G\bar{m}}r$$

Equivalently, a cloud of mass $M$ will collapse only if its radius is smaller than the Jeans radius:

$$r_J = \frac{G\bar{m}}{3k_B T}M$$

This condition can also be stated as a condition on the density, which must be larger than the Jeans density:

$$\rho_J = \frac{M}{\frac{4}{3}\pi r_J^3} = \frac{3}{4\pi M^2}\left(\frac{3k_B T}{G\bar{m}}\right)^3$$

Intuitively, what's happening here is that as density increases, it becomes easier for gravity to overpower thermal pressure, and so Jeans mass limit reduces. However, as temperature increases, thermal pressure is better able to contract gravity, and so Jean's mass limit increases. Similarly, if the total mass of the object is larger, then Jeans density limit is lower because the sheer mass provides enough gravitational pressure. A smaller mass would need each particle to be closer (and thus density to be higher) to trigger an overpowering gravitational contraction. 

It is especially useful to write these formulas in terms of temperature and density because in an extended interstellar cloud, the physically uniform properties are its $T$ and mass density $\rho_0$. If we substitute $r = \left(\frac{3M_J}{4\pi\rho_0}\right)^{1/3}$ into $M_J = \frac{3k_B T}{G\bar{m}}r$ and solve for $M_J$ and $r_J$ exclusively in terms of $T$ and $\rho_0$, we get two other standard forms of the Jeans Mass and Jeans Length:

$$M_J = \left(\frac{3}{4\pi\rho_0}\right)^{1/2}\left(\frac{3k_B T}{G\bar{m}}\right)^{3/2} \propto \left(\frac{T^3}{\rho_0}\right)^{1/2}$$
    
$$r_J = \left(\frac{9k_B T}{4\pi G\bar{m}\rho_0}\right)^{1/2} \propto \left(\frac{T}{\rho_0}\right)^{1/2}$$ 

This  is especially useful in understanding whether molecular clouds collapse from larger clouds progressively into smaller clouds or vice versa, because the ambient density and temperature can be considered the same for both smaller and larger clumps within the cloud.

For example, compare the entire $1000\,M_\odot$ cloud, with a $1\,M_\odot$ clump of gas inside the cloud (with the same temperature of $T = 20\text{ K}$ and number density of $10^2\text{–}10^4\text{ cm}^{-3}$), the Jeans density for this smaller clump is $10^6$ times larger ($\rho_J \propto M^{-2}$) than the entire cloud. Thus, the same density may be above the critical limit when we consider the entire cloud, but the smaller clumps may be stable against collapse. 

We can therefore expect the collapse of a molecular cloud to begin with the larger masses, which more easily pass the Jeans criterion. Moreover, during the initial collapse of a giant molecular cloud ($M \sim 10^3\text{–}10^5\,M_\odot$), the cloud is optically thin to infrared radiation from dust grains. Any compressional heat ($P\,dV$ work) is immediately radiated away into space, keeping the cloud isothermal ($T \approx \text{const.} \approx 10\text{–}20\text{ K}$). Because $T$ stays constant while the density $\rho_0$ increases by orders of magnitude as the cloud shrinks, the Jeans mass $M_J \propto \rho_0^{-1/2}$ steadily decreases as the collapse proceeds. 

Consequently, smaller and smaller sub-clumps inside the collapsing cloud drop below their local Jeans threshold and begin collapsing on their own, fragmenting a single $10^4\,M_\odot$ giant molecular cloud into a cluster of thousands of individual $0.1\text{–}10\,M_\odot$ stars.

If $M_J \propto \rho_0^{-1/2}$ keeps dropping as density rises, why doesn't a molecular cloud fragment all the way down into asteroid-sized or planet-sized pieces. Because eventually the collapsing fragments become so dense ($\rho \sim 10^{-13}\text{ g cm}^{-3}$) that they become optically thick to their own cooling radiation! Once photons are trapped, the collapse switches from isothermal ($T = \text{const.}$) to adiabatic ($P \propto \rho^\gamma \implies T \propto \rho^{\gamma - 1}$). Substituting $T \propto \rho^{\gamma - 1}$ into $M_J \propto T^{3/2}\rho^{-1/2}$ gives:

$$M_J \propto \rho^{\frac{3}{2}\gamma - 2}$$
    
For a diatomic molecular hydrogen gas ($\gamma = 7/5 = 1.4$) or monoatomic gas ($\gamma = 5/3$), the exponent $\frac{3}{2}\gamma - 2$ becomes positive ($+0.1$ or $+0.5$). That means as soon as the fragment becomes optically thick and heats up adiabatically, the Jeans mass stops decreasing and starts increasing with density because the trapped heat improves the thermal pressure's resistance to gravitational contraction. This halts any further fragmentation at a minimum fragment mass of $\sim 0.005\text{–}0.01\,M_\odot$ ($\sim 5\text{–}10\,M_{\text{Jupiter}}$).

**Acoustic Interpretation of the Jeans Length ($t_{\text{ff}} < t_{\text{sound}}$)**

Notice that the isothermal speed of sound in a gas is $c_s = \sqrt{\frac{k_B T}{\bar{m}}}$. In terms of $c_s$, your Jeans radius is simply:

$$r_J \sim \frac{c_s}{\sqrt{G\rho_0}} \sim c_s t_{\text{ff}}$$

Dividing both sides by $c_s$ gives the dynamical meaning of the Jeans criterion:

$$t_{\text{ff}} \sim \frac{1}{\sqrt{G\rho_0}} < \frac{r}{c_s} \equiv t_{\text{sound}}$$

A cloud collapses when its gravitational free-fall time ($t_{\text{ff}}$) is shorter than its sound-crossing time ($t_{\text{sound}}$)—meaning gravity pulls the cloud inward faster than pressure waves (sound waves) can propagate across the cloud to restore hydrostatic equilibrium.

### Mass Continuity

Nothing fancy here. This is just an expression for the mass of an infinitesimal mass shell in terms of the density:

$$dM(r) = \rho(r)4\pi r^2 dr, \quad \text{which is} \quad \frac{dM(r)}{dr} = 4\pi r^2\rho(r)$$

### Radiative Energy Transport

We looked at pressure and gravity. Is there something similar that determines the equilibrium temperature of a star in terms of the radius of some location in the star? Yes, there is. Temperature depends on radiative energy transfer, which is a fancy way of saying how much photon flux or luminosity is present at some point. To determine luminosity, we must determine how much opacity or obstruction a photon faces as it passes through some point in the star. This fundamentally comes down to how many particles are present and how likely those particles are to scatter or absorb a photon.

If $\sigma$ is the cross section of interaction of some particle and the number density of particles is $n$, then we can calculate the mean free path $l$, which gives us the average distance travelled by a photon between two interactions. This comes down to:

$$l = \frac{1}{n\sigma}$$

In reality, since there are multiple types of particles, we get:

$$l = \frac{1}{\sum_i n_i\sigma_i}$$

Since the number density of particles will be proportional to the mass density $\rho$ of the star at that point, we can subsume all this into a single $\kappa$ factor which stands for opacity (cross section per unit mass):

$$l = \frac{1}{\rho\kappa}$$

As opacity increases, as expected, the mean free path decreases, which means photons have many more scattering interactions. Similarly, the reverse holds as opacity decreases.

For the Sun, one of the most important interactions is Thomson scattering of photons on free electrons, which gives a mean free path of around $1\text{ mm}$. Note that the cross section of scattering is inversely proportional to the square of the scattering particle's mass ($\sigma_T \propto m^{-2}$, because a more massive charged particle undergoes a smaller acceleration $a = qE/m$ in the photon's oscillating electric field, and radiated scattered power scales as $a^2 \propto m^{-2}$). Protons, ions, and other heavier particles are therefore much less important from a scattering point of view than free electrons.

Since the scattering process is essentially a random walk, we can calculate the net distance $D$ travelled by a photon over $N$ steps by looking at the root-mean-square (RMS) distance travelled over $N$ random steps, which works out to:

$$D^2 = Nl^2 \implies D = \sqrt{N}l$$

We can get an idea of the time a photon takes to escape from the Sun by calculating the number of steps $N = r_*^2 / l^2$ needed to traverse the radius of the Sun, multiplied by the time $l/c$ taken to cover a single mean free path, which gives:

$$t_{\text{esc}} = \frac{l}{c}\frac{r_*^2}{l^2} = \frac{r_*^2}{lc} \approx 52,000\text{ yrs}$$

We can now calculate the net luminosity at $r$ by dividing the net energy difference across a shell of thickness $\Delta r$ by the diffusion time $(\Delta r)^2 / lc$ taken by photons to random-walk across that $\Delta r$ element, which is given by:

$$L(r) \approx -\frac{4\pi r^2\Delta r\Delta u}{(\Delta r)^2/lc} = -4\pi r^2 lc \frac{\Delta u}{\Delta r}$$

To account for the 3D angular distribution of photons, we actually need to integrate over $\cos^2\theta$. Specifically, a photon arriving at radius $r$ from angle $\theta$ relative to the radial direction was last scattered at radius $r - l\cos\theta$, where the energy density is $u(r - l\cos\theta) \approx u(r) - l\cos\theta\frac{du}{dr}$. And its radial component of velocity is $c\cos\theta$. Integrating the radial flux $c\cos\theta \, u(r - l\cos\theta)$ over all solid angles $\frac{d\Omega}{4\pi} = \frac{1}{2}\sin\theta\,d\theta$ kills the isotropic $u(r)$ term ($\int_0^\pi \cos\theta\sin\theta\,d\theta = 0$) and leaves:

$$F(r) = -cl\frac{du}{dr} \frac{1}{2}\int_0^\pi \cos^2\theta\sin\theta\,d\theta = -\frac{1}{3}cl\frac{du}{dr}$$

Thus we get the final formula:

$$\frac{L(r)}{4\pi r^2} = -\frac{cl}{3}\frac{du}{dr}$$

which tells us how energy diffuses outward in a star. The LHS is the energy flux, while the RHS is proportional to the energy density gradient. The mean free path and thus the opacity play a direct role in this equation. For a fixed temperature gradient, as opacity rises, the mean free path falls and therefore flux and luminosity fall.

We know that:

$$u = aT^4$$

$$\frac{du}{dr} = \frac{du}{dT}\frac{dT}{dr} = 4aT^3\frac{dT}{dr}$$

Substituting $l = \frac{1}{\rho(r)\kappa(r)}$ and $\frac{du}{dr}$, we get:

$$\frac{dT(r)}{dr} = -\frac{3L(r)\kappa(r)\rho(r)}{4\pi r^2 \cdot 4acT^3(r)} = -\frac{3\kappa(r)\rho(r)L(r)}{16\pi ac r^2 T^3(r)}$$

If we replace the derivatives in this formula with global scaling relations ($dT/dr \sim -T/R$, $\rho \sim M/R^3$) and rearrange for $L$, we get:

$$L \sim \frac{ac}{\kappa} \frac{R^4 T^4}{M}$$

Now substitute the Virial temperature scaling derived earlier ($T \sim \frac{GM m_H}{k_B R}$, so $R^4 T^4 \sim \left(\frac{GM m_H}{k_B}\right)^4$):

$$L \sim \left(\frac{ac G^4 m_H^4}{k_B^4}\right) \frac{M^3}{\kappa}$$

Notice that the stellar radius $R$ cancels out completely. For high-mass stars where Thomson scattering dominates ($\kappa = \text{const}$), this immediately yields the $L \propto M^3$ mass-luminosity relation we wrote about in the H-R diagram section!

### Energy Conservation

Unsurprisingly, energy conservation gives us another equation related to the equilibrium state of a star. Let us define $\epsilon(r)$ as the power produced per unit mass of stellar material. Energy conservation means that the addition to a star’s luminosity due to the energy production in a thin shell at radius $r$ is:

$$dL = \epsilon dm = \epsilon\rho 4\pi r^2 dr$$

or

$$\frac{dL(r)}{dr} = 4\pi r^2 \rho(r)\epsilon(r)$$

### Altogether Now!
We have now assembled the complete system of four first-order nonlinear differential equations that govern the interior structure of any static, spherically symmetric radiative star:

**Hydrostatic Equilibrium:** $\frac{dP}{dr} = -\frac{GM\rho}{r^2}$

**Mass Continuity:** $\frac{dM}{dr} = 4\pi r^2 \rho$
  
**Radiative Energy Transport:** $\frac{dT}{dr} = -\frac{3\kappa\rho L}{16\pi ac r^2 T^3}$

**Energy Conservation (Thermal Equilibrium):** $\frac{dL}{dr} = 4\pi r^2 \rho\epsilon$
    
To close and solve this system of $4$ differential equations for the $4$ primary radial functions ($M(r), P(r), L(r), T(r)$), a stellar model requires three constitutive relations from microphysics that express density, opacity, and energy generation in terms of pressure, temperature, and chemical composition ($X$):
    
$$P= P(\rho, T, X_i), \quad \kappa = \kappa(\rho, T, X_i), \quad \epsilon = \epsilon(\rho, T, X_i)$$
    
along with $4$ boundary conditions: two at the center ($M(0) = 0, L(0) = 0$) and two at the surface ($P(R_*) \approx 0, T(R_*) \approx T_{\text{eff}}$ or $T(r_*) \approx 0$ and $M(r_*) = M_*$).

#### Pressure and Equation of State
The microphysics is usually derived thusly: For pressure, we use the equation of state.

The element abundances and the ionization states of each element in the gas are commonly parametrized as the mass abundances of hydrogen, helium, and the heavier elements (the latter are often referred to collectively by the term “metals”) as:

$$X \equiv \frac{\rho_{\text{H}}}{\rho}, \quad Y \equiv \frac{\rho_{\text{He}}}{\rho}, \quad Z \equiv \frac{\rho_{\text{metals}}}{\rho}$$

$X$, $Y$, and $Z$ are mass fractions of the total gas density $\rho = \rho_{\text{H}} + \rho_{\text{He}} + \rho_{\text{metals}}$, they must strictly sum to unity at every point $r$ inside the star: $X + Y + Z = 1$

In the Sun's outer layers (representing the proto-solar nebula from which it formed), $X \approx 0.71$, $Y \approx 0.27$, and $Z \approx 0.02$. In the Sun's core today, after $4.6\text{ Gyr}$ of hydrogen fusion, $X$ has dropped to $\approx 0.34$ while $Y$ has risen to $\approx 0.64$.
    
We can connect $X, Y, Z$ to the Ideal Gas Equation of State ($P_g = \frac{\rho k_B T}{\mu m_H}$).

$$P_g = nk_B T = \frac{\rho}{\bar{m}} k_B T$$

$$\bar{m} = \frac{\rho}{n} = \frac{\rho}{n_{\text{H, free}} + n_{\text{He, free}} + n_{\text{metals, free}}}$$

More generally, the atomic number densities of hydrogen, helium, or an element of atomic mass number $A$ (i.e., an element with a total of $A$ protons and neutrons in each atomic nucleus) will be:

$$n_{\text{H}} = \frac{X\rho}{m_H}, \quad n_{\text{He}} = \frac{Y\rho}{4m_H}, \quad n_A = \frac{Z_A\rho}{Am_H}$$

where $Z_A$ is the mass abundance of an element of atomic mass number $A$. Complete ionization of hydrogen results in two particles (an electron and a proton); of helium, three particles (two electrons and a nucleus); and of an atom with atomic number $\mathcal{Z}$ (i.e., with $\mathcal{Z}$ protons or electrons), $\mathcal{Z} + 1$ particles, which for heavy enough atoms is always close to $A/2$.

Summing all free particles ($n = 2n_{\text{H}} + 3n_{\text{He}} + \sum_A (\mathcal{Z}+1)n_A \equiv \frac{\rho}{\mu m_H}$) yields the exact formula linking composition to the equation of state:

$$\frac{1}{\mu} = 2X + \frac{3}{4}Y + \frac{1}{2}Z$$

Thus we get:

$$P_g = \frac{\rho k_B T}{\mu m_H}$$

Additionally, we also have to consider the radiation pressure from photons. Consider photons inside a blackbody radiator with an intensity given by the Planck function, $I_\nu = B_\nu$, which, when integrated over frequency/wavelength, we denoted as $B$. The energy arriving at the surface of the radiator per unit time, per unit area, per unit solid angle, at some angle $\theta$ to the perpendicular to the surface, is $B \cos\theta$, because the area of the beam, when projected onto the wall of the radiator, is increased by $1/\cos\theta$. Now, consider the photons in the beam, which strike the fully reflective surface of the radiator at the angle $\theta$. Every photon of energy $E$ has momentum $p = E/c$. When reflected, it transmits to the surface a momentum $\Delta p = (2E/c)\cos\theta$. Therefore, there is a second factor of $\cos\theta$ that must be applied to the incoming beam. The rate of momentum transfer per unit area will be obtained by integrating over all incoming angles at which the photons hit the surface (the hemisphere $\theta \in [0, \pi/2]$). Since the rate of momentum transfer (i.e., the force) per unit area is, by definition, the pressure, we have:

$$P_{\text{rad}} = \frac{F}{A} = \frac{1}{A}\frac{dp}{dt} = \frac{2}{c} \int_0^{2\pi} d\phi \int_0^{\pi/2} B \cos^2\theta \sin\theta \, d\theta = \frac{4\pi}{3c}B = \frac{1}{3}u = \frac{1}{3}aT^4$$

The full equation of state for normal stars will therefore be:

$$P = P_g + P_{\text{rad}} = \frac{\rho k_B T}{\mu m_H} + \frac{1}{3}aT^4$$

---
**Aside 1:** Since we now have both the radiative transport equation and the radiation pressure formula $P_{\text{rad}} = \frac{1}{3}aT^4$, we can differentiate $P_{\text{rad}}$ with respect to radius:

$$\frac{dP_{\text{rad}}}{dr} = \frac{4}{3}aT^3 \frac{dT}{dr}$$

Substituting this directly into the radiative transport equation $\frac{dT}{dr} = -\frac{3\kappa\rho L}{16\pi ac r^2 T^3}$ eliminates $aT^3$ completely:

$$\frac{dP_{\text{rad}}}{dr} = -\frac{\kappa\rho L}{4\pi c r^2}$$

This is a remarkably clean physical statement: the outward force per unit volume exerted by escaping photons is $-\frac{dP_{\text{rad}}}{dr} = \frac{\kappa\rho L}{4\pi c r^2}$. In hydrostatic equilibrium, the total outward pressure gradient $\left\vert{}\frac{dP}{dr}\right\vert{} = \left\vert{}\frac{dP_g}{dr} + \frac{dP_{\text{rad}}}{dr}\right\vert{} = \frac{GM\rho}{r^2}$ cannot be smaller than the radiation pressure gradient alone (otherwise radiation force blows the star's outer layers into space). Setting $\left\vert{}\frac{dP_{\text{rad}}}{dr}\right\vert{} \le \frac{GM\rho}{r^2}$ gives the maximum possible luminosity a hydrostatic star of mass $M$ can have—the Eddington Luminosity:

$$L_{\text{Edd}} = \frac{4\pi G M c}{\kappa}$$

**Aside 2:** To analyze how the balance between gas pressure and radiation pressure changes with stellar mass, Arthur Eddington introduced the dimensionless parameter $\beta$, defined as the ratio of gas pressure to total pressure:

$$P_g = \beta P, \qquad P_{\text{rad}} = (1 - \beta)P$$

By substituting $P_g = \frac{\rho k_B T}{\mu m_H}$ and $P_{\text{rad}} = \frac{1}{3}aT^4$, we can eliminate $T$ and write the total pressure purely in terms of density $\rho$ and $\beta$:

$$P = \left[\frac{3}{a}\left(\frac{k_B}{\mu m_H}\right)^4 \frac{1 - \beta}{\beta^4}\right]^{1/3} \rho^{4/3}$$

Notice that if $\beta$ is roughly constant throughout a star, the star obeys a polytropic equation of state $P = K\rho^{4/3}$ (an $n=3$ polytrope)! Using the virial scaling $P \sim \frac{GM^2}{R^4}$ and $\rho \sim \frac{M}{R^3}$ (so $\rho^{4/3} \sim \frac{M^{4/3}}{R^4}$), the radius $R^4$ cancels out completely on both sides, yielding Eddington's Quartic Equation:

$$\frac{1 - \beta}{\beta^4} \propto \mu^4 M^2$$

This proves a profound fact about stellar astrophysics: the importance of radiation pressure $(1 - \beta)$ depends only on the star's mass $M$ (and composition $\mu$), not on its radius.

-   For the Sun ($M = 1\,M_\odot$), $1 - \beta \approx 10^{-3}$, so gas pressure provides $99.9\%$ of the support.
    
-   For a $50\text{–}100\,M_\odot$ O-type star, $\beta$ drops toward $0.5$ or lower—radiation pressure dominates the interior, driving the adiabatic index $\gamma$ toward $4/3$ and destabilizing the star against pulsations and mass loss.

---

#### Energy Generation
For $\epsilon(r)$, in a fully general star, the specific energy generation rate $\epsilon(r)$ (measured in $\text{erg}\cdot\text{g}^{-1}\cdot\text{s}^{-1}$) is actually the sum of three terms:

$$\epsilon(r) = \epsilon_{\text{nuc}} - \epsilon_\nu + \epsilon_{\text{grav}}$$
    
$\epsilon_{\text{nuc}}$ is the energy released by nuclear fusion (such as the proton-proton chain, where $\epsilon_{\text{pp}} \propto \rho T^4$, or the CNO cycle, where $\epsilon_{\text{CNO}} \propto \rho T^{16}$). Because of this extreme temperature sensitivity, $\epsilon_{\text{nuc}}$ is non-zero only in the innermost core ($r \lesssim 0.25\,R_\odot$); outside the core, $\epsilon(r) \approx 0$ and $L(r) = L_* = \text{constant}$.
        
$-\epsilon_\nu$ accounts for energy carried away directly by neutrinos, which escape the star without interacting with the gas or contributing to the photon luminosity $L(r)$.
        
$\epsilon_{\text{grav}} = -T\frac{ds}{dt}$ (where $s$ is specific entropy) is the gravothermal energy release from contraction or expansion. For a steady-state main-sequence star, $\epsilon_{\text{grav}} = 0$, whereas for a pre-main-sequence protostar with no nuclear fusion, $\epsilon_{\text{grav}}$ is the entire source of luminosity!

The equations for energy production via nuclear fusion are rather messy. But suffice to say they follow a power-law nuclear energy generation rate $\epsilon \sim \rho T^\nu$ (where $\nu \approx 4$ for the proton-proton chain in solar-type stars, and $\nu \approx 16$ for the CNO cycle in massive stars). Equating the luminosity produced by fusion ($L \sim M\rho T^\nu \sim \frac{M^2}{r^3} \left(\frac{M}{r}\right)^\nu$) with the luminosity carried away by radiative transport ($L \sim M^3$ for electron scattering) gives:

$$M^3 \sim M^{\nu + 2} r^{-(\nu + 3)} \implies r \sim M^{\frac{\nu - 1}{\nu + 3}}$$

For massive stars burning hydrogen via the CNO cycle ($\nu \approx 16$):  $r \sim M^{15/19} = M^{0.79}$, which is very close to $r \sim M$.
    
In the limit of an infinitely steep thermostat ($\nu \to \infty$, meaning fusion turns on like a step-function at a fixed ignition temperature $T_c$),  $\frac{\nu - 1}{\nu + 3} \to 1$, recovering our approximation $r \sim M$ and $T_c = \text{const.}$.

#### Opacity

We already mentioned that Thomson scattering of free electrons is one of the biggest contributors to opacity.

Let us now calculate correctly the electron density for an ionized gas of arbitrary abundance (rather than pure hydrogen, as before):

$$n_e = n_{\text{H}} + 2n_{\text{He}} + \sum_A \frac{A}{2}n_A = \frac{\rho}{m_H}\left(X + \frac{2}{4}Y + \frac{1}{2}Z\right) = \frac{\rho}{m_H}\left(X + \frac{1}{2}(Y+Z)\right) = \frac{\rho}{m_H}\left(X + \frac{1}{2}(1-X)\right) = \frac{\rho}{2m_H}(1+X)$$

where we have again assumed that the number of electrons in an atom of mass number $A$ is $A/2$. Therefore:

$$\kappa_{\text{es}} = \frac{n_e\sigma_T}{\rho} = \frac{\sigma_T}{2m_H}(1 + X) = 0.2(1 + X)\text{ cm}^2\text{ g}^{-1}$$

In regions of a star with relatively low temperatures, such that some or all of the electrons are still bound to their atoms, three additional processes that are important sources of opacity are bound-bound, bound-free (also called photoionization), and free-free absorption. In bound-bound and bound-free absorption, which we have already discussed in the context of photospheric absorption features, an atom or ion is excited to a higher energy level, or ionized to a higher degree of ionization, by absorbing a photon. Free-free absorption is the inverse process of free-free emission, often called Bremsstrahlung (“braking radiation” in German). In free-free emission, a free electron is accelerated by the electric potential of an ion, and as a result radiates a photon. Conversely, in free-free absorption, a photon is absorbed by a free electron and an ion, which share the photon’s momentum and energy. All three processes depend on photon wavelength, in addition to gas temperature, density, and composition.

When averaged over all wavelengths, the “mean opacity” due to both bound-free absorption and free-free absorption behaves approximately as:

$$\bar{\kappa}_{\text{bf,ff}} \sim \frac{\rho}{T^{3.5}}$$

which is called a Kramers opacity law. This behavior holds only over limited ranges in temperature and density. For example, free-free absorption actually increases with temperature at low temperature and density, with the increase in free electron density. Similarly, bound-free opacity cuts off at high temperatures at which the atoms are fully ionized. Additional sources of opacity, significant especially in low-mass stars, are molecules and $\text{H}^-$ ions.
        
---

**Aside:** When solving these four equations numerically, we almost always divide the other three equations by your mass continuity equation $dM = 4\pi r^2 \rho\,dr$ to use the enclosed mass $M$ (rather than radius $r$) as the independent variable. In mass coordinates, your energy conservation equation becomes simply: $\frac{dL}{dM} = \epsilon$

This is much cleaner for tracking stellar evolution because the total mass $M_*$ of a star remains constant even when its radius $R_*$ expands by orders of magnitude into a red giant.

---
### Applying Scaling Approximations to the HR Diagram

The first three differential equations (hydrostatic equilibrium, mass continuity, and radiative transport) can be written as scaling relations:

$$P \sim \frac{M\rho}{r}$$

$$M \sim r^3\rho$$

$$L \sim \frac{T^4 r}{\kappa\rho}$$

(just as, instead of solving a differential equation, say,  $df/dx = x^4$, we can write directly $f \sim x^5$).

These three relations can be conceptually understood in the following way: Hydrostatic balance is simply gas pressure equated to gravitational potential energy density ~ $GM^2/R/V = GM/R*M/V \sim M \rho/R$

The second relation is just the formula for density: $\rho \sim M/R^3$ rearranged.

The third one relates the luminosity to the gradient of radiative energy density: $L \sim d(aT^4)/dR * 4\pi R^2*mean free path \sim T^4R/\kappa \rho$. Now let us apply these approximations to different situations. 

For moderately massive stars, the pressure will be dominated by the kinetic gas pressure, and the opacity by electron scattering. Therefore $P \sim \rho T$ and $\kappa = \text{const.}$

Substituting $P \sim \rho T$ in $P \sim \frac{M\rho}{r}$, we get $T \sim \frac{M}{r}$. Substituting this into $L \sim \frac{T^4 r}{\kappa\rho}$ and using $M \sim r^3\rho$, we get:

$$L \sim M^3$$

$T \sim \frac{M}{r}$ also suggests that $r \sim M$ on the main sequence. To see this, consider a star that is forming from a mass $M$ that is contracting under its own gravity and heating up.  The contraction will stop, and an equilibrium will be set up, once the density and the temperature in the core are high enough for the onset of nuclear reactions. We will see that the nuclear power density depends mainly on temperature. Thus, for any initial mass, $r$ will stop shrinking when a particular core temperature is reached. Therefore, the internal temperature $T$ is comparable in all main-sequence stars (i.e., it is weakly dependent on mass, and hence approximately constant), and:

$$r \sim M$$

Detailed models confirm that the core temperature varies only by a factor $\approx 4$ over a range of $\sim 100$ in mass on the main sequence. With $r \sim M$, we see from $M \sim r^3\rho$ that the density of a star decreases as $\rho \sim M^{-2}$, so that more massive stars will have low density, and low-mass stars will have high density. 

For example, the Sun ($1\,M_\odot$) has a mean density $\bar{\rho}_\odot \approx 1.4\text{ g cm}^{-3}$. But a $20\,M_\odot$ O-type star has a mean density roughly $20^{-2} = \frac{1}{400}$ of the Sun's ($\bar{\rho} \approx 0.0035\text{ g cm}^{-3}$, comparable to terrestrial air), which is why bound-free/free-free collisions ($\kappa \propto \rho$) become negligible and radiation pressure ($P_{\text{rad}}/P_g \propto T^3/\rho$) takes over. Conversely, a $0.1\,M_\odot$ red dwarf has a mean density roughly $100$ times the Sun's ($\bar{\rho} \sim 100\text{ g cm}^{-3}$), driving Kramers opacity so high that radiative transport breaks down completely and the entire star becomes fully convective.

Proceeding to low-mass stars, the high density means there is a dominant role for bound-free and free-free opacity:

$$\kappa \sim \frac{\rho}{T^{3.5}}$$

Since $T \sim \text{const.}$,  $r \sim M$, and $\rho \sim M^{-2}$, then $\kappa \sim \rho \sim M^{-2}$, and $L \sim \frac{T^4 r}{\kappa\rho}$ gives:

$$L \sim \frac{T^4 r}{\kappa\rho} \sim \frac{r}{\rho^2} \sim M^5$$

as seen in low-mass stars.

For the most massive stars, the low gas density will make radiation pressure dominant in the equation of state:

$$P \sim T^4$$

and electron scattering, with $\kappa = \text{const.}$, will again be the main source of opacity. Equating $P \sim T^4$ with $P \sim \frac{M\rho}{r}$ and substituting for $T^4$ in $L \sim \frac{T^4 r}{\kappa\rho}$, we find:

$$L \sim M$$

a flattening of the mass-luminosity relationship that is, in fact, observed for the most massive stars.

Finally, we can also reproduce the functional dependence of the main sequence in the H-R diagram. We saw that $L \sim M^5$ for low-mass stars and $L \sim M^3$ for moderately massive stars. Let us then take an intermediate slope, $L \sim M^4$, as representative. Since $r \sim M$, then:

$$\sigma T_E^4 = \frac{L}{4\pi r_*^2} \sim \frac{M^4}{M^2} \sim M^2 \sim L^{1/2}$$

so:

$$L \sim T_E^8$$

We have thus seen that the mass vs. luminosity relation and the surface-temperature vs. luminosity relation of main-sequence stars are simply consequences of the different sources of pressure and opacity in stars of different masses, and of the fact that the onset of nuclear hydrogen burning keeps the core temperatures of all main-sequence stars in a narrow range.

### Convection

Under certain conditions, the main means of energy transport in some regions of a star is convection, rather than radiative transport. Convection occurs when a volume element of material that is displaced from its equilibrium position, rather than returning to the original position, continues moving in the displacement direction. For example, if the displacement is upward to a region of lower density, and after the displacement the density of the volume element is lower than that of its new surroundings, the element will continue to be buoyed upwards. When convection sets in, it is very efficient at transporting heat, and becomes the dominant transport mechanism.

For convection, note that density of a material reduces as it gets hotter. Thus we need to check if, as a blob of gas rises in the stellar atmosphere, the magnitude of temperature drop of the surrounding stellar gas is higher than the magnitude of temperature drop of the blob. If this holds, then the density of the blob will be lower than the surrounding gas as it rises and it will continue to rise, setting up convection. So convection sets in when:

$$\left\vert{}\frac{dT}{dr}\right\vert{} > \frac{\gamma - 1}{\gamma}\frac{T}{P}\left\vert{}\frac{dP}{dr}\right\vert{}$$

Note that on the RHS, we have assumed that the blob of gas expands adiabatically into lower pressure, which means it does work and cools down. The RHS is essentially $\left\vert{}\frac{dT}{dr}\right\vert{}_{\text{ad}}$. To arrive at the RHS, starting from $P V^\gamma = \text{constant}$ and $P V = N k_B T$, differentiating the first equation with respect to $R$ gives a relationship between $dP/dR$ and $dV/dR$, which can be substituted into the second equation. 

For a non-relativistic gas without internal degrees of freedom (e.g., ionized hydrogen), $\gamma = 5/3$. As the number of internal degrees of freedom increases, $\gamma$ becomes smaller, making convection possible even if $\vert{}dT/dr\vert{}$ is small. This can occur when the gas is made of atoms, which can be excited or ionized, or of molecules that have rotational and vibrational degrees of freedom and can be dissociated. Convection therefore occurs in some cool regions of stars, where atoms and molecules exist. This applies to the outer layers of intermediate-mass main-sequence stars and red giants, and to large ranges in radius in low-mass stars. Another range of applicability of convection is in the cores of massive stars because of an extremely steep radiative temperature gradient $\left\vert{}\frac{dT}{dr}\right\vert{}$, and secondarily because strong radiation pressure in the most massive stars lowers the adiabatic index $\gamma$ toward $\frac{4}{3}$. The Sun is convective in the outer $28\%$ of its radius.

Once convection sets in, it mixes material at different radii and thus works toward equilibrating temperatures, i.e., lowering the absolute value of the temperature gradient $\vert{}dT/dr\vert{}$. Therefore, convection can be implemented into stellar structure computations by testing, at every radius, if the convection condition has been met. If it has, convection will bring the temperature gradient back to its critical value, and therefore the equilibrium equation for radiative energy transport, $\frac{dT(r)}{dr} = -\frac{3L(r)\kappa(r)\rho(r)}{4\pi r^2 4acT(r)^3}$, can be replaced by the equation for convection, but with an equality sign:

$$\frac{dT}{dr} = \frac{\gamma - 1}{\gamma}\frac{T(r)}{P(r)}\frac{dP}{dr}$$

The inequality $\left\vert{}\frac{dT}{dr}\right\vert{} > \frac{\gamma - 1}{\gamma}\frac{T}{P}\left\vert{}\frac{dP}{dr}\right\vert{}$ is known as the Schwarzschild Criterion. Its derivation follows directly from comparing a rising fluid parcel ("blob") to the surrounding stellar medium:
    
Suppose a parcel at radius $r$ with initial density $\rho$, pressure $P$, and temperature $T$ (matching its surroundings) is displaced upward by $dr$ to $r + dr$.
        
Because the speed of sound is much faster than the convective motion, the parcel immediately expands to match the ambient pressure of its new surroundings: $P_{\text{blob}}(r+dr) = P_{\text{env}}(r+dr) = P + \frac{dP}{dr}dr$.
        
Because radiative heat exchange across a macroscopic parcel is slow compared to its rise time, the parcel expands adiabatically ($P\rho^{-\gamma} = \text{const.}$, or via the ideal gas law $P \propto \rho T$, $T P^{\frac{1-\gamma}{\gamma}} = \text{const.}$). Differentiating logarithmically gives the adiabatic temperature change of the rising blob:
        
$$\left(\frac{dT}{dr}\right)_{\text{ad}} = \frac{\gamma - 1}{\gamma}\frac{T}{P}\frac{dP}{dr}$$
        
The parcel will be buoyant and continue accelerating upward if its new density is _lower_ than the surrounding ambient density ($\rho_{\text{blob}} < \rho_{\text{env}}$). Since $P_{\text{blob}} = P_{\text{env}}$ and $P \propto \rho T$ (at constant composition $\mu$), lower density means the blob must be hotter than its new surroundings ($T_{\text{blob}} > T_{\text{env}}$). Since both $T_{\text{blob}}$ and $T_{\text{env}}$ decrease outward ($\frac{dT}{dr} < 0$), $T_{\text{blob}} > T_{\text{env}}$ requires that the ambient temperature drops _steeper_ than the blob's adiabatic cooling rate:
        
$$\left\vert{}\frac{dT}{dr}\right\vert{}_{\text{env}} > \left\vert{}\frac{dT}{dr}\right\vert{}_{\text{ad}} = \frac{\gamma - 1}{\gamma}\frac{T}{P}\left\vert{}\frac{dP}{dr}\right\vert{}$$
        
#### Three Physical Triggers for Convection

If you compare the radiative temperature gradient required to carry luminosity $L(r)$:
    
$$\left\vert{}\frac{dT}{dr}\right\vert{}_{\text{rad}} = \frac{3\kappa\rho L(r)}{16\pi ac r^2 T^3}$$
    
against the adiabatic threshold $\left\vert{}\frac{dT}{dr}\right\vert{}_{\text{ad}} = \frac{\gamma - 1}{\gamma}\frac{T}{P}\left\vert{}\frac{dP}{dr}\right\vert{}$, you can immediately see the three distinct physical mechanisms that trigger convection in stars:
    
1.  **Large $\kappa$ (High Opacity in Cool Outer Envelopes):** In the cool outer layers of low-mass stars ($M \lesssim 1.3\,M_\odot$) and red giants, Kramers and $\text{H}^-$ opacity become enormous, blocking radiative diffusion and making $\left\vert{}\frac{dT}{dr}\right\vert{}_{\text{rad}}$ spike above the adiabatic limit.
        
2.  **Small $\gamma$ (Partial Ionization Zones):** As you noted in your text, in regions where $\text{H I} \to \text{H II}$ ($T \sim 10^4\text{ K}$) or $\text{He I} \to \text{He II} \to \text{He III}$ ($T \sim 4 \times 10^4\text{ K}$), energy goes into stripping electrons rather than raising kinetic temperature. This drives $\gamma$ down from $5/3$ ($1.67$) toward $1.1\text{–}1.2$, shrinking the right-hand side factor $\frac{\gamma - 1}{\gamma}$ from $0.4$ down to $\sim 0.1$ and easily triggering convection.
        
3.  **Large $\frac{L(r)}{4\pi r^2}$ (Concentrated Core Fusion in Massive Stars):** You mentioned that massive stars have convective cores even though they are hot and fully ionized ($\gamma = 5/3$ and $\kappa = \kappa_{\text{es}}$ is low). Why? Because massive stars ($M \gtrsim 1.3\,M_\odot$) fuse hydrogen via the **CNO cycle**, whose energy generation rate scales as $\epsilon_{\text{CNO}} \propto T^{16}$. This extreme temperature sensitivity concentrates almost the entire luminosity $L$ inside a tiny central core radius $r$, making the local flux $\frac{L(r)}{4\pi r^2}$ (and thus $\left\vert{}\frac{dT}{dr}\right\vert{}_{\text{rad}}$) so huge that only vigorous core convection can carry the heat out!
        
#### Polytropic Structure of Fully Convective Stars ($n = 1.5$ Polytrope)
    
When convection dominates and enforces the equality $\frac{dT}{dr} = \frac{\gamma - 1}{\gamma}\frac{T}{P}\frac{dP}{dr}$, you can integrate both sides immediately to get $T \propto P^{\frac{\gamma - 1}{\gamma}}$. Combining this with the ideal gas law $P \propto \rho T$ yields a **polytropic equation of state**:
    
$$P = K\rho^\gamma = K\rho^{1 + 1/n}$$
    
For a monoatomic fully ionized gas ($\gamma = 5/3$), a fully convective star (such as a low-mass red dwarf with $M < 0.35\,M_\odot$, or a pre-main-sequence protostar on the Hayashi track) has a structure given strictly by an **$n = 1.5$ polytrope** ($P = K\rho^{5/3}$), completely independent of its opacity $\kappa$!
    
#### The Ledoux Criterion (Composition Gradients)
    
The Schwarzschild criterion assumes the chemical composition (mean molecular weight $\mu$) is uniform across radius $r$. Near the edge of a nuclear-burning core where helium ($Y$) builds up inside hydrogen ($X$), $\mu$ decreases outward ($\frac{d\mu}{dr} < 0$). A heavier helium-rich blob displaced upward into lighter hydrogen experiences an extra downward buoyancy force that resists convection, adding a stabilizing composition term known as the Ledoux Criterion:
    
$$\left\vert{}\frac{d\ln T}{d\ln P}\right\vert{} > \frac{\gamma - 1}{\gamma} + \frac{\ln \mu}{\ln P}$$

## Stellar Evolution & Remnants

We know that $L \sim M^\alpha$. We also know that the energy source is nuclear reactions, whereby a fraction of a star’s rest mass is converted to energy and radiated away. The total radiated energy is therefore proportional to mass, $L t_{\text{ms}} \sim E \sim M$, and:

$$t_{\text{ms}} \sim \frac{M}{L} \sim M^{1-\alpha}$$

For intermediate-mass stars, which obey a mass-luminosity relation with $\alpha \sim 3$, $t_{\text{ms}} \sim M^{-2}$. For the most massive stars, $\alpha \sim 1$, the result of electron-scattering opacity and radiation pressure. The lifetime $t_{\text{ms}}$ therefore becomes independent of mass and reaches a limiting value for $M > 30\,M_\odot \to t_{\text{ms}} \sim 3 \times 10^6\text{ yr}$. Thus, the more massive a star, the shorter its hydrogen-burning phase on the main sequence, and the lifespan hits a limit at around $30$ solar masses.

### Post-Main Sequence Nuclear Reactions

[Once most of the hydrogen](https://physics.weber.edu/palen/phsx1040/images/hrlowmass.jpg) in the core of a star has been converted into helium, the core contracts and the inner temperatures rise. As a result, [hydrogen in the less-processed regions](https://e7.pngegg.com/pngimages/69/33/png-clipart-hertzsprung-russell-diagram-asymptotic-giant-branch-giant-star-horizontal-branch-stellar-evolution-star-angle-text-thumbnail.png) outside the core starts to burn in a shell surrounding the core. Stellar models consistently predict that, at this stage, there is a huge expansion of the outer layers of the star. This phenomenon is widely known in stellar evolution as the Mirror Principle: whenever a star develops an active nuclear-burning shell separating a contracting core from an outer envelope, radial contraction inside the shell causes radial expansion outside the shell (and vice versa during core helium ignition, when core expansion causes the envelope to contract back leftward onto the Horizontal Branch).

The increase in luminosity, due to the gravitational contraction and the hydrogen shell burning, moves the star up in the H-R diagram, while the increase in radius lowers the effective temperature, moving the star to the right on the diagram into the red giant phase. The red-giant phase is brief compared to the main sequence, lasting roughly one-tenth the time.

As the red-giant phase progresses, the helium core contracts and heats up, while additional helium “ash” is deposited on it by the hydrogen-burning shell. At some point, helium burning can become effective through the “triple-alpha” reaction:

$$^4\text{He} + {}^4\text{He} + {}^4\text{He} \to {}^{12}\text{C} + \gamma\,(7.275\text{ MeV})$$

This is the only reaction that can produce elements heavier than helium when we start off with only hydrogen and helium because there are no stable nuclei in nature with mass number $A = 5$ ($^5\text{He}, {}^5\text{Li}$) or $A = 8$ ($^8\text{Be}$). Along with carbon production, some oxygen and neon can also be synthesized.

At this point, the star moves quickly on the H-R diagram to the left edge of the “horizontal branch”, and then starts to evolve at a mild pace to the right along the horizontal branch. Horizontal branch evolution lasts only about $1\%$ of the main-sequence lifetime. Once the helium in the core has been exhausted, the core (now composed mainly of oxygen and carbon) contracts again, until a surrounding shell of helium ignites, with a hydrogen-burning shell around it. The star rises up the “asymptotic giant branch” where double shell burning—a helium-burning shell within a hydrogen-burning shell—takes place.

Evolved stars undergo large mass loss, especially on the red giant branch and on the asymptotic giant branch, as a result of the low gravity in their extended outer regions and the radiation pressure produced by their large luminosities. Mass loss is particularly severe on the asymptotic giant branch during so-called thermal pulses—roughly periodic flashes of enhanced helium shell burning. These mass outflows, or stellar “winds”, lead to mass-loss rates of up to $10^{-4}\,M_\odot\text{ yr}^{-1}$, which rid a star of a large fraction of its initial mass. Giants are highly convective throughout their volumes, leading to a dredge-up of newly synthesized elements from the core to the outer layers, where they are expelled with the winds.

Finally, the exposed remnant of the original core, called a “white dwarf”, reaches the endpoint of stellar evolution for stars of this mass.

### White Dwarfs
#### Equation of State
After each contraction, the density of the core increases. At some point, the distances between particles will be smaller than their de Broglie wavelengths. At that point, our previous assumption of a classical (rather than quantum) ideal gas, which we used to derive the equation of state, becomes invalid.

Recall that the de Broglie wavelength of a particle of momentum $p$ is:

$$\lambda = \frac{h}{p} = \frac{h}{(2mE)^{1/2}} \approx \frac{h}{(3mk_B T)^{1/2}}$$

where we have represented the energy with the mean thermal energy of a particle, $E \sim \frac{3}{2}k_B T$. Since electrons and protons share the same thermal energy, but the mass of the electron is much smaller than the mass of the proton or of other nuclei, the wavelengths of the electrons are longer, and it is the electron density which will first reach the quantum domain. At interparticle separations of order less than half a de Broglie wavelength, quantum effects should become important, corresponding to a quantum density of:

$$\rho_q \approx \frac{m_p}{(\lambda_e/2)^3} = \frac{8m_p(3m_e k_B T)^{3/2}}{h^3}$$

Note that even a very dense gas can remain classical if it is hot enough, because the high momentum ensures a very small de Broglie wavelength.

Instead of the Maxwell-Boltzmann distribution, the energy distribution at quantum densities will follow Bose-Einstein statistics for bosons (particles with spin that is an integer multiple of $\hbar$) or Fermi-Dirac statistics for fermions.

In a white dwarf, the electrons reach degeneracy before neutrons or protons, and so we look at the Fermi sea created by electrons at the core of the white dwarf. The Fermi sea refers to how every available momentum/energy state up to the Fermi energy $E_F$ (or Fermi momentum $p_F$) is occupied.

Each single quantum state occupies a 6-dimensional phase-space volume of $h^3 = dx\,dy\,dz\,dp_x\,dp_y\,dp_z$. Because electrons are spin-$1/2$ fermions, each phase-space cell of volume $h^3$ can hold at most $g_s = 2$ electrons (spin up $\uparrow$ and spin down $\downarrow$). Per unit spatial volume ($dx\,dy\,dz = 1$), the momentum-space shell between $p$ and $p + dp$ is a spherical shell of volume $4\pi p^2 dp$. Multiplying the spin degeneracy ($2$) by the spherical momentum shell ($4\pi p^2 dp$) and dividing by $h^3$ gives $\frac{8\pi p^2 dp}{h^3}$. Inverting the result gives the Fermi momentum in terms of electron density:
    
$$p_F = \left(\frac{3h^3}{8\pi} n_e\right)^{1/3} = \hbar (3\pi^2 n_e)^{1/3}$$
    
 Notice that $p_F \propto n_e^{1/3} \propto \rho^{1/3}$ is completely independent of temperature $T$

Integrating over all momenta from $0$ to $p_F$ gives a relation between the electron number density $n_e$ and $p_F$:

$$n_e = \int_0^{p_F} \frac{8\pi}{h^3} p^2 dp = \frac{8\pi}{3h^3} p_F^3$$

Let us now calculate the equation of state of an ideal gas. Consider a container with a flat wall of area $A$ perpendicular to the $+x$-axis, and look at the subset of particles that have momentum magnitude between $p$ and $p+dp$ (number density $n(p)\,dp$). 

The change in momentum of the particle upon bouncing of a wall is $\Delta p_{\text{one}} = \mathbf{2\,p_x}$, and there are $dN_{\text{hits}} = \mathbf{\frac{1}{2}}\,n(p)\,dp \cdot (A\,\vert{}v_x\vert{}\,\Delta t)$, where the division by 2 comes because only half the particles are moving towards the wall. The other half are moving away from it. 

Now we get

$$dP_x^{\text{wall}} = \Delta p_{\text{one}} \cdot dN_{\text{hits}} = \left(\mathbf{2}\,\vert{}p_x\vert{}\right) \cdot \left(\mathbf{\frac{1}{2}}\,n(p)\,dp \cdot A\,\vert{}v_x\vert{}\,\Delta t\right)$$

Dividing by area $A$ and time $\Delta t$ to get the pressure contribution $dP = \frac{dF}{A} = \frac{dP_x^{\text{wall}}}{A\,\Delta t}$:

$$dP = n(p)\,\langle p_x v_x \rangle\,dp$$

Because the gas is isotropic (no preferred direction in 3D space), the average along the $x$, $y$, and $z$ axes must be equal:

$$\langle p_x v_x \rangle = \langle p_y v_y \rangle = \langle p_z v_z \rangle = \frac{1}{3}\langle p_x v_x + p_y v_y + p_z v_z \rangle = \mathbf{\frac{1}{3}\,p\,v}$$

Substituting $\langle p_x v_x \rangle = \frac{1}{3}p\,v$ and integrating over all momentum magnitudes $p$ from $0$ to $\infty$ yields:

$$P = \frac{1}{3}\int_0^\infty n(p)\,p\,v\,dp$$

We could have also arrived at this by considering how much pressure a single particle exerts on a wall, which is basically the change in momentum along with the time taken by the particle to traverse the length of the box and back, i.e., $2L$.

Replacing $n(p)$ with the Maxwell-Boltzmann distribution recovers the classical equation of state, $P = nk_B T$. For a non-relativistic degenerate electron gas, however, we replace $n(p)$ with the zero-temperature Fermi-Dirac distribution (where $n(p) = \frac{8\pi p^2}{h^3}$ for $p \le p_F$ and $0$ for $p > p_F$, with $v = \frac{p}{m_e}$):

$$P_e = \frac{1}{3}\int_0^{p_F} \frac{8\pi}{h^3}\frac{p^4}{m_e}dp = \frac{8\pi}{3h^3 m_e}\frac{p_F^5}{5} = \left(\frac{3}{8\pi}\right)^{2/3}\frac{h^2}{5m_e}n_e^{5/3}$$

There is another way to approximately arrive at this equation of state for degenerate elctrons. If there are $n$ particles per unit volume, each particle occupies a tiny cube of volume $(\Delta x)^3 = \frac{1}{n}$. Taking the cube root gives the linear spacing between particles: $\Delta x = n^{-1/3}$

Using the de Broglie / Heisenberg relation $p \sim \frac{h}{\Delta x}$ and substituting $\Delta x = n^{-1/3}$ gives: $p \sim \frac{h}{n^{-1/3}} = h\,n^{1/3}$
       
Substituting $p \sim h\,n^{1/3}$ into the non-relativistic kinetic energy $E = \frac{p^2}{2m}$ gives: $E \sim \frac{p^2}{2m} \sim \frac{h^2\,n^{2/3}}{2m}$
    
Multiplying the number of particles per unit volume ($n$) by the energy per particle ($E$) gives: $P \sim n \cdot E \sim n \left(\frac{h^2\,n^{2/3}}{2m}\right) \sim \frac{h^2}{2m}\,n^{5/3}$

To relate $n_e$ to the mass density appearing in the equations of stellar structure, consider a fully ionized gas composed of a particular element, of atomic number $Z$ and atomic mass number $A$, and a density of ions $n_+$. Then:

$$n_e = Zn_+ = Z\frac{\rho}{Am_p}$$

Substituting this into the expression for $P_e$, we obtain a useful form for the equation of state of a degenerate non-relativistic electron gas:

$$P_e = \left(\frac{3}{\pi}\right)^{2/3}\frac{h^2}{20m_e m_p^{5/3}}\left(\frac{Z}{A}\right)^{5/3}\rho^{5/3}$$

The important feature of this equation of state is that the electron pressure does not depend on temperature.

As opposed to the electrons, the nuclei at such densities are still completely in
the classical regime due to huge difference in mass between nucleons and electrons, since for the same $\delta x$ and $\delta p$, the velocity of the nucleon is much lower (and therefore the time taken by it to traverse a unit length is higher, which means fewer impacts on "walls"), which means it exerts far less pressure than electrons.

#### Properties of White Dwarfs

From gravitational potential energy (hydrostatic equilibrium), we know that:

$$P \sim \frac{GM\rho}{r} \sim \frac{GM^2}{r^4}$$

The degenerate electron-gas equation of state is:

$$P \sim b\rho^{5/3} \sim b\frac{M^{5/3}}{r^5}$$

where $b$ stands for all the non-density terms in the degenerate non-relativistic electron gas equation:

$$b = \left(\frac{3}{\pi}\right)^{2/3}\frac{h^2}{20m_e m_p^{5/3}}\left(\frac{Z}{A}\right)^{5/3}$$

Equating the gravitational pressure and the degeneracy pressure gives:

$$r \sim \frac{b}{G}M^{-1/3}$$

The radius of a white dwarf decreases with increasing mass, and is about $7200\text{ km}$ for a $1\,M_\odot$ star. This isn't surprising, since as mass increases, gravitational attraction increases, compressing the star into a smaller volume. This would lead to even higher gravity as the radius drops. However, electron degeneracy pressure is inversely proportional to the fifth power of radius ($P_e \propto r^{-5}$), whereas gravitational pressure is inversely proportional to the fourth power ($P_{\text{gr}} \propto r^{-4}$). This means as radius drops, the electron degeneracy pressure rises faster and more than makes up for the rise in gravitational pressure.

However, we don't see main-sequence stars or even giants shrinking with an increase in stellar mass. In fact, it's the opposite. This is because in regular stars, as mass increases, gravitational potential energy increases. However, in regular stars, gravitational pressure is balanced by the regular thermal kinetic pressure of the gas ($P_g \propto \rho T$), and the core temperature is locked to a roughly constant ignition value by nuclear fusion. Because thermal pressure can increase via temperature and nuclear energy generation, a more massive main-sequence star does not need to compress to higher densities to support its weight; instead, keeping the core temperature fixed ($T \sim \frac{M}{r} \approx \text{const.}$) requires the radius to expand proportionally with mass ($r \sim M$).

As the white dwarf's mass increases, its radius reduces, which means by the Uncertainty Principle, the uncertainty in momentum rises. At some point, as the velocity gets close to $c$, it enters the ultra-relativistic regime. In the ultra-relativistic limit, we can replace $v$ with $c$. The electron degeneracy pressure integral is then replaced with:

$$P_e = \frac{1}{3}\int_0^{p_F} \frac{8\pi}{h^3}p^2 pc\,dp = \frac{8\pi c}{3h^3}\frac{p_F^4}{4}$$

Again using the relations $p_F = \left(\frac{3h^3}{8\pi}n_e\right)^{1/3}$ and $n_e = \frac{Z\rho}{Am_p}$, we obtain the equation of state for an ultra-relativistic degenerate spin-$1/2$ fermion gas:

$$P_e = \left(\frac{3}{8\pi}\right)^{1/3}\frac{hc}{4m_p^{4/3}}\left(\frac{Z}{A}\right)^{4/3}\rho^{4/3} = \left(\frac{3}{\pi}\right)^{1/3}\frac{hc}{8m_p^{4/3}}\left(\frac{Z}{A}\right)^{4/3}\rho^{4/3}$$

Compared to the non-relativistic case, note the $4/3$ power, and also the fact that the electron mass $m_e$ does not appear—i.e., this equation holds for any ultra-relativistic degenerate ideal gas of spin-$1/2$ particles. This comes about because, for ultra-relativistic particles, the rest mass is a negligible fraction of the total energy, $E = (m_e^2 c^4 + p^2 c^2)^{1/2}$, and hence $p \approx E/c$. As we go from small to large white-dwarf masses, there will be a gradual transition from the non-relativistic to the ultra-relativistic equation of state, with the power-law index of $\rho$ gradually decreasing from $5/3$ to $4/3$. 

Fundamentally, once we hit the relativistic limit, as density rises, we don't get an additional fillip in the degeneracy pressure due to an increase in the velocity of the particles (since $v$ is capped at $c$). However, the momentum continues to rise due to the Uncertainity Principle and Pauli exclusion principle ($p_F = \hbar(3\pi^2 n_e)^{1/3} \propto \rho^{1/3}$. This does not contradict a "fixed" velocity becaise $p=\gamma m v$ and $\gamma$ handles the scaling though velocity is more or less fixed), the collision frequency per particle stops growing with momentum, so the increase in pressure is now sustained only by the increase in particle density and momentum ($P_e \propto n_e p_F c \propto \rho^{4/3}$ rather than $P_e \propto n_e p_F v_F \propto \rho^{5/3}$). Thus, for non-relativistic, we have $P_e \sim \rho^1 \cdot \rho^{1/3} \cdot \rho^{1/3} = \rho^{5/3}$ while for ultra-relativistic we have $P_e \sim \rho^1 \cdot \rho^{1/3} \cdot c = \rho^{4/3}$.

This necessarily means that, as we go to higher masses, and the density increases due to the shrinking radius, the pressure support will rise more and more slowly, so that the radius shrinks even more sharply with increasing mass.

At some mass, the electron pressure becomes incapable of supporting the star against gravity, and the radius shrinks to zero (and the density rises to infinity), unless some other source of pressure sets in. We will see that, at high enough density, the degeneracy pressure due to protons and neutrons begins to operate, and it can sometimes stop the full gravitational collapse, producing objects called neutron stars.

This mass limit is called the Chandrasekhar mass. The mass limit is on one level dependent on:

$$\alpha_G \equiv \frac{\frac{Gm_p^2}{\hbar / (m_p c)}}{m_p c^2} = \frac{Gm_p^2}{\hbar c}$$

The expression $\frac{Gm_p^2}{\hbar / (m_p c)}$ can be considered as the proton’s gravitational self-energy, where the characteristic radius of the proton is taken as its reduced Compton (or relativistic de Broglie) wavelength, $\lambda \sim \frac{\hbar}{m_p c}$. We then take the ratio of this with the proton’s rest energy $m_p c^2$. The dimensionless constant $\alpha_G$ expresses the strength of the gravitational interaction, and is the gravitational analog of the electromagnetic fine-structure constant ($\alpha = \frac{e^2}{\hbar c} \approx \frac{1}{137}$). The maximum mass of a star supported by electron degeneracy pressure is, to an order of magnitude, the mass of $\alpha_G^{-3/2}$ protons (i.e., $\sim 10^{57}$ protons):

$$M_{\text{Ch}} \sim \alpha_G^{-3/2} m_p = \left(\frac{\hbar c}{Gm_p^2}\right)^{3/2} m_p$$

We can arrive at this limit in the following way as well. Look at what happens when you plug this ultra-relativistic equation of state $P_e \sim K_{\text{UR}}\rho^{4/3}$ into the hydrostatic equilibrium scaling $P_{\text{gr}} \sim \frac{GM^2}{r^4}$:

$$P_e \sim K_{\text{UR}}\left(\frac{M}{r^3}\right)^{4/3} = K_{\text{UR}}\frac{M^{4/3}}{r^4}$$

Equating $P_e = P_{\text{gr}}$ gives:

$$K_{\text{UR}}\frac{M^{4/3}}{r^4} \sim \frac{GM^2}{r^4}$$

The radius $r^{-4}$ cancels out completely on both sides. Unlike the non-relativistic regime ($P_e \propto r^{-5}$), where shrinking the star always allowed degeneracy pressure to outrun gravity ($P_{\text{gr}} \propto r^{-4}$), once the electrons hit the speed of light $c$, degeneracy pressure and gravity scale with the exact same inverse fourth power of radius ($r^{-4}$). Shrinking the star further no longer provides any extra pressure advantage over gravity! Solving for $M$ yields a single maximum critical mass—the Chandrasekhar Limit:

$$M_{\text{Ch}} \sim \left(\frac{K_{\text{UR}}}{G}\right)^{3/2} \sim \left(\frac{hc}{Gm_p^{4/3}}\right)^{3/2}\left(\frac{Z}{A}\right)^2 = \left(\frac{hc}{G}\right)^{3/2}\frac{1}{m_p^2}\left(\frac{Z}{A}\right)^2 \approx 1.44\,M_\odot$$

---
**Aside:** This also ties back to our earlier Virial Theorem derivation for an arbitrary adiabatic index $\gamma$:

$$E_{\text{tot}} = \frac{3\gamma - 4}{3(\gamma - 1)}E_{\text{gr}}$$

In the non-relativistic white dwarf regime ($\gamma = 5/3$), $E_{\text{tot}} = \frac{1}{2}E_{\text{gr}} < 0$, so the white dwarf is stably bound at a well-defined equilibrium radius. As the mass increases and the electrons become ultra-relativistic, the adiabatic index softens to $\gamma = 4/3$, driving $3\gamma - 4 \to 0$ and $E_{\text{tot}} \to 0$. At $\gamma = 4/3$, the star has zero net binding energy barrier against collapse: if $M > M_{\text{Ch}}$, gravity permanently overwhelms degeneracy pressure at all radii, and the star collapses catastrophically (either igniting a Type Ia supernova or collapsing into a Neutron Star).

---

#### White Dwarf Cooling

Due to the good thermal conduction of the degenerate electrons in a white dwarf
(similar to the conduction in metals, which arises in the same way), the temperature
inside a white dwarf is approximately constant with radius. 

To understand why a white dwarf is a good conductor, recall that this is mostly due to the electrons at the top of the Fermi sea. Deep in the Fermi sea, there are no nearby higher empty states that an electron can jump to after picking up some thermal energy state. However, at the very top of the Fermi sea, this becomes feasible. Because temperature $T > 0$ slightly blurs the sharp step of the Fermi-Dirac distribution $\langle n_{\text{FD}}\rangle = \frac{1}{e^{(E - E_F)/k_B T} + 1}$ over a narrow thermal skin of width $\Delta E \sim k_B T$ right around $E_F$, a tiny fraction of electrons ($\sim \frac{k_B T}{E_F} \approx 0.005$) just below $E_F$ were thermally excited into states just above $E_F$.

When particles transport thermal energy down a temperature gradient $\frac{dT}{dr}$, the conductive heat flux is: $F_{\text{cond}} = -\kappa_{\text{cond}}\frac{dT}{dr}$, where the thermal conductivity $\kappa_{\text{cond}}$ is the product of three factors: $\kappa_{\text{cond}} = \frac{1}{3}\,c_V\,v\,\ell$.

$c_V$ or heat capacity per unit volume is how much thermal energy the active particles can pick up and drop off per degree of temperature difference. Deep in the Fermi sea, this is 0, but at the top of the Fermi sea, this becomes positive. 
    
$v$ is carrier speed or how fast those particles carry that thermal energy from the hotter layer to the cooler layer. Due to the extraordinarily high energy of the electrons at the top of the Fermi sea, their velocity is very high, which means conduction is good

$\ell$ is mean free path. For electrons deep in the Fermi sea, this is a huge value because they cannot participate in scattering due to there being no available nearby energy slots. However, they do not participate in the thermal conduction processso we can ignore them. Looking at the top of the Fermi sea, we see that mean free path is high for these electrons as well because they have a high velocity, which means Rutherford or electrostatic coulomb scattering between an electron and a nucleus is very minimal. Essentially, the electrons are so fast they are barely deflected by ions and protons, and so their mean free path is high.

Now getting back to white dwarf cooling, the thermal energy reservoir being radiated away during white dwarf cooling is purely the kinetic thermal energy of the non-degenerate ions. However, to estimate the peak temperature reached right at the onset of electron degeneracy, let us assume a pure helium composition; then the number of nuclei in the core is $\frac{M}{4m_p}$, and the number of electrons is $\frac{M}{2m_p}$. Prior to complete electron degeneracy, the total thermal energy (which, once degeneracy sets in, will no longer play a role in supporting the star against gravity) is therefore:

$$E_{\text{th}} = \frac{3}{2}Nk_B T = \frac{3}{2}\frac{M}{m_p}\left(\frac{1}{2} + \frac{1}{4}\right)k_B T = \frac{9}{8}\frac{M}{m_p}k_B T$$

Equating this to $-\frac{1}{2}E_{\text{gr}} \sim \frac{1}{2}\frac{GM^2}{r}$ via the Virial Theorem gives:

$$k_B T \sim \frac{4}{9}\frac{GMm_p}{r}$$

Substituting the equilibrium radius $r_{\text{wd}} \sim \frac{b}{G}M^{-1/3}$ of white dwarfs:

$$k_B T \sim \left(\frac{\pi}{3}\right)^{2/3}\frac{80G^2 m_e m_p^{8/3}}{9h^2}\left(\frac{Z}{A}\right)^{-5/3}M^{4/3}$$

Notice that the equation $E_{\text{th}} = \frac{3}{2}\frac{M}{m_p}\left(\frac{1}{2} + \frac{1}{4}\right)k_B T$ includes both the electrons ($\frac{1}{2}$) and the helium nuclei ($\frac{1}{4}$) in the classical particle count $N = N_e + N_{\text{He}}$. This is because we are calculating the maximum temperature reached at the boundary where classical contraction stops and degeneracy begins. Once the white dwarf settles at $r_{\text{wd}}$ and enters the cooling phase, the $\frac{1}{2}$ electron term freezes out due to Pauli exclusion, leaving only the ion term ($\frac{3}{2}\frac{M}{A m_p}k_B T$, which is $\frac{3}{8}\frac{M}{m_p}k_B T$ for Helium or $\frac{1}{8}\frac{M}{m_p}k_B T$ for Carbon-12) as the active thermal reservoir being radiated away.

Now the radiated luminosity will be:

$$L = 4\pi r_{\text{wd}}^2 \sigma T_E^4$$

where $T_E$ is the effective temperature of the white dwarf photosphere. Although electron heat conduction leads to a constant temperature over most of the volume, there is a thin non-degenerate surface layer (of order $1\%$ of the white dwarf radius) that insulates the star. This layer lowers $T_E$  relative to the interior temperature and slows down the rate of energy loss.

However, to obtain a crude upper limit on the rate at which a white dwarf cools by means of its radiative energy loss, let us assume a constant temperature all the way out to the surface of the star, so that $T_E \sim T$. The radiative energy loss rate is then:

$$4\pi r_{\text{wd}}^2 \sigma T^4 \sim -\frac{dE_{\text{th}}}{dt} = -M \cdot \text{const.} \cdot \frac{dT}{dt}$$

Integrating or taking the characteristic ratio gives a cooling timescale of:

$$\tau_{\text{cool}} \sim \frac{E_{\text{th}}}{L} \sim \frac{M}{r_{\text{wd}}^2 T^3} \propto \frac{1}{T^3}$$

### Brown Dwarfs

Consider a newly forming star (or “protostar”) composed of a collapsing cloud of hydrogen. Nuclear ignition of hydrogen requires a minimal temperature of about $T_{\text{ign}} \approx 10^7\text{ K}$. However, the contraction of the core will halt at the radius where degeneracy pressure sets in. Thus, there is a limit to how high the core temperature can go for a given mass:

$$k_B T \sim \left(\frac{\pi}{3}\right)^{2/3}\frac{10G^2 m_e m_p^{8/3}}{3h^2}\left(\frac{Z}{A}\right)^{-5/3} M^{4/3}$$

If the mass of the protostar is small enough such that contraction halts before $T_{\text{ign}}$ is attained, the object will never achieve true stardom on the main sequence. The limiting mass is $\approx 0.07\text{–}0.08\,M_\odot$. Such failed stars are called brown dwarfs.

By the way, look at the numerical prefactor in our equations for brown dwarf and white dwarf $k_B T_{\text{max}}$. For brown dwarfs, $\frac{1}{\mu} = 1 + 1 = 2$ particles per $m_p$.

$$E_{\text{th}} = \frac{3}{2}(2)\frac{M}{m_p}k_B T = 3\frac{M}{m_p}k_B T \implies k_B T \sim \frac{1}{6}\frac{GMm_p}{r}$$
    
Dividing $\frac{1}{6}$ by the $\frac{1}{20}$ inside $b$ gives $\frac{20}{6} = \frac{10}{3}$, which is the exact $\frac{10}{3}$ coefficient in your Brown Dwarf equation!
    
For white dwarfs with a helium core ($\frac{1}{\mu} = \frac{1}{2} + \frac{1}{4} = \frac{3}{4}$ particles per $m_p$)

$$E_{\text{th}} = \frac{3}{2}\left(\frac{3}{4}\right)\frac{M}{m_p}k_B T = \frac{9}{8}\frac{M}{m_p}k_B T \implies k_B T \sim \frac{4}{9}\frac{GMm_p}{r}$$

Dividing $\frac{4}{9}$ by the $\frac{1}{20}$ inside $b$ gives $4 \times \frac{20}{9} = \frac{80}{9}$, which is the exact $\frac{80}{9}$ coefficient in the white dwarf equation. Why did we calculate the temperature for a pure helium core? Because it tells us which stars can ignite the triple-alpha reaction ($3\,{}^4\text{He} \to {}^{12}\text{C}$ at $T_{\text{He, ign}} \approx 10^8\text{ K}$) and which stars get stuck as Helium White Dwarfs. 

Plugging $T_{\text{He, ign}} \approx 10^8\text{ K}$ and $\frac{Z}{A} = \frac{1}{2}$ into your $\frac{80}{9}$ formula shows that a contracting helium core can only reach $10^8\text{ K}$ before electron degeneracy halts its contraction if the core mass exceeds $M_{\text{He}} \gtrsim 0.45\,M_\odot$. Stars with initial mass below $\sim 0.5\,M_\odot$ never reach this threshold; once they exhaust their core hydrogen, their helium cores become degenerate before ever reaching $10^8\text{ K}$, ending their lives directly as Helium White Dwarfs rather than Carbon-Oxygen White Dwarfs.

Note that because brown dwarfs are supported by non-relativistic electron degeneracy pressure, their radii obey the white-dwarf scaling $r \propto M^{-1/3}$ across the mass range from $\sim 5\,M_{\text{Jupiter}}$ to $75\,M_{\text{Jupiter}}$ (competing slightly with electrostatic Coulomb pressure at the low-mass planet end, where $r \propto M^{+1/3}$). The peak of this curve sits near $3\text{–}5\,M_{\text{Jupiter}}$, which means that every gas giant and brown dwarf from $1\,M_{\text{Jupiter}}$ all the way up to $80\,M_{\text{Jupiter}}$ has virtually the exact same radius ($R \approx 1\,R_{\text{Jupiter}} \approx 70,000\text{ km}$, or about $0.1\,R_\odot$), regardless of whether it is $10$ or $70$ times as massive as Jupiter.

While brown dwarfs ($M \lesssim 0.075\,M_\odot$, or $\lesssim 75\text{–}80\,M_{\text{Jupiter}}$) never reach the $\sim 10^7\text{ K}$ core temperature required for sustained proton-proton ($^1\text{H}$) fusion, the more Massive brown dwarfs _do_ briefly fuse trace light isotopes with lower Coulomb barriers:

**Deuterium Fusion ($^2\text{H} + p \to {}^3\text{He} + \gamma$):** Ignites at $T_c \approx 10^6\text{ K}$, which occurs in objects above $M \approx 13\,M_{\text{Jupiter}}$ ($\approx 0.012\,M_\odot$). The International Astronomical Union (IAU) uses this $13\,M_{\text{Jupiter}}$ deuterium-burning threshold as the working boundary between giant planets and brown dwarfs.
    
**Lithium Fusion ($^7\text{Li} + p \to 2\,{}^4\text{He}$):** Ignites at $T_c \approx 2.5 \times 10^6\text{ K}$, which requires $M \gtrsim 60\text{–}65\,M_{\text{Jupiter}}$. Because brown dwarfs are fully convective throughout their interiors, any brown dwarf above $65\,M_{\text{Jupiter}}$ rapidly mixes and destroys all its primordial lithium, whereas lower-mass brown dwarfs retain a strong $\text{Li I}$ absorption line at $6708 \mathring{A} $. Observers use this Lithium Test to distinguish true substellar brown dwarfs from dim low-mass $\text{M}$-dwarf stars.

### Neutron Stars

Let us consider stars with initial masses (i.e., their masses when they begin their lives on the main sequence) of about $8\,M_\odot$  or more. This corresponds to spectral types O and “early” B. After exhausting most of the hydrogen in their cores, such stars move to the giant branch. They then begin a sequence of steps, each consisting of the contraction and heating of the inner regions, resulting in the ignition of new nuclear reactions. As time advances, shells at various inner radii attain the temperatures and the densities required for the reactions that produce progressively heavier elements.

Carbon burning is followed by neon, oxygen, and silicon burning. Each of these stages takes less and less time. For example, for a $25\,M_\odot$ star, the duration of each burning stage is:

-   $\text{H} \sim 5 \times 10^6\text{ yr}$
    
-   $\text{He} \sim 5 \times 10^5\text{ yr}$
    
-   $\text{C} \sim 500\text{ yr}$
    
-   $\text{Ne} \sim 1\text{ yr}$
    
-   $\text{Si} \sim 1\text{ day}$    

Massive stars undergo all the stages of nuclear burning up to the production of elements in the “iron group” with atomic mass number around $A = 56$, consisting of isotopes of $\text{Cr}$,  $\text{Mn}$,  $\text{Fe}$,  $\text{Co}$, and $\text{Ni}$. At this stage, the star’s outer envelope has expanded to about $1000\,R_\odot$, and it has a dense core of radius $\sim 10^4\text{ km}$ with an onion-like layered structure. The outer layers of this core are still burning hydrogen. Looking inwards, the core consists of concentric shells composed primarily of helium, carbon, neon, oxygen, silicon, and iron, respectively.

Energy can be gained by fusing or fissioning elements with low binding energy per nucleon into elements with high binding energy per nucleon. The iron group elements are the most tightly bound nuclei, and are therefore a “dead end” in nuclear energy production. Synthesis of iron-group elements into heavier elements consumes, rather than releases, thermal energy. This fact is at the root of the “iron catastrophe” that ensues. When the central iron core continues to grow and approaches $M_{\text{Ch}}$, two processes begin.

**Nuclear Photodisintegration:** The temperature is high enough for energetic photons to be abundant, and they get absorbed in the endothermic (i.e., energy-consuming) nuclear reaction:

$$\gamma + {}^{56}\text{Fe} \to 13\,{}^4\text{He} + 4n$$

with an energy consumption of $124\text{ MeV}$. The helium nuclei are further unbound in the process:

$$\gamma + {}^4\text{He} \to 2p + 2n$$

consuming $28.3\text{ MeV}$.

**Neutronization:** The large densities in the core lead to a large increase in the rates of processes such as:

$$e^- + p \to n + \nu_e$$

$$e^- + {}^{56}\text{Fe} \to {}^{56}\text{Mn} + \nu_e$$

$$e^- + {}^{56}\text{Mn} \to {}^{56}\text{Cr} + \nu_e$$

This neutronization depletes the core of electrons and their supporting degeneracy pressure, as well as of energy, which is carried off by the neutrinos.

The two processes lead, in principle, to an almost total loss of thermal and degeneracy pressure support and to an unrestrained collapse of the core of a star on a free-fall timescale. For the typical core densities prior to collapse,  $\rho \sim 10^9\text{ g cm}^{-3}$ (calculated from stellar evolution models), this timescale is a few tenths of a second to a few seconds.

As the collapse proceeds and the density and the temperature increase, the reaction:

$$e^- + p \to n + \nu_e$$

becomes common, and is infrequently offset by the inverse process of neutron decay:

$$n \to p + e^- + \bar{\nu}_e$$

leading to an equilibrium ratio of number densities of:

$$n_e = n_p \approx \frac{1}{200}n_n$$

Thus, most of the nucleons become neutrons, and a neutron star forms, in which degenerate neutrons, rather than electrons, provide the pressure support against gravity.

Because neutrons are spin-$1/2$ fermions just like electrons, a non-relativistic neutron star obeys the exact same equation of state as for white dwarfs, except with the electron mass $m_e$ replaced by the neutron mass $m_n \approx m_p \approx 1836\,m_e$, and with $Z/A \to 1$ (since every nucleon is now a fermion contributing to degeneracy pressure, rather than $1$ electron per $2$ nucleons):

$$P_n = \left(\frac{3}{\pi}\right)^{2/3}\frac{h^2}{20m_n m_p^{5/3}}\rho^{5/3} \approx \left(\frac{3}{\pi}\right)^{2/3}\frac{h^2}{20m_n^{8/3}}\rho^{5/3}$$

We saw white dwarf radius scaled as $r \sim \frac{b}{G}M^{-1/3} \propto \frac{1}{m_{\text{fermion}}}\left(\frac{Z}{A}\right)^{5/3}M^{-1/3}$, replacing $m_e \to m_n \approx 1836\,m_e$ and $Z/A = 1/2 \to 1$ shrinks the radius by a factor of:

$$\frac{R_{\text{WD}}}{R_{\text{NS}}} \sim \frac{m_n}{m_e}\left(\frac{1/2}{1}\right)^{5/3} \approx \frac{1836}{2^{5/3}} \approx 580$$

Dividing the $7200\text{ km}$ white dwarf radius by $580$ predicts a neutron star radius of $R_{\text{NS}} \approx 12\text{ km}$. And because surface area is $4\pi R^2$, a radius smaller by a factor of $\sim 500$ means a surface area smaller by $500^2 \approx 2.5 \times 10^5$

Neutron stars are mostly known when we detect them as pulsars. Pulsars produce their observed periodic emission because of the rotation of a neutron star having a magnetic field axis that is misaligned with respect to the star’s rotation axis by some angle $\theta$. A spinning magnetic dipole radiates an electromagnetic luminosity:

$$L = \frac{1}{6c^3} B^2 r^6 \omega^4 \sin^2\theta$$

where $B$ is the magnetic field on the surface of the star, at a radius $r$, on the magnetic pole. The emission of radiation takes place in two conical beams in the direction of the magnetic axis. As the star spins and the magnetic axis precesses around the rotation axis, each beam traces an annulus of angular radius $\theta$ on the sky, as seen from the neutron star. Distant observers who happen to lie on the path of these “lighthouse beams” detect a pulse once every rotation, when the beam sweeps past them.

This luminosity or emission is responsible for the loss of rotational energy of the pulsar ($E_{\text{rot}} = \frac{1}{2}I\omega^2$):

$$\frac{dE_{\text{rot}}}{dt} = I\omega\frac{d\omega}{dt} \propto -\omega^4$$

$$\frac{d\omega}{dt} = -C\omega^3$$

The constant $C$ can be determined from the present values of $\dot{\omega}_0 \equiv (d\omega/dt)_0$ and $\omega_0$:

$$C = -\frac{\dot{\omega}_0}{\omega_0^3}$$

Separating variables and integrating, we obtain for the age of the pulsar:

$$t_{\text{pulsar}} = -\frac{\omega_0^3}{2\dot{\omega}_0}\left(\frac{1}{\omega^2} - \frac{1}{\omega_i^2}\right)$$

where $\omega_i$ is the initial angular frequency of the neutron star upon formation. Thus, an upper limit on the current age of the Crab pulsar is obtained by taking $\omega = \omega_0$ and $\omega_i = \infty$:

$$t_{\text{pulsar}} < \frac{\omega_0}{2\vert{}\dot{\omega}_0\vert{}} = \frac{190\text{ s}^{-1}}{2 \times 2.4 \times 10^{-9}\text{ s}^{-2}} = 4 \times 10^{10}\text{ s} \approx 1260\text{ yr}$$

This limit is consistent with the historical age, $\approx 950\text{ yr}$, of the supernova of the year 1054. The pulsar age will equal $950\text{ yr}$ if we set the initial spin period $\tau_i = 2\pi/\omega_i = 2.5\text{ ms}$, close to the expected spin rate of newly formed neutron stars.

Thus, pulsars slow down and lose their rotational energies, and as a result, at some point in time, will become undetectable as pulsars. However, there should exist a large population of old, spun-down neutron stars—the remnants of all massive stars that have undergone core-collapse to this state. We know that white dwarfs have a small surface area and, as a result, very long cooling times. The surface areas of neutron stars, smaller by five orders of magnitude compared to those of white dwarfs, mean that old neutron stars will be “stuck” at temperatures of order $10^5\text{ K}$, with thermal radiation peaking at photon energies of tens of $\text{eV}$ (called the “extreme UV” range).

Detailed calculations of neutron star cooling are considerably more uncertain than those for white dwarfs, partly due to the poorly constrained equation of state of nuclear matter, which leads to uncertainty in the structure and composition of a neutron star. A cooling calculation also needs to take into account many different physical processes, not all fully understood, that may play a role under the extreme conditions of gravity, temperature, density, and magnetic field inside and near the surface of a neutron star.

Interstellar gas atoms falling onto a neutron-star surface also have an effect, and are likely to heat it to X-ray temperatures. To date, only several candidate isolated old neutron stars have been found in X-ray surveys. The small surface areas of neutron stars mean that their optical luminosities are very low, and hence such objects can be found only when they are near enough. X-ray surveys do reveal a large population of accreting neutron stars in binary systems, called “X-ray binaries”.

## References
- Astrophysics in a nutshell by Dan Maoz
- [Stellar Structure and Evolution Lecture Notes](https://www.astro.ru.nl/~onnop/education/stev_utrecht_notes/) by Onno Pols, Radboud University
