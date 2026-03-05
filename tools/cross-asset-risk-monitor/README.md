# Cross-Asset Risk Monitor (Quant-Grade)

Bloomberg-style market risk monitor for cross-asset portfolios.

## What makes it quant-grade
- Full covariance-matrix portfolio risk model.
- Parametric VaR and Expected Shortfall (ES) at configurable confidence.
- Component VaR/ES decomposition by factor.
- Concentration analytics (abs share + HHI).
- Correlation matrix diagnostics (symmetry, bounds, PSD via Cholesky).
- Stress PnL translation in parallel to parametric metrics.

## Input specification
Exposure CSV columns:
- `factor`
- `desk`
- `delta_usd_per_unit`
- `daily_vol_unit`
- `stress_shock_unit`
- `unit` (`bp` or `pct`)

Correlation CSV format:
- Header: `factor,<factor1>,<factor2>,...`
- Rows: `<factor_i>,rho_i1,rho_i2,...`

Factor names in correlation header/rows must match exposure factors exactly.

## Methodology
- `sigma_i = delta_i * vol_i * sqrt(horizon)`
- `sigma_p = sqrt(sigma^T * Corr * sigma)`
- `VaR(alpha) = z(alpha) * sigma_p`
- `ES(alpha) = phi(z)/(1-alpha) * sigma_p`
- `CompVaR_i = z(alpha) * sigma_i * (Corr*sigma)_i / sigma_p`

## Notes for governance
- Component VaR can be negative when a factor is hedging.
- Non-PSD correlation matrices are explicitly flagged.
- Stress PnL can exceed VaR materially under nonlinear or liquidity stress; treat this as a governance signal.
