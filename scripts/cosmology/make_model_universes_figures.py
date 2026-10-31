# Figures for the "Model Universes" chapter of the cosmology notes. Usage: python3 scripts/cosmology/make_model_universes_figures.py docs/astrophysics/figures
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad, solve_ivp

OUT = sys.argv[1]
SURF, INK, INK2, GRID = "#fcfcfb", "#0b0b0b", "#52514e", "#e4e3df"
C1, C2, C3, C4 = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
plt.rcParams.update({
    "figure.facecolor": SURF, "axes.facecolor": SURF, "savefig.facecolor": SURF,
    "axes.edgecolor": INK2, "axes.labelcolor": INK, "xtick.color": INK2, "ytick.color": INK2,
    "text.color": INK, "font.size": 11, "axes.titlesize": 12, "axes.spines.top": False,
    "axes.spines.right": False, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.8,
    "lines.linewidth": 2, "legend.frameon": False, "mathtext.fontset": "cm",
})
def save(fig, name):
    fig.tight_layout(); fig.savefig(f"{OUT}/{name}", dpi=150); plt.close(fig); print("wrote", name)

Or, Om = 9.21e-5, 0.315   # Planck 2018 LCDM (H0 = 67.4)
OL = 1 - Om - Or

# ---------- F1: energy densities vs a ----------
a = np.logspace(-6, 1, 400)
fig, ax = plt.subplots(figsize=(7, 4.6))
ax.loglog(a, Or/a**4, color=C1, ls="-")
ax.loglog(a, Om/a**3, color=C2, ls="--")
ax.loglog(a, OL*np.ones_like(a), color=C3, ls="-.")
arm, amL = Or/Om, (Om/OL)**(1/3)
for x, lab in [(arm, r"$a_{rm}\approx 2.9\times10^{-4}$"), (amL, r"$a_{m\Lambda}\approx 0.77$")]:
    ax.axvline(x, color=INK2, lw=1, ls=":")
    ax.text(x*1.15, 1e17, lab, color=INK2, fontsize=10)
ax.text(10**-5.6, Or/10**(-5.6*4)*3, r"radiation $\propto a^{-4}$", color=INK, fontsize=10.5)
ax.text(10**-5.6, Om/10**(-5.6*3)/40, r"matter $\propto a^{-3}$", color=INK, fontsize=10.5)
ax.text(2e-6, OL*3, r"$\Lambda$ = constant", color=INK, fontsize=10.5)
ax.set_ylim(1e-3, 1e21); ax.set_xlim(1e-6, 10)
ax.set_xlabel(r"scale factor $a$  (today $a=1$)")
ax.set_ylabel(r"$\varepsilon_i(a)\,/\,\varepsilon_{c,0}$")
ax.set_title("Who dominates when", loc="left")
save(fig, "model_universes_densities.png")

# ---------- F2: Milne universe inside Minkowski ----------
fig, ax = plt.subplots(figsize=(8.2, 4.8))
X = np.linspace(-2.6, 2.6, 400)
ax.plot(X, np.abs(X), color=INK2, lw=1.2, ls="--")
for chi in [-2, -1.5, -1, -0.5, -0.25, 0, 0.25, 0.5, 1, 1.5, 2]:
    T = np.linspace(0, 2.6, 50); ax.plot(T*np.tanh(chi), T, color=C1, lw=1.3)
for tt in [0.5, 1.0, 1.5, 2.0]:
    R = np.linspace(-2.6, 2.6, 400); T = np.sqrt(tt**2 + R**2)
    ax.plot(R, T, color=C2, lw=2.6 if tt == 1.0 else 1.3)
    ax.text(-0.04 if tt == 0.5 else 0.04, tt+0.05, f"$t={tt:g}\\,t_0$" if tt != 1.0 else "$t=t_0$", color=INK, fontsize=10,
            ha="right" if tt == 0.5 else "left", bbox=dict(fc=SURF, ec="none", pad=0.6))
