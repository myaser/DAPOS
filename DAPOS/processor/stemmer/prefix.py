'''
prefix related logic
'''
from DAPOS.data.affixes import prefixes


def iter_prefixes(raw, prefixes_trie=prefixes):
    '''
        extract all posible prefixes for the raw string
        iter results, it give better performance with loops
    '''
    yield prefixes_trie[u'']
    for prefix in prefixes_trie.iter_prefix_items(unicode(raw)):
        yield prefix[1]


def extract_prefixes(raw, prefixes_trie=prefixes):
    '''
        extract all posible prefixes for the raw string
    '''
    return list(iter_prefixes(raw, prefixes_trie))
