# Learning System
**AS-OF:** 2026-03-05 11:49:38 EST

This system converts the skill library into measurable capability growth (analyst to VP/ED) through cadence, repetition, simulation, and evidence-based assessment.

## 6-week curriculum (beginner -> strong analyst)
| Week | Theme | Required output |
|---|---|---|
| Week 1 | Foundations + Products baseline | Complete 00 modules 1-8 and 10 modules 1-4. |
| Week 2 | Core market + credit/CCR measurement | Complete 01 modules 1-8 and 02 modules 1-4. |
| Week 3 | Liquidity + stress design | Complete 03 modules 1-8 and 04 modules 1-4. |
| Week 4 | Capital + model risk | Complete 05 modules 1-8 and 06 modules 1-4. |
| Week 5 | Regulatory/data/tech execution | Complete 07 modules 1-8, 08 modules 1-8, and 09 modules 1-4. |
| Week 6 | Governance, AI, communication, career | Complete 11-14 categories and deliver final capstone pack. |

## Daily drills (30-60 min) + weekly capstones
1. 10 min retrieval: flashcards from current category and one prior category.
2. 20 min rebuild: reproduce one metric/chart from raw data or prior artifact.
3. 20 min challenge: write one risk decision memo with recommendation and caveats.
4. Weekly capstone: one 2-page pack + 5-minute verbal defense with scoring rubric.

## Flashcard bank (Q/A by category)

### Foundations
- Q: Difference between risk measurement and risk management?  
  A: Measurement quantifies exposure; management adds governance, limits, and action decisions.
- Q: Why keep an audit trail?  
  A: To reproduce numbers, defend decisions, and satisfy supervisory testing.

### Market Risk
- Q: Why complement VaR with ES?  
  A: ES captures average tail loss beyond quantile, improving tail sensitivity.
- Q: What is a clean PnL?  
  A: PnL stripped of fees/new trades/reserves per policy for backtesting comparability.

### Credit/CCR
- Q: EPE vs PFE?  
  A: EPE is expected exposure average; PFE is high-quantile potential exposure.
- Q: Wrong-way risk trigger?  
  A: Exposure increases as counterparty credit quality deteriorates.

### Liquidity
- Q: LCR intent?  
  A: Hold enough HQLA to survive 30-day stressed outflows per Basel rules.
- Q: NSFR intent?  
  A: Promote stable funding profile over one-year horizon.

### Stress
- Q: Reverse stress testing goal?  
  A: Identify scenarios that break risk appetite/capital/liquidity thresholds.
- Q: Macro-to-market mapping?  
  A: Translate macro narrative to tradable factor shocks and portfolio impacts.

### Capital
- Q: Regulatory vs economic capital?  
  A: Regulatory follows rules; economic capital reflects internal loss distribution/risk appetite.
- Q: Why capital bridge?  
  A: Explains period-over-period ratio changes by drivers.

### Model Risk
- Q: Core SR 11-7 principle?  
  A: Models require governance across development, validation, and use monitoring.
- Q: Validation independence?  
  A: Independent challenge reduces confirmation bias and control failure risk.

### Regulatory/Audit
- Q: CAPA quality marker?  
  A: Root-cause-based corrective action with tested effectiveness evidence.
- Q: Exam room mistake?  
  A: Producing conflicting evidence versions without source-of-truth references.

### Data/Controls
- Q: Data quality dimensions?  
  A: Accuracy, completeness, timeliness, consistency, validity, uniqueness.
- Q: Golden source?  
  A: Authoritative dataset approved for a defined metric/use case.

### Tech/Engineering
- Q: Why CI for risk code?  
  A: Prevent regression in calculations and control checks before deployment.
- Q: Reproducible notebook means?  
  A: Deterministic run with pinned dependencies, data version, and logged outputs.

### Products/Markets
- Q: Rates swap primary sensitivities?  
  A: DV01/curve key rates and convexity/vol for optionality.
- Q: FX option key greeks?  
  A: Delta, vega, gamma plus smile/term structure exposures.

### Governance/Process
- Q: Effective breach escalation?  
  A: Predefined thresholds, owners, time-bound decisions, and evidence.
- Q: RAID log purpose?  
  A: Track risks, assumptions, issues, dependencies with ownership.

### Communication/Leadership
- Q: Executive summary structure?  
  A: Decision, risk signal, evidence, options, recommendation, owner/date.
- Q: Challenge meeting success?  
  A: Decisions captured with dissent, rationale, and follow-up actions.

### AI/Automation
- Q: LLM control minimum?  
  A: Grounded sources, evaluation tests, human approval gate, full logging.
- Q: RAG failure mode?  
  A: Retrieving stale/low-authority docs without confidence checks.

### Self-Learning/Career
- Q: Deliberate practice loop?  
  A: Plan, attempt, feedback, correction, re-test weekly.
- Q: Portfolio of evidence?  
  A: Curated artifacts proving analytical, control, and communication impact.

## Case-study bank (10 cases) with scoring rubric
| Case | Prompt | Scoring rubric (0-5 each) |
|---|---|---|
| Rates shock + basis widening | Desk has sudden DV01 and basis concentration; design limit actions and hedge proposals. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Counterparty downgrade week | Large bilateral exposures and collateral disputes emerge after ratings actions. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Liquidity squeeze | Margin calls spike while funding spread widens and HQLA eligibility tightens. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Backtesting exceptions cluster | Three-day exception streak raises model and governance questions. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Structured note warehousing risk | Pipeline inventory sensitivity profile diverges from approved risk appetite. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Data lineage break in VaR feed | Upstream mapping change causes unexplained exposure jump. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Audit finding on evidence quality | Validation evidence lacks reproducibility and reviewer sign-off. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| AI copiloting pilot in risk reporting | Need approval gates and hallucination controls before production use. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Capital ratio compression under stress | Stress scenario breaches management buffer; propose mitigants. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |
| Committee communication failure | Important downside risk buried in appendix; redesign pack and narration. | Problem framing; Quant rigor; Control evidence; Decision quality; Communication clarity |

## Skills assessment checklist with levels
| Level | Capability signal | Evidence required |
|---|---|---|
| L1 | Understands definitions and process flow | Flashcards >=80% and one clean walkthrough |
| L2 | Executes analysis with guidance | Reproducible notebook/query + review comments addressed |
| L3 | Owns end-to-end deliverable | Committee-ready memo + control evidence pack |
| L4 | Leads and improves system | Drives change, mentors others, and closes control gaps |

## Spaced repetition cadence
- Day 1: learn and test immediately.
- Day 3: first review with mixed-category retrieval.
- Day 7: second review with applied mini-case.
- Day 14: third review with peer challenge.
- Day 30: consolidation review and rubric scoring.
