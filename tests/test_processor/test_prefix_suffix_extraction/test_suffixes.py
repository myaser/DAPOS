# -*- coding: UTF:8 -*-

import unittest
from DAPOS.processor.token.segmentation import extract_suffixes


class TestSuffix(unittest.TestCase):
    def test_suffix(self):
        '''check if suffix method return the expected
           longest prefix in the expected form'''
        test_words = [u"كتابك", u"كتابكي", u"كتابكما", u"عضمكوا", u"يضربني",
                      u"مضربش", u"مضربنيش", u"ضربهولنا", u"ضربهولهم",
                      u"ضربهالي", u"ضربهاله", u"ضربلنيش", u"ماضربهاليش",
                      u"مضربهلناش",]
        expects = [[(u'', u'C1'), (u"ك", "C2")],
                   [(u'', u'C1'), (u"كي", "C2"), (u"ي", "C2")],
                   [(u'', u'C1'), (u"كما","C2")], 
                   [(u'', u'C1'), (u"كوا","C2"),],
                   [(u'', u'C1'), (u"ني", "V1"), (u"ي", "C2")],
                   [(u'', u'C1'), (u"ش", "V2")],
                   [(u'', u'C1'), (u"نيش", "V2"), (u"ش", "V2")],
                   [(u'', u'C1'), (u"هولنا", "V3"), (u"نا", "C2"),],
                   [(u'', u'C1'), (u"هولهم", "V3"), (u"هم", u"C3"),],
                   [(u'', u'C1'), (u"هالي", "V3"), (u"ي", "C2"),],
                   [(u'', u'C1'), (u"هاله", "V3"), (u"ه", u"C3"),],
                   [(u'', u'C1'), (u"لنيش", "V4"),
                    (u"ش", "V2"), (u"نيش", "V2")],
                   [(u'', u'C1'), (u"هاليش", "V5"),
                    (u"ليش", "V4"), (u"ش", "V2")]]

        for word, expected in zip(test_words, expects):
            self.assertEqual(set(expected), set(extract_suffixes(word)))
