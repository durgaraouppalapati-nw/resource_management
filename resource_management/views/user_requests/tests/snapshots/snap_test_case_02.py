# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02UserRequestsAPITestCase::test_case status'] = 200

snapshots['TestCase02UserRequestsAPITestCase::test_case body'] = {
    'requests_details': [
        {
            'access_level': 'READ',
            'item_title': 'ResourceItem 1',
            'request_id': 2,
            'resource_name': 'Resource 0',
            'status': 'ACCEPTED'
        }
    ],
    'total_requests': 1
}

snapshots['TestCase02UserRequestsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '171',
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
