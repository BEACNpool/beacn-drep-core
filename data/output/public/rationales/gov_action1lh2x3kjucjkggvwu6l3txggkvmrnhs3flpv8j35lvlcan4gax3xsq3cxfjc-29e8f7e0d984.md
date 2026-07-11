# Rationale: gov_action1lh2x3kjucjkggvwu6l3txggkvmrnhs3flpv8j35lvlcan4gax3xsq3cxfjc
Recommendation: **ABSTAIN**
Score: `0.0` (raw `-0.01` + doctrine-LLM nudge `-0.02`) | Confidence: `0.5` | Readiness: `0.6`
> Reasoning layer (precomputed): The proposal aligns with protocol evolution goals and includes checkable references for CIPs and performance results, but for a hard fork the evidence quality is still thin on the required readiness and risk dimensions: stake pool readiness is explicitly pending, audits are asserted without detail, and the reversion plan acknowledges permanence while relying on disaster recovery rather than a concrete risk register with mitigations.

## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the hard fork is high-impact and the required readiness evidence was not complete. This is a conservative, evidence-based hold, not a rejection of the upgrade’s goals.

The action asks Cardano mainnet to move from protocol version 10.0 to 11.0 in an intra-era hard fork that remains in Conway. The proposal says this would add new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138, and CIP-0153, make Plutus built-ins consistently available across Plutus V1, V2, and V3, support native case expressions in Untyped Plutus Core, and tighten several ledger and node validation rules.

Several core claims were reviewable: the pinned anchor was available, the protocol-version change was clearly stated, the linked CIPs and performance results were checkable, and the proposal acknowledged the need for at least 85% stake pool readiness before ratification. But important claims were still too thin for a directional vote: performance gains from case expressions, full no-regression testing, audit details, mitigation evidence, independent assurance, and a complete readiness packet covering stake pools, exchanges, dApps, testnet results, constitutional alignment, security review, and rollback or containment planning.

Because hard forks are permanent, operator-sensitive changes, BEACN’s rules require more than proposer assertions for readiness and risk. A YES or NO vote would be unblocked by independently pinned evidence for the missing readiness checks, security review details, mitigation evidence, and testing results showing the upgrade is safe to execute across the ecosystem.

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
- finding: Requested: Initiate an intra-era hard fork of Cardano mainnet to Protocol Version 11.0, named the van Rossem hard fork.
- finding: Recipient: not stated in document
- finding: Stated amount: not stated in document
- finding: Deliverables: Upgrade Cardano mainnet protocol to major version 11 and minor version 0, Remain in the Conway era with no era transition, Make new Plutus primitives from CIP-0109, CIP-0132, CIP-0133, CIP-0138 and CIP-0153 available, Make all Plutus built-in functions consistently available across Plutus V1, V2 and V3, Support case expressions for Bool, Integer and Data in Untyped Plutus Core, Enforce or tighten ledger and node validation rules including VRF key hash uniqueness, reference input rules, Constitutional Committee voting restrictions, withdrawals validation, and PPView mismatch reporting
- finding: Deadline/expiry: not stated in document
- finding: Claim (technical, supported_in_proposal, high materiality): The action proposes upgrading Cardano mainnet from protocol version 10.0 to 11.0 through an intra-era hard fork that remains in the Conway era.
- finding: Claim (technical, independently_verifiable, high materiality): The upgrade adds new Plutus primitives defined in CIP-0109, CIP-0132, CIP-0133, CIP-0138 and CIP-0153, including modular exponentiation, dropList, BLS12-381 multi-scalar multiplication, Array, and Value-related built-ins.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposal states that all Plutus built-in functions, including newly introduced ones, will become available across Plutus V1, V2 and V3.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposal claims native case expressions over Bool, Integer and Data in Untyped Plutus Core will provide significant performance gains and cleaner script logic.
- finding: Claim (technical, proposer_asserted, high materiality): The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of the new Plutus primitives and case expressions across Plutus V1, V2 and V3.
- finding: Claim (technical, independently_verifiable, high materiality): The proposal links to Cardano Node 11.0.1 performance results that it says show no regressions for standard value, Plutus and voting benchmarks, and acceptable baseline performance for new Plutus primitives and case expressions.
- missing: Independent evidence for: The proposal claims native case expressions over Bool, Integer and Data in Untyped Plutus Core will provide significant performance gains and cleaner script logic.
- missing: Independent evidence for: The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of the new Plutus primitives and case expressions across Plutus V1, V2 and V3.
- missing: Independent evidence for: The proposal states that security audits have been undertaken for Plutus BLS primitives and execution costs for all Plutus primitives.
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
- finding: Strongest YES: the proposal substantiates "The action proposes upgrading Cardano mainnet from protocol version 10.0 to 11.0 through an intra-era hard fork that remains in the Conway era." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal claims native case expressions over Bool, Integer and Data in Untyped Plutus Core will provide significant performance gains and cleaner script logic." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The action proposes upgrading Cardano mainnet from protocol version 10.0 to 11.0 through an intra-era hard fork that remains in the Conway era." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal aligns with protocol evolution goals and includes checkable references for CIPs and performance results, but for a hard fork the evidence quality is still thin on the required readiness and risk dimensions: stake pool readiness is explicitly pending, audits are asserted without detail, and the reversion plan acknowledges permanence while relying on disaster recovery rather than a concrete risk register with mitigations.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Protocol action lacks a complete independently pinned readiness packet: version_guardrails_pass, testnet_results_pass, spo_readiness_pass, exchange_readiness_pass, dapp_readiness_pass, security_review_pass, constitutional_alignment_pass, rollback_or_containment_plan
- Claims and evidence missing: Independent evidence for: The proposal claims native case expressions over Bool, Integer and Data in Untyped Plutus Core will provide significant performance gains and cleaner script logic.
- Claims and evidence missing: Independent evidence for: The proposal states that testing reports demonstrate no behavioral regressions, complete conformance between specification and implementation for new ledger rules, and correct operation of the new Plutus primitives and case expressions across Plutus V1, V2 and V3.
- Claims and evidence status is thin.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.

## Reproducibility
- input_hash: `29e8f7e0d9844fc6000296a8494f08c2f450fd3f4bc0869fa1b5f117b05b6417`
- snapshot_bundle_hash: `98ab7318ab1e99e0221f08d9e41e220784bc51ebb8feb7432c9df2b72d10975a`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.445, "NO": 0.2775, "YES": 0.2775}`

