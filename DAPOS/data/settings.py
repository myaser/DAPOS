# -*- coding: UTF-8 -*-
from DAPOS import settings
import os.path

print "    loading arabic litters constants"

ARABIC_CHARS = [u"\u0621",    # ARABIC LETTER HAMZA
                u"\u0622",    # ARABIC LETTER ALEF WITH MADDA ABOVE
                u"\u0623",    # ARABIC LETTER ALEF WITH HAMZA ABOVE
                u"\u0624",    # ARABIC LETTER WAW WITH HAMZA ABOVE
                u"\u0625",    # ARABIC LETTER ALEF WITH HAMZA BELOW
                u"\u0626",    # ARABIC LETTER YEH WITH HAMZA ABOVE
                u"\u0627",    # ARABIC LETTER ALEF
                u"\u0628",    # ARABIC LETTER BEH
                u"\u0629",    # ARABIC LETTER TEH MARBUTA
                u"\u062A",    # ARABIC LETTER TEH
                u"\u062B",    # ARABIC LETTER THEH
                u"\u062C",    # ARABIC LETTER JEEM
                u"\u062D",    # ARABIC LETTER HAH
                u"\u062E",    # ARABIC LETTER KHAH
                u"\u062F",    # ARABIC LETTER DAL
                u"\u0630",    # ARABIC LETTER THAL
                u"\u0631",    # ARABIC LETTER REH
                u"\u0632",    # ARABIC LETTER ZAIN
                u"\u0633",    # ARABIC LETTER SEEN
                u"\u0634",    # ARABIC LETTER SHEEN
                u"\u0635",    # ARABIC LETTER SAD
                u"\u0636",    # ARABIC LETTER DAD
                u"\u0637",    # ARABIC LETTER TAH
                u"\u0638",    # ARABIC LETTER ZAH
                u"\u0639",    # ARABIC LETTER AIN
                u"\u063A",    # ARABIC LETTER GHAIN
                u"\u0641",    # ARABIC LETTER FEH
                u"\u0642",    # ARABIC LETTER QAF
                u"\u0643",    # ARABIC LETTER KAF
                u"\u0644",    # ARABIC LETTER LAM
                u"\u0645",    # ARABIC LETTER MEEM
                u"\u0646",    # ARABIC LETTER NOON
                u"\u0647",    # ARABIC LETTER HEH
                u"\u0648",    # ARABIC LETTER WAW
                u"\u0649",    # ARABIC LETTER ALEF MAKSURA
                u"\u064A",    # ARABIC LETTER YEH
                u"\u064B",    # ARABIC FATHATAN
                u"\u064C",    # ARABIC DAMMATAN
                u"\u064D",    # ARABIC KASRATAN
                u"\u064E",    # ARABIC FATHA
                u"\u064F",    # ARABIC DAMMA
                u"\u0650",    # ARABIC KASRA
                u"\u0651",    # ARABIC SHADDA
                u"\u0652",    # ARABIC SUKUN
            ]

ARABIC_VOWELS = [u"\u064B",    # ARABIC FATHATAN
                 u"\u064C",    # ARABIC DAMMATAN
                 u"\u064D",    # ARABIC KASRATAN
                 u"\u064E",    # ARABIC FATHA
                 u"\u064F",    # ARABIC DAMMA
                 u"\u0650",    # ARABIC KASRA
                 u"\u0651",    # ARABIC SHADDA
                 u"\u0652",    # ARABIC SUKUN
            ]

emoticons = r"(?:\s|^)([bcopvxBCDILOPSX:っ@Q;°_>,Þ$#03578&%ಠ~\-\\/\*\]\[<\)\(\{\}'\.\^=\|]{2,9})(?=\s|$)"
punctuation = ur"([^\u0621-\u063A^\u0641-\u064A^\w\s]+)"
word = u'([' + "".join(ARABIC_CHARS) + ']+)'
digit = r'\b(\d+)\b'
float_match = r'\b(\d+[.]\d+)\b'
vowels = '[' + "".join(ARABIC_VOWELS) + ']'

prefix_files = [
    os.path.join(settings.PROJECT_ROOT, 'data', 'affixes', 'prefixes.xml'),
]
suffix_files = [
    os.path.join(settings.PROJECT_ROOT, 'data', 'affixes', 'suffixes.xml'),
]
