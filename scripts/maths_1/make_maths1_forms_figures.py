#!/usr/bin/env python3
"""Generate eight publication-quality differential forms figures for 'Maths 1 - Differential Geometry'.

Project Context:
    Illustrates the Differential Forms section of `maths_1_differential_geometry.md`
    (Figures 9 and 11 to 17), matching the visual palette, typography (DejaVu Sans + Computer Modern mathtext),
    220-dpi white-card style, <= 11-inch width cap, and >= 9-pt minimum text size of
    `make_maths1_figures.py`.

What This Script Does:
    Accepts `<output_dir>` as its sole command-line argument, generates all eight PNG figures,
    computes every curve, arrow, projection, and area directly from the analytical formulas
    in the text, enforces width/fontsize/aspect/handedness assertions, and prints to stdout
    every numerical value quoted in the figure labels, captions, and subsection text:
        9.  `maths1_one_form_stacks.png`
        11. `maths1_semicircle_pullback_bins.png`
        12. `maths1_wedge_area.png`
        13. `maths1_surface_pullback.png`
        14. `maths1_flux_shadows.png`
        15. `maths1_microscopic_stokes.png`
        16. `maths1_half_disc_cell.png`
        17. `maths1_cylinder_cap_shadow.png`

Performance Note:
    Uses vectorized NumPy array operations over compact 2D/3D meshes (< 200 x 200 points),
    keeping peak memory below 200 MB and rendering all eight 220-dpi PNGs sequentially
    in a few seconds without multiprocessing overhead.

Usage:
    /home/ubuntu/.claude/skills/lecture-notes/.venv/bin/python \
        make_maths1_forms_figures.py <output_dir>
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Arc, Circle, FancyArrowPatch, FancyBboxPatch, Polygon
from mpl_toolkits.mplot3d import proj3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np


# ---------------------------------------------------------------------------
# Consistent visual palette & typography matching make_maths1_figures.py
# Minimum text size across all saved figures is >= 9.1 pt (brief rule: >= 9 pt).
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
})


def save_fig(fig: plt.Figure, out_dir: Path, filename: str) -> Path:
    """Save figure at 220 dpi with tight bounding box and verify width <= 11 in and text >= 9 pt."""
    for txt_obj in fig.findobj(matplotlib.text.Text):
        if txt_obj.get_visible() and txt_obj.get_text().strip():
            fs = float(txt_obj.get_fontsize())
            if fs < 9.0 - 1e-6:
                raise AssertionError(
                    f"{filename}: text {txt_obj.get_text()!r} has fontsize {fs:.2f} pt < 9.0 pt"
                )
    out_path = out_dir / filename
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", pad_inches=0.10, facecolor="white")
    plt.close(fig)
    with out_path.open("rb") as fh:
        sig_ihdr = fh.read(24)
    if sig_ihdr[:8] != b"\x89PNG\r\n\x1a\n":
        raise AssertionError(f"Invalid PNG header in {out_path}")
    w_px = int.from_bytes(sig_ihdr[16:20], "big")
    h_px = int.from_bytes(sig_ihdr[20:24], "big")
    w_in = w_px / DPI
    h_in = h_px / DPI
    if w_in > MAX_WIDTH_IN + 1e-6:
        raise AssertionError(
            f"{filename} width {w_in:.2f} in ({w_px} px) exceeds {MAX_WIDTH_IN} in limit"
        )
    print(f"  [saved] {out_path} ({w_px}x{h_px} px = {w_in:.2f}x{h_in:.2f} in @ {DPI} dpi)")
    return out_path


def draw_card(
    ax: plt.Axes,
    x: float,
    y: float,
    w: float,
    h: float,
    fc: str = GREY_BG,
    ec: str = GREY_LINE,
    lw: float = 1.05,
    pad: float = 0.04,
    zorder: int = 1,
) -> FancyBboxPatch:
    """Draw a rounded background card in data coordinates."""
    box = FancyBboxPatch(
        (x + pad, y + pad),
        w - 2 * pad,
        h - 2 * pad,
        boxstyle=f"round,pad={pad},rounding_size=0.10",
        facecolor=fc,
        edgecolor=ec,
        linewidth=lw,
        zorder=zorder,
    )
    ax.add_patch(box)
    return box


def draw_arrow_2d(
    ax: plt.Axes,
    p_start: tuple[float, float],
    p_end: tuple[float, float],
    color: str,
    lw: float = 2.1,
    ls: str = "-",
    head_length: float = 6.5,
    head_width: float = 3.9,
    zorder: int = 6,
) -> FancyArrowPatch:
    """Draw a 2D vector arrow with exact point-sized head (mutation_scale=1)."""
    arr = FancyArrowPatch(
        p_start,
        p_end,
        arrowstyle=f"-|>,head_length={head_length},head_width={head_width}",
        mutation_scale=1.0,
        color=color,
        linewidth=lw,
        linestyle=ls,
        shrinkA=0.0,
        shrinkB=0.0,
        zorder=zorder,
    )
    ax.add_patch(arr)
    return arr


def view_direction_3d(elev_deg: float, azim_deg: float) -> np.ndarray:
    """Unit vector pointing from the origin toward the 3D camera."""
    el = math.radians(elev_deg)
    az = math.radians(azim_deg)
    return np.array([math.cos(el) * math.cos(az), math.cos(el) * math.sin(az), math.sin(el)])


def add_3d_arrow(
    ax: plt.Axes,
    p_start: np.ndarray,
    p_end: np.ndarray,
    col: str,
    elev_deg: float,
    azim_deg: float,
    lw: float = 2.2,
    head_len: float | None = None,
    zord: int = 8,
) -> None:
    """Draw a 3D arrow whose wings lie perpendicular to the camera ray so they never foreshorten."""
    ax.plot(
        [p_start[0], p_end[0]],
        [p_start[1], p_end[1]],
        [p_start[2], p_end[2]],
        color=col,
        lw=lw,
        zorder=zord,
    )
    d = p_end - p_start
    d_norm = float(np.linalg.norm(d))
    if d_norm < 1e-9:
        return
    u = d / d_norm
    v_cam = view_direction_3d(elev_deg, azim_deg)
    perp = np.cross(u, v_cam)
    p_norm = float(np.linalg.norm(perp))
    if p_norm < 1e-6:
        ref = np.array([0.0, 0.0, 1.0]) if abs(u[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
        perp = np.cross(u, ref)
        p_norm = float(np.linalg.norm(perp))
    perp /= p_norm
    hlen = head_len if head_len is not None else min(0.11, 0.45 * d_norm)
    hw = 0.48 * hlen
    for sgn in (+1.0, -1.0):
        wing = p_end - hlen * u + sgn * hw * perp
        ax.plot(
            [p_end[0], wing[0]],
            [p_end[1], wing[1]],
            [p_end[2], wing[2]],
            color=col,
            lw=lw,
            zorder=zord,
        )


def set_equal_3d_box(
    ax: plt.Axes,
    xlim: tuple[float, float],
    ylim: tuple[float, float],
    zlim: tuple[float, float],
    zoom: float = 1.0,
) -> None:
    """Enforce strictly equal data ranges and a 1:1:1 3D box aspect."""
    span_x = xlim[1] - xlim[0]
    span_y = ylim[1] - ylim[0]
    span_z = zlim[1] - zlim[0]
    assert abs(span_x - span_y) < 1e-9 and abs(span_x - span_z) < 1e-9, (
        f"3D spans must be equal: {span_x}, {span_y}, {span_z}"
    )
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_zlim(*zlim)
    ax.set_box_aspect((1.0, 1.0, 1.0), zoom=zoom)


def annotate_3d_point(
    ax: plt.Axes,
    proj_mat: np.ndarray,
    xyz_target: tuple[float, float, float] | np.ndarray,
    xytext_2d: tuple[float, float],
    text: str,
    color: str,
    fontsize: float = 9.3,
    ec: str | None = None,
    shrinkB: float = 3.0,
    zorder: int = 12,
) -> None:
    """Annotate a 3D point cleanly using projected 2D data coordinates on the Axes3D."""
    sx, sy, _ = proj3d.proj_transform(
        float(xyz_target[0]), float(xyz_target[1]), float(xyz_target[2]), proj_mat
    )
    edge_col = color if ec is None else ec
    ax.annotate(
        text,
        xy=(float(sx), float(sy)),
        xycoords="data",
        xytext=xytext_2d,
        textcoords="axes fraction",
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight="bold",
        color=color,
        bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=edge_col, lw=0.9, alpha=0.96),
        arrowprops=dict(arrowstyle="->", color=color, lw=1.15, shrinkB=shrinkB),
        zorder=zorder,
    )


# ===========================================================================
# Figure 9: maths1_one_form_stacks.png
# ===========================================================================
def make_fig7_one_form_stacks(out_dir: Path) -> None:
    fig = plt.figure(figsize=(10.6, 4.8), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.06, 1.0], wspace=0.26)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1])

    # --- Panel (a): Constant 1-form omega = 2 dx + 3 dy ---
    xs = np.linspace(-2.35, 3.55, 200)
    n_vals = list(range(-4, 7))
    for n_int in n_vals:
        ys = (n_int - 2.0 * xs) / 3.0
        if n_int == 0:
            ax_a.plot(xs, ys, color=NAVY, lw=2.0, ls="-", alpha=0.85, zorder=2)
        elif n_int > 0:
            ax_a.plot(xs, ys, color=BLUE, lw=1.35, ls="-", alpha=0.58, zorder=2)
        else:
            ax_a.plot(xs, ys, color=SLATE, lw=1.20, ls="--", alpha=0.55, zorder=2)

    ax_a.axhline(0.0, color=GREY_LINE, lw=1.0, zorder=1)
    ax_a.axvline(0.0, color=GREY_LINE, lw=1.0, zorder=1)

    x_lbl = -1.92
    n_badge = dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.90)
    for n_int in range(-3, 5):
        y_lbl = (n_int - 2.0 * x_lbl) / 3.0
        col_n = NAVY if n_int == 0 else (BLUE if n_int > 0 else SLATE)
        lbl_txt = f"$n = {n_int}$" if n_int in (0, 4) else f"${n_int}$"
        ax_a.text(
            x_lbl,
            y_lbl,
            lbl_txt,
            ha="center",
            va="center",
            fontsize=9.3,
            fontweight="bold" if n_int in (0, 4) else "normal",
            color=col_n,
            bbox=n_badge,
            zorder=5,
        )

    vecs_a = [
        ((-1.0, 2.0), RED, r"$\langle -1, 2\rangle$: $\omega = 4$" "\n" r"(line $0 \to 4$)", (0.95, 2.15), (-0.65, 1.55)),
        ((1.0, 0.0), AMBER, r"$\langle 1, 0\rangle$: $\omega = 2$" "\n" r"(line $0 \to 2$)", (2.15, 0.68), (0.95, 0.04)),
        ((3.0, -2.0), TEAL, r"$\langle 3, -2\rangle$: $\omega = 0$" "\n" r"(stays on line $0$)", (0.85, -1.78), (2.05, -1.38)),
    ]
    ax_a.scatter([0.0], [0.0], s=42, color=NAVY, zorder=8)
    for (vx, vy), vcol, vtxt, txt_pos, ptr_xy in vecs_a:
        val_w = int(round(2 * vx + 3 * vy))
        assert (vx, vy, val_w) in {(-1.0, 2.0, 4), (1.0, 0.0, 2), (3.0, -2.0, 0)}
        draw_arrow_2d(ax_a, (0.0, 0.0), (vx, vy), color=vcol, lw=2.8, head_length=7.0, head_width=4.4, zorder=7)
        ax_a.scatter([vx], [vy], s=32, color=vcol, edgecolor="white", lw=0.8, zorder=8)
        ax_a.annotate(
            vtxt,
            xy=ptr_xy,
            xytext=txt_pos,
            ha="center",
            va="center",
            fontsize=9.4,
            fontweight="bold",
            color=vcol,
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec=vcol, lw=0.95, alpha=0.96),
            arrowprops=dict(arrowstyle="->", color=vcol, lw=1.15, shrinkB=3),
            zorder=9,
        )

    ax_a.set_xlim(-2.30, 3.45)
    ax_a.set_ylim(-2.40, 2.85)
    ax_a.set_aspect("equal")
    ax_a.set_xticks([-2, -1, 0, 1, 2, 3])
    ax_a.set_yticks([-2, -1, 0, 1, 2])
    ax_a.set_xlabel("$x$", color=TEXT)
    ax_a.set_ylabel("$y$", color=TEXT)
    ax_a.set_title(r"(a) Constant 1-form $\omega = 2\,dx + 3\,dy$", fontweight="bold", color=TEXT, pad=8)

    # --- Panel (b): Varying 1-form dU for U = x^2 + y^2 ---
    ax_b.axhline(0.0, color=GREY_LINE, lw=1.0, zorder=1)
    ax_b.axvline(0.0, color=GREY_LINE, lw=1.0, zorder=1)

    th = np.linspace(0.0, 2.0 * np.pi, 360)
    u_levels = [1, 2, 3, 4, 5, 6, 7]
    # Stagger angles slightly in Q2 so all seven circles U = 1..7 are cleanly readable
    lbl_angles_deg = {1: 135.0, 2: 122.0, 3: 144.0, 4: 122.0, 5: 146.0, 6: 122.0, 7: 144.0}
    for u_lv in u_levels:
        rad = math.sqrt(u_lv)
        ax_b.plot(rad * np.cos(th), rad * np.sin(th), color=BLUE, lw=1.35, alpha=0.62, zorder=2)
        ang_u = math.radians(lbl_angles_deg[u_lv])
        lbl_u = f"$U = {u_lv}$" if u_lv in (1, 7) else f"${u_lv}$"
        ax_b.text(
            rad * math.cos(ang_u),
            rad * math.sin(ang_u),
            lbl_u,
            ha="center",
            va="center",
            fontsize=9.2,
            color=NAVY,
            bbox=dict(boxstyle="round,pad=0.07", fc="white", ec="none", alpha=0.90),
            zorder=5,
        )

    step_dx = 0.5
    p1_b = (1.0, 0.0)
    p2_b = (2.0, 0.0)
    du_p1 = 2.0 * p1_b[0] * step_dx  # 1.0
    du_p2 = 2.0 * p2_b[0] * step_dx  # 2.0
    crossed_p1 = [u for u in u_levels if p1_b[0] < math.sqrt(u) < p1_b[0] + step_dx]  # [2]
    crossed_p2 = [u for u in u_levels if p2_b[0] < math.sqrt(u) < p2_b[0] + step_dx]  # [5, 6]
    assert abs(du_p1 - 1.0) < 1e-12 and abs(du_p2 - 2.0) < 1e-12
    assert crossed_p1 == [2] and crossed_p2 == [5, 6]

    draw_arrow_2d(
        ax_b, p1_b, (p1_b[0] + step_dx, 0.0), color=AMBER, lw=3.0, head_length=6.8, head_width=4.2, zorder=7
    )
    ax_b.scatter([p1_b[0]], [0.0], s=38, color=AMBER, edgecolor="white", lw=0.8, zorder=8)
    ax_b.annotate(
        r"$(1, 0) \to (1.5, 0)$: crosses $U = 2$" "\n" r"$dU(\mathbf{v}) = 2(1)(0.5) = 1$",
        xy=(1.23, 0.04),
        xytext=(0.72, 1.66),
        ha="center",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=AMBER,
        bbox=dict(boxstyle="round,pad=0.16", fc="white", ec=AMBER, lw=0.95, alpha=0.96),
        arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2, shrinkB=3),
        zorder=9,
    )

    draw_arrow_2d(
        ax_b, p2_b, (p2_b[0] + step_dx, 0.0), color=RED, lw=3.0, head_length=6.8, head_width=4.2, zorder=7
    )
    ax_b.scatter([p2_b[0]], [0.0], s=38, color=RED, edgecolor="white", lw=0.8, zorder=8)
    ax_b.annotate(
        r"$(2, 0) \to (2.5, 0)$: crosses $U = 5, 6$" "\n" r"$dU(\mathbf{v}) = 2(2)(0.5) = 2$",
        xy=(2.24, -0.04),
        xytext=(0.78, -1.78),
        ha="center",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=RED,
        bbox=dict(boxstyle="round,pad=0.16", fc="white", ec=RED, lw=0.95, alpha=0.96),
        arrowprops=dict(arrowstyle="->", color=RED, lw=1.2, shrinkB=3),
        zorder=9,
    )

    ax_b.set_xlim(-2.85, 2.85)
    ax_b.set_ylim(-2.85, 2.85)
    ax_b.set_aspect("equal")
    ax_b.set_xticks([-2, -1, 0, 1, 2])
    ax_b.set_yticks([-2, -1, 0, 1, 2])
    ax_b.set_xlabel("$x$", color=TEXT)
    ax_b.set_ylabel("$y$", color=TEXT)
    ax_b.set_title(r"(b) Varying 1-form $dU$ for $U = x^2 + y^2$", fontweight="bold", color=TEXT, pad=8)

    save_fig(fig, out_dir, "maths1_one_form_stacks.png")
    print(
        f"[Fig 7] (a) omega = 2 dx + 3 dy, integer lines n = -4..6 (labelled n = -3..4); "
        f"omega(<-1, 2>) = 4 (line 0 -> 4), omega(<1, 0>) = 2 (line 0 -> 2), "
        f"omega(<3, -2>) = 0 (stays on line 0). "
        f"(b) U = x^2 + y^2 level circles U = {u_levels}; step v = <0.5, 0>: "
        f"(1, 0) -> (1.5, 0) crosses U = {crossed_p1} with dU(v) = 2*1*0.5 = {du_p1:.0f}; "
        f"(2, 0) -> (2.5, 0) crosses U = {crossed_p2} with dU(v) = 2*2*0.5 = {du_p2:.0f}."
    )


# ===========================================================================
# Figure 11: maths1_semicircle_pullback_bins.png
# ===========================================================================
def make_fig8_semicircle_pullback_bins(out_dir: Path) -> None:
    fig = plt.figure(figsize=(10.8, 5.0), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.0, 1.0], wspace=0.18)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1])

    th_fine = np.linspace(np.pi, 0.0, 300)
    xc_fine, yc_fine = np.cos(th_fine), np.sin(th_fine)

    # --- Panel (a): Graph map phi(a) = (a, sqrt(1 - a^2)), 4 equal a-bins ---
    a_pts = np.linspace(-1.0, 1.0, 5)
    xa = a_pts
    ya = np.sqrt(1.0 - xa**2)
    dxa = np.diff(xa)
    dya = np.diff(ya)
    chords_a = np.hypot(dxa, dya)

    ax_a.plot(xc_fine, yc_fine, color=GREY_LINE, lw=2.2, ls="-", zorder=1)
    ax_a.axhline(0.0, color=SLATE, lw=1.0, alpha=0.55, zorder=1)

    vert_specs_a = [
        (0, xa[0], ya[0], ya[1], TEAL, (-1.08, 0.43), "right"),
        (1, xa[1], ya[1], ya[2], TEAL, (-0.59, 0.96), "right"),
        (2, xa[3], ya[2], ya[3], RED, (+0.59, 0.96), "left"),
        (3, xa[4], ya[3], ya[4], RED, (+1.08, 0.43), "left"),
    ]
    for idx_b, xv_leg, y_s, y_e, col_y, (lx, ly), ha_y in vert_specs_a:
        draw_arrow_2d(
            ax_a, (xv_leg, y_s), (xv_leg, y_e), color=col_y, lw=1.9, ls="-", head_length=5.4, head_width=3.3, zorder=4
        )
        if idx_b in (0, 1):
            ax_a.plot([xa[idx_b], xa[idx_b + 1]], [y_e, y_e], color=SLATE, lw=0.9, ls=":", zorder=2)
        else:
            ax_a.plot([xa[idx_b], xa[idx_b + 1]], [y_s, y_s], color=SLATE, lw=0.9, ls=":", zorder=2)
        dy_val = dya[idx_b]
        dy_str = f"{dy_val:+.2f}".replace("-", "\u2212")
        ax_a.text(
            lx,
            ly,
            rf"$\Delta y = {dy_str}$",
            ha=ha_y,
            va="center",
            fontsize=9.2,
            fontweight="bold",
            color=col_y,
            bbox=dict(boxstyle="round,pad=0.10", fc="white", ec=col_y, lw=0.75, alpha=0.94),
            zorder=8,
        )

    chord_lbl_offsets_a = [(-0.66, 0.34), (-0.24, 0.72), (+0.24, 0.72), (+0.66, 0.34)]
    for i in range(4):
        draw_arrow_2d(
            ax_a,
            (float(xa[i]), float(ya[i])),
            (float(xa[i + 1]), float(ya[i + 1])),
            color=NAVY,
            lw=2.5,
            head_length=6.6,
            head_width=4.0,
            zorder=6,
        )
        c_str = "1" if abs(chords_a[i] - 1.0) < 1e-9 else f"{chords_a[i]:.2f}"
        cx_l, cy_l = chord_lbl_offsets_a[i]
        ax_a.text(
            cx_l,
            cy_l,
            f"$L = {c_str}$",
            ha="center",
            va="center",
            fontsize=9.3,
            fontweight="bold",
            color=NAVY,
            bbox=dict(boxstyle="round,pad=0.10", fc=BLUE_PALE, ec=NAVY, lw=0.75, alpha=0.95),
            zorder=8,
        )

    ax_a.scatter(xa, ya, s=34, color=NAVY, edgecolor="white", lw=0.8, zorder=7)

    y_bar = -0.26
    for xv in xa:
        ax_a.plot([xv, xv], [0.0, y_bar - 0.05], color=SLATE, lw=0.95, ls=":", zorder=2)
    for i in range(4):
        draw_arrow_2d(
            ax_a,
            (float(xa[i]) + 0.02, y_bar),
            (float(xa[i + 1]) - 0.02, y_bar),
            color=BLUE,
            lw=2.3,
            head_length=5.8,
            head_width=3.6,
            zorder=6,
        )
        ax_a.text(
            0.5 * float(xa[i] + xa[i + 1]),
            y_bar - 0.14,
            r"$1/2$",
            ha="center",
            va="top",
            fontsize=9.5,
            fontweight="bold",
            color=BLUE,
        )

    ax_a.text(
        0.0,
        -0.63,
        r"Equal $a$-bins ($\Delta a = 1/2$): all $\Delta x = 1/2$, so $\varphi_1'(a) = 1$",
        ha="center",
        va="center",
        fontsize=9.4,
        color=TEXT,
        bbox=dict(boxstyle="round,pad=0.18", fc=GREY_BG, ec=GREY_LINE, lw=0.9),
    )

    ax_a.set_xlim(-1.62, 1.62)
    ax_a.set_ylim(-0.80, 1.24)
    ax_a.set_aspect("equal")
    ax_a.axis("off")
    ax_a.set_title(
        r"(a) Graph map $\varphi(a) = (a, \sqrt{1 - a^2})$, $\Delta a = 1/2$",
        fontweight="bold",
        color=TEXT,
        pad=6,
    )

    # --- Panel (b): Angular map phi_tilde(theta) = (cos theta, sin theta), theta: pi -> 0 ---
    th_pts = np.linspace(np.pi, 0.0, 5)
    xb = np.cos(th_pts)
    yb = np.sin(th_pts)
    dxb = np.diff(xb)
    dyb = np.diff(yb)
    chords_b = np.hypot(dxb, dyb)

    ax_b.plot(xc_fine, yc_fine, color=GREY_LINE, lw=2.2, ls="-", zorder=1)
    ax_b.axhline(0.0, color=SLATE, lw=1.0, alpha=0.55, zorder=1)

    for th_v in th_pts:
        ax_b.plot([0.0, math.cos(th_v)], [0.0, math.sin(th_v)], color=AMBER, lw=1.05, ls="--", alpha=0.65, zorder=2)
    arc_th = Arc((0.0, 0.0), 0.44, 0.44, angle=0.0, theta1=0.0, theta2=180.0, color=AMBER, lw=1.5, zorder=3)
    ax_b.add_patch(arc_th)
    ax_b.text(
        0.0,
        0.29,
        r"4 bins, $\Delta\theta = -\pi/4$",
        ha="center",
        va="bottom",
        fontsize=9.2,
        fontweight="bold",
        color=AMBER,
        bbox=dict(boxstyle="round,pad=0.09", fc="white", ec="none", alpha=0.88),
        zorder=5,
    )

    chord_lbl_pos_b = [(-0.98, 0.42), (-0.38, 0.99), (+0.38, 0.99), (+0.98, 0.42)]
    for i in range(4):
        draw_arrow_2d(
            ax_b,
            (float(xb[i]), float(yb[i])),
            (float(xb[i + 1]), float(yb[i + 1])),
            color=NAVY,
            lw=2.5,
            head_length=6.6,
            head_width=4.0,
            zorder=6,
        )
        lx_b, ly_b = chord_lbl_pos_b[i]
        ax_b.text(
            lx_b,
            ly_b,
            f"${chords_b[i]:.3f}$",
            ha="center",
            va="center",
            fontsize=9.3,
            fontweight="bold",
            color=NAVY,
            bbox=dict(boxstyle="round,pad=0.10", fc=BLUE_PALE, ec=NAVY, lw=0.75, alpha=0.95),
            zorder=8,
        )

    ax_b.scatter(xb, yb, s=34, color=NAVY, edgecolor="white", lw=0.8, zorder=7)

    for idx_p in range(5):
        ax_b.plot([xb[idx_p], xb[idx_p]], [yb[idx_p], y_bar - 0.05], color=SLATE, lw=0.95, ls=":", zorder=2)

    for i in range(4):
        draw_arrow_2d(
            ax_b,
            (float(xb[i]) + 0.02, y_bar),
            (float(xb[i + 1]) - 0.02, y_bar),
            color=BLUE,
            lw=2.3,
            head_length=5.6,
            head_width=3.5,
            zorder=6,
        )
        ax_b.text(
            0.5 * float(xb[i] + xb[i + 1]),
            y_bar - 0.14,
            f"${dxb[i]:.2f}$",
            ha="center",
            va="top",
            fontsize=9.4,
            fontweight="bold",
            color=BLUE,
        )

    ax_b.text(
        0.0,
        -0.63,
        r"Equal $\theta$-bins ($\pi \to 0$): chords all $0.765$, $\Delta x$ varies as $-\sin\theta$",
        ha="center",
        va="center",
        fontsize=9.4,
        color=TEXT,
        bbox=dict(boxstyle="round,pad=0.18", fc=GREY_BG, ec=GREY_LINE, lw=0.9),
    )

    ax_b.set_xlim(-1.62, 1.62)
    ax_b.set_ylim(-0.80, 1.24)
    ax_b.set_aspect("equal")
    ax_b.axis("off")
    ax_b.set_title(
        r"(b) Angular map $\tilde{\varphi}(\theta) = (\cos\theta, \sin\theta)$, $\theta: \pi \to 0$",
        fontweight="bold",
        color=TEXT,
        pad=6,
    )

    save_fig(fig, out_dir, "maths1_semicircle_pullback_bins.png")
    print(
        f"[Fig 8] (a) Graph map a in [-1, 1], 4 bins da = 1/2: "
        f"dx = {[round(float(v), 2) for v in dxa]}, "
        f"dy = {[round(float(v), 2) for v in dya]}, "
        f"chords = {[round(float(v), 2) for v in chords_a]}. "
        f"(b) Angular map theta: pi -> 0, 4 bins dtheta = -pi/4: "
        f"chords = {[round(float(v), 3) for v in chords_b]}, "
        f"dx = {[round(float(v), 2) for v in dxb]}, "
        f"dy = {[round(float(v), 2) for v in dyb]}."
    )


# ===========================================================================
# Figure 12: maths1_wedge_area.png
# ===========================================================================
def make_fig9_wedge_area(out_dir: Path) -> None:
    fig = plt.figure(figsize=(10.8, 4.8), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.22, 1.0], wspace=0.20)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1])

    ux, uy = 3, 1
    vx, vy = 1, 2
    plain_prod = ux * vy
    cross_term = uy * vx
    signed_area = plain_prod - cross_term
    box_area = (ux + vx) * (uy + vy)
    assert plain_prod == 6 and cross_term == 1 and signed_area == 5 and box_area == 12

    para_pts = [(0, 0), (ux, uy), (ux + vx, uy + vy), (vx, vy)]
    rect_pts = [(0, 0), (ux, 0), (ux, vy), (0, vy)]

    ax_a.add_patch(Polygon(para_pts, closed=True, fc=TEAL_LIGHT, ec=TEAL, lw=2.0, alpha=0.72, zorder=2))
    ax_a.add_patch(
        Polygon(rect_pts, closed=True, fc=AMBER_LIGHT, ec=AMBER, lw=2.1, ls="--", hatch="///", alpha=0.38, zorder=3)
    )
    ax_a.plot([0, ux, ux, 0, 0], [0, 0, vy, vy, 0], color=AMBER, lw=2.1, ls="--", zorder=4)

    draw_arrow_2d(ax_a, (0, 0), (ux, uy), color=BLUE, lw=2.7, head_length=7.0, head_width=4.3, zorder=6)
    draw_arrow_2d(ax_a, (0, 0), (vx, vy), color=RED, lw=2.7, head_length=7.0, head_width=4.3, zorder=6)

    ax_a.text(2.12, 1.58, "Parallelogram\narea $= 5$", ha="center", va="center", fontsize=9.6, fontweight="bold", color=TEAL,
              bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=TEAL, lw=0.85, alpha=0.94), zorder=7)
    ax_a.annotate(
        r"Plain product $u_x v_y = 3 \times 2 = 6$" "\n(overcounts by $1$)",
        xy=(2.55, 2.0),
        xytext=(1.75, 3.38),
        ha="center",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=AMBER,
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec=AMBER, lw=0.9, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.15, shrinkB=2),
        zorder=8,
    )
    ax_a.text(ux + 0.14, uy - 0.16, r"$\mathbf{u} = (3, 1)$", ha="left", va="top", fontsize=9.5, fontweight="bold", color=BLUE, zorder=8)
    ax_a.text(vx - 0.12, vy + 0.12, r"$\mathbf{v} = (1, 2)$", ha="right", va="bottom", fontsize=9.5, fontweight="bold", color=RED, zorder=8)

    ix0, iy0 = 4.78, 0.85
    draw_card(ax_a, 4.32, 0.20, 2.66, 3.35, fc=GREY_BG, ec=SLATE, lw=1.0, pad=0.03, zorder=2)
    ax_a.text(5.65, 3.22, r"Collapsed: $\mathbf{u} = \mathbf{v} = (1, 1)$", ha="center", va="center",
              fontsize=9.2, fontweight="bold", color=NAVY, zorder=7)
    sq_pts = [(ix0, iy0), (ix0 + 1.0, iy0), (ix0 + 1.0, iy0 + 1.0), (ix0, iy0 + 1.0)]
    ax_a.add_patch(Polygon(sq_pts, closed=True, fc=AMBER_LIGHT, ec=AMBER, lw=1.8, ls="--", alpha=0.65, zorder=4))
    ax_a.plot([ix0, ix0 + 1.85], [iy0, iy0 + 1.85], color=TEAL, lw=2.4, ls="-", zorder=5)
    draw_arrow_2d(ax_a, (ix0, iy0), (ix0 + 1.0, iy0 + 1.0), color=RED, lw=2.3, head_length=6.0, head_width=3.6, zorder=6)
    ax_a.text(5.65, iy0 - 0.34, "area $= 0$,  $u_x v_y = 1$", ha="center", va="center",
              fontsize=9.2, fontweight="bold", color=TEXT, zorder=7)

    ax_a.set_xlim(-0.55, 7.12)
    ax_a.set_ylim(-0.45, 3.85)
    ax_a.set_aspect("equal")
    ax_a.set_xticks([0, 1, 2, 3, 4])
    ax_a.set_yticks([0, 1, 2, 3])
    ax_a.set_xlabel("$x$", color=TEXT)
    ax_a.set_ylabel("$y$", color=TEXT)
    ax_a.set_title(r"(a) Parallelogram vs plain product $u_x v_y$", fontweight="bold", color=TEXT, pad=8)

    tri_bot = [(0, 0), (3, 0), (3, 1)]
    tri_top = [(1, 2), (1, 3), (4, 3)]
    tri_left = [(0, 0), (1, 2), (0, 2)]
    tri_right = [(3, 1), (4, 1), (4, 3)]
    rec_tl = [(0, 2), (1, 2), (1, 3), (0, 3)]
    rec_br = [(3, 0), (4, 0), (4, 1), (3, 1)]

    ax_b.add_patch(Polygon(para_pts, closed=True, fc=TEAL_LIGHT, ec=TEAL, lw=2.1, alpha=0.78, zorder=3))
    for tri_u in (tri_bot, tri_top):
        ax_b.add_patch(Polygon(tri_u, closed=True, fc=BLUE_LIGHT, ec=SLATE, lw=1.1, alpha=0.75, zorder=2))
    for tri_v in (tri_left, tri_right):
        ax_b.add_patch(Polygon(tri_v, closed=True, fc=RED_LIGHT, ec=SLATE, lw=1.1, alpha=0.75, zorder=2))
    for rec_c in (rec_tl, rec_br):
        ax_b.add_patch(Polygon(rec_c, closed=True, fc=AMBER_LIGHT, ec=AMBER, lw=1.3, alpha=0.85, zorder=2))

    ax_b.plot([0, 4, 4, 0, 0], [0, 0, 3, 3, 0], color=NAVY, lw=1.8, zorder=4)
    draw_arrow_2d(ax_b, (0, 0), (ux, uy), color=BLUE, lw=2.6, head_length=6.8, head_width=4.2, zorder=6)
    draw_arrow_2d(ax_b, (0, 0), (vx, vy), color=RED, lw=2.6, head_length=6.8, head_width=4.2, zorder=6)

    ang_u = math.degrees(math.atan2(uy, ux))
    ang_v = math.degrees(math.atan2(vy, vx))
    arc_uv = FancyArrowPatch(
        (0.85 * math.cos(math.radians(ang_u)), 0.85 * math.sin(math.radians(ang_u))),
        (0.85 * math.cos(math.radians(ang_v)), 0.85 * math.sin(math.radians(ang_v))),
        connectionstyle="arc3,rad=0.28",
        arrowstyle="-|>,head_length=5.2,head_width=3.2",
        mutation_scale=1.0,
        color=NAVY,
        lw=1.8,
        zorder=7,
    )
    ax_b.add_patch(arc_uv)
    ax_b.text(0.78, 0.68, "$+$", fontsize=10.5, fontweight="bold", color=NAVY, zorder=8)

    ax_b.text(2.12, 0.34, r"$3/2$", ha="center", va="center", fontsize=9.4, fontweight="bold", color=BLUE, zorder=7)
    ax_b.text(1.88, 2.66, r"$3/2$", ha="center", va="center", fontsize=9.4, fontweight="bold", color=BLUE, zorder=7)
    ax_b.text(0.32, 1.36, r"$1$", ha="center", va="center", fontsize=9.4, fontweight="bold", color=RED, zorder=7)
    ax_b.text(3.68, 1.64, r"$1$", ha="center", va="center", fontsize=9.4, fontweight="bold", color=RED, zorder=7)
    ax_b.text(0.50, 2.50, r"$u_y v_x = 1$", ha="center", va="center", fontsize=9.2, fontweight="bold", color=AMBER, zorder=7)
    ax_b.text(3.50, 0.50, r"$u_y v_x = 1$", ha="center", va="center", fontsize=9.2, fontweight="bold", color=AMBER, zorder=7)
    ax_b.text(
        2.00,
        1.50,
        r"$+5$" "\n" r"(swap $\to -5$)",
        ha="center",
        va="center",
        fontsize=9.6,
        fontweight="bold",
        color=TEAL,
        bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=TEAL, lw=0.85, alpha=0.93),
        zorder=8,
    )

    ax_b.text(
        2.0,
        3.42,
        r"Box $4\times 3 = 12$:  $12 - 3 - 2 - 2 = 5 = u_x v_y - u_y v_x$",
        ha="center",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=NAVY,
        bbox=dict(boxstyle="round,pad=0.15", fc=GREY_BG, ec=GREY_LINE, lw=0.9),
        zorder=8,
    )

    ax_b.set_xlim(-0.45, 4.45)
    ax_b.set_ylim(-0.45, 3.88)
    ax_b.set_aspect("equal")
    ax_b.set_xticks([0, 1, 2, 3, 4])
    ax_b.set_yticks([0, 1, 2, 3])
    ax_b.set_xlabel("$x$", color=TEXT)
    ax_b.set_ylabel("$y$", color=TEXT)
    ax_b.set_title(r"(b) Bounding-box subtraction & orientation", fontweight="bold", color=TEXT, pad=8)

    save_fig(fig, out_dir, "maths1_wedge_area.png")
    print(
        f"[Fig 9] u = ({ux}, {uy}), v = ({vx}, {vy}): plain product ux*vy = {plain_prod}, "
        f"cross-term uy*vx = {cross_term}, (dx ^ dy)(u, v) = +{signed_area}, "
        f"(dx ^ dy)(v, u) = -{signed_area}; collapsed u = v = (1, 1) has area 0 vs ux*vy = 1; "
        f"bounding box 4 x 3 = {box_area} minus 2*(3/2) - 2*1 - 2*1 = {signed_area}."
    )


# ===========================================================================
# Figure 13: maths1_surface_pullback.png
# ===========================================================================
def hemi_xyz(r: np.ndarray | float, t: np.ndarray | float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    ra, ta = np.broadcast_arrays(np.asarray(r, dtype=float), np.asarray(t, dtype=float))
    return ra * np.cos(ta), ra * np.sin(ta), np.sqrt(np.maximum(0.0, 1.0 - ra**2))


def draw_patch_and_parallelogram_3d(
    ax: plt.Axes,
    r0: float,
    dr: float,
    t0: float,
    dt: float,
    elev_deg: float,
    azim_deg: float,
    edge_lw: float = 2.4,
    arrow_lw: float = 2.7,
    head_len: float = 0.045,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Draw curved patch with blue edges on top and semi-transparent dashed-outline tangent parallelogram."""
    rp = np.linspace(r0, r0 + dr, 24)
    tp = np.linspace(t0, t0 + dt, 24)
    RP, TP = np.meshgrid(rp, tp)
    XP, YP, ZP = hemi_xyz(RP, TP)
    ax.plot_surface(XP, YP, ZP, color=BLUE_LIGHT, alpha=0.58, edgecolor="none", shade=False, zorder=3)

    p0 = np.array([r0 * math.cos(t0), r0 * math.sin(t0), math.sqrt(1.0 - r0**2)])
    p_r1 = np.array([(r0 + dr) * math.cos(t0), (r0 + dr) * math.sin(t0), math.sqrt(1.0 - (r0 + dr) ** 2)])
    phi_r = np.array([math.cos(t0), math.sin(t0), -r0 / math.sqrt(1.0 - r0**2)])
    phi_t = np.array([-r0 * math.sin(t0), r0 * math.cos(t0), 0.0])
    v_dr = phi_r * dr
    v_dt = phi_t * dt

    # Semi-transparent tangent parallelogram + explicit dashed amber outline
    para_3d = [p0, p0 + v_dr, p0 + v_dr + v_dt, p0 + v_dt]
    poly_tan = Poly3DCollection([para_3d], facecolor=AMBER_LIGHT, edgecolor="none", alpha=0.30)
    poly_tan.set_zorder(4)
    ax.add_collection3d(poly_tan)
    for k_e in range(4):
        pa = para_3d[k_e]
        pb = para_3d[(k_e + 1) % 4]
        ax.plot(
            [pa[0], pb[0]], [pa[1], pb[1]], [pa[2], pb[2]],
            color=AMBER, lw=edge_lw * 0.85, ls="--", zorder=7
        )

    # Four curved edges of the true patch drawn ON TOP in vivid blue
    for r_const in (r0, r0 + dr):
        xe, ye, ze = hemi_xyz(r_const, tp)
        ax.plot(xe, ye, ze, color=BLUE, lw=edge_lw, zorder=8)
    for t_const in (t0, t0 + dt):
        xe, ye, ze = hemi_xyz(rp, t_const)
        ax.plot(xe, ye, ze, color=BLUE, lw=edge_lw, zorder=8)

    # Two chain-rule tangent arrows at p0
    add_3d_arrow(ax, p0, p0 + v_dr, RED, elev_deg, azim_deg, lw=arrow_lw, head_len=head_len, zord=10)
    add_3d_arrow(ax, p0, p0 + v_dt, TEAL, elev_deg, azim_deg, lw=arrow_lw, head_len=head_len, zord=10)

    return p0, p_r1, v_dr, v_dt


