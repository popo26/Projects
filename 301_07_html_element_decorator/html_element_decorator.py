
from curses import wrapper


def tagify(*args):
    def decorator(function):
        def wrapper():
            return function
        return wrapper
    return decorator


    