# -*- coding: UTF-8 -*-

import unittest
from DAPOS.processor.stemmer.validate import has_valid_len, prefix_DT_no_suffix
from DAPOS.data.variation import Prefix, Suffix


class TestValidation(unittest.TestCase):
    def test_prefix_DT(self):
        result = prefix_DT_no_suffix(Prefix(u'', classe=u'', desc=u''), u'', Suffix(u'', classe=u'', desc=u''))
        self.assertTrue(result)

        result = prefix_DT_no_suffix(Prefix(u'وال', classe=u'pN2', desc=u'CC+DT'), u'', Suffix(u'', classe=u'', desc=u''))
        self.assertTrue(result)

        result = prefix_DT_no_suffix(Prefix(u'ال', classe=u'pN1', desc=u'DT'), u'', Suffix(u'', classe=u'', desc=u''))
        self.assertTrue(result)

        result = prefix_DT_no_suffix(Prefix(u'وال', classe=u'pN2', desc=u'CC+DT'), u'', Suffix("ي", desc="PRP|OBJP", classe="sC2"))
        self.assertFalse(result)


    def test_valid_len(self):
        result = has_valid_len(Prefix(u'', classe=u'', desc=u''), u'', Suffix(u'', classe=u'', desc=u''))
        self.assertFalse(result)

        result = has_valid_len(Prefix(u'', classe=u'', desc=u''), u'ا', Suffix(u'', classe=u'', desc=u''))
        self.assertFalse(result)

        result = has_valid_len(Prefix(u'', classe=u'', desc=u''), u'بحباني', Suffix(u'', classe=u'', desc=u''))
        self.assertTrue(result)

        result = has_valid_len(Prefix(u'و', classe=u'pC2', desc=u'CC'), u'يعرب', Suffix(u'', classe=u'', desc=u''))
        self.assertTrue(result)