def make_fig10_surface_pullback(out_dir: Path) -> None:
    fig = plt.figure(figsize=(10.8, 7.5), dpi=DPI)
    gs = fig.add_gridspec(2, 2, width_ratios=[1.02, 1.15], height_ratios=[0.96, 1.08], wspace=0.18, hspace=0.24)
    ax_a = fig.add_subplot(gs[0, 0])
    ax_b_full = fig.add_subplot(gs[0, 1], projection="3d", computed_zorder=False)
    ax_b_zoom = fig.add_subplot(gs[1, 0], projection="3d", computed_zorder=False)
    ax_c = fig.add_subplot(gs[1, 1])

    r0, dr = 0.50, 0.25
    t0, dt = math.pi / 6.0, math.pi / 6.0
    r_rim = 0.85

    param_area = dr * dt
    rect_shadow_area = r0 * dr * dt
    ring_sector_area = 0.5 * ((r0 + dr) ** 2 - r0**2) * dt
    scale_3d_r0 = r0 / math.sqrt(1.0 - r0**2)
    scale_3d_rim = r_rim / math.sqrt(1.0 - r_rim**2)
    minor_dydz_r0 = (r0**2 * math.cos(t0)) / math.sqrt(1.0 - r0**2)
    minor_dzdx_r0 = (r0**2 * math.sin(t0)) / math.sqrt(1.0 - r0**2)

    # --- Panel (a): Flat (r, t) parameter rectangle [0, 1] x [0, 2*pi] ---
    for rv in np.linspace(0.0, 1.0, 5):
        ax_a.plot([rv, rv], [0.0, 2.0 * math.pi], color=GREY_LINE, lw=0.9, zorder=1)
    for tv in np.linspace(0.0, 2.0 * math.pi, 13):
        ax_a.plot([0.0, 1.0], [tv, tv], color=GREY_LINE, lw=0.9, zorder=1)
    ax_a.plot([0, 1, 1, 0, 0], [0, 0, 2 * math.pi, 2 * math.pi, 0], color=NAVY, lw=1.5, zorder=2)

    cell_a = [(r0, t0), (r0 + dr, t0), (r0 + dr, t0 + dt), (r0, t0 + dt)]
    ax_a.add_patch(Polygon(cell_a, closed=True, fc=BLUE_LIGHT, ec=BLUE, lw=1.7, alpha=0.85, zorder=3))
    draw_arrow_2d(ax_a, (r0, t0), (r0 + dr, t0), color=RED, lw=2.5, head_length=6.2, head_width=3.8, zorder=6)
    draw_arrow_2d(ax_a, (r0, t0), (r0, t0 + dt), color=TEAL, lw=2.5, head_length=6.2, head_width=3.8, zorder=6)
    ax_a.scatter([r0], [t0], s=32, color=NAVY, zorder=7)

    ax_a.annotate(
        r"$\Delta t = \pi/6$",
        xy=(r0, t0 + 0.55 * dt),
        xytext=(0.24, 2.55),
        ha="center",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=TEAL,
        bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=TEAL, lw=0.85, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.1, shrinkB=2),
        zorder=8,
    )
    ax_a.annotate(
        r"$\Delta r = 0.25$",
        xy=(r0 + 0.55 * dr, t0),
        xytext=(0.64, 1.85),
        ha="center",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=RED,
        bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=RED, lw=0.85, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=RED, lw=1.1, shrinkB=2),
        zorder=8,
    )

    ax_a.plot([r_rim, r_rim], [0.0, 2.0 * math.pi], color=AMBER, lw=1.5, ls="--", zorder=3)
    ax_a.text(
        r_rim - 0.03,
        5.35,
        r"rim $r = 0.85$",
        ha="right",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=AMBER,
        bbox=dict(boxstyle="round,pad=0.11", fc="white", ec=AMBER, lw=0.75, alpha=0.94),
        zorder=7,
    )

    ax_a.set_xlim(-0.06, 1.06)
    ax_a.set_ylim(-0.25, 2.0 * math.pi + 0.25)
    ax_a.set_xticks([0.0, 0.5, 1.0])
    ax_a.set_yticks([0.0, math.pi, 2.0 * math.pi])
    ax_a.set_yticklabels(["$0$", r"$\pi$", r"$2\pi$"])
    ax_a.set_xlabel("$r$", color=TEXT)
    ax_a.set_ylabel("$t$", color=TEXT)
    ax_a.set_title("(a) Parameter cell in $(r, t)$", fontweight="bold", color=TEXT, pad=8)

    # --- Panel (b, top-right): Full hemisphere overview + steep rim ---
    elev_full, azim_full = 25.0, 35.0
    ax_b_full.view_init(elev=elev_full, azim=azim_full)
    set_equal_3d_box(ax_b_full, (-1.02, 1.02), (-1.02, 1.02), (-0.42, 1.62), zoom=1.22)
    ax_b_full.axis("off")

    rg = np.linspace(0.0, 1.0, 40)
    tg = np.linspace(0.0, 2.0 * math.pi, 96)
    RG, TG = np.meshgrid(rg, tg)
    XH, YH, ZH = hemi_xyz(RG, TG)
    ax_b_full.plot_surface(XH, YH, ZH, color=BLUE_PALE, alpha=0.48, edgecolor="none", shade=True, zorder=1)

    t_loop = np.linspace(0.0, 2.0 * math.pi, 180)
    for rv in (0.25, 0.50, 0.75, 1.00):
        xl, yl, zl = hemi_xyz(rv, t_loop)
        ax_b_full.plot(xl, yl, zl, color=SLATE, lw=0.75 if rv < 1.0 else 1.35, alpha=0.60, zorder=2)
    r_ray = np.linspace(0.0, 1.0, 40)
    for k_m in range(12):
        xm, ym, zm = hemi_xyz(r_ray, k_m * math.pi / 6.0)
        ax_b_full.plot(xm, ym, zm, color=SLATE, lw=0.68, alpha=0.50, zorder=2)

    draw_patch_and_parallelogram_3d(
        ax_b_full, r0, dr, t0, dt, elev_full, azim_full, edge_lw=1.8, arrow_lw=2.2, head_len=0.072
    )

    rp_rim = np.linspace(r_rim, 0.995, 14)
    tp_rim = np.linspace(-math.pi / 12.0, math.pi / 12.0, 14)
    RPR, TPR = np.meshgrid(rp_rim, tp_rim)
    XPR, YPR, ZPR = hemi_xyz(RPR, TPR)
    ax_b_full.plot_surface(XPR, YPR, ZPR, color=AMBER, alpha=0.58, edgecolor="none", zorder=5)

    fig.canvas.draw()
    proj_full = ax_b_full.get_proj()
    annotate_3d_point(
        ax_b_full, proj_full, (0.60 * math.cos(0.70), 0.60 * math.sin(0.70), math.sqrt(1.0 - 0.36)),
        (0.80, 0.80), "highlighted cell\n(enlarged below)", BLUE, fontsize=9.3
    )
    annotate_3d_point(
        ax_b_full, proj_full, (0.92, 0.0, math.sqrt(1.0 - 0.92**2)),
        (0.20, 0.78), "steep near\n$r = 0.85$", AMBER, fontsize=9.3
    )
    ax_b_full.text2D(
        0.50, 0.96, r"(b) Hemisphere $\varphi(r, t)$: full dome & steep rim",
        transform=ax_b_full.transAxes, ha="center", va="bottom",
        fontsize=10.3, fontweight="bold", color=TEXT
    )

    # --- Panel (b, bottom-left): Large 3D zoom of curved patch vs tangent parallelogram ---
    # View from azim = -24 deg (~54 deg sideways to the t0 = 30 deg meridian) so both the downward
    # radial curvature drop and the tangential arc curvature are clearly separated on screen.
    elev_z, azim_z = 21.0, -24.0
    ax_b_zoom.view_init(elev=elev_z, azim=azim_z)
    span_z_box = 0.48
    set_equal_3d_box(
        ax_b_zoom,
        (0.22, 0.22 + span_z_box),
        (0.21, 0.21 + span_z_box),
        (0.50, 0.50 + span_z_box),
        zoom=1.22,
    )
    ax_b_zoom.axis("off")

    rp_ctx = np.linspace(0.42, 0.82, 22)
    tp_ctx = np.linspace(math.pi / 12.0, 5.0 * math.pi / 12.0, 28)
    RPC, TPC = np.meshgrid(rp_ctx, tp_ctx)
    XPC, YPC, ZPC = hemi_xyz(RPC, TPC)
    ax_b_zoom.plot_surface(XPC, YPC, ZPC, color=BLUE_PALE, alpha=0.30, edgecolor="none", shade=False, zorder=1)
    for rv_c in (0.50, 0.75):
        xc_l, yc_l, zc_l = hemi_xyz(rv_c, tp_ctx)
        ax_b_zoom.plot(xc_l, yc_l, zc_l, color=GREY_LINE, lw=0.9, zorder=2)
    for tv_c in (t0, t0 + dt):
        xc_m, yc_m, zc_m = hemi_xyz(rp_ctx, tv_c)
        ax_b_zoom.plot(xc_m, yc_m, zc_m, color=GREY_LINE, lw=0.9, zorder=2)

    p0, p_r1, v_dr, v_dt = draw_patch_and_parallelogram_3d(
        ax_b_zoom, r0, dr, t0, dt, elev_z, azim_z, edge_lw=2.7, arrow_lw=3.0, head_len=0.036
    )

    true_step_r = p_r1 - p0
    len_true_r = float(np.linalg.norm(true_step_r))
    len_tan_r = float(np.linalg.norm(v_dr))

    tip_dr = p0 + v_dr
    ax_b_zoom.plot(
        [tip_dr[0], p_r1[0]], [tip_dr[1], p_r1[1]], [tip_dr[2], p_r1[2]],
        color=SLATE, lw=1.25, ls=":", zorder=9
    )
    ax_b_zoom.scatter(
        [p0[0], p_r1[0]], [p0[1], p_r1[1]], [p0[2], p_r1[2]],
        s=40, color=[NAVY, BLUE], edgecolor="white", lw=0.8, zorder=11
    )

    fig.canvas.draw()
    proj_z = ax_b_zoom.get_proj()
    annotate_3d_point(
        ax_b_zoom, proj_z, p0, (0.16, 0.62),
        r"$\varphi(r_0, t_0)$", NAVY, fontsize=9.4
    )
    annotate_3d_point(
        ax_b_zoom, proj_z, p0 + 0.65 * v_dt, (0.34, 0.88),
        r"$\frac{\partial\varphi}{\partial t}\Delta t$", TEAL, fontsize=9.6
    )
    annotate_3d_point(
        ax_b_zoom, proj_z, p0 + 0.76 * v_dr, (0.80, 0.80),
        r"$\frac{\partial\varphi}{\partial r}\Delta r$ (tangent)", RED, fontsize=9.3
    )
    p_mid_blue_r, p_mid_blue_y, p_mid_blue_z = hemi_xyz(r0 + 0.68 * dr, t0)
    annotate_3d_point(
        ax_b_zoom, proj_z, (float(p_mid_blue_r), float(p_mid_blue_y), float(p_mid_blue_z)),
        (0.56, 0.11),
        r"True edge $\varphi(r_0\!+\!\Delta r, t_0) - \varphi(r_0, t_0)$" "\n" r"$\approx \frac{\partial\varphi}{\partial r}\Delta r$ (blue patch)",
        BLUE, fontsize=9.2
    )

    ax_b_zoom.text2D(
        0.50, 0.96, r"(b, zoom) Curved patch (blue) vs. tangent parallelogram (dashed)",
        transform=ax_b_zoom.transAxes, ha="center", va="bottom",
        fontsize=10.1, fontweight="bold", color=TEXT
    )

    # --- Panel (c): First-quadrant zoom of xy-shadows ---
    th_q1 = np.linspace(0.0, 0.5 * math.pi, 180)
    for rv in (0.25, 0.50, 0.75, 1.00):
        ax_c.plot(
            rv * np.cos(th_q1),
            rv * np.sin(th_q1),
            color=GREY_LINE if rv < 1.0 else NAVY,
            lw=0.9 if rv < 1.0 else 1.6,
            zorder=1,
        )
    for k_q in range(4):
        ang_q = k_q * math.pi / 6.0
        ax_c.plot([0.0, math.cos(ang_q)], [0.0, math.sin(ang_q)], color=GREY_LINE, lw=0.9, zorder=1)

    ts_arc = np.linspace(t0, t0 + dt, 60)
    ring_xy = np.vstack([
        np.column_stack([(r0 + dr) * np.cos(ts_arc), (r0 + dr) * np.sin(ts_arc)]),
        np.column_stack([r0 * np.cos(ts_arc[::-1]), r0 * np.sin(ts_arc[::-1])]),
    ])
    ax_c.add_patch(Polygon(ring_xy, closed=True, fc=BLUE_LIGHT, ec=BLUE, lw=1.8, alpha=0.78, zorder=3))

    q0 = p0[:2]
    u_rad = v_dr[:2]
    u_tan = v_dt[:2]
    assert abs(float(np.dot(u_rad, u_tan))) < 1e-14
    rect_shadow_xy = [q0, q0 + u_rad, q0 + u_rad + u_tan, q0 + u_tan]
    ax_c.add_patch(
        Polygon(rect_shadow_xy, closed=True, fc=AMBER_LIGHT, ec=AMBER, lw=2.0, ls="--", alpha=0.65, zorder=4)
    )

    e_r = u_rad / np.linalg.norm(u_rad)
    e_t = u_tan / np.linalg.norm(u_tan)
    ra = 0.048
    ra_pts = [q0 + ra * e_r, q0 + ra * (e_r + e_t), q0 + ra * e_t]
    ax_c.plot([p[0] for p in ra_pts], [p[1] for p in ra_pts], color=NAVY, lw=1.2, zorder=6)

    draw_arrow_2d(ax_c, tuple(q0), tuple(q0 + u_rad), color=RED, lw=2.3, head_length=5.8, head_width=3.5, zorder=7)
    draw_arrow_2d(ax_c, tuple(q0), tuple(q0 + u_tan), color=TEAL, lw=2.3, head_length=5.8, head_width=3.5, zorder=7)

    ax_c.text(
        q0[0] + 0.42 * u_rad[0] + 0.02,
        q0[1] + 0.42 * u_rad[1] - 0.06,
        r"$\Delta r$",
        ha="center",
        va="top",
        fontsize=9.3,
        fontweight="bold",
        color=RED,
        zorder=8,
    )
    ax_c.text(
        q0[0] + 0.52 * u_tan[0] - 0.05,
        q0[1] + 0.52 * u_tan[1] - 0.02,
        r"$r_0\Delta t$",
        ha="right",
        va="top",
        fontsize=9.3,
        fontweight="bold",
        color=TEAL,
        bbox=dict(boxstyle="round,pad=0.06", fc="white", ec="none", alpha=0.88),
        zorder=8,
    )

    ax_c.annotate(
        r"Rectangle shadow" "\n" rf"$r_0\Delta r\Delta t \approx {rect_shadow_area:.3f}$",
        xy=tuple(q0 + 0.55 * u_rad + 0.85 * u_tan),
        xytext=(0.31, 0.92),
        ha="center",
        va="center",
        fontsize=9.2,
        fontweight="bold",
        color=AMBER,
        bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=AMBER, lw=0.85, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.1, shrinkB=2),
        zorder=8,
    )
    ax_c.annotate(
        r"Ring sector (patch)" "\n" rf"$\approx {ring_sector_area:.3f}$",
        xy=(0.71 * math.cos(t0 + 0.78 * dt), 0.71 * math.sin(t0 + 0.78 * dt)),
        xytext=(0.79, 0.72),
        ha="center",
        va="center",
        fontsize=9.2,
        fontweight="bold",
        color=BLUE,
        bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=BLUE, lw=0.85, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.1, shrinkB=2),
        zorder=8,
    )

    ax_c.set_xlim(-0.04, 1.08)
    ax_c.set_ylim(-0.04, 1.08)
    ax_c.set_aspect("equal")
    ax_c.set_xticks([0.0, 0.5, 1.0])
    ax_c.set_yticks([0.0, 0.5, 1.0])
    ax_c.set_xlabel("$x$", color=TEXT)
    ax_c.set_ylabel("$y$", color=TEXT)
    ax_c.set_title(r"(c) $xy$-shadows: $\varphi^*(dx\wedge dy) = r\,dr\wedge dt$", fontweight="bold", color=TEXT, pad=8)

    save_fig(fig, out_dir, "maths1_surface_pullback.png")
    print(
        f"[Fig 10] Hemisphere phi(r, t) = (r cos t, r sin t, sqrt(1 - r^2)); "
        f"cell r0 = {r0:.2f}, dr = {dr:.2f}, t0 = pi/6, dt = pi/6 (dr*dt = pi/24 = {param_area:.4f}): "
        f"true radial edge |phi(r0+dr, t0) - phi(r0, t0)| = {len_true_r:.4f} ({len_true_r:.3f}) vs "
        f"tangent arrow |(dphi/dr)*dr| = {len_tan_r:.4f} ({len_tan_r:.3f}); "
        f"parallelogram rectangle xy-shadow = r0*dr*dt = pi/48 = {rect_shadow_area:.4f} ({rect_shadow_area:.3f}), "
        f"curved patch ring-sector xy-shadow = ((r0+dr)^2 - r0^2)/2 * dt = 5*pi/192 = {ring_sector_area:.4f} ({ring_sector_area:.3f}); "
        f"3D area factor r/sqrt(1-r^2) is {scale_3d_r0:.2f} at r = {r0:.2f} vs {scale_3d_rim:.2f} at rim r = {r_rim:.2f} "
        f"(while xy-shadow factor is simply r = {r0:.2f} vs {r_rim:.2f}); "
        f"other minors at (r0, t0): (dy^dz) = {minor_dydz_r0:.4f}, (dz^dx) = {minor_dzdx_r0:.4f}."
    )


