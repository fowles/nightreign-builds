"""Revenant Deep of Night loadout search: incantation caster, general and one-spell variants.

Usage: python3 -I scripts/revenant_incant.py --build {general,oflame,dragonfire,lightning,beast,holy}
       [--top N] [--vessel NAME] [--max-curses N] [--rally X] [--min-focus N]
       python3 -I scripts/revenant_incant.py --inventory

Builds:
  - general:    cast whatever incantations the run's seals drop.
  - oflame:     O, Flame! (Giants' Flame, fire) on the Finger Seal.
  - dragonfire: Dragonfire (Dragon Communion, fire) on the Finger Seal.
  - lightning:  Lightning Spear (Dragon Cult, lightning) on the Finger Seal.
  - beast:      Beast Claw (Bestial, physical) on the Finger Seal.
  - holy:       Wrath of Gold (holy, no school on Fextralife's list) on the Finger Seal.

Every variant requires its `Changes compatible armament's incantation to X` relic. Per wiki.gg
it changes the secondary incantation slot and only works on Revenant's initial Finger Seal, so
a different converter on the same loadout fights for that slot and is penalized.

Damage is modeled as disjoint slices of your total damage, each with tags (self, incant, claw,
family, fire, giants, ...). A buff multiplies every slice carrying its tag (CLAUDE.md coverage
formula, generalized as in scripts/ironeye.py, because a fire spell takes Improved Incantations,
its school and Fire Attack Power Up all at once). Player attack buffs are assumed not to reach
the family slice (unverified).

FP limits a caster, so FP effects raise incantation damage by FP_BINDING of their size. They use
the damage formula but are reported under utility. Sustain, damage negation and curse handling
follow scripts/ironeye.py.
"""
import argparse
import itertools
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))  # -I drops the script dir from sys.path
import ironeye as ie  # noqa: E402
from ironeye import Pct, curse_count, damage_points, ehp, family, format_parts, heal, negation, pct, sustain_points, team  # noqa: E402

ELEMENTS = ("fire", "holy", "lightning", "magic")

# Share of total damage per source. All guesses.
SHARES = {"incant": 0.70, "claw": 0.10, "family": 0.20}

# Incantation mix by (element, school) when casting whatever drops. All guesses.
GENERAL_MIX = {
    ("holy", None): 0.25,  # Rejection and other unschooled holy spells
    ("holy", "fundamentalist"): 0.15,
    ("fire", "giants"): 0.12,
    ("fire", "dragon_communion"): 0.12,
    ("fire", "godslayer"): 0.08,
    ("fire", "frenzied"): 0.05,
    ("lightning", "dragon_cult"): 0.15,
    ("phys", "bestial"): 0.08,
}
FIRE_DROPS = {("fire", s): 0.25 for s in ("giants", "dragon_communion", "godslayer", "frenzied")}

CONVERTER = "Changes compatible armament's incantation to {} at start of expedition"
CONVERTED_SHARE = 0.6  # guess: share of incantation damage from the converted spell
# name -> converted spell, its (element, school), share of the remaining casts that are
# on-element drops (guess: fire seals are common, Bestial ones rare), and those drops' mix.
BUILDS = {
    "general": None,
    "oflame": ("O, Flame!", ("fire", "giants"), 0.7, FIRE_DROPS),
    "dragonfire": ("Dragonfire", ("fire", "dragon_communion"), 0.7, FIRE_DROPS),
    "lightning": ("Lightning Spear", ("lightning", "dragon_cult"), 0.5, {("lightning", "dragon_cult"): 1.0}),
    "beast": ("Beast Claw", ("phys", "bestial"), 0.3, {("phys", "bestial"): 1.0}),
    "holy": ("Wrath of Gold", ("holy", None), 0.6, {("holy", None): 0.5, ("holy", "fundamentalist"): 0.5}),
}
# Wrath of Gold has no school buff, but Fundamentalist still boosts this build's holy drops.
FOCUS_SCHOOL = {"holy": "fundamentalist"}
SCHOOL_EFFECT = {
    "fundamentalist": "Improved Fundamentalist Incantations",
    "giants": "Improved Giants' Flame Incantations",
    "dragon_communion": "Improved Dragon Communion Incantations",
    "godslayer": "Improved Godslayer Incantations",
    "frenzied": "Improved Frenzied Flame Incantations",
    "dragon_cult": "Improved Dragon Cult Incantations",
    "bestial": "Improved Bestial Incantations",
}
INVENTORY = {
    "fire": ("Fire Attack Power Up", "giants", "dragon_communion", "godslayer", "frenzied"),
    "lightning": ("Lightning Attack Power Up", "dragon_cult"),
    "beast claw": ("Physical Attack Up", "bestial"),
    "holy": ("Holy Attack Power Up", "fundamentalist"),
}

