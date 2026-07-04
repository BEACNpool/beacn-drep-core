# Rationale: gov_action1k02990lhw6wh74t7c6ufw3mqaek9ujtvyan99dj5qv5kvcs7pn8syhyg4hw
Recommendation: **NO**
Score: `-0.3733` (raw `-0.3533` + doctrine-LLM nudge `-0.02`) | Confidence: `0.6633` | Readiness: `0.85`
> Reasoning layer (precomputed): The proposal has stronger-than-thin process evidence, on-chain administration details, oversight descriptions, and checkable references, but the deterministic assessment marks treasury analysis incomplete and the document does not provide enough cost benchmarking or vendor-specific delivery evidence to fully satisfy treasury stewardship concerns for a 1.31M ADA withdrawal. A small cautionary negative nudge is justified because the doctrine prioritizes treasury stewardship and evidence quality over plausible ecosystem benefit.

## Plain-language explanation (precomputed)
BEACN voted NO because this was a large treasury withdrawal and the evidence did not fully meet the higher stewardship bar for spending 1,310,960 ada. The strongest concern was that the need for continuous maintenance was asserted, but not independently supported enough to show that the requested cost and precedent were justified.

The action requested funding for 12 months of Cardano hardware-wallet maintenance in 2026, including Ledger and Trezor compatibility updates, supporting libraries and `cardano-hw-cli`, developer support, integration support, vendor-required audits, and capped time-and-materials reporting. The proposal clearly stated the amount, the recipient treasury reserve smart-contract stake address, the split between 1,272,777 ada for maintenance and 38,183 ada for Intersect administration, and that the work was maintenance and compatibility support rather than a new wallet product.

Several parts were well supported: the anchor document was pinned and replayable, the budget amount was clear, the proposal included on-chain administration details through Intersect and Sundae Labs treasury contracts, and it described oversight, milestone controls, reporting obligations, and prior related funding references. However, key claims remained thin or unsupported, especially the claim that Cardano, Ledger, or Trezor changes could otherwise break secure hardware-wallet access, and the claim that the work aligned with Cardano strategy goals. The treasury review was also incomplete, with missing cost-benefit clarity and no sustainability path, while the risk review lacked independent assurance and a rollback or remedy path.

BEACN recognized the strongest YES case: hardware-wallet maintenance is plausibly useful, the requested amount was clearly disclosed, and the proposal included process evidence and oversight structures. But treasury withdrawals require elevated scrutiny because they spend shared ada, and the review found an incomplete diligence dossier, an unsustainable treasury-flow signal, unknown execution risk, and a confidence-reducing flag score. On the evidence available, BEACN’s conservative conclusion was NO.

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
- finding: Deep research dossier: required
- finding: Requested: Treasury withdrawal to fund Hardware Wallet Maintenance 2026 for Cardano hardware-wallet support.
- finding: Recipient: 2026 Treasury Reserve Smart Contract stake address stake1784sdxt6jjennmstphgdu7l7c2scf5d02a6cve2dgn5s2kq5u3j9v, submitted by Intersect on behalf of the vendor
- finding: Stated amount: 1,310,960
- finding: Deliverables: 12 months of production maintenance of Cardano hardware-wallet support, Ledger and Trezor compatibility updates, Maintenance of supporting interoperability libraries and cardano-hw-cli, Developer support for ecosystem integrators, Support for integration paths involving externally maintained components where shared hardware-wallet flows intersect, Vendor-required product or security audits where firmware or app changes trigger them, Transparent capped time-and-materials reporting with milestones and evidence
- finding: Deadline/expiry: 12 months during 2026
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests 1,310,960 ADA, consisting of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee.
- finding: Claim (technical, supported_in_proposal, high materiality): The funded work is limited to hardware-wallet compatibility, security, supporting libraries and tooling, release support, and vendor-required audit work, and is not intended to build a new wallet product.
- finding: Claim (technical, proposer_asserted, high materiality): The proposer claims continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise break secure hardware-wallet access for users and integrators.
- finding: Claim (governance, independently_verifiable, high materiality): The proposal says the requested amount did not, at submission, breach the 350M ADA Net Change Limit covering Epoch 613 to Epoch 713, and links to the relevant governance action.
- finding: Claim (governance, independently_verifiable, medium materiality): The proposal states it achieved the required 67% support threshold during the 2026 Intersect Budget Process Hydra Voting phase and provides references to voting, documentation, audited results, and an audit report.
- finding: Claim (technical, independently_verifiable, high materiality): Funds are to be administered through Intersect using Sundae Labs treasury management smart contracts, with stated TRSC and PSSC addresses and a public dashboard for auditability.
- missing: Independent evidence for: The proposer claims continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise break secure hardware-wallet access for users and integrators.
- missing: Independent evidence for: The proposer claims the work aligns with Cardano strategy Pillar 1 for security, reliability, and interoperability and secondarily with Pillar 2 for adoption, secure UX, developer experience, and tooling compatibility.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `incomplete`
- finding: Requested ADA: 1310960
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: confirmed
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: unsustainable (basis: total inflow (tau + donations) vs enacted withdrawals)
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
- finding: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA, consisting of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The proposer claims continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise break secure hardware-wallet access for users and integrators." — so cost or precedent may outweigh the benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
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
- Counterargument pass: Strongest YES: the proposal substantiates "The proposal requests 1,310,960 ADA, consisting of 1,272,777 ADA for Cardano Hardware Wallet Maintenance & Compatibility Assurance and 38,183 ADA for the Intersect Budget Administration fee." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is material but below threshold; treated as a modest context signal.
- Doctrine-aware reasoning layer nudged the score by -0.020 (clamped to ±0.05): The proposal has stronger-than-thin process evidence, on-chain administration details, oversight descriptions, and checkable references, but the deterministic assessment marks treasury analysis incomplete and the document does not provide enough cost benchmarking or vendor-specific delivery evidence to fully satisfy treasury stewardship concerns for a 1.31M ADA withdrawal. A small cautionary negative nudge is justified because the doctrine prioritizes treasury stewardship and evidence quality over plausible ecosystem benefit.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury flow signal is in unsustainable regime, ratio 2.28 (total inflow (tau + donations) vs enacted withdrawals); advisory penalty applied.
- Claims and evidence missing: Independent evidence for: The proposer claims continuous maintenance is needed because Cardano, Ledger, or Trezor changes could otherwise break secure hardware-wallet access for users and integrators.
- Claims and evidence missing: Independent evidence for: The proposer claims the work aligns with Cardano strategy Pillar 1 for security, reliability, and interoperability and secondarily with Pillar 2 for adoption, secure UX, developer experience, and tooling compatibility.
- Claims and evidence status is thin.
- Treasury analysis missing: sustainability path
- Treasury analysis missing: cost-benefit clarity
- Treasury analysis status is incomplete.
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Reproducibility
- input_hash: `e4ddbd06228bd62ba5753858f360b46313a47822caeb615fc3e186eaa1c04e73`
- snapshot_bundle_hash: `c5a4cfb3713c3b32ebfa75067fdefc8486bd14cd5a8e8c750553d0bd9fdbed1e`
- soul_commit: `6831a5e0ecdb429fd793fe9b865f94a0af9b0e31`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `3a194b6032448cec2eb7ae69ff68fc7e02a22fe7`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers`
- snapshot_age_seconds: `31`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.2033, "NO": 0.7538, "YES": 0.0429}`

