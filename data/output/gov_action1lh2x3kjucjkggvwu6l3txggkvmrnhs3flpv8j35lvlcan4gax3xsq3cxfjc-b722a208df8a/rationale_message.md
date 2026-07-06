# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the core request was clear and reviewable: this action initiates the Cardano mainnet hard fork to Protocol Version 11.0, the “van Rossem” hard fork, while staying within the Conway era. The proposal had a pinned, replayable anchor document, and the main upgrade claim cleared the evidence gates.

The action requests a protocol upgrade from version 10.0 to 11.0. The proposer says it would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153; make Plutus built-ins available consistently across Plutus V1, V2, and V3; add UPLC case expressions for Bool, Integer, and Data; tighten or promote several ledger validation checks; and improve Cardano node PPView mismatch reporting. The review found strong support for the basic hard fork scope, the new primitives, the cross-version Plutus availability claim, the absence of new protocol parameters, and the stated readiness condition that at least 85% of active stake pools should be on a capable node version before ratification.

BEACN also noted important limits in the evidence. Some claims were still mainly proposer assertions, including that the new UPLC case expressions will improve script performance and produce cleaner logic, that testing showed no behavioral regressions and full conformance, and that security audits covered Plutus BLS primitives and execution costs. The risk review was thin: execution risk was marked unknown, and the review lacked detailed mitigation evidence or independent assurance beyond the general CIP-0135 disaster recovery path and the possibility of disabling Plutus primitive use through companion cost model settings.

Even with those uncertainties, there were no decisive blockers. BEACN treated this as a high-impact hard fork requiring extra caution, but the action-type policy allows a clean hard-fork initiation to proceed when the core upgrade is well anchored and reviewable. The YES vote reflects support for moving forward, while openly preserving the uncertainty around thin risk documentation and several claims that were not independently evidenced in the review.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
