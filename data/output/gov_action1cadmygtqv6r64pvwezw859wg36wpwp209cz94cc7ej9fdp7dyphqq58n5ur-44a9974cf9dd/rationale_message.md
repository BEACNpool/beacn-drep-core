# Reduce the committeeMinSize parameter from 7 to 5
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal makes a supported case that lowering `committeeMinSize` from 7 to 5 improves governance continuity while keeping constitutional safeguards in place.

The action requested a protocol parameter change: set `committee_min_size` to 5 on-chain. The proposal says the current setting of 7 creates a liveness risk because, if committee membership falls below that minimum, major governance actions that require Constitutional Committee approval can no longer be ratified, including parameter changes, constitution updates, treasury withdrawals, and hard forks. It argues that a minimum of 5 would let governance continue if one or two members retire or their terms expire, assuming a current 7-member committee.

The strongest supported claims were that the change is aimed at operational resilience, that the halt risk is clearly described, that the 2/3 committee threshold was analyzed, that the CMS-01, CMS-02, and CMS-03 guardrails were addressed, and that a reversion path was described. The review also found a pinned, replayable proposal anchor, low execution risk, and no decisive blockers. DRep ratification support was also treated as a positive context signal.

BEACN still noted uncertainty. Independent evidence was missing for the claim that the current Constitutional Committee has exactly 7 members, and for the claim that the change is not intended to reduce the existing 7 seats. The risk review was also thin on mitigation evidence and independent assurance. Even with those limits, the action cleared the review gates for a directional vote, so BEACN voted YES.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
