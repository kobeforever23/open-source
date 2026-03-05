# Verification Policy
**AS-OF:** 2026-03-05 11:49:38 EST

## Scope
Applies to all factual, regulatory, policy, and definition claims in this library.

## Core rules
1. Prefer primary sources: BIS/BCBS, Fed/OCC/SEC/CFTC, ESMA/EBA, IOSCO, ISDA, IMF, exchanges.
2. Every regulatory or official-definition claim must cite source URL inline or in module references.
3. If uncertain or conflicting, label the statement **Unconfirmed** and include competing claims with citations.
4. Separate facts from interpretations; mark inferences explicitly as interpretation.
5. Preserve an audit trail: source date, retrieval date, editor, and confidence score.

## Citation format
- In-text: `... per BCBS FRTB [citation]`.
- References section: bullet list with source title + URL.
- Avoid citation to non-authoritative blogs for normative claims.

## Confidence model
| Score band | Label | Merge rule |
|---|---|---|
| 0.85-1.00 | High | Merge allowed |
| 0.60-0.84 | Medium | Merge with reviewer challenge note |
| 0.40-0.59 | Low | Keep as **Unconfirmed** |
| <0.40 | Reject | Do not include |

## Unconfirmed handling template
```text
Unconfirmed:
- Claim A (source 1)
- Competing claim B (source 2)
Resolution plan: identify primary rule text or supervisory clarification.
```

## Quality gates before merge
- Citation completeness check
- Link validity check
- Dependency/index consistency check
- Changelog entry added with timestamp (America/New_York)
