# Rationale: gov_action1654yj97lf7guxsh27phtknq2tsc4dajp95fh7vrucaltjy0502csq7qtkhq
Recommendation: **NO**
Score: `-0.4933` (raw `-0.4533` + doctrine-LLM nudge `-0.04`) | Confidence: `0.64` | Readiness: `0.8`
> Reasoning layer (precomputed): The claims describe a sympathetic reimbursement request, but the evidence is thin for the core treasury-relevant points: the node bug, unrecoverable loss, recipient identity, NCL adherence, prior funding status, and community support are mostly proposer-asserted. Given the deterministic assessment already flags missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, a small cautionary negative nudge is justified for treasury stewardship and evidence quality.

## Plain-language explanation (precomputed)
BEACN voted NO because this treasury withdrawal did not meet the evidence bar for spending shared ADA. The proposal asked for 103,000 ADA to reimburse an allegedly unrecoverable 100,000 ADA governance deposit, plus 3,000 ADA for lost staking rewards, but several core claims behind that reimbursement remained unsupported or incomplete.

The proposer claimed the earlier Ikigai Info action was submitted shortly after Chang, that it was symbolic, that a Cardano node bug allowed an unregistered stake key and prevented deposit recovery, that there was community support for reimbursement, that the recipient had not previously received treasury funds, and that the amount stayed within the Net Change Limit. The proposal did support the basic requested amount and calculation, and the anchor document was available and replayable. But the review found thin evidence for the most treasury-relevant points, including the alleged node bug, the unrecoverable loss, recipient identity, Net Change Limit adherence, prior funding status, and community support.

Because this is a TreasuryWithdrawals action, BEACN applied elevated scrutiny. Execution risk was judged low, and milestone gating was not applicable because this was a one-time reimbursement. However, the review still found decisive blockers: missing budget analysis, feasibility assessment, alternatives analysis, failure-mode analysis, and community impact analysis. The synthesis stage was blocked, and the treasury diligence dossier was incomplete.

The strongest case for YES was that the requested 103,000 ADA amount was clearly stated and explained. That was not enough to overcome the open blockers. BEACN’s NO vote reflects treasury stewardship: sympathetic reimbursement claims still need independently replayable evidence before public funds are withdrawn.

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
- finding: Requested: Reimburse the deposit allegedly lost by the submitter of the Ikigai Info governance action, plus compensation for staking rewards.
- finding: Recipient: not stated in document
- finding: Stated amount: 103,000
- finding: Deliverables: Instant on-chain distribution of treasury funds to the intended recipient as part of enactment
- finding: Deadline/expiry: instantly performed as part of the governance action's enactment on-chain
- finding: Claim (governance, proposer_asserted, medium materiality): The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork introduced on-chain governance.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai Info governance action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards calculated at 2% per annum.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states there was significant community sentiment at the time that the Ikigai Info governance action deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork introduced on-chain governance.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- missing: Independent evidence for: The proposer states there was significant community sentiment at the time that the Ikigai Info governance action deposit should be reimbursed.
- missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that governance action was not approved.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards calculated at 2% per annum." though 5 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork introduced on-chain governance." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards calculated at 2% per annum." though 5 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.040 (clamped to ±0.05): The claims describe a sympathetic reimbursement request, but the evidence is thin for the core treasury-relevant points: the node bug, unrecoverable loss, recipient identity, NCL adherence, prior funding status, and community support are mostly proposer-asserted. Given the deterministic assessment already flags missing budget, feasibility, alternatives, failure-mode, and community-impact analysis, a small cautionary negative nudge is justified for treasury stewardship and evidence quality.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork introduced on-chain governance.
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: missing budget analysis
- Synthesis missing: missing feasibility assessment
- Synthesis status is blocked.

## Reproducibility
- input_hash: `fd14db9c1120c688221dda5097618a890e488f36743e943568ec6e05dd49c54c`
- snapshot_bundle_hash: `f022b53854de47040cbcb2de6b49ddc0414f8c4fef323d87f49b891972275754`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `4be9e861f70b915ea4b160478106ee4b3b431e71`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1935, "NO": 0.7661, "YES": 0.0403}`

