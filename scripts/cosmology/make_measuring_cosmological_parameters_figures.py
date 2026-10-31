# Figures for the "Measuring Cosmological Parameters" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_measuring_cosmological_parameters_figures.py docs/astrophysics/figures scripts/cosmology/data/Pantheon+SH0ES.dat
# (download Pantheon+SH0ES.dat into scripts/cosmology/data/ first; it is about 1 MB:
#  curl -L -o scripts/cosmology/data/Pantheon+SH0ES.dat "https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat")
# The supernova file is the public Pantheon+ distance table:
# https://github.com/PantheonPlusSH0ES/DataRelease (Pantheon+_Data/4_DISTANCES_AND_COVAR/Pantheon+SH0ES.dat)
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad

OUT, PANTHEON = sys.argv[1], sys.argv[2]
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
    fig.tight_layout(); fig.savefig(f"{OUT}/measuring_cosmological_parameters_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

C_KMS = 299792.458
def E(z, Om, OL, Or=9.21e-5):
    Ok = 1 - Om - OL - Or
    return np.sqrt(Or*(1+z)**4 + Om*(1+z)**3 + Ok*(1+z)**2 + OL)
def dC(z, Om, OL, Or=9.21e-5):          # comoving distance in units of c/H0
    return quad(lambda x: 1/E(x, Om, OL, Or), 0, z, limit=200)[0]
def SK(x, Om, OL, Or=9.21e-5):
    Ok = 1 - Om - OL - Or
    if abs(Ok) < 1e-8: return x
    return np.sinh(np.sqrt(Ok)*x)/np.sqrt(Ok) if Ok > 0 else np.sin(np.sqrt(-Ok)*x)/np.sqrt(-Ok)
def dL(z, Om, OL, Or=9.21e-5): return (1+z)*SK(dC(z, Om, OL, Or), Om, OL, Or)
LCDM = (0.315, 0.68491)

# ---------- the distance ladder ----------
fig, ax = plt.subplots(figsize=(10, 4.6))
rungs = [  # (label, d_min [pc], d_max [pc], colour, row)
    ("radar ranging", 1e-6, 1e-4, INK2, 0),
    ("parallax (Gaia)", 1, 5e3, C1, 1),
    ("Cepheids, tip of the red giant branch", 1e3, 5e7, C2, 2),
    ("Type Ia supernovae", 1e7, 6.5e9, C3, 3),            # out to z = 2.9 (comoving 6.4 Gpc)
    ("baryon acoustic oscillations, CMB", 1e8, 1.4e10, C4, 4),
]
for lab, a, b, col, row in rungs:
    ax.plot([a, b], [row, row], color=col, lw=8, solid_capstyle="round")
    ax.text(a, row + 0.28, lab, fontsize=10, va="bottom")
marks = [("Sun", 4.85e-6), ("nearest star", 1.3), ("Galactic centre", 8.2e3), ("LMC", 4.96e4), ("M31", 7.6e5),
         ("NGC 4258", 7.6e6), ("Virgo", 1.65e7), ("Hubble flow\nbegins", 1e8), ("$z = 1$", 3.4e9)]
for lab, d in marks:
    ax.axvline(d, color=GRID, lw=1, zorder=0)
    ax.text(d, -0.75, lab, rotation=90, ha="center", va="top", fontsize=9, color=INK2)
ax.set_xscale("log"); ax.set_xlim(1e-6, 3e10); ax.set_ylim(-3.5, 5.1)
ax.set_yticks([]); ax.grid(False); ax.spines["left"].set_visible(False)
ax.set_xlabel("distance (pc)")
ax.set_title("The cosmic distance ladder", loc="left")
save(fig, "distance_ladder")

# ---------- three distances ----------
zz = np.logspace(-2, 3, 300)
dc = np.array([dC(z, *LCDM) for z in zz])
fig, ax = plt.subplots(figsize=(7, 4.8))
ax.loglog(zz, (1+zz)*dc, color=C2, ls="--", label=r"luminosity distance $d_L = (1+z)\,d_p(t_0)$")
ax.loglog(zz, dc, color=C1, ls="-", label=r"proper distance now $d_p(t_0)$")
ax.loglog(zz, dc/(1+zz), color=C3, ls="-.", label=r"angular-diameter distance $d_A = d_p(t_0)/(1+z)$")
ax.loglog(zz, zz, color=INK2, lw=1, ls=":", label=r"Hubble's law, $cz/H_0$")
i = np.argmax(dc/(1+zz)); ax.plot([zz[i]], [dc[i]/(1+zz[i])], "o", color=C3, ms=7, mec=SURF, mew=1.5)
ax.annotate(f"maximum: $z = {zz[i]:.1f}$", xy=(zz[i], dc[i]/(1+zz[i])), xytext=(6, 0.06), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.set_xlim(0.01, 1000); ax.set_ylim(0.005, 3000)
ax.set_xlabel("redshift $z$"); ax.set_ylabel(r"distance ($c/H_0$)")
ax.set_title(r"Three distances in our universe ($\Lambda$CDM)", loc="left"); ax.legend(loc="upper left", fontsize=9.5)
print("d_A max at z=%.2f value %.4f c/H0" % (zz[i], dc[i]/(1+zz[i])))
save(fig, "three_distances")

# ---------- Hubble diagram from Pantheon+ ----------
cols = open(PANTHEON).readline().split()
dat = np.genfromtxt(PANTHEON, names=True, dtype=None, encoding=None)
z = dat["zHD"]; mu = dat["MU_SH0ES"]; err = dat["MU_SH0ES_ERR_DIAG"]; cal = dat["IS_CALIBRATOR"]
sel = (cal == 0) & (z > 0.01)
z, mu, err = z[sel], mu[sel], err[sel]
# fit the H0 offset for flat LCDM (Omega_m fixed) to the Hubble-flow supernovae
def mu_model(z, H0, Om, OL):
    return 5*np.log10(np.array([dL(x, Om, OL) for x in np.atleast_1d(z)])*C_KMS/H0) + 25
m_ref = mu_model(z, 70.0, *LCDM)
w = 1/err**2; off = np.sum(w*(mu - m_ref))/np.sum(w)
H0fit = 70.0*10**(-off/5)
print("Hubble-flow SNe:", sel.sum(), " implied H0 with Om=0.315 flat: %.1f" % H0fit)
fig, axs = plt.subplots(2, 1, figsize=(7.6, 7.2), sharex=True, gridspec_kw={"height_ratios": [1.6, 1]})
ax = axs[0]
ax.errorbar(z, mu, yerr=err, fmt="o", ms=2.2, color=INK2, alpha=0.35, elinewidth=0.5, capsize=0, zorder=1)
zg = np.logspace(-2, np.log10(2.4), 200)
ax.plot(zg, mu_model(zg, H0fit, *LCDM), color=C1, lw=2, label=r"$\Lambda$CDM ($\Omega_m = 0.315$, $\Omega_\Lambda = 0.685$)", zorder=3)
ax.set_xscale("log"); ax.set_ylabel(r"distance modulus $m - M$")
ax.set_title(f"(a) Pantheon+ Type Ia supernovae (Hubble flow, {sel.sum()} light curves)", loc="left"); ax.legend(loc="upper left", fontsize=9.5)
ax = axs[1]
ref = mu_model(zg, H0fit, 0.0, 0.0, )
models = [(LCDM, C1, "-", r"$\Lambda$CDM"), ((1.0, 0.0), C2, "--", "flat, matter only"), ((0.0, 1.0), C3, "-.", r"flat, $\Lambda$ only")]
for (Om, OL), col, ls, lab in models:
    ax.plot(zg, mu_model(zg, H0fit, Om, OL) - ref, color=col, ls=ls, lw=2, label=lab)
ax.axhline(0, color=INK2, lw=1, ls=":"); ax.text(0.03, -0.19, "empty universe (dotted line)", fontsize=9, color=INK2)
bins = np.logspace(np.log10(0.01), np.log10(2.3), 16)
res = mu - np.interp(z, zg, ref)
for lo, hi in zip(bins[:-1], bins[1:]):
    m = (z >= lo) & (z < hi)
    if m.sum() >= 3:
        wm = 1/err[m]**2; r = np.sum(wm*res[m])/np.sum(wm); e = 1/np.sqrt(np.sum(wm))
        ax.errorbar(np.sqrt(lo*hi), r, yerr=e, fmt="o", ms=6, color=INK, mec=SURF, mew=1, elinewidth=1.4, capsize=0, zorder=4)
ax.set_xscale("log"); ax.set_xlim(0.01, 2.5); ax.set_ylim(-0.9, 0.6)
ax.set_xlabel("redshift $z$"); ax.set_ylabel(r"$\Delta(m - M)$ (mag)")
ax.text(0.012, 0.5, "(b) binned, relative to an empty universe", fontsize=10.5, va="top")
ax.legend(loc="lower left", fontsize=9.5, ncol=3)
save(fig, "hubble_diagram")
