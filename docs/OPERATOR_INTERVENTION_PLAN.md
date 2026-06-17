# Agentic Intervention Plan

BEACN's DRep system should fail closed, but it must not fail silent. When the
deterministic engine cannot responsibly decide, the workflow needs a defined
lane with a concrete next action.

## Intervention Lanes

### 1. Data Failure

Use when freshness, anchor integrity, replay, or action-state checks fail.

- Default vote state: `ABSTAIN` or no submission.
- Required intervention: refresh governance data, re-fetch anchors, verify replay.
- Live voting: blocked.
- Example blocker: stale export, missing anchor hash, replay mismatch.

### 2. Action-Type Mismatch

Use when generic scoring conflicts with the governance action's real-world
meaning.

- Default vote state: no live submission until policy profile is corrected.
- Required intervention: add or revise typed policy for the action family.
- Live voting: blocked unless the revised policy regenerates a rationale and
  passes replay.
- Example blocker: treating low hard-fork turnout as active opposition.

### 3. Agentic High-Impact Directional Vote

Use when the engine produces a directional vote on an action with protocol,
constitutional, committee, or large-treasury impact.

- Default vote state: directional rationale allowed; live submission proceeds
  once deterministic gates pass.
- Required workflow: record the high-impact reason in public rationale metadata,
  inspect the strongest countercase during automated scoring, and confirm no
  private/off-chain evidence was used.
- Live voting: no mandatory operator approval variable; still requires replay,
  public rationale hash, action-live, fee-cap, and vote-only transaction gates.
- Example: clean hard-fork initiation or committeeMinSize governance-liveness
  parameter with `agentic_high_impact_reason_code`.

### 4. Research-Debt Hold

Use when the action may deserve support but the evidence packet is incomplete.

- Default vote state: `NEEDS_MORE_INFO`; near expiry, the agentic workflow may
  choose `ABSTAIN` if the missing evidence cannot be gathered in time.
- Required intervention: collect the named missing evidence into resources,
  update decision-support CSVs, rerun the engine.
- Live voting: blocked.
- Example: treasury withdrawal without a completed budget/risk/failure-mode
  dossier.

### 5. Public-Rationale Publication Block

Use when the decision is ready but the published rationale URL/hash has not been
recorded.

- Default vote state: shadow signing may be tested; live submission blocked.
- Required intervention: publish the rationale, compute the blake2b-256 hash,
  record `rationale_anchor_url` and `rationale_anchor_hash`, rerun shadow.
- Live voting: blocked until anchor gate passes.

### 6. Expiry Pressure

Use when an action expires soon and the normal research path will not finish in
time.

- Default vote state: agent chooses one of: fast-track evidence, submit
  `ABSTAIN`, or intentionally no-vote.
- Required intervention: document why speed changed the normal bar.
- Live voting: requires the same gates as any other vote.

## Immediate Operating Rules

- A generated `NO` caused only by missing generic risk fields must be reviewed
  before live use on hard forks, parameter changes, committee actions, and
  constitution actions.
- Treasury withdrawals do not get the benefit of that rule. Missing controls,
  budget clarity, milestone gates, or failure-mode analysis remain blockers.
- Network vote percentages are ratification-support context, not a substitute
  for BEACN's own judgment.
- Any policy override must be expressed as public rationale content or a
  committed policy/profile change. No private memory or chat context may become
  hidden decision evidence.

## Standard Intervention Loop

1. Build the operator queue:
   `PYTHONPATH=src python3 scripts/build_operator_intervention_queue.py`
2. For `POLICY_REVIEW`: fix typed policy or mark an intentional hold.
3. For high-impact directional votes: confirm the public rationale metadata
   records `agentic_high_impact_reason_code`.
4. For `NEEDS_RESEARCH`: add admitted public evidence in `beacn-drep-resources`
   and rerun the decision.
5. For `PUBLISH_RATIONALE`: publish/anchor the rationale before live submission.
6. Verify:
   `PYTHONPATH=src python3 -m beacn_drep.cli verify-replay --run-id <run_id>`
7. Shadow:
   `PYTHONPATH=src python3 scripts/sign_votes_shadow.py --run-dir data/output/<run_id>`
8. Live when the agentic voting policy says to proceed.
