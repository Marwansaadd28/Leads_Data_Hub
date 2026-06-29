import os
import sys
from pathlib import Path

# ----------------------------------------
# Configure Django
# ----------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
BACKEND_DIR = BASE_DIR / "backend"

sys.path.insert(0, str(BACKEND_DIR))

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "config.settings"
)

import django

django.setup()

# ----------------------------------------
# Import Models
# ----------------------------------------

from leads.models import Lead, Source, Status


def load(rows):
    """
    Load transformed rows into the database.
    """

    created = 0
    skipped = 0

    for row in rows:

        # Get or create Source
        source, _ = Source.objects.get_or_create(
            name=row["source"]
        )

        # Get or create Status
        status, _ = Status.objects.get_or_create(
            name=row["status"]
        )

        # Create Lead
        _, is_created = Lead.objects.get_or_create(
            lead_id=row["lead_id"],
            defaults={
                "name": row["name"],
                "email": row["email"],
                "phone": row["phone"],
                "created_at": row["created_at"],
                "source": source,
                "status": status,
            },
        )

        if is_created:
            created += 1
        else:
            skipped += 1

    return created, skipped