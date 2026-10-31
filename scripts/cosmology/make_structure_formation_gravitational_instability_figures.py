# Figures for the "Structure Formation: Gravitational Instability" chapter of the cosmology notes.
# Usage: python3 scripts/cosmology/make_structure_formation_gravitational_instability_figures.py docs/astrophysics/figures scripts/cosmology/data
# Needs the CAMB Boltzmann code (pip install camb; Lewis, Challinor & Lasenby 2000, https://camb.info).
# The data directory must contain desi_dr2_bao.txt, the DESI DR2 BAO distances (its header gives the source table).
import sys
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, quad, simpson
from scipy.special import spherical_jn
import camb

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
    fig.tight_layout(); fig.savefig(f"{OUT}/structure_formation_gravitational_instability_{name}.png", dpi=150); plt.close(fig); print("wrote", name)

# ---------- Planck 2018 best fit (TT,TE,EE+lowE+lensing) ----------
h = 0.6736
PL = dict(H0=67.36, ombh2=0.02237, omch2=0.1200, mnu=0.06, num_massive_neutrinos=1, tau=0.0544, As=2.0989e-9, ns=0.9649)
pars = camb.set_params(**PL)
pars.set_matter_power(redshifts=[0.0], kmax=60.0)
res = camb.get_results(pars)
kh, _, pk = res.get_matter_power_spectrum(minkh=1e-4, maxkh=40, npoints=800)
k = kh*h; P = pk[0]/h**3                       # k in Mpc^-1, P in Mpc^3
der = res.get_derived_params()
print("CAMB: sigma8 = %.4f, r_drag = %.2f Mpc, z_drag = %.1f, age = %.3f Gyr" % (res.get_sigma8_0(), der["rdrag"], der["zdrag"], der["age"]))
Om = (PL["ombh2"] + PL["omch2"] + 0.06/93.14)/h**2; Ob = PL["ombh2"]/h**2
Or = 9.21e-5; OL = 1 - Om - Or
H0s = 67.36e3/3.0856776e22
rho_c0 = 3*H0s**2/(8*np.pi*6.674e-11)                       # kg m^-3
Msun, Mpc = 1.98892e30, 3.0856776e22
rho_m0_Msun = Om*rho_c0*Mpc**3/Msun                         # M_sun Mpc^-3
print("Omega_m = %.4f, rho_m0 = %.3e M_sun/Mpc^3; M(1 Mpc) = %.3e M_sun" % (Om, rho_m0_Msun, 4*np.pi/3*rho_m0_Msun))
a_eq = Or/Om
E = lambda a: np.sqrt(Or/a**4 + Om/a**3 + OL)
k_eq = a_eq*E(a_eq)*67.36/299792.458
print("equality: z = %.0f, k_eq = %.4f Mpc^-1, comoving Hubble radius %.0f Mpc; P(k) peaks at k = %.4f Mpc^-1" % (1/a_eq - 1, k_eq, 1/k_eq, k[np.argmax(P)]))

# ---------- Figure: growth of a sub-Hubble matter perturbation ----------
def growth(Om_, Or_, OL_, lna0=np.log(1e-6)):
    def rhs(x, y):
        a = np.exp(x); E2 = Or_/a**4 + Om_/a**3 + OL_
        dlnH = 0.5*(-4*Or_/a**4 - 3*Om_/a**3)/E2
        Omega_m_a = Om_/a**3/E2
        return [y[1], -(2 + dlnH)*y[1] + 1.5*Omega_m_a*y[0]]
    xs = np.linspace(lna0, np.log(3.0), 2000)
    s = solve_ivp(rhs, (xs[0], xs[-1]), [1.0, 1.0], t_eval=xs, rtol=1e-9, atol=1e-12)
    return np.exp(xs), s.y[0], s.y[1]/s.y[0]
a, D, f = growth(Om, Or, OL)
a2, D2, _ = growth(1/(1 + a_eq), a_eq/(1 + a_eq), 0.0)    # no dark energy, same matter-radiation equality
i1 = np.argmin(abs(a - 1)); i_eq = np.argmin(abs(a - a_eq))
print("growth from a=1e-6 to equality: %.2f (log growth); equality to today: %.0f; no dark energy (same equality) would give %.0f" % (D[i_eq], D[i1]/D[i_eq], D2[np.argmin(abs(a2 - 1))]/D2[np.argmin(abs(a2 - a_eq))]))
for zq in (0, 0.5, 1, 2):
    j = np.argmin(abs(a - 1/(1 + zq)))
    Omz = Om*(1 + zq)**3/E(1/(1 + zq))**2
    print("z=%.1f: D/a relative to matter era = %.3f, f = %.3f, Omega_m(z)^0.55 = %.3f" % (zq, (D[j]/a[j])/(D[np.argmin(abs(a - 1e-2))]/1e-2), f[j], Omz**0.55))
