# Reduce minPoolCost to 75 ada and increase Plutus Memory Limits (Part 2)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the proposal did not provide enough independently pinned protocol-readiness evidence for a system-wide parameter change.

The action requested lowering minPoolCost from 170 ada to 75 ada, and raising Plutus transaction and block memory limits as Part 2 of a two-step increase. The proposer argued that fixed pool costs now penalize small pools more heavily, that lowering the floor should improve small-pool competitiveness, that treasury impact would be marginal, and that the Plutus memory targets had committee support, Preview testnet exercise, and cited performance headroom.

The review found some claims well-supported: the anchor was pinned and replayable, the bundled parameter changes were clearly stated, and the proposal included meaningful rationale, committee process, testnet, and performance references. But key claims remained thin or asserted rather than demonstrated, especially the expected small-pool competitiveness effect and the treasury-stability claim. The risk review also stayed thin: execution risk was unknown, with missing mitigation evidence and missing independent assurance.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the goals. A directional vote would need a complete independently pinned readiness packet, including constitutional alignment, impact analysis, rollback or containment planning, and clear safety-margin evidence, plus independent support for the small-pool and treasury-impact claims.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
