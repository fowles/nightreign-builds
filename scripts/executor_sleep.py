"""Executor Deep of Night loadout search: the sleep-curse engine.

Usage: python3 -I scripts/executor_sleep.py [--top N] [--vessel NAME] [--max-curses N] [--min-engine N]

The build deliberately takes `Taking Damage Causes Sleep Buildup` and
`All Resistances Down` curses. Sleep procs Tenacity (+20% attack, 20 s)
immediately, and `[Executor] Slowly Restore HP upon Ability Activation` adds a
stacking 30 s regen on every Tenacity trigger (wiki.gg). More engine curses ->
more procs -> more Tenacity uptime and more regen stacks.

Hard requirements (deep triples that miss them are dropped):
  - the `[Executor] Slowly Restore HP upon Ability Activation` effect
  - at least one `Taking Damage Causes Sleep Buildup` curse
  - at least --min-engine engine curses (Sleep + All Resistances Down)

Scoring follows scripts/guardian_sustain.py (see CLAUDE.md "Weighing effects"),
plus an ailment model computed per loadout in ailments():
  - Every hit taken adds buildup per `Taking Damage Causes X Buildup` copy
    (wiki.gg: sleep 40, poison 52, rot/blood/frost 44, madness 40, death 32);
    `X Buildup When Below Max HP` adds 2 per 0.22 s (poison) / 0.24 s (rot) at
    85% HP or lower. Each `All Resistances Down` is -80 to every resistance.
    Procs per fight = buildup / resistance, capped by an immunity cycle.
  - Every proc triggers Tenacity and a regen stack, up to MAX_TRIGGERS per
    fight, so sleep alone saturates the engine and other ailments add little.
    Tenacity is innate, so only its gain over the curse-free baseline is scored.
  - Non-sleep procs cost HP (negative heal bars inside the eHP product, reported
    as penalties). Sleep procs cost SLEEP_COST points each (helpless window).
So other `Taking Damage` curses get worse with every All Resistances Down.
"""
import argparse
import itertools
import json
import math
import re
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "mfk-relicdb.json"

POINTS_PER_PCT = 0.4  # per 1% of total damage or of effective HP (CLAUDE.md)

# Share of this build's total damage each scope covers (CLAUDE.md "Coverage").
COVERAGE = {
    "all": 1.0,
    "katana": 0.6,  # guess: regular bleed katana (the Cursed Sword gets no katana bonuses)
    "cursed": 0.3,  # guess: Cursed Sword arts and unlocked attacks
    "crit": 0.08,  # guess: ripostes/backstabs after stance breaks
    "roar": 0.03,  # guess: Beast roar attacks
}

# Reference fight model (CLAUDE.md "Fight model"). All guesses.
INCOMING = {"physical": 0.6, "fire": 0.1, "holy": 0.1, "lightning": 0.1, "magic": 0.1}
AFFINITY = ("fire", "holy", "lightning", "magic")
FIGHT_HP_BUDGET = 3.0
ALLY_FACTOR = 0.5
ALLIES = 2

# Ailment model. All guesses unless marked wiki.gg.
FIGHT_SECONDS = 150
HITS_TAKEN = 25  # hits taken per fight: this build trades hits, it doesn't deflect everything
BELOW_85_UPTIME = 0.6  # share of the fight at 85% HP or lower
BASE_RESIST = 300  # Executor's resistance to each ailment, late run (guess)
RESIST_DOWN = 80  # per All Resistances Down (wiki.gg)
RESIST_FLOOR = 40  # resistance can't drop below this (guess)
PROC_CYCLE = {"sleep": 15, "other": 20}  # seconds per proc + immunity: caps procs per fight (guess)
NATURAL_BUILDUP = 300  # enemy-inflicted buildup per fight, mixed ailments (guess: 1 proc at base resist)
NATURAL_COST = 0.08  # max-HP bars lost per enemy-inflicted proc (guess)
ALLY_SLEEP_PROCS = 0.5  # sleeps near you per fight not caused by your curse (guess)
TENACITY = 20  # % attack for 20 s per trigger (wiki.gg)
SLEEP_COST = 0.75  # points per sleep proc: a few helpless seconds (hand-weighted, unverified)
MAX_HP = 1200  # for the flat "+3 HP/s" part of the regen (guess)
REGEN_PER_PROC = (0.0027 + 3 / MAX_HP) * 30  # max-HP bars per stack (wiki.gg formula)
MAX_TRIGGERS = 10  # Tenacity/regen triggers that count per fight; overlapping procs refresh rather than add (guess)

