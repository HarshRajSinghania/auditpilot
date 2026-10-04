from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routes.demo import router as demo_router

from app.routes.upload import router as upload_router
from app.routes.evidence import router as evidence_router
from app.routes.frameworks import router as frameworks_router
from app.routes.remediation import router as remediation_router

app = FastAPI(
    title="AuditPilot API",
    description="Open-source ISO 27001 readiness assistant.",
    version="0.1.0",
)

app.include_router(demo_router)
app.mount(
    "/demo-assets",
    StaticFiles(directory=Path(__file__).resolve().parent / "static"),
    name="demo-assets",
)

app.include_router(upload_router)
app.include_router(evidence_router)
app.include_router(frameworks_router)
app.include_router(remediation_router)


@app.get("/", tags=["Health"])
def root() -> dict[str, str]:
    return {
        "status": "healthy",
        "project": "AuditPilot",
        "version": "0.1.0",
    }


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {"status": "healthy"}
