# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAllUsersAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAllUsersAPITestCase::test_case body'] = {
    'total_users': 5,
    'users_details': [
        {
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 0',
            'profile_pic': None,
            'user_id': 2
        },
        {
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 1',
            'profile_pic': None,
            'user_id': 3
        },
        {
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 2',
            'profile_pic': None,
            'user_id': 4
        },
        {
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 3',
            'profile_pic': None,
            'user_id': 5
        },
        {
            'department': 'Backend',
            'job_role': 'Developer',
            'name': 'User 4',
            'profile_pic': None,
            'user_id': 6
        }
    ]
}

snapshots['TestCase01GetAllUsersAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '562',
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
