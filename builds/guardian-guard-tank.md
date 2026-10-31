# Guardian: Guard Tank (low-curse)

> Re-run 2026-10-31 with `scripts/guardian_sustain.py --max-curses N`. It uses the same weights, coverage and fight model as [guardian-sustain.md](guardian-sustain.md). The only difference is a cap on total curses per loadout. Character reference: [characters/guardian.md](../characters/guardian.md).
>
> **Why this changed:** this file used to hold the hand-picked builds from before the scripted search. Neither carried rally (`Partial HP Restoration upon Post-Damage Attacks`), which CLAUDE.md makes non-negotiable for melee. Under the current rules they score:
> - **65.3:** the old Forgotten Goblet build (R00855, R01922, R00823 / R01176, R00306, R00394; 1 curse).
> - **54.5:** the old Goblet build (R01922, R00823, R00855 / R01755, R01318, R00387; 2 curses).
>
> The same vessels reach 92–93 with the same or fewer curses. The file keeps its purpose (a guard tank that carries few curses) and now holds the best capped loadouts. Every one carries rally.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all / guard_counter / skill / crit | 1.0 / 0.35 / 0.05 / 0.03 | guesses except "all" |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
> | Fight HP budget | 3.0 max-HP bars | guess |
> | Ally factor | 0.5 per ally, 2 allies | guess |

**Goal:** the same halberd + greatshield guard tank as the sustain build, without the real curses (Reduced Vigor and Arcane, All Resistances Down) the top sustain loadout carries.

Best loadout per curse cap (the uncapped best is the Chalice at 102.0 with 3 curses):

| Cap | Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|---|
| 0 | Guardian's Chalice | 91.4 | 20.9 | 49.5 | 21.0 | 0.0 |
| 0 | Forgotten Guardian's Goblet | 85.2 | 12.1 | 52.1 | 21.0 | 0.0 |
| 1 | Guardian's Chalice | 96.0 | 22.6 | 56.5 | 18.0 | −1.0 |
| 1 | Forgotten Guardian's Goblet | 92.3 | 22.6 | 53.2 | 18.0 | −1.5 |
| 2 | Guardian's Chalice | 99.2 | 29.3 | 56.5 | 18.0 | −4.5 |
| 2 | Guardian's Goblet | 93.0 | 9.5 | 63.5 | 21.0 | −1.0 |

Utility (Art gauge, cooldowns), poise, aggro and curse penalties are still hand-weighted.

## Best: Guardian's Chalice, 1 curse (Normal B Y W / Deep R B Y)

**Score 96.0:** damage 22.6, sustain 56.5, utility 18.0, penalties −1.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R01914** Grand Luminous Scene | [Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking *(wasted on Guardian)*; HP Recovery From Successful Guarding; Successful guarding fills more of the Art gauge |
| Normal W | **R00156** Polished Luminous Scene (Yellow) | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R01789** Deep Grand Drizzly Scene | FP Restoration upon Dagger Attacks *(does nothing with a halberd)*; Slowly restore HP for self and nearby allies when HP is low; Guard counter is given a boost based on current HP |
| Deep Y | **R01700** Deep Grand Luminous Scene | FP Restoration upon Straight Sword Attacks *(does nothing with a halberd)*; Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Rune Acquisition)*; Improved Gravity Sorcery *(out of focus)* |

- **Curses: 1.** Reduced Rune Acquisition is acceptable: it slows leveling a little and doesn't touch combat.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Rally +2 recovers damage you take if you hit back right after. The low-HP regen backs it up.
  - Damage comes from Night Invader scaling (≈×1.2 over the run) and two guard-counter boosts (Improved Guard Counters and the HP-based boost). It has no Physical Attack Up.
  - The Art gauge charges from blocking and Auto Charge +3. Wings of Salvation revives and heals the team, and the whirlwind gives allies +12% damage negation.
