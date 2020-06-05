# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "delete_request"
REQUEST_METHOD = "delete"
URL_SUFFIX = "user/request/{request_id}/v1/"

from .test_case_01 import TestCase01DeleteRequestAPITestCase

__all__ = [
    "TestCase01DeleteRequestAPITestCase"
]
