from django.db import models

from .project import Project


class Borehole(models.Model):
    """Model that defines a single borehole in a project."""
    project = models.ForeignKey(
        Project, related_name="boreholes", on_delete=models.CASCADE
    )
    borehole_number = models.CharField(max_length=20)
    conducted_by = models.CharField(max_length=100)
    date_logged = models.DateTimeField()
    groundwater_depth = models.DecimalField(max_digits=5, decimal_places=2)
    elevation = models.DecimalField(max_digits=2, decimal_places=2)
    drill_rig = models.CharField(max_length=20)
    diameter = models.DecimalField(max_digits=2, decimal_places=2)
    total_boring_depth = models.DecimalField(max_digits=2, decimal_places=2)
    surface_description = models.TextField(max_length=500)
