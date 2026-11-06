# 37 — Automatically evaluate AI-proposed strategies before human review

**Track:** H · AI-guided improvement  
**Estimated learning time:** 8–12 hours  
**Prerequisite:** Complete issues 31–36 first.

## Why we're doing this

An AI agent should not get to declare its own strategy a winner. A separate deterministic evaluation process must check the evidence and reject regressions, data leakage, unsafe risk exposure, and hidden costs.

## Python and market concepts you'll practice

- CI quality gates and machine-readable evaluation reports
- Benchmark comparisons, confidence intervals, and minimum evidence
- Independence of proposal and evaluator

## Files to inspect or create

- `src/wallstreet/research/gates.py` (new)
- `tests/test_candidate_gates.py` (new)
- `.github/workflows/evaluate-candidate.yml` (new)

## Build it yourself — step by step

1. Define a `CandidateEvaluation` record with configuration SHA, dataset snapshot, code commit, evaluated folds, costs, risk metrics, and decisions.
2. Build hard safety gates first: no future leakage, valid strategy interface, permitted assets, risk-policy unchanged, tests passing, and reproducible data.
3. Add softer research criteria defined *before* testing: comparison to champion, cash, and benchmark; drawdown, turnover, fees, and fold stability.
4. Return one of `REJECTED`, `NEEDS_MORE_EVIDENCE`, or `ELIGIBLE_FOR_PAPER_CHALLENGER`. Never return `LIVE_APPROVED`.
5. Execute evaluation on deterministic historical fixtures and licensed datasets with explicit quotas. Use caching to avoid paid repeated computation.
6. Publish a Markdown or JSON report attached to the PR, showing *all* candidate metrics and failed checks.
7. Require manual review if a candidate's performance advantage is small relative to uncertainty or changes sign after costs.
8. Treat a failed or timed-out job as rejection, not automatic approval.
9. Test toy strategies: always BUY, never trade, use future returns illegally, and a valid low-activity strategy.

## Worked example

Candidate net return exceeds champion by 1%, but maximum drawdown is twice as large and one walk-forward fold failed. Gate result is `NEEDS_MORE_EVIDENCE` or `REJECTED`, not an automatic winner.

## Tests to write

- [ ] Any hard safety gate failure prevents eligibility.
- [ ] Out-of-sample metrics are required.
- [ ] An evaluation timeout fails closed.
- [ ] No candidate result changes live or paper champion state.
- [ ] Report includes full costs, losses, and source versions.

## Acceptance criteria

- [ ] Evaluation is independent of the LLM's narrative.
- [ ] Result states are reproducible and conservative.
- [ ] Human approval remains mandatory.

## Common mistake to avoid

Don't secretly change thresholds after seeing which candidate won. Avoid treating one lucky period as sufficient evidence.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

