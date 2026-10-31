#!/usr/bin/env python3
"""Generate publication-quality replacement figures for the 10 ASCII diagrams
in 'Maths 3 - Projective Geometry'.

Usage:
    /home/ubuntu/.claude/skills/lecture-notes/.venv/bin/python \
        make_maths3_figures.py <output_dir>
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


# ---------------------------------------------------------------------------
# Consistent visual palette & typography across all 10 figures
# ---------------------------------------------------------------------------
NAVY = "#1e3a8a"        # Points of the geometry / active node outlines
BLUE = "#2563eb"        # Lines of the geometry / single & double bonds
BLUE_LIGHT = "#dbeafe"  # Soft blue node/plane fill
BLUE_PALE = "#eff6ff"   # Very pale blue card background
TEAL = "#0f766e"        # Quadric surface / second regulus or generator family
TEAL_LIGHT = "#ccfbf1"  # Soft teal fill
AMBER = "#d97706"       # Fixed flag elements / polar hyperplane P^pi
AMBER_LIGHT = "#fef3c7" # Soft amber highlight fill
RED = "#dc2626"         # External point P / ambient secant poking off S
RED_LIGHT = "#fee2e2"   # Soft red warning fill
SLATE = "#64748b"       # Ambient rays / erased nodes / secondary annotations
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
# Helper drawing primitives
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
              pad: float = 0.08, zorder: int = 0):
    box = FancyBboxPatch(
        (x + pad, y + pad), w - 2 * pad, h - 2 * pad,
        boxstyle=f"round,pad={pad},rounding_size=0.14",
        facecolor=fc, edgecolor=ec, linewidth=lw, zorder=zorder
    )
    ax.add_patch(box)
    return box


def draw_bt_node(ax, x: float, y: float, idx_label: str,
                 title_below: str | None = None,
                 subtitle_below: str | None = None,
                 r: float = 0.27, active: bool = True,
                 fc: str | None = None, ec: str | None = None,
                 label_side: str = "below", zorder: int = 5):
    if active:
        fill = fc if fc is not None else BLUE_LIGHT
        edge = ec if ec is not None else NAVY
        txt_col = NAVY
        ls = "-"
        lw = 2.2
    else:
        fill = "#f1f5f9"
        edge = "#94a3b8"
        txt_col = "#94a3b8"
        ls = "--"
        lw = 1.5

    circ = Circle((x, y), r, facecolor=fill, edgecolor=edge,
                  linewidth=lw, linestyle=ls, zorder=zorder)
    ax.add_patch(circ)
    ax.text(x, y, idx_label, ha="center", va="center",
            fontsize=12, fontweight="bold", color=txt_col, zorder=zorder + 1)

    if not active:
        # Soft red/slate deletion cross
        d = r * 0.72
        ax.plot([x - d, x + d], [y - d, y + d], color=RED, lw=1.8, alpha=0.75, zorder=zorder + 2)
        ax.plot([x - d, x + d], [y + d, y - d], color=RED, lw=1.8, alpha=0.75, zorder=zorder + 2)

    if title_below:
        t_col = TEXT if active else "#94a3b8"
        s_col = SLATE if active else "#cbd5e1"
        if label_side == "below":
            ax.text(x, y - r - 0.16, title_below, ha="center", va="top",
                    fontsize=10.5, fontweight="bold", color=t_col, zorder=zorder + 1)
            if subtitle_below:
                ax.text(x, y - r - 0.44, subtitle_below, ha="center", va="top",
                        fontsize=8.8, color=s_col, zorder=zorder + 1)
        elif label_side == "above":
            ax.text(x, y + r + 0.14, title_below, ha="center", va="bottom",
                    fontsize=10.5, fontweight="bold", color=t_col, zorder=zorder + 1)
            if subtitle_below:
                ax.text(x, y + r + 0.42, subtitle_below, ha="center", va="bottom",
                        fontsize=8.8, color=s_col, zorder=zorder + 1)
        elif label_side == "right":
            ax.text(x + r + 0.18, y + (0.09 if subtitle_below else 0.0), title_below,
                    ha="left", va="center", fontsize=10.5, fontweight="bold",
                    color=t_col, zorder=zorder + 1)
            if subtitle_below:
                ax.text(x + r + 0.18, y - 0.18, subtitle_below,
                        ha="left", va="center", fontsize=8.8,
                        color=s_col, zorder=zorder + 1)
        elif label_side == "left":
            ax.text(x - r - 0.18, y + (0.09 if subtitle_below else 0.0), title_below,
                    ha="right", va="center", fontsize=10.5, fontweight="bold",
                    color=t_col, zorder=zorder + 1)
            if subtitle_below:
                ax.text(x - r - 0.18, y - 0.18, subtitle_below,
                        ha="right", va="center", fontsize=8.8,
                        color=s_col, zorder=zorder + 1)


def draw_bt_bond(ax, p1: tuple[float, float], p2: tuple[float, float],
                 order: int = 1, r: float = 0.27, active: bool = True,
                 top_label: str | None = None, bottom_label: str | None = None,
                 color: str | None = None, sep: float = 0.085, zorder: int = 3):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy)
    ux, uy = dx / L, dy / L
    nx, ny = -uy, ux

    sx, sy = x1 + ux * r, y1 + uy * r
    ex, ey = x2 - ux * r, y2 - uy * r

    col = (color if color else BLUE) if active else "#cbd5e1"
    ls = "-" if active else "--"
    lw = 2.5 if active else 1.5

    if order == 1:
        ax.plot([sx, ex], [sy, ey], color=col, lw=lw, linestyle=ls, zorder=zorder)
    elif order == 2:
        for sgn in (+1, -1):
            ax.plot([sx + sgn * sep * nx, ex + sgn * sep * nx],
                    [sy + sgn * sep * ny, ey + sgn * sep * ny],
                    color=col, lw=lw, linestyle=ls, zorder=zorder)

    mx, my = 0.5 * (x1 + x2), 0.5 * (y1 + y2)
    if top_label:
        ax.text(mx, my + 0.20, top_label, ha="center", va="bottom",
                fontsize=9.5, fontweight="bold",
                color=(BLUE if color is None else color) if active else "#94a3b8",
                zorder=zorder + 2)
    if bottom_label:
        ax.text(mx, my - 0.22, bottom_label, ha="center", va="top",
                fontsize=8.7, color=SLATE if active else "#cbd5e1",
                zorder=zorder + 2)


def project_cube_pts(cx: float, cy: float, scale: float = 0.55):
    """Oblique 3D-to-2D projection for the cube with vertices 1..8 matching
    the notes (lines 1285-1304): top face 1-2-3-4, bottom face 5-6-7-8
    with 5 below 1, 6 below 2, 7 below 3, 8 below 4."""
    pts3 = {
        1: (-1, -1,  1),  # front-left-top
        2: ( 1, -1,  1),  # front-right-top
        3: ( 1,  1,  1),  # back-right-top
        4: (-1,  1,  1),  # back-left-top
        5: (-1, -1, -1),  # front-left-bottom
        6: ( 1, -1, -1),  # front-right-bottom
        7: ( 1,  1, -1),  # back-right-bottom
        8: (-1,  1, -1),  # back-left-bottom
    }
    out = {}
    for k, (X, Y, Z) in pts3.items():
        px = cx + scale * (0.82 * X + 0.36 * Y)
        py = cy + scale * (0.76 * Z + 0.26 * Y)
        out[k] = (px, py)
    return out


CUBE_EDGES = [
    (1, 2), (2, 3), (3, 4), (4, 1),  # top
    (5, 6), (6, 7), (7, 8), (8, 5),  # bottom
    (1, 5), (2, 6), (3, 7), (4, 8),  # verticals
]


def save_fig(fig, out_dir: Path, filename: str):
    out_path = out_dir / filename
    fig.savefig(out_path, dpi=220, bbox_inches="tight", pad_inches=0.14)
    plt.close(fig)
    print(f"  [saved] {out_path}")


# ---------------------------------------------------------------------------
# Figure 1: Buekenhout-Tits Diagram of the 3D Cube (lines 1496-1501)
# ---------------------------------------------------------------------------
def make_fig1_cube_diagram(out_dir: Path):
    fig, ax = setup_canvas(10.6, 6.2, xlim=(0, 10.6), ylim=(0, 6.2))

    # Top panel: Buekenhout-Tits B_3 / C_3 diagram
    draw_card(ax, 0.2, 3.65, 10.2, 2.35, fc=BLUE_PALE, ec="#bfdbfe")
    ax.text(5.3, 5.72, r"Buekenhout-Tits Diagram of the 3D Cube ($B_3 / C_3$)",
            ha="center", va="center", fontsize=11.5, fontweight="bold", color=NAVY)

    n0, n1, n2 = (2.0, 4.72), (5.3, 4.72), (8.6, 4.72)
    draw_bt_node(ax, *n0, r"$0$", "Vertices", "(Type 0)")
    draw_bt_node(ax, *n1, r"$1$", "Edges", "(Type 1)")
    draw_bt_node(ax, *n2, r"$2$", "Faces", "(Type 2)")

    draw_bt_bond(ax, n0, n1, order=2,
                 top_label=r"Square ($4$-gon)",
                 bottom_label="fix a Face (Type 2)")
    draw_bt_bond(ax, n1, n2, order=1,
                 top_label="Triangle (Projective Plane)",
                 bottom_label="fix a Vertex (Type 0)")

    # Subtle arch showing no bond between 0 and 2 (generalized digon)
    arc = FancyArrowPatch(
        (n0[0] + 0.18, n0[1] + 0.30), (n2[0] - 0.18, n2[1] + 0.30),
        connectionstyle="arc3,rad=-0.16",
        arrowstyle="-", linestyle=":", linewidth=1.3, color=SLATE, zorder=2
    )
    ax.add_patch(arc)
    ax.text(5.3, 5.38, "No edge between 0 and 2: Generalized Digon (fix an Edge)",
            ha="center", va="center", fontsize=8.8, style="italic", color=SLATE,
            bbox=dict(boxstyle="round,pad=0.15", fc=BLUE_PALE, ec="none"))

    # Bottom 3 residue cards
    panel_w = 3.26
    xs = [0.2, 3.67, 7.14]
    titles = [
        r"(a) Fix a Face $\Rightarrow$ bond $0 = 1$",
        r"(b) Fix a Vertex $v$ $\Rightarrow$ bond $1 - 2$",
        r"(c) Fix an Edge $\Rightarrow$ no bond $0 \;\; 2$",
    ]
    subtitles = [
        "4 vertices & 4 edges form a square",
        "3 edges & 3 faces form a triangle",
        "2 vertices & 2 faces form a digon",
    ]

    for i, px in enumerate(xs):
        draw_card(ax, px, 0.15, panel_w, 3.35, fc=GREY_BG, ec=GREY_LINE)
        ax.text(px + panel_w / 2, 3.22, titles[i], ha="center", va="center",
                fontsize=9.6, fontweight="bold", color=TEXT)
        ax.text(px + panel_w / 2, 0.42, subtitles[i], ha="center", va="center",
                fontsize=8.8, color=SLATE)

    # --- Inset (a): Fixed top face 1-2-3-4 ---
    pts_a = project_cube_pts(xs[0] + panel_w / 2, 1.75, scale=0.62)
    for u, v in CUBE_EDGES:
        ax.plot([pts_a[u][0], pts_a[v][0]], [pts_a[u][1], pts_a[v][1]],
                color="#cbd5e1", lw=1.2, zorder=2)
    top_poly = Polygon([pts_a[k] for k in (1, 2, 3, 4)], closed=True,
                       facecolor=AMBER_LIGHT, edgecolor=BLUE, lw=2.5, alpha=0.85, zorder=4)
    ax.add_patch(top_poly)
    for k in (1, 2, 3, 4):
        ax.scatter(*pts_a[k], s=48, color=NAVY, zorder=6)
    cx_top = 0.25 * sum(pts_a[k][0] for k in (1, 2, 3, 4))
    cy_top = 0.25 * sum(pts_a[k][1] for k in (1, 2, 3, 4))
    ax.text(cx_top, cy_top, "fixed face",
            ha="center", va="center", fontsize=8.4, fontweight="bold", color=AMBER, zorder=7)

    # --- Inset (b): Fixed vertex 1, 3 edges (12,14,15) and 3 faces + vertex figure triangle ---
    pts_b = project_cube_pts(xs[1] + panel_w / 2, 1.75, scale=0.62)
    for u, v in CUBE_EDGES:
        ax.plot([pts_b[u][0], pts_b[v][0]], [pts_b[u][1], pts_b[v][1]],
                color="#cbd5e1", lw=1.2, zorder=2)
    # Tint the 3 faces meeting at vertex 1
    for face_nodes in [(1, 2, 3, 4), (1, 2, 6, 5), (1, 4, 8, 5)]:
        poly = Polygon([pts_b[k] for k in face_nodes], closed=True,
                       facecolor=BLUE_LIGHT, edgecolor="none", alpha=0.38, zorder=3)
        ax.add_patch(poly)
    # Highlight the 3 incident edges 1-2, 1-4, 1-5
    tri_pts = []
    for nb in (2, 4, 5):
        ax.plot([pts_b[1][0], pts_b[nb][0]], [pts_b[1][1], pts_b[nb][1]],
                color=BLUE, lw=2.6, zorder=5)
        mx = 0.55 * pts_b[1][0] + 0.45 * pts_b[nb][0]
        my = 0.55 * pts_b[1][1] + 0.45 * pts_b[nb][1]
        tri_pts.append((mx, my))
    # Vertex-figure triangle slice
    vfig = Polygon(tri_pts, closed=True, facecolor=TEAL_LIGHT, edgecolor=TEAL,
                   lw=1.8, linestyle="--", alpha=0.8, zorder=6)
    ax.add_patch(vfig)
    for tp in tri_pts:
        ax.scatter(*tp, s=26, color=TEAL, zorder=7)
    ax.scatter(*pts_b[1], s=72, color=AMBER, edgecolor=TEXT, linewidth=1.0, zorder=8)
    ax.text(pts_b[1][0] - 0.16, pts_b[1][1] + 0.12, r"$v$",
            ha="right", va="bottom", fontsize=9.5, fontweight="bold", color=AMBER, zorder=9)

    # --- Inset (c): Fixed edge 1-2, 2 vertices (1,2) & 2 faces (top 1234, front 1265) ---
    pts_c = project_cube_pts(xs[2] + panel_w / 2, 1.75, scale=0.62)
    for u, v in CUBE_EDGES:
        ax.plot([pts_c[u][0], pts_c[v][0]], [pts_c[u][1], pts_c[v][1]],
                color="#cbd5e1", lw=1.2, zorder=2)
    for face_nodes, fc_col in [((1, 2, 3, 4), BLUE_LIGHT), ((1, 2, 6, 5), TEAL_LIGHT)]:
        poly = Polygon([pts_c[k] for k in face_nodes], closed=True,
                       facecolor=fc_col, edgecolor=BLUE, lw=1.3, alpha=0.62, zorder=3)
        ax.add_patch(poly)
    ax.plot([pts_c[1][0], pts_c[2][0]], [pts_c[1][1], pts_c[2][1]],
            color=AMBER, lw=3.8, zorder=6)
    for k in (1, 2):
        ax.scatter(*pts_c[k], s=55, color=NAVY, zorder=7)
    mx_e = 0.5 * (pts_c[1][0] + pts_c[2][0])
    my_e = 0.5 * (pts_c[1][1] + pts_c[2][1])
    ax.text(mx_e, my_e - 0.19, "fixed edge", ha="center", va="top",
            fontsize=8.4, fontweight="bold", color=AMBER, zorder=8)

    save_fig(fig, out_dir, "maths3_diagrams_cube.png")


# ---------------------------------------------------------------------------
# Figure 2: Buekenhout-Tits Diagram of PG(3, q) (lines 1517-1522)
# ---------------------------------------------------------------------------
def make_fig2_pg3_diagram(out_dir: Path):
    fig, ax = setup_canvas(10.6, 6.2, xlim=(0, 10.6), ylim=(0, 6.2))

    # Top panel: A_3 diagram of PG(3, q)
    draw_card(ax, 0.2, 3.65, 10.2, 2.35, fc=BLUE_PALE, ec="#bfdbfe")
    ax.text(5.3, 5.72, r"Buekenhout-Tits Diagram of 3D Projective Space $\mathrm{PG}(3, q)$ ($A_3$)",
            ha="center", va="center", fontsize=11.5, fontweight="bold", color=NAVY)

    n0, n1, n2 = (2.0, 4.72), (5.3, 4.72), (8.6, 4.72)
    draw_bt_node(ax, *n0, r"$0$", "Points", "(Type 0)")
    draw_bt_node(ax, *n1, r"$1$", "Lines", "(Type 1)")
    draw_bt_node(ax, *n2, r"$2$", "Planes", "(Type 2)")

    draw_bt_bond(ax, n0, n1, order=1,
                 top_label=r"Projective Plane $\mathrm{PG}(2, q)$",
                 bottom_label=r"fix a Plane $\Pi$ (Type 2)")
    draw_bt_bond(ax, n1, n2, order=1,
                 top_label=r"Projective Plane $\mathrm{PG}(2, q)$",
                 bottom_label=r"fix a Point $P$ (Type 0)")

    arc = FancyArrowPatch(
        (n0[0] + 0.18, n0[1] + 0.30), (n2[0] - 0.18, n2[1] + 0.30),
        connectionstyle="arc3,rad=-0.16",
        arrowstyle="-", linestyle=":", linewidth=1.3, color=SLATE, zorder=2
    )
    ax.add_patch(arc)
    ax.text(5.3, 5.38, r"No edge between 0 and 2: Generalized Digon (fix a Line $\ell$)",
            ha="center", va="center", fontsize=8.8, style="italic", color=SLATE,
            bbox=dict(boxstyle="round,pad=0.15", fc=BLUE_PALE, ec="none"))

    panel_w = 3.26
    xs = [0.2, 3.67, 7.14]
    titles = [
        r"(a) Fix a Plane $\Pi$ $\Rightarrow$ bond $0 - 1$",
        r"(b) Fix a Point $P$ $\Rightarrow$ bond $1 - 2$",
        r"(c) Fix a Line $\ell$ $\Rightarrow$ no bond $0 \;\; 2$",
    ]
    subtitles = [
        r"Points & lines in $\Pi$ form $\mathrm{PG}(2, q)$",
        r"Lines & planes through $P$ form $\mathrm{PG}(2, q)$",
        r"Every $P \in \ell$ lies in every $\Pi \supset \ell$",
    ]
    for i, px in enumerate(xs):
        draw_card(ax, px, 0.15, panel_w, 3.35, fc=GREY_BG, ec=GREY_LINE)
        ax.text(px + panel_w / 2, 3.22, titles[i], ha="center", va="center",
                fontsize=9.5, fontweight="bold", color=TEXT)
        ax.text(px + panel_w / 2, 0.42, subtitles[i], ha="center", va="center",
                fontsize=8.7, color=SLATE)

    # --- Inset (a): Fixed plane Pi containing Fano plane (q=2 illustration) ---
    cx_a, cy_a = xs[0] + panel_w / 2, 1.75
    plane_poly = Polygon([
        (cx_a - 1.25, cy_a - 0.82), (cx_a + 0.95, cy_a - 0.82),
        (cx_a + 1.28, cy_a + 0.85), (cx_a - 0.92, cy_a + 0.85)
    ], closed=True, facecolor=AMBER_LIGHT, edgecolor=AMBER, lw=1.8, alpha=0.72, zorder=2)
    ax.add_patch(plane_poly)
    ax.text(cx_a + 1.05, cy_a + 0.65, r"$\Pi$", fontsize=11, fontweight="bold", color=AMBER)

    # Draw crisp Fano plane inside Pi
    R_tri = 0.62
    v_top = (cx_a, cy_a + 0.62)
    v_bl = (cx_a - 0.62, cy_a - 0.45)
    v_br = (cx_a + 0.62, cy_a - 0.45)
    m_ab = (0.5 * (v_top[0] + v_bl[0]), 0.5 * (v_top[1] + v_bl[1]))
    m_bc = (0.5 * (v_bl[0] + v_br[0]), 0.5 * (v_bl[1] + v_br[1]))
    m_ca = (0.5 * (v_br[0] + v_top[0]), 0.5 * (v_br[1] + v_top[1]))
    ctr = (cx_a, cy_a - 0.093)
    r_in = math.hypot(ctr[0] - m_bc[0], ctr[1] - m_bc[1])

    for a_pt, b_pt in [(v_top, v_bl), (v_bl, v_br), (v_br, v_top),
                       (v_top, m_bc), (v_bl, m_ca), (v_br, m_ab)]:
        ax.plot([a_pt[0], b_pt[0]], [a_pt[1], b_pt[1]], color=BLUE, lw=1.6, zorder=4)
    incirc = Circle(ctr, r_in, facecolor="none", edgecolor=BLUE, lw=1.6, zorder=4)
    ax.add_patch(incirc)
    for pt in [v_top, v_bl, v_br, m_ab, m_bc, m_ca, ctr]:
        ax.scatter(*pt, s=30, color=NAVY, zorder=6)

    # --- Inset (b): Fixed point P with bundle of lines & planes through P ---
    cx_b, cy_b = xs[1] + panel_w / 2, 1.75
    p_origin = (cx_b - 0.95, cy_b - 0.15)
    # Slicing screen showing PG(2, q) cross-section of the star at P
    scr = Polygon([
        (cx_b + 0.15, cy_b - 0.82), (cx_b + 1.15, cy_b - 0.62),
        (cx_b + 1.15, cy_b + 0.82), (cx_b + 0.15, cy_b + 0.62)
    ], closed=True, facecolor=BLUE_LIGHT, edgecolor=BLUE, lw=1.3, alpha=0.65, zorder=3)
    ax.add_patch(scr)
    targets = [
        (cx_b + 0.65, cy_b + 0.52),
        (cx_b + 0.36, cy_b - 0.36),
        (cx_b + 0.96, cy_b - 0.18),
    ]
    # Translucent plane wedges from P to pairs of lines
    for i_t in range(3):
        t1, t2 = targets[i_t], targets[(i_t + 1) % 3]
        wedge = Polygon([p_origin, t1, t2], closed=True,
                        facecolor=TEAL_LIGHT, edgecolor="none", alpha=0.35, zorder=2)
        ax.add_patch(wedge)
        ax.plot([t1[0], t2[0]], [t1[1], t2[1]], color=TEAL, lw=1.8, zorder=5)
    for t_pt in targets:
        ax.plot([p_origin[0], t_pt[0] + 0.18 * (t_pt[0] - p_origin[0])],
                [p_origin[1], t_pt[1] + 0.18 * (t_pt[1] - p_origin[1])],
                color=BLUE, lw=1.9, zorder=5)
        ax.scatter(*t_pt, s=26, color=NAVY, zorder=6)
    ax.scatter(*p_origin, s=72, color=AMBER, edgecolor=TEXT, lw=1.0, zorder=8)
    ax.text(p_origin[0] - 0.12, p_origin[1] + 0.16, r"$P$",
            ha="right", va="bottom", fontsize=10.5, fontweight="bold", color=AMBER)

    # --- Inset (c): Pencil ("book") of planes through fixed line ell ---
    cx_c, cy_c = xs[2] + panel_w / 2, 1.75
    l_bot = (cx_c, cy_c - 0.82)
    l_top = (cx_c, cy_c + 0.85)
    flaps = [
        [(-1.05, -0.58), (-1.05, 0.56), BLUE_LIGHT, BLUE],
        [(-0.62, -0.92), (-0.62, 0.22), TEAL_LIGHT, TEAL],
        [( 0.98, -0.50), ( 0.98, 0.64), BLUE_LIGHT, BLUE],
    ]
    for (dx1, dy1), (dx2, dy2), fc_f, ec_f in flaps:
        leaf = Polygon([
            l_bot,
            (cx_c + dx1, cy_c + dy1),
            (cx_c + dx2, cy_c + dy2),
            l_top
        ], closed=True, facecolor=fc_f, edgecolor=ec_f, lw=1.3, alpha=0.58, zorder=3)
        ax.add_patch(leaf)
    ax.plot([l_bot[0], l_top[0]], [l_bot[1], l_top[1]], color=AMBER, lw=3.6, zorder=6)
    for frac in (0.22, 0.50, 0.78):
        py = l_bot[1] + frac * (l_top[1] - l_bot[1])
        ax.scatter(cx_c, py, s=46, color=NAVY, zorder=7)
    ax.text(cx_c + 0.14, l_top[1] - 0.04, r"$\ell$", ha="left", va="center",
            fontsize=11, fontweight="bold", color=AMBER, zorder=8)

    save_fig(fig, out_dir, "maths3_diagrams_pg3.png")


# ---------------------------------------------------------------------------
# Figure 3: Reading Diagrams by Deleting Nodes - PG(4, q) (lines 1542-1546)
# ---------------------------------------------------------------------------
def make_fig3_deleting_nodes(out_dir: Path):
    fig, ax = setup_canvas(11.0, 7.3, xlim=(0, 11.0), ylim=(0, 7.3))

    x_cols = [0.92, 2.24, 3.56, 4.88]
    type_names = ["Points", "Lines", "Planes", "Solids"]

    # Header card: Full 4-node A_4 diagram
    draw_card(ax, 0.2, 5.42, 10.6, 1.72, fc=BLUE_PALE, ec="#bfdbfe")
    ax.text(2.90, 6.82, r"Full $A_4$ Diagram of $\mathrm{PG}(4, q)$",
            ha="center", va="center", fontsize=11.2, fontweight="bold", color=NAVY)
    y_top = 6.18
    for idx in range(4):
        draw_bt_node(ax, x_cols[idx], y_top, rf"${idx}$", type_names[idx], r=0.22)
    for idx in range(3):
        draw_bt_bond(ax, (x_cols[idx], y_top), (x_cols[idx + 1], y_top), order=1, r=0.22)

    ax.text(8.15, 6.26,
            "Rule for residues:\n"
            r"Fix a flag $F \Rightarrow$ erase the nodes" "\n"
            r"in $\mathrm{type}(F)$ and their attached edges.",
            ha="center", va="center", fontsize=9.2, color=TEXT,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="#bfdbfe", lw=1.0))

    # Three deletion rows matching lines 1550-1565
    rows = [
        {
            "y": 4.14,
            "active": [True, True, True, False],
            "bonds": [(0, 1, True), (1, 2, True), (2, 3, False)],
            "badge": "Delete 1 node (erase Node 3)",
            "flag": r"Fix one Solid $S$ ($F = \{S\}$):",
            "desc": r"Surviving chain $0 - 1 - 2$ is $\mathrm{PG}(3, q)$" "\n"
                    r"(all points, lines, and planes inside $S$).",
            "fc": GREY_BG,
        },
        {
            "y": 2.42,
            "active": [True, True, False, False],
            "bonds": [(0, 1, True), (1, 2, False), (2, 3, False)],
            "badge": "Delete 2 end nodes (erase Nodes 2, 3)",
            "flag": r"Fix flag $F = \{\Pi, S\}$ with $\Pi \subset S$:",
            "desc": r"Surviving single stroke $0 - 1$ is $\mathrm{PG}(2, q)$" "\n"
                    r"(all points and lines inside the plane $\Pi$).",
            "fc": GREY_BG,
        },
        {
            "y": 0.70,
            "active": [True, False, False, True],
            "bonds": [(0, 1, False), (1, 2, False), (2, 3, False)],
            "badge": "Delete 2 middle nodes (erase Nodes 1, 2)",
            "flag": r"Fix flag $F = \{\ell, \Pi\}$ with $\ell \subset \Pi$:",
            "desc": r"Disconnected nodes $0$ and $3$ form a digon:" "\n"
                    r"every $P \in \ell$ lies in every solid $S \supset \Pi$.",
            "fc": "#fffbeb",
        },
    ]

    for row in rows:
        yc = row["y"]
        draw_card(ax, 0.2, yc - 0.58, 10.6, 1.58, fc=row["fc"], ec=GREY_LINE)
        ax.text(2.90, yc + 0.72, row["badge"], ha="center", va="center",
                fontsize=9.4, fontweight="bold", color=AMBER if not row["active"][1] else NAVY)
        yn = yc + 0.06
        for i in range(4):
            draw_bt_node(ax, x_cols[i], yn, rf"${i}$", type_names[i],
                         r=0.21, active=row["active"][i])
        for i1, i2, b_act in row["bonds"]:
            draw_bt_bond(ax, (x_cols[i1], yn), (x_cols[i2], yn),
                         order=1, r=0.21, active=b_act)

        if row["active"] == [True, False, False, True]:
            ax.text(2.90, yn + 0.36, "no connecting edge (generalized digon)",
                    ha="center", va="center", fontsize=8.3, style="italic", color=AMBER,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=AMBER_LIGHT, lw=0.8))

        ax.text(5.75, yc + 0.40, row["flag"], ha="left", va="center",
                fontsize=9.6, fontweight="bold", color=TEXT)
        ax.text(5.75, yc - 0.10, row["desc"], ha="left", va="center",
                fontsize=9.1, color=SLATE)

    save_fig(fig, out_dir, "maths3_diagrams_deleting_nodes.png")


# ---------------------------------------------------------------------------
# Figure 4: D_4 Diagram and Triality on Q^+(7, q) (lines 1600-1608)
# ---------------------------------------------------------------------------
def make_fig4_d4_triality(out_dir: Path):
    fig, ax = setup_canvas(9.6, 6.2, xlim=(0, 9.6), ylim=(0, 6.2))

    draw_card(ax, 0.2, 0.2, 9.2, 5.8, fc=GREY_BG, ec=GREY_LINE)
    ax.text(4.8, 5.62, r"Symmetric $D_4$ Diagram of $Q^+(7, q)$ and Cartan's Triality",
            ha="center", va="center", fontsize=11.5, fontweight="bold", color=NAVY)

    hub = (4.45, 3.12)
    L_arm = 1.92
    p_pts = (hub[0] - L_arm, hub[1])  # 180 deg
    p_plus = (hub[0] + L_arm * math.cos(math.radians(60)),
              hub[1] + L_arm * math.sin(math.radians(60)))   # +60 deg
    p_minus = (hub[0] + L_arm * math.cos(math.radians(-60)),
               hub[1] + L_arm * math.sin(math.radians(-60))) # -60 deg

    # Bonds (all equal length, exact 120-degree Y-star)
    for target in (p_pts, p_plus, p_minus):
        draw_bt_bond(ax, hub, target, order=1, r=0.30)

    # Central node 1 (Lines)
    draw_bt_node(ax, *hub, r"$1$", r=0.30, fc="white", ec=NAVY)
    ax.text(hub[0] - 0.14, hub[1] - 0.44, "Lines\n(Type 1)",
            ha="center", va="top", fontsize=9.6, fontweight="bold", color=TEXT)

    # Outer symmetric nodes 0, 2, 3
    draw_bt_node(ax, *p_pts, r"$0$", "Points", "(Type 0: dim 0)",
                 r=0.30, fc=BLUE_LIGHT, ec=NAVY, label_side="left")
    draw_bt_node(ax, *p_plus, r"$2$", r"$+$ Solids", "(Type 2: dim 3)",
                 r=0.30, fc=TEAL_LIGHT, ec=TEAL, label_side="right")
    draw_bt_node(ax, *p_minus, r"$3$", r"$-$ Solids", "(Type 3: dim 3)",
                 r=0.30, fc=TEAL_LIGHT, ec=TEAL, label_side="right")

    # Curved 3-cycle triality arrows around the 3 outer prongs
    cycle_pairs = [
        ((p_pts[0] + 0.15, p_pts[1] + 0.36), (p_plus[0] - 0.34, p_plus[1] + 0.08), -0.26),
        ((p_plus[0] + 0.14, p_plus[1] - 0.35), (p_minus[0] + 0.14, p_minus[1] + 0.35), -0.26),
        ((p_minus[0] - 0.34, p_minus[1] - 0.08), (p_pts[0] + 0.15, p_pts[1] - 0.36), -0.26),
    ]
    for s_pt, e_pt, rad in cycle_pairs:
        arr = FancyArrowPatch(
            s_pt, e_pt,
            connectionstyle=f"arc3,rad={rad}",
            arrowstyle="-|>,head_length=6,head_width=3.8",
            linewidth=1.8, linestyle="--", color=AMBER, zorder=4
        )
        ax.add_patch(arr)

    ax.text(2.45, 4.90, "Triality\n(order-3 cycle)", ha="center", va="center",
            fontsize=9.3, fontweight="bold", color=AMBER,
            bbox=dict(boxstyle="round,pad=0.22", fc=AMBER_LIGHT, ec=AMBER, lw=0.9))

    # Explanatory callout box at bottom
    ax.text(4.8, 0.58,
            r"Three outer branches ($0$-D Points, $3$-D $+$ Solids, $3$-D $-$ Solids) are completely" "\n"
            r"symmetric around Node $1$ (Lines) under Cartan's triality in $\mathrm{P}\Omega^+(8, q)$.",
            ha="center", va="center", fontsize=8.9, color=SLATE)

    save_fig(fig, out_dir, "maths3_diagrams_d4_triality.png")


# ---------------------------------------------------------------------------
# Exact polar/conic geometry helper for Figures 5 & 6
# ---------------------------------------------------------------------------
def conic_secant_intersections(xP: float, yP: float, slope: float):
    """Intersect ray y = yP + slope * (x - xP) with unit circle x^2 + y^2 = 1
    and polar line x*xP + y*yP = 1."""
    # (1 + m^2) x^2 + 2 m (yP - m xP) x + (yP - m xP)^2 - 1 = 0
    c0 = yP - slope * xP
    qa = 1.0 + slope * slope
    qb = 2.0 * slope * c0
    qc = c0 * c0 - 1.0
    disc = qb * qb - 4.0 * qa * qc
    assert disc > 0, "Line is not a secant!"
    xA = (-qb - math.sqrt(disc)) / (2.0 * qa)
    xB = (-qb + math.sqrt(disc)) / (2.0 * qa)
    if abs(xA - xP) > abs(xB - xP):
        xA, xB = xB, xA
    yA = yP + slope * (xA - xP)
    yB = yP + slope * (xB - xP)

    # Polar line x * xP + y * yP = 1
    # x * xP + (yP + m(x - xP)) * yP = 1 => x (xP + m yP) = 1 - yP^2 + m xP yP
    denom = xP + slope * yP
    xM = (1.0 - yP * yP + slope * xP * yP) / denom
    yM = yP + slope * (xM - xP)
    return (xA, yA), (xM, yM), (xB, yB)


# ---------------------------------------------------------------------------
# Figure 5: Polarity - External Point, Tangents, Secant, Polar Hyperplane
#           (lines 2180-2193)
# ---------------------------------------------------------------------------
def make_fig5_polarity_tangent_polar(out_dir: Path):
    fig, ax = setup_canvas(9.8, 6.0, xlim=(-3.15, 2.45), ylim=(-1.75, 1.85))

    xP, yP = -2.4, 0.0
    x_pol = 1.0 / xP  # -5/12
    y_touch = math.sqrt(1.0 - x_pol * x_pol)  # sqrt(119)/12
    T1 = (x_pol, +y_touch)
    T2 = (x_pol, -y_touch)

    # Verify exact tangency orthogonality: OT_i . PT_i = 0
    for Ti in (T1, T2):
        dot = Ti[0] * (Ti[0] - xP) + Ti[1] * (Ti[1] - yP)
        assert abs(dot) < 1e-13, f"Tangency check failed: {dot}"

    # Draw Quadric Q (unit circle x^2 + y^2 = 1)
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.fill(np.cos(theta), np.sin(theta), color=TEAL_LIGHT, alpha=0.48, zorder=1)
    ax.plot(np.cos(theta), np.sin(theta), color=TEAL, lw=2.5, zorder=3)
    ax.text(0.42, 0.36, "Quadric /\nPolar Space\n" r"$\mathcal{Q}$",
            ha="center", va="center", fontsize=10.2, fontweight="bold", color=TEAL, zorder=4)

    # Polar hyperplane P^pi: vertical line x = x_pol
    ax.plot([x_pol, x_pol], [-1.52, 1.52], color=AMBER, lw=2.8, zorder=5)
    ax.text(x_pol, -1.57,
            r"$P^\pi$ (Polar hyperplane of $P$:" "\n"
            r"passes through all touchpoints $T_i$)",
            ha="center", va="top", fontsize=9.5, fontweight="bold", color=AMBER, zorder=7)

    # Two exact tangent lines from P through T_1 and T_2
    for Ti, sgn in [(T1, +1), (T2, -1)]:
        dx, dy = Ti[0] - xP, Ti[1] - yP
        ext = 1.15 if sgn > 0 else 1.45
        ax.plot([xP, xP + ext * dx], [yP, yP + ext * dy],
                color=BLUE, lw=2.0, zorder=4)
        # Right-angle radius indicator (subtle dashed radius O-T_i)
        ax.plot([0, Ti[0]], [0, Ti[1]], color=TEAL, lw=1.0, ls=":", alpha=0.65, zorder=2)

    # Passant ray from P missing Q completely (lines 2174)
    m_pass = 0.68
    x_end_p = 1.15
    ax.plot([xP, x_end_p], [yP, yP + m_pass * (x_end_p - xP)],
            color=SLATE, lw=1.5, ls="--", zorder=2)
    ax.annotate("", xy=(x_end_p, yP + m_pass * (x_end_p - xP)),
                xytext=(x_end_p - 0.2, yP + m_pass * (x_end_p - 0.2 - xP)),
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.5))
    ax.text(-0.75, 1.32, r"Passant ray (misses $\mathcal{Q}$)",
            ha="center", va="bottom", fontsize=9.0, color=SLATE, rotation=32)

    # Tilted secant ray through P piercing Q at A and B (well separated from tangents)
    m_sec = -0.13
    A, M, B = conic_secant_intersections(xP, yP, m_sec)
    x_sec_end = 1.95
    y_sec_end = yP + m_sec * (x_sec_end - xP)
    ax.plot([xP, x_sec_end], [yP, y_sec_end], color=NAVY, lw=2.0, zorder=5)
    ax.annotate("", xy=(x_sec_end, y_sec_end),
                xytext=(x_sec_end - 0.25, yP + m_sec * (x_sec_end - 0.25 - xP)),
                arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.0))
    ax.text(1.98, y_sec_end, "Secant line\n" r"(hits $\mathcal{Q}$ at $A, B$)",
            ha="left", va="center", fontsize=9.3, fontweight="bold", color=NAVY)

    # Plot points P, T1, T2, A, B
    ax.scatter(xP, yP, s=75, color=RED, edgecolor="white", lw=1.2, zorder=9)
    ax.text(xP - 0.12, yP, r"$P$", ha="right", va="center",
            fontsize=12.5, fontweight="bold", color=RED)
    ax.text(xP - 0.05, yP - 0.23, "(non-isotropic\nexternal point)",
            ha="center", va="top", fontsize=8.6, color=RED)

    ax.scatter(*T1, s=62, color=AMBER, edgecolor=TEXT, lw=1.0, zorder=9)
    ax.text(T1[0] + 0.18, T1[1] + 0.34,
            r"$T_1$ (touchpoint: $P \in T_1^\pi \Leftrightarrow T_1 \in P^\pi$)",
            ha="left", va="center", fontsize=9.5, fontweight="bold", color=BLUE,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="#bfdbfe", lw=0.9),
            zorder=10)
    ax.annotate("", xy=(T1[0] + 0.04, T1[1] + 0.04),
                xytext=(T1[0] + 0.17, T1[1] + 0.25),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1), zorder=9)

    ax.scatter(*T2, s=62, color=AMBER, edgecolor=TEXT, lw=1.0, zorder=9)
    ax.text(T2[0] - 0.14, T2[1] - 0.10, r"$T_2$ (tangent touchpoint)",
            ha="right", va="top", fontsize=9.4, fontweight="bold", color=BLUE, zorder=10)

    ax.scatter(*A, s=50, color=NAVY, zorder=8)
    ax.text(A[0] - 0.14, A[1] + 0.12, r"$A$", ha="center", va="bottom",
            fontsize=11, fontweight="bold", color=NAVY, zorder=10)

    ax.scatter(*B, s=50, color=NAVY, zorder=8)
    ax.text(B[0] + 0.14, B[1] + 0.11, r"$B$", ha="center", va="bottom",
            fontsize=11, fontweight="bold", color=NAVY, zorder=10)

    save_fig(fig, out_dir, "maths3_polarity_tangent_polar.png")


# ---------------------------------------------------------------------------
# Figure 6: Polarity - Harmonic Conjugate & Central Reflection on Secant Line
#           (lines 2206-2211)
# ---------------------------------------------------------------------------
def make_fig6_polarity_harmonic_secant(out_dir: Path):
    fig = plt.figure(figsize=(9.8, 6.9), dpi=220)
    gs = fig.add_gridspec(2, 1, height_ratios=[2.35, 1.15], hspace=0.12)
    ax = fig.add_subplot(gs[0])
    ax_bar = fig.add_subplot(gs[1])

    ax.set_xlim(-3.05, 2.35)
    ax.set_ylim(-1.42, 1.52)
    ax.set_aspect("equal")
    ax.axis("off")

    xP, yP = -2.4, 0.0
    x_pol = 1.0 / xP  # -5/12
    y_touch = math.sqrt(1.0 - x_pol * x_pol)

    # Quadric Q
    theta = np.linspace(0, 2 * np.pi, 400)
    ax.fill(np.cos(theta), np.sin(theta), color=TEAL_LIGHT, alpha=0.45, zorder=1)
    ax.plot(np.cos(theta), np.sin(theta), color=TEAL, lw=2.4, zorder=3)
    ax.text(0.88, 0.85, r"$\mathcal{Q}$", fontsize=12, fontweight="bold", color=TEAL)

    # Faint tangent envelope for visual continuity with Figure 5
    for sgn in (+1, -1):
        ax.plot([xP, x_pol], [yP, sgn * y_touch], color=GREY_LINE, lw=1.2, ls=":", zorder=2)

    # Polar hyperplane (mirror axis P^pi)
    ax.plot([x_pol, x_pol], [-1.28, 1.32], color=AMBER, lw=2.9, zorder=5)
    ax.text(x_pol, 1.36, r"Axis $P^\pi$ (polar mirror hyperplane)",
            ha="center", va="bottom", fontsize=9.8, fontweight="bold", color=AMBER)

    # Primary secant line ell (positive slope)
    m1 = 0.16
    A, M, B = conic_secant_intersections(xP, yP, m1)
    x_end = 1.85
    ax.plot([xP, x_end], [yP, yP + m1 * (x_end - xP)], color=BLUE, lw=2.3, zorder=6)
    ax.annotate("", xy=(x_end, yP + m1 * (x_end - xP)),
                xytext=(x_end - 0.25, yP + m1 * (x_end - 0.25 - xP)),
                arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.2))
    ax.text(1.88, yP + m1 * (x_end - xP), r"Secant line $\ell$",
            ha="left", va="center", fontsize=9.8, fontweight="bold", color=BLUE)

    # Reflection arc A <-> B across M
    refl1 = FancyArrowPatch(
        (A[0] + 0.04, A[1] + 0.11), (B[0] - 0.04, B[1] + 0.11),
        connectionstyle="arc3,rad=-0.28",
        arrowstyle="<->,head_length=5.5,head_width=3.5",
        color=RED, lw=1.6, ls="--", zorder=8
    )
    ax.add_patch(refl1)
    ax.text(0.55, 1.12, r"Reflection $\rho_P : A \leftrightarrow B$",
            ha="left", va="center", fontsize=9.2, fontweight="bold", color=RED,
            bbox=dict(boxstyle="round,pad=0.14", fc="white", ec="#fecaca", lw=0.8),
            zorder=9)

    # Secondary secant line ell' (negative slope) showing reflection works on EVERY secant ray
    m2 = -0.22
    A2, M2, B2 = conic_secant_intersections(xP, yP, m2)
    ax.plot([xP, 1.55], [yP, yP + m2 * (1.55 - xP)], color=SLATE, lw=1.4, ls="--", zorder=4)
    for pt in (A2, B2):
        ax.scatter(*pt, s=32, color=SLATE, zorder=6)
    ax.scatter(*M2, s=34, color=AMBER, zorder=7)
    refl2 = FancyArrowPatch(
        (A2[0] + 0.04, A2[1] - 0.10), (B2[0] - 0.04, B2[1] - 0.10),
        connectionstyle="arc3,rad=0.34",
        arrowstyle="<->,head_length=4.5,head_width=3.0",
        color=SLATE, lw=1.3, ls=":", zorder=6
    )
    ax.add_patch(refl2)
    ax.text(A2[0] - 0.13, A2[1] - 0.14, r"$A'$", fontsize=9.2, color=SLATE, ha="center", va="top")
    ax.text(M2[0] + 0.12, M2[1] - 0.08, r"$M'$", fontsize=9.2, color=AMBER, ha="left", va="top")
    ax.text(B2[0] + 0.12, B2[1] - 0.12, r"$B'$", fontsize=9.2, color=SLATE, ha="center", va="top")

    # Points & labels on primary secant
    ax.scatter(xP, yP, s=76, color=RED, edgecolor="white", lw=1.2, zorder=9)
    ax.text(xP - 0.12, yP + 0.05, r"$P$", ha="right", va="bottom",
            fontsize=12.5, fontweight="bold", color=RED)
    ax.text(xP - 0.05, yP - 0.16, r"(Centre of $\rho_P$)",
            ha="center", va="top", fontsize=8.8, color=RED)

    ax.scatter(*A, s=56, color=NAVY, zorder=9)
    ax.text(A[0] - 0.15, A[1] + 0.12, r"$A$", ha="center", va="bottom",
            fontsize=11.2, fontweight="bold", color=NAVY)

    ax.scatter(*M, s=64, color=AMBER, edgecolor=TEXT, lw=1.0, zorder=10)
    ax.text(M[0] + 0.14, M[1] - 0.18, r"$M = \ell \cap P^\pi$",
            ha="left", va="top", fontsize=9.8, fontweight="bold", color=AMBER,
            bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=AMBER_LIGHT, lw=0.8))

    ax.scatter(*B, s=56, color=NAVY, zorder=9)
    ax.text(B[0] + 0.14, B[1] + 0.10, r"$B$", ha="center", va="bottom",
            fontsize=11.2, fontweight="bold", color=NAVY)

    # --- Bottom panel: 1D directed-segment harmonic ruler along ell ---
    dP = 0.0
    dA = math.hypot(A[0] - xP, A[1] - yP)
    dM = math.hypot(M[0] - xP, M[1] - yP)
    dB = math.hypot(B[0] - xP, B[1] - yP)

    PA = dA - dP
    PB = dB - dP
    MA = dA - dM  # negative directed segment
    MB = dB - dM  # positive directed segment
    cross_ratio = (MA * PB) / (MB * PA)
    assert abs(cross_ratio + 1.0) < 1e-13, f"Harmonic cross-ratio failed: {cross_ratio}"
    assert abs(abs(MA) / abs(MB) - PA / PB) < 1e-13

    ax_bar.set_xlim(-0.52, dB + 0.82)
    ax_bar.set_ylim(-0.95, 1.05)
    ax_bar.axis("off")

    draw_card(ax_bar, -0.45, -0.88, dB + 1.20, 1.86, fc=GREY_BG, ec=GREY_LINE, pad=0.04)
    ax_bar.text(0.5 * (dB + 0.30), 0.75,
                r"1D Harmonic Division on $\ell$:  "
                rf"$|MA| / |MB| = |PA| / |PB| = {PA / PB:.4f}$   $\Rightarrow$   "
                r"$(P, M; A, B) = (A, B; M, P) = -1$",
                ha="center", va="center", fontsize=9.2, fontweight="bold", color=NAVY)

    ax_bar.plot([0.0, dB + 0.35], [0.05, 0.05], color=BLUE, lw=2.3, zorder=3)
    ax_bar.annotate("", xy=(dB + 0.38, 0.05), xytext=(dB + 0.15, 0.05),
                    arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.2))

    pts_1d = [
        (dP, r"$P$", RED),
        (dA, r"$A$", NAVY),
        (dM, r"$M$", AMBER),
        (dB, r"$B$", NAVY),
    ]
    for dx_pos, lbl, col in pts_1d:
        ax_bar.scatter(dx_pos, 0.05, s=62, color=col,
                       edgecolor=TEXT if col == AMBER else "white", lw=0.9, zorder=6)
        ax_bar.text(dx_pos, 0.22, lbl, ha="center", va="bottom",
                    fontsize=11, fontweight="bold", color=col)

    # Internal division arrows |MA| and |MB|
    for s_x, e_x, lbl in [(dA, dM, rf"$|MA|={abs(MA):.2f}$"),
                          (dM, dB, rf"$|MB|={abs(MB):.2f}$")]:
        ax_bar.annotate("", xy=(e_x, -0.24), xytext=(s_x, -0.24),
                        arrowprops=dict(arrowstyle="<->", color=AMBER, lw=1.4))
        ax_bar.text(0.5 * (s_x + e_x), -0.34, lbl, ha="center", va="top",
                    fontsize=8.6, color=AMBER, fontweight="bold")

    # External division |PA| and |PB|
    ax_bar.annotate("", xy=(dA, -0.24), xytext=(dP, -0.24),
                    arrowprops=dict(arrowstyle="<->", color=RED, lw=1.4))
    ax_bar.text(0.5 * (dP + dA), -0.34, rf"$|PA|={PA:.2f}$", ha="center", va="top",
                fontsize=8.6, color=RED, fontweight="bold")

    ax_bar.annotate("", xy=(dB, -0.62), xytext=(dP, -0.62),
                    arrowprops=dict(arrowstyle="<->", color=SLATE, lw=1.3))
    ax_bar.text(0.5 * (dP + dB), -0.66, rf"$|PB|={PB:.2f}$", ha="center", va="top",
                fontsize=8.6, color=SLATE, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none"))

    save_fig(fig, out_dir, "maths3_polarity_harmonic_secant.png")


# ---------------------------------------------------------------------------
# Figure 7: One-or-All Axiom on the 3D Hyperboloid vs Rank >= 3 Polar Space
#           (lines 2331-2341)
# ---------------------------------------------------------------------------
def r_plus(theta: float, s: float) -> np.ndarray:
    """Regulus R ruling on x^2 + y^2 - z^2 = 1."""
    return np.array([math.cos(theta) - s * math.sin(theta),
                     math.sin(theta) + s * math.cos(theta),
                     s])


def r_minus(phi: float, t: float) -> np.ndarray:
    """Opposite regulus R' ruling on x^2 + y^2 - z^2 = 1."""
    return np.array([math.cos(phi) + t * math.sin(phi),
                     math.sin(phi) - t * math.cos(phi),
                     t])


