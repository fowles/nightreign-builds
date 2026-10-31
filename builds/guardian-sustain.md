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
> **Changes in this run:**
> - **`Reduced Damage Negation After Evading` is now very bad (−8).** It used to be −0.5. Guardian still dodges outside Steel Guard, and a mistimed dodge then costs extra damage. `Repeated Evasions Lower Damage Negation` stays near-free (−0.5). This knocked out R00212 (rally +2 / thrust heal +1), which carries both curses. It had been in the previous Chalice, Cradle and Forgotten loadouts.
> - **Earlier this session: multiplicative sustain.** Max HP, heals and negation multiply. Rally is a heal of 1.5 / 1.875 / 2.025 max-HP bars per fight. Reduced Vigor and Arcane lowers max HP by 5% (guess) inside the product.
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
| Guardian's Chalice | 104.1 | 18.0 | 73.6 | 20.0 | −7.5 |
| Forgotten Guardian's Goblet | 97.9 | 17.6 | 65.8 | 18.0 | −3.5 |
| Sealed Guardian's Urn | 97.4 | 20.2 | 64.7 | 21.0 | −8.5 |
| Guardian's Goblet | 96.6 | 19.5 | 61.1 | 21.0 | −5.0 |
| Guardian's Urn | 96.1 | 8.0 | 76.1 | 20.0 | −8.0 |
| Giant's Cradle Grail | 94.9 | 7.0 | 79.4 | 12.0 | −3.5 |
| Decrepit Guardian's Goblet | 94.8 | 28.7 | 60.1 | 18.0 | −12.0 |
| Soot-Covered Guardian's Urn | 94.7 | 25.6 | 54.5 | 22.0 | −7.5 |
| Sacred Erdtree Grail | 94.1 | 24.0 | 62.7 | 20.0 | −12.5 |
| Spirit Shelter Grail | 91.3 | 32.5 | 49.2 | 18.0 | −8.5 |
| Scadutree Grail | 89.5 | 22.0 | 62.0 | 9.0 | −3.5 |

Utility (Art gauge, cooldowns), poise, aggro and flat curse penalties are still hand-weighted.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 104.1:** damage 18.0, sustain 73.6, utility 20.0, penalties −7.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R01922** Witch's Brooch (Blue) | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Deep R | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |
| Deep B | **R01789** Deep Grand Drizzly Scene | FP Restoration upon Dagger Attacks *(does nothing with a halberd)*; Slowly restore HP for self and nearby allies when HP is low; Guard counter is given a boost based on current HP |
| Deep Y | **R01527** Deep Grand Luminous Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Successful guarding fills more of the Art gauge +1 *(curse: Rot Buildup When Below Max HP)*; Increased Maximum HP *(curse: All Resistances Down)* |

- **Curses: 3.**
  - **Rot Buildup When Below Max HP** is a real cost. A tank spends a lot of time below max HP, though heal-on-block, rally and the low-HP regen keep topping it off.
  - **All Resistances Down** is a real cost, and it makes the Rot buildup worse.
  - Repeated Evasions Lower Damage Negation is near-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge (+1), and sends out a shockwave.
  - Rally +2 turns every counter into healing, and the low-HP regen catches you if you slip. Max HP +10% and Great Church max HP make all of it go further.
  - Damage comes from Night Invader scaling (≈×1.2 over the run) and the HP-based guard-counter boost, which stays strong because you stay near full HP. It has no Physical Attack Up.
  - The Art gauge charges from blocking and Auto Charge +3. Wings of Salvation revives and heals the team, the whirlwind gives allies +12% damage negation, and your flasks heal allies too.
