# -*- coding: UTF:8 -*-

import unittest
from DAPOS.processor.stemmer.suffix import extract_suffixes
from DAPOS.data.affixes import suffixes


class TestSuffix(unittest.TestCase):
    def test_suffix(self):
        '''check if suffix method return the expected
           longest prefix in the expected form'''
        test_words = [u"كتابك", u"كتابكي", u"كتابكما", u"عضمكوا", u"يضربني",
                      u"مضربش", u"مضربنيش", u"ضربهولنا", u"ضربهولهم",
                      u"ضربهالي", u"ضربهاله", u"ضربلنيش", u"ماضربهاليش",
                      u"مضربهلناش",]
        expects = [[(u'', u'sC1'), (u"ك", "sC4")],
                   [(u'', u'sC1'), (u"كي", "sV3"), (u"ي", "sC2")],
                   [(u'', u'sC1'), (u"كما","sC5")], 
                   [(u'', u'sC1'), (u"كوا","sC8"),],
                   [(u'', u'sC1'), (u"ني", "sV2"), (u"ي", "sC2")],
                   [(u'', u'sC1'), (u"ش", "sV1")],
                   [(u'', u'sC1'), (u"نيش", "sV4"), (u"ش", "sV1")],
                   [(u'', u'sC1'), (u"هولنا", "sV15"), (u"نا", "sC3"),],
                   [(u'', u'sC1'), (u"هولهم", "sV22"), (u"هم", u"sC13"),],
                   [(u'', u'sC1'), (u"هالي", "sV23"), (u"ي", "sC2"),],
                   [(u'', u'sC1'), (u"هاله", "sV30"), (u"ه", u"sC10"),],
                   [(u'', u'sC1'), (u"لنيش", "sV43"),
                    (u"ش", "sV1"), (u"نيش", "sV4")],
                   [(u'', u'sC1'), (u"هاليش", "sV61"),
                    (u"ليش", "sV44"), (u"ش", "sV1")]]

        for word, expected in zip(test_words, expects):
            self.assertEqual(set(expected),
                             set(extract_suffixes(word, suffixes)))
