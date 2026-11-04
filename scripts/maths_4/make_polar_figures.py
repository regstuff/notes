#!/usr/bin/env python3
"""Figures 20 to 23 for the chapter "Polar spaces" (Maths 4).

Usage:
    python3 make_polar_figures.py [OUTPUT_DIR]

Writes four PNGs into OUTPUT_DIR (default: docs/maths/figures in this repository):
  maths4_polar_disjoint_lines.png       (Figure 20) The three collinearity patterns between two disjoint lines in Q+(7, 2)
  maths4_polar_common_neighbours.png    (Figure 21) The common-neighbour subspace a^perp cap b^perp in W(5, 2)
  maths4_polar_line_classes.png         (Figure 22) The four line classes and the trace equation on hyperbolic lines
  maths4_polar_nucleus_isomorphism.png  (Figure 23) Projecting Q(4, 2) from its nucleus onto W(3, 2)
"""

from __future__ import annotations

import itertools
import sys
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Polygon
import numpy as np


DEFAULT_OUT_DIR = Path(__file__).resolve().parents[2] / "docs" / "maths" / "figures"
OUT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT_DIR

# Consistent textbook palette matching Maths 3 / Maths 4
NAVY = "#1e293b"
SLATE = "#475569"
MUTED = "#64748b"
LIGHT_SLATE = "#cbd5e1"
PALE_BG = "#f8fafc"

BLUE_FILL = "#dbeafe"
BLUE_EDGE = "#1d4ed8"
TEAL_FILL = "#ccfbf1"
TEAL_EDGE = "#0f766e"
AMBER_FILL = "#fef3c7"
AMBER_EDGE = "#b45309"
ROSE_FILL = "#ffe4e6"
ROSE_EDGE = "#be123c"
PURPLE_FILL = "#f3e8ff"
PURPLE_EDGE = "#6d28d9"
GREEN_FILL = "#dcfce7"
GREEN_EDGE = "#15803d"
GRAY_FILL = "#f1f5f9"
GRAY_EDGE = "#64748b"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.edgecolor": SLATE,
    "axes.linewidth": 0.8,
})


def fmt_vec(v: tuple[int, ...], basis_name: str = "e") -> str:
    """Format a binary vector as a sum of basis vectors e_i (1-indexed)."""
    terms = [f"{basis_name}_{{{i + 1}}}" for i, bit in enumerate(v) if bit]
    return "+".join(terms)


