#!/usr/bin/env python3
"""Generate Figures 13, 14, 15, 16, 18 and 19 of Maths 2 (the Representations & Characters chapter).

Usage: python make_maths2_rep_figures.py OUT_DIR (writes the PNGs into OUT_DIR, e.g. docs/maths/figures).
Reproduces the published PNGs byte for byte with matplotlib 3.10 (the lecture-notes skill venv).

Recomputes and asserts every mathematical quantity drawn:
1. Figure 13 (maths2_rep_maschke_averaging.png): Maschke averaging in the S_3
   permutation module (non-invariant projection phi vs averaged projection vartheta).
2. Figure 14 (maths2_rep_unit_circle_trace_kernel.png): Unit-circle eigenvalue sums
   for (a) a 3-cycle in S_3, (b) a^2 in D_8, and (c) the identity 1.
3. Figure 15 (maths2_rep_d8_square_modes.png): Irreducible mode decomposition
   V = Ve_1 + Ve_4 + Ve_5 of the 4-dimensional permutation module of D_8.
4. Figure 16 (maths2_rep_s5_a5_restriction.png): Index-2 restriction from S_5 to A_5
   and splitting of the 5-cycle conjugacy class.
5. Figure 18 (maths2_rep_orbital_grids.png): S_4 orbital grids on points (4x4, rank 2)
   and on 2-subsets (6x6, rank 3).
6. Figure 19 (maths2_rep_sn_ksubset_staircase.png): Staircase decomposition of
   pi_0, pi_1, pi_2, pi_3 for S_6 and the 4-region Venn diagram for I_k x I_l.
"""

import itertools
import math
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

DEFAULT_OUT_DIR = "/home/ubuntu/test/temp_gemini/20261104/rep_figures_gemini_to_host/"

# Okabe-Ito colourblind-safe palette
OI_ORANGE = "#E69F00"
OI_SKY = "#56B4E9"
OI_GREEN = "#009E73"
OI_YELLOW = "#F0E442"
OI_BLUE = "#0072B2"
OI_VERMILION = "#D55E00"
OI_PURPLE = "#CC79A7"
DARK_GREY = "#1A1A1A"
MID_GREY = "#4A4A4A"
LIGHT_GREY = "#E8E8E8"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.titlesize": 11.2,
    "axes.labelsize": 10.5,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "text.color": DARK_GREY,
    "axes.labelcolor": DARK_GREY,
    "xtick.color": DARK_GREY,
    "ytick.color": DARK_GREY,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "savefig.dpi": 200,
})


def perm_compose(p, q):
    """Compose permutations p and q left-to-right: i(pq) = (ip)q (0-indexed tuples)."""
    return tuple(q[p[i]] for i in range(len(p)))


def perm_inv(p):
    """Inverse of a 0-indexed permutation tuple."""
    inv = [0] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def perm_matrix(p):
    """Right-action permutation matrix: row i has 1 in column ip."""
    n = len(p)
    M = np.zeros((n, n), dtype=float)
    for i, j in enumerate(p):
        M[i, j] = 1.0
    return M


