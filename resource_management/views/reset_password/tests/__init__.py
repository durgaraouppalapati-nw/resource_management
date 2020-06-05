# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "reset_password"
REQUEST_METHOD = "post"
URL_SUFFIX = "password/reset/v1/"

from .test_case_01 import TestCase01ResetPasswordAPITestCase

__all__ = [
    "TestCase01ResetPasswordAPITestCase"
]
