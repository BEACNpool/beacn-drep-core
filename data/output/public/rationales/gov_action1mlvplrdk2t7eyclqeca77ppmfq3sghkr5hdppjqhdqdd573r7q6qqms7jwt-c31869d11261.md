# Rationale: gov_action1mlvplrdk2t7eyclqeca77ppmfq3sghkr5hdppjqhdqdd573r7q6qqms7jwt
Recommendation: **NEEDS_MORE_INFO**
Score: `-0.2433` (raw `-0.2433` + doctrine-LLM nudge `-0.03`) | Confidence: `0.7808` | Readiness: `0.8`
> Reasoning layer (precomputed): The proposal describes a potentially high-public-benefit BTC liquidity rail, but the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and economic claims remain asserted or only externally checkable rather than evidenced in the supplied text. Given the large treasury request and security-sensitive bridge scope, the bounded lean should apply a modest caution nudge rather than reward plausible ecosystem upside.

## Plain-language explanation (precomputed)
BEACN voted NEEDS_MORE_INFO because a directional treasury vote is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence. This is a conservative, evidence-based hold, not a rejection of the Bifrost idea.

The proposal asks for ₳12,332,031 for Phase 1 of a Bitcoin-Cardano bridge, delivered over nine months from July 2026 to March 2027. It says Phase 1 would produce an audited bridge running on Cardano mainnet in both federated and SPO-threshold custody modes under controlled access, with hardening, audits, formal verification, partner readiness, stewardship work, and economic foundations before a separate Phase 2 public rollout.

Several core technical claims were supported in the proposal: Bifrost is described as a permissionless Bitcoin-Cardano bridge, fBTC is described as issued and burned 1:1 against locked BTC, custody is described as distributed across 400+ Cardano SPOs, and the proposal states there is no bridge token or founder allocation. The review also found the anchor document pinned and replayable, and the strongest YES case cleared the evidence gates. But some material adoption and economic claims remained only asserted or externally checkable, including the Bitcoin market-size and DeFi-use claim, and the Q2 2029 targets for BTC TVL, transactions, and fBTC wallets.

The gates that held the vote back were evidence and treasury-risk gates. Treasury withdrawals require a higher bar because they spend shared ADA, and this review also flagged high execution risk, thin claims-and-evidence status, missing milestone-gated disbursement detail, missing independent assurance, and no clear rollback or remedy path. To unblock a YES or NO vote, BEACN would need the verified Net Change Limit from public chain evidence, plus stronger replayable evidence for the material adoption and economic claims and clearer treasury controls for disbursement, assurance, and remedies.

## Review Tree
- overall_status: `incomplete`

### Intake
- status: `complete`
- finding: Action type: TreasuryWithdrawals
- finding: Status: active
- finding: Proposed epoch: 640
- finding: Expires after epoch: 647
- finding: Treasury request: 12.33M ADA
- finding: Anchor pinned locally: yes
- conclusion: Baseline fields and source anchors establish whether the proposal can be reviewed at all.

### Claims and evidence
- status: `thin`
- finding: Proposal anchor: pinned and replayable
- finding: Proposal document read by reasoning layer: yes
- finding: Snapshot freshness source: deep_research_dossiers.csv
- finding: Deep research dossier: complete
- finding: Requested: Phase 1 of 2 for Bifrost, a Bitcoin-Cardano bridge, covering launch readiness work including hardening, security audits, formal verification, ecosystem and partner readiness, stewardship, and economic foundations.
- finding: Recipient: FluidTokens and Lantr Engineering
- finding: Stated amount: 12332031
- finding: Deliverables: Audited bridge running on Cardano mainnet in both federated and SPO threshold custody modes under controlled access by the end of Phase 1, Hardening, security audits, and formal verification, Ecosystem and partner readiness, Stewardship structure and hardened economic model required for public launch, SPO/dApp partner pipeline required for public launch
- finding: Deadline/expiry: 9-month delivery period from July 2026 to March 2027
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset.
- finding: Claim (economic, supported_in_proposal, high materiality): The proposal requests ₳12,332,031, approximately $1,973,125 at 0.16 USD/ADA, including a 10% refundable contingency, for a 9-month Phase 1 delivery period.
- finding: Claim (technical, supported_in_proposal, high materiality): Phase 1 is intended to produce an audited bridge running on Cardano mainnet in federated and SPO-threshold custody modes under controlled access before a separate Phase 2 public rollout and operations proposal in Q1 2027.
- finding: Claim (adoption, proposer_asserted, medium materiality): The document claims Bitcoin represents roughly $1.6 trillion in value and that only around 1% of BTC supply is currently used in DeFi.
- finding: Claim (technical, independently_verifiable, medium materiality): The document claims DeFiLlama historical loss data shows cumulative DeFi losses in the billions, with bridge-related failures accounting for a significant share.
- finding: Claim (technical, supported_in_proposal, high materiality): Bifrost custody is described as distributed across 400+ Cardano SPOs weighted by delegation, with fund movement requiring a cryptographic threshold representing the majority of delegated stake.
- missing: Independent evidence for: The document claims Bitcoin represents roughly $1.6 trillion in value and that only around 1% of BTC supply is currently used in DeFi.
- missing: Independent evidence for: The proposal targets by Q2 2029 a base contribution of 1,200 BTC in TVL, about 600,000 annual transactions, and 3,000 fBTC-holding wallets.
- conclusion: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.

