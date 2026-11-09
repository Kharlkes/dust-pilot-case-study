"""Checks for the independent fixture calculator, not for Dust itself."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class FixtureTests(unittest.TestCase):
    def test_expected_results_and_blank_open_ticket_hours(self):
        script = ROOT / "scripts" / "check_fixture.py"
        self.assertTrue(script.is_file(), "The independent fixture calculator is missing")
        spec = importlib.util.spec_from_file_location("check_fixture", script)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        self.assertEqual(module.summarize(ROOT / "data" / "support_tickets.csv"), {
            "total_tickets": 40,
            "billing_tickets": 14,
            "open_high_priority_tickets": 4,
            "closed_export_resolution_hours": 160,
        })
        with tempfile.TemporaryDirectory() as directory:
            tiny = Path(directory) / "tiny.csv"
            tiny.write_text(
                "id,date,customer,category,priority,status,resolution_hours\n"
                "T1,2026-10-01,Fictional,Billing,High,Open,\n"
                "T2,2026-10-02,Fictional,Export,Low,Closed,7\n",
                encoding="utf-8",
            )
            self.assertEqual(module.summarize(tiny), {
                "total_tickets": 2,
                "billing_tickets": 1,
                "open_high_priority_tickets": 1,
                "closed_export_resolution_hours": 7,
            })


if __name__ == "__main__":
    unittest.main()
