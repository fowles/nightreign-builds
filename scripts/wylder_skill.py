"""Wylder Deep of Night loadout search: skill use, with a required base set.

Usage: python3 -I scripts/wylder_skill.py [--top N] [--vessel NAME] [--bleed PCT] [--skill-share F]

Build: The Wylder's Earring (two Claw Shots), The Will of the Balancers and The Will
of Balance (your rule) fill all three normal slots. Wylder opens with Claw Shot and
spends most of his damage budget on weapon skills, which both Wills boost.

The base set is Red, Blue, Red, so only vessels with normal slots R R B can hold it
(checked in main). Only the three deep slots are searched.

Reuses the scoring engine in scripts/raider_charged.py (damage and sustain products,
curses, stacking). This script replaces its coverage, weights, curse, Dormant Power
and vessel tables before any relic is scored.
"""
import argparse
import heapq
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script dir from sys.path
import raider_charged as rc  # noqa: E402

BASE_IDS = ("R01921", "R00926", "R00805")  # Earring, Will of Balance, Will of the Balancers
BLOOD_LOSS = "[Wylder] Character Skill inflicts Blood Loss"

# Share of this build's total damage each scope covers (CLAUDE.md "Coverage"). All guesses.
# Shares are disjoint: "skill" is weapon-skill hits, the others are what's left.
rc.COVERAGE.clear()
rc.COVERAGE.update({
    "all": 1.0,  # treated as physical; elemental weapon skills depend on drops
    "skill": 0.4,  # weapon skills. Claw Shot itself does "miniscule" damage (wiki.gg)
    "greatsword": 0.25,  # normal attacks with the starting class
    "fire": 0.05,  # Art fire spread burn; damage unpublished
    "crit": 0.03,  # crits after stance breaks
    "initial": 0.03,  # first light attack; this build leads with skills
})


def tune(skill_share, bleed):
    """Set the two inputs the sensitivity runs vary, before relics are scored."""
    rc.COVERAGE["skill"] = skill_share
    rc.CATEGORIES["damage"].update(damage_table(bleed))
    rc.WEIGHTS = {fam: w for fams in rc.CATEGORIES.values() for fam, w in fams.items()}
    rc.CATEGORY = {fam: cat for cat, fams in rc.CATEGORIES.items() for fam in fams}


def damage_table(bleed):
    return {
        "Physical Attack Up": rc.pct([4, 5, 6, 10.5, 12]),  # wiki.gg, post-1.03
        "Improved Melee Attack Power": rc.pct([5]),  # wiki.gg; assumed to cover weapon skills too (unverified)
        "Improved Skill Attack Power": rc.pct([15], "skill"),  # wiki.gg; Claw Shot assumed not boosted (unverified)
        # 115 buildup per Claw Shot; a proc every ~60 s on a boss. Size is a guess. Only highest counts.
        BLOOD_LOSS: rc.pct([bleed]),
        "Improved Greatsword Attack Power": rc.pct([9], "greatsword"),  # wiki.gg
        "Improved Attack Power with 3+ Greatswords Equipped": rc.pct([1.5], "greatsword"),  # guess: ~10% x 0.15 availability
        "Fire Attack Power Up": rc.pct([4, 5, 6, 10.5, 12], "fire"),  # sizes assumed equal to physical (unverified)
        "Improved Affinity Attack Power": rc.pct([5, 8, 10], "fire"),  # wiki.gg, per ironeye.py
        "Improved Critical Hits": rc.pct([18, 23], "crit"),  # +1 = 23% per wiki.gg; base guessed
        "Improved Initial Standard Attack": rc.pct([15], "initial"),  # +15% first light attack (wiki.gg)
    }


sustain = {fam: w for fam, w in rc.CATEGORIES["sustain"].items() if "Raider" not in fam and "Totem" not in fam}
# Classes this build doesn't aim for; the shared table only covers Raider's.
for fam in ("HP Restoration upon Greataxe Attacks", "HP Restoration upon Colossal Weapon Attacks", "HP Restoration upon Great Hammer Attacks"):
    del sustain[fam]
