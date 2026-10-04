FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.12.19 /uv /uvx /bin/
ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"
WORKDIR /app
COPY backend/pyproject.toml backend/uv.lock backend/README.md ./
RUN uv sync --frozen --no-dev --no-install-project \
    && groupadd --gid 10001 auditpilot \
    && useradd --uid 10001 --gid 10001 --no-create-home auditpilot
COPY backend/app ./app
USER auditpilot
EXPOSE 8000
HEALTHCHECK --interval=5s --timeout=3s --start-period=15s --retries=12 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)" || exit 1
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
