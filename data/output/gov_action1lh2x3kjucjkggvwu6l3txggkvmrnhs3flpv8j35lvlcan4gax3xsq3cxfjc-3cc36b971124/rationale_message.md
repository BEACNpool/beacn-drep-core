# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES on the Protocol Version 11 “van Rossem” hard fork because the core upgrade claim was supported: the action moves Cardano mainnet from protocol version 10.0 to 11.0, stays within the Conway era, and does not change transaction shape.

The action requested an intra-era hard fork to make new Plutus primitives available from CIP-0109, CIP-0132, CIP-0133, CIP-0138, CIP-0153; make Plutus built-ins consistently available across Plutus V1, V2, and V3; add UPLC case expressions for Bool, Integer, and Data; and tighten several ledger and node validation rules. The proposal also stated that at least 85% of active stake should be running a node version capable of protocol version 11 before ratification, and DRep ratification support was treated as a positive context signal.

The strongest supported claims were the basic protocol upgrade, the availability of new Plutus primitives, the cross-version availability of Plutus built-ins, and the promotion or tightening of validation rules such as VRF key hash uniqueness and Constitutional Committee voting restrictions. Some claims were weaker: expected performance and cleaner script logic from native UPLC case expressions lacked independent evidence, and the stated testing and audit results were treated as proposer assertions rather than fully independently verified evidence.

The review gates were good enough for a YES, but not without caution. The pinned anchor document was available and replayable, and the proposal cleared the evidence gates for the main hard-fork case. However, the risk review was thin, with missing mitigation evidence and independent assurance, and execution risk remained unknown. BEACN therefore supported the action as a clean hard-fork initiation while explicitly recognizing that readiness verification, audit detail, and concrete risk mitigations were less complete than ideal for a high-impact protocol upgrade.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
