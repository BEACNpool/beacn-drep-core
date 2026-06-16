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
  git -C "$repo" add -A
  if git -C "$repo" diff --cached --quiet; then
    log "no changes in $(basename "$repo")"
  else
    git -C "$repo" commit -m "$message"
    git -C "$repo" push origin main
  fi
}

publish_web_gh_pages() {
  local tmp
  tmp="$(mktemp -d)"
  log "syncing web main to gh-pages"
  git -C "$WEB" worktree add "$tmp" gh-pages
  rsync -a --delete --exclude .git --exclude node_modules "$WEB"/ "$tmp"/
  git -C "$tmp" add -A
  if git -C "$tmp" diff --cached --quiet; then
    log "no changes in beacn-drep-web gh-pages"
  else
    git -C "$tmp" commit -m "publish: rationale refresh $(date -u +%Y-%m-%dT%H:%M:%SZ)"
    git -C "$tmp" push origin gh-pages
  fi
  git -C "$WEB" worktree remove "$tmp"
  rmdir "$tmp" 2>/dev/null || true
}

ensure_clean_or_ours() {
  local repo="$1"
  if [ -n "$(git -C "$repo" status --porcelain)" ]; then
    log "$(basename "$repo") has local changes; continuing because this job owns DRep generated artifacts"
  fi
}

log "starting BEACN DRep daily offline check"

for repo in "$SOUL" "$RES" "$CORE" "$WEB"; do
  git -C "$repo" fetch origin --prune
  if git -C "$repo" status --short --branch | head -1 | grep -q "behind"; then
    git -C "$repo" pull --ff-only origin main
  fi
done

ensure_clean_or_ours "$RES"
ensure_clean_or_ours "$CORE"
ensure_clean_or_ours "$WEB"

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

log "refreshing cached proposal anchors"
cd "$RES"
python3 scripts/fetch_anchor_documents.py
python3 scripts/compile_action_resource_index.py

log "running offline rationales for all proposals"
cd "$CORE"
PYTHONPATH=src python3 -m beacn_drep.cli run-all

log "preparing rationale anchors and public artifacts"
PYTHONPATH=src python3 scripts/prepare_rationale_anchors.py
PYTHONPATH=src python3 -m beacn_drep.exporters.export_public_artifacts
PYTHONPATH=src python3 scripts/generate_statements.py --force
PYTHONPATH=src BEACN_WEB_REPO="$WEB" python3 scripts/update_web_status.py

log "running tests and replay spot-check"
PYTHONPATH=src python3 -m unittest discover -s tests
FAIL=0
while IFS= read -r run_id; do
  result="$(PYTHONPATH=src python3 -m beacn_drep.cli verify-replay --run-id "$run_id" 2>&1)"
  if echo "$result" | grep -q '"ok": false'; then
    log "REPLAY MISMATCH: $run_id"
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
sample_ids = ids[:3] + ids[len(ids)//2:len(ids)//2+3] + ids[-3:]
for aid in sample_ids:
    if aid in latest:
        print(latest[aid].name)
PY
)
if [ "$FAIL" -eq 1 ]; then
  log "replay verification failed; aborting before commits"
  exit 1
fi

log "syncing public artifacts to web"
cd "$WEB"
rsync -a --delete "$CORE/data/output/public/" "$WEB/data/output/public/"
python3 src/beacn_drep_web/build_backtest.py
rsync -a --delete "$WEB/data/output/public/" "$WEB/public/data/output/public/"

stamp="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
commit_if_changed "$RES" "data: governance snapshot ${stamp}"
commit_if_changed "$CORE" "decisions: offline rationale refresh ${stamp}"
commit_if_changed "$WEB" "publish: rationale refresh ${stamp}"
publish_web_gh_pages

log "BEACN DRep daily offline check complete"
