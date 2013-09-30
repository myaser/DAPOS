#! /usr/bin/python
'''
pre-process text to remove all not-words words
'''
from DAPOS.data.normalization import (emoticons_regex,
    EMOTICONS_TAG, punctuation_regex, PUNCTUATION_TAG, float_regex, DIGIT_TAG,
    digit_regex, vowels_regex)
from DAPOS.utils.interval_overlap import overlap_with

def split(txt, regex, tag, tag_dict):
    '''
        tag positions of regex matched word
    '''
    for match in regex.finditer(txt):
        if not overlap_with(match.span(), tag_dict):
            tag_dict.update({match.span(): tag})

    return txt, tag_dict


def split_emoticons(txt, tag_dict):
    '''
        tag positions of emoticons
    '''
    return split(txt, emoticons_regex, EMOTICONS_TAG, tag_dict)


def split_punctuation(txt, tag_dict):
    '''
        tag positions of punctuation
    '''
    return split(txt, punctuation_regex, PUNCTUATION_TAG, tag_dict)


def split_digits(txt, tag_dict):
    '''
        tag positions of digits
    '''
    tagged_floats, tag_dict = split(txt, float_regex, DIGIT_TAG, tag_dict)
    return split(tagged_floats, digit_regex, DIGIT_TAG, tag_dict)



def remove_diacritics(txt, tag_dict):
    '''
        remove diacritic from the whole text
        path tag_dict throw it!
    '''
    return vowels_regex.sub("", txt), tag_dict
