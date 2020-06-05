# pylint: disable=wrong-import-position

APP_NAME = "resource_management"
OPERATION_NAME = "update_user_details"
REQUEST_METHOD = "put"
URL_SUFFIX = "user/update_profile/v1/"

from .test_case_01 import TestCase01UpdateUserDetailsAPITestCase

__all__ = [
    "TestCase01UpdateUserDetailsAPITestCase"
]
