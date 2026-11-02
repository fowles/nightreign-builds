# Revenant: Holy (Wrath of Gold)

> Run 2026-11-02 with `python3 -I scripts/revenant_incant.py --build holy --min-focus 3`. Shared rules, sizes and sources: [revenant-incantation.md](revenant-incantation.md).
>
> **Requirements:** a `Wrath of Gold` spell relic, plus at least 3 copies of `Holy Attack Power Up` or `Improved Fundamentalist Incantations`.
>
> **Meta check:** I found no guide for this build. Wrath of Gold's holy damage type comes from base Elden Ring **(unverified in Nightreign)**.

**Workable, but the weakest focus.** It scores 33.9, against 37.8 to 40.6 for the other variants. Fextralife's Fundamentalist list doesn't include Wrath of Gold, and that page says unlisted spells aren't boosted. So the spell gets no +12% school buff, and none of your 14 Fundamentalist relics make the top loadouts. If Wrath of Gold does turn out to get that buff, this build should be rerun.

| Model input | Value | Note |
|---|---|---|
| Damage share: incantations / claws / family | 0.70 / 0.10 / 0.20 | Guess |
| Wrath of Gold's share of casts | 0.60 | Guess |
| Remaining casts that are holy drops | 0.60, half of them Fundamentalist | Guess |
| `Holy Attack Power Up` | +4.5 / 5.5 / 6.5 / 10.5 / 12% | Base to +2 on wiki.gg |
| `Improved Fundamentalist Incantations` | +12%, on Fundamentalist drops only | wiki.gg, Fextralife |
| Rally | 25% of the melee anchor | Guess. Spell triggers **unverified** |
| Incoming mix / HP budget / ally factor | physical 0.6, elements 0.1 each / 3.0 / 0.5 × 2 | Guess |

You own 3 `Wrath of Gold` relics: R01423 (red), R01840 (yellow) and R01880 (green). None are scanner-flagged. You have no blue one, so the Giant's Cradle Grail can't run this build.

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Soot-Covered Revenant's Urn | 33.9 | 18.6 | 8.8 | 9.0 | −2.5 |
| Decrepit Revenant's Goblet | 33.5 | 19.7 | 10.8 | 9.0 | −6.0 |
| Revenant's Chalice | 32.6 | 10.9 | 21.2 | 3.0 | −2.5 |
| Revenant's Urn | 31.5 | 17.1 | 15.4 | 0.0 | −1.0 |
| Sacred Erdtree Grail | 30.8 | 17.1 | 14.2 | 6.0 | −6.5 |
| Forgotten Revenant's Goblet | 29.8 | 10.4 | 21.4 | 3.5 | −5.5 |
| Revenant's Goblet | 28.5 | 6.6 | 25.9 | 3.5 | −7.5 |
| Sealed Revenant's Urn | 27.4 | 5.8 | 25.6 | 0.0 | −4.0 |
| Scadutree Grail | 26.1 | 6.6 | 20.5 | 3.5 | −4.5 |
| Spirit Shelter Grail | 23.8 | 12.4 | 10.0 | 4.4 | −3.0 |

## Best: Soot-Covered Revenant's Urn (Normal R Y Y / Deep R Y Y)

**Score 33.9:** damage 18.6, sustain 8.8, utility 9.0, penalties −2.5. Costs 4 Sovereign Sigils.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01564** Grand Burning Scene | [Revenant] Strengthens family and allies when Ultimate Art is activated; Lightning Pots in possession at start of expedition *(scored 0)*; Holy Attack Power Up +1 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal Y | **R01840** Grand Luminous Scene | [Revenant] Trigger ghostflame explosion during Ultimate Art activation; **Changes compatible armament's incantation to Wrath of Gold at start of expedition**; Improved Blood Loss Resistance *(scored 0)* |
| Deep R | **R01686** Deep Grand Burning Scene | Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Reduced Rune Acquisition)*; Improved Incantations +1 *(curse: Repeated Evasions Lower Damage Negation)*; Improved Godslayer Incantations *(small value on Godslayer drops)* |
| Deep Y | **R00377** Deep Polished Luminous Scene | Holy Attack Power Up +4 *(curse: Reduced Strength and Intelligence)*; Improved Affinity Damage Negation |
| Deep Y | **R00624** Deep Polished Luminous Scene | Improved Flask HP Restoration; Holy Attack Power Up +2 |

- **Curses: 3.** Reduced Rune Acquisition, Repeated Evasions Lower Damage Negation (only chained dodges) and Reduced Strength and Intelligence (near-free).
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R01686 (+1).

## Alternative: Decrepit Revenant's Goblet (Normal R R Y / Deep R R Y)

**Score 33.5:** damage 19.7, sustain 10.8, utility 9.0, penalties −6.0. A little more damage and sustain, but more curses and a flagged effect. Costs 4 Sovereign Sigils. **Its normal slot colors are unverified:** wiki.gg says R R Y, and Fextralife's text says R R G. Check in game.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01564** Grand Burning Scene | [Revenant] Strengthens family and allies when Ultimate Art is activated; Lightning Pots in possession at start of expedition *(scored 0)*; Holy Attack Power Up +1 |
| Normal R | **R01423** Grand Burning Scene | Dormant Power Helps Discover Sacred Seals; Wraith Calling Bell in possession at start of expedition *(scored 0)*; **Changes compatible armament's incantation to Wrath of Gold at start of expedition** |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01686** Deep Grand Burning Scene | Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Reduced Rune Acquisition)*; Improved Incantations +1 *(curse: Repeated Evasions Lower Damage Negation)*; Improved Godslayer Incantations *(small value on Godslayer drops)* |
| Deep R | **R01857** Deep Grand Burning Scene | [Scholar] Improved Endurance and Dexterity, Reduced Intelligence and Arcane *(wasted on Revenant, flagged)*; Slowly restore HP for self and nearby allies when HP is low; Holy Attack Power Up +3 *(curse: Continuous HP Loss)* |
| Deep Y | **R00377** Deep Polished Luminous Scene | Holy Attack Power Up +4 *(curse: Reduced Strength and Intelligence)*; Improved Affinity Damage Negation |

- **Curses: 4.** Continuous HP Loss is the real cost. The other three are as in the best loadout.
- **Dormant Powers:** one, **Sacred Seals** (R01423). It's on-build, so neutral.
- **`unverified_effect` flags:** R01857's `[Scholar]` effect, which is wasted here anyway.
- **Rally:** R01686 (+1).

## Playing it

**Loop:** cast Wrath of Gold from the Finger Seal from the first minute, and use holy seals as they drop, since `Holy Attack Power Up` covers those too. Upgrade the Finger Seal with Smithing Stones. Fire Immortal March for revives or burst.

**Trade-offs:**
- Sustain is the thinnest of the focused builds, at 8.8 on the best loadout. It has no max HP relic, and rally is its main heal.
- Better-sustained option: the Chalice row (32.6, sustain 21.2) gives up Night Invader and most of the damage.
