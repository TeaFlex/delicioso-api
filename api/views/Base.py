from django.http import HttpRequest, HttpResponse
from abc import ABC
from django.views import View

class BaseView(View, ABC):

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
        return HttpResponse(status=405)
