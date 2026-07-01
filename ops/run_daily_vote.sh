#!/usr/bin/env bash
# Daily gated on-chain vote step. Runs AFTER run_daily_check.sh, which has
# already generated rationales, recorded + published rationale anchors, refreshed
# status.json, and pushed the web bundle.
#
# Policy (fully agentic, fail-closed):
#   * Auto-submits any votable recommendation (YES/NO/ABSTAIN) that passes all 8
#     adapter gates, and revises an existing on-chain vote when the recommendation
#     changes (latest agentic recommendation wins). No operator-review gate.
#   * Narrow with BEACN_AUTO_DIRECTIONS (default "YES,NO,ABSTAIN").
#   * The signing adapter independently enforces all 8 gates and fails closed.
#
# Disable by removing the call from run_drep_daily_with_signal.sh or setting
# BEACN_AUTOVOTE_DISABLED=1.
set -uo pipefail

WS="${BEACN_WORKSPACE:-$HOME/.openclaw/workspace}"
CORE="$WS/beacn-drep-core"
WEB="$WS/beacn-drep-web"
LOG_DIR="$WS/logs"
mkdir -p "$LOG_DIR"
log() { echo "[$(date -u +%FT%TZ)] $*"; }

if [ "${BEACN_AUTOVOTE_DISABLED:-0}" = "1" ]; then
  log "autovote disabled via BEACN_AUTOVOTE_DISABLED=1; skipping"
  exit 0
fi

cd "$CORE" || exit 1

# Anchors were published by run_daily_check moments ago; give Pages time to deploy
# so gate 4 (fetch + hash the public rationale) can pass for freshly published ones.
sleep "${BEACN_AUTOVOTE_PAGES_WAIT:-90}"

log "running gated fully-agentic auto-vote (YES/NO/ABSTAIN + revisions; adapter gates enforced)"
# stderr goes to its own log so stray warnings can never corrupt the JSON audit file.
report="$(BEACN_VOTING_LIVE=1 PYTHONPATH=src python3 scripts/run_live_votes.py --live 2>>"$LOG_DIR/drep_vote_stderr.log")"
if printf '%s' "$report" | python3 -m json.tool >/dev/null 2>&1; then
  printf '%s\n' "$report" > "data/output/last_vote_run.json"
else
  log "vote runner produced non-JSON output; see $LOG_DIR/drep_vote_stderr.log (audit file left untouched)"
fi
submitted="$(printf '%s' "$report" | python3 -c "import json,sys
try: print(json.load(sys.stdin).get('submitted',0))
except Exception: print('?')" 2>/dev/null)"
log "auto-vote submitted=$submitted"

if [ "${submitted:-0}" = "0" ]; then
  log "no new votes cast; nothing to publish"
  exit 0
fi

log "refreshing web status + share cards after $submitted vote(s)"
PYTHONPATH=src BEACN_WEB_REPO="$WEB" python3 scripts/update_web_status.py >/dev/null 2>&1
cd "$WEB"
ids="$(python3 -c "import json;print(' '.join(a['cip129_action_id'] for a in json.load(open('status.json'))['actions'] if str(a.get('status','')).lower()=='open' and a.get('cip129_action_id')))" 2>/dev/null)"
for id in $ids; do python3 scripts/build_share_card.py --id "$id" >/dev/null 2>&1 || true; done
rsync -a data/output/public/share/ public/data/output/public/share/

git add -A
if git diff --cached --quiet; then
  log "no web changes to commit"
else
  git commit -q -m "publish: on-chain vote(s) + cards $(date -u +%FT%TZ)"
  git push -q origin main || log "web push failed"
fi
log "daily vote step complete"
