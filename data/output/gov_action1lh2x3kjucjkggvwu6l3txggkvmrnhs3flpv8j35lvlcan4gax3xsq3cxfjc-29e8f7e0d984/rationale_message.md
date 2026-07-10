# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the hard fork is high-impact and the review did not find a complete independently pinned readiness and risk package. This is a conservative, evidence-based hold, not a rejection of the upgrade.

The action requested an intra-era Cardano mainnet hard fork from protocol version 10.0 to 11.0, the “van Rossem” hard fork. The proposal says it would add new Plutus primitives from several CIPs, make Plutus built-ins consistently available across Plutus V1, V2, and V3, add UPLC case expressions, and tighten ledger and node validation rules such as VRF key hash uniqueness and Constitutional Committee voting restrictions. Several core claims were supported or independently checkable, including the protocol version upgrade, the cited Plutus primitives, the VRF rule change, the performance report reference, and the statement that reversal would require the CIP-0135 disaster recovery process except for possible containment through companion cost model settings.

The hold came from what was still thin or unsupported. Some important safety and benefit claims remained proposer-asserted, including the claim that testing showed no behavioral regressions, full specification-to-implementation conformance, and correct operation of new Plutus features across versions. The review also lacked independent evidence that native UPLC case expressions would improve performance and produce cleaner script logic. Most importantly for a hard fork, the assessment did not have a complete readiness packet covering version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning.

The proposal had a pinned anchor and passed enough evidence review to show a serious case for YES, especially on the basic protocol upgrade claim. But the risk review was marked thin, with missing mitigation evidence and independent assurance. BEACN would need those readiness, testing, security, and containment materials tied to replayable public evidence before moving from ABSTAIN to a directional YES or NO.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
