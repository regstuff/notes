#!/usr/bin/env python3
"""Figures 13 to 16 (v3) for the chapter "Hyperplanes and Projective Embeddings of Point-Line Geometries" (Maths 4).

Usage:
    python3 make_embeddings_figures.py [OUTPUT_DIR]

Writes four PNGs into OUTPUT_DIR (default: docs/maths/figures in this repository):
  maths4_embeddings_quotient_book.png    (Figure 13) Secant avoidance and the pages-of-a-book quotient Sigma_alpha
  maths4_embeddings_fan_hyperplanes.png  (Figure 14) All 15 hyperplanes of the 3-vane fan: 7 surviving vs 8 killed
  maths4_embeddings_quotient.png         (Figure 15) Why proper quotients strictly lose hyperplanes & 3-vane fan quotient
  maths4_embeddings_ag23_parity.png      (Figure 16) Why AG(2,3) has zero hyperplanes: odd vs even pencil partition

Every point, line, secant, and hyperplane is computed from coordinates and asserted before plotting.
"""

from pathlib import Path
import itertools as it
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, Polygon, Circle
import numpy as np

DEFAULT_OUT_DIR = Path(__file__).resolve().parents[2] / "docs" / "maths" / "figures"

BLUE = "#1f3b73"
TEAL = "#0f766e"
ORANGE = "#d9730d"
GREEN = "#2e7d32"
PURPLE = "#6a3d9a"
RED = "#c62828"
MAGENTA = "#be185d"
INDIGO = "#3730a3"
GREY = "#94a3b8"
DARK = "#1e293b"


def build_fan3_pg32():
    """Construct the 3-vane fan in PG(3,2), verify all 15 hyperplanes, secants, and quotient by alpha=(1,1,1,0)."""
    F2 = (0, 1)
    pts = {
        "p0": (0, 0, 0, 1),
        "p1": (1, 0, 0, 0),
        "p2": (1, 0, 0, 1),
        "p3": (0, 1, 0, 0),
        "p4": (0, 1, 0, 1),
        "p5": (0, 0, 1, 0),
        "p6": (0, 0, 1, 1),
    }
    lines = [
        ("L1", ("p0", "p1", "p2")),
        ("L2", ("p0", "p3", "p4")),
        ("L3", ("p0", "p5", "p6")),
    ]
    for _, (a, b, c) in lines:
        va, vb, vc = pts[a], pts[b], pts[c]
        assert tuple((va[i] + vb[i] + vc[i]) % 2 for i in range(4)) == (0, 0, 0, 0)

    line_sets = [frozenset(L) for _, L in lines]
    abs_hyps = set()
    for r in range(1, 7):
        for sub in it.combinations(pts.keys(), r):
            H = frozenset(sub)
            if all(len(H & L) in (1, 3) for L in line_sets):
                abs_hyps.add(H)
    assert len(abs_hyps) == 15

    all_vecs = [v for v in it.product(F2, repeat=4) if any(v)]
    assert len(all_vecs) == 15
    planes = {}
    for a in all_vecs:
        H = frozenset(name for name, v in pts.items() if sum(ai * vi for ai, vi in zip(a, v)) % 2 == 0)
        planes[a] = H
    assert set(planes.values()) == abs_hyps

    emb_vecs = set(pts.values())
    sec_vecs = {
        tuple((u[i] + v[i]) % 2 for i in range(4))
        for u, v in it.combinations(pts.values(), 2)
    }
    valid_centers = [v for v in all_vecs if v not in emb_vecs and v not in sec_vecs]
    assert len(emb_vecs | sec_vecs) == 13
    assert valid_centers == [(1, 1, 1, 0), (1, 1, 1, 1)]

    beta = (1, 1, 0, 0)
    assert beta not in emb_vecs and beta in sec_vecs
    assert beta == tuple((pts["p1"][i] + pts["p3"][i]) % 2 for i in range(4))

    alpha = (1, 1, 1, 0)
    assert alpha == tuple((pts["p1"][i] + pts["p3"][i] + pts["p5"][i]) % 2 for i in range(4))

    surviving = {a: H for a, H in planes.items() if sum(ai * vi for ai, vi in zip(a, alpha)) % 2 == 0}
    killed = {a: H for a, H in planes.items() if sum(ai * vi for ai, vi in zip(a, alpha)) % 2 == 1}
    assert len(surviving) == 7 and len(killed) == 8

    return pts, lines, planes, surviving, killed, alpha, beta


