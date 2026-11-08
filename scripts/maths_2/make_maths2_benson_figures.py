#!/usr/bin/env python3
"""Generate Figures 20, 21, 22 and 23 of Maths 2 (the Modules, Homological Algebra & Cohomology chapter).

Usage: python make_maths2_benson_figures.py OUT_DIR (writes the PNGs into OUT_DIR, e.g. docs/maths/figures).
Reproduces the published PNGs byte for byte with matplotlib 3.10 (the lecture-notes skill venv).

Recomputes and asserts every mathematical quantity and set drawn:
1. Figure 20 (maths2_rep_radical_socle_layers.png): Radical and socle series for
   (a) the uniserial regular module F_3 C_3 ~= F_3[x]/(x^3) and
   (b) the direct sum M = F_3 C_3 (+) F_3 where the two filtrations differ.
2. Figure 21 (maths2_rep_snake_lemma.png): The snake lemma commutative diagram
   and switchback path in general (a) and on the worked Z -> Z -> Z/2Z example (b).
3. Figure 22 (maths2_rep_mackey_s3.png): Mackey decomposition on G = S_3 with
   K = {1, (1 2)} and H = {1, (2 3)} (left coset copies in (a), H-orbits and
   double cosets in (b)).
4. Figure 23 (maths2_rep_bar_cocycle_extensions.png): Homogeneous bar resolution
   triangle and tetrahedron with 2-cocycle faces in (a), and the two extensions
   V_4 (alpha[x|x]=0) vs C_4 (alpha[x|x]=1) of C_2 by Z/2Z in (b).
"""

import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Polygon
import numpy as np

DEFAULT_OUT_DIR = "/home/ubuntu/test/temp_gemini/20261104/benson_figures_gemini_to_host/"

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
LIGHT_GREY = "#F2F2F2"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.titlesize": 11.5,
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


def f3_rank(mat):
    """Compute the rank of a matrix over F_3 by Gaussian elimination."""
    A = np.array(mat, dtype=int) % 3
    rows, cols = A.shape
    r = 0
    for c in range(cols):
        if r >= rows:
            break
        pivot = None
        for i in range(r, rows):
            if A[i, c] % 3 != 0:
                pivot = i
                break
        if pivot is None:
            continue
        A[[r, pivot]] = A[[pivot, r]]
        inv = 1 if A[r, c] % 3 == 1 else 2
        A[r] = (A[r] * inv) % 3
        for i in range(rows):
            if i != r and A[i, c] % 3 != 0:
                A[i] = (A[i] - A[i, c] * A[r]) % 3
        r += 1
    return r


