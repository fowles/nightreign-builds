# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights at the top of the script). Changes since the 2026-10-30 run:
> - Attack buffs now stack per CLAUDE.md: `Improved Guard Counters`, `Physical Attack Up`, halberd attack power.
> - `Physical Attack Up` tier weights now scale with its real values (3/4/5/8.5/10%).
>
> Character reference: [characters/guardian.md](../characters/guardian.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Scores across all 11 eligible vessels: Chalice 88.5, Forgotten Goblet 88.5, Decrepit Goblet 83.5, Soot-Covered Urn 82.5, Goblet 81.9, Urn 81.0, Sealed Urn 78.5, Scadutree 78.0, Giant's Cradle 77.0, Spirit Shelter 76.0, Sacred Erdtree 71.0.

The top two tie. The Chalice is listed first because it keeps `HP Recovery From Successful Guarding`, which drives the whole loop, and it carries only one curse.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R01914** Grand Luminous Scene | [Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking *(wasted on Guardian)*; HP Recovery From Successful Guarding; Successful guarding fills more of the Art gauge |
| Normal W | **R00855** Night of the Champion (Green) | Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R00986** Deep Grand Drizzly Scene | [Wylder] Character Skill inflicts Blood Loss *(wasted)*; Critical Hit Boosts Stamina Recovery Speed +1; Improved Guard Counters |
| Deep Y | **R00274** Deep Polished Luminous Scene | Improved Guard Counters +1 *(curse: Reduced Strength and Intelligence)*; Partial HP Restoration upon Post-Damage Attacks |

- **Curses: 1.** Reduced Strength and Intelligence: Int is free; the small Strength cost hurts halberd damage a little.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Equal-score swap for Deep B:** **R01393** Deep Grand Drizzly Scene (Ironjar Aromatic in possession at start of expedition; Improved Guard Counters; Improved Glintblade Sorcery *(out of focus)*).
- **Loop:** Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave. Guard counters carry three stacked boosts (base, base, +1) plus the HP-based boost, and heal-on-block keeps HP high enough for that boost to stay strong. Thrusting counters heal too, and Partial HP Restoration recovers damage you take if you attack right after. Wings of Salvation revives and heals allies over time; the whirlwind gives allies +12% damage negation.
- **Trade-offs:** No max HP, Continuous HP Recovery, or Ultimate Art Auto Charge. Sustain depends on blocking well. Two relics are mostly there to carry one guard-counter copy each.

## Alternative: Forgotten Guardian's Goblet (Normal G B B / Deep R B W), more passive sustain

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R00855** Night of the Champion | Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack |
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R01176** Deep Grand Burning Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |
| Deep B | **R01318** Deep Grand Drizzly Scene | Successful guarding fills more of the Art gauge; Improved Frenzied Flame Incantations *(out of focus)*; Improved Affinity Damage Negation +1 *(curse: Reduced Dexterity and Faith)* |
| Deep W | **R00274** Deep Polished Luminous Scene (Yellow) | Improved Guard Counters +1 *(curse: Reduced Strength and Intelligence)*; Partial HP Restoration upon Post-Damage Attacks |

- **Curses: 2.** Reduced Dexterity and Faith is near-free. Reduced Strength and Intelligence costs a little Strength.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Trade-offs:** Adds max HP, Continuous HP Recovery, low-HP regen, and affinity negation. But it has **no `HP Recovery From Successful Guarding`**, and only two guard-counter copies.

**Previous best (2026-10-30), now 87.9.** It's the same Goblet with the same Normal slots (R00855, R01922, R00823); only the Deep slots differ. It is still a strong option if you'd rather have heal-on-block plus Fathom's passive regen than a second guard-counter copy.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Deep R | **R00437** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Faith and Strength)*; Successful guarding fills more of the Art gauge |
| Deep B | **R00306** Deep Polished Drizzly Scene | HP Recovery From Successful Guarding; Physical Attack Up +3 *(curse: All Resistances Down)* |
| Deep W | **R01176** Deep Grand Burning Scene (Red) | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Max HP Up with 3+ Medium Shields Equipped *(does nothing with a greatshield)*; Improved Guard Counters |

Curses: 2 (Reduced Faith and Strength, All Resistances Down). Dormant Powers: none.

## Assumptions and unknowns

- **Stacking:** `Improved Guard Counters` copies stack, per CLAUDE.md, and each copy adds its full weight. These per-copy weights (8/10/12) were set when only one copy counted. If guard counters now look too dominant, lower them.
- **Partial HP Restoration** tiers are scored as highest-only. wiki.gg says +1 and +2 stack with each other **(unverified)**. Partial HP Restoration heals after you take damage; unknown whether blocked damage counts.
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed. Other `Taking Damage` curses cost 8 points each, so none made either loadout. This rules out several owned `Improved Guard Counters +2` relics (R00703, R00712, R01387).
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
