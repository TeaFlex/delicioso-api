from django.http import HttpRequest, HttpResponse
from ..Base import BaseView

class AuthView(BaseView):
    
    def post(self, req: HttpRequest, *args, **kwargs) -> HttpResponse:
        return HttpResponse("OK")
