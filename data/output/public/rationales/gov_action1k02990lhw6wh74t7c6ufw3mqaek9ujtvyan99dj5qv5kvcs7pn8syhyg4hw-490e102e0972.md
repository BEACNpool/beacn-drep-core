# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8syhyg4hw
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims describe maintenance of a security-critical access layer, include independently checkable governance-process and NCL references, and specify smart-contract custody plus multi-party oversight controls. The nudge remains small because several core benefit and breakage-risk claims are proposer asserted rather than evidenced inside the document.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the hardware-wallet work.

The action requests 1,310,960 ada for 2026 hardware-wallet maintenance, including Ledger and Trezor compatibility updates, supporting libraries, cardano-hw-cli, developer support, release support, vendor-required audits, reporting, and milestone-based disbursement controls. The proposal says 1,272,777 ada is for maintenance and compatibility assurance, with 38,183 ada for Intersect budget administration. It also says funds would be administered through Intersect’s Treasury Reserve Smart Contract and a project-specific smart contract, with oversight by Intersect, technically capable third parties, an Oversight Committee, reporting obligations, and milestone controls.

Several governance and custody claims were reviewable: the proposal anchor was pinned and replayable, the requested amount was clearly stated, the Intersect budget-process support claim came with references, and the smart-contract custody and multi-party oversight structure were described. But several benefit and risk claims were still too thin for a treasury vote. The review did not have independent evidence that the work is 12 months of continuity maintenance for an already-proven hardware-wallet access layer, or independent evidence that Cardano, Ledger, or Trezor changes would otherwise break secure access for users and integrations. The review also flagged missing sustainability path, cost-benefit clarity, independent assurance, and rollback or remedy path.

The review gates therefore produced a hold: the intake and pinned anchor were sufficient to review the action, and the strongest YES case was that the amount and basic scope were substantiated. But treasury actions require elevated scrutiny because they spend shared ada and set precedent. A directional vote would be unblocked by pinned, independently verifiable public-chain evidence for the relevant Net Change Limit, plus stronger independent evidence for the maintenance need, breakage risk, cost-benefit case, assurance plan, and remedy path.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 1.31M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support, compatibility, tooling, release support, developer support, supporting libraries, cardano-hw-cli, and vendor-required audit work.
- finding: Recipient: Intersect Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 1,310,960
- finding: Deliverables: 12 months of production maintenance of Cardano hardware-wallet support, Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting, milestone evidence, and milestone-based disbursement controls
- finding: Deadline/expiry: 2026 funding period; specific completion deadline not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for hardware wallet maintenance and compatibility assurance and 38,183 ada for the Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): The work is framed as 12 months of continuity maintenance for an already-proven Cardano hardware-wallet access layer rather than a new wallet product.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer says continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise break secure access for users and integrations.
- finding: Claim (technical, proposer_asserted, medium materiality): The proposed scope is limited to hardware-wallet compatibility, tooling, vendor-required assurance, supporting libraries, release support, and developer support, and the document says it does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that it achieved the required 67% support threshold in the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting records, documentation, final audited results, and an audit report.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal states that the requested amount did not, at submission, breach the applicable 350M ada Net Change Limit covering Epoch 613 to Epoch 713, and links the referenced NCL governance action.
- missing: Independent evidence for: The work is framed as 12 months of continuity maintenance for an already-proven Cardano hardware-wallet access layer rather than a new wallet product.
- missing: Independent evidence for: The proposer says continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise break secure access for users and integrations.
- missing: Independent evidence for: The proposed scope is limited to hardware-wallet compatibility, tooling, vendor-required assurance, supporting libraries, release support, and developer support, and the document says it does not duplicate broader core-node, ledger, or general infrastructure maintenance budgets.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 1310960
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.62
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for hardware wallet maintenance and compatibility assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The work is framed as 12 months of continuity maintenance for an already-proven Cardano hardware-wallet access layer rather than a new wallet product." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 1310960
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ada, consisting of 1,272,777 ada for hardware wallet maintenance and compatibility assurance and 38,183 ada for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was +0.020 (display cap ±0.05) and had zero influence on the binding score: A small positive nudge is justified because the claims describe maintenance of a security-critical access layer, include independently checkable governance-process and NCL references, and specify smart-contract custody plus multi-party oversight controls. The nudge remains small because several core benefit and breakage-risk claims are proposer asserted rather than evidenced inside the document.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The work is framed as 12 months of continuity maintenance for an already-proven Cardano hardware-wallet access layer rather than a new wallet product.
- Claims and evidence missing: Independent evidence for: The proposer says continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise break secure access for users and integrations.
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
- input_hash: `490e102e09724620dece1c1c765d389b5ea15874acb635fa0cb0568f3c51c469`
- snapshot_bundle_hash: `2d84d7348f5deeb978bb185c45101ece8d6b7d2ef12689768c2853d1c9c9ac3c`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

