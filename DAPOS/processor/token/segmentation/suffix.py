'''
suffix related logic
'''
from DAPOS.data.affixes import suffixes


def iter_suffixes(raw):
    '''
        extract all posible suffixes for the raw string
        iter results, it give better performance with loops
    '''
    for suffix in suffixes.iter_prefix_items(raw[::-1]):
        yield suffix


def extract_suffixes(raw):
    '''
        extract all posible suffixes for the raw string
    '''
    return list(iter_suffixes(raw))
