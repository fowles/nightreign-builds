# Revenant

> Researched 2026-10-30. Sources at bottom. Game patch at time of research: App 1.03.5 (multiplayer hotfix, 2026-03-31); last balance patch 1.03.2 / Regulation 1.03.4 (2026-01-15). A PS4/PS5-only update (1.23 / 1.003.004, 2026-09-18) was reported by MP1st with no gameplay changes. No newer balance patch found.
> Anything marked **(unverified)** came from a single source or conflicting sources.

## Kit

| | |
|---|---|
| Base stat scaling | Faith S, Mind A, Int B, Arc B, Str C, Dex C, Vigor D, End D (wiki.gg grades). Lv15: Vig 35, Mind 31, End 21, Str 21, Dex 21, Int 30, Fai 51, Arc 12. HP 780, FP 200, Stamina 90. |
| Starting weapon | Cursed Claws (Faith S scaling) + Finger Seal (wiki.gg). The Finger Seal accepts the "Changes compatible armament's incantation to ..." effects (post-1.03 change, per wiki.gg). |
| Passive | **Necromancy**: non-boss enemies you helped kill (anyone can land the final blow) rise as allied ghosts for 1 minute. |
| Character Skill | **Summon Spirit**: summons one of three family members. Helen (fast, Page-like), Frederick (durable, Pumpkin Head-like), Sebastian (immobile, toughest, Giant Skeleton-like). No cooldown. Fallen family members return at half HP. FP cost not confirmed. |
| Ultimate Art | **Immortal March**: for 15 s, you, living allies and the active family member can't be killed (lethal damage leaves 1 HP). Instantly revives nearby downed allies (without immortality). Triggers a family special attack: Helen thrusts, Frederick spins, Sebastian fires a laser. |
| Stats that matter | Faith (claws, incantations), Mind/FP (summons, spells), Vigor (only 780 HP) |
| Stats that don't (near-free curses) | Intelligence, Dexterity, Arcane. Strength too, unless running the deep Strength swap. |

"Skill" = Summon Spirit. "Ult/Art" = Immortal March. In tagged effect text, **"ability" means the passive, Necromancy** (e.g. "Increased Max FP upon Ability Activation" = each raised ghost).

## Playstyles / archetypes

| Archetype | Weapons | Loop | Wants |
|---|---|---|---|
| **Faith summoner / support** (default) | Cursed Claws, any sacred seal | Keep a family member out, cast Faith incantations from the back, save Immortal March for revives and boss burst | Art buffs for the team, FP pool and regen, Improved Incantations, Holy/Fire Attack Power Up, Art charge |
| **Ult-centric team buffer** | Same | Charge Art fast, fire Immortal March with the family out for the 1.03.2-buffed special attack and +25% team damage | Strengthens family and allies, ghostflame explosion, Ultimate Art Auto Charge, Defeating enemies fills more of the Art gauge |
| **Strength/Faith melee** (niche) | Str/Faith weapons, claws | Deep "Improved Strength, Reduced Faith" (Str +25) turns her into a frontliner. wiki.gg suggests it. No community build found. **(unverified as viable)** | Physical Attack Up, Vigor, Max HP, Strength +N |

## Vessels

| Vessel | Normal | Deep | Unlock |
|---|---|---|---|
| Revenant's Urn | B B Y | B B Y | Starter |
| Revenant's Goblet | R R G | R R G | Small Jar Bazaar, 1200 Murk |
| Revenant's Chalice | B G W | B Y G | Revenant Remembrance 2 |
| Soot-Covered Revenant's Urn | R Y Y | R Y Y | 4 Sovereign Sigils |
| Sealed Revenant's Urn | Y B B | G G R | 4 Sovereign Sigils |
| Decrepit Revenant's Goblet (Forsaken Hollows) | R R Y **(unverified)** | R R Y | 4 Sovereign Sigils |
| Forgotten Revenant's Goblet (Forsaken Hollows) | G R R | Y G W | 4 Sovereign Sigils |
| Sacred Erdtree Grail (all) | Y Y Y | Y Y Y | 3000 Murk (after Night Aspect) |
| Spirit Shelter Grail (all) | G G G | G G G | 3000 Murk (after 4 Nightlords) |
| Giant's Cradle Grail (all) | B B B | B B B | 3000 Murk (after 7 Nightlords) |
| Scadutree Grail (all, DLC) | R R R | R R R | 3000 Murk (after Dreglord) |

