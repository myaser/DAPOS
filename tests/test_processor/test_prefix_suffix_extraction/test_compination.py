'''segmentation function test'''
import unittest
from DAPOS.segmentation import Word
import collections



class TestSegmentation(unittest.TestCase):
    def test_segment_words(self):
        '''
        test segment words to all possible prefixes, circufixes, and suffixes
        '''
        test_data = []
        expected_results = []

        word = Word(u"")
        self.assertEqual(word.stem, u"")
        self.assertEqual(word.segments, [(u"", u"", u""),])

        for word, expected in zip(test_data, expected_results):
            result = segment(word)
            self.assertTrue(isinstance(result, collections.Iterable))
            self.assertEqual(expected, result)


        prefixes = [u"أياضرب", u"أوياضرب", u"أفياضرب", u"سيضرب", u"وسيضرب",
                    u"فسيضرب", u"أسيضرب", u"أوسضرب", u"أفسيضرب",]
        expects_prefixes = [((u"أيا", "N6"), u"ضرب"), ((u"أويا", "N6"), u"ضرب"),
                   ((u"أفيا", "N6"), u"ضرب"), ((u"س", "V1"), u"يضرب"),
                   ((u"وس", "V1"), u"يضرب"), ((u"فس", "V1"), u"يضرب"),
                   ((u"أس", "V1"), u"يضرب"), ((u"أوس", "V1"), u"ضرب"),
                   ((u"أفس", "V1"), u"يضرب")]


        suffixes = [u"كتابك", u"كتابكي", u"كتابكما", u"عضمكوا", u"يضربني",
                      u"مضربش", u"مضربنيش", u"ضربهولنا", u"ضربهولهم",
                      u"ضربهالي", u"ضربهاله", u"ضربلنيش", u"ماضربهاليش",
                      u"مضربهلناش",]
        expects_suffixes = [((u"ك", "C2"), u"كتاب"), ((u"كي", "C2"), u"كتاب"),
                   ((u"كما","C2"), u"كتاب"), ((u"كوا","C2"), u"عضم"),
                   ((u"ني", "V1"), u"يضرب"), ((u"ش", "V2"), u"يضرب"),
                   ((u"نيش", "V2"), u"يضرب"), ((u"هولنا", "V3"), u"ضرب"),
                   ((u"هولهم", "V3"), u"ضرب"), ((u"هالي", "V3"), u"ضرب"),
                   ((u"هاله", "V3"), u"ضرب"), ((u"هالها", "V3"), u"ضرب"), 
                   ((u"لنيش", "V4"), u"ضرب"), ((u"ليش", "V4"), u"ضربه"),
                   ((u"هالناش", "V5"), u"مضرب")]
