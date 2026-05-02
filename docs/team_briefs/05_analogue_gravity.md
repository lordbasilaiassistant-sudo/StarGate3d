# Brief 05 — Analogue Gravity: What's Real, What Isn't, What We Can Build

**Author:** Dr. Yusra Okonkwo (experimental physicist, analogue gravity)
**For:** StarGate3d simulator + lab program
**Date:** 2026-05-01

---

## 1. Analogue gravity primer

The field starts with Bill Unruh, 1981, *Phys. Rev. Lett.* **46**, 1351–1353, "Experimental black-hole evaporation." Unruh noticed that sound propagating in a non-uniformly moving fluid obeys the same wave equation as a massless scalar field on a curved Lorentzian background. If the fluid flows faster than the local speed of sound across some surface, phonons upstream of that surface cannot escape — a *sonic horizon*, or "dumb hole." Crucially, the same derivation that yields Hawking radiation from a real black hole, applied here, predicts thermal phonon emission from the sonic horizon at a temperature set by the fluid's "surface gravity" (the gradient of flow velocity at the horizon).

What's actually analogous: the **kinematics**. The wave equation, the horizon as a one-way membrane for the relevant excitations, the mode-mixing across the horizon that produces a thermal spectrum, the existence of negative-norm partner modes inside. Under appropriate conditions (irrotational, barotropic, inviscid flow at low frequencies) the analogy is exact at the level of the linearised wave equation.

What is **not** analogous: dynamics. The fluid background obeys Navier–Stokes / Gross–Pitaevskii, not Einstein's equations. There is no GR backreaction — emitted phonons do not shrink the "horizon" the way Hawking emission shrinks a real BH. There is no genuine causal disconnection (you can always reach in and grab the fluid). And nothing here requires or exhibits exotic matter, closed timelike curves, or topology change. The analogy buys you the *quantum field theory in curved spacetime* half of the problem, never the *Einstein equations* half. Barceló, Liberati & Visser, *Living Rev. Relativity* **14**, 3 (2011), arXiv:gr-qc/0505065, is the canonical review.

## 2. Experiments that actually exist

All citations verified via arXiv / publisher this session.

- **Steinhauer, "black-hole laser" BEC analogue (2014).** *Nature Physics* **10**, 864–869. Trapped 87Rb BEC with a step potential created an inner+outer sonic horizon pair (charged-BH analogue); observed self-amplifying Hawking radiation between the horizons. Demonstrated: a working sonic-horizon geometry in a BEC, exponential growth of partner modes. Did NOT yet show thermality.
- **Steinhauer, "quantum Hawking entanglement" (2016).** *Nature Physics* **12**, 959–965, arXiv:1510.00621. Spontaneous Hawking radiation from a BEC sonic horizon, with cross-correlations between outside Hawking phonons and inside partners. High-energy pairs entangled, low-energy not. Demonstrated: quantum (vacuum-seeded) Hawking process. Caveat: thermality of the spectrum was contested.
- **Muñoz de Nova, Golubkov, Kolobov, Steinhauer (2019).** *Nature* **569**, 688–691, arXiv:1809.00913. Same platform, longer integration. Confirmed the spectrum is thermal at the temperature set by the analogue surface gravity. Demonstrated: the cleanest existing experimental confirmation of Hawking's prediction in any system.
- **Weinfurtner, Tedford, Penrice, Unruh, Lawrence (2011).** *Phys. Rev. Lett.* **106**, 021302, arXiv:1008.1911. Water flume, streamlined obstacle creating a region where surface-wave group velocity matches the flow — a kinematic horizon. Measured *stimulated* (classical) Hawking conversion; thermal spectrum of mode conversion was confirmed. Did NOT show quantum / spontaneous emission (impossible in a classical system) — what it shows is that the mode-mixing math is right.
- **Torres, Patrick, Coutant, Richartz, Tedford, Weinfurtner, "rotational superradiance" (2017).** *Nature Physics* **13**, 833–836. Draining-vortex water tank; surface waves co-rotating with the vortex were amplified by 14%±8%. Demonstrates the Penrose / superradiance side of rotating-BH physics, not Hawking. Important: this is the closest existing analogue to a *rotating* spacetime, which is what a Kerr BH (and any traversable wormhole with angular momentum) actually is.
- **Drori, Rosenberg, Bermudez, Silberberg, Leonhardt (2019).** *Phys. Rev. Lett.* **122**, 010404, arXiv:1808.09244. Optical fiber: a strong soliton creates a moving refractive-index perturbation; probe light sees this as a horizon when its group velocity matches the soliton's. Observed *stimulated* Hawking-like frequency conversion across positive/negative frequency. Demonstrates the optical-horizon kinematics; spontaneous quantum Hawking in optics remains unobserved.
- **Belgiorno, Cacciatori, Clerici, Gorini, Ortenzi, Rizzi, Rubino, Sala, Faccio (2010).** *Phys. Rev. Lett.* **105**, 203901. Ultrashort laser-pulse filaments in fused silica; reported photon emission they interpreted as analogue Hawking radiation. **Contested.** A 2012 Comment (Schützhold & Unruh, arXiv:1107.2538) argued the emission is more likely conventional four-wave mixing / Cherenkov from the moving refractive-index perturbation, and the "horizon" interpretation is not required. So: an experiment exists, the interpretation does not have consensus.
- **Prat-Camps, Navau, Sanchez (2015), "A Magnetic Wormhole."** *Sci. Rep.* **5**, 12488. Concentric ferromagnetic / superconductor / metamaterial shells transfer a magnetic dipole from one mouth to the other so the field appears at the far mouth as an isolated monopole — magnetically, the connecting tube is invisible. This is a beautiful **transformation-optics** analogue of wormhole *topology* for static magnetic fields. It is not a spacetime wormhole and it does not transmit dynamic signals or matter; phonons/photons in the surrounding lab don't see a horizon.
- **Wormhole-specific dynamic analogues:** none exist in fluids/optics/BECs. The Jafferis et al. 2022 *Nature* "traversable wormhole on a quantum processor" experiment is a SYK-model holography demonstration on Sycamore — it's a quantum-information analogue of an AdS wormhole, not a spacetime experiment. Its physical content is "this 9-qubit circuit reproduces correlations a holographic dual would call wormhole teleportation," nothing more.

