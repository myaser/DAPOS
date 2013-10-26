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

    def test_easy_first(self):
        word3 = Word(u"لي")
        self.assertEqual(word3.stems, [(Prefix(u"ل"), u"ي",   Suffix(u""))])

        word4 = Word(u"لكم")
        self.assertEqual(word4.stems, [(Prefix(u"ل"), u"كم",  Suffix(u""))])
        word5 = Word(u"لكما")
        self.assertEqual(word5.stems, [(Prefix(u"ل"), u"كما", Suffix(u""))])

    def test_variations(self):
        word = Word(u'مدرستها')
        self.assertEqual(word.stems, [
            (Prefix(u'', classe=u'', desc=u''), u'مدرستها', Suffix(u'', classe=u'', desc=u'')),
            (Prefix(u'', classe=u'', desc=u''), u'مدرست', Suffix(u'ها', classe=u'sC11', desc=u'PRP|OBJP')),
            (Prefix(u'', classe=u'', desc=u''), u'مدرسة', Suffix(u'ها', classe=u'sC11', desc=u'PRP|O,BJP')),
            (Prefix(u'م', classe=u'pV1', desc=u'NG'), u'درستها', Suffix(u'', classe=u'', desc=u'')),
            (Prefix(u'م', classe=u'pV1', desc=u'NG'), u'درست', Suffix(u'ها', classe=u'sC11', desc=u'PRP|OBJP')),
            (Prefix(u'م', classe=u'pV1', desc=u'NG'), u'درسة', Suffix(u'ها', classe=u'sC11', desc=u'PRP|OBJP'))
        ])
