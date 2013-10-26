'''segmentation function test'''
# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.stemmer import Word
from DAPOS.data.variation import Prefix, Suffix

class TestSegmentation(unittest.TestCase):
    def test_segment_words(self):
        '''
        test segment words to all possible prefixes, circufixes, and suffixes
        '''

        word = Word(u"")
        self.assertEqual(word.string, u"")
        self.assertEqual(word.stems, [])

        word2 = Word(u"الله")
        self.assertEqual([case for case in word2], [
                (Prefix(u'', classe=u'pC1'), u'الله', Suffix(u'', classe=u'sC1')),
                (Prefix(u'', classe=u'pC1'), u'الل', Suffix(u'ه', classe=u'sC10')),
                (Prefix(u'ال',classe= u'pN1'), u'له', Suffix(u'', classe=u'sC1')),
            ])
