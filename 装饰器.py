import time


def decorator():
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            print('Decorator:' + str(time.time()))
            print(time.time())
            return func(*args, **kwargs)
        return wrapper
    return inner_decorator


@decorator()
def f1(func_name):
    print('This is a function name: %s' % func_name)


print(f1('f1'))
