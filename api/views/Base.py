from django.http import HttpRequest, HttpResponse
from abc import ABC
from django.views import View

class BaseView(View, ABC):

    _prefix: str

    @classmethod
    def get_prefix(cls) -> str:
        com_pre = f"{cls._prefix}/"
        if(len(com_pre) == 1):
            com_pre = ""
        return com_pre

    def get(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return self.generic(req, *args, **kwargs)

    def head(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return self.generic(req, *args, **kwargs)

    def post(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return self.generic(req, *args, **kwargs)

    def options(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return self.generic(req, *args, **kwargs)

    def delete(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return self.generic(req, *args, **kwargs)

    def put(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return self.generic(req, *args, **kwargs)

    def patch(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return self.generic(req, *args, **kwargs)

    def generic(self, req: HttpRequest , *args, **kwargs) -> HttpResponse:
        return HttpResponse(f"{req.method} on {self._prefix}/ OK")