def make_figure_22_quotient_book(out_dir: Path) -> Path:
    """Figure 13: (a) Secant avoidance in PG(3,2); (b) Projecting PG(3,F) from a 1D hinge line ('book of pages')."""
    pts, lines, _, _, _, alpha, beta = build_fan3_pg32()

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["mathtext.fontset"] = "cm"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.8, 6.3), dpi=220)
    fig.patch.set_facecolor("white")

    # -------------------------------------------------------------------------
    # Panel (a): Secant avoidance when projecting from a point
    # -------------------------------------------------------------------------
    ax1.set_xlim(-0.4, 10.4)
    ax1.set_ylim(-0.3, 8.6)
    ax1.axis("off")
    ax1.set_title(
        "(a) Secant Avoidance: Valid Centre $\\alpha$ vs. Secant Point $\\beta$",
        fontsize=12.0,
        fontweight="bold",
        color=DARK,
        pad=10,
    )

    bg1 = FancyBboxPatch(
        (0.0, 0.0), 10.0, 8.1,
        boxstyle="round,pad=0.15",
        facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.5, zorder=0
    )
    ax1.add_patch(bg1)

    alpha_xy = np.array([3.65, 7.35])
    p0_xy = np.array([3.50, 5.35])
    p1_xy = np.array([1.85, 3.05])
    p2_xy = 0.50 * p0_xy + 0.50 * p1_xy
    p3_xy = np.array([5.25, 3.05])
    p4_xy = 0.50 * p0_xy + 0.50 * p3_xy

    # Draw the two vanes L1 and L2 ending exactly at the endpoints (no stubs)
    for end_xy, lbl, lpos in [
        (p1_xy, "$\\epsilon(L_1)$", (0.85, 3.85)),
        (p3_xy, "$\\epsilon(L_2)$", (5.38, 3.85)),
    ]:
        ax1.plot(
            [p0_xy[0], end_xy[0]],
            [p0_xy[1], end_xy[1]],
            color=TEAL, lw=2.8, zorder=3
        )
        ax1.text(lpos[0], lpos[1], lbl, fontsize=10.2, fontweight="bold", color=TEAL)

    # Secant line through p1 and p3 containing forbidden point beta = (1,1,0,0)
    beta_xy = np.array([7.65, 3.05])
    ax1.plot([0.55, 9.55], [3.05, 3.05], color=RED, lw=2.1, ls="--", zorder=2)
    ax1.text(
        3.55, 2.58,
        "Secant line $\\langle \\epsilon(p_1), \\epsilon(p_3) \\rangle_\\Sigma$",
        fontsize=9.3, fontweight="bold", color=RED, ha="center",
        bbox=dict(boxstyle="round,pad=0.14", facecolor="#f8fafc", edgecolor="none", alpha=0.88)
    )

    # Invalid centre beta on the secant line
    ax1.scatter([beta_xy[0]], [beta_xy[1]], s=120, facecolor="#fee2e2", edgecolor=RED, lw=2.2, zorder=6)
    ax1.scatter([beta_xy[0]], [beta_xy[1]], s=80, marker="x", color=RED, lw=2.4, zorder=7)
    ax1.text(
        7.65, 3.62,
        "Invalid centre $\\beta = \\langle(1,1,0,0)\\rangle$\n"
        "$\\langle \\beta, \\epsilon(p_1) \\rangle = \\langle \\beta, \\epsilon(p_3) \\rangle$ (collides)",
        fontsize=8.9, fontweight="bold", color=RED, ha="center", va="bottom",
        bbox=dict(boxstyle="round,pad=0.22", facecolor="#fef2f2", edgecolor="#fca5a5", lw=1.1)
    )

    # Quotient screen Sigma_alpha at bottom
    screen_y = 1.05
    screen_poly = Polygon(
        [(0.45, 0.50), (9.05, 0.50), (9.55, 1.55), (0.95, 1.55)],
        closed=True, facecolor="#eef2ff", edgecolor=INDIGO, lw=1.7, zorder=1
    )
    ax1.add_patch(screen_poly)
    ax1.text(8.88, 0.68, "Quotient space $\\Sigma_\\alpha$", fontsize=10.0, fontweight="bold", color=INDIGO, ha="right")

    # Project p1, p2, p0, p4, p3 from alpha_xy down to screen_y
    pts_list = [
        (p1_xy, "$\\epsilon(p_1)$", (-0.82, 0.14)),
        (p2_xy, "$\\epsilon(p_2)$", (-0.82, 0.08)),
        (p0_xy, "$\\epsilon(p_0)$", (0.20, 0.12)),
        (p4_xy, "$\\epsilon(p_4)$", (0.22, 0.08)),
        (p3_xy, "$\\epsilon(p_3)$", (0.18, 0.14)),
    ]
    for pt_xy, lbl, off in pts_list:
        t = (screen_y - alpha_xy[1]) / (pt_xy[1] - alpha_xy[1])
        proj_xy = alpha_xy + t * (pt_xy - alpha_xy)
        ax1.plot(
            [alpha_xy[0], proj_xy[0]], [alpha_xy[1], proj_xy[1]],
            color="#6366f1", lw=1.3, ls=":", alpha=0.88, zorder=2
        )
        ax1.scatter([pt_xy[0]], [pt_xy[1]], s=72, color=TEAL, edgecolor="white", lw=1.2, zorder=6)
        ax1.text(
            pt_xy[0] + off[0], pt_xy[1] + off[1], lbl,
            fontsize=9.6, fontweight="bold", color=DARK,
            bbox=dict(boxstyle="round,pad=0.10", facecolor="#f8fafc", edgecolor="none", alpha=0.82),
            zorder=7
        )
        ax1.scatter([proj_xy[0]], [proj_xy[1]], s=56, color=INDIGO, edgecolor="white", lw=1.0, zorder=5)

    ax1.scatter([alpha_xy[0]], [alpha_xy[1]], s=165, marker="*", color=GREEN, edgecolor="white", lw=1.0, zorder=7)
    ax1.text(
        6.55, 7.25,
        "Valid centre $\\alpha = \\langle(1,1,1,0)\\rangle$\n(misses all secants $\\Rightarrow$ injective)",
        fontsize=9.1, fontweight="bold", color=GREEN, ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.22", facecolor="#f0fdf4", edgecolor="#86efac", lw=1.1)
    )
    ax1.annotate(
        "", xy=(3.88, 7.35), xytext=(4.62, 7.30),
        arrowprops=dict(arrowstyle="->", lw=1.5, color=GREEN)
    )

    # -------------------------------------------------------------------------
    # Panel (b): Book of pages — Quotienting PG(3, F) by a 1D spine line alpha
    # -------------------------------------------------------------------------
    ax2.set_xlim(-0.4, 10.4)
    ax2.set_ylim(-0.3, 8.6)
    ax2.axis("off")
    ax2.set_title(
        "(b) Projecting $\\mathrm{PG}(3, \\mathbb{F})$ from a Line $\\alpha$: Pages Around a Spine",
        fontsize=12.0,
        fontweight="bold",
        color=DARK,
        pad=10,
    )

    bg2 = FancyBboxPatch(
        (0.0, 0.0), 10.0, 8.1,
        boxstyle="round,pad=0.15",
        facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.5, zorder=0
    )
    ax2.add_patch(bg2)

    spine_x = 2.05
    spine_bot = np.array([spine_x, 1.05])
    spine_top = np.array([spine_x, 7.25])

    pages_spec = [
        (np.array([7.35, 7.55]), np.array([7.35, 3.35]), "#dbeafe", "#2563eb", (0.34, 0.62), "$\\epsilon(p_1)$", "Page $\\langle \\alpha, \\epsilon(p_1) \\rangle_\\Sigma$", (7.50, 6.75)),
        (np.array([8.55, 6.15]), np.array([8.55, 1.95]), "#dcfce7", "#16a34a", (0.68, 0.50), "$\\epsilon(p_2)$", "Page $\\langle \\alpha, \\epsilon(p_2) \\rangle_\\Sigma$", (8.68, 4.45)),
        (np.array([7.75, 4.55]), np.array([7.75, 0.55]), "#fef3c7", "#d97706", (0.42, 0.36), "$\\epsilon(p_3)$", "Page $\\langle \\alpha, \\epsilon(p_3) \\rangle_\\Sigma$", (7.90, 1.15)),
    ]

    skewer_start = np.array([4.35, 7.45])
    skewer_end = np.array([7.35, 0.75])
    ax2.plot(
        [skewer_start[0], skewer_end[0]], [skewer_start[1], skewer_end[1]],
        color=MAGENTA, lw=2.8, zorder=6
    )
    ax2.text(
        4.10, 7.50,
        "1D screen line $T$ (skew to $\\alpha$):\n$\\dim(\\Sigma_\\alpha) = 3 - 1 - 1 = 1$",
        fontsize=9.1, fontweight="bold", color=MAGENTA, ha="left", va="bottom"
    )

    pierce_ts = [0.23, 0.50, 0.78]
    for (tr, br, fc, ec, (u, v), p_lbl, pg_lbl, lbl_xy), ts in zip(pages_spec, pierce_ts):
        poly = Polygon([spine_bot, spine_top, tr, br], closed=True, facecolor=fc, edgecolor=ec, lw=1.6, alpha=0.58, zorder=2)
        ax2.add_patch(poly)
        pt_xy = (1 - u) * (v * spine_top + (1 - v) * spine_bot) + u * (v * tr + (1 - v) * br)
        ax2.scatter([pt_xy[0]], [pt_xy[1]], s=72, color=ec, edgecolor="white", lw=1.2, zorder=5)
        ax2.text(
            pt_xy[0] + 0.16, pt_xy[1] + 0.12, p_lbl,
            fontsize=9.8, fontweight="bold", color=DARK, zorder=7,
            bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor="none", alpha=0.75)
        )
        ax2.text(lbl_xy[0], lbl_xy[1], pg_lbl, fontsize=8.8, fontweight="bold", color=ec, va="center")
        q_xy = (1 - ts) * skewer_start + ts * skewer_end
        ax2.scatter([q_xy[0]], [q_xy[1]], s=82, color=MAGENTA, edgecolor="white", lw=1.3, zorder=8)

    ax2.plot([spine_x, spine_x], [0.7, 7.6], color=RED, lw=3.6, zorder=7)
    ax2.text(
        spine_x - 0.18, 4.15,
        "Hinge line $\\alpha$\n($\\dim \\alpha = 1$)",
        fontsize=9.6, fontweight="bold", color=RED, ha="right", va="center",
        bbox=dict(boxstyle="round,pad=0.22", facecolor="#fef2f2", edgecolor="#fca5a5", lw=1.1)
    )

    fig.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "maths4_embeddings_quotient_book.png"
    fig.savefig(out_path, dpi=220, facecolor="white")
    plt.close(fig)
    return out_path


