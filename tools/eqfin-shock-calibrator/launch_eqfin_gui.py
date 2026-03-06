#!/usr/bin/env python3
"""Cross-platform launcher for the EQFIN Python GUI."""

from pathlib import Path
import sys


def main() -> int:
    script_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(script_dir))

    import calibrator_gui

    return calibrator_gui.main()


if __name__ == "__main__":
    raise SystemExit(main())
