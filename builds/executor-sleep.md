# Executor: Sleep Engine

> Generated 2026-10-31 with `scripts/executor_sleep.py --min-engine 3`. Character reference: [characters/executor.md](../characters/executor.md).

**Goal:** a curse build that *wants* to fall asleep. Each Sleep proc triggers Tenacity right away (+20% attack and +8 stamina/s for 20 s, wiki.gg). `[Executor] Slowly Restore HP upon Ability Activation` then adds a stacking regen on every trigger: (0.27% max HP + 3) per second for 30 s (wiki.gg). `Taking Damage Causes Sleep Buildup` (+40 sleep per hit taken) and `All Resistances Down` (−80 to every resistance) are the fuel. The more copies you carry, the more procs you get.

**Requirements you set (enforced by the search):**
- the `[Executor] Slowly Restore HP upon Ability Activation` effect
- at least one `Taking Damage Causes Sleep Buildup`
- 3+ engine curses (Sleep + All Resistances Down) via `--min-engine 3`. You said 4–5 is ideal.
- caution with other `Taking Damage Causes X` curses. The model makes them cost HP on every proc, and each All Resistances Down makes them proc more.

## Inventory ceiling: 3 engine curses

- **4–5 engine curses is impossible with what you own.** Engine curses only appear on deep relics, and every one of your 85 Sleep/ARD relics carries exactly one (40 Sleep, 45 ARD). Three deep slots means at most 3.
- **R00521 is the only relic with both the regen and a Sleep curse.** Any 3-engine loadout needs it, so it needs a blue (or white) deep slot. That rules out the Urn, the Chalice, the Erdtree Grail and the Scadutree Grail.
- Watch for a deep relic that rolls two engine curses (e.g. Sleep + ARD on different effects). That's the only way to reach 4.

## Results

Best 3-engine loadout per vessel:

| Vessel | Total | Damage | Sustain | Utility | Penalties |
|---|---|---|---|---|---|
| Forgotten Executor's Goblet | 96.8 | 4.8 | 102.9 | 0.0 | −10.9 |
| Soot-Covered Executor's Urn | 96.2 | 22.2 | 85.1 | 0.0 | −11.0 |
| Executor's Goblet | 95.3 | 21.5 | 87.7 | 0.0 | −13.9 |
| Sealed Executor's Urn | 94.2 | 13.7 | 90.4 | 5.0 | −14.9 |
| Giant's Cradle Grail | 88.8 | 22.9 | 72.1 | 2.0 | −8.3 |

**Model disagreement:** without the 3-engine floor, the model preferred a 2-engine Executor's Goblet (91.6 before the respec reweight and search fix; not re-run since). It trades R00521 for R01060 (regen without a Sleep curse). The trigger cap (below) makes the 3rd curse look redundant. You've played this build and say more copies is better, so I treated the floor as a hard requirement. If 3 copies really do outperform, `MAX_TRIGGERS` and `PROC_CYCLE["sleep"]` are probably too low.

Utility, poise, the per-sleep cost and the respec relic are hand-weighted.

> **Re-scored 2026-10-31:**
> - `Reduced Damage Negation After Evading` is now −8 instead of −1, per the updated CLAUDE.md curse rules: a failed roll costs far more damage. The old top pick used R00958, which carries that curse, so it's gone.
> - `[Executor] Improved Vigor and Endurance, Reduced Arcane` is now worth a 12% max-HP gain instead of 0.5 points. Its value is purely HP: Vigor +5, sized up from a linear ~8% to 12% because you find the extra HP very helpful in play. The Arcane −13 bleed loss is ignored, because the sleep engine carries the damage. **R00880** (standard, red, no curses) is in every top loadout. Your other two copies don't fit: R00396 (deep, blue) would take R00521's slot, and R01419 carries Death Buildup.
> - **Search fix:** normal-slot triples were shortlisted by their own score, which credits base rally in full even though the deep +1 copy makes it worthless. Rally-less triples fell off the shortlist, so R01898 (rally, Vigor +2, Poise +2) kept getting picked over better relics, as you spotted. The script now shortlists triples with and without rally separately. Every vessel gained 4–12 points.

## Best: Forgotten Executor's Goblet (Normal G B R / Deep Y G W)

