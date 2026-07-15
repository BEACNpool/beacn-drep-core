# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **YES**
Score: `0.2615` (binding treasury composite; advisory raw signal `-0.11`; LLM lean `+0.0` recorded, not added) | Confidence: `0.7854` | Readiness: `0.85`
> Reasoning layer (precomputed): The claims show plausible alignment with public-benefit ecosystem growth and maintenance of existing developer infrastructure, plus a materially reduced scope and budget, but many adoption, delivery, and governance-control statements remain proposer-asserted within the supplied document rather than independently evidenced here. The deterministic assessment already marked claims, treasury analysis, risk review, and synthesis complete, so no additional reasoning nudge is warranted.

## Plain-language explanation (deterministic-heuristic)
BEACN records YES on Scalus 2026: Maintenance, Dijkstra Readiness, Interoperability & Application Runtime. The deterministic gates found enough evidence and no decisive blocker.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a first scoped application runtime. It asks the treasury for 2464844 ADA. The strongest grounded claim is: The proposal claims three years of development with 4,642 commits, 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads.

A residual watch item: this claim remains proposer-asserted rather than independently shown: Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.

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
- finding: Requested: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a first scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance: bug fixes, dependency upkeep, security patches, and releases, Initial Plutus V4 support in the compiler and standard library, Improved JS/TS interfaces and documentation for Scalus components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Foundational runtime components and reactive workers, Ledger rules and transaction-builder updates for new builtins, cost models, nested transactions, accounts, and guard scripts, Conformance testing for Dijkstra changes, Java/Kotlin integration including Spring Boot and Ktor examples, Cleaner integration paths with Cardano Client Lib and Yaci, Runtime chain follower and task scheduler
- finding: Deadline/expiry: Three quarterly milestones over 9 months, July 2026 to March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Scalus is used by or underpins Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposal states that Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal claims three years of development with 4,642 commits, 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads.
- finding: Claim (economic, supported_in_proposal, high materiality): The requested budget is ₳2,464,844 for 9 months, approximately $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says it is a reduced resubmission from a prior ₳8.503M, 12-month proposal, with FTE reduced from 8.25 to 2.25 and several contested scope items removed.
- missing: Independent evidence for: Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: The proposal states that Scalus is used by or underpins Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- missing: Independent evidence for: The proposal states that Scalus components are reused in MeshJS SDK, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: The proposal asserts that Dijkstra readiness is needed because Plutus V4, nested transactions, guard script types, and accounts affect contract development, evaluation, transaction building, ledger rules, testing, and workflows.
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
- finding: Strongest YES: the proposal substantiates "The proposal claims three years of development with 4,642 commits, 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal claims three years of development with 4,642 commits, 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Scalus is described as an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: The proposal states that Scalus is used by or underpins Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `ff9db7f8b14171374e6d9eefab56de042ed1b6c05f68c29b2cca64b7b19e99c0`
- snapshot_bundle_hash: `b972c4309b86f8630aa0c0f753344bd48a76cae8f503b4d4b31dc18c49b55cc5`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `3e3c343fc0dd14a03a92aad1216ba6620b3d0185`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2074, "NO": 0.0467, "YES": 0.7459}`

