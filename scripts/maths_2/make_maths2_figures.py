"""Figures for Maths 0 (Rings & Fields) and Maths 2 (Group Theory).

Usage: python make_maths2_figures.py OUTPUT_DIR

Writes twelve PNGs into OUTPUT_DIR. The rings-and-fields part moved to Maths 0 on 2026-11-07, so the
figures now sit as:
  Maths 0, Figure 2: maths2_tape_quotient_isomorphism.png
  Maths 0, Figure 3: maths2_f9_field.png
  Maths 2, Figure 1: maths2_s3_cosets_normality.png
  Maths 2, Figure 2: maths2_cosets_conjugacy_s4.png
  Maths 2, Figure 3: maths2_class_equation.png
  Maths 2, Figure 4: maths2_fourth_isomorphism_fibration.png
  Maths 2, Figure 6: maths2_orbit_stabilizer_square.png
  Maths 2, Figure 7: maths2_extensions_mortar.png
  Maths 2, Figure 9: maths2_orbits_blocks_suborbits_hexagon.png
  Maths 2, Figure 10: maths2_orbitals_blocks_primitivity.png
  Maths 2, Figure 11: maths2_subspace_quotient_shear.png
  Maths 2, Figure 12: maths2_coherent_intersection_pentagon.png
The other figures come from make_maths2_rep_figures.py, make_maths2_benson_figures.py and
make_maths0_maths2_extra_figures.py.

Reproduces the published PNGs byte for byte with matplotlib 3.5.1 (drawn by Gemini, 2026-11-05;
the cosets and orbit-stabilizer figures switched to left-to-right products the same day, to match
the text; the centralizer-cosets and hexagon figures were added by Claude the same day; the
function names keep the original numbering).
"""

import itertools as it
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Polygon
import numpy as np

# Unified palette across all 10 figures:
# Identity coset / trivial orbital / kernel / zero: GREY
# 1st non-trivial role: BLUE
# 2nd non-trivial role: ORANGE
# 3rd non-trivial role: GREEN
# 4th non-trivial role: PURPLE
GREY = "#6e6e6e"
GREY_LIGHT = "#e6e6e6"
BLUE = "#1f3b73"
BLUE_LIGHT = "#d6e4f5"
ORANGE = "#d9730d"
ORANGE_LIGHT = "#fde2c8"
GREEN = "#2b7a4b"
GREEN_LIGHT = "#d5efe0"
PURPLE = "#6b3fa0"
PURPLE_LIGHT = "#e6daf5"
DARK = "#222222"


def compose(p, q):
    """Right-to-left composition (p o q)(x) = p(q(x))."""
    return tuple(p[q[i]] for i in range(len(p)))


def invert(p):
    inv = [0] * len(p)
    for i, v in enumerate(p):
        inv[v] = i
    return tuple(inv)


def get_d8():
    """Return D_8 acting on corners 0, 1, 2, 3 (labelled 1, 2, 3, 4)."""
    e = (0, 1, 2, 3)
    r = (1, 2, 3, 0)       # (1 2 3 4)
    r2 = compose(r, r)     # (1 3)(2 4)
    r3 = compose(r2, r)    # (1 4 3 2)
    s_h = (1, 0, 3, 2)     # (1 2)(3 4)
    s_v = (3, 2, 1, 0)     # (1 4)(2 3)
    d13 = (0, 3, 2, 1)     # (2 4)
    d24 = (2, 1, 0, 3)     # (1 3)
    D8 = [e, r, r2, r3, s_h, s_v, d13, d24]
    assert len(set(D8)) == 8
    return D8, dict(e=e, r=r, r2=r2, r3=r3, s_h=s_h, s_v=s_v, d13=d13, d24=d24)


def draw_node(ax, x, y, label="", r=0.14, face="white", edge=DARK, fs=11,
              square=False, lw=2.0, text_color=DARK, zorder=3, weight="normal"):
    if square:
        patch = plt.Rectangle((x - r, y - r), 2 * r, 2 * r,
                              facecolor=face, edgecolor=edge, lw=lw, zorder=zorder)
    else:
        patch = plt.Circle((x, y), r, facecolor=face, edgecolor=edge, lw=lw, zorder=zorder)
    ax.add_patch(patch)
    if label:
        ax.text(x, y, label, ha="center", va="center", fontsize=fs,
                color=text_color, fontweight=weight, zorder=zorder + 1)


def draw_box(ax, x, y, w, h, label="", face="white", edge=DARK, lw=1.8,
             fs=11, text_color=DARK, pad=0.06, ls="-", zorder=2, weight="normal"):
    patch = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={pad}",
                           facecolor=face, edgecolor=edge, lw=lw, linestyle=ls, zorder=zorder)
    ax.add_patch(patch)
    if label:
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=fs, color=text_color, fontweight=weight, zorder=zorder + 1)


