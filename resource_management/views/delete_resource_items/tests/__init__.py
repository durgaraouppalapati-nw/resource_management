# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "delete_resource_items"
REQUEST_METHOD = "post"
URL_SUFFIX = "resource/items/v1/"

from .test_case_01 import TestCase01DeleteResourceItemsAPITestCase

__all__ = [
    "TestCase01DeleteResourceItemsAPITestCase"
]
