# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4933` (raw `-0.4533` + doctrine-LLM nudge `-0.04`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, and the extracted claims show that the central reimbursement basis, recipient history, NCL adherence, and community sentiment are mostly proposer-asserted rather than evidenced. A small negative nudge is justified because treasury stewardship and evidence quality weigh against spending real treasury funds on a thin reimbursement record, even though the action is narrow and direct.

## Plain-language explanation (precomputed)
BEACN voted NO because the proposal asks the treasury to reimburse 103,000 ADA, but the central reason for reimbursement was not independently supported: the claim that a Cardano node bug caused the submitter to lose access to the 100,000 ADA deposit remained unsupported.

The action requested a one-time treasury withdrawal to reimburse the original 100,000 ADA deposit from the Ikigai Info governance action, plus 3,000 ADA for estimated lost staking rewards. The proposer stated that the Ikigai action was submitted shortly after the Chang hard fork, was symbolic in nature, and that community sentiment favored reimbursement because the submitter was an early governance participant. The review found the existence and timing of the Ikigai Info action to be supported, and the requested amount was clearly stated. However, the key technical claim about the node bug, the claim about broad community support, the recipient history, and Net Change Limit adherence were mostly proposer-asserted rather than independently evidenced.

Because this is a treasury withdrawal, BEACN applied elevated scrutiny. The action had a pinned, replayable anchor document, and execution risk was judged low because the payment would be direct and on-chain. But the treasury diligence record was incomplete, with missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. The review also noted missing independent assurance and a thin evidence record overall.

This NO vote is therefore about treasury stewardship and evidence quality, not a judgment on the submitter. A reimbursement from shared ADA creates precedent, and BEACN did not find enough public, replayable evidence to justify spending treasury funds when the main reimbursement basis and several supporting claims remained unproven.

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
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Reimburse the deposit from the Ikigai Info governance action and compensate estimated lost staking rewards.
- finding: Recipient: the Ikigai Info governance action submitter; specific recipient address not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain distribution of 103,000 ADA to the intended recipient upon enactment
- finding: Deadline/expiry: upon governance action enactment on-chain
- finding: Claim (governance, supported_in_proposal, medium materiality): An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement of thanks and hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum.
- finding: Claim (adoption, proposer_asserted, medium materiality): The community expressed significant sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early governance pioneer.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this deposit reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The community expressed significant sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early governance pioneer.
- missing: Independent evidence for: The Cardano in Oceania initiative included this deposit reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The recipient of this reimbursement has not previously received funds from the treasury.
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
- finding: Strongest YES: the proposal substantiates "An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.040 (clamped to ±0.05): The deterministic assessment is already blocked for missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, and the extracted claims show that the central reimbursement basis, recipient history, NCL adherence, and community sentiment are mostly proposer-asserted rather than evidenced. A small negative nudge is justified because treasury stewardship and evidence quality weigh against spending real treasury funds on a thin reimbursement record, even though the action is narrow and direct.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The community expressed significant sentiment that the Ikigai Info governance action deposit should be reimbursed because the submitter was an early governance pioneer.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `4fc390c7d66e87a10c5fdb76b23f4af2fea2cef3d195f58e57fb4578c939e058`
- snapshot_bundle_hash: `846617caa863e057ddf0031e92187cb0bc1fbb7eb2d3448951747c52f82735a2`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

