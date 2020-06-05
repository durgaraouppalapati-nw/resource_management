# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_requests"
REQUEST_METHOD = "post"
URL_SUFFIX = "requests/v1/"

from .test_case_01 import TestCase01GetRequestsAPITestCase

__all__ = [
    "TestCase01GetRequestsAPITestCase"
]
