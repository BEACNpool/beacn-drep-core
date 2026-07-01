# Rationale: gov_action10dp9wzmgt2nqshyrghufff4sfhcxedhmzluly5k0azguatnsthwqqs84cjf
Recommendation: **NO**
Score: `-0.3583` (raw `-0.3233` + doctrine-LLM nudge `-0.035`) | Confidence: `0.8483` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a treasury action: 5 well-supported claim(s), 1 unsupported high-materiality claim(s), assessment blocked, 7 open blocker(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.035 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records NO on Revised Cardano Summit 2026 Singapore. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Revised Cardano Summit 2026 Singapore. The recorded treasury amount is 7.80M ADA. The strongest grounded claim is: Following extensive discussions with the community the Foundation has revised the proposal as follows: This proposal is decoupled from EMURGO’s TOKEN2049 sponsorship proposal.

A material weak point is that this claim remains proposer-asserted or thinly supported: This is a revised and 22% reduced budget treasury withdrawal proposal for the Cardano Summit 2026 in Singapore. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
- finding: Proposed epoch: 627
- finding: Expires after epoch: 634
- finding: Treasury request: 7.80M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Revised Cardano Summit 2026 Singapore
- finding: Recipient: not stated in document
- finding: Stated amount: 7.80M ADA
- finding: Deliverables: This is a revised and 22% reduced budget treasury withdrawal proposal for the Cardano Summit 2026 in Singapore., Following extensive discussions with the community the Foundation has revised the proposal as follows: This proposal is decoupled from EMURGO’s TOKEN2049 sponsorship proposal., Budget is reduced by 22% or $550,000 while retaining the tier-one experience to showcase a L1 blockchain like Cardano, achieved through reduction from three stages to two which lowers production, tech and onsite logistics costs., Increased the CF’s estimated internal resource contributions to $380,000 from $250,000 to reduce external vendor costs.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, proposer_asserted, high materiality): This is a revised and 22% reduced budget treasury withdrawal proposal for the Cardano Summit 2026 in Singapore.
- finding: Claim (economic, supported_in_proposal, medium materiality): Following extensive discussions with the community the Foundation has revised the proposal as follows: This proposal is decoupled from EMURGO’s TOKEN2049 sponsorship proposal.
- finding: Claim (economic, supported_in_proposal, high materiality): Budget is reduced by 22% or $550,000 while retaining the tier-one experience to showcase a L1 blockchain like Cardano, achieved through reduction from three stages to two which lowers production, tech and onsite logistics costs.
- finding: Claim (economic, proposer_asserted, low materiality): Increased the CF’s estimated internal resource contributions to $380,000 from $250,000 to reduce external vendor costs.
- finding: Claim (economic, supported_in_proposal, low materiality): Cardano Summit 2026 moves to Singapore because it aligns with the overall Cardano 2030 Vision and Strategy and fully supports it.
- finding: Claim (economic, supported_in_proposal, low materiality): Cardano’s next phase of adoption must be shaped where enterprise, institutional, regulatory, and developer audiences already converge.
- missing: Independent evidence for: This is a revised and 22% reduced budget treasury withdrawal proposal for the Cardano Summit 2026 in Singapore.
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
- finding: Requested ADA: 7.80M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "Following extensive discussions with the community the Foundation has revised the proposal as follows: This proposal is decoupled from EMURGO’s TOKEN2049 sponsorship proposal." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "This is a revised and 22% reduced budget treasury withdrawal proposal for the Cardano Summit 2026 in Singapore." — so cost or precedent may outweigh the benefit.
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
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 7.80M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Following extensive discussions with the community the Foundation has revised the proposal as follows: This proposal is decoupled from EMURGO’s TOKEN2049 sponsorship proposal." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.035 (clamped to ±0.05): Doctrine-aware offline lean for a treasury action: 5 well-supported claim(s), 1 unsupported high-materiality claim(s), assessment blocked, 7 open blocker(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.035 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- Claims and evidence missing: Independent evidence for: This is a revised and 22% reduced budget treasury withdrawal proposal for the Cardano Summit 2026 in Singapore.
- Claims and evidence missing: complete proposal summary
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `04b67f4b7d6b3556bb7cc6035a96dc0376094b74362ca3d92fdfa0b0e71fce16`
- snapshot_bundle_hash: `3187033437860719d444b52800f3080e06b2bfef2d2a512c1e32a090dcc55afa`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `620`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1822, "NO": 0.7752, "YES": 0.0426}`

