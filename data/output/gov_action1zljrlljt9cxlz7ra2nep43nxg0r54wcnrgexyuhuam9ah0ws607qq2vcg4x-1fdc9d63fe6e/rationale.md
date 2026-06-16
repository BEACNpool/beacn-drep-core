# Rationale: gov_action1zljrlljt9cxlz7ra2nep43nxg0r54wcnrgexyuhuam9ah0ws607qq2vcg4x
Recommendation: **ABSTAIN**
Score: `0.0` | Confidence: `0.0` | Readiness: `0`

## Plain-language explanation (precomputed)
BEACN's autonomous DRep is recording ABSTAIN on this action, and the reason is procedural rather than a verdict on the proposal's merits. BEACN's on-chain governance data snapshot is currently about eight hours old, which is beyond the six-hour freshness limit its policy requires before it will cast a directional vote. When data is this stale BEACN holds rather than risk voting on an out-of-date picture of the proposal, the treasury, and the wider vote distribution. At about 18.26 million ADA this is one of the largest live treasury actions, funding Tweag by Modus Create to deliver core protocol infrastructure — chiefly the mainnet deployment of Peras for faster finality, plus History Expiry and conformance testing. The technical need is well-documented: Peras v1 is genuinely not yet on mainnet and the work it describes is real. The budget is transparently derived from a stated hourly rate and ADA/USD assumption, which is good practice, but the rate, the hours and the single-pipeline framing are proposer-set figures that warrant independent cost scrutiny at this scale. A request of this size demands a completed deep-research dossier, milestone-gated disbursement and a clear view of treasury runway — exactly the checks BEACN cannot complete on an eight-hour-old snapshot. It is therefore holding until the data is fresh and that evidence is in hand.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 634
- finding: Expires after epoch: unknown
- finding: Treasury request: 18.26M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: Fund Tweag by Modus Create to deliver 3 interdependent work packages of core infrastructure, centred on mainnet deployment of Peras (faster finality), plus History Expiry and conformance testing
- finding: Recipient: Tweag by Modus Create
- finding: Stated amount: 18,263,496 ADA (stated USD $4,565,874)
- finding: Deliverables: Peras v1 production cryptography, KillSwitch and mainnet readiness, History Expiry / partial-history nodes, Conformance testing and correctness scaffolding
- finding: Deadline/expiry: 2026-2027 delivery window
- finding: Claim (technical, supported_in_proposal, high materiality): Peras v1 (faster finality, ~2 min vs ~12 min) remains undeployed on mainnet and requires production cryptography and hard-fork readiness
- finding: Claim (technical, proposer_asserted, medium materiality): The 3 work packages are interdependent and should be funded as a single delivery pipeline, not a modular menu
- finding: Claim (economic, proposer_asserted, high materiality): The 18,263,496 ADA ask is based on $176/hour senior-engineer rates and a conservative 0.25 ADA/USD conversion
- finding: Claim (economic, proposer_asserted, medium materiality): Peras and Leios are required to unlock higher transaction volume, staking rewards and TVL
- missing: Independent evidence for: The 3 work packages are interdependent and should be funded as a single delivery pipeline, not a modular menu
- missing: Independent evidence for: The 18,263,496 ADA ask is based on $176/hour senior-engineer rates and a conservative 0.25 ADA/USD conversion
- missing: Independent evidence for: Peras and Leios are required to unlock higher transaction volume, staking rewards and TVL
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
- finding: Requested ADA: 18.26M ADA
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
- finding: Strongest YES: the proposal substantiates "Peras v1 (faster finality, ~2 min vs ~12 min) remains undeployed on mainnet and requires production cryptography and hard-fork readiness" and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The 3 work packages are interdependent and should be funded as a single delivery pipeline, not a modular menu" — so cost or precedent may outweigh the benefit.
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
- Treasury analysis: Requested ADA: 18.26M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Peras v1 (faster finality, ~2 min vs ~12 min) remains undeployed on mainnet and requires production cryptography and hard-fork readiness" and clears the evidence gates.
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
- Claims and evidence missing: Independent evidence for: The 3 work packages are interdependent and should be funded as a single delivery pipeline, not a modular menu
- Claims and evidence missing: Independent evidence for: The 18,263,496 ADA ask is based on $176/hour senior-engineer rates and a conservative 0.25 ADA/USD conversion
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
- input_hash: `1fdc9d63fe6e3b1ad618dd7968c1e38080ad7b170fb792da20dbd1df8a9451e2`
- snapshot_bundle_hash: `7f18c391fb6dc9c680b838db57682ed8f4948191a9f2b3d7acdd2faf1a0672f0`
- soul_commit: `a0d3b8b59ec356b6a4733bb8a0822326604b0766`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7da435ff32d6151125006e6138bc2da8eb0bcfc4`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `29349`
- uncertainty_band: `LOW`
- evidence_depth_score: `2`
- decision_probs: `{"ABSTAIN": 0.32, "NO": 0.34, "YES": 0.34}`

- **DATA STALE**: age exceeded threshold

