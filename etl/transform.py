from datetime import datetime


def transform_row(row):
    """
    Clean and normalize a single row.
    """

    transformed = row.copy()

    transformed["lead_id"] = int(transformed["lead_id"])

    transformed["name"] = transformed["name"].strip()

    transformed["email"] = transformed["email"].strip().lower()

    transformed["phone"] = transformed["phone"].strip()

    transformed["source"] = transformed["source"].strip().lower()

    transformed["status"] = transformed["status"].strip().lower()

    transformed["created_at"] = datetime.fromisoformat(
        transformed["created_at"]
    )

    return transformed


def transform(rows):
    """
    Transform all valid rows.
    """

    transformed_rows = []

    for row in rows:
        transformed_rows.append(
            transform_row(row)
        )

    return transformed_rows