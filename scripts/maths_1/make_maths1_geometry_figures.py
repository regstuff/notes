#!/usr/bin/env python3
"""Draw the eleven geometry figures (Figures 7, 8, 10 and 18 to 25) for 'Maths 1 - Differential Geometry'.

The figures illustrate the parts of `maths_1_differential_geometry.md` after the
vector calculus section: covector tick counters, charts and transition maps,
path-dependent work, the Lie bracket loop, a closed but not exact form, Liouville's
theorem, a constant field in polar coordinates, Schwarzschild tides, converging
meridians, the light cone and Betti numbers.

Style (palette, DejaVu Sans with Computer Modern mathtext, 220 dpi, width <= 11 in,
text >= 9 pt) is copied from `scripts/maths_1/make_maths1_forms_figures.py`.
No figure numbers are drawn inside the PNGs.

Every number quoted in a label or caption is computed here and printed to stdout.

Usage:
    /home/ubuntu/.claude/skills/lecture-notes/.venv/bin/python -I \
        make_maths1_geometry_figures.py <output_dir>
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, FancyArrowPatch, Polygon, Rectangle, Arc
import numpy as np

# ---------------------------------------------------------------------------
# Palette and typography (copied from make_maths1_forms_figures.py)
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
    "svg.hashsalt": "maths1",
})

PNG_META = {"Software": None}


def save_fig(fig: plt.Figure, out_dir: Path, filename: str) -> Path:
    """Save at 220 dpi with a tight box; enforce text >= 9 pt and width <= 11 in."""
    for txt_obj in fig.findobj(matplotlib.text.Text):
        if txt_obj.get_visible() and txt_obj.get_text().strip():
            fs = float(txt_obj.get_fontsize())
            if fs < 9.0 - 1e-6:
                raise AssertionError(f"{filename}: text {txt_obj.get_text()!r} has fontsize {fs:.2f} pt < 9.0 pt")
            if "\u2014" in txt_obj.get_text():
                raise AssertionError(f"{filename}: em dash in text {txt_obj.get_text()!r}")
    out_path = out_dir / filename
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight", pad_inches=0.10, facecolor="white", metadata=PNG_META)
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
    a = FancyArrowPatch(tuple(p0), tuple(p1), arrowstyle=style, mutation_scale=ms, color=color,
                        lw=lw, zorder=z, linestyle=ls, shrinkA=shrink, shrinkB=shrink)
    ax.add_patch(a)
    return a


def clean_axes(ax):
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_visible(False)


def label_box(ax, x, y, s, color=TEXT, fc="white", ec=GREY_LINE, fs=10, ha="center", va="center", z=8):
    ax.text(x, y, s, color=color, fontsize=fs, ha=ha, va=va, zorder=z,
            bbox=dict(boxstyle="round,pad=0.25", fc=fc, ec=ec, lw=0.8))


# ---------------------------------------------------------------------------
# Figure 7: dual basis tick counters
# ---------------------------------------------------------------------------
def fig_dual_basis(out_dir: Path) -> None:
    print("Figure 7 maths1_dual_basis_ticks.png")
    e1 = np.array([1.0, 0.0])
    e2 = np.array([0.5, 1.0])
    dx1 = np.array([1.0, -0.5])  # dx^1 = dx - 0.5 dy
    dx2 = np.array([0.0, 1.0])   # dx^2 = dy
    v = 2 * e1 + e2
    vals = {
        "dx1(e1)": dx1 @ e1, "dx1(e2)": dx1 @ e2, "dx2(e1)": dx2 @ e1, "dx2(e2)": dx2 @ e2,
        "dx1(v)": dx1 @ v, "dx2(v)": dx2 @ v,
    }
    for k, val in vals.items():
        print(f"    {k} = {val:g}")
    print(f"    v = 2 e1 + e2 = ({v[0]:g}, {v[1]:g})")
    assert vals["dx1(e1)"] == 1 and vals["dx1(e2)"] == 0 and vals["dx2(e1)"] == 0 and vals["dx2(e2)"] == 1
    assert vals["dx1(v)"] == 2 and vals["dx2(v)"] == 1

    xlim, ylim = (-1.25, 3.25), (-0.62, 2.38)
    fig, axes = plt.subplots(1, 3, figsize=(10.8, 3.55))

    def stack_dx1(ax, color, alpha=1.0, labels=True, lw=1.4):
        for n in range(-2, 5):
            ys = np.array([ylim[0], ylim[1]])
            xs = n + 0.5 * ys
            ax.plot(xs, ys, color=color, lw=lw, alpha=alpha, zorder=2)
            if labels and xlim[0] < n + 0.5 * 2.18 < xlim[1] - 0.3:
                ax.text(n + 0.5 * 2.18 + 0.06, 2.18, f"${n}$", color=color, fontsize=9.5, ha="left", va="center",
                        zorder=3, bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))

    def stack_dx2(ax, color, alpha=1.0, labels=True, lw=1.4):
        for n in range(0, 3):
            ax.plot(xlim, [n, n], color=color, lw=lw, alpha=alpha, zorder=2, ls=(0, (5, 3)))
            if labels:
                ax.text(xlim[1] - 0.06, n + 0.07, f"${n}$", color=color, fontsize=9.5, ha="right", va="bottom",
                        zorder=3, bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none"))

    def basis(ax):
        arrow(ax, (0, 0), e1, color=NAVY, lw=2.4, ms=15, z=7)
        arrow(ax, (0, 0), e2, color=RED, lw=2.4, ms=15, z=7)
        ax.text(1.0, -0.16, r"$e_1$", color=NAVY, fontsize=12, ha="center", va="top", zorder=8)
        ax.text(0.20, 0.72, r"$e_2$", color=RED, fontsize=12, ha="right", va="center", zorder=8,
                bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none"))
        ax.plot([0], [0], "o", color=TEXT, ms=4, zorder=8)
        ax.text(-0.08, -0.12, r"$p$", fontsize=11, ha="right", va="top", zorder=8)

    for ax in axes:
        ax.set_xlim(*xlim)
        ax.set_ylim(*ylim)
        ax.set_aspect("equal")
        clean_axes(ax)
        ax.add_patch(Rectangle((xlim[0], ylim[0]), xlim[1] - xlim[0], ylim[1] - ylim[0], fc=GREY_BG, ec=GREY_LINE,
                               lw=1.0, zorder=0))

    # (a)
    ax = axes[0]
    stack_dx1(ax, TEAL)
    basis(ax)
    ax.set_title(r"(a) Stack of $dx^1 = dx - 0.5\,dy$", fontweight="bold", color=TEXT, pad=8)
    label_box(ax, 1.95, -0.36, r"$dx^1(e_1) = 1$", color=NAVY)
    label_box(ax, -0.35, 1.55, r"$dx^1(e_2) = 0$", color=RED)

    # (b)
    ax = axes[1]
    stack_dx2(ax, AMBER)
    basis(ax)
    ax.set_title(r"(b) Stack of $dx^2 = dy$", fontweight="bold", color=TEXT, pad=8)
    label_box(ax, 1.95, -0.36, r"$dx^2(e_1) = 0$", color=NAVY)
    label_box(ax, 1.45, 1.55, r"$dx^2(e_2) = 1$", color=RED)

    # (c)
    ax = axes[2]
    stack_dx1(ax, TEAL, alpha=0.85, labels=True, lw=1.2)
    stack_dx2(ax, AMBER, alpha=0.85, labels=False, lw=1.2)
    # decomposition: two steps along e1 (stay on dx^2 line 0, cross two dx^1 lines),
    # then one step along e2 (stays on dx^1 line 2, crosses one dx^2 line)
    arrow(ax, (0, 0), (1, 0), color=NAVY, lw=1.7, ms=11, z=6)
    arrow(ax, (1, 0), (2, 0), color=NAVY, lw=1.7, ms=11, z=6)
    arrow(ax, (2, 0), (2.5, 1), color=RED, lw=1.7, ms=11, z=6)
    arrow(ax, (0, 0), v, color=BLUE, lw=2.6, ms=16, z=7)
    ax.plot([0], [0], "o", color=TEXT, ms=4, zorder=8)
    ax.text(-0.08, -0.12, r"$p$", fontsize=11, ha="right", va="top", zorder=8)
    ax.text(0.5, -0.1, r"$e_1$", color=NAVY, fontsize=10.5, ha="center", va="top", zorder=8)
    ax.text(1.5, -0.1, r"$e_1$", color=NAVY, fontsize=10.5, ha="center", va="top", zorder=8)
    ax.text(2.38, 0.36, r"$e_2$", color=RED, fontsize=10.5, ha="left", va="center", zorder=8,
            bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none"))
    ax.text(1.0, 0.55, r"$v$", color=BLUE, fontsize=12, ha="right", va="bottom", zorder=8,
            bbox=dict(boxstyle="round,pad=0.08", fc=GREY_BG, ec="none"))
    ax.set_title(r"(c) $v = 2e_1 + e_2$ over both stacks", fontweight="bold", color=TEXT, pad=8)
    label_box(ax, -0.35, 1.55, r"$dx^1(v) = 2$", color=TEAL)
    label_box(ax, 1.75, 1.55, r"$dx^2(v) = 1$", color=AMBER)

    fig.tight_layout(w_pad=1.2)
    save_fig(fig, out_dir, "maths1_dual_basis_ticks.png")


# ---------------------------------------------------------------------------
# Figure 8: charts and transition map
# ---------------------------------------------------------------------------
def ortho(lat, lon, lat0, lon0, R=1.0):
    """Orthographic projection (degrees in); returns x, y, visibility cos(c)."""
    la, lo, la0, lo0 = map(np.radians, (lat, lon, lat0, lon0))
    x = R * np.cos(la) * np.sin(lo - lo0)
    y = R * (np.cos(la0) * np.sin(la) - np.sin(la0) * np.cos(la) * np.cos(lo - lo0))
    cosc = np.sin(la0) * np.sin(la) + np.cos(la0) * np.cos(la) * np.cos(lo - lo0)
    return x, y, cosc


def fig_charts(out_dir: Path) -> None:
    print("Figure 8 maths1_charts_transition.png")
    lat0, lon0, R = 22.0, 87.0, 1.6
    pE = (27.98, 86.92)  # Everest
    lat_a, lon_a = (12.0, 42.0), (68.0, 102.0)       # O_alpha: lat-long patch
    capc, caprad = (34.0, 101.0), 16.0               # O_beta: spherical cap
    print(f"    O_alpha: latitude {lat_a[0]:g} to {lat_a[1]:g} deg, longitude {lon_a[0]:g} to {lon_a[1]:g} deg")
    print(f"    O_beta: cap centred at ({capc[0]:g} N, {capc[1]:g} E), angular radius {caprad:g} deg")
    print(f"    p (Everest) at ({pE[0]:.2f} N, {pE[1]:.2f} E)")

    def ang_dist(lat, lon, c):
        la, lo, la1, lo1 = map(np.radians, (lat, lon, c[0], c[1]))
        return np.degrees(np.arccos(np.clip(np.sin(la) * np.sin(la1) + np.cos(la) * np.cos(la1) * np.cos(lo - lo1), -1, 1)))

    def in_a(lat, lon):
        return (lat >= lat_a[0]) & (lat <= lat_a[1]) & (lon >= lon_a[0]) & (lon <= lon_a[1])

    def in_b(lat, lon):
        return ang_dist(lat, lon, capc) <= caprad

    assert in_a(*pE) and in_b(*pE), "Everest must lie in the overlap"

    fig = plt.figure(figsize=(10.4, 4.6))
    axA = fig.add_axes([0.0, 0.0, 0.70, 1.0])
    axB = fig.add_axes([0.72, 0.0, 0.28, 1.0])
    for ax in (axA, axB):
        ax.set_aspect("equal")
        ax.set_anchor("N")
        clean_axes(ax)

    # ---- panel (a): globe at left, two squares at right
    ax = axA
    ax.set_xlim(-1.9, 6.35)
    ax.set_ylim(-2.05, 2.25)
    ax.add_patch(Circle((0, 0), R, fc=BLUE_PALE, ec=NAVY, lw=1.4, zorder=1))
    for la in range(-60, 90, 30):
        lo = np.linspace(-180, 180, 721)
        x, y, c = ortho(la, lo, lat0, lon0, R)
        x = np.where(c > 0, x, np.nan)
        ax.plot(x, y, color=GREY_LINE, lw=0.8, zorder=2)
    for lo in range(-180, 180, 30):
        la = np.linspace(-90, 90, 361)
        x, y, c = ortho(la, lo + lon0 % 30, lat0, lon0, R)
        x = np.where(c > 0, x, np.nan)
        ax.plot(x, y, color=GREY_LINE, lw=0.8, zorder=2)
    # region fills via indicator on a lat-lon grid
    LA, LO = np.meshgrid(np.linspace(0, 60, 601), np.linspace(55, 125, 701), indexing="ij")
    X, Y, C = ortho(LA, LO, lat0, lon0, R)
    IA = in_a(LA, LO).astype(float)
    IB = in_b(LA, LO).astype(float)
    ax.contourf(X, Y, IA, levels=[0.5, 1.5], colors=[TEAL_LIGHT], alpha=0.9, zorder=3)
    ax.contourf(X, Y, IB, levels=[0.5, 1.5], colors=[AMBER_LIGHT], alpha=0.9, zorder=3)
    ax.contourf(X, Y, IA * IB, levels=[0.5, 1.5], colors=[RED_MID], alpha=0.95, zorder=4)
    ax.contour(X, Y, IA, levels=[0.5], colors=[TEAL], linewidths=1.6, zorder=5)
    ax.contour(X, Y, IB, levels=[0.5], colors=[AMBER], linewidths=1.6, zorder=5)
    # lat-long graticule inside O_alpha (every 10 deg)
    for la in np.arange(lat_a[0], lat_a[1] + 0.1, 10):
        x, y, _ = ortho(la, np.linspace(*lon_a, 50), lat0, lon0, R)
        ax.plot(x, y, color=TEAL, lw=0.6, alpha=0.7, zorder=5)
    for lo in np.arange(lon_a[0], lon_a[1] + 0.1, 10):
        x, y, _ = ortho(np.linspace(*lat_a, 50), lo, lat0, lon0, R)
        ax.plot(x, y, color=TEAL, lw=0.6, alpha=0.7, zorder=5)
    xp, yp, _ = ortho(*pE, lat0, lon0, R)
    ax.plot([xp], [yp], "o", color=TEXT, ms=4.5, zorder=9)
    ax.text(xp - 0.07, yp - 0.05, r"$p$", fontsize=11, ha="right", va="top", zorder=9)
    xa, ya, _ = ortho(lat_a[0] + 3, lon_a[0] + 2, lat0, lon0, R)
    ax.text(xa - 0.06, ya - 0.08, r"$O_\alpha$", color=TEAL, fontsize=12, ha="right", va="top", zorder=9)
    xb, yb, _ = ortho(capc[0] + caprad - 2, capc[1] + 3, lat0, lon0, R)
    ax.text(xb + 0.05, yb + 0.05, r"$O_\beta$", color=AMBER, fontsize=12, ha="left", va="bottom", zorder=9)
    ax.text(0, -R - 0.15, "the sphere $M$ (Earth)", fontsize=10, ha="center", va="top", color=SLATE)
    ax.text(-1.05, 1.02, r"$O_\alpha\cap O_\beta$", color=RED, fontsize=10.5, ha="center", va="center", zorder=9,
            bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))
    ax.add_patch(Circle((0, 0), R, fc="none", ec=NAVY, lw=1.4, zorder=6))
    assert in_a(39.0, 89.0) and in_b(39.0, 89.0)
    xo, yo, _ = ortho(39.0, 89.0, lat0, lon0, R)
    arrow(ax, (-0.8, 0.9), (xo, yo), color=RED, lw=1.0, ms=9, z=9)

    # square alpha (lambda across, theta up), square beta (x across, y up)
    Sa = (2.75, 0.35, 1.55)   # (x0, y0, side)
    Sb = (2.75, -1.85, 1.55)

    def to_sq_a(lat, lon):
        u = (lon - lon_a[0]) / (lon_a[1] - lon_a[0])
        w = (lat - lat_a[0]) / (lat_a[1] - lat_a[0])
        return Sa[0] + Sa[2] * u, Sa[1] + Sa[2] * w

    # tangent-plane (orthographic about cap centre) chart for O_beta, scaled to the square
    def chart_b(lat, lon):
        x, y, _ = ortho(lat, lon, capc[0], capc[1], 1.0)
        return x, y

    rb = math.sin(math.radians(caprad))
    scale_b = Sb[2] / (2.0 * rb * 1.18)
    cxb, cyb = Sb[0] + Sb[2] / 2, Sb[1] + Sb[2] / 2

    def to_sq_b(lat, lon):
        x, y = chart_b(lat, lon)
        return cxb + scale_b * x, cyb + scale_b * y

    for (x0, y0, s), col in ((Sa, TEAL), (Sb, AMBER)):
        ax.add_patch(Rectangle((x0, y0), s, s, fc="white", ec=col, lw=1.4, zorder=2))
        for k in range(1, 4):
            ax.plot([x0 + k * s / 4] * 2, [y0, y0 + s], color=GREY_LINE, lw=0.7, zorder=2)
            ax.plot([x0, x0 + s], [y0 + k * s / 4] * 2, color=GREY_LINE, lw=0.7, zorder=2)
    # image of overlap in square alpha
    U, W = to_sq_a(LA, LO)
    ax.contourf(U, W, IA * IB, levels=[0.5, 1.5], colors=[RED_MID], zorder=3)
    ax.contour(U, W, IB * IA, levels=[0.5], colors=[RED], linewidths=1.0, zorder=4)
    # image of O_beta and overlap in square beta
    Ub, Wb = to_sq_b(LA, LO)
    vis_b = ortho(LA, LO, capc[0], capc[1], 1.0)[2] > 0
    IBm = np.where(vis_b, IB, 0.0)
    ax.contourf(Ub, Wb, IBm, levels=[0.5, 1.5], colors=[AMBER_LIGHT], zorder=3)
    ax.contourf(Ub, Wb, IA * IBm, levels=[0.5, 1.5], colors=[RED_MID], zorder=3)
    ax.contour(Ub, Wb, IBm, levels=[0.5], colors=[AMBER], linewidths=1.2, zorder=4)
    ax.contour(Ub, Wb, IA * IBm, levels=[0.5], colors=[RED], linewidths=1.0, zorder=4)
    pa = to_sq_a(*pE)
    pb = to_sq_b(*pE)
    for q in (pa, pb):
        ax.plot([q[0]], [q[1]], "o", color=TEXT, ms=4, zorder=9)
    # axis labels
    ax.text(Sa[0] + Sa[2] / 2, Sa[1] - 0.06, r"$\lambda$ (longitude)", fontsize=10, ha="center", va="top")
    ax.text(Sa[0] - 0.07, Sa[1] + Sa[2] / 2, r"$\theta$ (latitude)", fontsize=10, ha="right", va="center", rotation=90)
    ax.text(Sb[0] + Sb[2] / 2, Sb[1] - 0.06, r"$x$ (Easting)", fontsize=10, ha="center", va="top")
    ax.text(Sb[0] - 0.07, Sb[1] + Sb[2] / 2, r"$y$ (Northing)", fontsize=10, ha="right", va="center", rotation=90)
    ax.text(Sa[0] + Sa[2] + 0.08, Sa[1] + 0.02, r"$\mathbb{R}^2$", fontsize=11, ha="left", va="bottom", color=TEAL)
    ax.text(Sb[0] + Sb[2] + 0.08, Sb[1] + 0.02, r"$\mathbb{R}^2$", fontsize=11, ha="left", va="bottom", color=AMBER)
    ax.text(Sa[0] + Sa[2] / 2, Sa[1] + Sa[2] + 0.07, r"chart $\phi_\alpha$: $(\theta, \lambda)$", fontsize=10,
            ha="center", va="bottom", color=TEAL)
    ax.text(Sb[0] + Sb[2] / 2, Sb[1] + Sb[2] + 0.07, r"chart $\phi_\beta$: $(x, y)$", fontsize=10,
            ha="center", va="bottom", color=AMBER)
    # arrows phi_alpha, phi_beta from globe to squares
    a1 = FancyArrowPatch((1.25, 0.95), (Sa[0] - 0.55, Sa[1] + 0.95), connectionstyle="arc3,rad=-0.15",
                         arrowstyle="-|>", mutation_scale=14, color=TEAL, lw=1.8, zorder=6)
    ax.add_patch(a1)
    ax.text(2.05, 1.42, r"$\phi_\alpha$", color=TEAL, fontsize=13, ha="center", va="bottom")
    a2 = FancyArrowPatch((1.25, -0.95), (Sb[0] - 0.55, Sb[1] + 0.55), connectionstyle="arc3,rad=0.15",
                         arrowstyle="-|>", mutation_scale=14, color=AMBER, lw=1.8, zorder=6)
    ax.add_patch(a2)
    ax.text(2.05, -1.42, r"$\phi_\beta$", color=AMBER, fontsize=13, ha="center", va="top")
    # transition arrow between squares (right side)
    a3 = FancyArrowPatch((Sa[0] + Sa[2] + 0.12, Sa[1] + 0.45), (Sb[0] + Sb[2] + 0.12, Sb[1] + Sb[2] - 0.2),
                         connectionstyle="arc3,rad=-0.55", arrowstyle="-|>", mutation_scale=15, color=RED, lw=2.0,
                         zorder=6)
    ax.add_patch(a3)
    ax.text(Sa[0] + Sa[2] + 0.55, -0.06, r"$\phi_\beta\circ\phi_\alpha^{-1}$", color=RED, fontsize=12.5,
            ha="left", va="center")
    ax.text(Sa[0] + Sa[2] + 0.55, -0.42, "transition map", color=RED, fontsize=9.5, ha="left", va="center")
    ax.set_title("(a) Two overlapping charts and their transition map", fontweight="bold", color=TEXT, pad=4)

    # ---- panel (b): polar cap from above
    ax = axB
    capR = 1.25
    ax.set_xlim(-1.45, 1.45)
    ax.set_ylim(-2.05, 2.25)
    ax.add_patch(Circle((0, 0), capR, fc=BLUE_PALE, ec=NAVY, lw=1.4, zorder=1))
    for k in range(12):
        t = math.radians(30 * k)
        ax.plot([0, capR * math.cos(t)], [0, capR * math.sin(t)], color=SLATE, lw=0.9, zorder=2)
    for rr in (capR / 3, 2 * capR / 3):
        ax.add_patch(Circle((0, 0), rr, fc="none", ec=GREY_LINE, lw=0.8, zorder=2))
    # Cartesian square grid over the cap
    s = 0.85
    for g in np.linspace(-s, s, 7):
        ax.plot([g, g], [-s, s], color=TEAL, lw=1.0, alpha=0.9, zorder=3)
        ax.plot([-s, s], [g, g], color=TEAL, lw=1.0, alpha=0.9, zorder=3)
    ax.plot([0], [0], "o", color=RED, ms=5, zorder=6)
    label_box(ax, 0.0, capR + 0.38, "longitude lines meet at the pole:\nlongitude undefined there", color=SLATE,
              fs=9.5)
    label_box(ax, 0.0, -capR - 0.42, "Cartesian $(x, y)$ chart:\npole at $(0, 0)$, smooth", color=TEAL, fs=9.5)
    ax.text(0.07, -0.06, "N", color=RED, fontsize=10, ha="left", va="top", zorder=7, fontweight="bold")
    ax.set_title("(b) Polar cap seen from above", fontweight="bold", color=TEXT, pad=4)

    save_fig(fig, out_dir, "maths1_charts_transition.png")


# ---------------------------------------------------------------------------
# Figure 10: PV work paths
# ---------------------------------------------------------------------------
def fig_pv(out_dir: Path) -> None:
    print("Figure 10 maths1_pv_work_paths.png")
    A, B = (1.0, 2.0), (3.0, 1.0)
    W1 = 2.0 * (3.0 - 1.0)   # expand at P = 2
    W2 = 1.0 * (3.0 - 1.0)   # expand at P = 1
    loop = 2.0 * 2.0 - 1.0 * 2.0
    print(f"    path 1 (expand at P=2, then drop): int P dV = {W1:g}")
    print(f"    path 2 (drop, then expand at P=1): int P dV = {W2:g}")
    print(f"    clockwise rectangle cycle: oint P dV = {loop:g} = enclosed area {(3 - 1) * (2 - 1):g}")
    assert loop == (3 - 1) * (2 - 1)

    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.0))
    for ax in axes:
        ax.set_xlim(0, 3.9)
        ax.set_ylim(0, 2.75)
        ax.set_xlabel(r"$V$")
        ax.set_ylabel(r"$P$", rotation=0, labelpad=10)
        ax.set_xticks([1, 2, 3])
        ax.set_yticks([1, 2])
        for s in ("top", "right"):
            ax.spines[s].set_visible(False)
        ax.spines["left"].set_color(SLATE)
        ax.spines["bottom"].set_color(SLATE)

    ax = axes[0]
    ax.fill_between([1, 3], 0, 2, color=TEAL_LIGHT, alpha=0.75, zorder=1, lw=0)
    ax.fill_between([1, 3], 0, 1, color=AMBER_LIGHT, alpha=0.95, zorder=2, lw=0)
    ax.plot([1, 3], [2, 2], color=TEAL, lw=2.4, zorder=4)
    ax.plot([3, 3], [2, 1], color=TEAL, lw=2.4, zorder=4)
    ax.plot([1, 1], [2, 1], color=AMBER, lw=2.4, zorder=4, ls=(0, (6, 3)))
    ax.plot([1, 3], [1, 1], color=AMBER, lw=2.4, zorder=4, ls=(0, (6, 3)))
    arrow(ax, (1.9, 2), (2.1, 2), color=TEAL, lw=0, ms=16)
    arrow(ax, (3, 1.6), (3, 1.4), color=TEAL, lw=0, ms=16)
    arrow(ax, (1, 1.6), (1, 1.4), color=AMBER, lw=0, ms=16)
    arrow(ax, (1.9, 1), (2.1, 1), color=AMBER, lw=0, ms=16)
    for pt, nm, dx, ha in ((A, "A", -0.08, "right"), (B, "B", 0.08, "left")):
        ax.plot(*pt, "o", color=TEXT, ms=6, zorder=6)
        ax.text(pt[0] + dx, pt[1] + 0.05, nm, fontsize=12, ha=ha, va="bottom", fontweight="bold")
    ax.text(2.0, 2.1, "path 1: \u222b $P\\;dV = 4$", color=TEAL, fontsize=10.5, ha="center", va="bottom")
    ax.text(2.0, 0.5, "path 2: \u222b $P\\;dV = 2$", color=AMBER, fontsize=10.5, ha="center", va="center",
            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.85))
    ax.text(2.0, 1.5, "extra area under path 1", color=TEAL, fontsize=9.5, ha="center", va="center")
    ax.set_title("(a) Same end points, different work", fontweight="bold", color=TEXT, pad=8)

    ax = axes[1]
    ax.add_patch(Rectangle((1, 1), 2, 1, fc=BLUE_LIGHT, ec="none", zorder=1))
    xs = [1, 3, 3, 1, 1]
    ys = [2, 2, 1, 1, 2]
    ax.plot(xs, ys, color=NAVY, lw=2.4, zorder=4)
    for (x0, y0), (x1, y1) in (((1.9, 2), (2.1, 2)), ((3, 1.6), (3, 1.4)), ((2.1, 1), (1.9, 1)), ((1, 1.4), (1, 1.6))):
        arrow(ax, (x0, y0), (x1, y1), color=NAVY, lw=0, ms=16)
    ax.plot(*A, "o", color=TEXT, ms=6, zorder=6)
    ax.text(A[0] - 0.08, A[1] + 0.05, "A", fontsize=12, ha="right", va="bottom", fontweight="bold")
    ax.text(2.0, 1.5, "\u222e $P\\;dV = 2$" + "\n= enclosed area", color=NAVY, fontsize=10.5, ha="center",
            va="center")
    ax.text(2.0, 2.12, "clockwise", color=NAVY, fontsize=10, ha="center", va="bottom")
    label_box(ax, 2.0, 0.45, r"clockwise is the positive orientation of $dP\wedge dV$" + "\n" +
              r"when $V$ is across and $P$ is up", color=SLATE, fs=9.5)
    ax.set_title("(b) A heat-engine cycle", fontweight="bold", color=TEXT, pad=8)

    fig.tight_layout(w_pad=2.5)
    save_fig(fig, out_dir, "maths1_pv_work_paths.png")


# ---------------------------------------------------------------------------
# Figure 18: Lie bracket gap
# ---------------------------------------------------------------------------
def fig_lie_bracket(out_dir: Path) -> None:
    print("Figure 18 maths1_lie_bracket_gap.png")
    eps = 0.4
    p0 = np.array([0.0, 0.0])
    p1 = p0 + np.array([eps, 0])
    p2 = p1 + np.array([0, p1[0] * eps])
    p3 = p2 + np.array([-eps, 0])
    p4 = p3 + np.array([0, -p3[0] * eps])
    for nm, q in (("after X", p1), ("after Y", p2), ("after -X", p3), ("after -Y", p4)):
        print(f"    {nm}: ({q[0]:.2f}, {q[1]:.2f})")
    print(f"    gap = ({p4[0]:.2f}, {p4[1]:.2f}) = eps^2 [X,Y] with eps^2 = {eps ** 2:.2f}")
    assert abs(p4[1] - eps ** 2) < 1e-12 and abs(p4[0]) < 1e-12

    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6), gridspec_kw={"width_ratios": [1.0, 1.0]})
    ax = axes[0]
    g = np.linspace(-1.0, 1.0, 6)
    GX, GY = np.meshgrid(g, g)
    ax.quiver(GX, GY, np.full_like(GX, 0.22), np.zeros_like(GX), color=TEAL, angles="xy", scale_units="xy",
              scale=1, width=0.006, zorder=2, alpha=0.9)
    ax.quiver(GX + 0.08, GY, np.zeros_like(GX), 0.22 * GX, color=AMBER, angles="xy", scale_units="xy", scale=1,
              width=0.006, zorder=2, alpha=0.9)
    loop = np.array([p0, p1, p2, p3])
    ax.plot(loop[:, 0], loop[:, 1], color=NAVY, lw=2.0, zorder=5)
    arrow(ax, p0, p4, color=RED, lw=2.0, ms=11, z=7)
    ax.add_patch(Rectangle((-0.12, -0.10), 0.64, 0.34, fc="none", ec=SLATE, lw=1.0, ls=(0, (3, 2)), zorder=6))
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.25, 1.55)
    ax.set_aspect("equal")
    ax.axhline(0, color=GREY_LINE, lw=0.8, zorder=0)
    ax.axvline(0, color=GREY_LINE, lw=0.8, zorder=0)
    ax.set_xticks([-1, 0, 1])
    ax.set_yticks([-1, 0, 1])
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$", rotation=0)
    label_box(ax, -0.62, 1.40, r"$X = \partial_x$ (teal)", color=TEAL)
    label_box(ax, 0.62, 1.40, r"$Y = x\,\partial_y$ (amber)", color=AMBER)
    ax.set_title(r"(a) The fields and the loop ($\epsilon = 0.4$)", fontweight="bold", color=TEXT, pad=8)

    ax = axes[1]
    ax.set_xlim(-0.14, 0.56)
    ax.set_ylim(-0.10, 0.24)
    ax.set_aspect("equal")
    ax.axhline(0, color=GREY_LINE, lw=0.8, zorder=0)
    ax.axvline(0, color=GREY_LINE, lw=0.8, zorder=0)
    steps = [(p0, p1, r"1: along $X$", (0.2, -0.018), "top"),
             (p1, p2, r"2: along $Y$", (0.418, 0.08), "center"),
             (p2, p3, r"3: along $-X$", (0.2, 0.145), "top")]
    for a_, b_, lab, pos, va in steps:
        arrow(ax, a_, b_, color=NAVY, lw=2.2, ms=14, z=5)
        ax.text(pos[0], pos[1], lab, color=NAVY, fontsize=10, ha="left" if va == "center" else "center", va=va)
    arrow(ax, p0, p4, color=RED, lw=2.4, ms=14, z=7)
    ax.text(-0.012, 0.08, r"gap $= \epsilon^2[X, Y] = \epsilon^2\,\partial_y$", color=RED, fontsize=10.5,
            ha="right", va="center", rotation=90)
    ax.text(0.012, 0.205, r"4: along $-Y$ does nothing ($Y = 0$ when $x = 0$)", color=NAVY, fontsize=9.5,
            ha="left", va="bottom")
    for q, lab, off, ha, va in ((p0, r"$(0, 0)$", (0.01, -0.012), "left", "top"),
                                (p1, r"$(0.4, 0)$", (0.0, -0.035), "center", "top"),
                                (p2, r"$(0.4, 0.16)$", (0.012, 0.0), "left", "bottom"),
                                (p3, r"$(0, 0.16)$", (0.012, 0.005), "left", "bottom")):
        ax.plot(*q, "o", color=TEXT, ms=4.5, zorder=8)
        ax.text(q[0] + off[0], q[1] + off[1], lab, fontsize=9.5, ha=ha, va=va, color=TEXT)
    ax.set_xticks([0, 0.2, 0.4])
    ax.set_yticks([0, 0.08, 0.16])
    ax.set_xlabel(r"$x$")
    ax.set_ylabel(r"$y$", rotation=0, labelpad=14)
    ax.set_title("(b) Zoom on the loop", fontweight="bold", color=TEXT, pad=8)
    fig.tight_layout(w_pad=2.0)
    save_fig(fig, out_dir, "maths1_lie_bracket_gap.png")


# ---------------------------------------------------------------------------
# Figure 19: closed but not exact
# ---------------------------------------------------------------------------
def fig_closed_not_exact(out_dir: Path) -> None:
    print("Figure 19 maths1_closed_not_exact.png")
    t = np.linspace(0, 2 * np.pi, 200001)
    x, y = np.cos(t), np.sin(t)
    dxdt, dydt = -np.sin(t), np.cos(t)
    integrand = (-y * dxdt + x * dydt) / (x ** 2 + y ** 2)
    loop = np.trapezoid(integrand, t) if hasattr(np, "trapezoid") else np.trapz(integrand, t)
    print(f"    oint dtheta round the unit circle = {loop:.6f} (2 pi = {2 * np.pi:.6f})")
    # flux of r_hat / r^2 through a sphere of radius a: (1/a^2) * 4 pi a^2
    for a in (0.5, 1.0, 2.0):
        print(f"    flux of r_hat/r^2 through sphere of radius {a:g} = {(1 / a ** 2) * 4 * np.pi * a ** 2:.6f}")
    print(f"    4 pi = {4 * np.pi:.6f}")
    labels = [r"$0$", r"$\frac{\pi}{6}$", r"$\frac{\pi}{3}$", r"$\frac{\pi}{2}$", r"$\frac{2\pi}{3}$",
              r"$\frac{5\pi}{6}$", r"$\pi$", r"$\frac{7\pi}{6}$", r"$\frac{4\pi}{3}$", r"$\frac{3\pi}{2}$",
              r"$\frac{5\pi}{3}$", r"$\frac{11\pi}{6}$"]

    fig, axes = plt.subplots(1, 2, figsize=(10.2, 5.0))
    for ax in axes:
        ax.set_anchor("N")
    ax = axes[0]
    Rr = 1.55
    for k in range(12):
        th = math.radians(30 * k)
        col = RED if k == 0 else TEAL
        if k == 0:
            ax.plot([0.06, Rr], [0, 0], color=RED, lw=2.2, ls=(0, (5, 3)), zorder=3)
        else:
            ax.plot([0.06 * math.cos(th), Rr * math.cos(th)], [0.06 * math.sin(th), Rr * math.sin(th)], color=col,
                    lw=1.3, zorder=2)
        if k != 0:
            ax.text(1.75 * math.cos(th), 1.75 * math.sin(th), labels[k], color=TEAL, fontsize=12, ha="center",
                    va="center")
    ax.text(1.78, 0.13, r"$0$", color=RED, fontsize=12, ha="center", va="bottom")
    ax.text(1.78, -0.13, r"$2\pi$", color=RED, fontsize=12, ha="center", va="top")
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color=NAVY, lw=1.8, zorder=4)
    a = FancyArrowPatch((math.cos(math.radians(105)), math.sin(math.radians(105))),
                        (math.cos(math.radians(125)), math.sin(math.radians(125))),
                        connectionstyle="arc3,rad=0.12", arrowstyle="-|>", mutation_scale=16, color=NAVY, lw=1.8,
                        zorder=5)
    ax.add_patch(a)
    ax.add_patch(Circle((0, 0), 0.06, fc="white", ec=TEXT, lw=1.4, zorder=6))
    label_box(ax, -1.45, -1.25, "\u222e $d\\theta = 2\\pi \\neq 0$", color=NAVY, fs=11)
    label_box(ax, 1.85, 1.62, "cut: the label jumps\nfrom $2\\pi$ back to $0$", color=RED, fs=9.5)
    arrow(ax, (1.8, 1.4), (1.42, 0.07), color=RED, lw=1.0, ms=9)
    ax.set_xlim(-2.05, 2.5)
    ax.set_ylim(-2.1, 2.05)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.set_title(r"(a) $d\theta$ on the punctured plane", fontweight="bold", color=TEXT, pad=8)

    ax = axes[1]
    ax.add_patch(Circle((0, 0), 1.2, fc=BLUE_PALE, ec=NAVY, lw=1.6, zorder=1))
    ax.add_patch(Ellipse((0, 0), 2.4, 0.55, fc="none", ec=NAVY, lw=0.9, ls=(0, (4, 3)), zorder=2))
    kscale = 0.1
    for k in range(12):
        # inner ring of long arrows and an interleaved outer ring of short ones, so both are visible
        for r0, off in ((0.42, 15), (0.85, 0)):
            thk = math.radians(30 * k + off)
            L = kscale / r0 ** 2
            p0 = (r0 * math.cos(thk), r0 * math.sin(thk))
            p1 = ((r0 + L) * math.cos(thk), (r0 + L) * math.sin(thk))
            arrow(ax, p0, p1, color=AMBER, lw=1.4, ms=9, z=4)
    ax.add_patch(Circle((0, 0), 0.06, fc="white", ec=TEXT, lw=1.4, zorder=6))
    label_box(ax, 0.0, -1.78, r"flux through the sphere $= 4\pi \neq 0$", color=NAVY, fs=10.5)
    ax.text(1.0, -1.25, r"arrow length $\propto 1/r^2$", fontsize=9.5, color=AMBER, ha="left", va="center")
    label_box(ax, 0.0, 1.78, r"$\nabla\cdot\frac{\hat{\mathbf{r}}}{r^2} = 0$ away from $0$: closed" + "\n" +
              "but not exact", color=AMBER, fs=10)
    ax.set_xlim(-2.05, 2.05)
    ax.set_ylim(-2.05, 2.05)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.set_title(r"(b) Point-charge flux in $\mathbb{R}^3$ minus the origin", fontweight="bold", color=TEXT, pad=8)
    fig.tight_layout(w_pad=2.0)
    save_fig(fig, out_dir, "maths1_closed_not_exact.png")


# ---------------------------------------------------------------------------
# Figure 20: Liouville
# ---------------------------------------------------------------------------
def rk4_flow(f, z, t_end, dt):
    n = int(round(t_end / dt))
    for _ in range(n):
        k1 = f(z)
        k2 = f(z + 0.5 * dt * k1)
        k3 = f(z + 0.5 * dt * k2)
        k4 = f(z + dt * k3)
        z = z + dt / 6.0 * (k1 + 2 * k2 + 2 * k3 + k4)
    return z


def shoelace(z):
    x, y = z[0], z[1]
    return 0.5 * abs(np.dot(x, np.roll(y, -1)) - np.dot(y, np.roll(x, -1)))


def fig_liouville(out_dir: Path) -> None:
    print("Figure 20 maths1_liouville_blob.png")
    npts, r0, c0, gamma, dt = 2000, 0.25, (0.8, 0.0), 0.3, 0.002
    ang = np.linspace(0, 2 * np.pi, npts, endpoint=False)
    z0 = np.array([c0[0] + r0 * np.cos(ang), c0[1] + r0 * np.sin(ang)])
    A0 = math.pi * r0 ** 2
    print(f"    initial disc: centre ({c0[0]:g}, {c0[1]:g}), radius {r0:g}, area pi r^2 = {A0:.4f}")

    def pend(z):
        return np.array([z[1], -np.sin(z[0])])

    def damped(z):
        return np.array([z[1], -z[0] - gamma * z[1]])

    times = [0, 2, 4, 6]
    cols = [NAVY, BLUE, TEAL, AMBER]
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.4))
    results = {}
    for ax, f, name in ((axes[0], pend, "pendulum"), (axes[1], damped, "damped")):
        z = z0.copy()
        tprev = 0
        for t_, col in zip(times, cols):
            z = rk4_flow(f, z, t_ - tprev, dt) if t_ > tprev else z
            tprev = t_
            area = shoelace(z)
            results[(name, t_)] = area
            zz = np.concatenate([z, z[:, :1]], axis=1)
            ax.fill(zz[0], zz[1], color=col, alpha=0.25, zorder=3, lw=0)
            ax.plot(zz[0], zz[1], color=col, lw=1.5, zorder=4)
            cx, cy = z[0].mean(), z[1].mean()
            if name == "pendulum":
                print(f"    pendulum t = {t_}: area = {area:.4f}")
            else:
                print(f"    damped t = {t_}: area = {area:.4f}, A0 exp(-gamma t) = {A0 * math.exp(-gamma * t_):.4f}")
    for t_ in times:
        assert abs(results[("pendulum", t_)] - A0) < 5e-4, results[("pendulum", t_)]
        assert abs(results[("damped", t_)] - A0 * math.exp(-gamma * t_)) < 5e-4

    # background level curves
    q = np.linspace(-2.2, 2.2, 400)
    p = np.linspace(-1.6, 1.6, 300)
    Q, P = np.meshgrid(q, p)
    axes[0].contour(Q, P, P ** 2 / 2 - np.cos(Q), levels=np.linspace(-0.95, 0.6, 7), colors=GREY_LINE,
                    linewidths=0.8, zorder=1, linestyles="solid")
    axes[1].contour(Q, P, P ** 2 / 2 + Q ** 2 / 2, levels=[0.1, 0.3, 0.5, 0.8, 1.1], colors=GREY_LINE,
                    linewidths=0.8, zorder=1)
    for ax in axes:
        ax.set_xlim(-1.55, 1.55)
        ax.set_ylim(-1.25, 1.25)
        ax.set_aspect("equal")
        ax.set_xlabel(r"$q$")
        ax.set_ylabel(r"$p$", rotation=0)
        ax.axhline(0, color=GREY_LINE, lw=0.7, zorder=0)
        ax.axvline(0, color=GREY_LINE, lw=0.7, zorder=0)
    # legends as text boxes
    for ax, name in ((axes[0], "pendulum"), (axes[1], "damped")):
        ax.add_patch(Rectangle((0.38, -1.2), 1.12, 0.78, fc="white", ec=GREY_LINE, lw=0.8, zorder=7))
        for i, (t_, col) in enumerate(zip(times, cols)):
            yy = -0.52 - 0.18 * i
            ax.add_patch(Rectangle((0.44, yy - 0.05), 0.12, 0.1, fc=col, alpha=0.35, ec=col, lw=1.2, zorder=8))
            ax.text(0.61, yy, f"$t = {t_}$: area {results[(name, t_)]:.3f}", fontsize=9.5, ha="left",
                    va="center", color=TEXT, zorder=8)
    axes[0].set_title(r"(a) Pendulum $H = \frac{p^2}{2} - \cos q$: area kept", fontweight="bold", color=TEXT, pad=8)
    axes[1].set_title(r"(b) Damped, $\gamma = 0.3$: area $\times\, e^{-\gamma t}$", fontweight="bold", color=TEXT,
                      pad=8)
    fig.tight_layout(w_pad=2.0)
    save_fig(fig, out_dir, "maths1_liouville_blob.png")


# ---------------------------------------------------------------------------
# Figure 23: constant field in polar coordinates
# ---------------------------------------------------------------------------
def fig_polar(out_dir: Path) -> None:
    print("Figure 23 maths1_polar_constant_field.png")
    pts = [(1.5, d) for d in (0, 60, 120, 180, 240, 300)] + [(0.75, 90), (0.75, 270)]
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.9), gridspec_kw={"width_ratios": [1.35, 1.0]})
    ax = axes[0]
    for rr in (0.5, 1.0, 1.5, 2.0):
        ax.add_patch(Circle((0, 0), rr, fc="none", ec=GREY_LINE, lw=0.9, zorder=1))
    for k in range(12):
        th = math.radians(30 * k)
        ax.plot([0, 2.0 * math.cos(th)], [0, 2.0 * math.sin(th)], color=GREY_LINE, lw=0.9, zorder=1)
    L = 0.42
    for r, d in pts:
        th = math.radians(d)
        x0, y0 = r * math.cos(th), r * math.sin(th)
        arrow(ax, (x0, y0), (x0 + L, y0), color=BLUE, lw=2.2, ms=13, z=5)
        ax.plot([x0], [y0], "o", color=TEXT, ms=3.5, zorder=6)
        Yr, Yt = math.cos(th), -math.sin(th) / r
        Yr = 0.0 if abs(Yr) < 5e-3 else Yr
        Yt = 0.0 if abs(Yt) < 5e-3 else Yt
        print(f"    r = {r:g}, theta = {d:3d} deg: (Y^r, Y^theta) = ({Yr:.2f}, {Yt:.2f})")
        if r == 1.5:
            off = {0: (0.06, -0.16, "left", "top"), 60: (0.06, 0.12, "left", "bottom"),
                   120: (-0.05, 0.12, "center", "bottom"), 180: (-0.06, 0.13, "right", "bottom"),
                   240: (-0.05, -0.12, "center", "top"), 300: (0.06, -0.14, "left", "top")}[d]
            ax.text(x0 + off[0], y0 + off[1], f"$({Yr:.2f},\\ {Yt:.2f})$", fontsize=9.5, ha=off[2], va=off[3],
                    color=NAVY, zorder=7, bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))
        else:
            ax.text(x0 - 0.07, y0 + (0.1 if d == 90 else -0.1), f"$({Yr:.2f},\\ {Yt:.2f})$", fontsize=9.5,
                    ha="right", va="bottom" if d == 90 else "top", color=NAVY, zorder=7,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))
    ax.set_xlim(-2.45, 2.45)
    ax.set_ylim(-2.15, 2.15)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.text(-2.4, 2.1, r"$\partial_x$ (same arrow everywhere)" + "\n" +
            r"labels: polar components $(Y^r,\ Y^\theta)$", fontsize=9.5, ha="left", va="top", color=NAVY,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=GREY_LINE, lw=0.8))
    ax.set_title(r"(a) The constant field $\partial_x$ on a polar grid", fontweight="bold", color=TEXT, pad=8)

    ax = axes[1]
    r, d = 1.5, 45
    th = math.radians(d)
    for rr in (1.0, 1.5, 2.0):
        ax.add_patch(Arc((0, 0), 2 * rr, 2 * rr, theta1=10, theta2=80, color=GREY_LINE, lw=0.9, zorder=1))
    for dd in (15, 30, 45, 60, 75):
        t2 = math.radians(dd)
        ax.plot([0.8 * math.cos(t2), 2.2 * math.cos(t2)], [0.8 * math.sin(t2), 2.2 * math.sin(t2)], color=GREY_LINE,
                lw=0.9, zorder=1)
    x0, y0 = r * math.cos(th), r * math.sin(th)
    s = 0.5  # drawing scale
    er = np.array([math.cos(th), math.sin(th)])
    et = np.array([-math.sin(th), math.cos(th)])
    arrow(ax, (x0, y0), (x0 + s * er[0], y0 + s * er[1]), color=TEAL, lw=2.4, ms=14, z=5)
    arrow(ax, (x0, y0), (x0 + s * r * et[0], y0 + s * r * et[1]), color=AMBER, lw=2.4, ms=14, z=5)
    off = -0.045 * er
    arrow(ax, (x0 + off[0], y0 + off[1]), (x0 + off[0] + s * et[0], y0 + off[1] + s * et[1]), color=NAVY, lw=1.8,
          ms=12, z=6)
    ax.plot([x0], [y0], "o", color=TEXT, ms=4, zorder=7)
    ax.text(x0 + s * er[0] + 0.04, y0 + s * er[1] - 0.04, r"$\partial_r = \hat e_r$" + "\n(length 1)",
            color=TEAL, fontsize=10, ha="left", va="top")
    ax.text(x0 + s * r * et[0] - 0.05, y0 + s * r * et[1] + 0.02, r"$\partial_\theta$ (length $r = 1.5$)",
            color=AMBER, fontsize=10, ha="right", va="bottom")
    ax.text(x0 + off[0] + s * et[0] - 0.06, y0 + off[1] + s * et[1] - 0.06, r"$\hat e_\theta = \frac{1}{r}\partial_\theta$",
            color=NAVY, fontsize=10, ha="right", va="top")
    ax.text(x0 + 0.06, y0 - 0.1, r"$(r, \theta) = (1.5, 45^\circ)$", fontsize=9.5, ha="left", va="top")
    ax.text(2.3, 0.0, "arrows drawn at half scale", fontsize=9.5, ha="right", va="bottom", color=SLATE)
    ax.set_xlim(-0.1, 2.35)
    ax.set_ylim(-0.1, 2.35)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.set_title("(b) Coordinate vs orthonormal basis", fontweight="bold", color=TEXT, pad=8)
    print("    basis at (1.5, 45 deg): |d_r| = 1, |d_theta| = r = 1.5, |e_theta hat| = 1 (drawn at half scale)")
    fig.tight_layout(w_pad=1.5)
    save_fig(fig, out_dir, "maths1_polar_constant_field.png")


# ---------------------------------------------------------------------------
# Figure 25: Schwarzschild tides
# ---------------------------------------------------------------------------
def fig_tides(out_dir: Path) -> None:
    print("Figure 25 maths1_schwarzschild_tides.png")
    print("    radial tidal acceleration per unit radial separation: +2M/r^3 (stretch)")
    print("    transverse tidal acceleration per unit transverse separation: -M/r^3 (squeeze), twice in 3D")
    print("    trace: 2 - 1 - 1 = 0 (volume unchanged at first)")
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    ax.add_patch(Circle((-3.1, 0), 0.75, fc=TEXT, ec=TEXT, zorder=3))
    ax.text(-3.1, -0.98, "mass $M$", fontsize=10.5, ha="center", va="top")
    arrow(ax, (-2.05, -1.75), (2.9, -1.75), color=SLATE, lw=1.2, ms=11)
    ax.text(0.4, -1.85, "radial direction (away from the mass)", fontsize=9.5, ha="center", va="top", color=SLATE)
    c = np.array([1.0, 0.0])
    R0 = 0.8
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(c[0] + R0 * np.cos(th), c[1] + R0 * np.sin(th), color=NAVY, lw=1.6, zorder=4)
    a, b = R0 * 1.45, R0 * 0.775
    ax.plot(c[0] + a * np.cos(th), c[1] + b * np.sin(th), color=RED, lw=1.6, ls=(0, (5, 3)), zorder=4)
    k = 0.55
    for kk in range(12):
        t = 2 * math.pi * kk / 12
        S = np.array([R0 * math.cos(t), R0 * math.sin(t)])
        A = np.array([2 * S[0], -S[1]]) * k * 0.5
        p0 = c + S
        ax.plot(*p0, "o", color=NAVY, ms=4.5, zorder=6)
        if np.linalg.norm(A) > 1e-6:
            arrow(ax, p0, p0 + A, color=AMBER, lw=1.7, ms=11, z=7)
    ax.plot(*c, "o", color=TEXT, ms=5, zorder=6)
    ax.text(c[0], c[1] - 0.1, "reference", fontsize=9.5, ha="center", va="top")
    label_box(ax, 3.55, 0.75, r"radial: $A = +\frac{2M}{r^3}\,S$" + "\n(stretch)", color=AMBER, fs=10.5, ha="left")
    label_box(ax, 3.55, -0.45, r"transverse: $A = -\frac{M}{r^3}\,S$" + "\n(squeeze)", color=AMBER, fs=10.5, ha="left")
    ax.text(c[0], 1.38, "dust ring (solid) and its later shape (dashed)", fontsize=9.5, ha="center",
            va="bottom", color=TEXT)
    label_box(ax, -3.1, 1.25, "in 3D: one stretch, two squeezes,\n" + r"$2 - 1 - 1 = 0$: volume unchanged at first",
              color=SLATE, fs=9.5)
    ax.set_xlim(-4.2, 6.4)
    ax.set_ylim(-2.25, 1.85)
    ax.set_aspect("equal")
    clean_axes(ax)
    save_fig(fig, out_dir, "maths1_schwarzschild_tides.png")


# ---------------------------------------------------------------------------
# Figure 24: meridians converging
# ---------------------------------------------------------------------------
def fig_meridians(out_dir: Path) -> None:
    print("Figure 24 maths1_meridian_deviation.png")
    lats = [0, 30, 60, 80]
    for la in lats:
        print(f"    latitude {la:2d} deg: s = {math.radians(la):.3f}, |S|/S0 = cos(s) = {math.cos(math.radians(la)):.3f}")
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.6), gridspec_kw={"width_ratios": [1.0, 1.15]})
    ax = axes[0]
    lat0, lon0, R = 25.0, 0.0, 1.6
    ax.add_patch(Circle((0, 0), R, fc=BLUE_PALE, ec=NAVY, lw=1.4, zorder=1))
    lo = np.linspace(-180, 180, 721)
    for la in (0, 30, 60):
        x, y, cc = ortho(la, lo, lat0, lon0, R)
        x = np.where(cc > 0, x, np.nan)
        ax.plot(x, y, color=GREY_LINE if la else SLATE, lw=0.9 if la else 1.3, zorder=2)
    mer = (-18.0, 18.0)
    la_line = np.linspace(0, 90, 300)
    for m, col in zip(mer, (TEAL, AMBER)):
        x, y, _ = ortho(la_line, m, lat0, lon0, R)
        ax.plot(x, y, color=col, lw=2.2, zorder=4)
        xs, ys, _ = ortho(np.array([0.0, 8.0]), m, lat0, lon0, R)
        arrow(ax, (xs[0], ys[0]), (xs[1], ys[1]), color=col, lw=2.2, ms=14, z=5)
    for la in lats:
        xa, ya, _ = ortho(la, mer[0], lat0, lon0, R)
        xb, yb, _ = ortho(la, mer[1], lat0, lon0, R)
        arrow(ax, (xa, ya), (xb, yb), color=RED, lw=1.8, ms=11, z=6)
        ax.text(xb + 0.08, yb, f"${la}^\\circ$", fontsize=9.5, ha="left", va="center", color=RED)
    xn, yn, _ = ortho(90, 0, lat0, lon0, R)
    ax.plot([xn], [yn], "o", color=TEXT, ms=4.5, zorder=7)
    ax.text(xn, yn + 0.1, "N", fontsize=10.5, ha="center", va="bottom", fontweight="bold")
    ax.text(0.0, -R - 0.12, "equator", fontsize=9.5, ha="center", va="top", color=SLATE)
    label_box(ax, -1.25, -1.35, r"deviation $S$ (red)", color=RED, fs=9.5)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-2.0, 1.95)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.set_title("(a) Two meridians leaving the equator parallel", fontweight="bold", color=TEXT, pad=8)

    ax = axes[1]
    s = np.linspace(0, np.pi / 2, 300)
    ax.plot(s, np.cos(s), color=RED, lw=2.2)
    for la in lats:
        sv = math.radians(la)
        ax.plot([sv], [math.cos(sv)], "o", color=RED, ms=6, zorder=5)
        ax.text(sv + 0.04, math.cos(sv) + 0.03, f"${la}^\\circ$", fontsize=9.5, ha="left", va="bottom", color=RED)
    ax.set_xlim(0, 1.72)
    ax.set_ylim(0, 1.12)
    ax.set_xticks([0, np.pi / 6, np.pi / 3, np.pi / 2])
    ax.set_xticklabels([r"$0$", r"$\frac{\pi}{6}$", r"$\frac{\pi}{3}$", r"$\frac{\pi}{2}$"], fontsize=11)
    ax.set_yticks([0, 0.5, 1])
    ax.set_xlabel(r"distance travelled from the equator, $s$ (unit sphere)")
    ax.set_ylabel(r"$|S| \,/\, S_0$")
    for sp_ in ("top", "right"):
        ax.spines[sp_].set_visible(False)
    label_box(ax, 1.08, 0.82, r"$|S| = S_0\cos s$" + "\n" + r"$\ddot S = -K S$ with $K = 1$", color=RED, fs=10.5)
    ax.set_title(r"(b) The gap shrinks like $\cos s$", fontweight="bold", color=TEXT, pad=8)
    fig.tight_layout(w_pad=2.0)
    save_fig(fig, out_dir, "maths1_meridian_deviation.png")


# ---------------------------------------------------------------------------
# Figure 21: light cone
# ---------------------------------------------------------------------------
def fig_light_cone(out_dir: Path) -> None:
    print("Figure 21 maths1_light_cone.png")
    vecs = {"timelike": (0.35, 1.0), "null": (1.0, 1.0), "spacelike": (1.0, 0.35)}
    for nm, (x, t) in vecs.items():
        print(f"    {nm} ({x:g}, {t:g}): g(X, X) = -t^2 + x^2 = {-t * t + x * x:.4f}")
    print("    unit hyperbolas: t^2 - x^2 = 1 is g(X, X) = -1; x^2 - t^2 = 1 is g(X, X) = +1")
    fig, ax = plt.subplots(figsize=(6.6, 6.6))
    L = 2.4
    ax.fill([0, L, -L], [0, L, L], color=BLUE_LIGHT, zorder=0, lw=0)
    ax.fill([0, L, -L], [0, -L, -L], color=BLUE_LIGHT, zorder=0, lw=0)
    ax.fill([0, L, L], [0, L, -L], color=AMBER_LIGHT, zorder=0, lw=0)
    ax.fill([0, -L, -L], [0, L, -L], color=AMBER_LIGHT, zorder=0, lw=0)
    ax.plot([-L, L], [-L, L], color=SLATE, lw=1.4, ls=(0, (5, 3)), zorder=2)
    ax.plot([-L, L], [L, -L], color=SLATE, lw=1.4, ls=(0, (5, 3)), zorder=2)
    ax.axhline(0, color=GREY_LINE, lw=0.8, zorder=1)
    ax.axvline(0, color=GREY_LINE, lw=0.8, zorder=1)
    xh = np.linspace(-2.15, 2.15, 300)
    ax.plot(xh, np.sqrt(1 + xh ** 2), color=NAVY, lw=1.8, zorder=3)
    th = np.linspace(-2.15, 2.15, 300)
    ax.plot(np.sqrt(1 + th ** 2), th, color=AMBER, lw=1.5, zorder=3, ls=(0, (2, 2)))
    cols = {"timelike": NAVY, "null": SLATE, "spacelike": AMBER}
    for nm, (x, t) in vecs.items():
        arrow(ax, (0, 0), (x, t), color=cols[nm], lw=2.4, ms=15, z=5)
    bb = dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.9)
    ax.text(0.05, 1.42, "timelike: $g(X, X) < 0$", fontsize=10, ha="center", va="bottom", color=NAVY, zorder=6,
            bbox=bb)
    ax.text(1.08, 0.95, "null:\n$g(X, X) = 0$", fontsize=10, ha="left", va="top", color=SLATE, zorder=6, bbox=bb)
    ax.text(1.12, 0.22, "spacelike:\n$g(X, X) > 0$", fontsize=10, ha="left", va="top", color=AMBER, zorder=6, bbox=bb)
    ax.text(-1.55, 2.1, r"$t^2 - x^2 = 1$:" + "\n" + r"$g(X, X) = -1$", fontsize=10, ha="center", va="top",
            color=NAVY, zorder=6, bbox=bb)
    ax.text(2.33, -1.05, r"$x^2 - t^2 = 1$:" + "\n" + r"$g(X, X) = +1$", fontsize=10, ha="right", va="center",
            color=AMBER, zorder=6, bbox=bb)
    label_box(ax, 0.0, -1.55, "inside the cone:\na signal can travel this way", color=NAVY, fs=9.5)
    label_box(ax, -1.62, 0.0, "outside:\nno signal;\ncan be made\nsimultaneous", color=AMBER, fs=9.5)
    ax.text(L - 0.05, -0.08, r"$x$", fontsize=12, ha="right", va="top")
    ax.text(0.07, L - 0.05, r"$t$", fontsize=12, ha="left", va="top")
    ax.set_xlim(-L, L)
    ax.set_ylim(-L, L)
    ax.set_aspect("equal")
    clean_axes(ax)
    save_fig(fig, out_dir, "maths1_light_cone.png")


# ---------------------------------------------------------------------------
# Figure 22: Betti numbers
# ---------------------------------------------------------------------------
def half_ellipse(ax, c, a, b, front, color, lw, z=4):
    t = np.linspace(np.pi, 2 * np.pi, 200) if front else np.linspace(0, np.pi, 200)
    ax.plot(c[0] + a * np.cos(t), c[1] + b * np.sin(t), color=color, lw=lw, zorder=z,
            ls="-" if front else (0, (3, 2.5)))


def fig_betti(out_dir: Path) -> None:
    print("Figure 22 maths1_betti_loops.png")
    print("    sphere: (b0, b1, b2) = (1, 0, 1); torus: (b0, b1, b2) = (1, 2, 1)")
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.3), gridspec_kw={"width_ratios": [1.0, 1.35]})
    ax = axes[0]
    ax.add_patch(Circle((0, 0), 1.5, fc=BLUE_PALE, ec=NAVY, lw=1.6, zorder=1))
    half_ellipse(ax, (0, 0), 1.5, 0.38, True, GREY_LINE, 1.0, z=2)
    half_ellipse(ax, (0, 0), 1.5, 0.38, False, GREY_LINE, 1.0, z=2)
    for (cy, a, b), col in zip(((0.55, 0.95, 0.24), (0.88, 0.55, 0.14), (1.10, 0.24, 0.06)), (TEAL, TEAL, TEAL)):
        half_ellipse(ax, (0.25, cy), a, b, True, col, 2.0, z=5)
        half_ellipse(ax, (0.25, cy), a, b, False, col, 1.3, z=5)
    ax.plot([0.25], [1.21], "o", color=TEAL, ms=4.5, zorder=6)
    ax.annotate("", xy=(0.25, 1.05), xytext=(0.25, 0.42), arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.4),
                zorder=6)
    ax.text(0.0, -1.68, "every loop shrinks to a point: $b_1 = 0$", fontsize=10, ha="center", va="top",
            color=TEAL)
    ax.text(0.0, -2.0, r"$(b_0, b_1, b_2) = (1, 0, 1)$", fontsize=10.5, ha="center", va="top", color=TEXT)
    ax.set_xlim(-1.9, 1.9)
    ax.set_ylim(-2.35, 1.75)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.set_title("(a) Sphere", fontweight="bold", color=TEXT, pad=8)

    ax = axes[1]
    ax.add_patch(Ellipse((0, 0), 4.4, 2.3, fc=BLUE_PALE, ec=NAVY, lw=1.6, zorder=1))
    # hole: lower "smile" and upper arc
    t = np.linspace(np.pi * 1.08, np.pi * 1.92, 200)
    ax.plot(0.95 * np.cos(t), 0.12 + 0.42 * np.sin(t), color=NAVY, lw=1.6, zorder=3)
    t2 = np.linspace(np.pi * 0.15, np.pi * 0.85, 200)
    ax.plot(0.72 * np.cos(t2), -0.32 + 0.38 * np.sin(t2), color=NAVY, lw=1.6, zorder=3)
    # loop around the hole (along the tube centre line)
    half_ellipse(ax, (0, 0.0), 1.6, 0.78, True, AMBER, 2.2, z=5)
    half_ellipse(ax, (0, 0.0), 1.6, 0.78, False, AMBER, 1.4, z=5)
    # loop around the tube (small cross-section on the right)
    cxr = 1.62
    tt = np.linspace(-np.pi / 2, np.pi / 2, 200)
    ax.plot(cxr + 0.2 * np.cos(tt), 0.0 + 0.55 * np.sin(tt) - 0.02, color=RED, lw=2.2, zorder=6)
    tt2 = np.linspace(np.pi / 2, 3 * np.pi / 2, 200)
    ax.plot(cxr + 0.2 * np.cos(tt2), 0.0 + 0.55 * np.sin(tt2) - 0.02, color=RED, lw=1.4, zorder=6, ls=(0, (3, 2.5)))
    label_box(ax, -1.75, 1.45, "loop round the hole", color=AMBER, fs=10)
    arrow(ax, (-1.6, 1.28), (-1.12, -0.52), color=AMBER, lw=1.0, ms=9)
    label_box(ax, 2.2, 1.45, "loop round the tube", color=RED, fs=10)
    arrow(ax, (2.15, 1.28), (1.83, 0.3), color=RED, lw=1.0, ms=9)
    ax.text(0.0, -1.42, "two independent loops that can't be shrunk: $b_1 = 2$", fontsize=10, ha="center",
            va="top", color=TEXT)
    ax.text(0.0, -1.74, r"$(b_0, b_1, b_2) = (1, 2, 1)$", fontsize=10.5, ha="center", va="top", color=TEXT)
    ax.set_xlim(-2.7, 2.95)
    ax.set_ylim(-2.1, 1.75)
    ax.set_aspect("equal")
    clean_axes(ax)
    ax.set_title("(b) Torus", fontweight="bold", color=TEXT, pad=8)
    fig.tight_layout(w_pad=1.5)
    save_fig(fig, out_dir, "maths1_betti_loops.png")


def main() -> None:
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(1)
    out_dir = Path(sys.argv[1])
    out_dir.mkdir(parents=True, exist_ok=True)
    fig_dual_basis(out_dir)
    fig_charts(out_dir)
    fig_pv(out_dir)
    fig_lie_bracket(out_dir)
    fig_closed_not_exact(out_dir)
    fig_liouville(out_dir)
    fig_polar(out_dir)
    fig_tides(out_dir)
    fig_meridians(out_dir)
    fig_light_cone(out_dir)
    fig_betti(out_dir)


if __name__ == "__main__":
    main()
