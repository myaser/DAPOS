'''segmentation function test'''
# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.token.segmentation import Word
from DAPOS.data.affixes import prefixes, suffixes
from DAPOS.processor.token.segmentation.prefix import extract_prefixes
from DAPOS.processor.token.segmentation.suffix import extract_suffixes


class TestSegmentation(unittest.TestCase):
    def test_segment_words(self):
        '''
        test segment words to all possible prefixes, circufixes, and suffixes
        '''

        word = Word(u"",
            extract_prefixes,
            extract_suffixes,
            prefixes,
            suffixes
        )
        self.assertEqual(word.string, u"")
        self.assertEqual(word.segment(), [])

        word2 = Word(u"الله",
            extract_prefixes,
            extract_suffixes,
            prefixes,
            suffixes
        )
        self.assertEqual(set(word2.segment()), set([
                ((u'', u'pC1'), u'الله', (u'', u'sC1')),
                ((u'', u'pC1'), u'الل', (u'ه', u'sC10')),
                ((u'ال', u'pN1'), u'له', (u'', u'sC1')),
            ]))
