# Decision Intelligence Models (Bounded)

This directory is for model-assisted intelligence features that improve recommendation quality without violating auditability.

Rules:
- No opaque model may directly finalize a vote recommendation.
- Any model outputs used by core must be written to rationale artifacts.
- Inputs must come only from admitted resources.
- Deterministic fallbacks are mandatory.

Current profile: `deterministic-v1` (score-based probability envelope + uncertainty banding).
