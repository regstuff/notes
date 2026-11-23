#!/usr/bin/env python3
"""Draw the five Linear Algebra figures (Figures 1 to 5) for 'Maths 0 - Linear & Abstract Algebra'.

Project context:
    These five 2D schematic figures accompany the Linear Algebra chapter of the Maths 0
    lecture notes (published with MkDocs Material for a physics-degree reader):
      - Figure 5 (`maths0_projection_reflection.png`): orthogonal projection onto u and u^perp,
        the two-step construction of the Householder reflector H_u = I - 2 P_u, the two
        sign choices u = x -/+ ||x|| e_1 sending x to +/-||x|| e_1, and an oblique
        projector P with ||P||_2 = sqrt(2) = 1 / sin(45 deg).
      - Figure 2 (`maths0_airline_network.png`): the five-city directed airline network with hub H
        built directly from its 5x5 adjacency matrix C, alongside two highlighted 4-flight
        walks from A to B among the [C^4]_{AB} = 7 walks.
      - Figure 1 (`maths0_unit_balls.png`): the nested 2D unit balls of the 1-, 2- and infinity-norms
        (||v||_1 >= ||v||_2 >= ||v||_inf) and norm equivalence ||v||_inf <= ||v||_1 <= 2||v||_inf.
      - Figure 4 (`maths0_induced_norms.png`): geometric meaning of the induced 1-, infinity- and
        2-norms of A = (1/sqrt(3)) [[3, -1], [0, sqrt(8)]], showing the faint unit ball, its
        image under A, and the touching norm ball(s) on identical axes.
      - Figure 3 (`maths0_two_norm_ellipse.png`): side-by-side transformation of the unit
        circle into an ellipse under A = (1/sqrt(3)) [[3, -1], [0, sqrt(8)]], tracking eight
        numbered unit vectors to their images and highlighting the maximum stretch ||A||_2 = 2
        and minimum stretch 1/||A^(-1)||_2 = sqrt(2).

Style (palette, DejaVu Sans with Computer Modern mathtext, 220 dpi, width <= 11 in,
text >= 9 pt, svg.hashsalt = "maths0", deterministic PNG metadata) is copied from
`scripts/maths_1/make_maths1_geometry_figures.py`. Every number quoted in a figure label
or caption is verified with NumPy and printed to stdout.

Usage:
    /home/ubuntu/.claude/skills/lecture-notes/.venv/bin/python -I \
        scripts/maths_0/make_maths0_linalg_figures.py docs/maths/figures
"""

from __future__ import annotations

import math
import re
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, Polygon, Rectangle
from matplotlib.path import Path as MplPath
import numpy as np

# ---------------------------------------------------------------------------
# Palette and typography (copied from make_maths1_geometry_figures.py)
# ---------------------------------------------------------------------------
NAVY = "#1e3a8a"
BLUE = "#2563eb"
BLUE_MID = "#93c5fd"
BLUE_LIGHT = "#dbeafe"
BLUE_PALE = "#eff6ff"
TEAL = "#0f766e"
TEAL_LIGHT = "#ccfbf1"
AMBER = "#d97706"
AMBER_LIGHT = "#fef3c7"
RED = "#dc2626"
RED_MID = "#fecaca"
RED_LIGHT = "#fee2e2"
SLATE = "#64748b"
GREY_LINE = "#cbd5e1"
GREY_WALL = "#f1f5f9"
GREY_BG = "#f8fafc"
TEXT = "#0f172a"

DPI = 220
MAX_WIDTH_IN = 11.0

plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
    "font.family": "DejaVu Sans",
    "font.size": 10.0,
    "axes.titlesize": 10.5,
    "axes.labelsize": 10.0,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "mathtext.fontset": "cm",
    "axes.edgecolor": GREY_LINE,
    "svg.hashsalt": "maths0",
})

PNG_META = {"Software": None}

# Detect an italic capital (optionally with a simple or braced subscript) immediately before ')' inside $...$
_MATH_SPAN_RE = re.compile(r"\$([^$]+)\$")
_ITALIC_CAP_PAREN_RE = re.compile(r"(?<![\\a-zA-Z])[A-Z](?:_(?:[a-zA-Z0-9]+|\{[^}]+\}))?\)")


