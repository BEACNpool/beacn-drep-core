# Rationale: 3234567a3f48ace25efc150f1369192615974e232ea06e0251701831d9e4486d#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.11` (raw `-0.11` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7775` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe bounded continuation of existing open-source infrastructure, a substantially reduced ask, explicit exclusions of larger risky scope, and milestone/assurance mechanisms. The nudge remains small because several adoption, execution, and oversight claims are proposer-asserted in the document rather than independently evidenced there, and treasury stewardship still requires caution for a multi-million ADA withdrawal.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the project.

The proposal requested ₳2,464,844 for Lantr Engineering to continue Scalus work through March 2027, covering maintenance, Dijkstra readiness, JVM and JS/TS interoperability, and scoped runtime components. The proposal itself supported several important points: Scalus is presented as an open-source Cardano development platform with three years of continuous delivery, the ask was reduced from a prior ₳8.503M proposal to ₳2.464844M over 9 months, and the funded scope explicitly excludes larger items such as a standalone L1 node, full Gummiworm L2 integration, broad formal verification, and advanced devnet expansion.

The review also found gaps. Several adoption claims were proposer-asserted rather than independently evidenced in the supplied record, including reuse in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution, and use by protocols or applications such as Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm. The review also flagged thin claims-and-evidence status, missing sustainability-path analysis, missing independent assurance, and a missing dependency map, with medium execution risk.

The vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence. Stronger independent evidence for the adoption and dependency claims, plus clearer sustainability and assurance materials, would also improve confidence. Until then, BEACN held at NEEDS_MORE_INFO to avoid overstating certainty on a multi-million ADA treasury request.

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
- finding: Requested: Continuation funding for Scalus 2026 covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra developer preview with initial Plutus V4 support in the compiler and standard library, Dijkstra ledger rules and transaction-builder updates including new builtins, cost models, nested transactions, accounts, and guard scripts, Improved JS/TS interfaces and documentation for components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin integration including Spring Boot and Ktor examples and cleaner integration with Cardano Client Lib and Yaci, Foundational runtime components, reactive workers, chain follower, and task scheduler, Reference applications, integration tests, and early-user feedback for the scoped runtime
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 for 9 months at a $0.16/ADA reference rate with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal is reduced from a previous ₳8.503M 12-month proposal to ₳2.464844M over 9 months, with FTE reduced from 8.25 to 2.25 and contingency reduced from 10% to 0%.
- finding: Claim (adoption, proposer_asserted, high materiality): Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- finding: Claim (adoption, proposer_asserted, high materiality): The proposer says protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- finding: Claim (adoption, independently_verifiable, medium materiality): The document states Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js reaches more than 20,000 downloads per month.
- missing: Independent evidence for: Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- missing: Independent evidence for: The proposer says protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- missing: Independent evidence for: Delivery is described as milestone-based through audited SundaeSwap treasury contracts with an independent oversight board and third-party assurance.
- missing: Independent evidence for: Lantr Engineering says every prior Scalus milestone was delivered on time and commits to public reporting, open community sessions, and on-time milestone delivery for treasury-funded work.
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
- finding: Strongest YES: the proposal substantiates "Scalus is an open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution." — so cost or precedent may outweigh the benefit.
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
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe bounded continuation of existing open-source infrastructure, a substantially reduced ask, explicit exclusions of larger risky scope, and milestone/assurance mechanisms. The nudge remains small because several adoption, execution, and oversight claims are proposer-asserted in the document rather than independently evidenced there, and treasury stewardship still requires caution for a multi-million ADA withdrawal.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: Scalus components are reused in Cardano Client Lib, YaciDevKit, MeshJS SDK, Evolution SDK, and Lucid Evolution.
- Claims and evidence missing: Independent evidence for: The proposer says protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `756e77b1c1a323d5437d66a99c04999331c14828dfabb978e9e202252c846961`
- snapshot_bundle_hash: `d54918925d75ad3ff5dc0badedd3cea3614b37de71bb5539f6d37b48f8faae3a`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5144, "NO": 0.3528, "YES": 0.1328}`

