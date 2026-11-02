# Revenant: Fire Incantations

> Run 2026-11-02 with `python3 -I scripts/revenant_incant.py --build {dragonfire,oflame} --min-focus 3`. Shared rules, sizes and sources: [revenant-incantation.md](revenant-incantation.md).
>
> **Requirements:** the matching spell relic, plus at least 3 copies of `Fire Attack Power Up` or the spell's school buff.
>
> **Meta check:** I found no guide for this build. The fire damage type comes from base Elden Ring **(unverified in Nightreign)**.

**Goal:** a spell relic puts a fire spell on the starting Finger Seal, so you have it from the first minute. wiki.gg says it changes the *secondary* incantation slot and only works on Revenant's initial Finger Seal.

**Which spell:** Dragonfire scores a little higher, at 39.5 with no curses against 38.2 with 2 curses for O, Flame!. You own more O, Flame! relics (6 against 3), so it fits more vessels. Only one spell relic fits the slot, so a loadout with both takes a penalty.

| Model input | Dragonfire | O, Flame! | Note |
|---|---|---|---|
| Damage share: incantations / claws / family | 0.70 / 0.10 / 0.20 | same | Guess |
| Converted spell's share of casts | 0.60 | 0.60 | Guess |
| Remaining casts that are fire drops | 0.70 | 0.70 | Guess: split evenly across 4 fire schools |
| School buff | Improved Dragon Communion Incantations +12% | Improved Giants' Flame Incantations +12% | wiki.gg, Fextralife |
| Rally | 25% of the melee anchor | same | Guess. Spell triggers **unverified** |
| Incoming mix / HP budget / ally factor | physical 0.6, elements 0.1 each / 3.0 / 0.5 × 2 | same | Guess |

## Best: Dragonfire on Revenant's Urn (Normal B B Y / Deep B B Y)

**Score 39.5:** damage 14.6, sustain 18.8, utility 6.0, penalties 0.0. This is the starter vessel.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal B | **R00797** Grand Drizzly Scene | [Scholar] Continuous damage inflicted on targets threaded by Ultimate Art *(wasted on Revenant)*; Partial HP Restoration upon Post-Damage Attacks; **Changes compatible armament's incantation to Dragonfire at start of expedition** |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep B | **R00546** Deep Polished Drizzly Scene | Improved Damage Negation at Low HP; Improved Dragon Communion Incantations |
| Deep B | **R00242** Deep Polished Drizzly Scene | Improved Dragon Communion Incantations; Fire Damage Negation Up |
| Deep Y | **R01288** Deep Grand Luminous Scene | FP Restoration upon Halberd Attacks *(scored 0)*; Crimsonspill Crystal Tear in possession at start of expedition *(scored 0)*; Fire Attack Power Up +2 |

- **Curses: 0.**
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R00797 (base).
- **FP gap:** it has no FP effects at all. Expect to run dry first.

## Alternative: Dragonfire on Revenant's Chalice (Normal B G W / Deep B Y G)

**Score 37.8:** damage 18.6, sustain 6.1, utility 14.0, penalties −1.0. More damage and FP, far less sustain. Unlocks through Revenant Remembrance 2.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00797** Grand Drizzly Scene | [Scholar] Continuous damage inflicted on targets threaded by Ultimate Art *(wasted on Revenant)*; Partial HP Restoration upon Post-Damage Attacks; **Changes compatible armament's incantation to Dragonfire at start of expedition** |
| Normal G | **R00837** Grand Tranquil Scene | Improved Dragon Communion Incantations; Mind +2; Faith +3 |
| Normal W | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep B | **R00546** Deep Polished Drizzly Scene | Improved Damage Negation at Low HP; Improved Dragon Communion Incantations |
| Deep Y | **R00475** Deep Polished Luminous Scene | [Revenant] Increased Max FP upon Ability Activation; Defeating enemies fills more of the Art gauge |
| Deep G | **R01312** Deep Grand Tranquil Scene | Arcane increased for each great enemy defeated at a Ruin *(scored 0)*; Fire Attack Power Up +4 *(curse: Repeated Evasions Lower Damage Negation)*; Improved Sleep Resistance |

