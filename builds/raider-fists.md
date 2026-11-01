# Raider: Fists (Dormant Power Helps Discover Fists)

> Run 2026-11-01 with `scripts/raider_fists.py`. It reuses the scoring engine in `scripts/raider_charged.py` and overrides the coverage, weights and Dormant Power tables at the top of the script. Rules from CLAUDE.md:
> - Attack buffs stack and multiply. Weapon-class buffs each cover only their class's share of damage.
> - **Self-sustain is one effective-HP product:** eHP = (1 + max HP) × (1 + heals ÷ budget) ÷ damage taken.
> - Damage and sustain share one scale: 0.4 points per 1% of total damage or of effective HP.
> - Stamina is worth 0, including the stamina half of the `[Raider]` Retaliate buff.
> - Meta anchors: Night Invader ≈ +20% damage. Rally is non-negotiable, and every vessel's best loadout carries it.
>
> **Hard requirement (your rule):** every loadout carries at least one `Dormant Power Helps Discover Fists`. Any other Dormant Power is scored −8, including heavy classes like Greataxes, because it dilutes the fist pool. Extra Fists copies are neutral; whether they stack is unknown.
>
> **Meta check:** I found no Raider fist guide. Current Raider guides all favor Colossal Weapons. Fists are the fastest weapon class, come in pairs, and equip both hands when two-handed (Mobalytics). This build is off-meta, and every fist-specific size below is a guess.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all | 1.0 | Fists, Retaliate and Totem Stela are all physical |
> | Weapon share: Fist / Greataxe | 0.6 / 0.15 | Guess. The Greataxe is carried until a fist drops. Colossal, Great Hammer and Colossal Sword buffs are 0 |
> | Coverage: skill (Retaliate) / crit / initial light attack | 0.15 / 0.05 / 0.04 | Guess. Retaliate is a punch, but it's a skill: fist buffs are assumed not to apply **(unverified)** |
> | `Improved Fist Attack Power` | +10% on the fist share | Size guessed, like other weapon classes |
> | `Improved Attack Power with 3+ Fists Equipped` | +3% on the fist share | Guess: ~10% × 0.3 chance of holding 3 fists, even with the Dormant Power |
> | `HP Restoration upon Fist Attacks` | 0.3 max-HP bars per fight | Guess: many fast hits × 0.6 coverage |
> | `FP Restoration upon Fist Attacks` | 0.5 points | Hand-weighted. Raider spends little FP |
> | Stance-breaking, two-handing / two armaments | 2 points each | Hand-weighted. Unknown which one paired fists trigger |
> | `[Raider]` Retaliate attack buff | +10% × 0.5 uptime = 5% | Same as the charged build |
> | `[Raider] Hit With Character Skill to Reduce Enemy Attack Power` | 5.2% negation of all damage | −13% × 0.4 uptime (guess) |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | Guess |
> | Fight HP budget | 3.0 max-HP bars | Guess |
> | Ally factor | 0.5 per ally, 2 allies | Guess |
>
> Character reference: [characters/raider.md](../characters/raider.md). Sister build: [raider-charged-sustain.md](raider-charged-sustain.md).

**Goal:** Raider starts on his Greataxe while the Fists Dormant Power steers drops toward fists (Caestus, Spiked Caestus, Star Fist, Iron Ball, Katar). Once one drops, he two-hands it for fast strike chains between Retaliate counters. Every quick hit after taking damage triggers rally.

**Fist relics don't make the cut.** You own 13 relics with fist effects: `Improved Fist Attack Power` ×4, `3+ Fists Equipped` ×2, `HP Restoration upon Fist Attacks` ×4, and `FP Restoration upon Fist Attacks` ×3. Each is worth only about 2–5 points, because it covers just the fist share of damage and its size is guessed. None of them beats the rally, max HP and negation relics for a slot. The fist identity comes from the Dormant Power and the weapon you pick up, not from relic stats. Carrying the Dormant Power costs about **7 points** compared with the same vessel without it (78.5 → 71.5). It takes the deep slot that would hold `Improved Physical Damage Negation +1`.

