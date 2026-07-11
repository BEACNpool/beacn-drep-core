# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sgx6wlxf
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims include specific budget work packages, public voting and NCL references, prior-funding disclosure, external assurance, and smart-contract custody controls, which improve evidence quality and treasury accountability beyond bare assertions. The nudge remains small because several high-materiality operational performance claims are still proposer-asserted within the document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a large Treasury withdrawal and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests 25,400,000 ada for Intersect’s June 2026 to June 2027 work: governance coordination, technical stewardship, incident response, release coordination, critical process management, milestone-based drawdowns, reporting, disclosures, and external assurance. It breaks the budget into 6,000,000 ada for operations and ecosystem coordination, 18,800,000 ada for technical stewardship and incident response, and 600,000 ada for critical process management.

Several parts were well-supported in the review. The anchor document was available, pinned, and replayable. The proposal provided specific work packages, disclosed 22,385,000 ada in prior Treasury withdrawals to Intersect and its committees, referenced the 2026 Intersect Budget Process Hydra Voting result, described Appold assurance, and gave treasury smart-contract custody details with public tracking. But some important claims remained too thin or only proposer-asserted, including Intersect’s operational maturity over two years, the claimed reduction from last year’s ask while preserving critical functions, sustainability path, cost-benefit clarity, execution risk, independent assurance status, and rollback or remedy path.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by independently verified public-chain evidence that the withdrawal fits within the applicable 350M Net Change Limit, plus stronger independent support for the material operational and economic claims that are currently only asserted or incomplete.

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
- finding: Requested: Treasury withdrawal for Intersect governance coordination, technical stewardship, incident response, release coordination, and critical process management for June 2026 to June 2027.
- finding: Recipient: Intersect / 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v
- finding: Stated amount: 25,400,000
- finding: Deliverables: WP 1 - Intersect operations and ecosystem coordination: 6,000,000 ADA, WP 2 - Technical Stewardship, Incident Response & Coordination including core Cardano repos: 18,800,000 ADA, WP 3 - Management of critical processes: 600,000 ADA, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance process
- finding: Deadline/expiry: June 2026 to June 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Intersect states the withdrawal funds its core operating model for June 2026 to June 2027, including governance coordination, reserved critical-process capacity, technical stewardship, incident response, and release coordination.
- finding: Claim (adoption, proposer_asserted, medium materiality): The proposal says Intersect has matured over two years into a focused operational layer that supports committees and working groups, stewards core Haskell repositories, coordinates upgrades and incident response, and administers community-approved initiatives.
- finding: Claim (economic, proposer_asserted, high materiality): Intersect states the current ask is reduced from last year's $7.875M to $6.35M while preserving the functions most critical to Cardano continuity and maturity.
- finding: Claim (technical, proposer_asserted, high materiality): Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to the voting proposal, documentation, final audited results, and audit report.
- finding: Claim (economic, independently_verifiable, high materiality): The proposal states the requested amount does not breach the applicable 350M Net Change Limit for Epoch 613 to Epoch 713 at the moment of submission and links to the relevant governance action.
- missing: Independent evidence for: The proposal says Intersect has matured over two years into a focused operational layer that supports committees and working groups, stewards core Haskell repositories, coordinates upgrades and incident response, and administers community-approved initiatives.
- missing: Independent evidence for: Intersect states the current ask is reduced from last year's $7.875M to $6.35M while preserving the functions most critical to Cardano continuity and maturity.
- missing: Independent evidence for: Intersect claims it has coordinated two network upgrades, is preparing for a third, and led ecosystem coordination during the November 2025 chain partition incident.
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
- finding: Strongest YES: the proposal substantiates "Intersect states the withdrawal funds its core operating model for June 2026 to June 2027, including governance coordination, reserved critical-process capacity, technical stewardship, incident response, and release coordination." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal says Intersect has matured over two years into a focused operational layer that supports committees and working groups, stewards core Haskell repositories, coordinates upgrades and incident response, and administers community-approved initiatives." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect states the withdrawal funds its core operating model for June 2026 to June 2027, including governance coordination, reserved critical-process capacity, technical stewardship, incident response, and release coordination." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims include specific budget work packages, public voting and NCL references, prior-funding disclosure, external assurance, and smart-contract custody controls, which improve evidence quality and treasury accountability beyond bare assertions. The nudge remains small because several high-materiality operational performance claims are still proposer-asserted within the document.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal says Intersect has matured over two years into a focused operational layer that supports committees and working groups, stewards core Haskell repositories, coordinates upgrades and incident response, and administers community-approved initiatives.
- Claims and evidence missing: Independent evidence for: Intersect states the current ask is reduced from last year's $7.875M to $6.35M while preserving the functions most critical to Cardano continuity and maturity.
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
- snapshot_bundle_hash: `bb6f2c1d0561528a7892a146f665776bd4c96fe372dcb4911505fedc163a6b9e`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

