from pipeline import Pipeline
from pipeline.utils import StopPipeline

from DAPOS.processor.token.segmentation import Word
from DAPOS.data.affixes import prefixes, suffixes
from DAPOS.processor.token.segmentation.prefix import extract_prefixes
from DAPOS.processor.token.segmentation.suffix import extract_suffixes
from DAPOS.processor.norm.cleaner import remove_diacritics, split_emoticons, \
    split_punctuation, split_digits
from DAPOS.data.normalization import split_tag_regex, tagged_text


def provide_text(text):
    '''
    pipline producer
    '''
    if text is None:
        raise StopPipeline("limit reached")
    return ((text, {}), None)


def consume_text(text):
    '''consumer function
    it don't do any thing!
    '''
    return text

def split_tag_or_iffex(element):
    '''
        if element was already tagged as punc, cd, or emo, return it as a list
        if not, so it's a word, return it segmented with
        all possible prefixes and suffixes
    '''
    if tagged_text.match(element.strip()):
        return split_tag_regex.split(element.strip())[1:-1]
    else:
        return Word(
            element,
            extract_prefixes,
            extract_suffixes,
            prefixes,
            suffixes
        ).segment()

def tag(text):
    '''get the data in the form the user intered and return tagged words'''
    pipeline = Pipeline(provide_text,
        [remove_diacritics, split_emoticons, split_punctuation, split_digits],
        consume_text)
    cleaned_text = pipeline.follow(text).pop()

    words = [split_tag_or_iffex(word)
        for word in cleaned_text.split()
    ]

    return words


