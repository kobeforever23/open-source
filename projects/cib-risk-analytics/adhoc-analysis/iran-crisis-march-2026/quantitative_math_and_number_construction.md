# Quantitative Math and Number Construction

## Purpose
This appendix makes the number-building logic explicit for the Iran crisis package, so internal reviewers can trace each headline shock and P&L range back to a calculation path.

## 1) Shock Construction Framework
For each risk driver \(i\), the stressed move is built as:

\[
\Delta X_i = w_h \cdot \Delta X_{i,\text{hist}} + w_f \cdot \Delta X_{i,\text{fund}} + w_r \cdot \Delta X_{i,\text{rp}} + w_o \cdot \Delta X_{i,\text{opt}} + w_e \cdot \Delta X_{i,\text{expert}}
\]

With:
- \(\sum w_k = 1\)
- \(w_k\) chosen by data quality/liquidity/confidence
- output tagged `HIGH`, `MEDIUM`, or `LOW` confidence

This matches the five-factor approach in the source stress specification:
- historical analog scaling
- supply-demand fundamentals
- risk premium decomposition
- options-implied tails
- expert consistency overlay

## 2) Energy Supply Shock Math
Use a short-run elasticity approximation:

\[
\%\Delta P \approx -\frac{\%\Delta Q_{\text{net}}}{\varepsilon_d}
\]

Where:
- \(\varepsilon_d\): short-run demand elasticity (document references about -0.05 to -0.10 for crude)
- \(\%\Delta Q_{\text{net}} = \frac{Q_{\text{disrupted}} - Q_{\text{offset}}}{Q_{\text{global}}}\)

### Worked example (document-aligned)
- net crude disruption: \(8\) to \(10\) M bpd (initial)
- assume global crude market \(Q_{\text{global}} \approx 102\) M bpd
- \(\%\Delta Q_{\text{net}} \approx 7.8\%\) to \(9.8\%\)
- with \(\varepsilon_d=-0.07\):

\[
\%\Delta P \approx 111\% \text{ to } 140\%
\]

This is a theoretical upper response. Applied scenario shocks are damped by offsets (pipeline rerouting, SPR drawdown, timing frictions, demand destruction), yielding lower implementation shocks (for example the spec notes Brent shock ranges roughly +35% to +55% in a severe-but-plausible calibration).

## 3) Basis and Curve Construction
For regional basis moves (e.g., WTI-Brent):

\[
\Delta \text{Basis} = f(\text{logistics bottlenecks}, \text{export constraints}, \text{regional supply mix}, \text{insurance/freight shock})
\]

Document-aligned example:
- WTI-Brent basis from about \(10.5\) to \(16\) to \(17\)
- basis widening: \(+5.5\) to \(+6.5\)

Curve shifts are split:
- prompt shock component (event gap)
- deferred shock component (supply response and demand destruction)
- backwardation or contango regime adjustment

## 4) Risk Premium Decomposition
For non-physical channels (equities, credit, FX):

\[
\Delta X = \Delta X_{\text{fundamental}} + \Delta X_{\text{risk premium}} + \Delta X_{\text{technical}}
\]

Typical decomposition inputs:
- earnings/cash-flow hit (fundamental)
- uncertainty and geopolitical premium (risk premium)
- CTA/risk-parity/deleveraging and flow pressure (technical)

## 5) Options-Implied Tail Translation
Use options surface signals (RR/BF/term structure) to shape tail severity:
- spot shock level
- skew shock
- vol-of-vol shock

Simplified mapping:

\[
\Delta \sigma_{\text{stress}} = g(\text{ATM IV}, \text{25d RR}, \text{BF}, \text{term inversion}, \text{event intensity})
\]

Then propagate through vega and convexity in desk books.

## 6) Correlation Stress and Diversification Erosion
Portfolio risk under stressed correlation:

\[
\sigma_p^2 = \mathbf{w}^\top \Sigma \mathbf{w}
\]

Compute with:
- base matrix \(\Sigma_{\text{base}}\)
- stressed matrix \(\Sigma_{\text{stress}}\) (with crisis overrides, e.g. higher cross-asset correlations)

Diversification erosion:

\[
\text{Erosion} = \frac{\sigma_{p,\text{stress}} - \sigma_{p,\text{base}}}{\sigma_{p,\text{base}}}
\]

## 7) Desk P&L Propagation Formula
Second-order local approximation:

\[
\Delta V \approx \sum_i \Delta_i \Delta X_i + \frac{1}{2}\sum_i \Gamma_i (\Delta X_i)^2 + \sum_{i<j}\Gamma_{ij}\Delta X_i\Delta X_j + \sum_k \text{Vega}_k \Delta \sigma_k + \Theta \Delta t
\]

Add explicit terms for:
- basis shocks
- funding/liquidity costs
- margin/collateral drag
- execution slippage

## 8) Scenario Probability and Aggregation
Given scenario set \(s \in S\):

\[
\mathbb{E}[\text{P\&L}] = \sum_{s \in S} p_s \cdot \text{P\&L}_s
\]

If scenario probabilities come from different documents/contexts, normalize:

\[
p'_s = \frac{p_s}{\sum_{j \in S} p_j}
\]

Tail measure:

\[
\text{Tail Expected Loss} = \sum_{s \in S_{\text{tail}}} p'_s \cdot |\text{Loss}_s|
\]

## 9) Confidence Scoring (Operationalized)
Convert qualitative confidence to numeric score:
- `HIGH` = 0.8 to 1.0
- `MEDIUM` = 0.5 to 0.79
- `LOW` = 0.2 to 0.49

Example weighted score:

\[
C_i = 0.35 D_i + 0.25 L_i + 0.20 A_i + 0.20 S_i
\]

Where:
- \(D_i\): data quality
- \(L_i\): market liquidity
- \(A_i\): analog relevance
- \(S_i\): cross-asset consistency

## 10) Data Freshness and Traceability Requirements
Each reported number should carry:
- as-of timestamp
- source
- transformation step
- model version
- assumption flags

Suggested trace key:
- `number_id`
- `raw_input`
- `transformation`
- `final_value`
- `owner`
- `review_status`

## 11) Practical Validation Checks
Before publishing:
1. Reconstruct top-20 headline numbers from raw inputs.
2. Re-run P&L under both base and stressed correlation matrices.
3. Compare sensitivity approximation vs full revaluation for nonlinear books.
4. Run probability sanity check (sum, overlap, conditional logic).
5. Verify all tail metrics against current limit/risk appetite thresholds.

## 12) What This Enables
- Full audit trail for shock and P&L numbers.
- Cleaner challenge process with Model Risk and Internal Audit.
- Faster refresh cycles when market conditions change intraday.
