from stridefy.analyzer import analyze_file
from stridefy.models import Category


def test_analyze_file(tmp_path):
    target = tmp_path / "targets.txt"
    target.write_text("https://example.com/admin/login\n")

    findings = analyze_file(target)

    assert len(findings) == 1
    assert findings[0].target == "https://example.com/admin/login"
    assert findings[0].categories == [
        Category.SPOOFING,
        Category.ELEVATION_OF_PRIVILEGE,
    ]
