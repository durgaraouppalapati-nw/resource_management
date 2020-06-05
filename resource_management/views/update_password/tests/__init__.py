# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "update_password"
REQUEST_METHOD = "put"
URL_SUFFIX = "password/v1/"

from .test_case_01 import TestCase01UpdatePasswordAPITestCase

__all__ = [
    "TestCase01UpdatePasswordAPITestCase"
]