SLEEP = "Taking Damage Causes Sleep Buildup"
ARD = "All Resistances Down"
REGEN = "[Executor] Slowly Restore HP upon Ability Activation"
# curse -> (ailment, buildup per hit) (wiki.gg)
ON_HIT = {
    SLEEP: ("sleep", 40),
    "Taking Damage Causes Poison Buildup": ("poison", 52),
    "Taking Damage Causes Rot Buildup": ("rot", 44),
    "Taking Damage Causes Blood Loss Buildup": ("blood", 44),
    "Taking Damage Causes Frost Buildup": ("frost", 44),
    "Taking Damage Causes Madness Buildup": ("madness", 40),
    "Taking Damage Causes Death Buildup": ("death", 32),
}
# curse -> (ailment, buildup per second at <= 85% HP) (wiki.gg)
BELOW_MAX = {
    "Poison Buildup When Below Max HP": ("poison", 2 / 0.22),
    "Rot Buildup When Below Max HP": ("rot", 2 / 0.24),
}
# Max-HP bars lost per proc (guess): DoT, burst, frost's damage-taken debuff, madness's FP burn.
PROC_COST = {"poison": 0.2, "rot": 0.3, "blood": 0.2, "frost": 0.25, "madness": 0.3, "sleep": 0}
RESIST_FAMILY = {
    "sleep": "Improved Sleep Resistance",
    "poison": "Improved Poison Resistance",
    "rot": "Improved Rot Resistance",
    "blood": "Improved Blood Loss Resistance",
    "frost": "Improved Frost Resistance",
    "madness": "Improved Madness Resistance",
    "death": "Improved Death Blight Resistance",
}
RESIST_SIZES = [75, 110, 130]  # wiki.gg


class Pct(float):
    """A percentage effect that combines multiplicatively in breakdown().

    Its float value is the linear (single-effect) weight, used for ranking relics.
    """

    def __new__(cls, points, kind, scope, size):
        obj = super().__new__(cls, points)
        obj.kind, obj.scope, obj.size = kind, scope, size
        return obj


def pct(sizes, scope="all"):
    """Tier weights for a damage buff of `sizes` percent over `scope`."""
    return [Pct(POINTS_PER_PCT * s * COVERAGE[scope], "damage", scope, s) for s in sizes]


def ehp(sizes):
    """Tier weights for a self max-HP-like gain: multiplies self eHP by (1 + `sizes` percent)."""
    return [Pct(POINTS_PER_PCT * s, "maxhp", "self", s) for s in sizes]


def negation(sizes, scope):
    """Tier weights for `sizes` percent damage negation of `scope` ("affinity" = all elements)."""
    share = sum(INCOMING[t] for t in AFFINITY) if scope == "affinity" else INCOMING[scope]
    return [Pct(POINTS_PER_PCT * share * (100 / (100 - s) - 1) * 100, "negation", scope, s) for s in sizes]


def heal(per_fight):
    """Tier weights for self-healing worth `per_fight` max-HP bars over the reference fight."""
    return [Pct(POINTS_PER_PCT * h / FIGHT_HP_BUDGET * 100, "heal", "self", h) for h in per_fight]


def team(sizes):
    """Tier weights for an eHP gain of `sizes` percent for each ally (added, not multiplied)."""
    return [POINTS_PER_PCT * s * ALLY_FACTOR * ALLIES for s in sizes]


