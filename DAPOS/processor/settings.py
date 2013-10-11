from DAPOS import settings

EMOTICONS = getattr(settings, 'EMOTICONS', {})

EMOTICONS_TAG = getattr(settings, 'EMOTICONS_TAG', 'EMO')
PUNCTUATION_TAG = getattr(settings, 'PUNCTUATION_TAG', 'PUNC')
DIGIT_TAG = getattr(settings, 'DIGIT_TAG', 'CD')
NOTDEFINED_TAG = getattr(settings, 'NOTDEFINED', 'NN')
