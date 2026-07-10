# Strike Finance Liquidity Deployment
**BEACN DRep vote: ABSTAIN**  _(plain-language explanation — precomputed)_

BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal, especially the missing `treasury_amount_lovelace` field. This is a conservative, evidence-based hold, not a judgment that the proposal is good or bad.

The proposal requested a 12-month deployment of 9,000,000 ADA into Strike Finance V2 liquidity infrastructure. It said the ADA would be sold for USDM, used as stablecoin-denominated liquidity, and returned to the Treasury with realized yield, with a month-6 yield return and a full month-12 wind-down. The proposal also described monthly transparency reporting, independent assurance reports, and oversight by an independent multisig council, but the exact receiving address and exact calendar dates were not stated in the document.

Several core proposal claims were supported inside the proposal itself, including the 9,000,000 ADA request, the USDM conversion model, the 10% modeled annual return with no guarantee, the V2 launch and activity figures through 2026-06-15, the independent multisig structure, the identified risks, and the 12-month growth targets. But important claims still lacked independent evidence, including Strike’s cumulative traction figures and the liquidity provider vault figures for TVL, APR, return, drawdown, and Sharpe ratio. The review also found the claims-and-evidence section thin, treasury analysis incomplete, risk review missing independent assurance and a dependency map, and synthesis blocked.

The evidence needed to unblock a directional vote is a complete treasury withdrawal baseline, including `treasury_amount_lovelace`, plus independently replayable support for the material traction and vault-performance claims, milestone-gated disbursement detail, independent assurance, and a dependency map. Without that baseline, BEACN could not responsibly vote yes or no on a treasury action that would use shared ADA and set precedent.

---
_The vote, score, and gates are produced deterministically and are the binding record. This explanation is a model-assisted plain-language layer over that record. Full reasoning, provenance, and limitations are documented openly in METHODOLOGY.md; the decision is byte-for-byte replayable via `cli verify-replay`._
