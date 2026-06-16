# Rationale: gov_action1ngpqafax5rvp8lcgey4asvqtycrh4e56fwp8cn2r9trx2ysryhtsqdm3w3z
Recommendation: **ABSTAIN**
Score: `0.0` | Confidence: `0.0` | Readiness: `0`

## Plain-language explanation (precomputed)
BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is procedural rather than a verdict on the proposal's merits. BEACN's on-chain governance data snapshot is currently about eight hours old, which is beyond the six-hour freshness limit its policy requires before it will cast a directional vote. When data is this stale BEACN holds rather than risk voting on an out-of-date picture of the proposal, the treasury, and the wider vote distribution. Eternl requests about 1.68 million ADA — roughly $420,000 — to fund a year of operations and maintenance for its widely used non-custodial wallet while it stands up a paid Pro plan intended to make it self-sustaining. The proposal's strength is that it names a concrete path off treasury funding: it estimates that around 5,500 Pro subscribers, about 4.2% of its install base, would cover annual costs. That conversion assumption is the load-bearing claim and is currently the proposer's projection rather than demonstrated revenue, and the install-base figures are self-reported. The amount is modest relative to other live actions and the public good of a maintained, widely used wallet is real. The directional question is the credibility of the sustainability plan and whether funding is staged against it. BEACN is holding only because its data snapshot is stale; once fresh, this is a tractable case.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 631
- finding: Expires after epoch: unknown
- finding: Treasury request: 1.68M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Fund 12 months of operations, maintenance and improvements for the Eternl non-custodial Cardano wallet while it transitions toward a paid Pro plan
- finding: Recipient: Eternl
- finding: Stated amount: 1,680,000 ADA (stated ≈$420,000/year)
- finding: Deliverables: 12 months of frontend/backend maintenance and development, Backend infrastructure and user support, Launch of a paid Pro plan toward self-sustainability
- finding: Deadline/expiry: 12-month period (2026-2027)
- finding: Claim (adoption, proposer_asserted, high materiality): Eternl serves about 100,000 browser-extension users and ~30,000 across Android and iOS
- finding: Claim (economic, proposer_asserted, high materiality): Roughly 5,500 Pro subscribers (≈4.2% of the install base) would fully cover the ~$420,000 annual cost
- finding: Claim (economic, supported_in_proposal, medium materiality): Annual operating cost is around $420,000 (~1,680,000 ADA)
- finding: Claim (adoption, proposer_asserted, medium materiality): Eternl is a primary gateway for Cardano payments, staking, governance and DApp interaction
- missing: Independent evidence for: Eternl serves about 100,000 browser-extension users and ~30,000 across Android and iOS
- missing: Independent evidence for: Roughly 5,500 Pro subscribers (≈4.2% of the install base) would fully cover the ~$420,000 annual cost
- missing: Independent evidence for: Eternl is a primary gateway for Cardano payments, staking, governance and DApp interaction
- missing: complete proposal summary
- missing: budget analysis
- missing: feasibility assessment
- missing: risk analysis
- missing: alternatives analysis
- missing: failure-mode analysis
- missing: community impact analysis
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1.68M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unsustainable
- finding: Financial confidence: unknown
- missing: line-item budget
- missing: milestone-gated disbursement
- missing: sustainability path
- missing: cost-benefit clarity
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `thin`
- finding: Execution risk: unknown
- finding: Governance risk: unknown
- finding: Technical risk: unknown
- finding: Treasury exposure risk: unknown
- finding: Mitigation evidence: unknown
- finding: Independent assurance: unknown
- finding: Rollback/remedy path: unknown
- finding: Flag count: 2
- missing: mitigation evidence
- missing: independent assurance
- missing: rollback/remedy path
- missing: dependency map
- conclusion: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.

### Counterargument pass
- status: `complete`
- finding: Strongest YES: the proposal substantiates "Annual operating cost is around $420,000 (~1,680,000 ADA)" and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "Eternl serves about 100,000 browser-extension users and ~30,000 across Android and iOS" — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: freshness gate failed
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Data freshness check failed: data is 29349s old, max allowed is 21600s
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 1.68M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Annual operating cost is around $420,000 (~1,680,000 ADA)" and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Cannot produce reliable recommendation with stale data.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- All scoring suspended until fresh data is available.
- Claims and evidence missing: Independent evidence for: Eternl serves about 100,000 browser-extension users and ~30,000 across Android and iOS
- Claims and evidence missing: Independent evidence for: Roughly 5,500 Pro subscribers (≈4.2% of the install base) would fully cover the ~$420,000 annual cost
- Claims and evidence status is thin.
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: freshness gate failed
- Synthesis missing: missing complete proposal summary
- Synthesis status is blocked.

## Reproducibility
- input_hash: `27d6f94059b3b5d3308135541e451e4ae0aac103402a041d2cd7d635e606c5de`
- snapshot_bundle_hash: `e6c423d78c8426efc515f58ade6de5c6fa479fb7652770f10f607ccf27c82408`
- soul_commit: `a0d3b8b59ec356b6a4733bb8a0822326604b0766`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7da435ff32d6151125006e6138bc2da8eb0bcfc4`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `29349`
- uncertainty_band: `LOW`
- evidence_depth_score: `2`
- decision_probs: `{"ABSTAIN": 0.32, "NO": 0.34, "YES": 0.34}`

- **DATA STALE**: age exceeded threshold

