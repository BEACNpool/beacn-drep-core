# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the review was missing DRep distribution data and did not have a complete independently pinned readiness packet for a high-impact hard fork. This is a conservative, evidence-based hold, not a rejection of the upgrade.

The action requested an intra-era Cardano mainnet hard fork from protocol version 10.0 to 11.0, named the van Rossem hard fork, while staying in the Conway era. The proposal described new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153; broader availability of Plutus built-ins across Plutus V1, V2, and V3; UPLC case expressions for Bool, Integer, and Data; VRF key hash uniqueness and other ledger rule changes; and improved PPView mismatch diagnostics in cardano-node.

Several core technical claims were supported or independently verifiable, including the protocol version upgrade, the linked CIP-based Plutus primitives, the absence of new or deprecated protocol parameters, and the stated recovery path through CIP-0135 disaster recovery. However, important claims still relied on proposer assertions or thin evidence, including the claimed performance and logic benefits of UPLC case expressions, the no-regression testing summary, security audit assurances, and mitigation evidence for execution risk.

The gates that kept BEACN from a directional vote were the missing DRep distribution data, thin claims-and-evidence status, thin risk review, missing mitigation evidence, missing independent assurance, and the lack of a complete readiness packet covering version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning. A YES or NO vote would require those materials to be pinned, replayable, and independently reviewable.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
