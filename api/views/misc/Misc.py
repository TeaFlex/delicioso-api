import os
from sys import prefix
from django.http import HttpResponse, JsonResponse, HttpRequest
from ..Base import BaseView
from subprocess import check_output

class MiscView(BaseView):

    _prefix = ""

    def get(self, req: HttpRequest) -> HttpResponse:
        infos = {
            "pid": os.getpid(),
            "uptime": check_output(["ps", "-o", "etime", "-p", str(os.getpid()), "--no-headers"]).decode("UTF-8").strip(),
            "version": os.getenv('API_VERSION')
        }
        return JsonResponse(infos)