# =============================================================================
# Figure 1: Maschke averaging in the S_3 permutation module
# =============================================================================
def make_figure_1(out_dir):
    # Recompute S_3 permutation matrices and averaged projection
    s3_perms = list(itertools.permutations(range(3)))
    assert len(s3_perms) == 6

    # Projection phi onto U = sp(v_1+v_2+v_3) along W_0 = sp(v_1, v_2):
    # v_1 phi = 0, v_2 phi = 0, v_3 phi = v_1 + v_2 + v_3
    P_phi = np.array([
        [0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0],
        [1.0, 1.0, 1.0],
    ])
    assert np.allclose(P_phi @ P_phi, P_phi)

    # Check W_0 is not S_3-invariant: v_2 (2 3) = v_3 not in W_0
    g_23 = (0, 2, 1)
    v2 = np.array([0.0, 1.0, 0.0])
    v3 = np.array([0.0, 0.0, 1.0])
    assert np.allclose(v2 @ perm_matrix(g_23), v3)

    # Average phi over S_3: vartheta = (1/6) sum_{g in S_3} g phi g^{-1}
    P_theta = np.zeros((3, 3), dtype=float)
    for g in s3_perms:
        Pg = perm_matrix(g)
        Pg_inv = perm_matrix(perm_inv(g))
        P_theta += Pg @ P_phi @ Pg_inv
    P_theta /= 6.0

    assert np.allclose(P_theta, np.ones((3, 3)) / 3.0)
    assert np.allclose(P_theta @ P_theta, P_theta)
    for g in s3_perms:
        Pg = perm_matrix(g)
        assert np.allclose(Pg @ P_theta, P_theta @ Pg)

    v3_phi = v3 @ P_phi
    v3_theta = v3 @ P_theta
    assert np.allclose(v3_phi, np.array([1.0, 1.0, 1.0]))
    assert np.allclose(v3_theta, np.array([1.0 / 3.0, 1.0 / 3.0, 1.0 / 3.0]))
    assert abs((v3 - v3_phi)[2]) < 1e-12
    assert abs(np.sum(v3 - v3_theta)) < 1e-12

    fig = plt.figure(figsize=(10.6, 4.7))
    ax1 = fig.add_subplot(1, 2, 1, projection="3d")
    ax2 = fig.add_subplot(1, 2, 2, projection="3d")

    label_box = dict(boxstyle="round,pad=0.20", fc=(1.0, 1.0, 1.0, 0.88), ec="#CCCCCC", lw=0.8)

    def setup_3d_axes(ax, title_text):
        ax.set_xlim(-0.68, 1.25)
        ax.set_ylim(-0.68, 1.25)
        ax.set_zlim(-0.68, 1.28)
        ax.view_init(elev=25, azim=-22)
        ax.set_xticks([0, 1])
        ax.set_yticks([0, 1])
        ax.set_zticks([0, 1])
        ax.xaxis.pane.fill = False
        ax.yaxis.pane.fill = False
        ax.zaxis.pane.fill = False
        ax.xaxis.pane.set_edgecolor("#DDDDDD")
        ax.yaxis.pane.set_edgecolor("#DDDDDD")
        ax.zaxis.pane.set_edgecolor("#DDDDDD")
        ax.grid(True, linestyle=":", alpha=0.45, color="#BBBBBB")
        # Draw coordinate axes through origin
        ax.plot([0, 1.15], [0, 0], [0, 0], color=MID_GREY, lw=1.2)
        ax.plot([0, 0], [0, 1.15], [0, 0], color=MID_GREY, lw=1.2)
        ax.plot([0, 0], [0, 0], [0, 1.15], color=MID_GREY, lw=1.2)
        ax.text(1.10, -0.26, 0.02, r"$v_1$", fontsize=11, fontweight="bold", color=DARK_GREY)
        ax.text(0.10, 1.22, -0.12, r"$v_2$", fontsize=11, fontweight="bold", color=DARK_GREY)
        ax.text(-0.20, -0.14, 1.16, r"$v_3$", fontsize=11, fontweight="bold", color=DARK_GREY)
        # Invariant line U = sp(v_1 + v_2 + v_3)
        ax.plot([-0.42, 1.12], [-0.42, 1.12], [-0.42, 1.12],
                color=OI_BLUE, lw=2.6)
        ax.set_title(title_text, pad=8, fontsize=11, fontweight="bold", color=DARK_GREY)

    # Panel (a): Unaveraged projection phi along W_0 = sp(v_1, v_2)
    setup_3d_axes(ax1, r"(a) Initial projection $\phi$ along $W_0 = \mathrm{sp}(v_1, v_2)$")
    w0_verts = [[(-0.38, -0.38, 0), (1.12, -0.38, 0), (1.12, 1.12, 0), (-0.38, 1.12, 0)]]
    poly_w0 = Poly3DCollection(w0_verts, alpha=0.25, facecolor=OI_ORANGE, edgecolor=OI_ORANGE, lw=1.2)
    ax1.add_collection3d(poly_w0)
    ax1.text2D(0.70, 0.36, r"$W_0 = \mathrm{sp}(v_1, v_2)$" + "\n(not a submodule)",
               transform=ax1.transAxes, color=DARK_GREY, fontsize=8.4,
               fontweight="bold", ha="center", va="center", bbox=label_box)

    # Vector v_3 and its image v_3 phi = (1, 1, 1)
    ax1.quiver(0, 0, 0, 0, 0, 1, color=DARK_GREY, lw=2.2, arrow_length_ratio=0.12)
    ax1.scatter([0], [0], [1], color=DARK_GREY, s=35, zorder=5)
    ax1.scatter([1], [1], [1], color=OI_VERMILION, s=50, zorder=6)
    # Projection arrow from v_3=(0,0,1) to v_3 phi=(1,1,1) parallel to W_0
    ax1.quiver(0, 0, 1, 1, 1, 0, color=OI_VERMILION, lw=2.0, arrow_length_ratio=0.10)
    ax1.text2D(0.53, 0.60, r"parallel to $W_0$", transform=ax1.transAxes,
               color=DARK_GREY, fontsize=9.2, ha="center", va="center")
    ax1.text2D(0.68, 0.78, r"$v_3\phi = v_1+v_2+v_3$", transform=ax1.transAxes,
               color=DARK_GREY, fontsize=9.4, fontweight="bold", ha="center", va="center", bbox=label_box)
    ax1.text2D(0.21, 0.36, r"$U$", transform=ax1.transAxes,
               color=DARK_GREY, fontsize=10.5, fontweight="bold", ha="center", va="center")

    # Panel (b): Averaged projection vartheta along W = {lambda_1 + lambda_2 + lambda_3 = 0}
    setup_3d_axes(ax2, r"(b) Averaged projection $\vartheta$ along $W = \ker\vartheta$")
    r_plane = 0.80
    e1_w = np.array([1.0, -1.0, 0.0]) / np.sqrt(2.0)
    e2_w = np.array([1.0, 1.0, -2.0]) / np.sqrt(6.0)
    angles = np.linspace(0, 2 * np.pi, 7)[:-1]
    w_pts = [tuple(r_plane * (np.cos(a) * e1_w + np.sin(a) * e2_w)) for a in angles]
    poly_w = Poly3DCollection([w_pts], alpha=0.28, facecolor=OI_GREEN, edgecolor=OI_GREEN, lw=1.4)
    ax2.add_collection3d(poly_w)
    ax2.text2D(0.71, 0.35, r"$W : \lambda_1+\lambda_2+\lambda_3=0$" + "\n" + r"($FS_3$-submodule)",
               transform=ax2.transAxes, color=DARK_GREY, fontsize=8.4,
               fontweight="bold", ha="center", va="center", bbox=label_box)

    # Vector v_3 and its averaged image v_3 vartheta = (1/3, 1/3, 1/3)
    ax2.quiver(0, 0, 0, 0, 0, 1, color=DARK_GREY, lw=2.2, arrow_length_ratio=0.12)
    ax2.scatter([0], [0], [1], color=DARK_GREY, s=35, zorder=5)
    ax2.scatter([1/3], [1/3], [1/3], color=OI_VERMILION, s=55, zorder=6)
    ax2.quiver(0, 0, 1, 1/3, 1/3, -2/3, color=OI_VERMILION, lw=2.2, arrow_length_ratio=0.16)
    ax2.text2D(0.54, 0.72, r"parallel to $W$", transform=ax2.transAxes,
               color=DARK_GREY, fontsize=9.2, ha="center", va="center")
    ax2.text2D(0.68, 0.63, r"$v_3\vartheta = \frac{1}{3}(v_1+v_2+v_3)$", transform=ax2.transAxes,
               color=DARK_GREY, fontsize=8.8, fontweight="bold", ha="center", va="center", bbox=label_box)
    ax2.text2D(0.84, 0.56, r"$U$", transform=ax2.transAxes,
               color=DARK_GREY, fontsize=10.5, fontweight="bold", ha="center", va="center")

    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.04, top=0.90, wspace=0.06)
    path = os.path.join(out_dir, "maths2_rep_maschke_averaging.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved {path}")


