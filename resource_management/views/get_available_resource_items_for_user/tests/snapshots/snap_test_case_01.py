# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAvailableResourceItemsForUserAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAvailableResourceItemsForUserAPITestCase::test_case body'] = {
    'resource_items': [
        {
            'access_level': 'READ',
            'item_id': 1,
            'item_title': 'ResourceItem 0',
            'link': 'www.resource_item0.com',
            'resource_name': 'Resource 0'
        },
        {
            'access_level': 'READ',
            'item_id': 2,
            'item_title': 'ResourceItem 1',
            'link': 'www.resource_item1.com',
            'resource_name': 'Resource 0'
        },
        {
            'access_level': 'READ',
            'item_id': 3,
            'item_title': 'ResourceItem 2',
            'link': 'www.resource_item2.com',
            'resource_name': 'Resource 0'
        }
    ],
    'total_resource_items': 3
}

snapshots['TestCase01GetAvailableResourceItemsForUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '458',
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
