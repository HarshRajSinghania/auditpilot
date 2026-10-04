# Launch copy

Attach `docs/assets/auditpilot-demo.mp4` to the main post. Use the actual
browser screenshot when video is unsuitable. These drafts describe tested
workflows; they do not promise the full ISO framework or an AI copilot.

## Main launch: LinkedIn

Your risk register can look complete and still be missing the basics.

A risk with no owner. A review date that has passed. A duplicated ID.
A likelihood value outside your scoring scale.

We've added a browser demo to AuditPilot, our open-source audit-preparation
toolkit, so you can check a CSV or XLSX and see exactly which rows need review.

The attached walkthrough uses three fictional risks:
→ 6 actionable findings before corrections
→ 0 findings after corrections
→ Exportable findings with recommended next steps

No account or API key is needed. The workflow uses deterministic validation
rules, and the score measures register quality—not certification.

Try the synthetic samples, then tell us: which check would save your team
the most time?

https://github.com/anirudhnshandilya/auditpilot

If you find it useful, a GitHub star helps other security and GRC teams
discover it. Contributions and practical feedback are welcome.

#CyberSecurity #GRC #OpenSource #RiskManagement

## Short launch: X

A missing owner. An overdue review. A duplicate risk ID.

AuditPilot checks CSV/XLSX risk registers and returns row-level fixes.
New local browser demo; no account or AI key needed.

Try the synthetic samples. Star if useful:
https://github.com/anirudhnshandilya/auditpilot

## Walkthrough 1: missing ownership

Who is accountable for this risk?

In our synthetic AuditPilot demo, row 2 has no owner. The check returns a
High finding and recommends assigning an accountable owner.

That is a small validation rule with a useful outcome: a specific row to
review, instead of another manual spreadsheet scan.

The open-source demo includes a messy register and its corrected version.
Try it and suggest a rule your team needs:
https://github.com/anirudhnshandilya/auditpilot

## Walkthrough 2: overdue reviews

An old review date is easy to miss in a spreadsheet.

AuditPilot's synthetic sample includes an overdue review. The validation
engine identifies the row and recommends updating the review date.

The sample is date-relative, so the walkthrough remains reproducible.
The finding is a reminder for human review; updating a date alone does not
prove the risk was reassessed.

CSV/XLSX demo and source:
https://github.com/anirudhnshandilya/auditpilot

## Walkthrough 3: evidence mapping is not approval

A document can match a control and still need human review.

AuditPilot's draft policy sample maps to A.5.1 through keywords, while its
separate quality check flags it as a draft.

The current mapping library contains A.5.1 and A.5.2 only. The walkthrough
makes that scope explicit and shows suggested missing evidence for A.5.2.

We're looking for practical feedback on evidence-review workflows:
https://github.com/anirudhnshandilya/auditpilot

## Show HN

Title: Show HN: AuditPilot – Check risk registers with a local, open-source tool

Link: https://github.com/anirudhnshandilya/auditpilot

First comment:

I'm a co-maintainer of AuditPilot. We built this to make some repetitive
risk-register and evidence-preparation checks easier to inspect and extend.

The current browser workflow validates CSV/XLSX registers with 14 rules,
shows the affected rows and suggested fixes, and exports findings. Synthetic
messy/corrected samples let you try it without an account or AI key.

There is also a deterministic evidence pipeline with a two-control ISO
starter subset. The AI copilot and full reporting dashboard are future work.

You can run it with Docker Compose or Python/uv. I'd appreciate feedback on
setup friction, findings that are unclear, and rules you'd add.

## Individual practitioner invitation (draft; personalize before sending)

Hi [name], I'm working on AuditPilot, an open-source risk-register checking
tool. Could you try the synthetic sample and tell me whether the row-level
findings would help your review workflow? It takes no account or API key,
but requires running the demo locally.

I'm looking for candid feedback, especially confusing findings and missing
checks. No company documents needed:
https://github.com/anirudhnshandilya/auditpilot
