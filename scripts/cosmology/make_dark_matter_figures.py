# Figures for the "Dark Matter" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_dark_matter_figures.py docs/astrophysics/figures scripts/cosmology/data/NGC3198_rotmod.dat
# The rotation-curve file is from the SPARC database (Lelli, McGaugh & Schombert 2016):
# https://astroweb.case.edu/SPARC/ (Rotmod_LTG.zip). Velocities for the stellar disc are for a mass-to-light
# ratio of 1 at 3.6 microns; we scale them to the commonly adopted 0.5.
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

OUT, ROT = sys.argv[1], sys.argv[2]
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
    fig.tight_layout(); fig.savefig(f"{OUT}/dark_matter_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- rotation curve of NGC 3198 ----------
d = np.loadtxt(ROT, comments="#")
R, V, eV, Vgas, Vdisk, Vbul = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4], d[:, 5]
Ud = 0.5
Vstar2 = Ud*Vdisk*np.abs(Vdisk) + 0.7*Vbul*np.abs(Vbul)
Vbar = np.sqrt(np.clip(Vgas*np.abs(Vgas) + Vstar2, 0, None))
Vdm = np.sqrt(np.clip(V**2 - Vbar**2, 0, None))
fig, ax = plt.subplots(figsize=(7.2, 4.8))
ax.errorbar(R, V, yerr=eV, fmt="o", ms=5, color=INK, mec=SURF, mew=0.8, elinewidth=1, capsize=0, label="measured (21 cm and H$\\alpha$)", zorder=4)
ax.plot(R, np.sqrt(np.clip(Vstar2, 0, None)), color=C2, ls="--", label="stars alone")
ax.plot(R, np.sign(Vgas)*np.sqrt(np.abs(Vgas*np.abs(Vgas))), color=C3, ls="-.", label="gas alone")
ax.plot(R, Vbar, color=C1, ls="-", label="all visible matter")
ax.plot(R, Vdm, color=C4, ls=(0, (1, 1.5)), lw=2.4, label="needed from dark matter")
ax.set_xlim(0, R.max()*1.05); ax.set_ylim(0, 205)
ax.set_xlabel("distance from the centre $R$ (kpc)"); ax.set_ylabel("orbital speed $v$ (km s$^{-1}$)")
ax.set_title("The spiral galaxy NGC 3198: a flat rotation curve", loc="left")
ax.legend(loc="upper center", fontsize=9.5, ncol=3, bbox_to_anchor=(0.5, 1.0))
print("NGC3198 last radius %.1f kpc, v=%.0f km/s, Vbar there %.0f" % (R[-1], V[-1], Vbar[-1]))
save(fig, "rotation_curve")

# ---------- gravitational lensing geometry ----------
from matplotlib.patches import Arc
fig, ax = plt.subplots(figsize=(9, 4.6))
xo, xl, xs, bb = 0.0, 5.0, 10.0, 1.1
ax.plot([xo], [0], "o", ms=9, color=INK); ax.text(xo, -0.42, "observer", ha="center", fontsize=10)
ax.add_patch(Circle((xl, 0), 0.25, color=C4, alpha=0.9)); ax.text(xl + 0.35, -0.12, "lens, mass $M$", fontsize=10)
ax.plot([xs], [0], "*", ms=16, color=C2); ax.text(xs, -0.42, "source", ha="center", fontsize=10)
yimg = bb*xs/xl
for sgn in (+1, -1):
    ax.plot([xs, xl], [0, sgn*bb], color=C1, lw=1.8); ax.plot([xl, xo], [sgn*bb, 0], color=C1, lw=1.8)
    ax.plot([xl, xs], [sgn*bb, sgn*yimg], color=C1, lw=1, ls=":")
    ax.plot([xs], [sgn*yimg], "*", ms=12, color=C2, alpha=0.4)
ax.text(xs - 0.1, yimg + 0.18, "apparent image", ha="center", fontsize=9.5, color=INK2)
ax.text(xs - 0.1, -yimg - 0.4, "apparent image", ha="center", fontsize=9.5, color=INK2)
ax.annotate("", xy=(xl, bb), xytext=(xl, 0.27), arrowprops=dict(arrowstyle="->", color=INK2, lw=1))
ax.text(xl - 0.3, 0.55, "$b$", fontsize=11)
ax.text(xl - 1.7, bb + 0.25, r"bent by $\alpha = 4GM/c^2b$", fontsize=10)
ang = np.degrees(np.arctan(bb/xl))
ax.add_patch(Arc((xo, 0), 2.4, 2.4, theta1=0, theta2=ang, color=INK2, lw=1))
ax.text(1.3, 0.08, r"$\theta_E$", fontsize=11)
ax.annotate("", xy=(xl, -2.55), xytext=(xo, -2.55), arrowprops=dict(arrowstyle="<->", color=INK2, lw=1)); ax.text(xl/2, -2.85, "$x\\,d$", ha="center", fontsize=10)
ax.annotate("", xy=(xs, -3.15), xytext=(xo, -3.15), arrowprops=dict(arrowstyle="<->", color=INK2, lw=1)); ax.text(xs/2, -3.45, "$d$", ha="center", fontsize=10)
ax.set_xlim(-0.6, 10.9); ax.set_ylim(-3.6, 2.9); ax.set_aspect("equal"); ax.axis("off")
ax.set_title("Gravitational lensing: light from one source reaches us along several paths", loc="left")
save(fig, "lensing_geometry")

# ---------- the matter census ----------
fig, ax = plt.subplots(figsize=(8, 3.6))
items = [("stars", 0.0027, C2), ("all baryons", 0.049, C3), ("neutrinos", 0.0014, INK2),
         ("dark matter", 0.264, C1), ("all matter", 0.315, INK), ("dark energy", 0.685, C4)]
for i, (lab, val, col) in enumerate(items):
    ax.barh(i, val, color=col, height=0.62)
    ax.text(val*1.15, i, f"{val:g}", va="center", fontsize=10)
ax.set_yticks(range(len(items))); ax.set_yticklabels([x[0] for x in items])
ax.invert_yaxis(); ax.set_xscale("log"); ax.set_xlim(5e-4, 2)
ax.set_xlabel(r"density parameter $\Omega_0$"); ax.grid(axis="y", visible=False)
ax.set_title("What the universe is made of", loc="left")
save(fig, "census")
