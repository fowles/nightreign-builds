"""Ironeye Deep of Night loadout search: poison mark, initial standard attack, and affinity builds.

Usage: python3 -I scripts/ironeye.py --build {poison,isa,affinity} [--switch-add PCT] [--top N]
       [--vessel NAME] [--max-curses N] [--min-isa N] [--no-poison-source]

Every build requires `[Ironeye] +1 additional Character Skill use` (your rule).
  - poison:   also requires `[Ironeye] Character Skill Inflicts Heavy Poison Damage on
              Poisoned Enemies` and a second poison source (`Starting armament inflicts
              poison` or `[Ironeye] Art Charge Activation Adds Poison Effect`). A poison model (poison_model()) turns the loadout's
              poison sources into a poison uptime, then scores the DoT, the Marking
              burst and the "vs poisoned" buffs from it.
  - isa:      stacks `Improved Initial Standard Attack` (+15% to the first light attack in
              a chain, wiki.gg) on a tap-fire bow. Every copy multiplies **(unverified)**.
  - affinity: also requires R00860 Night of the Lord (the only `Switching Weapons Adds an
              Affinity Attack` relic you own). Swap bows often: each swap adds random-element
              damage for 10 s, which affinity buffs boost. An elemental starting bow
              (`Starting armament deals <E> damage`) is optional and scored if carried.

Damage is modeled as disjoint slices of your total damage, each with tags (bow, phys,
first, start, skill, aff, holy, ...). A buff multiplies every slice carrying its tag
(CLAUDE.md coverage formula, generalized so scopes may overlap). Flat damage (poison DoT,
Marking bursts) is added as points. Sustain follows scripts/executor_sleep.py.
"""
import argparse
import itertools
import json
import re
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "mfk-relicdb.json"

POINTS_PER_PCT = 0.4  # per 1% of total damage or of effective HP (CLAUDE.md)
ELEMENTS = ("fire", "holy", "lightning", "magic")

# Reference fight model (CLAUDE.md "Fight model"). All guesses.
INCOMING = {"physical": 0.6, "fire": 0.1, "holy": 0.1, "lightning": 0.1, "magic": 0.1}
FIGHT_HP_BUDGET = 3.0
ALLY_FACTOR = 0.5
ALLIES = 2

FIGHT_SECONDS = 150
MARK_COOLDOWN = 10  # s (wiki.gg); the mandatory +1 use banks a 2nd charge but doesn't speed it up
BASE_MARKS = FIGHT_SECONDS / MARK_COOLDOWN

# Per-build damage profile. All guesses.
#   arrows: share of total damage from bow light attacks
#   first:  share of those arrows that are the first light attack in a chain (ISA)
#   start:  share of those arrows fired from the starting bow
#   switch: uptime of `Switching Weapons Boosts Attack Power` (+10% for 10 s after a swap)
#   other_aff: elemental share of arrows from found (non-starting) bows
BUILDS = {
    "poison": dict(arrows=0.70, first=0.2, start=0.7, switch=0.15, other_aff=0.0, ult=0.12, skill=0.10, crit=0.05, melee=0.03),
    "isa": dict(arrows=0.75, first=0.6, start=0.5, switch=0.15, other_aff=0.0, ult=0.12, skill=0.08, crit=0.05, melee=0.0),
    "affinity": dict(arrows=0.70, first=0.2, start=0.6, switch=0.6, other_aff=0.4, ult=0.12, skill=0.10, crit=0.05, melee=0.03),
}
ELEMENT_SPLIT = 0.5  # elemental share of an infused starting bow's arrows (guess)
SWITCH_ADD = 4  # default --switch-add: % extra damage while `Switching Weapons Adds an Affinity Attack`
# is up. wiki.gg (summarized, unverified) says +12 flat; on ~300 AR that's ~4% (guess)

# Poison model (poison build only). All guesses unless marked wiki.gg.
POISON_UPTIME = {"weapon": 0.55, "mark": 0.25, "art": 0.15}  # each source alone, at BASE_MARKS
POISON_DOT = 10  # % of your fight damage from poison ticks at 100% uptime
MARK_BURST = 3  # % of your fight damage per heavy-poison burst: 250 + 0.25% max HP (wiki.gg) ~ 310
# on a ~25k HP Deep of Night boss, against ~8-10k damage from you per fight (guess)