FP_BINDING = 0.4  # guess: +1% FP adds +0.4% incantation damage; other casts are limited by time, not FP
RALLY = "Partial HP Restoration upon Post-Damage Attacks"
RALLY_FACTOR = 0.25  # guess: rally on claw hits only; whether spells trigger it is unverified


def fp(sizes):
    """Tier weights for an FP effect of `sizes` percent, as incantation damage."""
    return [Pct(0.4 * s * FP_BINDING * SHARES["incant"], "fp", "incant", s * FP_BINDING) for s in sizes]


def categories(rally):
    """category -> family -> tier weights.

    Stamina (incl. Endurance) is deliberately unweighted. Out-of-focus effects are absent (worth 0).
    Conditional attack buffs (vicinity, vs. status) are 0: the build applies no status.
    """
    damage = {
        "Attack power increased for each Night Invader defeated": pct([20], "self"),  # meta-top
        "Attack power increased for each evergaol prisoner defeated": pct([5], "self"),  # guess
        "Taking attacks improves attack power": pct([2], "self"),  # guess: ~10% x 0.2 uptime from the backline
        "Physical Attack Up": pct([4, 5, 6, 10.5, 12], "phys"),  # wiki.gg, post-1.03
        **{f"{e.title()} Attack Power Up": pct([4.5, 5.5, 6.5, 10.5, 12], e) for e in ELEMENTS},  # wiki.gg
        "Improved Affinity Attack Power": pct([5, 8, 10], "aff"),  # wiki.gg
        "Improved Incantations": pct([6, 8, 10], "incant"),  # base from Millenium guide; +1/+2 guessed
        **{fam: pct([12], school) for school, fam in SCHOOL_EFFECT.items()},  # wiki.gg, Fextralife
        "Improved Claw Attack Power": pct([10], "claw"),  # guess, like other weapon classes
        "Improved Attack Power with 3+ Claws Equipped": pct([1.5], "claw"),  # guess: ~10% x 0.15 availability
        "Faith": pct([0, 1.5, 2.5, 4], "self"),  # guess: Faith S
        "[Revenant] Strengthens family and allies when Ultimate Art is activated": pct([6.25], "family"),  # +25% x 0.25 uptime
        "[Revenant] Power up while fighting alongside family": pct([8], "self"),  # Frederick +10% x 0.8 uptime; other spirits differ
        "[Revenant] Trigger ghostflame explosion during Ultimate Art activation": [0.5],  # hand-weighted: base 20 magic damage looks low
        "[Revenant] Improved Strength, Reduced Faith": pct([-8], "self"),  # guess: Faith -6 on a Faith caster
    }
    sustain = {
        RALLY: heal([1.5 * rally, 1.875 * rally, 2.025 * rally]),  # CLAUDE.md anchor x rally factor
        "Continuous HP Recovery": heal([0.25]),  # guess
        "Slowly restore HP for self and nearby allies when HP is low": heal([0.25]),  # guess
        "Improved Flask HP Restoration": heal([0.1]),
        "HP restored when using medicinal boluses, etc.": heal([0.03, 0.05]),  # guess
        "Increased Maximum HP": ehp([10]),  # guess
        "Max HP increased for each great enemy defeated at a Great Church.": ehp([2.5]),  # guess
        "Vigor": ehp([0, 2, 3.5, 5]),  # guess: % max HP per relic tier; she has only 780 HP
        "[Revenant] Improved Vigor and Endurance, Reduced Mind": ehp([8]),  # guess: Vigor +5
        "Improved Damage Negation at Low HP": ehp([2.5]),  # guess
        "[Revenant] Expend own HP to fully heal nearby allies when activating Art": team([7.5]),  # guess, net of halving your HP
        "Flask Also Heals Allies": team([10]),  # guess
        "Defeating enemies restores HP for allies but not for self": team([2.5]),  # guess
        "Improved Physical Damage Negation": negation([8, 10.5, 12], "physical"),  # base guessed
        "Improved Affinity Damage Negation": negation([6, 10.5, 12], "affinity"),
        **{f"{e.title()} Damage Negation Up": negation([10], e) for e in ELEMENTS},
        **{f"Improved {e.title()} Damage Negation": negation([10, 15, 16], e) for e in ELEMENTS},
        "Poise": [0, 1, 1.5, 2],  # hand-weighted: holds a cast through chip hits
        "Improved Poise & Damage Negation When Knocked Back by Damage": [1],  # hand-weighted
    }
    utility = {
        "[Revenant] Strengthens family and allies when Ultimate Art is activated": [3],  # hand-weighted: allies' +25% x 0.3 uptime
        "Ultimate Art Auto Charge": [0, 4, 5, 6],  # hand-weighted: Immortal March is her core
        "Defeating enemies fills more of the Art gauge": [3, 4],
        "Critical hits fill more of the Art gauge": [1, 1.5],
        "Items confer effect to all nearby allies": [0.5],
        "Increased rune acquisition for self and allies": [0.5],
        # FP: raises incantation damage by FP_BINDING of the size below. Sizes are % more casts.
        "Increased Maximum FP": fp([15]),  # wiki.gg summary (unverified)
        "Reduced FP Consumption": fp([8.7, 14.9, 19]),  # -8/-13/-16% FP (wiki.gg summary, unverified)
        "[Revenant] Increased Max FP upon Ability Activation": fp([20]),  # guess: ~30 ghosts by the last boss, cap +51%
        "Continuous FP Recovery": fp([25]),  # guess
        "Max FP Up with 3+ Sacred Seals Equipped": fp([6]),  # guess: ~30% x 0.2 availability
        "Max FP increased for each Sorcerer's Rise unlocked": fp([8]),  # +18% per rise (wiki.gg) x ~0.45 for the detour
        "FP Restoration upon Claw Attacks": fp([5]),  # guess: claws are a small share
        "FP Restoration upon Successive Attacks": fp([5]),  # guess
        "Madness Continually Recovers FP": fp([2]),  # guess: rarely mad
        "Mind": fp([0, 4, 7, 10]),  # guess: Mind A
        "[Revenant] Improved Vigor and Endurance, Reduced Mind": fp([-25]),  # guess: Mind -11
    }
    return {"damage": damage, "sustain": sustain, "utility": utility}