Best loadout per vessel (all carry rally and a Fists Dormant Power):

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Forgotten Raider's Goblet | 71.5 | 11.0 | 56.5 | 5.0 | −1.0 |
| Raider's Goblet | 70.7 | 16.8 | 54.2 | 5.0 | −5.2 |
| Raider's Chalice | 69.6 | 13.8 | 55.9 | 5.5 | −5.6 |
| Soot-Covered Raider's Urn | 68.3 | 13.8 | 47.6 | 10.0 | −3.0 |
| Raider's Urn | 66.3 | 15.8 | 52.0 | 8.0 | −9.5 |
| Sealed Raider's Urn | 64.4 | 15.8 | 44.7 | 8.5 | −4.5 |
| Scadutree Grail | 64.2 | 8.0 | 56.2 | 0.5 | −0.5 |
| Giant's Cradle Grail | 64.1 | 13.0 | 52.6 | 6.0 | −7.5 |
| Decrepit Raider's Goblet | 61.1 | 19.4 | 38.0 | 11.0 | −7.2 |
| Spirit Shelter Grail | 59.3 | 22.2 | 43.1 | 8.0 | −14.0 |
| Sacred Erdtree Grail | — | | | | |

Sacred Erdtree Grail can't run this build: you own no yellow Fists Dormant Power relic.

Utility (Art gauge, cooldowns), poise, stance-breaking and flat curse penalties are still hand-weighted.

## Best: Forgotten Raider's Goblet (Normal Y B R / Deep R G W)

**Score 71.5:** damage 11.0, sustain 56.5, utility 5.0, penalties −1.0.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal R | **R00783** Grand Burning Scene | [Duchess] Improved Vigor and Strength, Reduced Mind *(wasted on Raider)*; Vigor +3; Strength +3 |
| Deep R | **R01860** Deep Grand Burning Scene | [Raider] Hit With Character Skill to Reduce Enemy Attack Power; Opaline Bubbletear in possession at start of expedition *(scored 0)*; Improved Damage Negation at Low HP |
| Deep G | **R00594** Deep Polished Tranquil Scene | **Dormant Power Helps Discover Fists**; Holy Attack Power Up +3 *(off-focus, 0)* *(curse: Reduced Dexterity and Faith)* |
| Deep W | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |

