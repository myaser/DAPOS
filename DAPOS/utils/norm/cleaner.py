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


def split_emoticons(statment):
    '''
        tag positions of emoticons
    '''
    statment.text, statment.tag_dict = split(
        statment.text,
        emoticons_regex,
        EMOTICONS_TAG,
        statment.tag_dict
    )
    return statment


def split_punctuation(statment):
    '''
        tag positions of punctuation
    '''
    statment.text, statment.tag_dict = split(
        statment.text,
        punctuation_regex,
        PUNCTUATION_TAG,
        statment.tag_dict
    )
    return statment


def split_digits(statment):
    '''
        tag positions of digits
    '''
    statment.text, statment.tag_dict = split(
        statment.text,
        float_regex,
        DIGIT_TAG,
        statment.tag_dict
    )
    statment.text, statment.tag_dict = split(
        statment.text,
        digit_regex,
        DIGIT_TAG,
        statment.tag_dict
    )
    
    return statment



def remove_diacritics(statment):
    '''
        remove diacritic from the whole text
        path tag_dict throw it!
    '''
    statment.text = vowels_regex.sub("", statment.text)
    return statment
