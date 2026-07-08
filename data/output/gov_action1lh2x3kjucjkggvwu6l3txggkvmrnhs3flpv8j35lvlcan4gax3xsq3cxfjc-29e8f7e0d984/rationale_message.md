# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal had a pinned, replayable anchor and substantiated the core hard-fork request: upgrading Cardano mainnet from protocol version 10.0 to 11.0 without leaving the Conway era.

The action requested an intra-era hard fork to Protocol Version 11.0, the “van Rossem” hard fork. Its stated deliverables include enabling new Plutus primitives from several CIPs, making Plutus built-in functions consistently available across Plutus V1, V2, and V3, adding UPLC case expressions for Bool, Integer, and Data, and revising several ledger and node validation, diagnostics, and security rules. The proposer also stated that at least 85% of active stake should be on a compatible node version before ratification.

The review found several important claims well-supported or independently checkable, including the protocol version upgrade itself, the cited CIP-based Plutus primitives, consistent availability of Plutus built-ins across Plutus versions, the node performance report, the 85% stake-pool readiness condition, and the permanence of the hard fork with disaster recovery handled through CIP-0135. Other claims remained thinner: the performance and simplification benefits of UPLC case expressions, the full testing-regression claims, and the security-audit claims were treated as proposer assertions rather than fully independently evidenced in the review.

Because this is a high-impact hard fork, BEACN applied extra caution. The risk review was thin, with missing mitigation evidence and missing independent assurance, and readiness depended on a condition to be checked before ratification. Even so, there were no decisive blockers. Under BEACN’s policy, a clean hard-fork initiation can proceed despite incomplete generic risk fields when the core request and evidence gates are satisfied, so the final vote was YES with explicit residual uncertainty.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
