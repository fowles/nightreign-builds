# Executor

> Researched 2026-10-30. Sources at bottom. Game patch at time of research: App 1.03.5 (multiplayer hotfix, 2026-03-31); last balance patch 1.03.2 / Regulation 1.03.4 (2026-01-15). A PS4/PS5-only update (1.23 / 1.003.004, 2026-09-18) was reported by MP1st with no gameplay changes. No newer balance patch found.
> Anything marked **(unverified)** came from a single source or conflicting sources.

## Kit

| | |
|---|---|
| Base stat scaling | Dex S, Arcane S, Vigor B, End B, Str C, Mind D, Int D, Faith D (wiki.gg). Lv15: Vig 46, Mind 11, End 27, Str 25, Dex 63, Int 8, Fai 6, Arc 28. HP 1000, FP 100, Stamina 102. |
| Starting weapon | Executor's Blade (katana, innate bleed) |
| Passive | **Tenacity**: after recovering from an ailment, +20% attack power and +8 stamina regen/s for 20 s. Triggers when the ailment expires or is cured. Bleed, Sleep and Madness trigger it immediately. |
| Character Skill | **Cursed Sword** (renamed Suncatcher after the Remembrance): toggles to the Cursed Sword, no cooldown. Guard timing deflects for low stamina cost and stance damage; **deflects count as guards for passives**. Walk speed only; dodge is a short dash (8 i-frames vs 13). Three deflects "unlock" the sword: the next attack/weapon skill is empowered. The Cursed Sword deals no ailments and gets no katana-specific bonuses. |
| Ultimate Art | **Aspects of the Crucible: Beast**: full HP restore, max HP doubled, opening roar. Gauge drains over 15 s and can be cancelled early to save it. New light/heavy combos; guard = wide-area roar; weapon skill = claw swipe that ends the form. Large hitbox. Since 1.03.2: extra negation on the skill attack, a brief window where you can't be downed, and if HP hits 0 the form ends at 1 HP. |
| Stats that matter | Dex, Arcane (bleed), Vigor. Endurance (deflect stamina) is worth 0 in scoring per CLAUDE.md. |
| Stats that don't (near-free curses) | Intelligence, Faith. Strength is minor (C). |

"Skill" = Cursed Sword. "Ult/Art" = Beast transformation. In tagged effect text, **"ability" means the passive, Tenacity** (ailment recovery). "Roaring" = the guard input while in Beast form.

## Playstyles / archetypes

| Archetype | Weapons | Loop | Wants |
|---|---|---|---|
| **Bleed katana** (most-cited meta) | Executor's Blade, Rivers of Blood, Uchigatana, Nagakiba, Hand of Malenia | Bleed procs on the regular katana; Cursed Sword for deflect windows and big crits | Arcane, katana and bleed effects, Tenacity sustain, Improved Critical Hits |
| **Deflect / Cursed Sword** (buffed 1.03.2) | Cursed Sword plus any katana | Stay in the Cursed Sword, deflect three times, unlock, crit. Since 1.03.2 "Improved Skill Attack Power" and "Improved Melee Attack Power" apply to its arts. | Skill-attack boost, unlock heal, guard-triggered effects (deflect = guard), Improved Skill Attack Power, Improved Critical Hits |
| **Beast form** | Any | Bank Art; transform for burst plus a second life bar; roar heals the team | Roaring restores HP, Improved Roar & Breath Attacks, Art charge |

Most players mix all three: the bleed katana carries, the Cursed Sword handles bosses, and Beast is the panic button.

## Vessels

| Vessel | Normal | Deep | Unlock |
|---|---|---|---|
| Executor's Urn | R Y Y | R Y Y | Starter |
| Executor's Goblet | R B G | R B G | Small Jar Bazaar, 1200 Murk |
| Executor's Chalice | B Y W | Y Y G | Executor Remembrance 1 |
| Soot-Covered Executor's Urn | R R B | R R B | 4 Sovereign Sigils |
| Sealed Executor's Urn | Y Y R | G G B | 4 Sovereign Sigils |
| Decrepit Executor's Goblet (Forsaken Hollows) | R R Y **(unverified, single source)** | R R Y **(unverified, single source)** | 4 Sovereign Sigils |
| Forgotten Executor's Goblet (Forsaken Hollows) | G B R **(unverified, single source)** | Y G W **(unverified, single source)** | 4 Sovereign Sigils |
| Sacred Erdtree Grail (all) | Y Y Y | Y Y Y | 3000 Murk (after Night Aspect) |
| Spirit Shelter Grail (all) | G G G | G G G | 3000 Murk (after 4 Nightlords) |
| Giant's Cradle Grail (all) | B B B | B B B | 3000 Murk (after 7 Nightlords) |
| Scadutree Grail (all, DLC) | R R R | R R R | 3000 Murk (after Dreglord) |

