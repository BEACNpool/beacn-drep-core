# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8svfsvefn
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8333` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit developer tooling and some verifiable references, but the deterministic assessment is blocked by missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under a treasury withdrawal, that evidence gap matters more than the asserted ecosystem value, so a small cautionary negative adjustment is warranted without overriding the engine's hard blockers.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 1,162,746 ada for MLabs Core Tool Maintenance & Enhancement: Plutarc.... The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Annual funding for maintenance and enhancement of MLabs Core Tool Maintenance & Enhancement: Plutarch and Ply.. The recorded treasury amount is 1,162,746. The strongest grounded claim is: Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.

A material weak point is that this claim remains proposer-asserted or thinly supported: MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale section says it conservatively counted at least 15 teams. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

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
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Annual funding for maintenance and enhancement of MLabs Core Tool Maintenance & Enhancement: Plutarch and Ply.
- finding: Recipient: Treasury withdrawal reward address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v; vendor described as MLabs and submitter as Intersect on behalf of the vendor.
- finding: Stated amount: 1,162,746
- finding: Deliverables: WP1 - Plutarch and Ply Maintenance, Compatibility & Developer Experience, Critical breakages and serious vulnerabilities, Protocol-era and hard-fork compatibility, Bug fixes, correctness improvements, and optimizations, Documentation, examples, technical blog posts, and developer-experience improvements
- finding: Deadline/expiry: annual funding period; specific deadline not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types.
- finding: Claim (adoption, proposer_asserted, high materiality): MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale section says it conservatively counted at least 15 teams.
- finding: Claim (technical, independently_verifiable, medium materiality): Plutarch scripts rank among the smallest in MLabs' public cross-language benchmark suite while requiring comparatively low on-chain compute and memory.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal prioritizes resources first to critical breakages and serious vulnerabilities, then protocol-era and hard-fork compatibility, then bug fixes, correctness improvements, optimizations, documentation, examples, technical blog posts, and developer-experience improvements.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says the requested 1,162,746 ADA consists of 1,128,880 ADA for Plutarch and Ply maintenance, compatibility, and developer experience, plus a 33,866 ADA Intersect budget administration fee.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and was advanced for on-chain Treasury Withdrawal submission under the approved Budget Process Framework.
- missing: Independent evidence for: MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale section says it conservatively counted at least 15 teams.
- missing: Independent evidence for: Audit, oversight, reporting obligations, and milestone-based disbursement controls are described as being handled through Intersect, technically capable third parties, and Intersect's administration fee.
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1.16M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale section says it conservatively counted at least 15 teams." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1.16M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Plutarch is a Haskell eDSL for creating efficient Cardano smart contracts through controlled compilation into UPLC, and Ply serializes Plutarch scripts to and from CIP-57 blueprint-style artifacts with inferred types." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show plausible public-benefit developer tooling and some verifiable references, but the deterministic assessment is blocked by missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under a treasury withdrawal, that evidence gap matters more than the asserted ecosystem value, so a small cautionary negative adjustment is warranted without overriding the engine's hard blockers.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~18 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: MLabs counted at least 26 teams building with Plutarch and Ply in a recent internal audit, while the rationale section says it conservatively counted at least 15 teams.
- Claims and evidence missing: Independent evidence for: Audit, oversight, reporting obligations, and milestone-based disbursement controls are described as being handled through Intersect, technically capable third parties, and Intersect's administration fee.
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `3a93616211481cd7aaf1ac07acefda67466b569cdf8da9d9abf1b87e9a110976`
- snapshot_bundle_hash: `110a9bb782f9fa3e7a38dd61564bc8de72967ba624ab682848f346aa07f84838`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `659`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1914, "NO": 0.7642, "YES": 0.0443}`