def damage_points(buffs):
    """Points for a set of damage Pct buffs: multiplicative within a scope, scopes by coverage."""
    mult = {}
    for b in buffs:
        mult[b.scope] = mult.get(b.scope, 1.0) * (1 + b.size / 100)
    sub = [sc for sc in COVERAGE if sc != "all"]
    narrow = 1 - sum(COVERAGE[sc] for sc in sub) + sum(COVERAGE[sc] * mult.get(sc, 1.0) for sc in sub)
    total = mult.get("all", 1.0) * narrow
    return POINTS_PER_PCT * (total - 1) * 100


def sustain_points(effects, maxhp_extra=(), bars_extra=0.0):
    """Points for self-sustain Pct effects, combined into one effective-HP product.

    `maxhp_extra` holds additional max-HP percentages (e.g. from curses);
    `bars_extra` adds heal bars (negative for HP lost to ailment procs).
    """
    keep = {}
    maxhp = 1.0
    bars = bars_extra
    for e in effects:
        if e.kind == "negation":
            keep[e.scope] = keep.get(e.scope, 1.0) * (1 - e.size / 100)
        elif e.kind == "maxhp":
            maxhp *= 1 + e.size / 100
        else:
            bars += e.size
    for m in maxhp_extra:
        maxhp *= 1 + m / 100
    aff = keep.get("affinity", 1.0)
    taken = INCOMING["physical"] * keep.get("physical", 1.0)
    taken += sum(INCOMING[t] * aff * keep.get(t, 1.0) for t in AFFINITY)
    taken /= sum(INCOMING.values())
    return POINTS_PER_PCT * (maxhp * (1 + bars / FIGHT_HP_BUDGET) / taken - 1) * 100


def uptime(procs, seconds=20):
    """Share of the fight covered by a `seconds` buff triggered `procs` times at random."""
    return 1 - math.exp(-procs * seconds / FIGHT_SECONDS)


