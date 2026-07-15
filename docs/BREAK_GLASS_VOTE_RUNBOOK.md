# Break-Glass Vote Runbook

The manual path for when the daily pipeline is red and a governance action is
approaching expiry. Everything here runs the SAME code the automation runs —
break-glass means an operator drives it by hand, not that any safety gate is
skipped. All commands run on **midnight** (`ssh midnight-ops`, user
`ubuntudesktop`) unless noted; paths assume
`WS=~/.openclaw/workspace` and `cd $WS/beacn-drep-core`.

Companion docs: `docs/OPERATOR_INTERVENTION_PLAN.md` (which lane you are in),
`docs/SIGNING_GATES.md` (what the adapter enforces), `SECURITY.md`
(incident response — if you suspect credential compromise, freeze automation
per its steps before doing anything below).

## 1. Triage — find out what is actually broken

```bash
ssh midnight-ops
WS=~/.openclaw/workspace

# The whole daily run (check + vote + email) logs here:
tail -100 $WS/logs/drep_daily.log

# Vote-step specifics:
tail -50 $WS/logs/drep_vote_pytest.log      # test preflight result
tail -50 $WS/logs/drep_vote_stderr.log      # vote runner stderr
python3 -m json.tool $WS/beacn-drep-core/data/output/last_vote_run.json | head -60

# VOTES-SAFE marker: timestamp of the last run where every vote-CORRECTNESS
# gate passed (lint, tests, replay, public consistency, artifacts committed).
# If this is recent, a red pipeline is a PRESENTATION failure (gh-pages, share
# cards) and voting is still safe.
cat $WS/logs/drep_votes_safe.marker

# Leaked gh-pages worktrees killed publishing for 4 days in July 2026.
# run_daily_check.sh now self-heals these at start, but check anyway:
git -C $WS/beacn-drep-web worktree list

# Is a run already in flight? The daily check holds this flock:
ls -la $WS/logs/drep_daily.lock

# What the public sees (generated_at should be < ~30h old):
curl -s https://beacnpool.github.io/beacn-drep-web/status.json | python3 -c \
  'import json,sys; d=json.load(sys.stdin); print(d["generated_at"], d["last_check"]["summary"])'
```

How much runway does the action have? `status.json` lists open actions;
`data/output/<run-id>/rationale.json` records the action's expiry epoch where
known. Epoch math: epoch E starts at unix `1596059091 + (E-208)*432000`;
epochs are 5 days.

## 2. Run the daily check manually

The full wrapper (check + gated vote + email report) is what cron runs at
06:30 CT:

```bash
ssh midnight-ops
~/.openclaw/workspace/ops/run_drep_daily_with_signal.sh
```

To run the check WITHOUT the vote step (e.g. you want to inspect the fresh
rationales before anything can sign):

```bash
cd ~/.openclaw/workspace/beacn-drep-core
BEACN_AUTOVOTE_DISABLED=1 ~/.openclaw/workspace/ops/run_drep_daily_with_signal.sh
# or the check script alone (no email, no vote):
ops/run_daily_check.sh
```

Notes that will bite you if ignored:
- The wrapper exports `PATH="$HOME/.local/bin:$PATH"` because the reasoning /
  dossier stage shells out to the `claude` and `codex` binaries there. Running
  `run_daily_check.sh` directly from a bare cron-like environment silently
  starves every evidence gate and abstains the whole ballot (this has happened
  twice). An interactive login shell on midnight already has the right PATH.
- The check exits early on rationale-lint failure, replay mismatch, or
  public-consistency failure — those are CORRECTNESS aborts; do not work
  around them, fix the cause and rerun.
- Exit code 2 = share-card failure only; artifacts were verified and
  published, voting is safe.

## 3. Run the vote step alone

Safe to run standalone at any time — it re-runs the full pytest suite before
any signing, and the signing adapter independently enforces all 8 gates per
vote (see `docs/SIGNING_GATES.md`), fail-closed:

```bash
cd ~/.openclaw/workspace/beacn-drep-core
ops/run_daily_vote.sh
```

What it does: pytest preflight (refuses to vote on failure), waits
`BEACN_AUTOVOTE_PAGES_WAIT` (default 90s) for GitHub Pages so gate 4 can fetch
freshly published anchors, then runs
`BEACN_VOTING_LIVE=1 PYTHONPATH=src python3 scripts/run_live_votes.py --live`,
writes the JSON audit to `data/output/last_vote_run.json`, and refreshes the
web status + share cards if anything was submitted.

To preview what it WOULD do without submitting anything (shadow — builds and
signs, never broadcasts):

```bash
PYTHONPATH=src python3 scripts/run_live_votes.py | python3 -m json.tool
```

## 4. Vote a single action

