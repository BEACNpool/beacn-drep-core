#!/usr/bin/env python3
"""Record immutable public rationale anchors for the latest active runs."""
from __future__ import annotations

import csv
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = ROOT.parent / "beacn-drep-resources"
RUNS = ROOT / "data" / "output"
ACTIVE_CSV = RESOURCES / "data" / "input" / "governance" / "governance_actions_active.csv"
PUBLIC_BASE = os.environ.get(
    "BEACN_PUBLIC_BASE_URL",
    "https://beacnpool.github.io/beacn-drep-web/data/output/public",
).rstrip("/")


def blake2b_256(path: Path) -> str:
    digest = hashlib.blake2b(digest_size=32)
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def latest_runs() -> dict[str, Path]:
    selected: dict[str, Path] = {}
    for run_dir in RUNS.iterdir():
        rationale_path = run_dir / "rationale.json"
        if not run_dir.is_dir() or run_dir.name == "public" or not rationale_path.exists():
            continue
        rationale = json.loads(rationale_path.read_text(encoding="utf-8"))
        action_id = rationale.get("action_id")
        if not action_id:
            continue
        current = selected.get(action_id)
        if current is None or rationale_path.stat().st_mtime_ns > (current / "rationale.json").stat().st_mtime_ns:
            selected[action_id] = run_dir
    return selected


def main() -> None:
    with ACTIVE_CSV.open(newline="", encoding="utf-8") as handle:
        active_ids = {row["action_id"] for row in csv.DictReader(handle)}

    runs = latest_runs()
    plan = []
    missing = []
    for action_id in sorted(active_ids):
        run_dir = runs.get(action_id)
        if run_dir is None:
            missing.append(action_id)
            continue

        markdown_path = run_dir / "rationale.md"
        rationale_path = run_dir / "rationale.json"
        rationale = json.loads(rationale_path.read_text(encoding="utf-8"))
        anchor_hash = blake2b_256(markdown_path)
        anchor_url = f"{PUBLIC_BASE}/r/{anchor_hash[:24]}.md"
        rationale["rationale_anchor_url"] = anchor_url
        rationale["rationale_anchor_hash"] = anchor_hash
        rationale_path.write_text(json.dumps(rationale, indent=2) + "\n", encoding="utf-8")
        plan.append({
            "action_id": action_id,
            "run_id": run_dir.name,
            "recommendation": rationale.get("recommendation"),
            "rationale_anchor_url": anchor_url,
            "rationale_anchor_hash": anchor_hash,
        })

    output = {"active_actions": len(active_ids), "prepared": len(plan), "missing_runs": missing, "runs": plan}
    (RUNS / "live_vote_plan.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    if missing:
        raise SystemExit("active actions are missing deterministic runs")


if __name__ == "__main__":
    main()
