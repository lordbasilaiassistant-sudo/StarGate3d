```
+==============================================================================+
|  THEORY LEDGER                                                               |
|  DOC ID: SG3D-THEORY-INDEX     REV: 0.1     DATE: 2026-05-01                 |
+==============================================================================+
```

This directory is the program's evidence ledger. One markdown file per
credible portal mechanism. Each entry follows the same template so we can
rank them on the same axes and kill them on the same evidence rules.

## Template (every entry has these sections, in this order)

```markdown
# <Mechanism Name>

**Status:**  ACTIVE | PARKED | KILLED | NEVER-EXISTED
**Owner:**   R<n> (research department)
**Sim scene:** S<n> (per docs/physics_spec.md), or `none-yet`
**Last reviewed:** YYYY-MM-DD

## §1  Mechanism
Plain-language description. One paragraph.

## §2  Required ingredients
What physics has to be true; what materials/energy/conditions the device
needs. Numbers where possible (mass, charge, energy density, temperature,
field strength).

## §3  Predictions the simulator must make
What the running scene shows the user. Distinct, falsifiable visual outputs.

## §4  Lab analogue (if any)
Real benchtop experiment that demonstrates a piece of the physics. Cite paper
+ what was actually measured + what wasn't.

## §5  Materials & rough cost
BOM, vendors, total at minimum / reasonable / aggressive scope.

## §6  Current experimental status
Live citations (arXiv ID / DOI). What's confirmed, what's contested, what's
purely theoretical.

## §7  Kill criterion
The single piece of evidence that ends this line. Be specific: a measured
bound, a no-show experiment, a closed loophole. If you can't write one, the
entry is not yet a theory — it's a wish.

## §8  Open questions
What we'd most want to know next.
```

## Ranking

After all entries are populated, theories are ranked by

```
score = P_traversable × ln(1 / dollar_cost_to_decisive_test)
```

where `P_traversable` is our honest current estimate of the probability that
the mechanism could produce a person-traversable portal at any scale, and
`dollar_cost_to_decisive_test` is what it would take to either kill the entry
or push it to the next stage of evidence.

Rank table maintained at `theories/_ranking.md` (auto-regenerated from the
individual entries).

## Index

| Slug                          | Status        | Source brief    |
|-------------------------------|---------------|-----------------|
| morris-thorne                 | ACTIVE        | R1              |
| ellis-drainhole               | TBD           | R1              |
| teo-rotating                  | TBD           | R1              |
| mmp-stabilized                | TBD           | R2 + R10        |
| damour-solodukhin             | TBD           | R1              |
| magnetic-metamaterial         | TBD (Phase-1) | R3              |
| optical-metamaterial          | TBD           | R3              |
| acoustic-analogue             | TBD           | R5              |
| bec-analogue                  | TBD           | R5              |
| er-epr-gjw                    | TBD           | R7              |
| plasma-toroid                 | TBD (visual)  | R6              |
| alcubierre-warp               | TBD           | R1              |
| vacuum-engineering            | TBD           | R2              |

`TBD` entries are stubs — each will be expanded by the owning department.
The `morris-thorne` entry is the template you should pattern-match against.
