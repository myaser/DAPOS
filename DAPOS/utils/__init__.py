from functools import partial, wraps
from itertools import chain

import memcache
cache = memcache.Client(['127.0.0.1:11211'], debug=0)


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)
