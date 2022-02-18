from django.http import HttpRequest, HttpResponse
from ..Base import BaseView

class UserView(BaseView):
    
    def get(self, req: HttpRequest, userid: int, *args, **kwargs) -> HttpResponse:
        return HttpResponse(f"User {userid} OK")