### Treasury analysis
- status: `complete`
- finding: Requested ADA: 12332031
- finding: Budget granularity: confirmed
- finding: Milestone payment gates: unknown
- finding: Clawback/refund path: unknown
- finding: Cost/benefit clarity: confirmed
- finding: Recurring funding dependency: confirmed
- finding: Six-month treasury flow regime: stressed (basis: total inflow (tau + donations) vs enacted withdrawals)
- finding: Financial confidence: 0.78
- missing: milestone-gated disbursement
- conclusion: Treasury votes require a higher bar because they consume shared ADA and create precedent.

### Risk review
- status: `complete`
- finding: Execution risk: high
- finding: Governance risk: medium
- finding: Technical risk: high
- finding: Treasury exposure risk: high
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
- finding: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." and clears the evidence gates.
- finding: Strongest NO: a material claim is unsupported — "The document claims Bitcoin represents roughly $1.6 trillion in value and that only around 1% of BTC supply is currently used in DeFi." — so cost or precedent may outweigh the benefit.
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
- Flag score present (4), reducing confidence.
- Intake: Action type: TreasuryWithdrawals
- Claims and evidence: Proposal anchor: pinned and replayable
- Treasury analysis: Requested ADA: 12332031
- Risk review: Execution risk: high
- Counterargument pass: Strongest YES: the proposal substantiates "Bifrost is designed as a permissionless Bitcoin-Cardano bridge secured by Cardano's existing SPO ecosystem that brings BTC onto Cardano as a native Cardano asset." and clears the evidence gates.
- Synthesis: Final vote must be derived from completed sections above, not from a prose summary.

## Inferences
- Advisory model lean was -0.030 (display cap ±0.05) and had zero influence on the binding score: The proposal describes a potentially high-public-benefit BTC liquidity rail, but the deterministic assessment marks claims and evidence as thin, and several high-materiality adoption and economic claims remain asserted or only externally checkable rather than evidenced in the supplied text. Given the large treasury request and security-sensitive bridge scope, the bounded lean should apply a modest caution nudge rather than reward plausible ecosystem upside.
- Directional treasury voting is blocked until the applicable Net Change Limit is pinned and independently verified from public chain evidence.
- Intake: Baseline fields and source anchors establish whether the proposal can be reviewed at all.
- Claims and evidence: Each claim must map to replayable public evidence; proposer assertions alone are not enough for confidence.
- Treasury analysis: Treasury votes require a higher bar because they consume shared ADA and create precedent.
- Risk review: Risk is not a side note; unmitigated execution or governance risk can dominate an otherwise attractive proposal.
- Counterargument pass: A defensible rationale must show the best opposing case before it reaches a vote.
- Synthesis: The vote is only credible if the assessment tree shows enough work for a skeptical delegator to audit.

## Uncertainty
- Treasury flow signal is in stressed regime (total inflow (tau + donations) vs enacted withdrawals).
- DRep ratification support is below threshold; this is not treated as active opposition.
- Claims and evidence missing: Independent evidence for: The document claims Bitcoin represents roughly $1.6 trillion in value and that only around 1% of BTC supply is currently used in DeFi.
- Claims and evidence missing: Independent evidence for: The proposal targets by Q2 2029 a base contribution of 1,200 BTC in TVL, about 600,000 annual transactions, and 3,000 fBTC-holding wallets.
- Claims and evidence status is thin.
- Treasury analysis missing: milestone-gated disbursement
- Risk review missing: independent assurance
- Risk review missing: rollback/remedy path

## Missing Evidence
- independent ecosystem-value evidence packet
- verified ecosystem benefit or strategic necessity
- delivery controls, milestones, assurance, or remedy path

## Reproducibility
- input_hash: `c31869d1126149cb19b18718209277982ba9989fbc89f038a7523d22c858de31`
- snapshot_bundle_hash: `bf7bc0d45be3c8968f44da5a587d58a1e2247e2e9a469623270260d59278f8c5`
- soul_commit: `204e26c8230587b4b4df20eeb0a8485d478b54a9`
- soul_text_hash: `a8c48e8e59534bbaa71af9a923ef942aa2cda51cb9e259331cef24e0da27ae10`
- resource_registry_commit: `e3acb15e16a35828f6fc5c72eadf18669f12e080`
- resources_used: `gov_actions_snapshot, treasury_withdrawals_snapshot, drep_vote_history_snapshot, gov_actions_all_snapshot, gov_actions_active_snapshot, gov_treasury_recipients_snapshot, gov_action_flags_snapshot, gov_poll_runs_snapshot, top_drep_votes_snapshot, gov_anchor_documents, deep_research_dossiers, ecosystem_value_profiles, treasury_policy_state, treasury_portfolio, governance_outcomes, protocol_readiness_profiles`
- snapshot_age_seconds: `0`
- uncertainty_band: `MEDIUM`
- evidence_depth_score: `4`
- decision_probs: `{"ABSTAIN": 0.4902, "NO": 0.4622, "YES": 0.0476}`

