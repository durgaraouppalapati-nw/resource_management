# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_resource_items"
REQUEST_METHOD = "get"
URL_SUFFIX = "resource/{resource_id}/items/v1/"

from .test_case_01 import TestCase01GetResourceItemsAPITestCase

__all__ = [
    "TestCase01GetResourceItemsAPITestCase"
]
