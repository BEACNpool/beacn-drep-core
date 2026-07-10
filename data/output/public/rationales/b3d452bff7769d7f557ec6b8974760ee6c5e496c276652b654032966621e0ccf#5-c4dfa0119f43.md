# Rationale: b3d452bff7769d7f557ec6b8974760ee6c5e496c276652b654032966621e0ccf#5
Recommendation: **ABSTAIN**
Score: `0.0` (raw `0.0` + doctrine-LLM nudge `+0.0`) | Confidence: `0.1` | Readiness: `0`


## Plain-language explanation (precomputed)
BEACN voted ABSTAIN because the review was blocked by missing baseline evidence for a treasury withdrawal, specifically the missing `treasury_amount_lovelace` field. This is a conservative, evidence-based hold, not a judgment that the Mithril work is bad or that the request should fail.

The action requested 3,810,423 ada from the treasury for continued Mithril Protocol development and Intersect administration. The proposal says this includes 3,699,440 ada for Mithril continuous development and 110,983 ada for Intersect’s administration fee, with audit, oversight, reporting obligations, and milestone-based disbursement controls. That budget breakdown was supported in the proposal, the proposal anchor was pinned and replayable, the Intersect Budget Process Hydra vote was reported as meeting the required 67% support threshold, and the request was found not to breach the 350M Net Change Limit at submission.

However, several parts of the review did not reach the evidence bar needed for a directional treasury vote. The intake and synthesis were blocked because the required treasury amount field was missing. Claims about Mithril’s technical function and strategic alignment still lacked independent evidence in the review. The treasury analysis was incomplete because sustainability path and cost-benefit clarity were missing, and the risk review remained unknown because independent assurance and a rollback or remedy path were missing.

A YES vote would require treating an incomplete review record as sufficient, and a NO vote would go beyond what the evidence established. The specific evidence that would unblock a directional vote is a complete treasury withdrawal baseline, including `treasury_amount_lovelace`, plus independent support for the key technical and alignment claims, clearer cost-benefit and sustainability analysis, and documented independent assurance with a remedy path.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `blocked`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 638
- finding: Expires after epoch: 645
- finding: Treasury request: not specified
- finding: Anchor pinned locally: yes
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Mithril Protocol continued development and associated Intersect administration.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor.
- finding: Stated amount: 3,810,423
- finding: Deliverables: Mithril Protocol Continuous Development, Intersect Budget Administration fee, Audit, oversight, reporting obligations, and milestone-based disbursement controls
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests a total of 3,810,423 ADA, consisting of 3,699,440 ADA for Mithril Protocol Continuous Development and 110,983 ADA for Intersect Budget Administration fee.
- finding: Claim (technical, proposer_asserted, high materiality): Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- finding: Claim (governance, proposer_asserted, medium materiality): The proposer claims full alignment with Infrastructure & Research Excellence and Adoption & Utility, and partial alignment with Community & Ecosystem Growth.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase.
- finding: Claim (economic, independently_verifiable, high materiality): The requested amount does not, at time of submission, on its own or in aggregate, breach the 350M Net Change Limit covering Epoch 613 to Epoch 713.
- finding: Claim (governance, proposer_asserted, high materiality): Audit and oversight costs are included in the overhead, and independent oversight will be provided through Intersect and technically capable third parties with reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- missing: Independent evidence for: The proposer claims full alignment with Infrastructure & Research Excellence and Adoption & Utility, and partial alignment with Community & Ecosystem Growth.
- missing: Independent evidence for: Audit and oversight costs are included in the overhead, and independent oversight will be provided through Intersect and technically capable third parties with reporting obligations and milestone-based disbursement controls.
- missing: Independent evidence for: Teragone has not previously received direct funding from Cardano treasury or community governance programs, but has worked on Mithril for several years through IOG-funded collaboration.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 0
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.58
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
- finding: Flag count: 0
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "The proposal requests a total of 3,810,423 ADA, consisting of 3,699,440 ADA for Mithril Protocol Continuous Development and 110,983 ADA for Intersect Budget Administration fee." though 1 review blocker(s) remain open.
- finding: Strongest NO: a material claim is unsupported — "Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: treasury_amount_lovelace is missing for a treasury withdrawal
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Critical evidence fields are missing for this action.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 0
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests a total of 3,810,423 ADA, consisting of 3,699,440 ADA for Mithril Protocol Continuous Development and 110,983 ADA for Intersect Budget Administration fee." though 1 review blocker(s) remain open.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce a responsible recommendation without baseline evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Intake status is blocked.
- Claims and evidence missing: Independent evidence for: Mithril uses stake-based threshold multi-signatures to certify Cardano state in a trustless way, enabling nodes and applications to verify state rapidly without relying on the entire chain.
- Claims and evidence missing: Independent evidence for: The proposer claims full alignment with Infrastructure & Research Excellence and Adoption & Utility, and partial alignment with Community & Ecosystem Growth.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path
- Synthesis missing: treasury_amount_lovelace is missing for a treasury withdrawal
- Synthesis status is blocked.

## Missing Evidence
- treasury_amount_lovelace is missing for a treasury withdrawal

## Reproducibility
- input_hash: `c4dfa0119f43c74a1a225db1cdb49337b3b24ee7beecf3db58d0f16f71eefb1f`
- snapshot_bundle_hash: `65f6d1fc0d7982cf402b975d7831830e925e5ff64b2e6df21230f0decd36b734`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `3`
- uncertainty_band: `LOW`
- evidence_depth_score: `3`
- decision_probs: `{"ABSTAIN": 0.345, "NO": 0.3275, "YES": 0.3275}`