def intersect_opposite_rulings(theta_L: float, phi_P: float) -> tuple[float, np.ndarray]:
    """Exact intersection point Q of r_plus(theta_L, s) and r_minus(phi_P, s).
    Since z = s = t, solving (cos theta_L - s sin theta_L, sin theta_L + s cos theta_L)
    = (cos phi_P + s sin phi_P, sin phi_P - s cos phi_P) gives
    s = tan((phi_P - theta_L)/2)."""
    half = 0.5 * (phi_P - theta_L)
    s_Q = math.tan(half)
    Q = r_plus(theta_L, s_Q)
    Q_check = r_minus(phi_P, s_Q)
    assert np.linalg.norm(Q - Q_check) < 1e-12
    assert abs(Q[0]**2 + Q[1]**2 - Q[2]**2 - 1.0) < 1e-12
    return s_Q, Q


def make_fig7_polar_one_or_all(out_dir: Path):
    fig = plt.figure(figsize=(11.0, 5.5), dpi=220)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.18, 1.0], wspace=0.08)

    # --- Panel (a): 3D Hyperboloid of One Sheet (Case 1: EXACTLY ONE point Q) ---
    ax3 = fig.add_subplot(gs[0], projection="3d")
    ax3.set_facecolor("white")

    z_grid = np.linspace(-1.25, 1.25, 48)
    th_grid = np.linspace(0, 2 * np.pi, 72)
    TH, ZZ = np.meshgrid(th_grid, z_grid)
    RR = np.sqrt(1.0 + ZZ**2)
    XX = RR * np.cos(TH)
    YY = RR * np.sin(TH)

    ax3.plot_surface(XX, YY, ZZ, color=TEAL_LIGHT, alpha=0.22,
                     edgecolor="none", shade=True, zorder=1)

    # Subtle background rulings from both reguli
    s_vals = np.linspace(-1.25, 1.25, 40)
    for k in range(12):
        ang = 2 * np.pi * k / 12
        pts_p = np.array([r_plus(ang, sv) for sv in s_vals])
        pts_m = np.array([r_minus(ang, sv) for sv in s_vals])
        ax3.plot(pts_p[:, 0], pts_p[:, 1], pts_p[:, 2], color="#94a3b8", lw=0.55, alpha=0.45)
        ax3.plot(pts_m[:, 0], pts_m[:, 1], pts_m[:, 2], color="#94a3b8", lw=0.45, alpha=0.35)

    # Chosen line L in R and point P on Q \ L (facing camera cleanly at azim=-52, elev=20)
    theta_L = math.radians(-85.0)
    phi_P = math.radians(-18.0)
    t_P = -0.58
    P = r_minus(phi_P, t_P)
    assert abs(P[0]**2 + P[1]**2 - P[2]**2 - 1.0) < 1e-12

    s_Q, Q = intersect_opposite_rulings(theta_L, phi_P)
    # Second point R on L \ {Q}: chord PR pokes into hollow interior!
    s_R = -0.82
    R_pt = r_plus(theta_L, s_R)
    mid_PR = 0.5 * (P + R_pt)
    val_mid = mid_PR[0]**2 + mid_PR[1]**2 - mid_PR[2]**2
    assert val_mid < 1.0 - 0.15, f"Midpoint of PR should lie off Q: {val_mid}"

    # Verify every point of L and PQ lies on Q
    for u in np.linspace(-1.25, 1.25, 25):
        ptL = r_plus(theta_L, u)
        ptPQ = r_minus(phi_P, u)
        assert abs(ptL[0]**2 + ptL[1]**2 - ptL[2]**2 - 1.0) < 1e-12
        assert abs(ptPQ[0]**2 + ptPQ[1]**2 - ptPQ[2]**2 - 1.0) < 1e-12

    # Draw line L (bold royal blue)
    L_pts = np.array([r_plus(theta_L, sv) for sv in np.linspace(-1.25, 1.25, 50)])
    ax3.plot(L_pts[:, 0], L_pts[:, 1], L_pts[:, 2], color=BLUE, lw=3.0, zorder=6)

    # Draw unique opposite-regulus line through P and Q (bold teal)
    PQ_pts = np.array([r_minus(phi_P, sv) for sv in np.linspace(-1.25, 1.25, 50)])
    ax3.plot(PQ_pts[:, 0], PQ_pts[:, 1], PQ_pts[:, 2], color=TEAL, lw=2.8, zorder=7)

    # Draw ambient non-surface line P-R (dashed crimson)
    ax3.plot([P[0], R_pt[0]], [P[1], R_pt[1]], [P[2], R_pt[2]],
             color=RED, lw=2.1, ls="--", zorder=8)

    # Points P, Q, R
    ax3.scatter([P[0]], [P[1]], [P[2]], s=65, color=NAVY, edgecolor="white", lw=1.0, zorder=10)
    ax3.scatter([Q[0]], [Q[1]], [Q[2]], s=72, color=AMBER, edgecolor=TEXT, lw=1.0, zorder=10)
    ax3.scatter([R_pt[0]], [R_pt[1]], [R_pt[2]], s=48, color=RED, edgecolor="white", lw=0.9, zorder=10)

    lbl_box3 = dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.86)
    ax3.text(P[0] + 0.24, P[1] + 0.10, P[2] - 0.10, r"$P \in \mathcal{Q}$",
             fontsize=10.2, fontweight="bold", color=NAVY, bbox=lbl_box3)
    ax3.text(Q[0] + 0.30, Q[1] + 0.05, Q[2] - 0.02, r"$Q$ (unique)",
             fontsize=9.8, fontweight="bold", color=AMBER, bbox=lbl_box3)
    ax3.text(R_pt[0] - 0.26, R_pt[1] - 0.26, R_pt[2] - 0.16, r"$R$",
             fontsize=9.8, fontweight="bold", color=RED, bbox=lbl_box3)
    ax3.text(mid_PR[0], mid_PR[1] - 0.18, mid_PR[2] - 0.24, r"ambient $PR$",
             fontsize=8.8, fontweight="bold", color=RED, bbox=lbl_box3)
    L_top = r_plus(theta_L, 1.18)
    ax3.text(L_top[0] - 0.08, L_top[1] - 0.18, L_top[2] + 0.12, r"Line $L \subset \mathcal{Q}$",
             fontsize=9.8, fontweight="bold", color=BLUE, bbox=lbl_box3)

    ax3.view_init(elev=19, azim=-46)
    ax3.set_xlim(-1.6, 1.6)
    ax3.set_ylim(-1.6, 1.6)
    ax3.set_zlim(-1.35, 1.35)
    ax3.set_box_aspect((1, 1, 0.86))
    ax3.axis("off")
    ax3.set_title("(a) \"One\" Case: Hyperboloid $Q^+(3, \\mathbb{R})$ (Rank 2)\n"
                  "Unique line $PQ \\subset \\mathcal{Q}$; any other $PR$ pokes off $\\mathcal{Q}$",
                  fontsize=9.8, fontweight="bold", color=TEXT, pad=2)

    # --- Panel (b): "All" Case in Rank >= 3 (Klein Quadric Q^+(5, K)) ---
    ax2 = fig.add_subplot(gs[1])
    ax2.set_xlim(0, 6.0)
    ax2.set_ylim(0, 5.4)
    ax2.set_aspect("equal")
    ax2.axis("off")

    ax2.text(3.0, 5.05,
             "(b) \"All\" Case: Rank $\\geq 3$ (e.g. $Q^+(5, K)$)\n"
             "Every line $PQ_i$ lies in $\\mathcal{Q}$, spanning plane $\\Pi \\subset \\mathcal{Q}$",
             ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    # Ambient curved quadric hint
    th_arc = np.linspace(0.18, np.pi - 0.18, 200)
    ax2.fill_between(3.0 + 2.75 * np.cos(th_arc), 0.35,
                     0.75 + 3.70 * np.sin(th_arc), color=TEAL_LIGHT, alpha=0.25, zorder=0)
    ax2.plot(3.0 + 2.75 * np.cos(th_arc), 0.75 + 3.70 * np.sin(th_arc),
             color=TEAL, lw=1.6, ls=":", alpha=0.7, zorder=1)
    ax2.text(4.65, 3.92, r"Polar space $\mathcal{Q}$", fontsize=9.2, color=TEAL, fontweight="bold")

    # Totally isotropic plane Pi = P v L lying completely inside Q
    plane_pts = [(0.65, 0.85), (5.05, 0.85), (5.45, 3.45), (1.05, 3.45)]
    plane = Polygon(plane_pts, closed=True, facecolor=BLUE_LIGHT, edgecolor=BLUE,
                    lw=1.8, alpha=0.75, zorder=2)
    ax2.add_patch(plane)
    ax2.text(1.22, 3.16, r"Plane $\Pi = P \vee L \subset \mathcal{Q}$",
             ha="left", va="center", fontsize=9.2, fontweight="bold", color=NAVY)

    # Point P and line L inside Pi
    P2 = (3.05, 2.74)
    L1, L2 = (1.10, 1.32), (4.85, 1.32)
    ax2.plot([L1[0], L2[0]], [L1[1], L2[1]], color=BLUE, lw=3.0, zorder=5)
    ax2.text(4.92, 1.32, r"$L$", ha="left", va="center",
             fontsize=11, fontweight="bold", color=BLUE)

    # Fan of polar-space lines from P to EVERY point on L
    fracs = [0.10, 0.30, 0.50, 0.70, 0.90]
    for idx_f, fr in enumerate(fracs, start=1):
        qx = L1[0] + fr * (L2[0] - L1[0])
        qy = L1[1] + fr * (L2[1] - L1[1])
        dx, dy = qx - P2[0], qy - P2[1]
        ax2.plot([P2[0], P2[0] + 1.15 * dx], [P2[1], P2[1] + 1.15 * dy],
                 color=TEAL, lw=2.0, zorder=4)
        ax2.scatter(qx, qy, s=42, color=AMBER, edgecolor=TEXT, lw=0.8, zorder=6)
        ax2.text(qx, qy - 0.24, rf"$Q_{idx_f}$", ha="center", va="top",
                 fontsize=9.0, color=TEXT, fontweight="bold")

    ax2.scatter(*P2, s=68, color=NAVY, edgecolor="white", lw=1.1, zorder=8)
    ax2.text(P2[0] + 0.16, P2[1] + 0.12, r"$P \in \mathcal{Q} \setminus L$",
             ha="left", va="bottom", fontsize=9.8, fontweight="bold", color=NAVY)

    ax2.text(3.0, 0.36,
             r"All lines $PQ_i$ belong to $\mathcal{Q}$ $\Rightarrow$ $\Pi \cong \mathrm{PG}(2, K)$ inside $\mathcal{Q}$",
             ha="center", va="center", fontsize=8.9, color=SLATE)

    save_fig(fig, out_dir, "maths3_polar_one_or_all.png")


# ---------------------------------------------------------------------------
# Figure 8: C_4 vs D_4 Fork for Generator Families of Q^+(7, q)
#           (lines 2977-2984)
# ---------------------------------------------------------------------------
def make_fig8_polar_d4_generators(out_dir: Path):
    # Verify exact point and generator counts for Q^+(7, q) (n=4, e=0)
    for q in (2, 3, 4):
        pts_formula = ((q**4 - 1) * (q**3 + 1)) // (q - 1)
        fam_size = (q + 1) * (q**2 + 1) * (q**3 + 1)
        gen_total = (1 + 1) * (q + 1) * (q**2 + 1) * (q**3 + 1)
        assert pts_formula == fam_size
        assert gen_total == 2 * fam_size

    fig, ax = setup_canvas(11.2, 5.5, xlim=(0, 11.2), ylim=(0, 5.5))

    # Left card: General Rank-4 Polar Space (C_4, e > 0)
    draw_card(ax, 0.15, 0.25, 4.55, 5.0, fc=GREY_BG, ec=GREY_LINE)
    ax.text(2.42, 4.88, "General Rank-4 Polar Space ($C_4$)",
            ha="center", va="center", fontsize=10.2, fontweight="bold", color=TEXT)
    ax.text(2.42, 4.52, r"(for $e > 0$: asymmetric ends)",
            ha="center", va="center", fontsize=8.9, color=SLATE)

    xs_c4 = [0.64, 1.72, 2.80, 3.92]
    lbl_c4 = ["Points", "Lines", "Planes", "Generators"]
    yc4 = 2.95
    for idx in range(4):
        draw_bt_node(ax, xs_c4[idx], yc4, rf"${idx}$", lbl_c4[idx], r=0.21)
    draw_bt_bond(ax, (xs_c4[0], yc4), (xs_c4[1], yc4), order=1, r=0.21)
    draw_bt_bond(ax, (xs_c4[1], yc4), (xs_c4[2], yc4), order=1, r=0.21)
    draw_bt_bond(ax, (xs_c4[2], yc4), (xs_c4[3], yc4), order=2, r=0.21)

    ax.text(2.42, 1.35,
            r"Double bond at the generator end:" "\n"
            r"$|\mathrm{Points}| \neq |\mathrm{Generators}|$" "\n"
            r"Reversing the diagram gives a" "\n"
            r"distinct Dual Polar Space.",
            ha="center", va="center", fontsize=8.9, color=SLATE,
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=GREY_LINE))

    # Right card: Hyperbolic Quadric Q^+(7, q) (n = 4, e = 0 -> D_4 fork)
    draw_card(ax, 4.85, 0.25, 6.20, 5.0, fc=BLUE_PALE, ec="#bfdbfe")
    ax.text(7.95, 4.88, r"Hyperbolic Quadric $Q^+(7, q)$ ($n = 4, e = 0$: $D_4$ Fork)",
            ha="center", va="center", fontsize=10.4, fontweight="bold", color=NAVY)
    ax.text(7.95, 4.52, "Generators (3-spaces) split into 2 equal families",
            ha="center", va="center", fontsize=8.9, color=SLATE)

    p0 = (5.84, 2.80)
    p1 = (7.12, 2.80)
    g1 = (8.26, 3.82)
    g2 = (8.26, 1.78)

    draw_bt_bond(ax, p0, p1, order=1, r=0.24)
    draw_bt_bond(ax, p1, g1, order=1, r=0.24, color=TEAL)
    draw_bt_bond(ax, p1, g2, order=1, r=0.24, color=TEAL)

    draw_bt_node(ax, *p0, r"$0$", "Points", r"$(q+1)(q^2+1)(q^3+1)$",
                 r=0.24, fc="white", ec=NAVY)
    draw_bt_node(ax, *p1, r"$1$", "Lines", None, r=0.24, fc="white", ec=NAVY)
    draw_bt_node(ax, *g1, r"$+$", "Generator Family 1",
                 r"$(q+1)(q^2+1)(q^3+1)$",
                 r=0.24, fc=TEAL_LIGHT, ec=TEAL, label_side="right")
    draw_bt_node(ax, *g2, r"$-$", "Generator Family 2",
                 r"$(q+1)(q^2+1)(q^3+1)$",
                 r=0.24, fc=TEAL_LIGHT, ec=TEAL, label_side="right")

    ax.text(7.95, 0.72,
            r"Total generators $= 2(q+1)(q^2+1)(q^3+1) = 2 \times |\mathrm{Points}|$"
            "\n" r"(at $q = 2$: $135$ points and $135 + 135 = 270$ generators)",
            ha="center", va="center", fontsize=8.5, color=NAVY, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="#bfdbfe"))

    save_fig(fig, out_dir, "maths3_polar_d4_generators.png")