**Misremembering check:** Belgiorno's status as "first observation of Hawking" is overstated in some sources — the consensus credit goes to Steinhauer 2016/2019 in BECs. Everything else above checks out.

## 3. What the analogues tell us about real wormholes

**They succeed at:** confirming that the *kinematic* prediction of particle creation by a horizon — a robustly QFT-in-curved-spacetime result — is real in any system that supports the right wave equation. Hawking's calculation is not an artefact of the trans-Planckian extrapolation; it survives in BECs where there is a physical UV cutoff (the healing length). For wormholes specifically, the analogue program tells us that *propagation patterns* near throats, mouths, and horizons (mode mixing, scattering, superradiance) behave in laboratory-realisable ways.

**They fail at:** anything that requires Einstein's equations. No analogue has produced exotic matter, ANEC violation, traversability, topology change, or genuine causal disconnection. The magnetic wormhole demonstrates that *topology of a field* can be hidden, but the field still lives in ordinary 3-space. So: never conclude "we built a wormhole" from any of these. Conclude "we built something whose linear-wave-sector mathematics matches a piece of GR."

## 4. A "Stargate analogue" benchtop that doesn't yet exist (but should)

**Concept: phonon probe of a magnetic-wormhole topology.** Combine the Prat-Camps shell with a BEC or a thin-film 2D phonon medium so a quasiparticle's *effective metric* picks up the wormhole topology of the magnetic field, via spin-orbit coupling or an emergent gauge field.

**Sketch:**
- Outer ferromagnetic spherical shell (mu-metal), inner radius ~3 cm.
- Intermediate superconducting layer (YBCO at 77 K) creating the magnetic cloak.
- Inner ferromagnetic core threaded by a thin tube of high-permeability material (the "throat") connecting two opposite poles — this is the Prat-Camps geometry.
- Probe medium: a 2D dipolar BEC (erbium or dysprosium) confined in a pancake trap straddling one mouth, OR a magnonic film (YIG) in which the spin-wave dispersion depends on local **B**.
- Drive a phonon / magnon wavepacket at one mouth; image its arrival pattern at the far mouth via in-situ absorption imaging or Brillouin scattering.

**What it would demonstrate:** that a wave on a medium with an effective metric inherited from a wormhole-topology field reproduces the predicted *propagation* pattern (including phase shift across the "throat" and absence of an exterior path of equal length). It is *still not* a real wormhole, but it would be the first analogue where the topology, not just the horizon, is what matters.

**Materials (full overlap with Brief 04 expected):** mu-metal sheet; YBCO bulk pucks + LN2 dewar; high-permeability ferrofluid or annealed iron; for the BEC version, a full cold-atom apparatus (>$1M, **out of scope for us**). For the magnonic version, a YIG film on GGG substrate, microwave loop antenna, vector network analyser, electromagnet pair. **Magnonic version cost estimate: $40–80k** at university-lab pricing, the BEC version is $1–3M.

## 5. What to put in the simulator

Two analogue-side modes that bridge real-experiment results to in-simulator validation:

