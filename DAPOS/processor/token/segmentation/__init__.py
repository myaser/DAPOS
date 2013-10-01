from itertools import product


class Word(object):
    """represent each word in the query"""
    def __init__(self, raw_string, prefix_extractor,
                 suffix_extractor, prefix_trie, suffix_trie):
        self.string = raw_string
        self.prefix_extractor = prefix_extractor
        self.suffix_extractor = suffix_extractor
        self.prefixes = self.prefix_extractor(self.string, prefix_trie)
        self.suffixes = self.suffix_extractor(self.string, suffix_trie)

    def _circufix_for(self, prefix="", suffix=""):
        result = self.string
        if prefix:
            result = result[len(prefix):]
        if suffix:
            result = result[:-len(suffix)]
        return result

    def segment(self):
        prefixes_and_suffixes = filter(
            self.is_valid_segment,
            product(self.prefixes, self.suffixes)
        )

        segments = []
        for prefix, suffix in prefixes_and_suffixes:
            segments.append(
                (prefix, self._circufix_for(prefix[0], suffix[0]), suffix)
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
