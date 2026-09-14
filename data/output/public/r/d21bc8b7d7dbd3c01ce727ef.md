# Rationale: 7d37220b71806410cc8adfbdafbad494e1ce3fdc674ab13c88a72b3b27de78d9#0
Recommendation: **NO**
Score: `-0.15` (binding treasury composite; advisory raw signal `-0.15`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7275` | Readiness: `0.75`
> Reasoning layer (precomputed): The deterministic assessment already captures the incomplete status and thin evidence; under the doctrine, missing independent diligence should remain a needs-more-info condition rather than an additional directional penalty.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Reimburse Ikigai Info Governance Action Deposit. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Reimburse the Ikigai Info governance action submitter for an unrecovered governance action deposit and claimed lost staking rewards. It asks the treasury for 103000 ADA. The strongest grounded claim is: The proposal requests 103,000 ADA, consisting of a 100,000 ADA unrecovered deposit plus 3,000 ADA for staking rewards at 2% per annum.

A material claim remains proposer-asserted or thinly supported: The proposer states that a Cardano node bug allowed an unregistered stake key to be used, preventing the submitter from recovering the 100,000 ADA deposit.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 649
- finding: Expires after epoch: 656
- finding: Treasury request: 103.0k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Reimburse the Ikigai Info governance action submitter for an unrecovered governance action deposit and claimed lost staking rewards.
- finding: Recipient: not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Instant on-chain distribution of funds to the intended recipient as part of governance action enactment
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA, consisting of a 100,000 ADA unrecovered deposit plus 3,000 ADA for staking rewards at 2% per annum.
- finding: Claim (governance, independently_verifiable, medium materiality): The underlying Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork and was symbolic in nature.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer states that a Cardano node bug allowed an unregistered stake key to be used, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposer states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal states there are no associated costs or expenses beyond the withdrawal amount.
- missing: Independent evidence for: The proposer states that a Cardano node bug allowed an unregistered stake key to be used, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed.
- missing: Independent evidence for: The proposer states the Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- missing: Independent evidence for: The proposal states there are no associated costs or expenses beyond the withdrawal amount.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 103000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unknown (stale snapshot) (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA, consisting of a 100,000 ADA unrecovered deposit plus 3,000 ADA for staking rewards at 2% per annum." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer states that a Cardano node bug allowed an unregistered stake key to be used, preventing the submitter from recovering the 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
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
- Treasury profile: one-time reimbursement — milestone-gating expectations do not apply.
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 103000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 103,000 ADA, consisting of a 100,000 ADA unrecovered deposit plus 3,000 ADA for staking rewards at 2% per annum." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional NO forced: the applicable Net Change Limit is exhausted — treasury withdrawals already enacted within this NCL period leave no remaining capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury fee-flow snapshot is stale (epoch 647, ~7 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The proposer states that a Cardano node bug allowed an unregistered stake key to be used, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The proposer states there was significant community sentiment that the Ikigai Info governance action deposit should be reimbursed.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `2a1a21d0c16c329e9b5ec57e526b99b2365ebb94e716d88b43dedaf63b5176cf`
- snapshot_bundle_hash: `6b20902e01ef4dd40548e35e2dd7ee170177b75ce9fed83ecac9a6ce13fd2247`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `bd2895f90a3cd964e102675461b8ea0fbc829ea1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2291, "NO": 0.6719, "YES": 0.0991}`

