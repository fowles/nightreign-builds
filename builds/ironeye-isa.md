# Ironeye: Initial Standard Attack Stack

> Generated 2026-10-31 with `python3 -I scripts/ironeye.py --build isa --min-isa 4`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** stack `Improved Initial Standard Attack` (ISA: "damage of first light attack in a chain +15%", wiki.gg) and play a tap-fire bow, so most of your arrows open a fresh chain.

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- at least N ISA copies (`--min-isa N`)

**Big unknowns that decide this build:**
1. **Do ISA copies stack?** The model assumes they multiply like other attack buffs (4 copies = ×1.75). The only support is a Steam thread claiming "it stacks" **(unverified)**. If only one copy counts, this build is strictly worse than the poison one.
2. **Does a bow's first shot count as the "first light attack in a chain"?** It should, since Ironeye's bow light attacks form a four-shot chain (wiki.gg). How long you have to pause between shots to reset the chain is **unverified**. Test it in the training area.

## How many copies?

| ISA floor | Best vessel | Total | Damage | Sustain | Curses |
|---|---|---|---|---|---|
| none | Ironeye's Chalice | 60.1 | 21.9 | 40.2 | 5 *(0 ISA: the model doesn't pick ISA by itself)* |
| 2 | Forgotten Ironeye's Goblet | 58.5 | 24.6 | 30.4 | 2 |
| 3 | Ironeye's Goblet | 55.9 | 22.2 | 26.7 | 0 |
| **4** | **Ironeye's Goblet** | **50.8** | **29.9** | **13.9** | **0** |
| 5 | Ironeye's Goblet | 42.2 | 23.6 | 16.6 | 0 |
| 6 | — | — | — | — | impossible: the mandatory +1 skill relic has no ISA |

Each ISA copy is worth ~2.7 points alone (15% × the 45% of your damage that's first-in-chain). Copies multiply, but each one pushes out a relic that's worth more on its own. So the score falls as the stack grows. **4 copies is the sweet spot:** it holds the most damage of any row, and the 5th copy costs the Night Invader relic. Every row from 3 copies up is curse-free.

## Best: Ironeye's Goblet (Normal R B Y / Deep R B Y), 4 ISA

**Score 50.8:** damage 29.9, sustain 13.9, utility 7.0, penalties 0.0. Unlock: Small Jar Bazaar, 1200 Murk.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Normal B | **R00499** Polished Drizzly Scene | **Improved Initial Standard Attack**; Dexterity +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01233** Deep Grand Burning Scene | [Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies *(out of focus)*; HP Recovery From Successful Guarding *(out of focus)*; **Improved Initial Standard Attack** |
| Deep B | **R00237** Deep Polished Drizzly Scene | **Improved Initial Standard Attack**; Holy Damage Negation Up |
| Deep Y | **R01324** Deep Grand Luminous Scene | [Undertaker] Improved Mind and Faith, Reduced Strength *(wasted on Ironeye)*; Partial HP Restoration upon Post-Damage Attacks; **Improved Initial Standard Attack** |

- **ISA copies: 4** → first-in-chain arrows ×1.75 if they stack.
- **Curses: 0.** **Dormant Powers:** none. **`unverified_effect` flags:** none. **Rally:** yes (R01324, base tier).
- **Sustain is thin (13.9).** Base rally and holy negation are all you get. Swap R00499 for **R00823** Dark Night of the Fathom (Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low) to drop to 3 ISA. The score rises to 55.9 (sustain 26.7, damage 22.2), still with 0 curses. I'd take this swap until ISA stacking is confirmed.

## Alternative: Forgotten Ironeye's Goblet (Normal Y B R / Deep Y G W), 4 ISA

**Score 50.8:** the same score and split. Unlock: 4 Sovereign Sigils. The normal side is the same three relics. On the deep side, **R00568** Deep Polished Tranquil Scene (Speckled Hardtear in possession at start of expedition; **Improved Initial Standard Attack**) takes the green slot in place of R01233, with R01324 in yellow and R00237 in white.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal B | **R00499** Polished Drizzly Scene | **Improved Initial Standard Attack**; Dexterity +3 |
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Deep Y | **R01324** Deep Grand Luminous Scene | [Undertaker] Improved Mind and Faith, Reduced Strength *(wasted on Ironeye)*; Partial HP Restoration upon Post-Damage Attacks; **Improved Initial Standard Attack** |
| Deep G | **R00568** Deep Polished Tranquil Scene | Speckled Hardtear in possession at start of expedition; **Improved Initial Standard Attack** |
| Deep W | **R00237** Deep Polished Drizzly Scene (Blue) | **Improved Initial Standard Attack**; Holy Damage Negation Up |

- **Curses: 0.** **Dormant Powers:** none. **`unverified_effect` flags:** none. **Rally:** yes (R01324).
- With the 3-ISA floor, this vessel scores 56.5 (3 curses) by putting **R01257** (Physical Attack Up +4; Increased Maximum HP; Improved Affinity Damage Negation +1, curses Lower Attack When Below Max HP / Reduced Rune Acquisition / Reduced Strength and Intelligence) in the green slot.

## Gameplay loop

1. Fire single light shots with a short pause between them, so each arrow opens a new chain and gets the ISA multiplier.
2. Mark through the target for the team's +10% weak point, then pop it with tap shots.
3. Night Invader and the evergaol stacks carry the all-damage scaling. Single Shot is your burst and revive.
4. You trade sustained DPS (the faster four-shot chain) for burst per arrow. The model assumes 60% of your arrows are chain openers.

## Trade-offs and unknowns

- See the two big unknowns at the top. Both decide whether this build works at all.
- Bow DPS lost to pausing between shots isn't modeled: the 60% first-in-chain share is a guess about playstyle, not a measured DPS.
- R01233 carries the heavy-poison Marking, which does nothing here without a poison source.

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage slices | arrows 0.75 (60% first in chain, 50% from the starting bow), Single Shot 0.12, Marking bursts 0.08, crits 0.05 | guesses |
| ISA | +15% per copy on first-in-chain arrows; copies multiply | size wiki.gg; stacking unverified |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Rally | 1.0 / 1.25 / 1.35 bars per fight | ranged; guess |
| Ultimate Art Charging Impaired | −10 | Single Shot is the revive |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (ISA +15% on the first light attack in a chain)
- https://eldenring.wiki.gg/wiki/Ironeye (bow light attacks are a four-shot chain)
- https://steamcommunity.com/app/2622380/discussions/0/597405499344849482/ (player claim that ISA stacks, first light attack only; unverified)