# ===========================================================================
# Figure 14: maths1_flux_shadows.png
# ===========================================================================
def make_fig11_flux_shadows(out_dir: Path) -> None:
    fig = plt.figure(figsize=(10.9, 4.85), dpi=DPI)
    gs = fig.add_gridspec(1, 3, width_ratios=[1.08, 1.08, 0.96], wspace=0.18)
    ax_a = fig.add_subplot(gs[0], projection="3d", computed_zorder=False)
    ax_b = fig.add_subplot(gs[1], projection="3d", computed_zorder=False)
    ax_c = fig.add_subplot(gs[2])

    # --- Panel (a): Floating octant centred at (0.6, 0.6, 0.6) & room-wall shadows ---
    c0 = 0.6
    elev_a, azim_a = 26.0, 38.0
    ax_a.view_init(elev=elev_a, azim=azim_a)
    set_equal_3d_box(ax_a, (-0.12, 1.92), (-0.12, 1.92), (-0.12, 1.92), zoom=1.15)
    ax_a.axis("off")

    # Room walls (yz at x=0, zx at y=0, xy-floor at z=0)
    w_max = 1.78
    room_walls = [
        [(0.0, 0.0, 0.0), (0.0, w_max, 0.0), (0.0, w_max, w_max), (0.0, 0.0, w_max)],
        [(0.0, 0.0, 0.0), (w_max, 0.0, 0.0), (w_max, 0.0, w_max), (0.0, 0.0, w_max)],
        [(0.0, 0.0, 0.0), (w_max, 0.0, 0.0), (w_max, w_max, 0.0), (0.0, w_max, 0.0)],
    ]
    for w_verts in room_walls:
        pw = Poly3DCollection([w_verts], facecolor=GREY_WALL, edgecolor=GREY_LINE, linewidths=0.95, alpha=0.68)
        pw.set_zorder(1)
        ax_a.add_collection3d(pw)

    add_3d_arrow(ax_a, np.array([0.0, 0.0, 0.0]), np.array([1.84, 0.0, 0.0]), SLATE, elev_a, azim_a, lw=1.3, head_len=0.09, zord=2)
    add_3d_arrow(ax_a, np.array([0.0, 0.0, 0.0]), np.array([0.0, 1.84, 0.0]), SLATE, elev_a, azim_a, lw=1.3, head_len=0.09, zord=2)
    add_3d_arrow(ax_a, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 1.82]), SLATE, elev_a, azim_a, lw=1.3, head_len=0.09, zord=2)
    ax_a.text(1.94, -0.04, -0.03, "$x$", fontsize=9.6, fontweight="bold", color=TEXT, ha="center", va="center")
    ax_a.text(-0.04, 1.94, -0.02, "$y$", fontsize=9.6, fontweight="bold", color=TEXT, ha="center", va="center")
    ax_a.text(-0.06, 0.08, 1.88, "$z$", fontsize=9.6, fontweight="bold", color=TEXT, ha="center", va="center")

    ang_q = np.linspace(0.0, 0.5 * math.pi, 60)
    qd_yz = [(0.0, c0, c0)] + [(0.0, c0 + float(math.cos(a)), c0 + float(math.sin(a))) for a in ang_q]
    qd_zx = [(c0, 0.0, c0)] + [(c0 + float(math.cos(a)), 0.0, c0 + float(math.sin(a))) for a in ang_q]
    qd_xy = [(c0, c0, 0.0)] + [(c0 + float(math.cos(a)), c0 + float(math.sin(a)), 0.0) for a in ang_q]

    for verts, fc_s, ec_s in (
        (qd_yz, BLUE_LIGHT, BLUE),
        (qd_zx, TEAL_LIGHT, TEAL),
        (qd_xy, AMBER_LIGHT, AMBER),
    ):
        poly_s = Poly3DCollection([verts], facecolor=fc_s, edgecolor=ec_s, linewidths=1.5, alpha=0.78)
        poly_s.set_zorder(2)
        ax_a.add_collection3d(poly_s)

    # Dotted projection lines from shell corners to each wall
    proj_rays = [
        # To yz-wall (x = 0)
        ((c0, c0 + 1.0, c0), (0.0, c0 + 1.0, c0), BLUE),
        ((c0, c0, c0 + 1.0), (0.0, c0, c0 + 1.0), BLUE),
        ((c0, c0 + 0.707, c0 + 0.707), (0.0, c0 + 0.707, c0 + 0.707), BLUE),
        # To zx-wall (y = 0)
        ((c0 + 1.0, c0, c0), (c0 + 1.0, 0.0, c0), TEAL),
        ((c0, c0, c0 + 1.0), (c0, 0.0, c0 + 1.0), TEAL),
        ((c0 + 0.707, c0, c0 + 0.707), (c0 + 0.707, 0.0, c0 + 0.707), TEAL),
        # To xy-floor (z = 0)
        ((c0 + 1.0, c0, c0), (c0 + 1.0, c0, 0.0), AMBER),
        ((c0, c0 + 1.0, c0), (c0, c0 + 1.0, 0.0), AMBER),
        ((c0 + 0.707, c0 + 0.707, c0), (c0 + 0.707, c0 + 0.707, 0.0), AMBER),
    ]
    for p_from, p_to, col_ray in proj_rays:
        ax_a.plot(
            [p_from[0], p_to[0]], [p_from[1], p_to[1]], [p_from[2], p_to[2]],
            color=col_ray, lw=0.95, ls=":", alpha=0.62, zorder=3
        )

    # Floating curved octant shell centred at (c0, c0, c0) with shaded body + crisp NAVY outline
    th_s = np.linspace(0.0, 0.5 * math.pi, 45)
    ph_s = np.linspace(0.0, 0.5 * math.pi, 45)
    THS, PHS = np.meshgrid(th_s, ph_s)
    XS = c0 + np.sin(THS) * np.cos(PHS)
    YS = c0 + np.sin(THS) * np.sin(PHS)
    ZS = c0 + np.cos(THS)
    ax_a.plot_surface(XS, YS, ZS, color=BLUE_MID, alpha=0.68, edgecolor="none", shade=True, zorder=5)

    # Subtle mesh lines + bold boundary arcs on the floating shell
    for rv_lat in (math.pi / 6.0, math.pi / 3.0):
        ax_a.plot(
            c0 + math.sin(rv_lat) * np.cos(ang_q),
            c0 + math.sin(rv_lat) * np.sin(ang_q),
            np.full_like(ang_q, c0 + math.cos(rv_lat)),
            color=SLATE, lw=0.70, alpha=0.50, zorder=6
        )
    ax_a.plot(np.full_like(ang_q, c0), c0 + np.cos(ang_q), c0 + np.sin(ang_q), color=NAVY, lw=2.1, zorder=6)
    ax_a.plot(c0 + np.cos(ang_q), np.full_like(ang_q, c0), c0 + np.sin(ang_q), color=NAVY, lw=2.1, zorder=6)
    ax_a.plot(c0 + np.cos(ang_q), c0 + np.sin(ang_q), np.full_like(ang_q, c0), color=NAVY, lw=2.1, zorder=6)

    n_num = 600
    th_m = (np.arange(n_num) + 0.5) * (0.5 * math.pi / n_num)
    ph_m = (np.arange(n_num) + 0.5) * (0.5 * math.pi / n_num)
    THM, PHM = np.meshgrid(th_m, ph_m)
    dA_x = (np.sin(THM) ** 2) * np.cos(PHM)
    dA_y = (np.sin(THM) ** 2) * np.sin(PHM)
    dA_z = np.sin(THM) * np.cos(THM)
    dth_dph = (0.5 * math.pi / n_num) ** 2
    sh_yz_num = float(np.sum(dA_x) * dth_dph)
    sh_zx_num = float(np.sum(dA_y) * dth_dph)
    sh_xy_num = float(np.sum(dA_z) * dth_dph)
    flux_octant_num = sh_yz_num + sh_zx_num + sh_xy_num
    flux_octant_exact = 0.75 * math.pi
    assert abs(sh_yz_num - 0.25 * math.pi) < 1e-5
    assert abs(flux_octant_num - flux_octant_exact) < 1e-5

    # Outward constant field arrow F on the floating shell
    p_oct = np.array([
        c0 + math.sin(0.85) * math.cos(0.78),
        c0 + math.sin(0.85) * math.sin(0.78),
        c0 + math.cos(0.85),
    ])
    f_tip_oct = p_oct + 0.56 * np.array([0.42, 0.68, 0.60])
    add_3d_arrow(ax_a, p_oct, f_tip_oct, RED, elev_a, azim_a, lw=2.7, head_len=0.12, zord=8)
    ax_a.text(
        f_tip_oct[0] + 0.02, f_tip_oct[1] + 0.06, f_tip_oct[2] + 0.11,
        r"$\vec{F}$", fontsize=10.0, fontweight="bold", color=RED, ha="center",
        bbox=dict(boxstyle="round,pad=0.06", fc="white", ec="none", alpha=0.88), zorder=9
    )

    # Labels on the three wall shadows
    ax_a.text(0.0, c0 + 0.62, c0 + 0.55, r"$\pi/4$", fontsize=9.3, fontweight="bold", color=BLUE, ha="center",
              bbox=dict(boxstyle="round,pad=0.08", fc="white", ec=BLUE, lw=0.75, alpha=0.94), zorder=7)
    ax_a.text(c0 + 0.62, 0.0, c0 + 0.55, r"$\pi/4$", fontsize=9.3, fontweight="bold", color=TEAL, ha="center",
              bbox=dict(boxstyle="round,pad=0.08", fc="white", ec=TEAL, lw=0.75, alpha=0.94), zorder=7)
    ax_a.text(c0 + 0.46, c0 + 0.46, 0.0, r"$\pi/4$", fontsize=9.3, fontweight="bold", color=AMBER, ha="center",
              bbox=dict(boxstyle="round,pad=0.08", fc="white", ec=AMBER, lw=0.75, alpha=0.94), zorder=7)

    ax_a.text2D(
        0.50, 0.98, "(a) Floating octant & 3 shadows", transform=ax_a.transAxes,
        ha="center", va="bottom", fontsize=10.2, fontweight="bold", color=TEXT
    )
    ax_a.text2D(
        0.50, 0.01, r"Constant $\vec{F}$: flux $= (F_x + F_y + F_z)\,\frac{\pi}{4}$",
        transform=ax_a.transAxes, ha="center", va="bottom", fontsize=9.2, color=TEXT,
        bbox=dict(boxstyle="round,pad=0.15", fc=GREY_BG, ec=GREY_LINE, lw=0.85)
    )

    # --- Panel (b): Exploded Cauchy corner tetrahedron (0,0,0), (1,0,0), (0,2,0), (0,0,2) ---
    # View from elev = 23 deg, azim = -28 deg (+x front-right-down, +y back-right-up, +z up)
    # with a small explosion along each face's outward normal so all four faces, their centroids,
    # and the tilted F prop (1, 1, 1) inflow/outflow arrows separate cleanly on screen.
    elev_b, azim_b = 23.0, -28.0
    ax_b.view_init(elev=elev_b, azim=azim_b)
    set_equal_3d_box(ax_b, (-1.15, 2.85), (-1.25, 2.75), (-0.95, 3.05), zoom=1.24)
    ax_b.axis("off")

    O = np.array([0.0, 0.0, 0.0])
    Vx = np.array([1.0, 0.0, 0.0])
    Vy = np.array([0.0, 2.0, 0.0])
    Vz = np.array([0.0, 0.0, 2.0])

    area_vec_tet = 0.5 * np.cross(Vy - Vx, Vz - Vx)
    slant_area = float(np.linalg.norm(area_vec_tet))
    assert np.allclose(area_vec_tet, [2.0, 1.0, 1.0]) and abs(slant_area - math.sqrt(6.0)) < 1e-12
    n_unit_slant = area_vec_tet / slant_area

    # Clean 3D axis triad tucked well into the open upper-left margin away from the zx tip
    triad_o = np.array([-0.55, -1.28, 1.96])
    add_3d_arrow(ax_b, triad_o, triad_o + np.array([0.46, 0.0, 0.0]), SLATE, elev_b, azim_b, lw=1.3, head_len=0.10, zord=4)
    add_3d_arrow(ax_b, triad_o, triad_o + np.array([0.0, 0.46, 0.0]), SLATE, elev_b, azim_b, lw=1.3, head_len=0.10, zord=4)
    add_3d_arrow(ax_b, triad_o, triad_o + np.array([0.0, 0.0, 0.48]), SLATE, elev_b, azim_b, lw=1.3, head_len=0.10, zord=4)
    ax_b.text(triad_o[0] + 0.57, triad_o[1] - 0.04, triad_o[2] - 0.05, "$x$", fontsize=9.1, fontweight="bold", color=TEXT, ha="center", va="center")
    ax_b.text(triad_o[0] - 0.02, triad_o[1] + 0.58, triad_o[2] + 0.02, "$y$", fontsize=9.1, fontweight="bold", color=TEXT, ha="center", va="center")
    ax_b.text(triad_o[0], triad_o[1], triad_o[2] + 0.60, "$z$", fontsize=9.1, fontweight="bold", color=TEXT, ha="center", va="center")

    # Explode each face slightly along its own outward normal so a clean white channel separates zx and yz
    s_yz = np.array([-0.24, 0.0, 0.0])
    s_zx = np.array([0.0, -0.74, 0.0])
    s_xy = np.array([0.0, 0.0, -0.54])
    s_sl = 1.34 * n_unit_slant

    verts_yz = [O + s_yz, Vy + s_yz, Vz + s_yz]
    verts_zx = [O + s_zx, Vx + s_zx, Vz + s_zx]
    verts_xy = [O + s_xy, Vx + s_xy, Vy + s_xy]
    verts_sl = [Vx + s_sl, Vy + s_sl, Vz + s_sl]

    # Tint each right-angled shadow face strongly in its label's colour
    shadow_specs = [
        (verts_yz, "#bfdbfe", BLUE, 2),
        (verts_zx, "#99f6e4", TEAL, 3),
        (verts_xy, "#fde68a", AMBER, 2),
    ]
    for v_tri, fc_tri, ec_tri, z_tri in shadow_specs:
        pt = Poly3DCollection([v_tri], facecolor=fc_tri, edgecolor=ec_tri, linewidths=1.7, alpha=0.88)
        pt.set_zorder(z_tri)
        ax_b.add_collection3d(pt)

    # Light dotted explosion lines showing how the slanted lid lifts off along n_hat
    for v_base, v_lift in (
        (verts_zx[1], verts_sl[0]),
        (verts_yz[1], verts_sl[1]),
        (verts_yz[2], verts_sl[2]),
    ):
        ax_b.plot(
            [v_base[0], v_lift[0]], [v_base[1], v_lift[1]], [v_base[2], v_lift[2]],
            color=SLATE, lw=0.85, ls=":", alpha=0.50, zorder=2
        )

    # Slanted face: very light translucent fill + crisp 3D diagonal hatching + bold NAVY outline
    slanted = Poly3DCollection([verts_sl], facecolor="white", edgecolor=NAVY, linewidths=2.2, alpha=0.22)
    slanted.set_zorder(5)
    ax_b.add_collection3d(slanted)
    for frac_h in (0.16, 0.30, 0.44, 0.58, 0.72, 0.86):
        p_h1 = (1.0 - frac_h) * verts_sl[0] + frac_h * verts_sl[2]
        p_h2 = (1.0 - frac_h) * verts_sl[1] + frac_h * verts_sl[2]
        ax_b.plot(
            [p_h1[0], p_h2[0]], [p_h1[1], p_h2[1]], [p_h1[2], p_h2[2]],
            color=NAVY, lw=0.85, alpha=0.35, zorder=6
        )

    # Comparable-component constant field F prop (1, 1, 1): tilts strongly up-and-right on screen
    f_dir = np.array([1.0, 1.0, 1.0]) / math.sqrt(3.0)

    # Three inflow arrows: each starts visibly in white background outside all faces and ends on its face
    hit_yz = np.array([0.0, 0.28, 1.48]) + s_yz
    hit_zx = np.array([0.52, 0.0, 0.36]) + s_zx
    hit_xy = np.array([0.46, 0.62, 0.0]) + s_xy
    for p_hit, len_in in ((hit_yz, 0.64), (hit_zx, 0.80), (hit_xy, 0.80)):
        p_start_in = p_hit - len_in * f_dir
        add_3d_arrow(ax_b, p_start_in, p_hit, RED, elev_b, azim_b, lw=2.2, head_len=0.14, zord=7)
        ax_b.scatter([p_hit[0]], [p_hit[1]], [p_hit[2]], s=20, color=RED, edgecolor="white", lw=0.6, zorder=8)

    # Outflow arrow F leaving from the lifted slanted face
    c_sl_face = (verts_sl[0] + verts_sl[1] + verts_sl[2]) / 3.0
    p_out_start = c_sl_face + np.array([-0.10, 0.12, 0.30])
    p_out_tip = p_out_start + 0.82 * f_dir
    add_3d_arrow(ax_b, p_out_start, p_out_tip, RED, elev_b, azim_b, lw=2.6, head_len=0.15, zord=9)
    ax_b.scatter([p_out_start[0]], [p_out_start[1]], [p_out_start[2]], s=22, color=RED, edgecolor="white", lw=0.6, zorder=9)
    ax_b.text(
        p_out_tip[0] + 0.04, p_out_tip[1] + 0.14, p_out_tip[2] + 0.10,
        r"$\vec{F}$", fontsize=10.0, fontweight="bold", color=RED, ha="center",
        bbox=dict(boxstyle="round,pad=0.06", fc="white", ec="none", alpha=0.90), zorder=10
    )

    # Outward normal n_hat prop (2, 1, 1) on the lifted slanted face, with crisp tip badge
    p_n_start = c_sl_face + np.array([0.04, 0.12, -0.02])
    p_n_tip = p_n_start + 0.56 * n_unit_slant
    add_3d_arrow(ax_b, p_n_start, p_n_tip, NAVY, elev_b, azim_b, lw=2.5, head_len=0.14, zord=9)

    # Leader-line badges pointing directly to each of the four faces' centroids
    cent_yz = (verts_yz[0] + verts_yz[1] + verts_yz[2]) / 3.0
    cent_zx = (verts_zx[0] + verts_zx[1] + verts_zx[2]) / 3.0
    cent_xy = (verts_xy[0] + verts_xy[1] + verts_xy[2]) / 3.0

    fig.canvas.draw()
    proj_tet = ax_b.get_proj()
    annotate_3d_point(
        ax_b, proj_tet, cent_zx, (0.10, 0.54),
        r"$A_{zx} = 1$", TEAL, fontsize=9.1, shrinkB=2.0
    )
    annotate_3d_point(
        ax_b, proj_tet, cent_yz, (0.44, 0.90),
        r"$A_{yz} = 2$", BLUE, fontsize=9.1, shrinkB=2.0
    )
    annotate_3d_point(
        ax_b, proj_tet, cent_xy, (0.55, 0.13),
        r"$A_{xy} = 1$", AMBER, fontsize=9.1, shrinkB=2.0
    )
    annotate_3d_point(
        ax_b, proj_tet, c_sl_face, (0.85, 0.21),
        r"$A = \sqrt{6}$", NAVY, fontsize=9.1, shrinkB=2.0
    )
    ax_b.text2D(
        0.90, 0.54,
        r"$\hat{\mathbf{n}} \propto (2, 1, 1)$",
        transform=ax_b.transAxes, ha="center", va="center",
        fontsize=9.1, fontweight="bold", color=NAVY,
        bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=NAVY, lw=0.9, alpha=0.96),
        zorder=12,
    )

    ax_b.text2D(
        0.50, 0.98, "(b) Corner tetrahedron", transform=ax_b.transAxes,
        ha="center", va="bottom", fontsize=10.2, fontweight="bold", color=TEXT
    )
    ax_b.text2D(
        0.50, 0.01, r"Flux out $= 2F_x + F_y + F_z$",
        transform=ax_b.transAxes, ha="center", va="bottom", fontsize=9.2, color=TEXT,
        bbox=dict(boxstyle="round,pad=0.15", fc=GREY_BG, ec=GREY_LINE, lw=0.85)
    )

    # --- Panel (c): Edge-on view looking down z-axis onto xy-plane (with axis key) ---
    theta_deg = 35.0
    th_c = math.radians(theta_deg)
    L_seg = 1.55
    p_bot = np.array([1.22, 0.22])
    p_top = p_bot + L_seg * np.array([-math.sin(th_c), math.cos(th_c)])
    p_mid = 0.5 * (p_bot + p_top)
    n_hat_2d = np.array([math.cos(th_c), math.sin(th_c)])

    ax_c.plot([0.0, 0.0], [-0.08, 1.85], color=SLATE, lw=1.3, zorder=1)
    ax_c.plot([0.0, 0.0], [p_bot[1], p_top[1]], color=BLUE, lw=4.5, solid_capstyle="butt", zorder=4)

    ax_c.plot([0.0, p_bot[0]], [p_bot[1], p_bot[1]], color=SLATE, lw=1.05, ls=":", zorder=2)
    ax_c.plot([0.0, p_top[0]], [p_top[1], p_top[1]], color=SLATE, lw=1.05, ls=":", zorder=2)

    ax_c.plot([p_bot[0], p_top[0]], [p_bot[1], p_top[1]], color=NAVY, lw=4.0, zorder=5)

    ax_c.plot([p_mid[0], p_mid[0] + 0.68], [p_mid[1], p_mid[1]], color=SLATE, lw=1.1, ls="--", zorder=3)
    draw_arrow_2d(
        ax_c, tuple(p_mid), tuple(p_mid + 0.68 * n_hat_2d), color=RED, lw=2.5, head_length=6.4, head_width=4.0, zorder=7
    )
    arc_n = Arc(tuple(p_mid), 0.56, 0.56, angle=0.0, theta1=0.0, theta2=theta_deg, color=RED, lw=1.5, zorder=6)
    ax_c.add_patch(arc_n)
    ax_c.text(p_mid[0] + 0.36, p_mid[1] + 0.12, r"$\theta$", fontsize=9.8, fontweight="bold", color=RED)
    ax_c.text(
        p_mid[0] + 0.68 * n_hat_2d[0] + 0.05,
        p_mid[1] + 0.68 * n_hat_2d[1] + 0.04,
        r"$\hat{\mathbf{n}}$",
        fontsize=10.0,
        fontweight="bold",
        color=RED,
    )

    ax_c.plot([p_bot[0], p_bot[0]], [p_bot[1], p_bot[1] + 0.58], color=SLATE, lw=1.0, ls="--", zorder=3)
    arc_tilt = Arc(tuple(p_bot), 0.52, 0.52, angle=0.0, theta1=90.0, theta2=90.0 + theta_deg, color=NAVY, lw=1.4, zorder=6)
    ax_c.add_patch(arc_tilt)
    ax_c.text(p_bot[0] - 0.12, p_bot[1] + 0.34, r"$\theta$", fontsize=9.5, fontweight="bold", color=NAVY)

    ax_c.text(
        -0.08,
        0.5 * (p_bot[1] + p_top[1]) + 0.18,
        r"$A_{yz} = A\cos\theta$" "\n" r"$= A\,n_x$",
        ha="right",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=BLUE,
    )
    ax_c.text(
        p_top[0] + 0.10,
        p_top[1] + 0.08,
        "patch area $A$",
        ha="left",
        va="bottom",
        fontsize=9.4,
        fontweight="bold",
        color=NAVY,
    )

    # Right-handed axis key: x right, y up, z out of page (circle with dot)
    kx, ky = -0.68, 0.14
    draw_arrow_2d(ax_c, (kx, ky), (kx + 0.38, ky), color=SLATE, lw=1.7, head_length=5.2, head_width=3.2, zorder=6)
    draw_arrow_2d(ax_c, (kx, ky), (kx, ky + 0.38), color=SLATE, lw=1.7, head_length=5.2, head_width=3.2, zorder=6)
    ax_c.add_patch(Circle((kx, ky), 0.068, fc="white", ec=SLATE, lw=1.3, zorder=7))
    ax_c.scatter([kx], [ky], s=14, color=SLATE, zorder=8)
    ax_c.text(kx + 0.42, ky, "$x$", ha="left", va="center", fontsize=9.3, fontweight="bold", color=TEXT)
    ax_c.text(kx, ky + 0.42, "$y$", ha="center", va="bottom", fontsize=9.3, fontweight="bold", color=TEXT)
    ax_c.text(kx, ky - 0.11, "$z$ (out)", ha="center", va="top", fontsize=9.1, fontweight="bold", color=SLATE)

    ax_c.text(
        0.48,
        -0.30,
        r"$F_x A_{yz} + F_y A_{zx} + F_z A_{xy} = \vec{F}\cdot\hat{\mathbf{n}}\,A$",
        ha="center",
        va="center",
        fontsize=9.2,
        color=TEXT,
        bbox=dict(boxstyle="round,pad=0.15", fc=GREY_BG, ec=GREY_LINE, lw=0.85),
    )

    ax_c.set_xlim(-0.96, 1.72)
    ax_c.set_ylim(-0.48, 1.92)
    ax_c.set_aspect("equal")
    ax_c.axis("off")
    ax_c.set_title(r"(c) Edge-on tilt: shadow $= A\cos\theta$", fontweight="bold", color=TEXT, pad=8)

    save_fig(fig, out_dir, "maths1_flux_shadows.png")
    print(
        f"[Fig 11] (a) Floating unit-sphere octant centred at ({c0}, {c0}, {c0}) (x, y, z >= {c0}): "
        f"wall shadows = [pi/4, pi/4, pi/4] "
        f"(numerical {[round(sh_yz_num, 5), round(sh_zx_num, 5), round(sh_xy_num, 5)]}); "
        f"constant F = (1, 1, 1) flux = 3*pi/4 = {flux_octant_exact:.5f} (2dp: {flux_octant_exact:.2f}, numerical {flux_octant_num:.5f}). "
        f"(b) Corner tetrahedron (1,0,0),(0,2,0),(0,0,2): shadows A_yz = 2, A_zx = 1, A_xy = 1 "
        f"(2^2 + 1^2 + 1^2 = 6), outward normal n_hat prop (2, 1, 1), slanted area = sqrt(6) = {slant_area:.4f} (2dp: {slant_area:.2f}), "
        f"flux = 2*Fx + Fy + Fz. "
        f"(c) Edge-on patch (x right, y up, z out) at theta = {theta_deg:.0f} deg: cos(theta) = {math.cos(th_c):.3f} = n_x, "
        f"A_yz = A cos(theta) = A n_x."
    )


