from pipeline import Pipeline
from pipeline.utils import StopPipeline

from DAPOS.processor.token.segmentation import Word
from DAPOS.data.affixes import prefixes, suffixes
from DAPOS.processor.token.segmentation.prefix import extract_prefixes
from DAPOS.processor.token.segmentation.suffix import extract_suffixes
from DAPOS.processor.norm.cleaner import remove_diacritics, split_emoticons, \
    split_punctuation, split_digits


class Statment(object):
    """docstring for Statment"""
    def __init__(self, text):
        self.text = text
        self.tag_dict = {}

    def __iter__(self):
        # TODO: write it to return iterator for words of system
        pass

def provide_text(statment):
    '''
    pipline producer
    '''
    if statment is None:
        raise StopPipeline("limit reached")
    return statment, None


def consume_text(statment):
    '''consumer function
    it don't do any thing!
    '''
    return statment


def tag(text):
    '''get the data in the form the user intered and return tagged words'''
    statment = Statment(text)
    pipeline = Pipeline(provide_text,
        [remove_diacritics, split_emoticons, split_punctuation, split_digits],
        consume_text)
    cleaned_statment = pipeline.follow(statment).pop()

    words = [word
        for word in cleaned_statment
    ]

    return words


