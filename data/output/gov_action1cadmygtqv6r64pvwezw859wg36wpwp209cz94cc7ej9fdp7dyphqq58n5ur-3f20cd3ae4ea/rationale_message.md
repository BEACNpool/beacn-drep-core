# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal gives a clear governance-resilience reason for lowering `committeeMinSize` from 7 to 5: it would help keep eligible governance actions moving if one or two Constitutional Committee seats became vacant, while still staying within stated constitutional guardrails.

The action requested a protocol parameter change setting `committee_min_size` to 5. The proposer claimed this would improve operational resilience without changing the current number of Constitutional Committee members or the maximum number of members. The proposal also explained that if committee membership falls below `committeeMinSize`, governance actions needing Constitutional Committee approval can become ineligible for ratification, including parameter changes, constitution updates, treasury withdrawals, and hard forks.

Several important claims were supported in the proposal: the requested reduction from 7 to 5, the liveness risk if membership falls below the minimum, the effect of allowing governance to continue after one or two departures, the statement that the change does not directly reduce committee seats, the 2/3 voting-threshold implications for a 5-member committee, and the guardrail claim that 5 is allowed because it is not below 3 and does not exceed 10. Some claims were weaker: the current committee having exactly 7 members, and Intersect’s intent to continue maintaining a 7-seat committee, were treated as proposer assertions rather than independently evidenced facts.

The review found a pinned, replayable anchor document and low execution risk, and there were no decisive blockers. Because parameter changes carry system-wide risk, BEACN still noted residual uncertainty around thin independent evidence, missing mitigation evidence, and missing independent assurance. Even with those limits, the evidence cleared the review gates for a directional vote, so BEACN voted YES.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
