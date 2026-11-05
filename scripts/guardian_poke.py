"""Guardian Deep of Night loadout search: guard and poke, stacking Improved Initial Standard Attack (ISA).

Usage: python3 -I scripts/guardian_poke.py [--top N] [--min-isa N] [--initial SHARE] [--base ID,ID,ID]
       [--max-curses N]

Build: Guardian holds guard and answers with single halberd light attacks (thrusts), so most
pokes open a fresh chain and get every ISA copy. Guard counters are strong attacks, which ISA
doesn't cover (Game8), so they drop to a smaller share of damage.

The three normal slots are fixed to --base (your rule), and only vessels whose normal slots
fit those relics are searched. Every deep triple from the shortlist is scored as a full six-slot
set. ISA relics and rally relics are always on the shortlist, and rally is required.

Reuses the scoring engine in scripts/guardian_sustain.py (damage and sustain products, curses,
stacking, vessels). This script replaces its coverage and weights before any relic is scored;
everything not overridden here is shared.
"""
import argparse
import itertools
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script dir from sys.path
import guardian_sustain as gs  # noqa: E402

ISA = "Improved Initial Standard Attack"
BASE = ("R01922", "R00156", "R01208")

# Share of this build's total damage each scope covers (CLAUDE.md "Coverage"). All guesses.
gs.COVERAGE.clear()
gs.COVERAGE.update({
    "all": 1.0,  # halberd hits, skills, counters: effectively all physical
    "initial": 0.5,  # guess: single pokes that open a chain; the main damage source
    "guard_counter": 0.15,  # guess: still taken on big openings
    "skill": 0.05,  # guess: Whirlwind is used for its negation buff, not its damage
    "crit": 0.03,  # guess: ripostes/backstabs are rare from guard
})

poke = {
    "damage": {
        ISA: gs.pct([15], "initial"),  # wiki.gg; copies stack (confirmed by you). Game8 says ~12-13%
        "Improved Guard Counters": gs.pct([23, 25, 29], "guard_counter"),  # rescoped to the smaller share
        "Guard counter is given a boost based on current HP": gs.pct([18], "guard_counter"),  # guess
        "Improved Skill Attack Power": gs.pct([15], "skill"),
        "Improved Critical Hits": gs.pct([18, 23], "crit"),
    },
    "sustain": {
        # Pokes into attacking enemies are thrust counters: 15 hits x 2.5% / 3.3% (hit count guessed)
        "HP Restoration upon Thrusting Counterattack": gs.heal([0.375, 0.495]),
    },
}
for cat, fams in poke.items():
    gs.CATEGORIES[cat].update(fams)
gs.WEIGHTS = {fam: w for fams in gs.CATEGORIES.values() for fam, w in fams.items()}
gs.CATEGORY = {fam: cat for cat, fams in gs.CATEGORIES.items() for fam in fams}
gs.STACKING.add(ISA)


def isa_copies(relics):
    return sum(1 for r in relics for e in r.effects if gs.family(e["text"])[0] == ISA)


def has_rally(relics):
    return any(gs.RALLY in r.fams for r in relics)


def arrange(base, colors):
    """`base` ordered to fit the slot `colors`, or None if the vessel can't hold them."""
    for perm in itertools.permutations(base):
        if all(r.fits(c) for r, c in zip(perm, colors)):
            return perm
    return None


def search(relics, normal, deep, per_slot, min_isa, max_curses):
    """Every deep triple from the shortlist, scored with the fixed normal side."""
    pool = [r for r in relics if r.kind == "deep" and r.solo > gs.DISQUALIFY / 2 and len(r.curses) <= max_curses]
    cands = []
    for c in deep:
        fits = sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)
        cands.append(fits[:per_slot] + [r for r in fits[per_slot:] if isa_copies([r]) or gs.RALLY in r.fams])
    seen = set()
    results = []
    for combo in itertools.product(*cands):
        ids = frozenset(r.id for r in combo)
        if len(ids) < 3 or ids in seen:
            continue
        seen.add(ids)
        six = normal + combo
        if gs.curse_count(six) > max_curses or isa_copies(six) < min_isa or not has_rally(six):
            continue
        results.append((gs.score(six), normal, combo))
    results.sort(key=lambda t: -t[0])
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--min-isa", type=int, default=0, help="minimum ISA copies across all six slots")
    ap.add_argument("--initial", type=float, default=gs.COVERAGE["initial"], help="share of damage from chain-opening pokes")
    ap.add_argument("--base", default=",".join(BASE), help="the three relics fixed in the normal slots")
    ap.add_argument("--per-slot", type=int, default=60)
    ap.add_argument("--max-curses", type=int, default=99, help="cap on total curses per loadout")
    args = ap.parse_args()
    gs.COVERAGE["initial"] = args.initial
    relics = gs.load()
    by_id = {r.id: r for r in relics}
    base = [by_id[i] for i in args.base.split(",")]
    for name, (normal, deep) in gs.VESSELS.items():
        fixed = arrange(base, normal)
        if fixed is None:
            print(f"--- {name} (normal {normal}): can't hold the base relics")
            continue
        res = search(relics, fixed, deep, args.per_slot, args.min_isa, args.max_curses)
        print(f"=== {name}  normal {normal} / deep {deep}")
        for total, n, d in res[: args.top]:
            print(gs.describe(total, n, d, normal, deep))
            print(f"  ISA copies: {isa_copies(n + d)}")
        if not res:
            print("  no loadout meets the requirements")
        print()


if __name__ == "__main__":
    main()
