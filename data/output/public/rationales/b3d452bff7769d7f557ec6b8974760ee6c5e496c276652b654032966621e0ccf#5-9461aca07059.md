# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **NEEDS_MORE_INFO**
Score: `0.209` (raw `-0.53` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7722` | Readiness: `0.75`
> Reasoning layer (precomputed): The supplied claims show strong governance-process documentation, on-chain administration details, and independently checkable references for the budget vote, NCL compliance, and treasury-contract controls, while several core benefit and adoption claims remain mostly proposer-asserted. The deterministic assessment is already ready, so the evidence mix does not justify an additional positive or negative nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The action requests 3,810,423 ada for Mithril Protocol continuous development through Intersect, paid first to the 2026 Treasury Reserve Smart Contract stake address. The proposal breaks that into 3,699,440 ada for development and 110,983 ada for the Intersect budget administration fee. It also describes audit, oversight, reporting obligations, and milestone-based disbursement controls, though no deadline was stated.

Several governance and budget-process claims were well supported or independently verifiable: the pinned anchor document was available, the requested amount was clear, the proposal cited the 67% Intersect Budget Process Hydra Voting threshold, and it described the TRSC/PSSC treasury administration framework, oversight roles, reporting, and staged disbursement process. But important technical benefit claims remained only proposer assertions, including that Mithril solves the cost and complexity of securely verifying Cardano state and enables rapid trustless verification without relying on the full chain, centralized indexers, or hosted APIs.

This is a conservative, evidence-based hold, not a rejection of Mithril. A directional vote would be unblocked by pinned, independently verifiable public chain evidence for the applicable Net Change Limit, stronger independent evidence for the core technical claims, and clearer treasury-risk materials such as a line-item budget, sustainability path, independent assurance, and rollback or remedy path.

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
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continuous development through Intersect on behalf of the vendor
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 3810423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit, oversight, reporting obligations, and milestone-based disbursement controls
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state through stake-based threshold multi-signatures.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims Mithril enables rapid trustless state verification without relying on the entire chain, centralized indexers, or hosted APIs.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal claims faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, monitoring, bridges, full wallets, light wallets, and light clients.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting records, documentation, final audited results, and an audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested amount did not breach the applicable 350M Net Change Limit at submission, either alone or in aggregate, and links to the relevant governance action.
- missing: Independent evidence for: Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state through stake-based threshold multi-signatures.
- missing: Independent evidence for: The proposal claims Mithril enables rapid trustless state verification without relying on the entire chain, centralized indexers, or hosted APIs.
- missing: Independent evidence for: The proposal claims faster sync times lower onboarding friction and unlock tooling for exchanges, wallets, monitoring, bridges, full wallets, light wallets, and light clients.
- missing: Independent evidence for: The proposal states Teragone has not previously received direct funding from Cardano treasury or community governance programs, while IOG has funded its Mithril work to date.
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state through stake-based threshold multi-signatures." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 3,810,423 ada, consisting of 3,699,440 ada for Mithril Protocol Continuous Development and 110,983 ada for the Intersect Budget Administration fee." and clears the evidence gates.
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
- Proposal requests over 50% of rolling available capacity.
- Claims and evidence missing: Independent evidence for: Mithril is presented as solving the cost and complexity of securely accessing and verifying Cardano blockchain state through stake-based threshold multi-signatures.
- Claims and evidence missing: Independent evidence for: The proposal claims Mithril enables rapid trustless state verification without relying on the entire chain, centralized indexers, or hosted APIs.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `9461aca070597212ed37730f08cda903b38f3e3ad533d0c094bf2d4d8d7fb43d`
- snapshot_bundle_hash: `8e9f104b542fee37852f0bb82f7b68354d0d91f604ed10c18154f6d1498fdf36`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `fcde47763a7f055ead02e3e3a1dac917f51a9a68`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5052, "NO": 0.0492, "YES": 0.4456}`

