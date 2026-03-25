#!/usr/bin/env bash
set -euo pipefail

export BEACN_WORKSPACE="${BEACN_WORKSPACE:-${HOME}/.openclaw/workspace}"
CORE="${BEACN_WORKSPACE}/beacn-drep-core"
WEB="${BEACN_WORKSPACE}/beacn-drep-web"

cd "$CORE"
PYTHONPATH=src python3 change-control/scripts/weekly_review.py

# Optional: surface latest report in public web docs directory for visibility
latest_report=$(ls -1t change-control/reports/weekly-review-*.json 2>/dev/null | head -1 || true)
if [ -n "${latest_report}" ]; then
  mkdir -p "$WEB/docs/change-reviews"
  cp "$latest_report" "$WEB/docs/change-reviews/latest-weekly-review.json"
fi

echo "weekly change review complete"