- **Curses: 2.** Reduced Dexterity and Faith: Faith is D, Dex is C. It's near-free on the Greataxe, but some fists (Caestus, Katar) scale partly on Dex, so it costs a little more here than on the heavy-weapon build. Repeated Evasions Lower Damage Negation: only chained dodges trigger it.
- **Dormant Powers:** one, **Fists** (R00594).
- **`unverified_effect` flags:** none.
- **Rally:** R00162 (+2).
- **Fists Dormant Power swaps:** the Deep G slot is the only green Fists option you own. Swapping R00162 into Deep R and a red Fists relic into Deep W (R00253 grease buff / R00370 Reduced FP Consumption) drops R01860's Retaliate debuff, so it scores lower.
- **Near-ties (within 0.6):** swap R00783 for **R00312** Polished Burning Scene (Taking attacks improves attack power; Vigor +3) or **R01314** Grand Burning Scene (Attack power increased for each evergaol prisoner defeated; Changes compatible armament's skill to Determination at start of expedition; Vigor +3), both 70.9. R00312 fits the theme best: fists keep you in the hits that keep it active.
- **High-damage variant (71.3, 7 curses):** R00156 / R01119 / R01915 + R01287 / R01257 / R00128. It carries the standard-slot Fists Dormant Power (R01119, with Character Skill Cooldown Reduction +3) and three `Physical Attack Up` (+3, +4, +4), for damage 26.5. It brings `Lower Attack When Below Max HP` (bad for Raider) and `Reduced Vigor and Arcane`. Not recommended.

**Loop:** open on the Greataxe and Retaliate through boss strings. Charged punches tag the boss with −13% damage for 13 s. When a fist drops, two-hand it. Its fast chains after each hit taken refill HP through rally +2, and low-HP regen plus low-HP negation cover the stretches where Fighter's Resolve keeps you low. Night Invader kills bank +20% for the rest of the run.

**Trade-offs:** the most survivable fist loadout, but damage is thin: no `Physical Attack Up` and no fist attack power, just Night Invaders. It's nearly the charged-sustain loadout, with physical negation +1 swapped out for the Dormant Power.

## Alternative: Raider's Goblet (Normal R B Y / Deep R B Y), damage-leaning

**Score 70.7:** damage 16.8, sustain 54.2, utility 5.0, penalties −5.2. It trails the best by 0.8 points and carries about 50% more damage, through `Physical Attack Up +4` on the rally relic.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00783** Grand Burning Scene | [Duchess] Improved Vigor and Strength, Reduced Mind *(wasted on Raider)*; Vigor +3; Strength +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R01860** Deep Grand Burning Scene | [Raider] Hit With Character Skill to Reduce Enemy Attack Power; Opaline Bubbletear in possession at start of expedition *(scored 0)*; Improved Damage Negation at Low HP |
| Deep B | **R01158** Deep Grand Drizzly Scene | [Undertaker] Executing Art readies Character Skill *(wasted on Raider)*; FP Restoration upon Flail Attacks *(off-focus, 0)*; **Dormant Power Helps Discover Fists** |
| Deep Y | **R00128** Deep Polished Luminous Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)* |

- **Curses: 2.** Reduced Vigor and Arcane is a real cost: Vigor is A, and it's scored as about −5% max HP inside the eHP product (Arcane is free). Reduced Intelligence and Dexterity is near-free, with a small Dex cost on Dex-scaling fists.
- **Dormant Powers:** one, **Fists** (R01158).
- **`unverified_effect` flags:** none.
- **Rally:** R00128 (+2).
- **Sustain-leaning swap (70.6):** R01915 / R00823 / R00156 + R00162 / R01158 / R00266. That trades `Physical Attack Up +4` for `Improved Physical Damage Negation +2`. R00266 adds Improved Sorceries (off-focus) with the curse Reduced Dexterity and Faith.

**Loop:** the same as the best loadout, with fist chains hitting about 12% harder.

**Trade-offs:** about 5% less max HP from the Vigor curse. It gives up the Forgotten Goblet's spare utility.

## Unknowns

- **Every fist size is a guess:** `Improved Fist Attack Power`, `3+ Fists`, and `HP Restoration upon Fist Attacks` per hit. If fist relics turn out much stronger than other weapon-class buffs, R01600 (Improved Fist Attack Power; Improved Dragon Cult Incantations; Intelligence +2) and R00119 (HP Restoration upon Fist Attacks; Partial HP Restoration upon Post-Damage Attacks) become the first fist relics worth a slot.
- **The fist drop rate:** how often the Dormant Power delivers a fist, and how early. The 0.6 fist share is a guess.
- **Whether multiple Fists Dormant Powers stack.** The search never needed two.
- **Retaliate:** whether fist attack buffs apply to it, since it's a punch. Assumed not.
- **Stance-breaking:** which effect paired fists trigger, two-handing or two armaments.
- **Fist availability for Raider:** whether fists drop with his preferred affinities and Str scaling.
- **Vessel slot colors** come from wiki.gg. Check them against the in-game Relic Rites screen.

## Sources

- https://maxroll.gg/elden-ring-nightreign/characters/raider-character-guide
- https://mobalytics.gg/elden-ring-nightreign/wiki/fists
- https://eldenring.wiki.gg/wiki/Nightreign:Weapons
