# Figures for the "Fundamental Observations" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_fundamental_observations_figures.py docs/astrophysics/figures scripts/cosmology/data/firas_monopole_spec_v1.txt
# The FIRAS file is the COBE/FIRAS monopole spectrum from NASA LAMBDA:
# https://lambda.gsfc.nasa.gov/data/cobe/firas/monopole_spec/firas_monopole_spec_v1.txt
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT, FIRAS = sys.argv[1], sys.argv[2]
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
    fig.tight_layout(); fig.savefig(f"{OUT}/fundamental_observations_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- homogeneity versus isotropy ----------
rng = np.random.default_rng(11)
fig, axs = plt.subplots(1, 3, figsize=(11, 4.0))
# (a) homogeneous but not isotropic: parallel stripes
ax = axs[0]
for y0 in np.arange(-1.0, 1.01, 0.25):
    xs = rng.uniform(-1, 1, 40); ax.scatter(xs, y0 + rng.normal(0, 0.012, 40), s=6, color=C1)
ax.set_title("(a) homogeneous only", loc="left", fontsize=11)
# (b) isotropic about one point but not homogeneous: concentric rings
ax = axs[1]
for r0 in np.arange(0.15, 1.01, 0.2):
    th = rng.uniform(0, 2*np.pi, int(70*r0)); rr = r0 + rng.normal(0, 0.012, th.size)
    ax.scatter(rr*np.cos(th), rr*np.sin(th), s=6, color=C2)
ax.plot([0], [0], "o", ms=7, color=INK, mec=SURF, mew=1.5)
ax.set_title("(b) isotropic about one point only", loc="left", fontsize=11)
# (c) homogeneous and isotropic: uniform random
ax = axs[2]
P = rng.uniform(-1, 1, size=(330, 2)); ax.scatter(P[:, 0], P[:, 1], s=6, color=C3)
ax.set_title("(c) homogeneous and isotropic", loc="left", fontsize=11)
for ax in axs:
    ax.set_xlim(-1.05, 1.05); ax.set_ylim(-1.05, 1.05); ax.set_aspect("equal"); ax.grid(False)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(True); s.set_color(GRID)
save(fig, "homogeneity_isotropy")

# ---------- the CMB spectrum measured by COBE/FIRAS ----------
d = np.loadtxt(FIRAS, comments="#")
nu_cm, I_MJy, resid_kJy, sig_kJy = d[:, 0], d[:, 1], d[:, 2], d[:, 3]
nu = nu_cm*29.9792458                     # GHz
h, k, c = 6.62607015e-34, 1.380649e-23, 2.99792458e8
def B(nu_GHz, T):
    f = nu_GHz*1e9
    return 2*h*f**3/c**2/np.expm1(h*f/(k*T))/1e-20      # MJy/sr
T0 = 2.72548
fig, axs = plt.subplots(1, 2, figsize=(11, 4.4), gridspec_kw={"width_ratios": [1.35, 1]})
ax = axs[0]
ff = np.linspace(1, 700, 600)
ax.plot(ff, B(ff, T0), color=C1, lw=2, label=f"blackbody, $T = {T0}$ K", zorder=2)
ax.errorbar(nu, I_MJy, yerr=400*sig_kJy/1e3, fmt="o", ms=4.5, color=C2, mec=SURF, mew=0.8, ecolor=C2, elinewidth=1.2, capsize=0,
            label="COBE/FIRAS (error bars $\\times 400$)", zorder=3)
ax.set_xlim(0, 700); ax.set_ylim(0, 420)
ax.set_xlabel("frequency (GHz)"); ax.set_ylabel("intensity (MJy sr$^{-1}$)")
ax.set_title("(a) the spectrum of the microwave sky", loc="left"); ax.legend(loc="upper right", fontsize=9.5)
ax = axs[1]
ax.axhline(0, color=INK2, lw=1)
ax.errorbar(nu, resid_kJy, yerr=sig_kJy, fmt="o", ms=4, color=C2, mec=SURF, mew=0.8, ecolor=C2, elinewidth=1.2, capsize=0)
ax.set_xlim(0, 700); ax.set_ylim(-160, 160)
ax.text(330, -150, "noisiest point (640 GHz) off scale", fontsize=8.5, color=INK2)
ax.set_xlabel("frequency (GHz)"); ax.set_ylabel("data minus blackbody (kJy sr$^{-1}$)")
ax.set_title("(b) residuals: 1000 times smaller scale", loc="left")
peak = ff[np.argmax(B(ff, T0))]
print("peak frequency %.1f GHz; peak intensity %.1f MJy/sr; max |resid| %.0f kJy/sr" % (peak, B(ff, T0).max(), np.abs(resid_kJy).max()))
save(fig, "cmb_spectrum")
