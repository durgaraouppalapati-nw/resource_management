# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['test_my_func gpg_response'] = 3

snapshots['test_add_two_positive_numbers jpg_response'] = 3

snapshots['test_add_two_negative_numbers jpg_response'] = -3

snapshots['test_add_two_float_numbers jpg_response'] = 3.0
