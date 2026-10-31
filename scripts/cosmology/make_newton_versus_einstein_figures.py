# Figures for the "Newton versus Einstein" chapter of the cosmology notes. Usage: python3 scripts/cosmology/make_newton_versus_einstein_figures.py docs/astrophysics/figures
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

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
    fig.tight_layout(); fig.savefig(f"{OUT}/newton_versus_einstein_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- F1: circumference of circles, S_kappa(r) ----------
fig, ax = plt.subplots(figsize=(7, 4.6))
x = np.linspace(0, np.pi, 400)
ax.plot(x, np.sinh(x), color=C1, ls="-", label=r"negative curvature: $\sinh(r/R)$")
ax.plot(x, x, color=C2, ls="--", label=r"flat: $r/R$")
ax.plot(x, np.sin(x), color=C3, ls="-.", label=r"positive curvature: $\sin(r/R)$")
ax.plot([np.pi/2], [1], "o", color=C3, ms=7, mec=SURF, mew=1.5)
ax.annotate("equator: largest circle", xy=(np.pi/2, 1), xytext=(1.75, 1.75), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.plot([np.pi], [0], "o", color=C3, ms=7, mec=SURF, mew=1.5, clip_on=False, zorder=5)
ax.annotate("antipode: the circle\nshrinks to a point", xy=(np.pi, 0), xytext=(2.3, 1.2), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.set_xlim(0, np.pi); ax.set_ylim(0, 4)
ax.set_xticks([0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]); ax.set_xticklabels(["0", r"$\pi/4$", r"$\pi/2$", r"$3\pi/4$", r"$\pi$"])
ax.set_xlabel(r"radius of the circle, measured inside the space: $r/R$")
ax.set_ylabel(r"circumference $/\,2\pi R$")
ax.set_title("How big is a circle of radius $r$?", loc="left")
ax.legend(loc="upper left", fontsize=9.5)
save(fig, "circles")

# ---------- F2: sphere and hyperboloid with geodesic triangles ----------
fig = plt.figure(figsize=(10.5, 5.0))
ax = fig.add_subplot(1, 2, 1, projection="3d")
u, v = np.mgrid[0:2*np.pi:60j, 0:np.pi:30j]
ax.plot_wireframe(np.cos(u)*np.sin(v), np.sin(u)*np.sin(v), np.cos(v), color="#9ec5f4", linewidth=0.4, rstride=3, cstride=3)
s = np.linspace(0, np.pi/2, 100)
for arc in [(np.cos(s), np.sin(s), 0*s), (0*s, np.cos(s), np.sin(s)), (np.sin(s), 0*s, np.cos(s))]:
    ax.plot(*arc, color=C2, lw=2.6)
for p in [(1, 0, 0), (0, 1, 0), (0, 0, 1)]:
    ax.scatter(*p, color=INK, s=18)
ax.set_box_aspect((1, 1, 1)); ax.set_axis_off(); ax.view_init(elev=22, azim=30)
ax.set_title("(a) sphere: three right angles,\nangle sum $270^\\circ = \\pi + A/R^2$", loc="left", fontsize=11)
ax = fig.add_subplot(1, 2, 2, projection="3d")
rr, th = np.mgrid[0:1.7:18j, 0:2*np.pi:40j]
X, Y = np.sinh(rr)*np.cos(th), np.sinh(rr)*np.sin(th); W = np.cosh(rr)
ax.plot_wireframe(X, Y, W, color="#9ec5f4", linewidth=0.4)
def mink(p, q): return p[0]*q[0] + p[1]*q[1] - p[2]*q[2]
d = 1.3
verts = [np.array([np.sinh(d)*np.cos(t), np.sinh(d)*np.sin(t), np.cosh(d)]) for t in (np.pi/2, np.pi/2 + 2*np.pi/3, np.pi/2 + 4*np.pi/3)]
for i in range(3):
    p, q = verts[i], verts[(i+1) % 3]
    D = np.arccosh(-mink(p, q)); ss = np.linspace(0, 1, 100)[:, None]
    g = (np.sinh((1-ss)*D)*p + np.sinh(ss*D)*q)/np.sinh(D)
    ax.plot(g[:, 0], g[:, 1], g[:, 2], color=C2, lw=2.6)
    ax.scatter(*p, color=INK, s=18)
D = np.arccosh(-mink(verts[0], verts[1])); ch = np.cosh(D)
ang = np.degrees(np.arccos(ch*(ch - 1)/np.sinh(D)**2))
ax.set_box_aspect((1, 1, 0.75)); ax.set_axis_off(); ax.view_init(elev=68, azim=-90)
ax.set_title(f"(b) hyperboloid $w^2-x^2-y^2=R^2$ in Minkowski space:\nangle sum ${3*ang:.0f}^\\circ = \\pi - A/R^2$", loc="left", fontsize=11)
print("hyperbolic triangle angle each", ang, "sum", 3*ang, "area/R^2", np.pi - np.radians(3*ang))
save(fig, "surfaces")

# ---------- F3: Hubble's law from two viewpoints ----------
rng = np.random.default_rng(7)
g = np.linspace(-1.8, 1.8, 7)
P = np.array([(x, y) for x in g for y in g]) + rng.uniform(-0.18, 0.18, size=(49, 2))
A, B = P[16], P[32]
fig, axs = plt.subplots(1, 2, figsize=(10, 4.9))
for ax, O, col, name in [(axs[0], A, C1, "A"), (axs[1], B, C2, "B")]:
    rel1 = P - O; rel2 = 1.25*(P - O)
    ax.scatter(rel1[:, 0], rel1[:, 1], s=16, color=INK2, zorder=3)
    for r1, r2 in zip(rel1, rel2):
        if np.hypot(*r1) > 1e-9:
            ax.annotate("", xy=r2, xytext=r1, arrowprops=dict(arrowstyle="-|>", color=col, lw=1.3))
    ax.plot([0], [0], "o", ms=10, color=col, mec=SURF, mew=1.5, zorder=4)
    ax.text(-0.12, -0.42, f"galaxy {name}", ha="right", fontsize=10, bbox=dict(fc=SURF, ec="none", pad=1), zorder=5)
    ax.set_xlim(-3.2, 3.2); ax.set_ylim(-3.2, 3.2); ax.set_aspect("equal")
    ax.set_xlabel("position relative to " + name); ax.grid(False)
    ax.set_title(f"({'a' if name=='A' else 'b'}) the same expansion, seen from galaxy {name}", loc="left")
save(fig, "every_galaxy_a_centre")

# ---------- F4: two wave crests in (t, r) and in (eta, r) ----------
# matter-dominated illustration: a = t^(2/3) with t0 = 1, c = 1, so eta = 3 t^(1/3)
eta0, rs, deta = 3.0, 1.5, 0.15
t_of_eta = lambda e: (e/3.0)**3
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.6))
for k, col in [(0, C1), (1, C2)]:
    eo = eta0 + k*deta; e = np.linspace(eo - rs, eo, 200); r = eo - e
    axs[0].plot(r, t_of_eta(e), color=col, lw=2.2, label="first crest" if k == 0 else "next crest")
    axs[1].plot(r, e, color=col, lw=2.2, label="first crest" if k == 0 else "next crest")
te1, te2 = t_of_eta(eta0 - rs), t_of_eta(eta0 + deta - rs); to1, to2 = t_of_eta(eta0), t_of_eta(eta0 + deta)
ax = axs[0]
ax.axvline(rs, color=INK2, lw=1, ls=":"); ax.axvline(0, color=INK2, lw=1, ls=":")
ax.annotate("", xy=(rs+0.04, te2), xytext=(rs+0.04, te1), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
ax.text(rs+0.07, (te1+te2)/2, r"$\Delta t_e$", fontsize=11, va="center")
ax.annotate("", xy=(-0.04, to2), xytext=(-0.04, to1), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
ax.text(-0.28, (to1+to2)/2, r"$\Delta t_0$", fontsize=11, va="center")
ax.text(rs-0.02, 0.02, "source", ha="right", fontsize=10); ax.text(0.03, 0.02, "observer", fontsize=10)
ax.set_xlim(-0.35, 1.85); ax.set_ylim(0, 1.25)
ax.set_xlabel("comoving distance $r$"); ax.set_ylabel("cosmic time $t$")
ax.set_title(r"(a) cosmic time: $\Delta t_0 = (1+z)\,\Delta t_e$", loc="left"); ax.legend(loc="upper right", fontsize=9.5)
ax = axs[1]
ax.axvline(rs, color=INK2, lw=1, ls=":"); ax.axvline(0, color=INK2, lw=1, ls=":")
ax.annotate("", xy=(rs+0.04, eta0+deta-rs), xytext=(rs+0.04, eta0-rs), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
ax.text(rs+0.07, eta0-rs+deta/2, r"$\Delta\eta$", fontsize=11, va="center")
ax.annotate("", xy=(-0.04, eta0+deta), xytext=(-0.04, eta0), arrowprops=dict(arrowstyle="<->", color=INK, lw=1))
ax.text(-0.28, eta0+deta/2, r"$\Delta\eta$", fontsize=11, va="center")
ax.set_xlim(-0.35, 1.85); ax.set_ylim(1.2, 3.4); ax.set_aspect("equal")
ax.set_xlabel("comoving distance $r$"); ax.set_ylabel(r"conformal time $\eta$")
ax.set_title(r"(b) conformal time: the gap stays the same", loc="left"); ax.legend(loc="lower right", fontsize=9.5)
print("z of illustration:", 1/(t_of_eta(eta0 - rs))**(2/3) - 1, " dt ratio:", (to2-to1)/(te2-te1))
save(fig, "redshift_crests")

# ---------- F5: a flat torus universe ----------
fig, ax = plt.subplots(figsize=(6.2, 6.2))
L = 1.0
gal = {"star": (0.25, 0.7), "tri": (0.75, 0.3)}
obs = (0.45, 0.45)
for i in range(-1, 2):
    for j in range(-1, 2):
        ax.add_patch(plt.Rectangle((i*L, j*L), L, L, fill=(i == 0 and j == 0), fc="#cde2fb", ec=INK2, lw=1.2 if (i, j) == (0, 0) else 0.8, ls="-" if (i, j) == (0, 0) else "--"))
        ax.plot(gal["star"][0]+i*L, gal["star"][1]+j*L, marker="*", ms=14, color=C2, mec=SURF, mew=0.8, ls="none")
        ax.plot(gal["tri"][0]+i*L, gal["tri"][1]+j*L, marker="^", ms=10, color=C3, mec=SURF, mew=0.8, ls="none")
        if (i, j) != (0, 0) and abs(i) + abs(j) <= 2:
            gx, gy = gal["star"][0]+i*L, gal["star"][1]+j*L
            ax.plot([obs[0], gx], [obs[1], gy], color=C2, lw=0.9, alpha=0.7)
ax.plot([obs[0], gal["star"][0]], [obs[1], gal["star"][1]], color=C2, lw=0.9, alpha=0.7)
ax.plot(*obs, "o", ms=9, color=C1, mec=SURF, mew=1.5)
ax.text(obs[0]+0.04, obs[1]-0.09, "us", fontsize=10)
ax.text(0.02, 1.03, "the real universe: one square,\nopposite edges glued", fontsize=9.5, va="bottom")
ax.set_xlim(-1, 2); ax.set_ylim(-1, 2); ax.set_aspect("equal"); ax.grid(False)
ax.set_xticks([]); ax.set_yticks([])
ax.set_title("A flat torus universe: one galaxy, many images", loc="left")
save(fig, "torus")
