# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal gives a clear liveness reason: lowering `committeeMinSize` from 7 to 5 creates an operational buffer so governance actions do not become ineligible for ratification if one or two Constitutional Committee members leave or their terms expire.

The action requested a protocol parameter change setting `committee_min_size` to 5. The proposal argued that the current Constitutional Committee has 7 members and that the current minimum is also 7, but that specific current-state claim was not independently evidenced in the review. The better-supported claims were that falling below `committeeMinSize` can block ratification of actions needing Constitutional Committee approval, that the change does not directly alter the current or maximum committee size, and that a value of 5 satisfies the stated guardrails.

The review also found that the proposal acknowledged the main tradeoff: with 5 members and a 2/3 threshold, 4 constitutional votes would be needed, and inactivity by one member could allow another member to block threshold. Execution risk was assessed as low, the anchor document was available and replayable, and the strongest YES case cleared the evidence gates. The remaining uncertainty was that evidence was thin in places, with missing independent assurance and mitigation evidence, but there were no decisive blockers or open questions.

Because this is a system-wide protocol parameter change, BEACN applied conservative caution. Even so, the completed review found enough support for a directional YES: the operational-resilience benefit was explicit, the key governance risk was acknowledged, and action-type policy allowed a clean `committeeMinSize` liveness change to proceed despite thinner generic risk fields.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
