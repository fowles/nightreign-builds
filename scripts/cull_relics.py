"""Rank relics for culling: low general value and replaceable within their slot.

Strict dominance (scripts/dominated_relics.py) finds nothing left to drop, so this uses a
looser, build-agnostic rule. Every effect gets a rough "general value" in CLAUDE.md points: its
size for a build that wants it, times the share of builds that want it ("reach"). These are
hand-set guesses, not per-build weights. Curses get a generic penalty.

A relic is KEPT if any of these hold:
  - it appears in a build file (builds/*.md)
  - for some effect worth >= MIN_KEY_VALUE, it is in the top KEEP_PER_FAMILY relics of its
    kind + color carrying that effect family (ranked by tier, then lightest curses, then value)
  - it is in the top KEEP_PER_CHAR relics of its kind + color by total value, for its
    Nightfarer (character-tagged) or for universal relics
Everything else is a cull candidate, worst first.

Usage: python -I scripts/cull_relics.py [--md reports/cull-relics.md]
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "mfk-relicdb.json"

KEEP_PER_FAMILY = 4  # 3 slots of a kind, plus one spare
KEEP_PER_CHAR = 4
MIN_KEY_VALUE = 1.0  # effects below this never protect a relic on their own
UNVERIFIED = -0.5

TIER_RE = re.compile(r"^(.*?) \+(\d+)$")


def tiered(values):
    return lambda t: values[min(t, len(values) - 1)]


def flat(v):
    return lambda t: v


# (pattern, value-by-tier). First match wins. Value = size in points x reach (share of builds).
RULES = [
    # Meta anchors
    (r"^Partial HP Restoration upon Post-Damage Attacks$", tiered([16, 20, 21.6])),  # 20/25/27 x 0.8 melee
    (r"^Attack power increased for each Night Invader defeated$", flat(8)),
    # Stacking attack buffs: Physical Attack Up 4/5/6/10.5/12% at 0.4 pt/% x 0.9 reach
    (r"^Physical Attack Up$", tiered([1.4, 1.8, 2.2, 3.8, 4.3])),
    (r"^(Fire|Holy|Lightning|Magic) Attack Power Up$", tiered([0.8, 1.0, 1.2, 2.1, 2.4])),
    (r"^Improved Affinity Attack Power$", tiered([0.8, 1.0, 1.2, 2.1])),
    (r"^Improved (Sorceries|Incantations)$", tiered([0.8, 1.0, 1.2, 2.1])),
    (r"^Improved Guard Counters$", tiered([1.0, 1.1, 1.3])),  # 23-29% x 0.35 cov x ~0.3 reach
    (r"^Guard counter is given a boost", flat(0.8)),
    (r"^Improved Initial Standard Attack$", tiered([1.0, 1.3, 1.6])),
    (r"^Improved (Melee|Skill) Attack Power$", tiered([1.5, 2])),
    (r"^Improved Critical Hits$", tiered([0.8, 1.0, 1.2])),
    (r"^Improved .* Attack Power$", tiered([0.6, 0.8, 1.0])),  # one weapon class
    (r"^Improved Attack Power with 3\+", flat(0.4)),
    (r"^Improved .*(Sorcery|Incantations|Damage)$", tiered([0.5, 0.6, 0.8])),  # one spell school / item
    (r"^Improved Perfuming Arts$|^Improved Roar & Breath Attacks$", flat(0.4)),
    # Conditional attack buffs (highest tier only)
    (r"^Attack power up when facing", tiered([0.8, 1.0, 1.2])),
    (r"^Physical attack power increases after using grease", tiered([0.6, 0.8, 1.0])),
    (r"in Vicinity (Improves|Increases) Attack Power$", tiered([0.5, 0.6, 0.8])),
    (r"^Taking attacks improves attack power$", flat(1.0)),
    (r"^Attack power increased for each evergaol", flat(0.8)),
    (r"Boost(s)? Attack Power|Attack Power Up|Increase(s)? Attack Power", flat(0.5)),
    # Sustain (highest tier only)
    (r"^Improved Physical Damage Negation$", tiered([3, 3.8, 4.3])),
    (r"^Improved Affinity Damage Negation$", tiered([1.0, 1.7, 2.0])),
    (r"^Improved (Fire|Holy|Lightning|Magic) Damage Negation$", tiered([0.4, 0.6, 0.7])),
    (r"Damage Negation Up$", flat(0.4)),
    (r"^Increased Maximum HP$|^Vigor$", tiered([0.8, 1.2, 1.6, 2.0])),
    (r"^HP Recovery From Successful Guarding$", tiered([1.0, 1.4, 1.6])),
    (r"^HP Restoration upon Thrusting Counterattack$", tiered([1.0, 1.3, 1.5])),
    (r"^HP restored when using medicinal boluses", flat(0.3)),
    (r"^Improved Flask HP Restoration$", tiered([1.0, 1.3])),
    (r"^Flask Also Heals Allies$", flat(1.5)),
    (r"^Slowly restore HP for self and nearby allies", flat(1.0)),
    (r"^Continuous HP Recovery$", flat(2)),
    (r"^Improved Damage Negation at Low HP$|^Improved Poise & Damage Negation When Knocked", flat(0.6)),
    (r"^Poise$", tiered([0.5, 0.8, 1.0, 1.2])),
    (r"^HP Restoration upon", flat(0.4)),  # one weapon class
    (r"^Max HP (Up with|increased for each)", flat(0.4)),
    (r"Restores HP|restores HP", flat(0.3)),
    # Utility
    (r"^Ultimate Art Auto Charge$", tiered([1.0, 1.3, 1.6])),
    (r"fill(s)? more of the Art gauge$", tiered([0.8, 1.0, 1.2])),
    (r"^Improved Stance-Breaking", flat(0.8)),
    (r"^Improved Crystalian sorcery$", tiered([0.5, 0.6, 0.8])),
    (r"^Switching Weapons Adds an Affinity Attack$", flat(1.5)),
    (r"^Improved Poise Near Totem Stela$", flat(0.2)),
    (r"^Character Skill Cooldown Reduction$", tiered([0.8, 1.0, 1.2, 1.4])),
    (r"^Items confer effect to all nearby allies$", flat(0.5)),
    (r"^(Mind|Strength|Dexterity|Intelligence|Faith|Arcane)$", tiered([0.2, 0.4, 0.6, 0.8])),
    (r"^Reduced FP Consumption$|^Increased Maximum FP$|^FP Restoration upon Successive", flat(0.3)),
    (r"^FP Restoration upon|^Max FP", flat(0.1)),
    (r"^Increased rune acquisition|^Rune discount|^Huge rune discount|Earn Runes|Item Discovery", flat(0.3)),
    (r"^Treasure marked upon map$", flat(0.2)),
    (r"^Draw enemy attention while guarding$", flat(0.3)),
    # Zero: stamina, resistances, starting items, armament swaps (CLAUDE.md: stamina is worth 0)
    (r"Stamina|^Endurance$|stamina", flat(0)),
    (r"^Improved .* Resistance$", flat(0.1)),
    (r"in possession at start of expedition$", flat(0)),
    (r"^Changes compatible armament|^Starting armament", flat(0.1)),
    (r"^Dormant Power", flat(-0.3)),  # bad for every build that doesn't use the weapon
]
RULES = [(re.compile(p), f) for p, f in RULES]

# Character-tagged effects: value for that Nightfarer. Stat swaps are near-filler.
TAG_STATS = re.compile(r"\] Improved .*, Reduced ")
TAG_DEFAULT = 2.0

CURSE = {
    "Taking Damage Causes Death Buildup": -6,
    "Taking Damage Causes Sleep Buildup": -5,
    "Reduced Damage Negation After Evading": -5,
    "Ultimate Art Charging Impaired": -4,
    "Taking Damage Causes Madness Buildup": -3,
    "Taking Damage Causes Frost Buildup": -3,
    "Taking Damage Causes Blood Loss Buildup": -3,
    "Taking Damage Causes Rot Buildup": -2.5,
    "Taking Damage Causes Poison Buildup": -2.5,
    "Continuous HP Loss": -3,
    "Reduced Flask HP Restoration": -2,
    "Reduced Damage Negation for Flask Usages": -2,
    "Lower Attack When Below Max HP": -2,
    "Rot Buildup When Below Max HP": -1.5,
    "Poison Buildup When Below Max HP": -1.2,
    "Near Death Reduces Max HP": -1.5,
    "All Resistances Down": -1.5,
    "Reduced Vigor and Arcane": -1.5,
    "Repeated Evasions Lower Damage Negation": -0.5,
    "Reduced Rune Acquisition": -0.5,
}
CURSE_DEFAULT = -0.5  # two-stat reductions: free for most builds


def family_tier(text):
    m = TIER_RE.match(text)
    return (m.group(1), int(m.group(2))) if m else (text, 0)


def effect_value(text):
    fam, tier = family_tier(text)
    if fam.startswith("["):
        return 0.3 if TAG_STATS.search(fam) else TAG_DEFAULT
    for rx, f in RULES:
        if rx.search(fam):
            return f(tier)
    return 0.3  # unknown: assume minor


def load():
    db = json.loads(DB.read_text())
    used = set()
    for p in (ROOT / "builds").glob("*.md"):
        used |= set(re.findall(r"\bR\d{5}\b", p.read_text()))
    relics = []
    for r in db["relics"]:
        if r["status"] != "active":
            continue
        rel = r["relic"]
        unverified = {f.split(":", 1)[1] for f in rel["flags"] if f.startswith("unverified_effect:")}
        effects = [
            {"text": e["text"], "curse": e["curse"], "ft": family_tier(e["text"]),
             "value": effect_value(e["text"]), "unverified": e["text"] in unverified}
            for e in rel["effects"]
        ]
        curse_pen = sum(CURSE.get(e["curse"], CURSE_DEFAULT) for e in effects if e["curse"])
        value = (sum(e["value"] for e in effects) + curse_pen
                 + UNVERIFIED * sum(e["unverified"] for e in effects))
        relics.append({
            "id": r["relic_id"], "name": rel["name"], "color": rel["color"], "kind": rel["kind"],
            "nightfarer": rel["nightfarer"], "effects": effects, "curse_pen": curse_pen,
            "value": value, "used": r["relic_id"] in used,
        })
    return relics


def analyze(relics):
    keep = defaultdict(list)  # id -> reasons
    for r in relics:
        if r["used"]:
            keep[r["id"]].append("in a build")
    by_fam = defaultdict(list)
    by_char = defaultdict(list)
    for r in relics:
        for e in r["effects"]:
            if e["value"] >= MIN_KEY_VALUE:
                by_fam[(r["kind"], r["color"], e["ft"][0])].append((e["ft"][1], r))
        by_char[(r["kind"], r["color"], r["nightfarer"])].append(r)
    for (kind, color, fam), lst in by_fam.items():
        lst.sort(key=lambda x: (-x[0], -x[1]["curse_pen"], -x[1]["value"]))
        for tier, r in lst[:KEEP_PER_FAMILY]:
            keep[r["id"]].append(f"top {fam}" + (f" +{tier}" if tier else ""))
    for key, lst in by_char.items():
        lst.sort(key=lambda r: -r["value"])
        for r in lst[:KEEP_PER_CHAR]:
            keep[r["id"]].append(f"top {key[2] or 'universal'} by value")
    cull = sorted((r for r in relics if r["id"] not in keep), key=lambda r: r["value"])
    return cull, keep


def fmt_effects(r):
    parts = []
    for e in r["effects"]:
        s = e["text"] + (" (unverified)" if e["unverified"] else "")
        if e["curse"]:
            s += f" ⟶ curse: *{e['curse']}*"
        parts.append(s)
    return "<br>".join(parts)


def main():
    args = sys.argv[1:]
    md_out = args[args.index("--md") + 1] if "--md" in args else None
    relics = load()
    cull, keep = analyze(relics)
    tiers = [
        ("Junk (value ≤ 1): safe to clear", [r for r in cull if r["value"] <= 1.0]),
        ("Weak (value 1–5): clear unless you want a spare",
         [r for r in cull if 1.0 < r["value"] <= 5.0]),
        ("Outclassed but decent (value > 5): clear only if you need the space",
         [r for r in cull if r["value"] > 5.0]),
    ]
    lines = [
        "# Relic cull candidates",
        "",
        f"Generated by `scripts/cull_relics.py`. Active relics: {len(relics)}. "
        f"Kept: {len(keep)}. Cull candidates: {len(cull)} ("
        + "; ".join(f"{len(g)} {t.split(' (')[0].lower()}" for t, g in tiers) + ").",
        "",
        "Value is a rough, build-agnostic guess in CLAUDE.md points (effect size × share of builds "
        "that want it, minus generic curse penalties). A relic is kept if it is used in a build, "
        f"is in the top {KEEP_PER_FAMILY} of its kind + color for any effect worth ≥ {MIN_KEY_VALUE}, "
        f"or is in the top {KEEP_PER_CHAR} of its kind + color by value for its Nightfarer. "
        "Everything below is none of those, worst first.",
        "",
    ]
    for title, group in tiers:
        lines += [f"## {title}", "", "| Relic | Kind | Color | Nightfarer | Value | Effects |",
                  "|---|---|---|---|---|---|"]
        for r in group:
            lines.append(f"| `{r['id']}` {r['name']} | {r['kind']} | {r['color']} | "
                         f"{r['nightfarer'] or '—'} | {r['value']:.1f} | {fmt_effects(r)} |")
        lines.append("")
    text = "\n".join(lines)
    if md_out:
        Path(md_out).write_text(text)
    print(lines[2])


if __name__ == "__main__":
    main()
