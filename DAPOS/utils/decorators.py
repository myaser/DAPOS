from functools import update_wrapper


def method_decorator(decorator):
    """
    Converts a function decorator into a method decorator
    """
    # 'func' is a function at the time it is passed to _dec, but will eventually
    # be a method of the class it is defined it.
    def _dec(func):
        def _wrapper(self, *args, **kwargs):
            @decorator
            def bound_func(*args2, **kwargs2):
                return func(self, *args2, **kwargs2)
            # bound_func has the signature that 'decorator' expects i.e.  no
            # 'self' argument, but it is a closure over self so it can call
            # 'func' correctly.
            return bound_func(*args, **kwargs)
        # In case 'decorator' adds attributes to the function it decorates, we
        # want to copy those. We don't have access to bound_func in this scope,
        # but we can cheat by using it on a dummy function.
        @decorator
        def dummy(*args, **kwargs):
            pass
        update_wrapper(_wrapper, dummy)
        # Need to preserve any existing attributes of 'func', including the name.
        update_wrapper(_wrapper, func)

        return _wrapper
    update_wrapper(_dec, decorator)
    # Change the name to aid debugging.
    _dec.__name__ = 'method_decorator(%s)' % decorator.__name__
    return _dec
