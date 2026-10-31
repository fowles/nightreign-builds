"""Guardian Deep of Night loadout search: sustain + guard counters + Ultimate Art regen.

Usage: python3 -I scripts/guardian_sustain.py [--top N] [--vessel NAME]

Scoring:
  - Effects are grouped into families by stripping a trailing " +N". Attack
    families in STACKING count every copy across all six slots; in every other
    family only the highest tier counts (see CLAUDE.md "Stacking").
  - Each curse is penalized per CURSE_PENALTY; repeating a curse costs extra.
  - Dormant Powers: Halberds neutral, anything else negative, and carrying
    more than one costs extra because they dilute each other.
  - Effects flagged unverified_effect cost a small tiebreak penalty.
"""
import argparse
import itertools
import json
import re
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "mfk-relicdb.json"

# family -> list of weights indexed by tier (base = tier 0, "+1" = tier 1, ...)
WEIGHTS = {
    # Guard counters
    "Improved Guard Counters": [8, 10, 12],
    "Guard counter is given a boost based on current HP": [8],
    "[Guardian] Successful guards send out shockwaves while ability is active": [7],
    # Ultimate Art regen
    "Successful guarding fills more of the Art gauge": [9, 11],
    "Ultimate Art Auto Charge": [0, 5, 7, 9],
    "Critical hits fill more of the Art gauge": [2, 3],
    "Defeating enemies fills more of the Art gauge": [3, 4],
    # Sustain (self)
    "HP Recovery From Successful Guarding": [10],
    "HP Restoration upon Thrusting Counterattack": [5, 6],
    "Partial HP Restoration upon Post-Damage Attacks": [5, 6, 7],
    "Continuous HP Recovery": [6],
    "HP Restoration upon Halberd Attacks": [5],
    "Slowly restore HP for self and nearby allies when HP is low": [4],
    "Increased Maximum HP": [5],
    "Increased Maximum Stamina": [5],
    "Vigor": [0, 2, 3, 4],
    "Endurance": [0, 1.5, 2.5, 3.5],
    "Improved Flask HP Restoration": [3],
    # Sustain (team) / Art payoff
    "[Guardian] Slowly restores nearby allies' HP while Art is active": [6],
    "[Guardian] Character Skill Boosts Damage Negation of Nearby Allies": [5],
    "Flask Also Heals Allies": [3],
    "Draw enemy attention while guarding": [3],
    # Defense
    "Improved Physical Damage Negation": [4, 5, 6],
    "Improved Affinity Damage Negation": [3, 3.5, 4],
    "Improved Damage Negation at Low HP": [2],
    "Improved Poise & Damage Negation When Knocked Back by Damage": [1.5],
    "Poise": [0, 1.5, 2, 2.5],
    "Fire Damage Negation Up": [1],
    "Improved Fire Damage Negation": [1, 1.25, 1.5],
    "Holy Damage Negation Up": [1],
    "Improved Holy Damage Negation": [1, 1.25, 1.5],
    "Lightning Damage Negation Up": [1],
    "Improved Lightning Damage Negation": [1, 1.25, 1.5],
    "Magic Damage Negation Up": [1],
    "Improved Magic Damage Negation": [1, 1.25, 1.5],
    # Offense
    "Physical Attack Up": [1.2, 1.6, 2, 3.4, 4],  # 3/4/5/8.5/10%, 0.4 per %
    "Improved Halberd Attack Power": [4],
    "Strength": [0, 1, 1.5, 2],
    "Improved Attack Power with 3+ Halberds Equipped": [0.5],
    # Utility
    "Character Skill Cooldown Reduction": [0, 1, 1.5, 2],
    "Stamina Recovery upon Landing Attacks": [2, 2.5],
    "Raised stamina recovery for nearby allies, but not for self": [1],
    "Defeating enemies restores HP for allies but not for self": [1],
    "Max HP Up with 3+ Greatshields Equipped": [0.5],
    "HP restored when using medicinal boluses, etc.": [0.5, 0.75],
    "[Guardian] Increased duration for Character Skill": [1],
    "[Guardian] Creates whirlwind when charging halberd attacks": [1],
    # Stat swaps that cost Vigor
    "[Guardian] Improved Strength and Dexterity, Reduced Vigor": [-2],
    "[Guardian] Improved Mind and Faith, Reduced Vigor": [-4],
}

# Attack buffs: every copy counts, across tiers and duplicates.
STACKING = {
    "Improved Guard Counters",
    "Physical Attack Up",
    "Improved Halberd Attack Power",
    "Improved Attack Power with 3+ Halberds Equipped",
}

