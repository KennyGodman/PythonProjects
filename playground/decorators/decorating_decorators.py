import functools
import time


def hello():
    return "Hello world"

def decorate(func):
    @functools.wraps(func)
    def wrap(arg, **kwargs):
        print("I am a decorator")
        f = (func(arg, **kwargs))
        print("I am after decorator")
        return f
    return wrap

def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function")


# syntatic sugar
@decorate
def hello(name):
    return f"Hello {name}"

@decorate
def add(x,y):
    """

    :param x:
    :param y:
    :return:
    """
    return x + y


hello = decorate(hello)
hello("Godman")

print(add.__name__)
print(add.__doc__)