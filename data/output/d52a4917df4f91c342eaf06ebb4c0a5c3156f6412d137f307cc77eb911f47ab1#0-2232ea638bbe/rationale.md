# Rationale: d52a4917df4f91c342eaf06ebb4c0a5c3156f6412d137f307cc77eb911f47ab1#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.18` (raw `-0.18` + doctrine-LLM nudge `-0.02`) | Confidence: `0.735` | Readiness: `0.7`
> Reasoning layer (precomputed): The claims describe a plausible reimbursement case with an on-chain reference, but the material justification for the node bug, unrecoverable deposit, recipient history, NCL adherence, and reward calculation is mostly asserted rather than evidenced in the document. Given the assessment already marks claims and evidence as thin, only a small cautionary nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal depends on a required Net Change Limit check that was not pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the reimbursement case.

The action asks the treasury to pay 103,000 ADA to reimburse the Ikigai Info governance action deposit: 100,000 ADA for the original deposit and 3,000 ADA for claimed lost staking rewards at 2% per year. The proposer says the original Info action was submitted in September 2024, that a Cardano node bug allowed an unregistered stake key and made the deposit unrecoverable, that community sentiment favored reimbursement, that the recipient has not already received treasury funds, and that the request does not exceed the current Net Change Limit.

The review found the amount and basic structure of the request supported in the proposal, and the anchor document was available, pinned, and replayable. Execution risk was assessed as low, and milestone gating was not required because this is a one-time reimbursement rather than an ongoing project. But several important claims were still mostly proposer assertions rather than independently evidenced in the document, including the node-bug explanation, the unrecoverable deposit, the recipient history, and the reward calculation. Treasury actions also receive elevated scrutiny because they spend shared ADA and can set precedent.

A directional YES or NO vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. Stronger public evidence tying the key factual claims to replayable sources would also improve confidence, especially evidence for the node bug, the deposit being unrecoverable, the recipient’s prior treasury history, and the 3,000 ADA reward calculation.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: expired
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
- finding: Requested: Reimburse the lost deposit for the Ikigai Info governance action, including compensation for lost staking rewards.
- finding: Recipient: Ikigai Info governance action submitter / intended recipient, not otherwise named in document
- finding: Stated amount: 103000
- finding: Deliverables: On-chain treasury withdrawal directly to the intended recipient upon enactment, Reimbursement of 100,000 ADA governance action deposit, Additional 3,000 ADA compensation for lost staking rewards
- finding: Deadline/expiry: instantly performed as part of the governance action's enactment on-chain
- finding: Claim (governance, proposer_asserted, medium materiality): The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork as a symbolic Info action thanking contributors and expressing hope for Cardano's future.
- finding: Claim (technical, proposer_asserted, high materiality): A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer states there was significant community sentiment that the Ikigai deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- finding: Claim (governance, proposer_asserted, medium materiality): The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposer states the recipient has not previously received funds from the treasury.
- missing: Independent evidence for: The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork as a symbolic Info action thanking contributors and expressing hope for Cardano's future.
- missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- missing: Independent evidence for: The proposer states there was significant community sentiment that the Ikigai deposit should be reimbursed because the submitter was an early pioneer of Cardano governance.
- missing: Independent evidence for: The Cardano in Oceania initiative included the reimbursement in its budget Info governance action, but that governance action was not approved.
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
- finding: Strongest YES: the proposal substantiates "The proposal asks for 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork as a symbolic Info action thanking contributors and expressing hope for Cardano's future." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal asks for 103,000 ADA, consisting of the original 100,000 ADA deposit plus 3,000 ADA for lost staking rewards at 2% per annum." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The claims describe a plausible reimbursement case with an on-chain reference, but the material justification for the node bug, unrecoverable deposit, recipient history, NCL adherence, and reward calculation is mostly asserted rather than evidenced in the document. Given the assessment already marks claims and evidence as thin, only a small cautionary nudge is warranted.
- Directional treasury voting is blocked until this action is ranked against competing active proposals and verified NCL capacity.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The Ikigai Info governance action was submitted in September 2024 shortly after the Chang hard fork as a symbolic Info action thanking contributors and expressing hope for Cardano's future.
- Claims and evidence missing: Independent evidence for: A Cardano node bug permitted an unregistered stake key to be used in the governance action, preventing the submitter from recovering the 100,000 ADA deposit.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: sustainability path
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance

## Missing Evidence
- verified ecosystem benefit or strategic necessity
- delivery controls, milestones, assurance, or remedy path

## Reproducibility
- input_hash: `2232ea638bbef50da7cb2463515eb2dfd1cb5ce20d3421dcc52a7e21c43bafb2`
- snapshot_bundle_hash: `c241e9832219293e5b0e3720ff88eaa6b3cd344be208b620487c7dfe21285eee`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3d9c2c9681f9060eff076f9ca8f4e36a1ddb67a2`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5038, "NO": 0.4281, "YES": 0.0681}`

