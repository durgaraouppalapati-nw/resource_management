from django.contrib.auth.models import AbstractUser
from django.db import models

from resource_management.constants.enums import Gender

Gender_Choice = Gender.get_list_of_tuples()

class User(AbstractUser):
    name = models.CharField(max_length=100, null=True)
    profile_pic = models.URLField(null=True)
    job_role = models.CharField(max_length=50, null=True)
    department = models.CharField(max_length=100, null=True)
    gender = models.CharField(
                              choices=Gender_Choice,
                              max_length = 10,
                              null=True
                             )
    is_admin = models.BooleanField(default=False)