# category -> family -> list of weights indexed by tier (base = tier 0, "+1" = tier 1, ...)
# Stamina effects (incl. Endurance) are deliberately unweighted: nice to have at best.
# Sizes marked "guess" have no source.
CATEGORIES = {
    "damage": {
        "Physical Attack Up": pct([4, 5, 6, 10.5, 12]),  # wiki.gg, post-1.03
        "Attack power increased for each Night Invader defeated": pct([20]),  # meta-top
        "Attack power increased for each evergaol prisoner defeated": pct([5]),  # guess
        "Improved Katana Attack Power": pct([10], "katana"),  # size guessed
        "Improved Attack Power with 3+ Katana Equipped": pct([5], "katana"),  # guess incl. availability
        "Improved Melee Attack Power": pct([5]),  # wiki.gg (Will of the Balancers)
        "Improved Skill Attack Power": pct([15], "cursed"),  # applies to Cursed Sword arts since 1.03.2
        "Improved Critical Hits": pct([18, 23], "crit"),  # +1 = 23% per wiki.gg; base guessed
        "[Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking": pct([28], "cursed"),  # 35% x 0.8 uptime; negation cost in sustain
        "Taking attacks improves attack power": pct([5]),  # guess: ~10% x 0.5 uptime on a build that takes hits
        "Successive Attacks Boost Attack Power": pct([4]),  # guess
        "Improved Initial Standard Attack": pct([2]),  # guess
        "Improved Roar & Breath Attacks": pct([15], "roar"),  # guess
        "Attacks Inflict Rot when Damage is Taken": pct([4]),  # guess: enemy rot ticks after you get hit
        "Dexterity": [0, 1.5, 2, 2.5],  # Dex S
        "Arcane": [0, 1, 1.5, 2],  # Arcane S (bleed)
        "Changes compatible armament's skill to Seppuku at start of expedition": [1],
    },
    "sustain": {
        # Rally: meta anchor, non-negotiable for melee.
        "Partial HP Restoration upon Post-Damage Attacks": heal([1.5, 1.875, 2.025]),
        "[Executor] Roaring restores HP while Art is active": heal([0.3]),  # guess: ~2 roars x 15% per fight
        "[Executor] While Character Skill is active, unlocking use of cursed sword restores HP": heal([0.3]),  # guess: ~4 unlocks x (5% + 100)
        "HP Recovery From Successful Guarding": heal([0.3]),  # guess: deflects count as guards
        "HP Restoration upon Katana Attacks": heal([0.3]),  # guess
        "HP Restoration upon Thrusting Counterattack": heal([0.15, 0.2]),  # guess
        "Rot in Vicinity Causes Continuous HP Recovery": heal([0.2]),  # guess: ~1 enemy rot x (0.15% + 15)/s x 15 s
        "Continuous HP Recovery": heal([0.25]),  # guess
        "Slowly restore HP for self and nearby allies when HP is low": heal([0.25]),  # guess
        "Increased Maximum HP": ehp([10]),  # guess
        "Max HP increased for each great enemy defeated at a Great Church.": ehp([2.5]),  # guess
        "Vigor": ehp([0, 2, 3.5, 5]),  # guess: % max HP per relic tier
        "Improved Flask HP Restoration": heal([0.1]),
        "HP restored when using medicinal boluses, etc.": heal([0.03, 0.05]),  # guess
        "Flask Also Heals Allies": team([10]),  # guess
        "Defeating enemies restores HP for allies but not for self": team([2.5]),  # guess
        "Improved Physical Damage Negation": negation([8, 10.5, 12], "physical"),  # base guessed
        "Improved Affinity Damage Negation": negation([6, 10.5, 12], "affinity"),
        "Improved Damage Negation at Low HP": ehp([2.5]),  # guess
        "Improved Poise & Damage Negation When Knocked Back by Damage": [1.5],  # hand-weighted
        "Poise": [0, 1.5, 2, 2.5],  # hand-weighted
        "Fire Damage Negation Up": negation([10], "fire"),
        "Improved Fire Damage Negation": negation([10, 15, 16], "fire"),
        "Holy Damage Negation Up": negation([10], "holy"),
        "Improved Holy Damage Negation": negation([10, 15, 16], "holy"),
        "Lightning Damage Negation Up": negation([10], "lightning"),
        "Improved Lightning Damage Negation": negation([10, 15, 16], "lightning"),
        "Magic Damage Negation Up": negation([10], "magic"),
        "Improved Magic Damage Negation": negation([10, 15, 16], "magic"),
        "[Executor] Improved Dexterity and Arcane, Reduced Vigor": [0],  # +damage, -HP: a wash on a hit-trading build
        # Pure HP: Vigor +5, sized up to 12% max HP from play experience (a linear
        # read of the Vigor tiers below would say ~8%). The Arcane -13 bleed loss is
        # ignored because the sleep engine carries damage.
        "[Executor] Improved Vigor and Endurance, Reduced Arcane": ehp([12]),
    },
    "utility": {
        "Ultimate Art Auto Charge": [0, 3, 4, 5],
        "Critical hits fill more of the Art gauge": [2, 3],
        "Defeating enemies fills more of the Art gauge": [2, 3],
        "Successful guarding fills more of the Art gauge": [2, 3],
    },
}
# Weights computed per loadout in breakdown(), from the ailment model.
ENGINE = {
    REGEN: "sustain",
    "Sleep in Vicinity Improves Attack Power": "damage",  # +16/+20% for 20 s on any nearby sleep (wiki.gg)
    "Status Ailment Gauges Slowly Increase Attack Power": "damage",  # +4%/20 s while buildup is active, max 10
    **{fam: "sustain" for fam in RESIST_FAMILY.values()},
}
SLEEP_VICINITY = [16, 20]
AILMENT_GAUGE = 16  # guess: average stacks over a fight with constant buildup (x4%)
SKILL_NEGATION_COST = -4  # hand-weighted: -40% negation for 5 s after Cursed Sword attacks

WEIGHTS = {fam: w for fams in CATEGORIES.values() for fam, w in fams.items()}
CATEGORY = {fam: cat for cat, fams in CATEGORIES.items() for fam in fams}
CATEGORY.update(ENGINE)

