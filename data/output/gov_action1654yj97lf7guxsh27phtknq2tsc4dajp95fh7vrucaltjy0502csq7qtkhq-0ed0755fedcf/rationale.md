# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4833` (raw `-0.4533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims describe a narrow reimbursement with a checkable governance reference, but the material basis for spending treasury funds depends on asserted facts about the node bug, unrecoverable deposit, recipient history, NCL adherence, and reward calculation. Given the deterministic assessment is blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, a small cautionary negative lean is warranted rather than a positive nudge.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the evidence and analysis bar required for spending shared ADA, with key review blockers still unresolved.

The action requested 103,000 ADA to reimburse the Ikigai Info governance action submitter for a claimed unrecovered 100,000 ADA governance action deposit plus 3,000 ADA in estimated lost staking rewards. The proposal’s core payment request was clear and supported in the proposal, and the anchor document was available, pinned, and replayable. It also claimed that a Cardano node bug prevented recovery of the deposit, that the original action was submitted shortly after Chang, that community sentiment supported reimbursement, that the recipient had not previously received treasury funds, and that the request was within the Net Change Limit.

However, several material claims remained asserted rather than independently evidenced, including details about the original September 2024 Ikigai action and other facts needed to justify treasury reimbursement. The review also found the claims-and-evidence record thin, treasury analysis incomplete, and synthesis blocked. The strongest case for YES was that the reimbursement amount and purpose were clearly stated, but five blockers remained open: missing budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis.

Because this was a TreasuryWithdrawal, BEACN applied elevated scrutiny. Execution risk was judged low and milestone-gating expectations did not apply to this one-time reimbursement, but the incomplete treasury diligence dossier, unsupported material claims, and unsustainable treasury flow signal weighed against approval. The NO vote reflects that the proposal may have a checkable reimbursement target, but did not provide enough completed public analysis to justify treasury spending and precedent.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 636
- finding: Expires after epoch: 643
- finding: Treasury request: 103.0k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Reimburse the Ikigai Info governance action submitter for an unrecovered governance action deposit plus estimated lost staking rewards.
- finding: Recipient: the Ikigai Info governance action submitter
- finding: Stated amount: 103,000
- finding: Deliverables: Instant on-chain distribution to the intended recipient as part of enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA from the Cardano treasury to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for estimated staking rewards.
- finding: Claim (governance, proposer_asserted, medium materiality): The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, medium materiality): The Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The community expressed significant sentiment at the time that the Ikigai deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork.
- missing: Independent evidence for: The Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The community expressed significant sentiment at the time that the Ikigai deposit should be reimbursed.
- missing: budget analysis
- missing: feasibility assessment
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 103000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.70
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: low
- finding: Technical risk: low
- finding: Treasury exposure risk: low
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the Cardano treasury to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for estimated staking rewards." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Treasury profile: one-time reimbursement — milestone-gating expectations do not apply.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 103000
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA from the Cardano treasury to reimburse a lost 100,000 ADA governance action deposit plus 3,000 ADA for estimated staking rewards." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The claims describe a narrow reimbursement with a checkable governance reference, but the material basis for spending treasury funds depends on asserted facts about the node bug, unrecoverable deposit, recipient history, NCL adherence, and reward calculation. Given the deterministic assessment is blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, a small cautionary negative lean is warranted rather than a positive nudge.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The original Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork.
- Claims and evidence missing: Independent evidence for: The Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `0ed0755fedcf5504018db8ac84c957f76477c64e26567a70e361a03d3861a388`
- snapshot_bundle_hash: `5bdab2ce2ed260bca758fa48e5f7431fa0640ad0275a8a591d568d607cf151a1`
- soul_commit: `c2e8563ea5ae8b932f62009a99ae2fa581788f9b`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `55b0ab6e1fe7b1169fc4a1f8c7c9e290b59af2ab`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `961`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

