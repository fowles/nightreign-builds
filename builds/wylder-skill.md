# Wylder: Skill Use (Earring + both Wills)

> Run 2026-11-02 with `scripts/wylder_skill.py`. It reuses the scoring engine in `scripts/raider_charged.py` and overrides the coverage, weights, curse, Dormant Power and vessel tables at the top of the script. Rules from CLAUDE.md:
> - Attack buffs stack and multiply. Narrow buffs cover only their share of damage.
> - **Self-sustain is one effective-HP product:** eHP = (1 + max HP) × (1 + heals ÷ budget) ÷ damage taken.
> - Damage and sustain share one scale: 0.4 points per 1% of total damage or of effective HP.
> - Stamina is worth 0, including the Earring's `Stamina Recovery upon Landing Attacks`.
> - Meta anchor: rally is non-negotiable for melee. Every loadout below carries it.
>
> **Hard requirement (your rule):** the normal slots hold R01921 The Wylder's Earring, R00926 The Will of Balance and R00805 The Will of the Balancers.
>
> **"Skill use" as I read it:** both Claw Shot and weapon skills. Claw Shot does "miniscule" direct damage (wiki.gg), so `Improved Skill Attack Power` only pays off if weapon skills do the damage. Claw Shot's value here is its charges and its bleed.
>
> **Meta check:** I found no guide for this combination. wiki.gg says Will of the Balancers won't stack with a second copy of itself, but "will still function alongside The Will of Balance". So your pair works, and the two copies are scored as stacking.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all | 1.0 | Treated as physical. Elemental weapon skills depend on drops |
> | Coverage: weapon skills | 0.4 | Guess, and the key input. Tested at 0.2 and 0.6 |
> | Coverage: greatsword normal attacks | 0.25 | Guess |
> | Coverage: Art fire burn / crits / initial light attack | 0.05 / 0.03 / 0.03 | Guess. Burn damage is unpublished |
> | `Improved Skill Attack Power` | +15% on the skill share, 2 copies | wiki.gg. Whether it covers Claw Shot is **(unverified)**; assumed not |
> | `Improved Melee Attack Power` | +5% on all damage, 2 copies | wiki.gg. Whether it covers weapon skills is **(unverified)**; assumed yes |
> | `[Wylder] Character Skill inflicts Blood Loss` | +15% damage, highest copy only | Guess. 60 + 55 buildup per Claw Shot (wiki.gg). Tested at 0 and 8 |
> | `Physical Attack Up` | 4 / 5 / 6 / 10.5 / 12% | wiki.gg, post-1.03 |
> | `Improved Greatsword Attack Power` | +9% on the greatsword share | wiki.gg |
> | Rally base / +1 / +2 | 1.5 / 1.875 / 2.025 max-HP bars | CLAUDE.md anchor. Assumes weapon skills proc it **(unverified)** |
> | `Increased Maximum HP` | +10% | Guess |
> | `Reduced Vigor and Arcane` | −5% max HP inside the eHP product | Guess |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | Guess |
> | Fight HP budget | 3.0 max-HP bars | Guess |
> | Ally factor | 0.5 per ally, 2 allies | Guess |
>
> Utility (FP, Art gauge, Claw Shot charge), poise and flat curse penalties are hand-weighted. FP effects count as in focus because weapon skills run on FP. Character reference: [characters/wylder.md](../characters/wylder.md).

## What the base set forces

**Only two vessels can hold it.** The base set is Red, Red, Blue, so the normal slots must be R R B in some order. That leaves Wylder's Urn and Sealed Wylder's Urn. Wylder's Chalice (R Y W) is one slot short: its yellow slot can't take a Red or Blue relic.

**No other standard relic fits.** Everything standard-only is out, including these:

- `Attack power increased for each Night Invader defeated`, about +20% damage, the biggest loss
- `Character Skill Cooldown Reduction`, so Claw Shot stays at its base cooldown
- `Ultimate Art Auto Charge`
- `[Wylder] Standard attacks enhanced with fiery follow-ups`
- `Vigor`, `Strength` and `Dexterity` bonuses

**Your Wills are the only owned source of skill attack power.** You own exactly these two `Improved Skill Attack Power` effects. On a 0.4 skill share, the base set gives +24.5% total damage: 1.05² for melee × (0.6 + 0.4 × 1.15²) for skill.

