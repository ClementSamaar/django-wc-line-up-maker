from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    abbreviation = models.CharField(max_length=20, null=False, blank=False)
    type = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.abbreviation} ({self.type})"
