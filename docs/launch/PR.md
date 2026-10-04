# Add a reproducible risk-register browser demo and launch package

Visitors currently have to use Swagger to try register validation. Add a
local browser workflow that runs the existing API, displays affected rows and
recommended fixes, filters severity, and exports findings.

The synthetic messy/corrected samples demonstrate six findings and then
zero findings. Samples use relative dates; no account, API key or LLM is
required. Add Docker setup, an API walkthrough, browser regression checks,
CI, a real browser recording, and practical launch drafts.

The README now distinguishes heuristic register scores and the two-control
mapping subset from organizational compliance or certification. Existing
health and API routes remain compatible.

Validation: 86 tests pass; MyPy and Ruff pass. Browser checks cover uploads,
samples, filtering, export, error recovery, safe rendering and mobile layout.
An XLSX upload also returned the expected six findings. Docker build/run is
not validated in the delivery environment because container sockets/mounts
are unavailable; the CI job builds and exercises the container.

Launch posts are drafts. No external posts, messages or directory submissions
have been sent.
