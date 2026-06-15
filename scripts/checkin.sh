#!/usr/bin/env bash
# BEACN DRep daily check-in: refresh the status feed from the live chain and
# publish it to the website. This is the heartbeat the cron runs every day,
# whether or not anything is voted on.
#
#   PUBLISH=1 scripts/checkin.sh         # generate + commit + push status.json
#   scripts/checkin.sh                   # generate only (no git)
#
# BEACN_WEB_PUBLISH_BRANCH selects the branch the site-deploy flow consumes
# (default: main; openclaw's deploy copies static files main -> gh-pages).
set -euo pipefail

CORE="${BEACN_CORE_REPO:-$HOME/.openclaw/workspace/beacn-drep-core}"
WEB="${BEACN_WEB_REPO:-$HOME/.openclaw/workspace/beacn-drep-web}"
BRANCH="${BEACN_WEB_PUBLISH_BRANCH:-main}"

cd "$CORE"
PYTHONPATH=src python3 scripts/update_web_status.py

if [ "${PUBLISH:-0}" != "1" ]; then
  echo "generated status.json (set PUBLISH=1 to commit + push)"
  exit 0
fi

cd "$WEB"
git add status.json index.html
if git diff --cached --quiet; then
  echo "no status change to publish"
  exit 0
fi
git commit -q -m "checkin: status $(date -u +%FT%TZ)"
git push -q origin "$BRANCH"
echo "published status to $BRANCH (run the site deploy to push it to gh-pages)"
