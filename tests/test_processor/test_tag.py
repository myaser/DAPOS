# -*- coding: UTF-8 -*-
'''test functionality'''
import unittest
from DAPOS.processor.tag import tag
from DAPOS.processor.token import tokenize

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

    @unittest.skip("functionality not complete yet!")
    def test_cvs_file(self):
        for raw, expected in self.test_cases:
            sol = tag(raw)
            synt = iter(expected.split())
            for item in sol:
                if isinstance(item[0], tuple):
                    word = synt.next()
                    prefix = u""
                    suffix = u""
                    matched = False
                    for ((ex_prefix, ex_prefix_type),
                         ex_word,
                         (ex_suffix, ex_suffix_type)) in item:
                        if word == ex_prefix:
                            if not prefix:
                                prefix = word
                            word = synt.next()
                            if word == ex_word:
                                if ex_suffix:
                                    if not suffix:
                                        suffix = synt.next()
                                    if suffix == ex_suffix:
                                        matched = True
                                        break
                        if word == ex_word:
                            if ex_suffix:
                                if not suffix:
                                    suffix = synt.next()
                                if suffix == ex_suffix:
                                    matched = True
                                    break
                            else:
                                matched = True
                                break
                    if word[-1] in [u'ى', u'ة']:
                        for ((ex_prefix, ex_prefix_type),
                             ex_word,
                             (ex_suffix, ex_suffix_type)) in item:
                            if ex_suffix:
                                synt.next()
                                break
                        continue
                    if not matched:
                        print "Bad match: "
                        print item[0][1], "<=>", word
                        print 80 * "="
                else:
                    if synt.next() != item[0]:
                        print "Bad match: "
                        print synt.next(), "<=>", item[0]
                        print 80 * "="


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