def save_fig(fig: plt.Figure, out_dir: Path, filename: str) -> Path:
    """Save at 220 dpi with a tight box; enforce text >= 9 pt and width <= 11 in."""
    out_path = out_dir / filename
    try:
        for txt_obj in fig.findobj(matplotlib.text.Text):
            if txt_obj.get_visible() and txt_obj.get_text().strip():
                txt = txt_obj.get_text()
                fs = float(txt_obj.get_fontsize())
                if fs < 9.0 - 1e-6:
                    raise AssertionError(f"{filename}: text {txt!r} has fontsize {fs:.2f} pt < 9.0 pt")
                if "\u2014" in txt:
                    raise AssertionError(f"{filename}: em dash in text {txt!r}")
                for math_seg in _MATH_SPAN_RE.findall(txt):
                    if _ITALIC_CAP_PAREN_RE.search(math_seg):
                        raise AssertionError(
                            f"{filename}: italic capital before ')' needs thin space '\\,' in {txt!r}"
                        )
        fig.savefig(
            out_path,
            dpi=DPI,
            bbox_inches="tight",
            pad_inches=0.10,
            facecolor="white",
            metadata=PNG_META,
        )
    finally:
        plt.close(fig)
    with out_path.open("rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"Invalid PNG header in {out_path}")
    w_px = int.from_bytes(head[16:20], "big")
    h_px = int.from_bytes(head[20:24], "big")
    if w_px / DPI > MAX_WIDTH_IN + 1e-6:
        raise AssertionError(f"{filename} width {w_px / DPI:.2f} in exceeds {MAX_WIDTH_IN} in")
    print(f"  [saved] {out_path.name} ({w_px}x{h_px} px = {w_px / DPI:.2f}x{h_px / DPI:.2f} in)")
    return out_path


def arrow(ax, p0, p1, color=NAVY, lw=1.8, ms=13, z=6, ls="-", style="-|>", shrink=0.0):
    """Draw a straight 2D arrow from p0 to p1 in data coordinates."""
    a = FancyArrowPatch(
        tuple(p0),
        tuple(p1),
        arrowstyle=style,
        mutation_scale=ms,
        color=color,
        lw=lw,
        zorder=z,
        linestyle=ls,
        shrinkA=shrink,
        shrinkB=shrink,
    )
    ax.add_patch(a)
    return a


def clean_axes(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def label_box(ax, x, y, s, color=TEXT, fc="white", ec=GREY_LINE, fs=9.5, ha="center", va="center", z=9):
    ax.text(
        x,
        y,
        s,
        color=color,
        fontsize=fs,
        ha=ha,
        va=va,
        zorder=z,
        bbox=dict(boxstyle="round,pad=0.24", fc=fc, ec=ec, lw=0.8),
    )


def white_pad(alpha=0.92, pad=0.10):
    return dict(boxstyle=f"round,pad={pad}", fc="white", ec="none", alpha=alpha)


def frame_panel(ax, xlim, ylim):
    """Set equal-aspect limits, hide ticks/spines, and draw light axes + panel border."""
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.add_patch(
        Rectangle(
            (xlim[0], ylim[0]),
            xlim[1] - xlim[0],
            ylim[1] - ylim[0],
            fc="white",
            ec=GREY_LINE,
            lw=0.9,
            zorder=0,
        )
    )
    ax.axhline(0, color=GREY_LINE, lw=0.75, zorder=1)
    ax.axvline(0, color=GREY_LINE, lw=0.75, zorder=1)


def right_angle_mark(ax, vertex, dir1, dir2, size=0.22, color=SLATE, lw=1.0, z=4, alpha=1.0):
    """Draw an exact orthogonal right-angle corner at vertex spanned by dir1 and dir2."""
    v = np.asarray(vertex, dtype=float)
    u1 = np.asarray(dir1, dtype=float)
    u2 = np.asarray(dir2, dtype=float)
    n1 = float(np.linalg.norm(u1))
    n2 = float(np.linalg.norm(u2))
    if n1 <= 1e-12 or n2 <= 1e-12:
        raise AssertionError("Zero-length direction vector in right_angle_mark")
    u1 = u1 / n1
    u2 = u2 / n2
    if abs(float(np.dot(u1, u2))) > 1e-9:
        raise AssertionError(f"Non-orthogonal directions in right_angle_mark: dot={np.dot(u1, u2)}")
    p1 = v + size * u1
    p12 = v + size * (u1 + u2)
    p2 = v + size * u2
    ax.plot([p1[0], p12[0], p2[0]], [p1[1], p12[1], p2[1]], color=color, lw=lw, zorder=z, alpha=alpha)


def curved_node_arrow(
    ax,
    p0,
    p1,
    r_node: float,
    rad: float = 0.0,
    color=NAVY,
    lw: float = 1.8,
    ms: float = 13,
    z: int = 4,
    ls="-",
    alpha: float = 1.0,
):
    """Draw a straight or quadratic-Bezier arrow clipped in data coordinates to node circles."""
    p0 = np.asarray(p0, dtype=float)
    p1 = np.asarray(p1, dtype=float)
    dp = p1 - p0
    dist = float(np.linalg.norm(dp))
    if dist <= 2.0 * r_node:
        raise AssertionError("Nodes overlap or touch; cannot clip edge outside node circles")

    if abs(rad) < 1e-12:
        u = dp / dist
        q0 = p0 + r_node * u
        q1 = p1 - r_node * u
        patch = FancyArrowPatch(
            tuple(q0),
            tuple(q1),
            arrowstyle="-|>",
            mutation_scale=ms,
            color=color,
            lw=lw,
            zorder=z,
            linestyle=ls,
            alpha=alpha,
            shrinkA=0.0,
            shrinkB=0.0,
        )
        ax.add_patch(patch)
        mid = 0.5 * (q0 + q1)
        return patch, mid

    # Quadratic Bezier B(t) = (1-t)^2 p0 + 2(1-t)t ctrl + t^2 p1
    # Right-hand perpendicular to dp flips naturally when p0 and p1 are swapped.
    perp = np.array([dp[1], -dp[0]], dtype=float)
    ctrl = 0.5 * (p0 + p1) + rad * perp

    def bezier(t: float) -> np.ndarray:
        return ((1.0 - t) ** 2) * p0 + 2.0 * (1.0 - t) * t * ctrl + (t ** 2) * p1

    # Bisection for exact circle exits t0 near 0 and t1 near 1
    mid_pt = bezier(0.5)
    if np.linalg.norm(mid_pt - p0) <= r_node or np.linalg.norm(mid_pt - p1) <= r_node:
        raise AssertionError("Bezier midpoint lies inside node circle; reduce curvature or r_node")
    lo, hi = 0.0, 0.5
    for _ in range(60):
        mid_t = 0.5 * (lo + hi)
        if np.linalg.norm(bezier(mid_t) - p0) < r_node:
            lo = mid_t
        else:
            hi = mid_t
    t0 = 0.5 * (lo + hi)

    lo, hi = 0.5, 1.0
    for _ in range(60):
        mid_t = 0.5 * (lo + hi)
        if np.linalg.norm(bezier(mid_t) - p1) < r_node:
            hi = mid_t
        else:
            lo = mid_t
    t1 = 0.5 * (lo + hi)

    # Exact De Casteljau subdivision onto [t0, t1]
    q0 = bezier(t0)
    q1 = bezier(t1)
    # Derivative B'(t) = 2[(1-t)(ctrl - p0) + t(p1 - ctrl)]; sub-curve control point meets tangents:
    # For quadratic Bezier, blossom B(t0, t1) = (1-t0)[(1-t1)p0 + t1 ctrl] + t0[(1-t1)ctrl + t1 p1]
    q_ctrl = (1.0 - t0) * ((1.0 - t1) * p0 + t1 * ctrl) + t0 * ((1.0 - t1) * ctrl + t1 * p1)

    assert abs(np.linalg.norm(q0 - p0) - r_node) < 1e-9
    assert abs(np.linalg.norm(q1 - p1) - r_node) < 1e-9

    bpath = MplPath([tuple(q0), tuple(q_ctrl), tuple(q1)], [MplPath.MOVETO, MplPath.CURVE3, MplPath.CURVE3])
    patch = FancyArrowPatch(
        path=bpath,
        arrowstyle="-|>",
        mutation_scale=ms,
        color=color,
        lw=lw,
        zorder=z,
        linestyle=ls,
        alpha=alpha,
        shrinkA=0.0,
        shrinkB=0.0,
    )
    ax.add_patch(patch)
    mid = 0.25 * q0 + 0.5 * q_ctrl + 0.25 * q1
    return patch, mid


# ---------------------------------------------------------------------------
# Figure 5: projection, the Householder reflection, and an oblique projection
# ---------------------------------------------------------------------------
def fig_projection_reflection(out_dir: Path) -> None:
    print("F1 maths0_projection_reflection.png")

    # ---- Panel (a) math checks ----
    u_a = np.array([1.0, 2.0]) / math.sqrt(5.0)
    mirror_dir_a = np.array([2.0, -1.0])
    x_a = np.array([3.0, 1.0])
    P_u = np.outer(u_a, u_a)
    I2 = np.eye(2)
    H_u_a = I2 - 2.0 * P_u
    pu_x = P_u @ x_a
    proj_perp_x = (I2 - P_u) @ x_a
    refl_x = H_u_a @ x_a
    norm_xa = float(np.linalg.norm(x_a))

    assert np.allclose(np.linalg.norm(u_a), 1.0)
    assert abs(float(u_a @ mirror_dir_a)) < 1e-12
    assert np.allclose(pu_x, [1.0, 2.0])
    assert np.allclose(proj_perp_x, [2.0, -1.0])
    assert np.allclose(refl_x, [1.0, -3.0])
    assert abs(norm_xa - math.sqrt(10.0)) < 1e-12
    assert abs(float(np.linalg.norm(refl_x)) - norm_xa) < 1e-12

    print("  Panel (a): From projection to reflection")
    print(f"    u = (1, 2)/sqrt(5) = ({u_a[0]:.6f}, {u_a[1]:.6f}), ||u||_2 = {np.linalg.norm(u_a):g}")
    print(f"    mirror u^perp direction = ({mirror_dir_a[0]:g}, {mirror_dir_a[1]:g}), angle(u, u^perp) = 90 deg")
    print(f"    x = ({x_a[0]:g}, {x_a[1]:g}), ||x||_2 = sqrt(10) = {norm_xa:.6f}")
    print(f"    P_u x = ({pu_x[0]:g}, {pu_x[1]:g})")
    print(f"    1 step of -P_u x: (I - P_u)x = ({proj_perp_x[0]:g}, {proj_perp_x[1]:g})")
    print(f"    2 steps of -P_u x: H_u x = (I - 2 P_u)x = ({refl_x[0]:g}, {refl_x[1]:g}), ||H_u x||_2 = sqrt(10) = {np.linalg.norm(refl_x):.6f}")

    # ---- Panel (b) math checks ----
    x_b = np.array([3.0, 4.0])
    e1 = np.array([1.0, 0.0])
    norm_xb = float(np.linalg.norm(x_b))
    target_pos = norm_xb * e1
    target_neg = -norm_xb * e1
    u_b = x_b - target_pos
    u_b_prime = x_b + target_pos
    H_ub = I2 - 2.0 * np.outer(u_b, u_b) / float(u_b @ u_b)
    H_ub_prime = I2 - 2.0 * np.outer(u_b_prime, u_b_prime) / float(u_b_prime @ u_b_prime)
    mid_b = 0.5 * (x_b + target_pos)
    mid_b_prime = 0.5 * (x_b + target_neg)
    mirror_b = np.array([2.0, 1.0])
    mirror_b_prime = np.array([-1.0, 2.0])

    assert abs(norm_xb - 5.0) < 1e-12
    assert np.allclose(u_b, [-2.0, 4.0])
    assert np.allclose(u_b_prime, [8.0, 4.0])
    assert np.allclose(H_ub @ x_b, target_pos)
    assert np.allclose(H_ub_prime @ x_b, target_neg)
    assert np.allclose(mid_b, [4.0, 2.0])
    assert np.allclose(mid_b_prime, [-1.0, 2.0])
    assert abs(float(mirror_b @ u_b)) < 1e-12
    assert abs(float(mirror_b_prime @ u_b_prime)) < 1e-12
    assert abs(float(mirror_b @ mirror_b_prime)) < 1e-12

    def fmt_vec(v: np.ndarray) -> str:
        c0 = 0.0 if abs(float(v[0])) < 1e-12 else float(v[0])
        c1 = 0.0 if abs(float(v[1])) < 1e-12 else float(v[1])
        return f"({c0:g}, {c1:g})"

    print("  Panel (b): Householder sends x to ||x|| e_1")
    print(f"    x = ({x_b[0]:g}, {x_b[1]:g}), ||x||_2 = {norm_xb:g}, 5 e_1 = ({target_pos[0]:g}, {target_pos[1]:g})")
    print(f"    u = x - 5 e_1 = ({u_b[0]:g}, {u_b[1]:g}), mirror u^perp direction = ({mirror_b[0]:g}, {mirror_b[1]:g}), midpoint = ({mid_b[0]:g}, {mid_b[1]:g})")
    print(f"    H_u x = {fmt_vec(H_ub @ x_b)}")
    print(f"    u' = x + 5 e_1 = ({u_b_prime[0]:g}, {u_b_prime[1]:g}), mirror u'^perp direction = ({mirror_b_prime[0]:g}, {mirror_b_prime[1]:g}), midpoint = ({mid_b_prime[0]:g}, {mid_b_prime[1]:g}), angle(u^perp, u'^perp) = 90 deg")
    print(f"    H_{{u'}} x = -5 e_1 = {fmt_vec(H_ub_prime @ x_b)}")

    # ---- Panel (c) math checks ----
    P_ob = np.array([[1.0, 1.0], [0.0, 0.0]])
    assert np.allclose(P_ob @ P_ob, P_ob)
    x_c = np.array([1.0, 1.0]) / math.sqrt(2.0)
    px_c = P_ob @ x_c
    ipx_c = (I2 - P_ob) @ x_c
    orth_c = np.array([x_c[0], 0.0])
    norm_P_ob = float(np.linalg.norm(P_ob, 2))
    cos_pieces = float(px_c @ ipx_c) / (float(np.linalg.norm(px_c)) * float(np.linalg.norm(ipx_c)))
    ang_pieces_deg = math.degrees(math.acos(np.clip(cos_pieces, -1.0, 1.0)))
    ang_subspaces_deg = 45.0

    assert np.allclose(px_c, [math.sqrt(2.0), 0.0])
    assert np.allclose(ipx_c, [-1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)])
    assert abs(norm_P_ob - math.sqrt(2.0)) < 1e-12
    assert abs(norm_P_ob - 1.0 / math.sin(math.radians(ang_subspaces_deg))) < 1e-12
    assert abs(ang_pieces_deg - 135.0) < 1e-12

    print("  Panel (c): Oblique contrast")
    print("    P = [[1, 1], [0, 0]], P^2 = P, range = x-axis (y = 0), null space = line y = -x")
    print(f"    angle between range and null space = {ang_subspaces_deg:g} deg")
    print(f"    x = (1/sqrt(2), 1/sqrt(2)) = ({x_c[0]:.6f}, {x_c[1]:.6f}), ||x||_2 = {np.linalg.norm(x_c):g}")
    print(f"    P x = (sqrt(2), 0) = ({px_c[0]:.6f}, {px_c[1]:g})")
    print(f"    (I - P)x = (-1/sqrt(2), 1/sqrt(2)) = ({ipx_c[0]:.6f}, {ipx_c[1]:.6f})")
    print(f"    angle between P x and (I - P)x = {ang_pieces_deg:g} deg")
    print(f"    orthogonal projection of x onto x-axis = (1/sqrt(2), 0) = ({orth_c[0]:.6f}, 0)")
    print(f"    ||P||_2 = sqrt(2) = 1/sin(45 deg) = {norm_P_ob:.6f}")

    # Common height/width ratio = 6/7 across all three panels so panel boxes match exactly
    fig, axes = plt.subplots(1, 3, figsize=(10.85, 4.05))

    # ---------------- Panel (a) ----------------
    ax = axes[0]
    xlim_a = (-2.85, 5.69)    # span 8.54
    ylim_a = (-4.25, 3.07)    # span 7.32 -> 7.32 / 8.54 = 6/7
    frame_panel(ax, xlim_a, ylim_a)

    # Dotted projection guide from x to P_u x
    ax.plot([x_a[0], pu_x[0]], [x_a[1], pu_x[1]], color=TEAL, lw=0.9, ls=":", alpha=0.75, zorder=2)

    # Mirror u^perp: direction (2, -1)
    ax.plot([-2.65, 4.80], [1.325, -2.40], color=SLATE, lw=2.0, zorder=3)
    ax.text(-1.50, 1.25, r"mirror $\mathbf{u}^\perp$", color=SLATE, fontsize=9.8, ha="center", va="bottom",
            zorder=8, bbox=white_pad(pad=0.06))

    # Dashed arc of radius ||x|| = sqrt(10) through x and H_u x
    th_arc = np.linspace(math.radians(-82.0), math.radians(28.0), 240)
    ax.plot(norm_xa * np.cos(th_arc), norm_xa * np.sin(th_arc), color=SLATE, lw=1.25, ls=(0, (4, 3)), zorder=2)
    ax.text(3.26, 0.22, r"$\|\mathbf{x}\| = \sqrt{10}$", color=SLATE, fontsize=9.5, ha="left", va="center",
            zorder=8, bbox=white_pad(pad=0.06))

    # Right angle at (I - P_u)x = (2, -1)
    right_angle_mark(ax, proj_perp_x, (-2.0, 1.0), (1.0, 2.0), size=0.28, color=SLATE, lw=1.1, z=4)

    # Vectors from origin: P_u x, u, x, (I - P_u)x, H_u x
    arrow(ax, (0, 0), pu_x, color=TEAL, lw=2.0, ms=13, z=5)
    arrow(ax, (0, 0), u_a, color=NAVY, lw=2.5, ms=12, z=7)
    arrow(ax, (0, 0), x_a, color=NAVY, lw=2.2, ms=14, z=6)
    arrow(ax, (0, 0), proj_perp_x, color=BLUE, lw=1.9, ms=12, z=5)
    arrow(ax, (0, 0), refl_x, color=BLUE, lw=2.2, ms=14, z=6)

    # Two equal steps of -P_u x in one colour
    arrow(ax, x_a, proj_perp_x, color=RED, lw=2.0, ms=13, z=6, shrink=2.0)
    arrow(ax, proj_perp_x, refl_x, color=RED, lw=2.0, ms=13, z=6, shrink=2.0)
    ax.text(2.34, 0.14, r"$-P_{\mathbf{u}}\mathbf{x}$", color=RED, fontsize=9.6, ha="right", va="center",
            zorder=8, bbox=white_pad(pad=0.05))
    ax.plot([1.52, 2.08], [-1.96, -2.35], color=RED, lw=0.85, zorder=7)
    ax.text(2.14, -2.42, r"$-P_{\mathbf{u}}\mathbf{x}$", color=RED, fontsize=9.6, ha="left", va="center",
            zorder=8, bbox=white_pad(pad=0.05))

    for pt, col in (((0, 0), TEXT), (pu_x, TEAL), (x_a, NAVY), (proj_perp_x, BLUE), (refl_x, BLUE)):
        ax.plot([pt[0]], [pt[1]], "o", color=col, ms=4.0, zorder=8)

    # Labels for u, P_u x, x, (I - P_u)x, H_u x
    ax.plot([-0.22, 0.25], [0.58, 0.50], color=NAVY, lw=0.8, zorder=7)
    ax.text(-0.26, 0.58, r"$\mathbf{u}$", color=NAVY, fontsize=10.5, ha="right", va="center", zorder=8, bbox=white_pad())
    ax.text(1.02, 2.12, r"$P_{\mathbf{u}}\mathbf{x} = (1, 2)$", color=TEAL, fontsize=9.6, ha="center", va="bottom",
            zorder=8, bbox=white_pad(pad=0.06))
    ax.text(3.05, 1.14, r"$\mathbf{x} = (3, 1)$", color=NAVY, fontsize=9.6, ha="left", va="bottom",
            zorder=8, bbox=white_pad(pad=0.06))
    ax.plot([2.52, 2.10], [-0.76, -0.96], color=BLUE, lw=0.8, zorder=7)
    ax.text(2.56, -0.72, r"$(I - P_{\mathbf{u}}\,)\mathbf{x} = (2, -1)$", color=BLUE, fontsize=9.2, ha="left", va="center",
            zorder=8, bbox=white_pad(pad=0.06))
    ax.text(1.08, -3.22, r"$H_{\mathbf{u}}\mathbf{x} = (1, -3)$", color=BLUE, fontsize=9.6, ha="center", va="top",
            zorder=8, bbox=white_pad(pad=0.06))

    # Required summary labels in empty Quadrant III
    label_box(
        ax,
        -1.38,
        -1.15,
        "subtract $P_{\\mathbf{u}}\\mathbf{x}$ once:\nprojection onto $\\mathbf{u}^\\perp$",
        color=BLUE,
        fs=9.1,
    )
    label_box(
        ax,
        -1.38,
        -2.62,
        "subtract it twice:\nreflection $H_{\\mathbf{u}}\\mathbf{x}$",
        color=RED,
        fs=9.1,
    )
    ax.set_title("(a) From projection to reflection", fontweight="bold", color=TEXT, pad=8)

    # ---------------- Panel (b) ----------------
    ax = axes[1]
    xlim_b = (-6.85, 6.80)    # span 13.65
    ylim_b = (-3.75, 7.95)    # span 11.70 -> 11.70 / 13.65 = 6/7
    frame_panel(ax, xlim_b, ylim_b)

    # Arc of radius 5 through 5e_1, x, and -5e_1
    th_b = np.linspace(math.radians(-10.0), math.radians(190.0), 260)
    ax.plot(5.0 * np.cos(th_b), 5.0 * np.sin(th_b), color=SLATE, lw=1.2, ls=(0, (4, 3)), zorder=2)
    ax.text(0.25, 5.18, r"$\|\mathbf{x}\| = 5$", color=SLATE, fontsize=9.5, ha="left", va="bottom",
            zorder=8, bbox=white_pad(pad=0.06))

    # Second option (lighter dashed): mirror u'^perp, target -5e_1, and u' = x + 5e_1
    ax.plot([1.55, -3.20], [-3.10, 6.40], color=AMBER, lw=1.5, ls=(0, (5, 3)), alpha=0.85, zorder=3)
    ax.text(-3.22, 6.50, r"mirror ${\mathbf{u}'}^\perp$", color=AMBER, fontsize=9.5, ha="center", va="bottom",
            zorder=8, bbox=white_pad(pad=0.06))
    arrow(ax, (0, 0), target_neg, color=AMBER, lw=1.7, ms=12, z=4, ls=(0, (4, 3)))
    arrow(ax, target_neg, x_b, color=AMBER, lw=1.6, ms=12, z=4, ls=(0, (5, 3)), shrink=3.0)
    right_angle_mark(ax, mid_b_prime, (1.0, -2.0), (-8.0, -4.0), size=0.45, color=AMBER, lw=1.0, z=4, alpha=0.85)
    ax.plot([mid_b_prime[0]], [mid_b_prime[1]], "o", color=AMBER, ms=3.8, zorder=7)
    ax.plot([target_neg[0]], [target_neg[1]], "o", color=AMBER, ms=4.2, zorder=7)
    ax.text(-4.95, -0.45, r"$-5\mathbf{e}_1$", color=AMBER, fontsize=9.8, ha="center", va="top", zorder=8, bbox=white_pad(pad=0.06))
    ax.plot([-4.45, -2.65], [4.15, 1.25], color=AMBER, lw=0.85, zorder=7)
    ax.text(-6.55, 4.55, r"$\mathbf{u}' = \mathbf{x} + 5\mathbf{e}_1$", color=AMBER, fontsize=9.4, ha="left", va="center",
            zorder=8, bbox=white_pad(pad=0.06))

    # First option (solid): mirror u^perp, x, 5e_1, and u = x - 5e_1 with midpoint (4, 2)
    ax.plot([-5.80, 6.30], [-2.90, 3.15], color=TEAL, lw=2.1, zorder=4)
    ax.text(-2.95, -2.42, r"mirror $\mathbf{u}^\perp$", color=TEAL, fontsize=9.8, ha="center", va="top",
            zorder=8, bbox=white_pad(pad=0.06))
    right_angle_mark(ax, mid_b, (-2.0, -1.0), (-2.0, 4.0), size=0.45, color=TEAL, lw=1.1, z=5)

    arrow(ax, (0, 0), x_b, color=NAVY, lw=2.3, ms=14, z=6)
    arrow(ax, (0, 0), target_pos, color=BLUE, lw=2.3, ms=14, z=6)
    arrow(ax, target_pos, x_b, color=RED, lw=2.0, ms=13, z=6, shrink=3.0)

    for pt, col in (((0, 0), TEXT), (x_b, NAVY), (target_pos, BLUE), (mid_b, TEAL)):
        ax.plot([pt[0]], [pt[1]], "o", color=col, ms=4.3, zorder=8)

    ax.text(3.15, 4.28, r"$\mathbf{x} = (3, 4)$", color=NAVY, fontsize=9.8, ha="left", va="bottom",
            zorder=8, bbox=white_pad(pad=0.06))
    ax.text(4.95, -0.45, r"$5\mathbf{e}_1 = (5, 0)$", color=BLUE, fontsize=9.8, ha="center", va="top",
            zorder=8, bbox=white_pad(pad=0.06))
    ax.plot([4.35, 3.65], [3.48, 2.70], color=RED, lw=0.85, zorder=7)
    ax.text(3.85, 3.55, r"$\mathbf{u} = \mathbf{x} - 5\mathbf{e}_1$", color=RED, fontsize=9.5, ha="left", va="bottom",
            zorder=8, bbox=white_pad(pad=0.06))
    ax.plot([3.58, 3.92], [1.46, 1.92], color=TEAL, lw=0.8, zorder=7)
    ax.text(3.55, 1.42, r"$(4, 2)$", color=TEAL, fontsize=9.2, ha="right", va="top",
            zorder=8, bbox=white_pad(pad=0.05))

    ax.set_title(r"(b) Householder sends $\mathbf{x}$ to $\|\mathbf{x}\|\mathbf{e}_1$", fontweight="bold", color=TEXT, pad=8)

    # ---------------- Panel (c) ----------------
    ax = axes[2]
    xlim_c = (-1.72, 2.34)    # span 4.06
    ylim_c = (-1.60, 1.88)    # span 3.48 -> 3.48 / 4.06 = 6/7
    frame_panel(ax, xlim_c, ylim_c)

    # Unit circle
    ax.add_patch(Circle((0, 0), 1.0, fc="none", ec=SLATE, lw=1.2, ls=(0, (4, 3)), zorder=2))
    ax.text(-0.82, -0.85, "unit circle", color=SLATE, fontsize=9.3, ha="right", va="top",
            zorder=8, bbox=white_pad(pad=0.06))

    # Range (x-axis) and null space (y = -x)
    ax.plot([-1.62, 2.20], [0, 0], color=TEAL, lw=2.0, zorder=3)
    ax.plot([-1.50, 1.28], [1.50, -1.28], color=AMBER, lw=1.9, zorder=3)
    ax.text(-1.58, -0.10, "range", color=TEAL, fontsize=9.8, ha="left", va="top", zorder=8, bbox=white_pad(pad=0.06))
    ax.text(-1.56, 1.54, "null space", color=AMBER, fontsize=9.8, ha="left", va="bottom", zorder=8, bbox=white_pad(pad=0.06))

    # 45 deg angle between range and null space (in Q2 between 135 deg and 180 deg)
    ax.add_patch(Arc((0, 0), 0.88, 0.88, theta1=135.0, theta2=180.0, color=SLATE, lw=1.2, zorder=4))
    ax.text(-0.52, 0.22, r"$45^\circ$", color=SLATE, fontsize=9.5, ha="right", va="center",
            zorder=8, bbox=white_pad(pad=0.05))

    # 135 deg angle between Px (0 deg) and (I - P)x (135 deg)
    ax.add_patch(Arc((0, 0), 0.50, 0.50, theta1=0.0, theta2=135.0, color=SLATE, lw=1.0, zorder=4))
    ax.text(0.0, 0.31, r"$135^\circ$", color=SLATE, fontsize=9.2, ha="center", va="bottom",
            zorder=8, bbox=white_pad(pad=0.05))

    # Faint orthogonal projection of x onto the x-axis with right angle
    ax.plot([x_c[0], orth_c[0]], [x_c[1], 0.0], color=SLATE, lw=1.1, ls=":", alpha=0.85, zorder=3)
    right_angle_mark(ax, orth_c, (-1.0, 0.0), (0.0, 1.0), size=0.11, color=SLATE, lw=0.95, z=4, alpha=0.85)
    ax.plot([orth_c[0]], [0.0], "o", color=SLATE, ms=3.8, zorder=7)
    ax.text(orth_c[0] + 0.07, -0.12, r"$(1/\sqrt{2}, 0)$", color=SLATE, fontsize=9.2, ha="center", va="top",
            zorder=8, bbox=white_pad(pad=0.05))

    # Oblique projection dashed guide from x along null space to Px
    ax.plot([x_c[0], px_c[0]], [x_c[1], px_c[1]], color=RED, lw=1.3, ls=(0, (4, 2.5)), zorder=4)

    # Vectors x, Px, (I - P)x
    arrow(ax, (0, 0), x_c, color=NAVY, lw=2.3, ms=14, z=6)
    arrow(ax, (0, 0), px_c, color=RED, lw=2.4, ms=14, z=6)
    arrow(ax, (0, 0), ipx_c, color=AMBER, lw=2.3, ms=14, z=6)

    for pt, col in (((0, 0), TEXT), (x_c, NAVY), (px_c, RED), (ipx_c, AMBER)):
        ax.plot([pt[0]], [pt[1]], "o", color=col, ms=4.2, zorder=8)

    ax.text(x_c[0] + 0.04, x_c[1] + 0.08, r"$\mathbf{x} = (\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$", color=NAVY,
            fontsize=9.6, ha="left", va="bottom", zorder=8, bbox=white_pad(pad=0.06))
    ax.plot([px_c[0] + 0.02, 1.48], [0.05, 0.25], color=RED, lw=0.85, zorder=7)
    ax.text(1.16, 0.29, r"$P\mathbf{x} = (\sqrt{2}, 0)$", color=RED, fontsize=9.5, ha="left", va="bottom",
            zorder=8, bbox=white_pad(pad=0.05))
    ax.text(ipx_c[0] - 0.07, ipx_c[1] + 0.02, r"$(I - P\,)\mathbf{x}$", color=AMBER, fontsize=9.6, ha="right",
            va="bottom", zorder=8, bbox=white_pad(pad=0.06))

    label_box(ax, 0.22, -1.25, r"$\|P\|_2 = \sqrt{2} = 1/\sin 45^\circ$", color=RED, fs=9.5)
    ax.set_title("(c) Oblique contrast", fontweight="bold", color=TEXT, pad=8)

    fig.tight_layout(w_pad=1.0)
    save_fig(fig, out_dir, "maths0_projection_reflection.png")


# ---------------------------------------------------------------------------
# Figure 2: the airline network
# ---------------------------------------------------------------------------
def fig_airline_network(out_dir: Path) -> None:
    print("\nF2 maths0_airline_network.png")

    cities = ["A", "B", "C", "D", "H"]
    C = np.array([
        [0, 0, 1, 0, 1],  # A
        [1, 0, 0, 0, 1],  # B
        [0, 0, 0, 1, 1],  # C
        [0, 1, 0, 0, 1],  # D
        [1, 1, 1, 1, 0],  # H
    ], dtype=int)

    # Build directed edges from C and verify against specification
    edges = [(cities[i], cities[j]) for i in range(5) for j in range(5) if C[i, j] == 1]
    expected_outer = {("B", "A"), ("A", "C"), ("C", "D"), ("D", "B")}
    expected_hub = {("H", x) for x in "ABCD"} | {(x, "H") for x in "ABCD"}
    assert set(edges) == expected_outer | expected_hub
    assert len(edges) == 12

    print("  Adjacency matrix C (5x5, rows = from, cols = to, order A, B, C, D, H):")
    for idx, name in enumerate(cities):
        row_str = " ".join(str(v) for v in C[idx])
        print(f"    {name}: {row_str}")
    print(
        f"  {len(edges)} directed edges built from C "
        f"({len(expected_outer)} outer one-way, {len(expected_hub)} hub links = 4 two-way pairs): "
        f"{', '.join(f'{u}->{v}' for u, v in edges)}"
    )

    C2 = C @ C
    C3 = C2 @ C
    C4 = C3 @ C
    C_le4 = C + C2 + C3 + C4
    walks_4_AB = []
    for k1 in range(5):
        if C[0, k1]:
            for k2 in range(5):
                if C[k1, k2]:
                    for k3 in range(5):
                        if C[k2, k3] and C[k3, 1]:
                            walks_4_AB.append(("A", cities[k1], cities[k2], cities[k3], "B"))

    assert int(C4[0, 1]) == 7
    assert len(walks_4_AB) == 7
    assert int(C_le4[0, 1]) == 11

    walk_simple = ("A", "C", "D", "H", "B")
    walk_revisit = ("A", "H", "A", "H", "B")
    assert walk_simple in walks_4_AB
    assert walk_revisit in walks_4_AB

    print(f"  [C]_AB = {C[0, 1]}, [C^2]_AB = {C2[0, 1]}, [C^3]_AB = {C3[0, 1]}, [C^4]_AB = {C4[0, 1]}")
    print(f"  [C + C^2 + C^3 + C^4]_AB = {C_le4[0, 1]} (at most 4 flights from A to B)")
    print("  All 7 directed 4-flight walks from A to B:")
    for idx, w in enumerate(walks_4_AB, start=1):
        print(f"    {idx}. {' -> '.join(w)}")

    pos = {
        "A": np.array([-1.35, 1.35]),
        "B": np.array([1.35, 1.35]),
        "C": np.array([-1.35, -1.35]),
        "D": np.array([1.35, -1.35]),
        "H": np.array([0.0, 0.0]),
    }
    r_node = 0.24

    def draw_nodes(ax, faint: bool = False):
        for name, p in pos.items():
            is_hub = name == "H"
            if faint:
                fc = AMBER_LIGHT if is_hub else GREY_BG
                ec = AMBER if is_hub else SLATE
                lw = 1.6 if is_hub else 1.4
            else:
                fc = AMBER_LIGHT if is_hub else BLUE_PALE
                ec = AMBER if is_hub else NAVY
                lw = 2.0 if is_hub else 1.8
            ax.add_patch(Circle(tuple(p), r_node, fc=fc, ec=ec, lw=lw, zorder=6))
            ax.text(p[0], p[1], name, color=TEXT if is_hub else NAVY, fontsize=12.0, fontweight="bold",
                    ha="center", va="center", zorder=7)

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.95))
    xlim = (-1.95, 1.95)
    ylim = (-2.55, 1.80)

    for ax in axes:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_aspect("equal")
        clean_axes(ax)
        ax.add_patch(
            Rectangle(
                (xlim[0], ylim[0]),
                xlim[1] - xlim[0],
                ylim[1] - ylim[0],
                fc="white",
                ec=GREY_LINE,
                lw=0.9,
                zorder=0,
            )
        )

    # ---------------- Panel (a): The network ----------------
    ax = axes[0]
    for i in range(5):
        for j in range(5):
            if C[i, j] == 1:
                two_way = C[j, i] == 1
                rad = 0.18 if two_way else 0.0
                col = TEAL if two_way else NAVY
                lw = 1.85 if two_way else 2.1
                curved_node_arrow(ax, pos[cities[i]], pos[cities[j]], r_node, rad=rad, color=col, lw=lw, ms=14, z=4)

    draw_nodes(ax, faint=False)
    label_box(
        ax,
        0.0,
        -2.08,
        "outer cycle (navy): 4 one-way flights\nhub H links (teal): 4 two-way pairs (12 arcs total)",
        color=TEXT,
        fs=9.3,
    )
    ax.set_title("(a) The network", fontweight="bold", color=TEXT, pad=8)

    # ---------------- Panel (b): Two of the seven 4-flight walks ----------------
    ax = axes[1]
    # Faint background network built from C
    for i in range(5):
        for j in range(5):
            if C[i, j] == 1:
                two_way = C[j, i] == 1
                rad = 0.18 if two_way else 0.0
                curved_node_arrow(
                    ax,
                    pos[cities[i]],
                    pos[cities[j]],
                    r_node,
                    rad=rad,
                    color=GREY_LINE,
                    lw=1.25,
                    ms=11,
                    z=2,
                )

    draw_nodes(ax, faint=True)

    def step_badge(ax_, x_, y_, s_, col_):
        ax_.text(
            x_,
            y_,
            s_,
            color=col_,
            fontsize=9.4,
            fontweight="bold",
            ha="center",
            va="center",
            zorder=9,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec=col_, lw=1.0),
        )

    # Walk 1 (TEAL): A -> C -> D -> H -> B
    _, m1 = curved_node_arrow(ax, pos["A"], pos["C"], r_node, rad=0.0, color=TEAL, lw=2.5, ms=15, z=5)
    _, m2 = curved_node_arrow(ax, pos["C"], pos["D"], r_node, rad=0.0, color=TEAL, lw=2.5, ms=15, z=5)
    _, m3 = curved_node_arrow(ax, pos["D"], pos["H"], r_node, rad=0.18, color=TEAL, lw=2.5, ms=15, z=5)
    # H -> B is shared as step 4 of both walks; draw closely paired teal/red lanes on the H->B side
    _, m4_t = curved_node_arrow(ax, pos["H"], pos["B"], r_node, rad=0.12, color=TEAL, lw=2.4, ms=14, z=5)

    step_badge(ax, m1[0] - 0.24, m1[1], "1", TEAL)
    step_badge(ax, m2[0], m2[1] - 0.24, "2", TEAL)
    step_badge(ax, m3[0] + 0.22, m3[1] + 0.16, "3", TEAL)
    ax.plot([0.36, m4_t[0] - 0.02], [0.89, m4_t[1] + 0.02], color=TEAL, lw=0.9, zorder=7)
    step_badge(ax, 0.26, 0.99, "4", TEAL)

    # Walk 2 (RED): A -> H -> A -> H -> B (A->H used on steps 1 and 3)
    _, m13_r = curved_node_arrow(ax, pos["A"], pos["H"], r_node, rad=0.18, color=RED, lw=2.5, ms=15, z=5)
    _, m2_r = curved_node_arrow(ax, pos["H"], pos["A"], r_node, rad=0.18, color=RED, lw=2.5, ms=15, z=5)
    _, m4_r = curved_node_arrow(ax, pos["H"], pos["B"], r_node, rad=0.25, color=RED, lw=2.4, ms=14, z=5)

    # Note: A->H bends down-left (m13_r), while H->A bends up-right (m2_r)
    step_badge(ax, m13_r[0] - 0.30, m13_r[1] - 0.18, "1, 3", RED)
    step_badge(ax, m2_r[0] + 0.22, m2_r[1] + 0.18, "2", RED)
    step_badge(ax, m4_r[0] + 0.24, m4_r[1] - 0.15, "4", RED)

    # Legend box naming both walks
    ax.add_patch(Rectangle((-1.83, -2.44), 3.66, 0.72, fc="white", ec=GREY_LINE, lw=0.85, zorder=8))
    ax.plot([-1.72, -1.42], [-1.92, -1.92], color=TEAL, lw=2.5, zorder=9)
    ax.text(-1.33, -1.92, r"$A \to C \to D \to H \to B$ (visits no city twice)", color=TEAL,
            fontsize=9.3, ha="left", va="center", zorder=9)
    ax.plot([-1.72, -1.42], [-2.24, -2.24], color=RED, lw=2.5, zorder=9)
    ax.text(-1.33, -2.24, r"$A \to H \to A \to H \to B$ (revisits A and H)", color=RED,
            fontsize=9.3, ha="left", va="center", zorder=9)

    ax.set_title(r"(b) Two of the $[C^4]_{AB} = 7$ four-flight walks $A \to B$", fontweight="bold", color=TEXT, pad=8)

    fig.tight_layout(w_pad=1.3)
    save_fig(fig, out_dir, "maths0_airline_network.png")


