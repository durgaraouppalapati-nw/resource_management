# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase02GetRequestsAPITestCase::test_case status'] = 200

snapshots['TestCase02GetRequestsAPITestCase::test_case body'] = {
    'requests_details': [
        {
            'access_level': 'READ',
            'due_datetime': '02/07/2020 12:00 AM',
            'item_title': 'ResourceItem 0',
            'profile_pic': None,
            'request_id': 1,
            'resource_name': 'Resource 0',
            'user_name': 'User 0'
        },
        {
            'access_level': 'READ',
            'due_datetime': '02/07/2020 12:00 AM',
            'item_title': 'ResourceItem 1',
            'profile_pic': None,
            'request_id': 2,
            'resource_name': 'Resource 0',
            'user_name': 'User 1'
        },
        {
            'access_level': 'READ',
            'due_datetime': '02/07/2020 12:00 AM',
            'item_title': 'ResourceItem 2',
            'profile_pic': None,
            'request_id': 3,
            'resource_name': 'Resource 0',
            'user_name': 'User 2'
        }
    ],
    'total_requests': 3
}

snapshots['TestCase02GetRequestsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '610',
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
