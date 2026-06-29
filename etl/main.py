from etl.extract import extract
from etl.validate import validate
from etl.transform import transform
from etl.load import load
from etl.logger import save_invalid_rows


def main():

    # Step 1 - Extract
    rows = extract()

    # Step 2 - Validate
    valid_rows, invalid_rows = validate(rows)

    # Step 3 - Transform
    transformed_rows = transform(valid_rows)

    # Step 4 - Load
    created, skipped = load(transformed_rows)

    # Step 5 - Save invalid rows
    save_invalid_rows(invalid_rows)

    print("\n" + "=" * 60)
    print("ETL SUMMARY")
    print("=" * 60)

    print(f"Extracted Rows      : {len(rows)}")
    print(f"Valid Rows          : {len(valid_rows)}")
    print(f"Invalid Rows        : {len(invalid_rows)}")
    print(f"Transformed Rows    : {len(transformed_rows)}")
    print(f"Created Records     : {created}")
    print(f"Skipped Records     : {skipped}")

    print("=" * 60)


if __name__ == "__main__":
    main()