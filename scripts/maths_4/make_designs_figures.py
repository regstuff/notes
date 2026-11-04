"""Figures 24 to 27 for the chapter "Designs" (Maths 4, incidence geometry).

Usage: python make_designs_figures.py OUTPUT_DIR

Writes four PNGs into OUTPUT_DIR:
  maths4_designs_double_count.png   (Figure 24) double counting above X={000,001} in AG(3,2)=S(3,4,8)
  maths4_designs_fisher_ag23.png    (Figure 25) incidence matrix M and Gram matrix MM^T=3I+J of AG(2,3)
  maths4_designs_planes_count.png   (Figure 26) projective vs affine line budget at n=3: PG(2,3) vs AG(2,3)
  maths4_designs_building.png       (Figure 27) split incidence matrix of AG(3,2) and lambda_i^j triangles

Every count, block, incidence matrix, eigenvalue, determinant, and block-avoidance number is
computed from first principles and asserted before plotting.
"""

import itertools as it
import math
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Polygon, Rectangle
import numpy as np

BLUE = "#1f3b73"
ORANGE = "#d9730d"
GREEN = "#2e7d32"
PURPLE = "#6a3d9a"
RED = "#c62828"
GREY = "#9a9a9a"
DARK = "#222222"


def bits(v):
    return "".join(str(c) for c in v)


def build_ag32():
    """Return points and affine-plane blocks of AG(3,2) = S(3,4,8)."""
    pts = list(it.product((0, 1), repeat=3))
    assert len(pts) == 8
    blocks = []
    for B in it.combinations(pts, 4):
        xor = tuple(sum(p[c] for p in B) % 2 for c in range(3))
        if xor == (0, 0, 0):
            blocks.append(frozenset(B))
    assert len(blocks) == 14
    # Check 3-(8,4,1) design and downward cascade counts
    for s, expected in [(3, 1), (2, 3), (1, 7), (0, 14)]:
        for X in it.combinations(pts, s):
            X = frozenset(X)
            cnt = sum(1 for B in blocks if X <= B)
            formula = math.comb(8 - s, 3 - s) // math.comb(4 - s, 3 - s) * 1
            assert cnt == expected == formula
    # Check block classification: 6 faces, 6 diagonal planes, 2 parity tetrahedra
    faces, diag_planes, tetra = [], [], []
    for B in blocks:
        const_coords = [c for c in range(3) if len({p[c] for p in B}) == 1]
        pair_sums = [
            (c1, c2)
            for c1, c2 in it.combinations(range(3), 2)
            if len({(p[c1] + p[c2]) % 2 for p in B}) == 1
        ]
        if len(const_coords) == 1:
            faces.append(B)
        elif len(pair_sums) == 1:
            diag_planes.append(B)
        else:
            assert len({(p[0] + p[1] + p[2]) % 2 for p in B}) == 1
            tetra.append(B)
    assert len(faces) == 6 and len(diag_planes) == 6 and len(tetra) == 2
    return pts, blocks


def build_ag23():
    """Return points and blocks of AG(2,3) = S(2,3,9) in Figure 8(a) order."""
    # Points ordered row-by-row from y=0 to y=2, x=0 to x=2
    pts = [(x, y) for y in range(3) for x in range(3)]
    assert len(pts) == 9
    # 4 parallel classes in Figure 8(a) order:
    # Slope 0: y = c (c = 0, 1, 2)
    slope_0 = [frozenset((x, c) for x in range(3)) for c in range(3)]
    # Slope inf: x = c (c = 0, 1, 2)
    slope_inf = [frozenset((c, y) for y in range(3)) for c in range(3)]
    # Slope 1 mod 3: y = (x + c) mod 3 (c = 0, 1, 2)
    slope_1 = [frozenset((x, (x + c) % 3) for x in range(3)) for c in range(3)]
    # Slope 2 mod 3: y = (2x + c) mod 3 (c = 0, 1, 2)
    slope_2 = [frozenset((x, (2 * x + c) % 3) for x in range(3)) for c in range(3)]

    classes = [
        ("Slope $0$", slope_0),
        ("Slope $\\infty$", slope_inf),
        ("Slope $1$", slope_1),
        ("Slope $2$", slope_2),
    ]
    blocks = [B for _, cls in classes for B in cls]
    assert len(blocks) == 12
    assert all(len(B) == 3 for B in blocks)
    # Check each parallel class partitions the 9 points
    for _, cls in classes:
        assert len(cls) == 3
        assert set().union(*cls) == set(pts)
    # Check 2-(9,3,1) design properties
    for p in pts:
        assert sum(1 for B in blocks if p in B) == 4
    for p, q in it.combinations(pts, 2):
        assert sum(1 for B in blocks if p in B and q in B) == 1
    return pts, blocks, classes


def lambda_ij_closed(v, k, t, lam, i, j):
    b = math.comb(v, t) * lam // math.comb(k, t)
    return math.comb(v - i - j, k - i) * b // math.comb(v, k)


