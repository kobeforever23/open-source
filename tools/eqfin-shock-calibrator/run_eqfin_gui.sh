#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

if [[ -x "$SCRIPT_DIR/.venv/bin/python" ]]; then
  PY="$SCRIPT_DIR/.venv/bin/python"
else
  PY="${PYTHON:-python3}"
fi

exec "$PY" "$SCRIPT_DIR/launch_eqfin_gui.py" "$@"
