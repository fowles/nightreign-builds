# Guardian: Sustain / Guard Counter / Art Regen

> Re-run 2026-10-31 with `scripts/guardian_sustain.py` (weights, coverage and fight model at the top of the script). Rules from CLAUDE.md:
> - Attack buffs stack and multiply.
> - **Self-sustain is one effective-HP product:** eHP = (1 + max HP) × (1 + heals ÷ budget) ÷ damage taken.
> - Damage and sustain share one scale: 0.4 points per 1% of total damage or of effective HP.
> - Scores are split into damage / sustain / utility / penalties.
> - Stamina is worth 0.
> - Meta anchors: Night Invader ≈ +20% damage. Rally is non-negotiable, and the script flags any loadout without it; every vessel's top loadouts carry it.
> - Post-1.03 sizes from eldenring.wiki.gg: `Physical Attack Up` 4/5/6/10.5/12%, `Improved Guard Counters` 23/25/29%.
>
> **Changes in this run:**
> - **Search fix:** normal- and deep-slot triples were shortlisted by their own score. That credits base rally in full even when the other side carries a better copy (rally doesn't stack), so the shortlist filled with rally triples and dropped strong rally-less ones. The biggest casualty was **R00823** Dark Night of the Fathom in the Chalice's white slot. The script now shortlists triples with and without rally separately. The Chalice rose from 104.1 (3 curses) to **109.4 (1 near-free curse)**.
> - **`Reduced Damage Negation After Evading` is very bad (−8).** It used to be −0.5. Guardian still dodges outside Steel Guard, and a mistimed dodge then costs extra damage. `Repeated Evasions Lower Damage Negation` stays near-free (−0.5). This knocked out R00212 (rally +2 / thrust heal +1), which carries both curses.
> - **Earlier this session: multiplicative sustain.** Max HP, heals and negation multiply. Rally is a heal of 1.5 / 1.875 / 2.025 max-HP bars per fight. Reduced Vigor and Arcane lowers max HP by 5% (guess) inside the product.
>
> | Model input | Value | Note |
> |---|---|---|
> | Damage coverage: all / guard_counter / skill / crit | 1.0 / 0.35 / 0.05 / 0.03 | all but "all" are guesses |
> | Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
> | Fight HP budget | 3.0 max-HP bars | guess |
> | Ally factor | 0.5 per ally, 2 allies | guess. Team effects add on top of the self product. |
>
> Character reference: [characters/guardian.md](../characters/guardian.md). Low-curse variants: [guardian-guard-tank.md](guardian-guard-tank.md).

**Goal:** halberd + greatshield tank. Stay healthy through long Deep of Night fights, hit hard with guard counters, and keep Wings of Salvation (Ultimate Art) coming back often.

Best loadout per vessel (all carry rally):

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Guardian's Chalice | 109.4 | 15.0 | 74.9 | 21.0 | −1.5 |
| Forgotten Guardian's Goblet | 101.9 | 16.5 | 74.9 | 12.0 | −1.5 |
| Guardian's Urn | 99.8 | 17.9 | 69.4 | 20.0 | −7.5 |
| Guardian's Goblet | 99.2 | 34.1 | 67.6 | 11.0 | −13.5 |
| Sealed Guardian's Urn | 97.4 | 20.2 | 64.7 | 21.0 | −8.5 |
| Sacred Erdtree Grail | 95.2 | 29.7 | 56.0 | 22.0 | −12.5 |
| Soot-Covered Guardian's Urn | 95.0 | 20.8 | 63.3 | 18.0 | −7.0 |
| Giant's Cradle Grail | 94.9 | 7.0 | 79.4 | 12.0 | −3.5 |
| Decrepit Guardian's Goblet | 94.8 | 28.7 | 60.1 | 18.0 | −12.0 |
| Spirit Shelter Grail | 91.3 | 32.5 | 49.2 | 18.0 | −8.5 |
| Scadutree Grail | 90.1 | 16.6 | 66.0 | 9.0 | −1.5 |

Utility (Art gauge, cooldowns), poise, aggro and flat curse penalties are still hand-weighted.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y)

**Score 109.4:** damage 15.0, sustain 74.9, utility 21.0, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R00823** Dark Night of the Fathom (Blue) | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R00437** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Faith and Strength)*; Successful guarding fills more of the Art gauge |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |
| Deep Y | **R00211** Deep Polished Luminous Scene | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

