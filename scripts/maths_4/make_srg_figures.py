"""Figures for the chapter on strongly regular and distance-regular graphs.

Usage: python make_srg_figures.py OUTPUT_DIR

Writes
  maths4_srg_petersen_layers.png  the Petersen graph seen from one vertex
  maths4_srg_cube_shells.png      the cube graph in distance shells from 000
"""
import itertools
import os
import sys

import matplotlib
import numpy as np

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

BLACK = "#222222"
GREY = "#9a9a9a"
BLUE = "#1f5fa8"
ORANGE = "#d9730d"
GREEN = "#2e8b57"


def node(ax, xy, label, face="white", edge=BLACK, size=0.23, fs=12):
    circ = plt.Circle(xy, size, facecolor=face, edgecolor=edge, lw=1.6, zorder=3)
    ax.add_patch(circ)
    ax.text(xy[0], xy[1], label, ha="center", va="center", fontsize=fs, zorder=4)


def line(ax, p, q, color=BLACK, lw=1.6, ls="-"):
    ax.plot([p[0], q[0]], [p[1], q[1]], color=color, lw=lw, ls=ls, zorder=1)


def arc(ax, p, q, rad, color=GREY, lw=1.4):
    patch = FancyArrowPatch(p, q, connectionstyle=f"arc3,rad={rad}",
                            arrowstyle="-", color=color, lw=lw, zorder=1)
    ax.add_patch(patch)


def petersen_layers(outdir):
    """Petersen graph (2-subsets of {1..5}, joined when disjoint) seen from x = 12."""
    lab = lambda s: "".join(str(i) for i in sorted(s))
    x = frozenset({1, 2})
    middle = [frozenset(s) for s in ({3, 4}, {3, 5}, {4, 5})]
    # each middle vertex has two neighbours below; put them under it
    bottom = []
    for m in middle:
        kids = sorted((frozenset(s) for s in itertools.combinations(range(1, 6), 2)
                       if not (frozenset(s) & m) and frozenset(s) != x),
                      key=lambda s: sorted(s))
        bottom.extend(kids)
    pos = {x: (0.0, 4.0)}
    for i, m in enumerate(middle):
        pos[m] = (-3.0 + 3.0 * i, 2.2)
    for i, b in enumerate(bottom):
        pos[b] = (-3.75 + 1.5 * i, 0.4)

    fig, ax = plt.subplots(figsize=(8.6, 5.6))
    # x to its neighbours
    for m in middle:
        line(ax, pos[x], pos[m], color=BLACK, lw=1.8)
    # neighbours to non-neighbours: the k(k - lambda - 1) edges that the count uses
    for m in middle:
        for b in bottom:
            if not (m & b):
                line(ax, pos[m], pos[b], color=ORANGE, lw=2.4)
    # edges among the six non-neighbours, drawn as arcs below the row
    drawn = set()
    for b1, b2 in itertools.combinations(bottom, 2):
        if not (b1 & b2):
            i, j = sorted((bottom.index(b1), bottom.index(b2)))
            # a parabola below the row, deeper for longer spans
            depth = {1: 0.55, 3: 1.15, 5: 2.5}[j - i]
            (x1, y1), (x2, y2) = pos[bottom[i]], pos[bottom[j]]
            ts = np.linspace(0, 1, 80)
            xs = x1 + (x2 - x1) * ts
            ys = y1 - 4 * depth * ts * (1 - ts)
            ax.plot(xs, ys, color=GREY, lw=1.5, zorder=1)
            drawn.add((b1, b2))
    assert len(drawn) == 6
    node(ax, pos[x], lab(x), face="#e8eef8", edge=BLUE)
    for m in middle:
        node(ax, pos[m], lab(m))
    for b in bottom:
        node(ax, pos[b], lab(b))

    ax.text(4.35, 4.0, "$x$", fontsize=13, va="center")
    ax.text(4.35, 2.2, "3 neighbours of $x$\nno edges among them ($\\lambda = 0$)",
            fontsize=11, va="center")
    ax.text(4.35, 0.4, "6 non-neighbours of $x$\neach has one neighbour\nin the row above ($\\mu = 1$)",
            fontsize=11, va="center")
    ax.text(-4.3, -2.6,
            "orange: $3 \\times 2 = 6$ edges counted from above, $6 \\times 1 = 6$ counted from below;"
            "  grey: the other edges",
            fontsize=10.5, va="center", color="#444444")
    ax.set_xlim(-4.5, 8.4)
    ax.set_ylim(-2.9, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(os.path.join(outdir, "maths4_srg_petersen_layers.png"), dpi=200,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


def cube_shells(outdir):
    """Cube graph: binary triples, joined when exactly one coordinate differs."""
    verts = ["".join(p) for p in itertools.product("01", repeat=3)]
    wt = lambda s: s.count("1")
    shells = [[v for v in ["000"]],
              ["100", "010", "001"],
              ["110", "101", "011"],
              ["111"]]
    pos = {}
    for i, sh in enumerate(shells):
        n = len(sh)
        for j, v in enumerate(sh):
            pos[v] = (-(n - 1) * 1.15 + 2.3 * j, 6.0 - 2.0 * i)
    y = "110"
    fig, ax = plt.subplots(figsize=(8.6, 6.4))
    for a, b in itertools.combinations(verts, 2):
        if sum(c != d for c, d in zip(a, b)) == 1:
            if y in (a, b):
                other = b if a == y else a
                color = GREEN if wt(other) < wt(y) else ORANGE
                line(ax, pos[a], pos[b], color=color, lw=2.8)
            else:
                line(ax, pos[a], pos[b], color=GREY, lw=1.5)
    for v in verts:
        if v == "000":
            node(ax, pos[v], v, face="#e8eef8", edge=BLUE, size=0.36, fs=11)
        elif v == y:
            node(ax, pos[v], v, face="#fff1e0", edge=ORANGE, size=0.36, fs=11)
        else:
            node(ax, pos[v], v, size=0.36, fs=11)
    info = [("$\\Gamma_0(x)$", 1, "$b_0 = 3$"),
            ("$\\Gamma_1(x)$", 3, "$c_1 = 1,\\ a_1 = 0,\\ b_1 = 2$"),
            ("$\\Gamma_2(x)$", 3, "$c_2 = 2,\\ a_2 = 0,\\ b_2 = 1$"),
            ("$\\Gamma_3(x)$", 1, "$c_3 = 3,\\ a_3 = 0$")]
    for i, (name, size, nums) in enumerate(info):
        yy = 6.0 - 2.0 * i
        ax.text(3.6, yy + 0.22, f"{name}: $k_{i} = {size}$", fontsize=12, va="center")
        ax.text(3.6, yy - 0.3, nums, fontsize=11, va="center", color="#444444")
    ax.text(-3.9, -1.2,
            "$x = 000$ (blue).  From $y = 110$: green edges step back ($c_2 = 2$), "
            "the orange edge steps out ($b_2 = 1$).",
            fontsize=10.5, va="center", color="#444444")
    ax.set_xlim(-4.0, 7.6)
    ax.set_ylim(-1.6, 6.6)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.savefig(os.path.join(outdir, "maths4_srg_cube_shells.png"), dpi=200,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: make_srg_figures.py OUTPUT_DIR")
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    petersen_layers(out)
    cube_shells(out)
    print("wrote figures to", out)