# =========================================================================
# Figure 1 (P1): Ideals as seams on a tape and Third Isomorphism Theorem
# =========================================================================
def fig1_tape_quotient(out):
    R_mod_I = list(range(12))
    J_mod_I = [x for x in R_mod_I if x % 4 == 0]
    assert J_mod_I == [0, 4, 8]
    cosets = {r: sorted((r + j) % 12 for j in J_mod_I) for r in range(4)}
    assert cosets == {0: [0, 4, 8], 1: [1, 5, 9], 2: [2, 6, 10], 3: [3, 7, 11]}

    # Residue colours mod 4: [0] identity coset is GREY, [1] BLUE, [2] ORANGE, [3] GREEN
    res_Stroke = [GREY, BLUE, ORANGE, GREEN]
    res_Fill = [GREY_LIGHT, BLUE_LIGHT, ORANGE_LIGHT, GREEN_LIGHT]

    fig = plt.figure(figsize=(8.6, 6.4))
    ax_top = fig.add_axes([0.03, 0.67, 0.94, 0.26])
    ax_left = fig.add_axes([0.02, 0.03, 0.54, 0.60])
    ax_right = fig.add_axes([0.58, 0.03, 0.40, 0.60])

    # --- Top panel: Integer tape R = Z ---
    nums = list(range(-4, 16))
    for k in nums:
        r = k % 4
        x = k
        rect = plt.Rectangle((x - 0.44, -0.28), 0.88, 0.56,
                             facecolor=res_Fill[r], edgecolor=res_Stroke[r], lw=1.6, zorder=2)
        ax_top.add_patch(rect)
        ax_top.text(x, 0.0, f"${k}$", ha="center", va="center", fontsize=10.5, color=DARK, zorder=3)
        if k % 4 == 0:
            is_12 = (k % 12 == 0)
            lw = 3.0 if is_12 else 1.8
            ls = "-" if is_12 else "--"
            col = DARK if is_12 else GREY
            ax_top.plot([x - 0.5, x - 0.5], [-0.48, 0.48], color=col, lw=lw, ls=ls, zorder=4)
            if is_12:
                ax_top.text(x, 0.53, f"$I = 12\\mathbb{{Z}}$ seam", ha="center", va="bottom",
                            fontsize=10.5, color=DARK, fontweight="bold")
            else:
                ax_top.text(x, -0.50, f"$J = 4\\mathbb{{Z}}$", ha="center", va="top",
                            fontsize=9.5, color=GREY)

    ax_top.text(-4.8, 0.0, "$\\cdots$", ha="center", va="center", fontsize=14, color=DARK)
    ax_top.text(15.8, 0.0, "$\\cdots$", ha="center", va="center", fontsize=14, color=DARK)
    ax_top.set_title("Integer tape $R = \\mathbb{Z}$ with nested ideal seams $I = 12\\mathbb{Z} \\subseteq J = 4\\mathbb{Z}$",
                     fontsize=12.5, pad=6)
    ax_top.set_xlim(-5.3, 16.3)
    ax_top.set_ylim(-0.85, 0.88)
    ax_top.axis("off")

    # --- Left panel: Two-stage fold (R/I)/(J/I) ---
    cx1, cy1, rad1 = -1.35, 0.0, 1.32
    pts12 = {}
    for k in range(12):
        ang = np.pi / 2 - 2 * np.pi * k / 12
        pts12[k] = (cx1 + rad1 * np.cos(ang), cy1 + rad1 * np.sin(ang))

    circ12 = plt.Circle((cx1, cy1), rad1, fill=False, edgecolor="#cccccc", lw=1.8, zorder=1)
    ax_left.add_patch(circ12)

    for r in range(4):
        tri_pts = [pts12[m] for m in cosets[r]]
        poly = Polygon(tri_pts, closed=True, facecolor=res_Fill[r],
                       edgecolor=res_Stroke[r], alpha=0.35 if r > 0 else 0.45,
                       lw=2.2 if r == 0 else 1.7, ls="-" if r == 0 else "--", zorder=2)
        ax_left.add_patch(poly)

    for k in range(12):
        r = k % 4
        x, y = pts12[k]
        draw_node(ax_left, x, y, f"${k}$", r=0.22, face=res_Fill[r], edge=res_Stroke[r], fs=10.5, lw=1.8, zorder=4)

    ax_left.text(cx1, cy1 + 1.75, "$R/I = \\mathbb{Z}/12\\mathbb{Z}$", ha="center", va="center", fontsize=11.5, color=DARK)
    ax_left.text(cx1, cy1 - 1.78, "triangles: cosets of $J/I = \\{[0],[4],[8]\\}$",
                 ha="center", va="center", fontsize=10.5, color=DARK)

    # Arrow to collapsed 4-clock on the right side of panel (a), with wider gap
    ax_left.annotate("", xy=(1.18, 0.0), xytext=(0.25, 0.0),
                     arrowprops=dict(arrowstyle="-|>", color=DARK, lw=2.4, mutation_scale=18))
    ax_left.text(0.71, 0.32, "glue $J/I$", ha="center", va="center", fontsize=10.5, color=DARK)

    cx2, cy2, rad2 = 2.02, 0.0, 0.66
    circ4 = plt.Circle((cx2, cy2), rad2, fill=False, edgecolor=DARK, lw=2.0, zorder=1)
    ax_left.add_patch(circ4)
    for r in range(4):
        ang = np.pi / 2 - 2 * np.pi * r / 4
        x, y = cx2 + rad2 * np.cos(ang), cy2 + rad2 * np.sin(ang)
        draw_node(ax_left, x, y, f"$[{r}]$", r=0.24, face=res_Fill[r], edge=res_Stroke[r], fs=11, lw=2.0, zorder=4)
    ax_left.text(cx2, cy2 + 1.18, "$(R/I)/(J/I)$", ha="center", va="center", fontsize=11.5, color=DARK)

    ax_left.set_xlim(-3.0, 3.0)
    ax_left.set_ylim(-2.1, 2.15)
    ax_left.set_aspect("equal")
    ax_left.axis("off")
    ax_left.set_title("(a) Two-stage fold $(R/I)/(J/I)$", fontsize=12.5, pad=4)

    # --- Right panel: Direct fold R/J = Z/4Z with coset stacks ---
    # Light vertical separator between panels (a) and (b)
    ax_right.plot([-2.12, -2.12], [-1.95, 1.95], color="#dddddd", lw=1.4, ls="-", zorder=1)

    cx3, cy3, rad3 = 0.12, -0.05, 0.90
    circ_dir = plt.Circle((cx3, cy3), rad3, fill=False, edgecolor=DARK, lw=2.2, zorder=1)
    ax_right.add_patch(circ_dir)

    # Place coset labels outside the circle beside each node, well away from panel (a)
    stack_offsets = {
        0: (0.0, 0.56),
        1: (0.34, 0.54),
        2: (0.0, -0.58),
        3: (-0.34, 0.54),
    }
    for r in range(4):
        ang = np.pi / 2 - 2 * np.pi * r / 4
        x, y = cx3 + rad3 * np.cos(ang), cy3 + rad3 * np.sin(ang)
        draw_node(ax_right, x, y, f"$[{r}]$", r=0.25, face=res_Fill[r], edge=res_Stroke[r], fs=11.5, lw=2.2, zorder=4)
        dx, dy = stack_offsets[r]
        vals = ", ".join(str(v) for v in cosets[r])
        ax_right.text(x + dx, y + dy, f"$\\{{{vals}\\}}$", ha="center", va="center",
                      fontsize=10.2, color=res_Stroke[r],
                      bbox=dict(boxstyle="round,pad=0.18", facecolor=res_Fill[r], edgecolor=res_Stroke[r], lw=1.2),
                      zorder=5)

    ax_right.text(cx3, 1.82, "$R/J = \\mathbb{Z}/4\\mathbb{Z}$", ha="center", va="center", fontsize=11.5, color=DARK)
    ax_right.text(cx3, -1.86, "fold directly every $4$ steps", ha="center", va="center", fontsize=10.5, color=DARK)
    ax_right.set_xlim(-2.22, 2.22)
    ax_right.set_ylim(-2.1, 2.15)
    ax_right.set_aspect("equal")
    ax_right.axis("off")
    ax_right.set_title("(b) Direct fold $R/J$", fontsize=12.5, pad=4)

    fig.savefig(os.path.join(out, "maths2_tape_quotient_isomorphism.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 2 (P2): Building F_9 (no Frobenius arrows or text!)
# =========================================================================
def fig2_f9_field(out):
    def add(x, y):
        return ((x[0] + y[0]) % 3, (x[1] + y[1]) % 3)

    def mul(x, y):
        return ((x[0] * y[0] + 2 * x[1] * y[1]) % 3, (x[0] * y[1] + x[1] * y[0]) % 3)

    one = (1, 0)
    alpha = (1, 1)
    powers = []
    cur = one
    for _ in range(8):
        powers.append(cur)
        cur = mul(cur, alpha)
    assert cur == one and len(set(powers)) == 8

    def elem_str(a, b):
        if a == 0 and b == 0:
            return "0"
        if b == 0:
            return f"{a}"
        b_part = "i" if b == 1 else "2i"
        if a == 0:
            return b_part
        return f"{a}+{b_part}"

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 4.6), gridspec_kw=dict(width_ratios=[1, 1.15]))

    # --- Left panel: 3x3 additive grid over F_3 ---
    prime_box = FancyBboxPatch((-0.46, -0.46), 2.92, 0.92, boxstyle="round,pad=0.06",
                               facecolor=BLUE_LIGHT, edgecolor=BLUE, lw=2.0, ls="--", alpha=0.55, zorder=1)
    ax1.add_patch(prime_box)
    ax1.text(1.0, -0.78, "prime subfield $\\mathbb{F}_3 = \\{0, 1, 2\\}$",
             ha="center", va="center", fontsize=11, color=BLUE)

    for a in range(3):
        ax1.plot([a, a], [0, 2], color="#cccccc", lw=1.5, zorder=1)
    for b in range(3):
        ax1.plot([0, 2], [b, b], color="#cccccc", lw=1.5, zorder=1)

    for b in range(3):
        for a in range(3):
            if (a, b) == (0, 0):
                face, edge = GREY_LIGHT, GREY
            elif a == 0 or b == 0:
                # The four even powers {1, 2, i, 2i}
                face, edge = BLUE_LIGHT, BLUE
            else:
                # The four primitive generators {1+i, 2+i, 1+2i, 2+2i}
                face, edge = ORANGE_LIGHT, ORANGE
            draw_box(ax1, a - 0.34, b - 0.28, 0.68, 0.56, f"${elem_str(a, b)}$",
                     face=face, edge=edge, lw=2.0, fs=11.5, pad=0.04, zorder=3)

    # Show +1, +1, +1 wrapping back to 0 cleanly above the top row (rad > 0 arches UPWARD from right to left)
    ax1.annotate("", xy=(0.92, 2.40), xytext=(0.08, 2.40),
                 arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.9, mutation_scale=14))
    ax1.annotate("", xy=(1.92, 2.40), xytext=(1.08, 2.40),
                 arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.9, mutation_scale=14))
    arc = FancyArrowPatch((2.0, 2.50), (0.0, 2.50),
                          connectionstyle="arc3,rad=0.28",
                          arrowstyle="-|>", color=ORANGE, lw=1.9, mutation_scale=14, zorder=4)
    ax1.add_patch(arc)
    ax1.text(1.0, 3.05, "adding $3$ times wraps to $0$: $1+1+1=0$",
             ha="center", va="center", fontsize=10.5, color=ORANGE)

    ax1.text(-0.68, 0.0, "$0$", ha="center", va="center", fontsize=10.5, color=GREY)
    ax1.text(-0.68, 1.0, "$i$", ha="center", va="center", fontsize=10.5, color=GREY)
    ax1.text(-0.68, 2.0, "$2i$", ha="center", va="center", fontsize=10.5, color=GREY)
    ax1.set_xlim(-0.95, 2.65)
    ax1.set_ylim(-1.05, 3.35)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("(a) $3 \\times 3$ additive grid $\\mathbb{F}_3^2$", fontsize=12.5, pad=6)

    # --- Right panel: Multiplicative 8-cycle of alpha = 1 + i ---
    rad = 1.48
    pts8 = []
    for k in range(8):
        ang = np.pi / 2 - 2 * np.pi * k / 8
        pts8.append((rad * np.cos(ang), rad * np.sin(ang)))

    even_pts = [pts8[0], pts8[2], pts8[4], pts8[6]]
    sq_poly = Polygon(even_pts, closed=True, facecolor=BLUE_LIGHT, edgecolor=BLUE,
                      alpha=0.28, lw=1.8, ls="--", zorder=1)
    ax2.add_patch(sq_poly)

    for k in range(8):
        x1, y1 = pts8[k]
        x2, y2 = pts8[(k + 1) % 8]
        arr = FancyArrowPatch((x1, y1), (x2, y2),
                              connectionstyle="arc3,rad=-0.12",
                              arrowstyle="-|>", color=ORANGE, lw=2.2,
                              shrinkA=22, shrinkB=22, mutation_scale=15, zorder=2)
        ax2.add_patch(arr)

    draw_node(ax2, 0.0, 0.0, "$0$", r=0.22, face=GREY_LIGHT, edge=GREY, fs=11.5, lw=1.8, zorder=3)
    ax2.text(0.0, -0.45, "$\\langle i \\rangle$ even\npowers", ha="center", va="center", fontsize=9.8, color=BLUE)

    for k, (a, b) in enumerate(powers):
        x, y = pts8[k]
        is_even = (k % 2 == 0)
        face = BLUE_LIGHT if is_even else ORANGE_LIGHT
        edge = BLUE if is_even else ORANGE
        draw_node(ax2, x, y, f"${elem_str(a, b)}$", r=0.33, face=face, edge=edge, fs=10.5, lw=2.0, zorder=4)
        ang = np.pi / 2 - 2 * np.pi * k / 8
        lx, ly = (rad + 0.52) * np.cos(ang), (rad + 0.50) * np.sin(ang)
        ax2.text(lx, ly, f"$\\alpha^{k}$", ha="center", va="center",
                 fontsize=10.5, color=BLUE if is_even else ORANGE)

    ax2.text(0.0, -2.22, "step around ring: $\\times\\,\\alpha = \\times(1+i)$",
             ha="center", va="center", fontsize=10.8, color=DARK)
    ax2.set_xlim(-2.25, 2.25)
    ax2.set_ylim(-2.45, 2.22)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("(b) Multiplicative 8-cycle $\\mathbb{F}_9^\\times = \\langle 1+i \\rangle$", fontsize=12.5, pad=6)

    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths2_f9_field.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 3 (P3): S_3 Cayley tables stacked vertically
