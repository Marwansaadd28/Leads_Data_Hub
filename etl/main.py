from extract import extract
from validate import validate_row


def main():

    rows = extract()

    valid_rows = []
    invalid_rows = []

    for row in rows:

        is_valid, errors = validate_row(row)

        if is_valid:
            valid_rows.append(row)
        else:
            invalid_rows.append(
                {
                    "row": row,
                    "errors": errors,
                }
            )

    print("=" * 40)
    print(f"Total Rows     : {len(rows)}")
    print(f"Valid Rows     : {len(valid_rows)}")
    print(f"Invalid Rows   : {len(invalid_rows)}")
    print("=" * 40)


if __name__ == "__main__":
    main()