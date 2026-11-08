#!/usr/bin/env python3
"""Extra figures for Maths 0 and Maths 2 (drawn by Gemini, 2026-11-08).

Usage: python make_maths0_maths2_extra_figures.py OUTPUT_DIR

Writes four PNGs into OUTPUT_DIR:
  maths0_ring_circle_ideal.png       Maths 0, Figure 1 (wrapping Z round a circle; why the glued set must be an ideal)
  maths2_jordan_holder.png           Maths 2, Figure 5 (composition series of C_12, S_4 and A_5)
  maths2_goursat_chessboard.png      Maths 2, Figure 8 (Goursat couplings of S_4 x D_12 as a 6 x 6 chessboard)
  maths2_rep_induction_c3_d6.png     Maths 2, Figure 17 (inducing the irreducible C C_3-modules to C D_6)

Reproduces the published PNGs byte for byte with matplotlib 3.5.1 (the same environment as
make_maths2_figures.py). Every group-theoretic and arithmetic fact depicted is computed in code and
checked with assert.
"""

import itertools as it
import os
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle
import numpy as np

# Unified palette matching make_maths2_figures.py:
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

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10.5,
    "axes.titlesize": 12.0,
    "axes.labelsize": 10.5,
    "xtick.labelsize": 9.5,
    "ytick.labelsize": 9.5,
    "text.color": DARK,
    "axes.labelcolor": DARK,
    "xtick.color": DARK,
    "ytick.color": DARK,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "savefig.facecolor": "white",
})


def compose_perm(p, q):
    """Left-to-right permutation composition: i(pq) = (ip)q for 0-indexed tuples."""
    return tuple(q[p[i]] for i in range(len(p)))


def invert_perm(p):
    """Inverse of a 0-indexed permutation tuple."""
    inv = [0] * len(p)
    for i, v in enumerate(p):
        inv[v] = i
    return tuple(inv)


def perm_parity(p):
    """Return +1 for an even permutation, -1 for an odd permutation."""
    n = len(p)
    inversions = sum(1 for i in range(n) for j in range(i + 1, n) if p[i] > p[j])
    return 1 if inversions % 2 == 0 else -1


def draw_node(ax, x, y, label="", r=0.14, face="white", edge=DARK, fs=10.5,
              square=False, lw=2.0, text_color=DARK, zorder=3, weight="normal"):
    if square:
        patch = Rectangle((x - r, y - r), 2 * r, 2 * r,
                          facecolor=face, edgecolor=edge, lw=lw, zorder=zorder)
    else:
        patch = Circle((x, y), r, facecolor=face, edgecolor=edge, lw=lw, zorder=zorder)
    ax.add_patch(patch)
    if label:
        ax.text(x, y, label, ha="center", va="center", fontsize=fs,
                color=text_color, fontweight=weight, zorder=zorder + 1)


def draw_box(ax, x, y, w, h, label="", face="white", edge=DARK, lw=1.6,
             fs=10.0, text_color=DARK, pad=0.06, ls="-", zorder=2, weight="normal"):
    patch = FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad={pad}",
                           facecolor=face, edgecolor=edge, lw=lw, linestyle=ls, zorder=zorder)
    ax.add_patch(patch)
    if label:
        ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
                fontsize=fs, color=text_color, fontweight=weight, zorder=zorder + 1)


