# -*- coding: UTF-8 -*-

import unittest
from DAPOS.processor.norm.cleaner import split, normalize
import re

spaces = re.compile(u"\s+")
def remove_spaces(s):
    return spaces.sub(' ', s).strip()

class MainFunctionalityTest(unittest.TestCase):
    def test_split(self):
        self.assertEqual('the first test 123<CD>',
                         remove_spaces(normalize('the first test 123')))
        self.assertEqual('the first test 123<CD>',
                         remove_spaces(normalize('the first test 123')))
        self.assertEqual('text not matching regex',
                         remove_spaces(normalize('text not matching regex')))

        self.assertEqual(remove_spaces(normalize(u'1- بسمك اللهم، :)')),
                         u'1<CD> -<PUNC> بسمك اللهم ،<PUNC> :)<EMO>')