**Score 96.8:** damage 4.8, sustain 102.9, utility 0.0, penalties −10.9. Slot colors verified in game.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal G | **R01042** Grand Tranquil Scene | [Executor] Roaring restores HP while Art is active; Improved Damage Negation at Low HP; Lightning Attack Power Up +1 *(out of focus)* |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Normal R | **R00880** Grand Burning Scene | **[Executor] Improved Vigor and Endurance, Reduced Arcane**; Vigor +3; Endurance +3 *(stamina: worth 0)* |
| Deep Y | **R00206** Deep Polished Luminous Scene | [Guardian] Character Skill Boosts Damage Negation of Nearby Allies *(wasted on Executor)*; Improved Affinity Damage Negation +1 *(curse: **Taking Damage Causes Sleep Buildup**)* |
| Deep G | **R00462** Deep Polished Tranquil Scene | Partial HP Restoration upon Post-Damage Attacks +1 *(curse: Reduced Damage Negation for Flask Usages)*; Improved Physical Damage Negation +1 *(curse: **All Resistances Down**)* |
| Deep W | **R00521** Deep Polished Drizzly Scene (Blue) | **[Executor] Slowly Restore HP upon Ability Activation**; Attack power up when facing poison-afflicted enemy +1 *(out of focus; curse: **Taking Damage Causes Sleep Buildup**)* |

- **Engine:** 2 Sleep + 1 ARD = 3. Sleep resistance 300 → 220 (guess), so a proc every ~2.75 hits. About 9 sleeps a fight. With enemy ailments, triggers hit the cap of 10. Tenacity uptime is ~74% (+11.9% damage over a curse-free Executor), and regen heals ~1.56 max-HP bars per fight.
- **Curses: 4.**
  - Sleep ×2 and ARD ×1: the engine.
  - Reduced Damage Negation for Flask Usages: −2.5. Regen and rally should cover most of your healing, but flasking mid-combo now hurts more.
  - No other `Taking Damage Causes X` curses. No Death, no Ultimate Art Charging Impaired.
- **Dormant Powers:** none.
- **`unverified_effect` flags:** none.
- **Rally:** yes (R00462 +1).
- **Damage swap for the green normal slot (96.5, a tie):** **R01101** Grand Tranquil Scene (Improved Frenzied Flame Incantations *(out of focus)*; Attack power increased for each Night Invader defeated; Strength +2). It trades the roar heal and low-HP negation for the Night Invader stack (damage 13.7, sustain 93.6). Take this if you'd rather kill faster.

## Alternative: Soot-Covered Executor's Urn (Normal R R B / Deep R R B)

**Score 96.2:** damage 22.2, sustain 85.1, utility 0.0, penalties −11.0. This one runs **3 Sleep curses and no All Resistances Down**.

| Slot | Relic | Effects (curse attached) |
|---|---|---|
| Normal R | **R00880** Grand Burning Scene | **[Executor] Improved Vigor and Endurance, Reduced Arcane**; Vigor +3; Endurance +3 *(stamina: worth 0)* |
| Normal R | **R00844** The Night of Dregs | Status Ailment Gauges Slowly Increase Attack Power; Attacks Inflict Rot when Damage is Taken; Rot in Vicinity Causes Continuous HP Recovery |
| Normal B | **R00823** Dark Night of the Fathom | Increased Maximum HP; Continuous HP Recovery; Slowly restore HP for self and nearby allies when HP is low |
| Deep R | **R01478** Deep Grand Burning Scene | Partial HP Restoration upon Post-Damage Attacks +1 *(curse: **Taking Damage Causes Sleep Buildup**)*; Improved Lightning Damage Negation +2 *(curse: Reduced Strength and Intelligence)*; Improved Blood Loss Resistance +1 |
| Deep R | **R01605** Deep Grand Burning Scene | [Wylder] Character Skill inflicts Blood Loss *(wasted on Executor)*; Attack power up when facing frostbite-afflicted enemy +2 *(out of focus; curse: **Taking Damage Causes Sleep Buildup**)*; **Sleep in Vicinity Improves Attack Power +1** *(curse: Reduced Dexterity and Faith)* |
| Deep B | **R00521** Deep Polished Drizzly Scene | **[Executor] Slowly Restore HP upon Ability Activation**; Attack power up when facing poison-afflicted enemy +1 *(out of focus; curse: **Taking Damage Causes Sleep Buildup**)* |

