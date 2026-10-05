from datetime import date, timedelta
from io import BytesIO

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_upload_valid_csv() -> None:
    first_review = (date.today() + timedelta(days=365)).isoformat()
    second_review = (date.today() + timedelta(days=540)).isoformat()
    csv_content = (
        "Risk ID,Title,Description,Owner,Treatment,Likelihood,Impact,Review Date\n"
        "R001,Weak Password Policy,Weak passwords across systems,IT Manager,"
        f"Implement MFA,4,5,{first_review}\n"
        "R002,Missing MFA,MFA is not enabled,Security Team,"
        f"Roll out MFA,5,5,{second_review}\n"
    ).encode()

    response = client.post(
        "/upload/risk-register",
        files={
            "file": (
                "risk-register.csv",
                BytesIO(csv_content),
                "text/csv",
            )
        },
    )

    assert response.status_code == 200
    assert response.json() == {
    "filename": "risk-register.csv",
    "status": "validated",
    "rows": 2,
    "columns": 8,
    "column_names": [
        "Risk ID",
        "Title",
        "Description",
        "Owner",
        "Treatment",
        "Likelihood",
        "Impact",
        "Review Date",
    ],
    "score": 100,
    "audit_readiness": "Ready",
    "findings": [],
}


def test_reject_unsupported_file_type() -> None:
    response = client.post(
        "/upload/risk-register",
        files={
            "file": (
                "risk-register.txt",
                BytesIO(b"unsupported"),
                "text/plain",
            )
        },
    )

    assert response.status_code == 400


def test_reject_empty_file() -> None:
    response = client.post(
        "/upload/risk-register",
        files={
            "file": (
                "risk-register.csv",
                BytesIO(b""),
                "text/csv",
            )
        },
    )

    assert response.status_code == 400
