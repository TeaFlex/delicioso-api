from django.urls import path
from . import routes
from . import views

urlpatterns = [
    path("infos/", views.get_infos),
]