- **Engine:** 3 Sleep, 0 ARD. 120 sleep per hit against 300 resistance means a proc every ~2.5 hits, so ~10 sleeps a fight (the cap). Without ARD, enemy-inflicted bleed, frost and poison don't land any more often than normal. `Sleep in Vicinity Improves Attack Power +1` (+20%, ~72% uptime) and The Night of Dregs' ailment-gauge ramp carry the damage.
- **Curses: 5.** The three Sleep curses, plus:
  - Reduced Dexterity and Faith: −3. Dex is an S stat.
  - Reduced Strength and Intelligence: near-free.
- **Dormant Powers:** none. **`unverified_effect` flags:** none. **Rally:** yes (R01478 +1).
- **Executor's Goblet (95.3)** is the third option: R00880 / R00823 / R01101 normal; R01605 / R00521 / R00462 deep. Same engine as the Forgotten Goblet plus Sleep in Vicinity and Night Invader, with Reduced Dexterity and Faith (5 curses).

## Gameplay loop

1. Play the katana aggressively and trade hits. Rally heals back most of what you take if you swing right after getting hit. The respec's extra Vigor makes every hit cost a smaller share of your bar.
2. Every ~3 hits you fall asleep. Tenacity triggers at once (+20% attack), a 30 s regen stack starts, and with R01605, Sleep in Vicinity adds +20%.
3. Regen stacks overlap through a fight, on top of the constant regen from R00823.
4. Beast is still the panic button, and on the Forgotten Goblet each roar heals 15% for you and nearby allies. No loadout carries Ultimate Art Charging Impaired.

## Trade-offs and unknowns

- **How long a sleeping player is helpless isn't documented** on wiki.gg. The model charges 0.75 points per sleep (−6.8 to −7.5 per fight). If sleep is short and Tenacity triggers on contact, the cost is lower and more engine curses score better.
- **Do deflected or guarded hits add buildup?** Unverified. One low-authority source says `Taking Damage` curses don't proc while guarding. If that's true, deflecting with the Cursed Sword starves the engine, and this build should trade hits rather than deflect.
- **Regen stacking cap:** wiki.gg says repeated triggers stack but gives no cap. The model counts at most 10 triggers per fight (`MAX_TRIGGERS`). That cap is why the 3rd engine curse gains little in the model.
- **The respec weight comes from play, not a source.** It's pure HP, modeled as 12% max HP for Vigor +5. If that's right, the Vigor +N tiers (+3 ≈ 5%) are probably undervalued too, and that affects every build script.
- **The Forgotten Goblet build is almost all sustain:** 4.8 damage points, all from Tenacity. The Soot-Covered Urn (22.2) and the R01101 swap (13.7) trade some sustain for damage. Arcane −13 also weakens bleed on the katana.

## Model inputs

| Input | Value | Note |
|---|---|---|
| Damage coverage: all / katana / cursed sword / crit / roar | 1.0 / 0.6 / 0.3 / 0.08 / 0.03 | guesses except "all" |
| Incoming damage mix | physical 0.6; fire, holy, lightning, magic 0.1 each | guess |
| Fight HP budget / ally factor | 3.0 bars / 0.5 × 2 allies | guess |
| Fight length / hits taken | 150 s / 25 hits | guess |
| Base ailment resistance | 300; floor 40 | guess |
| Buildup per hit | sleep 40, poison 52, rot/blood/frost 44, madness 40, death 32 | wiki.gg |
| All Resistances Down | −80 to every resistance | wiki.gg |
| Proc cycle (proc + immunity) | sleep 15 s, others 20 s | guess |
| Tenacity / regen triggers counted per fight | max 10 | guess |
| Regen per trigger | (0.27% + 3/1200) × 30 s ≈ 0.156 bars | wiki.gg formula, max HP 1200 guessed |
| HP lost per non-sleep proc | poison 0.2, rot 0.3, blood 0.2, frost 0.25, madness 0.3 bars | guess |
| Sleep cost | 0.75 points per sleep | hand-weighted |
| Status Ailment Gauges | +16% average | guess (+4% per 20 s, max 10 stacks, per wiki.gg) |

## Sources

- https://eldenring.wiki.gg/wiki/Nightreign:Executor (Tenacity, Sleep triggers immediately, regen formula and stacking)
- https://eldenring.wiki.gg/wiki/Nightreign:Effects (curse buildup values, All Resistances Down −80, Sleep in Vicinity +16/+20%, Status Ailment Gauges)
- https://www.switchbladegaming.com/elden-ring-nightreign/status-effects-guide-2/ (claims `Taking Damage` curses don't proc while guarding; low authority)
- No community write-up of a sleep Executor turned up in searches (Reddit, guides).
