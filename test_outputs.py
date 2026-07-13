import json
from pathlib import Path


def load_report():
    with open("/app/report.json") as f:
        return json.load(f)


def test_report_exists():
    """Verifies Success Criterion 5."""
    assert Path("/app/report.json").exists()


def test_total_requests():
    """Verifies Success Criterion 2."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Verifies Success Criterion 3."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Verifies Success Criterion 4."""
    assert load_report()["top_path"] == "/index.html"
