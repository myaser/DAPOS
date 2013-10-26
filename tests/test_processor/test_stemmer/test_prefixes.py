# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.stemmer.prefix import extract_prefixes


class PrefixTest(unittest.TestCase):
    def prefixes(self, word):
        return set([prefix.string for prefix in extract_prefixes(word)])

    def test_prefix(self):
        '''check if prefix method return the expected
           longest prefix in the expected form'''
        prefixes = self.prefixes(u"أياضرب")
        expected = set([u'', u'أ', u"أيا"])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"أوياضرب")
        expected = set([u'', u'أ', u"أويا", u"أو"])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"أفياضرب")
        expected = set([u'', u'أ', u"أفيا", u"أف"])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"سيضرب")
        expected = set([u''])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"وسيضرب")
        expected = set([u'', u"و"])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"فسيضرب")
        expected = set([u'', u"ف"])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"أسيضرب")
        expected = set([u'', u'أ'])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"أوسضرب")
        expected = set([u'', u'أ', u"أو"])
        self.assertEqual(prefixes, expected)
        prefixes = self.prefixes(u"أفسيضرب")
        expected = set([u'', u'أ', u"أف"])
        self.assertEqual(prefixes, expected)
