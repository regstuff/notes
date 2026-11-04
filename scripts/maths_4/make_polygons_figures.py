"""Figures 17 to 19 for the chapter "Generalized Polygons" (Maths 4, incidence geometry).

Usage: python3 make_polygons_figures.py [OUTPUT_DIR]

Writes three PNGs into OUTPUT_DIR (default: docs/maths/figures in this repository):
  maths4_polygons_incidence_doubling.png   (Figure 17) Heawood incidence graph of PG(2,2), doubling, opposite-vertex bijection, and thick order proof
  maths4_polygons_triads_hyperplanes.png   (Figure 18) GQ triads, centers, Higman equality t = s^2, and hyperplane complement diameter at most 3
  maths4_polygons_feit_higman.png          (Figure 19) Distance-regular layers of the collinearity graph and the Feit-Higman classification

Every graph, incidence relation, cycle, distance, triad center count, hyperplane complement diameter,
distance-regular intersection number, sphere size, eigenvalue, and Biggs multiplicity is computed from
first principles and asserted before plotting.
"""

from collections import deque
import itertools as it
import math
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


DEFAULT_OUT_DIR = Path(__file__).resolve().parents[2] / "docs" / "maths" / "figures"


def bfs_distances(adj, start):
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist


def graph_girth(adj):
    best = math.inf
    for root in adj:
        dist = {root: 0}
        parent = {root: None}
        q = deque([root])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in dist:
                    dist[v] = dist[u] + 1
                    parent[v] = u
                    q.append(v)
                elif parent[u] != v:
                    best = min(best, dist[u] + dist[v] + 1)
    return best


def verify_and_build_heawood():
    """Build the 14-vertex Heawood graph as the incidence graph of PG(2,2) and verify all Figure 17 claims."""
    N = 14
    edges = set()
    for i in range(N):
        edges.add(tuple(sorted((i, (i + 1) % N))))
        if i % 2 == 0:
            edges.add(tuple(sorted((i, (i + 5) % N))))
    assert len(edges) == 21

    adj = {i: set() for i in range(N)}
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)

    # Even vertices = 7 points p_1..p_7; odd vertices = 7 lines L_1..L_7
    pts = [2 * k for k in range(7)]
    lines = [2 * k + 1 for k in range(7)]
    assert all(len(adj[u]) == 3 for u in range(N))

    # Check projective plane (Fano plane PG(2,2)) axioms:
    # every two distinct points share a unique line, and every two distinct lines share a unique point
    for p1, p2 in it.combinations(pts, 2):
        common_lines = adj[p1] & adj[p2]
        assert len(common_lines) == 1
    for l1, l2 in it.combinations(lines, 2):
        common_pts = adj[l1] & adj[l2]
        assert len(common_pts) == 1

    # Check diameter = 3 and girth = 6
    all_dists = {u: bfs_distances(adj, u) for u in range(N)}
    diam = max(max(d.values()) for d in all_dists.values())
    girth = graph_girth(adj)
    assert diam == 3 and girth == 6

    # Check highlighted 6-cycle (0,1,2,3,4,5) = (p_1, L_1, p_2, L_2, p_3, L_3)
    cycle_verts = [0, 1, 2, 3, 4, 5]
    cycle_edges = {
        tuple(sorted((cycle_verts[k], cycle_verts[(k + 1) % 6])))
        for k in range(6)
    }
    assert cycle_edges <= edges
    # Check opposite pair delta(p_1, L_4) = delta(0, 7) = 3
    assert all_dists[0][7] == 3

    # Check opposite-vertex degree bijection for every pair at distance 3
    for x in range(N):
        for y in range(N):
            if all_dists[x][y] == 3:
                for z in adj[x]:
                    step_closer = [w for w in adj[y] if all_dists[z][w] == 1]
                    assert len(step_closer) == 1

    # Check subdividing all 21 edges (doubling PG(2,2)) gives a 35-vertex incidence graph of girth 12 and diameter 6
    sub_adj = {i: set() for i in range(N)}
    for idx, (u, v) in enumerate(sorted(edges)):
        flag_node = N + idx
        sub_adj[flag_node] = {u, v}
        sub_adj[u].add(flag_node)
        sub_adj[v].add(flag_node)
    sub_dists = {u: bfs_distances(sub_adj, u) for u in sub_adj}
    assert max(max(d.values()) for d in sub_dists.values()) == 6
    assert graph_girth(sub_adj) == 12

    return N, edges, cycle_edges


