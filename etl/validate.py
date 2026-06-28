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


def validate_row(row: Dict) -> Tuple[bool, List[str]]:
    """
    Validate a single CSV row.

    Returns:
        (is_valid, errors)

    Example:
        True, []

        False, [
            "email is required",
            "Invalid status"
        ]
    """

    errors = []

    # Required fields validation
    for field in REQUIRED_FIELDS:
        value = row.get(field)

        if value is None or str(value).strip() == "":
            errors.append(f"{field} is required")

    # Stop if required fields are missing
    if errors:
        return False, errors

    # Status validation
    status = row["status"].strip().lower()

    if status not in VALID_STATUSES:
        errors.append(
            f"Unsupported status '{row['status']}'"
        )

    return len(errors) == 0, errors