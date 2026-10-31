"""Figures for the chapter "Generalized Polygons".

Usage: python make_polygons_figures.py OUTPUT_DIR

Writes
  maths4_polygons_opposite.png  opposite elements pair off their neighbours:
                                (a) two non-collinear points of a quadrangle of order (2,2),
                                (b) a point and a line not through it in the Fano plane;
  maths4_polygons_triad.png     triads in the doily W(3,2) and in Q^-(5,2) (computed);
  maths4_polygons_shells.png    the lines through a point y at distance i from x, for a polygon
                                of order (2,2): a middle shell, the last shell for even n, and the
                                last shell for odd n.
"""
import itertools
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

BLUE, RED, GREEN, ORANGE, GREY = "#1f77b4", "#d62728", "#2ca02c", "#ff9f1c", "0.6"


def pts(n):
    return [v for v in itertools.product((0, 1), repeat=n) if any(v)]


def add(a, b):
    return tuple((x + y) % 2 for x, y in zip(a, b))


def lines_in(pset):
    out = set()
    for a, b in itertools.combinations(sorted(pset), 2):
        c = add(a, b)
        if c in pset:
            out.add(frozenset((a, b, c)))
    return [tuple(sorted(l)) for l in out]


def dot(ax, xy, colour="black", size=90, hollow=False, z=3):
    if hollow:
        ax.scatter(*xy, s=size, facecolor="white", edgecolor="black", linewidth=1.0, zorder=z)
    else:
        ax.scatter(*xy, s=size, color=colour, edgecolor="black", linewidth=0.6, zorder=z)


# ---------------------------------------------------------------- opposite elements
def opposite_figure(out):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), facecolor="white")
    cols = [RED, BLUE, GREEN]

    ax = axes[0]
    x, y = np.array([0.0, 0.0]), np.array([6.0, 0.0])
    cs = [np.array([3.0, h]) for h in (2.1, 0.8, -2.1)]
    for c, col in zip(cs, cols):
        ax.plot([x[0], c[0]], [x[1], c[1]], color=col, lw=2.2, zorder=1)
        ax.plot([c[0], y[0]], [c[1], y[1]], color=col, lw=2.2, ls=(0, (6, 3)), zorder=1)
        dot(ax, (x + c) / 2, hollow=True, size=60)
        dot(ax, (c + y) / 2, hollow=True, size=60)
        dot(ax, c, colour=col, size=110)
    dot(ax, x, size=150)
    dot(ax, y, size=150)
    ax.annotate("x", x, xytext=(-16, 0), textcoords="offset points", fontsize=14, va="center", ha="right")
    ax.annotate("y", y, xytext=(16, 0), textcoords="offset points", fontsize=14, va="center", ha="left")
    ax.text(1.0, 1.55, "lines through x", fontsize=10.5, ha="center", rotation=34)
    ax.text(5.0, 1.55, "lines through y", fontsize=10.5, ha="center", rotation=-34)
    ax.text(3.0, -3.0, "each line through x has one point collinear with y,\n"
                       "which sends it to one line through y", ha="center", va="top", fontsize=10.5)
    ax.set_title("(a) Opposite points of a quadrangle of order (2,2)", fontsize=12)
    ax.set_xlim(-1.0, 7.0)
    ax.set_ylim(-4.2, 2.8)
    ax.set_aspect("equal")
    ax.axis("off")

    ax = axes[1]
    p = np.array([0.0, 3.2])
    Lpts = [np.array([xx, 0.0]) for xx in (-2.4, 0.0, 2.4)]
    ax.plot([-3.2, 3.2], [0, 0], color="black", lw=2.6, zorder=1)
    ax.text(3.35, 0, "L", fontsize=14, va="center")
    for q, col in zip(Lpts, cols):
        ax.plot([p[0], q[0]], [p[1], q[1]], color=col, lw=2.2, zorder=1)
        dot(ax, (p + q) / 2, hollow=True, size=60)
        dot(ax, q, colour=col, size=110)
    dot(ax, p, size=150)
    ax.annotate("p", p, xytext=(0, 14), textcoords="offset points", fontsize=14, ha="center")
    ax.text(0.0, -0.9, "the three lines through p and the three points of L pair off",
            ha="center", va="top", fontsize=10.5)
    ax.set_title("(b) A point opposite a line in the Fano plane", fontsize=12)
    ax.set_xlim(-4.0, 4.0)
    ax.set_ylim(-2.0, 4.2)
    ax.set_aspect("equal")
    ax.axis("off")

    fig.tight_layout()
    fig.savefig(out / "maths4_polygons_opposite.png", dpi=150, facecolor="white")


