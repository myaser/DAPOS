# -*- coding: UTF-8 -*-

import unittest
from DAPOS.utils.norm.cleaner import remove_diacritics



class CleanerTest(unittest.TestCase):
    def test_remove_diacritics(self):
        self.assertEqual(remove_diacritics(u''), u'')
        self.assertEqual(
            remove_diacritics(u'بسم الله الرحمن الرحيم'),
            u'بسم الله الرحمن الرحيم'
        )
        self.assertEqual(
            remove_diacritics(
              u'لَا يُحِبُّ اللَّهُ الْجَهْرَ بِالسُّوءِ مِنَ ' \
              u'الْقَوْلِ إِلَّا مَنْ ظُلِمَ وَكَانَ اللَّهُ سَمِيعًا عَلِيمًا'
            ),
            u'لا يحب الله الجهر بالسوء من القول إلا من ظلم وكان الله سميعا عليما'
        )
