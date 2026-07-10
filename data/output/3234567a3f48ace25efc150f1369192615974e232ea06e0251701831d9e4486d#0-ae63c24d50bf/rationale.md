# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because a required baseline field for a treasury withdrawal was missing: `treasury_amount_lovelace`. Even though the proposal text says it requests ₳2,464,844, the structured treasury review recorded the requested ADA amount as 0 and the intake and synthesis gates were blocked on the missing on-chain treasury amount field.

The action requested 9 months of Scalus funding for maintenance, Dijkstra hard-fork readiness, JVM and JS/TS interoperability, and foundational application runtime components, with delivery planned through March 2027. The proposer described Scalus as an established open-source Cardano development platform, claimed reuse across several Cardano developer tools, and listed prior delivery, milestone-based administration, public reporting, audited SundaeSwap treasury contracts, independent oversight, and third-party assurance.

Some claims were supported inside the proposal, including the ₳2,464,844 budget, the 9-month schedule, the reduced scope compared with the prior ₳8.503M proposal, and the quarterly milestone plan. But several important claims still lacked independent evidence in the review, including Scalus’s three-year open-source delivery record and its reuse across Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution. The treasury review also still lacked a sustainability path, while the risk review lacked independent assurance and a dependency map.

This ABSTAIN is a conservative, evidence-based hold, not a judgment that the work has no value. A directional vote would require the missing `treasury_amount_lovelace` field to be present and reviewable for the treasury withdrawal, plus stronger independent evidence for the key technical and adoption claims and the missing treasury and risk-review materials.

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
- finding: Requested: Fund a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview with initial Plutus V4 support in the compiler and standard library, Improved interfaces and documentation for JS/TS components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin integration examples for Spring Boot and Ktor and cleaner integration paths with Cardano Client Lib and Yaci, Dijkstra ledger rules and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts with conformance testing, Foundational runtime components, reactive workers, chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 for 9 months at a $0.16/ADA reference rate with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal is a reduced resubmission from a prior ₳8.503M 12-month proposal, reducing budget by 71%, FTE from 8.25 to 2.25, and removing the standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion from scope.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- finding: Claim (adoption, proposer_asserted, high materiality): Protocols and applications listed as built on Scalus include Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states Scalus has 4,642 commits across 32 releases, 12 contributors, and more than 20,000 monthly Scalus.js downloads.
- missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- missing: Independent evidence for: Protocols and applications listed as built on Scalus include Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm.
- missing: Independent evidence for: Delivery is described as milestone-based and administered through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
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
- finding: Flag count: 0
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests ₳2,464,844 for 9 months at a $0.16/ADA reference rate with no contingency." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests ₳2,464,844 for 9 months at a $0.16/ADA reference rate with no contingency." though 1 review blocker(s) remain open.
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
- Claims and evidence missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `ae63c24d50bfb9721b36ddd8c8e02dd09a4d2a84e81bfb4a5ac059d4d54a38c6`
- snapshot_bundle_hash: `7f075f04bea5d5a23a901844856a67f6168d0a43609f3fac2c97905784714322`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

