# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sxypfkyr
Recommendation: **NO**
Score: `-0.3133` (raw `-0.2833` + doctrine-LLM nudge `-0.03`) | Confidence: `0.8333` | Readiness: `0.0`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit governance infrastructure and some independently verifiable process references, but the deterministic assessment is blocked for missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, a treasury withdrawal with high material spend and incomplete diligence should receive a cautious negative nudge rather than credit for asserted ecosystem benefits.

## Plain-language explanation (codex-offline-review)
BEACN records NO on Withdraw 1,193,000 ada for Intersect Technical Steering Committee Support. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Treasury withdrawal to fund Intersect Technical Steering Committee Support activities for 12 months across community engagement, protocol governance, and independent technical review.. The recorded treasury amount is 1,193,000. The strongest grounded claim is: Intersect requests $298,250, stated as 1,193,000 ADA, for 12 months of Technical Steering Committee support.

A material weak point is that this claim remains proposer-asserted or thinly supported: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment. The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.19M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Intersect Technical Steering Committee Support activities for 12 months across community engagement, protocol governance, and independent technical review.
- finding: Recipient: Intersect 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1,193,000
- finding: Deliverables: WP 1 — Community-Facing Technical Coordination: attendance of technical experts at major ecosystem events and commissioning technical reports, WP 2 — Protocol Governance and Evolution: support for the Parameter Committee, CIP editors, and Hard Fork Working Group, WP 3 — Technical Review: establishment of a pilot independent technical review programme launching in 2027, Milestone-based drawdowns, evidence-backed reporting, transparent disclosures, and external assurance, Return of any unspent funds to the Cardano treasury
- finding: Deadline/expiry: 12 months; WP3 pilot launching in 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Intersect requests $298,250, stated as 1,193,000 ADA, for 12 months of Technical Steering Committee support.
- finding: Claim (economic, supported_in_proposal, high materiality): The budget is allocated as 256,000 ADA for WP1, 832,000 ADA for WP2, and 105,000 ADA for WP3, totaling 1,193,000 ADA.
- finding: Claim (technical, supported_in_proposal, medium materiality): WP1 funds expert attendance at major ecosystem events and commissioning technical reports on topics including throughput, finality, governance, quantum resistance, economic utility, and partner chains.
- finding: Claim (technical, supported_in_proposal, high materiality): WP2 funds the Parameter Committee, CIP editors, and Hard Fork Working Group to support protocol settings advice, improvement pipeline maintenance, and safe protocol upgrade coordination.
- finding: Claim (governance, supported_in_proposal, high materiality): WP3 funds a pilot independent technical review programme launching in 2027 with conflict-of-interest provisions, published recusals, and open reviewer selection against documented criteria.
- finding: Claim (economic, supported_in_proposal, medium materiality): The proposal states that technical workshops, the Security Council, and the Bug Bounty Programme are funded separately through the main Intersect budget and are not included in this request.
- missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment.
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
- finding: Requested ADA: 1.19M ADA
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
- finding: Strongest YES: the proposal substantiates "Intersect requests $298,250, stated as 1,193,000 ADA, for 12 months of Technical Steering Committee support." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1.19M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Intersect requests $298,250, stated as 1,193,000 ADA, for 12 months of Technical Steering Committee support." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The extracted claims show plausible public-benefit governance infrastructure and some independently verifiable process references, but the deterministic assessment is blocked for missing budget, feasibility, risk, alternatives, and failure-mode analysis. Under BEACN's hierarchy, a treasury withdrawal with high material spend and incomplete diligence should receive a cautious negative nudge rather than credit for asserted ecosystem benefits.
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
- Claims and evidence missing: Independent evidence for: Independent audits and assurance for this proposal will be provided by Appold, with possible reviews including deliverable verification, control testing, spend validation, and milestone evidence assessment.
- Claims and evidence missing: complete proposal summary
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
- input_hash: `7b17b37064a3503b773e69143157520109d21d956cba64b30ab336a8e7e9e413`
- snapshot_bundle_hash: `eea2ddcef3edada09c3f74f33a7e8b3dd8698438e86766858646873aeff58806`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `568`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1914, "NO": 0.7642, "YES": 0.0443}`