# =============================================================================
# Figure 2: Unit-circle eigenvalue sums and kernel/scalar criteria
# =============================================================================
def make_figure_2(out_dir):
    # Recompute eigenvalues for the three panels
    M_3cycle = perm_matrix((1, 2, 0))
    evals_a = np.linalg.eigvals(M_3cycle)
    omega = np.exp(2j * np.pi / 3.0)
    expected_a = np.array([1.0 + 0j, omega, omega**2])
    assert np.allclose(
        sorted(evals_a, key=lambda z: np.angle(z)),
        sorted(expected_a, key=lambda z: np.angle(z))
    )
    assert abs(np.sum(expected_a)) < 1e-12

    a_rho = np.array([[0.0, 1.0], [-1.0, 0.0]])
    a2_rho = a_rho @ a_rho
    assert np.allclose(a2_rho, -np.eye(2))
    evals_b = np.linalg.eigvals(a2_rho)
    assert np.allclose(evals_b, [-1.0, -1.0])
    assert abs(np.sum(evals_b) - (-2.0)) < 1e-12
    assert abs(abs(np.sum(evals_b)) - 2.0) < 1e-12

    I2 = np.eye(2)
    evals_c = np.linalg.eigvals(I2)
    assert np.allclose(evals_c, [1.0, 1.0])
    assert abs(np.sum(evals_c) - 2.0) < 1e-12

    fig, axes = plt.subplots(1, 3, figsize=(11.5, 4.0))

    theta = np.linspace(0, 2 * np.pi, 240)
    uc_x, uc_y = np.cos(theta), np.sin(theta)

    # --- Panel (a): 1, omega, omega^2 summing to 0 ---
    ax = axes[0]
    ax.set_aspect("equal")
    ax.set_xlim(-1.58, 1.58)
    ax.set_ylim(-1.48, 1.48)
    ax.axhline(0, color="#CCCCCC", lw=1.0, zorder=1)
    ax.axvline(0, color="#CCCCCC", lw=1.0, zorder=1)
    ax.plot(uc_x, uc_y, color=MID_GREY, ls="--", lw=1.3, zorder=2)

    for z, lbl, pos in [
        (1.0 + 0j, r"$\omega_1 = 1$", (1.06, 0.04)),
        (omega, r"$\omega_2 = \omega$", (-1.18, 0.96)),
        (omega**2, r"$\omega_3 = \omega^2$", (-1.22, -1.08)),
    ]:
        ax.annotate("", xy=(z.real, z.imag), xytext=(0, 0),
                    arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.32",
                                    color=OI_BLUE, lw=2.2), zorder=4)
        ax.text(pos[0], pos[1], lbl, color=DARK_GREY, fontsize=9.8, fontweight="bold")

    p0 = 0.0 + 0j
    p1 = 1.0 + 0j
    p2 = 1.0 + omega
    for start, end in [(p0, p1), (p1, p2), (p2, p0)]:
        ax.annotate("", xy=(end.real, end.imag), xytext=(start.real, start.imag),
                    arrowprops=dict(arrowstyle="->,head_width=0.20,head_length=0.28",
                                    color=OI_ORANGE, lw=1.9, ls=":"), zorder=5)
    ax.scatter([0], [0], color=OI_VERMILION, s=55, zorder=6)
    ax.text(0.58, 0.92, r"$1+\omega$", color=DARK_GREY, fontsize=9.2, fontweight="bold")
    ax.text(0.02, -0.58, r"$\chi(g) = 0$" + "\n(closed triangle)",
            color=DARK_GREY, fontsize=8.2, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.18", fc="#FFF8F2", ec=OI_ORANGE, lw=0.9))
    ax.set_title(r"(a) $3$-cycle in $S_3$: $1+\omega+\omega^2 = 0$", fontsize=10.5, fontweight="bold")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im", labelpad=4)

    # --- Panel (b): eigenvalues -1, -1 of a^2 rho in D_8 summing to -2 ---
    ax = axes[1]
    ax.set_aspect("equal")
    ax.set_xlim(-2.30, 1.35)
    ax.set_ylim(-1.50, 1.50)
    ax.axhline(0, color="#CCCCCC", lw=1.0, zorder=1)
    ax.axvline(0, color="#CCCCCC", lw=1.0, zorder=1)
    ax.plot(uc_x, uc_y, color=MID_GREY, ls="--", lw=1.3, zorder=2)
    ax.text(0.52, 0.98, "unit circle", color=MID_GREY, fontsize=9.0)

    ax.annotate("", xy=(-1.0, 0.08), xytext=(0.0, 0.08),
                arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.32",
                                color=OI_BLUE, lw=2.3), zorder=4)
    ax.text(-0.72, 0.22, r"$\omega_1 = -1$", color=DARK_GREY, fontsize=9.8, fontweight="bold")
    ax.annotate("", xy=(-2.0, -0.06), xytext=(-1.0, -0.06),
                arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.32",
                                color=OI_ORANGE, lw=2.3), zorder=4)
    ax.text(-1.82, -0.35, r"$\omega_2 = -1$", color=DARK_GREY, fontsize=9.8, fontweight="bold")
    ax.scatter([-1.0, -2.0], [0.0, 0.0], color=[OI_BLUE, OI_VERMILION], s=50, zorder=6)
    ax.text(-2.18, 0.56, r"$\chi(a^2) = -2$" + "\n" + r"$|\chi(a^2)| = \chi(1) = 2$" + "\n" + r"$\Rightarrow a^2\rho = -I_2$",
            color=DARK_GREY, fontsize=9.2, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.24", fc="#FFF5F0", ec=OI_VERMILION, lw=1.1))
    ax.set_title(r"(b) $a^2\rho$ in $D_8$: $(-1)+(-1) = -2$", fontsize=10.5, fontweight="bold")
    ax.set_xlabel("Re")

    # --- Panel (c): eigenvalues 1, 1 of identity 1 summing to +2 ---
    ax = axes[2]
    ax.set_aspect("equal")
    ax.set_xlim(-1.35, 2.30)
    ax.set_ylim(-1.50, 1.50)
    ax.axhline(0, color="#CCCCCC", lw=1.0, zorder=1)
    ax.axvline(0, color="#CCCCCC", lw=1.0, zorder=1)
    ax.plot(uc_x, uc_y, color=MID_GREY, ls="--", lw=1.3, zorder=2)
    ax.text(-1.24, 0.98, "unit circle", color=MID_GREY, fontsize=9.0)

    ax.annotate("", xy=(1.0, 0.08), xytext=(0.0, 0.08),
                arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.32",
                                color=OI_BLUE, lw=2.3), zorder=4)
    ax.text(0.20, 0.22, r"$\omega_1 = 1$", color=DARK_GREY, fontsize=9.8, fontweight="bold")
    ax.annotate("", xy=(2.0, -0.06), xytext=(1.0, -0.06),
                arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.32",
                                color=OI_GREEN, lw=2.3), zorder=4)
    ax.text(1.20, -0.35, r"$\omega_2 = 1$", color=DARK_GREY, fontsize=9.8, fontweight="bold")
    ax.scatter([1.0, 2.0], [0.0, 0.0], color=[OI_BLUE, OI_GREEN], s=50, zorder=6)
    ax.text(0.42, 0.56, r"$\chi(g) = 2 = \chi(1)$" + "\n" + r"$\Rightarrow g\rho = I_2$" + "\n" + r"($g \in \ker\chi$)",
            color=DARK_GREY, fontsize=9.2, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.24", fc="#F2FBF7", ec=OI_GREEN, lw=1.1))
    ax.set_title(r"(c) $g \in \ker\chi$: $1+1 = 2 = \chi(1)$", fontsize=10.5, fontweight="bold")
    ax.set_xlabel("Re")

    fig.subplots_adjust(left=0.065, right=0.985, bottom=0.13, top=0.88, wspace=0.22)
    path = os.path.join(out_dir, "maths2_rep_unit_circle_trace_kernel.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved {path}")


# =============================================================================
# Figure 3: D_8 square modes for V = Ve_1 + Ve_4 + Ve_5
# =============================================================================
def make_figure_3(out_dir):
    # Recompute D_8 elements (0-indexed for {1, 2, 3, 4}) with left-to-right composition
    e = (0, 1, 2, 3)
    a = (1, 2, 3, 0)         # (1 2 3 4)
    a2 = perm_compose(a, a)  # (1 3)(2 4)
    a3 = perm_compose(a2, a) # (1 4 3 2)
    b = (1, 0, 3, 2)         # (1 2)(3 4)
    ab = perm_compose(a, b)  # (2 4) -> 0-indexed: (0, 3, 2, 1)
    a2b = perm_compose(a2, b)# (1 4)(2 3) -> 0-indexed: (3, 2, 1, 0)
    a3b = perm_compose(a3, b)# (1 3) -> 0-indexed: (2, 1, 0, 3)

    assert ab == (0, 3, 2, 1), f"Expected (2 4), got {ab}"
    assert a3b == (2, 1, 0, 3), f"Expected (1 3), got {a3b}"
    assert a2 == (2, 3, 0, 1)
    assert a2b == (3, 2, 1, 0)

    d8_elems = [e, a, a2, a3, b, ab, a2b, a3b]
    d8_mats = [perm_matrix(g) for g in d8_elems]

    chi = [
        [1,  1,  1,  1,  1,  1,  1,  1],  # chi_1
        [1,  1,  1,  1, -1, -1, -1, -1],  # chi_2
        [1, -1,  1, -1,  1, -1,  1, -1],  # chi_3
        [1, -1,  1, -1, -1,  1, -1,  1],  # chi_4
        [2,  0, -2,  0,  0,  0,  0,  0],  # chi_5
    ]

    idemps = []
    for c in chi:
        deg = c[0]
        E = sum(c[k] * d8_mats[k] for k in range(8)) * (deg / 8.0)
        assert np.allclose(E @ E, E)
        idemps.append(E)
    assert np.allclose(sum(idemps), np.eye(4))

    v1 = np.array([1.0, 0.0, 0.0, 0.0])
    v2 = np.array([0.0, 1.0, 0.0, 0.0])
    assert np.allclose(v1 @ idemps[0], 0.25 * np.array([1, 1, 1, 1]))
    assert np.allclose(v1 @ idemps[1], np.zeros(4))
    assert np.allclose(v1 @ idemps[2], np.zeros(4))
    assert np.allclose(v1 @ idemps[3], 0.25 * np.array([1, -1, 1, -1]))
    assert np.allclose(v1 @ idemps[4], 0.5 * np.array([1, 0, -1, 0]))
    assert np.allclose(v2 @ idemps[4], 0.5 * np.array([0, 1, 0, -1]))

    fig, axes = plt.subplots(1, 4, figsize=(11.5, 4.0))

    corners = {
        1: (-0.62,  0.62),
        2: ( 0.62,  0.62),
        3: ( 0.62, -0.62),
        4: (-0.62, -0.62),
    }
    corner_label_offsets = {
        1: (-0.30,  0.26),
        2: ( 0.30,  0.26),
        3: ( 0.30, -0.28),
        4: (-0.30, -0.28),
    }

    modes = [
        ("(a) $Ve_1$ ($\\chi_1$, $\\dim 1$)",
         r"$v_1 + v_2 + v_3 + v_4$",
         [+1, +1, +1, +1],
         "Fixed by all $g \\in D_8$"),
        ("(b) $Ve_4$ ($\\chi_4$, $\\dim 1$)",
         r"$v_1 - v_2 + v_3 - v_4$",
         [+1, -1, +1, -1],
         "Fixed by $ab=(2\\,4)$,\n$a^3b=(1\\,3)$; negated by $a, b$"),
        ("(c) $Ve_5$ basis 1 ($\\chi_5$)",
         r"$v_1 - v_3$",
         [+1, 0, -1, 0],
         "Sent to $v_2 - v_4$ by $a$,\nnegated by $a^2=(1\\,3)(2\\,4)$"),
        ("(d) $Ve_5$ basis 2 ($\\chi_5$)",
         r"$v_2 - v_4$",
         [0, +1, 0, -1],
         "Sent to $-(v_1 - v_3)$ by $a$,\nnegated by $a^2=(1\\,3)(2\\,4)$"),
    ]

    for idx, (ax, (panel_title, formula, weights, note_text)) in enumerate(zip(axes, modes)):
        ax.set_aspect("equal")
        ax.set_xlim(-1.25, 1.25)
        ax.set_ylim(-1.58, 1.32)
        ax.axis("off")

        sq_x = [-0.62, 0.62, 0.62, -0.62, -0.62]
        sq_y = [ 0.62, 0.62, -0.62, -0.62, 0.62]
        ax.plot(sq_x, sq_y, color=DARK_GREY, lw=1.8, zorder=2)

        if idx == 1:
            ax.plot([-0.78, 0.78], [-0.78, 0.78], color=MID_GREY, ls=":", lw=1.2, zorder=1)
            ax.plot([-0.78, 0.78], [0.78, -0.78], color=MID_GREY, ls=":", lw=1.2, zorder=1)
            ax.text(0.0, 1.02, r"axes $ab=(2\,4)$, $a^3b=(1\,3)$", fontsize=8.8,
                    ha="center", va="center", color=MID_GREY)
        elif idx == 2:
            ax.plot([-0.62, 0.62], [0.62, -0.62], color=OI_BLUE, ls="--", lw=1.5, zorder=1)
        elif idx == 3:
            ax.plot([-0.62, 0.62], [-0.62, 0.62], color=OI_BLUE, ls="--", lw=1.5, zorder=1)

        for c_num, w in zip([1, 2, 3, 4], weights):
            cx, cy = corners[c_num]
            ox, oy = corner_label_offsets[c_num]
            ax.text(cx + ox, cy + oy, f"${c_num}$", fontsize=10.5, fontweight="bold",
                    ha="center", va="center", color=DARK_GREY)

            if w == 1:
                circ = Circle((cx, cy), 0.20, facecolor=OI_SKY, edgecolor=DARK_GREY, lw=1.8, zorder=4)
                ax.add_patch(circ)
                ax.text(cx, cy, "$+$", fontsize=13, fontweight="bold",
                        ha="center", va="center", color=DARK_GREY, zorder=5)
            elif w == -1:
                circ = Circle((cx, cy), 0.20, facecolor="white", edgecolor=OI_VERMILION, lw=2.5, zorder=4)
                ax.add_patch(circ)
                ax.text(cx, cy, "$-$", fontsize=14, fontweight="bold",
                        ha="center", va="center", color=DARK_GREY, zorder=5)
            else:
                circ = Circle((cx, cy), 0.12, facecolor=LIGHT_GREY, edgecolor=MID_GREY,
                              lw=1.2, ls="--", zorder=4)
                ax.add_patch(circ)
                ax.text(cx, cy, "$0$", fontsize=9.5, fontweight="bold",
                        ha="center", va="center", color=DARK_GREY, zorder=5)

        ax.set_title(panel_title, fontsize=10.5, fontweight="bold", pad=4, color=DARK_GREY)
        ax.text(0.0, -1.06, formula, fontsize=10.5, fontweight="bold",
                ha="center", va="center", color=DARK_GREY)
        ax.text(0.0, -1.39, note_text, fontsize=8.8,
                ha="center", va="center", color=MID_GREY)

    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.09, top=0.80, wspace=0.08)

    # Frame around panels (c) and (d) together
    pos_c = axes[2].get_position()
    pos_d = axes[3].get_position()
    frame_x0 = pos_c.x0 - 0.006
    frame_y0 = pos_c.y0 + 0.015
    frame_w = (pos_d.x1 + 0.006) - frame_x0
    frame_h = 0.875 - frame_y0
    ve5_frame = FancyBboxPatch(
        (frame_x0, frame_y0), frame_w, frame_h,
        boxstyle="round,pad=0.008,rounding_size=0.015",
        facecolor="none", edgecolor=OI_BLUE, lw=1.5,
        transform=fig.transFigure, zorder=3
    )
    fig.patches.append(ve5_frame)
    fig.text(
        frame_x0 + frame_w / 2.0, 0.935,
        r"(c) and (d): a basis of $Ve_5$, the $2$-dimensional irreducible submodule with character $\chi_5$",
        ha="center", va="center", fontsize=7.9, fontweight="bold", color=DARK_GREY,
        bbox=dict(boxstyle="round,pad=0.20", fc="#F0F7FC", ec=OI_BLUE, lw=1.2)
    )

    fig.text(0.50, 0.025,
             "Corner weight key:   filled circle (+) = +1     |     open thick-rimmed circle (\u2212) = \u22121     |     small dashed circle (0) = 0",
             ha="center", va="center", fontsize=9.5, color=DARK_GREY)

    path = os.path.join(out_dir, "maths2_rep_d8_square_modes.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved {path}")


