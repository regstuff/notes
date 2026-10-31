"""Figures for the chapter "Graphs and Point-Line Geometries" (Maths 4, incidence geometry).

Usage: python make_graphs_figures.py OUTPUT_DIR

Writes five PNGs into OUTPUT_DIR:
  maths4_graphs_valency.png          triangle, hexagon and two triangles (all valency 2)
  maths4_graphs_petersen.png         Petersen graph as pentagon and star, labelled by 2-subsets
  maths4_graphs_fano_heawood.png     Fano plane beside its incidence graph (the Heawood graph)
  maths4_graphs_grid_hyperplanes.png the 3x3 grid with a cross and an ovoid
  maths4_graphs_alternating_path.png a collinearity path in the grid and its alternating path

Every drawing is checked by computation before it is drawn:
  * the Petersen drawing is asserted to join exactly the disjoint 2-subsets of {1,...,5};
  * the Fano lines are the kernels a.x = 0 over F_2, and the Heawood drawing is asserted
    to be the incidence graph (14 vertices, 21 edges, girth 6, diameter 3);
  * the grid's hyperplanes are enumerated (9 crosses, 6 ovoids) and the drawn sets are
    asserted to be among them.
"""

import itertools as it
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

BLUE = "#1f3b73"
ORANGE = "#d9730d"
GREY = "#9a9a9a"
EDGE = dict(color="#222222", lw=2.2, zorder=1, solid_capstyle="round")


def node(ax, x, y, label="", r=0.13, face="white", edge="#222222", fs=11, square=False, lw=2.0):
    if square:
        patch = plt.Rectangle((x - r, y - r), 2 * r, 2 * r, facecolor=face, edgecolor=edge, lw=lw, zorder=3)
    else:
        patch = plt.Circle((x, y), r, facecolor=face, edgecolor=edge, lw=lw, zorder=3)
    ax.add_patch(patch)
    if label:
        ax.text(x, y, label, ha="center", va="center", fontsize=fs, zorder=4)


def finish(ax, title=None):
    ax.set_aspect("equal")
    ax.axis("off")
    if title:
        ax.set_title(title, fontsize=13, pad=8)


# ---------------------------------------------------------------- valency
def fig_valency(out):
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.6), gridspec_kw=dict(width_ratios=[1, 1.15, 1.6]))

    def ring(ax, n, cx, cy, rad, start=np.pi / 2):
        pts = [(cx + rad * np.cos(start + 2 * np.pi * k / n), cy + rad * np.sin(start + 2 * np.pi * k / n)) for k in range(n)]
        for k in range(n):
            (x1, y1), (x2, y2) = pts[k], pts[(k + 1) % n]
            ax.plot([x1, x2], [y1, y2], **EDGE)
        for x, y in pts:
            node(ax, x, y, r=0.09)
        return pts

    ring(axes[0], 3, 0, 0, 0.8)
    axes[0].set_xlim(-1.1, 1.1)
    axes[0].set_ylim(-0.8, 1.1)
    finish(axes[0], "triangle $C_3 = K_3$")
    ring(axes[1], 6, 0, 0, 0.9)
    axes[1].set_xlim(-1.2, 1.2)
    axes[1].set_ylim(-1.1, 1.1)
    finish(axes[1], "hexagon $C_6$")
    ring(axes[2], 3, -0.95, 0, 0.75)
    ring(axes[2], 3, 0.95, 0, 0.75)
    axes[2].set_xlim(-2.0, 2.0)
    axes[2].set_ylim(-0.8, 1.1)
    finish(axes[2], "two triangles $2K_3$")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths4_graphs_valency.png"), dpi=160, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Petersen
def lab(s):
    return "".join(str(i) for i in sorted(s))


