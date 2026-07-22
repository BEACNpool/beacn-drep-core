# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (binding treasury composite; advisory raw signal `-0.56`; LLM lean `+0.0` recorded, not added) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show a narrower scope, reduced budget, excluded high-risk items, and plausible public-infrastructure alignment, while key adoption, delivery-history, and governance-assurance claims remain mostly proposer asserted in the supplied text. The deterministic assessment is already ready, so the evidence mix does not justify an additional directional nudge.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal and the applicable Net Change Limit was not pinned and independently verified from public chain evidence. That blocks a directional treasury vote, even though parts of the proposal are reviewable and some technical claims were supported.

The action requests funding for 9 months of Scalus 2026 work by Lantr Engineering: maintenance of the existing Scalus stack, Dijkstra hard-fork readiness, interoperability improvements, and a scoped application runtime. The proposal asks for ₳2,464,844 and says this is a reduced resubmission from a larger prior request. It also states that Scalus is an open-source, JVM-native Cardano development platform built over three years, and that claim was treated as well-supported. Independent adoption signals were also present, including 4,642 commits, 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads.

Other important claims were not independently verified. The review lacked independent evidence that Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit. It also lacked independent evidence for the claimed milestone-based delivery structure using audited SundaeSwap treasury contracts, an oversight board, and third-party assurance. The treasury review also remained thin on sustainability path, independent assurance, and dependency mapping, with medium execution risk noted.

This is a conservative, evidence-based hold, not a rejection of the work. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus replayable public evidence for the major adoption and governance-assurance claims that currently remain unsupported.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: 2.46M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Scalus 2026 maintenance, Dijkstra hard-fork readiness, interoperability, and a scoped application runtime over 9 months
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance of the existing Scalus stack and supported export targets, Dijkstra readiness including Plutus V4 support, ledger rules, transaction-builder updates, conformance testing, nested transactions, accounts, guard scripts, and cost models, Improved JS/TS component interfaces and documentation for MeshJS, Evolution SDK, and Lucid Evolution reuse, Java/Kotlin interoperability with Spring Boot and Ktor examples and cleaner integration with Cardano Client Lib and Yaci, Scoped application runtime components including foundational reactive workers, chain follower, task scheduler, backend workflow support, and validation through reference applications, integration tests, and early-user feedback
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an open-source, JVM-native Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 for a 9-month continuation at a $0.16/ADA reference rate with no contingency.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, independently_verifiable, high materiality): Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js receives more than 20,000 downloads per month.
- finding: Claim (technical, supported_in_proposal, high materiality): The funded scope excludes a standalone L1 node, full Gummiworm L2 integration, broad formal verification, and advanced devnet expansion.
- finding: Claim (economic, supported_in_proposal, high materiality): This resubmission reduces the prior proposal from ₳8.503 million over 12 months to about ₳2.465 million over 9 months, and reduces FTE-months from 99 to 20.25.
- missing: Independent evidence for: Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Delivery is milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- missing: Independent evidence for: Lantr Engineering says every prior Scalus milestone was delivered on time and commits to public reporting and open community sessions for treasury-funded work.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.82
- missing: sustainability path
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: medium
- finding: Technical risk: medium
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 1
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Scalus is an open-source, JVM-native Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Scalus is an open-source, JVM-native Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence missing: Independent evidence for: Delivery is milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `e02e652b93a20753af84cc9f97f42d2cb218a22d337a4711115bb46e0e2302ec`
- snapshot_bundle_hash: `cbf3f5ddb33e3a4679a794d94600da1d66ef3963365cc3ea8f642fa970bde540`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `9e6d7de921490a42032dbcf21a53abc34f881376`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