# Attack buffs: every copy counts, across tiers and duplicates (CLAUDE.md).
STACKING = {
    "Physical Attack Up",
    "Improved Affinity Attack Power",
    "Improved Incantations",
    "Improved Claw Attack Power",
    "Improved Attack Power with 3+ Claws Equipped",
    *SCHOOL_EFFECT.values(),
    *(f"{e.title()} Attack Power Up" for e in ELEMENTS),
}

DORMANT_OK = {"Sacred Seals": 0, "Claws": 0}
DORMANT_BAD = -8
DORMANT_EXTRA = -3  # per Dormant Power beyond the first
CONVERTER_CONFLICT = -3  # per other spell fighting for the secondary incantation slot
GENERAL_CONVERTER = 0.5  # hand-weighted: general build, a guaranteed spell beats Rejection

DISQUALIFY = -1000
CURSE_PENALTY = {
    "Ultimate Art Charging Impaired": DISQUALIFY,  # Immortal March is her core (characters/revenant.md)
    "Taking Damage Causes Death Buildup": -12,  # instant kill; still avoided on a backline caster
    "Taking Damage Causes Sleep Buildup": -10,
    "Taking Damage Causes Madness Buildup": -4,  # Madness also drains FP
    "Taking Damage Causes Poison Buildup": -3,
    "Taking Damage Causes Rot Buildup": -3,
    "Taking Damage Causes Frost Buildup": -3,
    "Taking Damage Causes Blood Loss Buildup": -3,
    "Poison Buildup When Below Max HP": -1.5,
    "Rot Buildup When Below Max HP": -1.5,
    "All Resistances Down": -2.5,
    "Reduced Dexterity and Faith": -6,  # Faith S
    "Reduced Faith and Strength": -6,
    "Reduced Intelligence and Dexterity": -0.5,  # neither stat is used
    "Reduced Strength and Intelligence": -0.5,
    "Reduced Vigor and Arcane": -0.5,  # Arcane is free; HP part in CURSE_MAXHP
    "Reduced Rune Acquisition": -1,
    "Repeated Evasions Lower Damage Negation": -1,
    "Reduced Damage Negation After Evading": -8,  # very bad: missed dodges hurt (CLAUDE.md)
    "Reduced Damage Negation for Flask Usages": -2.5,
    "Reduced Flask HP Restoration": -3,
    "Near Death Reduces Max HP": -2,
    "Lower Attack When Below Max HP": -4,  # bad with `Expend own HP`, which keeps you below max
    "Continuous HP Loss": -3,
}
DUP_CURSE = -1  # extra per repeat of the same curse
ARD_AMPLIFY = -1  # per (Taking Damage curse x All Resistances Down) pair
CURSE_MAXHP = {"Reduced Vigor and Arcane": -5}  # guess: mirrors Vigor +3
UNVERIFIED = -0.5
FOCUS_PER_SLOT = 15

