# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the proposal did not include a complete, independently pinned readiness packet for a high-impact hard fork. This is a conservative, evidence-based hold: the review found useful technical detail, but not enough public, replayable evidence on protocol readiness, ecosystem readiness, security review, and risk mitigation to support a directional vote.

The action asked to move Cardano mainnet from protocol version 10.0 to 11.0, the “van Rossem” hard fork, while staying in the Conway era. It would add new Plutus primitives from several CIPs, make built-in functions consistently available across Plutus V1, V2, and V3, support UPLC case expressions, and tighten several ledger validation rules. The proposal’s core claim that this is an intra-era upgrade without changing transaction shape was supported, and the pinned anchor made the action reviewable.

Other important claims were not supported strongly enough for a hard fork vote. The proposal asserted no behavioral regressions, successful testing, security audits, readiness checks, performance benefits, and expanded script capabilities, but the review found these areas were mostly asserted or deferred rather than backed by complete independent evidence. The claims-and-evidence gate was thin, and the risk review was also thin because mitigation evidence and independent assurance were missing.

A directional vote would be unblocked by a complete independently pinned readiness packet, including evidence for version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and a rollback or containment plan. Until those materials are available, abstaining avoids overstating certainty on a permanent protocol upgrade.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
