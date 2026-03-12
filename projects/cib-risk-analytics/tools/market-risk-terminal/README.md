# Market Risk Terminal

Flagship quant-grade market risk workstation for professional risk teams.

## Core capabilities
- Parametric VaR and ES from covariance matrix.
- Monte Carlo VaR and ES with correlated factor shocks and gamma nonlinearity.
- Historical VaR and ES from realized PnL history.
- Backtesting with Kupiec proportion-of-failures test (p-value output).
- Factor-level component VaR/ES decomposition.
- Scenario PnL ranking with worst-case diagnostics.
- Correlation stress sweep (off-diagonal shift sensitivity).
- Reverse stress scaling against a target loss.
- Exportable JSON snapshot for governance packs.

## Input schemas
Factor exposure CSV:
- `factor`
- `desk`
- `delta_usd_per_unit`
- `gamma_usd_per_unit2`
- `daily_vol_unit`
- `stress_shock_unit`
- `unit` (`bp` or `pct`)

Correlation matrix CSV:
- first header field `factor`
- columns/rows matching factor names exactly

Historical PnL input:
- one numeric PnL per line (USD)

Scenario library CSV:
- first column `scenario`
- one shock column for each factor

## Validation and controls
- schema validation for all input blocks
- matrix quality checks and Monte Carlo PSD enforcement
- concentration and backtesting warnings
- explicit methodology in tool for audit traceability
