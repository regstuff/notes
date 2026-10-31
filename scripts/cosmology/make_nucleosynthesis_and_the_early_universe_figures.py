# Figures for the "Nucleosynthesis and the Early Universe" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_nucleosynthesis_and_the_early_universe_figures.py docs/astrophysics/figures scripts/cosmology/data/mass_1.mas20.txt
# The mass table is the 2020 Atomic Mass Evaluation (Huang et al. and Wang et al. 2021, Chinese Physics C 45, 030002/3),
# from https://www-nds.iaea.org/amdc/ame2020/mass_1.mas20.txt
# The abundance-versus-eta figure uses the fitting formulas of Kneller & Steigman 2004 (New J. Phys. 6, 117,
# arXiv:astro-ph/0406320), valid for 4 <= eta10 <= 8, and observed values from the PDG 2026 review of BBN.
#
# The neutron-proton calculation uses the Born-approximation weak rates normalised to the neutron lifetime,
# decoupled neutrinos, and the exact e+e- thermodynamics through annihilation (entropy conservation).
# It leaves out radiative, finite-nucleon-mass and incomplete-decoupling corrections, which shift Y_p by ~1%.
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad, solve_ivp
from scipy.interpolate import interp1d
from scipy.optimize import brentq

OUT, AME = sys.argv[1], sys.argv[2]
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
    fig.tight_layout(); fig.savefig(f"{OUT}/nucleosynthesis_and_the_early_universe_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- constants (MeV units, hbar = c = k = 1) ----------
me, Q, mn = 0.51099895, 1.29333, 939.56542   # electron mass, n-p mass difference, neutron mass
BD = 2.224566                                # deuteron binding energy
MPl = 1.220890e22                            # Planck mass
hbar = 6.582119569e-22                       # MeV s
TAU = 878.3                                  # neutron lifetime (s), PDG 2026

def fd(x):
    return 1/(np.exp(np.minimum(x, 700)) + 1)

def thermal_history(dN=0.0, Thi=20.0, Tlo=0.005, n=1500):
    """Photon temperature grid, time, neutrino temperature and H, through e+e- annihilation."""
    def rho_P_e(T):
        E = lambda p: np.sqrt(p*p + me*me)
        r = quad(lambda p: p*p*E(p)*fd(E(p)/T), 0, 60*T + 10*me, limit=200)[0]
        P = quad(lambda p: p**4/E(p)*fd(E(p)/T)/3, 0, 60*T + 10*me, limit=200)[0]
        return 4/(2*np.pi**2)*r, 4/(2*np.pi**2)*P
    T = np.logspace(np.log10(Thi), np.log10(Tlo), n)
    rP = np.array([rho_P_e(x) for x in T])
    rho_g = np.pi**2/15*T**4
    s = (4/3)*rho_g/T + (rP[:, 0] + rP[:, 1])/T          # entropy density of photons + e+e-
    a = (s[0]/s)**(1/3)                                   # comoving entropy conserved
    Tnu = T[0]/a                                          # neutrinos already decoupled
    rho = rho_g + rP[:, 0] + (3 + dN)*(7/8)*(np.pi**2/15)*Tnu**4
    H = np.sqrt(8*np.pi*rho/3)/MPl
    dt = np.diff(np.log(a))/(0.5*(H[1:] + H[:-1]))
    t = np.concatenate([[1/(2*H[0])], 1/(2*H[0]) + np.cumsum(dt)])*hbar
    return T, t, Tnu, H/hbar

def neutron_fraction(T, t, Tnu, tau=TAU, decay=True):
    A = 1/(tau*quad(lambda E: E*np.sqrt(E*E - me*me)*(Q - E)**2, me, Q)[0])
    pe = lambda E: E*np.sqrt(E*E - me*me)
    def rates(Tg, Tn):
        up = 60*max(Tg, Tn) + Q + 5
        np1 = quad(lambda E: pe(E)*(E - Q)**2*fd((E - Q)/Tn)*(1 - fd(E/Tg)), Q, up, limit=200)[0]     # n + nu -> p + e
        np2 = quad(lambda E: pe(E)*(E + Q)**2*fd(E/Tg)*(1 - fd((E + Q)/Tn)), me, up, limit=200)[0]    # n + e+ -> p + nubar
        np3 = quad(lambda E: pe(E)*(Q - E)**2*(1 - fd(E/Tg))*(1 - fd((Q - E)/Tn)), me, Q, limit=200)[0] if decay else 0.0
        pn1 = quad(lambda E: pe(E)*(E - Q)**2*fd(E/Tg)*(1 - fd((E - Q)/Tn)), Q, up, limit=200)[0]     # p + e -> n + nu
        pn2 = quad(lambda E: pe(E)*(E + Q)**2*fd((E + Q)/Tn)*(1 - fd(E/Tg)), me, up, limit=200)[0]    # p + nubar -> n + e+
        return A*(np1 + np2 + np3), A*(pn1 + pn2)
    L = np.array([rates(x, y) for x, y in zip(T, Tnu)])
    lt = np.log(t)
    fnp, fpn = interp1d(lt, L[:, 0]), interp1d(lt, L[:, 1])
    X0 = 1/(1 + np.exp(Q/T[0]))
    sol = solve_ivp(lambda u, X: [np.exp(u)*(fpn(u)*(1 - X[0]) - fnp(u)*X[0])], (lt[0], lt[-1]), [X0],
                    t_eval=lt, method="LSODA", rtol=1e-8, atol=1e-12)
    return sol.y[0], L[:, 0]

T, t, Tnu, H = thermal_history()
Xn, Lnp = neutron_fraction(T, t, Tnu)
Xn_nodecay, _ = neutron_fraction(T, t, Tnu, decay=False)
at = lambda arr, Tq: np.interp(-Tq, -T, arr)
hi = T > 0.3
T_f = np.interp(1, (Lnp/H)[hi][::-1], T[hi][::-1])
T_nuc = 0.075                                 # onset of helium production (see text)
print("t*T^2 early %.3f, late %.3f s MeV^2" % (at(t, 3)*9, at(t, 0.03)*0.03**2))
print("Gamma = H at kT = %.3f MeV, t = %.2f s; n/p there %.3f (equilibrium %.3f)" % (T_f, at(t, T_f), at(Xn, T_f)/(1 - at(Xn, T_f)), np.exp(-Q/T_f)))
print("frozen n/p without decay: %.3f (X_n = %.3f)" % (Xn_nodecay[-1]/(1 - Xn_nodecay[-1]), Xn_nodecay[-1]))
print("at kT = %.3f MeV: t = %.0f s, X_n = %.4f, n/p = %.3f, Y = 2X_n = %.4f" % (T_nuc, at(t, T_nuc), at(Xn, T_nuc), at(Xn, T_nuc)/(1 - at(Xn, T_nuc)), 2*at(Xn, T_nuc)))
for tau in (877.8, 887.7):
    X2, _ = neutron_fraction(T, t, Tnu, tau=tau); print("tau = %.1f s: Y = %.4f" % (tau, 2*at(X2, T_nuc)))
T3, t3, Tnu3, H3 = thermal_history(dN=1.0)
X3, _ = neutron_fraction(T3, t3, Tnu3); print("one extra neutrino: Y = %.4f" % (2*np.interp(-T_nuc, -T3, X3)))
for Tq in (10, 1, 0.1):
    print("kT = %g MeV at t = %.3g s" % (Tq, at(t, Tq)))

# ---------- deuterium: the Saha equation ----------
def D_over_n(kT, eta):
    return 8.14*(1 - 0.12)*eta*(kT/mn)**1.5*np.exp(BD/kT)     # n_p = (1 - X_n) eta n_gamma, X_n ~ 0.12
ETA = 6.1e-10
kT_nuc = brentq(lambda x: D_over_n(x, ETA) - 1, 0.03, 0.2)
print("deuterium Saha: n_D/n_n = 1 at kT = %.4f MeV (T = %.3g K, t = %.0f s)" % (kT_nuc, kT_nuc/8.617333e-11, at(t, kT_nuc)))
print("  at kT = %.3f: n_D/n_n = %.3g" % (T_nuc, D_over_n(T_nuc, ETA)))
for e_ in (ETA*10, ETA/10):
    print("  eta=%.1e: kT_nuc=%.4f" % (e_, brentq(lambda x: D_over_n(x, e_) - 1, 0.03, 0.2)))

# ---------- Figure: neutrons and deuterium ----------
fig, axs = plt.subplots(1, 2, figsize=(11.5, 4.6))
ax = axs[0]
r = Xn/(1 - Xn)
ax.loglog(t, np.exp(-Q/T), color=INK2, ls="--", lw=1.4, label=r"equilibrium, $e^{-Q_n/kT}$")
ax.loglog(t, Xn_nodecay/(1 - Xn_nodecay), color=C3, ls="-.", lw=1.6, label="weak reactions only (no decay)")
ax.loglog(t, r, color=C1, label="full calculation")
ax.axvline(at(t, T_f), color=GRID, lw=6, zorder=0)
ax.annotate("weak freeze-out\n$\\Gamma = H$, $kT \\approx %.1f$ MeV" % T_f, xy=(at(t, T_f), 0.2), xytext=(0.03, 0.035), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
tn = at(t, T_nuc); rn = at(r, T_nuc)
ax.plot([tn], [rn], "o", color=C2, ms=8, mec=SURF, mew=1.5, zorder=5)
ax.annotate("deuterium survives:\n$n/p \\approx 1/%.0f$, $Y \\approx %.3f$" % (1/rn, 2*at(Xn, T_nuc)), xy=(tn, rn), xytext=(25, 0.023), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=C2, lw=0.9))
ax.set_xlim(0.01, 2000); ax.set_ylim(0.01, 1.3)
ax.set_xlabel("time since the Big Bang (s)"); ax.set_ylabel("neutron-to-proton ratio $n/p$")
ax.legend(loc="lower left", fontsize=9)
top = ax.secondary_xaxis("top", functions=(lambda x: np.interp(np.log(np.clip(x, 1e-6, None)), np.log(t), T),
                                           lambda y: np.exp(np.interp(-np.asarray(y), -T, np.log(t)))))
top.set_xticks([3, 1, 0.3, 0.1, 0.05]); top.set_xticklabels(["3", "1", "0.3", "0.1", "0.05"])
top.set_xlabel("$kT$ (MeV)")
ax.set_title("(a) neutrons freeze out, then decay", loc="left", pad=8)
ax = axs[1]
kT = np.linspace(0.04, 0.2, 400)
for e_, col, ls, lab in [(ETA, C1, "-", r"$\eta = 6.1\times10^{-10}$"), (ETA*10, C2, "--", r"$\eta$ ten times larger"), (ETA/10, C3, "-.", r"$\eta$ ten times smaller")]:
    ax.semilogy(kT, D_over_n(kT, e_), color=col, ls=ls, label=lab)
ax.axhline(1, color=INK2, lw=0.8, ls=":")
ax.plot([kT_nuc], [1], "o", color=C1, ms=7, mec=SURF, mew=1.5, zorder=5)
ax.annotate("$kT_{\\rm nuc} \\approx %.3f$ MeV" % kT_nuc, xy=(kT_nuc, 1), xytext=(0.13, 30), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.invert_xaxis(); ax.set_ylim(1e-6, 1e4)
ax.set_xlabel("$kT$ (MeV)"); ax.set_ylabel("$n_D/n_n$ in equilibrium (Saha)")
ax.legend(loc="upper left", fontsize=9.5)
ax.set_title("(b) the deuterium bottleneck", loc="left", pad=8)
save(fig, "neutrons")

# ---------- Figure: binding energy per nucleon ----------
rows = []
for line in open(AME, encoding="latin-1").read().splitlines()[36:]:
    try:
        N, Z, A = int(line[5:9]), int(line[9:14]), int(line[14:19])
        el = line[20:22].strip()
        BA = float(line[54:67].replace("#", ".").strip())/1000      # MeV per nucleon
    except ValueError:
        continue
    rows.append((A, Z, N, el, BA))
best = {}
for A, Z, N, el, BA in rows:
    if A >= 2 and (A not in best or BA > best[A][1]):
        best[A] = (el, BA)
As = np.array(sorted(a for a in best if a <= 70))
Bs = np.array([best[a][1] for a in As])
fig, ax = plt.subplots(figsize=(9, 4.6))
stable = ~np.isin(As, [5, 8])
ax.plot(As, Bs, color=GRID, lw=1.2, zorder=1)
ax.plot(As[stable], Bs[stable], "o", color=C1, ms=5, zorder=3, label="most tightly bound nucleus of each mass number")
ax.plot(As[~stable], Bs[~stable], "o", mfc=SURF, mec=C2, mew=1.8, ms=8, zorder=4, label="mass 5 and 8: none is stable")
labels = {2: "${}^2$H", 3: "${}^3$H", 4: "${}^4$He", 6: "${}^6$Li", 7: "${}^7$Li", 12: "${}^{12}$C", 16: "${}^{16}$O", 56: "${}^{56}$Fe", 62: "${}^{62}$Ni"}
offs = {2: (6, -4), 3: (6, -2), 4: (-6, 8), 6: (0, -16), 7: (4, 6), 12: (-4, 9), 16: (-4, 9), 56: (-6, 9), 62: (-2, -16)}
for A_, lab in labels.items():
    ax.annotate(lab, xy=(A_, best[A_][1]), xytext=offs[A_], textcoords="offset points", fontsize=10, ha="left" if A_ in (2, 3) else "center")
ax.text(4.6, 5.5, "${}^5$He", fontsize=9.5, color=C2, ha="right", va="center"); ax.text(8.6, 7.0, "${}^8$Be", fontsize=9.5, color=C2)
ax.set_xlim(0, 71); ax.set_ylim(0, 9.4)
ax.set_xlabel("mass number $A$"); ax.set_ylabel("binding energy per nucleon (MeV)")
ax.legend(loc="lower right", fontsize=9.5)
ax.set_title("Nuclear binding energies", loc="left")
print("B/A: D %.4f, 3He %.4f, 4He %.4f, 7Li %.4f, 8Be %.4f, 12C %.4f, 56Fe %.4f, 62Ni %.4f" % tuple(
    next(r_[4] for r_ in rows if r_[0] == A_ and r_[3] == el) for A_, el in [(2, "H"), (3, "He"), (4, "He"), (7, "Li"), (8, "Be"), (12, "C"), (56, "Fe"), (62, "Ni")]))
save(fig, "binding_energy")

# ---------- Figure: abundances versus the baryon-to-photon ratio ----------
e10 = np.linspace(4, 8, 300)
Yp = 0.2384 + 0.0016*e10                    # Kneller & Steigman 2004
DH = 46.5*e10**-1.6*1e-5
LiH = e10**2/8.5*1e-10
cmb, dcmb = 6.12, 0.04                      # Planck 2018 Omega_b h^2 = 0.02237 +- 0.00015
obs = [(0.245, 0.003), (2.508e-5, 0.029e-5), (1.45e-10, 0.25e-10)]   # PDG 2026
fig, axs = plt.subplots(3, 1, figsize=(7.4, 8.4), sharex=True)
panels = [(Yp, 1, r"helium-4 mass fraction $Y_p$", (0.236, 0.256)),
          (DH, 1e5, r"D/H $\times 10^5$", (1.5, 4.6)),
          (LiH, 1e10, r"${}^7$Li/H $\times 10^{10}$", (0, 8.5))]
for ax, (y, sc, lab, yl), (o, do) in zip(axs, panels, obs):
    ax.axvspan(cmb - dcmb, cmb + dcmb, color=C1, alpha=0.25, lw=0, zorder=1)
    ax.axhspan((o - do)*sc, (o + do)*sc, color=C2, alpha=0.30, lw=0, zorder=1)
    ax.plot(e10, y*sc, color=INK, zorder=3)
    ax.set_ylabel(lab); ax.set_ylim(*yl)
axs[0].text(4.1, 0.2455, "observed", color=C2, fontsize=9.5, va="bottom")
axs[0].text(6.2, 0.2375, "CMB", color=C1, fontsize=9.5)
axs[0].text(7.1, 0.2510, "prediction", color=INK, fontsize=9.5)
axs[1].text(4.1, 2.58, "observed (quasar absorbers)", color=C2, fontsize=9.5, va="bottom")
axs[2].text(4.1, 1.05, "observed (old halo stars)", color=C2, fontsize=9.5, va="top")
axs[2].annotate("", xy=(6.3, 1.5), xytext=(6.3, 4.6), arrowprops=dict(arrowstyle="<->", color=INK2, lw=1))
axs[2].text(6.4, 2.6, "the lithium problem:\na factor of about 3", fontsize=9.5)
axs[2].set_xlabel(r"baryon-to-photon ratio $\eta \times 10^{10}$")
axs[0].set_title("Light-element yields and the baryon density", loc="left")
print("KS2004 at CMB eta: Y=%.4f D/H=%.3e Li/H=%.3e; eta10 from D/H = %.2f" % (0.2384 + 0.0016*cmb, 46.5*cmb**-1.6*1e-5, cmb**2/8.5*1e-10, (46.5/2.508)**(1/1.6)))
save(fig, "abundances")
