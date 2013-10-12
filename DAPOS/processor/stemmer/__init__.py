from itertools import product

from DAPOS.data.affixes import prefixes, suffixes
from DAPOS.processor.stemmer.prefix import extract_prefixes
from DAPOS.processor.stemmer.suffix import extract_suffixes

from fixer import fix_stem

class Word(object):
    """represent each word in the query"""
    def __init__(self, raw_string):
        self.string = raw_string
        self._prefixes = extract_prefixes(self.string)
        self._suffixes = extract_suffixes(self.string)
        self._prefixes_and_suffixes = [prefix_suffix
            for prefix_suffix in product(self._prefixes, self._suffixes)
            if self.is_valid_segment(prefix_suffix)
        ]
        self.update_stems()

    def _circufix_for(self, prefix="", suffix=""):
        result = self.string
        if prefix:
            result = result[len(prefix):]
        if suffix:
            result = result[:-len(suffix)]
        return result

    def update_stems(self):
        self.stems = []
        for prefix, suffix in self._prefixes_and_suffixes:
            self.stems.append(
                fix_stem(
                    (prefix, self._circufix_for(prefix[0], suffix[0]), suffix)
                )
            )

    def __iter__(self):
        return iter(self.stems)

    def is_valid_segment(self, comination):
        prefix, suffix = comination
        prefix, prefix_type = prefix
        suffix, suffix_type = suffix

        if prefix_type[0] == 'N' and suffix_type[0] == 'V':
            return False
        if prefix_type[0] == 'V' and suffix_type[0] == 'N':
            return False
        if prefix_type in ['N1', 'N2', 'N3', 'N5'] and bool(suffix_type):
            return False
        circufix = self._circufix_for(prefix, suffix)
        if len(circufix) > 1:
            return False
        return True
