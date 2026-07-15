#!/usr/bin/env python3
"""Generate plain-language rationale STATEMENTS for every reviewed governance action.

For each deterministic decision the engine has produced, this asks Claude to write a
short, public-facing explanation of WHY BEACN voted the way it did — for delegators to
read on the website. The model is given BEACN's deterministic verdict and the exact
facts that produced it, and is instructed to EXPLAIN that verdict faithfully. It never
changes, second-guesses, or invents facts.

Output: data/output/public/statements.json
        { action_id: { statement, decision, model, generated_at, source_input_hash } }

Resumable: actions already present are skipped (use --force to regenerate). Saves after
every item so an interrupted run loses nothing.

Ethos / reproducibility: the binding rationale and its hashes remain the deterministic
record (rationale.json / rationales.json). These statements are a clearly-labeled
plain-language layer whose only inputs are that public deterministic record.

  ANTHROPIC_API_KEY=...  python3 scripts/generate_statements.py [--limit N] [--force] [--dry-run]
  BEACN_STATEMENT_MODEL  overrides the model (default claude-opus-4-8).
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from beacn_drep.ids import canonical_action_id  # noqa: E402

RUNS = ROOT / "data" / "output"
OUT = ROOT / "data" / "output" / "public" / "statements.json"
RESOURCES = Path(os.environ.get("BEACN_RESOURCES_REPO", Path.home() / ".openclaw/workspace/beacn-drep-resources"))
ACTIONS_CSV = RESOURCES / "data" / "input" / "governance" / "governance_actions_all.csv"
MODEL = os.environ.get("BEACN_STATEMENT_MODEL", "claude-opus-4-8")
OFFLINE_REVIEW = os.environ.get("BEACN_DREP_OFFLINE_REVIEW", "").strip().lower() in ("1", "true", "yes")

SYSTEM = (
    "You write short, public-facing explanations of how the BEACN autonomous Cardano DRep voted on "
    "governance actions, for delegators to read on a transparency website. You are given BEACN's "
    "DETERMINISTIC verdict and the exact facts that produced it. Your only job is to EXPLAIN that "
    "verdict in clear, neutral, professional language — never to change it, second-guess it, or add "
    "facts that were not provided. Rules:\n"
    "1. State the verdict and its core reasoning in 2-4 sentences of plain prose.\n"
    "2. Use ONLY the supplied verdict, facts, inferences, and uncertainty. Invent nothing.\n"
    "3. Be diplomatic and respectful: critique the proposal, never people.\n"
    "4. For NEEDS_MORE_INFO or ABSTAIN, make clear it is a conservative, evidence-based hold, and "
    "state what additional evidence would let BEACN reach a directional vote, when that is given.\n"
    "5. No markdown, no headings, no bullet points, no preamble — return only the explanation paragraph."
)


def load_titles() -> dict[str, str]:
    """Titles under BOTH spellings, so a canonical key finds a row filed under either."""
    out: dict[str, str] = {}
    if ACTIONS_CSV.exists():
        with ACTIONS_CSV.open(newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                aid = r.get("action_id", "")
                if not aid:
                    continue
                title = r.get("metadata_title") or ""
                out.setdefault(aid, title)
                key = canonical_action_id(aid)
                if title or key not in out:
                    out[key] = title
    return out


def latest_rationales() -> dict[str, dict]:
    """Latest decision per action, keyed by CANONICAL id (see ids.py).

    Keying by the raw action_id published the same statement twice — once per id
    spelling — as duplicate top-level keys in statements.json. One action, one key;
    the source spelling survives inside the entry as `alias_action_id`.
    """
    by: dict[str, tuple[int, dict]] = {}
    for d in RUNS.iterdir():
        if not d.is_dir() or d.name == "public":
            continue
        p = d / "rationale.json"
        if not p.exists():
            continue
        try:
            j = json.loads(p.read_text())
        except Exception:
            continue
        aid = j.get("action_id")
        if not aid:
            continue
        key = canonical_action_id(aid)
        m = p.stat().st_mtime_ns
        if key not in by or m > by[key][0]:
            by[key] = (m, j)
    return {aid: j for aid, (m, j) in by.items()}


def canonicalize_store(store: dict) -> dict:
    """Fold an existing statements store onto canonical keys.

    Where both spellings of one action were published, the newer statement wins and the
    losing spelling is preserved as `alias_action_id` inside the entry — an alias FIELD,
    never a duplicate top-level key.
    """
    out: dict[str, dict] = {}
    for aid, entry in sorted(store.items()):
        key = canonical_action_id(aid)
        if aid != key:
            entry.setdefault("alias_action_id", aid)
        prev = out.get(key)
        if prev is None:
            out[key] = entry
            continue
        keep, drop = ((entry, prev)
                      if (entry.get("generated_at") or "") > (prev.get("generated_at") or "")
                      else (prev, entry))
        if drop.get("alias_action_id") and not keep.get("alias_action_id"):
            keep["alias_action_id"] = drop["alias_action_id"]
        out[key] = keep
    return out


def build_user(aid: str, j: dict, title: str) -> str:
    def lines(key):
        items = [x for x in (j.get(key) or []) if x]
        return "\n".join(f"- {x}" for x in items) or "- (none)"
    reason = j.get("abstain_reason_code") or j.get("needs_more_info_reason_code") or "n/a"
    return (
        f"Governance action: {title or aid}\n"
        f"Action type: {j.get('action_type')}\n"
        f"BEACN's verdict: {j.get('recommendation')}\n"
        f"Reason code: {reason}\n"
        f"Score: {j.get('score')}   Confidence: {j.get('confidence')}\n\n"
        f"Facts that drove the verdict:\n{lines('facts')}\n\n"
        f"Inferences:\n{lines('inferences')}\n\n"
        f"Residual uncertainty:\n{lines('uncertainty')}\n\n"
        f"Missing evidence:\n{lines('missing_evidence')}\n\n"
        f"Write the public explanation of why BEACN voted {j.get('recommendation')} on this action."
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--force", action="store_true", help="regenerate even if already present")
    ap.add_argument("--dry-run", action="store_true", help="show counts + a sample prompt, no API calls")
    args = ap.parse_args()

    rats = {a: j for a, j in latest_rationales().items() if not str(a).startswith("ga_")}
    titles = load_titles()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    store = canonicalize_store(json.loads(OUT.read_text())) if OUT.exists() else {}
    todo = [aid for aid in rats if args.force or aid not in store]
    todo.sort()
    if args.limit:
        todo = todo[: args.limit]
    mode = "offline (engine human_message + review tree)" if OFFLINE_REVIEW else MODEL
    print(f"{len(rats)} actions on record · {len(store)} already have statements · {len(todo)} to generate · model {mode}")

    if args.dry_run:
        if todo:
            print("\n--- sample SYSTEM ---\n" + SYSTEM[:400] + " …")
            print("\n--- sample USER prompt ---\n" + build_user(todo[0], rats[todo[0]], titles.get(todo[0], "")))
        return 0

    # Persist the canonical-key fold even when nothing new is generated — duplicate
    # id-spelling keys must leave the published artifact, not wait for the next statement.
    if OUT.exists():
        folded = json.dumps(store, indent=2, sort_keys=True) + "\n"
        if folded != OUT.read_text():
            OUT.write_text(folded)
            print(f"statements store canonicalized: {len(store)} entries")

    if OFFLINE_REVIEW:
        from beacn_drep.exporters.export_public_artifacts import _assessment_extract, _top_fixes

        for i, aid in enumerate(todo, 1):
            j = rats[aid]
            text = (j.get("human_message") or "").strip()
            if not text:
                text = " ".join([x for x in (j.get("inferences") or []) if x]).strip()
            if not text:
                text = f"BEACN records {j.get('recommendation')} on this action based on the deterministic review record."
            # Always close with the acknowledged counter-case and the concrete
            # path to a different vote — the two things delegators and
            # proposers most need from a rationale.
            rec = (j.get("recommendation") or "").upper()
            ax = _assessment_extract(j)
            extra = []
            counter = ax["strongest_yes"] if rec in ("NO", "ABSTAIN", "NEEDS_MORE_INFO") else ax["strongest_no"]
            if counter and counter.lower()[:40] not in text.lower():
                label = "The strongest case for the other side" if rec in ("YES", "NO") else "The strongest case for voting anyway"
                extra.append(f"{label}: {counter}")
            fixes = [f.rstrip('.') for f in _top_fixes({}, j)[:3]]
            if fixes and rec != "YES":
                target = "YES" if rec == "NO" else "a directional vote"
                extra.append(f"What would move BEACN to {target}: " + "; ".join(fixes) + ".")
            if extra:
                text = text + "\n\n" + " ".join(extra)
            store[aid] = {
                "statement": text,
                "decision": j.get("recommendation"),
                "model": "deterministic-heuristic",
                "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "source_input_hash": j.get("input_hash"),
            }
            if (j.get("action_id") or aid) != aid:
                store[aid]["alias_action_id"] = j["action_id"]
            print(f"[{i}/{len(todo)}] {str(j.get('recommendation')):16} {(titles.get(aid) or aid)[:54]}")
        OUT.write_text(json.dumps(store, indent=2, sort_keys=True) + "\n")
        print(f"done · {len(store)} offline statements in {OUT}")
        return 0

    import anthropic  # imported here so --dry-run works without the SDK
    client = anthropic.Anthropic()
    for i, aid in enumerate(todo, 1):
        j = rats[aid]
        try:
            resp = client.messages.create(
                model=MODEL, max_tokens=400, system=SYSTEM,
                messages=[{"role": "user", "content": build_user(aid, j, titles.get(aid, ""))}],
            )
        except Exception as e:  # noqa: BLE001 - keep going; resumable
            print(f"[{i}/{len(todo)}] ERROR {aid}: {e}", file=sys.stderr)
            continue
        if resp.stop_reason == "refusal":
            text = ""
        else:
            text = "".join(b.text for b in resp.content if b.type == "text").strip()
        if not text:
            print(f"[{i}/{len(todo)}] empty/refusal, skipping {aid}", file=sys.stderr)
            continue
        store[aid] = {
            "statement": text,
            "decision": j.get("recommendation"),
            "model": MODEL,
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "source_input_hash": j.get("input_hash"),
        }
        if (j.get("action_id") or aid) != aid:
            store[aid]["alias_action_id"] = j["action_id"]
        OUT.write_text(json.dumps(store, indent=2, sort_keys=True) + "\n")  # save each time
        print(f"[{i}/{len(todo)}] {str(j.get('recommendation')):16} {(titles.get(aid) or aid)[:54]}")
        time.sleep(0.15)

    print(f"done · {len(store)} statements in {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
