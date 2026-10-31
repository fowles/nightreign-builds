# Ironeye: Initial Standard Attack Stack

> Generated 2026-10-31 with `python3 -I scripts/ironeye.py --build isa --min-isa 4`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** stack `Improved Initial Standard Attack` (ISA: "damage of first light attack in a chain +15%", wiki.gg) and play a tap-fire bow, so most of your arrows open a fresh chain. **ISA copies stack** (confirmed by you) and multiply like other attack buffs: 4 copies = ×1.75 on chain-opening arrows.

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- at least N ISA copies (`--min-isa N`)

Rally does nothing on a ranged bow build, so it weighs 0.

**Open question:** how long you have to pause between shots to reset the chain. Ironeye's bow light attacks are a four-shot chain (wiki.gg). The model assumes 60% of your arrows open a chain. Measure it in the training area.

## How many copies?

Best vessel at each ISA floor (Ironeye's Goblet throughout; the Forgotten Goblet ties from 3 copies up):

| ISA floor | Total | Damage | Sustain | Curses |
|---|---|---|---|---|
| none (0 ISA picked) | 44.0 | 28.9 | 13.5 | 3 |
| 2 | 42.4 | 23.8 | 14.1 | 2 |
| 3 | 41.1 | 22.2 | 11.9 | 0 |
| **4** | **37.3** | **29.9** | **0.4** | **0** |
| 5 | 28.0 | 23.6 | 2.4 | 0 |
| 6 | — | — | — | impossible: the mandatory +1 skill relic has no ISA |

**Why the model doesn't stack ISA by itself:** one ISA copy is +15% on the ~45% of your damage that opens a chain, about +6.75% overall. `Physical Attack Up +3/+4` (+10.5/12%) covers every physical hit. None of your deep ISA relics also carries Physical Attack Up, so every ISA copy displaces a bigger physical buff. ISA catches up only if nearly every arrow opens a chain. At a 90% first-shot share (checked in the script), the 4-ISA Goblet scores 45.8 against 47.0 for the best unconstrained loadout.

**4 copies holds the most damage of any row** (29.9) and is curse-free, but it gives up all sustain. Three copies plus R00823 is the balanced version (below).

## Best: Ironeye's Goblet (Normal R B Y / Deep R B Y), 4 ISA

**Score 37.3:** damage 29.9, sustain 0.4, utility 7.0, penalties 0.0. Unlock: Small Jar Bazaar, 1200 Murk.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Normal B | **R00499** Polished Drizzly Scene | **Improved Initial Standard Attack**; Dexterity +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01233** Deep Grand Burning Scene | [Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies *(out of focus)*; HP Recovery From Successful Guarding *(out of focus)*; **Improved Initial Standard Attack** |
| Deep B | **R00237** Deep Polished Drizzly Scene | **Improved Initial Standard Attack**; Holy Damage Negation Up |
| Deep Y | **R00577** Deep Polished Luminous Scene | [Executor] Slowly Restore HP upon Ability Activation *(wasted on Ironeye)*; **Improved Initial Standard Attack** |

- **ISA copies: 4** → chain-opening arrows ×1.75.
- **Curses: 0.** **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Sustain is essentially nil:** holy negation only.

## Alternative: Ironeye's Goblet with 3 ISA + R00823

**Score 41.1:** damage 22.2, sustain 11.9, utility 7.0, penalties 0.0. Same vessel and deep side. Swap R00499 for:

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |

- **ISA copies: 3** (×1.52). **Curses: 0.** **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Forgotten Ironeye's Goblet** ties both rows (Normal Y B R / Deep Y G W). It uses the same normal relics, plus **R00568** Deep Polished Tranquil Scene (Speckled Hardtear in possession at start of expedition; **Improved Initial Standard Attack**) in green in place of R01233.

## Gameplay loop

1. Fire single light shots with a short pause between them, so each arrow opens a new chain and gets the ×1.75.
2. Mark through the target for the team's +10% weak point, then pop it with tap shots.
3. Night Invader and the evergaol stacks scale everything. Single Shot is your burst and revive.
4. You trade sustained DPS (the faster four-shot chain) for burst per arrow.

## Trade-offs and unknowns

- The 60% first-in-chain share is a playstyle guess. Bow DPS lost to pausing isn't modeled.
- R01233 carries the heavy-poison Marking, which does nothing here without a poison source.

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage slices | arrows 0.75 (60% first in chain, 50% from the starting bow), Single Shot 0.12, Marking bursts 0.08, crits 0.05 | guesses |
| ISA | +15% per copy on first-in-chain arrows; copies multiply | wiki.gg size; stacking confirmed by you |
| Rally | 0 | does nothing for ranged |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Ultimate Art Charging Impaired | −10 | Single Shot is the revive |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (ISA +15% on the first light attack in a chain)
- https://eldenring.wiki.gg/wiki/Ironeye (bow light attacks are a four-shot chain)
