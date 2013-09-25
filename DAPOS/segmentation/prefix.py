'''
prefix related logic
'''
# -*- coding: UTF-8 -*-

from DAPOS.segmentation.affixes.load import prefixes


def iter_prefixes(raw):
    '''
        extract all posible prefixes for the raw string
        iter results, it give better performance with loops
    '''
    for prefix in prefixes.iter_prefix_items(raw):
        yield prefix


def extract_prefixes(raw):
    '''
        extract all posible prefixes for the raw string
    '''
    return list(iter_prefixes(raw))
