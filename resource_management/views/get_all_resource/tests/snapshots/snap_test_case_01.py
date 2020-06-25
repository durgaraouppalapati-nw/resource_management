# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAllResourceAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAllResourceAPITestCase::test_case body'] = {
    'resources_details': [
        {
            'description': 'This is about Resource 0',
            'link': 'www.resource0.com',
            'name': 'Resource 0',
            'resource_id': 1,
            'resource_pic': 'www.resource0.pnj'
        },
        {
            'description': 'This is about Resource 1',
            'link': 'www.resource1.com',
            'name': 'Resource 1',
            'resource_id': 2,
            'resource_pic': 'www.resource1.pnj'
        },
        {
            'description': 'This is about Resource 2',
            'link': 'www.resource2.com',
            'name': 'Resource 2',
            'resource_id': 3,
            'resource_pic': 'www.resource2.pnj'
        },
        {
            'description': 'This is about Resource 3',
            'link': 'www.resource3.com',
            'name': 'Resource 3',
            'resource_id': 4,
            'resource_pic': 'www.resource3.pnj'
        }
    ],
    'total_resources': 4
}

snapshots['TestCase01GetAllResourceAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '649',
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
