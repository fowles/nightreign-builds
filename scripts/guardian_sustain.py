"""Guardian Deep of Night loadout search: sustain + guard counters + Ultimate Art regen.

Usage: python3 -I scripts/guardian_sustain.py [--top N] [--vessel NAME] [--max-curses N]

Scoring:
  - Each family belongs to a category (damage / sustain / utility); output
    reports those plus penalties (curses, Dormant Powers, unverified flags),
    which sum to the total score.
  - Effects are grouped into families by stripping a trailing " +N". Attack
    families in STACKING count every copy across all six slots; in every other
    family only the highest tier counts (see CLAUDE.md "Stacking").
  - Self-sustain is one effective-HP product (CLAUDE.md "Fight model"):
    eHP = (1 + max HP) x (1 + heals / budget) / damage taken. Max HP families
    multiply, heal families add (in max-HP bars per fight), negations multiply.
    Team heals/negation and hand-weighted sustain (poise, aggro) add on top.
  - Each curse is penalized per CURSE_PENALTY; repeating a curse costs extra.
    Curses in CURSE_MAXHP lower max HP inside the eHP product instead, and the
    eHP they cost is reported as a penalty.
  - Dormant Powers: Halberds neutral, anything else negative, and carrying
    more than one costs extra because they dilute each other.
  - Effects flagged unverified_effect cost a small tiebreak penalty.
  - Every loadout reports whether it carries rally (non-negotiable for melee).

Search: the best --keep triples per side (from the top --per-slot relics per
slot) are crossed and scored as six-slot sets. Narrower defaults (40 / 600)
missed the optimum because side-only scores double-count effects the other side
already supplies; 80 / 2000 matched 120 / 4000 on the top vessels.
"""
import argparse
import itertools
import json
import re
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "mfk-relicdb.json"

POINTS_PER_PCT = 0.4  # per 1% of total damage or of effective HP (CLAUDE.md)

# Share of this build's total damage each scope covers (CLAUDE.md "Coverage").
COVERAGE = {
    "all": 1.0,  # halberd hits, skills, counters: effectively all physical
    "guard_counter": 0.35,  # guess: guard counters are a big but minor share of damage
    "skill": 0.05,  # guess: Whirlwind is used for its negation buff, not its damage
    "crit": 0.03,  # guess: ripostes/backstabs are rare for a guard tank
}

# Reference fight model for sustain (CLAUDE.md "Fight model"). All guesses.
INCOMING = {"physical": 0.6, "fire": 0.1, "holy": 0.1, "lightning": 0.1, "magic": 0.1}  # share of damage taken
AFFINITY = ("fire", "holy", "lightning", "magic")
FIGHT_HP_BUDGET = 3.0  # max-HP bars absorbed per fight: base HP + flasks + baseline regen
ALLY_FACTOR = 0.5  # each ally's eHP vs. your own
ALLIES = 2


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


def damage_points(buffs):
    """Points for a set of damage Pct buffs: multiplicative within a scope, scopes by coverage."""
    mult = {}
    for b in buffs:
        mult[b.scope] = mult.get(b.scope, 1.0) * (1 + b.size / 100)
    sub = [sc for sc in COVERAGE if sc != "all"]
    narrow = 1 - sum(COVERAGE[sc] for sc in sub) + sum(COVERAGE[sc] * mult.get(sc, 1.0) for sc in sub)
    total = mult.get("all", 1.0) * narrow
    return POINTS_PER_PCT * (total - 1) * 100


def sustain_points(effects, maxhp_extra=()):
    """Points for self-sustain Pct effects, combined into one effective-HP product.

    `maxhp_extra` holds additional max-HP percentages (e.g. from curses).
    """
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
    taken += sum(INCOMING[t] * aff * keep.get(t, 1.0) for t in AFFINITY)
    taken /= sum(INCOMING.values())
    return POINTS_PER_PCT * (maxhp * (1 + bars / FIGHT_HP_BUDGET) / taken - 1) * 100


def heal(per_fight):
    """Tier weights for self-healing worth `per_fight` max-HP bars over the reference fight."""
    return [Pct(POINTS_PER_PCT * h / FIGHT_HP_BUDGET * 100, "heal", "self", h) for h in per_fight]


def team(sizes):
    """Tier weights for an eHP gain of `sizes` percent for each ally (added, not multiplied)."""
    return [POINTS_PER_PCT * s * ALLY_FACTOR * ALLIES for s in sizes]


