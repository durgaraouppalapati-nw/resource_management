from resource_management.models.user import User
from resource_management.models.resource import Resource
from resource_management.models.item import ResourceItem, AccessLevel
from resource_management.models.request import Request


__all__ = [
    "User",
    "Resource",
    "ResourceItem",
    "AccessLevel",
    "Request"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
