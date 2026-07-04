# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal’s core action was clear and reviewable: it initiates an intra-era hard fork from Cardano protocol version 10.0 to 11.0, remains in the Conway era, and does not change transaction shape.

The proposal requests the “van Rossem” hard fork, adding new Plutus primitives tied to CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153; making Plutus built-ins consistently available across V1, V2, and V3; adding UPLC case expressions; tightening several ledger predicates; and improving Cardano node diagnostics for PPView mismatches. The anchor document was available, pinned, and replayable, so the action could be reviewed.

Several technical claims were well-supported or independently checkable, including the protocol version change, the listed Plutus primitive additions, unified built-in availability across Plutus versions, the cited node 11.0.1 performance report, the 85% stake-pool readiness condition before ratification, and the statement that reversal would require disaster recovery because the ledger change is permanent. Other claims were thinner: performance improvements, throughput benefits, full regression-free testing, and security audit claims were asserted but not independently detailed in the supplied review.

The review recognized this as a high-impact hard fork requiring serious scrutiny. Evidence and counterargument gates were sufficient for a YES, and there were no decisive blockers or open questions. However, confidence was limited because execution risk, mitigation evidence, independent assurance, and stake-pool readiness evidence were still thin or outstanding, so this YES reflects support for a clean, reviewable hard-fork initiation while keeping those uncertainties visible.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