R = np.linspace(0, 0.5, 50); ax.plot(R, 1.0 - R, color=INK, lw=1.8, ls=":")
for chi in [0.25, 0.5, 1.0]:
    v = np.tanh(chi); Te = 1/(1+v)
    ax.plot([v*Te], [Te], "o", ms=6.5, color=INK, mec=SURF, mew=1.5)
ax.annotate("we are here: origin galaxy at $t=t_0$", xy=(0, 1), xytext=(-2.5, 0.62), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.annotate("our past light cone;\ndots = emission events", xy=(0.36, 0.64), xytext=(0.95, 0.3), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.annotate("light cone of the\n'Big Bang' event", xy=(1.6, 1.6), xytext=(1.75, 0.95), fontsize=9.5, color=INK2,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.text(-2.5, 0.12, "blue: galaxy worldlines ($\\chi$ = const)\norange: constant cosmic time $t$", fontsize=9.5, color=INK2)
ax.set_xlim(-2.6, 2.6); ax.set_ylim(0, 2.6); ax.set_aspect("equal")
ax.set_xlabel(r"Minkowski radius $R\,/\,(c\,t_0)$"); ax.set_ylabel(r"Minkowski time $T\,/\,t_0$")
ax.set_title("The Milne universe is the inside of one light cone", loc="left")
save(fig, "model_universes_milne_minkowski.png")

# ---------- F3: single-component universes with the same H0 ----------
fig, ax = plt.subplots(figsize=(7, 4.6))
x = np.linspace(-1.2, 1.6, 600)
def pw(x, p):
    y = 1 + x/p; out = np.full_like(x, np.nan); m = y >= 0; out[m] = y[m]**p; return out
ax.plot(x, pw(x, 0.5), color=C1, ls="-")
ax.plot(x, pw(x, 2/3), color=C2, ls="--")
ax.plot(x, pw(x, 1.0), color=C3, ls="-.")
xl = np.linspace(-1.2, np.log(4.2), 300); ax.plot(xl, np.exp(xl), color=C4, ls=(0, (1, 1.5)), lw=2.4)
ax.plot([0], [1], "o", color=INK, ms=6, mec=SURF, mew=1.5)
for xb, col in [(-0.5, C1), (-2/3, C2), (-1, C3)]:
    ax.plot([xb], [0], "o", color=col, ms=7, mec=SURF, mew=1.5, clip_on=False, zorder=5)
ax.text(-1.2, 3.0, "Age = where the curve hits $a=0$:\n"
        r"  radiation  $t_0=\frac{1}{2}H_0^{-1}$" "\n"
        r"  matter      $t_0=\frac{2}{3}H_0^{-1}$" "\n"
        r"  empty       $t_0=H_0^{-1}$" "\n"
        r"  $\Lambda$ only    never: infinitely old", fontsize=9.5, va="center")
ax.text(np.log(4.2)+0.05, 4.05, r"$\Lambda$ only", fontsize=10, va="center")
ax.text(1.63, 2.6, "empty", fontsize=10, va="center")
ax.text(1.63, 2.27, "matter", fontsize=10, va="center")
ax.text(1.63, 1.98, "radiation", fontsize=10, va="center")
ax.annotate("all share $a=1$ and slope $H_0$ today", xy=(0, 1), xytext=(0.15, 0.35), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.set_xlim(-1.25, 2.1); ax.set_ylim(0, 4.2)
ax.set_xlabel(r"$H_0\,(t-t_0)$"); ax.set_ylabel(r"$a(t)$")
ax.set_title("Same expansion rate today, different pasts", loc="left")
save(fig, "model_universes_single_component.png")

# ---------- F4: matter + curvature ----------
def closed(O0, th):
    A = O0/(2*(O0-1)); B = O0/(2*(O0-1)**1.5)
    return A*(1-np.cos(th)), B*(th-np.sin(th))
def openu(O0, et):
    A = O0/(2*(1-O0)); B = O0/(2*(1-O0)**1.5)
    return A*(np.cosh(et)-1), B*(np.sinh(et)-et)
def t0_closed(O0): return O0/(2*(O0-1)**1.5)*np.arccos((2-O0)/O0) - 1/(O0-1)
def t0_open(O0): return 1/(1-O0) - O0/(2*(1-O0)**1.5)*np.arccosh((2-O0)/O0)
fig, axs = plt.subplots(1, 2, figsize=(10, 4.3))
for ax, (Oo, Oc), xr in [(axs[0], (0.9, 1.1), (-1, 3)), (axs[1], (0.3, 2.0), (-1, 6.5))]:
    a1, t1 = openu(Oo, np.linspace(0, 6, 3000)); ax.plot(t1 - t0_open(Oo), a1, color=C1, ls="-", label=rf"$\Omega_0={Oo:g}$ (open)")
    tt = np.linspace(0, 10, 400); ax.plot(tt - 2/3, (1.5*tt)**(2/3), color=C2, ls="--", label=r"$\Omega_0=1$ (flat)")
    a2, t2 = closed(Oc, np.linspace(0, 2*np.pi, 3000)); ax.plot(t2 - t0_closed(Oc), a2, color=C3, ls="-.", label=rf"$\Omega_0={Oc:g}$ (closed)")
    ax.plot([0], [1], "o", color=INK, ms=6, mec=SURF, mew=1.5)
    ax.set_xlim(*xr); ax.set_xlabel(r"$H_0\,(t-t_0)$"); ax.set_ylabel(r"$a(t)$"); ax.legend(loc="upper left", fontsize=9.5)
axs[0].set_ylim(0, 3.2); axs[1].set_ylim(0, 4)
axs[0].set_title(r"(a) $\Omega_0=0.9$ vs $1.1$: twins today", loc="left")
axs[1].set_title(r"(b) $\Omega_0=2$: the full cycloid", loc="left")
axs[1].annotate("Big Crunch", xy=(2*np.pi*1 - t0_closed(2.0), 0), xytext=(4.0, 0.6), fontsize=9.5,
                arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
save(fig, "model_universes_matter_curvature.png")

# ---------- F5: the potential picture ----------
fig, axs = plt.subplots(1, 2, figsize=(10, 5.2))
ax = axs[0]; aa = np.linspace(0.02, 4, 600); U = -1/(2*aa)
ax.plot(aa, U, color=INK, lw=2)
for E, col, ls, lab in [(0.25, C1, "-", r"$\mathcal{E}>0$: open, coasts forever"), (0.0, C2, "--", r"$\mathcal{E}=0$: flat, just escapes"), (-0.35, C3, "-.", r"$\mathcal{E}<0$: closed, turns round")]:
    amax = 4 if E >= 0 else -1/(2*E)
    ax.plot([1/(-2*(-10)), min(amax, 4)], [E, E], color=col, ls=ls, lw=2, label=lab)
ax.fill_between(aa, U, -3, where=aa > -1/(2*-0.35), color=GRID, alpha=0.0)
ax.annotate(r"turnaround $a_{\max}$", xy=(1/(0.7), -0.35), xytext=(2.0, -0.85), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.set_ylim(-1.6, 0.5); ax.set_xlim(0, 4)
ax.set_xlabel(r"$a$"); ax.set_ylabel(r"$\mathcal{V}(a)$ and energy $\mathcal{E}$")
ax.set_title(r"(a) matter + curvature: $\mathcal{V}=-\Omega_0/(2a)$", loc="left"); ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), fontsize=9.5)
ax = axs[1]; Omx, OLx = 1.0, 0.5; aa = np.linspace(0.05, 2.6, 600); U = -0.5*(Omx/aa + OLx*aa**2)
ax.plot(aa, U, color=INK, lw=2)
Umax = -0.75
ax.plot([0.05, 2.6], [-0.55, -0.55], color=C1, ls="-", lw=2, label="above the hill: Big Bang, then Big Chill")
ax.plot([0.05, 2.6], [-0.735, -0.735], color=C2, ls="--", lw=2, label="just above: loiters near the top")
# below hill: two disjoint allowed regions
from scipy.optimize import brentq
Eb = -0.95
r1 = brentq(lambda x: -0.5*(Omx/x + OLx*x**2) - Eb, 0.05, 1.0); r2 = brentq(lambda x: -0.5*(Omx/x + OLx*x**2) - Eb, 1.0, 2.6)
ax.plot([0.05, r1], [Eb, Eb], color=C3, ls="-.", lw=2, label="below, left: Big Bang, then Big Crunch")
ax.plot([r2, 2.6], [Eb, Eb], color=C4, ls=(0, (1, 1.5)), lw=2.4, label="below, right: Big Bounce (no Bang)")
ax.plot([1.0], [Umax], "o", color=INK, ms=7, mec=SURF, mew=1.5)
ax.annotate("Einstein static universe\n(ball balanced on the crest)", xy=(1.0, Umax), xytext=(1.25, -0.3), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.set_ylim(-1.7, 0.05); ax.set_xlim(0, 2.6)
ax.set_xlabel(r"$a$"); ax.set_ylabel(r"$\mathcal{V}(a)$ and energy $\mathcal{E}$")
ax.set_title(r"(b) matter + $\Lambda$ + curvature: a hill", loc="left"); ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.17), fontsize=9.5)
save(fig, "model_universes_potential.png")

# ---------- F6: (Omega_m, Omega_Lambda) phase diagram ----------
def classify(om, ol):
    ok = 1 - om - ol
    if ol < 0: return 2
    if ol == 0: return 2 if om > 1 else 1
    if ok >= 0: return 1
    D = 4*ok**3 + 27*ol*om**2
    if D >= 0: return 1
    xm = np.sqrt(-ok/(3*ol))
    return 0 if xm < 1 else 2
M, L = np.meshgrid(np.linspace(0, 3, 601), np.linspace(-1, 3, 801))
Z = np.vectorize(classify)(M, L)
fig, ax = plt.subplots(figsize=(7, 6))
from matplotlib.colors import ListedColormap
ax.contourf(M, L, Z, levels=[-0.5, 0.5, 1.5, 2.5], colors=["#cde2fb", "#f3f2ee", "#fbd9c8"])
ax.contour(M, L, Z, levels=[0.5, 1.5], colors=[INK2], linewidths=1.2)
mm = np.linspace(0, 3, 10)
ax.plot(mm, 1 - mm, color=INK, ls="--", lw=1.4); ax.text(1.35, -0.22, "flat ($\\kappa=0$)", fontsize=10)
ax.plot(mm, mm/2, color=INK, ls=":", lw=1.4); ax.text(2.05, 1.62, "accelerating today\n(above dotted line)", fontsize=9.5)
ax.text(0.15, 2.55, "Big Bounce\n(no Big Bang)", fontsize=11)
ax.text(1.4, 0.6, "Big Bang,\nthen Big Chill", fontsize=11)
ax.text(2.2, -0.6, "Big Crunch", fontsize=11)
ax.text(0.12, 0.3, r"$\kappa=-1$", fontsize=10, color=INK2); ax.text(0.9, 1.0, r"$\kappa=+1$", fontsize=10, color=INK2)
pts = [(0.315, 0.685, "us"), (0.315, -0.315, ""), (0.315, 1.7364, "loiterer"), (0.315, 1.8, "bouncer")]
for om, ol, lab in pts:
    ax.plot([om], [ol], "o", color=INK, ms=6, mec=SURF, mew=1.5)
for om, ol, lab, dx, dy in [(0.315, 0.685, r"our universe ($\Lambda$CDM)", 0.06, -0.12), (0.315, -0.315, r"$\Omega_{\Lambda,0}=-0.315$", 0.06, -0.05), (0.315, 1.7364, "loiterer (1.7364)", 0.07, -0.13), (0.315, 1.8, "bouncer (1.8)", 0.07, 0.03)]:
    ax.text(om+dx, ol+dy, lab, fontsize=9.5)
ax.set_xlim(0, 3); ax.set_ylim(-1, 3)
ax.set_xlabel(r"$\Omega_{m,0}$"); ax.set_ylabel(r"$\Omega_{\Lambda,0}$")
ax.set_title("Fates of matter + $\\Lambda$ universes (radiation neglected)", loc="left")
save(fig, "model_universes_phase_diagram.png")

# ---------- F7: four futures with Omega_m = 0.315 ----------
def run(OLx, tspan):
    def rhs(t, y): return [y[1], -0.315/(2*y[0]**2) + OLx*y[0]]
    ev = lambda t, y: y[0] - 0.003; ev.terminal = True
    f = solve_ivp(rhs, (0, tspan[1]), [1, 1], events=ev, max_step=0.005, rtol=1e-10, atol=1e-12)
    b = solve_ivp(rhs, (0, tspan[0]), [1, 1], events=ev, max_step=0.005, rtol=1e-10, atol=1e-12)
    return np.concatenate([b.t[::-1], f.t]), np.concatenate([b.y[0][::-1], f.y[0]])
fig, ax = plt.subplots(figsize=(7, 4.6))
for OLx, col, ls, lab in [(0.685, C1, "-", r"$\Omega_{\Lambda,0}=0.685$ (our universe)"), (-0.315, C2, "--", r"$\Omega_{\Lambda,0}=-0.315$"), (1.7364, C3, "-.", r"$\Omega_{\Lambda,0}=1.7364$"), (1.8, C4, (0, (1, 1.5)), r"$\Omega_{\Lambda,0}=1.8$")]:
    t, y = run(OLx, (-6, 4.6)); ax.plot(t, y, color=col, ls=ls, lw=2.2, label=lab)
ax.plot([0], [1], "o", color=INK, ms=6, mec=SURF, mew=1.5)
ax.text(-5.9, 0.53, "loiters at $a\\approx0.45$", fontsize=9.5)
ax.text(-2.4, 1.05, "bounces at\n$a\\approx0.55$", fontsize=9.5)
ax.text(3.45, 0.3, "Big\nCrunch", fontsize=9.5)
ax.set_xlim(-6, 4.6); ax.set_ylim(0, 3)
ax.set_xlabel(r"$H_0\,(t-t_0)$"); ax.set_ylabel(r"$a(t)$"); ax.legend(loc="upper left", fontsize=9.5)
ax.set_title(r"Four universes with $\Omega_{m,0}=0.315$ and the same $H_0$", loc="left")
save(fig, "model_universes_four_futures.png")

# ---------- F8: LCDM a(t) and distances ----------
def E(a): return np.sqrt(Or/a**4 + Om/a**3 + OL)
tH = 977.792/67.4  # Gyr
aa = np.logspace(-8, 0.6, 300)
tt = np.array([quad(lambda x: 1/(x*E(x)), 0, A, limit=200)[0] for A in aa])*tH*1e9  # years
fig, axs = plt.subplots(1, 2, figsize=(10.5, 4.4))
ax = axs[0]
ax.loglog(tt, aa, color=C1, lw=2.2)
trm, tml, t0 = 0.0505e6, 10.29e9, 13.79e9
for tv, lab in [(trm, r"$t_{rm}\approx 50\,000$ yr"), (tml, r"$t_{m\Lambda}$"), (t0, r"$t_0$")]:
    ax.axvline(tv, color=INK2, lw=1, ls=":")
ax.text(trm*1.3, 2e-8, r"$t_{rm}\approx 5\times10^{4}$ yr", fontsize=9.5, color=INK2)
ax.text(tml*0.035, 2e-8, r"$t_{m\Lambda}$, $t_0$", fontsize=9.5, color=INK2)
ts = np.logspace(0, 4.2, 10); ax.loglog(ts, 2.9e-4*(ts/trm)**0.5*1.0, color=INK2, lw=1, ls="--")
ax.text(30, 2.9e-4*(30/trm)**0.5*2.2, r"$\propto t^{1/2}$", fontsize=10)
ts = np.logspace(6.5, 10, 10); ax.loglog(ts, 0.77*(ts/tml)**(2/3)/1.0*0.75, color=INK2, lw=1, ls="--")
ax.text(1e7, 0.77*(1e7/tml)**(2/3)*0.3, r"$\propto t^{2/3}$", fontsize=10)
ax.set_xlim(1, 1e11); ax.set_ylim(1e-8, 4)
ax.set_xlabel("cosmic time $t$ (years)"); ax.set_ylabel("$a(t)$")
ax.set_title(r"(a) $\Lambda$CDM: scale factor", loc="left")
ax = axs[1]
zz = np.logspace(-2, 3, 300)
dp0 = np.array([quad(lambda x: 1/(x*x*E(x)), 1/(1+z), 1, limit=200)[0] for z in zz])
ax.semilogx(zz, dp0, color=C1, lw=2.2, label=r"$d_p(t_0)$: distance now")
ax.semilogx(zz, dp0/(1+zz), color=C2, lw=2.2, ls="--", label=r"$d_p(t_e)$: distance at emission")
for yv, lab in [(3.18, "particle horizon 3.18"), (1.15, "event horizon 1.15"), (1.0, "")]:
    ax.axhline(yv, color=INK2, lw=0.9, ls=":")
ax.text(0.012, 3.25, r"particle horizon, $3.18\,c/H_0$", fontsize=9.5, color=INK2)
ax.text(0.012, 1.22, r"event horizon, $1.15\,c/H_0$", fontsize=9.5, color=INK2)
ax.text(0.012, 0.86, r"Hubble distance $c/H_0$", fontsize=9.5, color=INK2)
ax.plot([1.59], [0.403], "o", color=C2, ms=7, mec=SURF, mew=1.5); ax.annotate(r"peak: $z=1.6$, $0.40\,c/H_0$", xy=(1.59, 0.403), xytext=(3.0, 0.58), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=1))
ax.set_ylim(0, 3.6); ax.set_xlim(0.01, 1000)
ax.set_xlabel("redshift $z$"); ax.set_ylabel(r"proper distance ($c/H_0$)"); ax.legend(loc="upper left", fontsize=9.5, bbox_to_anchor=(0, 0.86))
ax.set_title(r"(b) $\Lambda$CDM: distances", loc="left")
save(fig, "model_universes_benchmark.png")

# ---------- F9: closed universe conformal diagram ----------
fig, ax = plt.subplots(figsize=(4.4, 7.4))
ax.add_patch(plt.Rectangle((0, 0), np.pi, 2*np.pi, fill=False, ec=INK2, lw=1.2))
eta = np.linspace(0, np.pi, 50)
ax.plot(eta, eta, color=C1, lw=2.2); ax.plot(np.pi - eta, np.pi + eta, color=C1, lw=2.2)
ax.axhline(np.pi, color=C2, ls="--", lw=1.4)
ax.text(np.pi/2, -0.35, "Big Bang ($\\theta=0$)", ha="center", fontsize=10)
ax.text(np.pi/2, 2*np.pi+0.15, "Big Crunch ($\\theta=2\\pi$)", ha="center", fontsize=10)
ax.text(0.08, np.pi+0.12, "maximum expansion", fontsize=9.5, color=C2)
ax.text(0.95, 0.35, "light leaves\nus at the Bang", fontsize=9.5)
ax.text(1.85, 1.15, "reaches the\nantipode at\nmax expansion", fontsize=9.5)
ax.text(0.1, 2*np.pi-1.45, "arrives back\nat the Crunch", fontsize=9.5)
ax.set_xlim(-0.1, np.pi+0.1); ax.set_ylim(-0.6, 2*np.pi+0.5)
ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(["0\n(us)", r"$\pi/2$", "$\\pi$\n(antipode)"])
ax.set_yticks([0, np.pi, 2*np.pi]); ax.set_yticklabels(["0", r"$\pi$", r"$2\pi$"])
ax.set_xlabel(r"comoving angle $\chi=r/R_0$"); ax.set_ylabel(r"development angle $\theta$ = conformal time")
ax.set_title("Closed, matter-only universe", loc="left"); ax.grid(False); ax.set_aspect("equal")
save(fig, "model_universes_closed_conformal.png")
