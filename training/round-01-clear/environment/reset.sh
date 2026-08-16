#!/usr/bin/env bash
set -euo pipefail

ROUND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REF_DIR="$ROUND_DIR/reference"

rm -rf "$REF_DIR/.venv"
rm -f "$REF_DIR/database.db" "$REF_DIR/database.db-shm" "$REF_DIR/database.db-wal"
find "$REF_DIR" -type d -name '__pycache__' -prune -exec rm -rf {} +

printf '[PASS] Removed only B7-2 local .venv/database/cache artifacts.\n'
printf '[INFO] .env is intentionally preserved because it may contain local secrets. Delete it manually only when intended.\n'
