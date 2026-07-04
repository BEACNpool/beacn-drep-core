# Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork)
**BEACN DRep vote: YES**  _(plain-language explanation — precomputed)_

BEACN voted YES because the core request was clear, reviewable, and supported: this action initiates the van Rossem hard fork to move Cardano mainnet from protocol version 10.0 to 11.0 while staying in the Conway era and preserving transaction shape.

The proposal asked to upgrade mainnet to protocol version 11.0, enable new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, make Plutus built-ins consistently available across Plutus V1, V2, and V3, add UPLC case expressions over Bool, Integer, and Data, and tighten several ledger and node validation, diagnostics, and security rules. The pinned anchor document was available and replayable, which allowed the action to clear the basic evidence gates.

Several technical claims were well-supported or independently checkable, including the intra-era hard fork structure, the listed new Plutus primitives, the linked Cardano Node 11.0.1 performance report, the stake pool readiness condition of at least 85% upgraded active stake before ratification, and the stated disaster recovery path through CIP-0135. Other material claims were thinner: the claimed performance and cleanliness benefits of UPLC case expressions, the claimed no-regression testing results, full conformance claims, and security audit claims were treated as proposer assertions unless independently evidenced in the review.

This was still a cautious YES, not a high-confidence endorsement. Hard forks are high-impact upgrades, and the review marked execution risk as unknown, with missing mitigation evidence and independent assurance. BEACN’s policy allows a clean hard-fork initiation to proceed despite thin generic risk fields when the main action and evidence gates clear, while keeping those uncertainties visible for delegators.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
