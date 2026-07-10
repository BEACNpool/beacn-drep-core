# Rationale: gov_action1mr0qdz2jmagvsch6r08fhqvq6vu8jakt4c8m9s7ea7z0p740vntqq4yjd6j
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `+0.0`) | Confidence: `0.7808` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal provides a detailed scope, milestones, budget breakdown, and some independently checkable success metrics, while several important adoption, cost-efficiency, and execution-capacity claims remain proposer asserted. Because the deterministic treasury analysis is already complete and the document's evidence mix is neither unusually weak nor strong enough to justify overriding the mechanical result, no additional bounded nudge is warranted.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not opposition to Daedalus or to the proposed work.

The proposal asks for 1,785,333 ADA to fund Se7en Labs, Inc. for Daedalus wallet maintenance and improvements in 2026-2027, with Intersect administering funds and verifying milestones. The work includes Cardano node and wallet upgrades, hard fork readiness, release engineering, security and dependency maintenance, hardware wallet support for Keystone and Flex, a CIP-30 dApp connector, Japanese-language support and translation, a public architecture assessment by Q3 2027, and independent financial audit oversight.

Several important claims were supported in the proposal: Daedalus private keys stay on the user’s device, the code is open-source under Apache 2.0, Se7en Labs has already shipped prior Daedalus maintenance work, the requested budget is broken down, and Intersect would administer funds with milestone-based oversight. Other claims were not independently supported enough for a treasury decision, including that Daedalus is Cardano’s only full-node desktop wallet with no third-party APIs or trusted backends, and that opt-in telemetry shows about 4,000 monthly active users while actual use is meaningfully higher.

The review found a pinned and replayable proposal anchor, medium execution risk, thin overall claims evidence, and missing treasury and risk details such as sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path. A directional vote would be unblocked by public, replayable evidence verifying the applicable Net Change Limit, plus stronger independent support for the key technical and adoption claims and clearer treasury-risk justification.

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
- finding: Requested: Treasury withdrawal to fund Daedalus Wallet Maintenance and Improvements 2026-2027 as a time-and-materials engagement delivered by Se7en Labs, Inc.
- finding: Recipient: Se7en Labs, Inc. with Intersect serving as administrator and milestone verifier
- finding: Stated amount: 1,785,333 ADA
- finding: Deliverables: Protocol maintenance including cardano-node and cardano-wallet upgrades, hard fork readiness, platform support, release engineering, and security/dependency maintenance, Compatible Daedalus release at least 2 weeks before each mainnet hard fork, Keystone and Flex hardware wallet support in a stable release, CIP-30 dApp connector in Daedalus with documentation and verified interoperability, Ongoing user support including Japanese-language support and full Japanese translation for new features, Architecture assessment published publicly by Q3 2027, Independent financial audit and milestone-based oversight through Intersect
- finding: Deadline/expiry: Contract year covering 2026-2027; IOG contract stated as closing August 31, 2026; architecture assessment by Q3 2027
- finding: Claim (technical, proposer_asserted, high materiality): Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- finding: Claim (technical, supported_in_proposal, high materiality): Daedalus private keys are generated and stored on the user's device and are never transmitted to an external service, with open-source Apache 2.0 code allowing auditability.
- finding: Claim (adoption, proposer_asserted, medium materiality): Opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while the proposer asserts the true count is meaningfully higher.
- finding: Claim (technical, supported_in_proposal, high materiality): Se7en Labs assumed responsibility for Daedalus under an IOG contract in January 2026 and shipped Mithril bootstrap, UTxO-HD/LSM backend integration, Apple Silicon builds, a release CLI, Nix modernization, and Daedalus 8.0 and 11.0.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal commits to stable Daedalus releases at least 2 weeks before each mainnet hard fork and to keeping cardano-node no more than 2 major versions behind the mainnet recommendation.
- finding: Claim (technical, supported_in_proposal, high materiality): The work includes Keystone and Flex hardware wallet support, a CIP-30 dApp connector, Japanese localisation, user support, and a public architecture assessment.
- missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- missing: Independent evidence for: Opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while the proposer asserts the true count is meaningfully higher.
- missing: Independent evidence for: Any unspent labor, test hardware, or audit budget at contract close is to be returned to the treasury.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1785333
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: confirmed
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
- finding: Strongest YES: the proposal substantiates "Daedalus private keys are generated and stored on the user's device and are never transmitted to an external service, with open-source Apache 2.0 code allowing auditability." and clears the evidence gates.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1785333
- Risk review: Execution risk: medium
- Counterargument pass: Strongest YES: the proposal substantiates "Daedalus private keys are generated and stored on the user's device and are never transmitted to an external service, with open-source Apache 2.0 code allowing auditability." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
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
- Claims and evidence missing: Independent evidence for: Daedalus is Cardano's only full-node desktop wallet and derives wallet and governance data directly from the chain without third-party APIs or trusted backends.
- Claims and evidence missing: Independent evidence for: Opt-in telemetry shows approximately 4,000 monthly active Daedalus users, while the proposer asserts the true count is meaningfully higher.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- cost comparables, budget proportionality, or sustainability evidence

## Reproducibility
- input_hash: `3f6bf165bef09c0437ec8ba119e6b340c47839e11f08c1f31bc1322d93a74bcf`
- snapshot_bundle_hash: `ee0c8dd595fb74d7d0231b66ed21aee02b14921bab899b75504d19ba26f7f597`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

