# Withdraw 1,310,960 ada for Hardware Wallet Maintenance 2026
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the review was missing baseline evidence needed to responsibly evaluate a treasury withdrawal. The decisive blocker was that `treasury_amount_lovelace` was missing for a treasury action, which left the intake and synthesis blocked even though the proposal text requested 1,310,960 ada.

The action asked to fund 12 months of Hardware Wallet Maintenance 2026, covering Cardano hardware-wallet support such as Ledger and Trezor compatibility updates, interoperability libraries, `cardano-hw-cli`, developer and integration support, and vendor-required audits. The proposer stated that the total request was 1,310,960 ada, made up of 1,272,777 ada for maintenance and compatibility assurance plus 38,183 ada for Intersect budget administration. The review found that this amount was supported in the proposal, that the proposal anchor was pinned and replayable, and that the proposal had passed the required 67% Intersect Budget Process Hydra Voting threshold.

However, several important claims were not independently supported enough for a directional vote. The review lacked independent evidence that continuous hardware-wallet maintenance is required because of protocol evolution, Ledger and Trezor release cycles, and wallet or dApp integration demand. It also lacked independent evidence that the scope does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets. The treasury analysis was incomplete, with missing sustainability path and cost-benefit clarity, and the risk review was unknown, missing independent assurance and a rollback or remedy path.

This ABSTAIN is a conservative, evidence-based hold, not a rejection of hardware-wallet maintenance. A directional vote would be unblocked by a complete treasury amount field for the withdrawal, independent public evidence for the key technical and scope claims, clearer cost-benefit and sustainability analysis, and a stronger risk review including independent assurance and a remedy path.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
