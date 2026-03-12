"""
Sample Data Loader — Starter Template
Minimal utility for loading and validating CSV risk data.
"""

import csv
import sys
import argparse
from pathlib import Path


def load_csv(filepath: str) -> list[dict]:
    """Load a CSV file and return rows as list of dicts."""
    path = Path(filepath)
    if not path.exists():
        print(f"Error: File not found: {filepath}")
        sys.exit(1)

    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Loaded {len(rows)} rows from {filepath}")
    return rows


def validate_columns(rows: list[dict], required: list[str]) -> bool:
    """Check that all required columns are present."""
    if not rows:
        print("Warning: No data rows found.")
        return False

    headers = set(rows[0].keys())
    missing = [col for col in required if col not in headers]

    if missing:
        print(f"Missing required columns: {', '.join(missing)}")
        return False

    print("All required columns present.")
    return True


def main():
    parser = argparse.ArgumentParser(description="Load and validate CSV risk data")
    parser.add_argument("--input", required=True, help="Path to CSV file")
    parser.add_argument("--require", nargs="*", default=[], help="Required column names")
    args = parser.parse_args()

    rows = load_csv(args.input)
    if args.require:
        validate_columns(rows, args.require)


if __name__ == "__main__":
    main()