# Attack buffs: every copy counts, across tiers and duplicates.
STACKING = {
    "Physical Attack Up",
    "Improved Katana Attack Power",
    "Improved Attack Power with 3+ Katana Equipped",
    "Improved Melee Attack Power",
    "Improved Skill Attack Power",
}
RALLY = "Partial HP Restoration upon Post-Damage Attacks"  # non-negotiable for melee (CLAUDE.md)

DORMANT_OK = {"Katana": 0}
DORMANT_BAD = -8
DORMANT_EXTRA = -3  # per Dormant Power beyond the first

DISQUALIFY = -1000
CURSE_PENALTY = {
    "Ultimate Art Charging Impaired": DISQUALIFY,  # Beast is the panic heal
    "Taking Damage Causes Death Buildup": DISQUALIFY,  # instant kill, and ARD makes it fill fast
    SLEEP: 0,  # costed per proc (SLEEP_COST)
    ARD: -1,  # costed through the ailment model; -1 for ailments it lets enemies land
    "Taking Damage Causes Poison Buildup": -2,  # plus HP per proc in the ailment model
    "Taking Damage Causes Rot Buildup": -2,
    "Taking Damage Causes Frost Buildup": -2,
    "Taking Damage Causes Blood Loss Buildup": -2,
    "Taking Damage Causes Madness Buildup": -4,  # also drains FP
    "Poison Buildup When Below Max HP": -1,
    "Rot Buildup When Below Max HP": -1,
    "Reduced Intelligence and Dexterity": -3,  # Dex S
    "Reduced Dexterity and Faith": -3,
    "Reduced Strength and Intelligence": -0.5,
    "Reduced Faith and Strength": -0.5,
    "Reduced Vigor and Arcane": -1.5,  # Arcane drives bleed; HP part in CURSE_MAXHP
    "Reduced Rune Acquisition": -1,
    "Repeated Evasions Lower Damage Negation": -0.5,
    "Reduced Damage Negation After Evading": -8,  # very bad: missed dodges hurt (CLAUDE.md)
    "Reduced Damage Negation for Flask Usages": -2.5,
    "Reduced Flask HP Restoration": -3,
    "Near Death Reduces Max HP": -2,
    "Lower Attack When Below Max HP": -3,  # -8.5% at <= 85% HP, which this build often is
    "Continuous HP Loss": -3,
}
DUP_CURSE = -1  # extra per repeat of the same curse (not applied to engine curses)
CURSE_MAXHP = {"Reduced Vigor and Arcane": -5}  # guess: mirrors Vigor +3
UNVERIFIED = -0.5

# name -> (normal colors, deep colors); "W" = any. characters/executor.md
VESSELS = {
    "Executor's Urn": ("RYY", "RYY"),
    "Executor's Goblet": ("RBG", "RBG"),
    "Executor's Chalice": ("BYW", "YYG"),
    "Soot-Covered Executor's Urn": ("RRB", "RRB"),
    "Sealed Executor's Urn": ("YYR", "GGB"),
    "Decrepit Executor's Goblet": ("RRY", "RRY"),  # unverified, single source
    "Forgotten Executor's Goblet": ("GBR", "YGW"),  # verified in game
    "Sacred Erdtree Grail": ("YYY", "YYY"),
    "Spirit Shelter Grail": ("GGG", "GGG"),
    "Giant's Cradle Grail": ("BBB", "BBB"),
    "Scadutree Grail": ("RRR", "RRR"),
}

TIER_RE = re.compile(r"^(.*?) \+(\d+)$")
DORMANT_RE = re.compile(r"^Dormant Power Helps Discover (.+)$")


def family(text):
    m = TIER_RE.match(text)
    return (m.group(1), int(m.group(2))) if m else (text, 0)


