# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sgx6wlxf
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims include meaningful governance and treasury controls, external references, prior-funding disclosure, and on-chain management details, but the large spend and several central performance claims remain mostly proposer-asserted within the document. The deterministic assessment already captured readiness and treasury analysis, so no additional bounded nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Intersect’s work or the proposal’s goals.

The action requests 25,400,000 ada for Intersect from June 2026 to June 2027, covering governance coordination, ecosystem coordination, technical stewardship, incident response, release coordination, and management of critical unowned processes. The proposal describes three work packages: 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for critical process management. It also proposes milestone-based drawdowns, evidence-backed reporting, transparent disclosures, Appold assurance, and use of Sundae Labs treasury smart contract controls.

Several important claims were supported or independently verifiable in the review. The basic request amount and operating period were substantiated. The proposal provided a pinned, replayable anchor document, disclosed prior treasury funding, referenced Hydra voting support and audited results, described Sundae Labs TRSC and PSSC controls, and provided a public dashboard for tracking. However, some material claims remained unsupported or thinly evidenced, including the claim that Intersect’s overall ask decreased from $7.875 million last year to $6.35 million this year while preserving critical functions, and the broader claims about Intersect’s support for committees, working groups, core repository stewardship, upgrades, incident response, and initiative administration.

The review gates reflected the higher bar for treasury withdrawals. Intake and source anchoring passed, and the strongest YES case was that the request itself is clear and evidence gates were partly cleared. But treasury analysis still lacked a sustainability path and cost-benefit clarity, risk review still lacked independent assurance and a rollback or remedy path, and execution risk was unknown. The evidence that would unblock a directional vote is independently pinned public-chain verification of the applicable Net Change Limit, plus stronger replayable evidence for the unsupported cost, delivery, assurance, and risk controls.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 25.40M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Intersect governance coordination, ecosystem coordination, technical stewardship, incident response, release coordination, and management of critical unowned processes for June 2026 to June 2027.
- finding: Recipient: Intersect via the 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v.
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination including core Cardano repositories: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance by Appold, Use of Sundae Labs treasury management smart contract framework with TRSC and PSSC controls
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests 25,400,000 ADA for its core operating model from June 2026 to June 2027.
- finding: Claim (economic, proposer_asserted, medium materiality): The proposal says Intersect's overall ask has decreased from $7.875M last year to $6.35M this year while preserving critical functions.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect says it supports Cardano through committees and working groups, core Haskell repository stewardship, upgrades, incident response, and community-approved initiative administration.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has already coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting documentation and audited results.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states the withdrawal does not breach the applicable 350M ADA Net Change Limit for Epoch 613 to Epoch 713 at the time of submission and links to the relevant governance action.
- missing: Independent evidence for: The proposal says Intersect's overall ask has decreased from $7.875M last year to $6.35M this year while preserving critical functions.
- missing: Independent evidence for: Intersect says it supports Cardano through committees and working groups, core Haskell repository stewardship, upgrades, incident response, and community-approved initiative administration.
- missing: Independent evidence for: Intersect claims it has already coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews of deliverables, controls, spend validation, and milestone evidence.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 25400000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.64
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
- finding: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model from June 2026 to June 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says Intersect's overall ask has decreased from $7.875M last year to $6.35M this year while preserving critical functions." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 25400000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests 25,400,000 ADA for its core operating model from June 2026 to June 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal says Intersect's overall ask has decreased from $7.875M last year to $6.35M this year while preserving critical functions.
- Claims and evidence missing: Independent evidence for: Intersect says it supports Cardano through committees and working groups, core Haskell repository stewardship, upgrades, incident response, and community-approved initiative administration.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `9e4a8741137d9f68ac94bfca2535f44c5f39eb762956956e62c86f683c6e5f12`
- snapshot_bundle_hash: `574eab7d040219727f8ab1861a4bf8d31627b4175d154f89a50e38ea8a3be928`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