def make_figure_23_fan_hyperplanes(out_dir: Path) -> Path:
    """Figure 14: All 15 hyperplanes of the 3-vane fan in PG(3,2), plus a labelled Key fan diagram."""
    pts, lines, planes, surviving, killed, alpha, _ = build_fan3_pg32()

    case_a_surv = sorted([(a, H) for a, H in surviving.items() if "p0" in H], key=lambda x: (len(x[1]), sorted(x[1])))
    case_a_kill = sorted([(a, H) for a, H in killed.items() if "p0" in H], key=lambda x: (len(x[1]), sorted(x[1])))
    case_b_surv = sorted([(a, H) for a, H in surviving.items() if "p0" not in H], key=lambda x: sorted(x[1]))
    case_b_kill = sorted([(a, H) for a, H in killed.items() if "p0" not in H], key=lambda x: sorted(x[1]))

    assert len(case_a_surv) == 3 and len(case_a_kill) == 4
    assert len(case_b_surv) == 4 and len(case_b_kill) == 4

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["mathtext.fontset"] = "cm"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.2, 6.4), dpi=220)
    fig.patch.set_facecolor("white")

    mini_pos = {
        "p0": np.array([0.0, 0.58]),
        "p2": np.array([-0.42, 0.05]),
        "p1": np.array([-0.82, -0.48]),
        "p4": np.array([0.0, -0.02]),
        "p3": np.array([0.0, -0.62]),
        "p6": np.array([0.42, 0.05]),
        "p5": np.array([0.82, -0.48]),
    }

    def format_eq(a):
        terms = [f"x_{i}" for i, ai in enumerate(a) if ai == 1]
        return " + ".join(terms) + " = 0"

    def draw_key_fan(ax, cx, cy):
        w, h = 2.15, 2.25
        card = FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.08", facecolor="#f8fafc", edgecolor=BLUE, lw=1.8, zorder=1
        )
        ax.add_patch(card)

        for _, (u, v, _) in lines:
            p_start = mini_pos[u] + np.array([cx, cy - 0.05])
            p_end = mini_pos[v] + np.array([cx, cy - 0.05])
            ax.plot([p_start[0], p_end[0]], [p_start[1], p_end[1]], color=TEAL, lw=2.2, zorder=2)

        key_offsets = {
            "p0": (0.26, 0.06),
            "p2": (-0.28, 0.10),
            "p1": (-0.14, -0.22),
            "p4": (-0.25, -0.04),
            "p3": (0.25, -0.04),
            "p6": (0.28, 0.10),
            "p5": (0.14, -0.22),
        }
        for name, rel in mini_pos.items():
            px, py = cx + rel[0], cy - 0.05 + rel[1]
            is_hub = name == "p0"
            ax.scatter(
                [px], [py],
                s=56 if is_hub else 44,
                facecolor=MAGENTA if is_hub else TEAL,
                edgecolor="white", lw=1.0, zorder=4
            )
            ox, oy = key_offsets[name]
            lbl = "$" + name.replace("p", "p_") + "$"
            ax.text(
                px + ox, py + oy, lbl,
                fontsize=8.2, fontweight="bold", color=DARK, ha="center", va="center", zorder=5
            )

        ax.text(
            cx, cy + h / 2 - 0.18,
            "Key: Point Labels",
            fontsize=8.3, fontweight="bold", color=BLUE, ha="center", va="center"
        )
        ax.text(
            cx, cy - h / 2 + 0.17,
            "$L_1, L_2, L_3$ from $p_0$",
            fontsize=7.9, fontweight="bold", color=TEAL, ha="center", va="center"
        )

    def draw_mini_fan(ax, cx, cy, a, H, survives: bool, subtitle: str):
        w, h = 2.15, 2.25
        fc = "#f0fdf4" if survives else "#fef2f2"
        ec = "#16a34a" if survives else "#dc2626"
        hi_col = "#15803d" if survives else "#b91c1c"
        card = FancyBboxPatch(
            (cx - w / 2, cy - h / 2), w, h,
            boxstyle="round,pad=0.08", facecolor=fc, edgecolor=ec, lw=1.5, zorder=1
        )
        ax.add_patch(card)

        for _, (u, v, w_pt) in lines:
            p_start = mini_pos[u] + np.array([cx, cy - 0.05])
            p_end = mini_pos[v] + np.array([cx, cy - 0.05])
            full_in_H = (u in H) and (v in H) and (w_pt in H)
            ax.plot(
                [p_start[0], p_end[0]], [p_start[1], p_end[1]],
                color=hi_col if full_in_H else "#cbd5e1",
                lw=2.5 if full_in_H else 1.4, zorder=2
            )

        for name, rel in mini_pos.items():
            px, py = cx + rel[0], cy - 0.05 + rel[1]
            in_h = name in H
            ax.scatter(
                [px], [py],
                s=52 if in_h else 26,
                facecolor=hi_col if in_h else "white",
                edgecolor="white" if in_h else "#64748b",
                lw=1.0, zorder=4
            )

        ax.text(
            cx, cy + h / 2 - 0.18,
            f"${format_eq(a)}$",
            fontsize=8.2, fontweight="bold", color=DARK, ha="center", va="center"
        )
        ax.text(
            cx, cy - h / 2 + 0.17,
            subtitle,
            fontsize=8.0, fontweight="bold", color=hi_col, ha="center", va="center"
        )

    # Panel (a): Key fan + 7 hyperplanes through p0 (a3 = 0)
    ax1.set_xlim(0.0, 10.2)
    ax1.set_ylim(0.0, 6.5)
    ax1.axis("off")
    ax1.set_title(
        "(a) Key & $7$ Hyperplanes Through $p_0$ ($a_3 = 0$): $3$ Survive, $4$ Killed",
        fontsize=11.6, fontweight="bold", color=DARK, pad=8
    )

    ax1.text(
        0.2, 5.95,
        "Key and $3$ surviving hyperplanes in $\\mathrm{PG}(2,2)$ ($\\alpha \\in \\Pi,\\; a_0+a_1+a_2=0$):",
        fontsize=9.2, fontweight="bold", color="#15803d"
    )
    draw_key_fan(ax1, 1.35, 4.55)
    surv_a_labels = {
        frozenset(["p0", "p1", "p2"]): "$L_1 = \\{p_0,p_1,p_2\\}$",
        frozenset(["p0", "p3", "p4"]): "$L_2 = \\{p_0,p_3,p_4\\}$",
        frozenset(["p0", "p5", "p6"]): "$L_3 = \\{p_0,p_5,p_6\\}$",
    }
    for idx, (a, H) in enumerate(case_a_surv):
        draw_mini_fan(ax1, 1.35 + (idx + 1) * 2.48, 4.55, a, H, True, surv_a_labels[H])

    ax1.text(
        0.2, 2.95,
        "Killed by $/\\alpha$ ($\\alpha \\notin \\Pi,\\; a_0+a_1+a_2=1$): singleton $\\{p_0\\}$ and $3$ two-vane unions",
        fontsize=9.2, fontweight="bold", color="#b91c1c"
    )
    kill_a_labels = {
        frozenset(["p0"]): "$\\{p_0\\}$ (size $1$)",
        frozenset(["p0", "p1", "p2", "p3", "p4"]): "$L_1 \\cup L_2$ (size $5$)",
        frozenset(["p0", "p1", "p2", "p5", "p6"]): "$L_1 \\cup L_3$ (size $5$)",
        frozenset(["p0", "p3", "p4", "p5", "p6"]): "$L_2 \\cup L_3$ (size $5$)",
    }
    for idx, (a, H) in enumerate(case_a_kill):
        draw_mini_fan(ax1, 1.35 + idx * 2.48, 1.55, a, H, False, kill_a_labels[H])

    # Panel (b): 8 three-point ovoids missing p0 (a3 = 1)
    ax2.set_xlim(0.0, 10.2)
    ax2.set_ylim(0.0, 6.5)
    ax2.axis("off")
    ax2.set_title(
        "(b) $8$ Ovoids Missing $p_0$ ($a_3 = 1$): $4$ Survive as Fano Lines, $4$ Killed",
        fontsize=11.6, fontweight="bold", color=DARK, pad=8
    )

    ax2.text(
        0.2, 5.95,
        "Survive as the $4$ new Fano lines of $\\mathrm{PG}(2,2)$ ($\\alpha \\in \\Pi,\\; a_0+a_1+a_2=0$):",
        fontsize=9.2, fontweight="bold", color="#15803d"
    )
    for idx, (a, H) in enumerate(case_b_surv):
        pts_str = ",".join(sorted(H))
        lbl = "$\\{" + pts_str.replace("p", "p_") + "\\}$"
        draw_mini_fan(ax2, 1.35 + idx * 2.48, 4.55, a, H, True, lbl)

    ax2.text(
        0.2, 2.95,
        "Killed by $/\\alpha$ ($\\alpha \\notin \\Pi,\\; a_0+a_1+a_2=1$, become triangles in $\\mathrm{PG}(2,2)$):",
        fontsize=9.2, fontweight="bold", color="#b91c1c"
    )
    for idx, (a, H) in enumerate(case_b_kill):
        pts_str = ",".join(sorted(H))
        lbl = "$\\{" + pts_str.replace("p", "p_") + "\\}$"
        draw_mini_fan(ax2, 1.35 + idx * 2.48, 1.55, a, H, False, lbl)

    fig.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "maths4_embeddings_fan_hyperplanes.png"
    fig.savefig(out_path, dpi=220, facecolor="white")
    plt.close(fig)
    return out_path


