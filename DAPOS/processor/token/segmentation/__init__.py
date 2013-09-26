from prefix import extract_prefixes, iter_prefixes
from suffix import extract_suffixes, iter_suffixes
from itertools import product



class Word(object):
    """represent each word in the query"""
    def __init__(self, raw_string):
        self.string = raw_string
        self.prefixes = extract_prefixes(self.string)
        self.suffixes = extract_suffixes(self.string)

    def _circufix_for(self, prefix="", suffix=""):
        return self.string[len(prefix):-len(suffix)]

    def segment(self):
        prefixes_and_suffixes = filter(
            product(self.prefixes, self.suffixes),
            self.is_valid_segment
        )

        segments = []
        for prefix, suffix in prefixes_and_suffixes:
            segments.append(
                (prefix, self._circufix_for(prefix, suffix), suffix)
            )
        return segments

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
        if len(circufix) > 9 or len(circufix) < 2:
            return False
        return True
