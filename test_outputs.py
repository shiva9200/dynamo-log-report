import json
from pathlib import Path

def report():
    with open("/app/report.json") as f:
        return json.load(f)

def test_report_exists():
    """Verifies success criterion 5."""
    assert Path("/app/report.json").exists()

def test_total_requests():
    """Verifies success criterion 2."""
    assert report()["total_requests"] == 6

def test_unique_ips():
    """Verifies success criterion 3."""
    assert report()["unique_ips"] == 3

def test_top_path():
    """Verifies success criterion 4."""
    assert report()["top_path"] == "/index.html"
