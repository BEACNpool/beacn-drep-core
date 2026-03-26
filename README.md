# beacn-drep-core

Execution layer for the BEACN DRep system.

Contains logic only:
- governance action detection (stub)
- deterministic decision pipeline
- rationale generation (`.md` + `.json`)
- reproducibility manifest (`input_manifest.json`)
- replay verification (`verify-replay`)
- publish/sign adapters (stubs)

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

## Scoring transparency
- Canonical weights are loaded from `../beacn-drep-soul/scoring_weights.json`.
- Core fails closed if that file is missing/invalid.
- Weight changes are doctrine changes and must be changeloged in soul.

## Conservative evidence gate
- Missing baseline evidence (including missing anchor URL/hash) now forces `ABSTAIN` with reason code `MISSING_BASELINE_EVIDENCE`.
