# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.stemmer.prefix import extract_prefixes
from DAPOS.data.affixes import prefixes


class PrefixTest(unittest.TestCase):
    def test_prefix(self):
        '''check if prefix method return the expected
           longest prefix in the expected form'''
        test_words = [u"أياضرب", u"أوياضرب", u"أفياضرب", u"سيضرب", u"وسيضرب",
                      u"فسيضرب", u"أسيضرب", u"أوسضرب", u"أفسيضرب",]
        expects = [[(u'', u'pC1'), (u'أ', u'pC4'), (u"أيا", u"pN43")],
                   [(u'', u'pC1'), (u'أ', u'pC4'),
                    (u"أويا", u"pN44"), (u"أو", u"pC5"), ],
                   [(u'', u'pC1'), (u'أ', u'pC4'),
                    (u"أفيا", u"pN45"), (u"أف", u"pC6"), ],
                   [(u'', u'pC1'),],
                   [(u'', u'pC1'),(u"و", u"pC2")],
                   [(u'', u'pC1'), (u"ف", u"pC3")],
                   [(u'', u'pC1'), (u'أ', u'pC4'),],
                   [(u'', u'pC1'), (u'أ', u'pC4'), (u"أو", u"pC5"), ],
                   [(u'', u'pC1'), (u'أ', u'pC4'), (u"أف", u"pC6"),]]

        for word, expected in zip(test_words, expects):
            self.assertEqual(set(expected),
                             set(extract_prefixes(word, prefixes)))