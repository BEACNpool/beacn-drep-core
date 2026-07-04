# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4933` (raw `-0.4533` + doctrine-LLM nudge `-0.04`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The extracted claims describe a plausible reimbursement purpose, but the assessment says evidence is thin and treasury analysis is incomplete, with missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than spending on an under-evidenced reimbursement request.

## Plain-language explanation (precomputed)
BEACN voted NO because the central justification for spending treasury funds was not independently supported: the proposal says a Cardano node bug caused the submitter to lose access to the 100,000 ADA deposit, but the review did not find replayable independent evidence for that claim.

The action requested 103,000 ADA from the treasury: 100,000 ADA to reimburse the original Ikigai Info governance action deposit, plus 3,000 ADA for estimated lost staking rewards. The proposal said the Ikigai Info action was submitted in September 2024 after Chang, that it was symbolic, that community sentiment favored reimbursement, that no later approved budget covered it, and that the requested amount was within the Net Change Limit. The anchor document was available, and the existence of the Ikigai action was supported in the proposal, but several important claims remained only proposer-asserted.

Because this is a treasury withdrawal, BEACN applied a higher evidence bar. Execution risk was assessed as low, and milestone gating was not treated as central because this was a one-time reimbursement rather than a project budget. But the treasury review was still incomplete: budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis were missing. The review also noted thin evidence, missing independent assurance, and an unsustainable treasury flow signal.

The strongest case for YES was that the proposal documents a plausible reimbursement request tied to a real prior Info action. But BEACN’s vote turned on treasury stewardship and precedent: without independent evidence for the claimed bug and loss, and without the missing treasury diligence, the proposal did not clear the bar for spending shared ADA.

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
- finding: Requested: Reimburse the lost deposit for the Ikigai Info governance action, including estimated lost staking rewards.
- finding: Recipient: not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain treasury withdrawal distribution to the intended recipient upon enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (governance, supported_in_proposal, medium materiality): An Info governance action titled Cardanoの生きがい - Ikigai - was submitted in September 2024 after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai action was symbolic and asked whether the community agreed with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The community expressed sentiment at the time that the Ikigai Info governance action deposit should be reimbursed via a treasury withdrawal.
- finding: Claim (governance, proposer_asserted, medium materiality): No entity-based budget submissions included the reimbursement after treasury withdrawals became available following the Plomin hard fork.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- missing: Independent evidence for: The community expressed sentiment at the time that the Ikigai Info governance action deposit should be reimbursed via a treasury withdrawal.
- missing: Independent evidence for: No entity-based budget submissions included the reimbursement after treasury withdrawals became available following the Plomin hard fork.
- missing: Independent evidence for: The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
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
- finding: Strongest YES: the proposal substantiates "An Info governance action titled Cardanoの生きがい - Ikigai - was submitted in September 2024 after the Chang hard fork." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "An Info governance action titled Cardanoの生きがい - Ikigai - was submitted in September 2024 after the Chang hard fork." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.040 (clamped to ±0.05): The extracted claims describe a plausible reimbursement purpose, but the assessment says evidence is thin and treasury analysis is incomplete, with missing budget, feasibility, alternatives, failure-mode, and community-impact analysis. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than spending on an under-evidenced reimbursement request.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The community expressed sentiment at the time that the Ikigai Info governance action deposit should be reimbursed via a treasury withdrawal.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `4c0cb23eb7a4018a1b50833208e9bd1bf8050cbb913d796bdaf31224e786e3bf`
- snapshot_bundle_hash: `3912d94e3a40582ee833f9fc4a62acae000a23c1d907b52e62df50c841c34125`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

