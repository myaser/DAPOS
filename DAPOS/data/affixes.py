'''
    load prefixes and suffixes in trie.
    It works as singleton; load just one time!
'''
print "    loading affix data"

import xml.etree.ElementTree as ET
from itertools import chain

import datrie
from functools import partial

from settings import ARABIC_CHARS, prefix_files, suffix_files
from variation import Prefix, Suffix

prefixes = datrie.Trie(ARABIC_CHARS)
suffixes = datrie.Trie(ARABIC_CHARS)

def extract_tree(files):
    for xml_file in files:
        yield ET.parse(xml_file).getroot()

def iter_tag(xml, tag):
    return xml.iter(tag)

iter_prefixe = partial(iter_tag, tag='prefixe')
iter_suffixe = partial(iter_tag, tag='suffixe')

for prefix in chain(*map(iter_prefixe, extract_tree(prefix_files))):
    unvoweled_prefix = unicode(prefix.attrib['unvoweledform'])
    prefixes[unvoweled_prefix] = Prefix(
        unvoweled_prefix,
        classe=unicode(prefix.attrib['classe']),
        desc=unicode(prefix.attrib['desc'])
    )


for suffix in chain(*map(iter_suffixe, extract_tree(suffix_files))):
    unvoweled_suffix = unicode(suffix.attrib['unvoweledform'][::-1])
    suffixes[unvoweled_suffix] = Suffix(
        unvoweled_suffix[::-1],
        classe=unicode(suffix.attrib['classe']),
        desc=unicode(suffix.attrib['desc'])
    )

__all__ = ['prefixes', 'suffixes']