# ---------------------------------------------------------------------------
# Figure 9: Rank-3 Polar Space C_3 Diagram and Thin q=1 Octahedron
#           (lines 3029-3034)
# ---------------------------------------------------------------------------
def project_octahedron(cx: float, cy: float, scale: float = 0.95):
    pts3 = {
        "N": ( 0.0,  0.0,  1.05),
        "S": ( 0.0,  0.0, -1.05),
        "E": ( 1.0,  0.0,  0.0),
        "W": (-1.0,  0.0,  0.0),
        "F": ( 0.0, -1.0,  0.0),
        "B": ( 0.0,  1.0,  0.0),
    }
    out = {}
    for k, (X, Y, Z) in pts3.items():
        px = cx + scale * (0.88 * X + 0.38 * Y)
        py = cy + scale * (0.86 * Z + 0.25 * Y - 0.10 * X)
        out[k] = (px, py)
    return out


OCT_OPPOSITES = [{"N", "S"}, {"E", "W"}, {"F", "B"}]
OCT_VERTS = ["N", "S", "E", "W", "F", "B"]
OCT_EDGES = [
    (u, v) for i, u in enumerate(OCT_VERTS) for v in OCT_VERTS[i + 1:]
    if {u, v} not in OCT_OPPOSITES
]


def make_fig9_polar_c3_octahedron(out_dir: Path):
    assert len(OCT_EDGES) == 12
    fig, ax = setup_canvas(10.6, 6.5, xlim=(0, 10.6), ylim=(0, 6.5))

    # Top panel: Rank-3 Polar Space C_3 diagram + duality note with Cube
    draw_card(ax, 0.2, 3.85, 10.2, 2.48, fc=BLUE_PALE, ec="#bfdbfe")
    ax.text(5.3, 6.02, r"Rank-3 Polar Space Diagram ($C_3$) vs. Dual 3D Cube",
            ha="center", va="center", fontsize=11.4, fontweight="bold", color=NAVY)

    n0, n1, n2 = (2.0, 5.08), (5.3, 5.08), (8.6, 5.08)
    draw_bt_node(ax, *n0, r"$0$", "Points", "(Type 0)")
    draw_bt_node(ax, *n1, r"$1$", "Lines", "(Type 1)")
    draw_bt_node(ax, *n2, r"$2$", "Planes", "(Type 2)")

    draw_bt_bond(ax, n0, n1, order=1,
                 top_label=r"Projective Plane $\mathrm{PG}(2, q)$",
                 bottom_label=r"fix a Plane $\Pi$")
    draw_bt_bond(ax, n1, n2, order=2,
                 top_label="Generalized Quadrangle",
                 bottom_label=r"fix a Point $P$")

    ax.text(5.3, 4.08,
            r"Swapping Points and Planes reverses the diagram to the dual 3D Cube; "
            r"at $q = 1$, this $C_3$ polar space is the 3D Octahedron.",
            ha="center", va="center", fontsize=8.5, color=NAVY, style="italic")

    # Bottom two insets: Thin q=1 Rank-3 Polar Space = Regular Octahedron
    # Equation x_0 x_1 + x_2 x_3 + x_4 x_5 = 0 -> 3 opposite pairs {N,S}, {E,W}, {F,B}
    draw_card(ax, 0.2, 0.15, 5.0, 3.52, fc=GREY_BG, ec=GREY_LINE)
    draw_card(ax, 5.4, 0.15, 5.0, 3.52, fc=GREY_BG, ec=GREY_LINE)

    ax.text(2.7, 3.38,
            r"(a) Fix a Plane (Face $\{N, E, F\}$) $\Rightarrow$ bond $0 - 1$",
            ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEXT)
    ax.text(2.7, 0.42,
            "3 vertices & 3 edges on the face form a triangle (thin PP)",
            ha="center", va="center", fontsize=8.8, color=SLATE)

    ax.text(7.9, 3.38,
            r"(b) Fix a Point (Vertex $N$) $\Rightarrow$ bond $1 = 2$",
            ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEXT)
    ax.text(7.9, 0.42,
            r"4 edges & 4 faces around $N$ form a square (thin GQ)",
            ha="center", va="center", fontsize=8.8, color=SLATE)

    lbl_off = {
        "N": (0.0, 0.16),
        "S": (0.0, -0.20),
        "E": (0.17, -0.02),
        "W": (-0.18, 0.02),
        "F": (-0.15, -0.14),
        "B": (-0.14, 0.08),
    }

    # --- Inset (a): Octahedron highlighting face {N, E, F} ---
    oct_a = project_octahedron(2.7, 1.88, scale=0.95)
    back_edges = {("N", "B"), ("S", "B"), ("E", "B"), ("W", "B"), ("B", "N"), ("B", "S"), ("B", "E"), ("B", "W")}
    for u, v in OCT_EDGES:
        is_back = (u, v) in back_edges
        ax.plot([oct_a[u][0], oct_a[v][0]], [oct_a[u][1], oct_a[v][1]],
                color="#cbd5e1", lw=1.2, ls="--" if is_back else "-", zorder=2)

    face_nef = Polygon([oct_a["N"], oct_a["E"], oct_a["F"]], closed=True,
                       facecolor=AMBER_LIGHT, edgecolor=BLUE, lw=2.6, alpha=0.85, zorder=5)
    ax.add_patch(face_nef)
    for k, pt in oct_a.items():
        col = NAVY if k in ("N", "E", "F") else "#94a3b8"
        sz = 48 if k in ("N", "E", "F") else 28
        ax.scatter(*pt, s=sz, color=col, zorder=7)
        ox, oy = lbl_off[k]
        ax.text(pt[0] + ox, pt[1] + oy, rf"${k}$", ha="center", va="center",
                fontsize=9.2, fontweight="bold", color=col, zorder=8)

    # --- Inset (b): Octahedron highlighting fixed point N & its 4 edges/4 faces ---
    oct_b = project_octahedron(7.9, 1.88, scale=0.95)
    for u, v in OCT_EDGES:
        is_back = (u, v) in back_edges
        ax.plot([oct_b[u][0], oct_b[v][0]], [oct_b[u][1], oct_b[v][1]],
                color="#cbd5e1", lw=1.2, ls="--" if is_back else "-", zorder=2)

    # 4 triangular faces meeting at N
    eq_cycle = ["E", "B", "W", "F"]
    for idx_f in range(4):
        v1, v2 = eq_cycle[idx_f], eq_cycle[(idx_f + 1) % 4]
        fc_tri = BLUE_LIGHT if idx_f % 2 == 0 else TEAL_LIGHT
        tri = Polygon([oct_b["N"], oct_b[v1], oct_b[v2]], closed=True,
                      facecolor=fc_tri, edgecolor="none", alpha=0.48, zorder=3)
        ax.add_patch(tri)

    # 4 edges through N + dashed 4-cycle vertex figure
    vfig_sq = []
    for nb in eq_cycle:
        ax.plot([oct_b["N"][0], oct_b[nb][0]], [oct_b["N"][1], oct_b[nb][1]],
                color=BLUE, lw=2.5, zorder=5)
        vfig_sq.append((0.60 * oct_b["N"][0] + 0.40 * oct_b[nb][0],
                        0.60 * oct_b["N"][1] + 0.40 * oct_b[nb][1]))

    sq_patch = Polygon(vfig_sq, closed=True, facecolor="none", edgecolor=TEAL,
                       lw=1.9, ls="--", zorder=6)
    ax.add_patch(sq_patch)
    for sp in vfig_sq:
        ax.scatter(*sp, s=26, color=TEAL, zorder=7)

    for k, pt in oct_b.items():
        if k == "N":
            ax.scatter(*pt, s=74, color=AMBER, edgecolor=TEXT, lw=1.0, zorder=9)
        else:
            col = NAVY if k in eq_cycle else "#94a3b8"
            ax.scatter(*pt, s=34, color=col, zorder=7)
        ox, oy = lbl_off[k]
        ax.text(pt[0] + ox, pt[1] + oy, rf"${k}$", ha="center", va="center",
                fontsize=9.2, fontweight="bold",
                color=AMBER if k == "N" else (TEXT if k in eq_cycle else "#94a3b8"),
                zorder=9)

    save_fig(fig, out_dir, "maths3_polar_c3_octahedron.png")


