from enum import Enum
from typing import Any, Callable
from django.http import HttpRequest, HttpResponse

class HttpMethod(Enum):
    GET = 0
    POST = 1
    PUT = 2
    PATCH = 3
    DELETE = 4
    HEAD = 5
    OPTIONS = 6
    TRACE = 7

def method(method):
    def inner(f, *args):
        print(args)
        def wrapper(self, *args):
            # setattr(args[0], method.name.lower(), f)
            print(method, f, self)
            return f(self, *args)
        return wrapper
    return inner