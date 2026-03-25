#!/usr/bin/env bash
set -euo pipefail

export BEACN_WORKSPACE="${BEACN_WORKSPACE:-${HOME}/.openclaw/workspace}"
RES="${BEACN_WORKSPACE}/beacn-drep-resources"

cd "$RES"
python3 scripts/compile_action_resource_index.py

echo "resource intelligence refresh complete"
