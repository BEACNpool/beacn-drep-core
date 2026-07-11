# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4633` (raw `-0.4633` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal describes useful wallet infrastructure and includes repayment, audit, and transparency mechanisms, but the deterministic assessment says claims and evidence are thin, and several high-materiality adoption and dependency claims remain proposer-asserted. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Eternl’s usefulness or a judgment on the team.

The proposal requests ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027. It says the funds would cover about $420,000 in annual operating costs across 6.0 FTE, backend infrastructure, support, governance tooling, and cross-platform wallet maintenance. Several financial terms were supported in the proposal, including the stated budget, the stablecoin conversion plan, the public company wallet, planned February 2027 and August 2027 audits of treasury fund use, and semiannual repayment or donation assessments if paid Pro plans produce surplus income.

The review found that some high-materiality claims remained only proposer-asserted. In particular, the stated install counts, the claim that 5,500 Pro users would cover the annual cost, and the claim that 10-18% of Cardano mainnet transactions are conducted through Eternl lacked independent replayable evidence in the supplied review. The review also noted thin claims-and-evidence status, stressed treasury-flow conditions, no documented milestone-gated disbursement, missing cost-benefit clarity, missing independent assurance, and no dependency map.

The anchor document was pinned and replayable, baseline intake passed, and the strongest YES case was acknowledged: the proposal substantiates the requested amount and the annual operating-cost rationale. But treasury withdrawals require elevated scrutiny because they spend shared ADA and set precedent. A directional vote would be unblocked by a pinned and independently verified Net Change Limit from public chain evidence, plus independent evidence for the major adoption and usage claims and clearer treasury safeguards such as milestone-gated disbursement, cost-benefit clarity, independent assurance, and a dependency map.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 637
- finding: Expires after epoch: 644
- finding: Treasury request: 2.35M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, and improvements while Eternl introduces paid Pro plans intended to replace treasury support.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for web, browser extension, iOS, Android, and beta channels, Backend infrastructure and operations including nodes, DBSync indexers, application servers, metadata aggregation, monitoring, and incident response, User support through Discord ticketing, Telegram, public channels, ecosystem support, wiki updates, and educational videos, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Periodic independent audits of treasury fund use and oversight metrics in February 2027 and August 2027, Introduction of paid Eternl Pro plans and semiannual treasury repayment or donation assessments
- finding: Deadline/expiry: 12-month delivery period, August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual operating costs for August 2026 through July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs, and about 5,500 Pro users would fully cover the stated $420,000 annual cost.
- finding: Claim (economic, supported_in_proposal, high materiality): After withdrawal, Eternl says it will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, supported_in_proposal, high materiality): The audits allocation is for independent audits of treasury fund use and oversight metrics, not technical security audits, with audits planned for February 2027 and August 2027 by a party unaffiliated with Tastenkunst GmbH or the Eternl team.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl commits to semiannual repayment assessments where surplus treasury stablecoins plus paid plan income above $420,000 would be repaid until $420,000 worth of Ada has been returned, followed by possible additional donations capped at $210,000 worth of Ada.
- missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs, and about 5,500 Pro users would fully cover the stated $420,000 annual cost.
- missing: Independent evidence for: Eternl says 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl states it has provided multi-platform Cardano access with basically zero downtime for over five years.
- missing: Independent evidence for: If treasury funding is not approved and paid plans do not sell enough licenses beyond August, Eternl says it may let developers go, scale down to essential maintenance, shift focus outside Cardano, remove the free option, and reduce support and infrastructure resilience.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.74
- missing: milestone-gated disbursement
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
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual operating costs for August 2026 through July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs, and about 5,500 Pro users would fully cover the stated $420,000 annual cost." — so cost or precedent may outweigh the benefit.
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
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover approximately $420,000 in annual operating costs for August 2026 through July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal describes useful wallet infrastructure and includes repayment, audit, and transparency mechanisms, but the deterministic assessment says claims and evidence are thin, and several high-materiality adoption and dependency claims remain proposer-asserted. Under BEACN doctrine, treasury stewardship and evidence quality justify a small cautionary nudge rather than a positive adjustment.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 Android and iOS installs, and about 5,500 Pro users would fully cover the stated $420,000 annual cost.
- Claims and evidence missing: Independent evidence for: Eternl says 10-18% of Cardano mainnet transactions are conducted via Eternl.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity

## Reproducibility
- input_hash: `b13ff24b1c499108ca110632cf2fc7da59cd8ff406880a54cacc7c8527a10b43`
- snapshot_bundle_hash: `4ab28cb13fb20c5f8b811d2f7e8d83be0d78f4a65a17d7171cde708b52d2850f`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `98204209c1160292d57e948cc03515956c20be3e`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

