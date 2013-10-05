'''
suffix related logic
'''
from DAPOS.data.affixes import suffixes


def iter_suffixes(raw, suffix_trie=suffixes):
    '''
        extract all posible suffixes for the raw string
        iter results, it give better performance with loops
    '''
    yield u"", suffix_trie[u'']
    for suffix, suffix_type in suffix_trie.iter_prefix_items(
                                unicode(raw[::-1])):
        yield suffix[::-1], suffix_type


def extract_suffixes(raw, suffix_trie=suffixes):
    '''
        extract all posible suffixes for the raw string
    '''
    return list(iter_suffixes(raw, suffix_trie))
