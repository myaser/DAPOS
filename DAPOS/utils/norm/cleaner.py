#! /usr/bin/python
'''
pre-process text to remove all not-words words
'''
from DAPOS.data.normalization import vowels_regex


def remove_diacritics(text):
    '''
        remove diacritic from the whole text
        path tag_dict throw it!
    '''
    return vowels_regex.sub("", text)
