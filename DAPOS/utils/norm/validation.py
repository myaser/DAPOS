from DAPOS.data.normalization import punctuation_regex, digit_regex, word_regex
from settings import EMOTICONS

def is_word(value):
    return bool(word_regex.match(value))

def is_punc(value):
    return bool(punctuation_regex.match(value))

def is_emoticon(value):
    return bool(EMOTICONS.get(value, None))

def is_digit(value):
    return bool(digit_regex.match(value))
