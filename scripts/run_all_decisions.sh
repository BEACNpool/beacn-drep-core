#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH=src python3 -m beacn_drep.cli run-all "$@"