def make_figure_26_incidence_doubling(out_dir: Path) -> Path:
    """Figure 17: Heawood incidence graph of Fano plane, doubling, opposite-vertex bijection, and thick order proof."""
    N, edges, cycle_edges = verify_and_build_heawood()

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["mathtext.fontset"] = "cm"

    fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0, 6.4), dpi=220)
    fig1.patch.set_facecolor("white")

    # Panel (a): Heawood Graph (incidence graph of PG(2,2): n=3, diam=3, girth=6) + Double
    ax1.set_xlim(-3.7, 3.7)
    ax1.set_ylim(-4.2, 3.8)
    ax1.axis("off")
    ax1.set_title(
        "(a) Incidence Graph $\\widetilde{\\Gamma}$ of Fano Plane ($n=3$: diam $3$, girth $6$)",
        fontsize=12.0, fontweight="bold", pad=8, color="#1a2530"
    )

    R = 2.65
    angles = [np.pi / 2 - 2 * np.pi * i / N for i in range(N)]
    hx = [R * np.cos(a) for a in angles]
    hy = [R * np.sin(a) for a in angles]

    for u, v in edges:
        if (u, v) in cycle_edges:
            ax1.plot([hx[u], hx[v]], [hy[u], hy[v]], color="#dc2626", lw=3.0, zorder=3)
        else:
            ax1.plot([hx[u], hx[v]], [hy[u], hy[v]], color="#cbd5e1", lw=1.5, zorder=2)

    # Show subdivision (doubling) on edge 0-1
    mx, my = 0.5 * (hx[0] + hx[1]), 0.5 * (hy[0] + hy[1])
    ax1.scatter([mx], [my], s=70, marker="D", color="#d97706", edgecolor="white", lw=1.0, zorder=6)
    ax1.annotate(
        "Doubling inserts flag\n$\\{p_1,L_1\\}$ ($2n=6$-gon)",
        xy=(mx, my), xytext=(1.35, 3.15),
        fontsize=8.8, fontweight="bold", color="#b45309", ha="center",
        arrowprops=dict(arrowstyle="->", lw=1.4, color="#d97706")
    )

    for i in range(N):
        is_pt = (i % 2 == 0)
        if is_pt:
            ax1.scatter([hx[i]], [hy[i]], s=110, marker="o", color="#0f766e", edgecolor="white", lw=1.2, zorder=5)
            lbl = f"$p_{{{i // 2 + 1}}}$"
        else:
            ax1.scatter([hx[i]], [hy[i]], s=115, marker="s", color="#3730a3", edgecolor="white", lw=1.2, zorder=5)
            lbl = f"$L_{{{i // 2 + 1}}}$"
        rx, ry = 1.17 * hx[i], 1.17 * hy[i]
        ax1.text(
            rx, ry, lbl, fontsize=9.6, fontweight="bold",
            color=("#0f766e" if is_pt else "#3730a3"), ha="center", va="center"
        )

    ax1.text(
        0.0, -3.88,
        "Circles = points $\\mathcal{P}$, Squares = lines $\\mathcal{L}$  |  Red $6$-cycle = ordinary $3$-gon ($2n = 6$)\n"
        "Opposite pair e.g. $\\delta(p_1, L_4) = 3 = n$ ($p_1$ at top, $L_4$ at bottom)",
        fontsize=8.9, color="#334155", ha="center", linespacing=1.35
    )

    # Panel (b): Opposite-vertex degree bijection & proving thick polygons have order (s, t)
    ax2.set_xlim(-0.4, 10.4)
    ax2.set_ylim(-0.6, 8.6)
    ax2.axis("off")
    ax2.set_title(
        "(b) Opposite-Vertex Bijection ($\\delta=n$) and Thick Order Proof",
        fontsize=12.0, fontweight="bold", pad=8, color="#1a2530"
    )

    # Top box: Bijection between neighbors of opposite vertices x and y (delta(x,y) = n)
    box_top = patches.FancyBboxPatch(
        (0.0, 4.45), 10.0, 3.7, boxstyle="round,pad=0.18",
        facecolor="#f8fafc", edgecolor="#94a3b8", lw=1.4
    )
    ax2.add_patch(box_top)
    ax2.text(
        0.3, 7.82, "1. Opposite vertices ($\\delta(x,y)=n$) have equal degree:",
        fontsize=10.0, fontweight="bold", color="#1e293b"
    )

    x_pt = (1.1, 6.0)
    y_pt = (8.9, 6.0)
    ax2.scatter([x_pt[0], y_pt[0]], [x_pt[1], y_pt[1]], s=110, color="#dc2626", edgecolor="white", lw=1.3, zorder=5)
    ax2.text(x_pt[0] - 0.38, x_pt[1], "$x$", fontsize=11, fontweight="bold", color="#b91c1c", va="center")
    ax2.text(y_pt[0] + 0.25, y_pt[1], "$y$", fontsize=11, fontweight="bold", color="#b91c1c", va="center")

    for idx, yy in enumerate([7.05, 6.0, 4.95]):
        zx = (2.7, yy)
        zy = (7.3, yy)
        ax2.plot([x_pt[0], zx[0]], [x_pt[1], zx[1]], color="#0f766e", lw=2.0)
        ax2.plot([y_pt[0], zy[0]], [y_pt[1], zy[1]], color="#3730a3", lw=2.0)
        ax2.plot([zx[0], zy[0]], [zx[1], zy[1]], color="#6366f1", lw=1.6, ls="--")
        ax2.scatter([zx[0]], [zx[1]], s=70, color="#0f766e", zorder=5)
        ax2.scatter([zy[0]], [zy[1]], s=70, color="#3730a3", zorder=5)
        if idx == 0:
            ax2.text(zx[0], zx[1] + 0.26, "$z \\in \\widetilde{\\Gamma}_1(x)$", fontsize=9.0, color="#0f766e", ha="center", fontweight="bold")
            ax2.text(zy[0], zy[1] + 0.26, "$\\pi_1(z) \\in \\widetilde{\\Gamma}_1(y)$", fontsize=9.0, color="#3730a3", ha="center", fontweight="bold")
            ax2.text(5.0, yy + 0.2, "unique geodesic of length $n-2$", fontsize=8.6, color="#4338ca", ha="center")

    ax2.text(
        5.0, 4.58, "When $n$ is odd, $x \\in \\mathcal{P}$ (deg $t+1$) and $y \\in \\mathcal{L}$ (deg $s+1$), forcing $s = t$",
        fontsize=8.9, fontweight="bold", color="#9d174d", ha="center"
    )

    # Bottom box: How thickness deg >= 3 equates deg(x) = deg(v) = deg(y) at distance 2
    box_bot = patches.FancyBboxPatch(
        (0.0, 0.0), 10.0, 4.0, boxstyle="round,pad=0.18",
        facecolor="#f8fafc", edgecolor="#94a3b8", lw=1.4
    )
    ax2.add_patch(box_bot)
    ax2.text(
        0.3, 3.65, "2. Why thickness ($\\deg \\geq 3$) forces a uniform order $(s, t)$:",
        fontsize=10.0, fontweight="bold", color="#1e293b"
    )

    ux, uy = (2.6, 1.85)
    xx = (1.1, 2.85)
    yx = (1.1, 0.85)
    zx_branch = (4.3, 1.85)
    vx = (8.4, 1.85)

    ax2.plot([xx[0], ux], [xx[1], uy], color="#0f766e", lw=2.3)
    ax2.plot([yx[0], ux], [yx[1], uy], color="#0f766e", lw=2.3)
    ax2.plot([ux, zx_branch[0]], [uy, zx_branch[1]], color="#d97706", lw=2.5)
    ax2.plot([zx_branch[0], vx[0]], [zx_branch[1], vx[1]], color="#d97706", lw=2.2, ls="--")

    for pt, col, lbl, off in [
        (xx, "#0f766e", "$x$", (-0.32, 0.05)),
        (yx, "#0f766e", "$y$", (-0.32, -0.08)),
        ((ux, uy), "#3730a3", "$u$", (0.0, 0.32)),
        (zx_branch, "#d97706", "$z \\neq x,y$ (3rd branch)", (0.0, 0.34)),
        (vx, "#dc2626", "$v$", (0.28, 0.0)),
    ]:
        ax2.scatter([pt[0]], [pt[1]], s=85, color=col, edgecolor="white", lw=1.1, zorder=5)
        ax2.text(pt[0] + off[0], pt[1] + off[1], lbl, fontsize=9.6, fontweight="bold", color=col, ha="center")

    ax2.text(6.35, 1.42, "non-backtracking path of length $n-1$", fontsize=8.6, color="#b45309", ha="center")
    ax2.text(
        5.0, 0.32, "$\\delta(x,v) = \\delta(y,v) = n \\;\\Rightarrow\\; \\deg(x) = \\deg(v) = \\deg(y)$",
        fontsize=9.1, fontweight="bold", color="#1e293b", ha="center"
    )

    fig1.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "maths4_polygons_incidence_doubling.png"
    fig1.savefig(out_path, dpi=220, facecolor="white")
    plt.close(fig1)
    return out_path


