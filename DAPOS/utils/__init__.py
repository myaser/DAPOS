from functools import partial, wraps

import memcache
cache = memcache.Client(['127.0.0.1:11211'], debug=0)


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