# ---------------------------------------------------------------------------
# Figure 1: unit balls of the 1-, 2- and infinity-norms
# ---------------------------------------------------------------------------
def fig_unit_balls(out_dir: Path) -> None:
    print("\nF3 maths0_unit_balls.png")

    v_mark = np.array([0.5, 0.5])
    n1 = float(np.linalg.norm(v_mark, 1))
    n2 = float(np.linalg.norm(v_mark, 2))
    ninf = float(np.linalg.norm(v_mark, np.inf))
    assert abs(n1 - 1.0) < 1e-12
    assert abs(n2 - 1.0 / math.sqrt(2.0)) < 1e-12
    assert abs(ninf - 0.5) < 1e-12
    assert n1 >= n2 >= ninf

    print("  Panel (a): 2D unit balls of the 1-, 2-, and infinity-norms")
    print("    touch points of all three unit balls: +/-e_1 = (+/-1, 0), +/-e_2 = (0, +/-1)")
    print(
        f"    marked point v = (1/2, 1/2): ||v||_1 = {n1:g}, "
        f"||v||_2 = 1/sqrt(2) = {n2:.6f} (approx {n2:.3f}), ||v||_inf = {ninf:g}"
    )
    print("  Panel (b): Equivalence of 1-norm and infinity-norm in R^2")
    print("    inner infinity-ball radius = 1/2, touching |x| + |y| = 1 at (+/-1/2, +/-1/2)")
    print("    outer infinity-ball radius = 1, touching |x| + |y| = 1 at +/-e_1 and +/-e_2")
    print("    inequality in R^2: 1 * ||v||_inf <= ||v||_1 <= 2 * ||v||_inf (2D analogue of 3 * ||v||_inf in R^3)")

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.95))
    xlim = (-1.75, 1.75)
    ylim = (-1.92, 1.62)

    diamond_verts = [(1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (0.0, -1.0)]

    def mark_axes_touches(ax):
        pts = [
            ((1.0, 0.0), r"$\mathbf{e}_1$", (1.08, 0.0), "left", "center"),
            ((-1.0, 0.0), r"$-\mathbf{e}_1$", (-1.08, 0.0), "right", "center"),
            ((0.0, 1.0), r"$\mathbf{e}_2$", (0.0, 1.07), "center", "bottom"),
            ((0.0, -1.0), r"$-\mathbf{e}_2$", (0.0, -1.08), "center", "top"),
        ]
        for p, lab, tpos, ha, va in pts:
            ax.plot([p[0]], [p[1]], "o", color=TEXT, ms=4.6, zorder=7)
            ax.text(tpos[0], tpos[1], lab, color=TEXT, fontsize=10.0, ha=ha, va=va, zorder=8, bbox=white_pad())

    # ---------------- Panel (a) ----------------
    ax = axes[0]
    frame_panel(ax, xlim, ylim)

    # Nested light fills + crisp boundaries
    ax.add_patch(Rectangle((-1.0, -1.0), 2.0, 2.0, fc=AMBER_LIGHT, ec="none", alpha=0.45, zorder=2))
    ax.add_patch(Circle((0.0, 0.0), 1.0, fc=BLUE_LIGHT, ec="none", alpha=0.55, zorder=2.5))
    ax.add_patch(Polygon(diamond_verts, closed=True, fc=TEAL_LIGHT, ec="none", alpha=0.75, zorder=3))

    ax.add_patch(Rectangle((-1.0, -1.0), 2.0, 2.0, fc="none", ec=AMBER, lw=2.1, zorder=4))
    ax.add_patch(Circle((0.0, 0.0), 1.0, fc="none", ec=NAVY, lw=2.1, zorder=4.5))
    ax.add_patch(Polygon(diamond_verts, closed=True, fc="none", ec=TEAL, lw=2.1, zorder=5))

    mark_axes_touches(ax)

    # Mark (1/2, 1/2) and radial comparison segment
    ax.plot([0.0, 1.0 / math.sqrt(2.0)], [0.0, 1.0 / math.sqrt(2.0)], color=RED, lw=1.0, ls=":", zorder=5.5)
    ax.plot([0.5], [0.5], "o", color=RED, ms=5.4, zorder=8)
    ax.plot([0.53, 0.72], [0.53, 1.15], color=RED, lw=0.85, zorder=7)
    ax.text(
        1.67,
        1.32,
        r"$(1/2, 1/2)$: $\|\mathbf{v}\|_1 = 1$," + "\n" + r"$\|\mathbf{v}\|_2 = 1/\sqrt{2} \approx 0.707$",
        color=RED,
        fontsize=9.3,
        ha="right",
        va="center",
        zorder=8,
        bbox=white_pad(),
    )

    # Shape labels in open corners with leader lines
    ax.plot([-1.0, -1.24], [0.82, 1.12], color=AMBER, lw=0.85, zorder=7)
    ax.text(-1.67, 1.34, r"$\max(|x|, |y|) = 1$" + "\n" + r"($\|\mathbf{v}\|_\infty = 1$)", color=AMBER, fontsize=9.3,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([-0.707, -1.08], [-0.707, -1.16], color=NAVY, lw=0.85, zorder=7)
    ax.text(-1.67, -1.26, r"$\|\mathbf{v}\|_2 = 1$", color=NAVY, fontsize=9.8, ha="left", va="center",
            zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([0.55, 0.88], [-0.45, -1.08], color=TEAL, lw=0.85, zorder=7)
    ax.text(1.67, -1.26, r"$\|\mathbf{v}\|_1 = 1$" + "\n" + r"($|x| + |y| = 1$)", color=TEAL, fontsize=9.3,
            ha="right", va="center", zorder=8, bbox=white_pad(pad=0.06))

    label_box(ax, 0.0, -1.67, r"smaller ball = larger norm: $\|\mathbf{v}\|_1 \geq \|\mathbf{v}\|_2 \geq \|\mathbf{v}\|_\infty$",
              color=TEXT, fs=9.4)
    ax.set_title("(a) The three unit balls", fontweight="bold", color=TEXT, pad=8)

    # ---------------- Panel (b) ----------------
    ax = axes[1]
    frame_panel(ax, xlim, ylim)

    ax.add_patch(Rectangle((-1.0, -1.0), 2.0, 2.0, fc=AMBER_LIGHT, ec="none", alpha=0.35, zorder=2))
    ax.add_patch(Polygon(diamond_verts, closed=True, fc=TEAL_LIGHT, ec="none", alpha=0.70, zorder=3))
    ax.add_patch(Rectangle((-0.5, -0.5), 1.0, 1.0, fc="white", ec="none", alpha=0.65, zorder=3.5))

    ax.add_patch(Rectangle((-1.0, -1.0), 2.0, 2.0, fc="none", ec=AMBER, lw=2.1, zorder=4))
    ax.add_patch(Polygon(diamond_verts, closed=True, fc="none", ec=TEAL, lw=2.1, zorder=5))
    ax.add_patch(Rectangle((-0.5, -0.5), 1.0, 1.0, fc="none", ec=NAVY, lw=2.0, ls=(0, (5, 3)), zorder=5.5))

    mark_axes_touches(ax)

    for sx in (-0.5, 0.5):
        for sy in (-0.5, 0.5):
            ax.plot([sx], [sy], "o", color=NAVY, ms=4.6, zorder=7)

    ax.plot([0.52, 0.78], [0.52, 1.20], color=NAVY, lw=0.85, zorder=7)
    ax.text(1.67, 1.34, r"touches at $(\pm 1/2, \pm 1/2)$", color=NAVY, fontsize=9.3,
            ha="right", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([-1.0, -1.20], [0.85, 1.20], color=AMBER, lw=0.85, zorder=7)
    ax.text(-1.67, 1.34, r"$\|\mathbf{v}\|_\infty = 1$", color=AMBER, fontsize=9.8,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([-0.34, -0.98], [-0.50, -1.16], color=NAVY, lw=0.85, zorder=7)
    ax.text(-1.67, -1.26, r"$\|\mathbf{v}\|_\infty = 1/2$", color=NAVY, fontsize=9.8,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([0.58, 0.96], [-0.42, -1.16], color=TEAL, lw=0.85, zorder=7)
    ax.text(1.67, -1.26, r"$\|\mathbf{v}\|_1 = 1$", color=TEAL, fontsize=9.8,
            ha="right", va="center", zorder=8, bbox=white_pad(pad=0.06))

    label_box(ax, 0.0, -1.67, r"$\|\mathbf{v}\|_\infty \leq \|\mathbf{v}\|_1 \leq 2\|\mathbf{v}\|_\infty$", color=TEXT, fs=9.6)
    ax.set_title("(b) Equivalence of norms", fontweight="bold", color=TEXT, pad=8)

    fig.tight_layout(w_pad=1.3)
    save_fig(fig, out_dir, "maths0_unit_balls.png")


# ---------------------------------------------------------------------------
# Figure 4: what the induced norms measure
# ---------------------------------------------------------------------------
def fig_induced_norms(out_dir: Path) -> None:
    print("\nF4 maths0_induced_norms.png")

    A = (1.0 / math.sqrt(3.0)) * np.array([[3.0, -1.0], [0.0, math.sqrt(8.0)]])
    a1 = A[:, 0]
    a2 = A[:, 1]

    norm_A1 = float(np.linalg.norm(A, 1))
    norm_a1_1 = float(np.linalg.norm(a1, 1))
    norm_a2_1 = float(np.linalg.norm(a2, 1))

    p_11 = A @ np.array([1.0, 1.0])
    p_1m1 = A @ np.array([1.0, -1.0])
    norm_Ainf = float(np.linalg.norm(A, np.inf))

    ata = A.T @ A
    eigvals = np.linalg.eigvalsh(ata)  # ascending: [2, 4]
    norm_A2 = float(np.linalg.norm(A, 2))
    min_stretch_2 = 1.0 / float(np.linalg.norm(np.linalg.inv(A), 2))
    norm_AF = float(np.linalg.norm(A, "fro"))

    x_long = np.array([1.0, -1.0]) / math.sqrt(2.0)
    x_short = np.array([1.0, 1.0]) / math.sqrt(2.0)
    ax_long = A @ x_long
    ax_short = A @ x_short

    # Exact NumPy assertions
    assert np.allclose(a1, [math.sqrt(3.0), 0.0])
    assert np.allclose(a2, [-1.0 / math.sqrt(3.0), math.sqrt(8.0) / math.sqrt(3.0)])
    assert abs(norm_A1 - norm_a2_1) < 1e-12
    assert abs(norm_A1 - (1.0 + math.sqrt(8.0)) / math.sqrt(3.0)) < 1e-12
    assert np.allclose(p_11, [2.0 / math.sqrt(3.0), math.sqrt(8.0) / math.sqrt(3.0)])
    assert np.allclose(p_1m1, [4.0 / math.sqrt(3.0), -math.sqrt(8.0) / math.sqrt(3.0)])
    assert abs(norm_Ainf - 4.0 / math.sqrt(3.0)) < 1e-12
    assert abs(float(np.linalg.norm(p_1m1, np.inf)) - norm_Ainf) < 1e-12
    assert np.allclose(ata, [[3.0, -1.0], [-1.0, 3.0]])
    assert np.allclose(eigvals, [2.0, 4.0])
    assert abs(norm_A2 - math.sqrt(eigvals[1])) < 1e-12 and abs(norm_A2 - 2.0) < 1e-12
    assert abs(min_stretch_2 - math.sqrt(eigvals[0])) < 1e-12 and abs(min_stretch_2 - math.sqrt(2.0)) < 1e-12
    assert abs(float(np.linalg.norm(ax_long, 2)) - 2.0) < 1e-12
    assert abs(float(np.linalg.norm(ax_short, 2)) - math.sqrt(2.0)) < 1e-12
    assert abs(float(ax_long @ ax_short)) < 1e-12
    assert abs(norm_AF - math.sqrt(6.0)) < 1e-12

    print("  Matrix A = (1/sqrt(3)) * [[3, -1], [0, sqrt(8)]]")
    print(f"    column a_1 = (sqrt(3), 0) = ({a1[0]:.6f}, {a1[1]:.6f}) approx ({a1[0]:.3f}, 0), ||a_1||_1 = {norm_a1_1:.3f}")
    print(
        f"    column a_2 = (-1/sqrt(3), sqrt(8)/sqrt(3)) = ({a2[0]:.6f}, {a2[1]:.6f}) "
        f"approx ({a2[0]:.3f}, {a2[1]:.3f}), ||a_2||_1 = {norm_a2_1:.6f} approx {norm_a2_1:.2f}"
    )
    print(f"    ||A||_1 = (1 + sqrt(8))/sqrt(3) = {norm_A1:.6f} approx {norm_A1:.2f} (attained at x = e_2)")
    print(
        f"    A(1, 1) = (2/sqrt(3), sqrt(8)/sqrt(3)) = ({p_11[0]:.6f}, {p_11[1]:.6f}) "
        f"approx ({p_11[0]:.3f}, {p_11[1]:.3f})"
    )
    print(
        f"    A(1, -1) = (4/sqrt(3), -sqrt(8)/sqrt(3)) = ({p_1m1[0]:.6f}, {p_1m1[1]:.6f}) "
        f"approx ({p_1m1[0]:.3f}, {p_1m1[1]:.3f})"
    )
    print(f"    ||A||_inf = 4/sqrt(3) = {norm_Ainf:.6f} approx {norm_Ainf:.2f} (attained at x = (1, -1))")
    print(f"    A^T A = [[3, -1], [-1, 3]], eigenvalues of A^T A = {eigvals[1]:g} and {eigvals[0]:g}")
    print(
        f"    ||A||_2 = sqrt(4) = {norm_A2:g} from x = (1, -1)/sqrt(2), "
        f"A x = ({ax_long[0]:.3f}, {ax_long[1]:.3f})"
    )
    print(
        f"    1/||A^(-1)||_2 = sqrt(2) = {min_stretch_2:.6f} approx {min_stretch_2:.3f} from x = (1, 1)/sqrt(2), "
        f"A x = ({ax_short[0]:.3f}, {ax_short[1]:.3f})"
    )
    print(f"    ||A||_F = sqrt(6) = {norm_AF:.6f} approx {norm_AF:.2f}")

    fig, axes = plt.subplots(1, 3, figsize=(10.9, 4.35))
    # Identical axis limits in all three panels
    xlim = (-3.00, 3.00)
    ylim = (-3.60, 2.95)

    for ax in axes:
        frame_panel(ax, xlim, ylim)

    # ---------------- Panel (a): The 1-norm ----------------
    ax = axes[0]
    unit_diamond = [(1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (0.0, -1.0)]
    img_1 = [tuple(a1), tuple(a2), tuple(-a1), tuple(-a2)]
    outer_diamond = [(norm_A1, 0.0), (0.0, norm_A1), (-norm_A1, 0.0), (0.0, -norm_A1)]

    ax.add_patch(Polygon(unit_diamond, closed=True, fc=GREY_WALL, ec=SLATE, lw=1.25, alpha=0.65, zorder=2))
    ax.add_patch(Polygon(img_1, closed=True, fc=TEAL_LIGHT, ec="none", alpha=0.72, zorder=3))
    ax.add_patch(Polygon(img_1, closed=True, fc="none", ec=TEAL, lw=2.1, zorder=5))
    ax.add_patch(Polygon(outer_diamond, closed=True, fc="none", ec=RED, lw=1.7, ls=(0, (5, 3)), zorder=4))

    arrow(ax, (0, 0), a1, color=TEAL, lw=1.9, ms=12, z=6)
    arrow(ax, (0, 0), a2, color=RED, lw=2.1, ms=13, z=6)
    for pt, col in ((a1, TEAL), (-a1, TEAL), (a2, RED), (-a2, RED)):
        ax.plot([pt[0]], [pt[1]], "o", color=col, ms=4.5, zorder=7)

    ax.plot([-0.60, -1.05], [1.66, 2.26], color=RED, lw=0.85, zorder=7)
    ax.text(-2.88, 2.52, r"$\mathbf{a}_2 \approx (-0.577, 1.633)$", color=RED, fontsize=9.1,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([0.85, 1.20], [norm_A1 - 0.85, 1.88], color=RED, lw=0.85, zorder=7)
    ax.text(2.88, 2.12, r"$\|A\|_1 = \|\mathbf{a}_2\|_1 \approx 2.21$", color=RED, fontsize=9.2,
            ha="right", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([a1[0], 1.55], [-0.06, -1.94], color=TEAL, lw=0.85, zorder=7)
    ax.text(2.88, -2.18, r"$\mathbf{a}_1 \approx (1.732, 0)$", color=TEAL, fontsize=9.2,
            ha="right", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([-0.55, -1.25], [-0.45, -1.94], color=SLATE, lw=0.8, zorder=7)
    ax.text(-2.88, -2.18, "unit 1-ball", color=SLATE, fontsize=9.1,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    label_box(ax, 0.0, -3.08, r"all the budget in one column: $\mathbf{x} = \mathbf{e}_2$", color=TEXT, fs=9.1)
    ax.set_title("(a) The 1-norm", fontweight="bold", color=TEXT, pad=8)

    # ---------------- Panel (b): The infinity-norm ----------------
    ax = axes[1]
    img_inf = [tuple(p_11), tuple(-p_1m1), tuple(-p_11), tuple(p_1m1)]

    ax.add_patch(Rectangle((-1.0, -1.0), 2.0, 2.0, fc=GREY_WALL, ec=SLATE, lw=1.25, alpha=0.65, zorder=2))
    ax.add_patch(Polygon(img_inf, closed=True, fc=AMBER_LIGHT, ec="none", alpha=0.72, zorder=3))
    ax.add_patch(Polygon(img_inf, closed=True, fc="none", ec=AMBER, lw=2.1, zorder=5))
    ax.add_patch(
        Rectangle(
            (-norm_Ainf, -norm_Ainf),
            2.0 * norm_Ainf,
            2.0 * norm_Ainf,
            fc="none",
            ec=RED,
            lw=1.7,
            ls=(0, (5, 3)),
            zorder=4,
        )
    )

    arrow(ax, (0, 0), p_11, color=AMBER, lw=1.9, ms=12, z=6)
    arrow(ax, (0, 0), p_1m1, color=RED, lw=2.1, ms=13, z=6)
    for pt, col in ((p_11, AMBER), (-p_11, AMBER), (p_1m1, RED), (-p_1m1, RED)):
        ax.plot([pt[0]], [pt[1]], "o", color=col, ms=4.5, zorder=7)

    ax.text(0.0, norm_Ainf + 0.14, r"$\|A\|_\infty = 4/\sqrt{3} \approx 2.31$", color=RED, fontsize=9.3,
            ha="center", va="bottom", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([p_11[0] - 0.03, 0.90], [p_11[1] + 0.03, 1.88], color=AMBER, lw=0.85, zorder=9)
    ax.text(-0.30, 1.98, r"$A(1, 1) \approx (1.155, 1.633)$", color=AMBER, fontsize=9.0,
            ha="center", va="center", zorder=8, bbox=white_pad(pad=0.05))

    ax.plot([p_1m1[0] - 0.06, 1.82], [p_1m1[1] - 0.02, -1.92], color=RED, lw=0.85, zorder=9)
    ax.text(0.38, -1.98, r"$A(1, -1) \approx (2.309, -1.633)$", color=RED, fontsize=9.0,
            ha="center", va="center", zorder=8, bbox=white_pad(pad=0.05))

    ax.plot([-1.00, -1.85], [-0.75, -2.44], color=SLATE, lw=0.8, zorder=7)
    ax.text(-2.88, -2.56, r"unit $\infty$-ball", color=SLATE, fontsize=9.0,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.05))

    label_box(ax, 0.0, -3.08, r"signs matched to row 1: $\mathbf{x} = (1, -1)$", color=TEXT, fs=9.1)
    ax.set_title(r"(b) The $\infty$-norm", fontweight="bold", color=TEXT, pad=8)

    # ---------------- Panel (c): The 2-norm ----------------
    ax = axes[2]
    tt = np.linspace(0.0, 2.0 * np.pi, 400)
    unit_circ = np.vstack([np.cos(tt), np.sin(tt)])
    ell_pts = A @ unit_circ

    ax.add_patch(Circle((0.0, 0.0), 1.0, fc=GREY_WALL, ec=SLATE, lw=1.25, alpha=0.65, zorder=2))
    ax.fill(ell_pts[0], ell_pts[1], color=BLUE_LIGHT, alpha=0.72, zorder=3, lw=0)
    ax.plot(ell_pts[0], ell_pts[1], color=NAVY, lw=2.1, zorder=5)
    ax.add_patch(Circle((0.0, 0.0), norm_A2, fc="none", ec=RED, lw=1.7, ls=(0, (5, 3)), zorder=4))
    ax.add_patch(Circle((0.0, 0.0), min_stretch_2, fc="none", ec=TEAL, lw=1.6, ls=(0, (4, 3)), zorder=4))

    arrow(ax, (0, 0), ax_long, color=RED, lw=2.1, ms=13, z=6)
    arrow(ax, (0, 0), ax_short, color=TEAL, lw=2.1, ms=13, z=6)
    for pt, col in ((ax_long, RED), (-ax_long, RED), (ax_short, TEAL), (-ax_short, TEAL)):
        ax.plot([pt[0]], [pt[1]], "o", color=col, ms=4.5, zorder=7)

    ax.plot([1.414, 1.75], [1.414, 2.22], color=RED, lw=0.85, zorder=7)
    ax.text(2.88, 2.45, r"$\|A\|_2 = 2$", color=RED, fontsize=9.6,
            ha="right", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([-0.82, -1.18], [1.15, 2.22], color=TEAL, lw=0.85, zorder=7)
    ax.text(-2.88, 2.45, r"$1/\|A^{-1}\|_2 = \sqrt{2}$", color=TEAL, fontsize=9.4,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([ax_long[0] + 0.04, 1.55], [ax_long[1] - 0.05, -1.96], color=RED, lw=0.85, zorder=7)
    ax.text(2.88, -2.22, r"from $\mathbf{x} = (1, -1)/\sqrt{2}$", color=RED, fontsize=9.0,
            ha="right", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([-ax_short[0] - 0.04, -1.25], [-ax_short[1] - 0.04, -1.96], color=TEAL, lw=0.85, zorder=7)
    ax.text(-2.88, -2.22, r"from $\mathbf{x} = (1, 1)/\sqrt{2}$", color=TEAL, fontsize=9.0,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    label_box(ax, 0.0, -3.08, r"eigenvalues of $A^T A$: $4$ and $2$", color=TEXT, fs=9.1)
    ax.set_title("(c) The 2-norm", fontweight="bold", color=TEXT, pad=8)

    fig.tight_layout(w_pad=1.0)
    save_fig(fig, out_dir, "maths0_induced_norms.png")


# ---------------------------------------------------------------------------
# Figure 3: unit circle stretched into an ellipse (induced 2-norm)
# ---------------------------------------------------------------------------
def fig_two_norm_ellipse(out_dir: Path) -> None:
    print("\nF5 maths0_two_norm_ellipse.png")

    A = (1.0 / math.sqrt(3.0)) * np.array([[3.0, -1.0], [0.0, math.sqrt(8.0)]])
    ata = A.T @ A
    eigvals = np.linalg.eigvalsh(ata)  # ascending: [2, 4]
    norm_A2 = float(np.linalg.norm(A, 2))
    min_stretch_2 = 1.0 / float(np.linalg.norm(np.linalg.inv(A), 2))

    assert np.allclose(ata, [[3.0, -1.0], [-1.0, 3.0]])
    assert np.allclose(eigvals, [2.0, 4.0])
    assert abs(norm_A2 - 2.0) < 1e-12
    assert abs(min_stretch_2 - math.sqrt(2.0)) < 1e-12

    # 8 evenly spaced unit vectors (45 deg steps), numbered 1..8
    angles_deg = [45 * k for k in range(8)]
    unit_pts = np.array([[math.cos(math.radians(d)), math.sin(math.radians(d))] for d in angles_deg])
    img_pts = (A @ unit_pts.T).T
    img_norms = np.linalg.norm(img_pts, axis=1)

    # Indices: 0->#1 (0 deg), 1->#2 (45 deg, min), 2->#3 (90 deg), 3->#4 (135 deg, max),
    #          4->#5 (180 deg), 5->#6 (225 deg, min), 6->#7 (270 deg), 7->#8 (315 deg, max)
    assert np.allclose(unit_pts[1], [1.0 / math.sqrt(2.0), 1.0 / math.sqrt(2.0)])
    assert np.allclose(unit_pts[7], [1.0 / math.sqrt(2.0), -1.0 / math.sqrt(2.0)])
    assert abs(float(img_norms[1]) - math.sqrt(2.0)) < 1e-12
    assert abs(float(img_norms[5]) - math.sqrt(2.0)) < 1e-12
    assert abs(float(img_norms[3]) - 2.0) < 1e-12
    assert abs(float(img_norms[7]) - 2.0) < 1e-12
    for idx_axis in (0, 2, 4, 6):
        assert abs(float(img_norms[idx_axis]) - math.sqrt(3.0)) < 1e-12
    assert abs(float(unit_pts[7] @ unit_pts[1])) < 1e-12
    assert abs(float(img_pts[7] @ img_pts[1])) < 1e-12

    ang_major_deg = math.degrees(math.atan2(float(img_pts[7, 1]), float(img_pts[7, 0])))
    ang_minor_deg = math.degrees(math.atan2(float(img_pts[1, 1]), float(img_pts[1, 0])))
    assert abs((ang_minor_deg - ang_major_deg) - 90.0) < 1e-12

    print("  Matrix A = (1/sqrt(3)) * [[3, -1], [0, sqrt(8)]]")
    print(f"  A^T A = [[3, -1], [-1, 3]], eigenvalues of A^T A = {eigvals[1]:g} and {eigvals[0]:g}")
    print(
        f"  max stretch ||A||_2 = sqrt(4) = {norm_A2:g}, reached at +/- (1, -1)/sqrt(2) (#8, #4) -> "
        f"+/- ({img_pts[7, 0]:.3f}, {img_pts[7, 1]:.3f}), angle = {ang_major_deg:.2f} deg"
    )
    print(
        f"  min stretch 1/||A^(-1)||_2 = sqrt(2) = {min_stretch_2:.6f} approx {min_stretch_2:.3f}, "
        f"reached at +/- (1, 1)/sqrt(2) (#2, #6) -> +/- ({img_pts[1, 0]:.3f}, {img_pts[1, 1]:.3f}), "
        f"angle = {ang_minor_deg:.2f} deg"
    )
    print(
        "  cardinal unit vectors (#1, #3, #5, #7, +/-e_1 and +/-e_2): "
        f"||A x||_2 = sqrt(3) = {math.sqrt(3.0):.6f} approx {math.sqrt(3.0):.3f}"
    )
    print("  8 evenly spaced unit vectors (45 deg steps) and their images under A:")
    for i, deg in enumerate(angles_deg):
        ux, uy = unit_pts[i]
        vx, vy = img_pts[i]
        ux = 0.0 if abs(ux) < 1e-12 else ux
        uy = 0.0 if abs(uy) < 1e-12 else uy
        vx = 0.0 if abs(vx) < 1e-12 else vx
        vy = 0.0 if abs(vy) < 1e-12 else vy
        print(
            f"    #{i + 1} ({deg:3d} deg): x = ({ux:.3f}, {uy:.3f}) -> "
            f"A x = ({vx:.3f}, {vy:.3f}), ||A x||_2 = {img_norms[i]:.3f}"
        )

    fig, axes = plt.subplots(1, 2, figsize=(10.65, 5.05))
    fig.subplots_adjust(left=0.02, right=0.98, bottom=0.03, top=0.91, wspace=0.18)

    # Identical axis limits in both panels so sizes compare 1-to-1
    xlim = (-2.95, 2.95)
    ylim = (-3.25, 2.85)
    for ax in axes:
        frame_panel(ax, xlim, ylim)

    def spoke_style(idx: int):
        if idx in (3, 7):  # #4, #8: max stretch
            return RED, (2.45 if idx == 7 else 1.90), (13.5 if idx == 7 else 11.5), 6.2, 5.0
        if idx in (1, 5):  # #2, #6: min stretch
            return TEAL, (2.45 if idx == 1 else 1.90), (13.5 if idx == 1 else 11.5), 6.1, 5.0
        return SLATE, 1.35, 10.0, 5.2, 4.2

    # ---------------- Panel (a): Before (input unit circle) ----------------
    ax = axes[0]
    ax.add_patch(Circle((0.0, 0.0), 1.0, fc=BLUE_PALE, ec="none", alpha=0.55, zorder=2))
    ax.add_patch(Circle((0.0, 0.0), 1.0, fc="none", ec=NAVY, lw=2.0, zorder=4))

    for i in range(8):
        col, lw, ms_arr, z_arr, ms_dot = spoke_style(i)
        p = unit_pts[i]
        arrow(ax, (0.0, 0.0), p, color=col, lw=lw, ms=ms_arr, z=z_arr)
        ax.plot([p[0]], [p[1]], "o", color=col, ms=ms_dot, zorder=7)
        r_lab = 1.23 if i in (1, 3, 5, 7) else 1.21
        lp = r_lab * p
        ax.text(
            lp[0],
            lp[1],
            f"${i + 1}$",
            color=col,
            fontsize=9.4,
            fontweight="bold" if i in (1, 3, 5, 7) else "normal",
            ha="center",
            va="center",
            zorder=8,
            bbox=white_pad(pad=0.04),
        )
    ax.plot([0.0], [0.0], "o", color=TEXT, ms=3.8, zorder=8)

    # Descriptive labels in open outer region of Panel (a)
    c120 = np.array([math.cos(math.radians(120.0)), math.sin(math.radians(120.0))])
    ax.plot([c120[0], -1.35], [c120[1], 2.15], color=NAVY, lw=0.85, zorder=7)
    ax.text(-2.82, 2.36, r"unit circle $\|\mathbf{x}\|_2 = 1$", color=NAVY, fontsize=9.6,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.06))

    ax.plot([0.98, 1.55], [0.98, 1.92], color=TEAL, lw=0.85, zorder=7)
    ax.text(
        2.82,
        2.26,
        "min-stretch directions ($2, 6$):\n" + r"$\mathbf{x} = \pm(1, 1)/\sqrt{2}$",
        color=TEAL,
        fontsize=9.2,
        ha="right",
        va="center",
        zorder=8,
        bbox=white_pad(pad=0.06),
    )

    ax.plot([0.98, 1.55], [-0.98, -1.80], color=RED, lw=0.85, zorder=7)
    ax.text(
        2.82,
        -2.14,
        "max-stretch directions ($8, 4$):\n" + r"$\mathbf{x} = \pm(1, -1)/\sqrt{2}$",
        color=RED,
        fontsize=9.2,
        ha="right",
        va="center",
        zorder=8,
        bbox=white_pad(pad=0.06),
    )

    label_box(ax, 0.0, -2.82, r"8 unit vectors $\mathbf{x}$ spaced by $45^\circ$", color=TEXT, fs=9.2)
    ax.set_title(r"(a) Before: unit circle $\|\mathbf{x}\|_2 = 1$", fontweight="bold", color=TEXT, pad=8)

    # ---------------- Panel (b): After applying A ----------------
    ax = axes[1]
    tt = np.linspace(0.0, 2.0 * np.pi, 400)
    ell_pts = A @ np.vstack([np.cos(tt), np.sin(tt)])

    # Faint unit circle for comparison
    ax.add_patch(Circle((0.0, 0.0), 1.0, fc=GREY_WALL, ec=SLATE, lw=1.2, ls=(0, (3, 2.5)), alpha=0.75, zorder=2))

    # Image ellipse and touching dashed circles of radii 2 and sqrt(2)
    ax.fill(ell_pts[0], ell_pts[1], color=BLUE_LIGHT, alpha=0.68, zorder=2.5, lw=0)
    ax.plot(ell_pts[0], ell_pts[1], color=NAVY, lw=2.1, zorder=5)
    ax.add_patch(Circle((0.0, 0.0), norm_A2, fc="none", ec=RED, lw=1.65, ls=(0, (5, 3)), zorder=4))
    ax.add_patch(Circle((0.0, 0.0), min_stretch_2, fc="none", ec=TEAL, lw=1.55, ls=(0, (4, 3)), zorder=4))

    for i in range(8):
        col, lw, ms_arr, z_arr, ms_dot = spoke_style(i)
        q = img_pts[i]
        u_dir = q / img_norms[i]
        arrow(ax, (0.0, 0.0), q, color=col, lw=lw, ms=ms_arr, z=z_arr)
        ax.plot([q[0]], [q[1]], "o", color=col, ms=ms_dot, zorder=7.2)
        if i in (3, 7):      # r = 2.000 -> place outside outer dashed circle
            r_lab = 2.19
        elif i in (1, 5):    # r = 1.414 -> place in wide gap inside outer circle
            r_lab = 1.62
        else:                # r = 1.732 -> place midway between 1.732 and 2.000
            r_lab = 1.855
        lp = r_lab * u_dir
        ax.text(
            lp[0],
            lp[1],
            f"${i + 1}$",
            color=col,
            fontsize=9.2,
            ha="center",
            va="center",
            zorder=8,
            bbox=white_pad(pad=0.03),
        )
    ax.plot([0.0], [0.0], "o", color=TEXT, ms=3.8, zorder=8)

    # Max stretch label (pointing to outer dashed circle at 36 deg, clear of #1 and #2)
    p_outer = norm_A2 * np.array([math.cos(math.radians(36.0)), math.sin(math.radians(36.0))])
    ax.plot([p_outer[0], 1.88], [p_outer[1], 1.98], color=RED, lw=0.85, zorder=7)
    ax.text(
        2.82,
        2.32,
        r"max stretch $\|A\|_2 = 2$" + "\n" + r"semi-major axis ($8, 4$)",
        color=RED,
        fontsize=9.2,
        ha="right",
        va="center",
        zorder=8,
        bbox=white_pad(pad=0.06),
    )

    # Min stretch label (pointing to inner dashed circle at 127 deg, bisecting #3 and #4)
    p_inner = min_stretch_2 * np.array([math.cos(math.radians(127.0)), math.sin(math.radians(127.0))])
    ax.plot([p_inner[0], -1.24], [p_inner[1], 1.98], color=TEAL, lw=0.85, zorder=7)
    ax.text(
        -2.82,
        2.32,
        r"min stretch $1/\|A^{-1}\|_2 = \sqrt{2}$" + "\n" + r"semi-minor axis ($2, 6$)",
        color=TEAL,
        fontsize=9.2,
        ha="left",
        va="center",
        zorder=8,
        bbox=white_pad(pad=0.06),
    )

    # Coordinates of #8 (pointing to semi-major shaft, clear of badge #8)
    ax.plot([1.22, 1.72], [-0.86, -1.94], color=RED, lw=0.85, zorder=7)
    ax.text(
        2.82,
        -2.18,
        r"at $8$: $A\mathbf{x} \approx (1.633, -1.155)$",
        color=RED,
        fontsize=9.1,
        ha="right",
        va="center",
        zorder=8,
        bbox=white_pad(pad=0.05),
    )

    # Faint unit circle callout (at 207 deg, bisecting #5 and #6)
    p_faint = np.array([math.cos(math.radians(207.0)), math.sin(math.radians(207.0))])
    ax.plot([p_faint[0], -1.68], [p_faint[1], -1.96], color=SLATE, lw=0.8, zorder=7)
    ax.text(-2.82, -2.18, "unit circle (faint)", color=SLATE, fontsize=9.1,
            ha="left", va="center", zorder=8, bbox=white_pad(pad=0.05))

    label_box(ax, 0.0, -2.82, r"semi-axes $\sqrt{4} = 2$ and $\sqrt{2}$ from eigenvalues of $A^T A$",
              color=TEXT, fs=9.1)
    ax.set_title(r"(b) After $A$: ellipse $\{A\mathbf{x} : \|\mathbf{x}\|_2 = 1\}$",
                 fontweight="bold", color=TEXT, pad=8)

    # Inter-panel transformation arrow ->^A aligned with y = 0 in figure coordinates
    fig.canvas.draw()
    inv_fig = fig.transFigure.inverted()
    x_right_a, y_zero = inv_fig.transform(axes[0].transData.transform((xlim[1], 0.0)))
    x_left_b, _ = inv_fig.transform(axes[1].transData.transform((xlim[0], 0.0)))
    x_mid = 0.5 * (x_right_a + x_left_b)
    dx_arrow = 0.34 * (x_left_b - x_right_a)
    map_arrow = FancyArrowPatch(
        (x_mid - dx_arrow, y_zero),
        (x_mid + dx_arrow, y_zero),
        transform=fig.transFigure,
        arrowstyle="-|>",
        mutation_scale=16,
        color=NAVY,
        lw=2.2,
        zorder=10,
    )
    fig.add_artist(map_arrow)
    fig.text(x_mid, y_zero + 0.018, r"$A$", fontsize=12.5, color=NAVY, ha="center", va="bottom")
    fig.text(x_mid, y_zero - 0.022, r"$\mathbf{x} \mapsto A\mathbf{x}$", fontsize=9.2, color=SLATE,
             ha="center", va="top")

    save_fig(fig, out_dir, "maths0_two_norm_ellipse.png")


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    fig_projection_reflection(out_dir)
    fig_airline_network(out_dir)
    fig_unit_balls(out_dir)
    fig_induced_norms(out_dir)
    fig_two_norm_ellipse(out_dir)


if __name__ == "__main__":
    main()
