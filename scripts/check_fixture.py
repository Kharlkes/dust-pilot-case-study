"""Recompute expected answers from the synthetic CSV. Never calls Dust."""
import csv
import json
from pathlib import Path


def summarize(path):
    with Path(path).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {
        "total_tickets": len(rows),
        "billing_tickets": sum(row["category"] == "Billing" for row in rows),
        "open_high_priority_tickets": sum(
            row["status"] == "Open" and row["priority"] == "High" for row in rows
        ),
        "closed_export_resolution_hours": sum(
            int(row["resolution_hours"])
            for row in rows
            if row["status"] == "Closed" and row["category"] == "Export"
        ),
    }


if __name__ == "__main__":
    print(json.dumps(summarize(Path(__file__).resolve().parents[1] / "data" / "support_tickets.csv"), indent=2))
