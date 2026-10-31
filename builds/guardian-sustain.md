# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights, coverage and fight model at the top of the script). Rules from CLAUDE.md:
> - Attack buffs stack and multiply. Negations multiply.
> - Damage and sustain share one scale: 0.4 points per 1% of total damage or of effective HP.
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina is worth 0.
> - Meta anchors: Night Invader ≈ +20% damage; rally is non-negotiable. The script now flags any loadout without rally. Every vessel's top three loadouts carry it.
> - Post-1.03 sizes from eldenring.wiki.gg: `Physical Attack Up` 4/5/6/10.5/12%, `Improved Guard Counters` 23/25/29%.
>
> **Changes in this run:**
> - **Wider search (the big one).** The old defaults kept the top 40 relics per slot and the top 600 triples per side. That missed the best loadouts: a triple ranked on its own side gets credit for effects (rally, Night Invader, heal-on-block) that the other side already supplies. The defaults are now 80 / 2000, which match 120 / 4000 on the Chalice and the Forgotten Goblet. The Chalice went from 94.8 to 102.0.
> - **Duplicate attack buffs on one relic** now each count. Before, a relic with two copies of a stacking family counted only one. No owned relic was affected in the final loadouts.
> - **Newly weighted in-focus effects:** `Improved Melee Attack Power` 5% (wiki.gg), `Improved Skill Attack Power` 15% (wiki.gg) at skill coverage 0.05, `Improved Critical Hits` 18/23% (+1 from wiki.gg, base guessed) at crit coverage 0.03, `Taking attacks improves attack power` 3% (guess), `Attack power increased for each evergaol prisoner defeated` 5% (guess), and `Max HP increased for each great enemy defeated at a Great Church.` 2.5% eHP (guess). None of them made a top loadout.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all | 1.0 | `Physical Attack Up`, Night Invader, halberd and melee attack power |
> | Damage coverage: guard_counter | 0.35 | guess |
> | Damage coverage: skill | 0.05 | guess. Whirlwind is cast for its negation buff. |
> | Damage coverage: crit | 0.03 | guess |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
> | Fight HP budget | 3.0 max-HP bars | guess |
> | Ally factor | 0.5 per ally, 2 allies | guess |
>
> Character reference: [characters/guardian.md](../characters/guardian.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Best loadout per vessel (all carry rally):

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Guardian's Chalice | 102.0 | 35.0 | 56.5 | 18.0 | −7.5 |
| Forgotten Guardian's Goblet | 95.2 | 35.0 | 47.2 | 18.0 | −5.0 |
| Guardian's Goblet | 93.1 | 30.0 | 47.2 | 21.0 | −5.0 |
| Guardian's Urn | 92.5 | 25.1 | 54.5 | 18.0 | −5.0 |
| Soot-Covered Guardian's Urn | 92.5 | 30.8 | 45.8 | 18.0 | −2.0 |
| Giant's Cradle Grail | 91.4 | 7.0 | 73.9 | 12.0 | −1.5 |
| Sacred Erdtree Grail | 90.4 | 24.0 | 58.5 | 20.0 | −12.0 |
| Sealed Guardian's Urn | 89.3 | 24.1 | 50.2 | 22.0 | −7.0 |
| Decrepit Guardian's Goblet | 88.8 | 32.5 | 44.8 | 22.0 | −10.5 |
| Scadutree Grail | 85.2 | 23.6 | 53.1 | 9.0 | −0.5 |
| Spirit Shelter Grail | 85.2 | 32.5 | 43.1 | 18.0 | −8.5 |

Utility (Art gauge, cooldowns) and a few sustain effects (poise, aggro) are still hand-weighted. So are curse penalties.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 102.0:** damage 35.0, sustain 56.5, utility 18.0, penalties −7.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R01208** Grand Drizzly Scene (Blue) | Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2 |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R00306** Deep Polished Drizzly Scene | HP Recovery From Successful Guarding; Physical Attack Up +3 *(curse: All Resistances Down)* |
| Deep Y | **R00128** Deep Polished Luminous Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)* |

- **Curses: 3.**
  - **Reduced Vigor and Arcane** is a real cost. Guardian scales S in Vigor, so it shrinks the HP pool that every heal is a percentage of.
  - **All Resistances Down** is a real cost.
  - Reduced Intelligence and Dexterity is near-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Rally +2 recovers damage you take if you hit back right after. Thrusting counters heal too.
  - Damage multiplies from three Physical Attack Up copies (+2, +3, +4: ×1.06 × 1.105 × 1.12 ≈ ×1.31), Night Invader scaling (≈×1.2 over the run), and Improved Guard Counters on counters.
  - The Art gauge charges from blocking and Auto Charge +3. Wings of Salvation revives and heals the team, and the whirlwind gives allies +12% damage negation.
