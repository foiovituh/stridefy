import argparse

from .analyzer import analyze_file
from .output import render


def main():
    parser = argparse.ArgumentParser(
        description="Minimal STRIDE threat modeling helper"
    )

    parser.add_argument(
        "files",
        nargs="+",
        help="Text files containing URLs or endpoints",
    )

    args = parser.parse_args()

    findings = [
        finding for filename in args.files for finding in analyze_file(filename)
    ]

    print(render(findings))
