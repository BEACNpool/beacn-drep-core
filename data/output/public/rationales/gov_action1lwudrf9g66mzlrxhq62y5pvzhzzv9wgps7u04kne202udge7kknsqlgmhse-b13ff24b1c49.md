# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.4633` (raw `-0.4633` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small negative nudge is justified because the ask is large and operational, the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and ecosystem-impact claims are proposer-asserted rather than evidenced in the document. The repayment, audit, and public-wallet commitments improve stewardship but do not fully offset the evidence gap for a treasury withdrawal of this size.

## Plain-language explanation (deterministic-heuristic)
BEACN records NEEDS_MORE_INFO on Eternl: Path to Sustainability - v2. This is an evidence hold, not opposition: BEACN cannot make a directional treasury judgment from the current record.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: 12 months of operations, maintenance, support, infrastructure, audits/oversight metrics, and continued development for the Eternl Cardano light wallet. It asks the treasury for 2350000 ADA. The strongest grounded claim is: Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.

A material claim remains proposer-asserted or thinly supported: Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS. Reason code: VERIFIED_NCL_REQUIRED.

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
- finding: Requested: 12 months of operations, maintenance, support, infrastructure, audits/oversight metrics, and continued development for the Eternl Cardano light wallet.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for browser extension, web/PWA, iOS, Android, and beta channel, Backend infrastructure and operations including multi-region servers, Cardano node operation, DBSync indexers, application servers, metadata aggregation, Hub backend services, and monitoring, User support through Discord ticketing, Telegram, public community channels, project support, wiki maintenance, and educational videos, Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Independent audits of treasury fund use and oversight metrics in February 2027 and August 2027
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (adoption, supported_in_proposal, high materiality): Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳2,350,000, calculated at about $0.1787 per Ada, to cover approximately $420,000 in annual costs.
- finding: Claim (economic, supported_in_proposal, high materiality): The funded work covers 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- finding: Claim (economic, supported_in_proposal, high materiality): If roughly 5,500 users, or about 4.2% of the stated install base, buy the planned Pro plan, that income would fully cover the annual $420,000 cost.
- finding: Claim (economic, supported_in_proposal, high materiality): The team will convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: Treasury-fund-use audits will be performed by an independent party unaffiliated with Tastenkunst GmbH or the Eternl team in February 2027 and August 2027.
- missing: Independent evidence for: Eternl says 10-18% of Cardano mainnet transactions are conducted via Eternl.
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
- finding: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl is a non-custodial Cardano light wallet available on web, browser extension, Android, and iOS." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): A small negative nudge is justified because the ask is large and operational, the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and ecosystem-impact claims are proposer-asserted rather than evidenced in the document. The repayment, audit, and public-wallet commitments improve stewardship but do not fully offset the evidence gap for a treasury withdrawal of this size.
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
- Claims and evidence missing: Independent evidence for: Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- Claims and evidence missing: Independent evidence for: Treasury-fund-use audits will be performed by an independent party unaffiliated with Tastenkunst GmbH or the Eternl team in February 2027 and August 2027.
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
- snapshot_bundle_hash: `7d7dd9cc314efdd5a115a69af192bffe89c041b4b4aaf24a1b716d037d215a14`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `ef21df7fcecbb56f66c12028d9c7dafb58b68c52`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `4`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

