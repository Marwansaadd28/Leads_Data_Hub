import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

ERRORS_PATH = BASE_DIR / "data" / "errors"


def save_invalid_rows(invalid_rows):

    if not invalid_rows:
        return

    output_file = ERRORS_PATH / "invalid_rows.csv"

    with open(output_file, "w", newline="", encoding="utf-8") as file:

        fieldnames = [
            "lead_id",
            "name",
            "email",
            "phone",
            "source",
            "created_at",
            "status",
            "errors",
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for item in invalid_rows:

            row = item["row"].copy()

            row["errors"] = ", ".join(item["errors"])

            writer.writerow(row)

    print(f"\nInvalid rows saved to:\n{output_file}")