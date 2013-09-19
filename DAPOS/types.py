#!/usr/bin/python
# -*- Codign:UTF-8 -*-

from DAPOS.processor.norm import cleaner


class DAText(object):
    UNTAGGED = "0"
    # TAG** = "1"

    def __init__(self, input_data):
        self.txt = input_data
        self.words = self._split(self.txt)

    def _split(self, data):
        return ((word, (None, None), self.UNTAGGED) for word in data.split())

    @property
    def get_tagged(self):
        return filter(self.words, lambda x: x[2] != self.UNTAGGED)

    @tagged.setter
    def set_tagged(self, span, tag):
        

    @property
    def get_untagged(self):
        return filter(self.words, lambda x: x[2] == self.UNTAGGED)

    def __getitem__(self, index):
        return self.words[index]

    def __iter__(self):
        for word in self.words:
            yield (word[0], word[2])

    def cleaned_data(self):
        pass

    def tags(self):
        return tuple(set(
            tag for _, _, tag in self.words
        ))

    def _norm(self):
        cleaner.split_emoticons(self.txt)
