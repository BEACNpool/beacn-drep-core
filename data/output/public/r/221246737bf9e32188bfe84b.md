# Rationale: gov_action1fdatlfcdnzzcw5x9pnt9r42v992nqw65zze57s8tyk0jll78eyusqccn9gc
Recommendation: **NO**
Score: `-0.4033` (raw `-0.3833` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.75`
> Reasoning layer (precomputed): The proposal has meaningful governance and stewardship features, including milestone-based multisig disbursement, separate auditable holding accounts, abstain delegation, KPI reporting requirements, and an independently verifiable prior repayment transaction. However, several high-materiality benefits remain mostly proposer-asserted, including KPI impact, live on-chain KPI dashboard maturity, and the claimed official documentation recognition, while the request is large and the detailed milestone and budget terms are only referenced externally rather than contained in the supplied document. A small cautionary nudge is justified because treasury stewardship and evidence quality should weigh ahead of plausible ecosystem growth.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large 20,000,000 ADA treasury request and several high-materiality claims did not have enough independent, replayable evidence to meet the higher bar for shared treasury withdrawals.

The proposal requested funding for the Cardano Builder DAO, described as a smart contract-governed funding mechanism for builders working toward Cardano Vision 2030 KPIs such as monthly active users, on-chain transactions, and TVL. It also proposed milestone-based disbursement through an independent dRep DAO council/multisig, KPI reporting by funded projects, continued dashboard development, and returning unused funds to the Cardano Treasury.

BEACN found meaningful strengths in the proposal. The pinned anchor document was available, the proposal described governance participation from prior rounds, independent multisig administration, separate auditable holding accounts, abstain delegation, milestone validation before disbursement, and one independently verifiable prior return of unused ADA. It also supported the claim that funded projects would track and publicly report core KPIs.

The NO vote came from the remaining evidence gaps and treasury risk. Key benefit claims were still mostly proposer-asserted, including the DAO’s ecosystem-wide role, the maturity of its live on-chain KPI dashboard, and claimed official documentation recognition. The review also found thin claims-and-evidence status, no line-item budget, no sustainability path, unknown execution risk, no independent assurance, and no dependency map. For a treasury withdrawal of this size, BEACN judged that plausible ecosystem benefit was outweighed by insufficient evidence and stewardship detail.

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
- finding: Requested: Treasury withdrawal for the Cardano Builder DAO, described as a smart contract-governed funding mechanism for builders advancing Cardano Vision 2030 KPIs.
- finding: Recipient: Cardano Builder DAO, with withdrawal administered by an independent dRep DAO council/multisig before milestone-based disbursement.
- finding: Stated amount: 20000000
- finding: Deliverables: Allocate capital to builders expected to improve monthly active users, monthly on-chain transactions, and TVL., Require funded projects to track core KPIs including monthly active users, TVL, and on-chain transactions., Continue KPI dashboard development toward live on-chain Cardano data and standardized KPI tracking with dReps., Use an independent multisig administrator to validate milestone completion before disbursing funds., Return unused or unallocated DAO treasury funds to the Cardano Treasury.
- finding: Deadline/expiry: not stated in document
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal says the Cardano Builder DAO is an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs such as monthly active users, monthly on-chain transactions, and TVL.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal says funded projects are required to track monthly active users, TVL, and on-chain transactions, with public reporting and increasingly on-chain KPI verification.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims the DAO built Version 1 and Version 2 of a KPI dashboard, moving from self-reported KPI tracking toward tracking tied directly to live on-chain Cardano data.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal states the CB DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states Round 1 included 38 voting members, 27 requesting members, 20 funded companies, an 83% governance participation rate, and 5,541,335 ADA distributed through a smart contract-governed process.
- finding: Claim (governance, supported_in_proposal, high materiality): The proposal states Round 2 added 18 new members, funded 14 companies, and had an 88% member participation rate after review, debate, temperature checks, and final voting.
- missing: Independent evidence for: The proposal says the Cardano Builder DAO is an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs such as monthly active users, monthly on-chain transactions, and TVL.
- missing: Independent evidence for: The proposal claims the DAO built Version 1 and Version 2 of a KPI dashboard, moving from self-reported KPI tracking toward tracking tied directly to live on-chain Cardano data.
- missing: Independent evidence for: The proposal states the CB DAO has already distributed 11.1 million ADA across 34 proposals in two funding rounds.
- missing: Independent evidence for: The proposal claims official Cardano developer documentation describes the CB DAO as a smart contract-governed mechanism with more than 50 established Cardano projects participating in funding decisions and KPI tracking tied to on-chain activity, users, and TVL.
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
- finding: Strongest YES: the proposal substantiates "The proposal says funded projects are required to track monthly active users, TVL, and on-chain transactions, with public reporting and increasingly on-chain KPI verification." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says the Cardano Builder DAO is an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs such as monthly active users, monthly on-chain transactions, and TVL." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal says funded projects are required to track monthly active users, TVL, and on-chain transactions, with public reporting and increasingly on-chain KPI verification." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has meaningful governance and stewardship features, including milestone-based multisig disbursement, separate auditable holding accounts, abstain delegation, KPI reporting requirements, and an independently verifiable prior repayment transaction. However, several high-materiality benefits remain mostly proposer-asserted, including KPI impact, live on-chain KPI dashboard maturity, and the claimed official documentation recognition, while the request is large and the detailed milestone and budget terms are only referenced externally rather than contained in the supplied document. A small cautionary nudge is justified because treasury stewardship and evidence quality should weigh ahead of plausible ecosystem growth.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposal says the Cardano Builder DAO is an ecosystem-wide, smart contract-governed funding mechanism for projects advancing Cardano Vision 2030 KPIs such as monthly active users, monthly on-chain transactions, and TVL.
- Claims and evidence missing: Independent evidence for: The proposal claims the DAO built Version 1 and Version 2 of a KPI dashboard, moving from self-reported KPI tracking toward tracking tied directly to live on-chain Cardano data.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `a9ef0a5602718bb0b7423e1d46f48853de33e857166f302f75c1d10508206e14`
- snapshot_bundle_hash: `f40c2a5c6a7d77aa69d68206c12f0d83e97eac1a5704628d38d020b646a18509`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1825, "NO": 0.7762, "YES": 0.0413}`