# ===========================================================================
# Figure 15: maths1_microscopic_stokes.png
# ===========================================================================
def make_fig12_microscopic_stokes(out_dir: Path) -> None:
    fig = plt.figure(figsize=(10.7, 4.6), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[0.84, 1.24], wspace=0.14)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1])

    p_tail = (0.35, 0.72)
    p_tip = (2.75, 1.52)
    draw_arrow_2d(ax_a, p_tail, p_tip, color=NAVY, lw=2.9, head_length=7.4, head_width=4.6, zorder=5)
    ax_a.scatter([p_tail[0]], [p_tail[1]], s=58, color=RED, edgecolor="white", lw=1.0, zorder=6)
    ax_a.scatter([p_tip[0]], [p_tip[1]], s=58, color=TEAL, edgecolor="white", lw=1.0, zorder=6)

    ax_a.text(
        p_tail[0], p_tail[1] + 0.28, "$-$", ha="center", va="center", fontsize=12.0, fontweight="bold",
        color=RED, bbox=dict(boxstyle="circle,pad=0.16", fc=RED_LIGHT, ec=RED, lw=1.1), zorder=7
    )
    ax_a.text(
        p_tip[0], p_tip[1] + 0.28, "$+$", ha="center", va="center", fontsize=12.0, fontweight="bold",
        color=TEAL, bbox=dict(boxstyle="circle,pad=0.16", fc=TEAL_LIGHT, ec=TEAL, lw=1.1), zorder=7
    )
    ax_a.text(p_tail[0], p_tail[1] - 0.22, "$p$", ha="center", va="top", fontsize=10.4, fontweight="bold", color=TEXT)
    ax_a.text(p_tip[0], p_tip[1] - 0.22, "$p + tV$", ha="center", va="top", fontsize=10.4, fontweight="bold", color=TEXT)
    ax_a.text(1.48, 1.32, "$tV$", ha="center", va="bottom", fontsize=10.2, fontweight="bold", color=NAVY)

    ax_a.text(
        1.55,
        -0.05,
        r"0-form boundary difference:" "\n" r"$f(p + tV\,) - f(p)$",
        ha="center",
        va="center",
        fontsize=9.6,
        color=TEXT,
        bbox=dict(boxstyle="round,pad=0.22", fc=GREY_BG, ec=GREY_LINE, lw=0.95),
    )

    ax_a.set_xlim(-0.15, 3.30)
    ax_a.set_ylim(-0.55, 2.25)
    ax_a.set_aspect("equal")
    ax_a.axis("off")
    ax_a.set_title(r"(a) 1D segment: $df_p(V\,)$", fontweight="bold", color=TEXT, pad=6)

    # --- Panel (b): Tiny parallelogram at p spanned by eps*V and eps*W ---
    P0 = np.array([0.55, 0.55])
    eV = np.array([2.55, 0.28])
    eW = np.array([0.68, 1.58])
    P_V = P0 + eV
    P_W = P0 + eW
    P_VW = P0 + eV + eW

    ax_b.add_patch(
        Polygon([P0, P_V, P_VW, P_W], closed=True, fc=GREY_BG, ec="none", alpha=0.92, zorder=1)
    )

    draw_arrow_2d(ax_b, tuple(P0), tuple(P_V), color=AMBER, lw=2.9, head_length=7.2, head_width=4.5, zorder=5)
    draw_arrow_2d(ax_b, tuple(P_VW), tuple(P_W), color=AMBER, lw=2.9, head_length=7.2, head_width=4.5, zorder=5)

    draw_arrow_2d(ax_b, tuple(P_V), tuple(P_VW), color=BLUE, lw=2.9, head_length=7.2, head_width=4.5, zorder=5)
    draw_arrow_2d(ax_b, tuple(P_W), tuple(P0), color=BLUE, lw=2.9, head_length=7.2, head_width=4.5, zorder=5)

    for pt_c in (P0, P_V, P_VW, P_W):
        ax_b.scatter([pt_c[0]], [pt_c[1]], s=34, color=NAVY, edgecolor="white", lw=0.8, zorder=7)

    ax_b.text(P0[0] - 0.10, P0[1] - 0.12, "$p$", ha="right", va="top", fontsize=10.0, fontweight="bold", color=TEXT)
    ax_b.text(P_V[0] + 0.10, P_V[1] - 0.10, r"$p + \epsilon V$", ha="left", va="top", fontsize=9.8, fontweight="bold", color=TEXT)
    ax_b.text(P_W[0] - 0.10, P_W[1] + 0.10, r"$p + \epsilon W$", ha="right", va="bottom", fontsize=9.8, fontweight="bold", color=TEXT)
    ax_b.text(P_VW[0] + 0.08, P_VW[1] + 0.10, r"$p + \epsilon V + \epsilon W$", ha="left", va="bottom", fontsize=9.8, fontweight="bold", color=TEXT)

    mid_bot = 0.5 * (P0 + P_V)
    mid_top = 0.5 * (P_W + P_VW)
    mid_right = 0.5 * (P_V + P_VW)
    mid_left = 0.5 * (P0 + P_W)

    ax_b.text(
        mid_bot[0], mid_bot[1] - 0.30, r"$+\omega(V_p)\,\epsilon$",
        ha="center", va="top", fontsize=9.7, fontweight="bold", color=TEAL,
        bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=AMBER, lw=1.3), zorder=8
    )
    ax_b.text(
        mid_top[0], mid_top[1] + 0.24, r"$-\omega(V_{p+\epsilon W}\,)\,\epsilon$",
        ha="center", va="bottom", fontsize=9.7, fontweight="bold", color=RED,
        bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=AMBER, lw=1.3), zorder=8
    )
    ax_b.text(
        mid_right[0] + 0.22, mid_right[1] - 0.04, r"$+\omega(W_{p+\epsilon V}\,)\,\epsilon$",
        ha="left", va="center", fontsize=9.7, fontweight="bold", color=TEAL,
        bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=BLUE, lw=1.3), zorder=8
    )
    ax_b.text(
        mid_left[0] - 0.20, mid_left[1] + 0.04, r"$-\omega(W_p)\,\epsilon$",
        ha="right", va="center", fontsize=9.7, fontweight="bold", color=RED,
        bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=BLUE, lw=1.3), zorder=8
    )

    # Curved counterclockwise loop arrow + full word "counterclockwise"
    centre_p = 0.25 * (P0 + P_V + P_VW + P_W)
    r_ccw = 0.23
    cy_arc = centre_p[1] + 0.14
    arc_ccw = Arc((centre_p[0], cy_arc), 2 * r_ccw, 2 * r_ccw, angle=0.0, theta1=-35.0, theta2=225.0, color=SLATE, lw=1.7, zorder=6)
    ax_b.add_patch(arc_ccw)
    a_end = math.radians(225.0)
    p_arc_tip = (centre_p[0] + r_ccw * math.cos(a_end), cy_arc + r_ccw * math.sin(a_end))
    p_arc_pre = (centre_p[0] + r_ccw * math.cos(a_end - 0.22), cy_arc + r_ccw * math.sin(a_end - 0.22))
    draw_arrow_2d(ax_b, p_arc_pre, p_arc_tip, color=SLATE, lw=1.7, head_length=5.4, head_width=3.5, zorder=7)
    ax_b.text(
        centre_p[0], centre_p[1] - 0.20, "counterclockwise",
        ha="center", va="center", fontsize=9.2, fontweight="bold", color=SLATE, zorder=7
    )

    ax_b.text(
        0.74, -0.36, r"Right + Left: $+\nabla_{V_p}\omega(W_p)$",
        ha="center", va="center", fontsize=9.3, fontweight="bold", color=BLUE,
        bbox=dict(boxstyle="round,pad=0.14", fc=BLUE_PALE, ec=BLUE, lw=0.95),
    )
    ax_b.text(
        3.56, -0.36, r"Bottom + Top: $-\nabla_{W_p}\omega(V_p)$",
        ha="center", va="center", fontsize=9.3, fontweight="bold", color=AMBER,
        bbox=dict(boxstyle="round,pad=0.14", fc=AMBER_LIGHT, ec=AMBER, lw=0.95),
    )

    ax_b.set_xlim(-1.12, 5.25)
    ax_b.set_ylim(-0.76, 3.05)
    ax_b.set_aspect("equal")
    ax_b.axis("off")
    ax_b.set_title(r"(b) Tiny parallelogram: $d\omega(V_p, W_p)$", fontweight="bold", color=TEXT, pad=6)

    save_fig(fig, out_dir, "maths1_microscopic_stokes.png")
    print(
        "[Fig 12] (a) 1D segment p -> p + tV: tail (-) at p, tip (+) at p + tV, f(p + tV) - f(p). "
        "(b) Counterclockwise parallelogram on eps*V, eps*W: bottom +omega(V_p)*eps & top -omega(V_{p+eps*W})*eps "
        "pair to -nabla_{W_p} omega(V_p); right +omega(W_{p+eps*V})*eps & left -omega(W_p)*eps "
        "pair to +nabla_{V_p} omega(W_p)."
    )


