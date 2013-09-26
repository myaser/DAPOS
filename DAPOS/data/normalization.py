# -*- coding: UTF-8 -*-
print "    loading normalization patterns and constants"
import re
from chars import ARABIC_VOWELS

emoticons_regex = re.compile("(?:\s|^)([bcopvxBCDILOPSX:っ@Q;°_>,Þ$#03578&%ಠ~\-\\/\*\]\[<\)\(\{\}'\.\^=\|]{2,9})(?=\s|$)\b")
punctuation_regex = re.compile(r'([^\w\s]+)')
digit_regex = re.compile(r'\b(\d+)\b')
float_regex = re.compile(r'\b(\d+[.]\d+)\b')
clock_regex = re.compile(r'\b(\d{1,2}[:]\d{1,2})\b')
date_regex = re.compile(r'\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b')
vowels_regex = re.compile('[' + "".join(ARABIC_VOWELS) + ']')
untagged_text = re.compile('(.+<\w+>)')

EMOTICONS_TAG = 'EMO'
PUNCTUATION_TAG = 'PUNC'
DIGIT_TAG = 'CD'
