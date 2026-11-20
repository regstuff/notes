#!/usr/bin/env python3
"""Generate six publication-quality vector calculus figures for 'Maths 1 - Differential Geometry'.

Project Context:
    Illustrates the Vector Calculus opening chapter (lines 1-509) of
    `maths_1_differential_geometry.md` in the MkDocs lecture-notes repository, matching the
    visual palette, typography (DejaVu Sans + Computer Modern mathtext), and 220-dpi white-card
    style of `make_maths3_figures.py`.

What This Script Does:
    Accepts `<output_dir>` as its sole command-line argument, generates six PNG figures with
    every vector arrow computed directly from the underlying analytical fields, verifies key
    geometric and numerical identities (non-zero wind curl, paddle-wheel curl signs, 3D and 2D
    counter-clockwise loop orientation on the Stokes dome, steepest-ascent directional
    derivatives, and 2D Laplacian circle averages), and prints to stdout every numerical value
    quoted in the figure labels and captions:
        1. `maths1_scalar_vector_fields.png`
        2. `maths1_divergence_theorem_cubes.png`
        3. `maths1_curl_paddle_wheels.png`
        4. `maths1_stokes_loops.png`
        5. `maths1_gradient_steepest_ascent.png`
        6. `maths1_laplacian_average.png`

Performance Note:
    Uses vectorized NumPy array evaluation over modest 2D/3D grids (< 250 x 250 points),
    keeping peak memory well below 200 MB and rendering all six 220-dpi figures sequentially
    in a few seconds without multiprocessing overhead.

Usage:
    /home/ubuntu/.claude/skills/lecture-notes/.venv/bin/python \
        make_maths1_figures.py <output_dir>
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Polygon
from mpl_toolkits.mplot3d import proj3d
import numpy as np


# ---------------------------------------------------------------------------
# Consistent visual palette & typography matching make_maths3_figures.py
# Minimum text size across all saved figures is >= 9.2 pt (brief rule: >= 9 pt).
# ---------------------------------------------------------------------------
NAVY = "#1e3a8a"
BLUE = "#2563eb"
BLUE_LIGHT = "#dbeafe"
BLUE_PALE = "#eff6ff"
TEAL = "#0f766e"
TEAL_LIGHT = "#ccfbf1"
AMBER = "#d97706"
AMBER_LIGHT = "#fef3c7"
RED = "#dc2626"
RED_LIGHT = "#fee2e2"
SLATE = "#64748b"
GREY_LINE = "#cbd5e1"
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
    """Save figure at 220 dpi with tight bounding box and verify width <= 11 inches."""
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
    lw: float = 1.1,
    pad: float = 0.06,
    zorder: int = 0,
) -> FancyBboxPatch:
    """Draw a rounded background card in data coordinates."""
    box = FancyBboxPatch(
        (x + pad, y + pad),
        w - 2 * pad,
        h - 2 * pad,
        boxstyle=f"round,pad={pad},rounding_size=0.14",
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
    lw: float = 2.0,
    ls: str = "-",
    head_length: float = 6.5,
    head_width: float = 3.8,
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


# ===========================================================================
# Figure 1: maths1_scalar_vector_fields.png
# ===========================================================================
def temp_field_c(x: np.ndarray | float, y: np.ndarray | float) -> np.ndarray | float:
    """Smooth temperature field T(x, y) in deg C over 0 <= x, y <= 10 km."""
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    return (
        15.2
        + 0.20 * xa
        - 0.14 * ya
        + 6.4 * np.exp(-(((xa - 6.5) / 2.5) ** 2 + ((ya - 6.0) / 2.1) ** 2))
    )


def wind_field_ms(
    x: np.ndarray | float, y: np.ndarray | float
) -> tuple[np.ndarray, np.ndarray]:
    """Smooth 2D horizontal wind field F(x, y) in m/s (with F_z = 0 in this slice).

    Combines a gentle eastward breeze (1.8, 0.3) m/s with a strong counter-clockwise
    cyclonic swirl around a low-pressure centre at (3.8, 5.6) km so the swirl is
    clearly visible (turning westward north of L) and curl(F) != 0.
    """
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    xc, yc = 3.8, 5.6
    r0 = 3.10
    omega = 2.35
    dx = xa - xc
    dy = ya - yc
    gauss = np.exp(-(dx**2 + dy**2) / (r0**2))
    fx = 1.8 - omega * dy * gauss
    fy = 0.3 + omega * dx * gauss
    return fx, fy


def make_fig1_scalar_vector_fields(out_dir: Path) -> dict[str, object]:
    fig = plt.figure(figsize=(10.8, 4.7), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.08, 1.0], wspace=0.38)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1])

    # --- Panel (a): Scalar temperature field T(x, y) ---
    ng = 220
    xg = np.linspace(0.0, 10.0, ng)
    yg = np.linspace(0.0, 10.0, ng)
    XX, YY = np.meshgrid(xg, yg)
    TT = temp_field_c(XX, YY)
    t_min = float(np.min(TT))
    t_max = float(np.max(TT))

    pcm = ax_a.pcolormesh(XX, YY, TT, cmap="YlOrRd", shading="gouraud", alpha=0.88, zorder=1)
    cbar = fig.colorbar(pcm, ax=ax_a, fraction=0.046, pad=0.035)
    cbar.set_label("Temperature $T$ (°C)", fontsize=9.8, color=TEXT)
    cbar.ax.tick_params(labelsize=9.3)

    iso_levels = [15.0, 17.0, 19.0, 21.0]
    cs = ax_a.contour(
        XX,
        YY,
        TT,
        levels=iso_levels,
        colors=TEXT,
        linewidths=1.1,
        linestyles="solid",
        alpha=0.75,
        zorder=3,
    )
    # Compute exact western crossings along y = 5.4 so all 4 contour levels are hit cleanly once
    manual_iso = []
    xs_scan = np.linspace(0.2, 6.4, 600)
    ts_scan = temp_field_c(xs_scan, np.full_like(xs_scan, 5.4))
    for lv in iso_levels:
        idx_lv = int(np.argmin(np.abs(ts_scan - lv)))
        manual_iso.append((float(xs_scan[idx_lv]), 5.4))
    ax_a.clabel(cs, fmt=lambda v: f"{v:.0f} °C", fontsize=9.3, manual=manual_iso)

    # Mark two points with dots and exact computed temperatures
    pt1 = (6.4, 6.2)
    pt2 = (2.2, 2.0)
    t1 = float(temp_field_c(*pt1))
    t2 = float(temp_field_c(*pt2))

    lbl_bbox = dict(boxstyle="round,pad=0.20", fc="white", ec=NAVY, lw=0.9, alpha=0.95)
    ax_a.scatter(
        [pt1[0], pt2[0]], [pt1[1], pt2[1]], s=54, color=NAVY, edgecolor="white", lw=1.1, zorder=7
    )
    ax_a.annotate(
        f"{t1:.1f} °C",
        xy=pt1,
        xytext=(pt1[0] + 0.55, pt1[1] + 1.25),
        fontsize=9.6,
        fontweight="bold",
        color=NAVY,
        bbox=lbl_bbox,
        arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2, shrinkB=4),
        zorder=8,
    )
    ax_a.annotate(
        f"{t2:.1f} °C",
        xy=pt2,
        xytext=(pt2[0] + 0.75, pt2[1] - 0.95),
        fontsize=9.6,
        fontweight="bold",
        color=NAVY,
        bbox=lbl_bbox,
        arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.2, shrinkB=4),
        zorder=8,
    )

    ax_a.set_xlim(0.0, 10.0)
    ax_a.set_ylim(0.0, 10.0)
    ax_a.set_aspect("equal")
    ax_a.set_xticks([0, 2, 4, 6, 8, 10])
    ax_a.set_yticks([0, 2, 4, 6, 8, 10])
    ax_a.set_xlabel("$x$ (km)", color=TEXT)
    ax_a.set_ylabel("$y$ (km)", color=TEXT)
    ax_a.set_title("(a) Scalar field: temperature $T(x, y)$", fontweight="bold", color=TEXT, pad=8)

    # --- Panel (b): Wind vector field F(x, y) on a 9 x 9 integer-km grid ---
    n_grid = 9
    xw = np.linspace(1.0, 9.0, n_grid)
    yw = np.linspace(1.0, 9.0, n_grid)
    XW, YW = np.meshgrid(xw, yw)
    FX, FY = wind_field_ms(XW, YW)
    speeds = np.hypot(FX, FY)
    speed_min = float(np.min(speeds))
    speed_max = float(np.max(speeds))

    # Verify analytically that curl_z(F) != 0 at the swirl centre (3.8, 5.6)
    xc_low, yc_low = 3.8, 5.6
    curl_z_centre = 2.0 * 2.35
    assert curl_z_centre > 4.0
    # Verify wind north of L (at x=4, y=7) has negative F_x (westward return flow)
    assert float(FX[6, 3]) < -0.5

    # Highlighted grid point southeast of low centre where both F_x > 0 and F_y > 0 are substantial:
    # row=2 (y=3.0 km), col=5 (x=6.0 km) -> (6, 3) km
    hi_row, hi_col = 2, 5
    xh = float(XW[hi_row, hi_col])
    yh = float(YW[hi_row, hi_col])
    fx_h = float(FX[hi_row, hi_col])
    fy_h = float(FY[hi_row, hi_col])
    sp_h = math.hypot(fx_h, fy_h)

    grid_spacing = float(xw[1] - xw[0])  # 1.0 km
    q_scale = 5.3  # m/s per 1 km of arrow length -> max arrow < 0.90 km < 1.0 km grid spacing!
    assert speed_max / q_scale < 0.92 * grid_spacing, (
        f"Longest arrow {speed_max / q_scale:.2f} km exceeds grid spacing {grid_spacing:.2f} km"
    )
    key_speed = 5.0
    inset_mag = 3
    dx_mag = inset_mag * (fx_h / q_scale)
    dy_mag = inset_mag * (fy_h / q_scale)

    # Magnified (x3) decomposition inset box in the lower-right corner, keeping (6, 3) km
    # uncovered on the map at field scale, and omitting background arrows under the two boxes.
    cbox_x0, cbox_y0 = 6.32, 0.30
    cbox_w, cbox_h = 3.44, 2.24
    kbox_x0, kbox_y0 = 7.38, 8.42
    kbox_w, kbox_h = 2.35, 1.34

    def hits_box(
        px: np.ndarray, py: np.ndarray, bx0: float, by0: float, bw: float, bh: float, pad_b: float = 0.14
    ) -> np.ndarray:
        return (
            (px >= bx0 - pad_b)
            & (px <= bx0 + bw + pad_b)
            & (py >= by0 - pad_b)
            & (py <= by0 + bh + pad_b)
        )

    XTIP = XW + FX / q_scale
    YTIP = YW + FY / q_scale
    XMID = 0.5 * (XW + XTIP)
    YMID = 0.5 * (YW + YTIP)
    in_comp = (
        hits_box(XW, YW, cbox_x0, cbox_y0, cbox_w, cbox_h)
        | hits_box(XMID, YMID, cbox_x0, cbox_y0, cbox_w, cbox_h)
        | hits_box(XTIP, YTIP, cbox_x0, cbox_y0, cbox_w, cbox_h)
    )
    in_key = (
        hits_box(XW, YW, kbox_x0, kbox_y0, kbox_w, kbox_h)
        | hits_box(XMID, YMID, kbox_x0, kbox_y0, kbox_w, kbox_h)
        | hits_box(XTIP, YTIP, kbox_x0, kbox_y0, kbox_w, kbox_h)
    )
    is_hi = (np.arange(n_grid)[:, None] == hi_row) & (np.arange(n_grid)[None, :] == hi_col)
    assert not bool(in_comp[hi_row, hi_col]), "Highlighted grid point (6, 3) must stay outside inset box"
    mask_bg = ~(in_comp | in_key | is_hi)

    ax_b.set_facecolor("#f8fafc")
    ax_b.scatter([xc_low], [yc_low], s=46, color=TEAL, zorder=3)
    ax_b.text(
        xc_low,
        yc_low + 0.24,
        "L",
        ha="center",
        va="bottom",
        fontsize=9.8,
        fontweight="bold",
        color=TEAL,
        bbox=dict(boxstyle="round,pad=0.10", fc="white", ec=TEAL, lw=0.8, alpha=0.92),
        zorder=6,
    )

    ax_b.quiver(
        XW[mask_bg],
        YW[mask_bg],
        FX[mask_bg],
        FY[mask_bg],
        angles="xy",
        scale_units="xy",
        scale=q_scale,
        color=BLUE,
        alpha=0.70,
        width=0.0058,
        headwidth=3.6,
        headlength=4.4,
        headaxislength=3.9,
        zorder=3,
    )

    # Highlighted grid arrow at (6, 3) km drawn at exact field scale on the map
    ax_b.quiver(
        [xh],
        [yh],
        [fx_h],
        [fy_h],
        angles="xy",
        scale_units="xy",
        scale=q_scale,
        color=RED,
        width=0.0072,
        headwidth=3.8,
        headlength=4.5,
        headaxislength=4.0,
        zorder=6,
    )
    ax_b.scatter([xh], [yh], s=32, color=RED, edgecolor="white", lw=0.8, zorder=7)

    # Thin leader line from the magnified inset box to the point (6, 3) km
    ax_b.plot([6.62, xh], [cbox_y0 + cbox_h, yh], color=SLATE, lw=1.05, ls="-", zorder=4)

    # Magnified (x3) inset box in the lower-right corner
    comp_card = FancyBboxPatch(
        (cbox_x0, cbox_y0),
        cbox_w,
        cbox_h,
        boxstyle="round,pad=0.05,rounding_size=0.15",
        facecolor="white",
        edgecolor=AMBER,
        linewidth=1.05,
        alpha=0.96,
        zorder=5,
    )
    ax_b.add_patch(comp_card)

    # Label "\u00d73" in the top-left of the inset box
    ax_b.text(
        cbox_x0 + 0.18,
        cbox_y0 + cbox_h - 0.16,
        "\u00d73",
        ha="left",
        va="top",
        fontsize=9.8,
        fontweight="bold",
        color=NAVY,
        zorder=8,
    )

    # Head-to-tail 3x magnified vectors inside the inset box:
    # F_x x_hat dashed amber from base, F_y y_hat dashed teal from tip of F_x x_hat,
    # and F solid red from base to tip of F_y y_hat.
    bx0, by0 = 6.66, 0.90
    p_base = (bx0, by0)
    p_x_tip = (bx0 + dx_mag, by0)
    p_f_tip = (bx0 + dx_mag, by0 + dy_mag)

    draw_arrow_2d(
        ax_b, p_base, p_x_tip, color=AMBER, lw=2.0, ls="--", head_length=6.0, head_width=3.6, zorder=6
    )
    draw_arrow_2d(
        ax_b, p_x_tip, p_f_tip, color=TEAL, lw=2.0, ls="--", head_length=5.8, head_width=3.5, zorder=6
    )
    draw_arrow_2d(
        ax_b, p_base, p_f_tip, color=RED, lw=2.5, ls="-", head_length=6.6, head_width=4.0, zorder=7
    )
    ax_b.scatter([bx0], [by0], s=28, color=NAVY, zorder=8)

    ax_b.text(
        bx0 + 0.50 * dx_mag,
        by0 - 0.14,
        r"$F_x\hat{\mathbf{x}}$",
        ha="center",
        va="top",
        fontsize=9.8,
        fontweight="bold",
        color=AMBER,
        zorder=8,
    )
    ax_b.text(
        bx0 + dx_mag + 0.13,
        by0 + 0.48 * dy_mag,
        r"$F_y\hat{\mathbf{y}}$",
        ha="left",
        va="center",
        fontsize=9.8,
        fontweight="bold",
        color=TEAL,
        zorder=8,
    )
    ax_b.text(
        bx0 + 0.44 * dx_mag - 0.08,
        by0 + 0.52 * dy_mag + 0.10,
        r"$\mathbf{F}$",
        ha="right",
        va="bottom",
        fontsize=10.5,
        fontweight="bold",
        color=RED,
        zorder=8,
    )

    # Key arrow ("5 m/s") centered inside upper-right box using the exact same quiver scale
    key_len = key_speed / q_scale
    kx0 = kbox_x0 + 0.5 * (kbox_w - key_len)
    ky0 = kbox_y0 + 0.92
    key_box = FancyBboxPatch(
        (kbox_x0, kbox_y0),
        kbox_w,
        kbox_h,
        boxstyle="round,pad=0.05,rounding_size=0.14",
        facecolor="white",
        edgecolor=NAVY,
        linewidth=1.0,
        alpha=0.96,
        zorder=8,
    )
    ax_b.add_patch(key_box)
    ax_b.quiver(
        [kx0],
        [ky0],
        [key_speed],
        [0.0],
        angles="xy",
        scale_units="xy",
        scale=q_scale,
        color=NAVY,
        width=0.0075,
        headwidth=3.8,
        headlength=4.6,
        headaxislength=4.0,
        zorder=9,
    )
    ax_b.text(
        kbox_x0 + 0.5 * kbox_w,
        kbox_y0 + 0.36,
        f"{key_speed:.0f} m/s",
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=NAVY,
        zorder=9,
    )

    ax_b.set_xlim(0.0, 10.0)
    ax_b.set_ylim(0.0, 10.0)
    ax_b.set_aspect("equal")
    ax_b.set_xticks([0, 2, 4, 6, 8, 10])
    ax_b.set_yticks([0, 2, 4, 6, 8, 10])
    ax_b.set_xlabel("$x$ (km)", color=TEXT)
    ax_b.set_ylabel("$y$ (km)", color=TEXT)
    ax_b.set_title(
        r"(b) Vector field: wind $\mathbf{F}(x, y)$ ($F_z = 0$)",
        fontweight="bold",
        color=TEXT,
        pad=8,
    )

    save_fig(fig, out_dir, "maths1_scalar_vector_fields.png")

    info = {
        "domain_km": [0, 10],
        "temp_min_C": round(t_min, 1),
        "temp_max_C": round(t_max, 1),
        "isotherms_C": [int(v) for v in iso_levels],
        "point_1_km": list(pt1),
        "point_1_temp_C": round(t1, 1),
        "point_2_km": list(pt2),
        "point_2_temp_C": round(t2, 1),
        "wind_grid": f"{n_grid}x{n_grid}",
        "wind_key_ms": int(key_speed),
        "low_centre_km": [xc_low, yc_low],
        "wind_speed_min_ms": round(speed_min, 1),
        "wind_speed_max_ms": round(speed_max, 1),
        "highlight_point_km": [int(round(xh)), int(round(yh))],
        "highlight_Fx_ms": round(fx_h, 1),
        "highlight_Fy_ms": round(fy_h, 1),
        "highlight_Fz_ms": 0,
        "highlight_speed_ms": round(sp_h, 1),
        "inset_magnification": inset_mag,
    }
    print(
        f"[Fig 1] Domain 0..10 km by 0..10 km; T range [{t_min:.1f}, {t_max:.1f}] deg C; "
        f"isotherms {info['isotherms_C']} deg C; "
        f"2 marked points ({pt1[0]:.1f}, {pt1[1]:.1f}) km -> {t1:.1f} deg C and "
        f"({pt2[0]:.1f}, {pt2[1]:.1f}) km -> {t2:.1f} deg C; "
        f"wind {n_grid}x{n_grid} grid, key arrow = {key_speed:.0f} m/s, "
        f"low centre ({xc_low:.1f}, {yc_low:.1f}) km, "
        f"highlighted point ({xh:.0f}, {yh:.0f}) km has F_x = {fx_h:.1f} m/s, "
        f"F_y = {fy_h:.1f} m/s, F_z = 0 m/s (speed {sp_h:.1f} m/s), "
        f"inset magnified x{inset_mag}."
    )
    return info


# ===========================================================================
# Figure 2: maths1_divergence_theorem_cubes.png
# ===========================================================================
def make_fig2_divergence_cubes(out_dir: Path) -> dict[str, object]:
    fig = plt.figure(figsize=(10.7, 5.3), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.18, 1.0], wspace=0.10)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1])

    # --- Panel (a): Two adjacent boxes in oblique view ---
    ax_a.set_xlim(-0.35, 6.85)
    ax_a.set_ylim(-1.95, 4.15)
    ax_a.set_aspect("equal")
    ax_a.axis("off")
    ax_a.text(
        3.25,
        3.92,
        r"(a) Two adjacent boxes sharing the face at $x + \frac{\Delta x}{2}$",
        ha="center",
        va="center",
        fontsize=10.4,
        fontweight="bold",
        color=TEXT,
    )

    sx = 2.35
    sy_x, sy_y = 0.82, 0.62
    sz = 1.95
    ox, oy = 0.45, 0.55

    def proj(X: float, Y: float, Z: float) -> tuple[float, float]:
        return (ox + sx * X + sy_x * Y, oy + sz * Z + sy_y * Y)

    b1_front = [proj(0, 0, 0), proj(1, 0, 0), proj(1, 0, 1), proj(0, 0, 1)]
    b1_top = [proj(0, 0, 1), proj(1, 0, 1), proj(1, 1, 1), proj(0, 1, 1)]
    b2_front = [proj(1, 0, 0), proj(2, 0, 0), proj(2, 0, 1), proj(1, 0, 1)]
    b2_top = [proj(1, 0, 1), proj(2, 0, 1), proj(2, 1, 1), proj(1, 1, 1)]
    b2_right = [proj(2, 0, 0), proj(2, 1, 0), proj(2, 1, 1), proj(2, 0, 1)]
    shared_face = [proj(1, 0, 0), proj(1, 1, 0), proj(1, 1, 1), proj(1, 0, 1)]

    ax_a.add_patch(Polygon(b1_top, closed=True, fc=BLUE_LIGHT, ec="none", alpha=0.45, zorder=1))
    ax_a.add_patch(Polygon(b1_front, closed=True, fc=BLUE_LIGHT, ec="none", alpha=0.38, zorder=1))
    ax_a.add_patch(Polygon(b2_top, closed=True, fc=TEAL_LIGHT, ec="none", alpha=0.45, zorder=1))
    ax_a.add_patch(Polygon(b2_front, closed=True, fc=TEAL_LIGHT, ec="none", alpha=0.38, zorder=1))
    ax_a.add_patch(Polygon(b2_right, closed=True, fc=TEAL_LIGHT, ec="none", alpha=0.50, zorder=1))

    hidden_segments = [
        (proj(0, 0, 0), proj(0, 1, 0)),
        (proj(0, 1, 0), proj(1, 1, 0)),
        (proj(0, 1, 0), proj(0, 1, 1)),
        (proj(1, 1, 0), proj(2, 1, 0)),
    ]
    for p_s, p_e in hidden_segments:
        ax_a.plot([p_s[0], p_e[0]], [p_s[1], p_e[1]], color=SLATE, lw=1.1, ls=":", alpha=0.65, zorder=2)

    ax_a.add_patch(
        Polygon(shared_face, closed=True, fc=AMBER_LIGHT, ec=AMBER, lw=2.2, alpha=0.82, zorder=3)
    )

    b1_edges = [
        (proj(0, 0, 0), proj(1, 0, 0)),
        (proj(0, 0, 1), proj(1, 0, 1)),
        (proj(0, 0, 0), proj(0, 0, 1)),
        (proj(0, 0, 1), proj(0, 1, 1)),
        (proj(0, 1, 1), proj(1, 1, 1)),
    ]
    for p_s, p_e in b1_edges:
        ax_a.plot([p_s[0], p_e[0]], [p_s[1], p_e[1]], color=BLUE, lw=2.0, zorder=4)

    b2_edges = [
        (proj(1, 0, 0), proj(2, 0, 0)),
        (proj(1, 0, 1), proj(2, 0, 1)),
        (proj(2, 0, 0), proj(2, 0, 1)),
        (proj(1, 1, 1), proj(2, 1, 1)),
        (proj(2, 0, 1), proj(2, 1, 1)),
        (proj(2, 0, 0), proj(2, 1, 0)),
        (proj(2, 1, 0), proj(2, 1, 1)),
    ]
    for p_s, p_e in b2_edges:
        ax_a.plot([p_s[0], p_e[0]], [p_s[1], p_e[1]], color=TEAL, lw=2.0, zorder=4)

    for p_s, p_e in [(proj(1, 0, 0), proj(1, 0, 1)), (proj(1, 0, 1), proj(1, 1, 1))]:
        ax_a.plot([p_s[0], p_e[0]], [p_s[1], p_e[1]], color=AMBER, lw=2.4, zorder=5)

    c_top1 = proj(0.45, 0.52, 1.0)
    c_top2 = proj(1.52, 0.52, 1.0)
    ax_a.text(c_top1[0], c_top1[1] + 0.30, "Box 1", ha="center", va="bottom", fontsize=10.2, fontweight="bold", color=BLUE)
    ax_a.text(c_top2[0], c_top2[1] + 0.30, "Box 2", ha="center", va="bottom", fontsize=10.2, fontweight="bold", color=TEAL)

    p_dz_b, p_dz_t = proj(2, 1, 0), proj(2, 1, 1)
    ax_a.text(p_dz_b[0] + 0.16, 0.5 * (p_dz_b[1] + p_dz_t[1]), r"$\Delta z$", ha="left", va="center", fontsize=9.8, color=SLATE)
    p_dy_f, p_dy_b = proj(2, 0, 0), proj(2, 1, 0)
    ax_a.text(0.5 * (p_dy_f[0] + p_dy_b[0]) + 0.24, 0.5 * (p_dy_f[1] + p_dy_b[1]) - 0.12, r"$\Delta y$", ha="left", va="top", fontsize=9.8, color=SLATE)

    # Arrows on the shared face X = 1 (with properly scaled arrowheads!)
    lbl_bg = dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.88)

    # 1. Single field arrow F pointing mainly along +x with a slight upward tilt
    p_F = proj(1.0, 0.55, 0.66)
    F_tip = (p_F[0] + 1.18, p_F[1] + 0.34)
    ax_a.scatter([p_F[0]], [p_F[1]], s=30, color=RED, zorder=8)
    draw_arrow_2d(ax_a, p_F, F_tip, color=RED, lw=2.6, head_length=7.0, head_width=4.2, zorder=8)
    ax_a.text(
        F_tip[0] + 0.08,
        F_tip[1] + 0.03,
        r"$\mathbf{F}$",
        ha="left",
        va="center",
        fontsize=11.0,
        fontweight="bold",
        color=RED,
        bbox=lbl_bg,
        zorder=9,
    )

    # 2. Box 1 outward normal n_1 = +x_hat (BLUE), pointing into Box 2
    p_n1 = proj(1.0, 0.45, 0.40)
    n1_tip = (p_n1[0] + 0.92, p_n1[1])
    ax_a.scatter([p_n1[0]], [p_n1[1]], s=24, color=BLUE, zorder=8)
    draw_arrow_2d(ax_a, p_n1, n1_tip, color=BLUE, lw=2.3, head_length=6.2, head_width=3.8, zorder=8)
    ax_a.text(
        n1_tip[0] + 0.08,
        n1_tip[1],
        r"$\hat{\mathbf{n}}_1 = +\hat{\mathbf{x}}$",
        ha="left",
        va="center",
        fontsize=9.6,
        fontweight="bold",
        color=BLUE,
        bbox=lbl_bg,
        zorder=9,
    )

    # 3. Box 2 outward normal n_2 = -x_hat (TEAL), pointing into Box 1
    p_n2 = proj(1.0, 0.35, 0.22)
    n2_tip = (p_n2[0] - 0.92, p_n2[1])
    ax_a.scatter([p_n2[0]], [p_n2[1]], s=24, color=TEAL, zorder=8)
    draw_arrow_2d(ax_a, p_n2, n2_tip, color=TEAL, lw=2.3, head_length=6.2, head_width=3.8, zorder=8)
    ax_a.text(
        n2_tip[0] - 0.08,
        n2_tip[1],
        r"$\hat{\mathbf{n}}_2 = -\hat{\mathbf{x}}$",
        ha="right",
        va="center",
        fontsize=9.6,
        fontweight="bold",
        color=TEAL,
        bbox=lbl_bg,
        zorder=9,
    )

    # Three x labels along bottom front edge
    x_ticks_3d = [
        (0.0, r"$x - \frac{\Delta x}{2}$", BLUE),
        (1.0, r"$x + \frac{\Delta x}{2}$", AMBER),
        (2.0, r"$x + \frac{3\Delta x}{2}$", TEAL),
    ]
    for xv, xlbl, xcol in x_ticks_3d:
        px, py = proj(xv, 0.0, 0.0)
        ax_a.plot([px, px], [py, py - 0.18], color=xcol, lw=1.5, zorder=5)
        ax_a.text(px, py - 0.24, xlbl, ha="center", va="top", fontsize=10.2, fontweight="bold", color=xcol)

    # Flux cancellation card below
    draw_card(ax_a, 0.05, -1.88, 6.45, 1.62, fc=GREY_BG, ec=GREY_LINE)
    ax_a.text(
        0.28,
        -0.58,
        r"Box 1:  $\mathbf{F}\cdot\hat{\mathbf{n}}_1\,\Delta y\,\Delta z = +F_x\!\left(x + \frac{\Delta x}{2}\right)\Delta y\,\Delta z$",
        ha="left",
        va="center",
        fontsize=9.6,
        color=BLUE,
    )
    ax_a.text(
        0.28,
        -1.08,
        r"Box 2:  $\mathbf{F}\cdot\hat{\mathbf{n}}_2\,\Delta y\,\Delta z = -F_x\!\left(x + \frac{\Delta x}{2}\right)\Delta y\,\Delta z$",
        ha="left",
        va="center",
        fontsize=9.6,
        color=TEAL,
    )
    ax_a.text(
        0.28,
        -1.56,
        r"Sum on shared face $= 0$",
        ha="left",
        va="center",
        fontsize=9.8,
        fontweight="bold",
        color=NAVY,
    )

    # --- Panel (b): Whole volume cut into small cells (2D cross-section) ---
    ax_b.set_xlim(-3.05, 3.05)
    ax_b.set_ylim(-2.95, 3.15)
    ax_b.set_aspect("equal")
    ax_b.axis("off")
    ax_b.text(
        0.0,
        2.92,
        r"(b) Interior faces cancel; outer $\partial V$ remains",
        ha="center",
        va="center",
        fontsize=10.4,
        fontweight="bold",
        color=TEXT,
    )

    def r_curve(th: np.ndarray) -> np.ndarray:
        return 2.02 + 0.20 * np.cos(2.0 * th - 0.35) + 0.12 * np.sin(3.0 * th + 0.55)

    def dr_dth(th: np.ndarray) -> np.ndarray:
        return -0.40 * np.sin(2.0 * th - 0.35) + 0.36 * np.cos(3.0 * th + 0.55)

    th_fine = np.linspace(0.0, 2.0 * np.pi, 400)
    rr_fine = r_curve(th_fine)
    xb_curve = rr_fine * np.cos(th_fine)
    yb_curve = rr_fine * np.sin(th_fine)
    pts_curve = np.column_stack([xb_curve, yb_curve])

    vol_patch = Polygon(pts_curve, closed=True, facecolor=BLUE_PALE, edgecolor="none", zorder=1)
    ax_b.add_patch(vol_patch)

    h_cell = 0.62
    grid_vals = np.arange(-2.48, 2.50, h_cell)
    for gv in grid_vals:
        lv, = ax_b.plot([gv, gv], [-2.6, 2.6], color="#94a3b8", lw=1.0, zorder=2)
        lv.set_clip_path(vol_patch)
        lh, = ax_b.plot([-2.6, 2.6], [gv, gv], color="#94a3b8", lw=1.0, zorder=2)
        lh.set_clip_path(vol_patch)

    ax_b.plot(xb_curve, yb_curve, color=NAVY, lw=2.4, zorder=5)
    ax_b.text(-0.93, -0.93, r"$V$", ha="center", va="center", fontsize=11.5, fontweight="bold", color=NAVY, zorder=7)
    ax_b.text(1.56, -1.78, r"$\partial V$", fontsize=11.0, fontweight="bold", color=NAVY, zorder=7)

    # Four interior shared faces with opposite short grey arrows
    cancel_specs = [
        (-0.62, 0.93, "v"),
        (0.62, -0.31, "v"),
        (-0.31, -0.62, "h"),
        (0.31, 0.62, "h"),
    ]
    for ex, ey, orient in cancel_specs:
        if orient == "v":
            ax_b.plot([ex, ex], [ey - 0.24, ey + 0.24], color=AMBER, lw=2.3, zorder=4)
            draw_arrow_2d(ax_b, (ex, ey + 0.08), (ex + 0.28, ey + 0.08), color=SLATE, lw=1.6, head_length=4.5, head_width=2.8, zorder=6)
            draw_arrow_2d(ax_b, (ex, ey - 0.08), (ex - 0.28, ey - 0.08), color=SLATE, lw=1.6, head_length=4.5, head_width=2.8, zorder=6)
        else:
            ax_b.plot([ex - 0.24, ex + 0.24], [ey, ey], color=AMBER, lw=2.3, zorder=4)
            draw_arrow_2d(ax_b, (ex + 0.08, ey), (ex + 0.08, ey + 0.28), color=SLATE, lw=1.6, head_length=4.5, head_width=2.8, zorder=6)
            draw_arrow_2d(ax_b, (ex - 0.08, ey), (ex - 0.08, ey - 0.28), color=SLATE, lw=1.6, head_length=4.5, head_width=2.8, zorder=6)

    cancel_bbox = dict(boxstyle="round,pad=0.16", fc="white", ec=SLATE, lw=0.9, alpha=0.95)
    ax_b.annotate(
        "cancel",
        xy=(-0.62, 0.96),
        xytext=(-0.85, 1.56),
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=SLATE,
        bbox=cancel_bbox,
        arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.1, shrinkB=5),
        zorder=8,
    )
    ax_b.annotate(
        "cancel",
        xy=(0.62, -0.31),
        xytext=(0.95, -1.08),
        ha="center",
        va="center",
        fontsize=9.5,
        fontweight="bold",
        color=SLATE,
        bbox=cancel_bbox,
        arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.1, shrinkB=5),
        zorder=8,
    )

    # Exact analytic outward unit normals n_hat along outer boundary curve dV
    n_normals = 12
    th_n = np.linspace(0.18, 2.0 * np.pi + 0.18, n_normals, endpoint=False)
    rr_n = r_curve(th_n)
    drr_n = dr_dth(th_n)
    tx = drr_n * np.cos(th_n) - rr_n * np.sin(th_n)
    ty = drr_n * np.sin(th_n) + rr_n * np.cos(th_n)
    t_norm = np.hypot(tx, ty)
    nx = ty / t_norm
    ny = -tx / t_norm
    bx = rr_n * np.cos(th_n)
    by = rr_n * np.sin(th_n)
    assert np.all(bx * nx + by * ny > 0.0), "Outward normal orientation check failed"

    n_len = 0.44
    for i in range(n_normals):
        draw_arrow_2d(
            ax_b,
            (float(bx[i]), float(by[i])),
            (float(bx[i] + n_len * nx[i]), float(by[i] + n_len * ny[i])),
            color=RED,
            lw=1.9,
            head_length=5.5,
            head_width=3.3,
            zorder=7,
        )

    for idx_lbl in (1, 6):
        lx = bx[idx_lbl] + (n_len + 0.24) * nx[idx_lbl]
        ly = by[idx_lbl] + (n_len + 0.24) * ny[idx_lbl]
        ax_b.text(lx, ly, r"$\hat{\mathbf{n}}$", ha="center", va="center", fontsize=10.5, fontweight="bold", color=RED, zorder=8)

    save_fig(fig, out_dir, "maths1_divergence_theorem_cubes.png")
    info = {
        "shared_face_sum": 0,
        "cancelled_interior_faces_shown": len(cancel_specs),
        "outer_normals_shown": n_normals,
    }
    print(
        f"[Fig 2] 2 adjacent boxes (Box 1: x - dx/2 to x + dx/2, Box 2: x + dx/2 to x + 3*dx/2); "
        f"shared face at x + dx/2 cancels (+Fx dy dz - Fx dy dz = 0); "
        f"{len(cancel_specs)} interior cancelled face pairs and {n_normals} outward normals shown."
    )
    return info


# ===========================================================================
# Figure 3: maths1_curl_paddle_wheels.png
# ===========================================================================
def draw_paddle_wheel(
    ax: plt.Axes,
    cx: float,
    cy: float,
    r_wheel: float = 0.18,
    amber_angle_deg: float = 90.0,
    spin: str = "none",
    zorder: int = 7,
) -> None:
    """Draw a 4-vane paddle wheel with one vane highlighted in amber and optional spin arc."""
    r_vane = 1.38 * r_wheel
    for k in range(4):
        ang = math.radians(amber_angle_deg + 90.0 * k)
        vx = cx + r_vane * math.cos(ang)
        vy = cy + r_vane * math.sin(ang)
        if k == 0:
            ax.plot([cx, vx], [cy, vy], color=AMBER, lw=3.2, solid_capstyle="round", zorder=zorder + 2)
            ax.scatter([vx], [vy], s=26, color=AMBER, edgecolor=TEXT, lw=0.6, zorder=zorder + 3)
        else:
            ax.plot([cx, vx], [cy, vy], color=NAVY, lw=2.0, solid_capstyle="round", zorder=zorder + 1)

    ring = Circle((cx, cy), r_wheel, facecolor="white", edgecolor=NAVY, lw=1.7, alpha=0.95, zorder=zorder)
    ax.add_patch(ring)
    ax.scatter([cx], [cy], s=18, color=NAVY, zorder=zorder + 3)

    if spin in ("ccw", "cw"):
        r_arc = 1.84 * r_wheel
        if spin == "ccw":
            th_s, th_e = math.radians(25.0), math.radians(155.0)
            rad_val = 0.45
        else:
            th_s, th_e = math.radians(155.0), math.radians(25.0)
            rad_val = -0.45
        p_s = (cx + r_arc * math.cos(th_s), cy + r_arc * math.sin(th_s))
        p_e = (cx + r_arc * math.cos(th_e), cy + r_arc * math.sin(th_e))
        arc = FancyArrowPatch(
            p_s,
            p_e,
            connectionstyle=f"arc3,rad={rad_val}",
            arrowstyle="-|>,head_length=5.2,head_width=3.2",
            mutation_scale=1.0,
            color=RED,
            lw=1.8,
            zorder=zorder + 4,
        )
        ax.add_patch(arc)


def make_fig3_curl_paddle_wheels(out_dir: Path) -> dict[str, object]:
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 4.6), dpi=DPI)
    fig.subplots_adjust(wspace=0.22)
    ax_a, ax_b, ax_c = axes

    v0 = 1.0
    h = 1.0
    lim = 1.88
    badge_box = dict(boxstyle="round,pad=0.18", fc="white", ec=NAVY, lw=0.9, alpha=0.94)

    # --- Panel (a): v = y_hat v_0 exp(-y^2 / h^2) ---
    xa = np.linspace(-1.45, 1.45, 5)
    ya = np.linspace(-1.35, 1.15, 5)
    XA, YA = np.meshgrid(xa, ya)
    UX_A = np.zeros_like(XA)
    UY_A = v0 * np.exp(-(YA**2) / (h**2))
    curl_a = 0.0

    ax_a.quiver(
        XA,
        YA,
        UX_A,
        UY_A,
        angles="xy",
        scale_units="xy",
        scale=1.95,
        color=BLUE,
        alpha=0.72,
        width=0.0085,
        headwidth=3.6,
        headlength=4.3,
        headaxislength=3.8,
        zorder=2,
    )
    draw_paddle_wheel(ax_a, 0.36, 0.42, r_wheel=0.20, amber_angle_deg=90.0, spin="none")
    ax_a.text(
        0.36,
        0.02,
        "no spin",
        ha="center",
        va="top",
        fontsize=9.5,
        fontweight="bold",
        color=NAVY,
        bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.88),
        zorder=9,
    )
    ax_a.text(
        0.0,
        -1.60,
        r"$\nabla\times\mathbf{v} = \mathbf{0}$,  $\nabla\cdot\mathbf{v} \neq 0$",
        ha="center",
        va="center",
        fontsize=9.6,
        fontweight="bold",
        color=NAVY,
        bbox=badge_box,
        zorder=10,
    )
    ax_a.set_xlim(-lim, lim)
    ax_a.set_ylim(-lim, lim)
    ax_a.set_aspect("equal")
    ax_a.set_xticks([-1.0, 0.0, 1.0])
    ax_a.set_xticklabels(["$-h$", "$0$", "$+h$"])
    ax_a.set_yticks([-1.0, 0.0, 1.0])
    ax_a.set_yticklabels(["$-h$", "$0$", "$+h$"])
    ax_a.set_xlabel("$x$", color=TEXT)
    ax_a.set_ylabel("$y$", color=TEXT)
    ax_a.set_title(r"(a) $\mathbf{v} = \hat{\mathbf{y}}\,v_0 e^{-y^2/h^2}$", fontweight="bold", color=TEXT, pad=8)

    # --- Panel (b): v = y_hat v_0 exp(-x^2 / h^2) ---
    xb = np.linspace(-1.55, 1.55, 7)
    yb = np.linspace(-1.35, 1.15, 5)
    XB, YB = np.meshgrid(xb, yb)
    UX_B = np.zeros_like(XB)
    UY_B = v0 * np.exp(-(XB**2) / (h**2))

    def curl_b_z(x_val: float) -> float:
        return -(2.0 * x_val * v0 / (h**2)) * math.exp(-(x_val**2) / (h**2))

    cz_left = curl_b_z(-0.5 * h)
    cz_mid = curl_b_z(0.0)
    cz_right = curl_b_z(+0.5 * h)
    assert cz_left > 0.0 and abs(cz_mid) < 1e-15 and cz_right < 0.0

    ax_b.quiver(
        XB,
        YB,
        UX_B,
        UY_B,
        angles="xy",
        scale_units="xy",
        scale=1.95,
        color=BLUE,
        alpha=0.65,
        width=0.0080,
        headwidth=3.5,
        headlength=4.2,
        headaxislength=3.7,
        zorder=2,
    )
    for xg_val in (-0.5 * h, 0.0, +0.5 * h):
        ax_b.axvline(xg_val, color=GREY_LINE, lw=0.9, ls=":", zorder=1)

    wheels_b = [
        (-0.5 * h, +0.72, "ccw", "CCW"),
        (0.0, 0.0, "none", "no spin"),
        (+0.5 * h, -0.72, "cw", "CW"),
    ]
    for wx, wy, wsp, wlbl in wheels_b:
        draw_paddle_wheel(ax_b, wx, wy, r_wheel=0.18, amber_angle_deg=90.0, spin=wsp)
        ly_off = 0.45 if wsp == "ccw" else (-0.36 if wsp == "none" else -0.43)
        ax_b.text(
            wx,
            wy + ly_off,
            wlbl,
            ha="center",
            va="center",
            fontsize=9.4,
            fontweight="bold",
            color=RED if wsp != "none" else NAVY,
            bbox=dict(boxstyle="round,pad=0.10", fc="white", ec="none", alpha=0.90),
            zorder=11,
        )

    ax_b.set_xlim(-lim, lim)
    ax_b.set_ylim(-lim, lim)
    ax_b.set_aspect("equal")
    ax_b.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
    ax_b.set_xticklabels(["$-h$", "$-\\frac{h}{2}$", "$0$", "$+\\frac{h}{2}$", "$+h$"])
    ax_b.set_yticks([-1.0, 0.0, 1.0])
    ax_b.set_yticklabels(["$-h$", "$0$", "$+h$"])
    ax_b.set_xlabel("$x$", color=TEXT)
    ax_b.set_title(r"(b) $\mathbf{v} = \hat{\mathbf{y}}\,v_0 e^{-x^2/h^2}$", fontweight="bold", color=TEXT, pad=8)

    # --- Panel (c): Irrotational vortex v = (k / r) phi_hat ---
    # Place arrows on 4 concentric rings with faint circular streamlines, scaled so that even
    # on the innermost ring r = 0.55 the arrow length (0.132 / 0.55 = 0.24) is shorter than
    # the smallest radial gap between rings (0.80 - 0.55 = 0.25), skipping any near the 4 wheels.
    k_vort = 0.132
    r_core = 0.28
    ring_radii = [0.55, 0.80, 1.25, 1.60]
    min_ring_gap = min(b - a for a, b in zip(ring_radii, ring_radii[1:]))
    assert k_vort / ring_radii[0] < min_ring_gap

    th_circ = np.linspace(0.0, 2.0 * np.pi, 240)
    for rv_s in ring_radii:
        ax_c.plot(rv_s * np.cos(th_circ), rv_s * np.sin(th_circ), color=GREY_LINE, lw=0.85, ls="-", zorder=1)
    # Dashed orbit circle r = 1 for the 4 paddle wheels
    ax_c.plot(np.cos(th_circ), np.sin(th_circ), color=SLATE, lw=1.15, ls="--", zorder=2)

    wheel_angles_deg = [0, 90, 180, 270]
    wheel_centres = [(math.cos(math.radians(a)), math.sin(math.radians(a))) for a in wheel_angles_deg]
    r_wheel_c = 0.17
    clearance = 1.65 * r_wheel_c  # 0.28: keeps arrows well off all 4 wheels and their amber tips

    pts_x, pts_y, vx_c, vy_c = [], [], [], []
    base_angles = np.linspace(15.0, 375.0, 12, endpoint=False)
    for rad in ring_radii:
        for deg in base_angles:
            ang_r = math.radians(float(deg))
            rx = rad * math.cos(ang_r)
            ry = rad * math.sin(ang_r)
            ux = -k_vort * ry / (rad**2)
            uy = +k_vort * rx / (rad**2)
            tx = rx + ux
            ty = ry + uy
            mx = rx + 0.5 * ux
            ty_m = ry + 0.5 * uy
            if any(
                min(
                    math.hypot(rx - wx, ry - wy),
                    math.hypot(mx - wx, ty_m - wy),
                    math.hypot(tx - wx, ty - wy),
                )
                < clearance
                for wx, wy in wheel_centres
            ):
                continue
            pts_x.append(rx)
            pts_y.append(ry)
            vx_c.append(ux)
            vy_c.append(uy)

    PX = np.array(pts_x)
    PY = np.array(pts_y)
    VXC = np.array(vx_c)
    VYC = np.array(vy_c)

    ax_c.quiver(
        PX,
        PY,
        VXC,
        VYC,
        angles="xy",
        scale_units="xy",
        scale=1.0,
        color=BLUE,
        alpha=0.80,
        width=0.0075,
        headwidth=3.8,
        headlength=4.4,
        headaxislength=3.9,
        zorder=3,
    )

    core = Circle((0.0, 0.0), r_core, facecolor="#e2e8f0", edgecolor=SLATE, lw=1.3, hatch="////", zorder=5)
    ax_c.add_patch(core)
    ax_c.text(
        0.0,
        1.72,
        r"$\mathbf{v}$ not defined at $r = 0$",
        ha="center",
        va="center",
        fontsize=9.2,
        color=SLATE,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=SLATE, lw=0.8, alpha=0.95),
        zorder=10,
    )
    ax_c.annotate(
        "",
        xy=(0.19, 0.21),
        xytext=(0.56, 1.54),
        arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.15, connectionstyle="arc3,rad=-0.10"),
        zorder=9,
    )

    for wx, wy in wheel_centres:
        draw_paddle_wheel(
            ax_c,
            wx,
            wy,
            r_wheel=r_wheel_c,
            amber_angle_deg=90.0,
            spin="none",
        )

    ax_c.text(
        0.0,
        -1.68,
        r"$\nabla\times\mathbf{v} = \mathbf{0}$ for $r > 0$",
        ha="center",
        va="center",
        fontsize=9.6,
        fontweight="bold",
        color=NAVY,
        bbox=badge_box,
        zorder=10,
    )
    ax_c.set_xlim(-1.95, 1.95)
    ax_c.set_ylim(-1.95, 1.95)
    ax_c.set_aspect("equal")
    ax_c.set_xticks([-1.0, 0.0, 1.0])
    ax_c.set_xticklabels(["$-1$", "$0$", "$+1$"])
    ax_c.set_yticks([-1.0, 0.0, 1.0])
    ax_c.set_yticklabels(["$-1$", "$0$", "$+1$"])
    ax_c.set_xlabel("$x$", color=TEXT)
    ax_c.set_title(r"(c) $\mathbf{v} = \frac{k}{r}\hat{\boldsymbol{\phi}}$", fontweight="bold", color=TEXT, pad=8)

    save_fig(fig, out_dir, "maths1_curl_paddle_wheels.png")
    info = {
        "panel_a_curl_z": curl_a,
        "panel_b_wheel_x_over_h": [-0.5, 0.0, 0.5],
        "panel_b_curl_z_norm": [round(cz_left, 2), 0.0, round(cz_right, 2)],
        "panel_c_orbit_r": 1,
        "panel_c_wheel_angles_deg": wheel_angles_deg,
        "panel_c_wheel_count": len(wheel_angles_deg),
        "panel_c_core_radius": r_core,
    }
    print(
        f"[Fig 3] 4-vane paddle wheels (1 amber vane); (a) max speed at y = 0, curl_z = 0; "
        f"(b) max speed at x = 0, 3 wheels at x/h = -1/2, 0, +1/2 have normalized "
        f"(curl v)_z = {cz_left:+.2f} (CCW), 0.00 (no spin), {cz_right:+.2f} (CW); "
        f"(c) {len(wheel_angles_deg)} wheels on r = 1 at {wheel_angles_deg} deg all keep "
        f"amber vane at 90 deg (straight up), curl = 0 for r > 0, core hatched inside r = {r_core:.2f}."
    )
    return info


# ===========================================================================
# Figure 4: maths1_stokes_loops.png
# ===========================================================================
def make_fig4_stokes_loops(out_dir: Path) -> dict[str, object]:
    fig = plt.figure(figsize=(10.7, 5.1), dpi=DPI)
    gs = fig.add_gridspec(1, 2, width_ratios=[1.02, 1.15], wspace=0.08)
    ax_a = fig.add_subplot(gs[0])
    ax_b = fig.add_subplot(gs[1], projection="3d", computed_zorder=False)

    # --- Panel (a): Two adjacent small square loops in the xy-plane ---
    ax_a.set_xlim(-2.60, 2.60)
    ax_a.set_ylim(-2.05, 2.15)
    ax_a.set_aspect("equal")
    ax_a.axis("off")
    fig.text(
        0.29,
        0.81,
        "(a) Two adjacent loops in the $xy$-plane",
        ha="center",
        va="center",
        fontsize=10.5,
        fontweight="bold",
        color=TEXT,
    )

    ox1, ox2 = -1.95, 1.95
    oy1, oy2 = -1.02, 1.02
    outer_rect = FancyBboxPatch(
        (ox1, oy1),
        ox2 - ox1,
        oy2 - oy1,
        boxstyle="round,pad=0.0,rounding_size=0.06",
        facecolor="none",
        edgecolor=NAVY,
        linewidth=2.8,
        zorder=2,
    )
    ax_a.add_patch(outer_rect)
    outer_arrows = [
        ((-0.26, oy1), (0.26, oy1)),     # bottom +x
        ((ox2, -0.24), (ox2, 0.24)),     # right +y
        ((0.26, oy2), (-0.26, oy2)),     # top -x
        ((ox1, 0.24), (ox1, -0.24)),     # left -y
    ]
    for p_s, p_e in outer_arrows:
        draw_arrow_2d(ax_a, p_s, p_e, color=NAVY, lw=2.8, head_length=7.0, head_width=4.4, zorder=4)

    ax_a.text(
        1.32,
        1.16,
        r"outer $C$ (CCW)",
        ha="center",
        va="bottom",
        fontsize=9.6,
        fontweight="bold",
        color=NAVY,
    )
    ax_a.text(
        -1.45,
        1.16,
        r"$\odot\;\hat{\mathbf{n}} = +\hat{\mathbf{z}}$",
        ha="center",
        va="bottom",
        fontsize=9.8,
        fontweight="bold",
        color=RED,
    )

    def draw_ccw_square_loop(x_l: float, x_r: float, y_b: float, y_t: float, col: str, fc_col: str) -> None:
        ax_a.add_patch(
            Polygon(
                [(x_l, y_b), (x_r, y_b), (x_r, y_t), (x_l, y_t)],
                closed=True,
                facecolor=fc_col,
                edgecolor=col,
                lw=1.9,
                alpha=0.52,
                zorder=3,
            )
        )
        xm = 0.5 * (x_l + x_r)
        ym = 0.5 * (y_b + y_t)
        segs = [
            ((xm - 0.24, y_b), (xm + 0.24, y_b)),  # bottom +x
            ((x_r, ym - 0.26), (x_r, ym + 0.26)),  # right +y
            ((xm + 0.24, y_t), (xm - 0.24, y_t)),  # top -x
            ((x_l, ym + 0.26), (x_l, ym - 0.26)),  # left -y
        ]
        for s_pt, e_pt in segs:
            draw_arrow_2d(ax_a, s_pt, e_pt, color=col, lw=2.0, head_length=5.8, head_width=3.6, zorder=6)

    draw_ccw_square_loop(-1.72, -0.10, -0.82, 0.82, BLUE, BLUE_LIGHT)
    draw_ccw_square_loop(+0.10, +1.72, -0.82, 0.82, TEAL, TEAL_LIGHT)

    ax_a.plot([0.0, 0.0], [-0.82, 0.82], color=AMBER, lw=1.6, ls="--", zorder=5)
    ax_a.text(-0.92, 0.0, "Loop 1", ha="center", va="center", fontsize=9.8, fontweight="bold", color=BLUE, zorder=7)
    ax_a.text(+0.92, 0.0, "Loop 2", ha="center", va="center", fontsize=9.8, fontweight="bold", color=TEAL, zorder=7)

    ax_a.text(
        0.0,
        1.70,
        "cancel",
        ha="center",
        va="center",
        fontsize=9.6,
        fontweight="bold",
        color=AMBER,
        bbox=dict(boxstyle="round,pad=0.16", fc=AMBER_LIGHT, ec=AMBER, lw=1.0),
        zorder=8,
    )
    ax_a.annotate(
        "",
        xy=(-0.09, 0.32),
        xytext=(-0.10, 1.50),
        arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.15),
        zorder=7,
    )
    ax_a.annotate(
        "",
        xy=(+0.09, 0.32),
        xytext=(+0.10, 1.50),
        arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.15),
        zorder=7,
    )

    ax_a.text(
        -0.30,
        -1.58,
        r"$+F_y\,\Delta y$ (up)",
        ha="right",
        va="center",
        fontsize=9.7,
        fontweight="bold",
        color=BLUE,
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec=BLUE, lw=0.9),
        zorder=8,
    )
    ax_a.annotate(
        "",
        xy=(-0.10, -0.32),
        xytext=(-0.55, -1.38),
        arrowprops=dict(arrowstyle="->", color=BLUE, lw=1.2),
        zorder=7,
    )

    ax_a.text(
        +0.30,
        -1.58,
        r"$-F_y\,\Delta y$ (down)",
        ha="left",
        va="center",
        fontsize=9.7,
        fontweight="bold",
        color=TEAL,
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec=TEAL, lw=0.9),
        zorder=8,
    )
    ax_a.annotate(
        "",
        xy=(+0.10, -0.32),
        xytext=(+0.55, -1.38),
        arrowprops=dict(arrowstyle="->", color=TEAL, lw=1.2),
        zorder=7,
    )

    # --- Panel (b): Curved dome S over closed boundary curve C in 3D ---
    ax_b.set_facecolor("white")
    R0 = 1.30
    H = 0.88

    def dome_xyz(r: np.ndarray | float, phi: np.ndarray | float) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        ra, pa = np.broadcast_arrays(np.asarray(r, dtype=float), np.asarray(phi, dtype=float))
        x = ra * np.cos(pa)
        y = ra * np.sin(pa)
        z = H * (1.0 - (ra / R0) ** 2)
        return x, y, z

    def dome_tangent_and_normal(r: float, phi: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        """Return point p, orthonormal tangent basis (e1, e2), and upward unit normal n_hat."""
        x, y, z = dome_xyz(r, phi)
        p = np.array([float(x), float(y), float(z)])
        if r < 1e-8:
            e1 = np.array([1.0, 0.0, 0.0])
            e2 = np.array([0.0, 1.0, 0.0])
            n_hat = np.array([0.0, 0.0, 1.0])
            return p, e1, e2, n_hat
        dr = np.array([math.cos(phi), math.sin(phi), -2.0 * H * r / (R0**2)])
        dphi = np.array([-r * math.sin(phi), r * math.cos(phi), 0.0])
        cross = np.cross(dr, dphi)
        n_hat = cross / np.linalg.norm(cross)
        e1 = dr / np.linalg.norm(dr)
        e2 = np.cross(n_hat, e1)
        assert np.dot(np.cross(e1, e2), n_hat) > 1.0 - 1e-12
        return p, e1, e2, n_hat

    r_rings = np.linspace(0.0, R0, 6)
    phi_fine = np.linspace(0.0, 2.0 * np.pi, 96)
    RR, PP = np.meshgrid(np.linspace(0.0, R0, 36), phi_fine)
    XD, YD, ZD = dome_xyz(RR, PP)

    # Configure camera and limits first so ax_b.get_proj() gives the exact projection matrix
    ax_b.view_init(elev=44, azim=-52)
    ax_b.set_xlim(-1.45, 1.45)
    ax_b.set_ylim(-1.45, 1.45)
    ax_b.set_zlim(-0.28, 1.15)
    ax_b.set_box_aspect((1.0, 1.0, 0.56))
    ax_b.axis("off")

    fig.canvas.draw()
    proj_mat = ax_b.get_proj()
    proj_inv = np.linalg.inv(proj_mat)

    def rim_is_hidden(phi_arr: np.ndarray) -> np.ndarray:
        """Exact ray-dome occlusion check for rim points (R0 cos phi, R0 sin phi, 0).

        Uses proj_mat and its inverse to trace the exact perspective/orthographic viewing
        ray from each rim point toward the camera and checks whether that ray re-enters
        the dome 0 <= z <= H * (1 - (x^2 + y^2) / R0^2) for t > 0.
        """
        xr_c, yr_c, zr_c = dome_xyz(R0, phi_arr)
        sx_r, sy_r, sz_r = proj3d.proj_transform(xr_c, yr_c, zr_c, proj_mat)
        # Step slightly closer to camera (sz - delta) at the exact same screen pixel (sx, sy)
        near_h = proj_inv @ np.vstack([sx_r, sy_r, sz_r - 0.05, np.ones_like(sx_r)])
        qx = near_h[0] / near_h[3]
        qy = near_h[1] / near_h[3]
        qz = near_h[2] / near_h[3]
        vx = qx - xr_c
        vy = qy - yr_c
        vz = qz - zr_c
        # Verify ray projects back to the exact same (sx, sy)
        sx_chk, sy_chk, _ = proj3d.proj_transform(xr_c + 0.3 * vx, yr_c + 0.3 * vy, zr_c + 0.3 * vz, proj_mat)
        assert np.max(np.hypot(sx_chk - sx_r, sy_chk - sy_r)) < 1e-12
        assert np.all(vz > 0.0)
        # Quadratic dome entry derivative at t = 0+: -(2H/R0^2)*(x0*vx + y0*vy) - vz > 0
        deriv0 = -(2.0 * H / (R0**2)) * (xr_c * vx + yr_c * vy) - vz
        return deriv0 > 0.0

    # Sample rim C densely and split into hidden back arc (drawn underneath dome at zorder=1)
    # and visible front arc (drawn bold on top of dome at zorder=6)
    phi_c = np.linspace(0.0, 2.0 * np.pi, 721)
    xc, yc, zc = dome_xyz(R0, phi_c)
    assert np.all(xc[:-1] * np.diff(yc) - yc[:-1] * np.diff(xc) > 0.0)
    hidden_mask = rim_is_hidden(phi_c[:-1])
    assert np.any(hidden_mask) and np.any(~hidden_mask)

    # Group contiguous runs around the circle cleanly
    def plot_masked_runs(mask_bool: np.ndarray, col: str, lw: float, ls: str, alpha: float, zord: int) -> None:
        n_seg = len(mask_bool)
        in_run = False
        start_i = 0
        for i in range(n_seg + 1):
            active = bool(mask_bool[i]) if i < n_seg else False
            if active and not in_run:
                start_i = i
                in_run = True
            elif not active and in_run:
                sl = slice(start_i, i + 1)
                ax_b.plot(xc[sl], yc[sl], zc[sl], color=col, lw=lw, ls=ls, alpha=alpha, zorder=zord)
                in_run = False

    # 1. Hidden back part of C drawn FIRST underneath the dome surface as thin dashed lighter navy line
    plot_masked_runs(hidden_mask, col=NAVY, lw=1.6, ls="--", alpha=0.48, zord=1)

    # 2. Translucent dome surface + visible mesh lines above the hidden back rim
    ax_b.plot_surface(XD, YD, ZD, color=BLUE_LIGHT, alpha=0.46, edgecolor="none", shade=True, zorder=2)

    for rv in r_rings[1:-1]:
        xr, yr, zr = dome_xyz(rv, phi_fine)
        ax_b.plot(xr, yr, zr, color=SLATE, lw=0.75, alpha=0.60, zorder=3)
    n_spokes = 12
    for ks in range(n_spokes):
        ang = 2.0 * math.pi * ks / n_spokes
        rs = np.linspace(r_rings[1], R0, 25)
        xs, ys, zs = dome_xyz(rs, ang)
        ax_b.plot(xs, ys, zs, color=SLATE, lw=0.75, alpha=0.60, zorder=3)

    def add_3d_arrow(
        p_start: np.ndarray, p_end: np.ndarray, col: str, lw: float = 2.0, zord: int = 8
    ) -> None:
        ax_b.plot(
            [p_start[0], p_end[0]], [p_start[1], p_end[1]], [p_start[2], p_end[2]], color=col, lw=lw, zorder=zord
        )
        d = p_end - p_start
        d_norm = np.linalg.norm(d)
        if d_norm < 1e-9:
            return
        u = d / d_norm
        ref = np.array([0.0, 0.0, 1.0]) if abs(u[2]) < 0.9 else np.array([1.0, 0.0, 0.0])
        perp = np.cross(u, ref)
        perp /= np.linalg.norm(perp)
        hlen = min(0.11, 0.65 * d_norm)
        hw = 0.45 * hlen
        for sgn in (+1.0, -1.0):
            wing = p_end - hlen * u + sgn * hw * perp
            ax_b.plot(
                [p_end[0], wing[0]], [p_end[1], wing[1]], [p_end[2], wing[2]], color=col, lw=lw, zorder=zord
            )

    # 3. Visible front part of C drawn bold on top, with all 4 arrowheads on the visible arc
    plot_masked_runs(~hidden_mask, col=NAVY, lw=3.1, ls="-", alpha=1.0, zord=6)

    front_arrow_degs = (198.0, 256.0, 314.0, 18.0)
    for deg_arr in front_arrow_degs:
        ph0 = math.radians(deg_arr)
        ph1 = math.radians(deg_arr + 8.5)
        assert not bool(rim_is_hidden(np.array([ph0, ph1])).any()), (
            f"Boundary arrow at {deg_arr} deg falls on hidden arc!"
        )
        p0 = np.array(dome_xyz(R0, ph0), dtype=float)
        p1 = np.array(dome_xyz(R0, ph1), dtype=float)
        add_3d_arrow(p0, p1, NAVY, lw=2.8, zord=7)

    # 4. Five patch circulation loops + outward normals n_hat, all on visible viewer-facing patches
    patch_centres = [
        (0.0, 0.0),                        # apex patch
        (0.58, math.radians(-85.0)),       # mid-slope front-left
        (0.58, math.radians(-20.0)),       # mid-slope front-right
        (0.58, math.radians(-148.0)),      # mid-slope left
        (0.92, math.radians(-5.0)),        # front-right slope between mid-slope front-right patch and rim
    ]

    for idx_p, (rc, phic) in enumerate(patch_centres):
        pc, e1, e2, n_hat = dome_tangent_and_normal(rc, phic)
        assert n_hat[2] > 0.0

        alphas = np.linspace(0.18 * math.pi, 1.82 * math.pi, 36)
        rho_loop = 0.145
        loop_pts = []
        for al in alphas:
            cand = pc + rho_loop * (math.cos(al) * e1 + math.sin(al) * e2)
            r_cand = math.hypot(cand[0], cand[1])
            z_surf = H * (1.0 - (r_cand / R0) ** 2) + 0.015
            loop_pts.append([cand[0], cand[1], z_surf])
        LP = np.array(loop_pts)

        for j in range(len(LP) - 1):
            rel = LP[j] - np.array([pc[0], pc[1], pc[2] + 0.015])
            dvec = LP[j + 1] - LP[j]
            assert np.dot(np.cross(rel, dvec), n_hat) > 0.0
            assert rel[0] * dvec[1] - rel[1] * dvec[0] > 0.0

        sx2, sy2, _ = proj3d.proj_transform(LP[:, 0], LP[:, 1], LP[:, 2], proj_mat)
        cx2 = float(np.mean(sx2))
        cy2 = float(np.mean(sy2))
        signed_area_2d = float(np.sum((sx2[:-1] - cx2) * np.diff(sy2) - (sy2[:-1] - cy2) * np.diff(sx2)))
        assert signed_area_2d > 0.0, f"Rendered 2D screen loop {idx_p} is not CCW: {signed_area_2d}"

        ax_b.plot(LP[:, 0], LP[:, 1], LP[:, 2], color=TEAL, lw=1.9, zorder=7)
        add_3d_arrow(LP[-3], LP[-1], TEAL, lw=1.9)

        n_len_3d = 0.30
        add_3d_arrow(pc, pc + n_len_3d * n_hat, RED, lw=2.1)
        if idx_p in (0, 2):
            lbl_p = pc + (n_len_3d + 0.10) * n_hat
            ax_b.text(
                lbl_p[0],
                lbl_p[1],
                lbl_p[2],
                r"$\hat{\mathbf{n}}$",
                fontsize=10.2,
                fontweight="bold",
                color=RED,
                ha="center",
                va="bottom",
            )

    # Place boundary C label clearly on the right side of the rim above the bottom formula card
    ax_b.text(
        R0 * math.cos(math.radians(-10.0)) + 0.14,
        R0 * math.sin(math.radians(-10.0)) + 0.08,
        0.04,
        r"$C$ (CCW)",
        fontsize=9.8,
        fontweight="bold",
        color=NAVY,
        ha="left",
        va="center",
    )
    ax_b.text(
        -0.95,
        0.72,
        0.54,
        r"$S$",
        fontsize=11.5,
        fontweight="bold",
        color=BLUE,
    )

    fig.text(
        0.72,
        0.81,
        "(b) Capped dome $S$ over boundary $C$",
        ha="center",
        va="center",
        fontsize=10.5,
        fontweight="bold",
        color=TEXT,
    )

    ax_b.text2D(
        0.50,
        0.02,
        r"$\iint_S (\nabla\times\mathbf{F})\cdot\hat{\mathbf{n}}\,dS = \oint_C \mathbf{F}\cdot\hat{\mathbf{t}}\,ds$"
        "\nRight-hand rule: fingers curl along $C$, thumb along $\\hat{\\mathbf{n}}$",
        transform=ax_b.transAxes,
        ha="center",
        va="bottom",
        fontsize=9.3,
        color=TEXT,
        bbox=dict(boxstyle="round,pad=0.22", fc=GREY_BG, ec=GREY_LINE, lw=0.9),
    )

    save_fig(fig, out_dir, "maths1_stokes_loops.png")
    info = {
        "shared_edge_sum": 0,
        "dome_radius": R0,
        "dome_height": H,
        "dome_patches_highlighted": len(patch_centres),
        "all_loops_ccw_verified": True,
    }
    print(
        f"[Fig 4] 2 adjacent CCW loops in xy-plane, shared vertical edge cancels (+Fy dy - Fy dy = 0); "
        f"3D dome S (R = {R0:.2f}, H = {H:.2f}) has {len(patch_centres)} patch circulation loops "
        f"and boundary C verified CCW in 3D, top-down xy, and rendered 2D screen projection."
    )
    return info


# ===========================================================================
# Figure 5: maths1_gradient_steepest_ascent.png
# ===========================================================================
def hill_f(x: np.ndarray | float, y: np.ndarray | float) -> np.ndarray | float:
    """Smooth elliptical Gaussian hill f(x, y) = exp(-(x^2 / 4 + y^2))."""
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    return np.exp(-(0.25 * xa**2 + ya**2))


def hill_grad(
    x: np.ndarray | float, y: np.ndarray | float
) -> tuple[np.ndarray, np.ndarray]:
    """Exact gradient grad f = (-x/2, -2y) * f(x, y)."""
    xa = np.asarray(x, dtype=float)
    ya = np.asarray(y, dtype=float)
    fv = hill_f(xa, ya)
    return -0.5 * xa * fv, -2.0 * ya * fv


def make_fig5_gradient_steepest_ascent(out_dir: Path) -> dict[str, object]:
    fig = plt.figure(figsize=(10.6, 8.2), dpi=DPI)
    gs = fig.add_gridspec(2, 2, height_ratios=[1.0, 1.08], hspace=0.28, wspace=0.20)
    ax_a = fig.add_subplot(gs[0, 0], projection="3d", computed_zorder=False)
    ax_b = fig.add_subplot(gs[0, 1])
    ax_c = fig.add_subplot(gs[1, :])

    xP, yP = 1.2, 0.6
    fP = float(hill_f(xP, yP))
    gxP_arr, gyP_arr = hill_grad(xP, yP)
    gxP, gyP = float(gxP_arr), float(gyP_arr)
    grad_norm = math.hypot(gxP, gyP)

    c_levels = [0.25, 0.45, 0.65, 0.85]

    # --- Panel (a): 3D surface z = f(x, y) + projected floor contours + steepest uphill arrow ---
    ax_a.set_facecolor("white")
    x3 = np.linspace(-2.4, 2.4, 80)
    y3 = np.linspace(-1.7, 1.7, 70)
    X3, Y3 = np.meshgrid(x3, y3)
    Z3 = hill_f(X3, Y3)
    z_floor = -0.34

    ax_a.contour(
        X3, Y3, Z3, levels=c_levels, zdir="z", offset=z_floor, colors=SLATE, linewidths=1.0, zorder=1
    )

    # Projected grad f arrow on the floor (drawn under translucent surface, above floor contours)
    eps_step = 0.85
    tip_floor = np.array([xP + eps_step * gxP, yP + eps_step * gyP, z_floor])
    ax_a.plot([xP, tip_floor[0]], [yP, tip_floor[1]], [z_floor, z_floor], color=NAVY, lw=2.2, zorder=2)
    ax_a.scatter([xP], [yP], [z_floor], s=28, color=AMBER, edgecolor=TEXT, lw=0.6, zorder=3)
    ax_a.plot([xP, xP], [yP, yP], [z_floor, fP], color=AMBER, lw=1.3, ls=":", zorder=3)
    ax_a.text(
        tip_floor[0] - 0.18,
        tip_floor[1] - 0.14,
        z_floor,
        r"$\nabla f$",
        fontsize=9.8,
        fontweight="bold",
        color=NAVY,
        zorder=3,
    )

    ax_a.plot_surface(
        X3, Y3, Z3, cmap="Blues", alpha=0.66, edgecolor="none", antialiased=True, zorder=4
    )

    # Point P and steepest uphill tangent arrow rendered cleanly ON TOP of front-facing slope
    ax_a.scatter([xP], [yP], [fP], s=54, color=AMBER, edgecolor=TEXT, lw=1.0, zorder=8)
    p_surf = np.array([xP, yP, fP])
    step_surf = eps_step * np.array([gxP, gyP, grad_norm**2])
    tip_surf = p_surf + step_surf
    ax_a.plot(
        [p_surf[0], tip_surf[0]],
        [p_surf[1], tip_surf[1]],
        [p_surf[2], tip_surf[2]],
        color=RED,
        lw=2.8,
        zorder=9,
    )
    u3 = step_surf / np.linalg.norm(step_surf)
    perp3 = np.cross(u3, np.array([0.0, 0.0, 1.0]))
    perp3 /= np.linalg.norm(perp3)
    for sgn in (+1.0, -1.0):
        w_pt = tip_surf - 0.14 * u3 + sgn * 0.065 * perp3
        ax_a.plot([tip_surf[0], w_pt[0]], [tip_surf[1], w_pt[1]], [tip_surf[2], w_pt[2]], color=RED, lw=2.6, zorder=9)

    ax_a.text(
        xP - 0.16,
        yP + 0.24,
        fP + 0.04,
        r"$P$",
        fontsize=10.5,
        fontweight="bold",
        color=AMBER,
        bbox=dict(boxstyle="round,pad=0.08", fc="white", ec="none", alpha=0.82),
        zorder=10,
    )
    ax_a.text(
        tip_surf[0] + 0.15,
        tip_surf[1] + 0.32,
        tip_surf[2] + 0.16,
        "steepest uphill",
        fontsize=9.3,
        fontweight="bold",
        color=RED,
        ha="center",
        bbox=dict(boxstyle="round,pad=0.12", fc="white", ec=RED, lw=0.8, alpha=0.90),
        zorder=10,
    )

    ax_a.view_init(elev=27, azim=38)
    ax_a.set_xlim(-2.4, 2.4)
    ax_a.set_ylim(-1.7, 1.7)
    ax_a.set_zlim(z_floor, 1.08)
    ax_a.set_box_aspect((1.35, 1.0, 0.78))
    ax_a.set_xticks([-2, 0, 2])
    ax_a.set_yticks([-1, 0, 1])
    ax_a.set_zticks([0.0, 0.5, 1.0])
    ax_a.set_xlabel("$x$", labelpad=2)
    ax_a.set_ylabel("$y$", labelpad=2)
    ax_a.set_zlabel("$f$", labelpad=1)
    ax_a.set_title(r"(a) Surface $z = f(x, y)$ and uphill arrow at $P$", fontweight="bold", color=TEXT, pad=6)

    # --- Panel (b): 2D contour map of f + coarse grid of grad f arrows ---
    xb = np.linspace(-2.5, 2.5, 240)
    yb = np.linspace(-1.75, 1.75, 180)
    XB, YB = np.meshgrid(xb, yb)
    FB = hill_f(XB, YB)

    ax_b.contourf(XB, YB, FB, levels=np.linspace(0.0, 1.0, 21), cmap="Blues", alpha=0.42, zorder=1)
    cs_b = ax_b.contour(XB, YB, FB, levels=c_levels, colors=NAVY, linewidths=1.2, linestyles="solid", zorder=3)

    # Place contour labels in arrow-free corridors (x = +/-0.35 for inner 3 contours, left flank for 0.25)
    manual_pts = [
        (-2.31, 0.22),
        (-0.35, -math.sqrt(-math.log(0.45) - 0.25 * 0.35**2)),
        (+0.35, -math.sqrt(-math.log(0.65) - 0.25 * 0.35**2)),
        (-0.35, -math.sqrt(-math.log(0.85) - 0.25 * 0.35**2)),
    ]
    ax_b.clabel(cs_b, fmt="%.2f", fontsize=9.2, manual=manual_pts)

    xq = np.linspace(-2.1, 2.1, 7)
    yq = np.linspace(-1.4, 1.4, 7)
    XQ, YQ = np.meshgrid(xq, yq)
    GXQ, GYQ = hill_grad(XQ, YQ)

    ax_b.quiver(
        XQ,
        YQ,
        GXQ,
        GYQ,
        angles="xy",
        scale_units="xy",
        scale=1.65,
        color=RED,
        alpha=0.85,
        width=0.0068,
        headwidth=3.6,
        headlength=4.3,
        headaxislength=3.8,
        zorder=5,
    )

    ax_b.scatter([xP], [yP], s=64, color=AMBER, edgecolor=TEXT, lw=1.1, zorder=8)
    ax_b.annotate(
        f"$P({xP:.1f}, {yP:.1f})$",
        xy=(xP, yP),
        xytext=(xP + 0.18, yP + 0.56),
        fontsize=9.6,
        fontweight="bold",
        color=TEXT,
        bbox=dict(boxstyle="round,pad=0.16", fc=AMBER_LIGHT, ec=AMBER, lw=0.9),
        arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.2, shrinkB=4),
        zorder=9,
    )

    ax_b.set_xlim(-2.5, 2.5)
    ax_b.set_ylim(-1.75, 1.75)
    ax_b.set_aspect("equal")
    ax_b.set_xlabel("$x$", color=TEXT)
    ax_b.set_ylabel("$y$", color=TEXT)
    ax_b.set_title(r"(b) Contours of $f$ and $\nabla f$ arrows", fontweight="bold", color=TEXT, pad=8)

    # --- Panel (c): Zoom at P = (1.2, 0.6) ---
    ax_c.set_xlim(xP - 1.28, xP + 1.55)
    ax_c.set_ylim(yP - 0.94, yP + 0.90)
    ax_c.set_aspect("equal")

    xc_g = np.linspace(xP - 1.32, xP + 1.6, 220)
    yc_g = np.linspace(yP - 0.98, yP + 0.94, 180)
    XC, YC = np.meshgrid(xc_g, yc_g)
    FC = hill_f(XC, YC)

    ax_c.contourf(XC, YC, FC, levels=np.linspace(0.0, 1.0, 26), cmap="Blues", alpha=0.25, zorder=1)
    ax_c.contour(XC, YC, FC, levels=[0.30, 0.40, 0.60, 0.70], colors=GREY_LINE, linewidths=0.9, linestyles="solid", zorder=2)
    ax_c.contour(XC, YC, FC, levels=[fP], colors=[NAVY], linewidths=2.3, linestyles="solid", zorder=3)

    u_grad = np.array([gxP, gyP]) / grad_norm
    phi_grad = math.atan2(u_grad[1], u_grad[0])

    u_tan = np.array([-u_grad[1], u_grad[0]])
    assert abs(np.dot(u_grad, u_tan)) < 1e-14
    s_tan = 0.72
    ax_c.plot(
        [xP - s_tan * u_tan[0], xP + s_tan * u_tan[0]],
        [yP - s_tan * u_tan[1], yP + s_tan * u_tan[1]],
        color=NAVY,
        lw=1.6,
        ls="--",
        zorder=4,
    )
    ax_c.text(
        0.52,
        1.10,
        f"contour $f = {fP:.2f}$\n(dashed tangent)",
        ha="center",
        va="center",
        fontsize=9.4,
        color=NAVY,
        bbox=dict(boxstyle="round,pad=0.15", fc="white", ec=NAVY, lw=0.85, alpha=0.95),
        zorder=8,
    )
    ax_c.annotate(
        "",
        xy=(xP - 0.44 * u_tan[0], yP - 0.44 * u_tan[1]),
        xytext=(0.64, 0.96),
        arrowprops=dict(arrowstyle="->", color=NAVY, lw=1.1),
        zorder=7,
    )

    # Common vector length scale L in Panel (c):
    # Each unit vector t_hat has length 1.0 * L, and grad f(P) is drawn to the EXACT same scale
    # with length ||grad f(P)|| * L = 0.6530 * L, so its orthogonal projection onto each t_hat
    # literally equals df/ds = ||grad f|| cos(theta).
    L_vec = 0.66
    len_grad_vis = grad_norm * L_vec
    grad_tip = (xP + len_grad_vis * u_grad[0], yP + len_grad_vis * u_grad[1])

    angles_deg = [0, 45, 90, 135, 180]
    df_ds_values: dict[int, float] = {}
    RED_DARK = "#991b1b"
    RED_LIGHT_VEC = "#ef4444"

    label_offsets = {
        0: (-0.08, -0.10, "right", "top"),
        45: (0.04, -0.11, "center", "top"),
        90: (0.10, -0.05, "left", "top"),
        135: (0.11, 0.02, "left", "center"),
        180: (0.09, 0.08, "left", "bottom"),
    }

    for th_d in angles_deg:
        th_r = phi_grad + math.radians(th_d)
        tx, ty = math.cos(th_r), math.sin(th_r)
        rate = gxP * tx + gyP * ty
        rate_formula = grad_norm * math.cos(math.radians(th_d))
        assert abs(rate - rate_formula) < 1e-13
        df_ds_values[th_d] = rate

        tip_t = (xP + L_vec * tx, yP + L_vec * ty)
        if th_d == 0:
            # Thin, lighter red unit vector t_hat at theta = 0 deg so thick dark grad f stands out on top
            draw_arrow_2d(
                ax_c, (xP, yP), tip_t, color=RED_LIGHT_VEC, lw=1.6, head_length=5.6, head_width=3.4, zorder=6
            )
            col_lbl = RED_LIGHT_VEC
        elif th_d == 90:
            draw_arrow_2d(ax_c, (xP, yP), tip_t, color=NAVY, lw=2.0, head_length=5.8, head_width=3.6, zorder=8)
            col_lbl = NAVY
        elif th_d == 180:
            draw_arrow_2d(ax_c, (xP, yP), tip_t, color=SLATE, lw=2.0, head_length=5.8, head_width=3.6, zorder=8)
            col_lbl = SLATE
        else:
            draw_arrow_2d(ax_c, (xP, yP), tip_t, color=TEAL, lw=2.0, head_length=5.8, head_width=3.6, zorder=8)
            col_lbl = TEAL

        ox_l, oy_l, ha_l, va_l = label_offsets[th_d]
        val_str = "0" if abs(rate) < 1e-12 else f"{rate:+.2f}"
        lbl_str = (
            rf"$\hat{{\mathbf{{t}}}}\;(\theta = 0^\circ)$: $df/ds = {val_str}$"
            if th_d == 0
            else rf"$\theta = {th_d}^\circ$: $df/ds = {val_str}$"
        )
        ax_c.text(
            tip_t[0] + ox_l,
            tip_t[1] + oy_l,
            lbl_str,
            ha=ha_l,
            va=va_l,
            fontsize=9.3,
            fontweight="bold",
            color=col_lbl,
            bbox=dict(boxstyle="round,pad=0.13", fc="white", ec=col_lbl, lw=0.8, alpha=0.95),
            zorder=9,
        )

    # Thick, dark gradient arrow grad f(P) of length 0.653 * L_vec on top of the theta = 0 unit vector
    draw_arrow_2d(
        ax_c, (xP, yP), grad_tip, color=RED_DARK, lw=3.6, head_length=7.4, head_width=4.6, zorder=9
    )
    ax_c.annotate(
        rf"$\nabla f(P)$" "\n" rf"$\Vert\nabla f\Vert = {grad_norm:.2f}$",
        xy=(xP + 0.62 * len_grad_vis * u_grad[0], yP + 0.62 * len_grad_vis * u_grad[1]),
        xytext=(0.45, 0.44),
        ha="center",
        va="center",
        fontsize=9.8,
        fontweight="bold",
        color=RED_DARK,
        bbox=dict(boxstyle="round,pad=0.16", fc="white", ec=RED_DARK, lw=0.95, alpha=0.96),
        arrowprops=dict(arrowstyle="->", color=RED_DARK, lw=1.2, shrinkB=3),
        zorder=10,
    )

    # Thin dotted perpendicular from the tip of grad f(P) onto the theta = 45 deg unit vector,
    # geometrically showing the projection ||grad f|| cos(45 deg) = 0.46!
    th_45 = phi_grad + math.radians(45.0)
    u45 = np.array([math.cos(th_45), math.sin(th_45)])
    proj_len_45 = df_ds_values[45] * L_vec
    foot_45 = (xP + proj_len_45 * u45[0], yP + proj_len_45 * u45[1])
    ax_c.plot([grad_tip[0], foot_45[0]], [grad_tip[1], foot_45[1]], color=RED_DARK, lw=1.25, ls=":", zorder=7)
    # Small right-angle corner marker at foot_45
    perp_u45 = np.array([grad_tip[0] - foot_45[0], grad_tip[1] - foot_45[1]])
    perp_u45 /= np.linalg.norm(perp_u45)
    ra_s = 0.042
    ra_p1 = (foot_45[0] - ra_s * u45[0], foot_45[1] - ra_s * u45[1])
    ra_p2 = (ra_p1[0] + ra_s * perp_u45[0], ra_p1[1] + ra_s * perp_u45[1])
    ra_p3 = (foot_45[0] + ra_s * perp_u45[0], foot_45[1] + ra_s * perp_u45[1])
    ax_c.plot([ra_p1[0], ra_p2[0], ra_p3[0]], [ra_p1[1], ra_p2[1], ra_p3[1]], color=RED_DARK, lw=1.0, zorder=7)
    ax_c.scatter([foot_45[0]], [foot_45[1]], s=20, color=TEAL, zorder=9)

    ax_c.scatter([xP], [yP], s=62, color=AMBER, edgecolor=TEXT, lw=1.1, zorder=10)
    ax_c.text(xP - 0.05, yP + 0.08, r"$P$", ha="right", va="bottom", fontsize=10.8, fontweight="bold", color=AMBER, zorder=10)

    ax_c.set_xlabel("$x$", color=TEXT)
    ax_c.set_ylabel("$y$", color=TEXT)
    ax_c.set_title(
        r"(c) Zoom at $P(1.2, 0.6)$: unit directions $\hat{\mathbf{t}}$ and $df/ds = \nabla f\cdot\hat{\mathbf{t}} = \Vert\nabla f\Vert\cos\theta$",
        fontweight="bold",
        color=TEXT,
        pad=8,
    )

    save_fig(fig, out_dir, "maths1_gradient_steepest_ascent.png")
    info = {
        "P": [xP, yP],
        "f_P_4dp": round(fP, 4),
        "f_P_2dp": round(fP, 2),
        "grad_f_P": [round(gxP, 4), round(gyP, 4)],
        "grad_norm_4dp": round(grad_norm, 4),
        "grad_norm_2dp": round(grad_norm, 2),
        "angles_deg": angles_deg,
        "df_ds_2dp": {str(k): (0.0 if abs(v) < 1e-12 else round(v, 2)) for k, v in df_ds_values.items()},
        "df_ds_3dp": {str(k): (0.0 if abs(v) < 1e-12 else round(v, 3)) for k, v in df_ds_values.items()},
    }
    print(
        f"[Fig 5] Hill f = exp(-(x^2/4 + y^2)), summit (0, 0) with f(0, 0) = 1 and grad f = 0, "
        f"contours {c_levels}, 7x7 quiver grid; at P = ({xP:.1f}, {yP:.1f}): "
        f"f(P) = {fP:.2f} ({fP:.4f}), grad f(P) = ({gxP:.3f}, {gyP:.3f}), "
        f"||grad f(P)|| = {grad_norm:.2f} ({grad_norm:.3f}); "
        f"5 unit directions at theta = 0, 45, 90, 135, 180 deg give df/ds: "
        + ", ".join(f"{th} deg -> {df_ds_values[th]:+.2f} ({df_ds_values[th]:+.3f})" for th in angles_deg)
    )
    return info


# ===========================================================================
# Figure 6: maths1_laplacian_average.png
# ===========================================================================
def make_fig6_laplacian_average(out_dir: Path) -> dict[str, object]:
    fig = plt.figure(figsize=(10.7, 3.65), dpi=DPI)
    gs = fig.add_gridspec(
        1,
        4,
        width_ratios=[1.0, 1.0, 1.0, 0.055],
        wspace=0.22,
    )

    R = 0.5
    n_circ = 3600
    th_c = np.linspace(0.0, 2.0 * np.pi, n_circ, endpoint=False)
    xc_r = R * np.cos(th_c)
    yc_r = R * np.sin(th_c)

    panels = [
        {
            "col": 0,
            "title": r"(a) Peak: $\psi = -(x^2 + y^2)$",
            "fn": lambda x, y: -(x**2 + y**2),
            "grad": lambda x, y: (-2.0 * x, -2.0 * y),
            "lap": -4,
            "flux_word": "inward",
        },
        {
            "col": 1,
            "title": r"(b) Valley: $\psi = x^2 + y^2$",
            "fn": lambda x, y: +(x**2 + y**2),
            "grad": lambda x, y: (+2.0 * x, +2.0 * y),
            "lap": +4,
            "flux_word": "outward",
        },
        {
            "col": 2,
            "title": r"(c) Saddle: $\psi = x^2 - y^2$",
            "fn": lambda x, y: x**2 - y**2,
            "grad": lambda x, y: (+2.0 * x, -2.0 * y),
            "lap": 0,
            "flux_word": "zero",
        },
    ]

    xg = np.linspace(-1.0, 1.0, 220)
    yg = np.linspace(-1.0, 1.0, 220)
    XX, YY = np.meshgrid(xg, yg)
    norm_div = TwoSlopeNorm(vmin=-2.0, vcenter=0.0, vmax=2.0)

    q1 = np.linspace(-0.84, 0.84, 6)
    XQ, YQ = np.meshgrid(q1, q1)

    pcm_ref = None
    panel_results: list[dict[str, object]] = []

    for spec in panels:
        c_idx = spec["col"]
        ax = fig.add_subplot(gs[0, c_idx])

        fn = spec["fn"]
        grad_fn = spec["grad"]
        lap_val = spec["lap"]

        ZZ = fn(XX, YY)
        pcm_ref = ax.pcolormesh(XX, YY, ZZ, cmap="RdBu_r", norm=norm_div, shading="gouraud", alpha=0.80, zorder=1)

        c_levs = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
        ax.contour(XX, YY, ZZ, levels=c_levs, colors="black", linewidths=0.85, linestyles="solid", alpha=0.58, zorder=2)

        GX, GY = grad_fn(XQ, YQ)
        ax.quiver(
            XQ,
            YQ,
            GX,
            GY,
            angles="xy",
            scale_units="xy",
            scale=6.8,
            color=NAVY,
            alpha=0.85,
            width=0.0085,
            headwidth=3.6,
            headlength=4.2,
            headaxislength=3.7,
            zorder=4,
        )

        # Dashed circle of radius R = 0.5 around origin
        th_plot = np.linspace(0.0, 2.0 * np.pi, 240)
        ax.plot(R * np.cos(th_plot), R * np.sin(th_plot), color=AMBER, lw=2.1, ls="--", zorder=5)
        if c_idx == 0:
            ax.annotate(
                r"$R = 0.5$",
                xy=(-R * math.cos(math.radians(45.0)), R * math.sin(math.radians(45.0))),
                xytext=(-0.64, 0.80),
                ha="center",
                va="center",
                fontsize=9.2,
                fontweight="bold",
                color=AMBER,
                bbox=dict(boxstyle="round,pad=0.10", fc="white", ec=AMBER, lw=0.75, alpha=0.94),
                arrowprops=dict(arrowstyle="->", color=AMBER, lw=1.0, shrinkB=2),
                zorder=8,
            )

        psi_centre = float(fn(0.0, 0.0))
        if abs(psi_centre) < 1e-14:
            psi_centre = 0.0
        psi_circle_vals = fn(xc_r, yc_r)
        psi_bar = float(np.mean(psi_circle_vals))
        if abs(psi_bar) < 1e-14:
            psi_bar = 0.0

        expected_diff = 0.25 * (R**2) * lap_val
        assert abs((psi_bar - psi_centre) - expected_diff) < 1e-12

        gcx, gcy = grad_fn(xc_r, yc_r)
        nx_c, ny_c = np.cos(th_c), np.sin(th_c)
        ds = (2.0 * math.pi * R) / n_circ
        flux_num = float(np.sum(gcx * nx_c + gcy * ny_c) * ds)
        if abs(flux_num) < 1e-14:
            flux_num = 0.0
        assert abs(flux_num - math.pi * (R**2) * lap_val) < 1e-10

        neighbours = [
            (+R, 0.0, (0.0, -0.15), "center", "top"),
            (-R, 0.0, (0.0, -0.15), "center", "top"),
            (0.0, +R, (0.0, +0.13), "center", "bottom"),
            (0.0, -R, (0.0, -0.15), "center", "top"),
        ]
        nb_vals: list[float] = []
        val_bbox = dict(boxstyle="round,pad=0.09", fc="white", ec=TEXT, lw=0.7, alpha=0.93)

        centre_str = "0" if psi_centre == 0.0 else f"{psi_centre:+.2f}"
        ax.scatter([0.0], [0.0], s=42, color=RED, edgecolor="white", lw=0.9, zorder=7)
        ax.text(
            0.0,
            0.12,
            centre_str,
            ha="center",
            va="bottom",
            fontsize=9.3,
            fontweight="bold",
            color=RED,
            bbox=dict(boxstyle="round,pad=0.10", fc="white", ec=RED, lw=0.8, alpha=0.95),
            zorder=8,
        )

        for nx_p, ny_p, (ox_p, oy_p), ha_p, va_p in neighbours:
            v_nb = float(fn(nx_p, ny_p))
            nb_vals.append(v_nb)
            ax.scatter([nx_p], [ny_p], s=36, color=AMBER, edgecolor=TEXT, lw=0.8, zorder=7)
            # Use a true Unicode minus sign (U+2212) rather than ASCII hyphen-minus
            v_str = f"{v_nb:+.2f}".replace("-", "\u2212")
            ax.text(
                nx_p + ox_p,
                ny_p + oy_p,
                v_str,
                ha=ha_p,
                va=va_p,
                fontsize=9.2,
                fontweight="bold",
                color=TEXT,
                bbox=val_bbox,
                zorder=8,
            )

        ax.set_xlim(-1.0, 1.0)
        ax.set_ylim(-1.0, 1.0)
        ax.set_aspect("equal")
        ax.set_xticks([-1.0, -0.5, 0.0, 0.5, 1.0])
        ax.set_yticks([-1.0, -0.5, 0.0, 0.5, 1.0])
        ax.set_xlabel("$x$", color=TEXT, labelpad=2)
        if c_idx == 0:
            ax.set_ylabel("$y$", color=TEXT, labelpad=2)
        else:
            ax.set_yticklabels([])
        ax.set_title(spec["title"], fontweight="bold", color=TEXT, pad=7, fontsize=10.0)

        bar_str = "0" if psi_bar == 0.0 else f"{psi_bar:+.2f}"
        lap_str = "0" if lap_val == 0 else f"{lap_val:+d}"
        summary_text = (
            rf"$\psi(0,0) = {centre_str}$,   $\bar{{\psi}}_R = {bar_str}$" "\n"
            rf"net $\nabla\psi$ flux: {spec['flux_word']}" "\n"
            rf"$\nabla^2\psi = {lap_str}$"
        )
        # Anchor summary box directly below the x-axis label of `ax` so there is no gap
        ax.text(
            0.50,
            -0.23,
            summary_text,
            transform=ax.transAxes,
            ha="center",
            va="top",
            fontsize=9.4,
            color=TEXT,
            clip_on=False,
            bbox=dict(boxstyle="round,pad=0.28", fc=GREY_BG, ec=NAVY, lw=0.95),
        )

        panel_results.append({
            "panel": ["a", "b", "c"][c_idx],
            "psi_centre": int(psi_centre) if psi_centre.is_integer() else psi_centre,
            "neighbours_pmR": nb_vals,
            "psi_bar_R": psi_bar,
            "flux": spec["flux_word"],
            "flux_integral": round(flux_num, 4),
            "laplacian": lap_val,
        })

    cax = fig.add_subplot(gs[0, 3])
    cbar = fig.colorbar(pcm_ref, cax=cax)
    cbar.set_label(r"Potential $\psi$", fontsize=9.8, color=TEXT)
    cbar.ax.tick_params(labelsize=9.3)

    save_fig(fig, out_dir, "maths1_laplacian_average.png")
    info = {
        "domain": [-1, 1],
        "R": R,
        "planar_factor_R2_over_4": round(0.25 * R**2, 4),
        "n_circle_points": n_circ,
        "panels": panel_results,
    }
    print(
        f"[Fig 6] Domain -1 <= x, y <= 1, circle R = {R:.1f} ({n_circ} sample points, 4 axis neighbours); "
        f"2D formula psi_bar_R - psi(0,0) = (R^2 / 4) * laplacian (denominator 4 in 2D vs 6 in 3D)."
    )
    for pr in panel_results:
        bar_p = "0" if pr["psi_bar_R"] == 0.0 else f"{pr['psi_bar_R']:+.2f}"
        lap_p = "0" if pr["laplacian"] == 0 else f"{pr['laplacian']:+d}"
        print(
            f"[Fig 6 ({pr['panel']})] R = {R:.1f}: psi(0,0) = {pr['psi_centre']}, "
            f"neighbours (+R,0),(-R,0),(0,+R),(0,-R) = {pr['neighbours_pmR']}, "
            f"circle average psi_bar_R = {bar_p} (from {n_circ} points), "
            f"net grad(psi) flux = {pr['flux']} ({pr['flux_integral']:+.4f}), "
            f"laplacian = {lap_p}."
        )
    return info


# ===========================================================================
# Entrypoint
# ===========================================================================
def main() -> None:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <output_dir>", file=sys.stderr)
        sys.exit(1)

    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Generating 6 Maths 1 Vector Calculus figures in {out_dir} ...")
    make_fig1_scalar_vector_fields(out_dir)
    make_fig2_divergence_cubes(out_dir)
    make_fig3_curl_paddle_wheels(out_dir)
    make_fig4_stokes_loops(out_dir)
    make_fig5_gradient_steepest_ascent(out_dir)
    make_fig6_laplacian_average(out_dir)
    print("All 6 Maths 1 figures generated and verified.")


if __name__ == "__main__":
    main()
