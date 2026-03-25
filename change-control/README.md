# Change Control (Self-Learning / Self-Correction)

Purpose: ensure any adaptation is auditable, justified, and publicly documented.

## Core Principles
- No silent self-modification.
- No automatic doctrine changes.
- No fundamental logic changes without explicit qualification.
- Every accepted change must be committed and publicly documented.

## Directory Layout
- `baseline/` — initial and periodic baseline snapshots.
- `policy/` — hard-coded qualification thresholds.
- `reports/` — machine-generated weekly review outcomes.
- `scripts/` — review tooling.

## Review Modes
- `STAY_COURSE` — no change required.
- `TUNE_NON_FUNDAMENTAL` — implementation/ops tune, doctrine unchanged.
- `PROPOSE_FUNDAMENTAL_CHANGE` — threshold met; proposal + public review required.

## Rule
The weekly review may propose changes, but it must never apply fundamental changes automatically.
