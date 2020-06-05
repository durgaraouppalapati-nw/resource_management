# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "update_resorce_item"
REQUEST_METHOD = "put"
URL_SUFFIX = "item/{item_id}/v1/"

from .test_case_01 import TestCase01UpdateResorceItemAPITestCase

__all__ = [
    "TestCase01UpdateResorceItemAPITestCase"
]
