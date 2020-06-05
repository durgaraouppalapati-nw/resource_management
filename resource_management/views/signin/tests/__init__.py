# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "signin"
REQUEST_METHOD = "post"
URL_SUFFIX = "signin/v1/"

from .test_case_01 import TestCase01SigninAPITestCase

__all__ = [
    "TestCase01SigninAPITestCase"
]
