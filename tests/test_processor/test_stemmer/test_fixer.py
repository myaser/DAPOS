# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.stemmer.fixer import fix_stem, lam_lam_fix, hamza_fix
from DAPOS.data.variation import Prefix, Suffix


class TestFixer(unittest.TestCase):
    def test_fixer(self):
        result = fix_stem((Prefix(u''), u'', Suffix(u'')))
        self.assertEqual(result, (Prefix(u''), u'', Suffix(u'')))

        result = fix_stem((Prefix(u'ال', classe=u'pN1'), u'تلفزيون', Suffix(u'', classe=u'pC1')))
        self.assertEqual(result, (Prefix(u'ال', classe=u'pN1'), u'تلفزيون', Suffix(u'', classe=u'pC1')))

        result = fix_stem((Prefix(u'', classe=u'pC1'), u'لاجئ', Suffix(u'نا', classe=u'sC3')))
        self.assertEqual( result, (Prefix(u'', classe=u'pC1'), u'لاجء', Suffix(u'نا', classe=u'sC3')))

        result = fix_stem((Prefix(u'لل', classe=u'pC1'), u'لاجئ', Suffix(u'نا', classe=u'Sc3')))
        self.assertEqual(result, (Prefix(u'ل ال', classe=u'pC1'), u'لاجء', Suffix(u'نا', classe=u'Sc3')))

        result = fix_stem((Prefix(u'لل', classe=u'pN13'), u'تلفزيون', Suffix(u'', classe=u'pC1')))
        self.assertEqual(result, (Prefix(u'ل ال', classe=u'pN13'), u'تلفزيون', Suffix(u'', classe=u'pC1')))

    def test_lam_lam_fix(self):
        result = lam_lam_fix((Prefix(u''), u'', Suffix(u'')))
        self.assertEqual(result, (Prefix(u''), u'', Suffix(u'')))


        result = lam_lam_fix((Prefix(u'لل', classe=u'pN13'), u'تلفزيون', Suffix(u'', classe=u'pC1')))
        self.assertEqual(result, (Prefix(u'ل ال', classe=u'pN13'), u'تلفزيون', Suffix(u'', classe=u'pC1')))

        result = lam_lam_fix((Prefix(u'ال', classe=u'pN1'), u'تلفزيون', Suffix(u'', classe=u'pC1')))
        self.assertEqual(result, (Prefix(u'ال', classe=u'pN1'), u'تلفزيون', Suffix(u'', classe=u'pC1')))


    def test_hamza_fix(self):
        result = hamza_fix((Prefix(u''), u'', Suffix(u'')))
        self.assertEqual(result, (Prefix(u''), u'', Suffix(u'')))

        result = hamza_fix((Prefix(u'', classe=u'pC1'), u'لاجئ', Suffix(u'نا', classe=u'sC3')))
        self.assertEqual( result, (Prefix(u'', classe=u'pC1'), u'لاجء', Suffix(u'نا', classe=u'sC3')))

        result = hamza_fix((Prefix(u'ال', classe=u'pN1'), u'تلفزيون', Suffix(u'', classe=u'pC1')))
        self.assertEqual(result, (Prefix(u'ال', classe=u'pN1'), u'تلفزيون', Suffix(u'', classe=u'pC1')))
