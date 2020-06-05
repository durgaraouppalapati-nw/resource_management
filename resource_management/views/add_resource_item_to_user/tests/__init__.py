# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "add_resource_item_to_user"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/{user_id}/add_item/v1/"

from .test_case_01 import TestCase01AddResourceItemToUserAPITestCase

__all__ = [
    "TestCase01AddResourceItemToUserAPITestCase"
]