def fig_petersen(out):
    outer = [frozenset(s) for s in [(1, 2), (3, 4), (5, 1), (2, 3), (4, 5)]]
    # inner vertex k: the 2-subset disjoint from outer[k] that is not an outer neighbour of it
    inner = []
    for k, s in enumerate(outer):
        nbrs = {outer[(k - 1) % 5], outer[(k + 1) % 5]}
        cand = [frozenset(t) for t in it.combinations(range(1, 6), 2) if not (frozenset(t) & s) and frozenset(t) not in nbrs]
        assert len(cand) == 1
        inner.append(cand[0])
    assert len(set(outer) | set(inner)) == 10
    ang = [np.pi / 2 - 2 * np.pi * k / 5 for k in range(5)]
    pos = {}
    for k in range(5):
        pos[outer[k]] = (1.6 * np.cos(ang[k]), 1.6 * np.sin(ang[k]))
        pos[inner[k]] = (0.8 * np.cos(ang[k]), 0.8 * np.sin(ang[k]))
    edges = [(a, b) for a, b in it.combinations(pos, 2) if not (a & b)]
    assert len(edges) == 15
    # the drawn edges are outer ring, spokes and inner pentagram
    drawn = {frozenset((outer[k], outer[(k + 1) % 5])) for k in range(5)}
    drawn |= {frozenset((outer[k], inner[k])) for k in range(5)}
    drawn |= {frozenset((inner[k], inner[(k + 2) % 5])) for k in range(5)}
    assert drawn == {frozenset(e) for e in edges}, "drawing is not the disjointness graph"
    G = nx.Graph(edges)
    assert nx.diameter(G) == 2 and nx.girth(G) == 5

    fig, ax = plt.subplots(figsize=(5.2, 5.2))
    for a, b in edges:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        ax.plot([x1, x2], [y1, y2], **EDGE)
    for v, (x, y) in pos.items():
        node(ax, x, y, lab(v), r=0.2, fs=13)
    ax.set_xlim(-1.95, 1.95)
    ax.set_ylim(-1.6, 1.95)
    finish(ax)
    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths4_graphs_petersen.png"), dpi=160, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- Fano and Heawood
def bits(v):
    return "".join(str(c) for c in v)


