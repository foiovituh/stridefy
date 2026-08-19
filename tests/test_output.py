from stridefy.models import Category, Finding
from stridefy.output import render


def test_render():
    findings = [
        Finding(
            target="https://example.com/login",
            categories=[
                Category.SPOOFING,
                Category.ELEVATION_OF_PRIVILEGE,
            ],
        )
    ]

    output = render(findings)

    assert "(S)poofing:" in output
    assert "https://example.com/login" in output
    assert "(E)levation of Privilege:" in output
