'''segmentation function test'''
# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.token.segmentation import Word
import collections



class TestSegmentation(unittest.TestCase):
    def test_segment_words(self):
        '''
        test segment words to all possible prefixes, circufixes, and suffixes
        '''

        word = Word(u"")
        self.assertEqual(word.string, u"")
        self.assertEqual(word.segment(), [])

        word2 = Word(u"الله")
        self.assertEqual(set(word2.segment()), set([
                ((u'', u'C1'), u'الله', (u'', u'C1')),
                ((u'', u'C1'), u'الل', (u'ه', u'C3')),
            ]))
