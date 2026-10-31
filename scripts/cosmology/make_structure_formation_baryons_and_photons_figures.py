# Figures for the "Structure Formation: Baryons and Photons" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_structure_formation_baryons_and_photons_figures.py docs/astrophysics/figures
# Needs the CAMB Boltzmann code (pip install camb) for the ionisation history and sigma(M).
# The star-formation history is the fitting formula of Madau & Dickinson 2014 (ARA&A 52, 415, arXiv:1403.0007).
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, quad, simpson
from scipy.optimize import brentq
from scipy.special import spherical_jn
import camb

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
    fig.tight_layout(); fig.savefig(f"{OUT}/structure_formation_baryons_and_photons_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- model (Planck 2018) ----------
h = 0.6736
PL = dict(H0=67.36, ombh2=0.02237, omch2=0.1200, mnu=0.06, num_massive_neutrinos=1, tau=0.0544, As=2.0989e-9, ns=0.9649)
Om = (PL["ombh2"] + PL["omch2"] + 0.06/93.14)/h**2; Ob = PL["ombh2"]/h**2; Or = 9.21e-5; OL = 1 - Om - Or
H0s = 67.36e3/3.0856776e22
G, kB, mp, c, sigT = 6.674e-11, 1.380649e-23, 1.67262e-27, 2.99792458e8, 6.6524587e-29
mH = 1.6735575e-27
Msun, Mpc, Gyr = 1.98892e30, 3.0856776e22, 3.15576e16
rho_c0 = 3*H0s**2/(8*np.pi*G)
Yp = 0.245
E = lambda z: np.sqrt(Or*(1 + z)**4 + Om*(1 + z)**3 + OL)
age = lambda z: quad(lambda x: 1/((1 + x)*E(x)), z, np.inf, limit=300)[0]/H0s/Gyr
t0 = age(0)
print("age today %.3f Gyr" % t0)

# ---------- reionisation: optical depth ----------
rho_b0 = Ob*rho_c0
nH0 = (1 - Yp)*rho_b0/mH; nHe0 = Yp*rho_b0/(4.0026*1.66054e-27)
print("n_H0 = %.4f m^-3, n_He0 = %.4f m^-3, n_b0 = %.4f m^-3" % (nH0, nHe0, rho_b0/mp))
def tau_inst(zre, zHe=3.5):
    f = lambda z: (nH0 + nHe0 + (nHe0 if z < zHe else 0.0))*(1 + z)**2/E(z)
    return c*sigT/H0s*quad(f, 0, zre, points=[zHe], limit=200)[0]
Gamma0 = c*sigT*nH0
print("Gamma_0 (hydrogen only) = %.3e s^-1 = %.2e Gyr^-1 = %.4f H0" % (Gamma0, Gamma0*Gyr, Gamma0/H0s))
tau_obs, dtau = 0.0544, 0.0073
zre = brentq(lambda z: tau_inst(z) - tau_obs, 3, 30)
zlo = brentq(lambda z: tau_inst(z) - (tau_obs - dtau), 3, 30); zhi = brentq(lambda z: tau_inst(z) - (tau_obs + dtau), 3, 30)
print("instantaneous reionisation: tau = %.4f -> z_re = %.2f (%.2f to %.2f), age %.0f Myr; fraction of photons scattered %.3f" %
      (tau_obs, zre, zlo, zhi, age(zre)*1e3, 1 - np.exp(-tau_obs)))
print("tau from z<6 alone: %.4f" % tau_inst(6.0))
pars = camb.set_params(**PL)
res = camb.get_results(pars)
zz = np.linspace(0, 20, 400)
xe = res.get_background_redshift_evolution(zz, ["x_e"], format="array")[:, 0]
fig, axs = plt.subplots(1, 2, figsize=(12, 4.6))
ax = axs[0]
zg = np.linspace(3.6, 20, 200)
ax.plot(zg, [tau_inst(z) for z in zg], color=C1, label="instantaneous reionisation at $z_{\\rm re}$")
ax.axhspan(tau_obs - dtau, tau_obs + dtau, color=C2, alpha=0.25, lw=0)
ax.axhline(tau_obs, color=C2, lw=1)
ax.text(14, 0.040, "Planck: $\\tau = 0.054 \\pm 0.007$", color=C2, fontsize=9.5)
ax.axvspan(zlo, zhi, color=GRID, zorder=0)
ax.annotate("$z_{\\rm re} \\approx %.1f$" % zre, xy=(zre, tau_obs), xytext=(11, 0.03), fontsize=10, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.set_xlim(3.5, 20); ax.set_ylim(0, 0.16)
ax.set_xlabel("redshift of reionisation $z_{\\rm re}$"); ax.set_ylabel(r"optical depth $\tau$")
ax.legend(loc="upper left", fontsize=9.5)
ax.set_title("(a) the CMB optical depth", loc="left")
ax = axs[1]
ax.plot(zz, xe, color=C1, label="Planck best fit (smooth step)")
ax.axvspan(5.3, 6.0, color=C3, alpha=0.2, lw=0); ax.text(5.35, 0.25, "end of\nreionisation\n(quasar spectra)", fontsize=9, color=C3)
ax.axvspan(10, 14.4, color=C4, alpha=0.18, lw=0); ax.text(10.3, 0.7, "galaxies seen\nby JWST", fontsize=9, color=INK2)
ax.text(15.5, 0.12, "mostly\nneutral", fontsize=9, color=INK2)
ax.text(0.3, 1.2, "helium doubly\nionised ($z < 3.5$)", fontsize=9, color=INK2)
ax.set_xlim(0, 20); ax.set_ylim(0, 1.32)
ax.set_xlabel("redshift $z$"); ax.set_ylabel("free electrons per hydrogen nucleus")
ax.legend(loc="upper right", fontsize=9.5)
ax.set_title("(b) the ionisation history", loc="left")
save(fig, "reionisation")

# ---------- cosmic star-formation history (Madau & Dickinson 2014) ----------
psi = lambda z: 0.015*(1 + z)**2.7/(1 + ((1 + z)/2.9)**5.6)          # M_sun yr^-1 Mpc^-3 (Salpeter IMF, h = 0.7)
zs = np.linspace(0, 12, 600)
zpk = zs[np.argmax(psi(zs))]
print("SFR density: today %.4f, peak %.4f at z = %.2f (age %.2f Gyr, lookback %.2f Gyr); ratio %.1f" % (psi(0), psi(zpk), zpk, age(zpk), t0 - age(zpk), psi(zpk)/psi(0)))
dt = lambda z: 1/((1 + z)*E(z)*H0s)/3.15576e7                        # yr per unit z
formed = lambda z1, z2: quad(lambda z: psi(z)*dt(z), z1, z2, limit=200)[0]
tot = formed(0, 20)
R_ret = 0.27
print("stars formed: total %.2e M_sun/Mpc^3; surviving (1-R) %.2e; Omega_* = %.4f" % (tot, (1 - R_ret)*tot, (1 - R_ret)*tot*Msun/Mpc**3/rho_c0))
for zq in (1, 2, 3, 6):
    print("  fraction formed before z=%g: %.2f" % (zq, formed(zq, 20)/tot))
print("SFR at z=%.1f: %.4f (%.2f of today)" % (zre, psi(zre), psi(zre)/psi(0)))
fig, ax = plt.subplots(figsize=(8.6, 4.6))
lb = np.array([t0 - age(z) for z in zs])
ax.plot(lb, psi(zs), color=C1)
ax.fill_between(lb, 0, psi(zs), color=C1, alpha=0.12, lw=0)
ax.axvline(t0 - age(zre), color=C2, lw=1, ls="--"); ax.text(t0 - age(zre) - 0.15, 0.115, "reionisation", fontsize=9.5, color=C2, ha="right")
ax.annotate("peak: $z \\approx %.1f$" % zpk, xy=(t0 - age(zpk), psi(zpk)), xytext=(5.0, 0.125), fontsize=9.5, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.set_xlim(0, t0); ax.set_ylim(0, 0.15)
ax.set_xlabel("lookback time (Gyr)"); ax.set_ylabel(r"star formation rate ($M_\odot$ yr$^{-1}$ Mpc$^{-3}$)")
zt = [0, 0.5, 1, 2, 3, 5, 8]
sec = ax.secondary_xaxis("top", functions=(lambda x: x, lambda x: x)); sec.set_xticks([t0 - age(z) for z in zt]); sec.set_xticklabels([str(z) for z in zt]); sec.set_xlabel("redshift")
ax.set_title("The cosmic history of star formation", loc="left", pad=8)
save(fig, "star_formation")

# ---------- spherical collapse (top hat in a matter-dominated universe) ----------
th = np.linspace(1e-3, 2*np.pi, 800)
Rn = (1 - np.cos(th))/2                     # R / R_turnaround
tn = (th - np.sin(th))/np.pi                # t / t_turnaround
dlin = 3/20*(6*(th - np.sin(th)))**(2/3)
with np.errstate(divide="ignore"):                  # R = 0 at collapse (theta = 2 pi), where delta diverges
    dnl = 9*(th - np.sin(th))**2/(2*(1 - np.cos(th))**3) - 1
print("turnaround: delta = %.3f, delta_lin = %.3f; collapse: delta_lin = %.3f; virial overdensity 18 pi^2 = %.1f" %
      (9*np.pi**2/16 - 1, 3/20*(6*np.pi)**(2/3), 3/20*(12*np.pi)**(2/3), 18*np.pi**2))
fig, axs = plt.subplots(1, 2, figsize=(12, 4.4))
ax = axs[0]
ax.plot(tn, Rn, color=C1, label="overdense sphere")
tt = np.linspace(0, 2.2, 200)
Rbg = 0.25*(6*np.pi*tt)**(2/3)              # same mass at the mean density: R = (1/4)(6 pi t)^(2/3) in these units
ax.plot(tt, Rbg, color=INK2, lw=1, ls=":", label="same mass at the mean density")
ax.axhline(0.5, color=C2, lw=1, ls="--"); ax.text(0.40, 0.40, "virial radius, half of turnaround", fontsize=9, color=C2)
ax.plot([1], [1], "o", color=C1, ms=6); ax.text(0.95, 1.05, "turnaround", fontsize=9.5, ha="center")
ax.plot([2], [0], "o", color=C1, ms=6); ax.text(1.97, 0.07, "collapse", fontsize=9.5, ha="right")
ax.set_xlim(0, 2.2); ax.set_ylim(0, 1.6)
ax.set_xlabel("time / turnaround time"); ax.set_ylabel("radius / turnaround radius")
ax.legend(loc="upper left", fontsize=9.5)
ax.set_title("(a) the life of a top-hat overdensity", loc="left")
ax = axs[1]
ax.semilogy(tn, 1 + dnl, color=C1, label=r"actual density contrast $1 + \delta$")
ax.semilogy(tn, 1 + dlin, color=C2, ls="--", label=r"linear theory $1 + \delta_{\rm lin}$")
ax.axhline(1 + 178, color=INK2, lw=0.8, ls=":"); ax.text(0.3, 120, r"virialised: $1 + \delta = 18\pi^2 \approx 178$", fontsize=9, color=INK2)
ax.annotate(r"$\delta_{\rm lin} = 1.686$", xy=(2, 2.686), xytext=(1.25, 8), fontsize=10, arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.set_xlim(0, 2.05); ax.set_ylim(1, 1e3)
ax.set_xlabel("time / turnaround time"); ax.legend(loc="upper left", fontsize=9.5)
ax.set_title("(b) linear theory versus reality", loc="left")
save(fig, "spherical_collapse")

# ---------- halo collapse redshifts, virial temperatures, cooling ----------
p2 = camb.set_params(**PL); p2.set_matter_power(redshifts=[0.0], kmax=60.0)
r2 = camb.get_results(p2)
kh, _, pk = r2.get_matter_power_spectrum(minkh=1e-4, maxkh=40, npoints=800)
k = kh*h; P = pk[0]/h**3
rho_m0_Msun = Om*rho_c0*Mpc**3/Msun
def sigma_M(M):
    R = (M/(4*np.pi/3*rho_m0_Msun))**(1/3); x = k*R; W = 3*spherical_jn(1, x)/x
    return np.sqrt(simpson(P*W**2*k**3, x=np.log(k))/(2*np.pi**2))
def growthD():
    def rhs(x, y):
        a = np.exp(x); E2 = Or/a**4 + Om/a**3 + OL
        return [y[1], -(2 + 0.5*(-4*Or/a**4 - 3*Om/a**3)/E2)*y[1] + 1.5*Om/a**3/E2*y[0]]
    xs = np.linspace(np.log(1e-3), 0, 1000)
    s = solve_ivp(rhs, (xs[0], 0), [1e-3, 1e-3], t_eval=xs, rtol=1e-10)
    return np.exp(xs), s.y[0]/s.y[0][-1]
aD, D = growthD()
def z_coll(M, nu):
    Dc = 1.686/(nu*sigma_M(M))
    return 1/np.interp(Dc, D, aD) - 1 if Dc < 1 else np.nan
mu_ion = 0.59
def halo(M, z):
    rho_vir = 178*Om*rho_c0*(1 + z)**3
    R = (3*M*Msun/(4*np.pi*rho_vir))**(1/3)
    T = mu_ion*mp*G*M*Msun/(2*kB*R)
    n_gas = Ob/Om*rho_vir/mp                 # nucleons per m^3 in the halo gas (mean)
    return R/Mpc*1e3, T, n_gas*1e-6         # kpc, K, cm^-3
def t_cool_ff(n_b_cm3, T):
    nH = (1 - Yp)*n_b_cm3; nHe = Yp/4*n_b_cm3
    ne = nH + 2*nHe; ni_Z2 = nH + 4*nHe; ntot = ne + nH + nHe
    eps = 1.4e-27*np.sqrt(T)*ne*ni_Z2*1.2      # erg s^-1 cm^-3 (free-free, Gaunt factor 1.2)
    return 1.5*ntot*1.380649e-16*T/eps/3.15576e16   # Gyr
rows = []
for M in (1e8, 1e10, 1e12, 1e14, 1e15):
    for nu in (1, 2, 3):
        z = z_coll(M, nu)
        if np.isfinite(z) and z >= 0:
            R, T, n = halo(M, z)
            rows.append((M, nu, z, R, T, n, t_cool_ff(n, T)))
            print("M=%.0e nu=%d: z_coll=%.2f, R_vir=%.0f kpc, T_vir=%.2e K, n_gas=%.2e cm^-3, t_cool(ff)=%.2g Gyr, t_dyn=%.2g Gyr" %
                  (M, nu, z, R, T, n, t_cool_ff(n, T), 1/np.sqrt(G*178*Om*rho_c0*(1 + z)**3)/Gyr))
fig, ax = plt.subplots(figsize=(8.6, 5.2))
Tg = np.logspace(4, 8.3, 200)
for tc, ls, lab in [(t0, "-", "cooling time = age of the universe"), (1.0, "--", "cooling time = 1 Gyr")]:
    n_line = np.array([brentq(lambda ln: np.log(t_cool_ff(10**ln, T)/tc), -12, 6) for T in Tg])
    ax.loglog(10**n_line, Tg, color=INK, ls=ls, lw=1.4, label=lab + " (free-free)")
cols = {1e8: C3, 1e10: C4, 1e12: C1, 1e14: C2, 1e15: INK2}
for M, nu, z, R, T, n, tc in rows:
    ax.plot(n, T, "o", ms=4 + 2*nu, color=cols[M], mec=SURF, mew=1, zorder=4)
for M, lab in [(1e8, r"$10^{8}\,M_\odot$"), (1e10, r"$10^{10}\,M_\odot$"), (1e12, r"$10^{12}\,M_\odot$"), (1e14, r"$10^{14}\,M_\odot$"), (1e15, r"$10^{15}\,M_\odot$")]:
    pts = [(n, T) for MM, nu, z, R, T, n, tc in rows if MM == M]
    if pts:
        ax.plot(*zip(*pts), color=cols[M], lw=1, zorder=3)
        n_, T_ = pts[-1]; ax.text(n_*1.4, T_*1.1, lab, fontsize=9.5, color=cols[M])
ax.axhspan(1e4, 1e6, color=C3, alpha=0.07, lw=0)
ax.text(1.5e-6, 1.8e5, "$10^4$ to $10^6$ K: atomic lines\ncool the gas much faster\nthan free-free", fontsize=9, color=INK2)
ax.text(1.5e-6, 3.5e3, "below $10^4$ K: only molecular\nhydrogen can cool the gas", fontsize=9, color=INK2)
ax.text(0.4, 1.2e6, "cools\nquickly", fontsize=10, color=INK2); ax.text(3e-6, 6e7, "cannot cool:\nstays hot", fontsize=10, color=INK2)
ax.set_xlim(1e-6, 10); ax.set_ylim(2e3, 2e8)
ax.set_xlabel(r"mean gas density in the halo (nucleons cm$^{-3}$)"); ax.set_ylabel("virial temperature (K)")
ax.legend(loc="upper right", fontsize=9)
ax.set_title("Which halos can cool and make a galaxy?", loc="left")
save(fig, "cooling")
