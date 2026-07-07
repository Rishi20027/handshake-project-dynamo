import json
from pathlib import Path

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"

def test_report_contents():
    """The report file contains the correct log processing calculations."""
    with open("/app/report.json", "r") as f:
        data = json.load(f)
        
    assert data.get("total_requests") == 6, f"Expected 6 total requests, got {data.get('total_requests')}"
    assert data.get("unique_ips") == 3, f"Expected 3 unique IPs, got {data.get('unique_ips')}"
    assert data.get("top_path") == "/index.html", f"Expected top path to be '/index.html', got {data.get('top_path')}"
