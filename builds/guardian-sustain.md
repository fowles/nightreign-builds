# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights and coverage at the top of the script). Changes since the 2026-10-30 run:
> - Attack buffs stack per CLAUDE.md.
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina is worth 0.
> - Meta anchors: Night Invader ≈ +20% damage; rally is non-negotiable. Every vessel's top two loadouts carry rally.
> - **Damage effects use per-build coverage** at 0.4 points per 1% of total damage. Coverage for this build:
>
>   | Scope | Coverage | Effects using it |
>   |---|---|---|
>   | all | 1.0 | `Physical Attack Up`, Night Invader, `Improved Halberd Attack Power` |
>   | guard_counter | 0.35 *(guess)* | `Improved Guard Counters`, the HP-based guard counter boost |
>
> Character reference: [characters/guardian.md](../characters/guardian.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Best loadout per vessel:

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Giant's Cradle Grail | 94.0 | 7.0 | 76.5 | 12.0 | −1.5 |
| Guardian's Chalice | 92.5 | 17.5 | 63.0 | 20.0 | −8.0 |
| Guardian's Goblet | 89.4 | 16.4 | 57.0 | 21.0 | −5.0 |
| Forgotten Guardian's Goblet | 89.0 | 9.0 | 60.0 | 21.0 | −1.0 |
| Sealed Guardian's Urn | 88.5 | 12.0 | 65.0 | 18.0 | −6.5 |
| Guardian's Urn | 87.0 | 8.0 | 63.5 | 18.0 | −2.5 |
| Sacred Erdtree Grail | 84.0 | 21.0 | 55.0 | 20.0 | −12.0 |
| Soot-Covered Guardian's Urn | 82.5 | 19.0 | 52.5 | 18.0 | −7.0 |
| Decrepit Guardian's Goblet | 82.0 | 13.5 | 53.0 | 18.0 | −2.5 |
| Scadutree Grail | 78.5 | 20.0 | 51.0 | 9.0 | −1.5 |
| Spirit Shelter Grail | 76.0 | 23.0 | 37.0 | 18.0 | −2.0 |

The score units are the script's weights. Damage points are tied to real percentages (0.4 per 1% of total damage); sustain and utility points are still hand-set and are **not** on an equivalent scale. That is why pure-sustain loadouts now lead.

## Best by score: Giant's Cradle Grail (Normal B B B / Deep B B B)

**Score 94.0:** damage 7.0, sustain 76.5, utility 12.0, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Deep B | **R00212** Deep Polished Drizzly Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)* |
| Deep B | **R01318** Deep Grand Drizzly Scene | Successful guarding fills more of the Art gauge; Improved Frenzied Flame Incantations *(out of focus)*; Improved Affinity Damage Negation +1 *(curse: Reduced Dexterity and Faith)* |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 |

- **Curses: 3.** Two punish evading, which a guard build rarely does. Reduced Dexterity and Faith is near-free. All three are close to free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Block everything. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Rally +2 and thrust-counter heals recover what gets through.
  - Max HP, Continuous HP Recovery, and low-HP regen cover the rest.
  - Wings of Salvation and the whirlwind protect the team, and allies share flask heals.
- **Trade-offs:** **Almost no damage.** It has no attack buffs, no guard-counter buffs, and no Night Invader relic. Your own blue Night Invader relics lose out to sustain relics at these weights. This is the most survivable loadout, but fights will be long.

## Alternative: Guardian's Chalice (Normal B Y W / Deep R B Y), balanced

**Score 92.5:** damage 17.5, sustain 63.0, utility 20.0, penalties −8.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R01914** Grand Luminous Scene | [Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking *(wasted on Guardian)*; HP Recovery From Successful Guarding; Successful guarding fills more of the Art gauge |
| Normal W | **R00156** Polished Luminous Scene (Yellow) | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01025** Deep Grand Burning Scene | [Ironeye] Improved Arcane, Reduced Dexterity *(wasted on Guardian)*; Improved Guard Counters; Improved Affinity Damage Negation |
| Deep B | **R00212** Deep Polished Drizzly Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)* |
| Deep Y | **R01527** Deep Grand Luminous Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Successful guarding fills more of the Art gauge +1 *(curse: Rot Buildup When Below Max HP)*; Increased Maximum HP *(curse: All Resistances Down)* |

- **Curses: 4.**
  - The two evasion curses are near-free.
  - **Rot Buildup When Below Max HP** and **All Resistances Down** are real costs, and they compound: lower resistances make the rot bar fill faster.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Same block-heal-charge loop as above, with rally +2.
  - Adds the Night Invader attack scaling over the run, a guard-counter boost, and a faster Art gauge (Auto Charge +3 plus guard-charging +1).
- **Trade-offs:** Has real damage, unlike the Cradle, but costs two real curses and has no Continuous HP Recovery.
- **Equal-score swap for Deep R:** **R00857** Deep Grand Burning Scene (Improved Flask HP Restoration; Improved Death Blight Resistance +1; Poise +3) instead of R01025. You trade the guard-counter boost and affinity negation for flask healing and poise.

## Assumptions and unknowns

- **Sustain vs. damage scale:** damage points now follow real percentages, but sustain weights are still hand-set. The sustain-heavy ranking above partly reflects that mismatch, not only real value.
- **Coverage guesses:** guard counters assumed to be 0.35 of total damage. The base `Improved Guard Counters` tier (18%) and the HP-based guard counter boost (18% at full HP) are also guesses **(unverified)**. Only +1/+2 (22/26%) come from a source (aoeah).
- **Night Invader effect:** about +20% damage per CLAUDE.md. It builds up over the run as you kill invaders. Copies are assumed not to stack **(unverified)**.
- **Rally weight** (20/22/24) is set so that no top loadout can skip it. Tiers are scored as highest-only; wiki.gg says +1 and +2 stack with each other **(unverified)**. Rally heals after you take damage; unknown whether blocked damage counts.
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is still a fine swap if you want the stamina.
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed. Other `Taking Damage` curses cost 8 points each, so none made either loadout.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
