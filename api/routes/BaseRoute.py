from django.shortcuts import render
from django.http import HttpResponse
from abc import ABC

class BaseRoute(ABC):

    _prefix: str

    def __init__(self, prefix: str):
        self._prefix = prefix

    def get_prefix(self) -> str:
        return self._prefix

    def test(self):
        return HttpResponse(self._prefix+" OK")