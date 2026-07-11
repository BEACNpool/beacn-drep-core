# Rationale: gov_action1xg69v73lfzkwyhhuz583x6geyc2ewn3r96sxuqj3wqvrrk0yfpksqqa63yc
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): The extracted claims show a narrowed resubmission with explicit exclusions, milestone governance, open-source reuse, and concrete infrastructure deliverables, which modestly improves alignment with treasury stewardship and public-benefit ecosystem growth. The nudge remains small because several high-materiality adoption and delivery-record claims are proposer-asserted rather than fully evidenced inside the anchor document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the work.

The proposal asks for ₳2,464,844 over 9 months for continued Scalus maintenance, Dijkstra hard-fork readiness, JVM and JS/TS interoperability, and a scoped application runtime, with delivery due by March 2027. The proposer presents this as a reduced resubmission from a prior larger request, with milestone-based delivery, audited SundaeSwap treasury contracts, oversight, and third-party assurance. The review found some claims well-supported, especially that Scalus components are reused in Cardano developer tooling including MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.

However, several material claims were still not independently evidenced in the reviewed anchor, including that Scalus is an established open-source Cardano platform built over three years of continuous delivery, and that protocols and applications such as Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on it. The evidence status was therefore thin, and the review also noted missing treasury and risk details: a sustainability path, independent assurance, and a dependency map.

The proposal passed the basic intake gate because the pinned anchor document was available and replayable, and the counterargument review found a credible strongest-YES case. But treasury actions require elevated scrutiny because they spend shared ADA, the treasury flow signal was stressed, execution risk was medium, and the verified Net Change Limit requirement was not satisfied. The specific evidence that would unblock a directional vote is a pinned, independently verifiable Net Change Limit from public chain evidence, plus stronger independent support for the major adoption, delivery-record, assurance, sustainability, and dependency claims.

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
- finding: Requested: Funding for a 9-month continuation of Scalus covering maintenance, Dijkstra hard-fork readiness, interoperability across JVM and JS/TS ecosystems, and a scoped application runtime.
- finding: Recipient: Lantr Engineering
- finding: Stated amount: 2464844
- finding: Deliverables: Ongoing maintenance including bug fixes, dependency upkeep, security patches, and releases, Dijkstra readiness including Plutus V4 support, ledger rules, transaction-builder updates, conformance testing, nested transactions, accounts, and guard scripts, Improved JS/TS interfaces and documentation for components embedded in MeshJS, Evolution SDK, and Lucid Evolution, Java/Kotlin interoperability including Spring Boot and Ktor examples and cleaner integration with Cardano Client Lib and Yaci, Scoped runtime components including foundational components, reactive workers, chain follower, and task scheduler
- finding: Deadline/expiry: March 2027
- finding: Claim (technical, proposer_asserted, high materiality): Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- finding: Claim (adoption, independently_verifiable, high materiality): Scalus components are reused in Cardano developer tooling including MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit.
- finding: Claim (adoption, proposer_asserted, high materiality): Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,464,844 over 9 months, equivalent to about $394,375 at a $0.16/ADA reference rate, with no contingency.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal is a reduced resubmission from a prior ₳8,503,000 12-month proposal, removing the standalone L1 node, full L2 integration, broad formal verification, and advanced devnet expansion from scope.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposer states that Scalus has 4,642 commits across 32 releases, 12 contributors, and Scalus.js has more than 20,000 monthly downloads.
- missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- missing: Independent evidence for: Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- missing: Independent evidence for: Dijkstra hard-fork changes are stated to affect smart contract development, Plutus evaluation, transaction building, ledger rules, testing, and developer workflows.
- missing: Independent evidence for: Lantr Engineering states that every prior milestone was delivered on time and commits to public reporting, open community sessions, and on-time milestone delivery for this work.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2464844
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.86
- missing: sustainability path
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: medium
- finding: Governance risk: low
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
- finding: Strongest YES: the proposal substantiates "Scalus components are reused in Cardano developer tooling including MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2464844
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Scalus components are reused in Cardano developer tooling including MeshJS, Evolution SDK, Lucid Evolution, Cardano Client Lib, and YaciDevKit." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: The extracted claims show a narrowed resubmission with explicit exclusions, milestone governance, open-source reuse, and concrete infrastructure deliverables, which modestly improves alignment with treasury stewardship and public-benefit ecosystem growth. The nudge remains small because several high-materiality adoption and delivery-record claims are proposer-asserted rather than fully evidenced inside the anchor document.
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
- Claims and evidence missing: Independent evidence for: Scalus is an established open-source Cardano development platform built by Lantr Engineering over three years of continuous delivery.
- Claims and evidence missing: Independent evidence for: Protocols and applications including Gummiworm L2, Bifrost, SugarRush, Vela, and DID/DIDComm are built on Scalus.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `b02a109afc6b522ac3daf4dc1c28c8ed8e5ab931ffdfa33f0317fef319c49fb4`
- snapshot_bundle_hash: `274fb0e98ea92d3ca91cd1ca684fa3cf0d4fcb78d85a130d0658f045114c0b0c`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

