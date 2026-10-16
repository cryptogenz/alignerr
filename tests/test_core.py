from aligner.core import check, parse_requirements


def test_parse_requirements():
    text = "# Title\n- First thing\n* Second thing\nnot a bullet"
    assert parse_requirements(text) == ["First thing", "Second thing"]


def test_check_statuses(tmp_path):
    (tmp_path / "app.py").write_text("def export_report():\n    # export results\n    pass\n")
    results = check(
        ["Export results report", "Export results spreadsheet", "Send email notifications"],
        tmp_path,
    )
    assert results["Export results report"] == "implemented"
    assert results["Export results spreadsheet"] == "partial"
    assert results["Send email notifications"] == "missing"
