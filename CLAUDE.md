# Nightreign Deep of Night Build Workshop

This project is for designing **Elden Ring Nightreign** relic loadouts for **Deep of Night** using my own relic inventory. Every recommendation must use relics I actually own, identified by `relic_id`.

## Data

- `mfk-relicdb.json` is my full relic inventory, produced by a video-scan pipeline.
  - `relics[]`: each entry has `relic_id`, `status` (only use `active`), and `relic`:
    - `name`, `color` (Red/Blue/Yellow/Green), `kind` (`standard` | `deep`)
    - `effects[]`: `{text, curse}`. `curse` is null or the drawback attached to that specific effect.
    - `nightfarer`: null for universal relics, or the character name for relics with a `[Character]`-tagged effect
    - `flags`: `unverified_effect:<text>` means the scanner wasn't sure of that effect text. Call these out, and prefer unflagged alternatives when they're close in value.
  - `scans[]`: scan history. Newer scans may add relics or mark them missing.
- Don't read the whole file into context (~1.5 MB). Query it with scripts (Python `-I`, `json` module).

## Core game rules

- **Deep of Night uses all six slots.** Each vessel has 3 normal slots, which take `standard` relics, and 3 deep slots, which take `deep` relics. Both sets apply in Deep of Night. Deep relics do nothing in normal expeditions.
- **Slot colors must match.** White slots accept any color.
- **Character-tagged effects** (`[Guardian] ...`) only work on that Nightfarer. A relic tagged for another character can still be used for its other effects, but the tagged effect is wasted. Score it that way.
- **Stacking:** different effect families always stack. Within one family it depends on the kind of buff:
  - **Attack buffs stack, and multiply** (two +10% = +21%). Count every copy, across tiers and duplicates: `Physical Attack Up`, element `Attack Power Up`, `Improved Affinity Attack Power`, `Improved Sorceries`/`Incantations`, spell-school and weapon-class attack power, `Improved Guard Counters`. Exception: conditional attack buffs (grease, `... in Vicinity Improves Attack Power`, attack up vs. poison/rot/frostbite) count highest tier only **(unverified)**.
  - **Defensive and healing buffs don't stack.** Only the highest tier counts: damage negation, poise, HP recovery and restoration, max HP. Different negation families (e.g. physical and affinity) still multiply together. wiki.gg says `Partial HP Restoration +1` and `+2` stack with each other **(unverified)**.
  - **Everything else** (crits, Art gauge, cooldowns): unknown. Assume highest tier only and say so when it affects a pick.

## Weighing effects

Weight = **focus × size × coverage × uptime × availability**, scored at **0.4 points per 1%** of total damage or of effective HP (eHP). The same scale is used for damage and sustain and in every build, so scores compare. The reasoning: how long you survive scales with eHP and how long you take to kill scales with damage, so +1% of either counts the same.

