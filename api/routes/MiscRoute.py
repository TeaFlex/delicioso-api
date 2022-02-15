import os
from django.http import HttpResponse, JsonResponse, HttpRequest
from .BaseRoute import BaseRoute
from subprocess import check_output

class MiscRoute(BaseRoute):
    def __init__(self):
        super().__init__("misc")

    def get_infos(req: HttpRequest) -> HttpResponse:
        infos = {
            "pid": os.getpid(),
            "uptime": check_output(["ps", "-o", "etime", "-p", str(os.getpid()), "--no-headers"]).decode("UTF-8").strip(),
            "version": os.getenv('API_VERSION')
        }
        return JsonResponse(infos)
