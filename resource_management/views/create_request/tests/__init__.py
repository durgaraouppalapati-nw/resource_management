# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "create_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/add/request/v1/"

from .test_case_01 import TestCase01CreateRequestAPITestCase

__all__ = [
    "TestCase01CreateRequestAPITestCase"
]
