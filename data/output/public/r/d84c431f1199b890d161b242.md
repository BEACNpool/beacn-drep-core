# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#3
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline treasury field was missing: `treasury_amount_lovelace` was not available for this treasury withdrawal review. That makes this a conservative, evidence-based hold, not a judgment that the proposal is bad or that the work lacks value.

The action requested 1,193,000 ada for 12 months of Intersect Technical Steering Committee support, covering community-facing technical coordination, protocol governance and evolution work, and a pilot independent technical review programme launching in 2027. The proposal stated a budget split of 256,000 ada for WP 1, 832,000 ada for WP 2, and 105,000 ada for WP 3. It also claimed that unspent funds would be returned to the treasury, that execution depended on approval of the IntersectMBO budget proposal, and that Appold would provide audit and assurance support.

Some claims were supported or independently checkable, including the requested amount, the work-package budget split, references to Intersect budget-process voting results, the Net Change Limit claim, prior treasury funding disclosures, and use of Sundae Labs treasury management smart contracts. Other important claims remained too thin or unsupported for confidence, including independent evidence that all spending would be fully accounted for and unspent funds returned, the dependency on the IntersectMBO budget proposal, the sustainability path, cost-benefit clarity, independent assurance, and a rollback or remedy path.

The intake and synthesis gates were blocked by the missing `treasury_amount_lovelace` field, while claims and evidence were rated thin and execution risk was medium. A directional vote would need the missing treasury amount field, stronger independent evidence for spending controls and return of unused funds, clearer cost-benefit and sustainability information, independent assurance detail, and a defined remedy path if delivery does not happen as expected.

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
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee support activities for 12 months across community-facing technical coordination, protocol governance and evolution, and technical review.
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1: Community-Facing Technical Coordination, including expert attendance at major ecosystem events and commissioning technical reports., WP 2: Protocol Governance and Evolution, funding the Parameter Committee, CIP editors, and Hard Fork Working Group., WP 3: Technical Review, establishing a pilot independent technical review programme launching in 2027.
- finding: Deadline/expiry: 12 months; pilot independent technical review programme launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 1,193,000 ada, described as $298,250, to support Technical Steering Committee activities for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 256,000 ada for WP 1, 832,000 ada for WP 2, and 105,000 ada for WP 3.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- finding: Claim (governance, proposer_asserted, high materiality): Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal says it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting and audited results materials.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal says the requested amount does not breach the applicable 350M Net Change Limit at the time of submission and links to the relevant governance action.
- missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
- missing: Independent evidence for: The proposal claims the TSC work supports Cardano strategy pillars including uptime, DRep participation, governance capture resistance, ecosystem growth, and treasury stewardship.
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ada, described as $298,250, to support Technical Steering Committee activities for 12 months." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 1,193,000 ada, described as $298,250, to support Technical Steering Committee activities for 12 months." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: The proposal states that all expenditure will be fully accounted for and any unspent funds returned to the Cardano treasury.
- Claims and evidence missing: Independent evidence for: Execution of the work packages is contingent on approval of the IntersectMBO budget proposal.
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
- input_hash: `8253356434e3c24a65090be25a76a4edcf6604c24c946699ec94383cdc418bcf`
- snapshot_bundle_hash: `dd504f7fe14ce2f23117e3c847451bfeb5f52b41ca6c19b04f0267626721cebb`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

