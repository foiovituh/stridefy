from dataclasses import dataclass
from enum import Enum


class Category(Enum):
    SPOOFING = "S"
    TAMPERING = "T"
    REPUDIATION = "R"
    INFORMATION_DISCLOSURE = "I"
    DENIAL_OF_SERVICE = "D"
    ELEVATION_OF_PRIVILEGE = "E"


@dataclass
class Finding:
    target: str
    categories: list[Category]
