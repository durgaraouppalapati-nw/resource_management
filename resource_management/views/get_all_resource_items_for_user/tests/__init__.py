# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_all_resource_items_for_user"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/{user_id}/items/v1/"

from .test_case_01 import TestCase01GetAllResourceItemsForUserAPITestCase

__all__ = [
    "TestCase01GetAllResourceItemsForUserAPITestCase"
]
