# analytics/models.py

from django.db import models


class Visit(models.Model):
    page = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
