"""Run the real API against synthetic samples; no LLM or credentials required.

From backend: uv run python ../scripts/demo.py
Optional: --base-url http://127.0.0.1:8000 to exercise a running server.
"""
import argparse
import json
import sys
from pathlib import Path

import httpx
from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))
from app.main import app  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def walkthrough(client: httpx.Client | TestClient) -> dict[str, object]:
    report: dict[str, object] = {}
    for name in ("messy", "corrected"):
        sample = client.get(f"/demo/samples/{name}.csv")
        sample.raise_for_status()
        response = client.post(
            "/upload/risk-register",
            files={"file": (f"{name}.csv", sample.content, "text/csv")},
        )
        response.raise_for_status()
        data = response.json()
        report[name] = data
        print(f"{name.upper()}: {data['rows']} risks | "
              f"{len(data['findings'])} findings | quality score {data['score']}/100")
        for finding in data["findings"]:
            print(f"  Row {finding['row']} | {finding['column']} | {finding['message']}")
        expected = 6 if name == "messy" else 0
        if len(data["findings"]) != expected:
            raise RuntimeError(f"Expected {expected} findings in {name} sample.")

    # Each uploaded document is removed afterwards so running the walkthrough
    # against an existing local server does not leave demo evidence behind.
    evidence_results: list[dict[str, object]] = []
    for filename in ("draft-policy.txt", "approved-policy.txt"):
        response = client.post(
            "/evidence/upload",
            files={"file": (filename, (ROOT / "examples" / filename).read_bytes(), "text/plain")},
        )
        response.raise_for_status()
        data = response.json()
        try:
            evidence_results.append(data)
            print(f"{filename}: {data['evidence_status']} | "
                  f"mapped controls {[m['control_id'] for m in data['control_mappings']]}")
            if filename == "approved-policy.txt":
                coverage = client.get("/frameworks/iso27001/coverage")
                coverage.raise_for_status()
                actions = client.get("/remediation/actions")
                actions.raise_for_status()
                report["starter_subset_coverage"] = coverage.json()
                report["starter_subset_actions"] = actions.json()
                print("Coverage is for the two-control starter subset only.")
        finally:
            client.delete(f"/evidence/{data['id']}").raise_for_status()
    report["evidence"] = evidence_results
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base-url", help="Exercise a running local API instead of TestClient")
    parser.add_argument("--output", type=Path, help="Save captured API responses as JSON")
    args = parser.parse_args()
    client = (
        httpx.Client(base_url=args.base_url.rstrip("/"), timeout=30)
        if args.base_url else TestClient(app)
    )
    with client:
        report = walkthrough(client)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        print(f"Captured responses: {args.output}")


if __name__ == "__main__":
    main()
