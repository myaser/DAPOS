from pipeline import Pipeline
from pipeline.utils import StopPipeline
from functools import partial
from DAPOS.processor.token.segmentation import Word

from DAPOS.processor.norm.cleaner import remove_diacritics, split_emoticons, \
    split_punctuation, split_digits, tagged_text

import re
split_tag_regex = re.compile(ur'([^\s^^]+)<(\w+)>')


def generate_producer(producer, text):
    '''
        return producer for pipeline in the form it deal with
    '''
    return partial(producer, text)

def generate_consumer(consumer):
    '''it should get a function that get one arg, and this function resposble
    for dealling with what to do with data
    '''
    return consumer

def provide_text(text, stage):
    '''
    pipline producer
    '''
    if stage < 1:
        return (text, stage+1)
    else:
        raise StopPipeline("limit reached")

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
        return Word(element).segment()

def tag(text):
    '''get the data in the form the user intered and return tagged words'''
    pipeline = Pipeline(generate_producer(provide_text, text),
        [remove_diacritics, split_emoticons, split_punctuation, split_digits],
        generate_consumer(consume_text))
    cleaned_text = pipeline.follow(0)[0]

    words = [split_tag_or_iffex(word)
        for word in cleaned_text.split()
    ]

    return words


