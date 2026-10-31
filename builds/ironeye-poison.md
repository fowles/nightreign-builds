# Ironeye: Poison Mark

> Generated 2026-10-31 with `python3 -I scripts/ironeye.py --build poison`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** keep the boss poisoned so that every Marking triggers `[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies`. Marking adds 70 poison buildup. On an already-poisoned target it also deals 250 + 0.25% of max HP (wiki.gg).

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- the deep heavy-poison Marking effect
- a second poison source: `Starting armament inflicts poison` or `[Ironeye] Art Charge Activation Adds Poison Effect`. Without the flag (`--no-poison-source`), the model narrowly prefers a loadout with Marking as the only poison source, at ~25% uptime (Ironeye's Goblet, 51.8). That isn't a poison build.

Rally (`Partial HP Restoration upon Post-Damage Attacks`) does nothing on a ranged bow build, so it weighs 0.

## Results

Best loadout per vessel (top 4):

| Vessel | Total | Damage | Sustain | Utility | Penalties | Curses |
|---|---|---|---|---|---|---|
| Soot-Covered Ironeye's Urn | 49.7 | 47.2 | 2.0 | 10.0 | −9.5 | 5 |
| Ironeye's Chalice | 49.2 | 33.5 | 11.2 | 9.5 | −5.0 | 4 |
| Forgotten Ironeye's Goblet | 47.3 | 41.8 | 7.9 | 9.5 | −12.0 | 7 |
| Sealed Ironeye's Urn | 46.5 | 38.6 | 1.4 | 9.5 | −3.0 | 3 |

The top two are 0.5 apart. **I'd play the Chalice:** it has fewer curses, real sustain, and no curses that build up poison on you. The Soot-Covered Urn is the glass-cannon option, and its slot colors are **unverified** between sources.

Utility, poise and the Marking-burst size are hand-weighted. The poison model is all guesses (see Model inputs).

## Best: Soot-Covered Ironeye's Urn (Normal B Y Y / Deep B Y Y)

**Score 49.7:** damage 47.2, sustain 2.0, utility 10.0, penalties −9.5. Unlock: 4 Sovereign Sigils.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R00842** Grand Drizzly Scene | **[Ironeye] +1 additional Character Skill use**; Defeating enemies restores HP for allies but not for self; Endurance +2 *(stamina: worth 0)* |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal Y | **R00814** Night of the Wise | Increased Maximum FP; **Starting armament inflicts poison**; **Poison & Rot in Vicinity Increases Attack Power** |
| Deep B | **R01283** Deep Grand Drizzly Scene | **[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies**; Physical Attack Up +3 *(curse: Taking Damage Causes Blood Loss Buildup)*; Improved Affinity Damage Negation |
| Deep Y | **R00292** Deep Polished Luminous Scene | [Wylder] Character Skill inflicts Blood Loss *(wasted on Ironeye)*; Physical Attack Up +4 *(curse: Near Death Reduces Max HP)* |
| Deep Y | **R00914** Deep Grand Luminous Scene | HP Restoration upon Thrusting Counterattack +1 *(out of focus; curse: Taking Damage Causes Poison Buildup)*; Attack power up when facing poison-afflicted enemy +1 *(curse: Poison Buildup When Below Max HP)*; Physical Attack Up +3 *(curse: Reduced Damage Negation for Flask Usages)* |

- **Poison engine:** weapon poison plus Marking, ~66% uptime (guess). About 15 Markings a fight, ~10 of them on a poisoned target. Poison ticks and Marking bursts add ~36% of your damage, on top of +16% vs poisoned and +12% from Poison & Rot in Vicinity.
- **Damage stack:** Physical Attack Up +3 / +4 / +3 multiply (+37%), plus Night Invader.
- **Curses: 5.**
  - Reduced Damage Negation for Flask Usages (−2.5), Near Death Reduces Max HP (−2).
  - Taking Damage Causes Blood Loss Buildup (−2) and Taking Damage Causes Poison Buildup (−2): mild at range, and no Death or Sleep.
  - Poison Buildup When Below Max HP (−1).
  - No Ultimate Art Charging Impaired.
- **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Sustain is nearly zero (2.0).** One mistake hurts.

## Alternative (recommended): Ironeye's Chalice (Normal R G W / Deep R R G)

**Score 49.2:** damage 33.5, sustain 11.2, utility 9.5, penalties −5.0. Slot colors are from wiki.gg. Check them in game.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01188** Grand Burning Scene | **Starting armament inflicts poison**; Changes compatible armament's skill to Thunderbolt at start of expedition *(skill swap; a bow likely isn't compatible)*; Poise +1 |
| Normal G | **R00066** Polished Tranquil Scene | **[Ironeye] +1 additional Character Skill use**; Dexterity +3 |
| Normal W | **R00156** Polished Luminous Scene (Yellow) | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Deep R | **R00281** Deep Polished Burning Scene | **[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies**; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R01525** Deep Grand Burning Scene | **Attack power up when facing poison-afflicted enemy +2** *(curse: Repeated Evasions Lower Damage Negation)*; Holy Damage Negation Up; Improved Rot Resistance |
| Deep G | **R01257** Deep Grand Tranquil Scene | Physical Attack Up +4 *(curse: Lower Attack When Below Max HP)*; Increased Maximum HP *(curse: Reduced Rune Acquisition)*; Improved Affinity Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |

- **Poison engine:** the same ~66% uptime (weapon poison plus Marking), with +20% vs poisoned (R01525 +2).
- **Curses: 4.** Lower Attack When Below Max HP (−3), Reduced Rune Acquisition (−1), Repeated Evasions Lower Damage Negation (fine: only chained dodges), Reduced Strength and Intelligence (near-free).
- **Dormant Powers:** none. **`unverified_effect` flags:** none.

## Gameplay loop

1. Open with arrows from the poisoned starting bow to get the first proc.
2. Mark through the boss while it's poisoned. Each Marking adds 70 more buildup and, on a poisoned target, a ~250 + 0.25% max HP burst. Two charges let you mark, reposition, and mark again.
3. Keep the weak point up for the team's +10% damage, and pop it with arrows.
4. Single Shot is your burst and the revive. No loadout carries Ultimate Art Charging Impaired.

## Trade-offs and unknowns

- **Poison numbers are guesses.** Uptime per source, poison DoT on bosses, and the ~3%-of-your-fight-damage value per heavy-poison burst (assumes ~25k boss HP and ~8–10k damage from you) all come without a source.
- `Starting armament inflicts poison` costs 15% damage on the starting bow (wiki.gg), and you have to keep using that bow.
- Whether attack buffs scale poison damage is unknown. The model adds poison as flat damage with no buffs applied.

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage slices | arrows 0.70 (20% first in chain, 70% from the starting bow), Single Shot 0.12, Marking bursts 0.10, crits 0.05, melee 0.03 | guesses |
| Poison uptime per source | weapon 0.55, Marking 0.25, charged Art 0.15; combined as 1 − Π(1 − u) | guesses |
| Poison DoT | 10% of your damage at full uptime | guess |
| Heavy-poison burst | 3% of your fight damage each, ×15 Markings × uptime | guess on wiki.gg's 250 + 0.25% max HP |
| `vs poisoned` / `Poison & Rot in Vicinity` | 10 / 16 / 20% and 12%, × poison uptime | wiki.gg sizes; uptime model |
| Rally | 0 | does nothing for ranged |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Ultimate Art Charging Impaired | disqualifying | the charged Art delivers poison and revives |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (heavy poison 70 / 250 + 0.25%, Art poison 300, starting-armament poison −15% / 35 buildup, vs-poisoned sizes, Poison & Rot +12% / 20 s)
- https://vulkk.com/2025/09/17/nightreign-ironeye-build-guide-and-tips/ and https://www.dexerto.com/elden-ring/best-ironeye-build-in-elden-ring-nightreign-3199036 (poison bow is the most cited Ironeye build)