- **Trade-offs:** The strongest damage and sustain together, but it carries two real curses. Compared with the previous best, R01208 replaces R01914 (Grand Luminous Scene). That adds Physical Attack Up +2 and thrust-counter healing, and drops a wasted [Executor] effect and a redundant heal-on-block.
- **Curse-light runner-up (98.2, 2 curses):** replace R00128 with **R01700** Deep Grand Luminous Scene. Its effects are FP Restoration upon Straight Sword Attacks *(does nothing with a halberd)*; Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Rune Acquisition)*; Improved Gravity Sorcery *(out of focus)*. You keep rally +2 and drop the Vigor curse, but lose Physical Attack Up +4. **This is the pick if you think the Vigor curse costs more than the script's −4.**

## Alternative: Forgotten Guardian's Goblet (Normal G B B / Deep R B W), no Vigor curse

**Score 95.2:** damage 35.0, sustain 47.2, utility 18.0, penalties −5.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R01182** Grand Tranquil Scene | [Guardian] Successful guards send out shockwaves while ability is active; Improved Throwing Pot Damage *(out of focus)*; Ultimate Art Auto Charge +3 |
| Normal B | **R01208** Grand Drizzly Scene | Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2 |
| Normal B | **R01299** Grand Drizzly Scene | [Raider] Duration of Ultimate Art extended *(wasted on Guardian)*; Attack power increased for each Night Invader defeated; Vigor +2 |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R00306** Deep Polished Drizzly Scene | HP Recovery From Successful Guarding; Physical Attack Up +3 *(curse: All Resistances Down)* |
| Deep W | **R00531** Deep Polished Tranquil Scene (Green) | Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Reduced Strength and Intelligence)*; Physical Attack Up +4 *(curse: Reduced Dexterity and Faith)* |

- **Curses: 3.** All Resistances Down is a real cost. Reduced Strength and Intelligence is mild (Str B). Reduced Dexterity and Faith is near-free. There's no Vigor curse.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Trade-offs:** The same damage as the Chalice (three Physical Attack Up copies, Night Invader, guard counters), but less sustain. It loses the [Guardian] Art team heal (Witch's Brooch) and has rally +1 instead of +2. It suits you if you'd rather not lose Vigor.
- **Runner-up on the same vessel (95.0):** swap R01182 for **R01101** Grand Tranquil Scene and R01299 for **R01922** Witch's Brooch. R01101's effects are Improved Frenzied Flame Incantations *(out of focus)*; Attack power increased for each Night Invader defeated; Strength +2. That brings back the Art team heal, but drops Auto Charge (utility 9.0).

**Maximum-sustain option:** Giant's Cradle Grail (91.4: damage 7.0, sustain 73.9) is unchanged. It has the most healing of any vessel and almost no damage.

## Assumptions and unknowns

- **Search depth:** 80 relics per slot and 2000 triples per side. Two vessels were checked at 120 / 4000 and matched. Lower-ranked vessels weren't checked at the wider setting, so their scores are lower bounds.
- **Post-1.03 sizes:** eldenring.wiki.gg pages edited after 1.03 give `Physical Attack Up` 4/5/6/10.5/12% and `Improved Guard Counters` 23/25/29%. The guard-counter tier labels are inferred **(unverified)**.
- **Three Physical Attack Up copies multiply** per CLAUDE.md's attack-stacking rule. If the game actually caps duplicates, the Chalice's damage drops from 35.0 to 25.1 (total about 92).
- **Guard counter HP boost:** wiki.gg says +0.045 to +0.065 damage per 1 current HP, by weapon type. The unit is ambiguous, so it's still scored as a guessed 18%.
- **Sustain sizes are mostly guesses.** The only sourced ones are rally's tier bonuses, thrust counter +1, Max HP +10%, Flask +10%, and the negation tiers. Per-fight counts (about 60 blocks and 10 thrust counters) are guesses marked in the script.
- **Rally** is a meta anchor at 50% eHP base (20 / 25 / 27 points). Tiers are scored as highest-only. wiki.gg says +1 and +2 stack with each other **(unverified)**.
- **Night Invader effect:** about +20% damage per CLAUDE.md. Copies are assumed not to stack **(unverified)**.
- **Curse penalties are hand-weighted** and not calibrated to the 0.4-per-1% scale. For example, Reduced Vigor and Arcane is −4, while Vigor +3 scores +2.
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is still a fine swap if you want the stamina.
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed. Other `Taking Damage` curses cost 8 points each, so none made either loadout.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
