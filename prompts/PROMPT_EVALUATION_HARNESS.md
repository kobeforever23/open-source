# Prompt Evaluation Harness
**AS-OF:** 2026-03-05 13:56:42 EST

## Purpose
Systematically evaluate prompt quality before production use.

## Test dimensions
- factual groundedness
- control completeness
- decision usefulness
- robustness under missing/contradictory data
- consistency across repeated runs

## Test protocol
1. Run 10-case benchmark set (normal, stressed, adversarial).
2. Score each run on 1-5 rubric dimensions.
3. Fail prompt if any of the following occur:
   - uncited regulatory claims
   - missing owner/due-date in actions
   - non-actionable summary
4. Iterate prompt until pass rate >= 90% and no critical control failures.
