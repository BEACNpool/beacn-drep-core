# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal gives Cardano governance an operational buffer: lowering `committeeMinSize` from 7 to 5 would help avoid governance actions becoming ineligible for ratification if one or two Constitutional Committee members leave or expire.

The action requested a protocol parameter change, setting `protocol_param_update.committee_min_size` to 5. The proposal clearly supported the core claim that it changes the minimum Constitutional Committee size from 7 to 5, and it explained the liveness risk: if committee membership falls below the required minimum, actions needing Constitutional Committee approval, including parameter changes, constitution updates, treasury withdrawals, and hard forks, cannot be ratified. It also supported that this change does not directly alter the current or maximum committee size.

The review did flag uncertainty. The claim that the current committee has 7 members, exactly matching the current minimum, was proposer-asserted but lacked independent evidence in the review. The same was true for the claim that the Intersect-facilitated election process is intended to keep a 7-seat committee rather than lower the number of seats. Risk evidence was also thin, with missing mitigation evidence and independent assurance.

Even with those limits, the review found no decisive blockers. Execution risk was rated low, the proposal anchor was available and replayable, and the proposal addressed the main governance tradeoff directly: a 5-member minimum improves continuity, but a smaller active committee can make individual inactivity or opposition more consequential. On balance, BEACN treated this as a clean liveness parameter change with explicit risks and voted YES.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
