# Guardian: Guard and Poke (ISA stack)

> Run 2026-11-05 with `python3 -I scripts/guardian_poke.py --min-isa 3`. It reuses the scoring engine in `scripts/guardian_sustain.py` and overrides the coverage and weights at the top of the script. Character reference: [characters/guardian.md](../characters/guardian.md). Sister builds: [guardian-sustain.md](guardian-sustain.md), [guardian-guard-tank.md](guardian-guard-tank.md).

**Goal:** hold guard, then answer with a single halberd light attack (a thrust) and go back to guard. Each poke opens a fresh chain, so it gets every copy of `Improved Initial Standard Attack` (ISA). ISA copies stack and multiply: 3 copies = ×1.52 on each poke.

**Requirements (your rule, enforced by the search):**
- **R01922, R00156 and R00823 fill the three normal slots.**
- Rally is required, as on every melee build (CLAUDE.md).

**The base relics decide the vessel and the ISA limit:**
- They need Blue, Yellow and a third slot that takes Blue. **Only the Guardian's Chalice (Normal B Y W) fits.** No other vessel or grail can hold all three.
- They fill the normal side and carry no ISA, so all ISA has to be on the three deep slots. **3 copies is the maximum.**

**Meta check:** I found no guide for a Guardian ISA or guard-poke build, so this is off-meta and the poke numbers are guesses. Guides still treat him as a guard-counter halberd tank. Game8 says ISA stacks and excludes jump, strong and charge attacks, so guard counters shouldn't get it. A search summary describes his light attacks as four consecutive thrusts. I only saw both through search summaries, not the pages themselves **(unverified)**.

## How many copies?

Best Chalice loadout at each ISA floor. Every row carries the base relics and rally.

| ISA floor | Total | Damage | Sustain | Utility | Penalties | Curses |
|---|---|---|---|---|---|---|
| none (0 ISA picked) | 111.3 | 15.0 | 76.8 | 21.0 | −1.5 | 1 |
| 1 | 107.8 | 18.6 | 73.2 | 18.0 | −2.0 | 2 |
| 2 | 105.7 | 22.7 | 70.9 | 20.0 | −8.0 | 4 |
| **3** | **101.2** | **27.5** | **65.2** | **9.0** | **−0.5** | **1** |

**The model doesn't pick ISA on its own.** Each deep slot that takes ISA gives up something else, mostly rally +2 and Art gauge on block. Going from 0 to 3 copies adds 12.5 damage points (about 83% more) but costs 11.6 sustain and 12.0 utility. That is 10.1 points below the pure sustain loadout, and it stays below at every poke share I tested:

| Share of damage from chain-opening pokes | 3 ISA total | 3 ISA damage | Gap to the 0-ISA loadout (111.3) |
|---|---|---|---|
| 0.3 | 96.2 | 22.5 | −15.1 |
| **0.5 (used here)** | **101.2** | **27.5** | **−10.1** |
| 0.7 | 106.2 | 32.5 | −5.1 |

So this build is a damage choice, not the top score. It is still the best way to play the guard-and-poke style you asked for, and it has only one curse.

## Best: Guardian's Chalice (Normal B Y W / Deep R B Y), 3 ISA

