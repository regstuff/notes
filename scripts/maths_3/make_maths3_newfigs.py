#!/usr/bin/env python3
"""Generate the nine settled new figures for 'Maths 3 - Projective Geometry'.

Usage:
    /home/ubuntu/.claude/skills/lecture-notes/.venv/bin/python \
        make_maths3_newfigs.py <output_dir>
"""

from __future__ import annotations

import itertools
import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon
import numpy as np


# ---------------------------------------------------------------------------
# Consistent visual palette & typography (matched to make_maths3_figures.py)
# ---------------------------------------------------------------------------
NAVY = "#1e3a8a"        # Points of the geometry / active node outlines
BLUE = "#2563eb"        # Lines of the geometry / subspace slices
BLUE_LIGHT = "#dbeafe"  # Soft blue node/plane fill
BLUE_PALE = "#eff6ff"   # Very pale blue card background
TEAL = "#0f766e"        # Quadric surface / second subspace or regulus family
TEAL_LIGHT = "#ccfbf1"  # Soft teal fill
AMBER = "#d97706"       # Distinguished element (pole, vertex, nucleus) / tangent or polar plane
AMBER_LIGHT = "#fef3c7" # Soft amber highlight fill
RED = "#dc2626"         # Non-isotropic / ambient secant / non-intersection
RED_LIGHT = "#fee2e2"   # Soft red warning fill
SLATE = "#64748b"       # Ambient rays / secondary lines / annotations
GREY_LINE = "#cbd5e1"   # Subtle borders / wireframe background
GREY_BG = "#f8fafc"     # Subtle inset panel background
TEXT = "#0f172a"        # Primary dark label text

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "mathtext.fontset": "cm",
    "axes.edgecolor": GREY_LINE,
})


# ---------------------------------------------------------------------------
# Shared helper primitives
# ---------------------------------------------------------------------------
def setup_canvas(width: float, height: float, xlim=(0, 10), ylim=(0, 6)):
    fig, ax = plt.subplots(figsize=(width, height), dpi=220)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    ax.axis("off")
    return fig, ax


def draw_card(ax, x: float, y: float, w: float, h: float,
              fc: str = GREY_BG, ec: str = GREY_LINE, lw: float = 1.1,
              pad: float = 0.08, rounding: float = 0.14, alpha: float = 1.0,
              ls: str = "-", zorder: int = 0):
    box = FancyBboxPatch(
        (x + pad, y + pad), w - 2 * pad, h - 2 * pad,
        boxstyle=f"round,pad={pad},rounding_size={rounding}",
        facecolor=fc, edgecolor=ec, linewidth=lw, linestyle=ls,
        alpha=alpha, zorder=zorder
    )
    ax.add_patch(box)
    return box