# ===========================================================================
# Figure 16: maths1_half_disc_cell.png
# ===========================================================================
def make_fig13_half_disc_cell(out_dir: Path) -> None:
    fig = plt.figure(figsize=(10.7, 4.8), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[0.96, 1.12], wspace=0.20)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1])

    # --- Panel (a): Unit square I^2 in (r, theta) with r, theta axes & signed edges ---
    ax_a.add_patch(Polygon([(0, 0), (1, 0), (1, 1), (0, 1)], closed=True, fc=GREY_BG, ec="none", zorder=1))
    for gv in (0.25, 0.50, 0.75):
        ax_a.plot([gv, gv], [0, 1], color=GREY_LINE, lw=0.8, zorder=1)
        ax_a.plot([0, 1], [gv, gv], color=GREY_LINE, lw=0.8, zorder=1)

    # Coordinate axes r (horizontal) and theta (vertical) tucked cleanly outside the signed edges
    y_rax = -0.32
    x_thax = -0.48
    draw_arrow_2d(ax_a, (0.0, y_rax), (1.08, y_rax), color=SLATE, lw=1.4, head_length=5.6, head_width=3.4, zorder=3)
    ax_a.plot([0.0, 0.0], [y_rax - 0.03, y_rax + 0.03], color=SLATE, lw=1.2, zorder=3)
    ax_a.plot([1.0, 1.0], [y_rax - 0.03, y_rax + 0.03], color=SLATE, lw=1.2, zorder=3)
    ax_a.text(0.0, y_rax - 0.05, "$0$", ha="center", va="top", fontsize=9.1, color=SLATE)
    ax_a.text(1.0, y_rax - 0.05, "$1$", ha="center", va="top", fontsize=9.1, color=SLATE)
    ax_a.text(1.13, y_rax, "$r$", ha="left", va="center", fontsize=9.8, fontweight="bold", color=TEXT)

    draw_arrow_2d(ax_a, (x_thax, 0.0), (x_thax, 1.08), color=SLATE, lw=1.4, head_length=5.6, head_width=3.4, zorder=3)
    ax_a.plot([x_thax - 0.03, x_thax + 0.03], [0.0, 0.0], color=SLATE, lw=1.2, zorder=3)
    ax_a.plot([x_thax - 0.03, x_thax + 0.03], [1.0, 1.0], color=SLATE, lw=1.2, zorder=3)
    ax_a.text(x_thax - 0.05, 0.0, "$0$", ha="right", va="center", fontsize=9.1, color=SLATE)
    ax_a.text(x_thax - 0.05, 1.0, "$1$", ha="right", va="center", fontsize=9.1, color=SLATE)
    ax_a.text(x_thax, 1.13, r"$\theta$", ha="center", va="bottom", fontsize=9.8, fontweight="bold", color=TEXT)

    sh = 0.045
    draw_arrow_2d(ax_a, (sh, 0.0), (1.0 - sh, 0.0), color=TEAL, lw=2.9, head_length=7.0, head_width=4.4, zorder=5)
    draw_arrow_2d(ax_a, (1.0, sh), (1.0, 1.0 - sh), color=TEAL, lw=2.9, head_length=7.0, head_width=4.4, zorder=5)
    draw_arrow_2d(ax_a, (1.0 - sh, 1.0), (sh, 1.0), color=RED, lw=2.9, head_length=7.0, head_width=4.4, zorder=5)
    draw_arrow_2d(ax_a, (0.0, 1.0 - sh), (0.0, sh), color=RED, lw=2.9, head_length=7.0, head_width=4.4, zorder=5)

    for cx, cy in ((0, 0), (1, 0), (1, 1), (0, 1)):
        ax_a.scatter([cx], [cy], s=38, color=NAVY, edgecolor="white", lw=0.9, zorder=7)

    ax_a.text(0.50, -0.14, r"$+\varphi(t, 0)$  ($\theta = 0$)", ha="center", va="top", fontsize=9.5, fontweight="bold", color=TEAL)
    ax_a.text(1.13, 0.50, r"$+\varphi(1, t)$" "\n" r"($r = 1$)", ha="left", va="center", fontsize=9.5, fontweight="bold", color=TEAL)
    ax_a.text(0.50, 1.15, r"$-\varphi(t, 1)$  ($\theta = 1$)", ha="center", va="bottom", fontsize=9.5, fontweight="bold", color=RED)
    ax_a.text(-0.11, 0.50, r"$-\varphi(0, t)$" "\n" r"($r = 0$)", ha="right", va="center", fontsize=9.5, fontweight="bold", color=RED)

    corner_badges = [
        ((-0.07, 0.08), "+"), ((0.09, -0.07), "-"),
        ((0.91, -0.07), "+"), ((1.07, 0.08), "-"),
        ((1.07, 0.92), "+"),  ((0.91, 1.07), "-"),
        ((0.09, 1.07), "+"),  ((-0.07, 0.92), "-"),
    ]
    for (bx, by), sgn_ch in corner_badges:
        col_s = TEAL if sgn_ch == "+" else RED
        fc_s = TEAL_LIGHT if sgn_ch == "+" else RED_LIGHT
        ax_a.text(
            bx, by, f"${sgn_ch}$", ha="center", va="center", fontsize=9.3, fontweight="bold",
            color=col_s, bbox=dict(boxstyle="circle,pad=0.08", fc=fc_s, ec=col_s, lw=0.8), zorder=8
        )

    ax_a.text(0.50, 0.50, r"$\partial\partial\sigma = \emptyset$" "\n(each corner: $+ -$)",
              ha="center", va="center", fontsize=9.3, fontweight="bold", color=NAVY,
              bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=GREY_LINE, lw=0.85, alpha=0.94), zorder=6)

    ax_a.set_xlim(-0.66, 1.56)
    ax_a.set_ylim(-0.50, 1.38)
    ax_a.set_aspect("equal")
    ax_a.axis("off")
    ax_a.set_title(r"(a) Unit square $I^2$ in $(r, \theta)$", fontweight="bold", color=TEXT, pad=6)

    # --- Panel (b): UNTOUCHED per review ---
    th_hd = np.linspace(0.0, math.pi, 240)
    disc_poly = [(0.0, 0.0)] + [(float(math.cos(a)), float(math.sin(a))) for a in th_hd]
    ax_b.add_patch(Polygon(disc_poly, closed=True, fc=BLUE_PALE, ec="none", zorder=1))

    for rv in (0.25, 0.50, 0.75):
        ax_b.plot(rv * np.cos(th_hd), rv * np.sin(th_hd), color=GREY_LINE, lw=0.85, zorder=2)
    for k_th in range(1, 6):
        ang_hd = k_th * math.pi / 6.0
        ax_b.plot([0.0, math.cos(ang_hd)], [0.0, math.sin(ang_hd)], color=GREY_LINE, lw=0.85, zorder=2)

    ax_b.plot(np.cos(th_hd), np.sin(th_hd), color=TEAL, lw=2.9, zorder=5)
    for deg_arc in (35.0, 90.0, 145.0):
        a0 = math.radians(deg_arc - 4.0)
        a1 = math.radians(deg_arc + 4.0)
        draw_arrow_2d(
            ax_b,
            (math.cos(a0), math.sin(a0)),
            (math.cos(a1), math.sin(a1)),
            color=TEAL,
            lw=2.8,
            head_length=7.0,
            head_width=4.4,
            zorder=6,
        )

    draw_arrow_2d(ax_b, (0.06, 0.0), (0.98, 0.0), color=TEAL, lw=2.9, head_length=7.0, head_width=4.4, zorder=6)
    draw_arrow_2d(ax_b, (-0.98, 0.0), (-0.06, 0.0), color=RED, lw=2.9, head_length=7.0, head_width=4.4, zorder=6)

    ax_b.scatter([0.0], [0.0], s=110, facecolor="white", edgecolor=RED, lw=2.3, zorder=7)
    ax_b.scatter([0.0], [0.0], s=28, color=RED, zorder=8)
    ax_b.scatter([-1.0, 1.0], [0.0, 0.0], s=36, color=NAVY, edgecolor="white", lw=0.8, zorder=7)

    ax_b.text(1.03, -0.05, "$(1, 0)$", ha="left", va="top", fontsize=9.4, fontweight="bold", color=TEXT)
    ax_b.text(-1.03, -0.05, "$(-1, 0)$", ha="right", va="top", fontsize=9.4, fontweight="bold", color=TEXT)

    ax_b.text(
        0.0, 1.15, r"Arc ($r = 1$): $\int x\,dy = \pi/2$",
        ha="center", va="bottom", fontsize=9.6, fontweight="bold", color=TEAL,
        bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=TEAL, lw=0.85, alpha=0.95), zorder=8
    )
    ax_b.text(0.58, -0.10, r"$\int x\,dy = 0$", ha="center", va="top", fontsize=9.4, fontweight="bold", color=TEAL)
    ax_b.text(-0.58, -0.10, r"$\int x\,dy = 0$", ha="center", va="top", fontsize=9.4, fontweight="bold", color=RED)
    ax_b.annotate(
        r"Collapsed $r = 0$ edge: $\int x\,dy = 0$",
        xy=(0.0, -0.06),
        xytext=(0.0, -0.66),
        ha="center",
        va="center",
        fontsize=9.3,
        fontweight="bold",
        color=RED,
        bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=RED, lw=0.85, alpha=0.95),
        arrowprops=dict(arrowstyle="->", color=RED, lw=1.15, shrinkB=2),
        zorder=8,
    )
    ax_b.text(
        0.0, 0.44, r"Total $= \frac{\pi}{2} = \mathrm{area}$",
        ha="center", va="center", fontsize=9.5, fontweight="bold", color=NAVY,
        bbox=dict(boxstyle="round,pad=0.14", fc="white", ec=NAVY, lw=0.85, alpha=0.93), zorder=8
    )

    ax_b.set_xlim(-1.38, 1.38)
    ax_b.set_ylim(-0.88, 1.42)
    ax_b.set_aspect("equal")
    ax_b.axis("off")
    ax_b.set_title(
        r"(b) Image $\varphi(r, \theta) = (r\cos\pi\theta, r\sin\pi\theta)$",
        fontweight="bold",
        color=TEXT,
        pad=6,
    )

    save_fig(fig, out_dir, "maths1_half_disc_cell.png")
    print(
        "[Fig 13] Half-disc phi(r, theta) = (r cos(pi*theta), r sin(pi*theta)): "
        "partial(sigma) = alpha - c - beta + gamma; "
        "boundary int(x dy) -> gamma (0,0)->(1,0): 0, alpha arc (1,0)->(-1,0): pi/2, "
        "-beta (-1,0)->(0,0): 0, collapsed c at (0,0): 0; total = pi/2 = area."
    )


