from .models import Category

RULES = {
    Category.SPOOFING: (
        "auth",
        "credential",
        "login",
        "oauth",
        "password",
        "session",
        "signin",
        "sign-in",
        "sso",
        "token",
    ),
    Category.TAMPERING: (
        "create",
        "delete",
        "edit",
        "modify",
        "update",
        "upload",
        "write",
    ),
    Category.REPUDIATION: (
        "activity",
        "audit",
        "audit-log",
        "audit_log",
        "history",
    ),
    Category.INFORMATION_DISCLOSURE: (
        "attachment",
        "backup",
        "config",
        "debug",
        "document",
        "download",
        "dump",
        "export",
        "file",
        "trace",
    ),
    Category.DENIAL_OF_SERVICE: (
        "batch",
        "bulk",
        "generate",
        "import",
        "report",
        "upload",
    ),
    Category.ELEVATION_OF_PRIVILEGE: (
        "admin",
        "administrator",
        "manage",
        "management",
        "permission",
        "privilege",
        "role",
    ),
}


def classify(target: str) -> list[Category]:
    value = target.lower()

    return [
        category
        for category, keywords in RULES.items()
        if any(keyword in value for keyword in keywords)
    ]
