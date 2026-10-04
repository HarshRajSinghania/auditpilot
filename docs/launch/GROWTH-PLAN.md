# Adoption and distribution plan

Goal: grow from the maintainer-reported 184 stars to 5,000. This is a goal,
not a forecast. The difference is 4,816 stars. There is no fixed deadline or
guaranteed conversion rate.

## Before publishing

- Push the launch branch, let CI complete, then review and merge.
- Test the README commands on a clean machine. The Docker build is covered
  by CI; local delivery validation may lack a Docker daemon.
- Watch the actual browser recording. Confirm all public examples are synthetic.
- Pin AuditPilot on the maintainer profile if it is the current priority.
- Suggested repository description: "Open-source risk-register validation,
  evidence checks, and audit-preparation workflows. CSV/XLSX browser demo."
- Relevant topics: `grc`, `risk-management`, `compliance`, `iso27001`,
  `audit-automation`, `cybersecurity`, `fastapi`, `python`.
- Keep the existing maintainer credits and Apache 2.0 license.

## First distribution cycle

| Sequence | Action | Outcome to observe |
|---|---|---|
| 1 | Publish the main post with the browser video | Visitors, clones, setup reports |
| 2 | Share the missing-owner walkthrough | Which rules practitioners value |
| 3 | Share the overdue-review walkthrough | Useful feedback about date handling |
| 4 | Share the evidence-review walkthrough | Feedback on mapping versus evidence quality |
| 5 | Make a Show HN submission and answer questions | Technical evaluation and reproducibility |
| 6 | Invite 10 relevant practitioners individually | Aim for 5 actual trials; record feedback |
| 7 | Fix the most common setup or workflow problem | A concrete improvement to demonstrate next |

These are sequences, not scheduled automations. Do not publish identical
messages across communities. Check each community's current rules and use
its allowed showcase threads. Show HN requires something people can try;
do not ask people to coordinate votes.

## Practitioner feedback

Select people with actual GRC / risk review experience. Ask them to use the
synthetic sample, not sensitive company evidence. Use the invitation draft
in POSTS.md, personalized to their work. Log consented feedback rather than
adding names or quotes to public marketing without permission.

Questions:

1. Could you start the demo from the README?
2. Which finding was useful or confusing?
3. Would you use this as part of your current workflow? Why?
4. What is the first missing check or integration?

## Measure weekly

Use the repository's GitHub Insights → Traffic page for visitors and clones;
those data require repository permissions. Stars alone do not show adoption.
Start with `metrics.csv`, entering actual measurements. Leave unavailable
metrics blank. Different platform impression counts are not repository visits.

Milestones: 250 → 500 → 1,000 → 2,500 → 5,000. At each milestone, report a
real product improvement or user lesson. Do not invent usage numbers,
certification outcomes, time savings, endorsements or partnerships.

## Relevant directories

Prioritize GRC / compliance / security tooling lists that accept this kind
of early-stage project. Inspect their contribution requirements and existing
entries first; do not scatter unrelated listing PRs. An existing AuditPilot
submission was found at https://github.com/Hack-with-Github/Awesome-Hacking/pull/233;
check its state before creating a duplicate. A directory listing is secondary
to a demonstrable, useful workflow.

## Next product work, based on feedback

- Normalize supported spreadsheet headers without hiding invalid data.
- Add persistent findings / actions when users need recurring reviews.
- Expand control mapping through reviewed, properly scoped contributions.
- Add evidence-quality gating before treating a keyword match as coverage.
- Improve human review and reports before advertising broader readiness.