- **Trade-offs:**
  - Low damage (18.0) for a lot of sustain (73.6).
  - The damage-leaning loadout is a near-tie at 103.8, with 3 curses: Reduced Vigor and Arcane, All Resistances Down, Reduced Intelligence and Dexterity. Its relics are R01922, R00156, R01208 (Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2) / R01176 ([Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped; Improved Guard Counters), R00306 (HP Recovery From Successful Guarding; Physical Attack Up +3 *(curse: All Resistances Down)*), R00128 (Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)*). It deals almost twice the damage (35.0) and is the pick if your team needs it.
- **Runner-up on the same vessel (103.5):** swap R01789 for **R00449** Deep Polished Drizzly Scene (Slowly restore HP for self and nearby allies when HP is low; Improved Affinity Damage Negation). That trades the guard-counter HP boost for affinity negation.

## Alternative: Forgotten Guardian's Goblet (Normal G B B / Deep R B W), near-free curses only

**Score 97.5:** damage 10.2, sustain 70.3, utility 18.0, penalties −1.0. This is the vessel's #3 loadout. Its #1 (97.9) is only 0.4 higher but carries All Resistances Down; see below.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R01182** Grand Tranquil Scene | [Guardian] Successful guards send out shockwaves while ability is active; Improved Throwing Pot Damage *(out of focus)*; Ultimate Art Auto Charge +3 |
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R01318** Deep Grand Drizzly Scene | Successful guarding fills more of the Art gauge; Improved Frenzied Flame Incantations *(out of focus)*; Improved Affinity Damage Negation +1 *(curse: Reduced Dexterity and Faith)* |
| Deep W | **R00162** Deep Polished Burning Scene (Red) | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |

- **Curses: 2, both near-free.** Reduced Dexterity and Faith costs little (Dex C, Faith unused). Repeated Evasions Lower Damage Negation only kicks in on chained dodges.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:** sustain-first. Heal on block, rally +2, continuous and low-HP regen, two max-HP effects (Fathom +10% and Great Church), affinity negation +1, and Flask Also Heals Allies. Damage comes from shockwaves and Improved Guard Counters.
- **Trade-offs:** The cleanest high scorer: no real curses, with Dark Night of the Fathom doing its job. But it has little damage (10.2): no Night Invader and no Physical Attack Up. It needs 4 Sovereign Sigils to unlock.
- **Vessel #1 (97.9, 2 curses):** swap R00115 for **R01208** (Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2) and R01318 for **R00306** (HP Recovery From Successful Guarding; Physical Attack Up +3 *(curse: All Resistances Down)*). That gives more damage (17.6), but All Resistances Down is a real curse.

## Assumptions and unknowns

- **Search depth:** 80 relics per slot and 2000 triples per side. The Chalice matched a 120 / 4000 search before this curse change. It wasn't re-checked after.
- **`Reduced Damage Negation After Evading` at −8** puts it on the same level as the `Taking Damage` buildup curses. The exact size of the negation drop is unknown.
- **Multiplicative sustain** assumes heals restore a share of max HP. Whether flasks do (so the whole budget scales with max HP) is **(unverified)**. If flasks heal a fixed amount, max HP is somewhat overvalued.
- **Damage and sustain still add to each other.** Within each side, effects compound, so a loadout that piles into one side gets increasing returns. That's part of why the top loadouts lean into sustain. A damage × eHP model would favor balance more. It isn't in CLAUDE.md.
- **Sizes:** `Increased Maximum HP` +10% is unsourced. Heal amounts per fight (about 60 blocks, 10 thrust counters, the regens) are guesses. The Vigor curse at −5% max HP is a guess.
- **Post-1.03 sizes:** `Physical Attack Up` and `Improved Guard Counters` come from eldenring.wiki.gg. The guard-counter tier labels are inferred **(unverified)**.
- **Guard counter HP boost** is still scored as a guessed 18%.
- **Rally** tiers are scored as highest-only. wiki.gg says +1 and +2 stack with each other **(unverified)**.
- **Night Invader effect:** about +20% damage per CLAUDE.md. Copies are assumed not to stack **(unverified)**.
- **Stamina is unweighted** (CLAUDE.md).
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
