# -*- coding: UTF-8 -*-
print "    loading normalization patterns and constants"
import re
from settings import ARABIC_VOWELS
from settings import emoticons, punctuation, digit, float_match, vowels

emoticons_regex = re.compile(emoticons)
punctuation_regex = re.compile(punctuation)
digit_regex = re.compile(digit)
float_regex = re.compile(float_match)
vowels_regex = re.compile(vowels)

EMOTICONS_TAG = 'EMO'
PUNCTUATION_TAG = 'PUNC'
DIGIT_TAG = 'CD'
