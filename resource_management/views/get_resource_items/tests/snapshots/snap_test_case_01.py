# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetResourceItemsAPITestCase::test_case status'] = 200

snapshots['TestCase01GetResourceItemsAPITestCase::test_case body'] = {
    'items': [
        {
            'description': 'This is about ResourceItem 0',
            'item_id': 1,
            'link': 'www.resource_item0.com',
            'title': 'ResourceItem 0'
        },
        {
            'description': 'This is about ResourceItem 1',
            'item_id': 2,
            'link': 'www.resource_item1.com',
            'title': 'ResourceItem 1'
        },
        {
            'description': 'This is about ResourceItem 2',
            'item_id': 3,
            'link': 'www.resource_item2.com',
            'title': 'ResourceItem 2'
        },
        {
            'description': 'This is about ResourceItem 3',
            'item_id': 4,
            'link': 'www.resource_item3.com',
            'title': 'ResourceItem 3'
        }
    ],
    'resource': {
        'description': 'This is about Resource 0',
        'link': 'www.resource0.com',
        'name': 'Resource 0',
        'resource_id': 1,
        'resource_pic': 'www.resource0.pnj'
    },
    'total_items': 4
}

snapshots['TestCase01GetResourceItemsAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '688',
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
