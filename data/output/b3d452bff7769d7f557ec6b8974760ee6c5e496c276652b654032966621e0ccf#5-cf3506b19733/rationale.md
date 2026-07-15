# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (binding treasury composite; advisory raw signal `-0.08`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): The extracted claims show strong alignment with protocol infrastructure, decentralization, and public-benefit growth, and the document provides checkable references for governance process, NCL compliance, smart contracts, audits, and dashboards. However, the core technical and adoption benefits are mostly proposer-asserted in the anchor text, and the deterministic assessment is already ready, so no additional nudge beyond the mechanical score is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Mithril or of the requested work.

The action requests 3,810,423 ada for Mithril Protocol continuous development through Intersect on behalf of Teragone. The proposal breaks that into 3,699,440 ada for development and 110,983 ada for Intersect budget administration, with oversight through Intersect and technically capable third parties, milestone-based disbursement controls, and use of treasury management smart contracts. Those funding and governance-process claims were supported in the proposal, and several Intersect process and treasury-management claims were described as independently verifiable.

The review found the evidence record too thin for a YES or NO. Important technical claims, including that Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way and helps with slow full-node synchronization and centralized-trust reliance by light clients, were still treated as proposer assertions rather than independently evidenced claims. The review also noted missing treasury and risk evidence: a line-item budget, a sustainability path, independent assurance, and a rollback or remedy path.

A directional vote would be unblocked by pinned, replayable public evidence verifying the Net Change Limit from chain data, plus stronger independent evidence for the material technical claims and the missing treasury and risk controls. Until then, BEACN’s position is to hold rather than overstate certainty on a large treasury withdrawal.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 3.81M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continuous development through Intersect on behalf of the vendor.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, with project-specific management by Intersect and the vendor Teragone identified in the text.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Audit and oversight through Intersect and technically capable third parties, Milestone-based disbursement controls using Intersect treasury management smart contracts
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for an Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid state verification without relying on the entire chain.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril is presented as addressing slow full-node synchronization and centralized-trust reliance by light clients.
- finding: Claim (governance, proposer_asserted, high materiality): The proposal states that funding Mithril through Intersect ensures continuity and long-term sustainability as development transitions from IOG-funded work to a community-governed funding model.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides voting and audit references.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states that the requested withdrawal does not breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 at the time of submission and links to the governance action for that limit.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid state verification without relying on the entire chain.
- missing: Independent evidence for: Mithril is presented as addressing slow full-node synchronization and centralized-trust reliance by light clients.
- missing: Independent evidence for: The proposal states that funding Mithril through Intersect ensures continuity and long-term sustainability as development transitions from IOG-funded work to a community-governed funding model.
- missing: Independent evidence for: The proposal states that Teragone has not previously received direct funding from Cardano treasury or community governance programs but has worked on Mithril for several years through IOG-funded collaboration.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 3810423
- finding: Budget granularity: not confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.45
- missing: line-item budget
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
- finding: Rollback/remedy path: unknown
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for an Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid state verification without relying on the entire chain." — so cost or precedent may outweigh the benefit.
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
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 3810423
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for an Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Treasury evidence is not sufficient for YES and does not affirmatively prove waste; requesting the missing evidence instead of defaulting to NO.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling rapid state verification without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: Mithril is presented as addressing slow full-node synchronization and centralized-trust reliance by light clients.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `cf3506b1973390ec0133fe0b6d550c3a18acbc7676135bdec119967116c69880`
- snapshot_bundle_hash: `db885eac0b2fe3a34ea831abe0d230f334b5547638320e838013075d6394d6fc`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

