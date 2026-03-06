# CIB Risk Tools Suite
**AS-OF:** 2026-03-05 14:03:09 EST

Standalone GUI/dashboard tools for CIB Risk execution.

## Quick start
1. `cd tools`
2. `python3 start_tools_server.py --port 8090`
3. Open `http://127.0.0.1:8090/`

## EQFIN Python GUI quick launch
- Folder: `eqfin-shock-calibrator/`
- Windows: `eqfin-shock-calibrator\\run_eqfin_gui.bat`
- macOS: `chmod +x eqfin-shock-calibrator/run_eqfin_gui.command eqfin-shock-calibrator/run_eqfin_gui.sh && eqfin-shock-calibrator/run_eqfin_gui.command`
- Linux: `chmod +x eqfin-shock-calibrator/run_eqfin_gui.sh && eqfin-shock-calibrator/run_eqfin_gui.sh`
- Self-test (headless): `python3 eqfin-shock-calibrator/calibrator_gui.py --self-test`

## Tool catalog
- `market-risk-terminal/`: flagship quant market risk workstation (VaR/ES, MC, backtesting, scenarios, stress sweeps).
- `eqfin-shock-calibrator/`: index and single-name stress shock calibration.
- `cross-asset-risk-monitor/`: exposure and stress PnL dashboard.
- `stress-scenario-studio/`: scenario definition and sensitivity translation.
- `liquidity-funding-war-room/`: liquidity and funding stress dashboard.
- `ccr-exposure-workbench/`: counterparty exposure and limit controls.
- `capital-bridge-analyzer/`: capital ratio bridge and management commentary support.
- `model-validation-lab/`: quick model outcomes validation diagnostics.
- `prompt-evaluation-console/`: AI prompt output quality and control checks.

## Quant governance
- [Market Risk Tooling Standards](MARKET_RISK_TOOLING_STANDARDS.md)

## Design principles
- Standalone first (HTML + JS).
- Fast to use under market-event pressure.
- Clear control thresholds and escalation cues.
- Export-friendly for committee packs.
