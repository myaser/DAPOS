'''segmentation function test'''
# -*- coding: UTF-8 -*-
import unittest
from DAPOS.data.affixes import prefixes, suffixes
from DAPOS.processor.stemmer import Word
from DAPOS.processor.stemmer.prefix import extract_prefixes
from DAPOS.processor.stemmer.suffix import extract_suffixes


class TestSegmentation(unittest.TestCase):
    def test_segment_words(self):
        '''
        test segment words to all possible prefixes, circufixes, and suffixes
        '''

        word = Word(u"")
        self.assertEqual(word.string, u"")
        self.assertEqual(word.stems, [])

        word2 = Word(u"الله")
        self.assertEqual(set(word2.stems), set([
                ((u'', u'pC1'), u'الله', (u'', u'sC1')),
                ((u'', u'pC1'), u'الل', (u'ه', u'sC10')),
                ((u'ال', u'pN1'), u'له', (u'', u'sC1')),
            ]))