- **Curses: 1.** Repeated Evasions Lower Damage Negation only affects chained dodges.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R00797 (base).

## O, Flame! on Decrepit Revenant's Goblet (Normal R R Y / Deep R R Y)

**Score 38.2:** damage 15.3, sustain 11.0, utility 13.9, penalties −2.0. Costs 4 Sovereign Sigils. **Its normal slot colors are unverified:** wiki.gg says R R Y, and Fextralife's text says R R G. Check in game.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01022** Grand Burning Scene | [Revenant] Expend own HP to fully heal nearby allies when activating Art; Max FP increased for each Sorcerer's Rise unlocked; Fire Attack Power Up +1 |
| Normal R | **R00873** Grand Burning Scene | Improved Attack Power with 3+ Axes Equipped *(scored 0)*; Partial HP Restoration upon Post-Damage Attacks; **Changes compatible armament's incantation to O, Flame! at start of expedition** |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01263** Deep Grand Burning Scene | Max stamina increased for each great enemy defeated at a Great Encampment *(scored 0)*; Improved Giants' Flame Incantations; Improved Physical Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |
| Deep R | **R01250** Deep Grand Burning Scene | HP Restoration upon Spear Attacks *(scored 0)*; Improved Gravity Sorcery *(scored 0)*; Fire Attack Power Up +4 *(curse: Rot Buildup When Below Max HP)* |
| Deep Y | **R00475** Deep Polished Luminous Scene | [Revenant] Increased Max FP upon Ability Activation; Defeating enemies fills more of the Art gauge |

- **Curses: 2.** Reduced Strength and Intelligence is near-free. Rot Buildup When Below Max HP matters more here, because `Expend own HP` halves your HP on every Art.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R00873 (base).

## O, Flame! alternative: Sealed Revenant's Urn (Normal Y B B / Deep G G R)

**Score 36.3:** damage 19.0, sustain 14.8, utility 6.0, penalties −3.5. Two `Fire Attack Power Up +4` make this the hardest-hitting O, Flame! loadout. Costs 4 Sovereign Sigils.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal B | **R00350** Polished Drizzly Scene | **Changes compatible armament's incantation to O, Flame! at start of expedition**; Faith +2 |
| Deep G | **R01312** Deep Grand Tranquil Scene | Arcane increased for each great enemy defeated at a Ruin *(scored 0)*; Fire Attack Power Up +4 *(curse: Repeated Evasions Lower Damage Negation)*; Improved Sleep Resistance |
| Deep G | **R00309** Deep Polished Tranquil Scene | Fire Attack Power Up +4 *(curse: Near Death Reduces Max HP)*; Improved Death Blight Resistance |
| Deep R | **R01263** Deep Grand Burning Scene | Max stamina increased for each great enemy defeated at a Great Encampment *(scored 0)*; Improved Giants' Flame Incantations; Improved Physical Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |

- **Curses: 3.** Repeated Evasions Lower Damage Negation, Near Death Reduces Max HP and Reduced Strength and Intelligence (near-free).
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** none. It's only worth 25% of the melee anchor on a caster, but you'll feel the loss if you lean on claws.

## Playing it

**Loop:** open with the converted spell on the Finger Seal rather than hunting for a seal first. Keep the seal upgraded with Smithing Stones, and take dropped fire seals only when they clearly beat it, because the spell stays on the Finger Seal. Fire Immortal March for revives or burst.

**Trade-offs:**
- Some enemies will resist fire, and the scoring doesn't account for enemy weaknesses. wiki.gg says the spell choice depends on the target's weakness.
- The school buffs only pay out on that school. `Fire Attack Power Up` also covers fire seals from other schools.
- Highest-damage options: `--build dragonfire --min-focus 4` reaches damage 21.4 on Revenant's Chalice, at a total of 33.9.
