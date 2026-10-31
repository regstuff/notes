# Figures for "The Cosmic Microwave Background" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_cosmic_microwave_background_figures.py docs/astrophysics/figures scripts/cosmology/data
# The data directory must contain the Planck 2018 (PR3) power spectra from the Planck Legacy Archive / IRSA:
#   COM_PowerSpect_CMB-TT-full_R3.01.txt, COM_PowerSpect_CMB-TT-binned_R3.01.txt,
#   COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt
#   from https://irsa.ipac.caltech.edu/data/Planck/release_3/ancillary-data/cosmoparams/
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import brentq

OUT, DATA = sys.argv[1], sys.argv[2]
SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
    "text.color": INK, "font.size": 11, "axes.titlesize": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "lines.linewidth": 2, "legend.frameon": False, "mathtext.fontset": "cm",
})
def save(fig, name):
    fig.tight_layout(); fig.savefig(f"{OUT}/cosmic_microwave_background_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- cosmology and recombination numbers (Planck 2018 values) ----------
H0 = 67.4e3/3.0856776e22; Om, Or, Ob = 0.315, 9.21e-5, 0.0493; OL = 1 - Om - Or
tH = 1/H0/3.15576e7            # years
E = lambda z: np.sqrt(Or*(1+z)**4 + Om*(1+z)**3 + OL)
age = lambda z: quad(lambda x: 1/((1+x)*E(x)), z, np.inf, limit=300)[0]*tH
k_eV, me_c2, Q, eta, T0 = 8.617333e-5, 510998.95, 13.6057, 6.12e-10, 2.7255
def X_saha(z):
    # Saha: (1 - X)/X^2 = S. Written as 2/(1 + sqrt(1 + 4S)) so that S -> infinity gives X -> 0 instead of inf/inf.
    kT = k_eV*T0*(1+z)
    with np.errstate(over="ignore"):
        S = 3.84*eta*(kT/me_c2)**1.5*np.exp(Q/kT)
    return 2/(1 + np.sqrt(1 + 4*S))
nb0 = 0.251; sigT, c = 6.6524587e-29, 2.99792458e8
Gamma = lambda z, X: X*nb0*sigT*c*(1+z)**3
Hz = lambda z: H0*E(z)
z_rec = brentq(lambda z: X_saha(z) - 0.5, 1000, 2000)
z90, z10 = brentq(lambda z: X_saha(z) - 0.9, 1000, 2000), brentq(lambda z: X_saha(z) - 0.1, 900, 2000)
z_dec = brentq(lambda z: Gamma(z, X_saha(z)) - Hz(z), 900, 1500)
z_dec_ion = brentq(lambda z: Gamma(z, 1.0) - Hz(z), 5, 200)
print("Saha: z_rec=%.0f T_rec=%.0f K kT=%.3f eV (Q/%.1f) t_rec=%.0f yr" % (z_rec, T0*(1+z_rec), k_eV*T0*(1+z_rec), Q/(k_eV*T0*(1+z_rec)), age(z_rec)))
print("X: 0.9 at z=%.0f, 0.1 at z=%.0f, dt=%.0f yr" % (z90, z10, age(z10) - age(z90)))
print("Saha decoupling z=%.0f; if always ionized z=%.1f T=%.0f K" % (z_dec, z_dec_ion, T0*(1+z_dec_ion)))
print("age at z=1089.9: %.0f yr; at z=3400: %.0f yr" % (age(1089.9), age(3400)))
DM = quad(lambda x: 1/E(x), 0, 1089.9, limit=400)[0]*c/H0/3.0856776e22
dhor_com = quad(lambda x: 1/E(x), 1089.9, np.inf, limit=400)[0]*c/H0/3.0856776e22
print("comoving distance to z*: %.0f Mpc; d_A = %.2f Mpc; comoving horizon at z*: %.0f Mpc; proper %.3f Mpc; theta_hor=%.2f deg" %
      (DM, DM/1090.9, dhor_com, dhor_com/1090.9, np.degrees(dhor_com/DM)))
print("theta_s from r*=144.43: %.3f deg, l ~ pi/theta = %.0f" % (np.degrees(144.43/DM), np.pi/(144.43/DM)))

# ---------- the Planck temperature power spectrum ----------
lo = np.loadtxt(f"{DATA}/COM_PowerSpect_CMB-TT-full_R3.01.txt", comments="#")
bi = np.loadtxt(f"{DATA}/COM_PowerSpect_CMB-TT-binned_R3.01.txt", comments="#")
th = np.loadtxt(f"{DATA}/COM_PowerSpect_CMB-base-plikHM-TTTEEE-lowl-lowE-lensing-minimum-theory_R3.01.txt", comments="#")
low = lo[lo[:, 0] < 30]
fig, ax = plt.subplots(figsize=(9.5, 5.0))
ax.plot(th[:, 0], th[:, 1], color=C1, lw=1.8, label=r"best-fitting $\Lambda$CDM model", zorder=2)
ax.errorbar(low[:, 0], low[:, 1], yerr=[low[:, 2], low[:, 3]], fmt="o", ms=3.5, color=C2, elinewidth=0.9, capsize=0, label="Planck 2018 data", zorder=3)
ax.errorbar(bi[:, 0], bi[:, 1], yerr=[bi[:, 2], bi[:, 3]], fmt="o", ms=3.5, color=C2, elinewidth=0.9, capsize=0, zorder=3)
ax.set_xscale("log"); ax.set_xlim(1.7, 2600); ax.set_ylim(0, 6500)
ax.set_xlabel(r"multipole $\ell$"); ax.set_ylabel(r"$\mathcal{D}_\ell = \ell(\ell+1)C_\ell T_0^2/2\pi$ ($\mu$K$^2$)")
for l, lab in [(220, "1st peak"), (537, "2nd"), (811, "3rd")]:
    ax.annotate(lab, xy=(l, th[int(l)-2, 1]), xytext=(l*0.8, th[int(l)-2, 1] + 650), fontsize=9.5, arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.text(2.3, 3000, "Sachs–Wolfe plateau:\nlarger than the horizon\nat last scattering", fontsize=9.5)
ax.text(1150, 2300, "damping tail", fontsize=9.5)
sec = ax.secondary_xaxis("top", functions=(lambda l: 180/np.clip(l, 1e-3, None), lambda t: 180/np.clip(t, 1e-3, None)))
sec.set_xlabel(r"angular scale $\approx 180^\circ/\ell$")
sec.set_xticks([90, 10, 1, 0.2]); sec.set_xticklabels([r"$90^\circ$", r"$10^\circ$", r"$1^\circ$", r"$0.2^\circ$"])
ax.legend(loc="upper left", fontsize=9.5)
ax.set_title("The temperature power spectrum of the CMB", loc="left", pad=28)
save(fig, "power_spectrum")

# ---------- recombination and decoupling ----------
zz = np.linspace(600, 2000, 600)
fig, axs = plt.subplots(1, 2, figsize=(11, 4.4))
ax = axs[0]
for e_, col, ls, lab in [(eta, C1, "-", r"$\eta = 6.1\times10^{-10}$"), (eta*10, C2, "--", r"$\eta$ ten times larger"), (eta/10, C3, "-.", r"$\eta$ ten times smaller")]:
    def Xs(z, e_=e_):
        kT = k_eV*T0*(1+z)
        with np.errstate(over="ignore"):
            S = 3.84*e_*(kT/me_c2)**1.5*np.exp(Q/kT)
        return 2/(1 + np.sqrt(1 + 4*S))
    ax.plot(zz, [Xs(z) for z in zz], color=col, ls=ls, label=lab)
ax.axhline(0.5, color=INK2, lw=0.8, ls=":")
ax.invert_xaxis(); ax.set_xlabel("redshift $z$"); ax.set_ylabel("fractional ionization $X$")
ax.set_title("(a) recombination (Saha equation)", loc="left", pad=34); ax.legend(loc="lower left", fontsize=9.5)
tw = ax.secondary_xaxis("top", functions=(lambda z: T0*(1+z), lambda T: T/T0 - 1)); tw.set_xlabel("temperature (K)")
ax = axs[1]
zz2 = np.logspace(np.log10(10), np.log10(3000), 400)
ax.loglog(zz2, Hz(zz2), color=INK, lw=2, label="expansion rate $H$")
ax.loglog(zz2, Gamma(zz2, 1.0), color=C2, ls="--", label=r"scattering rate $\Gamma$, if fully ionized")
ax.loglog(zz2, Gamma(zz2, np.array([X_saha(z) for z in zz2])), color=C1, label=r"$\Gamma$ with Saha ionization")
ax.plot([z_dec], [Hz(z_dec)], "o", color=C1, ms=7, mec=SURF, mew=1.5)
ax.annotate(f"decoupling, $z \\approx {z_dec:.0f}$", xy=(z_dec, Hz(z_dec)), xytext=(60, 3e-11), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.invert_xaxis(); ax.set_ylim(1e-17, 1e-8)
ax.set_xlabel("redshift $z$"); ax.set_ylabel("rate (s$^{-1}$)")
ax.set_title("(b) when photons stop scattering", loc="left"); ax.legend(loc="upper right", fontsize=9)
save(fig, "recombination")

# ---------- toy acoustic oscillations ----------
fig, axs = plt.subplots(1, 2, figsize=(11, 4.2))
ax = axs[0]
x = np.linspace(0, 1, 400)            # time in units of decoupling (sound-horizon phase k r_s)
for n, col, ls, lab in [(1, C1, "-", "1st peak: maximally compressed at decoupling"), (2, C2, "--", "2nd peak: compressed, then back to maximum rarefaction"), (1.5, C3, "-.", "trough: caught passing through zero")]:
    ax.plot(x, -np.cos(n*np.pi*x), color=col, ls=ls, label=lab)
ax.axvline(1, color=INK2, lw=1, ls=":"); ax.text(0.98, 1.2, "decoupling", ha="right", fontsize=9.5, color=INK2)
ax.axhline(0, color=GRID, lw=1)
ax.set_xlabel("time (in units of the decoupling time)"); ax.set_ylabel("effective temperature in a well (toy)")
ax.text(0.03, -1.32, "all start cold (climbing out of the well)", fontsize=9, color=INK2)
ax.set_ylim(-1.45, 1.9); ax.set_title("(a) standing sound waves of different wavelengths", loc="left"); ax.legend(loc="upper left", fontsize=9)
ax = axs[1]
kk = np.linspace(0.02, 4.2, 600)
ax.plot(kk, np.cos(np.pi*kk)**2, color=C1)
for n in (1, 2, 3, 4):
    ax.annotate("compression" if n % 2 else "rarefaction", xy=(n, 1), xytext=(n, 1.08), ha="center", fontsize=9, color=INK2)
ax.set_xlabel(r"wavenumber $k$ in units of $\pi/r_*$"); ax.set_ylabel("power at decoupling (toy)")
ax.set_ylim(0, 1.25); ax.set_title("(b) the snapshot: peaks at $k\\,r_* = n\\pi$", loc="left")
save(fig, "acoustic_toy")
