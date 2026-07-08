# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the core request was clear, reviewable, and supported: this action initiates the van Rossem hard fork to move Cardano mainnet from protocol version 10.0 to 11.0 while staying in the Conway era.

The proposal requests an intra-era hard fork with no treasury amount. It would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, make Plutus built-ins consistently available across Plutus V1, V2, and V3, add UPLC case expressions for Bool, Integer, and Data, and tighten several ledger and node validation rules. The proposal also says transaction shape is unchanged, ecosystem upgrade effort is minimized, testing found no behavioral regressions, audits were undertaken, and at least 85% of stake pools by active stake should be upgraded before ratification.

BEACN found the anchor document pinned and replayable, and the main protocol-version upgrade claim cleared the evidence gates. Several technical claims were independently verifiable or supported in the proposal, including the move to protocol version 11.0, the listed new Plutus primitives, cross-version availability of built-ins, the linked node performance report, and the stated disaster-recovery limits around reversion. However, some claims remained thinner: the claimed performance and cleanliness benefits of UPLC case expressions lacked independent evidence, the minimized ecosystem upgrade claim was still proposer-asserted, and the 85% stake pool upgrade threshold still needed to be determined before ratification.

The review treated this as a high-impact hard fork requiring elevated scrutiny, and it recorded thin risk evidence, missing mitigation evidence, missing independent assurance, and unknown execution risk. Even with those cautions, there were no decisive blockers or open questions, and BEACN’s hard-fork policy allows a clean hard-fork initiation to proceed despite thin generic risk fields when the core action clears review. Therefore BEACN voted YES, while recognizing that confidence was limited by the remaining readiness and risk uncertainty.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