# Prefix rules for effects not listed above.
PREFIX_WEIGHTS = [
    ("Starting armament deals", -1),  # converts physical halberd damage
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
    "Reduced Vigor and Arcane": -4,
    "Continuous HP Loss": -4,
}
DUP_CURSE = -1  # extra per repeat of the same curse
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
    fam, tier = family(text)
    if fam in WEIGHTS:
        w = WEIGHTS[fam]
        return fam, w[min(tier, len(w) - 1)]
    for prefix, w in PREFIX_WEIGHTS:
        if text.startswith(prefix):
            return fam, w
    return fam, 0


class Relic:
    def __init__(self, raw):
        r = raw["relic"]
        self.id = raw["relic_id"]
        self.name = r["name"]
        self.color = r["color"][0]
        self.kind = r["kind"]
        self.effects = r["effects"]
        self.unverified = [f.split(":", 1)[1] for f in r["flags"] if f.startswith("unverified_effect:")]
        self.fams = {}  # family -> best value on this relic
        self.dormant = []
        self.curses = []
        for e in self.effects:
            m = DORMANT_RE.match(e["text"])
            if m:
                self.dormant.append(m.group(1))
            else:
                fam, v = effect_value(e["text"])
                if v > self.fams.get(fam, float("-inf")):
                    self.fams[fam] = v
            if e["curse"]:
                self.curses.append(e["curse"])
        self.solo = score([self])

    def fits(self, slot):
        return slot == "W" or slot == self.color


def score(relics):
    best = {}
    curses = {}
    dormant = []
    s = 0.0
    for r in relics:
        for fam, v in r.fams.items():
            # Negative families (stat swaps) and attack buffs always apply;
            # other positives take the max.
            if v < 0 or fam in STACKING:
                s += v
            elif v > best.get(fam, 0):
                best[fam] = v
        for c in r.curses:
            curses[c] = curses.get(c, 0) + 1
        dormant += r.dormant
        s += UNVERIFIED * len(r.unverified)
    s += sum(best.values())
    for c, n in curses.items():
        s += CURSE_PENALTY.get(c, -2) * n + DUP_CURSE * (n - 1)
    for d in dormant:
        s += DORMANT_OK.get(d, DORMANT_BAD)
    s += DORMANT_EXTRA * max(0, len(dormant) - 1)
    return s


def load():
    data = json.loads(DB.read_text())
    return [Relic(r) for r in data["relics"] if r["status"] == "active"]


def top_triples(pool, colors, per_slot, keep):
    """Best `keep` relic triples (by triple score) for the given slot colors."""
    cands = [sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)[:per_slot] for c in colors]
    seen = set()
    out = []
    for combo in itertools.product(*cands):
        ids = frozenset(r.id for r in combo)
        if len(ids) < 3 or ids in seen:
            continue
        seen.add(ids)
        out.append((score(combo), combo))
    out.sort(key=lambda t: -t[0])
    return out[:keep]


def search(relics, normal, deep, per_slot, keep):
    std = [r for r in relics if r.kind == "standard" and r.solo > DISQUALIFY / 2]
    dp = [r for r in relics if r.kind == "deep" and r.solo > DISQUALIFY / 2]
    nt = top_triples(std, normal, per_slot, keep)
    dt = top_triples(dp, deep, per_slot, keep)
    results = []
    for _, n in nt:
        for _, d in dt:
            results.append((score(n + d), n, d))
    results.sort(key=lambda t: -t[0])
    return results


def describe(total, n, d, normal, deep):
    lines = [f"score {total:.1f}"]
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
    lines.append(f"  curses ({len(all_curses)}): {all_curses}")
    lines.append(f"  dormant: {dormant or 'none'}")
    lines.append(f"  unverified: {flags or 'none'}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--vessel")
    ap.add_argument("--per-slot", type=int, default=40)
    ap.add_argument("--keep", type=int, default=600)
    args = ap.parse_args()
    relics = load()
    summary = []
    for name, (normal, deep) in VESSELS.items():
        if args.vessel and args.vessel != name:
            continue
        res = search(relics, normal, deep, args.per_slot, args.keep)
        summary.append((res[0][0], name))
        print(f"=== {name}  normal {normal} / deep {deep}")
        for total, n, d in res[: args.top]:
            print(describe(total, n, d, normal, deep))
        print()
    print("=== summary")
    for s, name in sorted(summary, reverse=True):
        print(f"  {s:6.1f}  {name}")


if __name__ == "__main__":
    main()
