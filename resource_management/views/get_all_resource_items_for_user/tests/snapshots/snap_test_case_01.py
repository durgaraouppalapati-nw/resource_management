# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01GetAllResourceItemsForUserAPITestCase::test_case status'] = 404

snapshots['TestCase01GetAllResourceItemsForUserAPITestCase::test_case body'] = {
    'http_status_code': 404,
    'res_status': 'INVALID_USER_ID',
    'response': 'Invalid User Id'
}

snapshots['TestCase01GetAllResourceItemsForUserAPITestCase::test_case header_params'] = {
    'content-language': [
        'Content-Language',
        'en'
    ],
    'content-length': [
        '89',
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