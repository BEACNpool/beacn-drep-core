# Rationale: 7d37220b71806410cc8adfbdafbad494e1ce3fdc674ab13c88a72b3b27de78d9#0
Recommendation: **NO**
Score: `-0.25` (binding treasury composite; advisory raw signal `-0.25`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7525` | Readiness: `0.75`
> Reasoning layer (precomputed): No additional adjustment is justified because the reimbursive purpose and direct on-chain distribution fit treasury stewardship, but the material facts about the node bug, unrecovered deposit, recipient history, and NCL compliance are mostly proposer-asserted, and the deterministic assessment already captures the thin and incomplete evidence state.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Reimburse Ikigai Info Governance Action Deposit. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to reimburse the lost Ikigai Info governance action deposit and claimed lost staking rewards. It asks the treasury for 103000 ADA. The strongest grounded claim is: An Info governance action titled Cardanoの生きがい - Ikigai - was submitted in September 2024 shortly after the Chang hard fork.

A material claim remains proposer-asserted or thinly supported: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.

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
- finding: Requested: Treasury withdrawal to reimburse the lost Ikigai Info governance action deposit and claimed lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter / intended recipient; specific identity or address not stated in document
- finding: Stated amount: 103000
- finding: Deliverables: Reimburse the claimed 100,000 ADA lost governance action deposit, Pay an additional 3,000 ADA for claimed lost staking rewards, Distribute funds directly on-chain to the intended recipient upon enactment
- finding: Deadline/expiry: Instantly as part of governance action enactment on-chain
- finding: Claim (governance, independently_verifiable, medium materiality): An Info governance action titled Cardanoの生きがい - Ikigai - was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai Info governance action was symbolic and asked the community to agree with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer says there was significant community sentiment that the submitter should be reimbursed for the lost deposit.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested 103,000 ADA consists of the original 100,000 ADA deposit plus 3,000 ADA for claimed lost staking rewards calculated at 2% per annum.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer says there was significant community sentiment that the submitter should be reimbursed for the lost deposit.
- missing: Independent evidence for: The Cardano in Oceania initiative included this reimbursement in its budget Info governance action, but that action was not approved.
- missing: Independent evidence for: The recipient has not previously received funds from the Cardano treasury.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 103000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "An Info governance action titled Cardanoの生きがい - Ikigai - was submitted in September 2024 shortly after the Chang hard fork." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "An Info governance action titled Cardanoの生きがい - Ikigai - was submitted in September 2024 shortly after the Chang hard fork." and clears the evidence gates.
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
- Treasury flow signal is in unsustainable regime, ratio 2.14 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The proposer says there was significant community sentiment that the submitter should be reimbursed for the lost deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `069bf67770c57d64441ef44ba89955471afc6720f9d5f64e0cfcced0e1029a5b`
- snapshot_bundle_hash: `bb8aef484e16b951c109e151a84a07ac7e0d80b72653c5ccebf465cebd4430c7`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `dc656aa3e4c4b3f765fea44bdb4daf06c96f58a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2143, "NO": 0.7382, "YES": 0.0474}`

