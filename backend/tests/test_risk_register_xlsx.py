"""Exercise XLSX uploads without binary fixtures or clock-dependent dates."""

from datetime import date, timedelta
from io import BytesIO

import pandas as pd
from fastapi.testclient import TestClient

from app.main import app


def workbook(owner: str = "Security Team") -> BytesIO:
    review = (date.today() + timedelta(days=365)).isoformat()
    frame = pd.DataFrame(
        [
            {
                "Risk ID": "R001",
                "Title": "Missing MFA",
                "Description": "MFA is not enabled",
                "Owner": owner,
                "Treatment": "Roll out MFA",
                "Likelihood": 4,
                "Impact": 5,
                "Review Date": review,
            },
            {
                "Risk ID": "R002",
                "Title": "Weak passwords",
                "Description": "Weak passwords across systems",
                "Owner": "IT Manager",
                "Treatment": "Improve password policy",
                "Likelihood": 3,
                "Impact": 4,
                "Review Date": review,
            },
        ]
    )
    output = BytesIO()
    frame.to_excel(output, index=False)
    output.seek(0)
    return output


def upload(contents: BytesIO) -> dict[str, object]:
    with TestClient(app) as client:
        response = client.post(
            "/upload/risk-register",
            files={"file": ("risk-register.xlsx", contents,
                            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")},
        )
    assert response.status_code == 200
    return response.json()


def test_valid_xlsx_returns_complete_result() -> None:
    result = upload(workbook())
    assert result == {
        "filename": "risk-register.xlsx",
        "status": "validated",
        "rows": 2,
        "columns": 8,
        "column_names": ["Risk ID", "Title", "Description", "Owner", "Treatment",
                         "Likelihood", "Impact", "Review Date"],
        "score": 100,
        "audit_readiness": "Ready",
        "findings": [],
    }


def test_missing_xlsx_owner_has_row_level_finding() -> None:
    result = upload(workbook(owner=""))
    findings = result["findings"]
    assert isinstance(findings, list)
    owner_findings = [finding for finding in findings if finding["column"] == "Owner"]
    assert len(owner_findings) == 1
    assert owner_findings[0]["row"] == 2
    assert result["score"] != 100


def test_non_excel_bytes_return_useful_parsing_error() -> None:
    with TestClient(app) as client:
        response = client.post(
            "/upload/risk-register",
            files={"file": ("risk-register.xlsx", BytesIO(b"not an Excel workbook"),
                            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")},
        )
    assert response.status_code == 400
    assert response.json() == {"detail": "The uploaded file could not be parsed."}
