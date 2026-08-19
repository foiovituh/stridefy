from .models import Finding
from .parser import parse_file
from .rules import classify


def analyze_file(filename: str) -> list[Finding]:
    return [
        Finding(target=target, categories=classify(target))
        for target in parse_file(filename)
    ]
