# Revenant: Beast Claw

> Run 2026-11-02 with `python3 -I scripts/revenant_incant.py --build beast --min-focus 3`. Shared rules, sizes and sources: [revenant-incantation.md](revenant-incantation.md).
>
> **Requirements:** a `Beast Claw` spell relic, plus at least 3 copies of `Physical Attack Up` or `Improved Bestial Incantations`.
>
> **Meta check:** I found no guide for this build. The physical damage type comes from base Elden Ring **(unverified in Nightreign)**.

**Check this first:** **all 6 of your Beast Claw spell relics carry the scanner's `unverified_effect` flag on that exact effect** (R00493, R01080, R01143, R01222, R01762, R01883). Confirm the text on the relic in game before building around it. The O, Flame! and Lightning Spear relics aren't flagged.

**Goal:** Beast Claw from the first minute, on the starting Finger Seal. `Physical Attack Up` also boosts her claws, so this is the one spell focus where the element buff covers both weapons.

| Model input | Value | Note |
|---|---|---|
| Damage share: incantations / claws / family | 0.70 / 0.10 / 0.20 | Guess |
| Beast Claw's share of casts | 0.60 | Guess |
| Remaining casts that are Bestial drops | 0.30 | Guess: Bestial seals are rarer |
| `Physical Attack Up` | +4 / 5 / 6 / 10.5 / 12% | wiki.gg, post-1.03 |
| `Improved Bestial Incantations` | +12% | wiki.gg, Fextralife |
| Rally | 25% of the melee anchor | Guess. Spell triggers **unverified** |
| Incoming mix / HP budget / ally factor | physical 0.6, elements 0.1 each / 3.0 / 0.5 × 2 | Guess |

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Revenant's Urn | 40.6 | 18.9 | 18.8 | 15.3 | −12.4 |
| Revenant's Chalice | 39.4 | 25.4 | 13.7 | 13.0 | −12.7 |
| Decrepit Revenant's Goblet | 37.8 | 13.4 | 17.7 | 9.2 | −2.5 |
| Soot-Covered Revenant's Urn | 37.7 | 15.5 | 19.3 | 9.3 | −6.5 |
| Sealed Revenant's Urn | 36.9 | 14.6 | 19.3 | 9.0 | −6.0 |
| Forgotten Revenant's Goblet | 35.8 | 16.5 | 11.4 | 14.0 | −6.1 |
| Revenant's Goblet | 35.3 | 17.2 | 19.7 | 7.4 | −9.0 |
| Scadutree Grail | 34.9 | 17.4 | 10.9 | 9.5 | −3.0 |
| Spirit Shelter Grail | 33.4 | 18.7 | 13.7 | 8.6 | −7.5 |
| Sacred Erdtree Grail | 32.3 | 15.5 | 8.2 | 12.3 | −3.8 |
| Giant's Cradle Grail | 29.9 | 6.9 | 20.8 | 5.7 | −3.5 |

## Best by score: Revenant's Urn (Normal B B Y / Deep B B Y)

**Score 40.6:** damage 18.9, sustain 18.8, utility 15.3, penalties −12.4. The starter vessel.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal B | **R01883** Grand Drizzly Scene | [Revenant] Strengthens family and allies when Ultimate Art is activated; **Changes compatible armament's incantation to Beast Claw at start of expedition** *(flagged)*; Endurance +3 *(scored 0)* |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep B | **R00125** Deep Polished Drizzly Scene | [Revenant] Increased Max FP upon Ability Activation; Physical Attack Up +4 *(curse: Taking Damage Causes Poison Buildup)* |
| Deep B | **R00353** Deep Polished Drizzly Scene | Physical Attack Up +4 *(curse: Taking Damage Causes Rot Buildup)*; Increased Maximum FP *(curse: Near Death Reduces Max HP)* |
| Deep Y | **R00128** Deep Polished Luminous Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)* |

- **Curses: 5.** Taking Damage Causes Poison Buildup and Rot Buildup are the real risks, since Beast Claw's short range pulls you closer **(unverified in Nightreign)**. Near Death Reduces Max HP and Reduced Vigor and Arcane also cost HP on a character with only 780. Reduced Intelligence and Dexterity is near-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** R01883's Beast Claw effect.
- **Rally:** R00128 (+2).

## Alternative, and my pick: Decrepit Revenant's Goblet (Normal R R Y / Deep R R Y)

**Score 37.8:** damage 13.4, sustain 17.7, utility 9.2, penalties −2.5. It gives up 2.8 points and 5.5 damage for one curse instead of five. Costs 4 Sovereign Sigils. **Its normal slot colors are unverified:** wiki.gg says R R Y, and Fextralife's text says R R G. Check in game.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01915** Grand Burning Scene | Slowly restore HP for self and nearby allies when HP is low; Improved Damage Negation at Low HP; Vigor +3 |
| Normal R | **R01080** Grand Burning Scene | HP restored when using medicinal boluses, etc.; **Changes compatible armament's incantation to Beast Claw at start of expedition** *(flagged)*; Improved Blood Loss Resistance |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R00249** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks; Physical Attack Up +2 |
| Deep R | **R00851** Deep Grand Burning Scene | [Revenant] Increased Max FP upon Ability Activation; Increased Maximum HP *(curse: Near Death Reduces Max HP)*; Physical Attack Up +2 |
| Deep Y | **R01227** Deep Grand Luminous Scene | [Wylder] Character Skill inflicts Blood Loss *(wasted on Revenant)*; Improved Bestial Incantations; Improved Death Blight Resistance |

- **Curses: 1.** Near Death Reduces Max HP.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** R01080's Beast Claw effect.
- **Rally:** R00249 (base).

## Playing it

**Loop:** cast Beast Claw from mid range and mix in claw hits, which share the `Physical Attack Up` buffs. Claw hits should trigger rally even if spells don't, so mixing them in keeps it working. Upgrade the Finger Seal with Smithing Stones. Fire Immortal March for revives or burst.

**Trade-offs:**
- It plays closer than the fire and lightning builds, based on how the spell works in base Elden Ring **(unverified in Nightreign)**. Her 780 HP makes that risky.
- The scoring doesn't account for enemy weaknesses or resistances.
- Highest-damage option: the Chalice row above reaches damage 25.4 with 4 `Physical Attack Up` and a Bestial buff (`--min-focus 4`). Its penalties are about the same as the Urn's.
