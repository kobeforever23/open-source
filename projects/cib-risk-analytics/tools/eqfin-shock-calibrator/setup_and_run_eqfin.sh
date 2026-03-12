#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PY="$SCRIPT_DIR/.venv/bin/python"
PY_BIN="${PYTHON:-python3}"

if [[ ! -x "$VENV_PY" ]]; then
  echo "[EQFIN] Creating local virtual environment..."
  "$PY_BIN" -m venv "$SCRIPT_DIR/.venv"
fi

echo "[EQFIN] Launching GUI..."
exec "$VENV_PY" "$SCRIPT_DIR/launch_eqfin_gui.py" "$@"
