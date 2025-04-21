from typing import Callable
from functools import wraps

unique_calls = {}


def cache(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> int:
        func_call = (func, args, tuple(sorted(kwargs.items())))

        if func_call in unique_calls:
            print("Getting from cache")
            return unique_calls[func_call]
        print("Calculating new result")
        unique_calls[func_call] = func(*args, **kwargs)

        return unique_calls[func_call]

    return wrapper
