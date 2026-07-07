# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal gave a clear, reviewable reason for lowering `committeeMinSize` from 7 to 5: it creates an operational buffer so Cardano governance can keep functioning if one or two Constitutional Committee members retire or their terms expire.

The action requested a protocol parameter change setting `committee_min_size` to 5. The proposal said the current Constitutional Committee has 7 members, equal to the current minimum of 7, and explained that if membership drops below the minimum, governance actions requiring Constitutional Committee approval become ineligible for ratification. That would affect Parameter Changes, Constitution Updates, Treasury Withdrawals, and Hard Forks. The proposal also stated that this change does not directly change the current or maximum committee size.

The strongest supported claims were that the proposal changes only the minimum committee size, that reducing it to 5 creates a liveness buffer, that the voting-threshold effects were analyzed, and that the change is reversible if at least 7 committee members exist at the time of reversion. The review also noted explicit uncertainty: independent evidence was missing for the claim that the current committee has exactly 7 members, and the risk review lacked mitigation evidence and independent assurance.

BEACN still voted YES because the proposal had a pinned, replayable anchor document, low execution risk, no decisive blockers, and enough governance-specific detail to clear the evidence gates for this parameter change. The vote is positive but not strongly confident: the review recognized that a smaller committee can make vetoes easier and that some supporting evidence remains thin.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