# category -> family -> list of weights indexed by tier (base = tier 0, "+1" = tier 1, ...)
# Categories are reported separately so damage and sustain compare across builds.
# Stamina effects (incl. Endurance) are deliberately unweighted: nice to have at best.
# Sizes marked "guess" have no source; per-fight counts are guesses for a guard build.
CATEGORIES = {
    "damage": {
        "Improved Guard Counters": pct([23, 25, 29], "guard_counter"),  # wiki.gg, post-1.03; tier labels unverified
        "Guard counter is given a boost based on current HP": pct([18], "guard_counter"),  # guess; wiki.gg: +0.045-0.065 dmg per 1 HP
        "[Guardian] Successful guards send out shockwaves while ability is active": [7],
        "Physical Attack Up": pct([4, 5, 6, 10.5, 12]),  # wiki.gg, post-1.03
        "Attack power increased for each Night Invader defeated": pct([20]),  # meta-top
        "Attack power increased for each evergaol prisoner defeated": pct([5]),  # guess: size and evergaol count unknown
        "Improved Halberd Attack Power": pct([10]),  # size guessed
        "Improved Melee Attack Power": pct([5]),  # wiki.gg (Will of the Balancers)
        "Improved Skill Attack Power": pct([15], "skill"),  # wiki.gg (Will of the Balancers)
        "Improved Critical Hits": pct([18, 23], "crit"),  # +1 = 23% per wiki.gg; base guessed
        "Taking attacks improves attack power": pct([3]),  # guess: ~10% x 0.3 uptime; unknown if blocks count
        "Strength": [0, 1, 1.5, 2],
        "Improved Attack Power with 3+ Halberds Equipped": [0.5],
        "[Guardian] Creates whirlwind when charging halberd attacks": [1],
    },
    "sustain": {
        # Self
        # Rally: meta anchor, non-negotiable for melee. Base heals 1.5 bars per fight
        # (50% eHP on its own); +1/+2 heal 25%/35% more.
        "Partial HP Restoration upon Post-Damage Attacks": heal([1.5, 1.875, 2.025]),
        "HP Recovery From Successful Guarding": heal([0.9]),  # guess: ~60 blocks x 1.5%
        "HP Restoration upon Thrusting Counterattack": heal([0.25, 0.33]),  # 10 x 2.5% guess / 3.3%
        "HP Restoration upon Halberd Attacks": heal([0.3]),  # guess
        "Continuous HP Recovery": heal([0.25]),  # guess
        "Slowly restore HP for self and nearby allies when HP is low": heal([0.25]),  # guess
        "Increased Maximum HP": ehp([10]),  # guess: size unsourced
        "Max HP increased for each great enemy defeated at a Great Church.": ehp([2.5]),  # guess: ~5% x 0.5 availability
        "Vigor": ehp([0, 2, 3.5, 5]),  # guess: % max HP per relic tier
        "Improved Flask HP Restoration": heal([0.1]),  # +10% of ~1 bar of flask healing
        "Max HP Up with 3+ Greatshields Equipped": ehp([1]),  # guess, rarely active
        "HP restored when using medicinal boluses, etc.": heal([0.03, 0.05]),  # guess
        # Team
        "[Guardian] Slowly restores nearby allies' HP while Art is active": team([16.7]),  # guess
        "[Guardian] Character Skill Boosts Damage Negation of Nearby Allies": team([13.6]),  # 12%
        "Flask Also Heals Allies": team([10]),  # guess
        "Defeating enemies restores HP for allies but not for self": team([2.5]),  # guess
        "Draw enemy attention while guarding": [3],  # hand-weighted: aggro, not eHP
        # Defense
        "Improved Physical Damage Negation": negation([8, 10.5, 12], "physical"),  # base guessed
        "Improved Affinity Damage Negation": negation([6, 10.5, 12], "affinity"),
        "Improved Damage Negation at Low HP": ehp([2.5]),  # guess: eHP factor, low uptime
        "Improved Poise & Damage Negation When Knocked Back by Damage": [1.5],  # hand-weighted
        "Poise": [0, 1.5, 2, 2.5],  # hand-weighted: stagger, not eHP
        "Fire Damage Negation Up": negation([10], "fire"),  # guessed
        "Improved Fire Damage Negation": negation([10, 15, 16], "fire"),
        "Holy Damage Negation Up": negation([10], "holy"),
        "Improved Holy Damage Negation": negation([10, 15, 16], "holy"),
        "Lightning Damage Negation Up": negation([10], "lightning"),
        "Improved Lightning Damage Negation": negation([10, 15, 16], "lightning"),
        "Magic Damage Negation Up": negation([10], "magic"),
        "Improved Magic Damage Negation": negation([10, 15, 16], "magic"),
        # Stat swaps that cost Vigor
        "[Guardian] Improved Strength and Dexterity, Reduced Vigor": [-2],
        "[Guardian] Improved Mind and Faith, Reduced Vigor": [-4],
    },
    "utility": {
        # Ultimate Art regen
        "Successful guarding fills more of the Art gauge": [9, 11],
        "Ultimate Art Auto Charge": [0, 5, 7, 9],
        "Critical hits fill more of the Art gauge": [2, 3],
        "Defeating enemies fills more of the Art gauge": [3, 4],
        "Character Skill Cooldown Reduction": [0, 1, 1.5, 2],
        "[Guardian] Increased duration for Character Skill": [1],
    },
}
WEIGHTS = {fam: w for fams in CATEGORIES.values() for fam, w in fams.items()}
CATEGORY = {fam: cat for cat, fams in CATEGORIES.items() for fam in fams}

