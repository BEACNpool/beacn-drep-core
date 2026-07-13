# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because this is a high-impact hard fork and the review did not find a complete, independently pinned readiness packet for mainnet activation.

The action asked to initiate the van Rossem hard fork, upgrading Cardano mainnet from protocol version 10.0 to 11.0 while staying in the Conway era. The proposal says this would add new Plutus primitives, make built-in functions available consistently across Plutus V1, V2, and V3, add UPLC case expressions, and tighten several ledger and node rules. Some core claims were supported or independently verifiable, including the basic protocol-version upgrade, the listed CIPs for new Plutus primitives, the cited node performance report, and the permanent nature of the ledger-rule change.

The hold comes from the evidence gaps around readiness and risk. Several material claims were still proposer-asserted rather than independently evidenced inside the reviewed packet, including the claimed performance benefits of UPLC case expressions, the no-regression testing claims, security audit claims, constitutional guardrail alignment, and broad operational readiness. The risk review was also thin, with missing mitigation evidence and independent assurance.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the upgrade’s goals. A directional vote would need a complete independently pinned readiness packet covering guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
