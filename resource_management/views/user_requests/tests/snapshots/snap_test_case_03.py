# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase03UserRequestsAPITestCase::test_case status'] = 200

snapshots['TestCase03UserRequestsAPITestCase::test_case body'] = {
    'requests_details': [
        {
            'access_level': 'READ',
            'item_title': 'ResourceItem 1',
            'request_id': 2,
            'resource_name': 'Resource 0',
            'status': 'ACCEPTED'
        },
        {
            'access_level': 'READ',
            'item_title': 'ResourceItem 0',
            'request_id': 1,
            'resource_name': 'Resource 0',
            'status': 'PENDING'
        },
        {
            'access_level': 'READ',
            'item_title': 'ResourceItem 2',
            'request_id': 3,
            'resource_name': 'Resource 0',
            'status': 'REJECTED'
        }
    ],
    'total_requests': 3
}

snapshots['TestCase03UserRequestsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '426',
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
