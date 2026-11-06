# 39 — Promote or roll back paper strategies with an auditable approval trail

**Track:** H · AI-guided improvement  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Complete issues 33–38 first.

## Why we're doing this

An adaptive system needs a safe answer to 'Which algorithm is currently active, who approved it, and can we reverse the change?' Without this, debugging an unexpected loss becomes guesswork.

## Python and market concepts you'll practice

- Finite-state transitions and immutable versions
- Approval records, audit logs, and rollback
- Separation between research, paper trading, and live accounts

## Files to inspect or create

- `src/wallstreet/strategy_registry.py` (new)
- `tests/test_strategy_registry.py` (new)
- `docs/ADAPTIVE_STRATEGY_POLICY.md` (use)

## Build it yourself — step by step

1. Define explicit states `PROPOSED`, `EVALUATING`, `PAPER_CHALLENGER`, `APPROVED_FOR_PAPER`, `REJECTED`, and `ROLLED_BACK`. Real/live is **not** one of these automatic states.
2. Assign each strategy version an immutable identifier linking code commit, configuration hash, evaluation report, dataset version, and human approval.
3. Write a pure transition validator that rejects illegal jumps, e.g., PROPOSED directly to APPROVED without evaluation or paper evidence.
4. Create a manual CLI command that requires confirmation and a review note to promote a candidate to the **paper** champion. Do not let an AI agent invoke it.
5. Keep the previous champion version so rollback is a one-command paper-mode configuration selection, with no rewrite of historical ledgers.
6. Upon promotion, monitor data freshness, risk alerts, error counts, turnover, and paper equity. Implement a conservative automatic *stop* on failure, but not automatic fallback to riskier trading.
7. Show an audit trail listing who approved, when, what changed, supporting evidence, and the reason for a later rollback.
8. Test unauthorized promotion, missing evidence, stale performance data, bad state transitions, rollback correctness, and duplicate approval requests.
9. Write a final report describing whether AI suggestions genuinely improved the champion over several paper-only trials.

## Worked example

AI proposes v3; automated gates pass; v3 runs as challenger; Jerome reviews and manually approves v3 for paper. A later data failure stops new paper orders and records a rollback to v2. No real money moves.

## Tests to write

- [ ] Unapproved versions cannot become paper champion.
- [ ] AI output cannot impersonate a human approval.
- [ ] Rollback restores exact configuration SHA.
- [ ] Audit log keeps old records immutable.
- [ ] No transition enables real trading or withdrawals.

## Acceptance criteria

- [ ] At any timestamp you can identify the active paper algorithm.
- [ ] Promotion and rollback are testable and reversible.
- [ ] The AI cannot deploy or approve itself.

## Common mistake to avoid

Auto-rollback of a trading algorithm is not the same as reversing previously executed orders. Treat historical fills as immutable facts.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

