"""Raider Deep of Night loadout search: fists, with `Dormant Power Helps Discover Fists`.

Usage: python3 -I scripts/raider_fists.py [--top N] [--vessel NAME] [--max-curses N]

Build: Raider starts on his Greataxe, and a required Fists Dormant Power steers drops
toward fists (Caestus, Spiked Caestus, Star Fist, Iron Ball, Katar, ...). Once a fist
drops, he fights with fast paired strikes between Retaliate counters. Lots of quick
hits after taking damage make rally and `HP Restoration upon Fist Attacks` reliable.

Every loadout must carry at least one `Dormant Power Helps Discover Fists` (your rule).
Extra Fists copies are neutral (whether they stack is unknown). Any other Dormant Power,
heavy classes included, dilutes the fist pool and is scored as a real negative.

Reuses the scoring engine in scripts/raider_charged.py (damage and sustain products,
curses, stacking, vessels). This script replaces its coverage, weights and Dormant
Power tables before any relic is scored; everything not overridden here is shared.
"""
import argparse
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script dir from sys.path
import raider_charged as rc  # noqa: E402

# Share of this build's total damage each scope covers (CLAUDE.md "Coverage"). All guesses.
rc.COVERAGE.clear()
rc.COVERAGE.update({
    "all": 1.0,  # all physical: fist strikes, Retaliate, Totem Stela
    "fist": 0.6,  # main weapon once the Dormant Power delivers one
    "greataxe": 0.15,  # starting weapon, carried until a fist drops
    "skill": 0.15,  # charged Retaliate punch; a skill, so fist buffs don't apply (unverified)
    "crit": 0.05,  # fast strikes into stance breaks
    "initial": 0.04,  # first strike of long fist chains is a small share
})

fist = {
    "damage": {
        "Improved Fist Attack Power": rc.pct([10], "fist"),  # size guessed, like other weapon classes
        "Improved Attack Power with 3+ Fists Equipped": rc.pct([3], "fist"),  # guess: ~10% x 0.3 availability with the Dormant Power
        "Improved Greataxe Attack Power": rc.pct([10], "greataxe"),
        "Improved Attack Power with 3+ Greataxes Equipped": rc.pct([1.5], "greataxe"),
        "Improved Colossal Weapon Attack Power": [0],  # off-plan
        "Improved Great Hammer Attack Power": [0],
        "Improved Colossal Sword Attack Power": [0],
        "Improved Attack Power with 3+ Colossal Weapons Equipped": [0],
        "Improved Attack Power with 3+ Great Hammers Equipped": [0],
        "Improved Critical Hits": rc.pct([18, 23], "crit"),
        "Improved Initial Standard Attack": rc.pct([15], "initial"),
        "Improved Stance-Breaking when Two-Handing": [2],  # hand-weighted: two-handing fists equips the pair
        "Improved Stance-Breaking when Wielding Two Armaments": [2],  # hand-weighted: unknown which one paired fists trigger
    },
    "sustain": {
        "HP Restoration upon Fist Attacks": rc.heal([0.3]),  # guess: ~0.5 bars from many fast hits x 0.6 coverage
        "HP Restoration upon Greataxe Attacks": rc.heal([0.045]),  # 0.3 x 0.15
        "HP Restoration upon Colossal Weapon Attacks": [0],
        "HP Restoration upon Great Hammer Attacks": [0],
        "Poise": [0, 2, 2.5, 3],  # hand-weighted: trading strikes up close
    },
    "utility": {
        "FP Restoration upon Fist Attacks": [0.5],  # Raider spends little FP; weapon skills only
    },
}
for cat, fams in fist.items():
    rc.CATEGORIES[cat].update(fams)
