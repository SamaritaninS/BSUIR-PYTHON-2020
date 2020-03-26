def cached(func):
    previous_args = [None, None]
    def wrapper(*args, **kwargs):
        if (previous_args[0] == args):
            returned = previous_args[1]
            return returned
        else:
            previous_args.clear()
            previous_args.append(args)
            print("Result of operation: ")
            previous_args.append(func(*args, **kwargs))
            returned = previous_args[1]
            return returned

    return wrapper


@cached
def add(a, b):
    return a + b


@cached
def multi(a, b):
    return a * b


@cached
def sub(a, b):
    return a - b


print(add(5, 10))
print(multi(3, 2))
print(sub(10, 8))
