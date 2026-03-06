# EQFIN Shock Calibrator (Python GUI + Web UI)
**AS-OF:** 2026-03-06

Index shock calibration tool for SPX/NDX and single-name stress overlays.

## What You Can Run
- Python GUI (Tkinter): `calibrator_gui.py` (primary for PyCharm/desktop workflow)
- Cross-platform launcher: `launch_eqfin_gui.py`
- Windows launcher: `run_eqfin_gui.bat`
- macOS launcher: `run_eqfin_gui.command`
- Linux/macOS shell launcher: `run_eqfin_gui.sh`
- Bootstrap + run (creates local `.venv` first):
  - Windows: `setup_and_run_eqfin.bat`
  - macOS: `setup_and_run_eqfin.command`
  - Linux/macOS shell: `setup_and_run_eqfin.sh`
- Browser UI: `index.html`

## One-Minute Start
1. Open this folder in PyCharm.
2. Run [launch_eqfin_gui.py](./launch_eqfin_gui.py) using your Python interpreter.
3. GUI opens as `EQFIN Stress Shock Calibrator`.

## Command-Line Launch (Any Machine)
From this folder:

### Windows
```bat
run_eqfin_gui.bat
```

### macOS
```bash
chmod +x run_eqfin_gui.command run_eqfin_gui.sh
./run_eqfin_gui.command
```

### Linux
```bash
chmod +x run_eqfin_gui.sh
./run_eqfin_gui.sh
```

## Fresh Machine Bootstrap (Recommended)
This creates a local virtual environment and launches the GUI.

### Windows
```bat
setup_and_run_eqfin.bat
```

### macOS
```bash
chmod +x setup_and_run_eqfin.command setup_and_run_eqfin.sh
./setup_and_run_eqfin.command
```

### Linux
```bash
chmod +x setup_and_run_eqfin.sh
./setup_and_run_eqfin.sh
```

## Health Check (No GUI Required)
Use self-test in CI/headless environments:

```bash
python calibrator_gui.py --self-test
```

Expected output:
```text
EQFIN self-test: PASS
```

## Dependencies
- Python 3.9+
- Tkinter support (`tkinter` module)
- No external pip packages required for the Python GUI

If `tkinter` is missing on Linux:
```bash
sudo apt-get install python3-tk
```

## Files
- `calibrator_gui.py`: primary Python GUI app and solver
- `spx_ndx_data.py`: static SPX/NDX constituent dataset used by GUI
- `launch_eqfin_gui.py`: stable launcher entrypoint
- `run_eqfin_gui.bat`: Windows launcher
- `run_eqfin_gui.command`: macOS double-click launcher
- `run_eqfin_gui.sh`: shell launcher
- `index.html` + `data.js`: standalone browser version

## Notes
- Data is local/static in this folder; no network call is required to launch.
- Python and web UIs are both supported; use Python GUI for PyCharm-first workflow.
- Portable bundle is available in repo `dist/eqfin-shock-calibrator-portable-2026-03-06.zip`.
