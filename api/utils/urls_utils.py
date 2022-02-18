from django.urls import include

def include_url_file(view_module: str):
    return include(f"api.views.{view_module}.urls")