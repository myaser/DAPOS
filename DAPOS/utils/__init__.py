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


def _get_or_cache(key, fn, *args, **kwargs):
    @wraps(fn)
    def wrapper(*arg, **kwargs):
        if cache.get(key):
            return cache.get(key)

        result = fn(*arg, **kwargs)
        cache.set(key, result)
        return result

    return wrapper

get_or_cache = lambda key: partial(_get_or_cache, key)


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)
