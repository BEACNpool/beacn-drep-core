# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because this is a high-impact hard fork and the supplied evidence did not meet BEACN’s threshold for a directional vote. The hold is conservative: the proposal describes meaningful technical upgrades, but the review found the readiness and risk evidence too thin to justify a YES or NO.

The action requested an intra-era Cardano mainnet hard fork from protocol version 10.0 to 11.0, the “van Rossem” hard fork, while staying in the Conway era. It would enable new Plutus primitives from the referenced CIPs, make Plutus built-ins available consistently across Plutus V1, V2, and V3, add UPLC case expressions for Bool, Integer, and Data, and tighten several ledger and node validation behaviors. The proposal’s core upgrade claim was supported, and some technical references, including node performance results and the permanent nature of the ledger-rule change, were independently checkable.

The weaker part was evidence quality around readiness and risk. Several important claims were proposer-asserted rather than independently evidenced in the supplied review, including no behavioral regressions, full specification-to-implementation conformance, correct operation of new primitives and case expressions across Plutus versions, expected performance and logic improvements from native case expressions, and completed security audit work. The review also marked execution risk as unknown, with missing mitigation evidence and independent assurance.

A directional vote would need a complete, independently pinned readiness packet covering version guardrails, testnet results, stake pool readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning. Until that evidence is available and replayable, BEACN’s ABSTAIN reflects an evidence-based hold rather than opposition to the upgrade itself.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
