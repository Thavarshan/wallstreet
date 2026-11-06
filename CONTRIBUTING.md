# Contributing to Wallstreet

Thank you for helping make Wallstreet a friendly place to learn Python and responsible market research.

## Before you start

- **This is Jerome's hands-on learning project.** Please do not submit completed implementations of numbered learning issues unless the maintainer has asked for that help. Explanations, test suggestions, bug reports, documentation fixes, and small focused improvements are welcome.
- Read the [learning guide](docs/LEARNING_GUIDE.md), [roadmap](docs/ROADMAP.md), and [AI strategy policy](docs/ADAPTIVE_STRATEGY_POLICY.md).
- Everything stays in **research, backtesting, or paper trading**. Never add real-money order placement, withdrawal automation, leveraged trading, or a switch that bypasses safety checks.
- Never commit API keys, account details, personal addresses, paid datasets, or unlicensed news content.

## Find something to work on

1. Check [existing issues](https://github.com/Thavarshan/wallstreet/issues) before opening a duplicate.
2. For bugs, explain how to reproduce the problem and what you expected.
3. For ideas, explain **why** the feature matters, how a beginner might build it, and what tests would prove it works.
4. For security problems, follow [SECURITY.md](SECURITY.md), not a public issue.

## Run the starter project

Use Python 3.12 or newer:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
python -m pytest
```

On Windows, activate the virtual environment with `.venv\Scripts\activate`.

## Submit a pull request

1. Discuss large changes in an issue first; small fixes can go straight to a pull request.
2. Create a branch with a short descriptive name, such as `docs/explain-sqlite`.
3. Make the smallest change that solves the problem. Add tests for changes in behavior.
4. Run `python -m pytest` and explain any tests you could not run.
5. Open the pull request using the provided template and link any related issue.
6. Expect friendly questions and revisions; **maintainer review is required** before merging.

We value clear explanations over clever code. New Python learners should be able to follow your change.

## Data and financial claims

- Cite public data sources and preserve timestamps, time zones, and publication dates.
- Check source licenses and API usage limits before copying data.
- Avoid look-ahead bias in historical tests and include fees and bad outcomes in performance reports.
- Treat any model output as uncertain evidence, not a guaranteed trading signal.
- Do not claim profits, safety, or investment results without verifiable data.

Please read our [Code of Conduct](CODE_OF_CONDUCT.md) when participating.
