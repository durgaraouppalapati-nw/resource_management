# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "search_resource_items"
REQUEST_METHOD = "get"
URL_SUFFIX = "request/search/{resource_id}/resource_items/v1/"

from .test_case_01 import TestCase01SearchResourceItemsAPITestCase

__all__ = [
    "TestCase01SearchResourceItemsAPITestCase"
]
