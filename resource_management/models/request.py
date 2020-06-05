from django.db import models

from resource_management.constants.enums import Confirmation
from resource_management.models import User, ResourceItem, Resource


class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    resource_item = models.ForeignKey(ResourceItem, on_delete=models.CASCADE)
    access_level = models.CharField(max_length=10)
    due_datetime = models.DateTimeField()
    reason_for_access = models.TextField()
    
    Confirmation_Choice = Confirmation.get_list_of_tuples()
    
    request_status = models.CharField(max_length=10,
                                      choices=Confirmation_Choice,
                                      default='PENDING'
                                      )
    reason_for_rejection = models.TextField(null=True, blank=True)
