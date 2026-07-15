# Rationale: d8de068952df50c862fa1bce9b8180d3387976cbae0fb2c3d9ef84f0faaf64d6#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (raw `-0.56` + doctrine-LLM nudge `+0.02`) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a public-benefit maintenance proposal for established open-source wallet infrastructure with concrete deliverables, acceptance criteria, public verification paths for key release metrics, and described oversight and disbursement controls. The positive nudge is small because several important adoption, track-record, and return-of-funds statements remain proposer-asserted, and treasury stewardship still requires caution on a large time-and-materials withdrawal.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the proposal.

The action asks for 1,785,333 ADA for Se7en Labs to maintain and improve Daedalus through 2026-2027, with Intersect administering milestone-based disbursements. The work includes ongoing protocol and release maintenance, hard fork readiness, platform and security support, signed releases, hardware wallet support, CIP-30 dApp connector work, Japanese localisation and support, general user support, and an architecture assessment.

Several important parts were supported well enough for review: the proposal anchor was pinned and replayable, the budget was broken down, Intersect’s administration and milestone role was described, and public GitHub repositories plus the Cardano mainnet chain can verify key release-timing and version-currency metrics. The strongest case for approval is that the proposal substantiates Se7en Labs’ recent Daedalus maintenance track record, including prior shipped work such as Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.

However, treasury withdrawals require elevated scrutiny. Some material claims remained unsupported or only proposer-asserted, including that Daedalus is Cardano’s only full-node desktop wallet, the monthly active user figure, the return of unspent funds, and recent treasury funding history. The review also found thin evidence status, missing sustainability and cost-benefit clarity, missing independent assurance, and no clear rollback or remedy path. To unblock a directional vote, BEACN would need the Net Change Limit pinned and independently verified from public chain evidence, plus stronger replayable evidence for the unsupported material claims and treasury-risk gaps.

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
- finding: Requested: Daedalus Wallet Maintenance and Improvements 2026-2027 delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. via Intersect administration and milestone-based disbursement
- finding: Stated amount: 1,785,333
- finding: Deliverables: Protocol maintenance including node and wallet backend updates, hard fork readiness, platform support, release engineering, dependency/security maintenance, and signed releases, Keystone and Flex hardware wallet support, plus newer hardware wallet models as they emerge during the contract period, CIP-30 dApp connector implementation within Daedalus with documentation and dApp interoperability verification, Japanese localisation and Japanese-language user support alongside general user support, Architecture assessment covering current state, options, resource estimates, and recommendation
- finding: Deadline/expiry: Contract year through 2026-2027; specific milestones include 52 weeks ongoing maintenance/support, 20 weeks CIP-30, 12 weeks hardware wallet support, 8 weeks architecture assessment, and architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (adoption, proposer_asserted, high materiality): Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be higher due to privacy-conscious users being less likely to opt in.
- finding: Claim (technical, supported_in_proposal, high materiality): Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal commits to providing a compatible stable Daedalus release at least two weeks before every mainnet hard fork during the contract period.
- finding: Claim (governance, independently_verifiable, medium materiality): All release-timing and version-currency success metrics are independently verifiable from public GitHub repositories and the Cardano mainnet chain without reliance on applicant self-reporting.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget totals 1,785,333 ADA, consisting of 1,666,667 ADA for labor, 33,333 ADA for test hardware, 33,333 ADA for financial audit, and a 52,000 ADA Intersect administration fee.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be higher due to privacy-conscious users being less likely to opt in.
- missing: Independent evidence for: Any unspent labor, hardware, or audit budget at contract close will be returned to the treasury.
- missing: Independent evidence for: Se7en Labs states it has not received ADA from the Cardano Treasury within the last 24 months and that its current Daedalus maintenance funding is through a direct IOG contract ending August 31, 2026.
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
- finding: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization." and clears the evidence gates.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and has shipped Mithril snapshot bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, the drt release CLI, and Nix build modernization." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a public-benefit maintenance proposal for established open-source wallet infrastructure with concrete deliverables, acceptance criteria, public verification paths for key release metrics, and described oversight and disbursement controls. The positive nudge is small because several important adoption, track-record, and return-of-funds statements remain proposer-asserted, and treasury stewardship still requires caution on a large time-and-materials withdrawal.
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
- Claims and evidence missing: Independent evidence for: Daedalus has approximately 4,000 monthly active users according to opt-in telemetry, with the true count asserted to be higher due to privacy-conscious users being less likely to opt in.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `5893f249bcc7833de90e73ccb4c8ffd33f8f6a9800b6dba2ec517aa3ffb0a6a5`
- snapshot_bundle_hash: `98274fc27b33ccc8063c8a5ea3edf701445feca88f68a3b7201d29ffcdd266c3`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

