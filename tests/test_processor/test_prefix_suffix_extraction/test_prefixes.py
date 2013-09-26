# -*- coding: UTF-8 -*-

import sys
import os.path
sys.path.append(os.path.join(os.path.abspath(__file__), '..', '..'))

import unittest
from DAPOS.segmentation import extract_prefixes


class PrefixTest(unittest.TestCase):
    def test_prefix(self):
        '''check if prefix method return the expected
           longest prefix in the expected form'''
        test_words = [u"أياضرب", u"أوياضرب", u"أفياضرب", u"سيضرب", u"وسيضرب",
                      u"فسيضرب", u"أسيضرب", u"أوسضرب", u"أفسيضرب",]
        expects = [((u"أيا", "N6"), u"ضرب"), ((u"أويا", "N6"), u"ضرب"),
                   ((u"أفيا", "N6"), u"ضرب"), ((u"س", "V1"), u"يضرب"),
                   ((u"وس", "V1"), u"يضرب"), ((u"فس", "V1"), u"يضرب"),
                   ((u"أس", "V1"), u"يضرب"), ((u"أوس", "V1"), u"ضرب"),
                   ((u"أفس", "V1"), u"يضرب")]

        for word, expected in zip(test_words, expects):
            self.assertEqual(expected, extract_prefixes(word))

if __name__ == '__main__':
    unittest.main()
