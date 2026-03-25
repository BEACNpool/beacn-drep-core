# Architecture

## Layer separation
- `beacn-drep-soul`: doctrine only.
- `beacn-drep-resources`: approved inputs only.
- `beacn-drep-core`: execution only.

Core must never embed doctrine or datasets.

## Mandatory decision pipeline
1. Detect new governance action
2. Hash raw input
3. Classify action type
4. Load soul repo
5. Load resource registry
6. Select relevant resources for action type
7. Pull only approved data
8. Generate rationale (`.md` + `.json`)
9. Persist input hash + resource references
10. Publish to GitHub
11. Optional vote-sign stub
12. Append audit log

## Reproducibility envelope
Each decision artifact must contain:
- `input_hash`
- `soul_commit`
- `resource_registry_commit`
- `resources_used`
- deterministic timestamp used for run id derivation

Re-run is valid only when the same commits and inputs are available.