`scripts/run_live_votes.py` has exactly ONE flag: `--live`. There is no
per-action flag — it always evaluates the latest run for every active action,
and the vote-policy debounce (HOLD/NOOP) plus gate 7 (already-voted /
inactive) skip everything that should not be touched. Two real narrowing
levers exist:

- `BEACN_AUTO_DIRECTIONS` (env, default `YES,NO,ABSTAIN`) — restrict which
  recommendation directions may submit this run, e.g.
  `BEACN_AUTO_DIRECTIONS=ABSTAIN ops/run_daily_vote.sh`.
- `BEACN_MAX_VOTES_PER_RUN` (default 3) — lower it to 1 to guarantee at most
  one submission: `BEACN_MAX_VOTES_PER_RUN=1 ops/run_daily_vote.sh`.

For one specific action, target its run directory through the shadow runner,
which drives the same guarded adapter (`prepare_vote`) directly:

```bash
cd ~/.openclaw/workspace/beacn-drep-core
# Find the latest run directory for the action:
ls -dt data/output/<action_tx_hash>#<ix>-* | head -1

# ALWAYS shadow first — full gate report, builds + signs, submits nothing:
PYTHONPATH=src python3 scripts/sign_votes_shadow.py --run-dir data/output/<run-id>

# Only if the shadow report shows every gate true and the expected
# action/direction, go live:
BEACN_VOTING_LIVE=1 PYTHONPATH=src python3 scripts/sign_votes_shadow.py --live --run-dir data/output/<run-id>
```

Caveats of the single-action lane:
- It bypasses the vote-policy debounce ledger (persistence/hysteresis), so use
  it only when expiry pressure genuinely justifies skipping the anti-churn
  layer — and say so in the record you keep (Intervention Lane 6 requires
  documenting why speed changed the bar).
- It does NOT bypass any adapter gate. If a gate blocks, the vote is wrong to
  cast, not merely inconvenient.
- The vote lands in `vote_receipt.json` inside the run dir and in the
  vote-time snapshot ledger; the next daily run's gov-state scan sees the
  on-chain vote, so nothing double-votes (gate 7 blocks same-direction
  re-votes).

Verify after: `data/output/<run-id>/vote_receipt.json` has
`"status": "submitted"` and a `transaction_hash`; the tx appears on-chain;
the next `update_web_status.py` run reflects it.

## 5. Kill switches

| Switch | Effect |
|---|---|
| `BEACN_AUTOVOTE_DISABLED=1` | `ops/run_daily_vote.sh` exits before anything signs. THE kill switch. |
| `BEACN_AUTO_DIRECTIONS=...` | Narrow submittable directions (e.g. `ABSTAIN` only). |
| `BEACN_MAX_VOTES_PER_RUN=0` | Adapter gate 8 blocks every vote this run. |
| `BEACN_DOSSIER_AUTOAPPROVE_DISABLED=1` | Dossier verification cannot grant agentic approval (strict posture). |
| `BEACN_DREP_LLM_BACKEND=none` | Daily check skips the reasoning-cache refresh; deterministic offline fallback only. |
| Remove `BEACN_VOTING_LIVE=1` / omit `--live` | Adapter stops at `shadow_signed`; nothing is ever broadcast. |

For a durable freeze (not just one run), set the kill switch in the cron
wrapper's environment or comment out the `run_daily_vote.sh` call — and record
it. Suspected key/credential compromise → `SECURITY.md` incident response:
revoke, freeze automation that can publish or vote, publish an incident note,
re-run from trusted commits.

## 6. What NEVER to do

- **Never hand-build a vote with `cardano-cli` outside the adapter.** The
  adapter (`src/beacn_drep/adapters/cardano_cli_adapter.py`) is the only path
  that enforces vote-only tx contents, the pure-lovelace input filter (a
  LEDGER_SCROLLS token sits at the fee address and must never be spent), the
  fee cap, the anchor, and strict action-id parsing. A hand-built tx has none
  of that, and voting on the wrong action is the worst failure this system has.
- **Never bypass gate 4** (published rationale reachable + hash match). A vote
  without a verifiable public rationale anchor breaks the transparency
  contract the whole system exists for. If the anchor is the blocker, publish
  the rationale properly (Intervention Lane 5), don't stub the check.
- **Never hand-edit files inside a run directory**
  (`data/output/<run-id>/rationale.json`, `input_manifest.json`, …). Replay
  verification (gate 3) and the anchor hash (gate 4) hash exactly these bytes;
  editing them either blocks the vote or, worse, forges the record. A wrong
  verdict is fixed by fixing evidence/policy and regenerating, never by
  editing outputs.
- **Never vote a `NEEDS_MORE_INFO`** by relabeling it. Weak or stale evidence
  → ABSTAIN through the engine, or no vote.
- **Never run with secrets in new places.** Signing keys stay in
  `~/.secrets/cardano/beacn-drep-cli/`; nothing in this runbook requires
  touching, copying, or printing them.
