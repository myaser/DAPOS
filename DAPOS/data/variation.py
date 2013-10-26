class Prefix(object):
    """docstring for Variation"""
    def __init__(self, prefix, **prefix_args):
        self.string = prefix
        self.type = prefix_args.get('classe', u"")
        self.desc = prefix_args.get('desc', u"").split('|')

    def __unicode__(self):
        return unicode(self.string)

    def __eq__(self, assignee):
        if isinstance(assignee, Prefix):
            return self.string == assignee.string
        return assignee == self.string


class Suffix(object):
    """docstring for Suffix"""
    def __init__(self, suffix, **suffix_args):
        self.string = suffix
        self.type = suffix_args.get('classe', u"")
        self.desc = suffix_args.get('desc', u"").split('|')

    def __unicode__(self):
        return unicode(self.string)

    def __eq__(self, assignee):
        if isinstance(assignee, Suffix):
            return self.string == assignee.string
        return assignee == self.string
