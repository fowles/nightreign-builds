# Raider: Charged Heavy Attacks / Sustain

> Run 2026-10-31 with `scripts/raider_charged.py` (weights, coverage and fight model at the top of the script). Rules from CLAUDE.md:
> - Attack buffs stack and multiply. Weapon-class buffs each cover only their class's share of damage.
> - **Self-sustain is one effective-HP product:** eHP = (1 + max HP) × (1 + heals ÷ budget) ÷ damage taken.
> - Damage and sustain share one scale: 0.4 points per 1% of total damage or of effective HP.
> - Stamina is worth 0, including the stamina half of the `[Raider]` Retaliate buff.
> - Meta anchors: Night Invader ≈ +20% damage. Rally is non-negotiable, and every vessel's best loadout carries it.
>
> **No relic boosts charged weapon attacks.** The game has `Improved Charged Sorceries` / `Incantations`, but nothing for charged melee. Searches turned up no such effect, and none exists in the inventory. "Charged" is scored through what feeds charged heavies: `Physical Attack Up`, weapon-class attack power, two-handed stance-breaking, and poise to trade hits while charging. Charged Retaliate (the steaming +50% punch) counts as the `skill` scope.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all | 1.0 | Everything is physical |
> | Weapon share: Greataxe / Colossal Weapon / Great Hammer / Colossal Sword | 0.4 / 0.2 / 0.15 / 0.03 | Guess. The Greataxe is the starting weapon; the others need drops |
> | Coverage: skill (Retaliate) / crit / initial light attack | 0.15 / 0.03 / 0.04 | Guess |
> | `[Raider]` Retaliate attack buff | +10% × 0.5 uptime = 5% | Uptime guessed |
> | `Taking attacks improves attack power` | 5% | Guess: ~10% × 0.5 uptime |
> | `[Raider] Hit With Character Skill to Reduce Enemy Attack Power` | 5.2% negation of all damage | −13% × 0.4 uptime (guess). The ally benefit isn't scored. |
> | Two-handed stance-breaking | 4 points | Hand-weighted |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | Guess |
> | Fight HP budget | 3.0 max-HP bars | Guess |
> | Ally factor | 0.5 per ally, 2 allies | Guess |
>
> Character reference: [characters/raider.md](../characters/raider.md).

**Goal:** a two-handed heavy weapon (starting Greataxe, or a Colossal Weapon or Great Hammer that drops) that lands charged heavy attacks for stagger. It eats hits through Retaliate, then cashes in charged counters, and stays healthy through long Deep of Night fights.

Best loadout per vessel (all carry rally):

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Forgotten Raider's Goblet | 78.5 | 11.0 | 63.0 | 5.5 | −1.0 |
| Raider's Goblet | 76.0 | 8.0 | 64.0 | 5.0 | −1.0 |
| Raider's Chalice | 75.9 | 8.0 | 63.4 | 5.5 | −1.0 |
| Raider's Urn | 74.6 | 15.8 | 59.9 | 8.5 | −9.5 |
| Soot-Covered Raider's Urn | 73.7 | 19.4 | 48.8 | 10.0 | −4.5 |
| Decrepit Raider's Goblet | 71.1 | 20.2 | 58.2 | 7.0 | −14.3 |
| Sealed Raider's Urn | 70.6 | 21.4 | 45.8 | 8.5 | −5.1 |
| Scadutree Grail | 69.3 | 11.0 | 58.3 | 0.5 | −0.5 |
| Spirit Shelter Grail | 68.0 | 22.2 | 50.2 | 8.5 | −13.0 |
| Giant's Cradle Grail | 67.8 | 30.4 | 42.4 | 5.0 | −10.0 |
| Sacred Erdtree Grail | 65.7 | 22.4 | 43.8 | 7.0 | −7.5 |

The Soot-Covered Urn row shows the 3-curse variant presented below. A 4-curse variant ties it at 73.7 (damage 26.5) by swapping in a third `Physical Attack Up +4`.

Utility (Art gauge, cooldowns), poise, stance-breaking and flat curse penalties are still hand-weighted.

## Best: Forgotten Raider's Goblet (Normal Y B R / Deep R G W)

**Score 78.5:** damage 11.0, sustain 63.0, utility 5.5, penalties −1.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal R | **R00783** Grand Burning Scene | [Duchess] Improved Vigor and Strength, Reduced Mind *(wasted on Raider)*; Vigor +3; Strength +3 |
| Deep R | **R01860** Deep Grand Burning Scene | [Raider] Hit With Character Skill to Reduce Enemy Attack Power; Opaline Bubbletear in possession at start of expedition *(scored 0)*; Improved Damage Negation at Low HP |
| Deep G | **R00236** Deep Polished Tranquil Scene | Items confer effect to all nearby allies; Improved Physical Damage Negation +1 *(curse: Reduced Intelligence and Dexterity)* |
| Deep W | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |

