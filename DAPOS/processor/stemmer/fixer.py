# -*- coding: UTF-8 -*-
from pipeline import Pipeline
from pipeline.utils import StopPipeline


def lam_lam_fix((prefix, stem, suffix)):
    if prefix == u'لل':
        prefix.string = u'ل ال'
        return (prefix, stem, suffix)
    else:
        return (prefix, stem, suffix)


def hamza_fix((prefix, stem, suffix)):
    if stem.endswith(u'ئ') and suffix.string in [u"ي", u"نا", u"ك", u"كي", u"كم", u"ه", u"ها", u"هم"]:
        stem = stem[:-1] + u'ء'
    return (prefix, stem, suffix)


def provide_compination(compination):
    if compination is None:
        raise StopPipeline("limit reached")
    else:
        return compination, None


def consumer(compination):
    return compination


def fix_stem((prefix, stem, suffix)):
    stages = [hamza_fix, lam_lam_fix]
    fixxer = Pipeline(provide_compination, stages, consumer)
    return fixxer.follow((prefix, stem, suffix)).pop()


def find_alternate_compination((prefix, stem, suffix)):
    if stem.endswith(u'ت'):
        stem = stem[:-1] + 'ة'
        return (prefix, stem, suffix)
