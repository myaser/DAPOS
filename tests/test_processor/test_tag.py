# -*- coding: UTF-8 -*-
'''test functionality'''
import unittest
from DAPOS.processor.tag import tag

import os.path
import csv
import codecs


class UTF8Recoder(object):
    def __init__(self, f, encoding):
        self.reader = codecs.getreader(encoding)(f)
    def __iter__(self):
        return self
    def next(self):
        return self.reader.next().encode("utf-8")

class UnicodeReader(object):
    def __init__(self, f, dialect=csv.excel, encoding="utf-8-sig", **kwds):
        f = UTF8Recoder(f, encoding)
        self.reader = csv.reader(f, dialect=dialect, **kwds)
    def next(self):
        row = self.reader.next()
        return [unicode(s, "utf-8") for s in row]
    def __iter__(self):
        return self


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
        self.test_cases = UnicodeReader(self.csv_file)

    def tearDown(self):
        self.csv_file.close()

    def test_cvs_file(self):
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
                    self.assertEqual(synt.next(), synt.next())


class TestTag(unittest.TestCase):
    def test_tag(self):
        processed = tag(u'1- بسمك اللهم، :)')
        self.assertEqual([
            [u'1', u'CD'],
            [u'-', u'PUNC'],
            [
                ((u'', u'pC1'), u'بسمك', (u'', u'sC1')),
                ((u'', u'pC1'), u'بسم', (u'ك', u'sC4')),
                ((u'ب', u'pN25'), u'سمك', (u'', u'sC1')),
                ((u'ب', u'pN25'), u'سم', (u'ك', u'sC4')),
             ],
            [
                ((u'', u'pC1'), u'اللهم', (u'', u'sC1')),
                ((u'', u'pC1'), u'الل', (u'هم', u'sC13')),
                ((u'ال', u'pN1'), u'لهم', (u'', u'sC1')),
            ],
            [u'،', u'PUNC'],
            [u':)', u'EMO'],
        ], processed)