ISA = "Improved Initial Standard Attack"
SKILL_USE = "[Ironeye] +1 additional Character Skill use"
HEAVY_POISON = "[Ironeye] Character Skill Inflicts Heavy Poison Damage on Poisoned Enemies"
ART_POISON = "[Ironeye] Art Charge Activation Adds Poison Effect"
WEAPON_POISON = "Starting armament inflicts poison"
SWITCH_ADDS = "Switching Weapons Adds an Affinity Attack"
SWITCH_BOOST = "Switching Weapons Boosts Attack Power"
CDR = "Character Skill Cooldown Reduction"
CDR_SIZES = [0, 5, 7.5, 10]  # % shorter cooldown, +1..+3 (wiki.gg)
VS_POISON = "Attack power up when facing poison-afflicted enemy"
VS_POISON_SIZES = [10, 16, 20]  # wiki.gg
POISON_VICINITY = "Poison & Rot in Vicinity Increases Attack Power"  # +12% for 20 s (wiki.gg)
RALLY = "Partial HP Restoration upon Post-Damage Attacks"
START_RE = re.compile(r"^Starting armament (?:inflicts (.+)|deals (.+) damage)$")
NIGHT_OF_THE_LORD = "R00860"


class Pct(float):
    """A percentage effect that combines multiplicatively in breakdown().

    Its float value is the linear (single-effect) weight, used for ranking relics.
    """

    def __new__(cls, points, kind, scope, size):
        obj = super().__new__(cls, points)
        obj.kind, obj.scope, obj.size = kind, scope, size
        return obj


def pct(sizes, scope="all"):
    """Tier weights for a damage buff of `sizes` percent on slices tagged `scope`."""
    return [Pct(POINTS_PER_PCT * s * 0.5, "damage", scope, s) for s in sizes]


def ehp(sizes):
    """Tier weights for a self max-HP-like gain: multiplies self eHP by (1 + `sizes` percent)."""
    return [Pct(POINTS_PER_PCT * s, "maxhp", "self", s) for s in sizes]


def negation(sizes, scope):
    """Tier weights for `sizes` percent damage negation of `scope` ("affinity" = all elements)."""
    share = sum(INCOMING[t] for t in ELEMENTS) if scope == "affinity" else INCOMING[scope]
    return [Pct(POINTS_PER_PCT * share * (100 / (100 - s) - 1) * 100, "negation", scope, s) for s in sizes]


def heal(per_fight):
    """Tier weights for self-healing worth `per_fight` max-HP bars over the reference fight."""
    return [Pct(POINTS_PER_PCT * h / FIGHT_HP_BUDGET * 100, "heal", "self", h) for h in per_fight]


def team(sizes):
    """Tier weights for an eHP gain of `sizes` percent for each ally (added, not multiplied)."""
    return [POINTS_PER_PCT * s * ALLY_FACTOR * ALLIES for s in sizes]


