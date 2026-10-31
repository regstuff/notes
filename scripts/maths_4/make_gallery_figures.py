"""Figures for the chapter "A Gallery of Geometries" (Maths 4, incidence geometry).

Usage: python make_gallery_figures.py OUTPUT_DIR

Writes three PNGs into OUTPUT_DIR:
  maths4_gallery_small_geometries.png  small geometries that test the definitions
  maths4_gallery_glued_lines.png       two 3-point lines glued into a reducible projective space
  maths4_gallery_doily.png             the doily: W(3,2) drawn with 5-fold symmetry

Every incidence drawn is checked by computation first:
  * the glued pair is checked to be a linear space with generating index 4;
  * the doily is built twice, as W(3,2) from the alternating form
    x0*y1 + x1*y0 + x2*y3 + x3*y2 over F_2 and as duads/synthemes of {0,...,5};
    an explicit isomorphism is found and the drawn triples are asserted to be the
    15 totally isotropic lines of W(3,2), so the 4-bit labels in the picture are exact.
"""

import itertools as it
import os
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from networkx.algorithms import isomorphism

THICK = dict(color="#1f3b73", lw=2.6, solid_capstyle="round", zorder=2)
THIN = dict(color="#9a9a9a", lw=1.3, zorder=1)
DOT = dict(s=46, color="black", zorder=5)


