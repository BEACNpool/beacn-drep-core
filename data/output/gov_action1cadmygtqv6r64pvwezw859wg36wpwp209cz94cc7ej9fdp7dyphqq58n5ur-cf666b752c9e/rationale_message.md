# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the proposal did not meet BEACN’s evidence threshold for a directional vote. The main gap was that a material claim, that the current Constitutional Committee has 7 members and is therefore exactly at the current minimum of 7, was not independently supported in the review packet.

The action requested a protocol parameter change to reduce `committeeMinSize` from 7 to 5. The proposer argued this would improve operational resilience by allowing governance to continue if one or two Constitutional Committee members retire or their terms expire, while still maintaining constitutional safeguards. The proposal also explained that if committee membership falls below `committeeMinSize`, governance actions requiring Constitutional Committee approval can become ineligible for ratification, including parameter changes, constitution updates, treasury withdrawals, and hard forks.

Several parts of the proposal were well-supported in the review: the requested parameter change was clear, the anchor document was pinned and replayable, execution risk was assessed as low, the guardrail discussion was present, and the proposal discussed the 2/3 threshold effects at a committee size of 5. It also cited prior review through the Parameter Committee process. However, the review found the evidence status thin overall, with missing independent assurance, missing mitigation evidence, and an incomplete independently pinned readiness packet covering constitutional alignment, impact analysis, rollback or containment, and safety margin.

This abstention is a conservative, evidence-based hold, not a rejection of the operational-resilience argument. A directional vote would be unblocked by independently replayable evidence confirming the current committee size and minimum-size condition, plus a complete readiness packet covering constitutional alignment, impact analysis, mitigation or containment, and safety-margin analysis.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
