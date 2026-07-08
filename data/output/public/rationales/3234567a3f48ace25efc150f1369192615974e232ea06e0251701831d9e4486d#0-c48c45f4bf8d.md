# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because baseline evidence needed for a responsible treasury vote was missing. This is a conservative, evidence-based hold, not a rejection of Scalus or Lantr Engineering.

The action requested 9 months of continuation funding for Scalus maintenance, Dijkstra hard-fork readiness, JVM/JS/TS interoperability, and a scoped application runtime, with Lantr Engineering as recipient. The proposal said the request was ₳2,464,844, reduced from an earlier larger proposal, and described deliverables including maintenance, initial Plutus V4 support, JS/TS documentation, Java/Kotlin examples, Dijkstra ledger and transaction-builder updates, conformance testing, and foundational runtime components by March 2027.

Some claims were supported in the proposal, including that Scalus is an established open-source Cardano development platform built over three years of continuous delivery, that the ask was reduced, and that the scope excludes items such as a standalone L1 node and broad formal verification. Other important claims were still only proposer-asserted or lacked independent evidence in the review, including direct use by named projects and embedding in named Cardano tooling. The review also found missing or incomplete treasury, feasibility, risk, alternatives, failure-mode, and community-impact analysis. The intake was blocked because `treasury_amount_lovelace` was missing for a treasury withdrawal, treasury analysis was incomplete, claims evidence was thin, and risk review was thin.

A directional YES or NO would require the missing baseline evidence: the treasury amount in lovelace, a complete proposal summary, line-item budget, milestone-gated disbursement evidence, feasibility assessment, mitigation evidence, independent assurance, alternatives analysis, failure-mode analysis, and community impact analysis. Without that, BEACN could not produce a responsible recommendation for spending shared ADA.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: 9-month continuation funding for Scalus maintenance, Dijkstra hard-fork readiness, JVM/JS/TS interoperability, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing Scalus maintenance including bug fixes, dependency upkeep, security patches, and releases, Initial Plutus V4 support in the compiler and standard library, Improved JS/TS interfaces and documentation for components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin integration examples for Spring Boot and Ktor and cleaner integration paths with Cardano Client Lib and Yaci, Dijkstra ledger rules and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts, Conformance testing for Dijkstra changes, Foundational runtime components including reactive workers, chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 for 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says the ask was reduced from a previous ₳8.5M 12-month proposal to ₳2.464844M over 9 months, with the L1 node and third-party dependency-heavy work removed from scope.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus is claimed to be used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are claimed to be embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js has more than 20,000 monthly downloads.
- missing: Independent evidence for: Scalus is claimed to be used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- missing: Independent evidence for: Scalus components are claimed to be embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- missing: Independent evidence for: The proposal claims Dijkstra will introduce Plutus V4 support, nested transactions, guard script types, and accounts that affect smart contract development, evaluation, transaction building, ledger rules, testing, and workflows.
- missing: Independent evidence for: Delivery is described as milestone-based, administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Flag count: 0
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Scalus is claimed to be used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: evidence is too thin for a directional vote while 1 blocker(s) remain open.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Scalus is claimed to be used directly by Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm systems.
- Claims and evidence missing: Independent evidence for: Scalus components are claimed to be embedded in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `c48c45f4bf8df90bd4eadd1bcfeec3c1f44a3041614bc3f450754277dd999efa`
- snapshot_bundle_hash: `a460ea8435c758aae51d31c1fa48f2982a827fa01b92c3c5e475d4934a3b91a4`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `0`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

