# CIB Risk Prompt Library
**AS-OF:** 2026-03-05 13:24:30 EST

This folder is the canonical prompt operating system for CIB Risk workflows.

## Structure
- `00_system/`: System operators and guardrails
- `01_executive/`: CRO and committee-level reporting prompts
- `02_market_risk/`: Market risk analytics and governance prompts
- `03_credit_ccr/`: Credit and counterparty risk prompts
- `04_liquidity_funding/`: Liquidity and funding risk prompts
- `05_capital_stress/`: Capital and stress testing prompts
- `06_model_risk/`: Model risk and validation prompts
- `07_data_controls/`: Risk data, controls, and reconciliation prompts
- `08_governance_audit/`: Audit, exam, and issue management prompts
- `09_ai_automation/`: AI-enabled workflow prompts with controls
- `10_communication/`: Executive communication and stakeholder prompts
- `11_self_learning/`: Learning, drills, and capability-building prompts

## Prompt Index
| Category | Prompt | File |
|---|---|---|
| `00_system` | CIB Risk OS Master Operator | [cib_risk_os_master_operator.md](00_system/cib_risk_os_master_operator.md) |
| `00_system` | CIB Risk Output Quality Gate | [cib_risk_output_quality_gate.md](00_system/cib_risk_output_quality_gate.md) |
| `01_executive` | CRO Weekly Risk Intelligence Brief | [cro_weekly_risk_intelligence_brief.md](01_executive/cro_weekly_risk_intelligence_brief.md) |
| `01_executive` | CRO Morning Risk Flash | [cro_morning_risk_flash.md](01_executive/cro_morning_risk_flash.md) |
| `01_executive` | Risk Committee Pack Generator | [risk_committee_pack_generator.md](01_executive/risk_committee_pack_generator.md) |
| `02_market_risk` | Market Risk Daily Monitor | [market_risk_daily_monitor.md](02_market_risk/market_risk_daily_monitor.md) |
| `02_market_risk` | VaR Backtesting Exception Analysis | [var_backtesting_exception_analysis.md](02_market_risk/var_backtesting_exception_analysis.md) |
| `02_market_risk` | Stress Scenario Designer | [stress_scenario_designer.md](02_market_risk/stress_scenario_designer.md) |
| `03_credit_ccr` | CCR Exposure and Limit Monitor | [ccr_exposure_and_limit_monitor.md](03_credit_ccr/ccr_exposure_and_limit_monitor.md) |
| `03_credit_ccr` | Wrong-Way Risk Investigation | [wrong_way_risk_investigation.md](03_credit_ccr/wrong_way_risk_investigation.md) |
| `03_credit_ccr` | CVA Shock Commentary | [cva_shock_commentary.md](03_credit_ccr/cva_shock_commentary.md) |
| `04_liquidity_funding` | Liquidity Early Warning Dashboard | [liquidity_early_warning_dashboard.md](04_liquidity_funding/liquidity_early_warning_dashboard.md) |
| `04_liquidity_funding` | Margin Liquidity Drill | [margin_liquidity_drill.md](04_liquidity_funding/margin_liquidity_drill.md) |
| `05_capital_stress` | Capital Ratio Bridge | [capital_ratio_bridge_prompt.md](05_capital_stress/capital_ratio_bridge_prompt.md) |
| `05_capital_stress` | Regulatory Stress Mapping | [regulatory_stress_mapping.md](05_capital_stress/regulatory_stress_mapping.md) |
| `06_model_risk` | Model Validation Challenge Pack | [model_validation_challenge_pack.md](06_model_risk/model_validation_challenge_pack.md) |
| `07_data_controls` | Data Quality Incident RCA | [data_quality_incident_rca.md](07_data_controls/data_quality_incident_rca.md) |
| `07_data_controls` | Reconciliation Break Triage | [reconciliation_break_triage.md](07_data_controls/reconciliation_break_triage.md) |
| `08_governance_audit` | Audit Evidence Pack Builder | [audit_evidence_pack_builder.md](08_governance_audit/audit_evidence_pack_builder.md) |
| `08_governance_audit` | Exam Readiness War Room | [exam_readiness_war_room.md](08_governance_audit/exam_readiness_war_room.md) |
| `09_ai_automation` | AI Risk Workflow Designer | [ai_risk_workflow_designer.md](09_ai_automation/ai_risk_workflow_designer.md) |
| `09_ai_automation` | RAG Citation Guardrail Prompt | [rag_citation_guardrail_prompt.md](09_ai_automation/rag_citation_guardrail_prompt.md) |
| `10_communication` | CIB Risk Executive Memo Writer | [cib_risk_executive_memo_writer.md](10_communication/cib_risk_executive_memo_writer.md) |
| `10_communication` | Desk Head Briefing Note | [desk_head_briefing_note.md](10_communication/desk_head_briefing_note.md) |
| `11_self_learning` | Weekly Skill Gap Coach | [weekly_skill_gap_coach.md](11_self_learning/weekly_skill_gap_coach.md) |
| `11_self_learning` | Case Drill Generator | [case_drill_generator.md](11_self_learning/case_drill_generator.md) |

## How to use
1. Start with `00_system/cib_risk_os_master_operator.md`.
2. Select a workflow prompt by category and fill required inputs.
3. Run final output through `00_system/cib_risk_output_quality_gate.md`.

## Source and control alignment
- Skills OS references: `../skills/cib-risk-skills-os/`
- Verification policy: `../skills/cib-risk-skills-os/VERIFICATION_POLICY.md`
- Update playbook: `../skills/cib-risk-skills-os/UPDATE_PLAYBOOK.md`
