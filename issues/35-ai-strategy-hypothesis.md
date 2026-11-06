# 35 — Ask AI to propose testable strategy hypotheses and bounded parameter changes

**Track:** H · AI-guided improvement  
**Estimated learning time:** 6–10 hours  
**Prerequisite:** Complete issue 34 first.

## Why we're doing this

The first useful role for an AI agent isn't writing live trading code. It is suggesting specific hypotheses that can be falsified. Small versioned configuration changes are easier to understand, compare, and undo than arbitrary rewritten algorithms.

## Python and market concepts you'll practice

- LLM structured output with JSON validation
- Hypotheses, supporting evidence, counterevidence, and ablation tests
- Configuration allowlists and parameter boundaries

## Files to inspect or create

- `src/wallstreet/agents/proposals.py` (new)
- `src/wallstreet/strategy_config.py` (extend)
- `tests/test_agent_proposals.py` (new)

## Build it yourself — step by step

1. Define a `StrategyProposal` model: hypothesis, evidence-pack ID, proposed changes, reason, alternative explanation, expected failure cases, and evaluation plan.
2. Write a prompt that explicitly asks the model to state uncertainty and list reasons **not** to trust the hypothesis. Provide structured evidence only.
3. Restrict initial AI suggestions to allowlisted parameters (e.g., trend threshold, lookback window, max frequency), with strict numerical bounds.
4. Forbid any parameter that weakens the risk engine, permits leverage, increases hard exposure caps, changes credentials, or touches withdrawal logic.
5. Use a local deterministic fake model for tests. Only later connect a free inference service with a daily quota and automatic no-AI fallback.
6. Validate the JSON response against the schema. If malformed, stale, unsupported, or out of bounds, reject it with a clear reason.
7. Persist both accepted and rejected proposals for audit, including model/version, input pack ID, timestamp, and the reason for rejection.
8. Generate an experiment note using `docs/EXPERIMENT_TEMPLATE.md` *before* running a backtest.
9. Do not apply the proposal automatically. The output is a candidate configuration and a human-readable plan.

## Worked example

AI proposes `increase trend confirmation from 2 to 3 completed sessions` because signals whipsawed. This is testable. `Buy the next breakout with all available cash` is invalid and rejected.

## Tests to write

- [ ] Allowed parameter changes pass schema validation.
- [ ] Risk-limit loosening is always rejected.
- [ ] Unknown strategy names and invalid JSON fail closed.
- [ ] Repeated proposal has stable ID and isn't duplicated.
- [ ] No proposal calls a broker.

## Acceptance criteria

- [ ] Every proposal can be explained and tested.
- [ ] No generated setting bypasses risk controls.
- [ ] The AI can be unplugged without breaking the baseline strategy.

## Common mistake to avoid

A plausible narrative about a volatile market is not evidence that a new parameter improves out-of-sample performance.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

