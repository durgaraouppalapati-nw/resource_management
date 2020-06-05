from django.db import models

from resource_management.models import User


class Resource(models.Model):
    name = models.CharField(max_length=100, unique=True)
    resource_pic = models.URLField(null=True)
    link = models.URLField()
    description = models.TextField()