def lambda_ij_ie(v, k, t, lam, i, j):
    total = 0
    for m in range(j + 1):
        lam_im = math.comb(v - (i + m), t - (i + m)) * lam // math.comb(k - (i + m), t - (i + m))
        total += ((-1) ** m) * math.comb(j, m) * lam_im
    return total


# ---------------------------------------------------------------- Figure 24
def fig14_double_count(out):
    pts, blocks = build_ag32()
    X = frozenset({(0, 0, 0), (0, 0, 1)})
    triples_Y = [frozenset(X | {p}) for p in pts if p not in X]
    assert len(triples_Y) == math.comb(8 - 2, 3 - 2) == 6
    blocks_X = [B for B in blocks if X <= B]
    assert len(blocks_X) == 3

    B1 = frozenset({(0, 0, 0), (0, 0, 1), (0, 1, 0), (0, 1, 1)})  # face x0 = 0
    B2 = frozenset({(0, 0, 0), (0, 0, 1), (1, 0, 0), (1, 0, 1)})  # face x1 = 0
    B3 = frozenset({(0, 0, 0), (0, 0, 1), (1, 1, 0), (1, 1, 1)})  # diag plane x0 + x1 = 0
    assert set(blocks_X) == {B1, B2, B3}
    assert (B1 & B2) == X and (B1 & B3) == X and (B2 & B3) == X
    ordered_B = [B1, B2, B3]

    # Check bipartite degrees: each Y has degree 1, each B has degree 2, total flags = 6
    edges = [(i, j) for i, Y in enumerate(triples_Y) for j, B in enumerate(ordered_B) if Y <= B]
    assert len(edges) == 6
    for i in range(6):
        assert sum(1 for u, _ in edges if u == i) == 1
    for j in range(3):
        assert sum(1 for _, v in edges if v == j) == 2

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.4, 5.2), gridspec_kw=dict(width_ratios=[1.38, 1.0]))

    # Panel (a): Three copies of the 3-cube side by side, one for each block B_1, B_2, B_3
    def cpos(p, x_shift):
        x0, x1, x2 = p
        px = x_shift + 1.45 * x1 + 0.78 * x0
        py = 1.85 * x2 + 0.68 * x0
        return np.array([px, py])

    cube_specs = [
        (
            0.0,
            B1,
            [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)],
            BLUE,
            "$B_1$ (front face)",
            "$\\{000, 001, 010, 011\\}$",
            False,
        ),
        (
            3.35,
            B2,
            [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)],
            GREEN,
            "$B_2$ (left face)",
            "$\\{000, 001, 100, 101\\}$",
            False,
        ),
        (
            6.70,
            B3,
            [(0, 0, 0), (1, 1, 0), (1, 1, 1), (0, 0, 1)],
            PURPLE,
            "$B_3$ (diagonal plane)",
            "$\\{000, 001, 110, 111\\}$",
            True,
        ),
    ]

    offsets = {
        (0, 0, 0): (-0.36, -0.20),
        (0, 0, 1): (-0.36, 0.20),
        (0, 1, 0): (0.05, -0.28),
        (0, 1, 1): (-0.26, 0.22),
        (1, 0, 0): (-0.34, 0.16),
        (1, 0, 1): (-0.34, 0.18),
        (1, 1, 0): (0.38, -0.10),
        (1, 1, 1): (0.38, 0.18),
    }

    for x_shift, B_set, cyc, col, title_top, sub_bot, is_diag in cube_specs:
        assert frozenset(cyc) == B_set
        P = {p: cpos(p, x_shift) for p in pts}

        # Shaded polygon for B_m
        xy = np.array([P[q] for q in cyc])
        ax1.add_patch(Polygon(xy, closed=True, facecolor=col, edgecolor=col, lw=2.2, alpha=0.26, zorder=2))

        # All 12 cube edges
        for p, q in it.combinations(pts, 2):
            if sum(abs(a - b) for a, b in zip(p, q)) == 1:
                if frozenset({p, q}) == X:
                    ax1.plot(*zip(P[p], P[q]), color=ORANGE, lw=4.5, zorder=5, solid_capstyle="round")
                elif p in B_set and q in B_set:
                    ax1.plot(*zip(P[p], P[q]), color=col, lw=2.4, zorder=3)
                else:
                    ax1.plot(*zip(P[p], P[q]), color="#bbbbbb", lw=1.3, zorder=1)

        if is_diag:
            for p, q in [((0, 0, 0), (1, 1, 0)), ((0, 0, 1), (1, 1, 1))]:
                ax1.plot(*zip(P[p], P[q]), color=col, lw=2.2, ls="--", zorder=3)

        # Draw vertices and labels
        for p, (x, y) in P.items():
            in_X = p in X
            in_B = p in B_set
            if in_X:
                face, edge, r = ORANGE, DARK, 0.12
            elif in_B:
                face, edge, r = "white", col, 0.11
            else:
                face, edge, r = "white", "#999999", 0.075
            ax1.add_patch(plt.Circle((x, y), r, facecolor=face, edgecolor=edge, lw=2.0 if in_B else 1.3, zorder=6))
            if in_B:
                dx, dy = offsets[p]
                ax1.text(
                    x + dx,
                    y + dy,
                    bits(p),
                    ha="center",
                    va="center",
                    fontsize=9.6,
                    weight="bold",
                    color=ORANGE if in_X else col,
                    zorder=7,
                )

        cx = x_shift + 1.12
        ax1.text(cx, 3.12, title_top, ha="center", va="center", fontsize=10.8, weight="bold", color=col)
        ax1.text(cx, -0.72, sub_bot, ha="center", va="center", fontsize=9.6, weight="bold", color=col)

    ax1.text(
        4.45,
        -1.42,
        "Orange edge in each copy: $X = \\{000, 001\\}$ ($s = 2$), contained in $\\lambda_2 = 3$ blocks",
        ha="center",
        va="center",
        fontsize=10.2,
        weight="bold",
        color=ORANGE,
        bbox=dict(boxstyle="round,pad=0.28", facecolor="#fff9f0", edgecolor=ORANGE, lw=1.1),
    )

    ax1.set_xlim(-0.85, 9.60)
    ax1.set_ylim(-2.05, 3.65)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("(a) Cube $\\mathbb{F}_2^3$: the $\\lambda_2 = 3$ blocks containing $X = \\{000, 001\\}$", fontsize=12.5, pad=8)

    # Panel (b): Bipartite graph between the 6 triples Y and the 3 blocks B
    y_left = np.linspace(2.35, -0.85, 6)
    y_right = np.array([1.82, 0.75, -0.32])
    x_left, x_right = 0.0, 2.6
    b_colors = [BLUE, GREEN, PURPLE]

    for i, j in edges:
        col = b_colors[j]
        ax2.plot([x_left + 0.62, x_right - 0.78], [y_left[i], y_right[j]], color=col, lw=2.5, zorder=2)

    for i, Y in enumerate(triples_Y):
        extra = next(iter(Y - X))
        col = b_colors[next(j for u, j in edges if u == i)]
        box = FancyBboxPatch(
            (x_left - 0.62, y_left[i] - 0.18),
            1.24,
            0.36,
            boxstyle="round,pad=0.04",
            facecolor="white",
            edgecolor=col,
            lw=1.8,
            zorder=3,
        )
        ax2.add_patch(box)
        ax2.text(
            x_left,
            y_left[i],
            f"$X \\cup \\{{{bits(extra)}\\}}$",
            ha="center",
            va="center",
            fontsize=10.5,
            color=DARK,
            zorder=4,
        )

    b_names = [
        "$B_1$: $\\{000,001,010,011\\}$",
        "$B_2$: $\\{000,001,100,101\\}$",
        "$B_3$: $\\{000,001,110,111\\}$",
    ]
    for j in range(3):
        col = b_colors[j]
        box = FancyBboxPatch(
            (x_right - 0.78, y_right[j] - 0.26),
            1.78,
            0.52,
            boxstyle="round,pad=0.05",
            facecolor=col,
             alpha=0.14,
            edgecolor=col,
            lw=2.0,
            zorder=3,
        )
        ax2.add_patch(box)
        ax2.plot(
            [x_right - 0.78, x_right + 1.00, x_right + 1.00, x_right - 0.78, x_right - 0.78],
            [y_right[j] - 0.26, y_right[j] - 0.26, y_right[j] + 0.26, y_right[j] + 0.26, y_right[j] - 0.26],
            color=col,
            lw=2.0,
            zorder=4,
        )
        ax2.text(
            x_right + 0.11,
            y_right[j] + 0.08,
            b_names[j],
            ha="center",
            va="center",
            fontsize=9.8,
            color=col,
            weight="bold",
            zorder=5,
        )
        ax2.text(
            x_right + 0.11,
            y_right[j] - 0.12,
            "degree $C(4-2, 3-2) = 2$",
            ha="center",
            va="center",
            fontsize=9.0,
            color=DARK,
            zorder=5,
        )

    ax2.text(
        x_left,
        2.78,
        "$6$ triples $Y \\supseteq X$\n(each of degree $\\lambda = 1$)",
        ha="center",
        va="center",
        fontsize=10.5,
        weight="bold",
        color=DARK,
    )
    ax2.text(
        x_right + 0.11,
        2.78,
        "$\\lambda_2 = 3$ blocks $B \\supseteq X$\n(each of degree $2$)",
        ha="center",
        va="center",
        fontsize=10.5,
        weight="bold",
        color=DARK,
    )
    ax2.text(
        1.25,
        -1.26,
        "Flag count: $6 \\times 1 = 6 = \\lambda_2 \\times 2 \\;\\Longrightarrow\\; \\lambda_2 = 6/2 = 3$",
        ha="center",
        va="center",
        fontsize=11,
        weight="bold",
        color=BLUE,
        bbox=dict(boxstyle="round,pad=0.3", facecolor="#f4f7fb", edgecolor=BLUE, lw=1.2),
    )

    ax2.set_xlim(-0.85, 3.80)
    ax2.set_ylim(-1.55, 3.15)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("(b) Bipartite double count of flags $(Y, B)$ above $X$", fontsize=12.5, pad=8)

    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths4_designs_double_count.png"), dpi=160, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Figure 25
