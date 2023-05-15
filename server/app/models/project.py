from django.db import models


class Project(models.Model):
    """Model that defines a project."""
    project_number = models.CharField(max_length=20)
    client_name = models.CharField(max_length=255)
    project_name = models.CharField(max_length=255)
    site_address = models.CharField(max_length=255)