def verify_triads_and_hyperplanes():
    """Verify all triad, center, variance, and hyperplane-complement claims in Figure 18."""
    # Build W(2) from 2-element subsets of {1..6}
    pts = [frozenset(p) for p in it.combinations(range(1, 7), 2)]
    assert len(pts) == 15
    adj = {p: {q for q in pts if p != q and p.isdisjoint(q)} for p in pts}
    assert all(len(adj[p]) == 6 for p in pts)

    # Lines of W(2): 15 partitions of {1..6} into three 2-subsets
    lines = set()
    for p in pts:
        for q in adj[p]:
            r = frozenset(range(1, 7)) - p - q
            lines.add(frozenset([p, q, r]))
    assert len(lines) == 15

    # Fix noncollinear pair x = {1,2}, y = {1,3}
    x = frozenset([1, 2])
    y = frozenset([1, 3])
    assert y not in adj[x]
    common = adj[x] & adj[y]
    assert common == {frozenset([4, 5]), frozenset([4, 6]), frozenset([5, 6])}
    x_perp = {x} | adj[x]
    y_perp = {y} | adj[y]
    Z = set(pts) - (x_perp | y_perp)
    assert Z == {frozenset([1, 4]), frozenset([1, 5]), frozenset([1, 6]), frozenset([2, 3])}

    s, t = 2, 2
    assert len(Z) == 4 == s**2 * t - s * t - s + t
    tz_vals = sorted(len(common & adj[z]) for z in Z)
    assert tz_vals == [1, 1, 1, 3]
    assert sum(tz_vals) == 6 == (t + 1) * (t - 1) * s
    assert sum(v * v for v in tz_vals) == 12 == (t + 1) * (t - 1) * (s + t)
    lhs = len(Z) * sum(v * v for v in tz_vals) - sum(tz_vals) ** 2
    rhs = t * (t**2 - 1) * (s - 1) * (s**2 - t)
    assert lhs == rhs == 12 > 0

    # Check Q^-(5,2) parameters (s=2, t=4=s^2)
    s2, t2 = 2, 4
    v2 = (s2 + 1) * (s2 * t2 + 1)
    assert v2 == 27
    z2_size = s2**2 * t2 - s2 * t2 - s2 + t2
    assert z2_size == 10
    num_triads = v2 * (v2 - 1 - s2 * (t2 + 1)) * z2_size // 6
    assert num_triads == 720
    sum_tz2 = (t2 + 1) * (t2 - 1) * s2
    sum_tz2_sq = (t2 + 1) * (t2 - 1) * (s2 + t2)
    assert sum_tz2 == 30 and sum_tz2_sq == 90
    assert z2_size * sum_tz2_sq - sum_tz2**2 == 0
    assert sum_tz2 // z2_size == s2 + 1 == 3

    # Check hyperplane complements in W(2): every hyperplane H has connected complement of diameter <= 3
    hyperplanes = []
    for sub in it.chain.from_iterable(it.combinations(pts, r) for r in range(1, 15)):
        H = frozenset(sub)
        if all(len(H & L) in (1, 3) for L in lines):
            hyperplanes.append(H)
    # 15 tangent cones x^perp (size 7) + 6 ovoids (size 5) + 10 grids Q^+(3,2) (size 9) = 31 = 2^5 - 1 hyperplanes
    assert len(hyperplanes) == 31
    assert sum(1 for H in hyperplanes if len(H) == 5) == 6
    assert sum(1 for H in hyperplanes if len(H) == 7) == 15
    assert sum(1 for H in hyperplanes if len(H) == 9) == 10
    for H in hyperplanes:
        comp = set(pts) - H
        comp_adj = {u: adj[u] & comp for u in comp}
        for u in comp:
            d_u = bfs_distances(comp_adj, u)
            assert len(d_u) == len(comp)
            assert max(d_u.values()) <= 3


