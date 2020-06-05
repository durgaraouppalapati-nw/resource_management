# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "search_resource"
REQUEST_METHOD = "get"
URL_SUFFIX = "request/search/resource/v1/"

from .test_case_01 import TestCase01SearchResourceAPITestCase

__all__ = [
    "TestCase01SearchResourceAPITestCase"
]