- **Mode A — Magnetic wormhole field topology.** A finite-element magnetostatics solver (open-source `magpylib` for the analytic shell, or `FEMM` / `ngsolve` for full 3D) computing **B**(**r**) for the Prat-Camps geometry. Render field lines in the 3D scene. Validation: the field at the far mouth should appear as an isolated monopole to within ~5% of the published Sci. Rep. 5:12488 figures. Ship the comparison plot in `docs/validation/magnetic_wormhole.png`.
- **Mode B — BEC sonic horizon.** A 1D Gross–Pitaevskii solver (split-step Fourier) with a step potential, evolving a condensate into a black-hole-laser configuration. Plot the density-density correlation function `g(2)(x, x')` and look for the characteristic anti-diagonal Hawking correlation feature reported in Steinhauer 2016 fig. 2. Validation: the correlation amplitude and angle in the (x, x') plane match the paper's figures qualitatively. This gives a user a "press play, watch Hawking radiation appear" path.

Both modes are CPU-cheap (Mode A is one-shot; Mode B is a 256-grid 1D PDE). Neither requires a GPU. Both produce figures that can be A/B'd against published data, which is what makes the simulator scientifically credible rather than decorative.

## 6. Three experiments realistically runnable in 2026 on <$5k, in an apartment, with a 6-year-old around

Safety constraint is real — no high-power lasers, no cryogens unattended, no high voltage exposed.

- **(i) Water-flume kinematic horizon, kid-safe.** A 1.2 m clear acrylic channel, small submersible pump (~12V), an obstacle to make a transcritical flow region, surface-wave generator (an offset cam on a hobby motor), and a phone camera with synthetic schlieren analysis (open-source, see Moisy et al. 2009). Cost: ~$300–600. **Would prove:** you can create a kinematic horizon and observe wave blocking. **Would NOT prove:** Hawking thermality (Weinfurtner-quality data needs careful flow control we won't get on a kitchen counter), and certainly not anything quantum. Educationally outstanding and the daughter can help drop dye.
- **(ii) Soliton-pulse refractive-index horizon in a fiber, low-power.** A telecom-band CW laser + commercial mode-locked seed (Thorlabs / used eBay), a spool of highly-nonlinear fiber, an OSA borrowed from a local university lab. Cost: pushing the budget — $3–5k if we get used kit, otherwise out of reach. **Would prove:** soliton-induced frequency conversion across a moving refractive-index step (Drori-style stimulated emission, classical regime). **Would NOT prove:** spontaneous quantum Hawking in optics (needs single-photon detectors and shielding we don't have). **Daughter risk:** fiber lasers must be enclosed, no exposed beams, eyewear during alignment — tractable but the most demanding of the three.
- **(iii) Magnetic-wormhole tabletop replica.** Concentric mu-metal shell + room-temperature ferromagnetic inner sphere + iron-core "throat tube." Skip the superconductor (which is what makes it a *true* magnetic cloak); the field topology is still demonstrable just less cleanly. Hall-probe map the field on a CNC gantry (or 3D-printed 2-axis stage with a $20 sensor). Cost: ~$400–1,200. **Would prove:** the qualitative wormhole-topology field pattern (monopole-like emergence at far mouth above background). **Would NOT prove:** true magnetic invisibility of the connecting tube (that needs the superconductor). Zero kinetic / thermal / electrical hazard — kid-safe, demos well.

Honest pick: (i) and (iii) first, this year. (ii) is a stretch goal contingent on a used-equipment windfall.

## 7. Citations

- Unruh, *Phys. Rev. Lett.* **46**, 1351 (1981). DOI:10.1103/PhysRevLett.46.1351.
- Barceló, Liberati, Visser, *Living Rev. Relativity* **14**, 3 (2011). arXiv:gr-qc/0505065.
- Steinhauer, *Nature Physics* **10**, 864 (2014). DOI:10.1038/nphys3104.
- Steinhauer, *Nature Physics* **12**, 959 (2016). arXiv:1510.00621. DOI:10.1038/nphys3863.
- Muñoz de Nova, Golubkov, Kolobov, Steinhauer, *Nature* **569**, 688 (2019). arXiv:1809.00913. DOI:10.1038/s41586-019-1241-0.
- Kolobov, Golubkov, Muñoz de Nova, Steinhauer, *Nature Physics* **17**, 362 (2021), "stationary spontaneous Hawking radiation." arXiv:1910.09363. [verified]
- Weinfurtner, Tedford, Penrice, Unruh, Lawrence, *Phys. Rev. Lett.* **106**, 021302 (2011). arXiv:1008.1911.
- Torres, Patrick, Coutant, Richartz, Tedford, Weinfurtner, *Nature Physics* **13**, 833 (2017). DOI:10.1038/nphys4151.
- Drori, Rosenberg, Bermudez, Silberberg, Leonhardt, *Phys. Rev. Lett.* **122**, 010404 (2019). arXiv:1808.09244.
- Belgiorno et al., *Phys. Rev. Lett.* **105**, 203901 (2010). DOI:10.1103/PhysRevLett.105.203901.
- Schützhold & Unruh Comment, arXiv:1107.2538 (2011) [interpretation challenge to Belgiorno].
- Prat-Camps, Navau, Sanchez, *Sci. Rep.* **5**, 12488 (2015). DOI:10.1038/srep12488.
- Jafferis et al., *Nature* **612**, 51 (2022), "Traversable wormhole dynamics on a quantum processor." DOI:10.1038/s41586-022-05424-3. [Quantum-information analogue, not spacetime.]
- Moisy, Rabaud, Salsac (2009), free-surface synthetic schlieren — *Exp. Fluids* **46**, 1021. [Cited as the open-source method behind experiment (i).] [unverified specific page numbers, method itself is well-established]
