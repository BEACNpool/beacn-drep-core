# Rationale: gov_action1fdatlfcdnzzcw5x9pnt9r42v992nqw65zze57s8tyk0jll78eyusqccn9gc
Recommendation: **NO**
Score: `-0.4033` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal has public-benefit alignment and some governance safeguards, but many high-materiality claims about prior distributions, participation, KPI impact, and execution quality are asserted in the anchor rather than evidenced directly, while the request is a large treasury withdrawal and the detailed milestone and budget document is only referenced externally.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large 20,000,000 ADA treasury withdrawal and several material claims needed to justify that scale were not backed by independent, replayable evidence.

The proposal asked for treasury funding to continue and expand the Cardano Builder DAO as a smart contract-governed, KPI-driven funding mechanism for Cardano builders. It said funded projects would track monthly active users, TVL, and on-chain transactions; that an independent dRep DAO council or multisig would receive and administer funds before milestone-based disbursement; that pre-disbursement ADA would be held in separate auditable accounts, not staked, and delegated to abstain; and that unused or unallocated funds would be returned to the Cardano Treasury.

BEACN found several important parts of the proposal well-supported in the proposal itself, including the public-benefit purpose, KPI requirements, governance structure for fund custody, and treasury-handling commitments. However, high-materiality claims about past performance were thinner: the claims that the DAO had already distributed 11.1 million ADA across 34 proposals, and the detailed Round 1 participation and distribution figures, were treated as proposer assertions rather than independently evidenced facts. The proposal also lacked a line-item budget, a sustainability path, independent assurance, and a dependency map.

Because this is a treasury withdrawal, BEACN applied a higher evidence bar. The review recognized the strongest YES case: the proposal describes a public-benefit funding mechanism with governance safeguards and KPI tracking. But the strongest NO case carried more weight: for a request of this size, unsupported claims about prior distributions, participation, KPI impact, and execution quality create too much cost and precedent risk.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 20.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to continue and expand the Cardano Builder DAO as a smart contract-governed, KPI-driven funding mechanism for Cardano builders.
- finding: Recipient: Cardano Builder DAO, with funds initially received and administered by an independent dRep DAO council or multisig before milestone-based disbursement.
- finding: Stated amount: 20000000
- finding: Deliverables: Allocate funding to builders expected to improve monthly active users, monthly on-chain transactions, and TVL., Require funded projects to track core KPIs including monthly active users, TVL, and on-chain transactions., Operate an independent administrator process for milestone validation and disbursement., Maintain separate auditable accounts for ADA held before disbursement, with no stake pool delegation and voting delegated to predefined abstain., Return unused or unallocated DAO treasury funds to the Cardano Treasury.
- finding: Deadline/expiry: not stated in document
- finding: Claim (adoption, supported_in_proposal, high materiality): The proposal describes the Cardano Builder DAO as an ecosystem-wide, smart contract-governed funding mechanism intended to support projects advancing Cardano Vision 2030 KPIs.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says funded projects will be required to track monthly active users, TVL, and on-chain transactions.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer claims the DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer claims Round 1 funded 20 companies, involved 38 voting members and 27 requesting members, distributed 5,541,335 ADA, and achieved 83% governance participation.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer claims Round 2 funded 14 companies, added 18 new members, used review and voting processes, and achieved 88% member participation.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposer says prior funding impact was measured through public KPI dashboards, with Version 2 moving toward live on-chain Cardano data.
- missing: Independent evidence for: The proposer claims the DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- missing: Independent evidence for: The proposer claims Round 1 funded 20 companies, involved 38 voting members and 27 requesting members, distributed 5,541,335 ADA, and achieved 83% governance participation.
- missing: Independent evidence for: The proposer claims Round 2 funded 14 companies, added 18 new members, used review and voting processes, and achieved 88% member participation.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 20000000
- finding: Budget granularity: unknown
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.48
- missing: line-item budget
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal describes the Cardano Builder DAO as an ecosystem-wide, smart contract-governed funding mechanism intended to support projects advancing Cardano Vision 2030 KPIs." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer claims the DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 20000000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal describes the Cardano Builder DAO as an ecosystem-wide, smart contract-governed funding mechanism intended to support projects advancing Cardano Vision 2030 KPIs." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has public-benefit alignment and some governance safeguards, but many high-materiality claims about prior distributions, participation, KPI impact, and execution quality are asserted in the anchor rather than evidenced directly, while the request is a large treasury withdrawal and the detailed milestone and budget document is only referenced externally.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer claims the DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- Claims and evidence missing: Independent evidence for: The proposer claims Round 1 funded 20 companies, involved 38 voting members and 27 requesting members, distributed 5,541,335 ADA, and achieved 83% governance participation.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `918d7f7c613f518d034deb4507cf7fb53bf32a19433e9106f228d2425992c6e7`
- snapshot_bundle_hash: `2bb1b4b388d65634edb296db954f1a0d79279a8aeec685000f3d2d8ec42bd8b1`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1825, "NO": 0.7762, "YES": 0.0413}`

