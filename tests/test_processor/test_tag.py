# -*- coding: UTF-8 -*-
'''test functionality'''
import unittest
from DAPOS.processor.tag import tag

import os.path
import csv


class FunctionTest(unittest.TestCase):
    '''
        the whole operation against example CSV file
    '''
    CSVFile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           'raw2tokenized_utf8.csv')
    def setUp(self):
        '''read examples in csv file
        '''
        self.csv_file = open(self.CSVFile, 'rb')
        self.test_cases = csv.reader(self.csv_file)

    def tearDown(self):
        self.csv_file.close()

    def test_damn(self):
        for raw, expected in self.test_cases:
            sol = tag(raw)
            synt = iter(expected)
            for item in sol:
                if isinstance(item[0], tuple):
                    word = synt.next()
                    prefix = u""
                    suffix = u""
                    matched = False
                    for case in item:
                        if word == case[0][1]:
                            if not prefix:
                                prefix = word
                            word = synt.next()
                            if word == case[1]:
                                if case[2][1]:
                                    if not suffix:
                                        suffix = synt.next()
                                    if suffix == case[2][1]:
                                        matched = True
                                        break
                        if word == case[1]:
                            if case[2][1]:
                                if not suffix:
                                    suffix = synt.next()
                                if suffix == case[2][1]:
                                    matched = True
                                    break
                    self.assertTrue(matched)
                else:
                    self.assertEqual(unicode(synt.next()), synt.next())


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