# name -> (normal colors, deep colors); "W" = any. characters/revenant.md
VESSELS = {
    "Revenant's Urn": ("BBY", "BBY"),
    "Revenant's Goblet": ("RRG", "RRG"),
    "Revenant's Chalice": ("BGW", "BYG"),
    "Soot-Covered Revenant's Urn": ("RYY", "RYY"),
    "Sealed Revenant's Urn": ("YBB", "GGR"),
    "Decrepit Revenant's Goblet": ("RRY", "RRY"),  # unverified
    "Forgotten Revenant's Goblet": ("GRR", "YGW"),
    "Sacred Erdtree Grail": ("YYY", "YYY"),
    "Spirit Shelter Grail": ("GGG", "GGG"),
    "Giant's Cradle Grail": ("BBB", "BBB"),
    "Scadutree Grail": ("RRR", "RRR"),
}


def spell_tags(element, school):
    tags = {"self", "incant", element}
    if school:
        tags.add(school)
    if element in ELEMENTS:
        tags.add("aff")
    return frozenset(tags)


class Model:
    """Weights, slices and requirements for one build."""

    def __init__(self, build, rally=RALLY_FACTOR):
        self.build = build
        self.spec = BUILDS[build]
        self.want = self.spec and CONVERTER.format(self.spec[0])
        self.weights = {}
        for cat, fams in categories(rally).items():
            for fam, w in fams.items():
                self.weights.setdefault(fam, []).append((cat, w))
        self.slices = self.make_slices()

    def make_slices(self):
        mix = dict(GENERAL_MIX)
        if self.spec:
            _, spell, on_element, drops = self.spec
            rest = 1 - CONVERTED_SHARE
            mix = {k: v * rest * (1 - on_element) for k, v in GENERAL_MIX.items()}
            for k, v in drops.items():
                mix[k] = mix.get(k, 0) + v * rest * on_element
            mix[spell] = mix.get(spell, 0) + CONVERTED_SHARE
        out = [(SHARES["incant"] * share, spell_tags(*k)) for k, share in mix.items()]
        out.append((SHARES["claw"], frozenset({"self", "claw", "phys"})))  # physical is unverified
        out.append((SHARES["family"], frozenset({"family"})))
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
        self.parsed = []
        self.dormant = []
        self.converters = []
        self.curses = []
        for e in self.effects:
            m = ie.DORMANT_RE.match(e["text"])
            if m:
                self.dormant.append(m.group(1))
            else:
                self.parsed.append(family(e["text"]))
                if e["text"].startswith("Changes compatible armament's incantation"):
                    self.converters.append(e["text"])
            if e["curse"]:
                self.curses.append(e["curse"])
        self.solo = score([self], model)

    def fits(self, slot):
        return slot == "W" or slot == self.color