def categories(build):
    """category -> family -> tier weights, for one build.

    Stamina effects (incl. Endurance) are deliberately unweighted: nice to have at best.
    Out-of-focus effects are absent (worth 0). Sizes marked "guess" have no source.
    """
    p = BUILDS[build]
    damage = {
        "Physical Attack Up": pct([4, 5, 6, 10.5, 12], "phys"),  # wiki.gg, post-1.03
        "Attack power increased for each Night Invader defeated": pct([20]),  # meta-top
        "Attack power increased for each evergaol prisoner defeated": pct([5]),  # guess
        ISA: pct([15], "first"),  # wiki.gg; bows count as light attacks (unverified)
        "Improved Bow Attack Power": pct([6], "bow"),  # guess: nerfed in 1.03.2, no post-nerf number
        "Improved Attack Power with 3+ Bows Equipped": pct([4], "bow"),  # guess: ~8% x 0.5 availability
        "Improved Critical Hits": pct([18, 23], "crit"),  # wiki.gg
        SWITCH_BOOST: pct([10 * p["switch"]]),  # wiki.gg: +10% for 10 s
        "[Ironeye] Extends duration of weak point": pct([2]),  # guess: +20% mark uptime x 10%
        "Dexterity": [0, 1.5, 2, 2.5],  # Dex A
        # Stat swaps: the Dex loss is a bow-damage cut (guesses: Dex -9 ~ -4%, -13 ~ -6%).
        "[Ironeye] Improved Arcane, Reduced Dexterity": pct([-4], "bow"),
        "[Ironeye] Improved Vigor and Strength, Reduced Dexterity": pct([-6], "bow"),
        WEAPON_POISON: pct([-15], "start"),  # wiki.gg: starting weapon -15% damage
    }
    if build == "affinity":
        damage.update({
            "Improved Affinity Attack Power": pct([5, 8, 10], "aff"),  # wiki.gg
            "Boosts Attack Power of Added Affinity Attacks": pct([10], "added"),  # wiki.gg
            **{f"{e.title()} Attack Power Up": pct([4.5, 5.5, 6.5, 10.5, 12], e) for e in ELEMENTS},  # wiki.gg
        })
    if build == "poison":
        damage["Arcane"] = [0, 0.5, 0.75, 1]  # guess: poison buildup on Arcane-scaling bows
    sustain = {
        # Rally applies to bows since 1.02. Ranged takes fewer hits, so less than the melee
        # anchor of 1.5 bars (guess).
        RALLY: heal([1.0, 1.25, 1.35]),
        "Continuous HP Recovery": heal([0.25]),  # guess
        "Slowly restore HP for self and nearby allies when HP is low": heal([0.25]),  # guess
        "Increased Maximum HP": ehp([10]),  # guess
        "Max HP increased for each great enemy defeated at a Great Church.": ehp([2.5]),  # guess
        "Vigor": ehp([0, 2, 3.5, 5]),  # guess: % max HP per relic tier
        "[Ironeye] Improved Vigor and Strength, Reduced Dexterity": ehp([8]),  # guess: Vigor +5
        "Improved Flask HP Restoration": heal([0.1]),
        "HP restored when using medicinal boluses, etc.": heal([0.03, 0.05]),  # guess
        "Flask Also Heals Allies": team([10]),  # guess
        "Defeating enemies restores HP for allies but not for self": team([2.5]),  # guess
        "Improved Physical Damage Negation": negation([8, 10.5, 12], "physical"),  # base guessed
        "Improved Affinity Damage Negation": negation([6, 10.5, 12], "affinity"),
        "Improved Damage Negation at Low HP": ehp([2.5]),  # guess
        "Improved Poise & Damage Negation When Knocked Back by Damage": [1],  # hand-weighted
        "Poise": [0, 1, 1.5, 2],  # hand-weighted: ranged, poise matters less
        **{f"{e.title()} Damage Negation Up": negation([10], e) for e in ELEMENTS},
        **{f"Improved {e.title()} Damage Negation": negation([10, 15, 16], e) for e in ELEMENTS},
    }
    art = 1.5 if build == "poison" else 1.0  # the charged Art carries 300 poison
    utility = {
        SKILL_USE: [2],  # mandatory; hand-weighted so it shows up in the split
        "[Ironeye] Extends duration of weak point": [0.8],  # allies' share of the mark uptime
        "Ultimate Art Auto Charge": [x * art for x in (0, 3, 4, 5)],
        "Critical hits fill more of the Art gauge": [2 * art, 3 * art],
        "Defeating enemies fills more of the Art gauge": [2 * art, 3 * art],
        "FP Restoration upon Bow Attacks": [1],  # FP for bow skills (Rain of Arrows etc.)
        "Reduced FP Consumption": [0.5],
        "Increased Maximum FP": [0.5],
        "Increased rune acquisition for self and allies": [0.5],
    }
    return {"damage": damage, "sustain": sustain, "utility": utility}


# Attack buffs: every copy counts, across tiers and duplicates (CLAUDE.md).
STACKING = {
    "Physical Attack Up",
    "Improved Affinity Attack Power",
    ISA,
    "Improved Bow Attack Power",
    "Improved Attack Power with 3+ Bows Equipped",
    *(f"{e.title()} Attack Power Up" for e in ELEMENTS),
}
# Computed per loadout in breakdown(): poison engine, cooldown, conditional buffs.
ENGINE = {HEAVY_POISON, ART_POISON, CDR, VS_POISON, POISON_VICINITY, SWITCH_ADDS}

DORMANT_OK = {"Bows": 0, "Greatbows": 0}
DORMANT_BAD = -8
DORMANT_EXTRA = -3  # per Dormant Power beyond the first
START_CONFLICT = -4  # per starting-armament affinity beyond the one the build wants (they don't stack)
START_OFF = -1  # a starting-armament affinity on a build that wants none

