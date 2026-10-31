# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights, coverage and fight model at the top of the script). Rules from CLAUDE.md:
> - Attack buffs stack and multiply.
> - **Self-sustain is one effective-HP product:** eHP = (1 + max HP) × (1 + heals ÷ budget) ÷ damage taken.
> - Damage and sustain share one scale: 0.4 points per 1% of total damage or of effective HP.
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina is worth 0.
> - Meta anchors: Night Invader ≈ +20% damage. Rally is non-negotiable, and the script flags any loadout without it; every vessel's top loadouts carry it.
> - Post-1.03 sizes from eldenring.wiki.gg: `Physical Attack Up` 4/5/6/10.5/12%, `Improved Guard Counters` 23/25/29%.
>
> **Changes in this run (multiplicative sustain):**
> - **Max HP, heals and negation now multiply.** Before, each self-sustain effect was scored against a bare baseline and the results were added up. That undervalued max HP and negation, because every heal restores a share of max HP and negation makes each bar last longer. With the Chalice's healing, `Increased Maximum HP` (+10%, size **unverified**) is now worth about 10 points instead of 4.
> - **Rally is a heal**, anchored at 1.5 max-HP bars per fight (base), 1.875 (+1) and 2.025 (+2). On its own that's still 50% eHP, 20 points.
> - **Reduced Vigor and Arcane** now lowers max HP by 5% inside the product (guess: it mirrors the +5% of a Vigor +3 relic). Its flat −4 penalty is gone. Its cost now grows with how much healing the loadout has, about −4.3 in the old best.
> - **Result:** loadouts lean further toward sustain. Dark Night of the Fathom (R00823) now makes the best loadout on Giant's Cradle and on the Forgotten Goblet.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all / guard_counter / skill / crit | 1.0 / 0.35 / 0.05 / 0.03 | all but "all" are guesses |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
> | Fight HP budget | 3.0 max-HP bars | guess |
> | Ally factor | 0.5 per ally, 2 allies | guess. Team effects add on top of the self product. |
>
> Character reference: [characters/guardian.md](../characters/guardian.md). Low-curse variants: [guardian-guard-tank.md](guardian-guard-tank.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Best loadout per vessel (all carry rally):

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Guardian's Chalice | 105.7 | 18.9 | 74.8 | 20.0 | −8.0 |
| Giant's Cradle Grail | 102.2 | 7.0 | 84.7 | 12.0 | −1.5 |
| Sealed Guardian's Urn | 99.8 | 13.8 | 77.1 | 18.0 | −9.0 |
| Forgotten Guardian's Goblet | 99.6 | 10.2 | 72.9 | 18.0 | −1.5 |
| Guardian's Goblet | 98.5 | 7.0 | 86.5 | 9.0 | −4.0 |
| Guardian's Urn | 96.1 | 8.0 | 76.1 | 20.0 | −8.0 |
| Decrepit Guardian's Goblet | 94.8 | 28.7 | 60.1 | 18.0 | −12.0 |
| Soot-Covered Guardian's Urn | 94.7 | 25.6 | 54.5 | 22.0 | −7.5 |
| Sacred Erdtree Grail | 94.1 | 24.0 | 62.7 | 20.0 | −12.5 |
| Spirit Shelter Grail | 91.3 | 32.5 | 49.2 | 18.0 | −8.5 |
| Scadutree Grail | 89.5 | 22.0 | 62.0 | 9.0 | −3.5 |

Utility (Art gauge, cooldowns), poise, aggro and flat curse penalties are still hand-weighted.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 105.7:** damage 18.9, sustain 74.8, utility 20.0, penalties −8.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R01922** Witch's Brooch (Blue) | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Deep R | **R01025** Deep Grand Burning Scene | [Ironeye] Improved Arcane, Reduced Dexterity *(wasted on Guardian: no bonus and no penalty)*; Improved Guard Counters; Improved Affinity Damage Negation |
| Deep B | **R00212** Deep Polished Drizzly Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)* |
| Deep Y | **R01527** Deep Grand Luminous Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Successful guarding fills more of the Art gauge +1 *(curse: Rot Buildup When Below Max HP)*; Increased Maximum HP *(curse: All Resistances Down)* |

