# Figures for the "Cosmic Dynamics" chapter of the cosmology notes. Usage: python3 scripts/cosmology/make_cosmic_dynamics_figures.py docs/astrophysics/figures
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch

OUT = sys.argv[1]
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
    fig.tight_layout(); fig.savefig(f"{OUT}/cosmic_dynamics_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- angular size of a galaxy of fixed size in the three geometries (no expansion) ----------
fig, ax = plt.subplots(figsize=(7, 4.6))
x = np.linspace(0.05, 3.0, 500)          # r / R0
ax.semilogy(x, 1/np.sin(x), color=C3, ls="-.", label=r"positive curvature: $D/[R_0\sin(r/R_0)]$")
ax.semilogy(x, 1/x, color=C2, ls="--", label=r"flat: $D/r$")
ax.semilogy(x, 1/np.sinh(x), color=C1, ls="-", label=r"negative curvature: $D/[R_0\sinh(r/R_0)]$")
ax.annotate("smallest at $r = \\pi R_0/2$,\nthen growing again", xy=(np.pi/2, 1), xytext=(0.95, 4.2), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.annotate("near the antipode a galaxy\nwould fill the sky", xy=(2.95, 1/np.sin(2.95)), xytext=(1.85, 11.0), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.annotate("exponentially small", xy=(2.6, 1/np.sinh(2.6)), xytext=(2.15, 0.035), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.set_xlim(0, 3.1); ax.set_ylim(0.01, 30)
ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]); ax.set_xticklabels(["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.set_xlabel(r"distance $r/R_0$"); ax.set_ylabel(r"angular size $\alpha$ in units of $D/R_0$")
ax.set_title("How big does a galaxy of diameter $D$ look?", loc="left")
ax.legend(loc="lower left", fontsize=9.5)
save(fig, "angular_size")

# ---------- the Newtonian sphere ----------
fig, ax = plt.subplots(figsize=(6.4, 6.0))
rng = np.random.default_rng(3)
pts = rng.uniform(-2.2, 2.2, size=(700, 2))
ax.scatter(pts[:, 0], pts[:, 1], s=3, color=INK2, alpha=0.45, zorder=1)
for r in [1.35, 1.7, 2.05]:
    ax.add_patch(Circle((0, 0), r, fill=False, ec=C2, lw=1.0, ls="--", zorder=2))
ax.add_patch(Circle((0, 0), 1.0, fc="#cde2fb", ec=C1, lw=2, alpha=0.9, zorder=2))
ax.scatter(pts[np.hypot(pts[:, 0], pts[:, 1]) < 1, 0], pts[np.hypot(pts[:, 0], pts[:, 1]) < 1, 1], s=3, color=INK2, alpha=0.7, zorder=3)
ax.plot([0.707], [0.707], "o", ms=9, color=INK, mec=SURF, mew=1.5, zorder=5)
ax.add_patch(FancyArrowPatch((0.707, 0.707), (0.43, 0.43), arrowstyle="-|>", mutation_scale=14, color=INK, lw=1.6, zorder=6))
ax.text(0.78, 0.80, "test mass $m$", fontsize=10, zorder=6)
ax.annotate("", xy=(1.0, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=C1, lw=1.4))
ax.text(0.32, -0.13, "$R_s(t) = a(t)\\,r_s$", fontsize=10, color=INK)
ax.text(-0.62, 0.35, "mass $M_s$", fontsize=10.5, color=INK)
ax.text(-2.15, 2.25, "outer shells (dashed): no net pull on anything inside them", fontsize=9.5, color=C2,
        bbox=dict(fc=SURF, ec="none", pad=1.5))
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.2, 2.45); ax.set_aspect("equal"); ax.grid(False)
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_visible(False)
ax.set_title("A sphere carved out of a uniform universe", loc="left")
save(fig, "newtonian_sphere")

# ---------- the equation-of-state line ----------
fig, ax = plt.subplots(figsize=(9, 3.1))
ax.axvspan(-1.6, -1/3, color="#cde2fb", alpha=0.7, lw=0)
ax.axvspan(-1/3, 1.15, color="#fbd9c8", alpha=0.7, lw=0)
ax.axhline(0, color=INK2, lw=1.2)
items = [(1, "stiff matter", "w = 1"), (1/3, "radiation", "w = 1/3"), (0, "matter", "w = 0"),
         (-1/3, "curvature term", "w = -1/3"), (-1, "cosmological\nconstant", "w = -1"), (-1.3, "phantom\nenergy", "w < -1")]
for w, name, lab in items:
    ax.plot([w], [0], "o", ms=9, color=INK if w != -1/3 else SURF, mec=INK, mew=1.5, zorder=4)
    ax.text(w, 0.16, name, ha="center", va="bottom", fontsize=10)
    ax.text(w, -0.16, "$" + lab + "$", ha="center", va="top", fontsize=10, color=INK2)
ax.text(-1.55, 0.78, "accelerates the expansion  ($\\varepsilon + 3P < 0$)", fontsize=10.5, va="center")
ax.text(0.0, 0.78, "decelerates the expansion  ($\\varepsilon + 3P > 0$)", fontsize=10.5, va="center")
ax.annotate("", xy=(1.12, -0.62), xytext=(-1.55, -0.62), arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.text(-1.55, -0.78, "dilutes faster as the universe grows:  $\\varepsilon \\propto a^{-3(1+w)}$", fontsize=10, va="top", color=INK2)
ax.set_xlim(-1.6, 1.15); ax.set_ylim(-1.05, 1.0)
ax.set_yticks([]); ax.set_xticks([]); ax.grid(False)
for s in ax.spines.values(): s.set_visible(False)
ax.set_title("The equation-of-state parameter $w = P/\\varepsilon$", loc="left")
save(fig, "equation_of_state")
