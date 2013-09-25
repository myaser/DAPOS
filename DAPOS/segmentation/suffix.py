'''
suffix related logic
'''
#-*- coding: UTF-8 -*-
from affixes.load import suffixes



def iter_suffixes(raw):
    '''
        extract all posible suffixes for the raw string
        iter results, it give better performance with loops
    '''
    for suffix in suffixes.iter_prefix_items(unicode(raw[::-1])):
        yield suffix

def extract_suffix(raw):
    '''
        extract all posible suffixes for the raw string
    '''
    return list(iter_suffixes(raw))
