# Guardian: Guard Tank (low-curse)

> Re-run 2026-10-31 with `scripts/guardian_sustain.py --max-curses N`. It uses the same weights, coverage and fight model as [guardian-sustain.md](guardian-sustain.md), including the multiplicative self-sustain product: eHP = (1 + max HP) × (1 + heals ÷ budget) ÷ damage taken. The only difference is a cap on total curses per loadout. Character reference: [characters/guardian.md](../characters/guardian.md).
>
> **Search fix (this run):** triples are now shortlisted with and without rally separately. Before, rally-less triples (notably anything with **R00823** Dark Night of the Fathom) fell off the shortlist. Every row below went up. The uncapped best is now the Chalice at 109.4 with **one near-free curse** (Reduced Faith and Strength), so caps 1 and 2 reproduce the sustain build exactly. This file's remaining job is the **zero-curse** loadout.
>
> **History:** this file used to hold the hand-picked builds from before the scripted search. Neither carried rally, which CLAUDE.md makes non-negotiable for melee. They've been replaced by the best capped loadouts, and every one of those carries rally.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all / guard_counter / skill / crit | 1.0 / 0.35 / 0.05 / 0.03 | all but "all" are guesses |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
> | Fight HP budget | 3.0 max-HP bars | guess |
> | Ally factor | 0.5 per ally, 2 allies | guess |

**Goal:** the same halberd + greatshield guard tank as the sustain build, with no curses at all.

Best two vessels per curse cap:

| Cap | Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|---|
| 0 | Guardian's Chalice | 97.3 | 17.9 | 61.4 | 18.0 | 0.0 |
| 0 | Forgotten Guardian's Goblet | 90.7 | 8.0 | 69.2 | 13.5 | 0.0 |
| 1 | Guardian's Chalice | 109.4 | 15.0 | 74.9 | 21.0 | −1.5 |
| 1 | Forgotten Guardian's Goblet | 101.9 | 16.5 | 74.9 | 12.0 | −1.5 |
| 2 | *(same as cap 1)* | | | | | |

**Recommendation:** the one curse in the cap-1 loadout (Reduced Faith and Strength) costs a halberd blocker very little, and it buys 12 points, mostly rally +2 over base rally. Use the [sustain build](guardian-sustain.md) unless you want literally zero curses.

Utility (Art gauge, cooldowns), poise, aggro and flat curse penalties are still hand-weighted.

## Best: Guardian's Chalice, 0 curses (Normal B Y W / Deep R B Y)

**Score 97.3:** damage 17.9, sustain 61.4, utility 18.0, penalties 0.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R00823** Dark Night of the Fathom (Blue) | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R00249** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks; Physical Attack Up +2 |
| Deep B | **R00318** Deep Polished Drizzly Scene | HP Restoration upon Katana Attacks *(does nothing with a halberd)*; Successful guarding fills more of the Art gauge |
| Deep Y | **R00211** Deep Polished Luminous Scene | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

- **Curses: 0.**
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Base rally and thrust-counter healing turn counters into healing. Dark Night of the Fathom adds +10% max HP, continuous regen and a low-HP regen.
  - Damage comes from Night Invader scaling (≈×1.2 over the run), Physical Attack Up +2 and shockwaves.
  - The Art gauge charges from blocking and Auto Charge +3. Wings of Salvation revives and heals the team.
- **Trade-offs:** 12.1 points below the 1-curse sustain build, almost all from base rally instead of +2.
- **Runner-up (96.7):** swap R00318 for **R01755** Deep Grand Drizzly Scene ([Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)*). That trades Art charge on block for +12% negation for allies.

## Alternative: Forgotten Guardian's Goblet, 0 curses (Normal G B B / Deep R B W)

**Score 90.7:** damage 8.0, sustain 69.2, utility 13.5, penalties 0.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R00788** Grand Tranquil Scene | [Guardian] Creates whirlwind when charging halberd attacks; Partial HP Restoration upon Post-Damage Attacks; Character Skill Cooldown Reduction +2 |
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R00394** Deep Polished Burning Scene | Successful guarding fills more of the Art gauge; Improved Affinity Damage Negation |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |
| Deep W | **R00211** Deep Polished Luminous Scene (Yellow) | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

- **Curses: 0.** **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Loop:** sustain-first. Heal on block, base rally (on a normal relic here), continuous and low-HP regen, Fathom's +10% max HP, affinity negation, and team negation from the whirlwind. Damage is low (8.0): no Night Invader and no Physical Attack Up.
- **Trade-offs:** 6.6 points below the zero-curse Chalice, and it needs 4 Sovereign Sigils to unlock. Use it only if you don't have the Chalice.

## Assumptions and unknowns

- **Curse cap counts every curse equally.** It doesn't know that `Repeated Evasions Lower Damage Negation` and off-stat curses are near-free.
- **Search depth:** 80 relics per slot, 2000 triples per side (split 1000 with rally / 1000 without). Not separately checked under a cap.
- **Multiplicative sustain** assumes heals restore a share of max HP. Whether flasks do is **(unverified)**.
- **Damage and sustain still add to each other**, so low-damage, sustain-heavy loadouts score well. See [guardian-sustain.md](guardian-sustain.md).
- **Sizes:** `Increased Maximum HP` +10% and the Great Church max HP (2.5% effective) are guesses, as are the per-fight heal amounts.
- **Rally** is anchored at 1.5 / 1.875 / 2.025 bars per fight, with tiers scored as highest-only **(unverified)**.
- **Guard counter HP boost** is still a guessed 18%.
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is a fine swap if you want stamina for long guard strings.
- **Chalice unlock:** needs Guardian Remembrance 2, which you should have (you own Remembrance 3 and 4 relics).
