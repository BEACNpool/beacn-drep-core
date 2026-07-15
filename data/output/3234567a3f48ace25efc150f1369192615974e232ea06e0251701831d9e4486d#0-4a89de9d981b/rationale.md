# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **YES**
Score: `0.2615` (binding treasury composite; advisory raw signal `-0.11`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7854` | Readiness: `0.85`
> Reasoning layer (precomputed): The supplied claims show plausible public-benefit infrastructure, reduced scope, and stated oversight, but the main adoption, prior-delivery, and governance assurances remain mostly proposer-stated or only externally checkable rather than verified within the supplied material; the deterministic treasury and evidence gates are better suited to handle those issues, so no additional nudge is justified.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Scalus 2026: Maintenance, Dijkstra Readiness, Interoperability & Application Runtime. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS, and a scoped application runtime. It asks the treasury for 2464844 ADA. The strongest grounded claim is: The proposal asks for ₳2,464,844 over 9 months, approximately $394,375 at a $0.16/ADA reference rate, with no contingency.

A residual watch item: this claim remains proposer-asserted rather than independently shown: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.

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
- finding: Requested: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview with initial Plutus V4 support in the compiler and standard library, Updates for Dijkstra ledger rules, transaction building, cost models, nested transactions, accounts, guard scripts, and conformance testing, Improved JS/TS interfaces and documentation for components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin integration examples and cleaner integration paths with Cardano Client Lib and Yaci, Foundational runtime components including reactive workers, a chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,464,844 over 9 months, approximately $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The current proposal is a reduced resubmission from a prior ₳8.503M, 12-month proposal, with FTE reduced from 8.25 to 2.25 and the standalone L1 node, full L2 integration, and broad formal verification removed from scope.
- finding: Claim (adoption, independently_verifiable, high materiality): Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- finding: Claim (adoption, independently_verifiable, high materiality): Protocols and applications identified as built on Scalus include Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal says Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js has more than 20,000 downloads per month.
- missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: Dijkstra readiness is presented as necessary because Dijkstra introduces Plutus V4 support, nested transactions, guard script types, and accounts affecting smart contract development, evaluation, transaction building, ledger rules, testing, and workflows.
- missing: Independent evidence for: Delivery is described as milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board, third-party assurance, public reporting, and open community sessions.
- missing: Independent evidence for: The proposal frames Scalus as shared Apache 2.0 open-source infrastructure intended to reduce repeated assembly work across many Cardano teams, tools, and products.
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
- finding: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, approximately $394,375 at a $0.16/ADA reference rate, with no contingency." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal asks for ₳2,464,844 over 9 months, approximately $394,375 at a $0.16/ADA reference rate, with no contingency." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Directional YES cleared ecosystem benefit, delivery, cost-efficiency, downside-protection, and portfolio-capacity floors.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: Dijkstra readiness is presented as necessary because Dijkstra introduces Plutus V4 support, nested transactions, guard script types, and accounts affecting smart contract development, evaluation, transaction building, ledger rules, testing, and workflows.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `4a89de9d981be2d0efe9da19bc8d732cbab41ebfe5118706aeb837ae5de4b255`
- snapshot_bundle_hash: `1deecaf8081df86a8660abffdc84fbdffeb054dfb97a2caf68d6ce3e68772b39`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `d68b33ee7989803aaecd7edc03d77c134a98a7f1`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2074, "NO": 0.0467, "YES": 0.7459}`