def make_figure_24_quotient(out_dir: Path) -> Path:
    """Figure 15: Redrawn Panel (a) (3 noncollinear y_i spanning plane through x in alpha) + touched-up Panel (b)."""
    build_fan3_pg32()

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["mathtext.fontset"] = "cm"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0, 6.5), dpi=220)
    fig.patch.set_facecolor("white")

    # ==========================================================================
    # Panel (a): Redesigned — Three noncollinear epsilon(y_i) spanning a plane
    # containing x in alpha; Pi supset alpha survives, Pi' through y1,y2 missing y3 is killed
    # ==========================================================================
    ax1.set_xlim(-0.3, 10.3)
    ax1.set_ylim(-0.4, 8.8)
    ax1.axis("off")
    ax1.set_title(
        "(a) Quotient $\\epsilon/\\alpha : \\mathcal{S} \\to \\Sigma_\\alpha$"
        " and Why $\\mathcal{H}_{\\epsilon/\\alpha} \\subsetneq \\mathcal{H}_\\epsilon$",
        fontsize=12.1,
        fontweight="bold",
        pad=10,
        color="#1a2530",
    )
    sigma_box = patches.FancyBboxPatch(
        (0.0, 0.0), 10.0, 8.2,
        boxstyle="round,pad=0.18",
        facecolor="#f8fafc", edgecolor="#94a3b8", lw=1.6,
    )
    ax1.add_patch(sigma_box)
    ax1.text(
        0.35, 7.8,
        "Ambient projective space $\\Sigma = \\langle \\epsilon(\\mathcal{P}) \\rangle_\\Sigma$",
        fontsize=10.3, fontweight="bold", color="#334155",
    )

    alpha_pt = np.array([4.65, 6.95])

    screen_poly = patches.Polygon(
        [(0.8, 0.42), (9.1, 0.42), (9.55, 2.15), (1.25, 2.15)],
        closed=True, facecolor="#eef2ff", edgecolor="#4f46e5", lw=1.8, zorder=2,
    )
    ax1.add_patch(screen_poly)
    ax1.text(
        9.15, 1.78, "Quotient space $\\Sigma_\\alpha$",
        fontsize=10.1, fontweight="bold", color="#3730a3", ha="right",
    )

    py1 = np.array([2.10, 1.32])
    py2 = np.array([4.35, 1.24])
    py3 = np.array([6.55, 1.16])

    y1 = alpha_pt + 0.48 * (py1 - alpha_pt)
    y2 = alpha_pt + 0.65 * (py2 - alpha_pt)
    y3 = alpha_pt + 0.46 * (py3 - alpha_pt)

    spanned_plane = patches.Polygon(
        [alpha_pt, y1, y2, y3],
        closed=True, facecolor="#ccfbf1", edgecolor="#0d9488", lw=1.3, ls=":", alpha=0.58, zorder=2
    )
    ax1.add_patch(spanned_plane)
    ax1.text(
        4.48, 5.15,
        "Plane $\\langle \\epsilon(y_1), \\epsilon(y_2), \\epsilon(y_3) \\rangle_\\Sigma \\ni x$",
        fontsize=8.6, fontweight="bold", color="#0f766e", ha="center",
        bbox=dict(boxstyle="round,pad=0.14", facecolor="#f0fdfa", edgecolor="#99f6e4", lw=0.9, alpha=0.92),
        zorder=5
    )

    d_q = py3 - py1
    ax1.plot(
        [py1[0] - 0.14 * d_q[0], py3[0] + 0.14 * d_q[0]],
        [py1[1] - 0.14 * d_q[1], py3[1] + 0.14 * d_q[1]],
        color="#4338ca", lw=2.6, zorder=4
    )

    for pt, ppt, lbl, off, q_lbl in [
        (y1, py1, "$\\epsilon(y_1)$", (-0.88, 0.14), "$\\langle\\alpha,\\epsilon(y_1)\\rangle$"),
        (y2, py2, "$\\epsilon(y_2)$", (0.20, -0.08), "$\\langle\\alpha,\\epsilon(y_2)\\rangle$"),
        (y3, py3, "$\\epsilon(y_3)$", (0.20, 0.16), "$\\langle\\alpha,\\epsilon(y_3)\\rangle$"),
    ]:
        ax1.plot(
            [alpha_pt[0], ppt[0]], [alpha_pt[1], ppt[1]],
            color="#6366f1", lw=1.4, ls="--", alpha=0.85, zorder=3
        )
        ax1.scatter([pt[0]], [pt[1]], s=75, color="#0f766e", edgecolor="white", lw=1.2, zorder=6)
        ax1.text(
            pt[0] + off[0], pt[1] + off[1], lbl,
            fontsize=10.0, color="#0f766e", fontweight="bold",
            bbox=dict(boxstyle="round,pad=0.10", facecolor="#f8fafc", edgecolor="none", alpha=0.85),
            zorder=7
        )
        ax1.scatter([ppt[0]], [ppt[1]], s=62, color="#4338ca", edgecolor="white", lw=1.1, zorder=6)
        ax1.text(ppt[0], ppt[1] - 0.44, q_lbl, fontsize=8.8, color="#3730a3", ha="center")

    alpha_halo = patches.Circle(
        alpha_pt, 0.30, facecolor="#fee2e2", edgecolor="#dc2626", lw=2.0, zorder=6
    )
    ax1.add_patch(alpha_halo)
    ax1.scatter([alpha_pt[0]], [alpha_pt[1]], s=65, color="#dc2626", zorder=7)
    ax1.text(
        5.12, 6.98,
        "Point $x \\in \\alpha$ in minimal span\n"
        "$x \\in \\langle \\epsilon(y_1), \\epsilon(y_2), \\epsilon(y_3) \\rangle_\\Sigma$",
        fontsize=9.1, fontweight="bold", color="#b91c1c", ha="left", va="center", linespacing=1.2
    )

    d_pi = py1 - alpha_pt
    p_start = alpha_pt - 0.12 * d_pi
    p_end = alpha_pt + 1.06 * d_pi
    ax1.plot(
        [p_start[0], p_end[0]], [p_start[1], p_end[1]],
        color="#d97706", lw=2.4, ls="-", alpha=0.9, zorder=4
    )
    ax1.text(
        0.28, 5.65,
        "$\\Pi \\supset \\alpha$ survives:\n$H_\\Pi \\in \\mathcal{H}_{\\epsilon/\\alpha} \\subseteq \\mathcal{H}_\\epsilon$",
        fontsize=9.1, fontweight="bold", color="#b45309"
    )
    ax1.annotate(
        "", xy=(3.48, 4.45), xytext=(2.15, 5.45),
        arrowprops=dict(arrowstyle="->", lw=1.4, color="#d97706")
    )

    d_pi_prime = y2 - y1
    p1_ext = y1 - 0.78 * d_pi_prime
    p2_ext = y2 + 1.35 * d_pi_prime
    ax1.plot(
        [p1_ext[0], p2_ext[0]], [p1_ext[1], p2_ext[1]],
        color="#be185d", lw=2.2, ls="-.", alpha=0.95, zorder=5
    )
    ax1.text(
        6.15, 3.15,
        "$\\Pi'$ through $\\epsilon(y_1), \\epsilon(y_2)$\n"
        "misses $\\epsilon(y_3)$ and $\\alpha$:\n"
        "$H_{\\Pi'} \\in \\mathcal{H}_\\epsilon \\backslash \\mathcal{H}_{\\epsilon/\\alpha}$ (killed)",
        fontsize=8.8, fontweight="bold", color="#9d174d",
        bbox=dict(boxstyle="round,pad=0.2", facecolor="#fdf2f8", edgecolor="#f472b6", lw=1.0),
        zorder=7
    )

    # ==========================================================================
    # Panel (b): 3-Vane Fan PG(3,2) vs PG(2,2) with p2 clear of line & compact box
    # ==========================================================================
    ax2.set_xlim(-0.3, 10.6)
    ax2.set_ylim(-0.4, 8.8)
    ax2.axis("off")
    ax2.set_title(
        "(b) Worked Example: $3$-Vane Fan $\\tilde{\\epsilon}:\\mathcal{S}\\to\\mathrm{PG}(3,2)$"
        " vs. $\\tilde{\\epsilon}/\\alpha:\\mathcal{S}\\to\\mathrm{PG}(2,2)$",
        fontsize=12.0,
        fontweight="bold",
        pad=10,
        color="#1a2530",
    )
    ax2.text(
        2.15, 8.05,
        "Universal $\\tilde{\\epsilon} : \\mathcal{S} \\to \\mathrm{PG}(3,2)$",
        fontsize=10.7, fontweight="bold", color="#0f766e", ha="center",
    )
    ax2.text(
        2.15, 7.52,
        "$|\\mathcal{H}_{\\tilde{\\epsilon}}| = 15$ (all hyperplanes of $\\mathcal{S}$)",
        fontsize=9.4, color="#334155", ha="center",
    )

    p0_L = (2.15, 6.25)
    vane_pts_L = [
        ((0.55, 4.7), (1.35, 5.48), "$p_1$", "$p_2$", (-0.32, -0.22), (-0.46, 0.12)),
        ((2.15, 4.3), (2.15, 5.28), "$p_3$", "$p_4$", (-0.38, -0.10), (-0.38, -0.05)),
        ((3.75, 4.7), (2.95, 5.48), "$p_5$", "$p_6$", (0.22, -0.25), (0.24, 0.12)),
    ]
    h5_poly = patches.Polygon(
        [(2.15, 6.90), (0.55, 6.05), (-0.12, 4.42), (2.52, 3.78), (2.62, 5.70)],
        closed=True, facecolor="#fce7f3", edgecolor="#db2777", lw=1.4, ls="--", alpha=0.7, zorder=1,
    )
    ax2.add_patch(h5_poly)
    ax2.text(
        0.05, 3.38,
        "$H' = \\{p_0,p_1,p_2,p_3,p_4\\} \\in \\mathcal{H}_{\\tilde{\\epsilon}} \\backslash \\mathcal{H}_{\\tilde{\\epsilon}/\\alpha}$",
        fontsize=8.8, color="#9d174d", fontweight="bold",
    )

    for pend, pmid, l1, l2, o1, o2 in vane_pts_L:
        ax2.plot([p0_L[0], pend[0]], [p0_L[1], pend[1]], color="#0f766e", lw=2.4, zorder=3)
        ax2.scatter(
            [pend[0], pmid[0]], [pend[1], pmid[1]],
            s=65, color="#0f766e", edgecolor="white", lw=1.1, zorder=5,
        )
        ax2.text(pend[0] + o1[0], pend[1] + o1[1], l1, fontsize=9.8, fontweight="bold", color="#1e293b")
        ax2.text(pmid[0] + o2[0], pmid[1] + o2[1], l2, fontsize=9.8, fontweight="bold", color="#1e293b")

    ax2.scatter([p0_L[0]], [p0_L[1]], s=85, color="#be185d", edgecolor="white", lw=1.3, zorder=6)
    ax2.text(p0_L[0] + 0.22, p0_L[1] + 0.16, "$p_0$", fontsize=10.2, fontweight="bold", color="#9d174d")

    ax2.annotate(
        "", xy=(5.95, 5.45), xytext=(4.25, 5.45),
        arrowprops=dict(arrowstyle="->", lw=2.4, color="#dc2626"),
    )
    ax2.text(5.1, 6.02, "Quotient by", fontsize=9.2, fontweight="bold", color="#b91c1c", ha="center")
    ax2.text(5.1, 5.62, "$\\alpha = \\langle(1,1,1,0)\\rangle$", fontsize=9.0, color="#b91c1c", ha="center")
    ax2.text(
        5.1, 4.96,
        "$x = \\tilde{\\epsilon}(p_1)+\\tilde{\\epsilon}(p_3)+\\tilde{\\epsilon}(p_5)$",
        fontsize=8.3, color="#7f1d1d", ha="center",
    )

    ax2.text(
        8.25, 8.05,
        "Quotient $\\tilde{\\epsilon}/\\alpha : \\mathcal{S} \\to \\mathrm{PG}(2,2)$",
        fontsize=10.7, fontweight="bold", color="#3730a3", ha="center",
    )
    ax2.text(
        8.25, 7.52,
        "$|\\mathcal{H}_{\\tilde{\\epsilon}/\\alpha}| = 7$ (only the $7$ Fano lines)",
        fontsize=9.4, color="#334155", ha="center",
    )

    fp0 = np.array([8.25, 6.75])
    fp1 = np.array([6.55, 4.10])
    fp5 = np.array([9.95, 4.10])
    fp2 = 0.5 * (fp0 + fp1)
    fp6 = 0.5 * (fp0 + fp5)
    fp3 = 0.5 * (fp1 + fp5)
    fp4 = (fp0 + fp1 + fp5) / 3.0
    for a_pt, b_pt in [(fp0, fp1), (fp0, fp3), (fp0, fp5)]:
        ax2.plot([a_pt[0], b_pt[0]], [a_pt[1], b_pt[1]], color="#0f766e", lw=2.5, zorder=4)
    ax2.plot([fp1[0], fp5[0]], [fp1[1], fp5[1]], color="#dc2626", lw=2.3, ls="--", zorder=3)
    ax2.plot([fp1[0], fp6[0]], [fp1[1], fp6[1]], color="#7c3aed", lw=1.6, ls=":", zorder=3)
    ax2.plot([fp5[0], fp2[0]], [fp5[1], fp2[1]], color="#7c3aed", lw=1.6, ls=":", zorder=3)
    fano_circ = patches.Circle(
        fp4, np.linalg.norm(fp3 - fp4),
        fill=False, edgecolor="#7c3aed", lw=1.6, ls=":", zorder=3,
    )
    ax2.add_patch(fano_circ)

    for pt, lbl, off in [
        (fp0, "$p_0$", (0.0, 0.22)),
        (fp1, "$p_1$", (-0.28, -0.18)),
        (fp5, "$p_5$", (0.22, -0.18)),
        (fp2, "$p_2$", (-0.34, 0.08)),
        (fp6, "$p_6$", (0.32, 0.08)),
        (fp3, "$p_3$", (0.0, -0.34)),
        (fp4, "$p_4$", (0.28, 0.16)),
    ]:
        ax2.scatter([pt[0]], [pt[1]], s=65, color="#3730a3", edgecolor="white", lw=1.1, zorder=6)
        ax2.text(pt[0] + off[0], pt[1] + off[1], lbl, fontsize=9.8, fontweight="bold", color="#1e293b", ha="center")

    # Compact explanation box without empty top half
    info_box = patches.FancyBboxPatch(
        (0.0, 0.45), 10.35, 2.15,
        boxstyle="round,pad=0.16", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.4,
    )
    ax2.add_patch(info_box)
    summary_text = (
        "Why $8$ hyperplanes vanish in the quotient $\\tilde{\\epsilon}/\\alpha$:\n"
        "• Solid teal lines = the $3$ lines of $\\mathcal{S}$ ($\\{p_0,p_1,p_2\\}, \\{p_0,p_3,p_4\\}, \\{p_0,p_5,p_6\\}$).\n"
        "• Dashed red line $\\{p_1,p_3,p_5\\}$ = a new collinearity forced because $x = \\tilde{\\epsilon}(p_1)+\\tilde{\\epsilon}(p_3)+\\tilde{\\epsilon}(p_5) \\in \\alpha$.\n"
        "• Any line of $\\mathrm{PG}(2,2)$ through $p_1,p_3$ contains $p_5$, ruling out $H' = \\{p_0,p_1,p_2,p_3,p_4\\}$;\n"
        "  and every line of $\\mathrm{PG}(2,2)$ meets $\\{p_1,p_3,p_5\\}$, ruling out $\\{p_0\\}$ (its $\\mathrm{PG}(3,2)$-plane misses $\\alpha$)."
    )
    ax2.text(0.22, 1.52, summary_text, fontsize=8.65, color="#1e293b", va="center", linespacing=1.38)

    fig.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "maths4_embeddings_quotient.png"
    fig.savefig(out_path, dpi=220, facecolor="white")
    plt.close(fig)
    return out_path


