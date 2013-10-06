# TODO: Copyrights, license Documentation
"""
This package contains tokenization functionality
"""
from settings import special_tokens
from DAPOS.utils.norm.cleaner import remove_diacritics

from unicode_29 import ArabicWordBreakIterator
import re

space_splitter = re.compile('([^\s]+)')


def detect_special_tokens(text, tokens):
    '''detect positions of special tokens should be out of tokonization process
    '''
    intervals = []
    for token in space_splitter.finditer(text):
        if tokens.get(token.group(), None) is not None:
            intervals.append(token.span())
    return intervals


def tokenize(text):
    '''convert raw text into list of tokens'''
    # TODO: get pre-tokenization in settings file
    text = remove_diacritics(text)
    pre_intervals = detect_special_tokens(text, special_tokens)

    word_breaker = ArabicWordBreakIterator()
    return word_breaker.analyse(text, pre_intervals)
