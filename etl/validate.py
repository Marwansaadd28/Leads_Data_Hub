import re
from datetime import datetime
from typing import Dict, List, Tuple

REQUIRED_FIELDS = [
    "lead_id",
    "name",
    "email",
    "phone",
    "source",
    "created_at",
    "status",
]

VALID_STATUSES = {
    "new",
    "contacted",
    "qualified",
    "lost",
}

EMAIL_REGEX = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"


def validate_email(email: str) -> bool:
    return re.match(EMAIL_REGEX, email.strip()) is not None


def validate_date(date_string: str) -> bool:
    """
    Try multiple supported date formats.
    """

    formats = [
        "%Y-%m-%d",
        "%Y-%m-%d %H:%M:%S",
        "%d/%m/%Y",
        "%d/%m/%Y %H:%M:%S",
    ]

    for fmt in formats:
        try:
            datetime.strptime(date_string.strip(), fmt)
            return True
        except ValueError:
            continue

    return False


def validate_row(row: Dict) -> Tuple[bool, List[str]]:

    errors = []

    # Required fields
    for field in REQUIRED_FIELDS:
        value = row.get(field)

        if value is None or str(value).strip() == "":
            errors.append(f"{field} is required")

    if errors:
        return False, errors

    # Status validation
    status = row["status"].strip().lower()

    if status not in VALID_STATUSES:
        errors.append(f"Unsupported status '{row['status']}'")

    # Email validation
    if not validate_email(row["email"]):
        errors.append("Invalid email address")

    # Date validation
    if not validate_date(row["created_at"]):
        errors.append("Invalid date")

    return len(errors) == 0, errors


def validate(rows):

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

    return valid_rows, invalid_rows