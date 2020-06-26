# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetUsersForItemAPITestCase::test_case status'] = 200

snapshots['TestCase01GetUsersForItemAPITestCase::test_case body'] = {
    'total_users': 3,
    'users': [
        {
            'access_level': 'READ',
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 1'
        },
        {
            'access_level': 'READ',
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 2'
        },
        {
            'access_level': 'READ',
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 3'
        }
    ]
}

snapshots['TestCase01GetUsersForItemAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '311',
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
