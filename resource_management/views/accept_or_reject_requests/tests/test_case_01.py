"""
# TODO: Update test case description
"""

from resource_management.utils.custom_test_utils import CustomTestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

from resource_management.models import Request, AccessLevel

REQUEST_BODY = """
{
    "action": "ACCEPTED",
    "request_ids": [
        1
    ],
    "reason_for_rejection": ""
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {"oauth": {"tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read"], "type": "oauth2"}},
        "body": REQUEST_BODY,
    },
}


class TestCase01AcceptOrRejectRequestsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        self.set_up_user(username, password)
        self.set_foo_user_as_admin(self.foo_user)
        self.create_requests(size=3)

    def test_case(self):
        self.default_test_case()

        request_id = 1
        user_id = 2
        request = Request.objects.get(id=request_id)
        self.assert_match_snapshot(
            name='request_status',
            value=request.request_status
        )
        item_access = AccessLevel.objects.filter(
            user_id=user_id, resource_item=request.resource_item
        )
        self.assert_match_snapshot(
            name='resource_item_access_exists',
            value=item_access.exists()
        )
        self.assert_match_snapshot(
            name='access_level',
            value=item_access[0].access_level
        )
