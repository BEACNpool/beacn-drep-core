# Rationale: fbb8d1a4a8d6b62f8cd706944a0582b884c2b90187b8fada7953d5c6a33eb5a7#0
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.78` (raw `-0.78` + doctrine-LLM nudge `-0.02`) | Confidence: `0.79` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal describes a recognizable public-benefit infrastructure use case and includes some treasury-protection mechanisms such as excess Ada return, public wallet monitoring, and repayment logic, but the deterministic assessment marks claims and evidence as thin and several high-materiality adoption and counterfactual-risk claims are proposer-asserted rather than evidenced in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge, without overriding the engine's incomplete-status handling.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because this treasury withdrawal cannot receive a directional vote until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of Eternl’s work or of the proposal’s goals.

The proposal asks for ₳2,350,000 for 12 months of Eternl operations from August 2026 through July 2027, covering frontend and backend maintenance, infrastructure, user support, governance tooling, administration, and audits of treasury fund use and oversight metrics. The proposal supports several core budget claims: it ties the request to a stated $420,000 annual operating cost, describes 6.0 FTE across 10 contributors at $70,000 per FTE, commits to converting up to $420,000 worth of Ada into stablecoins, says excess Ada would be returned to the treasury, and includes semiannual repayment assessments.

The review also found important claims that were not independently supported in the supplied evidence. Eternl’s claimed install base of about 100,000 browser-extension installs plus about 30,000 mobile installs was proposer-asserted, as was the claim that 10-18% of Cardano mainnet transactions are conducted via Eternl. The review also noted thin claims-and-evidence status, unknown execution risk, no documented milestone-gated disbursement, missing cost-benefit clarity, missing independent assurance, and no dependency map. Because this is a treasury withdrawal, BEACN applies elevated scrutiny: public-benefit use cases and treasury-protection mechanisms help, but proposer assertions alone are not enough for high-confidence spending decisions.

A directional vote would be unblocked by the pinned and independently verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the material adoption and usage claims, clearer milestone-gated disbursement, cost-benefit detail, independent assurance, and a dependency map. Until then, BEACN’s NEEDS_MORE_INFO vote avoids overstating certainty while keeping the path open for a better-evidenced decision.

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
- finding: Requested: Treasury withdrawal for 12 months of Eternl operations, maintenance, and improvements, including frontend and backend maintenance and development, backend infrastructure, user support, administration, audits, and day-to-day operations.
- finding: Recipient: Tastenkunst GmbH, Eternl
- finding: Stated amount: 2350000
- finding: Deliverables: Maintain and develop Eternl frontend across web, browser extension, Android, and iOS, Maintain backend infrastructure including nodes, indexers, application servers, metadata services, monitoring, and incident response, Provide user support through Discord, Telegram, public channels, project support, wiki updates, and educational videos, Enhance governance tooling including DRep dashboards, proposal browsers, in-wallet voting, and proposal creation, Fund periodic independent audits of treasury fund use and oversight metrics, Convert up to $420,000 worth of Ada into stablecoins, return excess Ada to the treasury, and publish monitoring/reporting information
- finding: Deadline/expiry: 12-month delivery period from August 2026 to July 2027
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a $420,000 annual operating cost for 12 months.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal funds 6.0 FTE distributed across 10 contributors at $70,000 per FTE.
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl says it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl says that if about 4.2% of its install base, roughly 5,500 users, buy the Pro plan, that income would fully cover the annual $420,000 cost.
- finding: Claim (economic, supported_in_proposal, high materiality): Eternl commits to convert up to $420,000 worth of Ada into stablecoins, place it in a public company wallet, and return any Ada above that amount to the treasury.
- finding: Claim (governance, supported_in_proposal, medium materiality): The audits allocation is for independent audits of treasury fund use and oversight metrics in February 2027 and August 2027, not for technical security audits.
- missing: Independent evidence for: Eternl says it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- missing: Independent evidence for: Eternl says that without treasury funding it may let developers go, scale down to essential maintenance, shift focus outside Cardano, or remove the free option if paid licenses are insufficient.
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
- finding: Financial confidence: 0.72
- missing: milestone-gated disbursement
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: unknown
- finding: Governance risk: medium
- finding: Technical risk: unknown
- finding: Treasury exposure risk: medium
- finding: Mitigation evidence: confirmed
- finding: Independent assurance: not confirmed
- finding: Rollback/remedy path: confirmed
- finding: Flag count: 2
- missing: independent assurance
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a $420,000 annual operating cost for 12 months." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl says it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs." — so cost or precedent may outweigh the benefit.
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
- Flag score present (3), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 2350000
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Eternl requests ₳2,350,000, valued at about $0.1787 per Ada, to cover a $420,000 annual operating cost for 12 months." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Advisory model lean was -0.020 (display cap ±0.05) and had zero influence on the binding score: The proposal describes a recognizable public-benefit infrastructure use case and includes some treasury-protection mechanisms such as excess Ada return, public wallet monitoring, and repayment logic, but the deterministic assessment marks claims and evidence as thin and several high-materiality adoption and counterfactual-risk claims are proposer-asserted rather than evidenced in the document. Under BEACN's hierarchy, treasury stewardship and evidence quality justify a small cautionary nudge, without overriding the engine's incomplete-status handling.
- Proposal clears individual quality floors but is not currently portfolio-eligible: insufficient remaining NCL capacity after higher-ranked proposals.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- Proposal requests over 50% of rolling available capacity.
- No milestone-gated disbursement documented.
- Claims and evidence missing: Independent evidence for: Eternl says it has about 100,000 browser-extension installs and about 30,000 Android and iOS installs.
- Claims and evidence missing: Independent evidence for: Eternl claims 10-18% of Cardano mainnet transactions are conducted via Eternl.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis missing: cost-benefit clarity
- Risk review missing: independent assurance
- Risk review missing: dependency map

## Reproducibility
- input_hash: `9629ea066633add03faff320bc3c64d070b51636d3ae07c5ae7d4ae6cc4c2a05`
- snapshot_bundle_hash: `5f0ea9874a19914273bae58c7c63bc006a49d9ab244554d5074e8e42490e9c7a`
- soul_commit: `d866057afd0ecaf599eb0202220b1ec8339b9b09`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `f9b6c39b6de3125c603cd6e88f7b64a571da9e8f`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `1`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4111, "NO": 0.5492, "YES": 0.0397}`

