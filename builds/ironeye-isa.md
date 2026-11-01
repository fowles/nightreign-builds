# Ironeye: Initial Standard Attack Stack

> Generated 2026-11-01 with `python3 -I scripts/ironeye.py --build isa --min-isa 4`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** stack `Improved Initial Standard Attack` (ISA: "damage of first light attack in a chain +15%", wiki.gg) and play a tap-fire bow, so most of your arrows open a fresh chain. **ISA copies stack** (confirmed by you) and multiply like other attack buffs: 4 copies = ×1.75 on chain-opening arrows.

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- at least N ISA copies (`--min-isa N`)

Rally does nothing on a ranged bow build, so it weighs 0. **Arrows count as thrusting counterattacks** (confirmed by you), so `HP Restoration upon Thrusting Counterattack` now scores as a heal (2.5% max HP per counter hit, ~15 a fight, guess).

**Open question:** how long you have to pause between shots to reset the chain. Ironeye's bow light attacks are a four-shot chain (wiki.gg). The model assumes 60% of your arrows open a chain. Measure it in the training area.

## How many copies?

Best vessel at each ISA floor (Ironeye's Goblet, except at 3 where the Forgotten Goblet edges it 44.5 to 44.1 with 7.5 penalty points; the two tie at 4 and 5):

| ISA floor | Total | Damage | Sustain | Curses |
|---|---|---|---|---|
| none (0 ISA picked) | 47.7 | 28.9 | 20.3 | 5 |
| 2 | 45.7 | 23.8 | 20.5 | 3 |
| 3 | 44.1 | 22.2 | 17.9 | 1 |
| **4** | **39.9** | **29.9** | **6.0** | **1** |
| 5 | 30.9 | 23.6 | 8.3 | 1 |
| 6 | — | — | — | impossible: the mandatory +1 skill relic has no ISA |

**Why the model doesn't stack ISA by itself:** one ISA copy is +15% on the ~45% of your damage that opens a chain, about +6.75% overall. `Physical Attack Up +3/+4` (+10.5/12%) covers every physical hit. None of your deep ISA relics also carries Physical Attack Up, so every ISA copy displaces a bigger physical buff. ISA catches up only if nearly every arrow opens a chain. At a 90% first-shot share (checked in the script before this update), the 4-ISA Goblet scored 45.8 against 47.0 for the best unconstrained loadout.

**4 copies holds the most damage of any row** (29.9) with one near-free curse; its only sustain is the thrusting-counter heal. Three copies plus R00823 is the balanced version (below).

## Best: Ironeye's Goblet (Normal R B Y / Deep R B Y), 4 ISA

**Score 39.9:** damage 29.9, sustain 6.0, utility 7.0, penalties −3.0. Unlock: Small Jar Bazaar, 1200 Murk.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Normal B | **R00499** Polished Drizzly Scene | **Improved Initial Standard Attack**; Dexterity +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01233** Deep Grand Burning Scene | [Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies *(out of focus)*; HP Recovery From Successful Guarding *(out of focus)*; **Improved Initial Standard Attack** |
| Deep B | **R01171** Deep Grand Drizzly Scene | HP Restoration upon Thrusting Counterattack +1 *(curse: Reduced Intelligence and Dexterity)*; **Improved Initial Standard Attack**; Improved Frost Resistance *(hand-weighted 0)* |
| Deep Y | **R00577** Deep Polished Luminous Scene | [Executor] Slowly Restore HP upon Ability Activation *(wasted on Ironeye)*; **Improved Initial Standard Attack** |

- **ISA copies: 4** → chain-opening arrows ×1.75.
- **Curses: 1.** Reduced Intelligence and Dexterity (−3): Dex is Ironeye's A stat, so this one costs real damage. R00237 (ISA; Holy Damage Negation Up) is the curse-free swap at 37.3: it gives up the counter heal.
- **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Sustain:** the thrusting-counter heal only.

## Alternative: Ironeye's Goblet with 3 ISA + R00823

**Score 44.1:** damage 22.2, sustain 17.9, utility 7.0, penalties −3.0. Same vessel and deep side. Swap R00499 for:

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |

- **ISA copies: 3** (×1.52). **Curses: 1** (Reduced Intelligence and Dexterity, on R01171). With R00237 in place of R01171 it's curse-free at 41.1. **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Forgotten Ironeye's Goblet** (Normal Y B R / Deep Y G W) ties the 4-copy row and scores 44.5 at 3 copies, with more curses.

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
| Thrusting-counter heal | 2.5% max HP per counter hit (base, wiki.gg; +1 guessed 3%), 15 counter hits per fight → 0.375 / 0.45 bars | hit count guessed; arrows counting confirmed by you |
| `[Ironeye] Boosts thrusting counterattacks after executing Art` | +20% × 0.4 window uptime × 0.3 counter share on bow damage | guesses; never picked |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Ultimate Art Charging Impaired | −10 | Single Shot is the revive |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (ISA +15% on the first light attack in a chain)
- https://eldenring.wiki.gg/wiki/Ironeye (bow light attacks are a four-shot chain)
- https://eldenring.wiki.gg/wiki/Nightreign:Night_of_the_Champion (thrusting-counter heal 2.5% max HP)
