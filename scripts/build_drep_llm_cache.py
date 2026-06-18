#!/usr/bin/env python3
"""Build the BEACN DRep reasoning cache WITHOUT an Anthropic API key.

The engine never calls a live model; it only reads a precomputed cache via
BEACN_DREP_LLM_CACHE (source: precomputed) and stays deterministic + replayable.
This builder is the only thing that talks to a model, and it does so through a CLI
agent you already pay for — Claude Code (`claude -p`) or OpenCLAW/codex (`codex exec`,
ChatGPT OAuth) — so no API key is required.

For each selected action it asks the agent for {claims, lean} grounded in the
proposal's cached anchor document and the matching soul doctrine. Output is merged
into the cache file so a failed/empty agent call keeps the last good entry; the
engine fills any gap with its deterministic offline heuristic.

  claims -> Stage 1 evidence table (request + classified claim rows)
  lean   -> Stage 1.5 bounded score nudge (clamped to ±cap in the engine)

Usage:
  python3 scripts/build_drep_llm_cache.py --backend codex   --status active
  python3 scripts/build_drep_llm_cache.py --backend claude  --status active
  python3 scripts/build_drep_llm_cache.py --backend offline --status active   # no quota, plumbing test
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from beacn_drep import engine as E, llm  # noqa: E402
from beacn_drep.anchors import load_anchor_text  # noqa: E402

CACHE_PATH = E.OUTPUT_DIR / "llm_cache_active.json"
CODEX_BIN = os.environ.get(
    "BEACN_CODEX_BIN",
    str(Path.home() / ".openclaw/npm/node_modules/@openai/codex-linux-x64"
        "/vendor/x86_64-unknown-linux-musl/codex/codex"),
)

# Combined structured-output schema for one action: {claims, lean}.
OUTPUT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "claims": llm.CLAIMS_SCHEMA,
        "lean": llm.LEAN_SCHEMA,
    },
    "required": ["claims", "lean"],
}

SYSTEM = (
    "You are the reasoning layer of an autonomous Cardano DRep that votes REAL treasury money. "
    "A separate deterministic engine enforces every hard safety gate (stale data, missing evidence, "
    "treasury-needs-dossier, hard blockers, high risk flags) and you cannot override them. "
    "Return ONLY a JSON object with keys 'claims' and 'lean'.\n"
    + llm.CLAIM_SYSTEM
    + "\n\nFor 'lean': " + llm._lean_system()
)


def _prompt(action: dict, anchor_text: str, doctrine_text: str, assessment: dict, cap: float) -> str:
    return (
        SYSTEM
        + "\n\n========================================\n"
        + f"Action id: {action.get('action_id')}\n"
        + f"Action type: {action.get('action_type')}\n"
        + f"Title: {action.get('metadata_title') or '(none)'}\n"
        + f"Treasury amount (lovelace, if any): {action.get('treasury_amount_lovelace') or '(none)'}\n"
        + f"Lean score_adjustment MUST be within [-{cap}, {cap}].\n\n"
        + "DOCTRINE (BEACN's published standard for this action type):\n-----8<-----\n"
        + llm._truncate(doctrine_text or "(none on file)", 6000)
        + "\n-----8<-----\n\nDETERMINISTIC ASSESSMENT TREE:\n"
        + llm._assessment_digest(assessment)
        + "\n\nANCHOR DOCUMENT TEXT (verbatim, possibly JSON-LD):\n-----8<-----\n"
        + llm._truncate(anchor_text or "(no cached anchor document)", 24000)
        + "\n-----8<-----\n\n"
        + "Respond with the JSON object {\"claims\": {...}, \"lean\": {...}} only."
    )


def _extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("```", 2)[1]
        if text.startswith("json"):
            text = text[4:]
    start, end = text.find("{"), text.rfind("}")
    if start >= 0 and end > start:
        text = text[start:end + 1]
    return json.loads(text)


def call_codex(prompt: str) -> dict:
    with tempfile.TemporaryDirectory() as td:
        schema_f = Path(td) / "schema.json"
        out_f = Path(td) / "out.json"
        schema_f.write_text(json.dumps(OUTPUT_SCHEMA), encoding="utf-8")
        cmd = [
            CODEX_BIN, "exec", "--skip-git-repo-check", "-s", "read-only",
            "-c", "approval_policy=\"never\"",
            "-m", os.environ.get("BEACN_CODEX_MODEL", "gpt-5.5"),
            "--color", "never",
            "--output-schema", str(schema_f),
            "-o", str(out_f), "-",
        ]
        p = subprocess.run(cmd, input=prompt, capture_output=True, text=True, timeout=300)
        if out_f.exists() and out_f.read_text(encoding="utf-8").strip():
            return _extract_json(out_f.read_text(encoding="utf-8"))
        if p.returncode != 0:
            raise RuntimeError(f"codex exec failed rc={p.returncode}: {p.stderr.strip()[:400]}")
        return _extract_json(p.stdout)


def call_claude(prompt: str) -> dict:
    cmd = ["claude", "-p", "--output-format", "json", prompt]
    p = subprocess.run(cmd, capture_output=True, text=True, timeout=300)
    if p.returncode != 0:
        raise RuntimeError(f"claude -p failed rc={p.returncode}: {p.stderr.strip()[:400]}")
    env = json.loads(p.stdout)
    return _extract_json(env.get("result", p.stdout))


def call_offline(action, anchor_text, doctrine, assessment) -> dict:
    claims = llm._offline_extract_claims(action, anchor_text)
    lean = llm._offline_assess_lean(action, claims, assessment, doctrine.get("text"), doctrine.get("family"))
    return {
        "claims": {"request": claims.get("request"), "claims": claims.get("claims"),
                   "summary": claims.get("summary")},
        "lean": {k: lean.get(k) for k in ("direction", "score_adjustment", "confidence",
                                          "rationale", "doctrine_basis")},
    }


BACKENDS = {"codex": call_codex, "claude": call_claude, "offline": None}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend", choices=list(BACKENDS), default="codex")
    ap.add_argument("--status", default="active", help="action status filter (default: active)")
    ap.add_argument("--limit", type=int, default=0, help="cap number of actions (0 = all)")
    ap.add_argument("--out", default=str(CACHE_PATH))
    args = ap.parse_args()

    cap = float(os.environ.get("BEACN_LLM_SCORE_ADJUST_CAP", "0.05"))
    actions = [a for a in E._load_actions()
               if (a.get("status") or "").lower() == args.status.lower()]
    if args.limit:
        actions = actions[:args.limit]

    out_path = Path(args.out)
    cache = {}
    if out_path.exists():
        try:
            cache = json.loads(out_path.read_text(encoding="utf-8"))
        except Exception:
            cache = {}

    flags = E._load_flags()
    readiness = E._load_decision_support_csv("vote_readiness_matrix.csv")
    financial = E._load_decision_support_csv("financial_sustainability_profiles.csv")
    risk = E._load_decision_support_csv("risk_mitigation_registry.csv")
    deep = E._load_decision_support_csv("deep_research_dossiers.csv")
    tflow, tdoc = E._load_treasury_flow(), E._load_treasury_doctrine()
    anchor_index = E._load_anchor_index()
    freshness = E._check_freshness()

    ok = fail = 0
    for a in actions:
        aid = a["action_id"]
        anchor_ok = anchor_index.get(aid, {}).get("fetch_status") in ("ok", "ok_cached")
        anchor_text, _ = load_anchor_text(aid)
        doctrine = E._load_doctrine_for(a.get("action_type"))
        base_claims = llm._offline_extract_claims(a, anchor_text)
        assessment = E._build_assessment(
            a, freshness, E._check_missing_evidence(a), anchor_ok, readiness.get(aid),
            financial.get(aid), risk.get(aid), deep.get(aid), tflow, tdoc,
            flags.get(aid, []), base_claims)
        try:
            if args.backend == "offline":
                entry = call_offline(a, anchor_text, doctrine, assessment)
            else:
                prompt = _prompt(a, anchor_text, doctrine.get("text"), assessment, cap)
                entry = BACKENDS[args.backend](prompt)
            adj = max(-cap, min(cap, float((entry.get("lean") or {}).get("score_adjustment") or 0.0)))
            entry.setdefault("lean", {})["score_adjustment"] = adj
            cache[aid] = {**cache.get(aid, {}), **entry}
            ok += 1
            print(f"  [{args.backend}] ok  {aid[:24]}..  lean_adj={adj:+.3f} "
                  f"claims={len(entry.get('claims', {}).get('claims', []))}")
        except Exception as e:  # noqa: BLE001 - keep prior good entry, continue
            fail += 1
            print(f"  [{args.backend}] FAIL {aid[:24]}..  {type(e).__name__}: {str(e)[:160]}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(cache, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nwrote {out_path} ({len(cache)} actions; this run ok={ok} fail={fail})")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
