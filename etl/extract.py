import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_PATH = BASE_DIR / "data" / "raw"


def extract():
    """
    Read all CSV files from the raw folder.
    Returns a list of dictionaries.
    """

    rows = []

    csv_files = RAW_DATA_PATH.glob("*.csv")

    for csv_file in csv_files:
        print(f"Reading: {csv_file.name}")

        with open(csv_file, newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                rows.append(row)

    return rows