- **Focus is binary.** An effect is in focus if it boosts something the build does every fight: its damage type, weapon class, spell school, or the character's skill, Art or passive. Out-of-focus effects are worth 0, not negative. Dormant Power and curse penalties still apply separately.
- **Size:** use real percentages where known, e.g. `Physical Attack Up` base through +4 = 3 / 4 / 5 / 8.5 / 10%. Mark guessed sizes **(unverified)**.
- **Coverage (per build):** the share of the build's total damage that a damage effect boosts.
  - The default is 1.0, for effects like `Physical Attack Up` on a physical weapon build.
  - A narrow scope gets its fraction: e.g. `guard_counter: 0.35` for a guard-counter Guardian, or about 0.9 for `Improved Bestial Incantations` on an explicit Bestial caster.
  - Damage: total = Π(1 + all-damage buffs) × [(1 − Σc) + Σ c × Π(1 + that scope's buffs)], and points = 0.4 × (total − 1) × 100. Flat damage sources (shockwaves, stats) are added as points.
- **Fight model (per build)** for sustain:
  - **Incoming mix:** the share of damage taken per type (e.g. physical 0.6, each element 0.1). Negations multiply: damage taken = Σ share × Π(1 − negation), and eHP gain = 1 / damage taken − 1. Affinity negation applies to every element.
  - **Fight HP budget:** how many max-HP bars you absorb per fight, counting base HP, flasks and baseline regen (e.g. 3.0). A heal worth h max-HP bars per fight adds h / budget eHP. Max HP +x% adds about x% eHP.
  - **Ally factor:** how much each ally's eHP counts compared to yours (e.g. 0.5, with 2 allies). Used for team heals and team negation.
- **Uptime:** discount conditional effects (only at low HP, only while the Art is active, only near Madness, and so on).
- **Availability:** discount effects that need specific drops (a spell school, a weapon class, `3+ X Equipped`) by how likely the run is to supply them.
- **Meta anchors:**
  - **`Attack power increased for each Night Invader defeated`** ≈ **+20% damage**, possibly the best damage effect in the current meta. It's only on standard relics. Assume copies don't stack **(unverified)**.
  - **Rally (`Partial HP Restoration upon Post-Damage Attacks`)** is by far the strongest melee sustain effect and is **non-negotiable for melee builds**. Anchor it at 50% eHP for the base tier (20 points); +1/+2 heal 25%/35% more (25/27 points). Check that every top melee loadout carries it.
  - **Stamina is worth 0.** That covers max stamina, stamina recovery, and Endurance. It's nice to have at best. Use it only to break a tie.
- **Score in four parts**, which must add up to the total:
  - **damage:** attack buffs, guard counters, damage-dealing passives and skills
  - **sustain:** healing, max HP, damage negation, poise, team heals and protection
  - **utility:** Art gauge, cooldowns, everything else
  - **penalties:** curses, Dormant Powers, `unverified_effect` flags

  Utility, poise and aggro effects are still hand-weighted. Say so.

## Non-negotiable rules

1. **List every effect on every relic you recommend, including filler.** Never shorten a relic to its "useful" effects. A two- or three-effect relic must show all of them, with each curse attached to its effect.
2. **Dormant Power effects matter a lot.** `Dormant Power Helps Discover <Weapon>` changes what weapons drop during the run.
   - Avoid any Dormant Power for a weapon type the build doesn't use. Treat it as a real negative, not filler.
   - A Dormant Power for the build's own weapon is **neutral**: allowed, but not needed. The character's default drop pool is fine.
   - Several conflicting Dormant Powers dilute each other. Never stack them by accident.
   - Always flag which Dormant Powers a loadout carries, if any.
3. **Curses: judge each one against the build.**
   - Curses that lower a stat the build doesn't scale on are near-free (e.g., Int/Faith on a Strength build).
   - `Ultimate Art Charging Impaired` is disqualifying for any build that relies on its Ultimate Art.
   - **`Taking Damage Causes X Buildup`**: it's unconfirmed whether blocked chip damage triggers these. For guard-heavy builds, treat them as near-disqualifying, especially **Death** (an instant kill when the bar fills) and **Sleep**. Prefer `... When Below Max HP` variants or non-status curses.
   - Don't stack the same curse twice (e.g., two `All Resistances Down`) without saying so.
   - Count total curses in a loadout and report it.
4. **Optimize all six slots together, not normal and deep separately.** Effects duplicate across the two sets.
5. **State assumptions and unknowns plainly.** If something is unverified (game mechanics, vessel slot colors, scanner flags), say so instead of guessing.

## Vessels

Each character file lists that Nightfarer's vessels with slot colors. Colors come from eldenring.wiki.gg (`Nightreign:Vessels`), cross-checked with Fextralife; rows marked **(unverified)** disagree between sources. Verify against the in-game Relic Rites screen if something looks off.

Grails usable by every Nightfarer:

| Vessel | Normal | Deep | Unlock |
|---|---|---|---|
| Sacred Erdtree Grail | Y Y Y | Y Y Y | 3000 Murk |
| Spirit Shelter Grail | G G G | G G G | 3000 Murk |
| Giant's Cradle Grail | B B B | B B B | 3000 Murk |
| Scadutree Grail | R R R | R R R | 3000 Murk |

## Workflow for a new build

1. Confirm the goal: character, weapon type, playstyle. Fix the in-focus list, the coverage table and the fight model.
2. Check the current meta with web search. Patches change effects and vessels.
3. Write effect weights from **Weighing effects**, and curse penalties for the build's stats and playstyle. Apply the Dormant Power and on-hit curse rules above.
4. Score relics, then search every 6-slot combination for each eligible vessel, applying the stacking rules across all six slots.
5. Present the top vessel plus one alternative. For each loadout, give:
   - a table with every relic and every effect, curses attached
   - the score split into damage / sustain / utility / penalties, plus the total
   - the coverage table and fight model used, with guesses marked
   - total curses, Dormant Powers carried, and any `unverified_effect` flags
   - the gameplay loop the build creates, and its trade-offs
6. Keep scripts in `scripts/` so weights can be adjusted and re-run.
7. Write the result to its own file in `builds/`, not the character file.

## Character notes

Read the Nightfarer's file before building for them. Each covers kit and stat scaling, meta archetypes, vessels, every `[Character]`-tagged effect (with how many I own), remembrance relics (with `relic_id`s), key universal effects, on-build Dormant Powers, curse judgments, patch history, and sources. Character files are reference only: don't put builds in them. Each build gets its own file in `builds/`, named `<nightfarer>-<goal>.md` (e.g. `builds/guardian-sustain.md`), with the full presentation from the workflow above. Update a build's file when it changes.

| Nightfarer | File |
|---|---|
| Wylder | [characters/wylder.md](characters/wylder.md) |
| Guardian | [characters/guardian.md](characters/guardian.md) |
| Ironeye | [characters/ironeye.md](characters/ironeye.md) |
| Duchess | [characters/duchess.md](characters/duchess.md) |
| Raider | [characters/raider.md](characters/raider.md) |
| Revenant | [characters/revenant.md](characters/revenant.md) |
| Recluse | [characters/recluse.md](characters/recluse.md) |
| Executor | [characters/executor.md](characters/executor.md) |
| Scholar | [characters/scholar.md](characters/scholar.md) |
| Undertaker | [characters/undertaker.md](characters/undertaker.md) |

In tagged effect text, "ability" usually means the character's passive and "Art" means the Ultimate Art.

