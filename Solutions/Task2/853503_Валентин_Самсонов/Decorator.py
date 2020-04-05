from functools import wraps

def cache(function):
    cached = {}
    @wraps(function)
    def wrapper(*args):
        try:
            return cached[args]
        except KeyError:
            ar = function(*args)
            cached[args] = ar
            return ar
    return wrapper

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(20))
print(fib(10))
