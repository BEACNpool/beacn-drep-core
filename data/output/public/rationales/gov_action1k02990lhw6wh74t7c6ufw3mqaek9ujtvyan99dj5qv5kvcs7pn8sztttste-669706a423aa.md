# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8sztttste
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2133` (raw `-0.2133` + doctrine-LLM nudge `+0.02`) | Confidence: `0.7733` | Readiness: `0.85`
> Reasoning layer (precomputed): A small positive nudge is justified because the claims show public-benefit developer infrastructure, open-source maintenance, checkable repository and budget-process references, NCL compliance, and described custody/oversight controls; the nudge remains small because the anchor gives only a coarse work-package budget and some delivery-history claims are proposer asserted.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this is a treasury withdrawal, and a directional vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Dolos or TxPipe.

The action asks to withdraw 540,750 ada to fund Year 2 of Dolos maintenance by TxPipe, through the Intersect treasury reserve smart contract stake address. The proposal says this includes 525,000 ada for maintenance and enhancement plus a 15,750 ada administration fee. It describes 12 months of part-time maintenance, dependency updates, Cardano protocol compatibility, performance work, bug fixes, issue triage, contribution review, developer communication, and AI-friendly documentation resources.

Several important claims were supported well enough for review: the pinned anchor document was available and replayable, the requested amount and budget split were substantiated, the technical description of Dolos and the proposed work scope were supported in the proposal, and the proposal provided references for Intersect Budget Process support and stated NCL compliance. But other claims were thinner: the Strategic Pillar alignment claim and TxPipe delivery-history claim lacked independent evidence in the review, and the treasury review was missing sustainability-path and cost-benefit clarity. Risk review also lacked independent assurance and a clear rollback or remedy path.

The evidence that would unblock a directional vote is public, replayable verification of the applicable Net Change Limit from chain evidence, plus stronger independent support for the missing governance and delivery-history claims, clearer cost-benefit and sustainability analysis, and a firmer remedy path if delivery problems arise. Until then, BEACN held at NEEDS_MORE_INFO to avoid overstating certainty on a shared-treasury spend.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: 540.8k ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Fund Dolos by TxPipe: Maintaining Cardano's Lightweight Data Node, Year 2, including maintenance, enhancement, community support, and AI-friendly documentation resources.
- finding: Recipient: Intersect treasury reserve smart contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v on behalf of TxPipe as vendor
- finding: Stated amount: 540750
- finding: Deliverables: Part-time maintainer for Dolos over 12 months, Dependency updates, Cardano protocol compatibility, performance improvements, bug fixing, and documentation, Issue triage, review of external contributions, ecosystem-feedback enhancements, and public developer communication, AI-friendly documentation and integration resources for AI-driven development workflows
- finding: Deadline/expiry: 12 months; grant period begins after closure of the existing contract
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect Budget Administration fee.
- finding: Claim (economic, supported_in_proposal, high materiality): The motivation states the maintenance grant includes 420,000 ADA plus a 105,000 ADA contingency reserve to fund a part-time Dolos maintainer over 12 months at an annual rate of $105,000 USD.
- finding: Claim (technical, supported_in_proposal, high materiality): Dolos is described as a Rust lightweight Cardano data node that connects directly to the Cardano network, indexes ledger primitives, and exposes Mini-Blockfrost, UTxO-RPC, Mini-Kupo, and Ouroboros N2C interfaces.
- finding: Claim (adoption, independently_verifiable, medium materiality): The proposal says Dolos has 939 commits, 80 releases, 129 stars, 51 forks, and 27 contributors, and links to the Dolos GitHub repository.
- finding: Claim (technical, supported_in_proposal, high materiality): The proposed work scope covers essential codebase maintenance, community support, and AI-friendly documentation and integration resources.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source incentives.
- missing: Independent evidence for: The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source incentives.
- missing: Independent evidence for: The proposal says TxPipe has received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, and also received 2025 Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC that is being delivered on schedule.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 540750
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.68
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source incentives." — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 540750
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 540,750 ADA total, consisting of 525,000 ADA for Dolos maintenance and enhancement plus a 15,750 ADA Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by +0.020 (clamped to ±0.05): A small positive nudge is justified because the claims show public-benefit developer infrastructure, open-source maintenance, checkable repository and budget-process references, NCL compliance, and described custody/oversight controls; the nudge remains small because the anchor gives only a coarse work-package budget and some delivery-history claims are proposer asserted.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Claims and evidence missing: Independent evidence for: The proposal asserts Dolos aligns with Intersect Strategic Pillar 2 focus area A.3 for Developer Experience and open-source incentives.
- Claims and evidence missing: Independent evidence for: The proposal says TxPipe has received funding through 30 Project Catalyst proposals, with 26 delivered and 4 under development and on schedule, and also received 2025 Intersect open-source maintenance funding for Pallas, Dolos, and UTxO RPC that is being delivered on schedule.
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
- input_hash: `669706a423aa13b99df39c7de461593e9749783b36c1b1805dce75bae79ef2d4`
- snapshot_bundle_hash: `f9331fb38aaba2e369e17f4b3aee77eec6c14040afa6365d1b431913bafdda84`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `2`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.5033, "NO": 0.4477, "YES": 0.049}`

