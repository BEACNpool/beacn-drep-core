# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8svfsvefn
Recommendation: **NO**
Score: `-0.2833` (raw `-0.2533` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7908` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal is aligned with public-benefit ecosystem growth and includes checkable governance, NCL, contract-management, and benchmark references, but several high-materiality claims remain proposer-asserted, including the adoption audit, oversight execution, milestone controls, and the need for a large annual maintenance budget. Given BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than rewarding spending on partially asserted evidence.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large Treasury withdrawal request and the evidence did not meet the higher bar needed for spending shared ada. The proposal had a pinned, reviewable anchor and made a credible case that Plutarch and Ply are real Cardano developer tools, but several material claims behind the budget remained asserted rather than independently supported.

The action requested 1,162,746 ada for one year of MLabs Plutarch and Ply maintenance and enhancement, administered through the 2026 Treasury Reserve Smart Contract with Intersect oversight. The proposal said the work would cover critical breakages, serious vulnerabilities, protocol-era and hard-fork compatibility, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements. It also stated that the budget included 1,128,880 ada for the work and a 33,866 ada Intersect administration fee.

The review found several claims were well-supported: the basic technical description of Plutarch and Ply, the work-priority ordering, the budget breakdown, the Net Change Limit compliance, Intersect’s contract-management structure, and the proposal’s passage through the required Intersect Budget Process support threshold. However, the review did not find independent evidence for the claimed number of teams using Plutarch and Ply, for the scope of future protocol-era compatibility work, for the sustainability path, for clear cost-benefit justification, for independent assurance, or for a rollback or remedy path.

Because Treasury withdrawals require elevated scrutiny, those gaps mattered. BEACN’s review recognized the strongest YES case: these tools have substantiated technical value and the proposal cleared several governance and evidence gates. But the strongest NO case was stronger: a large annual maintenance budget relied on material unsupported claims, while the broader treasury-flow signal was already in an unsustainable regime. On that basis, BEACN voted NO.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.16M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Annual funding for maintenance and enhancement of MLabs' Plutarch and Ply tooling, including compatibility, bug fixes, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, administered by Intersect for the vendor MLabs
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale separately states a conservative count of at least 15 teams.
- finding: Claim (technical, independently_verifiable, medium materiality): Plutarch scripts rank among the smallest in MLabs' public cross-language benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, proposer_asserted, high materiality): The funding period is expected to cover Cardano ledger, Plutus, and tooling evolution, including protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal prioritizes resources first toward critical breakages and serious vulnerabilities, then protocol-era and hard-fork compatibility, then bug fixes, correctness improvements, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- missing: Independent evidence for: MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale separately states a conservative count of at least 15 teams.
- missing: Independent evidence for: The funding period is expected to cover Cardano ledger, Plutus, and tooling evolution, including protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land.
- missing: Independent evidence for: Audit and oversight costs are included in the proposal overhead, and independent oversight will be provided through Intersect and technically capable third parties with reporting obligations and milestone-based disbursement controls.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1162746
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: medium
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
- finding: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale separately states a conservative count of at least 15 teams." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1162746
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts via controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal is aligned with public-benefit ecosystem growth and includes checkable governance, NCL, contract-management, and benchmark references, but several high-materiality claims remain proposer-asserted, including the adoption audit, oversight execution, milestone controls, and the need for a large annual maintenance budget. Given BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary negative nudge rather than rewarding spending on partially asserted evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale separately states a conservative count of at least 15 teams.
- Claims and evidence missing: Independent evidence for: The funding period is expected to cover Cardano ledger, Plutus, and tooling evolution, including protocol-era compatibility for major ledger updates such as the Dijkstra era if relevant changes land.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `7e682f1542af0634a13177d06faf46c116a6bcaded56f32de46e51ae4a61e1c5`
- snapshot_bundle_hash: `7af8f1478ab18ff0b81335fb1d540ed94b45449bad31f5929755249ba024757c`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3f0094e6cf1d57b2aad31917fe6d7e8bf8f66c7c`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2025, "NO": 0.7517, "YES": 0.0458}`