# =========================================================================
def fig3_s3_cosets(out):
    # Figure 3 multiplies left to right, as the text of the notes does:
    # gh means first g, then h, so (gh)(x) = h(g(x)).
    def mul(g, h):
        return compose(h, g)

    e = (0, 1, 2)
    r1 = (1, 2, 0)   # (1 2 3)
    r2 = (2, 0, 1)   # (1 3 2)
    s12 = (1, 0, 2)  # (1 2)
    s13 = (2, 1, 0)  # (1 3)
    s23 = (0, 2, 1)  # (2 3)

    lbl = {
        e: "$e$",
        r1: "$(1\\,2\\,3)$",
        r2: "$(1\\,3\\,2)$",
        s12: "$(1\\,2)$",
        s13: "$(1\\,3)$",
        s23: "$(2\\,3)$",
    }

    fig = plt.figure(figsize=(8.4, 10.2))
    ax_a = fig.add_axes([0.04, 0.55, 0.92, 0.41])
    ax_b = fig.add_axes([0.04, 0.02, 0.92, 0.49])

    # --- Panel (a): Normal subgroup N = A_3 ---
    order_a = [e, r1, r2, s12, s13, s23]
    N_set = {e, r1, r2}

    def col_a(g):
        return (GREY_LIGHT, GREY) if g in N_set else (BLUE_LIGHT, BLUE)

    cw, ch = 0.88, 0.56
    ox, oy = 1.15, 0.25

    ax_a.text(ox - 0.55, oy + 6 * ch + 0.28, "$g \\cdot h$", ha="center", va="center", fontsize=11, fontweight="bold")
    for idx, g in enumerate(order_a):
        fc, ec = col_a(g)
        draw_box(ax_a, ox + idx * cw + 0.03, oy + 6 * ch + 0.06, cw - 0.06, ch - 0.08,
                 lbl[g], face=fc, edge=ec, lw=1.4, fs=10, pad=0.02)
        r_y = oy + (5 - idx) * ch
        draw_box(ax_a, ox - cw - 0.06, r_y + 0.04, cw - 0.06, ch - 0.08,
                 lbl[g], face=fc, edge=ec, lw=1.4, fs=10, pad=0.02)

    for i, g in enumerate(order_a):
        for j, h in enumerate(order_a):
            prod = mul(g, h)
            fc, ec = col_a(prod)
            cx = ox + j * cw
            cy = oy + (5 - i) * ch
            rect = plt.Rectangle((cx, cy), cw, ch, facecolor=fc, edgecolor="#888888", lw=0.8, zorder=2)
            ax_a.add_patch(rect)
            ax_a.text(cx + cw / 2, cy + ch / 2, lbl[prod], ha="center", va="center", fontsize=9.8, color=DARK, zorder=3)

    for k in (0, 3, 6):
        ax_a.plot([ox + k * cw, ox + k * cw], [oy, oy + 6 * ch], color=DARK, lw=2.6, zorder=5)
        ax_a.plot([ox, ox + 6 * cw], [oy + k * ch, oy + k * ch], color=DARK, lw=2.6, zorder=5)

    ax_a.text(ox + 1.5 * cw, oy + 7 * ch + 0.12, "$N = A_3$ (grey)", ha="center", va="center", fontsize=10.8, color=GREY, fontweight="bold")
    ax_a.text(ox + 4.5 * cw, oy + 7 * ch + 0.12, "$(1\\,2)N = N(1\\,2)$ (blue)", ha="center", va="center", fontsize=10.8, color=BLUE, fontweight="bold")

    ax_a.annotate("", xy=(7.15, oy + 3 * ch), xytext=(6.55, oy + 3 * ch),
                  arrowprops=dict(arrowstyle="-|>", color=DARK, lw=2.4, mutation_scale=18))
    ax_a.text(6.85, oy + 3 * ch + 0.35, "quotient\n$S_3/N$", ha="center", va="bottom", fontsize=10.5, color=DARK)

    qx, qy, qw, qh = 7.35, oy + 1.6 * ch, 0.92, 0.72
    q_labels = ["$N$", "$(1\\,2)N$"]
    q_cols = [(GREY_LIGHT, GREY), (BLUE_LIGHT, BLUE)]
    for i in range(2):
        for j in range(2):
            idx_c = (i + j) % 2
            fc, ec = q_cols[idx_c]
            rect = plt.Rectangle((qx + j * qw, qy + (1 - i) * qh), qw, qh,
                                 facecolor=fc, edgecolor=DARK, lw=2.0, zorder=2)
            ax_a.add_patch(rect)
            ax_a.text(qx + (j + 0.5) * qw, qy + (1.5 - i) * qh, q_labels[idx_c],
                      ha="center", va="center", fontsize=10.5, color=DARK, zorder=3)
    ax_a.text(qx + qw, qy + 2 * qh + 0.30, "solid $3\\times 3$ blocks", ha="center", va="center", fontsize=10.8, color=DARK)
    ax_a.text(qx + qw, qy - 0.35, "$(aN)(bN) = (ab)N$", ha="center", va="center", fontsize=10.8, color=BLUE)

    ax_a.set_xlim(0.0, 9.4)
    ax_a.set_ylim(0.0, 4.75)
    ax_a.axis("off")
    ax_a.set_title("(a) Normal subgroup $N = A_3 = \\{e, (1\\,2\\,3), (1\\,3\\,2)\\}$: left and right cosets agree",
                   fontsize=12.5, pad=4)

    # --- Panel (b): Non-normal subgroup H = {e, (1 2)} ---
    order_b = [e, s12, r1, s23, r2, s13]
    H0 = {e, s12}
    H1 = {r1, s23}
    H2 = {r2, s13}

    def col_b(g):
        if g in H0:
            return (GREY_LIGHT, GREY)
        if g in H1:
            return (BLUE_LIGHT, BLUE)
        return (ORANGE_LIGHT, ORANGE)

    # Raised coset strip so it has clean whitespace above the column headers
    sy = 4.42
    ax_b.text(0.15, sy + 0.58, "Left $gH$:", ha="left", va="center", fontsize=10.5, color=DARK, fontweight="bold")
    ax_b.text(0.15, sy + 0.04, "Right $Hg$:", ha="left", va="center", fontsize=10.5, color=DARK, fontweight="bold")

    left_boxes = [
        ("$eH = \\{e, (1\\,2)\\}$", GREY_LIGHT, GREY),
        ("$(1\\,2\\,3)H = \\{(1\\,2\\,3), (2\\,3)\\}$", BLUE_LIGHT, BLUE),
        ("$(1\\,3\\,2)H = \\{(1\\,3\\,2), (1\\,3)\\}$", ORANGE_LIGHT, ORANGE),
    ]
    right_boxes = [
        ("$He = \\{e, (1\\,2)\\}$", GREY_LIGHT, GREY),
        ("$H(1\\,2\\,3) = \\{(1\\,2\\,3), (1\\,3)\\}$", "#f7f7f7", DARK),
        ("$H(1\\,3\\,2) = \\{(1\\,3\\,2), (2\\,3)\\}$", "#f7f7f7", DARK),
    ]
    bx_positions = [1.25, 3.55, 6.45]
    bx_widths = [2.1, 2.7, 2.7]
    for k in range(3):
        txt_l, fc_l, ec_l = left_boxes[k]
        draw_box(ax_b, bx_positions[k], sy + 0.39, bx_widths[k], 0.38, txt_l,
                 face=fc_l, edge=ec_l, lw=1.6, fs=9.8, pad=0.02)
        txt_r, fc_r, ec_r = right_boxes[k]
        ls_r = "-" if k == 0 else "--"
        draw_box(ax_b, bx_positions[k], sy - 0.15, bx_widths[k], 0.38, txt_r,
                 face=fc_r, edge=ec_r, lw=1.5, ls=ls_r, fs=9.8, pad=0.02)

    oy_b = 0.15
    ax_b.text(ox - 0.55, oy_b + 6 * ch + 0.24, "$g \\cdot h$", ha="center", va="center", fontsize=11, fontweight="bold")
    for idx, g in enumerate(order_b):
        fc, ec = col_b(g)
        draw_box(ax_b, ox + idx * cw + 0.03, oy_b + 6 * ch + 0.05, cw - 0.06, ch - 0.10,
                 lbl[g], face=fc, edge=ec, lw=1.4, fs=10, pad=0.02)
        r_y = oy_b + (5 - idx) * ch
        draw_box(ax_b, ox - cw - 0.06, r_y + 0.04, cw - 0.06, ch - 0.10,
                 lbl[g], face=fc, edge=ec, lw=1.4, fs=10, pad=0.02)

    for i, g in enumerate(order_b):
        for j, h in enumerate(order_b):
            prod = mul(g, h)
            fc, ec = col_b(prod)
            cx = ox + j * cw
            cy = oy_b + (5 - i) * ch
            rect = plt.Rectangle((cx, cy), cw, ch, facecolor=fc, edgecolor="#888888", lw=0.8, zorder=2)
            ax_b.add_patch(rect)
            ax_b.text(cx + cw / 2, cy + ch / 2, lbl[prod], ha="center", va="center", fontsize=9.8, color=DARK, zorder=3)

    for k in (0, 2, 4, 6):
        ax_b.plot([ox + k * cw, ox + k * cw], [oy_b, oy_b + 6 * ch], color=DARK, lw=2.6, zorder=5)
        ax_b.plot([ox, ox + 6 * cw], [oy_b + k * ch, oy_b + k * ch], color=DARK, lw=2.6, zorder=5)

    ax_b.annotate("", xy=(ox + 4.0 * cw, oy_b + 5.0 * ch), xytext=(6.85, oy_b + 4.5 * ch),
                  arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2, mutation_scale=16))
    draw_box(ax_b, 6.75, oy_b + 1.5 * ch, 2.45, 2.7 * ch,
             "split $2\\times 2$ blocks:\n$eH \\cdot (1\\,2\\,3)H$ lands\nhalf in $(1\\,2\\,3)H$ (blue)\nand half in $(1\\,3\\,2)H$\n(orange)",
             face="white", edge=ORANGE, lw=1.8, fs=10.2, pad=0.05)

    ax_b.set_xlim(0.0, 9.4)
    ax_b.set_ylim(0.0, 5.45)
    ax_b.axis("off")
    ax_b.set_title("(b) Non-normal subgroup $H = \\{e, (1\\,2)\\}$: $gH \\neq Hg$ and coset blocks shatter",
                   fontsize=12.5, pad=4)

    fig.savefig(os.path.join(out, "maths2_s3_cosets_normality.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 4 (P4): Conjugacy classes and the class equation (D_8 and A_4)
# =========================================================================
def fig4_class_equation(out):
    fig = plt.figure(figsize=(8.6, 7.2))
    ax_a = fig.add_axes([0.04, 0.58, 0.92, 0.36])
    ax_b = fig.add_axes([0.04, 0.04, 0.92, 0.48])

    # --- Panel (a): D_8 (8 = 1 + 1 + 2 + 2 + 2) ---
    d8_tiles = [
        (0.0, 1.08, "$\\{e\\}$", "size $1$\n$|C_{D_8}(x)|=8$", GREY_LIGHT, GREY),
        (1.13, 1.08, "$\\{r^2\\}$", "size $1$\n$|C_{D_8}(x)|=8$", GREY_LIGHT, GREY),
        (2.45, 2.0, "$\\{r,\\, r^3\\}$", "size $2$, $|C_{D_8}(x)|=4$\n($90^\\circ$ rotations)", BLUE_LIGHT, BLUE),
        (4.58, 2.0, "$\\{s_x,\\, s_y\\}$", "size $2$, $|C_{D_8}(x)|=4$\n(axis flips)", ORANGE_LIGHT, ORANGE),
        (6.71, 2.0, "$\\{d_1,\\, d_2\\}$", "size $2$, $|C_{D_8}(x)|=4$\n(diagonal flips)", GREEN_LIGHT, GREEN),
    ]
    z_box = FancyBboxPatch((-0.10, 0.18), 2.41, 1.38, boxstyle="round,pad=0.06",
                           facecolor="none", edgecolor=DARK, lw=2.0, ls="--", zorder=4)
    ax_a.add_patch(z_box)
    # Left-aligned at x = -0.10 so it never clips on the left margin
    ax_a.text(-0.10, 1.78, "center $Z(D_8) = \\{e, r^2\\}$ (two singletons)",
              ha="left", va="center", fontsize=11, color=DARK, fontweight="bold")

    for x, w, title_t, sub_t, fc, ec in d8_tiles:
        draw_box(ax_a, x, 0.30, w, 1.12, "", face=fc, edge=ec, lw=2.0, pad=0.03, zorder=2)
        ax_a.text(x + w / 2, 1.04, title_t, ha="center", va="center", fontsize=11.5, color=DARK, zorder=3)
        ax_a.text(x + w / 2, 0.57, sub_t, ha="center", va="center", fontsize=9.4, color=DARK, zorder=3)

    ax_a.text(4.35, -0.12, "Every tile satisfies $|Cl(x)| \\times |C_{D_8}(x)| = 8$",
              ha="center", va="center", fontsize=11, color=DARK)
    ax_a.set_xlim(-0.3, 8.95)
    ax_a.set_ylim(-0.35, 2.05)
    ax_a.axis("off")
    ax_a.set_title("(a) $D_8$ (order $8$): class equation $8 = 1 + 1 + 2 + 2 + 2$", fontsize=12.5, pad=4)

    # --- Panel (b): A_4 (12 = 1 + 3 + 4 + 4) ---
    a4_tiles = [
        (0.0, 1.35, "$C_1$ (size $1$)", "$|C_{A_4}(x)|=12$\n\n$e$", GREY_LIGHT, GREY),
        (1.50, 2.30, "$C_2$ (size $3$, $|C_{A_4}(x)|=4$)", "$(1\\,2)(3\\,4)$\n$(1\\,3)(2\\,4)$\n$(1\\,4)(2\\,3)$", BLUE_LIGHT, BLUE),
        (3.95, 2.30, "$C_3$ (size $4$, $|C_{A_4}(x)|=3$)", "$(1\\,2\\,3),\\; (1\\,4\\,2)$\n$(1\\,3\\,4),\\; (2\\,4\\,3)$", ORANGE_LIGHT, ORANGE),
        (6.40, 2.30, "$C_4$ (size $4$, $|C_{A_4}(x)|=3$)", "$(1\\,3\\,2),\\; (1\\,2\\,4)$\n$(1\\,4\\,3),\\; (2\\,3\\,4)$", GREEN_LIGHT, GREEN),
    ]
    for x, w, head_t, body_t, fc, ec in a4_tiles:
        draw_box(ax_b, x, 1.85, w, 1.45, "", face=fc, edge=ec, lw=2.0, pad=0.03, zorder=2)
        ax_b.text(x + w / 2, 3.02, head_t, ha="center", va="center", fontsize=10.2, color=ec, fontweight="bold", zorder=3)
        ax_b.text(x + w / 2, 2.32, body_t, ha="center", va="center", fontsize=10.0, color=DARK, zorder=3)

    ax_b.text(0.0, 1.42, "Candidate normal subgroups (unions of whole tiles with $C_1$, order must divide $12$):",
              ha="left", va="center", fontsize=10.8, color=DARK, fontweight="bold")

    bars = [
        (0.95, "$C_1 \\cup C_2$: size $1 + 3 = 4 \\mid 12$", "normal subgroup $V_4 \\trianglelefteq A_4$", BLUE_LIGHT, BLUE, True),
        (0.48, "two tiles ($C_1 \\cup C_3$ or $C_1 \\cup C_4$): size $1 + 4 = 5 \\nmid 12$", "does not divide $12$", GREY_LIGHT, GREY, False),
        (0.01, "three tiles: $1 + 3 + 4 = 8$ or $1 + 4 + 4 = 9$, neither divides $12$", "does not divide $12$", GREY_LIGHT, GREY, False),
    ]
    for y_b, left_t, right_t, fc, ec, ok in bars:
        draw_box(ax_b, 0.0, y_b, 5.65, 0.36, "", face=fc, edge=ec, lw=1.8 if ok else 1.2, pad=0.02, zorder=2)
        ax_b.text(0.15, y_b + 0.18, left_t, ha="left", va="center", fontsize=10.2, color=DARK, zorder=3)
        ax_b.text(5.85, y_b + 0.18, right_t, ha="left", va="center", fontsize=10.5,
                  color=BLUE if ok else GREY, fontweight="bold" if ok else "normal")

    ax_b.set_xlim(-0.2, 8.95)
    ax_b.set_ylim(-0.15, 3.55)
    ax_b.axis("off")
    ax_b.set_title("(b) $A_4$ (order $12$): class equation $12 = 1 + 3 + 4 + 4$ and whole-tile test",
                   fontsize=12.5, pad=4)

    fig.savefig(os.path.join(out, "maths2_class_equation.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 5 (P5): Fibration and Fourth Isomorphism Theorem for D_8 over N
# =========================================================================
def fig5_fourth_isomorphism(out):
    fig = plt.figure(figsize=(8.6, 7.4))
    ax_a = fig.add_axes([0.04, 0.56, 0.92, 0.39])
    ax_b = fig.add_axes([0.04, 0.03, 0.92, 0.48])

    # --- Panel (a): Fibration 1 -> N -> D_8 -> D_8/N -> 1 ---
    fibers = [
        (1.2, "$N$", "$\\bar{e}$", "$e$", "$r^2$", GREY_LIGHT, GREY),
        (3.2, "$rN$", "$\\bar{r}$", "$r$", "$r^3$", BLUE_LIGHT, BLUE),
        (5.2, "$s_x N$", "$\\bar{s}$", "$s_x$", "$s_y$", ORANGE_LIGHT, ORANGE),
        (7.2, "$d_1 N$", "$\\bar{d}$", "$d_1$", "$d_2$", GREEN_LIGHT, GREEN),
    ]
    ax_a.plot([0.6, 7.8], [0.45, 0.45], color=DARK, lw=2.8, zorder=1)
    ax_a.text(0.4, 0.45, "spine\n$D_8/N$", ha="right", va="center", fontsize=11, color=DARK)
    ax_a.text(0.4, 1.95, "fibers\nin $D_8$", ha="right", va="center", fontsize=11, color=DARK)

    for x, cos_lbl, base_lbl, top_el, bot_el, fc, ec in fibers:
        draw_box(ax_a, x - 0.48, 1.25, 0.96, 1.35, "", face=fc, edge=ec, lw=1.8, pad=0.05, zorder=2)
        draw_node(ax_a, x, 2.25, top_el, r=0.24, face="white", edge=ec, fs=11, lw=1.8, zorder=3)
        draw_node(ax_a, x, 1.58, bot_el, r=0.24, face="white", edge=ec, fs=11, lw=1.8, zorder=3)
        ax_a.text(x, 2.82, cos_lbl, ha="center", va="center", fontsize=11, color=ec, fontweight="bold")
        ax_a.annotate("", xy=(x, 0.74), xytext=(x, 1.18),
                      arrowprops=dict(arrowstyle="-|>", color=DARK, lw=1.8, mutation_scale=15))
        draw_node(ax_a, x, 0.45, base_lbl, r=0.25, face=fc, edge=ec, fs=11, lw=2.2, zorder=3)

    ax_a.text(4.2, 0.96, "$\\pi$", ha="center", va="center", fontsize=11.5, color=DARK)
    ax_a.set_xlim(-0.4, 8.3)
    ax_a.set_ylim(0.0, 3.1)
    ax_a.axis("off")
    ax_a.set_title("(a) Fibration $1 \\;\\to\\; N \\;\\hookrightarrow\\; D_8 \\;\\to\\; D_8/N \\cong V_4 \\;\\to\\; 1$ with $N = \\{e, r^2\\}$",
                   fontsize=12.5, pad=4)

    # --- Panel (b): Subgroup lattice of D_8 (10 nodes) and V_4 (5 nodes) beside it ---
    pos_d8 = {
        "D8": (2.3, 3.1),
        "V_s": (1.1, 2.15),
        "C4": (2.3, 2.15),
        "V_d": (3.5, 2.15),
        "s_x": (0.3, 1.1),
        "s_y": (1.1, 1.1),
        "N": (2.3, 1.1),
        "d_1": (3.5, 1.1),
        "d_2": (4.3, 1.1),
        "e": (2.3, 0.15),
    }
    lbl_d8 = {
        "D8": "$D_8$",
        "V_s": "$V_s$",
        "C4": "$\\langle r \\rangle$",
        "V_d": "$V_d$",
        "s_x": "$\\langle s_x \\rangle$",
        "s_y": "$\\langle s_y \\rangle$",
        "N": "$N$",
        "d_1": "$\\langle d_1 \\rangle$",
        "d_2": "$\\langle d_2 \\rangle$",
        "e": "$\\{e\\}$",
    }
    upper_nodes = {"D8", "V_s", "C4", "V_d", "N"}
    edges_d8 = [
        ("D8", "V_s"), ("D8", "C4"), ("D8", "V_d"),
        ("V_s", "N"), ("C4", "N"), ("V_d", "N"),
        ("V_s", "s_x"), ("V_s", "s_y"),
        ("V_d", "d_1"), ("V_d", "d_2"),
        ("s_x", "e"), ("s_y", "e"), ("N", "e"), ("d_1", "e"), ("d_2", "e"),
    ]
    for u, v in edges_d8:
        x1, y1 = pos_d8[u]
        x2, y2 = pos_d8[v]
        is_up = (u in upper_nodes and v in upper_nodes)
        ax_b.plot([x1, x2], [y1, y2],
                  color=BLUE if is_up else "#bbbbbb",
                  lw=2.5 if is_up else 1.4, zorder=1)

    for k, (x, y) in pos_d8.items():
        is_up = (k in upper_nodes)
        if k == "N":
            fc, ec = GREY_LIGHT, BLUE
        elif is_up:
            fc, ec = BLUE_LIGHT, BLUE
        else:
            fc, ec = "#f2f2f2", GREY
        draw_node(ax_b, x, y, lbl_d8[k], r=0.31, face=fc, edge=ec,
                  fs=10.5, lw=2.3 if is_up else 1.4, zorder=3)

    ax_b.text(2.3, 3.62, "Subgroups of $D_8$", ha="center", va="center", fontsize=11.5, color=DARK, fontweight="bold")

    ax_b.annotate("", xy=(5.55, 2.15), xytext=(4.65, 2.15),
                  arrowprops=dict(arrowstyle="<->", color=BLUE, lw=2.2, mutation_scale=16))

    pos_v4 = {
        "V4": (7.1, 3.1),
        "bs": (6.0, 2.15),
        "br": (7.1, 2.15),
        "bd": (8.2, 2.15),
        "be": (7.1, 1.1),
    }
    lbl_v4 = {
        "V4": "$V_4$",
        "bs": "$\\langle \\bar{s} \\rangle$",
        "br": "$\\langle \\bar{r} \\rangle$",
        "bd": "$\\langle \\bar{d} \\rangle$",
        "be": "$\\{\\bar{e}\\}$",
    }
    edges_v4 = [
        ("V4", "bs"), ("V4", "br"), ("V4", "bd"),
        ("bs", "be"), ("br", "be"), ("bd", "be"),
    ]
    for u, v in edges_v4:
        x1, y1 = pos_v4[u]
        x2, y2 = pos_v4[v]
        ax_b.plot([x1, x2], [y1, y2], color=BLUE, lw=2.5, zorder=1)

    for k, (x, y) in pos_v4.items():
        fc = GREY_LIGHT if k == "be" else BLUE_LIGHT
        draw_node(ax_b, x, y, lbl_v4[k], r=0.31, face=fc, edge=BLUE, fs=10.5, lw=2.3, zorder=3)

    ax_b.text(7.1, 3.62, "Subgroups of $V_4$", ha="center", va="center", fontsize=11.5, color=DARK, fontweight="bold")

    ax_b.set_xlim(-0.2, 8.8)
    ax_b.set_ylim(-0.25, 3.85)
    ax_b.axis("off")
    ax_b.set_title("(b) Subgroup correspondence: the $5$ subgroups above $N$ match the lattice of $V_4$",
                   fontsize=12.5, pad=4)

    fig.savefig(os.path.join(out, "maths2_fourth_isomorphism_fibration.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 6 (P6): Orbit-Stabilizer on the four corners of a square (D_8)
# =========================================================================
def fig6_orbit_stabilizer(out):
    # Left-to-right products (gh = first g, then h): the coset {g, (2 4)g} of
    # elements sending corner 1 to the same corner is the right coset G_1 g.
    D8, names = get_d8()
    G_0 = {g for g in D8 if g[0] == 0}
    assert G_0 == {names["e"], names["d13"]}

    fig, ax = plt.subplots(figsize=(8.8, 5.1))

    coset_rows = [
        (3.25, "$G_1 e = \\{e,\\; (2\\,4)\\}$", "send $1 \\mapsto 1$", GREY_LIGHT, GREY, 1),
        (2.20, "$G_1 r = \\{(1\\,2\\,3\\,4),\\; (1\\,2)(3\\,4)\\}$", "send $1 \\mapsto 2$", BLUE_LIGHT, BLUE, 2),
        (1.15, "$G_1 r^2 = \\{(1\\,3)(2\\,4),\\; (1\\,3)\\}$", "send $1 \\mapsto 3$", ORANGE_LIGHT, ORANGE, 3),
        (0.10, "$G_1 r^3 = \\{(1\\,4\\,3\\,2),\\; (1\\,4)(2\\,3)\\}$", "send $1 \\mapsto 4$", GREEN_LIGHT, GREEN, 4),
    ]
    ax.text(1.75, 4.30, "Right cosets $G_1 g$ ($4 \\times 2 = 8$ elements)",
            ha="center", va="center", fontsize=11.5, color=DARK, fontweight="bold")

    sq_cx, sq_cy, sq_r = 6.55, 2.0, 0.96
    corners = {
        1: (sq_cx - sq_r, sq_cy + sq_r),
        2: (sq_cx + sq_r, sq_cy + sq_r),
        3: (sq_cx + sq_r, sq_cy - sq_r),
        4: (sq_cx - sq_r, sq_cy - sq_r),
    }
    for c1, c2 in [(1, 2), (2, 3), (3, 4), (4, 1)]:
        ax.plot([corners[c1][0], corners[c2][0]], [corners[c1][1], corners[c2][1]],
                color=DARK, lw=2.4, zorder=2)
    ax.plot([corners[1][0], corners[3][0]], [corners[1][1], corners[3][1]],
            color=GREY, lw=1.8, ls="--", zorder=1)
    ax.plot([corners[2][0], corners[4][0]], [corners[2][1], corners[4][1]],
            color=BLUE, lw=1.8, ls="--", zorder=1)

    # Put stabilizer labels outside the corners where arrows don't pass
    corner_cols = {
        1: (GREY_LIGHT, GREY, "$G_1 = \\{e, (2\\,4)\\}$", (-0.15, 0.56)),
        2: (BLUE_LIGHT, BLUE, "$G_2 = \\{e, (1\\,3)\\}$", (0.28, 0.56)),
        3: (ORANGE_LIGHT, ORANGE, "$G_3 = \\{e, (2\\,4)\\}$", (0.28, -0.58)),
        4: (GREEN_LIGHT, GREEN, "$G_4 = \\{e, (1\\,3)\\}$", (-0.15, -0.58)),
    }
    for c_idx, (cx, cy) in corners.items():
        fc, ec, stab_t, (dx, dy) = corner_cols[c_idx]
        draw_node(ax, cx, cy, f"${c_idx}$", r=0.24, face=fc, edge=ec, fs=12, lw=2.3, zorder=4)
        ax.text(cx + dx, cy + dy, stab_t, ha="center", va="center", fontsize=10.2, color=ec, fontweight="bold")

    ax.text(sq_cx, 4.30, "Orbit $\\Omega = \\{1, 2, 3, 4\\}$ and stabilizers $G_\\beta = g^{-1} G_1 g$",
            ha="center", va="center", fontsize=11.5, color=DARK, fontweight="bold")

    # Route arrows cleanly through the open gap between corners 1 and 4
    arrow_specs = {
        1: (corners[1][0] - 0.22, corners[1][1] + 0.10, -0.10),
        2: (corners[2][0] - 0.22, corners[2][1] - 0.12, 0.16),
        3: (corners[3][0] - 0.22, corners[3][1] + 0.12, -0.16),
        4: (corners[4][0] - 0.22, corners[4][1] - 0.10, 0.10),
    }
    for y_box, box_lbl, act_lbl, fc, ec, target in coset_rows:
        draw_box(ax, 0.1, y_box, 3.3, 0.68, "", face=fc, edge=ec, lw=2.0, pad=0.03, zorder=2)
        ax.text(1.75, y_box + 0.45, box_lbl, ha="center", va="center", fontsize=10.8, color=DARK, zorder=3)
        ax.text(1.75, y_box + 0.18, act_lbl, ha="center", va="center", fontsize=9.8, color=ec, zorder=3)

        tx, ty, rad_v = arrow_specs[target]
        arr = FancyArrowPatch((3.48, y_box + 0.34), (tx, ty),
                              connectionstyle=f"arc3,rad={rad_v}",
                              arrowstyle="-|>", color=ec, lw=2.1,
                              shrinkA=4, shrinkB=4, mutation_scale=15, zorder=3)
        ax.add_patch(arr)

    ax.set_xlim(-0.1, 8.75)
    ax.set_ylim(-0.2, 4.55)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths2_orbit_stabilizer_square.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 7 (P7): Pipeline from action on Omega to primitivity verdict
# =========================================================================
def fig7_orbitals_pipeline(out):
    fig, ax = plt.subplots(figsize=(8.6, 12.2))

    xL, xM, xR = 2.25, 4.4, 6.55

    # Column headers at top
    draw_box(ax, 0.35, 11.55, 3.8, 0.45, "$D_8$ on square $\\Omega = \\{1, 2, 3, 4\\}$ (order $8$)",
             face=GREY_LIGHT, edge=DARK, lw=1.8, fs=11, weight="bold", pad=0.03)
    draw_box(ax, 4.65, 11.55, 3.8, 0.45, "$S_4$ on $\\Omega = \\{1, 2, 3, 4\\}$ (order $24$)",
             face=GREY_LIGHT, edge=DARK, lw=1.8, fs=11, weight="bold", pad=0.03)

    def mini_square(cx, cy, r, edges_list, node_colors=None, title_txt=None, title_dy=-0.38):
        c_pos = {
            1: (cx - r, cy + r),
            2: (cx + r, cy + r),
            3: (cx + r, cy - r),
            4: (cx - r, cy - r),
        }
        for u, v, col, lw, ls in edges_list:
            ax.plot([c_pos[u][0], c_pos[v][0]], [c_pos[u][1], c_pos[v][1]],
                    color=col, lw=lw, ls=ls, zorder=2)
        for idx in (1, 2, 3, 4):
            fc, ec = node_colors[idx] if node_colors else ("white", DARK)
            draw_node(ax, c_pos[idx][0], c_pos[idx][1], f"${idx}$", r=0.16, face=fc, edge=ec, fs=10, lw=1.8, zorder=4)
        if title_txt:
            ax.text(cx, cy - r + title_dy, title_txt, ha="center", va="center", fontsize=10, color=DARK)
        return c_pos

    # Stage headers with ample vertical spacing
    stage_ys = [11.08, 9.02, 5.82, 3.72, 1.15]
    stage_titles = [
        "1. Action of $G$ on $\\Omega$",
        "2. Orbits on pairs $\\Omega \\times \\Omega$ = orbitals $\\Gamma_i$",
        "3. Fix $\\alpha = 1$: row slice = sub-orbits $\\Gamma_i(1)$",
        "4. Draw each non-trivial orbital as an orbital graph",
        "5. Verdict: disconnected islands vs all connected",
    ]
    for sy, st in zip(stage_ys, stage_titles):
        draw_box(ax, 1.35, sy - 0.17, 6.1, 0.34, st,
                 face="#f5f7fa", edge=BLUE, lw=1.5, fs=10.8, weight="bold", pad=0.02, zorder=3)

    arrow_spans = [
        (9.58, 9.25),
        (6.38, 6.05),
        (4.28, 3.95),
        (1.72, 1.38),
    ]
    for y_top, y_bot in arrow_spans:
        ax.annotate("", xy=(xM, y_bot), xytext=(xM, y_top),
                    arrowprops=dict(arrowstyle="-|>", color=DARK, lw=2.2, mutation_scale=16))

    # --- STAGE 1: Action on Omega ---
    sq_e_d8 = [(1, 2, BLUE, 2.0, "-"), (2, 3, BLUE, 2.0, "-"),
               (3, 4, BLUE, 2.0, "-"), (4, 1, BLUE, 2.0, "-")]
    mini_square(xL, 10.22, 0.38, sq_e_d8, title_txt="rotations and flips preserve square")

    sq_e_s4 = [(u, v, BLUE, 1.8, "-") for u, v in it.combinations([1, 2, 3, 4], 2)]
    mini_square(xR, 10.22, 0.38, sq_e_s4, title_txt="all $24$ permutations of corners")

    # --- STAGE 2: Pairs Omega x Omega and orbitals ---
    def draw_pair_grid(gx, gy, is_d8):
        cs = 0.48
        for i in range(4):
            for j in range(4):
                a, b = i + 1, j + 1
                if a == b:
                    fc, ec = GREY_LIGHT, GREY
                elif not is_d8 or abs(a - b) in (1, 3):
                    fc, ec = BLUE_LIGHT, BLUE
                else:
                    fc, ec = ORANGE_LIGHT, ORANGE
                cx = gx + j * cs
                cy = gy + (3 - i) * cs
                rect = plt.Rectangle((cx, cy), cs, cs, facecolor=fc, edgecolor=ec, lw=1.2, zorder=2)
                ax.add_patch(rect)
                ax.text(cx + cs / 2, cy + cs / 2, f"$({a},{b})$", ha="center", va="center", fontsize=9.2, color=DARK, zorder=3)
        row_rect = plt.Rectangle((gx - 0.03, gy + 3 * cs - 0.03), 4 * cs + 0.06, cs + 0.06,
                                 fill=False, edgecolor=DARK, lw=2.6, zorder=5)
        ax.add_patch(row_rect)
        ax.text(gx - 0.12, gy + 3.5 * cs, "row $\\alpha=1$", ha="right", va="center", fontsize=9.8, color=DARK, fontweight="bold")

    draw_pair_grid(1.40, 6.75, is_d8=True)
    ax.text(xL, 6.48, "rank $3$: $\\Gamma_0$ (grey), $\\Gamma_1$ (blue), $\\Gamma_2$ (orange)",
            ha="center", va="center", fontsize=9.8, color=DARK)

    draw_pair_grid(5.70, 6.75, is_d8=False)
    ax.text(xR, 6.48, "rank $2$: $\\Gamma_0$ (grey), $\\Gamma_1$ (blue)",
            ha="center", va="center", fontsize=9.8, color=DARK)

    # --- STAGE 3: Sub-orbits as a row slice (fix alpha = 1) ---
    draw_box(ax, 0.45, 4.98, 0.95, 0.42, "$\\{1\\}$", face=GREY_LIGHT, edge=GREY, lw=1.8, fs=10.5)
    draw_box(ax, 1.55, 4.98, 1.35, 0.42, "$\\{2,\\, 4\\}$", face=BLUE_LIGHT, edge=BLUE, lw=1.8, fs=10.5)
    draw_box(ax, 3.05, 4.98, 0.95, 0.42, "$\\{3\\}$", face=ORANGE_LIGHT, edge=ORANGE, lw=1.8, fs=10.5)
    ax.text(xL, 4.58, "$3$ sub-orbits of $G_1 = \\{e, (2\\,4)\\}$", ha="center", va="center", fontsize=10, color=DARK)

    draw_box(ax, 4.95, 4.98, 1.05, 0.42, "$\\{1\\}$", face=GREY_LIGHT, edge=GREY, lw=1.8, fs=10.5)
    draw_box(ax, 6.18, 4.98, 1.95, 0.42, "$\\{2,\\, 3,\\, 4\\}$", face=BLUE_LIGHT, edge=BLUE, lw=1.8, fs=10.5)
    ax.text(xR, 4.58, "$2$ sub-orbits of $G_1 \\cong S_3$", ha="center", va="center", fontsize=10, color=DARK)

    # --- STAGE 4: Orbital graphs ---
    blue_cols = {i: (BLUE_LIGHT, BLUE) for i in (1, 2, 3, 4)}
    sq_e_d8_blue = [(1, 2, BLUE, 2.8, "-"), (2, 3, BLUE, 2.8, "-"),
                    (3, 4, BLUE, 2.8, "-"), (4, 1, BLUE, 2.8, "-")]
    mini_square(1.25, 2.75, 0.38, sq_e_d8_blue, node_colors=blue_cols,
                title_txt="$\\Gamma_1$: connected $C_4$", title_dy=-0.42)
    diag_edges = [(1, 3, ORANGE, 2.8, "-"), (2, 4, ORANGE, 2.8, "-")]
    diag_cols = {1: (ORANGE_LIGHT, ORANGE), 3: (ORANGE_LIGHT, ORANGE),
                 2: (ORANGE_LIGHT, ORANGE), 4: (ORANGE_LIGHT, ORANGE)}
    mini_square(3.25, 2.75, 0.38, diag_edges, node_colors=diag_cols,
                title_txt="$\\Gamma_2$: two islands\n$\\{1,3\\}$ and $\\{2,4\\}$", title_dy=-0.46)

    mini_square(xR, 2.75, 0.38, sq_e_s4, node_colors=blue_cols,
                title_txt="$\\Gamma_1 = K_4$: connected", title_dy=-0.42)

    # --- STAGE 5: Primitive or imprimitive verdict ---
    draw_box(ax, 0.35, 0.12, 3.8, 0.72,
             "Imprimitive: $\\Gamma_2$ is disconnected,\ngiving blocks $\\{1, 3\\}$ and $\\{2, 4\\}$",
             face=ORANGE_LIGHT, edge=ORANGE, lw=2.2, fs=10.5, weight="bold", pad=0.03)
    draw_box(ax, 4.65, 0.12, 3.8, 0.72,
             "Primitive: all non-trivial orbital\ngraphs are connected (no blocks)",
             face=BLUE_LIGHT, edge=BLUE, lw=2.2, fs=10.5, weight="bold", pad=0.03)

    ax.set_xlim(0.0, 8.8)
    ax.set_ylim(0.0, 12.15)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths2_orbitals_blocks_primitivity.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 8 (P8): Submodule, non-invariant complement, and quotient V/W
# =========================================================================
def fig8_subspace_quotient_shear(out):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8.8, 4.4))

    # --- Left panel (a): Complementary subspace U spills into W ---
    ax1.axhline(0, color=BLUE, lw=3.0, zorder=2)
    ax1.axvline(0, color=GREY, lw=2.0, ls="--", zorder=1)
    ax1.plot([-0.6, 1.8], [-0.6, 1.8], color=ORANGE, lw=1.6, ls=":", zorder=1)

    ax1.annotate("", xy=(1.0, 0.0), xytext=(0.0, 0.0),
                 arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.6, mutation_scale=16), zorder=4)
    ax1.text(1.0, -0.25, "$w = (1,0) \\in W$", ha="center", va="center", fontsize=10.5, color=BLUE, fontweight="bold")
    ax1.text(-0.55, -0.22, "$W$ ($x$-axis)", ha="center", va="center", fontsize=10.5, color=BLUE)

    ax1.annotate("", xy=(0.0, 1.0), xytext=(0.0, 0.0),
                 arrowprops=dict(arrowstyle="-|>", color=GREY, lw=2.4, mutation_scale=16), zorder=4)
    ax1.text(-0.52, 1.02, "$u = (0,1)$", ha="center", va="center", fontsize=10.5, color=DARK)
    ax1.text(-0.42, 1.62, "$U$ ($y$-axis)", ha="center", va="center", fontsize=10.5, color=GREY)

    ax1.annotate("", xy=(1.0, 1.0), xytext=(0.0, 0.0),
                 arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.8, mutation_scale=17), zorder=5)
    # Placed cleanly to the right of (1, 1) below the dotted y=x line
    ax1.text(1.08, 0.85, "$ug = (1,1) \\notin U$", ha="left", va="center", fontsize=10.8, color=ORANGE, fontweight="bold")

    ax1.annotate("", xy=(0.98, 1.0), xytext=(0.04, 1.0),
                 arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2, ls="--", mutation_scale=15), zorder=4)
    ax1.text(0.48, 1.24, "spillover $Y_g = (1)$", ha="center", va="center", fontsize=10.2, color=ORANGE)
    ax1.plot([1.0, 1.0], [0.0, 1.0], color=GREY, lw=1.2, ls=":", zorder=1)

    ax1.set_xlim(-1.0, 2.85)
    ax1.set_ylim(-0.65, 2.15)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("(a) Subspace $U$ spills into $W$ ($Y_g \\neq 0$)", fontsize=12.5, pad=6)

    # --- Right panel (b): Quotient space V/W slides coset lines ---
    y_levels = [-0.5, 0.0, 1.0, 1.6]
    for yl in y_levels:
        is_w = (yl == 0.0)
        is_u = (yl == 1.0)
        col = BLUE if (is_w or is_u) else "#99b3d6"
        lw = 3.0 if is_w else (2.4 if is_u else 1.5)
        ax2.plot([-0.9, 1.50], [yl, yl], color=col, lw=lw, zorder=2)

    for x_start in (-0.6, 0.32):
        ax2.annotate("", xy=(x_start + 0.72, 1.0), xytext=(x_start, 1.0),
                     arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2, mutation_scale=15), zorder=4)
    ax2.text(0.30, 1.25, "$(u + W)g = u + W$", ha="center", va="center", fontsize=10.5, color=BLUE, fontweight="bold")
    ax2.text(0.30, -0.25, "$0_{V/W} = W$", ha="center", va="center", fontsize=10.5, color=BLUE, fontweight="bold")

    qx = 2.08
    ax2.plot([qx, qx], [-0.6, 1.8], color=DARK, lw=2.2, zorder=2)
    ax2.text(qx, 1.98, "$V/W$", ha="center", va="center", fontsize=11.5, color=DARK, fontweight="bold")
    for yl, lbl_q in [(0.0, "$W$"), (1.0, "$u+W$")]:
        ax2.annotate("", xy=(qx - 0.14, yl), xytext=(1.55, yl),
                     arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.5, mutation_scale=13))
        draw_node(ax2, qx, yl, r=0.10, face=BLUE_LIGHT if yl == 1.0 else GREY_LIGHT, edge=BLUE, lw=2.0, zorder=4)
        ax2.text(qx + 0.18, yl, lbl_q, ha="left", va="center", fontsize=10.5, color=DARK)

    ax2.set_xlim(-1.0, 2.85)
    ax2.set_ylim(-0.65, 2.15)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("(b) Quotient $V/W$: coset lines map to themselves", fontsize=12.5, pad=6)

    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths2_subspace_quotient_shear.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 9 (P9): Coherent configuration and intersection algebra on pentagon (D_10)
