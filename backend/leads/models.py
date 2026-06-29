from django.db import models


class Source(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.name


class Lead(models.Model):

    lead_id = models.IntegerField(
        unique=True
    )

    name = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=30
    )

    created_at = models.DateTimeField()

    source = models.ForeignKey(
        Source,
        on_delete=models.PROTECT,
        related_name="leads"
    )

    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name="leads"
    )

    def __str__(self):
        return self.name