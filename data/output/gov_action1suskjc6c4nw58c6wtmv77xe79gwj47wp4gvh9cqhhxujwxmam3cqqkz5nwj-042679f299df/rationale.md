# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NO**
Score: `-0.5633` (raw `-0.5333` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small negative nudge is justified because the ask is large, depends on modeled yield and future return of funds, and many central traction and vault-performance figures are asserted in the document without included references, while the completed audit is not included. The proposal does disclose risks and custody/reporting controls, so the adjustment should remain modest rather than maximal.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal with thin independent evidence for key performance claims and no documented milestone-gated disbursement.

The proposal requested 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure. The ADA would be sold for USDM stablecoin liquidity, with treasury ownership retained, first-six-month realized yield returned at month 6, and remaining principal plus realized yield targeted for return at month 12, subject to realized losses. The proposal also promised monthly transparency reports and third-party assurance reports at deployment, month 6, and month 12.

Several core terms were well-supported in the proposal itself: the amount requested, the 12-month deployment structure, the sale into USDM, the modeled 10% USD-denominated APR, the return schedule, independent multisig custody, and the list of material risks. But important adoption and performance claims were only proposer-asserted, including the cited cumulative volume, trade count, liquidity-provider profit, protocol revenue, recent V2 activity, and vault performance metrics. The completed audit report was also not included; the proposal only said an audit was underway.

The review gates were strong enough to understand the request, but not strong enough to justify a YES under elevated treasury scrutiny. The anchor document was available and replayable, and the best YES case was that this is structured as a productive deployment rather than a grant. Still, treasury withdrawals require a higher evidence bar because they use shared ADA and set precedent. The review found thin claims-and-evidence support, missing milestone-gated disbursement, missing independent assurance, an unknown execution risk picture, and an unsustainable treasury flow signal. On that record, BEACN’s evidence-based vote was NO.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 9.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure by selling deployed ADA for USDM stablecoin liquidity, with treasury ownership retained and return of principal plus realized yield targeted at month 12.
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta as administrator; Strike Finance V2 liquidity infrastructure as deployment venue.
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy 9,000,000 ADA sold for USDM into V2 stablecoin-denominated liquidity, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12 subject to realized losses, Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks, Provide third-party assurance reports at deployment confirmation, month-6 yield distribution, and month-12 return of funds
- finding: Deadline/expiry: 12 months after deployment, with midpoint yield distribution at month 6
- finding: Claim (economic, supported_in_proposal, high materiality): Strike requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says the deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD, producing approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions of a 10% USD-denominated annual percentage rate, the deployment is expected to generate approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal states treasury principal plus realized yield will be returned at month 12, with first-six-month realized yield returned at month 6.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states Strike Finance has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, generated over 3.25 million USD in liquidity-provider profit, and produced over 1.16 million USD in protocol revenue.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states Strike V2 produced 87,288,044 USD total volume, 410,800 trades, 2,681 users, and 30,105 USD revenue from 2026-03-20 through 2026-06-15.
- missing: Independent evidence for: The proposal states Strike Finance has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, generated over 3.25 million USD in liquidity-provider profit, and produced over 1.16 million USD in protocol revenue.
- missing: Independent evidence for: The proposal states Strike V2 produced 87,288,044 USD total volume, 410,800 trades, 2,681 users, and 30,105 USD revenue from 2026-03-20 through 2026-06-15.
- missing: Independent evidence for: The proposal states the Strike liquidity provider vault had 985,271.59 USD TVL, 43.52% APR, 8.85% all-time return, 1.15% maximum drawdown, and 4.97 Sharpe ratio after two months of history.
- missing: Independent evidence for: The proposal states an official audit by Christian Schmitz is underway and expected by July 1, 2026, with the report to be published upon completion, but no completed audit report is included in the anchor document.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9000000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
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
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Strike requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal states Strike Finance has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, generated over 3.25 million USD in liquidity-provider profit, and produced over 1.16 million USD in protocol revenue." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 9000000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Strike requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity infrastructure rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because the ask is large, depends on modeled yield and future return of funds, and many central traction and vault-performance figures are asserted in the document without included references, while the completed audit is not included. The proposal does disclose risks and custody/reporting controls, so the adjustment should remain modest rather than maximal.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal states Strike Finance has processed over 1.13 billion USD in cumulative volume, facilitated roughly one million trades, generated over 3.25 million USD in liquidity-provider profit, and produced over 1.16 million USD in protocol revenue.
- Claims and evidence missing: Independent evidence for: The proposal states Strike V2 produced 87,288,044 USD total volume, 410,800 trades, 2,681 users, and 30,105 USD revenue from 2026-03-20 through 2026-06-15.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `042679f299df8c38f46315394e9cc1af1b8624db5f26884eb73ae147c0e9c908`
- snapshot_bundle_hash: `27c206e837a337b4a87937a3c304b1c2c8c5069c37398c934870920980093da1`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

