# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "get_all_resources"
REQUEST_METHOD = "get"
URL_SUFFIX = "resources/v1/"

from .test_case_01 import TestCase01GetAllResourcesAPITestCase

__all__ = [
    "TestCase01GetAllResourcesAPITestCase"
]
