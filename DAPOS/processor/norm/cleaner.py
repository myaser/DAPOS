#! /usr/bin/python
from DAPOS.data.normalization import (untagged_text, emoticons_regex,
    EMOTICONS_TAG, punctuation_regex, PUNCTUATION_TAG, float_regex, DIGIT_TAG,
    digit_regex, clock_regex, date_regex, vowels_regex)


def split(txt, regex, tag):
    '''
        add xml-like tag on the matched regex pattern
    '''
    """
    >>> split('the first test 123', '(\d+)', 'CD')
    'the first test 123<CD> '
    >>> split('text not matching regex', '(\d+)', 'CD')
    'text not matching regex'
    """
    if untagged_text.match(txt.strip()) or not txt:
        return txt
    if untagged_text.search(txt.strip()):
        return " ".join([
            split(piece_of_text)
            for piece_of_text in untagged_text.split(txt.strip())
        ])

    return regex.sub(" \g<1><{0}> ".format(tag), txt)


def split_emoticons(txt):
    '''
        add emotion_tag tag to emoticons
    '''
    return split(txt, emoticons_regex, EMOTICONS_TAG)


def split_punctuation(txt):
    '''
        add punctuation_tag tag to punctuations
    '''
    return split(txt, punctuation_regex, PUNCTUATION_TAG)


def split_digits(txt):
    '''
        add digit_tag tag to digits
    '''
    tagged_floats = split(txt, float_regex, DIGIT_TAG)
    return split(tagged_floats, digit_regex, DIGIT_TAG)


def split_clock(txt):
    return split(txt, clock_regex, DIGIT_TAG)


def split_date(txt):
    return split(txt, date_regex, DIGIT_TAG)


def remove_diacritics(txt):
    return vowels_regex.sub("", txt)


def normalize(txt):
    txt = remove_diacritics(txt)
    txt = split_emoticons(txt)
    txt = split_punctuation(txt)
    return split_digits(txt)
