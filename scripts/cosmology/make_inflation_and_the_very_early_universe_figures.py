# Figures for the "Inflation and the Very Early Universe" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_inflation_and_the_very_early_universe_figures.py docs/astrophysics/figures scripts/cosmology/data
# The data directory must contain the r-n_s contour lines of Balkenhol et al. 2026 (arXiv:2512.10613),
#   SPA_BK_r_ns_contour_lines.txt and SPA_BK_DESI_r_ns_contour_lines.txt,
#   from https://github.com/Lbalkenhol/r_ns_2025/tree/main/contour_lines
# Model predictions follow theory_models.py in the same repository.
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad, solve_ivp

OUT, DATA = sys.argv[1], sys.argv[2]
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
    fig.tight_layout(); fig.savefig(f"{OUT}/inflation_and_the_very_early_universe_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- the cosmological model (Planck 2018) and units ----------
H0_si = 67.4e3/3.0856776e22                 # s^-1
hbarGeVs = 6.582119569e-25                  # GeV s
H0 = H0_si*hbarGeVs                          # GeV
Om, Or, OL = 0.315, 9.21e-5, 0.685
Mpl = 2.435e18                               # reduced Planck mass, GeV
T0 = 2.7255*8.617333e-14                     # GeV
Mpc, c = 3.0856776e22, 2.99792458e8
Dstar = 13864.0                              # comoving distance to last scattering, Mpc
Ok_max = 0.005                               # |1 - Omega_0| allowed by the CMB and BAO
# Standard Model relativistic degrees of freedom, a smooth approximation (energy g_* and entropy g_*s), T in GeV
_lT = np.log10([1e-5, 1e-4, 3e-4, 1e-3, 3e-3, 0.03, 0.1, 0.15, 0.25, 1, 5, 30, 100, 300])
_g = np.log10([3.36, 3.36, 6.0, 10.4, 10.75, 10.75, 14.0, 20.0, 55.0, 70.0, 80.0, 90.0, 103.0, 106.75])
_gs = np.log10([3.91, 3.91, 6.5, 10.4, 10.75, 10.75, 14.0, 20.0, 55.0, 70.0, 80.0, 90.0, 103.0, 106.75])
def gstar(T):
    return 10**np.interp(np.log10(T), _lT, _g)
def gstars(T):
    return 10**np.interp(np.log10(T), _lT, _gs)

def one_minus_omega(a):
    """|1 - Omega| in the hot Big Bang, for |Omega_k0| = Ok_max, with g_* steps in the radiation."""
    T = T0/a*(3.91/gstars(T0/a))**(1/3)
    Or_eff = Or*(gstar(T)/3.36)*(3.91/gstars(T))**(4/3)
    E2 = Or_eff/a**4 + Om/a**3 + OL
    return Ok_max/(a*a*E2)

# ---------- the flatness problem in numbers ----------
a_eq = 1/(1 + 3402)
a_nuc = 2.7255/7.69e8
tP = 5.391e-44
H_P = 1/(2*tP)*hbarGeVs                     # radiation era, H = 1/2t
# solve for a at the Planck time with g_* = 106.75
OrP = Or*(106.75/3.36)*(3.91/106.75)**(4/3)
a_P = (H0**2*OrP/H_P**2)**0.25
for lab, a in [("radiation-matter equality", a_eq), ("nucleosynthesis", a_nuc), ("Planck time", a_P)]:
    print("|1 - Omega| at %s (a = %.2e): %.1e" % (lab, a, one_minus_omega(a)))
t_years = 200*1e6/3.156e7
print("if |1-Omega| = 1e-6 at t = 200 s, it reaches 1 at t ~ %.0f yr (radiation era, |1-Omega| ~ t)" % t_years)

# ---------- inflation at V^(1/4) = 1e16 GeV with instant reheating ----------
As = 2.10e-9
r_max = 0.034
V14_max = (1.5*np.pi**2*As*r_max)**0.25*Mpl
H_max = np.sqrt((V14_max**4)/3)/Mpl
print("r < %.3f: V^(1/4) < %.2e GeV, H < %.1e GeV" % (r_max, V14_max, H_max))
V14 = 1e16
V = V14**4
He = np.sqrt(V/3)/Mpl                          # GeV
g_rh = 106.75
Trh = (30*V/(np.pi**2*g_rh))**0.25
ae = (3.91/g_rh)**(1/3)*T0/Trh
N_H0 = np.log(ae*He/H0)
N_Dstar = np.log(ae*He*Dstar*Mpc/(c*hbarGeVs))
N_flat = N_H0 + 0.5*np.log(1/Ok_max)
print("V^(1/4) = 1e16 GeV: H = %.2e GeV = %.2e s^-1 (1/H = %.1e s); T_rh = %.2e GeV = %.1e K; a_e = %.2e" %
      (He, He/hbarGeVs, hbarGeVs/He, Trh, Trh/8.617333e-14, ae))
print("e-folds: c/H0 inside Hubble radius N > %.1f; whole sphere of last scattering N > %.1f; flatness to %.3f N > %.1f" % (N_H0, N_Dstar, Ok_max, N_flat))
print("r for V^(1/4)=1e16: %.4f" % (V/(1.5*np.pi**2*As*Mpl**4)))
R_end = Dstar*Mpc*ae
print("observable universe (radius %.0f Mpc) at end of inflation: %.2e m; Hubble radius c/H_inf = %.1e m" % (Dstar, R_end, c*hbarGeVs/He))
for N in (60, 65):
    print("  N=%d: radius before inflation %.1e m; temperature drop factor e^-N = %.1e; monopole dilution e^-3N = %.1e; duration %.1e s"
          % (N, R_end*np.exp(-N), np.exp(-N), np.exp(-3*N), N*hbarGeVs/He))
eps_L0 = OL*4790.0                              # MeV m^-3
V_si = V/(1.97327e-16)**3*1e3                    # GeV^4 -> MeV m^-3
print("V = %.1e MeV m^-3; today's Lambda %.0f MeV m^-3; ratio %.1e" % (V_si, eps_L0, V_si/eps_L0))

# ---------- Figure: flatness ----------
fig, ax = plt.subplots(figsize=(9.5, 4.8))
la = np.linspace(np.log10(a_P), 0, 800)
ax.plot(la, np.log10(one_minus_omega(10**la)), color=C2, label=r"hot Big Bang, run backwards from $|1-\Omega_0| = 0.005$")
N = 65
la_e = np.log10(ae); la_i = la_e - N/np.log(10)
lb = np.linspace(la_i, la_e, 50)
y_e = np.log10(one_minus_omega(ae))
y_i = y_e + 2*N/np.log(10)
ax.plot(lb, y_i - 2*(lb - la_i), color=C1, label=r"with 65 e-folds of inflation, starting from $|1-\Omega| \sim 10$")
la2 = np.linspace(la_e, 0, 400)
ax.plot(la2, np.log10(one_minus_omega(10**la2)), color=C1, lw=1.2, ls=(0, (4, 2)))
for x, lab, ha in [(np.log10(a_P), "Planck time\n(no inflation)", "right"), (la_e, "end of inflation", "left"), (np.log10(a_nuc), "nucleosynthesis", "right"), (np.log10(a_eq), "equality", "center"), (0, "today", "center")]:
    ax.axvline(x, color=GRID, lw=1, zorder=0)
    ax.text(x + (0.4 if ha == "left" else -0.4 if ha == "right" else 0), 2.5, lab, ha=ha, va="bottom", fontsize=9, color=INK2)
ax.set_xlim(la_i - 1, 1.5); ax.set_ylim(-66, 2)
ax.set_xlabel(r"scale factor, $\log_{10} a$"); ax.set_ylabel(r"$\log_{10}|1 - \Omega|$")
ax.legend(loc="lower right", fontsize=9.5)
ax.set_title("The flatness problem", loc="left", pad=34)
save(fig, "flatness")

# ---------- Figure: comoving Hubble radius and the conformal diagram ----------
fig, axs = plt.subplots(1, 2, figsize=(12, 4.9), gridspec_kw={"width_ratios": [1.15, 1]})
ax = axs[0]
la_r = np.linspace(la_e, 0.6, 600)
aa = 10**la_r
T = T0/aa*(3.91/gstars(T0/aa))**(1/3)
E = np.sqrt(Or*(gstar(T)/3.36)*(3.91/gstars(T))**(4/3)/aa**4 + Om/aa**3 + OL)
RH = 1/(aa*E)                                  # comoving Hubble radius in units of c/H0
RH_e = H0/(ae*He)
la_inf = np.linspace(la_i, la_e, 50)
ax.plot(la_inf, np.log10(RH_e) + (la_e - la_inf), color=C1, label="during inflation, $\\propto 1/a$")
ax.plot(la_r, np.log10(RH), color=C2, label="hot Big Bang ($\\propto a$, then $a^{1/2}$)")
for scale, lab, col in [(1.0, "today's Hubble radius, $c/H_0$", INK), (10*Mpc/(c/H0_si), "a 10 Mpc region (a cluster)", C3)]:
    y = np.log10(scale)
    ax.axhline(y, color=col, lw=1.1, ls="--")
    ax.text(-27, y + 0.8, lab, fontsize=9.5, color=col)
ax.text(la_i + 1, -21, "scales leave\nthe Hubble radius", fontsize=9.5, color=C1)
ax.text(-12, -21, "...and re-enter\nit much later", fontsize=9.5, color=C2)
ax.set_xlim(la_i - 1, 1.5); ax.set_ylim(-30, 8)
ax.set_xlabel(r"scale factor, $\log_{10} a$"); ax.set_ylabel(r"$\log_{10}$ [comoving Hubble radius / $(c/H_0)$]")
ax.legend(loc="lower right", fontsize=9)
ax.set_title("(a) the shrinking Hubble sphere", loc="left")
ax = axs[1]
eta_star, eta0 = 280.0, Dstar + 280.0          # conformal times in Mpc (c = 1)
ax.axhspan(-16000, 0, color=C1, alpha=0.10, lw=0)
ax.axhline(0, color=INK2, lw=1)
ax.text(-16500, -1300, "$\\tau = 0$: the Big Bang without inflation", fontsize=9, color=INK2, bbox=dict(fc=SURF, ec="none", alpha=0.85, pad=1))
ax.text(-16500, -6500, "inflation adds\nconformal time here\n(far more than shown)", fontsize=9, color=C1, bbox=dict(fc=SURF, ec="none", alpha=0.85, pad=1))
ax.plot([0, -Dstar], [eta0, eta_star], color=INK, lw=1.4); ax.plot([0, Dstar], [eta0, eta_star], color=INK, lw=1.4)
ax.plot([0], [eta0], "o", color=INK, ms=6); ax.text(400, eta0 + 200, "us, today", fontsize=9.5)
ax.axhline(eta_star, color=C4, lw=2.2)
ax.text(-Dstar*0.6, eta_star + 600, "last scattering", fontsize=9.5, color=INK2)
for s in (-1, 1):
    x0 = s*Dstar
    ax.plot([x0, x0 - s*eta_star], [eta_star, 0], color=C2, lw=2)
    ax.plot([x0, x0 + s*eta_star], [eta_star, 0], color=C2, lw=2)
    ax.plot([x0, x0 - s*(eta_star + 16000)], [eta_star, -16000], color=C2, lw=1.2, ls=":")
    ax.plot([x0, x0 + s*(eta_star + 16000)], [eta_star, -16000], color=C2, lw=1.2, ls=":")
    ax.plot([x0], [eta_star], "o", color=C2, ms=6)
ax.annotate("past light cones overlap\nonly if inflation happened", xy=(0, -Dstar + eta_star), xytext=(1500, -9500), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.set_xlim(-17000, 17000); ax.set_ylim(-16000, 16000)
ax.set_xlabel("comoving distance (Mpc)"); ax.set_ylabel(r"conformal time $c\tau$ (Mpc)")
ax.set_title("(b) conformal diagram", loc="left")
save(fig, "horizon")

# ---------- Figure: slow roll in a plateau potential (units M_Pl = 1) ----------
k = np.sqrt(2/3)
Vf = lambda p: (1 - np.exp(-k*p))**2
dVf = lambda p: 2*k*np.exp(-k*p)*(1 - np.exp(-k*p))
def rhs(t, y):
    p, dp, Nn = y
    H = np.sqrt((0.5*dp*dp + Vf(p))/3)
    return [dp, -3*H*dp - dVf(p), H]
p_i = 5.75                                      # field value giving ~79 e-folds
dp_i = -dVf(p_i)/(3*np.sqrt(Vf(p_i)/3))         # start on the slow-roll attractor
sol = solve_ivp(rhs, (0, 1600), [p_i, dp_i, 0], max_step=0.05, rtol=1e-9, atol=1e-11)
p, dp, Nn = sol.y; t = sol.t
H = np.sqrt((0.5*dp*dp + Vf(p))/3)
epsH = 0.5*dp*dp/H**2
w = (0.5*dp*dp - Vf(p))/(0.5*dp*dp + Vf(p))
iend = np.argmax(epsH >= 1); N_end = Nn[iend]
print("Starobinsky run: total e-folds to end of inflation %.1f, phi_end = %.2f" % (N_end, p[iend]))
p60 = np.interp(N_end - 55, Nn, p)
fig, axs = plt.subplots(1, 2, figsize=(12, 4.6))
ax = axs[0]
pp = np.linspace(-2.5, 7, 600)
ax.plot(pp, Vf(pp), color=INK)
ax.plot([p_i], [Vf(p_i)], "o", color=C1, ms=8, mec=SURF, mew=1.5, zorder=5)
ax.plot([p60], [Vf(p60)], "o", color=C3, ms=8, mec=SURF, mew=1.5, zorder=5)
ax.plot([p[iend]], [Vf(p[iend])], "o", color=C2, ms=8, mec=SURF, mew=1.5, zorder=5)
ax.annotate("start: slow roll\non the plateau", xy=(p_i, Vf(p_i)), xytext=(4.6, 0.62), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.annotate("55 e-folds before the end:\nCMB scales leave the\nHubble radius", xy=(p60, Vf(p60)), xytext=(2.6, 0.45), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.annotate("inflation ends\n($\\epsilon = 1$)", xy=(p[iend], Vf(p[iend])), xytext=(1.1, 0.2), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.annotate("oscillations:\nreheating", xy=(-0.05, 0.01), xytext=(-2.4, 0.3), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.set_xlim(-2.5, 7); ax.set_ylim(-0.03, 1.15)
ax.set_xlabel(r"inflaton field $\phi$ (reduced Planck units)"); ax.set_ylabel(r"$V(\phi)/V_0$")
ax.set_title(r"(a) a plateau potential, $V_0(1 - e^{-\sqrt{2/3}\,\phi})^2$", loc="left")
ax = axs[1]
Nx = Nn - N_end
during = Nx <= 0.02
ax.plot(Nx[during], w[during], color=C1, lw=1.6, label=r"equation of state $w = P/\varepsilon$")
ax.plot(Nx[during], epsH[during], color=C2, lw=1.6, ls="--", label=r"$\epsilon = -\dot H/H^2$")
# after inflation: average w over the fast oscillations
after = ~during
win = 400
w_avg = np.convolve(w, np.ones(win)/win, mode="same")
ok = after & (np.arange(len(w)) > iend + win) & (np.arange(len(w)) < len(w) - win)
ax.plot(Nx[after], w[after], color=C1, lw=0.5, alpha=0.35)
ax.annotate("after inflation the field oscillates:\n$w$ swings between $-1$ and $+1$\nand averages to 0, like matter", xy=(0.8, 0.7), xytext=(-42, 0.5), fontsize=9, color=INK2, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
print("mean w over oscillations: %.3f; e-folds simulated after the end: %.1f" % (w_avg[ok].mean() if ok.any() else np.nan, Nn[-1] - N_end))
ax.axhline(-1/3, color=INK2, lw=0.8, ls=":"); ax.text(-58, -0.28, "$w = -1/3$: acceleration stops", fontsize=9, color=INK2)
ax.set_xlim(-62, 5.2); ax.set_ylim(-1.15, 1.25)
ax.set_xlabel("e-folds relative to the end of inflation"); ax.set_ylabel("")
ax.legend(loc="upper left", fontsize=9.5)
ax.set_title("(b) the field's equation of state", loc="left")
save(fig, "slow_roll")

# ---------- Figure: n_s and r ----------
fig, ax = plt.subplots(figsize=(8.4, 5.4))
for fname, col, lab in [("SPA_BK_r_ns_contour_lines.txt", C1, "CMB (Planck, ACT, SPT, BICEP/Keck)"),
                        ("SPA_BK_DESI_r_ns_contour_lines.txt", C2, "CMB + DESI BAO")]:
    d = np.loadtxt(f"{DATA}/{fname}")
    for (ci, alpha) in [(2, 0.18), (0, 0.38)]:
        x, y = d[:, ci], np.maximum(d[:, ci + 1], 1e-4)
        ax.fill(x, y, color=col, alpha=alpha, lw=0, label=lab if ci == 0 else None)
        ax.plot(x, y, color=col, lw=0.8)
Ns = np.linspace(50, 60, 50)
for pw, ls, lab in [(2, "-", r"$V \propto \phi^2$"), (1, "--", r"$V \propto \phi$"), (2/3, "-.", r"$V \propto \phi^{2/3}$")]:
    ns = (4*Ns - pw - 4)/(4*Ns + pw); r = 8*(1 - ns)*pw/(2 + pw)
    ax.plot(ns, r, color=INK, ls=ls, lw=1.6, label=lab + " ($N_\\star$ = 50 to 60)")
ns_s, r_s = 1 - 2/Ns, 12/Ns**2
ax.plot(ns_s, r_s, color=C3, lw=3, solid_capstyle="round", label="plateau ($R^2$, Higgs), $N_\\star$ = 50 to 60")
ax.axvline(1, color=INK2, lw=0.8, ls=":"); ax.text(0.9985, 0.15, "scale invariant", rotation=90, fontsize=9, color=INK2, ha="right")
ax.set_yscale("log"); ax.set_xlim(0.94, 1.003); ax.set_ylim(1e-3, 0.3)
ax.set_xlabel(r"scalar spectral index $n_s$"); ax.set_ylabel(r"tensor-to-scalar ratio $r$")
ax.legend(loc="lower right", fontsize=9)
ax.set_title("Inflation models against the data", loc="left")
for pw in (2, 1, 2/3):
    for Nq in (50, 60):
        ns = (4*Nq - pw - 4)/(4*Nq + pw); print("p=%.2f N=%d: ns=%.4f r=%.4f" % (pw, Nq, ns, 8*(1 - ns)*pw/(2 + pw)))
for Nq in (51, 55, 60):
    print("plateau N=%d: ns=%.4f r=%.4f" % (Nq, 1 - 2/Nq, 12/Nq**2))
save(fig, "ns_r")
