# Current architecture

FastAPI serves the API and a small browser interface. The interface calls
`POST /upload/risk-register`, which parses CSV / XLSX data and runs the
existing rule registry. Findings include severity, row, column, explanation,
and recommendation. The browser renders text without interpreting uploaded
values as HTML and exports a findings CSV.

Synthetic CSVs are generated through `/demo/samples/` using dates relative
to today. The walkthrough script exercises the same API via TestClient or
a running local server.

The evidence pipeline parses files, extracts metadata and text, classifies
documents, and evaluates deterministic draft / approval / version checks.
Evidence is stored in a process-local in-memory repository.

The framework engine matches keywords against A.5.1 / A.5.2 only. Mapping,
subset coverage and evidence-quality status are distinct results. Coverage
currently counts keyword mappings even when an evidence document requires
human review. Suggested remediation actions are derived from uncovered
starter controls, rather than persisted in a task system.

The Docker setup runs one worker so evidence requests share the same
in-memory repository. It is intended for local evaluation. Shared deployments
need additional application controls and persistence, as described in the
roadmap and SECURITY.md.