sustain.update({
    "Improved Damage Negation at Low HP": rc.ehp([2]),  # guess: Wylder spends less time low than Raider
    "Poise": [0, 1.5, 2, 2.5],  # hand-weighted: weapon-skill wind-ups get interrupted
    "Slowly restore HP for self and nearby allies when HP is low": rc.heal([0.2]),  # guess
    # Vigor -5 costs about 2 points; the swap is scored under utility with its Mind gain.
    "[Wylder] Improved Intelligence and Faith, Reduced Strength and Dexterity": [-5],  # guts both main stats
})
rc.CATEGORIES["damage"] = damage_table(15)
rc.CATEGORIES["sustain"] = sustain
rc.CATEGORIES["utility"] = {
    # Weapon skills run on FP, so FP effects are in focus. All hand-weighted.
    "Reduced FP Consumption": [3],
    "Increased Maximum FP": [2],
    "Continuous FP Recovery": [0.5],  # 1 FP per 5 s (wiki.gg)
    "FP Restoration upon Greatsword Attacks": [1.5],  # refills between skills, greatsword share only
    "FP Restoration upon Successive Attacks": [1.5],
    "Mind": [0, 0.5, 1, 1.5],
    "[Wylder] Improved Mind, Reduced Vigor": [0.5],  # Mind +10 for Vigor -5; net of the HP cost
    "[Wylder] +1 additional Character Skill use": [4],  # the point of the Earring
    "Character Skill Cooldown Reduction": [0, 2, 3, 4],  # -5 / -7.5 / -10% (wiki.gg)
    "[Wylder] Art activation spreads fire in area": [2],  # burn feeds the Art gauge (1.03.2)
    "Ultimate Art Auto Charge": [0, 3, 4, 5],
    "Defeating enemies fills more of the Art gauge": [2, 3],
    "Critical hits fill more of the Art gauge": [1, 1.5],
    "Items confer effect to all nearby allies": [0.5],
}
rc.WEIGHTS = {fam: w for fams in rc.CATEGORIES.values() for fam, w in fams.items()}
rc.CATEGORY = {fam: cat for cat, fams in rc.CATEGORIES.items() for fam in fams}
rc.STACKING.clear()
rc.STACKING |= {
    "Physical Attack Up",
    "Improved Melee Attack Power",
    "Improved Skill Attack Power",
    "Improved Initial Standard Attack",
    "Improved Greatsword Attack Power",
    "Improved Attack Power with 3+ Greatswords Equipped",
    "Fire Attack Power Up",
    "Improved Affinity Attack Power",
}
rc.PREFIX_WEIGHTS = []

rc.DORMANT_OK = {"Greatswords": 0, "Katana": -2, "Curved Greatswords": -2}  # wylder.md: on-build classes for flexible builds
rc.CURSE_PENALTY.clear()
rc.CURSE_PENALTY.update({
    "Taking Damage Causes Death Buildup": -15,  # Wylder doesn't block much, but it's still an instant kill
    "Taking Damage Causes Sleep Buildup": -12,
    "Taking Damage Causes Poison Buildup": -6,
    "Taking Damage Causes Rot Buildup": -6,
    "Taking Damage Causes Frost Buildup": -6,
    "Taking Damage Causes Blood Loss Buildup": -6,
    "Taking Damage Causes Madness Buildup": -6,
    "Ultimate Art Charging Impaired": rc.DISQUALIFY,  # the Earring's fire spread is built on the Art (wylder.md)
    "Reduced Intelligence and Dexterity": -1.5,  # Dex B
    "Reduced Dexterity and Faith": -1.5,
    "Reduced Strength and Intelligence": -2.5,  # Str A
    "Reduced Faith and Strength": -2.5,
    "Reduced Rune Acquisition": -1,
    "Repeated Evasions Lower Damage Negation": -0.5,
    "Reduced Damage Negation After Evading": -8,  # very bad: missed dodges hurt (CLAUDE.md)
    "Reduced Damage Negation for Flask Usages": -2.5,
    "Reduced Flask HP Restoration": -3,
    "Near Death Reduces Max HP": -3,
    "All Resistances Down": -3,
    "Lower Attack When Below Max HP": -5,
    "Poison Buildup When Below Max HP": -3,
    "Rot Buildup When Below Max HP": -3.5,
    "Reduced Vigor and Arcane": 0,  # scored through CURSE_MAXHP; Arcane is free
    "Continuous HP Loss": -4,
})

