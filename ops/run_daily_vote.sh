#!/usr/bin/env bash
# Daily gated on-chain vote step. Runs AFTER run_daily_check.sh, which has
# already generated rationales, recorded + published rationale anchors, refreshed
# status.json, and pushed the web bundle.
#
# Policy (conservative, fail-closed):
#   * Only ABSTAIN recommendations are auto-submitted, and only on actions this
#     DRep has NOT yet voted (brand-new votes).
#   * Directional (YES/NO) decisions AND any revision of an existing on-chain vote
#     are HELD for operator review — never auto-broadcast.
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

log "running gated auto-vote (ABSTAIN-only; directional + revisions held)"
report="$(BEACN_VOTING_LIVE=1 PYTHONPATH=src python3 scripts/run_live_votes.py --live 2>&1)"
echo "$report" > "data/output/last_vote_run.json"
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

git add -A
if git diff --cached --quiet; then
  log "no web changes to commit"
else
  git commit -q -m "publish: on-chain vote(s) + cards $(date -u +%FT%TZ)"
  git push -q origin main || log "web push failed"
fi
log "daily vote step complete"
