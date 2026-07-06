# Rationale: gov_action1lwudrf9g66mzlrxhq62y5pvzhzzv9wgps7u04kne202udge7kknsqlgmhse
Recommendation: **NO**
Score: `-0.5333` (raw `-0.5033` + doctrine-LLM nudge `-0.03`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): A small negative nudge is justified because the ask is large and operational, the deterministic assessment says claims and evidence are thin, and several high-materiality adoption and usage claims are proposer-asserted rather than evidenced. The document includes useful repayment, public-wallet, and audit commitments, so the adjustment should remain modest rather than a hard negative.

## Plain-language explanation (precomputed)
BEACN voted NO because this is a large treasury withdrawal for ongoing operations, and the review found the evidence base too thin for that level of shared-ADA spending.

The proposal requested ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027, covering maintenance, development, infrastructure, support, governance tooling, and two independent audits. The proposer said this equals about $420,000 at an Ada price of $0.1787, funding 6.0 FTE across 10 contributors, and described plans for stablecoin conversion, a public company wallet, possible repayment from Pro plan income, and refunds of Ada above the $420,000 target.

Several core claims were supported in the proposal itself, including the requested amount, the 12-month delivery period, the stated annual operating cost, the planned audit dates, the Pro plan pricing, and the repayment framework. But several material claims were still only proposer-asserted or lacked independent evidence, including the custody and voting treatment of treasury-held Ada before conversion or return, the stated install base, and the claimed 10-18% share of Cardano mainnet transactions conducted via Eternl.

The review also applied elevated scrutiny because this is a treasury withdrawal. It found no milestone-gated disbursement, missing cost-benefit clarity, unknown execution risk, missing independent assurance, and no dependency map. The public-wallet, repayment, and audit commitments were useful, and the strongest YES case was that the basic funding request and delivery period were clearly stated. But for BEACN, the combination of a large operational ask, unsupported material claims, and missing treasury safeguards made the cost and precedent risk outweigh the benefits.

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
- finding: Requested: Treasury withdrawal to fund 12 months of Eternl operations, maintenance, support, infrastructure, audits/oversight, and continued development from August 2026 to July 2027.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Frontend maintenance and cross-platform development for web/PWA, browser extension, iOS, Android, beta channel, security-critical upgrades, CIP support, hardfork feature testing, multisig, dApp interoperability, app store compliance, and hardware wallet support., Backend infrastructure and operations including multi-region servers, Cardano node operation, DBSync indexers, application servers, metadata aggregation, Hub backend services, and 24/7 monitoring and incident response., User support through Discord ticketing, Telegram, bug triage, project support channels, Wiki maintenance, knowledge-base additions, and short educational videos., Governance tooling enhancements including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation in Eternl., Periodic independent audits of treasury fund use and oversight metrics in February 2027 and August 2027.
- finding: Deadline/expiry: July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $420,000 using an Ada price of $0.1787, to fund a 12-month delivery period from August 2026 to July 2027.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal says the annual operating cost is about $420,000, funding 6.0 FTE across 10 contributors at $70,000 per FTE.
- finding: Claim (governance, supported_in_proposal, high materiality): Eternl plans to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposal commits that treasury-held Ada before conversion or return will be held in an auditable account, not delegated to an SPO, and delegated to the predefined abstain voting option.
- finding: Claim (governance, supported_in_proposal, high materiality): Independent audits by a party unaffiliated with Tastenkunst GmbH or the Eternl team are planned for February 2027 and August 2027 to review receipt, custody, conversion, spending, balances, Pro plan income relevant to repayment, and refunds or repayments.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl says it will introduce Pro plans priced at $96 per year for Personal and $360 per year for Company users, and that about 5,500 users, or 4.2% of its stated install base, would cover the $420,000 annual cost.
- missing: Independent evidence for: The proposal commits that treasury-held Ada before conversion or return will be held in an auditable account, not delegated to an SPO, and delegated to the predefined abstain voting option.
- missing: Independent evidence for: The proposal states Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- missing: Independent evidence for: The proposal claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 2350000
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: not confirmed
- finding: Clawback/refund path: confirmed
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using an Ada price of $0.1787, to fund a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposal commits that treasury-held Ada before conversion or return will be held in an auditable account, not delegated to an SPO, and delegated to the predefined abstain voting option." — so cost or precedent may outweigh the benefit.
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
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $420,000 using an Ada price of $0.1787, to fund a 12-month delivery period from August 2026 to July 2027." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.030 (clamped to ±0.05): A small negative nudge is justified because the ask is large and operational, the deterministic assessment says claims and evidence are thin, and several high-materiality adoption and usage claims are proposer-asserted rather than evidenced. The document includes useful repayment, public-wallet, and audit commitments, so the adjustment should remain modest rather than a hard negative.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: The proposal commits that treasury-held Ada before conversion or return will be held in an auditable account, not delegated to an SPO, and delegated to the predefined abstain voting option.
- Claims and evidence missing: Independent evidence for: The proposal states Eternl has about 100,000 browser-extension installs and about 30,000 installs across Android and iOS.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `2483163f03237d213b8324ae93e769fafb69d0074a6deb853fc9af41f9e2ef6f`
- snapshot_bundle_hash: `13fd785405085c1a67a013a051d0d31880bbb10ba86d67b0dfe146c078bdefc7`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `0ea81023446b54880e1eea7818c2845a8b5e6f8e`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1758, "NO": 0.7845, "YES": 0.0397}`

