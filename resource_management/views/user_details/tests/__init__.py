# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "user_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/details/v1/"

from .test_case_01 import TestCase01UserDetailsAPITestCase

__all__ = [
    "TestCase01UserDetailsAPITestCase"
]
