#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH=src python3 -m beacn_drep.exporters.export_public_artifacts
