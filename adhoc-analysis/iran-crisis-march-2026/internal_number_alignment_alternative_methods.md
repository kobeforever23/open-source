# Aligning to Real Internal Numbers: Alternative Methods

## Goal
Map external event scenarios to true internal portfolio risk and P&L with stronger quantitative reliability and governance.

## Champion-Challenger Setup
- Champion: current desk-level stress pipeline (fast, sensitivity-heavy).
- Challenger set: run at least 2 alternatives below in parallel.
- Promote challenger if it improves out-of-sample accuracy, stability, and governance quality.

## Method A: Sensitivity Overlay (Fast Baseline)
Best for:
- intraday decisions
- first-pass CRO alerts

Mechanics:
- map scenario shocks to internal risk factors
- apply Greeks/sensitivities
- include convexity for major nonlinear books

Formula core:
\[
\Delta V \approx \Delta \cdot \Delta X + \frac{1}{2}\Gamma(\Delta X)^2 + \text{Vega}\cdot\Delta \sigma
\]

Pros:
- very fast
- transparent

Limit:
- underperforms in large discontinuous moves and liquidity breaks

## Method B: Full Revaluation Stress (Pricing-Engine Accurate)
Best for:
- final governance pack
- Board/regulator-facing scenarios

Mechanics:
- reprice each position with stressed curves/surfaces/spreads
- include model-consistent revaluation for options and structured products

Pros:
- highest fidelity for nonlinear books

Limit:
- slower, infrastructure intensive

## Method C: Filtered Historical Simulation (FHS)
Best for:
- blending current volatility regime with historical shock structure

Mechanics:
- fit conditional volatility model (for example EWMA/GARCH)
- normalize historical returns
- re-scale by current vol regime
- apply to portfolio

Pros:
- regime-aware; better than raw historical replay

Limit:
- still dependent on historical pattern availability

## Method D: Regime-Switching Scenario Engine
Best for:
- geopolitical crises with phase changes

Mechanics:
- define latent states (contained conflict, prolonged conflict, regional war)
- estimate transition probabilities
- apply state-specific shock/correlation matrices

Pros:
- captures path dependency and nonlinearity over time

Limit:
- calibration uncertainty in state transitions

## Method E: Copula/MC Cross-Asset Simulation
Best for:
- joint tail dependency and diversification breakdown analysis

Mechanics:
- calibrate marginal shock distributions per factor
- apply copula dependency (t-copula often more tail-realistic than Gaussian)
- run Monte Carlo P&L distribution

Pros:
- stronger tail co-move realism

Limit:
- model risk and calibration sensitivity

## Method F: Bayesian Model Averaging (BMA)
Best for:
- combining conflicting model outputs

Mechanics:
- assign posterior weights to methods based on recent predictive performance
- aggregate stressed P&L and risk metrics

\[
\hat{Y} = \sum_m w_m Y_m,\quad \sum_m w_m = 1
\]

Pros:
- reduces single-model fragility

Limit:
- requires disciplined performance tracking

## Method G: Reverse Stress Calibration
Best for:
- capital and limit governance

Mechanics:
- solve for minimum shock vector that breaches target threshold (for example, VaR limit, loss budget, capital trigger)
- convert result into monitoring triggers

Pros:
- actionable for control thresholds

Limit:
- not a probability forecast by itself

## Method H: Liquidity-Adjusted Stress (LAS)
Best for:
- crisis execution realism

Mechanics:
- add spread widening + market depth haircuts + slippage + liquidation horizon penalties

Example add-on:
\[
\text{Stress Loss}_{\text{LAS}} = \text{MTM Stress Loss} + \text{Slippage} + \text{Funding Drag} + \text{Gap Risk}
\]

Pros:
- much closer to realizable loss

Limit:
- assumptions need frequent refresh in fast markets

## Recommended Standard Operating Mix
1. Intraday (0-2 hours): Method A + H
2. Same-day governance: Method B + D
3. Daily risk committee pack: Method B + C + H
4. Weekly validation: add E + F challenger outputs
5. Monthly deep review: include G reverse stress recalibration

## Minimum Data Needed to Align Internal Numbers
- full position inventory (desk, legal entity, product)
- Greeks and nonlinear sensitivities
- curve/surface snapshots (pre and stress)
- collateral and margin terms
- funding/liquidity metrics
- counterparty and wrong-way risk links
- model version metadata

## Alignment Control Checklist
1. Factor mapping completeness > 99% of risk notional.
2. Shock coverage across all material asset classes.
3. Sensitivity vs full reval gap within tolerance band.
4. Correlation stress applied and documented.
5. Liquidity adjustment included for crisis scenarios.
6. Scenario probabilities normalized and version-controlled.
7. Number-level traceability present for top CRO dashboard metrics.

## Immediate Enhancements You Should Add
1. Build a `number lineage table` for every top-dashboard figure.
2. Run dual-track P&L: sensitivity and full revaluation.
3. Add explicit diversification-erosion metric in all scenario packs.
4. Include liquidity-adjusted loss next to mark-to-market loss.
5. Maintain challenger model leaderboard with monthly promotion/demotion.
