"""Figures for the chapter "Hyperplanes and Projective Embeddings".

Usage: python make_embeddings_figures.py OUTPUT_DIR

Writes maths4_embeddings_projection.png:
  (a) the 3x3 grid x0x3 + x1x2 = 0 in PG(3,2), projected from c = (1,0,0,1):
      three secants through c each carry two grid points, so 9 points give 6 shadows;
  (b) Q(4,2): x0^2 + x1x2 + x3x4 = 0 in PG(4,2) and its nucleus N = (1,0,0,0,0):
      each of the 15 lines through N meets the quadric in exactly one point.
All incidences are computed, not typed in.
"""
import itertools
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def pts(n):
    return [v for v in itertools.product((0, 1), repeat=n) if any(v)]


def add(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))


def lab(v):
    return "".join(str(x) for x in v)


def grid_panel(ax):
    # the earlier notes' table: rows g1, g2, g3 and columns h1, h2, h3
    table = [[(1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 0, 0)],
             [(0, 0, 1, 0), (0, 0, 0, 1), (0, 0, 1, 1)],
             [(1, 0, 1, 0), (0, 1, 0, 1), (1, 1, 1, 1)]]
    for row in table:
        for p in row:
            assert (p[0] * p[3] + p[1] * p[2]) % 2 == 0
    pos = {}
    for r, row in enumerate(table):
        for col, p in enumerate(row):
            pos[p] = np.array([1.6 * col, -1.6 * r])
    c = (1, 0, 0, 1)
    assert (c[0] * c[3] + c[1] * c[2]) % 2 == 1
    grid = set(pos)
    pairs = sorted({frozenset((p, add(p, c))) for p in grid if add(p, c) in grid}, key=sorted)
    assert len(pairs) == 3
    colours = ["#d62728", "#1f77b4", "#2ca02c"]
    # grid lines
    for r in range(3):
        ax.plot([0, 3.2], [-1.6 * r] * 2, color="0.75", lw=2.5, zorder=1)
        ax.plot([1.6 * r] * 2, [0, -3.2], color="0.75", lw=2.5, zorder=1)
    # By the symmetry of this table the three secant lines through the pairs meet in one
    # point of the drawing, so the secants can be drawn straight; c sits at that point.
    def meet(p1, p2, p3, p4):
        a = np.array([p2 - p1, p3 - p4]).T
        lam = np.linalg.solve(a, p3 - p1)
        return p1 + lam[0] * (p2 - p1)
    prs = [sorted(pr) for pr in pairs]
    cpos = meet(pos[prs[0][0]], pos[prs[0][1]], pos[prs[1][0]], pos[prs[1][1]])
    assert np.allclose(cpos, meet(pos[prs[0][0]], pos[prs[0][1]], pos[prs[2][0]], pos[prs[2][1]]))
    for (pair, col) in zip(prs, colours):
        ends = [pos[pair[0]], pos[pair[1]], cpos]
        xs = sorted(ends, key=lambda e: (e[0], e[1]))
        ax.plot([xs[0][0], xs[-1][0]], [xs[0][1], xs[-1][1]], ls="--", color=col, lw=1.6, zorder=2)
    fibre_colour = {}
    for pair, col in zip(pairs, colours):
        for p in pair:
            fibre_colour[p] = col
    for p, xy in pos.items():
        col = fibre_colour.get(p, "black")
        ax.scatter(*xy, s=170, color=col, zorder=3, edgecolor="black", linewidth=0.6)
        ax.annotate(lab(p), xy, xytext=(0, 13), textcoords="offset points", ha="center", fontsize=9.5,
                    bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.85), zorder=4)
    ax.scatter(*cpos, s=260, marker="*", color="#ff9f1c", edgecolor="black", zorder=3)
    ax.annotate("c = 1001", cpos, xytext=(14, -14), textcoords="offset points", ha="left", fontsize=10.5,
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))
    ax.text(1.6, -4.25, "9 grid points, 6 shadows:\nthe three coloured pairs share a shadow",
            ha="center", va="top", fontsize=10)
    ax.set_title("(a) The grid in PG(3,2), projected from c", fontsize=12)
    ax.set_xlim(-0.9, 4.6)
    ax.set_ylim(-4.9, 0.9)
    ax.set_aspect("equal")
    ax.axis("off")


def nucleus_panel(ax):
    def q(x):
        return (x[0] * x[0] + x[1] * x[2] + x[3] * x[4]) % 2
    N = (1, 0, 0, 0, 0)
    Q = sorted(p for p in pts(5) if q(p) == 0)
    assert len(Q) == 15
    for p in Q:
        assert q(add(p, N)) == 1  # the third point of the line Np is off the quadric
    ang = np.linspace(0, 2 * np.pi, 16)[:-1] + np.pi / 2
    labelled = {0}
    for k, (p, a) in enumerate(zip(Q, ang)):
        d = np.array([np.cos(a), np.sin(a)])
        ax.plot([0, 2.25 * d[0]], [0, 2.25 * d[1]], color="0.7", lw=1.2, zorder=1)
        ax.scatter(*(1.15 * d), s=70, color="#1f77b4", edgecolor="black", linewidth=0.5, zorder=3)
        ax.scatter(*(2.0 * d), s=70, facecolor="white", edgecolor="black", linewidth=0.9, zorder=3)
        if k in labelled:
            ax.plot([0, 2.25 * d[0]], [0, 2.25 * d[1]], color="#ff9f1c", lw=2.6, zorder=2)
            ax.text(-2.65, 2.55, "a line through N:\n%s (N), %s (on Q), %s (off Q)"
                    % (lab(N), lab(p), lab(add(p, N))), fontsize=9.5, ha="left", va="top")
    ax.scatter(0, 0, s=260, marker="*", color="#ff9f1c", edgecolor="black", zorder=4)
    ax.annotate("N = 10000", (0, 0), xytext=(0, -17), textcoords="offset points", ha="center", fontsize=10,
                bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none"))
    ax.scatter([], [], s=60, color="#1f77b4", edgecolor="black", label="on Q(4,2)")
    ax.scatter([], [], s=60, facecolor="white", edgecolor="black", label="off Q(4,2)")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.06), ncol=2, frameon=False, fontsize=10)
    ax.set_title("(b) Q(4,2) in PG(4,2), projected from its nucleus N", fontsize=12)
    ax.set_xlim(-2.7, 2.7)
    ax.set_ylim(-2.7, 2.7)
    ax.set_aspect("equal")
    ax.axis("off")


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.6), facecolor="white")
    grid_panel(axes[0])
    nucleus_panel(axes[1])
    fig.tight_layout()
    fig.savefig(out / "maths4_embeddings_projection.png", dpi=150, facecolor="white")
    print("wrote", out / "maths4_embeddings_projection.png")


if __name__ == "__main__":
    main()
