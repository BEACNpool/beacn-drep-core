# Rationale: fdd468da5cc4ac8431dcd7e2b3211666c73bc229f85879469f67f1d9d51d344d#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.07` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5` | Readiness: `0.5`
> Reasoning layer (precomputed): Hard fork doctrine requires high evidence quality, clear upgrade readiness, compatibility readiness, and a concrete risk register; the claims include meaningful technical benefits and some checkable references, but the assessment marks risk review as thin and overall status as incomplete, while SPO readiness remains a pre-ratification condition rather than demonstrated in the document.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review did not have the DRep distribution information needed for a directional vote on this hard fork. This is a conservative, evidence-based hold on a high-impact protocol upgrade, not a rejection of the proposal’s technical direction.

The action requested an intra-era Cardano mainnet hard fork from protocol version 10.0 to 11.0, the van Rossem hard fork, while staying in the Conway era. The proposal claimed this would add new Plutus primitives from several CIPs, make Plutus built-ins consistently available across Plutus V1, V2, and V3, add UPLC case expressions, and tighten several ledger and node validation, diagnostic, and security checks. The pinned anchor document was available, and some core claims were supported or independently checkable, including the version upgrade, the cited CIPs, the broader Plutus built-in availability, and a referenced node performance report showing no benchmark regressions.

The review still found important gaps. The risk review was thin, with execution risk marked unknown and missing mitigation evidence and independent assurance. The proposal stated that at least 85% of stake pools by active stake should be upgraded before ratification, but that readiness was a condition rather than demonstrated evidence in the document. The review also lacked a complete independently pinned readiness packet, including version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning. Independent evidence was also missing for the claimed benefits of UPLC case expressions and for the stated working group and steering committee endorsements.

The gates for having a pinned, replayable proposal anchor and a serious strongest-YES counterargument passed, but the risk and readiness evidence did not reach the standard BEACN applies to hard forks. A directional vote would be unblocked by the missing DRep distribution data plus an independently pinned readiness packet covering operator, exchange, dApp, security, constitutional, and rollback or containment readiness, along with stronger independent evidence for the unsupported claims.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: HardForkInitiation
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: not required
- finding: Requested: Initiate an intra-era Cardano mainnet hard fork to Protocol Version 11.0, named the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: none
- finding: Deliverables: Upgrade Cardano mainnet protocol from version 10.0 to 11.0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions consistently available across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Promote or tighten several ledger and node validation, diagnostic, and security checks.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed hard fork upgrades Cardano mainnet from protocol version 10.0 to 11.0 while remaining in the Conway era with unchanged transaction shape.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade introduces new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153.
- finding: Claim (technical, supported_in_proposal, high materiality): The upgrade makes all Plutus built-ins available across Plutus V1, V2, and V3, expanding capabilities for existing V1 and V2 scripts.
- finding: Claim (technical, proposer_asserted, medium materiality): The upgrade adds UPLC case expressions for Bool, Integer, and Data, which the proposal says will improve performance and simplify script logic.
- finding: Claim (technical, supported_in_proposal, high materiality): The hard fork promotes VRF key hash uniqueness, Constitutional Committee voting restrictions, revised reference input rules, and withdrawal validation changes into ledger-level predicates or tightened ledger rules.
- finding: Claim (governance, proposer_asserted, medium materiality): Intersect's Hard Fork Working Group recommended submitting the governance action on 2026-06-15 and Intersect's Technical Steering Committee endorsed it on 2026-06-16.
- missing: Independent evidence for: The upgrade adds UPLC case expressions for Bool, Integer, and Data, which the proposal says will improve performance and simplify script logic.
- missing: Independent evidence for: Intersect's Hard Fork Working Group recommended submitting the governance action on 2026-06-15 and Intersect's Technical Steering Committee endorsed it on 2026-06-16.
- missing: Independent evidence for: Testing reports are said to show no behavioral regressions, complete specification-to-implementation conformance for new ledger rules, and correct operation of the new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 0
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposed hard fork upgrades Cardano mainnet from protocol version 10.0 to 11.0 while remaining in the Conway era with unchanged transaction shape." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The upgrade adds UPLC case expressions for Bool, Integer, and Data, which the proposal says will improve performance and simplify script logic." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: if claims cannot be tied to replayable evidence, abstaining avoids overclaiming certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `ready`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Hard fork actions are high-impact protocol upgrades and require operator-aware review.
- Intake: Action type: HardForkInitiation
- Claims and evidence: Proposal anchor: pinned and replayable
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposed hard fork upgrades Cardano mainnet from protocol version 10.0 to 11.0 while remaining in the Conway era with unchanged transaction shape." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: Hard fork doctrine requires high evidence quality, clear upgrade readiness, compatibility readiness, and a concrete risk register; the claims include meaningful technical benefits and some checkable references, but the assessment marks risk review as thin and overall status as incomplete, while SPO readiness remains a pre-ratification condition rather than demonstrated in the document.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Protocol action lacks a complete independently pinned readiness packet: version_guardrails_pass, testnet_results_pass, spo_readiness_pass, exchange_readiness_pass, dapp_readiness_pass, security_review_pass, constitutional_alignment_pass, rollback_or_containment_plan
- Claims and evidence missing: Independent evidence for: The upgrade adds UPLC case expressions for Bool, Integer, and Data, which the proposal says will improve performance and simplify script logic.
- Claims and evidence missing: Independent evidence for: Intersect's Hard Fork Working Group recommended submitting the governance action on 2026-06-15 and Intersect's Technical Steering Committee endorsed it on 2026-06-16.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `b7e4d2b3cbe0006a126e0a1b748dc4d96118c05e61c78fe0f0e0e7b0b1dfcb25`
- snapshot_bundle_hash: `e59363392da7d4b0f05b454c52c2d76f467a2981929d08d6a981f8721ed49065`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.445, "NO": 0.2775, "YES": 0.2775}`

