# -*- coding: UTF-8 -*-

import unittest
from DAPOS.tag import tag

class TestTag(unittest.TestCase):
    def test_tag(self):
        processed = tag(u'1- بسمك اللهم، :)')
        self.assertEqual([
            [u'1', u'CD'],
            [u'-', u'PUNC'],
            [
                ((u'', u'C1'), u'بسمك', (u'', u'C1')),
                ((u'', u'C1'), u'بسم', (u'ك', u'C2')),
                ((u'ب', u'N4'), u'سمك', (u'', u'C1')),
                ((u'ب', u'N4'), u'سم', (u'ك', u'C2')),
             ],
            [
                ((u'', u'C1'), u'اللهم', (u'', u'C1')),
                ((u'', u'C1'), u'الل', (u'هم', u'C3')),
            ],
            [u'،', u'PUNC'],
            [u':)', u'EMO'],
        ], processed)
