"""
# TODO: Update test case description
"""

from freezegun import freeze_time

from resource_management.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

REQUEST_BODY = """
{
    "filterby": "RESOURCE",
    "value": "Resource 0"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"offset": 0, "limit": 10, "sortby": "NAME"},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase02GetRequestsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        self.set_up_user(username, password)
        self.set_foo_user_as_admin(self.foo_user)
        self.create_requests(size=3)

    @freeze_time('2020-06-30 00:00:00')
    def test_case(self):
        self.default_test_case()
