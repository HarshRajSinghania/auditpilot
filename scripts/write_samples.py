"""Refresh downloadable synthetic CSV examples using today's date."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "backend"))
from app.demo.samples import risk_register_csv  # noqa: E402

for name in ("messy", "corrected"):
    (ROOT / "examples" / f"{name}-risk-register.csv").write_text(
        risk_register_csv(name), encoding="utf-8"
    )