- **Curses: 4.**
  - **Rot Buildup When Below Max HP** is a real cost. A tank spends a lot of time below max HP, though heal-on-block and rally keep topping it off.
  - **All Resistances Down** is a real cost, and it makes the Rot buildup worse.
  - Reduced Damage Negation After Evading and Repeated Evasions Lower Damage Negation are near-free: Steel Guard can't dodge.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge (+1), and sends out a shockwave.
  - Rally +2 and thrust-counter healing +1 turn every counter into healing. Max HP +10% and affinity negation make all of it go further.
  - Damage comes from Night Invader scaling (≈×1.2 over the run) and Improved Guard Counters. It has no Physical Attack Up.
  - The Art gauge charges from blocking and Auto Charge +3. Wings of Salvation revives and heals the team, the whirlwind gives allies +12% damage negation, and your flasks heal allies too.
- **Trade-offs:**
  - It has much less damage than the previous best (18.9 vs 35.0) and much more sustain (74.8 vs 58.6).
  - The previous best scores 103.8 under the new model. That's R01922, R00156, R01208 / R01176, R00306, R00128, with 3 curses: Reduced Vigor and Arcane, All Resistances Down, Reduced Intelligence and Dexterity. It's within 2 points and is the pick if you want damage.
- **Runner-up on the same vessel (105.6):** swap R00115 for **R01927** Golden Sprout (Red, so it goes in the W slot; Witch's Brooch moves to B). Its effects are [Executor] Roaring restores HP while Art is active *(wasted on Guardian)*; HP Recovery From Successful Guarding; Slowly restore HP for self and nearby allies when HP is low. That trades Flask Also Heals Allies for low-HP regen.

## Alternative: Giant's Cradle Grail (Normal B B B / Deep B B B), near-free curses only

**Score 102.2:** damage 7.0, sustain 84.7, utility 12.0, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep B | **R00212** Deep Polished Drizzly Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)* |
| Deep B | **R01318** Deep Grand Drizzly Scene | Successful guarding fills more of the Art gauge; Improved Frenzied Flame Incantations *(out of focus)*; Improved Affinity Damage Negation +1 *(curse: Reduced Dexterity and Faith)* |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |

- **Curses: 3, all near-free.** The two evasion curses don't affect a blocker. Reduced Dexterity and Faith is near-free (Dex C, Faith unused).
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:** pure sustain. Heal on block, rally +2, thrust-counter healing +1, continuous and low-HP regen, Max HP +10% and affinity negation +1, plus Flask Also Heals Allies. Shockwaves are the only damage.
- **Trade-offs:** The most sustain of any top loadout and no real curses, but almost no damage (7.0): no Night Invader, no Physical Attack Up, no guard-counter boost. Pick it when the team has damage covered.
- **Forgotten Guardian's Goblet (99.6)** is the same idea with some damage. Its loadout is R01182 (shockwaves; Improved Throwing Pot Damage; Ultimate Art Auto Charge +3), R00115, R00823 / R01176 (Improved Guard Counters), R00212, R01318. It has the same 3 near-free curses.

## Assumptions and unknowns

- **Search depth:** 80 relics per slot and 2000 triples per side. The Chalice was re-checked at 120 / 4000 under the new model and matched (105.7). Other vessels weren't re-checked.
- **Multiplicative sustain** assumes heals restore a share of max HP. Whether flasks do (so the whole budget scales with max HP) is **(unverified)**. If flasks heal a fixed amount, max HP is somewhat overvalued.
- **Damage and sustain still add to each other.** Within each side, effects compound, so a loadout that piles into one side gets increasing returns. That's part of why the top loadouts lean so hard into sustain. A model that multiplied damage by eHP (time to kill against time to die) would favor balance more. It isn't in CLAUDE.md.
- **Sizes:** `Increased Maximum HP` +10% is unsourced. Heal amounts per fight (about 60 blocks, 10 thrust counters, the regens) are guesses. The Vigor curse at −5% max HP is a guess.
- **Post-1.03 sizes:** `Physical Attack Up` and `Improved Guard Counters` come from eldenring.wiki.gg. The guard-counter tier labels are inferred **(unverified)**.
- **Guard counter HP boost** is still scored as a guessed 18%.
- **Rally** tiers are scored as highest-only. wiki.gg says +1 and +2 stack with each other **(unverified)**.
- **Night Invader effect:** about +20% damage per CLAUDE.md. Copies are assumed not to stack **(unverified)**.
- **Stamina is unweighted** (CLAUDE.md).
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
