# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "accept_or_reject_requests"
REQUEST_METHOD = "post"
URL_SUFFIX = "requests/action/v1/"

from .test_case_01 import TestCase01AcceptOrRejectRequestsAPITestCase

__all__ = [
    "TestCase01AcceptOrRejectRequestsAPITestCase"
]