# ---------------------------------------------------------------------------
# Figure 10: Hollow Triangle (Impossible) vs Filled Triangle (Rank >= 3)
#            (lines 3082-3090)
# ---------------------------------------------------------------------------
def make_fig10_gq_hollow_vs_filled(out_dir: Path):
    fig, ax = setup_canvas(11.0, 5.7, xlim=(0, 11.0), ylim=(0, 5.7))

    # Left panel: "Hollow" Triangle (Impossible in any polar space S)
    draw_card(ax, 0.15, 0.15, 5.20, 5.40, fc="#fffafa", ec="#fecaca")
    ax.text(2.75, 5.20, "(a) \"Hollow\" Triangle: IMPOSSIBLE in $S$",
            ha="center", va="center", fontsize=10.3, fontweight="bold", color=RED)
    ax.text(2.75, 4.84, r"Boundary $AB, BC, CA \subset S$, but chord $AD$ pokes out",
            ha="center", va="center", fontsize=8.9, color=SLATE)

    A1 = (2.75, 4.18)
    B1 = (0.95, 1.58)
    C1 = (4.55, 1.58)
    D1 = (2.75, 1.58)

    # Soft patch hinting that S curves away from the interior of ABC
    outer_tri = Polygon([A1, B1, C1], closed=True, facecolor="#f1f5f9",
                        edgecolor="none", zorder=1)
    ax.add_patch(outer_tri)
    hole = Circle((2.75, 2.48), 0.56, facecolor="white", edgecolor="#fca5a5",
                  lw=1.3, ls=":", zorder=2)
    ax.add_patch(hole)

    # 3 boundary lines in S
    for p_s, p_e in [(A1, B1), (B1, C1), (C1, A1)]:
        ax.plot([p_s[0], p_e[0]], [p_s[1], p_e[1]], color=BLUE, lw=3.0, zorder=5)

    # Interior line AD poking out into ambient space (only A and D lie in S!)
    ax.plot([A1[0], D1[0]], [A1[1], D1[1]], color=RED, lw=2.4, ls="--", zorder=6)
    ax.text(2.58, 2.95, r"$AD$ outside $S$?", ha="right", va="center",
            fontsize=8.8, fontweight="bold", color=RED,
            bbox=dict(boxstyle="round,pad=0.14", fc="white", ec="#fecaca"), zorder=9)
    ax.text(2.92, 2.02, "ambient\n" r"$\mathrm{PG}(d, K)$",
            ha="left", va="center", fontsize=8.3, color=RED, style="italic", zorder=9)

    # Red X in the middle of AD
    ax.scatter(2.75, 2.48, s=90, marker="x", color=RED, lw=2.5, zorder=8)

    for pt, lbl, off in [(A1, r"$A$", (0.0, 0.16)),
                         (B1, r"$B$", (-0.18, -0.06)),
                         (C1, r"$C$", (0.18, -0.06)),
                         (D1, r"$D$", (0.0, -0.24))]:
        col = AMBER if lbl == r"$D$" else NAVY
        ax.scatter(*pt, s=58, color=col, edgecolor="white", lw=1.0, zorder=9)
        ax.text(pt[0] + off[0], pt[1] + off[1], lbl, ha="center", va="center",
                fontsize=11.2, fontweight="bold", color=col)

    ax.text(2.75, 0.68,
            r"Ruled out by One-or-All: $A$ already joins $B, C \in BC$" "\n"
            r"in $S$, so $A$ is forced to join EVERY $D \in BC$ in $S$.",
            ha="center", va="center", fontsize=8.4, color=RED, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.22", fc=RED_LIGHT, ec="#fca5a5"))

    # Right panel: "Filled" Triangle (Projective plane <A,B,C> inside S)
    draw_card(ax, 5.65, 0.15, 5.20, 5.40, fc=BLUE_PALE, ec="#bfdbfe")
    ax.text(8.25, 5.20, "(b) \"Filled\" Triangle: Full Plane $\\langle A, B, C \\rangle \\subseteq S$",
            ha="center", va="center", fontsize=10.3, fontweight="bold", color=NAVY)
    ax.text(8.25, 4.84, r"Every cross-line $AD$ lies completely inside $S$",
            ha="center", va="center", fontsize=8.9, color=SLATE)

    A2 = (8.25, 4.18)
    B2 = (6.45, 1.58)
    C2 = (10.05, 1.58)
    D2 = (8.25, 1.58)

    # Filled singular plane patch
    filled_tri = Polygon([A2, B2, C2], closed=True, facecolor=TEAL_LIGHT,
                         edgecolor=BLUE, lw=3.0, alpha=0.72, zorder=3)
    ax.add_patch(filled_tri)

    # Interior fan of lines from A and transverse lines inside <A,B,C>
    for fr in (0.20, 0.35, 0.50, 0.65, 0.80):
        qx = B2[0] + fr * (C2[0] - B2[0])
        qy = B2[1]
        lw_i = 2.6 if abs(fr - 0.50) < 1e-6 else 1.4
        col_i = TEAL if abs(fr - 0.50) < 1e-6 else BLUE
        ax.plot([A2[0], qx], [A2[1], qy], color=col_i, lw=lw_i, alpha=0.85, zorder=5)

    for h_fr in (0.32, 0.62):
        pL = (A2[0] + h_fr * (B2[0] - A2[0]), A2[1] + h_fr * (B2[1] - A2[1]))
        pR = (A2[0] + h_fr * (C2[0] - A2[0]), A2[1] + h_fr * (C2[1] - A2[1]))
        ax.plot([pL[0], pR[0]], [pL[1], pR[1]], color=BLUE, lw=1.1, alpha=0.55, zorder=4)

    ax.text(8.38, 2.75, r"$AD \subset S$", ha="left", va="center",
            fontsize=9.6, fontweight="bold", color=TEAL,
            bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=TEAL, lw=0.9), zorder=8)

    for pt, lbl, off in [(A2, r"$A$", (0.0, 0.16)),
                         (B2, r"$B$", (-0.18, -0.06)),
                         (C2, r"$C$", (0.18, -0.06)),
                         (D2, r"$D$", (0.0, -0.24))]:
        col = AMBER if lbl == r"$D$" else NAVY
        ax.scatter(*pt, s=58, color=col, edgecolor="white", lw=1.0, zorder=9)
        ax.text(pt[0] + off[0], pt[1] + off[1], lbl, ha="center", va="center",
                fontsize=11.2, fontweight="bold", color=col)

    ax.text(8.25, 0.68,
            r"Occurs in rank $\geq 3$ (e.g. $Q^+(5, K)$).  In rank-2 GQs" "\n"
            r"(e.g. $Q^+(3, K)$, no planes in $S$), NO triangles exist!",
            ha="center", va="center", fontsize=8.4, color=NAVY, fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.22", fc="white", ec="#93c5fd"))

    save_fig(fig, out_dir, "maths3_gq_hollow_vs_filled.png")


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_dir>", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating 10 Maths 3 Projective Geometry figures in {out_dir} ...")
    make_fig1_cube_diagram(out_dir)
    make_fig2_pg3_diagram(out_dir)
    make_fig3_deleting_nodes(out_dir)
    make_fig4_d4_triality(out_dir)
    make_fig5_polarity_tangent_polar(out_dir)
    make_fig6_polarity_harmonic_secant(out_dir)
    make_fig7_polar_one_or_all(out_dir)
    make_fig8_polar_d4_generators(out_dir)
    make_fig9_polar_c3_octahedron(out_dir)
    make_fig10_gq_hollow_vs_filled(out_dir)
    print("All 10 figures generated and verified successfully.")


if __name__ == "__main__":
    main()
