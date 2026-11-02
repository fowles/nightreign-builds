# Revenant: Incantation Caster (general)

> Run 2026-11-02 with `python3 -I scripts/revenant_incant.py --build general`. Specialized variants: [revenant-fire.md](revenant-fire.md), [revenant-lightning.md](revenant-lightning.md), [revenant-beast-claw.md](revenant-beast-claw.md), [revenant-holy.md](revenant-holy.md). Character reference: [characters/revenant.md](../characters/revenant.md).
>
> **Meta check:** I found no current Deep of Night guide for a Revenant caster and no guide using the incantation-changing relics. General guides agree on HP, FP, damage negation and whichever incantation type you run. Every size marked as a guess below comes from me, not a source.

**Goal:** stay at range and cast Faith incantations from whatever seals the run drops, with a family member out. Save Immortal March for revives and boss burst.

## Can your relics support a focus?

**Yes, all four, including holy.** The limit is the spell relic and its colors, not the number of buffs.

| Focus | Spell relics owned | Element buff relics | School buff relics | Verdict |
|---|---|---|---|---|
| Fire | O, Flame! ×6, Dragonfire ×3 | Fire Attack Power Up ×69 | Giants' Flame ×8, Dragon Communion ×10, Godslayer ×14, Frenzied Flame ×14 | Deepest. Two spell options |
| Lightning | Lightning Spear ×3 (blue, green only) | Lightning Attack Power Up ×63 | Dragon Cult ×8 | Enough, but fewest vessels fit |
| Beast Claw | Beast Claw ×6, **all scanner-flagged** | Physical Attack Up ×117 | Bestial ×8 | Enough. Check the flagged effect in game first |
| Holy | Wrath of Gold ×3 | Holy Attack Power Up ×74 | Fundamentalist ×14 | Workable but weakest: the school buff doesn't cover Wrath of Gold |

Generic `Improved Incantations` adds 48 relics, all deep. It boosts every spell.

**What specializing costs.** Each variant must carry its spell relic and at least 3 element or school buffs. Scores drop because those slots no longer hold sustain or FP effects. The general build gets no credit for skipping a spell relic's main benefit, though: a damaging spell from the first minute. So treat this gap as an upper bound.

| Build | No focus minimum | With 3+ focus buffs | Best focused vessel |
|---|---|---|---|
| General | 48.1 | n/a | Revenant's Chalice |
| Dragonfire | 43.5 | 39.5 | Revenant's Urn |
| Lightning Spear | 43.0 | 39.4 | Revenant's Chalice |
| O, Flame! | 43.5 | 38.2 | Decrepit Revenant's Goblet |
| Beast Claw | 43.1 | 40.6 (5 curses), 37.8 (1 curse) | Revenant's Urn, Decrepit Revenant's Goblet |
| Wrath of Gold | 42.6 | 33.9 | Soot-Covered Revenant's Urn |

## Model

| Input | Value | Note |
|---|---|---|
| Damage share: incantations / claws / family | 0.70 / 0.10 / 0.20 | Guess. Player attack buffs are assumed not to reach family **(unverified)** |
| Spell mix: holy, no school / Fundamentalist | 0.25 / 0.15 | Guess, includes Rejection |
| Spell mix: Giants' Flame / Dragon Communion / Godslayer / Frenzied Flame | 0.12 / 0.12 / 0.08 / 0.05 | Guess |
| Spell mix: Dragon Cult / Bestial | 0.15 / 0.08 | Guess |
| `Improved Incantations` base, +1, +2 | +6 / +8 / +10% | Base from one French guide (Millenium, seen only in a search summary), +1 and +2 guessed |
| School effects (`Improved Bestial Incantations`, etc.) | +12% | wiki.gg, Fextralife |
| Fire, Holy, Lightning `Attack Power Up` | +4.5 / 5.5 / 6.5 / 10.5 / 12% | Same table as the Ironeye builds. Base to +2 confirmed on wiki.gg |
| FP binding | +1% FP = +0.4% incantation damage | Guess. Reported under utility |
| Rally | 25% of the melee anchor | Guess: claw hits only. Whether spells trigger it is **unverified** |
| `[Revenant] Strengthens family and allies` | Family +25% × 0.25 uptime, plus 3 utility points for allies | Hand-weighted |
| `[Revenant] Power up while fighting alongside family` | +10% × 0.8 uptime | Assumes Frederick |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | Guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 per ally, 2 allies | Guess |

