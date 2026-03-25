#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "data" / "output"
OUT_PUBLIC = RUNS / "public"


def load_latest_by_action():
    by_action = {}
    for d in RUNS.iterdir():
        if not d.is_dir() or d.name == "public":
            continue
        p = d / "rationale.json"
        if not p.exists():
            continue
        j = json.loads(p.read_text(encoding="utf-8"))
        aid = j.get("action_id")
        if not aid:
            continue
        mtime = p.stat().st_mtime
        prev = by_action.get(aid)
        if not prev or mtime > prev["mtime"]:
            by_action[aid] = {"run_id": d.name, "rationale": j, "mtime": mtime}
    return by_action


def main():
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    latest = load_latest_by_action()

    items = []
    for aid, obj in sorted(latest.items()):
        if str(aid).startswith("ga_"):
            continue
        r = obj["rationale"]
        items.append({
            "action_id": aid,
            "run_id": obj["run_id"],
            "action_type": r.get("action_type"),
            "vote": r.get("recommendation"),
            "abstain_reason_code": r.get("abstain_reason_code"),
            "score": r.get("score"),
            "confidence": r.get("confidence"),
            "uncertainty_band": r.get("uncertainty_band"),
            "evidence_depth_score": r.get("evidence_depth_score"),
            "decision_probs": r.get("decision_probs", {}),
            "rationale_summary": (r.get("inferences") or [""])[0],
            "missing_evidence": r.get("missing_evidence", []),
        })

    report_json = {
        "generated_at": now,
        "count": len(items),
        "items": items,
    }

    md_lines = [
        f"# Vote Rationale Simulation Report",
        f"",
        f"Generated: `{now}`",
        f"Total actions: `{len(items)}`",
        "",
    ]
    for x in items:
        md_lines.extend([
            f"## {x['action_id']}",
            f"- type: `{x.get('action_type')}`",
            f"- vote: `{x.get('vote')}`",
            f"- abstain_reason_code: `{x.get('abstain_reason_code')}`",
            f"- score/confidence: `{x.get('score')}` / `{x.get('confidence')}`",
            f"- uncertainty_band: `{x.get('uncertainty_band')}`",
            f"- evidence_depth_score: `{x.get('evidence_depth_score')}`",
            f"- decision_probs: `{json.dumps(x.get('decision_probs', {}), sort_keys=True)}`",
            f"- rationale_summary: {x.get('rationale_summary')}",
            f"- missing_evidence_count: `{len(x.get('missing_evidence', []))}`",
            "",
        ])

    OUT_PUBLIC.mkdir(parents=True, exist_ok=True)
    (OUT_PUBLIC / "vote_rationale_report.json").write_text(json.dumps(report_json, indent=2) + "\n", encoding="utf-8")
    (OUT_PUBLIC / "vote_rationale_report.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(json.dumps({"count": len(items), "json": "data/output/public/vote_rationale_report.json", "md": "data/output/public/vote_rationale_report.md"}))


if __name__ == "__main__":
    main()
