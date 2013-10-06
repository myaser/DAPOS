# -*- coding: UTF-8 -*-
import unittest
from DAPOS.processor.stemmer.fixer import fix_stem, lam_lam_fix, hamza_fix


class TestFixer(unittest.TestCase):
    def test_fixer(self):
        self.assertEqual(fix_stem(((u'', u''), u'', (u'', u''))),
                         ((u'', u''), u'', (u'', u'')))
        self.assertEqual(
            fix_stem(((u'ال', u'pN1'), u'تلفزيون', (u'', u'pC1'))),
            ((u'ال', u'pN1'), u'تلفزيون', (u'', u'pC1'))
        )
        self.assertEqual(
            fix_stem(((u'', u'pC1'), u'لاجئ', (u'نا', u'sC3'))),
            ((u'', u'pC1'), u'لاجء', (u'نا', u'sC3'))
        )
        self.assertEqual(
            fix_stem(((u'لل', u'pC1'), u'لاجئ', (u'نا', u'sC3'))),
        ((u'ل ال', u'pC1'), u'لاجء', (u'نا', u'sC3'))
        )
        self.assertEqual(
            fix_stem(((u'لل', u'pN13'), u'تلفزيون', (u'', u'pC1'))),
            ((u'ل ال', u'pN13'), u'تلفزيون', (u'', u'pC1'))
        )

    def test_lam_lam_fix(self):
        self.assertEqual(lam_lam_fix(((u'', u''), u'', (u'', u''))),
                         ((u'', u''), u'', (u'', u'')))
        self.assertEqual(
            lam_lam_fix(((u'لل', u'pN13'), u'تلفزيون', (u'', u'pC1'))),
            ((u'ل ال', u'pN13'), u'تلفزيون', (u'', u'pC1'))
        )
        self.assertEqual(
            lam_lam_fix(((u'ال', u'pN1'), u'تلفزيون', (u'', u'pC1'))),
            ((u'ال', u'pN1'), u'تلفزيون', (u'', u'pC1'))
        )

    def test_hamza_fix(self):
        self.assertEqual(hamza_fix(((u'', u''), u'', (u'', u''))),
                         ((u'', u''), u'', (u'', u'')))

        self.assertEqual(
            hamza_fix(((u'', u'pC1'), u'لاجئ', (u'نا', u'sC3'))),
            ((u'', u'pC1'), u'لاجء', (u'نا', u'sC3'))
        )
        self.assertEqual(
            hamza_fix(((u'ال', u'pN1'), u'تلفزيون', (u'', u'pC1'))),
            ((u'ال', u'pN1'), u'تلفزيون', (u'', u'pC1'))
        )
