# -*- coding: UTF-8 -*-


def is_contain(tag, tags_list):
    for t in tags_list:
        if tag in t.split(u'+'):
            return True
    return False

def prefix_DT_no_suffix(*compination):
    _, prefix_desc, _, _, suffix_desc = extract_args(*compination)

    if is_contain('DT', prefix_desc):
        if suffix_desc != [u'']:
            return False
    return True

def has_valid_len(*compination):
    _, _, circufix, _, _ = extract_args(*compination)
    return len(circufix) >= 2

def extract_args(prefix, stem, suffix):
    return prefix.type, prefix.desc, stem, suffix.type, suffix.desc
