# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAllResourceItemsForUserAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAllResourceItemsForUserAPITestCase::test_case body'] = {
    'resource_items': [
        {
            'access_level': 'READ',
            'description': 'This is about ResourceItem 0',
            'item_id': 1,
            'item_title': 'ResourceItem 0',
            'link': 'www.resource_item0.com',
            'resource_name': 'Resource 0'
        },
        {
            'access_level': 'READ',
            'description': 'This is about ResourceItem 1',
            'item_id': 2,
            'item_title': 'ResourceItem 1',
            'link': 'www.resource_item1.com',
            'resource_name': 'Resource 0'
        },
        {
            'access_level': 'READ',
            'description': 'This is about ResourceItem 2',
            'item_id': 3,
            'item_title': 'ResourceItem 2',
            'link': 'www.resource_item2.com',
            'resource_name': 'Resource 0'
        }
    ],
    'total_items': 3,
    'user_details': {
        'department': 'Backend',
        'job_role': 'Developer',
        'name': 'User 0',
        'profile_pic': None,
        'user_id': 2
    }
}

snapshots['TestCase01GetAllResourceItemsForUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '711',
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
