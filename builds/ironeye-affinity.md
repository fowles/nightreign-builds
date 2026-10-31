# Ironeye: Weapon-Switch Affinity

> Generated 2026-10-31 with `python3 -I scripts/ironeye.py --build affinity`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** build around **R00860 Night of the Lord** (Blue, standard, Heolstor reward). It's the only relic you own with `Switching Weapons Adds an Affinity Attack`. Swap between two bows often. Each swap adds random-element damage and +10% attack for 10 s.

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- R00860 Night of the Lord, so a blue or white normal slot

The switch supplies the affinity, so no elemental starting armament is required. One is still scored if a loadout carries it, but none of the top loadouts does.

## What Night of the Lord does (wiki.gg)

| Effect | Size | Note |
|---|---|---|
| Switching Weapons Adds an Affinity Attack | +12 random magic/fire/lightning/holy damage for 10 s | read from a page summary, not verbatim **(unverified)** |
| Boosts Attack Power of Added Affinity Attacks | +10% to infusions, weapon buffs and thrown/reusable consumables | verbatim |
| Switching Weapons Boosts Attack Power | +10% damage for 10 s after a swap | verbatim |

## Key finding: affinity buffs aren't worth slots

If the switch affinity is really +12 flat, it adds ~4% to an arrow (assuming ~300 AR, a guess). At 60% swap uptime, that's ~2.4% of your damage. `Improved Affinity Attack Power +2` (+10%) on that slice is worth ~0.1 points. Even if the switch affinity were 5× bigger (`--switch-add 20`), each copy would be worth ~0.5 points. So the search never takes one (you own 40), and the rankings don't change:

| `--switch-add` | Forgotten Goblet | Ironeye's Goblet | Decrepit Goblet |
|---|---|---|---|
| 4% (default) | 56.7 | 52.8 | 52.0 |
| 10% | 58.7 | 54.9 | 54.0 |
| 20% | 62.0 | 58.4 | 57.4 |

Night of the Lord itself earns ~2.4 points from the +10% switch boost, plus a little from the added affinity. The rest of the build is generic Ironeye damage and sustain. **This is the weakest of the three Ironeye builds in the model** (poison 65.8, ISA 50.8–55.9).

If the in-game number is much bigger than +12, or turns out to be a percentage, re-run with `--switch-add`. Affinity relics only start to pay if the added damage is a large share of each hit.

## Best: Forgotten Ironeye's Goblet (Normal Y B R / Deep Y G W)

**Score 56.7:** damage 18.0, sustain 39.7, utility 10.0, penalties −11.0. Unlock: 4 Sovereign Sigils.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal B | **R00860** Night of the Lord | **Switching Weapons Adds an Affinity Attack**; **Boosts Attack Power of Added Affinity Attacks**; **Switching Weapons Boosts Attack Power** |
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Deep Y | **R01893** Deep Grand Luminous Scene | [Ironeye] Improved Vigor and Strength, Reduced Dexterity; Critical hits fill more of the Art gauge +1 *(curse: Reduced Dexterity and Faith)*; Improved Physical Damage Negation +2 *(curse: Continuous HP Loss)* |
| Deep G | **R01257** Deep Grand Tranquil Scene | Physical Attack Up +4 *(curse: Lower Attack When Below Max HP)*; Increased Maximum HP *(curse: Reduced Rune Acquisition)*; Improved Affinity Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |
| Deep W | **R00162** Deep Polished Burning Scene (Red) | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |

- **Curses: 6.**
  - Costly: Reduced Dexterity and Faith (−3, Dex A), Continuous HP Loss (−3), Lower Attack When Below Max HP (−3).
  - Mild: Reduced Rune Acquisition (−1).
  - Fine: Repeated Evasions Lower Damage Negation, Reduced Strength and Intelligence.
- **Dormant Powers:** none. **`unverified_effect` flags:** none. **Rally:** yes (R00162 +2).
- R01893 (the Vigor/Str respec) brings 2 of the 6 curses. For a cleaner loadout, swap it for a curse-free yellow deep relic. Not separately scored.

## Alternative: Ironeye's Goblet (Normal R B Y / Deep R B Y)

**Score 52.8:** damage 14.8, sustain 34.5, utility 7.0, penalties −3.5. The normal side is the same three relics.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Normal B | **R00860** Night of the Lord | **Switching Weapons Adds an Affinity Attack**; **Boosts Attack Power of Added Affinity Attacks**; **Switching Weapons Boosts Attack Power** |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |
| Deep B | **R00969** Deep Grand Drizzly Scene | [Duchess] Use Character Skill for Brief Invulnerability *(wasted on Ironeye)*; Increased Maximum HP *(curse: Rot Buildup When Below Max HP)*; Improved Physical Damage Negation +2 *(curse: Taking Damage Causes Frost Buildup)* |
| Deep Y | **R01151** Deep Grand Luminous Scene | [Undertaker] Executing Art readies Character Skill *(wasted on Ironeye)*; FP Restoration upon Hammer Attacks *(out of focus)*; Flask Also Heals Allies |

- **Curses: 3.** Taking Damage Causes Frost Buildup (−2; mild at range, not a guard build), Rot Buildup When Below Max HP (−1), Repeated Evasions Lower Damage Negation (fine).
- **Dormant Powers:** none. **`unverified_effect` flags:** none. **Rally:** yes (R00162 +2).
- **Decrepit Ironeye's Goblet (52.0)** is the damage-heavy option: damage 32.2 from Physical Attack Up +3/+4/+4 (R00669, R00531, R01257), with 6 curses. Its deep colors are **unverified** between sources.

## Gameplay loop

1. Carry two bows (the starting bow plus a found one; a Dormant Power for Bows is neutral) and swap every ~10 s, so the +10% attack and the added affinity stay up (60% uptime assumed).
2. The added random element hits weak points across the four elements, so you never need an infusion that matches the boss.
3. Mark, pop the weak point, and charge Single Shot as usual. Night Invader and the evergaol stacks carry the all-damage scaling.

## Trade-offs and unknowns

- **The switch-affinity size is unverified** and drives the "affinity buffs are worthless" finding. Check it in game: watch the damage numbers on a dummy right after a swap.
- **Swap uptime of 60% is a guess.** At lower uptime both switch effects lose value in proportion.
- Does swapping interrupt your bow chain or cost DPS? Not modeled.
- Whether `Boosts Attack Power of Added Affinity Attacks` applies to the switch affinity is assumed, not confirmed. wiki.gg lists infusions, weapon buffs and consumables.

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage slices | arrows 0.70 (20% first in chain, 60% from the starting bow, 40% of found-bow damage elemental), Single Shot 0.12, Marking bursts 0.10, crits 0.05, melee 0.03 | guesses |
| Switch uptime | 0.6 | guess |
| Switch affinity | +4% damage while up (+12 flat on ~300 AR), split evenly across the four elements | `--switch-add`; guess |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Rally | 1.0 / 1.25 / 1.35 bars per fight | ranged; guess |
| Ultimate Art Charging Impaired | −10 | Single Shot is the revive |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (switch affinity +12 for 10 s, added-affinity +10%, switch boost +10% for 10 s, affinity sizes)
- https://gamewith.net/eldenring-nightreign/57370 and https://www.pcgamesn.com/elden-ring-nightreign/relics-best (Night of the Lord's effects, Heolstor reward)
