# Brief 02 — QFT Exotic Matter Sources for the Stargate Simulator

Author: Dr. Marcus Chen (QFT / exotic matter)
Scope: real negative-energy physics → simulator features → benchtop crosswalk.
Conventions: SI units; signature (-,+,+,+); ℏc ≈ 1.973×10⁻⁷ eV·m; ρ_Casimir uses parallel-plate ideal conductors unless noted.

---

## 1. Inventory of real negative-energy sources (numbers, not vibes)

**(a) Static Casimir effect (parallel ideal conductors, EM field).**
Energy per unit area: u_A = −(π²/720)(ℏc/d³). Force per area (= |energy density between plates|): P = (π²/240)(ℏc/d⁴).
Numerical between-plate energy density:
- d = 1 µm  → ρ ≈ −1.3×10⁻³ J/m³ (≈ −8.1×10¹⁵ eV/m³)
- d = 100 nm → ρ ≈ −13 J/m³
- d = 10 nm  → ρ ≈ −1.3×10⁵ J/m³
- d = 1 nm   → ρ ≈ −1.3×10⁹ J/m³ (here surface plasmon corrections matter; ideal-conductor formula breaks).

Scaling: ρ ∝ −1/d⁴. Casimir is the only macroscopic-control-knob source: you set d, you get ρ.

**(b) Dynamical Casimir effect (DCE).** Modulating a boundary at frequency ω_d ≳ 2ω_cavity converts virtual photons into real ones; transient regions of T_00 < 0 develop near the moving boundary. Demonstrated on superconducting circuits (Wilson 2011, arXiv:1105.4714) by flux-modulating a SQUID at ~11 GHz to flap the effective end-mirror at ~5% c. Photon flux observed; spectrum ~mK noise temperature; two-mode squeezing confirmed. Static-equivalent ρ at the boundary ~ ℏω_d² / (c² × A_mode) — small in absolute J/m³ but isolable.

**(c) Squeezed vacuum states.** A squeezed mode of squeezing parameter r has ⟨T_00⟩ that dips below the unsqueezed-vacuum value once per optical cycle. Best lab achievement: ~−15 dB squeezing (LIGO/AEI; standard NL-crystal OPOs hit ~−14 dB) → variance ratio ~0.032. Time-averaged negative-energy excursions are O(ℏω/λ³) per cycle and pass quantum-inequality bounds (see §3). Reference meta-analysis: arXiv:1806.01269.

**(d) Quantum field in curved spacetime (Boulware/Unruh/Hartle-Hawking).** Renormalized ⟨T_μν⟩ for scalar fields in a Schwarzschild/Reissner-Nordström background:
- *Boulware*: static, regular at infinity, **diverges negatively at the horizon** — strong WEC violation as r→r_+.
- *Unruh*: post-collapse state, finite on future horizon, outgoing Hawking flux at infinity (~T_H = ℏc³/8πGMk_B; for M_sun ≈ 6.2×10⁻⁸ K).
- *Hartle-Hawking*: thermal equilibrium, regular everywhere outside.
For solar-mass black hole, ρ on the horizon is order −ℏc/r_s⁴ ≈ −10⁻²² J/m³ — astrophysically negligible but conceptually the "free" negative energy. Reference review: Visser, *Lorentzian Wormholes* (1996); recent: arXiv:2307.10307.

**(e) Higher-D Casimir of compactified extra dimensions.** Maldacena-Milekhin-Popov / Maldacena-Milekhin (arXiv:2008.06618) use the Casimir energy of charged massless fermions wound around a compact magnetic-flux loop. In their geometry the line-integrated negative energy along the throat is ∫ρ dl ~ −Nℏc/r_e², where N = number of fermion species and r_e = throat radius. For N ~ N_SM and meter-scale r_e this is ~10²⁴ J·m of negative line-energy density — that's the only known proposal that closes the energy budget for a macroscopic, semiclassically-controlled wormhole.

---

## 2. The MMP / "Humanly traversable" route in detail

**Geometry.** Two near-extremal magnetically-charged Reissner-Nordström black holes, charges ±q, separated by distance L, connected through an AdS₂×S² throat. Magnetic field threads a closed loop through the throat; charged massless 4D fermions become 2D chiral fermions in the lowest Landau level along the loop. The 2D Casimir energy of those chiral fermions sources the NEC violation that holds the throat open.

