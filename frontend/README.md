# Browser demo

The first browser workflow is implemented in `backend/app/static/` and served
by the existing FastAPI application at `/demo`. It uses the real register
validation API, bundled synthetic samples, severity filters, and CSV exports.

No Node installation, frontend build, account, or LLM key is needed.

From the repository root:

```bash
docker compose up --build
```

Or from `backend`:

```bash
uv sync --frozen
uv run uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/demo.

This is a focused register-checking interface, not the planned full reporting
and evidence-management dashboard. The existing API remains at `/docs`.
