# Rationale: gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlpgcp0jyh
Recommendation: **NO**
Score: `-0.1033` (raw `-0.1233` + doctrine-LLM nudge `+0.02`) | Confidence: `0.6233` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw ₳212,000 for AdaStat.net Cardano blockchain explorer. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw ₳212,000 for AdaStat.net Cardano blockchain explorer. The recorded treasury amount is 212.0k ADA. The strongest grounded claim is: This treasury withdrawal funds AdaStat.net Cardano blockchain explorer which will provide the following services: We propose to continue development and support of the AdaStat.net Cardano blockchain explorer for the next 24 months.

Residual uncertainty remains limited to the replayed evidence and the public resources cited by the run manifest.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 570
- finding: Expires after epoch: 577
- finding: Treasury request: 212.0k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: complete
- finding: Requested: Withdraw ₳212,000 for AdaStat.net Cardano blockchain explorer
- finding: Recipient: 
- finding: Stated amount: 212.0k ADA
- finding: Deliverables: This treasury withdrawal funds AdaStat.net Cardano blockchain explorer which will provide the following services: We propose to continue development and support of the AdaStat.net Cardano blockchain explorer for the next 24 months., Planned work includes performance optimizations, improvements to UX/UI, and new features related to Cardano's evolving governance model and on-chain tooling., The frontend is developed using Vue.js and Tailwind CSS, which allows very small bundle size and fast loading time on different devices., The backend is built on Node.js and PostgreSQL, combining standard DB-Sync tables with custom-optimized indexes for high-speed data access.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, independently_verifiable, high materiality): This treasury withdrawal funds AdaStat.net Cardano blockchain explorer which will provide the following services: We propose to continue development and support of the AdaStat.net Cardano blockchain explorer for the next 24 months.
- finding: Claim (economic, independently_verifiable, medium materiality): Planned work includes performance optimizations, improvements to UX/UI, and new features related to Cardano's evolving governance model and on-chain tooling.
- finding: Claim (economic, independently_verifiable, low materiality): The frontend is developed using Vue.js and Tailwind CSS, which allows very small bundle size and fast loading time on different devices.
- finding: Claim (technical, independently_verifiable, low materiality): The backend is built on Node.js and PostgreSQL, combining standard DB-Sync tables with custom-optimized indexes for high-speed data access.
- finding: Claim (economic, independently_verifiable, low materiality): This proposal aims to solve the following problem: It's still a challenge to provide Cardano blockchain data in a way that's both decentralized and easy to use.
- finding: Claim (economic, independently_verifiable, medium materiality): Blockchain explorers are key tools in solving this issue, as they provide access to information about blocks, transactions, stake pools, governance activities, and other on-chain operations.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 212.0k ADA
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
- finding: Flag count: 1
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal funds AdaStat.net Cardano blockchain explorer which will provide the following services: We propose to continue development and support of the AdaStat.net Cardano blockchain explorer for the next 24 months." and clears the evidence gates.
- finding: Strongest NO: weak controls, unclear delivery, or governance precedent could outweigh the benefit of TreasuryWithdrawals.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 212.0k ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal funds AdaStat.net Cardano blockchain explorer which will provide the following services: We propose to continue development and support of the AdaStat.net Cardano blockchain explorer for the next 24 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `5c9cb61a925b829be3aa4b5bda2a7dae037c1c932b62957b6a38f789a2ef3d4c`
- snapshot_bundle_hash: `2a9b40686517c438d1108145af734f48ae579b26344a141f47e8e1dd24fe02df`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `576`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2421, "NO": 0.5991, "YES": 0.1588}`

