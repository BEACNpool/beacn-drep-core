# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the proposal depends on a key operational claim that was not independently evidenced: that the current Constitutional Committee has 7 members, equal to the current committeeMinSize of 7.

The action asked to reduce the Cardano `committeeMinSize` protocol parameter from 7 to 5. The proposal’s core case is that, with a 7-member committee and a minimum size of 7, a single resignation or term expiration could make governance actions requiring Constitutional Committee approval ineligible for ratification. It argues that lowering the minimum to 5 would create a buffer so governance could continue if one or two members leave, while acknowledging that a 5-member committee with a 2/3 threshold has its own risk: one inactive member could let another member effectively veto governance actions.

Several parts of the proposal were well-supported. The pinned anchor was available and replayable, the requested parameter change was clear, the execution risk was assessed as low, and the proposal stated that `committeeMinSize = 5` fits the listed guardrails. But this is still a system-wide protocol parameter change, and the review found the evidence packet incomplete: missing independent evidence for the current committee size claim, incomplete readiness materials including constitutional alignment, impact analysis, rollback or containment planning, and safety margin, plus missing mitigation evidence and independent assurance.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the goal. A directional vote would need independently replayable evidence confirming the current Constitutional Committee size, plus a complete readiness packet covering constitutional alignment, impact analysis, rollback or containment, safety margin, mitigation evidence, and independent assurance.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
