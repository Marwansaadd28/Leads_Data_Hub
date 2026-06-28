from django.db import models


class Lead(models.Model):

    class StatusChoices(models.TextChoices):
        NEW = "new", "New"
        CONTACTED = "contacted", "Contacted"
        QUALIFIED = "qualified", "Qualified"
        LOST = "lost", "Lost"

    lead_id = models.IntegerField(unique=True)

    name = models.CharField(max_length=255)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=20)

    source = models.CharField(max_length=100)

    created_at = models.DateTimeField()

    status = models.CharField(
        max_length=20,
        choices=StatusChoices.choices,
    )

    def __str__(self):
        return self.name