from django.urls import path, include

from api.views.misc.Info import InfoView

urlpatterns = [
    path("", InfoView.as_view()),
]