# Attack buffs: every copy counts, across tiers and duplicates.
STACKING = {
    "Improved Guard Counters",
    "Physical Attack Up",
    "Improved Halberd Attack Power",
    "Improved Attack Power with 3+ Halberds Equipped",
    "Improved Melee Attack Power",
    "Improved Skill Attack Power",
}
RALLY = "Partial HP Restoration upon Post-Damage Attacks"  # non-negotiable for melee (CLAUDE.md)

# Prefix rules for effects not listed above.
PREFIX_WEIGHTS = [
    ("Starting armament deals", -1, "damage"),  # converts physical halberd damage
]

DORMANT_OK = {"Halberds": 0, "Greatshields": -1}
DORMANT_BAD = -8
DORMANT_EXTRA = -3  # per Dormant Power beyond the first

DISQUALIFY = -1000
CURSE_PENALTY = {
    "Ultimate Art Charging Impaired": DISQUALIFY,
    "Taking Damage Causes Death Buildup": DISQUALIFY,
    "Taking Damage Causes Sleep Buildup": DISQUALIFY,
    "Taking Damage Causes Poison Buildup": -8,
    "Taking Damage Causes Rot Buildup": -8,
    "Taking Damage Causes Frost Buildup": -8,
    "Taking Damage Causes Blood Loss Buildup": -8,
    "Taking Damage Causes Madness Buildup": -8,
    "Reduced Intelligence and Dexterity": -0.5,
    "Reduced Dexterity and Faith": -0.5,
    "Reduced Strength and Intelligence": -1.5,
    "Reduced Faith and Strength": -1.5,
    "Reduced Rune Acquisition": -1,
    "Repeated Evasions Lower Damage Negation": -0.5,
    "Reduced Damage Negation After Evading": -0.5,
    "Reduced Damage Negation for Flask Usages": -2.5,
    "Reduced Flask HP Restoration": -3,
    "Near Death Reduces Max HP": -3,
    "All Resistances Down": -3,
    "Lower Attack When Below Max HP": -3,
    "Poison Buildup When Below Max HP": -3.5,
    "Rot Buildup When Below Max HP": -4,
    "Reduced Vigor and Arcane": 0,  # scored through CURSE_MAXHP; Arcane is free
    "Continuous HP Loss": -4,
}
DUP_CURSE = -1  # extra per repeat of the same curse
# Curses that lower max HP, as a percentage, applied inside the eHP product.
CURSE_MAXHP = {
    "Reduced Vigor and Arcane": -5,  # guess: mirrors the Vigor +3 relic (+5% max HP)
}
UNVERIFIED = -0.5