# ============================================================================
# Figure 20: Three configurations of two disjoint lines in a polar space
# ============================================================================
def build_figure_18() -> Path:
    """Verify the three disjoint-line relations in Q+(7, 2) and plot Figure 20."""
    def q_form(x: tuple[int, ...]) -> int:
        return (x[0] * x[1] + x[2] * x[3] + x[4] * x[5] + x[6] * x[7]) % 2

    def b_form(x: tuple[int, ...], y: tuple[int, ...]) -> int:
        return q_form(tuple((a + b) % 2 for a, b in zip(x, y))) ^ q_form(x) ^ q_form(y)

    pts = [
        v for v in itertools.product((0, 1), repeat=8)
        if any(v) and q_form(v) == 0
    ]
    assert len(pts) == 135, f"Expected 135 points in Q+(7,2), got {len(pts)}"

    def make_line(u: tuple[int, ...], v: tuple[int, ...]) -> list[tuple[int, ...]]:
        w = tuple((a ^ b) for a, b in zip(u, v))
        line = [u, v, w]
        assert len(set(line)) == 3
        for p in line:
            assert q_form(p) == 0
        assert b_form(u, v) == 0
        return line

    e = [tuple(1 if j == i else 0 for j in range(8)) for i in range(8)]
    L1 = make_line(e[0], e[2])  # <e_1, e_3> = {e_1, e_3, e_1+e_3}

    # Case (a): all-to-all collinearity, L2 = <e_5, e_7>
    L2_all = make_line(e[4], e[6])
    edges_all = [(i, j) for i, x in enumerate(L1) for j, y in enumerate(L2_all) if b_form(x, y) == 0]
    assert len(edges_all) == 9

    # Case (b): unique hub x_1 in L_1 and x_2 in L_2, L2 = <e_5, e_4>
    L2_hub = make_line(e[4], e[3])  # {e_5, e_4, e_4+e_5}
    edges_hub = [(i, j) for i, x in enumerate(L1) for j, y in enumerate(L2_hub) if b_form(x, y) == 0]
    assert len(edges_hub) == 5
    assert [j for i, j in edges_hub if i == 0] == [0, 1, 2]
    assert [i for i, j in edges_hub if j == 0] == [0, 1, 2]

    # Case (c): bijective matching, L2 = <e_4, e_2>
    L2_bij = [e[3], e[1], tuple(a ^ b for a, b in zip(e[3], e[1]))]
    for p in L2_bij:
        assert q_form(p) == 0
    assert b_form(L2_bij[0], L2_bij[1]) == 0
    edges_bij = [(i, j) for i, x in enumerate(L1) for j, y in enumerate(L2_bij) if b_form(x, y) == 0]
    assert edges_bij == [(0, 0), (1, 1), (2, 2)]

    fig, axes = plt.subplots(1, 3, figsize=(13.6, 4.9), dpi=180)
    fig.patch.set_facecolor("white")

    cases = [
        (
            axes[0],
            "(a) All-to-all collinear",
            r"$L_1 = \langle e_1, e_3 \rangle,\;\; L_2 = \langle e_5, e_7 \rangle$",
            L2_all,
            edges_all,
            BLUE_FILL,
            BLUE_EDGE,
            "9 collinear pairs:\n" r"$\langle L_1 \cup L_2 \rangle \cong \mathrm{PG}(3, 2)$" "\nis a singular 3-space",
        ),
        (
            axes[1],
            "(b) Unique hub on each line",
            r"$L_1 = \langle e_1, e_3 \rangle,\;\; L_2 = \langle e_5, e_4 \rangle$",
            L2_hub,
            edges_hub,
            AMBER_FILL,
            AMBER_EDGE,
            "5 collinear pairs:\n" r"hub $x_1 = e_1 \in L_1$ and" "\n" r"hub $x_2 = e_5 \in L_2$",
        ),
        (
            axes[2],
            "(c) Bijective projection",
            r"$L_1 = \langle e_1, e_3 \rangle,\;\; L_2 = \langle e_4, e_2 \rangle$",
            L2_bij,
            edges_bij,
            TEAL_FILL,
            TEAL_EDGE,
            "3 collinear pairs:\n" r"bijection $\pi_{1,2}: L_1 \to L_2$" "\n" r"$x \mapsto x^\perp \cap L_2$",
        ),
    ]

    # Stop grey L_1, L_2 bars exactly at the first and last point centers (no overhang into summary boxes)
    y_coords = [2.04, 1.26, 0.48]
    x_left, x_right = 0.88, 2.72

    for ax, title, l2_sub, l2_pts, edges, fill_c, edge_c, footer in cases:
        ax.set_xlim(0.0, 3.6)
        ax.set_ylim(-0.58, 3.15)
        ax.set_aspect("equal")
        ax.axis("off")

        card = FancyBboxPatch(
            (0.06, -0.50), 3.48, 3.55,
            boxstyle="round,pad=0.06,rounding_size=0.12",
            facecolor=PALE_BG, edgecolor=LIGHT_SLATE, linewidth=1.0, zorder=0
        )
        ax.add_patch(card)

        ax.text(
            1.80, 2.86, title,
            ha="center", va="center", fontsize=10.8, fontweight="bold", color=NAVY
        )
        ax.text(
            1.80, 2.58, l2_sub,
            ha="center", va="center", fontsize=9.0, color=SLATE
        )

        # Vertical line bars for L1 and L2 stopping at the first and last point centers
        ax.plot([x_left, x_left], [y_coords[2], y_coords[0]],
                color=NAVY, linewidth=3.2, alpha=0.25, solid_capstyle="butt", zorder=1)
        ax.plot([x_right, x_right], [y_coords[2], y_coords[0]],
                color=NAVY, linewidth=3.2, alpha=0.25, solid_capstyle="butt", zorder=1)

        ax.text(x_left, 2.24, r"$L_1$", ha="center", va="bottom",
                fontsize=10.2, fontweight="bold", color=NAVY)
        ax.text(x_right, 2.24, r"$L_2$", ha="center", va="bottom",
                fontsize=10.2, fontweight="bold", color=NAVY)

        # Collinearity edges between L1 and L2
        for i, j in edges:
            is_hub_edge = (title.startswith("(b)") and (i == 0 or j == 0))
            lw = 2.1 if not title.startswith("(a)") else 1.5
            alpha = 0.88 if not title.startswith("(a)") else 0.65
            if is_hub_edge and i == 0 and j == 0:
                lw = 2.6
            ax.plot(
                [x_left, x_right], [y_coords[i], y_coords[j]],
                color=edge_c, linewidth=lw, alpha=alpha, zorder=2
            )

        for idx, p in enumerate(L1):
            is_hub = title.startswith("(b)") and idx == 0
            node_fill = ROSE_FILL if is_hub else fill_c
            node_edge = ROSE_EDGE if is_hub else edge_c
            c = Circle((x_left, y_coords[idx]), 0.125,
                       facecolor=node_fill, edgecolor=node_edge, linewidth=1.8, zorder=4)
            ax.add_patch(c)
            lbl = f"${fmt_vec(p)}$"
            if is_hub:
                lbl = r"$x_1=" + fmt_vec(p) + "$"
            ax.text(x_left - 0.18, y_coords[idx], lbl,
                    ha="right", va="center", fontsize=9.0, color=NAVY, zorder=5)

        for idx, p in enumerate(l2_pts):
            is_hub = title.startswith("(b)") and idx == 0
            node_fill = ROSE_FILL if is_hub else fill_c
            node_edge = ROSE_EDGE if is_hub else edge_c
            c = Circle((x_right, y_coords[idx]), 0.125,
                       facecolor=node_fill, edgecolor=node_edge, linewidth=1.8, zorder=4)
            ax.add_patch(c)
            lbl = f"${fmt_vec(p)}$"
            if is_hub:
                lbl = r"$x_2=" + fmt_vec(p) + "$"
            ax.text(x_right + 0.18, y_coords[idx], lbl,
                    ha="left", va="center", fontsize=9.0, color=NAVY, zorder=5)

        foot_box = FancyBboxPatch(
            (0.24, -0.40), 3.12, 0.54,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor="white", edgecolor=edge_c, linewidth=1.0, zorder=3
        )
        ax.add_patch(foot_box)
        ax.text(
            1.80, -0.13, footer,
            ha="center", va="center", fontsize=8.7, color=NAVY, zorder=4
        )

    fig.suptitle(
        r"The three collinearity patterns between two disjoint lines $L_1, L_2$ (realized in $Q^+(7, 2)$)",
        fontsize=12, fontweight="bold", color=NAVY, y=0.98
    )
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.90, wspace=0.06)

    out_path = OUT_DIR / "maths4_polar_disjoint_lines.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return out_path


