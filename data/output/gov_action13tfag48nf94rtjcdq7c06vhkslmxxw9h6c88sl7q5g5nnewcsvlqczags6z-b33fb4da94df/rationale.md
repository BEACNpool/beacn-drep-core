# Rationale: gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlqczags6z
Recommendation: **NO**
Score: `-0.2033` (raw `-0.2233` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7708` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NO on Withdraw ₳578,571 for Gerolamo - Cardano node in typescript. On the evidence available to BEACN's published review, the request does not clear the bar for spending shared treasury funds.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw ₳578,571 for Gerolamo - Cardano node in typescript. It asks the treasury for 578.6k ADA. The strongest grounded claim is: This treasury withdrawal funds Gerolamo - Cardano node in typescript which will provide the following services: A node that can run in the browser.

Residual uncertainty remains limited to the replayed evidence and the public resources cited by the run manifest.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 570
- finding: Expires after epoch: 577
- finding: Treasury request: 578.6k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw ₳578,571 for Gerolamo - Cardano node in typescript
- finding: Recipient: 
- finding: Stated amount: 578.6k ADA
- finding: Deliverables: This treasury withdrawal funds Gerolamo - Cardano node in typescript which will provide the following services: A node that can run in the browser., This Treasury Withdrawal is submitted by Intersect on behalf of the vendor., The following sections; Abstract, Motivation, Rationale and Vendor Profile have been sourced from the approved proposal submitted by the Vendor as part of the Intersect budget process., This treasury withdrawal funds one of 39 proposals to give effect to the approved budget info action for ₳275,269,340, administered by Intersect via gov action1u9x73kwufaxa70lfy59g4ynwyrcsaxdcd0gxzzmh67s9fxq4j8hqqk2phgh.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, independently_verifiable, high materiality): This treasury withdrawal funds Gerolamo - Cardano node in typescript which will provide the following services: A node that can run in the browser.
- finding: Claim (economic, independently_verifiable, high materiality): This Treasury Withdrawal is submitted by Intersect on behalf of the vendor.
- finding: Claim (economic, independently_verifiable, high materiality): The following sections; Abstract, Motivation, Rationale and Vendor Profile have been sourced from the approved proposal submitted by the Vendor as part of the Intersect budget process.
- finding: Claim (economic, independently_verifiable, high materiality): This treasury withdrawal funds one of 39 proposals to give effect to the approved budget info action for ₳275,269,340, administered by Intersect via gov action1u9x73kwufaxa70lfy59g4ynwyrcsaxdcd0gxzzmh67s9fxq4j8hqqk2phgh.
- finding: Claim (technical, independently_verifiable, low materiality): A Typescript node would benefit the ecosystem in many ways: - Remove the ivory tower: make it easier for new developers to understand the protocol internals and contribute to the growth of Cardano.
- finding: Claim (technical, independently_verifiable, low materiality): Truly decentralized applications: every application that wants to interact with cardano needs access to a cardano node somewhere.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 578.6k ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal funds Gerolamo - Cardano node in typescript which will provide the following services: A node that can run in the browser." and clears the evidence gates.
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
- Treasury analysis: Requested ADA: 578.6k ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal funds Gerolamo - Cardano node in typescript which will provide the following services: A node that can run in the browser." and clears the evidence gates.
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
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `b33fb4da94dfcb8fcf689a12741838a90246beb508b5fdd7f7000fbdf4039159`
- snapshot_bundle_hash: `1d74533f95870e3b95c5de2f6e336382000d3e7f769f7f415c5c576253aedc80`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `15c9ee361cdd647ac25590d31885b9aa1b0cebf2`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `8`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2215, "NO": 0.729, "YES": 0.0495}`