def breakdown(relics, model):
    """Score split into damage / sustain / utility / penalties; values sum to the total."""
    parts = dict.fromkeys(("damage", "sustain", "utility", "penalties"), 0.0)
    pcts = []
    best = {}  # (family, category) -> best weight, for non-stacking families
    curses = {}
    dormant = []
    converters = set()
    for r in relics:
        for fam, tier in r.parsed:
            for cat, w in model.weights.get(fam, ()):
                v = w[min(tier, len(w) - 1)]
                # Attack buffs and negative weights (stat swaps) always apply.
                if fam in STACKING or v < 0:
                    pcts.append(v) if isinstance(v, Pct) else parts.__setitem__(cat, parts[cat] + v)
                elif v > best.get((fam, cat), 0):
                    best[(fam, cat)] = v
        for c in r.curses:
            curses[c] = curses.get(c, 0) + 1
        dormant += r.dormant
        converters.update(r.converters)
        parts["penalties"] += UNVERIFIED * len(r.unverified)
    for (fam, cat), v in best.items():
        if isinstance(v, Pct):
            pcts.append(v)
        else:
            parts[cat] += v

    if model.want:
        parts["penalties"] += CONVERTER_CONFLICT * len(converters - {model.want})
    elif converters:
        parts["utility"] += GENERAL_CONVERTER
        parts["penalties"] += CONVERTER_CONFLICT * (len(converters) - 1)

    dmg = [b for b in pcts if b.kind == "damage"]
    fps = [b for b in pcts if b.kind == "fp"]
    plain = damage_points(dmg, model.slices)
    parts["damage"] += plain
    parts["utility"] += damage_points(dmg + fps, model.slices) - plain
    selfs = [b for b in pcts if b.kind not in ("damage", "fp")]
    clean = sustain_points(selfs)
    parts["sustain"] += clean
    cursed = [CURSE_MAXHP[c] for c, n in curses.items() if c in CURSE_MAXHP for _ in range(n)]
    parts["penalties"] += sustain_points(selfs, cursed) - clean
    for c, n in curses.items():
        parts["penalties"] += CURSE_PENALTY.get(c, -2) * n + DUP_CURSE * (n - 1)
        if c.startswith("Taking Damage Causes"):
            parts["penalties"] += ARD_AMPLIFY * n * curses.get("All Resistances Down", 0)
    for d in dormant:
        parts["penalties"] += DORMANT_OK.get(d, DORMANT_BAD)
    parts["penalties"] += DORMANT_EXTRA * max(0, len(dormant) - 1)
    return parts


def score(relics, model):
    return sum(breakdown(relics, model).values())


def load(model):
    data = json.loads(ie.DB.read_text())
    return [Relic(r, model) for r in data["relics"] if r["status"] == "active"]


def has_rally(relics):
    return any(f == RALLY for r in relics for f, _ in r.parsed)


def focus_copies(relics, model):
    """On-focus attack buffs carried: (element or physical copies, school copies, generic incantation copies)."""
    if not model.spec:
        element, school = None, None
    else:
        element, school = model.spec[1]
        school = FOCUS_SCHOOL.get(model.build, school)
    el = "Physical Attack Up" if element == "phys" else element and f"{element.title()} Attack Power Up"
    counts = [0, 0, 0]
    for r in relics:
        for f, _ in r.parsed:
            counts[0] += f == el
            counts[1] += f == SCHOOL_EFFECT.get(school)
            counts[2] += f == "Improved Incantations"
    return counts


def focus_count(relics, model):
    """Copies of the buffs this build exists for: element and school, or Improved Incantations on general."""
    el, school, generic = focus_copies(relics, model)
    return el + school if model.spec else generic


