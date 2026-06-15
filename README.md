# beacn-drep-core

Execution layer for the BEACN DRep system.

Contains logic only:
- governance action detection (stub)
- deterministic decision pipeline
- rationale generation (`.md` + `.json`)
- reproducibility manifest (`input_manifest.json`)
- replay verification (`verify-replay`)
- rationale publish adapter (stub)
- **signing adapter — IMPLEMENTED, shadow-default** (`src/beacn_drep/adapters/cardano_cli_adapter.py`)

Doctrine and data are loaded from sibling repos:
- `../beacn-drep-soul`
- `../beacn-drep-resources`

Decision-boundary rule:
- Core decision logic may only use doctrine + admitted resources.
- OpenClaw private memory/context is not an allowed decision input.
- Public contract: `../beacn-drep-web/docs/PUBLIC_CONTEXT_AND_LIMITS.md`.
Public operating model: `../beacn-drep-web/docs/OPERATING_MODEL.md`.

## Quick run
```bash
PYTHONPATH=src python3 -m beacn_drep.cli run-once
PYTHONPATH=src python3 -m beacn_drep.cli verify-replay --run-id <run_id>
```

## Signing (shadow-default)
The signing adapter turns a decision run into a guarded, signed Conway vote.
It is SHADOW by default — it builds + signs but submits nothing unless
`--live` is passed AND `BEACN_VOTING_LIVE=1` is set. It enforces the full
8-point automation gate from `../infra/drep-cli-wallet.md` and fails closed.
Keys live on opsbox (`~/.secrets/cardano/beacn-drep-cli/`, see
`../ops/beacn-drep-wallet`); queries + build + submit go through `relay`; the
block producer is never in the voting path.
```bash
# shadow over recent runs (nothing submitted):
PYTHONPATH=src python3 scripts/sign_votes_shadow.py
PYTHONPATH=src python3 scripts/sign_votes_shadow.py --run-dir data/output/<run>
```
Not yet live-ready: the rationale must be published and its URL + blake2b-256
hash recorded into each run (`rationale_anchor_url`/`rationale_anchor_hash`),
and the admitted governance dataset refreshed. Until then the gate blocks at
`rationale_anchor` / `freshness`, which is correct.

## Scoring transparency
- Canonical weights are loaded from `../beacn-drep-soul/scoring_weights.json`.
- Core fails closed if that file is missing/invalid.
- Weight changes are doctrine changes and must be changeloged in soul.

## Conservative evidence gate
- Missing baseline evidence (including missing anchor URL/hash) now forces `ABSTAIN` with reason code `MISSING_BASELINE_EVIDENCE`.
