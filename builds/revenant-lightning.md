# Revenant: Lightning Spear

> Run 2026-11-02 with `python3 -I scripts/revenant_incant.py --build lightning --min-focus 3`. Shared rules, sizes and sources: [revenant-incantation.md](revenant-incantation.md).
>
> **Requirements:** a `Lightning Spear` spell relic, plus at least 3 copies of `Lightning Attack Power Up` or `Improved Dragon Cult Incantations`.
>
> **Meta check:** I found no guide for this build. The lightning damage type comes from base Elden Ring **(unverified in Nightreign)**.

**Goal:** a ranged Lightning Spear from the first minute, on the starting Finger Seal. You own only 3 spell relics, in blue and green, so only 7 of the 11 vessels can carry one.

| Model input | Value | Note |
|---|---|---|
| Damage share: incantations / claws / family | 0.70 / 0.10 / 0.20 | Guess |
| Lightning Spear's share of casts | 0.60 | Guess |
| Remaining casts that are Dragon Cult drops | 0.50 | Guess |
| `Lightning Attack Power Up` | +4.5 / 5.5 / 6.5 / 10.5 / 12% | Base to +2 on wiki.gg |
| `Improved Dragon Cult Incantations` | +12% | wiki.gg, Fextralife |
| Rally | 25% of the melee anchor | Guess. Spell triggers **unverified** |
| Incoming mix / HP budget / ally factor | physical 0.6, elements 0.1 each / 3.0 / 0.5 × 2 | Guess |

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Revenant's Chalice | 39.4 | 13.9 | 19.6 | 11.3 | −5.5 |
| Sealed Revenant's Urn | 38.8 | 13.9 | 20.1 | 9.3 | −4.5 |
| Revenant's Urn | 37.6 | 15.9 | 19.6 | 7.5 | −5.5 |
| Forgotten Revenant's Goblet | 34.1 | 22.9 | 7.2 | 8.5 | −4.5 |
| Revenant's Goblet | 32.7 | 10.7 | 15.9 | 8.1 | −2.0 |
| Giant's Cradle Grail | 30.4 | 15.9 | 14.4 | 1.5 | −1.5 |
| Spirit Shelter Grail | 27.1 | 15.4 | 7.4 | 5.7 | −1.5 |

Soot-Covered Urn, Decrepit Goblet, Scadutree Grail and Sacred Erdtree Grail have no blue or green normal slot, so they can't carry a Lightning Spear relic.

## Best: Revenant's Chalice (Normal B G W / Deep B Y G)

**Score 39.4:** damage 13.9, sustain 19.6, utility 11.3, penalties −5.5. Unlocks through Revenant Remembrance 2.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal G | **R01291** Grand Tranquil Scene | [Duchess] Become difficult to spot and silence footsteps after landing critical from behind *(wasted on Revenant)*; Increased rune acquisition for self and allies; **Changes compatible armament's incantation to Lightning Spear at start of expedition** |
| Normal W | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep B | **R01411** Deep Grand Drizzly Scene | Reduced FP Consumption; Improved Affinity Damage Negation; Lightning Attack Power Up +2 |
| Deep Y | **R01316** Deep Grand Luminous Scene | [Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies *(wasted on Revenant)*; Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Poison Buildup When Below Max HP)*; Lightning Attack Power Up +4 *(curse: Lower Attack When Below Max HP)* |
| Deep G | **R01399** Deep Grand Tranquil Scene | [Revenant] Increased Max FP upon Ability Activation; Improved Madness Resistance +1; Lightning Attack Power Up +2 |

- **Curses: 2,** both on R01316. `Lower Attack When Below Max HP` is the real cost: don't add `Expend own HP` to this loadout, since it would keep you below max.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R01316 (+1).

## Alternative: Revenant's Urn (Normal B B Y / Deep B B Y)

**Score 37.6:** damage 15.9, sustain 19.6, utility 7.5, penalties −5.5. The starter vessel, and it adds a Dragon Cult buff. The Sealed Urn scores 38.8 but costs 4 Sovereign Sigils and has less damage, so the Urn is the more useful comparison.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal B | **R00767** Grand Drizzly Scene | FP Restoration upon Hammer Attacks *(scored 0)*; **Changes compatible armament's incantation to Lightning Spear at start of expedition**; Endurance +1 *(scored 0)* |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep B | **R01411** Deep Grand Drizzly Scene | Reduced FP Consumption; Improved Affinity Damage Negation; Lightning Attack Power Up +2 |
| Deep B | **R00949** Deep Grand Drizzly Scene | [Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies *(wasted on Revenant)*; Improved Dragon Cult Incantations; Fire Attack Power Up +2 *(off-focus, small value on fire drops)* |
| Deep Y | **R01316** Deep Grand Luminous Scene | [Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies *(wasted on Revenant)*; Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Poison Buildup When Below Max HP)*; Lightning Attack Power Up +4 *(curse: Lower Attack When Below Max HP)* |

- **Curses: 2,** both on R01316.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R01316 (+1).

## Playing it

**Loop:** throw Lightning Spear from range from the first minute, using claws to help raise ghosts. Clearing camps builds FP through R01399. Upgrade the Finger Seal with Smithing Stones, and take dropped seals only when they clearly beat it. Fire Immortal March for revives or burst.

**Trade-offs:**
- It's the best-suited focus for staying at range, based on how the spell works in base Elden Ring **(unverified in Nightreign)**.
- Both loadouts rely on R01316, whose `Lower Attack` curse cuts damage whenever you're hurt. Keep HP topped up, and treat damage figures as optimistic if you often fight hurt.
- Highest-damage option: `--build lightning --min-focus 4` reaches damage 24.0 on the Forgotten Revenant's Goblet, at a total of 33.8, with far less sustain.
