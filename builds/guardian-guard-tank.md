# Guardian: Guard Tank (low-curse)

> Re-run 2026-10-31 with `scripts/guardian_sustain.py --max-curses N`. It uses the same weights, coverage and fight model as [guardian-sustain.md](guardian-sustain.md), including the multiplicative self-sustain product: eHP = (1 + max HP) × (1 + heals ÷ budget) ÷ damage taken. The only difference is a cap on total curses per loadout. `Reduced Damage Negation After Evading` now scores as very bad (−8), while `Repeated Evasions Lower Damage Negation` stays near-free (−0.5). The capped loadouts below only carry the latter, so they didn't change. Character reference: [characters/guardian.md](../characters/guardian.md).
>
> **History:** this file used to hold the hand-picked builds from before the scripted search. Neither carried rally, which CLAUDE.md makes non-negotiable for melee. Under the earlier additive model they scored 65.3 and 54.5. They've been replaced by the best capped loadouts, and every one of those carries rally.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all / guard_counter / skill / crit | 1.0 / 0.35 / 0.05 / 0.03 | all but "all" are guesses |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
> | Fight HP budget | 3.0 max-HP bars | guess |
> | Ally factor | 0.5 per ally, 2 allies | guess |

**Goal:** the same halberd + greatshield guard tank as the sustain build, without the real curses (Rot Buildup When Below Max HP, All Resistances Down, Reduced Vigor and Arcane) the top sustain loadouts carry.

Best two vessels per curse cap (the uncapped best is the Chalice at 104.1 with 3 curses):

| Cap | Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|---|
| 0 | Guardian's Chalice | 93.2 | 20.9 | 51.2 | 21.0 | 0.0 |
| 0 | Forgotten Guardian's Goblet | 89.0 | 12.1 | 56.0 | 21.0 | 0.0 |
| 1 | Guardian's Chalice | 99.1 | 17.9 | 60.7 | 21.0 | −0.5 |
| 1 | Forgotten Guardian's Goblet | 96.0 | 9.5 | 66.0 | 21.0 | −0.5 |
| 2 | Guardian's Chalice | 101.0 | 29.3 | 58.6 | 18.0 | −4.8 |
| 2 | Forgotten Guardian's Goblet | 97.9 | 17.6 | 65.8 | 18.0 | −3.5 |

The cap counts every curse equally, but some curses cost a blocker almost nothing. The Forgotten Goblet's 97.5 loadout (R01182, R00115, R00823 / R01176, R01318, R00162) has 2 curses, both near-free: Reduced Dexterity and Faith, and Repeated Evasions Lower Damage Negation. It's in [guardian-sustain.md](guardian-sustain.md) as the alternative. The cap-2 Forgotten row above (97.9) carries All Resistances Down instead.

Utility (Art gauge, cooldowns), poise, aggro and flat curse penalties are still hand-weighted.

## Best: Guardian's Chalice, 1 near-free curse (Normal B Y W / Deep R B Y)

**Score 99.1:** damage 17.9, sustain 60.7, utility 21.0, penalties −0.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R01208** Grand Drizzly Scene (Blue) | Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2 |
| Deep R | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |
| Deep Y | **R00211** Deep Polished Luminous Scene | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

- **Curses: 1.** Repeated Evasions Lower Damage Negation is near-free: it only kicks in on chained dodges, and Guardian rarely chains them.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Rally +2 and thrust-counter healing turn every counter into healing. Max HP grows as you clear Great Church bosses.
  - Damage comes from Night Invader scaling (≈×1.2 over the run) and Physical Attack Up +2.
  - The Art gauge charges from blocking, kills and Auto Charge +3. Wings of Salvation revives and heals the team, and the whirlwind gives allies +12% damage negation.
- **Trade-offs:** It's 5.0 points below the uncapped Chalice (104.1) and carries no real curse. It has no Improved Guard Counters. R00211 can be swapped for **R00238** Deep Polished Luminous Scene (HP Recovery From Successful Guarding; FP Restoration upon Dagger Attacks *(does nothing with a halberd)*). That ties at 99.1, because thrust-counter healing is already on R01208.
- **Zero curses (93.2):** swap R00162 for **R00249** Deep Polished Burning Scene (Partial HP Restoration upon Post-Damage Attacks; Physical Attack Up +2). That's base rally instead of +2, without the Great Church max HP.
- **Cap 2 (101.0):** Witch's Brooch, R01914, R00156 / R01176, R01789, R00128. It adds Improved Guard Counters and Physical Attack Up +4 (damage 29.3), but R00128 brings **Reduced Vigor and Arcane**, a real cost.

## Alternative: Forgotten Guardian's Goblet, 1 near-free curse, with Dark Night of the Fathom (Normal G B B / Deep R B W)

**Score 96.0:** damage 9.5, sustain 66.0, utility 21.0, penalties −0.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R01182** Grand Tranquil Scene | [Guardian] Successful guards send out shockwaves while ability is active; Improved Throwing Pot Damage *(out of focus)*; Ultimate Art Auto Charge +3 |
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |
| Deep W | **R01867** Deep Grand Tranquil Scene (Green) | [Revenant] Increased Max FP upon Ability Activation *(wasted on Guardian)*; Successful guarding fills more of the Art gauge; Guard counter is given a boost based on current HP |

- **Curses: 1.** Repeated Evasions Lower Damage Negation is near-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:** sustain-first. Heal on block, rally +2, continuous and low-HP regen, two max-HP effects (Fathom +10% and Great Church), and Flask Also Heals Allies. Damage comes from shockwaves and the HP-based guard-counter boost, which stays strong because you stay near full HP.
- **Trade-offs:** More sustain than the Chalice pick (66.0 vs 60.7), but little damage (9.5): no Night Invader and no Physical Attack Up. The Forgotten Goblet needs 4 Sovereign Sigils to unlock.
- **Runner-up (95.9):** swap R01867 for **R00394** Deep Polished Burning Scene (Successful guarding fills more of the Art gauge; Improved Affinity Damage Negation). That trades the guard-counter HP boost for affinity negation.

## Assumptions and unknowns

- **Curse cap counts every curse equally.** It doesn't know that `Repeated Evasions Lower Damage Negation` and off-stat curses are near-free. That's why the Forgotten Goblet's 97.5 loadout, with 2 near-free curses, doesn't top the cap-2 row.
- **Search depth:** 80 relics per slot, 2000 triples per side. Not separately checked under a cap.
- **Multiplicative sustain** assumes heals restore a share of max HP. Whether flasks do is **(unverified)**.
- **Damage and sustain still add to each other**, so low-damage, sustain-heavy loadouts score well. See [guardian-sustain.md](guardian-sustain.md).
- **Sizes:** `Increased Maximum HP` +10% and the Great Church max HP (2.5% effective) are guesses, as are the per-fight heal amounts.
- **Rally** is anchored at 1.5 / 1.875 / 2.025 bars per fight, with tiers scored as highest-only **(unverified)**.
- **Guard counter HP boost** is still a guessed 18%.
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is a fine swap if you want stamina for long guard strings.
- **Chalice unlock:** needs Guardian Remembrance 2, which you should have (you own Remembrance 3 and 4 relics).
