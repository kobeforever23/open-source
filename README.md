# Open Source CIB Risk Workspace

Production-ready CIB Risk workspace with prompts, skills, tools, briefs, and archived reference artifacts.

## Start Here
- `prompts/`: production prompt library (with role/category routing)
- `skills/`: CIB Risk Skills OS and operating standards
- `tools/`: standalone HTML/Python risk tooling suite
- `briefs/`: executive brief outputs and briefing artifacts
- `adhoc-analysis/`: one-off deep-dive analysis packages
- `artifacts/`: archived dashboards, reports, and references

## Quick Navigation
| If you need... | Go to | Notes |
|---|---|---|
| CRO and desk prompts | `prompts/` | Includes a full CRO weekly brief template |
| Skill framework and governance | `skills/cib-risk-skills-os/` | Verification and update playbooks included |
| Interactive risk tools | `tools/` | Run local server via `python3 tools/start_tools_server.py` |
| OpenClaw brief files | `briefs/openclaw/` | Includes color version and prior brief |
| Iran crisis ad hoc package | `adhoc-analysis/iran-crisis-march-2026/` | Source docs + methodology + generation prompt |
| Legacy one-off dashboards/exports | `artifacts/` | Organized by dashboard/report/reference |

## Repository Layout
```text
open-source/
  prompts/
  skills/
  tools/
  briefs/
    openclaw/
  adhoc-analysis/
    iran-crisis-march-2026/
  artifacts/
    dashboards/
    reports/
    reference/
  misc/  (legacy pointer only)
```

## Notes
- Legacy materials were moved from `misc/` into `artifacts/` for cleaner navigation.
- `misc/` is retained only as a compatibility pointer.