- **Trade-offs:** It scores 6 points below the uncapped Chalice (102.0). It loses 12.4 damage points (no Physical Attack Up +2/+3/+4) and wins back 6.5 in penalties by dropping the Vigor and resistance curses. Sustain is unchanged (56.5).
- **Near-tie (95.8, 1 curse):** a different set of relics. It's arguably better, because its one curse does nothing to a blocker:

  | Slot | Relic | Effects (curse attached) |
  |---|---|---|
  | Normal B | **R01922** Witch's Brooch | as above |
  | Normal Y | **R00156** Polished Luminous Scene | as above |
  | Normal W | **R01208** Grand Drizzly Scene (Blue) | Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2 |
  | Deep R | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |
  | Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |
  | Deep Y | **R00211** Deep Polished Luminous Scene | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

  Steel Guard can't dodge, so the evasion curse is near-free. It trades Improved Guard Counters for Physical Attack Up +2 and thrust-counter healing. 1 curse, no Dormant Powers, no flags.
- **Zero curses (91.4):** the near-tie above with **R00249** Deep Polished Burning Scene in Deep R (Partial HP Restoration upon Post-Damage Attacks; Physical Attack Up +2). That's base-tier rally instead of +2, and it loses the Great Church max HP. That costs 8 sustain points, and Physical Attack Up +2 gives 3 damage back.

## Alternative: Guardian's Goblet, 2 evasion-only curses (Normal B B G / Deep B B G)

**Score 93.0:** damage 9.5, sustain 63.5, utility 21.0, penalties −1.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal G | **R01182** Grand Tranquil Scene | [Guardian] Successful guards send out shockwaves while ability is active; Improved Throwing Pot Damage *(out of focus)*; Ultimate Art Auto Charge +3 |
| Deep B | **R00212** Deep Polished Drizzly Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)* |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |
| Deep G | **R01867** Deep Grand Tranquil Scene | [Revenant] Increased Max FP upon Ability Activation *(wasted on Guardian)*; Successful guarding fills more of the Art gauge; Guard counter is given a boost based on current HP |

- **Curses: 2.** Both lower damage negation only after you dodge. That's near-free for a Guardian who blocks instead of rolling, so this is effectively curse-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:** pure sustain. Heal on block, rally +2, thrust-counter healing +1, regen and Max HP, plus Flask Also Heals Allies for the team. The Art gauge charges from blocking, kills and Auto Charge +3. Shockwaves and the HP-based guard-counter boost are the only damage.
- **Trade-offs:** The most sustain of any capped loadout (63.5), but almost no damage (9.5): no Night Invader and no Physical Attack Up. Pick it when the team has damage covered and needs you to survive and revive.
- **Runner-up (92.3):** swap R00823 for **R01299** Grand Drizzly Scene ([Raider] Duration of Ultimate Art extended *(wasted on Guardian)*; Attack power increased for each Night Invader defeated; Vigor +2). That moves about 9 points from sustain into damage.

**Forgotten Guardian's Goblet (1 curse, 92.3):** R01182, R00115, R01299 / **R00437** Deep Polished Burning Scene (Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Faith and Strength)*; Successful guarding fills more of the Art gauge), R01789, R01176. Reduced Faith and Strength costs a little halberd damage (Str B).

## Assumptions and unknowns

- **Curse cap counts every curse equally.** The cap doesn't know that evasion curses are near-free for this build. That's why the 2-curse Goblet is effectively as clean as a 0-curse loadout.
- **Search depth:** 80 relics per slot, 2000 triples per side (converged on the top uncapped vessels; not separately checked under a cap).
- **Rally** is a meta anchor at 50% eHP base (20 / 25 / 27 points), with tiers scored as highest-only **(unverified)**.
- **Sustain sizes are mostly guesses** (blocks and thrust counters per fight, regen, team heals). See the script and [guardian-sustain.md](guardian-sustain.md).
- **Guard counter HP boost** is still a guessed 18% (wiki.gg's per-HP formula has an ambiguous unit).
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is a fine swap for R01789 or R01867 if you want stamina for long guard strings.
- **Chalice unlock:** needs Guardian Remembrance 2, which you should have (you own Remembrance 3 and 4 relics).
