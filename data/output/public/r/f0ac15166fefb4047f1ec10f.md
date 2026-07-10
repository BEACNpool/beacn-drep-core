# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4633` (raw `-0.4633` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal has a plausible public-benefit case for maintaining a widely used Cardano wallet and includes repayment, refund, and audit commitments, but the evidence quality remains thin for the size of the treasury ask: install base, transaction share, FTE need, conversion controls, auditor identity, and Pro-plan uptake are mostly asserted in the document. Under BEACN doctrine, treasury stewardship and evidence quality outweigh ecosystem growth when a large spend depends on non-verified adoption and revenue assumptions, so a small cautionary negative nudge is justified beyond the mechanical assessment.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Eternl or its public-benefit case.

The action requests ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027, including frontend and backend maintenance, infrastructure, support, governance tooling, audits, reporting, and continued development while Eternl introduces paid Pro plans. The proposal says this equals about $420,000 in annual operating cost, allocates the funds across frontend, backend, support, admin, and audits, and includes commitments around public wallets, stablecoin conversion, refunds, repayments, Pro-plan income reporting, and audits in February 2027 and August 2027.

Several core claims were supported by the proposal itself, including the requested amount, the budget allocation, the repayment structure, and the planned Pro pricing. But other important claims were still mostly proposer assertions rather than independently verified evidence, including the 6.0 FTE staffing need, install base, transaction-share claims, conversion controls, auditor identity, and expected Pro-plan uptake. The review also noted thin claims-and-evidence status, no documented milestone-gated disbursement, missing cost-benefit clarity, missing independent assurance, and an unknown execution-risk profile.

The review gates established that the proposal anchor was pinned and replayable, and the strongest YES case was acknowledged: Eternl presented a plausible request to fund a widely used Cardano wallet with repayment, refund, audit, and reporting commitments. But because this is a large treasury withdrawal, BEACN applies elevated scrutiny. A directional YES or NO would require the verified Net Change Limit from public chain evidence, plus stronger independent support for the major cost, adoption, conversion, assurance, and delivery claims.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, audits, and continued development while Eternl introduces paid Pro plans.
- finding: Recipient: Tastenkunst GmbH / Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: 12 months of frontend and backend maintenance and development, Backend infrastructure and operations including multi-region servers, Cardano node operation, indexers, app servers, metadata aggregation, monitoring, and incident response, User support through Discord, Telegram, public channels, ecosystem project support, wiki updates, and educational videos, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and governance proposal creation, Eternl Core rewrite, Eternl Hub features, enhanced hardware wallet support, mobile Bluetooth hardware wallet support, and enhanced wallet data export, Periodic independent audits of treasury fund use in February 2027 and August 2027, Public reporting of balances, conversion rates, transaction hashes, Pro plan earnings, repayment hashes, refunds, and repayments
- finding: Deadline/expiry: 12-month delivery period, August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover an estimated $420,000 annual operating cost for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal allocates the ask as ₳1,292,500 frontend, ₳587,500 backend, ₳117,500 support, ₳305,500 admin, and ₳47,000 audits.
- finding: Claim (economic, proposer_asserted, high materiality): The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (economic, proposer_asserted, high materiality): Eternl will convert up to $420,000 worth of Ada into stablecoins in a public company wallet and return any Ada above that amount to the treasury.
- finding: Claim (economic, supported_in_proposal, high materiality): Every December and June, Eternl will use surplus remaining treasury stablecoins plus paid plan income above $420,000 to repay the treasury until $420,000 in Ada has been repaid, and later donate 50% of paid-plan income above $420,000 until an additional $210,000 in Ada has been donated.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl plans Personal and Company Pro plans at $96/year and $360/year, and asserts that about 5,500 paying users, about 4.2% of its stated install base, would cover the $420,000 annual cost.
- missing: Independent evidence for: The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- missing: Independent evidence for: Eternl will convert up to $420,000 worth of Ada into stablecoins in a public company wallet and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl states it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- missing: Independent evidence for: Eternl states that 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover an estimated $420,000 annual operating cost for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl asks for ₳2,350,000, valued at about $0.1787 per Ada, to cover an estimated $420,000 annual operating cost for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): The proposal has a plausible public-benefit case for maintaining a widely used Cardano wallet and includes repayment, refund, and audit commitments, but the evidence quality remains thin for the size of the treasury ask: install base, transaction share, FTE need, conversion controls, auditor identity, and Pro-plan uptake are mostly asserted in the document. Under BEACN doctrine, treasury stewardship and evidence quality outweigh ecosystem growth when a large spend depends on non-verified adoption and revenue assumptions, so a small cautionary negative nudge is justified beyond the mechanical assessment.
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
- Claims and evidence missing: Independent evidence for: The proposal funds 6.0 FTE across 10 contributors at $70,000 per FTE.
- Claims and evidence missing: Independent evidence for: Eternl will convert up to $420,000 worth of Ada into stablecoins in a public company wallet and return any Ada above that amount to the treasury.
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
- snapshot_bundle_hash: `2b6ba7c6c37c81167d4469c8eadaac5a517f7b4f18ca5bdd608a53f9233e9efb`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `1016d41a520361eb8cc704812b2053b147b40d14`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

