#!/usr/bin/env python3
"""Build a deterministic treasury opportunity-cost portfolio.

Eligible proposals are ranked by verified public benefit, delivery confidence,
cost efficiency, and downside protection. Funding capacity is cumulative: a
proposal cannot receive a YES merely because it looks acceptable in isolation.
"""
from __future__ import annotations

import csv
import json
from datetime import datetime, timezone

from beacn_drep import engine as E


def rows(name: str) -> dict[str, dict]:
    return E._load_decision_support_csv(name)


def main() -> int:
    value = rows("ecosystem_value_profiles.csv")
    ready = rows("vote_readiness_matrix.csv")
    financial = rows("financial_sustainability_profiles.csv")
    risk = rows("risk_mitigation_registry.csv")
    deep = rows("deep_research_dossiers.csv")
    policy = E._load_treasury_policy_state()
    flow = E._load_treasury_flow()
    verified_ncl = policy.get("verification_status") == "verified_on_chain"
    ncl = E._to_float(policy.get("ncl_lovelace")) if verified_ncl else 0.0
    spent = E._to_float(flow.get("withdrawals_73e_lovelace"))
    remaining = max(0.0, ncl - spent) if ncl else 0.0

    candidates = []
    for action in E._load_actions():
        if (action.get("status") or "").lower() != "active" or E._action_family(action.get("action_type")) != "treasury":
            continue
        aid = action["action_id"]
        d = E._treasury_dimensions(
            action, value.get(aid), ready.get(aid), financial.get(aid), risk.get(aid),
            E._yn((deep.get(aid) or {}).get("dossier_complete")) is True,
        )
        request = E._to_float(action.get("treasury_amount_lovelace"))
        priority = round(
            (0.45 * d["benefit"]) + (0.25 * d["delivery_confidence"])
            + (0.20 * d["cost_efficiency"]) + (0.10 * (1 - d["downside_risk"])), 4
        )
        candidates.append({
            "action_id": aid,
            "title": action.get("metadata_title"),
            "requested_lovelace": int(request),
            "priority_score": priority,
            "dimensions": d,
            "funding_eligible": "no",
            "portfolio_reason": "pending ranking",
        })

    candidates.sort(key=lambda x: (-x["priority_score"], x["requested_lovelace"], x["action_id"]))
    allocated = 0.0
    for rank, item in enumerate(candidates, 1):
        item["rank"] = rank
        d = item["dimensions"]
        clears = (
            d["evidence_status"] == "independently_verified" and d["benefit"] >= 0.55
            and d["delivery_confidence"] >= 0.55 and d["cost_efficiency"] >= 0.45
            and d["downside_risk"] <= 0.55
        )
        if not verified_ncl:
            item["portfolio_reason"] = "applicable NCL is not verified"
        elif not clears:
            item["portfolio_reason"] = "balanced evidence floors not cleared"
        elif allocated + item["requested_lovelace"] > remaining:
            item["portfolio_reason"] = "insufficient remaining NCL capacity after higher-ranked proposals"
        else:
            item["funding_eligible"] = "yes"
            item["portfolio_reason"] = "within verified capacity after higher-ranked eligible proposals"
            allocated += item["requested_lovelace"]

    out = {
        "schema_version": "treasury-portfolio-v1",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "status": "verified" if verified_ncl else "blocked_ncl_unverified",
        "ncl_lovelace": int(ncl) if ncl else None,
        "withdrawals_window_lovelace": int(spent),
        "remaining_capacity_lovelace": int(remaining) if ncl else None,
        "allocated_candidate_lovelace": int(allocated),
        "candidates": candidates,
    }
    path = E.RESOURCES_REPO / "data" / "input" / "governance" / "treasury_portfolio.json"
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"portfolio: {len(candidates)} active treasury actions; status={out['status']}; eligible={sum(c['funding_eligible']=='yes' for c in candidates)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
