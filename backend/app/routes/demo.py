from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse, Response

from app.demo.samples import SampleName, risk_register_csv

router = APIRouter(prefix="/demo", tags=["Demo"])
STATIC_DIRECTORY = Path(__file__).resolve().parents[1] / "static"


@router.get("", include_in_schema=False)
@router.get("/", include_in_schema=False)
def demo_page() -> FileResponse:
    return FileResponse(STATIC_DIRECTORY / "index.html")


@router.get("/samples/{filename}")
def download_sample(filename: str) -> Response:
    if filename not in {"messy.csv", "corrected.csv"}:
        raise HTTPException(status_code=404, detail="Sample not found.")
    sample: SampleName = "messy" if filename == "messy.csv" else "corrected"
    return Response(
        content=risk_register_csv(sample),
        media_type="text/csv",
        headers={
            "Content-Disposition": f'attachment; filename="{filename}"',
            "Cache-Control": "no-store",
        },
    )