def fig_fano_heawood(out):
    pts = [v for v in it.product([0, 1], repeat=3) if any(v)]
    lines = {a: frozenset(p for p in pts if sum(x * y for x, y in zip(a, p)) % 2 == 0) for a in pts}
    assert all(len(L) == 3 for L in lines.values())

    # Fano drawing: triangle 100, 010, 001; side midpoints; centre 111
    P = {
        (1, 0, 0): (0.0, 1.55),
        (0, 1, 0): (-1.35, -0.78),
        (0, 0, 1): (1.35, -0.78),
        (1, 1, 0): (-0.675, 0.385),
        (0, 1, 1): (0.0, -0.78),
        (1, 0, 1): (0.675, 0.385),
        (1, 1, 1): (0.0, 0.0),
    }
    for L in lines.values():
        assert L <= set(P)

    fig, axes = plt.subplots(1, 2, figsize=(11.5, 5.4), gridspec_kw=dict(width_ratios=[1, 1.15]))
    ax = axes[0]
    circle_line = frozenset({(1, 1, 0), (0, 1, 1), (1, 0, 1)})
    assert circle_line in set(lines.values())
    for L in lines.values():
        if L == circle_line:
            continue
        xy = np.array([P[p] for p in L])
        # draw the segment between the two extreme points
        d = max(it.combinations(range(3), 2), key=lambda ij: np.linalg.norm(xy[ij[0]] - xy[ij[1]]))
        ax.plot(*zip(xy[d[0]], xy[d[1]]), color=BLUE, lw=2.4, zorder=1)
    ax.add_patch(plt.Circle((0, 0), 0.78, fill=False, edgecolor=BLUE, lw=2.4, zorder=1))
    for p, (x, y) in P.items():
        node(ax, x, y, r=0.07, face="black")
        off = {(1, 0, 0): (0.0, 0.2), (0, 1, 0): (-0.15, -0.2), (0, 0, 1): (0.15, -0.2), (1, 1, 0): (-0.3, 0.12),
               (0, 1, 1): (0.0, -0.22), (1, 0, 1): (0.3, 0.12), (1, 1, 1): (0.3, 0.0)}[p]
        ax.text(x + off[0], y + off[1], bits(p), ha="center", va="center", fontsize=12)
    ax.set_xlim(-1.7, 1.7)
    ax.set_ylim(-1.15, 1.85)
    finish(ax, "Fano plane: points of $PG(2,2)$")

    # Heawood: find a Hamiltonian cycle alternating points and lines
    B = nx.Graph()
    for a, L in lines.items():
        for p in L:
            B.add_edge(("p", p), ("L", a))
    assert B.number_of_nodes() == 14 and B.number_of_edges() == 21
    assert nx.girth(B) == 6 and nx.diameter(B) == 3

    start = ("p", (1, 0, 0))

    def hams(path, seen):
        # all Hamiltonian cycles through start, as vertex lists
        if len(path) == 14:
            if B.has_edge(path[-1], path[0]):
                yield path
            return
        for nb in sorted(B[path[-1]]):
            if nb not in seen:
                yield from hams(path + [nb], seen | {nb})

    def lcf_ok(c):
        # chords of the symmetric drawing: offsets +5 and -5 alternately (LCF notation [5,-5]^7)
        idx = {v: k for k, v in enumerate(c)}
        return all({(idx[w] - k) % 14 for w in B[v]} - {1, 13} == ({5} if k % 2 == 0 else {9}) for k, v in enumerate(c))

    cyc = next(c for c in hams([start], {start}) if lcf_ok(c))
    ax = axes[1]
    pos = {v: (1.6 * np.cos(np.pi / 2 - 2 * np.pi * k / 14), 1.6 * np.sin(np.pi / 2 - 2 * np.pi * k / 14)) for k, v in enumerate(cyc)}
    for u, v in B.edges():
        (x1, y1), (x2, y2) = pos[u], pos[v]
        ax.plot([x1, x2], [y1, y2], **EDGE)
    for v, (x, y) in pos.items():
        if v[0] == "p":
            node(ax, x, y, r=0.07, face="black")
            lx, ly = 1.85 * x / 1.6, 1.85 * y / 1.6
            ax.text(lx, ly, bits(v[1]), ha="center", va="center", fontsize=11)
        else:
            node(ax, x, y, r=0.075, face="white", edge=BLUE, square=True, lw=2.2)
            lx, ly = 1.9 * x / 1.6, 1.9 * y / 1.6
            ax.text(lx, ly, "[" + bits(v[1]) + "]", ha="center", va="center", fontsize=11, color=BLUE)
    ax.set_xlim(-2.25, 2.25)
    ax.set_ylim(-2.15, 2.15)
    finish(ax, "Heawood graph: incidence graph")
    fig.tight_layout()
    fig.savefig(os.path.join(out, "maths4_graphs_fano_heawood.png"), dpi=160, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- grid
GRID = [(i, j) for i in range(3) for j in range(3)]
ROWS = [frozenset((i, j) for j in range(3)) for i in range(3)]
COLS = [frozenset((i, j) for i in range(3)) for j in range(3)]
GLINES = ROWS + COLS


def grid_hyperplanes():
    def sub(X):
        return all(len(L & X) < 2 or L <= X for L in GLINES)

    hyps = []
    for r in range(1, 9):
        for X in it.combinations(GRID, r):
            X = frozenset(X)
            if sub(X) and all(L & X for L in GLINES):
                hyps.append(X)
    return hyps


def gxy(p):
    i, j = p
    return (j, 2 - i)


def draw_grid(ax, highlight=(), hl_lines=(), hl_color=ORANGE, labels=None):
    for L in GLINES:
        xy = sorted(gxy(p) for p in L)
        ax.plot([xy[0][0] - 0.3 if xy[0][1] == xy[-1][1] else xy[0][0], xy[-1][0] + 0.3 if xy[0][1] == xy[-1][1] else xy[-1][0]],
                [xy[0][1] - 0.3 if xy[0][0] == xy[-1][0] else xy[0][1], xy[-1][1] + 0.3 if xy[0][0] == xy[-1][0] else xy[-1][1]],
                color=GREY, lw=2.0, zorder=1)
    for L in hl_lines:
        xy = sorted(gxy(p) for p in L)
        ax.plot([xy[0][0], xy[-1][0]], [xy[0][1], xy[-1][1]], color=hl_color, lw=4.5, zorder=2, solid_capstyle="round")
    for p in GRID:
        x, y = gxy(p)
        if p in highlight:
            node(ax, x, y, r=0.14, face=hl_color, edge="#222222")
        else:
            node(ax, x, y, r=0.1, face="white", edge="#222222")
    if labels:
        for p, (t, dx, dy) in labels.items():
            x, y = gxy(p)
            ax.text(x + dx, y + dy, t, ha="center", va="center", fontsize=14, style="italic")
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylim(-0.6, 2.6)


def fig_grid_hyperplanes(out):
    hyps = grid_hyperplanes()
    crosses = [h for h in hyps if len(h) == 5]
    trans = [h for h in hyps if len(h) == 3]
    assert len(hyps) == 15 and len(crosses) == 9 and len(trans) == 6
    x = (1, 1)
    cross = ROWS[1] | COLS[1]
    assert cross in crosses
    tv = frozenset({(0, 1), (1, 2), (2, 0)})
    assert tv in trans and all(len(L & tv) == 1 for L in GLINES)

    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.6))
    draw_grid(axes[0], highlight=cross, hl_lines=[ROWS[1], COLS[1]], labels={x: ("x", 0.28, 0.28)})
    finish(axes[0], "(a) a cross $x^\\perp$: 5 points")
    draw_grid(axes[1], highlight=tv, hl_color=BLUE)
    finish(axes[1], "(b) an ovoid: 3 points")
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(os.path.join(out, "maths4_graphs_grid_hyperplanes.png"), dpi=160, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- alternating path
def fig_alternating_path(out):
    x, z, y = (0, 0), (0, 1), (1, 1)
    R, C = ROWS[0], COLS[1]
    assert x in R and z in R and z in C and y in C
    assert not any(x in L and y in L for L in GLINES)

    fig = plt.figure(figsize=(11, 4.0))
    ax1 = fig.add_axes([0.02, 0.05, 0.36, 0.85])
    ax2 = fig.add_axes([0.42, 0.05, 0.56, 0.85])
    draw_grid(ax1, highlight={x, z, y}, hl_lines=[], labels={x: ("x", -0.3, 0.28), z: ("z", 0.0, 0.32), y: ("y", 0.3, -0.28)})
    for a, b in [(x, z), (z, y)]:
        (x1, y1), (x2, y2) = gxy(a), gxy(b)
        ax1.annotate("", xy=(x2, y2), xytext=(x1, y1),
                     arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=3.2, shrinkA=11, shrinkB=11, mutation_scale=18), zorder=5)
    ax1.text(-0.55, 2.0, "$R$", ha="center", va="center", fontsize=14, color=BLUE)
    ax1.text(1.0, -0.55, "$C$", ha="center", va="center", fontsize=14, color=BLUE)
    ax1.text(1.0, -0.95, "collinearity graph: $d(x,y) = 2$", ha="center", fontsize=12)
    ax1.set_xlim(-0.8, 2.6)
    ax1.set_ylim(-1.15, 2.6)
    finish(ax1, "(a) in the grid")

    seq = [("x", "p"), ("row $R$", "L"), ("z", "p"), ("column $C$", "L"), ("y", "p")]
    xs = np.linspace(0, 4.4, len(seq))
    for k in range(len(seq) - 1):
        ax2.plot([xs[k], xs[k + 1]], [0, 0], color=ORANGE, lw=3.2, zorder=1)
        ax2.text((xs[k] + xs[k + 1]) / 2, 0.22, str(k + 1), ha="center", fontsize=11, color="#555555")
    for (t, kind), xx in zip(seq, xs):
        if kind == "p":
            node(ax2, xx, 0, r=0.16, face=ORANGE, edge="#222222")
            ax2.text(xx, -0.42, t, ha="center", fontsize=14, style="italic")
        else:
            node(ax2, xx, 0, r=0.15, face="white", edge=BLUE, square=True, lw=2.4)
            ax2.text(xx, -0.42, t, ha="center", fontsize=13, color=BLUE)
    ax2.text(2.2, -0.95, r"incidence graph: $\delta(x,y) = 4 = 2\,d(x,y)$", ha="center", fontsize=12)
    ax2.set_xlim(-0.5, 4.9)
    ax2.set_ylim(-1.2, 0.7)
    finish(ax2, "(b) the same path, alternating points and lines")
    fig.savefig(os.path.join(out, "maths4_graphs_alternating_path.png"), dpi=160, facecolor="white")
    plt.close(fig)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    out = sys.argv[1]
    os.makedirs(out, exist_ok=True)
    fig_valency(out)
    fig_petersen(out)
    fig_fano_heawood(out)
    fig_grid_hyperplanes(out)
    fig_alternating_path(out)


if __name__ == "__main__":
    main()
