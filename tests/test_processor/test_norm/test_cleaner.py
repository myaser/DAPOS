# -*- coding: UTF-8 -*-

import unittest
from DAPOS.processor.norm.cleaner import remove_diacritics, split_emoticons, \
    split_punctuation, split_digits


def normalize(statment):
    statment = remove_diacritics(statment)
    statment = split_emoticons(statment)
    statment = split_punctuation(statment)
    statment = split_digits(statment)
    return statment

class MockStatment(object):
    def __init__(self, text):
        self.text = text
        self.tag_dict = {}


class MainFunctionalityTest(unittest.TestCase):
    def test_split(self):
        # statment1 = MockStatment('text not matching regex')
        # normalize(statment1)
        # self.assertEqual({}, statment1.tag_dict)

        # statment2 = MockStatment('the first test 123')
        # normalize(statment2)
        # self.assertEqual({(15, 18): 'CD'}, statment2.tag_dict)

        statment3 = MockStatment(u'1- بسمك اللهم، :)')
        normalize(statment3)
        self.assertEqual(
            {
                (0,1): 'CD',
                (1,2):'PUNC',
                (13,14):'PUNC',
                (15,17): 'EMO'
            },
            statment3.tag_dict)
