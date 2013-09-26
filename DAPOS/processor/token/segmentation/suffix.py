'''
suffix related logic
'''
from DAPOS.data.affixes import suffixes


def iter_suffixes(raw):
    '''
        extract all posible suffixes for the raw string
        iter results, it give better performance with loops
    '''
    yield u"", u"C1"
    for suffix, suffix_type in suffixes.iter_prefix_items(unicode(raw[::-1])):
        yield suffix[::-1], suffix_type


def extract_suffixes(raw):
    '''
        extract all posible suffixes for the raw string
    '''
    return list(iter_suffixes(raw))
