# CIB Risk Analytics Platform

Production-grade CIB Risk workspace — AI-assisted prompts, a comprehensive skills operating system, interactive tooling, executive briefs, and ad-hoc analysis packages.

---

## Quick Start

| If you need... | Go to | Notes |
|---|---|---|
| CRO and desk prompts | [`prompts/`](prompts/) | Full CRO weekly brief template + role-based routing |
| Skill framework and governance | [`skills/cib-risk-skills-os/`](skills/cib-risk-skills-os/) | 120+ skills across 15 categories, verification playbooks |
| Interactive risk tools | [`tools/`](tools/) | 9 standalone HTML/Python tools, run via `python3 tools/start_tools_server.py` |
| OpenClaw brief files | [`briefs/openclaw/`](briefs/openclaw/) | Color and standard versions |
| Iran crisis analysis package | [`adhoc-analysis/iran-crisis-march-2026/`](adhoc-analysis/iran-crisis-march-2026/) | Source docs + methodology + generation prompt |
| Scenario committee deliverables | [`deliverables/scenario-committee/`](deliverables/scenario-committee/) | Reports, one-pagers, speaking scripts |
| CRO weekly briefs | [`deliverables/cro-briefs/`](deliverables/cro-briefs/) | Weekly intelligence briefs (.docx, .md, .html) |
| Stress testing dashboards | [`deliverables/stress-testing/`](deliverables/stress-testing/) | TOH BAU scenario dashboards and reports |
| Geopolitical risk packages | [`deliverables/geopolitical/`](deliverables/geopolitical/) | Persian Gulf dashboards and impact reports |
| Legacy dashboards and exports | [`artifacts/`](artifacts/) | Archived dashboards, reports, references |
| Portable calibrator bundle | [`dist/`](dist/) | Cross-platform ZIP with launch scripts |

---

## Platform Architecture

```
cib-risk-analytics/
├── prompts/                          # Production prompt library
│   ├── 00_system/                    #   System-level operator + quality gate
│   ├── 01_executive/                 #   CRO briefs, risk committee packs
│   ├── 02_market_risk/               #   VaR, stress, daily monitor
│   ├── 03_credit_ccr/                #   CCR exposure, CVA, wrong-way risk
│   ├── 04_liquidity_funding/         #   Liquidity dashboards, margin drills
│   ├── 05_capital_stress/            #   Capital bridge, regulatory mapping
│   ├── 06_model_risk/                #   Model validation challenge packs
│   ├── 07_data_controls/             #   Data quality RCA, recon triage
│   ├── 08_governance_audit/          #   Audit evidence, exam readiness
│   ├── 09_ai_automation/             #   AI workflow design, RAG guardrails
│   ├── 10_communication/             #   Executive memos, desk briefings
│   └── 11_self_learning/             #   Case drills, skill gap coaching
│
├── skills/                           # CIB Risk Skills OS
│   └── cib-risk-skills-os/           #   15 categories × 8 skills = 120 modules
│       ├── skills/                   #     00_foundations → 14_self_learning
│       ├── templates/                #     Committee packs, scorecards, playbooks
│       ├── sources/                  #     Authoritative sources + RSS watchlist
│       └── *.md                      #     Operating model, delivery standards, etc.
│
├── tools/                            # Interactive risk tooling suite
│   ├── eqfin-shock-calibrator/       #   Python GUI + HTML — EQ/FX shock calibration
│   ├── market-risk-terminal/         #   Real-time market risk monitor
│   ├── stress-scenario-studio/       #   Scenario design and P&L impact
│   ├── ccr-exposure-workbench/       #   Counterparty credit risk analyzer
│   ├── capital-bridge-analyzer/      #   CET1/RWA bridge decomposition
│   ├── liquidity-funding-war-room/   #   LCR/NSFR and margin liquidity
│   ├── model-validation-lab/         #   Model challenge and testing console
│   ├── cross-asset-risk-monitor/     #   Multi-asset class risk dashboard
│   └── prompt-evaluation-console/    #   LLM output evaluation harness
│
├── briefs/                           # Executive brief outputs
│   └── openclaw/                     #   OpenClaw intelligence briefs
│
├── adhoc-analysis/                   # One-off deep-dive packages
│   └── iran-crisis-march-2026/       #   Stress specs, risk assessments, methodology
│
├── deliverables/                     # Consolidated output artifacts
│   ├── scenario-committee/           #   AI scenario committee reports + scripts
│   ├── cro-briefs/                   #   Weekly CRO risk intelligence briefs
│   ├── stress-testing/               #   TOH BAU stress dashboards and reports
│   └── geopolitical/                 #   Persian Gulf impact analysis
│
├── artifacts/                        # Archived reference materials
│   ├── dashboards/                   #   Historical dashboards
│   ├── reports/                      #   Published reports and PDFs
│   └── reference/                    #   Cheat sheets and quick references
│
└── dist/                             # Distribution packages
    └── eqfin-shock-calibrator-portable-*.zip
```

