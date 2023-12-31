# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01AcceptOrRejectRequestsAPITestCase::test_case status'] = 200

snapshots['TestCase01AcceptOrRejectRequestsAPITestCase::test_case body'] = b''

snapshots['TestCase01AcceptOrRejectRequestsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '0',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin',
        'Vary'
    ],
    'x-frame-options': [
        'DENY',
        'X-Frame-Options'
    ]
}

snapshots['TestCase01AcceptOrRejectRequestsAPITestCase::test_case request_status'] = 'ACCEPTED'

snapshots['TestCase01AcceptOrRejectRequestsAPITestCase::test_case resource_item_access_exists'] = True

snapshots['TestCase01AcceptOrRejectRequestsAPITestCase::test_case access_level'] = 'READ'
