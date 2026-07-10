# Scalus 2026: Maintenance, Dijkstra Readiness, Interoperability & Application Runtime
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal was missing: `treasury_amount_lovelace`. Even though the proposal text says it requests ₳2,464,844, the structured treasury review recorded the requested ADA amount as 0 and the intake and synthesis gates were blocked on the missing on-chain treasury amount field.

The action requested 9 months of Scalus funding for maintenance, Dijkstra hard-fork readiness, JVM and JS/TS interoperability, and foundational application runtime components, with delivery planned through March 2027. The proposer described Scalus as an established open-source Cardano development platform, claimed reuse across several Cardano developer tools, and listed prior delivery, milestone-based administration, public reporting, audited SundaeSwap treasury contracts, independent oversight, and third-party assurance.

Some claims were supported inside the proposal, including the ₳2,464,844 budget, the 9-month schedule, the reduced scope compared with the prior ₳8.503M proposal, and the quarterly milestone plan. But several important claims still lacked independent evidence in the review, including Scalus’s three-year open-source delivery record and its reuse across Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution. The treasury review also still lacked a sustainability path, while the risk review lacked independent assurance and a dependency map.

This ABSTAIN is a conservative, evidence-based hold, not a judgment that the work has no value. A directional vote would require the missing `treasury_amount_lovelace` field to be present and reviewable for the treasury withdrawal, plus stronger independent evidence for the key technical and adoption claims and the missing treasury and risk-review materials.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