# ---------------------------------------------------------------- small geometries
def panel_point(ax):
    ax.scatter([0], [0], **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_line(ax):
    xs = np.linspace(-0.8, 0.8, 4)
    ax.plot([-0.8, 0.8], [0, 0], **THICK)
    ax.scatter(xs, 0 * xs, **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_k4(ax):
    ang = np.pi / 2 + 2 * np.pi * np.arange(3) / 3
    pts = [(0.85 * np.cos(a), 0.85 * np.sin(a) - 0.1) for a in ang] + [(0, -0.1)]
    for p, q in it.combinations(pts, 2):
        ax.plot([p[0], q[0]], [p[1], q[1]], **THIN)
    ax.scatter(*zip(*pts), **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_digon(ax):
    p, q = np.array([-0.7, 0.0]), np.array([0.7, 0.0])
    for h in (-0.55, 0.0, 0.55):
        t = np.linspace(0, 1, 60)
        x = p[0] + (q[0] - p[0]) * t
        y = 4 * h * t * (1 - t)
        ax.plot(x, y, **THIN)
    ax.scatter([p[0], q[0]], [p[1], q[1]], **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_pentagon(ax):
    ang = np.pi / 2 + 2 * np.pi * np.arange(5) / 5
    pts = [(0.85 * np.cos(a), 0.85 * np.sin(a) - 0.05) for a in ang]
    for i in range(5):
        p, q = pts[i], pts[(i + 1) % 5]
        ax.plot([p[0], q[0]], [p[1], q[1]], **THIN)
    ax.scatter(*zip(*pts), **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_near_pencil(ax):
    xs = np.linspace(-0.8, 0.8, 4)
    base = [(x, -0.55) for x in xs]
    top = (0.0, 0.65)
    for b in base:
        ax.plot([top[0], b[0]], [top[1], b[1]], **THIN)
    ax.plot([-0.8, 0.8], [-0.55, -0.55], **THICK)
    ax.scatter(*zip(*(base + [top])), **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_cross(ax):
    p = np.array([-0.75, 0.0])
    up = [p + s * np.array([1.0, 0.55]) for s in (0.75, 1.5)]
    down = [p + s * np.array([1.0, -0.55]) for s in (0.75, 1.5)]
    for a in up:
        for b in down:
            ax.plot([a[0], b[0]], [a[1], b[1]], **THIN)
    ax.plot([p[0], up[-1][0]], [p[1], up[-1][1]], **THICK)
    ax.plot([p[0], down[-1][0]], [p[1], down[-1][1]], **THICK)
    allp = [p] + up + down
    ax.scatter([q[0] for q in allp], [q[1] for q in allp], **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_grid23(ax):
    xs, ys = [-0.7, 0.0, 0.7], [0.35, -0.35]
    for y in ys:
        ax.plot([xs[0], xs[-1]], [y, y], **THICK)
    for x in xs:
        ax.plot([x, x], [ys[0], ys[1]], **THIN)
    ax.scatter([x for x in xs for y in ys], [y for x in xs for y in ys], **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def panel_k23(ax):
    top = [(-0.45, 0.5), (0.45, 0.5)]
    bot = [(-0.75, -0.5), (0.0, -0.5), (0.75, -0.5)]
    for a in top:
        for b in bot:
            ax.plot([a[0], b[0]], [a[1], b[1]], **THIN)
    ax.scatter(*zip(*(top + bot)), **DOT)
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)


def make_small_geometries(outdir):
    panels = [
        (panel_point, "a point"),
        (panel_line, "a line"),
        (panel_k4, "$K_4$, a circular space"),
        (panel_digon, "a digon (3 lines, 2 points)"),
        (panel_pentagon, "an ordinary 5-gon"),
        (panel_near_pencil, "a near-pencil on 5 points"),
        (panel_cross, "a (3,3)-cross"),
        (panel_grid23, "a $2\\times 3$ grid"),
        (panel_k23, "its dual, $K_{2,3}$"),
    ]
    fig, axs = plt.subplots(3, 3, figsize=(9, 9))
    for ax, (fn, title) in zip(axs.flat, panels):
        fn(ax)
        ax.set_title(title, fontsize=13)
        ax.set_aspect("equal")
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "maths4_gallery_small_geometries.png"), dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- glued pair
def check_glued():
    A, B = ["a1", "a2", "a3"], ["b1", "b2", "b3"]
    P = A + B
    lines = [tuple(A), tuple(B)] + [(a, b) for a in A for b in B]
    # linear space: every two points on exactly one line
    assert all(sum(1 for L in lines if x in L and y in L) == 1 for x, y in it.combinations(P, 2))

    def closure(X):
        X = set(X)
        while True:
            new = set(X)
            for L in lines:
                if len(set(L) & X) >= 2:
                    new |= set(L)
            if new == X:
                return X
            X = new

    gi = min(k for k in range(7) if any(closure(S) == set(P) for S in it.combinations(P, k)))
    assert gi == 4 and len(lines) == 11
    return lines


def make_glued(outdir):
    check_glued()
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    A = [(-1.0, y) for y in (1.0, 0.0, -1.0)]
    B = [(1.0, y) for y in (1.0, 0.0, -1.0)]
    for a in A:
        for b in B:
            ax.plot([a[0], b[0]], [a[1], b[1]], **THIN)
    ax.plot([-1, -1], [1, -1], **THICK)
    ax.plot([1, 1], [1, -1], **THICK)
    ax.scatter(*zip(*(A + B)), **DOT)
    for i, (x, y) in enumerate(A):
        ax.text(x - 0.12, y, f"$a_{i + 1}$", ha="right", va="center", fontsize=14)
    for i, (x, y) in enumerate(B):
        ax.text(x + 0.12, y, f"$b_{i + 1}$", ha="left", va="center", fontsize=14)
    ax.text(-1.0, 1.32, "line $A$", ha="center", fontsize=13, color=THICK["color"])
    ax.text(1.0, 1.32, "line $B$", ha="center", fontsize=13, color=THICK["color"])
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.35, 1.55)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "maths4_gallery_glued_lines.png"), dpi=150, facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- the doily
def pg32_points():
    return [v for v in it.product((0, 1), repeat=4) if any(v)]


def w32_lines():
    pts = pg32_points()

    def f(x, y):
        return (x[0] * y[1] + x[1] * y[0] + x[2] * y[3] + x[3] * y[2]) % 2

    lines = set()
    for a, b in it.combinations(pts, 2):
        c = tuple((x + y) % 2 for x, y in zip(a, b))
        if f(a, b) == 0:  # the line {a, b, a+b} is totally isotropic
            lines.add(frozenset([a, b, c]))
    assert len(lines) == 15
    return pts, lines


def duad_model():
    S = lambda i: frozenset([i % 5, 5])          # "spokes": midpoints of the outer pentagon
    E = lambda j: frozenset([j % 5, (j + 1) % 5])  # outer corners
    D = lambda j: frozenset([j % 5, (j + 2) % 5])  # inner points
    lines = (
        [("side", frozenset([S(i), E(i + 1), E(i + 3)])) for i in range(5)]
        + [("arc", frozenset([S(i), D(i + 1), D(i + 2)])) for i in range(5)]
        + [("diam", frozenset([S(i), D(i - 1), E(i + 2)])) for i in range(5)]
    )
    # these 15 triples are exactly the synthemes (three disjoint duads)
    duads = [frozenset(d) for d in it.combinations(range(6), 2)]
    synth = {frozenset([a, b, frozenset(range(6)) - a - b])
             for a in duads for b in duads if not a & b}
    assert {L for _, L in lines} == synth and len(synth) == 15
    R = 1.0
    th = lambda p: np.pi / 2 + 2 * np.pi * p / 5
    pos = {}
    for j in range(5):
        pos[E(j)] = (R * np.cos(th(3 * j)), R * np.sin(th(3 * j)))
        r = R * np.cos(np.pi / 5)
        pos[S(j)] = (r * np.cos(th(3 * j + 3.5)), r * np.sin(th(3 * j + 3.5)))
        rd = 0.45
        pos[D(j)] = (rd * np.cos(th(3 * j + 1.5)), rd * np.sin(th(3 * j + 1.5)))
    return lines, pos


def incidence_graph(lines):
    G = nx.Graph()
    for j, L in enumerate(lines):
        for p in L:
            G.add_node(("p", p), side="p")
            G.add_node(("L", j), side="L")
            G.add_edge(("p", p), ("L", j))
    return G


def circle_through(p, q, r):
    (ax, ay), (bx, by), (cx, cy) = p, q, r
    d = 2 * (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by))
    if abs(d) < 1e-9:
        return None
    ux = ((ax**2 + ay**2) * (by - cy) + (bx**2 + by**2) * (cy - ay) + (cx**2 + cy**2) * (ay - by)) / d
    uy = ((ax**2 + ay**2) * (cx - bx) + (bx**2 + by**2) * (ax - cx) + (cx**2 + cy**2) * (bx - ax)) / d
    return (ux, uy), float(np.hypot(ax - ux, ay - uy))


def make_doily(outdir):
    pts, wlines = w32_lines()
    dlines, pos = duad_model()
    G1 = incidence_graph([L for _, L in dlines])
    G2 = incidence_graph(sorted(wlines, key=sorted))
    gm = isomorphism.GraphMatcher(G1, G2, node_match=lambda a, b: a["side"] == b["side"])
    assert gm.is_isomorphic()
    # The search order of the matcher depends on hashing, so pick one isomorphism
    # deterministically: list the drawn points by angle (outer ring, middle ring, inner ring)
    # and take the labelling whose sequence of 4-bit labels is lexicographically smallest.
    order = sorted(pos, key=lambda d: (-round(float(np.hypot(*pos[d])), 6),
                                       round(float((np.pi / 2 - np.arctan2(pos[d][1], pos[d][0])) % (2 * np.pi)), 6)))
    best = None
    for iso in gm.isomorphisms_iter():
        seq = tuple(iso[("p", d)][1] for d in order)
        if best is None or seq < best[0]:
            best = (seq, dict(iso))
    iso = best[1]
    label = {d: iso[("p", d)][1] for (kind, d) in G1.nodes if kind == "p"}
    drawn = {frozenset(label[d] for d in L) for _, L in dlines}
    assert drawn == set(wlines), "drawn triples are not the lines of W(3,2)"

    colours = {"side": "#1f3b73", "diam": "#2e7d32", "arc": "#b5521b"}
    fig, ax = plt.subplots(figsize=(7.4, 7.4))
    polylines = []
    for kind, L in dlines:
        P = [pos[d] for d in L]
        c = circle_through(*P)
        if c is None:
            P = sorted(P)
            xs = np.linspace(P[0][0], P[-1][0], 200)
            ys = np.linspace(P[0][1], P[-1][1], 200)
        else:
            (ux, uy), r = c
            angs = sorted(np.arctan2(y - uy, x - ux) for x, y in P)
            best = None
            for k in range(3):
                a0 = angs[k]
                span = max((a - a0) % (2 * np.pi) for a in angs)
                if best is None or span < best[1]:
                    best = (a0, span)
            t = np.linspace(best[0], best[0] + best[1], 200)
            xs, ys = ux + r * np.cos(t), uy + r * np.sin(t)
        ax.plot(xs, ys, color=colours[kind], lw=2.0, zorder=2)
        polylines.append(np.column_stack([xs, ys]))
    for d, (x, y) in pos.items():
        ax.scatter([x], [y], s=70, color="black", zorder=5)
        txt = "".join(map(str, label[d]))
        rad = np.hypot(x, y)
        if rad > 0.6:  # outer corners and midpoints: label outside, along the radius
            off = 0.13
            ax.text(x + off * x / rad, y + off * y / rad, txt, ha="center", va="center",
                    fontsize=12, family="monospace", zorder=6)
            continue
        # inner points: put the label in the widest gap between the curves leaving the point
        dirs = []
        for poly in polylines:
            dist = np.hypot(poly[:, 0] - x, poly[:, 1] - y)
            i = int(np.argmin(dist))
            if dist[i] > 1e-3:
                continue
            for j in (i - 12, i + 12):
                if 0 <= j < len(poly):
                    dirs.append(np.arctan2(poly[j, 1] - y, poly[j, 0] - x))
        dirs = sorted(a % (2 * np.pi) for a in dirs)
        gaps = [((dirs[(k + 1) % len(dirs)] - dirs[k]) % (2 * np.pi), dirs[k]) for k in range(len(dirs))]
        g, a0 = max(gaps)
        a = a0 + g / 2
        ax.text(x + 0.15 * np.cos(a), y + 0.15 * np.sin(a), txt, ha="center", va="center",
                fontsize=11, family="monospace", zorder=6,
                bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.9))
    ax.set_xlim(-1.25, 1.25)
    ax.set_ylim(-1.1, 1.25)
    ax.set_aspect("equal")
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(os.path.join(outdir, "maths4_gallery_doily.png"), dpi=150, facecolor="white")
    plt.close(fig)
    return label, dlines


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: make_gallery_figures.py OUTPUT_DIR")
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    make_small_geometries(outdir)
    make_glued(outdir)
    label, dlines = make_doily(outdir)
    for kind, L in dlines:
        print(kind, sorted("".join(map(str, label[d])) for d in L))


if __name__ == "__main__":
    main()
