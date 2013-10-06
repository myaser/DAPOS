from DAPOS.utils import singleton
from icu import BreakIterator, Locale
from DAPOS.utils.interval_overlap import BoundariesOverlap
from itertools import tee


@singleton
class ArabicWordBreakIterator():
    def __init__(self):
        self.BreakIterator = BreakIterator.createWordInstance(
                                                  Locale.createFromName('ar'))

    def analyse(self, text, pre_intervals=[]):
        self.BreakIterator.setText(text)
        boundaries = [0] + [item for item in self.BreakIterator]

        merged = iter(BoundariesOverlap(boundaries, pre_intervals))
        last_boundary = merged.next()

        tokens = []
        for boundary in merged:
            token = text[last_boundary:boundary]
            if token.strip():
                tokens.append(token.strip())
            last_boundary = boundary

        return tokens
