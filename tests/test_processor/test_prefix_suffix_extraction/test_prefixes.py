# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.token.segmentation.prefix import extract_prefixes
from DAPOS.data.affixes import prefixes


class PrefixTest(unittest.TestCase):
    def test_prefix(self):
        '''check if prefix method return the expected
           longest prefix in the expected form'''
        test_words = [u"أياضرب", u"أوياضرب", u"أفياضرب", u"سيضرب", u"وسيضرب",
                      u"فسيضرب", u"أسيضرب", u"أوسضرب", u"أفسيضرب",]
        expects = [[(u'', u'C1'), (u'أ', u'C2'), (u"أيا", u"N6")],
                   [(u'', u'C1'), (u'أ', u'C2'),
                    (u"أويا", u"N6"), (u"أو", u"C2"), ],
                   [(u'', u'C1'), (u'أ', u'C2'),
                    (u"أفيا", u"N6"), (u"أف", u"C2"), ],
                   [(u'', u'C1'), (u"س", u"V1"), ],
                   [(u'', u'C1'), (u"وس", u"V1"), (u"و", u"C1")],
                   [(u'', u'C1'), (u"فس", u"V1"), (u"ف", u"C1")],
                   [(u'', u'C1'), (u'أ', u'C2'), (u"أس", u"V1"), ],
                   [(u'', u'C1'), (u'أ', u'C2'),
                    (u"أوس", u"V1"), (u"أو", u"C2"), ],
                   [(u'', u'C1'), (u'أ', u'C2'),
                    (u"أفس", u"V1"), (u"أف", u"C2"),]]

        for word, expected in zip(test_words, expects):
            self.assertEqual(set(expected),
                             set(extract_prefixes(word, prefixes)))
