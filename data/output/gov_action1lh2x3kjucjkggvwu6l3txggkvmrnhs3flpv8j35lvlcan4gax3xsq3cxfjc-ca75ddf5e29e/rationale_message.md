# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the proposal’s core request was clear, anchored, and sufficiently supported: it initiates Cardano mainnet’s move to protocol version 11.0 through an intra-era hard fork while remaining in the Conway era.

The action requests the “van Rossem” hard fork, upgrading mainnet from protocol version 10.0 to 11.0 without an era transition or transaction-shape change. The proposal says the upgrade makes new Plutus primitives available from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, unifies Plutus built-in function availability across Plutus V1, V2, and V3, adds UPLC case expressions for Bool, Integer, and Data, and tightens several ledger and node validation, diagnostics, and security rules.

The review found the anchor document pinned and replayable. The main protocol-version claim was supported, and several technical claims were independently checkable, including the new Plutus primitives, the cited Cardano Node 11.0.1 performance report, and the description of reversion through the CIP-0135 disaster recovery process. However, some important claims remained thinner: the performance and simplification benefits of UPLC case expressions, the testing conclusions about no regressions and conformance, and the security audit conclusions were treated as proposer assertions rather than fully embedded independent evidence.

This is a high-impact hard fork, so BEACN applied extra caution. Risk review remained thin, with execution risk unknown and missing mitigation and independent assurance evidence. Still, there were no decisive blockers, and the action-type policy allows a clean hard-fork initiation to proceed when the core evidence gates clear. BEACN’s YES is therefore a cautious approval of the hard fork initiation, with explicit uncertainty around readiness verification, testing depth, audit evidence, and mitigation detail.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