# ---------------------------------------------------------------- triads
def gq_graph(P, L):
    G = nx.Graph()
    G.add_nodes_from(P)
    for l in L:
        for a, b in itertools.combinations(l, 2):
            G.add_edge(a, b)
    return G


def triad_panel(ax, G, title, note):
    P = sorted(G.nodes)
    x = P[0]
    y = next(p for p in P if p != x and not G.has_edge(x, p))
    C = sorted(set(G[x]) & set(G[y]))
    Z = [z for z in P if z not in (x, y) and not G.has_edge(x, z) and not G.has_edge(y, z)]
    tz = {z: [c for c in C if G.has_edge(z, c)] for z in Z}
    Z.sort(key=lambda z: (-len(tz[z]), [C.index(c) for c in tz[z]]))
    width = max(len(C), len(Z)) - 1
    posx = {x: (width / 2 - 1.2, 2.0), y: (width / 2 + 1.2, 2.0)}
    posc = {c: (width / 2 + (k - (len(C) - 1) / 2) * 1.0 * max(1, width / max(1, len(C) - 1) * 0.75), 0.0)
            for k, c in enumerate(C)}
    posz = {z: (k * width / max(1, len(Z) - 1), -2.0) for k, z in enumerate(Z)}
    for c in C:
        for e in (x, y):
            ax.plot(*zip(posx[e], posc[c]), color=GREY, lw=1.2, zorder=1)
    for z in Z:
        for c in tz[z]:
            ax.plot(*zip(posz[z], posc[c]), color=BLUE, lw=1.1, alpha=0.8, zorder=1)
    for e in (x, y):
        dot(ax, posx[e], size=140)
    ax.annotate("x", posx[x], xytext=(-12, 6), textcoords="offset points", fontsize=13, ha="right")
    ax.annotate("y", posx[y], xytext=(12, 6), textcoords="offset points", fontsize=13, ha="left")
    for c in C:
        dot(ax, posc[c], colour=ORANGE, size=110)
    for z in Z:
        dot(ax, posz[z], colour=BLUE, size=90)
        ax.annotate(str(len(tz[z])), posz[z], xytext=(0, -15), textcoords="offset points", ha="center",
                    fontsize=11)
    ax.text(-0.9, 0.0, "common\nneighbours", ha="right", va="center", fontsize=10.5, color="#b36b00")
    ax.text(-0.9, -2.0, "Z", ha="right", va="center", fontsize=12, color=BLUE)
    ax.text(width / 2, -3.0, note, ha="center", va="top", fontsize=10.5)
    ax.set_title(title, fontsize=12)
    ax.set_xlim(-2.2, width + 0.8)
    ax.set_ylim(-4.0, 2.8)
    ax.axis("off")
    return [len(tz[z]) for z in Z]


def triad_figure(out):
    P4 = pts(4)

    def sym(v, u):
        return (v[0] * u[1] + v[1] * u[0] + v[2] * u[3] + v[3] * u[2]) % 2
    WL = [l for l in lines_in(set(P4)) if all(sym(a, b) == 0 for a, b in itertools.combinations(l, 2))]
    assert len(WL) == 15
    Qm = [p for p in pts(6) if (p[0] + p[0] * p[1] + p[1] + p[2] * p[3] + p[4] * p[5]) % 2 == 0]
    QmL = lines_in(set(Qm))
    assert len(Qm) == 27 and len(QmL) == 45
    fig, axes = plt.subplots(1, 2, figsize=(13, 4.9), facecolor="white",
                             gridspec_kw={"width_ratios": [1, 2.1]})
    c1 = triad_panel(axes[0], gq_graph(P4, WL), "(a) The doily, order (2,2)",
                     "|Z| = 4; centre counts 3, 1, 1, 1")
    c2 = triad_panel(axes[1], gq_graph(Qm, QmL), "(b) Q$^-$(5,2), order (2,4)",
                     "|Z| = 10; every triad {x, y, z} has 3 = s + 1 centres")
    assert sorted(c1) == [1, 1, 1, 3] and c2 == [3] * 10
    fig.tight_layout()
    fig.savefig(out / "maths4_polygons_triad.png", dpi=150, facecolor="white")