def make_figure_27_triads_hyperplanes(out_dir: Path) -> Path:
    """Figure 18: GQ triads, centers, Higman equality t = s^2, and hyperplane complement diameter at most 3."""
    verify_triads_and_hyperplanes()

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["mathtext.fontset"] = "cm"

    fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.0, 6.2), dpi=220)
    fig2.patch.set_facecolor("white")

    ax1.set_xlim(-0.5, 10.5)
    ax1.set_ylim(-1.15, 8.5)
    ax1.axis("off")
    ax1.set_title(
        "(a) Triads $\\{x,y,z\\}$, Centers, and Higman Equality $t = s^2$",
        fontsize=12.0, fontweight="bold", pad=8, color="#1a2530"
    )

    px = (1.5, 6.7)
    py = (1.5, 1.8)
    centers_y = [6.3, 4.25, 2.2]
    pz1 = (8.3, 5.4)
    pz2 = (8.3, 2.7)

    center_box = patches.FancyBboxPatch(
        (4.1, 1.4), 1.6, 5.7, boxstyle="round,pad=0.18",
        facecolor="#eef2ff", edgecolor="#6366f1", lw=1.5, ls="--"
    )
    ax1.add_patch(center_box)
    ax1.text(4.9, 7.45, "$x^\\perp \\cap y^\\perp$ ($t+1$ pts)", fontsize=9.8, fontweight="bold", color="#3730a3", ha="center")

    z_box = patches.FancyBboxPatch(
        (7.3, 1.4), 2.5, 5.7, boxstyle="round,pad=0.18",
        facecolor="#ecfdf5", edgecolor="#10b981", lw=1.5, ls="--"
    )
    ax1.add_patch(z_box)
    ax1.text(8.55, 7.45, "$Z = \\mathcal{P} \\backslash (x^\\perp \\cup y^\\perp)$", fontsize=9.6, fontweight="bold", color="#047857", ha="center")

    for idx, cy in enumerate(centers_y):
        u = (4.9, cy)
        ax1.plot([px[0], u[0]], [px[1], u[1]], color="#64748b", lw=1.6)
        ax1.plot([py[0], u[0]], [py[1], u[1]], color="#64748b", lw=1.6)
        ax1.scatter([u[0]], [u[1]], s=80, color="#4338ca", edgecolor="white", lw=1.1, zorder=5)
        ax1.text(u[0], u[1] + 0.32, f"$u_{idx + 1}$", fontsize=9.5, fontweight="bold", color="#3730a3", ha="center")
        ax1.plot([u[0], pz1[0]], [u[1], pz1[1]], color="#0f766e", lw=2.0)

    ax1.plot([4.9, pz2[0]], [centers_y[2], pz2[1]], color="#d97706", lw=2.0, ls="--")
    for pt, lbl, col, off in [
        (px, "$x$", "#dc2626", (-0.38, 0.0)),
        (py, "$y$", "#dc2626", (-0.38, 0.0)),
        (pz1, "$z_1$ ($t_{z_1}=3$)", "#0f766e", (0.0, 0.38)),
        (pz2, "$z_2$ ($t_{z_2}=1$)", "#b45309", (0.0, -0.45)),
    ]:
        ax1.scatter([pt[0]], [pt[1]], s=95, color=col, edgecolor="white", lw=1.2, zorder=6)
        ax1.text(pt[0] + off[0], pt[1] + off[1], lbl, fontsize=9.8, fontweight="bold", color=col, ha="center")

    ax1.text(
        5.0, -0.35,
        "Variance $\\sum_{z\\in Z}(t_z - \\bar{t})^2 \\geq 0 \\;\\Longleftrightarrow\\; t(t^2-1)(s-1)(s^2-t) \\geq 0$\n"
        "• $W(2)$ ($s=t=2 < s^2$): $|Z|=4$ with $t_z \\in \\{1,1,1,3\\}$ (non-constant)\n"
        "• $Q^-(5,2)$ ($s=2, t=4=s^2$): $|Z|=10$ and every triad has $t_z = s+1 = 3$ centers",
        fontsize=8.7, color="#1e293b", ha="center", linespacing=1.36
    )

    ax2.set_xlim(-0.5, 10.5)
    ax2.set_ylim(-1.15, 8.5)
    ax2.axis("off")
    ax2.set_title(
        "(b) Why $\\mathcal{P} \\backslash H$ Has Diameter $\\leq 3$ ($\\mathcal{S}$ Not a Dual Grid)",
        fontsize=11.8, fontweight="bold", pad=8, color="#1a2530"
    )

    h_band = patches.FancyBboxPatch(
        (0.3, 5.35), 9.4, 2.35, boxstyle="round,pad=0.18",
        facecolor="#fee2e2", edgecolor="#ef4444", lw=1.6
    )
    ax2.add_patch(h_band)
    ax2.text(
        0.6, 7.3, "Hyperplane $H$ (worst case: $\\Gamma_1(y_1) \\cap \\Gamma_1(y_2) \\subseteq H$)",
        fontsize=9.8, fontweight="bold", color="#991b1b"
    )

    comp_band = patches.FancyBboxPatch(
        (0.3, 0.9), 9.4, 3.85, boxstyle="round,pad=0.18",
        facecolor="#f0fdf4", edgecolor="#22c55e", lw=1.6
    )
    ax2.add_patch(comp_band)
    ax2.text(
        0.6, 1.2, "Complement $\\overline{H} = \\mathcal{P} \\backslash H$: $3$-step path $y_1 \\sim y'_1 \\sim y'_2 \\sim y_2$ stays inside $\\overline{H}$",
        fontsize=9.3, fontweight="bold", color="#166534"
    )

    z1 = (3.4, 6.25)
    z2 = (6.6, 6.25)
    y1_c = (2.0, 2.2)
    y2_c = (8.0, 2.2)
    y1p = (2.7, 4.22)
    y2p = (7.3, 4.22)

    ax2.plot([y1_c[0], z1[0]], [y1_c[1], z1[1]], color="#64748b", lw=1.8)
    ax2.plot([y2_c[0], z2[0]], [y2_c[1], z2[1]], color="#64748b", lw=1.8)
    ax2.plot([y1_c[0], z2[0]], [y1_c[1], z2[1]], color="#94a3b8", lw=1.2, ls=":")
    ax2.plot([y2_c[0], z1[0]], [y2_c[1], z1[1]], color="#94a3b8", lw=1.2, ls=":")

    ax2.plot([y1_c[0], y1p[0]], [y1_c[1], y1p[1]], color="#15803d", lw=3.2, zorder=4)
    ax2.plot([y1p[0], y2p[0]], [y1p[1], y2p[1]], color="#15803d", lw=3.2, zorder=4)
    ax2.plot([y2p[0], y2_c[0]], [y2p[1], y2_c[1]], color="#15803d", lw=3.2, zorder=4)
    ax2.text(
        5.0, 2.95, "GQ anti-flag $(y'_2, y_1 z_1)$\n$\\Rightarrow$ unique $y'_1 \\neq z_1, y_1$",
        fontsize=8.8, fontweight="bold", color="#166534", ha="center"
    )

    for pt, lbl, col, off in [
        (z1, "$z_1 \\in H$", "#dc2626", (-0.55, 0.15)),
        (z2, "$z_2 \\in H$", "#dc2626", (0.55, 0.15)),
        (y1_c, "$y_1$", "#15803d", (-0.38, -0.05)),
        (y2_c, "$y_2$", "#15803d", (0.38, -0.05)),
        (y1p, "$y'_1$", "#15803d", (-0.42, 0.05)),
        (y2p, "$y'_2$ ($|L|\\geq 3$)", "#15803d", (0.95, 0.05)),
    ]:
        ax2.scatter([pt[0]], [pt[1]], s=90, color=col, edgecolor="white", lw=1.2, zorder=6)
        ax2.text(pt[0] + off[0], pt[1] + off[1], lbl, fontsize=9.6, fontweight="bold", color=col, ha="center")

    ax2.text(
        5.0, -0.35, "Special case $H = x^\\perp$ ($\\mathcal{S}$ not a dual grid) $\\Rightarrow\\; \\Gamma_2(x) = \\mathcal{P} \\backslash x^\\perp$ is connected of diameter $\\leq 3$",
        fontsize=8.8, fontweight="bold", color="#1e293b", ha="center"
    )

    fig2.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "maths4_polygons_triads_hyperplanes.png"
    fig2.savefig(out_path, dpi=220, facecolor="white")
    plt.close(fig2)
    return out_path


