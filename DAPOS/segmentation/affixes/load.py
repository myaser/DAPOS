# -*- coding: UTF-8 -*-

import xml.etree.ElementTree as ET
import datrie
import os.path
from itertools import chain


ARABIC_CHARS = u"اآأإبتثجحخدذرزسشصضظعغفقكلمنهوؤيى"

prefixes = datrie.Trie(ARABIC_CHARS)
suffixes = datrie.Trie(ARABIC_CHARS)


_path = os.path.abspath(__file__)
_xml_prefixes = ET.parse(os.path.join(path, 'prefixes.xml')).getroot()
_xml_prefixes_EA = ET.parse(os.path.join(path, 'prefixes_EA_added.xml')).getroot()
_xml_suffixes = ET.parse(os.path.join(path, 'suffixes.xml')).getroot()
_xml_suffixes_EA = ET.parse(os.path.join(path, 'suffixes_EA_added.xml')).getroot()


for prefix in chain(_xml_prefixes.iter('prefixe'),
                    _xml_prefixes_EA.iter('prefixe')):
    prefixes[prefix.attrib['unvoweledform']] = prefix.attrib['classe']

for suffix in chain(_xml_suffixes.iter('suffixe'),
                    _xml_suffixes_EA.iter('suffixe')):
    suffixes[suffix.attrib['unvoweledform'][::-1]] = suffix.attrib['classe']
