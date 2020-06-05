# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_users_for_item"
REQUEST_METHOD = "get"
URL_SUFFIX = "item/{item_id}/users/v1/"

from .test_case_01 import TestCase01GetUsersForItemAPITestCase

__all__ = [
    "TestCase01GetUsersForItemAPITestCase"
]
