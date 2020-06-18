# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAvailableResourceItemsForUserAPITestCase::test_case status'] = 200

snapshots['TestCase01GetAvailableResourceItemsForUserAPITestCase::test_case body'] = {
    'resource_items': [
    ],
    'total_resource_items': 0
}

snapshots['TestCase01GetAvailableResourceItemsForUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '49',
        'Content-Length'
    ],
    'content-type': [
        'Content-Type',
        'text/html; charset=utf-8'
    ],
    'vary': [
        'Accept-Language, Origin, Cookie',
        'Vary'
    ],
    'x-frame-options': [
        'SAMEORIGIN',
        'X-Frame-Options'
    ]
}