# =========================================================================
# Figure A: maths0_ring_circle_ideal.png
# =========================================================================
def make_fig_a_ring_circle_ideal(out_dir):
    # Compute coset stacks of I = 4Z from -8 to 12
    nums = list(range(-8, 13))
    stacks = {r: [k for k in nums if k % 4 == r] for r in range(4)}
    assert stacks[0] == [-8, -4, 0, 4, 8, 12]
    assert stacks[1] == [-7, -3, 1, 5, 9]
    assert stacks[2] == [-6, -2, 2, 6, 10]
    assert stacks[3] == [-5, -1, 3, 7, 11]

    # Check representative products from stack of 2 and stack of 1
    reps_2 = [2, 6, 10]
    reps_1 = [1, 5, 9]
    assert all(a in stacks[2] for a in reps_2)
    assert all(b in stacks[1] for b in reps_1)
    prods = [a * b for a, b in zip(reps_2, reps_1)]
    assert prods == [2, 30, 90]
    assert all(p % 4 == 2 for p in prods)
    assert 30 % 4 == 2 and 90 % 4 == 2

    # Polynomial arithmetic in Z[x] (tuples of coefficients c_0 + c_1 x + ...)
    def trim_poly(p):
        p = list(p)
        while len(p) > 1 and p[-1] == 0:
            p.pop()
        return tuple(p)

    def sub_poly(p, q):
        m = max(len(p), len(q))
        return trim_poly((p[i] if i < len(p) else 0) - (q[i] if i < len(q) else 0) for i in range(m))

    def mul_poly(p, q):
        res = [0] * (len(p) + len(q) - 1)
        for i, a in enumerate(p):
            for j, b in enumerate(q):
                res[i + j] += a * b
        return trim_poly(res)

    def in_subring_Z(p):
        p = trim_poly(p)
        return len(p) == 1

    poly_0 = (0,)
    poly_5 = (5,)
    poly_x = (0, 1)
    assert in_subring_Z(poly_0) and in_subring_Z(poly_5)
    assert not in_subring_Z(poly_x)
    prod_0x = mul_poly(poly_0, poly_x)
    prod_5x = mul_poly(poly_5, poly_x)
    assert prod_0x == (0,) and in_subring_Z(prod_0x)
    assert prod_5x == (0, 5) and not in_subring_Z(prod_5x)
    diff = sub_poly(prod_5x, prod_0x)
    assert diff == (0, 5) and not in_subring_Z(diff)

    # Use identical y-span (-2.15 to 2.25) on both axes so titles align at the exact same height
    fig = plt.figure(figsize=(11.8, 5.5))
    ax_a = fig.add_axes([0.01, 0.03, 0.51, 0.88])
    ax_b = fig.add_axes([0.54, 0.03, 0.45, 0.88])

    # --- Panel (a): Wrapping Z round a circle of circumference 4 ---
    res_stroke = [GREY, BLUE, ORANGE, GREEN]
    res_fill = [GREY_LIGHT, BLUE_LIGHT, ORANGE_LIGHT, GREEN_LIGHT]

    cx, cy, rad = -0.75, 0.15, 0.96
    circ = Circle((cx, cy), rad, fill=False, edgecolor=DARK, lw=2.2, zorder=2)
    ax_a.add_patch(circ)

    # Curved winding arrow inside the circle to indicate wrapping around circumference 4
    theta_arc = np.linspace(np.pi * 0.42, -np.pi * 1.15, 80)
    r_arc = 0.46
    ax_a.plot(cx + r_arc * np.cos(theta_arc), cy + r_arc * np.sin(theta_arc),
              color=GREY, lw=1.4, ls="--", zorder=2)
    ax_a.annotate("", xy=(cx + r_arc * np.cos(-np.pi * 1.18), cy + r_arc * np.sin(-np.pi * 1.18)),
                  xytext=(cx + r_arc * np.cos(-np.pi * 1.08), cy + r_arc * np.sin(-np.pi * 1.08)),
                  arrowprops=dict(arrowstyle="-|>", color=GREY, lw=1.4, mutation_scale=12))
    ax_a.text(cx, cy, "wrap $\\mathbb{Z}$\n(mod $4$)", ha="center", va="center",
              fontsize=9.3, color=GREY)

    # 4 positions around the circle: 0 (top), 1 (right), 2 (bottom), 3 (left)
    angles = {0: np.pi / 2, 1: 0.0, 2: -np.pi / 2, 3: np.pi}
    for r in range(4):
        ang = angles[r]
        nx, ny = cx + rad * np.cos(ang), cy + rad * np.sin(ang)
        draw_node(ax_a, nx, ny, f"${r}$", r=0.21, face=res_fill[r], edge=res_stroke[r],
                  fs=10.8, lw=2.2, zorder=4, weight="bold")

    def format_stack(r):
        parts = ["\\dots"]
        for k in stacks[r]:
            parts.append(f"\\mathbf{{{k}}}" if k == r else f"{k}")
        parts.append("\\dots")
        return "$" + ",\\, ".join(parts) + "$"

    # Position 0 (top): highlighted as I = 4Z (the ideal)
    draw_box(ax_a, cx - 1.62, cy + rad + 0.30, 3.24, 0.58,
             label="", face=GREY_LIGHT, edge=DARK, lw=2.2, pad=0.05, zorder=3)
    ax_a.text(cx, cy + rad + 0.70, "$I = 4\\mathbb{Z}$ (the ideal, zero coset $0 + I$)",
              ha="center", va="center", fontsize=9.8, color=DARK, fontweight="bold", zorder=4)
    ax_a.text(cx, cy + rad + 0.43, format_stack(0),
              ha="center", va="center", fontsize=9.4, color=DARK, zorder=4)

    # Position 2 (bottom): 2 + I
    draw_box(ax_a, cx - 1.48, cy - rad - 0.88, 2.96, 0.56,
             label="", face=ORANGE_LIGHT, edge=ORANGE, lw=1.8, pad=0.05, zorder=3)
    ax_a.text(cx, cy - rad - 0.48, "coset $2 + I$",
              ha="center", va="center", fontsize=9.8, color=ORANGE, fontweight="bold", zorder=4)
    ax_a.text(cx, cy - rad - 0.72, format_stack(2),
              ha="center", va="center", fontsize=9.4, color=DARK, zorder=4)

    # Position 3 (left): vertical stack for 3 + I
    draw_box(ax_a, cx - rad - 1.32, cy - 0.80, 1.02, 1.60,
             label="", face=GREEN_LIGHT, edge=GREEN, lw=1.6, pad=0.05, zorder=3)
    ax_a.text(cx - rad - 0.81, cy + 0.62, "coset $3 + I$",
              ha="center", va="center", fontsize=9.5, color=GREEN, fontweight="bold", zorder=4)
    stack3_lines = ["$\\vdots$"] + [f"$\\mathbf{{{k}}}$" if k == 3 else f"${k}$" for k in reversed(stacks[3])] + ["$\\vdots$"]
    for idx, tok in enumerate(stack3_lines):
        ax_a.text(cx - rad - 0.81, cy + 0.40 - idx * 0.185, tok,
                  ha="center", va="center", fontsize=9.2, color=DARK, zorder=4)

    # Position 1 (right): vertical stack for 1 + I
    draw_box(ax_a, cx + rad + 0.30, cy - 0.80, 1.02, 1.60,
             label="", face=BLUE_LIGHT, edge=BLUE, lw=1.6, pad=0.05, zorder=3)
    ax_a.text(cx + rad + 0.81, cy + 0.62, "coset $1 + I$",
              ha="center", va="center", fontsize=9.5, color=BLUE, fontweight="bold", zorder=4)
    stack1_lines = ["$\\vdots$"] + [f"$\\mathbf{{{k}}}$" if k == 1 else f"${k}$" for k in reversed(stacks[1])] + ["$\\vdots$"]
    for idx, tok in enumerate(stack1_lines):
        ax_a.text(cx + rad + 0.81, cy + 0.40 - idx * 0.185, tok,
                  ha="center", va="center", fontsize=9.2, color=DARK, zorder=4)

    # Side box on the right of panel (a) showing the products landing in stack 2
    bx, by, bw, bh = 1.68, -1.72, 2.75, 1.88
    draw_box(ax_a, bx, by, bw, bh, label="", face="#fff9f2", edge=ORANGE, lw=1.8, pad=0.06, zorder=3)
    ax_a.text(bx + bw / 2, by + bh - 0.22, "Products from $(2+I) \\times (1+I)$:",
              ha="center", va="center", fontsize=9.8, color=DARK, fontweight="bold", zorder=4)
    ax_a.text(bx + bw / 2, by + bh - 0.56, f"${reps_2[0]} \\times {reps_1[0]} = {prods[0]} \\equiv 2 \\;(\\mathrm{{mod}}\\; 4)$",
              ha="center", va="center", fontsize=9.5, color=DARK, zorder=4)
    ax_a.text(bx + bw / 2, by + bh - 0.88, f"${reps_2[1]} \\times {reps_1[1]} = {prods[1]} \\equiv 2 \\;(\\mathrm{{mod}}\\; 4)$",
              ha="center", va="center", fontsize=9.5, color=DARK, zorder=4)
    ax_a.text(bx + bw / 2, by + bh - 1.20, f"${reps_2[2]} \\times {reps_1[2]} = {prods[2]} \\equiv 2 \\;(\\mathrm{{mod}}\\; 4)$",
              ha="center", va="center", fontsize=9.5, color=DARK, zorder=4)
    ax_a.text(bx + bw / 2, by + 0.24, "$I = 4\\mathbb{Z}$ absorbs $4(xl+ky)+16kl$",
              ha="center", va="center", fontsize=9.1, color=ORANGE, fontweight="bold", zorder=4)

    # Arrow from product box into stack 2
    ax_a.annotate("", xy=(cx + 1.54, cy - rad - 0.60), xytext=(bx - 0.06, by + 0.45),
                  arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.2,
                                  connectionstyle="arc3,rad=-0.12", mutation_scale=15))

    ax_a.set_xlim(-3.20, 4.60)
    ax_a.set_ylim(-2.05, 2.15)
    ax_a.set_aspect("equal")
    ax_a.axis("off")
    ax_a.set_title("(a) Wrapping $\\mathbb{Z}$ round a circle of circumference $4$", fontsize=12.0, pad=8)

    # --- Panel (b): Gluing a subring that is not an ideal ---
    ax_b.plot([-0.20, -0.20], [-1.95, 2.05], color="#dddddd", lw=1.4, zorder=1)

    # Outer box: polynomial ring Z[x]
    draw_box(ax_b, 0.05, -1.18, 6.20, 3.05, label="", face="#fafafa", edge=GREY, lw=1.6, pad=0.06, zorder=1)
    ax_b.text(3.15, 1.68, "Polynomial ring $R = \\mathbb{Z}[x]$",
              ha="center", va="center", fontsize=10.8, color=DARK, fontweight="bold", zorder=3)

    # Upper region: non-constant polynomials (outside S)
    draw_box(ax_b, 0.32, 0.52, 5.66, 0.90, label="", face=ORANGE_LIGHT, edge=ORANGE,
             lw=1.5, ls="--", pad=0.05, zorder=2)
    ax_b.text(1.90, 1.20, "Outside $S$ (degree $\\geq 1$):",
              ha="center", va="center", fontsize=9.8, color=ORANGE, fontweight="bold", zorder=3)
    ax_b.text(1.90, 0.78, "$x,\\; 2x,\\; x^2,\\; \\dots$",
              ha="center", va="center", fontsize=10.0, color=DARK, zorder=3)
    draw_node(ax_b, 4.65, 0.92, "$5x$", r=0.26, face="white", edge=ORANGE,
              fs=10.8, lw=2.4, text_color=ORANGE, zorder=4, weight="bold")

    # Lower band: subring S = Z of constant polynomials, glued to 0
    draw_box(ax_b, 0.32, -1.02, 5.66, 1.02, label="", face=BLUE_LIGHT, edge=BLUE,
             lw=2.0, pad=0.05, zorder=2)
    ax_b.text(0.52, -0.18, "Subring $S = \\mathbb{Z}$ (constants), glued to $0$",
              ha="left", va="center", fontsize=10.0, color=BLUE, fontweight="bold", zorder=3)
    ax_b.text(0.95, -0.55, "$\\dots, -1,$", ha="center", va="center", fontsize=9.6, color=GREY, zorder=3)
    draw_node(ax_b, 1.95, -0.55, "$0$", r=0.24, face="white", edge=BLUE,
              fs=10.8, lw=2.2, text_color=DARK, zorder=4, weight="bold")
    ax_b.text(3.25, -0.55, "$1,\\; 2,\\; \\dots,$", ha="center", va="center", fontsize=9.6, color=GREY, zorder=3)
    draw_node(ax_b, 4.65, -0.55, "$5$", r=0.24, face="white", edge=BLUE,
              fs=10.8, lw=2.2, text_color=DARK, zorder=4, weight="bold")
    ax_b.text(5.45, -0.55, "$\\dots$", ha="center", va="center", fontsize=9.6, color=GREY, zorder=3)

    # Loop arrow on 0: 0 * x = 0 stays in S
    ax_b.annotate("", xy=(1.70, -0.46), xytext=(1.70, -0.64),
                  arrowprops=dict(arrowstyle="-|>", color=GREEN, lw=2.1,
                                  connectionstyle="arc3,rad=-2.4", mutation_scale=13), zorder=5)
    ax_b.text(2.05, -0.92, "$0 \\cdot x = 0 \\in S$ (stays in band)",
              ha="center", va="center", fontsize=9.4, color=GREEN, fontweight="bold", zorder=5)

    # Escaping arrow from 5 in S to 5x outside S (well to the right of the band title)
    ax_b.annotate("", xy=(4.65, 0.62), xytext=(4.65, -0.27),
                  arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.5, mutation_scale=16), zorder=5)
    ax_b.text(5.36, 0.25, "$5 \\cdot x = 5x$\n(escapes $S$)",
              ha="center", va="center", fontsize=9.5, color=ORANGE, fontweight="bold", zorder=5)

    # Bottom explanation note
    draw_box(ax_b, 0.05, -1.92, 6.20, 0.54,
             label="$5x - 0 = 5x \\notin S$, so the product depends on the representative",
             face=ORANGE_LIGHT, edge=ORANGE, lw=1.6, fs=9.8, text_color=DARK, pad=0.05, zorder=3, weight="bold")

    ax_b.set_xlim(-0.30, 6.45)
    ax_b.set_ylim(-2.05, 2.15)
    ax_b.set_aspect("equal")
    ax_b.axis("off")
    ax_b.set_title("(b) Gluing a subring that is not an ideal", fontsize=12.0, pad=8)

    out_path = os.path.join(out_dir, "maths0_ring_circle_ideal.png")
    fig.savefig(out_path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure B: maths2_jordan_holder.png
# =========================================================================
def make_fig_b_jordan_holder(out_dir):
    # --- Part (a) computation: C_12 = <g> subgroups and maximal chains ---
    subgroups_c12 = {}
    for step in [1, 2, 3, 4, 6, 12]:
        H = frozenset((k * step) % 12 for k in range(12))
        order = len(H)
        subgroups_c12[order] = H
    assert sorted(subgroups_c12.keys()) == [1, 2, 3, 4, 6, 12]

    # Compute maximal inclusions (B subsetneq A with no C strictly between)
    orders_c12 = sorted(subgroups_c12.keys(), reverse=True)
    max_edges_c12 = {}
    for a in orders_c12:
        for b in orders_c12:
            if a > b and subgroups_c12[b].issubset(subgroups_c12[a]):
                between = [
                    c for c in orders_c12
                    if a > c > b and subgroups_c12[b].issubset(subgroups_c12[c])
                    and subgroups_c12[c].issubset(subgroups_c12[a])
                ]
                if not between:
                    q_ord = a // b
                    assert q_ord in (2, 3)
                    max_edges_c12[(a, b)] = q_ord

    expected_edges = {(12, 6): 2, (12, 4): 3, (6, 3): 2, (6, 2): 3, (4, 2): 2, (3, 1): 3, (2, 1): 2}
    assert max_edges_c12 == expected_edges

    # Enumerate all composition series from 12 down to 1
    chains_c12 = []
    def dfs_chains(curr, path, quots):
        if curr == 1:
            chains_c12.append((tuple(path), tuple(quots)))
            return
        for (u, v), q in sorted(max_edges_c12.items(), reverse=True):
            if u == curr:
                dfs_chains(v, path + [v], quots + [q])

    dfs_chains(12, [12], [])
    assert len(chains_c12) == 3
    assert chains_c12 == [
        ((12, 6, 3, 1), (2, 2, 3)),
        ((12, 6, 2, 1), (2, 3, 2)),
        ((12, 4, 2, 1), (3, 2, 2)),
    ]
    for _, quots in chains_c12:
        assert sorted(quots) == [2, 2, 3]

    # --- Part (b) computation: S_4 composition series and A_5 simplicity ---
    S4 = list(it.permutations(range(4)))
    A4 = [p for p in S4 if perm_parity(p) == 1]
    e4 = (0, 1, 2, 3)
    p_12_34 = (1, 0, 3, 2)
    p_13_24 = (2, 3, 0, 1)
    p_14_23 = (3, 2, 1, 0)
    V4 = [e4, p_12_34, p_13_24, p_14_23]
    C2_sub = [e4, p_12_34]
    E4 = [e4]

    def is_subgroup(H):
        H_set = set(H)
        return e4 in H_set and all(compose_perm(x, invert_perm(y)) in H_set for x in H for y in H)

    def is_normal_in(N, G):
        N_set = set(N)
        return is_subgroup(N) and set(N).issubset(set(G)) and all(
            compose_perm(compose_perm(invert_perm(g), n), g) in N_set
            for g in G for n in N
        )

    chain_s4 = [S4, A4, V4, C2_sub, E4]
    assert [len(G) for G in chain_s4] == [24, 12, 4, 2, 1]
    quots_s4 = []
    for i in range(len(chain_s4) - 1):
        G_prev, G_next = chain_s4[i], chain_s4[i + 1]
        assert is_normal_in(G_next, G_prev)
        q_ord = len(G_prev) // len(G_next)
        assert q_ord in (2, 3)
        quots_s4.append(q_ord)
    assert quots_s4 == [2, 3, 2, 2]
    assert is_normal_in(C2_sub, V4)
    assert not is_normal_in(C2_sub, S4)

    # Verify A_5 has order 60, is non-abelian, and has conjugacy class sizes 1, 12, 12, 15, 20
    S5 = list(it.permutations(range(5)))
    A5 = [p for p in S5 if perm_parity(p) == 1]
    assert len(A5) == 60
    assert any(compose_perm(x, y) != compose_perm(y, x) for x in A5[:10] for y in A5[:10])
    unvisited = set(A5)
    class_sizes_a5 = []
    while unvisited:
        rep = next(iter(unvisited))
        conj_cls = {compose_perm(compose_perm(invert_perm(g), rep), g) for g in A5}
        class_sizes_a5.append(len(conj_cls))
        unvisited -= conj_cls
    assert sorted(class_sizes_a5) == [1, 12, 12, 15, 20]
    non_id_classes = [12, 12, 15, 20]
    for r in range(1, len(non_id_classes)):
        for sub in it.combinations(non_id_classes, r):
            assert 60 % (1 + sum(sub)) != 0

    # --- Plotting ---
    fig = plt.figure(figsize=(11.4, 5.8))
    ax_a = fig.add_axes([0.02, 0.03, 0.48, 0.89])
    ax_b = fig.add_axes([0.52, 0.03, 0.46, 0.89])

    # Panel (a): Hasse diagram of C_12 with 3 composition series
    pos_c12 = {
        12: (0.0, 3.05),
        6:  (-0.95, 2.05),
        4:  (0.95, 2.05),
        3:  (-1.35, 1.05),
        2:  (0.35, 1.05),
        1:  (0.0, 0.05),
    }
    labels_c12 = {
        12: "$C_{12} = \\langle g \\rangle$\n(order $12$)",
        6:  "$\\langle g^2 \\rangle \\cong C_6$\n(order $6$)",
        4:  "$\\langle g^3 \\rangle \\cong C_4$\n(order $4$)",
        3:  "$\\langle g^4 \\rangle \\cong C_3$\n(order $3$)",
        2:  "$\\langle g^6 \\rangle \\cong C_2$\n(order $2$)",
        1:  "$\\{e\\}$\n(order $1$)",
    }

    series_specs = [
        ((12, 6, 3, 1), BLUE,   -0.055, "Series 1: $12 \\supset 6 \\supset 3 \\supset 1$ ($C_2, C_2, C_3$)"),
        ((12, 6, 2, 1), ORANGE,  0.000, "Series 2: $12 \\supset 6 \\supset 2 \\supset 1$ ($C_2, C_3, C_2$)"),
        ((12, 4, 2, 1), GREEN,   0.055, "Series 3: $12 \\supset 4 \\supset 2 \\supset 1$ ($C_3, C_2, C_2$)"),
    ]
    for path, col, off, _ in series_specs:
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            x1, y1 = pos_c12[u]
            x2, y2 = pos_c12[v]
            dx, dy = x2 - x1, y2 - y1
            length = np.hypot(dx, dy)
            nx, ny = -dy / length, dx / length
            shift = off if (u, v) in ((12, 6), (2, 1)) else 0.0
            ax_a.plot([x1 + shift * nx, x2 + shift * nx],
                      [y1 + shift * ny, y2 + shift * ny],
                      color=col, lw=3.2, solid_capstyle="round", zorder=2)

    edge_label_pos = {
        (12, 6): (-0.68, 2.63, "$C_2$"),
        (12, 4): (0.68, 2.63, "$C_3$"),
        (6, 3):  (-1.38, 1.55, "$C_2$"),
        (6, 2):  (-0.15, 1.65, "$C_3$"),
        (4, 2):  (0.85, 1.55, "$C_2$"),
        (3, 1):  (-0.88, 0.47, "$C_3$"),
        (2, 1):  (0.42, 0.50, "$C_2$"),
    }
    for (u, v), (lx, ly, qlab) in edge_label_pos.items():
        q_ord = max_edges_c12[(u, v)]
        assert qlab == f"$C_{q_ord}$"
        ax_a.text(lx, ly, qlab, ha="center", va="center", fontsize=9.8, color=DARK,
                  fontweight="bold",
                  bbox=dict(boxstyle="round,pad=0.14", facecolor="white", edgecolor="#cccccc", lw=1.0),
                  zorder=4)

    for ord_k, (nx, ny) in pos_c12.items():
        face = GREY_LIGHT if ord_k == 1 else ("#eef4fb" if ord_k == 12 else "white")
        draw_box(ax_a, nx - 0.62, ny - 0.26, 1.24, 0.52, label=labels_c12[ord_k],
                 face=face, edge=DARK, lw=1.8, fs=9.4, pad=0.04, zorder=5)

    # Legend / summary box at the bottom of panel (a), well below {e}
    draw_box(ax_a, -1.95, -1.32, 3.80, 0.90, label="", face="#fafafa", edge=GREY, lw=1.4, pad=0.05, zorder=3)
    for idx, (_, col, _, desc) in enumerate(series_specs):
        yy = -0.58 - idx * 0.22
        ax_a.plot([-1.80, -1.45], [yy, yy], color=col, lw=3.2, zorder=4)
        ax_a.text(-1.35, yy, desc, ha="left", va="center", fontsize=9.2, color=DARK, zorder=4)
    ax_a.text(0.0, -1.20, "Same list of simple factors $\\{C_2, C_2, C_3\\}$ every time",
              ha="center", va="center", fontsize=9.5, color=BLUE, fontweight="bold", zorder=4)

    ax_a.set_xlim(-2.15, 2.00)
    ax_a.set_ylim(-1.48, 3.55)
    ax_a.axis("off")
    ax_a.set_title("(a) Three composition series of $C_{12}$", fontsize=12.0, pad=6)

    # Panel (b): A soluble group (S_4) and a simple one (A_5)
    ax_b.plot([-0.22, -0.22], [-1.40, 3.45], color="#dddddd", lw=1.4, zorder=1)

    s4_nodes = [
        (3.05, "$S_4$ (order $24$)", BLUE_LIGHT, BLUE),
        (2.30, "$A_4$ (order $12$)", BLUE_LIGHT, BLUE),
        (1.55, "$V_4$ (order $4$)", BLUE_LIGHT, BLUE),
        (0.80, "$C_2 = \\{e, (12)(34)\\}$ (order $2$)", ORANGE_LIGHT, ORANGE),
        (0.05, "$\\{e\\}$ (order $1$)", GREY_LIGHT, GREY),
    ]
    x_s4 = 1.18
    quot_names = ["S_4/A_4", "A_4/V_4", "V_4/C_2", "C_2/\\{e\\}"]
    for i in range(len(s4_nodes) - 1):
        y_top = s4_nodes[i][0] - 0.21
        y_bot = s4_nodes[i + 1][0] + 0.21
        ax_b.annotate("", xy=(x_s4, y_bot), xytext=(x_s4, y_top),
                      arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=2.2, mutation_scale=13), zorder=2)
        q_ord = quots_s4[i]
        ax_b.text(x_s4 - 0.14, 0.5 * (y_top + y_bot), f"${quot_names[i]} \\cong C_{q_ord}$",
                  ha="right", va="center", fontsize=9.4, color=BLUE, fontweight="bold", zorder=4)

    for y_pos, lab, fcol, ecol in s4_nodes:
        w = 2.08 if "C_2 =" in lab else 1.56
        draw_box(ax_b, x_s4 - w / 2, y_pos - 0.20, w, 0.40, label=lab,
                 face=fcol, edge=ecol, lw=1.8, fs=9.3, pad=0.04, zorder=4)

    # Note on C_2 normal in V_4 though not in S_4, placed cleanly below {e}
    draw_box(ax_b, 0.00, -1.32, 2.30, 0.90,
             label="$C_2$ is normal in $V_4$ (though not in $S_4$),\nwhich is all a composition series needs.\nSoluble: factors $\\{C_2, C_2, C_2, C_3\\}$",
             face=GREEN_LIGHT, edge=GREEN, lw=1.5, fs=9.0, text_color=DARK, pad=0.04, zorder=4)

    # Right column of panel (b): Simple group A_5
    x_a5 = 3.38
    draw_box(ax_b, x_a5 - 0.82, 3.05 - 0.22, 1.64, 0.44,
             label="$A_5$ (order $60$)", face=ORANGE_LIGHT, edge=ORANGE, lw=2.0, fs=9.8,
             pad=0.04, zorder=4, weight="bold")
    draw_box(ax_b, x_a5 - 0.82, 0.05 - 0.22, 1.64, 0.44,
             label="$\\{e\\}$ (order $1$)", face=GREY_LIGHT, edge=GREY, lw=1.8, fs=9.6,
             pad=0.04, zorder=4)
    ax_b.annotate("", xy=(x_a5, 0.29), xytext=(x_a5, 2.81),
                  arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=2.6, mutation_scale=15), zorder=2)
    ax_b.text(x_a5 + 0.14, 1.55, "single step\nquotient $A_5$\n(no normal\nseam)",
              ha="left", va="center", fontsize=9.4, color=ORANGE, fontweight="bold", zorder=4)

    draw_box(ax_b, 2.46, -1.32, 1.94, 0.90,
             label="Simple, non-abelian\n(not soluble)\nclasses $1, 12, 12, 15, 20$",
             face=ORANGE_LIGHT, edge=ORANGE, lw=1.5, fs=9.0, text_color=DARK, pad=0.04, zorder=4)

    ax_b.set_xlim(-0.30, 4.52)
    ax_b.set_ylim(-1.48, 3.55)
    ax_b.axis("off")
    ax_b.set_title("(b) A soluble group ($S_4$) and a simple one ($A_5$)", fontsize=12.0, pad=6)

    out_path = os.path.join(out_dir, "maths2_jordan_holder.png")
    fig.savefig(out_path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure C: maths2_goursat_chessboard.png
# =========================================================================
def make_fig_c_goursat_chessboard(out_dir):
    # 1. Build S_4 on {0, 1, 2, 3} (representing {1, 2, 3, 4}) and induced map to S_3 on matchings
    S4 = list(it.permutations(range(4)))
    assert len(S4) == 24

    matchings = [
        frozenset([frozenset([0, 1]), frozenset([2, 3])]),  # 0: alpha
        frozenset([frozenset([0, 2]), frozenset([1, 3])]),  # 1: beta
        frozenset([frozenset([0, 3]), frozenset([1, 2])]),  # 2: gamma
    ]

    def induce_on_matchings(g):
        res = []
        for m in matchings:
            img = frozenset(frozenset(g[x] for x in pair) for pair in m)
            res.append(matchings.index(img))
        return tuple(res)

    for g1 in S4:
        for g2 in S4:
            assert induce_on_matchings(compose_perm(g1, g2)) == compose_perm(
                induce_on_matchings(g1), induce_on_matchings(g2)
            )
    V4 = [g for g in S4 if induce_on_matchings(g) == (0, 1, 2)]
    assert len(V4) == 4

    # 2. Build D_12 on hexagon vertices {0, 1, 2, 3, 4, 5} (representing {1..6})
    r_hex = (1, 2, 3, 4, 5, 0)
    s_hex = (0, 5, 4, 3, 2, 1)
    r_pows = [(0, 1, 2, 3, 4, 5)]
    for _ in range(5):
        r_pows.append(compose_perm(r_pows[-1], r_hex))
    C6_rot = set(r_pows)
    assert len(C6_rot) == 6
    D12 = list(r_pows) + [compose_perm(s_hex, rp) for rp in r_pows]
    assert len(set(D12)) == 12

    diagonals = [
        frozenset([0, 3]),  # 0: A
        frozenset([1, 4]),  # 1: B
        frozenset([2, 5]),  # 2: C
    ]

    def induce_on_diagonals(h):
        res = []
        for d in diagonals:
            img = frozenset(h[x] for x in d)
            res.append(diagonals.index(img))
        return tuple(res)

    for h1 in D12:
        for h2 in D12:
            assert induce_on_diagonals(compose_perm(h1, h2)) == compose_perm(
                induce_on_diagonals(h1), induce_on_diagonals(h2)
            )
    Z_D12 = [h for h in D12 if induce_on_diagonals(h) == (0, 1, 2)]
    assert set(Z_D12) == {r_pows[0], r_pows[3]} and len(Z_D12) == 2

    s3_order = [
        (0, 1, 2),  # e
        (1, 2, 0),  # (alpha beta gamma) / (A B C)
        (2, 0, 1),  # (alpha gamma beta) / (A C B)
        (0, 2, 1),  # (beta gamma)       / (B C)
        (2, 1, 0),  # (alpha gamma)      / (A C)
        (1, 0, 2),  # (alpha beta)       / (A B)
    ]
    assert [perm_parity(p) for p in s3_order] == [1, 1, 1, -1, -1, -1]

    row_cosets = [[g for g in S4 if induce_on_matchings(g) == p] for p in s3_order]
    col_cosets = [[h for h in D12 if induce_on_diagonals(h) == p] for p in s3_order]
    assert all(len(c) == 4 for c in row_cosets)
    assert all(len(c) == 2 for c in col_cosets)

    for i, coset in enumerate(row_cosets):
        for g in coset:
            assert (perm_parity(g) == 1) == (i < 3)
    for j, coset in enumerate(col_cosets):
        for h in coset:
            assert (h in C6_rot) == (j < 3)

    def pairs_from_cells(active_cells):
        pairs = set()
        for i, j in active_cells:
            for g in row_cosets[i]:
                for h in col_cosets[j]:
                    pairs.add((g, h))
        return pairs

    def is_subgroup_prod(P):
        id_pair = ((0, 1, 2, 3), (0, 1, 2, 3, 4, 5))
        if id_pair not in P:
            return False
        for g1, h1 in P:
            for g2, h2 in P:
                prod = (compose_perm(g1, invert_perm(g2)), compose_perm(h1, invert_perm(h2)))
                if prod not in P:
                    return False
        return True

    cells_case1 = [(i, j) for i in range(6) for j in range(6)]
    cells_case2 = [(i, j) for i in range(6) for j in range(6) if (i < 3) == (j < 3)]
    cells_case3 = [(i, i) for i in range(6)]

    G1 = pairs_from_cells(cells_case1)
    G2 = pairs_from_cells(cells_case2)
    G3 = pairs_from_cells(cells_case3)

    assert len(cells_case1) == 36 and len(G1) == 288 and is_subgroup_prod(G1)
    assert len(cells_case2) == 18 and len(G2) == 144 and is_subgroup_prod(G2)
    G2_direct = {(g, h) for g in S4 for h in D12 if (perm_parity(g) == 1) == (h in C6_rot)}
    assert G2 == G2_direct
    assert len(cells_case3) == 6 and len(G3) == 48 and is_subgroup_prod(G3)

    # --- Plotting ---
    row_labels = [
        "$e$",
        "$(\\alpha\\,\\beta\\,\\gamma)$",
        "$(\\alpha\\,\\gamma\\,\\beta)$",
        "$(\\beta\\,\\gamma)$",
        "$(\\alpha\\,\\gamma)$",
        "$(\\alpha\\,\\beta)$",
    ]
    col_labels = [
        "$e$",
        "$(A\\,B\\,C)$",
        "$(A\\,C\\,B)$",
        "$(B\\,C)$",
        "$(A\\,C)$",
        "$(A\\,B)$",
    ]

    fig, axes = plt.subplots(1, 3, figsize=(12.6, 5.0))
    fig.subplots_adjust(left=0.11, right=0.98, bottom=0.17, top=0.80, wspace=0.28)

    panel_specs = [
        (axes[0], set(cells_case1), BLUE_LIGHT, BLUE,
         "(a) Case 1, $Q = \\{1\\}$:\n$G = S_4 \\times D_{12}$",
         "$36$ cells $\\times\\, 8 = 288 = |G|$"),
        (axes[1], set(cells_case2), ORANGE_LIGHT, ORANGE,
         "(b) Case 2, $Q = C_2$ (parity),\n$N_2 = C_6$ (two $3\\times 3$ blocks)",
         "$18$ cells $\\times\\, 8 = 144 = |G|$"),
        (axes[2], set(cells_case3), GREEN_LIGHT, GREEN,
         "(c) Case 3, $Q = S_3$,\n$\\theta: \\alpha\\mapsto A,\\, \\beta\\mapsto B,\\, \\gamma\\mapsto C$",
         "$6$ cells $\\times\\, 8 = 48 = |G|$"),
    ]

    for idx, (ax, active, fill_col, edge_col, title, subtitle) in enumerate(panel_specs):
        for i in range(6):
            for j in range(6):
                y = 5 - i
                x = j
                is_on = (i, j) in active
                rect = Rectangle(
                    (x, y), 1.0, 1.0,
                    facecolor=fill_col if is_on else "white",
                    edgecolor=edge_col if is_on else "#cccccc",
                    lw=1.5 if is_on else 1.0,
                    zorder=2 if is_on else 1,
                )
                ax.add_patch(rect)
                if is_on:
                    ax.text(x + 0.5, y + 0.5, "$8$", ha="center", va="center",
                            fontsize=9.2, color=DARK, fontweight="bold", zorder=3)

        # Dashed 3x3 parity divider lines
        ax.plot([0, 6], [3, 3], color=DARK, lw=1.6, ls="--", zorder=4)
        ax.plot([3, 3], [0, 6], color=DARK, lw=1.6, ls="--", zorder=4)
        ax.add_patch(Rectangle((0, 0), 6, 6, fill=False, edgecolor=DARK, lw=2.0, zorder=5))

        for i, rlab in enumerate(row_labels):
            ax.text(-0.14, 5.5 - i, rlab, ha="right", va="center", fontsize=9.3, color=DARK)
        for j, clab in enumerate(col_labels):
            ax.text(j + 0.5, 6.15, clab, ha="center", va="bottom", fontsize=9.1,
                    color=DARK, rotation=32)

        if idx == 0:
            # Place Even/Odd and the vertical axis title well to the left of the row labels
            ax.plot([-1.65, -1.65], [3.1, 5.9], color=GREY, lw=1.2, clip_on=False)
            ax.plot([-1.65, -1.65], [0.1, 2.9], color=GREY, lw=1.2, clip_on=False)
            ax.text(-1.78, 4.5, "Even\n($A_4$)", ha="right", va="center", fontsize=9.0, color=GREY)
            ax.text(-1.78, 1.5, "Odd", ha="right", va="center", fontsize=9.0, color=GREY)
            ax.text(-2.95, 3.0, "Rows: $S_4/V_4$ on $\\{\\alpha, \\beta, \\gamma\\}$",
                    ha="center", va="center", fontsize=10.0, color=DARK, fontweight="bold", rotation=90)

        ax.text(3.0, -0.52, "Columns: $D_{12}/\\langle r^3\\rangle$ on $\\{A, B, C\\}$",
                ha="center", va="center", fontsize=9.4, color=DARK)
        ax.text(3.0, -1.02, subtitle, ha="center", va="center",
                fontsize=10.0, color=edge_col, fontweight="bold")

        ax.set_xlim(-0.2, 6.1)
        ax.set_ylim(-1.3, 6.2)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=11.2, pad=26)

    fig.text(0.54, 0.02,
             "Each cell = $|V_4| \\times |\\langle r^3\\rangle| = 4 \\times 2 = 8$ pairs   "
             "($\\alpha=\\{12|34\\},\\, \\beta=\\{13|24\\},\\, \\gamma=\\{14|23\\}$;   "
             "$A=\\{1,4\\},\\, B=\\{2,5\\},\\, C=\\{3,6\\}$)",
             ha="center", va="bottom", fontsize=10.0, color=DARK, fontweight="bold")

    out_path = os.path.join(out_dir, "maths2_goursat_chessboard.png")
    fig.savefig(out_path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# =========================================================================
# Figure D: maths2_rep_induction_c3_d6.png
# =========================================================================
def make_fig_d_rep_induction_c3_d6(out_dir):
    basis = [(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]
    idx_of = {el: k for k, el in enumerate(basis)}

    def mul_d6(x, y):
        """Multiply (a^i1 b^j1) * (a^i2 b^j2) using b a = a^{-1} b."""
        i1, j1 = x
        i2, j2 = y
        if j1 == 0:
            return ((i1 + i2) % 3, j2)
        else:
            return ((i1 - i2) % 3, (1 + j2) % 2)

    def right_act(vec, g):
        """Right multiplication v * g in CD_6."""
        out = np.zeros(6, dtype=complex)
        for idx, coeff in enumerate(vec):
            prod_el = mul_d6(basis[idx], g)
            out[idx_of[prod_el]] += coeff
        return out

    el_1 = (0, 0)
    el_a = (1, 0)
    el_b = (0, 1)
    assert mul_d6(el_a, mul_d6(el_a, el_a)) == el_1
    assert mul_d6(el_b, el_b) == el_1
    assert mul_d6(el_b, mul_d6(el_a, el_b)) == (2, 0)

    omega = np.exp(2j * np.pi / 3.0)
    v = {
        0: np.array([1.0, 1.0, 1.0, 0.0, 0.0, 0.0], dtype=complex),
        1: np.array([1.0, omega**2, omega, 0.0, 0.0, 0.0], dtype=complex),
        2: np.array([1.0, omega, omega**2, 0.0, 0.0, 0.0], dtype=complex),
    }
    vb = {k: right_act(v[k], el_b) for k in range(3)}

    for k in range(3):
        assert np.allclose(right_act(v[k], el_a), (omega**k) * v[k])
        assert np.allclose(right_act(vb[k], el_a), (omega**(-k)) * vb[k])
        assert np.allclose(vb[k][3:6], v[k][0:3]) and np.allclose(vb[k][0:3], 0.0)

    u1_gen = v[0] + vb[0]
    u2_gen = v[0] - vb[0]
    assert np.allclose(right_act(u1_gen, el_b), +u1_gen)
    assert np.allclose(right_act(u2_gen, el_b), -u2_gen)
    assert np.allclose(right_act(u1_gen, el_a), u1_gen)
    assert np.allclose(right_act(u2_gen, el_a), u2_gen)

    # --- Plotting ---
    fig, axes = plt.subplots(1, 3, figsize=(12.2, 3.15))
    fig.subplots_adjust(left=0.06, right=0.98, bottom=0.08, top=0.90, wspace=0.22)

    panel_info = [
        (0, "(a) $k = 0$: $v_0 = 1 + a + a^2$",
         "$W_0\\!\\uparrow G = \\mathrm{sp}(v_0, v_0 b) = U_1 \\oplus U_2$\n(sum and difference)",
         BLUE, BLUE_LIGHT),
        (1, "(b) $k = 1$: $v_1 = 1 + \\omega^2 a + \\omega a^2$",
         "$W_1\\!\\uparrow G = U_3$, irreducible\n($\\dim = 2$)",
         ORANGE, ORANGE_LIGHT),
        (2, "(c) $k = 2$: $v_2 = 1 + \\omega a + \\omega^2 a^2$",
         "$W_2\\!\\uparrow G = U_4$, irreducible\n($\\dim = 2$)",
         GREEN, GREEN_LIGHT),
    ]

    col_headers = [["$1$", "$a$", "$a^2$"], ["$b$", "$ab$", "$a^2b$"]]

    def coeff_label(c):
        if np.allclose(c, 1.0):
            return "$1$", BLUE
        elif np.allclose(c, omega):
            return "$\\omega$", GREEN
        else:
            assert np.allclose(c, omega**2)
            return "$\\omega^2$", ORANGE

    for k, title, bottom_text, theme_col, theme_fill in panel_info:
        ax = axes[k]
        coeffs_top = v[k][0:3]
        coeffs_bot = vb[k][3:6]
        grid_coeffs = [coeffs_top, coeffs_bot]

        for row_idx in range(2):
            y_center = 1.5 - row_idx * 1.15
            for col_idx in range(3):
                x_center = col_idx * 1.15 + 0.5
                rect = Rectangle(
                    (x_center - 0.52, y_center - 0.50), 1.04, 1.00,
                    facecolor=theme_fill if row_idx == 0 else "#f7f7f7",
                    edgecolor=theme_col if row_idx == 0 else GREY,
                    lw=1.7, zorder=1
                )
                ax.add_patch(rect)

                # Basis element badge in top-left of cell
                ax.text(x_center - 0.44, y_center + 0.37, col_headers[row_idx][col_idx],
                        ha="left", va="center", fontsize=9.5, color=DARK, fontweight="bold", zorder=3)

                # Unit circle and phase arrow for coefficient (clear shaft + arrowhead)
                c_val = grid_coeffs[row_idx][col_idx]
                lab_str, arr_col = coeff_label(c_val)
                rad_c = 0.30
                cy_c = y_center - 0.03
                unit_c = Circle((x_center, cy_c), rad_c, facecolor="white",
                                edgecolor="#bbbbbb", lw=1.1, ls="--", zorder=2)
                ax.add_patch(unit_c)
                ux = float(np.real(c_val))
                uy = float(np.imag(c_val))
                ax.plot([x_center, x_center + 0.65 * rad_c * ux],
                        [cy_c, cy_c + 0.65 * rad_c * uy],
                        color=arr_col, lw=2.2, solid_capstyle="round", zorder=4)
                ax.annotate("", xy=(x_center + rad_c * ux, cy_c + rad_c * uy),
                            xytext=(x_center + 0.35 * rad_c * ux, cy_c + 0.35 * rad_c * uy),
                            arrowprops=dict(arrowstyle="-|>", color=arr_col, lw=2.0, mutation_scale=11),
                            zorder=4)
                ax.plot([x_center], [cy_c], "o", color=DARK, markersize=2.8, zorder=5)

                # Coefficient value in bottom-right of cell
                ax.text(x_center + 0.44, y_center - 0.36, lab_str,
                        ha="right", va="center", fontsize=9.8, color=arr_col, fontweight="bold", zorder=3)

        ax.text(-0.14, 1.50, "$v_{" + str(k) + "}$\nin $H$",
                ha="right", va="center", fontsize=9.8, color=theme_col, fontweight="bold")
        ax.text(-0.14, 0.35, "$v_{" + str(k) + "}b$\nin $Hb$",
                ha="right", va="center", fontsize=9.8, color=DARK, fontweight="bold")

        eig_top = "1" if k == 0 else ("\\omega" if k == 1 else "\\omega^2")
        eig_bot = "1" if k == 0 else ("\\omega^2" if k == 1 else "\\omega")
        ax.text(3.42, 1.50, f"$\\cdot a = {eig_top}$", ha="left", va="center", fontsize=9.3, color=DARK)
        ax.text(3.42, 0.35, f"$\\cdot a = {eig_bot}$", ha="left", va="center", fontsize=9.3, color=DARK)

        draw_box(ax, -0.02, -0.82, 3.40, 0.52, label=bottom_text,
                 face=theme_fill, edge=theme_col, lw=1.6, fs=9.5, text_color=DARK,
                 pad=0.04, zorder=3, weight="bold")

        ax.set_xlim(-0.55, 4.15)
        ax.set_ylim(-0.92, 2.12)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.set_title(title, fontsize=11.3, pad=10)

    fig.text(0.52, 0.03,
             "For $k = 1, 2$: $a$ acts on $v_k$ by $\\omega^k$ and on $v_k b$ by $\\omega^{-k}$ "
             "($\\omega = e^{2\\pi i/3}$), while $b$ swaps $v_k \\leftrightarrow v_k b$, "
             "so no line is fixed by both $a$ and $b$.",
             ha="center", va="bottom", fontsize=10.0, color=DARK, fontweight="bold")

    out_path = os.path.join(out_dir, "maths2_rep_induction_c3_d6.png")
    fig.savefig(out_path, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def main():
    if len(sys.argv) != 2:
        print("Usage: python make_maths0_maths2_extra_figures.py OUTPUT_DIR", file=sys.stderr)
        sys.exit(1)
    out_dir = sys.argv[1]
    os.makedirs(out_dir, exist_ok=True)
    make_fig_a_ring_circle_ideal(out_dir)
    make_fig_b_jordan_holder(out_dir)
    make_fig_c_goursat_chessboard(out_dir)
    make_fig_d_rep_induction_c3_d6(out_dir)
    print("All 4 figures generated and verified in", out_dir)


if __name__ == "__main__":
    main()
