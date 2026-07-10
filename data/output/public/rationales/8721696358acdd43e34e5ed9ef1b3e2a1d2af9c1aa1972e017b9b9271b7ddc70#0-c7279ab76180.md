# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal, especially the missing `treasury_amount_lovelace` field. This is a conservative, evidence-based hold, not a judgment that the proposal is good or bad.

The proposal requested a 12-month deployment of 9,000,000 ADA into Strike Finance V2 liquidity infrastructure. It said the ADA would be sold for USDM, used as stablecoin-denominated liquidity, and returned to the Treasury with realized yield, with a month-6 yield return and a full month-12 wind-down. The proposal also described monthly transparency reporting, independent assurance reports, and oversight by an independent multisig council, but the exact receiving address and exact calendar dates were not stated in the document.

Several core proposal claims were supported inside the proposal itself, including the 9,000,000 ADA request, the USDM conversion model, the 10% modeled annual return with no guarantee, the V2 launch and activity figures through 2026-06-15, the independent multisig structure, the identified risks, and the 12-month growth targets. But important claims still lacked independent evidence, including Strike’s cumulative traction figures and the liquidity provider vault figures for TVL, APR, return, drawdown, and Sharpe ratio. The review also found the claims-and-evidence section thin, treasury analysis incomplete, risk review missing independent assurance and a dependency map, and synthesis blocked.

The evidence needed to unblock a directional vote is a complete treasury withdrawal baseline, including `treasury_amount_lovelace`, plus independently replayable support for the material traction and vault-performance claims, milestone-gated disbursement detail, independent assurance, and a dependency map. Without that baseline, BEACN could not responsibly vote yes or no on a treasury action that would use shared ADA and set precedent.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity and returned with realized yield.
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta; exact receiving address not stated in document.
- finding: Stated amount: 9,000,000 ADA
- finding: Deliverables: Deploy treasury-owned capital as USDM liquidity for Strike Finance V2 for 12 months., Return realized yield from the first six months to the Cardano Treasury at month 6., Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12, minus any realized losses in a wind-down., Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks., Provide independent third-party assurance reports at deployment confirmation, month 6, and month 12.
- finding: Deadline/expiry: 12 months after deployment, with month-6 yield distribution; exact calendar dates not stated in document.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA would be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual return, equal to approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, while stating returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports cumulative traction including over 1.13 billion USD in volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, medium materiality): Strike states that V2 launched on 2026-03-20 and produced 87,288,044 USD total V2 volume, 410,800 V2 trades, 2,681 V2 users, and 30,105 USD V2 revenue through 2026-06-15.
- finding: Claim (economic, proposer_asserted, high materiality): The document claims the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 all-time Sharpe ratio after two months of history.
- missing: Independent evidence for: Strike reports cumulative traction including over 1.13 billion USD in volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- missing: Independent evidence for: The document claims the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 all-time Sharpe ratio after two months of history.
- missing: Independent evidence for: The document says Christian Schmitz is conducting an official audit expected to be finalized by July 1, 2026, and that the report will be published upon completion.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment into Strike Finance V2 rather than grant funding." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Strike reports cumulative traction including over 1.13 billion USD in volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month treasury-owned liquidity deployment into Strike Finance V2 rather than grant funding." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Strike reports cumulative traction including over 1.13 billion USD in volume, about 968,000 to 1,001,000 trades, over 3,000 unique traders, over 1.16 million USD protocol revenue, and over 3.25 million USD liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The document claims the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 all-time Sharpe ratio after two months of history.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `c7279ab7618034893a4f557474bf68fc5fa2cf5ece19d5f0f34d610a361a4dc9`
- snapshot_bundle_hash: `54376b57da8a4127e52a5ff465c537db6accb24ea52d90c4eba992c284504501`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

