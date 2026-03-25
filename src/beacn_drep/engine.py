import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from .config import SOUL_REPO, RESOURCES_REPO, OUTPUT_DIR, AUDIT_LOG
from .routing import select_resources
from .adapters.git_adapter import commit_hash


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_registry() -> list[dict]:
    path = RESOURCES_REPO / "registries" / "resource_registry.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def _load_actions() -> list[dict]:
    path = RESOURCES_REPO / "data" / "input" / "governance" / "governance_actions_sample.csv"
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def run_once(action_id: str | None = None) -> dict:
    actions = _load_actions()
    action = next((a for a in actions if a["action_id"] == action_id), actions[0])

    raw_bytes = json.dumps(action, sort_keys=True).encode("utf-8")
    input_hash = _sha256_bytes(raw_bytes)
    action_type = action["action_type"]

    soul_commit = commit_hash(SOUL_REPO)
    resources_commit = commit_hash(RESOURCES_REPO)

    registry = _load_registry()
    resources = select_resources(registry, action_type)
    resources_used = [r["resource_id"] for r in resources]

    recommendation = "ABSTAIN"
    rationale = {
        "action_id": action["action_id"],
        "action_type": action_type,
        "recommendation": recommendation,
        "facts": ["Starter scaffold: deterministic pipeline in place."],
        "inferences": ["No full scoring implementation yet; conservative default applied."],
        "uncertainty": ["Scoring logic and expanded datasets pending."],
        "input_hash": input_hash,
        "soul_commit": soul_commit,
        "resource_registry_commit": resources_commit,
        "resources_used": resources_used,
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    run_id = f"{action['action_id']}-{input_hash[:12]}"
    out_dir = OUTPUT_DIR / run_id
    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "rationale.json").write_text(json.dumps(rationale, indent=2) + "\n", encoding="utf-8")
    (out_dir / "rationale.md").write_text(
        "\n".join([
            f"# Rationale: {action['action_id']}",
            f"Recommendation: **{recommendation}**",
            "",
            "## Facts",
            "- Starter scaffold: deterministic pipeline in place.",
            "",
            "## Inferences",
            "- No full scoring implementation yet; conservative default applied.",
            "",
            "## Uncertainty",
            "- Scoring logic and expanded datasets pending.",
            "",
            "## Reproducibility",
            f"- input_hash: `{input_hash}`",
            f"- soul_commit: `{soul_commit}`",
            f"- resource_registry_commit: `{resources_commit}`",
            f"- resources_used: `{', '.join(resources_used)}`",
        ]) + "\n",
        encoding="utf-8",
    )

    log_row = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "run_id": run_id,
        "action_id": action["action_id"],
        "input_hash": input_hash,
        "soul_commit": soul_commit,
        "resource_registry_commit": resources_commit,
    }
    AUDIT_LOG.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(log_row) + "\n")

    return {"run_id": run_id, "output_dir": str(out_dir)}