**Score 101.2:** damage 27.5, sustain 65.2, utility 9.0, penalties −0.5. Unlock: Guardian Remembrance 2.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal B | **R01922** Witch's Brooch | [Guardian] Slowly restores nearby allies' HP while Art is active; [Guardian] Successful guards send out shockwaves while ability is active; Vigor +3 |
| Normal Y | **R00156** Polished Luminous Scene | Attack power increased for each Night Invader defeated; Ultimate Art Auto Charge +3 |
| Normal W | **R00823** Dark Night of the Fathom (Blue) | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R01233** Deep Grand Burning Scene | [Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies *(wasted on Guardian)*; HP Recovery From Successful Guarding; **Improved Initial Standard Attack** |
| Deep B | **R01171** Deep Grand Drizzly Scene | HP Restoration upon Thrusting Counterattack +1 *(curse: Reduced Intelligence and Dexterity)*; **Improved Initial Standard Attack**; Improved Frost Resistance *(status resistance, scored 0)* |
| Deep Y | **R01324** Deep Grand Luminous Scene | [Undertaker] Improved Mind and Faith, Reduced Strength *(wasted on Guardian, so the Strength loss shouldn't apply)*; Partial HP Restoration upon Post-Damage Attacks *(base rally)*; **Improved Initial Standard Attack** |

- **ISA copies: 3** → chain-opening pokes ×1.52, about ×1.51 on total damage with Night Invader included.
- **Curses: 1.** Reduced Intelligence and Dexterity: Int is free and Dex is his C stat, so it costs little (−0.5).
- **Dormant Powers:** none, so the default halberd drop pool is unchanged.
- **`unverified_effect` flags:** none.
- **Rally:** yes, base tier on R01324.
- **Curse-free swap (95.0):** R00237 Deep Polished Drizzly Scene (Improved Initial Standard Attack; Holy Damage Negation Up) replaces R01171. Damage stays at 27.5, and sustain falls to 58.5 because you lose the thrust-counter heal.

## Alternative: Guardian's Chalice, 2 ISA + Physical Attack Up +4

**Score 104.3:** damage 29.4, sustain 73.2, utility 9.0, penalties −7.3. This is the highest-damage row I found. The normal side and R01233 and R01171 stay the same. Swap R01324 for:

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Deep Y | **R00128** Deep Polished Luminous Scene | Partial HP Restoration upon Post-Damage Attacks +2 *(curse: Reduced Vigor and Arcane)*; Physical Attack Up +4 *(curse: Reduced Intelligence and Dexterity)* |

- **ISA copies: 2** (×1.32 on pokes). Physical Attack Up +4 covers every physical hit, so at a 0.5 poke share it beats a third ISA copy, and rally +2 heals 35% more than base.
- **Curses: 3.** This **repeats Reduced Intelligence and Dexterity** (also on R01171), and Reduced Vigor and Arcane lowers his S-rank stat. The Vigor loss is a guessed −5% max HP.
- **Dormant Powers:** none. **`unverified_effect` flags:** none.
- **Use it if** you care more about damage than having three ISA copies, and can accept lower Vigor.

## Gameplay loop

1. Hold guard or Steel Guard. Each block heals (R01233), and in Steel Guard it sends out a shockwave (R01922).
2. As an attack ends, or to punish a slow one, poke once with a light attack and go straight back to guard. **Don't continue the chain:** thrusts 2 to 4 get no ISA.
3. Hit an enemy mid-attack for the thrust-counter heal (R01171). Any hit soon after taking damage recovers HP through rally (R01324).
4. Take guard counters on big openings. They get Night Invader, but not ISA.
5. Use Wings of Salvation for revives. It charges from Auto Charge +3 alone here, and it heals allies through R01922.

## Trade-offs

- **Art charges more slowly.** Utility falls from 21.0 to 9.0 because there is no `Successful guarding fills more of the Art gauge`. This is the biggest cost for a team that relies on your revive.
- **Base rally, not +2.** R01324 is the only relic I own with both ISA and rally, and its rally is base tier. A rally +2 relic costs an ISA copy.
- **Poke DPS isn't modeled.** Resetting the chain gives up the faster follow-up thrusts, and guard counters are still high damage in their own right.

## Replacing R00823

Dropping R00823 doesn't open up another vessel: R01922 and R00156 together still fit only the Chalice. The freed W slot takes any color. I scored every standard relic I own there, then re-searched the deep side for the top 25 and for every ISA or rally relic.

**R00823 still scores highest (101.2), but only narrowly.** The best swap is **R01208**, and it's worth taking if Art charge matters more to you than personal HP:

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal W | **R01208** Grand Drizzly Scene (Blue) | Successful guarding fills more of the Art gauge; HP Restoration upon Thrusting Counterattack; Physical Attack Up +2 |
| Deep B | **R00237** Deep Polished Drizzly Scene *(replaces R01171)* | Improved Initial Standard Attack; Holy Damage Negation Up |

| Loadout | Total | Damage | Sustain | Utility | Penalties | Curses |
|---|---|---|---|---|---|---|
| R00823, R01171 (best) | 101.2 | 27.5 | 65.2 | 9.0 | −0.5 | 1 |
| R01208, R01171 | 97.8 | 31.1 | 49.2 | 18.0 | −0.5 | 1 |
| **R01208, R00237** | **97.5** | **31.1** | **48.3** | **18.0** | **0.0** | **0** |
| R00823, R00237 | 95.0 | 27.5 | 58.5 | 9.0 | 0.0 | 0 |

- **R00237 pairs well with R01208.** R01208 brings its own thrust-counter heal, so R01171's +1 tier adds little, and its curse goes away for only 0.3 points. All rows have 3 ISA, no Dormant Powers and no `unverified_effect` flags.
- **The 3.4-point gap is within the guesses.** R01208 (97.8) passes R00823 if `Increased Maximum HP` is +5% rather than +10% (R00823 falls to 96.7) or if both regens are half what I guessed (97.3). It also passes if guard Art gauge is worth 13 points rather than 9 (R01208 rises to 101.8, against 101.2). If the HP and regen guesses are too low instead, R00823 pulls further ahead (105.6 at +15% max HP, 108.9 with doubled regens). Those sizes are unsourced, and the Art gauge value is hand-weighted.
- **The model slightly undervalues R00823.** Its low-HP regen also heals allies, and that part isn't scored.
- **Other W-slot options:** R00813 Night of the Fathom (Increased Maximum HP; Flask Also Heals Allies; Items confer effect to all nearby allies) scores 97.5 if you want to keep the max HP. A 4th ISA copy isn't worth it: the best is R01916 Grand Tranquil Scene (Improved Stance-Breaking when Two-Handing; Improved Initial Standard Attack; Poise +3) at 93.2, with damage 33.0 and sustain 51.7. R01640 Grand Luminous Scene (Improved Initial Standard Attack; Strength +2; Dexterity +1) has the most damage of the 4-copy options (34.5) at 92.2.

## Test in the training area

1. **Does a poke from guard count as an initial standard attack?** This is the build's main assumption. If that attack doesn't get ISA, the build loses most of its value.
2. **Can you poke out of Steel Guard, or does it drop the stance first?** I couldn't confirm this. It decides how many blocks produce shockwaves.
3. **How long do you have to pause before the next light attack opens a new chain?** This is also still open on the [Ironeye ISA build](ironeye-isa.md).
4. **Do pokes count as thrusting counterattacks?** You confirmed it for Ironeye's arrows, and the heal count assumes it here too.

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage coverage: all | 1.0 | All physical |
| Coverage: chain-opening pokes (ISA) | 0.5 | Guess, the key one. Tested at 0.3 and 0.7 above |
| Coverage: guard counter / skill / crit | 0.15 / 0.05 / 0.03 | Guesses. Guard counters are down from 0.35 on the sustain build |
| ISA size | +15% per copy, multiplies | wiki.gg. Game8 says about 12-13%, so this may be slightly high. Stacking confirmed by you |
| Night Invader | +20% | Meta anchor; copies assumed not to stack **(unverified)** |
| Shockwaves | 7 flat points | Hand-weighted, as on the sustain build |
| Thrusting-counter heal | 0.375 bars (+1: 0.495) | Guess: 15 counter hits × 2.5% / 3.3% max HP. Raised from 10 hits on the sustain build |
| HP Recovery From Successful Guarding | 0.9 bars | Guess, as on the sustain build |
| Rally | 1.5 / 1.875 / 2.025 bars | Meta anchor, highest tier only **(unverified)** |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | Guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | Guesses |
| Utility, poise, aggro, flat curse penalties | hand-weighted | As on the sustain build |

**Search:** every deep R / B / Y triple from the top 60 relics per slot, plus all ISA and rally relics, scored as a full six-slot set with the normal side fixed.

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Effects (ISA +15% on the first light attack in a chain)
- Game8's Elden Ring Nightreign guides (ISA stacks, about 12-13%, excludes jump, strong and charge attacks; seen in a search summary, exact page not confirmed)
- https://eldenring.wiki.gg/wiki/Nightreign:Guardian
- https://eldenring.wiki.gg/wiki/Nightreign:Vessels
