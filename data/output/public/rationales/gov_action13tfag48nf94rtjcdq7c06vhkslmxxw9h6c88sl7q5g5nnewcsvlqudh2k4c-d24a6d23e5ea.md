# Rationale: gov_action13tfag48nf94rtjcdq7c06vhkslmxxw9h6c88sl7q5g5nnewcsvlqudh2k4c
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.1833` (raw `-0.1833` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7658` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Withdraw ₳11,070,323 for TWEAG's Proposals for multiple core budget project. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw ₳11,070,323 for TWEAG's Proposals for multiple core budget project. It asks the treasury for 11.07M ADA. The strongest grounded claim is: This treasury withdrawal funds TWEAG's Proposals for multiple core budget projects for Cardano 2025 which will provide the following services: A suite of core infrastructure projects aimed at advancing the technical foundations of the Cardano blockchain.

Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 570
- finding: Expires after epoch: 577
- finding: Treasury request: 11.07M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw ₳11,070,323 for TWEAG's Proposals for multiple core budget project...
- finding: Recipient: 
- finding: Stated amount: 11.07M ADA
- finding: Deliverables: This treasury withdrawal funds TWEAG's Proposals for multiple core budget projects for Cardano 2025 which will provide the following services: A suite of core infrastructure projects aimed at advancing the technical foundations of the Cardano blockchain., These initiatives focus on novel, high-impact developments across key areas of the Cardano stack., In the months ahead, Tweag intends to collaborate closely with qualified suppliers, DReps, and Intersect to further shape the structure and scope of these engagements., The proposals presented here represent Tweag's intended contribution to Cardano's continued evolution.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, independently_verifiable, high materiality): This treasury withdrawal funds TWEAG's Proposals for multiple core budget projects for Cardano 2025 which will provide the following services: A suite of core infrastructure projects aimed at advancing the technical foundations of the Cardano blockchain.
- finding: Claim (economic, independently_verifiable, low materiality): These initiatives focus on novel, high-impact developments across key areas of the Cardano stack.
- finding: Claim (economic, independently_verifiable, low materiality): In the months ahead, Tweag intends to collaborate closely with qualified suppliers, DReps, and Intersect to further shape the structure and scope of these engagements.
- finding: Claim (economic, independently_verifiable, low materiality): The proposals presented here represent Tweag's intended contribution to Cardano's continued evolution.
- finding: Claim (technical, independently_verifiable, medium materiality): This proposal aims to solve the following problem: Backed by Tweag by Modus Create and a consortium of trusted ecosystem contributors, this proposal combines deep technical experience with proven delivery capability.
- finding: Claim (economic, independently_verifiable, low materiality): It not only addresses current pain points but lays the groundwork for Cardano's continued success as a scalable, decentralized, and open blockchain platform.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 11.07M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal funds TWEAG's Proposals for multiple core budget projects for Cardano 2025 which will provide the following services: A suite of core infrastructure projects aimed at advancing the technical foundations of the Cardano blockchain." and clears the evidence gates.
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
- Treasury analysis: Requested ADA: 11.07M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal funds TWEAG's Proposals for multiple core budget projects for Cardano 2025 which will provide the following services: A suite of core infrastructure projects aimed at advancing the technical foundations of the Cardano blockchain." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence
- delivery controls, milestones, assurance, or remedy path

## Reproducibility
- input_hash: `d24a6d23e5ea761a97dfa39459a1ad3b6fb2dc920c6ba549b47ce36f186dfa6a`
- snapshot_bundle_hash: `73f15f14c06192b3e6b194d7d79331aa6e812a38629fed7f820c31c451c5fad2`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `17`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5114, "NO": 0.4276, "YES": 0.061}`

