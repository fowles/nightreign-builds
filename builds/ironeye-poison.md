# Ironeye: Poison Mark

> Generated 2026-10-31 with `python3 -I scripts/ironeye.py --build poison`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** keep the boss poisoned so that every Marking triggers `[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies`. Marking adds 70 poison buildup. On an already-poisoned target it also deals 250 + 0.25% of max HP (wiki.gg).

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- the deep heavy-poison Marking effect
- a second poison source: `Starting armament inflicts poison` or `[Ironeye] Art Charge Activation Adds Poison Effect`. Without the flag (`--no-poison-source`), the model rates a poison weapon about the same as a big sustain relic and drops it (Ironeye's Goblet, 71.5). That leaves Marking as the only poison source, at ~25% uptime, and then it isn't a poison build.

## Results

Best loadout per vessel (top 5):

| Vessel | Total | Damage | Sustain | Utility | Penalties | Curses |
|---|---|---|---|---|---|---|
| Ironeye's Urn | 65.8 | 24.9 | 36.0 | 18.5 | −13.5 | 7 |
| Ironeye's Chalice | 65.4 | 26.2 | 34.7 | 9.5 | −5.0 | 4 |
| Forgotten Ironeye's Goblet | 65.0 | 21.3 | 38.6 | 18.5 | −13.5 | 7 |
| Ironeye's Goblet | 64.5 | 11.9 | 47.1 | 14.0 | −8.5 | 4 |
| Sealed Ironeye's Urn | 62.6 | 26.2 | 32.3 | 9.5 | −5.5 | 4 |

The top four are within 1.3 points, which is inside the model's noise. **I'd play the Chalice** (4 curses vs 7). The Urn tops the table, so it's shown first.

Utility, poise and the Marking-burst size are hand-weighted. The poison model is all guesses (see Model inputs).

## Best: Ironeye's Urn (Normal Y G G / Deep Y G G)

**Score 65.8:** damage 24.9, sustain 36.0, utility 18.5, penalties −13.5. Starter vessel.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal G | **R00066** Polished Tranquil Scene | **[Ironeye] +1 additional Character Skill use**; Dexterity +3 |
| Normal G | **R00892** Grand Tranquil Scene | FP Restoration upon Thrusting Sword Attacks *(out of focus)*; **Starting armament inflicts poison**; Lightning Attack Power Up +2 *(out of focus: physical arrows)* |
| Deep Y | **R01893** Deep Grand Luminous Scene | [Ironeye] Improved Vigor and Strength, Reduced Dexterity; Critical hits fill more of the Art gauge +1 *(curse: Reduced Dexterity and Faith)*; Improved Physical Damage Negation +2 *(curse: Continuous HP Loss)* |
| Deep G | **R00934** Deep Grand Tranquil Scene | **[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies**; Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Rot Buildup When Below Max HP)*; Defeating enemies fills more of the Art gauge +1 *(curse: Near Death Reduces Max HP)* |
| Deep G | **R01257** Deep Grand Tranquil Scene | Physical Attack Up +4 *(curse: Lower Attack When Below Max HP)*; Increased Maximum HP *(curse: Reduced Rune Acquisition)*; Improved Affinity Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |

- **Poison engine:** weapon poison plus Marking, ~66% poison uptime (guess). About 15 Markings a fight, ~10 of them on a poisoned target. Poison ticks and Marking bursts are worth ~36% of your damage in the model.
- **Curses: 7.**
  - Costly: Reduced Dexterity and Faith (−3, Dex is his A stat), Continuous HP Loss (−3), Lower Attack When Below Max HP (−3).
  - Mild: Near Death Reduces Max HP (−2), Rot Buildup When Below Max HP (−1), Reduced Rune Acquisition (−1).
  - Near-free: Reduced Strength and Intelligence.
  - No `Taking Damage Causes X`, no Death, no Ultimate Art Charging Impaired.
- **Dormant Powers:** none. **`unverified_effect` flags:** none. **Rally:** yes (R00934 +1).
- **Cleaner swap (64.4, 5 curses):** replace R01893 with **R01776** Deep Grand Luminous Scene (Attack power up when facing poison-afflicted enemy; Poise +3; Magic Damage Negation Up). This drops Continuous HP Loss and Reduced Dexterity and Faith. You lose the Vigor/Str respec and physical negation +2, and gain +10% damage against poisoned targets.

## Alternative (recommended): Ironeye's Chalice (Normal R G W / Deep R R G)

**Score 65.4:** damage 26.2, sustain 34.7, utility 9.5, penalties −5.0. Slot colors are from wiki.gg. Check them in game.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01911** Grand Burning Scene | **[Ironeye] Art Charge Activation Adds Poison Effect**; Attack power up when facing poison-afflicted enemy; Ultimate Art Auto Charge +3 |
| Normal G | **R00066** Polished Tranquil Scene | **[Ironeye] +1 additional Character Skill use**; Dexterity +3 |
| Normal W | **R01299** Grand Drizzly Scene (Blue) | [Raider] Duration of Ultimate Art extended *(wasted on Ironeye)*; Attack power increased for each Night Invader defeated; Vigor +2 |
| Deep R | **R00162** Deep Polished Burning Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Repeated Evasions Lower Damage Negation)*; Max HP increased for each great enemy defeated at a Great Church. |
| Deep R | **R00281** Deep Polished Burning Scene | **[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies**; Slowly restore HP for self and nearby allies when HP is low |
| Deep G | **R01257** Deep Grand Tranquil Scene | Physical Attack Up +4 *(curse: Lower Attack When Below Max HP)*; Increased Maximum HP *(curse: Reduced Rune Acquisition)*; Improved Affinity Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |

- **Poison engine:** charged Single Shot (300 poison) plus Marking, ~36% uptime (guess). There's no poisoned weapon, so the starting bow keeps full damage and you're free to switch to any bow you find. The trade is fewer poisoned Markings (~5 bursts a fight vs ~10).
- **Curses: 4.** Lower Attack When Below Max HP (−3), Reduced Rune Acquisition (−1), Repeated Evasions Lower Damage Negation (fine: only chained dodges), Reduced Strength and Intelligence (near-free).
- **Dormant Powers:** none. **`unverified_effect` flags:** none. **Rally:** yes (R00162 +2).
- To run both poison sources here, put **R00858** Grand Burning Scene (Partial HP Restoration upon Post-Damage Attacks; Starting armament inflicts poison; Changes compatible armament's skill to Lightning Slash) in the white slot in place of R01299. The rally on it is redundant with the deep +2 copy. Not separately scored.

## Gameplay loop

1. Open with arrows from the poisoned starting bow (Urn) or a charged Single Shot (Chalice) to get the first poison proc.
2. Mark through the boss while it's poisoned. Each Marking adds 70 more buildup and, on a poisoned target, a ~250 + 0.25% max HP burst. Two charges let you mark, reposition, and mark again.
3. Keep the weak point up for the team's +10% damage, and pop it with arrows.
4. Charge Single Shot when it's ready. On the Chalice it's your main poison source. On both it's still the revive.

## Trade-offs and unknowns

- **Poison numbers are guesses.** Uptime per source, poison DoT on bosses, and the ~3%-of-your-fight-damage value per heavy-poison burst (assumes ~25k boss HP and ~8–10k damage from you) all come without a source. If bursts are worth less, the poison source requirement is what keeps this a poison build.
- `Starting armament inflicts poison` costs 15% damage on the starting bow (wiki.gg), and you have to keep using that bow.
- Whether attack buffs scale poison damage is unknown. The model adds poison as flat damage with no buffs applied.
- `[Ironeye] Improved Vigor and Strength, Reduced Dexterity` is valued as 8% max HP minus ~6% bow damage (guess).

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage slices | arrows 0.70 (20% first in chain, 70% from the starting bow), Single Shot 0.12, Marking bursts 0.10, crits 0.05, melee 0.03 | guesses |
| Poison uptime per source | weapon 0.55, Marking 0.25, charged Art 0.15; combined as 1 − Π(1 − u) | guesses |
| Poison DoT | 10% of your damage at full uptime | guess |
| Heavy-poison burst | 3% of your fight damage each, ×15 Markings × uptime | guess on wiki.gg's 250 + 0.25% max HP |
| `vs poisoned` / `Poison & Rot in Vicinity` | 10 / 16 / 20% and 12%, × poison uptime | wiki.gg sizes; uptime model |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Rally | 1.0 / 1.25 / 1.35 bars per fight | ranged takes fewer hits than the 1.5 melee anchor; guess |
| Ultimate Art Charging Impaired | disqualifying | the charged Art delivers poison and revives |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (heavy poison 70 / 250 + 0.25%, Art poison 300, starting-armament poison −15% / 35 buildup, vs-poisoned sizes, Poison & Rot +12% / 20 s)
- https://vulkk.com/2025/09/17/nightreign-ironeye-build-guide-and-tips/ and https://www.dexerto.com/elden-ring/best-ironeye-build-in-elden-ring-nightreign-3199036 (poison bow is the most cited Ironeye build)