def make_figure_25_ag23_parity(out_dir: Path) -> Path:
    """Figure 16: Why AG(2,3) has zero hyperplanes — pencil through p in H (odd) vs pencil through q not in H (even=4)."""
    F3 = (0, 1, 2)
    pts = [(x, y) for y in F3 for x in F3]
    assert len(pts) == 9
    lines = []
    for a, b in [(1, 0), (0, 1), (1, 1), (1, 2)]:
        for c in F3:
            L = frozenset(p for p in pts if (a * p[0] + b * p[1]) % 3 == c)
            lines.append(L)
    assert len(lines) == 12 and all(len(L) == 3 for L in lines)

    hyps = [
        sub for r in range(1, 9)
        for sub in it.combinations(pts, r)
        if all(len(frozenset(sub) & L) in (1, 3) for L in lines)
    ]
    assert len(hyps) == 0

    center = (1, 1)
    pencil = [L for L in lines if center in L]
    assert len(pencil) == 4
    rays = [L - {center} for L in pencil]
    assert all(len(r) == 2 for r in rays)
    assert set().union(*rays) == set(pts) - {center}

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["mathtext.fontset"] = "cm"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.4, 6.2), dpi=220)
    fig.patch.set_facecolor("white")

    ray_specs = [
        ((0, 1), (2, 1), "#2563eb", "$L_1$ (slope $0$)"),
        ((1, 0), (1, 2), "#16a34a", "$L_2$ (slope $\\infty$)"),
        ((0, 0), (2, 2), "#d97706", "$L_3$ (slope $1$)"),
        ((0, 2), (2, 0), "#7c3aed", "$L_4$ (slope $2$)"),
    ]

    def grid_xy(pt):
        return np.array([1.8 + pt[0] * 1.65, 2.35 + pt[1] * 1.55])

    # -------------------------------------------------------------------------
    # Panel (a): View from p in H -> |H| is ODD (all 4 lines annotated)
    # -------------------------------------------------------------------------
    ax1.set_xlim(0.0, 7.2)
    ax1.set_ylim(0.0, 6.9)
    ax1.axis("off")
    ax1.set_title(
        "(a) Pencil Through $p \\in H$ Forces $|H|$ to Be Odd",
        fontsize=12.0, fontweight="bold", color=DARK, pad=10
    )

    bg1 = FancyBboxPatch(
        (0.15, 0.15), 6.9, 6.45,
        boxstyle="round,pad=0.12", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.5, zorder=0
    )
    ax1.add_patch(bg1)

    c_xy = grid_xy(center)
    in_H_a = {center, (0, 1), (2, 1)}

    for pa, pb, col, lbl in ray_specs:
        pa_xy, pb_xy = grid_xy(pa), grid_xy(pb)
        ax1.plot([pa_xy[0], pb_xy[0]], [pa_xy[1], pb_xy[1]], color=col, lw=2.8, alpha=0.85, zorder=2)
        for pt in (pa, pb):
            pt_xy = grid_xy(pt)
            filled = pt in in_H_a
            ax1.scatter(
                [pt_xy[0]], [pt_xy[1]], s=190,
                facecolor=col if filled else "white",
                edgecolor=col, lw=2.4, zorder=4
            )
            ax1.text(
                pt_xy[0], pt_xy[1] - 0.36,
                f"$({pt[0]},{pt[1]})$", fontsize=8.4, color=DARK, ha="center", va="center", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.07", facecolor="#f8fafc", edgecolor="none", alpha=0.92),
                zorder=5
            )

    ax1.scatter([c_xy[0]], [c_xy[1]], s=260, color=RED, edgecolor="white", lw=1.8, zorder=6)
    ax1.text(
        c_xy[0] + 0.56, c_xy[1] + 0.26, "$p \\in H$",
        fontsize=10.2, fontweight="bold", color=RED, ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.16", facecolor="white", edgecolor="#fca5a5", lw=1.1),
        zorder=8
    )

    # Annotate all four lines L1, L2, L3, L4 in Panel (a)
    ax1.text(
        5.52, 4.05, "$+2$ on $L_1$\n($|H \\cap L_1|=3$)",
        fontsize=8.5, fontweight="bold", color="#2563eb", ha="left", va="center"
    )
    ax1.text(
        3.45, 5.95, "$+0$ on $L_2$ ($|H \\cap L_2|=1$)",
        fontsize=8.5, fontweight="bold", color="#16a34a", ha="center"
    )
    ax1.text(
        5.52, 5.55, "$+0$ on $L_3$\n($|H \\cap L_3|=1$)",
        fontsize=8.5, fontweight="bold", color="#d97706", ha="left", va="center"
    )
    ax1.text(
        5.52, 2.35, "$+0$ on $L_4$\n($|H \\cap L_4|=1$)",
        fontsize=8.5, fontweight="bold", color="#7c3aed", ha="left", va="center"
    )

    box1 = FancyBboxPatch(
        (0.4, 0.35), 6.4, 1.35,
        boxstyle="round,pad=0.12", facecolor="#fef2f2", edgecolor="#fca5a5", lw=1.2, zorder=3
    )
    ax1.add_patch(box1)
    ax1.text(
        3.6, 1.02,
        "Since $p \\in H$ and $|H \\cap L_i| \\in \\{1, 3\\}$, each of the $4$ rays $L_i \\backslash \\{p\\}$\n"
        "contributes $0$ or $2$ points (even) $\\Rightarrow |H| = 1 + \\mathrm{even}$ is odd.",
        fontsize=9.2, color=DARK, ha="center", va="center", linespacing=1.35, fontweight="bold"
    )

    # -------------------------------------------------------------------------
    # Panel (b): View from q not in H -> |H| = 4 (EVEN)
    # -------------------------------------------------------------------------
    ax2.set_xlim(0.0, 7.2)
    ax2.set_ylim(0.0, 6.9)
    ax2.axis("off")
    ax2.set_title(
        "(b) Pencil Through $q \\notin H$ Forces $|H| = 4$ (Even)",
        fontsize=12.0, fontweight="bold", color=DARK, pad=10
    )

    bg2 = FancyBboxPatch(
        (0.15, 0.15), 6.9, 6.45,
        boxstyle="round,pad=0.12", facecolor="#f8fafc", edgecolor="#cbd5e1", lw=1.5, zorder=0
    )
    ax2.add_patch(bg2)

    in_H_b = {(0, 1), (1, 2), (2, 2), (2, 0)}
    for pa, pb, col, lbl in ray_specs:
        pa_xy, pb_xy = grid_xy(pa), grid_xy(pb)
        ax2.plot([pa_xy[0], pb_xy[0]], [pa_xy[1], pb_xy[1]], color=col, lw=2.8, alpha=0.85, zorder=2)
        for pt in (pa, pb):
            pt_xy = grid_xy(pt)
            filled = pt in in_H_b
            ax2.scatter(
                [pt_xy[0]], [pt_xy[1]], s=190,
                facecolor=col if filled else "white",
                edgecolor=col, lw=2.4, zorder=4
            )
            ax2.text(
                pt_xy[0], pt_xy[1] - 0.36,
                f"$({pt[0]},{pt[1]})$", fontsize=8.4, color=DARK, ha="center", va="center", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.07", facecolor="#f8fafc", edgecolor="none", alpha=0.92),
                zorder=5
            )
            if filled:
                ax2.text(
                    pt_xy[0] + 0.24, pt_xy[1] + 0.18,
                    "$+1$", fontsize=8.8, fontweight="bold", color=col
                )

    ax2.scatter([c_xy[0]], [c_xy[1]], s=260, facecolor="white", edgecolor=RED, lw=2.5, zorder=6)
    ax2.scatter([c_xy[0]], [c_xy[1]], s=110, marker="x", color=RED, lw=2.4, zorder=7)
    ax2.text(
        c_xy[0] + 0.56, c_xy[1] + 0.26, "$q \\notin H$",
        fontsize=10.2, fontweight="bold", color=RED, ha="center", va="center",
        bbox=dict(boxstyle="round,pad=0.16", facecolor="white", edgecolor="#fca5a5", lw=1.1),
        zorder=8
    )

    box2 = FancyBboxPatch(
        (0.4, 0.35), 6.4, 1.35,
        boxstyle="round,pad=0.12", facecolor="#eff6ff", edgecolor="#93c5fd", lw=1.2, zorder=3
    )
    ax2.add_patch(box2)
    ax2.text(
        3.6, 1.02,
        "Since $q \\notin H$, $|H \\cap L_i| = 3$ is impossible, so $|H \\cap L_i| = 1$ on all $4$ lines:\n"
        "each ray contributes $1$ point $\\Rightarrow |H| = 1+1+1+1 = 4$ (even).",
        fontsize=9.2, color=DARK, ha="center", va="center", linespacing=1.35, fontweight="bold"
    )

    fig.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "maths4_embeddings_ag23_parity.png"
    fig.savefig(out_path, dpi=220, facecolor="white")
    plt.close(fig)
    return out_path


def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT_DIR
    f22 = make_figure_22_quotient_book(out_dir)
    f23 = make_figure_23_fan_hyperplanes(out_dir)
    f24 = make_figure_24_quotient(out_dir)
    f25 = make_figure_25_ag23_parity(out_dir)
    for p in (f22, f23, f24, f25):
        print(f"Wrote {p}")


if __name__ == "__main__":
    main()
