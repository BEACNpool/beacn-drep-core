# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.01` + doctrine-LLM nudge `-0.02`) | Confidence: `0.5` | Readiness: `0.6`
> Reasoning layer (precomputed): For a hard fork, the doctrine requires high evidence quality, clear readiness, migration readiness, and a risk register with concrete mitigations. The claims include useful technical detail and checkable references, but several critical safety assertions are still proposer-asserted and the assessment marks risk review as thin, so a small cautionary nudge is justified.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the hard fork is high-impact and the review did not find a complete independently pinned readiness and risk package. This is a conservative, evidence-based hold, not a rejection of the upgrade.

The action requested an intra-era Cardano mainnet hard fork from protocol version 10.0 to 11.0, the “van Rossem” hard fork. The proposal says it would add new Plutus primitives from several CIPs, make Plutus built-ins consistently available across Plutus V1, V2, and V3, add UPLC case expressions, and tighten ledger and node validation rules such as VRF key hash uniqueness and Constitutional Committee voting restrictions. Several core claims were supported or independently checkable, including the protocol version upgrade, the cited Plutus primitives, the VRF rule change, the performance report reference, and the statement that reversal would require the CIP-0135 disaster recovery process except for possible containment through companion cost model settings.

The hold came from what was still thin or unsupported. Some important safety and benefit claims remained proposer-asserted, including the claim that testing showed no behavioral regressions, full specification-to-implementation conformance, and correct operation of new Plutus features across versions. The review also lacked independent evidence that native UPLC case expressions would improve performance and produce cleaner script logic. Most importantly for a hard fork, the assessment did not have a complete readiness packet covering version guardrails, testnet results, SPO readiness, exchange readiness, dApp readiness, security review, constitutional alignment, and rollback or containment planning.

The proposal had a pinned anchor and passed enough evidence review to show a serious case for YES, especially on the basic protocol upgrade claim. But the risk review was marked thin, with missing mitigation evidence and independent assurance. BEACN would need those readiness, testing, security, and containment materials tied to replayable public evidence before moving from ABSTAIN to a directional YES or NO.

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
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol from version 10.0 to 11.0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions consistently available across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Promote or tighten several ledger and node validation rules, including VRF key hash uniqueness and Constitutional Committee voting restrictions.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet from protocol version 10.0 to 11.0 without an era transition.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade would introduce new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153.
- finding: Claim (technical, supported_in_proposal, high materiality): The upgrade would make all Plutus built-in functions available across Plutus V1, V2, and V3, expanding capabilities for existing V1 and V2 scripts.
- finding: Claim (technical, proposer_asserted, medium materiality): Native UPLC case expressions for Bool, Integer, and Data would improve performance and produce cleaner script logic.
- finding: Claim (technical, supported_in_proposal, high materiality): The upgrade would promote VRF key hash uniqueness to a ledger-level rule so that no two stake pools can register or operate with the same VRF key.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2, and V3.
- missing: Independent evidence for: Native UPLC case expressions for Bool, Integer, and Data would improve performance and produce cleaner script logic.
- missing: Independent evidence for: The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2, and V3.
- missing: Independent evidence for: The proposal states that security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet from protocol version 10.0 to 11.0 without an era transition." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Native UPLC case expressions for Bool, Integer, and Data would improve performance and produce cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet from protocol version 10.0 to 11.0 without an era transition." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: For a hard fork, the doctrine requires high evidence quality, clear readiness, migration readiness, and a risk register with concrete mitigations. The claims include useful technical detail and checkable references, but several critical safety assertions are still proposer-asserted and the assessment marks risk review as thin, so a small cautionary nudge is justified.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Protocol action lacks a complete independently pinned readiness packet: version_guardrails_pass, testnet_results_pass, spo_readiness_pass, exchange_readiness_pass, dapp_readiness_pass, security_review_pass, constitutional_alignment_pass, rollback_or_containment_plan
- Claims and evidence missing: Independent evidence for: Native UPLC case expressions for Bool, Integer, and Data would improve performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus features across V1, V2, and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `29e8f7e0d9844fc6000296a8494f08c2f450fd3f4bc0869fa1b5f117b05b6417`
- snapshot_bundle_hash: `72b0ee6f6c2637187d805fe9e784de8521fae3f6554e6dce8580047ec4628290`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.445, "NO": 0.2775, "YES": 0.2775}`

