# -*- coding: UTF-8 -*-
from pipeline import Pipeline
from pipeline.utils import StopPipeline


def lam_lam_fix(((prefix, prefix_type), stem, suffix)):
    if prefix == u'لل':
        return ((u'ل ال', prefix_type), stem, suffix)
    else:
        return ((prefix, prefix_type), stem, suffix)


def hamza_fix((prefix, stem, (suffix, suffix_type))):
    if stem.endswith(u'ئ') and suffix in [u"ي", u"نا", u"ك", u"كي", u"كم", u"ه", u"ها", u"هم"]:
        stem = stem[:-1] + u'ء'
    return (prefix, stem, (suffix, suffix_type))


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
