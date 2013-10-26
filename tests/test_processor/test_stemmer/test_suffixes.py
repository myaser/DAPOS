# -*- coding: UTF:8 -*-

import unittest
from DAPOS.processor.stemmer.suffix import extract_suffixes


class TestSuffix(unittest.TestCase):
    def suffixes(self, word):
        return set([suffix.string for suffix in extract_suffixes(word)])

    def test_suffix(self):
        '''check if suffix method return the expected
           longest prefix in the expected form'''
        suffixes = self.suffixes(u"كتابك")
        expected = set([u'', u"ك"])
        self.assertEqual(suffixes, expected)

        suffixes = self.suffixes(u"كتابكي")
        expected = set([u'', u"كي", u"ي"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"كتابكما")
        expected = set([u'', u"كما"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"عضمكوا")
        expected = set([u'', u"كوا",])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"يضربني")
        expected = set([u'', u"ني", u"ي"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"مضربش")
        expected = set([u'', u"ش"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"مضربنيش")
        expected = set([u'', u"نيش", u"ش"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"ضربهولنا")
        expected = set([u'', u"هولنا", u"نا"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"ضربهولهم")
        expected = set([u'', u"هولهم", u"هم"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"ضربهالي")
        expected = set([u'', u"هالي", u"ي"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"ضربهاله")
        expected = set([u'', u"هاله", u"ه"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"ضربلنيش")
        expected = set([u'', u"لنيش", u"ش", u"نيش"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"ماضربهاليش")
        expected = set([u'', u"هاليش", u"ليش", u"ش"])
        self.assertEqual(suffixes, expected)


        suffixes = self.suffixes(u"مضربهالناش")
        expected = set([u'', u"ناش", u"ش", u"لناش", u"هالناش"])
        self.assertEqual(suffixes, expected)