Damage is scored per source, as in the Ironeye builds, because a single fire spell takes its school, fire and incantation buffs together. Utility, poise and curse penalties are still hand-weighted. Spell damage types come from base Elden Ring; the Nightreign pages I could read don't state them **(unverified)**.

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Revenant's Chalice | 48.1 | 11.8 | 23.2 | 15.1 | −2.0 |
| Decrepit Revenant's Goblet (search best, with R01915) | 47.0 | 13.1 | 23.7 | 12.7 | −2.5 |
| Sealed Revenant's Urn | 46.5 | 6.9 | 31.6 | 9.5 | −1.5 |
| Revenant's Urn | 46.4 | 12.4 | 25.8 | 12.2 | −4.0 |
| Soot-Covered Revenant's Urn | 42.6 | 9.8 | 18.2 | 15.2 | −0.5 |
| Forgotten Revenant's Goblet | 41.2 | 12.2 | 24.3 | 6.7 | −2.0 |
| Giant's Cradle Grail | 40.7 | 12.9 | 28.8 | 3.0 | −4.0 |
| Revenant's Goblet | 39.5 | 13.3 | 23.7 | 4.9 | −2.5 |
| Scadutree Grail | 38.6 | 13.1 | 24.3 | 3.7 | −2.5 |
| Sacred Erdtree Grail | 37.4 | 6.4 | 16.8 | 14.2 | 0.0 |
| Spirit Shelter Grail | 34.0 | 9.1 | 13.1 | 13.2 | −1.5 |

## Best: Revenant's Chalice (Normal B G W / Deep B Y G)

**Score 48.1:** damage 11.8, sustain 23.2, utility 15.1, penalties −2.0. Unlocks through Revenant Remembrance 2.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal G | **R00938** Grand Tranquil Scene | [Revenant] Strengthens family and allies when Ultimate Art is activated; FP Restoration upon Whip Attacks *(scored 0)*; Vigor +3 |
| Normal W | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep B | **R00139** Deep Polished Drizzly Scene | Improved Incantations +1 *(curse: Reduced Strength and Intelligence)*; Improved Flask HP Restoration |
| Deep Y | **R00475** Deep Polished Luminous Scene | [Revenant] Increased Max FP upon Ability Activation; Defeating enemies fills more of the Art gauge |
| Deep G | **R00454** Deep Polished Tranquil Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Poison Buildup When Below Max HP)*; Improved Incantations |

- **Curses: 2.** Reduced Strength and Intelligence is near-free on a Faith caster. Poison Buildup When Below Max HP is a real but small cost at range.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R00454 (+2).

## Alternative: Decrepit Revenant's Goblet (Normal R R Y / Deep R R Y)

**Score 45.2:** damage 13.6, sustain 18.4, utility 15.7, penalties −2.5. It ranks below the Sealed Urn and Revenant's Urn on score, but it keeps the Art buff for allies and family without relying on low-HP effects. Costs 4 Sovereign Sigils. **Its normal slot colors are unverified:** wiki.gg says R R Y, and Fextralife's text says R R G. Check in game.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00813** Night of the Fathom | Increased Maximum HP; Flask Also Heals Allies; Items confer effect to all nearby allies |
| Normal R | **R00120** Polished Burning Scene | [Revenant] Strengthens family and allies when Ultimate Art is activated; Vigor +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01686** Deep Grand Burning Scene | Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Reduced Rune Acquisition)*; Improved Incantations +1 *(curse: Repeated Evasions Lower Damage Negation)*; Improved Godslayer Incantations |
| Deep R | **R00368** Deep Polished Burning Scene | Improved Incantations +2 *(curse: Reduced Strength and Intelligence)*; Improved Poise & Damage Negation When Knocked Back by Damage |
| Deep Y | **R00475** Deep Polished Luminous Scene | [Revenant] Increased Max FP upon Ability Activation; Defeating enemies fills more of the Art gauge |

- **Curses: 3.** Reduced Rune Acquisition, Repeated Evasions Lower Damage Negation (only chained dodges) and Reduced Strength and Intelligence (near-free).
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R01686 (+1).
- **Hand swap:** the search's top pick for this slot is R01915 (Slowly restore HP for self and nearby allies when HP is low; Improved Damage Negation at Low HP; Vigor +3), at 47.0. You chose R00120 instead: R01915 leans on low-HP effects, while R00120 keeps the Vigor and adds the +25% Art buff for allies and family. So the script's output won't match this table for this slot.

## Playing it

**Loop:** summon a family member and hang back. Cast from the best seal you find, using claws when you run out of FP or need to tag enemies for ghosts. Each raised ghost adds max FP through R00475, so clearing camps early pays off by the boss. Night Invader kills add up to about +20% damage. Fire Immortal March for revives or big burst windows.

**Trade-offs:**
- It's the safest and steadiest of the five builds, but its damage depends on what seals drop. It carries no spell relic, so until you find a better seal you only have what the Finger Seal starts with.
- Rally is the biggest unknown. If spells trigger it, its value quadruples (`--rally 1`) and the general top score jumps to 72.7. The search then drops every `Improved Incantations` copy for sustain, which turns this into a different build. Test it in game by casting at an enemy right after taking a hit.

## Sources
- https://eldenring.wiki.gg/wiki/Nightreign:Revenant
- https://eldenring.wiki.gg/wiki/Nightreign:Finger_Seal
- https://eldenring.wiki.gg/wiki/Nightreign:Relics
- https://eldenringnightreign.wiki.fextralife.com/Improved_Sorceries_or_Incantations
- https://www.millenium.org/guide/425411.html
