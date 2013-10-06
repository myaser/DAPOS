# coding: UTF-8 -*-
import unittest
from DAPOS.processor.token import tokenize, detect_special_tokens


class TestTokenization(unittest.TestCase):
    def test_token(self):
        self.assertEqual(
            tokenize(u"دراسة: عقار الهلوسة لعلاج الادمان على الكحول"),
            [u"دراسة", u":", u"عقار", u"الهلوسة",
             u"لعلاج", u"الادمان", u"على", u"الكحول"]
        )
        self.assertEqual(
            tokenize(u"المواطن البسيط مبيتمناش حكومة ثورية ولا ديمقراطية وطبعا ميعرفش خالد علي عشان يتمنى فوزه الامنية الوحيدة اللي دماغه هو ان نفسه يقف قدام الجزار"),
            [u"المواطن", u"البسيط", u"مبيتمناش", u"حكومة", u"ثورية", u"ولا",
             u"ديمقراطية", u"وطبعا", u"ميعرفش", u"خالد", u"علي", u"عشان",
             u"يتمنى", u"فوزه", u"الامنية", u"الوحيدة", u"اللي", u"دماغه",
             u"هو", u"ان", u"نفسه", u"يقف", u"قدام", u"الجزار"]
        )
        self.assertEqual(
            tokenize(u"وايوه اللي في البرلمان دول ما عندهمش اخلاق. واحد سلم صاحبه اللي كانوا حيموتوا سوا حيبقى على مين. بس فيه ناس مارضيتش"),
            [u"وايوه", u"اللي", u"في", u"البرلمان", u"دول", u"ما", u"عندهمش",
             u"اخلاق", u".", u"واحد", u"سلم", u"صاحبه", u"اللي", u"كانوا",
             u"حيموتوا", u"سوا", u"حيبقى", u"على", u"مين", u".", u"بس", u"فيه",
             u"ناس", u"مارضيتش"]
        )

    def test_special_tokens(self):
        special_tokens = {u":)": "happy"}
        self.assertEqual(detect_special_tokens(u'إن الله معنا :)',
                                               special_tokens), [(13, 15)])