Best loadout per eligible vessel (exhaustive: 8.5M and 10.1M deep triples):

| Vessel | Total | Damage | Sustain | Utility | Penalties | Curses |
|---|---|---|---|---|---|---|
| Sealed Wylder's Urn | 67.0 | 40.4 | 36.9 | 6.5 | −16.8 | 6 |
| Wylder's Urn | 60.0 | 20.7 | 36.3 | 6.5 | −3.5 | 2 |

Sealed Urn's lead comes from its yellow deep slots: R00128 and R00292 each pair a key effect (rally, Blood Loss) with `Physical Attack Up +4`.

## Best: Sealed Wylder's Urn (Normal B R R / Deep G Y Y)

**Score 67.0:** damage 40.4, sustain 36.9, utility 6.5, penalties −16.8. About +101% damage and +92% eHP before penalties.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00805** The Will of the Balancers | Improved Melee Attack Power; Improved Skill Attack Power; Continuous FP Recovery |
| Normal R | **R01921** The Wylder's Earring | [Wylder] +1 additional Character Skill use; [Wylder] Art activation spreads fire in area; Stamina Recovery upon Landing Attacks *(worth 0)* |
| Normal R | **R00926** The Will of Balance | Improved Melee Attack Power; Improved Skill Attack Power; Occasionally Nullify Attacks When Damage Negation is Lowered *(scored 0, see Unknowns)* |
| Deep G | **R01257** Deep Grand Tranquil Scene | Physical Attack Up +4 *(curse: Lower Attack When Below Max HP)*; Increased Maximum HP *(curse: Reduced Rune Acquisition)*; Improved Affinity Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |
| Deep Y | **R00128** Deep Polished Luminous Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)* |
| Deep Y | **R00292** Deep Polished Luminous Scene | [Wylder] Character Skill inflicts Blood Loss; Physical Attack Up +4 *(curse: Near Death Reduces Max HP)* |

- **Curses: 6, no repeats.** All three of his main stats take a hit: Strength, Dexterity and Vigor. `Lower Attack When Below Max HP` is the most dangerous: rally builds spend a lot of time below max HP, and its size is unknown (scored −5). `Near Death Reduces Max HP` scores −3. Intelligence and Arcane are near-free.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R00128 (+2).
- **FP support:** only 1 FP per 5 s from R00805. Expect to run short on FP, since Wylder's Mind is only C.

**Loop:** Claw Shot in to apply bleed and close the gap, and keep the second charge for a reposition or a second bleed tick. Spend FP on weapon skills during openings, since each hit gets both Wills and all three `Physical Attack Up`. Land hits right after taking damage to trigger rally +2. Fire Onslaught Stake for i-frames and stagger; its burn feeds the Art gauge back.

**Trade-offs:** the highest score with this base set, but it pays with six curses and thin FP. Any hit that leaves you below max HP also lowers your attack, until rally or a flask tops you back up.

### Lower-curse swap on the same vessel (my pick to try first)

Same base set and vessel. It drops `Lower Attack When Below Max HP` and adds `Reduced FP Consumption`. Scored 61.6 with **2 curses**: damage 28.0, sustain 27.0, utility 11.5, penalties −4.9.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Deep G | **R00924** Deep Grand Tranquil Scene | Defeating enemies fills more of the Art gauge; Reduced FP Consumption; Improved Rot Resistance *(off-focus, 0)* |
| Deep Y | **R00128** Deep Polished Luminous Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)* |
| Deep Y | **R00952** Deep Grand Luminous Scene | [Wylder] Character Skill inflicts Blood Loss; Attack power up when facing scarlet rot-afflicted enemy *(no rot source, 0)*; Physical Attack Up +2 |

Using **R00292** in place of R00952 adds `Near Death Reduces Max HP` as a third curse and raises the score to 62.5, with damage 31.8.

It trails the best loadout by 5.4: it gives up 12.4 damage and 9.9 sustain, for 5.0 more hand-weighted utility and 11.9 fewer points of guessed penalties. If `Lower Attack When Below Max HP` is severe or FP runs out quickly, this one wins in play.

