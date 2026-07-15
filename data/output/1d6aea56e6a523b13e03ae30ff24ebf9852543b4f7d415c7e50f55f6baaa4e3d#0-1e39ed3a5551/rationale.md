# Rationale: 1d6aea56e6a523b13e03ae30ff24ebf9852543b4f7d415c7e50f55f6baaa4e3d#0
Recommendation: **NEEDS_MORE_INFO**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.2` | Readiness: `0`


## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Withdraw ₳5M for Cardano's Global Listing Expansion - Powered by Snek. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw ₳5M for Cardano's Global Listing Expansion - Powered by Snek. It asks the treasury for 5.00M ADA. The strongest grounded claim is: This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms.

BEACN's own independent diligence is also incomplete — before this vote could move to YES, BEACN's published review still needs complete proposal summary; budget analysis; feasibility assessment. Reason code: DEEP_RESEARCH_REQUIRED.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
- finding: Proposed epoch: 573
- finding: Expires after epoch: 580
- finding: Treasury request: 5.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Withdraw ₳5M for Cardano's Global Listing Expansion - Powered by Snek
- finding: Recipient: 
- finding: Stated amount: 5.00M ADA
- finding: Deliverables: This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms., SNEK is the largest community token on Cardano, holding the highest market capitalization, over 42,000 wallets, and more than 2 billion ADA in all-time trading volume., Over the past two years, the Snek Foundation has already invested over $4 million, entirely self funded, to secure major exchange listings., We’ve delivered the first and second ever Tier 1 listings for any Cardano native token, with Kraken and Crypto.com setting historic precedents for the ecosystem.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms.
- finding: Claim (economic, supported_in_proposal, medium materiality): SNEK is the largest community token on Cardano, holding the highest market capitalization, over 42,000 wallets, and more than 2 billion ADA in all-time trading volume.
- finding: Claim (economic, supported_in_proposal, high materiality): Over the past two years, the Snek Foundation has already invested over $4 million, entirely self funded, to secure major exchange listings.
- finding: Claim (economic, supported_in_proposal, low materiality): We’ve delivered the first and second ever Tier 1 listings for any Cardano native token, with Kraken and Crypto.com setting historic precedents for the ecosystem.
- finding: Claim (economic, proposer_asserted, low materiality): This proposal aims to address the following challenges: - Lack of exchange presence for Cardano native tokens: Most major centralized exchanges and retail brokers still do not support Cardano Native Tokens (CNTs).
- finding: Claim (economic, supported_in_proposal, low materiality): This severely limits Cardano’s accessibility and competitiveness on a global scale.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 5.00M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms." though 7 review blocker(s) remain open.
- finding: Strongest NO: an unresolved blocker (missing complete proposal summary) means costs or weak controls may outweigh the claimed benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Treasury actions are high-impact and require a completed deep research dossier.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 5.00M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal funds the Cardano Global Listing Expansion initiative, a strategic proposal by the Snek Foundation to list SNEK on major centralized exchanges (CEXs), retail brokers, and other widely adopted platforms." though 7 review blocker(s) remain open.
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
- Claims and evidence missing: complete proposal summary
- Claims and evidence missing: budget analysis
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Missing Evidence
- Deep research dossier is required for treasury actions before directional voting.
- Complete proposal summary, budget analysis, feasibility, risks, alternatives, and failure-mode sections.
- Missing dossier section: complete proposal summary
- Missing dossier section: budget analysis
- Missing dossier section: feasibility assessment
- Missing dossier section: risk analysis
- Missing dossier section: alternatives analysis
- Missing dossier section: failure-mode analysis
- Missing dossier section: community impact analysis

## Reproducibility
- input_hash: `1e39ed3a555114b7d779b5e8c05eb60084fab5509da0a5a5f363e85c295a242b`
- snapshot_bundle_hash: `5c166d7ad1fd723a2eb4ebdad0162a496d98ac76b37d69979b4e90fe17254ab8`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.37, "NO": 0.315, "YES": 0.315}`