def effect_value(text):
    """(family, weight, category) for one effect; engine families weigh 0 here."""
    fam, tier = family(text)
    if fam in WEIGHTS:
        w = WEIGHTS[fam]
        return fam, w[min(tier, len(w) - 1)], CATEGORY[fam]
    return fam, 0, CATEGORY.get(fam, "utility")


class Relic:
    def __init__(self, raw):
        r = raw["relic"]
        self.id = raw["relic_id"]
        self.name = r["name"]
        self.color = r["color"][0]
        self.kind = r["kind"]
        self.effects = r["effects"]
        self.unverified = [f.split(":", 1)[1] for f in r["flags"] if f.startswith("unverified_effect:")]
        self.fams = {}  # family -> best value on this relic (non-stacking families)
        self.stack = []  # (family, value) for every copy of a STACKING family
        self.cats = {}  # family -> category
        self.engine = {}  # ENGINE family -> best tier on this relic
        self.dormant = []
        self.curses = []
        for e in self.effects:
            m = DORMANT_RE.match(e["text"])
            if m:
                self.dormant.append(m.group(1))
            else:
                fam, v, cat = effect_value(e["text"])
                self.cats[fam] = cat
                if fam in ENGINE:
                    self.engine[fam] = max(self.engine.get(fam, -1), family(e["text"])[1])
                elif fam in STACKING:
                    self.stack.append((fam, v))
                elif v > self.fams.get(fam, float("-inf")):
                    self.fams[fam] = v
            if e["curse"]:
                self.curses.append(e["curse"])
        self.is_engine = REGEN in self.engine or SLEEP in self.curses or ARD in self.curses
        self.solo = score([self])

    def fits(self, slot):
        return slot == "W" or slot == self.color


def ailments(curses, engine):
    """Ailment procs per fight for a loadout's curses and resistance effects."""
    down = RESIST_DOWN * curses.get(ARD, 0)
    buildup = {}
    for c, n in curses.items():
        if c in ON_HIT:
            a, b = ON_HIT[c]
            buildup[a] = buildup.get(a, 0) + n * b * HITS_TAKEN
        elif c in BELOW_MAX:
            a, rate = BELOW_MAX[c]
            buildup[a] = buildup.get(a, 0) + n * rate * BELOW_85_UPTIME * FIGHT_SECONDS
    procs = {}
    for a, b in buildup.items():
        tier = engine.get(RESIST_FAMILY[a], -1)
        resist = max(RESIST_FLOOR, BASE_RESIST + (RESIST_SIZES[tier] if tier >= 0 else 0) - down)
        cycle = PROC_CYCLE["sleep" if a == "sleep" else "other"]
        procs[a] = min(b / resist, FIGHT_SECONDS / cycle)
    natural = NATURAL_BUILDUP / max(RESIST_FLOOR, BASE_RESIST - down)
    return procs, natural


