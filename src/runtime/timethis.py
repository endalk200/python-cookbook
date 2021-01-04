"""
Python function profiler.

function decorator to profile or time function execution. This decorator
can be used by importing the decorator and wrapping it like this

@timethis
def timed_function():
    print("This function is timed")
"""

import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()

        # You can either print out the execution time or log it to a file
        print('{}.{} : {}s'.format(func.__module__, func.__name__, end-start))
        return r
    return wrapper

if __name__ == '__main__':

    @timethis
    def countdown(n):
        while n > 0:
            n -= 1

    # call the countdown function which is decorated using timethis decorator
    countdown(10000000)