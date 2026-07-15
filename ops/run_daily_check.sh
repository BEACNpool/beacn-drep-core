#!/usr/bin/env bash
set -euo pipefail

export BEACN_WORKSPACE="${BEACN_WORKSPACE:-$HOME/.openclaw/workspace}"
export BEACN_DREP_OFFLINE_REVIEW=1

SKILL="${BEACN_WORKSPACE}/skills/cardano-gov"
SOUL="${BEACN_WORKSPACE}/beacn-drep-soul"
RES="${BEACN_WORKSPACE}/beacn-drep-resources"
CORE="${BEACN_WORKSPACE}/beacn-drep-core"
WEB="${BEACN_WORKSPACE}/beacn-drep-web"
LOG_DIR="${BEACN_WORKSPACE}/logs"
LOCK="${LOG_DIR}/drep_daily.lock"

mkdir -p "$LOG_DIR"
exec 9>"$LOCK"
flock -n 9 || {
  echo "[$(date -u +%FT%TZ)] another drep daily check is already running"
  exit 0
}

log() { echo "[$(date -u +%FT%TZ)] $*"; }

commit_if_changed() {
  local repo="$1"
  local message="$2"
  shift 2
  git -C "$repo" add -A -- "$@"
  if git -C "$repo" diff --cached --quiet; then
    log "no changes in $(basename "$repo")"
  else
    git -C "$repo" commit -m "$message"
    if ! git -C "$repo" push origin main; then
      # A concurrent human/agent push races the automation here (root cause of the
      # 2026-07-13 outage day). Retry once on a rebased tip; never leave the repo
      # mid-rebase; never let a push failure kill the run under set -e.
      log "push rejected for $(basename "$repo"); fetch + rebase + one retry"
      if git -C "$repo" fetch origin main && git -C "$repo" rebase origin/main; then
        git -C "$repo" push origin main \
          || log "WARNING: push still failing for $(basename "$repo"); commit retained, next run retries"
      else
        git -C "$repo" rebase --abort 2>/dev/null || true
        log "WARNING: rebase conflict in $(basename "$repo"); local commit retained; manual reconcile needed"
      fi
    fi
  fi
}