def fig15_fisher_ag23(out):
    pts, blocks, classes = build_ag23()
    v, b = len(pts), len(blocks)
    M = np.zeros((v, b), dtype=int)
    for i, p in enumerate(pts):
        for j, B in enumerate(blocks):
            if p in B:
                M[i, j] = 1

    # Verify M and MM^T properties
    assert M.shape == (9, 12)
    assert np.all(M.sum(axis=1) == 4)
    assert np.all(M.sum(axis=0) == 3)
    G = M @ M.T
    expected_G = 3 * np.eye(9, dtype=int) + np.ones((9, 9), dtype=int)
    assert np.array_equal(G, expected_G)
    evals = np.round(np.linalg.eigvalsh(G)).astype(int)
    assert sorted(evals) == [3] * 8 + [12]
    det_G = int(round(np.linalg.det(G)))
    assert det_G == 12 * (3**8) == 78732
    assert np.linalg.matrix_rank(M) == np.linalg.matrix_rank(G) == 9 <= 12

    # Highlight rows p_1=(0,0) (index 0) and p_2=(1,0) (index 1); they share only B_1 (index 0)
    shared_cols = [j for j in range(b) if M[0, j] == 1 and M[1, j] == 1]
    assert shared_cols == [0]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.6, 5.4), gridspec_kw=dict(width_ratios=[1.28, 1.0]))

    # Panel (a): 9 x 12 incidence matrix M
    for i in range(v):
        y = v - 1 - i
        row_hl = i in (0, 1)
        if row_hl:
            ax1.add_patch(
                Rectangle((-0.5, y - 0.5), b, 1.0, facecolor="#fff4e6", edgecolor="none", zorder=1)
            )
        for j in range(b):
            val = M[i, j]
            shared = j == 0 and row_hl
            if shared:
                face, tc, fw = ORANGE, "white", "bold"
            elif val == 1 and row_hl:
                face, tc, fw = "#ffd8a8", DARK, "bold"
            elif val == 1:
                face, tc, fw = "#dbe4f0", BLUE, "bold"
            else:
                face, tc, fw = "white" if not row_hl else "#fff9f0", GREY, "normal"
            ax1.add_patch(
                Rectangle((j - 0.5, y - 0.5), 1.0, 1.0, facecolor=face, edgecolor="#cccccc", lw=0.8, zorder=2)
            )
            ax1.text(j, y, str(val), ha="center", va="center", fontsize=10, color=tc, weight=fw, zorder=3)

    # Outer border and parallel-class dividers
    ax1.add_patch(Rectangle((-0.5, -0.5), b, v, fill=False, edgecolor=DARK, lw=1.8, zorder=4))
    for div in (2.5, 5.5, 8.5):
        ax1.plot([div, div], [-0.5, v - 0.5], color=DARK, lw=1.8, zorder=4)

    # Row labels
    for i, p in enumerate(pts):
        y = v - 1 - i
        row_hl = i in (0, 1)
        ax1.text(
            -0.7,
            y,
            f"$p_{{{i+1}}}=({p[0]},{p[1]})$",
            ha="right",
            va="center",
            fontsize=9.5,
            color=ORANGE if row_hl else DARK,
            weight="bold" if row_hl else "normal",
        )

    # Column labels and parallel class headers
    for j in range(b):
        ax1.text(
            j,
            v - 0.15,
            f"$B_{{{j+1}}}$",
            ha="center",
            va="bottom",
            fontsize=8.8,
            color=ORANGE if j == 0 else DARK,
            weight="bold" if j == 0 else "normal",
        )
    for k_cls, (cname, _) in enumerate(classes):
        cx = 3 * k_cls + 1.0
        ax1.text(cx, v + 0.55, cname, ha="center", va="bottom", fontsize=9.8, color=BLUE, weight="bold")

    ax1.text(
        5.5,
        -1.35,
        "Row sum $r = 4$ ones per row; rows $p_1, p_2$ share $\\lambda = 1$ column ($B_1$, orange)",
        ha="center",
        va="center",
        fontsize=10.0,
        color=DARK,
    )
    ax1.set_xlim(-3.0, b - 0.2)
    ax1.set_ylim(-1.85, v + 1.25)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("(a) Incidence matrix $M$ ($9 \\times 12$) of $\\mathrm{AG}(2, 3)$", fontsize=12.5, pad=8)

    # Panel (b): 9 x 9 Gram matrix MM^T = 3I + J
    for i in range(v):
        y = v - 1 - i
        for j in range(v):
            val = G[i, j]
            is_diag = i == j
            is_hl = (i, j) in ((0, 1), (1, 0))
            if is_diag:
                face, tc = BLUE, "white"
            elif is_hl:
                face, tc = ORANGE, "white"
            else:
                face, tc = "#eef3f9", DARK
            ax2.add_patch(
                Rectangle((j - 0.5, y - 0.5), 1.0, 1.0, facecolor=face, edgecolor="#cccccc", lw=0.8, zorder=2)
            )
            ax2.text(j, y, str(val), ha="center", va="center", fontsize=10, color=tc, weight="bold", zorder=3)

    ax2.add_patch(Rectangle((-0.5, -0.5), v, v, fill=False, edgecolor=DARK, lw=1.8, zorder=4))
    for i in range(v):
        y = v - 1 - i
        ax2.text(-0.68, y, f"$p_{{{i+1}}}$", ha="right", va="center", fontsize=9.5, color=DARK)
        ax2.text(i, v - 0.15, f"$p_{{{i+1}}}$", ha="center", va="bottom", fontsize=9.5, color=DARK)

    ax2.text(
        4.0,
        v + 0.55,
        "$M M^T = (r - \\lambda)I + \\lambda J = 3I + J$",
        ha="center",
        va="bottom",
        fontsize=10.5,
        color=BLUE,
        weight="bold",
    )
    ax2.text(
        4.0,
        -1.35,
        "Eigenvalues: $12^1$ (on $j$) and $3^8$ (on $j^\\perp$)\n"
        "$\\det(M M^T) = 12 \\cdot 3^8 = 78{,}732 > 0 \\;\\Longrightarrow\\; \\mathrm{rank}(M) = 9 \\leq 12 = b$",
        ha="center",
        va="center",
        fontsize=9.8,
        color=DARK,
        bbox=dict(boxstyle="round,pad=0.28", facecolor="#f4f7fb", edgecolor=BLUE, lw=1.1),
    )

    ax2.set_xlim(-1.6, v - 0.2)
    ax2.set_ylim(-1.85, v + 1.25)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("(b) Gram matrix $M M^T$ ($9 \\times 9$, full rank $9$)", fontsize=12.5, pad=8)

    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths4_designs_fisher_ag23.png"), dpi=160, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Figure 26
