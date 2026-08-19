from stridefy.models import Category
from stridefy.rules import classify


def test_login():
    assert classify("https://example.com/login") == [
        Category.SPOOFING,
    ]


def test_login_is_not_repudiation():
    assert Category.REPUDIATION not in classify("https://example.com/login")


def test_admin_upload():
    assert classify("https://example.com/admin/upload") == [
        Category.TAMPERING,
        Category.DENIAL_OF_SERVICE,
        Category.ELEVATION_OF_PRIVILEGE,
    ]


def test_information_disclosure():
    assert Category.INFORMATION_DISCLOSURE not in classify(
        "https://example.com/cat.php?id=1"
    )


def test_audit():
    assert classify("https://example.com/audit") == [
        Category.REPUDIATION,
    ]


def test_unmatched_target():
    assert classify("https://example.com/style.css") == []
