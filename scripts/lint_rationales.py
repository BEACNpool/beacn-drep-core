#!/usr/bin/env python3
"""Rationale QA lint — publish gate for the public decision record.

Walks the latest engine run per ACTIVE action and checks that what we are about
to publish is internally consistent and free of template artifacts:

  CRITICAL (exit 1 — abort publish):
    * the plain-language message names a different verdict than the vote
    * recommendation missing / not a known verdict
    * empty human message

  WARN (exit 0 — printed + written to the report, publish proceeds):
    * template artifacts ('..', 'The recorded treasury amount is')
    * counterargument claims the proposal 'clears the evidence gates' while
      blocking questions remain open
    * published confidence above the 0.90 doctrine cap
    * message under 200 chars (too thin to inform a delegator)

Report: data/output/lint_report.json
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from beacn_drep.llm import message_matches_recommendation  # noqa: E402

RESOURCES = ROOT.parent / "beacn-drep-resources"
ACTIVE_CSV = RESOURCES / "data/input/governance/governance_actions_active.csv"
RUNS = ROOT / "data" / "output"
REPORT = RUNS / "lint_report.json"
VERDICTS = {"YES", "NO", "ABSTAIN", "NEEDS_MORE_INFO"}
TEMPLATE_ARTIFACTS = ("The recorded treasury amount is", " ..", "..\n")


def latest_runs(active_ids: set[str]) -> dict[str, Path]:
    latest: dict[str, Path] = {}
    for d in RUNS.iterdir():
        if not d.is_dir() or d.name == "public" or not (d / "rationale.json").exists():
            continue
        aid = d.name.rsplit("-", 1)[0]
        if aid not in active_ids:
            continue
        if aid not in latest or d.stat().st_mtime > latest[aid].stat().st_mtime:
            latest[aid] = d
    return latest


def lint_run(run_dir: Path) -> tuple[list[str], list[str]]:
    critical: list[str] = []
    warns: list[str] = []
    r = json.loads((run_dir / "rationale.json").read_text(encoding="utf-8"))
    rec = (r.get("recommendation") or "").upper()
    message = r.get("human_message") or ""

    if rec not in VERDICTS:
        critical.append(f"unknown recommendation {rec!r}")
    if not message.strip():
        critical.append("empty human message")
    elif not message_matches_recommendation(message, rec):
        critical.append(f"message names a different verdict than {rec}")

    for artifact in TEMPLATE_ARTIFACTS:
        if artifact in message:
            warns.append(f"template artifact in message: {artifact!r}")
    if ".." in message.replace("...", ""):
        warns.append("double period in message")
    if len(message.strip()) < 200:
        warns.append(f"message is thin ({len(message.strip())} chars)")

    conf = float(r.get("confidence") or 0.0)
    if conf > 0.90:
        warns.append(f"confidence {conf} exceeds 0.90 doctrine cap")

    blockers = (r.get("assessment") or {}).get("blocking_questions") or []
    counter = ""
    for s in (r.get("assessment") or {}).get("sections", []):
        if s.get("title") == "Counterargument pass":
            counter = " ".join(s.get("findings") or [])
    if blockers and "clears the evidence gates" in counter:
        warns.append("counterargument claims gates cleared while blockers remain open")
    return critical, warns


def main() -> int:
    with ACTIVE_CSV.open(newline="", encoding="utf-8") as f:
        active_ids = {row["action_id"] for row in csv.DictReader(f)}
    runs = latest_runs(active_ids)

    report = {"checked": len(runs), "critical": {}, "warnings": {}}
    for aid, run_dir in sorted(runs.items()):
        critical, warns = lint_run(run_dir)
        if critical:
            report["critical"][aid] = critical
        if warns:
            report["warnings"][aid] = warns

    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    for aid, items in report["critical"].items():
        print(f"CRITICAL {aid[:32]}..: {'; '.join(items)}")
    for aid, items in report["warnings"].items():
        print(f"warn     {aid[:32]}..: {'; '.join(items)}")
    print(f"lint: {len(runs)} runs checked, "
          f"{len(report['critical'])} critical, {len(report['warnings'])} with warnings")
    return 1 if report["critical"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