# =========================================================================
def fig9_coherent_pentagon(out):
    n = 5
    A0 = np.eye(n, dtype=int)
    A1 = np.zeros((n, n), dtype=int)
    A2 = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            d = min((i - j) % n, (j - i) % n)
            if d == 1:
                A1[i, j] = 1
            elif d == 2:
                A2[i, j] = 1
    assert np.array_equal(A0 + A1 + A2, np.ones((n, n), dtype=int))
    P1 = np.array([[0, 2, 0], [1, 0, 1], [0, 1, 1]], dtype=int)
    assert np.array_equal(A1 @ A1, 2 * A0 + 0 * A1 + 1 * A2)
    assert np.array_equal(A1 @ A2, 0 * A0 + 1 * A1 + 1 * A2)

    fig = plt.figure(figsize=(8.6, 7.2))
    ax_a = fig.add_axes([0.03, 0.48, 0.94, 0.47])
    ax_b = fig.add_axes([0.03, 0.03, 0.94, 0.41])

    # --- Panel (a): Pentagon under D_10 and 5x5 matrix J_5 = A_0 + A_1 + A_2 ---
    cx, cy, rad = 1.65, 1.35, 1.15
    pts5 = {}
    for k in range(5):
        ang = np.pi / 2 - 2 * np.pi * k / 5
        pts5[k + 1] = (cx + rad * np.cos(ang), cy + rad * np.sin(ang))

    for i in range(1, 6):
        j = ((i + 1) % 5) + 1
        ax_a.plot([pts5[i][0], pts5[j][0]], [pts5[i][1], pts5[j][1]],
                  color=ORANGE, lw=2.0, ls="--", zorder=1)

    for i in range(1, 6):
        j = (i % 5) + 1
        is_hl = (i in (1, 2) and j in (2, 3))
        ax_a.plot([pts5[i][0], pts5[j][0]], [pts5[i][1], pts5[j][1]],
                  color=BLUE, lw=3.4 if is_hl else 2.2, zorder=2)

    for k in range(1, 6):
        x, y = pts5[k]
        draw_node(ax_a, x, y, f"${k}$", r=0.22, face=GREY_LIGHT, edge=DARK, fs=11, lw=2.0, zorder=4)

    ax_a.text(cx, -0.10, "path $1 \\;\\to\\; 2 \\;\\to\\; 3$ gives $p_{11}^2 = 1$",
              ha="center", va="center", fontsize=10.5, color=DARK)

    gx, gy, cs = 4.65, 0.20, 0.46
    for i in range(5):
        ax_a.text(gx - 0.22, gy + (4.5 - i) * cs, f"${i+1}$", ha="center", va="center", fontsize=10, color=GREY)
        ax_a.text(gx + (i + 0.5) * cs, gy + 5 * cs + 0.20, f"${i+1}$", ha="center", va="center", fontsize=10, color=GREY)
        for j in range(5):
            if A0[i, j]:
                fc, ec, txt = GREY_LIGHT, GREY, "$A_0$"
            elif A1[i, j]:
                fc, ec, txt = BLUE_LIGHT, BLUE, "$A_1$"
            else:
                fc, ec, txt = ORANGE_LIGHT, ORANGE, "$A_2$"
            rect = plt.Rectangle((gx + j * cs, gy + (4 - i) * cs), cs, cs,
                                 facecolor=fc, edgecolor=ec, lw=1.3, zorder=2)
            ax_a.add_patch(rect)
            ax_a.text(gx + (j + 0.5) * cs, gy + (4.5 - i) * cs, txt,
                      ha="center", va="center", fontsize=9.5, color=DARK, zorder=3)

    ax_a.text(gx + 2.5 * cs, -0.10, "$J_5 = A_0$ (grey) $+\\; A_1$ (blue) $+\\; A_2$ (orange)",
              ha="center", va="center", fontsize=10.5, color=DARK)

    ax_a.set_xlim(0.0, 8.2)
    ax_a.set_ylim(-0.32, 2.85)
    ax_a.set_aspect("equal")
    ax_a.axis("off")
    ax_a.set_title("(a) Regular pentagon under $D_{10}$ ($n = 5$, rank $r = 3$) and $5 \\times 5$ partition",
                   fontsize=12.5, pad=4)

    # --- Panel (b): Compression to 3x3 intersection matrix P_1 ---
    eq_lines = [
        (1.85, "Col $0$:  $A_1 A_0 = \\mathbf{0}\\,A_0 + \\mathbf{1}\\,A_1 + \\mathbf{0}\\,A_2$"),
        (1.15, "Col $1$:  $A_1 A_1 = \\mathbf{2}\\,A_0 + \\mathbf{0}\\,A_1 + \\mathbf{1}\\,A_2$"),
        (0.45, "Col $2$:  $A_1 A_2 = \\mathbf{0}\\,A_0 + \\mathbf{1}\\,A_1 + \\mathbf{1}\\,A_2$"),
    ]
    for y_eq, t_eq in eq_lines:
        draw_box(ax_b, 0.10, y_eq - 0.24, 3.75, 0.48, t_eq,
                 face="#f8f9fb", edge="#cccccc", lw=1.4, fs=10.8, pad=0.03)

    # Arrow ends at x = 4.78, well before k=1 label at x = 5.25
    ax_b.annotate("", xy=(4.78, 1.15), xytext=(4.02, 1.15),
                  arrowprops=dict(arrowstyle="-|>", color=DARK, lw=2.2, mutation_scale=16))
    ax_b.text(4.40, 1.48, "$(P_1)_{kj} = p_{1j}^k$", ha="center", va="center", fontsize=10.5, color=DARK)

    px, py, pcs = 5.70, 0.30, 0.58
    row_cols = [(GREY_LIGHT, GREY, "$k=0$"), (BLUE_LIGHT, BLUE, "$k=1$"), (ORANGE_LIGHT, ORANGE, "$k=2$")]
    for k in range(3):
        fc, ec, r_lbl = row_cols[k]
        ax_b.text(px - 0.42, py + (2.5 - k) * pcs, r_lbl, ha="center", va="center", fontsize=10, color=ec, fontweight="bold")
        ax_b.text(px + (k + 0.5) * pcs, py + 3 * pcs + 0.22, f"$j={k}$", ha="center", va="center", fontsize=10, color=ec, fontweight="bold")
        for j in range(3):
            rect = plt.Rectangle((px + j * pcs, py + (2 - k) * pcs), pcs, pcs,
                                 facecolor=fc, edgecolor=ec, lw=1.6, zorder=2)
            ax_b.add_patch(rect)
            ax_b.text(px + (j + 0.5) * pcs, py + (2.5 - k) * pcs, f"${P1[k, j]}$",
                      ha="center", va="center", fontsize=12, color=DARK, fontweight="bold", zorder=3)

    ax_b.text(px + 1.5 * pcs, 0.0, "$P_1$ ($3 \\times 3$) keeps eigenvalues $\\{2, \\frac{-1\\pm\\sqrt{5}}{2}\\}$ of $A_1$",
              ha="center", va="center", fontsize=10.2, color=DARK)

    ax_b.set_xlim(0.0, 8.3)
    ax_b.set_ylim(-0.22, 2.45)
    ax_b.set_aspect("equal")
    ax_b.axis("off")
    ax_b.set_title("(b) Left multiplication by $A_1$ compressed to the $3 \\times 3$ intersection matrix $P_1$",
                   fontsize=12.5, pad=4)

    fig.savefig(os.path.join(out, "maths2_coherent_intersection_pentagon.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure 10 (P10): Extensions - action phi_b and factor set f(b_1, b_2)
# =========================================================================
def fig10_extensions_mortar(out):
    fig = plt.figure(figsize=(8.6, 7.3))
    ax_a = fig.add_axes([0.03, 0.52, 0.45, 0.43])
    ax_b = fig.add_axes([0.52, 0.52, 0.45, 0.43])
    ax_c = fig.add_axes([0.08, 0.03, 0.84, 0.43])

    def draw_two_layers(ax, is_twisted):
        bot_pts = [(0.0, 0.35), (1.3, 0.0), (2.2, 0.55), (0.9, 0.90)]
        top_pts = [(x, y + 1.45) for (x, y) in bot_pts]
        bot_lbls = ["$1$", "$r$", "$r^2$", "$r^3$"]
        top_lbls = ["$b$", "$rb$", "$r^2b$", "$r^3b$"]

        for k in range(4):
            ax.plot([bot_pts[k][0], top_pts[k][0]], [bot_pts[k][1], top_pts[k][1]],
                    color=GREY, lw=1.6, ls="--", zorder=1)

        for k in range(4):
            p1, p2 = bot_pts[k], bot_pts[(k + 1) % 4]
            arr = FancyArrowPatch(p1, p2, arrowstyle="-|>", color=BLUE, lw=2.2,
                                  shrinkA=16, shrinkB=16, mutation_scale=15, zorder=2)
            ax.add_patch(arr)

        for k in range(4):
            if not is_twisted:
                p1, p2 = top_pts[k], top_pts[(k + 1) % 4]
                col = BLUE
            else:
                p1, p2 = top_pts[(k + 1) % 4], top_pts[k]
                col = ORANGE
            arr = FancyArrowPatch(p1, p2, arrowstyle="-|>", color=col, lw=2.4,
                                  shrinkA=16, shrinkB=16, mutation_scale=15, zorder=2)
            ax.add_patch(arr)

        for k in range(4):
            draw_node(ax, bot_pts[k][0], bot_pts[k][1], bot_lbls[k],
                      r=0.23, face=GREY_LIGHT, edge=GREY, fs=10.5, lw=1.8, zorder=4)
            draw_node(ax, top_pts[k][0], top_pts[k][1], top_lbls[k],
                      r=0.25, face=ORANGE_LIGHT if is_twisted else BLUE_LIGHT,
                      edge=ORANGE if is_twisted else BLUE, fs=10.2, lw=1.8, zorder=4)

        ax.text(-0.55, 0.45, "$A$", ha="center", va="center", fontsize=11, color=GREY, fontweight="bold")
        ax.text(-0.55, 1.90, "$Ab$", ha="center", va="center", fontsize=11,
                color=ORANGE if is_twisted else BLUE, fontweight="bold")
        ax.set_xlim(-0.85, 2.65)
        ax.set_ylim(-0.38, 2.75)
        ax.set_aspect("equal")
        ax.axis("off")

    draw_two_layers(ax_a, is_twisted=False)
    ax_a.text(1.1, -0.32, "$\\phi_b(r) = r$,  $f(b_1, b_2) = 1$", ha="center", va="center", fontsize=10.5, color=DARK)
    ax_a.set_title("(a) Direct product $C_4 \\times C_2$", fontsize=12, pad=4)

    draw_two_layers(ax_b, is_twisted=True)
    ax_b.text(1.1, -0.32, "$\\phi_b(r) = b r b^{-1} = r^{-1}$,  $f(b_1, b_2) = 1$",
              ha="center", va="center", fontsize=10.5, color=ORANGE)
    ax_b.set_title("(b) Semidirect product $D_8 = C_4 \\,\\rtimes\\, C_2$", fontsize=12, pad=4)

    # --- Panel (c): Factor-set slippage in C_4 vs V_4 (three non-crossing paths) ---
    draw_box(ax_c, 0.55, 0.25, 1.3, 1.85, "", face=GREY_LIGHT, edge=GREY, lw=1.8, pad=0.05, zorder=1)
    draw_box(ax_c, 4.15, 0.25, 1.3, 1.85, "", face=BLUE_LIGHT, edge=BLUE, lw=1.8, pad=0.05, zorder=1)

    p0 = (1.2, 0.65)
    p2 = (1.2, 1.65)
    p1 = (4.8, 0.65)
    p3 = (4.8, 1.65)

    draw_node(ax_c, *p0, "$0$", r=0.25, face="white", edge=GREY, fs=11.5, lw=2.0, zorder=4)
    draw_node(ax_c, *p2, "$2$", r=0.25, face=ORANGE_LIGHT, edge=ORANGE, fs=11.5, lw=2.2, zorder=4)
    draw_node(ax_c, *p1, "$1$", r=0.25, face="white", edge=BLUE, fs=11.5, lw=2.0, zorder=4)
    draw_node(ax_c, *p3, "$3$", r=0.25, face="white", edge=BLUE, fs=11.5, lw=2.0, zorder=4)

    ax_c.text(1.2, 2.34, "fiber $A = \\{0, 2\\}$ ($b=0$)", ha="center", va="center", fontsize=10.8, color=GREY, fontweight="bold")
    ax_c.text(4.8, 2.34, "coset $1+A = \\{1, 3\\}$ ($b=1$)", ha="center", va="center", fontsize=10.8, color=BLUE, fontweight="bold")

    # 1. Bottom arrow: step 1 across B (0 -> 1), curving downward
    arr_step1 = FancyArrowPatch(p0, p1, connectionstyle="arc3,rad=0.18",
                                arrowstyle="-|>", color=BLUE, lw=2.4,
                                shrinkA=18, shrinkB=18, mutation_scale=16, zorder=3)
    ax_c.add_patch(arr_step1)
    ax_c.text(3.0, 0.08, "step 1 across $B$: $0 \\;\\to\\; 1$",
              ha="center", va="center", fontsize=10.5, color=BLUE)

    # 2. Middle horizontal arrow: V_4 split return (1 -> 0), straight at y = 0.65
    arr_split = FancyArrowPatch(p1, p0, connectionstyle="arc3,rad=0.0",
                                arrowstyle="-|>", color=GREY, lw=1.8, ls="--",
                                shrinkA=18, shrinkB=18, mutation_scale=15, zorder=2)
    ax_c.add_patch(arr_split)
    ax_c.text(3.0, 0.86, "$V_4$: $f(1,1)=0$ (returns to $0$)", ha="center", va="center", fontsize=10, color=GREY)

    # 3. Upper curved arrow: C_4 slipped return (1 -> 2), curving upward (rad > 0 from right to left curves UP)
    arr_slip = FancyArrowPatch(p1, p2, connectionstyle="arc3,rad=0.14",
                               arrowstyle="-|>", color=ORANGE, lw=2.8,
                               shrinkA=18, shrinkB=18, mutation_scale=17, zorder=4)
    ax_c.add_patch(arr_slip)
    ax_c.text(3.05, 1.82, "$C_4$: slips by $f(1, 1) = 2 \\in A$",
              ha="center", va="center", fontsize=10.8, color=ORANGE, fontweight="bold")

    ax_c.set_xlim(0.1, 5.9)
    ax_c.set_ylim(-0.12, 2.62)
    ax_c.set_aspect("equal")
    ax_c.axis("off")
    ax_c.set_title("(c) Non-split extension $C_4$ of $A = \\{0, 2\\} \\cong C_2$ by $B = \\{0, 1\\} \\cong C_2$",
                   fontsize=12, pad=4)

    fig.savefig(os.path.join(out, "maths2_extensions_mortar.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Cosets of a centralizer and the conjugacy class (S_4, x = (1 2))
# =========================================================================
def fig_cosets_conjugacy(out):
    # Permutations of {0,1,2,3} as tuples p with p[i] = image of i.
    # Products are read left to right, as in the notes: gh = first g, then h.
    def mul(g, h):
        return compose(h, g)

    def cyc(p):
        seen, parts = set(), []
        for s in range(len(p)):
            if s in seen or p[s] == s:
                seen.add(s)
                continue
            c, x = [s], p[s]
            seen.add(s)
            while x != s:
                c.append(x)
                seen.add(x)
                x = p[x]
            parts.append("(" + "\\,".join(str(i + 1) for i in c) + ")")
        return "$" + ("".join(parts) if parts else "e") + "$"

    S4 = list(it.permutations(range(4)))
    e = (0, 1, 2, 3)
    x = (1, 0, 2, 3)                          # (1 2)
    C = [g for g in S4 if mul(g, x) == mul(x, g)]
    assert len(C) == 4
    C.sort(key=lambda p: (p != e, p != x, p))  # e, (1 2), then the rest

    def transposition(a, b):
        p = list(range(4))
        p[a], p[b] = b, a
        return tuple(p)

    targets = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    rows = []
    for a, b in targets:
        g = next(g for g in S4 if g[0] == a and g[1] == b)   # 1g = a+1, 2g = b+1
        coset = [mul(c, g) for c in C]                       # right coset C g
        conj = mul(mul(invert(g), x), g)                     # g^{-1} x g
        assert conj == transposition(a, b)
        assert all(mul(mul(invert(y), x), y) == conj for y in coset)
        rows.append((coset, conj))
    assert len({y for row, _ in rows for y in row}) == 24

    def cls(p):
        return tuple(sorted((len(part) for part in cycle_parts(p)), reverse=True))

    def cycle_parts(p):
        seen, parts = set(), []
        for s in range(4):
            if s in seen:
                continue
            c, y = [s], p[s]
            seen.add(s)
            while y != s:
                c.append(y)
                seen.add(y)
                y = p[y]
            parts.append(c)
        return parts

    class_style = {
        (1, 1, 1, 1): ("identity $e$ (1)", GREY_LIGHT, GREY),
        (2, 1, 1): ("transpositions (6)", BLUE_LIGHT, BLUE),
        (2, 2): ("double swaps (3)", GREEN_LIGHT, GREEN),
        (3, 1): ("3-cycles (8)", ORANGE_LIGHT, ORANGE),
        (4,): ("4-cycles (6)", PURPLE_LIGHT, PURPLE),
    }
    counts = {}
    for p in S4:
        counts[cls(p)] = counts.get(cls(p), 0) + 1
    assert counts == {(1, 1, 1, 1): 1, (2, 1, 1): 6, (2, 2): 3, (3, 1): 8, (4,): 6}

    fig = plt.figure(figsize=(8.4, 10.0))
    ax_a = fig.add_axes([0.03, 0.50, 0.94, 0.46])
    ax_b = fig.add_axes([0.03, 0.02, 0.94, 0.44])

    bw, bh, gap = 1.12, 0.52, 0.10
    x0 = 0.55

    def grid_box(ax, col, row, label, face, edge, lw=1.5):
        bx = x0 + col * (bw + gap)
        by = (5 - row) * (bh + gap) + 0.2
        ax.add_patch(plt.Rectangle((bx, by), bw, bh, facecolor=face, edgecolor=edge, lw=lw, zorder=2))
        ax.text(bx + bw / 2, by + bh / 2, label, ha="center", va="center", fontsize=9.6, color=DARK, zorder=3)
        return bx, by

    # Panel (a): rows are the 6 right cosets of C = C_G(x); each row gives one conjugate of x.
    row_cols = [(GREY_LIGHT, GREY)] + [(BLUE_LIGHT, BLUE)] * 5
    for r, (coset, conj) in enumerate(rows):
        fc, ec = row_cols[r]
        for c, y in enumerate(coset):
            bx, by = grid_box(ax_a, c, r, cyc(y), fc, ec)
        lab = "$C_G(x)$" if r == 0 else f"coset {r + 1}"
        ax_a.text(x0 - 0.12, by + bh / 2, lab, ha="right", va="center", fontsize=9.6, color=ec)
        ax_a.annotate("", xy=(6.55, by + bh / 2), xytext=(5.45, by + bh / 2),
                      arrowprops=dict(arrowstyle="-|>", color=ec, lw=1.6, mutation_scale=13))
        draw_node(ax_a, 7.15, by + bh / 2, cyc(conj), r=0.28, face=BLUE_LIGHT, edge=BLUE,
                  fs=10, square=True, lw=1.6)
    ax_a.text(3.0, 4.15, "24 elements of $S_4$ = 6 cosets of $C_G(x)$, 4 elements each",
              ha="center", va="center", fontsize=11, color=DARK, fontweight="bold")
    ax_a.text(7.15, 4.15, "class of $x$", ha="center", va="center", fontsize=11, color=BLUE, fontweight="bold")
    ax_a.text(6.0, 3.82, "$g^{-1}xg$", ha="center", va="center", fontsize=10, color=DARK)
    ax_a.set_xlim(-0.6, 7.8)
    ax_a.set_ylim(0.0, 4.45)
    ax_a.axis("off")
    ax_a.set_title("(a) $x = (1\\,2)$: each coset $C_G(x)\\,g$ gives one conjugate $g^{-1}xg$ (6 cosets, 6 conjugates)",
                   fontsize=11.5, pad=2)

    # Panel (b): the same 24 boxes coloured by conjugacy class.
    for r, (coset, conj) in enumerate(rows):
        for c, y in enumerate(coset):
            _, fc, ec = class_style[cls(y)]
            grid_box(ax_b, c, r, cyc(y), fc, ec)
    ly = 3.55
    for k, key in enumerate([(1, 1, 1, 1), (2, 1, 1), (2, 2), (3, 1), (4,)]):
        txt, fc, ec = class_style[key]
        ax_b.add_patch(plt.Rectangle((5.75, ly - k * 0.62), 0.32, 0.32, facecolor=fc, edgecolor=ec, lw=1.5))
        ax_b.text(6.18, ly - k * 0.62 + 0.16, txt, ha="left", va="center", fontsize=9.8, color=DARK)
    ax_b.text(6.75, 0.35, "$24 = 1 + 6 + 3 + 8 + 6$", ha="center", va="center", fontsize=11, color=DARK)
    ax_b.set_xlim(-0.6, 7.8)
    ax_b.set_ylim(0.0, 4.2)
    ax_b.axis("off")
    ax_b.set_title("(b) The same 24 elements coloured by conjugacy class: classes are not cosets",
                   fontsize=11.5, pad=2)

    fig.savefig(os.path.join(out, "maths2_cosets_conjugacy_s4.png"), dpi=160, facecolor="white")
    plt.close(fig)


# =========================================================================
# Orbits, blocks and sub-orbits (D_12 on the hexagon and its long diagonals)
# =========================================================================
def fig_orbits_blocks_suborbits(out):
    # D_12 as permutations of the vertices 0..5 (labelled 1..6).
    rot = tuple((i + 1) % 6 for i in range(6))
    ref = tuple((-i) % 6 for i in range(6))       # reflection through vertices 1 and 4
    D12 = {tuple(range(6))}
    frontier = [tuple(range(6))]
    while frontier:
        g = frontier.pop()
        for s in (rot, ref):
            h = compose(s, g)
            if h not in D12:
                D12.add(h)
                frontier.append(h)
    assert len(D12) == 12

    def is_block(B):
        return all(set(g[i] for i in B) == set(B) or not (set(g[i] for i in B) & set(B)) for g in D12)

    nontrivial = {frozenset(B) for k in (2, 3) for B in it.combinations(range(6), k) if is_block(B)}
    assert nontrivial == {frozenset({0, 3}), frozenset({1, 4}), frozenset({2, 5}),
                          frozenset({0, 2, 4}), frozenset({1, 3, 5})}
    stab = [g for g in D12 if g[0] == 0]
    assert sorted(stab) == sorted([tuple(range(6)), ref])
    suborbits = {frozenset(g[i] for g in stab) for i in range(6)}
    assert suborbits == {frozenset({0}), frozenset({1, 5}), frozenset({2, 4}), frozenset({3})}

    fig, axes = plt.subplots(2, 2, figsize=(8.4, 8.6))
    R, s = 1.0, 0.17

    def pos(i, cx=0.0, cy=0.0):
        ang = np.pi / 2 - i * np.pi / 3
        return cx + R * np.cos(ang), cy + R * np.sin(ang)

    def hexagon(ax, styles, title, lines=(), extra=None):
        for i in range(6):
            a, b = pos(i), pos((i + 1) % 6)
            ax.plot([a[0], b[0]], [a[1], b[1]], color="#bbbbbb", lw=1.6, zorder=1)
        for (i, j, col, ls) in lines:
            a, b = pos(i), pos(j)
            ax.plot([a[0], b[0]], [a[1], b[1]], color=col, lw=1.8, ls=ls, zorder=1)
        for i in range(6):
            fc, ec, lw = styles[i]
            x, y = pos(i)
            draw_node(ax, x, y, f"${i + 1}$", r=s, face=fc, edge=ec, fs=12, square=True, lw=lw)
        if extra:
            extra(ax)
        ax.set_xlim(-1.75, 1.75)
        ax.set_ylim(-1.6, 1.55)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=11.5, pad=4)

    # (a) Orbits: the 6 vertices and the 3 long diagonals A, B, C.
    def diag_boxes(ax):
        for k, name in enumerate("ABC"):
            a, b = pos(k), pos(k + 3)
            ax.plot([a[0], b[0]], [a[1], b[1]], color=ORANGE, lw=1.2, ls="--", zorder=0)
            end = pos([0, 4, 2][k])          # A towards 1, B towards 5, C towards 3
            t = 0.55
            x, y = end[0] * t, end[1] * t
            draw_node(ax, x, y, f"${name}$", r=0.15, face=ORANGE_LIGHT, edge=ORANGE, fs=11, square=True, lw=1.6)
        ax.text(0, -1.45, "orbit of size 6 (vertices) and orbit of size 3 (diagonals)",
                ha="center", va="center", fontsize=9.8, color=DARK)

    hexagon(axes[0, 0], [(BLUE_LIGHT, BLUE, 1.6)] * 6, "(a) Two orbits of $D_{12}$", extra=diag_boxes)

    # (b) Blocks of size 2: opposite vertices.
    pair_cols = {0: (BLUE_LIGHT, BLUE), 3: (BLUE_LIGHT, BLUE), 1: (ORANGE_LIGHT, ORANGE),
                 4: (ORANGE_LIGHT, ORANGE), 2: (GREEN_LIGHT, GREEN), 5: (GREEN_LIGHT, GREEN)}
    hexagon(axes[0, 1], [(pair_cols[i][0], pair_cols[i][1], 1.8) for i in range(6)],
            "(b) Blocks $\\{1,4\\}, \\{2,5\\}, \\{3,6\\}$",
            lines=[(0, 3, BLUE, "--"), (1, 4, ORANGE, "--"), (2, 5, GREEN, "--")],
            extra=lambda ax: ax.text(0, -1.45, "3 blocks of size 2 (opposite vertices)",
                                     ha="center", va="center", fontsize=9.8, color=DARK))

    # (c) Blocks of size 3: alternate vertices.
    tri_cols = {i: ((BLUE_LIGHT, BLUE) if i % 2 == 0 else (ORANGE_LIGHT, ORANGE)) for i in range(6)}
    hexagon(axes[1, 0], [(tri_cols[i][0], tri_cols[i][1], 1.8) for i in range(6)],
            "(c) Blocks $\\{1,3,5\\}, \\{2,4,6\\}$",
            lines=[(0, 2, BLUE, "--"), (2, 4, BLUE, "--"), (4, 0, BLUE, "--"),
                   (1, 3, ORANGE, "--"), (3, 5, ORANGE, "--"), (5, 1, ORANGE, "--")],
            extra=lambda ax: ax.text(0, -1.45, "2 blocks of size 3 (alternate vertices)",
                                     ha="center", va="center", fontsize=9.8, color=DARK))

    # (d) Sub-orbits of the stabilizer of vertex 1.
    sub_cols = {0: (GREY_LIGHT, DARK, 2.8), 1: (BLUE_LIGHT, BLUE, 1.8), 5: (BLUE_LIGHT, BLUE, 1.8),
                2: (ORANGE_LIGHT, ORANGE, 1.8), 4: (ORANGE_LIGHT, ORANGE, 1.8), 3: (GREEN_LIGHT, GREEN, 1.8)}

    def axis_line(ax):
        a, b = pos(0), pos(3)
        ax.plot([a[0], b[0]], [a[1] + 0.25, b[1] - 0.25], color=GREY, lw=1.2, ls=":", zorder=0)
        ax.text(0, -1.45, "sub-orbits $\\{1\\}, \\{2,6\\}, \\{3,5\\}, \\{4\\}$ (distance 0, 1, 2, 3 from 1)",
                ha="center", va="center", fontsize=9.8, color=DARK)

    hexagon(axes[1, 1], [sub_cols[i] for i in range(6)],
            "(d) Fix $1$: $G_1 = \\{e, (2\\,6)(3\\,5)\\}$", extra=axis_line)

    fig.tight_layout(h_pad=1.2, w_pad=0.6)
    fig.savefig(os.path.join(out, "maths2_orbits_blocks_suborbits_hexagon.png"), dpi=160, facecolor="white")
    plt.close(fig)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    fig1_tape_quotient(out)
    fig2_f9_field(out)
    fig3_s3_cosets(out)
    fig_cosets_conjugacy(out)
    fig4_class_equation(out)
    fig5_fourth_isomorphism(out)
    fig6_orbit_stabilizer(out)
    fig_orbits_blocks_suborbits(out)
    fig7_orbitals_pipeline(out)
    fig8_subspace_quotient_shear(out)
    fig9_coherent_pentagon(out)
    fig10_extensions_mortar(out)


if __name__ == "__main__":
    main()
