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
- **Stacking:** assume different tiers of the same effect (e.g., `Improved Guard Counters` / `+1` / `+2`) do **not** stack, so only the highest counts. State this assumption when it affects a pick. Different effect families do stack.

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

1. Confirm the goal: character, weapon type, playstyle, and what "alt", "ult" or "skill" means (Character Skill vs. Ultimate Art).
2. Check the current meta with web search. Patches change effects and vessels.
3. Write effect weights for the goal and curse penalties for the build's stats and playstyle. Apply the Dormant Power and on-hit curse rules above.
4. Score relics, then brute-force or search every 6-slot combination for each eligible vessel, deduplicating effect families across all six slots.
5. Present the top vessel plus one alternative, preferring easy-to-get vessels when scores are close. For each loadout, give:
   - a table with every relic and every effect, curses attached
   - total curses, Dormant Powers carried, and any `unverified_effect` flags
   - the gameplay loop the build creates, and its trade-offs
6. Keep scripts in `scripts/` so weights can be adjusted and re-run.

## Character notes

Read the Nightfarer's file before building for them. Each covers kit and stat scaling, meta archetypes, vessels, every `[Character]`-tagged effect (with how many I own), remembrance relics (with `relic_id`s), key universal effects, on-build Dormant Powers, curse judgments, patch history, and sources. Current builds live in the character file. Update it when a build changes.

| Nightfarer | File | Notes |
|---|---|---|
| Wylder | [characters/wylder.md](characters/wylder.md) | |
| Guardian | [characters/guardian.md](characters/guardian.md) | Has current best and fallback builds |
| Ironeye | [characters/ironeye.md](characters/ironeye.md) | Some vessel colors unverified |
| Duchess | [characters/duchess.md](characters/duchess.md) | |
| Raider | [characters/raider.md](characters/raider.md) | |
| Revenant | [characters/revenant.md](characters/revenant.md) | Decrepit Goblet colors unverified |
| Recluse | [characters/recluse.md](characters/recluse.md) | Decrepit/Forgotten colors unverified; Bone-Like Stone not owned |
| Executor | [characters/executor.md](characters/executor.md) | |
| Scholar | [characters/scholar.md](characters/scholar.md) | Forsaken Hollows DLC; Forgotten Goblet colors unverified |
| Undertaker | [characters/undertaker.md](characters/undertaker.md) | Forsaken Hollows DLC; four vessels unverified |

In tagged effect text, "ability" usually means the character's passive and "Art" means the Ultimate Art.

## Open questions

- Does blocked chip damage trigger `Taking Damage Causes X Buildup` curses? Test early in a Deep of Night run against an elemental attacker.
- Do different tiers of the same effect stack? Currently assumed no. wiki.gg claims some do (e.g. `Partial HP Restoration` +1 and +2 stack with each other but not with the base; `Stamina Recovery upon Landing Attacks` +1 stacks with its base). Single source; untested.
- Standard-relic stat-swap effects (`[X] Improved A, Reduced B` on fixed DLC Scene relics): magnitudes unknown. Deep versions are documented in the character files.