DISQUALIFY = -1000
CURSE_PENALTY = {
    # Single Shot is the revive; disqualifying on poison (see breakdown()).
    "Ultimate Art Charging Impaired": -10,
    "Taking Damage Causes Death Buildup": -5,  # instant kill; ranged takes fewer hits
    "Taking Damage Causes Sleep Buildup": -4,
    "Taking Damage Causes Madness Buildup": -3,
    "Taking Damage Causes Poison Buildup": -2,
    "Taking Damage Causes Rot Buildup": -2,
    "Taking Damage Causes Frost Buildup": -2,
    "Taking Damage Causes Blood Loss Buildup": -2,
    "Poison Buildup When Below Max HP": -1,
    "Rot Buildup When Below Max HP": -1,
    "All Resistances Down": -2.5,
    "Reduced Intelligence and Dexterity": -3,  # Dex A
    "Reduced Dexterity and Faith": -3,
    "Reduced Strength and Intelligence": -0.5,  # Str C, Int D
    "Reduced Faith and Strength": -0.5,
    "Reduced Vigor and Arcane": -2,  # Arc B; HP part in CURSE_MAXHP
    "Reduced Rune Acquisition": -1,
    "Repeated Evasions Lower Damage Negation": -0.5,
    "Reduced Damage Negation After Evading": -8,  # very bad: missed dodges hurt (CLAUDE.md)
    "Reduced Damage Negation for Flask Usages": -2.5,
    "Reduced Flask HP Restoration": -3,
    "Near Death Reduces Max HP": -2,
    "Lower Attack When Below Max HP": -3,
    "Continuous HP Loss": -3,
}
DUP_CURSE = -1  # extra per repeat of the same curse
ARD_AMPLIFY = -1  # per (Taking Damage curse x All Resistances Down) pair: -80 resistance makes them proc more
CURSE_MAXHP = {"Reduced Vigor and Arcane": -5}  # guess: mirrors Vigor +3
UNVERIFIED = -0.5