def breakdown(relics, report=None):
    """Score split into damage / sustain / utility / penalties; values sum to the total.

    If `report` is a dict, the ailment model's numbers are written into it.
    """
    parts = dict.fromkeys(("damage", "sustain", "utility", "penalties"), 0.0)
    pcts = []  # multiplicative effects, combined after the loop
    best = {}
    cats = {}
    curses = {}
    dormant = []
    engine = {}
    for r in relics:
        cats.update(r.cats)
        # Attack buffs and negative families (stat swaps) always apply;
        # other positives take the max.
        always = r.stack + [(fam, v) for fam, v in r.fams.items() if v < 0]
        for fam, v in always:
            if isinstance(v, Pct):
                pcts.append(v)
            else:
                parts[r.cats[fam]] += v
        for fam, v in r.fams.items():
            if v > best.get(fam, 0):
                best[fam] = v
        for fam, t in r.engine.items():
            engine[fam] = max(engine.get(fam, -1), t)
        for c in r.curses:
            curses[c] = curses.get(c, 0) + 1
        dormant += r.dormant
        parts["penalties"] += UNVERIFIED * len(r.unverified)
    for fam, v in best.items():
        if isinstance(v, Pct):
            pcts.append(v)
        else:
            parts[cats[fam]] += v
    if "[Executor] Character Skill Boosts Attack but Lowers Damage Negation While Attacking" in best:
        parts["sustain"] += SKILL_NEGATION_COST

    # Ailment engine
    procs, natural = ailments(curses, engine)
    _, natural0 = ailments({}, {})
    total = min(MAX_TRIGGERS, sum(procs.values()) + natural)
    tenacity = (1 + TENACITY / 100 * uptime(total)) / (1 + TENACITY / 100 * uptime(natural0)) - 1
    gain = [Pct(0, "damage", "all", 100 * tenacity)]
    if "Sleep in Vicinity Improves Attack Power" in engine:
        size = SLEEP_VICINITY[min(engine["Sleep in Vicinity Improves Attack Power"], 1)]
        gain.append(Pct(0, "damage", "all", size * uptime(procs.get("sleep", 0) + ALLY_SLEEP_PROCS)))
    if "Status Ailment Gauges Slowly Increase Attack Power" in engine:
        gain.append(Pct(0, "damage", "all", AILMENT_GAUGE * (1 if procs else 0.3)))
    regen = REGEN_PER_PROC * total if REGEN in engine else 0.0
    if regen:
        pcts.append(Pct(0, "heal", "self", regen))
    cost = sum(PROC_COST.get(a, 0) * p for a, p in procs.items()) + NATURAL_COST * (natural - natural0)

    dmg = [p for p in pcts if p.kind == "damage"]
    parts["damage"] += damage_points(dmg + gain)
    selfs = [p for p in pcts if p.kind != "damage"]
    clean = sustain_points(selfs)
    parts["sustain"] += clean
    cursed = [CURSE_MAXHP[c] for c, n in curses.items() if c in CURSE_MAXHP for _ in range(n)]
    parts["penalties"] += sustain_points(selfs, cursed, -cost) - clean
    parts["penalties"] -= SLEEP_COST * procs.get("sleep", 0)
    for c, n in curses.items():
        dup = 0 if c in (SLEEP, ARD) else DUP_CURSE * (n - 1)
        parts["penalties"] += CURSE_PENALTY.get(c, -2) * n + dup
    for d in dormant:
        parts["penalties"] += DORMANT_OK.get(d, DORMANT_BAD)
    parts["penalties"] += DORMANT_EXTRA * max(0, len(dormant) - 1)
    if report is not None:
        report.update(
            sleep=curses.get(SLEEP, 0),
            ard=curses.get(ARD, 0),
            procs={a: round(p, 1) for a, p in procs.items()},
            natural=round(natural, 1),
            tenacity_uptime=round(uptime(total), 2),
            tenacity_gain_pct=round(100 * tenacity, 1),
            regen_bars=round(regen, 2),
            hp_lost_bars=round(cost, 2),
        )
    return parts


def score(relics):
    return sum(breakdown(relics).values())


def format_parts(parts):
    return "  ".join(f"{k} {v:.1f}" for k, v in parts.items())


def load():
    data = json.loads(DB.read_text())
    return [Relic(r) for r in data["relics"] if r["status"] == "active"]


def curse_count(relics):
    return sum(len(r.curses) for r in relics)


def engine_count(relics):
    return sum(r.curses.count(SLEEP) + r.curses.count(ARD) for r in relics)


def engine_ok(deep, min_engine):
    """Hard requirements on the deep side: regen, a Sleep curse, enough engine curses."""
    return (
        any(REGEN in r.engine for r in deep)
        and any(SLEEP in r.curses for r in deep)
        and engine_count(deep) >= min_engine
    )


