# Rationale: fdd468da5cc4ac8431dcd7e2b3211666c73bc229f85879469f67f1d9d51d344d#0
Recommendation: **YES**
Score: `-0.1` (raw `-0.07` + doctrine-LLM nudge `-0.03`) | Confidence: `0.525` | Readiness: `0.5`
> Reasoning layer (precomputed): Hard forks receive highest scrutiny under the doctrine, and although the proposal provides substantial technical detail and external references, the extracted claims leave key readiness and risk evidence only partially covered: the 85% SPO upgrade threshold remains to be determined, testing and audit claims are mostly asserted rather than included, and reversion is limited to disaster recovery or disabling cost models. Given the assessment marks risk review as thin, a small cautionary negative nudge is justified without overriding the deterministic gates.

## Plain-language explanation (precomputed)
BEACN voted YES because the core request was clear, reviewable, and supported: this action initiates the van Rossem hard fork to move Cardano mainnet from protocol version 10.0 to 11.0 while staying in the Conway era.

The proposal requests an intra-era hard fork with no treasury amount. It would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, make Plutus built-ins consistently available across Plutus V1, V2, and V3, add UPLC case expressions for Bool, Integer, and Data, and tighten several ledger and node validation rules. The proposal also says transaction shape is unchanged, ecosystem upgrade effort is minimized, testing found no behavioral regressions, audits were undertaken, and at least 85% of stake pools by active stake should be upgraded before ratification.

BEACN found the anchor document pinned and replayable, and the main protocol-version upgrade claim cleared the evidence gates. Several technical claims were independently verifiable or supported in the proposal, including the move to protocol version 11.0, the listed new Plutus primitives, cross-version availability of built-ins, the linked node performance report, and the stated disaster-recovery limits around reversion. However, some claims remained thinner: the claimed performance and cleanliness benefits of UPLC case expressions lacked independent evidence, the minimized ecosystem upgrade claim was still proposer-asserted, and the 85% stake pool upgrade threshold still needed to be determined before ratification.

The review treated this as a high-impact hard fork requiring elevated scrutiny, and it recorded thin risk evidence, missing mitigation evidence, missing independent assurance, and unknown execution risk. Even with those cautions, there were no decisive blockers or open questions, and BEACN’s hard-fork policy allows a clean hard-fork initiation to proceed despite thin generic risk fields when the core action clears review. Therefore BEACN voted YES, while recognizing that confidence was limited by the remaining readiness and risk uncertainty.

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
- Action-type policy: a clean hard-fork initiation may proceed despite thin generic risk fields; missing risk detail remains explicit uncertainty.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- No DRep distribution available.
- Claims and evidence missing: Independent evidence for: The addition of UPLC case expressions over Bool, Integer, and Data is claimed to improve script performance and produce cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal claims transaction shape is unchanged and ecosystem upgrade effort is minimized because the hard fork is intra-era.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `133c5da842d96055da9a712f41dc11d900839e3f3567e05b3f9edefcd24b552e`
- snapshot_bundle_hash: `247615d6dcb9280a04b2576429a9a551c513df68f7ec0936cde6221ab3b01927`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ac61a1f4a2a6f8653b1f45352baf3efd8220c5e3`
- resources_used: `gov_actions_api, gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.2544, "NO": 0.3744, "YES": 0.3713}`

