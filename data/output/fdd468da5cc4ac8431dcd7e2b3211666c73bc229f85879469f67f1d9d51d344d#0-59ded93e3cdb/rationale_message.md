# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because this is a high-impact hard fork, and the review did not find a complete independently pinned readiness packet for protocol readiness, ecosystem readiness, security review, testing, and rollback or containment planning.

The action requested an intra-era hard fork of Cardano mainnet from protocol version 10.0 to 11.0, called the van Rossem hard fork, while staying in the Conway era. The proposal says this would add new Plutus primitives from several CIPs, make Plutus built-in functions consistently available across Plutus V1, V2, and V3, add UPLC case expressions for Bool, Integer, and Data, and tighten ledger and node rules such as VRF key hash uniqueness and PPView mismatch reporting.

Several core claims were reviewable or supported: the protocol version change itself, the linked CIPs for new Plutus primitives, the availability of built-ins across Plutus versions, the VRF uniqueness rule, the 85% active-stake SPO upgrade expectation before ratification, and the linked Cardano Node 11.0.1 performance report. But important readiness claims were still mostly proposer-asserted or thinly evidenced, including no behavioral regressions, full specification-to-implementation conformance, correct operation across Plutus versions, security audits for BLS primitives and execution costs, and performance benefits from UPLC case expressions.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of the upgrade’s goals. A directional vote would be unblocked by a complete independently pinned readiness packet covering version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning, plus stronger mitigation evidence and independent assurance for the execution risks.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
