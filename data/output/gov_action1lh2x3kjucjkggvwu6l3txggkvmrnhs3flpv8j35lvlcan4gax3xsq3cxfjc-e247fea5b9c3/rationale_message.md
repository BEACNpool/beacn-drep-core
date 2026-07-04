# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the core hard-fork request was clear, reviewable, and supported: this action upgrades Cardano mainnet from protocol version 10.0 to 11.0 while staying in the Conway era, with the proposal anchor available for audit.

The action requests the “van Rossem” intra-era hard fork to protocol version 11.0. The proposal says this would add new Plutus primitives from several CIPs, make Plutus built-in functions consistently available across Plutus V1, V2, and V3, add UPLC case expressions for Bool, Integer, and Data, and tighten several ledger validation rules, including VRF key hash uniqueness, reference input handling, Constitutional Committee voting restrictions, withdrawal validation, and PPView mismatch diagnostics.

The strongest supported claims were the basic protocol upgrade itself, the availability of new Plutus functionality, the broader availability of built-in functions across Plutus versions, and the listed ledger rule changes. Some claims were thinner: the claimed performance and cleaner-logic benefits of new UPLC case expressions, the governance endorsements by Intersect groups, and parts of the testing, mitigation, and assurance picture were treated as proposer-asserted or not independently evidenced in the supplied review.

The review passed the core intake and evidence gates: the action type was known, the anchor was pinned and replayable, and the strongest YES case cleared the evidence threshold. The risk review remained thin, with execution risk marked unknown and missing mitigation and independent assurance evidence. BEACN still voted YES because the action-type policy allows a clean hard-fork initiation to proceed despite thin generic risk fields, while keeping that uncertainty explicit.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