def fig16_planes_count(out):
    # Check parameters for n = 3:
    # PG(2,3) = S(2, 4, 13): v = 13, k = 4, r = (13-1)/(4-1) = 4, leftover = 4 - 4 = 0
    v_pg, k_pg = 13, 4
    r_pg = (v_pg - 1) // (k_pg - 1)
    assert r_pg == 4 and r_pg - k_pg == 0

    # AG(2,3) = S(2, 3, 9): v = 9, k = 3, r = (9-1)/(3-1) = 4, leftover = 4 - 3 = 1
    pts_ag, blocks_ag, _ = build_ag23()
    x_ag = (1, 1)
    L_ag = frozenset({(0, 0), (1, 0), (2, 0)})
    assert L_ag in blocks_ag and x_ag not in L_ag
    lines_through_x = [B for B in blocks_ag if x_ag in B]
    assert len(lines_through_x) == 4
    hitting_L = [B for B in lines_through_x if len(B & L_ag) == 1]
    missing_L = [B for B in lines_through_x if len(B & L_ag) == 0]
    assert len(hitting_L) == 3 and len(missing_L) == 1
    assert missing_L[0] == frozenset({(0, 1), (1, 1), (2, 1)})

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.0, 5.1))

    # Panel (a): Local schematic of PG(2,3) = S(2,4,13)
    x_pos = (0.0, 1.85)
    y_xs = np.linspace(-1.5, 1.5, 4)
    y_pos = [(xx, 0.0) for xx in y_xs]

    # Line L_1
    ax1.plot([-1.95, 1.95], [0.0, 0.0], color=DARK, lw=3.2, zorder=2)
    ax1.text(2.05, 0.0, "$L_1$ ($k = 4$ points)", ha="left", va="center", fontsize=11, weight="bold", color=DARK)

    # 4 connecting lines from x to y_1..y_4
    for idx, (yx, yy) in enumerate(y_pos):
        ax1.plot(
            [x_pos[0], yx],
            [x_pos[1], yy],
            color=BLUE,
            lw=2.5,
            zorder=1,
        )
        ax1.add_patch(plt.Circle((yx, yy), 0.11, facecolor="white", edgecolor=BLUE, lw=2.2, zorder=4))
        ax1.text(yx, yy - 0.30, f"$y_{idx+1}$", ha="center", va="center", fontsize=11, color=DARK)

    ax1.add_patch(plt.Circle(x_pos, 0.13, facecolor=ORANGE, edgecolor=DARK, lw=2.2, zorder=5))
    ax1.text(x_pos[0] + 0.24, x_pos[1] + 0.12, "$x \\notin L_1$", ha="left", va="center", fontsize=11.5, weight="bold", color=ORANGE)

    ax1.text(
        0.5,
        -0.92,
        "$r = \\frac{13 - 1}{4 - 1} = 4$ lines through $x$, and $k = 4$ points on $L_1$:\n"
        "$4 - 4 = 0$ lines left over (every line through $x$ meets $L_1$)",
        ha="center",
        va="center",
        fontsize=10.0,
        color=DARK,
        bbox=dict(boxstyle="round,pad=0.28", facecolor="#f4f7fb", edgecolor=BLUE, lw=1.1),
    )
    ax1.set_xlim(-2.25, 3.45)
    ax1.set_ylim(-1.45, 2.45)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("(a) Schematic of $\\mathrm{PG}(2, 3) = S(2, 4, 13)$", fontsize=12.5, pad=8)

    # Panel (b): AG(2,3) = S(2,3,9) on the 3x3 grid with x = (1,1) and L = bottom row y = 0
    ax2.plot([-0.25, 2.25], [0.0, 0.0], color=DARK, lw=3.4, zorder=2)
    ax2.text(2.35, 0.0, "$L$ ($k = 3$)", ha="left", va="center", fontsize=11, weight="bold", color=DARK)

    # Three connecting lines through x=(1,1) hitting L's 3 points:
    conn_segments = [
        ((0.0, 0.0), (2.0, 2.0)),
        ((1.0, 0.0), (1.0, 2.0)),
        ((2.0, 0.0), (0.0, 2.0)),
    ]
    for (x1, y1), (x2, y2) in conn_segments:
        ax2.plot([x1, x2], [y1, y2], color=BLUE, lw=2.5, zorder=1)

    # Fourth line through x=(1,1): middle row y = 1, parallel to L
    ax2.plot([-0.30, 2.30], [1.0, 1.0], color=ORANGE, lw=4.0, zorder=3)
    ax2.text(
        2.35,
        1.0,
        "parallel line\n($1$ left over)",
        ha="left",
        va="center",
        fontsize=10.5,
        weight="bold",
        color=ORANGE,
    )

    for px, py in pts_ag:
        if (px, py) == x_ag:
            face, edge, r = ORANGE, DARK, 0.13
        elif py == 0:
            face, edge, r = "white", BLUE, 0.11
        elif py == 1:
            face, edge, r = "#ffe8cc", ORANGE, 0.11
        else:
            face, edge, r = "white", GREY, 0.10
        ax2.add_patch(plt.Circle((px, py), r, facecolor=face, edgecolor=edge, lw=2.0, zorder=4))
        if (px, py) == (1, 1):
            ax2.text(
                px + 0.42,
                py + 0.19,
                "$x=(1,1)$",
                ha="center",
                va="center",
                fontsize=10.2,
                weight="bold",
                color=ORANGE,
                bbox=dict(boxstyle="round,pad=0.10", facecolor="white", edgecolor="none", alpha=0.9),
                zorder=5,
            )
        else:
            dy_lab = -0.27 if py == 0 else 0.25
            ax2.text(
                px,
                py + dy_lab,
                f"$({px},{py})$",
                ha="center",
                va="center",
                fontsize=9.2,
                color=DARK,
                zorder=5,
            )

    ax2.text(
        1.25,
        -0.92,
        "$r = \\frac{9 - 1}{3 - 1} = 4$ lines through $x$, and $k = 3$ points on $L$:\n"
        "$4 - 3 = 1$ line left over through $x$ missing $L$ (orange)",
        ha="center",
        va="center",
        fontsize=10.0,
        color=DARK,
        bbox=dict(boxstyle="round,pad=0.28", facecolor="#fff9f0", edgecolor=ORANGE, lw=1.2),
    )
    ax2.set_xlim(-1.45, 4.25)
    ax2.set_ylim(-1.45, 2.45)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("(b) Grid of $\\mathrm{AG}(2, 3) = S(2, 3, 9)$", fontsize=12.5, pad=8)

    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths4_designs_planes_count.png"), dpi=160, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Figure 27
