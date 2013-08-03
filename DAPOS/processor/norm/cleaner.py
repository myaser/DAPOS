#! /usr/bin/python
# -*- coding: UTF-8 -*-


import re


emoticons_regex = "(?:\s|^)([bcopvxBCDILOPSX:っ@Q;°_>,Þ$#03578&%ಠ~\-\\/\*\]\[<\)\(\{\}'\.\^=\|]{2,9})(?=\s|$)\b"
punctuation_regex = r'([^\w\s]+)'
digit_regex = r'\b(\d+)\b'
float_regex = r'\b(\d+[.]\d+)\b'
clock_regex = r'\b(\d{1,2}[:]\d{1,2})\b'
date_regex = r'\b(\d{1,2}[-/]\d{1,2}[-/]\d{2,4})\b'

EMOTICONS_TAG = 'EMO'
PUNCTUATION_TAG = 'PUNC'
DIGIT_TAG = 'CD'


def split(txt, regex, tag):
    '''
        add xml-like tag on the matched regex pattern
    '''
    """
    >>> split('the first test 123', '(\d+)', 'CD')
    'the first test <CD>123</CD> '
    >>> split('text not matching regex', '(\d+)', 'CD')
    'text not matching regex'
    """
    tag_regex = '(<\w+>.+</\w+>)'
    untagged_text_processor = re.compile(tag_regex)
    if untagged_text_processor.match(txt.strip()) or not txt:
        return txt
    if untagged_text_processor.search(txt.strip()):
        return " ".join([
            split(piece_of_text)
            for piece_of_text in untagged_text_processor.split(txt.strip())
        ])

    processor = re.compile(regex)
    return processor.sub(' <{0}>\g<1></{0}> '.format(tag), txt)


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
    pass
