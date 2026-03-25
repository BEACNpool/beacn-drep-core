#!/usr/bin/env python3
import json
from datetime import datetime, timezone
from pathlib import Path

CORE = Path(__file__).resolve().parents[2]
POLICY_PATH = CORE / "change-control" / "policy" / "fundamental_change_policy.json"
PUBLIC = CORE / "data" / "output" / "public"
AUDIT_LOG = CORE / "logs" / "audit_log.jsonl"
REPORTS = CORE / "change-control" / "reports"


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def count_recent_audit_rows(max_rows=1000):
    if not AUDIT_LOG.exists():
        return 0
    lines = AUDIT_LOG.read_text(encoding="utf-8").strip().splitlines()
    return min(len(lines), max_rows)


def main():
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    policy = load_json(POLICY_PATH, {})
    drep_summary = load_json(PUBLIC / "drep_summary.json", {})
    audit_status = load_json(PUBLIC / "audit_status.json", {})
    backtest_summary = load_json(PUBLIC / "backtest_summary.json", {})

    consistency = drep_summary.get("consistency", {})
    integrity = audit_status.get("integrity", {})

    abstain_rate = float(consistency.get("abstain_rate", 0) or 0)
    needs_more_info_rate = float(consistency.get("needs_more_info_rate", 0) or 0)

    network_aligned = int(backtest_summary.get("network_aligned", 0) or 0)
    network_diverged = int(backtest_summary.get("network_diverged", 0) or 0)
    denom = network_aligned + network_diverged
    network_divergence_rate = (network_diverged / denom) if denom > 0 else 0.0

    replay_failures_7d = 0
    stale_data_incidents_7d = 0

    rows_seen = count_recent_audit_rows()
    minimum_sample_size = int(policy.get("minimum_sample_size", 20))

    nf = policy.get("non_fundamental_change_triggers", {})
    f = policy.get("fundamental_change_triggers", {})

    reasons_non_fundamental = []
    reasons_fundamental = []

    if stale_data_incidents_7d >= int(nf.get("stale_data_incidents_7d_gte", 9999)):
        reasons_non_fundamental.append("stale_data_incidents_7d threshold met")
    if needs_more_info_rate >= float(nf.get("needs_more_info_rate_gte", 9)):
        reasons_non_fundamental.append("needs_more_info_rate threshold met")
    if abstain_rate >= float(nf.get("abstain_rate_gte", 9)):
        reasons_non_fundamental.append("abstain_rate threshold met")

    if replay_failures_7d >= int(f.get("replay_failures_7d_gte", 9999)):
        reasons_fundamental.append("replay_failures_7d threshold met")
    if bool(integrity.get("hidden_inputs_allowed", False)) == bool(f.get("hidden_inputs_allowed_true", True)):
        reasons_fundamental.append("hidden_inputs_allowed=true integrity breach")
    if bool(integrity.get("undeclared_resources_allowed", False)) == bool(f.get("undeclared_resources_allowed_true", True)):
        reasons_fundamental.append("undeclared_resources_allowed=true integrity breach")
    if bool(integrity.get("manual_override_enabled", False)) == bool(f.get("manual_override_enabled_true", True)):
        reasons_fundamental.append("manual_override_enabled=true integrity breach")
    if bool(integrity.get("private_assistant_context_allowed", False)) == bool(f.get("private_context_allowed_true", True)):
        reasons_fundamental.append("private_assistant_context_allowed=true integrity breach")
    if bool(integrity.get("private_memory_allowed", False)) == bool(f.get("private_memory_allowed_true", True)):
        reasons_fundamental.append("private_memory_allowed=true integrity breach")
    if abstain_rate >= float(f.get("abstain_rate_gte", 9)):
        reasons_fundamental.append("abstain_rate threshold met")
    if needs_more_info_rate >= float(f.get("needs_more_info_rate_gte", 9)):
        reasons_fundamental.append("needs_more_info_rate threshold met")
    if network_divergence_rate >= float(f.get("network_divergence_rate_gte", 9)):
        reasons_fundamental.append("network_divergence_rate threshold met")

    if rows_seen < minimum_sample_size:
        decision = "STAY_COURSE"
        reasons = [f"insufficient sample size ({rows_seen} < {minimum_sample_size})"]
    elif reasons_fundamental:
        decision = "PROPOSE_FUNDAMENTAL_CHANGE"
        reasons = reasons_fundamental
    elif reasons_non_fundamental:
        decision = "TUNE_NON_FUNDAMENTAL"
        reasons = reasons_non_fundamental
    else:
        decision = "STAY_COURSE"
        reasons = ["no policy thresholds met"]

    report = {
        "generated_at": now,
        "decision": decision,
        "reasons": reasons,
        "metrics": {
            "rows_seen": rows_seen,
            "abstain_rate": abstain_rate,
            "needs_more_info_rate": needs_more_info_rate,
            "network_divergence_rate": round(network_divergence_rate, 4),
            "replay_failures_7d": replay_failures_7d,
            "stale_data_incidents_7d": stale_data_incidents_7d
        },
        "integrity": integrity,
        "policy_version": policy.get("version", "unknown"),
        "next_action": {
            "STAY_COURSE": "No change required. Document status.",
            "TUNE_NON_FUNDAMENTAL": "Open a small tuning proposal with receipts. No doctrine rewrite.",
            "PROPOSE_FUNDAMENTAL_CHANGE": "Open public RFC/PR with evidence; do not auto-apply changes."
        }.get(decision)
    }

    REPORTS.mkdir(parents=True, exist_ok=True)
    out = REPORTS / f"weekly-review-{now.replace(':','').replace('-','')}.json"
    out.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"decision": decision, "report": str(out.relative_to(CORE))}))


if __name__ == "__main__":
    main()
