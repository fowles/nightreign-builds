# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights, coverage and fight model at the top of the script). Changes since the 2026-10-30 run:
> - Attack buffs stack per CLAUDE.md.
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina is worth 0.
> - Meta anchors: Night Invader ≈ +20% damage; rally is non-negotiable. Every vessel's top two loadouts carry rally.
> - **Damage and sustain share one scale: 0.4 points per 1%** of total damage or of effective HP.
> - **Damage buffs and negations combine multiplicatively** (two +10% = +21%).
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
| Guardian's Chalice | 93.5 | 16.0 | 56.5 | 22.5 | −1.5 |
| Giant's Cradle Grail | 91.4 | 7.0 | 73.9 | 12.0 | −1.5 |
| Guardian's Urn | 90.6 | 23.1 | 54.5 | 18.0 | −5.0 |
| Sacred Erdtree Grail | 88.9 | 22.4 | 58.5 | 20.0 | −12.0 |
| Guardian's Goblet | 88.2 | 16.1 | 53.1 | 21.0 | −2.0 |
| Sealed Guardian's Urn | 88.1 | 18.0 | 50.1 | 22.0 | −2.0 |
| Decrepit Guardian's Goblet | 87.1 | 24.6 | 47.0 | 18.0 | −2.5 |
| Forgotten Guardian's Goblet | 86.4 | 14.8 | 55.1 | 18.0 | −1.5 |
| Soot-Covered Guardian's Urn | 83.8 | 18.0 | 45.7 | 22.0 | −2.0 |
| Spirit Shelter Grail | 83.5 | 24.6 | 42.8 | 18.0 | −2.0 |
| Scadutree Grail | 81.2 | 21.6 | 52.1 | 9.0 | −1.5 |

Utility (Art gauge, cooldowns) and a few sustain effects (poise, aggro) are still hand-weighted.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 93.5:** damage 16.0, sustain 56.5, utility 22.5, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R00788** Grand Tranquil Scene (Green) | [Guardian] Creates whirlwind when charging halberd attacks; Partial HP Restoration upon Post-Damage Attacks *(redundant: the +2 on R00437 wins)*; Character Skill Cooldown Reduction +2 |
| Deep R | **R00437** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Faith and Strength)*; Successful guarding fills more of the Art gauge |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 |
| Deep Y | **R00211** Deep Polished Luminous Scene | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

- **Curses: 1.** Reduced Faith and Strength: Faith is free; the small Strength cost hurts halberd damage a little.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Rally +2 recovers damage you take if you hit back right after, and thrust counters heal too.
  - Whirlwind (cooldown −2) keeps +12% damage negation on allies.
  - Every Night Invader you kill raises attack power for the rest of the run.
  - The Art gauge charges from three sources: blocking, kills, and Auto Charge +3. Wings of Salvation revives and heals the team.
- **Trade-offs:**
  - **No guard-counter buffs at all.** At 0.35 coverage, guard-counter relics lose their slots to sustain and Art relics.
  - No max HP or Continuous HP Recovery.
  - Base rally on R00788 adds nothing.

## Alternative: Giant's Cradle Grail (Normal B B B / Deep B B B), maximum sustain

**Score 91.4:** damage 7.0, sustain 73.9, utility 12.0, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00115** Polished Drizzly Scene | HP Recovery From Successful Guarding; Flask Also Heals Allies |
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep B | **R00212** Deep Polished Drizzly Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Damage Negation After Evading)*; HP Restoration upon Thrusting Counterattack +1 *(curse: Repeated Evasions Lower Damage Negation)* |
| Deep B | **R01318** Deep Grand Drizzly Scene | Successful guarding fills more of the Art gauge; Improved Frenzied Flame Incantations *(out of focus)*; Improved Affinity Damage Negation +1 *(curse: Reduced Dexterity and Faith)* |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 |

- **Curses: 3.** Two punish evading, which a guard build rarely does. Reduced Dexterity and Faith is near-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Trade-offs:**
  - The most healing of any loadout: heal-on-block, rally +2, thrust heals, max HP, Continuous HP Recovery, low-HP regen, and team flask heals.
  - **Almost no damage:** shockwaves only, with no attack buffs and no Night Invader relic.

## Assumptions and unknowns

- **Sustain sizes are mostly guesses.** Sourced values (aoeah, Deep relics):
  - Rally +1/+2 heal 25%/35% more per hit.
  - Thrust counter +1 restores 3.3% max HP per counter.
  - Max HP +10%; Flask HP +10%.
  - Physical negation 10.5/12%; affinity 6/10.5/12%; element 15/16%.

  Everything else, including per-fight counts (about 60 blocks and 10 thrust counters), is a marked guess in the script.
- **Rally** is a meta anchor at 50% eHP base (20 / 25 / 27 points), set so that no top loadout can skip it. Tiers are scored as highest-only; wiki.gg says +1 and +2 stack with each other **(unverified)**.
- **Guard-counter coverage (0.35)** is a guess. Raising it would bring guard-counter relics back into the Chalice.
- **Night Invader effect:** about +20% damage per CLAUDE.md. It builds up over the run as you kill invaders. Copies are assumed not to stack **(unverified)**.
- **Stamina is unweighted** (CLAUDE.md). Night of the Champion (R00855: Increased Maximum Stamina; Guard counter is given a boost based on current HP; HP Restoration upon Thrusting Counterattack) is still a fine swap if you want the stamina.
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed. Other `Taking Damage` curses cost 8 points each, so none made either loadout.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
