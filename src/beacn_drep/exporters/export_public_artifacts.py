#!/usr/bin/env python3
"""Build the public JSON artifact bundle for beacn-drep-web consumption."""
import csv
import json
import subprocess
from pathlib import Path
from datetime import datetime, timezone

from ..config import CORE_REPO, SOUL_REPO, RESOURCES_REPO

OUT = CORE_REPO / "data" / "output" / "public"
RUNS = CORE_REPO / "data" / "output"
ACTIONS_CSV = RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_all.csv"


def _git_commit(path: Path) -> str:
    return subprocess.check_output(["git", "-C", str(path), "rev-parse", "HEAD"], text=True).strip()


def _load_actions_map():
    out = {}
    with ACTIONS_CSV.open(newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            out[r["action_id"]] = r
    return out


def _load_rationales_latest():
    by_action = {}
    for d in RUNS.iterdir():
        if not d.is_dir() or d.name == "public":
            continue
        p = d / "rationale.json"
        if not p.exists():
            continue
        j = json.loads(p.read_text())
        aid = j.get("action_id")
        if not aid:
            continue
        mtime_ns = p.stat().st_mtime_ns
        prev = by_action.get(aid)
        if not prev or mtime_ns > prev["mtime_ns"]:
            by_action[aid] = {
                "run_id": d.name,
                "mtime_ns": mtime_ns,
                "rationale": j,
                "md_path": f"/data/output/{d.name}/rationale.md",
            }
    return by_action


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "actions").mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    actions = _load_actions_map()
    rat = _load_rationales_latest()

    soul_commit = _git_commit(SOUL_REPO)
    res_commit = _git_commit(RESOURCES_REPO)
    core_commit = _git_commit(CORE_REPO)

    items = []
    rationale_items = []
    abstentions = 0
    needs_info = 0

    for aid, r in rat.items():
        if str(aid).startswith("ga_"):
            continue
        a = actions.get(aid, {})
        decision = r["rationale"].get("recommendation", "ABSTAIN")
        if decision == "ABSTAIN":
            abstentions += 1
        if decision == "NEEDS_MORE_INFO":
            needs_info += 1
        title = a.get("metadata_title") or a.get("action_id") or aid
        item = {
            "action_id": aid,
            "title": title,
            "type": a.get("action_type", ""),
            "status": a.get("status", ""),
            "decision": decision,
            "detected_at": a.get("first_seen", ""),
            "published_at": a.get("last_updated", ""),
            "detail_path": f"/actions/{aid}",
        }
        items.append(item)

        rd = {
            "action_id": aid,
            "title": title,
            "decision": decision,
            "summary": (r["rationale"].get("inferences") or [""])[0],
            "published_at": a.get("last_updated", ""),
        }
        rationale_items.append(rd)

        action_detail = {
            "action_id": aid,
            "title": title,
            "type": a.get("action_type", ""),
            "status": a.get("status", ""),
            "source": {
                "origin": "governance fetch pipeline",
                "raw_input_hash": f"sha256:{r['rationale'].get('input_hash', '')}",
                "detected_at": a.get("first_seen", ""),
            },
            "decision": {
                "vote": decision,
                "published_at": a.get("last_updated", ""),
                "signed": False,
                "transaction_hash": None,
            },
            "rationale": {
                "summary": (r["rationale"].get("inferences") or [""])[0],
                "markdown_path": r["md_path"],
                "missing_evidence": r["rationale"].get("missing_evidence", []),
            },
            "reproducibility": {
                "soul_repo": "beacn-drep-soul",
                "soul_commit": soul_commit,
                "resources_repo": "beacn-drep-resources",
                "resources_commit": res_commit,
                "core_commit": core_commit,
                "resource_ids_used": r["rationale"].get("resources_used", []),
            },
            "inputs_used": [
                {"resource_id": x, "type": "csv", "path": "registries/resource_registry.csv"}
                for x in r["rationale"].get("resources_used", [])
            ],
            "scoring": {
                "budget_pressure": float(max(0.0, -float(r["rationale"].get("score", 0)))),
                "conflict_risk": 0.0,
                "technical_value": float(max(0.0, float(r["rationale"].get("score", 0)))),
                "governance_alignment": float(r["rationale"].get("confidence", 0)),
            },
            "freshness": r["rationale"].get("freshness", {}),
        }
        (OUT / "actions" / f"{aid}.json").write_text(json.dumps(action_detail, indent=2) + "\n")

        md_source = CORE_REPO / "data" / "output" / r["run_id"] / "rationale.md"
        if md_source.exists():
            (OUT / "actions" / f"{aid}.md").write_text(md_source.read_text())

    items.sort(key=lambda x: x["detected_at"], reverse=True)
    rationale_items.sort(key=lambda x: x["published_at"], reverse=True)

    index = {
        "generated_at": now,
        "soul": {"repo": "beacn-drep-soul", "commit": soul_commit, "path": "README.md"},
        "resources": {"repo": "beacn-drep-resources", "commit": res_commit, "registry_path": "registries/resource_registry.csv"},
        "core": {"repo": "beacn-drep-core", "version": "0.2.0", "commit": core_commit},
        "stats": {
            "actions_seen": len(actions),
            "decisions_published": len(items),
            "votes_cast": len(items),
            "abstentions": abstentions,
            "needs_more_info": needs_info,
        },
        "latest_actions": [
            {
                "action_id": x["action_id"],
                "title": x["title"],
                "type": x["type"],
                "decision": x["decision"],
                "published_at": x["published_at"],
            }
            for x in items[:20]
        ],
    }

    treasury_summary = {
        "generated_at": now,
        "rolling_6m_fees": [],
        "treasury": {"inflows_6m": 0, "outflows_6m": 0},
    }

    drep_summary = {
        "generated_at": now,
        "beacn_history_count": len(items),
        "consistency": {
            "abstain_rate": round((abstentions / len(items)), 4) if items else 0,
            "needs_more_info_rate": round((needs_info / len(items)), 4) if items else 0,
        },
        "top_n_comparison": {"available": False, "reason": "top_drep_votes.csv not populated"},
    }

    audit_status = {
        "generated_at": now,
        "current_versions": {
            "soul_commit": soul_commit,
            "resources_commit": res_commit,
            "core_commit": core_commit,
        },
        "pipeline": {
            "last_scan_at": now,
            "last_decision_at": now,
            "last_publish_at": now,
        },
        "integrity": {
            "hidden_inputs_allowed": False,
            "undeclared_resources_allowed": False,
            "manual_override_enabled": False,
            "private_assistant_context_allowed": False,
            "private_memory_allowed": False,
            "policy_doc": "docs/PUBLIC_CONTEXT_AND_LIMITS.md",
        },
    }

    (OUT / "index.json").write_text(json.dumps(index, indent=2) + "\n")
    (OUT / "actions.json").write_text(json.dumps({"generated_at": now, "items": items}, indent=2) + "\n")
    (OUT / "rationales.json").write_text(json.dumps({"generated_at": now, "items": rationale_items}, indent=2) + "\n")
    (OUT / "treasury_summary.json").write_text(json.dumps(treasury_summary, indent=2) + "\n")
    (OUT / "drep_summary.json").write_text(json.dumps(drep_summary, indent=2) + "\n")
    (OUT / "audit_status.json").write_text(json.dumps(audit_status, indent=2) + "\n")

    print(json.dumps({"actions": len(items), "generated_at": now}))


if __name__ == "__main__":
    main()
