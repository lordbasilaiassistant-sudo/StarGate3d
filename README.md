# StarGate3d

Build a Stargate. For real.

## The Vision

A 3D simulation world that obeys real physics, where we test every credible path
to a traversable wormhole — then find the cheapest one we can actually build.

Not a movie prop. Not a science-fiction tribute. A working iris-and-puddle gate
that a person can step through and come out somewhere else. If our current
theories say it's impossible, then our current theories are incomplete and we
treat that as a hypothesis to break, not a verdict to accept.

This repo is the workshop.

## Why This Isn't Crazy

The pieces already exist in real labs. Nobody has assembled them yet.

- **Morris–Thorne wormholes** are valid solutions to General Relativity. They
  need exotic matter (negative energy density) to stay open.
- **Casimir effect** produces negative energy density. Measured. Real. Tiny.
- **Maldacena–Milekhin–Popov (2020)** showed Casimir energy from massless
  fermions in higher dimensions can in principle stabilize a traversable
  wormhole.
- **Jafferis et al. (Nature, 2022)** ran a "traversable wormhole" protocol on
  Google's Sycamore quantum processor — a holographic dual, not a literal
  hole, but the math is the same math.
- **Prat-Camps, Navau, Sánchez (Sci. Reports, 2015)** built a real magnetic
  wormhole on a benchtop with ferromagnetic shells and mu-metal. A field line
  vanishes on one side and reappears on the other with no detectable path
  between. ~$2k in materials.
- **Acoustic and BEC analogue wormholes** have been demonstrated. Phonons cross
  effective horizons in laboratory fluids.
- **ER = EPR** says quantum entanglement and wormholes are the same object
  viewed two ways. Entanglement is routine.

We have negative energy. We have wormhole math. We have analogue gates that
work in EM, sound, and BEC. The gap between these and a person-sized portal is
huge — but it's an engineering gap on top of physics that already cleared.

## What This Repo Will Become

1. **A 3D simulator** (browser-first, Three.js + WebGPU) where you can stand
   inside an actual Morris–Thorne metric and look around. Light bent by the
   real wormhole equations, not faked with shaders.
2. **A theory ledger** — every credible portal mechanism, its prediction, its
   simulator scene, its required materials, its estimated cost, its current
   experimental status, its kill criteria.
3. **A buildable analogue track** — start with the magnetic wormhole, recreate
   it, then push: bigger, multi-field, see how far the analogue can be taken
   before it stops being analogue and starts being the thing.
4. **A materials and cost model** — every step priced in materials a renter in
   Vestal NY can actually buy. Mu-metal sheet, neodymium, copper, vacuum pumps,
   not LIGO mirrors. If a path needs a billion dollars of antimatter, we log it
   and look for the cheap version.

## Honest About the Odds

Most of these paths fail. Some fail catastrophically (negative energy at human
scale may be forbidden by the averaged null energy condition). Some succeed
only as analogues that never become true gates.

That's fine. The point is to test them all in simulation, ship the
buildable ones to the bench, and learn exactly which wall we hit and why.
"It can't be done" with a measurement is worth more than ten thousand "I think
it can" without one.

If even the simulator never produces a traversable scene, we will have built
the most accurate wormhole physics sandbox on the public internet. That's not
nothing.

## For Humanity

If a real gate is possible, it belongs to everyone. All theory, simulator code,
materials lists, and lab notes here are open source from the first commit.

## Status

Day 0. Repo initialized. Plan in `PLAN.md`.

— Anthony Snider (`drlordbasil`)
