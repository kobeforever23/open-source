# Open Source CIB Risk Workspace

Production-ready CIB Risk workspace with prompts, skills, tools, briefs, and archived reference artifacts.

## EQ Index Calibration GUI (Python)
Direct folder:
- `tools/eqfin-shock-calibrator/`

Primary launcher files:
- `tools/eqfin-shock-calibrator/launch_eqfin_gui.py`
- `tools/eqfin-shock-calibrator/run_eqfin_gui.bat` (Windows)
- `tools/eqfin-shock-calibrator/run_eqfin_gui.command` (macOS)
- `tools/eqfin-shock-calibrator/run_eqfin_gui.sh` (Linux/macOS shell)

Quick run:
- Windows: `tools\\eqfin-shock-calibrator\\run_eqfin_gui.bat`
- macOS: `chmod +x tools/eqfin-shock-calibrator/run_eqfin_gui.command tools/eqfin-shock-calibrator/run_eqfin_gui.sh && tools/eqfin-shock-calibrator/run_eqfin_gui.command`
- Linux: `chmod +x tools/eqfin-shock-calibrator/run_eqfin_gui.sh && tools/eqfin-shock-calibrator/run_eqfin_gui.sh`

PyCharm:
1. Open the repo.
2. Open `tools/eqfin-shock-calibrator/launch_eqfin_gui.py`.
3. Click Run.

Portable ZIP bundle:
- `dist/eqfin-shock-calibrator-portable-2026-03-06.zip`
- Includes all required source/data + Windows/macOS/Linux launch scripts.

## Start Here
- `prompts/`: production prompt library (with role/category routing)
- `skills/`: CIB Risk Skills OS and operating standards
- `tools/`: standalone HTML/Python risk tooling suite
- `briefs/`: executive brief outputs and briefing artifacts
- `adhoc-analysis/`: one-off deep-dive analysis packages
- `artifacts/`: archived dashboards, reports, and references

## Quick Navigation
| If you need... | Go to | Notes |
|---|---|---|
| CRO and desk prompts | `prompts/` | Includes a full CRO weekly brief template |
| Skill framework and governance | `skills/cib-risk-skills-os/` | Verification and update playbooks included |
| Interactive risk tools | `tools/` | Run local server via `python3 tools/start_tools_server.py` |
| OpenClaw brief files | `briefs/openclaw/` | Includes color version and prior brief |
| Iran crisis ad hoc package | `adhoc-analysis/iran-crisis-march-2026/` | Source docs + methodology + generation prompt |
| Legacy one-off dashboards/exports | `artifacts/` | Organized by dashboard/report/reference |

## Repository Layout
```text
open-source/
  prompts/
  skills/
  tools/
  briefs/
    openclaw/
  adhoc-analysis/
    iran-crisis-march-2026/
  artifacts/
    dashboards/
    reports/
    reference/
  misc/  (legacy pointer only)
```

## Notes
- Legacy materials were moved from `misc/` into `artifacts/` for cleaner navigation.
- `misc/` is retained only as a compatibility pointer.