Checked against wiki.gg Vessels and Fextralife Vessels. They disagree only on Decrepit normal: wiki.gg says R R Y; Fextralife's text says R R G, but its own slot icons differ from that text. Check in-game.

## Character-tagged relic effects

Ratings: **Sup** = Faith summoner/support, **Ult** = ult-centric, **Str** = Strength melee.

| Effect | Kind | What it does (wiki.gg) | Sup | Ult | Str | Owned |
|---|---|---|---|---|---|---|
| [Revenant] Strengthens family and allies when Ultimate Art is activated | std | +25% damage for living allies and family for 30 s | core | core | good | 13 |
| [Revenant] Trigger ghostflame explosion during Ultimate Art activation | std | Explosion, "base 20 magic damage". Scaling unknown, the number looks low. | niche | good | niche | 9 |
| [Revenant] Expend own HP to fully heal nearby allies when activating Art | std | Halves your current HP to fully heal allies, including ones being revived | good | good | skip | 7 |
| [Revenant] Power up while fighting alongside family | std | Helen: 1 HP/s regen; Frederick: +10% attack; Sebastian: +20% affinity damage negation | good | good | good | 5 |
| [Revenant] Increased Max FP upon Ability Activation | deep | Each raised ghost adds max FP: 0.75% (first 20), 0.85% (next 20), 0.95% (last 20), cap +51% | good | good | niche | 30 |
| [Revenant] Improved Strength, Reduced Faith | deep | Str +25, Faith −6 | skip | skip | core | 10 deep, 1 std |
| [Revenant] Improved Vigor and Endurance, Reduced Mind | deep | Vigor +5, End +5, Mind −11 | niche | niche | good | 2 deep, 1 std |

Every known [Revenant] effect is owned.

**Stat swaps:**
- **Str +25 / Faith −6**: a large Strength gain for a small Faith cost. It only pays off if you actually swing Strength weapons. For a Faith caster it's a straight loss.
- **Vigor/End +5 / Mind −11**: trades FP for survivability. Fine on a melee variant. A caster at 200 FP feels the Mind loss.
- The standard-relic copies are Forsaken Hollows Scene relics (Grand Luminous Scene: Str +3 / Faith +3 + swap; a Blue Scene: Vigor +3 / End +3 + swap). Those aren't in my unique-relic list, so query the db for their relic_ids.

## Remembrance / unique relics

| Relic | Color | Effects | Source | Owned |
|---|---|---|---|---|
| Small Makeup Brush | Blue | [Revenant] Power up while fighting alongside family; Increased rune acquisition for self and allies | Remembrance 1 | **R00760** (scanner flag: `unverified_effect` on the [Revenant] line) |
| Old Portrait | Blue | [Revenant] Expend own HP to fully heal nearby allies when activating Art; [Revenant] Trigger ghostflame explosion during Ultimate Art activation; Defeating enemies fills more of the Art gauge | Remembrance 3 | **R01926** |
| Grand Drizzly Scene | Blue | [Revenant] ghostflame explosion; Faith +2; Arcane +2 | Small Jar Bazaar, 1000 Murk (after 4 Nightlords) | not in unique list |
| Grand Drizzly Scene | Blue | [Revenant] Strengthens family and allies...; Items confer effect to all nearby allies; Starlight Shards at start | Collector Signboard, 3 Sigils | not in unique list |
| Grand Luminous Scene (DLC) | Yellow | [Revenant] Improved Strength, Reduced Faith; Strength +3; Faith +3 | Collector Signboard, 3 Sigils (after Dreglord) | 1 std copy of the effect owned (relic_id: query db) |

## Key universal effects