# ============================================================================
# Figure 21: Common neighbours S_{a,b} = a^perp cap b^perp in W(5, 2)
# ============================================================================
def build_figure_19() -> Path:
    """Verify S_{a,b} = a^perp cap b^perp in W(5, 2) and plot Figure 21."""
    def symp(x: tuple[int, ...], y: tuple[int, ...]) -> int:
        return (
            x[0] * y[1] + x[1] * y[0]
            + x[2] * y[3] + x[3] * y[2]
            + x[4] * y[5] + x[5] * y[4]
        ) % 2

    pts = [v for v in itertools.product((0, 1), repeat=6) if any(v)]
    assert len(pts) == 63

    a = (1, 0, 0, 0, 0, 0)  # e_1
    b = (0, 1, 0, 0, 0, 0)  # e_2
    assert symp(a, a) == 0 and symp(b, b) == 0  # a in a^perp, b in b^perp
    assert symp(a, b) == 1  # noncollinear

    a_perp = [v for v in pts if symp(a, v) == 0]
    b_perp = [v for v in pts if symp(b, v) == 0]
    s_ab = [v for v in pts if symp(a, v) == 0 and symp(b, v) == 0]
    assert a in a_perp and b in b_perp
    assert a not in b_perp and b not in a_perp
    assert len(a_perp) == 31
    assert len(b_perp) == 31
    assert len(s_ab) == 15

    s_ab_set = set(s_ab)
    ti_lines = []
    for i in range(len(s_ab)):
        for j in range(i + 1, len(s_ab)):
            u, v = s_ab[i], s_ab[j]
            if symp(u, v) == 0:
                w = tuple(x ^ y for x, y in zip(u, v))
                assert w in s_ab_set
                line = tuple(sorted([u, v, w]))
                if line not in ti_lines:
                    ti_lines.append(line)
    assert len(ti_lines) == 15

    for y in s_ab:
        third = tuple(x ^ z for x, z in zip(a, y))
        assert third in a_perp and third not in s_ab_set
        assert symp(third, b) == 1

    fig, ax = plt.subplots(figsize=(12.0, 6.2), dpi=180)
    fig.patch.set_facecolor("white")
    ax.set_xlim(-5.8, 5.8)
    ax.set_ylim(-3.26, 3.24)
    ax.set_aspect("equal")
    ax.axis("off")

    ambient = FancyBboxPatch(
        (-5.6, -3.10), 11.2, 6.18,
        boxstyle="round,pad=0.08,rounding_size=0.18",
        facecolor=PALE_BG, edgecolor=LIGHT_SLATE, linewidth=1.1, zorder=0
    )
    ax.add_patch(ambient)

    ax.text(
        0.0, 2.84,
        r"Common-neighbour subspace $S_{a,b} = a^\perp \cap b^\perp$ for noncollinear points $a, b$ (in $W(5, 2)$)",
        ha="center", va="center", fontsize=11.3, fontweight="bold", color=NAVY
    )

    # Circles for a^perp and b^perp: centers (-0.92, 0.00) and (0.92, 0.00), radius 2.26
    # Circles span y in [-2.26, 2.26], leaving clear space for top labels (y=2.48) and bottom boxes (y=-2.66)
    cx_a, cy_a, r_lobe = -0.92, 0.00, 2.26
    cx_b, cy_b = 0.92, 0.00

    lobe_a = Circle((cx_a, cy_a), r_lobe, facecolor=BLUE_FILL, edgecolor=BLUE_EDGE,
                    linewidth=1.6, alpha=0.38, zorder=1)
    lobe_b = Circle((cx_b, cy_b), r_lobe, facecolor=AMBER_FILL, edgecolor=AMBER_EDGE,
                    linewidth=1.6, alpha=0.38, zorder=1)
    ax.add_patch(lobe_a)
    ax.add_patch(lobe_b)

    # Construct exact lens polygon for S_{a,b} = a^perp cap b^perp so it never sticks out of the lens
    h_lens = np.sqrt(r_lobe**2 - cx_a**2)
    phi = np.arcsin(h_lens / r_lobe)
    t_right = np.linspace(-phi, phi, 120)
    t_left = np.linspace(np.pi - phi, np.pi + phi, 120)
    lens_x = np.concatenate([cx_a + r_lobe * np.cos(t_right), cx_b + r_lobe * np.cos(t_left)])
    lens_y = np.concatenate([cy_a + r_lobe * np.sin(t_right), cy_b + r_lobe * np.sin(t_left)])
    lens_poly = Polygon(
        np.column_stack([lens_x, lens_y]),
        closed=True, facecolor=TEAL_FILL, edgecolor=TEAL_EDGE, linewidth=2.2, alpha=0.85, zorder=2
    )
    ax.add_patch(lens_poly)

    ax.text(
        -2.65, 2.48, r"$a^\perp = \mathrm{PG}(W_a)$ (31 pts, $a \in a^\perp$)",
        ha="center", va="center", fontsize=9.4, fontweight="bold", color=BLUE_EDGE
    )
    ax.text(
        2.65, 2.48, r"$b^\perp = \mathrm{PG}(W_b)$ (31 pts, $b \in b^\perp$)",
        ha="center", va="center", fontsize=9.4, fontweight="bold", color=AMBER_EDGE
    )
    ax.text(
        0.0, 1.24, r"$S_{a,b} = a^\perp \cap b^\perp$",
        ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEAL_EDGE, zorder=4
    )
    ax.text(
        0.0, 0.94, r"$\cong W(3, 2)$ (15 pts, 15 lines)",
        ha="center", va="center", fontsize=7.6, color=NAVY, zorder=4
    )

    # Place a inside a^perp and b inside b^perp
    ax_pt, ay_pt = -2.96, -0.20
    bx_pt, by_pt = 2.96, -0.20
    assert (ax_pt - cx_a) ** 2 + (ay_pt - cy_a) ** 2 < (r_lobe - 0.20) ** 2
    assert (bx_pt - cx_b) ** 2 + (by_pt - cy_b) ** 2 < (r_lobe - 0.20) ** 2

    # 3 collinear points y_1, y_2, y_3 in S_{a,b} with generous vertical spacing
    y_coords = [(-0.22, 0.64), (-0.22, -0.20), (-0.22, -1.04)]
    y_labels = [r"$y_1 = e_3$", r"$y_2 = e_5$", r"$y_3 = e_3+e_5$"]
    third_labels = [r"$e_1+e_3$", r"$e_1+e_5$", r"$e_1+e_3+e_5$"]

    # Each 3-point line through a is a straight segment: third point is exact midpoint of a and y_i
    third_coords = [
        (0.50 * ax_pt + 0.50 * yx, 0.50 * ay_pt + 0.50 * yy)
        for (yx, yy) in y_coords
    ]

    # Draw totally isotropic line L' inside S_{a,b}
    ax.plot(
        [y_coords[0][0], y_coords[2][0]],
        [y_coords[0][1], y_coords[2][1]],
        color=TEAL_EDGE, linewidth=2.8, zorder=4
    )
    ax.text(
        0.0, -1.44, r"line $L' \subseteq S_{a,b}$",
        ha="center", va="center", fontsize=8.5, fontweight="bold", color=TEAL_EDGE, zorder=5
    )

    for idx, ((yx, yy), (tx, ty), y_lbl, t_lbl) in enumerate(
        zip(y_coords, third_coords, y_labels, third_labels)
    ):
        # Straight line from a through third_pt to y_i
        ax.plot([ax_pt, yx], [ay_pt, yy], color=BLUE_EDGE, linewidth=1.9, zorder=3)
        # Collinearity from y_i to b
        ax.plot([yx, bx_pt], [yy, by_pt],
                color=AMBER_EDGE, linewidth=1.5, linestyle="--", alpha=0.82, zorder=3)

        c_t = Circle((tx, ty), 0.095, facecolor="white", edgecolor=BLUE_EDGE, linewidth=1.5, zorder=5)
        ax.add_patch(c_t)
        if idx == 0:
            lbl_dx, lbl_dy, va_mode = -0.04, 0.14, "bottom"
        elif idx == 1:
            lbl_dx, lbl_dy, va_mode = -0.02, 0.11, "bottom"
        else:
            lbl_dx, lbl_dy, va_mode = -0.04, -0.15, "top"
        ax.text(
            tx + lbl_dx, ty + lbl_dy, t_lbl, ha="center", va=va_mode,
            fontsize=7.6, color=NAVY,
            bbox=dict(boxstyle="round,pad=0.05", facecolor="white", edgecolor="none", alpha=0.88),
            zorder=6
        )

        c_y = Circle((yx, yy), 0.11, facecolor="white", edgecolor=TEAL_EDGE, linewidth=2.0, zorder=6)
        ax.add_patch(c_y)
        ax.text(
            yx + 0.16, yy, y_lbl, ha="left", va="center",
            fontsize=8.2, fontweight="bold", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.09", facecolor=TEAL_FILL, edgecolor="none", alpha=0.92),
            zorder=7
        )

    ax.text(
        -2.75, -2.66,
        r"Each line $L$ through $a$ meets $S_{a,b}$ in a unique point $y = L \cap b^\perp$;" "\n"
        r"the third point $a + y$ on $L$ lies in $a^\perp \backslash S_{a,b}$",
        ha="center", va="center", fontsize=8.5, color=NAVY,
        bbox=dict(boxstyle="round,pad=0.26", facecolor="white", edgecolor=BLUE_EDGE, linewidth=0.9),
        zorder=6
    )

    ax.text(
        2.78, -2.66,
        r"$a = e_1 \in a^\perp$ and $b = e_2 \in b^\perp$ are noncollinear ($d(a,b)=2$):" "\n"
        r"$\widetilde{S_{a,b}}$ is a polar space of rank $n - 1 = 2$",
        ha="center", va="center", fontsize=8.5, color=NAVY,
        bbox=dict(boxstyle="round,pad=0.26", facecolor="white", edgecolor=AMBER_EDGE, linewidth=0.9),
        zorder=6
    )

    ca = Circle((ax_pt, ay_pt), 0.16, facecolor=ROSE_FILL, edgecolor=ROSE_EDGE, linewidth=2.2, zorder=7)
    cb = Circle((bx_pt, by_pt), 0.16, facecolor=ROSE_FILL, edgecolor=ROSE_EDGE, linewidth=2.2, zorder=7)
    ax.add_patch(ca)
    ax.add_patch(cb)
    ax.text(ax_pt, ay_pt + 0.28, r"$a = e_1$", ha="center", va="bottom",
            fontsize=9.8, fontweight="bold", color=ROSE_EDGE,
            bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor="none", alpha=0.85),
            zorder=8)
    ax.text(bx_pt, by_pt + 0.28, r"$b = e_2$", ha="center", va="bottom",
            fontsize=9.8, fontweight="bold", color=ROSE_EDGE,
            bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor="none", alpha=0.85),
            zorder=8)

    out_path = OUT_DIR / "maths4_polar_common_neighbours.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return out_path


