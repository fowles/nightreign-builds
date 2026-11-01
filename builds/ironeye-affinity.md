# Ironeye: Weapon-Switch Affinity

> Generated 2026-11-01 with `python3 -I scripts/ironeye.py --build affinity`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** build around **R00860 Night of the Lord** (Blue, standard, Heolstor reward). It's the only relic you own with `Switching Weapons Adds an Affinity Attack`. Swap between two bows often. Each swap adds random-element damage and +10% attack for 10 s.

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- R00860 Night of the Lord, so a blue or white normal slot

The switch supplies the affinity, so no elemental starting armament is required. One is still scored if a loadout carries it, but none of the top loadouts does. Rally does nothing on a ranged bow build, so it weighs 0. Arrows count as thrusting counterattacks (confirmed by you), so the thrusting-counter heal and Ironeye's post-Art counter boost are scored.

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
| 4% (default) | 41.6 | 39.7 | 36.0 |
| 10% | 43.8 | 41.8 | 38.0 |
| 20% | 47.3 | 45.4 | 41.3 |

Night of the Lord itself earns ~2.4 points from the +10% switch boost, plus a little from the added affinity. The rest of the build is Physical Attack Up plus sustain. **This is the weakest of the three Ironeye builds in the model** (poison 49.6–51.2, ISA 39.9–44.1).

If the in-game number is much bigger than +12, or turns out to be a percentage, re-run with `--switch-add`.

## Best: Forgotten Ironeye's Goblet (Normal Y B R / Deep Y G W)

**Score 41.6:** damage 26.1, sustain 18.5, utility 7.0, penalties −10.0. Unlock: 4 Sovereign Sigils.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal B | **R00860** Night of the Lord | **Switching Weapons Adds an Affinity Attack**; **Boosts Attack Power of Added Affinity Attacks**; **Switching Weapons Boosts Attack Power** |
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Deep Y | **R00185** Deep Polished Luminous Scene | Max HP increased for each great enemy defeated at a Great Church.; Physical Attack Up +3 *(curse: Reduced Damage Negation for Flask Usages)* |
| Deep G | **R01257** Deep Grand Tranquil Scene | Physical Attack Up +4 *(curse: Lower Attack When Below Max HP)*; Increased Maximum HP *(curse: Reduced Rune Acquisition)*; Improved Affinity Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |
| Deep W | **R01191** Deep Grand Luminous Scene (Yellow) | HP Restoration upon Thrusting Counterattack +1 *(curse: Reduced Faith and Strength)*; Attack power up when facing scarlet rot-afflicted enemy *(out of focus)*; Improved Physical Damage Negation +2 *(curse: All Resistances Down)* |

- **Damage stack:** Physical Attack Up +3 / +4 multiply (+24%), plus Night Invader, the evergaol stacks and the +10% switch boost.
- **Sustain:** the thrusting-counter heal (arrows count, confirmed by you), max HP, physical and affinity negation.
- **Curses: 6.**
  - Lower Attack When Below Max HP (−3), Reduced Damage Negation for Flask Usages (−2.5), All Resistances Down (−2.5), Reduced Rune Acquisition (−1).
  - Near-free: Reduced Strength and Intelligence, Reduced Faith and Strength (Str C, Fai D).
- **Dormant Powers:** none. **`unverified_effect` flags:** none.

## Alternative: Ironeye's Goblet (Normal R B Y / Deep R B Y)

**Score 39.7:** damage 17.7, sustain 20.0, utility 7.0, penalties −5.0. The normal side is the same three relics.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Normal B | **R00860** Night of the Lord | **Switching Weapons Adds an Affinity Attack**; **Boosts Attack Power of Added Affinity Attacks**; **Switching Weapons Boosts Attack Power** |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R00851** Deep Grand Burning Scene | [Revenant] Increased Max FP upon Ability Activation *(wasted on Ironeye)*; Increased Maximum HP *(curse: Near Death Reduces Max HP)*; Physical Attack Up +2 |
| Deep B | **R00449** Deep Polished Drizzly Scene | Slowly restore HP for self and nearby allies when HP is low; Improved Affinity Damage Negation |
| Deep Y | **R01191** Deep Grand Luminous Scene | HP Restoration upon Thrusting Counterattack +1 *(curse: Reduced Faith and Strength)*; Attack power up when facing scarlet rot-afflicted enemy *(out of focus)*; Improved Physical Damage Negation +2 *(curse: All Resistances Down)* |

- **Curses: 3.** All Resistances Down (−2.5), Near Death Reduces Max HP (−2), Reduced Faith and Strength (near-free).
- **Dormant Powers:** none. **`unverified_effect` flags:** none.
- A sustain-leaning version: only one Physical Attack Up. Ironeye's Chalice (37.1) and Decrepit Ironeye's Goblet (36.0) follow; the Decrepit deep colors are **unverified** between sources.

## Gameplay loop

1. Carry two bows (the starting bow plus a found one; a Dormant Power for Bows is neutral) and swap every ~10 s, so the +10% attack and the added affinity stay up (60% uptime assumed).
2. The added random element hits weak points across the four elements, so you never need an infusion that matches the boss.
3. Mark, pop the weak point, and charge Single Shot as usual.

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
| Rally | 0 | does nothing for ranged |
| Thrusting-counter heal | 2.5% max HP per counter hit (base, wiki.gg; +1 guessed 3%), 15 counter hits per fight → 0.375 / 0.45 bars | hit count guessed; arrows counting confirmed by you |
| `[Ironeye] Boosts thrusting counterattacks after executing Art` | +20% × 0.4 window uptime × 0.3 counter share on bow damage | guesses; never picked |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Ultimate Art Charging Impaired | −10 | Single Shot is the revive |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (switch affinity +12 for 10 s, added-affinity +10%, switch boost +10% for 10 s, affinity sizes)
- https://eldenring.wiki.gg/wiki/Nightreign:Night_of_the_Champion (thrusting-counter heal 2.5% max HP)
- https://gamewith.net/eldenring-nightreign/57370 and https://www.pcgamesn.com/elden-ring-nightreign/relics-best (Night of the Lord's effects, Heolstor reward)
