# Stress Scenario Studio (Quant-Grade)

Advanced stress engine for market risk scenario translation.

## What makes it quant-grade
- First-order + second-order + volatility decomposition:
  - linear (`delta`)
  - convexity (`gamma`)
  - volatility (`vega`)
- Multi-scenario library with factor-level overrides.
- Scenario scaling control for severity sweeps.
- Reverse-stress scale solver against target PnL.
- Concentration and nonlinear-share diagnostics.

## Input specification
Factor CSV columns:
- `factor`
- `unit` (`bp` or `pct`)
- `delta_usd_per_unit`
- `gamma_usd_per_unit2`
- `vega_usd_per_vol_unit`
- `base_shock`
- `base_vol_shock`

Scenario CSV columns:
- `scenario`
- one column per factor shock (`<factor>`)
- optional vol shock override columns (`<factor>_VOL`)

## Methodology
For each factor `i`:
- `PnL_i = delta_i*shock_i + 0.5*gamma_i*shock_i^2 + vega_i*volShock_i`
- `Total PnL = Σ PnL_i`

Reverse stress target:
- Solve `A*m^2 + B*m = targetLoss`
- `A = 0.5*Σ(gamma_i*shock_i^2)`
- `B = Σ(delta_i*shock_i + vega_i*volShock_i)`

## Governance notes
- High nonlinear share indicates model risk and extrapolation sensitivity.
- Large scenario scales require explicit liquidity and valuation governance challenge.
- Reverse-stress outputs should be paired with realistic market-depth assumptions.
