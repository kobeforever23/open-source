# Market Risk Tooling Standards

## Objective
Ensure market-risk tools are defensible under senior quant and risk management scrutiny.

## Quant standards
- Explicit methodology with formulas visible in each tool.
- Input schema validation with clear failure messages.
- Stress + distributional metrics both reported (not one in isolation).
- Risk decomposition shown (component contributions, concentration shares).
- Matrix diagnostics for covariance/correlation-based models.

## Governance standards
- Escalation cues when concentration/instability thresholds are breached.
- Assumption transparency (units, horizons, confidence levels).
- Exportable outputs for committee and audit packs.
- Deterministic calculations from provided inputs.

## UI standards
- Bloomberg-style dark terminal aesthetic with high readability.
- Dense information layout without hiding key diagnostics.
- Fast operation during live-event windows.

## Current conforming tools
- `market-risk-terminal/`
- `cross-asset-risk-monitor/`
- `stress-scenario-studio/`
- `eqfin-shock-calibrator/`
