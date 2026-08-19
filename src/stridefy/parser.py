from pathlib import Path

from .utils import alert


def parse_file(filename: str) -> list[str]:
    try:
        lines = Path(filename).read_text().splitlines()
    except FileNotFoundError:
        alert(f"FILE_NOT_FOUND: {filename}")
    except IsADirectoryError:
        alert(f"MUST_BE_A_FILE: {filename}")
    except UnicodeDecodeError:
        alert(f"UNSUPPORTED_ENCODING: {filename}")

    return [line.strip() for line in lines if line.strip()]