The five base vessels match on wiki.gg and Fextralife. The two DLC vessels come only from wiki.gg (its Vessels and Executor pages agree, but that's one wiki); the Fextralife fetch was cut off before them.

## Character-tagged relic effects

Ratings: **Bleed** = bleed katana, **Defl** = deflect/Cursed Sword, **Beast** = Beast form.

| Effect | Kind | What it does (wiki.gg) | Bleed | Defl | Beast | Owned |
|---|---|---|---|---|---|---|
| [Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking | std | While the Cursed Sword is out: +35% damage for 6 s, −40% damage negation for 5 s. Renamed from "...Attacking Drains HP" and attack boost raised in 1.03.2. wiki.gg's numbers may predate the buff **(unverified)**. | good | core | niche | 13 |
| [Executor] While Character Skill is active, unlocking use of cursed sword restores HP | std | Heals 5% max HP + 100 when the sword unlocks (3 guards/deflects). Buffed 1.03.2; the number may be pre-buff **(unverified)**. | good | core | skip | 7 |
| [Executor] Roaring restores HP while Art is active | std | Each Beast roar heals self and nearby allies for 15% max HP | good | good | core | 17 |
| [Executor] Slowly Restore HP upon Ability Activation | deep | After ailment recovery (Tenacity): regen 0.27% max HP + 3 per second for 30 s; stacks on repeat. Duration raised in 1.03.2 (30 s may be pre- or post-buff). | core | good | good | 28 |
| [Executor] Improved Dexterity and Arcane, Reduced Vigor | deep | Dex +12, Arcane +9, Vigor −7 | core | good | niche | 6 deep, 1 std |
| [Executor] Improved Vigor and Endurance, Reduced Arcane | deep | Vigor +5, End +6, Arcane −13 | skip | good | good | 2 deep, 1 std |

Every known [Executor] effect is owned. The old "...Attacking Drains HP" text no longer exists after 1.03.2. If the scanner shows it, the relic data is stale.

**Stat swaps:**
- **Dex/Arc up, Vigor −7**: the damage swap. Arcane drives bleed buildup, Dex drives katana scaling. Costs about 7 Vigor of HP.
- **Vig/End up, Arcane −13**: a defensive swap for a deflect build with no bleed. It scores as Vigor +5 only, since stamina is worth 0. Arcane doesn't matter if the Cursed Sword (which can't inflict ailments) is your damage.
- The standard copies are DLC Scene relics (Grand Burning Scene: Vigor +3 / End +3 + swap; Grand Luminous Scene: Dex +3 / Arcane +3 + swap). They aren't in my unique-relic list, so query the db for their relic_ids.

## Remembrance / unique relics

| Relic | Color | Effects | Source | Owned |
|---|---|---|---|---|
| Blessed Flowers | Green | [Executor] While Character Skill is active, unlocking use of cursed sword restores HP; Dexterity +3 | Remembrance 1 | **R00762** |
| Golden Sprout | Red | [Executor] Roaring restores HP while Art is active; HP Recovery From Successful Guarding; Slowly restore HP for self and nearby allies when HP is low | Remembrance 2 | **R01927** |
| Grand Burning Scene | Red | [Executor] Roaring restores HP while Art is active; Dexterity +2; Arcane +2 | Small Jar Bazaar, 1000 Murk (after 4 Nightlords) | not in unique list |
| Grand Luminous Scene | Yellow | [Executor] Character Skill Boosts Attack but... (renamed effect); HP Recovery From Successful Guarding; Successful guarding fills more of the Art gauge | Collector Signboard, 3 Sigils | not in unique list |

Golden Sprout's "HP Recovery From Successful Guarding" should trigger on Cursed Sword deflects, since deflects count as guards for passives (per wiki.gg). That makes it strong on the deflect build.

## Key universal effects

| Group | Effects (exact text) |
|---|---|
| Offense | **Attack power increased for each Night Invader defeated** (≈+20%, meta-top per CLAUDE.md; standard relics only, 8 owned), Improved Katana Attack Power, Improved Attack Power with 3+ Katana Equipped, Improved Critical Hits (+1), Improved Skill Attack Power, Improved Melee Attack Power, Physical Attack Up (+1..+4), Improved Initial Standard Attack, Dexterity +3, Arcane +3, Starting armament inflicts blood loss, Changes compatible armament's skill to Blood Blade / Seppuku |
| Deflect (= guard) | HP Recovery From Successful Guarding, Successful guarding fills more of the Art gauge (+1), Improved Guard Counters (+1/+2) **(applies to deflects? unverified)** |
| Art / Beast | Improved Roar & Breath Attacks (1.02 made Roar & Breath boosts apply to some Beast attacks), Ultimate Art Auto Charge, Critical hits fill more of the Art gauge (+1), Defeating enemies fills more of the Art gauge |
| Sustain | **Rally** = Partial HP Restoration upon Post-Damage Attacks (non-negotiable for melee per CLAUDE.md), Increased Maximum HP, Vigor +3, HP Restoration upon Katana Attacks |
| Stamina | Increased Maximum Stamina, Critical Hit Boosts Stamina Recovery Speed: **worth 0 in scoring** (CLAUDE.md: stamina is tie-break only), even though deflects cost stamina |

## Dormant Powers

| Dormant Power | Verdict |
|---|---|
| Dormant Power Helps Discover Katana | neutral (on-build; the default pool already favors katanas) |
| Anything else | avoid (the Cursed Sword ignores your weapon, so other drops only matter for your second katana slot) |

## Curse considerations

| Curse | Verdict | Why |
|---|---|---|
| Reduced Faith and Strength | near-free | Faith D, Strength C and rarely used |
| Reduced Strength and Intelligence | near-free | |
| Reduced Intelligence and Dexterity / Reduced Dexterity and Faith | bad | Dex is his S stat |
| Reduced Vigor and Arcane | bad for bleed, acceptable for deflect | |
| Ultimate Art Charging Impaired | bad | Beast is his emergency heal and second life bar |
| Taking Damage Causes Death Buildup | **disqualifying** | Melee duelist who takes lots of hits |
| Taking Damage Causes Sleep / Madness Buildup | near-disqualifying | Sleep and Madness trigger Tenacity, but sleeping mid-fight is lethal |
| Taking Damage Causes Blood Loss Buildup | acceptable, possibly synergistic **(unverified)** | Bleed procs instantly trigger Tenacity (+20% attack) and the deep regen. Each proc still deals % HP damage. My inference, not a community-tested result. |
| Taking Damage Causes Poison / Rot / Frost Buildup | acceptable | Tenacity triggers when the ailment expires |
| Repeated Evasions Lower Damage Negation | acceptable | Executor mostly deflects rather than rolls; the Cursed Sword uses a dash |
| Reduced Damage Negation After Evading | very bad | A mistimed dodge costs extra damage (CLAUDE.md curse rules) |

## Meta notes and patch history

| Patch | Change |
|---|---|
| 1.02 (2025-07-31) | Roar & Breath boosts now apply to some Beast attacks |
| 1.02.1 (2025-08-12) | Fixed the unlock-heal relic not triggering in some cases |
| 1.02.2 (2025-09-10) | Cursed Sword attack power up (including its unleashed weapon skill); some Beast attacks stronger; Thrusting Counterattack HP restore now works with the Cursed Sword |
| 1.03 (2025-12-03) | Stagger fix on some parried attacks |
| 1.03.1 (2025-12-17) | Cold Mirage now applies to Beast |
| 1.03.2 (2026-01-15) | **Big buff**: Cursed Sword crit damage, Guard Boost and deflect stagger up; deflect stamina cost down; no guard break on stamina-out after a deflect; Skill/Melee Attack Power relic effects now apply to Cursed Sword arts. Beast: all attacks except Roar stronger (with Deep of Night depth scaling), extra negation on the skill attack, ends at 1 HP instead of dying. Tagged relics: skill-attack relic renamed and boosted, unlock-heal and Slowly Restore HP buffed. |

- Consensus: strong. S tier for random matchmaking (nightreignwiki.com, 2026); A in Steam Deep of Night posts.
- Guides still list bleed katanas (especially Rivers of Blood) as the top damage, but 1.03.2 made pure deflect play much more rewarding.

## Sources
- https://eldenring.wiki.gg/wiki/Executor
- https://eldenring.wiki.gg/wiki/Nightreign:Vessels
- https://eldenringnightreign.wiki.fextralife.com/Vessels
- https://eldenring.wiki.gg/wiki/Nightreign:Relics
- https://eldenring.wiki.gg/wiki/Nightreign:Patch_Notes
- https://mp1st.com/title-updates-and-patches/elden-ring-nightreign-version-1-03-2-balance-adjustments-update-1-003-002-1-22
- https://www.method.gg/nightreign/executor-guide-elden-ring-nightreign
- https://insider-gaming.com/best-executor-build-in-elden-ring-nightreign/
- https://nightreignwiki.com/characters/tier-list/
