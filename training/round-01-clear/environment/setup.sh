#!/usr/bin/env bash
set -euo pipefail

ROUND_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
REF_DIR="$ROUND_DIR/reference"
cd "$REF_DIR"

python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if [[ ! -f .env ]]; then
  cp .env.example .env
  printf '[INFO] Created .env from .env.example. Fill real values locally; never commit it.\n'
fi

printf '[PASS] B7-2 local environment prepared.\n'
