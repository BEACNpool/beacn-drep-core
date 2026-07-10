# Rationale: gov_action1lqun78lcznfa2gek49m3ydslakfnm8heargfp8sax9fk54yl6ghsqp042zv
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.1833` (raw `-0.1833` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7658` | Readiness: `0.0`
> Reasoning layer (deterministic-heuristic): Doctrine-aware offline lean for a treasury action: 8 well-supported claim(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment +0.020 (clamped to ±0.05).

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Withdraw ₳70,000,000 for Cardano Critical Integrations Budget. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Withdraw ₳70,000,000 for Cardano Critical Integrations Budget. It asks the treasury for 70.00M ADA. The strongest grounded claim is: This treasury withdrawal is submitted pursuant to the Budget Info Action “Cardano Critical Integrations Budget” (gov action13a2dqgwxum7d6kjfprcs57cf9733ek2dkt5qnuhqd4ll5ntcwu7sqluwkxd) and can only be ratified if that Budget Info Action is approved by DReps.

Reason code: VERIFIED_NCL_REQUIRED.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 599
- finding: Expires after epoch: 606
- finding: Treasury request: 70.00M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Withdraw ₳70,000,000 for Cardano Critical Integrations Budget
- finding: Recipient: 
- finding: Stated amount: 70.00M ADA
- finding: Deliverables: This treasury withdrawal is submitted pursuant to the Budget Info Action “Cardano Critical Integrations Budget” (gov action13a2dqgwxum7d6kjfprcs57cf9733ek2dkt5qnuhqd4ll5ntcwu7sqluwkxd) and can only be ratified if that Budget Info Action is approved by DReps..., This governance action requests to withdraw ₳70,000,000 from the Cardano Treasury to establish a strategic integration fund supporting the onboarding of critical infrastructure, including tier-one stablecoins, institutional digital asset custody and wallet..., These integrations are foundational for tier-one stablecoin deployment, large scale DeFi growth, and acceleration of RWA and DePin activity, strengthening Cardano’s long term fee generation and treasury sustainability., This project is being driven through close collaboration between Input | Output Global, the Cardano Foundation, and EMURGO, together with Midnight Foundation and Intersect, all of whom are actively engaged in negotiations with integration partners.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, independently_verifiable, high materiality): This treasury withdrawal is submitted pursuant to the Budget Info Action “Cardano Critical Integrations Budget” (gov action13a2dqgwxum7d6kjfprcs57cf9733ek2dkt5qnuhqd4ll5ntcwu7sqluwkxd) and can only be ratified if that Budget Info Action is approved by DReps...
- finding: Claim (technical, independently_verifiable, high materiality): This governance action requests to withdraw ₳70,000,000 from the Cardano Treasury to establish a strategic integration fund supporting the onboarding of critical infrastructure, including tier-one stablecoins, institutional digital asset custody and wallet...
- finding: Claim (economic, independently_verifiable, high materiality): These integrations are foundational for tier-one stablecoin deployment, large scale DeFi growth, and acceleration of RWA and DePin activity, strengthening Cardano’s long term fee generation and treasury sustainability.
- finding: Claim (economic, independently_verifiable, low materiality): This project is being driven through close collaboration between Input | Output Global, the Cardano Foundation, and EMURGO, together with Midnight Foundation and Intersect, all of whom are actively engaged in negotiations with integration partners.
- finding: Claim (technical, independently_verifiable, medium materiality): Strategic Need Cardano has a strong technical and governance foundation, but lacks several critical integrations required for large-scale economic activity and external liquidity.
- finding: Claim (technical, independently_verifiable, low materiality): The absence of key systems, including stablecoin infrastructures, interoperability frameworks, and institutional-grade pricing oracle networks limits the ecosystem’s capacity to attract external capital, facilitate stable on-chain operations, and support ad...
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 70.00M ADA
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
- finding: Strongest YES: the proposal substantiates "This treasury withdrawal is submitted pursuant to the Budget Info Action “Cardano Critical Integrations Budget” (gov action13a2dqgwxum7d6kjfprcs57cf9733ek2dkt5qnuhqd4ll5ntcwu7sqluwkxd) and can only be ratified if that Budget Info Action is approved by DReps..." and clears the evidence gates.
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
- Treasury analysis: Requested ADA: 70.00M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "This treasury withdrawal is submitted pursuant to the Budget Info Action “Cardano Critical Integrations Budget” (gov action13a2dqgwxum7d6kjfprcs57cf9733ek2dkt5qnuhqd4ll5ntcwu7sqluwkxd) and can only be ratified if that Budget Info Action is approved by DReps..." and clears the evidence gates.
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
- input_hash: `b6f0f0c255e6388e544f13aaa71ccea792b8760dcda244acf8d8279b5222ced3`
- snapshot_bundle_hash: `3135e63a6890aa48db853e17665ced5c0e8208a079e028e961b4053fb18a3d0e`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `13`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5114, "NO": 0.4276, "YES": 0.061}`

