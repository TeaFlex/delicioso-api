import os
from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView
from subprocess import check_output

class InfoView(APIView):

    def get(self, *args, **kwargs) -> HttpResponse:
        infos = {
            "pid": os.getpid(),
            "uptime": check_output(["ps", "-o", "etime", "-p", str(os.getpid()), "--no-headers"]).decode("UTF-8").strip(),
            "version": os.getenv('API_VERSION')
        }
        return JsonResponse(infos)
