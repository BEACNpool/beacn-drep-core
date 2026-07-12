# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the hard fork is a high-impact protocol change and the supplied evidence did not meet BEACN’s threshold for a directional vote. This is a conservative, evidence-based hold, not an objection to the upgrade itself.

The action requested an intra-era hard fork on Cardano mainnet from protocol version 10.0 to 11.0, the “van Rossem” hard fork, while remaining in the Conway era. The proposal says this would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, make Plutus built-ins consistently available across Plutus V1, V2, and V3, support additional UPLC case expressions, and promote or revise several ledger and node checks. The core claim that the action upgrades mainnet to protocol version 11.0 was supported, and the pinned anchor document made the proposal reviewable.

The review also found important gaps. Several material readiness, testing, and audit claims were asserted rather than independently evidenced in the supplied material, including the claim that transaction shape is unchanged and ecosystem upgrade effort is minimized, and the claim that testing showed no behavioral regressions and complete conformance for new rules and Plutus behavior. The risk review was also thin: execution risk was marked unknown, mitigation evidence and independent assurance were missing, and the readiness packet was incomplete across areas such as testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning.

A directional vote would be unblocked by a complete independently pinned readiness packet, including clear evidence for implementation readiness, migration readiness, testing results, security review, constitutional alignment, and concrete mitigation or containment plans. Until those claims are tied to replayable public evidence, abstaining avoids overstating certainty on a permanent, operator-sensitive protocol upgrade.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
