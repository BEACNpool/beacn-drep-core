# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline field was missing: the review could not confirm `treasury_amount_lovelace` for a treasury withdrawal. For a vote that would spend shared Cardano treasury funds, BEACN treats that as a blocking evidence problem, not a minor formatting issue.

The proposal requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support, split across community-facing technical coordination, protocol governance and evolution, and a pilot independent technical review programme. The proposal supported several core claims, including the stated budget split of 256,000 ada for WP1, 832,000 ada for WP2, and 105,000 ada for WP3. It also had independently verifiable support that the action passed the required 67% threshold in the 2026 Intersect Budget Process Hydra Voting phase, that the withdrawal did not breach the applicable Net Change Limit at submission, and that funds would be administered through specified treasury smart-contract arrangements.

However, several important claims were still unsupported or thinly evidenced. BEACN did not have independent evidence that all spending would be fully accounted for and that unspent funds would be returned to the treasury. The broader claim that the TSC work would support Cardano’s technical governance infrastructure, protocol evolution, DRep decision-making, and ecosystem resilience was also proposer-asserted rather than independently supported. The treasury analysis was missing a sustainability path and cost-benefit clarity, and the risk review was missing independent assurance and a rollback or remedy path.

This ABSTAIN is therefore a conservative, evidence-based hold. A directional vote would require the missing `treasury_amount_lovelace` baseline field to be supplied, along with stronger independent evidence for expenditure accounting, return of unspent funds, sustainability, cost-benefit clarity, independent assurance, and remedies if delivery problems occur.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee Support for 12 months across community engagement, protocol governance, and independent technical review activities.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination for 256,000 ADA, including attendance of technical experts at major ecosystem events and commissioning technical reports., WP 2: Protocol Governance and Evolution for 832,000 ADA, funding the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review for 105,000 ADA, establishing a pilot independent technical review programme launching in 2027., Full expenditure accounting, return of unspent funds to the Cardano treasury, milestone-based drawdowns, evidence-backed reporting, and transparent disclosures.
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect's TSC requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal breaks the 1,193,000 ADA budget into WP1 at 256,000 ADA, WP2 at 832,000 ADA, and WP3 at 105,000 ADA.
- finding: Claim (economic, proposer_asserted, high materiality): All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain submission under the approved Budget Process Framework.
- finding: Claim (economic, independently_verifiable, high materiality): The requested withdrawal does not, at submission, breach the applicable 350M Net Change Limit covering Epoch 613 to Epoch 713.
- missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- missing: Independent evidence for: The TSC's work is claimed to support Cardano's technical governance infrastructure, protocol evolution, DRep decision-making, and ecosystem resilience across all five stated strategic pillars.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.72
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: high
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Intersect's TSC requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect's TSC requests $298,250, stated as 1,193,000 ADA, to support TSC activities for 12 months." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: All expenditure will be fully accounted for and any unspent funds will be returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: The TSC's work is claimed to support Cardano's technical governance infrastructure, protocol evolution, DRep decision-making, and ecosystem resilience across all five stated strategic pillars.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `d371613a9116e36c06997e047da8e05b718c862ceff25ce5bf0428bb79a37d99`
- snapshot_bundle_hash: `ba0e8097507e32146241f16ab5d3d7176a5cd813b82f85add9c5dc266c58fc23`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

