from DAPOS.utils import singleton
from icu import BreakIterator, Locale


@singleton
class ArabicWordBreakIterator():
    def __init__(self):
        self.BreakIterator = BreakIterator.createWordInstance(
                                                  Locale.createFromName('ar'))

    def analyse(self, text):
        self.BreakIterator.setText(text)
        boundaries = [0] + [item for item in self.BreakIterator]

        return [text.__getslice__(*boundaries[i: i + 2])
                for i in range(len(boundaries) - 1)]
