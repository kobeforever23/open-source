# Stress Capital Linkage
**Category:** Capital and Balance Sheet
**Level:** L4
**Prereqs:** [01 Risk Organization Map](../00_foundations/01_risk_organization_map.md), [02 Core Financial Math For Risk](../00_foundations/02_core_financial_math_for_risk.md), [07 Rwa Optimization With Control Discipline](07_rwa_optimization_with_control_discipline.md)
**AS-OF:** 2026-03-05 11:49:38 EST

## What it is
A production-ready workflow for this capability, designed for daily CIB risk operation with clear ownership, evidence, and decision outputs.

## Why it matters in CIB risk
This skill improves speed-to-decision while preserving control quality, helping teams manage PnL/exposure volatility, governance obligations, and supervisory expectations.

## When to use it (signals + triggers)
- Metric volatility increases or unexplained PnL/exposure moves appear.
- Limit utilization exceeds early-warning thresholds (for example 80/90/100%).
- New product, booking model, or data feed introduces measurement uncertainty.
- Regulatory/audit review requests traceable evidence and method rationale.

## Step-by-step playbook
1. Define scope: portfolio, metric, horizon, and decision owner.
2. Collect data from approved golden sources and validate quality checks.
3. Run analysis using controlled code/query artifacts and preserve run metadata.
4. Challenge outputs with sensitivity checks, peer review, and benchmark comparison.
5. Translate findings into actions: limit proposals, hedges, controls, or escalation.
6. Package evidence in an audit-ready note with assumptions, caveats, and approvals.

## Outputs / artifacts produced (examples)
- One-page decision memo with key metrics, trend view, and recommended action.
- Reproducible analytics artifact (SQL/Python notebook or dashboard snapshot).
- Control evidence pack: lineage, reconciliation, reviewer sign-off, and ticket links.

## Common pitfalls & failure modes
- Relying on a single metric without triangulating by scenario, sensitivity, and concentration.
- Ignoring stale market data, broken joins, or booking population drift.
- Escalating too late because thresholds were not pre-agreed and monitored daily.
- Documenting outputs without assumptions, model limits, or ownership clarity.

## Quality bar (what “good” looks like)
- Accuracy: results reconcile to source systems and prior reports within tolerance.
- Timeliness: analysis delivered inside agreed cycle time for risk decisions.
- Explainability: stakeholders can trace each number to source, method, and owner.
- Actionability: output ends with clear decision options, trade-offs, and owners.

## Exercises (drills + case prompts)
- Drill: reproduce last week's metric from raw data and explain any variance >5%.
- Case prompt: simulate a 2-sigma market move and propose risk actions in 30 minutes.
- Peer challenge: swap analyses with a colleague and identify one hidden assumption.

## Interview / stakeholder questions (if relevant)
- What decision changes if this metric moves by +/-10%?
- Which assumptions are most fragile, and how are they monitored?
- What is the escalation trigger and who signs off?

## Tools & templates (SQL/Python/PowerBI/Jira/Confluence style)
```sql
-- Daily limit utilization and breaches by desk
SELECT as_of_date,
       desk,
       SUM(risk_metric) AS metric,
       SUM(limit_value) AS limit_value,
       SUM(risk_metric)/NULLIF(SUM(limit_value),0) AS utilization
FROM risk_limit_snapshot
GROUP BY 1,2;
```

```python
import pandas as pd

df = pd.read_csv('risk_snapshot.csv')
df['utilization'] = df['risk_metric'] / df['limit_value']
alert = df[df['utilization'] > 0.9]
print(alert[['desk', 'metric_name', 'utilization']])
```

```text
PowerBI pattern:
- Star schema: fact_risk_exposure + dim_desk + dim_counterparty + dim_date
- DAX measure: Utilization = DIVIDE(SUM(fact_risk_exposure[value]), SUM(fact_risk_exposure[limit]))
- Publish: certified dataset with row-level security by desk
```

```text
Jira workflow:
Issue Type: Risk-Control-Enhancement
Fields: control_owner, severity, due_date, evidence_link
States: Open -> In Progress -> Validation -> Closed
```

```text
Confluence template sections:
1) Context
2) Method
3) Results
4) Decisions
5) Actions + owners + dates
6) Evidence links
```

## References (with citations)
- [Basel Framework Calculation of RWA for Credit Risk (CRE)](https://www.bis.org/basel_framework/standard/CRE.htm)
- [Basel Framework Market Risk (MAR)](https://www.bis.org/basel_framework/standard/MAR.htm)
- [BCBS Basel III Leverage Ratio Framework and Disclosure Requirements](https://www.bis.org/bcbs/publ/d365.htm)
- [Verification Policy](../../VERIFICATION_POLICY.md)
- [Authoritative Sources Registry](../../sources/authoritative_sources.md)
## Advanced implementation notes
- **Depth objective:** move this module from descriptive understanding to decision-grade execution under stress.
- **Primary instrumentation focus:** `stress capital depletion slope`.
- **Control anchor:** `stress-capital linkage sign-off`.
- **Adverse case to rehearse monthly:** `stress path acceleration`.
- **Decision latency target:** deliver first recommendation within 30 minutes of trigger detection and final pack within policy SLA.

## KPI / KRI instrumentation
| Indicator | Definition | Threshold Logic | Owner | Cadence |
|---|---|---|---|---|
| Core KPI | `stress capital depletion slope` measured against approved baseline | Green/Amber/Red with pre-agreed escalation thresholds | Desk + Risk | Daily |
| Control KRI | `stress-capital linkage sign-off` exception count and aging | Any overdue high-severity exception -> immediate escalation | Control owner | Daily |
| Scenario KRI | Breach distance under `stress path acceleration` | <20% headroom to limit/appetite -> governance challenge | Risk manager | Weekly |
| Delivery KPI | Decision package timeliness | Missed SLA requires RCA and process correction | COO/PMO | Weekly |

## Control test library (module-specific)
1. **Preventive test:** verify input assumptions and source systems before running analytics.
2. **Detective test:** run independent reconciliation/challenge on key outputs and flag residuals above tolerance.
3. **Corrective test:** simulate a live exception and validate escalation path, owner accountability, and evidence closure.
4. **Audit test:** re-perform one historical decision end-to-end using stored evidence and confirm reproducibility.

## 30-60-90 mastery plan
- **Day 30:** reproduce the baseline workflow for `Stress Capital Linkage` on historical data and pass peer review.
- **Day 60:** independently own one production cycle and produce an executive-ready decision memo.
- **Day 90:** lead a challenge session, improve one control, and mentor a junior analyst through the playbook.