fig, axs = plt.subplots(1, 2, figsize=(12, 4.6))
ax = axs[0]
ax.loglog(a, D, color=C1, label=r"our universe ($\Lambda$CDM)")
ax.loglog(a2, D2, color=C2, ls="--", label="matter and radiation only")
ax.loglog(a, D[i_eq]*a/a_eq, color=INK2, lw=1, ls=":", label=r"$\delta \propto a$")
ax.axvline(a_eq, color=GRID, lw=6, zorder=0); ax.text(a_eq*1.25, 1.3, "matter-radiation\nequality", fontsize=9, color=INK2)
ax.axvline(1, color=INK2, lw=0.8); ax.text(0.9, 1.3, "today", fontsize=9, color=INK2, ha="right")
ax.text(1.5e-6, 40, "radiation era:\nslow, logarithmic growth", fontsize=9.5)
ax.set_xlim(1e-6, 3); ax.set_ylim(1, 3e4)
ax.set_xlabel("scale factor $a$"); ax.set_ylabel(r"density contrast $\delta$ (arbitrary units)")
ax.legend(loc="upper left", fontsize=9.5, bbox_to_anchor=(0, 0.88))
ax.set_title("(a) growth of a mode inside the Hubble radius", loc="left")
ax = axs[1]
m = a > 0.05
ref = D[np.argmin(abs(a - 0.05))]/0.05
ax.plot(1/a[m] - 1, D[m]/a[m]/ref, color=C1, label=r"growth relative to $\delta \propto a$")
Omz = Om/a[m]**3/E(a[m])**2
ax.plot(1/a[m] - 1, f[m], color=C3, ls="--", label=r"growth rate $f = d\ln\delta/d\ln a$")
ax.plot(1/a[m] - 1, Omz**0.55, color=INK2, lw=1, ls=":", label=r"$\Omega_m(z)^{0.55}$")
ax.set_xlim(5, 0); ax.set_ylim(0, 1.08)
ax.set_xlabel("redshift $z$"); ax.legend(loc="lower left", fontsize=9.5)
ax.set_title("(b) dark energy switches growth off", loc="left")
save(fig, "growth")

# ---------- Figure: the Jeans mass of the baryons ----------
zz = np.logspace(np.log10(10), np.log10(3000), 400)
ev = res.get_background_redshift_evolution(zz, ["x_e", "T_b"], format="array")
xe, Tb = ev[:, 0], ev[:, 1]
G, kB, mp, c = 6.674e-11, 1.380649e-23, 1.67262e-27, 2.99792458e8
Yp = 0.245
rho_m = Om*rho_c0*(1 + zz)**3
rho_b = Ob*rho_c0*(1 + zz)**3
Og = 5.44e-5
R = 3*Ob/(4*Og)/(1 + zz)
cs_before = c/np.sqrt(3*(1 + R))
rho_tot = rho_c0*(Om*(1 + zz)**3 + Or*(1 + zz)**4)
lamJ_before = cs_before*np.sqrt(np.pi/(G*rho_tot))
MJ_before = rho_b*4*np.pi/3*lamJ_before**3/Msun
mu = 1/((1 - Yp)*(1 + xe) + Yp/4)                           # mean particle mass in m_p (H ionised fraction x_e)
cs_after = np.sqrt(5/3*kB*Tb/(mu*mp))
lamJ_after = cs_after*np.sqrt(np.pi/(G*rho_m))
MJ_after = rho_b*4*np.pi/3*lamJ_after**3/Msun
jd = np.argmin(abs(zz - 1090))
print("z=1090: Jeans length before %.2f Mpc (proper), M_J = %.1e M_sun; after: c_s = %.1f km/s, lambda_J = %.0f pc, M_J = %.1e M_sun" %
      (lamJ_before[jd]/Mpc, MJ_before[jd], cs_after[jd]/1e3, lamJ_after[jd]/Mpc*1e6, MJ_after[jd]))
for zq in (500, 200, 100, 30, 10):
    j = np.argmin(abs(zz - zq)); print("  z=%d: T_b = %.0f K (T_CMB %.0f K), M_J = %.1e M_sun" % (zq, Tb[j], 2.7255*(1 + zq), MJ_after[j]))
