# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.56` (binding treasury composite; advisory raw signal `-0.56`; LLM lean `+0.0` recorded, not added) | Confidence: `0.82` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show plausible public-benefit infrastructure value, a reduced scope and budget, and some independently checkable adoption metrics, while several high-materiality adoption, governance, and delivery assurances remain proposer-asserted within the document. Because the deterministic assessment is already ready and the doctrine says missing or incomplete independently verified diligence should not become a directional penalty, no additional nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.

The proposal requests ₳2,464,844 for a 9-month continuation of Scalus by Lantr Engineering, covering maintenance, Dijkstra readiness, interoperability with JVM and JS/TS ecosystems, and a scoped application runtime, with delivery targeted for March 2027. The proposal says Scalus is an open-source Cardano development platform built over three years of continuous delivery, and that claim was well-supported. The proposal also states that this resubmission is much smaller than the earlier request, reducing the budget from ₳8,503,000 over 12 months to about ₳2,464,844 over 9 months and reducing staffing from 8.25 to 2.25 FTE.

Several important adoption claims were not independently supported in the review. In particular, BEACN did not have enough replayable public evidence that Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm, or that Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit. The review also found thin claims-and-evidence coverage, missing sustainability path analysis, and missing detail on independent assurance and dependency mapping.

This is a conservative, evidence-based hold, not a rejection of the project. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the adoption and reuse claims, the sustainability path, independent assurance, and the dependency map.

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
- finding: Requested: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance: bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview including initial Plutus V4 support in the compiler and standard library, Improved interfaces and documentation for JS/TS components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Foundational runtime components and reactive workers, Dijkstra ledger rules and transaction-builder updates for new builtins, cost models, nested transactions, accounts, and guard scripts, Conformance testing for Dijkstra changes, Java/Kotlin integration including Spring Boot and Ktor examples, Cleaner integration paths with Cardano Client Lib and Yaci, Runtime chain follower and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, independently_verifiable, medium materiality): Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js reaches more than 20,000 downloads per month.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal asks for ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): This resubmission reduces the previous proposal from ₳8,503,000 over 12 months to about ₳2,464,844 over 9 months and reduces FTE from 8.25 to 2.25.
- missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- missing: Independent evidence for: Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- missing: Independent evidence for: Delivery is milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- missing: Independent evidence for: The proposal claims Dijkstra changes including Plutus V4 support, nested transactions, guard script types, and accounts will affect smart contract development, Plutus evaluation, transaction building, ledger rules, testing, and developer workflows.
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
- finding: Strongest YES: the proposal substantiates "Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: Scalus is used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- Claims and evidence missing: Independent evidence for: Scalus components are reused in MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `45c6ae7f4013e5e9fbf1e4183dd2f22fae745aaffedc0c76b086d60f8aa42296`
- snapshot_bundle_hash: `47289969dbccb6ae012853c0b213dccde0bdffb8095abb9f012a487c3d76164c`
- soul_commit: `c813ed97f64dba61150d01964327553baf720d38`
- soul_text_hash: `fa491ed711b9834e5a3c72d35903cec18afe8d93e1262f42ffcb20f5fce2c276`
- resource_registry_commit: `cf10b7dbeda9a1c22264141d5790e689bc38a168`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4158, "NO": 0.5446, "YES": 0.0396}`