# ============================================================================
# Figure 22: Four line classes L_1, L_2, L_3, L_4 and trace equation
# ============================================================================
def build_figure_20() -> Path:
    """Verify line-class partition in PG(3,3) for Q+(3,3) and W(3,3) and plot Figure 22."""
    pts_pg33 = []
    for v in itertools.product((0, 1, 2), repeat=4):
        if any(v):
            first_nz = next(x for x in v if x != 0)
            if first_nz == 1:
                pts_pg33.append(v)
    assert len(pts_pg33) == 40

    def norm_pg3(v: tuple[int, ...]) -> tuple[int, ...]:
        first_nz = next(x for x in v if x != 0)
        inv = 1 if first_nz == 1 else 2
        return tuple((x * inv) % 3 for x in v)

    lines_pg33 = set()
    for i in range(len(pts_pg33)):
        for j in range(i + 1, len(pts_pg33)):
            u, v = pts_pg33[i], pts_pg33[j]
            line_pts = {u, v}
            for c1 in (1, 2):
                for c2 in (1, 2):
                    w = norm_pg3(tuple((c1 * a + c2 * b) % 3 for a, b in zip(u, v)))
                    line_pts.add(w)
            assert len(line_pts) == 4
            lines_pg33.add(tuple(sorted(line_pts)))
    assert len(lines_pg33) == 130

    def f_orth(x: tuple[int, ...], y: tuple[int, ...]) -> int:
        return (x[0] * y[1] + x[1] * y[0] + x[2] * y[3] + x[3] * y[2]) % 3

    iso_orth = {p for p in pts_pg33 if f_orth(p, p) == 0}
    assert len(iso_orth) == 16

    l1_o = l2_o = l3_o = l4_o = 0
    for line in lines_pg33:
        hits = [p for p in line if p in iso_orth]
        if len(hits) == 4 and all(f_orth(p, q) == 0 for p in line for q in line):
            l1_o += 1
        elif len(hits) == 1:
            l2_o += 1
        elif len(hits) == 0:
            l3_o += 1
        elif len(hits) == 2:
            l4_o += 1
        else:
            raise AssertionError(f"Unexpected intersection size {len(hits)}")
    assert (l1_o, l2_o, l3_o, l4_o) == (8, 32, 18, 72)

    def f_symp(x: tuple[int, ...], y: tuple[int, ...]) -> int:
        return (x[0] * y[1] - x[1] * y[0] + x[2] * y[3] - x[3] * y[2]) % 3

    iso_symp = {p for p in pts_pg33 if f_symp(p, p) == 0}
    assert len(iso_symp) == 40

    l1_s = l4_s = 0
    for line in lines_pg33:
        if all(f_symp(p, q) == 0 for p in line for q in line):
            l1_s += 1
        else:
            l4_s += 1
    assert (l1_s, l4_s) == (40, 90)

    fig, (ax_left, ax_right) = plt.subplots(
        1, 2, figsize=(13.6, 5.2), dpi=180, gridspec_kw={"width_ratios": [1.10, 1.15]}
    )
    fig.patch.set_facecolor("white")

    # ---------------- Left panel: Geometric partition L_1, L_2, L_3, L_4 ----------------
    # Fix 38:
    # - L_1 (totally isotropic) and L_2 (tangent) through x lie ENTIRELY inside the T_x box.
    # - L_4 (hyperbolic) meets T_x ONLY at x (which sits on the bottom boundary of T_x) and
    #   runs downward into the rest of P without entering the interior of the T_x box.
    ax_left.set_xlim(-3.25, 3.25)
    ax_left.set_ylim(-2.6, 2.75)
    ax_left.set_aspect("equal")
    ax_left.axis("off")

    card_l = FancyBboxPatch(
        (-3.12, -2.48), 6.24, 5.05,
        boxstyle="round,pad=0.06,rounding_size=0.14",
        facecolor=PALE_BG, edgecolor=LIGHT_SLATE, linewidth=1.0, zorder=0
    )
    ax_left.add_patch(card_l)
    ax_left.text(
        0.0, 2.32,
        r"(a) Partition of ambient lines into $\mathcal{L}_1, \mathcal{L}_2, \mathcal{L}_3, \mathcal{L}_4$",
        ha="center", va="center", fontsize=10.8, fontweight="bold", color=NAVY
    )

    # Polar space P: an ellipse centered at (-0.95, 0.05) with ry = 1.55 and rx chosen so that
    # x = (0.05, 0.45) lies EXACTLY on its right boundary!
    theta = np.linspace(0, 2 * np.pi, 240)
    cx_oval, cy_oval = -0.95, 0.05
    ry_oval = 1.55
    x_pt = (0.05, 0.45)
    rx_oval = (x_pt[0] - cx_oval) / np.sqrt(1.0 - ((x_pt[1] - cy_oval) / ry_oval) ** 2)
    px = cx_oval + rx_oval * np.cos(theta)
    py = cy_oval + ry_oval * np.sin(theta)
    ax_left.fill(px, py, color=BLUE_FILL, alpha=0.45, zorder=1)
    ax_left.plot(px, py, color=BLUE_EDGE, linewidth=1.8, zorder=2)
    ax_left.text(-1.72, -0.35, r"isotropic set" "\n" r"$\mathcal{P}$",
                 ha="center", va="center", fontsize=9.1, fontweight="bold", color=BLUE_EDGE, zorder=4)

    # Tangent hyperplane T_x = PG(W_{v_1}): box from y = 0.45 to y = 1.92
    # Place x = <v_1> = (0.05, 0.45) on the bottom edge y = 0.45 of T_x AND on the right boundary of P:
    # 1. L_1 (up-left into P) lies 100% inside P AND 100% inside T_x.
    # 2. L_2 (up-right inside T_x) touches P ONLY at x = (0.05, 0.45) and stays outside P everywhere else.
    # 3. L_4 (down-left through P) meets T_x ONLY at x = (0.05, 0.45) and cuts P at a second point <v_2>.
    tx_ymin, tx_ymax = 0.45, 1.92
    tx_box = FancyBboxPatch(
        (-2.85, tx_ymin), 5.62, tx_ymax - tx_ymin,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor=AMBER_FILL, edgecolor=AMBER_EDGE, linewidth=1.3, linestyle="--", alpha=0.46, zorder=2
    )
    ax_left.add_patch(tx_box)
    ax_left.text(
        -2.72, 1.68, r"tangent hyperplane $T_x = \mathrm{PG}(W_{v_1})$",
        ha="left", va="center", fontsize=8.6, fontweight="bold", color=AMBER_EDGE, zorder=4
    )

    # Line in L_2 (tangent line inside T_x through x, touching P ONLY at x)
    ax_left.plot([x_pt[0], 2.48], [x_pt[1], 1.28], color=AMBER_EDGE, linewidth=2.3, zorder=4)
    ax_left.text(
        2.62, 1.36, r"$\mathcal{L}_2$: tangent ($|L \cap \mathcal{P}| = 1$, $L \subseteq T_x$)",
        ha="right", va="bottom", fontsize=8.3, fontweight="bold", color=AMBER_EDGE,
        bbox=dict(boxstyle="round,pad=0.11", facecolor="white", edgecolor="none", alpha=0.88),
        zorder=5
    )

    # Line in L_1 (totally isotropic line through x, wholly inside BOTH P and T_x!)
    l1_end = (-1.12, 1.24)
    assert ((l1_end[0] - cx_oval) / rx_oval) ** 2 + ((l1_end[1] - cy_oval) / ry_oval) ** 2 <= 1.0
    assert tx_ymin <= l1_end[1] <= tx_ymax
    ax_left.plot([l1_end[0], x_pt[0]], [l1_end[1], x_pt[1]], color=TEAL_EDGE, linewidth=3.0, zorder=4)
    ax_left.text(
        -1.92, 0.96, r"$\mathcal{L}_1$: totally isotropic" "\n" r"($L \subseteq \mathcal{P} \cap T_x$)",
        ha="center", va="center", fontsize=8.2, fontweight="bold", color=TEAL_EDGE,
        bbox=dict(boxstyle="round,pad=0.13", facecolor="white", edgecolor=TEAL_EDGE, linewidth=0.7, alpha=0.92),
        zorder=5
    )

    # Line in L_4 (hyperbolic line meeting T_x ONLY at x = (0.05, 0.45) and cutting P at <v_2> on lower boundary)
    y2_val = -1.32
    x2_val = cx_oval + rx_oval * np.sqrt(1.0 - ((y2_val - cy_oval) / ry_oval) ** 2)
    x2_pt = (float(x2_val), y2_val)
    # Extend slightly below x2_pt along the same straight line
    l4_end = (x_pt[0] + 1.22 * (x2_pt[0] - x_pt[0]), x_pt[1] + 1.22 * (x2_pt[1] - x_pt[1]))
    ax_left.plot([x_pt[0], l4_end[0]], [x_pt[1], l4_end[1]], color=PURPLE_EDGE, linewidth=2.3, zorder=4)
    ax_left.text(
        1.55, -1.25,
        r"$\mathcal{L}_4$: hyperbolic ($|L \cap \mathcal{P}| \geq 2$," "\n" r"$L \cap T_x = \{x\}$)",
        ha="center", va="center", fontsize=8.3, fontweight="bold", color=PURPLE_EDGE,
        bbox=dict(boxstyle="round,pad=0.16", facecolor="white", edgecolor=PURPLE_EDGE, linewidth=0.8, alpha=0.92),
        zorder=5
    )

    # Line in L_3 (exterior / passant line missing P)
    ax_left.plot([-2.78, 0.85], [-2.02, -2.02], color=GRAY_EDGE, linewidth=2.0, linestyle=":", zorder=3)
    ax_left.text(
        -0.95, -2.18, r"$\mathcal{L}_3$: exterior / passant ($L \cap \mathcal{P} = \emptyset$)",
        ha="center", va="top", fontsize=8.5, fontweight="bold", color=GRAY_EDGE, zorder=5
    )

    # Draw points x = <v_1> and <v_2>
    cx1 = Circle(x_pt, 0.12, facecolor=ROSE_FILL, edgecolor=ROSE_EDGE, linewidth=2.0, zorder=6)
    cx2 = Circle(x2_pt, 0.12, facecolor=PURPLE_FILL, edgecolor=PURPLE_EDGE, linewidth=2.0, zorder=6)
    ax_left.add_patch(cx1)
    ax_left.add_patch(cx2)
    ax_left.text(
        x_pt[0] + 0.18, x_pt[1] - 0.12, r"$x = \langle v_1 \rangle$",
        ha="left", va="top", fontsize=8.9, fontweight="bold", color=ROSE_EDGE,
        bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor="none", alpha=0.88),
        zorder=7
    )
    ax_left.text(
        x2_pt[0] + 0.18, x2_pt[1] - 0.04, r"$\langle v_2 \rangle$",
        ha="left", va="center", fontsize=8.9, fontweight="bold", color=PURPLE_EDGE,
        bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor="none", alpha=0.88),
        zorder=7
    )

    # ---------------- Right panel: Trace equation on a hyperbolic line L in L_4 ----------------
    ax_right.set_xlim(0.0, 6.4)
    ax_right.set_ylim(-0.2, 5.2)
    ax_right.axis("off")

    card_r = FancyBboxPatch(
        (0.08, -0.08), 6.24, 5.12,
        boxstyle="round,pad=0.06,rounding_size=0.14",
        facecolor=PALE_BG, edgecolor=LIGHT_SLATE, linewidth=1.0, zorder=0
    )
    ax_right.add_patch(card_r)

    ax_right.text(
        3.20, 4.74,
        r"(b) Points of $\mathcal{P}$ on a hyperbolic line $L = \langle v_1, v_2 \rangle \in \mathcal{L}_4$",
        ha="center", va="center", fontsize=10.8, fontweight="bold", color=NAVY
    )
    ax_right.text(
        3.20, 4.38,
        r"Normalized with $f(v_1, v_2) = 1$:  $\langle v_1 + v_2\eta \rangle \in \mathcal{P} \Longleftrightarrow \eta + \eta^\sigma\epsilon = 0$",
        ha="center", va="center", fontsize=9.1, color=SLATE
    )

    rows = [
        (
            3.25,
            r"Orthogonal $Q^+(3, 3)$  ($\sigma = 1, \epsilon = 1$ over $\mathbb{F}_3$)",
            r"$2\eta = 0 \Rightarrow \eta = 0$ only:  2 of 4 points on $L$ lie in $\mathcal{P}$",
            [r"$\langle v_2 \rangle$", r"$\langle v_1 \rangle$", r"$\langle v_1+v_2 \rangle$", r"$\langle v_1+2v_2 \rangle$"],
            [True, True, False, False],
            BLUE_FILL,
            BLUE_EDGE,
        ),
        (
            1.80,
            r"Hermitian $H(3, 4)$  ($\sigma(\eta)=\eta^2, \epsilon = 1$ over $\mathbb{F}_4$)",
            r"$\eta + \eta^2 = 0 \Rightarrow \eta \in \mathbb{F}_2$:  3 of 5 points form a Baer subline",
            [r"$\langle v_2 \rangle$", r"$\langle v_1 \rangle$", r"$\langle v_1+v_2 \rangle$", r"$\langle v_1+\omega v_2 \rangle$", r"$\langle v_1+\omega^2 v_2 \rangle$"],
            [True, True, True, False, False],
            TEAL_FILL,
            TEAL_EDGE,
        ),
        (
            0.35,
            r"Symplectic $W(3, 3)$  ($\sigma = 1, \epsilon = -1$ over $\mathbb{F}_3$)",
            r"$\eta - \eta = 0$ for all $\eta \in \mathbb{F}_3$:  all 4 points on $L$ lie in $\mathcal{P}$ ($L \notin \mathcal{L}_1$)",
            [r"$\langle v_2 \rangle$", r"$\langle v_1 \rangle$", r"$\langle v_1+v_2 \rangle$", r"$\langle v_1+2v_2 \rangle$"],
            [True, True, True, True],
            PURPLE_FILL,
            PURPLE_EDGE,
        ),
    ]

    for y_base, title_r, sub_r, pt_labels, is_iso, f_col, e_col in rows:
        row_box = FancyBboxPatch(
            (0.26, y_base - 0.25), 5.88, 1.22,
            boxstyle="round,pad=0.04,rounding_size=0.10",
            facecolor="white", edgecolor=LIGHT_SLATE, linewidth=0.9, zorder=1
        )
        ax_right.add_patch(row_box)

        ax_right.text(0.42, y_base + 0.74, title_r, ha="left", va="center",
                      fontsize=9.3, fontweight="bold", color=NAVY, zorder=3)
        ax_right.text(0.42, y_base + 0.48, sub_r, ha="left", va="center",
                      fontsize=8.4, color=SLATE, zorder=3)

        xs = np.linspace(0.85, 5.55, len(pt_labels))
        ax_right.plot([xs[0], xs[-1]], [y_base + 0.08, y_base + 0.08],
                      color=SLATE, linewidth=1.8, zorder=2)

        for x_pos, lbl, flag in zip(xs, pt_labels, is_iso):
            c = Circle(
                (x_pos, y_base + 0.08), 0.11,
                facecolor=f_col if flag else "white",
                edgecolor=e_col if flag else MUTED,
                linewidth=1.8 if flag else 1.2,
                zorder=4
            )
            ax_right.add_patch(c)
            ax_right.text(
                x_pos, y_base - 0.12, lbl,
                ha="center", va="center", fontsize=8.0,
                color=NAVY if flag else MUTED, zorder=5
            )

    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.96, wspace=0.05)
    out_path = OUT_DIR / "maths4_polar_line_classes.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return out_path