fig, ax = plt.subplots(figsize=(8.6, 4.8))
before = zz > 1090
ax.loglog(zz[before], MJ_before[before], color=C2, label="photon-baryon fluid (before decoupling)")
ax.loglog(zz[~before], MJ_after[~before], color=C1, label="baryon gas (after decoupling)")
ax.plot([1090, 1090], [MJ_after[jd], MJ_before[jd]], color=INK2, lw=1, ls="--")
for M_, lab in [(1e15, "rich cluster"), (1e12, "Milky Way halo"), (1e9, "dwarf galaxy"), (1e6, "globular cluster")]:
    ax.axhline(M_, color=GRID, lw=1, zorder=0); ax.text(2900, M_*1.6, lab, fontsize=9, color=INK2)
ax.annotate("decoupling: the Jeans mass\nfalls by a factor of $10^{13}$", xy=(1090, 1e12), xytext=(330, 2e9), fontsize=9.5,
            arrowprops=dict(arrowstyle="-|>", color=INK2, lw=0.9))
ax.invert_xaxis(); ax.set_xlim(3000, 10); ax.set_ylim(1e3, 1e21)
ax.set_xlabel("redshift $z$"); ax.set_ylabel(r"baryonic Jeans mass ($M_\odot$)")
ax.legend(loc="upper right", fontsize=9.5)
ax.set_title("The smallest baryonic mass that can collapse", loc="left")
save(fig, "jeans_mass")

# ---------- Figure: power spectrum, hot versus cold, and sigma(M) ----------
p2 = camb.set_params(H0=67.36, ombh2=0.02237, omch2=1e-6, omnuh2=0.12, num_massive_neutrinos=3, tau=0.0544, As=2.0989e-9, ns=0.9649)
p2.set_matter_power(redshifts=[0.0], kmax=60.0)
r2 = camb.get_results(p2)
kh2, _, pk2 = r2.get_matter_power_spectrum(minkh=1e-4, maxkh=40, npoints=800)
P2 = pk2[0]/h**3
print("hot dark matter (3 x %.2f eV neutrinos): sigma8 = %.3f" % (0.12*93.14/3, r2.get_sigma8_0()))
def sigma_R(Rmpc, Pk):
    x = k*Rmpc
    W = 3*spherical_jn(1, x)/x
    return np.sqrt(simpson(Pk*W**2*k**3, x=np.log(k))/(2*np.pi**2))
Rs = np.logspace(-2, 2.5, 120)
sig_c = np.array([sigma_R(r, P) for r in Rs]); sig_h = np.array([sigma_R(r, P2) for r in Rs])
Ms = 4*np.pi/3*rho_m0_Msun*Rs**3
M1 = np.interp(0, -np.log(sig_c), np.log(Ms)); print("sigma(M) = 1 at M = %.2e M_sun (R = %.1f Mpc)" % (np.exp(M1), (np.exp(M1)/(4*np.pi/3*rho_m0_Msun))**(1/3)))
print("sigma at R = 8/h Mpc: %.3f" % sigma_R(8/h, P))
for Mq in (1e8, 1e10, 1e12, 1e14, 1e16):
    print("  M = %.0e: sigma = %.2f (CDM), slope dln sigma/dln M = %.3f" % (Mq, np.interp(np.log(Mq), np.log(Ms), sig_c),
          np.interp(np.log(Mq), np.log(Ms), np.gradient(np.log(sig_c), np.log(Ms)))))
fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.8))
ax = axs[0]
ax.loglog(k, P, color=C1, label="cold dark matter (our universe)")
cut = np.argmax(P2 < 3)
ax.loglog(k[:cut], P2[:cut], color=C2, ls="--", label="hot dark matter (neutrinos of 3.8 eV)")
kk = np.array([1e-4, 3e-3]); ax.loglog(kk, P[0]*(kk/k[0])**0.965, color=INK2, lw=1, ls=":")
ax.text(2.2e-4, 1.4e3, r"$P \propto k^{n_s}$", fontsize=10, color=INK2)
ax.axvline(k_eq, color=GRID, lw=6, zorder=0); ax.text(k_eq/1.25, 3e2, "scale that entered\nthe Hubble radius\nat equality", fontsize=9, color=INK2, ha="right")
ax.set_xlim(1e-4, 20); ax.set_ylim(1, 1e5)
ax.set_xlabel(r"wavenumber $k$ (Mpc$^{-1}$)"); ax.set_ylabel(r"$P(k)$ (Mpc$^3$), today, linear")
sec = ax.secondary_xaxis("top", functions=(lambda x: 2*np.pi/np.clip(x, 1e-9, None), lambda l: 2*np.pi/np.clip(l, 1e-9, None)))
sec.set_xlabel("wavelength $2\\pi/k$ (Mpc)")
ax.legend(loc="lower left", fontsize=9.5)
ax.set_title("(a) the matter power spectrum", loc="left", pad=8)
ax = axs[1]
ax.loglog(Ms, sig_c, color=C1, label="cold dark matter")
ax.loglog(Ms, np.maximum(sig_h, 1e-4), color=C2, ls="--", label="hot dark matter")
ax.axhline(1, color=INK2, lw=0.8, ls=":")
ax.text(3e5, 1.2, r"$\delta M/M = 1$: these masses are collapsing now", fontsize=9, color=INK2)
ax.set_xlim(1e5, 1e18); ax.set_ylim(1e-2, 30)
ax.set_xlabel(r"mass $M$ ($M_\odot$)"); ax.set_ylabel(r"rms fluctuation $\delta M/M$ today (linear)")
ax.legend(loc="lower left", fontsize=9.5)
ax.set_title("(b) small masses first: bottom-up", loc="left", pad=8)
save(fig, "power_spectrum")

# ---------- Figure: BAO in the correlation function and the DESI distances ----------
r = np.linspace(20, 200, 400)
kf = np.logspace(-4, np.log10(40), 6000)
Pf = np.interp(np.log(kf), np.log(k), P)
damp = np.exp(-(kf*1.0)**2)                                  # mild smoothing for the oscillatory integral
xi = np.array([simpson(Pf*damp*kf**2*np.sinc(kf*ri/np.pi), x=kf)/(2*np.pi**2) for ri in r])
ib = np.argmax(np.where(r > 120, xi, -1))
print("BAO peak in xi(r) at r = %.1f Mpc (r_drag = %.1f)" % (r[ib], der["rdrag"]))
d = np.array([ln.split() for ln in open(f"{DATA}/desi_dr2_bao.txt") if ln.strip() and not ln.startswith("#")])
fig, axs = plt.subplots(1, 2, figsize=(12.4, 4.6))
ax = axs[0]
ax.plot(r, r**2*xi, color=C1)
ax.axvline(der["rdrag"], color=C2, lw=1, ls="--"); ax.text(der["rdrag"] + 3, (r**2*xi).max()*0.95, "sound horizon\n%.0f Mpc" % der["rdrag"], fontsize=9.5, color=C2)
ax.set_xlabel("comoving separation $r$ (Mpc)"); ax.set_ylabel(r"$r^2\,\xi(r)$ (Mpc$^2$)")
ax.set_title("(a) the BAO bump in the correlation function", loc="left")
ax = axs[1]
zf = np.linspace(0.05, 2.6, 300)
def DM(z):
    return np.array([quad(lambda x: 1/E(1/(1 + x)), 0, zi)[0] for zi in np.atleast_1d(z)])*299792.458/67.36
DMz = DM(zf); DHz = 299792.458/67.36/E(1/(1 + zf)); DVz = (zf*DMz**2*DHz)**(1/3)
rd = der["rdrag"]
ax.plot(zf, DMz/rd/np.sqrt(zf), color=C1, label=r"$D_M/r_d$ (transverse)")
ax.plot(zf, DHz/rd*zf/np.sqrt(zf), color=C3, label=r"$z\,D_H/r_d$ (radial)")
ax.plot(zf, DVz/rd/np.sqrt(zf), color=INK2, lw=1.2, ls="--", label=r"$D_V/r_d$ (average)")
for row in d:
    zt, kind, val, err = float(row[1]), row[2], float(row[3]), float(row[4])
    col, fac = {"DM": (C1, 1), "DH": (C3, zt), "DV": (INK2, 1)}[kind]
    ax.errorbar([zt], [val*fac/np.sqrt(zt)], yerr=[err*fac/np.sqrt(zt)], fmt="o", ms=5, color=col, mec=SURF, mew=0.8, capsize=0, zorder=4)
ax.set_xlabel("redshift $z$"); ax.set_ylabel(r"distance $/\,(r_d\sqrt{z})$")
ax.legend(loc="lower right", fontsize=9.5); ax.set_xlim(0, 2.6)
ax.set_title("(b) DESI measurements against the Planck model", loc="left")
save(fig, "bao")
