# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4933` (raw `-0.4933` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal contains substantial operational detail and acknowledges major risks, but the ask is large, yield is modeled rather than guaranteed, the audit report is not included, references are empty, and the treasury would take stablecoin, custody, smart contract, drawdown, and ADA opportunity-cost exposure. The mechanical assessment can score the structured terms, but BEACN's doctrine supports a small cautionary nudge where treasury stewardship and independently reproducible evidence remain weaker than the claimed upside.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large treasury withdrawal and the applicable Net Change Limit has not been pinned and independently verified from public chain evidence. That blocks a directional vote under BEACN’s treasury rules, even though the proposal contains meaningful operational detail.

The action asks for 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity, not a grant. The proposal says the ADA would be sold into USDM, used as stablecoin liquidity, with realized yield returned at month 6 and principal plus remaining realized yield returned at month 12, minus any realized losses. It also promises monthly transparency reports and third-party assurance reports. The proposal models a 10% USD-denominated annual return, but clearly states returns are not guaranteed.

Several basic claims were supported in the proposal itself: the amount, the 12-month structure, the USDM deployment model, Strike’s reported historical usage figures, the independent multisig custody structure, and the stated risks. But important claims were not independently supported by replayable public evidence, especially the claim that liquidity is Strike’s main growth bottleneck and that added stablecoin liquidity has driven higher volume, fees, and vault performance. The proposal also says an official audit was expected by July 1, 2026, but the audit report was not included.

This is a conservative, evidence-based hold. A directional vote would require the Net Change Limit to be pinned and independently verified from public chain evidence, stronger independent evidence for the key growth and liquidity claims, the missing audit or assurance evidence, a documented milestone-gated disbursement plan, and clearer risk materials such as independent assurance and a dependency map.

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
- finding: Requested: 12-month productive deployment of treasury capital into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM stablecoin liquidity and returned with realized yield.
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta; exact withdrawal address not stated in document.
- finding: Stated amount: 9000000
- finding: Deliverables: Sell 9,000,000 ADA for USDM in an orderly manner to provide stablecoin-denominated liquidity for Strike Finance V2., Return realized yield from the first six months to the Cardano Treasury at month 6., Return 100% of treasury-owned deployed assets, including remaining principal and realized yield minus any realized losses, at month 12., Provide monthly public transparency reports covering deployment status, utilization, volume, open interest, profit and loss, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks., Provide third-party assurance reports at deployment confirmation, month-6 yield distribution, and month-12 return of funds.
- finding: Deadline/expiry: 12 months, with month-6 yield distribution and month-12 final return
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, with modeled deployment of approximately 1,350,000 USDM at ADA = 0.15 USD.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual percentage rate producing about 135,000 USD or 900,000 ADA-equivalent annual yield, but states returns are not guaranteed.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike claims more than 1.13 billion USD cumulative volume, roughly one million trades, over 3,000 unique traders, more than 1.16 million USD protocol revenue, and over 3.25 million USD liquidity-provider profit.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike V2 data from 2026-03-20 through 2026-06-15 is presented as 87,288,044 USD total volume, 410,800 trades, 2,681 users, 30,105 USD revenue, and 1,246,007 USD peak open interest.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal claims liquidity is the primary bottleneck to Strike's further growth and that increased stablecoin liquidity has coincided with higher volume, fee generation, and vault performance.
- missing: Independent evidence for: The proposal claims liquidity is the primary bottleneck to Strike's further growth and that increased stablecoin liquidity has coincided with higher volume, fee generation, and vault performance.
- missing: Independent evidence for: The proposal states Strike V2 has had unofficial reviews and that an official audit by Christian Schmitz is expected to be finalized by July 1, 2026, but the report is not included in the document.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 9000000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal claims liquidity is the primary bottleneck to Strike's further growth and that increased stablecoin liquidity has coincided with higher volume, fee generation, and vault performance." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal contains substantial operational detail and acknowledges major risks, but the ask is large, yield is modeled rather than guaranteed, the audit report is not included, references are empty, and the treasury would take stablecoin, custody, smart contract, drawdown, and ADA opportunity-cost exposure. The mechanical assessment can score the structured terms, but BEACN's doctrine supports a small cautionary nudge where treasury stewardship and independently reproducible evidence remain weaker than the claimed upside.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- No milestone-gated disbursement documented.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal claims liquidity is the primary bottleneck to Strike's further growth and that increased stablecoin liquidity has coincided with higher volume, fee generation, and vault performance.
- Claims and evidence missing: Independent evidence for: The proposal states Strike V2 has had unofficial reviews and that an official audit by Christian Schmitz is expected to be finalized by July 1, 2026, but the report is not included in the document.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `1b091b80946f67485feefea5fb75a44b5fb54c34efc039817dd93cb3cf83751b`
- snapshot_bundle_hash: `46752526f555fd6f19af8278045ee151aba686e23446e2d388f464482d90b69d`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