def verify_feit_higman():
    """Verify distance-regular layer parameters, sphere sizes, eigenvalues, and multiplicities in Figure 19."""
    # Check sphere sizes and total vertex count for even n = 2d in {4, 6, 8, 12} and odd n = 2d+1 in {5, 7}
    for s, t in [(2, 2), (2, 4), (3, 3), (1, 3)]:
        for n in [4, 5, 6, 7, 8, 12]:
            d = n // 2
            b = [s * (t + 1)] + [s * t] * (d - 1) + [0]
            c = [0] + [1] * (d - 1) + ([t + 1] if n % 2 == 0 else [1])
            a = [b[0] - b[i] - c[i] for i in range(d + 1)]
            assert a[0] == 0
            for i in range(1, d):
                assert a[i] == s - 1
            if n % 2 == 0:
                assert a[d] == (s - 1) * (t + 1)
            else:
                assert a[d] == s * t + s - 1

            k = [1]
            for i in range(d):
                k.append(k[i] * b[i] // c[i + 1])
            for i in range(1, d):
                assert k[i] == (s**i) * (t**(i - 1)) * (t + 1)
            if n % 2 == 0:
                assert k[d] == (s**d) * (t**(d - 1))
                v_expected = (s + 1) * sum((s * t) ** j for j in range(d))
                assert sum(k) == v_expected
            else:
                assert k[d] == (s**d) * (t**(d - 1)) * (t + 1)

            # Check bottom eigenvalue theta = -t - 1 for even n = 2d
            if n % 2 == 0:
                theta_bot = -t - 1
                u = [1.0, theta_bot / b[0]]
                for i in range(1, d):
                    u_next = ((theta_bot - a[i]) * u[i] - c[i] * u[i - 1]) / b[i]
                    u.append(u_next)
                for i in range(d + 1):
                    assert abs(u[i] - ((-1.0 / s) ** i)) < 1e-12
                # Boundary equation at d
                assert abs((theta_bot - a[d]) * u[d] - c[d] * u[d - 1]) < 1e-12

    # Check worked hexagon of order (2, 2) (n = 6, d = 3, v = 63)
    s, t, n, d = 2, 2, 6, 3
    k_hex = [1, 6, 24, 32]
    assert sum(k_hex) == 63
    eigs_hex = [6.0, 3.0, -1.0, -3.0]
    mults_hex = []
    b_hex = [6, 4, 4, 0]
    a_hex = [0, 1, 1, 3]
    c_hex = [0, 1, 1, 3]
    for th in eigs_hex:
        u = [1.0, th / 6.0]
        for i in range(1, d):
            u.append(((th - a_hex[i]) * u[i] - c_hex[i] * u[i - 1]) / b_hex[i])
        assert abs((th - a_hex[d]) * u[d] - c_hex[d] * u[d - 1]) < 1e-12
        denom = sum(k_hex[i] * (u[i] ** 2) for i in range(d + 1))
        mults_hex.append(round(63.0 / denom))
    assert mults_hex == [1, 21, 27, 14]
    assert sum(mults_hex) == 63

    # Check hypothetical pentagon of order (2, 2) (n = 5, d = 2, v = 31)
    cos_2pi_5 = (math.sqrt(5) - 1.0) / 4.0
    s_odd_1 = (5.0 / 3.0) * (1.0 + 1.0 / (4.0 * (1.0 - cos_2pi_5)))
    assert abs(s_odd_1 - (25.0 + math.sqrt(5)) / 12.0) < 1e-12

    # Check smallest Ree-Tits octagon order (2, 4) has 1,755 points
    s_rt, t_rt = 2, 4
    v_rt = (s_rt + 1) * (1 + s_rt * t_rt + (s_rt * t_rt) ** 2 + (s_rt * t_rt) ** 3)
    assert v_rt == 1755


def make_figure_28_feit_higman(out_dir: Path) -> Path:
    """Figure 19: Distance-regular layers of the collinearity graph and the Feit-Higman classification."""
    verify_feit_higman()

    plt.rcParams.update(plt.rcParamsDefault)
    plt.rcParams["font.family"] = "DejaVu Sans"
    plt.rcParams["mathtext.fontset"] = "cm"

    fig3, (ax1, ax2) = plt.subplots(1, 2, figsize=(15.2, 6.2), dpi=220)
    fig3.patch.set_facecolor("white")

    ax1.set_xlim(-0.4, 10.6)
    ax1.set_ylim(-0.5, 8.5)
    ax1.axis("off")
    ax1.set_title(
        "(a) Collinearity Graph $\\Gamma$: Distance-Regular Layers ($d = \\lfloor n/2 \\rfloor$)",
        fontsize=12.0, fontweight="bold", pad=8, color="#1a2530"
    )

    layers_x = [0.7, 3.15, 5.95, 9.0]
    layer_titles = ["$\\Gamma_0(x)$", "$\\Gamma_1(x)$", "$\\Gamma_i(x)$ ($1\\leq i < d$)", "$\\Gamma_d(x)$ (Opposite)"]
    layer_sizes = ["$k_0 = 1$", "$k_1 = s(t+1)$", "$k_i = s^i t^{i-1}(t+1)$", "Even $n$: $s^d t^{d-1}$\nOdd $n$: $s^d t^{d-1}(t+1)$"]
    layer_a = ["$a_0 = 0$", "$a_1 = s-1$", "$a_i = s-1$", "Even $n$: $(s-1)(t+1)$\nOdd $n$: $st + s - 1$"]

    for idx, lx in enumerate(layers_x):
        w = 1.35 if idx == 0 else (1.55 if idx == 1 else (1.95 if idx == 2 else 2.25))
        box = patches.FancyBboxPatch(
            (lx - w / 2, 2.55), w, 4.4, boxstyle="round,pad=0.14",
            facecolor=("#eef2ff" if idx < 3 else "#fef3c7"),
            edgecolor=("#4f46e5" if idx < 3 else "#d97706"), lw=1.7
        )
        ax1.add_patch(box)
        ax1.text(lx, 6.55, layer_titles[idx], fontsize=9.4, fontweight="bold", color="#1e293b", ha="center")
        ax1.text(lx, 4.95, layer_sizes[idx], fontsize=8.6, color="#334155", ha="center", linespacing=1.35)
        ax1.text(lx, 3.25, layer_a[idx], fontsize=8.4, fontweight="bold", color="#0f766e", ha="center", linespacing=1.35)

    arrow_specs = [
        (1.52, 2.24, "$b_0 = s(t+1)$", "$c_1 = 1$"),
        (4.08, 4.84, "$b_1 = st$", "$c_2 = 1$"),
        (7.08, 7.74, "$b_{d-1} = st$", "Even $n$: $c_d = t+1$\nOdd $n$: $c_d = 1$"),
    ]
    for xL, xR, b_lbl, c_lbl in arrow_specs:
        ax1.annotate("", xy=(xR, 6.95), xytext=(xL, 6.95), arrowprops=dict(arrowstyle="->", lw=1.8, color="#dc2626"))
        ax1.text(0.5 * (xL + xR), 7.22, b_lbl, fontsize=8.5, fontweight="bold", color="#b91c1c", ha="center")
        ax1.annotate("", xy=(xL, 3.95), xytext=(xR, 3.95), arrowprops=dict(arrowstyle="->", lw=1.8, color="#2563eb"))
        ax1.text(0.5 * (xL + xR), 1.78 if "Even" in c_lbl else 3.55, c_lbl, fontsize=8.2, fontweight="bold", color="#1d4ed8", ha="center")

    ax1.text(
        5.1, 0.58,
        "Eigenvalues: $\\theta_0 = s(t+1)$, roots-of-unity modes $\\theta_l = s - 1 + 2\\sqrt{st}\\cos(2\\pi l/n)$,\n"
        "plus $\\theta_d = -(t+1)$ when $n = 2d$ is even (standard sequence $(1, -1/s, \\dots, (-1/s)^d)$).",
        fontsize=8.75, color="#1e293b", ha="center", linespacing=1.38
    )

    ax2.set_xlim(0.0, 10.4)
    ax2.set_ylim(-0.5, 8.5)
    ax2.axis("off")
    ax2.set_title(
        "(b) Feit–Higman Classification of Finite Generalized $n$-gons of Order $(s,t)$",
        fontsize=11.4, fontweight="bold", pad=8, color="#1a2530"
    )

    rows_fh = [
        ("$n = 3$ (Planes)", "Thick: $s = t \\geq 2$", "Projective planes $\\mathrm{PG}(2,q)$, etc.", "#dcfce7", "#16a34a"),
        ("$n = 4$ (Quadrangles)", "Known thick: $(q,q),(q,q^2),(q^2,q),(q^2,q^3),(q^3,q^2),(q\\pm 1,q\\mp 1)$", "Grids $(s,1)$, dual grids $(1,t)$, $W(q), Q(4,q), Q^-(5,q), H(3,q^2), H(4,q^2)$", "#dcfce7", "#16a34a"),
        ("$n = 6$ (Hexagons)", "Thick: $st$ is a square; known $(q,q), (q,q^3), (q^3,q)$", "Split-Cayley & twisted triality; $(1,q)$ = doubled plane", "#dcfce7", "#16a34a"),
        ("$n = 8$ (Octagons)", "Thick: $2st$ is a square; known $(q,q^2), (q^2,q)$, $q=2^{2e+1}$", "Ree–Tits octagons; $(1,q)$ = doubled GQ of order $(q,q)$", "#dcfce7", "#16a34a"),
        ("$n = 12$ (Dodecagons)", "no thick ($s=1$ or $t=1$ forced)", "$(1,q)$ = doubled hexagon of order $(q,q)$; $(q,1)$ = its point-line dual", "#fef9c3", "#ca8a04"),
        ("All other $n \\geq 5$", "only $s = t = 1$ ($\\cos(2\\pi/n)$ or $\\cos(4\\pi/n) \\notin \\mathbb{Q}$)", "With order $(s,t)$: ordinary $n$-gons only (no thick or semi-thin order $(s,t)$)", "#fee2e2", "#dc2626"),
    ]

    y_top = 7.15
    for title, cond, ex, bg, border in rows_fh:
        card = patches.FancyBboxPatch(
            (0.15, y_top - 0.85), 10.0, 1.05, boxstyle="round,pad=0.1",
            facecolor=bg, edgecolor=border, lw=1.5
        )
        ax2.add_patch(card)
        ax2.text(0.35, y_top - 0.14, title, fontsize=9.5, fontweight="bold", color="#0f172a")
        cond_fs = 8.05 if "Known thick" in cond else 8.8
        ax2.text(3.38 if "Known thick" in cond else 3.45, y_top - 0.14, cond, fontsize=cond_fs, fontweight="bold", color="#1e293b")
        ax2.text(0.35, y_top - 0.60, ex, fontsize=8.4, color="#334155")
        y_top -= 1.32

    fig3.tight_layout()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "maths4_polygons_feit_higman.png"
    fig3.savefig(out_path, dpi=220, facecolor="white")
    plt.close(fig3)
    return out_path


def main():
    out_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT_DIR
    f26 = make_figure_26_incidence_doubling(out_dir)
    f27 = make_figure_27_triads_hyperplanes(out_dir)
    f28 = make_figure_28_feit_higman(out_dir)
    for p in (f26, f27, f28):
        print(f"Wrote {p}")


if __name__ == "__main__":
    main()