- **Curses: 1.** Reduced Faith and Strength: Faith is unused, and Strength is a minor cost on a halberd (scored −1.5).
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Loop:**
  - Steel Guard through combos. Each block heals, charges the Art gauge, and sends out a shockwave.
  - Rally +2 and thrust-counter healing turn every counter into healing. Dark Night of the Fathom adds +10% max HP, continuous regen and a low-HP regen on top.
  - Damage comes from Night Invader scaling (≈×1.2 over the run) and shockwaves. It has no Physical Attack Up and no Improved Guard Counters.
  - The Art gauge charges from blocking, kills and Auto Charge +3. Wings of Salvation revives and heals the team, and the whirlwind gives allies +12% damage negation.
- **Trade-offs:**
  - Low damage (15.0) for a lot of sustain (74.9), with almost no curse cost.
  - **Near-tie (108.7, 2 near-free curses):** swap R00437 for **R00162** Deep Polished Burning Scene (Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church.) and R01755 for **R01318** Deep Grand Drizzly Scene (Successful guarding fills more of the Art gauge; Improved Frenzied Flame Incantations *(out of focus)*; Improved Affinity Damage Negation +1 *(curse: Reduced Dexterity and Faith)*). That trades the team negation for affinity negation and Great Church max HP.
  - **Damage near-tie (108.7, 4 curses):** R00162 deep R plus **R01386** Deep Grand Drizzly Scene (Successful guarding fills more of the Art gauge +1 *(curse: Reduced Strength and Intelligence)*; Physical Attack Up +3 *(curse: Near Death Reduces Max HP)*; Improved Affinity Damage Negation +1 *(curse: Reduced Flask HP Restoration)*) in deep B. Damage 20.0, but it carries two real curses (Near Death Reduces Max HP, Reduced Flask HP Restoration).

## Alternative: Forgotten Guardian's Goblet (Normal G B B / Deep R B W)

**Score 101.9:** damage 16.5, sustain 74.9, utility 12.0, penalties −1.5.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R01101** Grand Tranquil Scene | Improved Frenzied Flame Incantations *(out of focus)*; Attack power increased for each Night Invader defeated; Strength +2 |
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R00437** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Faith and Strength)*; Successful guarding fills more of the Art gauge |
| Deep B | **R01755** Deep Grand Drizzly Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies; Defeating enemies fills more of the Art gauge; Improved Sleep Resistance +1 *(status resistance, scored 0)* |
| Deep W | **R00211** Deep Polished Luminous Scene (Yellow) | HP Recovery From Successful Guarding; HP Restoration upon Thrusting Counterattack |

- **Curses: 1**, the same near-free Reduced Faith and Strength.
- **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Loop:** the Chalice build with its Night Invader relic in the green slot. It loses Auto Charge +3, so the Art comes back more slowly (utility 12.0 vs 21.0).
- **Trade-offs:** 7.5 points below the Chalice, and it needs 4 Sovereign Sigils to unlock. Use it only if you don't have the Chalice. **R01182** (shockwaves; Improved Throwing Pot Damage; Ultimate Art Auto Charge +3) in the green slot ties at 101.4, trading Night Invader for Art charge.

## Assumptions and unknowns

- **Search depth:** 80 relics per slot and 2000 triples per side, split 1000 with rally and 1000 without. Not re-checked against a deeper search since the split.
- **`Reduced Damage Negation After Evading` at −8** puts it on the same level as the `Taking Damage` buildup curses. The exact size of the negation drop is unknown.
- **Multiplicative sustain** assumes heals restore a share of max HP. Whether flasks do (so the whole budget scales with max HP) is **(unverified)**. If flasks heal a fixed amount, max HP is somewhat overvalued.
- **Damage and sustain still add to each other.** Within each side, effects compound, so a loadout that piles into one side gets increasing returns. That's part of why the top loadouts lean into sustain. A damage × eHP model would favor balance more. It isn't in CLAUDE.md.
- **Sizes:** `Increased Maximum HP` +10% is unsourced. Heal amounts per fight (about 60 blocks, 10 thrust counters, the regens) are guesses. The Vigor curse at −5% max HP is a guess.
- **Post-1.03 sizes:** `Physical Attack Up` and `Improved Guard Counters` come from eldenring.wiki.gg. The guard-counter tier labels are inferred **(unverified)**.
- **Guard counter HP boost** is still scored as a guessed 18%.
- **Rally** tiers are scored as highest-only. wiki.gg says +1 and +2 stack with each other **(unverified)**.
- **Night Invader effect:** about +20% damage per CLAUDE.md. Copies are assumed not to stack **(unverified)**.
- **Stamina is unweighted** (CLAUDE.md).
- **Excluded curses:** relics with Death or Sleep `Taking Damage` curses, or with Ultimate Art Charging Impaired, were removed.
- **Chalice unlock:** needs Guardian Remembrance 2. You own Remembrance 3 and 4 relics, so it should be unlocked.
