# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the core case for lowering `committeeMinSize` depends on a material fact that was not independently evidenced: that the current Constitutional Committee has 7 members, exactly matching the current minimum of 7.

The action requested a Cardano parameter change to reduce `committeeMinSize` from 7 to 5. The proposer’s stated rationale was that this would create an operational buffer, so governance could continue if one or two Committee members retired or their terms expired. The proposal also stated that the change would not directly alter the current number of Committee members or signal a desire to shrink the Committee.

Several parts of the proposal were well supported: the requested parameter change itself, the explanation that falling below `committeeMinSize` can make certain governance actions ineligible for ratification, the 5-member threshold math, the guardrail range, and the reversion caveat. The review also found a pinned, replayable anchor document and low execution risk. However, the evidence record was still thin for a system-wide protocol parameter change. Independent evidence was missing for the current 7-member Committee claim, mitigation evidence and independent assurance were missing, and the readiness packet was incomplete on constitutional alignment, impact analysis, rollback or containment, and safety margin.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the operational-buffer argument. A directional vote would be unblocked by independently pinned evidence confirming the current Committee size and current `committeeMinSize`, plus a complete readiness packet covering constitutional alignment, impact, rollback or containment, safety margin, mitigation evidence, and independent assurance.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
