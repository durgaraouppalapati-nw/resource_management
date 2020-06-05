# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "user_requests"
REQUEST_METHOD = "post"
URL_SUFFIX = "user/requests/v1/"

from .test_case_01 import TestCase01UserRequestsAPITestCase

__all__ = [
    "TestCase01UserRequestsAPITestCase"
]