rc.VESSELS.clear()
rc.VESSELS.update({
    "Wylder's Urn": ("RRB", "RRB"),
    "Wylder's Goblet": ("YGG", "YGG"),
    "Wylder's Chalice": ("RYW", "RBG"),
    "Soot-Covered Wylder's Urn": ("BBY", "BBY"),
    "Sealed Wylder's Urn": ("BRR", "GYY"),
    "Decrepit Wylder's Goblet": ("BGY", "BGY"),
    "Forgotten Wylder's Goblet": ("GGY", "RGW"),
    "Sacred Erdtree Grail": ("YYY", "YYY"),
    "Spirit Shelter Grail": ("GGG", "GGG"),
    "Giant's Cradle Grail": ("BBB", "BBB"),
    "Scadutree Grail": ("RRR", "RRR"),
})


def seat(base, colors):
    """The base relics ordered to fit `colors`, or None if they can't all fit."""
    for perm in itertools.permutations(base):
        if all(r.fits(c) for r, c in zip(perm, colors)):
            return perm
    return None


def search(base, relics, deep, per_slot, top, max_curses, no_rally=False, need_bleed=False):
    """The best `top` deep triples, each scored with the base set, and how many were scored.

    Takes the top `per_slot` relics per slot; 0 searches every deep relic.
    `no_rally` removes rally relics; `need_bleed` keeps only triples with Claw Shot Blood Loss.
    """
    pool = [r for r in relics if r.kind == "deep" and r.solo > rc.DISQUALIFY / 2]
    if no_rally:
        pool = [r for r in pool if rc.RALLY not in r.fams]
    cands = []
    for c in deep:
        fits = sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)
        cands.append(fits[:per_slot] if per_slot else fits)
    same = [(i, j) for i, j in itertools.combinations(range(3), 2) if deep[i] == deep[j]]
    count = 0

    def scored():
        nonlocal count
        for combo in itertools.product(*cands):
            # Same-color slots share a candidate list: keep one order of each pair.
            if any(combo[i].id >= combo[j].id for i, j in same):
                continue
            if rc.curse_count(combo) > max_curses:
                continue
            if need_bleed and not any(BLOOD_LOSS in r.fams for r in combo):
                continue
            count += 1
            yield rc.score(base + combo), combo

    return heapq.nlargest(top, scored(), key=lambda t: t[0]), count


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=5)
    ap.add_argument("--vessel")
    ap.add_argument("--per-slot", type=int, default=0, help="shortlist per slot; 0 searches every deep relic")
    ap.add_argument("--max-curses", type=int, default=99, help="cap on curses across the three deep relics (the base set has none)")
    ap.add_argument("--bleed", type=float, default=15, help="damage %% credited to Claw Shot Blood Loss")
    ap.add_argument("--skill-share", type=float, default=0.4, help="share of damage from weapon skills")
    ap.add_argument("--no-rally", action="store_true", help="exclude every rally relic")
    ap.add_argument("--need-bleed", action="store_true", help="require [Wylder] Character Skill inflicts Blood Loss")
    args = ap.parse_args()
    tune(args.skill_share, args.bleed)
    relics = rc.load()
    by_id = {r.id: r for r in relics}
    base = [by_id[i] for i in BASE_IDS]
    summary = []
    for name, (normal, deep) in rc.VESSELS.items():
        if args.vessel and args.vessel != name:
            continue
        seated = seat(base, normal)
        if not seated:
            print(f"--- {name}  normal {normal}: can't hold the base set")
            continue
        res, count = search(seated, relics, deep, args.per_slot, args.top, args.max_curses, args.no_rally, args.need_bleed)
        best = seated + res[0][1]
        summary.append((res[0][0], name, rc.breakdown(best), any(rc.RALLY in r.fams for r in best)))
        print(f"=== {name}  normal {normal} / deep {deep}  ({count} deep triples scored)")
        for total, combo in res[: args.top]:
            print(rc.describe(total, seated, combo, normal, deep))
        print()
    print("=== summary")
    for s, name, parts, has_rally in sorted(summary, key=lambda t: -t[0]):
        print(f"  {s:6.1f}  {name:30}  {rc.format_parts(parts)}" + ("" if has_rally else "  NO RALLY"))


if __name__ == "__main__":
    main()