rc.WEIGHTS = {fam: w for fams in rc.CATEGORIES.values() for fam, w in fams.items()}
rc.CATEGORY = {fam: cat for cat, fams in rc.CATEGORIES.items() for fam in fams}
rc.STACKING |= {"Improved Fist Attack Power", "Improved Attack Power with 3+ Fists Equipped"}
rc.STACKING -= {
    "Improved Colossal Weapon Attack Power",
    "Improved Great Hammer Attack Power",
    "Improved Colossal Sword Attack Power",
    "Improved Attack Power with 3+ Colossal Weapons Equipped",
    "Improved Attack Power with 3+ Great Hammers Equipped",
}
rc.PREFIX_WEIGHTS = [
    ("Starting armament deals", -0.3, "damage"),  # converts the Greataxe, which is short-lived here
    ("Starting armament inflicts blood loss", 0.3, "damage"),
]

FISTS = "Fists"
rc.DORMANT_OK = {FISTS: 0}  # every other class is DORMANT_BAD: it dilutes the fist pool
_breakdown = rc.breakdown


def breakdown(relics):
    """raider_charged.breakdown, except extra Fists copies don't count as dilution."""
    parts = _breakdown(relics)
    dormant = [d for r in relics for d in r.dormant]
    dup = len(dormant) - len(set(dormant))
    parts["penalties"] -= rc.DORMANT_EXTRA * dup
    return parts


rc.breakdown = breakdown


def has_fists(relics):
    return any(FISTS in r.dormant for r in relics)


def top_triples(pool, colors, per_slot, keep, max_curses):
    """Best triples for the given colors, shortlisted per (rally, Fists Dormant Power) bucket.

    Fist Dormant Power relics are always candidates, however low their solo score,
    so the required effect can't fall off the per-slot shortlist.
    """
    pool = [r for r in pool if len(r.curses) <= max_curses]
    cands = []
    for c in colors:
        fits = sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)
        top = fits[:per_slot]
        cands.append(top + [r for r in fits[per_slot:] if FISTS in r.dormant])
    seen = set()
    buckets = {}
    for combo in itertools.product(*cands):
        ids = frozenset(r.id for r in combo)
        if len(ids) < 3 or ids in seen or rc.curse_count(combo) > max_curses:
            continue
        seen.add(ids)
        key = (any(rc.RALLY in r.fams for r in combo), has_fists(combo))
        buckets.setdefault(key, []).append((rc.score(combo), combo))
    out = []
    for b in buckets.values():
        b.sort(key=lambda t: -t[0])
        out += b[: keep // 4]
    return out


def search(relics, normal, deep, per_slot, keep, max_curses=99):
    std = [r for r in relics if r.kind == "standard" and r.solo > rc.DISQUALIFY / 2]
    dp = [r for r in relics if r.kind == "deep" and r.solo > rc.DISQUALIFY / 2]
    nt = top_triples(std, normal, per_slot, keep, max_curses)
    dt = top_triples(dp, deep, per_slot, keep, max_curses)
    results = []
    for _, n in nt:
        for _, d in dt:
            if has_fists(n + d) and rc.curse_count(n + d) <= max_curses:
                results.append((rc.score(n + d), n, d))
    results.sort(key=lambda t: -t[0])
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--vessel")
    ap.add_argument("--per-slot", type=int, default=60)
    ap.add_argument("--keep", type=int, default=2000)
    ap.add_argument("--max-curses", type=int, default=99, help="cap on total curses per loadout")
    args = ap.parse_args()
    relics = rc.load()
    summary = []
    for name, (normal, deep) in rc.VESSELS.items():
        if args.vessel and args.vessel != name:
            continue
        res = search(relics, normal, deep, args.per_slot, args.keep, args.max_curses)
        print(f"=== {name}  normal {normal} / deep {deep}")
        if not res:
            print("  no loadout carries a Fists Dormant Power\n")
            continue
        best = res[0][1] + res[0][2]
        summary.append((res[0][0], name, breakdown(best), any(rc.RALLY in r.fams for r in best)))
        for total, n, d in res[: args.top]:
            print(rc.describe(total, n, d, normal, deep))
        print()
    print("=== summary")
    for s, name, parts, has_rally in sorted(summary, key=lambda t: -t[0]):
        print(f"  {s:6.1f}  {name:30}  {rc.format_parts(parts)}" + ("" if has_rally else "  NO RALLY"))


if __name__ == "__main__":
    main()
