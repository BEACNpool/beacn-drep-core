#!/usr/bin/env bash
set -euo pipefail
PYTHONPATH=src python3 src/beacn_drep/exporters/export_public_artifacts.py
