# 36 — Let AI draft algorithm code changes only in an isolated pull request

**Track:** H · AI-guided improvement  
**Estimated learning time:** 8–12 hours  
**Prerequisite:** Complete issues 33–35 and the project test pipeline first.

## Why we're doing this

You also want an agent to develop new strategy algorithms. That is feasible, but generated Python can be buggy, overfit, or intentionally manipulated through untrusted inputs. Isolation and human review keep experimentation from silently changing the working system.

## Python and market concepts you'll practice

- Git branches, pull requests, code review, and Python diff reading
- Sandbox boundaries and least-privilege credentials
- Test-driven change proposals

## Files to inspect or create

- `docs/AI_AGENT_RUNBOOK.md` (new)
- `.github/pull_request_template.md` (new)
- `tests/test_generated_strategy_contract.py` (new)

## Build it yourself — step by step

1. Write a small strategy contract that generated code must implement: pure inputs to a Signal output, explicit reason, no network access, no file writes, no order execution.
2. Explain the difference between changing a JSON parameter and writing new Python code. Begin with configuration PRs; allow code PRs only as a separate advanced exercise.
3. Create an isolated branch from a known commit using a narrowly scoped GitHub credential with no financial secrets. Do not give AI write access to `main`.
4. Provide the agent only sanitized evidence, the strategy interface, allowed file paths, and the exercise goal. Never place account secrets in its workspace.
5. Require a PR that includes `why`, exact files changed, new tests, data usage, risk impact, and a completed experiment template.
6. Review generated code for network calls, subprocess execution, dynamic imports, filesystem side effects, ignored risk checks, dependency changes, and unsafe deserialization.
7. Run tests in a credential-free environment with resource/time limits. Do not run untrusted code in a privileged `pull_request_target` workflow.
8. Reject any PR that edits brokerage credentials, `.github/workflows` permissions, risk ceilings, payout functions, or investor identity fields without separate manual review.
9. Only Jerome can approve a merge. PR creation is not permission to execute a strategy with real money.

## Worked example

A PR adding `MeanReversionCandidate` with tests and an experiment note may be reviewed. A PR that silently replaces `risk.check_order()` with `return True` is automatically rejected.

## Tests to write

- [ ] Generated strategies satisfy a pure function contract.
- [ ] Restricted paths cannot be changed by an automatic agent process.
- [ ] CI runs without broker/Stripe/Wise secrets.
- [ ] A malicious code example fails a static or structural guard.
- [ ] Unmerged PR has no impact on the paper champion.

## Acceptance criteria

- [ ] AI changes arrive as reviewable PRs, not direct main edits.
- [ ] Every PR has tests and a reproducible rationale.
- [ ] The agent has no live-order authority.

## Common mistake to avoid

Never execute AI-generated code with repository administration privileges or live brokerage keys. 'Tests passed' alone does not prove a strategy is safe.

## How to get help without losing the learning experience

Ask your AI tutor to explain one unfamiliar term, show a toy example unrelated to the whole feature, or review **your implementation attempt**. The AI should not solve the issue wholesale unless you explicitly request it. This issue is research/paper-only; no live orders or withdrawals.

