# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights, coverage and fight model at the top of the script). Rules from CLAUDE.md:
> - Attack buffs stack and multiply. Negations multiply.
> - Damage and sustain share one scale: 0.4 points per 1% of total damage or of effective HP.
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina is worth 0.
> - Meta anchors: Night Invader ≈ +20% damage; rally is non-negotiable. Every vessel's top two loadouts carry rally.
> - **Post-1.03 sizes from eldenring.wiki.gg:** `Physical Attack Up` 4/5/6/10.5/12%, `Improved Guard Counters` 23/25/29%. These replace aoeah's older values.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all | 1.0 | `Physical Attack Up`, Night Invader, halberd attack power |
> | Damage coverage: guard_counter | 0.35 | guess |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
> | Fight HP budget | 3.0 max-HP bars | guess |
> | Ally factor | 0.5 per ally, 2 allies | guess |
>
> Character reference: [characters/guardian.md](../characters/guardian.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Best loadout per vessel:

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Guardian's Chalice | 94.8 | 31.2 | 53.1 | 18.0 | −7.5 |
| Guardian's Urn | 92.5 | 25.1 | 54.5 | 18.0 | −5.0 |
| Giant's Cradle Grail | 91.4 | 7.0 | 73.9 | 12.0 | −1.5 |
| Sacred Erdtree Grail | 90.4 | 24.0 | 58.5 | 20.0 | −12.0 |
| Guardian's Goblet | 89.6 | 17.5 | 53.1 | 21.0 | −2.0 |
| Sealed Guardian's Urn | 89.0 | 33.5 | 49.4 | 18.0 | −12.0 |
| Decrepit Guardian's Goblet | 88.2 | 25.6 | 47.0 | 18.0 | −2.5 |
| Forgotten Guardian's Goblet | 87.7 | 16.1 | 55.1 | 18.0 | −1.5 |
| Soot-Covered Guardian's Urn | 85.7 | 21.5 | 45.8 | 22.0 | −3.5 |
| Spirit Shelter Grail | 85.2 | 32.5 | 43.1 | 18.0 | −8.5 |
| Scadutree Grail | 83.2 | 23.6 | 52.1 | 9.0 | −1.5 |

Utility (Art gauge, cooldowns) and a few sustain effects (poise, aggro) are still hand-weighted.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 94.8:** damage 31.2, sustain 53.1, utility 18.0, penalties −7.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R01914** Grand Luminous Scene | [Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking *(wasted on Guardian)*; HP Recovery From Successful Guarding *(redundant with R00306)*; Successful guarding fills more of the Art gauge |
| Normal W | **R00156** Polished Luminous Scene (Yellow) | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
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
  - Rally +2 recovers damage you take if you hit back right after.
  - Damage multiplies from Physical Attack Up +3 and +4 (×1.105 × 1.12), Night Invader scaling (≈×1.2 over the run), and a guard-counter boost.
  - The Art gauge charges from blocking and Auto Charge +3. Wings of Salvation revives and heals the team, and the whirlwind gives allies +12% damage negation.
- **Trade-offs:** The strongest damage and sustain together, but carries two real curses. Heal-on-block appears twice, and the second copy adds nothing.
- **Runner-up on the same vessel (94.1):** swap Deep B for **R01386** Deep Grand Drizzly Scene. Its effects are Successful guarding fills more of the Art gauge +1 *(curse: Reduced Strength and Intelligence)*; Physical Attack Up +3 *(curse: Near Death Reduces Max HP)*; Improved Affinity Damage Negation +1 *(curse: Reduced Flask HP Restoration)*. That's 5 curses in total. Not recommended.

## Alternative: Guardian's Urn (Normal R Y Y / Deep R Y Y), fewer curses

**Score 92.5:** damage 25.1, sustain 54.5, utility 18.0, penalties −5.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01908** Grand Burning Scene | [Guardian] Successful guards send out shockwaves while ability is active; Successful guarding fills more of the Art gauge; Endurance +3 *(stamina, worth 0)* |
| Normal Y | **R00901** Grand Luminous Scene | [Guardian] Slowly restores nearby allies' HP while Art is active; Improved Attack Power with 3+ Reapers Equipped *(out of focus; **unverified_effect** flag)*; Partial HP Restoration upon Post-Damage Attacks *(redundant with R00128's +2)* |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep Y | **R00128** Deep Polished Luminous Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)* |
| Deep Y | **R00211** Deep Polished Luminous Scene | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

- **Curses: 2.** Reduced Vigor and Arcane is a real cost. Reduced Intelligence and Dexterity is near-free. There's no All Resistances Down.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** R00901, on `Improved Attack Power with 3+ Reapers Equipped`. That effect is out of focus, so the flag doesn't affect the score's substance.
- **Trade-offs:** Same core loop as the Chalice (shockwaves, Art-on-block, rally +2, heal-on-block, Night Invader, guard counters), with thrust-counter healing added. It gives up Physical Attack Up +3 and the All Resistances Down curse.
- **Curse-light swap (89.8, 1 curse):** replace R00128 with **R01700** Deep Grand Luminous Scene. Its effects are FP Restoration upon Straight Sword Attacks *(does nothing with a halberd)*; Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Rune Acquisition)*; Improved Gravity Sorcery *(out of focus)*. You keep rally +2 and drop the Vigor curse, but lose Physical Attack Up +4.

**Maximum-sustain option:** Giant's Cradle Grail (91.4: damage 7.0, sustain 73.9) is unchanged from the previous run. It has the most healing of any vessel and almost no damage.

## Assumptions and unknowns

- **Post-1.03 sizes:** eldenring.wiki.gg pages edited after 1.03 give `Physical Attack Up` 4/5/6/10.5/12% and `Improved Guard Counters` 23/25/29%. The +3/+4 and guard counter +1/+2 values came from a page summary, not verbatim text. The guard-counter tier labels are inferred **(unverified)**. Patch notes only say these effects were "increased".
- **Guard counter HP boost:** wiki.gg says +0.045 to +0.065 damage per 1 current HP, by weapon type. The unit is ambiguous, so it's still scored as a guessed 18%.
- **Sustain sizes are mostly guesses.** The only sourced ones are rally's tier bonuses, thrust counter +1, Max HP +10%, Flask +10%, and the negation tiers. Per-fight counts (about 60 blocks and 10 thrust counters) are guesses marked in the script.
- **Rally** is a meta anchor at 50% eHP base (20 / 25 / 27 points). Tiers are scored as highest-only; wiki.gg says +1 and +2 stack with each other **(unverified)**.
- **Guard-counter coverage (0.35)** is a guess.
- **Night Invader effect:** about +20% damage per CLAUDE.md. It builds up over the run as you kill invaders. Copies are assumed not to stack **(unverified)**.
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is still a fine swap if you want the stamina.
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed. Other `Taking Damage` curses cost 8 points each, so none made either loadout.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
