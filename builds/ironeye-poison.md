# Ironeye: Poison Mark

> Generated 2026-11-01 with `python3 -I scripts/ironeye.py --build poison`. Character reference: [characters/ironeye.md](../characters/ironeye.md).

**Goal:** keep the boss poisoned so that every Marking triggers `[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies`. Marking adds 70 poison buildup. On an already-poisoned target it also deals 250 + 0.25% of max HP (wiki.gg). The charged Single Shot, with `[Ironeye] Art Charge Activation Adds Poison Effect`, is the build's second poison source.

**Requirements (enforced by the search):**
- `[Ironeye] +1 additional Character Skill use` (your rule for every Ironeye build)
- the deep heavy-poison Marking effect
- `[Ironeye] Art Charge Activation Adds Poison Effect` (your call: the build is built around the poisoned Single Shot). `Starting armament inflicts poison` is optional. Drop the Art requirement with `--no-art-poison`.

Rally (`Partial HP Restoration upon Post-Damage Attacks`) does nothing on a ranged bow build, so it weighs 0. **Arrows count as thrusting counterattacks** when they land during an enemy's attack (confirmed by you), so `HP Restoration upon Thrusting Counterattack` and `[Ironeye] Boosts thrusting counterattacks after executing Art` are now scored (see Model inputs).

## Results

Best loadout per vessel (top 4):

| Vessel | Total | Damage | Sustain | Utility | Penalties | Curses |
|---|---|---|---|---|---|---|
| Forgotten Ironeye's Goblet | 51.2 | 40.9 | 12.8 | 9.5 | −12.0 | 7 |
| Ironeye's Chalice | 51.0 | 32.0 | 15.5 | 14.0 | −10.5 | 5 |
| Scadutree Grail | 49.6 | 29.1 | 15.5 | 9.5 | −4.5 | 3 |
| Ironeye's Goblet | 48.8 | 37.0 | 11.8 | 9.5 | −9.5 | 5 |

The top three are within 1.6 points. **I'd play the Scadutree Grail:** 3 curses against 7, only one of them builds up status on you, and it costs 3000 Murk instead of 4 Sovereign Sigils. The Forgotten Goblet carries two poison-buildup curses and a Blood Loss one on a build that already sits in poison clouds. The Chalice (51.0) carries `Taking Damage Causes Madness Buildup` and `Reduced Flask HP Restoration`.

None of the top loadouts carries `Starting armament inflicts poison` alongside the Art poison: the extra slot and the −15% on the starting bow cost more than the uptime it adds in the model. Poison uptime is therefore ~36% (Marking + Art) rather than the ~66% the old weapon-poison loadouts had.

Utility, poise and the Marking-burst size are hand-weighted. The poison model is all guesses (see Model inputs).

## Best: Forgotten Ironeye's Goblet (Normal Y B R / Deep Y G W)

