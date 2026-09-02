# Reduce minPoolCost to 75 ada and increase Plutus Memory Limits (Part 2)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the proposal did not include enough independently pinned protocol readiness evidence for a system-wide parameter change.

The action asked to lower minPoolCost from 170 ada to 75 ada and raise Plutus memory limits, moving maxTxExecutionUnits[memory] from 16,500,000 to 17,500,000 and maxBlockExecutionUnits[memory] from 72,000,000 to 77,500,000. The proposal gave concrete parameter values and some checkable references, including Preview testnet exercise and IOE performance evaluations. The strongest supported case was that the minPoolCost change itself was clearly specified and evidence-gated.

The hold came from what was still thin. The proposal bundled two otherwise unrelated changes, but the review found missing independent evidence for that bundling rationale and for the economic penalty projections. More importantly, the risk review left execution risk unknown and lacked mitigation evidence and independent assurance.

This is a conservative, evidence-based abstention. A directional vote would need a complete independently pinned readiness packet: constitutional alignment, completed impact analysis, rollback or containment plan, clear safety margin, plus independent support for the major economic and bundling claims.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
