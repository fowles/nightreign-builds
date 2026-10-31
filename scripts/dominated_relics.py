"""Find relics that are strictly dominated by others, so they can be dropped.

B dominates A when, with absolutely no trade-off, B is at least as good in every slot A fits:
  - same kind (standard/deep) and same color
  - every effect of A is matched by a distinct effect of B in the same family at an equal or
    higher tier ("X" < "X +1" < "X +2" ...)
  - B's curses are a sub-multiset of A's curses (where a curse is attached doesn't matter)
  - B's extra effects carry no possible downside: no Dormant Powers, no built-in stat
    reductions or drawbacks, no armament-skill swaps, no aggro

Dominance needs a matching that uses only scanner-verified effects to count as "clean";
anything resting on an `unverified_effect` flag is reported separately.

Up to three relics of one kind share a loadout, so a relic is only safe to drop when at least
three *kept* relics dominate it: then any loadout using it can swap in one not already there.
Relics are walked best-first (topological order of dominance) and kept unless three kept
relics already dominate them.

Usage: python -I scripts/dominated_relics.py [mfk-relicdb.json] [--md builds/out.md]
"""

import json
import re
import sys
from collections import Counter, defaultdict
from itertools import permutations
from pathlib import Path

SLOTS_PER_KIND = 3

# Extra effects on a dominator that could hurt some build, so they break dominance.
DRAWBACK = re.compile(
    r"Dormant Power|Reduced|Lowers|\bbut\b|Suffer|Changes compatible armament|"
    r"Starting armament|Draw enemy attention|Taking Damage|Near Death",
    re.IGNORECASE,
)
TIER = re.compile(r"^(.*) \+(\d+)$")
# Families where a second copy in the loadout adds nothing: defensive and healing buffs (only
# the highest tier counts) and run-setup effects that can only apply once. A relic made only of
# these needs just one kept dominator. Everything else might stack, so it needs three.
NON_STACKING = re.compile(
    r"Damage Negation|Poise|HP Restor|HP restor|restores HP|Max HP|Resistance|"
    r"Dormant Power|Changes compatible armament|Starting armament",
)


def family_tier(text):
    m = TIER.match(text)
    return (m.group(1), int(m.group(2))) if m else (text, 0)


def load(path):
    db = json.loads(Path(path).read_text())
    relics = []
    for r in db["relics"]:
        if r["status"] != "active":
            continue
        rel = r["relic"]
        unverified = {f.split(":", 1)[1] for f in rel["flags"] if f.startswith("unverified_effect:")}
        relics.append({
            "id": r["relic_id"],
            "name": rel["name"],
            "color": rel["color"],
            "kind": rel["kind"],
            "effects": [
                {"text": e["text"], "curse": e["curse"], "ft": family_tier(e["text"]),
                 "unverified": e["text"] in unverified}
                for e in rel["effects"]
            ],
            "curses": Counter(e["curse"] for e in rel["effects"] if e["curse"]),
            "flagged": bool(unverified),
        })
    return relics


def dominates(b, a):
    """None if b doesn't weakly dominate a, else 'clean' or 'flagged'."""
    if b["curses"] - a["curses"]:  # b has a curse a lacks
        return None
    if len(b["effects"]) < len(a["effects"]):
        return None
    best = None
    for perm in permutations(range(len(b["effects"])), len(a["effects"])):
        ok, flagged = True, a["flagged"]
        for ea, j in zip(a["effects"], perm):
            eb = b["effects"][j]
            if eb["ft"][0] != ea["ft"][0] or eb["ft"][1] < ea["ft"][1]:
                ok = False
                break
            flagged |= eb["unverified"]
        if not ok:
            continue
        extras = [b["effects"][j] for j in range(len(b["effects"])) if j not in perm]
        if any(DRAWBACK.search(e["text"]) for e in extras):
            continue
        flagged |= any(e["unverified"] for e in extras)
        verdict = "flagged" if flagged else "clean"
        if verdict == "clean":
            return verdict
        best = verdict
    return best


