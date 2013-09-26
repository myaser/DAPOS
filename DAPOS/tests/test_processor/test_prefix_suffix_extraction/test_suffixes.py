# -*- coding: UTF:8 -*-

import unittest
from DAPOS.segmentation import extract_suffixes


class TestSuffix(unittest.TestCase):
    def test_suffix(self):
        '''check if suffix method return the expected
           longest prefix in the expected form'''
        test_words = [u"كتابك", u"كتابكي", u"كتابكما", u"عضمكوا", u"يضربني",
                      u"مضربش", u"مضربنيش", u"ضربهولنا", u"ضربهولهم",
                      u"ضربهالي", u"ضربهاله", u"ضربلنيش", u"ماضربهاليش",
                      u"مضربهلناش",]
        expects = [((u"ك", "C2"), u"كتاب"), ((u"كي", "C2"), u"كتاب"),
                   ((u"كما","C2"), u"كتاب"), ((u"كوا","C2"), u"عضم"),
                   ((u"ني", "V1"), u"يضرب"), ((u"ش", "V2"), u"يضرب"),
                   ((u"نيش", "V2"), u"يضرب"), ((u"هولنا", "V3"), u"ضرب"),
                   ((u"هولهم", "V3"), u"ضرب"), ((u"هالي", "V3"), u"ضرب"),
                   ((u"هاله", "V3"), u"ضرب"), ((u"هالها", "V3"), u"ضرب"), 
                   ((u"لنيش", "V4"), u"ضرب"), ((u"ليش", "V4"), u"ضربه"),
                   ((u"هالناش", "V5"), u"مضرب")]

        for word, expected in zip(test_words, expects):
            self.assertEqual(expected, extract_suffixes(word))




