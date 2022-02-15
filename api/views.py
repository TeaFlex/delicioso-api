import os
from subprocess import check_output
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse

def get_infos(req: HttpRequest):
    infos = {
        "pid": os.getpid(),
        "uptime": check_output(["ps", "-o", "etime", "-p", str(os.getpid()), "--no-headers"]).decode("UTF-8").strip(),
        "version": os.getenv('API_VERSION')
    }
    return JsonResponse(infos)

def get_home(req: HttpRequest):
    return HttpResponse()