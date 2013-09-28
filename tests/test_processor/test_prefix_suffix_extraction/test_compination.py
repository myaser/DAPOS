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
        test_data = []
        expected_results = []

        word = Word(u"")
        # import pdb; pdb.set_trace()
        self.assertEqual(word.string, u"")
        self.assertEqual(word.segment(), [])

        for word, expected in zip(test_data, expected_results):
            result = segment(word)
            self.assertTrue(isinstance(result, collections.Iterable))
            self.assertEqual(expected, result)