publish_web_gh_pages() {
  # Self-healing gh-pages publish. Design constraints, from the 2026-07-12..15
  # outage (4 days of no publishes AND no votes):
  #   1. Crashed runs used to leak registered worktrees (cleanup ran only after a
  #      successful push under set -e); any leaked worktree holding gh-pages made
  #      every later publish die rc=128. -> prune + sweep stale worktrees at START,
  #      and cleanup ALWAYS runs (subshell, explicit rc, no early death).
  #   2. gh-pages diverged from origin when a second publisher pushed between our
  #      commit and our push -> every later push rejected non-fast-forward. -> the
  #      publish commit is ALWAYS built on origin/gh-pages' current tip (content is
  #      a full rsync of committed main HEAD, so this is order-independent), with
  #      one refetch-and-rebuild retry on rejection.
  #   3. /tmp staging dies on reboot mid-publish -> stage under ~/.cache instead.
  local staging_root="$HOME/.cache/beacn-publish"
  mkdir -p "$staging_root"
  git -C "$WEB" worktree prune 2>/dev/null || true
  local wt
  while IFS= read -r wt; do
    case "$wt" in
      "$WEB") ;;
      /tmp/tmp.*|"$staging_root"/*)
        log "removing stale publish worktree $wt"
        git -C "$WEB" worktree remove --force "$wt" 2>/dev/null || true
        ;;
    esac
  done < <(git -C "$WEB" worktree list --porcelain | awk '/^worktree /{print $2}')
  git -C "$WEB" worktree prune 2>/dev/null || true

  (
    set +e
    tmp=""
    stage="$(mktemp -d "$staging_root/stage.XXXXXX")"
    cleanup() {
      [ -n "$tmp" ] && git -C "$WEB" worktree remove --force "$tmp" 2>/dev/null
      git -C "$WEB" worktree remove --force "$stage" 2>/dev/null
      git -C "$WEB" worktree prune 2>/dev/null
      rm -rf "$tmp" "$stage" 2>/dev/null
      return 0
    }
    # Publish committed HEAD, never the working tree: unrelated local UI/source
    # edits must not leak into an automated Pages deployment.
    if ! git -C "$WEB" worktree add --detach "$stage" HEAD; then
      log "WARNING: could not stage web HEAD for gh-pages publish"
      cleanup; exit 1
    fi
    rc=1
    for attempt in 1 2; do
      git -C "$WEB" fetch origin gh-pages 2>/dev/null \
        || log "WARNING: could not fetch origin gh-pages; building on last-known tip"
      tmp="$(mktemp -d "$staging_root/ghpages.XXXXXX")"
      rmdir "$tmp"
      if ! git -C "$WEB" worktree add --detach "$tmp" origin/gh-pages; then
        log "WARNING: could not create gh-pages worktree (attempt $attempt)"
        tmp=""; continue
      fi
      rsync -a --delete --exclude .git --exclude node_modules "$stage"/ "$tmp"/
      git -C "$tmp" add -A
      if git -C "$tmp" diff --cached --quiet; then
        log "no changes in beacn-drep-web gh-pages"
        rc=0; break
      fi
      git -C "$tmp" commit -m "publish: rationale refresh $(date -u +%Y-%m-%dT%H:%M:%SZ)"
      if git -C "$tmp" push origin HEAD:gh-pages; then
        log "gh-pages published"
        # Keep the local branch ref tracking origin so nothing ever again builds
        # on a divergent local gh-pages lineage.
        git -C "$WEB" fetch origin gh-pages 2>/dev/null \
          && git -C "$WEB" branch -f gh-pages origin/gh-pages 2>/dev/null
        rc=0; break
      fi
      log "gh-pages push rejected (attempt $attempt); refetching origin tip and rebuilding"
      git -C "$WEB" worktree remove --force "$tmp" 2>/dev/null
      git -C "$WEB" worktree prune 2>/dev/null
      tmp=""
    done
    cleanup
    exit "$rc"
  )
}

ensure_source_clean() {
  local repo="$1"
  shift
  local dirty
  dirty="$(git -C "$repo" status --porcelain -- . ":(exclude)$1" 2>/dev/null || true)"
  if [ -n "$dirty" ]; then
    log "$(basename "$repo") has source/unapproved local changes; continuing without staging them"
    printf '%s\n' "$dirty"
  fi
}

log "starting BEACN DRep daily offline check"

for repo in "$SOUL" "$RES" "$CORE" "$WEB"; do
  if git -C "$repo" fetch origin --prune; then
    if git -C "$repo" status --short --branch | head -1 | grep -q "behind"; then
      # A diverged repo (concurrent manual work) must not kill the whole run under
      # set -e — that cost a full day of votes on 2026-07-13. Run from local HEAD;
      # the push-retry in commit_if_changed reconciles at publish time.
      git -C "$repo" pull --ff-only origin main \
        || log "WARNING: ff-only pull failed for $(basename "$repo") (diverged from origin?); continuing from local HEAD"
    fi
  else
    log "WARNING: GitHub fetch failed for $(basename "$repo"); continuing from pinned local HEAD"
  fi
done

ensure_source_clean "$RES" "data/"
ensure_source_clean "$CORE" "data/output/"
ensure_source_clean "$WEB" "data/output/"

if [ -d "$HOME/gov-bot-env" ]; then
  # shellcheck disable=SC1091
  source "$HOME/gov-bot-env/bin/activate"
fi

log "polling governance proposals"
cd "$SKILL"
python3 -u scripts/poll_proposals.py

log "exporting governance CSV snapshot"
cd "$CORE"
PYTHONPATH=src python3 -m beacn_drep.exporters.export_proposals_to_resources

cd "$RES"
# The poller scrapes the requested amount out of proposal metadata and sometimes gets NOTHING.
# A blank amount is not harmless: the engine cannot run capacity or cost arithmetic without it, so
# the action trips MISSING_BASELINE_EVIDENCE and ABSTAINS regardless of the evidence against it.
# That silently neutralised the two largest asks on the 2026-07-12 ballot (AlphaGrowth's 120M,
# which already had verified duplication + excessive-cost evidence, and dOSPO's 4.09M).
# The amount is on-chain in db-sync's treasury_withdrawal table -- authoritative, not scraped.
log "backfilling any missing treasury amounts from chain (relay db-sync, read-only)"
python3 scripts/backfill_treasury_amounts.py \
  || log "WARNING: treasury-amount backfill failed; actions with a blank amount will abstain"

log "refreshing cached proposal anchors"
python3 scripts/fetch_anchor_documents.py
python3 scripts/compile_action_resource_index.py

# Treasury fee-flow / risk metrics from relay db-sync (read-only). Non-fatal:
# the engine treats a stale snapshot as UNKNOWN and says so in the rationale,
# but letting it drift for weeks (epoch 621 incident) starves treasury context.
log "refreshing governance risk metrics (relay db-sync, read-only)"
python3 scripts/export_governance_risk_metrics.py \
  || log "WARNING: governance risk metrics refresh failed; engine will mark treasury flow UNKNOWN"

# Re-pin the applicable Net Change Limit from chain evidence, every cycle. The NCL is set by an
# Info action (which can never be enacted), a LATER action supersedes an earlier one for the same
# period, and the in-period spend it measures moves as withdrawals are enacted. Fails closed: if
# nothing hash-verifies, covers this epoch, and wins its vote, the previous state is left alone
# and treasury stays at NEEDS_MORE_INFO. Never invents a limit.
log "re-pinning Net Change Limit from chain evidence (relay db-sync, read-only)"
python3 scripts/pin_ncl_from_chain.py \
  || log "WARNING: NCL re-pin failed or found no qualifying action; treasury gate unchanged"

cd "$CORE"
export BEACN_DREP_LLM_CACHE="$CORE/data/output/llm_cache_active.json"
if [ "${BEACN_DREP_LLM_BACKEND:-codex}" = "none" ]; then
  log "reasoning cache refresh SKIPPED (backend=none); reusing existing cache"
else
  log "refreshing model reasoning cache (backend: ${BEACN_DREP_LLM_BACKEND:-codex}; keyless — uses Claude Code / codex OAuth, no API key)"
  if PYTHONPATH=src python3 scripts/build_drep_llm_cache.py \
       --backend "${BEACN_DREP_LLM_BACKEND:-codex}" --status active; then
    log "reasoning cache refreshed (active proposals)"
  else
    log "reasoning cache refresh failed; using prior cache + deterministic offline fallback"
  fi
fi

# Deep-research dossiers for any NEW treasury action (missing-only, so this is a
# no-op on quiet days), then the independent verification pass that can grant
# agentic approval (doctrine v1.3.0). Verification failure keeps the strict
# posture; kill switch BEACN_DOSSIER_AUTOAPPROVE_DISABLED=1.
log "drafting deep-research dossiers for new treasury actions (missing-only)"
PYTHONPATH=src python3 scripts/build_deep_research_dossiers.py \
    --backend "${BEACN_DREP_LLM_BACKEND:-codex}" --missing-only \
  || log "WARNING: dossier drafting failed; engine continues with existing rows"

log "verifying pending dossiers (independent fact-check; agentic approval on pass)"
PYTHONPATH=src python3 scripts/verify_dossiers.py \
    --backend "${BEACN_DREP_VERIFY_BACKEND:-claude}" \
  || log "WARNING: dossier verification errored; unverified dossiers stay pending (strict posture)"

log "verifying pinned independent ecosystem-value evidence"
PYTHONPATH=src python3 scripts/verify_ecosystem_value_evidence.py \
  || log "WARNING: one or more value-evidence packets failed; affected actions stay non-directional"

log "verifying pinned protocol-readiness evidence"
PYTHONPATH=src python3 scripts/verify_protocol_readiness_evidence.py \
  || log "WARNING: one or more protocol packets failed; affected actions stay ABSTAIN"

log "building treasury opportunity-cost portfolio"
PYTHONPATH=src python3 scripts/build_treasury_portfolio.py

log "updating historical policy calibration"
PYTHONPATH=src python3 scripts/calibrate_policy.py

log "running rationales for all proposals (cache where present, offline fallback elsewhere)"
PYTHONPATH=src python3 -m beacn_drep.cli run-all

log "linting rationales before publish (verdict consistency + template artifacts)"
if ! PYTHONPATH=src python3 scripts/lint_rationales.py; then
  log "RATIONALE LINT CRITICAL FAILURE — aborting publish; see data/output/lint_report.json"
  exit 1
fi

log "preparing rationale anchors and public artifacts"
PYTHONPATH=src python3 scripts/prepare_rationale_anchors.py
PYTHONPATH=src python3 -m beacn_drep.exporters.export_public_artifacts
PYTHONPATH=src python3 scripts/generate_statements.py --force
/usr/bin/python3 scripts/build_social_post_pack.py --all-open

log "running tests and replay spot-check"
PYTHONPATH=src python3 -m unittest discover -s tests
FAIL=0
while IFS= read -r run_id; do
  # Fail closed: anything other than an explicit "ok": true (mismatch, crash,
  # missing manifest) marks the spot-check failed instead of dying mid-loop.
  result="$(PYTHONPATH=src python3 -m beacn_drep.cli verify-replay --run-id "$run_id" 2>&1 || true)"
  if ! echo "$result" | grep -q '"ok": true'; then
    log "REPLAY MISMATCH/ERROR: $run_id"
    FAIL=1
  fi
done < <(python3 - <<'PY'
import csv
import pathlib

resources = pathlib.Path.home() / ".openclaw/workspace/beacn-drep-resources/data/input/governance/governance_actions_all.csv"
runs = pathlib.Path("data/output")
ids = []
with resources.open(newline="", encoding="utf-8") as f:
    ids = [r["action_id"] for r in csv.DictReader(f)]
latest = {}
for d in runs.iterdir():
    if not d.is_dir() or d.name == "public" or "-" not in d.name or not (d / "input_manifest.json").exists():
        continue
    aid = d.name.rsplit("-", 1)[0]
    if aid in ids and (aid not in latest or d.stat().st_mtime > latest[aid].stat().st_mtime):
        latest[aid] = d
active_ids = []
with resources.open(newline="", encoding="utf-8") as f:
    active_ids = [r["action_id"] for r in csv.DictReader(f)
                  if (r.get("status") or "").lower() == "active"]
for aid in active_ids:
    if aid in latest:
        print(latest[aid].name)
PY
)
if [ "$FAIL" -eq 1 ]; then
  log "replay verification failed; aborting before commits"
  exit 1
fi

# status.json only refreshes after the replay gate passes, so the email/site
# timestamp can never look fresher than what was actually verified.
cd "$CORE"
PYTHONPATH=src BEACN_WEB_REPO="$WEB" python3 scripts/update_web_status.py

log "validating public verdict consistency and scoring disclosure"
if ! PYTHONPATH=src BEACN_WEB_REPO="$WEB" python3 scripts/validate_public_consistency.py; then
  log "PUBLIC CONSISTENCY FAILURE — aborting before web sync/commit/push"
  exit 1
fi

log "syncing public artifacts to web"
cd "$WEB"
# Preserve web-only share/ cards (generated by the vote step; not present in core).
rsync -a --delete --exclude 'share' "$CORE/data/output/public/" "$WEB/data/output/public/"
python3 src/beacn_drep_web/build_backtest.py
# Share cards are cosmetic: a card failure must not block publishing verified
# artifacts or voting (that blackout is exactly what happened 2026-06-19..07-01).
# We still exit non-zero afterwards so the email says FAILED and the card gets fixed.
card_rc=0
python3 scripts/build_share_card.py --all || card_rc=$?
# (2026-07-15) The redundant public/data/output/public mirror is retired: it
# committed every artifact twice per publish and served nothing the SPA reads.

stamp="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
commit_if_changed "$RES" "data: governance snapshot ${stamp}" \
  data/input/governance data/history/governance_metrics
commit_if_changed "$CORE" "decisions: offline rationale refresh ${stamp}" \
  data/output logs/audit_log.jsonl
commit_if_changed "$WEB" "publish: rationale refresh ${stamp}" \
  status.json data/output/public

# VOTES-SAFE CHECKPOINT. Every gate that protects vote CORRECTNESS has now passed:
# rationale lint, unit tests, per-action replay verification, public-consistency
# validation, and the verified artifacts are committed. Anything that fails below
# (gh-pages mechanics, share cards) is presentation, not safety — the signing
# adapter's gate 4 still independently fetches and hash-verifies each vote's
# rationale anchor before signing, fail-closed per vote. A gh-pages failure
# suspended on-chain voting for 4 days in July 2026; that coupling was the bug.
date -u +%FT%TZ > "$LOG_DIR/drep_votes_safe.marker"

publish_rc=0
publish_web_gh_pages || publish_rc=$?
if [ "$publish_rc" -ne 0 ]; then
  log "WARNING: gh-pages publish failed after retry; public site stale until next run (voting proceeds under gate-4 anchor verification)"
fi

if [ "$card_rc" -ne 0 ]; then
  log "share card build FAILED (rc=$card_rc); verified artifacts published; voting proceeds"
  exit 2
fi
if [ "$publish_rc" -ne 0 ]; then
  exit 1
fi

log "BEACN DRep daily offline check complete"
