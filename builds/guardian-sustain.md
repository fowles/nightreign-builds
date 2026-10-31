# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights at the top of the script). Changes since the 2026-10-30 run:
> - Attack buffs now stack per CLAUDE.md: `Improved Guard Counters`, `Physical Attack Up`, halberd attack power.
> - `Physical Attack Up` tier weights scale with its real values (3/4/5/8.5/10%, 0.4 points per %).
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina effects (max stamina, stamina recovery, Endurance) are worth 0.
> - Meta anchors from CLAUDE.md:
>   - `Attack power increased for each Night Invader defeated` is about +20% damage (8 points).
>   - Rally (`Partial HP Restoration upon Post-Damage Attacks`) is non-negotiable (20/22/24 points). Every vessel's top two loadouts carry it.
>
> Character reference: [characters/guardian.md](../characters/guardian.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Best loadout per vessel:

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Guardian's Chalice | 106.5 | 41.0 | 49.0 | 18.0 | −1.5 |
| Forgotten Guardian's Goblet | 98.9 | 30.4 | 55.0 | 18.0 | −4.5 |
| Decrepit Guardian's Goblet | 95.5 | 43.0 | 33.0 | 22.0 | −2.5 |
| Guardian's Urn | 95.0 | 33.0 | 46.0 | 18.0 | −2.0 |
| Scadutree Grail | 94.5 | 41.0 | 49.0 | 9.0 | −4.5 |
| Giant's Cradle Grail | 94.0 | 15.0 | 71.5 | 9.0 | −1.5 |
| Guardian's Goblet | 92.9 | 20.4 | 55.0 | 22.0 | −4.5 |
| Sealed Guardian's Urn | 91.0 | 26.0 | 50.0 | 18.0 | −3.0 |
| Sacred Erdtree Grail | 91.0 | 37.0 | 38.5 | 21.0 | −5.5 |
| Soot-Covered Guardian's Urn | 89.0 | 35.0 | 41.0 | 18.0 | −5.0 |
| Spirit Shelter Grail | 83.5 | 37.0 | 40.0 | 9.0 | −2.5 |

The score units are the script's weights, not real percentages. They compare across builds only when those builds use the same weight scale.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 106.5:** damage 41.0, sustain 49.0, utility 18.0, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R01914** Grand Luminous Scene | [Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking *(wasted on Guardian)*; HP Recovery From Successful Guarding; Successful guarding fills more of the Art gauge |
| Normal W | **R00156** Polished Luminous Scene (Yellow) | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R01789** Deep Grand Drizzly Scene | FP Restoration upon Dagger Attacks *(does nothing with a halberd)*; Slowly restore HP for self and nearby allies when HP is low; Guard counter is given a boost based on current HP |
| Deep Y | **R00274** Deep Polished Luminous Scene | Improved Guard Counters +1 *(curse: Reduced Strength and Intelligence)*; Partial HP Restoration upon Post-Damage Attacks |

- **Curses: 1.** Reduced Strength and Intelligence: Int is free; the small Strength cost hurts halberd damage a little.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Rally recovers damage you take if you hit back right after.
  - Guard counters carry two stacked boosts (base + +1) plus the HP-based boost. Heal-on-block and rally keep HP high enough for that boost to stay strong.
  - Every Night Invader you kill raises attack power for the rest of the run.
  - The Art gauge also charges on its own (Auto Charge +3). Wings of Salvation revives allies and heals them over time, and the whirlwind gives allies +12% damage negation.
- **Trade-offs:** No max HP or Continuous HP Recovery. Rally is only the base tier. Two relics carry an effect that does nothing for this build.
- **Runner-up on the same vessel (104.5):** swap Deep B and Deep Y for **R00212** and **R00548**.
  - **R00212** Deep Polished Drizzly Scene: Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)*.
  - **R00548** Deep Polished Luminous Scene: Critical hits fill more of the Art gauge +1 *(curse: Reduced Dexterity and Faith)*; Improved Guard Counters +1 *(curse: Reduced Flask HP Restoration)*.
  - That gives Rally +2 and thrust-counter healing, but costs 4 curses and the HP-based guard-counter boost.

## Alternative: Forgotten Guardian's Goblet (Normal G B B / Deep R B W), more passive sustain

**Score 98.9:** damage 30.4, sustain 55.0, utility 18.0, penalties −4.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R01182** Grand Tranquil Scene | [Guardian] Successful guards send out shockwaves while ability is active; Improved Throwing Pot Damage *(out of focus)*; Ultimate Art Auto Charge +3 |
| Normal B | **R01208** Grand Drizzly Scene | Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R00306** Deep Polished Drizzly Scene | HP Recovery From Successful Guarding; Physical Attack Up +3 *(curse: All Resistances Down)* |
| Deep W | **R00274** Deep Polished Luminous Scene (Yellow) | Improved Guard Counters +1 *(curse: Reduced Strength and Intelligence)*; Partial HP Restoration upon Post-Damage Attacks |

- **Curses: 2.** All Resistances Down is a real cost. Reduced Strength and Intelligence costs a little Strength.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Trade-offs:**
  - Adds max HP, Continuous HP Recovery, and two stacked Physical Attack Up copies (+2 and +3).
  - **No Night Invader relic.** The Goblet's normal slots can only take your blue and green copies, and those carry little else of use, so they lose their slots.
  - No Witch's Brooch, so there's no ally regen while the Art is active.

## Assumptions and unknowns

- **Night Invader effect:** rated as about +20% damage per CLAUDE.md. It builds up over the run as you kill invaders. Copies are assumed not to stack **(unverified)**.
- **Rally weight** (20/22/24) is twice the next-best healing effect. It's set so that no top loadout can skip it. Tiers are scored as highest-only; wiki.gg says +1 and +2 stack with each other **(unverified)**. Rally heals after you take damage; unknown whether blocked damage counts.
- **Guard counters vs. Night Invader:** under binary focus, `Improved Guard Counters` (8/10/12) rates the same as or higher than the Night Invader effect (8), even though it only boosts counters.
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is still a fine swap if you want the stamina.
- **Stacking:** `Improved Guard Counters` and `Physical Attack Up` copies stack, per CLAUDE.md, at full weight per copy.
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed. Other `Taking Damage` curses cost 8 points each, so none made either loadout.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
