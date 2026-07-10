# Rationale: fdd468da5cc4ac8431dcd7e2b3211666c73bc229f85879469f67f1d9d51d344d#0
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.07` + doctrine-LLM nudge `-0.03`) | Confidence: `0.5` | Readiness: `0.5`
> Reasoning layer (precomputed): Hard forks receive highest scrutiny under the doctrine, and although the proposal provides substantial technical detail and external references, the extracted claims leave key readiness and risk evidence only partially covered: the 85% SPO upgrade threshold remains to be determined, testing and audit claims are mostly asserted rather than included, and reversion is limited to disaster recovery or disabling cost models. Given the assessment marks risk review as thin, a small cautionary negative nudge is justified without overriding the deterministic gates.

## Plain-language explanation (deterministic-heuristic)
BEACN records ABSTAIN on Hard Fork to Protocol Version 11 ('van Rossem' Hard Fork). This is a conservative abstention because the evidence does not justify stronger certainty.

The action is a HardForkInitiation. The cached anchor describes the request as: Initiate an intra-era hard fork of Cardano mainnet to Protocol Version 11.0, called the van Rossem hard fork. It asks the treasury for none ADA. The strongest grounded claim is: The proposal would upgrade Cardano mainnet to protocol major version 11 and minor version 0 through an intra-era hard fork that remains in the Conway era.

A material claim remains proposer-asserted or thinly supported: The addition of UPLC case expressions over Bool, Integer, and Data is claimed to improve script performance and produce cleaner script logic. Reason code: DREP_DISTRIBUTION_MISSING.

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
- finding: Requested: Initiate an intra-era hard fork of Cardano mainnet to Protocol Version 11.0, called the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: none
- finding: Deliverables: Upgrade Cardano mainnet protocol from version 10.0 to 11.0 while remaining in the Conway era., Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153 available., Make all Plutus built-in functions consistently available across Plutus V1, V2, and V3., Add UPLC case expressions for Bool, Integer, and Data., Promote or tighten several ledger and node validation rules, including VRF key hash uniqueness, reference input rules, Constitutional Committee voting restrictions, withdrawal predicates, and PPView mismatch reporting.
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal would upgrade Cardano mainnet to protocol major version 11 and minor version 0 through an intra-era hard fork that remains in the Conway era.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade introduces new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, including modular exponentiation, dropList, BLS12-381 multi-scalar multiplication, Array, and Value-related built-ins.
- finding: Claim (technical, supported_in_proposal, high materiality): The upgrade will make the full set of Plutus built-ins available across Plutus V1, V2, and V3, expanding capabilities for existing V1 and V2 scripts.
- finding: Claim (technical, proposer_asserted, medium materiality): The addition of UPLC case expressions over Bool, Integer, and Data is claimed to improve script performance and produce cleaner script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims transaction shape is unchanged and ecosystem upgrade effort is minimized because the hard fork is intra-era.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal claims testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- missing: Independent evidence for: The addition of UPLC case expressions over Bool, Integer, and Data is claimed to improve script performance and produce cleaner script logic.
- missing: Independent evidence for: The proposal claims transaction shape is unchanged and ecosystem upgrade effort is minimized because the hard fork is intra-era.
- missing: Independent evidence for: The proposal claims testing reports show no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of new Plutus primitives and case expressions across Plutus V1, V2, and V3.
- missing: Independent evidence for: The proposal says security audits were undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol major version 11 and minor version 0 through an intra-era hard fork that remains in the Conway era." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The addition of UPLC case expressions over Bool, Integer, and Data is claimed to improve script performance and produce cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal would upgrade Cardano mainnet to protocol major version 11 and minor version 0 through an intra-era hard fork that remains in the Conway era." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): Hard forks receive highest scrutiny under the doctrine, and although the proposal provides substantial technical detail and external references, the extracted claims leave key readiness and risk evidence only partially covered: the 85% SPO upgrade threshold remains to be determined, testing and audit claims are mostly asserted rather than included, and reversion is limited to disaster recovery or disabling cost models. Given the assessment marks risk review as thin, a small cautionary negative nudge is justified without overriding the deterministic gates.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Protocol action lacks a complete independently pinned readiness packet: version_guardrails_pass, testnet_results_pass, spo_readiness_pass, exchange_readiness_pass, dapp_readiness_pass, security_review_pass, constitutional_alignment_pass, rollback_or_containment_plan
- Claims and evidence missing: Independent evidence for: The addition of UPLC case expressions over Bool, Integer, and Data is claimed to improve script performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal claims transaction shape is unchanged and ecosystem upgrade effort is minimized because the hard fork is intra-era.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `63cb57d0ebc6649f03ddb91e32697599876b24c5810abaa45b39636ae1329b53`
- snapshot_bundle_hash: `e61d6ef37960e678d6abacfb38a5db654696fe1a1dd2ea96321287a86fee95f6`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.445, "NO": 0.2775, "YES": 0.2775}`

