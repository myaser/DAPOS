print "    loading affix data"

import os
import xml.etree.ElementTree as ET
from itertools import chain

import datrie

from chars import ARABIC_CHARS


prefixes = datrie.Trie(ARABIC_CHARS)
suffixes = datrie.Trie(ARABIC_CHARS)

# _path = os.path.abspath(os.path.join(__file__, os.path.pardir, 'affixes'))
# _xml_khalil_prefixes = ET.parse(os.path.join(_path, 'KHALIL_prefixes.xml')).getroot()
# _xml_dapos_prefixes = ET.parse(os.path.join(_path, 'DAPOS_prefixes.xml')).getroot()
# 
# _xml_khalil_suffixes = ET.parse(os.path.join(_path, 'KHALIL_suffixes.xml')).getroot()
# _xml_dapos_suffixes = ET.parse(os.path.join(_path, 'DAPOS_suffixes.xml')).getroot()
# 
# for prefix in chain(_xml_khalil_prefixes.iter('prefixe'),
#                     _xml_dapos_prefixes.iter('prefixe')):
#     prefixes[prefix.attrib[u'unvoweledform']] = prefix.attrib['classe']
# 
# for suffix in chain(_xml_khalil_suffixes.iter('suffixe'),
#                     _xml_dapos_suffixes.iter('suffixe')):
#     suffixes[suffix.attrib[u'unvoweledform'][::-1]] = suffix.attrib['classe']

__all__ = ['prefixes', 'suffixes']