def top_triples(pool, colors, per_slot, keep, max_curses, require=None):
    """Best relic triples (by triple score) for the given slot colors.

    Keeps the best `keep` / 2 triples with rally and the best `keep` / 2
    without. A side-only score credits rally fully even when the other side
    already carries a better copy, so a single list fills with rally triples
    and drops strong rally-less ones (it missed R01180 for R01898).
    Engine relics are always candidates, whatever their solo score.
    """
    pool = [r for r in pool if len(r.curses) <= max_curses]
    cands = []
    for c in colors:
        fit = sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)
        cands.append(fit[:per_slot] + [r for r in fit[per_slot:] if r.is_engine])
    seen = set()
    out = []
    for combo in itertools.product(*cands):
        ids = frozenset(r.id for r in combo)
        if len(ids) < 3 or ids in seen or curse_count(combo) > max_curses:
            continue
        if require and not require(combo):
            continue
        seen.add(ids)
        out.append((score(combo), combo))
    out.sort(key=lambda t: -t[0])
    with_rally = [t for t in out if any(RALLY in r.fams for r in t[1])]
    without = [t for t in out if not any(RALLY in r.fams for r in t[1])]
    return with_rally[: keep // 2] + without[: keep // 2]


def search(relics, normal, deep, per_slot, keep, max_curses=99, min_engine=1):
    std = [r for r in relics if r.kind == "standard" and r.solo > DISQUALIFY / 2]
    dp = [r for r in relics if r.kind == "deep" and r.solo > DISQUALIFY / 2]
    nt = top_triples(std, normal, per_slot, keep, max_curses)
    dt = top_triples(dp, deep, per_slot, keep, max_curses, lambda d: engine_ok(d, min_engine))
    results = []
    for _, n in nt:
        for _, d in dt:
            if curse_count(n + d) <= max_curses:
                results.append((score(n + d), n, d))
    results.sort(key=lambda t: -t[0])
    return results


def describe(total, n, d, normal, deep):
    report = {}
    lines = [f"score {total:.1f}  ({format_parts(breakdown(n + d, report))})"]
    all_curses = []
    dormant = []
    flags = []
    for label, colors, rs in (("normal", normal, n), ("deep", deep, d)):
        for slot, r in zip(colors, rs):
            effs = "; ".join(e["text"] + (f" [curse: {e['curse']}]" if e["curse"] else "") for e in r.effects)
            lines.append(f"  {label} {slot}: {r.id} {r.name} ({r.color}) solo={r.solo:.1f} :: {effs}")
            all_curses += r.curses
            dormant += r.dormant
            flags += [f"{r.id}: {u}" for u in r.unverified]
    rally = [r.id for r in n + d if RALLY in r.fams]
    lines.append(f"  engine: {report}")
    lines.append(f"  rally: {rally or 'MISSING (non-negotiable for melee)'}")
    lines.append(f"  curses ({len(all_curses)}): {all_curses}")
    lines.append(f"  dormant: {dormant or 'none'}")
    lines.append(f"  unverified: {flags or 'none'}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--vessel")
    ap.add_argument("--per-slot", type=int, default=60)
    ap.add_argument("--keep", type=int, default=1500)
    ap.add_argument("--max-curses", type=int, default=99, help="cap on total curses per loadout")
    ap.add_argument("--min-engine", type=int, default=1, help="minimum Sleep + All Resistances Down curses")
    args = ap.parse_args()
    relics = load()
    summary = []
    for name, (normal, deep) in VESSELS.items():
        if args.vessel and args.vessel != name:
            continue
        res = search(relics, normal, deep, args.per_slot, args.keep, args.max_curses, args.min_engine)
        if not res:
            print(f"=== {name}  normal {normal} / deep {deep}: no loadout meets the engine requirements\n")
            continue
        best = res[0][1] + res[0][2]
        has_rally = any(RALLY in r.fams for r in best)
        summary.append((res[0][0], name, breakdown(best), has_rally, engine_count(best)))
        print(f"=== {name}  normal {normal} / deep {deep}")
        for total, n, d in res[: args.top]:
            print(describe(total, n, d, normal, deep))
        print()
    print("=== summary")
    for s, name, parts, has_rally, eng in sorted(summary, key=lambda t: -t[0]):
        print(f"  {s:6.1f}  {name:30}  engine {eng}  {format_parts(parts)}" + ("" if has_rally else "  NO RALLY"))


if __name__ == "__main__":
    main()
