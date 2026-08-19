from .models import Category, Finding

NAMES = {
    Category.SPOOFING: "poofing",
    Category.TAMPERING: "ampering",
    Category.REPUDIATION: "epudiation",
    Category.INFORMATION_DISCLOSURE: "nformation Disclosure",
    Category.DENIAL_OF_SERVICE: "enial of Service",
    Category.ELEVATION_OF_PRIVILEGE: "levation of Privilege",
}


def render(findings: list[Finding]) -> str:
    if not any(finding.categories for finding in findings):
        return "NO_STRIDE_CATEGORIES_MATCHED"

    sections = []

    for category in Category:
        targets = [
            finding.target for finding in findings if category in finding.categories
        ]

        if not targets:
            continue

        lines = [f"({category.value}){NAMES[category]}:"]
        lines.extend(targets)
        sections.append("\n".join(lines))

    return "\n\n".join(sections)