def seg_intersection_2d(p1, p2, q1, q2):
    """Exact intersection of 2D lines p1-p2 and q1-q2, returning (x, y, t, u)."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = q1
    x4, y4 = q2
    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(den) < 1e-12:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / den
    return (x1 + t * (x2 - x1), y1 + t * (y2 - y1), t, u)


def save_fig(fig, out_dir: Path, filename: str):
    out_path = out_dir / filename
    fig.savefig(out_path, dpi=220, bbox_inches="tight", pad_inches=0.14)
    plt.close(fig)
    print(f"  [saved] {out_path}")


# ---------------------------------------------------------------------------
# Figure 1: Fano Plane (maths3_axioms_fano.png)
# ---------------------------------------------------------------------------
def make_fig1_fano(out_dir: Path):
    # Seven triples from line 79 of the notes
    fano_lines = [
        {1, 2, 3}, {1, 4, 5}, {1, 6, 7},
        {2, 4, 7}, {2, 5, 6}, {3, 4, 6}, {3, 5, 7},
    ]
    pts = sorted(set().union(*fano_lines))
    q = 2
    assert pts == [1, 2, 3, 4, 5, 6, 7]
    assert len(pts) == q * q + q + 1 == 7
    assert len(fano_lines) == q * q + q + 1 == 7
    for L in fano_lines:
        assert len(L) == q + 1 == 3
    for p in pts:
        assert sum(1 for L in fano_lines if p in L) == q + 1 == 3
    for a, b in itertools.combinations(pts, 2):
        containing = [L for L in fano_lines if a in L and b in L]
        assert len(containing) == 1
    for L1, L2 in itertools.combinations(fano_lines, 2):
        assert len(L1 & L2) == 1

    # Triangle-and-incircle coordinates centred at (0, 0)
    R = 2.15
    pos = {
        1: np.array([0.0, 0.0]),
        2: R * np.array([math.cos(math.radians(90.0)), math.sin(math.radians(90.0))]),
        4: R * np.array([math.cos(math.radians(210.0)), math.sin(math.radians(210.0))]),
        6: R * np.array([math.cos(math.radians(330.0)), math.sin(math.radians(330.0))]),
    }
    pos[3] = 0.5 * (pos[4] + pos[6])
    pos[5] = 0.5 * (pos[2] + pos[6])
    pos[7] = 0.5 * (pos[2] + pos[4])

    # Verify collinearity of the 6 straight triples and circularity of {3, 5, 7}
    r_in = R * 0.5
    circle_line = {3, 5, 7}
    for L in fano_lines:
        if L == circle_line:
            for p in L:
                assert abs(np.linalg.norm(pos[p]) - r_in) < 1e-12
            for p in set(pts) - L:
                assert abs(np.linalg.norm(pos[p]) - r_in) > 0.4
        else:
            p_list = sorted(L)
            v1 = pos[p_list[1]] - pos[p_list[0]]
            v2 = pos[p_list[2]] - pos[p_list[0]]
            cross = abs(v1[0] * v2[1] - v1[1] * v2[0])
            assert cross < 1e-12, f"Non-collinear triple {L}"
            for other in set(pts) - L:
                vo = pos[other] - pos[p_list[0]]
                assert abs(v1[0] * vo[1] - v1[1] * vo[0]) > 0.5

    fig, ax = setup_canvas(9.8, 5.2, xlim=(-2.75, 6.95), ylim=(-1.95, 2.95))
    draw_card(ax, -2.65, -1.85, 9.50, 4.70, fc=GREY_BG, ec=GREY_LINE)

    # Shift Fano centre slightly left inside card
    offset = np.array([-0.15, 0.25])
    P = {k: v + offset for k, v in pos.items()}

    # 1. Draw the two non-highlighted outer sides {2, 4, 7} and {2, 5, 6}
    for a, b in [(2, 4), (2, 6)]:
        ax.plot([P[a][0], P[b][0]], [P[a][1], P[b][1]],
                color=SLATE, lw=2.3, zorder=2)

    # 2. Draw the inscribed circle {3, 5, 7} in TEAL
    th = np.linspace(0, 2 * np.pi, 360)
    ax.plot(offset[0] + r_in * np.cos(th), offset[1] + r_in * np.sin(th),
            color=TEAL, lw=2.6, zorder=3)

    # White overpass halos where medians cross the circle at non-points (90, 210, 330 deg)
    for ang_deg in (90.0, 210.0, 330.0):
        cx = offset[0] + r_in * math.cos(math.radians(ang_deg))
        cy = offset[1] + r_in * math.sin(math.radians(ang_deg))
        gap = Circle((cx, cy), 0.105, facecolor=GREY_BG, edgecolor="none", zorder=4)
        ax.add_patch(gap)

    # 3. Highlighted point 1's three concurrent lines {1,2,3}, {1,4,5}, {1,6,7} in AMBER
    for corner, mid in [(2, 3), (4, 5), (6, 7)]:
        ax.plot([P[corner][0], P[mid][0]], [P[corner][1], P[mid][1]],
                color=AMBER, lw=3.2, zorder=5)

    # 4. Highlighted line {3, 4, 6} in bold BLUE
    ax.plot([P[4][0], P[6][0]], [P[4][1], P[6][1]],
            color=BLUE, lw=3.8, zorder=6)

    # 5. Draw the 7 point nodes
    r_node = 0.22
    # Soft amber halo around point 1
    ax.add_patch(Circle(P[1], r_node + 0.10, facecolor=AMBER_LIGHT,
                        edgecolor=AMBER, lw=1.2, ls="--", zorder=7))
    for k in pts:
        if k == 1:
            fc, ec, txt_c, lw_n = AMBER, NAVY, "white", 2.2
        elif k in {3, 4, 6}:
            # Outer blue highlight ring for the 3 collinear points on {3, 4, 6}
            ax.add_patch(Circle(P[k], r_node + 0.085, facecolor=BLUE_LIGHT,
                                edgecolor=BLUE, lw=1.8, zorder=7))
            fc, ec, txt_c, lw_n = NAVY, "white", "white", 1.5
        else:
            fc, ec, txt_c, lw_n = NAVY, "white", "white", 1.5
        ax.add_patch(Circle(P[k], r_node, facecolor=fc, edgecolor=ec,
                            lw=lw_n, zorder=8))
        ax.text(P[k][0], P[k][1], str(k), ha="center", va="center",
                fontsize=12.0, fontweight="bold", color=txt_c, zorder=9)

    ax.text(offset[0], -1.48,
            r"Line $\{3, 4, 6\}$ ($q + 1 = 3$ collinear points)",
            ha="center", va="center", fontsize=9.8, fontweight="bold", color=BLUE)

    # Right-hand explanation & duality summary box
    kx, ky, kw, kh = 2.15, -1.55, 4.45, 4.10
    draw_card(ax, kx, ky, kw, kh, fc="white", ec=GREY_LINE, lw=1.0, zorder=2)

    ax.text(kx + 0.25, ky + kh - 0.38,
            r"Fano Plane ($\mathrm{order}\ q = 2$)",
            ha="left", va="center", fontsize=11.5, fontweight="bold", color=TEXT)
    ax.text(kx + 0.25, ky + kh - 0.78,
            r"$N_2 = q^2 + q + 1 = 7$ points,  $7$ lines",
            ha="left", va="center", fontsize=10.0, color=TEXT)

    # Amber highlight legend item
    ax.plot([kx + 0.28, kx + 0.78], [ky + kh - 1.32, ky + kh - 1.32],
            color=AMBER, lw=3.2)
    ax.add_patch(Circle((kx + 0.53, ky + kh - 1.32), 0.11, facecolor=AMBER,
                        edgecolor=NAVY, lw=1.3, zorder=5))
    ax.text(kx + 0.95, ky + kh - 1.32,
            "Point $1$ and its $q + 1 = 3$\n"
            r"concurrent lines: $\{1,2,3\}$, $\{1,4,5\}$, $\{1,6,7\}$",
            ha="left", va="center", fontsize=9.2, color=TEXT)

    # Blue highlight legend item
    ax.plot([kx + 0.28, kx + 0.78], [ky + kh - 2.08, ky + kh - 2.08],
            color=BLUE, lw=3.6)
    ax.add_patch(Circle((kx + 0.53, ky + kh - 2.08), 0.11, facecolor=NAVY,
                        edgecolor=BLUE, lw=1.8, zorder=5))
    ax.text(kx + 0.95, ky + kh - 2.08,
            r"Line $\{3,4,6\}$ and its $q + 1 = 3$" "\n"
            "collinear points: $3$, $4$, $6$",
            ha="left", va="center", fontsize=9.2, color=TEXT)

    # Remaining lines item
    ax.plot([kx + 0.28, kx + 0.78], [ky + kh - 2.82, ky + kh - 2.82],
            color=SLATE, lw=2.3)
    ax.text(kx + 0.95, ky + kh - 2.82,
            r"Outer sides: $\{2,4,7\}$ and $\{2,5,6\}$",
            ha="left", va="center", fontsize=9.2, color=TEXT)

    # Circle line item
    ax.plot([kx + 0.28, kx + 0.78], [ky + kh - 3.42, ky + kh - 3.42],
            color=TEAL, lw=2.6)
    ax.text(kx + 0.95, ky + kh - 3.42,
            r"7th line $\{3,5,7\}$ (drawn as a circle;" "\n"
            "white gaps are not points)",
            ha="left", va="center", fontsize=9.1, color=TEAL)

    save_fig(fig, out_dir, "maths3_axioms_fano.png")


# ---------------------------------------------------------------------------
# Figure 2: Affine Slice vs Projective Subspaces (maths3_affine_slice.png)
# ---------------------------------------------------------------------------
def make_fig2_affine_slice(out_dir: Path):
    # Concrete vectors in F^3 with coordinates (x_0, x_1, x_2)
    origin = np.array([0.0, 0.0, 0.0])
    e0 = np.array([1.0, 0.0, 0.0])           # affine origin [1 : 0 : 0]
    v_dir = np.array([0.0, 1.0, 0.36])       # direction ray in H_0 (x_0 = 0)
    u_pt = np.array([1.0, -0.25, 0.98])      # shifted point [1 : u_1 : u_2] on x_0 = 1
    a_pt = np.array([1.0, 1.05, -0.82])      # sample projective ray point on x_0 = 1

    # Plane normals in (x_0, x_1, x_2)
    n1 = np.cross(e0, v_dir)   # W_1 = span(e0, v_dir)
    n2 = np.cross(u_pt, v_dir) # W_2 = span(u_pt, v_dir)
    assert abs(np.dot(n1, e0)) < 1e-12
    assert abs(np.dot(n2, e0)) > 0.5         # W_2 misses [1:0:0]
    assert abs(np.dot(n1, v_dir)) < 1e-12
    assert abs(np.dot(n2, v_dir)) < 1e-12
    inter_dir = np.cross(n1, n2)
    # W_1 cap W_2 is parallel to v_dir inside x_0 = 0
    assert np.linalg.norm(np.cross(inter_dir, v_dir)) < 1e-12
    assert abs(inter_dir[0]) < 1e-12

    # Check affine slices at x_0 = 1 are parallel lines missing each other
    for t in np.linspace(-1.5, 1.5, 15):
        p_sub = e0 + t * v_dir
        p_cos = u_pt + t * v_dir
        assert abs(p_sub[0] - 1.0) < 1e-12 and abs(np.dot(n1, p_sub)) < 1e-12
        assert abs(p_cos[0] - 1.0) < 1e-12 and abs(np.dot(n2, p_cos)) < 1e-12

    # Oblique 3D-to-2D projection: x_1 right-forward, x_2 back-right, x_0 vertical
    def proj(pt3):
        x0, x1, x2 = pt3
        px = 0.88 * x1 + 0.44 * x2
        py = 1.48 * x0 + 0.30 * x2 - 0.14 * x1
        return np.array([px, py])

    fig = plt.figure(figsize=(11.2, 5.3), dpi=220)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.25, 1.0], wspace=0.06)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.axis("off")

    # ---------------- Panel (a): 3D vector space F^3 ----------------
    ax1.set_xlim(-2.50, 2.80)
    ax1.set_ylim(-1.15, 3.25)
    draw_card(ax1, -2.45, -1.08, 5.20, 4.25, fc=GREY_BG, ec=GREY_LINE)
    ax1.text(0.15, 2.88,
             r"(a) Vector Space $\mathbb{F}^3$: Planes Through $\mathbf{0}=(0,0,0)$",
             ha="center", va="center", fontsize=10.2, fontweight="bold", color=TEXT)

    # Plane sheet bounds in (x_1, x_2)
    s1_min, s1_max = -1.55, 1.65
    s2_min, s2_max = -1.15, 1.55

    def sheet_poly(x0_val):
        corners = [
            (x0_val, s1_min, s2_min),
            (x0_val, s1_max, s2_min),
            (x0_val, s1_max, s2_max),
            (x0_val, s1_min, s2_max),
        ]
        return np.array([proj(c) for c in corners])

    # 1. Hyperplane at infinity H_0 (x_0 = 0)
    poly_h0 = sheet_poly(0.0)
    ax1.add_patch(Polygon(poly_h0, closed=True, facecolor=AMBER_LIGHT,
                          edgecolor=AMBER, lw=1.4, alpha=0.48, zorder=1))
    ax1.text(-2.12, -0.68, r"$H_0 : x_0 = 0$" "\n(at infinity)",
             ha="left", va="center", fontsize=9.1, fontweight="bold", color=AMBER)

    # Shared direction ray <(0, v_1, v_2)> inside H_0
    t_ray = 1.48
    r_a = proj(-t_ray * v_dir)
    r_b = proj(+t_ray * v_dir)
    ax1.plot([r_a[0], r_b[0]], [r_a[1], r_b[1]], color=AMBER, lw=2.8, zorder=3)
    ax1.text(r_b[0] + 0.06, r_b[1] - 0.08, r"$\langle(0, v_1, v_2)\rangle$",
             ha="left", va="top", fontsize=9.3, fontweight="bold", color=AMBER)

    # 2. Lower wedges (0 <= x_0 <= 1) of W_1 (BLUE) and W_2 (TEAL)
    t_w = 1.32
    w1_low = np.array([
        proj(-t_w * v_dir), proj(+t_w * v_dir),
        proj(e0 + t_w * v_dir), proj(e0 - t_w * v_dir),
    ])
    w2_low = np.array([
        proj(-t_w * v_dir), proj(+t_w * v_dir),
        proj(u_pt + t_w * v_dir), proj(u_pt - t_w * v_dir),
    ])
    ax1.add_patch(Polygon(w1_low, closed=True, facecolor=BLUE_LIGHT,
                          edgecolor=BLUE, lw=1.0, alpha=0.36, zorder=4))
    ax1.add_patch(Polygon(w2_low, closed=True, facecolor=TEAL_LIGHT,
                          edgecolor=TEAL, lw=1.0, alpha=0.38, zorder=4))

    # Scalar ray segment below x_0 = 1
    p_orig = proj(origin)
    p_a1 = proj(a_pt)
    p_a2 = proj(1.78 * a_pt)
    ax1.plot([p_orig[0], p_a1[0]], [p_orig[1], p_a1[1]],
             color=SLATE, lw=1.6, ls="--", zorder=4)

    # Origin 0 = (0, 0, 0)
    ax1.scatter(p_orig[0], p_orig[1], s=58, color=NAVY, edgecolor="white",
                lw=1.1, zorder=6)
    ax1.text(p_orig[0] - 0.10, p_orig[1] - 0.16, r"$\mathbf{0}=(0,0,0)$",
             ha="right", va="top", fontsize=9.2, fontweight="bold", color=NAVY)

    # Vertical x_0 axis from 0 through [1:0:0]
    p_e0 = proj(e0)
    ax1.plot([p_orig[0], p_e0[0]], [p_orig[1], p_e0[1]],
             color=SLATE, lw=1.3, ls=":", zorder=5)

    # 3. Affine slice sheet x_0 = 1
    poly_x1 = sheet_poly(1.0)
    ax1.add_patch(Polygon(poly_x1, closed=True, facecolor="white",
                          edgecolor=SLATE, lw=1.4, alpha=0.58, zorder=7))
    ax1.text(-2.28, 2.02, r"Affine slice $x_0 = 1$ ($\mathbf{A}$)",
             ha="left", va="center", fontsize=9.0, fontweight="bold", color=TEXT,
             bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=GREY_LINE, lw=0.8),
             zorder=11)

    # 4. Affine intersection lines on x_0 = 1: <v> (BLUE) and u + <v> (TEAL)
    sub_a, sub_b = proj(e0 - t_w * v_dir), proj(e0 + t_w * v_dir)
    cos_a, cos_b = proj(u_pt - t_w * v_dir), proj(u_pt + t_w * v_dir)
    ax1.plot([sub_a[0], sub_b[0]], [sub_a[1], sub_b[1]],
             color=BLUE, lw=3.0, zorder=9)
    ax1.plot([cos_a[0], cos_b[0]], [cos_a[1], cos_b[1]],
             color=TEAL, lw=3.0, zorder=9)

    ax1.text(sub_b[0] + 0.06, sub_b[1] - 0.04, r"$\langle v \rangle$",
             ha="left", va="center", fontsize=10.2, fontweight="bold", color=BLUE, zorder=11)
    ax1.text(cos_b[0] + 0.05, cos_b[1] + 0.06, r"$u + \langle v \rangle$",
             ha="left", va="center", fontsize=10.2, fontweight="bold", color=TEAL, zorder=11)

    # Affine origin [1:0:0] and shifted point [1:u_1:u_2]
    p_u = proj(u_pt)
    ax1.scatter(p_e0[0], p_e0[1], s=60, color=NAVY, edgecolor="white", lw=1.1, zorder=10)
    ax1.text(p_e0[0] - 0.08, p_e0[1] - 0.14, r"$[1:0:0]$",
             ha="right", va="top", fontsize=9.2, fontweight="bold", color=NAVY,
             bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.85),
             zorder=11)

    ax1.scatter(p_u[0], p_u[1], s=56, color=TEAL, edgecolor="white", lw=1.1, zorder=10)
    ax1.text(p_u[0] - 0.10, p_u[1] + 0.14, r"$[1:u_1:u_2]$",
             ha="right", va="bottom", fontsize=9.0, fontweight="bold", color=TEAL,
             bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.85),
             zorder=11)

    # Scalar equivalence ray continuing above x_0 = 1
    ax1.plot([p_a1[0], p_a2[0]], [p_a1[1], p_a2[1]],
             color=SLATE, lw=1.8, zorder=10)
    ax1.annotate("", xy=p_a2, xytext=proj(1.58 * a_pt),
                 arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.7), zorder=10)
    ax1.scatter(p_a1[0], p_a1[1], s=46, color=NAVY, edgecolor="white", lw=1.0, zorder=11)
    ax1.text(p_a2[0] + 0.08, p_a2[1] + 0.06, r"ray $\rho(1, a_1, a_2)$",
             ha="left", va="bottom", fontsize=8.6, color=SLATE,
             bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none", alpha=0.88),
             zorder=11)

    # ---------------- Panel (b): Observer's 2D view inside A ----------------
    ax2.set_xlim(-2.15, 2.55)
    ax2.set_ylim(-1.55, 2.85)
    draw_card(ax2, -2.10, -1.48, 4.60, 4.25, fc=GREY_BG, ec=GREY_LINE)
    ax2.text(0.20, 2.48,
             r"(b) Inside $\mathbf{A}$ ($x_0 = 1$): Parallel Cosets",
             ha="center", va="center", fontsize=10.5, fontweight="bold", color=TEXT)

    # Subtle 2D affine coordinate rectangle
    draw_card(ax2, -1.85, -1.20, 3.05, 3.25, fc="white", ec=GREY_LINE, lw=1.0, zorder=1)
    ax2.axhline(0.0, xmin=0.08, xmax=0.68, color="#e2e8f0", lw=0.9, zorder=2)
    ax2.axvline(-0.55, ymin=0.09, ymax=0.76, color="#e2e8f0", lw=0.9, zorder=2)

    # Boundary bar on the right for H_0 (x_0 = 0)
    hx = 1.88
    ax2.plot([hx, hx], [-1.05, 1.95], color=AMBER, lw=3.2, zorder=4)
    ax2.fill_betweenx([-1.05, 1.95], hx - 0.10, hx + 0.10,
                      color=AMBER_LIGHT, alpha=0.75, zorder=3)
    ax2.text(hx, -1.16, r"$H_0$ ($x_0 = 0$)",
             ha="center", va="top", fontsize=9.2, fontweight="bold", color=AMBER)

    # Parallel lines <v> and u + <v> inside the affine card
    orig2 = np.array([-0.55, -0.08])
    dir2 = np.array([1.0, 0.32])
    u2 = np.array([-0.82, 0.74])

    p1_l, p1_r = orig2 - 1.10 * dir2, orig2 + 1.55 * dir2
    p2_l, p2_r = u2 - 0.83 * dir2, u2 + 1.66 * dir2
    ax2.plot([p1_l[0], p1_r[0]], [p1_l[1], p1_r[1]], color=BLUE, lw=2.8, zorder=5)
    ax2.plot([p2_l[0], p2_r[0]], [p2_l[1], p2_r[1]], color=TEAL, lw=2.8, zorder=5)

    # Dashed projective convergence to shared point at infinity [0 : v_1 : v_2] on H_0
    inf_pt = np.array([hx, 0.78])
    ax2.plot([p1_r[0], inf_pt[0]], [p1_r[1], inf_pt[1]],
             color=BLUE, lw=1.6, ls="--", zorder=4)
    ax2.plot([p2_r[0], inf_pt[0]], [p2_r[1], inf_pt[1]],
             color=TEAL, lw=1.6, ls="--", zorder=4)

    # Shift arrow +u from affine origin to u
    ax2.annotate("", xy=u2, xytext=orig2,
                 arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.6, ls="--"),
                 zorder=6)
    ax2.text(-0.84, 0.34, r"shift $+u$", ha="right", va="center",
             fontsize=9.0, fontweight="bold", color=SLATE)

    # Points & labels
    ax2.scatter(orig2[0], orig2[1], s=58, color=NAVY, edgecolor="white", lw=1.1, zorder=7)
    ax2.text(orig2[0] + 0.06, orig2[1] - 0.18,
             r"Affine origin $[1:0:0]$",
             ha="left", va="top", fontsize=9.0, fontweight="bold", color=NAVY)

    ax2.scatter(u2[0], u2[1], s=56, color=TEAL, edgecolor="white", lw=1.1, zorder=7)
    ax2.text(u2[0] - 0.04, u2[1] + 0.16, r"$[1:u_1:u_2]$",
             ha="center", va="bottom", fontsize=9.0, fontweight="bold", color=TEAL)

    ax2.text(-0.05, 0.20, r"subspace $\langle v \rangle$",
             ha="center", va="bottom", fontsize=9.4, fontweight="bold",
             color=BLUE, rotation=18)
    ax2.text(-0.04, 1.12, r"coset $u + \langle v \rangle$",
             ha="center", va="bottom", fontsize=9.4, fontweight="bold",
             color=TEAL, rotation=18)

    ax2.scatter(inf_pt[0], inf_pt[1], s=74, color=AMBER, edgecolor=TEXT, lw=1.1, zorder=8)
    ax2.annotate(r"$[0 : v_1 : v_2]$" "\n(shared point\nat infinity)",
                 xy=(inf_pt[0], inf_pt[1] + 0.08),
                 xytext=(2.36, 1.38),
                 ha="right", va="bottom", fontsize=8.6, fontweight="bold", color=AMBER,
                 bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=AMBER, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2),
                 zorder=9)

    save_fig(fig, out_dir, "maths3_affine_slice.png")


# ---------------------------------------------------------------------------
# Figure 3: Transversal + 16-Point Theorem Schematic
#           (maths3_quadrics_transversal.png)
# ---------------------------------------------------------------------------
def quat_mul(q1, q2):
    """Quaternion product (w1 + x1 i + y1 j + z1 k)(w2 + x2 i + y2 j + z2 k)."""
    w1, x1, y1, z1 = q1
    w2, x2, y2, z2 = q2
    return (
        w1 * w2 - x1 * x2 - y1 * y2 - z1 * z2,
        w1 * x2 + x1 * w2 + y1 * z2 - z1 * y2,
        w1 * y2 - x1 * z2 + y1 * w2 + z1 * x2,
        w1 * z2 + x1 * y2 - y1 * x2 + z1 * w2,
    )


def make_fig3_transversal_16pt(out_dir: Path):
    # ---- Verify Panel (a) real 3D transversal construction ----
    # Plane Pi = <P, g_2> lies at z = 0; g_1 pierces Pi at P; g_3 pierces Pi at R.
    P3 = np.array([-1.28, -0.42, 0.0])
    d1 = np.array([0.24, 0.36, 1.0])          # g_1(u) = P3 + u * d1
    g2_p0 = np.array([0.06, 0.0, 0.0])
    d2 = np.array([0.28, 1.0, 0.0])           # g_2(s) = g2_p0 + s * d2 (lies in Pi)
    R3_true = np.array([1.34, 0.38, 0.0])
    d3 = np.array([-0.22, 0.32, 1.0])         # g_3(w) = R3_true + w * d3

    # Check mutual skewness of g_1, g_2, g_3 in R^3
    for (pA, vA), (pB, vB) in [((P3, d1), (g2_p0, d2)),
                               ((P3, d1), (R3_true, d3)),
                               ((g2_p0, d2), (R3_true, d3))]:
        vol = abs(np.linalg.det(np.column_stack([pB - pA, vA, vB])))
        assert vol > 0.25, f"Lines failed skewness check: {vol}"

    # Compute plane Pi = <P3, g_2> normal and verify R = Pi cap g_3
    n_pi = np.cross(g2_p0 - P3, d2)
    assert np.linalg.norm(n_pi[:2]) < 1e-12 and abs(n_pi[2]) > 0.5
    w_R = -np.dot(n_pi, R3_true - P3) / np.dot(n_pi, d3)
    R3 = R3_true + w_R * d3
    assert np.linalg.norm(R3 - R3_true) < 1e-12

    # Compute Q = PR cap g_2 inside Pi by solving P3 + lam*(R3 - P3) = g2_p0 + s*d2
    A_mat = np.column_stack([(R3 - P3)[:2], -d2[:2]])
    lam_Q, s_Q = np.linalg.solve(A_mat, (g2_p0 - P3)[:2])
    Q3 = P3 + lam_Q * (R3 - P3)
    assert np.linalg.norm(Q3 - (g2_p0 + s_Q * d2)) < 1e-12
    assert 0.2 < lam_Q < 0.8

    # ---- Verify Panel (b) 16-point theorem over F = R and over Quaternions H ----
    Q_ONE = (1.0, 0.0, 0.0, 0.0)
    Q_ZERO = (0.0, 0.0, 0.0, 0.0)
    Q_I = (0.0, 1.0, 0.0, 0.0)
    Q_J = (0.0, 0.0, 1.0, 0.0)
    Q_K = (0.0, 0.0, 0.0, 1.0)
    Q_MK = (0.0, 0.0, 0.0, -1.0)
    assert quat_mul(Q_I, Q_J) == Q_K
    assert quat_mul(Q_J, Q_I) == Q_MK and Q_K != Q_MK

    # Check the 15 guaranteed intersections in left-module H^4 for a = i, b = j:
    # g_x = <(1, 0, x, 0), (0, 1, 0, x)> for x in {0, inf, 1, a}
    # h_y = <(1, y, 0, 0), (0, 0, 1, y)> for y in {0, inf, 1, b}
    def qvec_left_scale(scalar, vec4):
        return tuple(quat_mul(scalar, c) for c in vec4)

    def qvec_add(u4, v4):
        return tuple(tuple(u4[m][n] + v4[m][n] for n in range(4)) for m in range(4))

    a_q, b_q = Q_I, Q_J
    g_bases = {
        "g1": ((Q_ONE, Q_ZERO, Q_ZERO, Q_ZERO), (Q_ZERO, Q_ONE, Q_ZERO, Q_ZERO)),
        "g2": ((Q_ZERO, Q_ZERO, Q_ONE, Q_ZERO), (Q_ZERO, Q_ZERO, Q_ZERO, Q_ONE)),
        "g3": ((Q_ONE, Q_ZERO, Q_ONE, Q_ZERO), (Q_ZERO, Q_ONE, Q_ZERO, Q_ONE)),
        "ga": ((Q_ONE, Q_ZERO, a_q, Q_ZERO), (Q_ZERO, Q_ONE, Q_ZERO, a_q)),
    }
    h_bases = {
        "h1": ((Q_ONE, Q_ZERO, Q_ZERO, Q_ZERO), (Q_ZERO, Q_ZERO, Q_ONE, Q_ZERO)),
        "h2": ((Q_ZERO, Q_ONE, Q_ZERO, Q_ZERO), (Q_ZERO, Q_ZERO, Q_ZERO, Q_ONE)),
        "h3": ((Q_ONE, Q_ONE, Q_ZERO, Q_ZERO), (Q_ZERO, Q_ZERO, Q_ONE, Q_ONE)),
        "hb": ((Q_ONE, b_q, Q_ZERO, Q_ZERO), (Q_ZERO, Q_ZERO, Q_ONE, b_q)),
    }

    # Verify rank over R (each H-line has real dimension 8 in R^16; intersection <-> rank < 16)
    def quat_left_mat(q):
        w, x, y, z = q
        return np.array([
            [w, -x, -y, -z],
            [x,  w, -z,  y],
            [y,  z,  w, -x],
            [z, -y,  x,  w],
        ])

    def line_real_basis(u4, v4):
        # Left H-span of u4, v4 is right-column span of left-multiplication or row span:
        # alpha * u4 has real vector sum_c alpha_c (e_c * u4)
        units = [Q_ONE, Q_I, Q_J, Q_K]
        cols = []
        for vec in (u4, v4):
            for e in units:
                scaled = qvec_left_scale(e, vec)
                cols.append(np.array([comp for q in scaled for comp in q]))
        return np.column_stack(cols)  # 16 x 8

    intersections_15 = 0
    for gk, gb in g_bases.items():
        for hk, hb in h_bases.items():
            M = np.column_stack([line_real_basis(*gb), line_real_basis(*hb)])
            rk = np.linalg.matrix_rank(M, tol=1e-9)
            if (gk, hk) != ("ga", "hb"):
                assert rk == 12, f"Expected intersection (rank 12) for {(gk, hk)}, got {rk}"
                intersections_15 += 1
            else:
                assert rk == 16, f"Expected skew miss (rank 16) at 16th corner in H, got {rk}"
    assert intersections_15 == 15

    # Also verify exact 16th-corner vectors from lines 569-577
    pt_on_hb = qvec_add(h_bases["hb"][0], qvec_left_scale(a_q, h_bases["hb"][1]))
    pt_on_ga = qvec_add(g_bases["ga"][0], qvec_left_scale(b_q, g_bases["ga"][1]))
    assert pt_on_hb == (Q_ONE, Q_J, Q_I, Q_K)
    assert pt_on_ga == (Q_ONE, Q_J, Q_I, Q_MK)

    # ---------------- Draw Figure 3 ----------------
    fig = plt.figure(figsize=(11.4, 5.4), dpi=220)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.05, 1.15], wspace=0.06)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.axis("off")

    # -------- Panel (a): Real 3D geometry --------
    def proj3(pt):
        x, y, z = pt
        return np.array([0.92 * x + 0.36 * y, 0.96 * z + 0.36 * y - 0.10 * x])

    ax1.set_xlim(-2.40, 2.40)
    ax1.set_ylim(-1.65, 2.35)
    draw_card(ax1, -2.35, -1.58, 4.70, 3.85, fc=GREY_BG, ec=GREY_LINE)
    ax1.text(0.0, 1.96,
             r"(a) Unique Transversal $h_P$ via $\Pi = \langle P, g_2 \rangle$",
             ha="center", va="center", fontsize=10.2, fontweight="bold", color=TEXT)

    # Segments of g_1 and g_3 below Pi (z < 0) drawn first (occluded behind Pi)
    for p_base, d_vec in [(P3, d1), (R3, d3)]:
        p_low = proj3(p_base - 1.12 * d_vec)
        p_0 = proj3(p_base)
        ax1.plot([p_low[0], p_0[0]], [p_low[1], p_0[1]],
                 color=BLUE, lw=2.2, ls="--", alpha=0.48, zorder=1)

    # Plane Pi = <P, g_2> (z = 0)
    pi_corners = [
        (-1.85, -1.15, 0.0), (1.85, -1.15, 0.0),
        (1.85,  1.22, 0.0), (-1.85,  1.22, 0.0),
    ]
    pi_2d = np.array([proj3(c) for c in pi_corners])
    ax1.add_patch(Polygon(pi_2d, closed=True, facecolor=AMBER_LIGHT,
                          edgecolor=AMBER, lw=1.5, alpha=0.68, zorder=2))
    ax1.text(-1.92, -0.70, r"Plane $\Pi = \langle P, g_2 \rangle$",
             ha="left", va="top", fontsize=9.2, fontweight="bold", color=AMBER)

    # Line g_2 lying inside Pi
    g2_a, g2_b = proj3(g2_p0 - 1.12 * d2), proj3(g2_p0 + 1.18 * d2)
    ax1.plot([g2_a[0], g2_b[0]], [g2_a[1], g2_b[1]],
             color=BLUE, lw=2.8, zorder=4)
    ax1.text(g2_b[0] + 0.05, g2_b[1] + 0.08, r"$g_2 \subset \Pi$",
             ha="left", va="bottom", fontsize=9.8, fontweight="bold", color=BLUE)

    # Transversal line h_P = PR lying inside Pi
    hp_a = proj3(P3 - 0.18 * (R3 - P3))
    hp_b = proj3(P3 + 1.18 * (R3 - P3))
    ax1.plot([hp_a[0], hp_b[0]], [hp_a[1], hp_b[1]],
             color=TEAL, lw=3.0, zorder=5)
    ax1.text(hp_a[0] - 0.04, hp_a[1] - 0.14, r"$h_P = PR$",
             ha="left", va="top", fontsize=9.8, fontweight="bold", color=TEAL)

    # Segments of g_1 and g_3 above Pi (z >= 0) drawn crisply in front, with white halo if crossing g_2
    for p_base, d_vec, lbl, off in [
        (P3, d1, r"$g_1$", (-0.12, 0.08)),
        (R3, d3, r"$g_3$", (0.10, 0.08)),
    ]:
        p_0 = proj3(p_base)
        p_hi = proj3(p_base + 1.25 * d_vec)
        # Check 2D crossing with g_2 for clean overpass gap
        hit = seg_intersection_2d(p_0, p_hi, g2_a, g2_b)
        if hit is not None and 0.05 < hit[2] < 0.95 and 0.05 < hit[3] < 0.95:
            ax1.plot([p_0[0], p_hi[0]], [p_0[1], p_hi[1]],
                     color=AMBER_LIGHT, lw=6.5, zorder=6)
        ax1.plot([p_0[0], p_hi[0]], [p_0[1], p_hi[1]],
                 color=BLUE, lw=2.9, zorder=7)
        ax1.text(p_hi[0] + off[0], p_hi[1] + off[1], lbl,
                 ha="center", va="bottom", fontsize=10.2, fontweight="bold", color=BLUE)

    # Points P, Q, R
    for pt3, lbl, col, dxy in [
        (P3, r"$P \in g_1$", NAVY, (-0.38, 0.22)),
        (Q3, r"$Q = PR \cap g_2$", NAVY, (0.04, -0.26)),
        (R3, r"$R = \Pi \cap g_3$", AMBER, (0.12, -0.20)),
    ]:
        p2 = proj3(pt3)
        ec = TEXT if col == AMBER else "white"
        ax1.scatter(p2[0], p2[1], s=66, color=col, edgecolor=ec, lw=1.1, zorder=9)
        ax1.text(p2[0] + dxy[0], p2[1] + dxy[1], lbl,
                 ha="center", va="center", fontsize=9.2, fontweight="bold", color=col,
                 bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.86),
                 zorder=10)

    # -------- Panel (b): Flat schematic 4x4 grid + magnified 16th-corner insets --------
    ax2.set_xlim(0.0, 5.45)
    ax2.set_ylim(-1.65, 2.35)
    draw_card(ax2, 0.05, -1.58, 5.35, 3.85, fc=GREY_BG, ec=GREY_LINE)
    ax2.text(2.72, 1.96,
             r"(b) 16-Point Theorem (Schematic $4 \times 4$ Grid)",
             ha="center", va="center", fontsize=10.2, fontweight="bold", color=TEXT)

    xs = [0.68, 1.24, 1.80, 2.48]  # h_1, h_2, h_3, h_b
    ys = [1.22, 0.66, 0.10, -0.62] # g_1, g_2, g_3, g_a
    h_lbls = [r"$h_1$", r"$h_2$", r"$h_3$", r"$h_b$"]
    g_lbls = [r"$g_1$", r"$g_2$", r"$g_3$", r"$g_a$"]

    for idx, x in enumerate(xs):
        lw = 2.5 if idx == 3 else 1.9
        ax2.plot([x, x], [ys[3] - 0.30, ys[0] + 0.28], color=TEAL, lw=lw, zorder=2)
        ax2.text(x, ys[0] + 0.33, h_lbls[idx], ha="center", va="bottom",
                 fontsize=9.6, fontweight="bold", color=TEAL)

    for idx, y in enumerate(ys):
        lw = 2.5 if idx == 3 else 1.9
        ax2.plot([xs[0] - 0.26, xs[3] + 0.26], [y, y], color=BLUE, lw=lw, zorder=3)
        ax2.text(xs[0] - 0.30, y, g_lbls[idx], ha="right", va="center",
                 fontsize=9.6, fontweight="bold", color=BLUE)

    # 15 guaranteed intersections
    for i, y in enumerate(ys):
        for j, x in enumerate(xs):
            if i == 3 and j == 3:
                continue
            ax2.scatter(x, y, s=46, color=NAVY, edgecolor="white", lw=0.9, zorder=5)

    ax2.text(1.48, -1.24, "$9 + 3 + 3 = 15$\nguaranteed intersections",
             ha="center", va="center", fontsize=8.8, color=TEXT, fontweight="bold")

    # Magnifier ring on 16th crossing (xs[3], ys[3])
    c16 = (xs[3], ys[3])
    ax2.add_patch(Circle(c16, 0.21, facecolor=AMBER_LIGHT, edgecolor=AMBER,
                         lw=1.8, ls="--", zorder=6))
    ax2.text(c16[0], c16[1], "?", ha="center", va="center",
             fontsize=10.5, fontweight="bold", color=AMBER, zorder=7)

    # Two stacked magnified outcome cards on the right
    # Top inset: Commutative ab = ba
    ix, iw = 3.05, 2.22
    draw_card(ax2, ix, 0.14, iw, 1.48, fc="white", ec=TEAL, lw=1.3, zorder=2)
    ax2.text(ix + iw * 0.5, 1.38, r"If $ab = ba$ (field $F$)",
             ha="center", va="center", fontsize=9.3, fontweight="bold", color=TEAL)
    cx1, cy1 = ix + 0.62, 0.80
    ax2.plot([cx1 - 0.42, cx1 + 0.42], [cy1, cy1], color=BLUE, lw=2.6, zorder=3)
    ax2.plot([cx1, cx1], [cy1 - 0.34, cy1 + 0.34], color=TEAL, lw=2.6, zorder=3)
    ax2.scatter(cx1, cy1, s=68, color=NAVY, edgecolor="white", lw=1.1, zorder=5)
    ax2.text(ix + 1.15, cy1 + 0.06, "Lines meet:", ha="left", va="bottom",
             fontsize=8.6, fontweight="bold", color=NAVY)
    ax2.text(ix + iw * 0.5, 0.32, r"$(1 : b : a : ab) = (1 : b : a : ba)$",
             ha="center", va="center", fontsize=8.7, color=TEXT)

    # Bottom inset: Non-commutative ab != ba (Quaternions H)
    draw_card(ax2, ix, -1.46, iw, 1.50, fc="white", ec=RED, lw=1.3, zorder=2)
    ax2.text(ix + iw * 0.5, -0.20, r"If $ab \neq ba$ ($\mathbb{H}$: $ij = k \neq -k$)",
             ha="center", va="center", fontsize=9.1, fontweight="bold", color=RED)
    cx2, cy2 = ix + 0.62, -0.78
    # Vertical h_j behind, white overpass gap, slanted/offset horizontal g_i passing without meeting
    ax2.plot([cx2 - 0.10, cx2 - 0.10], [cy2 - 0.36, cy2 + 0.36],
             color=TEAL, lw=2.5, zorder=3)
    ax2.add_patch(Circle((cx2 - 0.10, cy2 - 0.12), 0.085, facecolor="white",
                         edgecolor="none", zorder=4))
    ax2.plot([cx2 - 0.44, cx2 + 0.42], [cy2 - 0.12, cy2 - 0.12],
             color=BLUE, lw=2.5, zorder=5)
    # Mark distinct points on h_j and g_i
    p_hj = (cx2 - 0.10, cy2 + 0.16)
    p_gi = (cx2 + 0.18, cy2 - 0.12)
    ax2.scatter(*p_hj, s=46, color=RED, edgecolor="white", lw=0.9, zorder=6)
    ax2.scatter(*p_gi, s=46, color=RED, edgecolor="white", lw=0.9, zorder=6)
    ax2.plot([p_hj[0], p_gi[0]], [p_hj[1], p_gi[1]],
             color=RED, lw=1.4, ls=":", zorder=6)
    ax2.text(ix + 1.12, cy2 + 0.14, r"$h_j : (1:j:i:k)$",
             ha="left", va="center", fontsize=8.3, fontweight="bold", color=TEAL)
    ax2.text(ix + 1.12, cy2 - 0.14, r"$g_i : (1:j:i:-k)$",
             ha="left", va="center", fontsize=8.3, fontweight="bold", color=BLUE)
    ax2.text(ix + iw * 0.5, -1.29, "Lines miss (skew gap)",
             ha="center", va="center", fontsize=8.6, fontweight="bold", color=RED)

    # Connector arrows from magnifier circle to both insets
    for ty, col in [(0.75, TEAL), (-0.75, RED)]:
        arr = FancyArrowPatch(
            (c16[0] + 0.20, c16[1] + (0.08 if ty > 0 else -0.08)),
            (ix + 0.04, ty),
            connectionstyle="arc3,rad=0.10" if ty > 0 else "arc3,rad=-0.10",
            arrowstyle="->,head_length=5,head_width=3",
            color=col, lw=1.4, ls="--", zorder=6
        )
        ax2.add_patch(arr)

    save_fig(fig, out_dir, "maths3_quadrics_transversal.png")


# ---------------------------------------------------------------------------
# Figure 4: Tangent Planes of the Four 3D Quadratic Sets
#           (maths3_quadsets_tangent_planes.png)
# ---------------------------------------------------------------------------
def make_3d_cam(azim_deg: float = -42.0, elev_deg: float = 21.0):
    """Orthographic 3D camera returning (px, py, depth) for true occlusion."""
    az = math.radians(azim_deg)
    el = math.radians(elev_deg)
    right = np.array([-math.sin(az), math.cos(az), 0.0])
    up = np.array([-math.cos(az) * math.sin(el),
                   -math.sin(az) * math.sin(el),
                   math.cos(el)])
    view = np.array([math.cos(az) * math.cos(el),
                     math.sin(az) * math.cos(el),
                     math.sin(el)])

    def project(pts):
        arr = np.asarray(pts, dtype=float)
        px = arr @ right
        py = arr @ up
        depth = arr @ view
        return px, py, depth

    return project


def draw_mesh_patches(ax, XX, YY, ZZ, cam, fc_base, ec="none", alpha=0.45,
                      mask_fn=None, zorder=2):
    """Render quad patches of a surface back-to-front using exact camera depth."""
    ny, nx = XX.shape
    quads = []
    for i in range(ny - 1):
        for j in range(nx - 1):
            pts3 = np.array([
                [XX[i, j],     YY[i, j],     ZZ[i, j]],
                [XX[i, j + 1], YY[i, j + 1], ZZ[i, j + 1]],
                [XX[i + 1, j + 1], YY[i + 1, j + 1], ZZ[i + 1, j + 1]],
                [XX[i + 1, j], YY[i + 1, j], ZZ[i + 1, j]],
            ])
            centroid = pts3.mean(axis=0)
            if mask_fn is not None and not mask_fn(centroid):
                continue
            px, py, dep = cam(pts3)
            quads.append((dep.mean(), np.column_stack([px, py])))
    quads.sort(key=lambda item: item[0])
    for _, poly2 in quads:
        ax.add_patch(Polygon(poly2, closed=True, facecolor=fc_base,
                             edgecolor=ec, lw=0.25, alpha=alpha, zorder=zorder))


def make_fig4_tangent_planes(out_dir: Path):
    # ---- Mathematical assertions for all four 3D quadratic sets ----
    # (a) Sphere x^2 + y^2 + z^2 = 1 at North Pole P = (0, 0, 1), Q_P : z = 1
    P_sph = np.array([0.0, 0.0, 1.0])
    d_sec = np.array([0.62, -0.34, -1.0])
    t_sec = -2.0 * np.dot(P_sph, d_sec) / np.dot(d_sec, d_sec)
    Q_sph = P_sph + t_sec * d_sec
    assert abs(np.dot(Q_sph, Q_sph) - 1.0) < 1e-12 and Q_sph[2] < 0.5

    # (b) Cone x^2 + y^2 - z^2 = 0: vertex V = (0,0,0), smooth P != V, base plane U : z = -1
    V_cone = np.array([0.0, 0.0, 0.0])
    th_P = math.radians(-38.0)
    z_P = 0.72
    P_cone = np.array([z_P * math.cos(th_P), z_P * math.sin(th_P), z_P])
    assert abs(P_cone[0]**2 + P_cone[1]**2 - P_cone[2]**2) < 1e-12
    grad_cone_P = np.array([2 * P_cone[0], 2 * P_cone[1], -2 * P_cone[2]])
    grad_cone_V = np.array([0.0, 0.0, 0.0])
    assert np.linalg.norm(grad_cone_V) == 0.0  # V is singular: Q_V = P
    # Tangent plane Q_P: grad_cone_P . (X - P_cone) = 0 <=> x cos th_P + y sin th_P - z = 0
    for s_rul in np.linspace(-1.15, 1.15, 20):
        rul_pt = np.array([s_rul * math.cos(th_P), s_rul * math.sin(th_P), s_rul])
        assert abs(rul_pt[0]**2 + rul_pt[1]**2 - rul_pt[2]**2) < 1e-12
        assert abs(np.dot(grad_cone_P, rul_pt - P_cone)) < 1e-12
    # Base conic Q' = Q cap U in plane U : z = -1.05 (missing V)
    z_U = -1.05
    for th_u in np.linspace(0, 2 * np.pi, 24):
        bx = abs(z_U) * math.cos(th_u)
        by = abs(z_U) * math.sin(th_u)
        assert abs(bx**2 + by**2 - z_U**2) < 1e-12

    # (c) Hyperboloid x^2 + y^2 - z^2 = 1 at P = (1, 0, 0), Q_P : x = 1 => g u h: z = +- y
    P_hyp = np.array([1.0, 0.0, 0.0])
    for s_h in np.linspace(-1.1, 1.1, 20):
        g_pt = np.array([1.0, s_h, s_h])
        h_pt = np.array([1.0, s_h, -s_h])
        assert abs(g_pt[0]**2 + g_pt[1]**2 - g_pt[2]**2 - 1.0) < 1e-12
        assert abs(h_pt[0]**2 + h_pt[1]**2 - h_pt[2]**2 - 1.0) < 1e-12

    # (d) Union of two planes H_1 : z = 0.25 y, H_2 : y = 0 (q(x,y,z) = y*(z - 0.25*y) = 0)
    P_pl = np.array([0.35, -0.82, 0.25 * (-0.82)])
    assert abs(P_pl[1]) > 0.5 and abs(P_pl[2] - 0.25 * P_pl[1]) < 1e-12

    # ---- Create 2x2 grid ----
    fig = plt.figure(figsize=(11.0, 8.6), dpi=220)
    gs = fig.add_gridspec(2, 2, wspace=0.06, hspace=0.08)
    axes = [fig.add_subplot(gs[i, j]) for i in range(2) for j in range(2)]
    for ax in axes:
        ax.set_xlim(-2.15, 2.15)
        ax.set_ylim(-1.75, 1.95)
        ax.set_aspect("equal")
        ax.axis("off")
        draw_card(ax, -2.10, -1.70, 4.20, 3.60, fc=GREY_BG, ec=GREY_LINE)

    # -------- Panel (a): Elliptic quadric (sphere) --------
    axa = axes[0]
    cam_a = make_3d_cam(azim_deg=-38.0, elev_deg=20.0)
    axa.text(0.0, 1.63,
             r"(a) Elliptic Quadric ($0$ $\mathcal{Q}$-lines): $\mathcal{Q}_P \cap \mathcal{Q} = \{P\}$",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    u_sp = np.linspace(0, np.pi, 22)
    v_sp = np.linspace(0, 2 * np.pi, 36)
    UU, VV = np.meshgrid(u_sp, v_sp, indexing="ij")
    R_sp = 0.96
    XXs = R_sp * np.sin(UU) * np.cos(VV)
    YYs = R_sp * np.sin(UU) * np.sin(VV)
    ZZs = R_sp * np.cos(UU) - 0.15
    draw_mesh_patches(axa, XXs, YYs, ZZs, cam_a, TEAL_LIGHT, ec="#99f6e4",
                      alpha=0.55, zorder=2)

    # Secant line piercing sphere from P to Q
    P_s_draw = np.array([0.0, 0.0, R_sp - 0.15])
    Q_s_draw = R_sp * Q_sph + np.array([0.0, 0.0, -0.15])
    sec_ext = P_s_draw + 1.28 * (Q_s_draw - P_s_draw)
    px_s, py_s, _ = cam_a(np.array([P_s_draw, Q_s_draw, sec_ext]))
    axa.plot(px_s[:2], py_s[:2], color=RED, lw=2.0, ls="--", zorder=4)
    axa.plot(px_s[1:], py_s[1:], color=RED, lw=2.0, ls="--", zorder=6)

    # Horizontal tangent plane Q_P at North Pole z = R_sp - 0.15
    z_tp = R_sp - 0.15
    tp_a = np.array([[-1.30, -1.20, z_tp], [1.30, -1.20, z_tp],
                     [1.30,  1.20, z_tp], [-1.30,  1.20, z_tp]])
    px_tp, py_tp, _ = cam_a(tp_a)
    axa.add_patch(Polygon(np.column_stack([px_tp, py_tp]), closed=True,
                          facecolor=AMBER_LIGHT, edgecolor=AMBER, lw=1.5,
                          alpha=0.68, zorder=5))

    # 1-point tangent lines inside Q_P
    for dx, dy in [(1.18, 0.15), (-0.35, 1.08)]:
        t_pts = np.array([P_s_draw - np.array([dx, dy, 0.0]),
                          P_s_draw + np.array([dx, dy, 0.0])])
        tx, ty, _ = cam_a(t_pts)
        axa.plot(tx, ty, color=SLATE, lw=1.7, ls="-", zorder=6)

    px_P, py_P, _ = cam_a(P_s_draw[None, :])
    px_Q, py_Q, _ = cam_a(Q_s_draw[None, :])
    axa.scatter(px_P[0], py_P[0], s=64, color=NAVY, edgecolor="white", lw=1.1, zorder=8)
    axa.scatter(px_Q[0], py_Q[0], s=52, color=RED, edgecolor="white", lw=1.0, zorder=8)
    axa.text(px_P[0] - 0.12, py_P[0] + 0.18, r"$P$", fontsize=10.5,
             fontweight="bold", color=NAVY, ha="right", va="bottom", zorder=9)
    axa.text(1.18, py_P[0] + 0.50, r"$\mathcal{Q}_P$ ($1$-pt tangents)",
             fontsize=8.8, fontweight="bold", color=AMBER, ha="center",
             bbox=dict(boxstyle="round,pad=0.10", fc=GREY_BG, ec="none", alpha=0.88),
             zorder=9)
    axa.text(px_Q[0] + 0.14, py_Q[0] - 0.12, r"$2$-pt secant ($Q$)",
             fontsize=8.8, fontweight="bold", color=RED, ha="left", va="top", zorder=9)

    # -------- Panel (b): Cone with base plane U, base circle Q', rulings VX --------
    axb = axes[1]
    cam_b = make_3d_cam(azim_deg=-42.0, elev_deg=19.0)
    axb.text(0.0, 1.63,
             r"(b) Cone ($1$ $\mathcal{Q}$-line): $\mathcal{Q}_P \cap \mathcal{Q} = g = PV$, base $\mathcal{Q}' = \mathcal{Q} \cap U$",
             ha="center", va="center", fontsize=9.1, fontweight="bold", color=TEXT)

    # Complementary horizontal plane U at z = z_U (-1.05) missing vertex V = (0,0,0)
    u_plane = np.array([[-1.48, -1.35, z_U], [1.48, -1.35, z_U],
                        [1.48,  1.35, z_U], [-1.48,  1.35, z_U]])
    ux, uy, _ = cam_b(u_plane)
    axb.add_patch(Polygon(np.column_stack([ux, uy]), closed=True,
                          facecolor=BLUE_PALE, edgecolor=BLUE, lw=1.2,
                          alpha=0.72, zorder=1))
    axb.text(-1.98, -0.68, r"Complement $U$" "\n" r"($V \notin U$)",
             ha="left", va="center", fontsize=8.5, fontweight="bold", color=BLUE,
             bbox=dict(boxstyle="round,pad=0.10", fc=GREY_BG, ec="none", alpha=0.85))

    # Double cone mesh z in [-1.05, +0.98]
    zc = np.linspace(z_U, 0.98, 22)
    tc = np.linspace(0, 2 * np.pi, 36)
    ZC, TC = np.meshgrid(zc, tc, indexing="ij")
    XXc = np.abs(ZC) * np.cos(TC)
    YYc = np.abs(ZC) * np.sin(TC)
    draw_mesh_patches(axb, XXc, YYc, ZC, cam_b, TEAL_LIGHT, ec="#99f6e4",
                      alpha=0.44, zorder=2)

    # Base circle Q' = Q cap U at z = z_U
    th_circ = np.linspace(0, 2 * np.pi, 160)
    q_prime = np.column_stack([abs(z_U) * np.cos(th_circ),
                               abs(z_U) * np.sin(th_circ),
                               np.full_like(th_circ, z_U)])
    qpx, qpy, _ = cam_b(q_prime)
    axb.plot(qpx, qpy, color=TEAL, lw=2.6, zorder=4)
    axb.text(1.12, -1.46, r"Base conic $\mathcal{Q}' = \mathcal{Q} \cap U$",
             ha="center", va="top", fontsize=8.5, fontweight="bold", color=TEAL,
             bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none", alpha=0.92),
             zorder=9)

    # Sample rulings VX from V to points X on Q'
    for ang_deg in (-145.0, -98.0, 18.0, 115.0):
        ang = math.radians(ang_deg)
        r_end_lo = np.array([abs(z_U) * math.cos(ang), abs(z_U) * math.sin(ang), z_U])
        r_end_hi = np.array([-0.98 * math.cos(ang), -0.98 * math.sin(ang), 0.98])
        rx, ry, _ = cam_b(np.array([r_end_lo, r_end_hi]))
        axb.plot(rx, ry, color=SLATE, lw=1.1, ls="--", alpha=0.75, zorder=3)

    # Mark one explicit base point X on Q' and its ruling VX cleanly at bottom-left
    ang_X = math.radians(-98.0)
    X_pt = np.array([abs(z_U) * math.cos(ang_X), abs(z_U) * math.sin(ang_X), z_U])
    xx, xy, _ = cam_b(X_pt[None, :])
    axb.scatter(xx[0], xy[0], s=48, color=TEAL, edgecolor="white", lw=1.0, zorder=6)
    axb.text(-1.12, -1.46, r"$X \in \mathcal{Q}'$ (ruling $VX$)",
             ha="center", va="top", fontsize=8.4, fontweight="bold", color=SLATE,
             bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none", alpha=0.92),
             zorder=9)

    # Tangent plane Q_P touching cone along ruling g = PV
    e_rul = np.array([math.cos(th_P), math.sin(th_P), 1.0])
    e_tan = np.array([-math.sin(th_P), math.cos(th_P), 0.0])
    tp_b = np.array([
        -0.25 * e_rul - 0.96 * e_tan,
        -0.25 * e_rul + 0.96 * e_tan,
         1.05 * e_rul + 0.96 * e_tan,
         1.05 * e_rul - 0.96 * e_tan,
    ])
    tbx, tby, _ = cam_b(tp_b)
    axb.add_patch(Polygon(np.column_stack([tbx, tby]), closed=True,
                          facecolor=AMBER_LIGHT, edgecolor=AMBER, lw=1.4,
                          alpha=0.65, zorder=5))

    # Single Q-line ruling g = PV
    g_pts = np.array([-abs(z_U) * e_rul, 1.04 * e_rul])
    gx, gy, _ = cam_b(g_pts)
    axb.plot(gx, gy, color=BLUE, lw=3.0, zorder=7)

    vx, vy, _ = cam_b(V_cone[None, :])
    px_c, py_c, _ = cam_b(P_cone[None, :])
    axb.scatter(vx[0], vy[0], s=66, color=AMBER, edgecolor=TEXT, lw=1.1, zorder=8)
    axb.scatter(px_c[0], py_c[0], s=58, color=NAVY, edgecolor="white", lw=1.0, zorder=8)
    axb.text(vx[0] - 0.16, vy[0] + 0.06,
             r"$V$ ($\mathrm{Rad}(\mathcal{Q})=\{V\}$, $\mathcal{Q}_V=\mathbf{P}$)",
             ha="right", va="center", fontsize=8.3, fontweight="bold", color=AMBER,
             bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.92),
             zorder=9)
    axb.text(px_c[0] + 0.13, py_c[0] - 0.03, r"$P$ ($g = PV$)",
             ha="left", va="center", fontsize=8.6, fontweight="bold", color=BLUE,
             bbox=dict(boxstyle="round,pad=0.08", fc="white", ec="none", alpha=0.92),
             zorder=9)
    axb.text(1.42, 0.56, r"$\mathcal{Q}_P$", ha="left", va="center",
             fontsize=9.6, fontweight="bold", color=AMBER, zorder=9)

    # -------- Panel (c): Hyperbolic quadric (true depth occlusion across x = 1) --------
    axc = axes[2]
    cam_c = make_3d_cam(azim_deg=-36.0, elev_deg=20.0)
    axc.text(0.0, 1.63,
             r"(c) Hyperbolic Quadric ($2$ $\mathcal{Q}$-lines): $\mathcal{Q}_P \cap \mathcal{Q} = g \cup h$",
             ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEXT)

    zh = np.linspace(-1.02, 1.02, 24)
    th_h = np.linspace(0, 2 * np.pi, 44)
    ZH, THH = np.meshgrid(zh, th_h, indexing="ij")
    RH = np.sqrt(1.0 + ZH**2) * 0.82
    XXh = RH * np.cos(THH)
    YYh = RH * np.sin(THH)
    ZZh = ZH * 0.82
    x_cut = 0.82  # scaled waist radius

    # 1. Back half of hyperboloid (x <= x_cut) behind Q_P
    draw_mesh_patches(axc, XXh, YYh, ZZh, cam_c, TEAL_LIGHT, ec="#99f6e4",
                      alpha=0.45, mask_fn=lambda c: c[0] <= x_cut + 0.01, zorder=2)

    # 2. Tangent plane Q_P : x = x_cut
    tp_c = np.array([
        [x_cut, -1.18, -1.05], [x_cut, 1.18, -1.05],
        [x_cut,  1.18,  1.05], [x_cut, -1.18, 1.05],
    ])
    tcx, tcy, _ = cam_c(tp_c)
    axc.add_patch(Polygon(np.column_stack([tcx, tcy]), closed=True,
                          facecolor=AMBER_LIGHT, edgecolor=AMBER, lw=1.5,
                          alpha=0.66, zorder=4))

    # 3. Front flaring portions of hyperboloid (x > x_cut) in front of Q_P!
    draw_mesh_patches(axc, XXh, YYh, ZZh, cam_c, "#99f6e4", ec=TEAL,
                      alpha=0.62, mask_fn=lambda c: c[0] > x_cut + 0.01, zorder=5)

    # 4. X-shaped intersection rulings g and h inside Q_P : x = x_cut, z = +- y
    s_lim = 1.02 * 0.82
    g_line = np.array([[x_cut, -s_lim, -s_lim], [x_cut, s_lim, s_lim]])
    h_line = np.array([[x_cut, -s_lim,  s_lim], [x_cut, s_lim, -s_lim]])
    glx, gly, _ = cam_c(g_line)
    hlx, hly, _ = cam_c(h_line)
    axc.plot(glx, gly, color=BLUE, lw=3.1, zorder=7)
    axc.plot(hlx, hly, color=TEAL, lw=3.1, zorder=7)

    phx, phy, _ = cam_c(np.array([[x_cut, 0.0, 0.0]]))
    axc.scatter(phx[0], phy[0], s=64, color=NAVY, edgecolor="white", lw=1.1, zorder=8)
    axc.text(phx[0] + 0.14, phy[0] - 0.04, r"$P$", fontsize=10.5,
             fontweight="bold", color=NAVY, ha="left", va="center", zorder=9)
    axc.text(glx[1] + 0.08, gly[1] + 0.04, r"$g \in \mathcal{R}$",
             fontsize=9.2, fontweight="bold", color=BLUE, ha="left", zorder=9)
    axc.text(hlx[1] + 0.08, hly[1] - 0.06, r"$h \in \mathcal{R}'$",
             fontsize=9.2, fontweight="bold", color=TEAL, ha="left", zorder=9)
    axc.text(-1.25, -1.56, r"$\mathcal{Q}_P = \langle g, h \rangle$ slices through saddle",
             fontsize=8.7, fontweight="bold", color=AMBER, ha="left",
             bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none", alpha=0.92),
             zorder=9)

    # -------- Panel (d): Union of two planes H_1 u H_2 --------
    axd = axes[3]
    cam_d = make_3d_cam(azim_deg=-35.0, elev_deg=22.0)
    axd.text(0.0, 1.63,
             r"(d) Two Planes $H_1 \cup H_2$ (Pencil): $\mathcal{Q}_P = H_1$",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    # H_2 : tilted back plane x = 0; H_1 : horizontal plane z = 0 (= Q_P for P in H_1 \ H_2)
    h2_back = np.array([[0.0, -1.25, -1.05], [0.0, 1.25, -1.05],
                        [0.0,  1.25,  0.0],  [0.0, -1.25, 0.0]])
    h1_full = np.array([[-1.42, -1.25, 0.0], [1.42, -1.25, 0.0],
                        [1.42,  1.25,  0.0], [-1.42, 1.25, 0.0]])
    h2_top = np.array([[0.0, -1.25, 0.0], [0.0, 1.25, 0.0],
                       [0.0,  1.25, 1.12], [0.0, -1.25, 1.12]])

    b2x, b2y, _ = cam_d(h2_back)
    axd.add_patch(Polygon(np.column_stack([b2x, b2y]), closed=True,
                          facecolor=TEAL_LIGHT, edgecolor=TEAL, lw=1.2,
                          alpha=0.50, zorder=2))

    # H_1 = Q_P highlighted in AMBER_LIGHT with TEAL/AMBER border
    h1x, h1y, _ = cam_d(h1_full)
    axd.add_patch(Polygon(np.column_stack([h1x, h1y]), closed=True,
                          facecolor=AMBER_LIGHT, edgecolor=AMBER, lw=1.6,
                          alpha=0.72, zorder=4))

    # Full pencil of Q-lines through P = (0.72, -0.15, 0) inside H_1
    P_d = np.array([0.72, -0.15, 0.0])
    for ang_d in (-65.0, -28.0, 8.0, 44.0, 80.0):
        dd = np.array([math.cos(math.radians(ang_d)), math.sin(math.radians(ang_d)), 0.0])
        seg = np.array([P_d - 0.65 * dd, P_d + 0.65 * dd])
        sx, sy, _ = cam_d(seg)
        axd.plot(sx, sy, color=BLUE, lw=2.2, zorder=5)

    t2x, t2y, _ = cam_d(h2_top)
    axd.add_patch(Polygon(np.column_stack([t2x, t2y]), closed=True,
                          facecolor=TEAL_LIGHT, edgecolor=TEAL, lw=1.3,
                          alpha=0.58, zorder=6))

    # Singular intersection line H_1 cap H_2 (x = z = 0)
    hinge = np.array([[0.0, -1.25, 0.0], [0.0, 1.25, 0.0]])
    hx, hy, _ = cam_d(hinge)
    axd.plot(hx, hy, color=AMBER, lw=3.3, zorder=7)

    pdx, pdy, _ = cam_d(P_d[None, :])
    axd.scatter(pdx[0], pdy[0], s=62, color=NAVY, edgecolor="white", lw=1.1, zorder=8)
    axd.text(pdx[0] + 0.16, pdy[0] - 0.18, r"$P \in H_1 \backslash H_2$",
             fontsize=8.9, fontweight="bold", color=NAVY, ha="left", va="top",
             bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.85),
             zorder=9)
    axd.text(-1.82, -0.82, r"$H_1 = \mathcal{Q}_P$" "\n" r"(pencil of $\mathcal{Q}$-lines)",
             fontsize=8.7, fontweight="bold", color=AMBER, ha="left", zorder=9)
    axd.text(-0.22, 1.15, r"$H_2$", fontsize=9.8, fontweight="bold", color=TEAL, zorder=9)
    axd.annotate(r"$H_1 \cap H_2$ (singular)",
                 xy=(0.62 * hx[1], 0.62 * hy[1]), xytext=(1.12, 0.85),
                 ha="center", va="bottom", fontsize=8.5, fontweight="bold", color=AMBER,
                 bbox=dict(boxstyle="round,pad=0.10", fc="white", ec=AMBER_LIGHT, lw=0.8),
                 arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2), zorder=9)

    save_fig(fig, out_dir, "maths3_quadsets_tangent_planes.png")


# ---------------------------------------------------------------------------
# Figure 5: Ovals in Odd (q=3) and Even (q=2) Order, with Nucleus
#           (maths3_quadsets_ovals_nucleus.png)
# ---------------------------------------------------------------------------
def norm_proj(vec, p_mod: int):
    for c in vec:
        if c % p_mod != 0:
            inv = pow(int(c % p_mod), -1, p_mod)
            return tuple(int((x * inv) % p_mod) for x in vec)
    raise ValueError("Zero vector")


def enumerate_pg2(p_mod: int):
    pts = sorted(set(
        norm_proj(v, p_mod)
        for v in itertools.product(range(p_mod), repeat=3)
        if any(v)
    ))
    lines = []
    for u in pts:
        L = tuple(sorted(
            x for x in pts
            if (u[0] * x[0] + u[1] * x[1] + u[2] * x[2]) % p_mod == 0
        ))
        lines.append((u, L))
    assert len(pts) == p_mod * p_mod + p_mod + 1
    assert len(lines) == p_mod * p_mod + p_mod + 1
    return pts, lines


def make_fig5_ovals_nucleus(out_dir: Path):
    # ---- Panel (a) math: PG(2, 3), conic x_0 x_2 - x_1^2 = 0 (mod 3) ----
    pts3, lines3 = enumerate_pg2(3)
    oval3 = [p for p in pts3 if (p[0] * p[2] - p[1] * p[1]) % 3 == 0]
    assert oval3 == [(0, 0, 1), (1, 0, 0), (1, 1, 1), (1, 2, 1)]

    tangents3 = []
    for _, L in lines3:
        hit = [p for p in L if p in oval3]
        assert len(hit) in (0, 1, 2)
        if len(hit) == 1:
            tangents3.append((hit[0], L))
    assert len(tangents3) == 4

    mult3 = {
        x: sum(1 for _, L in tangents3 if x in L)
        for x in pts3 if x not in oval3
    }
    assert sorted(mult3.values()) == [0, 0, 0, 2, 2, 2, 2, 2, 2]

    # ---- Panel (b) math: PG(2, 2), conic x_0 x_2 - x_1^2 = 0 (mod 2) ----
    pts2, lines2 = enumerate_pg2(2)
    oval2 = [p for p in pts2 if (p[0] * p[2] - p[1] * p[1]) % 2 == 0]
    assert set(oval2) == {(1, 0, 0), (0, 0, 1), (1, 1, 1)}

    tangents2 = []
    for coeff, L in lines2:
        hit = [p for p in L if p in oval2]
        assert len(hit) in (0, 1, 2)
        if len(hit) == 1:
            tangents2.append((hit[0], coeff, L))
    assert len(tangents2) == 3

    common_nucleus = set(tangents2[0][2]) & set(tangents2[1][2]) & set(tangents2[2][2])
    assert common_nucleus == {(0, 1, 0)}
    nucleus = (0, 1, 0)

    hyperoval2 = set(oval2) | {nucleus}
    assert len(hyperoval2) == 4
    passants_h = [ (c, L) for c, L in lines2 if len(set(L) & hyperoval2) == 0 ]
    secants_h  = [ (c, L) for c, L in lines2 if len(set(L) & hyperoval2) == 2 ]
    assert len(passants_h) == 1 and len(secants_h) == 6
    assert passants_h[0][0] == (1, 1, 1)  # x_0 + x_1 + x_2 = 0

    # Also verify embedding into plane x_1 = x_2 of Q^+(3, 2) (line 631)
    emb = lambda p: (p[0], p[1], p[1], p[2])
    for p in oval2:
        q4 = emb(p)
        assert (q4[0] * q4[3] - q4[1] * q4[2]) % 2 == 0
    nuc4 = emb(nucleus)
    assert nuc4 == (0, 1, 1, 0) and (nuc4[0] * nuc4[3] - nuc4[1] * nuc4[2]) % 2 == 1

    # ---- Draw Figure 5 ----
    fig = plt.figure(figsize=(11.4, 6.3), dpi=220)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.22, 1.0], wspace=0.06)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])

    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.axis("off")

    # ---------------- Panel (a): PG(2, 3) honest grid + tangent key ----------------
    ax1.set_xlim(-0.55, 6.55)
    ax1.set_ylim(-2.22, 4.15)
    draw_card(ax1, -0.50, -2.14, 7.00, 6.22, fc=GREY_BG, ec=GREY_LINE)
    ax1.text(3.00, 3.76,
             r"(a) Odd Order $q = 3$: Conic $\mathcal{O}$ in $\mathrm{PG}(2, 3)$ ($0$ or $2$ Tangents)",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    # Infinity bar x_0 = 0 at y = 2.95
    draw_card(ax1, -0.25, 2.52, 4.05, 0.90, fc="white", ec=GREY_LINE, lw=1.0, zorder=1)
    ax1.text(-0.14, 3.28, r"Line at infinity $x_0 = 0$",
             ha="left", va="center", fontsize=8.3, fontweight="bold", color=SLATE)
    inf3_pts = [(0, 1, 0), (0, 1, 1), (0, 1, 2), (0, 0, 1)]
    pos3 = {}
    for idx, p in enumerate(inf3_pts):
        pos3[p] = (0.30 + idx * 0.98, 2.95)

    # 3x3 affine grid x_0 = 1 below
    draw_card(ax1, -0.25, -0.32, 4.05, 2.72, fc="white", ec=GREY_LINE, lw=1.0, zorder=1)
    ax1.text(-0.14, 2.22, r"Affine grid $x_0 = 1$ ($x_1, x_2 \in \mathbb{F}_3$)",
             ha="left", va="center", fontsize=8.3, fontweight="bold", color=SLATE)
    for x1 in range(3):
        gx = 0.65 + x1 * 1.15
        ax1.plot([gx, gx], [0.15, 1.85], color="#e2e8f0", lw=0.9, ls=":", zorder=2)
    for x2 in range(3):
        gy = 0.18 + x2 * 0.84
        ax1.plot([0.65, 2.95], [gy, gy], color="#e2e8f0", lw=0.9, ls=":", zorder=2)
    for x1 in range(3):
        for x2 in range(3):
            pos3[(1, x1, x2)] = (0.65 + x1 * 1.15, 0.18 + x2 * 0.84)

    # Plot all 13 points styled by role (conic / 2 tangents / 0 tangents)
    for p, (px, py) in pos3.items():
        if p in oval3:
            ax1.add_patch(Circle((px, py), 0.165, facecolor=TEAL,
                                 edgecolor=NAVY, lw=1.8, zorder=6))
            ax1.text(px, py, r"$\mathcal{O}$", ha="center", va="center",
                     fontsize=8.6, fontweight="bold", color="white", zorder=7)
        elif mult3[p] == 2:
            ax1.add_patch(Circle((px, py), 0.155, facecolor=BLUE_LIGHT,
                                 edgecolor=BLUE, lw=1.8, zorder=6))
            ax1.text(px, py, "2", ha="center", va="center",
                     fontsize=9.0, fontweight="bold", color=BLUE, zorder=7)
        else:
            ax1.add_patch(Circle((px, py), 0.150, facecolor=GREY_BG,
                                 edgecolor=SLATE, lw=1.4, ls="--", zorder=6))
            ax1.text(px, py, "0", ha="center", va="center",
                     fontsize=8.8, fontweight="bold", color=SLATE, zorder=7)

        lbl_p = f"({p[0]}:{p[1]}:{p[2]})"
        ax1.text(px, py - 0.25, lbl_p, ha="center", va="top",
                 fontsize=7.7, color=TEXT, zorder=7)

    # Right legend box inside Panel (a)
    draw_card(ax1, 3.88, -0.32, 2.52, 3.74, fc="white", ec=GREY_LINE, lw=1.0, zorder=1)
    ax1.text(4.05, 3.16, "Point types:", ha="left", va="center",
             fontsize=9.2, fontweight="bold", color=TEXT)

    leg_items = [
        (2.74, TEAL, NAVY, "-", r"$\mathcal{O}$", "white", "Conic $\\mathcal{O}$ ($4$ pts)\n$1$ tangent each"),
        (2.04, BLUE_LIGHT, BLUE, "-", "2", BLUE, "On $2$ tangents\n($6$ points)"),
        (1.34, GREY_BG, SLATE, "--", "0", SLATE, "On $0$ tangents\n($3$ points)"),
    ]
    for ly, fc, ec, ls, sym, sc, desc in leg_items:
        ax1.add_patch(Circle((4.22, ly), 0.145, facecolor=fc, edgecolor=ec,
                             lw=1.6, linestyle=ls, zorder=5))
        ax1.text(4.22, ly, sym, ha="center", va="center",
                 fontsize=8.5, fontweight="bold", color=sc, zorder=6)
        ax1.text(4.48, ly, desc, ha="left", va="center", fontsize=8.4, color=TEXT)

    ax1.text(5.14, 0.42, "No $3$ tangents\nmeet at a point\n(no nucleus)",
             ha="center", va="center", fontsize=8.6, fontweight="bold", color=NAVY,
             bbox=dict(boxstyle="round,pad=0.20", fc=BLUE_PALE, ec="#bfdbfe", lw=0.9))

    # Bottom 4-tangent point-set key generated directly from computed tangents3 (4 clean full-width rows)
    draw_card(ax1, -0.25, -2.02, 6.65, 1.62, fc="white", ec=GREY_LINE, lw=1.0, zorder=1)
    tan_map = {pt: L for pt, L in tangents3}
    eq_specs = [
        ((1, 0, 0), r"$T_{(1:0:0)}\ (x_2 = 0)$"),
        ((0, 0, 1), r"$T_{(0:0:1)}\ (x_0 = 0)$"),
        ((1, 1, 1), r"$T_{(1:1:1)}\ (x_0 + x_1 + x_2 = 0)$"),
        ((1, 2, 1), r"$T_{(1:2:1)}\ (x_0 + 2x_1 + x_2 = 0)$"),
    ]
    ax1.text(-0.08, -0.60, "Four tangent lines (listed as $4$-point sets over $\\mathbb{F}_3$):",
             ha="left", va="center", fontsize=8.4, fontweight="bold", color=BLUE)
    for idx, (pt_t, eq_str) in enumerate(eq_specs):
        row_y = -0.90 - idx * 0.30
        pts_str = ",  ".join(f"({q[0]}:{q[1]}:{q[2]})" for q in tan_map[pt_t])
        ax1.text(-0.06, row_y, f"{eq_str}:   {{{pts_str}}}",
                 ha="left", va="center", fontsize=8.1, color=TEXT)

    # ---------------- Panel (b): PG(2, 2) Fano layout with Nucleus ----------------
    ax2.set_xlim(-2.76, 2.76)
    ax2.set_ylim(-2.74, 2.95)
    draw_card(ax2, -2.70, -2.66, 5.40, 5.54, fc=GREY_BG, ec=GREY_LINE)
    ax2.text(0.0, 2.55,
             r"(b) Even Order $q = 2$: Nucleus $N$ in $\mathrm{PG}(2, 2)$",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    # Place conic points at the 3 outer corners and nucleus N = (0:1:0) at centre!
    R2 = 1.82
    c_off = np.array([0.0, 0.25])
    pos2 = {
        (0, 1, 0): c_off + np.array([0.0, 0.0]),  # Nucleus N
        (1, 0, 0): c_off + R2 * np.array([math.cos(math.radians(90.0)),  math.sin(math.radians(90.0))]),
        (0, 0, 1): c_off + R2 * np.array([math.cos(math.radians(210.0)), math.sin(math.radians(210.0))]),
        (1, 1, 1): c_off + R2 * np.array([math.cos(math.radians(330.0)), math.sin(math.radians(330.0))]),
    }
    pos2[(1, 1, 0)] = 0.5 * (pos2[(0, 0, 1)] + pos2[(1, 1, 1)])  # on median x_2 = 0
    pos2[(0, 1, 1)] = 0.5 * (pos2[(1, 0, 0)] + pos2[(1, 1, 1)])  # on median x_0 = 0
    pos2[(1, 0, 1)] = 0.5 * (pos2[(1, 0, 0)] + pos2[(0, 0, 1)])  # on median x_0 + x_2 = 0

    # Verify geometrically that the 3 medians are the 3 tangents and the incircle is the passant!
    r2_in = 0.5 * R2
    for p in passants_h[0][1]:
        assert abs(np.linalg.norm(pos2[p] - c_off) - r2_in) < 1e-12

    # 3 outer sides (secants of O)
    corners2 = [(1, 0, 0), (0, 0, 1), (1, 1, 1)]
    for pA, pB in itertools.combinations(corners2, 2):
        ax2.plot([pos2[pA][0], pos2[pB][0]], [pos2[pA][1], pos2[pB][1]],
                 color=SLATE, lw=2.0, zorder=2)

    # Inscribed circle = unique passant line x_0 + x_1 + x_2 = 0 to hyperoval O u {N}
    th = np.linspace(0, 2 * np.pi, 360)
    ax2.plot(c_off[0] + r2_in * np.cos(th), c_off[1] + r2_in * np.sin(th),
             color=SLATE, lw=1.9, ls="--", zorder=3)
    for ang_deg in (90.0, 210.0, 330.0):
        gx = c_off[0] + r2_in * math.cos(math.radians(ang_deg))
        gy = c_off[1] + r2_in * math.sin(math.radians(ang_deg))
        ax2.add_patch(Circle((gx, gy), 0.095, facecolor=GREY_BG, edgecolor="none", zorder=4))

    # 3 tangent lines (medians) concurring at N = (0:1:0) in bold BLUE
    med_pairs = [
        ((1, 0, 0), (1, 1, 0), r"$x_2=0$"),
        ((0, 0, 1), (0, 1, 1), r"$x_0=0$"),
        ((1, 1, 1), (1, 0, 1), r"$x_0+x_2=0$"),
    ]
    for c_pt, m_pt, _ in med_pairs:
        ax2.plot([pos2[c_pt][0], pos2[m_pt][0]], [pos2[c_pt][1], pos2[m_pt][1]],
                 color=BLUE, lw=3.2, zorder=5)

    # Plot the 7 nodes
    ax2.add_patch(Circle(pos2[nucleus], 0.255, facecolor=AMBER_LIGHT,
                         edgecolor=AMBER, lw=1.5, ls="--", zorder=6))
    for p, xy in pos2.items():
        if p == nucleus:
            ax2.add_patch(Circle(xy, 0.185, facecolor=AMBER, edgecolor=TEXT, lw=1.8, zorder=8))
            ax2.text(xy[0], xy[1], "N", ha="center", va="center",
                     fontsize=10.0, fontweight="bold", color="white", zorder=9)
        elif p in oval2:
            ax2.add_patch(Circle(xy, 0.185, facecolor=TEAL, edgecolor=NAVY, lw=1.8, zorder=8))
            ax2.text(xy[0], xy[1], r"$\mathcal{O}$", ha="center", va="center",
                     fontsize=9.2, fontweight="bold", color="white", zorder=9)
        else:
            ax2.add_patch(Circle(xy, 0.145, facecolor="white", edgecolor=SLATE, lw=1.5, zorder=8))

    # Coordinate labels cleanly positioned outside every node
    lbl_offsets = {
        (1, 0, 0): (0.24, 0.10, "left"),
        (0, 0, 1): (-0.20, -0.24, "center"),
        (1, 1, 1): (0.20, -0.24, "center"),
        (0, 1, 0): (0.35, -0.04, "left"),
        (1, 1, 0): (0.0, -0.29, "center"),
        (0, 1, 1): (0.22, 0.12, "left"),
        (1, 0, 1): (-0.22, 0.12, "right"),
    }
    for p, (dx, dy, ha_align) in lbl_offsets.items():
        xy = pos2[p]
        prefix = "N = " if p == nucleus else ""
        col_t = AMBER if p == nucleus else (TEAL if p in oval2 else SLATE)
        fc_b = "white" if p == nucleus else GREY_BG
        ax2.text(xy[0] + dx, xy[1] + dy, f"{prefix}({p[0]}:{p[1]}:{p[2]})",
                 ha=ha_align, va="center", fontsize=8.4, fontweight="bold",
                 color=col_t,
                 bbox=dict(boxstyle="round,pad=0.09", fc=fc_b, ec="none", alpha=0.92),
                 zorder=10)

    # Bottom summary box explaining characteristic 2 & hyperoval (cleanly wrapped inside box)
    draw_card(ax2, -2.54, -2.54, 5.08, 1.52, fc="white", ec=GREY_LINE, lw=1.0, zorder=2)
    ax2.text(0.0, -1.32,
             r"In char $2$, tangent $t^2 x_0 + x_2 = 0$ loses its $x_1$ term ($2 = 0$),",
             ha="center", va="center", fontsize=8.0, fontweight="bold", color=BLUE)
    ax2.text(0.0, -1.62,
             r"so all $q + 1 = 3$ tangents concur at the nucleus $N = (0:1:0)$.",
             ha="center", va="center", fontsize=8.0, fontweight="bold", color=BLUE)
    ax2.text(0.0, -1.98,
             r"Hyperoval $\mathcal{O}\cup\{N\}$ ($4$ pts, no $3$ collinear):",
             ha="center", va="center", fontsize=7.9, color=TEXT)
    ax2.text(0.0, -2.28,
             r"$6$ secants ($2$ pts each), $1$ passant ($x_0 + x_1 + x_2 = 0$).",
             ha="center", va="center", fontsize=7.9, color=TEXT)

    save_fig(fig, out_dir, "maths3_quadsets_ovals_nucleus.png")


# ---------------------------------------------------------------------------
# Figure 6: Symplectic W(3, 3) Fan + Real Propeller
#           (maths3_polar_symplectic_fan.png)
# ---------------------------------------------------------------------------
def symp_f3(x, y) -> int:
    return (x[0] * y[1] - x[1] * y[0] + x[2] * y[3] - x[3] * y[2]) % 3


def make_fig6_symplectic_fan(out_dir: Path):
    # ---- Enumerate PG(3, 3) and W(3, 3) ----
    pts_pg33 = sorted(set(
        norm_proj(v, 3)
        for v in itertools.product(range(3), repeat=4)
        if any(v)
    ))
    assert len(pts_pg33) == (3**4 - 1) // (3 - 1) == 40
    for x in pts_pg33:
        assert symp_f3(x, x) == 0  # every point is isotropic

    lines_pg33 = set()
    symp_lines = set()
    for u, v in itertools.combinations(pts_pg33, 2):
        L = tuple(sorted(set(
            norm_proj(tuple((a * u[k] + b * v[k]) % 3 for k in range(4)), 3)
            for a, b in itertools.product(range(3), repeat=2)
            if (a, b) != (0, 0)
        )))
        assert len(L) == 4
        lines_pg33.add(L)
        if symp_f3(u, v) == 0:
            for p1, p2 in itertools.combinations(L, 2):
                assert symp_f3(p1, p2) == 0
            symp_lines.add(L)
    assert len(lines_pg33) == 130
    assert len(symp_lines) == 40

    P = (1, 0, 0, 0)
    P_pi = sorted(x for x in pts_pg33 if symp_f3(P, x) == 0)
    assert len(P_pi) == 13 and P in P_pi
    assert all(x[1] == 0 for x in P_pi)

    lines_in_Ppi = [L for L in lines_pg33 if set(L).issubset(P_pi)]
    lines_thru_P = [L for L in lines_pg33 if P in L]
    pencil_P = [L for L in lines_in_Ppi if P in L]
    assert len(lines_in_Ppi) == 13
    assert len(lines_thru_P) == 13
    assert len(pencil_P) == 4
    assert set(pencil_P) == (set(lines_in_Ppi) & symp_lines)
    assert set(pencil_P) == (set(lines_thru_P) & symp_lines)

    # Screen line y_0 = y_1 = 0 inside P^pi
    Q_screen = [
        (0, 0, 1, 0),  # Q_1 = R
        (0, 0, 0, 1),  # Q_2 = S
        (0, 0, 1, 1),  # Q_3
        (0, 0, 1, 2),  # Q_4
    ]
    R_pt, S_pt = Q_screen[0], Q_screen[1]
    assert symp_f3(R_pt, S_pt) == 1  # RS is NOT a symplectic line!
    assert tuple(sorted(Q_screen)) in lines_in_Ppi
    assert tuple(sorted(Q_screen)) not in symp_lines

    rays_pts = []
    seen = {P}
    for Qi in Q_screen:
        p_mid1 = norm_proj(tuple((P[k] + Qi[k]) % 3 for k in range(4)), 3)
        p_mid2 = norm_proj(tuple((P[k] + 2 * Qi[k]) % 3 for k in range(4)), 3)
        ray = [P, p_mid1, p_mid2, Qi]
        assert tuple(sorted(ray)) in symp_lines
        rays_pts.append(ray)
        seen.update(ray)
    assert seen == set(P_pi)  # all 13 points of P^pi accounted for honestly!

    # ---- Verify Panel (b) real null-plane normal (1, -c, b) in chart x_0 = 1 ----
    for a, b, c in [(-0.5, -1.5, 0.4), (0.0, -0.8, 0.0), (0.0, 1.6, 0.0), (1.1, 0.3, -0.7)]:
        n_vec = np.array([1.0, -c, b])
        X_aff = np.array([a, b, c])
        for dy in [np.array([c * 0.7 - b * 0.3, 0.7, 0.3]), np.array([0.5, -0.4, 0.9])]:
            Y_aff = X_aff + dy
            f_real = 1.0 * Y_aff[0] - a * 1.0 + b * Y_aff[2] - c * Y_aff[1]
            assert abs(f_real - np.dot(n_vec, Y_aff - X_aff)) < 1e-12

    # ---- Draw Figure 6 ----
    fig = plt.figure(figsize=(11.4, 5.5), dpi=220)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.12, 1.0], wspace=0.06)
    ax1 = fig.add_subplot(gs[0])
    ax2 = fig.add_subplot(gs[1])
    for ax in (ax1, ax2):
        ax.set_aspect("equal")
        ax.axis("off")

    # ---------------- Panel (a): Flat projective fan inside P^pi ----------------
    ax1.set_xlim(-2.95, 2.95)
    ax1.set_ylim(-2.15, 2.95)
    draw_card(ax1, -2.90, -2.08, 5.80, 4.95, fc=GREY_BG, ec=GREY_LINE)
    ax1.text(0.0, 2.58,
             r"(a) Polar Plane $P^\pi$ ($y_1 = 0$) in $W(3, 3)$: $4$ Symplectic Lines",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    # Inner polar plane card P^pi
    draw_card(ax1, -2.68, -1.36, 5.36, 3.62, fc=AMBER_LIGHT, ec=AMBER,
              lw=1.5, alpha=0.52, zorder=1)
    ax1.text(-2.50, 2.02, r"$P^\pi : y_1 = 0$ ($\cong \mathrm{PG}(2, 3)$, $13$ points)",
             ha="left", va="center", fontsize=8.7, fontweight="bold", color=AMBER)

    P_xy = np.array([-0.52, 1.38])
    qx_list = [-2.12, -0.78, 0.65, 2.08]
    y_scr = -0.82

    # Ambient lines leaving P^pi stub at P (routed below header, into open top-right card space)
    for dx_out, dy_out in [(1.02, 0.30), (1.12, 0.04)]:
        ax1.plot([P_xy[0], P_xy[0] + dx_out], [P_xy[1], P_xy[1] + dy_out],
                 color=RED, lw=1.7, ls="--", zorder=3)
    ax1.text(P_xy[0] + 1.18, P_xy[1] + 0.16,
             r"$9$ lines through $P$" "\n" r"leave $P^\pi$ ($f \neq 0$)",
             ha="left", va="center", fontsize=8.3, fontweight="bold", color=RED,
             bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=RED_LIGHT, lw=0.8),
             zorder=8)

    # Screen line L = RS (y_0 = y_1 = 0) across bottom in dashed RED
    ax1.plot([-2.48, 2.48], [y_scr, y_scr], color=RED, lw=2.6, ls="--", zorder=4)
    ax1.text(0.0, -1.68,
             r"Screen line $RS$ ($y_0 = y_1 = 0$): $f(R, S) = 1 \neq 0$," "\n"
             r"so $RS \notin W(3, 3)$ ($9$ lines in $P^\pi$ miss $P$)",
             ha="center", va="center", fontsize=8.35, fontweight="bold", color=RED)

    # 4 solid BLUE symplectic lines PQ_1 .. PQ_4 and all 13 discrete points
    q_labels = [
        r"$Q_1 = R$" "\n" r"$(0,0,1,0)$",
        r"$Q_2 = S$" "\n" r"$(0,0,0,1)$",
        r"$Q_3$" "\n" r"$(0,0,1,1)$",
        r"$Q_4$" "\n" r"$(0,0,1,2)$",
    ]
    # Staggered fractions and side-alignments so all 8 intermediate 4-tuples sit in open space
    mid_specs = [
        [(0.34, -0.10, "right"), (0.66, -0.10, "right")],
        [(0.45, -0.08, "right"), (0.72,  0.09, "left")],
        [(0.34,  0.09, "left"),  (0.64,  0.09, "left")],
        [(0.46,  0.10, "left"),  (0.73,  0.10, "left")],
    ]
    for idx, ray in enumerate(rays_pts):
        Q_xy = np.array([qx_list[idx], y_scr])
        ext_xy = P_xy + 1.07 * (Q_xy - P_xy)
        ax1.plot([P_xy[0], ext_xy[0]], [P_xy[1], ext_xy[1]],
                 color=BLUE, lw=2.8, zorder=5)

        for (frac, dx_lbl, ha_lbl), pt_m in zip(mid_specs[idx], [ray[1], ray[2]]):
            m_xy = P_xy + frac * (Q_xy - P_xy)
            ax1.scatter(m_xy[0], m_xy[1], s=42, color=NAVY,
                        edgecolor="white", lw=0.9, zorder=7)
            coord_s = f"({pt_m[0]},{pt_m[1]},{pt_m[2]},{pt_m[3]})"
            ax1.text(m_xy[0] + dx_lbl, m_xy[1], coord_s,
                     ha=ha_lbl, va="center", fontsize=6.9, color=TEXT,
                     bbox=dict(boxstyle="round,pad=0.05", fc="white",
                               ec="none", alpha=0.84), zorder=7)

        # Screen point Q_i
        is_RS = idx in (0, 1)
        ax1.scatter(Q_xy[0], Q_xy[1], s=60, color=NAVY,
                    edgecolor=RED if is_RS else "white",
                    lw=1.6 if is_RS else 1.0, zorder=8)
        ax1.text(Q_xy[0], Q_xy[1] - 0.16, q_labels[idx],
                 ha="center", va="top", fontsize=7.9,
                 fontweight="bold", color=RED if is_RS else NAVY, zorder=9)

    # Pole P
    ax1.scatter(P_xy[0], P_xy[1], s=84, color=AMBER, edgecolor=TEXT, lw=1.3, zorder=9)
    ax1.text(P_xy[0] - 0.16, P_xy[1] + 0.04,
             r"Pole $P = \langle(1,0,0,0)\rangle$",
             ha="right", va="center", fontsize=8.9, fontweight="bold", color=NAVY,
             bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.88),
             zorder=10)

    # ---------------- Panel (b): Real propeller in chart x_0 = 1 ----------------
    ax2.set_xlim(-2.65, 2.65)
    ax2.set_ylim(-2.15, 2.95)
    draw_card(ax2, -2.60, -2.08, 5.20, 4.95, fc=GREY_BG, ec=GREY_LINE)
    ax2.text(0.0, 2.58,
             r"(b) Real Analogue ($\mathrm{PG}(3, \mathbb{R})$, $x_0 = 1$): Propeller",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    # Map real chart coordinates (y_1, y_2, y_3) with stretched y_2 spacing so 5 blades never collide
    cam_p = make_3d_cam(azim_deg=-26.0, elev_deg=21.0)

    def map_real(pts_y):
        scaled = np.asarray(pts_y, dtype=float).copy()
        if scaled.ndim == 1:
            scaled[1] *= 1.32
        else:
            scaled[:, 1] *= 1.32
        px, py, dep = cam_p(scaled)
        return px, py + 0.24, dep

    # Spine line X(b) = (1, 0, b, 0) along y_2 axis
    spine = np.array([[0.0, -1.98, 0.0], [0.0, 1.98, 0.0]])
    spx, spy, _ = map_real(spine)
    ax2.plot(spx, spy, color=NAVY, lw=2.3, zorder=3)
    ax2.text(spx[0] + 0.05, spy[0] - 0.22, r"Line $X = (1, 0, b, 0)$",
             ha="left", va="top", fontsize=8.8, fontweight="bold", color=NAVY)

    b_vals = [-1.5, -0.75, 0.0, 0.75, 1.5]
    patches_data = []
    for b in b_vals:
        center = np.array([0.0, b, 0.0])
        u_ax = np.array([0.0, 1.0, 0.0])
        w_blade = np.array([-b, 0.0, 1.0]) / math.hypot(1.0, b)
        du, dw = 0.23, 0.80
        corners = np.array([
            center - du * u_ax - dw * w_blade,
            center + du * u_ax - dw * w_blade,
            center + du * u_ax + dw * w_blade,
            center - du * u_ax + dw * w_blade,
        ])
        _, _, dep = map_real(center[None, :])
        patches_data.append((dep[0], b, center, u_ax, w_blade, corners))

    patches_data.sort(key=lambda item: item[0])
    for idx_z, (_, b, center, u_ax, w_blade, corners) in enumerate(patches_data):
        z_base = 4 + 2 * idx_z
        cx, cy, _ = map_real(corners)
        ax2.add_patch(Polygon(np.column_stack([cx, cy]), closed=True,
                              facecolor=AMBER_LIGHT, edgecolor=AMBER,
                              lw=1.35, alpha=0.74, zorder=z_base))
        for ang_f in (-60.0, -24.0, 24.0, 60.0):
            af = math.radians(ang_f)
            dir_f = 0.21 * math.sin(af) * u_ax + 0.72 * math.cos(af) * w_blade
            fx, fy, _ = map_real(np.array([center - dir_f, center + dir_f]))
            ax2.plot(fx, fy, color=BLUE, lw=1.65, zorder=z_base + 1)

        px0, py0, _ = map_real(center[None, :])
        ax2.scatter(px0[0], py0[0], s=46, color=AMBER, edgecolor=TEXT,
                    lw=1.0, zorder=z_base + 1)
        top_mid = 0.5 * (corners[2] + corners[3]) + 0.14 * w_blade
        tx_b, ty_b, _ = map_real(top_mid[None, :])
        b_txt = r"$b=0$" if b == 0.0 else rf"$b={b:+.2g}$"
        ax2.text(tx_b[0], ty_b[0] + 0.06, b_txt,
                 ha="center", va="bottom", fontsize=7.8, fontweight="bold",
                 color=AMBER,
                 bbox=dict(boxstyle="round,pad=0.06", fc=GREY_BG, ec="none", alpha=0.86),
                 zorder=22)

    ax2.text(0.0, -1.58,
             r"Null plane $X^\pi$ through $(a,b,c)$ has normal $(1, -c, b)$:" "\n"
             r"along $X = (1, 0, b, 0)$, normal $(1, 0, b)$ twists with $b$",
             ha="center", va="center", fontsize=8.4, color=TEXT,
             bbox=dict(boxstyle="round,pad=0.22", fc="white", ec=GREY_LINE, lw=0.9))

    save_fig(fig, out_dir, "maths3_polar_symplectic_fan.png")


# ---------------------------------------------------------------------------
# Figure 7: Hermitian Curve H(2, 9) in PG(2, 9)
#           (maths3_polar_hermitian_pg29.png)
# ---------------------------------------------------------------------------
def f9_add(z1, z2):
    return ((z1[0] + z2[0]) % 3, (z1[1] + z2[1]) % 3)


def f9_mul(z1, z2):
    # (a + b i)(c + d i) with i^2 = 2 (mod 3)
    a, b = z1
    c, d = z2
    return ((a * c + 2 * b * d) % 3, (a * d + b * c) % 3)


def f9_conj(z):
    # Frobenius z^3 = a - b i = (a, -b mod 3)
    z3 = f9_mul(f9_mul(z, z), z)
    conj = (z[0] % 3, (-z[1]) % 3)
    assert z3 == conj
    return conj


def f9_inv(z):
    assert z != (0, 0)
    for w in itertools.product(range(3), repeat=2):
        if w != (0, 0) and f9_mul(z, w) == (1, 0):
            return w
    raise ValueError("No inverse")


def f9_label(z) -> str:
    a, b = z
    if z == (0, 0):
        return "0"
    parts = []
    if a != 0:
        parts.append(str(a))
    if b == 1:
        parts.append("+i" if parts else "i")
    elif b == 2:
        parts.append("-i")
    return "".join(parts)


def make_fig7_hermitian_pg29(out_dir: Path):
    # Trace-ordered elements of F_9 so Baer triples {c, c+i, c-i} group cleanly
    f9_elems = [
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
    ]
    assert len(set(f9_elems)) == 9

    def norm_pg29(v):
        for c in v:
            if c != (0, 0):
                inv = f9_inv(c)
                return tuple(f9_mul(inv, x) for x in v)
        raise ValueError("Zero vector")

    pts91 = []
    seen = set()
    for v in itertools.product(f9_elems, repeat=3):
        if v == ((0, 0), (0, 0), (0, 0)):
            continue
        nv = norm_pg29(v)
        if nv not in seen:
            seen.add(nv)
            pts91.append(nv)
    assert len(pts91) == 9**2 + 9 + 1 == 91

    # Split Hermitian form from lines 2633-2689: f(x, y) = x_0^3 y_1 + x_1^3 y_0 + x_2^3 y_2
    def herm_f(x, y):
        t0 = f9_mul(f9_conj(x[0]), y[1])
        t1 = f9_mul(f9_conj(x[1]), y[0])
        t2 = f9_mul(f9_conj(x[2]), y[2])
        return f9_add(f9_add(t0, t1), t2)

    H_pts = {x for x in pts91 if herm_f(x, x) == (0, 0)}
    assert len(H_pts) == 3**3 + 1 == 28

    # Check polar lines across all 91 points -> 91 distinct lines splitting 28 / 63 / 0
    polar_lines = {}
    counts_dist = {0: 0, 1: 0, 4: 0}
    for pole in pts91:
        L = frozenset(y for y in pts91 if herm_f(pole, y) == (0, 0))
        assert len(L) == 10
        polar_lines[pole] = L
        nh = len(L & H_pts)
        assert nh in (1, 4), f"Unexpected intersection size {nh}"
        counts_dist[nh] += 1
    assert len(set(polar_lines.values())) == 91
    assert counts_dist == {0: 0, 1: 28, 4: 63}

    # Check worked poles P = <(1,0,0)> and Q = <(0,0,1)>
    F0, F1, FI, FMI = (0, 0), (1, 0), (0, 1), (0, 2)
    P_pole = (F1, F0, F0)
    Q_pole = (F0, F0, F1)
    assert P_pole in H_pts and Q_pole not in H_pts

    P_pi = polar_lines[P_pole]  # y_1 = 0
    Q_pi = polar_lines[Q_pole]  # y_2 = 0
    assert (P_pi & H_pts) == {P_pole}
    expected_baer = {
        (F1, F0, F0),
        (F1, FI, F0),
        (F1, FMI, F0),
        (F0, F1, F0),
    }
    assert (Q_pi & H_pts) == expected_baer

    # Check affine vs infinity split of H_pts
    inf_pts = [ (F0, F0, F1) ] + [ (F0, F1, m) for m in f9_elems ]
    assert len(inf_pts) == 10 and set(inf_pts).issubset(pts91)
    assert (set(inf_pts) & H_pts) == {(F0, F1, F0)}
    for y2 in f9_elems:
        row_h = [y1 for y1 in f9_elems if (F1, y1, y2) in H_pts]
        assert len(row_h) == 3

    # ---- Draw Figure 7 ----
    fig, ax = setup_canvas(11.5, 7.5, xlim=(-1.92, 14.50), ylim=(-1.35, 11.15))
    draw_card(ax, -1.82, -1.25, 16.20, 12.28, fc=GREY_BG, ec=GREY_LINE)

    ax.text(6.28, 10.62,
            r"Split Hermitian Curve $H(2, 9) : x_0^3 x_1 + x_1^3 x_0 + x_2^4 = 0$ in $\mathrm{PG}(2, 9)$ ($91$ Points, $28$ Isotropic)",
            ha="center", va="center", fontsize=10.3, fontweight="bold", color=TEXT)

    # Top strip: 10-point line at infinity y_0 = 0 (with Q = <(0,0,1)> aligned at x = 0 above column y_1 = 0!)
    y_inf = 9.05
    draw_card(ax, -0.82, 8.28, 9.45, 1.82, fc="white", ec=GREY_LINE, lw=1.1, zorder=1)
    ax.text(-0.62, 9.84,
            r"Line at infinity $y_0 = 0$ ($10$ points: $Q=\langle(0,0,1)\rangle$ and $\langle(0,1,m)\rangle$, $m \in \mathbb{F}_9$)",
            ha="left", va="center", fontsize=8.3, fontweight="bold", color=SLATE)

    # Main 9x9 affine grid box y_0 = 1 (x = 0..8 for y_1, y = 0..8 for y_2, scaled cleanly)
    sx, sy = 0.92, 0.80
    draw_card(ax, -0.82, -0.62, 9.45, 8.68, fc="white", ec=GREY_LINE, lw=1.1, zorder=1)

    # Highlight straight column P^pi : y_1 = 0 (extends straight up to Q = <(0,0,1)> at x = 0, y = y_inf!)
    ax.add_patch(FancyBboxPatch(
        (-0.32, -0.32), 0.64, y_inf + 0.64,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        facecolor=AMBER_LIGHT, edgecolor=AMBER, lw=1.6, alpha=0.72, zorder=2
    ))

    # Highlight straight horizontal row Q^pi : y_2 = 0 (plus matching blue badge on <(0,1,0)> at infinity)
    ax.add_patch(FancyBboxPatch(
        (-0.32, -0.30), 8 * sx + 0.64, 0.60,
        boxstyle="round,pad=0.02,rounding_size=0.14",
        facecolor=BLUE_LIGHT, edgecolor=BLUE, lw=1.6, alpha=0.72, zorder=2
    ))

    # Subtle 3x3 coset block grid lines
    for i in range(9):
        ax.plot([i * sx, i * sx], [0, 8 * sy], color="#f1f5f9", lw=0.8, zorder=2)
        ax.plot([0, 8 * sx], [i * sy, i * sy], color="#f1f5f9", lw=0.8, zorder=2)
    for sep in (2.5, 5.5):
        ax.plot([sep * sx, sep * sx], [-0.20, 8 * sy + 0.20],
                color="#e2e8f0", lw=1.0, ls=":", zorder=2)

    # Axis tick labels for y_1 and y_2
    for idx, z in enumerate(f9_elems):
        ax.text(idx * sx, -0.45, f9_label(z), ha="center", va="center",
                fontsize=8.3, fontweight="bold" if idx == 0 else "normal",
                color=AMBER if idx == 0 else TEXT)
        ax.text(-0.56, idx * sy, f9_label(z), ha="center", va="center",
                fontsize=8.3, fontweight="bold" if idx == 0 else "normal",
                color=BLUE if idx == 0 else TEXT)

    ax.text(4 * sx, -0.92, r"Affine coordinate $y_1 \in \mathbb{F}_9$ ($y_0 = 1$)",
            ha="center", va="center", fontsize=9.2, fontweight="bold", color=TEXT)
    ax.text(-1.40, 4 * sy, r"Affine coordinate $y_2 \in \mathbb{F}_9$ ($y_0 = 1$)",
            ha="center", va="center", fontsize=9.2, fontweight="bold",
            color=TEXT, rotation=90)

    # Plot all 81 affine points as discrete dots
    for ix, y1 in enumerate(f9_elems):
        for iy, y2 in enumerate(f9_elems):
            pt = (F1, y1, y2)
            px, py = ix * sx, iy * sy
            if pt == P_pole:
                ax.add_patch(Circle((px, py), 0.23, facecolor=AMBER_LIGHT,
                                    edgecolor=AMBER, lw=1.8, zorder=5))
            if pt in (Q_pi & H_pts):
                ax.add_patch(Circle((px, py), 0.21, facecolor="none",
                                    edgecolor=BLUE, lw=2.0, zorder=6))
            if pt in H_pts:
                ax.scatter(px, py, s=68, color=TEAL, edgecolor=NAVY, lw=1.2, zorder=7)
            else:
                ax.scatter(px, py, s=34, facecolor="white", edgecolor="#94a3b8",
                           lw=1.1, zorder=5)

    # Label P = <(1,0,0)> cleanly inside open grid space (well left of (1, i) at x = 2.76!)
    ax.annotate(r"$P = \langle(1,0,0)\rangle$",
                xy=(0.16, 0.16), xytext=(0.56, 1.16),
                fontsize=8.5, fontweight="bold", color=AMBER,
                bbox=dict(boxstyle="round,pad=0.11", fc="white", ec=AMBER, lw=0.9),
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.3), zorder=10)

    # Plot the 10 points on y_0 = 0 cleanly spaced with non-overlapping labels
    inf_x_step = 0.90
    for idx, pt in enumerate(inf_pts):
        px = idx * inf_x_step
        py = y_inf
        if pt == Q_pole:
            ax.scatter(px, py, s=74, color=RED_LIGHT, edgecolor=RED, lw=2.0, zorder=8)
            ax.text(px, py - 0.36, r"$Q$", ha="center", va="center",
                    fontsize=8.3, fontweight="bold", color=RED)
            ax.text(px, py - 0.62, "(0,0,1)", ha="center", va="center",
                    fontsize=6.3, fontweight="bold", color=RED)
        elif pt == (F0, F1, F0):
            ax.add_patch(FancyBboxPatch(
                (px - 0.26, py - 0.25), 0.52, 0.50,
                boxstyle="round,pad=0.02,rounding_size=0.12",
                facecolor=BLUE_LIGHT, edgecolor=BLUE, lw=1.6, zorder=4
            ))
            ax.add_patch(Circle((px, py), 0.21, facecolor="none",
                                edgecolor=BLUE, lw=2.0, zorder=6))
            ax.scatter(px, py, s=72, color=TEAL, edgecolor=NAVY, lw=1.2, zorder=8)
            ax.text(px + 0.12, py + 0.42, r"$4$th pt of $Q^\pi$",
                    ha="center", va="center", fontsize=7.3, fontweight="bold", color=BLUE)
            ax.text(px, py - 0.38, "m=0", ha="center", va="center",
                    fontsize=7.3, fontweight="bold", color=BLUE)
            ax.text(px, py - 0.62, "(0,1,0)", ha="center", va="center",
                    fontsize=6.6, fontweight="bold", color=BLUE)
        else:
            m_lbl = f9_label(pt[2])
            ax.scatter(px, py, s=36, facecolor="white", edgecolor="#94a3b8",
                       lw=1.1, zorder=6)
            ax.text(px, py - 0.38, f"m={m_lbl}", ha="center", va="center",
                    fontsize=6.7, color=SLATE)

    # Right-side explanation & 91-line audit card (widened so zero text touches right border)
    rx, ry, rw, rh = 8.82, -0.62, 5.40, 10.72
    draw_card(ax, rx, ry, rw, rh, fc="white", ec=GREY_LINE, lw=1.1, zorder=1)

    ax.text(rx + 0.25, ry + rh - 0.48, "Point & Line Audit",
            ha="left", va="center", fontsize=10.5, fontweight="bold", color=TEXT)

    # Point legend
    ax.scatter(rx + 0.42, ry + rh - 1.05, s=68, color=TEAL, edgecolor=NAVY, lw=1.2, zorder=5)
    ax.text(rx + 0.72, ry + rh - 1.05,
            r"Isotropic points of $H(2, 9)$:" "\n"
            r"$q^3 + 1 = 28$ ($27$ affine + $1$ on $y_0=0$)",
            ha="left", va="center", fontsize=8.6, color=TEXT)

    ax.scatter(rx + 0.42, ry + rh - 1.82, s=38, facecolor="white",
               edgecolor="#94a3b8", lw=1.2, zorder=5)
    ax.text(rx + 0.72, ry + rh - 1.82,
            r"Non-isotropic points of $\mathrm{PG}(2, 9)$:" "\n"
            r"$91 - 28 = 63$ points",
            ha="left", va="center", fontsize=8.6, color=TEXT)

    # Worked line 1: P^pi
    draw_card(ax, rx + 0.20, ry + rh - 4.25, rw - 0.40, 1.92,
              fc=AMBER_LIGHT, ec=AMBER, lw=1.2, alpha=0.55, zorder=2)
    ax.text(rx + 0.38, ry + rh - 2.68,
            r"Tangent polar line $P^\pi$ ($y_1 = 0$)",
            ha="left", va="center", fontsize=9.1, fontweight="bold", color=AMBER)
    ax.text(rx + 0.38, ry + rh - 3.45,
            r"Pole $P = \langle(1,0,0)\rangle \in H(2, 9)$." "\n"
            r"Vertical column ($9$ affine pts) plus" "\n"
            r"$Q = \langle(0,0,1)\rangle$ on $y_0 = 0$:" "\n"
            r"meets $H(2, 9)$ in $1$ point ($P$ alone).",
            ha="left", va="center", fontsize=8.2, color=TEXT)

    # Worked line 2: Q^pi
    draw_card(ax, rx + 0.20, ry + rh - 6.85, rw - 0.40, 2.42,
              fc=BLUE_PALE, ec=BLUE, lw=1.2, zorder=2)
    ax.text(rx + 0.38, ry + rh - 4.78,
            r"Secant polar line $Q^\pi$ ($y_2 = 0$)",
            ha="left", va="center", fontsize=9.1, fontweight="bold", color=BLUE)
    ax.text(rx + 0.38, ry + rh - 5.82,
            r"Pole $Q = \langle(0,0,1)\rangle \notin H(2, 9)$." "\n"
            r"Horizontal row ($9$ affine pts) plus" "\n"
            r"$\langle(0,1,0)\rangle$ on $y_0 = 0$: meets $H(2, 9)$ in" "\n"
            r"$q + 1 = 4$ points (Baer subline $\mathrm{PG}(1,3)$):" "\n"
            r"$\langle(1,0,0)\rangle, \langle(1,i,0)\rangle, \langle(1,-i,0)\rangle, \langle(0,1,0)\rangle$.",
            ha="left", va="center", fontsize=8.05, color=TEXT)

    # Global 91-line summary box
    draw_card(ax, rx + 0.20, ry + 0.25, rw - 0.40, 2.95,
              fc=GREY_BG, ec=GREY_LINE, lw=1.1, zorder=2)
    ax.text(rx + 0.38, ry + 2.82, r"All $91$ lines of $\mathrm{PG}(2, 9)$:",
            ha="left", va="center", fontsize=9.1, fontweight="bold", color=NAVY)

    bars = [
        (ry + 2.15, 28, AMBER, r"$28$ tangents ($1$ point)"),
        (ry + 1.40, 63, BLUE,  r"$63$ secants ($4$ points)"),
        (ry + 0.65,  0, SLATE, r"$0$ passants ($0$ points)"),
    ]
    for by, val, col, lbl in bars:
        ax.text(rx + 0.38, by + 0.18, lbl, ha="left", va="center",
                fontsize=8.3, fontweight="bold", color=col)
        w_bar = max(0.04, (val / 63.0) * (rw - 0.85))
        ax.add_patch(FancyBboxPatch(
            (rx + 0.38, by - 0.18), w_bar, 0.18,
            boxstyle="round,pad=0.01,rounding_size=0.05",
            facecolor=col if val > 0 else "#e2e8f0", edgecolor="none", zorder=4
        ))

    save_fig(fig, out_dir, "maths3_polar_hermitian_pg29.png")


# ---------------------------------------------------------------------------
# Figure 8: Point-Count Partition Across Q, W, H
#           (maths3_polar_point_count.png)
# ---------------------------------------------------------------------------
def make_fig8_point_count(out_dir: Path):
    # ---- Verify inside/outside partition numerically on concrete spaces ----
    # 1. Q^+(3, 3): d = 3, Q = q = 3, |Q^+(1, 3)| = 2
    pts33 = sorted(set(
        norm_proj(v, 3) for v in itertools.product(range(3), repeat=4) if any(v)
    ))
    Q33 = [x for x in pts33 if (x[0] * x[3] - x[1] * x[2]) % 3 == 0]
    P_q = (1, 0, 0, 0)
    P_perp_q = {x for x in pts33 if x[3] == 0}  # polar of (1,0,0,0) in x0 y3 + x3 y0 - x1 y2 - x2 y1
    in_q = [x for x in Q33 if x in P_perp_q]
    out_q = [x for x in Q33 if x not in P_perp_q]
    assert len(in_q) == 1 + 3 * 2 == 7
    assert len(out_q) == 3**(3 - 1) * 1 == 9
    assert len(Q33) == 16

    # 2. W(3, 3): d = 3, Q = q = 3, |W(1, 3)| = 4
    in_w = [x for x in pts33 if symp_f3(P_q, x) == 0]
    out_w = [x for x in pts33 if symp_f3(P_q, x) != 0]
    assert len(in_w) == 1 + 3 * 4 == 13
    assert len(out_w) == 3**(3 - 1) * 3 == 27
    assert len(in_w) + len(out_w) == 40

    # 3. H(2, 9) at d = 2, q = 3, Q = 9 (|H_0| = 0): 1 inside P^perp, 9 * 3 = 27 outside
    assert 1 + 9 * 0 + 3 * (9 ** (2 - 1)) == 28

    # ---- Draw Figure 8 ----
    fig = plt.figure(figsize=(11.6, 5.5), dpi=220)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.42], wspace=0.05)
    axL = fig.add_subplot(gs[0])
    axR = fig.add_subplot(gs[1])
    for ax in (axL, axR):
        ax.set_aspect("equal")
        ax.axis("off")

    # ---------------- Left panel: Simplified 4-label schematic ----------------
    axL.set_xlim(0.0, 5.05)
    axL.set_ylim(0.0, 5.35)
    draw_card(axL, 0.05, 0.05, 4.95, 5.25, fc=GREY_BG, ec=GREY_LINE)
    axL.text(2.52, 4.92,
             r"Two-Zone Partition Around $P$ (Schematic)",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    # Tangent hyperplane box P^perp on the left, with P near its right boundary
    # so secant lines L outside P^perp radiate rightward meeting P^perp ONLY at P!
    draw_card(axL, 0.26, 0.85, 2.74, 3.68, fc=AMBER_LIGHT, ec=AMBER,
              lw=1.7, alpha=0.68, zorder=1)
    axL.text(0.46, 4.22, r"$P^\perp$", ha="left", va="center",
             fontsize=12.0, fontweight="bold", color=AMBER)

    P_pos = np.array([2.72, 2.68])

    # Base oval P_{d-2} on left side inside P^perp
    th = np.linspace(0, 2 * np.pi, 240)
    ov_cx, ov_cy, ov_rx, ov_ry = 0.96, 2.58, 0.34, 0.86
    axL.fill(ov_cx + ov_rx * np.cos(th), ov_cy + ov_ry * np.sin(th),
             color=TEAL_LIGHT, alpha=0.80, zorder=2)
    axL.plot(ov_cx + ov_rx * np.cos(th), ov_cy + ov_ry * np.sin(th),
             color=TEAL, lw=2.2, zorder=3)
    axL.text(ov_cx, ov_cy + ov_ry + 0.14, r"$\mathcal{P}_{d-2}$",
             ha="center", va="bottom", fontsize=10.6, fontweight="bold", color=TEAL)

    # Faint cone envelope + one highlighted cone line <P, Y> fanning leftward inside P^perp
    for dy_c in (-0.80, 0.80):
        tgt = np.array([ov_cx + 0.06, ov_cy + dy_c])
        axL.plot([P_pos[0], tgt[0]], [P_pos[1], tgt[1]],
                 color=BLUE, lw=1.2, alpha=0.36, zorder=3)

    Y_pos = np.array([ov_cx - 0.04, ov_cy + 0.18])
    cone_end = P_pos + 1.06 * (Y_pos - P_pos)
    axL.plot([P_pos[0], cone_end[0]], [P_pos[1], cone_end[1]],
             color=BLUE, lw=2.8, zorder=4)
    for frac in (0.35, 0.68, 1.00):
        pt_c = P_pos + frac * (Y_pos - P_pos)
        axL.scatter(pt_c[0], pt_c[1], s=44, color=NAVY,
                    edgecolor="white", lw=0.9, zorder=6)
    axL.text(Y_pos[0] - 0.14, Y_pos[1] + 0.02, r"$Y$",
             ha="right", va="center", fontsize=10.2, fontweight="bold", color=NAVY,
             bbox=dict(boxstyle="round,pad=0.06", fc="white", ec="none", alpha=0.88),
             zorder=7)
    mid_py = 0.50 * P_pos + 0.50 * Y_pos
    axL.text(mid_py[0] + 0.04, mid_py[1] - 0.18, r"$\langle P, Y \rangle$",
             ha="center", va="top", fontsize=9.0, fontweight="bold", color=BLUE,
             zorder=7)
    axL.text(1.63, 1.15,
             r"Inside $P^\perp$: $1 + Q|\mathcal{P}_{d-2}|$",
             ha="center", va="center", fontsize=8.6, fontweight="bold", color=NAVY,
             bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="#bfdbfe", lw=0.9),
             zorder=6)

    # Fan of Q^{d-1} secant lines L exiting P^perp rightward from P into right panel
    for ty_out in (3.62, 2.52, 1.18):
        end_out = np.array([4.82, ty_out])
        axL.plot([P_pos[0], end_out[0]], [P_pos[1], end_out[1]],
                 color=RED, lw=1.9, ls="--", zorder=5)
        axL.annotate("", xy=end_out,
                     xytext=P_pos + 0.86 * (end_out - P_pos),
                     arrowprops=dict(arrowstyle="->", color=RED, lw=1.8), zorder=5)

    axL.text(4.02, 4.18,
             r"$Q^{d-1}$ secant lines $L$" "\n" r"outside $P^\perp$",
             ha="center", va="center", fontsize=8.4, fontweight="bold", color=RED,
             bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=RED_LIGHT, lw=0.9),
             zorder=7)

    # Vertex P
    axL.scatter(P_pos[0], P_pos[1], s=84, color=AMBER, edgecolor=TEXT, lw=1.2, zorder=8)
    axL.text(P_pos[0] - 0.04, P_pos[1] + 0.24, r"$P$",
             ha="center", va="bottom", fontsize=11.5, fontweight="bold", color=NAVY)

    axL.text(2.52, 0.42,
             r"$|\mathcal{P}_d| = (1 + Q|\mathcal{P}_{d-2}|) + Q^{d-1} \times (\mathrm{pts\ per\ } L)$",
             ha="center", va="center", fontsize=8.7, fontweight="bold", color=TEXT)

    # ---------------- Right panel: Three concrete secant rows (at q = 3) ----------------
    axR.set_xlim(0.0, 7.05)
    axR.set_ylim(0.0, 5.35)
    draw_card(axR, 0.05, 0.05, 6.95, 5.25, fc=GREY_BG, ec=GREY_LINE)
    axR.text(3.52, 4.92,
             r"Isotropic Points Beyond $P$ on Each Secant Line $L$ ($q = 3$)",
             ha="center", va="center", fontsize=9.5, fontweight="bold", color=TEXT)

    rows = [
        (3.52,
         r"Orthogonal $\mathcal{Q}(d, q)$ ($Q = q = 3$, $4$ points on $L$)",
         [True, False, False],
         r"$1$ point $\times\, q^{d-1} = +q^{d-1}$",
         None),
        (2.02,
         r"Symplectic $\mathcal{W}(d, q)$ ($Q = q = 3$, $4$ points on $L$)",
         [True, True, True],
         r"$q$ points $\times\, q^{d-1} = +q^d$",
         r"all points isotropic, but line $L \notin \mathcal{W}$"),
        (0.45,
         r"Unitary $\mathcal{H}(d, q^2)$ ($Q = q^2 = 9$, $10$ points on $L$)",
         [True, True, True, False, False, False, False, False, False],
         r"$q$ points $\times\, (q^2)^{d-1} = +q^{2d-1}$",
         r"Baer subline ($q + 1 = 4$ isotropic pts)"),
    ]

    for ry, title_r, flags, contrib, note_s in rows:
        draw_card(axR, 0.20, ry, 6.65, 1.32, fc="white", ec=GREY_LINE, lw=1.0, zorder=1)
        axR.text(0.38, ry + 1.04, title_r, ha="left", va="center",
                 fontsize=8.9, fontweight="bold", color=TEXT)

        x_start, x_end = 0.55, 3.88
        ly = ry + 0.52
        axR.plot([x_start, x_end + 0.16], [ly, ly], color=RED, lw=2.2, ls="--", zorder=2)

        # Vertex P on left of L
        axR.scatter(x_start, ly, s=70, color=AMBER, edgecolor=TEXT, lw=1.1, zorder=6)
        axR.text(x_start, ly - 0.27, r"$P$", ha="center", va="top",
                 fontsize=9.2, fontweight="bold", color=AMBER)

        n_rem = len(flags)
        xs_rem = np.linspace(x_start + (0.65 if n_rem == 3 else 0.36), x_end, n_rem)

        # Optional pill behind Baer subline in Unitary row
        if n_rem == 9:
            axR.add_patch(FancyBboxPatch(
                (x_start - 0.15, ly - 0.17), xs_rem[2] - x_start + 0.30, 0.34,
                boxstyle="round,pad=0.02,rounding_size=0.14",
                facecolor=BLUE_LIGHT, edgecolor=BLUE, lw=1.0, alpha=0.65, zorder=2
            ))

        for x_pt, is_iso in zip(xs_rem, flags):
            if is_iso:
                axR.scatter(x_pt, ly, s=62, color=NAVY, edgecolor="white", lw=1.0, zorder=6)
            else:
                axR.scatter(x_pt, ly, s=46, facecolor="white", edgecolor=RED, lw=1.5, zorder=5)

        if note_s:
            axR.text(2.32, ry + 0.17, note_s, ha="center", va="center",
                     fontsize=7.9, fontweight="bold",
                     color=BLUE if n_rem == 9 else SLATE)

        axR.text(5.46, ly, contrib, ha="center", va="center",
                 fontsize=8.6, fontweight="bold", color=NAVY,
                 bbox=dict(boxstyle="round,pad=0.18", fc=BLUE_PALE,
                           ec="#bfdbfe", lw=0.9), zorder=5)

    save_fig(fig, out_dir, "maths3_polar_point_count.png")


# ---------------------------------------------------------------------------
# Figure 9: Simple Quadrangle vs Complete Quadrangle and Complete Quadrilateral
#           (maths3_polygons_quadrangle.png)
# ---------------------------------------------------------------------------
def make_fig9_polygons(out_dir: Path):
    # ---- Verify Panel (a) & (b): 4 points in general position ----
    q_pts = [
        np.array([-1.18, -0.82]),
        np.array([ 1.24, -0.78]),
        np.array([ 0.92,  0.96]),
        np.array([-0.96,  0.86]),
    ]
    for a, b, c in itertools.combinations(q_pts, 3):
        area2 = abs((b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]))
        assert area2 > 0.8, "Three vertices nearly collinear"

    pairs_6 = list(itertools.combinations(range(4), 2))
    assert len(pairs_6) == 6
    inc_quad = np.zeros((4, 6), dtype=int)
    for col, (i, j) in enumerate(pairs_6):
        inc_quad[i, col] = 1
        inc_quad[j, col] = 1
    assert list(inc_quad.sum(axis=1)) == [3, 3, 3, 3]  # 4_3
    assert list(inc_quad.sum(axis=0)) == [2, 2, 2, 2, 2, 2]  # 6_2

    # ---- Verify Panel (c): 4 lines in general position -> 6 points (6_2, 4_3) ----
    # Lines written as y = m x + c
    lat_lines = [
        (0.0,   -0.84),  # l_1: horizontal bottom
        (1.22,   1.02),  # l_2: left-rising
        (-1.18,  1.15),  # l_3: right-falling
        (0.36,   0.04),  # l_4: tilted transversal
    ]
    lat_pts = {}
    for i, j in itertools.combinations(range(4), 2):
        m1, c1 = lat_lines[i]
        m2, c2 = lat_lines[j]
        assert abs(m1 - m2) > 0.2
        xi = (c2 - c1) / (m1 - m2)
        yi = m1 * xi + c1
        lat_pts[(i, j)] = np.array([xi, yi])
    assert len(lat_pts) == 6
    # Verify no three lines concurrent (all 6 pairwise intersections well separated)
    for p1, p2 in itertools.combinations(lat_pts.values(), 2):
        assert np.linalg.norm(p1 - p2) > 0.48

    inc_lat = np.zeros((6, 4), dtype=int)
    for row, (i, j) in enumerate(lat_pts.keys()):
        inc_lat[row, i] = 1
        inc_lat[row, j] = 1
    assert list(inc_lat.sum(axis=1)) == [2, 2, 2, 2, 2, 2]  # 6_2
    assert list(inc_lat.sum(axis=0)) == [3, 3, 3, 3]        # 4_3
    assert inc_quad.shape != inc_lat.shape  # not self-dual

    # ---- Draw Figure 9 ----
    fig = plt.figure(figsize=(11.4, 4.6), dpi=220)
    gs = fig.add_gridspec(1, 3, width_ratios=[0.95, 1.0, 1.15], wspace=0.05)
    axes = [fig.add_subplot(gs[k]) for k in range(3)]
    for ax in axes:
        ax.set_aspect("equal")
        ax.axis("off")

    # -------- Panel (a): Simple quadrangle (Euclidean 4-cycle) --------
    axa = axes[0]
    axa.set_xlim(-1.95, 1.95)
    axa.set_ylim(-1.75, 2.18)
    draw_card(axa, -1.90, -1.69, 3.80, 3.80, fc=GREY_BG, ec=GREY_LINE)
    axa.text(0.0, 1.78, "(a) Simple Quadrangle\n(Euclidean $4$-cycle)",
             ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEXT)

    cyc = [(0, 1), (1, 2), (2, 3), (3, 0)]
    for i, j in cyc:
        axa.plot([q_pts[i][0], q_pts[j][0]], [q_pts[i][1], q_pts[j][1]],
                 color=SLATE, lw=2.5, zorder=3)
    for idx, pt in enumerate(q_pts):
        axa.scatter(pt[0], pt[1], s=66, color=NAVY, edgecolor="white", lw=1.1, zorder=6)

    axa.text(0.0, -1.38, "$4$ points, $4$ boundary edges\n($2$ edges per point, no diagonals)",
             ha="center", va="center", fontsize=8.4, color=TEXT)

    # -------- Panel (b): Complete quadrangle (4_3, 6_2) — NO diagonal points marked --------
    axb = axes[1]
    axb.set_xlim(-2.05, 2.05)
    axb.set_ylim(-1.75, 2.18)
    draw_card(axb, -2.00, -1.69, 4.00, 3.80, fc=GREY_BG, ec=GREY_LINE)
    axb.text(0.0, 1.78, r"(b) Complete Quadrangle $(4_3, 6_2)$" "\n"
                        r"($v = 4$ points, $b = 6$ lines)",
             ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEXT)

    # Compute exact overpass crossing of the two inner diagonals (0,2) and (1,3)
    diag_hit = seg_intersection_2d(q_pts[0], q_pts[2], q_pts[1], q_pts[3])
    assert diag_hit is not None

    ext = 0.20
    for idx_e, (i, j) in enumerate(pairs_6):
        pa, pb = q_pts[i], q_pts[j]
        u = (pb - pa) / np.linalg.norm(pb - pa)
        sa, sb = pa - ext * u, pb + ext * u
        z_line = 4 if (i, j) == (0, 2) else 3
        if (i, j) == (0, 2):
            # Clean white overpass gap so the diagonal crossing is unmistakably NOT a marked point!
            axb.add_patch(Circle((diag_hit[0], diag_hit[1]), 0.11,
                                 facecolor=GREY_BG, edgecolor="none", zorder=3.5))
        axb.plot([sa[0], sb[0]], [sa[1], sb[1]], color=BLUE, lw=2.4, zorder=z_line)

    # Mark ONLY the 4 vertices of the quadrangle!
    for pt in q_pts:
        axb.scatter(pt[0], pt[1], s=70, color=NAVY, edgecolor="white", lw=1.1, zorder=6)

    axb.text(0.0, -1.38, "$3$ lines through each point,\n$2$ marked points on each line",
             ha="center", va="center", fontsize=8.4, fontweight="bold", color=BLUE)

    # -------- Panel (c): Complete quadrilateral (6_2, 4_3) (Dual) --------
    axc = axes[2]
    axc.set_xlim(-2.92, 2.12)
    axc.set_ylim(-1.75, 2.18)
    draw_card(axc, -2.86, -1.69, 4.92, 3.80, fc=GREY_BG, ec=GREY_LINE)
    axc.text(-0.40, 1.78, r"(c) Complete Quadrilateral $(6_2, 4_3)$" "\n"
                          r"(Dual: $b = 4$ lines, $v = 6$ points)",
             ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEXT)

    # Clip each of the 4 lines cleanly around its 3 collinear intersection points
    for k, (m, c) in enumerate(lat_lines):
        on_k = [pt for (i, j), pt in lat_pts.items() if k in (i, j)]
        assert len(on_k) == 3
        xs_k = [p[0] for p in on_k]
        pad_x = 0.16 if abs(m) > 1.0 else 0.19
        xa, xb = min(xs_k) - pad_x, max(xs_k) + pad_x
        pa = np.array([xa, m * xa + c])
        pb = np.array([xb, m * xb + c])
        axc.plot([pa[0], pb[0]], [pa[1], pb[1]], color=TEAL, lw=2.5, zorder=3)

    # Mark ALL 6 pairwise intersections!
    for pt in lat_pts.values():
        axc.scatter(pt[0], pt[1], s=66, color=NAVY, edgecolor="white", lw=1.1, zorder=6)

    axc.text(-0.40, -1.38, "$3$ marked points on each line,\n$2$ lines through each point",
             ha="center", va="center", fontsize=8.4, fontweight="bold", color=TEAL)

    save_fig(fig, out_dir, "maths3_polygons_quadrangle.png")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_dir>", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"Generating 9 settled projective geometry figures into {out_dir} ...")

    make_fig1_fano(out_dir)
    make_fig2_affine_slice(out_dir)
    make_fig3_transversal_16pt(out_dir)
    make_fig4_tangent_planes(out_dir)
    make_fig5_ovals_nucleus(out_dir)
    make_fig6_symplectic_fan(out_dir)
    make_fig7_hermitian_pg29(out_dir)
    make_fig8_point_count(out_dir)
    make_fig9_polygons(out_dir)

    print("All 9 figures generated and verified successfully.")


if __name__ == "__main__":
    main()
