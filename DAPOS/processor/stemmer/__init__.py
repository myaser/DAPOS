from itertools import product

from DAPOS.processor.stemmer.prefix import extract_prefixes
from DAPOS.processor.stemmer.suffix import extract_suffixes

from fixer import fix_stem, find_alternate_compination
from validate import has_valid_len, prefix_DT_no_suffix
from settings import EASY_WORDS

class Word(object):
    """represent each word in the query"""
    VALIDATORS = [has_valid_len, prefix_DT_no_suffix, ]
    def __init__(self, raw_string):
        self.string = raw_string
        if EASY_WORDS.get(self.string, None):
            self.stems = EASY_WORDS[self.string]
        else:
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
            stem = self._circufix_for(prefix.string, suffix.string)
            compination = fix_stem((prefix, stem, suffix))
            self.stems.append(compination)
            alt_compination = find_alternate_compination(compination)
            if alt_compination:
                self.stems.append(alt_compination)


    def __iter__(self):
        return iter(self.stems)

    def is_valid_segment(self, (prefix, suffix)):
        circufix = self._circufix_for(prefix.string, suffix.string)
        for validator in self.VALIDATORS:
            if not validator(prefix, circufix, suffix):
                return False
        return True
