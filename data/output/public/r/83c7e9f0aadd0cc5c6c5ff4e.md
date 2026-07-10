# Rationale: gov_action1suskjc6c4nw58c6wtmv77xe79gwj47wp4gvh9cqhhxujwxmam3cqqkz5nwj
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4933` (raw `-0.4933` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small cautionary nudge is warranted because the ask is large, the expected treasury benefit depends on modeled yield and stablecoin conversion, and several high-materiality traction and vault-performance claims are asserted in the document without attached references. The proposal does include risk disclosure, reporting, return mechanics, and multisig oversight, so the adjustment should remain modest rather than a broad rejection by reasoning alone.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal asks for 9,000,000 ADA for a 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, rather than a grant. The plan is to sell the ADA for USDM, provide stablecoin-denominated liquidity, return realized yield after six months, and return the remaining treasury-owned assets and realized yield after 12 months, subject to realized losses. The proposal also includes monthly transparency reports, third-party assurance reports, risk disclosures, and independent multisig custody.

Several core terms are supported in the proposal itself: the amount requested, the 12-month deployment structure, the ADA-to-USDM model, the modeled 10% USD-denominated APR, the proposed multisig setup, and the identified risks. However, several high-materiality performance and adoption claims remain unsupported by independent replayable evidence, including Strike’s claimed cumulative volume, trade count, user count, protocol revenue, liquidity provider profit, recent V2 volume, and vault-performance metrics.

This is a conservative, evidence-based hold, not a rejection of the idea. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable public evidence for the major adoption, volume, revenue, and vault-performance claims. The review also noted missing milestone-gated disbursement, independent assurance, and a dependency map, which matter because treasury votes consume shared ADA and require a higher evidence bar.

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
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity
- finding: Recipient: independent multisig council administering Strike Finance liquidity deployment
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital as USDM liquidity for Strike Finance V2, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets, including remaining principal and realized yield, at month 12 subject to realized losses, Provide monthly public transparency reports covering deployment status, liquidity utilization, volume, open interest, profit and loss, yield, drawdown, stablecoin exposure, market quality metrics, distributions, and material risks, Publish independent third-party assurance reports for deployment confirmation, month-6 yield distribution, and month-12 return of funds
- finding: Deadline/expiry: 12 months after deployment
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, modeled at ADA = 0.15 USD to create approximately 1,350,000 USDM of stablecoin liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated APR producing approximately 135,000 USD, or 900,000 ADA-equivalent, in annual yield, while stating returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated about 968,000 to 1,001,000 trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal states Strike V2 produced 87,288,044 USD in total volume from 2026-03-20 through 2026-06-15, including 75,322,500 USD in 30-day volume and 29,220,000 USD in 7-day volume.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal asserts the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 Sharpe ratio over two months of history.
- missing: Independent evidence for: Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated about 968,000 to 1,001,000 trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposal states Strike V2 produced 87,288,044 USD in total volume from 2026-03-20 through 2026-06-15, including 75,322,500 USD in 30-day volume and 29,220,000 USD in 7-day volume.
- missing: Independent evidence for: The proposal asserts the Strike Liquidity Provider vault has 985,271.59 USD TVL, 43.52% APR, +8.85% all-time return, 1.15% maximum drawdown, and a 4.97 Sharpe ratio over two months of history.
- missing: Independent evidence for: The proposal says Christian Schmitz is conducting an official audit expected by July 1, 2026, and that the report will be published upon completion.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated about 968,000 to 1,001,000 trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month liquidity deployment rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: A small cautionary nudge is warranted because the ask is large, the expected treasury benefit depends on modeled yield and stablecoin conversion, and several high-materiality traction and vault-performance claims are asserted in the document without attached references. The proposal does include risk disclosure, reporting, return mechanics, and multisig oversight, so the adjustment should remain modest rather than a broad rejection by reasoning alone.
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
- Claims and evidence missing: Independent evidence for: Strike claims it has processed over 1.13 billion USD in cumulative volume, facilitated about 968,000 to 1,001,000 trades, served over 3,000 unique traders, generated over 1.16 million USD in protocol revenue, and produced over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The proposal states Strike V2 produced 87,288,044 USD in total volume from 2026-03-20 through 2026-06-15, including 75,322,500 USD in 30-day volume and 29,220,000 USD in 7-day volume.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `1b091b80946f67485feefea5fb75a44b5fb54c34efc039817dd93cb3cf83751b`
- snapshot_bundle_hash: `6f7703f899cc4cb4b17b6fd89fce1cfc4d0e1be52cf15fe9e56c198e9556189b`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