## Alternative: Wylder's Urn (Normal R R B / Deep R R B), starter vessel

**Score 60.0:** damage 20.7, sustain 36.3, utility 6.5, penalties −3.5. About half the damage bonus of the best loadout, but a cleaner curse list.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01921** The Wylder's Earring | [Wylder] +1 additional Character Skill use; [Wylder] Art activation spreads fire in area; Stamina Recovery upon Landing Attacks *(worth 0)* |
| Normal R | **R00926** The Will of Balance | Improved Melee Attack Power; Improved Skill Attack Power; Occasionally Nullify Attacks When Damage Negation is Lowered *(scored 0, see Unknowns)* |
| Normal B | **R00805** The Will of the Balancers | Improved Melee Attack Power; Improved Skill Attack Power; Continuous FP Recovery |
| Deep R | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |
| Deep R | **R00851** Deep Grand Burning Scene | [Revenant] Increased Max FP upon Ability Activation *(wasted on Wylder)*; Increased Maximum HP *(curse: Near Death Reduces Max HP)*; Physical Attack Up +2 |
| Deep B | **R01453** Deep Grand Drizzly Scene | [Wylder] Character Skill inflicts Blood Loss; Magic Damage Negation Up; Improved Poison Resistance *(off-focus, 0)* |

- **Curses: 2.** `Repeated Evasions Lower Damage Negation` only triggers on chained dodges. It may also be what enables the Will of Balance's nullify effect **(unverified)**. `Near Death Reduces Max HP` scores −3.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** R00162 (+2).
- **Exact tie (60.0):** R01757 (Blood Loss; Lightning Damage Negation Up; Improved Blood Loss Resistance) can replace R01453.

**Loop:** the same as the best loadout, with weapon skills hitting noticeably softer.

**Trade-offs:** no stat curses at all, and Vigor, Strength and Dexterity stay whole. It has only one `Physical Attack Up`, at +2. It's the safer choice if you don't want curses, but the 2-curse Sealed Urn swap scores higher.

## Sensitivity

Sealed Urn stays on top in every run. Its three deep relics stay the same in all but one.

| Change | Sealed Urn | Wylder's Urn | What changes |
|---|---|---|---|
| Default | 67.0 | 60.0 | |
| Weapon-skill share 0.2 | 62.4 | 56.5 | Same relics |
| Weapon-skill share 0.6 | 71.6 | 63.5 | Same relics |
| Blood Loss +8% | 62.1 | 56.3 | Same relics |
| Blood Loss +0% | 57.9 | 56.3 | Blood Loss drops out: Sealed takes R00185, Urn takes R00449 |

## Unknowns

- **Scope of `Improved Skill Attack Power`:** wiki.gg doesn't say whether it covers Claw Shot. A 1.03.2 change added it to Executor's Cursed Sword arts specifically, which suggests character skills aren't included by default. Worth testing in play by comparing Claw Shot damage with and without the Wills.
- **`Occasionally Nullify Attacks When Damage Negation is Lowered`:** wiki.gg gives only the name, with no trigger or rate. It's scored 0. If it reacts to negation-lowering curses, Repeated Evasions (R00162) or `Reduced Damage Negation for Flask Usages` could enable it. The best loadout carries neither.
- **The Blood Loss size:** +15% is a guess from how often 115 buildup per Claw Shot might proc on a boss. Boss bleed resistance in Deep of Night isn't sourced.
- **Curse sizes:** `Lower Attack When Below Max HP`, `Near Death Reduces Max HP` and all stat curses are unmeasured.
- **Weapon skills and rally:** whether a weapon skill hit counts as a post-damage attack is assumed, not confirmed.
- **Claw Shot cooldown:** 10 s on wiki.gg, 8 s on Fextralife. `+1 additional Character Skill use` stores charges, but doesn't change how fast they come back.
- **Vessel slot colors** come from wiki.gg, cross-checked with Fextralife. Check them against the in-game Relic Rites screen.

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:The_Will_of_Balance
- https://eldenring.wiki.gg/wiki/Nightreign:The_Will_of_the_Balancers
- https://eldenring.wiki.gg/wiki/Nightreign:Wylder
- https://eldenring.wiki.gg/wiki/Nightreign:Relics
