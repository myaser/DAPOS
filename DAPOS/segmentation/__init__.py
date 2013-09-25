from DAPOS.segmentation.prefix import extract_prefix, iter_prefixes
from DAPOS.segmentation.suffix import extract_suffix, iter_suffixes
from itertools import product as _product

def product(prefixes, suffixes, *args, **kwds):
    '''
        extend for product function in main liberaries to make it
        return prefixes and suffixes without combination
    '''
    fillvalue = kwds.get('fillvalue', [])
    prefixes_pools = map(tuple, prefixes) * kwds.get('repeat', 1)
    suffixes_pools = map(tuple, suffixes) * kwds.get('repeat', 1)
    for prefix in prefixes_pools:
        yield prefix, fillvalue
    for combination in _product(prefixes, suffixes, *args, **kwds):
        yield combination
    for suffix in suffixes_pools:
        yield suffix, fillvalue


class Word(object):
    """represent each word in the query"""
    def __init__(self, raw_string):
        self.string = raw_string
        self.prefixes = extract_prefix(self.string)
        self.suffixes = extract_suffix(self.string)

    def _circufix_for(self, prefix="", suffix=""):
        return self.string[len(prefix):-len(suffix)]

    def segment(self):
        prefixes_and_suffixes = filter(
            product(self.prefixes, self.suffixes, fillvalue=("", "")),
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

        if prefix_type[0] != suffix_type[0]:
            return False
        circufix = self._circufix_for(prefix, suffix)
        if len(circufix) > 9 or len(circufix) < 2:
            return False
        if prefix_type in ['N1', 'N2', 'N3', 'N5'] and bool(suffix_type):
            return False
        return True