**Score 51.2:** damage 40.9, sustain 12.8, utility 9.5, penalties −12.0. Unlock: 4 Sovereign Sigils.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal B | **R00941** Grand Drizzly Scene | **[Ironeye] Art Charge Activation Adds Poison Effect**; Fire Grease in possession at start of expedition *(out of focus)*; Strength +1 *(out of focus)* |
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Deep Y | **R00914** Deep Grand Luminous Scene | HP Restoration upon Thrusting Counterattack +1 *(curse: Taking Damage Causes Poison Buildup)*; Attack power up when facing poison-afflicted enemy +1 *(curse: Poison Buildup When Below Max HP)*; Physical Attack Up +3 *(curse: Reduced Damage Negation for Flask Usages)* |
| Deep G | **R01257** Deep Grand Tranquil Scene | Physical Attack Up +4 *(curse: Lower Attack When Below Max HP)*; Increased Maximum HP *(curse: Reduced Rune Acquisition)*; Improved Affinity Damage Negation +1 *(curse: Reduced Strength and Intelligence)* |
| Deep W | **R01283** Deep Grand Drizzly Scene (Blue) | **[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies**; Physical Attack Up +3 *(curse: Taking Damage Causes Blood Loss Buildup)*; Improved Affinity Damage Negation |

- **Poison engine:** Art poison plus Marking, ~36% uptime (guess). About 15 Markings a fight. Poison ticks and Marking bursts add ~20% of your damage, plus +16% vs poisoned × uptime.
- **Damage stack:** Physical Attack Up +3 / +4 / +3 multiply (+37%), plus Night Invader and the evergaol stacks.
- **Curses: 7.**
  - Lower Attack When Below Max HP (−3), Reduced Damage Negation for Flask Usages (−2.5).
  - Taking Damage Causes Poison Buildup (−2) and Taking Damage Causes Blood Loss Buildup (−2): mild at range, no Death or Sleep.
  - Poison Buildup When Below Max HP (−1), Reduced Rune Acquisition (−1), Reduced Strength and Intelligence (near-free).
  - No Ultimate Art Charging Impaired.
- **Dormant Powers:** none. **`unverified_effect` flags:** none.

## Alternative (recommended): Scadutree Grail (Normal R R R / Deep R R R)

**Score 49.6:** damage 29.1, sustain 15.5, utility 9.5, penalties −4.5. Unlock: 3000 Murk.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R01041** Grand Burning Scene | [Duchess] Defeating enemies while Art is active ups attack power *(wasted on Ironeye)*; Attack power increased for each Night Invader defeated; HP Restoration upon Thrusting Counterattack |
| Normal R | **R01911** Grand Burning Scene | **[Ironeye] Art Charge Activation Adds Poison Effect**; **Attack power up when facing poison-afflicted enemy**; Ultimate Art Auto Charge +3 |
| Normal R | **R00826** Grand Burning Scene | **[Ironeye] +1 additional Character Skill use**; Attack power increased for each evergaol prisoner defeated; Endurance +1 *(stamina: worth 0)* |
| Deep R | **R00281** Deep Polished Burning Scene | **[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies**; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R00851** Deep Grand Burning Scene | [Revenant] Increased Max FP upon Ability Activation *(wasted on Ironeye)*; Increased Maximum HP *(curse: Near Death Reduces Max HP)*; Physical Attack Up +2 |
| Deep R | **R00243** Deep Polished Burning Scene | Physical Attack Up +3 *(curse: Reduced Faith and Strength)*; Improved Affinity Damage Negation +1 *(curse: Taking Damage Causes Poison Buildup)* |

- **Poison engine:** the same ~36% uptime (Art plus Marking), with +10% vs poisoned (R01911, base tier).
- **Curses: 3.** Near Death Reduces Max HP (−2), Taking Damage Causes Poison Buildup (−2, mild at range), Reduced Faith and Strength (near-free).
- **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Ironeye's Chalice (51.0)** is the higher-scoring middle option: it keeps R01041, R01911 and R00281, adds **R00066** (+1 skill use; Dexterity +3), **R00136** (Critical hits fill more of the Art gauge +1 *(curse: Taking Damage Causes Madness Buildup)*; Physical Attack Up +3 *(curse: Reduced Flask HP Restoration)*) and **R01257** (above). Its slot colors are from wiki.gg; check them in game.

## Gameplay loop

1. Charge Single Shot early: the fully charged Art puts 300 poison on the main arrow and opens the poison window.
2. Mark through the boss while it's poisoned. Each Marking adds 70 more buildup and, on a poisoned target, a ~250 + 0.25% max HP burst. Two charges let you mark, reposition, and mark again.
3. Keep the weak point up for the team's +10% damage, and pop it with arrows. Arrows that land during the boss's attacks are thrusting counters and heal you (2.5% max HP each).
4. Single Shot is also the revive. No loadout carries Ultimate Art Charging Impaired; Art gauge effects are weighted ×1.5 on this build.

## Trade-offs and unknowns

- **Poison numbers are guesses.** Uptime per source, poison DoT on bosses, and the ~3%-of-your-fight-damage value per heavy-poison burst (assumes ~25k boss HP and ~8–10k damage from you) all come without a source. If the charged Art keeps a boss poisoned longer than the 15% uptime assumed, Art gauge effects and the Art requirement are worth even more.
- Adding `Starting armament inflicts poison` (R00814, R01188 and others) would raise uptime but costs a slot and 15% damage on the starting bow (wiki.gg). The model doesn't take it.
- Whether attack buffs scale poison damage is unknown. The model adds poison as flat damage with no buffs applied.
- How many arrows per fight land as thrusting counters is a guess (15 for the heal, 30% of arrow damage for the Art boost).

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage slices | arrows 0.70 (20% first in chain, 70% from the starting bow), Single Shot 0.12, Marking bursts 0.10, crits 0.05, melee 0.03 | guesses |
| Poison uptime per source | weapon 0.55, Marking 0.25, charged Art 0.15; combined as 1 − Π(1 − u) | guesses |
| Poison DoT | 10% of your damage at full uptime | guess |
| Heavy-poison burst | 3% of your fight damage each, ×15 Markings × uptime | guess on wiki.gg's 250 + 0.25% max HP |
| `vs poisoned` / `Poison & Rot in Vicinity` | 10 / 16 / 20% and 12%, × poison uptime | wiki.gg sizes; uptime model |
| Thrusting counters (arrows) | 30% of arrow damage lands as counters; 15 counter hits per fight | guesses; arrows counting confirmed by you |
| `HP Restoration upon Thrusting Counterattack` | 2.5% max HP per counter hit (base, wiki.gg); +1 guessed 3% → 0.375 / 0.45 bars per fight | heal tier, highest only |
| `[Ironeye] Boosts thrusting counterattacks after executing Art` | +20% for 30 s × 0.4 window uptime × 0.3 counter share on bow damage (~+2.4% bow damage) | size Vulkk/GameWith; uptime guess |
| Rally | 0 | does nothing for ranged |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Ultimate Art Charging Impaired | disqualifying | the charged Art delivers poison and revives |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (heavy poison 70 / 250 + 0.25%, Art poison 300, starting-armament poison −15% / 35 buildup, vs-poisoned sizes, Poison & Rot +12% / 20 s)
- https://eldenring.wiki.gg/wiki/Nightreign:Night_of_the_Champion (thrusting-counter heal 2.5% max HP)
- https://vulkk.com/2025/09/17/nightreign-ironeye-build-guide-and-tips/ (Ironeye thrusting-counter boost +20% for 30 s; poison bow is the most cited Ironeye build) and https://www.dexerto.com/elden-ring/best-ironeye-build-in-elden-ring-nightreign-3199036