---

## EQ/FX Shock Calibrator (Python GUI)

The flagship standalone tool. Runs on Windows, macOS, and Linux.

**Quick run:**
```bash
# macOS / Linux
chmod +x tools/eqfin-shock-calibrator/run_eqfin_gui.sh
tools/eqfin-shock-calibrator/run_eqfin_gui.sh

# Windows
tools\eqfin-shock-calibrator\run_eqfin_gui.bat
```

**Portable bundle:** `dist/eqfin-shock-calibrator-portable-2026-03-06.zip` — includes all source, data, and cross-platform launch scripts.

---

## Prompt Library Standards

All prompts follow a structured standard defined in [`prompts/PROMPT_STANDARDS.md`](prompts/PROMPT_STANDARDS.md):
- Role-based routing ([`ROLE_BASED_PROMPT_ROUTING.md`](prompts/ROLE_BASED_PROMPT_ROUTING.md))
- Evaluation harness ([`PROMPT_EVALUATION_HARNESS.md`](prompts/PROMPT_EVALUATION_HARNESS.md))
- Red team test bank ([`RED_TEAM_TEST_BANK.md`](prompts/RED_TEAM_TEST_BANK.md))

---

## Skills OS

The Skills OS covers the full CIB Risk professional development lifecycle:

| Category | Skills | Coverage |
|---|---|---|
| Foundations | 8 | Org map, financial math, portfolio aggregation, limits taxonomy |
| Market Risk | 8 | VaR, ES, sensitivities, backtesting, stress, P&L explain, XVA |
| Credit & CCR | 8 | EPE/PFE, netting, margining, WWR, CVA, FVA, limits |
| Liquidity & Funding | 8 | Funding curves, LCR, NSFR, margin liquidity, intraday |
| Stress Testing | 8 | Scenario design, shock calibration, reverse stress, governance |
| Capital & Balance Sheet | 8 | RWA, capital ratios, economic vs regulatory, optimization |
| Model Risk | 8 | SR 11-7, inventory, MDD, VDD, monitoring, change management |
| Regulatory & Audit | 8 | Documentation, issue management, exam readiness, 3LOD |
| Risk Data & Controls | 8 | Data quality, reconciliation, golden source, lineage, KRI |
| Risk Technology | 8 | SQL, Python, notebooks, Power BI, Git, CI/CD, observability |
| Products & Markets | 8 | Rates, FX, credit, equity, commodity, structured, securitized |
| Governance & Process | 8 | Limits, breaches, committee packs, change management, CSA |
| Communication | 8 | Executive writing, data storytelling, stakeholder management |
| AI & Automation | 8 | Agentic AI, prompting standards, RAG, safety, audit, HITL |
| Self-Learning & Career | 8 | Second brain, spaced repetition, portfolio, interview prep |

Each skill includes learning objectives, prerequisite mapping, practical exercises, and assessment criteria.

---

## Tools Suite

Launch all tools locally:
```bash
python3 tools/start_tools_server.py
```

Then open `http://localhost:8000` for the tool index.