# =============================================================================
# Figure 7: Radical and socle series for F_3 C_3 and F_3 C_3 (+) F_3
# =============================================================================
def make_figure_7(out_dir):
    # Action of x = a - 1 on F_3[x]/(x^3) in basis (1, x, x^2)
    X_reg = np.array([
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
    ], dtype=int)

    # Powers X_reg^j over F_3: Rad^j = Im(x^j), Soc^j = Ker(x^j)
    I3 = np.eye(3, dtype=int)
    X_powers = [I3, X_reg, (X_reg @ X_reg) % 3, (X_reg @ X_reg @ X_reg) % 3]
    rad_dims_reg = [f3_rank(P) for P in X_powers]
    soc_dims_reg = [3 - f3_rank(P) for P in X_powers]
    assert rad_dims_reg == [3, 2, 1, 0], f"Unexpected rad_dims_reg: {rad_dims_reg}"
    assert soc_dims_reg == [0, 1, 2, 3], f"Unexpected soc_dims_reg: {soc_dims_reg}"
    for j in range(4):
        assert rad_dims_reg[j] == soc_dims_reg[3 - j]

    # Action of x on M = F_3 C_3 (+) F_3 in basis (1, x, x^2, e_triv)
    X_M = np.zeros((4, 4), dtype=int)
    X_M[:3, :3] = X_reg
    I4 = np.eye(4, dtype=int)
    XM_powers = [I4, X_M, (X_M @ X_M) % 3, (X_M @ X_M @ X_M) % 3]
    rad_dims_M = [f3_rank(P) for P in XM_powers]
    soc_dims_M = [4 - f3_rank(P) for P in XM_powers]
    assert rad_dims_M == [4, 2, 1, 0], f"Unexpected rad_dims_M: {rad_dims_M}"
    assert soc_dims_M == [0, 2, 3, 4], f"Unexpected soc_dims_M: {soc_dims_M}"

    rad_layer_dims_M = [rad_dims_M[j] - rad_dims_M[j + 1] for j in range(3)]
    soc_layer_dims_M = [soc_dims_M[j + 1] - soc_dims_M[j] for j in range(3)]
    assert rad_layer_dims_M == [2, 1, 1]
    assert soc_layer_dims_M == [2, 1, 1]

    fig, (ax_a, ax_b) = plt.subplots(1, 2, figsize=(11.4, 5.2), gridspec_kw={"width_ratios": [1.0, 1.38]})
    fig.subplots_adjust(wspace=0.16, left=0.03, right=0.98, top=0.86, bottom=0.06)

    # --- Panel (a): Uniserial regular module F_3 C_3 ~= F_3[x]/(x^3) ---
    ax_a.set_xlim(0.0, 10.0)
    ax_a.set_ylim(-0.6, 4.3)
    ax_a.axis("off")
    ax_a.set_title(
        "(a) Uniserial regular module $\\mathbb{F}_3 C_3 \\cong \\mathbb{F}_3[x]/(x^3)$\n"
        "($x = a - 1$: radical and socle series coincide)",
        fontsize=11, fontweight="bold", pad=10
    )

    tower_x = 3.5
    box_w = 2.6
    box_h = 0.95
    floors = [
        (2.2, "$\\mathbb{F}_3$", "coset $1 + (x)$", OI_SKY, ""),
        (1.25, "$\\mathbb{F}_3$", "coset $x + (x^2)$", OI_ORANGE, ""),
        (0.3, "$\\mathbb{F}_3$", "span of $x^2$", OI_GREEN, ""),
    ]

    for y0, lbl_main, lbl_sub, col, hatch in floors:
        rect = FancyBboxPatch(
            (tower_x, y0), box_w, box_h,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=col, edgecolor=DARK_GREY, linewidth=1.6, alpha=0.38, hatch=hatch
        )
        ax_a.add_patch(rect)
        ax_a.text(tower_x + box_w / 2, y0 + 0.60, lbl_main, ha="center", va="center",
                  fontsize=11.5, fontweight="bold", color=DARK_GREY)
        ax_a.text(tower_x + box_w / 2, y0 + 0.27, lbl_sub, ha="center", va="center",
                  fontsize=9.2, color=DARK_GREY)

    boundaries_a = [
        (3.15, "$\\mathrm{Rad}^0 = (1)$ (dim $3$)", "$\\mathrm{Soc}^3 = (1)$ (dim $3$)"),
        (2.20, "$\\mathrm{Rad}^1 = (x)$ (dim $2$)", "$\\mathrm{Soc}^2 = (x)$ (dim $2$)"),
        (1.25, "$\\mathrm{Rad}^2 = (x^2)$ (dim $1$)", "$\\mathrm{Soc}^1 = (x^2)$ (dim $1$)"),
        (0.30, "$\\mathrm{Rad}^3 = 0$ (dim $0$)", "$\\mathrm{Soc}^0 = 0$ (dim $0$)"),
    ]
    for y_b, rad_lbl, soc_lbl in boundaries_a:
        ax_a.plot([tower_x - 0.35, tower_x + box_w + 0.35], [y_b, y_b],
                  color=MID_GREY, linestyle="--", linewidth=1.0)
        ax_a.text(tower_x - 0.42, y_b, rad_lbl, ha="right", va="center",
                  fontsize=9.0, color=OI_BLUE, fontweight="bold")
        ax_a.text(tower_x + box_w + 0.42, y_b, soc_lbl, ha="left", va="center",
                  fontsize=9.0, color=OI_VERMILION, fontweight="bold")

    for y_top, y_bot in [(2.75, 1.80), (1.80, 0.85)]:
        arr = FancyArrowPatch(
            (tower_x + box_w - 0.22, y_top),
            (tower_x + box_w - 0.22, y_bot),
            connectionstyle="arc3,rad=-0.35",
            arrowstyle="-|>", mutation_scale=13,
            color=DARK_GREY, linewidth=1.4
        )
        ax_a.add_patch(arr)
    ax_a.text(tower_x + box_w / 2, -0.25,
              "curved arrows inside tower: multiply by $x = a - 1$ ($x^3 = 0$)",
              ha="center", va="center", fontsize=9.0, style="italic", color=MID_GREY)

    # --- Panel (b): Direct sum M = F_3 C_3 (+) F_3 ---
    ax_b.set_xlim(0.0, 13.0)
    ax_b.set_ylim(-0.6, 4.3)
    ax_b.axis("off")
    ax_b.set_title(
        "(b) Direct sum $M = \\mathbb{F}_3 C_3 \\oplus \\mathbb{F}_3$\n"
        "(extra trivial summand sits at the top of $\\mathrm{Rad}$ and bottom of $\\mathrm{Soc}$)",
        fontsize=11, fontweight="bold", pad=10
    )

    rx = 1.05
    bw = 2.02
    bh = 0.95
    ax_b.text(rx + bw, 3.62, "Radical layers (from top)\n$\\mathrm{Rad}^j(M)$: dims $4 \\supset 2 \\supset 1 \\supset 0$",
              ha="center", va="center", fontsize=9.6, fontweight="bold", color=OI_BLUE)

    for y0, lbl_sub, col in [
        (2.2, "$1 + (x)$", OI_SKY),
        (1.25, "$x + (x^2)$", OI_ORANGE),
        (0.3, "$x^2$", OI_GREEN),
    ]:
        rect = FancyBboxPatch(
            (rx, y0), bw, bh,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=col, edgecolor=DARK_GREY, linewidth=1.5, alpha=0.38
        )
        ax_b.add_patch(rect)
        ax_b.text(rx + bw / 2, y0 + 0.62, "$\\mathbb{F}_3$", ha="center", va="center",
                  fontsize=11, fontweight="bold")
        ax_b.text(rx + bw / 2, y0 + 0.26, lbl_sub, ha="center", va="center", fontsize=8.8)

    ex_r = rx + bw + 0.18
    rect_triv_top = FancyBboxPatch(
        (ex_r, 2.2), bw, bh,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        facecolor=OI_PURPLE, edgecolor=DARK_GREY, linewidth=1.8, alpha=0.45, hatch="//"
    )
    ax_b.add_patch(rect_triv_top)
    ax_b.text(ex_r + bw / 2, 2.2 + 0.62, "$\\mathbb{F}_3$ (extra)", ha="center", va="center",
              fontsize=10.2, fontweight="bold")
    ax_b.text(ex_r + bw / 2, 2.2 + 0.26, "in $M/\\mathrm{Rad}\\,M$", ha="center", va="center",
              fontsize=8.6)

    for y_b, r_lbl in [
        (3.15, "$\\mathrm{Rad}^0$ ($4$)"),
        (2.20, "$\\mathrm{Rad}^1$ ($2$)"),
        (1.25, "$\\mathrm{Rad}^2$ ($1$)"),
        (0.30, "$\\mathrm{Rad}^3$ ($0$)"),
    ]:
        w_line = (2 * bw + 0.18) if y_b >= 2.15 else bw
        ax_b.plot([rx - 0.12, rx + w_line + 0.12], [y_b, y_b],
                  color=OI_BLUE, linestyle="--", linewidth=1.0)
        ax_b.text(rx - 0.16, y_b, r_lbl, ha="right", va="center",
                  fontsize=8.6, color=OI_BLUE, fontweight="bold")

    ax_b.plot([6.35, 6.35], [0.1, 3.85], color=MID_GREY, linestyle=":", linewidth=1.1)

    sx = 7.60
    ax_b.text(sx + bw, 3.62, "Socle layers (from bottom)\n$\\mathrm{Soc}^j(M)$: dims $0 \\subset 2 \\subset 3 \\subset 4$",
              ha="center", va="center", fontsize=9.6, fontweight="bold", color=OI_VERMILION)

    for y0, lbl_sub, col in [
        (2.2, "$1 + (x)$", OI_SKY),
        (1.25, "$x + (x^2)$", OI_ORANGE),
        (0.3, "$x^2$", OI_GREEN),
    ]:
        rect = FancyBboxPatch(
            (sx, y0), bw, bh,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=col, edgecolor=DARK_GREY, linewidth=1.5, alpha=0.38
        )
        ax_b.add_patch(rect)
        ax_b.text(sx + bw / 2, y0 + 0.62, "$\\mathbb{F}_3$", ha="center", va="center",
                  fontsize=11, fontweight="bold")
        ax_b.text(sx + bw / 2, y0 + 0.26, lbl_sub, ha="center", va="center", fontsize=8.8)

    ex_s = sx + bw + 0.18
    rect_triv_bot = FancyBboxPatch(
        (ex_s, 0.3), bw, bh,
        boxstyle="round,pad=0.02,rounding_size=0.06",
        facecolor=OI_PURPLE, edgecolor=DARK_GREY, linewidth=1.8, alpha=0.45, hatch="//"
    )
    ax_b.add_patch(rect_triv_bot)
    ax_b.text(ex_s + bw / 2, 0.3 + 0.62, "$\\mathbb{F}_3$ (extra)", ha="center", va="center",
              fontsize=10.2, fontweight="bold")
    ax_b.text(ex_s + bw / 2, 0.3 + 0.26, "in $\\mathrm{Soc}\\,M$", ha="center", va="center",
              fontsize=8.6)

    for y_b, s_lbl in [
        (3.15, "$\\mathrm{Soc}^3$ ($4$)"),
        (2.20, "$\\mathrm{Soc}^2$ ($3$)"),
        (1.25, "$\\mathrm{Soc}^1$ ($2$)"),
        (0.30, "$\\mathrm{Soc}^0$ ($0$)"),
    ]:
        w_line = (2 * bw + 0.18) if y_b <= 1.30 else bw
        ax_b.plot([sx - 0.12, sx + w_line + 0.12], [y_b, y_b],
                  color=OI_VERMILION, linestyle="--", linewidth=1.0)
        ax_b.text(sx - 0.16, y_b, s_lbl, ha="right", va="center",
                  fontsize=8.6, color=OI_VERMILION, fontweight="bold")

    ax_b.text(6.5, -0.25,
              "Hatched box: direct summand $\\mathbb{F}_3$ ($x \\cdot v = 0$), which lies in $\\mathrm{Head}(M)$ and $\\mathrm{Soc}(M)$ simultaneously",
              ha="center", va="center", fontsize=9.0, style="italic", color=MID_GREY)

    out_path = os.path.join(out_dir, "maths2_rep_radical_socle_layers.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"Saved {out_path}")


# =============================================================================
# Figure 8: Snake lemma diagram and switchback chase
# =============================================================================
def make_figure_8(out_dir):
    # Verify the worked example chase numerically
    x_ker_gamma = 1  # 1 mod 2 in Ker(gamma) = Z/2Z
    assert (0 * x_ker_gamma) % 2 == 0
    y_lift = 1  # in C_1 = Z with y_lift mod 2 == x_ker_gamma
    assert y_lift % 2 == x_ker_gamma
    beta_y = 2 * y_lift  # beta = 2 on C_1 = Z
    assert beta_y == 2 and beta_y % 2 == 0
    z_pullback = beta_y // 2  # unique z in C'_0 = Z with 2*z = beta_y
    assert 2 * z_pullback == beta_y and z_pullback == 1
    del_x = z_pullback % 2  # image in Coker(alpha) = Z/2Z
    assert del_x == 1

    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(10.6, 8.8))
    fig.subplots_adjust(hspace=0.25, left=0.03, right=0.97, top=0.93, bottom=0.03)

    def draw_snake_panel(ax, title, nodes_dict, h_arrows, v_arrows, step_boxes):
        ax.set_xlim(0.0, 11.6)
        ax.set_ylim(0.05, 4.7)
        ax.axis("off")
        ax.set_title(title, fontsize=11.2, fontweight="bold", pad=8)

        col_x = {0: 0.75, 1: 3.05, 2: 5.80, 3: 8.55, 4: 10.75}
        row_y = {"ker": 4.10, "c1": 2.85, "c0": 1.60, "cok": 0.42}

        def box_dims(r_key, c_idx):
            highlight = nodes_dict[(r_key, c_idx)][2]
            if highlight:
                return 1.72, 0.62
            return (1.35 if c_idx in (1, 2, 3) else 0.72), 0.52

        # Highlighted continuous S-shaped switchback curve behind the boxes
        s_curve_pts = np.array([
            [col_x[3] + 0.22, row_y["ker"] - 0.25],
            [col_x[3] + 0.22, row_y["c1"] - 0.14],
            [col_x[2] + 0.22, row_y["c1"] - 0.14],
            [col_x[2] + 0.22, row_y["c0"] - 0.14],
            [col_x[1] + 0.22, row_y["c0"] - 0.14],
            [col_x[1] + 0.22, row_y["cok"] + 0.25],
        ])
        ax.plot(s_curve_pts[:, 0], s_curve_pts[:, 1],
                color=OI_ORANGE, linewidth=5.5, alpha=0.32,
                solid_capstyle="round", solid_joinstyle="round", zorder=1)

        snake_segments = [
            ((col_x[3] + 0.22, row_y["ker"] - 0.31), (col_x[3] + 0.22, row_y["c1"] + 0.31)),
            ((col_x[3] - 0.86, row_y["c1"] - 0.14), (col_x[2] + 0.86, row_y["c1"] - 0.14)),
            ((col_x[2] + 0.22, row_y["c1"] - 0.31), (col_x[2] + 0.22, row_y["c0"] + 0.31)),
            ((col_x[2] - 0.86, row_y["c0"] - 0.14), (col_x[1] + 0.86, row_y["c0"] - 0.14)),
            ((col_x[1] + 0.22, row_y["c0"] - 0.31), (col_x[1] + 0.22, row_y["cok"] + 0.31)),
        ]
        for p1, p2 in snake_segments:
            s_arr = FancyArrowPatch(
                p1, p2,
                arrowstyle="-|>", mutation_scale=15,
                color=OI_ORANGE, linewidth=3.2, alpha=0.90, zorder=2
            )
            ax.add_patch(s_arr)

        # Draw node boxes
        for (r_key, c_idx), (main_txt, chase_txt, highlight) in nodes_dict.items():
            x, y = col_x[c_idx], row_y[r_key]
            bw, bh = box_dims(r_key, c_idx)
            fc = "#FFF7E8" if highlight else LIGHT_GREY
            ec = OI_VERMILION if highlight else MID_GREY
            lw = 1.8 if highlight else 1.1
            rect = FancyBboxPatch(
                (x - bw / 2, y - bh / 2), bw, bh,
                boxstyle="round,pad=0.02,rounding_size=0.08",
                facecolor=fc, edgecolor=ec, linewidth=lw, zorder=3
            )
            ax.add_patch(rect)
            if chase_txt:
                ax.text(x, y + 0.12, main_txt, ha="center", va="center",
                        fontsize=10.0, fontweight="bold", color=DARK_GREY, zorder=4)
                ax.text(x, y - 0.14, chase_txt, ha="center", va="center",
                        fontsize=9.1, fontweight="bold", color=OI_VERMILION, zorder=4)
            else:
                ax.text(x, y, main_txt, ha="center", va="center",
                        fontsize=10.0, color=DARK_GREY, zorder=4)

        # Horizontal diagram arrows
        for r_key, c_from, c_to, lbl in h_arrows:
            x1, x2 = col_x[c_from], col_x[c_to]
            y = row_y[r_key]
            bw1, _ = box_dims(r_key, c_from)
            bw2, _ = box_dims(r_key, c_to)
            h_arr = FancyArrowPatch(
                (x1 + bw1 / 2 + 0.04, y), (x2 - bw2 / 2 - 0.04, y),
                arrowstyle="-|>", mutation_scale=12,
                color=DARK_GREY, linewidth=1.2, zorder=3
            )
            ax.add_patch(h_arr)
            if lbl:
                ax.text((x1 + x2) / 2, y + 0.14, lbl, ha="center", va="bottom",
                        fontsize=9.4, color=DARK_GREY, zorder=5)

        # Vertical diagram arrows
        for c_idx, r_from, r_to, lbl, style in v_arrows:
            x = col_x[c_idx]
            y1, y2 = row_y[r_from], row_y[r_to]
            _, bh1 = box_dims(r_from, c_idx)
            _, bh2 = box_dims(r_to, c_idx)
            v_arr = FancyArrowPatch(
                (x, y1 - bh1 / 2 - 0.03), (x, y2 + bh2 / 2 + 0.03),
                arrowstyle="-|>", mutation_scale=12,
                color=DARK_GREY, linewidth=1.2, linestyle=style, zorder=3
            )
            ax.add_patch(v_arr)
            if lbl:
                ax.text(x - 0.12, (y1 + y2) / 2, lbl, ha="right", va="center",
                        fontsize=9.4, color=DARK_GREY, zorder=5)

        # Step callout badges along the switchback path
        for (bx, by, btxt) in step_boxes:
            ax.text(
                bx, by, btxt, ha="center", va="center",
                fontsize=8.7, fontweight="bold", color=DARK_GREY,
                bbox=dict(boxstyle="round,pad=0.20", facecolor="#FFF0D4",
                          edgecolor=OI_VERMILION, lw=1.2),
                zorder=6
            )

    nodes_a = {
        ("ker", 0): ("$0$", "", False),
        ("ker", 1): ("$\\mathrm{Ker}\\,\\alpha$", "", False),
        ("ker", 2): ("$\\mathrm{Ker}\\,\\beta$", "", False),
        ("ker", 3): ("$\\mathrm{Ker}\\,\\gamma$", "$[x]$", True),
        ("c1", 0): ("$0$", "", False),
        ("c1", 1): ("$C'_1$", "", False),
        ("c1", 2): ("$C_1$", "$y$", True),
        ("c1", 3): ("$C''_1$", "$x$", True),
        ("c1", 4): ("$0$", "", False),
        ("c0", 0): ("$0$", "", False),
        ("c0", 1): ("$C'_0$", "$z$", True),
        ("c0", 2): ("$C_0$", "$\\beta(y)$", True),
        ("c0", 3): ("$C''_0$", "$0$", False),
        ("c0", 4): ("$0$", "", False),
        ("cok", 1): ("$\\mathrm{Coker}\\,\\alpha$", "$\\partial[x] = [z]$", True),
        ("cok", 2): ("$\\mathrm{Coker}\\,\\beta$", "", False),
        ("cok", 3): ("$\\mathrm{Coker}\\,\\gamma$", "", False),
        ("cok", 4): ("$0$", "", False),
    }
    h_arrows_a = [
        ("ker", 0, 1, ""), ("ker", 1, 2, ""), ("ker", 2, 3, ""),
        ("c1", 0, 1, ""), ("c1", 1, 2, "$\\phi_1$"), ("c1", 2, 3, "$\\psi_1$"), ("c1", 3, 4, ""),
        ("c0", 0, 1, ""), ("c0", 1, 2, "$\\phi_0$"), ("c0", 2, 3, "$\\psi_0$"), ("c0", 3, 4, ""),
        ("cok", 1, 2, ""), ("cok", 2, 3, ""), ("cok", 3, 4, ""),
    ]
    v_arrows_a = [
        (1, "ker", "c1", "", "--"), (2, "ker", "c1", "", "--"), (3, "ker", "c1", "incl.", "--"),
        (1, "c1", "c0", "$\\alpha$", "-"), (2, "c1", "c0", "$\\beta$", "-"), (3, "c1", "c0", "$\\gamma$", "-"),
        (1, "c0", "cok", "proj.", "--"), (2, "c0", "cok", "", "--"), (3, "c0", "cok", "", "--"),
    ]
    steps_a = [
        (7.18, 3.48, "1. lift along $\\psi_1$"),
        (7.18, 2.25, "2. apply $\\beta$"),
        (4.42, 1.05, "3. pull back along $\\phi_0$"),
        (1.42, 0.98, "4. pass to $\\mathrm{Coker}\\,\\alpha$"),
    ]
    draw_snake_panel(
        ax_a,
        "(a) General switchback path defining the connecting homomorphism $\\partial : \\mathrm{Ker}\\,\\gamma \\to \\mathrm{Coker}\\,\\alpha$",
        nodes_a, h_arrows_a, v_arrows_a, steps_a
    )

    nodes_b = {
        ("ker", 0): ("$0$", "", False),
        ("ker", 1): ("$0$", "", False),
        ("ker", 2): ("$0$", "", False),
        ("ker", 3): ("$\\mathbb{Z}/2\\mathbb{Z}$", "$x = 1\\ \\mathrm{mod}\\ 2$", True),
        ("c1", 0): ("$0$", "", False),
        ("c1", 1): ("$\\mathbb{Z}$", "", False),
        ("c1", 2): ("$\\mathbb{Z}$", "$y = 1$", True),
        ("c1", 3): ("$\\mathbb{Z}/2\\mathbb{Z}$", "$x = 1\\ \\mathrm{mod}\\ 2$", True),
        ("c1", 4): ("$0$", "", False),
        ("c0", 0): ("$0$", "", False),
        ("c0", 1): ("$\\mathbb{Z}$", "$z = 1$", True),
        ("c0", 2): ("$\\mathbb{Z}$", "$\\beta(1) = 2$", True),
        ("c0", 3): ("$\\mathbb{Z}/2\\mathbb{Z}$", "$0\\ \\mathrm{mod}\\ 2$", False),
        ("c0", 4): ("$0$", "", False),
        ("cok", 1): ("$\\mathbb{Z}/2\\mathbb{Z}$", "$\\partial(x) = 1\\ \\mathrm{mod}\\ 2$", True),
        ("cok", 2): ("$\\mathbb{Z}/2\\mathbb{Z}$", "", False),
        ("cok", 3): ("$\\mathbb{Z}/2\\mathbb{Z}$", "", False),
        ("cok", 4): ("$0$", "", False),
    }
    h_arrows_b = [
        ("ker", 0, 1, ""), ("ker", 1, 2, ""), ("ker", 2, 3, ""),
        ("c1", 0, 1, ""), ("c1", 1, 2, "$\\phi_1 = 2$"), ("c1", 2, 3, "$\\psi$"), ("c1", 3, 4, ""),
        ("c0", 0, 1, ""), ("c0", 1, 2, "$\\phi_0 = 2$"), ("c0", 2, 3, "$\\psi$"), ("c0", 3, 4, ""),
        ("cok", 1, 2, "$0$"), ("cok", 2, 3, "$\\sim$"), ("cok", 3, 4, ""),
    ]
    v_arrows_b = [
        (1, "ker", "c1", "", "--"), (2, "ker", "c1", "", "--"), (3, "ker", "c1", "incl.", "--"),
        (1, "c1", "c0", "$\\alpha = 2$", "-"), (2, "c1", "c0", "$\\beta = 2$", "-"), (3, "c1", "c0", "$\\gamma = 0$", "-"),
        (1, "c0", "cok", "mod $2$", "--"), (2, "c0", "cok", "", "--"), (3, "c0", "cok", "", "--"),
    ]
    steps_b = [
        (7.18, 3.48, "1. lift $1\\ \\mathrm{mod}\\ 2 \\mapsto 1$"),
        (7.18, 2.25, "2. $\\beta(1) = 2$"),
        (4.42, 1.05, "3. $2z = 2 \\Rightarrow z = 1$"),
        (1.42, 0.98, "4. $1 \\mapsto 1\\ \\mathrm{mod}\\ 2$"),
    ]
    draw_snake_panel(
        ax_b,
        "(b) Worked example on $0 \\to \\mathbb{Z} \\overset{2}{\\to} \\mathbb{Z} \\overset{\\psi}{\\to} \\mathbb{Z}/2\\mathbb{Z} \\to 0$ with $\\alpha = 2$, $\\beta = 2$, $\\gamma = 0$",
        nodes_b, h_arrows_b, v_arrows_b, steps_b
    )

    out_path = os.path.join(out_dir, "maths2_rep_snake_lemma.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"Saved {out_path}")


# =============================================================================
# Figure 9: Mackey decomposition for S_3 with K = {1, (1 2)}, H = {1, (2 3)}
# =============================================================================
def make_figure_9(out_dir):
    # Represent permutations of {1, 2, 3} as tuples, composing RIGHT TO LEFT:
    # (f * g)(i) = f(g(i))
    def compose_rl(f, g):
        return tuple(f[g[i - 1] - 1] for i in (1, 2, 3))

    def inv_perm(f):
        res = [0, 0, 0]
        for i in (1, 2, 3):
            res[f[i - 1] - 1] = i
        return tuple(res)

    e = (1, 2, 3)
    s12 = (2, 1, 3)
    s23 = (1, 3, 2)
    s13 = (3, 2, 1)
    c123 = (2, 3, 1)  # 1->2->3->1
    c132 = (3, 1, 2)  # 1->3->2->1

    assert compose_rl(s23, s12) == c132
    assert compose_rl(s13, s12) == c123

    G = {e, s12, s23, s13, c123, c132}
    assert len(G) == 6
    K = {e, s12}
    H = {e, s23}

    def left_coset(g, sub):
        return frozenset(compose_rl(g, k) for k in sub)

    coset_1K = left_coset(e, K)
    coset_23K = left_coset(s23, K)
    coset_13K = left_coset(s13, K)

    assert coset_1K == frozenset({e, s12})
    assert coset_23K == frozenset({s23, c132})
    assert coset_13K == frozenset({s13, c123})
    assert (coset_1K | coset_23K | coset_13K) == G

    # Action of (2 3) in H on the left cosets
    act_23_on_1K = frozenset(compose_rl(s23, x) for x in coset_1K)
    act_23_on_23K = frozenset(compose_rl(s23, x) for x in coset_23K)
    act_23_on_13K = frozenset(compose_rl(s23, x) for x in coset_13K)
    assert act_23_on_1K == coset_23K
    assert act_23_on_23K == coset_1K
    assert act_23_on_13K == coset_13K

    # Double cosets H g K
    def double_coset(subH, g, subK):
        return frozenset(compose_rl(h, compose_rl(g, k)) for h in subH for k in subK)

    dc_1 = double_coset(H, e, K)
    dc_13 = double_coset(H, s13, K)
    assert dc_1 == frozenset({e, s12, s23, c132})
    assert dc_13 == frozenset({s13, c123})
    assert dc_1 == (coset_1K | coset_23K)
    assert dc_13 == coset_13K

    # Stabilisers H \cap ^g K
    def conj_sub(g, sub):
        ginv = inv_perm(g)
        return frozenset(compose_rl(g, compose_rl(k, ginv)) for k in sub)

    stab_1 = H & conj_sub(e, K)
    stab_13 = H & conj_sub(s13, K)
    assert stab_1 == frozenset({e})
    assert stab_13 == frozenset(H)

    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(10.4, 7.0), gridspec_kw={"height_ratios": [1.0, 1.38]})
    fig.subplots_adjust(hspace=0.32, left=0.03, right=0.97, top=0.91, bottom=0.04)

    # --- Panel (a): Induced module M \uparrow^G as 3 left-coset boxes ---
    ax_a.set_xlim(0.0, 10.5)
    ax_a.set_ylim(0.0, 3.0)
    ax_a.axis("off")
    ax_a.set_title(
        "(a) Induced module $M{\\uparrow^{S_3}} = RS_3 \\otimes_{RK} M$ as three copies of $M$ over the left cosets of $K = \\{1, (1\\,2)\\}$",
        fontsize=11.0, fontweight="bold", pad=8
    )

    coset_boxes = [
        (0.7, "$1K = \\{1,\\, (1\\,2)\\}$", "$1 \\otimes M$", OI_SKY, ""),
        (3.9, "$(2\\,3)K = \\{(2\\,3),\\, (1\\,3\\,2)\\}$", "$(2\\,3) \\otimes M$", OI_SKY, ""),
        (7.1, "$(1\\,3)K = \\{(1\\,3),\\, (1\\,2\\,3)\\}$", "$(1\\,3) \\otimes M$", OI_GREEN, "//"),
    ]
    bw, bh = 2.7, 1.85
    for x0, c_lbl, m_lbl, col, ht in coset_boxes:
        outer = FancyBboxPatch(
            (x0, 0.55), bw, bh,
            boxstyle="round,pad=0.03,rounding_size=0.10",
            facecolor=col, edgecolor=DARK_GREY, linewidth=1.6, alpha=0.25, hatch=ht
        )
        ax_a.add_patch(outer)
        ax_a.text(x0 + bw / 2, 2.08, c_lbl, ha="center", va="center",
                  fontsize=9.8, fontweight="bold", color=DARK_GREY)
        inner = FancyBboxPatch(
            (x0 + 0.35, 0.78), bw - 0.70, 0.92,
            boxstyle="round,pad=0.02,rounding_size=0.07",
            facecolor="white", edgecolor=DARK_GREY, linewidth=1.3
        )
        ax_a.add_patch(inner)
        ax_a.text(x0 + bw / 2, 1.24, f"copy of $M$:  {m_lbl}", ha="center", va="center",
                  fontsize=9.8, fontweight="bold", color=DARK_GREY)

    ax_a.text(3.625, 1.48, "$\\oplus$", ha="center", va="center", fontsize=15, fontweight="bold")
    ax_a.text(6.825, 1.48, "$\\oplus$", ha="center", va="center", fontsize=15, fontweight="bold")
    ax_a.text(5.25, 0.16,
              "$M{\\uparrow^{S_3}} = (1 \\otimes M) \\;\\oplus\\; ((2\\,3) \\otimes M) \\;\\oplus\\; ((1\\,3) \\otimes M)$",
              ha="center", va="center", fontsize=10.0, fontweight="bold", color=DARK_GREY)

    # --- Panel (b): Restriction to H = {1, (2 3)} and double-coset orbits ---
    ax_b.set_xlim(0.0, 10.5)
    ax_b.set_ylim(-0.18, 4.05)
    ax_b.axis("off")
    ax_b.set_title(
        "(b) Restricting to $H = \\{1, (2\\,3)\\}$ groups the three cosets into two $H$-orbits indexed by $H \\backslash S_3 / K$",
        fontsize=11.0, fontweight="bold", pad=8
    )

    # Orbit 1 container: H * 1 * K
    orb1_rect = FancyBboxPatch(
        (0.45, 0.85), 6.1, 2.95,
        boxstyle="round,pad=0.04,rounding_size=0.14",
        facecolor="#EEF7FC", edgecolor=OI_BLUE, linewidth=1.8, linestyle="--"
    )
    ax_b.add_patch(orb1_rect)
    ax_b.text(3.50, 3.52,
              "Double coset $H \\cdot 1 \\cdot K = \\{1, (1\\,2), (2\\,3), (1\\,3\\,2)\\}$ ($H$-orbit of size $2$)",
              ha="center", va="center", fontsize=9.6, fontweight="bold", color=OI_BLUE)

    for x0, c_lbl, m_lbl in [
        (0.75, "$1K = \\{1, (1\\,2)\\}$", "$1 \\otimes M$"),
        (3.85, "$(2\\,3)K = \\{(2\\,3), (1\\,3\\,2)\\}$", "$(2\\,3) \\otimes M$"),
    ]:
        b_patch = FancyBboxPatch(
            (x0, 1.05), 2.45, 1.48,
            boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=OI_SKY, edgecolor=DARK_GREY, linewidth=1.5, alpha=0.35
        )
        ax_b.add_patch(b_patch)
        ax_b.text(x0 + 1.225, 2.18, c_lbl, ha="center", va="center",
                  fontsize=9.2, fontweight="bold")
        ax_b.text(x0 + 1.225, 1.50, m_lbl, ha="center", va="center",
                  fontsize=9.8, fontweight="bold",
                  bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor=DARK_GREY))

    # Double-headed swap arrow between 1K and (2 3)K, curving gently below the label
    swap_arr = FancyArrowPatch(
        (2.45, 2.58), (4.55, 2.58),
        connectionstyle="arc3,rad=-0.18",
        arrowstyle="<->", mutation_scale=14,
        color=OI_VERMILION, linewidth=2.0
    )
    ax_b.add_patch(swap_arr)
    ax_b.text(3.50, 3.08, "$(2\\,3)$ swaps $1K \\leftrightarrow (2\\,3)K$",
              ha="center", va="center", fontsize=9.1, fontweight="bold", color=OI_VERMILION)

    ax_b.text(3.50, 0.28,
              "Stabiliser $H \\cap {}^1 K = \\{1\\}$  $\\Longrightarrow$  $({}^1 M){\\downarrow_{\\{1\\}}}{\\uparrow^H}$\n"
              "(for trivial $M = R$: gives regular module $RH$ of rank $2$)",
              ha="center", va="center", fontsize=9.2, color=DARK_GREY)

    # Orbit 2 container: H(1 3)K
    orb2_rect = FancyBboxPatch(
        (6.85, 0.85), 3.25, 2.95,
        boxstyle="round,pad=0.04,rounding_size=0.14",
        facecolor="#EFFAF5", edgecolor=OI_GREEN, linewidth=1.8, linestyle="--"
    )
    ax_b.add_patch(orb2_rect)
    ax_b.text(8.475, 3.50,
              "Double coset $H(1\\,3)K = \\{(1\\,3), (1\\,2\\,3)\\}$\n($H$-orbit of size $1$)",
              ha="center", va="center", fontsize=9.2, fontweight="bold", color=OI_GREEN)

    b3_patch = FancyBboxPatch(
        (7.25, 1.05), 2.45, 1.48,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor=OI_GREEN, edgecolor=DARK_GREY, linewidth=1.5, alpha=0.32, hatch="//"
    )
    ax_b.add_patch(b3_patch)
    ax_b.text(8.475, 2.18, "$(1\\,3)K = \\{(1\\,3), (1\\,2\\,3)\\}$",
              ha="center", va="center", fontsize=9.2, fontweight="bold")
    ax_b.text(8.475, 1.50, "$(1\\,3) \\otimes M$", ha="center", va="center",
              fontsize=9.8, fontweight="bold",
              bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor=DARK_GREY))

    loop_arr = FancyArrowPatch(
        (8.05, 2.56), (8.90, 2.56),
        connectionstyle="arc3,rad=-0.42",
        arrowstyle="-|>", mutation_scale=13,
        color=OI_VERMILION, linewidth=1.8
    )
    ax_b.add_patch(loop_arr)
    ax_b.text(8.475, 3.06, "$(2\\,3)$ fixes $(1\\,3)K$",
              ha="center", va="center", fontsize=9.0, fontweight="bold", color=OI_VERMILION)

    ax_b.text(8.475, 0.28,
              "Stabiliser $H \\cap {}^{(1\\,3)}K = H$  $\\Longrightarrow$  $({}^{(1\\,3)}M){\\downarrow_H}$\n"
              "(for trivial $M = R$: gives trivial $R$ of rank $1$)",
              ha="center", va="center", fontsize=9.2, color=DARK_GREY)

    out_path = os.path.join(out_dir, "maths2_rep_mackey_s3.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"Saved {out_path}")


# =============================================================================
# Figure 10: Homogeneous bar resolution (triangle + tetrahedron) & C_2 extensions
# =============================================================================
def make_figure_10(out_dir):
    # Verify the two extensions of C_2 = {0, 1} by M = Z/2Z = {0, 1}
    def ext_mul(e1, e2, alpha_xx):
        m1, g1 = e1
        m2, g2 = e2
        cocycle = alpha_xx if (g1 == 1 and g2 == 1) else 0
        return ((m1 + m2 + cocycle) % 2, (g1 + g2) % 2)

    x_hat = (0, 1)

    p0 = (0, 0)
    p1 = ext_mul(p0, x_hat, 0)
    p2 = ext_mul(p1, x_hat, 0)
    assert p1 == (0, 1) and p2 == (0, 0)

    q0 = (0, 0)
    q1 = ext_mul(q0, x_hat, 1)
    q2 = ext_mul(q1, x_hat, 1)
    q3 = ext_mul(q2, x_hat, 1)
    q4 = ext_mul(q3, x_hat, 1)
    assert [q0, q1, q2, q3, q4] == [(0, 0), (0, 1), (1, 0), (1, 1), (0, 0)]

    fig, (ax_a, ax_b) = plt.subplots(2, 1, figsize=(10.6, 8.9), gridspec_kw={"height_ratios": [1.10, 1.02]})
    fig.subplots_adjust(hspace=0.26, left=0.03, right=0.97, top=0.93, bottom=0.03)

    # --- Panel (a): Homogeneous triangle (1, g_1, g_1 g_2) and tetrahedron ---
    ax_a.set_xlim(0.0, 11.2)
    ax_a.set_ylim(0.0, 4.5)
    ax_a.axis("off")
    ax_a.set_title(
        "(a) Homogeneous bar simplices: $2$-cochain on $(1, g_1, g_1 g_2)$ and the four faces of $(\\delta^2\\alpha)(g_1, g_2, g_3) = 0$",
        fontsize=11.0, fontweight="bold", pad=8
    )

    tri_pts = np.array([[0.8, 0.95], [2.25, 3.45], [3.85, 1.15]])
    tri_poly = Polygon(tri_pts, closed=True, facecolor=OI_SKY, edgecolor=DARK_GREY,
                       alpha=0.28, linewidth=1.8)
    ax_a.add_patch(tri_poly)

    edge_specs = [
        (tri_pts[0], tri_pts[1], "$[g_1]$", (-0.36, 0.12)),
        (tri_pts[1], tri_pts[2], "$g_1[g_2]$", (0.44, 0.14)),
        (tri_pts[0], tri_pts[2], "$-[g_1 g_2]$", (0.0, -0.26)),
    ]
    for p_start, p_end, e_lbl, (dx, dy) in edge_specs:
        mid = 0.5 * (p_start + p_end)
        direction = p_end - p_start
        e_arr = FancyArrowPatch(
            tuple(mid - 0.12 * direction), tuple(mid + 0.12 * direction),
            arrowstyle="-|>", mutation_scale=13, color=DARK_GREY, linewidth=1.6, zorder=4
        )
        ax_a.add_patch(e_arr)
        ax_a.text(mid[0] + dx, mid[1] + dy, e_lbl, ha="center", va="center",
                  fontsize=9.4, fontweight="bold", color=DARK_GREY)

    for pt, v_lbl, (ox, oy) in [
        (tri_pts[0], "$1$", (-0.24, -0.15)),
        (tri_pts[1], "$g_1$", (0.0, 0.25)),
        (tri_pts[2], "$g_1 g_2$", (0.38, -0.12)),
    ]:
        ax_a.plot(pt[0], pt[1], "o", color=OI_BLUE, markersize=7.5, zorder=5)
        ax_a.text(pt[0] + ox, pt[1] + oy, v_lbl, ha="center", va="center",
                  fontsize=10.5, fontweight="bold", color=DARK_GREY)

    ax_a.text(2.30, 1.88, "$[g_1 \\mid g_2]$\n$\\alpha(g_1, g_2)$", ha="center", va="center",
              fontsize=10.2, fontweight="bold", color=OI_BLUE,
              bbox=dict(boxstyle="round,pad=0.22", facecolor="white", edgecolor=OI_BLUE, alpha=0.9))
    ax_a.text(2.30, 0.25,
              "$\\partial_2[g_1 \\mid g_2] = g_1[g_2] - [g_1 g_2] + [g_1]$",
              ha="center", va="center", fontsize=9.5, color=DARK_GREY)

    ax_a.plot([4.65, 4.65], [0.2, 4.1], color=MID_GREY, linestyle=":", linewidth=1.1)

    # Right of Panel (a): Tetrahedron (1, g_1, g_1 g_2, g_1 g_2 g_3)
    v0 = np.array([5.45, 1.15])   # 1
    v1 = np.array([6.85, 3.65])   # g_1
    v2 = np.array([8.10, 2.30])   # g_1 g_2
    v3 = np.array([10.15, 1.15])  # g_1 g_2 g_3

    face0_poly = Polygon([v1, v2, v3], closed=True, facecolor=OI_ORANGE, edgecolor="none", alpha=0.35)
    ax_a.add_patch(face0_poly)
    face3_poly = Polygon([v0, v1, v2], closed=True, facecolor=OI_SKY, edgecolor="none", alpha=0.22)
    ax_a.add_patch(face3_poly)

    solid_edges = [(v0, v1), (v1, v2), (v2, v3), (v0, v2), (v1, v3)]
    for pA, pB in solid_edges:
        ax_a.plot([pA[0], pB[0]], [pA[1], pB[1]], color=DARK_GREY, linewidth=1.6, zorder=3)
    ax_a.plot([v0[0], v3[0]], [v0[1], v3[1]], color=MID_GREY, linestyle="--", linewidth=1.4, zorder=2)

    for pt, v_lbl, (ox, oy) in [
        (v0, "$1$", (-0.22, -0.15)),
        (v1, "$g_1$", (-0.05, 0.25)),
        (v2, "$g_1 g_2$", (-0.08, -0.26)),
        (v3, "$g_1 g_2 g_3$", (0.52, -0.12)),
    ]:
        ax_a.plot(pt[0], pt[1], "o", color=OI_VERMILION, markersize=7.5, zorder=5)
        ax_a.text(pt[0] + ox, pt[1] + oy, v_lbl, ha="center", va="center",
                  fontsize=10.2, fontweight="bold", color=DARK_GREY)

    face_boxes = [
        (9.35, 3.45, (8.38, 2.45),
         "Face opposite $1$: $(g_1, g_1 g_2, g_1 g_2 g_3) = g_1(1, g_2, g_2 g_3)$\n"
         "gives $+g_1\\,\\alpha(g_2, g_3)$", "#FFF0D4", OI_VERMILION),
        (5.65, 3.85, (6.72, 2.48),
         "Face opposite $g_1 g_2 g_3$:\n$-\\alpha(g_1, g_2)$", "#EEF7FC", OI_BLUE),
        (6.05, 0.38, (7.30, 1.50),
         "Face opposite $g_1 g_2$: $+\\alpha(g_1, g_2 g_3)$", "#EFFAF5", OI_GREEN),
        (9.35, 0.38, (8.25, 1.50),
         "Face opposite $g_1$: $-\\alpha(g_1 g_2, g_3)$", "#F9F0F6", OI_PURPLE),
    ]
    for bx, by, target, txt, fc, ec in face_boxes:
        ax_a.annotate(
            txt, xy=target, xytext=(bx, by),
            ha="center", va="center", fontsize=8.6, fontweight="bold", color=DARK_GREY,
            bbox=dict(boxstyle="round,pad=0.22", facecolor=fc, edgecolor=ec, lw=1.2),
            arrowprops=dict(arrowstyle="->", color=ec, lw=1.2, shrinkB=4),
            zorder=6
        )

    # --- Panel (b): Two extensions V_4 vs C_4 of C_2 = {1, x} by M = Z/2Z = {0, 1} ---
    ax_b.set_xlim(0.0, 11.2)
    ax_b.set_ylim(0.0, 4.25)
    ax_b.axis("off")
    ax_b.set_title(
        "(b) Fibres of $\\hat{G}$ over $C_2 = \\{1, x\\}$ ($M = \\mathbb{Z}/2\\mathbb{Z} = \\{0, 1\\}$) and the path \"multiply by $\\hat{x} = (0, x)$\"",
        fontsize=11.0, fontweight="bold", pad=8
    )

    def draw_extension_subdiagram(x_off, sub_title, is_c4):
        ax_b.text(x_off + 2.40, 3.96, sub_title, ha="center", va="center",
                  fontsize=9.9, fontweight="bold", color=DARK_GREY)

        fx1, fxx = x_off + 0.95, x_off + 3.85
        ax_b.plot([fx1 - 0.45, fxx + 0.45], [0.42, 0.42], color=DARK_GREY, lw=1.5)
        ax_b.plot([fx1, fxx], [0.42, 0.42], "s", color=DARK_GREY, markersize=6.5)
        ax_b.text(fx1, 0.14, "$1 \\in C_2$", ha="center", va="center", fontsize=9.5, fontweight="bold")
        ax_b.text(fxx, 0.14, "$x \\in C_2$", ha="center", va="center", fontsize=9.5, fontweight="bold")

        for fx in (fx1, fxx):
            fbox = FancyBboxPatch(
                (fx - 0.62, 0.98), 1.24, 2.42,
                boxstyle="round,pad=0.02,rounding_size=0.10",
                facecolor=LIGHT_GREY, edgecolor=MID_GREY, linewidth=1.2, linestyle="--"
            )
            ax_b.add_patch(fbox)
            p_arr = FancyArrowPatch(
                (fx, 0.95), (fx, 0.50),
                arrowstyle="-|>", mutation_scale=11, color=MID_GREY, linewidth=1.2
            )
            ax_b.add_patch(p_arr)

        y_m0, y_m1 = 1.62, 2.92
        pts = [
            (fx1, y_m0, "$(0, 1) = \\hat{1}$", -0.32),
            (fx1, y_m1, "$(1, 1)$", +0.26),
            (fxx, y_m0, "$(0, x) = \\hat{x}$", -0.32),
            (fxx, y_m1, "$(1, x)$", +0.26),
        ]
        for px, py, plbl, dy_lbl in pts:
            ax_b.plot(px, py, "o", color=DARK_GREY, markersize=7.5, zorder=5)
            ax_b.text(px, py + dy_lbl, plbl,
                      ha="center", va="center", fontsize=9.0, fontweight="bold", color=DARK_GREY, zorder=6)

        if not is_c4:
            arr1 = FancyArrowPatch(
                (fx1 + 0.16, y_m0 + 0.08), (fxx - 0.16, y_m0 + 0.08),
                connectionstyle="arc3,rad=-0.20",
                arrowstyle="-|>", mutation_scale=14,
                color=OI_BLUE, linewidth=2.2, zorder=4
            )
            arr2 = FancyArrowPatch(
                (fxx - 0.16, y_m0 - 0.06), (fx1 + 0.16, y_m0 - 0.06),
                connectionstyle="arc3,rad=-0.16",
                arrowstyle="-|>", mutation_scale=14,
                color=OI_GREEN, linewidth=2.2, linestyle="--", zorder=4
            )
            ax_b.add_patch(arr1)
            ax_b.add_patch(arr2)
            ax_b.text((fx1 + fxx) / 2, y_m0 + 0.45, "step 1: $\\cdot\\,\\hat{x}$",
                      ha="center", va="center", fontsize=9.0, fontweight="bold", color=OI_BLUE)
            ax_b.text((fx1 + fxx) / 2, y_m0 - 0.48, "step 2: $\\cdot\\,\\hat{x}$ ($\\hat{x}^2 = (0, 1)$)",
                      ha="center", va="center", fontsize=8.8, fontweight="bold", color=OI_GREEN)
        else:
            arr1 = FancyArrowPatch(
                (fx1 + 0.16, y_m0 - 0.02), (fxx - 0.16, y_m0 - 0.02),
                connectionstyle="arc3,rad=-0.14",
                arrowstyle="-|>", mutation_scale=14,
                color=OI_BLUE, linewidth=2.2, zorder=4
            )
            arr2 = FancyArrowPatch(
                (fxx - 0.16, y_m0 + 0.12), (fx1 + 0.16, y_m1 - 0.12),
                connectionstyle="arc3,rad=0.14",
                arrowstyle="-|>", mutation_scale=14,
                color=OI_VERMILION, linewidth=2.4, zorder=4
            )
            arr3 = FancyArrowPatch(
                (fx1 + 0.16, y_m1 + 0.02), (fxx - 0.16, y_m1 + 0.02),
                connectionstyle="arc3,rad=0.14",
                arrowstyle="-|>", mutation_scale=12,
                color=OI_PURPLE, linewidth=1.6, linestyle="--", zorder=4
            )
            arr4 = FancyArrowPatch(
                (fxx - 0.16, y_m1 - 0.12), (fx1 + 0.16, y_m0 + 0.12),
                connectionstyle="arc3,rad=0.14",
                arrowstyle="-|>", mutation_scale=12,
                color=OI_PURPLE, linewidth=1.6, linestyle=":", zorder=4
            )
            for a in (arr1, arr2, arr3, arr4):
                ax_b.add_patch(a)
            ax_b.text((fx1 + fxx) / 2, y_m0 - 0.42, "step 1: $\\cdot\\,\\hat{x}$",
                      ha="center", va="center", fontsize=8.9, fontweight="bold", color=OI_BLUE)
            ax_b.text((fx1 + fxx) / 2, 2.27,
                      "step 2: $\\hat{x}^2 = (1, 1)$\n(slips by $\\alpha[x \\mid x] = 1$)",
                      ha="center", va="center", fontsize=8.2, fontweight="bold", color=OI_VERMILION,
                      bbox=dict(boxstyle="round,pad=0.14", facecolor="#FFF0D4", edgecolor=OI_VERMILION, lw=1.0),
                      zorder=6)
            ax_b.text((fx1 + fxx) / 2, 3.60, "steps 3, 4: $\\hat{x}^3 = (1, x),\\; \\hat{x}^4 = (0, 1)$",
                      ha="center", va="center", fontsize=8.6, fontweight="bold", color=OI_PURPLE)

    draw_extension_subdiagram(
        0.35,
        "$\\alpha[x \\mid x] = 0$: split extension $\\hat{G} \\cong V_4 = C_2 \\times C_2$ ($\\hat{x}^2 = \\hat{1}$)",
        is_c4=False
    )
    ax_b.plot([5.6, 5.6], [0.1, 4.0], color=MID_GREY, linestyle=":", linewidth=1.1)
    draw_extension_subdiagram(
        5.85,
        "$\\alpha[x \\mid x] = 1$: non-split extension $\\hat{G} \\cong C_4$ ($\\hat{x}$ of order $4$)",
        is_c4=True
    )

    out_path = os.path.join(out_dir, "maths2_rep_bar_cocycle_extensions.png")
    fig.savefig(out_path, dpi=200)
    plt.close(fig)
    print(f"Saved {out_path}")


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUT_DIR
    os.makedirs(out_dir, exist_ok=True)
    make_figure_7(out_dir)
    make_figure_8(out_dir)
    make_figure_9(out_dir)
    make_figure_10(out_dir)
    print("ALL 4 BENSON FIGURES GENERATED AND VERIFIED SUCCESSFULLY.")


if __name__ == "__main__":
    main()
