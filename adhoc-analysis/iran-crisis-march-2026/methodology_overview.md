# Methodology Overview: Iran Stress Scenario + Risk Report Package

## Scope
This methodology summary consolidates the current approach embedded in the March 2026 Iran crisis artifacts in `source-materials/`.

## Methodology Stack
1. Event-centric scenario framing
- Anchor analysis to a concrete geopolitical trigger and timeline.
- Define severity at enterprise level (for example: `CRITICAL`) before desk-level analysis.
- Use explicit horizon buckets: immediate (`T+0`), short-term (`T+5`/`1 week`), medium (`T+10`/`2 weeks`), sustained (`T+30`/`1 month`).

2. Multi-scenario architecture
- Build a base scenario plus adverse and tail scenarios.
- Separate commodity-specific shock design from cross-asset contagion design.
- Include at least one rapid de-escalation path and one catastrophic escalation path.

3. Five-factor shock calibration approach
- Historical analog scaling:
  Align shock magnitudes to prior geopolitical episodes and scale for current conditions.
- Supply-demand fundamentals:
  Quantify physical disruption (oil/LNG/shipping) and elasticity-based repricing.
- Risk premium decomposition:
  Split moves into fundamentals, uncertainty premium, and technical/flow effects.
- Options-implied distribution extraction:
  Use skew/term-structure/vol surfaces to calibrate tail severity.
- Expert consistency overlay:
  Enforce cross-asset internal consistency and desk-level plausibility.

4. Driver-level shock specification
- Define shocks at granular driver level by asset class (energy, rates, FX, credit, equities, vol surfaces).
- Assign confidence tier per driver (`HIGH`/`MEDIUM`/`LOW`) based on data quality and precedent strength.
- Preserve rationale and calibration source per shock.

5. Cross-asset transmission mapping
- Explicitly model first-order and second-order channels:
  energy -> inflation/breakevens -> rates path; energy -> growth -> equities/credit; conflict risk -> vol/FX/carry unwind.
- Include correlation regime assumptions and scenario-specific correlation shifts.

6. Enterprise risk integration
- Map market, counterparty, credit, liquidity, operational/cyber, and country risk in one dashboard.
- Tie scenario outputs to desk P&L ranges and concentration hotspots.
- Convert outputs into risk actions with owner, trigger, and time bound.

7. Governance and escalation controls
- Run under crisis governance cadence (war-room style).
- Define escalation framework tied to trigger levels (price, spread, vol, shipping status, cyber posture).
- Include model caveats, uncertainty tags, and explicit assumptions.

8. Data-source discipline
- Timestamp all market and event data.
- Blend internal positions/Greeks/exposure data with external market and intelligence feeds.
- Use source triangulation for key claims (market data + intelligence + operational telemetry).

## Output Pattern Used by Current Package
1. Executive dashboard and situation summary
2. Scenario matrix with probabilities and severity
3. Cross-asset shock tables and transmission logic
4. Desk/portfolio impact ranges and watchlists
5. Immediate actions, tactical controls, and escalation triggers
6. Assumptions, caveats, and confidence annotations

## Known Limitations (Current Approach)
- Geopolitical path-dependency can dominate model-based calibrations.
- Liquidity gaps and weekend repricing effects can exceed historical analogs.
- Cross-asset correlation may break under tail stress.
- Operational/cyber impacts are partly non-linear and harder to quantify than market shocks.

## Recommended Standard for Future Iterations
- Keep scenario templates stable; refresh calibrations with current data.
- Separate factual data from assumptions in all tables.
- Require confidence tags and rationale for every material shock.
- Maintain a reproducible generation prompt and an audit trail of source timestamps.
