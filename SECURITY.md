# Security Policy

Wallstreet is an educational scaffold. It does **not** currently place real orders, control funds, or access bank accounts.

## Supported versions

Security fixes target the latest commit on `main`. No stable release or long-term support branch exists yet.

## Reporting a vulnerability

Please **do not open a public issue** containing an exploit, credentials, account identifiers, or private financial information.

1. Prefer GitHub's **Report a vulnerability** / private vulnerability reporting option in this repository's Security tab, **if it is enabled**.
2. If that option is unavailable, request a private contact method via the [maintainer's GitHub profile](https://github.com/Thavarshan) without including vulnerability details in a public message.
3. Describe the affected files or version, the impact, and how the maintainer can reproduce it safely. Use fake credentials and synthetic market data wherever possible.

Please allow the maintainer time to investigate before disclosing details publicly. No fixed response-time guarantee is offered for this volunteer-run project.

## Safety boundaries

- No live brokerage credentials, bank details, or withdrawal automation in the repository or test fixtures.
- External news, data, and AI-generated text must be treated as **untrusted input**.
- Generated strategy changes require human review and must never bypass independent risk limits.
- GitHub Actions and other free services should use least-privilege tokens, safe dependency versions, and explicit resource limits.
- Do not execute AI-generated code with secrets or unattended production permissions.

See [CONTRIBUTING.md](CONTRIBUTING.md) for general bug reports and contributions.
