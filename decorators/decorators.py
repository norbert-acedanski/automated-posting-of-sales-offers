import time
from typing import Union


def delay_decorator(delay: Union[float, int]):
    def wrap(function):
        time.sleep(delay)

        def wrapped_function(*args, **kwargs):
            function(*args, **kwargs)
            time.sleep(delay)
        return wrapped_function
    return wrap
