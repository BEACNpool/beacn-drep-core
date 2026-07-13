# Rationale: d52a4917df4f91c342eaf06ebb4c0a5c3156f6412d137f307cc77eb911f47ab1#0
Recommendation: **NO**
Score: `-0.2394` (raw `-0.18` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7498` | Readiness: `0.7`
> Reasoning layer (precomputed): The request is narrow and reimbursement-oriented, but the highest-materiality claims about the node bug, unrecoverable deposit, prior treasury funding, and NCL compliance are largely proposer asserted in the document. Given the deterministic assessment says evidence is thin and overall status is incomplete, a small cautionary nudge is justified rather than a spending-positive adjustment.

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Reimburse Ikigai Info Governance Action Deposit. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Reimburse the lost deposit for the Ikigai Info governance action, including compensation for missed staking rewards. It asks the treasury for 103,000 ADA. The strongest grounded claim is: An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.

A material claim remains proposer-asserted or thinly supported: A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.

## Review Tree
- overall_status: `incomplete`

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
- finding: Deep research dossier: complete
- finding: Requested: Reimburse the lost deposit for the Ikigai Info governance action, including compensation for missed staking rewards.
- finding: Recipient: Ikigai Info governance action submitter
- finding: Stated amount: 103,000
- finding: Deliverables: Instant on-chain treasury withdrawal to the intended recipient upon enactment
- finding: Deadline/expiry: instantly performed as part of governance action enactment on-chain
- finding: Claim (governance, supported_in_proposal, medium materiality): An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork.
- finding: Claim (governance, proposer_asserted, low materiality): The Ikigai action was symbolic and asked the community whether they agreed with a statement thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for missed staking rewards at 2% per annum.
- finding: Claim (adoption, proposer_asserted, medium materiality): The Cardano community expressed significant sentiment that the lost Ikigai deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- missing: Independent evidence for: The Cardano community expressed significant sentiment that the lost Ikigai deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- missing: Independent evidence for: The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
- missing: Independent evidence for: The recipient of this reimbursement has not previously received funds from the treasury.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 103000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: not confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: not confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: low
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: not confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: not confirmed
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit." — so cost or precedent may outweigh the benefit.
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
- Risk review: Execution risk: low
- Counterargument pass: Strongest YES: the proposal substantiates "An Info governance action titled "Cardanoの生きがい - Ikigai -" was submitted in September 2024 shortly after the Chang hard fork." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The request is narrow and reimbursement-oriented, but the highest-materiality claims about the node bug, unrecoverable deposit, prior treasury funding, and NCL compliance are largely proposer asserted in the document. Given the deterministic assessment says evidence is thin and overall status is incomplete, a small cautionary nudge is justified rather than a spending-positive adjustment.
- Directional NO is supported by affirmative independent evidence of waste, duplication, excessive cost, or failed delivery — not by missing information.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: A Cardano node bug allowed an unregistered stake key to be used in the governance action, preventing the submitter from recovering a 100,000 ADA deposit.
- Claims and evidence missing: Independent evidence for: The Cardano community expressed significant sentiment that the lost Ikigai deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance

## Reproducibility
- input_hash: `67379b6b5defc8add38f1be6384f3fd8bc53b678e3bd69946308b40385af3918`
- snapshot_bundle_hash: `2006ce3b67a6828a215cf0d5fdef09cd0a3518442ec5dcf7c556a888e0bd6640`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `d43566c2ec38caf2768100e67762e66da78895a8`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `8`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2169, "NO": 0.7351, "YES": 0.0479}`

