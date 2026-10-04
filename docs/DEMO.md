# A reproducible AuditPilot walkthrough

## Browser: messy register → findings → corrections

Start the application using the README's Docker or Python quick start. Open
http://127.0.0.1:8000/demo.

1. Click **Try messy sample**. Expected: 3 risks, 6 findings, score 40/100.
2. Show the affected rows. Explain the missing owner, overdue review,
   missing treatment, invalid likelihood and duplicate IDs.
3. Filter **High**. Expected: 5 findings.
4. Click **Export findings CSV**; open it to inspect the recommended fixes.
5. Click **Try corrected sample**. Expected: 0 findings, score 100/100.
6. Explain that the quality score covers the implemented checks only.

The sample download endpoints generate dates relative to today.
The empty state means no findings from these rules, not an audit opinion.

## API: evidence checks and starter control mapping

From `backend`:

```bash
uv run python ../scripts/demo.py --output demo-results.json
```

The walkthrough uploads `draft-policy.txt` and `approved-policy.txt` in an
isolated test-client process, then queries subset coverage and suggested
remediation actions. It deletes the synthetic evidence after each upload.

Expected observations:

- The draft requires human review, even though its keywords map to A.5.1.
- The approved sample receives the API status `Sufficient` because the
  deterministic checks find approval / version markers.
- With only the approved policy uploaded, A.5.1 maps and A.5.2 is a gap:
  **1 of 2 starter controls**, or 50% of the starter subset.
- Suggested remediation for A.5.2 asks for roles / responsibilities evidence.

Do not describe the subset result as an organization's ISO compliance level.

## Recording script (30–45 seconds)

“Risk registers can look complete while still missing important details.
This is AuditPilot, an open-source register-checking toolkit.

Here are three fictional risks. AuditPilot returns six findings, with the
row, field and recommended next step. I can filter high-severity findings
and export the list.

After correcting the register, the same engine finds no issues under its
14 implemented rules. The score is a register-quality heuristic, not
certification.

No account or AI key is needed for this demo. The source and samples are
on GitHub. Try it and tell us what would help your GRC workflow.”

Use synthetic data. Keep the repo URL visible at the end. The included demo
video is a recording of this browser workflow; its pauses are shortened for
readability. No hosted AI inference is shown.

## Browser regression checks (optional for contributors)

With Node 22+ available, run from the repository root:

```bash
npm install --no-save --package-lock=false playwright@1.62.1
npx playwright install chromium
```

Start the API using the quick start, then run in a second terminal:

```bash
node scripts/browser-check.cjs
```

The script checks real requests, sample results, filters, downloads, invalid
file handling, literal rendering of uploaded content, and mobile overflow.
Set `AUDITPILOT_BASE_URL` if the server is on a different local URL. Screenshots
and downloaded findings go to the system temporary directory. The application
itself still needs no Node installation.
