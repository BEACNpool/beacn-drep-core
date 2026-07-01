# Rationale: gov_action1w0shrfxqwv95kk0v4cn34wylz25a2cmqkq5jpc0e2yrahhqava3q2yd5rxu
Recommendation: **NO**
Score: `-0.3333` (raw `-0.3233` + doctrine-LLM nudge `-0.01`) | Confidence: `0.8233` | Readiness: `0.0`
> Reasoning layer (codex-offline-review): Doctrine-aware offline lean for a treasury action: 7 well-supported claim(s), assessment blocked, 7 open blocker(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.010 (clamped to ±0.05).

## Plain-language explanation (codex-offline-review)
BEACN records NO on IO: Cardano High Assurance Technical Collaboration. The decisive concern is that the proposal's risks, precedent, or evidence gaps outweigh the case presented.

The action is a TreasuryWithdrawals. The cached anchor describes the request as: IO: Cardano High Assurance Technical Collaboration. The recorded treasury amount is 13.08M ADA. The strongest grounded claim is: Proposal as pdf: https://ipnso-com.ipns.dweb.link/?cid=QmQBhjELHaMKhYZjwuskHS9NRyvUdiGv69aK8C1H787c5A Cardano's strongest differentiator is its focus on security and correctness, but the tools that deliver on that promise have so far been the domain of audi...

The blocking questions are: missing complete proposal summary; missing budget analysis; missing feasibility assessment.

## Review Tree
- overall_status: `blocked`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: enacted
- finding: Proposed epoch: 626
- finding: Expires after epoch: 633
- finding: Treasury request: 13.08M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `complete`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: manifest
- finding: Deep research dossier: required
- finding: Requested: IO: Cardano High Assurance Technical Collaboration
- finding: Recipient: 
- finding: Stated amount: 13.08M ADA
- finding: Deliverables: Proposal as pdf: https://ipnso-com.ipns.dweb.link/?cid=QmQBhjELHaMKhYZjwuskHS9NRyvUdiGv69aK8C1H787c5A Cardano's strongest differentiator is its focus on security and correctness, but the tools that deliver on that promise have so far been the domain of audi..., This proposal lowers the barrier: it brings automated formal verification, and the full high-assurance toolkit, within reach of every Cardano developer., The first extends Blaster, IO's open-source automated formal verification tool, from single-script verification to full DApp-level verification., Blaster has already been used to prove correctness properties on production DApps including Djed and USDCx, and has received strong feedback from the Cardano developer community.
- finding: Deadline/expiry: not stated in document
- finding: Claim (economic, supported_in_proposal, high materiality): Proposal as pdf: https://ipnso-com.ipns.dweb.link/?cid=QmQBhjELHaMKhYZjwuskHS9NRyvUdiGv69aK8C1H787c5A Cardano's strongest differentiator is its focus on security and correctness, but the tools that deliver on that promise have so far been the domain of audi...
- finding: Claim (economic, supported_in_proposal, low materiality): This proposal lowers the barrier: it brings automated formal verification, and the full high-assurance toolkit, within reach of every Cardano developer.
- finding: Claim (economic, supported_in_proposal, low materiality): The first extends Blaster, IO's open-source automated formal verification tool, from single-script verification to full DApp-level verification.
- finding: Claim (economic, supported_in_proposal, medium materiality): Blaster has already been used to prove correctness properties on production DApps including Djed and USDCx, and has received strong feedback from the Cardano developer community.
- finding: Claim (economic, supported_in_proposal, low materiality): As an experienced Cardano smart contract developer, interested in software quality and correctness, I want access to automated formal verification tools and a fully pre-configured development environment, so that I can prove the correctness of my contracts...
- finding: Claim (technical, supported_in_proposal, low materiality): Opportunity: The Cardano ecosystem has always positioned itself as the blockchain for serious applications: financial systems, identity management, DeFi protocols, and use cases where correctness is essential.
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
- finding: Requested ADA: 13.08M ADA
- finding: Budget granularity: unknown
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: unknown
- finding: Recurring funding dependency: unknown
- finding: Six-month treasury flow regime: unknown (stale snapshot)
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
- finding: Strongest YES: the proposal substantiates "Proposal as pdf: https://ipnso-com.ipns.dweb.link/?cid=QmQBhjELHaMKhYZjwuskHS9NRyvUdiGv69aK8C1H787c5A Cardano's strongest differentiator is its focus on security and correctness, but the tools that deliver on that promise have so far been the domain of audi..." and clears the evidence gates.
- finding: Strongest NO: an unresolved blocker (missing complete proposal summary) means costs or weak controls may outweigh the claimed benefit.
- finding: Strongest hold: a treasury action without a complete deep-research dossier cannot be voted directionally without pretending certainty.
- conclusion: A defensible rationale must show the best opposing case before it reaches a vote.

### Synthesis
- status: `blocked`
- finding: Final vote must be derived from completed sections above, not from a prose summary.
- finding: The public rationale should name the decisive section and the strongest counterargument.
- missing: missing complete proposal summary
- missing: missing budget analysis
- missing: missing feasibility assessment
- missing: missing risk analysis
- missing: missing alternatives analysis
- missing: missing failure-mode analysis
- missing: missing community impact analysis
- conclusion: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Facts
- Pinned anchor document is available for this action.
- Treasury withdrawal actions require elevated scrutiny.
- Flag score present (7), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 13.08M ADA
- Risk review: Execution risk: unknown
- Counterargument pass: Strongest YES: the proposal substantiates "Proposal as pdf: https://ipnso-com.ipns.dweb.link/?cid=QmQBhjELHaMKhYZjwuskHS9NRyvUdiGv69aK8C1H787c5A Cardano's strongest differentiator is its focus on security and correctness, but the tools that deliver on that promise have so far been the domain of audi..." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- DRep ratification support is above the hard-fork threshold; treated as a positive context signal.
- Doctrine-aware reasoning layer nudged the score by -0.010 (clamped to ±0.05): Doctrine-aware offline lean for a treasury action: 7 well-supported claim(s), assessment blocked, 7 open blocker(s), treasury doctrine demands elevated scrutiny. Net bounded adjustment -0.010 (clamped to ±0.05).
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury diligence dossier incomplete; soft gate applied a -0.1 caution penalty and judged on available repo context (anchor + doctrine + reasoning lean) rather than abstaining.
- Treasury fee-flow snapshot is stale (epoch 621, ~17 epochs behind); regime treated as UNKNOWN and NOT scored. Refresh export_governance_risk_metrics.
- Claims and evidence missing: complete proposal summary
- Claims and evidence missing: budget analysis
- Treasury analysis missing: line-item budget
- Treasury analysis missing: milestone-gated disbursement
- Treasury analysis status is incomplete.
- Risk review missing: mitigation evidence
- Risk review missing: independent assurance
- Risk review status is thin.
- Synthesis missing: missing complete proposal summary
- Synthesis missing: missing budget analysis
- Synthesis status is blocked.

## Reproducibility
- input_hash: `704e8e5802925ef493269cba15cb56947be6716f93d070b7d1c165b8bd871db6`
- snapshot_bundle_hash: `19f66ef3178485e3b398aa1b3be390cd96e840e5fa111f0f1cc9320b88991a8e`
- soul_commit: `8e5afeb10af64d4e1c9708d4029f95043c3f5354`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `7d671706a9a739988611151bb93ebc1eebba6851`
- resources_used: `gov_actions_api, gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents`
- snapshot_age_seconds: `253`
- uncertainty_band: `HIGH`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.1894, "NO": 0.767, "YES": 0.0436}`

