# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because this is a high-impact hard fork and the review did not find a complete, independently pinned readiness packet for Protocol Version 11. This is a conservative, evidence-based hold, not a rejection of the upgrade itself.

The action asks Cardano mainnet to move from protocol version 10.0 to 11.0, the “van Rossem” hard fork, while staying in the Conway era and requesting no treasury funds. The proposal says the upgrade would add new Plutus primitives from several CIPs, make Plutus built-ins available consistently across Plutus V1, V2, and V3, add UPLC case expressions for Bool, Integer, and Data, and tighten several ledger and node validation, diagnostic, and security rules. The review found the anchor document available and replayable, and it treated the basic version upgrade claim as substantiated.

The main gap was readiness evidence. The proposal itself says at least 85% of stake pools by active stake should be upgraded before ratification, but that status still needed to be determined. Several important claims were also still proposer-asserted or thinly evidenced, including the impact of making all Plutus built-ins available across versions, the performance and simplification benefits of new UPLC case expressions, security review details, compatibility readiness, mitigation evidence, and independent assurance. Execution risk was therefore marked unknown.

A directional vote would be unblocked by a complete independently pinned readiness packet covering version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning. Until those items are tied to replayable public evidence, ABSTAIN is the more honest vote: it avoids overstating certainty on a major protocol change while recognizing that the proposal does present a coherent case for the upgrade.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
