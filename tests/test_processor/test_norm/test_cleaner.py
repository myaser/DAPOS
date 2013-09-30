# -*- coding: UTF-8 -*-

import unittest
from DAPOS.processor.norm.cleaner import remove_diacritics, split_emoticons, \
    split_punctuation, split_digits


def normalize(txt):
    result = remove_diacritics(txt, {})
    result = split_emoticons(*result)
    result = split_punctuation(*result)
    result = split_digits(*result)
    return result

class MainFunctionalityTest(unittest.TestCase):
    def test_split(self):

        self.assertEqual(('text not matching regex', {}),
                         normalize('text not matching regex'))
        self.assertEqual(('the first test 123', {(15, 18): 'CD'}),
                         normalize('the first test 123'))
        self.assertEqual(normalize(u'1- بسمك اللهم، :)'),
                         (u'1- بسمك اللهم، :)', {(0,1): 'CD',
                                                 (1,2):'PUNC',
                                                 (13,14):'PUNC',
                                                 (15,17): 'EMO'}))