def fig17_building(out):
    pts, blocks = build_ag32()
    x0 = (0, 0, 0)
    assert pts[0] == x0
    other_pts = pts[1:]

    # Blocks containing x0 (7 blocks), ordered lexicographically
    blocks_in = sorted([B for B in blocks if x0 in B], key=lambda B: sorted(B))
    assert len(blocks_in) == 7
    # Parallel partner of each block through x0 is its complement P \ B
    blocks_out = [frozenset(pts) - B for B in blocks_in]
    assert set(blocks_out) == {B for B in blocks if x0 not in B}
    ordered_blocks = blocks_in + blocks_out

    # Build 8 x 14 incidence matrix
    M = np.zeros((8, 14), dtype=int)
    for i, p in enumerate(pts):
        for j, B in enumerate(ordered_blocks):
            if p in B:
                M[i, j] = 1

    # Assert derived design S_x (bottom-left 7x7) is 2-(7,3,1) Fano plane
    M_der = M[1:, :7]
    assert M_der.shape == (7, 7)
    assert np.all(M_der.sum(axis=0) == 3) and np.all(M_der.sum(axis=1) == 3)
    assert np.array_equal(M_der @ M_der.T, 2 * np.eye(7, dtype=int) + np.ones((7, 7), dtype=int))

    # Assert external structure S^x (bottom-right 7x7) is 2-(7,4,2) and equals 1 - M_der
    M_ext = M[1:, 7:]
    assert M_ext.shape == (7, 7)
    assert np.array_equal(M_ext, 1 - M_der)
    assert np.all(M_ext.sum(axis=0) == 4) and np.all(M_ext.sum(axis=1) == 4)
    assert np.array_equal(M_ext @ M_ext.T, 2 * np.eye(7, dtype=int) + 2 * np.ones((7, 7), dtype=int))

    # Verify lambda_i^j triangles for S(3,4,8) and AG(2,3)=S(2,3,9)
    tri_s348 = {}
    for m_level in range(4):
        for j in range(m_level + 1):
            i = m_level - j
            c1 = lambda_ij_closed(8, 4, 3, 1, i, j)
            c2 = lambda_ij_ie(8, 4, 3, 1, i, j)
            # Direct count on AG(3,2) blocks
            U = set(pts[:i])
            W = set(pts[i : i + j])
            c3 = sum(1 for B in blocks if U <= B and not (W & B))
            assert c1 == c2 == c3
            tri_s348[(i, j)] = c1
    for m_level in range(3):
        for j in range(m_level + 1):
            i = m_level - j
            assert tri_s348[(i, j)] == tri_s348[(i + 1, j)] + tri_s348[(i, j + 1)]

    _, blocks_ag23, _ = build_ag23()
    pts_ag23 = [(x, y) for y in range(3) for x in range(3)]
    tri_ag23 = {}
    for m_level in range(3):
        for j in range(m_level + 1):
            i = m_level - j
            c1 = lambda_ij_closed(9, 3, 2, 1, i, j)
            c2 = lambda_ij_ie(9, 3, 2, 1, i, j)
            U = set(pts_ag23[:i])
            W = set(pts_ag23[i : i + j])
            c3 = sum(1 for B in blocks_ag23 if U <= B and not (W & B))
            assert c1 == c2 == c3
            tri_ag23[(i, j)] = c1
    for m_level in range(2):
        for j in range(m_level + 1):
            i = m_level - j
            assert tri_ag23[(i, j)] == tri_ag23[(i + 1, j)] + tri_ag23[(i, j + 1)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.0, 5.5), gridspec_kw=dict(width_ratios=[1.22, 1.05]))

    # Panel (a): 8 x 14 split incidence matrix of AG(3,2)
    for i in range(8):
        y = 7 - i
        for j in range(14):
            val = M[i, j]
            if i == 0:
                face = "#e9ecef" if val == 1 else "#f8f9fa"
                tc = DARK if val == 1 else GREY
                fw = "bold" if val == 1 else "normal"
            elif j < 7:
                face = "#dbe4f0" if val == 1 else "white"
                tc = BLUE if val == 1 else GREY
                fw = "bold" if val == 1 else "normal"
            else:
                face = "#ffe8cc" if val == 1 else "white"
                tc = ORANGE if val == 1 else GREY
                fw = "bold" if val == 1 else "normal"
            ax1.add_patch(
                Rectangle((j - 0.5, y - 0.5), 1.0, 1.0, facecolor=face, edgecolor="#cccccc", lw=0.8, zorder=2)
            )
            ax1.text(j, y, str(val), ha="center", va="center", fontsize=9.8, color=tc, weight=fw, zorder=3)

    # Outer border and split lines
    ax1.add_patch(Rectangle((-0.5, -0.5), 14, 8, fill=False, edgecolor=DARK, lw=1.8, zorder=4))
    ax1.plot([6.5, 6.5], [-0.5, 7.5], color=DARK, lw=2.2, zorder=4)
    ax1.plot([-0.5, 13.5], [6.5, 6.5], color=DARK, lw=2.0, ls="--", zorder=4)

    # Row labels
    for i, p in enumerate(pts):
        y = 7 - i
        lab_str = f"$x={bits(p)}$" if i == 0 else bits(p)
        ax1.text(
            -0.68,
            y,
            lab_str,
            ha="right",
            va="center",
            fontsize=9.5,
            weight="bold" if i == 0 else "normal",
            color=DARK,
        )

    # Column labels B_1..B_7 and B'_1..B'_7
    for j in range(7):
        ax1.text(j, 7.65, f"$B_{{{j+1}}}$", ha="center", va="bottom", fontsize=9.0, color=BLUE, weight="bold")
        ax1.text(
            j + 7, 7.65, f"$B'_{{{j+1}}}$", ha="center", va="bottom", fontsize=9.0, color=ORANGE, weight="bold"
        )

    ax1.text(3.0, 8.35, "$r = 7$ blocks with $x \\in B$", ha="center", va="bottom", fontsize=10.2, color=BLUE, weight="bold")
    ax1.text(10.0, 8.35, "$b - r = 7$ blocks with $x \\notin B$", ha="center", va="bottom", fontsize=10.2, color=ORANGE, weight="bold")

    ax1.text(
        3.0,
        -1.22,
        "Derived design $\\mathcal{S}_x = \\mathrm{PG}(2, 2)$\n$2$-$(7, 3, 1)$-design (Fano plane)",
        ha="center",
        va="center",
        fontsize=9.8,
        color=BLUE,
        weight="bold",
        bbox=dict(boxstyle="round,pad=0.24", facecolor="#f4f7fb", edgecolor=BLUE, lw=1.1),
    )
    ax1.text(
        10.0,
        -1.22,
        "External structure $\\mathcal{S}^x$\n$2$-$(7, 4, 2)$-design ($B'_m = \\mathcal{P} \\backslash B_m$)",
        ha="center",
        va="center",
        fontsize=9.8,
        color=ORANGE,
        weight="bold",
        bbox=dict(boxstyle="round,pad=0.24", facecolor="#fff9f0", edgecolor=ORANGE, lw=1.1),
    )

    ax1.set_xlim(-2.35, 13.8)
    ax1.set_ylim(-1.95, 9.05)
    ax1.set_aspect("equal")
    ax1.axis("off")
    ax1.set_title("(a) Split of $\\mathrm{AG}(3, 2) = S(3, 4, 8)$ at $x = 000$", fontsize=12.5, pad=8)

    # Panel (b): Two Pascal triangles of lambda_i^j (top: S(3,4,8), bottom: AG(2,3))
    def draw_triangle(ax, tri, max_m, y_top, dy, dx, title_str, special_labels, col_main):
        ax.text(0.0, y_top + 0.52, title_str, ha="center", va="center", fontsize=10.8, weight="bold", color=col_main)
        pos = {}
        for m_level in range(max_m + 1):
            for j in range(m_level + 1):
                i = m_level - j
                xx = (j - m_level / 2.0) * dx
                yy = y_top - m_level * dy
                pos[(i, j)] = (xx, yy)

        # Draw edges showing each parent is sum of two children below
        for m_level in range(max_m):
            for j in range(m_level + 1):
                i = m_level - j
                x_p, y_p = pos[(i, j)]
                for ch in [(i + 1, j), (i, j + 1)]:
                    x_c, y_c = pos[ch]
                    ax.plot([x_p, x_c], [y_p - 0.18, y_c + 0.18], color=GREY, lw=1.4, zorder=1)

        for (i, j), (xx, yy) in pos.items():
            val = tri[(i, j)]
            box = FancyBboxPatch(
                (xx - 0.34, yy - 0.17),
                0.68,
                0.34,
                boxstyle="round,pad=0.03",
                facecolor="white",
                edgecolor=col_main,
                lw=1.6,
                zorder=3,
            )
            ax.add_patch(box)
            ax.text(
                xx,
                yy,
                f"$\\lambda_{{{i}}}^{{{j}}}={val}$",
                ha="center",
                va="center",
                fontsize=9.3,
                weight="bold",
                color=DARK,
                zorder=4,
            )
            if (i, j) in special_labels:
                slab, sdx, sdy, sha = special_labels[(i, j)]
                ax.text(xx + sdx, yy + sdy, slab, ha=sha, va="center", fontsize=8.8, color=col_main, weight="bold")

    labels_s348 = {
        (0, 0): ("$b = 14$", 0.44, 0.0, "left"),
        (1, 0): ("$r = 7$", -0.44, 0.0, "right"),
        (0, 1): ("$b - r = 7$", 0.44, 0.0, "left"),
        (3, 0): ("$\\lambda = 1$", -0.44, 0.0, "right"),
    }
    draw_triangle(
        ax2,
        tri_s348,
        3,
        y_top=3.55,
        dy=0.72,
        dx=1.08,
        title_str="$S(3, 4, 8)$ ($t = 3$: each entry $=$ sum of two below)",
        special_labels=labels_s348,
        col_main=BLUE,
    )

    labels_ag23 = {
        (0, 0): ("$b = 12$", 0.44, 0.0, "left"),
        (1, 0): ("$r = 4$", -0.44, 0.0, "right"),
        (0, 1): ("$b - r = 8$", 0.44, 0.0, "left"),
        (2, 0): ("$\\lambda = 1$", -0.44, 0.0, "right"),
        (1, 1): ("$r - \\lambda = 3$", 0.0, -0.34, "center"),
        (0, 2): ("$b - 2r + \\lambda = 5$", 0.44, 0.0, "left"),
    }
    draw_triangle(
        ax2,
        tri_ag23,
        2,
        y_top=0.15,
        dy=0.72,
        dx=1.18,
        title_str="$\\mathrm{AG}(2, 3) = S(2, 3, 9)$ ($t = 2$)",
        special_labels=labels_ag23,
        col_main=ORANGE,
    )

    ax2.set_xlim(-2.65, 2.95)
    ax2.set_ylim(-1.95, 4.35)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("(b) Pascal triangles of $\\lambda_i^j = \\lambda_{i+1}^j + \\lambda_i^{j+1}$", fontsize=12.5, pad=8)

    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths4_designs_building.png"), dpi=160, facecolor="white")
    plt.close(fig)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    fig14_double_count(out)
    fig15_fisher_ag23(out)
    fig16_planes_count(out)
    fig17_building(out)
    print("Generated 4 figures in", out)


if __name__ == "__main__":
    main()
