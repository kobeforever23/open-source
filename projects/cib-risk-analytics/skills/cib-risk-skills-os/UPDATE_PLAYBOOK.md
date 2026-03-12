# Update Playbook
**AS-OF:** 2026-03-05 11:49:38 EST

## Objective
Keep this library current, source-grounded, and audit-defensible as regulations, markets, products, and tooling evolve.

## Weekly update routine
1. Pull watchlist updates from [sources/rss_and_watchlist.md](sources/rss_and_watchlist.md).
2. Capture deltas in a triage table: source, claim, impacted skills, confidence score.
3. Open a branch and update affected modules with citations.
4. Run diff review checklist (below) and open a PR.
5. Require reviewer sign-off from domain owner + control owner.
6. Merge and append dated entry to [CHANGELOG.md](CHANGELOG.md).

## Monthly deep refresh
1. Re-evaluate authoritative source ranking in [sources/authoritative_sources.md](sources/authoritative_sources.md).
2. Review new regulations, consultation papers, enforcement actions, and market incidents.
3. Refresh skill gaps: add/retire modules, update dependencies, revise drills and cases.
4. Rebuild optional RAG index and rerun citation/link checks.

## Diff-based review policy
- Every changed factual claim must include at least one authoritative citation.
- Regulatory/policy claims require primary source citation (rule text/guidance).
- If evidence conflicts, mark claim **Unconfirmed** and list competing sources.
- PR must include rationale: why changed, risk impact, and expected user behavior change.

## Confidence scoring rule
- `High (0.85-1.00)`: primary regulator/standard-setter source, explicit text match.
- `Medium (0.60-0.84)`: strong secondary summary corroborated by at least one primary source.
- `Low (0.40-0.59)`: early signal or incomplete text; keep as **Unconfirmed**.
- `<0.40`: do not merge into core skill guidance.

## Suggested tooling
- RSS/Atom reader for recurring sources.
- GitHub PR workflow with CODEOWNERS reviews.
- Automated link checker (weekly) and markdown linting.
- Optional: RAG index rebuild for local search assistant after merge.

## Update artifacts
- `delta_log.md` (working file during updates)
- PR template with source links and confidence fields
- Evidence bundle: screenshots/PDF snapshots of key source passages where needed