# name -> (normal colors, deep colors); "W" = any
VESSELS = {
    "Guardian's Urn": ("RYY", "RYY"),
    "Guardian's Goblet": ("BBG", "BBG"),
    "Guardian's Chalice": ("BYW", "RBY"),
    "Soot-Covered Guardian's Urn": ("RGG", "RGG"),
    "Sealed Guardian's Urn": ("YYR", "GGB"),
    "Decrepit Guardian's Goblet": ("YGG", "YGG"),
    "Forgotten Guardian's Goblet": ("GBB", "RBW"),
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
    """(family, weight, category) for one effect."""
    fam, tier = family(text)
    if fam in WEIGHTS:
        w = WEIGHTS[fam]
        return fam, w[min(tier, len(w) - 1)], CATEGORY[fam]
    for prefix, w, cat in PREFIX_WEIGHTS:
        if text.startswith(prefix):
            return fam, w, cat
    return fam, 0, "utility"


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
        self.dormant = []
        self.curses = []
        for e in self.effects:
            m = DORMANT_RE.match(e["text"])
            if m:
                self.dormant.append(m.group(1))
            else:
                fam, v, cat = effect_value(e["text"])
                self.cats[fam] = cat
                if fam in STACKING:
                    self.stack.append((fam, v))
                elif v > self.fams.get(fam, float("-inf")):
                    self.fams[fam] = v
            if e["curse"]:
                self.curses.append(e["curse"])
        self.solo = score([self])

    def fits(self, slot):
        return slot == "W" or slot == self.color


def breakdown(relics):
    """Score split into damage / sustain / utility / penalties; values sum to the total."""
    parts = dict.fromkeys(("damage", "sustain", "utility", "penalties"), 0.0)
    pcts = []  # multiplicative effects, combined after the loop
    best = {}
    cats = {}
    curses = {}
    dormant = []
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
        for c in r.curses:
            curses[c] = curses.get(c, 0) + 1
        dormant += r.dormant
        parts["penalties"] += UNVERIFIED * len(r.unverified)
    for fam, v in best.items():
        if isinstance(v, Pct):
            pcts.append(v)
        else:
            parts[cats[fam]] += v
    parts["damage"] += damage_points([p for p in pcts if p.kind == "damage"])
    selfs = [p for p in pcts if p.kind != "damage"]
    clean = sustain_points(selfs)
    parts["sustain"] += clean
    cursed = [CURSE_MAXHP[c] for c, n in curses.items() if c in CURSE_MAXHP for _ in range(n)]
    parts["penalties"] += sustain_points(selfs, cursed) - clean
    for c, n in curses.items():
        parts["penalties"] += CURSE_PENALTY.get(c, -2) * n + DUP_CURSE * (n - 1)
    for d in dormant:
        parts["penalties"] += DORMANT_OK.get(d, DORMANT_BAD)
    parts["penalties"] += DORMANT_EXTRA * max(0, len(dormant) - 1)
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


def top_triples(pool, colors, per_slot, keep, max_curses):
    """Best `keep` relic triples (by triple score) for the given slot colors."""
    pool = [r for r in pool if len(r.curses) <= max_curses]
    cands = [sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)[:per_slot] for c in colors]
    seen = set()
    out = []
    for combo in itertools.product(*cands):
        ids = frozenset(r.id for r in combo)
        if len(ids) < 3 or ids in seen or curse_count(combo) > max_curses:
            continue
        seen.add(ids)
        out.append((score(combo), combo))
    out.sort(key=lambda t: -t[0])
    return out[:keep]


def search(relics, normal, deep, per_slot, keep, max_curses=99):
    std = [r for r in relics if r.kind == "standard" and r.solo > DISQUALIFY / 2]
    dp = [r for r in relics if r.kind == "deep" and r.solo > DISQUALIFY / 2]
    nt = top_triples(std, normal, per_slot, keep, max_curses)
    dt = top_triples(dp, deep, per_slot, keep, max_curses)
    results = []
    for _, n in nt:
        for _, d in dt:
            if curse_count(n + d) <= max_curses:
                results.append((score(n + d), n, d))
    results.sort(key=lambda t: -t[0])
    return results


def describe(total, n, d, normal, deep):
    lines = [f"score {total:.1f}  ({format_parts(breakdown(n + d))})"]
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
    lines.append(f"  rally: {rally or 'MISSING (non-negotiable for melee)'}")
    lines.append(f"  curses ({len(all_curses)}): {all_curses}")
    lines.append(f"  dormant: {dormant or 'none'}")
    lines.append(f"  unverified: {flags or 'none'}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--vessel")
    ap.add_argument("--per-slot", type=int, default=80)
    ap.add_argument("--keep", type=int, default=2000)
    ap.add_argument("--max-curses", type=int, default=99, help="cap on total curses per loadout")
    args = ap.parse_args()
    relics = load()
    summary = []
    for name, (normal, deep) in VESSELS.items():
        if args.vessel and args.vessel != name:
            continue
        res = search(relics, normal, deep, args.per_slot, args.keep, args.max_curses)
        best = res[0][1] + res[0][2]
        has_rally = any(RALLY in r.fams for r in best)
        summary.append((res[0][0], name, breakdown(best), has_rally))
        print(f"=== {name}  normal {normal} / deep {deep}")
        for total, n, d in res[: args.top]:
            print(describe(total, n, d, normal, deep))
        print()
    print("=== summary")
    for s, name, parts, has_rally in sorted(summary, key=lambda t: -t[0]):
        print(f"  {s:6.1f}  {name:30}  {format_parts(parts)}" + ("" if has_rally else "  NO RALLY"))


if __name__ == "__main__":
    main()