- **Curses: 2, both near-free.** Reduced Intelligence and Dexterity: Int is D, Dex is C. Repeated Evasions Lower Damage Negation: only chained dodges trigger it, and Raider tanks more than he rolls.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R00162 (+2).
- Near-ties (within 0.6): swap R00783 for **R00312** Polished Burning Scene (Taking attacks improves attack power; Vigor +3) or **R01314** Grand Burning Scene (evergaol attack power; Determination skill swap; Vigor +3). R00312 is the more on-theme pick: it gives up Strength +3 for a conditional attack buff that Raider's tanking keeps active.

**Loop:** open on a charged heavy, or hold Retaliate through the boss's string so the next one comes out charged (the deep relic then cuts that enemy's damage 13% for 13 s). Every hit landed after taking damage pays back through rally +2, and the low-HP regen and negation cover the stretches where Fighter's Resolve keeps you at low HP. Night Invader kills bank the +20% for the rest of the run.

**Trade-offs:** this is the sustain end of the build. It carries only 11 damage points and no `Physical Attack Up`, so charged heavies hit at base strength plus Night Invaders. Totem Stela gets Auto Charge +3 but no duration extension.

## Alternative: Soot-Covered Raider's Urn (Normal B B G / Deep B B G), damage-leaning

**Score 73.7:** damage 19.4, sustain 48.8, utility 10.0, penalties −4.5. That is 4.8 points behind on total but about 75% more damage: three `Physical Attack Up` copies (+4, +4, +3 multiply to ≈ +29% on a two-handed Greataxe), Night Invader, and more Retaliate uptime.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal B | **R01299** Grand Drizzly Scene | [Raider] Duration of Ultimate Art extended; Attack power increased for each Night Invader defeated; Vigor +2 |
| Normal G | **R00890** Grand Tranquil Scene | HP Restoration upon Greataxe Attacks; Character Skill Cooldown Reduction +3; Ultimate Art Auto Charge +2 |
| Deep B | **R01437** Deep Grand Drizzly Scene | Increased rune acquisition for self and allies *(scored 0)*; Physical Attack Up +3 *(curse: Reduced Dexterity and Faith)*; Improved Death Blight Resistance *(scored 0)* |
| Deep B | **R00698** Deep Polished Drizzly Scene | [Raider] Hit With Character Skill to Reduce Enemy Attack Power; Improved Incantations *(off-focus, 0)* |
| Deep G | **R00531** Deep Polished Tranquil Scene | Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Reduced Strength and Intelligence)*; Physical Attack Up +4 *(curse: Reduced Dexterity and Faith)* |

- **Curses: 3.** Reduced Dexterity and Faith appears **twice** (duplicate stated; both stats are near-free). Reduced Strength and Intelligence is a real cost on a Str S character (scored −2.5).
- **Dormant Powers:** none. An equal-score swap of R00698 for **R01266** (Raider deep tag; Dormant Power Helps Discover Greataxes; Magic Attack Power Up +2) adds an on-build Greataxe Dormant Power, which is neutral.
- **`unverified_effect` flags:** none.
- **Rally:** R00531 (+1).
- **Max-damage variant (also 73.7, 4 curses):** swap R00698 for **R00545** Deep Polished Drizzly Scene (Opaline Hardtear at start; Physical Attack Up +4 *(curse: Reduced Damage Negation for Flask Usages)*). Damage rises to 26.5, but it drops the Retaliate debuff and adds a flask-timing curse.

**Loop:** the same Retaliate → charged counter rhythm, with Character Skill Cooldown Reduction +3 for more of it. Greataxe hits heal a little on top of rally. Totem Stela runs 30 s with Auto Charge +2, so allies get +15% physical more often.

**Trade-offs:** it commits to Greataxes: `HP Restoration upon Greataxe Attacks` is wasted if you switch to a Colossal Weapon. It gives up rally +2 for +1 and loses the physical negation and low-HP negation from the top pick.

## Unknowns

- Every effect size marked "guess" in the script, especially the uptimes of the `[Raider]` attack buff and the Retaliate debuff. Raising either moves the tagged relics up.
- Whether a big HP drop (Fighter's Resolve, post-1.03.2) stacks with `Taking attacks improves attack power`. Its exact numbers are **unverified**.
- Retaliate's cooldown isn't published, so Cooldown Reduction is hand-weighted.
- Vessel slot colors come from wiki.gg. Check them against the in-game Relic Rites screen.