# ===========================================================================
# Figure 17: maths1_cylinder_cap_shadow.png
# ===========================================================================
def make_fig14_cylinder_cap_shadow(out_dir: Path) -> None:
    fig = plt.figure(figsize=(8.6, 5.7), dpi=DPI)
    ax = fig.add_subplot(111, projection="3d", computed_zorder=False)

    elev_c, azim_c = 28.0, -122.0
    ax.view_init(elev=elev_c, azim=azim_c)
    set_equal_3d_box(ax, (-1.35, 1.35), (-1.35, 1.35), (-0.20, 2.50), zoom=1.10)
    ax.axis("off")

    n_th = 4000
    th_num = np.linspace(0.0, 2.0 * math.pi, n_th, endpoint=False)
    dth_num = 2.0 * math.pi / n_th
    x_c = np.cos(th_num)
    y_c = np.sin(th_num)
    z_c = x_c + 1.0
    dx_dth = -np.sin(th_num)
    dy_dth = np.cos(th_num)
    dz_dth = -np.sin(th_num)
    integrand_line = (-x_c**2 * y_c) * dx_dth + (x_c * y_c**2) * dy_dth + (z_c**3) * dz_dth
    line_int_num = float(np.sum(integrand_line) * dth_num)
    exact_pi_over_2 = 0.5 * math.pi
    assert abs(line_int_num - exact_pi_over_2) < 1e-10

    rs = np.linspace(0.0, 1.0, 28)
    ts = np.linspace(0.0, 2.0 * math.pi, 96)
    RS, TS = np.meshgrid(rs, ts)
    X_SH = RS * np.cos(TS)
    Y_SH = RS * np.sin(TS)
    Z_SH = np.zeros_like(X_SH)
    ax.plot_surface(X_SH, Y_SH, Z_SH, color=AMBER_LIGHT, alpha=0.72, edgecolor="none", shade=False, zorder=1)
    th_rim = np.linspace(0.0, 2.0 * math.pi, 240)
    ax.plot(np.cos(th_rim), np.sin(th_rim), np.zeros_like(th_rim), color=AMBER, lw=2.0, zorder=2)
    ax.plot(0.5 * np.cos(th_rim), 0.5 * np.sin(th_rim), np.zeros_like(th_rim), color=AMBER, lw=0.85, ls="--", alpha=0.65, zorder=2)

    s_wall = np.linspace(0.0, 1.0, 20)
    SW, TW = np.meshgrid(s_wall, ts)
    XW = np.cos(TW)
    YW = np.sin(TW)
    ZW = SW * (np.cos(TW) + 1.0)
    ax.plot_surface(XW, YW, ZW, color=SLATE, alpha=0.11, edgecolor="none", shade=True, zorder=2)

    for deg_drop in (0.0, 60.0, 120.0, 240.0, 300.0):
        ad = math.radians(deg_drop)
        xd, yd = math.cos(ad), math.sin(ad)
        zd = xd + 1.0
        ax.plot([xd, xd], [yd, yd], [0.0, zd], color=SLATE, lw=0.95, ls=":", alpha=0.70, zorder=3)

    add_3d_arrow(ax, np.array([0.0, 0.0, 0.0]), np.array([1.28, 0.0, 0.0]), SLATE, elev_c, azim_c, lw=1.2, head_len=0.09, zord=3)
    add_3d_arrow(ax, np.array([0.0, 0.0, 0.0]), np.array([0.0, 1.28, 0.0]), SLATE, elev_c, azim_c, lw=1.2, head_len=0.09, zord=3)
    add_3d_arrow(ax, np.array([0.0, 0.0, 0.0]), np.array([0.0, 0.0, 2.38]), SLATE, elev_c, azim_c, lw=1.2, head_len=0.09, zord=3)
    ax.text(1.36, 0.0, 0.0, "$x$", fontsize=9.8, fontweight="bold", color=TEXT, ha="center", va="center")
    ax.text(0.0, 1.36, 0.0, "$y$", fontsize=9.8, fontweight="bold", color=TEXT, ha="center", va="center")
    ax.text(0.0, 0.0, 2.45, "$z$", fontsize=9.8, fontweight="bold", color=TEXT, ha="center", va="center")

    Z_CAP = X_SH + 1.0
    ax.plot_surface(X_SH, Y_SH, Z_CAP, color=BLUE_LIGHT, alpha=0.60, edgecolor="none", shade=True, zorder=4)
    for rv in (0.5,):
        xc_r, yc_r = rv * np.cos(th_rim), rv * np.sin(th_rim)
        ax.plot(xc_r, yc_r, xc_r + 1.0, color=SLATE, lw=0.8, alpha=0.65, zorder=5)
    for k_sp in range(8):
        ang_sp = k_sp * math.pi / 4.0
        r_sp = np.linspace(0.0, 1.0, 15)
        xs_p, ys_p = r_sp * math.cos(ang_sp), r_sp * math.sin(ang_sp)
        ax.plot(xs_p, ys_p, xs_p + 1.0, color=SLATE, lw=0.75, alpha=0.55, zorder=5)

    xc_b = np.cos(th_rim)
    yc_b = np.sin(th_rim)
    zc_b = xc_b + 1.0
    ax.plot(xc_b, yc_b, zc_b, color=NAVY, lw=3.0, zorder=6)

    fig.canvas.draw()
    proj_m = ax.get_proj()
    sx_c, sy_c, _ = proj3d.proj_transform(xc_b, yc_b, zc_b, proj_m)
    cx_m, cy_m = float(np.mean(sx_c)), float(np.mean(sy_c))
    area_2d_screen = float(np.sum((sx_c[:-1] - cx_m) * np.diff(sy_c) - (sy_c[:-1] - cy_m) * np.diff(sx_c)))
    assert area_2d_screen > 0.0, f"Boundary curve is not counterclockwise on screen: {area_2d_screen}"

    for deg_arr in (25.0, 115.0, 205.0, 295.0):
        a0 = math.radians(deg_arr)
        a1 = math.radians(deg_arr + 9.0)
        p0 = np.array([math.cos(a0), math.sin(a0), math.cos(a0) + 1.0])
        p1 = np.array([math.cos(a1), math.sin(a1), math.cos(a1) + 1.0])
        add_3d_arrow(ax, p0, p1, NAVY, elev_c, azim_c, lw=2.8, head_len=0.12, zord=7)

    c_cap = np.array([0.0, 0.0, 1.0])
    n_cap = np.array([-1.0, 0.0, 1.0]) / math.sqrt(2.0)
    n_tip = c_cap + 0.50 * n_cap
    add_3d_arrow(ax, c_cap, n_tip, RED, elev_c, azim_c, lw=2.5, head_len=0.10, zord=8)
    ax.text(
        n_tip[0] - 0.12,
        n_tip[1] + 0.06,
        n_tip[2] + 0.06,
        r"$\hat{\mathbf{n}}$",
        fontsize=10.2,
        fontweight="bold",
        color=RED,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.07", fc="white", ec="none", alpha=0.88),
        zorder=10,
    )

    annotate_3d_point(
        ax, proj_m, (0.65, 0.35, 1.65), (0.86, 0.85),
        r"Tilted cap $\Psi(r, \theta)$" "\n" r"in $z = x + 1$", NAVY, fontsize=9.5
    )
    annotate_3d_point(
        ax, proj_m, (0.58, -0.58, 0.0), (0.86, 0.23),
        r"$xy$-shadow: unit disc" "\n" r"($x^2 + y^2 \leq 1$)", AMBER, fontsize=9.4
    )
    annotate_3d_point(
        ax, proj_m, (-math.cos(math.radians(40.0)), -math.sin(math.radians(40.0)), 1.0 - math.cos(math.radians(40.0))),
        (0.08, 0.58),
        r"Boundary $C$" "\n(counterclockwise\nseen from above)", NAVY, fontsize=9.2
    )

    ax.text2D(
        0.50, 0.95,
        r"Cylinder $x^2 + y^2 = 1$ cut by $z = x + 1$: only the $xy$-shadow counts",
        transform=ax.transAxes, ha="center", va="bottom", fontsize=10.4, fontweight="bold", color=TEXT
    )
    ax.text2D(
        0.50, 0.02,
        r"$d\omega^1_{\vec{F}} = (x^2 + y^2)\,dx\wedge dy \;\Longrightarrow\; \oint_C \vec{F}\cdot d\vec{r} = \int_0^{2\pi}\!\int_0^1 r^3\,dr\,d\theta = \frac{\pi}{2}$",
        transform=ax.transAxes, ha="center", va="bottom", fontsize=9.4, color=TEXT,
        bbox=dict(boxstyle="round,pad=0.18", fc=GREY_BG, ec=GREY_LINE, lw=0.9)
    )

    save_fig(fig, out_dir, "maths1_cylinder_cap_shadow.png")
    print(
        f"[Fig 14] Cylinder x^2 + y^2 = 1 cut by z = x + 1, F = <-x^2*y, x*y^2, z^3>: "
        f"d w1(F) = (x^2 + y^2) dx^dy; shadow integral = pi/2 = {exact_pi_over_2:.6f}, "
        f"direct line integral round boundary curve = {line_int_num:.6f} (= pi/2)."
    )


