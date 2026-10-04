import csv
from datetime import date, timedelta
from io import StringIO
from typing import Literal

SampleName = Literal["messy", "corrected"]
COLUMNS = [
    "Risk ID", "Title", "Description", "Owner", "Treatment",
    "Likelihood", "Impact", "Review Date",
]


def risk_register_csv(sample: SampleName, today: date | None = None) -> str:
    """Generate the same six defects without relying on fixed calendar dates."""
    today = today or date.today()
    future = (today + timedelta(days=90)).isoformat()
    overdue = (today - timedelta(days=30)).isoformat()
    rows: list[list[str | int]] = [
        ["R001", "Cloud admin access", "Privileged accounts lack strong MFA",
         "Security", "Require phishing-resistant MFA", 4, 5, future],
        ["R002", "Backup recovery", "Restore testing is incomplete",
         "Platform", "Schedule and record restore tests", 3, 4, future],
        ["R003", "Laptop encryption", "Some endpoints are not encrypted",
         "IT", "Enforce disk encryption", 3, 4, future],
    ]
    if sample == "messy":
        rows[0][3] = ""
        rows[0][7] = overdue
        rows[1][0] = "R001"
        rows[1][4] = ""
        rows[2][5] = 9
    buffer = StringIO(newline="")
    writer = csv.writer(buffer, lineterminator="\n")
    writer.writerow(COLUMNS)
    writer.writerows(rows)
    return buffer.getvalue()