| Group | Effects (exact text) |
|---|---|
| Offense (Faith) | Improved Incantations (+1/+2), Holy Attack Power Up (+1..+4), Fire Attack Power Up (+1..+4), Improved Claw Attack Power, Improved Attack Power with 3+ Claws Equipped, Faith +3, Improved Fundamentalist / Godslayer / Dragon Communion Incantations (whichever school you're running) |
| FP | Increased Maximum FP, Reduced FP Consumption, Continuous FP Recovery, FP Restoration upon Claw Attacks, Max FP Up with 3+ Sacred Seals Equipped |
| Art charge | Ultimate Art Auto Charge (+1..+3), Defeating enemies fills more of the Art gauge (+1), Critical hits fill more of the Art gauge |
| Sustain / team | Increased Maximum HP, Vigor +3, Flask Also Heals Allies, Items confer effect to all nearby allies, Slowly restore HP for self and nearby allies when HP is low |
| Utility | Changes compatible armament's incantation to ... (Wrath of Gold, Lightning Spear, O, Flame!, etc.) for the Finger Seal |

## Dormant Powers

| Dormant Power | Faith summoner | Str melee |
|---|---|---|
| Dormant Power Helps Discover Sacred Seals | neutral (on-build) | avoid |
| Dormant Power Helps Discover Claws | neutral (on-build) | neutral if using claws |
| Any other weapon type | avoid | avoid, except the weapon class you actually run |

## Curse considerations

| Curse | Verdict | Why |
|---|---|---|
| Reduced Strength and Intelligence | near-free | Neither stat matters for Faith (bad for the Str variant) |
| Reduced Intelligence and Dexterity | near-free | Neither stat is used |
| Reduced Faith and Strength / Reduced Dexterity and Faith | bad | Faith is her S stat |
| Reduced Vigor and Arcane | acceptable-to-bad | Arcane is free, but she only has 780 HP |
| Ultimate Art Charging Impaired | **disqualifying** | Immortal March plus 4 Art-trigger tagged effects are her core |
| Taking Damage Causes X Buildup | acceptable for backline caster; Death/Sleep still avoid | She takes fewer hits than a tank, but a summoner who gets caught still dies |
| Near Death Reduces Max HP / Reduced Flask HP Restoration | acceptable | She can self-revive the team via Art |
| Lower Attack When Below Max HP | bad with "Expend own HP..." | That effect halves your HP on every Art, so this curse is almost always on |

## Meta notes and patch history

| Patch | Change |
|---|---|
| 1.02 (2025-07-31) | Bug fixes for summons and Lira backstab interaction |
| 1.02.2 (2025-09-10) | Spirits made more transparent; players can walk through Helen and Frederick |
| 1.03.1 (2025-12-17) | Immortal March visual fix; a Revenant family-effect tooltip wrongly showed as active on Scholar/Undertaker relics (fixed) |
| 1.03.2 (2026-01-15) | Family special attacks during Immortal March hit harder. **Summon Spirit spirits gain attack and damage negation scaled by Deep of Night depth.** |

- Deep of Night opinion on Revenant is split. One Steam DoN tier post puts her S, another B. A general 2026 tier list (nightreignwiki.com) puts her A for random matchmaking.
- No current community build was found for the Strength-swap variant.

## Sources
- https://eldenring.wiki.gg/wiki/Nightreign:Revenant
- https://eldenring.wiki.gg/wiki/Nightreign:Vessels
- https://eldenringnightreign.wiki.fextralife.com/Vessels
- https://eldenring.wiki.gg/wiki/Nightreign:Relics
- https://eldenring.wiki.gg/wiki/Nightreign:Patch_Notes
- https://mp1st.com/title-updates-and-patches/elden-ring-nightreign-version-1-03-2-balance-adjustments-update-1-003-002-1-22
- https://mp1st.com/title-updates-and-patches/elden-ring-nightreign-hotfix-1-03-5-march-31
- https://steamcommunity.com/app/2622380/discussions/0/603043591290473383/
- https://nightreignwiki.com/characters/tier-list/
