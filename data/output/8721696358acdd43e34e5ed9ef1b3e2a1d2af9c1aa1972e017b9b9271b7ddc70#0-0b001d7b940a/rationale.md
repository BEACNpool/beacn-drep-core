# Rationale: 8721696358acdd43e34e5ed9ef1b3e2a1d2af9c1aa1972e017b9b9271b7ddc70#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a high-impact treasury withdrawal and the required deep-research dossier was not complete enough to support a directional vote.

The proposal asks for 9,000,000 ADA to be deployed for 12 months into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity. The proposer describes this as a productive treasury deployment rather than grant funding, administered by an independent multisig council, with month-6 yield returned to the Treasury and full wind-down at month 12 minus any realized losses. The proposal also promises monthly public reporting and third-party assurance reports at deployment, month 6, and month 12.

Several core claims were supported inside the proposal: the requested structure, the ADA-to-USDM deployment model, the 10% modeled annual return with no guarantee, the independent multisig arrangement, the 12-month targets, and the list of material risks. But important claims were still unsupported by independent evidence, including Strike’s reported historical volume, trades, traders, protocol revenue, liquidity provider profit, and the claim that liquidity depth is the main constraint on further growth. The review also found treasury analysis incomplete, with missing milestone-gated disbursement, and risk review incomplete, with missing independent assurance and dependency mapping.

This is a conservative, evidence-based hold. A directional vote would be unblocked by a completed deep-research dossier with replayable public evidence for the major adoption and economic claims, a complete treasury analysis including milestone-gated disbursement, and a stronger risk review covering independent assurance and key dependencies.

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
- finding: Deep research dossier: required
- finding: Requested: 12-month productive treasury deployment into Strike Finance V2 liquidity infrastructure, with ADA sold for USDM to provide stablecoin-denominated liquidity
- finding: Recipient: Independent multisig council composed of Rami from Snek, Phil from Surf, and James from Monetra/Moneta as administrator
- finding: Stated amount: 9000000
- finding: Deliverables: Deploy treasury-owned capital as USDM liquidity for Strike Finance V2, Return realized yield from the first six months to the Cardano Treasury at month 6, Return 100% of treasury-owned deployed assets plus remaining realized yield, minus any realized losses in wind-down, at month 12, Provide monthly public transparency reports covering deployment status, utilization, volume, open interest, P&L, yield, drawdown, stablecoin exposure, market quality, distributions, and risks, Provide third-party assurance reports at deployment confirmation, month 6, and month 12
- finding: Deadline/expiry: 12 months after deployment, with month-6 yield distribution
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity rather than grant funding.
- finding: Claim (economic, supported_in_proposal, high materiality): The deployed ADA will be sold for USDM, with modeling assuming ADA equals 0.15 USD and approximately 1,350,000 USDM of deployed liquidity.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal models a 10% USD-denominated annual return, generating approximately 135,000 USD or 900,000 ADA-equivalent in annual yield, but states returns are not guaranteed.
- finding: Claim (adoption, proposer_asserted, high materiality): Strike reports over 1.13 billion USD in cumulative volume, around one million trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- finding: Claim (adoption, supported_in_proposal, high materiality): Strike V2 public data from 2026-03-20 through 2026-06-15 is presented as evidence of rapid growth in volume, trades, users, revenue, open interest, and vault TVL.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states that the main constraint on further Strike growth is liquidity depth and that additional stablecoin liquidity would improve execution, volume, fee generation, and Cardano-native DeFi strength.
- missing: Independent evidence for: Strike reports over 1.13 billion USD in cumulative volume, around one million trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- missing: Independent evidence for: The proposal states that the main constraint on further Strike growth is liquidity depth and that additional stablecoin liquidity would improve execution, volume, fee generation, and Cardano-native DeFi strength.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity rather than grant funding." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Strike reports over 1.13 billion USD in cumulative volume, around one million trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 9,000,000 ADA for a 12-month deployment into Strike Finance V2 liquidity rather than grant funding." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional voting is blocked until dossier quality gates pass.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Dossier completeness not confirmed for this treasury proposal.
- Claims and evidence missing: Independent evidence for: Strike reports over 1.13 billion USD in cumulative volume, around one million trades, over 3,000 unique traders, over 1.16 million USD in protocol revenue, and over 3.25 million USD in liquidity provider profit.
- Claims and evidence missing: Independent evidence for: The proposal states that the main constraint on further Strike growth is liquidity depth and that additional stablecoin liquidity would improve execution, volume, fee generation, and Cardano-native DeFi strength.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.

## Reproducibility
- input_hash: `0b001d7b940aff34fec275dd6e270f94ecf4a3ceb56c4b50849269eef1555718`
- snapshot_bundle_hash: `652c61c7e1e238c8b2500d5001351e9e403aef8929eeabe88451920421e63434`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

