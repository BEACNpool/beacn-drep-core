#!/usr/bin/env bash
set -euo pipefail

export BEACN_WORKSPACE="${BEACN_WORKSPACE:-${HOME}/.openclaw/workspace}"
SOUL="${BEACN_WORKSPACE}/beacn-drep-soul"
RES="${BEACN_WORKSPACE}/beacn-drep-resources"
CORE="${BEACN_WORKSPACE}/beacn-drep-core"
WEB="${BEACN_WORKSPACE}/beacn-drep-web"

log() { echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] $*"; }

# Pre-flight: soul must be clean
if [ -n "$(git -C "$SOUL" status --porcelain)" ]; then
  log "ERROR: soul repo has uncommitted changes. Aborting."
  exit 1
fi

# Step 1: Export governance data
log "Step 1: Exporting governance data..."
cd "$CORE"
if python3 -m beacn_drep.exporters.export_from_postgres 2>/dev/null; then
  log "PostgreSQL export succeeded."
else
  log "PostgreSQL failed, falling back to SQLite..."
  python3 -m beacn_drep.exporters.export_proposals_to_resources
fi

# Step 2: Commit resources
log "Step 2: Committing resources..."
cd "$RES"
git add -A
git diff --cached --quiet || git commit -m "governance snapshot $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git push origin main

# Step 3: Run engine
log "Step 3: Running decision engine..."
cd "$CORE"
python3 -m beacn_drep.cli run-all

# Step 4: Verify replay (spot-check latest 5)
log "Step 4: Verifying replay..."
FAIL=0
for d in $(ls -td data/output/gov_action*/ 2>/dev/null | head -5); do
  run_id=$(basename "$d")
  result=$(python3 -m beacn_drep.cli verify-replay --run-id "$run_id" 2>&1)
  if echo "$result" | grep -q '"ok": false'; then
    log "REPLAY MISMATCH: $run_id"
    FAIL=1
  fi
done
if [ "$FAIL" -eq 1 ]; then
  log "ERROR: Replay verification failed. Aborting publish."
  exit 1
fi

# Step 5: Export public artifacts
log "Step 5: Exporting public artifacts..."
python3 -m beacn_drep.exporters.export_public_artifacts

# Step 6: Build backtest
log "Step 6: Building backtest..."
cd "$WEB"
python3 src/beacn_drep_web/build_backtest.py

# Step 7: Sync to web
log "Step 7: Syncing artifacts to web..."
rsync -av --delete \
  "${CORE}/data/output/public/" \
  "${WEB}/public/data/output/public/"

# Step 8: Commit and push
log "Step 8: Committing and pushing..."
cd "$CORE"
git add -A
git diff --cached --quiet || git commit -m "decisions $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git push origin main

cd "$WEB"
git add -A
git diff --cached --quiet || git commit -m "publish $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git push origin main

log "Pipeline complete."
