# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_all_users"
REQUEST_METHOD = "get"
URL_SUFFIX = "users/v1/"

from .test_case_01 import TestCase01GetAllUsersAPITestCase

__all__ = [
    "TestCase01GetAllUsersAPITestCase"
]