# name -> (normal colors, deep colors); "W" = any. characters/ironeye.md
VESSELS = {
    "Ironeye's Urn": ("YGG", "YGG"),
    "Ironeye's Goblet": ("RBY", "RBY"),
    "Ironeye's Chalice": ("RGW", "RRG"),
    "Soot-Covered Ironeye's Urn": ("BYY", "BYY"),  # unverified
    "Sealed Ironeye's Urn": ("GGY", "BBR"),
    "Decrepit Ironeye's Goblet": ("BBG", "BGG"),  # deep unverified
    "Forgotten Ironeye's Goblet": ("YBR", "YGW"),
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


class Model:
    """Weights and rules for one build."""

    def __init__(self, build, switch_add=SWITCH_ADD):
        self.build, self.switch_add = build, switch_add
        self.p = BUILDS[build]
        self.cats = categories(build)
        self.weights = {}
        self.category = {}
        # A family may sit in two categories (stat swaps, weak point): keep both parts.
        for cat, fams in self.cats.items():
            for fam, w in fams.items():
                self.weights.setdefault(fam, []).append((cat, w))
        self.want = {"poison": "poison", "affinity": "element", "isa": None}[build]  # starting-armament affinity

    def slices(self, start_element):
        """(share, tags) slices of total damage. `start_element` infuses the starting bow."""
        p = self.p
        out = []
        for first in (True, False):
            f = p["first"] if first else 1 - p["first"]
            for start in (True, False):
                s = p["start"] if start else 1 - p["start"]
                share = p["arrows"] * f * s
                tags = {"bow"} | ({"first"} if first else set()) | ({"start"} if start else set())
                if start and start_element:
                    aff = ELEMENT_SPLIT
                    eltags = {"aff", "added", start_element}
                elif not start and p["other_aff"]:
                    aff = p["other_aff"]
                    eltags = {"aff"}  # random elements from drops
                else:
                    aff, eltags = 0, set()
                if aff:
                    out.append((share * aff, frozenset(tags | eltags)))
                out.append((share * (1 - aff), frozenset(tags | {"phys"})))
        out += [
            (p["ult"], frozenset({"phys", "art"})),
            (p["skill"], frozenset({"phys", "skill"})),
            (p["crit"], frozenset({"phys", "crit"})),
            (p["melee"], frozenset({"phys"})),
        ]
        return out


class Relic:
    def __init__(self, raw, model):
        r = raw["relic"]
        self.id = raw["relic_id"]
        self.name = r["name"]
        self.color = r["color"][0]
        self.kind = r["kind"]
        self.effects = r["effects"]
        self.unverified = [f.split(":", 1)[1] for f in r["flags"] if f.startswith("unverified_effect:")]
        self.parsed = []  # (family, tier) for every non-Dormant effect
        self.dormant = []
        self.curses = []
        self.start = []  # starting-armament affinities: "poison", "holy", ...
        for e in self.effects:
            m = DORMANT_RE.match(e["text"])
            if m:
                self.dormant.append(m.group(1))
            else:
                self.parsed.append(family(e["text"]))
                s = START_RE.match(e["text"])
                if s:
                    self.start.append((s.group(1) or s.group(2)).lower())
            if e["curse"]:
                self.curses.append(e["curse"])
        fams = {f for f, _ in self.parsed}
        self.key = bool(fams & ({SKILL_USE, ISA, SWITCH_ADDS} | ENGINE)) or bool(self.start)
        self.solo = score([self], model)

    def fits(self, slot):
        return slot == "W" or slot == self.color


def poison_model(fams, marks):
    """Poison uptime on the target from the loadout's poison sources."""
    keep = 1.0
    if WEAPON_POISON in fams:
        keep *= 1 - POISON_UPTIME["weapon"]
    if HEAVY_POISON in fams:
        keep *= 1 - min(0.5, POISON_UPTIME["mark"] * marks / BASE_MARKS)
    if ART_POISON in fams:
        keep *= 1 - POISON_UPTIME["art"]
    return 1 - keep


def damage_points(buffs, slices):
    """Points for damage Pct buffs over tagged slices (each buff multiplies matching slices)."""
    total = 0.0
    for share, tags in slices:
        m = 1.0
        for b in buffs:
            if b.scope == "all" or b.scope in tags:
                m *= 1 + b.size / 100
        total += share * m
    return POINTS_PER_PCT * (total - 1) * 100


def sustain_points(effects, maxhp_extra=()):
    """Points for self-sustain Pct effects, combined into one effective-HP product."""
    keep = {}
    maxhp = 1.0
    bars = 0.0
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
    taken += sum(INCOMING[t] * aff * keep.get(t, 1.0) for t in ELEMENTS)
    taken /= sum(INCOMING.values())
    return POINTS_PER_PCT * (maxhp * (1 + bars / FIGHT_HP_BUDGET) / taken - 1) * 100


def breakdown(relics, model, report=None):
    """Score split into damage / sustain / utility / penalties; values sum to the total."""
    parts = dict.fromkeys(("damage", "sustain", "utility", "penalties"), 0.0)
    pcts = []
    best = {}  # (family, category) -> best weight, for non-stacking families
    tiers = {}  # family -> best tier
    curses = {}
    dormant = []
    starts = []
    for r in relics:
        for fam, tier in r.parsed:
            tiers[fam] = max(tiers.get(fam, -1), tier)
            for cat, w in model.weights.get(fam, ()):
                v = w[min(tier, len(w) - 1)]
                # Attack buffs and negative weights (stat swaps, -15% poison) always apply.
                if fam in STACKING or v < 0:
                    pcts.append(v) if isinstance(v, Pct) else parts.__setitem__(cat, parts[cat] + v)
                elif v > best.get((fam, cat), 0):
                    best[(fam, cat)] = v
        for c in r.curses:
            curses[c] = curses.get(c, 0) + 1
        dormant += r.dormant
        starts += r.start
        parts["penalties"] += UNVERIFIED * len(r.unverified)
    for (fam, cat), v in best.items():
        if isinstance(v, Pct):
            pcts.append(v)
        else:
            parts[cat] += v

    # Starting-armament affinities don't stack (wiki.gg): keep the one the build wants.
    start_el = None
    distinct = set(starts)
    if model.want == "element" and distinct & set(ELEMENTS):
        start_el = sorted(distinct & set(ELEMENTS))[0]
        parts["penalties"] += START_CONFLICT * (len(distinct) - 1)
    elif model.want and model.want in distinct:
        parts["penalties"] += START_CONFLICT * (len(distinct) - 1)
    elif distinct and model.build != "affinity":
        parts["penalties"] += (START_OFF if model.build == "isa" else START_CONFLICT) * len(distinct)
    if WEAPON_POISON in tiers and start_el:
        # Poison relic on an elemental build: it's not the affinity we keep, so drop its -15%.
        pcts = [b for b in pcts if b.scope != "start"]
    slices = model.slices(start_el)

    # Engine: Marking rate, poison uptime, conditional buffs.
    cdr = CDR_SIZES[min(tiers[CDR], 3)] if CDR in tiers else 0
    marks = BASE_MARKS / (1 - cdr / 100)
    if cdr:
        pcts.append(Pct(0, "damage", "skill", 100 * (marks / BASE_MARKS - 1)))
    u = 0.0
    flat = 0.0
    if model.build == "poison":
        u = poison_model(tiers, marks)
        flat += POISON_DOT * u
        if HEAVY_POISON in tiers:
            flat += MARK_BURST * marks * u
        if VS_POISON in tiers:
            pcts.append(Pct(0, "damage", "all", VS_POISON_SIZES[min(tiers[VS_POISON], 2)] * u))
        if POISON_VICINITY in tiers:
            pcts.append(Pct(0, "damage", "all", 12 * u))
    if model.build == "affinity" and SWITCH_ADDS in tiers:
        # Random-element damage on hits for 10 s after a swap: extra slices, one per element.
        share = model.switch_add / 100 * model.p["switch"] / len(ELEMENTS)
        slices = slices + [(share, frozenset({"aff", "added", "bow", e})) for e in ELEMENTS]

    dmg = [b for b in pcts if b.kind == "damage"]
    parts["damage"] += damage_points(dmg, slices) + POINTS_PER_PCT * flat
    selfs = [b for b in pcts if b.kind != "damage"]
    clean = sustain_points(selfs)
    parts["sustain"] += clean
    cursed = [CURSE_MAXHP[c] for c, n in curses.items() if c in CURSE_MAXHP for _ in range(n)]
    parts["penalties"] += sustain_points(selfs, cursed) - clean
    for c, n in curses.items():
        pen = CURSE_PENALTY.get(c, -2)
        if c == "Ultimate Art Charging Impaired" and model.build == "poison":
            pen = DISQUALIFY  # the charged Art delivers 300 poison (characters/ironeye.md)
        parts["penalties"] += pen * n + DUP_CURSE * (n - 1)
        if c.startswith("Taking Damage Causes"):
            parts["penalties"] += ARD_AMPLIFY * n * curses.get("All Resistances Down", 0)
    for d in dormant:
        parts["penalties"] += DORMANT_OK.get(d, DORMANT_BAD)
    parts["penalties"] += DORMANT_EXTRA * max(0, len(dormant) - 1)
    if report is not None:
        report.update(
            marks=round(marks, 1),
            poison_uptime=round(u, 2),
            poison_flat_pct=round(flat, 1),
            start_element=start_el or ("poison" if model.want == "poison" and "poison" in distinct else None),
            isa_copies=sum(1 for r in relics for f, _ in r.parsed if f == ISA),
        )
    return parts


def score(relics, model):
    return sum(breakdown(relics, model).values())


def format_parts(parts):
    return "  ".join(f"{k} {v:.1f}" for k, v in parts.items())


def load(model):
    data = json.loads(DB.read_text())
    return [Relic(r, model) for r in data["relics"] if r["status"] == "active"]


def curse_count(relics):
    return sum(len(r.curses) for r in relics)


def has(relics, fam):
    return any(f == fam for r in relics for f, _ in r.parsed)


def requirements(build, min_isa, poison_source):
    """(normal-side check, deep-side check, whole-loadout check) for a build."""
    normal = lambda n: has(n, SKILL_USE)
    deep = None
    whole = None
    checks = []
    if build == "poison":
        deep = lambda d: has(d, HEAVY_POISON)
        if poison_source:
            # The heavy-poison burst needs an already-poisoned target: carry a 2nd source.
            checks.append(lambda rs: has(rs, WEAPON_POISON) or has(rs, ART_POISON))
    if build == "affinity":
        normal = lambda n: has(n, SKILL_USE) and any(r.id == NIGHT_OF_THE_LORD for r in n)
    if min_isa:
        checks.append(lambda rs: sum(1 for r in rs for f, _ in r.parsed if f == ISA) >= min_isa)
    if checks:
        whole = lambda rs: all(c(rs) for c in checks)
    return normal, deep, whole


def top_triples(pool, colors, per_slot, keep, max_curses, model, require=None):
    """Best relic triples (by triple score) for the given slot colors.

    Keeps the best `keep` / 2 triples with rally and the best `keep` / 2 without, so a
    side-only score that credits rally fully doesn't crowd out strong rally-less triples.
    Key relics (requirements, ISA, poison engine, starting-armament) are always candidates.
    """
    pool = [r for r in pool if len(r.curses) <= max_curses]
    cands = []
    for c in colors:
        fit = sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)
        cands.append(fit[:per_slot] + [r for r in fit[per_slot:] if r.key])
    seen = set()
    out = []
    for combo in itertools.product(*cands):
        ids = frozenset(r.id for r in combo)
        if len(ids) < 3 or ids in seen or curse_count(combo) > max_curses:
            continue
        if require and not require(combo):
            continue
        seen.add(ids)
        out.append((score(combo, model), combo))
    out.sort(key=lambda t: -t[0])
    with_rally = [t for t in out if has(t[1], RALLY)]
    without = [t for t in out if not has(t[1], RALLY)]
    # ISA triples score low alone but multiply with each other: keep a slice of the best ones.
    isa = sorted(out, key=lambda t: (-sum(f == ISA for r in t[1] for f, _ in r.parsed), -t[0]))
    return with_rally[: keep // 2] + without[: keep // 2] + isa[: keep // 4]


def search(relics, model, normal, deep, per_slot, keep, max_curses, min_isa, poison_source):
    std = [r for r in relics if r.kind == "standard" and r.solo > DISQUALIFY / 2]
    dp = [r for r in relics if r.kind == "deep" and r.solo > DISQUALIFY / 2]
    need_n, need_d, need_all = requirements(model.build, min_isa, poison_source)
    nt = top_triples(std, normal, per_slot, keep, max_curses, model, need_n)
    dt = top_triples(dp, deep, per_slot, keep, max_curses, model, need_d)
    results = []
    seen = set()
    for _, n in nt:
        for _, d in dt:
            ids = frozenset(r.id for r in n + d)
            if ids in seen or curse_count(n + d) > max_curses:
                continue
            if need_all and not need_all(n + d):
                continue
            seen.add(ids)
            results.append((score(n + d, model), n, d))
    results.sort(key=lambda t: -t[0])
    return results


def describe(total, n, d, normal, deep, model):
    report = {}
    lines = [f"score {total:.1f}  ({format_parts(breakdown(n + d, model, report))})"]
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
    rally = [r.id for r in n + d if has([r], RALLY)]
    lines.append(f"  engine: {report}")
    lines.append(f"  rally: {rally or 'none'}")
    lines.append(f"  curses ({len(all_curses)}): {all_curses}")
    lines.append(f"  dormant: {dormant or 'none'}")
    lines.append(f"  unverified: {flags or 'none'}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", choices=BUILDS, required=True)
    ap.add_argument("--switch-add", type=float, default=SWITCH_ADD, help="affinity: %% damage added by the switch affinity attack")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--vessel")
    ap.add_argument("--per-slot", type=int, default=40)
    ap.add_argument("--keep", type=int, default=800)
    ap.add_argument("--max-curses", type=int, default=99, help="cap on total curses per loadout")
    ap.add_argument("--min-isa", type=int, default=0, help="minimum Improved Initial Standard Attack copies")
    ap.add_argument("--no-poison-source", action="store_true", help="poison: don't require weapon or Art poison")
    args = ap.parse_args()
    model = Model(args.build, args.switch_add)
    relics = load(model)
    summary = []
    for name, (normal, deep) in VESSELS.items():
        if args.vessel and args.vessel != name:
            continue
        res = search(relics, model, normal, deep, args.per_slot, args.keep, args.max_curses, args.min_isa, not args.no_poison_source)
        if not res:
            print(f"=== {name}  normal {normal} / deep {deep}: no loadout meets the requirements\n")
            continue
        summary.append((res[0][0], name, breakdown(res[0][1] + res[0][2], model)))
        print(f"=== {name}  normal {normal} / deep {deep}")
        for total, n, d in res[: args.top]:
            print(describe(total, n, d, normal, deep, model))
        print()
    print("=== summary")
    for s, name, parts in sorted(summary, key=lambda t: -t[0]):
        print(f"  {s:6.1f}  {name:30}  {format_parts(parts)}")


if __name__ == "__main__":
    main()
