# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (binding treasury composite; advisory raw signal `-0.56`; LLM lean `+0.0` recorded, not added) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit alignment for open-source wallet maintenance and include concrete deliverables, success metrics, oversight structure, and some independently verifiable checks, but major adoption, track-record, and cost-efficiency claims remain largely proposer-asserted within the document. Because the deterministic assessment is already ready and the doctrine says missing or incomplete diligence should not be converted into a directional penalty, no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not active opposition to the work.

The proposal asks for 1,785,333 ADA to fund Daedalus Wallet maintenance and improvements for 2026-2027, delivered by Se7en Labs through Intersect administration and milestone-based disbursement. The requested work includes protocol maintenance, hard fork readiness, release engineering, hardware wallet support, CIP-30 dApp connector work, Japanese localization and support, a public architecture assessment, test hardware, and an independent financial audit. The proposal gives a clear budget split and includes success metrics such as signed releases, release timing before hard forks, platform CI, security fixes, hardware wallet support, and a public architecture assessment.

Several claims were supported well enough inside the proposal, including the time-and-materials scope, the total budget, the milestone administration role for Intersect, and the stated success metrics. But important claims remained unsupported by independent replayable evidence, including that Daedalus is Cardano’s only full-node desktop wallet and that it derives wallet and governance data directly from the chain without third-party APIs or trusted backends. The claimed monthly active user figure of about 4,000 opt-in telemetry users also lacked independent evidence.

The review gates were strong enough to review the action: the pinned anchor document was available, the proposal anchor was replayable, and the counterargument pass found a credible YES case. But treasury scrutiny is higher because the action spends shared ADA. The hold would be unblocked by public, replayable evidence verifying the applicable Net Change Limit from chain data, plus stronger independent evidence for the key technical and adoption claims, and clearer support for sustainability, cost-benefit, independent assurance, and rollback or remedy paths.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 639
- finding: Expires after epoch: 646
- finding: Treasury request: 1.79M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. through Intersect administration and milestone-based disbursement
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including cardano-node/cardano-wallet integration, hard fork readiness, platform support, release engineering, dependency maintenance, and signed releases, Compatible Daedalus release at least 2 weeks before every mainnet hard fork during the contract period, Leios, Peras, and Nested Transactions readiness as protocol work progresses, Keystone and Flex hardware wallet support, plus newer hardware wallet models as they emerge, CIP-30 dApp connector implementation with documentation and dApp interoperability, User support across GitHub, community forums, and direct channels, including Japanese-language support, Full Japanese translation maintained across all shipped features, Architecture assessment published publicly with recommendation and rationale, Independent financial audit of funds received and expended, Test hardware acquisition and maintenance for release verification
- finding: Deadline/expiry: Contract year 2026-2027; architecture assessment by Q3 2027; IOG contract closes August 31, 2026
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting true usage is meaningfully higher.
- finding: Claim (technical, proposer_asserted, high materiality): Se7en Labs has maintained Daedalus under an IOG contract since January 2026 and shipped Mithril bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, release tooling, Nix build modernization, and Daedalus 8.0 and 11.0.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds a time-and-materials engagement covering maintenance, protocol compatibility, hardware wallet support, CIP-30, Japanese localization, user support, and an architecture assessment.
- finding: Claim (economic, supported_in_proposal, high materiality): The total requested budget is 1,785,333 ADA, consisting of 1,666,667 ADA for maintenance and improvements, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and 52,000 ADA for Intersect administration.
- finding: Claim (economic, proposer_asserted, medium materiality): Any unspent labor, hardware, or audit budget is to be returned to the treasury at contract close.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting true usage is meaningfully higher.
- missing: Independent evidence for: Se7en Labs has maintained Daedalus under an IOG contract since January 2026 and shipped Mithril bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, release tooling, Nix build modernization, and Daedalus 8.0 and 11.0.
- missing: Independent evidence for: Any unspent labor, hardware, or audit budget is to be returned to the treasury at contract close.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
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
- finding: Flag count: 1
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal funds a time-and-materials engagement covering maintenance, protocol compatibility, hardware wallet support, CIP-30, Japanese localization, user support, and an architecture assessment." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1785333
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal funds a time-and-materials engagement covering maintenance, protocol compatibility, hardware wallet support, CIP-30, Japanese localization, user support, and an architecture assessment." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Proposal clears individual quality floors but is not currently portfolio-eligible: insufficient remaining NCL capacity after higher-ranked proposals.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the proposer asserting true usage is meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `e09131211319db9e2b0874295e2d58fe5ed1a01e81d4fe7a6acbfae150dfee7e`
- snapshot_bundle_hash: `8f7eaf89ae259047f2704b819d5ae80a539bbe91ae3c1aea16db75b269d8dbae`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `05bc17eb7f8c498b4adfa70bbeda8dcd97978738`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