# ============================================================================
# Figure 23: Nucleus projection Q(4, 2) -> W(3, 2) in characteristic 2
# ============================================================================
def build_figure_21() -> Path:
    """Verify the nucleus projection Q(4, 2) -> W(3, 2) and plot Figure 23."""
    def q_para(x: tuple[int, ...]) -> int:
        return (x[0] + x[1] * x[2] + x[3] * x[4]) % 2

    def f_alt4(u: tuple[int, ...], v: tuple[int, ...]) -> int:
        return (u[0] * v[1] + u[1] * v[0] + u[2] * v[3] + u[3] * v[2]) % 2

    p_nuc = (1, 0, 0, 0, 0)
    pg3_pts = [w for w in itertools.product((0, 1), repeat=4) if any(w)]
    assert len(pg3_pts) == 15

    q42_pts = []
    x0_zero_count = 0
    x0_one_count = 0
    for w in pg3_pts:
        cand0 = (0,) + w
        cand1 = (1,) + w
        in0 = (q_para(cand0) == 0)
        in1 = (q_para(cand1) == 0)
        assert in0 != in1
        if in0:
            q42_pts.append(cand0)
            x0_zero_count += 1
        else:
            q42_pts.append(cand1)
            x0_one_count += 1

    assert len(q42_pts) == 15
    assert (x0_zero_count, x0_one_count) == (9, 6)

    q42_set = set(q42_pts)
    q42_lines = set()
    w32_lines = set()
    for i in range(15):
        for j in range(i + 1, 15):
            u, v = q42_pts[i], q42_pts[j]
            uv = tuple(a ^ b for a, b in zip(u, v))
            if uv in q42_set:
                q42_lines.add(tuple(sorted([u, v, uv])))
                wu, wv, wuv = u[1:], v[1:], uv[1:]
                assert f_alt4(wu, wv) == 0
                w32_lines.add(tuple(sorted([wu, wv, wuv])))
    assert len(q42_lines) == 15 and len(w32_lines) == 15
    assert p_nuc not in q42_set

    # Verify the specific line L = {u, v, u+v}:
    # u = (0, 1, 0, 0, 0) lies in Q(4, 2) cap H (X_0 = 0, fixed by projection)
    # v = (1, 0, 0, 1, 1) and u+v = (1, 1, 0, 1, 1) have X_0 = 1 and project to H
    u_pt = (0, 1, 0, 0, 0)
    v_pt = (1, 0, 0, 1, 1)
    uv_pt = (1, 1, 0, 1, 1)
    assert u_pt in q42_set and v_pt in q42_set and uv_pt in q42_set
    assert u_pt[0] == 0 and v_pt[0] == 1 and uv_pt[0] == 1

    fig, ax = plt.subplots(figsize=(13.2, 5.7), dpi=180)
    fig.patch.set_facecolor("white")
    ax.set_xlim(-6.2, 6.4)
    ax.set_ylim(-2.65, 3.05)
    ax.set_aspect("equal")
    ax.axis("off")

    ambient = FancyBboxPatch(
        (-6.0, -2.50), 12.2, 5.30,
        boxstyle="round,pad=0.08,rounding_size=0.18",
        facecolor=PALE_BG, edgecolor=LIGHT_SLATE, linewidth=1.1, zorder=0
    )
    ax.add_patch(ambient)

    ax.text(
        0.1, 2.52,
        r"Nucleus projection $\theta: Q(4, 2) \to W(3, 2)$ along lines through $p = (1:0:0:0:0)$ in $\mathrm{PG}(4, 2)$",
        ha="center", va="center", fontsize=11.3, fontweight="bold", color=NAVY
    )

    # Nucleus p at top-left
    px, py = -2.55, 1.88

    # Upper layer: the 6 lifted points of Q(4, 2) with X_0 = 1 (outside H)
    q_box = FancyBboxPatch(
        (-5.75, -0.34), 6.55, 1.44,
        boxstyle="round,pad=0.05,rounding_size=0.14",
        facecolor=BLUE_FILL, edgecolor=BLUE_EDGE, linewidth=1.5, alpha=0.50, zorder=1
    )
    ax.add_patch(q_box)
    ax.text(
        -5.55, 0.88,
        r"Lifted layer $X_0 = 1$ of $Q(4, 2)$ (6 pts outside $H$)",
        ha="left", va="center", fontsize=8.6, fontweight="bold", color=BLUE_EDGE,
        bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor="none", alpha=0.88),
        zorder=5
    )

    # Bottom layer: Hyperplane H = {X_0 = 0} carrying W(3, 2) AND already containing the 9 points of Q(4, 2) cap H
    h_box = FancyBboxPatch(
        (-5.75, -2.28), 6.55, 1.48,
        boxstyle="round,pad=0.05,rounding_size=0.14",
        facecolor=TEAL_FILL, edgecolor=TEAL_EDGE, linewidth=1.6, alpha=0.55, zorder=1
    )
    ax.add_patch(h_box)
    ax.text(
        -5.58, -2.06,
        r"Hyperplane $H = \{X_0 = 0\} \cong \mathrm{PG}(3, 2)$ carrying $W(3, 2)$ (9 pts with $X_0 = 0$ stay fixed)",
        ha="left", va="center", fontsize=7.8, fontweight="bold", color=TEAL_EDGE, zorder=3
    )

    # The 3 points in H = {X_0 = 0}:
    # u = (0:1:0:0:0) is ALREADY in H (at y = y_h), so u = theta(u) is a single shared hinge point!
    # v and u+v have X_0 = 1, so they lie on the tilted line L through u inside the lifted layer X_0 = 1!
    rep_x_h = [-4.75, -2.75, -0.75]
    y_h = -1.25

    # Straight line L passes through u = (rep_x_h[0], y_h) with positive slope m_line
    # So at xh_0 = -4.75, y_q[0] = y_h (t = 1.0: u stays put in H!)
    m_line = 0.52
    c_line = y_h - m_line * rep_x_h[0]
    t_vals = [
        (c_line + m_line * px - py) / (y_h - py - m_line * (xh - px))
        for xh in rep_x_h
    ]
    assert abs(t_vals[0] - 1.0) < 1e-9  # u is on H (t = 1)
    rep_x_q = [px + t * (xh - px) for t, xh in zip(t_vals, rep_x_h)]
    y_q = [py + t * (y_h - py) for t in t_vals]

    # Projection rays from p through the 3 points of L to H
    for xh in rep_x_h:
        ax.plot([px, xh], [py, y_h], color=SLATE, linewidth=1.4, linestyle="--", zorder=2)

    # Projected line theta(L) in W(3, 2) (horizontal in H)
    ax.plot([rep_x_h[0], rep_x_h[-1]], [y_h, y_h], color=TEAL_EDGE, linewidth=2.6, zorder=4)
    ax.text(
        rep_x_h[-1] + 0.18, y_h, r"line $\theta(L) \subseteq W(3, 2)$",
        ha="left", va="center", fontsize=8.4, fontweight="bold", color=TEAL_EDGE, zorder=5
    )

    # Tilted line L in Q(4, 2), meeting theta(L) at the shared point u in Q(4, 2) cap H!
    ax.plot(rep_x_q, y_q, color=BLUE_EDGE, linewidth=2.6, zorder=4)
    ax.text(
        rep_x_q[-1] + 0.18, y_q[-1] + 0.24, r"line $L \subseteq Q(4, 2)$",
        ha="left", va="center", fontsize=8.4, fontweight="bold", color=BLUE_EDGE, zorder=5
    )

    # Shared hinge point u = theta(u) in Q(4, 2) cap H (X_0 = 0, stays put)
    cu = Circle((rep_x_h[0], y_h), 0.135, facecolor=GREEN_FILL, edgecolor=GREEN_EDGE, linewidth=2.2, zorder=6)
    ax.add_patch(cu)
    ax.text(
        rep_x_h[0], y_h - 0.24,
        r"$u = (0:1:0:0:0) \in Q(4, 2) \cap H$" "\n" r"($X_0 = 0$: stays put as $(1:0:0:0)$)",
        ha="center", va="top", fontsize=7.9, fontweight="bold", color=GREEN_EDGE,
        bbox=dict(boxstyle="round,pad=0.12", facecolor="white", edgecolor=GREEN_EDGE, linewidth=0.8, alpha=0.94),
        zorder=7
    )

    # The 2 lifted points v and u+v (with X_0 = 1) and their projections theta(v), theta(u+v) in H
    lifted_q_labels = [
        r"$v = (1:0:0:1:1)$" "\n" r"$X_0 = 1$",
        r"$u+v = (1:1:0:1:1)$" "\n" r"$X_0 = 1$",
    ]
    proj_h_labels = [
        r"$\theta(v) = (0:0:1:1)$",
        r"$\theta(u+v) = (1:0:1:1)$",
    ]
    lifted_offsets = [(-0.18, 0.36), (0.98, -0.16)]

    for idx in (1, 2):
        xq, yq = rep_x_q[idx], y_q[idx]
        xh = rep_x_h[idx]
        qlbl = lifted_q_labels[idx - 1]
        hlbl = proj_h_labels[idx - 1]
        dx, dy = lifted_offsets[idx - 1]

        cq = Circle((xq, yq), 0.12, facecolor=AMBER_FILL, edgecolor=AMBER_EDGE, linewidth=1.8, zorder=5)
        ch = Circle((xh, y_h), 0.12, facecolor="white", edgecolor=TEAL_EDGE, linewidth=1.8, zorder=5)
        ax.add_patch(cq)
        ax.add_patch(ch)
        ax.text(
            xq + dx, yq + dy, qlbl,
            ha="center", va="center", fontsize=7.8, color=NAVY,
            bbox=dict(boxstyle="round,pad=0.11", facecolor="white", edgecolor=AMBER_EDGE, linewidth=0.7, alpha=0.92),
            zorder=6
        )
        ax.text(
            xh, y_h - 0.22, hlbl,
            ha="center", va="top", fontsize=8.1, fontweight="bold", color=NAVY, zorder=6
        )

    cp = Circle((px, py), 0.16, facecolor=ROSE_FILL, edgecolor=ROSE_EDGE, linewidth=2.2, zorder=6)
    ax.add_patch(cp)
    ax.text(
        px - 0.24, py,
        r"nucleus $p = \langle e_0 \rangle = (1:0:0:0:0)$" "\n" r"($p = \langle \mathrm{rad}\, f \rangle \notin Q(4, 2)$)",
        ha="right", va="center", fontsize=8.8, fontweight="bold", color=ROSE_EDGE,
        bbox=dict(boxstyle="round,pad=0.18", facecolor="white", edgecolor=ROSE_EDGE, linewidth=0.8),
        zorder=7
    )

    # Right explanatory panel
    info_box = FancyBboxPatch(
        (1.08, -2.28), 4.92, 4.35,
        boxstyle="round,pad=0.06,rounding_size=0.14",
        facecolor="white", edgecolor=SLATE, linewidth=1.1, zorder=2
    )
    ax.add_patch(info_box)

    ax.text(
        3.54, 1.72,
        r"Why $\mathrm{char}(\mathbb{F}) = 2$ and perfectness both matter",
        ha="center", va="center", fontsize=9.6, fontweight="bold", color=NAVY, zorder=4
    )

    steps = [
        (
            1.02,
            ROSE_FILL,
            ROSE_EDGE,
            r"1. $\mathrm{char}(\mathbb{F}) = 2$ creates the nucleus $p$:",
            r"Polar form $f(X,Y) = X_1Y_2 + X_2Y_1 + X_3Y_4 + X_4Y_3$" "\n"
            r"kills $e_0$, so $p = \langle \mathrm{rad}\, f \rangle \in \mathrm{PG}(4, \mathbb{F}) \backslash Q(4, \mathbb{F})$.",
        ),
        (
            -0.25,
            AMBER_FILL,
            AMBER_EDGE,
            r"2. Perfectness puts 1 point on each ray:",
            r"On the line through $p$ and $(0:X_1:X_2:X_3:X_4)$," "\n"
            r"$X_0^2 = X_1X_2 + X_3X_4$ has a solution $X_0 \in \mathbb{F}$ for" "\n"
            r"every $(X_1:\dots:X_4)$ iff every element of $\mathbb{F}$ is a square.",
        ),
        (
            -1.58,
            TEAL_FILL,
            TEAL_EDGE,
            r"3. Split of the 15 points of $Q(4, 2)$ over $\mathbb{F}_2$:",
            r"9 points have $X_1X_2+X_3X_4 = 0 \Rightarrow X_0 = 0$ (stay in $H$);" "\n"
            r"6 points have $X_1X_2+X_3X_4 = 1 \Rightarrow X_0 = 1$ (project to $H$).",
        ),
    ]

    for y_s, fc, ec, head_s, body_s in steps:
        sbox = FancyBboxPatch(
            (1.26, y_s - 0.52), 4.56, 1.04,
            boxstyle="round,pad=0.04,rounding_size=0.09",
            facecolor=fc, edgecolor=ec, linewidth=1.0, alpha=0.65, zorder=3
        )
        ax.add_patch(sbox)
        ax.text(1.40, y_s + 0.30, head_s, ha="left", va="center",
                fontsize=8.6, fontweight="bold", color=NAVY, zorder=4)
        ax.text(1.40, y_s - 0.14, body_s, ha="left", va="center",
                fontsize=8.0, color=NAVY, zorder=4)

    out_path = OUT_DIR / "maths4_polar_nucleus_isomorphism.png"
    fig.savefig(out_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return out_path


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    paths = [
        build_figure_18(),
        build_figure_19(),
        build_figure_20(),
        build_figure_21(),
    ]
    for p in paths:
        print(f"Generated {p}")


if __name__ == "__main__":
    main()
