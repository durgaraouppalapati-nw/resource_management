# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_available_resource_items_for_user"
REQUEST_METHOD = "get"
URL_SUFFIX = "resource_items/v1/"

from .test_case_01 import TestCase01GetAvailableResourceItemsForUserAPITestCase

__all__ = [
    "TestCase01GetAvailableResourceItemsForUserAPITestCase"
]
