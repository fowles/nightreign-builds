# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights at the top of the script). Changes since the 2026-10-30 run:
> - Attack buffs now stack per CLAUDE.md: `Improved Guard Counters`, `Physical Attack Up`, halberd attack power.
> - `Physical Attack Up` tier weights scale with its real values (3/4/5/8.5/10%).
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina effects (max stamina, stamina recovery, Endurance) are worth 0.
>
> Character reference: [characters/guardian.md](../characters/guardian.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Best loadout per vessel:

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Guardian's Chalice | 86.5 | 33.0 | 37.0 | 18.0 | −1.5 |
| Forgotten Guardian's Goblet | 86.0 | 23.0 | 46.0 | 18.0 | −1.0 |
| Guardian's Goblet | 81.0 | 23.0 | 41.0 | 18.0 | −1.0 |
| Soot-Covered Guardian's Urn | 80.5 | 41.0 | 22.0 | 18.0 | −0.5 |
| Decrepit Guardian's Goblet | 80.5 | 43.0 | 18.0 | 22.0 | −2.5 |
| Guardian's Urn | 77.5 | 33.0 | 28.0 | 18.0 | −1.5 |
| Giant's Cradle Grail | 77.0 | 15.0 | 54.5 | 9.0 | −1.5 |
| Scadutree Grail | 74.5 | 33.0 | 28.0 | 18.0 | −4.5 |
| Sealed Guardian's Urn | 73.0 | 18.0 | 36.0 | 22.0 | −3.0 |
| Spirit Shelter Grail | 72.5 | 37.0 | 20.0 | 18.0 | −2.5 |
| Sacred Erdtree Grail | 71.0 | 29.0 | 26.5 | 21.0 | −5.5 |

The score units are the script's weights, not real percentages. They compare across builds only when those builds use the same weight scale.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 86.5:** damage 33.0, sustain 37.0, utility 18.0, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R01914** Grand Luminous Scene | [Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking *(wasted on Guardian)*; HP Recovery From Successful Guarding; Successful guarding fills more of the Art gauge |
| Normal W | **R00817** Grand Luminous Scene (Yellow) | FP Restoration upon Greatsword Attacks *(does nothing with a halberd)*; Flask Also Heals Allies; Ultimate Art Auto Charge +3 |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R01789** Deep Grand Drizzly Scene | FP Restoration upon Dagger Attacks *(does nothing with a halberd)*; Slowly restore HP for self and nearby allies when HP is low; Guard counter is given a boost based on current HP |
| Deep Y | **R00274** Deep Polished Luminous Scene | Improved Guard Counters +1 *(curse: Reduced Strength and Intelligence)*; Partial HP Restoration upon Post-Damage Attacks |

- **Curses: 1.** Reduced Strength and Intelligence: Int is free; the small Strength cost hurts halberd damage a little.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:** Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave. Guard counters carry two stacked boosts (base + +1) plus the HP-based boost, and heal-on-block keeps HP high enough for that boost to stay strong. The Art gauge also charges on its own (Auto Charge +3), so Wings of Salvation comes up often. When it does, it revives allies and heals them over time, and the whirlwind gives allies +12% damage negation. Low-HP regen and Flask Also Heals Allies back up the team.
- **Trade-offs:** No max HP or Continuous HP Recovery, so sustain depends on blocking well. Three relics carry an effect that does nothing for this build.

## Alternative: Forgotten Guardian's Goblet (Normal G B B / Deep R B W), more passive sustain

**Score 86.0:** damage 23.0, sustain 46.0, utility 18.0, penalties −1.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R01182** Grand Tranquil Scene | [Guardian] Successful guards send out shockwaves while ability is active; Improved Throwing Pot Damage *(out of focus)*; Ultimate Art Auto Charge +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R00212** Deep Polished Drizzly Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)* |
| Deep W | **R01867** Deep Grand Tranquil Scene (Green) | [Revenant] Increased Max FP upon Ability Activation *(wasted on Guardian)*; Successful guarding fills more of the Art gauge; Guard counter is given a boost based on current HP |

- **Curses: 2.** Both punish evading, which a guard build rarely does, so they're near-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Trade-offs:** Adds max HP, Continuous HP Recovery, Partial HP Restoration +2, and thrust-counter healing. Drops Witch's Brooch, so there's no ally regen while the Art is active. Only one guard-counter copy, so damage is 10 points lower.

## Assumptions and unknowns

- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) dropped out mostly because of this. It's still a fine swap if you want the stamina.
- **Stacking:** `Improved Guard Counters` copies stack, per CLAUDE.md, and each copy adds its full weight. These per-copy weights (8/10/12) were set when only one copy counted.
- **Partial HP Restoration** tiers are scored as highest-only. wiki.gg says +1 and +2 stack with each other **(unverified)**. Partial HP Restoration heals after you take damage; unknown whether blocked damage counts.
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed. Other `Taking Damage` curses cost 8 points each, so none made either loadout. This rules out several owned `Improved Guard Counters +2` relics (R00703, R00712, R01387).
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