# ---------------------------------------------------------------- shells
def shell_panel(ax, title, lines, labels, counts):
    """lines: list of (colour, [points other than y]); y sits at the origin."""
    for xc, lab in zip((-2.2, 0.0, 2.2), labels):
        ax.add_patch(plt.Rectangle((xc - 0.85, -2.3), 1.7, 4.6, color="0.93", zorder=0))
        ax.text(xc, 2.45, lab, ha="center", va="bottom", fontsize=12)
    for col, others in lines:
        allp = np.array([[0.0, 0.0]] + others)
        order = np.argsort(allp[:, 0] + 1e-3 * allp[:, 1])
        a, b = allp[order[0]], allp[order[-1]]
        ax.plot([a[0], b[0]], [a[1], b[1]], color=col, lw=2.2, zorder=1)
        for o in others:
            dot(ax, o, colour=col, size=70)
    dot(ax, (0, 0), size=130, z=4)
    ax.annotate("y", (0, 0), xytext=(0, 13), textcoords="offset points", fontsize=13, ha="center",
                bbox=dict(boxstyle="round,pad=0.1", fc="white", ec="none"), zorder=5)
    ax.text(0.0, -2.55, counts, ha="center", va="top", fontsize=11)
    ax.set_title(title, fontsize=12)
    ax.set_xlim(-3.2, 3.2)
    ax.set_ylim(-3.6, 3.1)
    ax.set_aspect("equal")
    ax.axis("off")


def shells_figure(out):
    fig, axes = plt.subplots(1, 3, figsize=(14, 5.2), facecolor="white")
    back = lambda h: [[-2.2, h], [0.7, -0.7 * h / 2.2]]
    # (a) middle shell: one line back, t = 2 lines out with s = 2 points each
    shell_panel(axes[0], "(a) y in a middle shell",
                [(RED, back(2.0)),
                 (BLUE, [[1.7, 1.0], [2.5, 1.47]]),
                 (BLUE, [[1.7, -0.3], [2.5, -0.44]])],
                [r"$\Gamma_{i-1}(x)$", r"$\Gamma_i(x)$", r"$\Gamma_{i+1}(x)$"],
                r"$c_i = 1,\ a_i = s-1,\ b_i = st$")
    # (b) last shell, n even: all t + 1 lines go back
    shell_panel(axes[1], "(b) y in the last shell, n even",
                [(RED, back(2.0)), (RED, [[-2.2, 0.0], [0.7, 0.0]]), (RED, back(-2.0))],
                [r"$\Gamma_{d-1}(x)$", r"$\Gamma_d(x)$", ""],
                r"$c_d = t+1,\ a_d = (s-1)(t+1),\ b_d = 0$")
    # (c) last shell, n odd: one line back, t lines inside the last shell
    shell_panel(axes[2], "(c) y in the last shell, n odd",
                [(RED, back(0.0)),
                 (GREEN, [[0.25, 1.0], [0.5, 2.0]]),
                 (GREEN, [[0.25, -1.0], [0.5, -2.0]])],
                [r"$\Gamma_{d-1}(x)$", r"$\Gamma_d(x)$", ""],
                r"$c_d = 1,\ a_d = st+s-1,\ b_d = 0$")
    for ax in axes[1:]:
        ax.patches[-1].set_visible(False)  # no next shell after the last one
    fig.tight_layout()
    fig.savefig(out / "maths4_polygons_shells.png", dpi=150, facecolor="white")


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)
    opposite_figure(out)
    triad_figure(out)
    shells_figure(out)
    print("wrote polygons figures to", out)


if __name__ == "__main__":
    main()
