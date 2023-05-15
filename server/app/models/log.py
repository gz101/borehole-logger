from django.db import models

from .borehole import Borehole


class Log(models.Model):
    """Model that defines a single log in a borehole."""
    borehole = models.ForeignKey(
        Borehole, related_name="logs", on_delete=models.CASCADE
    )
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    soil_type = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    sample_number = models.CharField(max_length=20)
    sample_type = models.CharField(max_length=20)
    spt_count = models.PositiveIntegerField(default=0)
