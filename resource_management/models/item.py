from django.db import models

from resource_management.models import Resource, User


class ResourceItem(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField()
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    users = models.ManyToManyField(User, through='AccessLevel')


class AccessLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource_item = models.ForeignKey(ResourceItem, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=10)
    
    class Meta:
        unique_together = [['user', 'resource_item']]
