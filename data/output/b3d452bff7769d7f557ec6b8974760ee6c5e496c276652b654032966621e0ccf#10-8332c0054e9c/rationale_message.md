# Withdraw 540,750 ada for UTxO RPC by TxPipe: Maintaining Cardano’s Integratio...
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal was missing: `treasury_amount_lovelace`. Even though the proposal describes a 540,750 ada request, the review record’s treasury analysis could not complete the required baseline evidence check for the on-chain treasury amount, so BEACN treated this as a conservative evidence-based hold.

The action requested funding for Year 2 of UTxO RPC by TxPipe: 12 months of part-time maintenance and enhancement, including protobuf specification work, official SDK maintenance, community support, AI-friendly documentation, and Intersect administration. The proposer claimed the budget includes 525,000 ada for maintenance and enhancement plus a 15,750 ada Intersect administration fee, for 540,750 ada total. The proposal also supported several technical and governance claims, including the existence of open-source UTxO RPC repositories, SDKs across multiple languages, Intersect budget-process support, Net Change Limit compliance, and a treasury management framework.

Some claims were still too thin for a directional vote. The review lacked independent evidence for the claim that Amaru, Dingo, and the Haskell Cardano node have adopted UTxO RPC as a query interface, and for the claim about TxPipe’s Catalyst delivery record. The treasury review was also incomplete because it lacked a sustainability path and clear cost-benefit analysis, and the risk review lacked independent assurance and a rollback or remedy path.

This ABSTAIN is not a rejection of UTxO RPC or TxPipe. It is a conservative hold because BEACN could not produce a responsible recommendation without complete baseline evidence for the treasury withdrawal. A directional vote would require the missing `treasury_amount_lovelace` field, stronger independent evidence for the adoption and delivery-record claims, clearer treasury cost-benefit and sustainability analysis, and better assurance around execution risk and remedies.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
