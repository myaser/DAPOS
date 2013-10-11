from DAPOS.processor.token import tokenize
from DAPOS.utils.norm.validation import is_word, is_digit, is_emoticon, is_punc
from DAPOS.processor.stemmer import Word
from settings import EMOTICONS_TAG, PUNCTUATION_TAG, DIGIT_TAG, NOTDEFINED_TAG

def stem_tokens(tokens):
    for token in tokens:
        if is_word(token):
            yield Word(token).stems
        elif is_digit(token):
            yield [token, DIGIT_TAG]
        elif is_emoticon(token):
            yield [token, EMOTICONS_TAG]
        elif is_punc(token):
            yield [token, PUNCTUATION_TAG]
        else:
            yield [token, NOTDEFINED_TAG]

def tag(text):
    '''get the data in the form the user intered and return tagged words'''
    tokens = tokenize(text)

    return [stemmed_token for stemmed_token in stem_tokens(tokens)]