def top_triples(pool, colors, per_slot, keep, max_curses, model, require=None):
    """Best triples for the given colors, shortlisted per (rally, focus copies) bucket.

    Converters are always candidates, and so are the best FOCUS_PER_SLOT on-focus relics per slot,
    because attack buffs multiply each other but score low alone.
    """
    pool = [r for r in pool if len(r.curses) <= max_curses]
    cands = []
    for c in colors:
        fit = sorted((r for r in pool if r.fits(c)), key=lambda r: -r.solo)
        focus = [r for r in fit[per_slot:] if focus_count([r], model)][:FOCUS_PER_SLOT]
        cands.append(fit[:per_slot] + focus + [r for r in fit[per_slot:] if model.want in r.converters and r not in focus])
    seen = set()
    buckets = {}
    for combo in itertools.product(*cands):
        ids = frozenset(r.id for r in combo)
        if len(ids) < 3 or ids in seen or curse_count(combo) > max_curses:
            continue
        seen.add(ids)
        if require and not require(combo):
            continue
        key = (has_rally(combo), min(2, focus_count(combo, model)))
        buckets.setdefault(key, []).append((score(combo, model), combo))
    out = []
    for b in buckets.values():
        b.sort(key=lambda t: -t[0])
        out += b[: keep // 4]
    return out


def search(relics, model, normal, deep, per_slot, keep, max_curses, min_focus=0):
    std = [r for r in relics if r.kind == "standard" and r.solo > DISQUALIFY / 2]
    dp = [r for r in relics if r.kind == "deep" and r.solo > DISQUALIFY / 2]
    # Converters are all on standard relics, so the requirement is checked on the normal side.
    need = (lambda n: any(model.want in r.converters for r in n)) if model.want else None
    nt = top_triples(std, normal, per_slot, keep, max_curses, model, need)
    dt = top_triples(dp, deep, per_slot, keep, max_curses, model)
    results = []
    for _, n in nt:
        for _, d in dt:
            if curse_count(n + d) > max_curses:
                continue
            if focus_count(n + d, model) < min_focus:
                continue
            results.append((score(n + d, model), n, d))
    results.sort(key=lambda t: -t[0])
    return results


def describe(total, n, d, normal, deep, model):
    lines = [f"score {total:.1f}  ({format_parts(breakdown(n + d, model))})"]
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
    el, sch, gen = focus_copies(n + d, model)
    lines.append(f"  focus copies: element {el}, school {sch}, Improved Incantations {gen}")
    lines.append(f"  rally: {[r.id for r in n + d if any(f == RALLY for f, _ in r.parsed)] or 'none'}")
    lines.append(f"  curses ({len(all_curses)}): {all_curses}")
    lines.append(f"  dormant: {dormant or 'none'}")
    lines.append(f"  unverified: {flags or 'none'}")
    return "\n".join(lines)


def inventory():
    """Per focus: copies owned of its element and school buffs, and its converters, by color and kind."""
    data = json.loads(ie.DB.read_text())
    active = [r["relic"] for r in data["relics"] if r["status"] == "active"]

    def show(label, match):
        rows = {}
        for r in active:
            if any(match(family(e["text"])[0]) for e in r["effects"]):
                key = (r["kind"], r["color"][0])
                rows[key] = rows.get(key, 0) + 1
        print(f"  {label}: {sum(rows.values())} relics  " + " ".join(f"{k}/{c}:{v}" for (k, c), v in sorted(rows.items())))

    for name, (element, *schools) in INVENTORY.items():
        print(f"== {name}")
        show(element, lambda f, e=element: f == e)
        for s in schools:
            show(SCHOOL_EFFECT[s], lambda f, e=SCHOOL_EFFECT[s]: f == e)
    print("== converters")
    for spell in ("O, Flame!", "Dragonfire", "Lightning Spear", "Beast Claw", "Wrath of Gold"):
        show(spell, lambda f, e=CONVERTER.format(spell): f == e)
    print("== general")
    show("Improved Incantations", lambda f: f == "Improved Incantations")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", choices=BUILDS)
    ap.add_argument("--inventory", action="store_true", help="count on-focus relics and exit")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--vessel")
    ap.add_argument("--per-slot", type=int, default=30)
    ap.add_argument("--keep", type=int, default=300)
    ap.add_argument("--max-curses", type=int, default=99, help="cap on total curses per loadout")
    ap.add_argument("--rally", type=float, default=RALLY_FACTOR, help="share of the melee rally anchor this build gets")
    ap.add_argument("--min-focus", type=int, default=0, help="minimum focus copies (see focus_count)")
    args = ap.parse_args()
    if args.inventory:
        inventory()
        return
    if not args.build:
        ap.error("--build or --inventory is required")
    model = Model(args.build, args.rally)
    relics = load(model)
    summary = []
    for name, (normal, deep) in VESSELS.items():
        if args.vessel and args.vessel != name:
            continue
        res = search(relics, model, normal, deep, args.per_slot, args.keep, args.max_curses, args.min_focus)
        print(f"=== {name}  normal {normal} / deep {deep}")
        if not res:
            print("  no loadout meets the requirements\n")
            continue
        summary.append((res[0][0], name, breakdown(res[0][1] + res[0][2], model), focus_copies(res[0][1] + res[0][2], model)))
        for total, n, d in res[: args.top]:
            print(describe(total, n, d, normal, deep, model))
        print()
    print("=== summary")
    for s, name, parts, focus in sorted(summary, key=lambda t: -t[0]):
        print(f"  {s:6.1f}  {name:30}  {format_parts(parts)}  focus {focus}")


if __name__ == "__main__":
    main()