# =============================================================================
# Figure 4: Restriction from S_5 to A_5 and 5-cycle class splitting
# =============================================================================
def make_figure_4(out_dir):
    # Recompute S_5 and A_5 character degrees, restriction, and alpha/beta
    s5_degrees = [1, 1, 4, 4, 6, 5, 5]
    assert sum(d**2 for d in s5_degrees) == 120

    a5_degrees = [1, 4, 5, 3, 3]
    assert sum(d**2 for d in a5_degrees) == 60

    alpha = 0.5 * (1.0 + math.sqrt(5.0))
    beta = 0.5 * (1.0 - math.sqrt(5.0))
    assert abs((alpha + beta) - 1.0) < 1e-12
    assert abs((alpha * beta) - (-1.0)) < 1e-12
    assert abs((alpha**2 + beta**2) - 3.0) < 1e-12
    assert abs(2.0 + 2.0 * alpha * beta) < 1e-12

    s5_all = list(itertools.permutations(range(5)))
    def sign_perm(p):
        inv_cnt = sum(1 for i in range(5) for j in range(i + 1, 5) if p[i] > p[j])
        return 1 if inv_cnt % 2 == 0 else -1
    a5_all = [p for p in s5_all if sign_perm(p) == 1]
    assert len(a5_all) == 60

    rep1 = (1, 2, 3, 4, 0)  # (1 2 3 4 5)
    rep2 = (2, 0, 3, 4, 1)  # (1 3 4 5 2) = (1 2)^{-1}(1 2 3 4 5)(1 2)
    t12 = (1, 0, 2, 3, 4)
    assert perm_compose(perm_compose(t12, rep1), t12) == rep2

    class_s5 = {perm_compose(perm_compose(perm_inv(g), rep1), g) for g in s5_all}
    class_a5_1 = {perm_compose(perm_compose(perm_inv(g), rep1), g) for g in a5_all}
    class_a5_2 = {perm_compose(perm_compose(perm_inv(g), rep2), g) for g in a5_all}
    assert len(class_s5) == 24
    assert len(class_a5_1) == 12
    assert len(class_a5_2) == 12
    assert class_a5_1.isdisjoint(class_a5_2)
    assert class_a5_1 | class_a5_2 == class_s5

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.6, 4.35),
                                   gridspec_kw={"width_ratios": [1.58, 1.0]})

    # --- Panel (a): Character restriction diagram S_5 -> A_5 ---
    ax1.set_xlim(-0.15, 10.65)
    ax1.set_ylim(0.0, 5.2)
    ax1.axis("off")
    ax1.set_title(r"(a) Restricting the $7$ irreducible characters of $S_5$ to $A_5$",
                  fontsize=11, fontweight="bold", pad=6, color=DARK_GREY)

    s5_nodes = [
        (0.75, 4.0, r"$\chi_1$", "deg $1$", OI_BLUE),
        (2.05, 4.0, r"$\chi_2 = \chi_1\lambda$", "deg $1$", OI_BLUE),
        (3.55, 4.0, r"$\chi_3$", "deg $4$", OI_GREEN),
        (4.85, 4.0, r"$\chi_4 = \chi_3\lambda$", "deg $4$", OI_GREEN),
        (6.35, 4.0, r"$\chi_6$", "deg $5$", OI_ORANGE),
        (7.65, 4.0, r"$\chi_7 = \chi_6\lambda$", "deg $5$", OI_ORANGE),
        (9.35, 4.0, r"$\chi_5 = \chi_5\lambda$", "deg $6$", OI_VERMILION),
    ]

    for x, y, lbl, sub, col in s5_nodes:
        box = FancyBboxPatch((x - 0.54, y - 0.42), 1.08, 0.84,
                             boxstyle="round,pad=0.05", facecolor="white",
                             edgecolor=col, lw=1.8, zorder=3)
        ax1.add_patch(box)
        ax1.text(x, y + 0.12, lbl, ha="center", va="center", fontsize=9.6, fontweight="bold", color=DARK_GREY)
        ax1.text(x, y - 0.20, sub, ha="center", va="center", fontsize=8.8, color=MID_GREY)

    a5_nodes = [
        (1.40, 1.15, r"$\psi_1$", "deg $1$", OI_BLUE),
        (4.20, 1.15, r"$\psi_2$", "deg $4$", OI_GREEN),
        (7.00, 1.15, r"$\psi_3$", "deg $5$", OI_ORANGE),
        (8.70, 1.15, r"$\psi_4$", "deg $3$", OI_VERMILION),
        (9.95, 1.15, r"$\psi_5$", "deg $3$", OI_VERMILION),
    ]
    for x, y, lbl, sub, col in a5_nodes:
        box = FancyBboxPatch((x - 0.48, y - 0.42), 0.96, 0.84,
                             boxstyle="round,pad=0.05", facecolor="#FAFAFA",
                             edgecolor=col, lw=2.0, zorder=3)
        ax1.add_patch(box)
        ax1.text(x, y + 0.12, lbl, ha="center", va="center", fontsize=10.5, fontweight="bold", color=DARK_GREY)
        ax1.text(x, y - 0.20, sub, ha="center", va="center", fontsize=8.8, color=MID_GREY)

    merge_arrows = [
        (0.75, 3.55, 1.30, 1.60, OI_BLUE),
        (2.05, 3.55, 1.50, 1.60, OI_BLUE),
        (3.55, 3.55, 4.10, 1.60, OI_GREEN),
        (4.85, 3.55, 4.30, 1.60, OI_GREEN),
        (6.35, 3.55, 6.90, 1.60, OI_ORANGE),
        (7.65, 3.55, 7.10, 1.60, OI_ORANGE),
    ]
    for x0, y0, x1, y1, col in merge_arrows:
        ax1.annotate("", xy=(x1, y1), xytext=(x0, y0),
                     arrowprops=dict(arrowstyle="->,head_width=0.22,head_length=0.28",
                                     color=col, lw=1.8))

    for x1 in [8.70, 9.95]:
        ax1.annotate("", xy=(x1, 1.60), xytext=(9.35, 3.55),
                     arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.30",
                                     color=OI_VERMILION, lw=2.1))

    ax1.text(4.20, 2.55, r"$\chi(g) \neq 0$ for some $g \notin A_5$:" + "\n" + r"pairs $\{\chi, \chi\lambda\}$ merge ($\chi\downarrow A_5$ irreducible)",
             ha="center", va="center", fontsize=9.1, color=DARK_GREY,
             bbox=dict(boxstyle="round,pad=0.22", fc="#F4F8FB", ec="#B0C8DE", lw=1.0))
    ax1.text(9.35, 2.55, r"$\chi_5 = 0$ outside $A_5$:" + "\n" + r"splits as $\psi_4 + \psi_5$",
             ha="center", va="center", fontsize=9.1, color=DARK_GREY, fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.22", fc="#FFF5F0", ec=OI_VERMILION, lw=1.1))

    ax1.text(0.10, 4.72, r"$\mathbf{S_5}$ ($|S_5|=120$):", fontsize=10, fontweight="bold", color=DARK_GREY)
    ax1.text(0.10, 0.32, r"$\mathbf{A_5}$ ($|A_5|=60$):", fontsize=10, fontweight="bold", color=DARK_GREY)

    # --- Panel (b): Splitting of the 5-cycle conjugacy class and the (alpha, beta) block ---
    ax2.set_xlim(0.0, 6.0)
    ax2.set_ylim(0.0, 5.2)
    ax2.axis("off")
    ax2.set_title(r"(b) Splitting of the $5$-cycle class in $A_5$",
                  fontsize=11, fontweight="bold", pad=6, color=DARK_GREY)

    top_box = FancyBboxPatch((0.8, 3.75), 4.4, 0.95, boxstyle="round,pad=0.08",
                             facecolor="#F4F8FB", edgecolor=OI_BLUE, lw=1.8)
    ax2.add_patch(top_box)
    ax2.text(3.0, 4.38, r"Single $S_5$-class $(1\,2\,3\,4\,5)^{S_5}$ (size $24$)",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=DARK_GREY)
    ax2.text(3.0, 4.00, r"No odd permutation commutes with $(1\,2\,3\,4\,5)$",
             ha="center", va="center", fontsize=8.8, color=MID_GREY)

    ax2.annotate("", xy=(1.65, 2.95), xytext=(2.4, 3.72),
                 arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.30", color=OI_BLUE, lw=1.8))
    ax2.annotate("", xy=(4.35, 2.95), xytext=(3.6, 3.72),
                 arrowprops=dict(arrowstyle="->,head_width=0.24,head_length=0.30", color=OI_BLUE, lw=1.8))

    for cx, rep_str in [(1.65, r"$(1\,2\,3\,4\,5)^{A_5}$"), (4.35, r"$(1\,3\,4\,5\,2)^{A_5}$")]:
        cbox = FancyBboxPatch((cx - 1.18, 2.10), 2.36, 0.80, boxstyle="round,pad=0.06",
                              facecolor="white", edgecolor=OI_BLUE, lw=1.6)
        ax2.add_patch(cbox)
        ax2.text(cx, 2.62, rep_str, ha="center", va="center", fontsize=9.8, fontweight="bold", color=DARK_GREY)
        ax2.text(cx, 2.28, r"size $12$, $|C_{A_5}(g)| = 5$", ha="center", va="center", fontsize=8.6, color=MID_GREY)

    tbl_box = FancyBboxPatch((0.45, 0.25), 5.10, 1.55, boxstyle="round,pad=0.06",
                             facecolor="#FFF9F5", edgecolor=OI_VERMILION, lw=1.5)
    ax2.add_patch(tbl_box)
    ax2.plot([0.45, 5.55], [1.28, 1.28], color=OI_VERMILION, lw=1.0)
    ax2.plot([0.45, 5.55], [0.78, 0.78], color="#E0C0B0", lw=0.9)
    ax2.plot([1.85, 1.85], [0.25, 1.80], color=OI_VERMILION, lw=1.0)
    ax2.plot([3.70, 3.70], [0.25, 1.80], color="#E0C0B0", lw=0.9)

    ax2.text(1.15, 1.53, "Character", ha="center", va="center", fontsize=9.2, fontweight="bold", color=DARK_GREY)
    ax2.text(2.77, 1.53, r"on $(1\,2\,3\,4\,5)$", ha="center", va="center", fontsize=9.2, fontweight="bold", color=DARK_GREY)
    ax2.text(4.62, 1.53, r"on $(1\,3\,4\,5\,2)$", ha="center", va="center", fontsize=9.2, fontweight="bold", color=DARK_GREY)

    ax2.text(1.15, 1.03, r"$\psi_4$ (deg $3$)", ha="center", va="center", fontsize=9.5, fontweight="bold", color=DARK_GREY)
    ax2.text(2.77, 1.03, r"$\alpha = \frac{1+\sqrt{5}}{2}$", ha="center", va="center", fontsize=9.5, fontweight="bold", color=DARK_GREY)
    ax2.text(4.62, 1.03, r"$\beta = \frac{1-\sqrt{5}}{2}$", ha="center", va="center", fontsize=9.5, fontweight="bold", color=DARK_GREY)

    ax2.text(1.15, 0.52, r"$\psi_5$ (deg $3$)", ha="center", va="center", fontsize=9.5, fontweight="bold", color=DARK_GREY)
    ax2.text(2.77, 0.52, r"$\beta = \frac{1-\sqrt{5}}{2}$", ha="center", va="center", fontsize=9.5, fontweight="bold", color=DARK_GREY)
    ax2.text(4.62, 0.52, r"$\alpha = \frac{1+\sqrt{5}}{2}$", ha="center", va="center", fontsize=9.5, fontweight="bold", color=DARK_GREY)

    fig.subplots_adjust(left=0.015, right=0.985, bottom=0.04, top=0.88, wspace=0.06)
    path = os.path.join(out_dir, "maths2_rep_s5_a5_restriction.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved {path}")


# =============================================================================
# Figure 5: Orbital grids for S_4 on points (4x4) and on 2-subsets (6x6)
# =============================================================================
def make_figure_5(out_dir):
    # Brute-force orbit calculation over S_4
    s4_perms = list(itertools.permutations(range(4)))
    assert len(s4_perms) == 24

    pts = list(range(4))
    pairs_pts = [(i, j) for i in pts for j in pts]
    visited = set()
    orbits_pts = []
    for p in pairs_pts:
        if p not in visited:
            orb = {(g[p[0]], g[p[1]]) for g in s4_perms}
            orbits_pts.append(orb)
            visited |= orb
    assert len(orbits_pts) == 2
    orb_sizes_pts = sorted(len(o) for o in orbits_pts)
    assert orb_sizes_pts == [4, 12]

    subsets_2 = list(itertools.combinations(range(4), 2))
    assert len(subsets_2) == 6
    pairs_sub = [(A, B) for A in subsets_2 for B in subsets_2]
    visited_sub = set()
    orbits_sub = []
    for pair in pairs_sub:
        if pair not in visited_sub:
            A, B = pair
            orb = {
                (tuple(sorted((g[A[0]], g[A[1]]))), tuple(sorted((g[B[0]], g[B[1]]))))
                for g in s4_perms
            }
            orbits_sub.append(orb)
            visited_sub |= orb
    assert len(orbits_sub) == 3

    counts_by_inter = {2: 0, 1: 0, 0: 0}
    for A, B in pairs_sub:
        s = len(set(A) & set(B))
        counts_by_inter[s] += 1
    assert counts_by_inter == {2: 6, 1: 24, 0: 6}

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.4, 5.2),
                                   gridspec_kw={"width_ratios": [1.0, 1.0]})

    badge = dict(boxstyle="round,pad=0.14", fc="white", ec="none", alpha=0.88)

    # --- Panel (a): 4x4 grid of ordered pairs of points of {1, 2, 3, 4} ---
    ax1.set_aspect("equal")
    ax1.set_xlim(0, 4)
    ax1.set_ylim(0, 4)
    ax1.invert_yaxis()

    for r in range(4):
        for c in range(4):
            if r == c:
                fc, hatch, sym = OI_SKY, "//", "D"
            else:
                fc, hatch, sym = "#FBE3B5", "", "O"
            rect = Rectangle((c, r), 1, 1, facecolor=fc, edgecolor=DARK_GREY, lw=1.3, hatch=hatch)
            ax1.add_patch(rect)
            ax1.text(c + 0.5, r + 0.5, sym, ha="center", va="center",
                     fontsize=11, fontweight="bold", color=DARK_GREY, bbox=badge)

    ax1.set_xticks([0.5, 1.5, 2.5, 3.5])
    ax1.set_xticklabels(["1", "2", "3", "4"], fontsize=10.5, fontweight="bold")
    ax1.set_yticks([0.5, 1.5, 2.5, 3.5])
    ax1.set_yticklabels(["1", "2", "3", "4"], fontsize=10.5, fontweight="bold")
    ax1.xaxis.tick_top()
    ax1.tick_params(length=0)
    ax1.set_title(r"(a) $\Omega \times \Omega$ for $\Omega = \{1,2,3,4\}$ (rank $2$)",
                  fontsize=11, fontweight="bold", y=1.14, pad=0, color=DARK_GREY)

    leg_a = [
        mpatches.Patch(facecolor=OI_SKY, edgecolor=DARK_GREY, hatch="//",
                       label=r"D: diagonal $\Delta$ ($\alpha = \beta$, $4$ cells)"),
        mpatches.Patch(facecolor="#FBE3B5", edgecolor=DARK_GREY,
                       label=r"O: off-diagonal ($\alpha \neq \beta$, $12$ cells)"),
    ]
    ax1.legend(handles=leg_a, loc="upper center", bbox_to_anchor=(0.5, -0.05),
               frameon=True, fontsize=9.2, ncol=1)

    # --- Panel (b): 6x6 grid of ordered pairs of 2-subsets of {1, 2, 3, 4} ---
    ax2.set_aspect("equal")
    ax2.set_xlim(0, 6)
    ax2.set_ylim(0, 6)
    ax2.invert_yaxis()

    sub_labels = [f"{{{a+1},{b+1}}}" for a, b in subsets_2]
    for r, A in enumerate(subsets_2):
        for c, B in enumerate(subsets_2):
            inter_sz = len(set(A) & set(B))
            if inter_sz == 2:
                fc, hatch, sym = OI_SKY, "//", "2"
            elif inter_sz == 1:
                fc, hatch, sym = "#FBE3B5", "", "1"
            else:
                fc, hatch, sym = "#A8E0CE", "\\\\", "0"
            rect = Rectangle((c, r), 1, 1, facecolor=fc, edgecolor=DARK_GREY, lw=1.2, hatch=hatch)
            ax2.add_patch(rect)
            ax2.text(c + 0.5, r + 0.5, sym, ha="center", va="center",
                     fontsize=10.5, fontweight="bold", color=DARK_GREY, bbox=badge)

    ax2.set_xticks([i + 0.5 for i in range(6)])
    ax2.set_xticklabels(sub_labels, fontsize=9.2, fontweight="bold", rotation=28, ha="left")
    ax2.set_yticks([i + 0.5 for i in range(6)])
    ax2.set_yticklabels(sub_labels, fontsize=9.2, fontweight="bold")
    ax2.xaxis.tick_top()
    ax2.tick_params(length=0)
    ax2.set_title(r"(b) $I_2 \times I_2$ for $2$-subsets of $\{1,2,3,4\}$ (rank $3$)",
                  fontsize=11, fontweight="bold", y=1.14, pad=0, color=DARK_GREY)

    leg_b = [
        mpatches.Patch(facecolor=OI_SKY, edgecolor=DARK_GREY, hatch="//",
                       label=r"2: $\Delta$ ($|A \cap B| = 2$, $6$ cells)"),
        mpatches.Patch(facecolor="#FBE3B5", edgecolor=DARK_GREY,
                       label=r"1: $\Delta_1$ ($|A \cap B| = 1$, $24$ cells)"),
        mpatches.Patch(facecolor="#A8E0CE", edgecolor=DARK_GREY, hatch="\\\\",
                       label=r"0: $\Delta_2$ ($|A \cap B| = 0$, $6$ cells)"),
    ]
    ax2.legend(handles=leg_b, loc="upper center", bbox_to_anchor=(0.5, -0.04),
               frameon=True, fontsize=9.0, ncol=1)

    fig.subplots_adjust(left=0.05, right=0.98, bottom=0.22, top=0.80, wspace=0.22)
    path = os.path.join(out_dir, "maths2_rep_orbital_grids.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved {path}")


