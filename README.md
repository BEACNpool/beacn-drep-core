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

## Quick run
```bash
PYTHONPATH=src python3 -m beacn_drep.cli run-once
PYTHONPATH=src python3 -m beacn_drep.cli verify-replay --run-id <run_id>
```