def analyze(relics):
    groups = defaultdict(list)
    for r in relics:
        groups[(r["kind"], r["color"])].append(r)

    # dom[a_id] = {b_id: verdict} for every b that weakly dominates a
    dom = defaultdict(dict)
    for members in groups.values():
        for a in members:
            for b in members:
                if a is not b and (v := dominates(b, a)):
                    dom[a["id"]][b["id"]] = v

    def strictly(b, a):
        return b in dom[a] and a not in dom[b]

    # Best-first order: a relic comes after everything that strictly dominates it.
    by_id = {r["id"]: r for r in relics}
    depth = {}

    def d(rid):
        if rid not in depth:
            depth[rid] = 1 + max((d(b) for b in dom[rid] if strictly(b, rid)), default=-1)
        return depth[rid]

    order = sorted(by_id, key=lambda rid: (d(rid), rid))

    def needed(r):
        stacks = any(not NON_STACKING.search(e["text"]) for e in r["effects"])
        return SLOTS_PER_KIND if stacks else 1

    kept, drop = set(), {}
    for rid in order:
        clean_kept = [b for b, v in dom[rid].items() if v == "clean" and b in kept]
        if len(clean_kept) >= needed(by_id[rid]):
            drop[rid] = clean_kept
        else:
            kept.add(rid)

    # Dominated, but by too few kept relics, or only via flagged effects. Exact duplicates
    # (mutual dominance only) aren't listed: neither copy is worse.
    partial = {
        rid: dom[rid] for rid in kept
        if any(strictly(b, rid) or b in drop for b in dom[rid])
    }
    return by_id, dom, drop, partial, kept


def fmt_effects(r):
    parts = []
    for e in r["effects"]:
        s = e["text"]
        if e["curse"]:
            s += f" [curse: {e['curse']}]"
        if e["unverified"]:
            s += " (unverified)"
        parts.append(s)
    return "; ".join(parts)


def main():
    args = sys.argv[1:]
    md_out = None
    if "--md" in args:
        i = args.index("--md")
        md_out = args[i + 1]
        del args[i:i + 2]
    path = args[0] if args else "mfk-relicdb.json"

    relics = load(path)
    by_id, dom, drop, partial, kept = analyze(relics)

    lines = [
        f"Active relics: {len(relics)}. Safe to drop: {len(drop)}. Kept: {len(kept)}.",
        "",
        "## Safe to drop",
        "",
        "Each is dominated, with no trade-off, by kept relics of the same kind and color: at "
        "least one if all its effects are non-stacking (defensive, healing, Dormant Power, "
        "armament swaps), otherwise at least three.",
        "",
        "| Drop | Kind | Color | Effects | Dominated by (kept) |",
        "|---|---|---|---|---|",
    ]
    for rid in sorted(drop, key=lambda x: (by_id[x]["kind"], by_id[x]["color"], x)):
        r = by_id[rid]
        doms = ", ".join(sorted(drop[rid])[:5]) + (" …" if len(drop[rid]) > 5 else "")
        lines.append(f"| {rid} | {r['kind']} | {r['color']} | {fmt_effects(r)} | "
                     f"{doms} ({len(drop[rid])}) |")

    lines += [
        "",
        "## Dominated but kept",
        "",
        "Strictly dominated, but kept: it has a possibly-stacking effect and fewer than three "
        "kept dominators (dropping could cost a loadout that wants several copies), or the "
        "dominance rests on an `unverified_effect` flag. Review by hand.",
        "",
        "| Relic | Kind | Color | Effects | Dominators |",
        "|---|---|---|---|---|",
    ]
    for rid in sorted(partial, key=lambda x: (by_id[x]["kind"], by_id[x]["color"], x)):
        r = by_id[rid]
        doms = ", ".join(f"{b}{'' if v == 'clean' else '?'}" + ("" if b in kept else "↓")
                         for b, v in sorted(partial[rid].items()))
        lines.append(f"| {rid} | {r['kind']} | {r['color']} | {fmt_effects(r)} | {doms} |")
    lines += ["", "`?` = relies on an unverified effect; `↓` = that dominator is itself dropped."]

    text = "\n".join(lines) + "\n"
    if md_out:
        Path(md_out).write_text(text)
    print(text)


if __name__ == "__main__":
    main()