# =============================================================================
# Figure 6: S_6 k-subset staircase and 4-region subset intersection diagram
# =============================================================================
def make_figure_6(out_dir):
    # Recompute binomial coefficients and character degrees for S_6 (n = 6)
    n = 6
    pi_degs = [math.comb(n, k) for k in range(4)]
    assert pi_degs == [1, 6, 15, 20]
    chi_degs = [pi_degs[0]] + [pi_degs[k] - pi_degs[k - 1] for k in range(1, 4)]
    assert chi_degs == [1, 5, 9, 5]
    for k in range(4):
        assert sum(chi_degs[: k + 1]) == pi_degs[k]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.35),
                                   gridspec_kw={"width_ratios": [1.45, 1.0]})

    # --- Panel (a): Stacked horizontal bar staircase for pi_0, pi_1, pi_2, pi_3 of S_6 ---
    ax1.set_xlim(0, 23.8)
    ax1.set_ylim(-0.65, 3.8)
    ax1.invert_yaxis()

    block_labels = [
        r"$\chi^{(6)}$ ($1$)",
        r"$\chi^{(5,1)}$ ($5$)",
        r"$\chi^{(4,2)}$ ($9$)",
        r"$\chi^{(3,3)}$ ($5$)",
    ]
    # Softer Okabe-Ito tints so dark grey text has high contrast inside every block
    block_colors = ["#8CC5E3", OI_SKY, "#F3BA4A", "#68C4A8"]
    bar_labels = [
        r"$\pi_0 = 1_{S_6}$",
        r"$\pi_1$ ($1$-subsets)",
        r"$\pi_2$ ($2$-subsets)",
        r"$\pi_3$ ($3$-subsets)",
    ]

    bar_h = 0.62
    for row_k in range(4):
        left = 0.0
        for j in range(row_k + 1):
            w = chi_degs[j]
            is_new = (j == row_k)
            rect = Rectangle((left, row_k - bar_h / 2), w, bar_h,
                             facecolor=block_colors[j],
                             edgecolor=DARK_GREY,
                             lw=2.1 if is_new else 1.2,
                             alpha=1.0 if is_new else 0.72)
            ax1.add_patch(rect)
            if w == 1:
                ax1.text(left + w / 2, row_k, "$1$", ha="center", va="center",
                         fontsize=9.5, fontweight="bold", color=DARK_GREY)
            else:
                ax1.text(left + w / 2, row_k, block_labels[j], ha="center", va="center",
                         fontsize=9.8, fontweight="bold", color=DARK_GREY)
            left += w

        ax1.text(left + 0.45, row_k, f"$\\binom{{6}}{{{row_k}}} = {pi_degs[row_k]}$",
                 ha="left", va="center", fontsize=10, fontweight="bold", color=DARK_GREY)

        if row_k > 0:
            prev_len = pi_degs[row_k - 1]
            ax1.plot([prev_len, prev_len], [row_k - 1 + bar_h / 2, row_k - bar_h / 2],
                     color=OI_VERMILION, ls="--", lw=1.6)

    ax1.annotate(r"$\chi^{(6)}$ (deg $1$)", xy=(0.5, -bar_h / 2), xytext=(2.4, -0.45),
                 arrowprops=dict(arrowstyle="->", color=OI_BLUE, lw=1.5),
                 fontsize=9.5, fontweight="bold", color=DARK_GREY, va="center")

    ax1.set_yticks([0, 1, 2, 3])
    ax1.set_yticklabels(bar_labels, fontsize=10, fontweight="bold")
    ax1.set_xlabel(r"Character degree at $1 \in S_6$ (number of $k$-subsets)", fontsize=10)
    ax1.set_title(r"(a) Staircase decomposition $\pi_k = \sum_{i=0}^k \chi^{(6-i,i)}$ in $S_6$",
                  fontsize=11, fontweight="bold", pad=10, color=DARK_GREY)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # --- Panel (b): Four disjoint regions of I = {1, ..., n} for (A, B) in I_k x I_l ---
    ax2.set_aspect("equal")
    ax2.set_xlim(0.0, 6.2)
    ax2.set_ylim(0.0, 4.4)
    ax2.axis("off")
    ax2.set_title(r"(b) Orbit invariant $s = |A \cap B|$ on $I_k \times I_l$",
                  fontsize=11, fontweight="bold", pad=10, color=DARK_GREY)

    outer = FancyBboxPatch((0.20, 0.20), 5.80, 3.85, boxstyle="round,pad=0.08",
                           facecolor="#F7F7F7", edgecolor=DARK_GREY, lw=1.8)
    ax2.add_patch(outer)
    ax2.text(0.42, 3.80, r"$I = \{1, \dots, n\}$", fontsize=10, fontweight="bold", color=DARK_GREY)

    cA = Circle((2.35, 1.98), 1.18, facecolor=OI_SKY, alpha=0.35, edgecolor=OI_BLUE, lw=2.0)
    cB = Circle((3.85, 1.98), 1.12, facecolor=OI_ORANGE, alpha=0.35, edgecolor=OI_VERMILION, lw=2.0)
    ax2.add_patch(cA)
    ax2.add_patch(cB)
    ax2.add_patch(Circle((2.35, 1.98), 1.18, facecolor="none", edgecolor=OI_BLUE, lw=2.0))
    ax2.add_patch(Circle((3.85, 1.98), 1.12, facecolor="none", edgecolor=OI_VERMILION, lw=2.0))

    ax2.text(2.15, 3.36, r"$A \in I_k$ ($|A|=k$)", ha="center", va="center",
             fontsize=9.8, fontweight="bold", color=DARK_GREY)
    ax2.text(4.15, 3.36, r"$B \in I_l$ ($|B|=l$)", ha="center", va="center",
             fontsize=9.8, fontweight="bold", color=DARK_GREY)

    ax2.text(1.70, 1.98, r"$A \setminus B$" + "\n" + r"size $k - s$",
             ha="center", va="center", fontsize=9.6, fontweight="bold", color=DARK_GREY)
    ax2.text(3.14, 1.98, r"$A \cap B$" + "\n" + r"size $s$",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=DARK_GREY)
    ax2.text(4.45, 1.98, r"$B \setminus A$" + "\n" + r"size $l - s$",
             ha="center", va="center", fontsize=9.6, fontweight="bold", color=DARK_GREY)
    ax2.text(3.10, 0.48, r"$I \setminus (A \cup B)$:  size $n - k - l + s$",
             ha="center", va="center", fontsize=9.6, fontweight="bold", color=DARK_GREY)

    fig.subplots_adjust(left=0.14, right=0.985, bottom=0.14, top=0.83, wspace=0.14)
    path = os.path.join(out_dir, "maths2_rep_sn_ksubset_staircase.png")
    fig.savefig(path)
    plt.close(fig)
    print(f"Saved {path}")


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    make_figure_1(out_dir)
    make_figure_2(out_dir)
    make_figure_3(out_dir)
    make_figure_4(out_dir)
    make_figure_5(out_dir)
    make_figure_6(out_dir)
    print("ALL 6 FIGURES GENERATED AND VERIFIED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