**Scaling laws (paraphrased from arXiv:2008.06618; verify in §IV–V of the paper).**
- Throat radius r_e set by extremal RN: r_e ~ q·l_P / √α_em (with q the magnetic charge in Dirac units).
- Holding open requires N (number of charged-fermion species in the loop) ≳ q. SM has too few; need beyond-SM dark sector or RS-style 5D KK tower.
- Mass-to-radius: a 1 m throat ⇒ M ~ 10²³ kg per mouth (~Jupiter's moon Io), q ~ 10²⁹ in Dirac units.
- Internal proper time τ_int ~ L_throat/c (seconds for a meter throat).
- External time T_ext ≫ τ_int (boost factor γ huge); external observers wait ~years while traveler experiences seconds → no closed timelike curves form provided mouths stay sub-light.

**Why it isn't built.** (i) Requires magnetic monopoles — none observed; (ii) Requires N≫1 charged massless fermion species — physics beyond SM; (iii) Requires assembling Jupiter-mass extremal black holes at sub-AU separation; (iv) Backreaction of the very fermions sourcing it is a 1-loop calculation: 2-loop and beyond uncontrolled; (v) Stability against generic perturbations is at best marginal (eternal-inflation / Cauchy-horizon analog issues).

**Cost summary.** Free in operations (Casimir is vacuum); cost is in the construction substrate (mass, charge, exotic field content). It is the existence proof that traversable wormholes are not forbidden by QFT+GR — that is the value to us.

---

## 3. Quantum inequalities (Ford-Roman) — the throttle

**Inequality (Ford-Roman, flat 4D, massless scalar, inertial geodesic with Lorentzian sampling time τ₀):**

  ∫ ⟨T_μν u^μ u^ν⟩ · (τ₀/π) / (τ² + τ₀²) dτ  ≥  −3ℏc / (32π² τ₀⁴)

Equivalent statement: |⟨T_00⟩| · τ₀⁴ ≲ ℏc. **The deeper the negative dip, the shorter it can last.**

**Wormhole consequence (Ford-Roman 1995, arXiv:gr-qc/9510071; Pfenning-Ford 1997, arXiv:gr-qc/9711030).** Apply the bound on a geodesic threading the throat. For a throat of radius r_0, requiring static-traversable Morris-Thorne metric ⇒ negative energy must be confined to a band of thickness Δr ≲ (l_P · r_0)^{1/2} (i.e. geometric mean of Planck length and throat radius).
- r_0 = 1 m  ⇒ Δr ≲ 4×10⁻¹⁸ m  (≪ proton radius)
- r_0 = 1 km ⇒ Δr ≲ 1.3×10⁻¹⁶ m
- And ρ in that band must be ~ −10²⁰ × (Schwarzschild density of an equivalent BH).

That is the killer for "naïve" Morris-Thorne wormholes built from generic squeezed vacuum: you cannot fit the required ρ within the band the QI allows. **The MMP construction evades this** because the negative energy lives in a higher-dimensional Casimir geometry, not as a free QFT excitation in 4D Minkowski; the 4D QI is satisfied trivially by the time-averaged stress tensor of the background.

---

## 4. Benchtop today — what we can actually measure

| Effect | Setup | Achieved | Cost (USD) | arXiv/DOI |
|---|---|---|---|---|
| Static Casimir | Sparnaay 1958 (parallel plates, qualitative); Lamoreaux 1997 sphere-plate torsion pendulum, 0.6–6 µm, 5% agreement | F ~ 100 pN at d = 1 µm | $50k–$200k for a modern AFM-Casimir rig | DOI:10.1103/PhysRevLett.78.5 |
| Casimir at MEMS scale | Decca, Mohideen, Capasso microsphere AFM | 1% precision, 100 nm–1 µm | $250k+ | many; e.g. Decca 2007 |
| Dynamical Casimir | Wilson 2011 SQUID-terminated coplanar waveguide, ω_d/2π ≈ 11 GHz | Real-photon emission, two-mode squeezing observed | $500k–$1M (dilution fridge + microwave) | arXiv:1105.4714 |
| Squeezed vacuum (negative ⟨T_00⟩ excursions) | OPO with periodically-poled KTP/LN, balanced homodyne + tomography | −15 dB squeezing (Vahlbruch 2016) | $100k–$300k benchtop | arXiv:1806.01269 |
| Casimir torque | Birefringent plates (Somers 2018) | Measured | $300k | DOI:10.1038/s41586-018-0777-8 |

For *our* simulator-companion experiment, the cheapest credible "negative energy on demand" demonstrator is a homodyne-detected OPO squeezed-light bench (~$100–150k all-in if we buy refurbished). It produces measured negative ⟨T_00⟩ excursions and lets us calibrate the simulator's ANEC accounting against real data.

---

## 5. Three things to put in the simulator

**5a. Per-voxel renormalized stress-energy field T_μν(x,t).**
For each voxel store the 10 independent components plus the energy density ρ = T^00. Color-map ρ on a diverging scale (blue = negative, red = positive, white = 0). Compute:

  ρ_Casimir(x) = −(π²/720) · ℏc / d_eff(x)⁴

where d_eff is the local minimum boundary distance for "Casimir-shell" voxels. For squeezed-mode voxels:

  ρ_squeezed(x,t) = ρ_vac · [cosh(2r) − sinh(2r)·cos(2(ωt − k·x))] − ρ_vac

Render as a volumetric overlay on the wormhole throat; alpha proportional to |ρ|/ρ_QI_bound.

**5b. Integrated negative-energy budget readout.**
Live HUD tracks two scalars:
- E_neg(t) = ∫_{ρ<0} ρ(x,t) d³x  (must equal or exceed the Morris-Thorne requirement E_req = −c⁴ r_0 / G for throat radius r_0).
- Quality factor Q_QI(t) = E_neg / E_FR_bound where E_FR_bound is the Ford-Roman-allowed integral over the current geodesic sample. Q > 1 = unphysical; flash red.

**5c. ANEC integrand & violation indicator.**
Along the central null geodesic γ through the throat compute:
  I_ANEC = ∫_γ T_μν k^μ k^ν dλ
Plot I_ANEC(λ) as a curve under the 3D view; integrated value displayed. ANEC violation (I_ANEC < 0) flashes a "WORMHOLE VIABLE" badge; positive-or-zero kills the badge. Compute on at least 8 sample geodesics (axial + 7 off-axis at r/r_0 = {0.25, 0.5, 0.75, 1.0} pairs) so the user sees the radial profile of the violation, not just the deepest line.

Voxel data needed per cell: {ρ, p_r, p_t, T_μν 4×4, |∇T|, source-tag (Casimir|squeezed|MMP-fermion|none)}.

---

## 6. Three real failure modes that kill traversable wormholes

**6a. Semiclassical backreaction destabilization.** ⟨T_μν⟩ sources Einstein equations linearly, but the source is itself a 1-loop quantity. A small perturbation of the metric perturbs ⟨T_μν⟩, which perturbs the metric again; in most known geometries this loop has positive feedback, throat collapses on timescale ~ r_0/c. MMP claim controlled stability; that claim is 1-loop, 2-loop is open.

**6b. Quantum inequality squeeze.** As §3 shows, for any 4D-local QFT source the negative-energy band width is ~√(l_P · r_0). A 1 m throat needs the exotic matter packed into 4×10⁻¹⁸ m of radial extent — sub-nuclear scale. Any thermal/structural fluctuation smears it and the throat closes. This is why MMP needs the higher-D escape hatch.

**6c. ANEC violation at human scale + chronology protection.** Even if you build the throat, moving the mouths produces closed timelike curves; Hawking's chronology-protection conjecture says vacuum polarization diverges on the would-be Cauchy horizon and destroys the wormhole. Kim-Thorne, Visser, and Maldacena-Milekhin discuss this; the only escape is to keep mouths nearly co-moving forever, which defeats the purpose.

We should treat the simulator as a **constraint visualizer**: it should let the user see *why* every "easy" knob (make ρ deeper / make throat wider / move the mouth) blows one of these three.

---

## 7. Citations

- Maldacena, Milekhin, Popov / Maldacena-Milekhin, "Humanly traversable wormholes," arXiv:2008.06618 (Phys. Rev. D 103, 066007, 2021).
- Maldacena, Milekhin, Popov, "Traversable wormholes in four dimensions," arXiv:1807.04726.
- Ford, Roman, "Quantum field theory constrains traversable wormhole geometries," arXiv:gr-qc/9510071.
- Pfenning, Ford, "Quantum inequalities and singular negative energy densities," arXiv:gr-qc/9711030.
- Kontou, "Wormhole restrictions from quantum energy inequalities," arXiv:2405.05963.
- Wilson et al., "Observation of the Dynamical Casimir Effect in a Superconducting Circuit," arXiv:1105.4714 (Nature 479, 376, 2011).
- Lamoreaux, "Demonstration of the Casimir Force in the 0.6 to 6 µm Range," Phys. Rev. Lett. 78, 5 (1997), DOI:10.1103/PhysRevLett.78.5.
- Sparnaay, "Measurements of attractive forces between flat plates," Physica 24, 751 (1958). [unverified DOI in this draft]
- Vahlbruch et al., 15 dB squeezed light, Phys. Rev. Lett. 117, 110801 (2016). [unverified arxiv id]
- Fewster, Pfenning, Ford et al., "Testing a Quantum Inequality with a Meta-analysis of Data from Squeezed Light," arXiv:1806.01269.
- Renormalized ⟨T_μν⟩ in Boulware/Unruh/Hartle-Hawking, Reissner-Nordström: arXiv:2307.10307 (Phys. Rev. D 108, 125004).
- Visser, *Lorentzian Wormholes: From Einstein to Hawking* (AIP, 1995). ISBN 1-56396-394-9. [book; no arxiv]
- Morris, Thorne, "Wormholes in spacetime and their use for interstellar travel," Am. J. Phys. 56, 395 (1988). [foundational]

Marked [unverified] above are claims I did not re-check from primary source in this brief; flag for Maya/QA before any public quote.

---

## Implementation hand-off (for Kai/backend, Zara/frontend)

- Build a `StressEnergyField` class keyed by voxel index → struct{T[4][4], ρ, source_tag}.
- Provide closed-form ρ_Casimir, ρ_squeezed(t), ρ_MMP(r) as static methods so the renderer can populate voxels analytically before the GR solver runs.
- HUD subscribes to E_neg, Q_QI, I_ANEC reducers updated each tick.
- Default scenario presets: "Morris-Thorne textbook" (fails QI — show user *why*), "MMP throat" (passes; shows scale issue), "Casimir slab" (works at µm scale, throat too small to be a stargate — pedagogical).

— Marcus