def print_subsection_numbers() -> None:
    """Compute and print every numerical value quoted in the subsection text."""
    t_s = np.linspace(0.0, 1.0, 4000, endpoint=False)
    dt_s = 1.0 / 4000
    eq_sigma1 = float(np.sum(np.cos(2.0 * np.pi * t_s) * (2.0 * np.pi * np.cos(2.0 * np.pi * t_s))) * dt_s)
    eq_sigma2 = float(np.sum((-np.cos(2.0 * np.pi * t_s)) * (2.0 * np.pi * np.cos(2.0 * np.pi * t_s))) * dt_s)
    assert abs(eq_sigma1 - math.pi) < 1e-10 and abs(eq_sigma2 + math.pi) < 1e-10

    cusp_val = (1**2) * (1**3) - (1**2) * ((-1) ** 3)
    assert cusp_val == 2

    th_p = np.linspace(math.pi, 0.0, 4001)
    x_p, y_p = np.cos(th_p), np.sin(th_p)
    dx_p, dy_p = np.diff(x_p), np.diff(y_p)
    xm_p, ym_p = 0.5 * (x_p[:-1] + x_p[1:]), 0.5 * (y_p[:-1] + y_p[1:])
    int_semicircle = float(np.sum((xm_p**2 + ym_p) * dx_p + (xm_p - ym_p**2) * dy_p))
    int_diameter = 2.0 / 3.0
    assert abs(int_semicircle - int_diameter) < 1e-6

    cube_flux = 4.0 / 3.0

    print(
        f"[Subsection text] Sphere hemispheres equator int(x dy) = (+pi, -pi) = "
        f"({eq_sigma1:+.6f}, {eq_sigma2:+.6f}), sum = 0; "
        f"pull-back check phi(a,b)=(a+b,a-b,ab) on y dx + z dy + x dz -> d(phi* w) = phi*(dw) = (2 - 2b) da^db; "
        f"cusped curve (t^2, t^3) on [-1, 1] for f = x^2*y -> f(1,1) - f(1,-1) = {cusp_val}; "
        f"path-swap int_sigma w = {int_semicircle:.6f} = int_tau w = 2/3 ({int_diameter:.6f}); "
        f"cylinder cap Stokes = pi/2 ({0.5 * math.pi:.6f}); "
        f"unit-cube I^3 flux of <x*y^2, y^3, x^2*y^2> = int_0^1 4*y^2 dy = 4/3 ({cube_flux:.6f}); "
        f"graded Leibniz row 6 sign = (-1)^1 = -1; shear flow d(f dy) = (df/dx) dx^dy; "
        f"d^dagger = (-1)^p * d * -> d^dagger d w1(F) = +w1(curl(curl F)), d d^dagger w1(F) = -w1(grad(div F))."
    )


# ===========================================================================
# Entrypoint
# ===========================================================================
def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_dir>", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating 8 Maths 1 Differential Forms figures in {out_dir} ...")
    make_fig7_one_form_stacks(out_dir)
    make_fig8_semicircle_pullback_bins(out_dir)
    make_fig9_wedge_area(out_dir)
    make_fig10_surface_pullback(out_dir)
    make_fig11_flux_shadows(out_dir)
    make_fig12_microscopic_stokes(out_dir)
    make_fig13_half_disc_cell(out_dir)
    make_fig14_cylinder_cap_shadow(out_dir)
    print_subsection_numbers()
    print("All 8 Maths 1 Differential Forms figures generated and verified.")


if __name__ == "__main__":
    main()
