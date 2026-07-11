# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4933` (raw `-0.4933` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary nudge is justified because the request exposes treasury assets to market, stablecoin, custody, and smart contract risks while several key traction, market-share, audit, and performance claims are stated without references in the anchor document. The proposal does include concrete terms, reporting commitments, custody separation, and risk triggers, so the adjustment should remain small rather than overriding the deterministic assessment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the idea.

The proposal asks for 9,000,000 ADA for a 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, rather than a grant. It says the ADA would be sold for USDM, modeled at ADA = 0.15 USD, creating about 1,350,000 USDM of stablecoin liquidity. It also models a 10% USD-denominated annual return, or about 135,000 USD / 900,000 ADA-equivalent in yield, while stating that returns are not guaranteed. The proposal commits to month-6 yield return, month-12 return of treasury-owned assets and remaining yield minus realized wind-down losses, monthly public reporting, and third-party assurance reports at deployment, month 6, and month 12.

Several core terms were supported in the proposal: the amount, the 12-month deployment structure, the USDM conversion model, the custody separation through an independent multisig council, the major identified risks, and governance review triggers for drawdown, missed reporting, custody, accounting, stablecoin, redemption, or smart contract concerns. But important claims were not independently evidenced in the supplied review, including Strike’s claimed volume, trade count, trader count, protocol revenue, liquidity-provider profit, and claim of representing over 50% of Cardano trading activity during the past six months. The review also found thin claims-and-evidence status, no documented milestone-gated disbursement, missing independent assurance, and no dependency map.

Because this is a TreasuryWithdrawals action, BEACN applies elevated scrutiny: shared ADA is being put at market, stablecoin, custody, smart contract, and execution risk. The proposal has enough structure to review, but not enough verified evidence to vote yes or no. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus replayable independent evidence for the major adoption and market-share claims and stronger treasury-risk documentation such as milestone-gated disbursement, independent assurance, and dependency mapping.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM stablecoin liquidity and returned after the deployment period.
- finding: Recipient: independent council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta as administrator and multisig overseer; exact treasury receiving account not stated in document
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital as USDM-denominated liquidity for Strike Finance V2, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, to the Cardano Treasury at month 12, minus any realized losses in wind-down scenarios, Provide monthly public transparency reports covering deployment status, utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and material risks, Provide third-party assurance reports at deployment confirmation, month-6 distribution, and month-12 return
- finding: Deadline/expiry: 12 months after deployment; month-6 yield distribution; monthly reporting; wind-down reconciliation within 30 days if triggered
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment into Strike Finance V2 rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to produce approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): Under modeled assumptions of a 10% USD-denominated annual percentage rate, the deployment is expected to generate approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, but returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike claims it has processed more than 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served more than 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity-provider profit.
- finding: Claim (adoption, proposer_asserted, high materiality): The document claims Strike represented over 50% of Cardano trading activity during the past six months.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states that operational custody will be handled by an independent multisig council and that Strike Finance will not have unilateral custody or control of treasury assets.
- missing: Independent evidence for: Strike claims it has processed more than 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served more than 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity-provider profit.
- missing: Independent evidence for: The document claims Strike represented over 50% of Cardano trading activity during the past six months.
- missing: Independent evidence for: Strike V2 is described as live on mainnet with public performance history, unofficial reviews, and an official audit by Christian Schmitz expected to be finalized by July 1, 2026.
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
- finding: Strongest NO: a material claim is unsupported — "Strike claims it has processed more than 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served more than 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity-provider profit." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is justified because the request exposes treasury assets to market, stablecoin, custody, and smart contract risks while several key traction, market-share, audit, and performance claims are stated without references in the anchor document. The proposal does include concrete terms, reporting commitments, custody separation, and risk triggers, so the adjustment should remain small rather than overriding the deterministic assessment.
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
- Claims and evidence missing: Independent evidence for: Strike claims it has processed more than 1.13 billion USD in cumulative volume, facilitated roughly 968,000 to 1,001,000 trades, served more than 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity-provider profit.
- Claims and evidence missing: Independent evidence for: The document claims Strike represented over 50% of Cardano trading activity during the past six months.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `1b091b80946f67485feefea5fb75a44b5fb54c34efc039817dd93cb3cf83751b`
- snapshot_bundle_hash: `bf8cf91ed67bebbb79de72cd10e2ece039cacd09d0c9e9018f6bc17fd08cc807`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

